import vecpy as vp
import numpy as np
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

    def repr(self, code=None, i=None):
        return self.__str__()

    def eval(self, code, i=None):
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
