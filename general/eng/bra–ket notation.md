---
aliases:
  - Dirac notation
  - Dirac notations
  - bra
  - bra-ket notation
  - bra-ket notations
  - bras
  - bra–ket notation
  - bra–ket notations
  - ket
  - kets
tags:
  - flashcard/active/general/eng/bra-ket_notation
  - language/in/English
---

# bra–ket notation

__Bra–ket notation__, also called {@{__Dirac notation__}@}, is {@{a notation for [linear algebra](linear%20algebra.md) and [linear operators](linear%20map.md) on complex [vector spaces](vector%20space.md) together with their [dual space](dual%20space.md) both in the finite-[dimensional](dimension%20(vector%20space).md) and infinite-dimensional case}@}. <!--SR:!2025-07-02,267,330!2025-04-17,191,310-->

## quantum mechanics

In [quantum mechanics](quantum%20mechanics.md), bra–ket notation is used ubiquitously to {@{denote quantum states}@}. The notation uses {@{[angle brackets](bracket.md#angle%20brackets), $\langle$ (bra-) and $\rangle$ (-ket), and a [vertical bar](vertical%20bar.md) $|$}@}, to construct {@{"bras" and "kets"}@}. <!--SR:!2025-04-22,212,330!2025-01-04,128,310!2025-05-04,222,330-->

A __ket__ is of the form {@{$|v\rangle$}@}. Mathematically, it denotes {@{a [vector](vector%20space.md), $\mathbf v$, in an abstract complex [vector space](vector%20space.md) $V$}@}, and physically it represents {@{a state of some quantum system}@}. A simple case is {@{in the finite-dimensional complex vector space $\mathbb C^n$}@}, a ket can be identified with {@{a [column vector](row%20and%20column%20vectors.md): $$|v\rangle = \mathbf v = \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix}$$}@}. <!--SR:!2025-04-28,218,330!2025-05-19,234,330!2025-06-03,246,330!2025-12-21,383,310!2025-03-16,172,310-->

A __bra__ is of the form {@{$\langle f|$}@}. Mathematically, it denotes {@{a [linear form](linear%20form.md) $f: V \to \mathbb C$, i.e. a [linear map](linear%20map.md) that maps each vector in $V$ to a complex number $\mathbb C$}@}. Letting the linear functional {@{$\langle f|$ act on a vector $|v \rangle$, $f(\mathbf v)$}@}, is written as {@{$\langle f | v \rangle$}@}. A simple case is {@{in the finite-dimensional complex vector space $\mathbb C^n$}@}, a bra can be identified with {@{a [row vector](row%20and%20column%20vectors.md): $$\langle f| = \mathbf f = \begin{bmatrix} f_1 & \cdots & f_n \end{bmatrix}$$}@}. Applying the linear functional $\langle f|$ on a vector $|v \rangle$ is then {@{a [matrix multiplication](matrix%20multiplication.md): $$\langle f|v \rangle = \mathbf f \mathbf v = \begin{bmatrix} f_1 & \cdots & f_n \end{bmatrix} \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \sum_{k = 1}^n f_k v_k$$}@}. <!--SR:!2025-05-23,239,330!2025-08-11,300,330!2025-08-11,300,330!2025-05-13,229,330!2025-01-30,148,310!2025-06-10,252,330!2025-07-03,268,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bra–ket_notation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
