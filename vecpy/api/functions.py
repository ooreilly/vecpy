from vecpy.base.functions import Function

"""

TODO: Implement functions for all CUDA Math library functions 
https://docs.nvidia.com/cuda/cuda-math-api/ 

A temporary work-around is to use `function` to create a custom function that matches the name of
the function you want to use.

Example: 

`
>>> erf = lambda expr : function("erf", expr)
`
to define the error function.

"""

def function(name, expr, *args):
    return Function(name, expr, *args)

def sqrt(expr):
    return Function("sqrt", expr)

def sin(expr):
    return Function("sin", expr)

def cos(expr):
    return Function("cos", expr)

def exp(expr):
    return Function("exp", expr)

def log(expr):
    return Function("log", expr)

def abs(expr):
    return Function("fabs", expr)

def pow(expr, exp):
    return Function("pow", expr, exp)

def floor(expr):
    return Function("floor", expr)
