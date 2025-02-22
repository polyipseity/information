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
- [function](../../../../general/function%20(mathematics).md) ::@:: image, pre-image, graph of a function, continuity <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - function / image ::@:: It of an input value $x$ is the single output value produced by $f$ when passed $x$. It of a set of input values $X$ is the set of output values produced by $f$ when passed each value of $X$. <!--SR:!2025-02-26,14,290!2025-02-23,12,270-->
  - function / pre-image ::@:: It of an output value $y$ is the set of input values that produce $y$ when passed to $f$. It of a set of output values $Y$ is the set of input values that produce any value in $Y$ when passed to $f$. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - function / graph of a function ::@:: The set of points $(x, f(x))$ for all $x$ in the domain of $f$ on the 2D Cartesian plane. <p> Not all set of points $(x, y)$ is the graph of a function. Use the vertical line test: If any vertical line pass through at most one point in the set, then the graph is a function. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - function / [continuity](../../../../general/continuous%20function.md) ::@:: The limit of the function at each input value equals the function evaluated at that value. (Some special cases regarding domain boundaries have been omitted here...) <!--SR:!2025-02-24,12,270!2025-02-26,14,290-->
- [calculus](../../../../general/calculus.md) ::@:: rate of change, differentiation, integration, fundamental theorem of calculus <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - calculus / [differentiation](../../../../general/derivative.md) ::@:: Definition: $$f'(x) = \lim_{\delta \to 0} \frac {f(x + \delta) - f(x)} {\delta} \,$$ if it exists. But in practice, we apply some rules. <p> Related to the rate of change. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - calculus / [integration](../../../../general/integral.md) ::@:: Inverse operation to differentiation. <p> Related to area under the curve. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - calculus / [fundamental theorem of calculus](../../../../general/fundamental%20theorem%20of%20calculus.md) ::@:: There are 2 parts. It relates a function to its antiderivatives. <p> The first part: We have a continuous function $f$. Then we can define a function as the definite integral of $f$ from $a$ to $x$. The function is an antiderivative of $f$. <p> The second part: We have a Riemann integrable function $f$. We also have a function $F$ that is the antiderivaive of $f$. Then the definite integral of $f$ from $a$ to $b$ is $F(b) - F(a)$. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- function
  - function / extension in this course ::@:: We will study functions with multiple inputs and/or multiple outputs. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [function of several real variables](../../../../general/function%20of%20a%20several%20real%20variables.md) ::@:: In general, $$\mathbb R^n \to X \,.$$ <p> For this course in particular, we will focus on $X = \mathbb R^m$. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [Cartesian coordinate system](../../../../general/Cartesian%20coordinate%20system.md) ::@:: A coordinate system that specifies each point uniquely by a pair of real numbers called _coordinates_, which are the signed distances to the point from two fixed perpendicular oriented lines, called _coordinate lines_, _coordinate axes_ or just _axes_ (plural of _axis_) of the system. <!--SR:!2025-02-23,12,270!2025-03-31,38,290-->
  - Cartesian coordinate system / dimension ::@:: number of points to describe a point <!--SR:!2025-04-06,43,290!2025-02-26,14,290-->
  - Cartesian coordinate system / symbols ::@:: Using real numbers, $\mathbb R^n$, where $n$ is the dimension of the entire space. <!--SR:!2025-02-26,14,290!2025-04-01,39,290-->
  - Cartesian coordinate system / orientation ::@:: left-hand side, right-hand side; by most convention (including this course), we use right-hand side <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Cartesian coordinate system / shape description ::@:: Equations can describe a subset of points of the entire space. Intersection and/or union may be used to define shapes defined by multiple equations. <p> For example: $x^2 + y^2 + z^2 = r^2$ is a 3D sphere of radius $r$. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Cartesian coordinate system / projection ::@:: Orthogonal project may be used to extract a specific coordinate of a point. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [Euclidean vector](../../../../general/Euclidean%20vector.md) ::@:: A set whose elements, often called _vectors_, can be added together and multiplied ("scaled") by numbers called _scalars_. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / vector ::@:: A line segment with a direction, up to translation. That is, two vectors are the same if they have the same length and direction. <p> The zero vector has 0 length and no direction. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / scalar ::@:: A real number. In general, the field associated with the vector space. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / position vector ::@:: A vector used to represent the position of a point. <p> For example, in 3D space, the point $(x, y, z)$ can be represented by the position vector $\langle x, y, z \rangle$ (note the angle brackets). <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / element-wise operations ::@:: vector addition, vector subtraction: perform the operation on each coordinate separately to get the resulting vector <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / scalar multiplication ::@:: multiply each coordinate by the specified scalar to get the resulting vector <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - Euclidean vector / magnitude or length ::@:: The square root of the sum of the squared coordinates. This is a specific case of the _p_-norm. <p> For example, the vector $\vec v = \langle x, y, z \rangle$ has the magnitude $\lvert \vec v \rvert = \sqrt{x^2 + y^2 + z^2}$. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [unit vector](../../../../general/unit%20vector.md) ::@:: A vector of magnitude 1. The unit vector associated with an arbitrary vector $\vec v$ is $\vec v / \lvert \vec v \rvert$. The zero vector has no unit vector, as it has no direction. <p> For example, in 3D space, the unit vectors along the coordinate axes (and their notations): $\vec i = \langle 1, 0, 0 \rangle, \vec j = \langle 0, 1, 0 \rangle, \vec k = \langle 0, 0, 1 \rangle$. These 3 unit vectors form is _an_ (not _the_) orthonormal basis of the 3D space. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [orthonormal basis](../../../../general/orthonormal%20basis.md) ::@:: The set of unit vectors along the coordinate axes form an orthonormal basis. This means any vector can be _uniquely_ written as a linear combination of the orthonormal basis. <p> For example, in 3D space, each vector $\vec v$ can be written uniquely as $\vec v = x \vec i + y \vec j + z \vec k$, where $x, y, z$ are scalars. <!--SR:!2025-02-24,12,270!2025-02-26,14,290-->

