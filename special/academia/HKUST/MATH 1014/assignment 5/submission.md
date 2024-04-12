---
aliases:
  - HKUST MATH 1014 L1 assignment 4 submission
tags:
  - date/2024/04/12
  - language/in/English
---

# HKUST MATH 1014 L1 assignment 5 submission

MATH1014 Calculus II Problem Set 5<br/>
L01 (Spring 2024)

Problem Set 5

Note: The problem sets serve as additional exercise problems for your own practice. Problem Set 5 covers materials from §7.1 – §7.6.

## Q5

Let $\mathbf{u}$ and $\mathbf{v}$ be two vectors <span style="color: red;">in</span> $\textcolor {red} {\mathbb{R}^3}$ such that $\lVert \mathbf{u} \rVert = 4$, $\lVert \mathbf{v} \rVert = 3$, and the angle between $\mathbf{u}$ and $\mathbf{v}$ is $\frac \pi 3$.

### Q5.a

Find $\mathbf{u} \cdot \mathbf{v}$.

> $$\begin{aligned}
> & \phantom{=} \mathbf{u} \cdot \mathbf{v} \\
> & = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos \frac \pi 3 \\
> & = 4 \cdot 3 \cdot \frac 1 2 \\
> & = 6
> \end{aligned}$$

### Q5.b

Find the real number $k$ such that the vectors $\mathbf{u} + k \mathbf{v}$ and $\mathbf{u} - 2 \mathbf{v}$ are orthogonal.

> $$\begin{aligned}
> & \text{Set the dot product of the vectors to 0.} \\
> & \begin{aligned} (\mathbf{u} + k \mathbf{v}) \cdot (\mathbf{u} - 2 \mathbf{v}) & = 0 \\
> \mathbf{u} \cdot \mathbf{u} - 2 \mathbf{u} \cdot \mathbf{v} + k \mathbf{v} \cdot \mathbf{u} - 2k \mathbf{v} \cdot \mathbf{v} & = 0 \\
> \lVert \mathbf{u} \rVert^2 + (k - 2) \mathbf{u} \cdot \mathbf{v} - 2k \lVert \mathbf{v} \rVert^2 & = 0 \\
> 4^2 + (k - 2) 6 - 2k \cdot 3^2 & = 0 \\
> 16 + 6k - 12 - 18k & = 0 \\
> -12k & = -4 \\
> k & = \frac 1 3 \end{aligned}
> \end{aligned}$$

### Q5.c

Let $\mathbf{a} = 3 \mathbf{u} + 4 \mathbf{v}$ and $\mathbf{b} = -2 \mathbf{u} - \mathbf{v}$. Find the area of the parallelogram with $\mathbf{a}$ and $\mathbf{b}$ as two adjacent edges.

> $$\begin{aligned}
> & \phantom{=} \lVert \mathbf{a} \rVert^2 \\
> & = \mathbf{a} \cdot \mathbf{a} \\
> & = (3 \mathbf{u} + 4 \mathbf{v}) \cdot (3 \mathbf{u} + 4 \mathbf{v}) \\
> & = 9 \lVert \mathbf{u} \rVert^2 + 24 \mathbf{u} \cdot \mathbf{v} + 16 \lVert \mathbf{v} \rVert^2 \\
> & = 9 \cdot 4^2 + 24 \cdot 6 + 16 \cdot 3^2 \\
> & = 144 + 144 + 144 \\
> & = 432 \\
> & \phantom{=} \lVert \mathbf{b} \rVert^2 \\
> & = \mathbf{b} \cdot \mathbf{b} \\
> & = (-2 \mathbf{u} - \mathbf{v}) \cdot (-2 \mathbf{u} - \mathbf{v}) \\
> & = 4 \lVert \mathbf{u} \rVert^2 + 4 \mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert^2 \\
> & = 4 \cdot 4^2 + 4 \cdot 6 + 3^2 \\
> & = 64 + 24 + 9 \\
> & = 97 \\
> & \phantom{=} \mathbf{a} \cdot \mathbf{b} \\
> & = (3 \mathbf{u} + 4 \mathbf{v}) \cdot (-2 \mathbf{u} - \mathbf{v}) \\
> & = -6 \mathbf{u} \cdot \mathbf{u} - 3 \mathbf{u} \cdot \mathbf{v} - 8 \mathbf{v} \cdot \mathbf{u} - 4 \mathbf{v} \cdot \mathbf{v} \\
> & = -6 \lVert \mathbf{u} \rVert^2 - 11 \mathbf{u} \cdot \mathbf{v} - 4 \lVert \mathbf{v} \rVert^2 \\
> & = - 6 \cdot 4^2 - 11 \cdot 6 - 4 \cdot 3^2 \\
> & = -96 - 66 - 36 \\
> & = -198 \\
> \\
> & \text{Let }\theta\text{ be the angle between }\mathbf{a}\text{ and }\mathbf{b}\text{.} \\
> & \phantom{=} \text{area} \\
> & = \lVert \mathbf{a} \times \mathbf{b} \rVert \\
> & = \sqrt{ \lVert \mathbf{a} \times \mathbf{b} \rVert^2 } \\
> & = \sqrt{ \lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 \sin^2 \theta } \\
> & = \sqrt{ \lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 \left(1 - \cos^2 \theta\right) } \\
> & = \sqrt{ \lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2 } \\
> & = \sqrt{432 \cdot 97 - 198^2} \\
> & = \sqrt{41904 - 39204} \\
> & = \sqrt{2700} \\
> & = 30\sqrt{3}
> \end{aligned}$$

