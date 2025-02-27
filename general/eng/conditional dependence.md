---
aliases:
  - conditional dependence
  - conditional dependent
tags:
  - flashcard/active/general/eng/conditional_dependence
  - language/in/English
---

# conditional dependence

- see: [conditional independence](conditional%20independence.md)

For example, if $A$ and $B$ are {@{two events that do not affect each other, and increases the probability of event $C$}@}, then {@{when $C$ is not observed}@}: {@{$$P(A \mid B) = P(A) \quad \text{ and } \quad P(B \mid A) = P(B)$$, i.e. $A$ and $B$ are [independent](independence%20(probability%20theory).md)}@}. <!--SR:!2026-02-04,421,313!2027-01-14,719,333!2025-07-25,313,330-->

Now suppose {@{$C$ is observed to occur}@}. If {@{event $B$ occurs, then the probability of event $A$ decreases because there is less need for event $A$ to explain event $C$ happening}@}, and vice versa. So now, the two events $A$ and $B$ {@{are negatively dependent on each other if the other occurs, given $C$}@}: {@{$$P(A \mid C \cap B) < P(A \mid C) \quad \text{ and } \quad P(B \mid C \cap A) < P(B \mid C)$$}@}. This is called {@{the conditional dependence of $A$ and $B$ given $C$}@}. <!--SR:!2026-05-10,509,313!2025-12-29,410,310!2026-09-03,618,330!2025-03-02,188,290!2025-07-28,315,333-->

Conditional dependence of $A$ and $B$ given $C$ is the logical negation of {@{[conditional independence](conditional%20independence.md) $(A \mathrel{\perp\!\!\!\perp} B \mid C)$}@}, in which the two events {@{do not affect the probability of each other given the occurrence of a third event}@}: {@{$$P(A \mid C \cap B) = P(A \mid C) \quad \text{ and } \quad P(B \mid C \cap A) = P(B \mid C)$$}@}. <!--SR:!2026-09-11,561,310!2026-09-18,630,333!2026-07-22,586,333-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conditional_dependence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
