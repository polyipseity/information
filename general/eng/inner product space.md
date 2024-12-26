---
aliases:
  - inner product
  - inner product space
  - inner product spaces
tags:
  - flashcard/active/general/eng/inner_product_space
  - language/in/English
---

# inner product space

## some examples

### Hilbert space

- see: [Hilbert space](Hilbert%20space.md)

[Hilbert spaces](Hilbert%20space.md) are {@{inner product spaces with an [induced](subspace%20topology.md) [distance function](metric%20space.md) for which the space is a [complete metric space](complete%20metric%20space.md)}@}. However, for simplicity, inner product spaces are often introduced {@{without regards to the completeness of the induced metric space}@}.

An example of an inner product space which {@{induces an incomplete metric}@} is {@{the space $C([a, b])$ of continuous complex-valued functions on the interval $[a, b]$}@}. The inner product of two functions $f$ and $g$ in this space is often stated as {@{$$\langle f, g \rangle = \int_a^b \! f(t) \overline{g(t)} \,\mathrm{d}t$$}@}. This space is not complete. Consider for example, on the interval $[-1, 1]$ ($C([-1, 1])$) the sequence of continuous "step" functions, $\set{f_k}_k$, defined by {@{$$f_k(t) = \begin{cases} 0 & t \in [-1, 0] \\ kt & t \in (0, 1 / k) \\ 1 & t \in [1 / k, 1] \end{cases}$$}@}. Graphically, the graph a function in the sequence can be described as {@{constant $0$ from $-1$ to $0$, then linearly increasing to $1$ from $0$ to $1 / k$, then constant $1$ from $1 / k$ to $1$; as $k$ increases, the function [converges pointwise](pointwise%20convergence.md) to the [Heaviside step function](Heaviside%20step%20function.md) (with $f(0) = 0$)}@}. Consider the norm, defined as {@{$$\lVert f \rVert = \sqrt{\langle f, f \rangle}$$}@}, and the distance function in terms of the norm, defined as {@{$$d(f, g) = \lVert f - g \rVert = \sqrt{\langle f - g, f - g \rangle}$$}@}. For any error $\varepsilon > 0$, we can find {@{a large enough number $N$ such that the "distance" between any two functions after the $N$-th function is smaller than the error $\varepsilon$}@}. Loosely, the distance function roughly describes {@{how different two functions are}@}, and the sequence of functions are {@{increasingly similar to all functions after it in the sequence (compare $f_1 - f_2$ and $f_{100} - f_{101}$)}@}, so the maximum "distance" between {@{any two functions after the $N$-th function can be controlled by setting a large enough $N$}@}. So the above sequence of function is {@{a [Cauchy sequence](Cauchy%20sequence.md) for the [metric space](metric%20space.md) defined by $C([-1, 1])$ and the distance function}@}, yet the sequence {@{[converges pointwise](pointwise%20convergence.md) to the [Heaviside step function](Heaviside%20step%20function.md), which is [discontinuous](continuous%20function.md) and does not belong to $C([-1, 1])$}@}, making the metric space incomplete.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/inner_product_space) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
