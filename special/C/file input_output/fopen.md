---
aliases:
  - "`fopen_s`"
  - "`fopen`"
  - fopen
  - fopen_s
tags:
  - flashcard/special/C/file_input_output/fopen
  - language/in/English
---

# `fopen`

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../tools/utility.py.md
```

%%

- _defined in {{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}}_ <!--SR:!2024-05-09,188,310-->

```C
// (1)
FILE *fopen(char const *filename, char const *mode); // (until C99)
FILE *fopen(char const *restrict filename, char const *restrict mode); // (since C99)
// (2)
errno_t fopen_s(FILE *restrict *restrict streamptr,
                char const *restrict filename,
                char const *restrict mode); // (since C11)
```

> [!tip] tips
>
> - {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}}
> - overload selection: {{use the `_s`-ending overloads whenever feasible}}
> - remember: {{call [`fclose`](fclose.md) on the file after you are done with it}} <!--SR:!2025-07-18,499,310!2024-05-22,201,310!2024-03-12,83,357!2024-12-09,291,357-->

## parameters

### modes

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
options = {
  "a": "append",
  "a+": "append extended",
  "r": "read",
  "r+": "read extended",
  "w": "write",
  "w+": "write extended",
}
return await memorize_table(
  __env__.cwf_sects("ee2f", "b23d"),
  ("character", "description"),
  options.items(),
  partial(map, cloze),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee2f"--><!-- The following content is generated at 2023-08-25T12:57:43.306675+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{a}} | {{append}} |
> | {{a+}} | {{append extended}} |
> | {{r}} | {{read}} |
> | {{r+}} | {{read extended}} |
> | {{w}} | {{write}} |
> | {{w+}} | {{write extended}} | <!--SR:!2024-04-30,179,310!2024-05-17,196,310!2024-04-25,174,310!2024-05-25,204,310!2024-04-19,168,310!2024-04-12,161,310!2024-05-20,199,310!2024-04-10,159,310!2024-05-08,187,310!2024-04-21,170,310!2024-04-17,166,310!2024-05-04,183,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b23d"--><!-- The following content is generated at 2024-01-04T20:17:58.525781+08:00. Any edits will be overridden! -->

- _(begin)_→:::←a <!--SR:!2024-04-25,174,310!2024-04-23,172,310-->
- a→:::←a+ <!--SR:!2024-05-04,183,310!2024-04-26,175,310-->
- a+→:::←r <!--SR:!2024-05-13,192,310!2024-04-15,164,310-->
- r→:::←r+ <!--SR:!2024-04-27,176,310!2024-05-13,192,310-->
- r+→:::←w <!--SR:!2024-04-08,157,310!2024-05-01,180,310-->
- w→:::←w+ <!--SR:!2024-05-16,195,310!2024-05-05,184,310-->
- w+→:::←_(end)_ <!--SR:!2024-05-08,187,310!2024-05-12,191,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## return value

- 1) {{If successful, a pointer to the new file stream. On error, `NULL`.}}
- 2) {{If successful, `0` and writes a pointer to the new file stream into `*streamptr`. On error, non-zero error code and writes `NULL` into `*streamptr` unless `streamptr` is `NULL`.}} <!--SR:!2025-05-07,451,290!2024-04-09,137,250-->
