---
aliases:
  - "`fprintf_s`"
  - "`fprintf`"
  - "`printf_s`"
  - "`printf`"
  - "`snprintf_s`"
  - "`snprintf`"
  - "`sprintf_s`"
  - "`sprintf`"
  - fprintf
  - fprintf_s
  - printf
  - printf_s
  - snprintf
  - snprintf_s
  - sprintf
  - sprintf_s
tags:
  - flashcards/special/C/file_intput_output/printf
---

# `printf`

- _defined in {{[`<stdio.h>`](../../../general/C%20file%20input_output.md)}}_
- {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}}

```C
// (1)
int printf(char const *format, ...); // (until C99)
int printf(char const *restrict format, ...); // (since C99)
// (2)
int fprintf(FILE *stream, char const *format, ...); // (until C99)
int fprintf(FILE *restrict stream, char const *restrict format, ...); // (since C99)
// (3)
int sprintf(char const *buffer, char const *format, ...); // (until C99)
int sprintf(char const *restrict buffer, char const *restrict format, ...); // (since C99)
// (4)
int snprintf(char const *restrict buffer, size_t bufsz, char const *restrict format, ...); // (since C99)
// (5)
int printf_s(char const *restrict format, ...); // (since C11)
// (6)
int fprintf_s(FILE *restrict stream, char const *restrict format, ...); // (since C11)
// (7)
int sprintf_s(char const *restrict buffer, rsize_t bufsz, char const *restrict format, ...); // (since C11)
// (8)
int snprintf_s(char const *restrict buffer, rsize_t bufsz, char const *restrict format, ...); // (since C11)
```

## parameters

### placeholder

See [`printf` § placeholder](../../../general/printf.md#placeholder).