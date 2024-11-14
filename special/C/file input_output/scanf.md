---
aliases:
  - "`fscanf_s`"
  - "`fscanf`"
  - "`scanf_s`"
  - "`scanf`"
  - "`sscanf_s`"
  - "`sscanf`"
  - fscanf
  - fscanf_s
  - scanf
  - scanf_s
  - sscanf
  - sscanf_s
tags:
  - flashcard/active/special/C/file_intput_output/scanf
  - language/in/English
---

# `scanf`

- _defined in {@{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}@}_

```C
// (1)
int scanf(char const *format, ...); // (until C99)
int scanf(char const *restrict format, ...); // (since C99)
// (2)
int fscanf(FILE *stream, char const *format, ...); // (until C99)
int fscanf(FILE *restrict stream, char const *restrict format, ...); // (since C99)
// (3)
int sscanf(char const *buffer, char const *format, ...); // (until C99)
int sscanf(char const *restrict buffer, char const *restrict format, ...); // (since C99)
// (4)
int scanf_s(char const *restrict format, ...); // (since C11)
// (5)
int fscanf_s(FILE *restrict stream, char const *restrict format, ...); // (since C11)
// (6)
int sscanf_s(char const *restrict buffer, char const *restrict format, ...); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible

## parameters

### placeholder

See [`scanf` § placeholder](../../../general/scanf.md#placeholder).

## return value

- (1-3) :@: Number of arguments assigned, or [`EOF`](../file%20input_output.md) if input failure occurs before assigning the first argument.
- (4-6) :@: Same as (1-3), returning [`EOF`](../file%20input_output.md) also on runtime constraint violation.
