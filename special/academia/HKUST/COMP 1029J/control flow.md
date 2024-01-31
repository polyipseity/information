---
aliases:
  - Java control flow
  - Java control flows
tags:
  - flashcards/special/academic/HKUST/COMP_1029J/control_flow
  - languages/in/English
---

# Java control flow

## branching

An `if` statement consists of {{a condition and a statement}}:

```Java
if (condition)
  statement
```

The semantics of `if` is obvious: {{If the condition is `true`, then the following statement is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}}

An `if...else` statement consists of {{a condition and two statements}}:

```Java
if (condition)
  statement
else
  statement
```

The semantics of `if...else` is also obvious: {{If the condition is `true`, then the first statement is executed. Otherwise, the second statement is executed. Note that the condition itself is always executed.}}

One can chain `if...else` by {{using another `if...else` statement as the `else` statement}}:

```Java
if (condition1) {
  // ...
} else
  if (condition2) {
    // ...
  } else {
    // ...
  }
// The above is commonly written as:
if (condition1) {
  // ...
} else if (condition2) {
  // ...
} else {
  // ...
}
```

The semantics of chaining `if...else` can be found by consider the semantics of `if...else`: {{The statement after the first `true` condition is executed. If there are no `true` conditions, the statement after `else` is executed if there is an `else`. Otherwise, nothing is executed. Note that the conditions up until the first `true` condition (inclusive) are themselves always executed in the order of appearance. If there are no `true` conditions, all conditions are always executed in the order of appearance.}}

Alternatively, a `switch` statement can be used if {{the conditions are checking if a value equal to constant values}}:

```Java
switch (string) {
  case "abc":
    // ...
    break;
  case "def":
    // ...
    break;
  default:
    // ...
}
// This is equivalent to:
if ("abc".equals(string)) {
  // ...
} else if ("def".equals(string)) {
  // ...
} else {
  // ...
}
```

Note that there is subtly with the `switch` statement. First, {{only constant values but not variables can be used after `switch`}}. Second, {{a `break` is needed to get the desirable behavior before the next `case` or `default`. It is possible to not have `break` but the semantics are more advanced than the `if...else` statement}}.

## iteration

A `for` statement consists of {{an initial statement, a condition, a loop statement, and a statement to execute}}:

```Java
for (initial_statement; condition; loop_statement)
  statement
```

The semantics of `for` is a bit complicated. First, {{the initial statement is executed. Then the condition is checked. If the condition is `true`, the statement following `for` is executed. Otherwise, the `for` statement finishes}}. Each time the statement following `for` has finished execution, {{the loop statement is executed. Then we go back to checking the condition and repeat}}.

One can use a `for` statement to iterate through {{an interval}}. More advanced stuff are possible but they are not mentioned here:

```Java
for (int ii = 1; ii < 11; ++ii) {
  System.out.print("From 1 to 10 (both ends inclusive): ");
  System.out.println(ii);
}
```

A `while` statement consists of {{a condition and a statement}}:

```Java
while (condition)
  statement
```

The semantics of `while` is {{that the condition is executed first. If the condition is `true`, the statement is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}}.

One can also first run the statement instead of the condition by using a `do...while` statement, which consists of {{a statement and a condition}}:

```Java
do
  statement
while (condition);
```

The semantics of `do...while` is {{that the statement is executed first. Then the condition is executed. If the condition is `true`, we repeat the above process again. If the condition is `false`, the `do...while` statement ends its execution}}.
