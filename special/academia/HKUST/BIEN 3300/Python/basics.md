---
aliases:
  - Python basic
  - Python basics
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/basics
  - language/in/English
---

# Python basics

```Python
# pytextgen generate module
# import ../../../../../../tools/utility.py.md
```

## operators

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2026-01-01,67,310-->

### arithmetic operators

Below are common arithmetic operators. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2026-01-11,76,329!2026-01-11,76,329!2026-01-11,76,329-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`**`", "power",),
  (
    "`*` <br/> "
    "`/` <br/> "
    "`//` <br/> "
    "`%`",
    "multiplication <br/> "
    "division <br/> "
    "floor division <br/> "
    "remainder; the resulting sign is the same as the divider, i.e. the number after the operator",
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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2025-09-21T20:03:36.972808+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `**` | power |
> | `*` <br/> `/` <br/> `//` <br/> `%` | multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator |
> | `+` <br/> `-` | addition <br/> subtraction |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2025-09-21T20:03:36.996978+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`**` <!--SR:!2026-01-11,76,329!2026-01-06,71,329-->
- `**`→::@::←`*` <br/> `/` <br/> `//` <br/> `%` <!--SR:!2026-01-11,76,329!2026-01-05,70,329-->
- `*` <br/> `/` <br/> `//` <br/> `%`→::@::←`+` <br/> `-` <!--SR:!2026-01-11,76,329!2026-01-11,76,329-->
- `+` <br/> `-`→::@::←_(end)_ <!--SR:!2026-01-11,76,329!2026-01-11,76,329-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2025-09-21T20:03:36.946434+08:00. Any edits will be overridden! -->

- `**`:@:power <!--SR:!2026-01-11,76,329-->
- `*` <br/> `/` <br/> `//` <br/> `%`:@:multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2026-01-11,76,329-->
- `+` <br/> `-`:@:addition <br/> subtraction <!--SR:!2026-01-07,72,329-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. The comparison operators below {@{have the same precedence}@}: <!--SR:!2025-12-30,65,310!2026-01-11,76,329!2026-01-11,76,329!2026-01-09,74,329-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`in`", "membership test",),
  ("`<`", "lesser than",),
  ("`<=`", "lesser than or equal to",),
  ("`>`", "greater than",),
  ("`>=`", "greater than or equal to",),
  ("`!=`", "not equal to",),
  ("`==`", "equal to",),
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

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2024-01-30T13:35:46.650809+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `in` | membership test |
> | `<` | lesser than |
> | `<=` | lesser than or equal to |
> | `>` | greater than |
> | `>=` | greater than or equal to |
> | `!=` | not equal to |
> | `==` | equal to |

<!--/pytextgen-->

<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`in` <!--SR:!2025-12-30,65,310!2025-12-18,55,310-->
- `in`→::@::←`<` <!--SR:!2025-12-30,65,310!2025-12-26,62,310-->
- `<`→::@::←`<=` <!--SR:!2025-12-20,57,310!2025-12-24,60,310-->
- `<=`→::@::←`>` <!--SR:!2025-12-19,56,310!2025-12-29,64,310-->
- `>`→::@::←`>=` <!--SR:!2025-12-31,66,310!2025-12-31,66,310-->
- `>=`→::@::←`!=` <!--SR:!2025-12-24,60,310!2025-12-19,56,310-->
- `!=`→::@::←`==` <!--SR:!2026-01-01,67,310!2025-12-17,54,310-->
- `==`→::@::←_(end)_ <!--SR:!2025-12-27,63,310!2025-12-24,60,310-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`:@:membership test <!--SR:!2026-01-01,67,310-->
- `<`:@:lesser than <!--SR:!2025-12-17,54,310-->
- `<=`:@:lesser than or equal to <!--SR:!2025-12-26,62,310-->
- `>`:@:greater than <!--SR:!2025-12-30,65,310-->
- `>=`:@:greater than or equal to <!--SR:!2025-12-17,54,310-->
- `!=`:@:not equal to <!--SR:!2025-12-23,59,310-->
- `==`:@:equal to <!--SR:!2025-12-21,58,310-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}. <!--SR:!2025-12-18,55,310-->

Also, one {@{CAN chain comparison operators}@} in Python, unlike {@{many other languages}@}. For example, {@{`2 <= aNumber <= 5`}@} is equivalent to {@{`2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once}@}. In fact, you can {@{chain any numbers of comparison operators together}@}, even if {@{they do not make sense together as a whole}@}, such as {@{`2 <= aNumber >= 2`}@} being {@{equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!2025-12-18,55,310!2025-12-21,58,310!2025-12-25,61,310!2025-12-19,56,310!2025-12-21,58,310!2026-01-01,67,310!2025-12-27,63,310!2025-12-23,59,310-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2025-12-29,64,310!2026-01-11,76,329!2026-01-08,73,329!2026-01-10,75,329-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`not`", "negate",),
  ("`and`", "and",),
  ("`or`", "or",),
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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2024-01-30T13:35:46.667324+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `not` | negate |
> | `and` | and |
> | `or` | or |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-01-30T13:35:46.722323+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`not` <!--SR:!2025-12-29,64,310!2025-12-27,63,310-->
- `not`→::@::←`and` <!--SR:!2025-12-23,59,310!2025-12-29,64,310-->
- `and`→::@::←`or` <!--SR:!2025-12-20,57,310!2025-12-31,66,310-->
- `or`→::@::←_(end)_ <!--SR:!2025-12-30,65,310!2025-12-20,57,310-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`:@:negate <!--SR:!2025-12-24,60,310-->
- `and`:@:and <!--SR:!2025-12-25,61,310-->
- `or`:@:or <!--SR:!2025-12-31,66,310-->

<!--/pytextgen-->

In particular, {@{`and` has a higher precedence than `or`}@}. This implies {@{`True or False and False` is `True or (False and False)` instead of `(True or False) and False`}@}. The former \(the correct one\) {@{is `True` while the latter \(the wrong one\) is `False`}@}. <!--SR:!2025-12-26,62,310!2025-12-07,43,290!2025-12-25,61,310-->

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}: <!--SR:!2025-12-27,63,310-->

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type before assigning to it}@}. <!--SR:!2025-12-21,58,310-->

Variable names are {@{case sensitive, cannot be keywords}@}, cannot have {@{some characters like spaces \(but underscores `_` are okay\), and cannot begin with some characters like numbers}@}.  Also, while allowed, it is recommended to {@{not use builtin names, e.g. `print`}@}, as we will {@{no longer be able to use those builtin functions of variables later \(replaced by us\)}@}. <!--SR:!2026-04-21,146,310!2026-01-11,76,329!2026-01-11,76,329!2026-01-11,76,329-->

### augmented assignment

Assignment supports {@{performing an arithmetic operation on an existing variable}@}. Use {@{`<op>=`}@}, where {@{`<op>` is the arithmetic operator}@}: <!--SR:!2025-12-23,59,310!2025-12-18,55,310!2025-12-19,56,310-->

```Python
variableName += 2
```

The variable must already {@{have a value assigned to it}@}. <!--SR:!2025-12-29,64,310-->
