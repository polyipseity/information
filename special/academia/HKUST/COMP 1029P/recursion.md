---
aliases:
  - Python recursion
  - Python recursions
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/recursion
  - language/in/English
---

# Python recursion

Recursion is all about {@{reducing any problem to a simpler similar problem,  repeating this process until you get several base problems that are irreducible}@}.

Usually, we {@{do not use recursion}@} in Python. But if it is required, it is as simple as {@{conditionally calling the method itself in a method and adding base cases to the method}@}. For example, a recursive way to calculate factorial:

```Python
def factorial(n):
  if n == 0: return 1 # base case
  return n * factorial(n - 1) # call the function itself
```

## see also

- [general/recursion](../../../../general/recursion%20(computer%20science).md)
