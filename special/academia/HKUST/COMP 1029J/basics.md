---
aliases:
  - Java basic
  - Java basics
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/basics
  - language/in/English
---

# Java basics

```Python
# pytextgen generate module
# import ../../../../../tools/utility.py.md
```

## basics

- comment :@: A comment is either enclosed by `/*` and `*/` like `/* example */` or starts with `//` like `// example`. For the first one, the comment ends when the `*/` is first encountered. For the second one, the comment ends when the line ends. <!--SR:!2028-03-19,1173,350-->
- package :@: Packages are analogous to directories. The differences are that package names are more restricted and each package component is separated by `.` instead of `/`. One imports all the Java files in a package by `import a.package.*;`. More commonly, one imports a Java file, say `Example.java` in a package by `import a.package.Example;`. <!--SR:!2027-01-12,816,330-->
- spacing :@: Java ignores whitespace in most places. Whitespace are not ignored in some places, such as in strings `"This string has a space."` or before the names of method calls `. thisIsInvalidJavaCode()`. Usually whitespace are added before statements systematically, with more spaces per level of code block `{ /* code block */ }`. This is called indentation. <!--SR:!2025-12-09,491,310-->
- statement :@: A Java program is a collection of statements. A statement can be multiline and ends with a semicolon `;`. A statement can also be a code block `{ /* code block */ }`, which is also a collection of statements itself. <!--SR:!2027-08-14,970,330-->

## variable

To assign a value or the result of an expression to a variable, use {@{`=`}@}: <!--SR:!2028-03-11,1166,350-->

```Java
variableName = 1 + 2;
```

One must {@{declare a variable, prefixed with the type of the variable, i.e. what the variable can hold}@}, before assigning things to it. Optionally, {@{one can declare a variable and assign to it}@} simultaneously: <!--SR:!2026-08-04,687,330!2025-01-28,281,330-->

```Java
int anIntegerVariable; // `int` means the variable can hold integers
anIntegerVariable = 1 + 2;
String aStringVariable = "a string"; // variables can be declared and assigned simultaneously
```

Variable names are {@{case sensitive, cannot be keywords, cannot have some characters like spaces, and cannot begin with some characters like numbers}@}. <!--SR:!2027-03-22,862,330-->

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

- _(begin)_→::@::←`String` <!--SR:!2028-06-26,1253,350!2027-07-12,976,350-->
- `String`→::@::←`boolean` <!--SR:!2026-10-27,749,330!2028-05-21,1223,350-->
- `boolean`→::@::←`char` <!--SR:!2025-02-03,281,330!2025-02-21,296,330-->
- `char`→::@::←`double` <!--SR:!2025-08-13,366,290!2027-01-18,812,330-->
- `double`→::@::←`float` <!--SR:!2025-11-29,483,310!2026-09-05,711,330-->
- `float`→::@::←`int` <!--SR:!2025-04-29,289,290!2027-05-27,910,330-->
- `int`→::@::←_(end)_ <!--SR:!2028-04-21,1201,350!2025-12-28,475,310-->

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-02-01T11:50:25.871864+08:00. Any edits will be overridden! -->

