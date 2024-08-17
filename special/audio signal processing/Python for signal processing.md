---
aliases:
  - Python for signal processing
tags:
  - flashcard/active/special/audio_signal_processing/Python_for_signal_processing
  - language/in/English
---

# Python for signal processing

- see: [general/Python](../../general/Python%20(programming%20language).md)

[Python](../../general/Python%20(programming%20language).md) is {{a programming language}}. Have you tried {{searching for documentation and reading them}}?

## numpy

`numpy` is {{a Python library allowing one to manipulate arrays of numbers}}. Its documentation is available on {{<https://numpy.org/doc/>}}.

- useful functions in general ::: [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`numpy.cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html), [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- useful functions for spectrums ::: [`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html), [`numpy.angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html)
- useful functions for DFT matrix ::: [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html), [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)

## matplotlib

`matplotlib` is {{a Python library allowing one to visualize numbers}}. Its documentation is available on {{<https://matplotlib.org/stable/api/>}}.

## complex number

Python has {{builtin support (no libraries needed) for complex numbers}}. The imaginary unit is {{denoted `j`}}. To create a complex number, write code {{as if you are writing the complex number in other contexts (e.g. `4 + 2j`)}}. It can be used with {{[`numpy`](#numpy) and [`matplotlib`](#matplotlib)}}.
