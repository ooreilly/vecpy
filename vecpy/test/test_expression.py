import numpy as np
import vecpy as vp

a = np.random.randn(100).astype(np.float32)
b = np.random.randn(100).astype(np.float32)
d_a = vp.Array(a, None, "a")
d_b = vp.Array(b, None, "b")

def test_repr():
    assert (d_a + d_b).repr() == "Add(a, b)"
    assert (d_a * d_b).repr() == "Mul(a, b)"
    assert (d_a - d_b).repr() == "Sub(a, b)"
    assert (d_a / d_b).repr() == "Div(a, b)"

def test_str_expressions():
    assert str(d_a + d_b) == "(a) + (b)"
    assert str(d_a - d_b) == "(a) - (b)"
    assert str(d_a * d_b) == "(a) * (b)"
    assert str(d_a / d_b) == "(a) / (b)"
    assert str(d_a ** d_b) == "(a) ** (b)"
    assert str(-2.0 * d_a) == "(-2.0) * (a)"

def test_ccode_expressions():
    assert (d_a + d_b).ccode() == "(a) + (b)"
    assert (d_a - d_b).ccode() == "(a) - (b)"
    assert (d_a * d_b).ccode() == "(a) * (b)"
    assert (d_a / d_b).ccode() == "(a) / (b)"
    assert (d_a ** d_b).ccode() == "pow((a), (b))"

    assert (d_a + d_b).ccode("i") == "(a[i]) + (b[i])"
    assert (d_a - d_b).ccode("i") == "(a[i]) - (b[i])"
    assert (d_a * d_b).ccode("i") == "(a[i]) * (b[i])"
    assert (d_a / d_b).ccode("i") == "(a[i]) / (b[i])"
    assert (d_a ** d_b).ccode("i") == "pow((a[i]), (b[i]))"

    assert (- d_a).ccode("i") == "(-1.0) * (a[i])"
    assert (- 2.0 * d_a).ccode("i") == "(-2.0) * (a[i])"

    # Test constants
    c = 2.0
    assert (c * d_a).ccode() == "(2.0) * (a)"
    assert (d_a * c).ccode() == "(a) * (2.0)"
    assert (c + d_a).ccode() == "(2.0) + (a)"
    assert (d_a + c).ccode() == "(a) + (2.0)"
    assert (c - d_a).ccode() == "(2.0) - (a)"
    assert (d_a - c).ccode() == "(a) - (2.0)"

    assert (c * d_a).ccode("i") == "(2.0) * (a[i])"
    assert (d_a * c).ccode("i") == "(a[i]) * (2.0)"
    assert (c + d_a).ccode("i") == "(2.0) + (a[i])"
    assert (d_a + c).ccode("i") == "(a[i]) + (2.0)"
    assert (c - d_a).ccode("i") == "(2.0) - (a[i])"
    assert (d_a - c).ccode("i") == "(a[i]) - (2.0)"
    assert (d_a ** c).ccode("i") == "pow((a[i]), (2.0))"
    assert (c ** d_a).ccode("i") == "pow((2.0), (a[i]))"

    # Test distributive law
    assert (c * (d_a + d_b)).ccode("i") == "(2.0) * ((a[i]) + (b[i]))"
