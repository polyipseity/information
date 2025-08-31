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

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## placeholder

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

- _(begin)_→::@::←\[[parameter](#parameter)\] <!--SR:!2026-11-09,897,337!2026-12-26,941,349-->
- \[[parameter](#parameter)\]→::@::←\[[flags](#flags)\] <!--SR:!2026-05-30,720,329!2026-04-17,687,329-->
- \[[flags](#flags)\]→::@::←\[[width](#width)\] <!--SR:!2025-12-06,424,269!2027-12-21,1075,309-->
- \[[width](#width)\]→::@::←\[.[precision](#precision)\] <!--SR:!2027-10-20,1010,317!2029-10-24,1631,309-->
- \[.[precision](#precision)\]→::@::←\[[length](#length)\] <!--SR:!2026-07-13,754,329!2027-04-30,683,309-->
- \[[length](#length)\]→::@::←[type](#type) <!--SR:!2027-02-10,979,349!2030-05-02,1771,309-->
- [type](#type)→::@::←_(end)_ <!--SR:!2026-08-26,835,337!2026-12-11,929,349-->

<!--/pytextgen-->

### parameter

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

<!--pytextgen generate section="f192"--><!-- The following content is generated at 2023-08-24T22:47:11.290253+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {@{_n_$}@} | {@{([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier}@} | <!--SR:!2032-01-05,2325,337!2027-03-15,1006,349-->

<!--/pytextgen-->

<!--pytextgen generate section="c19d"--><!-- The following content is generated at 2024-01-04T20:17:52.598048+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←_n_$ <!--SR:!2027-02-23,755,297!2027-03-10,1002,349-->
- _n_$→::@::←_(end)_ <!--SR:!2026-06-16,778,337!2026-11-30,920,349-->

<!--/pytextgen-->

### flags

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

A combination of zero or more of the following in any order:

<!--pytextgen generate section="ff12"--><!-- The following content is generated at 2024-01-04T19:31:50.120526+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {@{(space)}@} | {@{prepend a space before positive numbers; overridden by the [flag](#flag) `+`}@} |
> | {@{\#}@} | {@{use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`}@} |
> | {@{+}@} | {@{prepend + before positive numbers}@} |
> | {@{-}@} | {@{align left}@} |
> | {@{0}@} | {@{prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`}@} | <!--SR:!2026-06-06,770,337!2030-04-04,1711,297!2026-09-29,862,337!2026-09-07,365,197!2025-12-21,592,317!2028-11-15,1425,329!2026-10-25,888,349!2030-12-28,2074,349!2026-11-03,897,349!2027-05-01,687,309-->

<!--/pytextgen-->

<!--pytextgen generate section="123d"--><!-- The following content is generated at 2024-01-04T20:17:52.621048+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←(space) <!--SR:!2026-06-28,788,337!2026-11-06,900,349-->
- (space)→::@::←\# <!--SR:!2027-05-19,742,249!2027-01-27,968,349-->
- \#→::@::←+ <!--SR:!2027-09-17,936,309!2026-05-22,615,289-->
- +→::@::←- <!--SR:!2026-12-22,938,349!2026-10-11,879,349-->
- -→::@::←0 <!--SR:!2026-08-27,836,337!2026-01-05,268,257-->
- 0→::@::←_(end)_ <!--SR:!2027-05-10,1052,349!2027-01-05,950,349-->

<!--/pytextgen-->

### width

An integer or {@{`*` specifying the minimum width}@}. The result is {@{padded with spaces}@}. If {@{`*` is used, an additional argument to `printf` of type `int` appears before the field argument; a negative value adds the `-` [flag](#flags)}@}. <!--SR:!2025-11-24,572,317!2025-12-11,623,329!2027-04-02,763,269-->

### precision

An integer or {@{`*` specifying the precision, the meaning of which depends on the [type](#type)}@}. If {@{`*` is used, an additional argument to `printf` of type `int` appears before the field argument and after the width additional argument if present; a negative value is ignored while invalid values are 0}@}. <!--SR:!2029-12-29,1697,317!2026-07-15,521,229-->

### length

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

A combination of zero or more of the following in any order:

<!--pytextgen generate section="3052"--><!-- The following content is generated at 2023-08-25T01:23:36.864394+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {@{L}@} | {@{`long double`-sized float}@} |
> | {@{h}@} | {@{`short`-sized integer}@} |
> | {@{hh}@} | {@{`char`-sized integer}@} |
> | {@{j}@} | {@{`intmax_t`-sized integer}@} |
> | {@{l}@} | {@{`long`-sized integer; `double`-sized (ignored for) float}@} |
> | {@{ll}@} | {@{`long long`-sized integer}@} |
> | {@{t}@} | {@{`ptrdiff_t`-sized integer}@} |
> | {@{z}@} | {@{`size_t`-sized integer}@} | <!--SR:!2030-12-21,1967,317!2025-10-19,544,317!2026-08-07,821,337!2028-11-15,1341,317!2026-05-06,744,337!2025-10-18,543,317!2028-02-06,1150,297!2030-01-16,1737,317!2028-10-25,1344,297!2025-12-11,584,317!2026-03-11,659,329!2027-03-31,1019,349!2025-10-19,540,309!2029-02-24,1374,329!2027-01-24,965,349!2030-12-23,1989,329-->

<!--/pytextgen-->

<!--pytextgen generate section="beff"--><!-- The following content is generated at 2024-01-04T20:17:52.664065+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←L <!--SR:!2026-07-16,803,337!2027-05-09,1051,349-->
- L→::@::←h <!--SR:!2027-09-25,875,257!2027-02-06,976,349-->
- h→::@::←hh <!--SR:!2028-02-18,1212,317!2027-04-23,1038,349-->
- hh→::@::←j <!--SR:!2028-06-13,1161,297!2026-04-28,735,329-->
- j→::@::←l <!--SR:!2026-01-13,469,329!2026-04-04,677,329-->
- l→::@::←ll <!--SR:!2026-06-17,779,337!2026-12-27,942,349-->
- ll→::@::←t <!--SR:!2026-06-13,543,277!2029-07-20,1562,309-->
- t→::@::←z <!--SR:!2026-07-23,808,337!2026-09-14,596,277-->
- z→::@::←_(end)_ <!--SR:!2026-09-26,866,349!2027-01-13,956,349-->

<!--/pytextgen-->

### type

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

<!--pytextgen generate section="40db"--><!-- The following content is generated at 2023-09-16T08:38:52.742774+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {@{%}@} | {@{literal %; rejects all other options}@} |
> | {@{a, A}@} | {@{float into heximal exponential; [precision](#precision), by default enough to exactly represent the value, is the number of digits after the decimal point; `A` capitalizes the result}@} |
> | {@{c}@} | {@{character}@} |
> | {@{d, i}@} | {@{signed integer into decimal; [precision](#precision), by default 1, is the minimum number of digits; `i` can interpret octals and heximals when used with [`scanf`](scanf.md)}@} |
> | {@{e, E}@} | {@{float into decimal exponential; [precision](#precision), by default 6, is the number of digits after the decimal point; `E` capitalizes the result}@} |
> | {@{f, F}@} | {@{float into [fixed-point](fixed-point%20arithmetic.md) decimal; [precision](#precision), by default 6, is the number of digitals after the decimal point; `F` capitalizes the result}@} |
> | {@{g, G}@} | {@{`f` if [precision](#precision) > exponent ≥ -4 and `e` otherwise, removing trailing zeros; [precision](#precision), by default 6 and 1 if 0, is the maximum number of significant figures; `G` capitalizes the result}@} |
> | {@{n}@} | {@{prints nothing and writes the number of characters written so far to the specified integer pointer; rejects [flags](#flags), [precision](#precision), and [width](#width)}@} |
> | {@{o}@} | {@{unsigned integer into octal; [precision](#precision), by default 1, is the minimum number of digits}@} |
> | {@{p}@} | {@{pointer (`void*`) into an implementation-defined format}@} |
> | {@{s}@} | {@{string; [precision](#precision), if specified, is the maximum number of bytes or, otherwise, the 0-based index of the first [null terminator](null-terminated%20string.md) is used}@} |
> | {@{u}@} | {@{unsigned integer into decimal; [precision](#precision), by default 1, is the minimum number of digits}@} |
> | {@{x, X}@} | {@{unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result}@} | <!--SR:!2026-03-19,703,330!2026-07-17,804,337!2025-11-07,559,317!2025-12-01,542,277!2026-08-06,820,337!2026-08-31,840,337!2025-12-04,579,317!2028-02-16,910,257!2025-10-03,532,317!2025-12-31,547,277!2026-06-22,783,337!2025-10-11,192,277!2025-12-30,598,317!2027-03-23,711,237!2027-02-16,984,349!2026-05-12,646,289!2031-01-06,2000,329!2025-09-28,524,309!2026-11-07,901,349!2027-04-01,1020,349!2026-05-12,706,329!2026-03-28,672,329!2026-10-24,887,349!2030-01-02,1642,309!2026-06-03,723,329!2031-01-31,2020,329-->

<!--/pytextgen-->

<!--pytextgen generate section="45dd"--><!-- The following content is generated at 2024-01-04T20:17:52.718619+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←% <!--SR:!2026-11-13,906,349!2027-03-21,1011,349-->
- %→::@::←a, A <!--SR:!2025-09-21,520,310!2027-02-15,983,349-->
- a, A→::@::←c <!--SR:!2027-01-06,951,349!2026-06-13,731,329-->
- c→::@::←d, i <!--SR:!2025-12-30,634,317!2027-01-19,961,349-->
- d, i→::@::←e, E <!--SR:!2026-12-06,925,349!2029-01-20,1476,329-->
- e, E→::@::←f, F <!--SR:!2026-04-25,733,330!2026-07-20,805,337-->
- f, F→::@::←g, G <!--SR:!2026-11-08,902,349!2026-10-06,875,349-->
- g, G→::@::←n <!--SR:!2026-01-18,428,249!2027-11-25,1058,309-->
- n→::@::←o <!--SR:!2026-10-19,880,337!2026-04-12,312,269-->
- o→::@::←p <!--SR:!2026-07-02,745,329!2026-12-21,937,349-->
- p→::@::←s <!--SR:!2025-09-17,517,310!2026-07-29,571,277-->
- s→::@::←u <!--SR:!2026-05-06,702,329!2026-07-03,746,329-->
- u→::@::←x, X <!--SR:!2025-11-15,561,309!2026-12-28,943,349-->
- x, X→::@::←_(end)_ <!--SR:!2027-03-20,1010,349!2027-01-04,949,349-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
