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
  - flashcard/active/general/eng/naive_Bayes_classifier
  - language/in/English
---

# naive Bayes classifier

## probabilistic model

Abstractly, naive Bayes classifier is {@{a [conditional probability](conditional%20probability.md) model}@}. The problem to be solved is: Given a sample with {@{$n$ features ($n$ inputs)}@}, assign {@{the conditional probability of the sample belonging to a class (1 output) for each of the $K$ possible classes}@}. The $n$ inputs are represented by {@{a vector $\mathbf{x} = (x_1, \ldots, x_n)$}@}. The $k$-th class of the $K$ possible classes is represented by {@{$C_k$}@}. Then the conditional probability is mathematically {@{$p(C_k \mid \mathbf{x})$}@}. <!--SR:!2027-10-14,914,330!2028-10-20,1236,350!2029-02-12,1241,310!2028-09-17,1210,350!2028-12-22,1284,350!2027-02-17,742,330-->

Using {@{[Bayes' theorem](Bayes'%20theorem.md)}@}, the {@{required conditional probability}@} can be written as: {@{$$p(C_k \mid \mathbf{x}) = \frac {p(C_k) p(\mathbf{x} \mid C_k)} {p(\mathbf{x})}$$}@}. <!--SR:!2028-11-24,1260,350!2026-12-30,704,330!2027-01-19,725,330-->

In plain English, {@{using [Bayesian probability](Bayesian%20probability.md) terminology}@}, the above equation is: {@{$$\text{posterior} = \frac {\text{prior} \times \text{likelihood} } {\text{evidence} }$$}@}. <!--SR:!2029-03-02,1340,350!2026-04-08,494,310-->

In practice, there is only {@{interest in the numerator but not the denominator}@}, because {@{the denominator depends not on $C_k$ but only $\mathbf{x}$, and $\mathbf{x}$ is often given so it is effectively constant}@}. The numerator is {@{equivalent to the [joint probability](joint%20probability%20distribution.md) model}@}: {@{$$p(C_k) p(\mathbf{x} \mid C_k) = p\left(C_k \cap \left(\bigcap_{i = 1}^n x_i \right) \right) = p(C_k, x_1, \ldots, x_n)$$}@}. <!--SR:!2027-03-31,768,330!2027-01-24,686,290!2026-01-31,435,310!2026-01-28,431,310-->

The joint probability model can {@{be rewritten as follows, using the [chain rule](chain%20rule%20(probability).md) arising from repeated applications of the definition of [conditional probability](conditional%20probability.md)}@}: {@{$$\begin{aligned} p(C_k, x_1, \ldots, x_n) & = p(x_1, \ldots, x_n, C_k) \\ & = p(x_1 \mid x_2, \ldots, x_n, C_k) p(x_2, \ldots, x_n, C_k) \\ & = \cdots \\ & = p(x_1, \mid x_2, \ldots, x_n, C_k) p(x_2 \mid x_3, \ldots, x_n, C_k) \cdots p(x_n \mid C_k) p(C_k) \end{aligned}$$}@} <!--SR:!2026-10-27,649,330!2027-01-17,684,290-->

After rewriting the joint probability model, {@{the "naive" assumptions come into play: Assume that all features of $\mathbf{x}$ are [mutually independent](independence%20(probability%20theory).md), conditional on the class $C_k$}@}, written mathematically as: {@{$$p(x_i \mid x_{i + 1}, \ldots, x_n, C_k) = p(x_i \mid C_k)$$}@}. <!--SR:!2026-04-17,468,310!2026-10-25,652,330-->

With the assumption, the joint probability model can {@{be simplified}@}: {@{$$\begin{aligned} p(C_k \mid \mathbf{x}) & \propto p(C_k, x_1, \ldots, x_n) && (p(\mathbf{x}) = \text{const.}) \\ & = p(C_k) p(x_1 \mid C_k) p(x_2 \mid C_k) \cdots p(x_n \mid C_k) \\ & = p(C_k) \prod_{i = 1}^n p(x_i \mid C_k) \end{aligned}$$}@}. <!--SR:!2026-11-06,665,330!2027-09-16,848,290-->

To conclude, {@{with the above assumptions}@}, {@{the conditional probability of class $C_k$ given features $\mathbf{x}$}@} is: {@{$$p(C_k \mid \mathbf{x}) = \frac 1 Z p(C_k) \prod_{i = 1}^n p(x_i \mid C_k)$$}@}, where {@{$Z = p(\mathbf{x}) = \sum_k p(C_k) p(\mathbf{x} \mid C_k)$ is a scaling factor dependent on $\mathbf{x}$ only}@}. <!--SR:!2027-08-06,861,330!2026-05-29,532,310!2029-08-29,1382,310!2027-06-14,777,290-->

The {@{prior for a given class, i.e. $p(C_k)$}@}, can be obtained from {@{the training dataset (empirical distribution)}@}, or {@{assumed equiprobable, i.e. $p(C_k) = \frac 1 K$}@}. For empirical distribution: {@{$$p(C_k) = \frac {\text{number of samples of class }C_k} {\text{number of samples} }$$}@}. <!--SR:!2028-12-25,1283,350!2025-11-30,352,290!2028-06-09,1130,350!2027-11-01,927,330-->

The {@{conditional probabilities of a feature having a specific value given a class, i.e. $p(x_i = v \mid C_k)$}@} required for calculations above can also be obtained from {@{the training dataset}@}. For discrete values: {@{$$p(x_i = v \mid C_k) = \frac {\text{number of samples of class }C_k\text{ and feature }x_i = v} {\text{number of samples of class }C_k}$$}@}, and for continuous values, {@{[Gaussian naive Bayes](#Gaussian%20naive%20Bayes)}@} is usually used. <!--SR:!2026-05-11,519,310!2026-06-04,527,310!2027-05-22,726,290!2028-11-29,1265,350-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/naive_Bayes_classifier) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
