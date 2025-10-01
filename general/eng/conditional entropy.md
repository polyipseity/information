---
aliases:
  - conditional entropy
tags:
  - flashcard/active/general/eng/conditional_entropy
  - language/in/English
---

# conditional entropy

## definition

The conditional entropy of a [random variable](random%20variable.md) $Y$ given another random variable $X$ is defined as: {@{$$\Eta(Y | X) = -\sum_{x \in \mathcal X, y \in \mathcal Y} p(x, y) \log \frac {p(x, y)} {p(x)} = -\sum_{x \in \mathcal X} \left( p(x) \sum_{y \in \mathcal Y} p(y | x) \log p(y | x) \right) \,,$$}@} where $\mathcal X$ and $\mathcal Y$ are {@{the [support sets](support%20(mathematics).md) \(e.g. possible values of a random variable\) of respectively $X$ and $Y$}@}. <!--SR:!2028-02-05,839,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conditional_entropy) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
