---
id: elementwise
title: elementwise
sidebar_label: elementwise  
---

```python
def elementwise(expr: vecpy.base.Expr, out: vecpy.base.Array = None, deviceID: int = 0):
```

---



Returns a new vecpy that contains the result of the element wise operation applied to the 
expression `expr`.

## Args
* **expr**  : VecPy expression to compute.
* **out** (optional) : output argument to assign to.
* **deviceID** (optional) : device ID to use.

## Example

Square each value, $y_i = x_i^2$

 
```python
 
>>> import numpy as np
>>> x = np.arange(10)
>>> # Copy to GPU
>>> vx = vecpy.to_vecpy(x)
>>> # Compute x^2 elementwise
>>> vy = vecpy.elementwise(vx ** 2)
>>> # Copy result to CPU
>>> y = vy.get()
>>> y
array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])
 
```


