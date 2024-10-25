---
aliases:
  - complex dot product
  - complex dot products
  - dot product
  - dot products
  - inner product
  - inner products
  - norm squared
  - projection product
  - projection products
  - scalar product
  - scalar products
tags:
  - flashcard/active/general/dot_product
  - language/in/English
---

# dot product

In [mathematics](mathematics.md), the __dot product__ or __scalar product__ is {{an [algebraic operation](algebraic%20operation.md) that takes two equal-length sequences of numbers (usually [coordinate vectors](coordinate%20vector.md)), and returns a single number}}. In [Euclidean geometry](euclidean%20geometry.md), {{the dot product of the [Cartesian coordinates](cartesian%20coordinate%20system.md) of two [vectors](euclidean%20vector.md)}} is widely used. It is often called {{the __inner product__ (or rarely __projection product__) of [Euclidean space](euclidean%20space.md)}}, even though {{it is not the only inner product that can be defined on Euclidean space (see [inner product space](inner%20product%20space.md) for more)}}. <!--SR:!2024-10-27,62,310!2024-10-28,63,310!2024-10-26,61,310!2025-05-17,214,330-->

## generalizations

### complex vectors

For {{vectors with [complex](complex%20number.md) entries}}, using the given definition of the dot product would {{lead to quite different properties}}. For instance, {{the dot product of a vector with itself could be zero without the vector being the zero vector (e.g. this would happen with the vector $\mathbf a = [1\ i]$)}}. This in turn would {{have consequences for notions like length and angle}}. Properties such as {{the positive-definite norm can be salvaged at the cost of giving up the symmetric and bilinear properties of the dot product}}, through {{the alternative definition $$\begin{aligned} \mathbf a \cdot \mathbf b & = \sum_i a_i \overline{b_i} && (\text{in mathematics}) \\ \mathbf a \cdot \mathbf b & = \sum_i \overline{a_i} b_i && (\text{in most other fields}) \end{aligned}$$, where $\overline{*}$ is the [complex conjugate](complex%20conjugate.md) of $*$}}. When {{vectors are represented by [column vectors](row%20and%20column%20vectors.md)}}, the dot product can be {{expressed as a [matrix product](matrix%20multiplication.md#matrix%20product%20.28two%20matrices.29) involving a [conjugate transpose](conjugate%20transpose.md), denoted with the superscript $\mathrm H$}}: {{$$\begin{aligned} \mathbf a \cdot \mathbf b & = {\mathbf b}^{\mathrm H} \mathbf a = {\mathbf a}^\intercal \overline{\mathbf b} && (\text{in mathematics}) \\ \mathbf a \cdot \mathbf b & = {\mathbf a}^{\mathrm H} \mathbf b && (\text{in most other fields}) \end{aligned}$$}}. <!--SR:!2025-06-09,236,330!2025-01-16,116,290!2025-01-21,120,290!2024-11-03,67,310!2024-10-26,61,310!2025-03-02,151,310!2025-01-11,111,290!2024-11-02,68,310!2024-11-04,68,310-->

In the case of {{vectors with real components}}, this definition is {{the same as in the real case}}. The dot product of any vector with itself is {{a non-negative real number, and it is nonzero except for the zero vector}}. However, the complex dot product is {{[sesquilinear](sesquilinear%20form.md) rather than bilinear}}, as {{it is [conjugate linear](antilinear%20map.md) instead of linear in $\mathbf b$ (for mathematics) or $\mathbf a$ (for most other fields)}}. The dot product is {{not symmetric}}, since {{$$\mathbf a \cdot \mathbf b = \overline{\mathbf b \cdot \mathbf a}$$}}. The angle between two complex vectors is then given by {{$$\cos⁡ \theta = \frac {\operatorname{Re}⁡(\mathbf a \cdot \mathbf b)} {\lVert \mathbf a \rVert \lVert \mathbf b \rVert}$$}}. <!--SR:!2025-07-11,260,330!2025-07-04,255,330!2024-10-27,62,310!2025-04-22,196,310!2025-05-02,190,310!2025-05-22,219,330!2025-07-03,255,330!2025-04-26,193,310-->

The complex dot product leads to {{the notions of [Hermitian forms](sesquilinear%20form.md#hermitian%20form) and general [inner product spaces](inner%20product%20space.md)}}, which are {{widely used in mathematics and [physics](physics.md)}}. <!--SR:!2025-07-11,261,330!2025-05-03,190,310-->

{{The self dot product of a complex vector $\mathbf a \cdot \mathbf a = {\mathbf a}^{\mathrm H} \mathbf a$}}, involving {{the conjugate transpose of a row vector}}, is also known as {{the __norm squared__, $\mathbf a \cdot \mathbf a = \lVert \mathbf a \rVert^2$, after the [Euclidean norm](Euclidean%20space.md#Euclidean%20norm)}}; it is {{a vector generalization of the _[absolute square](square%20(algebra).md#absolute%20square)_ of a complex scalar (see also: [squared Euclidean distance](Euclidean%20distance.md#squared%20Euclidean%20distance))}}. <!--SR:!2025-05-17,214,330!2024-10-28,63,310!2025-06-30,253,330!2025-02-05,131,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/dot_product) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
