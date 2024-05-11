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

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_ <!--SR:!2026-07-02,787,330-->

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2026-04-24,732,330!2026-07-24,806,330-->
> - `destsz` ::: includes [null terminator](null-terminated%20string) <!--SR:!2024-12-21,302,348!2024-06-25,83,341-->
> - overload selection ::: use the `_s`-ending overloads whenever feasible <!--SR:!2024-11-05,266,348!2024-06-24,82,341-->
