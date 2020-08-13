import vecpy as vp
import numpy as np
import pytest


def test_array():

    a = vp.base.array.dummy("a")
    a.noconst()
    a.norestrict()
    assert vp.base.codegen.get_signature([a]) == "double *a"
    a.const()
    a.restrict()
    assert vp.base.codegen.get_signature([a]) == "const double *__restrict__ a"
    assert str(a) == "a"
    assert a.repr() == "Array"

    
def test_copy():
    a = np.ones(10)
    va = vp.to_vecpy(a)
    vb = va.copy()
    assert va.shape == vb.shape
    assert va.dtype == vb.dtype
    assert va.label != vb.label
    b = vb.get()
    assert np.all(np.equal(a, b))
