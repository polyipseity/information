---
aliases:
  - array declaration
tags:
  - flashcard/special/Cpp/array_declaration
  - language/in/English
---

# array declaration

## multidimensional arrays

A multidimensional array is {{an array with another array as its element type}}. The declaration order of dimensions is {{the same as the acccess order, i.e. `int a[2][3]` means `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]` are accessible}}. <!--SR:!2025-03-05,396,330!2024-12-31,342,330-->

```Cpp
int a[2][3]{{0, 1, 2}, {3, 4, 5}};
```

[Array-to-pointer decay](#array-to-pointer%20decay) is {{applied only once to multidimensional arrays}}. <!--SR:!2025-01-19,359,330-->

## arrays of unknown bound

A multidimensional array can {{have an unknown bound only in the first dimension}}. <!--SR:!2024-10-28,272,310-->

```Cpp
int valid[][10];
// int error[10][];
```

## array-to-pointer decay

> [!tip] tips
>
> - differences between array and [pointer](pointer%20declaration.md): While arrays can decay to [pointers](pointer%20declaration.md), {{they are distinct types and not equivalent. For example, `int(*arr)[10]` (pointer to array of 10 `int`s) is not equivalent to `int **arr` (pointer to pointer to `int`)}}. It might seem reasonable to {{decay the inner array of the first type to a [pointer](pointer%20declaration.md), making it equivalent to the second type}}. However, consider {{[pointer arithmetic](../../general/pointer%20arithmetic.md) on both types: `arr + 1`. In the first case, the address is incremented by `sizeof(int[10])`. But in the second case, the address is incremented by `sizeof(int*)`}}. The distinction is important when {{performing [pointer arithmetic](../../general/pointer%20arithmetic.md) on [multidimensional arrays](#multidimensional%20arrays), such as `int arr[2][10]`, which decays to `int(*)[10]` instead of `int**`. It makes `arr[1]`, equivalent to `*(arr + 1)`, work properly}}. <!--SR:!2025-01-16,273,292!2024-11-06,209,333!2024-04-30,79,333!2024-05-01,80,333-->
