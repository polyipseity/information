---
aliases:
  - Java basic
  - Java basics
tags:
  - flashcards/special/academic/HKUST/COMP_1029J/basics
  - languages/in/English
---

# Java basics

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../tools/utility.py.md
```

%%

## basics

- comment :: A comment is either enclosed by `/*` and `*/` like `/* example */` or starts with `//` like `// example`. For the first one, the comment ends when the `*/` is first encountered. For the second one, the comment ends when the line ends.
- package :: Packages are analogous to directories. The differences are that package names are more restricted and each package component is separated by `.` instead of `/`. One imports all the Java files in a package by `import a.package.*;`. More commonly, one imports a Java file, say `Example.java` in a package by `import a.package.Example;`.
- spacing :: Java ignores whitespace in most places. Whitespace are not ignored in some places, such as in strings `"This string has a space."` or before the names of method calls `. thisIsInvalidJavaCode()`. Usually whitespace are added before statements systematically, with more spaces per level of code block `{ /* code block */ }`. This is called indentation.
- statement :: A Java program is a collection of statements. A statement can be multiline and ends with a semicolon `;`. A statement can also be a code block `{ /* code block */ }`, which is also a collection of statements itself.
- variable :: Variable names are case sensitive, cannot have some characters like spaces, and cannot begin with some characters like numbers.

## variables

To assign a value or the result of an expression to a variable, use {{`=`}}:

```Java
variableName = 1 + 2;
```

One must {{declare a variable, prefixed with the type of the variable, i.e. what the variable can hold}}, before assigning things to it. Optionally, {{one can declare a variable and assign to it}} simultaneously:

```Java
int anIntegerVariable; // `int` means the variable can hold integers
anIntegerVariable = 1 + 2;
String aStringVariable = "a string"; // variables can be declared and assigned simultaneously
```

## types

