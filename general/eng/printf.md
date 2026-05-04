---
aliases:
  - <code>printf</code>
  - "`printf`"
  - printf
tags:
  - flashcard/active/general/eng/printf
  - language/in/English
---

# `printf`

## placeholder

{@{A `printf`‑style placeholder}@} begins {@{with `%`}@} and describes how {@{a single argument should be formatted}@}. Each placeholder is composed of {@{several components that must appear in a fixed order}@}. {@{Most of these components}@} are {@{optional}@}, but {@{the final _type_ specifier}@} is {@{always required}@}. <!--SR:!2027-02-22,300,351!2027-03-07,313,351!2027-04-16,348,351!2027-02-27,305,351!2027-03-01,307,351!2027-04-21,352,351!2027-04-02,336,351!2027-04-02,336,351-->

In {@{full form}@}, a placeholder looks like: (annotation: {@{`% [parameter] [flags] [width] [.precision] [length] type`}@}) <!--SR:!2027-03-04,310,351!2027-03-23,329,351-->

```text
% [parameter] [flags] [width] [.precision] [length] type
```

When {@{reading or writing a placeholder}@}, it helps to think of it as {@{a pipeline applied to one argument}@}. First, {@{an argument can be selected explicitly}@}, then {@{formatting rules are applied}@}, and finally the value is {@{converted to text according to its type}@}. <!--SR:!2027-04-21,352,351!2027-04-17,349,351!2027-04-14,346,351!2027-04-15,347,351!2027-04-21,352,351-->

{@{The components appear}@} in this order: (annotation: 6 ordered items: {@{parameter, flags}@}, {@{width, precision}@}, {@{length modifier, type specifier}@}) <!--SR:!2027-03-05,311,351!2027-04-13,345,351!2027-04-21,352,351!2027-04-23,354,351-->

- an optional positional _parameter_
- zero or more _flags_
- an optional _width_
- an optional _precision_
- an optional _length modifier_
- exactly one _type specifier_

{@{Skipping a component}@} simply means its {@{default behavior applies}@}. <!--SR:!2027-04-02,336,351!2027-02-26,304,351-->

### parameter selection

Placeholders may optionally specify {@{_which argument_ they apply to}@}. This is done using {@{a number followed by <code>&dollar;</code>, such as <code>1&dollar;</code> or <code>2&dollar;</code>}@}. For example, {@{<code>%2&dollar;d</code>}@} formats {@{the second argument as a decimal integer}@}. <!--SR:!2027-04-08,340,351!2026-10-20,203,331!2026-10-22,205,331!2027-04-07,339,351-->

This feature follows {@{POSIX rules}@}: either {@{_all_ placeholders in the format string}@} use positional parameters, or {@{_none_ of them do}@}. {@{Mixing positional and non-positional placeholders}@} is {@{not allowed}@}. <!--SR:!2027-03-19,325,351!2027-04-11,343,351!2027-04-09,341,351!2027-03-16,322,351!2027-03-12,318,351-->

### flags

{@{_Flags_}@} are {@{single characters}@} that {@{fine‑tune alignment, padding, and signs}@}. They may appear {@{in any order, and multiple flags can be combined}@}. <!--SR:!2027-03-03,309,351!2027-04-21,352,351!2027-02-28,306,351!2027-04-23,354,351-->

The most important flags are:

- a space (` `), ::@:: which prefixes positive numbers with a space (unless `+` is used) <!--SR:!2027-03-17,323,351!2027-04-23,354,351-->
- `+`, ::@:: which explicitly prefixes positive numbers with a plus sign (overrides a space (` `)) <!--SR:!2027-04-09,341,351!2027-03-07,313,351-->
- `-`, ::@:: which left-aligns the output within the field width (overrides `0`) <!--SR:!2027-03-10,316,351!2027-03-22,328,351-->
- `0`, ::@:: which pads numeric output with leading zeros when a width is specified (ignored if `-` is present) <!--SR:!2027-04-02,336,351!2027-04-21,352,351-->
- `#`, ::@:: which enables an alternative form whose meaning depends on the type <!--SR:!2027-04-17,349,351!2027-02-21,299,351-->

{@{The alternative form}@} preserves {@{decimal points or trailing zeros for certain floating‑point formats}@}, and adds {@{prefixes such as `0`, `0x`, or `0X` for octal and hexadecimal integers}@} when {@{the value is nonzero}@}. <!--SR:!2027-03-12,318,351!2027-04-22,353,351!2027-04-23,354,351!2027-02-21,299,351-->

