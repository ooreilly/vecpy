import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import vecpy as vp


a = np.random.randn(int(1e6))
b = np.random.randn(int(1e6))
ans = np.zeros_like(a)


def test_elementwise():
    va = vp.to_vecpy(a)
    vb = vp.to_vecpy(b)
    vout = vp.to_vecpy(ans)

    # sqrt(a**2 + b**2)
    def test_function(fcn, a, b): return fcn(a**2 + b**2)
    vp.elementwise(vout, test_function(vp.sqrt, va, vb))
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function(np.sqrt, a, b))

    # cos((a+b)*(a-b))
    def test_function(fcn, a, b): return fcn((a+b)*(a-b))
    vp.elementwise(vout, test_function(vp.cos, va, vb))
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function(np.cos, a, b))

    # scalar
    def test_function(): return 1.0
    vp.elementwise(vout, test_function())
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function())
