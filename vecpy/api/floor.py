import vecpy


def floor(expr: vecpy.base.Expr):
    """
    Apply the `floor` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("floor", expr)
