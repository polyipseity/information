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
# import ../../../../../scripts/utility.py.md
```

## operators

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2026-10-23,292,330-->

### arithmetic operators

Below are common arithmetic operators. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2027-01-01,352,349!2026-12-31,351,349!2026-12-31,351,349-->

```Python
# pytextgen generate data
from asyncer import create_task_group
from itertools import chain
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
results = []
async with create_task_group() as tg:
  results.append(tg.soonify(memorize_table)(
    __env__.cwf_sects("93ab", "f21a",),
    headers,
    table,
  ))
  results.append(tg.soonify(memorize_map)(
    __env__.cwf_sects(None, "9cda", None,),
    items_to_map(*table),
  ))
return chain.from_iterable([r.value for r in results])
```

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2026-01-25T23:32:20.656009+08:00. Any edits will be overridden! -->

> | operator                           | description                                                                                                                                           |
> | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `**`                               | power                                                                                                                                                 |
> | `*` <br/> `/` <br/> `//` <br/> `%` | multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator |
> | `+` <br/> `-`                      | addition <br/> subtraction                                                                                                                            |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2025-09-21T20:03:36.996978+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`**` <!--SR:!2026-12-31,351,349!2026-11-30,320,349-->
- `**`→::@::←`*` <br/> `/` <br/> `//` <br/> `%` <!--SR:!2026-12-31,351,349!2026-11-24,314,349-->
- `*` <br/> `/` <br/> `//` <br/> `%`→::@::←`+` <br/> `-` <!--SR:!2026-12-31,351,349!2027-01-01,352,349-->
- `+` <br/> `-`→::@::←_(end)_ <!--SR:!2026-12-31,351,349!2027-01-01,352,349-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2025-09-21T20:03:36.946434+08:00. Any edits will be overridden! -->

- `**`:@:power <!--SR:!2027-01-01,352,349-->
- `*` <br/> `/` <br/> `//` <br/> `%`:@:multiplication <br/> division <br/> floor division <br/> remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2026-12-31,351,349-->
- `+` <br/> `-`:@:addition <br/> subtraction <!--SR:!2026-12-07,327,349-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. The comparison operators below {@{have the same precedence}@}: <!--SR:!2026-10-14,283,330!2027-01-01,352,349!2026-12-31,351,349!2026-12-16,336,349-->

```Python
# pytextgen generate data
from asyncer import create_task_group
from itertools import chain
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
results = []
async with create_task_group() as tg:
  results.append(tg.soonify(memorize_table)(
    __env__.cwf_sects("bd23", "d123",),
    headers,
    table,
  ))
  results.append(tg.soonify(memorize_map)(
    __env__.cwf_sects(None, "cc23", None,),
    items_to_map(*table),
  ))
return chain.from_iterable([r.value for r in results])
```

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2026-01-25T23:32:20.670975+08:00. Any edits will be overridden! -->

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

