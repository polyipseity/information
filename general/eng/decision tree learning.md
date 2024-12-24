---
aliases:
  - decision tree learning
tags:
  - flashcard/active/general/decision_tree_learning
  - language/in/English
---

# decision tree learning

## decision tree types

### algorithms

Notable decision tree algorithms include:

- [C4.5](C4.5%20algorithm.md) ::@:: Classification 4.5
- [CART](classification%20and%20regression%20tree.md) ::@:: classification and regression tree
- [ID3](ID3%20algorithm.md) ::@:: Iterative Dichotomiser 3

### metrics

#### Gini impurity

__Gini impurity__, {@{__Gini's diversity index__, or __[Gini–Simpson index](diversity%20index.md#Gini–Simpson%20index)__ in biodiversity research}@}, is {@{the probability of sampling a [random variable](random%20variable.md) $X$ twice with replacement and getting different outcomes}@}. Symbolically, {@{$$\operatorname{I_G}(X) = \sum_{x \in \mathcal X} p(x) \left( \sum_{y \in \mathcal X, y \ne x} p(y) \right) = \sum_{x \in \mathcal X} p(x) (1 - p(x)) = \sum_{x \in \mathcal X} \left(p(x) - (p(x))^2 \right) = \sum_{x \in \mathcal X} p(x) - \sum_{x \in \mathcal X} (p(x))^2 = 1 - \sum_{x \in \mathcal X} (p(x))^2$$, where $\mathcal X$ is the [support set](support%20(mathematics).md) (e.g. possible values of a random variable) of $X$}@}.

Note that the Gini impurity is also {@{an [information entropy](entropy%20(information%20theory).md) measure, corresponding to the [Tsallis entropy](Tsallis%20entropy.md) with $q = 2$}@}. The usual [Shannon entropy](entropy%20(information%20theory).md) is also {@{the [Tsallis entropy](Tsallis%20entropy.md) when $q \to 1^+$}@}, showing that the Gini impurity is {@{simply a variation of the normal entropy}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/decision_tree_learning) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
