---
aliases:
  - limit
  - limit of a function
  - limits
  - limits of a function
tags:
  - flashcard/general/limit_of_a_function
  - language/in/English
---

# limit of a function

## functions of a single variable

### (ϵ,δ)-definition of limit

Let $f: \mathbb{R} \to \mathbb{R}$ be a [function](function%20(mathematics).md) defined on the [reals](real%20number.md). Let $p, L \in \mathbb{R}$ be two reals. One would say {{__the limit of $f$, as $x$ approaches $p$, is $L$<!-- LaTeX separator -->__, and written $$\lim_{x \to p} f(x) = L$$, or alternatively, __f(x)__ tends to $L$ as $x$ tends to $p$, and written $$f(x) \to L \text{ as } x \to p$$}}, if the following property holds: {{for every real $\epsilon > 0$, there exists real $\delta > 0$ such that for all real $x$, $0 < \lvert x - p \rvert < \delta$ implies $\lvert f(x) - L \rvert < \epsilon$, or symbolically $$(\forall \epsilon > 0)(\exists \delta > 0)(\forall x \in \mathbb{R})(0 < \lvert x - p \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon)$$}}. <!--SR:!2024-10-22,155,324!2024-12-08,192,324-->

The above definition requires $f$ to be defined on $\mathbb{R}$ and is too restrictive. A more general definition {{applies for [functions](function%20(mathematics).md) defined on [subsets](subset.md) of the [reals](real%20number.md)}}. Let $S \subseteq \mathbb{R}$. Let $f: S \to \mathbb{R}$ be a [real-valued function](real-valued%20function.md). {{If there exists a real open [interval](interval%20(mathematics).md) $(a, b)$ containing $p \in (a, b)$, such that $(a, p) \cup (p, b) \subseteq S$ is a subset of $S$}}, then {{the limit of $f(x)$ as $x$ approaches $p$ is $L$, if for every real $\epsilon > 0$, there exists real $\delta > 0$ such that for all $x \in (a, b)$, $0 < \lvert x - p \rvert < \delta$ implies $\lvert f(x) - L \rvert < \epsilon$, or symbolically $$(\forall \epsilon > 0)(\exists \delta > 0)(\forall x \in (a, b))(0 < \lvert x - p \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon)$$}}. By this definition, a limit can exist {{in $\set{p \in \mathbb{R} : (\exists (a, b) \subseteq \mathbb{R})(p \in (a, b) \land (a, p) \cup (p, b) \subseteq S)}$, which equals $\operatorname{int} S \cup \operatorname{iso} S^c$, where $\operatorname{int} S$ is the the [interior](interior%20(topology).md) of $S$ and $\operatorname{iso} S^c$ are the [isolated points](isolated%20point.md) of the [complement](complement%20(set%20theory).md) of $S$}}. <!--SR:!2025-02-27,271,344!2025-02-11,258,344!2025-01-05,213,324!2024-12-27,206,324-->

Note that the above definition is still too restrictive because {{the limits are not defined at endpoints of [function domains](domain%20of%20a%20function.md), like limits at $a$ and $b$ for $f: [a, b] \to \mathbb{R}$}}. We can obtain an even more general definition by {{using [limit points](accumulation%20point.md)}}. Let $f: S \to \mathbb{R}$ be a [real-valued function](real-valued%20function.md). {{Let $p$, that may or may not be in $S$, be a [limit point](limit%20point.md) of a [sequence](sequence.md) $(T_n)_{n \in \mathbb{N} }$ where $T_n \in S_{\ne p}$ — that is, $p$ is the limit of sequence $T$ in $S$ distinct from $p$}}. Then {{__the limit of $f$, as $x$ approaches $p$ from values in $T$, is $L$<!-- LaTeX separator -->__, and written: $$\lim_{x \to p \atop x \in T} f(x) = L$$}}, if the following holds: {{For every real $\epsilon > 0$, there exists a real $\delta > 0$ such that for all $x \in T$, $0 < \lvert x - p \rvert < \delta$ implies $\lvert f(x) - L \rvert < \epsilon$, or symbolically $$(\forall \epsilon > 0)(\exists \delta > 0)(\forall x \in T)(0 < \lvert x - p \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon)$$}}. Note that the limit {{may be different depending on the selection of $T$, such as the left-sided and right-sided limits at a discontinuous point of a function}}. Using this definition, a limit can exist {{in [limit points](accumulation%20point.md) of the [function domains](domain%20of%20a%20function.md), such as the endpoints of a semi-closed or closed interval, but not [isolated points](isolated%20point.md)}}. We use this definition in this article unless otherwise specified. <!--SR:!2025-01-15,236,344!2024-09-07,124,304!2024-11-06,163,304!2024-12-29,222,344!2024-07-13,84,284!2025-02-23,254,344!2025-02-20,266,344-->

