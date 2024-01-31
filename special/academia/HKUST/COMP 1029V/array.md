---
aliases:
  - VBA array
  - VBA arrays
tags:
  - flashcards/special/academia/HKUST/COMP_1029V/array
  - languages/in/English
---

# array

## declaration

Arrays are declared like {{[variables](basics.md#variable) but with a piece of extra syntax: the indices of the array}}. The syntax is {{`Dim VariableName(start_index To end_index) As ElementType`, where the indices are both ends inclusive}}. You can omit {{the `start_index To`, in which case the `start_index` depends on the option `Base`}}. By default, the option `Base` {{is `0`, but you can change it by running `Option Base value` first}}.

## indexing

To index into an array, write {{`Array(Index)`}}. Assignment uses the same syntax.

## multidimensional

To make a multidimensional array, {{specify each dimension using `start_index To end_index` or `end_index` separated by commas `,` and use `Variant` as the `ElementType`, like `Dim VariableName(start_index1 To end_index1, end_index2, start_index3 To end_index3) As Variant`}}. Indexing a multidimensional array is simply {{adding commas in between the multiple indices, like `Array(Index1, Index2, Index3)`}}.

For two-dimensional arrays, one can initialize the content by {{separating elements in the same row by commas `,`, separating rows by `;`, and enclose the entire thing in `[{...}]`, like `2DArray = [{1, 2, 3; 4, 5, 6; 7, 8, 9}]`}}.

## bounds

One can obtain the lower bound and upper bound, both inclusive, via {{`LBound(array[, rank])` and `UBound(array[, rank])` respectively}}. The `rank` means {{the bound for which inner array to return. It is by default `1`, meaning it returns the bounds for the outermost array}}.

## interaction with range

Assigning `Range` values from an array {{can be done using a simple assignment}}:

```VB
Dim NumberArray(0 To 2) As Integer
NumberArray(0) = 42
NumberArray(1) = 69
NumberArray(2) = 13
Range("A4:C4").Value = NumberArray
```