### width

{@{The _width_}@} specifies {@{the minimum number of characters used for the output}@}. If {@{the formatted result is shorter}@}, it is {@{padded with spaces by default}@}. Width can be written {@{directly as an integer or as `*`}@}. When {@{`*` is used}@}, {@{an additional `int` argument}@} {@{before the supplied value (and the argument supplying the precision if any)}@} supplies {@{the width}@}; {@{a negative width}@} activates {@{left alignment}@}. <!--SR:!2032-09-29,2501,337!2033-09-11,2831,349!2027-04-02,763,269!2027-03-08,314,351!2027-04-23,354,351!2027-04-22,353,351!2027-04-12,344,351!2027-04-11,343,351!2027-04-22,353,351!2027-04-10,342,351!2027-04-17,349,351-->

### precision

{@{The _precision_, introduced by a dot (`.`)}@}, further {@{constrains the output}@}. {@{Its meaning}@} depends on {@{the type being formatted}@}. <!--SR:!2027-04-12,344,351!2027-04-21,352,351!2027-04-16,348,351!2027-03-02,308,351-->

For {@{_integer types_ (`d`/`i`, `u`, `o`, `x`/`X`)}@}, precision specifies {@{the _minimum number of digits_ to display}@}. If {@{the value has fewer digits}@}, it is {@{padded on the left with zeros}@}. {@{The default precision}@} for these types is {@{_1_}@}. <!--SR:!2027-04-22,353,351!2027-04-23,354,351!2027-04-22,353,351!2027-04-13,345,351!2027-04-23,354,351!2027-04-02,336,351-->

For {@{_floating‑point types_}@}, precision {@{depends on the notation}@}: (annotation: 4 items: {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@}) <!--SR:!2027-04-22,353,351!2027-03-13,319,351!2027-04-07,339,351-->

- `f` and `F`; `e` and `E` ::@:: use precision as the _number of digits after the decimal point_, with a default of _6_. <!--SR:!2027-02-23,301,351!2027-03-06,312,351-->
- `g` and `G` ::@:: precision specifies the _maximum number of significant digits_ (default _6_, with an explicit `0` treated as _1_), determines whether fixed‑point or exponential notation is chosen based on the value's exponent (using fixed-point when −4&nbsp;≤&nbsp;exponent&nbsp;<&nbsp;precision and exponential otherwise), rounds to at most that many significant digits, and removes trailing zeros and the decimal point unless the `#` flag is used. <!--SR:!2027-02-27,305,351!2026-10-21,204,331-->
- `a` and `A` ::@:: use precision to control the _number of hexadecimal digits after the decimal point_; if omitted, the precision is large enough to exactly represent the value. <!--SR:!2027-04-08,340,351!2026-12-15,236,331-->

For {@{_non-numeric and special types_}@}, precision is either {@{limited or rejected}@}: (annotation: 5 items: {@{`s`, `c`, `p`, `%`, `n`}@}) <!--SR:!2027-04-16,348,351!2027-04-08,340,351!2027-03-09,315,351-->

- `s` ::@:: uses precision as the _maximum number of bytes printed_; if omitted, output continues until the terminating null character. <!--SR:!2027-04-13,345,351!2027-04-13,345,351-->
- `c` and `p` ::@:: ignore precision entirely. <!--SR:!2027-04-21,352,351!2027-04-15,347,351-->
- `%` ::@:: rejects precision. <!--SR:!2027-04-17,349,351!2027-04-10,342,351-->
- `n` ::@:: rejects precision, along with flags and width. <!--SR:!2027-04-22,353,351!2027-04-15,347,351-->

Like {@{width, precision}@} may be {@{given as a number or as `*`}@}. {@{A negative precision}@} is {@{ignored}@}, while {@{invalid values are treated as zero}@}. <!--SR:!2027-04-22,353,351!2027-03-10,316,351!2027-04-02,336,351!2027-04-23,354,351!2027-02-23,301,351-->

### length modifiers

{@{_Length modifiers_}@} describe {@{the _size of the argument type_}@} so that `printf` {@{interprets it correctly}@}. {@{These modifiers matter}@} primarily for {@{integer and floating‑point conversions}@}. <!--SR:!2027-04-21,352,351!2027-04-23,354,351!2027-04-06,338,351!2027-04-14,346,351!2027-04-23,354,351-->

