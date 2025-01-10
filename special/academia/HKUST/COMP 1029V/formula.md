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
# import ../../../../../tools/utility.py.md
```

A formula always {@{starts with an equals sign `=`}@}. <!--SR:!2025-02-20,294,330-->

## cell reference

To get the value of a cell in a formula, {@{use its location, like `=A1`. This is known as a _cell reference_}@}. <!--SR:!2026-10-13,702,330-->

When copying and pasting formulas, the cell references in the formula are {@{offsetted by the same offset from the original cell to the copied cell}@}. To prevent this offset, {@{add ` $ ` before the column, the row, or both, like `=$A$1`}@}. <!--SR:!2027-05-05,892,330!2027-05-08,896,330-->

## operators

### arithmetic operators

Below are common arithmetic and string operators. Operators have higher precedence than or same precedence as operators below it in the list:

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

- _(begin)_→::@::←`^` <!--SR:!2025-11-09,452,310!2025-03-09,307,330-->
- `^`→::@::←`*` <!--SR:!2027-03-28,822,330!2026-08-23,697,330-->
- `*`→::@::←`/` <!--SR:!2026-11-14,758,330!2027-07-06,972,350-->
- `/`→::@::←`+` <!--SR:!2025-01-14,265,330!2025-01-26,277,330-->
- `+`→::@::←`-` <!--SR:!2028-02-12,1145,350!2027-12-26,1107,350-->
- `-`→::@::←_(end)_ <!--SR:!2025-02-13,292,330!2025-01-20,272,330-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-31T12:32:22.752951+08:00. Any edits will be overridden! -->

- `^`:@:power <!--SR:!2025-01-15,268,330-->
- `*`:@:multiplication <!--SR:!2028-04-12,1192,350-->
- `/`:@:division <!--SR:!2028-03-24,1178,350-->
- `+`:@:addition <!--SR:!2028-03-29,1181,350-->
- `-`:@:subtraction <!--SR:!2027-07-25,985,350-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{booleans}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2028-02-01,1133,350-->

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

- _(begin)_→::@::←`=` <!--SR:!2025-03-09,209,270!2026-07-17,626,310-->
- `=`→::@::←`<` <!--SR:!2025-11-08,425,290!2025-02-19,273,310-->
- `<`→::@::←`>` <!--SR:!2025-01-12,268,330!2027-05-11,898,330-->
- `>`→::@::←`<=` <!--SR:!2027-05-10,896,330!2025-11-02,355,250-->
- `<=`→::@::←`>=` <!--SR:!2026-10-27,747,330!2026-09-06,667,290-->
- `>=`→::@::←`<>` <!--SR:!2025-03-13,139,270!2025-07-09,237,310-->
- `<>`→::@::←_(end)_ <!--SR:!2027-07-17,978,350!2026-08-15,690,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-31T12:32:22.829082+08:00. Any edits will be overridden! -->

- `=`:@:equal to <!--SR:!2025-02-04,282,330-->
- `<`:@:lesser than <!--SR:!2027-08-02,992,350-->
- `>`:@:greater than <!--SR:!2025-02-28,302,330-->
- `<=`:@:lesser than or equal to <!--SR:!2027-03-22,818,330-->
- `>=`:@:greater than or equal to <!--SR:!2027-11-23,1078,350-->
- `<>`:@:not equal to <!--SR:!2025-01-23,273,330-->

<!--/pytextgen-->

Also, one cannot chain {@{comparison operators, like `2 <= A1 <= 5`. [Logic functions](#logic%20functions) are needed instead, like `AND(2 <= A1, A1 <= 5)`}@}. <!--SR:!2025-03-02,303,330-->

## functions

### logic functions

Below are common logic functions, all of which {@{accept booleans and return booleans}@}: <!--SR:!2025-02-11,290,330-->

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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2024-02-05T12:43:06.967772+08:00. Any edits will be overridden! -->

> | function | description |
> |-|-|
> | `NOT(boolean)` | negate |
> | `AND(booleans...)` | every input is true |
> | `OR(booleans...)` | there exists true inputs |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-02-05T12:43:06.987947+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`NOT(boolean)` <!--SR:!2028-04-04,1183,350!2025-03-01,304,330-->
- `NOT(boolean)`→::@::←`AND(booleans...)` <!--SR:!2026-06-10,643,330!2025-02-09,285,330-->
- `AND(booleans...)`→::@::←`OR(booleans...)` <!--SR:!2027-12-02,1087,350!2026-09-20,720,330-->
- `OR(booleans...)`→::@::←_(end)_ <!--SR:!2027-12-23,1101,350!2025-01-24,272,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-05T12:43:07.023980+08:00. Any edits will be overridden! -->

- `NOT(boolean)`:@:negate <!--SR:!2025-01-16,269,330-->
- `AND(booleans...)`:@:every input is true <!--SR:!2028-01-01,1110,350-->
- `OR(booleans...)`:@:there exists true inputs <!--SR:!2025-02-10,289,330-->

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

- _(begin)_→::@::←(operator) `&` <!--SR:!2025-09-10,444,330!2025-03-07,307,330-->
- (operator) `&`→::@::←`LEFT(string, length)` <!--SR:!2025-04-13,257,290!2027-01-29,768,290-->
- `LEFT(string, length)`→::@::←`LEN(string)` <!--SR:!2025-05-03,311,290!2026-09-26,624,250-->
- `LEN(string)`→::@::←`LOWER(string)` <!--SR:!2025-01-29,192,270!2025-05-04,257,290-->
- `LOWER(string)`→::@::←`RIGHT(string, length)` <!--SR:!2025-04-03,116,150!2026-01-30,426,250-->
- `RIGHT(string, length)`→::@::←`SUBSTITUTE(string, old, new)` <!--SR:!2025-01-27,229,270!2026-02-17,430,250-->
- `SUBSTITUTE(string, old, new)`→::@::←`UPPER(string)` <!--SR:!2025-08-04,291,230!2025-03-01,59,150-->
- `UPPER(string)`→::@::←_(end)_ <!--SR:!2026-11-06,757,330!2025-01-24,240,290-->

<!--/pytextgen-->

<!--pytextgen generate section="29ca"--><!-- The following content is generated at 2024-01-31T12:40:31.103335+08:00. Any edits will be overridden! -->

- (operator) `&`:@:concatenation <!--SR:!2027-10-03,1039,350-->
- `LEFT(string, length)`:@:get the first `length` characters in `string` <!--SR:!2025-01-14,266,330-->
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

- _(begin)_→::@::←`AVERAGE(numbers...)` <!--SR:!2025-12-27,485,290!2027-11-05,1067,350-->
- `AVERAGE(numbers...)`→::@::←`COUNTIF(values, criteria)` <!--SR:!2025-02-27,257,290!2025-04-28,259,290-->
- `COUNTIF(values, criteria)`→::@::←`IF(boolean, value_if_true[, value_if_false = FALSE])` <!--SR:!2026-07-10,608,310!2025-03-09,231,290-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`→::@::←`MAX(numbers...)` <!--SR:!2026-07-19,579,250!2026-07-24,575,270-->
- `MAX(numbers...)`→::@::←`MIN(numbers...)` <!--SR:!2028-03-02,1160,350!2027-11-18,1078,350-->
- `MIN(numbers...)`→::@::←`RANK(number, numbers...)` <!--SR:!2025-01-23,171,210!2025-04-21,291,270-->
- `RANK(number, numbers...)`→::@::←`STDEV(numbers...)` <!--SR:!2025-04-25,276,250!2025-08-22,358,270-->
- `STDEV(numbers...)`→::@::←`SUM(numbers...)` <!--SR:!2025-03-03,304,330!2026-01-20,504,290-->
- `SUM(numbers...)`→::@::←_(end)_ <!--SR:!2025-02-26,254,290!2026-02-05,476,270-->

<!--/pytextgen-->

<!--pytextgen generate section="f123"--><!-- The following content is generated at 2024-01-31T12:52:39.120607+08:00. Any edits will be overridden! -->

- `AVERAGE(numbers...)`:@:average <!--SR:!2027-10-31,1060,350-->
- `COUNTIF(values, criteria)`:@:number of `values` satisfying `criteria` <!--SR:!2025-01-22,272,330-->
- `IF(boolean, value_if_true[, value_if_false = FALSE])`:@:`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested <!--SR:!2028-03-25,1175,350-->
- `MAX(numbers...)`:@:maximum <!--SR:!2027-12-16,1097,350-->
- `MIN(numbers...)`:@:minimum <!--SR:!2027-02-10,789,330-->
- `RANK(number, numbers...)`:@:rank of `number` in `numbers`, starting from 1 <!--SR:!2025-01-26,95,290-->
- `STDEV(numbers...)`:@:standard deviation <!--SR:!2025-03-02,305,330-->
- `SUM(numbers...)`:@:summation <!--SR:!2025-01-17,270,330-->

<!--/pytextgen-->
