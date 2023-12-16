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

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_ <!--SR:!2024-05-05,184,310-->

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src); // (since C11)
```


> [!tip]
>
> - {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}}
> - `destsz`: {{includes [null terminator](null-terminated%20string)}}
> - overload selection: {{use the `_s`-ending overloads whenever feasible}} <!--SR:!2024-04-22,171,310!2024-05-09,188,310!2023-12-18,16,308!2024-02-13,59,328-->
