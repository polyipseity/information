---
aliases:
  - Java basic
  - Java basics
tags:
  - flashcards/special/academia/HKUST/COMP_1029J/basics
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

- comment :: A comment is either enclosed by `/*` and `*/` like `/* example */` or starts with `//` like `// example`. For the first one, the comment ends when the `*/` is first encountered. For the second one, the comment ends when the line ends. <!--SR:!2024-02-18,14,290-->
- package :: Packages are analogous to directories. The differences are that package names are more restricted and each package component is separated by `.` instead of `/`. One imports all the Java files in a package by `import a.package.*;`. More commonly, one imports a Java file, say `Example.java` in a package by `import a.package.Example;`. <!--SR:!2024-02-19,15,290-->
- spacing :: Java ignores whitespace in most places. Whitespace are not ignored in some places, such as in strings `"This string has a space."` or before the names of method calls `. thisIsInvalidJavaCode()`. Usually whitespace are added before statements systematically, with more spaces per level of code block `{ /* code block */ }`. This is called indentation. <!--SR:!2024-03-29,41,290-->
- statement :: A Java program is a collection of statements. A statement can be multiline and ends with a semicolon `;`. A statement can also be a code block `{ /* code block */ }`, which is also a collection of statements itself. <!--SR:!2024-02-21,17,290-->

## variable

To assign a value or the result of an expression to a variable, use {{`=`}}: <!--SR:!2024-02-19,15,290-->

```Java
variableName = 1 + 2;
```

One must {{declare a variable, prefixed with the type of the variable, i.e. what the variable can hold}}, before assigning things to it. Alternatively, {{one can declare a variable and assign to it}} simultaneously: <!--SR:!2024-04-08,51,310!2024-02-19,15,290-->

```Java
int anIntegerVariable; // `int` means the variable can hold integers
anIntegerVariable = 1 + 2;
String aStringVariable = "a string"; // variables can be declared and assigned simultaneously
```

