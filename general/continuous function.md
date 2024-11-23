---
aliases:
  - continuity
  - continuous function
  - continuous functions
  - discontinuity
  - discontinuous function
  - discontinuous functions
tags:
  - flashcard/active/general/continuous_function
  - language/in/English
---

# continuous function

## real functions

### definition

#### continuity at a point

There are {@{several ways}@} to define whether a function is _continuous_ at a point. The most common one {@{is in terms of [limits](limit%20of%20a%20function.md). A function $f$ is continuous at a point $c$ if $\lim_{x \to c} f(x) = f(c)$ or $c$ is an [isolated point](isolated%20point.md) of the [domain](domain%20of%20a%20function.md) of $f$}@}. <!--SR:!2025-12-05,462,310!2026-07-31,654,330-->

> [!tip] tips
>
> There are subtleties with the common definition, described under [§ definition in terms of limits of functions](#definition%20in%20terms%20of%20limits%20of%20functions).
>
> - [isolated points](isolated%20point.md) of a [set](set%20(mathematics).md) containing [reals](real%20number.md) ::@:: For example, $\set{0, 2}$ are [isolated points](isolated%20point.md) of $(-\infty, -12) \cup \set{0} \cup [0.5, 1) \cup \set{2} \cup [2.1, 2.11]$. <!--SR:!2026-04-07,530,310!2025-11-30,458,310-->

#### global continuity

There are {@{several incompatible definitions}@} of the (global) continuity of a function, depending on the nature of its domain. <!--SR:!2026-10-08,717,330-->

A function is continuous on an open [interval](interval%20(mathematics).md) {@{if the interval is contained in the [function domain](domain%20of%20a%20function.md) and the function is continuous at every interval point}@}. A function is continuous on a semi-open or closed [interval](interval%20(mathematics).md) {@{if the interval is contained in the [function domain](domain%20of%20a%20function.md), the function is continuous at every [interior](interior%20(topology).md) point of the interval, and the value of the function at each interval endpoint is the limit of the values of the function as the input tends to the endpoint from the interval interior}@}. <!--SR:!2025-10-30,396,290!2025-12-08,431,304-->

A function that {@{is continuous on the interval $(-\infty, +\infty)$, i.e. $\mathbb{R}$}@}, is _continuous everywhere_. It is also {@{often simply called a continuous function}@}. Sometimes, a function that {@{is continuous on its [domain](domain%20of%20a%20function.md) but not all [real](real%20number.md)}@} is also called a continuous function, but it is {@{not continuous everywhere}@}. For example, {@{[partial functions](partial%20function.md) that have a domain of all reals except at [isolated points](isolated%20point.md)}@}, which are continuous in its domain. In {@{contexts interested in the partial functions' behavior near exceptional points}@}, they are called _discontinuous functions_ instead, confusingly. <!--SR:!2025-02-21,265,330!2026-11-28,755,330!2025-02-01,248,324!2026-01-01,487,310!2025-01-07,228,324!2025-07-14,324,290-->

A __discontinuous function__ is {@{a function that is _not continuous_. By this definition, a function is either continuous or discontinuous}@}. <!--SR:!2025-02-01,212,333-->

> [!tip] tips
>
> - [interior](interior%20(topology).md) of a real interval ::@:: For $a, b \in \mathbb{R}$, $(a, b)$ is the [interior](interior%20(topology).md) of $[a, b]$, $(a, b]$, $[a, b)$, and $(a, b)$. <!--SR:!2025-05-25,343,344!2024-12-13,213,330-->
> - relation of definitions between open intervals and semi-closed or closed intervals ::@:: One can interpret the definition for the semi-closed or closed interval differently. The function is continuous on an interval if the function is continuous on the corresponding open interval, and the endpoints $a$ satisfies $\lim_{x \to a^\pm} f(x) = f(a)$, choosing the direction such that the limit approaches the endpoint from the interval. <!--SR:!2026-05-13,575,310!2025-01-21,239,324-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :@: It is continuous by [vacuous truth](vacuous%20truth.md). Interestingly, it is neither continuous nor discontinuous at every [real](real%20number.md), and it is continuous and it is not continuous at every point in its [domain](domain%20of%20a%20function.md) by [vacuous truth](vacuous%20truth.md). <!--SR:!2024-11-28,192,310-->
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ :@: It is continuous. Note that an isolated point is closed under the usual definition of "closed". <!--SR:!2025-06-20,306,290-->

#### discontinuity at a point

A function is _discontinuous_ at a point {@{if the point is in the [topological closure](closure%20(topology).md) of the [function domain](domain%20of%20a%20function.md), and either the point is not in the [function domain](domain%20of%20a%20function.md) or the function is not continuous at the point}@}. <!--SR:!2025-05-15,283,290-->

> [!tip] tips
>
> - neither continuous nor discontinuous ::@:: A function can be neither continuous nor discontinuous at a point. For example, $f(x > 0) = 0$ is neither continuous nor discontinuous at $-1$. It is however discontinuous at $0$.  An exaggerated example is that all [real-valued functions](real-valued%20function.md) are not defined at [Mount Everest](Mount%20Everest.md). <!--SR:!2025-11-04,438,310!2025-01-12,235,330-->
> - [topological closure](closure%20(topology).md) of a real interval ::@:: For $a, b \in \mathbb{R}$, $[a, b]$ is the [topological closure](closure%20(topology).md) of $(a, b)$, $[a, b)$, $(a, b]$, and $[a, b]$. <!--SR:!2024-12-13,194,310!2027-01-30,820,344-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :@: It is not discontinuous at every [real](real%20number.md). However, it is discontinuous and it is not discontinuous at every point in its [domain](domain%20of%20a%20function.md) by [vacuous truth](vacuous%20truth.md). <!--SR:!2026-07-31,654,330-->
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ at $0$ :@: It is not discontinuous at $0$. <!--SR:!2025-09-30,414,310-->
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $0$ :@: It is not discontinuous at $0$. <!--SR:!2027-03-24,854,344-->
> - $f(x \in (0, +\infty)) = \sqrt{x}$ at $0$ :@: It is discontinuous at $0$. <!--SR:!2026-08-07,668,330-->
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $-1$ :@: It is not discontinuous at $-1$. <!--SR:!2026-10-02,702,330-->

#### definition in terms of limits of functions

A function $f$ is _continuous_ at a point $c$ {@{if $$\lim_{x \to c} f(x) = f(c)$$ or $c$ is an [isolated point](isolated%20point.md) of the [domain](domain%20of%20a%20function.md) of $f$}@}. <!--SR:!2026-02-24,530,324-->

Note that for endpoints of the [function domain](domain%20of%20a%20function.md), {@{the [limit](limit%20of%20a%20function.md) at the endpoints only requires approaching the endpoint from the domain}@}. The part about [isolated point](isolated%20point.md) is needed because {@{[limit](limit%20of%20A%20function.md) is not defined for isolated points}@}. <!--SR:!2026-12-30,790,330!2025-01-03,210,310-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :@: It is not continuous at every [real](real%20number.md). However, it is continuous and it is not continuous at every point in its [domain](domain%20of%20a%20function.md) by [vacuous truth](vacuous%20truth.md). <!--SR:!2024-12-28,222,330-->
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ at $0$ :@: It is continuous at $0$. <!--SR:!2024-12-21,214,324-->
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $0$ :@: It is continuous at $0$. <!--SR:!2025-02-18,263,330-->
> - $f(x \in (0, +\infty)) = \sqrt{x}$ at $0$ :@: It is not continuous at $0$. <!--SR:!2026-11-09,740,330-->
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $-1$ :@: It is not continuous at $-1$. <!--SR:!2026-06-18,634,330-->

### construction of continuous functions

The set of continuous functions is closed under {@{addition, subtraction, multiplication; and reciprocal and division when restricting the domain to where the divisor is nonzero}@}. That is, given two continuous functions $f, g: D \subseteq \mathbb{R} \to \mathbb{R}$, {@{$f + g$, $f - g$, $f \cdot g$ are continuous in $D$, and $1 / g$ and $f / g$ are continuous in $D \setminus \set{x: g(x) \ne 0}$}@}. The [converse](converse%20(logic).md) {@{is not necessarily true, however}@}. For example, {@{given a discontinuous [real-valued function](real-valued%20function.md) $f$, $f + (-f) = f - f = 0$ and $f \cdot (f)^{-1} = f / f = 1$ are continuous. So the antecedent and the consequent cannot be swapped}@}. <!--SR:!2026-02-16,505,333!2026-07-10,621,333!2024-12-02,176,333!2026-01-20,484,333-->

> [!info]- proof of the set of continuous functions being closed under basic arithmetic operations
>
> - proof of the set of continuous functions being closed under basic arithmetic operations / strategy ::@:: For a continuous function $f(x)$, $\lvert f(x) - f(c) \rvert$ can be made to be smaller than an arbitrary small real $\epsilon$ for inputs in an interval around $c$. So setup the required inequalities, transform them, and identify expressions like $\lvert f(x) - f(c) \rvert$ in said inequalities. Claim that such expressions can be made arbitrarily small. <!--SR:!2025-08-11,268,370!2024-12-12,81,370-->
>
> Using the above definitions...
>
> $f \pm g$: Let $\epsilon > 0$ be an arbitrary real. Choose any $c$ in $D$. By continuity, there is a $\delta_f > 0$ such that $0 < \lvert f(x) - f(c) \rvert < \epsilon / 2$ for all $x$ in $D$ that satisfies $0 < \lvert x - c \rvert < \delta_f$. Similarly, there is a $\delta_g > 0$ such that $0 < \lvert g(x) - g(c) \rvert < \epsilon / 2$ for all $x$ in $D$ that satisfies $0 < \lvert x - c \rvert < \delta_g$. Let $\delta > 0$ be the minimum of $\delta_f$ and $\delta_g$. Then for all $x$ in $D$ that satisfies $0 < \lvert x - c \rvert < \delta$, we have $$\begin{aligned}
> \lvert (f(x) \pm g(x)) - (f(c) \pm g(c)) \rvert & = \lvert (f(x) - f(c)) \pm (g(x) - g(c)) \rvert \\
> & \le \lvert f(x) - f(c) \rvert + \lvert g(x) - g(c) \rvert \\
> & < \epsilon / 2 + \epsilon / 2 \\
> & = \epsilon
> \end{aligned}$$, as required.
>
> $f \cdot g$: Let $\epsilon > 0$ be an arbitrary real. Choose any $c$ in $D$. Consider $$\begin{aligned}
> \lvert f(x) g(x) - f(c) g(c) \rvert & = \lvert (f(x) - f(c)) (g(x) - g(c)) + f(x) g(c) + f(c) g(x) - 2 f(c) g(c) \rvert \\
> & = \lvert (f(x) - f(c)) (g(x) - g(c)) + (f(x) - f(c)) g(c) + f(c) (g(x) - g(c)) \rvert \\
> & \le \lvert f(x) - f(c) \rvert \lvert g(x) - g(c) \rvert + \lvert f(x) - f(c) \rvert \lvert g(c) \rvert + \lvert f(c) \rvert \lvert g(x) - g(c) \rvert
> \end{aligned}$$. By continuity, $\lvert f(x) - f(c) \rvert > 0$ and $\lvert g(x) - g(c) \rvert > 0$ can be as small as we want for all $x$ in an interval near $c$ in $D$. So we can always choose two small enough errors for the above two expressions such that $0 < \lvert f(x) - f(c) \rvert \lvert g(x) - g(c) \rvert + \lvert f(x) - f(c) \rvert \lvert g(c) \rvert + \lvert f(c) \rvert \lvert g(x) - g(c) \rvert < \epsilon$. Note that $\lvert f(c) \rvert$ and $\lvert g(c) \rvert$ do not depend on $x$ and are constants. Finally, $0 < \lvert f(x) g(x) - f(c) g(c) \rvert < \epsilon$, as required.
>
> $1 / g$: Let $\epsilon > 0$ be an arbitrary real. Let $g'$ be the restriction of $g$ to $D' := \set{x \in D : g(x) \ne 0}$. Choose any $c$ in $D'$. Let $\epsilon' := \lvert g(x) - g(c) \rvert$. Consider $$\begin{aligned}
> \lvert 1 / g'(x) - 1 / g'(c) \rvert & = \lvert (g'(c) - g'(x)) / (g'(x) g'(c)) \rvert \\
> & = \lvert g'(x) - g'(c) \rvert / \lvert g'(x) g'(c) \rvert \\
> & = \frac {\epsilon'} {\left\lvert (g'(x) - g'(c)) g'(c) + (g'(c))^2 \right\rvert} \\
> & = \frac {\epsilon'} {\lvert (g'(x) - g'(c)) g'(c) \rvert + (g'(c))^2} \\
> & = \frac {\epsilon'} {\lvert (g'(x) - g'(c)) \rvert \lvert g'(c) \rvert + (g'(c))^2} \\
> & = \frac {\epsilon'} {\epsilon' \lvert g'(c) \rvert + (g'(c))^2}
> \end{aligned}$$. Set the expression to be less than $\epsilon$: $$\begin{aligned}
> \frac {\epsilon'} {\epsilon' \lvert g'(c) \rvert + (g'(c))^2} & < \epsilon \\
> \epsilon' & < \epsilon' \epsilon \lvert g'(c) \rvert + \epsilon (g'(c))^2 \\
> \epsilon' - \epsilon' \epsilon \lvert g'(c) \rvert & < \epsilon (g'(c))^2 \\
> \epsilon' (1 - \epsilon \lvert g'(c) \rvert) & < \epsilon (g'(c))^2 \\
> \epsilon' & \begin{cases} < \frac {\epsilon (g'(c))^2} {1 - \epsilon \lvert g'(c) \rvert} & \text{if } 1 - \epsilon \lvert g'(c) \rvert > 0 \\
> \in \mathbb{R}, \epsilon (g'(c))^2 > 0 & \text{if } 1 - \epsilon \lvert g'(c) \rvert = 0 \\
> {>} \frac {\epsilon (g'(c))^2} {1 - \epsilon \lvert g'(c) \rvert} & \text{if } 1 - \epsilon \lvert g'(c) \rvert < 0
> \end{cases}
> \end{aligned}$$. Note that the above $\epsilon'$ is only required to respect an inequality that depends on $\epsilon$ and $c$ but not $x$. So by the continuity of $g'$, we can choose $\epsilon' > 0$ arbitrarily small (or large) for all $x$ near $c$ in $D'$. The first case can always be satisfied by choosing $\epsilon'$ small enough. The second case can always be satisfied as $\epsilon (g'(c))^2 > 0$. The third case can always be satisfied as the expression on the right is always negative. So $0 < \lvert 1 / g'(x) - 1 / g'(c) \rvert < \epsilon$, as required.
>
> $f / g$: Let $f'$ and $g'$ be the restriction of respectively $f$ and $g$ to $D' := \set{x \in D : g(x) \ne 0}$. Let $h := 1 / g'$. Then $h$ is continuous by above. Let $f' / g' := f' \cdot h$. Then $f' / g'$ is continuous by above, as required.

Apart from basic arithmetic operations, the set of continuous functions is also closed under {@{[function composition](function%20composition.md)}@}. That is, {@{given two continuous functions $g: D_g \subseteq \mathbb{R} \to \mathbb{R}, f: D_f \subseteq \mathbb{R} \to R_f \subseteq D_g$, then their composition $c(x): D_f \to \mathbb{R} := (g \circ f)(x) \equiv g(f(x))$ is continuous}@}. The [converse](converse%20(logic).md) {@{is not necessarily true, however}@}. For example, {@{given a discontinuous [real-valued function](real-valued%20function.md) $f$, one can let $g$ be a [constant function](constant%20function.md). Then $g \circ f$ is continuous. So the antecedent and the consequent cannot be swapped}@}. <!--SR:!2025-04-28,293,353!2025-11-24,441,333!2024-11-24,162,333!2026-07-17,620,333-->

> [!info]- proof of the set of continuous functions being closed under function composition
>
> - proof of the set of continuous functions being closed under function composition / strategy ::@:: Chain the two inequalities together to produce the required inequality. <!--SR:!2024-12-17,86,370!2025-10-06,317,370-->
>
> Using the above definitions...
>
> $g \circ f$: Let $\epsilon > 0$ be an arbitrary real. Choose any $c_g$ in $D_g$. By continuity, there is a $\delta_g > 0$ such that $0 < \lvert g(x) - g(c_g) \rvert < \epsilon$ for all $x$ in $D_g$ that satisfies $0 < \lvert x - c_g \rvert < \delta_g$. Now choose any $c$ in $D_f$. By continuity, using $\delta_g$ as the error, there is a $\delta > 0$ such that $0 < \lvert f(x) - f(c) \rvert < \delta_g$ for all $x$ in $D_f$ that satisfies $0 < \lvert x - c \rvert < \delta$. By combining them, there is a $\delta > 0$ such that $0 < \lvert g(f(x)) - g(f(c)) \rvert < \epsilon$ for all $x$ in $D_f$ that satisfies $0 < \lvert x - c \rvert < \delta$, as required.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/continuous_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
