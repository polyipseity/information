---
aliases:
  - Python string
  - Python strings
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/string
  - language/in/English
---

# Python string

## formatting

There are {@{4 main ways}@} to {@{format a string with values}@} in Python: {@{C formatting, f-string, string concatenation, and `str.format`}@}. <!--SR:!2026-09-26,259,330!2026-09-30,263,330!2026-10-09,272,330-->

### f-string

{@{f-string}@} starts the string with {@{`f` before the starting quote `"`}@}. Then use {@{`{variableName}`}@} to {@{print a value in the middle of the string}@}. To {@{literally represent `{}`}@}, use {@{`{{}}`}@}. <!--SR:!2026-10-05,268,330!2026-10-08,271,330!2026-10-11,274,330!2026-09-30,263,330!2026-10-04,267,330!2026-10-04,267,330-->

### string concatenation

String concatenation uses {@{`+`}@} to {@{concat strings and values converted to strings}@}. This is the {@{most cumbersome way}@} and usually is {@{the least efficient}@} as well. <!--SR:!2026-09-30,263,330!2026-10-31,294,330!2026-10-15,278,330!2026-10-26,289,330-->

### `str.format`

`str.format` replaces {@{each `{}` in the string}@} by {@{each argument passed to `str.format` in the order of passing}@}. There are {@{more advanced usage}@} not mentioned here. <!--SR:!2026-10-27,290,330!2026-10-27,290,330!2026-10-17,280,330-->

## functions

- `<str>.count(<substr>)` ::@:: Count the number of _non-overlapping_ occurrences of `<substr>` in `<str>`. <!--SR:!2026-10-13,276,330!2026-10-12,275,330-->
- `<str>.find(<substr>)` ::@:: Get the index of the _first_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2026-10-26,289,330!2026-10-30,293,330-->
- `<str>.lower()` ::@:: Converts all characters of `<str>` to lowercase. <!--SR:!2026-09-25,258,330!2026-10-18,281,330-->
- `<str>.replace(<substr>, <replacement>)` ::@:: Replace _all non-overlapping_ occurrences of `<substr>` in `<str>` with `<replacement>`. <!--SR:!2026-10-20,283,330!2026-09-26,259,330-->
- `<str>.rfind(<substr>)` ::@:: Get the index of the _last_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2026-10-19,282,330!2026-10-16,279,330-->
- `<str>.split(<splitter> = None)` ::@:: If `<splitter>` is not `None` \(by specifying the argument\), split `<str>` into a `list` by `<splitter>`. Splitting an empty `<str>` yields a `list` containing an empty `str`. If `<splitter>` is an empty `str`, raise `ValueError`. <p> If `<splitter>` is `None`, split `<str>` into a `list` by consecutive whitespaces. Splitting an empty `<str>` yields an empty `list`. <!--SR:!2026-06-26,195,310!2026-04-29,153,310-->
- `<str>.upper()` ::@:: Converts all characters of `<str>` to uppercase. <!--SR:!2026-10-28,291,330!2026-10-10,273,330-->
