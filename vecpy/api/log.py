import vecpy


def log(expr: vecpy.base.Expr):
    """
    Apply the `log` function to a VecPy Expression.

    Args:
        expr: VecPy expression

    Returns:
        VecPy function

    """
    return vecpy.function("log", expr)