Variable names are {{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}}. <!--SR:!2024-02-19,15,290-->

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
  ("`double`", "A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14`",),
  ("`float`", "A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F`",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2f02"--><!-- The following content is generated at 2024-02-01T11:50:25.897878+08:00. Any edits will be overridden! -->

> | type | description |
> |-|-|
> | `String` | A piece of text. Example: `"Hello"` |
> | `boolean` | Either true or false. Example: `true`, `false` |
> | `char` | A single character. Example: `'a'`, `'3'`, `' '` |
> | `double` | A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` |
> | `float` | A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` |
> | `int` | An integer. Example: `42` |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="652a"--><!-- The following content is generated at 2024-01-29T08:31:35.198780+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`String` <!--SR:!2024-02-19,15,290!2024-04-07,50,310-->
- `String`→:::←`boolean` <!--SR:!2024-04-13,56,310!2024-02-19,15,290-->
- `boolean`→:::←`char` <!--SR:!2024-02-20,16,290!2024-02-21,17,290-->
- `char`→:::←`double` <!--SR:!2024-03-29,44,290!2024-02-20,16,290-->
- `double`→:::←`float` <!--SR:!2024-02-18,14,290!2024-04-11,54,310-->
- `float`→:::←`int` <!--SR:!2024-03-24,36,290!2024-02-21,17,290-->
- `int`→:::←_(end)_ <!--SR:!2024-02-18,14,290!2024-04-08,51,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3b1a"--><!-- The following content is generated at 2024-02-01T11:50:25.871864+08:00. Any edits will be overridden! -->

- `String`::A piece of text. Example: `"Hello"` <!--SR:!2024-02-19,15,290-->
- `boolean`::Either true or false. Example: `true`, `false` <!--SR:!2024-02-19,15,290-->
- `char`::A single character. Example: `'a'`, `'3'`, `' '` <!--SR:!2024-02-20,16,290-->
- `double`::A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` <!--SR:!2024-04-13,56,310-->
- `float`::A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` <!--SR:!2024-02-18,14,290-->
- `int`::An integer. Example: `42` <!--SR:!2024-04-12,55,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

One cannot usually assign a value of a type to a variable {{declared with a different type}}: <!--SR:!2024-02-18,14,290-->

```Java
int anInteger = 3.14; // compilation error
float aFloat = 3.14; // compilation error
double aDouble = 3.14; // okay
```

In some circumstances, the value can be {{implicitly converted to the type of the variable, since there is no loss of data}}: <!--SR:!2024-03-25,37,290-->

```Java
float aFloat = 3; // the `int` of value 3 is implicitly converted into a `float` of value 3
assert aFloat == 3;
```

One can also {{explicitly convert the value to the type of the variable, but with loss of data}}: <!--SR:!2024-02-20,16,290-->

```Java
int anInteger = (int) -3.14; // the `double` of value -3.14 is explicitly converted into an `int` of value 3
assert anInteger == 3;
```

The above explicit conversion is called {{casting. A value can be casted to any type without any compilation error. However, only casting that makes sense will not result in a runtime error}}: <!--SR:!2024-02-18,14,290-->

```Java
int anInteger = (int) -3.14; // no compilation error and runtime error
assert anInteger == 3;
int anInteger2 = (int) "-3.14"; // no compilation error; but a runtime error when you run it
```

## operators

The assignment operator {{assigns a value to a variable}}: <!--SR:!2024-02-19,15,290-->

```Java
theAnswerToLifeTheUniverseAndEverything = 42
```

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93ab"--><!-- The following content is generated at 2024-01-30T13:35:46.604804+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `++` | increment a numerical variable by 1 |
> | `--` | decrement a numerical variable by 1 |
> | `*` | multiplication |
> | `/` | division; if both operands are of integral types, then round-towards-zero division |
> | `%` | remainder; the resulting sign is the same as the dividend, i.e. the number before the operator |
> | `+` | addition |
> | `-` | subtraction |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f21a"--><!-- The following content is generated at 2024-01-30T13:35:46.620801+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`++` <!--SR:!2024-02-21,17,290!2024-02-21,17,290-->
- `++`→:::←`--` <!--SR:!2024-02-19,15,290!2024-02-21,17,290-->
- `--`→:::←`*` <!--SR:!2024-03-20,35,290!2024-03-31,45,290-->
- `*`→:::←`/` <!--SR:!2024-02-18,14,290!2024-02-18,14,290-->
- `/`→:::←`%` <!--SR:!2024-02-20,16,290!2024-03-23,37,290-->
- `%`→:::←`+` <!--SR:!2024-02-21,17,290!2024-03-27,42,290-->
- `+`→:::←`-` <!--SR:!2024-02-21,17,290!2024-02-20,16,290-->
- `-`→:::←_(end)_ <!--SR:!2024-04-06,49,310!2024-02-20,16,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- `++`::increment a numerical variable by 1 <!--SR:!2024-04-07,50,310-->
- `--`::decrement a numerical variable by 1 <!--SR:!2024-02-21,17,290-->
- `*`::multiplication <!--SR:!2024-02-21,17,290-->
- `/`::division; if both operands are of integral types, then round-towards-zero division <!--SR:!2024-02-18,14,290-->
- `%`::remainder; the resulting sign is the same as the dividend, i.e. the number before the operator <!--SR:!2024-03-27,39,290-->
- `+`::addition <!--SR:!2024-02-20,16,290-->
- `-`::subtraction <!--SR:!2024-02-20,16,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### comparison operators

Below are common comparison operators, all of which returns {{a `boolean` value}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-02-19,15,290-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bd23"--><!-- The following content is generated at 2024-01-30T13:35:46.668328+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `<` | lesser than |
> | `>` | greater than |
> | `<=` | lesser than or equal to |
> | `>=` | greater than or equal to |
> | `==` | equal to |
> | `!=` | not equal to |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d123"--><!-- The following content is generated at 2024-01-30T13:35:46.651317+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`<` <!--SR:!2024-02-19,2,210!2024-02-22,5,270-->
- `<`→:::←`>` <!--SR:!2024-02-20,16,290!2024-02-21,17,290-->
- `>`→:::←`<=` <!--SR:!2024-02-18,14,290!2024-03-06,21,270-->
- `<=`→:::←`>=` <!--SR:!2024-02-19,15,290!2024-03-22,37,290-->
- `>=`→:::←`==` <!--SR:!2024-02-21,17,290!2024-02-19,2,170-->
- `==`→:::←`!=` <!--SR:!2024-02-20,16,290!2024-02-20,16,290-->
- `!=`→:::←_(end)_ <!--SR:!2024-02-20,16,290!2024-02-21,17,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.690328+08:00. Any edits will be overridden! -->

- `<`::lesser than <!--SR:!2024-02-18,14,290-->
- `>`::greater than <!--SR:!2024-02-19,15,290-->
- `<=`::lesser than or equal to <!--SR:!2024-02-21,17,290-->
- `>=`::greater than or equal to <!--SR:!2024-02-19,15,290-->
- `==`::equal to <!--SR:!2024-02-21,17,290-->
- `!=`::not equal to <!--SR:!2024-04-10,53,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

Do not mix up the equal to operator `==` and {{the assignment operator `=`}}. <!--SR:!2024-02-18,14,290-->

Also, one cannot chain {{comparison operators, like `2 <= aNumber <= 5`. [logic operators](#logic%20operators) are needed instead, like `2 <= aNumber && aNumber <= 5`}}. <!--SR:!2024-02-19,15,290-->

### logic operators

Below are common logic operators, all of which {{accept two booleans and return a boolean}}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2024-02-18,14,290-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = "operator", "description"
table = (
  ("`!`", "negate",),
  ("`&&`", "and",),
  ("`||`", "or",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2856"--><!-- The following content is generated at 2024-01-30T13:35:46.722323+08:00. Any edits will be overridden! -->

> | operator | description |
> |-|-|
> | `!` | negate |
> | `&&` | and |
> | `\|\|` | or |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d882"--><!-- The following content is generated at 2024-01-30T13:35:46.738334+08:00. Any edits will be overridden! -->

- _(begin)_→:::←`!` <!--SR:!2024-02-19,15,290!2024-03-17,33,290-->
- `!`→:::←`&&` <!--SR:!2024-02-20,16,290!2024-02-18,14,290-->
- `&&`→:::←`||` <!--SR:!2024-02-19,15,290!2024-02-20,16,290-->
- `||`→:::←_(end)_ <!--SR:!2024-04-12,55,310!2024-04-05,48,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee13"--><!-- The following content is generated at 2024-01-30T13:35:46.752902+08:00. Any edits will be overridden! -->

- `!`::negate <!--SR:!2024-02-18,14,290-->
- `&&`::and <!--SR:!2024-02-20,16,290-->
- `||`::or <!--SR:!2024-02-18,14,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
