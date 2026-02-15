---
aliases:
  - VBA control flow
  - VBA control flows
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/control_flow
  - language/in/English
---

# VBA control flow

## branching

An `If...Then...End If` statement consists of {@{a condition and a statement block}@}: <!--SR:!2028-02-02,1137,350-->

```VB
If condition Then
  statement_block
End If
```

The semantics of `If...Then...End If` is obvious: {@{If the condition is `True`, then the statement block is executed. Otherwise, it is not executed. Note that the condition itself is always executed.}@} <!--SR:!2028-02-19,1146,350-->

An `If...Then...Else...End If` statement consists of {@{a condition and two statement blocks}@}: <!--SR:!2028-11-30,1371,350-->

```VB
If condition Then
  statement_block
Else
  statement_block
End If
```

{@{The semantics of `If...Then...Else...End If`}@} is also obvious: If {@{the condition is `True`, then the first statement block is executed}@}. Otherwise, {@{the second statement block is executed}@}. Note that {@{the condition itself is always executed}@}. <!--SR:!2027-12-22,1081,341!2026-03-01,20,361!2026-03-01,20,361!2026-02-28,19,361-->

In VBA, one usually does not {@{chain `If...Then...Else...End If`}@}. Instead, VBA provides {@{the keyword `ElseIf...Then`}@} so that {@{`If...Then...ElseIf...Then...Else...End If` represents the chained `if...else if...else` in most programming languages}@}: <!--SR:!2031-08-25,2032,321!2026-03-01,20,361!2026-03-01,20,361-->

```VB
If condition1 Then
  ...
ElseIf condition2 Then
  ...
Else
  ...
End If
```

The semantics of `If...Then...ElseIf...Then...Else...End If` can be found by consider the semantics of chaining `If...Then...Else...End If`: {@{The statement block after the first `True` condition is executed. If there are no `True` conditions, the statement block after `Else` is executed if there is an `Else`. Otherwise, nothing is executed}@}. Note that {@{the conditions up until the first `True` condition (inclusive) are themselves always executed in the appearance order, ignoring statement blocks along the way. If there are no `True` conditions, all conditions are always executed in the appearance order, followed by the `Else` statement block if there is one}@}. <!--SR:!2026-03-30,538,310!2026-11-23,766,329-->

## iteration

In VBA, there are (unnecessarily) many ways to do iteration.

You can of course put nested iterations inside iterations.

### `While`

`While...Wend` can also perform iteration. A `While...Wend` statement consists of {@{a condition and a statement block}@}: <!--SR:!2027-07-23,952,330-->

```VB
While
  statement_block
Wend
```

The semantics of `While...Wend` is {@{that the condition is executed first. If the condition is `True`, the statement block is executed and then we repeat the above process again. If the condition is `False`, the `While...Wend` statement ends its execution}@}. <!--SR:!2028-01-03,1111,350-->

### `Do`

Another way is using `Do While...Loop`. A `Do While...Loop` statement consists of {@{a condition and a statement block}@}: <!--SR:!2027-10-19,1055,350-->

```VB
Do While condition
  statement_block
Loop
```

The semantics of `Do While...Loop` is {@{that the condition is executed first. If the condition is `True`, the statement is executed and then we repeat the above process again. If the condition is `False`, the `Do While...Loop` statement ends its execution}@}. You can see it is exactly {@{the same as that for [`While...Wend`](#`While`)}@}. The only difference is that you cannot {@{prematurely end a loop in `While...Wend`, while you can do so for `Do While...Loop`}@}. <!--SR:!2027-03-11,790,321!2027-10-08,1020,341!2027-04-20,800,301-->

One can also first run the statement block instead of the condition by using a `Do...Loop While` statement, which consists of {@{a statement block and a condition}@}: <!--SR:!2026-06-30,650,321-->

```VB
Do
  statement_block
Loop While condition
```

The semantics of `Do...Loop While` is {@{that the statement block is executed first. Then the condition is executed. If the condition is `True`, we repeat the above process again. If the condition is `False`, the `Do...Loop While` statement ends its execution}@}. <!--SR:!2026-04-11,548,310-->

As VBA is intended to be English like, it also provides the unconventional {@{`Do Until...Loop` and `Do...Loop Until` constructs}@}. The semantics is exactly the same except that {@{the loop stops if the condition is `True`}@}. <!--SR:!2027-03-15,793,321!2027-01-31,773,321-->

### `For`

VBA also has for-loops. A `For...To...Step...Next` statement consists of {@{a loop variable, a starting point, a stopping point, a step (optional, by default 1), and a statement block to execute}@}: <!--SR:!2031-05-09,1945,321-->

```VB
For LoopVariable = start To end Step step ' `Step step` optional
  statement_block
Next LoopVariable
```

{@{The semantics of `For...To...Step...Next`}@} is {@{a bit complicated}@}. First, {@{the loop variable}@} is assigned {@{the starting point}@}. Then {@{the loop variable is checked}@}. If the loop variable is {@{in between start and end, both ends inclusive}@}, {@{the statement block is executed}@}. Otherwise, {@{the `For...To...Step...Next` statement finishes}@}. Each time {@{the statement block has finished execution}@}, the loop {@{variable is incremented by `step`}@}. Then we go {@{back to checking the loop variable and repeat}@}. <!--SR:!2031-07-03,1995,321!2027-10-28,1036,341!2026-05-18,89,369!2026-05-21,91,369!2026-05-17,88,369!2026-05-16,87,369!2026-05-20,90,369!2026-05-18,89,369!2026-05-21,91,369!2026-05-24,94,369!2026-05-22,92,369-->

### ending iteration early

One can end a loop prematurely. This is done by {@{`Exit Do` for `Do`-loops and `Exit For` for `For`-loops}@}. As mentioned before, {@{`While`-loops cannot be ended prematurely}@}. <!--SR:!2029-02-05,1173,310!2027-09-07,1008,341-->
