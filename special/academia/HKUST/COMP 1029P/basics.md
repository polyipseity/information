---
aliases:
  - Python basic
  - Python basics
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/basics
  - language/in/English
---

# Python basics

```Python
# pytextgen generate module
# import ../../../../tools/utility.py.md
```

## operators

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2031-03-10,1891,398-->

### arithmetic operators

Below are common arithmetic operators. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2026-03-21,136,402!2026-03-18,134,402!2026-03-24,139,402-->

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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2026-01-25T23:32:20.871774+08:00. Any edits will be overridden! -->

> | operator                           | description                                                                                                                                           |
> | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `**`                               | power                                                                                                                                                 |
> | `*` <br/> `/` <br/> `//` <br/> `%` | multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator |
> | `+` <br/> `-`                      | addition <br/> subtraction                                                                                                                            |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2025-09-21T20:03:37.057451+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`**` <!--SR:!2026-03-24,139,402!2026-03-18,134,402-->
- `**`→::@::←`*` <br/> `/` <br/> `//` <br/> `%` <!--SR:!2028-02-17,708,422!2028-02-09,701,422-->
- `*` <br/> `/` <br/> `//` <br/> `%`→::@::←`+` <br/> `-` <!--SR:!2026-03-18,134,402!2026-03-17,133,402-->
- `+` <br/> `-`→::@::←_(end)_ <!--SR:!2026-03-16,132,402!2026-03-18,134,402-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2025-09-21T20:03:37.010169+08:00. Any edits will be overridden! -->

- `**`:@:power <!--SR:!2026-03-17,133,402-->
- `*` <br/> `/` <br/> `//` <br/> `%`:@:multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2028-02-12,703,422-->
- `+` <br/> `-`:@:addition <br/> subtraction <!--SR:!2028-02-18,709,422-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. The comparison operators below {@{have the same precedence}@}: <!--SR:!2028-12-19,1385,350!2026-03-22,137,402!2028-02-10,702,422!2028-02-14,705,422-->

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

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2026-01-25T23:32:20.909907+08:00. Any edits will be overridden! -->

> | operator | description              |
> | -------- | ------------------------ |
> | `in`     | membership test          |
> | `<`      | lesser than              |
> | `<=`     | lesser than or equal to  |
> | `>`      | greater than             |
> | `>=`     | greater than or equal to |
> | `!=`     | not equal to             |
> | `==`     | equal to                 |

<!--/pytextgen-->

<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`in` <!--SR:!2026-10-11,733,330!2028-05-28,1224,350-->
- `in`→::@::←`<` <!--SR:!2026-07-14,621,330!2031-02-13,1836,290-->
- `<`→::@::←`<=` <!--SR:!2026-04-10,547,310!2032-08-08,2357,350-->
- `<=`→::@::←`>` <!--SR:!2027-03-27,863,330!2028-06-12,909,230-->
- `>`→::@::←`>=` <!--SR:!2027-05-31,817,270!2028-09-01,1301,350-->
- `>=`→::@::←`!=` <!--SR:!2028-07-31,1220,310!2028-05-24,998,250-->
- `!=`→::@::←`==` <!--SR:!2030-02-15,1673,330!2029-03-12,1263,310-->
- `==`→::@::←_(end)_ <!--SR:!2028-02-26,1155,350!2026-11-17,761,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`:@:membership test <!--SR:!2028-02-24,1151,350-->
- `<`:@:lesser than <!--SR:!2028-10-16,1335,350-->
- `<=`:@:lesser than or equal to <!--SR:!2026-05-25,634,330-->
- `>`:@:greater than <!--SR:!2027-01-01,762,330-->
- `>=`:@:greater than or equal to <!--SR:!2028-10-07,1330,350-->
- `!=`:@:not equal to <!--SR:!2027-07-14,978,350-->
- `==`:@:equal to <!--SR:!2028-03-28,1179,350-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}. <!--SR:!2027-09-11,1019,350-->

Also, one {@{CAN chain comparison operators}@} in Python, unlike {@{many other languages}@}. For example, {@{`2 <= aNumber <= 5`}@} is equivalent to {@{`2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once}@}. In fact, you can {@{chain any numbers of comparison operators together}@}, even if {@{they do not make sense together as a whole}@}, such as {@{`2 <= aNumber >= 2`}@} being {@{equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!2027-10-07,1041,350!2027-12-14,696,420!2027-12-05,688,420!2027-12-25,706,420!2027-12-12,695,420!2027-11-29,683,420!2027-12-13,695,420!2027-12-24,705,420-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2028-04-17,1196,350!2026-03-22,137,402!2028-02-13,704,422!2028-02-11,703,422-->

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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2026-01-25T23:32:20.962215+08:00. Any edits will be overridden! -->

> | operator | description |
> | -------- | ----------- |
> | `not`    | negate      |
> | `and`    | and         |
> | `or`     | or          |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-01-30T13:35:46.722323+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`not` <!--SR:!2028-02-29,1154,350!2028-01-11,1120,350-->
- `not`→::@::←`and` <!--SR:!2028-02-01,1134,350!2028-08-15,1289,350-->
- `and`→::@::←`or` <!--SR:!2028-04-24,1196,350!2028-01-15,1123,350-->
- `or`→::@::←_(end)_ <!--SR:!2027-01-26,827,330!2027-06-18,955,350-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`:@:negate <!--SR:!2028-01-28,1133,350-->
- `and`:@:and <!--SR:!2027-04-30,917,350-->
- `or`:@:or <!--SR:!2027-08-25,1010,350-->

<!--/pytextgen-->

In particular, {@{`and` has a higher precedence than `or`}@}. This implies {@{`True or False and False` is `True or (False and False)`}@} instead of {@{`(True or False) and False`}@}. The former \(the correct one\) {@{is `True` while the latter \(the wrong one\) is `False`}@}. <!--SR:!2026-11-20,485,396!2027-06-01,650,416!2027-05-30,648,416!2026-06-02,140,423-->

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}: <!--SR:!2027-09-17,1027,350-->

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type before assigning to it}@}. <!--SR:!2027-03-21,858,330-->

Variable names are {@{case sensitive, cannot be keywords}@}, cannot have {@{some characters like spaces \(but underscores `_` are okay\), and cannot begin with some characters like numbers}@}.  Also, while allowed, it is recommended to {@{not use builtin names, e.g. `print`}@}, as we will {@{no longer be able to use those builtin functions of variables later \(replaced by us\)}@}. <!--SR:!2026-12-28,802,330!2026-03-21,136,402!2026-03-16,132,402!2026-03-23,138,402-->
