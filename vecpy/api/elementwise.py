import vecpy

def elementwise(out: vecpy.base.Array, expr: vecpy.base.Expr, deviceID: int=0):
    vecpy.kernels.elementwise(out, expr, deviceID)
