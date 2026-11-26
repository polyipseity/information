---
aliases:
  - artificial neural network
  - connectionist model
  - neural network
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/artificial_neural_network
  - language/in/English
---

# artificial neural network

An artificial neural network approximates a population of neurons in the respects that matter for its task. It learns by example rather than by rule. Connectionist models of cognition treat such networks as accounts of perception, language and learning. Whether such a network models the process behind the behaviour is open.

---

Flashcards for this section are as follows:

- what an artificial neural network approximates ::@:: A population of neurons, in the respects that matter for its task.
- how an artificial neural network learns ::@:: By example rather than by rule.
- what connectionist models of cognition treat a neural network as ::@:: An account of perception, language and learning.
- what is still open about a network that behaves like a person ::@:: Whether it models the process behind that behaviour.

## forward pass

At inference, data moves one way through three tiers: input, hidden, and output layers. A shape classifier for squares, circles, and triangles takes a 28 by 28 pixel image, 784 input values, one per pixel. Each connection into the next layer carries a weight. The receiving unit adds a bias and passes the sum through an activation function. A sigmoid or a rectified linear unit (ReLU) decides whether the unit fires. The hidden layers do most of the processing, combining edges into shapes. The output layer returns a probability per class, and the highest is the prediction.

---

Flashcards for this section are as follows:

- the three tiers a neural network's data moves through at inference, and the direction ::@:: The input, hidden, and output layers, in one direction only.
- how many input values a shape classifier for squares, circles, and triangles takes from a 28 by 28 pixel image ::@:: 784, one per pixel.
- the two numeric parameters a connection and its receiving unit contribute, in a neural network ::@:: A weight on the connection, and a bias that the receiving unit adds to the weighted sum.
- what a sigmoid or a rectified linear unit (ReLU) decides for a unit's summed input ::@:: Whether the unit fires.
- what the hidden layers and the output layer each do in a shape classifier ::@:: The hidden layers combine edges into shapes; the output layer returns a probability per class, and the highest is the prediction.

## single-layer networks

### artificial neuron

Warren McCulloch and Walter Pitts showed in 1943 that one simple unit can compute logical functions. Frank Rosenblatt's 1958 Perceptron, a group of such units, recognised simple visual patterns. It used no hand-crafted features. A decentralised rule updated its synaptic connection strengths to fix errors. The network tuned itself to the statistics of its training data.

---

Flashcards for this section are as follows:

- what Warren McCulloch and Walter Pitts showed in 1943 ::@:: That a single simple unit can compute logical (Boolean) functions.
- what Frank Rosenblatt's 1958 Perceptron recognised ::@:: Simple visual patterns.
- how the Perceptron learned without hand-crafted features ::@:: A decentralised rule updated its synaptic connection strengths to correct errors.
- what the Perceptron's learning tuned the network to ::@:: The statistics of its training data.

### linear limit

A single-layer Perceptron splits patterns only when they are linearly separable (Minsky & Papert, 1969; Mycielski, 1972). It cannot compute exclusive-or. That limit slowed the field as digital computers spread. The Neocognitron (Fukushima, 1980) kept going. Its simulated neurons, modelled on cat visual cortex (Hubel & Wiesel, 1959), are convolution operators.

---

Flashcards for this section are as follows:

- when a single-layer Perceptron can separate patterns ::@:: The patterns must be linearly separable.
- the simple logical function a single-layer Perceptron cannot compute ::@:: Exclusive-or.
- what the linear limit did to neural network research ::@:: Slowed it as digital computers spread.
- the network that kept going through the first neural network winter ::@:: The Neocognitron (Fukushima, 1980).
- what the Neocognitron's simulated neurons were modelled on ::@:: Cells in cat visual cortex (Hubel & Wiesel, 1959).
- how the Neocognitron's simulated neurons operate ::@:: As convolution operators.

## multi-layer networks

### backpropagation

