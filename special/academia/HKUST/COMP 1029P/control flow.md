---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/control_flow
  - language/in/English
---

# Python control flow

## branching

An `if` statement consists of {{a condition and a statement block}}: <!--SR:!2024-04-06,48,310-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}} <!--SR:!2024-04-14,55,310-->

An `if...else` statement consists of {{a condition and two statement blocks}}: <!--SR:!2024-04-11,52,310-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}} <!--SR:!2024-04-11,53,310-->

In Python, one usually does not chain `if...else`. Instead, Python provides {{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}}: <!--SR:!2024-04-21,61,310-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}}. Note that {{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, alternated with statement block execution. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one.}} <!--SR:!2024-04-24,63,310!2024-05-08,75,323-->

Python has no {{`switch` statements}}. <!--SR:!2024-05-01,69,310-->

## iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {{loop variables, iterable, and a statement block}}: <!--SR:!2024-04-28,66,310-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {{ranges, strings, lists, and many more not mentioned here}}. The semantics of `for...in` is that {{for each element in the iterable, the loop variables are assigned that element and then the statement block is executed}}. <!--SR:!2024-04-23,62,310!2024-04-13,54,310-->

To emulate the traditional `for` loop, one uses {{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}}. `range(begin, end, step)` has shorter forms: {{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}}. <!--SR:!2024-04-22,62,310!2024-04-10,52,310!2024-04-29,68,310-->

In Python, `while` can also perform iteration. A `while` statement consists of {{a condition and a statement block}}: <!--SR:!2024-04-23,63,310-->

```Python
while condition:
  statement_block
```

The semantics of `while` is {{that the condition is executed first. If the condition is `true`, the statement block is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}}. <!--SR:!2024-04-27,65,310-->

You can of course put loops inside loops.
