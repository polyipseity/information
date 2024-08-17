---
aliases:
  - Bayes theorem
  - Bayes' theorem
tags:
  - flashcard/active/general/Bayes__theorem
  - language/in/English
---

# Bayes' theorem

## statement of theorem

Bayes' theorem is stated mathematically: {{$$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) > 0$$}} where {{$A$ and $B$ are [events](event%20(probability%20theory).md)}}. Further:

- $P(A \mid B)$ ::: [conditional probability](conditional%20probability.md) of $A$ happening given $B$ is true; also known as [posterior probability](posterior%20probability.md) of $A$ given $B$
- $P(B \mid A)$ ::: [conditional probability](conditional%20probability.md) of $B$ happening given $A$ is true; also known as [likelihood](likelihood%20function.md) of $A$ given $B$ because $P(B \mid A) = L(A \mid B)$
- $P(A)$ ::: [prior probability](prior%20probability.md)
- $P(B)$ ::: [marginal likelihood](marginal%20likelihood.md) or evidence

## generalizations

### Bayes' theorem for 3 events

A version of Bayes' theorem for 3 events {{results from the addition of a 3rd event $C$ (or more events if $C$ is composed from multiple events, such as $C = X \cap Y$) called the _context_, with $P(C) > 0$}}, on which {{all probabilities are conditioned}}:

$$P(A \mid B \cap C) = \frac {P(B \mid A \cap C) P(A \mid C)} {P(B \mid C)}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bayes'_theorem) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
