import vecpy


def sin(expr: vecpy.base.Expr):
    """
    Apply the `sin` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("sin", expr)
