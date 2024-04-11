---
aliases:
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

### construction of integrable functions

The set of Riemann integrable function is closed under {{addition, subtraction, multiplication; and reciprocal and division provided that $\inf \lvert g \rvert > 0$}}. That is, given two integrable functions $f, g: D \subseteq \mathbb{R} \to \mathbb{R}$, {{$f + g$, $f - g$, $f \cdot g$ are integrable in $D$, and $1 / g$ and $f / g$ are integrable in $D \setminus \set{x: \liminf_{x' \to x} \lvert g(x') \rvert > 0}$}}. The [converse](converse%20(logic).md) {{is not necessarily true, however}}. For example, {{given a non-integrable [real-valued function](real-valued%20function.md) $f$, $f + (-f) = f - f = 0$, $f \cdot f^{-1} = f / f = 1$ are integrable, so the antecedent and the consequent cannot be swapped}}. The above is somewhat similar to {{[the construction of continuous functions](continuous%20function.md#construction%20of%20continuous%20functions)}}. <!--SR:!2024-04-16,4,270!2024-04-16,4,270!2024-04-16,4,270!2024-04-16,4,270!2024-04-16,4,270-->

Apart from basic arithmetic operations, the set of continuous functions is also closed under {{[absolute value](absolute%20value.md)}}. That is, {{given an integrable function $f: D \subseteq \mathbb{R} \to \mathbb{R}$, $\lvert f \rvert$ is integrable}}. <!--SR:!2024-04-16,4,270!2024-04-16,4,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Riemann_integral) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