Below are common data types:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "type", "description"
table = (
  ("`String`", "A piece of text. Example: `\"Hello\"`",),
  ("`boolean`", "Either true or false. Example: `true`, `false`",),
  ("`char`", "A single character. Example: `'a'`, `'3'`, `' '`",),
  ("`double`", "A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14`, `6.29d`, `3.12D`, `5.`",),
  ("`float`", "A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14f`, `9.20F`, `1.f`",),
  ("`int`", "An integer. Example: `42`",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    e.cwf_sects("2f02", "652a",),
    headers,
    table,
  ),
  memorize_map(
    e.cwf_sects(None, "3b1a", None,),
    items_to_map(*table),
  )
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2f02"--><!-- The following content is generated at 2024-01-29T08:31:35.212812+08:00. Any edits will be overridden! -->

> | type | description |
> |-|-|
> | `String` | A piece of text. Example: `"Hello"` |
> | `boolean` | Either true or false. Example: `true`, `false` |
> | `char` | A single character. Example: `'a'`, `'3'`, `' '` |
> | `double` | A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14`, `6.29d`, `3.12D`, `5.` |
> | `float` | A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14f`, `9.20F`, `1.f` |
> | `int` | An integer. Example: `42` |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="652a"--><!-- The following content is generated at 2024-01-29T08:31:35.198780+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`String`
- `String`→:::←`boolean`
- `boolean`→:::←`char`
- `char`→:::←`double`
- `double`→:::←`float`
- `float`→:::←`int`
- `int`→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3b1a"--><!-- The following content is generated at 2024-01-29T08:24:20.610949+08:00. Any edits will be overridden! -->

- `String`::A piece of text. Example: `"Hello"`
- `boolean`::Either true or false. Example: `true`, `false`
- `char`::A single character. Example: `'a'`, `'3'`, `' '`
- `double`::A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14`, `6.29d`, `3.12D`, `5.`
- `float`::A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `3.14f`, `9.20F`, `1.f`
- `int`::An integer. Example: `42`

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

One cannot usually assign a value of a type to a variable {{declared with a different type}}:

```Java
int anInteger = 3.14; // compilation error
float aFloat = 3.14; // compilation error
double aDouble = 3.14; // okay
```

In some circumstances, the value can be {{implicitly converted to the type of the variable, since there is no loss of data}}:

```Java
float aFloat = 3; // the `int` of value 3 is implicitly converted into a `float` of value 3
assert aFloat == 3;
```

One can also {{explicitly convert the value to the type of the variable, but with loss of data}}:

```Java
int anInteger = (int) -3.14; // the `double` of value -3.14 is explicitly converted into an `int` of value 3
assert anInteger == 3;
```

The above explicit conversion is called {{casting. A value can be casted to any type without any compilation error. However, only casting that makes sense will not result in a runtime error}}:

```Java
int anInteger = (int) -3.14; // no compilation error and runtime error
assert anInteger == 3;
int anInteger2 = (int) "-3.14"; // no compilation error; but a runtime error when you run it
```

## operators

The assignment operator {{assigns a value to a variable}}:

```Java
theAnswerToLifeTheUniverseAndEverything = 42
```

### arithmetic operators

Below are common arithmetic operators:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "operator", "description"
table = (
  ("`+`", "addition",),
  ("`-`", "subtraction",),
  ("`*`", "multiplication",),
  ("`/`", "division; if both operands are of integral types, then round-to-zero division",),
  ("`%`", "remainder; the resulting sign is the same as the dividend, i.e. the number before the operator",),
  ("`++`", "increment a numerical variable by 1",),
  ("`--`", "decrement a numerical variable by 1",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93ab"--><!-- The following content is generated at 2024-01-29T09:43:58.585505+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `+` | addition |
> | `-` | subtraction |
> | `*` | multiplication |
> | `/` | division; if both operands are of integral types, then round-to-zero division |
> | `%` | remainder; the resulting sign is the same as the dividend, i.e. the number before the operator |
> | `++` | increment a numerical variable by 1 |
> | `--` | decrement a numerical variable by 1 |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f21a"--><!-- The following content is generated at 2024-01-29T08:48:00.329385+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`+`
- `+`→:::←`-`
- `-`→:::←`*`
- `*`→:::←`/`
- `/`→:::←`%`
- `%`→:::←`++`
- `++`→:::←`--`
- `--`→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9cda"--><!-- The following content is generated at 2024-01-29T09:43:57.655354+08:00. Any edits will be overridden! -->

- `+`::addition
- `-`::subtraction
- `*`::multiplication
- `/`::division; if both operands are of integral types, then round-to-zero division
- `%`::remainder; the resulting sign is the same as the dividend, i.e. the number before the operator
- `++`::increment a numerical variable by 1
- `--`::decrement a numerical variable by 1

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### comparison operators

Below are common comparison operators, all of which returns {{a `boolean` value}}:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "operator", "description"
table = (
  ("`==`", "equal to",),
  ("`!=`", "not equal to",),
  ("`>`", "greater than",),
  ("`<`", "lesser than",),
  ("`>=`", "greater than or equal to",),
  ("`<=`", "lesser than or equal to",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bd23"--><!-- The following content is generated at 2024-01-29T09:03:17.952034+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `==` | equal to |
> | `!=` | not equal to |
> | `>` | greater than |
> | `<` | lesser than |
> | `>=` | greater than or equal to |
> | `<=` | lesser than or equal to |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d123"--><!-- The following content is generated at 2024-01-29T09:03:17.885672+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`==`
- `==`→:::←`!=`
- `!=`→:::←`>`
- `>`→:::←`<`
- `<`→:::←`>=`
- `>=`→:::←`<=`
- `<=`→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cc23"--><!-- The following content is generated at 2024-01-29T09:03:17.844640+08:00. Any edits will be overridden! -->

- `==`::equal to
- `!=`::not equal to
- `>`::greater than
- `<`::lesser than
- `>=`::greater than or equal to
- `<=`::lesser than or equal to

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}.

Also, one cannot chain {{comparison operators, like `2 <= aNumber <= 5`. [Conditional operators](#conditional%20operators) are needed instead, like `2 <= aNumber && aNumber <= 5`}}.

### conditional operators

Below are common conditional operators, all of which {{accept two booleans and return a boolean}}:

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "operator", "description"
table = (
  ("`&&`", "and",),
  ("`||`", "or",),
  ("`!`", "negate",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2856"--><!-- The following content is generated at 2024-01-29T09:32:57.652827+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `&&` | and |
> | `\|\|` | or |
> | `!` | negate |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d882"--><!-- The following content is generated at 2024-01-29T09:21:35.430345+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`&&`
- `&&`→:::←`||`
- `||`→:::←`!`
- `!`→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee13"--><!-- The following content is generated at 2024-01-29T09:21:36.360650+08:00. Any edits will be overridden! -->

- `&&`::and
- `||`::or
- `!`::negate

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
