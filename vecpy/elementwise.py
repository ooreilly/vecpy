import vecpy as vp
from pycuda.compiler import SourceModule
from pycuda.autoinit import context
import pycuda.driver as cuda


def elementwise(out, expr):
    arrays = vp.get_arrays(expr)
    for ai in arrays:
        ai.const()
    arrays.append(out)
    assert arrays != set()
    assert vp.check_size(arrays)

    args = vp.get_args(arrays)
    signature = vp.get_signature(arrays)
    size = vp.get_size(out.shape)
    src = __elementwise_source(signature, out.label, expr, size)
    mod = SourceModule(src)
    mp = cuda.device_attribute.MULTIPROCESSOR_COUNT
    num_blocks = 8 * cuda.Device(0).get_attribute(mp)

    fcn = mod.get_function("elementwise_kernel")
    fcn(*args, block=(128, 1, 1), grid=(num_blocks, 1, 1))
    context.synchronize()


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
