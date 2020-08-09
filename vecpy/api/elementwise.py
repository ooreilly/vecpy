import vecpy

def elementwise(out: vecpy.base.Array, expr: vecpy.base.Expr, deviceID: int=0):
    """

    Applies the element wise operation to the expression `expr` and stores the result to
    the device array `out`. 

    Args:
        out: output argument to assign to.
        expr: VecPy expression to compute.
        deviceID(optional): device ID to use.

    Example:
        
        Square each value, $y_i = x_i^2$

        >>> 
        >>> import numpy as np
        >>> x = np.arange(10)
        >>> # Copy to GPU
        >>> vx = vecpy.to_vecpy(x)
        >>> # Zero-initialize output array
        >>> vy = vecpy.zeros_like(x)
        >>> # Compute x^2 elementwise and store result in vy
        >>> vecpy.elementwise(vy, vx ** 2)
        >>> # Copy result to CPU
        >>> y = vecpy.to_numpy(vy)
        >>> y
        array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

    """
    vecpy.kernels.elementwise(out, expr, deviceID)
