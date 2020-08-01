import numpy as np
import vecpy as vp
import pytest as pt

a = np.random.randn(100).astype(np.float32)
b = np.random.randn(100).astype(np.float32)
d_a = vp.Array(a, "d_a", "a")
d_b = vp.Array(b, "d_b", "b")

def test_to_ctype_str():
    assert vp.to_ctype_str(np.int8) ==  "int8_t"
    assert vp.to_ctype_str(np.int16) ==  "int16_t"
    assert vp.to_ctype_str(np.int32) ==  "int32_t"
    assert vp.to_ctype_str(np.int64) ==  "int64_t"
    assert vp.to_ctype_str(np.uint8) ==  "uint8_t"
    assert vp.to_ctype_str(np.uint16) ==  "uint16_t"
    assert vp.to_ctype_str(np.uint32) ==  "uint32_t"
    assert vp.to_ctype_str(np.uint64) ==  "uint64_t"
    assert vp.to_ctype_str(np.float32) ==  "float"
    assert vp.to_ctype_str(np.float64) ==  "double"
    assert vp.to_ctype_str(np.complex64) ==  "float complex"
    assert vp.to_ctype_str(np.complex128) ==  "double complex"
    with pt.raises(ValueError) : vp.to_ctype_str(None)


def test_get_arrays():
    arrays = vp.get_arrays(None)
    assert arrays == []

    arrays = vp.get_arrays(d_a)
    assert arrays == [d_a]

    arrays = vp.get_arrays(d_a + d_b)
    assert arrays == [d_a, d_b]

    arrays = vp.get_arrays(2 + d_a + d_b)
    assert arrays == [d_a, d_b]

    arrays = vp.get_arrays(2 + 2 * d_a + 3 * d_b)
    assert arrays == [d_a, d_b]

    arrays = vp.get_arrays(2 + 2 * d_a + 3 * d_b * d_a)
    assert arrays == [d_a, d_b]

    arrays = vp.get_arrays(2 + 2 * d_a + 3 * d_b * d_a - d_b ** d_a)
    assert arrays == [d_a, d_b]


def test_args():
    arrays = vp.get_arrays(2 + 2 * d_a + 3 * d_b * d_a - d_b ** d_a)
    args = vp.get_args(arrays)
    assert "d_a" in args and "d_b" in args and len(args) == 2


def test_get_signature():
    arrays = vp.get_arrays(d_a + d_b)
    sig = vp.get_signature(arrays)
    assert sig == "float *__restrict__ a, float *__restrict__ b"

    out = vp.Array(b, "d_b", "out")
    out.const()
    arrays = vp.get_arrays(out + d_a + d_b)
    sig = vp.get_signature(arrays)
    assert sig == "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b"

    r = vp.Array(b, "d_r", "r")
    r.norestrict()
    arrays = vp.get_arrays(out + d_a + d_b + out + r)
    sig = vp.get_signature(arrays)
    assert sig == \
            "const float *__restrict__ out, float *__restrict__ a, float *__restrict__ b, float *r"
