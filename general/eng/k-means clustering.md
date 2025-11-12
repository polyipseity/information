---
aliases:
  - k-means algorithm
  - k-means clustering
tags:
  - flashcard/active/general/eng/k-means_clustering
  - language/in/English
---

# _k_-means clustering

## algorithms

### standard algorithm (naive _k_-means)

Assuming that we have $k$ clusters, {@{make $k$ initial means}@}. Repeat the following two steps: <!--SR:!2026-10-17,699,333-->

1. __assignment step__ ::@:: Assign each observation to the nearest mean, using the (squared) [Euclidean distance](Euclidean%20distance.md). If there are two or more means of the same distance, arbitrarily choose one of them. <!--SR:!2026-11-12,719,333!2028-08-02,1224,353-->
2. __update step__ ::@:: Recalculate means (or [centroids](centroid.md)) using the assigned observations. <!--SR:!2026-06-03,575,310!2029-10-22,1537,330-->

The algorithm has converged {@{when the assignments no longer change}@}, but the resulting clusters are {@{not guaranteed to be the optimum}@}. <!--SR:!2026-07-08,571,313!2027-03-07,809,330-->

The algorithm may not converge if {@{using a distance function other than the (squared) [Euclidean distance](Euclidean%20distance.md)}@}. <!--SR:!2026-01-11,475,313-->

#### initialization methods

The clustering result {@{depends on the initial means}@}, so it is important to {@{find "good" initial means to get more optimal clustering}@}. An extreme example is {@{an initial mean that is so far away from all observations that no observation ever gets assigned to it}@}. <!--SR:!2026-04-07,198,293!2030-09-28,1794,330!2026-01-02,84,370-->

A naive way to initialize the means is {@{randomly choose $k$ observations}@}. A less naive way is {@{repeat the standard algorithm several times with different random initial means and take their average}@}. <!--SR:!2028-06-17,1189,353!2026-01-13,414,270-->

#### variations

- generalized sequential _k_-means ::@:: Make $k$ initial means. Instead of running the assignment step on all observations and the update step on all means each time, run the assignment step on one observation and the update step on one mean each time. Specifically, for each observation $x$ and its closest mean $m_*$, the new mean is $m_* + \alpha (x - m_*) = (1 - \alpha) m_* + \alpha x$, where the weight $\alpha$ is an arbitrary variable. <!--SR:!2027-10-14,867,270!2028-12-24,1257,310-->
  - generalized sequential _k_-means advantages ::@:: The advantage is that it can update the clustering incrementally as new observations are made instead of requiring all observations at once. Incremental updates can also save computation compared to recalculation. <!--SR:!2030-09-04,1776,330!2026-05-27,489,270-->
  - sequential _k_-means ::@:: The weight $\alpha = \frac 1 {n + 1}$, where $n$ is the number of observations that has modified the closest mean $m_*$, not including the current one. <!--SR:!2028-01-23,935,270!2026-02-26,443,270-->
    - sequential _k_-means interpretation ::@:: The resulting mean is the same as the mean of all incoming observations calculated at once, i.e. $m_n = \frac 1 n \sum_{k = 1}^n x_k$. This is simply the [cumulative average](moving%20average.md#cumulative%20average) of the incoming observations. <!--SR:!2029-01-05,1264,310!2025-12-31,459,313-->
  - forgetful sequential _k_-means ::@:: The weight $\alpha \in [0, 1]$ is a constant. It is useful for clusters that drift over time. <!--SR:!2026-02-02,491,313!2027-02-18,784,333-->
    - forgetful sequential _k_-means interpretation ::@:: When $\alpha = 0$, the mean never moves. When $\alpha = 1$, the mean is always the new observation. Otherwise, observations have exponentially less weighting on the mean over time, though never zero. This way, they are "forgotten", but never quite completely. The closed form is $m_n = (1 - a)^n m_0 + a \sum_{k = 1}^n (1 - a)^{n - k} x_k$. This is simply the [exponential moving average](moving%20average.md#exponential%20moving%20average). <!--SR:!2029-05-12,1267,273!2026-08-28,523,253-->

## discussion

While _k_-means is {@{simple to implement and efficient}@}, there are {@{several drawbacks to it}@}. {@{The number of clusters _k_}@} is {@{a [hyperparameter](hyperparameter%20(machine%20learning).md) that is crucial for optimal results}@}. Yet, {@{[determining the number of clusters in a data set](determining%20the%20number%20of%20clusters%20in%20a%20data%20set)}@} is {@{difficult and often ambiguous}@}. {@{\(Squared\) [Euclidean distance](Euclidean%20distance.md)}@} is {@{\(almost\) always used as a [metric](metric%20(mathematics).md)}@} and {@{[variance](variance.md)}@} is used as {@{a measure of cluster scatter}@}, which is {@{limited for many clustering models}@}. Lastly, convergence may {@{produce counterintuitive results}@}, like {@{a mean in between two somewhat close but still separate clusters}@}, or {@{a cluster being split into two by two means}@}. <!--SR:!2026-08-27,666,330!2029-04-17,1359,313!2027-03-05,786,310!2027-08-31,866,290!2026-12-18,401,374!2026-12-12,395,374!2026-12-11,394,374!2026-12-07,390,374!2026-12-17,400,374!2026-12-06,389,374!2026-12-13,396,374!2026-12-10,393,374!2025-12-02,87,363!2025-12-02,87,363-->

Its cluster model is also very limited. It assumes the clusters are {@{spherical and separable so that the mean converges to the cluster center. The clusters are also of similar size so that the observations are assigned the correct mean}@}. <!--SR:!2027-11-22,893,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/k-means_clustering) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
