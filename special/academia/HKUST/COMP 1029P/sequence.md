---
aliases:
  - Python sequence
  - Python sequences
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/sequence
  - language/in/English
---

# Python sequence

Here, we are interested in two sequence types: {{strings and lists}}. <!--SR:!2024-02-21,16,290-->

## string

To define a string in Python, {{enclose the string in either double quotes `"example"` or single quotes `'example'`. Both are equivalent except that you need to escape double quotes in the strings for the first one and single quotes for the second one}}. To escape a character, {{precede the character with a backslash `\`, like `"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}}. <!--SR:!2024-02-21,16,290!2024-03-20,36,290-->

## list

To define a list in Python, {{enclose all items in square brackets `[]` and separate each item by a comma `,`, like `[1, 2, "item", 4.2, "ok", 'hey', False]`}}. Note that a list can {{contain items of different types like the example just now}}. <!--SR:!2024-04-13,54,310!2024-02-21,16,290-->

## length

The length of a sequence can be determined by {{`len(sequence)`}}. <!--SR:!2024-02-21,16,290-->

## indexing

To access the n-th item, simply write {{`sequence[n-1]`}}: <!--SR:!2024-04-14,55,310-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {{negative, in which case it counts from the back}}: <!--SR:!2024-02-22,17,290-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

One can obtain subsequences, i.e. smaller sequences, via {{slicing}}. To obtain a subsequence from the a-th item to the b-th item, write {{`sequence[a-1:b]`}}: <!--SR:!2024-04-11,52,310!2024-04-17,57,310-->

```Python
assert "asd"[1:3] == 'sd'
assert [39, "omg", 'asd', 3.4][1:2] == ['omg']
assert "asd"[1:1] == ""
```

Slicing also accepts {{negative indices, in which case the meaning is still the same as that for indexing}}. Slicing also allows {{omitting one or both indices. Omitting the starting point means the starting point is the first element, i.e. `0` (or if step is negative, then the last element, i.e. `len(sequence) - 1`). Omitting the ending point means the ending point is after the last element, i.e. `len(sequence)` (or if step is negative, then before the first element, i.e. `-len(sequence) - 1`)}}: <!--SR:!2024-04-12,53,310!2024-04-12,53,310-->

```Python
assert "asd"[:2] = "as"
assert [39, "omg", 'asd', 3.4][1:] == ["omg", 'asd', 3.4]
assert [39, "omg", 'asd', 3.4][:] == [39, "omg", 'asd', 3.4]
```

Lastly, slicing accepts {{a third parameter called step}}. When omitted, it is {{by default 1}}. It determines {{how many items to move forward after slicing an element}}, and hence called step. For example, setting step to 3 means {{every third element is sliced starting from the starting point}}. Negative steps are also allowed, which simply means {{going backwards}}. Here are some more examples: <!--SR:!2024-04-09,51,310!2024-02-21,16,290!2024-04-08,50,310!2024-04-02,46,290!2024-04-20,60,310-->

```Python
assert "abcdefg"[::2] == "aceg"
assert [39, "omg", 'asd', 3.4][1::2] == ["omg", 3.4]
assert 'abcdefg'[::-1] == 'gfedcba'
assert "abcdefg"[:0:-1] == "gfedcb"
```

## concatenation

Concatenation means {{joining several sequences into one larger sequence}}. It is as simple as using {{the operator `+`}}: <!--SR:!2024-02-22,17,290!2024-04-08,50,310-->

```Python
assert "abc" + "def" == "abcdef"
assert [39, "omg"] + ['asd', 3.4] == [39, "omg", "asd", 3.4]
```

Extrapolation the addition above further to multiplication, {{the operator `*` repeats the sequence itself for the specified number of times}}: <!--SR:!2024-04-14,56,310-->

```Python
assert 'ab' * 3 == "ababab"
assert 7 * [42, 69] == [42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69]
```

## mutability

Note that there is a difference between strings and lists when it comes to {{mutability}}. Strings are {{always immutable, while lists are mutable}}. So any operation you have done on strings {{does not change the original string itself, and reassigning to the variable is the only way to change the value of a variable containing a string}}. Meanwhile, for lists, {{there are operations that can change the original list. Compare using `+` and `append` to extend a list}}: <!--SR:!2024-02-22,17,290!2024-02-22,17,290!2024-04-13,55,310!2024-04-19,59,310-->

```Python
original = [1, 2, 3]
new = original + [4]
assert new == [1, 2, 3, 4]
assert original == [1, 2, 3] # `original` is not affected as `+` creates a new list
assert id(original) != id(new) # `id` can determine whether two objects are the same object in memory

original = [1, 2, 3]
new = original
new.append(4)
assert new == [1, 2, 3, 4]
assert original == [1, 2, 3, 4] # `original` is affected as `append` modifies the original list
assert id(original) == id(new) # `id` can determine whether two objects are the same object in memory
```

## multidimensional

In Python, there is {{nothing special}} about multidimensional sequences. It is literally {{lists inside a list}}: <!--SR:!2024-04-16,56,310!2024-04-18,58,310-->

```Python
sudoku = [
  [9, 1, 6],
  [3, 5, 8],
  [4, 7, 2],
]
assert sudoku[0][0] == 9
assert sudoku[2][1] == 7
assert sudoku[1] == [3, 5, 8]
```
