---
aliases:
  - Excel formula
  - Excel formulae
  - Excel formulas
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/formula
  - language/in/English
---

# Excel formula

```Python
# pytextgen generate module
# import ../../../../tools/utility.py.md
```

A formula always {@{starts with an equals sign `=`}@}. <!--SR:!2028-10-22,1340,350-->

## cell reference

To get the value of a cell in a formula, {@{use its location, like `=A1`. This is known as a _cell reference_}@}. <!--SR:!2026-10-13,702,330-->

When copying and pasting formulas, the cell references in the formula are {@{offsetted by the same offset from the original cell to the copied cell}@}. To prevent this offset, {@{add ` $ ` before the column, the row, or both, like `=$A$1`}@}. <!--SR:!2027-05-05,892,330!2027-05-08,896,330-->

## operators

### arithmetic operators

Below are common arithmetic and string operators. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2027-07-10,518,397!2027-07-13,521,397!2027-07-17,524,397-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`^`", "power",),
  (
    "`*` <br/> "
    "`/`",
    "multiplication <br/> "
    "division",
  ),
  (
    "`+` <br/> "
    "`-`",
    "addition <br/> "
    "subtraction",
  ),
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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2026-01-25T23:32:20.917433+08:00. Any edits will be overridden! -->

> | operator      | description                   |
> | ------------- | ----------------------------- |
> | `^`           | power                         |
> | `*` <br/> `/` | multiplication <br/> division |
> | `+` <br/> `-` | addition <br/> subtraction    |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2025-09-21T20:03:37.027388+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`^` <!--SR:!2027-07-08,517,397!2027-07-21,528,397-->
- `^`→::@::←`*` <br/> `/` <!--SR:!2027-07-02,511,397!2027-07-20,527,397-->
- `*` <br/> `/`→::@::←`+` <br/> `-` <!--SR:!2027-07-11,519,397!2027-07-14,522,397-->
- `+` <br/> `-`→::@::←_(end)_ <!--SR:!2027-07-15,523,397!2027-07-12,520,397-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2025-09-21T20:03:37.077571+08:00. Any edits will be overridden! -->

- `^`:@:power <!--SR:!2027-07-09,518,397-->
- `*` <br/> `/`:@:multiplication <br/> division <!--SR:!2027-07-09,518,397-->
- `+` <br/> `-`:@:addition <br/> subtraction <!--SR:!2027-07-18,525,397-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{booleans}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. The comparison operators below {@{have the same precedence}@}: <!--SR:!2028-02-01,1133,350!2027-07-19,526,397!2027-07-06,515,397!2027-07-07,516,397-->

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

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2026-01-25T23:32:20.967213+08:00. Any edits will be overridden! -->

> | operator | description              |
> | -------- | ------------------------ |
> | `=`      | equal to                 |
> | `<`      | lesser than              |
> | `>`      | greater than             |
> | `<=`     | lesser than or equal to  |
> | `>=`     | greater than or equal to |
> | `<>`     | not equal to             |

<!--/pytextgen-->

<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-01-31T12:32:22.775056+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`=` <!--SR:!2027-05-05,787,290!2026-07-17,626,310-->
- `=`→::@::←`<` <!--SR:!2030-07-19,1714,310!2028-05-11,1177,330-->
- `<`→::@::←`>` <!--SR:!2028-05-18,1222,350!2027-05-11,898,330-->
- `>`→::@::←`<=` <!--SR:!2027-05-10,896,330!2029-04-05,1250,270-->
- `<=`→::@::←`>=` <!--SR:!2026-10-27,747,330!2026-09-06,667,290-->
- `>=`→::@::←`<>` <!--SR:!2026-08-18,523,290!2028-04-25,1017,330-->
- `<>`→::@::←_(end)_ <!--SR:!2027-07-17,978,350!2026-08-15,690,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-31T12:32:22.829082+08:00. Any edits will be overridden! -->

- `=`:@:equal to <!--SR:!2028-08-17,1290,350-->
- `<`:@:lesser than <!--SR:!2027-08-02,992,350-->
- `>`:@:greater than <!--SR:!2028-12-03,1374,350-->
- `<=`:@:lesser than or equal to <!--SR:!2027-03-22,818,330-->
- `>=`:@:greater than or equal to <!--SR:!2027-11-23,1078,350-->
- `<>`:@:not equal to <!--SR:!2028-06-18,1242,350-->

