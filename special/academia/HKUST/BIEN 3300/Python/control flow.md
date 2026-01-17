---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {@{Indentation matters in Python, so do not omit the indentations shown below.}@} <!--SR:!2026-08-10,234,330-->

## branching

An `if` statement consists of {@{a condition and a statement block}@}: <!--SR:!2026-09-26,258,330-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: If {@{the condition is `true`, then the following statement is executed}@}. Otherwise, {@{it is not executed}@}. Note that the condition itself is {@{always executed}@}. <!--SR:!2026-04-24,149,310!2026-12-16,339,347!2026-12-21,344,347-->

An `if...else` statement consists of {@{a condition and two statement blocks}@}: <!--SR:!2026-08-21,245,330-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: If {@{the condition is `true`, then the first statement block is executed}@}. Otherwise, {@{the second statement block is executed}@}. Note that the condition itself is {@{always executed}@}. <!--SR:!2026-08-12,237,330!2026-12-20,343,347!2026-12-13,336,347-->

In Python, one usually does not chain `if...else`. Instead, Python provides {@{the keyword `elif`}@} so that {@{`if...elif...else` represents the chained `if...else if...else` in most programming languages}@}: <!--SR:!2026-09-28,260,330!2026-12-22,345,347-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

{@{The semantics of `if...elif...else`}@} can be found by {@{considering the semantics of chaining `if...else`}@}: {@{The statement block after the first `true` condition}@} is {@{executed}@}. If there are {@{no `true` conditions}@}, {@{the statement block after `else` is executed}@} if {@{there is an `else`}@}. Otherwise, {@{nothing is executed}@}. Note that {@{the conditions up until the first `true` condition \(inclusive\)}@} are themselves {@{always executed in the appearance order}@}, ignoring {@{statement blocks along the way}@}. If {@{there are no `true` conditions}@}, {@{all conditions}@} are always {@{executed in the appearance order}@}, followed by {@{the `else` statement block if there is one}@}. <!--SR:!2026-10-01,263,330!2026-10-09,271,330!2026-08-31,253,330!2026-08-30,252,330!2026-10-08,270,330!2026-10-27,289,330!2026-10-15,277,330!2026-10-31,293,330!2026-08-31,253,330!2026-08-18,241,330!2026-10-29,291,330!2026-10-18,280,330!2026-10-23,285,330!2026-10-11,273,330!2026-10-20,282,330-->

If there are {@{no statements to be executed in a branch}@}, you {@{must still put a properly indented `pass` statement}@}, which {@{does nothing, for that branch}@}. This is also {@{true for other control flow constructs introduced below}@}. For example: <!--SR:!2026-10-28,290,330!2026-10-26,288,330!2026-08-10,235,330!2026-04-09,88,370-->

```Python
if condition:
  pass # required, otherwise error
```

Python has {@{no `switch` statements}@}. Since {@{Python 3.10}@}, Python has {@{a similar construct called `match...case` statement}@}, but it will {@{not be described here}@}. <!--SR:!2026-10-17,279,330!2026-08-26,249,330!2026-11-01,294,330!2026-10-03,265,330-->

## iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {@{loop variables, iterable, and a statement block}@}: <!--SR:!2026-10-19,281,330-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {@{ranges, strings, lists, and many more not mentioned here}@}. The semantics of `for...in` is that for {@{each element in the iterable}@}, {@{the loop variables are assigned that element}@} and then {@{the statement block is executed}@}. <!--SR:!2026-10-06,268,330!2026-08-06,232,330!2026-12-18,341,347!2026-12-14,337,347-->

To emulate the traditional `for` loop, one uses {@{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}@}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {@{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}@}. `range(begin, end, step)` has shorter forms: {@{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}@}. <!--SR:!2026-08-11,235,330!2026-09-25,257,330!2026-08-11,237,330-->

In Python, `while` can also perform iteration. A `while` statement consists of {@{a condition and a statement block}@}: <!--SR:!2026-10-10,272,330-->

```Python
while condition:
  statement_block
```

The semantics of `while` is that {@{the condition is executed first}@}. If {@{the condition is `true`}@}, the statement block is {@{executed and then we repeat the above process again}@}. If {@{the condition is `false`}@}, {@{the `while` statement ends its execution}@}. <!--SR:!2026-10-13,275,330!2026-12-15,338,347!2026-12-19,342,347!2026-12-17,340,347!2026-12-17,340,347-->

If there are {@{no statements to be executed in an iteration}@}, you {@{must still put a properly indented `pass` statement}@}, which {@{does nothing, for that iteration}@}. For example: <!--SR:!2026-10-21,283,330!2026-10-14,276,330!2026-04-05,84,370-->

```Python
for loop_variables in iterable:
  pass # required, otherwise error
```

```Python
while condition:
  pass # required, otherwise error
```

You can of course {@{put branches and loops}@} inside loops. <!--SR:!2026-08-10,236,330-->
