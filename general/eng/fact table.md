---
aliases:
  - fact table
  - fact tables
tags:
  - flashcard/active/general/eng/fact_table
  - language/in/English
---

# fact table

## examples

> [!example] transactional fact table examples
>
> A {@{transactional fact table}@} example. The rows are {@{the transactions}@}, while the columns are {@{the transaction properties}@}.
>
> | {@{part}@} | {@{supplier}@} | {@{customer}@} | {@{price}@} |
> |:--------:|:------------:|:------------:|:---------:|
> | p1       | s1           | c1           | 4         |
> | p3       | s1           | c2           | 3         |
> | p2       | s3           | c1           | 7         |
>
> The table above can also be represented as {@{a [OLAP cube](OLAP%20cube.md) (also called [data cube](data%20cube.md))}@}.
>
> The fact table can be {@{aggregated}@}, such as {@{averaging, maximum, minimum, and summing}@}:
>
> | {@{part}@} | {@{customer}@} | {@{sum of price over suppliers}@} |
> |:--------:|:------------:|:-------------------------------:|
> | p1       | c1           | 4                               |
> | p3       | c2           | 3                               |
> | p2       | c1           | 7                               |
>
> | {@{customer}@} | {@{sum of price over parts and suppliers}@} |
> |:------------:|:-----------------------------------------:|
> | c1           | 11                                        |
> | c2           | 3                                         | <!--SR:!2026-11-08,665,330!2025-08-09,313,310!2025-02-14,182,310!2025-07-23,310,330!2025-02-03,175,310!2025-05-18,257,330!2025-01-27,170,310!2025-05-13,254,330!2025-07-06,298,330!2025-01-13,156,310!2025-04-23,239,330!2026-08-03,593,330!2026-08-12,596,330!2025-06-17,280,330!2025-11-20,390,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fact_table) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
