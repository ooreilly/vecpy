

class Expr(object):

    def __add__(a, b):
        return BinaryOp(a, b, "Add", _caddstr, _paddstr)
                                                      
    def __radd__(a, b):                               
        return BinaryOp(b, a, "Add", _caddstr, _paddstr)
                                                      
    def __sub__(a, b):                                
        return BinaryOp(a, b, "Sub", _csubstr, _psubstr)
                                                      
    def __rsub__(b, a):                               
        return BinaryOp(a, b, "Sub", _csubstr, _psubstr)
                                                      
    def __mul__(a, b):                                
        return BinaryOp(a, b, "Mul", _cmulstr, _pmulstr)
                                                      
    def __rmul__(a, b):                               
        return BinaryOp(b, a, "Mul", _cmulstr, _pmulstr)
                                                      
    def __truediv__(a, b):                            
        return BinaryOp(a, b, "Div", _cdivstr, _pdivstr)
                                                      
    def __rtruediv__(a, b):                           
        return BinaryOp(b, a, "Div", _cdivstr, _pdivstr)
                                                      
    def __pow__(a, b):                                
        return BinaryOp(a, b, "Pow", _cpowstr, _ppowstr)
                                                      
    def __rpow__(a, b):                               
        return BinaryOp(b, a, "Pow", _cpowstr, _ppowstr)
    
    def __str__(self):
        return self.eval("py")

    def repr(self):
        return "%s(%s, %s)" % (self.op_cls, self.a, self.b)

    def ccode(self, i=None):
        return self.eval("c", i)

    def pycode(self, i=None):
        return self.eval("py", i)

    def eval(self, code, i=None):
        if isinstance(self.a, Expr):
            a = self.a.eval(code, i)
        else:
            a = self.a
        if isinstance(self.b, Expr):
            b = self.b.eval(code, i)
        else:
            b = self.b

        if code == "c":
            return self.ccode_fcn(a, b)
        if code == "py":
            return self.pcode_fcn(a, b)
        else:
            raise NotImplementedError("Code generation for %s is not implemented" % code)


class BinaryOp(Expr):
    def __init__(self, a, b, op_cls, ccode_fcn, pcode_fcn):
        self.a = a
        self.b = b
        self.op_cls = op_cls
        self.ccode_fcn = ccode_fcn
        self.pcode_fcn = pcode_fcn

def _caddstr(a, b):
    return "%s + %s" % (a, b)

def _csubstr(a, b):
    return "%s - %s" % (a, b)

def _cmulstr(a, b):
    return "%s * %s" % (a, b)

def _cdivstr(a, b):
    return "%s / %s" % (a, b)

def _cpowstr(a, b):
    return "pow(%s, %s)" % (a, b)

def _paddstr(a, b):
    return "%s + %s" % (a, b)

def _psubstr(a, b):
    return "%s - %s" % (a, b)

def _pmulstr(a, b):
    return "%s * %s" % (a, b)

def _pdivstr(a, b):
    return "%s / %s" % (a, b)

def _ppowstr(a, b):
    return "%s ** %s" % (a, b)
