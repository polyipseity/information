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

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [continuously differentiable](differentiable%20function.md). $f$ is [continuous](continuous%20function.md). <!--SR:!2024-04-02,18,301!2024-03-30,15,301-->
2. result ::: $$\int_a^b \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int_{g(a)}^{g(b)} \! f(u) \,\mathrm{d}u$$ <!--SR:!2024-03-30,17,290!2024-03-27,14,290-->

### statement for indefinite integrals

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [continuously differentiable](differentiable%20function.md). $f$ is [continuous](continuous%20function.md).
2. result ::: $$\int \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int \! f(u) \,\mathrm{d}u \qquad u := g(x), x \in [a, b]$$ <!--SR:!2024-03-27,14,290!2024-03-29,16,290-->

### proof

Integration by substitution can be derived from {{the [fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}}. <!--SR:!2024-05-02,37,290-->

1. conditions ::: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md) on $[a, b]$. $f$ is [continuous](continuous%20function.md). <!--SR:!2024-04-18,28,270!2024-03-27,14,290-->
2. existence of integrals ::: <!--SR:!2024-03-28,15,290!2024-04-21,27,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/integration_by_substitution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
