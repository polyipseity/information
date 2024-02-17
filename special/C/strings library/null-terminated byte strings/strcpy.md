---
aliases:
  - "`strcpy_s`"
  - "`strcpy`"
  - strcpy
  - strcpy_s
tags:
  - flashcard/special/C/strings_library/null-terminated_byte_strings/strcpy
  - language/in/English
---

# `strcpy`

- _defined in {{[`<string.h>`](../../../../general/C%20string%20handling.md)}}_

```C
// (1)
char *strcpy(char *dest, char const *src); // (until C99)
char *strcpy(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcpy_s(char *restrict dest, rsize_t destsz, const char *restrict stc); // (since C11)
```

> [!tip] tip
>
> - {{`_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md))}}: {{define to `1` to disable errors from using non-`_s`-ending functions}}
> - `destsz`: {{includes [null terminator](null-terminated%20string)}}
> - overload selection: {{use the `_s`-ending overloads whenever feasible}}
