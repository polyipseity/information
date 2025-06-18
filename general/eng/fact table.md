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
> | c2           | 3                                         | <!--SR:!2026-11-08,665,330!2025-08-09,313,310!2027-04-09,784,330!2025-07-23,310,330!2027-03-02,757,330!2028-07-30,1169,350!2027-01-25,728,330!2028-07-11,1152,350!2025-07-06,298,330!2026-11-13,669,330!2028-04-10,1083,350!2026-08-03,593,330!2026-08-12,596,330!2028-12-15,1277,350!2025-11-20,390,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fact_table) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
