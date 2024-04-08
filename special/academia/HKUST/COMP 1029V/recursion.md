---
aliases:
  - VBA recursion
  - VBA recursions
tags:
  - flashcard/special/academia/HKUST/COMP_1029V/recursion
  - language/in/English
---

# VBA recursion

Recursion is all about {{reducing any problem to a simpler similar problem,  repeating this process until you get several base problems that are irreducible}}. <!--SR:!2024-05-04,72,310-->

Usually, we {{do not use recursion}} in VBA. But if it is required, it is as simple as {{conditionally calling the method itself in a method and adding base cases to the method}}. For example, a recursive way to calculate factorial: <!--SR:!2024-11-02,208,330!2024-04-15,56,310-->

```VB
Function Factorial(N):
  If N = 0 Then ' base case
    Factorial = 1
    Exit Function
  End If
  Factorial = N * Factorial(N - 1) ' call the function itself
End Function
```

## see also

- [general/recursion](../../../../general/recursion%20(computer%20science).md)
