import numpy as np
import vecpy as vp
import hashlib


def to_ctype_str(dtype):
    dtypes = [np.int8,
              np.int16,
              np.int32,
              np.int64,
              np.uint8,
              np.uint16,
              np.uint32,
              np.uint64,
              np.intp,
              np.uintp,
              np.float32,
              np.float64,
              np.complex64,
              np.complex128]
    ctypes = ["int8_t",
              "int16_t",
              "int32_t",
              "int64_t",
              "uint8_t",
              "uint16_t",
              "uint32_t",
              "uint64_t",
              "intptr_t",
              "uintptr_t",
              "float",
              "double",
              "float complex",
              "double complex"]

    for i, dt in enumerate(dtypes):
        if dt == dtype:
            return ctypes[i]
    raise ValueError("Unknown dtype")


def get_arrays(expr):
    arr = []
    __get_arrays(expr, arr)
    return arr


def get_args(arrays):
    args = []
    for ai in arrays:
        args.append(ai.x)
    return args


def get_signature(arrays):
    sig = []
    for ai in arrays:
        sig.append(ai.cdecl())
    return ", ".join(sig)


def get_size(shape):
    size = 1
    for si in shape:
        size *= si
    return size


def isconsistent(arrays):
    expected = 0
    for ai in arrays:
        if expected == 0:
            expected = ai.shape
        if ai.shape != expected:
            return False
    return True


def const(isconst):
    if isconst == True:
        return "const "
    else:
        return ""


def restrict(isrestrict):
    if isrestrict == True:
        return "__restrict__ "
    else:
        return ""


def __get_arrays(expr, arrays=[]):
    if isinstance(expr, vp.base.array.Array):
        if expr not in arrays:
            arrays.append(expr)
    elif isinstance(expr, vp.base.functions.Function):
        __get_arrays(expr.expr, arrays)
        for arg in expr.args:
            __get_arrays(arg, arrays)
    elif isinstance(expr, vp.base.Expr):
        __get_arrays(expr.a, arrays)
        __get_arrays(expr.b, arrays)


def pycode(expr, i=None):
    return expr.pycode(i)


def ccode(expr, i=None):
    return expr.ccode(i)


def eval(expr, i=None):
    return expr.eval(i)


def vecpify(arg):
    if isinstance(arg, vp.base.Expr):
        return arg
    else:
        # Check if array or scalar
        try:
            arg.shape
        except:
            return vp.base.Scalar(arg)

        raise ValueError(
            "Non-VecPy Array detected in expression. Convert array first using Array()")
