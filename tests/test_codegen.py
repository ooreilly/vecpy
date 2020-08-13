import numpy as np
import vecpy as vp
import pytest as pt
from vecpy.base.codegen import get_arrays, to_ctype_str, get_args, get_signature, isconsistent

a = np.random.randn(100).astype(np.float32)
b = np.random.randn(100).astype(np.float32)
c = np.random.randn(10).astype(np.float32)
va = vp.base.Array(a, "va", "a")
vb = vp.base.Array(b, "vb", "b")
vc = vp.base.Array(c, "vc", "c")


def test_to_ctype_str():
    assert to_ctype_str(np.int8) == "int8_t"
    assert to_ctype_str(np.int16) == "int16_t"
    assert to_ctype_str(np.int32) == "int32_t"
    assert to_ctype_str(np.int64) == "int64_t"
    assert to_ctype_str(np.uint8) == "uint8_t"
    assert to_ctype_str(np.uint16) == "uint16_t"
    assert to_ctype_str(np.uint32) == "uint32_t"
    assert to_ctype_str(np.uint64) == "uint64_t"
    assert to_ctype_str(np.float32) == "float"
    assert to_ctype_str(np.float64) == "double"
    assert to_ctype_str(np.complex64) == "float complex"
    assert to_ctype_str(np.complex128) == "double complex"
    with pt.raises(ValueError):
        to_ctype_str(None)


def test_get_arrays():
    arrays = get_arrays(None)
    assert arrays == []

    arrays = get_arrays(va)
    assert arrays == [va]

    arrays = get_arrays(va + vb)
    assert arrays == [va, vb]

    arrays = get_arrays(2 + va + vb)
    assert arrays == [va, vb]

    arrays = get_arrays(2 + 2 * va + 3 * vb)
    assert arrays == [va, vb]

    arrays = get_arrays(2 + 2 * va + 3 * vb * va)
    assert arrays == [va, vb]

    arrays = get_arrays(2 + 2 * va + 3 * vb * va - vb ** va)
    assert arrays == [va, vb]


def test_args():
    arrays = get_arrays(2 + 2 * va + 3 * vb * va - vb ** va)
    args = get_args(arrays)
    assert "va" in args and "vb" in args and len(args) == 2


def test_get_signature():
    arrays = get_arrays(va + vb)
    sig = get_signature(arrays)
    assert sig == "float *__restrict__ a, float *__restrict__ b"

    out = vp.base.Array(b, "vb", "out")
    out.const()
    arrays = get_arrays(out + va + vb)
    sig = get_signature(arrays)
    assert sig == "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b"

    r = vp.base.Array(b, "d_r", "r")
    r.norestrict()
    arrays = get_arrays(out + va + vb + out + r)
    sig = get_signature(arrays)
    assert sig == \
        "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b, float *r"


def test_check_size():

    assert isconsistent([va, vb]) == True
    assert isconsistent([va, vc]) == False


def test_vecpify():

    assert isinstance(vp.base.codegen.vecpify(0.2), vp.base.Scalar)
    with pt.raises(ValueError) : vp.base.codegen.vecpify(np.zeros(2))
