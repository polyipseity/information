---
aliases:
  - OLAP
  - online analytical processing
tags:
  - flashcard/general/online_analytical_processing
  - language/in/English
---

# online analytical processing

## overview of OLAP systems

### aggregations

OLAP uses {{aggregation to improve performance}}. It {{is generated from the [fact table](fact%20tablee.md) with different granularity by aggregating data along the collapsed dimensions using an [aggregate function](aggregate%20function.md)}}. The number of possible aggregations is {{determined by the number of possible combination of ways to collapse different dimensions}}. <!--SR:!2024-07-04,16,290!2024-06-26,9,250!2024-06-27,10,250-->

Because usually there are {{too many possible aggregations that can be calculated}}, often {{only a predetermined number or those that are within a certain size are calculated; the rest are solved on demand}}. The problem of {{selecting aggregations (or views) to calculate is known as the [view selection or materialization problem](materialized%20view.md#algorithms)}}. View selection can be constrained by {{the number of views, the total size of the views, time to update the views from the base data, an arbitrary combination of the above, etc.}} The objective is {{to minimize the average time to answer OLAP queries, or alternatively minimize update time}}. View selection is {{[NP-complete](NP-completeness.md)}}. A variety of [algorithms](materialized%20view.md#algorithms) have been explored, such as {{[greedy algorithms](greedy%20algorithm.md), randomized search, [genetic algorithms](genetic%20algorithm.md), and [A* search algorithm](A*%20search%20algorithm.md)}}. <!--SR:!2024-07-01,13,290!2024-06-26,9,250!2024-06-30,13,270!2024-07-12,19,270!2024-07-03,15,290!2024-07-05,17,290!2024-06-25,8,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/online_analytical_processing) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
