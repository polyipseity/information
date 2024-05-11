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

- 6 major topics ::: association, clustering, classification, data warehouse, dimension reduction, web database <!--SR:!2024-07-14,89,250!2025-01-13,260,330-->
- association ::: Finding frequent _patterns_, e.g. frequent items and _item sets_, and _association rules_, e.g. the likelihood of A implying B. <!--SR:!2024-08-25,132,290!2024-11-21,218,330-->
- clustering ::: Finding all _clusters_, e.g. the clusters of items after graphing them in a 2D graph. <!--SR:!2024-11-05,191,310!2025-02-08,282,330-->
- classification ::: _Predict_ results given some input data, e.g. decision trees. <!--SR:!2024-08-01,115,290!2025-02-16,286,330-->
- data warehouse ::: Knowledge database containing _pre-computed_ results from data sources. <!--SR:!2024-10-09,180,310!2024-09-17,154,310-->
- dimension reduction ::: Reducing _dimensionality_ while minimizing _information loss_. One can visualize this by imagine many data points lying close to a line in a $xy$ graph. Then instead of representing each data point with two numbers, $x$ and $y$, we can represent each data point with one number representing the distance from the origin to the point on the line closest to the original data point. Information loss is the distance between the original point and the point on the line closest to the origin point. <!--SR:!2024-07-29,115,290!2024-11-16,199,310-->
- web database ::: Using data from the web, e.g. ranking webpages. <!--SR:!2025-02-05,278,330!2025-02-28,295,330-->
- [delimiter](../../../../general/delimiter.md) definition ::: The text each data point is separated by. For example, `column 1,column 2,column 3` is delimited by `,`. <!--SR:!2025-01-23,269,330!2025-01-13,261,330-->

## week 2 lecture 1