## Q9

Let $\mathbf{u}$ and $\mathbf{v}$ be non-zero vectors of the same dimension. Show that the vector $$\mathbf{w} = \lVert \mathbf{u} \rVert \mathbf{v} + \lVert \mathbf{v} \rVert \mathbf{u}$$ bisects the angle between $\mathbf{u}$ and $\mathbf{v}$.

> $$\begin{aligned}
> & \text{Let }\theta \in [0, \pi]\text{ be the angle between }\mathbf{u}\text{ and }\mathbf{w}\text{.} \\
> & \begin{aligned} \mathbf{u} \cdot \mathbf{w} & = \lVert \mathbf{u} \rVert \lVert \mathbf{w} \rVert \cos\theta \\
> \lVert \mathbf{u} \rVert \mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert \lVert \mathbf{u} \rVert^2 & = \lVert \mathbf{u} \rVert \lVert \mathbf{w} \rVert \cos\theta \\
> \cos\theta & = \frac {\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert} {\lVert \mathbf{w} \rVert} \end{aligned} \\
> & \text{Let }\phi \in [0, \pi]\text{ be the angle between }\mathbf{v}\text{ and }\mathbf{w}\text{.} \\
> & \begin{aligned} \mathbf{v} \cdot \mathbf{w} & = \lVert \mathbf{v} \rVert \lVert \mathbf{w} \rVert \cos \phi \\
> \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert^2 + \lVert \mathbf{v} \rVert \mathbf{u} \cdot \mathbf{v} & = \lVert \mathbf{v} \rVert \lVert \mathbf{w} \rVert \cos \phi \\
> \cos \phi & = \frac {\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert + \mathbf{u} \cdot \mathbf{v} } {\lVert \mathbf{w} \rVert} \\
> & = \cos \theta \\
> \phi & = \theta && (\cos(*)\text{ is injective on }[0, \pi]) \end{aligned} \\
> & \therefore \mathbf{w}\text{ bisects the angle between }\mathbf{u}\text{ and }\mathbf{v}\text{.}
> \end{aligned}$$

## Q11

Let $\mathbf{a}$ and $\mathbf{b}$ be vectors in $\mathbb{R}^n$ suchh that $$\mathbf{a} \cdot \mathbf{a} = 1, \mathbf{b} \cdot \mathbf{b} = 1\text{ and }\mathbf{a} \cdot \mathbf{b} = 0$$.

Let $S = \set{\mathbf{u} \in \mathbb{R}^n : \mathbf{u} = x \mathbf{a} + y \mathbf{b}\text{ for some }x, y \in \mathbb{R} }$.

### Q11.a

Show that for every $\mathbf{u} \in S$, we have $$\mathbf{u} = (\mathbf{u} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{u} \cdot \mathbf{b}) \mathbf{b}$$.

