---
aliases:
  - Excel formula
  - Excel formulae
  - Excel formulas
tags:
  - flashcard/special/academia/HKUST/COMP_1029V/formula
  - language/in/English
---

# Excel formula

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../tools/utility.py.md
```

%%

A formula always {{starts with an equals sign `=`}}. <!--SR:!2024-05-02,70,310-->

## cell reference

To get the value of a cell in a formula, {{use its location, like `=A1`. This is known as a _cell reference_}}. <!--SR:!2024-04-11,52,310-->

When copy and pasting formulas, the cell references in the formula {{are offsetted by the same offset from the original cell to the copied cell}}. To prevent this offset, {{add `$` before the column, the row, or both, like `=$A$1`}}. <!--SR:!2024-04-29,67,310!2024-04-28,67,310-->

## operators

### arithmetic operators

Below are common arithmetic and string operators. Operators have higher precedence than or same precedence as operators below it in the list:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`^`", "power",),
  ("`*`", "multiplication",),
  ("`/`", "division",),
  ("`+`", "addition",),
  ("`-`", "subtraction",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("93ab", "f21a",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "9cda", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93ab"--><!-- The following content is generated at 2024-01-31T12:32:22.690955+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `^` | power |
> | `*` | multiplication |
> | `/` | division |
> | `+` | addition |
> | `-` | subtraction |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f21a"--><!-- The following content is generated at 2024-01-31T12:32:22.637380+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`^` <!--SR:!2024-03-21,36,290!2024-05-05,73,310-->
- `^`→:::←`*` <!--SR:!2024-04-20,60,310!2024-04-14,55,310-->
- `*`→:::←`/` <!--SR:!2024-04-15,56,310!2024-04-08,50,310-->
- `/`→:::←`+` <!--SR:!2024-04-24,63,310!2024-04-24,64,310-->
- `+`→:::←`-` <!--SR:!2024-04-17,58,310!2024-04-14,55,310-->
- `-`→:::←_(end)_ <!--SR:!2024-04-27,66,310!2024-04-23,63,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9cda"--><!-- The following content is generated at 2024-01-31T12:32:22.752951+08:00. Any edits will be overridden! -->

- `^`::power <!--SR:!2024-04-22,62,310-->
- `*`::multiplication <!--SR:!2024-04-19,59,310-->
- `/`::division <!--SR:!2024-04-17,58,310-->
- `+`::addition <!--SR:!2024-04-18,59,310-->
- `-`::subtraction <!--SR:!2024-04-10,52,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### comparison operators

Below are common comparison operators, all of which returns {{booleans}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-04-20,60,310-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`=`", "equal to",),
  ("`<`", "lesser than",),
  ("`>`", "greater than",),
  ("`<=`", "lesser than or equal to",),
  ("`>=`", "greater than or equal to",),
  ("`<>`", "not equal to",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("bd23", "d123",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "cc23", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bd23"--><!-- The following content is generated at 2024-01-31T12:32:22.894695+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `=` | equal to |
> | `<` | lesser than |
> | `>` | greater than |
> | `<=` | lesser than or equal to |
> | `>=` | greater than or equal to |
> | `<>` | not equal to |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d123"--><!-- The following content is generated at 2024-01-31T12:32:22.775056+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`=` <!--SR:!2024-03-15,18,270!2024-03-24,23,270-->
- `=`→:::←`<` <!--SR:!2024-04-13,51,290!2024-03-10,18,270-->
- `<`→:::←`>` <!--SR:!2024-04-19,60,310!2024-04-28,67,310-->
- `>`→:::←`<=` <!--SR:!2024-04-29,68,310!2024-04-03,40,270-->
- `<=`→:::←`>=` <!--SR:!2024-04-18,59,310!2024-03-11,25,270-->
- `>=`→:::←`<>` <!--SR:!2024-04-23,62,310!2024-04-21,60,310-->
- `<>`→:::←_(end)_ <!--SR:!2024-04-10,52,310!2024-04-12,53,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cc23"--><!-- The following content is generated at 2024-01-31T12:32:22.829082+08:00. Any edits will be overridden! -->

- `=`::equal to <!--SR:!2024-04-28,66,310-->
- `<`::lesser than <!--SR:!2024-04-09,51,310-->
- `>`::greater than <!--SR:!2024-05-02,70,310-->
- `<=`::lesser than or equal to <!--SR:!2024-04-20,60,310-->
- `>=`::greater than or equal to <!--SR:!2024-04-16,56,310-->
- `<>`::not equal to <!--SR:!2024-04-25,64,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

Also, one cannot chain {{comparison operators, like `2 <= A1 <= 5`. [Logic functions](#logic%20functions) are needed instead, like `AND(2 <= A1, A1 <= 5)`}}. <!--SR:!2024-05-03,71,310-->

## functions

### logic functions

Below are common logic functions, all of which {{accept booleans and return booleans}}: <!--SR:!2024-04-26,65,310-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "function", "description"
table = (
  ("`NOT(boolean)`", "negate",),
  ("`AND(booleans...)`", "every input is true",),
  ("`OR(booleans...)`", "there exists true inputs",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("2856", "d882",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "ee13", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2856"--><!-- The following content is generated at 2024-02-05T12:43:06.967772+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | `NOT(boolean)` | negate |
> | `AND(booleans...)` | every input is true |
> | `OR(booleans...)` | there exists true inputs |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d882"--><!-- The following content is generated at 2024-02-05T12:43:06.987947+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`NOT(boolean)` <!--SR:!2024-04-22,61,310!2024-05-01,69,310-->
- `NOT(boolean)`→:::←`AND(booleans...)` <!--SR:!2024-04-07,49,310!2024-04-30,68,310-->
- `AND(booleans...)`→:::←`OR(booleans...)` <!--SR:!2024-04-16,56,310!2024-04-13,54,310-->
- `OR(booleans...)`→:::←_(end)_ <!--SR:!2024-04-18,58,310!2024-04-26,65,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee13"--><!-- The following content is generated at 2024-02-05T12:43:07.023980+08:00. Any edits will be overridden! -->

- `NOT(boolean)`::negate <!--SR:!2024-04-21,61,310-->
- `AND(booleans...)`::every input is true <!--SR:!2024-04-16,57,310-->
- `OR(booleans...)`::there exists true inputs <!--SR:!2024-04-27,65,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### string functions and operators

Below are common string functions and operators:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "function", "description"
table = (
  ("(operator) `&`", "concatenation",),
  ("`LEFT(string, length)`", "get the first `length` characters in `string`",),
  ("`LEN(string)`", "length of `string`",),
  ("`LOWER(string)`", "convert to lowercase",),
  ("`RIGHT(string, length)`", "get the last `length` characters in `string`",),
  ("`SUBSTITUTE(string, old, new)`", "replace all occurrences of `old` with `new` in `string`",),
  ("`UPPER(string)`", "convert to uppercase",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("0ff2", "305b",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "29ca", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0ff2"--><!-- The following content is generated at 2024-01-31T12:40:30.974267+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | (operator) `&` | concatenation |
> | `LEFT(string, length)` | get the first `length` characters in `string` |
> | `LEN(string)` | length of `string` |
> | `LOWER(string)` | convert to lowercase |
> | `RIGHT(string, length)` | get the last `length` characters in `string` |
> | `SUBSTITUTE(string, old, new)` | replace all occurrences of `old` with `new` in `string` |
> | `UPPER(string)` | convert to uppercase |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="305b"--><!-- The following content is generated at 2024-01-31T12:40:31.061300+08:00. Any edits will be overridden! -->

- _(begin)_→:::←(operator) `&` <!--SR:!2024-03-11,26,290!2024-05-04,72,310-->
- (operator) `&`→:::←`LEFT(string, length)` <!--SR:!2024-04-07,47,290!2024-03-16,28,270-->
- `LEFT(string, length)`→:::←`LEN(string)` <!--SR:!2024-03-10,28,270!2024-04-07,37,230-->
- `LEN(string)`→:::←`LOWER(string)` <!--SR:!2024-03-13,9,250!2024-03-23,34,290-->
- `LOWER(string)`→:::←`RIGHT(string, length)` <!--SR:!2024-03-10,4,130!2024-04-26,53,250-->
- `RIGHT(string, length)`→:::←`SUBSTITUTE(string, old, new)` <!--SR:!2024-03-19,32,270!2024-03-07,6,230-->
- `SUBSTITUTE(string, old, new)`→:::←`UPPER(string)` <!--SR:!2024-04-06,37,230!2024-03-07,2,150-->
- `UPPER(string)`→:::←_(end)_ <!--SR:!2024-04-14,56,310!2024-03-07,22,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29ca"--><!-- The following content is generated at 2024-01-31T12:40:31.103335+08:00. Any edits will be overridden! -->

- (operator) `&`::concatenation <!--SR:!2024-04-13,55,310-->
- `LEFT(string, length)`::get the first `length` characters in `string` <!--SR:!2024-04-23,62,310-->
- `LEN(string)`::length of `string` <!--SR:!2024-04-19,60,310-->
- `LOWER(string)`::convert to lowercase <!--SR:!2024-04-06,48,310-->
- `RIGHT(string, length)`::get the last `length` characters in `string` <!--SR:!2024-04-21,60,310-->
- `SUBSTITUTE(string, old, new)`::replace all occurrences of `old` with `new` in `string` <!--SR:!2024-04-27,66,310-->
- `UPPER(string)`::convert to uppercase <!--SR:!2024-04-12,54,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### common functions

Below are common functions:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "function", "description"
table = (
  ("`AVERAGE(numbers...)`", "average",),
  ("`COUNTIF(values, criteria)`", "number of `values` satisfying `criteria`",),
  ("`IF(boolean, value_if_true[, value_if_false = FALSE])`", "`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested",),
  ("`MAX(numbers...)`", "maximum",),
  ("`MIN(numbers...)`", "minimum",),
  ("`RANK(number, numbers...)`", "rank of `number` in `numbers`, starting from 1",),
  ("`STDEV(numbers...)`", "standard deviation",),
  ("`SUM(numbers...)`", "summation",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("93ba", "ee42",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "f123", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93ba"--><!-- The following content is generated at 2024-01-31T12:52:39.241194+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | `AVERAGE(numbers...)` | average |
> | `COUNTIF(values, criteria)` | number of `values` satisfying `criteria` |
> | `IF(boolean, value_if_true[, value_if_false = FALSE])` | `value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested |
> | `MAX(numbers...)` | maximum |
> | `MIN(numbers...)` | minimum |
> | `RANK(number, numbers...)` | rank of `number` in `numbers`, starting from 1 |
> | `STDEV(numbers...)` | standard deviation |
> | `SUM(numbers...)` | summation |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee42"--><!-- The following content is generated at 2024-01-31T12:52:39.155842+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`AVERAGE(numbers...)` <!--SR:!2024-04-20,48,270!2024-04-12,54,310-->
- `AVERAGE(numbers...)`→:::←`COUNTIF(values, criteria)` <!--SR:!2024-03-17,31,290!2024-04-11,53,310-->
- `COUNTIF(values, criteria)`→:::←`IF(boolean, value_if_true[, value_if_false = FALSE])` <!--SR:!2024-04-27,65,310!2024-03-26,39,290-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`→:::←`MAX(numbers...)` <!--SR:!2024-04-04,34,230!2024-03-10,22,250-->
- `MAX(numbers...)`→:::←`MIN(numbers...)` <!--SR:!2024-04-17,58,310!2024-04-11,53,310-->
- `MIN(numbers...)`→:::←`RANK(number, numbers...)` <!--SR:!2024-03-08,3,170!2024-03-18,30,250-->
- `RANK(number, numbers...)`→:::←`STDEV(numbers...)` <!--SR:!2024-03-31,34,230!2024-04-18,49,270-->
- `STDEV(numbers...)`→:::←`SUM(numbers...)` <!--SR:!2024-05-03,71,310!2024-04-22,50,270-->
- `SUM(numbers...)`→:::←_(end)_ <!--SR:!2024-03-21,23,270!2024-03-16,24,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f123"--><!-- The following content is generated at 2024-01-31T12:52:39.120607+08:00. Any edits will be overridden! -->

- `AVERAGE(numbers...)`::average <!--SR:!2024-04-13,55,310-->
- `COUNTIF(values, criteria)`::number of `values` satisfying `criteria` <!--SR:!2024-04-25,64,310-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`::`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested <!--SR:!2024-04-21,61,310-->
- `MAX(numbers...)`::maximum <!--SR:!2024-04-17,57,310-->
- `MIN(numbers...)`::minimum <!--SR:!2024-04-17,57,310-->
- `RANK(number, numbers...)`::rank of `number` in `numbers`, starting from 1 <!--SR:!2024-04-22,61,310-->
- `STDEV(numbers...)`::standard deviation <!--SR:!2024-05-01,69,310-->
- `SUM(numbers...)`::summation <!--SR:!2024-04-21,61,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
