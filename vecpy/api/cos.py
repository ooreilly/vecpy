import vecpy


def cos(expr: vecpy.base.Expr):
    """
    Apply the `cos` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("cos", expr)
