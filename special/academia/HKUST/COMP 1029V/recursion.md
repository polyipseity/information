---
aliases:
  - VBA recursion
  - VBA recursions
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/recursion
  - language/in/English
---

# VBA recursion

Recursion is all about {@{reducing any problem to a simpler similar problem,  repeating this process until you get several base problems that are irreducible}@}. <!--SR:!2027-07-12,944,330-->

Usually, we {@{do not use recursion}@} in VBA. But if it is required, it is as simple as {@{conditionally calling the method itself in a method and adding base cases to the method}@}. For example, a recursive way to calculate factorial: <!--SR:!2027-06-02,942,350!2027-12-15,1097,350-->

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
