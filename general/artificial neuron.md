---
aliases:
  - artificial neuron
  - artificial neurons
tags:
  - flashcard/active/general/artificial_neuron
  - language/in/English
---

# artificial neuron

## basic structure

For a given artificial neuron _k_, let there be {{_m_ + 1 inputs and weights. The inputs are labelled _x_<sub>0</sub> to _x_<sub>_m_</sub>. The weights are labelled _w_<sub>_k_<!-- separator -->0</sub> to _w_<sub>_km_</sub>}}. Usually, {{the _x_<sub>0</sub> input is always assigned +1, making it a _bias input_ with the weight _b_<sub>_k_</sub> = _w_<sub>_k_<!-- separator -->0</sub> being the _bias_}}. This leaves {{_m_ actual inputs to the neurons: from _x_<sub>1</sub> to _x_<sub>_m_</sub>}}. <!--SR:!2024-09-11,68,310!2024-09-16,73,310!2024-09-07,65,310-->

The output of the _k_-th neuron is: {{$$y_k = \varphi\left(\sum_{j = 0}^m w_{kj} x_j \right) = \varphi\left(b_k + \sum_{j = 1}^m w_{kj} x_j \right)$$}}, where {{$\varphi$ is the _[activation function](activation%20function.md)_ (also called _threshold function_, or confusingly, _transfer function_)}}. <!--SR:!2024-09-14,58,250!2024-09-14,71,310-->

## types of activation function

- see: [activation function](activation%20function.md)

The [activation function](activation%20function.md) of a neurons is chosen {{to have properties enhancing or simplifying the network}}. Crucially, {{any [multilayer perceptron](multilayer%20perceptron.md) using a _linear_ activation function has a equivalent single-layer network, which can be proved mathematically; thus, a non-linear function is needed to leverage the full power of a multilayer network}}. <!--SR:!2024-09-10,68,310!2025-01-09,152,310-->

Below, _u_, also called {{the _net input_}}, is {{the weighted sum of all inputs to the neuron, including the bias}}. For _m + 1_ inputs as described above: {{$$u = \sum_{j = 0}^m w_{kj} x_j = b_k + \sum_{j = 1}^m w_{kj} x_j$$}}. <!--SR:!2025-04-27,241,330!2024-09-08,66,310!2024-12-04,127,290-->

### step function

The output of _y_ is {{binary depending on whether the net input meets a specified threshold, _θ_}}: {{$$y = \begin{cases} 1 & \text{if }u \ge \theta \\ 0 & \text{if }u < \theta \end{cases}$$}}. <!--SR:!2025-04-10,227,330!2024-09-09,67,310-->

Usually, the threshold _θ_ is {{chosen to be 0}}. <!--SR:!2024-08-31,60,310-->

### linear combination

In this case, the output _y_ is {{simply the net input _u_ multiplied by a constant _k_}}: {{$$y = ku$$}} When {{$k = 1$}}, this is {{simply the [identity function](identity%20function.md): $y = u$}}. It is a type of {{linear activation function}}. <!--SR:!2025-04-06,225,330!2024-09-05,64,310!2025-05-04,247,330!2025-03-28,217,330!2025-04-12,229,330-->

### sigmoid

- see: [sigmoid function](sigmoid%20function.md)

[Sigmoid functions](sigmoid%20function.md) are {{fairly simple non-linear activation functions}}. Usually, it refers to the {{[logistic function](logistic%20function.md) with _L_ = 1, _k_ = 1, and _x_<sub>0</sub> = 0}}: {{$$y = \frac 1 {1 + e^{-u} }$$}}. Its more practical counterpart is {{the [hyperbolic tangent](hyperbolic%20function.md) ($\tanh$)}}: {{$$y = \frac {\sinh u} {\cosh u} = \frac {e^u - e^{-u} } {e^u + e^{-u} } = \frac {e^{2u} - 1} {e^{2u} + 1}$$}} <!--SR:!2024-12-19,136,310!2024-11-21,116,290!2025-01-26,153,290!2024-12-26,130,290!2025-02-10,164,270-->

### rectifier

- see: [rectifier](rectifier%20(neural%20networks).md)

The __rectifier__ or {{__ReLU__ (__rectified linear unit__)}} is an activation function defined as {{the positive part of its argument}}: {{$$y = u^+ = \max(0, u) = \frac {u + \lvert u \rvert} 2 = \begin{cases} u & \text{if }u > 0 \\ 0 & \text{otherwise} \end{cases}$$}}. <!--SR:!2024-08-31,59,310!2025-04-07,226,330!2025-01-25,170,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/artificial_neuron) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
