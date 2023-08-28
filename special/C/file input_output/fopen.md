---
aliases:
  - "`fopen_s`"
  - "`fopen`"
  - fopen
  - fopen_s
tags:
  - flashcards/special/C/file_input_output/fopen
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../tools/utility.py.md
```
%%

# `fopen`

- _defined in {{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}}_
- {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}} <!--SR:!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270-->

```C
// (1)
FILE *fopen(char const *filename, char const *mode); // (until C99)
FILE *fopen(char const *restrict filename, char const *restrict mode); // (since C99)
// (2)
errno_t fopen_s(FILE *restrict *restrict streamptr,
                char const *restrict filename,
                char const *restrict mode); // (since C11)
```

## parameters

### modes

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from functools import partial
e = __env__
options = {
	"a": "append",
	"a+": "append extended",
	"r": "read",
	"r+": "read extended",
	"w": "write",
	"w+": "write extended",
}
return await memorize_table(
	e.cwf_sects("ee2f", "b23d"),
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
> | {{w+}} | {{write extended}} | <!--SR:!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b23d"--><!-- The following content is generated at 2023-08-25T12:57:45.196310+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←a <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
2. a→:::←a+ <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
3. a+→:::←r <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
4. r→:::←r+ <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
5. r+→:::←w <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
6. w→:::←w+ <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->
7. w+→:::←_(end)_ <!--SR:!2023-09-01,4,270!2023-09-01,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## return value

- 1) {{If successful, a pointer to the new file stream if successful. On error, `NULL`.}}
- 2) {{If successful, `0` and writes a pointer to the new file stream into `*streamptr`. On error, non-zero error code and writes `NULL` into `*streamptr` unless `streamptr` is `NULL`.}} <!--SR:!2023-08-29,1,230!2023-08-31,3,250-->
