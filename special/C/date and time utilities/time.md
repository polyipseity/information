---
aliases:
  - "`time`"
  - time
tags:
  - flashcard/special/C/date_and_time_utilities/time
  - language/in/English
---

# `time`

- _defined in {{[`<time.h>`](../../../general/C%20date%20and%20time%20functions.md)}}_ <!--SR:!2024-10-29,257,331-->

```C
time_t time(time_t *arg);
```

> [!tip] tips
>
> - two ways to get the result ::: [return value](../../../general/return%20statement.md) (pass `NULL` to `arg`), `arg` [output parameter](../../../general/parameter%20(computer%20programming).md#output%20parameters) <!--SR:!2026-01-16,549,316!2025-05-20,336,346-->
