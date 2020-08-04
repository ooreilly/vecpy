import vecpy

def elementwise(out: vecpy.base.Array, expr: vecpy.base.Expr, deviceID: int=0):
    """

    Applies the element wise operation to the expression `expr` and stores the result to
    the device array `out`. 

    Args:
        out: output argument to assign to.
        expr: VecPy expression to compute.
        deviceID: device ID to use.

    Example:
        
        Square each value, $y_i = x_i^2$

        >>> 
        >>> import numpy as np
        >>> x = np.arange((10,))
        >>> # Copy to GPU
        >>> vx = vecpy.copy(x)
        >>> # Zero-intialize output array
        >>> vy = vecpy.zero_like(x)
        >>> # Compute x^2 elementwise and store result in vy
        >>> vecpy.elementwise(vy, x ** 2)
        >>> # Copy result to CPU
        >>> y = vecpy.copy(vy)
        >>> y

    """
    vecpy.kernels.elementwise(out, expr, deviceID)