> [!tip] tips
>
> - [complement](complement%20(set%20theory).md) of a real interval ::: For example, for $a, b \in \mathbb{R}$, $(-\infty, a] \cup (b, +\infty)$ is the [complement](complement%20(set%20theory).md) of $(a, b]$. <!--SR:!2025-04-15,316,364!2024-06-19,79,344-->
> - [interior](interior%20(topology).md) of a real interval ::: For $a, b \in \mathbb{R}$, $(a, b)$ is the [interior](interior%20(topology).md) of $[a, b]$, $(a, b]$, $[a, b)$, and $(a, b)$. <!--SR:!2024-06-26,86,344!2025-05-31,351,364-->
> - [isolated points](isolated%20point.md) of a [set](set%20(mathematics).md) containing [reals](real%20number.md) ::: For example, $\set{0, 2}$ are [isolated points](isolated%20point.md) of $(-\infty, -12) \cup \set{0} \cup [0.5, 1) \cup \set{2} \cup [2.1, 2.11]$. <!--SR:!2025-01-22,242,344!2025-04-21,321,364-->
> - motivation of not defining limits at [isolated points](isolated%20point.md) of the [function domain](domain%20of%20a%20function.md) ::: Limits are meant for describing the behavior of a function around a point, but not at the point itself. As an isolated point has no other points around it, so defining the limit there is useless. <!--SR:!2024-11-15,174,324!2024-06-16,76,344-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - empty function $\varnothing \to X$ :: It has no limit at every [real](real%20number.md). However, it has limit and it has no limit at every point in its [domain](domain%20of%20a%20function.md) by [vacuous truth](vacuous%20truth.md). <!--SR:!2025-02-25,269,344-->
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ :: It has no limit at every [real](real%20number.md), including $0$. <!--SR:!2025-06-04,354,364-->

### one-sided limits and existence

Note that the first two definitions above consider {{$x$ approaching from both sides}}. Alternatively, one can consider {{$x$ approaching $p$ from below (left) or above (right)}}, in which case the limits are respectively denoted as {{$$\lim_{x \to p^-} f(x) \quad \text{ or } \quad \lim_{x\,\uparrow\,p} f(x) \quad \text{ or } \quad \lim_{x \nearrow p} f(x) \quad \text{ or } \quad f(x-)$$ and $$\lim_{x \to p^+} f(x) \quad \text{ or } \quad \lim_{x\,\downarrow\,p} f(x) \quad \text{ or } \quad \lim_{x \searrow p} f(x) \quad \text{ or } \quad f(x+)$$}}. Such a limit is called {{_one-sided limit_}}. <!--SR:!2025-02-24,268,344!2025-01-04,227,344!2024-12-12,195,324!2025-05-22,343,364-->

