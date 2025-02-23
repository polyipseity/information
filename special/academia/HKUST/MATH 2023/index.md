---
aliases:
  - HKUST MATH 2023
  - HKUST MATH 2023 index
  - HKUST MATH2023
  - HKUST MATH2023 index
  - MATH 2023
  - MATH 2023 index
  - MATH2023
  - MATH2023 index
  - Multivariable Calculus
  - Multivariable Calculus index
tags:
  - flashcard/active/special/academia/HKUST/MATH_2023/index
  - function/index
  - language/in/English
---

# index

- HKUST MATH 2023
- name: Multivariable Calculus

The content is in teaching order.

- grading
  - scheme
    - homework ×?: 10%
    - midterm exam: 40%
    - final exam: 50%
- logistics

## children

<!-- - [questions](questions.md) -->

## week 1 lecture

- datetime: 2025-02-04T13:30:00+08:00/2025-02-04T14:50:00+08:00
- [function](../../../../general/function%20(mathematics).md) ::@:: image, pre-image, graph of a function, continuity
  - function / image ::@:: It of an input value $x$ is the single output value produced by $f$ when passed $x$. It of a set of input values $X$ is the set of output values produced by $f$ when passed each value of $X$.
  - function / pre-image ::@:: It of an output value $y$ is the set of input values that produce $y$ when passed to $f$. It of a set of output values $Y$ is the set of input values that produce any value in $Y$ when passed to $f$.
  - function / graph of a function ::@:: The set of points $(x, f(x))$ for all $x$ in the domain of $f$ on the 2D Cartesian plane. <p> Not all set of points $(x, y)$ is the graph of a function. Use the vertical line test: If any vertical line pass through at most one point in the set, then the graph is a function.
  - function / [continuity](../../../../general/continuous%20function.md) ::@:: The limit of the function at each input value equals the function evaluated at that value. (Some special cases regarding domain boundaries have been omitted here...)
- [calculus](../../../../general/calculus.md) ::@:: rate of change, differentiation, integration, fundamental theorem of calculus
  - calculus / [differentiation](../../../../general/derivative.md) ::@:: Definition: $$f'(x) = \lim_{\delta \to 0} \frac {f(x + \delta) - f(x)} {\delta} \,$$ if it exists. But in practice, we apply some rules. <p> Related to the rate of change.
  - calculus / [integration](../../../../general/integral.md) ::@:: Inverse operation to differentiation. <p> Related to area under the curve.
  - calculus / [fundamental theorem of calculus](../../../../general/fundamental%20theorem%20of%20calculus.md) ::@:: There are 2 parts. It relates a function to its antiderivatives. <p> The first part: We have a continuous function $f$. Then we can define a function as the definite integral of $f$ from $a$ to $x$. The function is an antiderivative of $f$. <p> The second part: We have a Riemann integrable function $f$. We also have a function $F$ that is the antiderivaive of $f$. Then the definite integral of $f$ from $a$ to $b$ is $F(b) - F(a)$.
- function
  - function / extension in this course ::@:: We will study functions with multiple inputs and/or multiple outputs.
- [function of several real variables](../../../../general/function%20of%20a%20several%20real%20variables.md) ::@:: In general, $$\mathbb R^n \to X \,.$$ <p> For this course in particular, we will focus on $X = \mathbb R^m$.
- [Cartesian coordinate system](../../../../general/Cartesian%20coordinate%20system.md) ::@:: A coordinate system that specifies each point uniquely by a pair of real numbers called _coordinates_, which are the signed distances to the point from two fixed perpendicular oriented lines, called _coordinate lines_, _coordinate axes_ or just _axes_ (plural of _axis_) of the system.
  - Cartesian coordinate system / dimension ::@:: number of points to describe a point
  - Cartesian coordinate system / symbols ::@:: Using real numbers, $\mathbb R^n$, where $n$ is the dimension of the entire space.
  - Cartesian coordinate system / orientation ::@:: left-hand side, right-hand side; by most convention (including this course), we use right-hand side
  - Cartesian coordinate system / shape description ::@:: Equations can describe a subset of points of the entire space. Intersection and/or union may be used to define shapes defined by multiple equations. <p> For example: $x^2 + y^2 + z^2 = r^2$ is a 3D sphere of radius $r$.
  - Cartesian coordinate system / projection ::@:: Orthogonal project may be used to extract a specific coordinate of a point.
