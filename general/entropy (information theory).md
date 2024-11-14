---
aliases:
  - Shannon entropy
  - entropy
  - information entropy
  - informational entropy
tags:
  - flashcard/active/general/statistical_classification
  - language/in/English
---

# entropy

In [information theory](information%20entropy.md), the __entropy__ {@{of a [random variable](random%20variable.md) is the weighted average of "information", "surprise", or "uncertainty" to the variable's outcomes}@}. Given {@{a discrete random variable $X$ that takes values in the alphabet $\mathcal X$, and is distributed according to a probability function $p: \mathcal X \to [0, 1]$}@}, the entropy is defined as {@{$$\Eta(X) := -\sum_{x \in \mathcal X} p(x) \log p(x)$$}@}. The choice of base of $\log$, the [logarithm](logarithm.md) {@{can be chosen according to the application. It is usually base 2, base [_e_](Euler's%20number.md), or base 10}@}. The different bases respectively give {@{the units of [bits](bit.md), [nats](nat%20(unit).md), and [dits](hartley%20(unit).md)}@}. When an outcome {@{has a probability of 0, its entropy is 0 by taking the following limit: $\lim_{x \to 0^+} -p(x) \log p(x) = 0$}@}. <!--SR:!2024-12-05,175,310!2026-02-09,495,310!2024-11-16,160,310!2024-12-09,167,310!2026-08-28,665,330!2025-10-04,359,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/entropy_(information_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
