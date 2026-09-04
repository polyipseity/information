---
aliases:
  - Python sequence
  - Python sequences
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/sequence
  - language/in/English
---

# Python sequence

Here, we are interested in two sequence types: {@{strings and lists}@}. <!--SR:!fsrs,2029-09-13T00:00:00.000Z,1099,1099.36699517,1,2,9,0,0,2026-09-10T00:00:00.000Z-->

## string

- see: [string](string.md)

To define a string in Python, {@{enclose the string in either double quotes `"example"` or single quotes `'example'`}@}. Both are {@{equivalent}@} except that you need to {@{escape double quotes in the strings for the first one and single quotes for the second one}@}. To escape a character, {@{precede the character with a backslash `\`}@}, like {@{`"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}@}. <!--SR:!fsrs,2029-08-29T00:00:00.000Z,1099,1099.36699517,1,2,9,0,0,2026-08-26T00:00:00.000Z!fsrs,2029-07-19T00:00:00.000Z,1068,1068.495917,1,2,9,0,0,2026-08-16T00:00:00.000Z!2026-12-21,338,346!2026-12-23,340,346!2026-11-15,315,346-->

## list

To define a list in Python, {@{enclose all items in square brackets `[]` and separate each item by a comma `,`}@}, like {@{`[1, 2, "item", 4.2, "ok", 'hey', False]`}@}. A trailing comma is {@{allowed and optional after the last item \(but not if there are no items, i.e. `[,]` is invalid\)}@}. Note that a list can {@{contain items of different types \(including lists\)}@} like the example just now, though usually it is {@{more useful for them to be of the same type}@}. <!--SR:!fsrs,2029-08-09T00:00:00.000Z,1084,1083.94697941,1,2,9,0,0,2026-08-21T00:00:00.000Z!fsrs,2029-09-24T00:00:00.000Z,1119,1118.59914239,1,2,9,0,0,2026-09-01T00:00:00.000Z!fsrs,2029-12-14T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-09-29T00:00:00.000Z!2027-02-05,384,369!2027-01-24,372,369-->

## length

{@{The length of a sequence}@} can be determined by {@{`len(sequence)`}@}. <!--SR:!fsrs,2029-07-30T00:00:00.000Z,1076,1076.22532725,1,2,9,0,0,2026-08-19T00:00:00.000Z!2026-10-16,285,330-->

## indexing

To {@{access or replace the n-th item}@}, simply write {@{`sequence[n-1]`}@}: <!--SR:!fsrs,2029-12-24T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-10-01T00:00:00.000Z!fsrs,2028-09-24T00:00:00.000Z,733,732.76739939,2.49272837,2,9,0,0,2026-09-22T00:00:00.000Z-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {@{negative, in which case it counts from the back}@}: <!--SR:!fsrs,2030-02-09T00:00:00.000Z,1218,1217.87747351,1,2,9,0,0,2026-10-10T00:00:00.000Z-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

One can obtain subsequences, i.e. smaller sequences, via {@{slicing}@}. To obtain a subsequence from the a-th item to the b-th item, write {@{`sequence[a-1:b]`}@}: <!--SR:!fsrs,2028-09-13T00:00:00.000Z,725,725.23172215,2.49272837,2,9,0,0,2026-09-19T00:00:00.000Z!fsrs,2029-12-31T00:00:00.000Z,1186,1186.0509745,1,2,9,0,0,2026-10-02T00:00:00.000Z-->

```Python
assert "asd"[1:3] == 'sd'
assert [39, "omg", 'asd', 3.4][1:2] == ['omg']
assert "asd"[1:1] == ""
```

Slicing also accepts {@{negative indices, in which case the meaning is still the same as that for indexing}@}. Slicing also allows {@{omitting one or both indices}@}. {@{Omitting the starting point}@} means {@{the starting point is the first element, i.e. `0`}@} \(or if {@{step is negative, then the last element, i.e. `len(sequence) - 1`}@}\). {@{Omitting the ending point}@} means {@{the ending point is after the last element, i.e. `len(sequence)`}@} \(or if {@{step is negative, then before the first element, i.e. `-len(sequence) - 1`}@}\): <!--SR:!fsrs,2029-11-30T00:00:00.000Z,1161,1160.74715681,1,2,9,0,0,2026-09-26T00:00:00.000Z!fsrs,2030-02-18T00:00:00.000Z,1225,1225.46601476,1,2,9,0,0,2026-10-12T00:00:00.000Z!2026-12-24,341,346!2026-12-10,327,346!2026-12-22,339,346!2026-12-20,337,346!2026-11-13,313,346!2026-12-07,324,346-->

```Python
assert "asd"[:2] = "as"
assert [39, "omg", 'asd', 3.4][1:] == ["omg", 'asd', 3.4]
assert [39, "omg", 'asd', 3.4][:] == [39, "omg", 'asd', 3.4]
```

Lastly, slicing accepts {@{a third parameter called step}@}. When omitted, it is {@{by default 1}@}. It determines {@{how many items to move forward after slicing an element}@}, and hence called step. For example, setting step to 3 means {@{every third element is sliced starting from the starting point}@}. Negative steps are also allowed, which simply means {@{going backwards}@}. Here are some more examples: <!--SR:!2026-10-17,286,330!fsrs,2029-09-03T00:00:00.000Z,1103,1103.2172026,1,2,9,0,0,2026-08-27T00:00:00.000Z!fsrs,2029-09-28T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-02T00:00:00.000Z!fsrs,2029-11-25T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-09-25T00:00:00.000Z!fsrs,2030-01-21T00:00:00.000Z,1203,1202.68030072,1,2,9,0,0,2026-10-06T00:00:00.000Z-->

```Python
assert "abcdefg"[::2] == "aceg"
assert [39, "omg", 'asd', 3.4][1::2] == ["omg", 3.4]
assert 'abcdefg'[::-1] == 'gfedcba'
assert "abcdefg"[:0:-1] == "gfedcb"
```

If {@{the index \(but not slicing\) is out of range}@} \(regardless if {@{it is positive or negative}@}\), then {@{an `IndexError` will be raised}@}. For {@{slicing \(but not indexing\)}@}, {@{no errors will be thrown}@}, and the slicing range is {@{truncated to be within the sequence range}@}. <!--SR:!fsrs,2028-10-22T00:00:00.000Z,753,752.82030637,2.49272837,2,9,0,0,2026-09-30T00:00:00.000Z!fsrs,2029-08-25T00:00:00.000Z,1096,1095.51488793,1,2,9,0,0,2026-08-25T00:00:00.000Z!2026-10-25,294,330!fsrs,2029-07-24T00:00:00.000Z,1072,1072.36160804,1,2,9,0,0,2026-08-17T00:00:00.000Z!2027-02-07,386,369!2027-02-04,383,369-->

## concatenation

Concatenation means {@{joining several sequences into one larger sequence}@}. It is as simple as using {@{the operator `+`}@}: <!--SR:!2026-10-18,287,330!fsrs,2030-02-14T00:00:00.000Z,1222,1221.67255456,1,2,9,0,0,2026-10-11T00:00:00.000Z-->

```Python
assert "abc" + "def" == "abcdef"
assert [39, "omg"] + ['asd', 3.4] == [39, "omg", "asd", 3.4]
```

Extrapolating the addition above further to multiplication, {@{the operator `*` repeats the sequence itself for the specified number of times}@}: <!--SR:!fsrs,2029-10-03T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-03T00:00:00.000Z-->

```Python
assert 'ab' * 3 == "ababab"
assert 7 * [42, 69] == [42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69]
```

## mutability

Note that there is {@{a difference between strings and lists}@} when it comes to {@{mutability}@}. Strings are {@{always immutable, while lists are mutable}@}. So {@{any operation you have done on strings}@} {@{does not change the original string itself}@}, and {@{reassigning to the variable}@} is {@{the only way to change the value of a variable containing a string}@}. Meanwhile, for {@{lists}@}, there are {@{operations that can change the original list}@}. Compare using {@{`+` and `append` to extend a list}@}: <!--SR:!fsrs,2028-07-10T00:00:00.000Z,690,689.94707246,2.49272837,2,9,0,0,2026-08-20T00:00:00.000Z!2026-10-19,288,330!fsrs,2030-01-25T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-10-07T00:00:00.000Z!2028-03-27,686,330!2026-12-25,342,346!2027-01-31,379,369!fsrs,2028-12-01T00:00:00.000Z,896,895.73024309,1,2,9,0,0,2026-06-19T00:00:00.000Z!2027-02-06,385,369!2027-04-28,438,394!2027-04-29,439,394-->

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

In Python, there is {@{nothing special}@} about multidimensional sequences. It is literally {@{lists inside a list}@}: <!--SR:!fsrs,2029-07-15T00:00:00.000Z,1065,1064.62815785,1,2,9,0,0,2026-08-15T00:00:00.000Z!fsrs,2030-03-05T00:00:00.000Z,1237,1236.83645167,1,2,9,0,0,2026-10-15T00:00:00.000Z-->

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