- [Euclidean vector](../../../../general/Euclidean%20vector.md) ::@:: A set whose elements, often called _vectors_, can be added together and multiplied ("scaled") by numbers called _scalars_.
  - Euclidean vector / vector ::@:: A line segment with a direction, up to translation. That is, two vectors are the same if they have the same length and direction. <p> The zero vector has 0 length and no direction.
  - Euclidean vector / scalar ::@:: A real number. In general, the field associated with the vector space.
  - Euclidean vector / position vector ::@:: A vector used to represent the position of a point. <p> For example, in 3D space, the point $(x, y, z)$ can be represented by the position vector $\langle x, y, z \rangle$ (note the angle brackets).
  - Euclidean vector / element-wise operations ::@:: vector addition, vector subtraction: perform the operation on each coordinate separately to get the resulting vector
  - Euclidean vector / scalar multiplication ::@:: multiply each coordinate by the specified scalar to get the resulting vector
  - Euclidean vector / magnitude or length ::@:: The square root of the sum of the squared coordinates. This is a specific case of the _p_-norm. <p> For example, the vector $\vec v = \langle x, y, z \rangle$ has the magnitude $\lvert \vec v \rvert = \sqrt{x^2 + y^2 + z^2}$.
  - [unit vector](../../../../general/unit%20vector.md) ::@:: A vector of magnitude 1. The unit vector associated with an arbitrary vector $\vec v$ is $\vec v / \lvert \vec v \rvert$. The zero vector has no unit vector, as it has no direction. <p> For example, in 3D space, the unit vectors along the coordinate axes (and their notations): $\vec i = \langle 1, 0, 0 \rangle, \vec j = \langle 0, 1, 0 \rangle, \vec k = \langle 0, 0, 1 \rangle$. These 3 unit vectors form is _an_ (not _the_) orthonormal basis of the 3D space.
  - [orthonormal basis](../../../../general/orthonormal%20basis.md) ::@:: The set of unit vectors along the coordinate axes form an orthonormal basis. This means any vector can be _uniquely_ written as a linear combination of the orthonormal basis. <p> For example, in 3D space, each vector $\vec v$ can be written uniquely as $\vec v = x \vec i + y \vec j + z \vec k$, where $x, y, z$ are scalars.

## week 1 tutorial