{@{Common integer length modifiers}@} include: (annotation: 7 items: {@{`hh`, `h`, `l`, `ll`}@}, {@{`j`, `t`, `z`}@}) <!--SR:!2027-03-06,312,351!2027-04-22,353,351!2027-04-22,353,351-->

- `hh` ::@:: for `char` <!--SR:!2027-03-18,324,351!2027-04-11,343,351-->
- `h` ::@:: for `short` <!--SR:!2027-03-13,319,351!2027-04-10,342,351-->
- `l` ::@:: for `long` <!--SR:!2027-04-23,354,351!2027-04-16,348,351-->
- `ll` ::@:: for `long long` <!--SR:!2027-04-14,346,351!2027-04-22,353,351-->
- `j` ::@:: for `intmax_t` <!--SR:!2027-04-17,349,351!2027-04-23,354,351-->
- `t` ::@:: for `ptrdiff_t` <!--SR:!2027-04-05,337,351!2027-03-20,326,351-->
- `z` ::@:: for `size_t` <!--SR:!2027-03-02,308,351!2027-04-23,354,351-->

For {@{floating-point values}@}, {@{`L`}@} indicates {@{a `long double`}@}. {@{The `l` modifier is accepted}@} for floating-point types but has {@{no effect and is ignored (remains `double`)}@}. <!--SR:!2027-04-16,348,351!2027-04-22,353,351!2027-03-03,309,351!2027-04-09,341,351!2027-03-14,320,351-->

### type specifiers

{@{The _type specifier_}@} determines how {@{the argument is converted to text}@}. It is {@{the only required component}@} of a placeholder. <!--SR:!2027-02-28,306,351!2027-04-05,337,351!2027-04-02,336,351-->

{@{Numeric types}@} include: (annotation: 8 items: {@{`d`/`i`, `u`}@}, {@{`o`, `x`/`X`}@}, {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@}) <!--SR:!2027-04-02,336,351!2027-03-15,321,351!2027-04-15,347,351!2027-04-17,349,351-->

- `d` and `i` ::@:: for signed decimal integers; note the latter interpret octals and heximals when used with `scanf` <!--SR:!2027-03-21,327,351!2027-02-28,306,351-->
- `u` ::@:: for unsigned decimal integers <!--SR:!2027-03-04,310,351!2027-04-21,352,351-->
- `o` ::@:: for octal integers <!--SR:!2027-04-21,352,351!2027-03-09,315,351-->
- `x` and `X` ::@:: for hexadecimal integers <!--SR:!2027-02-24,302,351!2027-04-14,346,351-->
- `f` and `F` ::@:: for fixed-point decimal floating-point output <!--SR:!2027-04-06,338,351!2027-04-07,339,351-->
- `e` and `E` ::@:: for decimal exponential notation <!--SR:!2027-03-05,311,351!2027-04-12,344,351-->
- `g` and `G` ::@:: for adaptive floating-point formatting that chooses between fixed and exponential forms <!--SR:!2027-02-24,302,351!2027-04-10,342,351-->
- `a` and `A` ::@:: for hexadecimal floating-point notation <!--SR:!2027-04-04,336,351!2027-03-08,314,351-->

{@{Character and pointer types}@} include: (annotation: 3 items: {@{`c`, `s`, `p`}@}) <!--SR:!2027-02-22,300,351!2027-02-26,304,351-->

- `c` ::@:: for a single character <!--SR:!2027-04-11,343,351!2027-02-25,303,351-->
- `s` ::@:: for a string (precision limits the number of bytes printed) <!--SR:!2027-04-22,353,351!2027-04-22,353,351-->
- `p` ::@:: for a pointer value in an implementation-defined format <!--SR:!2027-04-12,344,351!2027-03-01,307,351-->

{@{Two special cases}@} deserve mention: (annotation: 2 items: {@{`%`, `n`}@}) <!--SR:!2027-04-21,352,351!2027-03-11,317,351-->

- `%` ::@:: prints a literal percent sign and rejects all other options <!--SR:!2027-04-21,352,351!2027-04-21,352,351-->
- `n` ::@:: produces no output but stores the number of characters written so far into the provided integer pointer; it does not accept flags, width, or precision <!--SR:!2027-02-27,305,351!2027-04-23,354,351-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
