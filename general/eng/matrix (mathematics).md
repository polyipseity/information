---
aliases:
  - matrices
  - matrix
tags:
  - flashcard/active/general/eng/matrix__mathematics_
  - language/in/English
---

# matrix

## basic operations

### addition, scalar multiplication, subtraction and transposition

#### addition

The _sum_ of {@{two matrices __A__ and __B__ of the same size _m_ × _n_}@} is denoted {@{__A__ + __B__}@}. It is calculated by {@{adding the matrices element-wise}@}: {@{$$(\mathbf{A} + \mathbf{B})_{i, j} = \mathbf{A}_{i, j} + \mathbf{B}_{i, j} \qquad \text{where }1 \le i \le m\text{ and }1 \le j \le n$$}@}. <!--SR:!2025-07-23,311,330!2025-03-28,218,330!2025-04-30,244,330!2025-05-25,264,330-->

#### scalar multiplication

The _product_ of {@{a [scalar](scalar%20(mathematics).md) _c_ and a matrix __A__ of size _m_ × _n_}@} is denoted {@{$c\mathbf{A}$, $c \cdot \mathbf{A}$, or $\mathbf{A} \cdot c$}@}. It is calculated by {@{multiplying every element of __A__ by _c_}@}: {@{$$(c\mathbf{A})_{i, j} = c \cdot \mathbf{A}_{i, j} \qquad \text{where }1 \le i \le m\text{ and }1 \le j \le n$$}@}. <!--SR:!2025-06-22,286,330!2026-11-21,675,330!2026-03-15,469,310!2025-03-19,209,310-->

#### subtraction

The subtraction of {@{a matrix __A__ by another matrix __B__ of the same size}@} is denoted {@{__A__ - __B__}@}. It is defined by {@{[addition](#addition) of __A__ and __B__ that is scalar multiplied by -1}@}: {@{$$\mathbf{A} - \mathbf{B} = \mathbf{A} + (-1) \cdot \mathbf{B}$$}@} <!--SR:!2025-05-12,252,330!2025-05-31,269,330!2026-11-06,668,330!2025-06-07,273,330-->

#### transposition

The _transpose_ of {@{an _m_-by-_n_ matrix __A__}@} is {@{the _n_-by-_m_ matrix denoted by __A__<sup>T</sup>, __A__<sup>tr</sup>, or <sup>t</sup>__A__}@}. It is formed by {@{swapping the row index with the column index for every element of __A__}@}: {@{$$\left(\mathbf{A}^{\text{T} }\right)_{j, i} = \mathbf{A}_{i, j} \qquad \text{where }1 \le i \le m\text{ and }1 \le j \le n$$}@} <!--SR:!2027-06-20,841,330!2025-05-27,267,330!2025-07-13,302,330!2026-11-12,672,330-->

### matrix multiplication

- see: [matrix multiplication](matrix%20multiplication.md)

_Multiplication_ of two matrices is defined iff {@{the number of columns in the left matrix equals the number of rows in the right matrix}@}. Given two matrices {@{__A__, a _m_-by-_p_ matrix, and __B__, a _p_-by-_n_ matrix}@}, the _matrix product_ is denoted {@{__AB__, which does not equal __BA__ in general, and __BA__ may even not be defined}@}. The matrix product element are given by {@{the [dot product](dot%20product.md) between the corresponding row of __A__ and the corresponding column of __B__}@}: {@{$$(\mathbf{A} \mathbf{B})_{i, j} = \sum_{r = 1}^p \mathbf{A}_{i, r} \mathbf{B}_{r, j} = \mathbf{A}_{i, 1} \mathbf{B}_{1, j} + \mathbf{A}_{i, 2} \mathbf{B}_{2, j} + \cdots + \mathbf{A}_{i, p} \mathbf{B}_{p, j} \qquad \text{where }1 \le i \le m\text{ and }1 \le j \le n$$}@}. <!--SR:!2025-04-01,204,310!2025-04-30,216,290!2027-02-07,735,330!2025-03-07,173,270!2026-02-12,439,310-->

## linear equation

- see: [linear equation](linear%20equation.md), [system of linear equations](system%20of%20linear%20equations.md)

Matrices can {@{compactly write and work with multiple [linear equations](linear%20equation.md), that is, a [system of linear equations](system%20of%20linear%20equations.md)}@}. Let {@{__A__ be a _m_-by-_n_ matrix, __x__ be a _n_-by-1 column vector of _n_ variables _x_<sub>1</sub>, _x_<sub>2</sub>, ..., _x_<sub>n</sub>, and __b__ be a _m_-by-1 column vector}@}. Then the matrix equation {@{$$\mathbf{A} \mathbf{x} = \mathbf{b}$$}@} is equivalent to the system of linear equations {@{$$\begin{cases} \mathbf{A}_{1, 1} x_1 + \mathbf{A}_{1, 2} x_2 + \cdots + \mathbf{A}_{1, n} x_n & = b_1 \\ \mathbf{A}_{2, 1} x_1 + \mathbf{A}_{2, 2} x_2 + \cdots + \mathbf{A}_{2, n} x_n & = b_2 \\ & \vdots \\ \mathbf{A}_{m, 1} x_1 + \mathbf{A}_{m, 2} x_2 + \cdots + \mathbf{A}_{m, n} x_n & = b_m \end{cases}$$}@}. <!--SR:!2027-04-05,780,330!2025-06-06,273,330!2025-05-18,243,290!2025-05-24,248,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/matrix_(mathematics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
