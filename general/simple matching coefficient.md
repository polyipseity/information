---
aliases:
  - SMC
  - Rand coefficient
  - Rand coefficients
  - Rand similarity
  - Rand similarity coefficient
  - Rand similarity coefficients
  - matching coefficient
  - matching coefficients
  - simple matching coefficient
  - simple matching coefficients
tags:
  - flashcard/active/general/simple_matching_coefficient
  - language/in/English
---

# simple matching coefficient

{@{Two objects, _A_ and _B_, each with _n_ [binary](binary%20number.md) attributes}@} are given. Define: <!--SR:!2025-05-18,261,330-->

- $M_{00}$ ::@:: number of attributes where _A_ has value 0 and _B_ has value 0 <!--SR:!2025-05-21,261,330!2025-04-25,241,330-->
- $M_{01}$ ::@:: number of attributes where _A_ has value 0 and _B_ has value 1 <!--SR:!2025-06-23,286,330!2025-06-29,291,330-->
- $M_{10}$ ::@:: number of attributes where _A_ has value 1 and _B_ has value 0 <!--SR:!2025-03-12,205,330!2025-05-25,263,330-->
- $M_{11}$ ::@:: number of attributes where _A_ has value 1 and _B_ has value 1 <!--SR:!2025-05-21,260,330!2025-05-30,267,330-->

The simple matching coefficient is defined as {@{$$\text{SMC} = \frac {\text{number of matching attributes} } {\text{number of attributes} } = \frac {M_{00} + M_{11} } {M_{00} + M_{01} + M_{10} + M_{11} }$$}@}. <!--SR:!2025-01-31,162,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/simple_matching_coefficient) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
