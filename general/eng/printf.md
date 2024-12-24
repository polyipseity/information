---
aliases:
  - <code>printf</code>
  - "`printf`"
  - printf
tags:
  - flashcard/active/general/printf
  - language/in/English
---

# `printf`

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
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

- _(begin)_→::@::←\[[parameter](#parameter)\]
- \[[parameter](#parameter)\]→::@::←\[[flags](#flags)\]
- \[[flags](#flags)\]→::@::←\[[width](#width)\]
- \[[width](#width)\]→::@::←\[.[precision](#precision)\]
- \[.[precision](#precision)\]→::@::←\[[length](#length)\]
- \[[length](#length)\]→::@::←[type](#type)
- [type](#type)→::@::←_(end)_

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
> | {@{_n_$}@} | {@{([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier}@} |

<!--/pytextgen-->

<!--pytextgen generate section="c19d"--><!-- The following content is generated at 2024-01-04T20:17:52.598048+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←_n_$
- _n_$→::@::←_(end)_

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
> | {@{0}@} | {@{prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`}@} |

<!--/pytextgen-->

<!--pytextgen generate section="123d"--><!-- The following content is generated at 2024-01-04T20:17:52.621048+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←(space)
- (space)→::@::←\#
- \#→::@::←+
- +→::@::←-
- -→::@::←0
- 0→::@::←_(end)_

<!--/pytextgen-->

### width

An integer or {@{`*` specifying the minimum width}@}. The result is {@{padded with spaces}@}. If {@{`*` is used, an additional argument to `printf` of type `int` appears before the field argument; a negative value adds the `-` [flag](#flags)}@}.

### precision

An integer or {@{`*` specifying the precision, the meaning of which depends on the [type](#type)}@}. If {@{`*` is used, an additional argument to `printf` of type `int` appears before the field argument and after the width additional argument if present; a negative value is ignored while invalid values are 0}@}.

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
> | {@{z}@} | {@{`size_t`-sized integer}@} |

<!--/pytextgen-->

<!--pytextgen generate section="beff"--><!-- The following content is generated at 2024-01-04T20:17:52.664065+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←L
- L→::@::←h
- h→::@::←hh
- hh→::@::←j
- j→::@::←l
- l→::@::←ll
- ll→::@::←t
- t→::@::←z
- z→::@::←_(end)_

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
> | {@{x, X}@} | {@{unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result}@} |

<!--/pytextgen-->

<!--pytextgen generate section="45dd"--><!-- The following content is generated at 2024-01-04T20:17:52.718619+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←%
- %→::@::←a, A
- a, A→::@::←c
- c→::@::←d, i
- d, i→::@::←e, E
- e, E→::@::←f, F
- f, F→::@::←g, G
- g, G→::@::←n
- n→::@::←o
- o→::@::←p
- p→::@::←s
- s→::@::←u
- u→::@::←x, X
- x, X→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/printf) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
