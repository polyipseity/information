---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {@{Indentation matters in Python, so do not omit the indentations shown below.}@}

## branching

An `if` statement consists of {@{a condition and a statement block}@}:

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {@{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}@}

An `if...else` statement consists of {@{a condition and two statement blocks}@}:

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {@{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}@}

In Python, one usually does not chain `if...else`. Instead, Python provides {@{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}@}:

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

{@{The semantics of `if...elif...else`}@} can be found by {@{considering the semantics of chaining `if...else`}@}: {@{The statement block after the first `true` condition}@} is {@{executed}@}. If there are {@{no `true` conditions}@}, {@{the statement block after `else` is executed}@} if {@{there is an `else`}@}. Otherwise, {@{nothing is executed}@}. Note that {@{the conditions up until the first `true` condition \(inclusive\)}@} are themselves {@{always executed in the appearance order}@}, ignoring {@{statement blocks along the way}@}. If {@{there are no `true` conditions}@}, {@{all conditions}@} are always {@{executed in the appearance order}@}, followed by {@{the `else` statement block if there is one}@}.

If {@{there are no statements to be executed in a branch}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that branch}@}. This is also {@{true for other control flow constructs introduced below}@}. For example:

```Python
if condition:
  pass # required, otherwise error
```

Python has {@{no `switch` statements before Python 3.10. Since Python 3.10, Python has `match...case` statement, but it will not be described here}@}.

## iteration

You can of course {@{put branches (`if`) and loops (`for`, `while`)}@} inside loops.

### for-iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {@{loop variables, iterable, and a statement block}@}:

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {@{ranges, strings, lists, and many more not mentioned here}@}. The semantics of `for...in` is that {@{for each element in the iterable, the loop variables are assigned that element and then the statement block is executed}@}.

To emulate the traditional `for` loop, one uses {@{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}@}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {@{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}@}. `range(begin, end, step)` has shorter forms: {@{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}@}.

If {@{there are no statements to be executed in a `for`-iteration}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that iteration}@}. For example:

```Python
for loop_variables in iterable:
  pass # required, otherwise error
```

If {@{you want to stop a `for` loop early}@}, use {@{the `break` statement}@}. This will {@{stop the innermost `for` or `while` loop}@}.

### while-iteration

In Python, `while` can also perform iteration. A `while` statement consists of {@{a condition and a statement block}@}:

```Python
while condition:
  statement_block
```

The semantics of `while` is {@{that the condition is executed first. If the condition is `true`, the statement block is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}@}.

If {@{there are no statements to be executed in a `while`-iteration}@}, you {@{must still put a properly indented `pass` statement, which does nothing, for that iteration}@}. For example:

```Python
while condition:
  pass # required, otherwise error
```

If {@{you want to stop a `while` loop early in the loop}@}, use {@{the `break` statement}@}. This will {@{stop the innermost `for` or `while` loop}@}.

ISOM 2020 note: {@{We have only learnt `while True`. ONLY USE `while True` in your exercises, labs, and exams.}@} If {@{you really need a condition to stop the loop}@}, use {@{`break` under an `if` statement checking for said condition}@}.
