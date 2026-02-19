---
aliases:
  - FP growth algorithm
  - FP-growth algorithm
  - frequent pattern growth algorithm
tags:
  - flashcard/active/general/eng/FP-growth_algorithm
  - language/in/English
---

# FP-growth algorithm

FP stands for {@{frequent pattern}@}. <!--SR:!2028-07-13,1206,350-->

## overview

The FP-growth algorithm {@{outperforms the [Apriori](Apriori%20algorithm.md) and [Eclat](Eclat%20algorithm.md) algorithms}@}. This is because {@{it does not generate and test candidates}@}, and {@{scan the entire database only once \(or twice, depending on how you define "scan"\) to construct a [FP-tree](#FP-tree)}@}, which is {@{a compact tree structure called [trie](trie.md)}@}. The [FP-tree](#FP-tree) is {@{usually compact enough to fit into the memory, which is fast}@}, allowing {@{quick generation of large item sets from it}@}. <!--SR:!2029-11-26,1457,290!2029-04-20,1342,310!2029-03-16,1306,310!2026-12-25,393,377!2027-01-06,402,377!2027-01-04,401,377-->

### FP-tree

The _FP-tree_ is {@{a compact tree structure called [trie](trie.md), representing the entire database exactly while only discarding the order of transactions in the database}@}. It is constructed with {@{a _header table_}@}. To construct {@{a FP-tree for a set of transactions}@}, {@{two passes are required}@}. <!--SR:!2028-01-22,878,270!2027-01-23,771,330!2027-05-26,867,330!2026-06-08,113,388-->

{@{A minimum support}@} is given. (Here, we define support as {@{"the number of transactions"}@}.) In the first pass, count {@{the support for each individual item and store the supports into a header table}@}. Then, for the header table, sort {@{items by descending support and remove items below the minimum support}@}. Also, for each item in the header table, add {@{a list structure that will be storing FP-tree nodes}@}. <!--SR:!2026-04-07,493,270!2028-10-29,1213,310!2029-07-04,1398,310!2026-06-08,113,388!2026-06-11,116,388-->

In the second pass, we construct {@{the FP-tree to represent the entire set of transactions}@}. To ensure {@{fast construction}@}, sort {@{the items in each transaction by descending support}@}. If an item {@{does not meet the minimum support globally (i.e. not in the header table)}@}, it is {@{removed}@}. Then we insert {@{the processed transactions into the FP-tree}@} such that {@{the FP-tree is a [trie](trie.md) of the transactions}@}. The FP-tree is {@{a tree of nodes}@}, with {@{each node except for the root node}@} storing {@{an item and a count}@}. Initialize the FP-tree with {@{one root node}@}. Specifically, to {@{insert a transaction}@} into the FP-tree, {@{start from the root node and consider the first item of the transaction}@}. If the item {@{is already a child of the root node}@}, increment {@{the count of the child by 1}@}. Otherwise, create {@{a new child with said item and count 1}@}, and add {@{the new child to the corresponding list structure in the header table}@}. Then, repeat the above steps with {@{the child and the next item of the transaction}@} until {@{the items are exhausted}@}. <!--SR:!2031-07-07,1999,330!2026-12-04,731,330!2027-06-07,811,290!2030-11-11,1828,330!2029-01-08,1265,310!2026-11-01,710,330!2026-05-28,464,250!2028-08-31,959,250!2026-06-08,113,388!2026-06-10,115,388!2026-06-19,123,388!2026-06-08,113,388!2026-06-26,129,388!2026-06-08,113,388!2026-06-18,122,388!2026-06-09,114,388!2026-06-16,120,388!2026-06-25,128,388!2026-06-26,129,388-->

By ordering {@{the items in each transaction by descending support}@}, the FP-tree stores frequent prefixes {@{close to the tree root, enabling high compression of the set of transactions}@}. The height of the FP-tree is {@{the maximum number of frequent items in a transaction considering all transactions}@}. (Note that the height of a FP-tree with the root node only is {@{0, not 1}@}.) <!--SR:!2030-01-04,1586,330!2026-06-05,535,310!2029-01-06,1359,368!2026-06-15,119,388-->

### growth

We can now describe how to {@{grow the frequent item sets}@} using {@{the [FP-tree](#FP-tree) and header table}@}. To find all {@{frequent item sets}@} in {@{a set of transactions or database $D$}@}, first construct {@{its FP-tree and header table}@}. Iterate {@{through the header table}@}, starting from {@{the bottom of the header table (i.e. the item with the least support)}@}. <!--SR:!2026-09-04,609,310!2029-03-19,1274,290!2027-06-26,844,290!2027-04-27,439,394!2027-04-29,440,394!2027-04-29,440,394!2027-01-03,325,374-->

For each item $I$ in the header table iterated as described above, {@{iterate through its corresponding FP-tree node list to construct a new set of transactions or sub-database $D_I$ that must have the item $I$, also described as conditional on item $I$}@}. Specifically, for each node $N$ in the node list, {@{find the corresponding item set by gathering the node, the node's parent, and further parents up to the root node}@}. Then said item set has a count {@{specified by the original node $N$ (i.e. the deepest node)}@}. After iterating through the whole node list, the set of item sets is {@{the new sub-database $D_I$}@}. After removing $I$ from each transaction in the sub-database $D_I$, {@{_recursively_ apply the growth step described in this section on the sub-database $D_I$ to get the new frequent item sets of $D_I$}@}. _Add back_ item $I$ {@{to each new frequent item sets, and save it for now}@}. Note that the FP-tree constructed from the sub-database $D_I$ is {@{the original FP-tree projected on $I$, also called the conditional FP-tree on $I$}@}. <!--SR:!2027-01-04,597,250!2026-04-09,456,270!2026-04-16,476,270!2031-09-01,2038,330!2026-03-06,418,250!2027-05-22,680,250!2030-09-03,1776,330-->

After {@{iterating through the header table}@}, {@{the union of all previously saved frequent item sets during the iteration, plus the empty set}@}, are {@{the frequent item sets of the database $D$}@}. We can also {@{attach the count of each frequent item set}@} by {@{adding the number of transactions in the entire database as the count of the empty set}@}, and {@{the previously saved frequent item sets already have counts}@} as they are {@{generated _recursively_ by the this growth step}@}. If {@{the database $D$ is the entire database}@}, i.e. not {@{the sub-database from the _recursive_ step described above}@}, {@{remove the empty set}@} depending on {@{whether you consider the empty set as a frequent item set}@}. {@{An edge case}@} is that if {@{the number of transactions in the entire database $D$ is less than the support threshold}@}, then {@{the empty set should always be removed}@}. <!--SR:!2028-02-29,916,270!2029-12-01,1396,270!2028-11-17,1225,310!2030-07-21,1648,310!2027-03-02,437,380!2027-03-06,440,380!2027-02-28,435,380!2027-03-01,436,380!2027-03-06,440,380!2027-02-27,434,380!2027-02-24,432,380!2027-03-05,439,380!2027-02-19,427,380!2027-02-23,431,380-->

The reason why we {@{add the the empty set before returning the frequent item sets}@} is {@{mainly for the recursive step}@}, where {@{the transactions in the provided sub-database}@} are {@{already conditional on an item identified by the parent step}@}. {@{The empty set}@} simply represents {@{that item is a frequent item set}@}, keeping in mind that {@{the parent step will _add back_ that item to the empty set}@}. In fact, it is not necessary to {@{use an empty set}@} if {@{the above algorithm is _slightly modified_}@}: {@{Ignore all steps related to the empty set}@}, and instead when {@{_adding back_ item $I$ to the new frequent item sets}@}, additionally add {@{an item set with only item $I$}@} and, if needed, attach it {@{a count of the number of transactions in the sub-database $D_I$}@}. Note that this _slightly modified_ algorithm will not {@{return an empty set as a frequent item set in any circumstances}@}, but this is {@{easily fixed and might be even desirable}@}. <!--SR:!2030-11-24,1828,330!2030-09-09,1681,290!2027-05-31,811,290!2026-04-05,186,250!2026-04-16,512,310!2026-09-21,277,371!2027-03-18,424,391!2026-04-20,95,378!2026-04-16,91,378!2026-04-17,92,378!2026-04-20,95,378!2026-04-21,96,378!2026-04-11,86,378!2026-04-20,95,378!2026-04-15,90,378-->

#### growth shortcut

While the above algorithm is now complete as described, there is {@{a special case in which we can shortcut the growth step}@}. If, after constructing the FP-tree, the FP-tree {@{is a chain, i.e. every node has at most one child, which includes the tree with only the root node}@}, then the frequent item sets are {@{all possible subsets of the set of items in the entire chain, including the empty set and the whole set itself}@}. The number of subsets should be {@{$2^H$, where $H$ is the height of the chain}@}.  (Note that the height of a chain with the root node only is {@{0, not 1}@}.) Their corresponding item set counts are {@{the minimums of the counts of the items in the item set, i.e. item count of the deepest node. For the empty set, it is the number of transactions in the provided database $D$}@}. If the _slightly modified_ algorithm is used, {@{always remove the empty set}@}. <!--SR:!2026-08-19,652,330!2026-03-09,508,310!2029-01-25,1271,310!2026-07-01,612,310!2030-10-13,1810,330!2030-09-08,1697,310!2027-11-18,1001,348-->

One can prove that the shortcut above {@{produces the same result as without using the shortcut}@}. <!--SR:!2028-06-20,1188,350-->

### association rule creation

Creation of association rules from the frequent item sets is {@{not covered by this algorithm}@}. <!--SR:!2029-03-23,1402,350-->

## the algorithm

### Python implementation

See [`FP-growth algorithm.py`](attachments/FP-growth%20algorithm.py) for a runnable example in [Python](Python%20(programming%20language).md).

## complexity

Time-wise, building the FP-tree {@{only requires one (or two, depending on how you define "scan") scan, and inserting one transaction into the FP-tree only grows with the number of frequent items in the transaction}@}. This is good especially if {@{the entire database is IO-bounded and too large to be fitted into memory}@}. <!--SR:!2029-07-05,1450,330!2029-05-20,1380,310-->

Space-wise, the FP-tree size, i.e. number of nodes, is {@{bounded by the number of frequent item set patterns, and is usually much less than the bound}@}. The height of the FP-tree, is {@{bounded by the maximum number of items in a frequent item set}@}. This is good because it means {@{the FP-tree can be fitted into memory even if the database is very large}@}. <!--SR:!2027-08-07,821,270!2027-01-16,681,270!2026-07-04,594,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/FP-growth_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
