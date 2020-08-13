import vecpy as vp
import pytest

va = vp.base.array.dummy("a")
vb = vp.base.array.dummy("b")

def test_cache():
    expr = va + vb
    src = lambda: """
          __global__ void test(int a) {

          }
          """
    fcn = vp.base.cache.cache(expr, "test", src)

    # Already added to cache
    with pytest.raises(ValueError) : vp.base.cache.insert(expr, "test", src)

    # Retrieve from cache
    fcn2 = vp.base.cache.cache(expr, "test", src)

    assert fcn == fcn2

    vp.base.cache.flush()

