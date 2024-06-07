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

- time: 2024-01-31T09:00:00+08:00/2024-01-31T10:30:00+08:00
- 6 major topics ::: association, clustering, classification, data warehouse, dimension reduction, web database
  - association ::: Finding frequent _patterns_, e.g. frequent items and _item sets_, and _association rules_, e.g. the likelihood of A implying B.
  - clustering ::: Finding all _clusters_, e.g. the clusters of items after graphing them in a 2D graph.
  - classification ::: _Predict_ results given some input data, e.g. decision trees.
  - data warehouse ::: Knowledge database containing _pre-computed_ results from data sources.
  - dimension reduction ::: Reducing _dimensionality_ while minimizing _information loss_. One can visualize this by imagine many data points lying close to a line in a $xy$ graph. Then instead of representing each data point with two numbers, $x$ and $y$, we can represent each data point with one number representing the distance from the origin to the point on the line closest to the original data point. Information loss is the distance between the original point and the point on the line closest to the origin point.
  - web database ::: Using data from the web, e.g. ranking webpages.
- [delimiter](../../../../general/delimiter.md) definition ::: The text each data point is separated by. For example, `column 1,column 2,column 3` is delimited by `,`.

## week 2 lecture 1

- time: 2024-02-05T09:00:00+08:00/2024-02-05T10:30:00+08:00
- [association rule learning § support](../../../../general/association%20rule%20learning.md#support)
  - support definition ::: We use "the number of transactions containing $X$" definition here.
- [association rule learning § confidence](../../../../general/association%20rule%20learning.md#confidence)
- [association rule learning § lift](../../../../general/association%20rule%20learning.md#lift)
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)

## week 2 lecture 2

- time: 2024-02-07T09:00:00+08:00/2024-02-07T10:30:00+08:00
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)

## week 3 lecture

- time: 2024-02-14T09:00:00+08:00/2024-02-14T10:30:00+08:00
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)
- [Apriori algorithm § the algorithm](../../../../general/Apriori%20algorithm.md#the%20algorithm)
- [Apriori algorithm § limitations](../../../../general/Apriori%20algorithm.md#limitations)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)

## week 4 lecture 1

- time: 2024-02-19T09:00:00+08:00/2024-02-19T10:30:00+08:00
- [FP-growth algorithm § FP-tree](../../../../general/FP-growth%20algorithm.md#FP-tree)
- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
  - FP-growth algorithm growth step ::: We use the slightly modified algorithm, never return an empty item set, and use the growth shortcut.
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)

## week 4 tutorial

- time: 2024-02-19T18:00:00+08:00/2024-02-19T19:00:00+08:00
- topic: helping students who encountered problems of using XLMiner in our CSE lab and using XLMiner outside CSE Lab
- [Analytics Solver usage § installation](../../../Analytic%20Solver%20usage.md#installation)

## week 4 lecture 2

- time: 2024-02-21T09:00:00+08:00/2024-02-21T10:30:00+08:00
- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)
- [FP-growth algorithm § complexity](../../../../general/FP-growth%20algorithm.md#complexity)
- [cluster analysis § applications](../../../../general/cluster%20analysis.md#applications)

## week 5 lecture 1

- time: 2024-02-26T09:00:00+08:00/2024-02-26T10:30:00+08:00
- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [_k_-means clustering § initialization methods](../../../../general/k-means%20clustering.md#initialization%20methods)
- [_k_-means clustering § discussion](../../../../general/k-means%20clustering.md#discussion)
- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
  - _k_-means clustering variations ::: We only teach original _k_-means, sequential _k_-means and forgetful sequential _k_-means.

## week 5 tutorial

- time: 2024-02-26T18:00:00+08:00/2024-02-26T19:00:00+08:00
- topic: using XLMiner for association rule mining
- [association rule learning § useful concepts](../../../../general/association%20rule%20learning.md#useful%20concepts)
- [association rule learning § algorithms](../../../../general/association%20rule%20learning.md#algorithms)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)
- [Analytics Solver usage § input formats](../../../Analytic%20Solver%20usage.md#input%20formats)
- [Analytics Solver usage § common parameters](../../../Analytic%20Solver%20usage.md#common%20parameters)

## week 5 lecture 2

- time: 2024-02-28T09:00:00+08:00/2024-02-28T10:30:00+08:00
- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
- [Analytics Solver usage § random seed](../../../Analytic%20Solver%20usage.md#random%20seed)
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
  - cluster linkage ::: We only teach single-linkage, centroid linkage, complete-linkage, group average linkage (unweighted average linkage), median linkage, McQuitty's method (weighted average linkage), and Ward's method (minimum increase of sum of squares).
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)

## week 6 lecture 1

- time: 2024-03-04T09:00:00+08:00/2024-03-04T10:30:00+08:00
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisive%20clustering)
  - divisive clustering ::: We prefer divisive clustering to stop after a certain amount of clusters are created instead of using the [dendrogram](../../../../general/dendrogram.md).
- [hierarchial clustering § monothetic clustering](../../../../general/hierarchical%20clustering.md#monothetic%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)

## week 6 tutorial

- time: 2024-03-04T18:00:00+08:00/2024-03-04T19:00:00+08:00
- topic: how to do in-class exercise 2 (FP-tree) and additional exercise (FP-tree)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)
- Jaccard's coefficient for binary data ::: [Jaccard index § similarity of asymmetric binary attributes](../../../../general/Jaccard%20index.md#similarity%20of%20asymmetric%20binary%20attributes)
- matching coefficient for binary data ::: [simple matching coefficient](../../../../general/simple%20matching%20coefficient.md)

## week 6 lecture 2

- time: 2024-03-06T09:00:00+08:00/2024-03-06T10:30:00+08:00
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)
- [statistical classification § application domains](../../../../general/statistical%20classification.md#application%20domains)
  - similarities and differences between classification and clustering ::: They are both data analysis. The difference is that classification has a target attribute or variable while clustering does not.
- [statistical classification § algorithms](../../../../general/statistical%20classification.md#application%20algorithms)
  - statistical classification algorithms ::: We only teach decision tree, bayesian classifier, and nearest neighbor classifier.
- [entropy](../../../../general/entropy%20(information%20theory).md)
  - entropy base ::: We use base 2.

## week 7 lecture 1

- time: 2024-03-11T09:00:00+08:00/2024-03-11T10:30:00+08:00
- [entropy](../../../../general/entropy%20(information%20theory).md)
- decision tree format ::: All nodes show the percentage of actual labels in that decision nodes. The internal nodes show the attribute being split on. The terminal nodes show the predicted label. Arrows point from top to bottom, and each is labelled with an inequality operating on the attribute, which decides whether an sample being predicted should go through said arrow.
- [decision tree learning § algorithms](../../../../general/decision%20tree%20learning.md#algorithms)
  - decision tree learning algorithms ::: We only teach ID3 algorithm, C4.5 algorithm, and CART.
- [ID3 § algorithm](../../../../general/ID3%20algorithm.md#algorithm)
- [information gain § general definition](../../../../general/information%20gain%20(decision%20tree).md#general%20definition)
- [conditional entropy § definition](../../../../general/conditional%20entropy.md#definition)
- [ID3 § properties](../../../../general/ID3%20algorithm.md#properties)
- [C4.5 § algorithm](../../../../general/C4.5%20algorithm.md#algorithm)
  - split information of an attribute ::: It can be the entropy of the attribute in the entire set or the set of the decision node. The former is preferred.
- [information gain ratio § definition](../../../../general/information%20gain%20ratio.md#definition)
- [classification and regression tree § algorithm](../../../../general/classification%20and%20regression%20tree.md#algorithm)
- [decision tree learning § Gini impurity](../../../../general/decision%20tree%20learning.md#Gini%20impurity)

## week 7 tutorial

- time: 2024-03-11T18:00:00+08:00/2024-03-11T19:00:00+08:00
- topic: using XLMiner for _k_-means and hierarchical clustering
- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisibe%20clustering)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)

## week 7 lecture 2

- time: 2024-03-13T09:00:00+08:00/2024-03-13T10:30:00+08:00
- [confusion matrix](../../../../general/confusion%20matrix.md)
  - confusion matrix format ::: Each row represents an actual class while each column represents a predicted class.
- [confusion matrix § error report](../../../../general/confusion%20matrix.md#error%20report)
- [lift chart](../../../lift%20chart.md)
- [lift chart § construction](../../../lift%20chart.md#construction)
- [lift chart § interpretation](../../../lift%20chart.md#interpretation)
- [lift chart § decile-wise](../../../lift%20chart.md#decile-wise)
- other classification performance measures ::: We will teach F1-score, precision, recall, specificity, and more later.
- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)

## week 8 lecture 1

- time: 2024-03-18T09:00:00+08:00/2024-03-18T10:30:00+08:00
- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)
- midterm exam format voting
  - bonus question (+10%, max 100%): no
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 70 minutes
  - types: 80% long questions, 20% multiple choice questions
- [naive Bayes classifier § probabilistic model](../../../../general/naive%20Bayes%20classifier.md#probabilistic%20model)
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md)
  - [§ statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
  - [§ Bayes' theorem for 3 events](../../../../general/Bayes'%20theorem.md#Bayes'%20theorem%20for%203%20events)
- [conditional probability § Kolmogorov definition](../../../../general/conditional%20probability.md#Kolmogorov%20definition)

<!--
- final exam format voting
  - bonus question (+10%, max 100%): no
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 150 minutes
  - types: 100% short or long questions, 0% multiple choice questions
-->
