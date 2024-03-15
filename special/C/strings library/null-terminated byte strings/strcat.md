---
aliases:
  - "`strcat_s`"
  - "`strcat`"
  - strcat
  - strcat_s
tags:
  - flashcard/special/C/strings_library/null-terminated_byte_strings/strcat
  - language/in/English
---

# `strcat`

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_ <!--SR:!2024-05-05,184,310-->

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2024-04-22,171,310!2024-05-09,188,310-->
> - `destsz` ::: includes [null terminator](null-terminated%20string) <!--SR:!2024-12-21,302,348!2024-04-03,19,321-->
> - overload selection ::: use the `_s`-ending overloads whenever feasible <!--SR:!2024-11-05,266,348!2024-04-03,19,321-->
