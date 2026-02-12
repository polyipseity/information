---
aliases:
  - Python sequence
  - Python sequences
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/sequence
  - language/in/English
---

# Python sequence

Here, we are interested in two sequence types: {@{strings and lists}@}. <!--SR:!2026-09-09,248,330-->

## string

- see: [string](string.md)

To define a string in Python, {@{enclose the string in either double quotes `"example"` or single quotes `'example'`}@}. Both are {@{equivalent}@} except that you need to {@{escape double quotes in the strings for the first one and single quotes for the second one}@}. To escape a character, {@{precede the character with a backslash `\`}@}, like {@{`"quo'te \"example\" un'quote"` and `'quo\'te "example" un\'quote'`}@}. <!--SR:!2026-08-25,248,330!2026-08-15,240,330!2026-12-21,338,346!2026-12-23,340,346!2026-11-15,315,346-->

## list

To define a list in Python, {@{enclose all items in square brackets `[]` and separate each item by a comma `,`}@}, like {@{`[1, 2, "item", 4.2, "ok", 'hey', False]`}@}. A trailing comma is {@{allowed and optional after the last item \(but not if there are no items, i.e. `[,]` is invalid\)}@}. Note that a list can {@{contain items of different types \(including lists\)}@} like the example just now, though usually it is {@{more useful for them to be of the same type}@}. <!--SR:!2026-08-20,244,330!2026-08-31,253,330!2026-09-28,267,330!2027-02-05,384,369!2027-01-24,372,369-->

## length

{@{The length of a sequence}@} can be determined by {@{`len(sequence)`}@}. <!--SR:!2026-08-18,242,330!2026-10-16,285,330-->

## indexing

To {@{access or replace the n-th item}@}, simply write {@{`sequence[n-1]`}@}: <!--SR:!2026-09-30,269,330!2026-09-21,260,330-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {@{negative, in which case it counts from the back}@}: <!--SR:!2026-10-10,279,330-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

One can obtain subsequences, i.e. smaller sequences, via {@{slicing}@}. To obtain a subsequence from the a-th item to the b-th item, write {@{`sequence[a-1:b]`}@}: <!--SR:!2026-09-18,257,330!2026-10-01,270,330-->

```Python
assert "asd"[1:3] == 'sd'
assert [39, "omg", 'asd', 3.4][1:2] == ['omg']
assert "asd"[1:1] == ""
```

Slicing also accepts {@{negative indices, in which case the meaning is still the same as that for indexing}@}. Slicing also allows {@{omitting one or both indices}@}. {@{Omitting the starting point}@} means {@{the starting point is the first element, i.e. `0`}@} \(or if {@{step is negative, then the last element, i.e. `len(sequence) - 1`}@}\). {@{Omitting the ending point}@} means {@{the ending point is after the last element, i.e. `len(sequence)`}@} \(or if {@{step is negative, then before the first element, i.e. `-len(sequence) - 1`}@}\): <!--SR:!2026-09-25,264,330!2026-10-12,281,330!2026-12-24,341,346!2026-12-10,327,346!2026-12-22,339,346!2026-12-20,337,346!2026-11-13,313,346!2026-12-07,324,346-->

```Python
assert "asd"[:2] = "as"
assert [39, "omg", 'asd', 3.4][1:] == ["omg", 'asd', 3.4]
assert [39, "omg", 'asd', 3.4][:] == [39, "omg", 'asd', 3.4]
```

Lastly, slicing accepts {@{a third parameter called step}@}. When omitted, it is {@{by default 1}@}. It determines {@{how many items to move forward after slicing an element}@}, and hence called step. For example, setting step to 3 means {@{every third element is sliced starting from the starting point}@}. Negative steps are also allowed, which simply means {@{going backwards}@}. Here are some more examples: <!--SR:!2026-10-17,286,330!2026-08-26,249,330!2026-09-01,254,330!2026-09-24,263,330!2026-10-06,275,330-->

```Python
assert "abcdefg"[::2] == "aceg"
assert [39, "omg", 'asd', 3.4][1::2] == ["omg", 3.4]
assert 'abcdefg'[::-1] == 'gfedcba'
assert "abcdefg"[:0:-1] == "gfedcb"
```

If {@{the index \(but not slicing\) is out of range}@} \(regardless if {@{it is positive or negative}@}\), then {@{an `IndexError` will be raised}@}. For {@{slicing \(but not indexing\)}@}, {@{no errors will be thrown}@}, and the slicing range is {@{truncated to be within the sequence range}@}. <!--SR:!2026-09-29,268,330!2026-08-24,247,330!2026-10-25,294,330!2026-08-16,241,330!2027-02-07,386,369!2027-02-04,383,369-->

## concatenation

Concatenation means {@{joining several sequences into one larger sequence}@}. It is as simple as using {@{the operator `+`}@}: <!--SR:!2026-10-18,287,330!2026-10-11,280,330-->

```Python
assert "abc" + "def" == "abcdef"
assert [39, "omg"] + ['asd', 3.4] == [39, "omg", "asd", 3.4]
```

Extrapolating the addition above further to multiplication, {@{the operator `*` repeats the sequence itself for the specified number of times}@}: <!--SR:!2026-09-02,255,330-->

```Python
assert 'ab' * 3 == "ababab"
assert 7 * [42, 69] == [42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69, 42, 69]
```

## mutability

Note that there is {@{a difference between strings and lists}@} when it comes to {@{mutability}@}. Strings are {@{always immutable, while lists are mutable}@}. So {@{any operation you have done on strings}@} {@{does not change the original string itself}@}, and {@{reassigning to the variable}@} is {@{the only way to change the value of a variable containing a string}@}. Meanwhile, for {@{lists}@}, there are {@{operations that can change the original list}@}. Compare using {@{`+` and `append` to extend a list}@}: <!--SR:!2026-08-19,243,330!2026-10-19,288,330!2026-10-07,276,330!2026-05-07,160,310!2026-12-25,342,346!2027-01-31,379,369!2026-06-19,182,349!2027-02-06,385,369!2027-04-28,438,394!2027-04-29,439,394-->

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

In Python, there is {@{nothing special}@} about multidimensional sequences. It is literally {@{lists inside a list}@}: <!--SR:!2026-08-14,239,330!2026-10-15,284,330-->

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
