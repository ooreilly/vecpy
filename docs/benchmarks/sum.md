---
id: sum
title: Performance benchmarks
sidebar_label: Summation
---
import useBaseUrl from '@docusaurus/useBaseUrl';


This page compares how fast several different Python libraries can compute the sum of a mathematical
expression, e.g., 

$\sum_{i=1}^n \cos^2(\theta_i) + \sin^2(\theta_i)$, 

where $\theta_i$ is a vector of length $n$.

The benchmarks below show how many elements per nano-second each library can process as a function
of the number of elements ($n$). Each data point comes from timing the computation 100 times and reporting
the average time. The transfer time of copying the result (either a float, or double) from the
device to the host is included in the measurements for the GPU libraries. Each figure shows the
performance on a log-log time scale in base 10 format. 


The benchmarks were conducted using:
* Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
* NVIDIA(R) GeForce RTX 2080 Ti

### Libraries
These are the libraries used in the benchmarks
* [NumPy](https://numpy.org)
* [NumExpr](https://github.com/pydata/numexpr)
* [scikit-cuda](https://scikit-cuda.readthedocs.io/en/latest/)
* [CuPy](https://github.com/cupy/cupy)
* [VecPy](https://github.com/ooreilly/vecpy)

If the result for a particular library does not show up in a given benchmark, it is because the
library could not solve the problem.


### Source code
The source code for the benchmarks is available [here](https://github.com/ooreilly/vecpy/tree/master/benchmarks).


## Benchmarks
###  Norm
Computes the norm $\sqrt{\sum_i^n x_i^2 + y_i^2}$
<img alt="Norm (float32)" src={useBaseUrl('img/benchmarks/sum_float32.svg')} />
<img alt="Norm (float64)" src={useBaseUrl('img/benchmarks/sum_float64.svg')} />

###  Geometric series
Computes the truncated geometric series 

$\sum_{i=0}^{n-1} r^i = \frac{1 - r^n}{1 - r}$.

<img alt="Geometric series (float32)" src={useBaseUrl('img/benchmarks/geometric-series_float32.svg')} />

Single precision performance

<img alt="Geometries series (float64)" src={useBaseUrl('img/benchmarks/geometric-series_float64.svg')} />

Double precision performance

###  Sum of trigonometric identities
Computes the sum of trigonometric identities 

$\sum_{i=1}^n \sin^2(\theta_i) + \cos^2(\theta_i) = n$.

<img alt="Sum of trigonometric identities (float32)" src={useBaseUrl('img/benchmarks/trig_float32.svg')} />

Single precision performance

<img alt="Sum of trigonometric identities (float64)" src={useBaseUrl('img/benchmarks/trig_float64.svg')} />

Double precision performance


###  Sum of arrays
Adds $9$ arrays together and sums them, $\sum_{i=1}^n a_i + b_i + c_i + \ldots$. Note that this
benchmark could have been implemented by introducing a Matrix a $n \times 9$ matrix. However, the
motivation behind this benchmark is to look for performance bottlenecks caused by adding many objects together.


<img alt="Sum of arrays (float32)" src={useBaseUrl('img/benchmarks/array-sum_float32.svg')} />

Single precision performance

<img alt="Sum of arrays (float64)" src={useBaseUrl('img/benchmarks/array-sum_float64.svg')} />

Double precision performance
