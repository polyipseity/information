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

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2026-01-02,365,378-->

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

- _(begin)_→::@::←`**` <!--SR:!2026-08-31,706,330!2028-04-26,1201,350-->
- `**`→::@::←`*` <!--SR:!2027-07-17,978,350!2027-10-04,1040,350-->
- `*`→::@::←`/` <!--SR:!2028-09-03,1305,350!2027-07-05,969,350-->
- `/`→::@::←`//` <!--SR:!2027-09-05,1018,350!2027-09-10,1025,350-->
- `//`→::@::←`%` <!--SR:!2027-07-14,943,330!2029-01-09,1404,350-->
- `%`→::@::←`+` <!--SR:!2027-05-30,913,330!2028-04-25,1199,350-->
- `+`→::@::←`-` <!--SR:!2028-04-23,1199,350!2028-08-22,1293,350-->
- `-`→::@::←_(end)_ <!--SR:!2029-01-25,1415,350!2028-07-09,1260,350-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`:@:power <!--SR:!2027-05-05,920,350-->
- `*`:@:multiplication <!--SR:!2028-09-19,1315,350-->
- `/`:@:division <!--SR:!2027-07-14,946,330-->
- `//`:@:floor division <!--SR:!2028-07-05,1258,350-->
- `%`:@:remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2026-06-20,651,330-->
- `+`:@:addition <!--SR:!2028-07-04,1256,350-->
- `-`:@:subtraction <!--SR:!2027-11-11,1069,350-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2028-12-19,1385,350-->

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

- _(begin)_→::@::←`in` <!--SR:!2026-10-11,733,330!2028-05-28,1224,350-->
- `in`→::@::←`<` <!--SR:!2026-07-14,621,330!2026-02-01,487,270-->
- `<`→::@::←`<=` <!--SR:!2026-04-10,547,310!2026-02-24,518,330-->
- `<=`→::@::←`>` <!--SR:!2027-03-27,863,330!2025-12-16,304,210-->
- `>`→::@::←`>=` <!--SR:!2027-05-31,817,270!2028-09-01,1301,350-->
- `>=`→::@::←`!=` <!--SR:!2028-07-31,1220,310!2025-08-30,307,230-->
- `!=`→::@::←`==` <!--SR:!2025-07-18,390,310!2025-09-26,312,290-->
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

Also, one CAN chain {@{comparison operators in Python, unlike other languages. For example, `2 <= aNumber <= 5` is equivalent to `2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once. In fact, you can chain any numbers of comparison operators together, even if they do not make sense together as a whole, such as `2 <= aNumber >= 2` being equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!2027-10-07,1041,350-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2028-04-17,1196,350-->

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

In particular, {@{`and` has a higher precedence than `or`}@}. This implies {@{`True or False and False` is `True or (False and False)` instead of `(True or False) and False`}@}. The former \(the correct one\) {@{is `True` while the latter \(the wrong one\) is `False`}@}. <!--SR:!2025-04-18,19,356!2025-04-22,23,376!2025-04-22,23,376-->

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}: <!--SR:!2027-09-17,1027,350-->

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type before assigning to it}@}. <!--SR:!2027-03-21,858,330-->

Variable names are {@{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}@}. <!--SR:!2026-12-28,802,330-->
