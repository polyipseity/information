---
aliases:
  - Python basic
  - Python basics
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/basics
  - language/in/English
---

# Python basics

```Python
# pytextgen generate module
# import ../../../../../tools/utility.py.md
```

## operators

The operator precedence for the 3 types of operators introduced below is {@{[arithmetic operators](#arithmetic%20operators), [comparison operators](#comparison%20operators), and finally [logic operators](#logic%20operators)}@}. Note that this only considers operators mentioned below and not any others omitted. <!--SR:!2026-03-15,405,386-->

### arithmetic operators

Below are common arithmetic operators. Brackets have {@{the highest precedence (very intuitive)}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2025-09-30,304,342-->

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

- _(begin)_→::@::←`**` <!--SR:!2025-09-10,287,342!2025-07-17,240,330-->
- `**`→::@::←`*` <!--SR:!2025-08-06,259,342!2025-11-26,348,342-->
- `*`→::@::←`/` <!--SR:!2025-10-20,319,342!2025-11-19,344,342-->
- `/`→::@::←`//` <!--SR:!2025-08-13,264,342!2025-11-27,349,342-->
- `//`→::@::←`%` <!--SR:!2025-06-20,218,330!2025-09-20,294,342-->
- `%`→::@::←`+` <!--SR:!2025-09-17,293,342!2025-06-14,213,322-->
- `+`→::@::←`-` <!--SR:!2025-07-07,232,330!2025-11-18,342,342-->
- `-`→::@::←_(end)_ <!--SR:!2025-10-30,327,342!2025-11-07,335,342-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`:@:power <!--SR:!2025-07-20,243,330-->
- `*`:@:multiplication <!--SR:!2025-10-26,325,342-->
- `/`:@:division <!--SR:!2025-08-12,264,342-->
- `//`:@:floor division <!--SR:!2025-10-21,320,342-->
- `%`:@:remainder; the resulting sign is the same as the divider, i.e. the number after the operator <!--SR:!2025-08-23,273,342-->
- `+`:@:addition <!--SR:!2025-09-03,282,342-->
- `-`:@:subtraction <!--SR:!2025-10-22,321,342-->

<!--/pytextgen-->

For the return type of operators, all of above (if only `float` and `int` are considered), with two exceptions, {@{returns `int` (integer) if both operands are `int`, and `float` otherwise}@}. The two exceptions are {@{that `/` (division) always return `float`, even if both operands are `int`}@}, and {@{applying `**` (power) on a negative base results in a `complex` (complex number) but not an error, which is not discussed here}@}. <!--SR:!2025-06-11,210,322!2025-09-20,296,342!2025-10-12,313,342-->

A note regarding accuracy is that {@{there may be some inaccuracies involved when `float`s are involved, such as `0.1 + 0.2` is `0.30000000000000004` instead of `0.3`}@}. Also, regarding zeros, {@{`0.0` and `-0.0` are technically different `float`s, but they are equivalent for most purposes and even compare the same, i.e. `0.0 == -0.0` is `True`}@}. Finally, a notable error (raising an error causes {@{the program to stop and print out error messages}@}) is that {@{`/` (division), `//` (floor division), and `%` (remainder) raises `ZeroDivisionError` if the second operand is zero}@}. However, `0 ** 0` (power) {@{returns `1` instead of being undefined or raising an error}@}. <!--SR:!2025-11-09,336,342!2025-08-14,265,342!2025-07-13,222,322!2025-09-09,286,342!2025-05-02,170,340-->

### comparison operators

Below are common comparison operators, all of which returns {@{a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2026-06-12,503,389-->

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

- _(begin)_→::@::←`in` <!--SR:!2026-05-17,481,389!2026-06-18,509,389-->
- `in`→::@::←`<` <!--SR:!2025-11-03,328,369!2025-11-21,331,369-->
- `<`→::@::←`<=` <!--SR:!2025-10-10,309,369!2025-09-22,293,369-->
- `<=`→::@::←`>` <!--SR:!2025-09-28,295,369!2025-09-27,298,369-->
- `>`→::@::←`>=` <!--SR:!2025-09-03,274,369!2026-06-19,510,389-->
- `>=`→::@::←`!=` <!--SR:!2025-08-23,265,369!2026-03-19,409,329-->
- `!=`→::@::←`==` <!--SR:!2025-10-05,304,369!2026-05-21,485,389-->
- `==`→::@::←_(end)_ <!--SR:!2025-07-19,235,369!2025-12-19,354,369-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.619801+08:00. Any edits will be overridden! -->

- `in`:@:membership test <!--SR:!2026-06-19,510,389-->
- `<`:@:lesser than <!--SR:!2025-12-20,355,369-->
- `<=`:@:lesser than or equal to <!--SR:!2026-06-11,502,389-->
- `>`:@:greater than <!--SR:!2026-06-18,509,389-->
- `>=`:@:greater than or equal to <!--SR:!2026-06-17,508,389-->
- `!=`:@:not equal to <!--SR:!2026-06-22,513,389-->
- `==`:@:equal to <!--SR:!2026-06-21,512,389-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}. <!--SR:!2026-05-18,482,389-->

Also, one CAN chain {@{comparison operators in Python, unlike other languages. For example, `2 <= aNumber <= 5` is equivalent to `2 <= aNumber and aNumber <= 5` except that `aNumber` is evaluated only once. In fact, you can chain any numbers of comparison operators together, even if they do not make sense together as a whole, such as `2 <= aNumber >= 2` being equivalent to `2 <= aNumber and aNumber >= 2` except that `aNumber` is evaluated only once}@}. See <https://docs.python.org/3/reference/expressions.html#comparisons>. <!--SR:!2025-08-04,249,369-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2026-02-02,373,369-->

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

- _(begin)_→::@::←`not` <!--SR:!2026-06-14,505,389!2026-06-17,508,389-->
- `not`→::@::←`and` <!--SR:!2026-06-15,506,389!2026-05-16,480,389-->
- `and`→::@::←`or` <!--SR:!2025-06-20,209,349!2026-06-16,507,389-->
- `or`→::@::←_(end)_ <!--SR:!2026-05-19,483,389!2025-07-12,229,369-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.696328+08:00. Any edits will be overridden! -->

- `not`:@:negate <!--SR:!2026-04-19,459,389-->
- `and`:@:and <!--SR:!2026-06-13,504,389-->
- `or`:@:or <!--SR:!2026-05-23,487,389-->

<!--/pytextgen-->

## mathematics

- `abs(<int/float>)` ::@:: Returns the absolute value of the first argument. The return type is the same as the input type. (Note that the two `float`s, `-0.0` and `0.0`, are technically different, and `abs` turns both of them into `0.0`.) <!--SR:!2025-04-28,175,322!2025-05-25,196,322-->
- `round(<int/float>[, <int/None> = None])` ::@:: Round the first argument to the number of decimal places specified by the 2nd argument (if unspecified, `None`). Tie-breaking rounds to even multiples (for Python 3; Python 2 is round away from zero), so `round(0.5)` is `0`, `round(1.5)` is `2`, and `round(0.75, 1)` and `round(0.85, 1)` are both `0.8`. (Note that `float`s usually cannot represent decimals exactly. For example, `round(2.675, 2)` yields `2.67` instead of the expected `2.68`, because `2.675` is internally represented by a `float` that is not _exactly_ `2.675`.) For the 2nd argument, negative values are possible, and `None` is the same (except for return types) as `0`. The return type is always the same as the input type, except if the first argument is `float` and the 2nd argument is `None` at the same time, then the return type is `int`. <!--SR:!2026-07-26,508,322!2025-05-16,189,322-->
- `math.log(<int/float>)` ::@:: Requires importing `math` first by `import math`. Returns the natural logarithm (base is _e_) of the provided number. Always output a `float`. It does not accept nonpositive (raises a `ValueError` error) or complex numbers (raises a `TypeError` error). The number provided to `sqrt` is always converted into a `float` first before applying the natural algorithm on it. <!--SR:!2026-04-05,411,343!2025-04-27,170,343-->
- `math.pi` ::@:: A `float` representing the value of pi. It is NOT a function (so `math.pi()` is invalid), but a variable. <!--SR:!2025-09-13,287,363!2026-05-05,478,383-->
- `math.sqrt(<int/float>)` ::@:: Requires importing `math` first by `import math`. Returns the square root of the provided number. Always output a `float`. The differences from `<int/float> ** 0.5` are that `sqrt` does not accept negative (raises a `ValueError` error) or complex numbers (raises a `TypeError` error), and the number provided to `sqrt` is always converted into a `float` first before applying the square root on it. <!--SR:!2025-05-26,197,322!2025-05-06,169,302-->
- `random.randint(a, b)` ::@:: Requires importing `random` first by `import random`. Returns a random `int` _N_ such that _a_ ≤ _N_ ≤ _b_. If _a_ > _b_, then raises a `ValueError`. <!--SR:!2027-02-02,684,417!2025-08-25,182,377-->

## string

To define a string in Python, {@{enclose the string in either double quotes `"example"` or single quotes `'example'`. Both are equivalent except that you need to escape double quotes in the strings for the first one and single quotes for the second one}@}. Note that the enclosing quotes are {@{not part of the string}@}. To escape a character, {@{precede the character with a backslash `\`, like `"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}@}. Note that you cannot {@{add literal new lines inside a string if you use the above format}@}. Instead, you need to {@{use `\n` to represent newlines}@}. However, you can {@{add literal new lines you enclose the strings in 3 double quotes `"""example"""` or 3 single quotes `'''example'''`}@}. Additionally with this format, {@{you only need to escape quotes if there are 3 consecutive quotes of the same type as the enclosing quotes}@}. <!--SR:!2025-06-21,219,330!2025-12-01,353,342!2025-08-19,269,342!2025-08-05,258,342!2025-09-03,282,342!2025-06-07,207,322!2025-03-27,148,310-->

`\` is {@{the escape character}@}. Apart from {@{escaping quotes (`\"`, `\'`) and itself (`\\`)}@}, it can also {@{represent a newline using `\n` and a tab character (kinda like a wider space, but not exactly) using `\t`}@}. <!--SR:!2026-01-05,356,363!2025-11-04,322,363!2025-09-03,279,363-->

To {@{find the length of a string}@}, use {@{`len(str)`, which returns an `int` representing the number of characters in `str`}@}. To {@{concatenate/join two strings}@}, use {@{the `+` operator}@}. If {@{the `+` operator is applied between a `str` and another (incompatible) type}@}, then {@{a `TypeError` will be raised}@}. <!--SR:!2026-05-20,484,389!2025-11-05,319,369!2026-06-20,511,389!2026-06-16,507,389!2026-08-11,554,406!2026-05-22,486,406-->

Like lists, strings can be {@{indexed using the `string_var[n]`, which access the _n_ + 1-th character of the string}@}. If {@{the index is out of range}@}, then {@{an `IndexError` will be raised}@}. But unlike lists, strings {@{cannot be modified using the indexing notation, because strings in Python are immutable (not modifiable)}@}. <!--SR:!2026-07-28,496,397!2027-02-06,687,417!2027-01-20,672,417!2027-01-14,667,417-->

## output

In {@{a Jupyter notebook}@}, it outputs {@{the value of the last expression (and prints nothing if the last expression is `None`)}@}. Note that {@{assignments are not expressions, and do not produce output as the last expression}@}. To get it to print more things, {@{use `print(<any>...)`}@}. It can {@{print anything (and prints `None` if the last expression is `None`)}@}. Note that it automatically {@{adds a newline after the printed content, so each `print` outputs on a new line instead of being glued together in a single line}@}. Also, when multiple arguments are passed, {@{each argument is joined into a single string, separated by a space in between}@}. When {@{no arguments are passed, only a newline is printed}@}. <!--SR:!2025-10-27,318,363!2026-04-11,458,383!2025-12-30,351,363!2026-04-05,457,383!2025-10-13,312,363!2025-08-12,265,363!2025-08-06,260,363!2026-05-20,491,383-->

Note that strings are outputted, escaped {@{with `\` properly (without unnecessary escapes)}@}, and preferably {@{wrapped in `'`, and only uses `"` if there is at least 1 `'` in the string but not any `"`}@}. <!--SR:!2026-06-25,516,394!2026-05-24,488,394-->

If {@{you do not want a newline to be printed automatically afterwards}@}, `print` has {@{the `end` argument, which is used like `print(..., end=...)`}@}. The value passed to it {@{must be either a `str` or `None`, and `None` is the default value if you do not specify `end` and represents a newline, explaining why a newline is automatically printed without using `end`}@}. If `end` is used, then {@{after printing the passed objects as strings, the string passed to `end` is also printed (or if `end` is `None`, a newline is printed)}@}. For example, {@{`print(..., end="")` disables automatically printing a newline afterwards, while `print(..., end=" ")` automatically prints a space instead of a newline afterwards}@}. <!--SR:!2025-05-03,166,392!2026-10-17,590,392!2025-05-02,165,392!2025-11-11,285,352!2026-10-13,587,392-->

## variable

To {@{assign a value or the result of an expression to a variable}@}, use {@{`=`}@}: <!--SR:!2025-06-27,222,322!2025-10-28,327,342-->

```Python
variableName = 1 + 2
```

One does not need to {@{declare the variable and its type before assigning to it}@}. Reassigning the variable (i.e. {@{replacing the variable value}@}) uses {@{the same syntax as above}@}. To {@{use the value of a variable}@}, {@{simply write the variable name}@}. <!--SR:!2025-09-26,300,342!2025-11-01,329,342!2025-05-15,188,322!2025-06-08,208,322!2025-11-10,335,342-->

Variable names are {@{case sensitive, cannot be keywords, cannot have some characters like spaces (but underscores `_` are okay), and cannot begin with some characters like numbers}@}. Also, while allowed, it is recommended to {@{not use builtin names, e.g. `print`, as we will no longer be able to use those builtin functions of variables later (replaced by us)}@}. <!--SR:!2026-11-16,608,330!2025-07-17,241,330-->

Variable name should be {@{descriptive of the values it is supposed to hold}@}. <!--SR:!2025-10-05,308,342-->

ISOM 2020 note: {@{`+=`, `-=`, `*=`, `/=`, etc.}@} are {@{not taught and should NOT be used in exercises or exams}@}. <!--SR:!2025-03-22,127,397!2027-02-04,685,417-->

## data types

Below are common data types:

- `NoneType` :@: The type for the `None` value. <!--SR:!2025-11-20,345,342-->
- `bool` :@: A boolean, which is either `True` or `False`. Note that `bool`s are also `int`s. In particular, `True == 1` and `False == 0`, and can be used in arithmetic operators. <!--SR:!2025-08-17,268,342-->
- `float` :@: A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. `float` can hold integers as well, with only the internal representation being different from `int`. Example: `1.`, `3.14`, `9.20`, `2e3` (2×10<sup>3</sup>). <!--SR:!2025-05-05,169,310-->
- `int` :@: An integer. Example: `42`. <!--SR:!2025-09-26,300,342-->
- `str` :@: A piece of text. Example: `"Hello"`. <!--SR:!2025-08-23,273,342-->

Some interesting facts about `float`s:  `print`, for relatively small `float`s, {@{it always outputs at least 1 decimal place for `float`s, and outputs at most as many digits as needed to represent the number exactly}@}. For relatively large `floats`, {@{it outputs the float in exponential notation, e.g. `1e+100`, `1.2e-100`, etc.}@} `1` {@{is an `int` while `1.` and `1.0` are `float`s representing the same value `1`}@}. <!--SR:!2025-06-02,202,322!2025-04-02,153,310!2025-08-23,270,363-->

To get the type of a value, {@{use `type(<any>)`, which will return the type of `<any>`}@}. Note that the return type is {@{a special type called classes, which we will not go into detail here}@}. On Jupyter, {@{without using `print` (i.e. placing `type(<any>)` as the last expression), it will simply print out the type name, e.g. `float`, `int`, etc.}@} In most other situations, including {@{evaluating `type(<any>)` in your local Python installation instead of Jupyter}@}, it will {@{print out `<class '<type>'>`, with `<type>` replaced by the type name, e.g. `<class 'float'>`, `<class 'int'>`, etc.}@} <!--SR:!2025-08-29,277,342!2025-10-28,325,342!2025-07-12,234,322!2025-05-14,187,322!2025-08-30,276,330-->

### data type conversion

We can convert a value (`value`) into other data types using {@{`float(value)`, `int(value)`, and `str(value)`}@}. If {@{the data type of `value` and the resulting data type are the same}@}, {@{the same value is simply returned}@}. Note that not all {@{conversions are valid, and will throw a `ValueError` if it is invalid}@}. <!--SR:!2026-04-12,458,380!2026-05-07,479,380!2025-10-04,303,360!2025-09-14,288,360-->

- `bool(value)` ::@:: Converts `value` to a `bool`. If it is an `int` or `float`, converts to `True` unless `value` is zero, i.e. `value == 0`. If it is a `str` or `list`, converts to `True` unless `value` is empty, i.e. `value == ""` or `value == []`. There are also many other situations where `value` returns `True` unless `value` satisfies something, which will be unmentioned here. It is very difficult to get a `TypeError` or `ValueError` from this conversion, but possible with some very special types that will not be mentioned here. For exams, please use more explicit operations instead of this conversion, e.g. `len(list) == 0` instead of `not list`. <!--SR:!2025-10-01,272,366!2025-11-15,329,386-->
- `float(value)` ::@:: Converts `value` to a `float`. If it is an `int`, the same value but in `float` is returned. If it is a `str`, it removes whitespaces (spaces) surrounding the string and then parse it as a `float`, and raises a `ValueError` if it is invalid, e.g. an empty string, the string `.` (but not `0.`, `.0`, etc.), contains alphabets (except for `e` as used in exponential notation, e.g. `1e+100` and `1.2e-100` are valid), etc. (But `float("1.")`, `float(".1")`, `float("  4.2  ")`, etc. are valid. In general, if the string is a valid `float` when treated as Python code, the string is valid.) <!--SR:!2025-06-16,211,340!2026-02-22,392,320-->
- `int(value)` ::@:: Converts `value` to a `int`. If it is an `float`, the numbers behind the decimal point `.` is removed and then the rest is returned as an `int`. If it is a `str`, it removes whitespaces (spaces) surrounding the string and then parse it as a `int`, and raises a `ValueError` if it is invalid, e.g. an empty string, contains a decimal point `.`, contains alphabets, etc. (But `int("  4  ")` is valid. In general, if the string is a valid `int` when treated as Python code, the string is valid.) <!--SR:!2025-05-09,184,340!2025-09-14,288,360-->
- `list(value)` ::@:: Converts `value` to a `list`. If it is a `str`, then the resulting list consists of its individual characters (but note each individual character is still a `str`). If it is a `range(n)`, then the resulting list consists of `int`s from `0` (inclusive) to `n - 1` (inclusive). There are some other valid conversions not mentioned here. If the conversion is invalid (e.g. `value` is `int`), then it raises a `TypeError`. <br/> additional information: Technically speaking, if `value` is _iterable_, then the resulting list consists of elements of that iterable. Otherwise, it raises a `TypeError`. <!--SR:!2025-10-18,305,386!2025-07-10,219,366-->
- `str(value)` ::@:: Converts `value` to a `str`. (Almost) anything can be converted into a `str`. The resulting string is the same as that outputted by `print(value)`. <!--SR:!2025-07-09,218,340!2026-03-04,430,380-->

## input

We can request user input {@{using `input(prompt)`, where `prompt` is an (optional) value (not necessarily a `str`) to be printed (like `print(...)`, but without automatically printing a newline and only accepts a single argument) before asking for input}@}. Note that some Juypter notebooks {@{automatically adds a space after printing the string, while other environments do not}@}. The user input ends when {@{user enters a newline to confirm the input, i.e. presses enter}@}. Then, it will {@{return a string, keeping any leading or trailing spaces, but not the newline the user typed at the end to confirm the input}@}. <!--SR:!2026-05-28,478,340!2025-09-21,294,360!2025-10-08,301,360!2025-11-01,328,360-->
