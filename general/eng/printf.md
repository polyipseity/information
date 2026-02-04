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

{@{A `printf`‑style placeholder}@} begins {@{with `%`}@} and describes how {@{a single argument should be formatted}@}. Each placeholder is composed of {@{several components that must appear in a fixed order}@}. {@{Most of these components}@} are {@{optional}@}, but {@{the final _type_ specifier}@} is {@{always required}@}. <!--SR:!2026-02-16,16,311!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311!2026-02-16,16,311-->

In {@{full form}@}, a placeholder looks like: (annotation: {@{`% [parameter] [flags] [width] [.precision] [length] type`}@}) <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->

```text
% [parameter] [flags] [width] [.precision] [length] type
```

When {@{reading or writing a placeholder}@}, it helps to think of it as {@{a pipeline applied to one argument}@}. First, {@{an argument can be selected explicitly}@}, then {@{formatting rules are applied}@}, and finally the value is {@{converted to text according to its type}@}. <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311-->

{@{The components appear}@} in this order: (annotation: 6 ordered items: {@{parameter, flags}@}, {@{width, precision}@}, {@{length modifier, type specifier}@}) <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311-->

- an optional positional _parameter_
- zero or more _flags_
- an optional _width_
- an optional _precision_
- an optional _length modifier_
- exactly one _type specifier_

{@{Skipping a component}@} simply means its {@{default behavior applies}@}. <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->

### parameter selection

Placeholders may optionally specify {@{_which argument_ they apply to}@}. This is done using {@{a number followed by `$`, such as `1$` or `2$`}@}. For example, {@{`%2$d`}@} formats {@{the second argument as a decimal integer}@}. <!--SR:!2026-02-17,17,311!2026-02-12,12,291!2026-02-12,12,291!2026-02-17,17,311-->

This feature follows {@{POSIX rules}@}: either {@{_all_ placeholders in the format string}@} use positional parameters, or {@{_none_ of them do}@}. {@{Mixing positional and non-positional placeholders}@} is {@{not allowed}@}. <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311!2026-02-16,16,311-->

### flags

{@{_Flags_}@} are {@{single characters}@} that {@{fine‑tune alignment, padding, and signs}@}. They may appear {@{in any order, and multiple flags can be combined}@}. <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311!2026-02-17,17,311-->

The most important flags are:

- a space (` `), ::@:: which prefixes positive numbers with a space (unless `+` is used) <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `+`, ::@:: which explicitly prefixes positive numbers with a plus sign (overrides a space (` `)) <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->
- `-`, ::@:: which left-aligns the output within the field width (overrides `0`) <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->
- `0`, ::@:: which pads numeric output with leading zeros when a width is specified (ignored if `-` is present) <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `#`, ::@:: which enables an alternative form whose meaning depends on the type <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->

{@{The alternative form}@} preserves {@{decimal points or trailing zeros for certain floating‑point formats}@}, and adds {@{prefixes such as `0`, `0x`, or `0X` for octal and hexadecimal integers}@} when {@{the value is nonzero}@}. <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311-->

### width

{@{The _width_}@} specifies {@{the minimum number of characters used for the output}@}. If {@{the formatted result is shorter}@}, it is {@{padded with spaces by default}@}. Width can be written {@{directly as an integer or as `*`}@}. When {@{`*` is used}@}, {@{an additional `int` argument}@} {@{before the supplied value (and the argument supplying the precision if any)}@} supplies {@{the width}@}; {@{a negative width}@} activates {@{left alignment}@}. <!--SR:!2032-09-29,2501,337!2033-09-11,2831,349!2027-04-02,763,269!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311-->

### precision

{@{The _precision_, introduced by a dot (`.`)}@}, further {@{constrains the output}@}. {@{Its meaning}@} depends on {@{the type being formatted}@}. <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311-->

For {@{_integer types_ (`d`/`i`, `u`, `o`, `x`/`X`)}@}, precision specifies {@{the _minimum number of digits_ to display}@}. If {@{the value has fewer digits}@}, it is {@{padded on the left with zeros}@}. {@{The default precision}@} for these types is {@{_1_}@}. <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311-->

For {@{_floating‑point types_}@}, precision {@{depends on the notation}@}: (annotation: 4 items: {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@}) <!--SR:!2026-02-17,17,311!2026-02-16,16,311!2026-02-17,17,311-->

