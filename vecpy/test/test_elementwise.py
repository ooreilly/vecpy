import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import vecpy as vp


a = np.random.randn(int(1e6))
b = np.random.randn(int(1e6))
ans = np.zeros_like(a)

def test_elementwise():
    va = vp.Array(a, cuda.to_device(a), "a")
    vb = vp.Array(b, cuda.to_device(b), "b")
    vout = vp.Array(ans, cuda.to_device(ans), "out")

    # sqrt(a**2 + b**2)
    test_function = lambda fcn, a, b : fcn(a**2 + b**2)
    vp.elementwise(vout, test_function(vp.sqrt, va, vb))
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function(np.sqrt, a, b))

    # cos((a+b)*(a-b))
    test_function = lambda fcn, a, b : fcn((a+b)*(a-b))
    vp.elementwise(vout, test_function(vp.cos, va, vb))
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function(np.cos, a, b))
