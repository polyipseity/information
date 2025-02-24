---
aliases:
  - linear dependence
  - linear independence
  - linearly dependent
  - linearly independent
tags:
  - flashcard/active/general/eng/linear_independence
  - language/in/English
---

# linear independence

## definition

Let $V$ be a [vector space](vector%20space.md) over a [field](field%20(mathematics).md) $F$. A finite [set](set%20(mathematics).md) of $n$ [vectors](vector%20(mathematics%20and%20physics).md) $\vec{v_1}, \vec{v_2}, \ldots, \vec{v_n}$ from $V$ are _linearly dependent_, {@{if and only if there exists $n$ [scalars](scalar%20(mathematics).md) $k_1, k_2, \ldots, k_n$ from $F$ that are not all [zero elements](zero%20element.md), such that $$k_1 \vec{v_1} + k_2 \vec{v_2} + \cdots + k_n \vec{v_n} = \vec{0}$$. [Inversely](inverse%20(logic).md), a finite set of vectors is _linearly independent_ if and only if it is not linearly dependent, i.e. the above equation can only be satisfied by $k_1 = k_2 = \cdots = k_n = 0$}@}. <!--SR:!2028-01-11,1071,310-->

> [!example] examples
>
> - [empty set](empty%20set.md) $\emptyset$ :@: Linearly independent. Consider that the condition for linear dependence uses [existential quantification](existential%20quantification.md) and its [inverse](inverse%20(logic).md) uses [universal quantification](universal%20quantification.md) by [De Morgan's laws](De%20Morgan's%20laws.md), it is linearly independent by [vacuous truth](vacuous%20truth.md). <!--SR:!2025-10-16,458,310-->

### infinite case

An infinite [set](set%20(mathematics).md) of [vectors](vector%20(mathematics%20and%20physics).md) is _linearly dependent_ {@{if and only if it contains a finite [subset](subset.md) that is linearly dependent. [Inversely](inverse%20(logic).md), an infinite set of vectors is _linearly independent_ if and only if it is not _linearly dependent_, i.e. every finite [subset](subset.md) is linearly independent}@}. <!--SR:!2027-05-17,812,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/linear_independence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
