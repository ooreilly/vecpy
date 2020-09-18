import vecpy

def sum(expr: vecpy.base.Expr, deviceID=0) -> float:
    """

    Return the sum of each value in a vector expression.

    Args:
        expr: VecPy expression to sum.
        deviceID(optional): device ID to use.

    Returns:
        The sum of the expression.

    Example:
        
        Compute the l2-norm, $\|x\| = \sqrt{\sum_i x_i^2}$

        >>> 
        >>> import numpy as np
        >>> x = np.ones(10)
        >>> # Copy to GPU
        >>> vx = vecpy.to_vecpy(x)
        >>> # Compute l2 norm
        >>> norm = vecpy.sum(vecpy.sqrt(vx ** 2))
        >>> norm.get()
        array([10.])



    """
    return vecpy.kernels.sum(expr, deviceID)
