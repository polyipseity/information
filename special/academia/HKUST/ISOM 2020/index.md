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

- general recommendations ::@:: Do NOT use techniques not learnt in lectures! Also, if you have learnt Python before well, you would find a few quiz questions ambiguous with imprecise wordings. Good luck guessing the answer... <!--SR:!2025-06-19,218,329!2025-05-10,185,329-->
- course logistics
  - pathway: ISOM 2020 → ISOM 2600
  - duration: 7 weeks, for the first half of the semester
  - time: 2 hour lectures, 2 hour labs
  - format: pre-lecture videos → weekly exercise (graded, infinite attempts) → lecture → lab (graded, attendance required) → practice question set (ungraded, optional)
  - grading scheme: weekly exercise 10%, lab submissions 20%, final examination 70% (basic programming test 45%, free coding exam 25%)
  - course intended learning outcomes (CILOs): understand coding logic, Python basics, and hands-on guidance
  - lab: attendance required, can be waived by doing a challenging exercise and demonstrate it to lab helpers at the start of the lab to be waived
- [assignments](assignments/)
- final examination: 2024-10-19T15:00:00+08:00/2024-10-19T16:30:00+08:00 (PT1H30M)

## week 1 pre-lecture

- datetime: 2024-09-01T12:00:00+08:00
- [basics](basics.md)
  - [§ Python basics](basics.md#Python%20basics)
  - [§ arithmetic operators](basics.md#arithmetic%20operators)
    - [basics § arithmetic operators](basics.md#arithmetic%20operators) / note ::@:: They really like testing you on the return type of operators... for a somewhat obvious reason. <!--SR:!2024-11-16,56,318!2025-04-17,158,310-->
  - [§ mathematics](basics.md#mathematics)
  - [§ string](basics.md#string)
    - [basics § string](basics.md#string) / note ::@:: They taught `'''` but not `"""` for some reason... But it was later taught in the [week 2 lab](#week%202%20lab) (lab 1). <!--SR:!2025-06-22,222,332!2025-03-20,147,310-->
  - [§ output](basics.md#output)
    - [basics § output](basics.md#output) / note ::@:: Jupyter notebooks automatically outputting the value of the last statement without using `print` is also considered "output". Note that strings are outputted, escaped with `\` properly (without unnecessary escapes), and preferably wrapped in `'`, and only uses `"` if there is at least 1 `'` in the string but not any `"`. <!--SR:!2025-03-25,141,323!2024-11-25,48,323-->
  - [§ variable](basics.md#variable)
    - [basics § variable](basics.md#variable) / note ::@:: In a quiz question, they use the word "save", which means storing a value to a variable. Also, `+=`, `-=`, `*=`, `/=`, etc. are not taught and should NOT be used in exercises or exams. <!--SR:!2025-04-19,170,312!2025-03-22,146,312-->
  - [§ data types](basics.md#data%20types)
    - [basics § data types](basics.md#data%20types) / note ::@:: They have not taught `bool` (values: `True`, `False`) and `NoneType` (value: `None`) up to this point... <!--SR:!2025-01-10,92,292!2024-11-22,59,312-->
- week 1 exercise: 1/1, graded
  - Can variables be used to save user input? ::@:: Yes, variables can be used to save user input (store in a variable). <!--SR:!2025-02-15,97,366!2025-02-12,94,366-->
  - Can `print(...)` be used to save data? ::@:: No, `print(...)` cannot be used to save data (store in a variable), only display data. <!--SR:!2025-02-12,94,366!2025-02-13,95,366-->

## week 1 lecture

- datetime: 2024-09-06T16:00:00+08:00/2024-09-06T17:50:00+08:00
- course logistics
- [Python](../../../../general/Python.md) ::@:: It is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability. <!--SR:!2024-11-20,51,309!2024-12-17,77,329-->
  - Python / why ::@:: beginner-friendly (simple, elegant), free and open-source, runs anywhere, supported by a large community, extensible with libraries (flexible), "batteries included": many standard libraries <!--SR:!2025-04-12,159,309!2024-11-21,54,309-->
- [§ week 1 pre-lecture](#week%201%20pre-lecture)
- [basics](basics.md)
  - [§ string](basics.md#string)
    - addition: string concatenation
- week 1 lecture materials
- week 1 practice question set: 10/10, ungraded
  - Python becomes very popular due to the following reasons, except for... ::@:: It executes the fastest as compared to other programming languages. <!--SR:!2025-02-10,92,366!2025-02-13,95,366-->

## week 2 pre-lecture

- datetime: 2024-09-09T12:00:00+08:00
- [basics](basics.md)
  - [§ data type conversion](basics.md#data%20type%20conversion)
  - [§ input](basics.md#input)
    - [basics § input](basics.md#input) / note ::@:: It seems like Jupyter automatically adds a space after the prompt... But other environments do not. Also, the prompt is optional (i.e. `input()` is okay and does not print anything before asking for user input). Lastly, `prompt` does not need to be a `str`, and other objects are accepted. This is similar to `print(...)`, except that a newline is NOT automatically printed, and it only accepts a single argument (i.e. `input("a", "b")` is NOT okay). <!--SR:!2025-03-22,142,309!2024-12-22,81,329-->
- [list](list.md)
  - [§ Python list](list.md#Python%20list)
  - [§ syntax](list.md#syntax)
  - [§ indexing](list.md#indexing)
    - [list § indexing](list.md#indexing) / note ::@:: We have not learnt slicing so far, so do not use it. <!--SR:!2025-01-02,77,344!2025-01-02,77,344-->
  - [§ manipulation](list.md#manipulation)
  - [§ length](list.md#length)
  - [§ aggregate functions](list.md#aggregate%20functions)
- week 2 exercise: 1/1, graded
  - Can a list be sliced? ::@:: Yes! But you cannot use this in exercises or exams. <!--SR:!2025-02-14,96,366!2025-02-16,98,366-->
- [week 3 lab attendance waiver](assignments/lab%202/lab%202%20waiver%20submission.ipynb): 1/1, graded

## week 2 lab

- datetime: 2024-09-10T11:00:00+08:00/2024-09-10T12:50:00+08:00
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

- datetime: 2024-09-13T16:00:00+08:00/2024-09-13T17:50:00+08:00
- [§ week 2 pre-lecture](#week%202%20pre-lecture)
- [list](list.md)
  - [§ manipulation](list.md#manipulation)
    - addition: list concatenation
  - [§ search functions](list.md#search%20functions)
    - addition: `list.count(val)`, `list.index(val)`
- week 2 lecture materials
- week 2 practice question set: 10/10, ungraded

## week 3 pre-lecture

- datetime: 2024-09-16T12:00:00+08:00
- [basics](basics.md)
  - [§ data types](basics.md#data%20types)
    - addition: type `bool`
  - [§ comparison operators](basics.md#comparison%20operators)
    - [basics § comparison operators](basics.md#comparison%20operators) / note ::@:: One CAN chain comparison operators in Python, unlike other languages. See contents inside. <!--SR:!2025-01-02,77,352!2025-01-12,86,352-->
- [control flow](control%20flow.md)
  - [§ Python control flow](control%20flow.md#Python%20control%20flow)
  - [§ branching](control%20flow.md#branching)
    - [control flow § branching](control%20flow.md#branching) / note ::@:: If there are no statements to be executed in a branch, you must still put a properly indented `pass` statement, which does nothing, for that branch. <!--SR:!2024-12-22,75,341!2024-12-29,80,341-->
- [basics](basics.md)
  - [§ logic operators](basics.md#logic%20operators)
- week 3 exercise: 1/1, graded
- [week 4 lab attendance waiver](assignments/lab%203/lab%203%20waiver%20submission.ipynb): 1/1, graded

## week 3 lab

- datetime: 2024-09-17T11:00:00+08:00/2024-09-17T12:50:00+08:00
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

- datetime: 2024-09-20T16:00:00+08:00/2024-09-20T17:50:00+08:00
- [§ week 3 pre-lecture](#week%203%20pre-lecture)
- [basics](basics.md)
  - [§ operators](basics.md#operators)
    - additional: operator group precedence
- week 3 lecture materials
- week 3 practice question set: 10/10, ungraded

## week 4 pre-lecture

- datetime: 2024-09-23T12:00:00+08:00
- [control flow](control%20flow.md)
  - [§ for-iteration](control%20flow.md#for-iteration)
    - [control flow § for-iteration](control%20flow.md#for-iteration) / note ::@:: First, we have only learnt about `range(end)` and `list(range(end))`. So do not use the other ways of using `range(...)` in your exams. Second, if there are no statements to be executed in an iteration, you must still put a properly indented `pass` statement, which does nothing, for that iteration. <!--SR:!2024-12-28,72,352!2024-12-28,72,352-->
- [basics](basics.md)
  - [§ data type conversion](basics.md#data%20type%20conversion)
    - addition: `list(value)`
- [control flow](control%20flow.md)
  - [§ iteration](control%20flow.md#iteration)
    - [control flow § iteration](control%20flow.md#iteration) / note ::@:: Yes, did you know you can put branches (`if`) and loops (`for`, `while`) inside branches (`if`) and loops (`for`, `while`)? <!--SR:!2025-01-17,90,352!2024-12-29,74,352-->
- week 4 exercise: 1/1, graded
- [week 5 lab attendance waiver](assignments/lab%204/lab%204%20waiver%20submission.ipynb): ?/1, ignored due to public holiday

## week 4 lab

- datetime: 2024-09-24T11:00:00+08:00/2024-09-24T12:50:00+08:00
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

## week 4 lecture

- datetime: 2024-09-27T16:00:00+08:00/2024-09-27T17:50:00+08:00
- [§ week 4 pre-lecture](#week%204%20pre-lecture)
- [basics](basics.md)
  - [§ output](basics.md#output)
    - addition: `print(end=<str | None = None>)`
- week 4 lecture materials
- week 4 practice question set: 10/10, ungraded

## week 5 pre-lecture

- datetime: 2024-09-30T12:00:00+08:00
- [control flow](control%20flow.md)
  - [§ while-iteration](control%20flow.md#while-iteration)
    - [control flow § while-iteration](control%20flow.md#while-iteration) / note : We have only learnt `while True`. ONLY USE `while True` in your exercises, labs, and exams. If you really need a condition to stop the loop, use `break` under an `if` statement.
  - [§ iteration](control%20flow.md#iteration)
- week 5 exercise: 1/1, graded

## week 5 lab

- datetime: 2024-10-01T11:00:00+08:00/2024-10-01T12:50:00+08:00
- status: unscheduled, public holiday: National Day
- [§ week 4 pre-lecture](#week%204%20pre-lecture)
- [control flow](control%20flow.md)
  - [§ for-iteration](control%20flow.md#for-iteration)
- [week 5 lab tasks](assignments/lab%204/lab%204%20submission.ipynb): 1/1, graded

## week 6 lecture

- datetime: 2024-10-04T16:00:00+08:00/2024-10-04T17:50:00+08:00
- [§ week 5 pre-lecture](#week%205%20pre-lecture)
- [basics](basics.md)
  - [§ mathematics](basics.md#mathematics)
    - addition: `random.randint(a, b)`
- week 6 lecture materials
- week 6 practice question set: 10/10, ungraded
  - How does a 'for' loop differ from a 'while' loop in Python? ::@:: 'for' loops iterate a fixed number of times. <!--SR:!2025-02-14,96,366!2025-02-14,96,366-->
  - What can be a potential pitfall when using the 'while' loop? ::@:: It can lead to infinite loops if the loop termination condition is not met. <!--SR:!2025-01-14,70,346!2025-02-16,98,366-->
  - In a 'while' loop, under what circumstances could an infinite loop occur? ::@:: When the loop condition is always 'True'. <!--SR:!2025-02-15,97,366!2025-02-14,96,366-->

## week 6 lab

- datetime: 2024-10-08T11:00:00+08:00/2024-10-08T12:50:00+08:00
- [§ week 5 pre-lecture](#week%205%20pre-lecture)
- [control flow](control%20flow.md)
  - [§ while-iteration](control%20flow.md#while-iteration)
  - [§ for-iteration](control%20flow.md#for-iteration)
- challenging questions
- exam dos, don'ts, and tips
- [week 6 lab tasks](assignments/lab%205/lab%205%20submission.py): 1/1, graded

## week 7 lecture

- datetime: 2024-10-11T16:00:00+08:00/2024-10-11T17:50:00+08:00
- status: unscheduled, public holiday: Chung Yeung Festival
- common mistakes
  - `=` vs `==` ::@:: Do not mix up the assignment operator and comparison operator. <!--SR:!2025-02-13,95,366!2025-02-12,94,366-->
  - `input(...)` return type ::@:: `input(...)` returns a `str` and may require further conversions. <!--SR:!2025-02-16,98,366!2025-02-11,93,366-->
  - `//` vs `%` ::@:: Do not mix up the floor division operator and remainder operator. <!--SR:!2025-02-16,98,366!2025-02-11,93,366-->
  - `print(...)` multiple arguments ::@:: Note that if multiple arguments are passed to `print(...)`, the outputted strings are separated by a space in between arguments. <!--SR:!2025-02-10,92,366!2025-02-22,103,380-->
  - indentation ::@:: Indentation matters in Python!!! <!--SR:!2025-02-15,97,366!2025-02-15,97,366-->
  - `break` notes ::@:: Do not forget to add `break` when needed to exit the loop. The indentation of `break` matters. Also, `break` only exits the innermost loop and does not affect outer loops. <!--SR:!2025-02-16,98,366!2025-02-15,97,366-->
- week 7 lecture materials
- integrated question set (week 7 practice question set): 0/0, ungraded

## final examination

- datetime: 2024-10-19T15:00:00+08:00/2024-10-19T16:30:00+08:00, PT1H30M
- venue: Lecture Theater B, Lecture Theater C, Lecture Theater J, Lecture Theater L
- [cheatsheet](cheatsheet.md): provided during the examination
- grades: ?/?
- report
  - There is neither paper checking nor result release.

## aftermath

- They do not release final examination marks.
