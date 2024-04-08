---
aliases:
  - Java array
  - Java arrays
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/array
  - language/in/English
---

# Java array

A variable can store a single value while an array can {{store multiple values}}. <!--SR:!2024-04-29,68,310-->

## creation

To create an array, {{enclose the multiple values in `{}`}}: <!--SR:!2024-04-15,57,310-->

```Java
String[] aStringArray = { "Hello", ",", "world", "!" };
```

Less ideally, an array can be {{created and initialized}} separately: <!--SR:!2024-04-22,62,310-->

```Java
String[] aStringArray = new String[4];
aStringArray[0] = "Hello";
aStringArray[1] = ",";
aStringArray[2] = "world";
aStringArray[3] = "!";
```

## indexing

To access the n-th element in an array, simply write {{`array[n-1]`}}. <!--SR:!2024-10-29,207,330-->

If the index does not refer to values inside the array, like {{the index being negative, or larger than or equal to the array length}}, an {{`java.lang.ArrayIndexOutOfBoundsException` is thrown}}. <!--SR:!2024-04-16,58,310!2024-04-20,61,310-->

## multi-dimensional array

A multi-dimensional array is simply {{an array with lower-dimensional arrays as its elements}}: <!--SR:!2024-04-21,62,310-->

```Java
boolean[][] threeByThreeSquare = {
  {false, true,  false},
  {true,  false, true},
  {false, true,  false},
};
assert threeByThreeSquare[0][1];
assert !threeByThreeSquare[1][1];
assert threeByThreeSquare[2][1];
```

## length

The length of an array can be determined by {{accessing the field `.length`}}: <!--SR:!2024-09-02,152,310-->

```Java
int[] anIntArray = new int[123];
assert anIntArray.length == 123;
```
