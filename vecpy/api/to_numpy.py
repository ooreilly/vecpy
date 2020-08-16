import numpy
import vecpy
import pycuda
import pycuda.driver as cuda

def to_numpy(array: vecpy.base.Array) -> numpy.ndarray:
    """

    Transfer a VecPy array to the CPU.

    Args:
        array: Input VecPy array

    Returns:
        A NumPy array that contains a copy of the VecPy array stored on the CPU.


    """
    out = numpy.ndarray(array.shape).astype(array.dtype)
    cuda.memcpy_dtoh(out, array.x)
    return out