The formal definitions for the above one-sided limits can be obtained by {{taking any of the above definition and replacing the implication antecedent $0 < \lvert x - p \rvert < \delta$ with respectively $0 < p - x < \delta$ and $0 < x - p < \delta$}}. Restated, the __limit of $f$ as $x$ approaches $p$ from below is $L$<!-- LaTeX separator -->__, if: {{For every real $\epsilon > 0$, there exists real $\delta > 0$ such that for all $x \in (a, b)$, $0 < p - x < \delta$ implies $\lvert f(x) - L \rvert < \epsilon$. $$(\forall \epsilon > 0)(\exists \delta > 0)(\forall x \in (a, b))(0 < p - x < \delta \implies \lvert f(x) - L \rvert < \epsilon)$$}}. The __limit of $f$ as $x$ approaches $p$ from above is $L$<!-- LaTeX separator -->__, if: {{For every real $\epsilon > 0$, there exists real $\delta > 0$ such that for all $x \in (a, b)$, $0 < x - p < \delta$ implies $\lvert f(x) - L \rvert < \epsilon$. $$(\forall \epsilon > 0)(\exists \delta > 0)(\forall x \in (a, b))(0 < x - p < \delta \implies \lvert f(x) - L \rvert < \epsilon)$$}}. For the third definition, {{the above replacement is unnecessary as the sequence $T$ can be selected such that it contains reals from one side only, and define this to be the one-sided limit}}. <!--SR:!2024-12-26,205,324!2024-09-10,127,304!2024-07-05,79,284!2024-11-04,167,324-->

The _two-sided limit_ exists at a point if {{the two one-sided limits exist and equal each other}}. By convention, the _limit_, without any adjectives, exists at a point {{for endpoints of the [function domains](domain%20of%20a%20function.md), if one of the one-sided limit exist, and for other points, if the two-sided limit exists}}. A less common definition is the _limit_ exists {{if the two-sided limit exists regardless if the point is an endpoint}}. The former definition is {{more aligned with even further generalized definitions of the limit as it only considers points within the [function domains](domain%20of%20a%20function.md)}}. We will use this definition in the article. <!--SR:!2024-08-16,108,304!2024-12-09,209,344!2025-02-05,240,344!2024-10-06,151,324-->

