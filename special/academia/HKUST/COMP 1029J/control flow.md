---
aliases:
  - Java control flow
  - Java control flows
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/control_flow
  - language/in/English
---

# Java control flow

## branching

An `if` statement consists of {@{a condition and a statement block}@}: <!--SR:!2027-05-04,854,330-->

```Java
if (condition)
  statement_block
```

The semantics of `if` is obvious: {@{If the condition is `true`, then the statement block is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}@} <!--SR:!2026-07-23,677,330-->

An `if...else` statement consists of {@{a condition and two statement blocks}@}: <!--SR:!2028-09-12,1311,350-->

```Java
if (condition)
  statement_block
else
  statement_block
```

The semantics of `if...else` is also obvious: {@{If the condition is `true`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}@} <!--SR:!2027-04-27,888,330-->

One can chain `if...else` by {@{using another `if...else` statement as the `else` statement}@}: <!--SR:!2029-01-30,1420,350-->

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

The semantics of chaining `if...else` can be found by consider the semantics of `if...else`: {@{The statement block after the first `true` condition is executed. If there are no `true` conditions, the statement block after `else` is executed if there is an `else`. Otherwise, nothing is executed}@}. Note that {@{the conditions up until the first `true` condition (inclusive) are themselves always executed in the appearance order, ignoring statement blocks along the way. If there are no `true` conditions, all conditions are always executed in the appearance order, followed by the `else` statement block if there is one}@}. <!--SR:!2029-04-14,1318,310!2028-01-21,1103,341-->

Alternatively, a `switch` statement can be used if {@{the conditions are checking if a value equals some constant values}@}: <!--SR:!2026-08-24,698,330-->

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

Note that there is subtly with the `switch` statement. First, {@{only constant values but not variables can be used after `case`}@}. Second, {@{a `break` is needed before the next `case` or `default` to get the desirable behavior. It is possible to not have `break` but the semantics are more advanced than the `if...else` statement}@}. <!--SR:!2026-02-12,543,310!2027-03-14,815,330-->

## iteration

A `for` statement consists of {@{an initial statement, a condition, a loop statement, and a statement block to execute}@}: <!--SR:!2027-07-11,946,330-->

```Java
for (initial_statement; condition; loop_statement)
  statement
```

The semantics of `for` is a bit complicated. First, {@{the initial statement is executed. Then the condition is checked. If the condition is `true`, the statement block is executed. Otherwise, the `for` statement finishes}@}. Each time the statement block has finished execution, {@{the loop statement is executed. Then we go back to checking the condition and repeat}@}. <!--SR:!2027-08-24,979,330!2027-07-04,972,350-->

One can use a `for` statement to iterate through {@{an interval}@}. More advanced stuff are possible but they are not mentioned here: <!--SR:!2026-10-14,736,330-->

```Java
for (int ii = 1; ii < 11; ++ii) {
  System.out.print("From 1 to 10 (both ends inclusive): ");
  System.out.println(ii);
}
```

A `while` statement consists of {@{a condition and a statement block}@}: <!--SR:!2026-06-09,642,330-->

```Java
while (condition)
  statement_block
```

The semantics of `while` is {@{that the condition is executed first. If the condition is `true`, the statement block is executed and then we repeat the above process again. If the condition is `false`, the `while` statement ends its execution}@}. <!--SR:!2027-08-29,938,330-->

One can also first run the statement block instead of the condition by using a `do...while` statement, which consists of {@{a statement block and a condition}@}: <!--SR:!2026-12-22,796,330-->

```Java
do
  statement_block
while (condition);
```

The semantics of `do...while` is {@{that the statement block is executed first. Then the condition is executed. If the condition is `true`, we repeat the above process again. If the condition is `false`, the `do...while` statement ends its execution}@}. <!--SR:!2027-02-18,851,330-->
