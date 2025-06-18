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
  - flashcard/active/general/eng/confusion_matrix
  - language/in/English
---

# confusion matrix

In [machine learning](machine%20learning.md) and specifically [statistical classification](statistical%20classification.md), a __confusion matrix__ or {@{__error matrix__}@}, is {@{a table that visualizes the performance of a classification algorithm}@}. <!--SR:!2027-10-12,992,350!2026-04-26,565,330-->

Each row represents {@{an actual class while each column represents a predicted class. The reverse is less common but also possible, and both are found in the literature}@}. <!--SR:!2025-10-13,363,290-->

> [!example] examples
>
> {@{A quick example}@} below.
>
> | actual class \ predicted class | __yes__ | __no__ |
> |:------------------------------:|:-------:|:------:|
> | __yes__                        | 3       | 1      |
> | __no__                         | 2       | 2      | <!--SR:!2028-11-13,1301,350-->

## error report

An __error report__ {@{is a related table that can be constructed from a confusion matrix}@}. The column headers are, in order, {@{(actual) class, number of cases (# cases), number of errors (# errors), and percentage error (% error)}@}. The row headers are {@{all possible classes, with an additional "total" at the end that considers all classes at once}@}. <!--SR:!2028-09-13,1184,310!2025-07-27,303,270!2025-11-18,367,270-->

> [!example] examples
>
> {@{A quick example}@} below, using the same statistics as above.
>
> | class     | __# cases__ | __# errors__ | __% error__ |
> |:---------:|:-----------:|:------------:|:-----------:|
> | __yes__   | 4           | 1            | 25.00       |
> | __no__    | 4           | 2            | 50.00       |
> | __total__ | 8           | 3            | 37.50       | <!--SR:!2026-08-25,665,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/confusion_matrix) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
