---
aliases:
  - Java string
  - Java strings
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/string
  - language/in/English
---

# Java string

A `String` is a piece of text. It is declared by {{enclosing the text in double quotes `"`, like `"example"`}}. A `char` is a single character. It is declared by {{enclosing the character in single quotes `'`, like `'a'`}}. <!--SR:!2024-05-03,71,316!2024-04-12,54,316-->

To put double quotes inside a `String`, one needs to {{escape them by adding `\` before the double quote, like `"quote, \"something\", unquote"`}}. Similarly, for `char`, one needs to {{escape the single quote, like `'\''`}}. <!--SR:!2024-04-24,63,316!2024-04-11,52,310-->

## parsing

If you want to convert a `String` representing a number into {{an `int`, use `Integer.parseInt`}}. Similarly, for `float` and `double` respectively, use {{`Float.parseFloat` and `Double.parseDouble` respectively}}: <!--SR:!2024-04-23,62,310!2024-04-13,54,316-->

```Java
int anInteger = Integer.parseInt("3");
assert anInteger == 3;
float aFloat = Float.parseFloat("3.1");
assert Math.abs(aFloat - 3.1f) < 1e-6f;
double aDouble = Double.parseDouble("3.14");
assert Math.abs(aDouble - 3.14) < 1e-15;
```

## indexing

To get the a `char` in a `String`, use {{`charAt(idx)`, where `idx` is the 0-based index of the character}}: <!--SR:!2024-04-29,67,310-->

```Java
char aChar = "abcdefg".charAt(3);
assert aChar == 'd';
```

## equality

One should (almost) always use {{`equals` instead of `==` to compare whether two strings are the same, like `string1.equals(string2)`}}. In general, comparing equality of objects uses {{`equals` in most cases. Non-objects always use `==`}}. See [object § equality](object.md#equality). <!--SR:!2024-04-21,61,316!2024-03-27,42,296-->
