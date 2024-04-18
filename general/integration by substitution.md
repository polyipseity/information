---
aliases:
  - integration by substitution
tags:
  - flashcard/general/integration_by_substitution
  - language/in/English
---

# integration by substitution

## substitution for a single variable

### statement for definite integrals

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [continuously differentiable](differentiable%20function.md). $f$ is [continuous](continuous%20function.md). <!--SR:!2024-05-25,53,301!2024-06-05,65,321-->
2. result ::: $$\int_a^b \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int_{g(a)}^{g(b)} \! f(u) \,\mathrm{d}u$$ <!--SR:!2024-06-08,68,310!2024-05-11,40,290-->

### statement for indefinite integrals

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [continuously differentiable](differentiable%20function.md). $f$ is [continuous](continuous%20function.md).
2. result ::: $$\int \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int \! f(u) \,\mathrm{d}u \qquad u := g(x), x \in [a, b]$$ <!--SR:!2024-05-08,37,290!2024-06-03,63,310-->

### proof

Integration by substitution can be derived from {{the [fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}}. <!--SR:!2024-05-02,37,290-->

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md) on $[a, b]$. $f$ is [continuous](continuous%20function.md). <!--SR:!2024-07-01,74,270!2024-05-13,42,290-->
2. existence of integrals ::: <!--SR:!2024-05-14,43,290!2024-04-21,27,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/integration_by_substitution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
