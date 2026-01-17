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

1. conditions <!-- flashcard ID: 966534dc-acbf-4b1b-a0b1-acf81b151ca0 -->::@:: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $f$ is [continuous](continuous%20function.md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md). <!--SR:!2026-07-28,462,321!2026-10-29,668,321-->
2. result ::@:: $$\int_a^b \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int_{g(a)}^{g(b)} \! f(u) \,\mathrm{d}u$$ <!--SR:!2028-11-09,1324,350!2026-10-04,714,330-->

### statement for indefinite integrals

1. conditions <!-- flashcard ID: 0f7756e3-85b4-48d0-a619-7d8062b916e1 -->::@:: Let $g: [a, b] \to I, f: I \to \mathbb{R}$. $I \subseteq \mathbb{R}$ is a real [interval](interval%20(mathematics).md). $f$ is [continuous](continuous%20function.md). $g$ is [differentiable](differentiable%20function.md) and $g'$ is [integrable](integral.md). <!--SR:!2026-04-20,463,274!2029-10-21,1375,314-->
2. result ::@:: $$\int \! f(g(x)) \cdot g'(x) \,\mathrm{d}x = \int \! f(u) \,\mathrm{d}u \qquad u := g(x), x \in [a, b]$$ <!--SR:!2030-10-25,1829,330!2026-08-10,604,310-->

### proof

Integration by substitution can be derived from {@{the [fundamental theorem of calculus](fundamental%20theorem%20of%20calculus.md)}@}. <!--SR:!2028-04-15,1119,354-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/integration_by_substitution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
