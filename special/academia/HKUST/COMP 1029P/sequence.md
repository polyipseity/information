---
aliases:
  - Python sequence
  - Python sequences
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/sequence
  - language/in/English
---

# Python sequence

Here, we are interested in two sequence types: {@{strings and lists}@}. <!--SR:!2028-06-29,1251,350-->

## string

- see: [string](string.md)

To define a string in Python, {@{enclose the string in either double quotes `"example"` or single quotes `'example'`}@}. Both are {@{equivalent}@} except that you need to {@{escape double quotes in the strings for the first one and single quotes for the second one}@}. To escape a character, {@{precede the character with a backslash `\`}@}, like {@{`"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}@}. <!--SR:!2026-12-16,785,330!2026-05-01,625,330!2025-11-04,25,372!2025-11-03,24,372!2025-11-04,25,372-->

## list

To define a list in Python, {@{enclose all items in square brackets `[]` and separate each item by a comma `,`}@}, like {@{`[1, 2, "item", 4.2, "ok", 'hey', False]`}@}. A trailing comma is {@{allowed and optional after the last item \(but not if there are no items, i.e. `[,]` is invalid\)}@}. Note that a list can {@{contain items of different types \(including lists\)}@} like the example just now, though usually it is {@{more useful for them to be of the same type}@}. <!--SR:!2027-10-22,1053,350!2028-03-24,1174,350!2026-04-04,457,386!2025-11-06,26,383!2025-11-06,26,383-->

## length

{@{The length of a sequence}@} can be determined by {@{`len(sequence)`}@}. <!--SR:!2028-04-22,1197,350!2026-04-10,462,386-->

## indexing

To {@{access or replace the n-th item}@}, simply write {@{`sequence[n-1]`}@}: <!--SR:!2027-11-15,1073,350!2026-03-29,452,386-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {@{negative, in which case it counts from the back}@}: <!--SR:!2028-11-29,1371,350-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

One can obtain subsequences, i.e. smaller sequences, via {@{slicing}@}. To obtain a subsequence from the a-th item to the b-th item, write {@{`sequence[a-1:b]`}@}: <!--SR:!2026-01-01,476,310!2028-01-07,1115,350-->

```Python
assert "asd"[1:3] == 'sd'
assert [39, "omg", 'asd', 3.4][1:2] == ['omg']
assert "asd"[1:1] == ""
```

Slicing also accepts {@{negative indices, in which case the meaning is still the same as that for indexing}@}. Slicing also allows {@{omitting one or both indices}@}. {@{Omitting the starting point}@} means {@{the starting point is the first element, i.e. `0`}@} \(or if {@{step is negative, then the last element, i.e. `len(sequence) - 1`}@}\). {@{Omitting the ending point}@} means {@{the ending point is after the last element, i.e. `len(sequence)`}@} \(or if {@{step is negative, then before the first element, i.e. `-len(sequence) - 1`}@}\): <!--SR:!2027-09-13,1024,350!2026-01-27,495,310!2025-11-03,24,372!2025-11-04,25,372!2025-11-03,24,372!2025-11-02,23,372!2025-11-03,24,372!2025-11-02,23,372-->

```Python
assert "asd"[:2] = "as"
assert [39, "omg", 'asd', 3.4][1:] == ["omg", 'asd', 3.4]
assert [39, "omg", 'asd', 3.4][:] == [39, "omg", 'asd', 3.4]
```

Lastly, slicing accepts {@{a third parameter called step}@}. When omitted, it is {@{by default 1}@}. It determines {@{how many items to move forward after slicing an element}@}, and hence called step. For example, setting step to 3 means {@{every third element is sliced starting from the starting point}@}. Negative steps are also allowed, which simply means {@{going backwards}@}. Here are some more examples: <!--SR:!2026-01-08,483,310!2028-04-23,1197,350!2026-01-03,480,310!2029-11-02,1527,310!2028-04-02,1183,350-->

```Python
assert "abcdefg"[::2] == "aceg"
assert [39, "omg", 'asd', 3.4][1::2] == ["omg", 3.4]
assert 'abcdefg'[::-1] == 'gfedcba'
assert "abcdefg"[:0:-1] == "gfedcb"
```

If {@{the index \(but not slicing\) is out of range}@} \(regardless if {@{it is positive or negative}@}\), then {@{an `IndexError` will be raised}@}. For {@{slicing \(but not indexing\)}@}, {@{no errors will be thrown}@}, and the slicing range is {@{truncated to be within the sequence range}@}. <!--SR:!2026-03-23,447,386!2026-03-05,432,386!2029-11-15,1510,386!2030-04-10,1628,386!2025-11-06,26,383!2025-11-06,26,383-->

## concatenation

Concatenation means {@{joining several sequences into one larger sequence}@}. It is as simple as using {@{the operator `+`}@}: <!--SR:!2027-07-19,948,330!2027-08-29,1015,350-->

```Python
assert "abc" + "def" == "abcdef"
assert [39, "omg"] + ['asd', 3.4] == [39, "omg", "asd", 3.4]
```

Extrapolating the addition above further to multiplication, {@{the operator `*` repeats the sequence itself for the specified number of times}@}: <!--SR:!2026-10-19,741,330-->

```Python
assert 'ab' * 3 == "ababab"
assert 7 * [42, 69] == [42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69]
```

## mutability

Note that there is a difference between strings and lists when it comes to {@{mutability}@}. Strings are {@{always immutable, while lists are mutable}@}. So {@{any operation you have done on strings}@} {@{does not change the original string itself}@}, and {@{reassigning to the variable}@} is {@{the only way to change the value of a variable containing a string}@}. Meanwhile, for lists, {@{there are operations that can change the original list}@}. Compare using {@{`+` and `append` to extend a list}@}: <!--SR:!2029-03-19,1461,350!2027-07-17,948,330!2027-01-15,771,330!2026-11-11,755,330!2025-11-02,23,372!2025-11-06,26,383!2025-11-06,26,383!2025-11-06,26,383-->

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

In Python, there is {@{nothing special}@} about multidimensional sequences. It is literally {@{lists inside a list}@}: <!--SR:!2027-12-05,1090,350!2027-11-23,1077,350-->

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
