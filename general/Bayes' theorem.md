---
aliases:
  - Bayes theorem
  - Bayes' theorem
tags:
  - flashcard/general/Bayes__theorem
  - language/in/English
---

# Bayes' theorem

## statement of theorem

Bayes' theorem is stated mathematically: {{$$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) > 0$$}} where {{$A$ and $B$ are [events](event%20(probability%20theory).md)}}. Further: <!--SR:!2024-07-03,15,294!2024-07-04,16,290-->

- $P(A \mid B)$ ::: [conditional probability](conditional%20probability.md) of $A$ happening given $B$ is true; also known as [posterior probability](posterior%20probability.md) of $A$ given $B$ <!--SR:!2024-07-17,22,254!2024-07-13,20,274-->
- $P(B \mid A)$ ::: [conditional probability](conditional%20probability.md) of $B$ happening given $A$ is true; also known as [likelihood](likelihood%20function.md) of $A$ given $B$ because $P(B \mid A) = L(A \mid B)$ <!--SR:!2024-07-14,19,254!2024-07-12,19,274-->
- $P(A)$ ::: [prior probability](prior%20probability.md) <!--SR:!2024-07-02,14,294!2024-07-04,16,294-->
- $P(B)$ ::: [marginal likelihood](marginal%20likelihood.md) or evidence <!--SR:!2024-08-10,43,294!2024-07-01,13,294-->

## generalizations

### Bayes' theorem for 3 events

A version of Bayes' theorem for 3 events {{results from the addition of a 3rd event $C$ (or more events if $C$ is composed from multiple events, such as $C = X \cap Y$) called the _context_, with $P(C) > 0$}}, on which {{all probabilities are conditioned}}: <!--SR:!2024-06-30,13,274!2024-07-05,17,290-->

$$P(A \mid B \cap C) = \frac {P(B \mid A \cap C) P(A \mid C)} {P(B \mid C)}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bayes'_theorem) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
