---
id: reference
title: reference
sidebar_label: reference  
---

```python
def reference(host_array: numpy.ndarray, device_array: pycuda.driver.DeviceAllocation, label: str = None) -> vecpy.base.Array:
```

---



Create a VecPy array that references an already existing PyCUDA DeviceAllocation

## Args
* **host_array**  : NumPy array that describes the shape and type of data
* **device_array**  : PyCUDA DeviceAllocation that contains the allocated data on the GPU
* **label** (optional) : Label to use for the VecPy in symbolic expressions


## Returns
A VecPy array that references the PyCUDA DeviceAllocation. 




