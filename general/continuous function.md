---
aliases:
  - continuity
  - continuous function
  - continuous functions
tags:
  - flashcard/general/continuous_function
  - language/in/English
---

# continuous function

## real functions

### continuity at a point

There are {{several ways}} to define whether a function is _continuous_ at a point. The most common one {{is in terms of [limits](limit%20of%20a%20function.md). A function $f$ is continuous at a point $c$ if $\lim_{x \to c} f(x) = f(c)$ or $c$ is an [isolated point](isolated%20point.md) of $f$}}.

> [!tip] tips
>
> There are subtleties with the common definition, described under [§ definition in terms of limits of functions](#definition%20in%20terms%20of%20limits%20of%20functions).
>
> - [isolated points](isolated%20point.md) of a [set](set%20(mathematics).md) containing [reals](real%20number.md) ::: For example, $\set{0, 2}$ are [isolated points](isolated%20point.md) of $(-\infty, -12) \cup \set{0} \cup [0.5, 1) \cup \set{2} \cup [2.1, 2.11]$.

### global continuity

There are {{several incompatible definitions}} of the (global) continuity of a function, depending on the nature of its domain.

A function is continuous on an open [interval](interval%20(mathematics).md) {{if the interval is contained in the [function domain](domain%20of%20a%20function.md) and the function is continuous at every interval point}}. A function is continuous on a semi-open or closed [interval](interval%20(mathematics).md) {{if the interval is contained in the [function domain](domain%20of%20a%20function.md), the function is continuous at every [interior](interior%20(topology).md) point of the interval, and the value of the function at each interval endpoint is the limit of the values of the function as the input tends to the endpoint from the interval interior}}.

A function that {{is continuous on the interval $(-\infty, +\infty)$, i.e. $\mathbb{R}$}}, is _continuous everywhere_. It is also {{often simply called a continuous function}}. Sometimes, a function that {{is continuous on its [domain](domain%20of%20a%20function.md)}} is also called a continuous function. For example, {{[partial functions](partial%20function.md) that have a domain of all reals except at [isolated points](isolated%20point.md)}}, which are continuous in its domain. The partial functions are however {{not everywhere continuous}}. In {{contexts interested in the partial functions' behavior near exceptional points}}, they are called discontinuous functions instead, confusingly.

> [!tip] tips
>
> - [interior](interior%20(topology).md) of a real interval ::: For $a, b \in \mathbb{R}$, $(a, b)$ is the [interior](interior%20(topology).md) of $[a, b]$, $(a, b]$, $[a, b)$, and $(a, b)$.
> - relation of definitions between open intervals and semi-closed or closed intervals ::: One can interpret the definition for the semi-closed or closed interval differently. The function is continuous on an interval if the function is continuous on the corresponding open interval, and the endpoints $a$ satisfies $\lim_{x \to a^\pm} f(x) = f(a)$, choosing the direction such that the limit approaches the endpoint from the interval.

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :: It is continuous by [vacuous truth](vacuous%20truth.md). Interestingly, it is neither continuous nor discountinuous at every point.
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ :: It is continuous. Note that an isolated point is closed under usual definitions.

### discontinuity at a point

A function is _discontinuous_ function at a point {{if the point is in the [topological closure](closure%20(topology).md) of the [function domain](domain%20of%20a%20function.md), and either the point is not in the [function domain](domain%20of%20a%20function.md) or the function is not continuous at the point}}.

> [!tip] tips
>
> - neither continuous nor discountinuous ::: A function can be neither continuous nor discontinuous at a point. For example, $f(x > 0) = 0$ is neither continuous nor discontinuous at -1. It is however discontinuous at 0.
> - [topological closure](closure%20(topology).md) of a real interval ::: For $a, b \in \mathbb{R}$, $[a, b]$ is the [topological closure](closure%20(topology).md) of $(a, b)$, $[a, b)$, $(a, b]$, and $[a, b]$.

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :: It is not discontinuous at every point.
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ at $0$ :: It is not discontinuous at 0.
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $0$ :: It is not discontinuous at 0.
> - $f(x \in (0, +\infty)) = \sqrt{x}$ at $0$ :: It is discontinuous at 0.
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $-1$ :: It is not discontinuous at -1.

### definition in terms of limits of functions

A function $f$ is _continuous_ at a point $c$ {{if $$\lim_{x \to c} f(x) = f(c)$$ or $c$ is an [isolated point](isolated%20point.md) of $f$}}.

Note that for endpoints of the [function domain](domain%20of%20a%20function.md), {{the [limit](limit%20of%20a%20function.md) at the endpoints only requires approaching the endpoint from the domain}}. The part about [isolated point](isolated%20point.md) is needed because {{[limit](limit%20of%20A%20function.md) is not defined for isolated points}}.

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :: It is not continuous at every point.
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ at $0$ :: It is continuous at 0.
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $0$ :: It is continuous at 0.
> - $f(x \in (0, +\infty)) = \sqrt{x}$ at $0$ :: It is not continuous at 0.
> - $f(x \in [0, +\infty)) = \sqrt{x}$ at $-1$ :: It is not continuous at -1.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/continuous_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
