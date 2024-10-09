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

- general recommendations ::: Do NOT use techniques not learnt in lectures! Also, if you have learnt Python before well, you would find a few quiz questions ambiguous with imprecise wordings. Good luck guessing the answer... <!--SR:!2024-11-13,50,309!2024-11-06,43,309-->
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
    - [basics § arithmetic operators](basics.md#arithmetic%20operators) / note ::: They really like testing you on the return type of operators... for a somewhat obvious reason. <!--SR:!2024-11-16,56,318!2024-11-10,50,310-->
  - [§ mathematics](basics.md#mathematics)
  - [§ string](basics.md#string)
    - [basics § string](basics.md#string) / note ::: They taught `'''` but not `"""` for some reason... But it was later taught in the [week 2 lab](#week%202%20lab) (lab 1). <!--SR:!2024-11-12,52,312!2024-10-24,37,290-->
  - [§ output](basics.md#output)
    - [basics § output](basics.md#output) / note ::: Jupyter notebooks automatically outputting the value of the last statement without using `print` is also considered "output". Note that strings are outputted, escaped with `\` properly (without unnecessary escapes), and preferably wrapped in `'`, and only uses `"` if there is at least 1 `'` in the string but not any `"`. <!--SR:!2024-11-04,33,303!2024-11-25,48,323-->
  - [§ variable](basics.md#variable)
    - [basics § variable](basics.md#variable) / note ::: In a quiz question, they use the word "save", which means storing a value to a variable. <!--SR:!2024-10-31,40,292!2024-10-27,36,292-->
  - [§ data types](basics.md#data%20types)
    - [basics § data types](basics.md#data%20types) / note ::: They have not taught `bool` (values: `True`, `False`) and `NoneType` (value: `None`) up to this point... <!--SR:!2024-10-10,24,272!2024-11-22,59,312-->
- week 1 exercise: 1/1, graded

## week 1 lecture

- time: 2024-09-06T16:00:00+08:00/2024-09-06T17:50:00+08:00
- course logistics
- [Python](../../../../general/Python.md) ::: It is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability. <!--SR:!2024-11-20,51,309!2024-12-17,77,329-->
  - Python / why ::: beginner-friendly (simple, elegant), free and open-source, runs anywhere, supported by a large community, extensible with libraries (flexible), "batteries included": many standard libraries <!--SR:!2024-11-04,39,289!2024-11-21,54,309-->
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
    - [basics § input](basics.md#input) / note ::: It seems like Jupyter automatically adds a space after the prompt... But other environments do not. Also, the prompt is optional (i.e. `input()` is okay and does not print anything before asking for user input). Lastly, `prompt` does not need to be a `str`, and other objects are accepted. This is similar to `print(...)`, except that a newline is NOT automatically printed, and it only accepts a single argument (i.e. `input("a", "b")` is NOT okay). <!--SR:!2024-10-30,34,289!2024-12-22,81,329-->
- [list](list.md)
  - [§ Python list](list.md#Python%20list)
  - [§ syntax](list.md#syntax)
  - [§ indexing](list.md#indexing)
    - [list § indexing](list.md#indexing) / note ::: We have not learnt slicing so far, so do not use it. <!--SR:!2024-10-11,17,324!2024-10-12,18,324-->
  - [§ manipulation](list.md#manipulation)
  - [§ length](list.md#length)
  - [§ aggregate functions](list.md#aggregate%20functions)
- week 2 exercise: 1/1, graded
- [week 3 lab attendance waiver](assignments/lab%202/lab%202%20waiver%20submission.ipynb): 1/1, graded

## week 2 lab

- time: 2024-09-10T11:00:00+08:00/2024-09-10T12:50:00+08:00
- course logistics
- [§ week 1 pre-lecture](#week%201%20pre-lecture)
- [basics](basics.md)
  - [§ arithmetic operators](basics.md#arithmetic%20operators)
  - [§ mathematics](basics.md#mathematics)
  - [§ string](basics.md#string)
  - [§ output](basics.md#output)
  - [§ variable](basics.md#variable)
  - [§ data types](basics.md#data%20types)
- [week 2 lab tasks](assignments/lab%201/lab%201%20submission.ipynb): 1/1, graded

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
    - [basics § comparison operators](basics.md#comparison%20operators) / note ::: One CAN chain comparison operators in Python, unlike other languages. See contents inside. <!--SR:!2024-10-17,17,332!2024-10-18,18,332-->
- [control flow](control%20flow.md)
  - [§ Python control flow](control%20flow.md#Python%20control%20flow)
  - [§ branching](control%20flow.md#branching)
    - [control flow § branching](control%20flow.md#branching) / note ::: If there are no statements to be executed in a branch, you must still put a properly indented `pass` statement, which does nothing, for that branch. <!--SR:!2024-12-22,75,341!2024-10-09,18,321-->
- [basics](basics.md)
  - [§ logic operators](basics.md#logic%20operators)
- week 3 exercise: 1/1, graded
- [week 4 lab attendance waiver](assignments/lab%203/lab%203%20waiver%20submission.ipynb): 1/1, graded

## week 3 lab

- time: 2024-09-17T11:00:00+08:00/2024-09-17T12:50:00+08:00
- [§ week 2 pre-lecture](#week%202%20pre-lecture)
- [basics](basics.md)
  - [§ data types](basics.md#data%20types)
  - [§ data type conversion](basics.md#data%20type%20conversion)
  - [§ output](basics.md#output)
  - [§ input](basics.md#input)
- [list](list.md)
  - [§ Python list](list.md#Python%20list)
  - [§ syntax](list.md#syntax)
  - [§ indexing](list.md#indexing)
  - [§ manipulation](list.md#manipulation)
  - [§ length](list.md#length)
  - [§ aggregate functions](list.md#aggregate%20functions)
- week 3 lab tasks: ?/1, waived

## week 3 lecture

- time: 2024-09-20T16:00:00+08:00/2024-09-20T17:50:00+08:00
- [§ week 3 pre-lecture](#week%203%20pre-lecture)
- [basics](basics.md)
  - [§ operators](basics.md#operators)
    - additional: operator group precedence
- week 3 lecture materials
- week 3 practice question set: 10/10, ungraded

## week 4 pre-lecture

- time: 2024-09-23T12:00:00+08:00
- [control flow](control%20flow.md)
  - [§ for-iteration](control%20flow.md#for-iteration)
    - [control flow § for-iteration](control%20flow.md#for-iteration) / note ::: First, we have only learnt about `range(end)` and `list(range(end))`. So do not use the other ways of using `range(...)` in your exams. Second, if there are no statements to be executed in an iteration, you must still put a properly indented `pass` statement, which does nothing, for that iteration. <!--SR:!2024-10-15,15,332!2024-10-15,15,332-->
- [basics](basics.md)
  - [§ data type conversion](basics.md#data%20type%20conversion)
    - addition: `list(value)`
- [control flow](control%20flow.md)
  - [§ iteration](control%20flow.md#iteration)
    - [control flow § iteration](control%20flow.md#iteration) / note ::: Yes, did you know you can put branches (`if`) and loops (`for`) inside branches (`if`) and loops (`for`)? <!--SR:!2024-10-19,19,332!2024-10-16,16,332-->
- week 4 exercise: 1/1, graded
- [week 5 lab attendance waiver](assignments/lab%204/lab%204%20waiver%20submission.ipynb)

## week 4 lab

- time: 2024-09-24T11:00:00+08:00/2024-09-24T12:50:00+08:00
- [§ week 3 pre-lecture](#week%203%20pre-lecture)
- [basics](basics.md)
  - [§ data types](basics.md#data%20types)
    - addition: type `bool`
  - [§ data type conversion](basics.md#data%20type%20conversion)
    - addition: `bool(value)`
  - [§ comparison operators](basics.md#comparison%20operators)
- [control flow](control%20flow.md)
  - [§ Python control flow](control%20flow.md#Python%20control%20flow)
  - [§ branching](control%20flow.md#branching)
- [basics](basics.md)
  - [§ logic operators](basics.md#logic%20operators)
- week 4 lab tasks: ?/1, waived
