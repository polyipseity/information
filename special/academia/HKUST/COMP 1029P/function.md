---
aliases:
  - Python function
  - Python functions
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/function
  - language/in/English
---

# Python function

A function {{receives zero or more inputs and returns nothing or a output}}. A Python function consists of {{a name, arguments, and a statement block}}: <!--SR:!2025-01-05,261,330!2026-10-28,750,330-->

```Python
def name(arguments):
  statement_block
```

This is an example of a function that takes in a number and returns the square of the number:

```Python
def square(x):
  return x * x
```

This is an example of a function that returns nothing. They are used for {{side effects}}: <!--SR:!2027-06-30,965,350-->

```Python
def print_square(x):
  print(x * x)
```
