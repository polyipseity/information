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

A formula always {@{starts with an equals sign `=`}@}.

## cell reference

To get the value of a cell in a formula, {@{use its location, like `=A1`. This is known as a _cell reference_}@}.

When copying and pasting formulas, the cell references in the formula are {@{offsetted by the same offset from the original cell to the copied cell}@}. To prevent this offset, {@{add ` $ ` before the column, the row, or both, like `=$A$1`}@}.

## operators

### arithmetic operators

Below are common arithmetic and string operators. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}:

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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2025-09-21T20:03:37.053459+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `^` | power |
> | `*` <br/> `/` | multiplication <br/> division |
> | `+` <br/> `-` | addition <br/> subtraction |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2025-09-21T20:03:37.027388+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`^`
- `^`→::@::←`*` <br/> `/`
- `*` <br/> `/`→::@::←`+` <br/> `-`
- `+` <br/> `-`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2025-09-21T20:03:37.077571+08:00. Any edits will be overridden! -->

- `^`:@:power
- `*` <br/> `/`:@:multiplication <br/> division
- `+` <br/> `-`:@:addition <br/> subtraction

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{booleans}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. The comparison operators below {@{have the same precedence}@}:

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

- _(begin)_→::@::←`=`
- `=`→::@::←`<`
- `<`→::@::←`>`
- `>`→::@::←`<=`
- `<=`→::@::←`>=`
- `>=`→::@::←`<>`
- `<>`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-31T12:32:22.829082+08:00. Any edits will be overridden! -->

- `=`:@:equal to
- `<`:@:lesser than
- `>`:@:greater than
- `<=`:@:lesser than or equal to
- `>=`:@:greater than or equal to
- `<>`:@:not equal to

<!--/pytextgen-->

Also, one cannot chain {@{comparison operators, like `2 <= A1 <= 5`. [Logic functions](#logic%20functions) are needed instead, like `AND(2 <= A1, A1 <= 5)`}@}.

## functions

### logic functions

Below are common logic functions, all of which {@{accept booleans and return booleans}@}:

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

- _(begin)_→::@::←`NOT(boolean)`
- `NOT(boolean)`→::@::←`AND(booleans...)`
- `AND(booleans...)`→::@::←`OR(booleans...)`
- `OR(booleans...)`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-05T12:43:07.023980+08:00. Any edits will be overridden! -->

- `NOT(boolean)`:@:negate
- `AND(booleans...)`:@:every input is true
- `OR(booleans...)`:@:there exists true inputs

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

- _(begin)_→::@::←(operator) `&`
- (operator) `&`→::@::←`LEFT(string, length)`
- `LEFT(string, length)`→::@::←`LEN(string)`
- `LEN(string)`→::@::←`LOWER(string)`
- `LOWER(string)`→::@::←`RIGHT(string, length)`
- `RIGHT(string, length)`→::@::←`SUBSTITUTE(string, old, new)`
- `SUBSTITUTE(string, old, new)`→::@::←`UPPER(string)`
- `UPPER(string)`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="29ca"--><!-- The following content is generated at 2024-01-31T12:40:31.103335+08:00. Any edits will be overridden! -->

- (operator) `&`:@:concatenation
- `LEFT(string, length)`:@:get the first `length` characters in `string`
- `LEN(string)`:@:length of `string`
- `LOWER(string)`:@:convert to lowercase
- `RIGHT(string, length)`:@:get the last `length` characters in `string`
- `SUBSTITUTE(string, old, new)`:@:replace all occurrences of `old` with `new` in `string`
- `UPPER(string)`:@:convert to uppercase

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

- _(begin)_→::@::←`AVERAGE(numbers...)`
- `AVERAGE(numbers...)`→::@::←`COUNTIF(values, criteria)`
- `COUNTIF(values, criteria)`→::@::←`IF(boolean, value_if_true[, value_if_false = FALSE])`
- `IF(boolean, value_if_true[, value_if_false = FALSE])`→::@::←`MAX(numbers...)`
- `MAX(numbers...)`→::@::←`MIN(numbers...)`
- `MIN(numbers...)`→::@::←`RANK(number, numbers...)`
- `RANK(number, numbers...)`→::@::←`STDEV(numbers...)`
- `STDEV(numbers...)`→::@::←`SUM(numbers...)`
- `SUM(numbers...)`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="f123"--><!-- The following content is generated at 2024-01-31T12:52:39.120607+08:00. Any edits will be overridden! -->

- `AVERAGE(numbers...)`:@:average
- `COUNTIF(values, criteria)`:@:number of `values` satisfying `criteria`
- `IF(boolean, value_if_true[, value_if_false = FALSE])`:@:`value_if_true` if `boolean` is true, otherwise `value_if_false`; can be nested
- `MAX(numbers...)`:@:maximum
- `MIN(numbers...)`:@:minimum
- `RANK(number, numbers...)`:@:rank of `number` in `numbers`, starting from 1
- `STDEV(numbers...)`:@:standard deviation
- `SUM(numbers...)`:@:summation

<!--/pytextgen-->
