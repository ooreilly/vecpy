import numpy as np
import vecpy as vp

a = np.random.randn(100).astype(np.float32)
va = vp.base.array.dummy("a")

def test_functions():
    assert str(vp.function("test", va, 2)) == "test(a, 2)"
    assert str(vp.sqrt(va)) == "sqrt(a)"
    assert str(vp.sin(va)) == "sin(a)"
    assert str(vp.cos(va)) == "cos(a)"
    assert str(vp.exp(va)) == "exp(a)"
    assert str(vp.log(va)) == "log(a)"
    assert str(vp.abs(va)) == "fabs(a)"
    assert str(vp.pow(va, 2)) == "pow(a, 2)"
    assert str(vp.floor(va)) == "floor(a)"
