import numpy as np
import vecpy as vp
import pycuda

def copy(array : np.ndarray) -> vp.base.Array:
    import pycuda.driver as cuda
    return vp.base.Array(array, cuda.to_device(array))

def reference(host_array : np.ndarray, device_array : pycuda.driver.DeviceAllocation) -> \
        vp.base.Array:
            return vp.base.Array(host_array, device_array)
