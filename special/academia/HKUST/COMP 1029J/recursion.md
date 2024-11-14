---
aliases:
  - Java recursion
  - Java recursions
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/recursion
  - language/in/English
---

# Java recursion

Recursion is all about {@{reducing any problem to a simpler similar problem,  repeating this process until you get several base problems that are irreducible}@}.

Usually, we {@{do not use recursion}@} in Java. But if it is required, it is as simple as {@{conditionally calling the method itself in a method and adding base cases to the method}@}. For example, a recursive way to reverse a string:

```Java
public static String reverse(String input) {
  if (input.length() <= 1) return input; // base case
  return reverse(input.substring(1)) + input.charAt(0); // call the method itself
}
```

## see also

- [general/recursion](../../../../general/recursion%20(computer%20science).md)
