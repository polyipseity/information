---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {{a programming language}}. Have you tried {{searching for documentation and reading them}}? <!--SR:!2025-06-27,247,330!2025-08-10,283,330-->

## numpy

`numpy` is {{a Python library allowing one to manipulate arrays of numbers}}. Its documentation is available on {{<https://numpy.org/doc/>}}. <!--SR:!2025-07-24,268,339!2025-08-20,291,339-->

### useful functions

- DFT matrix ::: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) <!--SR:!2025-06-27,234,340!2025-06-01,212,340-->
- general ::: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html) <!--SR:!2025-02-26,146,319!2025-07-13,260,339-->
- spectrum ::: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html) <!--SR:!2025-06-24,230,340!2024-12-06,80,340-->
- window ::: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html) <!--SR:!2025-03-10,142,299!2025-09-13,307,339-->

## matplotlib

`matplotlib` is {{a Python library allowing one to visualize numbers}}. Its documentation is available on {{<https://matplotlib.org/stable/api/>}}. <!--SR:!2025-07-06,254,339!2025-08-11,283,339-->

## complex number

Python has {{builtin support (no libraries needed) for complex numbers}}. The imaginary unit is {{denoted `j`}}. To create a complex number, write code {{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}}. It can be used with {{[`numpy`](#numpy) and [`matplotlib`](#matplotlib)}}. <!--SR:!2024-11-11,70,319!2024-11-17,75,319!2025-08-25,291,339!2025-09-08,303,339-->
