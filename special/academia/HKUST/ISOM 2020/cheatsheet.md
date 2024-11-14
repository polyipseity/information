---
aliases:
  - HKUST ISOM 2020
  - HKUST ISOM 2020 cheatsheet
  - HKUST ISOM 2020 cheatsheets
  - HKUST ISOM2020
  - HKUST ISOM2020 cheatsheet
  - HKUST ISOM2020 cheatsheets
  - ISOM 2020
  - ISOM 2020 cheatsheet
  - ISOM 2020 cheatsheets
  - ISOM2020
  - ISOM2020 cheatsheet
  - ISOM2020 cheatsheets
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/cheatsheet
  - language/in/English
---

# cheatsheet

- HKUST ISOM 2020

The cheatsheet is provided during the final examination.

## previews

- [`cheatsheet.png`](cheatsheet.png): the original cheatsheet

## data types

- `int` ::@:: integer
- `float` ::@:: floating point
- `bool` ::@:: `True` or `False`
- `str` ::@:: string
- `[...]` ::@:: list

## arithmetic operators

- `+` ::@:: addition
- `-` ::@:: subtraction
- `*` ::@:: multiplication
- `**` ::@:: to the power of
- `/` ::@:: division
- `//` ::@:: floor division
- `%` ::@:: mod

## input / output

- `print()` ::@:: display the input value(s), optionally `end` with specific input
- `input()` ::@:: ask user for input
- `\n` ::@:: escape character: line break
- `\t` ::@:: escape character: tab

## math functions / conversion

- `abs()` ::@:: absolute value
- `math.sqrt()` ::@:: square root of
- `round()` ::@:: round off the input value
- `type()` ::@:: return data type of input
- `int()` ::@:: convert input to integer
- `float()` ::@:: convert input to float
- `str()` ::@:: convert input to str

## list / string operations

- `list[...]` ::@:: locate an item at the specific index in a list
- `+` ::@:: combine two lists / strings
- `in` ::@:: check existence in a list / string
- `not in` ::@:: check if not exists in a list / string
- `list.append()` ::@:: add a new element in the list
- `list.pop()` ::@:: remove and return an item at a specific index
- `list.count()` ::@:: count the occurrence of the input item
- `list.index()` ::@:: find the index of the input item
- `len()` ::@:: return the number of elements in the input list
- `max()` ::@:: find the biggest element in the input list
- `min()` ::@:: find the smallest element in the input list
- `sum()` ::@:: find the sum of all elements of the input list
- `range()` ::@:: create a number sequence starting from zero

## relational operators

- `==` ::@:: is equal?
- `!=` ::@:: is not equal?
- `<` ::@:: is less than?
- `>` ::@:: is greater than?
- `<=` ::@:: is less than or equal to?
- `>=` ::@:: is greater than or equal to?

## boolean operators

- `and` ::@:: are both operands `True`?
- `or` ::@:: is/are either (or both) of the operands `True`?
- `not` ::@:: flip `True`/`False` to one another

## conditional statement

- keywords ::@:: `if ...: ... [elif ...: ...] [else: ...]`

```Python
if <caseA>:
  <true-statements-for-A>
elif <caseB>:
  <true-statements-for-B>
else:
  <false-statements>
```

## loop

- keywords ::@:: `for ... in ...: ...`, `while True: ...`
- `break` ::@:: terminate a loop

```Python
for <variable> in <iterable>:
  <code-block>
```

```Python
while True:
  <code-block>
```

## random function

- `random.randint(a, b)` ::@:: return a number between `a` and `b`
