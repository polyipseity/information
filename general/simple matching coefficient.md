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
  - flashcard/general/simple_matching_coefficient
  - language/in/English
---

# simple matching coefficient

{{Two objects, _A_ and _B_, each with _n_ [binary](binary%20number.md) attributes}} are given. Define: <!--SR:!2024-07-02,14,290-->

- $M_{00}$ ::: number of attributes where _A_ has value 0 and _B_ has value 0 <!--SR:!2024-07-03,15,290!2024-07-02,14,290-->
- $M_{01}$ ::: number of attributes where _A_ has value 0 and _B_ has value 1 <!--SR:!2024-07-05,17,290!2024-07-05,17,290-->
- $M_{10}$ ::: number of attributes where _A_ has value 1 and _B_ has value 0 <!--SR:!2024-07-01,13,290!2024-07-04,16,290-->
- $M_{11}$ ::: number of attributes where _A_ has value 1 and _B_ has value 1 <!--SR:!2024-07-03,15,290!2024-07-04,16,290-->

The simple matching coefficient is defined as {{$$\text{SMC} = \frac {\text{number of matching attributes} } {\text{number of attributes} } = \frac {M_{00} + M_{11} } {M_{00} + M_{01} + M_{10} + M_{11} }$$}}. <!--SR:!2024-07-01,13,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/simple_matching_coefficient) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
