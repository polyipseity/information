---
aliases:
  - RNN
  - RNNs
  - recurrent neural network
  - recurrent neural networks
tags:
  - flashcard/active/general/recurrent_neural_network
  - language/in/English
---

# recurrent neural network

A __recurrent neural network__ (__RNN__) is {@{one of the two board types of [neural network](neural%20network%20(machine%20learning).md)}@}, characterized by {@{the direction of information flow between its layers}@}. In contrast to {@{the unidirectional [feedforward neural network](feedforward%20nerual%20network.md), an RNN allows outputs from some neurons to affect subsequent inputs to the same neurons}@}. <!--SR:!2024-11-25,109,290!2025-03-05,195,310!2026-01-19,426,310-->

An RNN exhibits {@{temporal [dynamic behavior](dynamical%20system.md)}@}. This makes it suitable for datasets {@{with temporal relationship between the samples}@}. <!--SR:!2025-07-12,301,330!2025-04-08,225,330-->

The term "recurrent neural network" is used to refer {@{to the class of networks with [infinite impulse response](infinite%20impulse%20response.md)}@}, while {@{"[convolutional neural network](convolutional%20neural%20network.md)" refers to the class of networks with [finite impulse response](finite%20impulse%20response.md)}@}. <!--SR:!2025-12-26,406,310!2024-12-20,130,290-->

## architectures

- see: [layer](layer%20(deep%20learning).md)

### Elman networks and Jordan networks

An [Elman](Jeffrey%20Elman.md) network is {@{a 3-layer network with the addition of a context layer}@}. The middle hidden layer is {@{connected to the context layer with a fixed weight of 1}@}. The context layer connects {@{back to the middle hidden layer}@}. <!--SR:!2025-01-01,135,290!2025-01-30,171,310!2024-12-20,127,290-->

[Jordan](Michael%20I.%20Jordan.md) network are {@{similar to Elman networks}@}. The exception is {@{that the context layer is fed from the output layer instead of the middle hidden layer}@}. <!--SR:!2024-12-13,120,290!2024-12-13,121,290-->

Elman and Jordan networks are also known as {@{"simple recurrent networks" (SRN)}@}. The disadvantages are that {@{the networks are likely too simple, and they might take a long time to converge}@}. <!--SR:!2025-04-25,239,330!2025-01-16,149,290-->

### long short-term memory

- see: [long short-term memory](long%20short-term%20memory.md)

Long short-term memory (LSTM) is {@{a [deep learning](deep%20learning.md) system that avoids the [vanishing gradient problem](vanishing%20gradient%20problem.md)}@}. LSTMs are augmented with {@{recurrent gates like "forget gates", "input gates", and "output gates"}@}. LSTMs can learn {@{tasks that require memories of events thousands or even millions of time steps earlier}@}. LSTM works even if {@{there are long delays between significant events and can handle low and high-frequency components}@}. <!--SR:!2024-11-21,105,290!2024-12-29,137,290!2024-12-09,121,290!2025-02-24,179,310-->

### gated recurrent unit

- see: [gated recurrent unit](gated%20recurrent%20unit.md)

Gated recurrent units (GRUs) are {@{a gating mechanism in RNN introduced in 2014}@}. They have {@{fewer parameters than LSTM, as they lack an output gate}@}. This may make {@{the training time shorter and the training requiring fewer data samples}@}. <!--SR:!2025-02-23,178,310!2025-01-01,137,290!2025-01-04,152,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/recurrent_neural_network) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
