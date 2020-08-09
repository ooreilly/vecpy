import numpy
import vecpy
import pycuda
import pycuda.driver as cuda


def zeros_like(array: numpy.ndarray, label: str = None) -> vecpy.base.Array:
    """
    Zero-initialize a VecPy array of the same shape and type as a NumPy array.

    Args:
        array: Input NumPy array
        label(optional): Label to use for the VecPy in symbolic expressions

    Returns:
        A zero-initialized VecPy array of the same shape and type as the NumPy array.


    """
    return vecpy.base.Array(array, cuda.to_device(numpy.zeros_like(array).astype(array.dtype)), 
                            label)
