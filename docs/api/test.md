---
id: codegen
title: Expressible and high performing mathematical libraries  (2016 - ongoing) 
sidebar_label: Expressible and high performing mathematical libraries
---
import useBaseUrl from '@docusaurus/useBaseUrl';

## Background
When I was a teaching assistant for a modern Fortran programming class, the instructor, Damien
Rouson, planted a philosophy in mind that has stuck with me ever since that time. He said, we when write scientific
software, we should strive to write code that mimics the abstract nature of the mathematical
expressions that we write on the blackboard. The reality is that the source codes behind most scientific
software look nothing like the actual mathematical expressions that they implement. The reason why
we should strive for this level of abstraction is flexibility. With the right level of abstraction,
it should be possible to make changes without rewriting massive parts of the code. Such flexibility
encourages experimentation, and that may lead to new discoveries and breakthroughs. Damien
Rouson was convinced that to reach this level of abstraction in a scalable manner required a functional programming
approach, or graph-based approach. 

### TensorFlow and blackboard-like mathematical expressivity
Today, we have libraries like TensorFlow that construct graphs to
provide powerful abstractions that make these blackboard like calculations possible. 
While TensorFlow is primarily geared for machine
learning, it can also be used for computational physics simulations. This
[example](https://github.com/tensorflow/examples/blob/master/community/en/pdes.ipynb) solves a
partial differential equation, like the
wave equation in 2D. The whole solution is just a few lines of code, and brings us one step closer
towards writing code that looks similar to the math you would write on a blackboard. In this regard,
libraries like TensorFlow greatly simplifies the task of not only doing machine learning, but also
solving partial differential equations. However, there
is a part of the story missing here. 


### The performance gap
While TensorFlow makes it
possible to implement say the elastic wave equation in 3D, it is not an efficient solution. 
As the bar charts below show, TensorFlow is about 4 - 7 times slower than the hand-coded solutions.

<img alt="Elastic 3D benchmark" src={useBaseUrl('img/tensorflow_64.svg')} />
<img alt="Elastic 3D benchmark" src={useBaseUrl('img/tensorflow_256.svg')} />

*Time per time step (FPS) obtained when solving 3D elastic wave equation on a NVIDIA Titan X (Pascal).*

Implementations tested:
* [SeisCL](https://github.com/gfabieno/SeisCL)
* [AWP-ODC](https://github.com/HPGeoC/awp-odc-os)
* [TensorFlow](https://github.com/ooreilly/WaveFlow/blob/develop-ooreilly/problems/elastic3d.py)

I wrote the 3D elastic wave equation solver using TensorFlow. This
implementation does not impose any boundary conditions. I have not put any effort into
testing that this implementation actually solves the elastic wave equation and not something else.
Furthermore, this implementation uses constant coefficients for the elastic material
properties, whereas the hand-coded implementations use variable coefficients. A variable coefficient
implementation would be even slower.  

### A closer look at blackboard-like mathematical abstractions
The beauty of the TensorFlow approach is that it is not far away from achieving the blackboard-like
mathematical abstractions. Let us take a closer look. Here are the governing equations for the linear elastic wave equation with an isotropic material in Cartesian coordinates,

$
\partial_t v_i = \partial_{x_j} \sigma_{ij}, \\
\partial_t\sigma_{ij} = \lambda \partial_{x_k} v_k \delta_{ij} + \mu \partial_{x_i} v_j + \mu
\partial_{x_j} v_i. 
$

If we expand out the index notation expression, we obtain

$
\rho \partial_t v_x = \partial_x \sigma_{xx} + \partial_y \sigma_{xy} + \partial_z \sigma_{xz}, \\
\rho \partial_t v_y = \partial_x \sigma_{xy} + \partial_y \sigma_{yy} + \partial_z \sigma_{xz}, \\
\rho \partial_t v_z = \partial_x \sigma_{xz} + \partial_y \sigma_{yz} + \partial_z \sigma_{zz}, \\
\partial_t \sigma_{xx} = \lambda (\partial_x v_x + \partial_y v_y + \partial_z v_x) + 2\mu \partial_x v_x \\
\partial_t \sigma_{yy} = \lambda (\partial_x v_x + \partial_y v_y + \partial_z v_x) + 2\mu \partial_y v_y \\
\partial_t \sigma_{zz} = \lambda (\partial_x v_x + \partial_y v_y + \partial_z v_x) + 2\mu \partial_z v_z \\
\partial_t \sigma_{xy} = \mu (\partial_x v_y + \partial_y v_x) \\
\partial_t \sigma_{xz} = \mu (\partial_x v_z + \partial_z v_x) \\
\partial_t \sigma_{yz} = \mu (\partial_y v_z + \partial_z v_y) 
\\
$

And this is the TensorFlow implementation taken from [here](https://github.com/ooreilly/WaveFlow/blob/develop-ooreilly/problems/elastic3d.py) with minor modifications:  
```python
# Velocities
vx = tf.Variable(vx0)
vy = tf.Variable(vy0)
vz = tf.Variable(vz0)

# Stresses
sxx = tf.Variable(sxx0)
sxy = tf.Variable(sxy0)
sxz = tf.Variable(sxz0)
syy = tf.Variable(syy0)
syz = tf.Variable(syz0)
szz = tf.Variable(szz0)

# Derivatives of velocities
vx_x = k.Dx3d(vx, s)
vx_y = k.Dy3d(vx, s)
vx_z = k.Dz3d(vx, s)
vy_x = k.Dx3d(vy, s)
vy_y = k.Dy3d(vy, s)
vy_z = k.Dz3d(vy, s)
vz_x = k.Dx3d(vz, s)
vz_y = k.Dy3d(vz, s)
vz_z = k.Dz3d(vz, s)

# Derivatives of stresses (implemented using convolution stencils)
sxx_x = k.Dxh3d(sxx, s)
sxy_x = k.Dxh3d(sxy, s)
sxz_x = k.Dxh3d(sxz, s)
sxy_y = k.Dyh3d(sxy, s)
syy_y = k.Dyh3d(syy, s)
syz_y = k.Dyh3d(syz, s)
sxz_z = k.Dzh3d(sxz, s)
syz_z = k.Dzh3d(syz, s)
szz_z = k.Dzh3d(szz, s)

# Momentum balance
vx_t = vx + nu * rhoi * (sxx_x + sxy_y + sxz_z)
vy_t = vy + nu * rhoi * (sxy_x + syy_y + syz_z)
vz_t = vz + nu * rhoi * (sxz_x + syz_y + szz_z)

# Time derivative of Hooke's law for a linear isotropoic elastic material
sxx_t = sxx + nu * (lam * (vx_x + vy_y + vz_z) + 2 * mu * vx_x)
syy_t = syy + nu * (lam * (vx_x + vy_y + vz_z) + 2 * mu * vy_y)
szz_t = szz + nu * (lam * (vx_x + vy_y + vz_z) + 2 * mu * vz_z)
sxy_t = sxy + nu * mu * (vx_y + vy_x)
sxz_t = sxz + nu * mu * (vx_z + vz_x)
syz_t = syz + nu * mu * (vy_z + vz_y)
```
As you can see, the last few lines of code show a striking resemblance to the actual mathematical
equations. The derivatives are implemented via finite difference stencils that map to convolution kernels in TensorFlow, see [here](https://github.com/ooreilly/ooreilly.github.io/codes/codegen/kernels.py).

Unfortunately, as you saw earlier, this solution is inefficient. In the sections that
follow, you will see why this solution is inefficient. You will also see that similar inefficient
solutions exist in libraries like NumPy, and NumPy-like libraries that targeted the GPU. I also
share some of my work-arounds that can dramatically improve the performance, and what I believe is
important for future work. I my free time, I am in pursuit of developing solutions that are
highly expressible via black-board like abstractions and also delivers high performance. 

## Linear algebra
[Matlab](https://www.mathworks.com/products/matlab.html), [Octave](https://www.gnu.org/software/octave/), [Mathematica](https://www.wolfram.com/mathematica/), [Julia](https://julialang.org/), and libraries like [NumPy](https://numpy.org/), [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)
provide high-level and convenient interfaces for basic linear algebra computations.
Under the hood of these packages lies highly efficient implementations of the [BLAS](http://www.netlib.org/blas/) specification.
As you can see, the BLAS specification is a collection of functions that perform linear algebra
operations like the dot product, matrix vector multiplication, and matrix matrix multiplication. If
you use a BLAS library directly instead of using a high-level library like NumPy, the syntax is
quite verbose and easily obfuscates the underlying mathematical expressions. On the other hand, the
high-level aspect of NumPy hides implementation details that can have a negative impact on
performance. Next, you will see why this is the case.

Suppose you are interested in computing
$\mathbf{v} \leftarrow \alpha \mathbf{x} + \beta \mathbf{y} + \gamma \mathbf{z}$, where
$\alpha$, $\beta$, $\gamma$ are scalars, and $\mathbf{x}$, $\mathbf{y}$, and $\mathbf{z}$ are
vectors of length $N$. 

Using NumPy, this linear algebra expression could be implemented by 
```python
v = alpha * x + beta * y + gamma * z.
```
See [here](https://github.com/ooreilly/ooreilly.github.io/codes/codegen/example1.py) for the
complete code. 
The complete code contains some additional details that we will cover soon. 


### Temporary arrays
For NumPy to be able to compute the previous expression, it needs to introduce temporary arrays. The
term `alpha * x` will be stored in a temporary array, and `beta * y` will be stored in another
temporary array. Under certain circumstances, NumPy can reuse temporary arrays. So `gamma * z` may
be stored in one of the previous temporary arrays [[1](#further-reading)]. Finally, NumPy needs
to allocate a new array to hold the output `v`. What you should take away from all of this is that NumPy may need to create several temporary arrays to
perform the computation. From one point view, this approach causes sudden memory allocation and deallocation 
which can be problematic when working with large arrays. As a result,
this approach can have a negative impact on performance. On the other hand, this approach increases parallelism
because the computation of each term is independent of the other terms if there is one temporary
array per term.

It is possible to gain control over the number of temporary arrays that NumPy creates. NumPy provides the optional argument `out` to some of its functions. This argument allows NumPy to
write results directly to a pre-allocated array instead of returning by value (which will create a
copy of the input array). Using the `out` argument, we can implement the previous example using only
one temporary array `tmp`:
```python
tmp = np.zeros_like(x)
w = np.zeros_like(x)
# alpha * x
np.multiply(alpha, x, out=w)
# beta * y
np.multiply(beta, y, out=tmp)
# alpha *x + beta * y
np.add(w, tmp, out=w)
# gamma * z
np.multiply(gamma, z, out=tmp)
# alpha * x + beta * y + gamma * z
np.add(w, tmp, out=w)
```
As you can see, this approach trades code readability for reducing the number of temporary arrays.
So unfortunately, we have now lost the capability to write clear and concise expressions.

### Local temporary arrays
The library [NumExpr](https://github.com/pydata/numexpr) takes a different approach than NumPy to
achieve speedups for certain mathematical expressions. As explained in their documentation, they
take a man in the middle approach that only uses small, and local temporary arrays. This solution
avoids all the excess memory traffic caused by the temporary arrays approach that NumPy takes.

### NumPy-like GPU libraries

It is become more and more popular to accelerate compute-intense mathematical expressions using
GPUs. One library that closely mimics the syntax of NumPy is [CuPY](https://github.com/cupy/cupy).
This library works for CUDA-enabled GPUs and implements a subset of the NumPy library. The library
[scikit-cuda](https://github.com/lebedov/scikit-cuda) is another
library that supports NumPY-like functionality for CUDA-enabled GPUs. Both CuPy and scikit-cuda introduce temporary arrays like NumPy. To the best of my knowledge, there are no NumExpr-like libraries for the GPU.

### VecPy

To overcome the potential performance penalties due to temporary arrays, I decided to write my own
light-weight library that runs on CUDA-enabled GPUs. Currently, this library supports an extremely limited set of the core NumPy
functionality. Only vector operations are supported (i.e., dot product, and element wise
multiplication). However, it can achieve dramatic speedups compared to the other libraries. Its
syntax is a slightly bit more complicated than NumPy. For example, suppose you want to compute
$\sqrt{\sum_{i}^n \alpha x_i^2 + \beta y_i^2}$. Here is a NumPy implementation using randomly initialized values:
```python
import numpy as np

n=int(1e7)
x = np.random.rand(n)
y = np.random.rand(n)
alpha = 1.0
beta = 2.0
norm = np.sqrt(np.sum(alpha * x**2 + beta * y**2))
```
and here is a VecPy implementation:

```python
import numpy as np
import vecpy as vp

n=int(1e7)
x = np.random.rand(n)
y = np.random.rand(n)
alpha = 1.0
beta = 2.0
# Copy NumPy arrays to the GPU
vx = vp.to_vecpy(x)
vy = vp.to_vecpy(y)
norm = np.sqrt(vp.sum(alpha * vx**2 + beta * vy**2))
```
Note that, you should call `np.sqrt()` and not `vp.sqrt()` at the end. This is because `vp.sum()`
returns a scalar value that gets copied over the CPU. 

Timing results for `n = 1e7`, are:
* NumPy: 5.409374817973003 s 
* VecPy: 0.10328862397000194 s.

These results were obtained by performing 100 iterations on a Intel(R) Core(TM) i7-6700K CPU @
4.00GHz and NVIDIA GeForce RTX 2080 Ti Graphics card. 

Unlike NumPy, VecPy uses lazy-evaluation. So if you write an expression like `vx ** 2 + vy ** 2`,
almost nothing happens until you call one of VecPy's compute functions (e.g., `sum()`).

<img alt="VecPy sum benchmark" src={useBaseUrl('img/vecpy.svg')} />


## Further reading
1. [TensorFlow Partial Differential Equation Example](https://github.com/tensorflow/examples/blob/master/community/en/pdes.ipynb)
2. [Python in HPC: Temporary Arrays](https://www.futurelearn.com/courses/python-in-hpc/0/steps/65112)