Multi-layer networks trained by backpropagation (Rumelhart & McClelland, 1986) restored nonlinearity. Training compares the prediction with the label at the output layer, sends the error back through the chain rule, and moves each weight against the gradient. Connectionist modelling of higher-order cognition followed. NetTalk (Sejnowski & Rosenberg, 1987) mapped English text to phonetics. Its output went from noise through babbling to adult speech. Other networks learned English past tenses and made a child's confusions between regular and irregular forms. A 1991 network that predicted the next word of a sentence learned some syntax.

---

Flashcards for this section are as follows:

- what the backpropagation training rule restored to neural networks ::@:: Nonlinear capability, in multi-layer networks (Rumelhart & McClelland, 1986).
- what connectionist modelling took on in the 1980s ::@:: Higher-order cognitive tasks, language among them.
- what NetTalk mapped English text to ::@:: Phonetic output (Sejnowski & Rosenberg, 1987).
- how NetTalk's output changed across learning ::@:: From random noise, through infant-like babbling, to an approximation of adult speech.
- the mistakes networks made in learning English past tenses ::@:: The same confusions between regular and irregular forms that a child makes.
- what the 1991 network that predicted a sentence's next word internalised ::@:: Some of the syntax of English.
- when training computes the error, and against what ::@:: Once, at the output layer, by comparing the prediction with the target label, not separately at each hidden layer.
- how training changes each weight once the error is computed ::@:: The error travels back through the chain rule, and each weight moves against the gradient.

### deep networks

Yann LeCun's 1989 network read messy handwritten postal codes by backpropagation, with an architecture close to the Neocognitron. AlexNet (Krizhevsky, Sutskever & Hinton, 2012) then beat every earlier model on ImageNet, which sorted 1.3 million images into 1000 categories. Face recognition reached human parity (Taigman et al., 2014). It later matched the level of super-recognisers and forensic examiners (Phillips et al., 2018).

---

Flashcards for this section are as follows:

- the task Yann LeCun's 1989 network learned ::@:: Reading messy handwritten postal codes.
- what the architecture of Yann LeCun's 1989 network was close to ::@:: The Neocognitron.
- the challenge AlexNet won in 2012 ::@:: The ImageNet challenge, which sorted 1.3 million images into 1000 categories.
- what AlexNet did to earlier models on ImageNet ::@:: Beat every one of them.
- the level face recognition reached in 2014 ::@:: Human parity (Taigman et al., 2014).
- the level automated face recognition reached a few years later ::@:: That of super-recognisers and professional forensic face examiners (Phillips et al., 2018).

## as a model of mind

From the 1990s to the 2000s, small networks reproduced particular human effects rather than a whole mind. Those results gave the network's architecture its cognitive plausibility. A model can be wrong and still useful (Box, 1979). [computational model](computational%20model.md) covers how one is tested.

---

Flashcards for this section are as follows:

- what small networks reproduced from the 1990s through the 2000s ::@:: Particular human effects, rather than a whole mind.
- what a small network's results gave its architecture ::@:: Its cognitive plausibility.
- what matching human behaviour leaves open ::@:: Whether the network is a true model of the human process.
- George Box's 1979 line on models ::@:: All models are wrong, but some are useful.

## references

- O'Toole, A. J., & Ludvig, E. A. (2026). [The use of AI in psychology: A historical perspective](https://doi.org/10.1111/bjop.70061). _British Journal of Psychology_, _117_(2).
    - Source of the material on the artificial neuron, the linear limit, backpropagation, deep networks, and the model of mind.
    - Open access under a Creative Commons license; the publisher footer does not name the variant.
- \[missing\].
    - Source of the 1980s connectionist aim at higher-order cognitive tasks, and of the point that the decade's advances were small-scale versions of real problems.
- \[missing\]. (\[missing\]). [Neural Network In 5 Minutes](https://www.youtube.com/watch?v=bfmFfD2RIcg) [Video]. YouTube.
    - Source of the material on the forward pass.
