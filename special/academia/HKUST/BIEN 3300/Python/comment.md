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

In Python, comments start {@{with `#` and end at end of line}@}: <!--SR:!fsrs,2029-10-03T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-03T00:00:00.000Z-->

```Python
a = 1 # assign 1 to `a`
a += 1 # increment `a` by 1
```

If you want multiline comments, you can use {@{multiline strings to emulate it}@}: <!--SR:!fsrs,2029-12-27T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-08T00:00:00.000Z-->

```Python
a = 1
"""
This is actually a multiline string. But since the string is not being used, so it is effectively a multiline comment.
Anyway, the code above and below assigns 1 to `a` and then increment `a` by 1.
"""
a += 1
```

## docstring

Docstrings {@{are documentations for classes and functions}@}. To add a docstring, {@{add a multiline comment right below the start of the class or function}@}: <!--SR:!fsrs,2029-07-25T00:00:00.000Z,1072,1072.36160804,1,2,9,0,0,2026-08-18T00:00:00.000Z!2026-11-03,294,330-->

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
