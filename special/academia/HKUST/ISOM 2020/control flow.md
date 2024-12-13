---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {@{Indentation matters in Python, so do not omit the indentations shown below.}@} <!--SR:!2025-06-11,196,310-->

## branching

An `if` statement consists of {@{a condition and a statement block}@}: <!--SR:!2025-08-23,258,330-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {@{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}@} <!--SR:!2025-07-18,230,330-->

An `if...else` statement consists of {@{a condition and two statement blocks}@}: <!--SR:!2025-07-14,226,330-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {@{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}@} <!--SR:!2025-06-29,215,330-->

In Python, one usually does not chain `if...else`. Instead, Python provides {@{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}@}: <!--SR:!2025-07-22,233,330-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {@{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}@}. Note that {@{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, ignoring statement blocks along the way. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one}@}. <!--SR:!2024-12-24,68,310!2025-05-05,167,310-->

If {@{there are no statements to be executed in a branch}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that branch}@}. This is also {@{true for other control flow constructs introduced below}@}. For example: <!--SR:!2025-05-20,180,310!2025-05-18,183,310!2025-09-17,278,330-->

```Python
if condition:
  pass # required, otherwise error
```

Python has {@{no `switch` statements before Python 3.10. Since Python 3.10, Python has `match...case` statement, but it will not be described here}@}. <!--SR:!2024-12-24,68,310-->

## iteration

You can of course {@{put branches (`if`) and loops (`for`, `while`)}@} inside loops. <!--SR:!2025-01-03,77,332-->

### for-iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {@{loop variables, iterable, and a statement block}@}: <!--SR:!2024-12-15,58,312-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {@{ranges, strings, lists, and many more not mentioned here}@}. The semantics of `for...in` is that {@{for each element in the iterable, the loop variables are assigned that element and then the statement block is executed}@}. <!--SR:!2025-01-03,77,332!2025-01-03,77,332-->

To emulate the traditional `for` loop, one uses {@{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}@}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {@{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}@}. `range(begin, end, step)` has shorter forms: {@{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}@}. <!--SR:!2025-01-03,77,332!2025-01-03,77,332!2025-01-03,77,332-->

If {@{there are no statements to be executed in a `for`-iteration}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that iteration}@}. For example: <!--SR:!2025-05-21,167,337!2024-12-16,49,337-->

```Python
for loop_variables in iterable:
  pass # required, otherwise error
```

If {@{you want to stop a `for` loop early}@}, use {@{the `break` statement}@}. This will {@{stop the innermost `for` or `while` loop}@}. <!--SR:!2025-01-30,86,351!2025-02-02,89,351!2025-02-02,89,351-->

### while-iteration

In Python, `while` can also perform iteration. A `while` statement consists of {@{a condition and a statement block}@}: <!--SR:!2025-02-03,90,351-->

```Python
while condition:
  statement_block
```

The semantics of `while` is {@{that the condition is executed first. If the condition is `true`, the statement block is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}@}. <!--SR:!2025-02-02,89,351-->

If {@{there are no statements to be executed in a `while`-iteration}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that iteration}@}. For example: <!--SR:!2025-02-07,93,357!2025-02-06,92,357-->

```Python
while condition:
  pass # required, otherwise error
```

If {@{you want to stop a `while` loop early in the loop}@}, use {@{the `break` statement}@}. This will {@{stop the innermost `for` or `while` loop}@}. <!--SR:!2025-01-29,85,351!2025-02-01,88,351!2025-02-01,88,351-->

ISOM 2020 note: {@{We have only learnt `while True`. ONLY USE `while True` in your exercises, labs, and exams.}@} If {@{you really need a condition to stop the loop}@}, use {@{`break` under an `if` statement checking for said condition}@}. <!--SR:!2025-01-30,86,351!2025-02-03,90,351!2025-01-30,86,351-->
