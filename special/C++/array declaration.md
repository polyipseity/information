---
aliases:
  - array declaration
tags:
  - flashcards/special/Cpp/array_declaration
---

# array declaration

## multidimensional arrays

A multidimensional array is {{an array with another array as its element type}}. The declaration order of dimensions is {{the same as the acccess order, i.e. `int a[2][3]` means `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]` are accessible}}. <!--SR:!2023-09-28,4,270!2023-09-28,4,270-->

```Cpp
int a[2][3]{{0, 1, 2}, {3, 4, 5}};
```

[Array-to-pointer decay](#array-to-pointer%20decay) is {{applied only once to multidimensional arrays}}. <!--SR:!2023-09-28,4,270-->

## arrays of unknown bound

A multidimensional array can {{have an unknown bound only in the first dimension}}. <!--SR:!2023-09-28,4,270-->

```Cpp
int valid[][10];
int error[10][];
```
