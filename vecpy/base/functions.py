import vecpy as vp
from vecpy.base.expression import Expr


class Function(Expr):

    def __init__(self, label, expr, *args):
        self.label = label
        self.expr = expr
        self.args = args

    def eval(self, code, i=None):
        if self.args == ():
            args_str = ""
        else:
            args_str = ", " +  ", ".join(["%s" % arg for arg in self.args])
        return "%s(%s%s)" % (self.label, self.expr.eval(code, i), args_str) 
