---
aliases:
  - integration by substitution
tags:
  - flashcard/active/general/eng/integration_by_substitution
  - language/in/English
---

# integration by substitution

## substitution for a single variable

### statement for definite integrals

1. conditions ::@:: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $f$ is [continuous](continuous%20function.md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md).<!-- flashcard 966534dc-acbf-4b1b-a0b1-acf81b151ca0 --> <!--SR:!2024-12-31,220,321!2024-12-30,208,321-->
2. result ::@:: $$\int_a^b \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int_{g(a)}^{g(b)} \! f(u) \,\mathrm{d}u$$ <!--SR:!2025-03-26,291,330!2026-10-04,714,330-->

### statement for indefinite integrals

1. conditions ::@:: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $f$ is [continuous](continuous%20function.md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md).<!-- flashcard 0f7756e3-85b4-48d0-a619-7d8062b916e1 --> <!--SR:!2025-01-12,169,274!2026-01-10,437,314-->
2. result ::@:: $$\int \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int \! f(u) \,\mathrm{d}u \qquad u := g(x), x \in [a, b]$$ <!--SR:!2025-10-22,426,310!2026-08-10,604,310-->

### proof

Integration by substitution can be derived from {@{the [fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}@}. <!--SR:!2025-03-23,243,334-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/integration_by_substitution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
