---
aliases:
  - Java basic
  - Java basics
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/basics
  - language/in/English
---

# Java basics

```Python
# pytextgen generate module
# import ../../../../../tools/utility.py.md
```

## basics

- comment :: A comment is either enclosed by `/*` and `*/` like `/* example */` or starts with `//` like `// example`. For the first one, the comment ends when the `*/` is first encountered. For the second one, the comment ends when the line ends. <!--SR:!2025-01-01,258,330-->
- package :: Packages are analogous to directories. The differences are that package names are more restricted and each package component is separated by `.` instead of `/`. One imports all the Java files in a package by `import a.package.*;`. More commonly, one imports a Java file, say `Example.java` in a package by `import a.package.Example;`. <!--SR:!2024-10-18,182,310-->
- spacing :: Java ignores whitespace in most places. Whitespace are not ignored in some places, such as in strings `"This string has a space."` or before the names of method calls `. thisIsInvalidJavaCode()`. Usually whitespace are added before statements systematically, with more spaces per level of code block `{ /* code block */ }`. This is called indentation. <!--SR:!2024-08-05,122,290-->
- statement :: A Java program is a collection of statements. A statement can be multiline and ends with a semicolon `;`. A statement can also be a code block `{ /* code block */ }`, which is also a collection of statements itself. <!--SR:!2024-12-15,225,310-->

## variable

To assign a value or the result of an expression to a variable, use {{`=`}}: <!--SR:!2024-12-31,256,330-->

```Java
variableName = 1 + 2;
```

One must {{declare a variable, prefixed with the type of the variable, i.e. what the variable can hold}}, before assigning things to it. Optionally, {{one can declare a variable and assign to it}} simultaneously: <!--SR:!2024-09-15,160,310!2025-01-28,281,330-->

```Java
int anIntegerVariable; // `int` means the variable can hold integers
anIntegerVariable = 1 + 2;
String aStringVariable = "a string"; // variables can be declared and assigned simultaneously
```

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}}. <!--SR:!2024-11-10,201,310-->

## types

