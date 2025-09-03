---
aliases:
  - conservative vector field
  - conservative vector fields
  - irrotational vector field
  - irrotational vector fields
tags:
  - flashcard/active/general/eng/conservative_vector_field
  - language/in/English
---

# conservative vector field

<!--| ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General_references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline_citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(May 2009\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[vector calculus](vector%20calculus.md)}@}, {@{a __conservative vector field__}@} is {@{a [vector field](vector%20field.md) that is the [gradient](gradient.md) of some [function](function%20(mathematics).md)}@}.<sup>[\[1\]](#^ref-1)</sup> A conservative vector field has the property that {@{its [line integral](line%20integral.md) is path independent}@}; the choice of {@{path between two points does not change the value of the line integral}@}. {@{Path independence of the line integral}@} is equivalent to {@{the vector field under the line integral being conservative}@}. A conservative vector field is also {@{__irrotational__}@}; in {@{three dimensions}@}, this means that it {@{has vanishing [curl](curl%20(mathematics).md)}@}. {@{An irrotational vector field}@} is {@{necessarily conservative provided that the domain is [simply connected](simply%20connected.md)}@}. <!--SR:!2025-10-03,73,330!2025-09-23,64,310!2025-09-26,67,310!2025-09-25,66,310!2025-09-23,64,310!2025-10-06,76,330!2025-10-04,74,330!2025-09-26,67,310!2025-09-26,67,310!2025-10-04,74,330!2025-09-18,60,310!2025-09-25,66,310-->

Conservative vector fields appear {@{naturally in [mechanics](mechanics.md)}@}: They are {@{vector fields representing [forces](force.md) of [physical systems](physical%20system.md)}@} in which {@{[energy](energy.md) is [conserved](conservation%20of%20energy.md)}@}.<sup>[\[2\]](#^ref-2)</sup> For {@{a conservative system}@}, {@{the [work](work%20(physics).md) done in moving along a path in a configuration space}@} depends {@{on only the endpoints of the path}@}, so it is possible to {@{define [potential energy](potential%20energy.md) that is independent of the actual path taken}@}. <!--SR:!2025-09-25,66,310!2025-10-03,73,330!2025-10-04,74,330!2025-09-26,67,310!2025-09-23,64,310!2025-10-06,76,330!2025-10-06,76,330-->

## informal treatment

In {@{a two- and three-dimensional space}@}, there is {@{an ambiguity in taking an integral between two points}@} as there are {@{infinitely many paths between the two points}@}—apart from {@{the straight line formed between the two points}@}, one could choose {@{a curved path of greater length as shown in the figure}@}. Therefore, in general, {@{the value of the integral depends on the path taken}@}. However, in {@{the special case of a conservative vector field}@}, {@{the value of the integral is independent of the path taken}@}, which can be thought of as {@{a large-scale cancellation of all elements $d{R}$}@} that {@{do not have a component along the straight line between the two points}@}. To {@{visualize this}@}, imagine {@{two people climbing a cliff}@}; one decides to {@{scale the cliff by going vertically up it}@}, and the second decides to {@{walk along a winding path that is longer in length than the height of the cliff}@}, but at {@{only a small angle to the horizontal}@}. Although {@{the two hikers have taken different routes to get up to the top of the cliff}@}, at {@{the top}@}, they will have {@{both gained the same amount of gravitational potential energy}@}. This is because {@{a gravitational field is conservative}@}. <!--SR:!2025-09-26,67,310!2025-10-06,76,330!2025-09-25,66,310!2025-09-13,55,310!2025-10-06,76,330!2025-10-05,75,330!2025-10-03,73,330!2025-10-06,76,330!2025-09-23,64,310!2025-09-20,62,310!2025-10-06,76,330!2025-10-04,74,330!2025-10-06,76,330!2025-10-06,76,330!2025-09-24,65,310!2025-09-26,67,310!2025-10-06,76,330!2025-10-04,74,330!2025-10-04,74,330-->

> {@{![Depiction of two possible paths to integrate.](../../archives/Wikimedia%20Commons/Pathdependence.png)}@}
>
> Depiction of {@{two possible paths to integrate}@}. In green is {@{the simplest possible path; blue shows a more convoluted curve}@} <!--SR:!2025-09-25,66,310!2025-10-04,74,330!2025-09-25,66,310-->

## intuitive explanation

{@{[M. C. Escher's](M.%20C.%20Escher.md) lithograph print _[Ascending and Descending](Ascending%20and%20Descending.md)_ \(annotation: infinite circular staircase\)}@} illustrates {@{a non-conservative vector field}@}, impossibly made to {@{appear to be the gradient of the varying height above ground \(gravitational potential\) as one moves along the staircase}@}. {@{The force field experienced by the one moving on the staircase}@} is {@{non-conservative}@} in that one can {@{return to the starting point while ascending more than one descends or vice versa}@}, resulting in {@{nonzero work done by gravity}@}. On {@{a real staircase}@}, {@{the height above the ground is a scalar potential field}@}: one has to {@{go upward exactly as much as one goes downward in order to return to the same place}@}, in which case {@{the work by gravity totals to zero}@}. This suggests {@{path-independence of work done on the staircase}@}; equivalently, {@{the force field experienced is conservative}@} \(see the later section: [Path independence and conservative vector field](#path%20independence%20and%20conservative%20vector%20field)\). {@{The situation depicted in the print}@} is {@{impossible}@}. <!--SR:!2025-10-06,76,330!2025-09-26,67,310!2025-09-24,65,310!2025-10-05,75,330!2025-10-04,74,330!2025-10-06,76,330!2025-10-05,75,330!2025-09-25,66,310!2025-10-05,75,330!2025-10-03,73,330!2025-09-23,64,310!2025-09-25,66,310!2025-09-26,67,310!2025-10-04,74,330!2025-09-23,64,310-->

## definition

{@{A [vector field](vector%20field.md) $\mathbf {v} :U\to \mathbb {R} ^{n}$}@}, where {@{$U$ is an open subset of $\mathbb {R} ^{n}$}@}, is {@{said to be conservative}@} if {@{there exists a $C^{1}$ \([continuously differentiable](smoothness.md#multivariate%20differentiability%20classes)\) [scalar field](scalar%20field.md) $\varphi$<sup>[\[3\]](#^ref-3)</sup> on $U$}@} such that {@{$$\mathbf {v} =\nabla \varphi .$$}@} Here, $\nabla \varphi$ denotes {@{the [gradient](gradient.md) of $\varphi$}@}. Since {@{$\varphi$ is continuously differentiable}@}, {@{$\mathbf {v}$ is continuous}@}. When {@{the equation above holds}@}, $\varphi$ is called {@{a [scalar potential](scalar%20potential.md) for $\mathbf {v}$}@}. <!--SR:!2025-10-06,76,330!2025-10-06,76,330!2025-09-24,65,310!2025-10-03,73,330!2025-10-06,76,330!2025-09-23,64,310!2025-10-04,74,330!2025-09-24,65,310!2025-10-04,74,330!2025-10-03,73,330-->

{@{The [fundamental theorem of vector calculus](Helmholtz%20decomposition.md)}@} states that, under {@{some regularity conditions}@}, any vector field can be {@{expressed as the sum of a conservative vector field and a [solenoidal field](solenoidal%20field.md)}@}. <!--SR:!2025-09-24,65,310!2025-10-05,75,330!2025-09-25,66,310-->

## path independence and conservative vector field

- Main article: ::@:: [Gradient theorem](gradient%20theorem.md) <!--SR:!2025-09-14,56,310!2025-09-14,56,310-->

### path independence

{@{A line integral of a vector field $\mathbf {v}$}@} is {@{said to be path-independent}@} if {@{it depends on only two integral path endpoints regardless of which path between them is chosen}@}:<sup>[\[4\]](#^ref-4)</sup> {@{$$\int _{P_{1} }\mathbf {v} \cdot d\mathbf {r} =\int _{P_{2} }\mathbf {v} \cdot d\mathbf {r}$$}@} for {@{any pair of integral paths $P_{1}$ and $P_{2}$ between a given pair of path endpoints in $U$}@}. <!--SR:!2025-09-25,66,310!2025-10-06,76,330!2025-10-06,76,330!2025-09-24,65,310!2025-10-03,73,330-->

{@{The path independence}@} is also {@{equivalently expressed}@} as {@{$$\int _{P_{c} }\mathbf {v} \cdot d\mathbf {r} =0$$}@} for {@{any [piecewise](piecewise.md) smooth closed path $P_{c}$ in $U$}@} where {@{the two endpoints are coincident}@}. {@{Two expressions are equivalent}@} since {@{any closed path $P_{c}$ can be made by two path}@}; $P_{1}$ from {@{an endpoint $A$ to another endpoint $B$}@}, and {@{$P_{2}$ from $B$ to $A$}@}, so {@{$$\int _{P_{c} }\mathbf {v} \cdot d\mathbf {r} =\int _{P_{1} }\mathbf {v} \cdot d\mathbf {r} +\int _{P_{2} }\mathbf {v} \cdot d\mathbf {r} =\int _{P_{1} }\mathbf {v} \cdot d\mathbf {r} -\int _{-P_{2} }\mathbf {v} \cdot d\mathbf {r} =0$$}@} where {@{$-P_{2}$ is the reverse of $P_{2}$}@} and the last equality holds due to {@{the path independence $\displaystyle \int _{P_{1} }\mathbf {v} \cdot d\mathbf {r} =\int _{-P_{2} }\mathbf {v} \cdot d\mathbf {r}$}@}. <!--SR:!2025-10-04,74,330!2025-09-26,67,310!2025-09-26,67,310!2025-10-05,75,330!2025-10-06,76,330!2025-10-05,75,330!2025-09-24,65,310!2025-09-26,67,310!2025-10-04,74,330!2025-09-26,67,310!2025-09-23,64,310!2025-10-03,73,330-->

<!-- markdownlint-disable-next-line MD024 -->
### conservative vector field

{@{A key property of a conservative vector field $\mathbf {v}$}@} is that {@{its integral along a path depends on only the endpoints of that path, not the particular route taken}@}. In other words, _if {@{it is a conservative vector field}@}, then {@{its line integral is path-independent}@}._ Suppose that {@{$\mathbf {v} =\nabla \varphi$}@} for {@{some $C^{1}$ \([continuously differentiable](smoothness.md#multivariate%20differentiability%20classes)\) scalar field $\varphi$<sup>[\[3\]](#^ref-3)</sup> over $U$ as an open subset of $\mathbb {R} ^{n}$}@} \(so {@{$\mathbf {v}$ is a conservative vector field that is continuous}@}\) and $P$ is {@{a differentiable path \(i.e., it can be parameterized by a [differentiable function](differentiable%20function.md)\) in $U$}@} with {@{an initial point $A$ and a terminal point $B$}@}. Then {@{the [gradient theorem](gradient%20theorem.md) \(also called _fundamental theorem of calculus for line integrals_\)}@} states that {@{$$\int _{P}\mathbf {v} \cdot d{\mathbf {r} }=\varphi (B)-\varphi (A).$$}@} <!--SR:!2025-10-05,75,330!2025-09-18,60,310!2025-10-06,76,330!2025-09-24,65,310!2025-09-26,67,310!2025-10-06,76,330!2025-10-04,74,330!2025-10-04,74,330!2025-10-05,75,330!2025-09-23,64,310!2025-09-21,63,310-->

This holds as a consequence of {@{the [definition of a line integral](line%20integral.md#line%20integral%20of%20a%20vector%20field), the [chain rule](chain%20rule.md), and the [second fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}@}. {@{$\mathbf {v} \cdot d\mathbf {r} =\nabla {\varphi }\cdot d\mathbf {r}$ in the line integral}@} is {@{an [exact differential](exact%20differential.md) for an orthogonal coordinate system}@} \(e.g., {@{[Cartesian](Cartesian%20coordinate%20system.md), [cylindrical](cylindrical.md), or [spherical coordinates](spherical%20coordinate%20system.md)}@}\). Since {@{the gradient theorem is applicable for a differentiable path}@}, {@{the path independence of a conservative vector field over piecewise-differential curves}@} is also proved by {@{the proof per differentiable curve component}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-10-05,75,330!2025-09-26,67,310!2025-10-05,75,330!2025-10-05,75,330!2025-10-06,76,330!2025-10-03,73,330!2025-09-13,55,310-->

So far it has been proven that {@{a conservative vector field $\mathbf {v}$ is line integral path-independent}@}. Conversely, _if {@{a continuous vector field $\mathbf {v}$ is \(line integral\) path-independent}@}, then {@{it is a conservative vector field}@}_, so {@{the following [biconditional](logical%20biconditional.md) statement}@} holds:<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-10-03,73,330!2025-09-23,64,310!2025-10-06,76,330!2025-09-23,64,310-->

> For {@{a continuous [vector field](vector%20field.md) $\mathbf {v} :U\to \mathbb {R} ^{n}$}@}, where {@{$U$ is an open subset of $\mathbb {R} ^{n}$}@}, it is {@{conservative if and only if its line integral along a path in $U$ is path-independent}@}, meaning that {@{the line integral depends on only both path endpoints regardless of which path between them is chosen}@}. <!--SR:!2025-09-24,65,310!2025-10-06,76,330!2025-10-06,76,330!2025-09-25,66,310-->

The proof of this converse statement is the following.

> {@{![Line integral paths used to prove the following statement: if the line integral of a vector field is path-independent, then the vector field is a conservative vector field.](../../archives/Wikimedia%20Commons/Line%20Integral%20paths%20to%20prove%20the%20Relation%20between%20Path%20Independence%20and%20Conservative%20Vector%20Field,%202022-03-13.png)}@}
>
> {@{Line integral paths}@} used to prove the following statement: if {@{the line integral of a vector field is path-independent}@}, then {@{the vector field is a conservative vector field}@}. <!--SR:!2025-10-04,74,330!2025-09-25,66,310!2025-09-24,65,310!2025-10-03,73,330-->

$\mathbf {v}$ is {@{a continuous vector field which line integral is path-independent}@}. Then, let's make {@{a function $\varphi$}@} defined as {@{$$\varphi (x,y)=\int _{a,b}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }$$}@} over {@{an arbitrary path between a chosen starting point $(a,b)$ and an arbitrary point $(x,y)$}@}. Since {@{it is path-independent}@}, it depends on {@{only $(a,b)$ and $(x,y)$ regardless of which path between these points is chosen}@}. <!--SR:!2025-09-24,65,310!2025-09-26,67,310!2025-09-24,65,310!2025-10-04,74,330!2025-10-03,73,330!2025-09-24,65,310-->

Let's choose {@{the path shown in the left of the right figure}@} where {@{a 2-dimensional [Cartesian coordinate system](Cartesian%20coordinate%20system.md) is used}@}. {@{The second segment of this path}@} is {@{parallel to the $x$ axis so there is no change along the $y$ axis}@}. {@{The line integral along this path}@} is {@{$$\int _{a,b}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }=\int _{a,b}^{x_{1},y}\mathbf {v} \cdot d{\mathbf {r} }+\int _{x_{1},y}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }.$$}@} By {@{the path independence}@}, {@{its [partial derivative](partial%20derivative.md) with respect to $x$}@} \(for {@{$\varphi$ to have partial derivatives \(annotation: also ensures $\mathbf v$ is integrable\)}@}, {@{$\mathbf {v}$ needs to be continuous}@}.\) is {@{$${\frac {\partial \varphi }{\partial x} }={\frac {\partial }{\partial x} }\int _{a,b}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }={\frac {\partial }{\partial x} }\int _{a,b}^{x_{1},y}\mathbf {v} \cdot d{\mathbf {r} }+{\frac {\partial }{\partial x} }\int _{x_{1},y}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }=0+{\frac {\partial }{\partial x} }\int _{x_{1},y}^{x,y}\mathbf {v} \cdot d{\mathbf {r} }$$}@} since {@{$x_{1}$ and $x$ are independent to each other}@}. Let's express {@{$\mathbf {v}$ as ${\displaystyle \mathbf {v} }=P(x,y)\mathbf {i} +Q(x,y)\mathbf {j}$}@} where {@{$\mathbf {i}$ and $\mathbf {j}$ are unit vectors along the $x$ and $y$ axes respectively}@}, then, since {@{$d\mathbf {r} =dx\mathbf {i} +dy\mathbf {j}$}@}, {@{$${\frac {\partial }{\partial x} }\varphi (x,y)={\frac {\partial }{\partial x} }\int _{x_{1},y}^{x,y}\mathbf {v} \cdot d\mathbf {r} ={\frac {\partial }{\partial x} }\int _{x_{1},y}^{x,y}P(t,y)dt=P(x,y)$$}@} where the last equality is from {@{the [second fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}@}. <!--SR:!2025-09-23,64,310!2025-09-25,66,310!2025-09-24,65,310!2025-09-23,64,310!2025-09-24,65,310!2025-10-05,75,330!2025-09-23,64,310!2025-10-06,76,330!2025-09-26,67,310!2025-09-25,66,310!2025-10-04,74,330!2025-10-06,76,330!2025-09-23,64,310!2025-10-04,74,330!2025-09-15,57,310!2025-09-26,67,310!2025-10-03,73,330-->

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD059 -->

{@{A similar approach for the line integral path shown in the right of the right figure}@} results in {@{${\frac {\partial }{\partial y} }\varphi (x,y)=Q(x,y)$}@} so {@{$$\mathbf {v} =P(x,y)\mathbf {i} +Q(x,y)\mathbf {j} ={\frac {\partial \varphi }{\partial x} }\mathbf {i} +{\frac {\partial \varphi }{\partial y} }\mathbf {j} =\nabla \varphi$$}@} is proved for {@{the 2-dimensional [Cartesian coordinate system](Cartesian%20coordinate%20system.md)}@}. This proof method can be {@{straightforwardly expanded to a higher dimensional orthogonal coordinate system}@} \(e.g., {@{a 3-dimensional [spherical coordinate system](spherical%20coordinate%20system.md)}@}\) so {@{the converse statement is proved}@}. Another proof is {@{found [here](gradient%20theorem.md) \(annotation: [gradient theorem](gradient%20theorem.md)\) as the converse of the gradient theorem}@}. <!--SR:!2025-10-31,92,361!2025-10-28,89,361!2025-10-31,92,361!2025-10-31,92,361!2025-10-31,92,361!2025-10-30,91,361!2025-10-29,90,361!2025-10-30,91,361-->

<!-- markdownlint-restore -->

## irrotational vector fields

> {@{![Example of an irrotational vector field which is not conservative.](../../archives/Wikimedia%20Commons/Irrotational%20vector%20field.svg)}@}
>
> {@{The above vector field $\mathbf {v} =\left(-{\frac {y}{x^{2}+y^{2} } },{\frac {x}{x^{2}+y^{2} } },0\right)$}@} defined on {@{$U=\mathbb {R} ^{3}\setminus \{(0,0,z)\mid z\in \mathbb {R} \}$, i.e., $\mathbb {R} ^{3}$ with removing all coordinates on the $z$-axis}@} \(so {@{not a simply connected space}@}\), has {@{zero curl in $U$ and is thus irrotational}@}. However, it is {@{not conservative and does not have path independence}@}. <!--SR:!2025-10-06,76,330!2025-09-26,67,310!2025-09-26,67,310!2025-10-04,74,330!2025-09-24,65,310!2025-10-06,76,330-->

Let {@{$n=3$ \(3-dimensional space\)}@}, and let {@{$\mathbf {v} :U\to \mathbb {R} ^{3}$ be a $C^{1}$ \([continuously differentiable](smoothness.md#multivariate%20differentiability%20classes)\) vector field}@}, with {@{an open subset $U$ of $\mathbb {R} ^{n}$}@}. Then {@{$\mathbf {v}$ is called irrotational}@} if {@{its [curl](curl%20(mathematics).md) is $\mathbf {0}$ everywhere in $U$, i.e., if $$\nabla \times \mathbf {v} \equiv \mathbf {0} .$$}@} <!--SR:!2025-10-03,73,330!2025-09-25,66,310!2026-04-29,229,330!2025-09-24,65,310!2025-10-05,75,330-->

For {@{this reason}@}, such vector fields are sometimes referred to as {@{curl-free vector fields or curl-less vector fields}@}. They are also referred to as {@{[longitudinal vector fields](Helmholtz%20decomposition.md#longitudinal%20and%20transverse%20fields)}@}. <!--SR:!2025-10-03,73,330!2025-10-06,76,330!2025-10-05,75,330-->

It is {@{an [identity of vector calculus](vector%20calculus%20identities.md#curl%20of%20gradient%20is%20zero) that for any $C^{2}$ \([continuously differentiable up to the 2nd derivative](smoothness.md#multivariate%20differentiability%20classes)\) scalar field $\varphi$ on $U$}@}, we have {@{$$\nabla \times (\nabla \varphi )\equiv \mathbf {0} .$$}@} <!--SR:!2025-10-04,74,330!2025-10-06,76,330-->

Therefore, _{@{every $C^{1}$ conservative vector field in $U$}@} is also {@{an irrotational vector field in $U$}@}_. This result can be easily proved by {@{expressing $\nabla \times (\nabla \varphi )$ in a [Cartesian coordinate system](Cartesian%20coordinate%20system.md)}@} with {@{[Schwarz's theorem](symmetry%20of%20second%20derivatives.md#Schwarz's%20theorem) \(also called Clairaut's theorem on equality of mixed partials\)}@}. <!--SR:!2025-10-06,76,330!2025-10-03,73,330!2025-10-05,75,330!2025-09-17,59,310-->

Provided that {@{$U$ is a [simply connected open space](simply%20connected%20space.md)}@} \(roughly speaking, {@{a single piece open space without a hole within it}@}\), {@{the converse of this is also true}@}: _{@{Every irrotational vector field in a simply connected open space $U$}@} is {@{a $C^{1}$ conservative vector field in $U$}@}_. <!--SR:!2025-09-19,61,310!2025-09-25,66,310!2025-10-03,73,330!2025-10-04,74,330!2025-10-05,75,330-->

{@{The above statement is _not_ true in general}@} if {@{$U$ is not simply connected}@}. Let $U$ be {@{$\mathbb {R} ^{3}$ with removing all coordinates on the $z$-axis}@} \(so {@{not a simply connected space}@}\), i.e., {@{$U=\mathbb {R} ^{3}\setminus \{(0,0,z)\mid z\in \mathbb {R} \}$}@}. Now, define {@{a vector field $\mathbf {v}$ on $U$}@} by {@{$$\mathbf {v} (x,y,z)~{\stackrel {\text{def} }{=} }~\left(-{\frac {y}{x^{2}+y^{2} } },{\frac {x}{x^{2}+y^{2} } },0\right).$$}@} <!--SR:!2025-09-23,64,310!2025-10-06,76,330!2025-09-23,64,310!2025-09-14,56,310!2025-09-24,65,310!2025-09-25,66,310!2025-09-25,66,310-->

Then $\mathbf {v}$ has {@{zero curl everywhere in $U$}@} \({@{$\nabla \times \mathbf {v} \equiv \mathbf {0}$ at everywhere in $U$}@}\), i.e., {@{$\mathbf {v}$ is irrotational}@}. However, {@{the [circulation](circulation%20(physics).md) of $\mathbf {v}$}@} {@{around the [unit circle](unit%20circle.md) in the $xy$-plane is $2\pi$}@}; in {@{[polar coordinates](polar%20coordinates.md)}@}, {@{$\mathbf {v} =\mathbf {e} _{\phi }/r$}@}, so {@{the integral over the unit circle}@} is {@{$$\oint _{C}\mathbf {v} \cdot \mathbf {e} _{\phi }~d{\phi }=2\pi .$$}@} <!--SR:!2025-09-26,67,310!2025-09-24,65,310!2026-04-30,230,330!2025-10-06,76,330!2025-09-16,58,310!2025-10-03,73,330!2025-09-26,67,310!2025-09-26,67,310!2025-10-05,75,330-->

Therefore, $\mathbf {v}$ {@{does not have the path-independence property discussed above}@} so is {@{not conservative even if $\nabla \times \mathbf {v} \equiv \mathbf {0}$}@} since {@{$U$ where $\mathbf {v}$ is defined is not a simply connected open space}@}. <!--SR:!2025-09-23,64,310!2025-09-25,66,310!2025-10-05,75,330-->

Say again, in {@{a simply connected open region}@}, {@{an irrotational vector field $\mathbf {v}$}@} has {@{the path-independence property \(so $\mathbf {v}$ as conservative\)}@}. This can be {@{proved directly by using [Stokes' theorem](Stokes'%20theorem.md)}@}, {@{$$\oint _{P_{c} }\mathbf {v} \cdot d\mathbf {r} =\iint _{A}(\nabla \times \mathbf {v} )\cdot d\mathbf {a} =0$$}@} for {@{any smooth oriented surface $A$ which boundary is a simple closed path $P_{c}$}@}. So, it is concluded that _In {@{a simply connected open region}@}, {@{any $C^{1}$ vector field that has the path-independence property \(so it is a conservative vector field.\)}@} must {@{also be irrotational and vice versa}@}._ <!--SR:!2025-10-05,75,330!2025-10-06,76,330!2025-10-05,75,330!2025-10-03,73,330!2025-09-26,67,310!2025-09-23,64,310!2025-09-26,67,310!2025-10-04,74,330!2025-10-05,75,330-->

### abstraction

More abstractly, in {@{the presence of a [Riemannian metric](Riemannian%20metric.md#Riemannian%20metrics%20and%20Riemannian%20manifolds)}@}, vector fields {@{correspond to [differential $1$-forms](differential%20form.md)}@}. {@{The conservative vector fields}@} correspond to {@{the [exact](closed%20and%20exact%20differential%20forms.md) $1$-forms}@}, that is, to {@{the forms which are the [exterior derivative](exterior%20derivative.md) $d\phi$ of a function \(scalar field\) $\phi$ on $U$}@}. {@{The irrotational vector fields}@} correspond to {@{the [closed](closed%20and%20exact%20differential%20forms.md) $1$-forms}@}, that is, to {@{the $1$-forms $\omega$ such that $d\omega =0$}@}. As {@{$d^{2}=0$}@}, {@{any exact form is closed}@}, so {@{any conservative vector field is irrotational}@}. Conversely, {@{all closed $1$-forms are exact if $U$ is [simply connected](simply%20connected.md)}@}. <!--SR:!2025-10-03,73,330!2025-09-25,66,310!2025-09-24,65,310!2025-10-06,76,330!2025-10-03,73,330!2025-10-04,74,330!2025-09-25,66,310!2025-10-04,74,330!2025-09-24,65,310!2025-09-15,57,310!2025-10-04,74,330!2025-10-06,76,330-->

### vorticity

- Main article: ::@:: [Vorticity](vorticity.md) <!--SR:!2025-10-03,73,330!2025-10-05,75,330-->

{@{The [vorticity](vorticity.md) ${\boldsymbol {\omega } }$ of a vector field}@} can be defined by: {@{$${\boldsymbol {\omega } }~{\stackrel {\text{def} }{=} }~\nabla \times \mathbf {v} .$$}@} <!--SR:!2025-10-04,74,330!2025-10-05,75,330-->

{@{The vorticity of an irrotational field}@} is {@{zero everywhere}@}.<sup>[\[6\]](#^ref-6)</sup> {@{[Kelvin's circulation theorem](Kelvin's%20circulation%20theorem.md)}@} states that {@{a fluid that is irrotational in an [inviscid flow](inviscid%20flow.md) will remain irrotational}@}. This result can be derived from {@{the [vorticity transport equation](vorticity%20transport%20equation.md)}@}, obtained by {@{taking the curl of the [Navier–Stokes equations](Navier–Stokes%20equations.md)}@}. <!--SR:!2025-09-23,64,310!2025-10-03,73,330!2025-09-21,63,310!2025-10-06,76,330!2025-10-04,74,330!2025-10-04,74,330-->

For {@{a two-dimensional field}@}, the vorticity acts as {@{a measure of the _local_ rotation of fluid elements}@}. The vorticity does _not_ {@{imply anything about the global behavior of a fluid}@}. It is possible {@{for a fluid that travels in a straight line to have vorticity}@}, and it is possible {@{for a fluid that moves in a circle to be irrotational}@}. <!--SR:!2025-10-05,75,330!2025-10-06,76,330!2025-10-06,76,330!2025-10-05,75,330!2025-10-06,76,330-->

## conservative forces

> {@{![Examples of potential and gradient fields in physics](../../archives/Wikimedia%20Commons/Conservative%20fields.png)}@}
>
> Examples of {@{potential and gradient fields in physics}@}:
>
> - <span class="legend-color mw-no-invert" style="background-color:yellow; color:black;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> {@{Scalar fields, scalar potentials}@}:
>   - __V<sub>G</sub>__, {@{gravitational potential}@}
>   - __W<sub>pot</sub>__, {@{\(gravitational or electrostatic\) potential energy}@}
>   - __V<sub>C</sub>__, {@{Coulomb potential}@}
> - <span class="legend-color mw-no-invert" style="background-color:cyan; color:black;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> {@{Vector fields, gradient fields}@}:
>   - __a<sub>G</sub>__, {@{gravitational acceleration}@}
>   - __F__, {@{\(gravitational or electrostatic\) force}@}
>   - __E__, {@{electric field strength}@} <!--SR:!2025-09-23,64,310!2025-10-03,73,330!2025-10-03,73,330!2025-10-03,73,330!2025-10-05,75,330!2025-10-03,73,330!2025-10-04,74,330!2025-10-05,75,330!2025-10-06,76,330!2025-09-25,66,310-->

If {@{the vector field associated to a force $\mathbf {F}$ is conservative}@}, then {@{the force is said to be a [conservative force](conservative%20force.md)}@}. <!--SR:!2025-10-05,75,330!2025-10-03,73,330-->

{@{The most prominent examples of conservative forces}@} are {@{gravitational force \(associated with a gravitational field\)}@} and {@{electric force \(associated with an electrostatic field\)}@}. According to {@{[Newton's law of gravitation](Newton's%20law%20of%20universal%20gravitation.md)}@}, {@{a [gravitational force](gravitational%20force.md) $\mathbf {F} _{G}$ acting on a mass $m$ due to a mass $M$ located at a distance $r$ from $m$}@}, obeys the equation {@{$$\mathbf {F} _{G}=-{\frac {GmM}{r^{2} } }{\hat {\mathbf {r} } },$$}@} where {@{$G$ is the [gravitational constant](gravitational%20constant.md) and ${\hat {\mathbf {r} } }$ is a _unit_ vector pointing from $M$ toward $m$}@}. {@{The force of gravity is conservative}@} because {@{$\mathbf {F} _{G}=-\nabla \Phi _{G}$}@}, where {@{$$\Phi _{G}~{\stackrel {\text{def} }{=} }-{\frac {GmM}{r} }$$}@} is {@{the [gravitational potential energy](gravitational%20potential%20energy.md)}@}. In other words, {@{the gravitation field ${\frac {\mathbf {F} _{G} }{m} }$ associated with the gravitational force $\mathbf {F} _{G}$}@} is {@{the [gradient](gradient.md) of the gravitation potential ${\frac {\Phi _{G} }{m} }$ associated with the gravitational potential energy $\Phi _{G}$}@}. It can be shown that {@{any vector field of the form $\mathbf {F} =F(r){\hat {\mathbf {r} } }$ is conservative}@}, provided that {@{$F(r)$ is integrable}@}. <!--SR:!2025-10-05,75,330!2025-10-03,73,330!2025-09-20,62,310!2025-10-04,74,330!2025-09-24,65,310!2025-09-23,64,310!2025-09-25,66,310!2025-09-24,65,310!2025-09-24,65,310!2025-09-23,64,310!2025-10-05,75,330!2025-10-03,73,330!2025-10-05,75,330!2025-10-04,74,330!2025-10-05,75,330-->

For {@{[conservative forces](conservative%20force.md)}@}, {@{_path independence_}@} can be interpreted to mean that {@{the [work done](work%20done.md) in going from a point $A$ to a point $B$}@} is {@{independent of the moving path chosen \(dependent on only the points $A$ and $B$\)}@}, and that {@{the work $W$ done in going around a simple closed loop $C$ is $0$}@}: {@{$$W=\oint _{C}\mathbf {F} \cdot d{\mathbf {r} }=0.$$}@} <!--SR:!2025-10-06,76,330!2025-09-24,65,310!2025-10-06,76,330!2025-09-23,64,310!2025-10-03,73,330!2025-10-03,73,330-->

{@{The total [energy](conservation%20of%20energy.md) of a particle moving under the influence of conservative forces}@} is {@{conserved}@}, in the sense that {@{a loss of potential energy is converted to the equal quantity of kinetic energy, or vice versa}@}. <!--SR:!2025-10-04,74,330!2025-10-03,73,330!2025-09-25,66,310-->

## see also

- [Beltrami vector field](Beltrami%20vector%20field.md)
- [Conservative force](conservative%20force.md)
- [Conservative system](conservative%20system.md)
- [Complex lamellar vector field](complex%20lamellar%20vector%20field.md)
- [Helmholtz decomposition](Helmholtz%20decomposition.md)
- [Laplacian vector field](Laplacian%20vector%20field.md)
- [Longitudinal and transverse vector fields](longitudinal%20and%20transverse%20vector%20fields.md)
- [Solenoidal vector field](solenoidal%20vector%20field.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conservative_vector_field) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFMarsdenTromba2003"></a> [Marsden, Jerrold](Jerrold%20Marsden.md); Tromba, Anthony \(2003\). _Vector calculus_ \(Fifth ed.\). W.H.Freedman and Company. pp. 550–561. <a id="^ref-1"></a>^ref-1
2. George B. Arfken and Hans J. Weber, _Mathematical Methods for Physicists_, 6th edition, Elsevier Academic Press \(2005\) <a id="^ref-2"></a>^ref-2
3. For {@{$\mathbf {v} =\nabla \varphi$ to be [path-independent](#path%20independence)}@}, $\varphi$ is {@{not necessarily continuously differentiable}@}, {@{the condition of being differentiable is enough}@}, since {@{the [Gradient theorem](gradient%20theorem.md), that proves the path independence of $\nabla \varphi$}@}, does not {@{require $\varphi$ to be continuously differentiable}@}. There must be {@{a reason for the definition of conservative vector fields}@} to {@{require $\varphi$ to be [continuously differentiable](smoothness.md#multivariate%20differentiability%20classes)}@}. \(annotation: One possible reason is {@{to ensure the vector field is _integrable_ along any path}@}.\) <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFStewart2015"></a> Stewart, James \(2015\). "16.3 The Fundamental Theorem of Line Integrals"". _Calculus_ \(8th ed.\). Cengage Learning. pp. 1127–1134. [ISBN](ISBN%20(identifier).md) [978-1-285-74062-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-285-74062-1). <a id="^ref-4"></a>^ref-4
5. Need to verify if exact differentials also exist for non-orthogonal coordinate systems. <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFLiepmannRoshko1993"></a> [Liepmann, H.W.](Hans%20W.%20Liepmann.md); [Roshko, A.](Anatol%20Roshko.md) \(1993\) \[1957\], _Elements of Gas Dynamics_, Courier Dover Publications, [ISBN](ISBN%20(identifier).md) [0-486-41963-0](https://en.wikipedia.org/wiki/Special:BookSources/0-486-41963-0), pp. 194–196. <a id="^ref-6"></a>^ref-6 <!--SR:!2025-10-04,74,330!2025-09-24,65,310!2025-10-05,75,330!2025-09-26,67,310!2025-09-26,67,310!2025-09-25,66,310!2025-09-25,66,310!2025-09-23,64,310-->

## further reading

- <a id="CITEREFAcheson1990"></a> Acheson, D. J. \(1990\). _Elementary Fluid Dynamics_. Oxford University Press. [ISBN](ISBN%20(identifier).md) [0198596790](https://en.wikipedia.org/wiki/Special:BookSources/0198596790).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Vector calculus](https://en.wikipedia.org/wiki/Category:Vector%20calculus)
> - [Force](https://en.wikipedia.org/wiki/Category:Force)