If the limit does not exist, then {{the [oscillation](oscillation%20(mathematics).md#oscillation%20of%20a%20function%20at%20a%20point) of $f$ at $p$ is nonzero}}. <!--SR:!2025-04-25,321,364-->

> [!example] examples
>
> - function at an [isolated point](isolated%20point.md): $f(x \in \set{0}) = 0$ :: It has no one-sided limits at every [real](real%20number.md), including $0$. <!--SR:!2025-01-23,243,344-->

### examples

#### non-existence of one-sided limit(s)

The {{[Dirichlet function](Dirichlet%20function.md): $$f(x) = \begin{cases} 1 & x\text{ rational} \\ 0 & x\text{ irrational} \end{cases}$$}} has no limit at every [real](real%20number.md). <!--SR:!2025-04-09,311,364-->

#### non-equality of one-sided limits

The function {{$$f(x) = \begin{cases} 1 & x \ge 0 \\ -1 & x < 0 \end{cases}$$}} has a limit at every nonzero $x$. It has no limit at $0$. <!--SR:!2025-04-04,307,364-->

#### limits at only one point

The functions {{$$f(x) = \begin{cases} x & x\text{ rational} \\ 0 & x\text{ irrational} \end{cases}$$ and $$f(x) = \begin{cases} \lvert x \rvert & x\text{ rational} \\ 0 & x\text{ irrational} \end{cases}$$}} both have a limit at $x = 0$ and equals $0$, but not anywhere else. <!--SR:!2025-02-20,265,344-->

#### limits at countably many points

The function {{$$f(x) = \begin{cases} \cos x & x\text{ rational} \\ 1 & x\text{ irrational} \end{cases}$$}} has a limit that equals 1 at every $x = 2n \pi$, where $n$ is any integer. <!--SR:!2024-07-07,79,284-->

## properties

### algebraic limit theorem

The __algebraic limit theorem__ states that {{for [real](real%20number.md) or [complex](complex%20number.md)-valued functions $f(x)$ and $g(x)$, the limit of an operation on $f(x)$ and $g(x)$, i.e. $f(x) + g(x)$, $f(x) - g(x)$, $f(x) \cdot g(x)$, $f(x) / g(x)$, and ${f(x)}^{g(x)}$, is compatible with the same operation on the limits of $f(x)$ and $g(x)$ under some conditions}}. <!--SR:!2024-11-25,269,330-->

> __algebraic limit theorem__
>
> Also valid for one-sided limits and limits at infinity.
>
> - condition ::: $x$ is [real](real%20number.md) or [complex](complex%20number). Limits on the right side of the equations exist or are in [determinate form](#determinate%20forms). <!--SR:!2024-12-23,291,330!2025-02-17,263,344-->
> - addition ::: $\lim_{x \to p} (f(x) + g(x)) = \lim_{x \to p} f(x) + \lim_{x \to p} g(x)$ <!--SR:!2024-11-03,252,330!2025-01-06,232,344-->
> - subtraction ::: $\lim_{x \to p} (f(x) - g(x)) = \lim_{x \to p} f(x) - \lim_{x \to p} g(x)$ <!--SR:!2024-09-26,222,330!2025-05-23,344,364-->
> - multiplication ::: $\lim_{x \to p} (f(x) \cdot g(x)) = \lim_{x \to p} f(x) \cdot \lim_{x \to p} g(x)$ <!--SR:!2024-10-12,235,330!2024-10-16,154,324-->
> - division ::: $\lim_{x \to p} (f(x) / g(x)) = \lim_{x \to p} f(x) / \lim_{x \to p} g(x)\qquad(\lim_{x \to p} g(x) \ne 0)$ <!--SR:!2025-08-28,466,310!2025-05-02,330,364-->
> - exponentiation ::: $\lim_{x \to p} {f(x)}^{g(x)} = \lim_{x \to p} f(x)^{\lim_{x \to p} g(x)}\qquad(\lim_{x \to p} f(x) > 0 \text{ or } (\lim_{x \to p} f(x) = 0, 0 < \lim_{x \to p} g(x) < +\infty))$  (If only [real](real%20number.md) $x$ is considered, the base, if it approaches 0, must approach it from the positive.) <!--SR:!2024-07-07,129,250!2025-01-14,235,344-->

#### determinate forms

- see: [extended real number line](extended%20real%20number%20line.md), [indeterminate form](indeterminate%20form.md)

When the limit on the right of the equation does not exist but are in the following determinate forms, {{it can still be determined by the following rules}}. In other cases, the limit on the left exists, but {{the limit on the right is in [indeterminate form](indeterminate%20form.md) that does not allow direct calculation, in which case [L'Hôpital's rule](L'Hôpital's%20rule.md) may be used to determinate the limit}}. <!--SR:!2024-09-09,209,330!2024-08-05,176,310-->

> __determinate forms__
>
> - {{$L + \infty = \infty \quad \text{if } q \ne -\infty$}}
> - {{$L \cdot \infty = \begin{cases} \infty & \text{if } q > 0 \\ -\infty & \text{if } q < 0 \end{cases}$}}
> - {{$\frac{q}\infty = 0 \quad \text{if } q \ne \infty \text{ and } q \ne -\infty$}}
> - {{$\infty^q = \begin{cases} 0 & \text{if } q < 0 \\ \infty & \text{if } q > 0 \end{cases}$}}
> - {{$q^\infty = \begin{cases} 0 & \text{if } 0 < q < 1 \\ \infty & \text{if } q > 1 \end{cases}$}}
> - {{$q^{-\infty} = \begin{cases} \infty & \text{if } 0 < q < 1 \\ 0 & \text{if } q > 1 \end{cases}$}} <!--SR:!2024-06-24,148,310!2025-11-05,511,310!2025-06-14,391,290!2024-07-29,150,270!2025-01-27,275,290!2024-06-23,104,310-->

### limits of compositions of functions

In general, $\lim_{x \to G} f(x) = F$ and $\lim_{x \to a} g(x) = G$ {{does not imply $\lim_{x \to a} f(g(x)) = F$ unless either $f$ is continuous at $G$ (i.e. $f(G) = F$) or $g$ is defined and does not equal $G$ near $a$ (i.e. $(\exists \delta > 0)(\forall{x} \in \operatorname{domain} g)(0 < \lvert x - a \rvert < \delta \implies \lvert g(x) - G \rvert > 0)$)}}. <!--SR:!2024-06-22,119,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/limit_of_a_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
