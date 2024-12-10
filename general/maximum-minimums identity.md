---
aliases:
  - maximum-minimums identities
  - maximum-minimums identity
  - minimum-maximums identities
  - minimum-maximums identity
tags:
  - flashcard/active/general/maximum-minimums_identity
  - language/in/English
---

# maximum-minimums identity

In [mathematics](mathematics.md), {@{the __maximum-minimums identity__}@} is {@{a relation between the maximum element of a [set](set%20(mathematics).md) _S_ of _n_ numbers and the minima of the 2<sup>_n_</sup> − 1 [non-empty](empty%20set.md) [subsets](subset.md) of _S_}@}. <!--SR:!2024-12-25,15,290!2024-12-24,14,296-->

Let {@{_S_ = {_x_<sub>1</sub>, _x_<sub>2</sub>, ..., _x_<sub>_n_</sub>}<!-- flashcard separator -->}@}. The [identity](identity%20(mathematics).md) states that {@{$${\begin{aligned}\max\{x_{1},x_{2},\ldots ,x_{n}\}&=\sum _{i=1}^{n}x_{i}-\sum _{i<j}\min\{x_{i},x_{j}\}+\sum _{i<j<k}\min\{x_{i},x_{j},x_{k}\}-\cdots \\&\qquad \cdots +\left(-1\right)^{n+1}\min\{x_{1},x_{2},\ldots ,x_{n}\},\end{aligned}}$$ or conversely $${\begin{aligned}\min\{x_{1},x_{2},\ldots ,x_{n}\}&=\sum _{i=1}^{n}x_{i}-\sum _{i<j}\max\{x_{i},x_{j}\}+\sum _{i<j<k}\max\{x_{i},x_{j},x_{k}\}-\cdots \\&\qquad \cdots +\left(-1\right)^{n+1}\max\{x_{1},x_{2},\ldots ,x_{n}\}.\end{aligned}}$$}@} <!--SR:!2024-12-20,12,276!2024-12-22,12,276-->

For {@{a probabilistic proof}@}, see the reference. <!--SR:!2024-12-25,15,290-->

> [!tip] tips
>
> - proof using the inclusion–exclusion principle ::@:: Assume the set contains nonnegative real numbers only. Each number $x_i$ represents the interval $[0, x_i]$. Then $\max$ corresponds to the union operation of said intervals, and $\min$ corresponds to the intersection operation of said intervals. For example, compare $\max\set{1, 2} = 2, \min\set{1, 2} = 1$ and $[0, 1] \cup [0, 2] = [0, 2], [0, 1] \cap [0, 2] = [0, 1]$. Clearly, the above equation is an application of the inclusion–exclusion principle on the above intervals. <p> To generalize it for sets containing negative real numbers, simply shift all numbers in the set to be nonnegative, and then un-shift afterwards. <p> To get the converse theorem ($\min$ and $\max$ being swapped), notice that the minimum of real numbers equals the negation of the maximum of their negations. <p> credit: [stochastic](https://math.stackexchange.com/a/2579069), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), via Mathematics Stack Exchange <!--SR:!2024-12-24,14,296!2024-12-25,15,290-->

## see also

- [inclusion–exclusion principle](inclusion–exclusion%20principle.md)
- [maxima and minima § In relation to sets](maximum%20and%20minimum.md#in%20relation%20to%20sets)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/maximum-minimums_identity) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Ross, Sheldon \(2002\). [_A First Course in Probability_](https://archive.org/details/firstcourseinpro00ross). Englewood Cliffs: Prentice Hall. [ISBN](ISBN.md) [0-13-033851-6](https://en.wikipedia.org/wiki/Special:BookSources/0-13-033851-6).
