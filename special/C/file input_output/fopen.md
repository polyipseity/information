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
# pytextgen generate module
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
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2025-07-18,499,310!2024-05-22,201,310-->
> - overload selection ::: use the `_s`-ending overloads whenever feasible <!--SR:!2025-04-23,406,377!2024-07-07,93,361-->
> - remember ::: call [`fclose`](fclose.md) on the file after you are done with it <!--SR:!2024-12-09,291,357!2024-07-06,92,361-->

## parameters

### modes

%%

```Python
# pytextgen generate data
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

<!--pytextgen generate section="ee2f"--><!-- The following content is generated at 2023-08-25T12:57:43.306675+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {{a}} | {{append}} |
> | {{a+}} | {{append extended}} |
> | {{r}} | {{read}} |
> | {{r+}} | {{read extended}} |
> | {{w}} | {{write}} |
> | {{w+}} | {{write extended}} | <!--SR:!2024-04-30,179,310!2024-05-17,196,310!2024-04-25,174,310!2024-05-25,204,310!2024-04-19,168,310!2026-03-03,690,330!2024-05-20,199,310!2026-02-22,683,330!2024-05-08,187,310!2024-04-21,170,310!2025-09-13,514,310!2024-05-04,183,310-->

<!--/pytextgen-->

<!--pytextgen generate section="b23d"--><!-- The following content is generated at 2024-01-04T20:17:58.525781+08:00. Any edits will be overridden! -->

- _(begin)_→:::←a <!--SR:!2024-04-25,174,310!2024-04-23,172,310-->
- a→:::←a+ <!--SR:!2024-05-04,183,310!2024-04-26,175,310-->
- a+→:::←r <!--SR:!2024-05-13,192,310!2025-09-04,507,310-->
- r→:::←r+ <!--SR:!2024-04-27,176,310!2024-05-13,192,310-->
- r+→:::←w <!--SR:!2026-02-10,673,330!2024-05-01,180,310-->
- w→:::←w+ <!--SR:!2024-05-16,195,310!2024-05-05,184,310-->
- w+→:::←_(end)_ <!--SR:!2024-05-08,187,310!2024-05-12,191,310-->

<!--/pytextgen-->

## return value

- 1) {{If successful, a pointer to the new file stream. On error, `NULL`.}}
- 2) {{If successful, `0` and writes a pointer to the new file stream into `*streamptr`. On error, non-zero error code and writes `NULL` into `*streamptr` unless `streamptr` is `NULL`.}} <!--SR:!2025-05-07,451,290!2025-03-17,342,250-->
