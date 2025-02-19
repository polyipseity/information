---
aliases:
  - hierarchical cluster
  - hierarchical clustering
  - hierarchical clusters
tags:
  - flashcard/active/general/eng/hierarchical_clustering
  - language/in/English
---

# hierarchical clustering

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

In [data mining](data%20mining.md) and [statistics](statistics.md), __hierarchical clustering__ is {@{a method of [cluster analysis](cluster%20analysis.md) that builds a [hierarchy](hierarchy.md) of clusters}@}. The methods can be classified into two main types: {@{__agglomerative__, a [bottom-up](bottom–up%20and%20top–down%20design.md) approach that starts by making a cluster for each point, and then merge pairs of clusters repeatedly}@}; and {@{__divisive__, a [top-down](bottom–up%20and%20top–down%20design.md) approach that starts by making a cluster containing every point, and then splitting the cluster into two clusters repeatedly}@}. <!--SR:!2026-02-10,499,315!2025-06-27,300,295!2026-11-16,688,295-->

The merges and splits are {@{usually [greedy](greedy%20algorithm.md)}@}. The results of hierarchical clustering can be represented as {@{a [dendrogram](dendrogram.md), a [tree](tree.md)-shaped diagram, with a horizontal ruler at the bottom indicating the distance when the clusters are merged or split}@}. <!--SR:!2025-10-09,394,295!2025-07-14,312,295-->

## cluster linkage

To determine the distance between two observations, {@{a _[metric](metric%20(mathematics).md)_, usually the [Euclidean distance](Euclidean%20distance.md)}@} is needed. To decide how to merge or split clusters, {@{a measure of _dissimilarity_ between clusters}@} is required. The metric is {@{insufficient, and a linkage criterion is also needed, which specifies the _dissimilarity_ of clusters as a function of the pairwise distances of observations in the clusters, or a function of the properties of the clusters before being combined}@}. <!--SR:!2025-04-25,291,335!2026-09-12,675,335!2025-08-01,324,295-->

Both the choice of the metric and the linkage criterion {@{affects the clustering results significantly}@}. The metric affects {@{which observations are similar}@} more, while the linkage affects {@{the cluster shapes}@} more. <!--SR:!2026-05-16,564,315!2026-03-02,515,315!2025-06-01,321,335-->

