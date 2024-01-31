---
aliases:
  - Python function
  - Python functions
tags:
  - flashcards/special/academia/HKUST/COMP_1029P/function
  - languages/in/English
---

# Python function

A function {{receives zero or more inputs and returns nothing or a output}}. A Python consists of {{a name, arguments, and statements}}:

```Python
def name(arguments):
  statements
```

This is an example of a function that takes in a number and returns the square of the number:

```Python
def square(x):
  return x * x
```

This is an example of a function that returns nothing. They are used for {{side effects}}:

```Python
def print_square(x):
  print(x * x)
```
