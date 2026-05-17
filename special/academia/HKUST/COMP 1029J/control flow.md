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

{@{The semantics of chaining `if...else`}@} can be found by {@{considering the semantics of `if...else`}@}: {@{The statement block after the first `true` condition}@} is {@{executed}@}. If there are {@{no `true` conditions}@}, {@{the statement block after `else` is executed}@} if {@{there is an `else`}@}. Otherwise, {@{nothing is executed}@}. Note that {@{the conditions up until the first `true` condition \(inclusive\)}@} are themselves {@{always executed in the appearance order}@}, ignoring {@{statement blocks along the way}@}. If {@{there are no `true` conditions}@}, {@{all conditions}@} are always {@{executed in the appearance order}@}, followed by {@{the `else` statement block if there is one}@}. <!--SR:!2029-04-14,1318,310!2028-01-21,1103,341!2027-04-06,457,387!2027-03-10,444,387!2027-04-02,453,387!2027-04-08,459,387!2027-04-07,458,387!2027-04-02,453,387!2027-04-03,454,387!2027-03-09,443,387!2027-03-16,450,387!2027-04-04,455,387!2027-04-04,455,387!2027-04-03,454,387!2027-04-05,456,387-->

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

Note that there is subtly with the `switch` statement. First, {@{only constant values but not variables can be used after `case`}@}. Second, {@{a `break` is needed before the next `case` or `default` to get the desirable behavior. It is possible to not have `break` but the semantics are more advanced than the `if...else` statement}@}. <!--SR:!2032-06-26,2326,330!2027-03-14,815,330-->

## iteration

A `for` statement consists of {@{an initial statement, a condition, a loop statement, and a statement block to execute}@}: <!--SR:!2027-07-11,946,330-->

```Java
for (initial_statement; condition; loop_statement)
  statement
```

{@{The semantics of `for`}@} is {@{a bit complicated}@}. First, {@{the initial statement}@} is {@{executed}@}. Then {@{the condition is checked}@}. If {@{the condition is `true`}@}, {@{the statement block is executed}@}. Otherwise, {@{the `for` statement finishes}@}. Each time {@{the statement block has finished execution}@}, the loop {@{statement is executed}@}. Then we go {@{back to checking the condition and repeat}@}. <!--SR:!2027-08-24,979,330!2027-07-04,972,350!fsrs,2028-05-25T00:00:00.000Z,702,701.98388208,1,2,8,0,0,2026-06-23T00:00:00.000Z!fsrs,2028-07-19T00:00:00.000Z,745,744.52265934,1,2,8,0,0,2026-07-05T00:00:00.000Z!fsrs,2028-05-19T00:00:00.000Z,697,697.23354019,1,2,8,0,0,2026-06-22T00:00:00.000Z!fsrs,2028-06-25T00:00:00.000Z,726,725.66338141,1,2,8,0,0,2026-06-30T00:00:00.000Z!fsrs,2028-05-19T00:00:00.000Z,697,697.23354019,1,2,8,0,0,2026-06-22T00:00:00.000Z!fsrs,2028-06-25T00:00:00.000Z,726,725.66338141,1,2,8,0,0,2026-06-30T00:00:00.000Z!fsrs,2028-07-24T00:00:00.000Z,749,749.22610987,1,2,8,0,0,2026-07-06T00:00:00.000Z!fsrs,2028-07-13T00:00:00.000Z,740,739.81467051,1,2,8,0,0,2026-07-04T00:00:00.000Z!fsrs,2028-06-25T00:00:00.000Z,726,725.66338141,1,2,8,0,0,2026-06-30T00:00:00.000Z-->

One can use a `for` statement to iterate through {@{an interval}@}. More advanced stuff are possible but they are not mentioned here: <!--SR:!2026-10-14,736,330-->

```Java
for (int ii = 1; ii < 11; ++ii) {
  System.out.print("From 1 to 10 (both ends inclusive): ");
  System.out.println(ii);
}
```

A `while` statement consists of {@{a condition and a statement block}@}: <!--SR:!fsrs,2033-05-15T15:02:11.811Z,2528,2527.98347305,1,2,10,0,0,2026-06-13T15:02:11.811Z-->

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

The semantics of {@{`do...while`}@} is that {@{the statement block is executed}@} first. Then {@{the condition is executed}@}. If {@{the condition is `true`, we repeat the above process again}@}. If {@{the condition is `false`, the `do...while` statement ends its execution}@}. <!--SR:!2027-02-18,851,330!fsrs,2026-11-29T05:28:21.579Z,177,176.73131765,1,2,6,0,0,2026-06-05T05:28:21.579Z!fsrs,2026-11-29T05:28:20.718Z,177,176.73131765,1,2,6,0,0,2026-06-05T05:28:20.718Z!fsrs,2026-12-16T09:10:28.219Z,191,190.67066968,1,2,6,0,0,2026-06-08T09:10:28.219Z!fsrs,2026-12-16T09:10:26.881Z,191,190.67066968,1,2,6,0,0,2026-06-08T09:10:26.881Z-->
