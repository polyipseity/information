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

> __limit of a function__
>
> For {{$p,L\in\mathbb{R}$, $S\subseteq\mathbb{R}$, and $f:S\to\mathbb{R}$, if $(\forall\epsilon>0)(\exists\delta>0)(\forall{x}\in{S})(0<\lvert{x-p}\rvert<\delta\implies\lvert{f(x)-L}\rvert<\epsilon)$, then $\lim_{x\to{}p}f(x)$ exists and equals $L$.}} <!--SR:!2024-06-04,109,250-->

## properties

### algebraic limit theorem

The __algebraic limit theorem__ states that {{for [real](real%20number.md) or [complex](complex%20number.md)-valued functions $f(x)$ and $g(x)$, the limit of an operation on $f(x)$ and $g(x)$, i.e. $f(x) + g(x)$, $f(x) - g(x)$, $f(x) \cdot g(x)$, $f(x) / g(x)$, and ${f(x)}^{g(x)}$, is compatible with the same operation on the limits of $f(x)$ and $g(x)$ under some conditions}}. <!--SR:!2024-03-01,63,310-->

> __algebraic limit theorem__
> Also valid for one-sided limits and limits at infinity.
>
> - main condition: {{limit on the right side of the equations exist or is in [determinate form](#determinate%20forms)}}
> - {{$\lim_{x \to p} (f(x) + g(x)) = \lim_{x \to p} f(x) + \lim_{x \to p} g(x)$}}
> - {{$\lim_{x \to p} (f(x) - g(x)) = \lim_{x \to p} f(x) - \lim_{x \to p} g(x)$}}
> - {{$\lim_{x \to p} (f(x) \cdot g(x)) = \lim_{x \to p} f(x) \cdot \lim_{x \to p} g(x)$}}
> - {{$\lim_{x \to p} (f(x) / g(x)) = \lim_{x \to p} f(x) / \lim_{x \to p} g(x)\qquad(\lim_{x \to p} g(x) \ne 0)$}}
> - {{$\lim_{x \to p} {f(x)}^{g(x)} = \lim_{x \to p} f(x)^{\lim_{x \to p} g(x)}\qquad(\lim_{x \to p} f(x) > 0 \text{ or } (\lim_{x \to p} f(x) = 0, \lim_{x \to p} g(x) > 0))$}} <!--SR:!2024-03-07,68,310!2024-11-03,252,330!2024-09-26,222,330!2024-10-12,235,330!2024-05-19,116,290!2024-07-07,129,250-->

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
> - {{$q^{-\infty} = \begin{cases} \infty & \text{if } 0 < q < 1 \\ 0 & \text{if } q > 1 \end{cases}$}} <!--SR:!2024-06-24,148,310!2024-06-12,127,290!2024-05-19,104,270!2024-03-01,56,270!2024-04-27,95,290!2024-03-11,26,290-->

### limits of compositions of functions

In general, $\lim_{x \to G} f(x) = F$ and $\lim_{x \to a} g(x) = G$ {{does not imply $\lim_{x \to a} f(g(x)) = F$ unless either $f$ is continuous at $G$ (i.e. $f(G) = F$) or $g$ is defined and does not equals to $G$ near $a$ (i.e. $(\exists \delta > 0)(\forall{x}\in\mathbb{R})(0 < \lvert{x - a}\rvert < \delta \implies \lvert{g(x) - G}\rvert > 0)$)}}. <!--SR:!2024-06-22,119,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/limit_of_a_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
