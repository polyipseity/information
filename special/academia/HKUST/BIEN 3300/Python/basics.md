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

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted.

### arithmetic operators

Below are common arithmetic operators. Operators have higher precedence than or same precedence as operators below it in the list:

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`**`", "power",),
  ("`*`", "multiplication",),
  ("`/`", "division",),
  ("`//`", "floor division",),
  ("`%`", "remainder; the resulting sign is the same as the divider, i.e. the number after the operator",),
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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-01-30T13:35:46.570804+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `**` | power |
> | `*` | multiplication |
> | `/` | division |
> | `//` | floor division |
> | `%` | remainder; the resulting sign is the same as the divider, i.e. the number after the operator |
> | `+` | addition |
> | `-` | subtraction |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2024-01-30T13:35:46.598807+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`**`
- `**`→::@::←`*`
- `*`→::@::←`/`
- `/`→::@::←`//`
- `//`→::@::←`%`
- `%`→::@::←`+`
- `+`→::@::←`-`
- `-`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`:@:power
- `*`:@:multiplication
- `/`:@:division
- `//`:@:floor division
- `%`:@:remainder; the resulting sign is the same as the divider, i.e. the number after the operator
- `+`:@:addition
- `-`:@:subtraction

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list:

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

- _(begin)_→::@::←`in`
- `in`→::@::←`<`
- `<`→::@::←`<=`
- `<=`→::@::←`>`
- `>`→::@::←`>=`
- `>=`→::@::←`!=`
- `!=`→::@::←`==`
- `==`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`:@:membership test
- `<`:@:lesser than
- `<=`:@:lesser than or equal to
- `>`:@:greater than
- `>=`:@:greater than or equal to
- `!=`:@:not equal to
- `==`:@:equal to

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}.

Also, one {@{CAN chain comparison operators}@} in Python, unlike {@{many other languages}@}. For example, {@{`2 <= aNumber <= 5`}@} is equivalent to {@{`2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once}@}. In fact, you can {@{chain any numbers of comparison operators together}@}, even if {@{they do not make sense together as a whole}@}, such as {@{`2 <= aNumber >= 2`}@} being {@{equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>.

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list:

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

- _(begin)_→::@::←`not`
- `not`→::@::←`and`
- `and`→::@::←`or`
- `or`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`:@:negate
- `and`:@:and
- `or`:@:or

<!--/pytextgen-->

In particular, {@{`and` has a higher precedence than `or`}@}. This implies {@{`True or False and False` is `True or (False and False)` instead of `(True or False) and False`}@}. The former \(the correct one\) {@{is `True` while the latter \(the wrong one\) is `False`}@}.

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}:

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type before assigning to it}@}.

Variable names are {@{case sensitive, cannot be keywords}@}, cannot have {@{some characters like spaces \(but underscores `_` are okay\), and cannot begin with some characters like numbers}@}. Also, while allowed, it is recommended to {@{not use builtin names, e.g. `print`}@}, as we will {@{no longer be able to use those builtin functions of variables later \(replaced by us\)}@}.

### augmented assignment

Assignment supports {@{performing an arithmetic operation on an existing variable}@}. Use {@{`<op>=`}@}, where {@{`<op>` is the arithmetic operator}@}:

```Python
variableName += 2
```

The variable must already {@{have a value assigned to it}@}.