> $$\begin{aligned}
> & \phantom{=} (\mathbf{u} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{u} \cdot \mathbf{b}) \mathbf{b} \\
> & = ((x \mathbf{a} + y \mathbf{b}) \cdot \mathbf{a}) \mathbf{a} + ((x \mathbf{a} + y \mathbf{b}) \cdot \mathbf{b}) \mathbf{b} \\
> & = (x \mathbf{a} \cdot \mathbf{a} + y \mathbf{b} \cdot \mathbf{a}) \mathbf{a} + (x \mathbf{a} \cdot \mathbf{b} + y \mathbf{b} \cdot \mathbf{b}) \mathbf{b} \\
> & = (x + 0) \mathbf{a} + (0 + y) \mathbf{b} \\
> & = x \mathbf{a} + y \mathbf{b} \\
> & = \mathbf{u} \\
> \end{aligned}$$

### Q11.b

For each $\mathbf{v} \in \mathbb{R}^n$, let $\mathbf{w} = (\mathbf{v} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{v} \cdot \mathbf{b}) \mathbf{b}$. Show that $\mathbf{v} - \mathbf{w}$ is orthogonal to every $\mathbf{u} \in S$.

> $$\begin{aligned}
> & \phantom{=} (\mathbf{v} - \mathbf{w}) \cdot \mathbf{u} \\
> & = \mathbf{v} \cdot \mathbf{u} - \mathbf{w} \cdot \mathbf{u} \\
> & = \mathbf{v} \cdot \mathbf{u} - ((\mathbf{v} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{v} \cdot \mathbf{b}) \mathbf{b}) \cdot ((\mathbf{u} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{u} \cdot \mathbf{b}) \mathbf{b}) \\
> & = \mathbf{v} \cdot \mathbf{u} - (\mathbf{v} \cdot \mathbf{a}) (\mathbf{u} \cdot \mathbf{a}) \mathbf{a} \cdot \mathbf{a} - (\mathbf{v} \cdot \mathbf{a}) (\mathbf{u} \cdot \mathbf{b}) \mathbf{a} \cdot \mathbf{b} \\
> & \phantom{=} - (\mathbf{v} \cdot \mathbf{b}) (\mathbf{u} \cdot \mathbf{a}) \mathbf{b} \cdot \mathbf{a} - (\mathbf{v} \cdot \mathbf{b}) (\mathbf{u} \cdot \mathbf{b}) \mathbf{b} \cdot \mathbf{b} \\
> & = \mathbf{v} \cdot \mathbf{u} - (\mathbf{v} \cdot \mathbf{a}) (\mathbf{u} \cdot \mathbf{a}) - (\mathbf{v} \cdot \mathbf{b}) (\mathbf{u} \cdot \mathbf{b}) \\
> & = \mathbf{v} \cdot \mathbf{u} - \mathbf{v} \cdot ((\mathbf{u} \cdot \mathbf{a}) \mathbf{a} + (\mathbf{u} \cdot \mathbf{b}) \mathbf{b}) \\
> & = \mathbf{v} \cdot \mathbf{u} - \mathbf{v} \cdot \mathbf{u} \\
> & = 0 \\
> & \phantom \implies (\mathbf{v} - \mathbf{w}) \cdot \mathbf{u} = 0 \\
> & \implies \mathbf{v} - \mathbf{w} \perp \mathbf{u}
> \end{aligned}$$

## Q16

Three lines are said to be ___concurrent___ if they pass through the same point.

### Q16.a

A __median__ of a triangle is a line that passes through both a vertex of the triangle and the mid-point of the edge opposite the vertex. Prove that the three medians of a triangle are concurrent.

