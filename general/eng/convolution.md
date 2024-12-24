---
aliases:
  - convolution
  - convolutions
tags:
  - flashcard/active/general/eng/convolution
  - language/in/English
---

# convolution

In [mathematics](mathematics.md) (in particular, {@{[functional analysis](functional%20analysis.md)}@}), __convolution__ is {@{a [mathematical operation](operation%20(mathematics).md) on two [functions](function%20(mathematics).md) ($f$ and $g$) that produces a third function ($f * g$)}@}. The term _convolution_ refers to {@{both the result function and to the process of computing it}@}. It is defined as {@{the [integral](integral.md) of the product of the two functions after one is reflected about the y-axis and shifted}@}. The integral is {@{evaluated for all values of shift (with the argument of the convolution function specifying the shift), producing the convolution function}@}. The choice of which function is reflected and shifted before the integral {@{does not change the integral result (see [commutativity](#properties))}@}. Graphically, it expresses {@{how the 'shape' of one function is modified by the other}@}.

## definition

The convolution of $f$ and $g$ is written {@{$f * g$, denoting the operator with the symbol $*$}@}. It is defined as {@{the integral of the product of the two functions after one is reflected about the y-axis and shifted}@}. As such, it is {@{a particular kind of [integral transform](integral%20transform.md)}@}: {@{$$(f * g)(t) := \int_{-\infty}^\infty \! f(\tau) g(t - \tau) \,\mathrm{d}\tau$$}@}. An equivalent definition is (see {@{[commutativity](#properties)}@}): {@{$$(f * g)(t) := \int_{-\infty}^\infty \! f(t - \tau) g(\tau) \,\mathrm{d}\tau$$}@}.

While the symbol $t$ is used above, it {@{need not represent the time domain}@}. At each $t$, the convolution formula can be described as {@{the area under the function $f(\tau)$ weighted by the function $g(-\tau)$ shifted by the amount $t$}@}. As $t$ changes, {@{the weighting function $g(t - \tau)$ emphasizes different parts of the input function $f(\tau)$}@}; If {@{$t$ is a positive value}@}, then $g(t - \tau)$ is {@{equal to $g(-\tau)$ that slides or is shifted along the $\tau$-axis toward the right (toward $+\infty$) by the amount of $t$}@}, while if {@{$t$ is a negative value}@}, then $g(t - \tau)$ is equal to {@{$g(-\tau)$ that slides or is shifted toward the left (toward $-\infty$) by the amount of $\lvert t \rvert$}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/convolution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
