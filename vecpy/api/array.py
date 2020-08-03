import numpy as np
import vecpy as vp
import pycuda
import pycuda.driver as cuda

def copy(array: np.ndarray, label: str=None) -> vp.base.Array:
    return vp.base.Array(array, cuda.to_device(array), label)

def zeros_like(array: np.ndarray, label: str=None) -> vp.base.Array:
    return vp.base.Array(array, cuda.to_device(np.zeros_like(array)), label)

def reference(host_array: np.ndarray, device_array: pycuda.driver.DeviceAllocation, 
        label: str=None) -> vp.base.Array:
            return vp.base.Array(host_array, device_array, label)