Some commonly used linkage criterion given two clusters _A_ and _B_ and a _[distance](distance.md)_ function $d$ are:

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
headers = (R"cluster linkage", R"aliases", R"formula", R"description")
table = (
  (R"[Ward's method](Ward's%20method.md)", R"MISSQ, minimum increase of sum of squares", R"$d(A, B) = \frac {\lvert A \rvert \cdot \lvert B \rvert} {\lvert A \cup B \rvert} \lVert \mu_A - \mu_B \rVert^2 = \sum_{x \in A \cup B} \lVert x - \mu_{A \cup B} \rVert^2 - \sum_{x \in A} \lVert x - \mu_A \rVert^2 - \sum_{x \in B} \lVert x - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$", R"It is also known as the information loss, defined as the increase in the squared error after merging multiple clusters."),
  (R"centroid linkage clustering", R"UPGMC, unweighted centroid clustering", R"$d(A, B) = \lVert \mu_A - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$", R"Squaring the distance is optional. Centroid linkage clustering does not preserve well small clusters that are merged into large clusters."),
  (R"[complete-linkage clustering](complete-linkage%20clustering.md)", R"maximum linkage clustering", R"$d(A, B) = \max_{a \in A, b \in B} d(a, b)$", R""),
  (R"median linkage clustering", R"WPGMC, weighted centroid clustering", R"$d(A \cup B, *) = d\left( \frac {m_A + m_B} 2, m_* \right)$, where $m_*$ is the [medoid](medoid.md) of the cluster $*$", R"Median linkage clustering can better preserve small clusters that are merged into large clusters."),
  (R"[single-linkage clustering](single-linkage%20clustering.md)", R"minimum linkage clustering, nearest neighbor technique", R"$d(A, B) = \min_{a \in A, b \in B} d(a, b)$", R""),
  (R"unweighted average linkage clustering", R"[UPGMA](UPGMA.md), group average linkage clustering", R"$d(A, B) = \frac 1 {\lvert A \rvert \cdot \lvert B \rvert} \sum_{a \in A} \sum_{b \in B} d(a, b)$", R""),
  (R"weighted average linkage clustering", R"McQuitty's Method, [WPGMA](WPGMA.md)", R"$d(A \cup B, *) = \frac {d(A, *) + d(B, *)} 2$", R""),
)
return chain.from_iterable(await gather(
  memorize_table(
    __env__.cwf_sects("84ba", "c471"),
    headers, table,
    lambda datum: (*datum[:-1], cloze(datum[-1])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "e892", "259f"),
    items_to_map(*((row[0], row[1]) for row in table if row[1])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "0196", "ff72"),
    items_to_map(*((row[0], row[2]) for row in table if row[2])),
  ),
))
```

<!--pytextgen generate section="84ba"--><!-- The following content is generated at 2024-04-12T10:15:07.411820+08:00. Any edits will be overridden! -->

> | cluster linkage | aliases | formula | description |
> |-|-|-|-|
> | [Ward's method](Ward's%20method.md) | MISSQ, minimum increase of sum of squares | $d(A, B) = \frac {\lvert A \rvert \cdot \lvert B \rvert} {\lvert A \cup B \rvert} \lVert \mu_A - \mu_B \rVert^2 = \sum_{x \in A \cup B} \lVert x - \mu_{A \cup B} \rVert^2 - \sum_{x \in A} \lVert x - \mu_A \rVert^2 - \sum_{x \in B} \lVert x - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$ | {@{It is also known as the information loss, defined as the increase in the squared error after merging multiple clusters.}@} |
> | centroid linkage clustering | UPGMC, unweighted centroid clustering | $d(A, B) = \lVert \mu_A - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$ | {@{Squaring the distance is optional. Centroid linkage clustering does not preserve well small clusters that are merged into large clusters.}@} |
> | [complete-linkage clustering](complete-linkage%20clustering.md) | maximum linkage clustering | $d(A, B) = \max_{a \in A, b \in B} d(a, b)$ |  |
> | median linkage clustering | WPGMC, weighted centroid clustering | $d(A \cup B, *) = d\left( \frac {m_A + m_B} 2, m_* \right)$, where $m_*$ is the [medoid](medoid.md) of the cluster $*$ | {@{Median linkage clustering can better preserve small clusters that are merged into large clusters.}@} |
> | [single-linkage clustering](single-linkage%20clustering.md) | minimum linkage clustering, nearest neighbor technique | $d(A, B) = \min_{a \in A, b \in B} d(a, b)$ |  |
> | unweighted average linkage clustering | [UPGMA](UPGMA.md), group average linkage clustering | $d(A, B) = \frac 1 {\lvert A \rvert \cdot \lvert B \rvert} \sum_{a \in A} \sum_{b \in B} d(a, b)$ |  |
> | weighted average linkage clustering | McQuitty's Method, [WPGMA](WPGMA.md) | $d(A \cup B, *) = \frac {d(A, *) + d(B, *)} 2$ |  | <!--SR:!2025-07-27,318,290!2025-12-02,449,315!2025-08-03,314,289-->

<!--/pytextgen-->

<!--pytextgen generate section="c471"--><!-- The following content is generated at 2024-03-25T02:33:59.339528+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[Ward's method](Ward's%20method.md) <!--SR:!2025-04-30,295,335!2025-05-04,299,335-->
- [Ward's method](Ward's%20method.md)→::@::←centroid linkage clustering <!--SR:!2026-02-11,421,275!2026-11-23,671,315-->
- centroid linkage clustering→::@::←[complete-linkage clustering](complete-linkage%20clustering.md) <!--SR:!2025-10-30,385,295!2025-04-22,238,275-->
- [complete-linkage clustering](complete-linkage%20clustering.md)→::@::←median linkage clustering <!--SR:!2025-02-24,203,275!2025-08-11,331,275-->
- median linkage clustering→::@::←[single-linkage clustering](single-linkage%20clustering.md) <!--SR:!2025-05-08,252,275!2025-12-11,415,295-->
- [single-linkage clustering](single-linkage%20clustering.md)→::@::←unweighted average linkage clustering <!--SR:!2025-10-05,362,295!2025-04-26,213,235-->
- unweighted average linkage clustering→::@::←weighted average linkage clustering <!--SR:!2025-03-03,175,275!2025-05-29,279,295-->
- weighted average linkage clustering→::@::←_(end)_ <!--SR:!2027-10-04,960,335!2025-06-03,212,295-->

<!--/pytextgen-->

### cluster linkage–aliases

<!--pytextgen generate section="e892"--><!-- The following content is generated at 2024-04-12T02:13:02.070775+08:00. Any edits will be overridden! -->

- [Ward's method](Ward's%20method.md):@:MISSQ, minimum increase of sum of squares <!--SR:!2025-04-24,225,255-->
- centroid linkage clustering:@:UPGMC, unweighted centroid clustering <!--SR:!2026-03-10,465,295-->
- [complete-linkage clustering](complete-linkage%20clustering.md):@:maximum linkage clustering <!--SR:!2026-12-10,744,335-->
- median linkage clustering:@:WPGMC, weighted centroid clustering <!--SR:!2025-07-21,279,255-->
- [single-linkage clustering](single-linkage%20clustering.md):@:minimum linkage clustering, nearest neighbor technique <!--SR:!2025-02-28,247,335-->
- unweighted average linkage clustering:@:[UPGMA](UPGMA.md), group average linkage clustering <!--SR:!2025-09-05,347,295-->
- weighted average linkage clustering:@:McQuitty's Method, [WPGMA](WPGMA.md) <!--SR:!2025-05-06,236,255-->

<!--/pytextgen-->

<!--pytextgen generate section="259f"--><!-- The following content is generated at 2024-04-12T02:13:02.092326+08:00. Any edits will be overridden! -->

- MISSQ, minimum increase of sum of squares:@:[Ward's method](Ward's%20method.md) <!--SR:!2027-04-29,801,335-->
- UPGMC, unweighted centroid clustering:@:centroid linkage clustering <!--SR:!2026-09-23,629,315-->
- maximum linkage clustering:@:[complete-linkage clustering](complete-linkage%20clustering.md) <!--SR:!2025-03-28,269,335-->
- WPGMC, weighted centroid clustering:@:median linkage clustering <!--SR:!2025-06-17,289,275-->
- minimum linkage clustering, nearest neighbor technique:@:[single-linkage clustering](single-linkage%20clustering.md) <!--SR:!2025-03-21,265,335-->
- [UPGMA](UPGMA.md), group average linkage clustering:@:unweighted average linkage clustering <!--SR:!2026-10-26,631,295-->
- McQuitty's Method, [WPGMA](WPGMA.md):@:weighted average linkage clustering <!--SR:!2025-05-13,267,295-->

<!--/pytextgen-->

### cluster linkage–formula

<!--pytextgen generate section="0196"--><!-- The following content is generated at 2024-04-12T10:15:07.434836+08:00. Any edits will be overridden! -->

- [Ward's method](Ward's%20method.md):@:$d(A, B) = \frac {\lvert A \rvert \cdot \lvert B \rvert} {\lvert A \cup B \rvert} \lVert \mu_A - \mu_B \rVert^2 = \sum_{x \in A \cup B} \lVert x - \mu_{A \cup B} \rVert^2 - \sum_{x \in A} \lVert x - \mu_A \rVert^2 - \sum_{x \in B} \lVert x - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$ <!--SR:!2025-03-18,82,255-->
- centroid linkage clustering:@:$d(A, B) = \lVert \mu_A - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$ <!--SR:!2026-01-06,466,315-->
- [complete-linkage clustering](complete-linkage%20clustering.md):@:$d(A, B) = \max_{a \in A, b \in B} d(a, b)$ <!--SR:!2025-03-06,252,335-->
- median linkage clustering:@:$d(A \cup B, *) = d\left( \frac {m_A + m_B} 2, m_* \right)$, where $m_*$ is the [medoid](medoid.md) of the cluster $*$ <!--SR:!2025-06-11,274,275-->
- [single-linkage clustering](single-linkage%20clustering.md):@:$d(A, B) = \min_{a \in A, b \in B} d(a, b)$ <!--SR:!2025-02-23,243,335-->
- unweighted average linkage clustering:@:$d(A, B) = \frac 1 {\lvert A \rvert \cdot \lvert B \rvert} \sum_{a \in A} \sum_{b \in B} d(a, b)$ <!--SR:!2026-02-02,453,275-->
- weighted average linkage clustering:@:$d(A \cup B, *) = \frac {d(A, *) + d(B, *)} 2$ <!--SR:!2026-05-13,575,315-->

<!--/pytextgen-->

<!--pytextgen generate section="ff72"--><!-- The following content is generated at 2024-04-12T10:15:07.423835+08:00. Any edits will be overridden! -->

- $d(A, B) = \frac {\lvert A \rvert \cdot \lvert B \rvert} {\lvert A \cup B \rvert} \lVert \mu_A - \mu_B \rVert^2 = \sum_{x \in A \cup B} \lVert x - \mu_{A \cup B} \rVert^2 - \sum_{x \in A} \lVert x - \mu_A \rVert^2 - \sum_{x \in B} \lVert x - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$:@:[Ward's method](Ward's%20method.md) <!--SR:!2025-12-04,432,295-->
- $d(A, B) = \lVert \mu_A - \mu_B \rVert^2$, where $\mu_*$ is the [centroid](centroid.md) of the cluster $*$:@:centroid linkage clustering <!--SR:!2026-10-30,653,315-->
- $d(A, B) = \max_{a \in A, b \in B} d(a, b)$:@:[complete-linkage clustering](complete-linkage%20clustering.md) <!--SR:!2025-05-22,313,335-->
- $d(A \cup B, *) = d\left( \frac {m_A + m_B} 2, m_* \right)$, where $m_*$ is the [medoid](medoid.md) of the cluster $*$:@:median linkage clustering <!--SR:!2025-10-05,404,315-->
- $d(A, B) = \min_{a \in A, b \in B} d(a, b)$:@:[single-linkage clustering](single-linkage%20clustering.md) <!--SR:!2025-04-13,282,335-->
- $d(A, B) = \frac 1 {\lvert A \rvert \cdot \lvert B \rvert} \sum_{a \in A} \sum_{b \in B} d(a, b)$:@:unweighted average linkage clustering <!--SR:!2026-12-26,760,335-->
- $d(A \cup B, *) = \frac {d(A, *) + d(B, *)} 2$:@:weighted average linkage clustering <!--SR:!2026-01-17,432,295-->

<!--/pytextgen-->

## agglomerative clustering

Note that [distance](distance.md) described below is {@{the measure of _dissimilarity_ between clusters as described in [§ cluster linkage](#cluster%20linkage)<!-- flashcard a2c1b40f-e67e-45fd-ad01-b9449a7c2df4 -->}@}, so the method is applicable to {@{any distance functions and [cluster linkages](#cluster%20linkage)<!-- flashcard 9bb1c2ee-7fda-427b-8bc0-8af05b09ab26-->}@}. <!--SR:!2025-09-03,354,309!2025-03-21,246,329-->

To perform agglomerative clustering, initially {@{create a cluster for each observation, containing the observation itself}@}. Then {@{find the pair of clusters that has the least [distance](distance.md) (arbitrarily choose one if there are multiple satisfying pairs) and merge them}@}. Keep track of the {@{merge history by drawing a [dendrogram](dendrogram.md), also noting the distance of the two clusters when merging in the dendrogram}@}. Repeat this until {@{you have only one cluster left}@}. Then your dendrogram is the result, and {@{you can choose to cut the dendrogram at any distance to get the desirable number of clusters}@}. <!--SR:!2025-09-18,356,295!2026-07-30,534,275!2026-08-27,554,275!2025-03-27,248,295!2026-03-28,466,270-->

One way to implement this is, after creating a cluster for each observation, {@{construct a [distance matrix](distance%20matrix.md) of all clusters, where the number in the _i_-th row and _j_-th column is the [distance](distance.md) between the _i_-th and _j_-th clusters}@}. Use the matrix to {@{identify the pair of clusters with the least distance}@}. After merging the pair of clusters, {@{the distance matrix should decrease in dimension by one in both axes. Update the distances to the new merged cluster from other untouched clusters}@}. Repeat this until {@{you have only one cluster left}@}. An optimization is that since distance is symmetric, we can use {@{a lower [triangular matrix](triangular%20matrix.md) to store the distances}@}. <!--SR:!2026-04-10,528,295!2026-07-14,578,315!2025-11-15,394,295!2026-05-21,568,315!2025-08-04,355,315-->

## divisive clustering

Note that [distance](distance.md) described below is {@{the measure of _dissimilarity_ between clusters as described in [§ cluster linkage](#cluster%20linkage)<!-- flashcard 1c9bde9b-954f-4d41-b1c9-3c62095fb6a7 -->}@}, so the method is applicable to {@{any distance functions and [cluster linkages](#cluster%20linkage)<!-- flashcard bf2e7702-5a6b-460b-a424-475b27c6f443 -->}@}. <!--SR:!2026-12-06,736,329!2025-03-24,249,329-->

The basic principle of divisive clustering was {@{published as the DIANA (DIvisive ANAlysis clustering) algorithm}@}.<sup>[\[1\]](#^ref-Kaufman-2009)</sup> <!--SR:!2027-05-01,854,335-->

Initially, {@{create a cluster that contain all observations}@}. Find the cluster {@{that has two or more items, and has the largest [diameter](diameter.md). Diameter of a cluster is the [distance](distance.md) between two furthest observations apart in the cluster}@}. Then, in said cluster, {@{find the observation that has the highest distance from the belonging cluster excluding the observation itself}@}. Next, {@{move the observation from said cluster to a new _splinter cluster_}@}. Now, keep {@{moving observations one by one from the old cluster to the new cluster}@}. To choose the observation to be moved, {@{calculate the _dissimilarity difference_ for each observation in the old cluster}@}. The _dissimilarity difference_ of an observation in the old cluster is {@{the distance of the observation to the old cluster excluding the observation itself, subtracted by the distance of the observation to the new cluster}@}. Move the observation {@{with the highest nonnegative _dissimilarity difference_ (arbitrarily choose one if there are multiple satisfying observations)}@}. If all _dissimilarity differences_ are negative, {@{stop moving the observations}@}. If there is only one item left, {@{keep the cluster, considering that the _dissimilarity difference_ can no longer be defined}@}. Repeat the above steps {@{until you reach the desirable number of clusters}@}. <!--SR:!2025-03-15,260,335!2025-07-12,277,255!2025-06-13,257,255!2025-09-22,359,295!2025-09-11,319,255!2026-04-14,479,275!2025-07-04,269,255!2025-05-14,255,275!2025-08-04,324,295!2025-07-27,285,255!2025-06-26,313,295-->

Alternatively, repeat the above steps until {@{the number of clusters equals the number of observations}@}. Construct {@{a [dendrogram](dendrogram.md) by letting the _splinter cluster_ and the updated old cluster be children of the old cluster in the above steps}@}. The dendrogram splits are ordered by {@{the order of splitting}@}. One can {@{split the dendrogram at any height to get the desirable number of clusters}@}. <!--SR:!2026-04-17,479,275!2026-05-07,482,275!2026-04-08,523,295!2025-08-10,352,314-->

### monothetic clustering

The above algorithm is {@{polythetic clustering because it considers all variables of each observation}@}. Consider an observation with _n_ numerical variables, define the _n-dimensional location_ of an observation {@{as the values of the _n_ numerical variables. Then note that the distance function applied to two observations considers all variables at once}@}. An another type of divisive clustering is {@{monothetic clustering, where only one variable is considered when splitting}@}. <!--SR:!2025-07-01,303,295!2026-06-28,568,315!2025-04-12,233,270-->

Monothetic clustering is usually used {@{when the data consists of binary or boolean variables, though some variants also support non-binary variables}@}. <!--SR:!2026-06-27,565,310-->

### chi-squared monothetic clustering

We define the _chi-squared measure_ between two binary variables $A$ and $B$, denoted $\chi_{AB}^2$, as the following:

> __chi-squared measure__
>
> Given {@{a [confusion matrix](confusion%20matrix) of two binary variables $A$ and $B$}@}:
>
> | $B$ \ $A$ | __1__ | __0__ |
> |:---------:|:-----:|:-----:|
> | __1__     | $a$   | $b$   |
> | __0__     | $c$   | $d$   |
>
> The _chi-squared measure_ of $A$ and $B$ (symbol: $\chi_{AB}^2$ or $\chi_{BA}^2$) is defined as {@{$$\chi_{AB}^2 = \chi_{BA}^2 = \frac {(a + b + c + d)(ad - bc)^2} {(a + b)(b + d)(d + c)(c + a)}$$}@}. The equation in words, which may be easier to remember, is {@{$$\chi_{AB}^2 = \chi_{BA}^2 = \frac {(\text{total})((\text{true positive})(\text{true negative}) - (\text{false positive})(\text{false negative}))^2} {(A\text{ is true})(A\text{ is false})(B\text{ is true})(B\text{ is false})}$$}@}. <!--SR:!2025-09-26,353,295!2025-04-30,162,275!2025-07-10,262,235-->

The chi-squared measure describes {@{the degree of correlation between two variables}@}. <!--SR:!2026-04-11,513,315-->

Now, for each variable, denoted $A$ here, calculate {@{the sum of all chi-squared measure with other variables except itself: $$\text{chi-squared measure sum of }A = \sum_{B \in \text{all variables except }A} \chi_{AB}^2$$}@}. Find {@{the variable with the largest sum (arbitrarily choose one if there are multiple variables with the largest sum)}@}. Finally, {@{split the observations into two clusters by the value of that variable and ignore that variable thereafter if further clustering is performed}@}. Repeat {@{this process recursively until you are satisfied with the clustering result}@}. <!--SR:!2025-12-06,404,295!2027-07-06,905,335!2025-04-18,159,255!2025-09-24,338,275-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/hierarchical_clustering) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Kaufman, L.; Rousseeuw, P.J. (2009) [1990]. ["6. Divisive Analysis (Program DIANA)"](https://books.google.com/books?id=YeFQHiikNo0C&pg=PA253). _Finding Groups in Data: An Introduction to Cluster Analysis_. Wiley. pp. 253–279. [ISBN](ISBN%20(identifier).md) 978-0-470-31748-8. <a id="^ref-Kaufman-2009"></a> ^ref-Kaufman-2009
