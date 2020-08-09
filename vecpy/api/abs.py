import vecpy


def abs(expr: vecpy.base.Expr):
    """
    Apply the `abs` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("fabs", expr)
