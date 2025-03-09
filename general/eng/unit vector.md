---
aliases:
  - unit vector
  - unit vectors
tags:
  - flashcard/active/general/eng/unit_vector
  - language/in/English
---

# unit vector

- Not to be confused with {@{[Vector of ones](vector%20of%20ones.md)}@}. <!--SR:!2025-05-16,72,319-->

In {@{[mathematics](mathematics.md)}@}, {@{a __unit vector__}@} in {@{a [normed vector space](normed%20vector%20space.md) is a [vector](vector%20(mathematics%20and%20physics).md) \(often a [spatial vector](vector%20(geometry).md)\) of [length](norm%20(mathematics).md) 1}@}. A unit vector is often denoted by {@{a lowercase letter with a [circumflex](circumflex.md), or "hat"}@}, as in {@{${\hat {\mathbf {v} } }$ \(pronounced "v-hat"\)}@}. {@{The term _normalized vector_}@} is sometimes {@{used as a synonym for _unit vector_}@}. <!--SR:!2025-05-16,73,319!2025-05-15,71,319!2025-05-14,70,319!2025-05-17,73,319!2025-05-17,73,319!2025-05-17,73,319!2025-05-16,72,319-->

{@{The __normalized vector û__ of a non-zero vector __u__}@} is {@{the unit vector in the direction of __u__}@}, i.e., {@{$$\mathbf {\hat {u} } ={\frac {\mathbf {u} }{\|\mathbf {u} \|} }=({\frac {u_{1} }{\|\mathbf {u} \|} },{\frac {u_{2} }{\|\mathbf {u} \|} },...,{\frac {u_{n} }{\|\mathbf {u} \|} })$$}@} where {@{‖<!-- markdown separator -->__u__<!-- markdown separator -->‖ is the [norm](norm%20(mathematics).md) \(or length\) of __u__ and $\mathbf {u} =(u_{1},u_{2},...,u_{n})$}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-05-15,71,319!2025-05-11,67,310!2025-05-16,72,319!2025-05-10,67,319-->

The proof is the following: {@{$$\|\mathbf {\hat {u} } \|={\sqrt { {\frac {u_{1} }{\sqrt {u_{1}^{2}+...+u_{n}^{2} } } }^{2}+...+{\frac {u_{n} }{\sqrt {u_{1}^{2}+...+u_{n}^{2} } } }^{2} } }={\sqrt {\frac {u_{1}^{2}+...+u_{n}^{2} }{u_{1}^{2}+...+u_{n}^{2} } } }={\sqrt {1} }=1$$}@} <!--SR:!2025-05-13,69,319-->

A unit vector is often {@{used to represent [directions](direction%20(geometry).md)}@}, such as {@{[normal directions](normal%20direction.md)}@}. Unit vectors are often {@{chosen to form the [basis](basis%20(linear%20algebra).md) of a vector space}@}, and {@{every vector in the space may be written as a [linear combination](linear%20combination.md) form of unit vectors}@}. <!--SR:!2025-05-15,71,319!2025-05-12,68,319!2025-05-15,71,319!2025-05-14,70,319-->

## orthogonal coordinates

### Cartesian coordinates

- Main article: ::@:: [Standard basis](standard%20basis.md) <!--SR:!2025-05-13,69,319!2025-05-16,72,319-->

Unit vectors may be used to {@{represent the axes of a [Cartesian coordinate system](Cartesian%20coordinate%20system.md)}@}. For instance, {@{the standard _unit vectors_}@} in {@{the direction of the _x_, _y_, and _z_ axes of a [three dimensional Cartesian coordinate system](Cartesian%20coordinate%20system.md)}@} are {@{$$\mathbf {\hat {x} } ={\begin{bmatrix}1\\0\\0\end{bmatrix} },\,\,\mathbf {\hat {y} } ={\begin{bmatrix}0\\1\\0\end{bmatrix} },\,\,\mathbf {\hat {z} } ={\begin{bmatrix}0\\0\\1\end{bmatrix} }$$}@} They form {@{a set of mutually [orthogonal](orthogonal.md) _unit vectors_}@}, typically referred to as {@{a [standard basis](standard%20basis.md) in [linear algebra](linear%20algebra.md)}@}. <!--SR:!2025-05-13,69,319!2025-05-14,70,319!2025-05-15,71,319!2025-05-12,69,319!2025-05-16,72,319!2025-05-13,69,319-->

They are often denoted {@{using common [vector notation](vector%20notation.md) \(e.g., __x__ or ${\vec {x} }$\) rather than standard unit vector notation \(e.g., __x̂__\)}@}. In most contexts it can be assumed that {@{__x__, __y__, and __z__, \(or ${\vec {x} }$, ${\vec {y} }$, and ${\vec {z} }$\) are versors of a 3-D [Cartesian coordinate system](Cartesian%20coordinate%20system.md)}@}. {@{The notations \(__î__, __ĵ__, __k̂__\), \(__x̂<sub>1</sub>__, __x̂<sub>2</sub>__, __x̂<sub>3</sub>__\), \(__ê<sub>x</sub>__, __ê<sub>y</sub>__, __ê<sub>z</sub>__\), or \(__ê<sub>1</sub>__, __ê<sub>2</sub>__, __ê<sub>3</sub>__\), with or without [hat](hat%20notation.md)}@}, are also used,<sup>[\[1\]](#^ref-1)</sup> particularly in {@{contexts where __i__, __j__, __k__ might lead to confusion with another quantity}@} \(for instance with {@{[index](indexed%20family.md) symbols such as _i_, _j_, _k_}@}, which are used to {@{identify an element of a set or array or sequence of variables}@}\). <!--SR:!2025-05-13,69,319!2025-05-12,68,319!2025-05-17,73,319!2025-05-14,70,319!2025-05-11,68,319!2025-05-14,70,319-->

When a unit vector in space is {@{expressed in [Cartesian notation](Cartesian%20coordinate%20system.md#Representing%20a%20vector%20with%20Cartesian%20notation) as a linear combination of __x__, __y__, __z__}@}, {@{its three scalar components}@} can be referred to as {@{[direction cosines](direction%20cosines.md)}@}. {@{The value of each component}@} is equal to {@{the cosine of the angle formed by the unit vector with the respective basis vector}@}. This is {@{one of the methods used to describe the [orientation](orientation%20(mathematics).md) \(angular position\)}@} of {@{a straight line, segment of straight line, oriented axis, or segment of oriented axis \([vector](vector%20(geometry).md)\)}@}. <!--SR:!2025-05-12,68,314!2025-05-12,68,314!2025-05-17,73,319!2025-05-16,72,319!2025-05-11,68,319!2025-05-15,72,319!2025-05-12,68,319-->

### cylindrical coordinates

- See also: ::@:: [Jacobian matrix](Jacobian%20matrix.md) <!--SR:!2025-05-16,72,319!2025-05-13,69,319-->

{@{The three [orthogonal](orthogonal.md) unit vectors appropriate to cylindrical symmetry}@} are: (annotation: 3 items: {@{$\boldsymbol {\hat \rho}$, $\boldsymbol {\hat \varphi}$, $\boldsymbol {\hat z}$}@}) <!--SR:!2025-05-15,71,319!2025-04-14,48,299-->

- ${\boldsymbol {\hat {\rho } } }$ \(also designated $\mathbf {\hat {e} }$ or ${\boldsymbol {\hat {s} } }$\), ::@:: representing the direction along which the distance of the point from the axis of symmetry is measured; <!--SR:!2025-05-15,72,319!2025-05-17,73,319-->
- ${\boldsymbol {\hat {\varphi } } }$, ::@:: representing the direction of the motion that would be observed if the point were rotating counterclockwise about the [symmetry axis](symmetry%20axis.md); <!--SR:!2025-05-17,73,319!2025-05-12,68,319-->
- $\mathbf {\hat {z} }$, ::@:: representing the direction of the symmetry axis; <!--SR:!2025-05-13,69,319!2025-05-16,72,319-->

They are {@{related to the Cartesian basis ${\hat {x} }$, ${\hat {y} }$, ${\hat {z} }$}@} by: <!--SR:!2025-05-14,70,319-->

- (annotation: $\boldsymbol {\hat \rho}$, Cartesian basis) ::@:: $${\boldsymbol {\hat {\rho } } }=\cos(\varphi )\mathbf {\hat {x} } +\sin(\varphi )\mathbf {\hat {y} }$$ <!--SR:!2025-05-11,68,319!2025-05-16,72,319-->
- (annotation: $\boldsymbol {\hat \varphi}$, Cartesian basis) ::@:: $${\boldsymbol {\hat {\varphi } } }=-\sin(\varphi )\mathbf {\hat {x} } +\cos(\varphi )\mathbf {\hat {y} }$$ <!--SR:!2025-05-14,70,319!2025-05-12,68,319-->
- (annotation: $\boldsymbol {\hat z}$, Cartesian basis) ::@:: $$\mathbf {\hat {z} } =\mathbf {\hat {z} } .$$ <!--SR:!2025-05-12,68,314!2025-05-17,73,319-->

{@{The vectors ${\boldsymbol {\hat {\rho } } }$ and ${\boldsymbol {\hat {\varphi } } }$}@} are {@{functions of $\varphi$, and are _not_ constant in direction}@}. When {@{differentiating or integrating in cylindrical coordinates}@}, {@{these unit vectors themselves must also be operated on}@}. {@{The derivatives with respect to $\varphi$}@} are: <!--SR:!2025-05-14,70,319!2025-05-12,68,319!2025-05-16,72,319!2025-05-13,70,319!2025-05-10,67,319-->

- (annotation: $\frac {\partial \boldsymbol {\hat \rho} } {\partial \varphi}$) ::@:: $${\frac {\partial {\boldsymbol {\hat {\rho } } } }{\partial \varphi } }=-\sin \varphi \mathbf {\hat {x} } +\cos \varphi \mathbf {\hat {y} } ={\boldsymbol {\hat {\varphi } } }$$ <!--SR:!2025-05-14,70,319!2025-04-24,51,299-->
- (annotation: $\frac {\partial \boldsymbol {\hat \varphi} } {\partial \varphi}$) ::@:: $${\frac {\partial {\boldsymbol {\hat {\varphi } } } }{\partial \varphi } }=-\cos \varphi \mathbf {\hat {x} } -\sin \varphi \mathbf {\hat {y} } =-{\boldsymbol {\hat {\rho } } }$$ <!--SR:!2025-05-14,70,319!2025-03-31,34,279-->
- (annotation: $\frac {\partial \boldsymbol {\hat z} } {\partial \varphi}$) ::@:: $${\frac {\partial \mathbf {\hat {z} } }{\partial \varphi } }=\mathbf {0} .$$ <!--SR:!2025-05-13,69,319!2025-05-14,70,319-->

### spherical coordinates

{@{The unit vectors appropriate to spherical symmetry}@} are: {@{$\mathbf {\hat {r} }$, the direction in which the radial distance from the origin increases}@}; {@{${\boldsymbol {\hat {\varphi } } }$, the direction in which the angle in the _x_-_y_ plane counterclockwise from the positive _x_-axis is increasing}@}; and {@{${\boldsymbol {\hat {\theta } } }$, the direction in which the angle from the positive _z_ axis is increasing}@}. To {@{minimize redundancy of representations}@}, {@{the polar angle $\theta$}@} is usually {@{taken to lie between zero and 180 degrees}@}. It is especially important to note {@{the context of any ordered triplet written in [spherical coordinates](spherical%20coordinates.md)}@}, as {@{the roles of ${\boldsymbol {\hat {\varphi } } }$ and ${\boldsymbol {\hat {\theta } } }$ are often reversed}@}. Here, {@{the American "physics" convention}@}<sup>[\[3\]](#^ref-3)</sup> is used. This leaves {@{the [azimuthal angle](azimuthal%20angle.md) $\varphi$ defined the same as in cylindrical coordinates}@}. {@{The [Cartesian](Cartesian%20coordinate%20system.md) relations}@} are: <!--SR:!2025-05-16,73,319!2025-05-13,69,319!2025-05-16,72,319!2025-05-13,69,319!2025-05-12,69,319!2025-05-15,71,319!2025-05-13,69,319!2025-05-16,72,319!2025-05-15,71,319!2025-05-14,70,319!2025-04-27,53,299!2025-05-17,73,319-->

- (annotation: $\mathbf {\hat r}$, Cartesian basis) ::@:: $$\mathbf {\hat {r} } =\sin \theta \cos \varphi \mathbf {\hat {x} } +\sin \theta \sin \varphi \mathbf {\hat {y} } +\cos \theta \mathbf {\hat {z} }$$ (annotation: memorize the effect of $\varphi$, and then the effect of $\theta$) <!--SR:!2025-03-10,18,259!2025-03-11,19,259-->
- (annotation: $\boldsymbol {\hat \theta}$, Cartesian basis) ::@:: $${\boldsymbol {\hat {\theta } } }=\cos \theta \cos \varphi \mathbf {\hat {x} } +\cos \theta \sin \varphi \mathbf {\hat {y} } -\sin \theta \mathbf {\hat {z} }$$ (annotation: memorize the effect of $\varphi$, and then the effect of $\theta$) <!--SR:!2025-04-22,44,259!2025-03-11,19,259-->
- (annotation: $\boldsymbol {\hat \varphi}$, Cartesian basis) ::@:: $${\boldsymbol {\hat {\varphi } } }=-\sin \varphi \mathbf {\hat {x} } +\cos \varphi \mathbf {\hat {y} }$$ (annotation: memorize the effect of $\varphi$, and then the effect of $\theta$; the latter of which is null, as in cylindrical coordinates) <!--SR:!2025-04-27,53,299!2025-05-12,68,319-->

{@{The spherical unit vectors}@} depend on {@{both $\varphi$ and $\theta$}@}, and hence there are {@{5 possible non-zero derivatives}@}. For a more complete description, see {@{[Jacobian matrix and determinant](Jacobian%20matrix%20and%20determinant.md)}@}. The non-zero derivatives are: <!--SR:!2025-05-17,73,319!2025-05-15,71,319!2025-05-16,72,319!2025-05-15,71,319-->

- (annotation: $\frac {\partial \mathbf {\hat r} } {\partial \varphi}$) ::@:: $${\frac {\partial \mathbf {\hat {r} } }{\partial \varphi } }=-\sin \theta \sin \varphi \mathbf {\hat {x} } +\sin \theta \cos \varphi \mathbf {\hat {y} } =\sin \theta {\boldsymbol {\hat {\varphi } } }$$ (annotation: $\boldsymbol {\hat \varphi}$ modulated by the polar angle $\theta$) <!--SR:!2025-03-17,25,279!2025-03-16,24,279-->
- (annotation: $\frac {\partial \mathbf {\hat r} } {\partial \theta}$) ::@:: $${\frac {\partial \mathbf {\hat {r} } }{\partial \theta } }=\cos \theta \cos \varphi \mathbf {\hat {x} } +\cos \theta \sin \varphi \mathbf {\hat {y} } -\sin \theta \mathbf {\hat {z} } ={\boldsymbol {\hat {\theta } } }$$ <!--SR:!2025-03-16,24,279!2025-05-12,68,319-->
- (annotation: $\frac {\partial \boldsymbol {\hat \theta} } {\partial \varphi}$) ::@:: $${\frac {\partial {\boldsymbol {\hat {\theta } } } }{\partial \varphi } }=-\cos \theta \sin \varphi \mathbf {\hat {x} } +\cos \theta \cos \varphi \mathbf {\hat {y} } =\cos \theta {\boldsymbol {\hat {\varphi } } }$$ (annotation: $\boldsymbol {\hat \varphi}$ modulated by the polar angle $\theta$) <!--SR:!2025-03-17,25,279!2025-03-31,34,279-->
- (annotation: $\frac {\partial \boldsymbol {\hat \theta} } {\partial \theta}$) ::@:: $${\frac {\partial {\boldsymbol {\hat {\theta } } } }{\partial \theta } }=-\sin \theta \cos \varphi \mathbf {\hat {x} } -\sin \theta \sin \varphi \mathbf {\hat {y} } -\cos \theta \mathbf {\hat {z} } =-\mathbf {\hat {r} }$$ <!--SR:!2025-03-27,30,279!2025-03-29,32,279-->
- (annotation: $\frac {\partial \boldsymbol {\hat \varphi} } {\partial \varphi}$) ::@:: $${\frac {\partial {\boldsymbol {\hat {\varphi } } } }{\partial \varphi } }=-\cos \varphi \mathbf {\hat {x} } -\sin \varphi \mathbf {\hat {y} } =-\sin \theta \mathbf {\hat {r} } -\cos \theta {\boldsymbol {\hat {\theta } } }$$ (annotation: the derivative vector is in the plane formed by $\mathbf {\hat r}$ and $\boldsymbol {\hat \theta}$) <!--SR:!2025-04-20,42,259!2025-03-16,24,279-->

### general unit vectors

- Main article: ::@:: [Orthogonal coordinates](orthogonal%20coordinates.md) <!--SR:!2025-04-14,48,299!2025-05-12,68,319-->

Common themes of unit vectors occur {@{throughout [physics](physics.md) and [geometry](geometry.md)}@}:<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-05-16,72,319-->

| Unit vector                                                                                                         | Nomenclature                                                                                                                                                                                              | Diagram                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| {@{Tangent vector to a curve/flux line}@}                                                                           | {@{$\mathbf {\hat {t} }$}@}                                                                                                                                                                               | !["200px"](../../archives/Wikimedia%20Commons/Tangent%20normal%20binormal%20unit%20vectors.svg) <p> {@{!["200px"](../../archives/Wikimedia%20Commons/Polar%20coord%20unit%20vectors%20and%20normal.svg)}@} <p> {@{A normal vector $\mathbf {\hat {n} }$ to the plane}@} containing and defined by {@{the radial position vector $r\mathbf {\hat {r} }$ and angular tangential direction of rotation $\theta {\boldsymbol {\hat {\theta } } }$}@} is {@{necessary so that the vector equations of angular motion hold}@}. |
| {@{Normal to a surface tangent plane/plane containing radial position component and angular tangential component}@} | {@{$\mathbf {\hat {n} }$}@} <p> In terms of {@{[polar coordinates](spherical%20coordinate%20system.md)}@}; <br/> {@{$\mathbf {\hat {n} } =\mathbf {\hat {r} } \times {\boldsymbol {\hat {\theta } } }$}@} |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {@{Binormal vector to tangent and normal}@}                                                                         | {@{$\mathbf {\hat {b} } =\mathbf {\hat {t} } \times \mathbf {\hat {n} }$}@}<sup>[\[5\]](#^ref-5)</sup>                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {@{Parallel to some axis/line}@}                                                                                    | {@{$\mathbf {\hat {e} } _{\parallel }$}@}                                                                                                                                                                 | {@{!["200px"](../../archives/Wikimedia%20Commons/Perpendicular%20and%20parallel%20unit%20vectors.svg)}@} <p> One unit vector $\mathbf {\hat {e} } _{\parallel }$ {@{aligned parallel to a principal direction \(red line\)}@}, and a perpendicular unit vector $\mathbf {\hat {e} } _{\bot }$ is in {@{any radial direction relative to the principal line}@}.                                                                                                                                                           |
| {@{Perpendicular to some axis/line in some radial direction}@}                                                      | {@{$\mathbf {\hat {e} } _{\bot }$}@}                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {@{Possible angular deviation relative to some axis/line}@}                                                         | {@{$\mathbf {\hat {e} } _{\angle }$}@}                                                                                                                                                                    | {@{!["200px"](../../archives/Wikimedia%20Commons/Angular%20unit%20vector.svg)}@} <p> Unit vector at {@{acute deviation angle _φ_ \(including 0 or _π_/2 rad\) relative to a principal direction}@}.                                                                                                                                                                                                                                                                                                                      | <!--SR:!2025-05-17,73,319!2025-05-15,71,319!2025-05-10,66,310!2025-05-13,69,319!2025-03-30,33,279!2025-05-13,69,319!2025-05-17,73,319!2025-05-14,70,319!2025-05-12,68,319!2025-03-29,32,279!2025-05-15,71,319!2025-03-10,18,259!2025-05-13,69,319!2025-05-16,72,319!2025-03-28,31,279!2025-05-14,71,319!2025-05-12,68,319!2025-05-17,73,319!2025-05-15,71,319!2025-05-14,71,319!2025-05-12,69,319!2025-05-15,71,319!2025-05-16,73,319-->

## curvilinear coordinates

In general, a coordinate system may be {@{uniquely specified using a number of [linearly independent](linear%20independence.md) unit vectors $\mathbf {\hat {e} } _{n}$}@}<sup>[\[1\]](#^ref-1)</sup> \(the actual number being {@{equal to the degrees of freedom of the space}@}\). For {@{ordinary 3-space}@}, these vectors may be denoted {@{$\mathbf {\hat {e} } _{1},\mathbf {\hat {e} } _{2},\mathbf {\hat {e} } _{3}$}@}. It is nearly always {@{convenient to define the system to be orthonormal and [right-handed](right-hand%20rule.md)}@}: {@{$$\mathbf {\hat {e} } _{i}\cdot \mathbf {\hat {e} } _{j}=\delta _{ij}$$ <br/> $$\mathbf {\hat {e} } _{i}\cdot (\mathbf {\hat {e} } _{j}\times \mathbf {\hat {e} } _{k})=\varepsilon _{ijk}$$}@} where {@{$\delta _{ij}$ is the [Kronecker delta](Kronecker%20delta.md) \(which is 1 for _i_ = _j_, and 0 otherwise\)}@} and {@{$\varepsilon _{ijk}$ is the [Levi-Civita symbol](Levi-Civita%20symbol.md) \(which is 1 for permutations ordered as _ijk_, and −1 for permutations ordered as _kji_\)}@}. <!--SR:!2025-05-17,73,319!2025-05-12,68,319!2025-05-15,71,319!2025-05-14,70,319!2025-05-13,69,319!2025-05-15,71,319!2025-05-17,73,319!2025-05-14,70,319-->

## right versor

{@{A unit vector in $\mathbb {R} ^{3}$}@} was called {@{a __right versor__ by [W. R. Hamilton](W.%20R.%20Hamilton.md)}@}, as he {@{developed his [quaternions](quaternion.md) $\mathbb {H} \subset \mathbb {R} ^{4}$}@}. In fact, he was {@{the originator of the term _vector_}@}, as {@{every quaternion $q=s+v$ has a scalar part _s_ and a vector part _v_}@}. If {@{_v_ is a unit vector in $\mathbb {R} ^{3}$}@}, then {@{the square of _v_ in quaternions is –1}@}. Thus by {@{[Euler's formula](Euler's%20formula.md)}@}, {@{$\exp(\theta v)=\cos \theta +v\sin \theta$}@} is {@{a [versor](versor.md) in the [3-sphere](3-sphere.md)}@}. When {@{_θ_ is a [right angle](right%20angle.md)}@}, the versor is {@{a right versor: its scalar part is zero and its vector part _v_ is a unit vector in $\mathbb {R} ^{3}$}@}. <!--SR:!2025-05-14,70,319!2025-05-17,73,319!2025-05-16,72,319!2025-05-15,71,319!2025-05-17,73,319!2025-05-10,67,319!2025-05-17,73,319!2025-05-14,70,319!2025-04-27,53,299!2025-05-17,73,319!2025-05-13,70,319!2025-03-30,33,279-->

Thus the right versors {@{extend the notion of [imaginary units](imaginary%20unit.md) found in the [complex plane](complex%20plane.md)}@}, where the right versors now {@{range over the [2-sphere](2-sphere.md#dimensionality) $\mathbb {S} ^{2}\subset \mathbb {R} ^{3}\subset \mathbb {H}$}@} rather than {@{the pair {i, –i} in the complex plane}@}. <!--SR:!2025-04-26,53,299!2025-05-13,69,319!2025-04-27,53,299-->

By extension, {@{a __right quaternion__}@} is {@{a real multiple of a right versor}@}. <!--SR:!2025-04-27,53,299!2025-05-15,72,319-->

## see also

> ![Wiktionary logo](../../archives/Wikimedia%20Commons/Wiktionary-logo-en-v2.svg) Look up ___[unit vector](https://en.wiktionary.org/wiki/unit%20vector)___ in Wiktionary, the free dictionary.

- [Cartesian coordinate system](Cartesian%20coordinate%20system.md)
- [Coordinate system](coordinate%20system.md)
- [Curvilinear coordinates](curvilinear%20coordinates.md)
- [Four-velocity](four-velocity.md)
- [Jacobian matrix and determinant](Jacobian%20matrix%20and%20determinant.md)
- [Normal vector](normal%20vector.md)
- [Polar coordinate system](polar%20coordinate%20system.md)
- [Standard basis](standard%20basis.md)
- [Unit interval](unit%20interval.md)
- Unit [square](unit%20square.md), [cube](unit%20cube.md), [circle](unit%20circle.md), [sphere](unit%20sphere.md), and [hyperbola](unit%20hyperbola.md)
- [Vector notation](vector%20notation.md)
- [Vector of ones](vector%20of%20ones.md)
- [Unit matrix](unit%20matrix.md)

## notes

1. <a id="CITEREFWeisstein"></a> Weisstein, Eric W. ["Unit Vector"](https://mathworld.wolfram.com/UnitVector.html#:~:text=A%20unit%20vector%20is%20a,as%20the%20(finite)%20vector%20.). _Wolfram MathWorld_. Retrieved 2020-08-19. <a id="^ref-1"></a>^ref-1
2. ["Unit Vectors"](https://brilliant.org/wiki/unit-vectors/). _Brilliant Math & Science Wiki_. Retrieved 2020-08-19. <a id="^ref-2"></a>^ref-2
3. Tevian Dray and Corinne A. Manogue, Spherical Coordinates, College Math Journal 34, 168-169 \(2003\). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFF. AyresE. Mendelson2009"></a> F. Ayres; E. Mendelson \(2009\). _Calculus \(Schaum's Outlines Series\)_ \(5th ed.\). Mc Graw Hill. [ISBN](ISBN%20(identifier).md) [978-0-07-150861-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-07-150861-2). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFM. R. SpiegelS. LipschutzD. Spellman2009"></a> M. R. Spiegel; S. Lipschutz; D. Spellman \(2009\). _Vector Analysis \(Schaum's Outlines Series\)_ \(2nd ed.\). Mc Graw Hill. [ISBN](ISBN%20(identifier).md) [978-0-07-161545-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-07-161545-7). <a id="^ref-5"></a>^ref-5

## references

This text incorporates [content](https://en.wikipedia.org/wiki/unit_vector) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFG. B. ArfkenH. J. Weber2000"></a> G. B. Arfken & H. J. Weber \(2000\). _Mathematical Methods for Physicists_ \(5th ed.\). Academic Press. [ISBN](ISBN%20(identifier).md) [0-12-059825-6](https://en.wikipedia.org/wiki/Special:BookSources/0-12-059825-6).
- <a id="CITEREFSpiegel1998"></a> Spiegel, Murray R. \(1998\). _Schaum's Outlines: Mathematical Handbook of Formulas and Tables_ \(2nd ed.\). McGraw-Hill. [ISBN](ISBN%20(identifier).md) [0-07-038203-4](https://en.wikipedia.org/wiki/Special:BookSources/0-07-038203-4).
- <a id="CITEREFGriffiths1998"></a> Griffiths, David J. \(1998\). [_Introduction to Electrodynamics_](https://archive.org/details/introductiontoel00grif_0) \(3rd ed.\). Prentice Hall. [ISBN](ISBN%20(identifier).md) [0-13-805326-X](https://en.wikipedia.org/wiki/Special:BookSources/0-13-805326-X).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Linear algebra](https://en.wikipedia.org/wiki/Category:Linear%20algebra)
> - [Elementary mathematics](https://en.wikipedia.org/wiki/Category:Elementary%20mathematics)
> - [1 \(number\)](https://en.wikipedia.org/wiki/Category:1%20%28number%29)
> - [Vectors \(mathematics and physics\)](https://en.wikipedia.org/wiki/Category:Vectors%20%28mathematics%20and%20physics%29)
