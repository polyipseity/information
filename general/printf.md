---
aliases:
  - <code>printf</code>
  - "`printf`"
  - printf
tags:
  - flashcard/general/printf
  - language/in/English
---

# `printf`

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

## placeholder

%%

```Python
# pytextgen generate data
from pytextgen.gen import text
from pytextgen.util import Result
def link(name: str):
  return f"[{name}](#{name})"
def opt(string: str):
  return Rf"\[{string}\]"
components = [
  opt(link("parameter")),
  opt(link("flags")),
  opt(link("width")),
  opt(f".{link('precision')}"),
  opt(link("length")),
  link("type"),
]
return (
  Result(
    location=__env__.cwf_sect("b23d"),
    text=text(f"<code>%{''.join(components)}</code>"),
  ),
  *await memorize_seq(
    __env__.cwf_sects("49bd", "ee2f"),
    components,
  ),
)
```

%%

### syntax

<!--pytextgen generate section="b23d"--><!-- The following content is generated at 2023-08-24T21:36:58.847817+08:00. Any edits will be overridden! -->

<code>%\[[parameter](#parameter)\]\[[flags](#flags)\]\[[width](#width)\]\[.[precision](#precision)\]\[[length](#length)\][type](#type)</code>

<!--/pytextgen-->

<!--pytextgen generate section="49bd"--><!-- The following content is generated at 2023-08-28T21:01:29.628061+08:00. Any edits will be overridden! -->

> 1. \[[parameter](#parameter)\]
> 2. \[[flags](#flags)\]
> 3. \[[width](#width)\]
> 4. \[.[precision](#precision)\]
> 5. \[[length](#length)\]
> 6. [type](#type)

<!--/pytextgen-->

<!--pytextgen generate section="ee2f"--><!-- The following content is generated at 2024-01-04T20:17:52.556525+08:00. Any edits will be overridden! -->

- _(begin)_→:::←\[[parameter](#parameter)\] <!--SR:!2024-05-26,205,317!2024-05-29,208,329-->
- \[[parameter](#parameter)\]→:::←\[[flags](#flags)\] <!--SR:!2024-06-09,219,329!2024-05-30,209,329-->
- \[[flags](#flags)\]→:::←\[[width](#width)\] <!--SR:!2024-10-05,158,269!2025-01-10,348,309-->
- \[[width](#width)\]→:::←\[.[precision](#precision)\] <!--SR:!2024-05-13,63,277!2025-05-05,406,289-->
- \[.[precision](#precision)\]→:::←\[[length](#length)\] <!--SR:!2024-06-19,229,329!2024-12-28,339,309-->
- \[[length](#length)\]→:::←[type](#type) <!--SR:!2024-06-06,216,329!2025-06-26,441,289-->
- [type](#type)→:::←_(end)_ <!--SR:!2024-05-12,191,317!2024-05-26,205,329-->

<!--/pytextgen-->

### parameter

%%

```Python
# pytextgen generate data
from functools import partial
options = {
  "_n_$": "([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier",
}
return await memorize_table(
  __env__.cwf_sects("f192", "c19d"),
  ("character", "description"),
  options.items(),
  partial(map, cloze),
)
```

%%

<!--pytextgen generate section="f192"--><!-- The following content is generated at 2023-08-24T22:47:11.290253+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{_n_$}} | {{([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier}} | <!--SR:!2025-08-24,531,317!2024-06-12,222,329-->

<!--/pytextgen-->

<!--pytextgen generate section="c19d"--><!-- The following content is generated at 2024-01-04T20:17:52.598048+08:00. Any edits will be overridden! -->

- _(begin)_→:::←_n_$ <!--SR:!2024-05-20,66,277!2024-06-11,221,329-->
- _n_$→:::←_(end)_ <!--SR:!2026-06-16,778,337!2024-05-24,203,329-->

<!--/pytextgen-->

### flags

%%

```Python
# pytextgen generate data
from functools import partial
options = {
  "(space)": 'prepend a space before positive numbers; overridden by the [flag](#flag) `+`',
  R"\#": "use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`",
  "+": 'prepend + before positive numbers',
  "-": "align left",
  "0": "prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`",
}
return await memorize_table(
  __env__.cwf_sects("ff12", "123d"),
  ("character", "description"),
  options.items(),
  partial(map, cloze),
)
```

%%

A combination of zero or more of the following in any order:

<!--pytextgen generate section="ff12"--><!-- The following content is generated at 2024-01-04T19:31:50.120526+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{(space)}} | {{prepend a space before positive numbers; overridden by the [flag](#flag) `+`}} |
> | {{\#}} | {{use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`}} |
> | {{+}} | {{prepend + before positive numbers}} |
> | {{-}} | {{align left}} |
> | {{0}} | {{prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`}} | <!--SR:!2026-06-06,770,337!2024-05-09,160,277!2024-05-18,197,317!2024-05-29,86,217!2024-05-08,187,317!2024-12-21,333,309!2024-05-17,196,329!2025-04-24,457,329!2024-05-19,198,329!2024-12-24,336,309-->

<!--/pytextgen-->

<!--pytextgen generate section="123d"--><!-- The following content is generated at 2024-01-04T20:17:52.621048+08:00. Any edits will be overridden! -->

- _(begin)_→:::←(space) <!--SR:!2026-06-28,788,337!2024-05-20,199,329-->
- (space)→:::←\# <!--SR:!2024-05-07,17,209!2024-06-03,213,329-->
- \#→:::←+ <!--SR:!2024-07-05,81,289!2024-09-13,213,289-->
- +→:::←- <!--SR:!2024-05-28,207,329!2024-05-15,194,329-->
- -→:::←0 <!--SR:!2024-05-12,191,317!2024-06-12,73,277-->
- 0→:::←_(end)_ <!--SR:!2024-06-22,232,329!2024-05-30,209,329-->

<!--/pytextgen-->

### width

An integer or {{`*` specifying the minimum width}}. The result is {{padded with spaces}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument; a negative value adds the `-` [flag](#flags)}}. <!--SR:!2025-11-24,572,317!2025-12-11,623,329!2024-05-17,106,269-->

### precision

An integer or {{`*` specifying the precision, the meaning of which depends on the [type](#type)}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument and after the width additional argument if present; a negative value is ignored while invalid values are 0}}. <!--SR:!2025-05-07,412,297!2024-06-26,100,229-->

### length

%%

```Python
# pytextgen generate data
from functools import partial
options = {
  "L": "`long double`-sized float",
  "h": "`short`-sized integer",
  "hh": "`char`-sized integer",
  "j": "`intmax_t`-sized integer",
  "l": "`long`-sized integer; `double`-sized (ignored for) float",
  "ll": "`long long`-sized integer",
  "t": "`ptrdiff_t`-sized integer",
  "z": "`size_t`-sized integer",
}
return await memorize_table(
  __env__.cwf_sects("3052", "beff"),
  ("character", "description"),
  options.items(),
  partial(map, cloze),
)
```

%%

A combination of zero or more of the following in any order:

<!--pytextgen generate section="3052"--><!-- The following content is generated at 2023-08-25T01:23:36.864394+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{L}} | {{`long double`-sized float}} |
> | {{h}} | {{`short`-sized integer}} |
> | {{hh}} | {{`char`-sized integer}} |
> | {{j}} | {{`intmax_t`-sized integer}} |
> | {{l}} | {{`long`-sized integer; `double`-sized (ignored for) float}} |
> | {{ll}} | {{`long long`-sized integer}} |
> | {{t}} | {{`ptrdiff_t`-sized integer}} |
> | {{z}} | {{`size_t`-sized integer}} | <!--SR:!2025-08-02,477,297!2025-10-19,544,317!2024-05-08,187,317!2025-03-15,423,317!2026-05-06,744,337!2025-10-18,543,317!2024-12-13,298,277!2025-04-15,420,297!2025-02-19,348,277!2024-05-05,184,317!2024-05-21,200,329!2024-06-15,225,329!2025-10-19,540,309!2024-07-04,80,289!2024-06-03,213,329!2025-07-13,466,309-->

<!--/pytextgen-->

<!--pytextgen generate section="beff"--><!-- The following content is generated at 2024-01-04T20:17:52.664065+08:00. Any edits will be overridden! -->

- _(begin)_→:::←L <!--SR:!2026-07-16,803,337!2024-06-22,232,329-->
- L→:::←h <!--SR:!2024-05-27,133,257!2024-06-05,215,329-->
- h→:::←hh <!--SR:!2024-10-24,304,297!2024-06-19,229,329-->
- hh→:::←j <!--SR:!2025-04-09,391,297!2026-04-28,735,329-->
- j→:::←l <!--SR:!2024-06-13,223,329!2024-05-27,206,329-->
- l→:::←ll <!--SR:!2026-06-17,779,337!2024-05-29,208,329-->
- ll→:::←t <!--SR:!2024-06-04,71,277!2025-04-10,389,289-->
- t→:::←z <!--SR:!2024-05-05,184,317!2024-06-25,78,277-->
- z→:::←_(end)_ <!--SR:!2024-05-12,191,329!2024-06-01,211,329-->

<!--/pytextgen-->

### type

%%

```Python
# pytextgen generate data
from functools import partial
options = {
  "%": "literal %; rejects all other options",
  "a, A": "float into heximal exponential; [precision](#precision), by default enough to exactly represent the value, is the number of digits after the decimal point; `A` capitalizes the result",
  "c": "character",
  "d, i": "signed integer into decimal; [precision](#precision), by default 1, is the minimum number of digits; `i` can interpret octals and heximals when used with [`scanf`](scanf.md)",
  "e, E": "float into decimal exponential; [precision](#precision), by default 6, is the number of digits after the decimal point; `E` capitalizes the result",
  "f, F": "float into [fixed-point](fixed-point%20arithmetic.md) decimal; [precision](#precision), by default 6, is the number of digitals after the decimal point; `F` capitalizes the result",
  "g, G": "`f` if [precision](#precision) > exponent ≥ -4 and `e` otherwise, removing trailing zeros; [precision](#precision), by default 6 and 1 if 0, is the maximum number of significant figures; `G` capitalizes the result",
  "n": "prints nothing and writes the number of characters written so far to the specified integer pointer; rejects [flags](#flags), [precision](#precision), and [width](#width)",
  "o": "unsigned integer into octal; [precision](#precision), by default 1, is the minimum number of digits",
  "p": "pointer (`void*`) into an implementation-defined format",
  "s": "string; [precision](#precision), if specified, is the maximum number of bytes or, otherwise, the 0-based index of the first [null terminator](null-terminated%20string.md) is used",
  "u": "unsigned integer into decimal; [precision](#precision), by default 1, is the minimum number of digits",
  "x, X": "unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result",
}
return await memorize_table(
  __env__.cwf_sects("40db", "45dd"),
  ("character", "description"),
  options.items(),
  partial(map, cloze),
)
```

%%

<!--pytextgen generate section="40db"--><!-- The following content is generated at 2023-09-16T08:38:52.742774+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{%}} | {{literal %; rejects all other options}} |
> | {{a, A}} | {{float into heximal exponential; [precision](#precision), by default enough to exactly represent the value, is the number of digits after the decimal point; `A` capitalizes the result}} |
> | {{c}} | {{character}} |
> | {{d, i}} | {{signed integer into decimal; [precision](#precision), by default 1, is the minimum number of digits; `i` can interpret octals and heximals when used with [`scanf`](scanf.md)}} |
> | {{e, E}} | {{float into decimal exponential; [precision](#precision), by default 6, is the number of digits after the decimal point; `E` capitalizes the result}} |
> | {{f, F}} | {{float into [fixed-point](fixed-point%20arithmetic.md) decimal; [precision](#precision), by default 6, is the number of digitals after the decimal point; `F` capitalizes the result}} |
> | {{g, G}} | {{`f` if [precision](#precision) > exponent ≥ -4 and `e` otherwise, removing trailing zeros; [precision](#precision), by default 6 and 1 if 0, is the maximum number of significant figures; `G` capitalizes the result}} |
> | {{n}} | {{prints nothing and writes the number of characters written so far to the specified integer pointer; rejects [flags](#flags), [precision](#precision), and [width](#width)}} |
> | {{o}} | {{unsigned integer into octal; [precision](#precision), by default 1, is the minimum number of digits}} |
> | {{p}} | {{pointer (`void*`) into an implementation-defined format}} |
> | {{s}} | {{string; [precision](#precision), if specified, is the maximum number of bytes or, otherwise, the 0-based index of the first [null terminator](null-terminated%20string.md) is used}} |
> | {{u}} | {{unsigned integer into decimal; [precision](#precision), by default 1, is the minimum number of digits}} |
> | {{x, X}} | {{unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result}} | <!--SR:!2026-03-19,703,330!2026-07-17,804,337!2025-11-07,559,317!2024-06-07,196,277!2024-05-08,187,317!2024-05-13,192,317!2025-12-04,579,317!2024-08-31,138,257!2025-10-03,532,317!2024-07-02,198,277!2026-06-22,783,337!2025-04-02,385,297!2024-05-10,189,317!2024-06-15,127,237!2024-06-07,217,329!2024-08-04,224,289!2025-07-16,469,309!2025-09-28,524,309!2024-05-20,199,329!2024-06-15,225,329!2024-06-05,215,329!2024-05-25,204,329!2024-05-17,196,329!2024-05-22,109,269!2024-06-10,220,329!2025-07-20,472,309-->

<!--/pytextgen-->

<!--pytextgen generate section="45dd"--><!-- The following content is generated at 2024-01-04T20:17:52.718619+08:00. Any edits will be overridden! -->

- _(begin)_→:::←% <!--SR:!2024-05-21,200,329!2024-06-13,223,329-->
- %→:::←a, A <!--SR:!2025-09-21,520,310!2024-06-07,217,329-->
- a, A→:::←c <!--SR:!2024-05-30,209,329!2024-06-12,222,329-->
- c→:::←d, i <!--SR:!2025-12-30,634,317!2024-06-02,212,329-->
- d, i→:::←e, E <!--SR:!2024-05-25,204,329!2025-01-05,345,309-->
- e, E→:::←f, F <!--SR:!2026-04-25,733,330!2024-05-05,184,317-->
- f, F→:::←g, G <!--SR:!2024-05-20,199,329!2024-05-14,193,329-->
- g, G→:::←n <!--SR:!2024-05-13,26,229!2025-01-01,342,309-->
- n→:::←o <!--SR:!2024-05-22,201,317!2024-06-28,79,289-->
- o→:::←p <!--SR:!2024-06-17,227,329!2024-05-28,207,329-->
- p→:::←s <!--SR:!2025-09-17,517,310!2024-06-14,74,277-->
- s→:::←u <!--SR:!2024-06-03,213,329!2024-06-17,227,329-->
- u→:::←x, X <!--SR:!2025-11-15,561,309!2024-05-29,208,329-->
- x, X→:::←_(end)_ <!--SR:!2024-06-13,223,329!2024-05-30,209,329-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
