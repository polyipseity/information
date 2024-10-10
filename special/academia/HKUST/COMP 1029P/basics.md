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
# import ../../../../../tools/utility.py.md
```

## operators

The operator precedence for the 3 types of operators introduced below is {{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2024-10-20,20,358-->

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

- _(begin)_→:::←`**` <!--SR:!2026-08-31,706,330!2025-01-11,264,330-->
- `**`→:::←`*` <!--SR:!2024-11-11,216,330!2024-11-28,227,330-->
- `*`→:::←`/` <!--SR:!2025-02-06,287,330!2024-11-08,213,330-->
- `/`→:::←`//` <!--SR:!2024-11-21,224,330!2024-11-19,225,330-->
- `//`→:::←`%` <!--SR:!2024-12-12,220,310!2025-03-07,309,330-->
- `%`→:::←`+` <!--SR:!2024-11-28,213,310!2025-01-12,264,330-->
- `+`→:::←`-` <!--SR:!2025-01-10,263,330!2025-02-06,284,330-->
- `-`→:::←_(end)_ <!--SR:!2025-03-11,311,330!2025-01-26,277,330-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`::power <!--SR:!2024-10-27,202,330-->
- `*`::multiplication <!--SR:!2025-02-12,289,330-->
- `/`::division <!--SR:!2024-12-10,220,310-->
- `//`::floor division <!--SR:!2025-01-24,276,330-->
- `%`::remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2026-06-20,651,330-->
- `+`::addition <!--SR:!2025-01-25,276,330-->
- `-`::subtraction <!--SR:!2024-12-06,235,330-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {{a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2025-03-02,303,330-->

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

- _(begin)_→:::←`in` <!--SR:!2026-10-11,733,330!2025-01-18,269,330-->
- `in`→:::←`<` <!--SR:!2024-10-31,143,310!2026-02-01,487,270-->
- `<`→:::←`<=` <!--SR:!2026-04-10,547,310!2026-02-24,518,330-->
- `<=`→:::←`>` <!--SR:!2024-11-14,201,310!2025-02-15,144,210-->
- `>`→:::←`>=` <!--SR:!2025-03-04,233,250!2025-02-08,286,330-->
- `>=`→:::←`!=` <!--SR:!2025-03-29,301,290!2024-10-27,98,210-->
- `!=`→:::←`==` <!--SR:!2025-07-18,390,310!2024-11-18,81,270-->
- `==`→:::←_(end)_ <!--SR:!2024-12-28,254,330!2024-10-13,177,310-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`::membership test <!--SR:!2024-12-30,252,330-->
- `<`::lesser than <!--SR:!2025-02-19,294,330-->
- `<=`::lesser than or equal to <!--SR:!2026-05-25,634,330-->
- `>`::greater than <!--SR:!2024-11-29,231,330-->
- `>=`::greater than or equal to <!--SR:!2025-02-15,291,330-->
- `!=`::not equal to <!--SR:!2024-11-08,214,330-->
- `==`::equal to <!--SR:!2025-01-04,259,330-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}. <!--SR:!2024-11-26,225,330-->

Also, one CAN chain {{comparison operators in Python, unlike other languages. For example, `2 <= aNumber <= 5` is equivalent to `2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once. In fact, you can chain any numbers of comparison operators together, even if they do not make sense together as a whole, such as `2 <= aNumber >= 2` being equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!2024-11-30,229,330-->

### logic operators

Below are common logic operators, all of which {{accept two booleans and return a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2025-01-07,263,330-->

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

- _(begin)_→:::←`not` <!--SR:!2025-01-01,254,330!2024-12-17,245,330-->
- `not`→:::←`and` <!--SR:!2024-12-23,248,330!2025-02-03,282,330-->
- `and`→:::←`or` <!--SR:!2025-01-14,264,330!2024-12-18,247,330-->
- `or`→:::←_(end)_ <!--SR:!2024-10-21,187,310!2024-11-05,211,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`::negate <!--SR:!2024-12-20,249,330-->
- `and`::and <!--SR:!2024-10-25,200,330-->
- `or`::or <!--SR:!2024-11-18,222,330-->

<!--/pytextgen-->

## variable

To assign a value or the result of an expression to a variable, use {{`=`}}: <!--SR:!2024-11-24,226,330-->

```Python
variableName = 1 + 2
```

One does not need to {{declare the variable and its type before assigning to it}}. <!--SR:!2024-11-13,200,310-->

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}}. <!--SR:!2024-10-15,180,310-->
