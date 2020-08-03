import numpy as np
import vecpy as vp
import pytest

a = np.random.randn(100).astype(np.float32)
b = np.random.randn(100).astype(np.float32)
d_a = vp.base.Array(a, None, "a")
d_b = vp.base.Array(b, None, "b")

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
    assert str(-2.0 / d_a) == "(-2.0) / (a)"

def test_codegens():
    assert vp.base.codegen.ccode(d_a + d_b) == "(a) + (b)"
    assert vp.base.codegen.pycode(d_a + d_b) == "(a) + (b)"
    with pytest.raises(NotImplementedError) : vp.base.codegen.eval(d_a + d_b, "?")

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
    assert (d_a ** c).ccode("i") == "(a[i]) * (a[i])"
    assert (c ** d_a).ccode("i") == "pow((2.0), (a[i]))"

    # Test distributive law
    assert (c * (d_a + d_b)).ccode("i") == "(2.0) * ((a[i]) + (b[i]))"

    # Check that integer power expressions are auto-expanded
    assert (d_a ** 2 + d_a ** 3).ccode("i") == "((a[i]) * (a[i])) + ((a[i]) * (a[i]) * (a[i]))"


def test_functions():
    assert vp.sqrt(d_a).ccode("i") == "sqrt(a[i])"
    assert vp.log(d_a).ccode("i") == "log(a[i])"
    assert vp.cos(d_a).ccode("i") == "cos(a[i])"
    assert vp.sin(d_a).ccode("i") == "sin(a[i])"
    assert vp.exp(d_a).ccode("i") == "exp(a[i])"
    assert vp.pow(d_a, 2).ccode("i") == "pow(a[i], 2)"
    assert vp.function("test", d_a, 2).ccode("i") == "test(a[i], 2)"
