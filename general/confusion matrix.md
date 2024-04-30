---
aliases:
  - confusion matrices
  - confusion matrix
  - error matrices
  - error matrix
  - error report
  - error reports
  - matching matrices
  - matching matrix
tags:
  - flashcard/general/confusion_matrix
  - language/in/English
---

# confusion matrix

In [machine learning](machine%20learning.md) and specifically [statistical classification](statistical%20classification.md), a __confusion matrix__ or {{__error matrix__}}, is {{a table that visualizes the performance of a classification algorithm}}. <!--SR:!2024-06-19,51,310!2024-05-28,33,290-->

Each row represents {{an actual class while each column represents a predicted class. The reverse is less common but also possible, and both are found in the literature}}. <!--SR:!2024-06-12,43,290-->

> [!example] examples
>
> {{A quick example}} below.
>
> | actual class \ predicted class | __yes__ | __no__ |
> |:------------------------------:|:-------:|:------:|
> | __yes__                        | 3       | 1      |
> | __no__                         | 2       | 2      | <!--SR:!2024-05-03,17,290-->

## error report

An __error report__ {{is a related table that can be constructed from a confusion matrix}}. The column headers are, in order, {{(actual) class, number of cases (# cases), number of errors (# errors), and percentage error (% error)}}. The row headers are {{all possible classes, with an additional "total" at the end that considers all classes at once}}. <!--SR:!2024-05-20,27,270!2024-05-16,22,250!2024-05-14,21,250-->

> [!example] examples
>
> {{A quick example}} below, using the same statistics as above.
>
> | class     | __# cases__ | __# errors__ | __% error__ |
> |:---------:|:-----------:|:------------:|:-----------:|
> | __yes__   | 4           | 1            | 25.00       |
> | __no__    | 4           | 2            | 50.00       |
> | __total__ | 8           | 3            | 37.50       | <!--SR:!2024-06-03,37,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/confusion_matrix) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
