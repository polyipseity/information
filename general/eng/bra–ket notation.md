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

__Bra–ket notation__, also called {@{__Dirac notation__}@}, is {@{a notation for [linear algebra](linear%20algebra.md) and [linear operators](linear%20map.md) on complex [vector spaces](vector%20space.md) together with their [dual space](dual%20space.md) both in the finite-[dimensional](dimension%20(vector%20space).md) and infinite-dimensional case}@}. <!--SR:!2028-10-27,1213,350!2027-07-11,815,330-->

## quantum mechanics

In [quantum mechanics](quantum%20mechanics.md), bra–ket notation is used ubiquitously to {@{denote quantum states}@}. The notation uses {@{[angle brackets](bracket.md#angle%20brackets), $\langle$ (bra-) and $\rangle$ (-ket), and a [vertical bar](vertical%20bar.md) $|$}@}, to construct {@{"bras" and "kets"}@}. <!--SR:!2027-12-20,972,350!2026-07-07,549,330!2028-02-10,1009,350-->

A __ket__ is of the form {@{$|v\rangle$}@}. Mathematically, it denotes {@{a [vector](vector%20space.md), $\mathbf v$, in an abstract complex [vector space](vector%20space.md) $V$}@}, and physically it represents {@{a state of some quantum system}@}. A simple case is {@{in the finite-dimensional complex vector space $\mathbb C^n$}@}, a ket can be identified with {@{a [column vector](row%20and%20column%20vectors.md): $$|v\rangle = \mathbf v = \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix}$$}@}. <!--SR:!2028-01-16,992,350!2028-04-14,1058,350!2028-06-26,1119,350!2025-12-21,383,310!2027-03-24,738,330-->

A __bra__ is of the form {@{$\langle f|$}@}. Mathematically, it denotes {@{a [linear form](linear%20form.md) $f: V \to \mathbb C$, i.e. a [linear map](linear%20map.md) that maps each vector in $V$ to a complex number $\mathbb C$}@}. Letting the linear functional {@{$\langle f|$ act on a vector $|v \rangle$, $f(\mathbf v)$}@}, is written as {@{$\langle f | v \rangle$}@}. A simple case is {@{in the finite-dimensional complex vector space $\mathbb C^n$}@}, a bra can be identified with {@{a [row vector](row%20and%20column%20vectors.md): $$\langle f| = \mathbf f = \begin{bmatrix} f_1 & \cdots & f_n \end{bmatrix}$$}@}. Applying the linear functional $\langle f|$ on a vector $|v \rangle$ is then {@{a [matrix multiplication](matrix%20multiplication.md): $$\langle f|v \rangle = \mathbf f \mathbf v = \begin{bmatrix} f_1 & \cdots & f_n \end{bmatrix} \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \sum_{k = 1}^n f_k v_k$$}@}. <!--SR:!2028-05-15,1087,350!2028-04-27,990,330!2029-05-07,1365,350!2028-03-29,1042,350!2026-10-27,635,330!2028-08-03,1147,350!2028-11-10,1226,350-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bra–ket_notation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