- [association rule learning § support](../../../../general/association%20rule%20learning.md#support)
- support definition ::: We use "the number of transactions containing $X$" definition here. <!--SR:!2025-01-08,256,330!2024-12-23,244,330-->
- [association rule learning § confidence](../../../../general/association%20rule%20learning.md#confidence)
- [association rule learning § lift](../../../../general/association%20rule%20learning.md#lift)
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)

## week 2 lecture 2

- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)

## week 3 lecture

- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)
- [Apriori algorithm § the algorithm](../../../../general/Apriori%20algorithm.md#the%20algorithm)
- [Apriori algorithm § limitations](../../../../general/Apriori%20algorithm.md#limitations)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)

## week 4 lecture 1

- [FP-growth algorithm § FP-tree](../../../../general/FP-growth%20algorithm.md#FP-tree)
- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
  - FP-growth algorithm growth step ::: We use the slightly modified algorithm, never return an empty item set, and use the growth shortcut. <!--SR:!2024-06-10,43,311!2024-06-11,47,327-->
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)

## week 4 tutorial

- topic: helping students who encountered problems of using XLMiner in our CSE lab and using XLMiner outside CSE Lab
- [Analytics Solver usage § installation](../../../Analytic%20Solver%20usage.md#installation)

## week 4 lecture 2

- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)
- [FP-growth algorithm § complexity](../../../../general/FP-growth%20algorithm.md#complexity)
- [cluster analysis § applications](../../../../general/cluster%20analysis.md#applications)

## week 5 lecture 1

- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [_k_-means clustering § initialization methods](../../../../general/k-means%20clustering.md#initialization%20methods)
- [_k_-means clustering § discussion](../../../../general/k-means%20clustering.md#discussion)
- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
  - _k_-means clustering variations ::: We only teach original _k_-means, sequential _k_-means and forgetful sequential _k_-means. <!--SR:!2024-06-07,43,331!2024-06-10,46,331-->

## week 5 tutorial

- topic: using XLMiner for association rule mining
- [association rule learning § useful concepts](../../../../general/association%20rule%20learning.md#useful%20concepts)
- [association rule learning § algorithms](../../../../general/association%20rule%20learning.md#algorithms)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)

## week 5 lecture 2

- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
- [Analytics Solver usage § random seed](../../../Analytic%20Solver%20usage.md#random%20seed)
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
  - cluster linkage ::: We only teach single-linkage, centroid linkage, complete-linkage, group average linkage (unweighted average linkage), median linkage, McQuitty's method (weighted average linkage), and Ward's method (minimum increase of sum of squares). <!--SR:!2024-05-21,27,291!2024-06-08,44,327-->
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)

## week 6 lecture 1

- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisive%20clustering)
  - divisive clustering ::: We prefer divisive clustering to stop after a certain amount of clusters are created instead of using the [dendrogram](../../../../general/dendrogram.md). <!--SR:!2024-05-21,27,291!2024-06-18,52,327-->
- [hierarchial clustering § monothetic clustering](../../../../general/hierarchical%20clustering.md#monothetic%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)

## week 6 tutorial

- topic: how to do in-class exercise 2 (FP-tree) and additional exercise (FP-tree)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)

## week 6 lecture 2

- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)
- [statistical classification § application domains](../../../../general/statistical%20classification.md#application%20domains)
  - similarities and differences between classification and clustering ::: They are both data analysis. The difference is that classification has a target attribute or variable while clustering does not. <!--SR:!2024-07-05,66,351!2024-06-02,36,307-->
- [statistical classification § algorithms](../../../../general/statistical%20classification.md#application%20algorithms)
  - statistical classification algorithms ::: We only teach decision tree, bayesian classifier, and nearest neighbor classifier. <!--SR:!2024-07-05,62,331!2024-06-06,40,311-->
- [entropy](../../../../general/entropy%20(information%20theory).md)
  - entropy base ::: We use base 2. <!--SR:!2024-07-11,71,347!2024-07-22,80,347-->

## week 7 lecture 1

- [entropy](../../../../general/entropy%20(information%20theory).md)
- [decision tree learning § algorithms](../../../../general/decision%20tree%20learning.md#algorithms)
  - decision tree learning algorithms ::: We only teach ID3 algorithm, C4.5 algorithm, and CART. <!--SR:!2024-07-17,76,351!2024-06-16,50,327-->
- [ID3 § algorithm](../../../../general/ID3%20algorithm.md#algorithm)
- [information gain § general definition](../../../../general/information%20gain%20(decision%20tree).md#general%20definition)
- [conditional entropy § definition](../../../../general/conditional%20entropy.md#definition)
- [ID3 § properties](../../../../general/ID3%20algorithm.md#properties)
- [C4.5 § algorithm](../../../../general/C4.5%20algorithm.md#algorithm)
  - split information of an attribute ::: It can be the entropy of the attribute in the entire set or the set of the decision node. The former is preferred. <!--SR:!2024-06-04,35,320!2024-07-17,69,340-->
- [information gain ratio § definition](../../../../general/information%20gain%20ratio.md#definition)
- [classification and regression tree § algorithm](../../../../general/classification%20and%20regression%20tree.md#algorithm)
- [decision tree learning § Gini impurity](../../../../general/decision%20tree%20learning.md#Gini%20impurity)

## week 7 tutorial

- topic: using XLMiner for _k_-means and hierarchical clustering
- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisibe%20clustering)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)

## week 7 lecture 2

- [confusion matrix](../../../../general/confusion%20matrix.md)
  - confusion matrix format ::: Each row represents an actual class while each column represents a predicted class. <!--SR:!2024-06-11,42,320!2024-07-12,64,340-->
- [confusion matrix § error report](../../../../general/confusion%20matrix.md#error%20report)
- [lift chart](../../../lift%20chart.md)
- [lift chart § construction](../../../lift%20chart.md#construction)
- [lift chart § interpretation](../../../lift%20chart.md#interpretation)
- [lift chart § decile-wise](../../../lift%20chart.md#decile-wise)
- other classification performance measures ::: We will teach F1-score, precision, recall, specificity, and more later. <!--SR:!2024-05-19,26,291!2024-06-14,48,327-->
- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)

## week 8 lecture 1

- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)
- exam format voting
  - bonus question (+10%, max 100%): no
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 70 minutes
  - types: 80% long questions, 20% multiple choice questions
- [naive Bayes classifier § probabilistic model](../../../../general/naive%20Bayes%20classifier.md#probabilistic%20model)
- [Bayes' theorem § statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
- [conditional probability § Kolmogorov definition](../../../../general/conditional%20probability.md#Kolmogorov%20definition)
