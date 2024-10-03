---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {{a programming language}}. Have you tried {{searching for documentation and reading them}}? <!--SR:!2024-10-23,55,310!2024-10-31,63,310-->

## numpy

`numpy` is {{a Python library allowing one to manipulate arrays of numbers}}. Its documentation is available on {{<https://numpy.org/doc/>}}. <!--SR:!2024-10-29,59,319!2024-11-02,63,319-->

### useful functions

- DFT matrix ::: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) <!--SR:!2024-11-05,52,320!2024-11-01,48,320-->
- general ::: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html) <!--SR:!2025-02-26,146,319!2024-10-26,57,319-->
- spectrum ::: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html) <!--SR:!2024-11-06,51,320!2024-12-06,80,340-->
- window ::: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html) <!--SR:!2024-10-19,47,299!2024-11-10,69,319-->

## matplotlib

`matplotlib` is {{a Python library allowing one to visualize numbers}}. Its documentation is available on {{<https://matplotlib.org/stable/api/>}}. <!--SR:!2024-10-25,56,319!2024-11-01,62,319-->

## complex number

Python has {{builtin support (no libraries needed) for complex numbers}}. The imaginary unit is {{denoted `j`}}. To create a complex number, write code {{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}}. It can be used with {{[`numpy`](#numpy) and [`matplotlib`](#matplotlib)}}. <!--SR:!2024-11-11,70,319!2024-11-17,75,319!2024-11-07,66,319!2024-11-09,68,319-->
