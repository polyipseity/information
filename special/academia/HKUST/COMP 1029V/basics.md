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

Before using a variable, it needs to be {{declared using the keyword `Dim` first}}. The syntax is {{`Dim VariableName As Type`}}. You can also declare multiple variables in one line, like {{`Dim VariableName1 As Type1, VariableName2 As Type2`}}. <!--SR:!2025-01-19,271,330!2024-10-20,186,310!2026-06-22,651,330-->

To assign variables, use {{the equals operator `=`, like `Variable = Value`}}. For object types (basically anything that are not simple types like numbers, strings, booleans), you need to {{prepend `Set` before the variable as well, like `Set ObjectVariable = Value`}}. <!--SR:!2025-02-22,295,330!2025-12-29,476,310-->

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

- _(begin)_→:::←`Boolean` <!--SR:!2025-04-08,334,345!2024-12-29,254,330-->
- `Boolean`→:::←`Double` <!--SR:!2025-01-19,272,330!2025-02-24,300,330-->
- `Double`→:::←`Integer` <!--SR:!2024-10-16,132,310!2024-11-08,199,310-->
- `Integer`→:::←`Long` <!--SR:!2025-07-31,359,290!2024-12-25,233,325-->
- `Long`→:::←`Single` <!--SR:!2025-08-03,313,305!2024-12-24,232,325-->
- `Single`→:::←_(end)_ <!--SR:!2024-12-28,253,330!2025-02-25,299,330-->

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-03-07T00:04:17.302448+08:00. Any edits will be overridden! -->

- `Boolean`::Either `True` or `False`. <!--SR:!2025-01-17,270,330-->
- `Double`::A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. <!--SR:!2024-10-17,182,310-->
- `Integer`::An integer from -2<sup>15</sup> = -32768 to 2<sup>15</sup>-1 = 32767. <!--SR:!2025-03-28,326,345-->
- `Long`::An integer from -2<sup>31</sup> = -2147483648 to 2<sup>31</sup>-1 = 2147483647. <!--SR:!2024-10-18,179,310-->
- `Single`::A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. <!--SR:!2024-12-17,225,310-->

<!--/pytextgen-->

One cannot usually assign a value of a type to a variable {{declared with a different type}}: <!--SR:!2024-11-04,194,310-->

```VB
Dim ADouble As Double, AnObject As Object
Set AnObject = 3.14 ' runtime error
ADouble = Range("A1") ' runtime error
ADouble = 3.14 ' okay
```

In some circumstances, the value can be {{implicitly converted to the type of the variable, though sometimes with loss of data}}: <!--SR:!2025-01-04,240,325-->

```VB
Dim ALong as Long
ALong = 2.5 ' `ALong` is rounded to 2 as VBA uses banker's rounding
```

## output

To output things, we can use {{a message box by calling `MsgBox message[, icon][, title]`}}. `message` refers to {{the message, `icon`, by default no icon, refers to icon shown next to the message, and `title`, by default `Microsoft Excel`, is the title}}. If you want to specify a optional argument that is after another optional argument that you do not want to specify, leave the argument blank, like {{`MsgBox "message", , "title"`}}. <!--SR:!2025-01-03,242,325!2025-09-29,408,305!2025-01-16,267,330-->

There are several icons. Some of them are {{`vbCritical`, `vbExclamation`, `vbInformation`, and `vbQuestion`}}. <!--SR:!2025-10-04,381,265-->

## input

To accept user input, we can use {{an input box by calling `Input = InputBox(prompt[, title][, default])`}}. `prompt` refers to {{the message, `title`, by default `Microsoft Excel`, is the title, and `default`, by default empty, is the initial value in the input box. The user input is assigned to the variable `Input`}}. Similar to [output](#output), you can skip optional arguments by {{leaving it blank}}. <!--SR:!2024-12-22,212,290!2025-01-09,245,325!2024-11-05,211,330-->

## parentheses

When calling subroutines or functions, sometimes we {{use parentheses `()`, sometimes we do not}}. We only use parentheses when {{we need to use the output of the called function, otherwise we do not}}. As subroutines have no output, {{calling them never needs parentheses}}. The only exception is when you need to {{use the output of a function providing no arguments (so includes having optional arguments only), then having parentheses or not are both okay}}. <!--SR:!2026-09-20,720,330!2026-06-26,655,330!2026-01-02,479,310!2026-01-18,481,305-->
