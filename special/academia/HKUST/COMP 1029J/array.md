---
aliases:
  - Java array
  - Java arrays
tags:
  - flashcards/special/academic/HKUST/COMP_1029J/array
  - languages/in/English
---

# Java array

A variable can store a single value while an array can {{store multiple values}}.

## creation

To create an array, {{enclose the multiple values in `{}`}}:

```Java
String[] aStringArray = { "Hello", ",", "world", "!" };
```

Less ideally, an array can be {{created and initialized}} separately:

```Java
String[] aStringArray = new String[4];
aStringArray[0] = "Hello";
aStringArray[1] = ",";
aStringArray[2] = "world";
aStringArray[3] = "!";
```

## indexing

To access the $n + 1$-th element in an array, simply write {{`array[n]`}}.

If the index does not refer to values inside the array, like {{the index being negative or larger than the array length}}, an {{`java.lang.ArrayIndexOutOfBoundsException` is thrown}}.

## multi-dimensional array

A multi-dimensional array is simply {{an array with lower-dimensional arrays as its elements}}:

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

The length of an array can be determined by {{accessing the field `.length`}}:

```Java
int[] anIntArray = new int[123];
assert anIntArray.length == 123;
```