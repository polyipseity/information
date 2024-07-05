---
aliases:
  - ID3
  - ID3 algorithm
tags:
  - flashcard/general/ID3_algorithm
  - language/in/English
---

# ID3 algorithm

## algorithm

The algorithm starts {{with the entire set as the root node}}. On each iteration of the algorithm on a tree node with set $T$, {{calculate the [conditional entropy](conditional%20entropy.md#definition) $\Eta(T | a)$ or the [information gain](information%20gain%20(decision%20tree).md) $\operatorname{IG}(T, a) = \Eta(T) - \Eta(T | a)$ for each unused attribute $a$}}. Then, {{split the set $T$ by the attribute with the lowest entropy or the highest information gain (arbitrary choosing one if tied)}}. The split sets are {{the new child nodes}}. Consider the attribute used for splitting {{used and [recursively](recursion%20(computer%20science).md) process the child nodes}}. <!--SR:!2024-11-29,170,310!2024-09-07,105,290!2024-09-01,91,270!2024-12-07,179,310!2025-04-05,274,330-->

There are three or four base cases to note: First, {{if every element in the set has the same class, the node becomes a leaf node labeled with said class}}. Second, {{if all attributes have been used, the node becomes a leaf node labeled with the [most common class](mode%20(statistics).md) of the set (arbitrary choosing one if tied)}}. Third, {{if the set is empty, the node becomes a leaf node labeled with the most common class of the set in the parent node}}. Optionally, {{the algorithm can additionally accept a threshold, then if the set size is less than the threshold, the node is treated like the second case above}}. <!--SR:!2024-07-21,61,270!2024-11-30,174,310!2024-11-14,146,270!2024-08-25,79,250-->

Throughout the algorithm, the decision tree is constructed by {{letting the internal nodes represent the selected attribute on which the set is split, and the leaf nodes be labeled with the predicted result}}. <!--SR:!2024-08-02,78,290-->

### properties

One problem with using {{the [information gain](information%20gain%20(decision%20tree).md) to select the attribute to split on is that it is generally larger if the attribute have more possible values, making it favor those attributes}}. A solution to this is {{use the [information gain ratio](information%20gain%20ratio.md) instead, like in the [C4.5 algorithm](C4.5%20algorithm.md)}}. <!--SR:!2024-11-06,152,310!2024-10-14,136,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ID3_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