> $$\begin{aligned}
> & n \in \mathbb{Z}_{\ge 2} \\
> & \text{Let }\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{R}^n\text{ be the position vectors of vertices of a triangle.} \\
> & \mathbf{x} := \frac {\mathbf{a} + \mathbf{b} + \mathbf{c} } 3\text{.} \\
> & \mathbf{x_a} := \mathbf{x} - \mathbf{a} = \frac{-2 \mathbf{a} + \mathbf{b} + \mathbf{c} } 3 \\
> & \mathbf{x_b} := \mathbf{x} - \mathbf{b} = \frac{\mathbf{a} - 2 \mathbf{b} + \mathbf{c} } 3 \\
> & \mathbf{x_c} := \mathbf{x} - \mathbf{c} = \frac{\mathbf{a} + \mathbf{b} - 2\mathbf{c} } 3 \\
> & \phantom{=} \frac 3 2 \mathbf{x_a} \\
> & = \frac {-6 \mathbf{a} + 3 \mathbf{b} + 3 \mathbf{c} } 6 \\
> & = -\mathbf{a} + \frac 1 2 \mathbf{b} + \frac 1 2 \mathbf{c} \\
> & = \frac{\mathbf{b} + \mathbf{c} } 2 - \mathbf{a} \\
> & \implies \mathbf{x_a}\text{ is a direction vector of the median starting from }\mathbf{a}\text{.} \\
> & \phantom{=} \frac 3 2 \mathbf{x_b} \\
> & = \frac {3 \mathbf{a} - 6 \mathbf{b} + 3 \mathbf{c} } 6 \\
> & = \frac 1 2 \mathbf{a} - \mathbf{b} + \frac 1 2 \mathbf{c} \\
> & = \frac{\mathbf{a} + \mathbf{c} } 2 - \mathbf{b} \\
> & \implies \mathbf{x_b}\text{ is a direction vector of the median starting from }\mathbf{b}\text{.} \\
> & \phantom{=} \frac 3 2 \mathbf{x_c} \\
> & = \frac {3 \mathbf{a} + 3 \mathbf{b} - 6 \mathbf{c} } 6 \\
> & = \frac 1 2 \mathbf{a} + \frac 1 2 \mathbf{b} - \mathbf{c} \\
> & = \frac{\mathbf{a} + \mathbf{b} } 2 - \mathbf{c} \\
> & \implies \mathbf{x_c}\text{ is a direction vector of the median starting from }\mathbf{c}\text{.} \\
> & \because \mathbf{a} + \mathbf{x_a} = \mathbf{x} \\
> & \phantom \because \mathbf{b} + \mathbf{x_b} = \mathbf{x} \\
> & \phantom \because \mathbf{c} + \mathbf{x_c} = \mathbf{x} \\
> & \therefore \text{The three medians are concurrent.}
> \end{aligned}$$

### Q16.b

Prove that the three altitudes of a triangle are concurrent.

