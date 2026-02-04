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

The algorithm starts {@{with the entire set as the root node}@}. On each iteration of the algorithm on a tree node with set $T$, {@{calculate the [conditional entropy](conditional%20entropy.md#definition) $\Eta(T | a)$ or the [information gain](information%20gain%20(decision%20tree).md) $\operatorname{IG}(T, a) = \Eta(T) - \Eta(T | a)$ for each unused attribute $a$}@}. Then, {@{split the set $T$ by the attribute with the lowest entropy or the highest information gain (arbitrary choosing one if tied)}@}. The split sets are {@{the new child nodes}@}. Consider the attribute used for splitting {@{used and [recursively](recursion%20(computer%20science).md) process the child nodes}@}. <!--SR:!2026-11-29,729,330!2030-10-15,1807,330!2028-04-22,987,290!2026-06-15,555,310!2028-09-03,1247,350-->

There are {@{three or four base cases}@} to note: First, if {@{every element in the set has the same class}@}, the node becomes {@{a leaf node labeled with said class}@}. Second, if {@{all attributes have been used}@}, the node becomes {@{a leaf node labeled with the [most common class](mode%20(statistics).md) of the set \(arbitrary choosing one if tied\)}@}. Third, if {@{the set is empty}@}, the node becomes {@{a leaf node labeled with the most common class of the set in the parent node}@}. Optionally, the algorithm can additionally accept {@{a threshold}@}, then if {@{the set size is less than the threshold}@}, the node is {@{treated like the second case above \(labeled with the most common class\)}@}. <!--SR:!2026-03-20,443,270!2026-12-16,746,330!2028-12-06,1082,270!2026-07-18,494,250!2026-04-24,81,343!2026-04-24,81,343!2026-04-25,82,343!2026-04-26,83,343!2026-04-25,82,343!2026-04-24,81,343-->

Throughout the algorithm, the decision tree is constructed by {@{letting the internal nodes represent the selected attribute on which the set is split, and the leaf nodes be labeled with the predicted result}@}. <!--SR:!2026-12-29,653,290-->

### properties

One problem with using {@{the [information gain](information%20gain%20(decision%20tree).md) to select the attribute to split on is that it is generally larger if the attribute has more possible values, making it favor those attributes}@}. A solution to this is use {@{the [information gain ratio](information%20gain%20ratio.md)}@} instead, like in {@{the [C4.5 algorithm](C4.5%20algorithm.md)}@}. <!--SR:!2026-08-20,652,330!2029-07-02,1301,310!2026-04-26,83,343-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ID3_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
