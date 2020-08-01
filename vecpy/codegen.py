import numpy as np
import vecpy as vp

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

def check_size(arrays):
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
    if isinstance(expr, vp.Array):
        if expr not in arrays:
            arrays.append(expr)
    elif isinstance(expr, vp.Expr):
        __get_arrays(expr.a, arrays)
        __get_arrays(expr.b, arrays)
