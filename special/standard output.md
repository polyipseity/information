---
aliases:
  - standard output
  - stdout
tags:
  - flashcards/special/standard_output
---

# standard output

## buffering

The standard output is {{usually [line-buffered](../general/data%20buffer.md), so writing a [newline](../general/newline.md) `\n` is needed to flush it}}. That means while `printf("text\n")` shows `text` immediately, {{`printf("\ntext")` may not and may never will until a `\n` is written}}.