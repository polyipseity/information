---
aliases:
  - "`fopen_s`"
  - "`fopen`"
  - fopen
  - fopen_s
tags:
  - flashcard/active/special/C/file_input_output/fopen
  - language/in/English
---

# `fopen`

```Python
# pytextgen generate module
# import ../../../../tools/utility.py.md
```

- _defined in {@{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}@}_ <!--SR:!2026-07-22,804,330-->

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
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2031-05-29,2141,330!2026-09-30,861,330-->
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible <!--SR:!2031-01-17,2095,397!2025-10-10,460,381-->
> - remember ::@:: call [`fclose`](fclose.md) on the file after you are done with it <!--SR:!2028-11-04,1425,377!2029-11-28,1639,381-->

## parameters

### modes

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

<!--pytextgen generate section="ee2f"--><!-- The following content is generated at 2023-08-25T12:57:43.306675+08:00. Any edits will be overridden! -->

> | character | description |
> |-|-|
> | {@{a}@} | {@{append}@} |
> | {@{a+}@} | {@{append extended}@} |
> | {@{r}@} | {@{read}@} |
> | {@{r+}@} | {@{read extended}@} |
> | {@{w}@} | {@{write}@} |
> | {@{w+}@} | {@{write extended}@} | <!--SR:!2026-06-08,769,330!2026-09-09,840,330!2026-05-10,745,330!2026-10-16,874,330!2026-04-11,722,330!2026-03-03,690,330!2026-09-22,853,330!2026-02-22,683,330!2026-07-19,801,330!2026-04-20,728,330!2025-09-13,514,310!2026-06-26,783,330-->

<!--/pytextgen-->

<!--pytextgen generate section="b23d"--><!-- The following content is generated at 2024-01-04T20:17:58.525781+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←a <!--SR:!2026-05-09,744,330!2026-04-30,737,330-->
- a→::@::←a+ <!--SR:!2026-06-27,784,330!2026-05-19,752,330-->
- a+→::@::←r <!--SR:!2026-08-14,823,330!2025-09-04,507,310-->
- r→::@::←r+ <!--SR:!2026-05-21,754,330!2026-08-13,822,330-->
- r+→::@::←w <!--SR:!2026-02-10,673,330!2026-06-09,769,330-->
- w→::@::←w+ <!--SR:!2026-08-30,836,330!2026-07-03,788,330-->
- w+→::@::←_(end)_ <!--SR:!2026-07-18,800,330!2026-08-09,818,330-->

<!--/pytextgen-->

## return value

- (1) :@: If successful, a pointer to the new file stream. On error, `NULL`. <!--SR:!2028-12-06,1308,290-->
- (2) :@: If successful, `0` and writes a pointer to the new file stream into `*streamptr`. On error, non-zero error code and writes `NULL` into `*streamptr` unless `streamptr` is `NULL`. <!--SR:!2027-07-26,860,250-->
