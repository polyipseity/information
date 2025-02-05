---
aliases:
  - HKUST COMP 1029P review questions - lesson 3.1
tags:
  - language/in/English
---

# review questions - lesson 3.1

- HKUST COMP 1029P

## The neighbors\(\) Function

In this review question you will develop a function called neighbors\(\), which you will need for the next exercise.

In a 2D array, each element has up to eight neighbors - the cells immediately to the north, east, west, south, northeast, northwest, southeast, and southwest of it. Of course, elements on the boundary of the array have fewer neighbors \(entries at the four corners only have three neighbors\). Your task is to write a function called neighbors\(\) that takes a 2D array named input, a row index, and a column index as input and returns the number of neighbors of array\[row\]\[column\] that are 1's.

For example, if the 2D input array is

```Python
array = [ [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 1] ]
```

representing the array

```text
0 0 0 0
1 1 0 1
0 0 0 1
```

then here are some examples of the function being used:

```Python
>>> neighbors(array, 1, 1)
1
>>> neighbors(array, 2, 2)
3
```

\(Remember that the top left corner is referred to as \[0\]\[0\]\).

Here is another example.

If the 2D input array is

```Python
bigArray = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1]
]
```

representing the array

```text
0 1 1 1 1 0 0 0
1 0 0 0 0 1 0 1
0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 1 0 1 1
0 0 0 0 0 1 0 1
1 1 1 0 0 0 1 0
1 0 1 0 0 0 0 1
```

then here are some examples of the function being used:

```Python
>>> neighbors(bigArray, 3, 3)
3
>>> neighbors(bigArray, 5, 6)
5
>>> neighbors(bigArray, 4, 1)
0
```

\(Again remember that the top left corner is referred to as \[0\]\[0\]\).

Notice that you'll need to be careful when counting the neighbors of the cells along the boundaries!
