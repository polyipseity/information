---
aliases:
  - perceptron
  - perceptrons
tags:
  - flashcard/general/perceptron
  - language/in/English
---

# perceptron

## learning algorithm for a single-layer perceptron

### steps

1. initialization ::: Initialize the weights arbitrary. Weights may be initialized to 0 or small random values. <!--SR:!2024-07-04,16,290!2024-07-05,17,290-->
2. training ::: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$: <!--SR:!2024-07-27,31,270!2024-08-31,59,310-->
    1. training: forward ::: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <!--SR:!2024-08-04,38,290!2024-08-08,41,290-->
    2. training: backward ::: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <!--SR:!2024-07-13,18,250!2024-07-04,16,290-->
3. termination ::: For [offline training](offline%20training.md), the second steps may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <!--SR:!2024-07-17,22,250!2024-07-22,24,270-->

Since {{$x_{j, 0} = 1$ always}}, $w_0$ is {{effectively the bias $b$}}. Thus the above algorithm {{already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t))$$}}. <!--SR:!2024-08-29,58,310!2024-08-08,37,290!2024-07-28,31,290-->

### convergence of one perceptron on a linearly separable dataset

A single perceptron is {{a [linear classifier](linear%20classifier.md)}}. It only {{converges (reaches a stable state) if the training samples are [linearly separable](linear%20separability.md), i.e. can always be classified correctly by a [linear classifier](linear%20classifier.md)}}. <!--SR:!2024-08-28,57,310!2024-09-05,64,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/perceptron) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
