---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {@{Indentation matters in Python, so do not omit the indentations shown below.}@} <!--SR:!2026-04-29,464,378-->

## branching

An `if` statement consists of {@{a condition and a statement block}@}: <!--SR:!2027-05-23,934,350-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: If {@{the condition is `true`, then the following statement is executed}@}. Otherwise, {@{it is not executed}@}. Note that the condition itself is {@{always executed}@}. <!--SR:!2026-10-09,736,330!2026-03-26,141,409!2026-03-25,140,409-->

An `if...else` statement consists of {@{a condition and two statement blocks}@}: <!--SR:!2026-09-05,710,330-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: If {@{the condition is `true`, then the first statement block is executed}@}. Otherwise, {@{the second statement block is executed}@}. Note that the condition itself is {@{always executed}@}. <!--SR:!2026-09-16,720,330!2026-03-20,136,409!2026-03-20,136,409-->

In Python, one usually does not chain `if...else`. Instead, Python provides {@{the keyword `elif`}@} so that {@{`if...elif...else` represents the chained `if...else if...else` in most programming languages}@}: <!--SR:!2028-07-01,1256,350!2026-03-25,140,409-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

{@{The semantics of `if...elif...else`}@} can be found by {@{considering the semantics of chaining `if...else`}@}: {@{The statement block after the first `true` condition}@} is {@{executed}@}. If there are {@{no `true` conditions}@}, {@{the statement block after `else` is executed}@} if {@{there is an `else`}@}. Otherwise, {@{nothing is executed}@}. Note that {@{the conditions up until the first `true` condition \(inclusive\)}@} are themselves {@{always executed in the appearance order}@}, ignoring {@{statement blocks along the way}@}. If {@{there are no `true` conditions}@}, {@{all conditions}@} are always {@{executed in the appearance order}@}, followed by {@{the `else` statement block if there is one}@}. <!--SR:!2026-07-11,611,310!2027-04-01,807,323!2026-01-01,98,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-04,101,385!2026-01-06,103,385!2026-01-06,103,385!2026-01-05,102,385!2026-01-03,100,385!2026-01-06,103,385-->

If there are {@{no statements to be executed in a branch}@}, you {@{must still put a properly indented `pass` statement}@}, which {@{does nothing, for that branch}@}. This is also {@{true for other control flow constructs introduced below}@}. For example: <!--SR:!2026-05-02,467,378!2026-05-01,466,378!2026-05-03,468,378-->

```Python
if condition:
  pass # required, otherwise error
```

Python has {@{no `switch` statements}@}. Since {@{Python 3.10}@}, Python has {@{a similar construct called `match...case` statement}@}, but it will {@{not be described here}@}. <!--SR:!2027-05-07,892,330!2026-03-26,141,407!2026-03-12,129,407!2026-03-19,135,407-->

## iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {@{loop variables, iterable, and a statement block}@}: <!--SR:!2028-06-10,1233,350-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {@{ranges, strings, lists, and many more not mentioned here}@}. The semantics of `for...in` is that for {@{each element in the iterable}@}, {@{the loop variables are assigned that element}@} and then {@{the statement block is executed}@}. <!--SR:!2028-03-08,1160,350!2026-08-20,694,330!2026-03-14,131,409!2026-03-20,136,409-->

To emulate the traditional `for` loop, one uses {@{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}@}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {@{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}@}. `range(begin, end, step)` has shorter forms: {@{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}@}. <!--SR:!2028-07-15,1267,350!2026-01-21,492,310!2028-10-23,1342,350-->

In Python, `while` can also perform iteration. A `while` statement consists of {@{a condition and a statement block}@}: <!--SR:!2028-06-13,1240,350-->

```Python
while condition:
  statement_block
```

The semantics of `while` is that {@{the condition is executed first}@}. If {@{the condition is `true`}@}, the statement block is {@{executed and then we repeat the above process again}@}. If {@{the condition is `false`}@}, {@{the `while` statement ends its execution}@}. <!--SR:!2027-07-18,903,330!2026-03-26,141,409!2026-03-25,140,409!2026-03-14,131,409!2026-03-26,141,409-->

If there are {@{no statements to be executed in an iteration}@}, you {@{must still put a properly indented `pass` statement}@}, which {@{does nothing, for that iteration}@}. For example: <!--SR:!2026-04-12,450,385!2030-05-09,1617,385-->

```Python
for loop_variables in iterable:
  pass # required, otherwise error
```

```Python
while condition:
  pass # required, otherwise error
```

You can of course {@{put branches and loops}@} inside loops. <!--SR:!2026-03-04,420,385-->
