---
aliases:
  - Python variable
  - Python variables
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/variable
  - language/in/English
---

# Python variable

## scope

In Python, unlike most other languages, an indentation, which corresponds to curly braces `{}` in other languages, {@{does not necessarily create a new scope}@}: <!--SR:!2025-01-30,278,330-->

```Python
if condition:
  x = 1
else:
  x = 2
print(x) # `x` does not go out of scope as an `if...else` statement does not create a scope in the first place
```

Functions do create {@{a new scope}@}: <!--SR:!2024-11-16,203,310-->

```Python
x = 1
def print_x(y):
  x = y # creates a new variable `x` in function scope instead of assigning to `x`
  print(x)
print_x(2) # prints 2 instead of 1
print(x) # prints 1 as the global `x` is unchanged
```
