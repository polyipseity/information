---
aliases:
  - Python function
  - Python functions
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/function
  - language/in/English
---

# Python function

A function {@{receives zero or more inputs and returns nothing or a output}@}. A Python function consists of {@{a name, arguments, and a statement block}@}: <!--SR:!2026-10-09,272,330!fsrs,2029-09-13T00:00:00.000Z,1111,1110.91195779,1,2,9,0,0,2026-08-29T00:00:00.000Z-->

```Python
def name(arguments):
  statement_block
```

This is an example of a function that takes in a number and returns the square of the number:

```Python
def square(x):
  return x * x
```

This is an example of a function that returns nothing. They are used for {@{side effects}@}: <!--SR:!2026-10-21,284,330-->

```Python
def print_square(x):
  print(x * x)
```
