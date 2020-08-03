import vecpy as vp

def sum(expr: vp.base.Expr, deviceID=0) -> float:
    return vp.kernels.sum(expr, deviceID)
