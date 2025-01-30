---
aliases:
  - "`strcpy_s`"
  - "`strcpy`"
  - strcpy
  - strcpy_s
tags:
  - flashcard/active/special/C/strings_library/null-terminated_byte_strings/strcpy
  - language/in/English
---

# `strcpy`

- _defined in {@{[`<string.h>`](../../../../general/C%20string%20handling.md)}@}_ <!--SR:!2026-04-12,723,330-->

```C
// (1)
char *strcpy(char *dest, char const *src); // (until C99)
char *strcpy(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcpy_s(char *restrict dest, rsize_t destsz, const char *restrict stc); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2026-10-06,866,330!2025-08-11,489,310-->
> - `destsz` ::@:: includes [null terminator](null-terminated%20string) <!--SR:!2027-05-24,972,348!2025-06-20,363,359-->
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible <!--SR:!2029-06-21,1603,368!2025-07-18,386,359-->
