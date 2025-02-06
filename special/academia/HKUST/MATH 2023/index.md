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
- [week 1 lecture 2](#week%201%20lecture%202)

## week 1 lecture 2

## assignments

## midterm examination

## final examination

## aftermath

### total
