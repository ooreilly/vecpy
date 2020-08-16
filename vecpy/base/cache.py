import vecpy as vp
from pycuda.compiler import SourceModule

"""

Cache for kernel compilation

The cache is a dictionary that stores the expression as keys, and the compiled source code as
values.

The keys are in the form "kernel_name:expression", where `expression` maps to the representation
obtained by calling repr(), i.e. `"Add(Array, Array)"`. 


"""

__cache = {}


def get(expr, kernel_name):
    """
    Return compiled function from cache.

    """
    repr = key(expr, kernel_name)
    if repr in __cache:
        return __cache[repr]
    return None


def key(expr, kernel_name):
    return (kernel_name + ":" + vp.base.codegen.vecpify(expr).repr()).encode()


def insert(expr, kernel_name, source, options=[]):
    repr = key(expr, kernel_name)
    if repr in __cache:
        raise ValueError("Source code already cached")
    else:
        mod = SourceModule(source, options=options)
        fcn = mod.get_function(kernel_name)
        __cache[repr] = fcn
        return fcn


def cache(expr, kernel_name, src, options=[]):
    fcn = get(expr, kernel_name)
    if fcn is None:
        fcn = insert(expr, kernel_name, src(), options)
    return fcn


def flush():
    __cache = {}
