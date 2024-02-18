---
aliases:
  - Python function
  - Python functions
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/function
  - language/in/English
---

# Python function

A function {{receives zero or more inputs and returns nothing or a output}}. A Python function consists of {{a name, arguments, and a statement block}}: <!--SR:!2024-02-19,14,290!2024-02-20,15,290-->

```Python
def name(arguments):
  statement_block
```

This is an example of a function that takes in a number and returns the square of the number:

```Python
def square(x):
  return x * x
```

This is an example of a function that returns nothing. They are used for {{side effects}}: <!--SR:!2024-04-09,51,310-->

```Python
def print_square(x):
  print(x * x)
```
