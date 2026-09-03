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

There are {@{4 main ways}@} to {@{format a string with values}@} in Python: {@{C formatting, f-string, string concatenation, and `str.format`}@}. <!--SR:!fsrs,2029-11-12T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-09-27T00:00:00.000Z!fsrs,2029-12-01T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-01T00:00:00.000Z!fsrs,2030-01-12T00:00:00.000Z,1191,1191.26470738,1,2,9,0,0,2026-10-09T00:00:00.000Z-->

### f-string

{@{f-string}@} starts the string with {@{`f` before the starting quote `"`}@}. Then use {@{`{variableName}`}@} to {@{print a value in the middle of the string}@}. To {@{literally represent `{}`}@}, use {@{`{{}}`}@}. <!--SR:!fsrs,2029-12-24T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-05T00:00:00.000Z!fsrs,2030-01-07T00:00:00.000Z,1187,1187.45608877,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2030-01-22T00:00:00.000Z,1199,1198.87680538,1,2,9,0,0,2026-10-11T00:00:00.000Z!fsrs,2029-12-01T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-01T00:00:00.000Z!fsrs,2029-12-19T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-04T00:00:00.000Z!fsrs,2029-12-19T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-04T00:00:00.000Z-->

### string concatenation

String concatenation uses {@{`+`}@} to {@{concat strings and values converted to strings}@}. This is the {@{most cumbersome way}@} and usually is {@{the least efficient}@} as well. <!--SR:!fsrs,2029-12-01T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-01T00:00:00.000Z!2026-10-31,294,330!2026-10-15,278,330!2026-10-26,289,330-->

### `str.format`

`str.format` replaces {@{each `{}` in the string}@} by {@{each argument passed to `str.format` in the order of passing}@}. There are {@{more advanced usage}@} not mentioned here. <!--SR:!2026-10-27,290,330!2026-10-27,290,330!2026-10-17,280,330-->

## functions

- `<str>.count(<substr>)` ::@:: Count the number of _non-overlapping_ occurrences of `<substr>` in `<str>`. <!--SR:!2026-10-13,276,330!2026-10-12,275,330-->
- `<str>.find(<substr>)` ::@:: Get the index of the _first_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2026-10-26,289,330!2026-10-30,293,330-->
- `<str>.lower()` ::@:: Converts all characters of `<str>` to lowercase. <!--SR:!fsrs,2029-11-07T00:00:00.000Z,1138,1137.78464757,1,2,9,0,0,2026-09-26T00:00:00.000Z!2026-10-18,281,330-->
- `<str>.replace(<substr>, <replacement>)` ::@:: Replace _all non-overlapping_ occurrences of `<substr>` in `<str>` with `<replacement>`. <!--SR:!2026-10-20,283,330!fsrs,2029-11-12T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-09-27T00:00:00.000Z-->
- `<str>.rfind(<substr>)` ::@:: Get the index of the _last_ occurrence of `<substr>` in `<str>`, or raise `ValueError` if not found. <!--SR:!2026-10-19,282,330!2026-10-16,279,330-->
- `<str>.split(<splitter> = None)` ::@:: If `<splitter>` is not `None` \(by specifying the argument\), split `<str>` into a `list` by `<splitter>`. Splitting an empty `<str>` yields a `list` containing an empty `str`. If `<splitter>` is an empty `str`, raise `ValueError`. <p> If `<splitter>` is `None`, split `<str>` into a `list` by consecutive whitespaces. Splitting an empty `<str>` yields an empty `list`. <!--SR:!fsrs,2028-10-05T00:00:00.000Z,831,830.79438507,1,2,9,0,0,2026-06-27T00:00:00.000Z!2028-02-21,662,330-->
- `<str>.upper()` ::@:: Converts all characters of `<str>` to uppercase. <!--SR:!2026-10-28,291,330!fsrs,2030-01-17T00:00:00.000Z,1195,1195.07164214,1,2,9,0,0,2026-10-10T00:00:00.000Z-->
