import vecpy as vp
import numpy as np
import pycuda.driver as cuda
from .expression import Expr

__count__ = 0


class Array(Expr):

    def __init__(self, host_array, device_array, label=None):
        if label is None:
            self.label = _label()
        else:
            self.label = label
        self.type = "Array"
        self.x = device_array
        self.dtype = host_array.dtype
        self.shape = host_array.shape
        self.nbytes = host_array.nbytes
        self.__restrict = True
        self.__const = False

    def const(self):
        self.__const = True

    def noconst(self):
        self.__const = False

    def restrict(self):
        self.__restrict = True

    def norestrict(self):
        self.__restrict = False

    def __str__(self):
        return "%s" % (self.label)

    def repr(self, i=None):
        return self.type

    def get(self):
        out = np.ndarray(self.shape, self.dtype)
        cuda.memcpy_dtoh(out, self.x)
        return out

    def copy(self):
        tmp = np.ndarray((1,))
        out = Array(tmp, None)
        out.nbytes = self.nbytes
        out.x = cuda.mem_alloc(self.nbytes)
        cuda.memcpy_dtod(out.x, self.x, out.nbytes)
        out.dtype = self.dtype
        out.shape = self.shape
        return out

    def eval(self, code, i=None):
        if code == "repr":
            return self.type
        if i is None:
            return self.label
        else:
            return "%s[%s]" % (self.label, i)

    def cdecl(self):
        return "%s%s *%s%s" % (vp.base.codegen.const(self.__const),
                               vp.base.codegen.to_ctype_str(self.dtype),
                               vp.base.codegen.restrict(self.__restrict), self.label)


def _label():
    global __count__
    out = "v%d" % __count__
    __count__ += 1
    return out


def dummy(label: str, shape: tuple = (1,)) -> Array:
    return Array(np.zeros(shape), None, label)
