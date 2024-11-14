---
aliases:
  - Analytic Solver help
  - Analytic Solver usage
tags:
  - flashcard/active/special/Analytic_Solver_usage
  - language/in/English
---

# Analytic Solver usage

## installation

Eventually you should figure it out with online searching...

## usage

Eventually you should figure it out with online searching... Also, get familiar with the technical terms.

### category reduction

There are {@{some restrictions on the distinct values of an attribute}@} depending on the XLMiner edition. One way to resolve this is {@{merging some values into the same value}@}. Funny enough, the category reduction, which is designed for this workload, also has {@{restrictions on the distinct values depending on the XLMiner edition}@}. So {@{multiple category reductions on a subset of distinct values}@} may be needed if there are too many distinct values.

XLMiner offers {@{2 ways}@} to reduce categories: {@{automatically by frequency and manually}@}. The first option {@{reduces the values with the smallest frequencies into one value and leave the rest intact}@}. The second option {@{reduces the values using a user-specified table mapping current values to new values}@}.

### common parameters

- success probability cutoff ::@:: The minimum percentage of values being the "success" value for a set of values to be considered as "success" overall. The cutoff is `>=`, so the percentage equalling the threshold means the set is considered as "success".

### decision tree

- see: [general/decision tree](../general/decision%20tree.md)

The decision tree ends are called {@{_leaf nodes_ or _terminal nodes_}@}. The rest of the nodes are called {@{_decision nodes_ or _internal nodes_}@}.

The _error rate_ of a decision tree is {@{the number of mispredicted observations divided by the number of all observations}@}.

The decision tree threshold are used as follows: {@{If the attribute value is smaller or equal to the threshold, go left; otherwise, go right}@}.

### input formats

For inputting item lists, XLMiner provides 2 input formats: {@{binary matrix and item list}@}. The former is a table {@{with the column headers being the items and values (0 or 1) representing whether an item is in a transaction}@}. The latter is a table {@{with no column headers and values (string) representing the items themselves}@}.

### partitioning

XLMiner can partition the dataset into {@{3 datasets}@}: {@{training set, validation set, and test set}@}.

### random seed

- see: [general/random seed](../general/random%20seed.md)

Computers usually generate random numbers using a {@{[pseudorandom number generator](../general/pseudorandom%20number%20generator.md), which is usually a _deterministic_ algorithm that generates a random number from the previous random number}@}. Thus, to generate the first number, it needs {@{an initial "previous random number", which is called the _random seed_}@}. Since the algorithm is _deterministic_, given the same algorithm and {@{the same random seed, the sequence of randomly generated numbers are always the same}@}.

The seed option present in various interfaces is {@{simply the random seed to generate random numbers for use by the selected data mining algorithm}@}, so given the same data, inputting the same seed {@{will give the same result, even if the data mining algorithm requires random numbers}@}. If producing the same result is undesirable, we can use {@{the current time in milliseconds as the seed}@}.

### rescaling

XLMiner can rescale the dataset {@{in 4 ways}@}: {@{standardization, normalization, adjusted normalization, and unit-norm}@}. The first option {@{replaces the values with their standard scores}@}.
