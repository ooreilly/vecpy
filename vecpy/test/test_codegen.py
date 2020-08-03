import numpy as np
import vecpy as vp
import pytest as pt
from vecpy.base.codegen import get_arrays, to_ctype_str, get_args, get_signature

a = np.random.randn(100).astype(np.float32)
b = np.random.randn(100).astype(np.float32)
d_a = vp.base.Array(a, "d_a", "a")
d_b = vp.base.Array(b, "d_b", "b")

def test_to_ctype_str():
    assert to_ctype_str(np.int8) ==  "int8_t"
    assert to_ctype_str(np.int16) ==  "int16_t"
    assert to_ctype_str(np.int32) ==  "int32_t"
    assert to_ctype_str(np.int64) ==  "int64_t"
    assert to_ctype_str(np.uint8) ==  "uint8_t"
    assert to_ctype_str(np.uint16) ==  "uint16_t"
    assert to_ctype_str(np.uint32) ==  "uint32_t"
    assert to_ctype_str(np.uint64) ==  "uint64_t"
    assert to_ctype_str(np.float32) ==  "float"
    assert to_ctype_str(np.float64) ==  "double"
    assert to_ctype_str(np.complex64) ==  "float complex"
    assert to_ctype_str(np.complex128) ==  "double complex"
    with pt.raises(ValueError) : to_ctype_str(None)


def test_get_arrays():
    arrays = get_arrays(None)
    assert arrays == []

    arrays = get_arrays(d_a)
    assert arrays == [d_a]

    arrays = get_arrays(d_a + d_b)
    assert arrays == [d_a, d_b]

    arrays = get_arrays(2 + d_a + d_b)
    assert arrays == [d_a, d_b]

    arrays = get_arrays(2 + 2 * d_a + 3 * d_b)
    assert arrays == [d_a, d_b]

    arrays = get_arrays(2 + 2 * d_a + 3 * d_b * d_a)
    assert arrays == [d_a, d_b]

    arrays = get_arrays(2 + 2 * d_a + 3 * d_b * d_a - d_b ** d_a)
    assert arrays == [d_a, d_b]


def test_args():
    arrays = get_arrays(2 + 2 * d_a + 3 * d_b * d_a - d_b ** d_a)
    args = get_args(arrays)
    assert "d_a" in args and "d_b" in args and len(args) == 2


def test_get_signature():
    arrays = get_arrays(d_a + d_b)
    sig = get_signature(arrays)
    assert sig == "float *__restrict__ a, float *__restrict__ b"

    out = vp.base.Array(b, "d_b", "out")
    out.const()
    arrays = get_arrays(out + d_a + d_b)
    sig = get_signature(arrays)
    assert sig == "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b"

    r = vp.base.Array(b, "d_r", "r")
    r.norestrict()
    arrays = get_arrays(out + d_a + d_b + out + r)
    sig = get_signature(arrays)
    assert sig == \
            "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b, float *r"
