---
aliases:
  - VBA array
  - VBA arrays
tags:
  - flashcard/special/academia/HKUST/COMP_1029V/array
  - language/in/English
---

# array

## declaration

Arrays are declared like {{[variables](basics.md#variable) but with extra syntax: indicating the indices of the array}}. The syntax is {{`Dim VariableName(start_index To end_index) As ElementType`, where the indices are both ends inclusive}}. You can omit {{the `start_index To`, in which case the `start_index` depends on the option `Base`}}. By default, the option `Base` {{is `0`, but you can change it by running `Option Base value` first}}. <!--SR:!2024-11-30,215,310!2024-06-29,100,290!2024-07-23,130,310!2024-07-07,95,290-->

## indexing

To index into an array, write {{`Array(Index)`}}. Assignment uses the same syntax. <!--SR:!2024-09-10,154,310-->

## multidimensional

To make a multidimensional array, {{specify each dimension using `start_index To end_index` or `end_index` separated by commas `,` and use `Variant` as the element type, like `Dim VariableName(3 To 5, 2, 0 To 6) As Variant`}}. Indexing a multidimensional array is simply {{adding commas in between the multiple indices, like `Array(4, 2, 5)`}}. <!--SR:!2025-04-12,289,290!2024-10-16,182,310-->

For two-dimensional arrays, one can initialize the content by {{separating elements in the same row by commas `,`, separating rows by `;`, and enclose the entire thing in `[{...}]`, like `2DArray = [{1, 2, 3; 4, 5, 6; 7, 8, 9}]`}}. <!--SR:!2024-07-17,105,290-->

## bounds

One can obtain the lower bound and upper bound, both inclusive, via {{`LBound(array[, rank])` and `UBound(array[, rank])` respectively}}. The `rank` means {{the bound for which inner array to return. It is by default `1`, meaning it returns the bounds for the outermost array}}. <!--SR:!2024-08-16,130,290!2024-12-12,213,290-->

## interaction with range

Assigning `Range` values from an array {{can be done using simple assignment}}: <!--SR:!2024-11-07,197,310-->

```VB
Dim NumberArray(0 To 2) As Integer
NumberArray(0) = 42
NumberArray(1) = 69
NumberArray(2) = 13
Range("A4:C4").Value = NumberArray
```
