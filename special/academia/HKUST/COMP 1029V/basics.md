---
aliases:
  - VBA basic
  - VBA basics
tags:
  - flashcard/special/academia/HKUST/COMP_1029V/basics
  - language/in/English
---

# VBA basics

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../tools/utility.py.md
```

%%

## variable

Before using a variable, it needs to be {{declared using the keyword `Dim` first}}. The syntax is {{`Dim VariableName As Type`}}. You can also declare multiple variables in one line, like {{`Dim VariableName1 As Type1, VariableName2 As Type2`}}. <!--SR:!2024-02-21,16,290!2024-04-17,58,310!2024-04-09,51,310-->

To assign variables, use {{the equals operator `=`, like `Variable = Value`}}. For object types (basically anything that are not simple like numbers, strings, booleans), you need to {{prepend `Set` before the variable as well, like `Set ObjectVariable = Value`}}. <!--SR:!2024-02-22,17,290!2024-04-07,49,310-->

## types

Below are common data types:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "type", "description"
table = (
  ("Boolean", "Either `True` or `False`."),
  ("Double", "A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes.",),
  ("Integer", "An integer from -2<sup>15</sup>=-32768 to 2<sup>15</sup>-1=32767.",),
  ("Long", "An integer from -2<sup>31</sup>=-2147483648 to 2<sup>31</sup>-1=2147483647.",),
  ("Single", "A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes.",),
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2f02"--><!-- The following content is generated at 2024-01-31T22:17:45.635102+08:00. Any edits will be overridden! -->

> | type | description |
> |-|-|
> | Boolean | Either `True` or `False`. |
> | Double | A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. |
> | Integer | An integer from -2<sup>15</sup>=-32768 to 2<sup>15</sup>-1=32767. |
> | Long | An integer from -2<sup>31</sup>=-2147483648 to 2<sup>31</sup>-1=2147483647. |
> | Single | A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="652a"--><!-- The following content is generated at 2024-01-31T22:17:45.602573+08:00. Any edits will be overridden! -->

- _(begin)_→:::←Boolean <!--SR:!2024-02-23,18,305!2024-04-19,60,310-->
- Boolean→:::←Double <!--SR:!2024-02-20,15,290!2024-02-22,17,290-->
- Double→:::←Integer <!--SR:!2024-02-22,17,290!2024-02-20,15,290-->
- Integer→:::←Long <!--SR:!2024-04-02,43,290!2024-02-23,18,305-->
- Long→:::←Single <!--SR:!2024-02-23,18,305!2024-02-23,18,305-->
- Single→:::←_(end)_ <!--SR:!2024-02-20,15,290!2024-02-22,17,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3b1a"--><!-- The following content is generated at 2024-01-31T22:17:45.587449+08:00. Any edits will be overridden! -->

- Boolean::Either `True` or `False`. <!--SR:!2024-02-21,16,290-->
- Double::A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. <!--SR:!2024-04-18,59,310-->
- Integer::An integer from -2<sup>15</sup>=-32768 to 2<sup>15</sup>-1=32767. <!--SR:!2024-02-23,18,305-->
- Long::An integer from -2<sup>31</sup>=-2147483648 to 2<sup>31</sup>-1=2147483647. <!--SR:!2024-02-21,16,290-->
- Single::A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. <!--SR:!2024-02-22,17,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

One cannot usually assign a value of a type to a variable {{declared with a different type}}: <!--SR:!2024-02-20,15,290-->

```VB
Dim ADouble As Double, AnObject As Object
Set AnObject = 3.14 ' runtime error
ADouble = Range("A1") ' runtime error
ADouble = 3.14 ' okay
```

In some circumstances, the value can be {{implicitly converted to the type of the variable, though sometimes with loss of data}}: <!--SR:!2024-02-23,18,305-->

```VB
Dim ALong as Long
ALong = 2.5 ' `ALong` is rounded to 2 as VBA uses banker's rounding
```

## output

To output things, we can use {{a message box by calling `MsgBox message[, icon][, title]`}}. `message` refers to {{the message, `icon`, by default no icon, refers to icon shown next to the message, and `title`, by default `Microsoft Excel`, is the title}}. If you want to specify a optional argument that is after another optional argument that you do not want to specify, leave the argument blank, like {{`MsgBox "message", , "title"`}}. <!--SR:!2024-02-23,18,305!2024-03-31,44,305!2024-02-21,16,290-->

There are several icons. Some of them are {{`vbCritical`, `vbExclamation`, `vbInformation`, and `vbQuestion`}}. <!--SR:!2024-03-04,20,265-->

## input

To accept user input, we can use {{an input box by calling `Input = InputBox(prompt[, title][, default])`}}. `prompt` refers to {{the message, `title`, by default `Microsoft Excel`, is the title, and `default`, by default empty, is the initial value in the input box. The user input is assigned to the variable `Input`}}. Similar to [output](#output), you can skip optional arguments by {{leaving it blank}}. <!--SR:!2024-03-10,25,290!2024-02-23,18,305!2024-04-07,49,310-->

## parentheses

When calling subroutines or functions, sometimes we {{use parentheses `()`, sometimes we do not}}. We only use parentheses when {{we need to use the output of the called function, otherwise we do not}}. As subroutines have no output, {{calling them never needs parentheses}}. The only exception is when you need to {{use the output of a function providing no arguments (so includes having optional arguments only), then having parentheses or not are both okay}}. <!--SR:!2024-04-14,55,310!2024-04-09,51,310!2024-04-07,49,310!2024-02-23,18,305-->
