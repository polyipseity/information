---
aliases:
  - variation of parameter
  - variation of parameters
  - variations of parameter
  - variations of parameters
tags:
  - flashcard/active/general/eng/variation_of_parameters
  - language/in/English
---

# variation of parameters

## description of method

Consider {@{a $n$-th order linear [ordinary differential equation](ordinary%20differential%20equation.md) in the form: $$a_n(x) y^{(n)}(x) + a_{n - 1}(x) y^{(n - 1)}(x) + \cdots + a_0(x) y(x) = b(x)$$, where $\frac{a_{i = 0,1,\ldots,n - 1}(x)}{a_n(x)}, \frac{b(x)}{a_n(x)}$ are [continuous functions](continuous%20function.md)}@}. The homogeneous equation is: {@{$$a_n(x) y^{(n)}(x) + a_{n - 1}(x) y^{(n - 1)}(x) + \cdots + a_0(x) y(x) = 0$$}@}. The general solution to the homogeneous equation {@{is called the _complementary solution_ $y_c(x)$, which is a [linear combination](linear%20combination.md) of $n$ [linearly independent](linear%20independence.md) [functions](function%20(mathematics).md) $y_{i = 1, 2, \ldots, n}(x)$, henceforth called the _[basis](basis%20(linear%20algebra).md)_, with arbitrary [constant](constant%20(mathematics).md) [coefficients](coefficient.md) $C_{i = 1, 2, \ldots, n}$: $$y_c(x) = C_1 y_1(x) + C_2 y_2(x) + \cdots + C_n y_n(x)$$}@}. A part of the solution to the nonhomogeneous equation {@{is called the _particular solution_ $y_p(x)$, which is a [linear combination](linear%20combination.md) of the [basis](basis%20(linear%20algebra).md) mentioned above with [function](function%20(mathematics).md) [coefficients](coefficient.md) $c_{i = 1, 2, \ldots, n}(x)$: $$y_p(x) = c_1(x) y_1(x) + c_2(x) y_2(x) + \cdots + c_n(x) y_n(x)$$}@}. Additionally, the method assumes {@{$n - 1$ conditions, which are: $$c_1'(x) y_1^{(j)}(x) + c_2'(x) y_2^{(j)}(x) + \cdots + c_n'(x) y_n^{(j)}(x) = 0 \qquad j = 0, 1, \ldots, n - 2$$}@}. This finishes the setup of the method.

Now we [differentiate](derivative.md) {@{the complementary solution $y_c(x)$ and the particular solution $y_p(x)$ $n$-times side by side and compare them}@}:

| $n$-th [derivative](derivative.md) | $y_c(x)$ | $y_p(x)$ | comments |
| - | - | - | - |
| $y_*(x)$ | $C_1 y_1(x) + C_2 y_2(x) + \cdots + C_n y_n(x)$ | $c_1(x) y_1(x) + c_2(x) y_2(x) + \cdots + c_n(x) y_n(x)$ | |
| $y_*^{(1)}(x)$ | $C_1 y_1^{(1)}(x) + C_2 y_2^{(1)}(x) + \cdots + C_n y_n^{(1)}(x)$ | $c_1(x) y_1^{(1)}(x) + c_2(x) y_2^{(1)}(x) + \cdots + c_n(x) y_n^{(1)}(x)$ | {@{By the [product rule](product%20rule.md), there should be an extra expression $c_1'(x) y_1(x) + c_2'(x) y_2(x) + \cdots + c_n'(x) y_n(x)$. However, the one of the assumptions made by the method means this expression equals zero. This continues to apply as we [differentiate](derivative.md) further.}@} |
| $y_*^{(2)}(x)$ | $C_1 y_1^{(2)}(x) + C_2 y_2^{(2)}(x) + \cdots + C_n y_n^{(2)}(x)$ | $c_1(x) y_1^{(2)}(x) + c_2(x) y_2^{(2)}(x) + \cdots + c_n(x) y_n^{(2)}(x)$ | See above. |
| ⋮ | ⋮ | ⋮ | ⋮ |
| $y_*^{(n - 1)}(x)$ | $C_1 y_1^{(n - 1)}(x) + C_2 y_2^{(n - 1)}(x) + \cdots + C_n y_n^{(n - 1)}(x)$ | $c_1(x) y_1^{(n - 1)}(x) + c_2(x) y_2^{(n - 1)}(x) + \cdots + c_n(x) y_n^{(n - 1)}(x)$ | See above. |
| $y_*^{(n)}(x)$ | $C_1 y_1^{(n)}(x) + C_2 y_2^{(n)}(x) + \cdots + C_n y_n^{(n)}(x)$ | $\begin{aligned} & c_1(x) y_1^{(n)}(x) + c_2(x) y_2^{(n)}(x) + \cdots + c_n(x) y_n^{(n)}(x) \\ + & c_1'(x) y_1^{(n - 1)}(x) + c_2'(x) y_2^{(n - 1)}(x) + \cdots + c_n'(x) y_n^{(n - 1)}(x) \end{aligned}$ | {@{As the assumptions only go up to the $n - 2$-th [derivative](derivative.md), so the extra expression produced by the [product rule](product%20rule.md) cannot be eliminated.}@} |

Comparing them, {@{if we set $c_i(x) = C_i$, which does not add any conditions to $c_i(x)$ since $C_i$ is arbitrary, then we get: $$\begin{aligned} y_p^{(j)}(x) & = y_c^{(j)}(x) \qquad j = 0, 1, \ldots, n - 1 \\ y_p^{(n)}(x) & = y_c^{(n)}(x) + c_1'(x) y_1^{(n - 1)}(x) + c_2'(x) y_2^{(n - 1)}(x) + \cdots + c_n'(x) y_n^{(n - 1)}(x) \end{aligned}$$}@}. Substitute {@{the particular solution $y_p(x)$ and above equations into the nonhomogeneous equation: $$\begin{aligned} a_n(x) y_p^{(n)}(x) + a_{n - 1}(x) y_p^{(n - 1)}(x) + \cdots + a_0(x) y_p(x) & = b(x) \\ \begin{aligned} a_n(x) y_c^{(n)}(x) + a_{n - 1}(x) y_c^{(n - 1)}(x) + \cdots + a_0(x) y_c(x) \\ + a_n(x) \left(c_1'(x) y_1^{(n - 1)}(x) + c_2'(x) y_2^{(n - 1)}(x) + \cdots + c_n'(x) y_n^{(n - 1)}(x)\right) \end{aligned} & = b(x) \\ c_1'(x) y_1^{(n - 1)}(x) + c_2'(x) y_2^{(n - 1)}(x) + \cdots + c_n'(x) y_n^{(n - 1)}(x) & = \frac{b(x)}{a_n(x)} && (\text{the complementary solution equals zero}) \end{aligned}$$}@}. The last equation is {@{the last condition we need to find the $n$ [function](function%20(mathematics).md) [coefficients](coefficient.md) as we now have a [system of linear equations](system%20of%20linear%20equations.md): $$\begin{cases} && y_1(x) c_1'(x) & + & y_2(x) c_2'(x) & + & \cdots & + & y_n(x) c_n'(x) & = & 0 \\ && y_1^{(1)}(x) c_1'(x) & + & y_2^{(1)}(x) c_2'(x) & + & \cdots & + & y_n^{(1)}(x) c_n'(x) & = & 0 \\ && \vdots & + & \vdots & + & \ddots & + & \vdots & = & 0 \\ && y_1^{(n - 2)}(x) c_1'(x) & + & y_2^{(n - 2)}(x) c_2'(x) & + & \cdots & + & y_n^{(n - 2)}(x) c_n'(x) & = & 0 \\ && y_1^{(n - 1)}(x) c_1'(x) & + & y_2^{(n - 1)}(x) c_2'(x) & + & \cdots & + & y_n^{(n - 1)}(x) c_n'(x) & = & \frac{b(x)}{a_n(x)} \end{cases}$$}@}. Then, {@{solve the above system to find $c_i'(x)$, and [integrate](integral.md) them to find $c_i(x)$. This completes finding the particular solution $y_p(x)$}@}. Using {@{[Cramer's rule](Cramer's%20rule.md) and the [Wronskian](Wronskian.md), where $W(x)$ is the [Wronskian](Wronskian.md) of the [basis](basis%20(linear%20algebra).md) and $W_i(x)$ is $W(x)$ but with the $i$-th column of the [matrix](matrix%20(mathematics).md) replaced with $\left(0, 0, \ldots, \frac{b(x)}{a_n(x)}\right)^{\operatorname{T} }$, the particular solution $y_p(x)$ can be written as: $$y_p(x) = \sum_{i = 1}^n y_i(x) \int\! \frac{W_i(x)}{W(x)} \,\mathrm{d}x \qquad (\text{discard constants of integration})$$}@}. Finally, the general solution {@{is the sum of the complementary solution and the particular solution, i.e. $y(x) = y_c(x) + y_p(x)$. This is because of [linearity of differentiation](linearity%20of%20differentiation.md) and that the complementary solution is the solution to the homogeneous counterpart of the nonhomogeneous equation, so adding the complementary solution corresponds to adding zero to the right hand side of the nonhomogeneous equation, which changes nothing}@}. Alternatively, {@{the [constants of integration](constant%20of%20integration.md) discarded above already give the complementary solution for free, so the general solution is: $$y(x) = \sum_{i = 1}^n y_i(x) \int\! \frac{W_i(x)}{W(x)} \,\mathrm{d}x$$}@}. There are two things to note about the general solution above. One, {@{the [basis](basis%20(linear%20algebra).md) are [linearly independent](linear%20independence.md) and are solutions of a linear homogeneous equation with [continuous](continuous%20function.md) [coefficients](coefficient.md), so $W(x)$ must not be identically zero. See [Wronskian § the Wronskian and linear independence](Wronskian.md#the%20Wronskian%20and%20linear%20independence)}@}. Two, {@{for a homogeneous equation, $b(x) = 0$, then $W_i(x)$ has a column of zeros, then $W_i(x) = 0$, then the [coefficients](coefficient.md) are only [constants of integration](constant%20of%20integration.md), recovering the general solution for a homogeneous equation, so the equation above also works for homogeneous equations}@}.

## intuitive explanations

### arbitrary conditions

It is okay to impose arbitrary conditions to get $n$ conditions to solve for the $n$ [function](function%20(mathematics).md) [coefficients](coefficient.md) $c_i(x)$ because {@{we are simply trying to find a solution and do not need to care about the uniqueness of it}@}. More generally, an additional assumption to solve a problem is called an {@{[ansatz](ansatz.md)}@}.

### reduction of order

- see: [ordinary differential equation § reduction of order](ordinary%20differential%20equation.md#reduction%20of%20order)

Variation of parameters comes quite naturally if {@{one reduces the inhomogeneous linear [ordinary differential equation](ordinary%20differential%20equation.md) into a first order system, convert it into [matrix](matrix%20(mathematics).md) form}@}, and {@{use the [fundamental matrix](fundamental%20matrix%20(linear%20differential%20equation).md), which is the same as the [Wronskian](Wronskian.md) matrix of the solutions to the homogeneous equation for linear ordinary differential equations, to solve the resulting equation}@}.

### osculating parameters

Consider {@{a $n$-th order inhomogeneous linear [ordinary differential equation](ordinary%20differential%20equation.md)}@}. We want to {@{express the solution and its up to $n - 1$-th [derivatives](derivative.md) to the inhomogeneous equation using a [linear combination](linear%20combination.md) of the [linearly independent](linear%20independence.md) solutions to the homogeneous equation with [constant](constant%20(mathematics).md) [coefficients](coefficient.md): $$y^{(j)}(x) = \sum_{i = 1}^n c_i y_i^{(j)}(x) \qquad j = 0, 1, \ldots, n - 1$$. The equations for the derivatives are easily derived from the original equation where $j = 0$}@}.

In general, {@{this cannot be done for all $x$ using constant coefficients only}@}. However, by {@{viewing the $n$ equations above as a [system of linear equations](system%20of%20linear%20equations.md)}@}, we find that we can {@{vary the constants $c_i$ such that the right hand side matches $y^{(j)}(x)$ at some $x_0$ and approximate nearby values}@}.

Variation of parameters is {@{simply performing the above approximation for every $x$ to get an exact solution}@}. To do so, {@{we replace the constants $c_i$ with  [functions](function%20(mathematics).md) $c_i(x)$ that varies with $x$ and then find $c_i(x)$}@}. As {@{the [product rule](product%20rule.md) produces an extra expression $\sum_{i = 1}^n c_i'(x) y_i^{(j)}(x)$ every time we [differentiate](derivative.md), so we set that expression to 0 for the first $n - 1$ derivatives to match the form needed for the aforementioned approximation and keep the derivatives simple}@}. Conveniently, {@{this gets us $n - 1$ conditions, and we only need 1 more condition to find the $n$ functions $c_i(x)$}@}.

The last condition {@{comes from the inhomogeneous equation. For deriving the $n$-th derivative, keep the extra expression $\sum_{i = 1}^n c_i'(x) y_i^{(n - 1)}(x)$. Substitute the $n - 1$ equations we have just derived above into the inhomogeneous equation, replace the homogeneous equation that subsequently appears with 0 to get the last condition: $$\sum_{i = 1}^n c_i'(x) y_i^{(n - 1)}(x) = \frac{b(x)}{a_n(x)}$$, where $b(x)$ is the constant term and $a_n(x)$ is the leading coefficient}@}. Solve {@{the system of linear equations of $n$ conditions to find $c_i(x)$}@}.

### physical explanation

Consider {@{a [linear ordinary differential equation](linear%20differential%20equation.md) describing a forced [damped](damping.md) [spring](spring%20(device).md): $$\begin{aligned} mx''(t) & = -mx(t) - 2mx'(t) + mF(x) && (\text{Newton's second law}) \\ x''(t) + 2x'(t) + x(t) & = F(x) && (\text{differential equation}) \end{aligned}$$, where $x$ is the [displacement](displacement%20(geometry).md) from the equilibrium, $m$ is the [mass](mass.md), and $mF(t)$ is a [time](time.md)-dependent driving [force](force.md)}@}. All quantities on the right hand side (but not left hand side) of the first equation are additionally multiplied by $m$ to make the second equation simpler. When the driving force is {@{zero, the differential equation is homogeneous}@}.

We now construct the solution [physically](physics.md). Consider {@{an infinitesimal [time](time.md) slice $\mathrm{d}t_0$ centered on time $t_0$}@}. We can interpret the system above {@{during the time slice $\mathrm{d}t_0$ as a system satisfying the homogeneous equation, distributed by an [impulse](impulse%20(physics).md) (change in [momentum](momentum.md)) of $mF(x) \,\mathrm{d}t_0$}@}.

Mathematically, this can be written as {@{an [initial value problem](initial%20value%20problem.md), in which the system satisfies the homogeneous equation at all times, constrained by initial values at $t_0$: $$\begin{aligned} x_{t_0}''(t) + 2x_{t_0}'(t) + x_{t_0}(t) & = 0 \\ x_{t_0}'(t_0) & = F(t_0) \,\mathrm{d}t_0 \\ x_{t_0}(t_0) & = 0 \end{aligned}$$}@}. To derive the above initial value problem, first {@{ignore the [force](force.md) disturbance and [translate](translation%20(geometry).md) $x(t)$ to a new [function](function%20(mathematics).md) $x_{t_0}(t)$ such that $x_{t_0}(t_0) = x'_{t_0}(t_0) = 0$: $$\begin{aligned} x_{t_0}'(t) & := x'(t) - (x'(t_0)) \\ x_{t_0}(t) & := x(t) - tx'(t_0) - (x(t_0) - t_0x'(t_0)) \\ & \text{Validate using }t = t_0 \\ x_{t_0}'(t_0) & = x'(t_0) - (x'(t_0)) = 0 \\ x_{t_0}(t_0) & = x(t_0) - t_0x'(t_0) - (x(t_0) - t_0x'(t_0)) = 0 \end{aligned}$$. This can be physically seen as changing the [frame of reference](frame%20of%20reference.md) so that the initial values at $t_0$ are all 0}@}. Then, {@{it is obvious that the initial values are all 0, except for $x_{t_0}'(t_0) = \frac{mF(x)}m \,\mathrm{d}t_0 = F(x) \,\mathrm{d}t_0$ by reconsidering the force disturbance}@}. The solution to the above initial value problem {@{can be solved like a homogeneous equation and is $$x_{t_0}(t) = (t - t_0) e^{t_0 - t} F(t_0) \,\mathrm{d}t_0$$}@}.

> [!info]- details
>
> $$\begin{aligned}
> x_{t_0}''(t) + 2x_0'(t) + x_{t_0}(t) & = 0 \\
> r^2 + 2r + 1 & = 0  \\
> r & = -1 \,(\text{multiplicity 2}) \\
> x_{t_0}(t) & = (c_1 + c_2 t) e^{-t} \\
> x_{t_0}'(t) & = (-c_1 + c_2 - c_2 t) e^{-t} \\
> \\
> x_{t_0}(t_0) & = 0 \\
> (c_1 + c_2 t_0) e^{-t_0} & = 0 \\
> c_1 & = -c_2 t_0 \\
> \\
> x_{t_0}'(t_0) & = F(t_0) \,\mathrm{d}t_0 \\
> (-c_1 + c_2 - c_2 t_0) e^{-t_0} & = F(t_0) \,\mathrm{d}t_0 \\
> c_2 e^{-t_0} & = F(t_0) \,\mathrm{d}t_0 \\
> c_2 & = e^{t_0} F(t_0) \,\mathrm{d}t_0 \\
> c_1 & = -t_0 e^{t_0} F(t_0) \,\mathrm{d}t_0 \\
> \\
> x_{t_0}(t) & = (t - t_0) e^{t_0 - t} F(t_0) \,\mathrm{d}t_0
> \end{aligned}$$

Consider the physical meaning of $x_{t_0}(t)$. It describes {@{the effect of $F(t_0) \,\mathrm{d}t_0$ during an infinitesimal time slice $\mathrm{d}t_0$ on the homogeneous version of $x(t)$, [translated](translatio%20(geometry).md) such that $x(t_0) = 0$ (since $x_{t_0}(t_0) = 0$)}@}. Thus, $x_{t_0}(t)$ gives {@{the difference from the homogeneous version of $x(t)$ at time $t$ caused by $F(t_0) \,\mathrm{d}t_0$ during the time interval $[t_0, t]$ (if $t_0 > t$, its effect is run backwards from $t_0$ to $t$)}@}. Finally, by linearity, {@{summing $x_{t_0}(t) \,\mathrm{d}t_0$ from $t_0 = 0$ to $t_0 = t$ accounts for the effect of $F(t)$ during $[0, t]$ on the homogeneous version of $x(t)$}@}. Finally, the solution, {@{assuming $x(0) = 0$, is: $$\begin{aligned} x(t) & = \int_0^t\! (t - t_0) e^{t_0 - t} F(t_0) \,\mathrm{d}t_0 \\ & = e^{-t} \int_0^t\! (t - t_0) e^{t_0} F(t_0) \,\mathrm{d}t_0 \\ & = e^{-t} t \int_0^t\! e^{t_0} F(t_0) \,\mathrm{d}t_0 - e^{-t} \int_0^t\! t_0 e^{t_0} F(t_0) \,\mathrm{d}t_0 \end{aligned}$$}@}. (annotation: Actually, $x_{t_0}(t)$ is {@{an example of using a [Green's function](Green's%20function.md)}@}.)

To assure ourselves, we can {@{verify that the above solution satisfies the original inhomogeneous differential equation}@} (using {@{the second expression above to make the proof shorter}@} and applying {@{the [Leibniz integral rule](Leibniz%20integral%20rule.md) several times}@}):

$$\begin{aligned}
x(t) & = e^{-t} \int_0^t\! (t - t_0) e^{t_0} F(t_0) \,\mathrm{d}t_0 \\
x'(t) & = e^{-t} \int_0^t\! e^{t_0} F(t_0) \,\mathrm{d}t_0 - e^{-t} \int_0^t\! (t - t_0) e^{t_0} F(t_0) \,\mathrm{d}t_0 \\
& = e^{-t} \int_0^t\! e^{t_0} F(t_0) \,\mathrm{d}t_0 - x(t) \\
x''(t) & = F(t) - e^{-t} \int_0^t\! e^{t_0} F(t_0) \,\mathrm{d}t_0 - x'(t) \\
& = F(t) - 2x'(t) - x(t) \\
x''(t) + 2x'(t) + x(t) & = F(t)
\end{aligned}$$

Remember that we have assumed $x(0) = 0$ above, but {@{this condition can be removed by recognizing that the above $x(t)$ is a particular solution. Adding the complementary solution, i.e. the solution to the corresponding homogeneous equation, gets us the general solution that can accommodate any [initial values](inital%20value%20problem.md), which is: $$\begin{aligned} x(t) = c_1 e^{-t} + c_2 e^{-t} t + e^{-t} t \int_0^t\! e^{t_0} F(t_0) \,\mathrm{d}t_0 - e^{-t} \int_0^t\! t_0 e^{t_0} F(t_0) \,\mathrm{d}t_0 \end{aligned}$$}@}.

This explanation can be generalized to {@{higher order inhomogeneous differential equations}@}. Consider {@{a $n$-th order inhomogeneous linear differential equation: $$Dx(t) = F(t)$$, where $D$ is a $n$-th order linear [differential operator](differential%20operator.md)}@}. Then, {@{convert the equation into a homogeneous [initial value problem](initial%20value%20problem.md): $$Dx(t) = 0, \quad x(t_0) = x'(t_0) = \cdots = x^{(n - 2)}(t_0) = 0, x^{(n - 1)}(t_0) = F(t_0) \,\mathrm{d}t_0$$. Find its solution, remove $\mathrm{d}t_0$ (this is not done in the first example), and denote said expression $x_{t_0}(t)$}@}. Finally, calculate {@{a particular solution of the inhomogeneous equation as follows: $$x(t) = \int_{c}^t\! x_{t_0}(t) \,\mathrm{d}t_0$$, where $c$ is an arbitrary [constant](constant%20(mathematics).md). You can set $c$ to something convenient for finding the arbitrary constants in the general solution from initial values}@}. {@{Add the complementary solution}@} to get the general solution.

The relation between this explanation and variation of parameters is that {@{setting $n - 1$ [initial values](initial%20value%20problem.md) to 0 corresponds to the $n - 1$ assumptions made by variation of parameters}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/variation_of_parameters) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