- `f` and `F`; `e` and `E` ::@:: use precision as the _number of digits after the decimal point_, with a default of _6_. <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->
- `g` and `G` ::@:: precision specifies the _maximum number of significant digits_ (default _6_, with an explicit `0` treated as _1_), determines whether fixed‑point or exponential notation is chosen based on the value's exponent (using fixed-point when −4&nbsp;≤&nbsp;exponent&nbsp;<&nbsp;precision and exponential otherwise), rounds to at most that many significant digits, and removes trailing zeros and the decimal point unless the `#` flag is used. <!--SR:!2026-02-16,16,311!2026-02-12,12,291-->
- `a` and `A` ::@:: use precision to control the _number of hexadecimal digits after the decimal point_; if omitted, the precision is large enough to exactly represent the value. <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->

For {@{_non-numeric and special types_}@}, precision is either {@{limited or rejected}@}: (annotation: 5 items: {@{`s`, `c`, `p`, `%`, `n`}@}) <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311-->

- `s` ::@:: uses precision as the _maximum number of bytes printed_; if omitted, output continues until the terminating null character. <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `c` and `p` ::@:: ignore precision entirely. <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `%` ::@:: rejects precision. <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `n` ::@:: rejects precision, along with flags and width. <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->

Like {@{width, precision}@} may be {@{given as a number or as `*`}@}. {@{A negative precision}@} is {@{ignored}@}, while {@{invalid values are treated as zero}@}. <!--SR:!2026-02-17,17,311!2026-02-16,16,311!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311-->

### length modifiers

{@{_Length modifiers_}@} describe {@{the _size of the argument type_}@} so that `printf` {@{interprets it correctly}@}. {@{These modifiers matter}@} primarily for {@{integer and floating‑point conversions}@}. <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311!2026-02-17,17,311-->

{@{Common integer length modifiers}@} include: (annotation: 7 items: {@{`hh`, `h`, `l`, `ll`}@}, {@{`j`, `t`, `z`}@}) <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311-->

- `hh` ::@:: for `char` <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `h` ::@:: for `short` <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `l` ::@:: for `long` <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `ll` ::@:: for `long long` <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `j` ::@:: for `intmax_t` <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `t` ::@:: for `ptrdiff_t` <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->
- `z` ::@:: for `size_t` <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->

For {@{floating-point values}@}, {@{`L`}@} indicates {@{a `long double`}@}. {@{The `l` modifier is accepted}@} for floating-point types but has {@{no effect and is ignored (remains `double`)}@}. <!--SR:!2026-02-17,17,311!2026-02-17,17,311!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311-->

### type specifiers

{@{The _type specifier_}@} determines how {@{the argument is converted to text}@}. It is {@{the only required component}@} of a placeholder. <!--SR:!2026-02-16,16,311!2026-02-17,17,311!2026-02-16,16,311-->

{@{Numeric types}@} include: (annotation: 8 items: {@{`d`/`i`, `u`}@}, {@{`o`, `x`/`X`}@}, {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@}) <!--SR:!2026-02-16,16,311!2026-02-16,16,311!2026-02-17,17,311!2026-02-17,17,311-->

- `d` and `i` ::@:: for signed decimal integers; note the latter interpret octals and heximals when used with `scanf` <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->
- `u` ::@:: for unsigned decimal integers <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `o` ::@:: for octal integers <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->
- `x` and `X` ::@:: for hexadecimal integers <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `f` and `F` ::@:: for fixed-point decimal floating-point output <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `e` and `E` ::@:: for decimal exponential notation <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `g` and `G` ::@:: for adaptive floating-point formatting that chooses between fixed and exponential forms <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->
- `a` and `A` ::@:: for hexadecimal floating-point notation <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->

{@{Character and pointer types}@} include: (annotation: 3 items: {@{`c`, `s`, `p`}@}) <!--SR:!2026-02-16,16,311!2026-02-16,16,311-->

- `c` ::@:: for a single character <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->
- `s` ::@:: for a string (precision limits the number of bytes printed) <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `p` ::@:: for a pointer value in an implementation-defined format <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->

{@{Two special cases}@} deserve mention: (annotation: 2 items: {@{`%`, `n`}@}) <!--SR:!2026-02-17,17,311!2026-02-16,16,311-->

- `%` ::@:: prints a literal percent sign and rejects all other options <!--SR:!2026-02-17,17,311!2026-02-17,17,311-->
- `n` ::@:: produces no output but stores the number of characters written so far into the provided integer pointer; it does not accept flags, width, or precision <!--SR:!2026-02-16,16,311!2026-02-17,17,311-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
