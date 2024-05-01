---
aliases:
  - Lebesgue-Vitali theorem
  - Lebesgue-Vitali theorem of characterization of the Riemann integrable functions
  - Riemann integrability
  - Riemann integrable
  - Riemann integral
  - Riemann integrals
tags:
  - flashcard/general/Riemann_integral
  - language/in/English
---

# Riemann integral

## integrability

{{A [bounded function](bounded%20function.md) on a [compact interval](compact%20space.md) (closed and bounded interval)}} is Riemann integrable {{[iff](if%20and%20only%20if.md) it is continuous [almost everywhere](almost%20everywhere.md) (its points of [discontinuity](classification%20of%20discontinuities.md) has [measure zero](null%20set.md), in terms of [Lebesgue measure](Lebesgue%20measure.md))}}. This is known as the {{__Lebesgue-Vitali theorem__}} (of characterization of the Riemann integrable functions). <!--SR:!2024-05-04,10,281!2024-05-13,14,261!2024-05-19,19,261-->

### construction of integrable functions

The set of Riemann integrable function is closed under {{addition, subtraction, multiplication; and reciprocal and division provided that $\inf \lvert g \rvert > 0$}}. That is, given two integrable functions $f, g: D \subseteq \mathbb{R} \to \mathbb{R}$, {{$f + g$, $f - g$, $f \cdot g$ are integrable in $D$, and $1 / g$ and $f / g$ are integrable in $D \setminus \set{x: \liminf_{x' \to x} \lvert g(x') \rvert > 0}$}}. The [converse](converse%20(logic).md) {{is not necessarily true, however}}. For example, {{given a non-integrable [real-valued function](real-valued%20function.md) $f$, $f + (-f) = f - f = 0$, $f \cdot f^{-1} = f / f = 1$ are integrable. So the antecedent and the consequent cannot be swapped}}. The above is somewhat similar to {{[the construction of continuous functions](continuous%20function.md#construction%20of%20continuous%20functions)}}. <!--SR:!2024-05-23,26,270!2024-06-08,41,290!2024-05-17,22,270!2024-06-11,41,290!2024-06-11,44,290-->

Apart from basic arithmetic operations, the set of continuous functions is also closed under {{[absolute value](absolute%20value.md)}}. That is, {{given an integrable function $f: D \subseteq \mathbb{R} \to \mathbb{R}$, $\lvert f \rvert$ is integrable}}. <!--SR:!2024-06-04,38,290!2024-06-05,39,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Riemann_integral) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