> $$\begin{aligned}
> & n \in \mathbb{Z}_{\ge 2} \\
> & \text{Let the origin }\mathbf{o}\text{ be one of the vertex of the triangle.} \\
> & \text{Let }\mathbf{a}, \mathbf{b} \in \mathbb{R}^n\text{ be the position vectors of the other two vertices of the triangle.} \\
> & \mathbf{a} \ne \mathbf{0}, \mathbf{b} \ne \mathbf{0}\text{ because otherwise two vertices are the same position,} \\
> & \text{making it no longer a triangle.} \\
> & \mathbf{a}\text{ and }\mathbf{b}\text{ are linearly independent because otherwise the three vertices are collinear,} \\
> & \text{making it no longer a triangle.} \\
> \\
> & \text{Consider the 2-dimensional linear span }S\text{ generated by }\mathbf{a}\text{ and }\mathbf{b}\text{.} \\
> & \text{The triangle is on }S\text{ as its three vertices are on }S\text{.} \\
> & \text{So its altitudes are on }S\text{.} \\
> & \text{Let }\mathbf{A_*}\text{ be the direction vector (not necessarily normalized)} \\
> & \text{of the altitude of the triangle starting from }*\text{.} \\
> & \mathbf{A_o} := \omega \mathbf{a} + \mathbf{b} \qquad \omega \in \mathbb{R} \\
> & \mathbf{A_a} := \alpha \mathbf{a} + \mathbf{b} \qquad \alpha \in \mathbb{R} \\
> & \mathbf{A_b} := \beta \mathbf{a} + \mathbf{b} \qquad \beta \in \mathbb{R} \\
> \\
> & \begin{aligned} \mathbf{A_o} \cdot (\mathbf{b} - \mathbf{a}) & = 0 \\
> (\omega \mathbf{a} + \mathbf{b}) \cdot (\mathbf{b} - \mathbf{a}) & = 0 \\
> (\omega - 1) \mathbf{a} \cdot \mathbf{b} - \omega \lVert \mathbf{a} \rVert^2 + \lVert \mathbf{b} \rVert^2 & = 0 \\
> \omega & = \frac {\mathbf{a} \cdot \mathbf{b} - \lVert \mathbf{b} \rVert^2} {\mathbf{a} \cdot \mathbf{b} - \lVert \mathbf{a} \rVert^2 } \\
> \\
> \mathbf{A_a} \cdot \mathbf{b} & = 0 \\
> (\alpha \mathbf{a} + \mathbf{b}) \cdot \mathbf{b} & = 0 \\
> \alpha \mathbf{a} \cdot \mathbf{b} + \lVert \mathbf{b} \rVert^2 & = 0 \\
> \alpha & = -\frac {\lVert \mathbf{b} \rVert^2} {\mathbf{a} \cdot \mathbf{b} } \\
> \\
> \mathbf{A_b} \cdot \mathbf{a} & = 0 \\
> (\beta \mathbf{a} + \mathbf{b}) \cdot \mathbf{a} & = 0 \\
> \beta \lVert \mathbf{a} \rVert^2 + \mathbf{a} \cdot \mathbf{b} & = 0 \\
> \beta & = -\frac {\mathbf{a} \cdot \mathbf{b} } {\lVert \mathbf{a} \rVert^2} \end{aligned} \\
> \\
> & \text{Find the intersection between the two medians starting from }\mathbf{a}\text{ and }\mathbf{b}\text{,} \\
> & \text{which is always possible on a plane, considering the medians are not parallel.} \\
> & \begin{aligned} \mathbf{a} + x \mathbf{A_a} & = \mathbf{b} + y \mathbf{A_b} && (x, y \in \mathbb{R}) \\
> \mathbf{a} + x\alpha \mathbf{a} + x \mathbf{b} & = \mathbf{b} + y \beta \mathbf{a} + y \mathbf{b} \\
> & \begin{cases} 1 + x\alpha = y\beta \\
> x = 1 + y \end{cases} \\
> 1 + \alpha + y\alpha & = y \beta \\
> y & = \frac {1 + \alpha} {\beta - \alpha} \\
> & = \frac {\frac {\mathbf{a} \cdot \mathbf{b} - \lVert \mathbf{b} \rVert^2} {\mathbf{a} \cdot \mathbf{b} } } {\frac {\lVert \mathbf{a} \rVert ^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} } } \\
> & = \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - \lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2} {\lVert \mathbf{a} \rVert ^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \\
> \\
> \mathbf{b} + y\mathbf{A_b} & = \mathbf{b} + \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - \lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2} {\lVert \mathbf{a} \rVert ^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \left(-\frac {\mathbf{a} \cdot \mathbf{b} } {\lVert \mathbf{a} \rVert^2} \mathbf{a} + \mathbf{b} \right) \\
> & = \frac {\lVert \mathbf{b} \rVert^2 \mathbf{a} \cdot \mathbf{b}  - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert ^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \mathbf{a} + \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \mathbf{b} \\
> & = \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \left(\frac {\lVert \mathbf{b} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} \mathbf{a} + \mathbf{b} \right) \\
> & = \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \left(\frac {\lVert \mathbf{b} \rVert^2 - \mathbf{a} \cdot \mathbf{b} } {\lVert \mathbf{a} \rVert^2 - \mathbf{a} \cdot \mathbf{b} } \mathbf{a} + \mathbf{b} \right) \\
> & = \frac {\lVert \mathbf{a} \rVert^2 \mathbf{a} \cdot \mathbf{b} - (\mathbf{a} \cdot \mathbf{b})^2} {\lVert \mathbf{a} \rVert^2 \lVert \mathbf{b} \rVert^2 - (\mathbf{a} \cdot \mathbf{b})^2} \mathbf{A_o} \end{aligned} \\
> & \because \text{The intersection of the two altitudes starting from }\mathbf{a}\text{ and }\mathbf{b} \\
> & \phantom{\because} \text{is a direction vector of the altitude starting from }\mathbf{o}\text{,} \\
> & \therefore \text{The three altitudes are concurrent.}
> \end{aligned}$$

## Q19

Find a vector equation and parametric equations for each of the following lines in $\mathbb{R}^3$.

### Q19.a

The line passing through $(6, -5, 2)$ and parallel to $\langle 3, 9, -2 \rangle$.

<!--
> $$\begin{aligned}
> \mathbf{a} & := \langle 6, -5, 2 \rangle \\
> \mathbf{b} & := \langle 3, 9, -2 \rangle \\
> \text{projection of }\mathbf{a}\text{ on }\mathbf{b} & = \frac {\mathbf{a} \cdot \mathbf{b} } {\mathbf{b} \cdot \mathbf{b} } \mathbf{b} \\
> & = \frac {6(3) + (-5)9 + 2(-2)} {3^2 + 9^2 + 2^2} \langle 3, 9, -2 \rangle \\
> & = \frac {18 - 45 - 4} {9 + 81 + 4} \langle 3, 9, -2 \rangle \\
> & = -\frac {31} {94} \langle 3, 9, -2 \rangle \\
> \text{direction vector} & = \mathbf{a} + \frac {31} {94} \langle 3, 9, -2 \rangle \\
> & = \langle 6, -5, 2 \rangle + \frac {31} {94} \langle 3, 9, -2 \rangle \\
> & = \left\langle \frac {657} {94}, -\frac {191} {94}, \frac {126} {94} \right\rangle \\
> \\
> \text{Let }t& \in \mathbb{R}\text{.} \\
> \text{vector equation} & = -\frac {31} {94} \langle 3, 9, -2 \rangle + \left\langle \frac {657} {94} t, -\frac {191} {94} t, \frac {126} {94} t \right\rangle \\
> & = \left\langle \frac {-93 + 657t} {94}, \frac {-279 - 191t} {94}, \frac {52 + 126t} {94} \right\rangle \\
> & = \left\langle \frac {-93 + 657t} {94}, \frac {-279 - 191t} {94}, \frac {26 + 63t} {47} \right\rangle \\
> \text{parametric equation} & = \begin{cases} x = \frac {-93 + 657t} {94} \\
> y = \frac {-279 - 191t} {94} \\
> z = \frac {26 + 63t} {47} \end{cases}
> \end{aligned}$$
-->

> $$\begin{aligned}
> \text{Let }t & \in \mathbb{R}\text{.} \\
> \text{vector equation} & = \langle 6, -5, 2 \rangle + t \langle 3, 9, -2 \rangle \\
> & = \langle 6 + 3t, -5 + 9t, 2 - 2t \rangle \\
> \text{parametric equation} & = \begin{cases} x = 6 + 3t \\
> y = -5 + 9t \\
> z = 2 - 2t \end{cases}
> \end{aligned}$$

### Q19.b

The line segment with end-points with end-points $(4, -6, 6)$ and $(2, 3, 1)$.

> $$\begin{aligned}
> \text{difference vector} & = \langle 4, -6, 6 \rangle - \langle 2, 3, 1 \rangle \\
> & = \langle 2, -9, 5 \rangle
> \\
> \text{Let }t & \in [0, 1]\text{.} \\
> \text{vector equation} & = \langle 2, 3, 1 \rangle + t \langle 2, -9, 5 \rangle \\
> & = \langle 2 + 2t, 3 - 9t, 1 + 5t \rangle \\
> \text{parametric equation} & = \begin{cases} x = 2 + 2t \\
> y = 3 - 9t \\
> z = 1 + 5 t \end{cases}
> \end{aligned}$$

### Q19.c

The line passing through $(2, 1, 0)$ and perpendicular to both $\hat{i} + \hat{j}$ and $\hat{j} + \hat{k}$.

> $$\begin{aligned}
> \text{direction vector} & = (\hat{i} + \hat{j}) \times (\hat{j} + \hat{k}) \\
> & = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} \\
> & = \hat{i} - \hat{j} + \hat{k} \\
> & = \langle 1, -1, 1 \rangle \\
> \text{Let }t & \in \mathbb{R}\text{.} \\
> \text{vector equation} & = \langle 2, 1, 0 \rangle + t \langle 1, -1, 1 \rangle \\
> & = \langle 2 + t, 1 - t, t \rangle \\
> \text{parametric equation} & = \begin{cases} x = 2 + t \\
> y = 1 - t \\
> z = t \end{cases}
> \end{aligned}$$

### Q19.d

The line passing through $(0, 1, 2)$ and orthogonally intersecting the line $$x = 1 + t\text{ and }y = 1 - t\text{ and }z = 2t$$.

> $$\begin{aligned}
> \mathbf{p} & := \langle 0, 1, 2 \rangle \\
> \mathbf{L}(t) & := \langle 1 + t, 1 - t, 2t \rangle \qquad t \in \mathbb{R} \\
> \\
> \text{Set...} \\
> (\mathbf{L}(t) - \mathbf{p}) \cdot \text{direction vector of }\mathbf{L} & = 0 \\
> \langle 1 + t, -t, 2t - 2 \rangle \cdot \langle 1, -1, 2 \rangle & = 0 \\
> (1 + t)(1) + (-t)(-1) + (2t - 2)(2) & = 0 \\
> 6t - 3 & = 0 \\
> t & = 0.5 \\
> \\
> \text{direction vector} & = \mathbf{L}(0.5) - \mathbf{p} \\
> & = \langle 1 + 0.5, 1 - 0.5, 1 \rangle - \langle 0, 1, 2 \rangle \\
> & = \langle 1.5, -0.5, -1 \rangle \\
> \text{Let }u & \in \mathbb{R}\text{.} \\
> \text{vector equation} & = \langle 0, 1, 2 \rangle + u \langle 1.5, -0.5, -1 \rangle \\
> & = \langle 1.5u, 1 - 0.5u, 2 - u \rangle \\
> \text{parametric equation} & = \begin{cases} x = 1.5u \\
> y = 1 - 0.5u \\
> z = 2 - u \end{cases}
> \end{aligned}$$

## Q22

### Q22.a

Let $P$ be a point on a <span style="color: red;">smooth</span> curve $r = f(\theta)$ in $\mathbb{R}^2$ which is not the origin, and let $\alpha$ be the acute angle between the line $OP$ and the tangent to the curve at $P$. Show that $$\cos \alpha = \frac {\lvert f'(\theta) \rvert} {\sqrt{f(\theta)^2 + f'(\theta)^2} }$$.

