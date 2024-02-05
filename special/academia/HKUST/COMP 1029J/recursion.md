---
aliases:
  - Java recursion
  - Java recursions
tags:
  - flashcards/special/academia/HKUST/COMP_1029J/recursion
  - languages/in/English
---

# Java recursion

Recursion is all about {{reducing any problem to a simpler similar problem,  repeating this process until you get several base problems that are irreducible}}. <!--SR:!2024-02-20,15,290-->

Usually, we {{do not use recursion}} in Java. But if it is required, it is as simple as {{conditionally calling the method itself in a method and adding base cases to the method}}. For example, a recursive way to reverse a string: <!--SR:!2024-02-19,14,290!2024-02-18,13,290-->

```Java
public static String reverse(String input) {
  if (input.length() <= 1) return input; // base case
  return reverse(input.substring(1)) + input.charAt(0); // call the method itself
}
```

## see also

- [general/recursion](../../../../general/recursion%20(computer%20science).md)
