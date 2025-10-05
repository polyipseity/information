---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {@{a programming language}@}. Have you tried {@{searching for documentation and reading them}@}? <!--SR:!2028-07-25,1124,350!2029-02-19,1289,350-->

## NumPy

NumPy \(`numpy`\) is {@{a Python library allowing one to manipulate arrays of numbers}@}. Its documentation is available on {@{<https://numpy.org/doc/>}@}. <!--SR:!2028-12-30,1254,359!2029-05-13,1362,359-->

## matplotlib

`matplotlib` is {@{a Python library allowing one to visualize numbers}@}. Its documentation is available on {@{<https://matplotlib.org/stable/api/>}@}. <!--SR:!2028-10-03,1184,359!2029-03-27,1324,359-->

## complex number

Python has {@{builtin support (no libraries needed) for complex numbers}@}. The imaginary unit is {@{denoted `j`}@}. To create a complex number, write code {@{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}@}. It can be used with {@{[NumPy](#NumPy) and [`matplotlib`](#matplotlib)}@}. <!--SR:!2029-09-20,1461,359!2029-12-31,1540,359!2029-05-14,1358,359!2029-07-24,1415,359-->

## useful functions

- Fourier transform ::@:: [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html), [`numpy.fft.fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html), [`numpy.fft.fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html), [`numpy.fft.ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html), [`numpy.fft.ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html), [`scipy.fft`](https://docs.scipy.org/doc/scipy/reference/fft.html) <!--SR:!2026-11-25,408,381!2027-01-08,445,381-->
- discrete Fourier transform matrix ::@:: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) <!--SR:!2026-11-30,412,381!2026-12-17,426,381-->
- general ::@:: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html), [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) <!--SR:!2026-08-26,312,361!2026-11-28,411,381-->
- segmentation ::@:: [`numpy.array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html), [`numpy.diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html), [`numpy.split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html), [`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) <!--SR:!2027-01-01,439,381!2027-01-13,449,381-->
- signal ::@:: [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html), [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html), [`scipy.signal.resample`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html) <!--SR:!2025-10-23,92,361!2026-12-27,435,381-->
- spectrum ::@:: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html) <!--SR:!2026-12-22,431,381!2026-12-01,413,381-->
- statistics ::@:: [`numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html) <!--SR:!2026-11-18,402,381!2026-11-29,412,381-->
- window ::@:: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html), [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) <!--SR:!2026-12-02,414,381!2026-12-23,432,381-->

## Essentia

Essentia is {@{an open-source C++ library for audio analysis and audio-based music information retrieval}@}. It is best described as {@{a collection of low-level algorithms to _extract audio features_}@} that {@{you can freely combine by yourself to achieve high-level functions}@}. It is available from {@{<https://essentia.upf.edu/>}@}. <!--SR:!2026-12-24,433,381!2026-11-22,406,381!2026-11-16,400,380!2026-12-21,430,381-->

To use it, you will need to {@{follow the instructions to compile and install the library}@}. Then, the library {@{provides Python bindings}@} that allows you to {@{use algorithms in the library using Python directly instead of using C++}@}. <!--SR:!2026-11-27,410,381!2026-11-17,401,381!2026-11-15,399,381-->

## Freesound

Freesound provides {@{an application programming interface \(API\)}@} that allows you to {@{retrieve and edit data on Freesound}@}. Its API documentation is available on {@{<https://freesound.org/docs/api/>}@}. <!--SR:!2026-11-19,403,381!2027-01-23,458,381!2026-12-25,433,381-->

To use {@{the API}@}, you can {@{manually construct the request according to the API documentation}@}, or much more conveniently, use {@{an existing Python library that has already done all of this for you}@}, and you only need to {@{authenticate with an API key and call the correct functions}@}. <!--SR:!2026-11-26,409,381!2026-11-24,408,381!2026-12-31,438,381!2026-12-26,434,381-->
