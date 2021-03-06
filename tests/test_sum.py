import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import vecpy as vp

a = np.random.randn(int(1e6))
b = np.random.randn(int(1e6))
ans = np.zeros_like(a)


def test_sum():
    va = vp.to_vecpy(a)
    vb = vp.to_vecpy(b)

    # sum(sqrt(a**2 + b**2))
    def test_function(fcn, a, b): return fcn(a**2 + b**2)
    vp_ans = vp.sum(test_function(vp.sqrt, va, vb)).get()
    np_ans = np.sum(test_function(np.sqrt, a, b))
    assert np.isclose(vp_ans, np_ans)

    # sum(cos((a+b)*(a-b)))
    def test_function(fcn, a, b): return fcn((a+b)*(a-b))
    vp_ans = vp.sum(test_function(vp.cos, va, vb)).get()
    np_ans = np.sum(test_function(np.cos, a, b))
    assert np.isclose(vp_ans, np_ans)

    # Sum of exponential functions
    def test_function(fcn, a, b): return fcn(a, b)
    print(test_function(vp.pow, va, va).ccode("i"))
    vp_ans = vp.sum(test_function(vp.pow, 0.2, vb)).get()
    np_ans = np.sum(test_function(lambda u, v : u ** v, 0.2, b))
    assert np.isclose(vp_ans, np_ans)

    # scalar, expected sum = 1.0
    def test_function(): return 1.0
    vp_ans = vp.sum(test_function()).get()
    np_ans = np.sum(test_function())
    assert np.isclose(vp_ans, np_ans)

