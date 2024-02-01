---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcards/special/academia/HKUST/COMP_1029P/control_flow
  - languages/in/English
---

# Python control flow

## branching

An `if` statement consists of {{a condition and a statement}}: <!--SR:!2024-02-04,4,270-->

```Python
if condition:
  statement
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}} <!--SR:!2024-02-04,4,270-->

An `if...else` statement consists of {{a condition and two statements}}: <!--SR:!2024-02-04,4,270-->

```Python
if condition:
  statement
else:
  statement
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement is executed. Otherwise, the second statement is executed. Note that the condition itself is always executed.}} <!--SR:!2024-02-04,4,270-->

In Python, one usually does not chain `if...else`. Instead, Python provides {{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}}: <!--SR:!2024-02-04,4,270-->

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement after `else` is executed if there is an `else`. Otherwise, nothing is executed}}. Note that {{the conditions up until the first `true` condition (inclusive) are themselves always executed in the order of appearance. If there are no `true` conditions, all conditions are always executed in the order of appearance.}} <!--SR:!2024-02-04,4,270-->

Python has no {{`switch` statements}}. <!--SR:!2024-02-04,4,270-->

## iteration

In Python, iteration is done through using `for...in`. A `for...in` statement consists of {{loop variables, iterable, and statements}}: <!--SR:!2024-02-04,4,270-->

```Python
for loop_variables in iterable:
  statements
```

Iterables can be {{ranges, strings, lists, and many more not mentioned here}}. The semantics of `for...in` is that {{for each element in the iterable, the loop variables are assigned that element and then the statements are executed}}. <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

To emulate the traditional `for` loop, one uses {{`range` and specifies the starting point (inclusive), ending point (exclusive), and step}}. A `for` loop with code in the form of `for (int idx = begin; idx < end; idx += step)` translates to {{`for idx in range(begin, end, step):` (if `step` is negative, then `idx < end` becomes `idx > end`)}}. `range(begin, end, step)` has shorter forms: {{`range(begin, end)` is equivalent to `range(begin, end, 1)` and `range(end)` is equivalent to `range(0, end, 1)`}}. <!--SR:!2024-02-04,4,270!2024-02-04,4,270!2024-02-04,4,270-->

In Python, `while` can also perform iteration. A `while` statement consists of {{a condition and a statement}}: <!--SR:!2024-02-04,4,270-->

```Python
while condition:
  statement
```

The semantics of `while` is {{that the condition is executed first. If the condition is `true`, the statement is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}}. <!--SR:!2024-02-04,4,270-->

You can of course put loops inside loops.
