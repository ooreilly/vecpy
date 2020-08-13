import vecpy as vp
import numpy as np
from pycuda.compiler import SourceModule
from pycuda.autoinit import context
import pycuda.driver as cuda
from vecpy.base.codegen import get_arrays, get_args, get_size, isconsistent, get_signature


def elementwise(expr, out=None, deviceID=0, options=["--use_fast_math"]):
    arrays = get_arrays(expr)
    for ai in arrays:
        ai.const()


    if out is None:
        out = arrays[0].copy()

    arrays.append(out)
    assert arrays != []
    assert isconsistent(arrays)
    args = get_args(arrays)
    signature = get_signature(arrays)
    size = np.int64(get_size(out.shape))
    mp = cuda.device_attribute.MULTIPROCESSOR_COUNT
    num_blocks = 8 * cuda.Device(deviceID).get_attribute(mp)
    source = lambda: __elementwise_source(signature, out.label, expr)
    fcn = vp.base.cache.cache(expr, "elementwise_kernel", source, options)
    fcn(*args, size, block=(256, 1, 1), grid=(num_blocks, 1, 1))

    return out


def __elementwise_source(signature, out, expr):
    try:
        code = expr.ccode("i")
    except:
        code = str(expr)
    return """
            __global__ void elementwise_kernel(%s, const int N)
            {
              const int idx = threadIdx.x + blockIdx.x * blockDim.x;
              for (int i = idx; i < N; i += blockDim.x * gridDim.x) {
                %s[i] = %s;
              }
            }
            """ % (signature, out, code)