- `String`:@:A piece of text. Example: `"Hello"` <!--SR:!2028-01-31,1135,350-->
- `boolean`:@:Either true or false. Example: `true`, `false` <!--SR:!2027-12-14,1098,350-->
- `char`:@:A single character. Example: `'a'`, `'3'`, `' '` <!--SR:!2025-02-12,290,330-->
- `double`:@:A floating point number with double precision (15 to 17 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` <!--SR:!2026-11-12,763,330-->
- `float`:@:A floating point number with single precision (6 to 9 significant figures). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` <!--SR:!2026-12-22,796,330-->
- `int`:@:An integer. Example: `42` <!--SR:!2027-11-09,1071,350-->

<!--/pytextgen-->

### conversion

One cannot usually assign a value of a type to a variable {@{declared with a different type}@}: <!--SR:!2026-10-23,745,330-->

```Java
int anInteger = 3.14; // compilation error
float aFloat = 3.14; // compilation error
double aDouble = 3.14; // okay
```

In some circumstances, the value can be {@{implicitly converted to the type of the variable, since there is no loss of data}@}: <!--SR:!2026-05-08,617,330-->

```Java
float aFloat = 3; // the `int` of value 3 is implicitly converted into a `float` of value 3
assert aFloat == 3;
```

If implicit conversion is disallowed, one can also {@{explicitly convert the value to the type of the variable, but with loss of data}@}: <!--SR:!2025-02-13,291,330-->

```Java
int anInteger = (int) -3.14; // the `double` of value -3.14 is explicitly converted into an `int` of value 3
assert anInteger == 3;
```

The above explicit conversion is called {@{casting. A value can be casted to any type without any compilation error. However, only casting that makes sense will not result in a runtime error}@}: <!--SR:!2026-07-19,677,330-->

```Java
int anInteger = (int) -3.14; // no compilation error and runtime error
assert anInteger == 3;
int anInteger2 = (int) "-3.14"; // no compilation error; but a runtime error when you run it
```

## operators

The assignment operator {@{assigns a value to a variable}@}: <!--SR:!2028-03-05,1161,350-->

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

- _(begin)_→::@::←`++` <!--SR:!2025-03-17,318,330!2025-02-23,299,330-->
- `++`→::@::←`--` <!--SR:!2025-01-21,274,330!2025-01-30,277,330-->
- `--`→::@::←`*` <!--SR:!2025-02-18,253,310!2026-03-18,538,310-->
- `*`→::@::←`/` <!--SR:!2026-12-22,796,330!2028-02-08,1143,350-->
- `/`→::@::←`%` <!--SR:!2028-05-30,1229,350!2025-05-23,306,290-->
- `%`→::@::←`+` <!--SR:!2025-03-14,314,330!2025-07-20,350,290-->
- `+`→::@::←`-` <!--SR:!2025-02-10,288,330!2025-02-04,282,330-->
- `-`→::@::←_(end)_ <!--SR:!2027-06-11,950,350!2025-01-29,281,330-->

<!--/pytextgen-->

<!--pytextgen generate section="9cda"--><!-- The following content is generated at 2024-01-30T13:35:46.633801+08:00. Any edits will be overridden! -->

- `++`:@:increment a numerical variable by 1 <!--SR:!2027-07-11,976,350-->
- `--`:@:decrement a numerical variable by 1 <!--SR:!2025-03-15,316,330-->
- `*`:@:multiplication <!--SR:!2025-03-01,303,330-->
- `/`:@:division; if both operands are of integral types, then round-towards-zero division <!--SR:!2025-02-05,100,270-->
- `%`:@:remainder; the resulting sign is the same as the dividend, i.e. the number before the operator <!--SR:!2025-06-14,322,290-->
- `+`:@:addition <!--SR:!2028-06-12,1239,350-->
- `-`:@:subtraction <!--SR:!2028-03-13,1165,350-->

<!--/pytextgen-->

### comparison operators

Below are common comparison operators, all of which returns {@{a `boolean` value}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2025-01-30,283,330-->

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

- _(begin)_→::@::←`<` <!--SR:!2025-10-23,293,210!2027-11-04,1031,330-->
- `<`→::@::←`>` <!--SR:!2025-02-17,296,330!2025-01-28,275,330-->
- `>`→::@::←`<=` <!--SR:!2026-02-26,514,310!2027-03-22,845,310-->
- `<=`→::@::←`>=` <!--SR:!2026-12-22,796,330!2025-05-09,306,290-->
- `>=`→::@::←`==` <!--SR:!2025-12-03,412,310!2025-03-26,137,170-->
- `==`→::@::←`!=` <!--SR:!2025-01-27,279,330!2026-07-04,625,330-->
- `!=`→::@::←_(end)_ <!--SR:!2025-01-29,280,330!2025-03-02,304,330-->

<!--/pytextgen-->

<!--pytextgen generate section="cc23"--><!-- The following content is generated at 2024-01-30T13:35:46.690328+08:00. Any edits will be overridden! -->

- `<`:@:lesser than <!--SR:!2027-10-28,1059,350-->
- `>`:@:greater than <!--SR:!2028-03-01,1158,350-->
- `<=`:@:lesser than or equal to <!--SR:!2027-05-25,909,330-->
- `>=`:@:greater than or equal to <!--SR:!2025-01-23,276,330-->
- `==`:@:equal to <!--SR:!2025-02-01,279,330-->
- `!=`:@:not equal to <!--SR:!2027-09-26,1036,350-->

<!--/pytextgen-->

Do not mix up the equal to operator `==` and {@{the assignment operator `=`}@}. <!--SR:!2027-11-19,1076,350-->

Also, one cannot chain {@{comparison operators, like `2 <= aNumber <= 5`. [logic operators](#logic%20operators) are needed instead, like `2 <= aNumber && aNumber <= 5`}@}. <!--SR:!2027-01-21,816,330-->

### logic operators

Below are common logic operators, all of which {@{accept two booleans and return a boolean}@}. Operators have higher precedence than or same precedence as operators below it in the list: <!--SR:!2026-09-01,707,330-->

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

- _(begin)_→::@::←`!` <!--SR:!2028-06-14,1241,350!2026-02-19,570,330-->
- `!`→::@::←`&&` <!--SR:!2026-08-12,635,310!2026-12-22,796,330-->
- `&&`→::@::←<code>&#124;&#124;</code> <!--SR:!2025-01-24,277,330!2028-05-16,1220,350-->
- <code>&#124;&#124;</code>→::@::←_(end)_ <!--SR:!2027-11-25,1083,350!2026-06-07,643,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ee13"--><!-- The following content is generated at 2024-02-20T14:26:41.011968+08:00. Any edits will be overridden! -->

- `!`:@:negate <!--SR:!2027-08-19,1005,350-->
- `&&`:@:and <!--SR:!2028-01-10,1115,350-->
- <code>&#124;&#124;</code>:@:or <!--SR:!2026-12-22,796,330-->

<!--/pytextgen-->
