---
aliases:
  - artificial neuron
  - artificial neurons
tags:
  - flashcard/active/general/eng/artificial_neuron
  - language/in/English
---

# artificial neuron

## basic structure

For a given artificial neuron _k_, let there be {@{_m_ + 1 inputs and weights. The inputs are labelled _x_<sub>0</sub> to _x_<sub>_m_</sub>. The weights are labelled _w_<sub>_k_<!-- separator -->0</sub> to _w_<sub>_km_</sub>}@}. Usually, {@{the _x_<sub>0</sub> input is always assigned +1, making it a _bias input_ with the weight _b_<sub>_k_</sub> = _w_<sub>_k_<!-- separator -->0</sub> being the _bias_}@}. This leaves {@{_m_ actual inputs to the neurons: from _x_<sub>1</sub> to _x_<sub>_m_</sub>}@}. <!--SR:!2025-07-07,299,330!2027-12-20,965,330!2025-06-05,271,330-->

The output of the _k_-th neuron is: {@{$$y_k = \varphi\left(\sum_{j = 0}^m w_{kj} x_j \right) = \varphi\left(b_k + \sum_{j = 1}^m w_{kj} x_j \right)$$}@}, where {@{$\varphi$ is the _[activation function](activation%20function.md)_ (also called _threshold function_, or confusingly, _transfer function_)}@}. <!--SR:!2026-07-09,517,270!2025-07-15,304,330-->

## types of activation function

- see: [activation function](activation%20function.md)

The [activation function](activation%20function.md) of a neurons is chosen {@{to have properties enhancing or simplifying the network}@}. Crucially, {@{any [multilayer perceptron](multilayer%20perceptron.md) using a _linear_ activation function has a equivalent single-layer network, which can be proved mathematically; thus, a non-linear function is needed to leverage the full power of a multilayer network}@}. <!--SR:!2025-06-28,291,330!2026-04-25,471,310-->

Below, _u_, also called {@{the _net input_}@}, is {@{the weighted sum of all inputs to the neuron, including the bias}@}. For _m + 1_ inputs as described above: {@{$$u = \sum_{j = 0}^m w_{kj} x_j = b_k + \sum_{j = 1}^m w_{kj} x_j$$}@}. <!--SR:!2028-05-04,1102,350!2025-06-18,282,330!2026-05-06,518,310-->

### step function

The output of _y_ is {@{binary depending on whether the net input meets (greater than or equal to) a specified threshold, _θ_}@}: {@{$$y = \begin{cases} 1 & \text{if }u \ge \theta \\ 0 & \text{if }u < \theta \end{cases}$$}@}. <!--SR:!2028-02-14,1040,350!2025-06-21,285,330-->

Usually, the threshold _θ_ is {@{chosen to be 0}@}. <!--SR:!2025-05-16,258,330-->

### linear combination

In this case, the output _y_ is {@{simply the net input _u_ multiplied by a constant _k_}@}: {@{$$y = ku$$}@} When {@{$k = 1$}@}, this is {@{simply the [identity function](identity%20function.md): $y = u$}@}. It is a type of {@{linear activation function}@}. <!--SR:!2028-01-26,1024,350!2025-06-05,273,330!2028-06-11,1131,350!2027-12-10,987,350!2028-02-15,1039,350-->

### sigmoid

- see: [sigmoid function](sigmoid%20function.md)

[Sigmoid functions](sigmoid%20function.md) are {@{fairly simple non-linear activation functions}@}. Usually, it refers to the {@{[logistic function](logistic%20function.md) with _L_ = 1, _k_ = 1, and _x_<sub>0</sub> = 0}@}: {@{$$y = \frac L {1 + e^{-k(u - x_0)} } = \frac 1 {1 + e^{-u} }$$}@}. Its more practical counterpart is {@{the [hyperbolic tangent](hyperbolic%20function.md) ($\tanh$)}@}: {@{$$y = \frac {\sinh u} {\cosh u} = \frac {e^u - e^{-u} } {e^u + e^{-u} } = \frac {e^{2u} - 1} {e^{2u} + 1}$$}@} <!--SR:!2026-07-29,587,330!2026-03-02,466,310!2026-04-20,449,290!2026-01-07,377,290!2026-04-29,443,270-->

### rectifier

- see: [rectifier](rectifier%20(neural%20networks).md)

The __rectifier__ or {@{__ReLU__ (__rectified linear unit__)}@} is an activation function defined as {@{the positive part of its argument}@}: {@{$$y = u^+ = \max(0, u) = \frac {u + \lvert u \rvert} 2 = \begin{cases} u & \text{if }u > 0 \\ 0 & \text{otherwise} \end{cases}$$}@}. <!--SR:!2025-05-14,256,330!2028-01-29,1027,350!2027-01-23,728,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/artificial_neuron) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
