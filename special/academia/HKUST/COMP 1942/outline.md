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

- 6 major topics ::: association, clustering, classification, data warehouse, dimension reduction, web database <!--SR:!2024-03-11,14,250!2024-04-28,61,310-->
- association ::: Finding frequent _patterns_, e.g. frequent items and _item sets_, and _association rules_, e.g. the likelihood of A implying B. <!--SR:!2024-04-13,46,290!2024-04-17,51,310-->
- clustering ::: Finding all _clusters_, e.g. the clusters of items after graphing them in a 2D graph. <!--SR:!2024-04-28,62,310!2024-05-02,65,310-->
- classification ::: _Predict_ results given some input data, e.g. decision trees. <!--SR:!2024-04-06,40,290!2024-05-05,67,310-->
- data warehouse ::: Knowledge database containing _pre-computed_ results from data sources. <!--SR:!2024-04-12,45,290!2024-04-16,50,310-->
- dimension reduction ::: Reducing _dimensionality_ while minimizing _information loss_. One can visualize this by imagine many data points lying close to a line in a $xy$ graph. Then instead of representing each data point with two numbers, $x$ and $y$, we can represent each data point with one number representing the distance from the origin to the point on the line closest to the original data point. Information loss is the distance between the original point and the point on the line closest to the origin point. <!--SR:!2024-03-25,31,270!2024-05-01,64,310-->
- web database ::: Using data from the web, e.g. ranking webpages. <!--SR:!2024-05-03,65,310!2024-05-07,69,310-->
- [delimiter](../../../../general/delimiter.md) definition ::: The text each data point is separated by. For example, `column 1,column 2,column 3` is delimited by `,`. <!--SR:!2024-04-29,63,310!2024-04-27,61,310-->

## week 2 lecture 1

- [association rule learning § support](../../../../general/association%20rule%20learning.md#support)
- support definition ::: We use "the number of transactions containing $X$" definition here. <!--SR:!2024-04-26,60,310!2024-04-23,57,310-->
- [association rule learning § confidence](../../../../general/association%20rule%20learning.md#confidence)
- [association rule learning § lift](../../../../general/association%20rule%20learning.md#lift)
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

## week 4 lecture 2

- [association rule learning § FP-growth algorithm](../../../../general/association%20rule%20learning.md#FP-growth%20algorithm)
