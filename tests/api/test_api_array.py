import numpy as np
import vecpy as vp
import pycuda.autoinit
import pycuda.driver as cuda
import pytest


def test_array():

    a = np.ones((100,))
    va = vp.copy(a)
    b = a.copy()
    cuda.memcpy_dtoh(b, va.x)
    assert np.all(np.equal(a, b))

    a = np.zeros((100,))
    va = vp.zeros_like(a)
    b = a.copy()
    cuda.memcpy_dtoh(b, va.x)
    assert np.all(np.equal(a, b))

    a = np.ones((100,))
    d_a = cuda.mem_alloc(a.nbytes)
    cuda.memcpy_htod(d_a, a)
    va = vp.reference(a, d_a)
    h_a = np.zeros((100,))
    cuda.memcpy_dtoh(h_a, va.x)
    assert np.all(np.equal(h_a, a))
