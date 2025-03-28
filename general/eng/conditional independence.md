---
aliases:
  - conditional independence
  - conditional independent
tags:
  - flashcard/active/general/eng/conditional_independence
  - language/in/English
---

# conditional independence

- see: [conditional dependence](conditional%20dependence.md)

## conditional independence of events

Let $A$, $B$, and $C$ be [events](event%20(probability%20theory).md). $A$ and $B$ are said to be {@{__conditionally independent__ given $C$}@} iff {@{$P(C) > 0$}@} and: {@{$$P(A \mid B, C) = P(A \mid C)$$}@}. This property is also written as {@{$(A \mathrel{\perp\!\!\!\perp} B \mid C)$}@}. Note that this formulation {@{unnecessarily require $P(B, C) > 0$, which is resolved by the alternate formulation below}@}.

Equivalently, conditional independence may be stated as: {@{$$P(A, B \mid C) = P(A \mid C) P(B \mid C)$$}@} where {@{$P(A, B \mid C)$ is the [joint probability](joint%20probability%20distribution.md) given $C$}@}. This alternate formulation states that {@{$A$ and $B$ are [independent events](independence%20(probability%20theory).md) given $C$}@}. Note that it does not {@{require $P(B, C) > 0$}@}. It also demonstrates that {@{$(A \mathrel{\perp\!\!\!\perp} B \mid C)$ is equivalent to $(B \mathrel{\perp\!\!\!\perp} A \mid C)$}@}.

### proof of the equivalent definition

The strategy is {@{decomposing both expressions using [the definition of conditional probability](conditional%20probability.md#Kolmogorov%20definition) and perform basic algebraic manipulation}@}. Assuming {@{$P(C) > 0$ and $P(B, C) > 0$}@}:

$$\begin{aligned}
& \phantom \iff P(A, B \mid C) = P(A \mid C) P(B \mid C) \\
& \iff \frac {P(A, B, C)} {P(C)} = \left( \frac {P(A, C)} {P(C)} \right) \left( \frac {P(B, C)} {P(C)} \right) && (\text{definition of conditional probability}) \\
& \iff P(A, B, C) = \frac {P(A, C) P(B, C)} {P(C)} && (\text{multiply both sides by }P(C) > 0) \\
& \iff \frac {P(A, B, C)} {P(B, C)} = \frac {P(A, C)} {P(C)} && (\text{divide both sides by }P(B, C) > 0) \\
& \iff P(A \mid B, C) = P(A \mid C) && (\text{definition of conditional probability})
\end{aligned}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conditional_independence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
