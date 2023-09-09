---
aliases:
  - "`strcat_s`"
  - "`strcat`"
  - strcat
  - strcat_s
tags:
  - flashcards/special/C/strings_library/null-terminated_byte_strings/strcat
---

# `strcat`

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_
- {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}} <!--SR:!2023-10-25,46,290!2023-10-22,43,290!2023-10-26,47,290-->

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict stc); // (since C11)
```
