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
# pytextgen generate module
# import ../../../../../tools/utility.py.md
```

%%

A formula always {{starts with an equals sign `=`}}. <!--SR:!2024-05-02,70,310-->

## cell reference

To get the value of a cell in a formula, {{use its location, like `=A1`. This is known as a _cell reference_}}. <!--SR:!2024-11-10,213,330-->

When copy and pasting formulas, the cell references in the formula {{are offsetted by the same offset from the original cell to the copied cell}}. To prevent this offset, {{add `$` before the column, the row, or both, like `=$A$1`}}. <!--SR:!2024-04-29,67,310!2024-04-28,67,310-->

## operators

### arithmetic operators

Below are common arithmetic and string operators. Operators have higher precedence than or same precedence as operators below it in the list:

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-01-31T12:32:22.690955+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `^` | power |
> | `*` | multiplication |
> | `/` | division |
> | `+` | addition |
> | `-` | subtraction |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2024-01-31T12:32:22.637380+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`^` <!--SR:!2024-08-14,146,310!2024-05-05,73,310-->
- `^`→:::←`*` <!--SR:!2024-12-26,250,330!2024-09-25,163,310-->
- `*`→:::←`/` <!--SR:!2024-10-11,179,310!2024-11-06,212,330-->
- `/`→:::←`+` <!--SR:!2024-04-24,63,310!2024-04-24,64,310-->
- `+`→:::←`-` <!--SR:!2024-12-24,251,330!2024-12-14,243,330-->
- `-`→:::←_(end)_ <!--SR:!2024-04-27,66,310!2025-01-20,272,330-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-31T12:32:22.752951+08:00. Any edits will be overridden! -->

- `^`::power <!--SR:!2025-01-15,268,330-->
- `*`::multiplication <!--SR:!2025-01-06,262,330-->
- `/`::division <!--SR:!2025-01-01,259,330-->
- `+`::addition <!--SR:!2025-01-03,260,330-->
- `-`::subtraction <!--SR:!2024-11-12,216,330-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {{booleans}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-12-25,249,330-->

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2024-01-31T12:32:22.894695+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `=` | equal to |
> | `<` | lesser than |
> | `>` | greater than |
> | `<=` | lesser than or equal to |
> | `>=` | greater than or equal to |
> | `<>` | not equal to |

<!--/pytextgen-->

<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-01-31T12:32:22.775056+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`=` <!--SR:!2024-05-03,49,270!2024-05-27,42,270-->
- `=`→:::←`<` <!--SR:!2024-09-09,147,290!2024-05-18,68,290-->
- `<`→:::←`>` <!--SR:!2025-01-12,268,330!2024-04-28,67,310-->
- `>`→:::←`<=` <!--SR:!2024-04-29,68,310!2024-04-27,23,250-->
- `<=`→:::←`>=` <!--SR:!2024-10-09,174,310!2024-05-15,65,270-->
- `>=`→:::←`<>` <!--SR:!2024-05-27,34,290!2024-05-21,29,290-->
- `<>`→:::←_(end)_ <!--SR:!2024-11-11,215,330!2024-09-20,161,310-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-31T12:32:22.829082+08:00. Any edits will be overridden! -->

- `=`::equal to <!--SR:!2024-04-28,66,310-->
- `<`::lesser than <!--SR:!2024-11-13,218,330-->
- `>`::greater than <!--SR:!2024-05-02,70,310-->
- `<=`::lesser than or equal to <!--SR:!2024-12-24,248,330-->
- `>=`::greater than or equal to <!--SR:!2024-12-09,237,330-->
- `<>`::not equal to <!--SR:!2024-04-25,64,310-->

<!--/pytextgen-->

Also, one cannot chain {{comparison operators, like `2 <= A1 <= 5`. [Logic functions](#logic%20functions) are needed instead, like `AND(2 <= A1, A1 <= 5)`}}. <!--SR:!2024-05-03,71,310-->

## functions

### logic functions

Below are common logic functions, all of which {{accept booleans and return booleans}}: <!--SR:!2024-04-26,65,310-->

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2024-02-05T12:43:06.967772+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | `NOT(boolean)` | negate |
> | `AND(booleans...)` | every input is true |
> | `OR(booleans...)` | there exists true inputs |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-02-05T12:43:06.987947+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`NOT(boolean)` <!--SR:!2025-01-07,260,330!2024-05-01,69,310-->
- `NOT(boolean)`→:::←`AND(booleans...)` <!--SR:!2024-09-05,150,310!2024-04-30,68,310-->
- `AND(booleans...)`→:::←`OR(booleans...)` <!--SR:!2024-12-10,238,330!2024-09-30,168,310-->
- `OR(booleans...)`→:::←_(end)_ <!--SR:!2024-12-16,242,330!2024-04-26,65,310-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-05T12:43:07.023980+08:00. Any edits will be overridden! -->

- `NOT(boolean)`::negate <!--SR:!2025-01-16,269,330-->
- `AND(booleans...)`::every input is true <!--SR:!2024-12-16,244,330-->
- `OR(booleans...)`::there exists true inputs <!--SR:!2024-04-27,65,310-->

<!--/pytextgen-->

### string functions and operators

Below are common string functions and operators:

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="0ff2"--><!-- The following content is generated at 2024-01-31T12:40:30.974267+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | (operator) `&` | concatenation |
> | `LEFT(string, length)` | get the first `length` characters in `string` |
> | `LEN(string)` | length of `string` |
> | `LOWER(string)` | convert to lowercase |
> | `RIGHT(string, length)` | get the last `length` characters in `string` |
> | `SUBSTITUTE(string, old, new)` | replace all occurrences of `old` with `new` in `string` |
> | `UPPER(string)` | convert to uppercase |

<!--/pytextgen-->

<!--pytextgen generate section="305b"--><!-- The following content is generated at 2024-01-31T12:40:31.061300+08:00. Any edits will be overridden! -->

- _(begin)_→:::←(operator) `&` <!--SR:!2024-06-23,104,310!2024-05-04,72,310-->
- (operator) `&`→:::←`LEFT(string, length)` <!--SR:!2024-05-02,24,270!2024-06-01,75,270-->
- `LEFT(string, length)`→:::←`LEN(string)` <!--SR:!2024-06-26,107,290!2024-07-01,84,230-->
- `LEN(string)`→:::←`LOWER(string)` <!--SR:!2024-05-09,35,250!2024-04-29,7,250-->
- `LOWER(string)`→:::←`RIGHT(string, length)` <!--SR:!2024-04-24,20,150!2024-04-26,53,250-->
- `RIGHT(string, length)`→:::←`SUBSTITUTE(string, old, new)` <!--SR:!2024-06-12,85,270!2024-06-25,69,250-->
- `SUBSTITUTE(string, old, new)`→:::←`UPPER(string)` <!--SR:!2024-04-25,17,210!2024-04-27,7,130-->
- `UPPER(string)`→:::←_(end)_ <!--SR:!2024-10-09,177,310!2024-05-29,83,290-->

<!--/pytextgen-->

<!--pytextgen generate section="29ca"--><!-- The following content is generated at 2024-01-31T12:40:31.103335+08:00. Any edits will be overridden! -->

- (operator) `&`::concatenation <!--SR:!2024-11-28,227,330-->
- `LEFT(string, length)`::get the first `length` characters in `string` <!--SR:!2025-01-14,266,330-->
- `LEN(string)`::length of `string` <!--SR:!2025-01-01,257,330-->
- `LOWER(string)`::convert to lowercase <!--SR:!2024-10-29,204,330-->
- `RIGHT(string, length)`::get the last `length` characters in `string` <!--SR:!2024-12-24,246,330-->
- `SUBSTITUTE(string, old, new)`::replace all occurrences of `old` with `new` in `string` <!--SR:!2024-04-27,66,310-->
- `UPPER(string)`::convert to uppercase <!--SR:!2024-12-02,234,330-->

<!--/pytextgen-->

### common functions

Below are common functions:

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="93ba"--><!-- The following content is generated at 2024-01-31T12:52:39.241194+08:00. Any edits will be overridden! -->

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

<!--/pytextgen-->

<!--pytextgen generate section="ee42"--><!-- The following content is generated at 2024-01-31T12:52:39.155842+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`AVERAGE(numbers...)` <!--SR:!2024-08-27,129,270!2024-12-03,235,330-->
- `AVERAGE(numbers...)`→:::←`COUNTIF(values, criteria)` <!--SR:!2024-06-15,89,290!2024-05-12,31,290-->
- `COUNTIF(values, criteria)`→:::←`IF(boolean, value_if_true[, value_if_false = FALSE])` <!--SR:!2024-04-27,65,310!2024-04-26,22,270-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`→:::←`MAX(numbers...)` <!--SR:!2024-06-22,78,230!2024-05-29,79,270-->
- `MAX(numbers...)`→:::←`MIN(numbers...)` <!--SR:!2024-12-28,255,330!2024-12-04,237,330-->
- `MIN(numbers...)`→:::←`RANK(number, numbers...)` <!--SR:!2024-05-15,40,210!2024-07-04,108,270-->
- `RANK(number, numbers...)`→:::←`STDEV(numbers...)` <!--SR:!2024-07-23,110,250!2024-08-29,133,270-->
- `STDEV(numbers...)`→:::←`SUM(numbers...)` <!--SR:!2024-05-03,71,310!2024-09-03,134,270-->
- `SUM(numbers...)`→:::←_(end)_ <!--SR:!2024-06-17,88,290!2024-04-24,14,210-->

<!--/pytextgen-->

<!--pytextgen generate section="f123"--><!-- The following content is generated at 2024-01-31T12:52:39.120607+08:00. Any edits will be overridden! -->

- `AVERAGE(numbers...)`::average <!--SR:!2024-12-04,233,330-->
- `COUNTIF(values, criteria)`::number of `values` satisfying `criteria` <!--SR:!2024-04-25,64,310-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`::`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested <!--SR:!2025-01-05,258,330-->
- `MAX(numbers...)`::maximum <!--SR:!2024-12-14,241,330-->
- `MIN(numbers...)`::minimum <!--SR:!2024-12-12,239,330-->
- `RANK(number, numbers...)`::rank of `number` in `numbers`, starting from 1 <!--SR:!2024-10-23,184,310-->
- `STDEV(numbers...)`::standard deviation <!--SR:!2024-05-01,69,310-->
- `SUM(numbers...)`::summation <!--SR:!2025-01-17,270,330-->

<!--/pytextgen-->
