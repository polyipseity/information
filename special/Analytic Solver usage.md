---
aliases:
  - Analytic Solver help
  - Analytic Solver usage
tags:
  - flashcard/special/Analytic_Solver_usage
  - language/in/English
---

# Analytic Solver usage

## installation

Eventually you should figure it out with online searching...

## usage

Eventually you should figure it out with online searching... Also, get familiar with the technical terms.

### decision tree

- see: [general/decision tree](../general/decision%20tree.md)

The decision tree ends are called {{_leaf nodes_ or _terminal nodes_}}. The rest of the nodes are called {{_decision nodes_ or _internal nodes_}}. <!--SR:!2024-11-19,163,310!2024-06-10,44,290-->

The _error rate_ of a decision tree is {{the number of mispredicted observations divided by the number of all observations}}. <!--SR:!2024-07-17,67,270-->

### random seed

- see: [general/random seed](../general/random%20seed.md)

Computers usually generate random numbers using a {{[pseudorandom number generator](../general/pseudorandom%20number%20generator.md), which is usually a _deterministic_ algorithm that generates a random number from the previous random number}}. Thus, to generate the first number, it needs {{an initial "previous random number", which is called the _random seed_}}. Since the algorithm is _deterministic_, given the same algorithm and {{the same random seed, the sequence of randomly generated numbers are always the same}}. <!--SR:!2024-07-12,71,310!2024-12-05,179,310!2024-10-05,121,290-->

The seed option present in various interfaces is {{simply the random seed to generate random numbers for use by the selected data mining algorithm}}, so given the same data, inputting the same seed {{will give the same result, even if the data mining algorithm requires random numbers}}. If producing the same result is undesirable, we can use {{the current time in milliseconds as the seed}}. <!--SR:!2024-09-07,96,270!2024-11-13,160,310!2024-10-16,140,310-->
