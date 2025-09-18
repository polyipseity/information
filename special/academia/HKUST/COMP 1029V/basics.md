---
aliases:
  - VBA basic
  - VBA basics
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/basics
  - language/in/English
---

# VBA basics

```Python
# pytextgen generate module
# import ../../../../../tools/utility.py.md
```

## variable

Before using a variable, it needs to be {@{declared using the keyword `Dim` first}@}. The syntax is {@{`Dim VariableName As Type`}@}. You can also declare multiple variables in one line, like {@{`Dim VariableName1 As Type1, VariableName2 As Type2`}@}.

To assign variables, use {@{the equals operator `=`, like `Variable = Value`}@}. For object types (basically anything that are not simple types like numbers, strings, booleans), you need to {@{prepend `Set` before the variable as well, like `Set ObjectVariable = Value`}@}.

## types

Below are common data types:

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "type", "description"
table = (
  ("`Boolean`", "Either `True` or `False`."),
  ("`Double`", "A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes.",),
  ("`Integer`", "An integer from -2<sup>15</sup> = -32768 to 2<sup>15</sup>-1 = 32767.",),
  ("`Long`", "An integer from -2<sup>31</sup> = -2147483648 to 2<sup>31</sup>-1 = 2147483647.",),
  ("`Single`", "A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes.",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("2f02", "652a",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "3b1a", None,),
    items_to_map(*table),
  )
))
```

<!--pytextgen generate section="2f02"--><!-- The following content is generated at 2024-03-07T00:04:17.315438+08:00. Any edits will be overridden! -->

> | type | description |
> |-|-|
> | `Boolean` | Either `True` or `False`. |
> | `Double` | A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. |
> | `Integer` | An integer from -2<sup>15</sup> = -32768 to 2<sup>15</sup>-1 = 32767. |
> | `Long` | An integer from -2<sup>31</sup> = -2147483648 to 2<sup>31</sup>-1 = 2147483647. |
> | `Single` | A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. |

<!--/pytextgen-->

<!--pytextgen generate section="652a"--><!-- The following content is generated at 2024-03-07T00:04:17.291438+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←`Boolean`
- `Boolean`→::@::←`Double`
- `Double`→::@::←`Integer`
- `Integer`→::@::←`Long`
- `Long`→::@::←`Single`
- `Single`→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-03-07T00:04:17.302448+08:00. Any edits will be overridden! -->

- `Boolean`:@:Either `True` or `False`.
- `Double`:@:A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes.
- `Integer`:@:An integer from -2<sup>15</sup> = -32768 to 2<sup>15</sup>-1 = 32767.
- `Long`:@:An integer from -2<sup>31</sup> = -2147483648 to 2<sup>31</sup>-1 = 2147483647.
- `Single`:@:A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes.

<!--/pytextgen-->

One cannot usually assign a value of a type to a variable {@{declared with a different type}@}:

```VB
Dim ADouble As Double, AnObject As Object
Set AnObject = 3.14 ' runtime error
ADouble = Range("A1") ' runtime error
ADouble = 3.14 ' okay
```

In some circumstances, the value can be {@{implicitly converted to the type of the variable, though sometimes with loss of data}@}:

```VB
Dim ALong as Long
ALong = 2.5 ' `ALong` is rounded to 2 as VBA uses banker's rounding
```

## output

To output things, we can use {@{a message box by calling `MsgBox message[, icon][, title]`}@}. `message` refers to {@{the message}@}, `icon`, by default {@{no icon, refers to icon shown next to the message}@}, and `title`, by default {@{`Microsoft Excel`, is the title}@}. If you want to {@{specify a optional argument}@} that is after {@{another optional argument that you do not want to specify}@}, {@{leave the argument blank}@}, like {@{`MsgBox "message", , "title"`}@}.

There are several icons. Some of them are {@{`vbCritical`, `vbExclamation`, `vbInformation`, and `vbQuestion`}@}.

## input

To accept user input, we can use {@{an input box by calling `Input = InputBox(prompt[, title][, default])`}@}. `prompt` refers to {@{the message, `title`, by default `Microsoft Excel`, is the title, and `default`, by default empty, is the initial value in the input box. The user input is assigned to the variable `Input`}@}. Similar to [output](#output), you can skip optional arguments by {@{leaving it blank}@}.

## parentheses

When calling subroutines or functions, sometimes we {@{use parentheses `()`, sometimes we do not}@}. We only use parentheses when {@{we need to use the output of the called function, otherwise we do not}@}. As subroutines have no output, {@{calling them never needs parentheses}@}. The only exception is when you need to {@{use the output of a function providing no arguments (so includes having optional arguments only), then having parentheses or not are both okay}@}.
