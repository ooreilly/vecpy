# Benchmarks
Run performance benchmarks using Numpy, CuPy, sci-kit cuda, and VecPy. To create a new benchmark,
you can look at the provided `Makefile`, or use the script `benchmark.py`. For example,
```
$ make outputdir=example lib=numpy benchmark=sum init benchmark
```
will create a new directory `example` and run a performance test using the Numpy library, and other
default settings specified in the `Makefile`. After the benchmark is completed, you can find a text
file in the output directory (in this case `example`) that contains results from the run. To see the
available benchmarks, you can call `benchmark.py`, to learn about all options.
```
$ python3 benchmarks.py
```
