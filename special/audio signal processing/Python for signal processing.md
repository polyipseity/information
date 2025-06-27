---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {@{a programming language}@}. Have you tried {@{searching for documentation and reading them}@}? <!--SR:!2028-07-25,1124,350!2025-08-10,283,330-->

## NumPy

NumPy \(`numpy`\) is {@{a Python library allowing one to manipulate arrays of numbers}@}. Its documentation is available on {@{<https://numpy.org/doc/>}@}. <!--SR:!2025-07-24,268,339!2025-08-20,291,339-->

## matplotlib

`matplotlib` is {@{a Python library allowing one to visualize numbers}@}. Its documentation is available on {@{<https://matplotlib.org/stable/api/>}@}. <!--SR:!2025-07-06,254,339!2025-08-11,283,339-->

## complex number

Python has {@{builtin support (no libraries needed) for complex numbers}@}. The imaginary unit is {@{denoted `j`}@}. To create a complex number, write code {@{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}@}. It can be used with {@{[NumPy](#NumPy) and [`matplotlib`](#matplotlib)}@}. <!--SR:!2025-09-20,313,339!2025-10-13,330,339!2025-08-25,291,339!2025-09-08,303,339-->

## useful functions

- Fourier transform ::@:: [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html), [`numpy.fft.fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html), [`numpy.fft.fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html), [`numpy.fft.ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html), [`numpy.fft.ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html), [`scipy.fft`](https://docs.scipy.org/doc/scipy/reference/fft.html)
- discrete Fourier transform matrix ::@:: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)
- general ::@:: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html), [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- segmentation ::@:: [`numpy.array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html), [`numpy.diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html), [`numpy.split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html), [`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- signal ::@:: [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html), [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html), [`scipy.signal.resample`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html)
- spectrum ::@:: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html)
- statistics ::@:: [`numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
- window ::@:: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html), [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html)

## Essentia

Essentia is {@{an open-source C++ library for audio analysis and audio-based music information retrieval}@}. It is best described as {@{a collection of low-level algorithms to _extract audio features_}@} that {@{you can freely combine by yourself to achieve high-level functions}@}. It is available from {@{<https://essentia.upf.edu/>}@}.

To use it, you will need to {@{follow the instructions to compile and install the library}@}. Then, the library {@{provides Python bindings}@} that allows you to {@{use algorithms in the library using Python directly instead of using C++}@}.

## Freesound

Freesound provides {@{an application programming interface \(API\)}@} that allows you to {@{retrieve and edit data on Freesound}@}. Its API documentation is available on {@{<https://freesound.org/docs/api/>}@}.

To use {@{the API}@}, you can {@{manually construct the request according to the API documentation}@}, or much more conveniently, use {@{an existing Python library that has already done all of this for you}@}, and you only need to {@{authenticate with an API key and call the correct functions}@}.
