---
id: to_vecpy
title: to_vecpy
sidebar_label: to_vecpy  
---

```python
def to_vecpy(array: numpy.ndarray, label: str = None) -> vecpy.base.Array:
```

---


Transfer NumPy array to the GPU.

## Args
* **array**  : Input NumPy array
* **label** (optional) : Label to use for the VecPy array in symbolic expressions

## Returns
A VecPy array that contains a copy of the NumPy array stored on the GPU.




