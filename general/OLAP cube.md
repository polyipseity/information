---
aliases:
  - OLAP cube
  - OLAP cubes
tags:
  - flashcard/general/OLAP_cube
  - language/in/English
---

# OLAP cube

An __OLAP cube__ is {{a [multi-dimensional array](array%20(data%20type).md#multi-dimensional%20arrays)}}. OLAP refers to {{[online analytical processing](online%20analytical%20processing.md), a computer-based technique of analyzing data to look for insights}}. The term _cube_ refers to {{a multi-dimensional dataset, laid out in a multi-dimensional spreadsheet}}. It is also sometimes called {{a [hypercube](hypercube.md) if the number of dimensions is greater than 3}}. <!--SR:!2024-08-19,45,290!2024-12-05,115,290!2024-12-11,121,290!2025-01-13,156,310-->

## operations

_Drill down/up_ allows the user to {{navigate among levels of data}} ranging from {{the most summarized (up) to the most detailed (down)}}. The more summarized the data level, {{the more dimensions are collapsed and thus hidden}}, and vice versa. <!--SR:!2024-09-02,61,310!2024-09-10,68,310!2024-12-18,126,290-->

_Rollup_ involves {{summarizing the data along a dimension}}. The summarization rule may be {{an [aggregate function](aggregate%20function.md)}}, such as {{computing the average, max, min, sum, or a custom formula}}. <!--SR:!2024-09-08,65,310!2024-11-18,104,290!2024-08-16,45,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/OLAP_cube) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
