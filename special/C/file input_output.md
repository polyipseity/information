---
aliases:
  - EOF
  - "`EOF`"
  - file input/output
tags:
  - flashcard/active/special/C/file_input_output
  - language/in/English
---

# file input/output

## types

- _defined in {@{[`<stdio.h>`](../../general/C%20file%20input_output.md)}@}_
- [`FILE`](file%20input_output/FILE.md) <!--SR:!2026-04-27,734,330-->

## functions

### file access

- _defined in {@{[`<stdio.h>`](../../general/C%20file%20input_output.md)}@}_
- [`fclose`](file%20input_output/fclose.md)
- [`fopen`, `fopen_s`](file%20input_output/fopen.md) <!--SR:!2026-06-11,771,330-->

### formatted input/output

- _defined in {@{[`<stdio.h>`](../../general/C%20file%20input_output.md)}@}_
- [`fscanf`, `fscanf_s`, `scanf`, `scanf_s`, `sscanf`, `sscanf_s`](file%20input_output/scanf.md)
- [`fprintf`, `fprintf_s`, `printf`, `printf_s`, `snprintf`, `snprintf_s`, `sprintf`, `sprintf_s`](file%20input_output/printf.md) <!--SR:!2026-05-22,754,330-->

## macro constants

- _defined in {@{[`<stdio.h>`](../../general/C%20file%20input_output.md)}@}_ <!--SR:!2024-05-05,184,310-->
- `EOF` ::@:: negative `int` constant expression indicating end-of-file <!--SR:!2029-12-01,1741,330!2029-01-29,1409,372-->
