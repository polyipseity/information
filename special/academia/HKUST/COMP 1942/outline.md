---
aliases:
  - COMP 1942
  - COMP 1942 outline
  - COMP1942
  - COMP1942 outline
  - HKUST COMP 1942
  - HKUST COMP 1942 outline
  - HKUST COMP1942
  - HKUST COMP1942 outline
tags:
  - flashcard/special/academia/HKUST/COMP_1942/outline
  - functional/outline
  - language/in/English
---

# HKUST COMP 1942 outline

The content is in teaching order.

## week 1 lecture

- 6 major topics ::: association, clustering, classification, data warehouse, dimension reduction, web database
  - association ::: Finding frequent _patterns_, e.g. frequent items and _item sets_, and _association rules_, e.g. the likelihood of A implying B.
  - clustering ::: Finding all _clusters_, e.g. the clusters of items after graphing them in a 2D graph.
  - classification ::: _Predict_ results given some input data, e.g. decision trees.
  - data warehouse ::: Knowledge database containing _pre-computed_ results from data sources.
  - dimension reduction ::: Reducing _dimensionality_ while minimizing _information loss_. One can visualize this by imagine many data points lying close to a line in a $xy$ graph. Then instead of representing each data point with two numbers, $x$ and $y$, we can represent each data point with one number representing the distance from the origin to the point on the line closest to the original data point. Information loss is the distance between the original point and the point on the line closest to the origin point.
  - web database ::: Using data from the web, e.g. ranking webpages.
- [delimiter](../../../../general/delimiter.md) definition ::: The text each data point is separated by. For example, `column 1,column 2,column 3` is delimited by `,`.

## week 2 lecture 1

- [association rule learning § support](../../../../general/association%20rule%20learning.md#support)
  - support definition ::: We use "the number of transactions containing $X$" definition here.
- [association rule learning § confidence](../../../../general/association%20rule%20learning.md#confidence)
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)

## week 2 lecture 2

- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)

## week 3 lecture

- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)
- [Apriori algorithm § limitations](../../../../general/Apriori%20algorithm.md#limitations)
- [association rule learning § FP-growth algorithm](../../../../general/association%20rule%20learning.md#FP-growth%20algorithm)

## week 4 lecture 1

- [association rule learning § FP-growth algorithm](../../../../general/association%20rule%20learning.md#FP-growth%20algorithm)
