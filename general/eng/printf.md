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

{@{A `printf`‑style placeholder}@} begins {@{with `%`}@} and describes how {@{a single argument should be formatted}@}. Each placeholder is composed of {@{several components that must appear in a fixed order}@}. {@{Most of these components}@} are {@{optional}@}, but {@{the final _type_ specifier}@} is {@{always required}@}.

In {@{full form}@}, a placeholder looks like: (annotation: {@{`% [parameter] [flags] [width] [.precision] [length] type`}@})

```text
% [parameter] [flags] [width] [.precision] [length] type
```

When {@{reading or writing a placeholder}@}, it helps to think of it as {@{a pipeline applied to one argument}@}. First, {@{an argument can be selected explicitly}@}, then {@{formatting rules are applied}@}, and finally the value is {@{converted to text according to its type}@}.

{@{The components appear}@} in this order: (annotation: 6 ordered items: {@{parameter, flags}@}, {@{width, precision}@}, {@{length modifier, type specifier}@})

- an optional positional _parameter_
- zero or more _flags_
- an optional _width_
- an optional _precision_
- an optional _length modifier_
- exactly one _type specifier_

{@{Skipping a component}@} simply means its {@{default behavior applies}@}.

### parameter selection

Placeholders may optionally specify {@{_which argument_ they apply to}@}. This is done using {@{a number followed by `$`, such as `1$` or `2$`}@}. For example, {@{`%2$d`}@} formats {@{the second argument as a decimal integer}@}.

This feature follows {@{POSIX rules}@}: either {@{_all_ placeholders in the format string}@} use positional parameters, or {@{_none_ of them do}@}. {@{Mixing positional and non-positional placeholders}@} is {@{not allowed}@}.

### flags

{@{_Flags_}@} are {@{single characters}@} that {@{fine‑tune alignment, padding, and signs}@}. They may appear {@{in any order, and multiple flags can be combined}@}.

The most important flags are:

- a space (` `), ::@:: which prefixes positive numbers with a space (unless `+` is used)
- `+`, ::@:: which explicitly prefixes positive numbers with a plus sign (overrides a space (` `))
- `-`, ::@:: which left-aligns the output within the field width (overrides `0`)
- `0`, ::@:: which pads numeric output with leading zeros when a width is specified (ignored if `-` is present)
- `#`, ::@:: which enables an alternative form whose meaning depends on the type

{@{The alternative form}@} preserves {@{decimal points or trailing zeros for certain floating‑point formats}@}, and adds {@{prefixes such as `0`, `0x`, or `0X` for octal and hexadecimal integers}@} when {@{the value is nonzero}@}.

### width

{@{The _width_}@} specifies {@{the minimum number of characters used for the output}@}. If {@{the formatted result is shorter}@}, it is {@{padded with spaces by default}@}. Width can be written {@{directly as an integer or as `*`}@}. When {@{`*` is used}@}, {@{an additional `int` argument}@} {@{before the supplied value (and the argument supplying the precision if any)}@} supplies {@{the width}@}; {@{a negative width}@} activates {@{left alignment}@}.

### precision

{@{The _precision_, introduced by a dot (`.`)}@}, further {@{constrains the output}@}. {@{Its meaning}@} depends on {@{the type being formatted}@}.

For {@{_integer types_ (`d`/`i`, `u`, `o`, `x`/`X`)}@}, precision specifies {@{the _minimum number of digits_ to display}@}. If {@{the value has fewer digits}@}, it is {@{padded on the left with zeros}@}. {@{The default precision}@} for these types is {@{_1_}@}.

For {@{_floating‑point types_}@}, precision {@{depends on the notation}@}: (annotation: 4 items: {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@})

- `f` and `F`; `e` and `E` ::@:: use precision as the _number of digits after the decimal point_, with a default of _6_.
- `g` and `G` ::@:: precision specifies the _maximum number of significant digits_ (default _6_, with an explicit `0` treated as _1_), determines whether fixed‑point or exponential notation is chosen based on the value's exponent (using fixed-point when −4&nbsp;≤&nbsp;exponent&nbsp;<&nbsp;precision and exponential otherwise), rounds to at most that many significant digits, and removes trailing zeros and the decimal point unless the `#` flag is used.
- `a` and `A` ::@:: use precision to control the _number of hexadecimal digits after the decimal point_; if omitted, the precision is large enough to exactly represent the value.

For {@{_non-numeric and special types_}@}, precision is either {@{limited or rejected}@}: (annotation: 5 items: {@{`s`, `c`, `p`, `%`, `n`}@})

- `s` ::@:: uses precision as the _maximum number of bytes printed_; if omitted, output continues until the terminating null character.
- `c` and `p` ::@:: ignore precision entirely.
- `%` ::@:: rejects precision.
- `n` ::@:: rejects precision, along with flags and width.

Like {@{width, precision}@} may be {@{given as a number or as `*`}@}. {@{A negative precision}@} is {@{ignored}@}, while {@{invalid values are treated as zero}@}.

### length modifiers

{@{_Length modifiers_}@} describe {@{the _size of the argument type_}@} so that `printf` {@{interprets it correctly}@}. {@{These modifiers matter}@} primarily for {@{integer and floating‑point conversions}@}.

{@{Common integer length modifiers}@} include: (annotation: 7 items: {@{`hh`, `h`, `l`, `ll`}@}, {@{`j`, `t`, `z`}@})

- `hh` ::@:: for `char`
- `h` ::@:: for `short`
- `l` ::@:: for `long`
- `ll` ::@:: for `long long`
- `j` ::@:: for `intmax_t`
- `t` ::@:: for `ptrdiff_t`
- `z` ::@:: for `size_t`

For {@{floating-point values}@}, {@{`L`}@} indicates {@{a `long double`}@}. {@{The `l` modifier is accepted}@} for floating-point types but has {@{no effect and is ignored (remains `double`)}@}.

### type specifiers

{@{The _type specifier_}@} determines how {@{the argument is converted to text}@}. It is {@{the only required component}@} of a placeholder.

{@{Numeric types}@} include: (annotation: 8 items: {@{`d`/`i`, `u`}@}, {@{`o`, `x`/`X`}@}, {@{`f`/`F`, `e`/`E`, `g`/`G`, `a`/`A`}@})

- `d` and `i` ::@:: for signed decimal integers; note the latter interpret octals and heximals when used with `scanf`
- `u` ::@:: for unsigned decimal integers
- `o` ::@:: for octal integers
- `x` and `X` ::@:: for hexadecimal integers
- `f` and `F` ::@:: for fixed-point decimal floating-point output
- `e` and `E` ::@:: for decimal exponential notation
- `g` and `G` ::@:: for adaptive floating-point formatting that chooses between fixed and exponential forms
- `a` and `A` ::@:: for hexadecimal floating-point notation

{@{Character and pointer types}@} include: (annotation: 3 items: {@{`c`, `s`, `p`}@})

- `c` ::@:: for a single character
- `s` ::@:: for a string (precision limits the number of bytes printed)
- `p` ::@:: for a pointer value in an implementation-defined format

{@{Two special cases}@} deserve mention: (annotation: 2 items: {@{`%`, `n`}@})

- `%` ::@:: prints a literal percent sign and rejects all other options
- `n` ::@:: produces no output but stores the number of characters written so far into the provided integer pointer; it does not accept flags, width, or precision

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
