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
# import ../../../tools/utility.py.md
```

- _defined in {@{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}@}_

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
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible
> - remember ::@:: call [`fclose`](fclose.md) on the file after you are done with it

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

<!--pytextgen generate section="ee2f"--><!-- The following content is generated at 2026-01-25T23:32:21.201126+08:00. Any edits will be overridden! -->

> | character | description           |
> | --------- | --------------------- |
> | {@{a}@}   | {@{append}@}          |
> | {@{a+}@}  | {@{append extended}@} |
> | {@{r}@}   | {@{read}@}            |
> | {@{r+}@}  | {@{read extended}@}   |
> | {@{w}@}   | {@{write}@}           |
> | {@{w+}@}  | {@{write extended}@}  |

<!--/pytextgen-->

<!--pytextgen generate section="b23d"--><!-- The following content is generated at 2024-01-04T20:17:58.525781+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←a
- a→::@::←a+
- a+→::@::←r
- r→::@::←r+
- r+→::@::←w
- w→::@::←w+
- w+→::@::←_(end)_

<!--/pytextgen-->

## return value

- (1) :@: If successful, a pointer to the new file stream. On error, `NULL`.
- (2) :@: If successful, `0` and writes a pointer to the new file stream into `*streamptr`. On error, non-zero error code and writes `NULL` into `*streamptr` unless `streamptr` is `NULL`.
