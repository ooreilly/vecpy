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

>>> x = numpy.ones(10,)
>>> vx = vecpy.to_vecpy(x)
>>> vy = vecpy.zeros_like(x)
>>> expr = vecpy.function("erf", vx)
>>> vecpy.elementwise(vy, expr)
>>> y = vecpy.to_numpy(vy)
>>> y

```


