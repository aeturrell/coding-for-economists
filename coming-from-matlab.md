---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: 'Python 3.8.12 64-bit (''codeforecon'': conda)'
  language: python
  name: python3
---

# Coming from Matlab

This chapter is indebted to the excellent [numpy](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) documentation.

Matlab is very much built around matrix operations. The biggest difference between Python and Matlab is that Python is designed to do many things that are *not* matrix manipulation. What this means in practice is that sometimes the notation to do this or that operation in Python (or any other general purpose programming language) is less concise than in Matlab. There is greater competition for each command in Python because it does many more things. However, Python has really first class support for matrices (and tensors, if that's your thing). In this chapter, we'll look at some of the common matrix manipulation commands you might use in Matlab and Python.

In MATLAB, the basic data type, even for scalars, is a multidimensional array. Array assignments in MATLAB are stored as 2D arrays of double precision floating point numbers, unless you specify the number of dimensions and type. Operations on the 2D instances of these arrays are modeled on matrix operations in linear algebra. When doing matrix manipulation in Python (using **numpy** arrays), the basic type will be a multidimensional array. In Python, multiplying 2D arrays with `*` is not matrix multiplication--it's element-by-element multiplication. (In Python 3.5+, the `@` operator can be used for conventional matrix multiplication.)

MATLAB numbers indices from 1; with `a(1)` the first element. Like C++, Python is numbered from zero, with, eg, `a[0]` as the first element.

Another big difference is that Python and its matrix packages are free and open source.

## Matlab <==> Python

What follows is a giant table of translations between Matlab code and Python's **numpy** and [**scipy**](https://www.scipy.org/) packages, which provide a good core set of matrix manipulations. In what follows, we'll assume that you've imported these two packages using

```python
from numpy import *
import scipy.linalg
```

before using any of the Python commands. In case you're wondering, `from package import *` imports everything from that package so that, instead of calling `np.size(a)` you can just call `size(a)`.

In what follows, `a` and `b` will be arrays. For more, see [hyperpolyglot](https://hyperpolyglot.org/numerical-analysis).

| Matlab      | Python (using numpy and scipy) |
| ----------- | ----------- |
| `help func`      | `help(func)`       |
| `a && b`   |  `a and b`    |
| `a || b`   | `a or b`       |
| `ndims(a)`   | `ndim(a)`    |
| `numel(a)`   | `size(a)`    |
| `size(a)`   | `shape(a)` or `a.shape` |
| `size(a,n)`   | `a.shape[n-1]`      |
| `[ 1 2 3; 4 5 6 ]`   | `array([[1.,2.,3.], [4.,5.,6.]])` |
| `[ a b; c d ]`   | `block([[a,b], [c,d]])`   |
| `a(end)`   | `a[-1]`      |
| `a(2,:)`   | `a[1]` or `a[1,:]`      |
| `a(1:5,:)`   | `a[0:5,:]` or `a[:5]`     |
| `a(1:2:end,:)`   | `a[::2,:]`      |
| `flipud(a)`   | `a[::-1,:]`      |
| `a.'`   | `a.T`      |
| `a'`   | `a.conj().T`      |
| `a * b`   | `a @ b`      |
| `a .* b`   | `a * b`      |
| `a./b`   | `a/b`      |
| `a.^3`   | `a**3`      |
| `a(a<0.5)=0`   | `a[a<5]=0`      |
| `a(:) = 3`   | `a[:]=3`      |
| `y=x(:)`   | `x.flatten()`      |
| `1:10`   | `arange(1.,11.)`      |
| `zeros(3,4)`   | `zeros((3,4))`      |
| `ones(3,4)`   | `ones((3,4))`      |
| `eye(3)`   | `eye(3)`      |
| `diag(a)`   | `diag(a)`      |
| `rand(3,4)`   | `random.rand(3,4)`      |
| `linspace(1,3,4)`  | `linspace(1,3,4)`      |
| `[x,y]=meshgrid(0:8,0:5)`  | `mgrid[0:9.,0:6.]` |
| `repmat(a, m, n)`  | `tile(a, (m, n))` |
| `[a b]`  | `concatenate((a,b),1)`|
| `[a; b]`  | `concatenate((a,b))` |
| `max(max(a))`  | `a.max()` |
| `max(a,b)`  | `maximum(a, b)` |
| `norm(v)`  | `linalg.norm(v)` |
| `inv(a)`  | `linalg.inv(a)` |
| `pinv(a)`  | `linalg.pinv(a)` |
| `rank(a)`  | `linalg.matrix_rank(a)` |
| `[U,S,V]=svd(a)`  | <code>U, S, Vh = linalg.svd(a) <br> V = Vh.T </code> |
| `chol(a)`  | `linalg.cholesky(a).T` |
| `[V,D]=eig(a)`  | `D,V = linalg.eig(a)` |
| `[Q,R,P]=qr(a,0)`  | `Q,R = scipy.linalg.qr(a)` |
| `sort(a)`  | `sort(a)` |
| `unique(a)`  | `unique(a)` |
| `squeeze(a)`  | `a.squeeze()` |

Although not featured in the table, **scipy** also has a good range of optimisation algorithms, for instance

```python
from scipy.optimize import minimize
result = minimize(function, start_value, method='Nelder-Mead', tol=1e-6)
```
