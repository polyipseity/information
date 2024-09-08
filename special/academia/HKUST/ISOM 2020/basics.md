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

## arithmetic operators

Below are common arithmetic operators. Brackets have {{the highest precedence (very intuitive)}}. Operators have higher precedence than or same precedence as operators below it in the list:

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

- _(begin)_→:::←`**`
- `**`→:::←`*`
- `*`→:::←`/`
- `/`→:::←`//`
- `//`→:::←`%`
- `%`→:::←`+`
- `+`→:::←`-`
- `-`→:::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.549289+08:00. Any edits will be overridden! -->

- `**`::power
- `*`::multiplication
- `/`::division
- `//`::floor division
- `%`::remainder; the resulting sign is the same as the divider, i.e. the number after the operator
- `+`::addition
- `-`::subtraction

<!--/pytextgen-->

For the return type of operators, all of above (if only `float` and `int` are considered), with two exceptions, {{returns `int` (integer) if both operands are `int`, and `float` otherwise}}. The two exceptions are {{that `/` (division) always return `float`, even if both operands are `int`}}, and {{applying `**` (power) on a negative base results in a `complex` (complex number) but not an error, which is not discussed here}}.

A note regarding accuracy is that {{there may be some inaccuracies involved when `float`s are involved, such as `0.1 + 0.2` is `0.30000000000000004` instead of `0.3`}}. Also, regarding zeros, {{`0.0` and `-0.0` are technically different `float`s, but they are equivalent for most purposes and even compare the same, i.e. `0.0 == -0.0` is `True`}}. Finally, a notable error (raising an error causes {{the program to stop and print out error messages}}) is that {{`/` (division), `//` (floor division), and `%` (remainder) raises `ZeroDivisionError` if the second operand is zero}}. However, `0 ** 0` (power) {{returns `1` instead of being undefined or raising an error}}.

## mathematics

- `abs(<int/float>)` ::: Returns the absolute value of the first argument. The return type is the same as the input type. (Note that the two `float`s, `-0.0` and `0.0`, are technically different, and `abs` turns both of them into `0.0`.)
- `round(<int/float>[, <int/None> = None])` ::: Round the first argument to the number of decimal places specified by the 2nd argument (if unspecified, `None`). Tie-breaking rounds to even numbers (for Python 3; Python 2 is round away from zero), so `round(0.5)` is `0` but `round(1.5)` is `2`. For the 2nd argument, negative values are possible, and `None` is the same (except for return types) as `0`. The return type is always the same as the input type, except if the first argument is `float` and the 2nd argument is `None` at the same time, then the return type is `int`.
- `math.sqrt(<int/float>)` ::: Requires importing `math` first by `import math`. Returns the square root of the provided number. Always output a `float`. The differences from `<int/float> ** 0.5` are that `sqrt` does not accept negative (raises a `ValueError` error) or complex numbers (raises a `TypeError` error), and the number provided to `sqrt` is always converted into a `float` first before applying square root on it.

## output

In {{a Jupyter notebook}}, it outputs {{the value of the last expression (and prints nothing if the last expression is `None`)}}. Note that {{assignments are not expressions, and do not produce output as the last expression}}. To get it to print more things, {{use `print(<any>...)`}}. It can {{print anything (and prints `None` if the last expression is `None`)}}. Note that it automatically {{adds a newline after the printed content, so each `print` outputs on a new line instead of being glued together in a single line}}. Also, when multiple arguments are passed, {{each argument is joined into a single string, separated by a space in between}}. When {{no arguments are passed, only a newline is printed}}.

To define a string in Python, {{enclose the string in either double quotes `"example"` or single quotes `'example'`. Both are equivalent except that you need to escape double quotes in the strings for the first one and single quotes for the second one}}. Note that the enclosing quotes are {{not part of the string}}. To escape a character, {{precede the character with a backslash `\`, like `"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}}. Note that you cannot {{add literal new lines inside a string if you use the above format}}. Instead, you need to {{use `\n` to represent newlines}}. However, you can {{add literal new lines you enclose the strings in 3 double quotes `"""example"""` or 3 single quotes `'''example'''`}}. Additionally with this format, {{you only need to escape quotes if there are 3 consecutive quotes of the same type as the enclosing quotes}}.

## variable

To {{assign a value or the result of an expression to a variable}}, use {{`=`}}:

```Python
variableName = 1 + 2
```

One does not need to {{declare the variable and its type before assigning to it}}. Reassigning the variable (i.e. {{replacing the variable value}}) uses {{the same syntax as above}}. To {{use the value of a variable}}, {{simply write the variable name}}.

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces (but underscores `_` are okay), and cannot begin with some characters like numbers}}. Also, while allowed, it is recommended to {{not use builtin names, e.g. `print`, as we will no longer be able to use those builtin functions of variables later (replaced by us)}}.

Variable name should be {{descriptive of the values it is supposed to hold}}.

## data types

Below are common data types:

- `NoneType` :: The type for the `None` value.
- `bool` :: A boolean, which is either `True` or `False`. Note that `bool`s are also `int`s. In particular, `True == 1` and `False == 0`, and can be used in arithmetic operators.
- `float` :: A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. `float` can hold integers as well, with only the internal representation being different from `int`. Example: `1.`, `3.14`, `9.20`.
- `int` :: An integer. Example: `42`.
- `str` :: A piece of text. Example: `"Hello"`.

Some interesting facts about `float`s:  `print` {{always output at least 1 decimal place for `float`s, and outputs at most as many digits as needed to represent the number exactly}}. `1` {{is an `int` while `1.` and `1.0` are `float`s representing the same value `1`}}.

To get the type of a value, {{use `type(<any>)`, which will return the type of `<any>`}}. Note that the return type is {{a special type called classes, which we will not go into detail here}}. On Jupyter, {{without using `print` (i.e. placing `type(<any>)` as the last expression), it will simply print out the type name, e.g. `float`, `int`, etc.}}. In most other situations, including {{evaluating `type(<any>)` in your local Python installation instead of Jupyter}}, it will {{print out `<class '<type>'>`, with `<type>` replaced by the type name, e.g. `<class 'float'>`, `<class 'int'>`, etc.}}
