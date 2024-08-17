---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/control_flow
  - language/in/English
---

# Python control flow

## branching

An `if` statement consists of {{a condition and a statement block}}: <!--SR:!2024-10-30,205,330-->

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}} <!--SR:!2024-10-03,171,310-->

An `if...else` statement consists of {{a condition and two statement blocks}}: <!--SR:!2024-09-24,166,310-->

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}} <!--SR:!2024-09-26,168,310-->

In Python, one usually does not chain `if...else`. Instead, Python provides {{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}}: <!--SR:!2025-01-22,275,330-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}}. Note that {{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, alternated with statement block execution. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one.}} <!--SR:!2024-11-07,197,310!2025-01-14,250,323-->

Python has {{no `switch` statements before Python 3.10. Since Python 3.10, Python has `match...case` statement, but it will not be described here}}. <!--SR:!2024-11-26,209,310-->

## iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {{loop variables, iterable, and a statement block}}: <!--SR:!2025-01-24,271,330-->

```Python
for loop_variables in iterable:
  statement_block
```

Iterables can be {{ranges, strings, lists, and many more not mentioned here}}. The semantics of `for...in` is that {{for each element in the iterable, the loop variables are assigned that element and then the statement block is executed}}. <!--SR:!2025-01-03,255,330!2024-09-24,162,310-->

To emulate the traditional `for` loop, one uses {{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}}. `range(begin, end, step)` has shorter forms: {{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}}. <!--SR:!2025-01-25,278,330!2024-09-16,159,310!2025-02-18,295,330-->

In Python, `while` can also perform iteration. A `while` statement consists of {{a condition and a statement block}}: <!--SR:!2025-01-19,271,330-->

```Python
while condition:
  statement_block
```

The semantics of `while` is {{that the condition is executed first. If the condition is `true`, the statement block is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}}. <!--SR:!2025-01-26,274,330-->

You can of course put loops inside loops.
