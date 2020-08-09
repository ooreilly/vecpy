import vecpy


def pow(expr: vecpy.base.Expr, exponent: float):
    """
    Apply the `pow` function to a VecPy Expression.

    Args:
        expr: VecPy expression
        exponent: Exponent 

    Returns:
        VecPy function

    """
    return vecpy.function("pow", expr, exponent)