- _(begin)_→::@::←`in` <!--SR:!2026-10-13,282,330!fsrs,2029-06-20T00:00:00.000Z,1045,1045.2595081,1,2,9,0,0,2026-08-10T00:00:00.000Z-->
- `in`→::@::←`<` <!--SR:!2026-10-14,283,330!2026-10-02,271,330-->
- `<`→::@::←`<=` <!--SR:!fsrs,2029-09-08T00:00:00.000Z,1107,1107.06552019,1,2,9,0,0,2026-08-28T00:00:00.000Z!2026-09-22,261,330-->
- `<=`→::@::←`>` <!--SR:!fsrs,2029-08-04T00:00:00.000Z,1080,1080.08717202,1,2,9,0,0,2026-08-20T00:00:00.000Z!2026-10-09,278,330-->
- `>`→::@::←`>=` <!--SR:!2026-10-15,284,330!2026-10-21,290,330-->
- `>=`→::@::←`!=` <!--SR:!2026-09-23,262,330!fsrs,2029-08-19T00:00:00.000Z,1092,1091.66087084,1,2,9,0,0,2026-08-23T00:00:00.000Z-->
- `!=`→::@::←`==` <!--SR:!2026-10-22,291,330!fsrs,2029-06-29T00:00:00.000Z,1053,1053.01305103,1,2,9,0,0,2026-08-11T00:00:00.000Z-->
- `==`→::@::←_(end)_ <!--SR:!2026-10-05,274,330!2026-09-24,263,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`:@:membership test <!--SR:!2026-10-20,289,330-->
- `<`:@:lesser than <!--SR:!fsrs,2029-06-24T00:00:00.000Z,1049,1049.13725568,1,2,9,0,0,2026-08-10T00:00:00.000Z-->
- `<=`:@:lesser than or equal to <!--SR:!2026-10-03,272,330-->
- `>`:@:greater than <!--SR:!2026-10-16,285,330-->
- `>=`:@:greater than or equal to <!--SR:!fsrs,2029-05-21T00:00:00.000Z,1022,1021.94953015,1,2,9,0,0,2026-08-03T00:00:00.000Z-->
- `!=`:@:not equal to <!--SR:!fsrs,2028-02-28T00:00:00.000Z,531,530.94934286,5.00637887,2,9,0,0,2026-09-15T00:00:00.000Z-->
- `==`:@:equal to <!--SR:!fsrs,2029-09-28T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-02T00:00:00.000Z-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}. <!--SR:!fsrs,2029-07-24T00:00:00.000Z,1072,1072.36160804,1,2,9,0,0,2026-08-17T00:00:00.000Z-->

Also, one {@{CAN chain comparison operators}@} in Python, unlike {@{many other languages}@}. For example, {@{`2 <= aNumber <= 5`}@} is equivalent to {@{`2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once}@}. In fact, you can {@{chain any numbers of comparison operators together}@}, even if {@{they do not make sense together as a whole}@}, such as {@{`2 <= aNumber >= 2`}@} being {@{equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!fsrs,2029-07-15T00:00:00.000Z,1065,1064.62815785,1,2,9,0,0,2026-08-15T00:00:00.000Z!fsrs,2029-09-19T00:00:00.000Z,1115,1114.75652523,1,2,9,0,0,2026-08-31T00:00:00.000Z!2026-09-27,266,330!fsrs,2029-08-09T00:00:00.000Z,1084,1083.94697941,1,2,9,0,0,2026-08-21T00:00:00.000Z!fsrs,2029-09-24T00:00:00.000Z,1119,1118.59914239,1,2,9,0,0,2026-09-01T00:00:00.000Z!2026-10-24,293,330!2026-10-07,276,330!fsrs,2028-02-25T00:00:00.000Z,529,529.03656056,5.00637887,2,9,0,0,2026-09-14T00:00:00.000Z-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. {@{Round brackets \(`()`\)}@} have {@{the highest precedence \(very intuitive\)}@}. Operators higher in the list {@{have higher precedence}@}: <!--SR:!2026-10-10,279,330!2026-12-31,351,349!2026-12-11,331,349!2026-12-25,345,349-->

```Python
# pytextgen generate data
from asyncer import create_task_group
from itertools import chain
headers = "operator", "description"
table = (
  ("`not`", "negate",),
  ("`and`", "and",),
  ("`or`", "or",),
)
results = []
async with create_task_group() as tg:
  results.append(tg.soonify(memorize_table)(
    __env__.cwf_sects("2856", "d882",),
    headers,
    table,
  ))
  results.append(tg.soonify(memorize_map)(
    __env__.cwf_sects(None, "ee13", None,),
    items_to_map(*table),
  ))
return chain.from_iterable([r.value for r in results])
```

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2026-01-25T23:32:20.699458+08:00. Any edits will be overridden! -->

> | operator | description |
> | -------- | ----------- |
> | `not`    | negate      |
> | `and`    | and         |
> | `or`     | or          |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-01-30T13:35:46.722323+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`not` <!--SR:!2026-10-09,278,330!2026-10-04,273,330-->
- `not`→::@::←`and` <!--SR:!fsrs,2028-09-20T00:00:00.000Z,730,730.25645087,2.49272837,2,9,0,0,2026-09-21T00:00:00.000Z!2026-10-11,280,330-->
- `and`→::@::←`or` <!--SR:!fsrs,2029-09-03T00:00:00.000Z,1103,1103.2172026,1,2,9,0,0,2026-08-27T00:00:00.000Z!2026-10-18,287,330-->
- `or`→::@::←_(end)_ <!--SR:!2026-10-12,281,330!fsrs,2029-08-29T00:00:00.000Z,1099,1099.36699517,1,2,9,0,0,2026-08-26T00:00:00.000Z-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`:@:negate <!--SR:!fsrs,2028-09-24T00:00:00.000Z,733,732.76739939,2.49272837,2,9,0,0,2026-09-22T00:00:00.000Z-->
- `and`:@:and <!--SR:!2026-09-28,267,330-->
- `or`:@:or <!--SR:!2026-10-17,286,330-->

<!--/pytextgen-->

In particular, {@{`and` has a higher precedence than `or`}@}. This implies {@{`True or False and False` is `True or (False and False)`}@} instead of {@{`(True or False) and False`}@}. The former \(the correct one\) {@{is `True` while the latter \(the wrong one\) is `False`}@}. <!--SR:!2026-09-30,269,330!2027-08-20,499,310!2026-09-29,268,330!2027-06-16,443,395-->

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}: <!--SR:!2026-10-06,275,330-->

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type}@} before {@{assigning to it}@}.  Reassigning the variable (i.e. {@{replacing the variable value}@}) uses {@{the same syntax as above}@}. To {@{use the value of a variable}@}, {@{simply write the variable name}@}. <!--SR:!fsrs,2029-10-03T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-03T00:00:00.000Z!fsrs,2027-01-29T00:00:00.000Z,140,140.44399864,1,2,2,0,0,2026-09-11T00:00:00.000Z!fsrs,2027-01-29T00:00:00.000Z,140,140.44399864,1,2,2,0,0,2026-09-11T00:00:00.000Z!fsrs,2027-01-29T00:00:00.000Z,140,140.44399864,1,2,2,0,0,2026-09-11T00:00:00.000Z!fsrs,2027-01-29T00:00:00.000Z,140,140.44399864,1,2,2,0,0,2026-09-11T00:00:00.000Z!fsrs,2027-01-29T00:00:00.000Z,140,140.44399864,1,2,2,0,0,2026-09-11T00:00:00.000Z-->

Variable names are {@{case sensitive, cannot be keywords}@}, cannot have {@{some characters like spaces \(but underscores `_` are okay\), and cannot begin with some characters like numbers}@}.  Also, while allowed, it is recommended to {@{not use builtin names, e.g. `print`}@}, as we will {@{no longer be able to use those builtin functions of variables later \(replaced by us\)}@}. <!--SR:!2028-01-17,627,330!2027-01-01,352,349!2027-01-01,352,349!2027-01-01,352,349-->

### augmented assignment

Assignment supports {@{performing an arithmetic operation on an existing variable}@}. Use {@{`<op>=`}@}, where {@{`<op>` is the arithmetic operator}@}: <!--SR:!fsrs,2028-09-17T00:00:00.000Z,728,727.74459265,2.49272837,2,9,0,0,2026-09-20T00:00:00.000Z!fsrs,2029-07-19T00:00:00.000Z,1068,1068.495917,1,2,9,0,0,2026-08-16T00:00:00.000Z!fsrs,2029-07-30T00:00:00.000Z,1076,1076.22532725,1,2,9,0,0,2026-08-19T00:00:00.000Z-->

```Python
variableName += 2
```

The variable must already {@{have a value assigned to it}@}. <!--SR:!2026-10-08,277,330-->
