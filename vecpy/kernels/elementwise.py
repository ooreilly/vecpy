import vecpy as vp
from pycuda.compiler import SourceModule
from pycuda.autoinit import context
import pycuda.driver as cuda
from vecpy.base.codegen import get_arrays, get_args, get_size, check_size, get_signature


def elementwise(out, expr, deviceID=0):
    arrays = get_arrays(expr)
    for ai in arrays:
        ai.const()
    arrays.append(out)

    assert arrays != []
    assert check_size(arrays)

    args = get_args(arrays)
    signature = get_signature(arrays)
    size = get_size(out.shape)
    src = __elementwise_source(signature, out.label, expr, size)
    options = ["-use_fast_math"]
    mod = SourceModule(src, options=options)
    mp = cuda.device_attribute.MULTIPROCESSOR_COUNT
    num_blocks = 8 * cuda.Device(deviceID).get_attribute(mp)
    fcn = mod.get_function("elementwise_kernel")
    fcn(*args, block=(256, 1, 1), grid=(num_blocks, 1, 1))


def __elementwise_source(signature, out, expr, N):
    try:
        code = expr.ccode("i")
    except:
        code = str(expr)
    return """
            __global__ void elementwise_kernel(%s)
            {
              const int idx = threadIdx.x + blockIdx.x * blockDim.x;
              for (int i = idx; i < %d; i += blockDim.x * gridDim.x) {
                %s[i] = %s;
              }
            }
            """ % (signature, N, out, code)
