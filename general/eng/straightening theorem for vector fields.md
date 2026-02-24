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

In {@{[differential calculus](differential%20calculus.md)}@}, {@{the __domain-straightening theorem__}@} states that, given {@{a [vector field](vector%20field.md) $X$ on a [manifold](manifold.md)}@}, there {@{exist local coordinates $y_{1},\dots ,y_{n}$ such that $X=\partial /\partial y_{1}$ in a neighborhood of a point where $X$ is nonzero}@}. The theorem is also known as {@{__straightening out of a vector field__}@}. <!--SR:!2026-05-18,241,330!2026-05-28,249,330!2026-05-23,245,330!2026-05-18,241,330!2026-05-09,233,330-->

{@{The [Frobenius theorem](Frobenius%20theorem%20(differential%20topology).md) in [differential geometry](differential%20geometry.md)}@} can be {@{considered as a higher-dimensional generalization of this theorem}@}. <!--SR:!2026-05-31,251,330!2026-06-16,262,330-->

## proof

It is clear that we only have to {@{find such coordinates at __0__ in $\mathbb {R} ^{n}$}@}. First we write {@{$X=\sum _{j}f_{j}(x){\partial  \over \partial x_{j} }$}@} where {@{$x$ is some coordinate system at $0$}@}, and {@{$f_{1},f_{2},\dots ,f_{n}$ are the component function of $X$ relative to $x$}@}. \(annotation: Consider {@{curvilinear coordinates $\mathbf r(\mathbf x)$}@}, where {@{$\mathbf x$ are the coordinate values and $\mathbf r(\mathbf x)$ is the actual vector given the coordinate values}@}. Then {@{$\partial \mathbf x / \partial x_j$}@} is {@{one of the _basis_ vectors}@}, and is {@{a vector function of the coordinate values}@}. The above notation is {@{simply expressing the vector field $X$ in terms of the basis vectors}@}.\) Let {@{$f=(f_{1},\dots ,f_{n})$}@}. By {@{linear change of coordinates \(annotation: an affine transformation that is the same everywhere\)}@}, we can {@{assume $f(\mathbf 0)=(1,0,\dots ,0)$}@}. \(annotation: This {@{makes $X(\mathbf 0) = \partial / \partial x_j$}@}, but {@{this may not hold for nonzero coordinate values}@}. This is {@{what the steps below will fix}@}.\) Let $\Phi (t,p)$ be {@{the solution of the initial value problem ${\dot {x} }=f(x),x(0)=p$}@} and let {@{$$\psi (x_{1},\dots ,x_{n})=\Phi (x_{1},(0,x_{2},\dots ,x_{n})).$$}@} \(annotation: Given {@{the initial value $\mathbf x(0) = \mathbf p$}@}, the solution is {@{$\mathbf x(t)$, a function of $t$ that returns a vector satisfying $\partial_t \mathbf x = f(\mathbf x)$}@}. Also, notice by {@{parameterizing the initial value}@}, $\psi$ {@{maps $n$ numbers to $n$ numbers}@}, so {@{later we will use it as a coordinate transformation}@}, in which the input is {@{in the desired coordinates $y_i$ and the output is in the original coordinates $x_i$}@}. Intuitively, we can consider the above as {@{"collecting" the component values of _X_ across the original basis vectors into one new basis vector, obtained by changing $t$ of the IVP solution}@}.\) <!--SR:!2026-06-30,275,330!2026-05-29,250,330!2026-05-18,241,330!2026-05-30,251,330!2026-06-20,265,330!2026-05-18,241,330!2026-06-28,273,330!2026-06-28,272,330!2026-06-29,274,330!2026-05-20,242,330!2026-05-27,248,330!2026-03-21,180,310!2026-05-28,248,330!2026-05-13,237,330!2026-06-21,266,330!2026-05-19,241,330!2026-05-18,241,330!2027-08-30,548,310!2026-05-21,243,330!2026-06-15,261,330!2026-05-24,246,330!2026-05-13,237,330!2026-05-29,249,330!2026-06-25,271,330!2026-05-26,247,330-->

{@{$\Phi$ \(and thus $\psi$\)}@} is {@{smooth by smooth dependence on initial conditions in [ordinary differential equations](ordinary%20differential%20equations.md)}@}. It follows that {@{$${\partial  \over \partial x_{1} }\psi (x)=f(\psi (x)) \,,$$}@} \(annotation: Varying $x_1$ is {@{the same as varying $t$}@}.\) and, since {@{$\psi (0,x_{2},\dots ,x_{n})=\Phi (0,(0,x_{2},\dots ,x_{n}))=(0,x_{2},\dots ,x_{n})$}@}, {@{the differential $d\psi$ is the identity at $\mathbf 0$ \(annotation: except for the first coordinate $x_1$\)}@}. Thus, {@{$y=\psi ^{-1}(x)$ is a coordinate system at $\mathbf 0$}@}. \(annotation: This is because {@{the total differential is nonzero for all coordinates}@}. For $x_i$, note that {@{$f \ne \mathbf 0$ as $X$ is nonzero in a neighborhood}@}.\) Finally, since {@{$x=\psi (y)$}@}, we have: {@{${\partial x_{j} \over \partial y_{1} }=f_{j}(\psi (y))=f_{j}(x)$}@} \(annotation: note {@{$\partial / \partial y_1 = \sum_j (\partial x_j / \partial y_1) (\partial / \partial x_j)$}@}\) and so {@{${\partial  \over \partial y_{1} }=X$ as required \(annotation: on a neighborhood around $\mathbf 0$, not just at $\mathbf 0$\)}@}. <!--SR:!2026-05-13,237,330!2026-05-18,241,330!2026-06-19,264,330!2026-05-22,244,330!2026-06-17,263,330!2026-06-24,270,330!2026-03-20,180,310!2026-05-10,234,330!2026-05-13,237,330!2026-05-30,250,330!2026-05-27,247,330!2026-04-12,195,310!2026-06-23,269,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/straightening_theorem_for_vector_fields) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Theorem B.7 in Camille Laurent-Gengoux, Anne Pichereau, Pol Vanhaecke. _Poisson Structures_, Springer, 2013.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Differential calculus](https://en.wikipedia.org/wiki/Category:Differential%20calculus)
> - [Theorems in mathematical analysis](https://en.wikipedia.org/wiki/Category:Theorems%20in%20mathematical%20analysis)
