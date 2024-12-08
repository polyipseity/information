---
aliases:
  - independence Bayes
  - independence bayes
  - naive Bayes classifier
  - naive Bayes classifiers
  - naive bayes classifier
  - naive bayes classifiers
  - simple Bayes
  - simple bayes
tags:
  - flashcard/active/general/naive_Bayes_classifier
  - language/in/English
---

# naive Bayes classifier

## probabilistic model

Abstractly, naive Bayes classifier is {@{a [conditional probability](conditional%20probability.md) model}@}. The problem to be solved is: Given a sample with {@{$n$ features ($n$ inputs)}@}, assign {@{the conditional probability of the sample belonging to a class (1 output) for each of the $K$ possible classes}@}. The $n$ inputs are represented by {@{a vector $\mathbf{x} = (x_1, \ldots, x_n)$}@}. The $k$-th class of the $K$ possible classes is represented by {@{$C_k$}@}. Then the conditional probability is mathematically {@{$p(C_k \mid \mathbf{x})$}@}. <!--SR:!2025-04-13,213,310!2025-06-02,271,330!2025-09-20,308,290!2025-05-26,265,330!2025-06-17,282,330!2025-02-05,173,310-->

Using {@{[Bayes' theorem](Bayes'%20theorem.md)}@}, the {@{required conditional probability}@} can be written as: {@{$$p(C_k \mid \mathbf{x}) = \frac {p(C_k) p(\mathbf{x} \mid C_k)} {p(\mathbf{x})}$$}@}. <!--SR:!2025-06-13,277,330!2025-01-25,164,310!2025-01-24,169,310-->

In plain English, {@{using [Bayesian probability](Bayesian%20probability.md) terminology}@}, the above equation is: {@{$$\text{posterior} = \frac {\text{prior} \times \text{likelihood} } {\text{evidence} }$$}@}. <!--SR:!2025-07-01,295,330!2026-04-08,494,310-->

In practice, there is only {@{interest in the numerator but not the denominator}@}, because {@{the denominator depends not on $C_k$ but only $\mathbf{x}$, and $\mathbf{x}$ is often given so it is effectively constant}@}. The numerator is {@{equivalent to the [joint probability](joint%20probability%20distribution.md) model}@}: {@{$$p(C_k) p(\mathbf{x} \mid C_k) = p\left(C_k \cap \left(\bigcap_{i = 1}^n x_i \right) \right) = p(C_k, x_1, \ldots, x_n)$$}@}. <!--SR:!2025-02-21,179,310!2025-03-09,182,270!2026-01-31,435,310!2026-01-28,431,310-->

The joint probability model can {@{be rewritten as follows, using the [chain rule](chain%20rule%20(probability).md) arising from repeated applications of the definition of [conditional probability](conditional%20probability.md)}@}: {@{$$\begin{aligned} p(C_k, x_1, \ldots, x_n) & = p(x_1, \ldots, x_n, C_k) \\ & = p(x_1 \mid x_2, \ldots, x_n, C_k) p(x_2, \ldots, x_n, C_k) \\ & = \cdots \\ & = p(x_1, \mid x_2, \ldots, x_n, C_k) p(x_2 \mid x_3, \ldots, x_n, C_k) \cdots p(x_n \mid C_k) p(C_k) \end{aligned}$$}@} <!--SR:!2025-01-16,150,310!2025-03-04,182,270-->

After rewriting the joint probability model, {@{the "naive" assumptions come into play: Assume that all features of $\mathbf{x}$ are [mutually independent](independence%20(probability%20theory).md), conditional on the class $C_k$}@}, written mathematically as: {@{$$p(x_i \mid x_{i + 1}, \ldots, x_n, C_k) = p(x_i \mid C_k)$$}@}. <!--SR:!2025-01-04,151,310!2025-01-11,152,310-->

With the assumption, the joint probability model can {@{be simplified}@}: {@{$$\begin{aligned} p(C_k \mid \mathbf{x}) & \propto p(C_k, x_1, \ldots, x_n) && (p(\mathbf{x}) = \text{const.}) \\ & = p(C_k) p(x_1 \mid C_k) p(x_2 \mid C_k) \cdots p(x_n \mid C_k) \\ & = p(C_k) \prod_{i = 1}^n p(x_i \mid C_k) \end{aligned}$$}@}. <!--SR:!2025-01-10,155,310!2025-05-21,223,270-->

To conclude, {@{with the above assumptions}@}, {@{the conditional probability of class $C_k$ given features $\mathbf{x}$}@} is: {@{$$p(C_k \mid \mathbf{x}) = \frac 1 Z p(C_k) \prod_{i = 1}^n p(x_i \mid C_k)$$}@}, where {@{$Z = p(\mathbf{x}) = \sum_k p(C_k) p(\mathbf{x} \mid C_k)$ is a scaling factor dependent on $\mathbf{x}$ only}@}. <!--SR:!2025-03-28,201,310!2024-12-13,131,290!2025-11-16,343,290!2025-04-28,207,270-->

The {@{prior for a given class, i.e. $p(C_k)$}@}, can be obtained from {@{the training dataset (empirical distribution)}@}, or {@{assumed equiprobable, i.e. $p(C_k) = \frac 1 K$}@}. For empirical distribution: {@{$$p(C_k) = \frac {\text{number of samples of class }C_k} {\text{number of samples} }$$}@}. <!--SR:!2025-06-19,282,330!2024-12-13,121,290!2025-05-04,248,330!2025-04-18,216,310-->

The {@{conditional probabilities of a feature having a specific value given a class, i.e. $p(x_i = v \mid C_k)$}@} required for calculations above can also be obtained from {@{the training dataset}@}. For discrete values: {@{$$p(x_i = v \mid C_k) = \frac {\text{number of samples of class }C_k\text{ and feature }x_i = v} {\text{number of samples of class }C_k}$$}@}, and for continuous values, {@{[Gaussian naive Bayes](#Gaussian%20naive%20Bayes)}@} is usually used. <!--SR:!2026-05-11,519,310!2024-12-24,130,290!2025-05-26,251,290!2025-06-12,278,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/naive_Bayes_classifier) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
