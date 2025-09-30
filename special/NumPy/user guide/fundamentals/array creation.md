---
aliases:
  - array creation
tags:
  - flashcard/active/special/NumPy/user_guide/fundamentals/array_creation
  - function/index
  - language/in/English
  - version/NumPy/2/1
---

# array creation

- see also: [array creation routines](../../../API%20reference/by%20topic/array%20creation%20routines.md)

## introduction

There are {@{6 general mechanisms}@} for creating arrays: <!--SR:!2026-01-12,343,350-->

1. Conversion ::@:: from other Python structures (i.e. lists and tuples) <!--SR:!2026-01-13,344,350!2026-01-06,338,350-->
2. Intrinsic ::@:: NumPy array creation functions (e.g. arange, ones, zeros, etc.) <!--SR:!2026-01-17,347,350!2029-02-28,1229,350-->
3. Replicating, joining, or mutating ::@:: existing arrays <!--SR:!2027-10-29,818,330!2025-12-25,327,350-->
4. Reading ::@:: arrays from disk, either from standard or custom formats <!--SR:!2026-01-12,343,350!2026-01-15,345,350-->
5. Creating arrays ::@:: from raw bytes through the use of strings or buffers <!--SR:!2028-11-09,1129,350!2027-11-14,834,330-->
6. Use of ::@:: special library functions (e.g., random) <!--SR:!2026-01-21,350,350!2026-01-20,349,350-->

You can use these methods to {@{create ndarrays or [structured arrays](structured%20arrays.md)}@}. This document will cover general methods for {@{ndarray creation}@}. <!--SR:!2026-01-16,346,350!2029-03-06,1235,350-->

## converting Python sequences to NumPy arrays

NumPy arrays can be defined using {@{Python sequences such as lists and tuples}@}. {@{Lists and tuples}@} are defined {@{using `[...]` and `(...)`, respectively}@}. Lists and tuples can define ndarray creation: <!--SR:!2025-10-22,273,330!2025-10-19,270,330!2026-01-18,348,350-->

- a list of numbers will create ::@:: a 1D array, <!--SR:!2028-11-07,1142,350!2026-01-05,337,350-->
- a list of lists will create ::@:: a 2D array, <!--SR:!2025-11-04,283,330!2025-10-21,271,330-->
- further nested lists will create ::@:: higher-dimensional arrays. In general, any array object is called an **ndarray** in NumPy. <!--SR:!2025-10-29,278,330!2026-01-21,350,350-->

