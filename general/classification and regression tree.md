---
aliases:
  - CART
  - classification and regression tree
tags:
  - flashcard/general/classification_and_regression_tree
  - language/in/English
---

# classification and regression tree

## algorithm

The algorithm is similar to the [ID3 algorithm](ID3%20algorithm.md), with several changes described below. First, instead of {{using [Shannon entropy](entropy%20(information%20theory).md), replace all use of [Shannon entropy](entropy%20(information%20theory).md) with [Gini impurity](decision%20tree%20learning.md#Gini%20impurity)}}. Note that when replacing {{[conditional Shannon entropy](conditional%20entropy.md), there are many inconsistent ways to replace it with a conditional analog of Gini impurity.[<sup>[1]</sup>](#^ref-Teixeira-2021) In this case, use this definition of conditional Gini impurity: $$\operatorname{I_G}(Y | X) = \sum_{x \in \mathcal X} p(x) \left(1 - \sum_{y \in \mathcal Y} (p(y | x))^2 \right)$$, using the same notation in conditional entropy}}. <!--SR:!2024-05-28,33,290!2024-07-12,57,250-->

Note that that the Gini impurity is {{simply a variation of the usual [Shannon entropy](entropy%20(information%20theory).md)}}. Both variations can be obtained from {{the more general [Tsallis entropy](Tsallis%20entropy.md)}}. <!--SR:!2024-05-26,31,270!2024-07-21,66,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/classification_and_regression_tree) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Teixeira A, Souto A, Antunes L. On Conditional Tsallis Entropy. _Entropy_. 2021; 23(11):1427. <https://doi.org/10.3390/e23111427> <a id="^ref-Teixeira-2021"></a> ^ref-Teixeira-2021
