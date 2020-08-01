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

    test_function = lambda a, b : (a**2 + b**2 + (a + b) / 2 + (a / 2 - b / 4) / 2 )**2

    vp.elementwise(vout, test_function(va, vb))
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, test_function(a, b))
