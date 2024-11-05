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

There are {{some restrictions on the distinct values of an attribute}} depending on the XLMiner edition. One way to resolve this is {{merging some values into the same value}}. Funny enough, the category reduction, which is designed for this workload, also has {{restrictions on the distinct values depending on the XLMiner edition}}. So {{multiple category reductions on a subset of distinct values}} may be needed if there are too many distinct values. <!--SR:!2025-09-04,345,355!2025-09-23,364,355!2025-10-14,379,355!2025-05-26,266,335-->

XLMiner offers {{2 ways}} to reduce categories: {{automatically by frequency and manually}}. The first option {{reduces the values with the smallest frequencies into one value and leave the rest intact}}. The second option {{reduces the values using a user-specified table mapping current values to new values}}. <!--SR:!2025-09-08,349,355!2025-04-02,225,335!2025-07-01,274,335!2025-06-17,265,335-->

### common parameters

- success probability cutoff ::: The minimum percentage of values being the "success" value for a set of values to be considered as "success" overall. The cutoff is `>=`, so the percentage equalling the threshold means the set is considered as "success". <!--SR:!2025-06-20,269,335!2025-01-14,159,315-->

### decision tree

- see: [general/decision tree](../general/decision%20tree.md)

The decision tree ends are called {{_leaf nodes_ or _terminal nodes_}}. The rest of the nodes are called {{_decision nodes_ or _internal nodes_}}. <!--SR:!2024-11-19,163,310!2026-04-05,533,310-->

The _error rate_ of a decision tree is {{the number of mispredicted observations divided by the number of all observations}}. <!--SR:!2025-03-30,252,290-->

The decision tree threshold are used as follows: {{If the attribute value is smaller or equal to the threshold, go left; otherwise, go right}}. <!--SR:!2025-03-11,126,315-->

### input formats

For inputting item lists, XLMiner provides 2 input formats: {{binary matrix and item list}}. The former is a table {{with the column headers being the items and values (0 or 1) representing whether an item is in a transaction}}. The latter is a table {{with no column headers and values (string) representing the items themselves}}. <!--SR:!2024-11-12,103,295!2025-09-07,348,355!2025-09-18,359,355-->

### partitioning

XLMiner can partition the dataset into {{3 datasets}}: {{training set, validation set, and test set}}. <!--SR:!2025-09-09,350,355!2025-02-15,183,315-->

### random seed

- see: [general/random seed](../general/random%20seed.md)

Computers usually generate random numbers using a {{[pseudorandom number generator](../general/pseudorandom%20number%20generator.md), which is usually a _deterministic_ algorithm that generates a random number from the previous random number}}. Thus, to generate the first number, it needs {{an initial "previous random number", which is called the _random seed_}}. Since the algorithm is _deterministic_, given the same algorithm and {{the same random seed, the sequence of randomly generated numbers are always the same}}. <!--SR:!2025-05-16,306,330!2024-12-05,179,310!2026-02-06,486,310-->

The seed option present in various interfaces is {{simply the random seed to generate random numbers for use by the selected data mining algorithm}}, so given the same data, inputting the same seed {{will give the same result, even if the data mining algorithm requires random numbers}}. If producing the same result is undesirable, we can use {{the current time in milliseconds as the seed}}. <!--SR:!2025-09-03,361,290!2024-11-13,160,310!2026-07-05,626,330-->

### rescaling

XLMiner can rescale the dataset {{in 4 ways}}: {{standardization, normalization, adjusted normalization, and unit-norm}}. The first option {{replaces the values with their standard scores}}. <!--SR:!2025-08-26,341,355!2025-06-08,257,335!2025-01-22,163,315-->
