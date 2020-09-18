---
id: function
title: function
sidebar_label: function  
---

```python
def function(name: str, expr: vecpy.base.Expr, *args) -> vecpy.base.Function:
```

---


Create a custom function that maps to one of the CUDA Math library functions. 
The function name must match one of the already existing names in the CUDA
Math library: https://docs.nvidia.com/cuda/cuda-math-api/ 

## Args
* **name**  : Function name
* **expr**  : VecPy Expression
* **args**  : Additional arguments that needs to be passed to the function

## Example

Apply the error function       


```python

>>> x = numpy.linspace(0, 1, 10)
>>> vx = vecpy.to_vecpy(x)
>>> vy = vecpy.zeros_like(x)
>>> expr = vecpy.function("erf", vx)
>>> vy = vecpy.elementwise(expr)
>>> vy.get()
array([0.        , 0.12486142, 0.24668378, 0.36264811, 0.47034933,
0.56794162, 0.65422141, 0.72864343, 0.79127487, 0.84270079])

```