- datetime: 2025-02-04T16:00:00+08:00/2025-02-04T16:50:00+08:00
- [week 1 lecture](#week%201%20lecture)
- [week 1 lecture 2](#week%201%20lecture%202)

## week 1 lecture 2

- datetime: 2025-02-06T13:30:00+08:00/2025-02-06T14:50:00+08:00
- [dot product](../../../../general/dot%20product.md)
  - dot product / algebraically ::@:: It is the sum of the products of the corresponding entries of the two sequences of numbers. Algebraic and geometric definitions are equivalent when using Cartesian coordinates.
  - dot product / geometrically ::@:: It is the product of the Euclidean magnitudes of the two vectors and the cosine of the angle between them. Algebraic and geometric definitions are equivalent when using Cartesian coordinates.
  - dot product / properties
    - dot product / properties / magnitude ::@:: $\vec v \cdot \vec v = \lvert \vec v \rvert^2$
    - dot product / properties / commutativity ::@:: $\vec v \cdot \vec w = \vec w \cdot \vec v$
    - dot product / properties / distributivity ::@:: $\vec u \cdot (\vec v + \vec w) = \vec u \cdot \vec v + \vec u \cdot \vec w \qquad (\vec u + \vec v) \cdot \vec w = \vec u \cdot \vec w + \vec v \cdot \vec w$
    - dot product / properties / homogeneity ::@:: $(c \vec u) \cdot \vec v = c (\vec u \cdot \vec v) = \vec u \cdot (c \vec v)$
- [polarization identity](../../../../general/polarization%20identity.md) ::@:: $2 \lVert \vec x \rVert^2 + 2 \lVert \vec y \rVert^2 = \lVert \vec x + \vec y \rVert^2 - \lVert \vec x - \vec y \rVert^2$
  - polarization identity / variant ::@:: $\langle \vec x, \vec y \rangle = \frac 1 4 \left(\lVert x + y \rVert^2 - \lVert x - y \rVert^2 \right)$
- [dot product](../../../../general/dot%20product.md)
  - dot product / cosine ::@:: $\cos \theta = \frac {\vec u \cdot \vec v} {\lVert \vec u \rVert \lVert \vec v \rVert}$
    - dot product / cosine / applications ::@:: inscribed triangle with diameter has a right angle, law of cosine/generalized Pythagoras theorem
  - dot product / projection ::@:: Project $\vec b$ onto $\vec a$: $\operatorname{proj}_{\vec a} \vec b = \frac {\vec a \cdot \vec b} {\vec a \cdot \vec a} \vec a$. $\frac {\vec a \cdot \vec b} {\vec a \cdot \vec a}$ can be interpreted as $\cos \theta$, where $\theta$ is the angle between them.
    - dot product / projection / scalar ::@:: It is simply the signed length of the projection, which is $\operatorname{comp}_{\vec a} \vec b = \frac {\vec a \cdot \vec b} {\lvert \vec a \rvert}$.
- [cross product](../../../../general/cross%20product.md) ::@:: Given two linearly independent vectors $\mathbf a$ and $\mathbf b$, the cross product, $\mathbf a \times \mathbf b$ (read "a cross b"), is a vector that is perpendicular to both $\mathbf a$ and $\mathbf b$, and thus normal to the plane containing them. <p> The magnitude of the cross product equals the area of a parallelogram with the vectors for sides; in particular, the magnitude of the product of two perpendicular vectors is the product of their lengths, i.e. $\lVert \mathbf a \rVert \lVert \mathbf b \rVert \sin \theta$, where $\theta$ is the angle between them.
  - cross product / properties
    - cross product / properties / anti-commutative ::@:: $\mathbf a \times \mathbf b = -\mathbf b \times \mathbf a$
    - cross product / properties / distributivity ::@:: $\mathbf a \times (\mathbf b + \mathbf c) = \mathbf a \times \mathbf b + \mathbf a \times \mathbf c \qquad (\mathbf a + \mathbf b) \times \mathbf c = \mathbf a \times \mathbf c + \mathbf b \times \mathbf c$
    - cross product / properties / zero element ::@:: $\mathbf a \times \mathbf 0 = \mathbf 0 \times \mathbf a = \mathbf 0$
    - cross product / properties / parallel ::@:: $\mathbf a \times \mathbf a = \mathbf 0$
  - cross product / calculation
    - cross product / calculation / element-wise ::@:: $\mathbf a \times \mathbf b = \langle a_2 b_3 - a_3 b_2, a_3 b_1 - a_1 b_3, a_1 b_2 - a_2 b_1 \rangle$
    - cross product / calculation / matrix determinant ::@:: $\mathbf a \times \mathbf b = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$

## week 2 lecture

- datetime: 2025-02-11T13:30:00+08:00/2025-02-11T14:50:00+08:00
- [cross product](../../../../general/cross%20product.md)
  - cross product / calculation
    - cross product / calculation / 3D basis ::@:: $\hat i \times \hat j = \hat k \qquad \hat j \times \hat k = \hat i \qquad \hat k \times \hat i = \hat j$
  - cross product / properties
    - cross product / properties / perpendicularity ::@:: $(\mathbf u \times \mathbf v) \cdot \mathbf u = (\mathbf u \times \mathbf v) \cdot \mathbf v = 0$
    - cross product / properties / parallelism ::@:: $\mathbf u \times \mathbf v = \mathbf 0$ iff the 2 vectors are parallel or at least 1 of them is $\mathbf 0$.
  - cross product / area and volume ::@:: $\lvert \mathbf u \times \mathbf v \rvert$ is the area of the parallelogram formed by the 2 vectors. $\lvert \mathbf u \cdot (\mathbf v \times \mathbf w) \rvert$ is the volume of the parallelepiped (analogy of parallelogram to 3D space) formed by the 3 vectors.
- [parametric equation](../../../../general/parmetric%20equation.md) ::@:: It expresses several quantities, such as the coordinates of a point, as functions of one or several variables called parameters. <p> We consider there are exactly 1 parameter, in which case the equation describes a curve (it need not be a line).
  - parametric equation / notation ::@:: For example, to describe a curve in 3D space, we have several ways: $$\begin{aligned} \gamma(t) & = (x(t), y(t), z(t)) \\ & \begin{cases} x(t) = \text{function of }t \\ y(t) = \text{function of }t \\ z(t) = \text{function of }t \end{cases} \\ & \begin{cases} x = \text{function of }t \\ y = \text{function of }t \\ z = \text{function of }t \end{cases} \end{aligned}$$
  - parametric equation / construction
    - parametric equation / construction / line through a point parallel to a vector ::@:: If the point is $(x_0, y_0, z_0)$ and the vector is $\langle a, b, c \rangle$, then $\gamma(t) = (x_0, y_0, z_0) + t (a, b, c) = (x_0 + at, y_0 + bt, z_0 + ct)$. <p> We notice that actually, as long as the multiplication factor ($t$ in this context) has a domain of $\mathbb R$ and are the same for $a, b, c$, the equation describes the same line. So we can replace $t$ with $2t$, but not $0t$ or $t^2$.
  - parametric equation / non-uniqueness ::@:: Different equations can represent the same curve. <p> The simplest would be to replace $t$ by $\alpha t$, where $\alpha$ is a nonzero real number. The curve is the same but we can think of it as $t$ going "faster" or "slower" along the curve.

## week 2 tutorial

- datetime: 2025-02-11T16:00:00+08:00/2025-02-11T16:50:00+08:00
- [week 2 lecture](#week%202%20lecture)
- [week 2 lecture 2](#week%202%20lecture%202)

## week 2 lecture 2

- datetime: 2025-02-13T13:30:00+08:00/2025-02-13T14:50:00+08:00
- parametric equation
  - parametric equation / symmetric equation ::@:: Solve for $t$ in the parametric equation $\gamma(t) = (x_0 + at, y_0 + bt, z_0 + ct)$ to get this form: $$\frac {x - x_0} a = \frac {y - y_0} b = \frac {z - z_0} c \,.$$ Note that if one or more of $a$, $b$, or $c$ is 0, it means the curve does not change in coordinate for said axes. In that case, we simply have resp. $x = x_0$, $y = y_0$, $z = z_0$.
- [line](../../../../general/line%20(geometry).md) ::@:: an infinitely long object with no width, depth, or curvature, an idealization of such physical objects as a straightedge, a taut string, or a ray of light
  - line / relations with other lines ::@:: same: same line <br/> intersect: two _distinct_ lines intersecting at one point (they must be in the same plane) <br/> parallel: two _distinct_ lines in the same plane (always true for 2D space) and does not intersect <br/> skew: two _distinct_ lines not in the same plane (always false for 2D space) and does not intersect
    - line / relations with other lines / checking ::@:: Check direction first. If the same direction, if they intersect then same line, otherwise parallel lines. If not the same direction, if they intersect, then intersect, otherwise skew.
- [Euclidean plane](../../../../general/Euclidean%20plane.md) ::@:: A Euclidean space of dimension two. In 3D space, it can be described by a point it passes through and its _nonzero_ normal vector (which reduces the dimensionality by 1).
  - Euclidean plane / equation ::@:: Given a point $(x_0, y_0, z_0)$ and a _nonzero_ normal vector $\langle a, b, c \rangle$, the plane described has the equation: $$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$ which is more commonly written as $$ax + by + cz - d = 0 \,.$$ You can think of _d_ as the _signed_ (positive in the direction of the normal vector) distance of the plane from the origin scaled by the normal vector length. <p> Conversely, any equation in the above form, where $a, b, c$ are not all zero, describes a plane. <p> (You can also describe it using linear algebra.)
- [Hesse normal form](../../../../general/Hesse%20normal%20form.md) ::@:: It describes a _n_−1 Euclidean space in a _n_-dimensional space. For 3D space, it describes a plane.
  - Hesse normal form / expression ::@:: It is written in vector notation as $${\vec {r} }\cdot {\vec {n} }_{0}-d=0.\,$$ The dot $\cdot$ indicates the [dot product](../../../../general/dot%20product.md) \(or scalar product\). Vector ${\vec {r} }$ points from the origin of the coordinate system, _O_, to any point _P_ that lies precisely in plane or on line _E_. The vector ${\vec {n} }_{0}$ represents the [unit](../../../../general/unit%20vector.md) [normal vector](../../../../general/normal%20vector.md) of plane or line _E_. The distance $d$ is the shortest _signed_ (positive in the direction of $\vec n_0$) distance from the origin _O_ to the plane or line.
- Euclidean plane
  - Euclidean plane / cross product ::@:: In 3D space, we can find the plane two non-parallel vectors lie in. Find the cross product of the two vectors. Then the resulting vector is a normal vector of the plane.
  - Euclidean plane / angle between two planes ::@:: The angle is the same as the angle between their two normal vectors. So you can use dot product (and cross product if in 3D space) to find it.
  - Euclidean plane / relations with other planes ::@:: same: same plane <br/> intersect: _distinct_ planes that intersect at a line <br/> parallel: _distinct_ planes that do not intersect
    - Euclidean plane / relations with other planes / checking ::@:: Check if their normal vectors are parallel. If so, they are either the same or parallel. Otherwise, they are intersect.
  - Euclidean plane / distance to a point ::@:: This is the length of the line connecting the point to the plane parallel to the plane normal vector.
    - Euclidean plane / distance to a point / intuition ::@:: Consider the plane equation $ax + by + cz - d = 0$. In particular, the left hand side without $d$ is the component of $\langle x, y, z \rangle$ in the normal vector direction, scaled by the length of the normal vector. The $d$ represents the _signed_ (positive in the direction of the normal vector) distance of the plane from the origin scaled by the normal vector length. So the entire left hand side is the _signed_ distance from the plane to the point $(x, y, z)$. <p> So clearly, the (_unsigned_) distance to the point $(x, y, z)$ is: $$\text{distance} = \frac {\lvert ax + by + cz - d \rvert} {\sqrt {a^2 + b^2 + c^2} } \,.$$ <p> If you use the Hesse normal form, since the normal vector is normalized, the denominator (length of the normal vector) is 1 and can be omitted.
    - Euclidean plane / distance to a point / derivation ::@:: Consider the plane equation $ax + by + cz - d = 0$. Find its distance to $P_0 = (x_0, y_0, z_0)$. <p> Consider any point on the plane $P_1 = (x_1, y_1, z_1)$. Construct the vector $\overrightarrow{P_1 P_0}$. The distance is the component of the vector in the normal vector $\langle a, b, c \rangle$ direction. So we have $$\text{distance} = \left\lvert \frac {a(x_0 - x_1) + b(y_0 - y_1) + c(z_0 - z_1)} {\sqrt{a^2 + b^2 + c^2} } \right\rvert = \frac {\lvert a x_0 + b y_0 + c z_0 - d \rvert} {\sqrt{a^2 + b^2 + c^2} } \,.$$ <p> The above derivation also applies to higher dimensions for hyperplanes.

## week 3 lecture

- datetime: 2025-02-18T13:30:00+08:00/2025-02-18T14:50:00+08:00
- parametric equation
  - parametric equation / parametric curve ::@:: A curve described by a parametric equation: $\gamma : A \to \mathbb R^n$, where $A \subseteq \mathbb R$.
    - parametric equation / parametric curve / circle ::@:: $$(x, y) = (x_0 + r \cos at, y_0 + r \sin at)$$, where $(x_0, y_0)$ is the center, $r$ is the radius, $a \ne 0$ is "the rate of running along the shape".
    - parametric equation / parametric curve / graph of a function ::@:: $$(x, y) = (t, f(t))$$, where $f$ is a function.
    - parametric equation / parametric curve / cycloid ::@:: Consider the cycloid through the origin, generated by a circle of radius _r_ rolling over the _x_-axis on the positive side (_y_ ≥ 0). <p> To derive the equation, consider the circle that is not rolling: $\gamma'(\theta) = (r \sin \theta, r(1 - \cos \theta))$. Then consider that the circle rolls to the right by $r \, \mathrm d\theta$ per $\mathrm d\theta$ (compare when $\theta = 0$ and $\theta = 2\pi$). So we have: $$\gamma(\theta) = (r(\theta - \sin \theta), r(1- \cos \theta))$$.
- [cycloid](../../../../general/cycloid.md) ::@:: the curve traced by a point on a circle as it rolls along a straight line without slipping
- [parametric derivative](../../../../general/parametric%20derivative.md) ::@:: It is a derivative of a dependent variable with respect to another dependent variable that is taken when both variables depend on an independent third variable, usually thought of as "time" (that is, when the dependent variables are _x_ and _y_ and are given by parametric equations in _t_).
  - parametric derivative / intuition ::@:: Recall we can consider changing $t$ as running along the curve. Then its parametric derivative is the velocity (vector) of running.
  - parametric derivative / slope ::@:: To extract the slope for a curve on 2D, use $y'(t) / x'(t)$.
    - parametric derivative / slope / indeterminate slope ::@::  Note that the slope as defined above may be indeterminate, e.g. when $x'(t) = y'(t) = 0$. That does not necessarily mean that slope is undefined there (sometimes it really is undefined though, e.g. sharp corners). <p> In said cases, we can try to compute $\lim_{\tau \to t} \frac {y'(\tau)} {x'(\tau)}$, and maybe make use of the L'Hoptial rule if needed.
    - parametric derivative / slope / horizontal slope ::@:: Find $t$ for which $x'(t) \ne 0$ and $y'(t) = 0$. Also check if there are indeterminate slopes and see if they are actually also horizontal.
    - parametric derivative / slope / vertical slope ::@:: Find $t$ for which $x'(t) = 0$ and $y'(t) \ne 0$. Also check if there are indeterminate slopes and see if they are actually also vertical.
- [function of several real variables](../../../../general/function%20of%20several%20real%20variables.md) (multivariable functions) ::@:: It is a function with more than one argument, with all arguments being real variables. <p> In this course, we study real-valued functions, i.e. the codomain is also real.
  - function of several real variables / domain ::@:: The [domain](../../../../general/domain%20of%20a%20function.md) of a function of _n_ variables is the [subset](../../../../general/subset.md) of ⁠$\mathbb {R} ^{n}$⁠ for which the function is defined. As usual, the domain of a function of several real variables is supposed to contain a nonempty [open](../../../../general/open%20set.md) subset of ⁠$\mathbb {R} ^{n}$⁠. <p> When the domain is not specified, it is usually implicitly understood as the largest subset that makes the function defined.
  - function of several real variables / graph ::@:: For _n_ real arguments, we can visualize it in a _n_+1-dimensional space. It also satisfies the vertical line test. <p> For example, when _n_ = 1, we get the graph of a function in 2D. When _n_ = 2, we get a surface in 3D satisfying the vertical line test. When _n_ = 3, we need to visualize in 4D, and good luck with that!
- [level set](../../../../general/level%20set.md) ::@:: It of a [real-valued function](../../../../general/real-valued%20function.md) _f_ of _n_ [real variables](../../../../general/function%20of%20several%20real%20variables.md) is a [set](../../../../general/set%20(mathematics).md) where the function takes on a given [constant](../../../../general/constant%20(mathematics).md) value _c_, that is: $$L_{c}(f)=\left\{(x_{1},\ldots ,x_{n})\mid f(x_{1},\ldots ,x_{n})=c\right\}~.$$
  - level set / names ::@:: It depends on the number of independent variables to the function. If 2, it is also called a _level curve_. If 3, it is also called a _level surface_. If more than 3, it is also called a _level hypersurface_.
  - level set / visualization ::@:: It can be visualized using _contour lines_ for functions of 2 independent variables. <p> Note that a level curve (_n_ = 2) does not always have to be a curve: it could be a point or a surface. Similarly, a level surface (_n_ = 3) does not always have to be a surface.
  - level set / interpretations ::@:: It is the preimage of the function over $c$. It is also the intersection of the graph of the function with the (hyper)plane $y = c$. <p> Further, if $f$ is _differentiable_, then the gradient of $f$ at a point is either zero, or _perpendicular_ to the level set of $f$ at that point.
- reading: [cycloid](../../../../general/cycloid.md)

## week 3 tutorial

- datetime: 2025-02-18T16:00:00+08:00/2025-02-18T16:50:00+08:00
- [week 3 lecture](#week%203%20lecture)
- [week 3 lecture 2](#week%203%20lecture%202)

## assignments

## midterm examination

## final examination

## aftermath

### total
