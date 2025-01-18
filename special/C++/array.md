---
aliases:
  - array
  - array declaration
tags:
  - flashcard/active/special/Cpp/array
  - language/in/English
---

# array declaration

## multidimensional arrays

A multidimensional array is {@{an array with another array as its element type}@}. The declaration order of dimensions is {@{the same as the acccess order, i.e. `int a[2][3]` means `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]` are accessible}@}. <!--SR:!2025-03-05,396,330!2029-03-30,1550,350-->

```Cpp
int a[2][3]{@{0, 1, 2}, {3, 4, 5}@};
```

[Array-to-pointer decay](#array-to-pointer%20decay) is {@{applied only once to multidimensional arrays}@}. <!--SR:!2025-01-19,359,330-->

## arrays of unknown bound

A multidimensional array can {@{have an unknown bound only in the first dimension}@}. <!--SR:!2028-01-11,1170,330-->

```Cpp
int valid[][10];
// int error[10][];
```

## array-to-pointer decay

> [!tip] tips
>
> - differences between array and [pointer](pointer%20declaration.md): While arrays can decay to [pointers](pointer%20declaration.md), {@{they are distinct types and not equivalent. For example, `int(*arr)[10]` (pointer to array of 10 `int`s) is not equivalent to `int **arr` (pointer to pointer to `int`)}@}. It might seem reasonable to {@{decay the inner array of the first type to a [pointer](pointer%20declaration.md), making it equivalent to the second type}@}. However, consider {@{[pointer arithmetic](../../general/pointer%20arithmetic.md) on both types: `arr + 1`. In the first case, the address is incremented by `sizeof(int[10])`. But in the second case, the address is incremented by `sizeof(int*)`}@}. The distinction is important when {@{performing [pointer arithmetic](../../general/pointer%20arithmetic.md) on [multidimensional arrays](#multidimensional%20arrays), such as `int arr[2][10]`, which decays to `int(*)[10]` instead of `int**`. It makes `arr[1]`, equivalent to `*(arr + 1)`, work properly}@}. <!--SR:!2028-01-30,1109,312!2027-06-26,962,353!2028-05-09,1208,353!2025-01-21,265,333-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/array) from [cppreference.com](https://cppreference.com) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
