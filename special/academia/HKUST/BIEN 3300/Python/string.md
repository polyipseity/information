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

There are {@{4 main ways}@} to {@{format a string with values}@} in Python: {@{C formatting, f-string, string concatenation, and `str.format`}@}. <!--SR:!2025-12-23,59,310!2025-12-24,60,310!2025-12-26,62,310-->

### f-string

{@{f-string}@} starts the string with {@{`f` before the starting quote `"`}@}. Then use {@{`{variableName}`}@} to {@{print a value in the middle of the string}@}. To {@{literally represent `{}`}@}, use {@{`{{}}`}@}. <!--SR:!2025-12-25,61,310!2025-12-26,62,310!2025-12-27,63,310!2025-12-24,60,310!2025-12-25,61,310!2025-12-25,61,310-->

### string concatenation

String concatenation uses {@{`+`}@} to {@{concat strings and values converted to strings}@}. This is the {@{most cumbersome way}@} and usually is {@{the least efficient}@} as well. <!--SR:!2025-12-24,60,310!2025-10-26,16,290!2025-10-26,16,290!2025-10-26,16,290-->

### `str.format`

`str.format` replaces {@{each `{}` in the string}@} by {@{each argument passed to `str.format` in the order of passing}@}. There are {@{more advanced usage}@} not mentioned here. <!--SR:!2025-10-26,16,290!2025-10-26,16,290!2025-10-26,16,290-->

## functions

- `<str>.count(<substr>)` ::@:: Count the number of _non-overlapping_ occurrences of `<substr>` in `<str>`. <!--SR:!2025-12-27,63,310!2025-10-26,16,290-->
- `<str>.find(<substr>)` ::@:: Get the index of the _first_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2025-10-26,16,290!2025-10-26,16,290-->
- `<str>.lower()` ::@:: Converts all characters of `<str>` to lowercase. <!--SR:!2025-12-23,59,310!2025-10-26,16,290-->
- `<str>.replace(<substr>, <replacement>)` ::@:: Replace _all non-overlapping_ occurrences of `<substr>` in `<str>` with `<replacement>`. <!--SR:!2025-10-26,16,290!2025-12-23,59,310-->
- `<str>.rfind(<substr>)` ::@:: Get the index of the _last_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2025-10-26,16,290!2025-10-26,16,290-->
- `<str>.split(<splitter> = None)` ::@:: If `<splitter>` is not `None` \(by specifying the argument\), split `<str>` into a `list` by `<splitter>`. Splitting an empty `<str>` yields a `list` containing an empty `str`. If `<splitter>` is an empty `str`, raise `ValueError`. <p> If `<splitter>` is `None`, split `<str>` into a `list` by consecutive whitespaces. Splitting an empty `<str>` yields an empty `list`. <!--SR:!2025-10-26,16,290!2025-11-27,38,290-->
- `<str>.upper()` ::@:: Converts all characters of `<str>` to uppercase. <!--SR:!2025-10-26,16,290!2025-12-27,63,310-->
