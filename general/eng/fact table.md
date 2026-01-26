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
> | :--------: | :------------: | :------------: | :---------: |
> |     p1     |       s1       |       c1       |      4      |
> |     p3     |       s1       |       c2       |      3      |
> |     p2     |       s3       |       c1       |      7      |
>
> The table above can also be represented as {@{a [OLAP cube](OLAP%20cube.md) (also called [data cube](data%20cube.md))}@}.
>
> The fact table can be {@{aggregated}@}, such as {@{averaging, maximum, minimum, and summing}@}:
>
> | {@{part}@} | {@{customer}@} | {@{sum of price over suppliers}@} |
> | :--------: | :------------: | :-------------------------------: |
> |     p1     |       c1       |                 4                 |
> |     p3     |       c2       |                 3                 |
> |     p2     |       c1       |                 7                 |
>
> | {@{customer}@} | {@{sum of price over parts and suppliers}@} |
> | :------------: | :-----------------------------------------: |
> |       c1       |                     11                      |
> |       c2       |                      3                      |

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fact_table) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
