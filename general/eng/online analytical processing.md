---
aliases:
  - OLAP
  - online analytical processing
tags:
  - flashcard/active/general/eng/online_analytical_processing
  - language/in/English
---

# online analytical processing

## overview of OLAP systems

### aggregations

OLAP uses {@{aggregation to improve performance}@}. It is generated from {@{the [fact table](fact%20tablee.md) with different granularity by aggregating data along the collapsed dimensions using an [aggregate function](aggregate%20function.md)}@}. The number of possible aggregations is {@{determined by the number of possible combination of ways to collapse different dimensions}@}. <!--SR:!2028-09-19,1208,350!2026-06-21,503,270!2026-05-12,520,310-->

Because usually there are {@{too many possible aggregations that can be calculated}@}, often {@{only a predetermined number or those that are within a certain size are calculated; the rest are solved on demand}@}. The problem of {@{selecting aggregations (or views) to calculate is known as the [view selection or materialization problem](materialized%20view.md#algorithms)}@}. View selection can be constrained by {@{the number of views, the total size of the views, time to update the views from the base data, an arbitrary combination of the above, etc.}@} The objective is {@{to minimize the average time to answer OLAP queries, or alternatively minimize update time}@}. View selection is {@{[NP-complete](NP-completeness.md)}@}. A variety of [algorithms](materialized%20view.md#algorithms) have been explored, such as {@{[greedy algorithms](greedy%20algorithm.md), randomized search, [genetic algorithms](genetic%20algorithm.md), and [A* search algorithm](A*%20search%20algorithm.md)}@}. <!--SR:!2026-03-21,446,310!2026-05-24,530,310!2026-11-08,615,310!2025-06-30,281,310!2028-08-03,1174,350!2027-12-17,962,330!2028-06-20,1087,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/online_analytical_processing) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