## week 1 tutorial

- datetime: 2025-02-04T16:00:00+08:00/2025-02-04T16:50:00+08:00
- [week 1 lecture 2](#week%201%20lecture%202)

## week 1 lecture 2

- datetime: 2025-02-06T13:30:00+08:00/2025-02-06T14:50:00+08:00
- [dot product](../../../../general/dot%20product.md)
  - dot product / algebraically ::@:: It is the sum of the products of the corresponding entries of the two sequences of numbers. Algebraic and geometric definitions are equivalent when using Cartesian coordinates. <!--SR:!2025-03-07,18,327!2025-02-28,11,307-->
  - dot product / geometrically ::@:: It is the product of the Euclidean magnitudes of the two vectors and the cosine of the angle between them. Algebraic and geometric definitions are equivalent when using Cartesian coordinates. <!--SR:!2025-03-07,18,327!2025-02-28,11,307-->
  - dot product / properties
    - dot product / properties / magnitude ::@:: $\vec v \cdot \vec v = \lvert \vec v \rvert^2$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - dot product / properties / commutativity ::@:: $\vec v \cdot \vec w = \vec w \cdot \vec v$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - dot product / properties / distributivity ::@:: $\vec u \cdot (\vec v + \vec w) = \vec u \cdot \vec v + \vec u \cdot \vec w \qquad (\vec u + \vec v) \cdot \vec w = \vec u \cdot \vec w + \vec v \cdot \vec w$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - dot product / properties / homogeneity ::@:: $(c \vec u) \cdot \vec v = c (\vec u \cdot \vec v) = \vec u \cdot (c \vec v)$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
- [polarization identity](../../../../general/polarization%20identity.md) ::@:: $2 \lVert \vec x \rVert^2 + 2 \lVert \vec y \rVert^2 = \lVert \vec x + \vec y \rVert^2 - \lVert \vec x - \vec y \rVert^2$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
  - polarization identity / variant ::@:: $\langle \vec x, \vec y \rangle = \frac 1 4 \left(\lVert x + y \rVert^2 - \lVert x - y \rVert^2 \right)$ <!--SR:!2025-03-07,18,327!2025-03-07,18,326-->
- [dot product](../../../../general/dot%20product.md)
  - dot product / cosine ::@:: $\cos \theta = \frac {\vec u \cdot \vec v} {\lVert \vec u \rVert \lVert \vec v \rVert}$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - dot product / cosine / applications ::@:: inscribed triangle with diameter has a right angle, law of cosine/generalized Pythagoras theorem <!--SR:!2025-03-07,18,327!2025-02-28,11,307-->
  - dot product / projection ::@:: Project $\vec b$ onto $\vec a$: $\operatorname{proj}_{\vec a} \vec b = \frac {\vec a \cdot \vec b} {\vec a \cdot \vec a} \vec a$. $\frac {\vec a \cdot \vec b} {\vec a \cdot \vec a}$ can be interpreted as $\cos \theta$, where $\theta$ is the angle between them. <!--SR:!2025-02-28,11,307!2025-03-07,18,327-->
    - dot product / projection / scalar ::@:: It is simply the signed length of the projection, which is $\operatorname{comp}_{\vec a} \vec b = \frac {\vec a \cdot \vec b} {\lvert \vec a \rvert}$. <!--SR:!2025-03-07,18,326!2025-03-07,18,327-->
- [cross product](../../../../general/cross%20product.md) ::@:: Given two linearly independent vectors $\mathbf a$ and $\mathbf b$, the cross product, $\mathbf a \times \mathbf b$ (read "a cross b"), is a vector that is perpendicular to both $\mathbf a$ and $\mathbf b$, and thus normal to the plane containing them. <p> The magnitude of the cross product equals the area of a parallelogram with the vectors for sides; in particular, the magnitude of the product of two perpendicular vectors is the product of their lengths, i.e. $\lVert \mathbf a \rVert \lVert \mathbf b \rVert \sin \theta$, where $\theta$ is the angle between them. <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
  - cross product / properties
    - cross product / properties / anti-commutative ::@:: $\mathbf a \times \mathbf b = -\mathbf b \times \mathbf a$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - cross product / properties / distributivity ::@:: $\mathbf a \times (\mathbf b + \mathbf c) = \mathbf a \times \mathbf b + \mathbf a \times \mathbf c \qquad (\mathbf a + \mathbf b) \times \mathbf c = \mathbf a \times \mathbf c + \mathbf b \times \mathbf c$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - cross product / properties / zero element ::@:: $\mathbf a \times \mathbf 0 = \mathbf 0 \times \mathbf a = \mathbf 0$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
    - cross product / properties / parallel ::@:: $\mathbf a \times \mathbf a = \mathbf 0$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->
  - cross product / calculation
    - cross product / calculation / element-wise ::@:: $\mathbf a \times \mathbf b = \langle a_2 b_3 - a_3 b_2, a_3 b_1 - a_1 b_3, a_1 b_2 - a_2 b_1 \rangle$ <!--SR:!2025-02-28,11,306!2025-03-07,18,327-->
    - cross product / calculation / matrix determinant ::@:: $\mathbf a \times \mathbf b = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$ <!--SR:!2025-03-07,18,327!2025-03-07,18,327-->

## week 2 lecture

- datetime: 2025-02-11T13:30:00+08:00/2025-02-11T14:50:00+08:00
- [cross product](../../../../general/cross%20product.md)
  - cross product / calculation
    - cross product / calculation / 3D basis ::@:: $\hat i \times \hat j = \hat k \qquad \hat j \times \hat k = \hat i \qquad \hat k \times \hat i = \hat j$ <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
  - cross product / properties
    - cross product / properties / perpendicularity ::@:: $(\mathbf u \times \mathbf v) \cdot \mathbf u = (\mathbf u \times \mathbf v) \cdot \mathbf v = 0$ <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
    - cross product / properties / parallelism ::@:: $\mathbf u \times \mathbf v = \mathbf 0$ iff the 2 vectors are parallel or at least 1 of them is $\mathbf 0$. <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
  - cross product / area and volume ::@:: $\lvert \mathbf u \times \mathbf v \rvert$ is the area of the parallelogram formed by the 2 vectors. $\lvert \mathbf u \cdot (\mathbf v \times \mathbf w) \rvert$ is the volume of the parallelepiped (analogy of parallelogram to 3D space) formed by the 3 vectors. <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
- [parametric equation](../../../../general/parmetric%20equation.md)  ::@:: It expresses several quantities, such as the coordinates of a point, as functions of one or several variables called parameters. <p> We consider there are exactly 1 parameter, in which case the equation describes a curve (it need not be a line). <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
  - parametric equation / notation ::@:: For example, to describe a curve in 3D space, we have several ways: $$\begin{aligned} \gamma(t) & = (x(t), y(t), z(t)) \\ & \begin{cases} x(t) = \text{function of }t \\ y(t) = \text{function of }t \\ z(t) = \text{function of }t \end{cases} \\ & \begin{cases} x = \text{function of }t \\ y = \text{function of }t \\ z = \text{function of }t \end{cases} \end{aligned}$$ <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
  - parametric equation / construction
    - parametric equation / construction / line through a point parallel to a vector ::@:: If the point is $(x_0, y_0, z_0)$ and the vector is $\langle a, b, c \rangle$, then $\gamma(t) = (x_0, y_0, z_0) + t (a, b, c) = (x_0 + at, y_0 + bt, z_0 + ct)$. <p> We notice that actually, as long as the multiplication factor ($t$ in this context) has a domain of $\mathbb R$ and are the same for $a, b, c$, the equation describes the same line. So we can replace $t$ with $2t$, but not $0t$ or $t^2$. <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->
  - parametric equation / non-uniqueness ::@:: Different equations can represent the same curve. <p> The simplest would be to replace $t$ by $\alpha t$, where $\alpha$ is a nonzero real number. The curve is the same but we can think of it as $t$ going "faster" or "slower" along the curve. <!--SR:!2025-02-23,4,323!2025-02-23,4,323-->

## week 2 tutorial

- datetime: 2025-02-11T16:00:00+08:00/2025-02-11T16:50:00+08:00
- [week 2 lecture](#week%202%20lecture)
- [week 2 lecture 2](#week%202%20lecture%202)

## assignments

## midterm examination

## final examination

## aftermath

### total
