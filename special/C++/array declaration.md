---
aliases:
  - array declaration
tags:
  - flashcards/special/Cpp/array_declaration
---

# array declaration

## multidimensional arrays

A multidimensional array is {{an array with another array as its element type}}. The declaration order of dimensions is {{the same as the acccess order, i.e. `int a[2][3]` means `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]` are dereferenceable addresses}}.

```Cpp
int a[2][3]{{0, 1, 2}, {3, 4, 5}};
```

[Array-to-pointer decay](#array-to-pointer%20decay) is {{applied only once to multidimensional arrays}}.

## arrays of unknown bound

A multidimensional array can {{only have an unknown bound in the first dimension}}.

```Cpp
int valid[][10];
int error[10][];
```
