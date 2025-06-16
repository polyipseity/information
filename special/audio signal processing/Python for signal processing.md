---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {@{a programming language}@}. Have you tried {@{searching for documentation and reading them}@}?

## numpy

`numpy` is {@{a Python library allowing one to manipulate arrays of numbers}@}. Its documentation is available on {@{<https://numpy.org/doc/>}@}.

## matplotlib

`matplotlib` is {@{a Python library allowing one to visualize numbers}@}. Its documentation is available on {@{<https://matplotlib.org/stable/api/>}@}.

## complex number

Python has {@{builtin support (no libraries needed) for complex numbers}@}. The imaginary unit is {@{denoted `j`}@}. To create a complex number, write code {@{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}@}. It can be used with {@{[`numpy`](#numpy) and [`matplotlib`](#matplotlib)}@}.

## useful functions

- Fourier transform ::@:: [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html), [`numpy.fft.fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html), [`numpy.fft.fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html), [`numpy.fft.ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html), [`numpy.fft.ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html), [`scipy.fft`](https://docs.scipy.org/doc/scipy/reference/fft.html)
- discrete Fourier transform matrix ::@:: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)
- general ::@:: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html), [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- segmentation ::@:: [`numpy.array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html), [`numpy.diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html), [`numpy.split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html), [`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- spectrum ::@:: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html)
- statistics ::@:: [`numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
- window ::@:: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html), [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html)
