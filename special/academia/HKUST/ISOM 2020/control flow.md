---
aliases:
  - Python control flow
  - Python control flows
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/control_flow
  - language/in/English
---

# Python control flow

Keep in mind a thing mostly unique to Python: {{Indentation matters in Python, so do not omit the indentations shown below.}}

## branching

An `if` statement consists of {{a condition and a statement block}}:

```Python
if condition:
  statement_block
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}}

An `if...else` statement consists of {{a condition and two statement blocks}}:

```Python
if condition:
  statement_block
else:
  statement_block
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}}

In Python, one usually does not chain `if...else`. Instead, Python provides {{the keyword `elif` so that `if...elif...else` represents the chained `if...else if...else` in most programming languages}}:

```Python
if condition1:
  ...
elif condition2:
  ...
else:
  ...
```

The semantics of `if...elif...else` can be found by consider the semantics of chaining `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}}. Note that {{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, alternated with statement block execution. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one.}}

If {{there are no statements to be executed in a branch}}, you {{must still put a properly indented `pass` statement, which does nothing, for that branch}}. This is also {{true for other control flow constructs introduced below}}. For example:

```Python
if condition:
  pass # required, otherwise error
```

Python has {{no `switch` statements before Python 3.10. Since Python 3.10, Python has `match...case` statement, but it will not be described here}}.
