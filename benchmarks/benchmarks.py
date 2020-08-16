"""
Performance benchmarks for NumPy, NumExpr, scikit-cuda, CuPy, and VecPy
"""
import numpy as np
from timeit import timeit
import sys
import numexpr as ne
import pycuda.gpuarray as gpuarray
import skcuda as sk
import skcuda.linalg as linalg
import pycuda.autoinit
import pycuda.driver as cuda
import cupy as cp
import vecpy as vp
from functools import reduce
linalg.init()
cp.cuda.Device(0).use()

if len(sys.argv) != 9:
    print("""usage: %s <benchmark> <lib> <sizes> <begin> <end> <trials> <dtype> <test>
             benchmark:         Benchmark to run ('sum' for summation, 'elementwise' for
                                elementwise)
             lib:               Library to use ('numpy', 'numexpr', 'skcuda', 'cupy', or 'vecpy')
             sizes:             Logspace number of values
             begin:             Logspace start value
             end:               Logspace end value
             trials:            Number of trials
             dtype:             Precision to use ('float32', or 'float64')
             test:              Run test.
          """ % sys.argv[0])
    exit(1)

libs = ["numpy", "numexpr", "skcuda", "cupy", "vecpy", "test"]
gpu_libs = ["skcuda", "cupy", "vecpy"]
dtypes = {"float64": np.float64, "float32": np.float32}
labels = {"numpy": "NumPy", "numexpr": "NumExpr",
          "skcuda": "scikit-cuda", "cupy": "CuPy", "vecpy": "VecPy"}

benchmark = sys.argv[1]
lib = sys.argv[2]
num_sizes = int(sys.argv[3])
begin = float(sys.argv[4])
end = float(sys.argv[5])
trials = int(sys.argv[6])
str_dtype = sys.argv[7]
test = int(sys.argv[8])


if lib not in libs:
    raise ValueError("Unknown library: %s " % lib)

if str_dtype not in dtypes:
    raise ValueError("Unknown precision: %s " % str_dtype)

dtype = dtypes[str_dtype]
sizes = np.logspace(begin, end, num_sizes).astype(np.int64)
num_sizes = len(sizes)

work_rate = np.zeros((num_sizes,))
elapsed = np.zeros((num_sizes,))

print(str_dtype, labels[lib])


copy = {"skcuda": lambda x: gpuarray.to_gpu(x),
        "cupy": lambda x: cp.asarray(x),
        "vecpy": lambda x: vp.to_vecpy(x)}


transfer = {"skcuda": lambda x: x.get(),
            "cupy": lambda x: x.get(),
            "vecpy": lambda x: vp.to_numpy(x)}


def prod(lst):
    return reduce(lambda x, y: x * y, lst)


for i, size in enumerate(sizes):
    u = np.random.rand(size).astype(dtype)
    v = np.random.rand(size).astype(dtype)
    w = np.random.rand(size).astype(dtype)
    s = [0] * 9
    d_s = [0] * 9
    for i, si in enumerate(s):
        s[i] = np.random.rand(size).astype(dtype)
    d_u = d_v = d_w = None
    # Value to use in exponential function test: sum(r ** v[i])
    r = 0.999999999999

    if benchmark == "geometric-series":
        v = np.arange(size).astype(dtype)

    if lib in gpu_libs:
        d_u = copy[lib](u)
        d_v = copy[lib](v)
        d_w = copy[lib](w)
        for i, si in enumerate(s):
            d_s[i] = copy[lib](si)

    kernels = {}
    kernels["numpy"] = {"sum": lambda: np.sqrt(np.sum(u**2 + v**2, dtype=np.float64)),
                        "geometric-series": lambda: np.sum(r ** v, dtype=np.float64),
                        "trig": lambda: np.sum(np.cos(u)**2 + np.sin(u)**2),
                        "array-sum": lambda: np.sum(sum([si for si in s]), dtype=np.float64),
                        "array-mul": lambda: prod([si for si in s])
                        }
    kernels["numexpr"] = {"sum": lambda: np.sqrt(ne.evaluate("sum(u**2 + v**2)")),
                          "geometric-series": lambda: ne.evaluate("sum(r**v)"),
                          "trig": lambda: ne.evaluate("sum(cos(u)**2 + sin(u)**2)"),
                          # Not supported
                          "array-sum": lambda: ne.evaluate("sum(%s)" %
                                                           (" + ".join(
                                                               "s[%d]" % i for i in range(9))))}
    kernels["skcuda"] = {"sum": lambda: np.sqrt(sk.misc.sum(d_u**2 + d_v**2).get()),
                         # Not supported
                         "geometric-series": lambda: sk.misc.sum(r ** d_v).get(),
                         # Not supported (no cos? )
                         "trig": lambda: sk.misc.sum(sk.cos(d_u)**2 + sk.sin(d_u)**2).get(),
                         "array-sum": lambda: sk.misc.sum(sum([si for si in d_s]),
                                                          dtype=np.float64).get()
                         }
    kernels["cupy"] = {
        "sum": lambda: np.sqrt(cp.sum(d_u**2 + d_v**2, dtype=np.float64).get()),
        "trig": lambda: cp.sum(cp.cos(d_u)**2 + cp.sin(d_u)**2).get(),
        "geometric-series": lambda: cp.sum(r ** d_v, dtype=np.float64).get(),
        "array-sum": lambda: cp.sum(sum([si for si in d_s])).get(),
        "array-mul": lambda: prod([si for si in d_s]),
        "pow": lambda: (d_u).get()
    }
    kernels["vecpy"] = {"sum": lambda: np.sqrt(vp.sum(d_u**2 + d_v**2).get()),
                        "geometric-series": lambda: vp.sum(r ** d_v).get(),
                        "trig": lambda: vp.sum(vp.cos(d_u)**2 + vp.sin(d_u)**2).get(),
                        "array-sum": lambda: vp.sum(sum([si for si in d_s])).get(),
                        "array-mul": lambda: vp.elementwise(prod([si for si in d_s]), out=d_w),
                        "pow": lambda: vp.elementwise(d_u)
                        }
    # Compare against numpy when exact answer is not known
    kernels["test"] = {"sum": kernels["numpy"]["sum"],
                       "geometric-series": lambda: (1.0 - r ** size) / (1.0 - r),
                       "trig": lambda: size,
                       "array-sum": kernels["numpy"]["array-sum"],
                       "array-mul": kernels["numpy"]["array-mul"]
                       }
    kernel = kernels[lib][benchmark]

    if test:
        print("Absolute error: %g " %
              (np.sum(np.abs(kernels["test"][benchmark]() - kernel()))), flush=True)
    else:
        elapsed[i] = timeit(kernel, number=trials) / trials

        work_rate[i] = size / elapsed[i] * 1e-9
        print("%-10d %-8.4f ms %-8.4f Elements/ns" %
              (size, elapsed[i] * 1e3, work_rate[i]), flush=True)
