---
aliases:
  - ID3
  - ID3 algorithm
tags:
  - flashcard/active/general/eng/ID3_algorithm
  - language/in/English
---

# ID3 algorithm

## algorithm

The algorithm starts {@{with the entire set as the root node}@}. On each iteration of the algorithm on a tree node with set $T$, {@{calculate the [conditional entropy](conditional%20entropy.md#definition) $\Eta(T | a)$ or the [information gain](information%20gain%20(decision%20tree).md) $\operatorname{IG}(T, a) = \Eta(T) - \Eta(T | a)$ for each unused attribute $a$}@}. Then, {@{split the set $T$ by the attribute with the lowest entropy or the highest information gain (arbitrary choosing one if tied)}@}. The split sets are {@{the new child nodes}@}. Consider the attribute used for splitting {@{used and [recursively](recursion%20(computer%20science).md) process the child nodes}@}.

There are {@{three or four base cases}@} to note: First, if {@{every element in the set has the same class}@}, the node becomes {@{a leaf node labeled with said class}@}. Second, if {@{all attributes have been used}@}, the node becomes {@{a leaf node labeled with the [most common class](mode%20(statistics).md) of the set \(arbitrary choosing one if tied\)}@}. Third, if {@{the set is empty}@}, the node becomes {@{a leaf node labeled with the most common class of the set in the parent node}@}. Optionally, the algorithm can additionally accept {@{a threshold}@}, then if {@{the set size is less than the threshold}@}, the node is {@{treated like the second case above \(labeled with the most common class\)}@}.

Throughout the algorithm, the decision tree is constructed by {@{letting the internal nodes represent the selected attribute on which the set is split, and the leaf nodes be labeled with the predicted result}@}.

### properties

One problem with using {@{the [information gain](information%20gain%20(decision%20tree).md) to select the attribute to split on is that it is generally larger if the attribute has more possible values, making it favor those attributes}@}. A solution to this is use {@{the [information gain ratio](information%20gain%20ratio.md)}@} instead, like in {@{the [C4.5 algorithm](C4.5%20algorithm.md)}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ID3_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
