---
aliases:
  - HKUST ISOM 2020
  - HKUST ISOM 2020 index
  - HKUST ISOM2020
  - HKUST ISOM2020 index
  - ISOM 2020
  - ISOM 2020 index
  - ISOM2020
  - ISOM2020 index
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/index
  - function/index
  - language/in/English
---

# index

- HKUST ISOM 2020
- name: Coding for Business

The content is in teaching order.

- general recommendations ::: Do NOT use techniques not learnt in lectures! Also, if you have learnt Python before well, you would find a few quiz questions ambiguous with imprecise wordings. Good luck guessing the answer...
- course logistics
  - pathway: ISOM 2020 → ISOM 2600
  - duration: 7 weeks, for the first half of the semester
  - time: 2 hour lectures, 2 hour labs
  - format: pre-lecture videos → weekly exercise (graded, infinite attempts) → lecture → lab (graded, attendance required) → practice question set (ungraded, optional)
  - grading scheme: weekly exercise 10%, lab submissions 20%, final exam 70% (basic programming test 45%, free coding exam 25%)
  - course intended learning outcomes (CILOs): understand coding logic, Python basics, and hands-on guidance
  - lab: attendance required, can be waived by doing a challenging exercise and demonstrate it to lab helpers at the start of the lab to be waived
- [assignments](assignments/)
- final exam: 2024-10-19T14:30:00+08:00/2024-10-19T17:30:00+08:00 (PT3H)

## week 1 pre-lecture

- time: 2024-09-01T12:00:00+08:00
- [basics](basics.md)
  - [§ Python basics](basics.md#Python%20basics)
  - [§ arithmetic operators](basics.md#arithmetic%20operators)
    - [basics § arithmetic operators](basics.md#arithmetic%20operators) / note ::: They really like testing you on the return type of operators... for a somewhat obvious reason.
  - [§ mathematics](basics.md#mathematics)
  - [§ string](basics.md#string)
    - [basics § string](basics.md#string) / note ::: They taught `'''` but not `"""` for some reason... But it was later taught in the [week 2 lab](#week%202%20lab) (lab 1).
  - [§ output](basics.md#output)
  - [§ variable](basics.md#variable)
    - [basics § variable](basics.md#variable) / note ::: In a quiz question, they use the word "save", which means storing a value to a variable.
  - [§ data types](basics.md#data%20types)
    - [basics § data types](basics.md#data%20types) / note ::: They have not taught `bool` (values: `True`, `False`) and `NoneType` (value: `None`) up to this point...
- week 1 exercise: 1/1, graded

## week 1 lecture

- time: 2024-09-06T16:00:00+08:00/2024-09-06T17:50:00+08:00
- course logistics
- [Python](../../../../general/Python.md) ::: It is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability.
  - Python / why ::: beginner-friendly (simple, elegant), free and open-source, runs anywhere, supported by a large community, extensible with libraries (flexible), "batteries included": many standard libraries
- [§ week 1 pre-lecture](#week%201%20pre-lecture)
- [basics](basics.md)
  - [§ string](basics.md#string)
    - addition: string concatenation
- week 1 lecture materials
- week 1 practice question set: 10/10, ungraded

## week 2 pre-lecture

- time: 2024-09-09T12:00:00+08:00
- [basics](basics.md)
  - [§ data type conversion](basics.md#data%20type%20conversion)
  - [§ input](basics.md#input)
    - [basics § input](basics.md#input) / note ::: It seems like Jupyter automatically adds a space after the prompt... But other environments do not. Also, the prompt is optional (i.e. `input()` is okay and does not print anything before asking for user input). Lastly, `prompt` does not need to be a `str`, and other objects are accepted. This is similar to `print(...)`, except that a newline is NOT automatically printed, and it only accepts a single argument (i.e. `input("a", "b")` is NOT okay).
- [list](list.md)
  - [§ Python list](list.md#Python%20list)
  - [§ syntax](list.md#syntax)
  - [§ indexing](list.md#indexing)
    - [list § indexing](list.md#indexing) / note ::: We have not learnt slicing so far, so do not use it.
  - [§ manipulation](list.md#manipulation)
  - [§ length](list.md#length)
  - [§ aggregate functions](list.md#aggregate%20functions)
- week 2 exercise: 1/1, graded
- week 3 lab attendance waiver

## week 2 lab

- time: 2024-09-10T11:00:00+08:00/2024-09-10T12:50:00+08:00
- course logistics
- [basics](basics.md)
  - [§ arithmetic operators](basics.md#arithmetic%20operators)
  - [§ mathematics](basics.md#mathematics)
  - [§ string](basics.md#string)
  - [§ output](basics.md#output)
  - [§ variable](basics.md#variable)
  - [§ data types](basics.md#data%20types)
- week 2 lab tasks: 1/1, graded

## week 2 lecture

- time: 2024-09-13T16:00:00+08:00/2024-09-13T17:50:00+08:00
- [§ week 2 pre-lecture](#week%202%20pre-lecture)
- [list](list.md)
  - [§ manipulation](list.md#manipulation)
    - addition: list concatenation
  - [§ search functions](list.md#search%20functions)
    - addition: `list.count(val)`, `list.index(val)`
- week 2 lecture materials
- week 2 practice question set: 10/10, ungraded

## week 3 pre-lecture

- time: 2024-09-16T12:00:00+08:00
- [basics](basics.md)
  - [§ data types](basics.md#data%20types)
    - addition: type `bool`
  - [§ comparison operators](basics.md#comparison%20operators)
- [control flow](control%20flow.md)
  - [§ Python control flow](control%20flow.md#Python%20control%20flow)
  - [§ branching](control%20flow.md#branching)
    - [control flow § branching](control%20flow.md#branching) / note ::: If there are no statements to be executed in a branch, you must still put a properly indented `pass` statement, which does nothing, for that branch.
- [basics](basics.md)
  - [§ logic operators](basics.md#logic%20operators)
- week 3 exercise: 1/1, graded
- week 4 lab attendance waiver
