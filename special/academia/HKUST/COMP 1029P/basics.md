---
aliases:
  - Python basic
  - Python basics
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/basics
  - language/in/English
---

# Python basics

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../tools/utility.py.md
```

%%

## operators

### arithmetic operators

Below are common arithmetic operators. Operators have higher precedence than or same precedence as operators below it in the list:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93ab"--><!-- The following content is generated at 2024-01-30T13:35:46.570804+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `**` | power |
> | `*` | multiplication |
> | `/` | division |
> | `//` | floor division |
> | `%` | remainder; the resulting sign is the same as the divider, i.e. the number after the operator |
> | `+` | addition |
> | `-` | subtraction |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f21a"--><!-- The following content is generated at 2024-01-30T13:35:46.598807+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`**` <!--SR:!2024-04-11,53,310!2024-04-21,61,310-->
- `**`→:::←`*` <!--SR:!2024-04-09,51,310!2024-04-14,55,310-->
- `*`→:::←`/` <!--SR:!2024-04-25,64,310!2024-04-09,51,310-->
- `/`→:::←`//` <!--SR:!2024-04-11,52,310!2024-04-08,50,310-->
- `//`→:::←`%` <!--SR:!2024-05-05,73,310!2024-05-02,70,310-->
- `%`→:::←`+` <!--SR:!2024-04-29,68,310!2024-04-23,62,310-->
- `+`→:::←`-` <!--SR:!2024-04-22,61,310!2024-04-28,66,310-->
- `-`→:::←_(end)_ <!--SR:!2024-05-04,72,310!2024-04-24,64,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`::power <!--SR:!2024-04-06,48,310-->
- `*`::multiplication <!--SR:!2024-04-29,67,310-->
- `/`::division <!--SR:!2024-05-04,72,310-->
- `//`::floor division <!--SR:!2024-04-23,63,310-->
- `%`::remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2024-04-07,49,310-->
- `+`::addition <!--SR:!2024-04-24,64,310-->
- `-`::subtraction <!--SR:!2024-04-14,55,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### comparison operators

Below are common comparison operators, all of which returns {{a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-05-03,71,310-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bd23"--><!-- The following content is generated at 2024-01-30T13:35:46.650809+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `in` | membership test |
> | `<` | lesser than |
> | `<=` | lesser than or equal to |
> | `>` | greater than |
> | `>=` | greater than or equal to |
> | `!=` | not equal to |
> | `==` | equal to |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d123"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`in` <!--SR:!2024-04-17,57,310!2024-04-24,63,310-->
- `in`→:::←`<` <!--SR:!2024-05-05,73,310!2024-03-04,14,230-->
- `<`→:::←`<=` <!--SR:!2024-04-16,56,310!2024-04-22,62,310-->
- `<=`→:::←`>` <!--SR:!2024-04-26,65,310!2024-03-01,12,230-->
- `>`→:::←`>=` <!--SR:!2024-03-04,12,230!2024-04-28,67,310-->
- `>=`→:::←`!=` <!--SR:!2024-03-12,30,270!2024-03-11,21,250-->
- `!=`→:::←`==` <!--SR:!2024-03-16,33,290!2024-04-13,54,310-->
- `==`→:::←_(end)_ <!--SR:!2024-04-18,59,310!2024-04-19,59,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`::membership test <!--SR:!2024-04-21,60,310-->
- `<`::lesser than <!--SR:!2024-05-01,69,310-->
- `<=`::lesser than or equal to <!--SR:!2024-03-23,37,290-->
- `>`::greater than <!--SR:!2024-04-12,54,310-->
- `>=`::greater than or equal to <!--SR:!2024-04-30,68,310-->
- `!=`::not equal to <!--SR:!2024-04-08,50,310-->
- `==`::equal to <!--SR:!2024-04-20,60,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}. <!--SR:!2024-04-13,55,310-->

Also, one cannot chain {{comparison operators, like `2 <= aNumber <= 5`. [Logic operators](#logic%20operators) are needed instead, like `2 <= aNumber and aNumber <= 5`}}. <!--SR:!2024-04-14,55,310-->

### logic operators

Below are common logic operators, all of which {{accept two booleans and return a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-04-19,60,310-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2856"--><!-- The following content is generated at 2024-01-30T13:35:46.667324+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `not` | negate |
> | `and` | and |
> | `or` | or |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d882"--><!-- The following content is generated at 2024-01-30T13:35:46.722323+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`not` <!--SR:!2024-04-21,60,310!2024-04-16,57,310-->
- `not`→:::←`and` <!--SR:!2024-04-19,59,310!2024-04-27,66,310-->
- `and`→:::←`or` <!--SR:!2024-04-25,64,310!2024-04-14,56,310-->
- `or`→:::←_(end)_ <!--SR:!2024-04-17,58,310!2024-04-07,49,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`::negate <!--SR:!2024-04-15,56,310-->
- `and`::and <!--SR:!2024-04-06,48,310-->
- `or`::or <!--SR:!2024-04-10,52,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## variable

To assign a value or the result of an expression to a variable, use {{`=`}}: <!--SR:!2024-04-12,53,310-->

```Python
variableName = 1 + 2
```

One does not need to {{declare the variable and its type before assigning to it}}. <!--SR:!2024-04-27,65,310-->

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}}. <!--SR:!2024-04-18,58,310-->