Below are common data types:

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "type", "description"
table = (
  ("`String`", "A piece of text. Example: `\"Hello\"`",),
  ("`boolean`", "Either true or false. Example: `true`, `false`",),
  ("`char`", "A single character. Example: `'a'`, `'3'`, `' '`",),
  ("`double`", "A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14`",),
  ("`float`", "A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F`",),
  ("`int`", "An integer. Example: `42`",),
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

<!--pytextgen generate section="2f02"--><!-- The following content is generated at 2024-02-01T11:50:25.897878+08:00. Any edits will be overridden! -->

> | type | description |
> |-|-|
> | `String` | A piece of text. Example: `"Hello"` |
> | `boolean` | Either true or false. Example: `true`, `false` |
> | `char` | A single character. Example: `'a'`, `'3'`, `' '` |
> | `double` | A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` |
> | `float` | A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` |
> | `int` | An integer. Example: `42` |

<!--/pytextgen-->

<!--pytextgen generate section="652a"--><!-- The following content is generated at 2024-01-29T08:31:35.198780+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`String` <!--SR:!2025-01-20,275,330!2024-11-08,214,330-->
- `String`→:::←`boolean` <!--SR:!2024-10-07,175,310!2025-01-14,269,330-->
- `boolean`→:::←`char` <!--SR:!2025-02-03,281,330!2025-02-21,296,330-->
- `char`→:::←`double` <!--SR:!2024-08-10,127,290!2024-10-28,189,310-->
- `double`→:::←`float` <!--SR:!2024-08-03,120,290!2024-09-24,166,310-->
- `float`→:::←`int` <!--SR:!2024-07-14,100,290!2024-11-28,212,310-->
- `int`→:::←_(end)_ <!--SR:!2025-01-06,264,330!2024-09-09,154,310-->

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-02-01T11:50:25.871864+08:00. Any edits will be overridden! -->

- `String`::A piece of text. Example: `"Hello"` <!--SR:!2024-12-22,249,330-->
- `boolean`::Either true or false. Example: `true`, `false` <!--SR:!2024-12-11,240,330-->
- `char`::A single character. Example: `'a'`, `'3'`, `' '` <!--SR:!2025-02-12,290,330-->
- `double`::A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` <!--SR:!2024-10-09,177,310-->
- `float`::A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` <!--SR:!2024-10-16,183,310-->
- `int`::An integer. Example: `42` <!--SR:!2024-12-03,235,330-->

<!--/pytextgen-->

### conversion

One cannot usually assign a value of a type to a variable {{declared with a different type}}: <!--SR:!2024-10-05,173,310-->

```Java
int anInteger = 3.14; // compilation error
float aFloat = 3.14; // compilation error
double aDouble = 3.14; // okay
```

In some circumstances, the value can be {{implicitly converted to the type of the variable, since there is no loss of data}}: <!--SR:!2024-08-27,144,310-->

```Java
float aFloat = 3; // the `int` of value 3 is implicitly converted into a `float` of value 3
assert aFloat == 3;
```

If implicit conversion is disallowed, one can also {{explicitly convert the value to the type of the variable, but with loss of data}}: <!--SR:!2025-02-13,291,330-->

```Java
int anInteger = (int) -3.14; // the `double` of value -3.14 is explicitly converted into an `int` of value 3
assert anInteger == 3;
```

The above explicit conversion is called {{casting. A value can be casted to any type without any compilation error. However, only casting that makes sense will not result in a runtime error}}: <!--SR:!2024-09-10,158,310-->

```Java
int anInteger = (int) -3.14; // no compilation error and runtime error
assert anInteger == 3;
int anInteger2 = (int) "-3.14"; // no compilation error; but a runtime error when you run it
```

## operators

The assignment operator {{assigns a value to a variable}}: <!--SR:!2024-12-30,255,330-->

```Java
theAnswerToLifeTheUniverseAndEverything = 42
```

### arithmetic operators

Below are common arithmetic operators. Operators have higher precedence than or same precedence as operators below it in the list:

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`++`", "increment a numerical variable by 1",),
  ("`--`", "decrement a numerical variable by 1",),
  ("`*`", "multiplication",),
  ("`/`", "division; if both operands are of integral types, then round-towards-zero division",),
  ("`%`", "remainder; the resulting sign is the same as the dividend, i.e. the number before the operator",),
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

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-01-30T13:35:46.604804+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `++` | increment a numerical variable by 1 |
> | `--` | decrement a numerical variable by 1 |
> | `*` | multiplication |
> | `/` | division; if both operands are of integral types, then round-towards-zero division |
> | `%` | remainder; the resulting sign is the same as the dividend, i.e. the number before the operator |
> | `+` | addition |
> | `-` | subtraction |

<!--/pytextgen-->

<!--pytextgen generate section="f21a"--><!-- The following content is generated at 2024-01-30T13:35:46.620801+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`++` <!--SR:!2025-03-17,318,330!2025-02-23,299,330-->
- `++`→:::←`--` <!--SR:!2025-01-21,274,330!2025-01-30,277,330-->
- `--`→:::←`*` <!--SR:!2025-02-18,253,310!2024-09-26,174,310-->
- `*`→:::←`/` <!--SR:!2024-10-13,181,310!2024-12-22,251,330-->
- `/`→:::←`%` <!--SR:!2025-01-17,270,330!2024-07-20,106,290-->
- `%`→:::←`+` <!--SR:!2025-03-14,314,330!2024-08-04,121,290-->
- `+`→:::←`-` <!--SR:!2025-02-10,288,330!2025-02-04,282,330-->
- `-`→:::←_(end)_ <!--SR:!2024-11-03,209,330!2025-01-29,281,330-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- `++`::increment a numerical variable by 1 <!--SR:!2024-11-07,213,330-->
- `--`::decrement a numerical variable by 1 <!--SR:!2025-03-15,316,330-->
- `*`::multiplication <!--SR:!2025-03-01,303,330-->
- `/`::division; if both operands are of integral types, then round-towards-zero division <!--SR:!2024-08-04,121,290-->
- `%`::remainder; the resulting sign is the same as the dividend, i.e. the number before the operator <!--SR:!2024-07-26,112,290-->
- `+`::addition <!--SR:!2025-01-19,272,330-->
- `-`::subtraction <!--SR:!2025-01-03,256,330-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {{a `boolean` value}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2025-01-30,283,330-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`<`", "lesser than",),
  ("`>`", "greater than",),
  ("`<=`", "lesser than or equal to",),
  ("`>=`", "greater than or equal to",),
  ("`==`", "equal to",),
  ("`!=`", "not equal to",),
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

<!--pytextgen generate section="bd23"--><!-- The following content is generated at 2024-01-30T13:35:46.668328+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `<` | lesser than |
> | `>` | greater than |
> | `<=` | lesser than or equal to |
> | `>=` | greater than or equal to |
> | `==` | equal to |
> | `!=` | not equal to |

<!--/pytextgen-->

<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-01-30T13:35:46.651317+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`<` <!--SR:!2024-07-11,50,190!2025-01-07,239,310-->
- `<`→:::←`>` <!--SR:!2025-02-17,296,330!2025-01-28,275,330-->
- `>`→:::←`<=` <!--SR:!2024-09-28,166,310!2024-11-27,210,290-->
- `<=`→:::←`>=` <!--SR:!2024-10-12,179,310!2024-07-06,106,290-->
- `>=`→:::←`==` <!--SR:!2024-10-13,132,310!2024-07-05,18,150-->
- `==`→:::←`!=` <!--SR:!2025-01-27,279,330!2024-10-16,139,310-->
- `!=`→:::←_(end)_ <!--SR:!2025-01-29,280,330!2025-03-02,304,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.690328+08:00. Any edits will be overridden! -->

- `<`::lesser than <!--SR:!2024-12-02,234,330-->
- `>`::greater than <!--SR:!2024-12-29,255,330-->
- `<=`::lesser than or equal to <!--SR:!2024-11-27,212,310-->
- `>=`::greater than or equal to <!--SR:!2025-01-23,276,330-->
- `==`::equal to <!--SR:!2025-02-01,279,330-->
- `!=`::not equal to <!--SR:!2024-11-24,228,330-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}. <!--SR:!2024-12-08,237,330-->

Also, one cannot chain {{comparison operators, like `2 <= aNumber <= 5`. [logic operators](#logic%20operators) are needed instead, like `2 <= aNumber && aNumber <= 5`}}. <!--SR:!2024-10-27,190,310-->

### logic operators

Below are common logic operators, all of which {{accept two booleans and return a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-09-23,165,310-->

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "operator", "description"
table = (
  ("`!`", "negate",),
  ("`&&`", "and",),
  ("<code>&#124;&#124;</code>", "or",),
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

<!--pytextgen generate section="2856"--><!-- The following content is generated at 2024-02-20T14:26:41.018968+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `!` | negate |
> | `&&` | and |
> | <code>&#124;&#124;</code> | or |

<!--/pytextgen-->

<!--pytextgen generate section="d882"--><!-- The following content is generated at 2024-02-20T14:26:40.998968+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`!` <!--SR:!2025-01-18,273,330!2024-07-29,133,310-->
- `!`→:::←`&&` <!--SR:!2024-11-15,205,310!2024-10-14,181,310-->
- `&&`→:::←<code>&#124;&#124;</code> <!--SR:!2025-01-24,277,330!2025-01-12,267,330-->
- <code>&#124;&#124;</code>→:::←_(end)_ <!--SR:!2024-12-06,238,330!2024-09-02,150,310-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-20T14:26:41.011968+08:00. Any edits will be overridden! -->

- `!`::negate <!--SR:!2024-11-17,221,330-->
- `&&`::and <!--SR:!2024-12-21,245,330-->
- <code>&#124;&#124;</code>::or <!--SR:!2024-10-11,179,310-->

<!--/pytextgen-->
