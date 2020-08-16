import vecpy


def sqrt(expr: vecpy.base.Expr):
    """
    Apply the `sqrt` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("sqrt", expr)
