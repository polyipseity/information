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
  - flashcard/general/naive_Bayes_classifier
  - language/in/English
---

# naive Bayes classifier

## probabilistic model

Abstractly, naive Bayes classifier is {{a [conditional probability](conditional%20probability.md) model}}. The problem to be solved is: Given a sample with {{$n$ features ($n$ inputs)}}, assign {{the conditional probability of the sample belonging to a class (1 output) for each of the $K$ possible classes}}. The $n$ inputs are represented by {{a vector $\mathbf{x} = (x_1, \ldots, x_n)$}}. The $k$-th class of the $K$ possible classes is represented by {{$C_k$}}. Then the conditional probability is mathematically {{$p(C_k \mid \mathbf{x})$}}. <!--SR:!2024-07-05,17,290!2024-09-04,63,310!2024-08-04,37,290!2024-09-03,62,310!2024-09-08,66,310!2024-08-15,43,290-->

Using {{[Bayes' theorem](Bayes'%20theorem.md)}}, the {{required conditional probability}} can be written as: {{$$p(C_k \mid \mathbf{x}) = \frac {p(C_k) p(\mathbf{x} \mid C_k)} {p(\mathbf{x})}$$}}. <!--SR:!2024-07-05,17,290!2024-08-13,41,290!2024-08-07,41,290-->

In plain English, {{using [Bayesian probability](Bayesian%20probability.md) terminology}}, the above equation is: {{$$\text{posterior} = \frac {\text{prior} \times \text{likelihood} } {\text{evidence} }$$}}. <!--SR:!2024-09-09,67,310!2024-07-29,33,270-->

In practice, there is only {{interest in the numerator but not the denominator}}, because {{the denominator depends not on $C_k$ but only $\mathbf{x}$, and $\mathbf{x}$ is often given so it is effectively constant}}. The numerator is {{equivalent to the [joint probability](joint%20probability%20distribution.md) model}}: {{$$p(C_k) p(\mathbf{x} \mid C_k) = p\left(C_k \cap \left(\bigcap_{i = 1}^n x_i \right) \right) = p(C_k, x_1, \ldots, x_n)$$}}. <!--SR:!2024-08-26,55,310!2024-07-17,22,250!2024-08-06,38,290!2024-08-07,36,290-->

The joint probability model can {{be rewritten as follows, using the [chain rule](chain%20rule%20(probability).md) arising from repeated applications of the definition of [conditional probability](conditional%20probability.md)}}: {{$$\begin{aligned} p(C_k, x_1, \ldots, x_n) & = p(x_1, \ldots, x_n, C_k) \\ & = p(x_1 \mid x_2, \ldots, x_n, C_k) p(x_2, \ldots, x_n, C_k) \\ & = \cdots \\ & = p(x_1, \mid x_2, \ldots, x_n, C_k) p(x_2 \mid x_3, \ldots, x_n, C_k) \cdots p(x_n \mid C_k) p(C_k) \end{aligned}$$}} <!--SR:!2024-08-19,48,310!2024-07-14,19,250-->

After rewriting the joint probability model, {{the "naive" assumptions come into play: Assume that all features of $\mathbf{x}$ are [mutually independent](independence%20(probability%20theory).md), conditional on the class $C_k$}}, written mathematically as: {{$$p(x_i \mid x_{i + 1}, \ldots, x_n, C_k) = p(x_i \mid C_k)$$}}. <!--SR:!2024-08-06,39,290!2024-08-09,38,290-->

With the assumption, the joint probability model can {{be simplified}}: {{$$\begin{aligned} p(C_k \mid \mathbf{x}) & \propto p(C_k, x_1, \ldots, x_n) && (p(\mathbf{x}) = \text{const.}) \\ & = p(C_k) p(x_1 \mid C_k) p(x_2 \mid C_k) \cdots p(x_n \mid C_k) \\ & = p(C_k) \prod_{i = 1}^n p(x_i \mid C_k) \end{aligned}$$}}. <!--SR:!2024-08-07,40,290!2024-07-18,23,250-->

To conclude, {{with the above assumptions}}, {{the conditional probability of class $C_k$ given features $\mathbf{x}$}} is: {{$$p(C_k \mid \mathbf{x}) = \frac 1 Z p(C_k) \prod_{i = 1}^n p(x_i \mid C_k)$$}}, where {{$Z = p(\mathbf{x}) = \sum_k p(C_k) p(\mathbf{x} \mid C_k)$ is a scaling factor dependent on $\mathbf{x}$ only}}. <!--SR:!2024-07-05,17,290!2024-08-04,35,270!2024-08-10,41,290!2024-07-18,22,250-->

The {{prior for a given class, i.e. $p(C_k)$}}, can be obtained from {{the training dataset (empirical distribution)}}, or {{assumed equiprobable, i.e. $p(C_k) = \frac 1 K$}}. For empirical distribution: {{$$p(C_k) = \frac {\text{number of samples of class }C_k} {\text{number of samples} }$$}}. <!--SR:!2024-07-05,17,290!2024-08-13,42,290!2024-08-29,58,310!2024-07-05,17,290-->

The {{conditional probabilities of a feature having a specific value given a class, i.e. $p(x_i = v \mid C_k)$}} required for calculations above can also be obtained from {{the training dataset}}. For discrete values: {{$$p(x_i = v \mid C_k) = \frac {\text{number of samples of class }C_k\text{ and feature }x_i = v} {\text{number of samples of class }C_k}$$}}, and for continuous values, {{[Gaussian naive Bayes](#Gaussian%20naive%20Bayes)}} is usually used. <!--SR:!2024-08-01,35,270!2024-08-16,45,290!2024-07-13,18,250!2024-09-07,65,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/naive_Bayes_classifier) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