<!--
> $$\begin{aligned}
> & \text{Let }P = (f(\theta), \theta)\text{.} \\
> & \text{Let }U = (f(\varphi), \varphi)\text{ be another point on the curve.} \\
> & \text{Consider }\triangle OPU\text{.} \\
> & \text{Let }\chi\text{ be the angle between }OP\text{ and }PU{.}\\
> & \begin{aligned} PU^2 & = f(\theta)^2 + f(\varphi)^2 - 2 f(\theta) f(\varphi) \cos(\theta - \varphi) && (\text{cosine law}) \\
> f(\varphi)^2 & = f(\theta)^2 + PU^2 - 2(PU)f(\theta) \cos \chi && (\text{cosine law}) \\
> \cos \chi & = \frac {f(\theta)^2 + PU^2 - f(\varphi)^2} {2(PU) f(\theta)} \end{aligned} \\
> & \text{As the curve is smooth, as }\varphi \to \theta, PU\text{ approaches the tangent at }P\text{.} \\
> & \text{So }\chi \to \alpha\text{.} \\
> & \begin{aligned} \cos \alpha & = \lim_{\varphi \to \theta} \frac {f(\theta)^2 + PU^2 - f(\varphi)^2} {2(PU) f(\theta)} \\
> & = \lim_{\varphi \to \theta} \frac {2f(\theta)^2 - 2 f(\theta) f(\varphi) \cos(\theta - \varphi)} {f(\theta)^3 + f(\theta)f(\varphi)^2 - 2f(\theta)^2 f(\varphi) \cos(\theta - \varphi)} \\
> & = \lim_{\varphi \to \theta} \frac {2f(\theta) - 2f(\varphi) \cos(\theta - \varphi)} {f(\theta)^2 + f(\varphi)^2 - 2 f(\theta) f(\varphi) \cos(\theta - \varphi)} \\
> & = \frac {\lim_{\varphi \to \theta} \frac {2f(\theta) - 2f(\varphi) \cos(\theta - \varphi)} {\theta - \varphi} } {\lim_{\varphi \to \theta} \frac {f(\theta)^2 + f(\varphi)^2 - 2 f(\theta) f(\varphi) \cos(\theta - \varphi)} {\theta - \varphi} } \\
> & = \frac {2 \lim_{\varphi \to \theta} (f'(\varphi) \cos(\theta - \varphi) - f(\varphi) \sin(\theta - \varphi))} {2 \lim_{\varphi \to \theta} (f(\varphi)f'(\varphi) + f(\theta)(f'(\varphi) \cos(\theta - \varphi) - f(\varphi) \sin(\theta - \varphi))) } && (\text{L'Hopital rule}) \\
> & = \frac {f'(\theta)}  {2f(\theta)f'(\theta)} \end{aligned}
> \end{aligned}$$
-->

> $$\begin{aligned}
> \mathbf{p} & := \langle \cos\theta, \sin\theta \rangle \\
> \mathbf{p} \cdot \mathbf{p} & = 1 \\
> \\
> \mathbf{p}' & = \langle -\sin\theta, \cos\theta \rangle \\
> \mathbf{p}' \cdot \mathbf{p}' & = 1 \\
> \\
> \mathbf{p} \cdot \mathbf{p'} & = -\sin\theta \cos\theta + \sin\theta \cos\theta \\
> & = 0 \\
> \\
> \mathbf{P} & = \langle r \cos\theta, r \sin\theta \rangle \\
> & = \langle f(\theta) \cos\theta, f(\theta) \sin\theta \rangle \\
> & = f(\theta) \langle \cos\theta, \sin\theta \rangle \\
> & = f(\theta) \mathbf{p} \\
> \mathbf{P} \cdot \mathbf{P} & = f(\theta)^2 \mathbf{p} \cdot \mathbf{p} \\
> & = f(\theta)^2 \\
> \\
> \mathbf{P}' & = f'(\theta) \mathbf{p} + f(\theta) \mathbf{p}' \\
> \mathbf{P}' \cdot \mathbf{P}' & = f'(\theta)^2 + f(\theta)^2 \\
> \\
> \mathbf{P} \cdot \mathbf{P'} & = f(\theta)f'(\theta) \\
> \\
> \cos\alpha & = \frac {\lvert \mathbf{P} \cdot \mathbf{P}' \rvert} {\lVert \mathbf{P} \rVert \lVert \mathbf{P}' \rVert} && (\alpha\text{ is acute}) \\
> & = \frac{\lvert f(\theta) f'(\theta) \rvert} { \lvert f(\theta) \rvert  \sqrt{f(\theta)^2 + f'(\theta)^2} } \\
> & = \frac {\lvert f'(\theta) \rvert} {\sqrt{f(\theta)^2 + f'(\theta)^2} }
> \end{aligned}$$

### Q22.b

Using [(a)](#Q22.a), show that at every point $P$ on the curve $r = e^\theta$, the angle between the line $OP$ and the tangent line to the curve at $P$ is always $\pi / 4$.

> $$\begin{aligned}
> \cos a & = \frac {\lvert f'(\theta) \rvert} {\sqrt{f(\theta)^2 + f'(\theta)^2} } \\
> & = \frac {\lvert e^\theta \rvert} {\sqrt{e^{2\theta} + e^{2\theta} } } \\
> & = \frac {\lvert e^\theta \rvert} {\lvert e^\theta \rvert \sqrt 2} \\
> & = \frac 1 {\sqrt 2} \\
> \alpha & = \frac \pi 4 && (\alpha\text{ is acute})
> \end{aligned}$$

### Q22.c

Let $r = f(\theta)$ be a <span style="color: red;">smooth</span> curve such that at every point $P$ on it, the angle between the line $OP$ and the tangent line to the curve at $P$ is always a fixed constant. Show that there exist constants $C$ and $k$ such that $f(\theta) = C e^{k \theta}$ for all $\theta$.

> $$\begin{aligned}
> & \text{Let }f(\theta) = Ce^{k \theta}\text{.} \\
> & \begin{aligned} \cos\alpha & = \frac {\lvert Cke^{k \theta} \rvert} {\sqrt{e^{2k\theta} + C^2 k^2 e^{2k\theta} } } \\
> & = \frac {\lvert Ck \rvert \lvert e^{k \theta} \rvert} {\lvert e^{k \theta} \rvert \sqrt{1 + C^2 k^2} } \\
> & = \frac {\lvert Ck \rvert} {\sqrt{1 + C^2 k^2} } \end{aligned} \\
> & \text{The above shows that }\cos a\text{ does not depend on }\theta\text{.} \\
> & \text{So the angle is constant when changing }\theta\text{.} \\
> & \\
> & \text{When }C = 1,\text{ set }k = 0\text{ to get }\cos\alpha = 0, \\
> & \text{and as }k \to +\infty\text{, }\cos\alpha \to 1\text{.} \\
> & \text{By the intermediate value theorem,} \\
> & C, k\text{ can be set arbitrarily to get any real number in }[0, 1)\text{.} \\
> & \cos\alpha = 1\text{ can be ignored because the tangent is parallel to }OP\text{,}\\
> & \text{which is impossible if }f(\theta)\text{ is a function.}
> \end{aligned}$$