<!--/pytextgen-->

Also, one cannot chain {@{comparison operators, like `2 <= A1 <= 5`. [Logic functions](#logic%20functions) are needed instead, like `AND(2 <= A1, A1 <= 5)`}@}. <!--SR:!2028-12-20,1386,350-->

## functions

### logic functions

Below are common logic functions, all of which {@{accept booleans and return booleans}@}: <!--SR:!2028-09-24,1321,350-->

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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2026-01-25T23:32:20.977730+08:00. Any edits will be overridden! -->

> | function           | description              |
> | ------------------ | ------------------------ |
> | `NOT(boolean)`     | negate                   |
> | `AND(booleans...)` | every input is true      |
> | `OR(booleans...)`  | there exists true inputs |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-02-05T12:43:06.987947+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`NOT(boolean)` <!--SR:!2028-04-04,1183,350!2028-12-18,1388,350-->
- `NOT(boolean)`→::@::←`AND(booleans...)` <!--SR:!2026-06-10,643,330!2028-08-28,1296,350-->
- `AND(booleans...)`→::@::←`OR(booleans...)` <!--SR:!2027-12-02,1087,350!2026-09-20,720,330-->
- `OR(booleans...)`→::@::←_(end)_ <!--SR:!2027-12-23,1101,350!2027-07-11,898,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-05T12:43:07.023980+08:00. Any edits will be overridden! -->

- `NOT(boolean)`:@:negate <!--SR:!2028-05-27,1227,350-->
- `AND(booleans...)`:@:every input is true <!--SR:!2028-01-01,1110,350-->
- `OR(booleans...)`:@:there exists true inputs <!--SR:!2028-09-22,1320,350-->

<!--/pytextgen-->

### string functions and operators

Below are common string functions and operators:

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

<!--pytextgen generate section="0ff2"--><!-- The following content is generated at 2026-01-25T23:32:21.003172+08:00. Any edits will be overridden! -->

> | function                       | description                                             |
> | ------------------------------ | ------------------------------------------------------- |
> | (operator) `&`                 | concatenation                                           |
> | `LEFT(string, length)`         | get the first `length` characters in `string`           |
> | `LEN(string)`                  | length of `string`                                      |
> | `LOWER(string)`                | convert to lowercase                                    |
> | `RIGHT(string, length)`        | get the last `length` characters in `string`            |
> | `SUBSTITUTE(string, old, new)` | replace all occurrences of `old` with `new` in `string` |
> | `UPPER(string)`                | convert to uppercase                                    |

<!--/pytextgen-->

<!--pytextgen generate section="305b"--><!-- The following content is generated at 2024-01-31T12:40:31.061300+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←(operator) `&` <!--SR:!2029-09-13,1464,330!2029-01-02,1397,350-->
- (operator) `&`→::@::←`LEFT(string, length)` <!--SR:!2028-02-13,1036,310!2027-01-29,768,290-->
- `LEFT(string, length)`→::@::←`LEN(string)` <!--SR:!2028-10-12,1254,310!2026-09-26,624,250-->
- `LEN(string)`→::@::←`LOWER(string)` <!--SR:!2027-01-21,722,290!2028-03-08,1036,310-->
- `LOWER(string)`→::@::←`RIGHT(string, length)` <!--SR:!2026-10-18,388,170!2030-03-07,1495,270-->
- `RIGHT(string, length)`→::@::←`SUBSTITUTE(string, old, new)` <!--SR:!2026-10-07,618,270!2030-04-06,1509,270-->
- `SUBSTITUTE(string, old, new)`→::@::←`UPPER(string)` <!--SR:!2028-03-10,946,250!2026-06-05,327,190-->
- `UPPER(string)`→::@::←_(end)_ <!--SR:!2026-11-06,757,330!2027-09-15,964,310-->

<!--/pytextgen-->

<!--pytextgen generate section="29ca"--><!-- The following content is generated at 2024-01-31T12:40:31.103335+08:00. Any edits will be overridden! -->

- (operator) `&`:@:concatenation <!--SR:!2027-10-03,1039,350-->
- `LEFT(string, length)`:@:get the first `length` characters in `string` <!--SR:!2027-06-13,880,330-->
- `LEN(string)`:@:length of `string` <!--SR:!2028-03-15,1169,350-->
- `LOWER(string)`:@:convert to lowercase <!--SR:!2027-05-14,927,350-->
- `RIGHT(string, length)`:@:get the last `length` characters in `string` <!--SR:!2028-01-17,1119,350-->
- `SUBSTITUTE(string, old, new)`:@:replace all occurrences of `old` with `new` in `string` <!--SR:!2027-05-14,902,330-->
- `UPPER(string)`:@:convert to uppercase <!--SR:!2027-11-03,1065,350-->

<!--/pytextgen-->

### common functions

Below are common functions:

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

<!--pytextgen generate section="93ba"--><!-- The following content is generated at 2026-01-25T23:32:21.046485+08:00. Any edits will be overridden! -->

> | function                                               | description                                                                     |
> | ------------------------------------------------------ | ------------------------------------------------------------------------------- |
> | `AVERAGE(numbers...)`                                  | average                                                                         |
> | `COUNTIF(values, criteria)`                            | number of `values` satisfying `criteria`                                        |
> | `IF(boolean, value_if_true[, value_if_false = FALSE])` | `value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested |
> | `MAX(numbers...)`                                      | maximum                                                                         |
> | `MIN(numbers...)`                                      | minimum                                                                         |
> | `RANK(number, numbers...)`                             | rank of `number` in `numbers`, starting from 1                                  |
> | `STDEV(numbers...)`                                    | standard deviation                                                              |
> | `SUM(numbers...)`                                      | summation                                                                       |

<!--/pytextgen-->

<!--pytextgen generate section="ee42"--><!-- The following content is generated at 2024-01-31T12:52:39.155842+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`AVERAGE(numbers...)` <!--SR:!2031-05-27,1957,310!2027-11-05,1067,350-->
- `AVERAGE(numbers...)`→::@::←`COUNTIF(values, criteria)` <!--SR:!2027-03-19,750,290!2027-05-21,751,290-->
- `COUNTIF(values, criteria)`→::@::←`IF(boolean, value_if_true[, value_if_false = FALSE])` <!--SR:!2026-07-10,608,310!2027-09-26,931,310-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`→::@::←`MAX(numbers...)` <!--SR:!2026-07-19,579,250!2026-07-24,575,270-->
- `MAX(numbers...)`→::@::←`MIN(numbers...)` <!--SR:!2028-03-02,1160,350!2027-11-18,1078,350-->
- `MIN(numbers...)`→::@::←`RANK(number, numbers...)` <!--SR:!2029-01-11,1075,230!2028-04-21,1095,290-->
- `RANK(number, numbers...)`→::@::←`STDEV(numbers...)` <!--SR:!2027-12-23,972,270!2029-05-02,1349,290-->
- `STDEV(numbers...)`→::@::←`SUM(numbers...)` <!--SR:!2028-12-21,1387,350!2031-08-28,2034,310-->
- `SUM(numbers...)`→::@::←_(end)_ <!--SR:!2027-12-16,1023,310!2031-01-04,1794,290-->

<!--/pytextgen-->

<!--pytextgen generate section="f123"--><!-- The following content is generated at 2024-01-31T12:52:39.120607+08:00. Any edits will be overridden! -->

- `AVERAGE(numbers...)`:@:average <!--SR:!2027-10-31,1060,350-->
- `COUNTIF(values, criteria)`:@:number of `values` satisfying `criteria` <!--SR:!2028-06-13,1238,350-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`:@:`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested <!--SR:!2028-03-25,1175,350-->
- `MAX(numbers...)`:@:maximum <!--SR:!2027-12-16,1097,350-->
- `MIN(numbers...)`:@:minimum <!--SR:!2027-02-10,789,330-->
- `RANK(number, numbers...)`:@:rank of `number` in `numbers`, starting from 1 <!--SR:!2030-09-04,1660,330-->
- `STDEV(numbers...)`:@:standard deviation <!--SR:!2028-12-22,1388,350-->
- `SUM(numbers...)`:@:summation <!--SR:!2028-05-30,1229,350-->

<!--/pytextgen-->
