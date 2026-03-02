---
aliases:
  - del
  - del operator
  - del operators
  - nabla
  - nabla operator
  - nabla operators
tags:
  - flashcard/active/general/eng/del
  - language/in/English
---

# del

- This article is about {@{the mathematical operator represented by the nabla symbol}@}. For {@{the symbol itself}@}, see {@{[nabla symbol](nabla%20symbol.md)}@}. For {@{the operation associated with the symbol ∂, also sometimes referred to as "del"}@}, see {@{[Partial derivative](partial%20derivative.md)}@}. For other uses, see [Del \(disambiguation\)](del%20(disambiguation).md).
- Not to be confused with {@{[Dell](Dell.md)}@}. <!--SR:!2029-11-09,1340,350!2029-02-24,1136,350!2029-10-20,1327,350!2029-05-21,1201,350!2029-05-23,1202,350!2028-10-11,1030,350-->

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a [list of references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources), [related reading](https://en.wikipedia.org/wiki/Wikipedia:Further%20reading), or [external links](https://en.wikipedia.org/wiki/Wikipedia:External%20links), __but its sources remain unclear because it lacks [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(March 2010\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

> {@{![Del operator, represented by the [nabla symbol](nabla%20symbol.md)](../../archives/Wikimedia%20Commons/Del.svg)}@}
>
> {@{Del operator}@}, represented by {@{the [nabla symbol](nabla%20symbol.md)}@} <!--SR:!2029-02-23,1135,350!2029-10-21,1327,350!2029-07-26,1255,350-->

{@{__Del__, or __nabla__}@}, is {@{an [operator](operator%20(mathematics).md) used in mathematics \(particularly in [vector calculus](vector%20calculus.md)\) as a [vector](vector%20(geometry).md) [differential operator](differential%20operator.md)}@}, usually {@{represented by the [nabla symbol](nabla%20symbol.md) __∇__}@}. When {@{applied to a [function](function%20(mathematics).md) defined on a [one-dimensional](dimension%20(mathematics).md#in%20mathematics) domain}@}, it denotes {@{the standard [derivative](derivative.md) of the function as defined in [calculus](calculus.md)}@}. When {@{applied to a _field_ \(a function defined on a multi-dimensional domain\)}@}, it may denote {@{any one of three operations depending on the way it is applied}@}: {@{the [gradient](gradient.md) or \(locally\) steepest slope of a [scalar field](scalar%20field.md)}@} \(or sometimes of {@{a [vector field](vector%20field.md), as in the [Navier–Stokes equations](Navier–Stokes%20equations.md#interpretation%20as%20v%C2%B7(%E2%88%87v))}@}\); {@{the [divergence](divergence.md) of a vector field}@}; or {@{the [curl](curl%20(mathematics).md) \(rotation\) of a vector field}@}. <!--SR:!2029-04-22,1175,350!2029-10-08,1317,350!2029-09-22,1304,350!2029-07-28,1257,350!2029-03-24,1163,350!2029-02-28,1140,350!2028-11-07,1052,350!2029-04-21,1174,350!2029-02-25,1137,350!2029-10-14,1322,350!2028-06-27,946,348-->

Del is {@{a very convenient [mathematical notation](mathematical%20notation.md) for those three operations \(gradient, divergence, and curl\)}@} that {@{makes many [equations](equations.md) easier to write and remember}@}. The del symbol \(or nabla\) can be {@{[formally](formal%20calculation.md) defined as a vector operator whose components are the corresponding [partial derivative](partial%20derivative.md) operators}@}. As {@{a vector operator}@}, it can {@{act on scalar and vector fields in three different ways}@}, giving rise to {@{three different differential operations}@}: first, it can {@{act on scalar fields by a formal scalar multiplication}@}—to {@{give a vector field called the gradient}@}; second, it can {@{act on vector fields by a formal [dot product](dot%20product.md)}@}—to {@{give a scalar field called the divergence}@}; and lastly, it can {@{act on vector fields by a formal [cross product](cross%20product.md)}@}—to {@{give a vector field called the curl}@}. {@{These formal products}@} {@{do not necessarily [commute](commutative%20operation.md) with other operators or products}@}. These three uses, detailed below, are summarized as: <!--SR:!2029-11-07,1341,350!2029-10-03,1313,350!2029-10-29,1334,350!2029-07-24,1253,350!2029-03-10,1150,350!2029-04-07,1164,350!2027-07-27,677,330!2029-04-04,1168,350!2029-07-27,1256,350!2029-11-09,1343,350!2029-01-11,1092,350!2029-02-19,1131,350!2029-02-18,1130,350!2029-11-15,1345,350-->

- Gradient: ::@:: $\operatorname {grad} f=\nabla f$ <!--SR:!2029-03-21,1159,350!2029-10-24,1327,350-->
- Divergence: ::@:: $\operatorname {div} \mathbf {v} =\nabla \cdot \mathbf {v}$ <!--SR:!2029-01-31,1112,350!2029-09-26,1307,350-->
- Curl: ::@:: $\operatorname {curl} \mathbf {v} =\nabla \times \mathbf {v}$ <!--SR:!2029-09-15,1297,350!2029-10-19,1326,350-->

## definition

In {@{the [Cartesian coordinate system](Cartesian%20coordinate%20system.md) $\mathbb {R} ^{n}$ with coordinates $(x_{1},\dots ,x_{n})$}@} and {@{[standard basis](standard%20basis.md) $\{\mathbf {e} _{1},\dots ,\mathbf {e} _{n}\}$}@}, del is {@{a vector operator whose $x_{1},\dots ,x_{n}$ components are the [partial derivative](partial%20derivative.md) operators ${\partial  \over \partial x_{1} },\dots ,{\partial  \over \partial x_{n} }$}@}; that is, {@{$$\nabla =\sum _{i=1}^{n}\mathbf {e} _{i}{\partial  \over \partial x_{i} }=\left({\partial  \over \partial x_{1} },\ldots ,{\partial  \over \partial x_{n} }\right)$$}@} Where {@{the expression in parentheses is a row vector}@}. In {@{[three-dimensional](three-dimensional.md) Cartesian coordinate system $\mathbb {R} ^{3}$}@} with {@{coordinates $(x,y,z)$ and standard basis or unit vectors of axes $\{\mathbf {e} _{x},\mathbf {e} _{y},\mathbf {e} _{z}\}$}@}, del is written as {@{$$\nabla =\mathbf {e} _{x}{\partial  \over \partial x}+\mathbf {e} _{y}{\partial  \over \partial y}+\mathbf {e} _{z}{\partial  \over \partial z}=\left({\partial  \over \partial x},{\partial  \over \partial y},{\partial  \over \partial z}\right)$$}@} <!--SR:!2029-05-09,1191,350!2029-02-12,1124,350!2029-02-26,1138,350!2029-10-08,1317,350!2029-11-05,1339,350!2029-11-10,1344,350!2029-02-14,1126,350!2029-11-10,1344,350-->

As {@{a vector operator}@}, del naturally {@{acts on scalar fields via scalar multiplication}@}, and naturally {@{acts on vector fields via dot products and cross products}@}. <!--SR:!2029-05-31,1205,350!2029-11-15,1345,350!2029-08-03,1263,350-->

More specifically, for {@{any scalar field $f$ and any vector field $\mathbf {F} =(F_{x},F_{y},F_{z})$}@}, if one _defines_ <!--SR:!2029-11-02,1334,350-->

- (annotation: gradient, component) ::@:: $$\left(\mathbf {e} _{i}{\partial  \over \partial x_{i} }\right)f:={\partial  \over \partial x_{i} }(\mathbf {e} _{i}f)={\partial f \over \partial x_{i} }\mathbf {e} _{i}$$ <!--SR:!2029-05-04,1187,350!2029-11-11,1345,350-->
- (annotation: divergence, component) ::@:: $$\left(\mathbf {e} _{i}{\partial  \over \partial x_{i} }\right)\cdot \mathbf {F} :={\partial  \over \partial x_{i} }(\mathbf {e} _{i}\cdot \mathbf {F} )={\partial F_{i} \over \partial x_{i} }$$ <!--SR:!2029-07-25,1254,350!2029-01-22,1103,350-->
- (annotation: curl, component _x_) ::@:: $$\left(\mathbf {e} _{x}{\partial  \over \partial x}\right)\times \mathbf {F} :={\partial  \over \partial x}(\mathbf {e} _{x}\times \mathbf {F} )={\partial  \over \partial x}(0,-F_{z},F_{y})$$ <!--SR:!2027-01-08,515,310!2027-12-16,773,330-->
- (annotation: curl, component _y_) ::@:: $$\left(\mathbf {e} _{y}{\partial  \over \partial y}\right)\times \mathbf {F} :={\partial  \over \partial y}(\mathbf {e} _{y}\times \mathbf {F} )={\partial  \over \partial y}(F_{z},0,-F_{x})$$ <!--SR:!2028-07-05,874,330!2027-10-27,650,290-->
- (annotation: curl, component _z_) ::@:: $$\left(\mathbf {e} _{z}{\partial  \over \partial z}\right)\times \mathbf {F} :={\partial  \over \partial z}(\mathbf {e} _{z}\times \mathbf {F} )={\partial  \over \partial z}(-F_{y},F_{x},0),$$ <!--SR:!2026-11-09,460,310!2028-01-16,805,330-->

then using {@{the above definition of $\nabla$}@}, one may write {@{$$\nabla f=\left(\mathbf {e} _{x}{\partial  \over \partial x}\right)f+\left(\mathbf {e} _{y}{\partial  \over \partial y}\right)f+\left(\mathbf {e} _{z}{\partial  \over \partial z}\right)f={\partial f \over \partial x}\mathbf {e} _{x}+{\partial f \over \partial y}\mathbf {e} _{y}+{\partial f \over \partial z}\mathbf {e} _{z}$$}@} and {@{$$\nabla \cdot \mathbf {F} =\left(\mathbf {e} _{x}{\partial  \over \partial x}\cdot \mathbf {F} \right)+\left(\mathbf {e} _{y}{\partial  \over \partial y}\cdot \mathbf {F} \right)+\left(\mathbf {e} _{z}{\partial  \over \partial z}\cdot \mathbf {F} \right)={\partial F_{x} \over \partial x}+{\partial F_{y} \over \partial y}+{\partial F_{z} \over \partial z}$$}@} and {@{$${\begin{aligned}\nabla \times \mathbf {F} &=\left(\mathbf {e} _{x}{\partial  \over \partial x}\times \mathbf {F} \right)+\left(\mathbf {e} _{y}{\partial  \over \partial y}\times \mathbf {F} \right)+\left(\mathbf {e} _{z}{\partial  \over \partial z}\times \mathbf {F} \right)\\&={\partial  \over \partial x}(0,-F_{z},F_{y})+{\partial  \over \partial y}(F_{z},0,-F_{x})+{\partial  \over \partial z}(-F_{y},F_{x},0)\\&=\left({\partial F_{z} \over \partial y}-{\partial F_{y} \over \partial z}\right)\mathbf {e} _{x}+\left({\partial F_{x} \over \partial z}-{\partial F_{z} \over \partial x}\right)\mathbf {e} _{y}+\left({\partial F_{y} \over \partial x}-{\partial F_{x} \over \partial y}\right)\mathbf {e} _{z}\end{aligned} }$$}@} <!--SR:!2029-05-05,1188,350!2029-03-04,1144,350!2029-02-22,1134,350!2027-02-18,535,310-->

__Example:__

(annotation: example) $$f(x,y,z)=x+y+z$$ <p> ::@:: $$\nabla f=\mathbf {e} _{x}{\partial f \over \partial x}+\mathbf {e} _{y}{\partial f \over \partial y}+\mathbf {e} _{z}{\partial f \over \partial z}=\left(1,1,1\right)$$ <!--SR:!2029-10-22,1328,350!2029-04-19,1176,350-->

Del can also be {@{expressed in other coordinate systems}@}, see for example {@{[del in cylindrical and spherical coordinates](del%20in%20cylindrical%20and%20spherical%20coordinates.md)}@}. <!--SR:!2029-05-20,1197,350!2029-09-26,1306,350-->

## notational uses

Del is used as {@{a shorthand form to simplify many long mathematical expressions}@}. It is most commonly used to {@{simplify expressions for the [gradient](gradient.md), [divergence](divergence.md), [curl](curl%20(mathematics).md), [directional derivative](directional%20derivative.md), and [Laplacian](Laplacian.md)}@}. <!--SR:!2029-03-22,1160,350!2027-11-07,753,330-->

### gradient

{@{The vector derivative of a [scalar field](scalar%20field.md) $f$}@} is called {@{the [gradient](gradient.md)}@}, and it can be represented as: {@{$$\operatorname {grad} f={\partial f \over \partial x}{\hat {\mathbf {x} } }+{\partial f \over \partial y}{\hat {\mathbf {y} } }+{\partial f \over \partial z}{\hat {\mathbf {z} } }=\nabla f$$}@} <!--SR:!2029-05-17,1198,350!2029-01-05,1086,350!2029-10-12,1317,350-->

It always {@{points in the [direction](direction%20(geometry).md) of greatest increase of $f$}@}, and it has {@{a [magnitude](magnitude%20(mathematics).md) equal to the maximum rate of increase at the point}@}—just like {@{a standard derivative}@}. In particular, if {@{a hill is defined as a height function over a plane $h(x,y)$}@}, {@{the gradient at a given location}@} will be {@{a vector in the xy-plane \(visualizable as an arrow on a map\) pointing along the steepest direction}@}. {@{The magnitude of the gradient}@} is {@{the value of this steepest slope}@}. <!--SR:!2029-11-11,1345,350!2029-06-13,1220,350!2029-10-20,1327,350!2029-02-09,1121,350!2029-05-28,1206,350!2029-03-09,1149,350!2029-01-18,1099,350!2029-10-24,1327,350-->

In particular, this notation is powerful because {@{the gradient product rule looks very similar to the 1d-derivative case}@}: {@{$$\nabla (fg)=f\nabla g+g\nabla f$$}@} However, {@{the rules for [dot products](dot%20product.md) do not turn out to be simple}@}, as illustrated by: {@{$$\nabla (\mathbf {u} \cdot \mathbf {v} )=(\mathbf {u} \cdot \nabla )\mathbf {v} +(\mathbf {v} \cdot \nabla )\mathbf {u} +\mathbf {u} \times (\nabla \times \mathbf {v} )+\mathbf {v} \times (\nabla \times \mathbf {u} )$$}@} <!--SR:!2029-09-25,1303,350!2029-04-02,1166,350!2029-11-06,1340,350!2026-11-13,295,210-->

### divergence

{@{The [divergence](divergence.md) of a [vector field](vector%20field.md) $\mathbf {v} (x,y,z)=v_{x}{\hat {\mathbf {x} } }+v_{y}{\hat {\mathbf {y} } }+v_{z}{\hat {\mathbf {z} } }$}@} is {@{a [scalar field](scalar%20field.md)}@} that can be represented as: {@{$$\operatorname {div} \mathbf {v} ={\partial v_{x} \over \partial x}+{\partial v_{y} \over \partial y}+{\partial v_{z} \over \partial z}=\nabla \cdot \mathbf {v}$$}@} <!--SR:!2029-03-13,1153,350!2029-10-02,1312,350!2029-03-28,1166,350-->

The divergence is roughly {@{a measure of a vector field's increase in the direction it points}@}; but more accurately, it is {@{a measure of that field's tendency to converge toward or diverge from a point}@}. <!--SR:!2029-11-05,1340,350!2028-11-01,1047,350-->

{@{The power of the del notation}@} is shown by {@{the following product rule}@}: {@{$$\nabla \cdot (f\mathbf {v} )=(\nabla f)\cdot \mathbf {v} +f(\nabla \cdot \mathbf {v} )$$}@} {@{The formula for the [vector product](vector%20product.md) is slightly less intuitive}@}, because {@{this product is not commutative}@}: {@{$$\nabla \cdot (\mathbf {u} \times \mathbf {v} )=(\nabla \times \mathbf {u} )\cdot \mathbf {v} -\mathbf {u} \cdot (\nabla \times \mathbf {v} )$$}@} <!--SR:!2029-02-03,1115,350!2028-04-16,822,330!2027-09-16,712,330!2026-09-25,427,310!2027-01-30,523,310!2026-11-30,390,230-->

### curl

{@{The [curl](curl%20(mathematics).md) of a vector field $\mathbf {v} (x,y,z)=v_{x}{\hat {\mathbf {x} } }+v_{y}{\hat {\mathbf {y} } }+v_{z}{\hat {\mathbf {z} } }$}@} is {@{a [vector](vector%20field.md) function that can be represented as}@}: {@{$$\operatorname {curl} \mathbf {v} =\left({\partial v_{z} \over \partial y}-{\partial v_{y} \over \partial z}\right){\hat {\mathbf {x} } }+\left({\partial v_{x} \over \partial z}-{\partial v_{z} \over \partial x}\right){\hat {\mathbf {y} } }+\left({\partial v_{y} \over \partial x}-{\partial v_{x} \over \partial y}\right){\hat {\mathbf {z} } }=\nabla \times \mathbf {v}$$}@} <!--SR:!2029-10-18,1322,350!2029-05-11,1193,350!2027-12-27,782,330-->

{@{The curl at a point}@} is {@{proportional to the on-axis torque}@} that {@{a tiny pinwheel would be subjected to if it were centered at that point}@}. <!--SR:!2029-03-05,1145,350!2028-05-09,842,330!2026-06-25,127,389-->

{@{The vector product operation}@} can be visualized as {@{a pseudo-[determinant](determinant.md)}@}: {@{$$\nabla \times \mathbf {v} =\left|{\begin{matrix}{\hat {\mathbf {x} } }&{\hat {\mathbf {y} } }&{\hat {\mathbf {z} } }\\[2pt]{\frac {\partial }{\partial x} }&{\frac {\partial }{\partial y} }&{\frac {\partial }{\partial z} }\\[2pt]v_{x}&v_{y}&v_{z}\end{matrix} }\right|$$}@} <!--SR:!2029-01-24,1105,350!2029-07-03,1236,350!2028-10-08,1028,350-->

Again {@{the power of the notation}@} is shown by {@{the product rule}@}: {@{$$\nabla \times (f\mathbf {v} )=(\nabla f)\times \mathbf {v} +f(\nabla \times \mathbf {v} )$$}@} {@{The rule for the vector product}@} does not turn out to be simple: {@{$$\nabla \times (\mathbf {u} \times \mathbf {v} )=\mathbf {u} \,(\nabla \cdot \mathbf {v} )-\mathbf {v} \,(\nabla \cdot \mathbf {u} )+(\mathbf {v} \cdot \nabla )\,\mathbf {u} -(\mathbf {u} \cdot \nabla )\,\mathbf {v}$$}@} <!--SR:!2029-04-13,1177,350!2029-08-03,1263,350!2028-05-01,877,330!2027-05-23,626,330!2026-12-02,394,250-->

### directional derivative

{@{The [directional derivative](directional%20derivative.md) of a scalar field $f(x,y,z)$}@} in {@{the direction $\mathbf {a} (x,y,z)=a_{x}{\hat {\mathbf {x} } }+a_{y}{\hat {\mathbf {y} } }+a_{z}{\hat {\mathbf {z} } }$}@} is defined as: {@{$$(\mathbf {a} \cdot \nabla )f=\lim _{h\to 0}{\frac {f(x+a_{x}h,y+a_{y}h,z+a_{z}h)-f(x,y,z)}{h} }.$$}@} Which is {@{equal to the following when the gradient exists}@} {@{$$\mathbf {a} \cdot \operatorname {grad} f=a_{x}{\partial f \over \partial x}+a_{y}{\partial f \over \partial y}+a_{z}{\partial f \over \partial z}=\mathbf {a} \cdot (\nabla f)$$}@} <!--SR:!2029-04-16,1180,350!2029-11-11,1345,350!2029-03-14,1154,350!2029-08-03,1263,350!2029-03-27,1165,350-->

This gives {@{the rate of change of a field $f$ in the direction of $\mathbf {a}$, scaled by the magnitude of $\mathbf {a}$}@}. In operator notation, {@{the element in parentheses}@} can be {@{considered a single coherent unit}@}; {@{[fluid dynamics](fluid%20dynamics.md)}@} uses {@{this convention extensively}@}, terming it {@{the [convective derivative](convective%20derivative.md)—the "moving" derivative of the fluid}@}. <!--SR:!2029-03-23,1162,350!2029-07-06,1235,350!2028-10-24,1042,350!2029-03-03,1143,350!2029-10-07,1313,350!2029-10-14,1322,350-->

Note that {@{$(\mathbf {a} \cdot \nabla )$ is an operator that takes scalar to a scalar}@}. It can be {@{extended to operate on a vector}@}, by {@{separately operating on each of its components}@}. <!--SR:!2029-11-05,1340,350!2029-04-30,1183,350!2029-03-01,1141,350-->

### Laplacian

{@{The [Laplace operator](Laplace%20operator.md)}@} is {@{a scalar operator that can be applied to either vector or scalar fields}@}; for {@{cartesian coordinate systems}@} it is defined as: {@{$$\Delta ={\partial ^{2} \over \partial x^{2} }+{\partial ^{2} \over \partial y^{2} }+{\partial ^{2} \over \partial z^{2} }=\nabla \cdot \nabla =\nabla ^{2}$$}@} and {@{the definition for more general coordinate systems}@} is given in {@{[vector Laplacian](vector%20Laplacian.md#vector%20Laplacian)}@}. <!--SR:!2028-12-28,1078,350!2029-11-05,1340,350!2029-10-05,1311,350!2029-11-10,1344,350!2029-02-11,1123,350!2029-04-15,1179,350-->

The Laplacian is {@{ubiquitous throughout modern [mathematical physics](mathematical%20physics.md)}@}, appearing for example in {@{[Laplace's equation](Laplace's%20equation.md), [Poisson's equation](Poisson's%20equation.md), the [heat equation](heat%20equation.md)}@}, {@{the [wave equation](wave%20equation.md), and the [Schrödinger equation](Schrödinger%20equation.md)}@}. <!--SR:!2029-11-03,1335,350!2029-10-14,1318,350!2029-04-25,1180,350-->

### Hessian matrix

While {@{$\nabla ^{2}$ usually represents the [Laplacian](Laplacian.md)}@}, sometimes {@{$\nabla ^{2}$ also represents the [Hessian matrix](Hessian%20matrix.md)}@}. The former refers to {@{the inner product of $\nabla$}@}, while the latter refers to {@{the [dyadic product](dyadic%20product.md) of $\nabla$}@}: <p> {@{$\nabla ^{2}=\nabla \cdot \nabla ^{T}$}@}. <p> So {@{whether $\nabla ^{2}$ refers to a Laplacian or a Hessian matrix}@} depends on the context. <!--SR:!2029-06-07,1215,350!2029-03-06,1146,350!2027-06-03,635,330!2029-11-11,1345,350!2029-01-19,1100,350!2029-02-20,1132,350-->

### tensor derivative

Del can also be {@{applied to a vector field with the result being a [tensor](tensor.md)}@}. {@{The [tensor derivative](tensor%20derivative.md) of a vector field $\mathbf {v}$ \(in three dimensions\)}@} is {@{a 9-term second-rank tensor – that is, a 3×3 matrix}@} – but can be denoted simply as {@{$\nabla \otimes \mathbf {v}$}@}, where {@{$\otimes$ represents the [dyadic product](dyadic%20product.md)}@}. This quantity is equivalent to {@{the transpose of the [Jacobian matrix](Jacobian%20matrix.md) of the vector field with respect to space}@}. {@{The divergence of the vector field}@} can then be expressed as {@{the [trace](trace%20(linear%20algebra).md) of this matrix}@}. <!--SR:!2029-03-08,1148,350!2027-07-08,661,330!2029-10-28,1333,350!2029-11-09,1340,350!2029-04-17,1181,350!2028-05-05,877,330!2029-04-24,1179,350!2027-12-25,781,330-->

For {@{a small displacement $\delta \mathbf {r}$}@}, {@{the change in the vector field}@} is given by: {@{$$\delta \mathbf {v} =(\nabla \otimes \mathbf {v} )^{T}\cdot \delta \mathbf {r}$$ (annotation: $(\nabla \otimes \mathbf v)^\intercal$ is the Jacobian matrix)}@} <!--SR:!2027-03-16,527,310!2027-11-11,759,330!2026-04-14,297,290-->

## product rules

For {@{[vector calculus](vector%20calculus.md)}@}: $${\begin{aligned}\nabla (fg)&=f\nabla g+g\nabla f\\\nabla (\mathbf {u} \cdot \mathbf {v} )&=\mathbf {u} \times (\nabla \times \mathbf {v} )+\mathbf {v} \times (\nabla \times \mathbf {u} )+(\mathbf {u} \cdot \nabla )\mathbf {v} +(\mathbf {v} \cdot \nabla )\mathbf {u} \\\nabla \cdot (f\mathbf {v} )&=f(\nabla \cdot \mathbf {v} )+\mathbf {v} \cdot (\nabla f)\\\nabla \cdot (\mathbf {u} \times \mathbf {v} )&=\mathbf {v} \cdot (\nabla \times \mathbf {u} )-\mathbf {u} \cdot (\nabla \times \mathbf {v} )\\\nabla \times (f\mathbf {v} )&=(\nabla f)\times \mathbf {v} +f(\nabla \times \mathbf {v} )\\\nabla \times (\mathbf {u} \times \mathbf {v} )&=\mathbf {u} \,(\nabla \cdot \mathbf {v} )-\mathbf {v} \,(\nabla \cdot \mathbf {u} )+(\mathbf {v} \cdot \nabla )\,\mathbf {u} -(\mathbf {u} \cdot \nabla )\,\mathbf {v} \end{aligned} }$$ <!--SR:!2029-06-15,1218,350-->

For {@{[matrix calculus](matrix%20calculus.md) \(for which $\mathbf {u} \cdot \mathbf {v}$ can be written $\mathbf {u} ^{\text{T} }\mathbf {v}$\)}@}: {@{$${\begin{aligned}\left(\mathbf {A} \nabla \right)^{\text{T} }\mathbf {u} &=\nabla ^{\text{T} }\left(\mathbf {A} ^{\text{T} }\mathbf {u} \right)-\left(\nabla ^{\text{T} }\mathbf {A} ^{\text{T} }\right)\mathbf {u} \end{aligned} }$$}@} <!--SR:!2026-10-11,399,290!2027-06-21,552,286-->

{@{Another relation of interest \(see e.g. _[Euler equations](Euler%20equations.md#equations)_\)}@} is the following, where {@{$\mathbf {u} \otimes \mathbf {v}$ is the [outer product](outer%20product.md) tensor}@}: {@{$${\begin{aligned}\nabla \cdot (\mathbf {u} \otimes \mathbf {v} )=(\nabla \cdot \mathbf {u} )\mathbf {v} +(\mathbf {u} \cdot \nabla )\mathbf {v} \end{aligned} }$$}@} <!--SR:!2028-01-19,789,330!2026-06-25,349,290!2027-05-05,618,346-->

> __flashcards__
>
> - $\nabla (fg)$ ::@:: $=f\nabla g+g\nabla f$ <!--SR:!2029-02-26,1138,350!2029-02-13,1125,350-->
> - $\nabla (\mathbf {u} \cdot \mathbf {v} )$ ::@:: $=\mathbf {u} \times (\nabla \times \mathbf {v} )+\mathbf {v} \times (\nabla \times \mathbf {u} )+(\mathbf {u} \cdot \nabla )\mathbf {v} +(\mathbf {v} \cdot \nabla )\mathbf {u}$ <!--SR:!2026-05-23,95,230!2026-12-03,485,310-->
> - $\nabla \cdot (f\mathbf {v} )$ ::@:: $=f(\nabla \cdot \mathbf {v} )+\mathbf {v} \cdot (\nabla f)$ <!--SR:!2027-06-02,633,330!2028-12-19,1069,350-->
> - $\nabla \cdot (\mathbf {u} \times \mathbf {v} )$ ::@:: $=\mathbf {v} \cdot (\nabla \times \mathbf {u} )-\mathbf {u} \cdot (\nabla \times \mathbf {v} )$ <!--SR:!2026-07-24,190,210!2027-05-13,555,270-->
> - $\nabla \times (f\mathbf {v} )$ ::@:: $=(\nabla f)\times \mathbf {v} +f(\nabla \times \mathbf {v} )$ <!--SR:!2027-09-04,664,290!2029-10-14,1322,350-->
> - $\nabla \times (\mathbf {u} \times \mathbf {v} )$ ::@:: $=\mathbf {u} \,(\nabla \cdot \mathbf {v} )-\mathbf {v} \,(\nabla \cdot \mathbf {u} )+(\mathbf {v} \cdot \nabla )\,\mathbf {u} -(\mathbf {u} \cdot \nabla )\,\mathbf {v}$ <!--SR:!2026-10-21,335,250!2026-03-24,32,190-->
> - $\left(\mathbf {A} \nabla \right)^{\text{T} }\mathbf {u}$ ::@:: $=\nabla ^{\text{T} }\left(\mathbf {A} ^{\text{T} }\mathbf {u} \right)-\left(\nabla ^{\text{T} }\mathbf {A} ^{\text{T} }\right)\mathbf {u}$ <!--SR:!2026-03-20,36,130!2027-02-20,377,230-->
> - $\nabla \cdot (\mathbf {u} \otimes \mathbf {v} )$ ::@:: $=(\nabla \cdot \mathbf {u} )\mathbf {v} +(\mathbf {u} \cdot \nabla )\mathbf {v}$ <!--SR:!2026-05-16,258,290!2026-07-16,138,270-->

## second derivatives

> {@{![DCG chart: A simple chart depicting all rules pertaining to second derivatives.](../../archives/Wikimedia%20Commons/DCG%20chart.svg)}@}
>
> {@{DCG chart}@}: {@{A simple chart depicting all rules pertaining to second derivatives}@}. {@{D, C, G, L and CC}@} stand for {@{divergence, curl, gradient, Laplacian and curl of curl}@}, respectively. Arrows indicate {@{existence of second derivatives}@}. {@{Blue circle in the middle}@} represents {@{curl of curl}@}, whereas {@{the other two red circles \(dashed\) mean that DD and GG do not exist}@}. <!--SR:!2026-10-25,449,310!2027-10-13,733,330!2029-09-23,1304,350!2027-12-17,774,330!2029-02-27,1139,350!2027-10-10,734,330!2029-10-19,1326,350!2029-03-21,1160,350!2028-04-06,812,330-->

When {@{del operates on a scalar or vector}@}, {@{either a scalar or vector is returned}@}. Because of {@{the diversity of vector products \(scalar, dot, cross\)}@} {@{one application of del already gives rise to three major derivatives}@}: {@{the gradient \(scalar product\), divergence \(dot product\), and curl \(cross product\)}@}. {@{Applying these three sorts of derivatives again to each other}@} gives {@{five possible second derivatives, for a scalar field _f_ or a vector field ___v___}@}; {@{the use of the scalar [Laplacian](Laplacian.md) and [vector Laplacian](vector%20Laplacian.md#vector%20Laplacian)}@} {@{gives two more}@}: $${\begin{aligned}\operatorname {div} (\operatorname {grad} f)&=\nabla \cdot (\nabla f)=\nabla ^{2}f\\\operatorname {curl} (\operatorname {grad} f)&=\nabla \times (\nabla f)\\\operatorname {grad} (\operatorname {div} \mathbf {v} )&=\nabla (\nabla \cdot \mathbf {v} )\\\operatorname {div} (\operatorname {curl} \mathbf {v} )&=\nabla \cdot (\nabla \times \mathbf {v} )\\\operatorname {curl} (\operatorname {curl} \mathbf {v} )&=\nabla \times (\nabla \times \mathbf {v} )\\\Delta f&=\nabla ^{2}f\\\Delta \mathbf {v} &=\nabla ^{2}\mathbf {v} \end{aligned} }$$ <!--SR:!2029-02-01,1113,350!2029-04-12,1165,350!2029-04-13,1166,350!2029-03-30,1167,350!2029-02-07,1119,350!2029-02-19,1131,350!2029-10-29,1331,350!2029-11-15,1345,350!2029-03-31,1164,350-->

> __flashcards__
>
> - $\operatorname {div} (\operatorname {grad} f)$ ::@:: $=\nabla \cdot (\nabla f)=\nabla ^{2}f$ <!--SR:!2029-09-22,1304,350!2029-09-22,1304,350-->
> - $\operatorname {curl} (\operatorname {grad} f)$ ::@:: $=\nabla \times (\nabla f)$ <!--SR:!2029-02-16,1128,350!2029-01-23,1104,350-->
> - $\operatorname {grad} (\operatorname {div} \mathbf {v} )$ ::@:: $=\nabla (\nabla \cdot \mathbf {v} )$ <!--SR:!2028-10-01,943,330!2029-03-12,1152,350-->
> - $\operatorname {div} (\operatorname {curl} \mathbf {v} )$ ::@:: $=\nabla \cdot (\nabla \times \mathbf {v} )$ <!--SR:!2029-02-02,1114,350!2029-06-19,1224,350-->
> - $\operatorname {curl} (\operatorname {curl} \mathbf {v} )$ ::@:: $=\nabla \times (\nabla \times \mathbf {v} )$ <!--SR:!2028-08-14,905,330!2029-09-27,1308,350-->
> - $\Delta f$ ::@:: $=\nabla ^{2}f$ <!--SR:!2029-03-22,1161,350!2029-10-01,1308,350-->
> - $\Delta \mathbf {v}$ ::@:: $=\nabla ^{2}\mathbf {v}$ <!--SR:!2029-06-14,1220,350!2029-11-09,1343,350-->

These are {@{of interest principally}@} because {@{they are not always unique or independent of each other}@}. As long as {@{the functions are well-behaved \($C^{\infty }$ in most cases\)}@}, {@{two of them are always zero}@}: {@{$${\begin{aligned}\operatorname {curl} (\operatorname {grad} f)&=\nabla \times (\nabla f)=0\\\operatorname {div} (\operatorname {curl} \mathbf {v} )&=\nabla \cdot (\nabla \times \mathbf {v} )=0\end{aligned} }$$}@} <!--SR:!2029-11-05,1339,350!2029-11-08,1342,350!2028-12-18,1068,350!2029-10-28,1330,350!2029-09-17,1296,350-->

{@{Two of them are always equal}@}: {@{$$\operatorname {div} (\operatorname {grad} f)=\nabla \cdot (\nabla f)=\nabla ^{2}f=\Delta f$$}@} <!--SR:!2029-02-21,1133,350!2029-03-15,1155,350-->

{@{The 3 remaining vector derivatives}@} are related by the equation: {@{$$\nabla \times \left(\nabla \times \mathbf {v} \right)=\nabla (\nabla \cdot \mathbf {v} )-\nabla ^{2}\mathbf {v}$$ (annotation: notice the similarity to $\mathbf a \times (\mathbf b \times \mathbf c) = (\mathbf a \cdot \mathbf c) \mathbf b - (\mathbf a \cdot \mathbf b) \mathbf c$)}@} <!--SR:!2029-04-29,1182,350!2026-08-17,325,250-->

And {@{one of them can even be expressed with the tensor product}@}, if {@{the functions are well-behaved}@}: {@{$$\nabla (\nabla \cdot \mathbf {v} )=\nabla \cdot (\mathbf {v} \otimes \nabla )$$}@} <!--SR:!2026-11-29,482,310!2026-09-10,342,230!2026-10-09,331,380-->

## precautions

{@{Most of the above vector properties}@} \(except {@{for those that rely explicitly on del's differential properties—for example, the product rule}@}\) {@{rely only on symbol rearrangement}@}, and {@{must necessarily hold if the del symbol is replaced by any other vector}@}. This is part of {@{the value to be gained in notationally representing this operator as a vector}@}. <!--SR:!2029-10-08,1317,350!2028-04-19,825,330!2029-01-10,1091,350!2029-03-07,1147,350!2029-02-08,1120,350-->

Though {@{one can often replace del with a vector and obtain a vector identity}@}, {@{making those identities mnemonic}@}, {@{the reverse is _not_ necessarily reliable}@}, because {@{del does not commute in general}@}. <!--SR:!2029-01-02,1083,350!2029-03-17,1156,350!2029-03-29,1167,350!2029-04-04,1161,350-->

A counterexample that demonstrates {@{the divergence \($\nabla \cdot \mathbf {v}$\) and the [advection operator](advection.md#mathematics%20of%20advection) \($\mathbf {v} \cdot \nabla$\) are not commutative}@}: {@{$${\begin{aligned}(\mathbf {u} \cdot \mathbf {v} )f&\equiv (\mathbf {v} \cdot \mathbf {u} )f\\(\nabla \cdot \mathbf {v} )f&=\left({\frac {\partial v_{x} }{\partial x} }+{\frac {\partial v_{y} }{\partial y} }+{\frac {\partial v_{z} }{\partial z} }\right)f={\frac {\partial v_{x} }{\partial x} }f+{\frac {\partial v_{y} }{\partial y} }f+{\frac {\partial v_{z} }{\partial z} }f\\(\mathbf {v} \cdot \nabla )f&=\left(v_{x}{\frac {\partial }{\partial x} }+v_{y}{\frac {\partial }{\partial y} }+v_{z}{\frac {\partial }{\partial z} }\right)f=v_{x}{\frac {\partial f}{\partial x} }+v_{y}{\frac {\partial f}{\partial y} }+v_{z}{\frac {\partial f}{\partial z} }\\\Rightarrow (\nabla \cdot \mathbf {v} )f&\neq (\mathbf {v} \cdot \nabla )f\\\end{aligned} }$$}@} <!--SR:!2029-02-15,1127,350!2027-08-04,682,330-->

A counterexample that {@{relies on del's differential properties}@}: {@{$${\begin{aligned}(\nabla x)\times (\nabla y)&=\left(\mathbf {e} _{x}{\frac {\partial x}{\partial x} }+\mathbf {e} _{y}{\frac {\partial x}{\partial y} }+\mathbf {e} _{z}{\frac {\partial x}{\partial z} }\right)\times \left(\mathbf {e} _{x}{\frac {\partial y}{\partial x} }+\mathbf {e} _{y}{\frac {\partial y}{\partial y} }+\mathbf {e} _{z}{\frac {\partial y}{\partial z} }\right)\\&=(\mathbf {e} _{x}\cdot 1+\mathbf {e} _{y}\cdot 0+\mathbf {e} _{z}\cdot 0)\times (\mathbf {e} _{x}\cdot 0+\mathbf {e} _{y}\cdot 1+\mathbf {e} _{z}\cdot 0)\\&=\mathbf {e} _{x}\times \mathbf {e} _{y}\\&=\mathbf {e} _{z}\\(\mathbf {u} x)\times (\mathbf {u} y)&=xy(\mathbf {u} \times \mathbf {u} )\\&=xy\mathbf {0} \\&=\mathbf {0} \end{aligned} }$$}@} <!--SR:!2029-07-29,1258,350!2026-09-24,426,310-->

{@{Central to these distinctions}@} is the fact that {@{del is not simply a vector; it is a [vector operator](vector%20operator.md)}@}. Whereas {@{a vector is an object with both a magnitude and direction}@}, del {@{has neither a magnitude nor a direction until it operates on a function}@}. <!--SR:!2029-04-05,1169,350!2029-10-11,1316,350!2029-02-04,1116,350!2029-11-06,1340,350-->

For that reason, {@{identities involving del must be derived with care}@}, using {@{both vector identities and _differentiation_ identities such as the product rule}@}. <!--SR:!2029-03-23,1161,350!2029-05-18,1199,350-->

## see also

- [Del in cylindrical and spherical coordinates](del%20in%20cylindrical%20and%20spherical%20coordinates.md)
- [Notation for differentiation](notation%20for%20differentiation.md)
- [Vector calculus identities](vector%20calculus%20identities.md)
- [Maxwell's equations](Maxwell's%20equations.md)
- [Navier–Stokes equations](Navier–Stokes%20equations.md)
- [Table of mathematical symbols](table%20of%20mathematical%20symbols.md)
- [Quabla operator](quabla%20operator.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/del) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- [Willard Gibbs](Willard%20Gibbs.md) & [Edwin Bidwell Wilson](Edwin%20Bidwell%20Wilson.md) \(1901\) [Vector Analysis](Vector%20Analysis.md), [Yale University Press](Yale%20University%20Press.md), 1960: [Dover Publications](Dover%20Publications.md).
- <a id="CITEREFSchey1997"></a> Schey, H. M. \(1997\). _Div, Grad, Curl, and All That: An Informal Text on Vector Calculus_. New York: Norton. [ISBN](ISBN%20(identifier).md) [0-393-96997-5](https://en.wikipedia.org/wiki/Special:BookSources/0-393-96997-5).
- <a id="CITEREFMiller"></a> Miller, Jeff. ["Earliest Uses of Symbols of Calculus"](http://jeff560.tripod.com/calculus.html).
- <a id="CITEREFArnold Neumaier1998"></a> Arnold Neumaier \(January 26, 1998\). Cleve Moler \(ed.\). ["History of Nabla"](http://www.netlib.org/na-digest-html/98/v98n03.html#2). NA Digest, Volume 98, Issue 03. netlib.org.

## external links

- <a id="CITEREFTai1994"></a> Tai, Chen-To \(1994\). A survey of the improper use of ∇ in vector analysis \(Report\). Radiation Laboratory, University of Michigan. [hdl](hdl%20(identifier).md):[2027.42/7869](https://hdl.handle.net/2027.42%2F7869).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Vector calculus](https://en.wikipedia.org/wiki/Category:Vector%20calculus)
> - [Mathematical notation](https://en.wikipedia.org/wiki/Category:Mathematical%20notation)
> - [Differential operators](https://en.wikipedia.org/wiki/Category:Differential%20operators)
