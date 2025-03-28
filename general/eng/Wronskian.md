---
aliases:
  - Wronskian
  - Wronskian determinant
  - Wronskian determinants
  - Wronskians
tags:
  - flashcard/active/general/eng/Wronskian
  - language/in/English
---

# Wronskian

## the Wronskian and linear independence

If some [differentiable functions](differentiable%20function.md) are [linearly dependent](linear%20independence.md) on some [interval](interval%20(mathematics).md), {@{since [differentiation](derivative.md) is [linear](linearity%20of%20differentiation.md), the columns of the Wronskian are linearly dependent as well, thus the Wronskian is identically zero on said interval}@}. [Contrapositively](contraposition.md), {@{showing the Wronskian of some differentiable functions is not identically zero on some interval implies the functions are linearly independent on said interval}@}.

The converse statement that {@{the Wronskian is identically zero on some [interval](interval%20(mathematics).md) implies [linear dependence](linear%20dependence.md) on said interval is not true}@}. For example, {@{$x^2$ and $\lvert x \rvert x$ are [continuously differentiable](differentiable%20function.md) and linearly independent on any [interval](interval%20(mathematics).md) containing 0, but their Wronskian is identically zero everywhere}@}. Hence, the contrapositive statement that {@{linear independence on some interval implies the Wronskian is not identically zero on said interval is also false}@}. Extra conditions are {@{required, combined with the Wronskian being identically zero on some interval, to imply linear dependence on said interval}@}.

### examples of extra conditions

- {@{homogeneous [ordinary differential equation](linear%20differential%20equation.md)}@}: If {@{$n$ [differentiable functions](differentiable%20function.md) are solutions to a $k$-th order homogeneous ordinary differential equation on some interval $I$, where $n \le k$}@}, and {@{the equation in its explicit form is [continuous](continuous%20function.md) with respect to the [independent variable](dependent%20and%20independent%20variables.md) and [Lipschitz continuous](Lipschitz%20continuity.md) with respect to the solutions and their up to $k - 1$-th [derivatives](derivative.md)}@}, then {@{the Wronskian being identically zero (if $n = k$, the Wronskian being zero at a point $x_0$) implies linear dependence on $I$}@}. [Contrapositively](contraposition.md), {@{linearly independence on said interval implies the Wronskian is not identically zero (if $n = k$, the Wronskian is nowhere zero) on $I$}@}. A complete proof is given by Bôcher (1901).<sup>[\[1\]](#^ref-Bocher-1901)</sup> Another proof when $n = k$ is given as below.
    1. First, we construct {@{specific [initial values](initial%20value%20problem.md) from the Wronskian at $x_0$}@}. {@{The determinant of the Wronskian [matrix](matrix%20(mathematics).md) at $x_0$}@} is {@{given to be 0}@}. This implies {@{the following [system of linear equations](system%20of%20linear%20equations.md) has nontrivial solutions for the constants $c_i$: $$\begin{cases} && c_1 y_1(x_0) & + & c_2 y_2(x_0) & + & \cdots & + & c_n y_n(x_0) & = & 0 \\ && c_1 y_1'(x_0) & + & c_2 y_2'(x_0) & + & \cdots & + & c_n y_n'(x_0) & = & 0 \\ && \vdots & + & \vdots & + & \ddots & + & \vdots & = & 0 \\ && c_1 y_1^{(n - 1)}(x_0) & + & c_2 y_2^{(n - 1)}(x_0) & + & \cdots & + & c_n y_n^{(n - 1)}(x_0) & = & 0 \end{cases}$$}@}. Curiously, the left hand sides of the system are {@{the general solution of the differential equation and the derivatives of the general solution, giving $y(x_0) = y'(x_0) = \cdots = y^{(n - 1)}(x_0) = 0$}@}. Set {@{these to be the initial values of the differential equation at $x_0$}@}.
    2. Next, we prove that if {@{the [initial values](initial%20value%20problem.md) of the differential equation are all 0 for some $x_0$ on $I$, i.e. $y(x_0) = y'(x_0) = \cdots = y^{(n - 1)}(x_0) = 0$}@}, then {@{$y(x) = 0$ is the unique solution to the differential equation on $I$}@}. One, {@{$y(x) = 0$ is obviously a solution satisfying the above initial values}@}. Two, by {@{the [Picard–Lindelöf theorem](Picard–Lindelöf%20theorem.md) using the continuity conditions above, $y(x) = 0$ is the local unique solution satisfying the initial values}@}. Three, note that {@{$y(x) = 0$ can be defined on all of $I$ and does not explode to [infinity](infinity.md)}@}, so {@{$y(x) = 0$ is the global unique solution on $I$ satisfying the initial values}@}.
    3. Finally, if {@{$y(x) = 0$ is the unique solution on $I$}@}, then {@{the linear combination of the $n$ functions with [constant](constant%20(mathematics).md) [coefficients](coefficient.md)}@}, as {@{a solution of the differential equation, must equal the unique solution, i.e. $d_1 y_1(x) + d_2 y_2(x) + \cdots + d_n y_n(x) = 0$ for $n$ arbitrary constants $d_1, d_2, \ldots, d_n$}@}. Using {@{the initial value conditions above, we find that $d_i = c_i$}@}. Hence, there {@{exists nontrivial $c_i$ such that $c_1 y_1(x) + c_2 y_2(x) + \cdots + c_n y_n(x) = 0$}@}, proving that {@{the $n$ functions are [linearly dependent](linear%20independence.md) on $I$}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Wronskian) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Bôcher, Maxime (1901), ["Certain cases in which the vanishing of the Wronskian is a sufficient condition for linear dependence"](https://www.ams.org/journals/tran/1901-002-02/S0002-9947-1901-1500560-5/S0002-9947-1901-1500560-5.pdf) (PDF), _[Transactions of the American Mathematical Society](Transactions%20of%20the%20American%20Mathematical%20Society.md)_, Providence, R.I.: [American Mathematical Society](American%20Mathematical%20Society.md), __2__ (2): 139–149, [doi](doi%20(identifier).md):[10.2307/1986214](https://doi.org/10.2307%2F1986214), [ISSN](ISSN%20(identifier).md) [0002-9947](https://www.worldcat.org/issn/0002-9947), [JFM](JFM%20(identifier).md) [32.0313.02](https://zbmath.org/?format=complete&q=an:32.0313.02), [JSTOR](JSTOR%20(identifier).md) [1986214](https://www.jstor.org/stable/1986214) <a id="^ref-Bocher-1901"></a> ^ref-Bocher-1901
