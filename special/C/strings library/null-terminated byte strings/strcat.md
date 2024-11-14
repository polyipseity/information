---
aliases:
  - "`strcat_s`"
  - "`strcat`"
  - strcat
  - strcat_s
tags:
  - flashcard/active/special/C/strings_library/null-terminated_byte_strings/strcat
  - language/in/English
---

# `strcat`

- _defined in {@{[`<string.h>`](../../../../general/C%20string%20handling.md)}@}_

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions
> - `destsz` ::@:: includes [null terminator](null-terminated%20string)
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible
