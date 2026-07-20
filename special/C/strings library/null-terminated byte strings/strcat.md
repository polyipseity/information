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

- _defined in {@{[`<string.h>`](../../../../general/C%20string%20handling.md)}@}_ <!--SR:!fsrs,2034-09-30T00:00:00.000Z,3011,3011.49640457,1,2,11,0,0,2026-07-03T00:00:00.000Z-->

```C
// (1)
char *strcat(char *dest, char const *src); // (until C99)
char *strcat(char *restrict dest, char const *restrict src); // (since C99)
// (2)
errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src); // (since C11)
```

> [!tip] tips
>
> - `_CRT_SECURE_NO_WARNINGS` ([Visual Studio](Visual%20Studio.md)) ::@:: define to `1` to disable errors from using non-`_s`-ending functions <!--SR:!2035-06-06,3326,350!fsrs,2034-12-25T00:00:00.000Z,3075,3075.11619593,1,2,11,0,0,2026-07-25T00:00:00.000Z-->
> - `destsz` ::@:: includes [null terminator](null-terminated%20string) <!--SR:!2028-12-04,1444,368!2030-10-28,1923,381-->
> - overload selection ::@:: use the `_s`-ending overloads whenever feasible <!--SR:!2028-05-04,1276,368!2030-09-29,1899,381-->
