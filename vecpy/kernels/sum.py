import vecpy as vp
import numpy as np
from pycuda.compiler import SourceModule
from pycuda.autoinit import context
import pycuda.driver as cuda
from vecpy.base.codegen import get_arrays, isconsistent, get_args, get_signature, get_size

__device_sum_temp = 0


def sum(expr, deviceID=0):

    arrays = get_arrays(expr)
    for ai in arrays:
        ai.const()

    assert isconsistent(arrays)

    result = np.zeros((1,))
    vresult = vp.base.Array(result, cuda.to_device(result), "temp")
    arrays.append(vresult)

    args = get_args(arrays)
    signature = get_signature(arrays)
    N = get_size(arrays[0].shape)
    mp = cuda.Device(deviceID).get_attribute(
        cuda.device_attribute.MULTIPROCESSOR_COUNT)
    num_threads = cuda.Device(deviceID).get_attribute(
        cuda.device_attribute.MAX_THREADS_PER_BLOCK)
    blocks_per_SM = 2
    num_blocks = min(blocks_per_SM * mp, int((N - 1) /
                                             (blocks_per_SM * num_threads) + 1))

    src = __sum_source(signature, expr, N)
    options = ["-use_fast_math"]
    mod = SourceModule(src, options=options)

    fcn = mod.get_function("sum_kernel")
    fcn(*args, block=(num_threads, 1, 1), grid=(num_blocks, 1, 1))
    cuda.memcpy_dtoh(result, vresult.x)
    return result[0]


def __sum_source(signature, expr, N):
    try:
        code = expr.ccode("i")
    except:
        code = str(expr)
    src = """
            __global__ void sum_kernel(%s) {

                const int warpSize = 32;
                const int N = %s;
                int numThreads = blockDim.x;
                int numValuesPerBlockPerThread = (N - 1) / gridDim.x / numThreads + 1;
                int numValuesPerBlock = numValuesPerBlockPerThread * numThreads;
                int idx = threadIdx.x + blockIdx.x * numValuesPerBlock;
                int warpID = threadIdx.x / warpSize;
                int lane = threadIdx.x %% warpSize;
                int numWarps = numThreads / warpSize;

                double partialSum = 0.0;
                __shared__ double sPartialSum[1024];
                int end = idx + numValuesPerBlock;
                int iEnd = end > N ? N : end;
                for (int i = idx; i < iEnd; i += numThreads) {
                        partialSum += %s;
                }

                double val = partialSum;
                for (int i = 16; i > 0; i /= 2)
                        val += __shfl_down_sync(0xffffffff, val, i);

                if (lane == 0) sPartialSum[warpID] = val;

                __syncthreads();

                if (lane == 0 && warpID == 0) {
                        double blockSum = 0.0;
                        for (int i = 0; i < numWarps; ++i) {
                                blockSum += sPartialSum[i];
                        }

                        double val = atomicAdd(temp, blockSum);
                }
        } 
    """ % (signature, N, code)
    return src
