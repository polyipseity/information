---
aliases:
  - chain rule
  - chain rule for probability
  - chain rules
  - chain rules for probability
tags:
  - flashcard/general/chain_rule__probability_
  - language/in/English
---

# chain rule

## chain rule for events

### two events

For two [events](event%20(probability%20theory).md) $A$ and $B$ such that {{$\mathbb P(A) > 0$}}, the chain rule states that: {{$$\mathbb P(A \cap B) = \mathbb P(B \mid A) \mathbb P(A)$$}}, which can be proved easily from {{the [definition of conditional probability](conditional%20probability.md#Kolmogorov%20definition)}}. <!--SR:!2024-06-29,12,270!2024-07-02,14,290!2024-07-05,17,290-->

### finitely many events

For {{finitely many}} events $A_1, \ldots, A_n$ whose {{intersection has not probability zero}}, the chain rule states that: {{$$\begin{aligned} \mathbb P(A_1 \cap \ldots \cap A_n) & = \mathbb P(A_1 \cap \ldots \cap A_{n - 1}) \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \mathbb P(A_1) \mathbb P(A_2 \mid A_1) \ldots \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \prod_{k = 1}^n \mathbb P(A_k \mid A_1 \cap \ldots A_{k - 1}) \\ & = \prod_{k = 1}^n \mathbb P\left(A_k \,\Bigg|\, \bigcap_{j = 1}^{k - 1} A_j \right) \end{aligned}$$}}, which results from {{repeated application of the [chain rule for two events](#two%20events)}}. <!--SR:!2024-06-28,11,270!2024-07-01,13,290!2024-06-25,8,250!2024-07-03,15,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/chain_rule_(probability)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
