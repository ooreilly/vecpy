import numpy as np
import vecpy as vp
import pycuda
import pycuda.driver as cuda

def to_vecpy(array: np.ndarray, label: str=None) -> vp.base.Array:
    return vp.base.Array(array, cuda.to_device(array), label)

def to_numpy(array: vp.base.Array, label: str=None) -> np.ndarray:
    out = np.ndarray(array.shape).astype(array.dtype)
    cuda.memcpy_dtoh(out, array.x)
    return out

def zeros_like(array: np.ndarray, label: str=None) -> vp.base.Array:
    return vp.base.Array(array, cuda.to_device(np.zeros_like(array).astype(array.dtype)), label)

def reference(host_array: np.ndarray, device_array: pycuda.driver.DeviceAllocation, 
        label: str=None) -> vp.base.Array:
            return vp.base.Array(host_array, device_array, label)
