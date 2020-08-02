import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import vecpy as vp

a = np.random.randn(int(1e6))
b = np.random.randn(int(1e6))
ans = np.zeros_like(a)

def test_sum():
    va = vp.Array(a, cuda.to_device(a))
    vb = vp.Array(b, cuda.to_device(b))

    # sum(sqrt(a**2 + b**2))
    test_function = lambda fcn, a, b : fcn(a**2 + b**2)
    vp_ans = vp.sum(test_function(vp.sqrt, va, vb))
    np_ans = np.sum(test_function(np.sqrt, a, b))
    assert np.isclose(vp_ans, np_ans)

    # sum(cos((a+b)*(a-b)))
    test_function = lambda fcn, a, b : fcn((a+b)*(a-b))
    vp_ans = vp.sum(test_function(vp.cos, va, vb))
    np_ans = np.sum(test_function(np.cos, a, b))
    assert np.isclose(vp_ans, np_ans)
