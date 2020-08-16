from . expression import Expr

class Scalar(Expr):

    def __init__(self, value):
        self.value = value

    def eval(self, code, i=None):
        return "%s" % self.value
