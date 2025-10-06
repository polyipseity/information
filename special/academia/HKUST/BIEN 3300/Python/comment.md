---
aliases:
  - Python comment
  - Python comments
  - Python docstring
  - Python docstrings
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/comment
  - language/in/English
---

# Python comment

## comment

In Python, comments start {@{with `#` and end at end of line}@}: <!--SR:!2025-12-21,58,310-->

```Python
a = 1 # assign 1 to `a`
a += 1 # increment `a` by 1
```

If you want multiline comments, you can use {@{multiline strings to emulate it}@}: <!--SR:!2025-10-25,15,290-->

```Python
a = 1
"""
This is actually a multiline string. But since the string is not being used, so it is effectively a multiline comment.
Anyway, the code above and below assigns 1 to `a` and then increment `a` by 1.
"""
a += 1
```

## docstring

Docstrings {@{are documentations for classes and functions}@}. To add a docstring, {@{add a multiline comment right below the start of the class or function}@}: <!--SR:!2025-12-19,56,310!2025-10-26,16,290-->

```Python
class A:
  """
  This is a class named `A`. And this is the docstring for it.
  """

def a(self):
  """
  This is a function named `a`. And this is the docstring for it.
  """
```
