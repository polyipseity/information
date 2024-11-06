---
aliases:
  - standard output
  - stdout
tags:
  - flashcard/active/special/standard_output
  - language/in/English
---

# standard output

## buffering

The standard output is {{usually [line-buffered](../general/data%20buffer.md), so writing a [newline](../general/newline.md) `\n` is needed to flush it}}. That means while `printf("text\n")` shows `text` immediately, {{`printf("\ntext")` may not and may never will until an extra `\n` is written by another call to `printf`}}.
