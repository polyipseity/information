---
aliases:
  - EOF
  - "`EOF`"
  - file input/output
tags:
  - flashcards/special/C/file_input_output
---

# file input/output

## types

- _defined in {{[`<stdio.h>`](../../general/C%20file%20input_output.md)}}_
- [`FILE`](file%20input_output/FILE.md) <!--SR:!2023-10-22,43,290-->

## functions

### file access

- _defined in {{[`<stdio.h>`](../../general/C%20file%20input_output.md)}}_
- [`fclose`](file%20input_output/fclose.md)
- [`fopen`, `fopen_s`](file%20input_output/fopen.md) <!--SR:!2023-10-24,45,290-->

### formatted input/output

- _defined in {{[`<stdio.h>`](../../general/C%20file%20input_output.md)}}_
- [`fscanf`, `fscanf_s`, `scanf`, `scanf_s`, `sscanf`, `sscanf_s`](file%20input_output/scanf.md)
- [`fprintf`, `fprintf_s`, `printf`, `printf_s`, `snprintf`, `snprintf_s`, `sprintf`, `sprintf_s`](file%20input_output/printf.md) <!--SR:!2023-10-23,44,290-->

## macro constants

- _defined in {{[`<stdio.h>`](../../general/C%20file%20input_output.md)}}_
- `EOF`: {{negative `int` constant expression}} <!--SR:!2023-10-25,46,290!2024-01-15,101,290-->
