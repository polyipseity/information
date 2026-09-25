---
aliases:
  - Python variable
  - Python variables
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/variable
  - language/in/English
---

# Python variable

## scope

In Python, unlike most other languages, an indentation, which corresponds to curly braces `{}` in other languages, {@{does not necessarily create a new scope}@}: <!--SR:!fsrs,2030-04-19T00:00:00.000Z,1267,1267.08647061,1,2,9,0,0,2026-10-30T00:00:00.000Z-->

```Python
if condition:
  x = 1
else:
  x = 2
print(x) # `x` does not go out of scope as an `if...else` statement does not create a scope in the first place
```

Functions do create {@{a new scope}@}: <!--SR:!fsrs,2029-11-22T00:00:00.000Z,1149,1149.27403969,1,2,9,0,0,2026-09-30T00:00:00.000Z-->

```Python
x = 1
def print_x(y):
  x = y # creates a new variable `x` in function scope instead of assigning to `x`
  print(x)
print_x(2) # prints 2 instead of 1
print(x) # prints 1 as the global `x` is unchanged
```
