---
aliases:
  - cross product
  - cross products
  - directed area product
  - directed area products
  - vector product
  - vector products
tags:
  - flashcard/active/general/eng/cross_product
  - language/in/English
---

# cross product

- This article is about {@{the cross product of two vectors in three-dimensional Euclidean space}@}. For other uses, see [Cross product \(disambiguation\)](cross%20product%20(disambiguation).md).

> {@{![The cross product with respect to a right-handed coordinate system](../../archives/Wikimedia%20Commons/Cross%20product%20vector.svg)}@}
>
> {@{The cross product with respect to a right-handed coordinate system}@}

In {@{[mathematics](mathematics.md)}@}, {@{the __cross product__ or __vector product__}@} \(occasionally {@{__directed area product__, to emphasize its geometric significance}@}\) is {@{a [binary operation](binary%20operation.md) on two [vectors](Euclidean%20vector.md) in a three-dimensional [oriented](orientation%20(vector%20space).md) [Euclidean vector space](Euclidean%20vector%20space.md#Euclidean%20vector%20space) \(named here $E$\)}@}, and is denoted by {@{the symbol $\times$}@}. Given {@{two [linearly independent vectors](linearly%20independent%20vectors.md) __a__ and __b__}@}, {@{the cross product, __a__ × __b__}@} \(read {@{"a cross b"}@}\), is {@{a vector that is [perpendicular](perpendicular.md) to both __a__ and __b__}@},<sup>[\[1\]](#^ref-1)</sup> and thus {@{[normal](normal%20(geometry).md) to the plane containing them}@}. It has many applications in {@{mathematics, [physics](physics.md), [engineering](engineering.md), and [computer programming](computer%20programming.md)}@}. It should not be confused with {@{the [dot product](dot%20product.md) \(projection product\)}@}.

{@{The magnitude}@} of the cross product equals {@{the area of a [parallelogram](parallelogram.md) with the vectors for sides}@}; in particular, {@{the magnitude of the product of two perpendicular vectors}@} is {@{the product of their lengths}@}. {@{The [units](unit%20of%20measurement.md)}@} of the cross-product are {@{the product of the units of each vector}@}. If {@{two vectors are [parallel](parallel%20vectors.md#parallel) or are [anti-parallel](antiparallel%20vectors.md#antiparallel)}@} \(that is, they are {@{linearly dependent}@}\), or if {@{either one has zero length}@}, then {@{their cross product is zero}@}.<sup>[\[2\]](#^ref-2)</sup>

The cross product is {@{[anticommutative](anticommutativity.md)}@} \(that is, {@{__a__ × __b__ = − __b__ × __a__}@}\) and is {@{[distributive](distributivity.md) over addition}@}, that is, {@{__a__ × \(__b__ + __c__\) = __a__ × __b__ + __a__ × __c__}@}.<sup>[\[1\]](#^ref-1)</sup> {@{The space $E$ together with the cross product}@} is {@{an [algebra over the real numbers](algebra%20over%20a%20field.md)}@}, which is {@{neither [commutative](commutative.md) nor [associative](associative.md)}@}, but is {@{a [Lie algebra](Lie%20algebra.md) with the cross product being the [Lie bracket](Lie%20bracket.md)}@}.

Like {@{the dot product}@}, it depends on {@{the [metric](metric%20space.md) of [Euclidean space](Euclidean%20space.md)}@}, but {@{unlike the dot product}@}, it also depends on {@{a choice of [orientation](orientation%20(mathematics).md) \(or "[handedness](right-hand%20rule.md)"\)}@} of {@{the space \(it is why an oriented space is needed\)}@}. {@{The resultant vector}@} is {@{invariant of rotation of basis}@}. Due to {@{the dependence on [handedness](right-hand%20rule.md)}@}, the cross product is said to be {@{a [pseudovector](pseudovector.md)}@}.

In {@{connection with the cross product}@}, {@{the [exterior product](exterior%20algebra.md) of vectors}@} can be used in {@{arbitrary dimensions}@} \(with {@{a [bivector](bivector.md) or [2-form](2-form.md) result}@}\) and is {@{independent of the orientation of the space}@}.

The product can be {@{generalized in various ways}@}, using {@{the orientation and metric structure}@} just as for {@{the traditional 3-dimensional cross product}@}; one can, in {@{_n_ dimensions}@}, take {@{the product of _n_ − 1 vectors}@} to produce {@{a vector perpendicular to all of them}@}. But if the product is {@{limited to non-trivial binary products with vector results}@}, it {@{exists only in three and seven dimensions}@}.<sup>[\[3\]](#^ref-3)</sup> {@{The [cross-product in seven dimensions](seven-dimensional%20cross%20product.md)}@} has {@{undesirable properties}@} \(e.g. it {@{[fails](seven-dimensional%20cross%20product.md#relation%20to%20the%20octonions) to satisfy the [Jacobi identity](Jacobi%20identity.md)}@}\), so it is not {@{used in mathematical physics}@} to represent {@{quantities such as multi-dimensional [space-time](space-time.md)}@}.<sup>[\[4\]](#^ref-4)</sup> \(See {@{[§ Generalizations](#generalizations) below for other dimensions}@}.\)

## definition

> {@{![Finding the direction of the cross product by the [right-hand rule](right-hand%20rule.md)](../../archives/Wikimedia%20Commons/Right%20hand%20rule%20cross%20product.svg)}@}
>
> {@{Finding the direction of the cross product by the [right-hand rule](right-hand%20rule.md)}@}

The cross product of {@{two vectors __a__ and __b__}@} is {@{defined only in three-dimensional space}@} and is denoted by {@{__a__ × __b__}@}. In {@{[physics](physics.md) and [applied mathematics](applied%20mathematics.md)}@}, {@{the wedge notation __a__ ∧ __b__}@} is often {@{used \(in conjunction with the name _vector product_\)}@},<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup> although in {@{pure mathematics}@} such notation is usually {@{reserved for just the exterior product}@}, {@{an abstraction of the vector product to _n_ dimensions}@}.

The cross product {@{__a__ × __b__}@} is defined as {@{a vector __c__ that is [perpendicular](perpendicular.md) \(orthogonal\) to both __a__ and __b__}@}, with {@{a direction given by the [right-hand rule](right-hand%20rule.md)}@}<sup>[\[1\]](#^ref-1)</sup> and {@{a magnitude equal to the area of the [parallelogram](parallelogram.md) that the vectors span}@}.<sup>[\[2\]](#^ref-2)</sup>

The cross product is defined by the formula<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> {@{$$\mathbf {a} \times \mathbf {b} =\|\mathbf {a} \|\|\mathbf {b} \|\sin(\theta )\,\mathbf {n} ,$$}@} where

- _θ_ ::@:: is the [angle](angle.md) between __a__ and __b__ in the plane containing them \(hence, it is between 0° and 180°\),
- ‖<!-- markdown separator -->__a__<!-- markdown separator -->‖ and ‖<!-- markdown separator -->__b__<!-- markdown separator -->‖ ::@:: are the [magnitudes](magnitude%20(vector).md) of vectors __a__ and __b__,
- __n__ ::@:: is a [unit vector](unit%20vector.md) [perpendicular](perpendicular.md) to the plane containing __a__ and __b__, with direction such that the ordered set \(__a__, __b__, __n__\) is [positively oriented](orientation%20(vector%20space).md).

If {@{the vectors __a__ and __b__ are parallel}@} \(that is, {@{the angle _θ_ between them is either 0° or 180°}@}\), by {@{the above formula}@}, {@{the cross product of __a__ and __b__}@} is {@{the [zero vector](zero%20vector.md#additive%20identities) __0__}@}.

### direction

> {@{![The cross product __a__ × __b__ \(vertical, in purple\) changes as the angle between the vectors __a__ \(blue\) and __b__ \(red\) changes.](../../archives/Wikimedia%20Commons/Cross%20product.gif)}@}
>
> {@{The cross product __a__ × __b__ \(vertical, in purple\)}@} changes as {@{the angle between the vectors __a__ \(blue\) and __b__ \(red\) changes}@}. The cross product is always {@{orthogonal to both vectors}@}, and has {@{magnitude zero when the vectors are parallel}@} and {@{maximum magnitude ‖<!-- markdown separator -->__a__<!-- markdown separator -->‖‖<!-- markdown separator -->__b__<!-- markdown separator -->‖ when they are orthogonal}@}.

{@{The direction of the vector __n__}@} depends on {@{the chosen orientation of the space}@}. {@{Conventionally}@}, it is given by {@{the right-hand rule}@}, where one simply {@{points the forefinger of the right hand in the direction of __a__}@} and {@{the middle finger in the direction of __b__}@}. Then, {@{the vector __n__ is coming out of the thumb}@} \(see the adjacent picture\). {@{Using this rule}@} implies that the cross product is {@{[anti-commutative](anticommutativity.md)}@}; that is, {@{__b__ × __a__ = −\(__a__ × __b__\)}@}. By {@{pointing the forefinger toward __b__ first}@}, and then {@{pointing the middle finger toward __a__}@}, the thumb will be {@{forced in the opposite direction}@}, {@{reversing the sign of the product vector}@}.

As {@{the cross product operator depends on the orientation of the space}@}, in general {@{the cross product of two vectors}@} is {@{not a "true" vector, but a _pseudovector_}@}. See {@{[§ Handedness](#handedness) for more detail}@}.

## names and origin

> {@{![According to [Sarrus's rule](Sarrus's%20rule.md), the [determinant](determinant.md) of a 3×3 matrix involves multiplications between matrix elements identified by crossed diagonals](../../archives/Wikimedia%20Commons/Sarrus%20rule.svg)}@}
>
> According to {@{[Sarrus's rule](Sarrus's%20rule.md)}@}, {@{the [determinant](determinant.md) of a 3×3 matrix}@} involves {@{multiplications between matrix elements identified by crossed diagonals}@}

In {@{1842, [William Rowan Hamilton](William%20Rowan%20Hamilton.md)}@} first described {@{the algebra of [quaternions](quaternion.md)}@} and {@{the non-commutative Hamilton product}@}. In particular, when {@{the Hamilton product of two vectors}@} \(that is, {@{pure quaternions with zero scalar part}@}\) is performed, it results in {@{a quaternion with a scalar and vector part}@}. {@{The scalar and vector part of this Hamilton product}@} corresponds to {@{the negative of dot product and cross product of the two vectors}@}.

In {@{1881, [Josiah Willard Gibbs](Josiah%20Willard%20Gibbs.md),<sup>[\[10\]](#^ref-10)</sup> and independently [Oliver Heaviside](Oliver%20Heaviside.md)}@}, introduced {@{the notation for both the dot product and the cross product}@} using {@{a period \(__a__ ⋅ __b__\) and an "×" \(__a__ × __b__\), respectively}@}, to denote them.<sup>[\[11\]](#^ref-11)</sup>

In {@{1877, to emphasize the fact that the result of a dot product}@} is {@{a [scalar](scalar%20(mathematics).md) while the result of a cross product is a [vector](Euclidean%20vector.md)}@}, {@{[William Kingdon Clifford](William%20Kingdon%20Clifford.md) coined}@} {@{the alternative names __scalar product__ and __vector product__ for the two operations}@}.<sup>[\[11\]](#^ref-11)</sup> These alternative names are {@{still widely used in the literature}@}.

Both {@{the cross notation \(__a__ × __b__\) and the name _cross product_}@} were possibly inspired by the fact that {@{each [scalar component](scalar%20component.md) of __a__ × __b__}@} is {@{computed by multiplying non-corresponding components of __a__ and __b__}@}. Conversely, {@{a dot product __a__ ⋅ __b__}@} involves {@{multiplications between corresponding components of __a__ and __b__}@}. As {@{explained [below](#matrix%20notation)}@}, {@{the cross product}@} can be expressed in {@{the form of a determinant of a special 3 × 3 matrix}@}. According to {@{[Sarrus's rule](Sarrus's%20rule.md)}@}, this involves {@{multiplications between matrix elements identified by crossed diagonals}@}.

## computing

### coordinate notation

> {@{![[Standard basis](standard%20basis.md) vectors __i__, __j__, __k__ and [vector components](vector%20component.md#decomposition) of __a__, denoted here __a__<sub>x</sub>, __a__<sub>y</sub>, __a__<sub>z</sub>](../../archives/Wikimedia%20Commons/3D%20Vector.svg)}@}
>
> {@{[Standard basis](standard%20basis.md) vectors __i__, __j__, __k__ and [vector components](vector%20component.md#decomposition) of __a__, denoted here __a__<sub>x</sub>, __a__<sub>y</sub>, __a__<sub>z</sub>}@}

If {@{$(\mathbf {\color {blue}{i} } ,\mathbf {\color {red}{j} } ,\mathbf {\color {green}{k} } )$}@} is {@{a positively oriented [orthonormal basis](orthonormal%20basis.md)}@}, {@{the basis vectors}@} satisfy the following equalities<sup>[\[1\]](#^ref-1)</sup> {@{$${\begin{alignedat}{2}\mathbf {\color {blue}{i} } &\times \mathbf {\color {red}{j} } &&=\mathbf {\color {green}{k} } \\\mathbf {\color {red}{j} } &\times \mathbf {\color {green}{k} } &&=\mathbf {\color {blue}{i} } \\\mathbf {\color {green}{k} } &\times \mathbf {\color {blue}{i} } &&=\mathbf {\color {red}{j} } \end{alignedat} }$$}@}

{@{A [mnemonic](mnemonic.md) for these formulas}@} is that they can be {@{deduced from any other of them}@} by {@{a [cyclic permutation](cyclic%20permutation.md) of the basis vectors}@}. {@{This mnemonic applies}@} also to {@{many formulas given in this article}@}.

{@{The [anticommutativity](anticommutativity.md) of the cross product}@}, implies that {@{$${\begin{alignedat}{2}\mathbf {\color {red}{j} } &\times \mathbf {\color {blue}{i} } &&=-\mathbf {\color {green}{k} } \\\mathbf {\color {green}{k} } &\times \mathbf {\color {red}{j} } &&=-\mathbf {\color {blue}{i} } \\\mathbf {\color {blue}{i} } &\times \mathbf {\color {green}{k} } &&=-\mathbf {\color {red}{j} } \end{alignedat} }$$}@}

{@{The anticommutativity of the cross product}@} \(and {@{the obvious lack of linear independence}@}\) also implies that <p> &emsp; {@{$\mathbf {\color {blue}{i} } \times \mathbf {\color {blue}{i} } =\mathbf {\color {red}{j} } \times \mathbf {\color {red}{j} } =\mathbf {\color {green}{k} } \times \mathbf {\color {green}{k} } =\mathbf {0}$}@} \({@{the [zero vector](zero%20vector.md#additive%20identities)}@}\).

{@{These equalities}@}, together with {@{the [distributivity](distributivity.md) and [linearity](linearity.md) of the cross product}@} \(though {@{neither follows easily from the definition given above}@}\), are {@{sufficient to determine the cross product of any two vectors __a__ and __b__}@}. Each vector can be defined as {@{the sum of three orthogonal components parallel to the standard basis vectors}@}: {@{$${\begin{alignedat}{3}\mathbf {a} &=a_{1}\mathbf {\color {blue}{i} } &&+a_{2}\mathbf {\color {red}{j} } &&+a_{3}\mathbf {\color {green}{k} } \\\mathbf {b} &=b_{1}\mathbf {\color {blue}{i} } &&+b_{2}\mathbf {\color {red}{j} } &&+b_{3}\mathbf {\color {green}{k} } \end{alignedat} }$$}@}

{@{Their cross product __a__ × __b__}@} can be {@{expanded using distributivity}@}: {@{$${\begin{aligned}\mathbf {a} \times \mathbf {b} ={}&(a_{1}\mathbf {\color {blue}{i} } +a_{2}\mathbf {\color {red}{j} } +a_{3}\mathbf {\color {green}{k} } )\times (b_{1}\mathbf {\color {blue}{i} } +b_{2}\mathbf {\color {red}{j} } +b_{3}\mathbf {\color {green}{k} } )\\={}&a_{1}b_{1}(\mathbf {\color {blue}{i} } \times \mathbf {\color {blue}{i} } )+a_{1}b_{2}(\mathbf {\color {blue}{i} } \times \mathbf {\color {red}{j} } )+a_{1}b_{3}(\mathbf {\color {blue}{i} } \times \mathbf {\color {green}{k} } )+{}\\&a_{2}b_{1}(\mathbf {\color {red}{j} } \times \mathbf {\color {blue}{i} } )+a_{2}b_{2}(\mathbf {\color {red}{j} } \times \mathbf {\color {red}{j} } )+a_{2}b_{3}(\mathbf {\color {red}{j} } \times \mathbf {\color {green}{k} } )+{}\\&a_{3}b_{1}(\mathbf {\color {green}{k} } \times \mathbf {\color {blue}{i} } )+a_{3}b_{2}(\mathbf {\color {green}{k} } \times \mathbf {\color {red}{j} } )+a_{3}b_{3}(\mathbf {\color {green}{k} } \times \mathbf {\color {green}{k} } )\\\end{aligned} }$$}@}

This can be interpreted as the {@{decomposition of __a__ × __b__}@} into {@{the sum of nine simpler cross products involving vectors aligned with __i__, __j__, or __k__}@}. {@{Each one of these nine cross products}@} operates on {@{two vectors that are easy to handle}@} as they are {@{either parallel or orthogonal to each other}@}. From {@{this decomposition}@}, by {@{using the above-mentioned [equalities](#coordinate%20notation) and collecting similar terms}@}, we obtain: {@{$${\begin{aligned}\mathbf {a} \times \mathbf {b} ={}&\quad \ a_{1}b_{1}\mathbf {0} +a_{1}b_{2}\mathbf {\color {green}{k} } -a_{1}b_{3}\mathbf {\color {red}{j} } \\&-a_{2}b_{1}\mathbf {\color {green}{k} } +a_{2}b_{2}\mathbf {0} +a_{2}b_{3}\mathbf {\color {blue}{i} } \\&+a_{3}b_{1}\mathbf {\color {red}{j} } \ -a_{3}b_{2}\mathbf {\color {blue}{i} } \ +a_{3}b_{3}\mathbf {0} \\={}&(a_{2}b_{3}-a_{3}b_{2})\mathbf {\color {blue}{i} } +(a_{3}b_{1}-a_{1}b_{3})\mathbf {\color {red}{j} } +(a_{1}b_{2}-a_{2}b_{1})\mathbf {\color {green}{k} } \\\end{aligned} }$$}@} meaning that {@{the three [scalar components](scalar%20component.md)}@} of {@{the resulting vector __s__ = _s_<sub>1</sub>__i__ + _s_<sub>2</sub>__j__ + _s_<sub>3</sub>__k__ = __a__ × __b__}@} are {@{$${\begin{aligned}s_{1}&=a_{2}b_{3}-a_{3}b_{2}\\s_{2}&=a_{3}b_{1}-a_{1}b_{3}\\s_{3}&=a_{1}b_{2}-a_{2}b_{1}\end{aligned} }$$}@} Using {@{[column vectors](column%20vector.md)}@}, we can {@{represent the same result as follows}@}: {@{$${\begin{bmatrix}s_{1}\\s_{2}\\s_{3}\end{bmatrix} }={\begin{bmatrix}a_{2}b_{3}-a_{3}b_{2}\\a_{3}b_{1}-a_{1}b_{3}\\a_{1}b_{2}-a_{2}b_{1}\end{bmatrix} }$$}@}

### matrix notation

> {@{![Use of Sarrus's rule to find the cross product of __a__ and __b__](../../archives/Wikimedia%20Commons/Sarrus%20rule%20cross%20product%20ab.svg)}@}
>
> {@{Use of Sarrus's rule to find the cross product of __a__ and __b__}@}

{@{The cross product}@} can also be expressed as {@{the [formal](formal%20calculation.md) determinant}@}:<sup>[\[note 1\]](#^ref-note-1)</sup><sup>[\[1\]](#^ref-1)</sup> {@{$$\mathbf {a\times b} ={\begin{vmatrix}\mathbf {i} &\mathbf {j} &\mathbf {k} \\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\\\end{vmatrix} }$$}@}

{@{This determinant}@} can be {@{computed using [Sarrus's rule](rule%20of%20Sarrus.md) or [cofactor expansion](cofactor%20expansion.md)}@}. Using {@{Sarrus's rule}@}, it expands to {@{$${\begin{aligned}\mathbf {a\times b} &=(a_{2}b_{3}\mathbf {i} +a_{3}b_{1}\mathbf {j} +a_{1}b_{2}\mathbf {k} )-(a_{3}b_{2}\mathbf {i} +a_{1}b_{3}\mathbf {j} +a_{2}b_{1}\mathbf {k} )\\&=(a_{2}b_{3}-a_{3}b_{2})\mathbf {i} -(a_{1}b_{3}-a_{3}b_{1})\mathbf {j} +(a_{1}b_{2}-a_{2}b_{1})\mathbf {k} .\end{aligned} }$$}@} which gives {@{the components of the resulting vector directly}@}.

### using Levi-Civita tensors

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD059 -->

- In {@{any basis}@}, {@{the cross-product $a\times b$}@} is given by {@{the tensorial formula $E_{ijk}a^{i}b^{j}$}@} where {@{$E_{ijk}$ is the covariant [Levi-Civita](Levi-Civita%20symbol.md#Levi-Civita%20tensors) tensor}@} \(we note {@{the position of the indices}@}\). That corresponds to {@{the intrinsic formula given [here](#as%20an%20external%20product)}@}.
- In {@{an orthonormal basis _having the same orientation as the space_}@}, {@{$a\times b$}@} is given by {@{the pseudo-tensorial formula $\varepsilon _{ijk}a^{i}b^{j}$}@} where {@{$\varepsilon _{ijk}$ is the Levi-Civita symbol \(which is a pseudo-tensor\)}@}. That is the formula used {@{for everyday physics}@} but it {@{works only for this special choice of basis}@}.
- In {@{any orthonormal basis}@}, {@{$a\times b$}@} is given by {@{the pseudo-tensorial formula $(-1)^{B}\varepsilon _{ijk}a^{i}b^{j}$}@} where {@{$(-1)^{B}=\pm 1$ indicates whether the basis has the same orientation as the space or not}@}.

<!-- markdownlint-restore -->

{@{The latter formula}@} avoids {@{having to change the orientation of the space}@} when {@{we inverse an orthonormal basis}@}.

## properties

### geometric meaning

- See also: ::@:: [Triple product](triple%20product.md)

> {@{![Figure 1. The area of a parallelogram as the magnitude of a cross product](../../archives/Wikimedia%20Commons/Cross%20product%20parallelogram.svg)}@}
>
> {@{Figure 1. The area of a parallelogram as the magnitude of a cross product}@}

<!-- markdownlint MD028 -->

> {@{![Figure 2. Three vectors defining a parallelepiped](../../archives/Wikimedia%20Commons/Parallelepiped%20volume.svg)}@}
>
> {@{Figure 2. Three vectors defining a parallelepiped}@}

{@{The [magnitude](Euclidean%20norm.md#Euclidean%20norm)}@} of the cross product can be interpreted as {@{the positive [area](area.md) of the [parallelogram](parallelogram.md) having __a__ and __b__ as sides}@} \(see Figure 1\):<sup>[\[1\]](#^ref-1)</sup> {@{$$\left\|\mathbf {a} \times \mathbf {b} \right\|=\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\left|\sin \theta \right|.$$}@}

Indeed, one can also compute {@{the volume _V_ of a [parallelepiped](parallelepiped.md) having __a__, __b__ and __c__ as edges}@} by using {@{a combination of a cross product and a dot product}@}, called {@{[scalar triple product](scalar%20triple%20product.md#scalar%20triple%20product)}@} \(see Figure 2\): {@{$$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )=\mathbf {c} \cdot (\mathbf {a} \times \mathbf {b} ).$$}@}

Since the result of {@{the scalar triple product may be negative}@}, {@{the volume of the parallelepiped}@} is given by {@{its absolute value}@}: {@{$$V=|\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )|.$$}@}

Because the magnitude of the cross product {@{goes by the sine of the angle between its arguments}@}, the cross product can be thought of as {@{a measure of _perpendicularity_}@} in the same way that the dot product is {@{a measure of _parallelism_}@}. Given {@{two [unit vectors](unit%20vectors.md)}@}, {@{their cross product has a magnitude of 1}@} if {@{the two are perpendicular}@} and {@{a magnitude of zero if the two are parallel}@}. {@{The dot product of two unit vectors}@} {@{behaves just oppositely}@}: it is {@{zero when the unit vectors are perpendicular}@} and {@{1 if the unit vectors are parallel}@}.

{@{Unit vectors}@} enable {@{two convenient identities}@}: {@{the dot product}@} of two unit vectors yields {@{the cosine \(which may be positive or negative\) of the angle between the two unit vectors}@}. {@{The magnitude of the cross product}@} of the two unit vectors yields {@{the sine \(which will always be positive\)}@}.

### algebraic properties

> {@{![Cross product [scalar multiplication](scalar%20multiplication.md).](../../archives/Wikimedia%20Commons/Cross%20product%20scalar%20multiplication.svg)}@}
>
> {@{Cross product}@} {@{[scalar multiplication](scalar%20multiplication.md)}@}. __Left:__ {@{Decomposition of __b__}@} into {@{components parallel and perpendicular to __a__}@}. Right: {@{Scaling of the perpendicular components}@} by {@{a positive real number _r_}@} \(if {@{negative}@}, {@{__b__ and the cross product are reversed}@}\).

<!-- markdownlint MD028 -->

> {@{![Cross product distributivity over vector addition.](../../archives/Wikimedia%20Commons/Cross%20product%20distributivity.svg)}@}
>
> {@{Cross product distributivity}@} over {@{vector addition}@}. __Left:__ {@{The vectors __b__ and __c__}@} are {@{resolved into parallel and perpendicular components to __a__}@}. __Right:__ {@{The parallel components}@} {@{vanish in the cross product}@}, {@{only the perpendicular components shown in the plane perpendicular to __a__}@} {@{remain}@}.<sup>[\[12\]](#^ref-12)</sup>

<!-- markdownlint MD028 -->

> {@{![The two nonequivalent triple cross products of three vectors __a__, __b__, __c__.](../../archives/Wikimedia%20Commons/Cross%20product%20triple.svg)}@}
>
> {@{The two nonequivalent triple cross products}@} of {@{three vectors __a__, __b__, __c__}@}. In {@{each case}@}, {@{two vectors}@} {@{define a plane}@}, {@{the other is out of the plane}@} and can be split into {@{parallel and perpendicular components}@} to {@{the cross product of the vectors defining the plane}@}. {@{These components}@} can be found by {@{[vector projection](vector%20projection.md) and [rejection](vector%20rejection.md)}@}. {@{The triple product}@} is {@{in the plane and is rotated as shown}@}.

If {@{the cross product of two vectors}@} is {@{the zero vector \(that is, __a__ × __b__ = __0__\)}@}, then {@{either one or both of the inputs is the zero vector, \(__a__ = __0__ or __b__ = __0__\)}@} or else {@{they are parallel or antiparallel \(__a__ ∥ __b__\)}@} so that {@{the sine of the angle between them is zero}@} \({@{_θ_ = 0° or _θ_ = 180° and sin _θ_ = 0}@}\).

{@{The self cross product of a vector}@} is {@{the zero vector}@}: {@{$$\mathbf {a} \times \mathbf {a} =\mathbf {0} .$$}@}

The cross product is {@{[anticommutative](anticommutativity.md)}@}, {@{$$\mathbf {a} \times \mathbf {b} =-(\mathbf {b} \times \mathbf {a} ),$$}@} {@{[distributive](distributive%20property.md) over addition}@}, {@{$$\mathbf {a} \times (\mathbf {b} +\mathbf {c} )=(\mathbf {a} \times \mathbf {b} )+(\mathbf {a} \times \mathbf {c} ),$$}@} and {@{compatible with scalar multiplication}@} so that {@{$$(r\,\mathbf {a} )\times \mathbf {b} =\mathbf {a} \times (r\,\mathbf {b} )=r\,(\mathbf {a} \times \mathbf {b} ).$$}@}

It is {@{not [associative](associative.md)}@}, but {@{satisfies the [Jacobi identity](Jacobi%20identity.md)}@}: {@{$$\mathbf {a} \times (\mathbf {b} \times \mathbf {c} )+\mathbf {b} \times (\mathbf {c} \times \mathbf {a} )+\mathbf {c} \times (\mathbf {a} \times \mathbf {b} )=\mathbf {0} .$$}@}

{@{Distributivity, linearity and Jacobi identity}@} show that {@{the __R__<sup>3</sup> [vector space](real%20coordinate%20space.md)}@} together with {@{vector addition and the cross product}@} forms {@{a [Lie algebra](Lie%20algebra.md)}@}, {@{the Lie algebra of the real [orthogonal group](orthogonal%20group.md) in 3 dimensions}@}, {@{[SO\(3\)](SO(3).md)}@}. {@{The cross product}@} does not obey {@{the [cancellation law](cancellation%20law.md)}@}; that is, {@{__a__ × __b__ = __a__ × __c__ with __a__ ≠ __0__ does not imply __b__ = __c__}@}, but only that: {@{$${\begin{aligned}\mathbf {0} &=(\mathbf {a} \times \mathbf {b} )-(\mathbf {a} \times \mathbf {c} )\\&=\mathbf {a} \times (\mathbf {b} -\mathbf {c} ).\\\end{aligned} }$$}@}

This can be the case where {@{__b__ and __c__ cancel}@}, but additionally where {@{__a__ and __b__ − __c__ are parallel}@}; that is, they are {@{related by a scale factor _t_}@}, leading to: {@{$$\mathbf {c} =\mathbf {b} +t\,\mathbf {a} ,$$}@} for {@{some scalar _t_}@}.

If, in addition to {@{__a__ × __b__ = __a__ × __c__ and __a__ ≠ __0__}@} as above, it is the case that {@{__a__ ⋅ __b__ = __a__ ⋅ __c__}@} then {@{$${\begin{aligned}\mathbf {a} \times (\mathbf {b} -\mathbf {c} )&=\mathbf {0} \\\mathbf {a} \cdot (\mathbf {b} -\mathbf {c} )&=0,\end{aligned} }$$}@}

As {@{__b__ − __c__}@} cannot be {@{simultaneously parallel \(for the cross product to be __0__\) and perpendicular \(for the dot product to be 0\) to __a__}@}, it must be the case that {@{__b__ and __c__ cancel: __b__ = __c__}@}.

From {@{the geometrical definition}@}, the cross product is {@{invariant under proper [rotations](rotation%20(mathematics).md)}@} about {@{the axis defined by __a__ × __b__}@}. In formulae: <p> &emsp; {@{$(R\mathbf {a} )\times (R\mathbf {b} )=R(\mathbf {a} \times \mathbf {b} )$}@}, where {@{$R$ is a [rotation matrix](rotation%20matrix.md) with $\det(R)=1$}@}.

More generally, the cross product obeys {@{the following identity under [matrix](matrix%20(mathematics).md) transformations}@}: {@{$$(M\mathbf {a} )\times (M\mathbf {b} )=(\det M)\left(M^{-1}\right)^{\mathrm {T} }(\mathbf {a} \times \mathbf {b} )=\operatorname {cof} M(\mathbf {a} \times \mathbf {b} )$$}@} where $M$ is {@{a 3-by-3 [matrix](matrix%20(mathematics).md)}@} and $\left(M^{-1}\right)^{\mathrm {T} }$ is {@{the [transpose](transpose.md) of the [inverse](inverse%20matrix.md)}@} and $\operatorname {cof}$ is {@{the cofactor matrix}@}. It can be readily seen how this formula {@{reduces to the former one}@} if {@{$M$ is a rotation matrix}@}. If {@{$M$ is a 3-by-3 symmetric matrix}@} applied to {@{a generic cross product $\mathbf {a} \times \mathbf {b}$}@}, the following relation holds true: {@{$$M(\mathbf {a} \times \mathbf {b} )=\operatorname {Tr} (M)(\mathbf {a} \times \mathbf {b} )-\mathbf {a} \times M\mathbf {b} +\mathbf {b} \times M\mathbf {a}$$}@} \(annotation: mnemonic: {@{"M ab = Tr a b - Ma b - a Mb"}@}\)

{@{The cross product of two vectors}@} lies in {@{the [null space](null%20space.md)}@} of {@{the 2 × 3 matrix with the vectors as rows}@}: {@{$$\mathbf {a} \times \mathbf {b} \in NS\left({\begin{bmatrix}\mathbf {a} \\\mathbf {b} \end{bmatrix} }\right).$$}@}

For {@{the sum of two cross products}@}, {@{the following identity}@} holds: {@{$$\mathbf {a} \times \mathbf {b} +\mathbf {c} \times \mathbf {d} =(\mathbf {a} -\mathbf {c} )\times (\mathbf {b} -\mathbf {d} )+\mathbf {a} \times \mathbf {d} +\mathbf {c} \times \mathbf {b} .$$}@} \(annotation: mnemonic: {@{"ab+cd = a-c b-d + a d+cb"}@}\)

### differentiation

- Main article: ::@:: [Vector-valued function § Derivative and vector multiplication](vector-valued%20function.md#derivative%20and%20vector%20multiplication)

{@{The [product rule](product%20rule.md)}@} of {@{differential calculus}@} {@{applies to any bilinear operation}@}, and therefore {@{also to the cross product}@}: {@{$${\frac {d}{dt} }(\mathbf {a} \times \mathbf {b} )={\frac {d\mathbf {a} }{dt} }\times \mathbf {b} +\mathbf {a} \times {\frac {d\mathbf {b} }{dt} },$$}@} where {@{__a__ and __b__ are vectors that depend on the real variable _t_}@}.

### triple product expansion

- Main article: ::@:: [Triple product](triple%20product.md)

{@{The cross product}@} is used in {@{both forms of the triple product}@}. {@{The [scalar triple product](scalar%20triple%20product.md#scalar%20triple%20product) of three vectors}@} is defined as {@{$$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} ),$$}@}

It is {@{the signed volume}@} of {@{the [parallelepiped](parallelepiped.md) with edges __a__, __b__ and __c__}@} and as such {@{the vectors can be used in any order}@} that's {@{an [even permutation](even%20permutation.md) of the above ordering}@}. The following therefore {@{are equal}@}: {@{$$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )=\mathbf {c} \cdot (\mathbf {a} \times \mathbf {b} ),$$}@}

{@{The [vector triple product](vector%20triple%20product.md#vector%20triple%20product)}@} is {@{the cross product of a vector with the result of another cross product}@}, and is related to {@{the dot product by the following formula}@} {@{$${\begin{aligned}\mathbf {a} \times (\mathbf {b} \times \mathbf {c} )=\mathbf {b} (\mathbf {a} \cdot \mathbf {c} )-\mathbf {c} (\mathbf {a} \cdot \mathbf {b} )\\(\mathbf {a} \times \mathbf {b} )\times \mathbf {c} =\mathbf {b} (\mathbf {c} \cdot \mathbf {a} )-\mathbf {a} (\mathbf {b} \cdot \mathbf {c} )\end{aligned} }$$}@}

{@{The [mnemonic](mnemonic.md) "BAC minus CAB"}@} is used to {@{remember the order of the vectors in the right hand member}@}. This formula is used in {@{[physics](physics.md) to simplify vector calculations}@}. {@{A special case}@}, regarding {@{[gradients](gradient.md) and useful in [vector calculus](vector%20calculus.md)}@}, is {@{$${\begin{aligned}\nabla \times (\nabla \times \mathbf {f} )&=\nabla (\nabla \cdot \mathbf {f} )-(\nabla \cdot \nabla )\mathbf {f} \\&=\nabla (\nabla \cdot \mathbf {f} )-\nabla ^{2}\mathbf {f} ,\\\end{aligned} }$$}@} where {@{∇<sup>2</sup> is the [vector Laplacian](vector%20Laplacian.md#vector%20Laplacian) operator}@}.

{@{Other identities}@} relate the cross product to {@{the scalar triple product}@}: {@{$${\begin{aligned}(\mathbf {a} \times \mathbf {b} )\times (\mathbf {a} \times \mathbf {c} )&=(\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} ))\mathbf {a} \end{aligned} }$$}@} \(annotation: mnemonic: {@{"ab ac = triple(abc) a"}@}\) <br/> {@{$${\begin{aligned} (\mathbf {a} \times \mathbf {b} )\cdot (\mathbf {c} \times \mathbf {d} )&=\mathbf {b} ^{\mathrm {T} }\left(\left(\mathbf {c} ^{\mathrm {T} }\mathbf {a} \right)I-\mathbf {c} \mathbf {a} ^{\mathrm {T} }\right)\mathbf {d} \\&=(\mathbf {a} \cdot \mathbf {c} )(\mathbf {b} \cdot \mathbf {d} )-(\mathbf {a} \cdot \mathbf {d} )(\mathbf {b} \cdot \mathbf {c} )\end{aligned} }$$}@} \(annotation: mnemonic: {@{"ab⋅cd = (ac) (bd) - (a d)(cb)"}@}\) where {@{_I_ is the identity matrix}@}.

### alternative formulation

{@{The cross product and the dot product}@} are related by: {@{$$\left\|\mathbf {a} \times \mathbf {b} \right\|^{2}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a} \cdot \mathbf {b} )^{2}.$$}@}

{@{The right-hand side}@} is {@{the [Gram determinant](Gramian%20matrix.md) of __a__ and __b__}@}, {@{the square of the area of the parallelogram}@} defined by the vectors. {@{This condition}@} determines {@{the magnitude of the cross product}@}. Namely, since {@{the dot product is defined}@}, in terms of {@{the angle _θ_ between the two vectors}@}, as: {@{$$\mathbf {a\cdot b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\cos \theta ,$$}@} {@{the above given relationship can be rewritten}@} as follows: {@{$$\left\|\mathbf {a\times b} \right\|^{2}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}\left(1-\cos ^{2}\theta \right).$$}@} Invoking {@{the [Pythagorean trigonometric identity](Pythagorean%20trigonometric%20identity.md)}@} one obtains: {@{$$\left\|\mathbf {a} \times \mathbf {b} \right\|=\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\left|\sin \theta \right|,$$}@} which is {@{the magnitude of the cross product expressed in terms of _θ_}@}, equal to {@{the area of the parallelogram defined by __a__ and __b__}@} \(see {@{[definition](#definition) above}@}\).

{@{The combination of this requirement}@} and the property that {@{the cross product be orthogonal to its constituents __a__ and __b__}@} provides {@{an alternative definition of the cross product}@}.<sup>[\[13\]](#^ref-13)</sup>

### cross product inverse

Given {@{two vectors __a__ and __c__ with __a__<!-- markdown separator -->≠<!-- markdown separator -->__0__}@}, {@{the equation __a__ × __b__ = __c__}@} admits {@{solutions for __b__}@} {@{if and only if __a__ is orthogonal to __c__}@} \(that is, if {@{__a__ ⋅ __c__ = 0}@}\). In that case, there exists {@{an infinite family of solutions for __b__}@}, which are {@{$$\mathbf {b} ={\frac {\mathbf {c} \times \mathbf {a} }{\left\|\mathbf {a} \right\|^{2} } }+t\mathbf {a} ,$$}@} where {@{_t_ is an arbitrary constant}@}. \(annotation: Since {@{__a__, __b__, and __c__ in this order forms a orthogonal triad}@}, we can {@{recover a vector in the direction of __b__ using __c__ × __a__}@}. The result is {@{divided by the squared magnitude of __a__}@} because {@{__b__ is "multiplied" twice by __a__ in __c__ × __a__ = \(__a__ × __b__\) × __a__}@}. Finally, {@{the second term}@} is due to {@{the component of __b__ parallel to __a__ not affecting the result of __c__}@}.\)

This can be derived using {@{the triple product expansion}@}: {@{$$\mathbf {c} \times \mathbf {a} =(\mathbf {a} \times \mathbf {b} )\times \mathbf {a} =\left\|\mathbf {a} \right\|^{2}\mathbf {b} -(\mathbf {a} \cdot \mathbf {b} )\mathbf {a}$$}@} {@{Rearrange to solve for __b__}@} to give {@{$$\mathbf {b} ={\frac {\mathbf {c} \times \mathbf {a} }{\left\|\mathbf {a} \right\|^{2} } }+{\frac {\mathbf {a} \cdot \mathbf {b} }{\left\|\mathbf {a} \right\|^{2} } }\mathbf {a}$$}@} {@{The coefficient of the last term \(annotation: which is seen to be the projection of $\mathbf b$ on $\mathbf a$ divided by $\lvert \mathbf a \rvert$\)}@} can be {@{simplified to just the arbitrary constant _t_}@} to {@{yield the result shown above}@}.

### Lagrange's identity

The relation {@{$$\left\|\mathbf {a} \times \mathbf {b} \right\|^{2}\equiv \det {\begin{bmatrix}\mathbf {a} \cdot \mathbf {a} &\mathbf {a} \cdot \mathbf {b} \\\mathbf {a} \cdot \mathbf {b} &\mathbf {b} \cdot \mathbf {b} \\\end{bmatrix} }\equiv \left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a} \cdot \mathbf {b} )^{2}$$}@} can be compared with {@{another relation involving the right-hand side}@}, namely {@{[Lagrange's identity](Lagrange's%20identity.md)}@} expressed as<sup>[\[14\]](#^ref-14)</sup> {@{$$\sum _{1\leq i<j\leq n}\left(a_{i}b_{j}-a_{j}b_{i}\right)^{2}\equiv \left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a\cdot b} )^{2},$$}@} where {@{__a__ and __b__ may be _n_-dimensional vectors}@}. This also shows that {@{the [Riemannian volume form](Riemannian%20volume%20form.md#Riemannian%20volume%20form) for surfaces}@} is {@{exactly the [surface element](volume%20form.md) from vector calculus}@}. In the case where {@{_n_ = 3}@}, combining {@{these two equations}@} results in {@{the expression for the magnitude of the cross product}@} in terms of {@{its components}@}:<sup>[\[15\]](#^ref-15)</sup> {@{$${\begin{aligned}\|\mathbf {a} \times \mathbf {b} \|^{2}&\equiv \sum _{1\leq i<j\leq 3}(a_{i}b_{j}-a_{j}b_{i})^{2}\\&\equiv (a_{1}b_{2}-b_{1}a_{2})^{2}+(a_{2}b_{3}-a_{3}b_{2})^{2}+(a_{3}b_{1}-a_{1}b_{3})^{2}.\end{aligned} }$$}@}

{@{The same result is found}@} directly using {@{the components of the cross product}@} found from {@{$$\mathbf {a} \times \mathbf {b} \equiv \det {\begin{bmatrix}{\hat {\mathbf {i} } }&{\hat {\mathbf {j} } }&{\hat {\mathbf {k} } }\\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\\\end{bmatrix} }.$$}@}

In {@{__R__<sup>3</sup>}@}, {@{Lagrange's equation}@} is {@{a special case of the multiplicativity \|__vw__\| = \|__v__\|\|__w__\|}@} of {@{the norm in the [quaternion algebra](quaternion.md#algebraic%20properties)}@}.

It is {@{a special case of another formula}@}, also sometimes called {@{Lagrange's identity}@}, which is {@{the three dimensional case of the [Binet–Cauchy identity](Binet–Cauchy%20identity.md)}@}:<sup>[\[16\]](#^ref-16)</sup><sup>[\[17\]](#^ref-17)</sup> {@{$$(\mathbf {a} \times \mathbf {b} )\cdot (\mathbf {c} \times \mathbf {d} )\equiv (\mathbf {a} \cdot \mathbf {c} )(\mathbf {b} \cdot \mathbf {d} )-(\mathbf {a} \cdot \mathbf {d} )(\mathbf {b} \cdot \mathbf {c} ).$$}@} \(annotation: mnemonic: {@{"ab⋅cd = (ac) (bd) - (a d)(cb)"}@}\) If {@{__a__ = __c__ and __b__ = __d__}@}, this {@{simplifies to the formula above}@}.

### infinitesimal generators of rotations

- Further information: ::@:: [Infinitesimal rotation matrix § Generators of rotations](infinitesimal%20rotation%20matrix.md#generators%20of%20rotations)

The cross product {@{conveniently describes}@} {@{the infinitesimal generators of [rotations](rotation%20(mathematics).md) in __R__<sup>3</sup>}@}. Specifically, if {@{__n__ is a unit vector in __R__<sup>3</sup>}@} and {@{_R_\(_φ_, <!-- markdown separator -->__n__\)}@} denotes {@{a rotation about the axis through the origin specified by __n__}@}, with {@{angle φ \(measured in radians, counterclockwise when viewed from the tip of __n__\)}@}, then {@{$$\left.{d \over d\phi }\right|_{\phi =0}R(\phi ,{\boldsymbol {n} }){\boldsymbol {x} }={\boldsymbol {n} }\times {\boldsymbol {x} }$$}@} for {@{every vector __x__ in __R__<sup>3</sup>}@}. {@{The cross product with __n__}@} therefore describes {@{the infinitesimal generator of the rotations about __n__}@}. {@{These infinitesimal generators}@} form {@{the [Lie algebra](Lie%20algebra.md) __so__\(3\)}@} of {@{the [rotation group SO\(3\)](rotation%20group%20SO(3).md)}@}, and we obtain the result that {@{the Lie algebra __R__<sup>3</sup> with cross product}@} is {@{isomorphic to the Lie algebra __so__\(3\)}@}.

## alternative ways to compute

### conversion to matrix multiplication

{@{The vector cross product}@} also can be expressed as {@{the product of a [skew-symmetric matrix](skew-symmetric%20matrix.md) and a vector}@}:<sup>[\[16\]](#^ref-16)</sup> {@{$${\begin{aligned}\mathbf {a} \times \mathbf {b} =[\mathbf {a} ]_{\times }\mathbf {b} &={\begin{bmatrix}\,0&\!-a_{3}&\,\,a_{2}\\\,\,a_{3}&0&\!-a_{1}\\-a_{2}&\,\,a_{1}&\,0\end{bmatrix} }{\begin{bmatrix}b_{1}\\b_{2}\\b_{3}\end{bmatrix} }\\\mathbf {a} \times \mathbf {b} ={[\mathbf {b} ]_{\times } }^{\mathrm {\!\!T} }\mathbf {a} &={\begin{bmatrix}\,0&\,\,b_{3}&\!-b_{2}\\-b_{3}&0&\,\,b_{1}\\\,\,b_{2}&\!-b_{1}&\,0\end{bmatrix} }{\begin{bmatrix}a_{1}\\a_{2}\\a_{3}\end{bmatrix} },\end{aligned} }$$}@} where {@{superscript <sup>T</sup> refers to the [transpose](transpose.md) operation}@}, and {@{\[__a__\]<sub>×</sub> is defined}@} by: {@{$$[\mathbf {a} ]_{\times }{\stackrel {\rm {def} }{=} }{\begin{bmatrix}\,\,0&\!-a_{3}&\,\,\,a_{2}\\\,\,\,a_{3}&0&\!-a_{1}\\\!-a_{2}&\,\,a_{1}&\,\,0\end{bmatrix} }.$$}@}

{@{The columns \[__a__\]<sub>×,i</sub>}@} of {@{the skew-symmetric matrix for a vector __a__}@} can be also obtained by {@{calculating the cross product with [unit vectors](unit%20vectors.md)}@}. That is, {@{$$[\mathbf {a} ]_{\times ,i}=\mathbf {a} \times \mathbf { {\hat {e} }_{i} } ,\;i\in \{1,2,3\}$$}@} or {@{$$[\mathbf {a} ]_{\times }=\sum _{i=1}^{3}\left(\mathbf {a} \times \mathbf { {\hat {e} }_{i} } \right)\otimes \mathbf { {\hat {e} }_{i} } ,$$}@} where {@{$\otimes$ is the [outer product](outer%20product.md) operator}@}.

Also, if __a__ is {@{itself expressed as a cross product}@}: {@{$$\mathbf {a} =\mathbf {c} \times \mathbf {d}$$}@} then {@{$$[\mathbf {a} ]_{\times }=\mathbf {d} \mathbf {c} ^{\mathrm {T} }-\mathbf {c} \mathbf {d} ^{\mathrm {T} }.$$}@}

> {@{__Proof by substitution__}@}
>
> {@{Evaluation of the cross product}@} gives {@{$$\mathbf {a} =\mathbf {c} \times \mathbf {d} ={\begin{pmatrix}c_{2}d_{3}-c_{3}d_{2}\\c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}\end{pmatrix} }$$}@} Hence, {@{the left hand side}@} equals {@{$$[\mathbf {a} ]_{\times }={\begin{bmatrix}0&c_{2}d_{1}-c_{1}d_{2}&c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}&0&c_{3}d_{2}-c_{2}d_{3}\\c_{1}d_{3}-c_{3}d_{1}&c_{2}d_{3}-c_{3}d_{2}&0\end{bmatrix} }$$}@} Now, for {@{the right hand side}@}, {@{$$\mathbf {c} \mathbf {d} ^{\mathrm {T} }={\begin{bmatrix}c_{1}d_{1}&c_{1}d_{2}&c_{1}d_{3}\\c_{2}d_{1}&c_{2}d_{2}&c_{2}d_{3}\\c_{3}d_{1}&c_{3}d_{2}&c_{3}d_{3}\end{bmatrix} }$$}@} And {@{its transpose}@} is {@{$$\mathbf {d} \mathbf {c} ^{\mathrm {T} }={\begin{bmatrix}c_{1}d_{1}&c_{2}d_{1}&c_{3}d_{1}\\c_{1}d_{2}&c_{2}d_{2}&c_{3}d_{2}\\c_{1}d_{3}&c_{2}d_{3}&c_{3}d_{3}\end{bmatrix} }$$}@} {@{Evaluation of the right hand side}@} gives {@{$$\mathbf {d} \mathbf {c} ^{\mathrm {T} }-\mathbf {c} \mathbf {d} ^{\mathrm {T} }={\begin{bmatrix}0&c_{2}d_{1}-c_{1}d_{2}&c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}&0&c_{3}d_{2}-c_{2}d_{3}\\c_{1}d_{3}-c_{3}d_{1}&c_{2}d_{3}-c_{3}d_{2}&0\end{bmatrix} }$$}@} {@{Comparison}@} shows that {@{the left hand side equals the right hand side}@}.

This result can be {@{generalized to higher dimensions}@} using {@{[geometric algebra](geometric%20algebra.md)}@}. In particular in {@{any dimension}@} {@{bivectors}@} can be {@{identified with skew-symmetric matrices}@}, so {@{the product}@} between {@{a skew-symmetric matrix and vector}@} is equivalent to {@{the grade-1 part}@} of {@{the product of a bivector and vector}@}.<sup>[\[18\]](#^ref-18)</sup> In {@{three dimensions}@} {@{bivectors}@} are {@{[dual](Hodge%20dual.md) to vectors}@} so {@{the product is equivalent to the cross product}@}, with {@{the bivector instead of its vector dual}@}. In {@{higher dimensions}@} the product can {@{still be calculated}@} but {@{bivectors have more degrees of freedom}@} and are {@{not equivalent to vectors}@}.<sup>[\[18\]](#^ref-18)</sup>

{@{This notation \(annotation: using skew-symmetric matrices\)}@} is also often {@{much easier to work with}@}, for example, in {@{[epipolar geometry](epipolar%20geometry.md)}@}.

From {@{the general properties}@} of the cross product follows immediately that {@{$$[\mathbf {a} ]_{\times }\,\mathbf {a} =\mathbf {0}$$}@}  and   {@{$$\mathbf {a} ^{\mathrm {T} }\,[\mathbf {a} ]_{\times }=\mathbf {0}$$}@} and from fact that {@{\[__a__\]<sub>×</sub> is skew-symmetric}@} it follows that {@{$$\mathbf {b} ^{\mathrm {T} }\,[\mathbf {a} ]_{\times }\,\mathbf {b} =0.$$}@}

The above-mentioned {@{triple product expansion \(bac–cab rule\)}@} can be easily {@{proven using this notation \(annotation: using skew-symmetric matrices\)}@}.

As mentioned above, {@{the Lie algebra __R__<sup>3</sup> with cross product}@} is {@{isomorphic to the Lie algebra __so\(3\)__}@}, whose elements can be {@{identified with the 3×3 skew-symmetric matrices}@}. {@{The map __a__ → \[__a__\]<sub>×</sub>}@} provides {@{an isomorphism between __R__<sup>3</sup> and __so\(3\)__}@}. Under {@{this map}@}, {@{the cross product of 3-vectors}@} corresponds to {@{the [commutator](commutator.md) of 3x3 skew-symmetric matrices}@}.

> __{@{Matrix conversion}@} for {@{cross product with canonical base vectors}@}__
>
> Denoting with {@{$\mathbf {e} _{i}\in \mathbf {R} ^{3\times 1}$}@} the {@{$i$-th canonical base vector}@}, {@{the cross product}@} of {@{a generic vector $\mathbf {v} \in \mathbf {R} ^{3\times 1}$ with $\mathbf {e} _{i}$}@} is given by: {@{$\mathbf {v} \times \mathbf {e} _{i}=\mathbf {C} _{i}\mathbf {v}$}@}, where {@{$$\mathbf {C} _{1}={\begin{bmatrix}0&0&0\\0&0&1\\0&-1&0\end{bmatrix} },\quad \mathbf {C} _{2}={\begin{bmatrix}0&0&-1\\0&0&0\\1&0&0\end{bmatrix} },\quad \mathbf {C} _{3}={\begin{bmatrix}0&1&0\\-1&0&0\\0&0&0\end{bmatrix} }$$}@}
>
> {@{These matrices}@} {@{share the following properties}@}:
>
> - {@{$\mathbf {C} _{i}^{\textrm {T} }=-\mathbf {C} _{i}$}@} \({@{skew-symmetric}@}\);
> - {@{Both trace and determinant}@} are {@{zero}@};
> - \(annotation: {@{rank}@}\) {@{${\text{rank} }(\mathbf {C} _{i})=2$}@};
> - {@{$\mathbf {C} _{i}\mathbf {C} _{i}^{\textrm {T} }=\mathbf {P} _{\mathbf {e} _{i} }^{^{\perp } }$}@} \(see below\);
>
> {@{The [orthogonal projection matrix](projection%20(linear%20algebra).md#orthogonal%20projection)}@} of {@{a vector $\mathbf {v} \neq \mathbf {0}$}@} \(annotation: which maps {@{a vector to its component vector in the direction of $\mathbf v$}@}\) is given by {@{$\mathbf {P} _{\mathbf {v} }=\mathbf {v} \left(\mathbf {v} ^{\textrm {T} }\mathbf {v} \right)^{-1}\mathbf {v} ^{T}$}@}. {@{The projection matrix}@} onto {@{the [orthogonal complement](orthogonal%20complement.md)}@} is given by {@{$\mathbf {P} _{\mathbf {v} }^{^{\perp } }=\mathbf {I} -\mathbf {P} _{\mathbf {v} }$ \(annotation: the original vector subtracted by its component vector in the direction of $\mathbf v$\)}@}, where {@{$\mathbf {I}$ is the identity matrix}@}. For the special case of {@{$\mathbf {v} =\mathbf {e} _{i}$}@}, it can be verified that
>
> {@{$$\mathbf {P} _{\mathbf {e} _{1} }^{^{\perp } }={\begin{bmatrix}0&0&0\\0&1&0\\0&0&1\end{bmatrix} },\quad \mathbf {P} _{\mathbf {e} _{2} }^{^{\perp } }={\begin{bmatrix}1&0&0\\0&0&0\\0&0&1\end{bmatrix} },\quad \mathbf {P} _{\mathbf {e} _{3} }^{^{\perp } }={\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix} }$$}@}
>
> For {@{other properties of orthogonal projection matrices}@}, see {@{[projection \(linear algebra\)](projection%20(linear%20algebra).md)}@}.

### index notation for tensors

{@{The cross product}@} can alternatively be defined in terms of {@{the [Levi-Civita tensor](Levi-Civita%20symbol.md#Levi-Civita%20tensors) _E<sub>ijk</sub>_}@} and {@{a dot product _η<sup>mi</sup>_}@}, which are useful in {@{converting vector notation for tensor applications}@}: {@{$$\mathbf {c} =\mathbf {a\times b} \Leftrightarrow \ c^{m}=\sum _{i=1}^{3}\sum _{j=1}^{3}\sum _{k=1}^{3}\eta ^{mi}E_{ijk}a^{j}b^{k}$$}@} where {@{the [indices](indexed%20family.md) $i,j,k$ correspond to vector components}@}. {@{This characterization of the cross product}@} is often expressed {@{more compactly using the [Einstein summation convention](Einstein%20summation%20convention.md)}@} as {@{$$\mathbf {c} =\mathbf {a\times b} \Leftrightarrow \ c^{m}=\eta ^{mi}E_{ijk}a^{j}b^{k}$$}@} in which {@{repeated indices are summed over the values 1 to 3}@}.

In {@{a positively-oriented orthonormal basis}@} {@{_η<sup>mi</sup>_ = δ<sup>_mi_</sup> \(the [Kronecker delta](Kronecker%20delta.md)\)}@} and {@{$E_{ijk}=\varepsilon _{ijk}$ \(the [Levi-Civita symbol](Levi-Civita%20symbol.md)\)}@}. In that case, this representation is another form of {@{the skew-symmetric representation of the cross product}@}: {@{$$[\varepsilon _{ijk}a^{j}]=[\mathbf {a} ]_{\times }.$$}@}

In {@{[classical mechanics](classical%20mechanics.md)}@}: representing {@{the cross product}@} by using {@{the Levi-Civita symbol}@} can cause {@{mechanical symmetries to be obvious}@} when {@{physical systems are [isotropic](isotropic.md)}@}. \(An example: consider {@{a particle in a [Hooke's law](Hooke's%20law.md) potential}@} in {@{three-space}@}, free to {@{oscillate in three dimensions}@}; {@{none of these dimensions}@} are {@{"special" in any sense}@}, so {@{symmetries lie}@} in {@{the cross-product-represented angular momentum}@}, which are made clear by {@{the abovementioned Levi-Civita representation}@}\).<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>

### mnemonic

> {@{![Mnemonic to calculate a cross product in vector form](../../archives/Wikimedia%20Commons/Cross%20product%20mnemonic.svg)}@}
>
> {@{Mnemonic to calculate a cross product in vector form}@}

- {@{"Xyzzy \(mnemonic\)"}@} redirects here. For other uses, see [Xyzzy](xyzzy%20(disambiguation).md).

{@{The word "xyzzy"}@} can be used to {@{remember the definition of the cross product}@}.

If {@{$$\mathbf {a} =\mathbf {b} \times \mathbf {c}$$}@} where: {@{$$\mathbf {a} ={\begin{bmatrix}a_{x}\\a_{y}\\a_{z}\end{bmatrix} },\ \mathbf {b} ={\begin{bmatrix}b_{x}\\b_{y}\\b_{z}\end{bmatrix} },\ \mathbf {c} ={\begin{bmatrix}c_{x}\\c_{y}\\c_{z}\end{bmatrix} }$$}@} then: {@{$$a_{x}=b_{y}c_{z}-b_{z}c_{y}$$ <br/> $$a_{y}=b_{z}c_{x}-b_{x}c_{z}$$ <br/> $$a_{z}=b_{x}c_{y}-b_{y}c_{x}.$$}@}

{@{The second and third equations}@} can be {@{obtained from the first}@} by {@{simply vertically rotating the subscripts, _x_ → _y_ → _z_ → _x_}@}. {@{The problem}@}, of course, is {@{how to remember the first equation}@}, and {@{two options are available for this purpose}@}: either to {@{remember the relevant two diagonals of Sarrus's scheme}@} \(those {@{containing ___i___}@}\), or to {@{remember the xyzzy sequence}@}.

Since {@{the first diagonal in Sarrus's scheme}@} is just {@{the [main diagonal](main%20diagonal.md) of the [above](#matrix%20notation)-mentioned 3×3 matrix}@}, {@{the first three letters of the word xyzzy}@} can be {@{very easily remembered}@}.

### cross visualization

Similarly to {@{the mnemonic device}@} above, {@{a "cross" or X}@} can be {@{visualized between the two vectors in the equation}@}. This may be helpful for {@{remembering the correct cross product formula}@}.

If {@{$$\mathbf {a} =\mathbf {b} \times \mathbf {c}$$}@} then: {@{$$\mathbf {a} ={\begin{bmatrix}b_{x}\\b_{y}\\b_{z}\end{bmatrix} }\times {\begin{bmatrix}c_{x}\\c_{y}\\c_{z}\end{bmatrix} }.$$}@}

If we want to {@{obtain the formula for $a_{x}$}@} we simply {@{drop the $b_{x}$ and $c_{x}$ from the formula}@}, and {@{take the next two components down}@}: {@{$$a_{x}={\begin{bmatrix}b_{y}\\b_{z}\end{bmatrix} }\times {\begin{bmatrix}c_{y}\\c_{z}\end{bmatrix} }.$$}@} When {@{doing this for $a_{y}$}@} {@{the next two elements down}@} should {@{"wrap around" the matrix}@} so that after {@{the z component comes the x component}@}. For {@{clarity}@}, when {@{performing this operation for $a_{y}$}@}, {@{the next two components}@} should be {@{z and x \(in that order\)}@}. While for {@{$a_{z}$}@} {@{the next two components}@} should be {@{taken as x and y}@}. {@{$$a_{y}={\begin{bmatrix}b_{z}\\b_{x}\end{bmatrix} }\times {\begin{bmatrix}c_{z}\\c_{x}\end{bmatrix} },\ a_{z}={\begin{bmatrix}b_{x}\\b_{y}\end{bmatrix} }\times {\begin{bmatrix}c_{x}\\c_{y}\end{bmatrix} }$$}@}

For {@{$a_{x}$}@} then, if we {@{visualize the cross operator}@} as {@{pointing from an element on the left to an element on the right}@}, we can {@{take the first element on the left}@} and simply {@{multiply by the element that the cross points to in the right-hand matrix}@}. We then {@{subtract the next element down on the left}@}, multiplied by {@{the element that the cross points to here as well}@}. This results in {@{our $a_{x}$ formula}@} – {@{$$a_{x}=b_{y}c_{z}-b_{z}c_{y}.$$}@} We can {@{do this in the same way for $a_{y}$ and $a_{z}$}@} to {@{construct their associated formulas}@}.

## applications

The cross product has {@{applications in various contexts}@}. For example, it is used in {@{computational geometry, physics and engineering}@}. {@{A non-exhaustive list of examples}@} follows.

### computational geometry

The cross product appears in {@{the calculation of the distance}@} of {@{two [skew lines](skew%20lines.md#distance) \(lines not in the same plane\) from each other}@} in {@{three-dimensional space}@}.

The cross product can be used to calculate {@{the normal for a triangle or polygon}@}, an operation frequently {@{performed in [computer graphics](computer%20graphics.md)}@}. For example, {@{the winding of a polygon \(clockwise or anticlockwise\)}@} about {@{a point within the polygon}@} can be calculated by {@{triangulating the polygon \(like spoking a wheel\)}@} and {@{summing the angles \(between the spokes\)}@} using {@{the cross product to keep track of the sign of each angle}@}.

In {@{[computational geometry](computational%20geometry.md) of [the plane](plane%20(geometry).md)}@}, the cross product is used to {@{determine the sign of the [acute angle](acute%20angle.md#types%20of%20angles)}@} defined by {@{three points $p_{1}=(x_{1},y_{1}),p_{2}=(x_{2},y_{2})$ and $p_{3}=(x_{3},y_{3})$}@}. It corresponds to {@{the direction \(upward or downward\)}@} of {@{the cross product of the two coplanar [vectors](vector%20(geometry).md)}@} defined by {@{the two pairs of points}@} {@{$(p_{1},p_{2})$ and $(p_{1},p_{3})$}@}. {@{The sign of the acute angle}@} is {@{the sign of the expression}@} {@{$$P=(x_{2}-x_{1})(y_{3}-y_{1})-(y_{2}-y_{1})(x_{3}-x_{1}),$$}@} which is {@{the signed length}@} of {@{the cross product of the two vectors}@}. To {@{use the cross product}@}, simply {@{extend the 2D vectors $p_{1},p_{2},p_{3}$}@} to {@{co-planar 3D vectors}@} by {@{setting $z_{k}=0$ for each of them}@}.

In {@{the "right-handed" coordinate system}@}, if {@{the result is 0}@}, the points are {@{[collinear](collinear.md)}@}; if {@{it is positive}@}, the three points {@{constitute a positive angle of rotation}@} around {@{$p_{1}$ from $p_{2}$ to $p_{3}$}@}, otherwise {@{a negative angle}@}. From {@{another point of view}@}, {@{the sign of $P$}@} tells whether {@{$p_{3}$ lies to the left or to the right}@} of {@{line $p_{1},p_{2}$}@}.

The cross product is used in calculating {@{the volume of a [polyhedron](polyhedron.md)}@} such as {@{a [tetrahedron](tetrahedron.md#volume) or [parallelepiped](parallelepiped.md#volume)}@}.

### angular momentum and torque

{@{The [angular momentum](angular%20momentum.md) __L__}@} of {@{a particle about a given origin}@} is defined as: {@{$$\mathbf {L} =\mathbf {r} \times \mathbf {p} ,$$}@} where __r__ is {@{the position vector of the particle relative to the origin}@}, __p__ is {@{the linear momentum of the particle}@}.

In {@{the same way}@}, {@{the [moment](moment%20(physics).md) __M__}@} of {@{a force __F__<sub>B</sub> applied at point B around point A}@} is given as: {@{$$\mathbf {M} _{\mathrm {A} }=\mathbf {r} _{\mathrm {AB} }\times \mathbf {F} _{\mathrm {B} }\,$$}@} In {@{mechanics}@} {@{the _moment of a force_}@} is also called {@{_[torque](torque.md)_}@} and written as {@{$\mathbf {\tau }$}@}

Since {@{position __r__, linear momentum __p__ and force __F__}@} are {@{all _true_ vectors}@}, {@{both the angular momentum __L__ and the moment of a force __M__}@} are {@{_pseudovectors_ or _axial vectors_}@}.

### rigid body

The cross product frequently appears in {@{the description of rigid motions}@}. {@{Two points _P_ and _Q_ on a [rigid body](rigid%20body.md)}@} can be related by: {@{$$\mathbf {v} _{P}-\mathbf {v} _{Q}={\boldsymbol {\omega } }\times \left(\mathbf {r} _{P}-\mathbf {r} _{Q}\right)\,$$}@} where $\mathbf {r}$ is {@{the point's position}@}, $\mathbf {v}$ is {@{its velocity}@} and ${\boldsymbol {\omega } }$ is {@{the body's [angular velocity](angular%20velocity.md)}@}.

Since {@{position $\mathbf {r}$ and velocity $\mathbf {v}$}@} are {@{_true_ vectors}@}, {@{the angular velocity ${\boldsymbol {\omega } }$}@} is {@{a _pseudovector_ or _axial vector_}@}.

### Lorentz force

- See also: ::@:: [Lorentz force](Lorentz%20force.md)

The cross product is used to describe {@{the [Lorentz force](Lorentz%20force.md)}@} experienced by {@{a moving electric charge _q<sub>e</sub>_}@}: {@{$$\mathbf {F} =q_{e}\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)$$}@}

Since {@{velocity __v__, force __F__ and electric field __E__}@} are {@{all _true_ vectors}@}, {@{the magnetic field __B__}@} is {@{a _pseudovector_}@}.

### other

In {@{[vector calculus](vector%20calculus.md)}@}, the cross product is used to define {@{the formula for the [vector operator](vector%20operator.md) [curl](curl%20(mathematics).md)}@}.

The trick of {@{rewriting a cross product in terms of a matrix multiplication}@} appears frequently in {@{[epipolar](epipolar%20geometry.md) and multi-view geometry}@}, in particular when {@{deriving matching constraints}@}.

## as an external product

> {@{![The cross product in relation to the exterior product.](../../archives/Wikimedia%20Commons/Exterior%20calc%20cross%20product.svg)}@}
>
> {@{The cross product}@} in relation to {@{the exterior product}@}. In red are {@{the orthogonal [unit vector](unit%20vector.md),}@} and {@{the "parallel" unit bivector}@}.

The cross product can be defined in terms of {@{the exterior product}@}. It can be generalized to {@{an [external product](#external%20product)}@} in {@{other than three dimensions}@}.<sup>[\[19\]](#^ref-19)</sup> This generalization allows {@{a natural geometric interpretation}@} of the cross product. In {@{[exterior algebra](exterior%20algebra.md)}@} {@{the exterior product of two vectors}@} is {@{a bivector}@}. {@{A bivector}@} is {@{an oriented plane element}@}, in much the same way that {@{a vector is an oriented line element}@}. Given {@{two vectors _a_ and _b_}@}, one can view {@{the bivector _a_ ∧ _b_}@} as {@{the oriented parallelogram spanned by _a_ and _b_}@}. The cross product is then obtained by {@{taking the [Hodge star](Hodge%20star.md) of the bivector _a_ ∧ _b_}@}, mapping {@{[2-vectors](p-vector.md) to vectors}@}: {@{$$a\times b=\star (a\wedge b).$$}@}

This can be thought of as {@{the oriented multi-dimensional element}@} {@{"perpendicular" to the bivector}@}. In {@{a _d-_<!-- markdown separator -->dimensional space}@}, {@{Hodge star}@} takes {@{a _k_-vector to a \(_d–k_\)-vector}@}; thus {@{only in _d =_ 3 dimensions}@} is the result {@{an element of dimension one \(3–2 = 1\)}@}, i.e. {@{a vector}@}. For example, in {@{_d =_ 4 dimensions}@}, {@{the cross product of two vectors}@} has {@{dimension 4–2 = 2}@}, giving {@{a bivector}@}. Thus, {@{only in three dimensions}@} does cross product define {@{an algebra structure to multiply vectors}@}.

## handedness

<!-- | ![](../../archives/Wikimedia%20Commons/Ambox%20important.svg) | This section __possibly contains [original research](https://en.wikipedia.org/wiki/Wikipedia:No%20original%20research)__. Please [improve it](https://en.wikipedia.org/w/index.php?title=Cross_product&action=edit) by [verifying](https://en.wikipedia.org/wiki/Wikipedia:Verifiability) the claims made and adding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline_citations). Statements consisting only of original research should be removed. _\(September 2021\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

### consistency

When {@{physics laws}@} are {@{written as equations}@}, it is possible to make {@{an arbitrary choice of the coordinate system}@}, including {@{handedness}@}. One should be careful to {@{never write down an equation}@} where {@{the two sides do not behave equally under all transformations}@} that {@{need to be considered}@}. For example, if {@{one side of the equation}@} is {@{a cross product of two [polar vectors](polar%20vector.md)}@}, one must take into account that {@{the result is an [axial vector](pseudovector.md)}@}. Therefore, for {@{consistency}@}, {@{the other side}@} must {@{also be an axial vector}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> More generally, {@{the result of a cross product}@} may be {@{either a polar vector or an axial vector}@}, depending on {@{the type of its operands \(polar vectors or axial vectors\)}@}. Namely, {@{polar vectors and axial vectors}@} are {@{interrelated in the following ways}@} under {@{application of the cross product}@}:

- polar vector × polar vector :@: = axial vector
- axial vector × axial vector :@: = axial vector
- polar vector × axial vector :@: = polar vector
- axial vector × polar vector :@: = polar vector

or symbolically

- polar × polar :@: = axial
- axial × axial :@: = axial
- polar × axial :@: = polar
- axial × polar :@: = polar

Because the cross product may {@{also be a polar vector}@}, it may {@{not change direction with a mirror image transformation}@}. This happens, according to {@{the above relationships}@}, if {@{one of the operands is a polar vector and the other one is an axial vector}@} \(e.g., {@{the cross product of two polar vectors}@}\). For instance, {@{a [vector triple product](vector%20triple%20product.md#vector%20triple%20product) involving three polar vectors}@} is {@{a polar vector}@}.

{@{A handedness-free approach}@} is possible using {@{exterior algebra}@}.

### the paradox of the orthonormal basis

Let {@{\(__i__, __j__, __k__\)}@} be {@{an orthonormal basis}@}. {@{The vectors __i__, __j__ and __k__}@} do not {@{depend on the orientation of the space}@}. They can even be defined in {@{the absence of any orientation}@}. They can {@{not therefore be axial vectors}@}. But if {@{__i__ and __j__ are polar vectors}@}, then {@{__k__ is an axial vector}@} for {@{__i__ × __j__ = __k__ or __j__ × __i__ = __k__}@}. This is {@{a paradox}@}.

{@{"Axial" and "polar"}@} are {@{_physical_ qualifiers for _physical_ vectors}@}; that is, {@{vectors which represent _physical_ quantities}@} such as {@{the velocity or the magnetic field}@}. {@{The vectors __i__, __j__ and __k__}@} are {@{mathematical vectors}@}, {@{neither axial nor polar}@}.

## generalizations

There are {@{several ways}@} to {@{generalize the cross product to higher dimensions}@}.

### Lie algebra

- Main article: ::@:: [Lie algebra](Lie%20algebra.md)

The cross product can be seen as {@{one of the simplest Lie products}@}, and is thus generalized by {@{[Lie algebras](Lie%20algebra.md)}@}, which are {@{axiomatized as binary products}@} satisfying the axioms of {@{multilinearity, skew-symmetry, and the Jacobi identity}@}. {@{Many Lie algebras}@} exist, and {@{their study}@} is {@{a major field of mathematics, called [Lie theory](Lie%20theory.md)}@}.

For example, {@{the [Heisenberg algebra](Heisenberg%20algebra.md#Heisenberg%20algebra)}@} gives {@{another Lie algebra structure on $\mathbf {R} ^{3}$}@}. In {@{the basis $\{x,y,z\}$}@}, {@{the product}@} is {@{$[x,y]=z,[x,z]=[y,z]=0$}@}.

### quaternions

- Further information: ::@:: [quaternions and spatial rotation](quaternions%20and%20spatial%20rotation.md)

The cross product can also be described in terms of {@{[quaternions](quaternion.md)}@}. In general, if {@{a vector \[_a_<sub>1</sub>, _a_<sub>2</sub>, _a_<sub>3</sub>\]}@} is represented as {@{the quaternion _a_<sub>1</sub>_i_ + _a_<sub>2</sub>_j_ + _a_<sub>3</sub>_k_}@}, {@{the cross product of two vectors}@} can be obtained by {@{taking their product as quaternions}@} and {@{deleting the real part of the result}@}. {@{The real part}@} will be {@{the negative of the dot product of the two vectors}@}.

### octonions

- See also: ::@:: [Seven-dimensional cross product](seven-dimensional%20cross%20product.md) and [Octonion](octonion.md)

{@{A cross product for 7-dimensional vectors}@} can be {@{obtained in the same way}@} by using {@{the [octonions](octonion.md) instead of the quaternions}@}. {@{The nonexistence}@} of {@{nontrivial vector-valued cross products of two vectors in other dimensions}@} is related to {@{the result from [Hurwitz's theorem](Hurwitz's%20theorem%20(normed%20division%20algebras).md)}@} that {@{the only [normed division algebras](normed%20division%20algebra.md)}@} are {@{the ones with dimension 1, 2, 4, and 8}@}.

### exterior product

- Main articles: ::@:: [Exterior algebra](exterior%20algebra.md) and [Comparison of vector algebra and geometric algebra § Cross and exterior products](comparison%20of%20vector%20algebra%20and%20geometric%20algebra.md#cross%20and%20exterior%20products)

In {@{general dimension}@}, there is {@{no direct analogue of the binary cross product}@} that {@{yields specifically a vector}@}. There is however {@{the exterior product}@}, which has {@{similar properties}@}, except that {@{the exterior product of two vectors}@} is now {@{a [2-vector](p-vector.md) instead of an ordinary vector}@}. As {@{mentioned above}@}, the cross product can be interpreted as {@{the exterior product in three dimensions}@} by using {@{the [Hodge star](Hodge%20star.md) operator}@} to map {@{2-vectors to vectors}@}. {@{The Hodge dual of the exterior product}@} yields {@{an \(_n_ − 2\)-vector}@}, which is {@{a natural generalization of the cross product}@} in {@{any number of dimensions}@}.

{@{The exterior product and dot product}@} can be {@{combined \(through summation\)}@} to form {@{the [geometric product](geometric%20algebra.md) in geometric algebra}@}.

### external product

As {@{mentioned above}@}, the cross product can be {@{interpreted in three dimensions}@} as {@{the Hodge dual of the exterior product}@}. In {@{any finite _n_ dimensions}@}, {@{the Hodge dual of the exterior product of _n_ − 1 vectors}@} is {@{a vector}@}. So, instead of {@{a binary operation}@}, in {@{arbitrary finite dimensions}@}, the cross product is generalized as {@{the Hodge dual of the exterior product of some given _n_ − 1 vectors}@}. This generalization is called {@{__external product__}@}.<sup>[\[20\]](#^ref-20)</sup>

### commutator product

- Main articles: ::@:: [Geometric algebra § Extensions of the inner and exterior products](geometric%20algebra.md#extensions%20of%20the%20inner%20and%20exterior%20products), [Cross product § Cross product and handedness](#cross%20product%20and%20handedness), and [Cross product § Lie algebra](#Lie%20algebra)

Interpreting {@{the three-dimensional [vector space](vector%20space.md) of the algebra}@} as {@{the [2-vector](bivector.md) \(not the 1-vector\) [subalgebra](graded%20vector%20space.md)}@} of {@{the three-dimensional geometric algebra}@}, where {@{$\mathbf {i} =\mathbf {e_{2} } \mathbf {e_{3} }$, $\mathbf {j} =\mathbf {e_{1} } \mathbf {e_{3} }$, and $\mathbf {k} =\mathbf {e_{1} } \mathbf {e_{2} }$}@}, the cross product corresponds {@{exactly to the [commutator product](geometric%20algebra.md#extensions%20of%20the%20inner%20and%20exterior%20products)}@} in {@{geometric algebra}@} and both use {@{the same symbol $\times$}@}. {@{The commutator product}@} is defined for {@{2-vectors $A$ and $B$ in geometric algebra}@} as: {@{$$A\times B={\tfrac {1}{2} }(AB-BA),$$}@} where $AB$ is {@{the geometric product}@}.<sup>[\[21\]](#^ref-21)</sup>

{@{The commutator product}@} could be {@{generalised to arbitrary [multivectors](multivector.md#geometric%20algebra)}@} in {@{three dimensions}@}, which results in {@{a multivector}@} consisting of {@{only elements of [grades](graded%20vector%20space.md) 1 \(1-vectors/[true vectors](#handedness)\) and 2 \(2-vectors/pseudovectors\)}@}. While {@{the commutator product of two 1-vectors}@} is indeed {@{the same as the exterior product}@} and yields {@{a 2-vector}@}, {@{the commutator of a 1-vector and a 2-vector}@} yields {@{a true vector}@}, corresponding instead to {@{the [left and right contractions](geometric%20algebra.md#extensions%20of%20the%20inner%20and%20exterior%20products) in geometric algebra}@}. {@{The commutator product of two 2-vectors}@} has {@{no corresponding equivalent product}@}, which is why the commutator product is {@{defined in the first place for 2-vectors}@}. Furthermore, {@{the commutator triple product}@} of {@{three 2-vectors}@} is the same as {@{the [vector triple product](vector%20triple%20product.md#vector%20triple%20product)}@} of {@{the same three pseudovectors in vector algebra}@}. However, {@{the commutator triple product}@} of {@{three 1-vectors in geometric algebra}@} is instead {@{the [negative](sign%20(mathematics).md#sign%20of%20a%20direction) of the [vector triple product](vector%20triple%20product.md#vector%20triple%20product)}@} of {@{the same three true vectors in vector algebra}@}.

{@{Generalizations to higher dimensions}@} is provided by {@{the same commutator product of 2-vectors}@} in {@{higher-dimensional geometric algebras}@}, but {@{the 2-vectors are no longer pseudovectors}@}. Just as {@{the commutator product/cross product of 2-vectors in three dimensions}@} {@{[correspond to the simplest Lie algebra](#Lie%20algebra)}@}, {@{the 2-vector subalgebras of higher dimensional geometric algebra}@} equipped with {@{the commutator product}@} also {@{correspond to the Lie algebras}@}.<sup>[\[22\]](#^ref-22)</sup> Also as in {@{three dimensions}@}, {@{the commutator product}@} could be further {@{generalised to arbitrary multivectors}@}.

### multilinear algebra

In the context of {@{[multilinear algebra](multilinear%20algebra.md)}@}, the cross product can be seen as {@{the \(1,2\)-tensor}@} \({@{a [mixed tensor](mixed%20tensor.md)}@}, specifically {@{a [bilinear map](bilinear%20map.md)}@}\) obtained from {@{the 3-dimensional [volume form](volume%20form.md)}@},<sup>[\[note 2\]](#^ref-note-2)</sup> {@{a \(0,3\)-tensor}@}, by {@{[raising an index](raising%20and%20lowering%20indices.md)}@}.

In detail, {@{the 3-dimensional volume form}@} defines {@{a product $V\times V\times V\to \mathbf {R}$}@}, by {@{taking the determinant of the matrix given by these 3 vectors}@}. By {@{[duality](dual%20space.md)}@}, this is equivalent to {@{a function $V\times V\to V^{*}$}@}, \({@{fixing any two inputs}@} gives {@{a function $V\to \mathbf {R}$}@} by {@{evaluating on the third input}@}\) and in {@{the presence of an [inner product](inner%20product.md)}@} \(such as {@{the dot product}@}; more generally, {@{a non-degenerate bilinear form}@}\), we have {@{an isomorphism $V\to V^{*}$}@}, and thus this yields {@{a map $V\times V\to V$}@}, which is {@{the cross product}@}: {@{a \(0,3\)-tensor}@} \({@{3 vector inputs, scalar output}@}\) has been transformed into {@{a \(1,2\)-tensor}@} \({@{2 vector inputs, 1 vector output}@}\) by {@{"raising an index"}@}.

Translating {@{the above algebra into geometry}@}, {@{the function}@} "{@{volume of the parallelepiped}@} defined by {@{$(a,b,-)$}@}" \(where {@{the first two vectors are fixed}@} and {@{the last is an input}@}\), which defines {@{a function $V\to \mathbf {R}$}@}, can be {@{_represented_ uniquely}@} as {@{the dot product with a vector}@}: {@{this vector}@} is {@{the cross product $a\times b$}@}. From {@{this perspective}@}, the cross product is _defined_ by {@{the [scalar triple product](scalar%20triple%20product.md#scalar%20triple%20product)}@}, {@{$\mathrm {Vol} (a,b,c)=(a\times b)\cdot c$}@}.

In {@{the same way}@}, in {@{higher dimensions}@} one may {@{define generalized cross products}@} by {@{raising indices of the _n_-dimensional volume form}@}, which is {@{a $(0,n)$-tensor}@}. {@{The most direct generalizations of the cross product}@} are to define either:

- a $(1,n-1)$-tensor, ::@:: which takes as input $n-1$ vectors, and gives as output 1 vector – an $(n-1)$-ary vector-valued product, or
- a $(n-2,2)$-tensor, ::@:: which takes as input 2 vectors and gives as output [skew-symmetric tensor](skew-symmetric%20tensor.md) of rank _n_ − 2 – a binary product with rank _n_ − 2 tensor values. One can also define $(k,n-k)$-tensors for other _k_.

{@{These products}@} are {@{all multilinear and skew-symmetric}@}, and can be defined in terms of {@{the determinant and [parity](parity%20(physics).md)}@}.

{@{The $(n-1)$-ary product}@} can be {@{described as follows}@}: given {@{$n-1$ vectors $v_{1},\dots ,v_{n-1}$ in $\mathbf {R} ^{n}$}@}, define {@{their generalized cross product $v_{n}=v_{1}\times \cdots \times v_{n-1}$}@} as:

- perpendicular ::@:: to the hyperplane defined by the $v_{i}$,
- magnitude ::@:: is the volume of the parallelotope defined by the $v_{i}$, which can be computed as the Gram determinant of the $v_{i}$,
- oriented ::@:: so that $v_{1},\dots ,v_{n}$ is positively oriented.

This is {@{the unique multilinear, alternating product}@} which evaluates to {@{$e_{1}\times \cdots \times e_{n-1}=e_{n}$, $e_{2}\times \cdots \times e_{n}=e_{1}$, and so forth}@} for {@{cyclic permutations of indices}@}.

In {@{coordinates}@}, one can give {@{a formula for this $(n-1)$-ary analogue}@} of the cross product in {@{__R__<sup>_n_</sup>}@} by: {@{$$\bigwedge _{i=0}^{n-1}\mathbf {v} _{i}={\begin{vmatrix}v_{1}{}^{1}&\cdots &v_{1}{}^{n}\\\vdots &\ddots &\vdots \\v_{n-1}{}^{1}&\cdots &v_{n-1}{}^{n}\\\mathbf {e} _{1}&\cdots &\mathbf {e} _{n}\end{vmatrix} }.$$}@}

{@{This formula}@} is {@{identical in structure}@} to {@{the determinant formula for the normal cross product in __R__<sup>3</sup>}@} except that {@{the row of basis vectors}@} is {@{the last row in the determinant rather than the first}@}. {@{The reason for this}@} is to ensure that {@{the ordered vectors \(__v__<sub>1</sub>, ..., __v__<sub>_n_<!-- markdown separator -->−1</sub>, Λ<sup>_n_<!-- markdown separator -->–1</sup><sub>i=0</sub>__v__<sub>_i_</sub>\)}@} have {@{a positive [orientation](orientation%20(mathematics).md) with respect to \(__e__<sub>1</sub>, ..., __e__<sub>_n_</sub>\)}@}. If {@{_n_ is odd}@}, this modification {@{leaves the value unchanged}@}, so this convention {@{agrees with the normal definition of the binary product}@}. In the case that {@{_n_ is even}@}, however, the distinction {@{must be kept}@}. {@{This $(n-1)$-ary form}@} enjoys {@{many of the same properties as the vector cross product}@}: it is {@{[alternating](alternating%20form.md#alternating%20multilinear%20forms) and linear in its arguments}@}, it is {@{perpendicular to each argument}@}, and {@{its magnitude}@} gives {@{the hypervolume of the region bounded by the arguments}@}. And just like {@{the vector cross product}@}, it can be defined in {@{a coordinate independent way}@} as {@{the Hodge dual of the wedge product of the arguments}@}. Moreover, {@{the product $[v_{1},\ldots ,v_{n}]:=\bigwedge _{i=0}^{n}v_{i}$}@} satisfies {@{the Filippov identity}@}, {@{$$[[x_{1},\ldots ,x_{n}],y_{2},\ldots ,y_{n}]=\sum _{i=1}^{n}[x_{1},\ldots ,x_{i-1},[x_{i},y_{2},\ldots ,y_{n}],x_{i+1},\ldots ,x_{n}],$$}@} \(annotation: Compare with {@{the Jacobi identity in three dimensions}@}: {@{$(\mathbf a \times \mathbf b) \times \mathbf c = (\mathbf a \times \mathbf c) \times \mathbf b + \mathbf a \times (\mathbf b \times \mathbf c)$}@}, which can be rewritten into {@{$(\mathbf a \times \mathbf b) \times \mathbf c + (\mathbf c \times \mathbf a) \times \mathbf b + (\mathbf b \times \mathbf c) \times \mathbf a = \mathbf 0$}@}.\) and so it {@{endows __R__<sup>n+1</sup>}@} with {@{a structure of n-Lie algebra}@} \(see Proposition 1 of <sup>[\[23\]](#^ref-23)</sup>\).

## history

In {@{1773, [Joseph-Louis Lagrange](Joseph-Louis%20Lagrange.md)}@} used {@{the component form}@} of {@{both the dot and cross products}@} in order to {@{study the [tetrahedron](tetrahedron.md) in three dimensions}@}.<sup>[\[24\]](#^ref-24)</sup><sup>[\[note 3\]](#^ref-note-3)</sup>

In {@{1843, [William Rowan Hamilton](William%20Rowan%20Hamilton.md)}@} introduced {@{the [quaternion](quaternion.md) product}@}, and with it {@{the terms _vector_ and _scalar_}@}. Given {@{two quaternions \[0, __u__\] and \[0, __v__\]}@}, where {@{__u__ and __v__ are vectors in __R__<sup>3</sup>}@}, {@{their quaternion product}@} can be summarized as {@{\[−<!-- markdown separator -->__u__ ⋅ __v__, __u__ × __v__\]}@}. {@{[James Clerk Maxwell](James%20Clerk%20Maxwell.md) used Hamilton's quaternion tools}@} to {@{develop his famous [electromagnetism equations](Maxwell's%20equations.md)}@}, and for {@{this and other reasons}@} {@{quaternions for a time}@} were {@{an essential part of physics education}@}.

In {@{1844, [Hermann Grassmann](Hermann%20Grassmann.md)}@} published {@{a geometric algebra not tied to dimension two or three}@}. Grassmann developed {@{several products}@}, including {@{a cross product represented then by \[uv\]}@}.<sup>[\[25\]](#^ref-25)</sup> \(_See also: {@{[exterior algebra](exterior%20algebra.md)}@}._\)

In {@{1853, [Augustin-Louis Cauchy](Augustin-Louis%20Cauchy.md)}@}, {@{a contemporary of Grassmann}@}, published {@{a paper on algebraic keys}@} which were used to {@{solve equations}@} and had {@{the same multiplication properties as the cross product}@}.<sup>[\[26\]](#^ref-26)</sup><sup>[\[27\]](#^ref-27)</sup>

In {@{1878, [William Kingdon Clifford](William%20Kingdon%20Clifford.md)}@}, known for {@{a [precursor](geometric%20algebra.md) to the [Clifford algebra](Clifford%20algebra.md) named in his honor}@}, published {@{_[Elements of Dynamic](Elements%20of%20Dynamic.md)_}@}, in which {@{the term _vector product_ is attested}@}. In the book, {@{this product of two vectors}@} is defined to have {@{magnitude equal to the [area](area.md)}@} of {@{the [parallelogram](parallelogram.md) of which they are two sides}@}, and {@{direction perpendicular to their plane}@}.<sup>[\[28\]](#^ref-28)</sup>

In {@{lecture notes from 1881, [Gibbs](Josiah%20Willard%20Gibbs.md)}@} represented {@{the cross product by $u\times v$}@} and called it {@{the _skew product_}@}.<sup>[\[29\]](#^ref-29)</sup><sup>[\[30\]](#^ref-30)</sup> In {@{1901, Gibb's student [Edwin Bidwell Wilson](Edwin%20Bidwell%20Wilson.md)}@} {@{edited and extended these lecture notes}@} into {@{the [textbook](textbook.md) _[Vector Analysis](Vector%20Analysis.md)_}@}. Wilson {@{kept the term _skew product_}@}, but observed that {@{the alternative terms _cross product_<sup>[\[note 4\]](#^ref-note-4)</sup> and _vector product_}@} were {@{more frequent}@}.<sup>[\[31\]](#^ref-31)</sup>

In {@{1908, [Cesare Burali-Forti](Cesare%20Burali-Forti.md) and [Roberto Marcolongo](Roberto%20Marcolongo.md)}@} introduced {@{the vector product notation u ∧ v}@}.<sup>[\[25\]](#^ref-25)</sup> This is used in {@{[France](France.md) and other areas until this day}@}, as {@{the symbol $\times$}@} is already used to {@{denote [multiplication](multiplication.md) and the [Cartesian product](Cartesian%20product.md)}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>

## see also

- [Cartesian product](Cartesian%20product.md) ::@:: – a product of two sets
- [Geometric algebra: Rotating systems](geometric%20algebra.md#rotating%20systems)
- [Multiple cross products](multiple%20cross%20products.md#vector%20triple%20product) ::@:: – products involving more than three vectors
- [Multiplication of vectors](multiplication%20of%20vectors.md)
- [Quadruple product](quadruple%20product.md#quadruple%20product)
- [×](×.md) \(the symbol\)

## notes

1. Here, {@{"formal"}@} means that {@{this notation has the form of a determinant}@}, but does not {@{strictly adhere to the definition}@}; it is {@{a mnemonic used to remember the expansion of the cross product}@}. <a id="^ref-note-1"></a>^ref-note-1
2. By {@{a volume form}@} one means {@{a function that takes in _n_ vectors}@} and {@{gives out a scalar}@}, {@{the volume of the [parallelotope](parallelepiped.md#parallelotope) defined by the vectors}@}: {@{$V\times \cdots \times V\to \mathbf {R}$}@}. This is {@{an _n_-ary multilinear skew-symmetric form}@}. In {@{the presence of a basis}@}, such as {@{on $\mathbf {R} ^{n}$}@}, this is given by {@{the determinant}@}, but in {@{an abstract vector space}@}, this is {@{added structure}@}. In terms of {@{[_G_-structures](G-structure.md)}@}, {@{a volume form}@} is {@{an [$$SL$$](special%20linear%20group.md)-structure}@}. <a id="^ref-note-2"></a>^ref-note-2
3. In {@{modern notation}@}, {@{Lagrange}@} defines {@{$\mathbf {\xi } =\mathbf {y} \times \mathbf {z}$, ${\boldsymbol {\eta } }=\mathbf {z} \times \mathbf {x}$, and ${\boldsymbol {\zeta } }=\mathbf {x} \times {\boldsymbol {y} }$}@}. Thereby, {@{the modern $\mathbf {x}$}@} corresponds to {@{the three variables $(x,x',x'')$ in Lagrange's notation}@}. <a id="^ref-note-3"></a>^ref-note-3
4. since {@{A × B}@} is read as {@{"A cross B"}@} <a id="^ref-note-4"></a>^ref-note-4

## references

This text incorporates [content](https://en.wikipedia.org/wiki/cross_product) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFWeisstein"></a> Weisstein, Eric W. ["Cross Product"](https://mathworld.wolfram.com/CrossProduct.html). _Wolfram MathWorld_. Retrieved 2020-09-06. <a id="^ref-1"></a>^ref-1
2. ["Cross Product"](https://www.mathsisfun.com/algebra/vectors-cross-product.html). _<www.mathsisfun.com>_. Retrieved 2020-09-06. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFMassey1983"></a> [Massey, William S.](William%20S.%20Massey.md) \(December 1983\). ["Cross products of vectors in higher dimensional Euclidean spaces"](https://web.archive.org/web/20210226011747/https://pdfs.semanticscholar.org/1f6b/ff1e992f60eb87b35c3ceed04272fb5cc298.pdf) \(PDF\). _The American Mathematical Monthly_. __90__ \(10\): 697–701. [doi](doi%20(identifier).md):[10.2307/2323537](https://doi.org/10.2307%2F2323537). [JSTOR](JSTOR%20(identifier).md#content) [2323537](https://www.jstor.org/stable/2323537). [S2CID](S2CID%20(identifier).md#S2CID) [43318100](https://api.semanticscholar.org/CorpusID:43318100). Archived from [the original](https://pdfs.semanticscholar.org/1f6b/ff1e992f60eb87b35c3ceed04272fb5cc298.pdf) \(PDF\) on 2021-02-26. If one requires only three basic properties of the cross product ... it turns out that a cross product of vectors exists only in 3-dimensional and 7-dimensional Euclidean space. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFArfken"></a> Arfken, George B. _Mathematical Methods for Physicists_ \(4th ed.\). Elsevier. <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFJeffreys, H.Jeffreys, B. S.1999"></a> Jeffreys, H.; Jeffreys, B. S. \(1999\). _Methods of mathematical physics_. Cambridge University Press. [OCLC](OCLC%20(identifier).md#OCLC) [41158050](https://search.worldcat.org/oclc/41158050). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFAcheson, D. J.1990"></a> [Acheson, D. J.](David%20Acheson%20(mathematician).md) \(1990\). _Elementary Fluid Dynamics_. Oxford University Press. [ISBN](ISBN%20(identifier).md) [0198596790](https://en.wikipedia.org/wiki/Special:BookSources/0198596790). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFHowison, Sam2005"></a> Howison, Sam \(2005\). _Practical Applied Mathematics_. Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0521842743](https://en.wikipedia.org/wiki/Special:BookSources/0521842743). <a id="^ref-7"></a>^ref-7
8. [Wilson 1901](#CITEREFWilson1901), p. 60–61. <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFDennis G. ZillMichael R. Cullen2006"></a> Dennis G. Zill; Michael R. Cullen \(2006\). ["Definition 7.4: Cross product of two vectors"](https://books.google.com/books?id=x7uWk8lxVNYC&pg=PA324). _Advanced engineering mathematics_ \(3rd ed.\). Jones & Bartlett Learning. p. 324. [ISBN](ISBN%20(identifier).md) [0-7637-4591-X](https://en.wikipedia.org/wiki/Special:BookSources/0-7637-4591-X). <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFEdwin Bidwell Wilson1913"></a> Edwin Bidwell Wilson \(1913\). "Chapter II. Direct and Skew Products of Vectors". _[Vector Analysis](Vector%20Analysis.md)_. Founded upon the lectures of J. William Gibbs. New Haven: Yale University Press. The dot product is called "direct product", and cross product is called "skew product". <a id="^ref-10"></a>^ref-10
11. [_A History of Vector Analysis_](https://www.math.ucdavis.edu/~temple/MAT21D/SUPPLEMENTARY-ARTICLES/Crowe_History-of-Vectors.pdf) by Michael J. Crowe, Math. UC Davis. <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFM. R. SpiegelS. LipschutzD. Spellman2009"></a> M. R. Spiegel; S. Lipschutz; D. Spellman \(2009\). _Vector Analysis_. Schaum's outlines. McGraw Hill. p. 29. [ISBN](ISBN%20(identifier).md) [978-0-07-161545-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-07-161545-7). <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFWS Massey1983"></a> WS Massey \(Dec 1983\). "Cross products of vectors in higher dimensional Euclidean spaces". _The American Mathematical Monthly_. __90__ \(10\). The American Mathematical Monthly, Vol. 90, No. 10: 697–701. [doi](doi%20(identifier).md):[10.2307/2323537](https://doi.org/10.2307%2F2323537). [JSTOR](JSTOR%20(identifier).md#content) [2323537](https://www.jstor.org/stable/2323537). <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFVladimir A. BoichenkoGennadiĭ Alekseevich LeonovVolker Reitmann2005"></a> Vladimir A. Boichenko; Gennadiĭ Alekseevich Leonov; Volker Reitmann \(2005\). [_Dimension theory for ordinary differential equations_](https://books.google.com/books?id=9bN1-b_dSYsC&pg=PA26). Vieweg+Teubner Verlag. p. 26. [ISBN](ISBN%20(identifier).md) [3-519-00437-2](https://en.wikipedia.org/wiki/Special:BookSources/3-519-00437-2). <a id="^ref-14"></a>^ref-14
15. <a id="CITEREFPertti Lounesto2001"></a> Pertti Lounesto \(2001\). [_Clifford algebras and spinors_](https://books.google.com/books?id=kOsybQWDK4oC&q=%22which+in+coordinate+form+means+Lagrange%27s+identity%22&pg=PA94) \(2nd ed.\). Cambridge University Press. p. 94. [ISBN](ISBN%20(identifier).md) [0-521-00551-5](https://en.wikipedia.org/wiki/Special:BookSources/0-521-00551-5). <a id="^ref-15"></a>^ref-15
16. <a id="CITEREFShuangzhe LiuGõtz Trenkler2008"></a> Shuangzhe Liu; Gõtz Trenkler \(2008\). ["Hadamard, Khatri-Rao, Kronecker and other matrix products"](https://www.researchgate.net/publication/251677036). _Int J Information and Systems Sciences_. __4__ \(1\). Institute for scientific computing and education: 160–177. <a id="^ref-16"></a>^ref-16
17. by <a id="CITEREFEric W. Weisstein2003"></a> Eric W. Weisstein \(2003\). ["Binet-Cauchy identity"](https://books.google.com/books?id=8LmCzWQYh_UC&pg=PA228). _CRC concise encyclopedia of mathematics_ \(2nd ed.\). CRC Press. p. 228. [ISBN](ISBN%20(identifier).md) [1-58488-347-2](https://en.wikipedia.org/wiki/Special:BookSources/1-58488-347-2). <a id="^ref-17"></a>^ref-17
18. <a id="CITEREFLounesto, Pertti2001"></a> Lounesto, Pertti \(2001\). [_Clifford algebras and spinors_](https://archive.org/details/cliffordalgebras00loun). Cambridge: Cambridge University Press. pp. [193](https://archive.org/details/cliffordalgebras00loun/page/n200). [ISBN](ISBN%20(identifier).md) [978-0-521-00551-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-00551-7). <a id="^ref-18"></a>^ref-18
19. <a id="CITEREFGreub, W.1978"></a> Greub, W. \(1978\). _Multilinear Algebra_. <a id="^ref-19"></a>^ref-19
20. <a id="CITEREFHogben, L2007"></a> [Hogben, L](Leslie%20Hogben.md), ed. \(2007\). _Handbook of Linear Algebra_.<sup>\[_[page needed](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources)_\]</sup> <a id="^ref-20"></a>^ref-20
21. <a id="CITEREFArthur2011"></a> Arthur, John W. \(2011\). [_Understanding Geometric Algebra for Electromagnetic Theory_](https://books.google.com/books?id=rxGCaDvBCoAC). [IEEE Press](IEEE%20Press.md). p. 49. [ISBN](ISBN%20(identifier).md) [978-0470941638](https://en.wikipedia.org/wiki/Special:BookSources/978-0470941638). <a id="^ref-21"></a>^ref-21
22. <a id="CITEREFDoranLasenby2003"></a> Doran, Chris; Lasenby, Anthony \(2003\). [_Geometric Algebra for Physicists_](https://books.google.com/books?id=VW4yt0WHdjoC). [Cambridge University Press](Cambridge%20University%20Press.md). pp. 401–408. [ISBN](ISBN%20(identifier).md) [978-0521715959](https://en.wikipedia.org/wiki/Special:BookSources/978-0521715959). <a id="^ref-22"></a>^ref-22
23. <a id="CITEREFFilippov1985"></a> Filippov, V.T. \(1985\). ["n-Lie algebras"](https://link.springer.com/article/10.1007/BF00969110). _Sibirsk. Mat. Zh_. __26__ \(6\): 879–891. [Bibcode](bibcode%20(identifier).md):[1985SibMJ..26..879F](https://ui.adsabs.harvard.edu/abs/1985SibMJ..26..879F). [doi](doi%20(identifier).md):[10.1007/BF00969110](https://doi.org/10.1007%2FBF00969110). [S2CID](S2CID%20(identifier).md#S2CID) [125051596](https://api.semanticscholar.org/CorpusID:125051596). <a id="^ref-23"></a>^ref-23
24. <a id="CITEREFLagrange, Joseph-Louis1773"></a> Lagrange, Joseph-Louis \(1773\). "Solutions analytiques de quelques problèmes sur les pyramides triangulaires". [_Oeuvres_](https://gallica.bnf.fr/ark:/12148/bpt6k229222d/f662.item.zoom). Vol. 3. p. 661. <a id="^ref-24"></a>^ref-24
25. [Cajori \(1929\)](#CITEREFCajori1929), p. [134](https://archive.org/details/historyofmathema00cajo_0/pages/134). <a id="^ref-25"></a>^ref-25
26. [Crowe \(1994\)](#CITEREFCrowe1994), p. [83](https://archive.org/details/historyofvectora0000crow/page/83). <a id="^ref-26"></a>^ref-26
27. <a id="CITEREFCauchy1900"></a> Cauchy, Augustin-Louis \(1900\). _Ouvres_. Vol. 12. p. [16](https://books.google.com/books?id=0k9eAAAAcAAJ&pg=PA16). <a id="^ref-27"></a>^ref-27
28. <a id="CITEREFClifford1878"></a> [Clifford, William Kingdon](William%20Kingdon%20Clifford.md) \(1878\). ["Elements of Dynamic, Part I"](https://archive.org/details/elementsofdynami01clifiala/page/94). London: MacMillan & Co. p. 95. <a id="^ref-28"></a>^ref-28
29. <a id="CITEREFGibbs1884"></a> Gibbs, Josiah Willard \(1884\). [_Elements of vector analysis : arranged for the use of students in physics_](https://archive.org/details/elementsvectora00gibb/page/4). New Haven : Printed by Tuttle, Morehouse & Taylor. <a id="^ref-29"></a>^ref-29
30. [Crowe \(1994\)](#CITEREFCrowe1994), p. [154](https://archive.org/details/historyofvectora0000crow/page/154). <a id="^ref-30"></a>^ref-30
31. [Wilson \(1901\)](#CITEREFWilson1901), p. [61](https://archive.org/details/117714283/page/61). <a id="^ref-31"></a>^ref-31

## bibliography

- <a id="CITEREFCajori1929"></a> [Cajori, Florian](Florian%20Cajori.md) \(1929\). [_A History Of Mathematical Notations Volume II_](https://archive.org/details/historyofmathema00cajo_0). [Open Court Publishing](Open%20Court%20Publishing%20Company.md). p. [134](https://archive.org/details/historyofmathema00cajo_0/pages/134). [ISBN](ISBN%20(identifier).md) [978-0-486-67766-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-67766-8).
- <a id="CITEREFCrowe1994"></a> Crowe, Michael J. \(1994\). [_A History of Vector Analysis_](https://archive.org/details/historyvectorana00crow). Dover. [ISBN](ISBN%20(identifier).md) [0-486-67910-1](https://en.wikipedia.org/wiki/Special:BookSources/0-486-67910-1).
- [E. A. Milne](E.%20A.%20Milne.md) \(1948\) [Vectorial Mechanics](Vectorial%20Mechanics.md), Chapter 2: Vector Product, pp 11 –31, London: [Methuen Publishing](Methuen%20Publishing.md).
- <a id="CITEREFWilson1901"></a> Wilson, Edwin Bidwell \(1901\). [_Vector Analysis: A text-book for the use of students of mathematics and physics, founded upon the lectures of J. Willard Gibbs_](https://archive.org/details/117714283). [Yale University Press](Yale%20University%20Press.md).
- <a id="CITEREFT. Levi-CivitaU. Amaldi1949"></a> T. Levi-Civita; U. Amaldi \(1949\). _Lezioni di meccanica razionale_ \(in Italian\). Bologna: Zanichelli editore.

## external links

- ["Cross product"](https://www.encyclopediaofmath.org/index.php?title=Cross_product), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]
- [A quick geometrical derivation and interpretation of cross products](http://behindtheguesses.blogspot.com/2009/04/dot-and-cross-products.html)
- [An interactive tutorial](https://web.archive.org/web/20060424151900/http://physics.syr.edu/courses/java-suite/crosspro.html) created at [Syracuse University](Syracuse%20University.md) – \(requires [java](Java%20(programming%20language).md)\)
- [W. Kahan \(2007\). Cross-Products and Rotations in Euclidean 2- and 3-Space. University of California, Berkeley \(PDF\).](http://www.cs.berkeley.edu/~wkahan/MathH110/Cross.pdf)
- [The vector product](https://www.mathcentre.ac.uk/resources/uploaded/mc-ty-vectorprod-2009-1.pdf), Mathcentre \(UK\), 2009

|                                                     | <!-- - [v](https://en.wikipedia.org/wiki/Template:Linear%20algebra) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Linear%20algebra) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ALinear%20algebra) <br/> --> [Linear algebra](linear%20algebra.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                          |
| --------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
|                                                     | - [Outline](outline%20of%20linear%20algebra.md) <br/> - [Glossary](glossary%20of%20linear%20algebra.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                          |
|                                  __Basic concepts__ | - [Scalar](scalar%20(mathematics).md) <br/> - [Vector](Euclidean%20vector.md) <br/> - [Vector space](vector%20space.md) <br/> - [Scalar multiplication](scalar%20multiplication.md) <br/> - [Vector projection](vector%20projection.md) <br/> - [Linear span](linear%20span.md) <br/> - [Linear map](linear%20map.md) <br/> - [Linear projection](projection%20(linear%20algebra).md) <br/> - [Linear independence](linear%20independence.md) <br/> - [Linear combination](linear%20combination.md) <br/> - [Multilinear map](multilinear%20map.md) <br/> - [Basis](basis%20(linear%20algebra).md) <br/> - [Change of basis](change%20of%20basis.md) <br/> - [Row and column vectors](row%20and%20column%20vectors.md) <br/> - [Row and column spaces](row%20and%20column%20spaces.md) <br/> - [Kernel](kernel%20(linear%20algebra).md) <br/> - [Eigenvalues and eigenvectors](eigenvalues%20and%20eigenvectors.md) <br/> - [Transpose](transpose.md) <br/> - [Linear equations](system%20of%20linear%20equations.md) | [![Three dimensional Euclidean space](../../archives/Wikimedia%20Commons/Linear%20subspaces%20with%20shading.svg)](Euclidean%20space.md) |
|           __[Matrices](matrix%20(mathematics).md)__ | - [Block](block%20matrix.md) <br/> - [Decomposition](matrix%20decomposition.md) <br/> - [Invertible](invertible%20matrix.md) <br/> - [Minor](minor%20(linear%20algebra).md) <br/> - [Multiplication](matrix%20multiplication.md) <br/> - [Rank](rank%20(linear%20algebra).md) <br/> - [Transformation](transformation%20matrix.md) <br/> - [Cramer's rule](Cramer's%20rule.md) <br/> - [Gaussian elimination](Gaussian%20elimination.md) <br/> - [Productive matrix](productive%20matrix.md) <br/> - [Gram matrix](Gram%20matrix.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                          |
|                   __[Bilinear](bilinear%20map.md)__ | - [Orthogonality](orthogonality.md) <br/> - [Dot product](dot%20product.md) <br/> - [Hadamard product](Hadamard%20product%20(matrices).md) <br/> - [Inner product space](inner%20product%20space.md) <br/> - [Outer product](outer%20product.md) <br/> - [Kronecker product](Kronecker%20product.md) <br/> - [Gram–Schmidt process](Gram–Schmidt%20process.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                          |
| __[Multilinear algebra](multilinear%20algebra.md)__ | - [Determinant](determinant.md) <br/> - [Cross product](cross%20product.md) <br/> - [Triple product](triple%20product.md) <br/> - [Seven-dimensional cross product](seven-dimensional%20cross%20product.md) <br/> - [Geometric algebra](geometric%20algebra.md) <br/> - [Exterior algebra](exterior%20algebra.md) <br/> - [Bivector](bivector.md) <br/> - [Multivector](multivector.md) <br/> - [Tensor](tensor.md) <br/> - [Outermorphism](outermorphism.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                          |
| __[Vector space](vector%20space.md) constructions__ | - [Dual](dual%20space.md) <br/> - [Direct sum](direct%20sum%20of%20modules.md#construction%20for%20two%20vector%20spaces) <br/> - [Function space](function%20space.md#in%20linear%20algebra) <br/> - [Quotient](quotient%20space%20(linear%20algebra).md) <br/> - [Subspace](linear%20subspace.md) <br/> - [Tensor product](tensor%20product.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                          |
|    __[Numerical](numerical%20linear%20algebra.md)__ | - [Floating-point](floating-point%20arithmetic.md) <br/> - [Numerical stability](numerical%20stability.md) <br/> - [Basic Linear Algebra Subprograms](Basic%20Linear%20Algebra%20Subprograms.md) <br/> - [Sparse matrix](sparse%20matrix.md) <br/> - [Comparison of linear algebra libraries](comparison%20of%20linear%20algebra%20libraries.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                          |
|                                                     | - ![category icon](../../archives/Wikimedia%20Commons/Symbol%20category%20class.svg) <br/>  [Category](https://en.wikipedia.org/wiki/Category:Linear%20algebra)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                          |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Bilinear maps](https://en.wikipedia.org/wiki/Category:Bilinear%20maps)
> - [Operations on vectors](https://en.wikipedia.org/wiki/Category:Operations%20on%20vectors)
> - [Analytic geometry](https://en.wikipedia.org/wiki/Category:Analytic%20geometry)
