---
aliases:
  - domain-straightening theorem
  - domain-straightening theorems
  - straightening out of a vector field
  - straightening theorem
  - straightening theorem for vector fields
  - straightening theorems
  - straightening theorems for vector fields
tags:
  - flashcard/active/general/eng/straightening_theorem_for_vector_fields
  - language/in/English
---

# straightening theorem for vector fields

In {@{[differential calculus](differential%20calculus.md)}@}, {@{the __domain-straightening theorem__}@} states that, given {@{a [vector field](vector%20field.md) $X$ on a [manifold](manifold.md)}@}, there {@{exist local coordinates $y_{1},\dots ,y_{n}$ such that $X=\partial /\partial y_{1}$ in a neighborhood of a point where $X$ is nonzero}@}. The theorem is also known as {@{__straightening out of a vector field__}@}. <!--SR:!2029-05-16,1093,350!2029-07-04,1132,350!2029-06-16,1114,350!2028-07-21,794,330!2029-04-10,1065,350-->

{@{The [Frobenius theorem](Frobenius%20theorem%20(differential%20topology).md) in [differential geometry](differential%20geometry.md)}@} can be {@{considered as a higher-dimensional generalization of this theorem}@}. <!--SR:!2029-07-17,1142,350!fsrs,2029-08-12T02:43:04.601Z,1153,1153.10014712,1,2,9,0,0,2026-06-16T02:43:04.601Z-->

## proof

It is clear that we only have to {@{find such coordinates at __0__ in $\mathbb {R} ^{n}$}@}. First we write {@{$X=\sum _{j}f_{j}(x){\partial  \over \partial x_{j} }$}@} where {@{$x$ is some coordinate system at $0$}@}, and {@{$f_{1},f_{2},\dots ,f_{n}$ are the component function of $X$ relative to $x$}@}. \(annotation: Consider {@{curvilinear coordinates $\mathbf r(\mathbf x)$}@}, where {@{$\mathbf x$ are the coordinate values and $\mathbf r(\mathbf x)$ is the actual vector given the coordinate values}@}. Then {@{$\partial \mathbf x / \partial x_j$}@} is {@{one of the _basis_ vectors}@}, and is {@{a vector function of the coordinate values}@}. The above notation is {@{simply expressing the vector field $X$ in terms of the basis vectors}@}.\) Let {@{$f=(f_{1},\dots ,f_{n})$}@}. By {@{linear change of coordinates \(annotation: an affine transformation that is the same everywhere\)}@}, we can {@{assume $f(\mathbf 0)=(1,0,\dots ,0)$}@}. \(annotation: This {@{makes $X(\mathbf 0) = \partial / \partial x_j$}@}, but {@{this may not hold for nearby nonzero coordinate values}@}. This is {@{what the steps below will fix}@}.\) Let $\Phi (t,p)$ be {@{the solution of the initial value problem ${\dot {x} }=f(x),x(0)=p$}@} and let {@{$$\psi (x_{1},\dots ,x_{n})=\Phi (x_{1},(0,x_{2},\dots ,x_{n})).$$}@} \(annotation: Given {@{the initial value $\mathbf x(0) = \mathbf p$}@}, the solution is {@{$\mathbf x(t)$, a function of $t$ that returns a vector satisfying $\partial_t \mathbf x = f(\mathbf x)$}@}. Also, notice by {@{parameterizing the initial value}@}, $\psi$ {@{maps $n$ numbers to $n$ numbers}@}, so {@{later we will use it as a coordinate transformation}@}, in which the input is {@{in the desired coordinates $y_i$ and the output is in the original coordinates $x_i$}@}. Intuitively, we can consider the above as {@{"collecting" the component values of _X_ across the original basis vectors into one new basis vector, obtained by changing $t$ of the IVP solution}@}.\) <!--SR:!2026-06-30,275,330!2029-07-10,1138,350!2029-05-23,1100,350!2029-07-18,1145,350!fsrs,2029-08-28T00:00:00.000Z,1165,1164.5679841,1,2,9,0,0,2026-06-20T00:00:00.000Z!2029-05-18,1095,350!2026-06-28,273,330!2026-06-28,272,330!2026-06-29,274,330!2029-05-30,1097,350!2029-07-01,1129,350!2028-05-01,772,330!2029-06-30,1128,350!2029-05-02,1085,350!fsrs,2029-09-01T00:00:00.000Z,1168,1168.38706892,1,2,9,0,0,2026-06-21T00:00:00.000Z!2029-05-22,1099,350!2029-05-17,1094,350!2027-08-30,548,310!2029-06-04,1102,350!fsrs,2029-08-07T06:06:35.477Z,1149,1149.27403969,1,2,9,0,0,2026-06-15T06:06:35.477Z!2029-06-23,1121,350!2029-04-29,1082,350!2029-07-06,1134,350!2026-06-25,271,330!2029-06-26,1124,350-->

{@{$\Phi$ \(and thus $\psi$\)}@} is {@{smooth by smooth dependence on initial conditions in [ordinary differential equations](ordinary%20differential%20equations.md)}@}. It follows that {@{$${\partial  \over \partial x_{1} }\psi (x)=f(\psi (x)) \,,$$}@} \(annotation: varying $x_1$ is {@{the same as varying $t$}@}\) and, since {@{$\psi (0,x_{2},\dots ,x_{n})=\Phi (0,(0,x_{2},\dots ,x_{n}))=(0,x_{2},\dots ,x_{n})$}@}, {@{the differential $d\psi$ is the identity at $\mathbf 0$ \(annotation: except for the first coordinate $x_1$\)}@}. Thus, {@{$y=\psi ^{-1}(x)$ is a coordinate system at $\mathbf 0$}@}. \(annotation: This is because {@{the total differential is nonzero for all coordinates}@}. For $x_i$, note that {@{$f \ne \mathbf 0$ as $X$ is nonzero in a neighborhood}@}.\) Finally, since {@{$x=\psi (y)$}@}, we have: {@{${\partial x_{j} \over \partial y_{1} }=f_{j}(\psi (y))=f_{j}(x)$}@} \(annotation: note {@{$\partial / \partial y_1 = \sum_j (\partial x_j / \partial y_1) (\partial / \partial x_j)$}@}\) and so {@{${\partial  \over \partial y_{1} }=X$ as required \(annotation: on a neighborhood around $\mathbf 0$, not just at $\mathbf 0$\)}@}. <!--SR:!2029-04-30,1083,350!2029-05-24,1101,350!fsrs,2029-08-23T00:00:00.000Z,1161,1160.74715681,1,2,9,0,0,2026-06-19T00:00:00.000Z!2029-06-09,1107,350!fsrs,2028-06-26T00:00:00.000Z,740,740.29434474,2.49272837,2,9,0,0,2026-06-17T00:00:00.000Z!2026-06-24,270,330!2027-09-29,558,310!2029-04-15,1070,350!2029-05-01,1084,350!2029-07-09,1136,350!2028-08-15,809,330!2028-08-13,834,330!fsrs,2029-09-15T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-06-23T00:00:00.000Z-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/straightening_theorem_for_vector_fields) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Theorem B.7 in Camille Laurent-Gengoux, Anne Pichereau, Pol Vanhaecke. _Poisson Structures_, Springer, 2013.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Differential calculus](https://en.wikipedia.org/wiki/Category:Differential%20calculus)
> - [Theorems in mathematical analysis](https://en.wikipedia.org/wiki/Category:Theorems%20in%20mathematical%20analysis)
