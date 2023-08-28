---
aliases:
  - "`strcpy_s`"
  - "`strcpy`"
  - strcpy
  - strcpy_s
tags:
  - flashcards/special/C/strings_library/null-terminated_byte_strings/strcpy
---

# `strcpy`

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_
- {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}} <!--SR:!2023-09-01,4,270!2023-09-01,4,270!2023-09-01,4,270-->

```C
// (1)
char *strcpy(char *dest, char const *src); // (until C99)
char *strcpy(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcpy_s(char *restrict dest, rsize_t destsz, const char *restrict stc); // (since C11)
```
