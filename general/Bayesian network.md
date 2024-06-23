---
aliases:
  - Bayes net
  - Bayes nets
  - Bayes network
  - Bayes networks
  - Bayesian belief network
  - Bayesian belief networks
  - Bayesian network
  - Bayesian networks
  - bayes net
  - bayes nets
  - bayes network
  - bayes networks
  - bayesian belief network
  - bayesian belief networks
  - bayesian network
  - bayesian networks
  - belief network
  - belief networks
  - decision network
  - decision networks
tags:
  - flashcard/general/Bayesian_network
  - language/in/English
---

# Bayesian network

A __Bayesian network__ (also known as a __Bayes network__, __Bayes net__, __belief network__, or __decision network__) is {{a [probabilistic graphical model](graphical%20model.md) that represents a set of variables and their [conditional dependencies](conditional%20dependence.md) via a [directed acyclic graph](directed%20acyclic%20graph.md) (DAG)}}. <!--SR:!2024-06-27,9,270-->

One advantage of Bayesian networks is that {{it is more intuitive for humans to understand over complete [joint distributions](joint%20probability%20distribution.md)}}. Disadvantages include {{it requires predefined knowledge about the network topology, and it cannot contain cycles}}. <!--SR:!2024-07-03,15,290!2024-06-29,11,270-->

## graphical model

Each edge {{represents a direct [conditional dependency](conditional%20dependence.md)}}. This means if {{A points to B, then the probability of B is modified if A is known, and the probability of A is also modified if B is known, but in an reverse way. That is, $P(A \mid B) \ne P(A)$ and $P(B \mid A) \ne P(B)$ in general}}. Any pair of nodes C and D that are {{not connected (i.e. there are no paths following the arrow directions that start from one of the node and end at the other node)}} represent {{variables that are [independent](conditional%20independence.md) of each other. That is, $P(C \mid D) = P(C)$ and $P(D \mid C) = P(D)$}}. Each node is {{associated with a [probability function](probability%20distribution.md) that takes (as inputs) a particular set of values for all the node's direct parents, and gives (as outputs) the probability of each possible value for the node}}. For discrete values, the above function can be represented by {{a [conditional probability table](conditional%20probability%20table.md)}}. <!--SR:!2024-07-03,15,290!2024-06-25,8,250!2024-06-30,13,270!2024-07-01,13,290!2024-07-06,13,250!2024-06-27,9,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bayesian_network) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