```Python
>>> import numpy as np
>>> a1D = np.array([1, 2, 3, 4])
>>> a2D = np.array([[1, 2], [3, 4]])
>>> a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

When {@{you use [`numpy.array`](../../API%20reference/generated/numpy.array.md#numpy.array "numpy.array") to define a new array}@}, you should {@{consider the [dtype](data%20types.md) of the elements in the array}@}, which {@{can be specified explicitly}@}. This feature gives you {@{more control over the underlying data structures and how the elements are handled in C/C++ functions}@}. When {@{values do not fit and you are using a `dtype`}@}, NumPy may {@{raise an error}@}: <!--SR:!2025-11-03,282,330!2026-01-04,336,350!2029-02-04,1209,350!2025-10-23,274,330!2026-01-18,348,350!2029-03-02,1231,350-->

```Python
>>> import numpy as np
>>> np.array([127, 128, 129], dtype=np.int8)
Traceback (most recent call last):
...
OverflowError: Python integer 128 out of bounds for int8
```

{@{An 8-bit signed integer}@} represents {@{integers from -128 to 127}@}. Assigning {@{the `int8` array to integers outside of this range}@} results in {@{overflow}@}. This feature can {@{often be misunderstood}@}. If {@{you perform calculations with mismatching `dtypes`}@}, you can {@{get unwanted results}@}, for example: <!--SR:!2026-01-17,347,350!2026-01-22,351,350!2026-01-09,340,350!2026-01-24,353,350!2026-01-23,352,350!2025-10-27,276,330!2025-10-26,275,330-->

```Python
>>> import numpy as np
>>> a = np.array([2, 3, 4], dtype=np.uint32)
>>> b = np.array([5, 6, 7], dtype=np.uint32)
>>> c_unsigned32 = a - b
>>> print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
unsigned c: [4294967293 4294967293 4294967293] uint32
>>> c_signed32 = a - b.astype(np.int32)
>>> print('signed c:', c_signed32, c_signed32.dtype)
signed c: [-3 -3 -3] int64
```

Notice when {@{you perform operations with two arrays of the same `dtype`: `uint32`}@}, the resulting array is {@{the same type}@}. When {@{you perform operations with different `dtype`}@}, NumPy will {@{assign a new type that satisfies all of the array elements involved in the computation, here `uint32` and `int32` can both be represented in as `int64`}@}. <!--SR:!2025-11-07,285,330!2026-01-02,335,350!2025-11-14,292,330!2025-10-23,273,330-->

The default NumPy behavior is to {@{create arrays in either 32 or 64-bit signed integers (platform dependent and matches C `long` size) or double precision floating point numbers}@}. If {@{you expect your integer arrays to be a specific type}@}, then {@{you need to specify the `dtype` while you create the array}@}. <!--SR:!2026-01-10,341,350!2025-11-08,286,330!2026-01-03,335,350-->

## intrinsic NumPy array creation functions

NumPy has {@{over 40 built-in functions for creating arrays as laid out in the [array creation routines](../../../API%20reference/generated/array%20creation%20routines.md)}@}. These functions {@{can be split into roughly three categories}@}, based on the dimension of the array they create: <!--SR:!2026-01-13,344,350!2025-10-26,276,330-->

1. 1D arrays
2. 2D arrays
3. ndarrays

### 1D array creation functions

{@{The 1D array creation functions}@} e.g. {@{[`numpy.linspace`](../../API%20reference/generated/numpy.linspace.md#numpy.linspace "numpy.linspace") and [`numpy.arange`](../../API%20reference/generated/numpy.arange.md#numpy.arange "numpy.arange")}@} generally {@{need at least two inputs, `start` and `stop`}@}. <!--SR:!2025-10-28,277,330!2025-11-05,284,330!2026-01-24,353,350-->

{@{[`numpy.arange`](../../API%20reference/generated/numpy.arange.md#numpy.arange "numpy.arange")}@} creates {@{arrays with regularly incrementing values}@}. Check the documentation for complete information and examples. A few examples are shown: <!--SR:!2025-10-20,271,330!2025-10-22,273,330-->

```Python
>>> import numpy as np
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(2, 10, dtype=float)
array([2., 3., 4., 5., 6., 7., 8., 9.])
>>> np.arange(2, 3, 0.1)
array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
```

Note: {@{best practice for [`numpy.arange`](../../API%20reference/generated/numpy.arange.md#numpy.arange "numpy.arange")}@} is {@{to use integer start, end, and step values}@}. There are {@{some subtleties regarding `dtype`}@}. In the second example, {@{the `dtype` is defined}@}. In the third example, the array is {@{`dtype=float` to accommodate the step size of `0.1`}@}. Due to {@{roundoff error}@}, {@{the `stop` value is sometimes included}@}. <!--SR:!2026-01-01,333,350!2025-10-20,272,330!2026-01-16,346,350!2025-10-30,279,330!2025-10-20,272,330!2025-11-01,280,330!2025-12-24,326,350-->

{@{[`numpy.linspace`](../../API%20reference/generated/numpy.linspace.md#numpy.linspace "numpy.linspace")}@} will {@{create arrays with a specified number of elements}@}, and {@{spaced equally between the specified beginning and end values}@}. For example: <!--SR:!2025-10-24,275,330!2025-11-09,287,330!2025-12-21,323,350-->

```Python
>>> import numpy as np
>>> np.linspace(1., 4., 6)
array([1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
```

{@{The advantage of this creation function}@} is that {@{you guarantee the number of elements and the starting and end point}@}. {@{The previous `arange(start, stop, step)`}@} will {@{not include the value `stop`}@}. <!--SR:!2025-11-06,285,330!2025-10-24,274,330!2025-12-31,333,350!2026-01-13,344,350-->

### 2D array creation functions

{@{The 2D array creation functions}@} e.g. {@{[`numpy.eye`](../../API%20reference/generated/numpy.eye.md#numpy.eye "numpy.eye"), [`numpy.diag`](../../API%20reference/generated/numpy.diag.md#numpy.diag "numpy.diag"), and [`numpy.vander`](../../API%20reference/generated/numpy.vander.md#numpy.vander "numpy.vander")}@} define {@{properties of special matrices represented as 2D arrays}@}. <!--SR:!2025-10-29,278,330!2027-11-18,837,330!2025-10-20,270,330-->

{@{`np.eye(n, m)`}@} defines {@{a 2D identity matrix}@}. {@{The elements where i=j (row index and column index are equal)}@} are {@{1 and the rest are 0}@}, as such: <!--SR:!2029-01-30,1205,350!2029-02-10,1214,350!2025-10-22,273,330!2026-01-07,339,350-->

```Python
>>> import numpy as np
>>> np.eye(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> np.eye(3, 5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.]])
```

{@{[`numpy.diag`](../../API%20reference/generated/numpy.diag.md#numpy.diag "numpy.diag")}@} can {@{define either a square 2D array with given values along the diagonal _or_ if given a 2D array returns a 1D array that is only the diagonal elements}@}. The two array creation functions can be helpful while doing linear algebra, as such: <!--SR:!2025-10-23,273,330!2025-10-23,273,330-->

```Python
>>> import numpy as np
>>> np.diag([1, 2, 3])
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
>>> np.diag([1, 2, 3], 1)
array([[0, 1, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 3],
       [0, 0, 0, 0]])
>>> a = np.array([[1, 2], [3, 4]])
>>> np.diag(a)
array([1, 4])
```

{@{`numpy.vander(x, n)`}@} defines {@{a Vandermonde matrix as a 2D NumPy array}@}. {@{Each column of the Vandermonde matrix}@} is {@{a decreasing power of the input 1D array or list or tuple, `x`}@} where {@{the highest polynomial order is `n-1`}@}. \(annotation: Given {@{a 1D array `x`}@}, the {@{_m_-th (1-based) column is the 1D array `x ** (n - m)`}@}.\) This array creation routine is helpful in {@{generating linear least squares models}@}, as such: <!--SR:!2025-10-25,274,330!2027-12-07,850,330!2025-10-19,271,330!2026-01-29,122,310!2026-01-10,341,350!2025-10-22,272,330!2026-01-04,336,350!2025-11-05,26,379-->

```Python
>>> import numpy as np
>>> np.vander(np.linspace(0, 2, 5), 2)
array([[0. , 1. ],
      [0.5, 1. ],
      [1. , 1. ],
      [1.5, 1. ],
      [2. , 1. ]])
>>> np.vander([1, 2, 3, 4], 2)
array([[1, 1],
       [2, 1],
       [3, 1],
       [4, 1]])
>>> np.vander((1, 2, 3, 4), 4)
array([[ 1,  1,  1,  1],
       [ 8,  4,  2,  1],
       [27,  9,  3,  1],
       [64, 16,  4,  1]])
```

### general ndarray creation functions

{@{The ndarray creation functions}@} e.g. {@{[`numpy.ones`](../../API%20reference/generated/numpy.ones.md#numpy.ones "numpy.ones"), [`numpy.zeros`](../../API%20reference/generated/numpy.zeros.md#numpy.zeros "numpy.zeros"), and [`random`](../../API%20reference/generated/numpy.random.Generator.random.md#numpy.random.Generator.random "numpy.random.Generator.random")}@} define {@{arrays based upon the desired shape}@}. The ndarray creation functions can {@{create arrays with any dimension}@} by specifying {@{how many dimensions and length along that dimension in a tuple or list}@}. <!--SR:!2025-10-20,272,330!2026-01-11,342,350!2029-01-13,1192,350!2027-04-29,623,310!2026-01-15,125,398-->

{@{[`numpy.zeros`](../../API%20reference/generated/numpy.zeros.md#numpy.zeros "numpy.zeros")}@} will {@{create an array filled with 0 values with the specified shape}@}. The default dtype is {@{`float64`}@}: <!--SR:!2025-11-13,291,330!2026-01-17,347,350!2029-03-07,1236,350-->

```Python
>>> import numpy as np
>>> np.zeros((2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> np.zeros((2, 3, 2))
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])
```

{@{[`numpy.ones`](../../API%20reference/generated/numpy.ones.md#numpy.ones "numpy.ones")}@} will {@{create an array filled with 1 values}@}. It is {@{identical to `zeros` in all other respects}@} as such: <!--SR:!2025-11-09,288,330!2029-02-06,1211,350!2029-02-23,1226,350-->

```Python
>>> import numpy as np
>>> np.ones((2, 3))
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.ones((2, 3, 2))
array([[[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]]])
```

{@{The [`random`](../../API%20reference/generated/numpy.random.Generator.random.md#numpy.random.Generator.random "numpy.random.Generator.random") method of the result of `default_rng`}@} will {@{create an array filled with random values between 0 and 1}@}. It is included with {@{the [`numpy.random`](../../API%20reference/generated/index.md#module-numpy.random "numpy.random") library}@}. Below, two arrays are {@{created with shapes (2,3) and (2,3,2), respectively}@}. The seed is set to 42 so {@{you can reproduce these pseudorandom numbers}@}: <!--SR:!2027-11-29,859,330!2026-01-14,344,350!2027-12-10,800,330!2025-10-28,277,330!2029-01-07,1187,350-->

```Python
>>> import numpy as np
>>> from numpy.random import default_rng
>>> default_rng(42).random((2,3))
array([[0.77395605, 0.43887844, 0.85859792],
       [0.69736803, 0.09417735, 0.97562235]])
>>> default_rng(42).random((2,3,2))
array([[[0.77395605, 0.43887844],
        [0.85859792, 0.69736803],
        [0.09417735, 0.97562235]],
       [[0.7611397 , 0.78606431],
        [0.12811363, 0.45038594],
        [0.37079802, 0.92676499]]])
```

{@{[`numpy.indices`](../../API%20reference/generated/numpy.indices.md#numpy.indices "numpy.indices")}@} will {@{create a set of arrays (stacked as a one-higher dimensioned array), one per dimension with each representing variation in that dimension}@}. This is particularly useful for {@{evaluating functions of multiple dimensions on a regular grid}@}: <!--SR:!2029-01-25,1201,350!2027-03-31,667,330!2025-12-28,330,350-->

```Python
>>> import numpy as np
>>> np.indices((3,3))
array([[[0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]],
       [[0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]]])
```

## replicating, joining, or mutating existing arrays

Once {@{you have created arrays}@}, you can {@{replicate, join, or mutate those existing arrays to create new arrays}@}. When you {@{assign an array or its elements to a new variable}@}, you have to {@{explicitly [`numpy.copy`](../../API%20reference/generated/numpy.copy.md#numpy.copy "numpy.copy") the array}@}, otherwise {@{the variable is a view into the original array}@}. Consider the following example: <!--SR:!2026-01-05,337,350!2029-01-31,1206,350!2026-01-14,344,350!2025-11-11,289,330!2026-01-06,338,350-->

```Python
>>> import numpy as np
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> b = a[:2]
>>> b += 1
>>> print('a =', a, '; b =', b)
a = [2 3 3 4 5 6] ; b = [2 3]
```

In this example, you {@{did not create a new array}@}. You {@{created a variable, `b` that viewed the first 2 elements of `a`}@}. When {@{you added 1 to `b`}@} you would {@{get the same result by adding 1 to `a[:2]`}@}. If {@{you want to create a _new_ array}@}, use {@{the [`numpy.copy`](../../API%20reference/generated/numpy.copy.md#numpy.copy "numpy.copy") array creation routine}@} as such: <!--SR:!2025-10-21,272,330!2026-01-21,350,350!2029-01-15,1193,350!2025-12-29,331,350!2025-10-25,275,330!2025-10-21,272,330-->

```Python
>>> import numpy as np
>>> a = np.array([1, 2, 3, 4])
>>> b = a[:2].copy()
>>> b += 1
>>> print('a = ', a, 'b = ', b)
a =  [1 2 3 4] b =  [2 3]
```

For more information and examples look at [copies and Views](../quickstart.md#copies%20and%20views).

There are {@{a number of routines to join existing arrays}@} e.g. {@{[`numpy.vstack`](../../API%20reference/generated/numpy.vstack.md#numpy.vstack "numpy.vstack"), [`numpy.hstack`](../../API%20reference/generated/numpy.hstack.md#numpy.hstack "numpy.hstack"), and [`numpy.block`](../../API%20reference/generated/numpy.block.md#numpy.block "numpy.block")}@}. Here is an example of {@{joining four 2-by-2 arrays into a 4-by-4 array using `block`}@}: <!--SR:!2025-10-24,274,330!2025-12-27,329,350!2025-11-11,290,330-->

```Python
>>> import numpy as np
>>> A = np.ones((2, 2))
>>> B = np.eye(2, 2)
>>> C = np.zeros((2, 2))
>>> D = np.diag((-3, -4))
>>> np.block([[A, B], [C, D]])
array([[ 1.,  1.,  1.,  0.],
       [ 1.,  1.,  0.,  1.],
       [ 0.,  0., -3.,  0.],
       [ 0.,  0.,  0., -4.]])
```

Other routines {@{use similar syntax to join ndarrays}@}. Check the routine's documentation for further examples and syntax. <!--SR:!2026-01-12,343,350-->

## reading arrays from disk, either from standard or custom formats

This is {@{the most common case of large array creation}@}. The details {@{depend greatly on the format of data on disk}@}. This section gives {@{general pointers on how to handle various formats}@}. For {@{more detailed examples of IO}@} look at {@{[how to read and write files](../how-tos/reading%20and%20writing%20files.md)}@}. <!--SR:!2026-01-11,342,350!2025-11-02,281,330!2025-10-19,269,330!2026-01-19,348,350!2026-01-20,349,350-->

### standard binary formats

{@{Various fields}@} have {@{standard formats for array data}@}. The following lists {@{the ones with known Python libraries to read them and return NumPy arrays}@} (there may be {@{others for which it is possible to read and convert to NumPy arrays so check the last section as well}@}) <!--SR:!2029-02-11,1215,350!2026-01-22,351,350!2025-11-10,288,330!2025-11-16,294,330-->

- HDF5 ::@:: h5py <!--SR:!2026-01-07,339,350!2025-11-10,289,330-->
- FITS ::@:: Astropy <!--SR:!2027-12-08,851,330!2025-12-22,324,350-->

Examples of {@{formats that cannot be read directly but for which it is not hard to convert}@} are those formats supported by libraries like {@{PIL (able to read and write many image formats such as jpg, png, etc)}@}. <!--SR:!2025-10-19,271,330!2028-01-21,885,330-->

### common ASCII formats

{@{Delimited files}@} such as {@{comma separated value (csv) and tab separated value (tsv) files}@} are {@{used for programs like Excel and LabView}@}. Python functions can {@{read and parse these files line-by-line}@}. NumPy has {@{two standard routines for importing a file with delimited data}@} {@{[`numpy.loadtxt`](../../API%20reference/generated/numpy.loadtxt.md#numpy.loadtxt "numpy.loadtxt") and [`numpy.genfromtxt`](../../API%20reference/generated/numpy.genfromtxt.md#numpy.genfromtxt "numpy.genfromtxt")}@}. These functions have {@{more involved use cases in [reading and writing files](../how-tos/reading%20and%20writing%20files.md)}@}. A simple example given a `simple.csv`: <!--SR:!2025-11-04,283,330!2025-10-31,280,330!2026-01-03,335,350!2026-01-23,352,350!2028-06-27,1033,350!2025-10-21,272,330!2029-02-22,1224,350-->

```shell
$ cat simple.csv
x, y
0, 0
1, 1
2, 4
3, 9
```

{@{Importing `simple.csv`}@} is accomplished using {@{[`numpy.loadtxt`](../../API%20reference/generated/numpy.loadtxt.md#numpy.loadtxt "numpy.loadtxt")}@}: <!--SR:!2025-10-24,273,330!2025-10-24,275,330-->

```Python
>>> import numpy as np
>>> np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 
array([[0., 0.],
       [1., 1.],
       [2., 4.],
       [3., 9.]])
```

{@{More generic ASCII files}@} can be read using {@{[`scipy.io`](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io "(in SciPy v1.14.0)") and [Pandas](https://pandas.pydata.org/)}@}. <!--SR:!2026-01-15,345,350!2026-01-18,348,350-->

## creating arrays from raw bytes through the use of strings or buffers

There are {@{a variety of approaches one can use}@}. If {@{the file has a relatively simple format}@} then {@{one can write a simple I/O library and use the NumPy `fromfile()` function and `tofile()` method}@} to {@{read and write NumPy arrays directly (mind your byteorder though!)}@}. If {@{a good C or C++ library exists that read the data}@}, one can {@{wrap that library with a variety of techniques}@} though that certainly is {@{much more work and requires significantly more advanced knowledge to interface with C or C++}@}. <!--SR:!2025-10-23,274,330!2029-02-28,1230,350!2025-10-24,274,330!2025-12-26,328,350!2025-12-30,332,350!2026-01-14,344,350!2025-12-19,321,350-->

## use of special library functions (e.g., SciPy, pandas, and OpenCV)

NumPy is {@{the fundamental library for array containers in the Python Scientific Computing stack}@}. {@{Many Python libraries}@}, including {@{SciPy, Pandas, and OpenCV}@}, use {@{NumPy ndarrays as the common format for data exchange}@}. These libraries can {@{create, operate on, and work with NumPy arrays}@}. <!--SR:!2027-11-25,840,330!2029-01-19,1196,350!2025-12-23,325,350!2025-11-15,293,330!2026-01-19,348,350-->

## references

- source: <https://numpy.org/doc/2.1/user/basics.creation.html>
- license: [LICENSE.txt](../../LICENSE.txt)
