import vecpy


def exp(expr: vecpy.base.Expr):
    """
    Apply the `exp` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("exp", expr)
