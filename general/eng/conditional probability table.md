---
aliases:
  - CPT
  - CPTs
  - conditional probability table
  - conditional probability tables
tags:
  - flashcard/active/general/eng/conditional_probability_table
  - language/in/English
---

# conditional probability table

For example, suppose that two [binary variables](binary%20data.md#binary%20variable) _x_ and _y_ have the [joint probability distribution](joint%20probability%20distribution.md) given in this table:

|            | ___x_=0__ | ___x_=1__ | __P(_y_)__ |
| ---------- |:---------:|:---------:|:----------:|
| ___y_=0__  | 4/9       | 1/9       | 5/9        |
| ___y_=1__  | 2/9       | 2/9       | 4/9        |
| __P(_x_)__ | 6/9       | 3/9       | 1          |

This gives us the table of conditional of probabilities of _y_ given _x_, with {@{the row headers being the conditional probabilities and the column headers being the variable conditioned on (mnemonic: ↙)}@}: <!--SR:!2027-09-19,718,250-->

|                      | ___x_=0__ | ___x_=1__ |
| -------------------- |:---------:|:---------:|
| __P(_y_=0&mid;_x_)__ | 4/9       | 1/9       |
| __P(_y_=1&mid;_x_)__ | 2/9       | 2/9       |
| __sum__              | 6/9       | 3/9       |

Swapping {@{the row and column headers is also possible (mnemonic: ↗)}@}: <!--SR:!2026-07-28,530,310-->

|           | __P(_y_=0&mid;_x_)__ | __P(_y_=1&mid;_x_)__ | __sum__ |
| --------- |:--------------------:|:--------------------:|:-------:|
| ___x_=0__ | 4/9                  | 2/9                  | 6/9     |
| ___x_=1__ | 1/9                  | 2/9                  | 3/9     |

With more than {@{one conditioning variable or output variable}@}, {@{the table headers simply become all possible combinations of the multiple variables}@}. <!--SR:!2025-11-30,395,310!2027-10-07,909,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conditional_probability_table) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
