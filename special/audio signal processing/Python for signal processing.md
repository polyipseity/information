---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {{a programming language}}. Have you tried {{searching for documentation and reading them}}? <!--SR:!2024-08-26,14,290!2024-08-28,16,290-->

## numpy

`numpy` is {{a Python library allowing one to manipulate arrays of numbers}}. Its documentation is available on {{<https://numpy.org/doc/>}}. <!--SR:!2024-08-31,15,299!2024-08-31,15,299-->

### useful functions

- DFT matrix ::: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) <!--SR:!2024-08-26,4,300!2024-08-26,4,300-->
- general ::: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html) <!--SR:!2024-08-26,10,279!2024-08-30,14,299-->
- spectrum ::: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html) <!--SR:!2024-08-26,4,300!2024-08-26,4,300-->
- window ::: [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html) <!--SR:!2024-09-01,16,299!2024-09-02,17,299-->

## matplotlib

`matplotlib` is {{a Python library allowing one to visualize numbers}}. Its documentation is available on {{<https://matplotlib.org/stable/api/>}}. <!--SR:!2024-08-30,14,299!2024-08-31,15,299-->

## complex number

Python has {{builtin support (no libraries needed) for complex numbers}}. The imaginary unit is {{denoted `j`}}. To create a complex number, write code {{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}}. It can be used with {{[`numpy`](#numpy) and [`matplotlib`](#matplotlib)}}. <!--SR:!2024-09-02,17,299!2024-09-03,18,299!2024-09-01,16,299!2024-09-02,17,299-->
