---
aliases:
  - <code>printf</code>
  - "`printf`"
  - printf
tags:
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
		location=e.cwf_sect("b23d"),
		text=text(f"<code>%{''.join(components)}</code>"),
	),
	*await memorize_seq(
		e.cwf_sects("49bd", "ee2f"),
		components,
	),
)
```
%%

### syntax

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b23d"--><!-- The following content is generated at 2023-08-24T21:36:58.847817+08:00. Any edits will be overridden! -->

<code>%\[[parameter](#parameter)\]\[[flags](#flags)\]\[[width](#width)\]\[.[precision](#precision)\]\[[length](#length)\][type](#type)</code>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="49bd"--><!-- The following content is generated at 2023-08-28T21:01:29.628061+08:00. Any edits will be overridden! -->

> 1. \[[parameter](#parameter)\]
> 2. \[[flags](#flags)\]
> 3. \[[width](#width)\]
> 4. \[.[precision](#precision)\]
> 5. \[[length](#length)\]
> 6. [type](#type)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee2f"--><!-- The following content is generated at 2023-08-28T21:01:29.604636+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←\[[parameter](#parameter)\] <!--SR:!2023-10-29,50,297!2023-10-28,49,309-->
2. \[[parameter](#parameter)\]→:::←\[[flags](#flags)\] <!--SR:!2023-10-30,51,309!2023-10-28,49,309-->
3. \[[flags](#flags)\]→:::←\[[width](#width)\] <!--SR:!2023-10-20,41,289!2023-10-05,26,289-->
4. \[[width](#width)\]→:::←\[.[precision](#precision)\] <!--SR:!2023-10-22,43,297!2023-10-28,49,289-->
5. \[.[precision](#precision)\]→:::←\[[length](#length)\] <!--SR:!2023-10-31,52,309!2023-10-05,26,289-->
6. \[[length](#length)\]→:::←[type](#type) <!--SR:!2023-10-30,51,309!2023-09-12,3,269-->
7. [type](#type)→:::←_(end)_ <!--SR:!2023-10-25,46,297!2023-10-27,48,309-->

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
> | {{_n_$}} | {{([POSIX](POSIX.md)) use the _n_-th parameter; either no or all placeholders have this specifier}} | <!--SR:!2023-10-23,44,297!2023-10-29,50,309-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="c19d"--><!-- The following content is generated at 2023-08-24T22:44:32.846596+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←_n_$ <!--SR:!2023-10-25,46,297!2023-10-30,51,309-->
2. _n_$→:::←_(end)_ <!--SR:!2023-10-22,43,297!2023-10-27,48,309-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### flags

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
options = {
	"  (space)": 'prepend a space before positive numbers; overridden by the [flag](#flag) `+`',
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff12"--><!-- The following content is generated at 2023-08-28T16:44:43.033581+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{  (space)}} | {{prepend a space before positive numbers; overridden by the [flag](#flag) `+`}} |
> | {{\#}} | {{use the alternative form: trailing 0s are kept for `g` and `G`; decimal point is kept for `e`, `E`, `f`, `F`, `g`, and `G`; and `0`, `0x`, and `0X` are prepended to non-zero numbers respectively for `o`, `x`, and `X`}} |
> | {{+}} | {{prepend + before positive numbers}} |
> | {{-}} | {{align left}} |
> | {{0}} | {{prepend 0s before numbers if [width](#width) is specified; overridden by the [flag](#flag) `-`}} | <!--SR:!2023-10-22,43,297!2023-09-30,21,277!2023-10-27,48,297!2023-09-12,3,237!2023-10-25,46,297!2023-10-02,23,289!2023-10-26,47,309!2023-10-03,24,289!2023-10-26,47,309!2023-10-05,26,289-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123d"--><!-- The following content is generated at 2023-08-25T00:41:32.736032+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←  (space) <!--SR:!2023-10-23,44,297!2023-10-26,47,309-->
2.   (space)→:::←\# <!--SR:!2023-10-01,22,269!2023-10-29,50,309-->
3. \#→:::←+ <!--SR:!2023-10-20,41,289!2023-10-31,52,309-->
4. +→:::←- <!--SR:!2023-10-29,50,309!2023-10-26,47,309-->
5. -→:::←0 <!--SR:!2023-10-25,46,297!2023-10-29,50,297-->
6. 0→:::←_(end)_ <!--SR:!2023-10-31,52,309!2023-10-28,49,309-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### width

An integer or {{`*` specifying the minimum width}}. The result is {{padded with spaces}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument; a negative value adds the `-` [flag](#flags)}}. <!--SR:!2023-10-22,43,297!2023-10-27,48,309!2023-10-04,25,289-->

### precision

An integer or {{`*` specifying the precision, the meaning of which depends on the [type](#type)}}. If {{`*` is used, an additional argument to `printf` of type `int` appears before the field argument and after the width additional argument if present; a negative value is ignored while invalid values are 0}}. <!--SR:!2023-10-25,46,297!2023-09-12,3,249-->

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
> | {{z}} | {{`size_t`-sized integer}} | <!--SR:!2023-10-21,42,277!2023-10-21,42,297!2023-10-25,46,297!2023-10-04,25,277!2023-10-21,42,297!2023-10-21,42,297!2023-10-19,40,277!2023-10-19,40,277!2023-10-24,45,277!2023-10-24,45,297!2023-10-26,47,309!2023-10-30,51,309!2023-10-23,44,289!2023-10-20,41,289!2023-10-29,50,309!2023-10-17,38,289-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="beff"--><!-- The following content is generated at 2023-08-25T01:19:18.238502+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←L <!--SR:!2023-10-24,45,297!2023-10-31,52,309-->
2. L→:::←h <!--SR:!2023-10-20,41,277!2023-10-28,49,309-->
3. h→:::←hh <!--SR:!2023-09-12,3,237!2023-10-31,52,309-->
4. hh→:::←j <!--SR:!2023-10-23,44,297!2023-10-22,43,289-->
5. j→:::←l <!--SR:!2023-10-31,52,309!2023-10-27,48,309-->
6. l→:::←ll <!--SR:!2023-10-23,44,297!2023-10-28,49,309-->
7. ll→:::←t <!--SR:!2023-10-16,37,277!2023-10-26,47,289-->
8. t→:::←z <!--SR:!2023-10-24,45,297!2023-10-20,41,277-->
9. z→:::←_(end)_ <!--SR:!2023-10-24,45,309!2023-10-29,50,309-->

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
> | {{x, X}} | {{unsigned integer into heximal; [precision](#precision), by default 1, is the minimum number of digits; `X` capitalizes the result}} | <!--SR:!2023-10-20,41,290!2023-10-24,45,297!2023-10-22,43,297!2023-09-30,21,257!2023-10-23,44,297!2023-10-25,46,297!2023-10-24,45,297!2023-10-19,40,277!2023-10-21,42,297!2023-10-02,23,277!2023-10-22,43,297!2023-10-23,44,297!2023-10-25,46,297!2023-09-12,3,237!2023-10-30,51,309!2023-10-03,24,289!2023-10-17,38,289!2023-10-23,44,289!2023-10-27,48,309!2023-10-31,52,309!2023-10-30,51,309!2023-10-27,48,309!2023-10-25,46,309!2023-10-03,24,289!2023-10-30,51,309!2023-10-29,50,309-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="45dd"--><!-- The following content is generated at 2023-08-25T01:19:18.269420+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←% <!--SR:!2023-10-26,47,309!2023-10-29,50,309-->
2. %→:::←a, A <!--SR:!2023-10-21,42,290!2023-10-30,51,309-->
3. a, A→:::←c <!--SR:!2023-10-28,49,309!2023-10-31,52,309-->
4. c→:::←d, i <!--SR:!2023-10-18,39,277!2023-10-29,50,309-->
5. d, i→:::←e, E <!--SR:!2023-10-27,48,309!2023-10-05,26,289-->
6. e, E→:::←f, F <!--SR:!2023-10-21,42,290!2023-10-24,45,297-->
7. f, F→:::←g, G <!--SR:!2023-10-26,47,309!2023-10-26,47,309-->
8. g, G→:::←n <!--SR:!2023-09-12,3,269!2023-10-01,22,289-->
9. n→:::←o <!--SR:!2023-10-28,49,297!2023-10-31,52,309-->
10. o→:::←p <!--SR:!2023-10-31,52,309!2023-10-28,49,309-->
11. p→:::←s <!--SR:!2023-10-20,41,290!2023-10-18,39,277-->
12. s→:::←u <!--SR:!2023-10-29,50,309!2023-10-30,51,309-->
13. u→:::←x, X <!--SR:!2023-10-24,45,289!2023-10-27,48,309-->
14. x, X→:::←_(end)_ <!--SR:!2023-10-30,51,309!2023-10-28,49,309-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
