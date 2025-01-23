---
aliases:
  - perceptron
  - perceptrons
tags:
  - flashcard/active/general/eng/perceptron
  - language/in/English
---

# perceptron

## learning algorithm for a single-layer perceptron

### steps

1. initialization ::@:: Initialize the weights arbitrarily. Weights may be initialized to 0 or small random values. <!--SR:!2025-03-02,192,310!2025-05-02,229,310-->
2. training ::@:: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$: <!--SR:!2025-08-31,318,290!2025-05-10,252,330-->
    1. training: forward ::@:: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <!--SR:!2026-01-29,435,310!2026-07-02,525,310-->
    2. training: backward ::@:: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <!--SR:!2025-09-15,276,250!2026-08-11,576,310-->
3. termination ::@:: For [offline training](offline%20training.md), the second step may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <!--SR:!2025-01-26,137,250!2025-07-23,275,290-->

Since {@{$x_{j, 0} = 1$ always}@}, $w_0$ is {@{effectively the bias $b$}@}. Thus the above algorithm {@{already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t))$$}@}. <!--SR:!2025-05-06,250,330!2026-09-25,631,330!2025-07-26,272,290-->

### convergence of one perceptron on a linearly separable dataset

A single perceptron is {@{a [linear classifier](linear%20classifier.md)}@}. It only {@{converges (reaches a stable state) if the training samples are [linearly separable](linear%20separability.md), i.e. can always be classified correctly by a [linear classifier](linear%20classifier.md)}@}. <!--SR:!2025-05-03,247,330!2025-03-19,195,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/perceptron) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
