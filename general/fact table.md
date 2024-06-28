---
aliases:
  - fact table
  - fact tables
tags:
  - flashcard/general/fact_table
  - language/in/English
---

# fact table

## examples

> [!example] transactional fact table examples
>
> A {{transactional fact table}} example. The rows are {{the transactions}}, while the columns are {{the transaction properties}}.
>
> | {{part}} | {{supplier}} | {{customer}} | {{price}} |
> |:--------:|:------------:|:------------:|:---------:|
> | p1       | s1           | c1           | 4         |
> | p3       | s1           | c2           | 3         |
> | p2       | s3           | c1           | 7         |
>
> The table above can also be represented as {{a [OLAP cube](OLAP%20cube.md) (also called [data cube](data%20cube.md))}}.
>
> The fact table can be {{aggregated}}, such as {{averaging, maximum, minimum, and summing}}:
>
> | {{part}} | {{customer}} | {{sum of price over suppliers}} |
> |:--------:|:------------:|:-------------------------------:|
> | p1       | c1           | 4                               |
> | p3       | c2           | 3                               |
> | p2       | c1           | 7                               |
>
> | {{customer}} | {{sum of price over parts and suppliers}} |
> |:------------:|:-----------------------------------------:|
> | c1           | 11                                        |
> | c2           | 3                                         | <!--SR:!2024-07-01,13,290!2024-07-13,20,270!2024-07-02,14,290!2024-07-05,17,290!2024-08-11,44,290!2024-07-04,16,290!2024-08-09,42,290!2024-07-03,15,290!2024-07-05,17,290!2024-07-02,14,290!2024-07-02,14,290!2024-07-31,34,290!2024-07-01,13,290!2024-07-05,17,290!2024-07-21,26,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fact_table) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
