import vecpy as vp
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
