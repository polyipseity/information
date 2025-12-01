---
aliases:
  - Einstein notation
  - Einstein notations
  - Einstein sum convention
  - Einstein sum conventions
  - Einstein sum notation
  - Einstein sum notations
  - Einstein summation convention
  - Einstein summation conventions
  - Einstein summation notation
  - Einstein summation notations
tags:
  - flashcard/active/general/eng/Einstein_notation
  - language/in/English
---

# Einstein notation

In {@{[mathematics](mathematics.md), especially the usage of [linear algebra](linear%20algebra.md) in [mathematical physics](mathematical%20physics.md) and [differential geometry](differential%20geometry.md)}@}, {@{__Einstein notation__ \(also known as the __Einstein summation convention__ or __Einstein summation notation__\)}@} is {@{a notational convention that implies [summation](summation.md) over a set of indexed terms in a formula}@}, thus {@{achieving brevity}@}. As {@{part of mathematics}@} it is {@{a notational subset of [Ricci calculus](Ricci%20calculus.md)}@}; however, it is often used in {@{physics applications}@} that {@{do not distinguish between [tangent](tangent%20space.md) and [cotangent spaces](cotangent%20space.md)}@}. It was introduced {@{to physics by [Albert Einstein](Albert%20Einstein.md) in 1916}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-12-29,64,310!2025-12-31,66,310!2025-12-20,57,310!2025-12-30,65,310!2025-12-30,65,310!2025-12-31,66,310!2025-12-18,55,310!2025-12-25,61,310!2025-12-31,66,310-->

## introduction

### statement of convention

According to {@{this convention}@}, when {@{an index variable appears twice in a single [term](addend.md#addend)}@} and is {@{not otherwise defined \(see [Free and bound variables](free%20and%20bound%20variables.md)\)}@}, it implies {@{summation of that term over all the values of the index}@}. So where the indices can {@{range over the [set](set%20(mathematics).md) {1, 2, 3}<!-- flashcard separator -->}@}, {@{$$y=\sum _{i=1}^{3}x^{i}e_{i}=x^{1}e_{1}+x^{2}e_{2}+x^{3}e_{3}$$}@} is simplified by the convention to: {@{$$y=x^{i}e_{i}$$}@} <!--SR:!2025-12-28,63,310!2025-12-31,66,310!2025-12-11,46,290!2025-12-31,66,310!2025-12-21,58,310!2025-12-23,59,310!2026-01-01,67,310-->

{@{The upper indices}@} are {@{not [exponents](exponentiation.md) but are indices}@} of {@{coordinates, [coefficients](coefficient.md) or [basis vectors](basis%20vector.md)}@}. That is, in this context {@{_x_<sup>2</sup>}@} should be understood as {@{the second component of _x_ rather than the square of _x_}@} \(this can {@{occasionally lead to ambiguity}@}\). {@{The upper index position}@} in _x_<sup>_i_</sup> is because, typically, an index occurs {@{once in an upper \(superscript\) and once in a lower \(subscript\) position in a term}@} \(see _[§ Application](#application)_ below\). Typically, {@{\(_x_<sup>1</sup> _x_<sup>2</sup> _x_<sup>3</sup>\)}@} would be equivalent to {@{the traditional \(_x_ _y_ _z_\)}@}. <!--SR:!2025-12-30,65,310!2025-12-18,55,310!2025-12-27,63,310!2025-12-29,64,310!2026-01-01,67,310!2025-12-24,60,310!2025-12-30,65,310!2026-01-01,67,310!2025-12-19,56,310!2026-01-01,67,310-->

In {@{[general relativity](general%20relativity.md)}@}, {@{a common convention}@} is that <!--SR:!2025-12-31,66,310!2025-12-23,59,310-->

- the [Greek alphabet](Greek%20alphabet.md) ::@:: is used for space and time components, where indices take on values 0, 1, 2, or 3 \(frequently used letters are _μ_, _ν_, ...\), <!--SR:!2026-01-01,67,310!2025-12-26,62,310-->
- the [Latin alphabet](Latin%20alphabet.md) ::@:: is used for spatial components only, where indices take on values 1, 2, or 3 \(frequently used letters are _i_, _j_, ...\), <!--SR:!2025-12-29,64,310!2025-12-29,64,310-->

In general, indices can {@{range over any [indexing set](indexed%20family.md), including an [infinite set](infinite%20set.md)}@}. This should not be confused with {@{a typographically similar convention}@} used to distinguish between {@{[tensor index notation](tensor%20index%20notation.md) and the closely related but distinct basis-independent [abstract index notation](abstract%20index%20notation.md)}@}. <!--SR:!2025-12-28,63,310!2025-12-26,62,310!2025-12-20,57,310-->

{@{An index that is summed over}@} is {@{a _summation index_}@}, in this case "_i_<!-- markdown separator -->&hairsp;". It is also called {@{a [dummy index](bound%20variable.md)}@} since {@{any symbol can replace "_i_<!-- markdown separator -->&hairsp;" without changing the meaning of the expression}@} \(provided that it {@{does not collide with other index symbols in the same term}@}\). <!--SR:!2025-12-20,57,310!2025-12-28,63,310!2026-01-01,67,310!2025-12-26,62,310!2025-12-24,60,310-->

{@{An index that is not summed over}@} is {@{a [_free index_](free%20variable.md)}@} and should {@{appear only once per term}@}. If {@{such an index does appear}@}, it usually also {@{appears in every other term in an equation}@}. An example of a free index is the "_i_<!-- markdown separator -->&hairsp;" in {@{the equation $v_{i}=a_{i}b_{j}x^{j}$}@}, which is equivalent to {@{the equation $v_{i}=\sum _{j}(a_{i}b_{j}x^{j})$}@}. <!--SR:!2025-12-24,60,310!2025-12-18,55,310!2025-12-29,64,310!2025-12-21,58,310!2026-01-01,67,310!2025-12-28,63,310!2025-12-31,66,310-->

### application

Einstein notation can be {@{applied in slightly different ways}@}. Typically, {@{each index}@} occurs {@{once in an upper \(superscript\) and once in a lower \(subscript\) position in a term}@}; however, the convention can be applied {@{more generally to any repeated indices within a term}@}.<sup>[\[2\]](#^ref-2)</sup> When dealing with {@{[covariant and contravariant](covariance%20and%20contravariance%20of%20vectors.md) vectors}@}, where {@{the position of an index indicates the type of vector}@}, {@{the first case}@} usually applies; {@{a covariant vector}@} can only be {@{contracted with a contravariant vector}@}, corresponding to {@{summation of the products of coefficients}@}. On the other hand, when there is {@{a fixed coordinate basis \(or when not considering coordinate vectors\)}@}, one may choose to {@{use only subscripts}@}; see {@{_[§ Superscripts and subscripts versus only subscripts](#superscripts%20and%20subscripts%20versus%20only%20subscripts)_}@} below. <!--SR:!2025-12-30,65,310!2026-01-01,67,310!2025-12-30,65,310!2025-12-29,64,310!2025-12-21,58,310!2025-12-19,56,310!2025-12-25,61,310!2025-12-25,61,310!2025-12-28,63,310!2025-12-30,65,310!2026-01-01,67,310!2025-12-31,66,310!2025-12-29,64,310-->

## vector representations

### superscripts and subscripts versus only subscripts

In terms of {@{[covariance and contravariance of vectors](covariance%20and%20contravariance%20of%20vectors.md)}@}, <!--SR:!2026-01-01,67,310-->

- upper indices ::@:: represent components of [contravariant vectors](covariance%20and%20contravariance%20of%20vectors.md) \([vectors](coordinate%20vector.md)\), <!--SR:!2025-12-31,66,310!2025-12-29,64,310-->
- lower indices ::@:: represent components of [covariant](covariant%20vector.md) vectors \([covectors](covector.md)\). <!--SR:!2025-12-08,44,290!2025-12-24,60,310-->

They {@{transform contravariantly or covariantly}@}, respectively, with respect to {@{[change of basis](change%20of%20basis.md)}@}. <!--SR:!2025-12-31,66,310!2025-12-31,66,310-->

In {@{recognition of this fact}@}, the following notation uses {@{the same symbol both for a vector or covector and its _components_}@}, as in: {@{$${\begin{aligned}v=v^{i}e_{i}={\begin{bmatrix}e_{1}&e_{2}&\cdots &e_{n}\end{bmatrix} }{\begin{bmatrix}v^{1}\\v^{2}\\\vdots \\v^{n}\end{bmatrix} }\\w=w_{i}e^{i}={\begin{bmatrix}w_{1}&w_{2}&\cdots &w_{n}\end{bmatrix} }{\begin{bmatrix}e^{1}\\e^{2}\\\vdots \\e^{n}\end{bmatrix} }\end{aligned} }$$}@} where {@{$v$ is the vector and $v^{i}$ are its components \(not the $i$th covector $v$\)}@}, {@{$w$ is the covector and $w_{i}$ are its components}@}. {@{The basis vector elements $e_{i}$}@} are {@{each column vectors}@}, and {@{the covector basis elements $e^{i}$}@} are {@{each row covectors}@}. \(See also {@{[§ Abstract description](#abstract%20description); [duality](dual%20basis.md)}@}, below and the [examples](dual%20basis.md#examples)\) <!--SR:!2025-12-27,63,310!2026-01-01,67,310!2025-12-24,60,310!2025-12-27,63,310!2025-12-28,63,310!2025-12-19,56,310!2026-01-01,67,310!2025-12-31,66,310!2025-12-29,64,310!2025-12-20,57,310-->

In {@{the presence of a [non-degenerate form](degenerate%20bilinear%20form.md)}@} \({@{an [isomorphism](isomorphism.md) _V_ → _V_<sup>∗</sup>}@}, for instance {@{a [Riemannian metric](Riemannian%20metric.md#Riemannian%20metrics%20and%20Riemannian%20manifolds) or [Minkowski metric](Minkowski%20metric.md#Minkowski%20metric)}@}\), one can {@{[raise and lower indices](raising%20and%20lowering%20indices.md)}@}. <!--SR:!2026-01-01,67,310!2025-12-19,56,310!2026-01-01,67,310!2025-12-23,59,310-->

{@{A basis}@} gives {@{such a \(annotation: non-degenerate\) form \(via the [dual basis](dual%20basis.md)\)}@}, hence when working on {@{__R__<sup>_n_</sup> with a [Euclidean metric](Euclidean%20metric.md) and a fixed [orthonormal basis](orthonormal%20basis.md)}@}, one has the option to {@{work with only subscripts}@}. <!--SR:!2025-12-21,58,310!2025-12-31,66,310!2025-12-23,59,310!2025-12-31,66,310-->

However, if {@{one changes coordinates}@}, {@{the way that coefficients change}@} depends on {@{the variance of the object}@}, and one cannot {@{ignore the distinction}@}; see {@{[Covariance and contravariance of vectors](covariance%20and%20contravariance%20of%20vectors.md)}@}. <!--SR:!2025-12-20,57,310!2025-12-26,62,310!2025-12-29,64,310!2025-12-21,58,310!2025-12-28,63,310-->

### mnemonics

In the above example, {@{vectors}@} are represented as {@{_n_ × 1 [matrices](matrix%20(mathematics).md) \(column vectors\)}@}, while {@{covectors are represented as 1 × _n_ matrices \(row covectors\)}@}. <!--SR:!2025-12-27,63,310!2025-12-21,58,310!2025-12-25,61,310-->

When using {@{the column vector convention}@}: <!--SR:!2025-12-18,55,310-->

- \(annotation: direction mnemonic\) ::@:: "__Up__<!-- markdown separator -->per indices go __up__ to down; __l__<!-- markdown separator -->ower indices go __l__<!-- markdown separator -->eft to right." <!--SR:!2026-01-01,67,310!2026-01-01,67,310-->
- \(annotation: word mnemonic\) ::@:: "__Co__<!-- markdown separator -->variant tensors are __row__ vectors that have indices that are __below__ \(__co-row-below__\)." <!--SR:!2025-12-20,57,310!2025-12-31,66,310-->
- Covectors are row vectors: $${\begin{bmatrix}w_{1}&\cdots &w_{k}\end{bmatrix} }.$$ ::@:: Hence the lower index indicates which _column_ you are in. <!--SR:!2025-12-31,66,310!2025-12-31,66,310-->
- Contravariant vectors are column vectors: $${\begin{bmatrix}v^{1}\\\vdots \\v^{k}\end{bmatrix} }$$ ::@:: Hence the upper index indicates which _row_ you are in. <!--SR:!2025-12-29,64,310!2025-12-18,55,310-->

### abstract description

{@{The virtue of Einstein notation}@} is that it represents {@{the [invariant](invariant%20(mathematics).md) quantities with a simple notation}@}. <!--SR:!2025-12-19,56,310!2025-12-20,57,310-->

In {@{physics}@}, {@{a [scalar](scalar%20(physics).md)}@} is {@{invariant under transformations of basis}@}. In particular, {@{a [Lorentz scalar](Lorentz%20scalar.md)}@} is {@{invariant under a [Lorentz transformation](Lorentz%20transformation.md)}@}. {@{The individual terms in the sum}@} are {@{not}@}. When {@{the basis is changed}@}, {@{the _components_ of a vector}@} change by {@{a [linear transformation](linear%20transformation.md) described by a matrix}@}. This led {@{Einstein to propose the convention}@} that {@{repeated indices imply the summation is to be done}@}. <!--SR:!2025-12-21,58,310!2025-12-29,64,310!2025-12-25,61,310!2025-12-27,63,310!2025-12-26,62,310!2025-12-24,60,310!2026-01-01,67,310!2026-01-01,67,310!2025-12-27,63,310!2025-12-28,63,310!2025-12-19,56,310!2025-12-30,65,310-->

As for {@{covectors}@}, they change by {@{the [inverse matrix](inverse%20matrix.md)}@}. This is designed to {@{guarantee that the linear function associated with the covector, the sum above}@}, is {@{the same no matter what the basis is}@}. <!--SR:!2025-12-31,66,310!2025-12-21,58,310!2026-01-01,67,310!2026-01-01,67,310-->

{@{The value of the Einstein convention}@} is that it applies to {@{other [vector spaces](vector%20space.md) built from _V_}@} using {@{the [tensor product](tensor%20product.md) and [duality](dual%20space.md)}@}. For example, {@{_V_ ⊗ <!-- markdown separator -->_V_}@}, {@{the tensor product of _V_ with itself}@}, has {@{a basis}@} consisting of {@{tensors of the form __e__<sub>_ij_</sub> = __e__<sub>_i_</sub> ⊗ __e__<sub>_j_</sub>}@}. {@{Any tensor __T__ in _V_ ⊗ <!-- markdown separator -->_V_}@} can be written as: {@{$$\mathbf {T} =T^{ij}\mathbf {e} _{ij}.$$}@} <!--SR:!2025-12-21,58,310!2025-12-25,61,310!2025-12-30,65,310!2025-12-28,63,310!2026-01-01,67,310!2025-12-18,55,310!2025-12-18,55,310!2025-12-31,66,310!2025-12-21,58,310-->

{@{_V_<!-- markdown separator -->&hairsp;\*}@}, {@{the dual of _V_}@}, has {@{a basis}@} {@{__e__<sup>1</sup>, __e__<sup>2</sup>, ..., __e__<sup>_n_</sup>}@} which obeys {@{the rule $$\mathbf {e} ^{i}(\mathbf {e} _{j})=\delta _{j}^{i}.$$}@} where {@{_δ_ is the [Kronecker delta](Kronecker%20delta.md)}@}. As {@{$$\operatorname {Hom} (V,W)=V^{*}\otimes W$$}@} {@{the row/column coordinates on a matrix}@} correspond to {@{the upper/lower indices on the tensor product}@}. <!--SR:!2025-12-28,63,310!2025-12-23,59,310!2025-12-31,66,310!2025-12-19,56,310!2025-12-30,65,310!2025-12-30,65,310!2025-12-26,62,310!2026-01-01,67,310!2025-12-31,66,310-->

## common operations in this notation

In Einstein notation, {@{the usual element reference $A_{mn}$}@} for {@{the $m$-th row and $n$-th column of matrix $A$}@} becomes {@{${A^{m} }_{n}$}@}. We can then write {@{the following operations in Einstein notation}@} as follows. <!--SR:!2025-12-19,56,310!2025-12-30,65,310!2025-12-31,66,310!2025-12-25,61,310-->

### inner product

{@{The [inner product](inner%20product.md) of two vectors}@} is {@{the sum of the products of their corresponding components}@}, with {@{the indices of one vector lowered}@} \(see {@{[\#Raising and lowering indices](#raising%20and%20lowering%20indices)}@}\): {@{$$\langle \mathbf {u} ,\mathbf {v} \rangle =\langle \mathbf {e} _{i},\mathbf {e} _{j}\rangle u^{i}v^{j}=u_{j}v^{j}$$}@} In the case of {@{an [orthonormal basis](orthonormal%20basis.md)}@}, we have {@{$u^{j}=u_{j}$}@}, and {@{the expression simplifies to}@}: {@{$$\langle \mathbf {u} ,\mathbf {v} \rangle =\sum _{j}u^{j}v^{j}=u_{j}v^{j}$$}@} <!--SR:!2025-12-21,58,310!2026-01-01,67,310!2025-12-29,64,310!2025-12-23,59,310!2025-12-18,55,310!2025-12-28,63,310!2025-12-28,63,310!2025-12-20,57,310!2025-12-28,63,310-->

### vector cross product

In {@{three dimensions}@}, {@{the [cross product](cross%20product.md) of two vectors}@} with respect to {@{a [positively oriented](orientation%20(vector%20space).md) orthonormal basis}@}, meaning that {@{$\mathbf {e} _{1}\times \mathbf {e} _{2}=\mathbf {e} _{3}$}@}, can be expressed as: {@{$$\mathbf {u} \times \mathbf {v} =\varepsilon _{\,jk}^{i}u^{j}v^{k}\mathbf {e} _{i}$$}@} \(annotation: Also applies for {@{_normalized_ cylindrical coordinate basis, _normalized_ spherical coordinate basis, etc.}@}\) Here, {@{$\varepsilon _{\,jk}^{i}=\varepsilon _{ijk}$}@} is {@{the [Levi-Civita symbol](Levi-Civita%20symbol.md)}@}. Since {@{the basis is orthonormal}@}, {@{raising the index $i$ does not alter the value of $\varepsilon _{ijk}$}@}, when {@{treated as a tensor}@}. <!--SR:!2025-12-23,59,310!2026-01-01,67,310!2025-12-28,63,310!2025-12-19,56,310!2026-01-01,67,310!2026-01-01,67,310!2026-04-08,122,290!2026-01-01,67,310!2025-12-26,62,310!2025-12-31,66,310!2025-12-30,65,310-->

### matrix-vector multiplication

{@{The product of a matrix _A<sub>ij</sub>_ with a column vector _v<sub>j</sub>_}@} is: {@{$$\mathbf {u} _{i}=(\mathbf {A} \mathbf {v} )_{i}=\sum _{j=1}^{N}A_{ij}v_{j}$$}@} equivalent to {@{$$u^{i}={A^{i} }_{j}v^{j}$$}@} This is {@{a special case}@} of {@{matrix multiplication}@}. <!--SR:!2026-05-28,173,310!2025-12-25,61,310!2025-12-31,66,310!2026-01-01,67,310!2025-12-27,63,310-->

### matrix multiplication

{@{The [matrix product](matrix%20multiplication.md) of two matrices _A<sub>ij</sub>_ and _B<sub>jk</sub>_}@} is: {@{$$\mathbf {C} _{ik}=(\mathbf {A} \mathbf {B} )_{ik}=\sum _{j=1}^{N}A_{ij}B_{jk}$$}@} equivalent to {@{$${C^{i} }_{k}={A^{i} }_{j}{B^{j} }_{k}$$}@} <!--SR:!2025-12-31,66,310!2025-12-29,64,310!2025-12-24,60,310-->

### trace

For {@{a [square matrix](square%20matrix.md) _A<sup>i</sup><sub>j</sub>_}@}, {@{the [trace](trace%20(linear%20algebra).md)}@} is {@{the sum of the diagonal elements}@}, hence {@{the sum over a common index _A<sup>i</sup><sub>i</sub>_}@}. <!--SR:!2025-12-23,59,310!2026-01-01,67,310!2025-12-20,57,310!2025-12-31,66,310-->

### outer product

{@{The [outer product](outer%20product.md) of the column vector _u<sup>i</sup>_ by the row vector _v<sub>j</sub>_}@} yields {@{an _m_<!-- markdown separator --> × <!-- markdown separator -->_n_ matrix __A__}@}: {@{$${A^{i} }_{j}=u^{i}v_{j}={(uv)^{i} }_{j}$$}@} Since {@{_i_ and _j_ represent two _different_ indices}@}, there is {@{no summation}@} and the indices are {@{not eliminated by the multiplication}@}. <!--SR:!2026-01-01,67,310!2025-12-26,62,310!2025-12-31,66,310!2025-12-20,57,310!2025-12-31,66,310!2025-12-29,64,310-->

### raising and lowering indices

Given {@{a [tensor](tensor.md)}@}, one can {@{[raise an index or lower an index](raising%20and%20lowering%20indices.md)}@} by {@{contracting the tensor with the [metric tensor](metric%20tensor.md), _g<sub>μν</sub>_}@}. For example, taking {@{the tensor _T<sup>α</sup><sub>β</sub>_}@}, one can {@{lower an index}@}: {@{$$g_{\mu \sigma }{T^{\sigma } }_{\beta }=T_{\mu \beta }$$}@} Or one can {@{raise an index}@}: {@{$$g^{\mu \sigma }{T_{\sigma } }^{\alpha }=T^{\mu \alpha }$$}@} <!--SR:!2025-12-18,55,310!2025-12-31,66,310!2025-12-24,60,310!2025-12-31,66,310!2026-01-01,67,310!2025-12-29,64,310!2025-12-30,65,310!2025-12-30,65,310-->

## see also

- [Tensor](tensor.md)
- [Abstract index notation](abstract%20index%20notation.md)
- [Bra–ket notation](bra–ket%20notation.md)
- [Penrose graphical notation](Penrose%20graphical%20notation.md)
- [Levi-Civita symbol](Levi-Civita%20symbol.md)
- [DeWitt notation](DeWitt%20notation.md)

## notes

1. This applies only for numerical indices. The situation is the opposite for [abstract indices](abstract%20indices.md). Then, vectors themselves carry upper abstract indices and covectors carry lower abstract indices, as per the example in the [introduction](#introduction) of this article. Elements of a basis of vectors may carry a lower _numerical_ index and an upper _abstract_ index.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Einstein_notation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFEinstein1916"></a> [Einstein, Albert](Albert%20Einstein.md) \(1916\). ["The Foundation of the General Theory of Relativity"](https://web.archive.org/web/20060829045130/http://www.alberteinstein.info/gallery/gtext3.html). _Annalen der Physik_. __354__ \(7\): 769. [Bibcode](bibcode%20(identifier).md):[1916AnP...354..769E](https://ui.adsabs.harvard.edu/abs/1916AnP...354..769E). [doi](doi%20(identifier).md):[10.1002/andp.19163540702](https://doi.org/10.1002%2Fandp.19163540702). Archived from [the original](http://www.alberteinstein.info/gallery/gtext3.html) \([PDF](PDF.md)\) on 2006-08-29. Retrieved 2006-09-03. <a id="^ref-1"></a>^ref-1
2. ["Einstein Summation"](http://mathworld.wolfram.com/EinsteinSummation.html). Wolfram Mathworld. Retrieved 13 April 2011. <a id="^ref-2"></a>^ref-2

## bibliography

- <a id="CITEREFKuptsov2001"></a> Kuptsov, L. P. \(2001\) \[1994\], ["Einstein rule"](https://www.encyclopediaofmath.org/index.php?title=Einstein_rule), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md).

## external links

> ![Wikibook logo](../../archives/Wikimedia%20Commons/Wikibooks-logo-en-noslogan.svg) The Wikibook _[General Relativity](https://en.wikibooks.org/wiki/General%20Relativity)_ has a page on the topic of: ___[Einstein Summation Notation](https://en.wikibooks.org/wiki/General%20Relativity/Einstein%20Summation%20Notation)___

- <a id="CITEREFRawlings2007"></a> Rawlings, Steve \(2007-02-01\). ["Lecture 10 – Einstein Summation Convention and Vector Identities"](https://web.archive.org/web/20170106185911/http://www-astro.physics.ox.ac.uk/~sr/lectures/vectors/lecture10final.pdfc). Oxford University. Archived from [the original](http://www-astro.physics.ox.ac.uk/~sr/lectures/vectors/lecture10final.pdfc) on 2017-01-06. Retrieved 2008-07-02.
- ["Vector Calculation in Index Notation \(Einstein's Summation Convention\)"](https://www.goldsilberglitzer.at/Rezepte/Rezept004E.pdf) \(PDF\).
- ["Understanding NumPy's einsum"](https://stackoverflow.com/a/33641428). _Stack Overflow_.

|                                                | <!-- - [v](https://en.wikipedia.org/wiki/Template:Tensors) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Tensors) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ATensors) <br/> --> [Tensors](tensor.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                | _[Glossary of tensor theory](glossary%20of%20tensor%20theory.md)_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                      __Scope__ | __[Mathematics](mathematics.md)__ <p>  - [Coordinate system](coordinate%20system.md) <br/> - [Differential geometry](differential%20geometry.md) <br/> - [Dyadic algebra](dyadics.md) <br/> - [Euclidean geometry](Euclidean%20geometry.md) <br/> - [Exterior calculus](exterior%20calculus.md) <br/> - [Multilinear algebra](multilinear%20algebra.md) <br/> - [Tensor algebra](tensor%20algebra.md) <br/> - [Tensor calculus](tensor%20calculus.md)  <p> __- [Physics](physics.md) <br/> - [Engineering](engineering.md)__ <p>  - [Computer vision](computer%20vision.md) <br/> - [Continuum mechanics](continuum%20mechanics.md) <br/> - [Electromagnetism](electromagnetism.md) <br/> - [General relativity](general%20relativity.md) <br/> - [Transport phenomena](transport%20phenomena.md)                                                                                                                                                                                                                                                            |
|                                   __Notation__ | - [Abstract index notation](abstract%20index%20notation.md) <br/> - [Einstein notation](Einstein%20notation.md) <br/> - [Index notation](index%20notation.md) <br/> - [Multi-index notation](multi-index%20notation.md) <br/> - [Penrose graphical notation](Penrose%20graphical%20notation.md) <br/> - [Ricci calculus](Ricci%20calculus.md) <br/> - [Tetrad \(index notation\)](tetrad%20(index%20notation).md) <br/> - [Van der Waerden notation](Van%20der%20Waerden%20notation.md) <br/> - [Voigt notation](Voigt%20notation.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                   __Tensor <br/> definitions__ | - [Tensor \(intrinsic definition\)](tensor%20(intrinsic%20definition).md) <br/> - [Tensor field](tensor%20field.md) <br/> - [Tensor density](tensor%20density.md) <br/> - [Tensors in curvilinear coordinates](tensors%20in%20curvilinear%20coordinates.md) <br/> - [Mixed tensor](mixed%20tensor.md) <br/> - [Antisymmetric tensor](antisymmetric%20tensor.md) <br/> - [Symmetric tensor](symmetric%20tensor.md) <br/> - [Tensor operator](tensor%20operator.md) <br/> - [Tensor bundle](tensor%20bundle.md) <br/> - [Two-point tensor](two-point%20tensor.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| __[Operations](operation%20(mathematics).md)__ | - [Covariant derivative](covariant%20derivative.md) <br/> - [Exterior covariant derivative](exterior%20covariant%20derivative.md) <br/> - [Exterior derivative](exterior%20derivative.md) <br/> - [Exterior product](exterior%20product.md) <br/> - [Hodge star operator](Hodge%20star%20operator.md) <br/> - [Lie derivative](Lie%20derivative.md) <br/> - [Raising and lowering indices](raising%20and%20lowering%20indices.md) <br/> - [Symmetrization](symmetrization.md) <br/> - [Tensor contraction](tensor%20contraction.md) <br/> - [Tensor product](tensor%20product.md) <br/> - [Transpose](transpose.md) \(2nd-order tensors\)                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                 __Related <br/> abstractions__ | - [Affine connection](affine%20connection.md) <br/> - [Basis](basis%20(linear%20algebra).md) <br/> - [Cartan formalism \(physics\)](Cartan%20formalism%20(physics).md) <br/> - [Connection form](connection%20form.md) <br/> - [Covariance and contravariance of vectors](covariance%20and%20contravariance%20of%20vectors.md) <br/> - [Differential form](differential%20form.md) <br/> - [Dimension](dimension.md) <br/> - [Exterior form](exterior%20form.md) <br/> - [Fiber bundle](fiber%20bundle.md) <br/> - [Geodesic](geodesic.md) <br/> - [Levi-Civita connection](Levi-Civita%20connection.md) <br/> - [Linear map](linear%20map.md) <br/> - [Manifold](manifold.md) <br/> - [Matrix](matrix%20(mathematics).md) <br/> - [Multivector](multivector.md) <br/> - [Pseudotensor](pseudotensor.md) <br/> - [Spinor](spinor.md) <br/> - [Vector](vector%20(mathematics%20and%20physics).md) <br/> - [Vector space](vector%20space.md)                                                                                                                   |
|                            __Notable tensors__ | __Mathematics__ <p>  - [Kronecker delta](Kronecker%20delta.md) <br/> - [Levi-Civita symbol](Levi-Civita%20symbol.md) <br/> - [Metric tensor](metric%20tensor.md) <br/> - [Nonmetricity tensor](nonmetricity%20tensor.md) <br/> - [Ricci curvature](Ricci%20curvature.md) <br/> - [Riemann curvature tensor](Riemann%20curvature%20tensor.md) <br/> - [Torsion tensor](torsion%20tensor.md) <br/> - [Weyl tensor](Weyl%20tensor.md)  <p> __Physics__ <p>  - [Moment of inertia](moment%20of%20inertia.md#inertia%20tensor) <br/> - [Angular momentum tensor](angular%20momentum.md#angular%20momentum%20in%20relativistic%20mechanics) <br/> - [Spin tensor](spin%20tensor.md) <br/> - [Cauchy stress tensor](Cauchy%20stress%20tensor.md) <br/> - [stress–energy tensor](stress–energy%20tensor.md) <br/> - [Einstein tensor](Einstein%20tensor.md) <br/> - [EM tensor](electromagnetic%20tensor.md) <br/> - [Gluon field strength tensor](gluon%20field%20strength%20tensor.md) <br/> - [Metric tensor \(GR\)](metric%20tensor%20(general%20relativity).md) |
|         __[Mathematicians](mathematician.md)__ | - [Élie Cartan](Élie%20Cartan.md) <br/> - [Augustin-Louis Cauchy](Augustin-Louis%20Cauchy.md) <br/> - [Elwin Bruno Christoffel](Elwin%20Bruno%20Christoffel.md) <br/> - [Albert Einstein](Albert%20Einstein.md) <br/> - [Leonhard Euler](Leonhard%20Euler.md) <br/> - [Carl Friedrich Gauss](Carl%20Friedrich%20Gauss.md) <br/> - [Hermann Grassmann](Hermann%20Grassmann.md) <br/> - [Tullio Levi-Civita](Tullio%20Levi-Civita.md) <br/> - [Gregorio Ricci-Curbastro](Gregorio%20Ricci-Curbastro.md) <br/> - [Bernhard Riemann](Bernhard%20Riemann.md) <br/> - [Jan Arnoldus Schouten](Jan%20Arnoldus%20Schouten.md) <br/> - [Woldemar Voigt](Woldemar%20Voigt.md) <br/> - [Hermann Weyl](Hermann%20Weyl.md)                                                                                                                                                                                                                                                                                                                                                |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Mathematical notation](https://en.wikipedia.org/wiki/Category:Mathematical%20notation)
> - [Multilinear algebra](https://en.wikipedia.org/wiki/Category:Multilinear%20algebra)
> - [Tensors](https://en.wikipedia.org/wiki/Category:Tensors)
> - [Riemannian geometry](https://en.wikipedia.org/wiki/Category:Riemannian%20geometry)
> - [Mathematical physics](https://en.wikipedia.org/wiki/Category:Mathematical%20physics)
> - [Albert Einstein](https://en.wikipedia.org/wiki/Category:Albert%20Einstein)
