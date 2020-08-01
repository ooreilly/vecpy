import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import vecpy as vp


a = np.random.randn(1000)
b = np.random.randn(1000)
ans = np.zeros_like(a)

def test_elementwise():
    va = vp.Array(a, cuda.to_device(a), "a")
    vb = vp.Array(b, cuda.to_device(b), "b")
    vout = vp.Array(ans, cuda.to_device(ans), "out")

    vp.elementwise(vout, va * vb ** 2 + 1)
    cuda.memcpy_dtoh(ans, vout.x)
    assert np.allclose(ans, a * b ** 2 + 1)
