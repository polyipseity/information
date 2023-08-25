---
aliases:
  - <code>printf</code>
  - "`printf`"
  - printf
tags:
  - categories/computer_science
  - flashcards/general/printf
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# `printf`

## placeholder

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import text
from pytextgen.util import Result
e = __env__
def link(name: str):
	return f"[{name}](#{name})"
def opt(string: str):
	return Rf"\[{string}\]"
components = {
	"parameter": opt(link("parameter")),
	"flags": opt(link("flags")),
	"width": opt(link("width")),
	"precision": opt(f".{link('precision')}"),
	"length": opt(link("length")),
	"type": link("type"),
}
return (
	Result(
		location=e.cwf_sect("b23d"),
		text=text(f"<code>%{''.join(components.values())}</code>"),
	),
	*await memorize_seq(
		e.cwf_sects("49bd", "ee2f"),
		map(link, components.keys()),
	),
)
```
%%

### syntax

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b23d"--><!-- The following content is generated at 2023-08-24T21:36:58.847817+08:00. Any edits will be overridden! -->

<code>%\[[parameter](#parameter)\]\[[flags](#flags)\]\[[width](#width)\]\[.[precision](#precision)\]\[[length](#length)\][type](#type)</code>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="49bd"--><!-- The following content is generated at 2023-08-24T21:32:32.563811+08:00. Any edits will be overridden! -->

> 1. [parameter](#parameter)
> 2. [flags](#flags)
> 3. [width](#width)
> 4. [precision](#precision)
> 5. [length](#length)
> 6. [type](#type)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee2f"--><!-- The following content is generated at 2023-08-24T21:32:32.576806+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[parameter](#parameter)
2. [parameter](#parameter)→:::←[flags](#flags)
3. [flags](#flags)→:::←[width](#width)
4. [width](#width)→:::←[precision](#precision)
5. [precision](#precision)→:::←[length](#length)
6. [length](#length)→:::←[type](#type)
7. [type](#type)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### parameter

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
options = {
	"_n_$": "([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier",
}
return await memorize_table(
	e.cwf_sects("f192", "c19d"),
	("character", "description"),
	options.items(),
	partial(map, cloze),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f192"--><!-- The following content is generated at 2023-08-24T22:47:11.290253+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{_n_$}} | {{([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="c19d"--><!-- The following content is generated at 2023-08-24T22:44:32.846596+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←_n_$
2. _n_$→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### flags

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
options = {
	"  (space)": 'prepend spaces before positive numbers; overridden by the [flag](#flag) `+`',
	R"\#": "use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`",
	"+": 'prepend + before positive numbers',
	"-": "align left",
	"0": "prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`",
}
return await memorize_table(
	e.cwf_sects("ff12", "123d"),
	("character", "description"),
	options.items(),
	partial(map, cloze),
)
```
%%

A combination of zero or more of the following in any order:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff12"--><!-- The following content is generated at 2023-08-25T01:19:18.222545+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{  (space)}} | {{prepend spaces before positive numbers; overridden by the [flag](#flag) `+`}} |
> | {{\#}} | {{use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`}} |
> | {{+}} | {{prepend + before positive numbers}} |
> | {{-}} | {{align left}} |
> | {{0}} | {{prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123d"--><!-- The following content is generated at 2023-08-25T00:41:32.736032+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←  (space)
2.   (space)→:::←\#
3. \#→:::←+
4. +→:::←-
5. -→:::←0
6. 0→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### width

An integer or {{`*` specifying the minimum width}}. The result is {{padded with spaces}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument; a negative value adds the `-` [flag](#flags)}}.
### precision

An integer or {{`*` specifying the precision, the meaning of which depends on the [type](#type)}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument and after the width additional argument if present; a negative value is ignored while invalid values are 0}}.

### length

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
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
	e.cwf_sects("3052", "beff"),
	("character", "description"),
	options.items(),
	partial(map, cloze),
)
```
%%

A combination of zero or more of the following in any order:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3052"--><!-- The following content is generated at 2023-08-25T01:23:36.864394+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{L}} | {{`long double`-sized float}} |
> | {{h}} | {{`short`-sized integer}} |
> | {{hh}} | {{`char`-sized integer}} |
> | {{j}} | {{`intmax_t`-sized integer}} |
> | {{l}} | {{`long`-sized integer; `double`-sized (ignored for) float}} |
> | {{ll}} | {{`long long`-sized integer}} |
> | {{t}} | {{`ptrdiff_t`-sized integer}} |
> | {{z}} | {{`size_t`-sized integer}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="beff"--><!-- The following content is generated at 2023-08-25T01:19:18.238502+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←L
2. L→:::←h
3. h→:::←hh
4. hh→:::←j
5. j→:::←l
6. l→:::←ll
7. ll→:::←t
8. t→:::←z
9. z→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### type

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
options = {
	"%": "literal %; rejects all other options",
	"a, A": "float into heximal exponential; [precision](#precision), by default enough to exactly represent the value, is the number of digits after the decimal point; `A` capitalizes the result",
	"c": "character",
	"d, i": "signed integer into decimal; [precision](#precision), by default 1, is the minimum number of digits; `i` can interpret octals and heximals when used with [`scanf`](scanf.md)",
	"e, E": "float into decimal exponential; [precision](#precision), by default 6, is the number of digits after the decimal point; `E` capitalizes the result",
	"f, F": "float into [fixed-point](fixed-point%20arithmetic.md) decimal; [precision](#precision), by default 6, is the number of digitals after the decimal point; `F` capitalizes the result",
	"g, G": "`e` if [precision](#precision) > exponent ≥ -4 or `f` otherwise, removing trailing zeros; [precision](#precision), by default 6 and 1 if 0, is the maximum number of significant figures; `G` capitalizes the result",
	"n": "prints nothing and writes the number of characters written so far to the specified integer pointer; rejects [flags](#flags), [precision](#precision), and [width](#width)",
	"o": "unsigned integer into octal; [precision](#precision), by default 1, is the minimum number of digits",
	"p": "pointer (`void*`) into an implementation-defined format",
	"s": "string; [precision](#precision), if specified, is the maximum number of bytes or, otherwise, the first [null terminator](null-terminated%20string.md) is used",
	"u": "unsigned integer into decimal; [precision](#precision), by default 1, is the minimum number of digits",
	"x, X": "unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result",
}
return await memorize_table(
	e.cwf_sects("40db", "45dd"),
	("character", "description"),
	options.items(),
	partial(map, cloze),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="40db"--><!-- The following content is generated at 2023-08-25T01:26:21.284791+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{%}} | {{literal %; rejects all other options}} |
> | {{a, A}} | {{float into heximal exponential; [precision](#precision), by default enough to exactly represent the value, is the number of digits after the decimal point; `A` capitalizes the result}} |
> | {{c}} | {{character}} |
> | {{d, i}} | {{signed integer into decimal; [precision](#precision), by default 1, is the minimum number of digits; `i` can interpret octals and heximals when used with [`scanf`](scanf.md)}} |
> | {{e, E}} | {{float into decimal exponential; [precision](#precision), by default 6, is the number of digits after the decimal point; `E` capitalizes the result}} |
> | {{f, F}} | {{float into [fixed-point](fixed-point%20arithmetic.md) decimal; [precision](#precision), by default 6, is the number of digitals after the decimal point; `F` capitalizes the result}} |
> | {{g, G}} | {{`e` if [precision](#precision) > exponent ≥ -4 or `f` otherwise, removing trailing zeros; [precision](#precision), by default 6 and 1 if 0, is the maximum number of significant figures; `G` capitalizes the result}} |
> | {{n}} | {{prints nothing and writes the number of characters written so far to the specified integer pointer; rejects [flags](#flags), [precision](#precision), and [width](#width)}} |
> | {{o}} | {{unsigned integer into octal; [precision](#precision), by default 1, is the minimum number of digits}} |
> | {{p}} | {{pointer (`void*`) into an implementation-defined format}} |
> | {{s}} | {{string; [precision](#precision), if specified, is the maximum number of bytes or, otherwise, the first [null terminator](null-terminated%20string.md) is used}} |
> | {{u}} | {{unsigned integer into decimal; [precision](#precision), by default 1, is the minimum number of digits}} |
> | {{x, X}} | {{unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="45dd"--><!-- The following content is generated at 2023-08-25T01:19:18.269420+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←%
2. %→:::←a, A
3. a, A→:::←c
4. c→:::←d, i
5. d, i→:::←e, E
6. e, E→:::←f, F
7. f, F→:::←g, G
8. g, G→:::←n
9. n→:::←o
10. o→:::←p
11. p→:::←s
12. s→:::←u
13. u→:::←x, X
14. x, X→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
