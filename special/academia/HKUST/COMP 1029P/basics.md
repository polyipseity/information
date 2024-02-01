---
aliases:
  - Python basic
  - Python basics
tags:
  - flashcards/special/academic/HKUST/COMP_1029P/basics
  - languages/in/English
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
e = __env__
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
    e.cwf_sects("93ab", "f21a",),
    headers,
    table,
  ),
  memorize_map(
    e.cwf_sects(None, "9cda", None,),
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

- _(begin)_→:::←`**` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `**`→:::←`*` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `*`→:::←`/` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `/`→:::←`//` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `//`→:::←`%` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `%`→:::←`+` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `+`→:::←`-` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `-`→:::←_(end)_ <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`::power <!--SR:!2024-02-04,4,270-->
- `*`::multiplication <!--SR:!2024-02-04,4,270-->
- `/`::division <!--SR:!2024-02-04,4,270-->
- `//`::floor division <!--SR:!2024-02-04,4,270-->
- `%`::remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2024-02-04,4,270-->
- `+`::addition <!--SR:!2024-02-04,4,270-->
- `-`::subtraction <!--SR:!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### comparison operators

Below are common comparison operators, all of which returns {{a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-02-04,4,270-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
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
    e.cwf_sects("bd23", "d123",),
    headers,
    table,
  ),
  memorize_map(
    e.cwf_sects(None, "cc23", None,),
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

- _(begin)_→:::←`in` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `in`→:::←`<` <!--SR:!2024-02-04,4,270!2024-02-03,3,250-->
- `<`→:::←`<=` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `<=`→:::←`>` <!--SR:!2024-02-04,4,270!2024-02-03,3,250-->
- `>`→:::←`>=` <!--SR:!2024-02-03,3,250!2024-02-04,4,270-->
- `>=`→:::←`!=` <!--SR:!2024-02-03,3,250!2024-02-04,4,270-->
- `!=`→:::←`==` <!--SR:!2024-02-03,3,250!2024-02-04,4,270-->
- `==`→:::←_(end)_ <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`::membership test <!--SR:!2024-02-04,4,270-->
- `<`::lesser than <!--SR:!2024-02-04,4,270-->
- `<=`::lesser than or equal to <!--SR:!2024-02-04,4,270-->
- `>`::greater than <!--SR:!2024-02-04,4,270-->
- `>=`::greater than or equal to <!--SR:!2024-02-04,4,270-->
- `!=`::not equal to <!--SR:!2024-02-04,4,270-->
- `==`::equal to <!--SR:!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}. <!--SR:!2024-02-04,4,270-->

Also, one cannot chain {{comparison operators, like `2 <= aNumber <= 5`. [Conditional operators](#conditional%20operators) are needed instead, like `2 <= aNumber and aNumber <= 5`}}. <!--SR:!2024-02-04,4,270-->

### conditional operators

Below are common conditional operators, all of which {{accept two booleans and return a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-02-04,4,270-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "operator", "description"
table = (
  ("`not`", "negate",),
  ("`and`", "and",),
  ("`or`", "or",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    e.cwf_sects("2856", "d882",),
    headers,
    table,
  ),
  memorize_map(
    e.cwf_sects(None, "ee13", None,),
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

- _(begin)_→:::←`not` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `not`→:::←`and` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `and`→:::←`or` <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
- `or`→:::←_(end)_ <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`::negate <!--SR:!2024-02-04,4,270-->
- `and`::and <!--SR:!2024-02-04,4,270-->
- `or`::or <!--SR:!2024-02-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## variable

To assign a value or the result of an expression to a variable, use {{`=`}}: <!--SR:!2024-02-04,4,270-->

```Python
variableName = 1 + 2
```

One does not need to {{declare the variable and its type before assigning to it}}. <!--SR:!2024-02-04,4,270-->

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}}. <!--SR:!2024-02-04,4,270-->
