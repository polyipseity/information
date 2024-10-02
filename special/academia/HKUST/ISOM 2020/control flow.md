---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {{Indentation matters in Python, so do not omit the indentations shown below.}} <!--SR:!2024-10-09,15,290-->

## branching

An `if` statement consists of {{a condition and a statement block}}: <!--SR:!2024-10-09,15,290-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}} <!--SR:!2024-10-07,13,290-->

An `if...else` statement consists of {{a condition and two statement blocks}}: <!--SR:!2024-10-07,13,290-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}} <!--SR:!2024-10-07,13,290-->

In Python, one usually does not chain `if...else`. Instead, Python provides {{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}}: <!--SR:!2024-10-08,14,290-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}}. Note that {{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, ignoring statement blocks along the way. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one}}. <!--SR:!2024-10-11,17,290!2024-10-05,11,270-->

If {{there are no statements to be executed in a branch}}, you {{must still put a properly indented `pass` statement, which does nothing, for that branch}}. This is also {{true for other control flow constructs introduced below}}. For example: <!--SR:!2024-10-08,14,290!2024-11-16,45,290!2024-10-10,16,290-->

```Python
if condition:
  pass # required, otherwise error
```

Python has {{no `switch` statements before Python 3.10. Since Python 3.10, Python has `match...case` statement, but it will not be described here}}. <!--SR:!2024-10-11,17,290-->

## iteration

You can of course {{put branches and loops}} inside loops. <!--SR:!2024-10-18,18,312-->

### for-iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {{loop variables, iterable, and a statement block}}: <!--SR:!2024-10-18,18,312-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {{ranges, strings, lists, and many more not mentioned here}}. The semantics of `for...in` is that {{for each element in the iterable, the loop variables are assigned that element and then the statement block is executed}}. <!--SR:!2024-10-18,18,312!2024-10-18,18,312-->

To emulate the traditional `for` loop, one uses {{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}}. `range(begin, end, step)` has shorter forms: {{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}}. <!--SR:!2024-10-18,18,312!2024-10-18,18,312!2024-10-18,18,312-->

If {{there are no statements to be executed in an iteration}}, you {{must still put a properly indented `pass` statement, which does nothing, for that iteration}}. For example: <!--SR:!2024-10-18,18,312!2024-10-18,18,312-->

```Python
for loop_variables in iterable:
  pass # required, otherwise error
```
