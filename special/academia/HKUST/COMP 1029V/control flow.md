---
aliases:
  - VBA control flow
  - VBA control flows
tags:
  - flashcards/special/academic/HKUST/COMP_1029V/control_flow
  - languages/in/English
---

# VBA control flow

## branching

An `If...Then...End If` statement consists of {{a condition and statements}}: <!--SR:!2024-02-04,4,270-->

```VB
If condition Then
  statements
End If
```

The semantics of `If...Then...End If` is obvious: {{If the condition is `True`, then the following statements are executed. Otherwise, they are not executed. Note that the condition itself is always executed.}} <!--SR:!2024-02-04,4,270-->

An `If...Then...Else...End If` statement consists of {{a condition and two statement blocks}}: <!--SR:!2024-02-04,4,270-->

```VB
If condition Then
  statements
Else
  statements
End If
```

The semantics of `If...Then...Else...End If` is also obvious: {{If the condition is `True`, then the first statement block is executed. Otherwise, the second statement block is executed. Note that the condition itself is always executed.}} <!--SR:!2024-02-04,4,281-->

In VBA, one usually does not chain `If...Then...Else...End If`. Instead, VBA provides {{the keyword `ElseIf...Then` so that `If...Then...ElseIf...Then...Else...End If` represents the chained `if...else if...else` in most programming languages}}: <!--SR:!2024-02-04,4,281-->

```VB
If condition1 Then
  ...
ElseIf condition2 Then
  ...
Else
  ...
End If
```

The semantics of `If...Then...ElseIf...Then...Else...End If` can be found by consider the semantics of chaining `If...Then...Else...End If`: {{The statement block after the first `True` condition is executed. If there are no `True` conditions, the statement block after `Else` is executed if there is an `Else`. Otherwise, nothing is executed. Note that the conditions up until the first `True` condition (inclusive) are themselves always executed in the order of appearance. If there are no `True` conditions, all conditions are always executed in the order of appearance.}} <!--SR:!2024-02-04,4,270-->

## iteration

In VBA, there are (unnecessarily) many ways to do iteration.

You can of course put nested iterations inside iterations.

### `While`

`While...Wend` can also perform iteration. A `While...Wend` statement consists of {{a condition and a statement block}}: <!--SR:!2024-02-04,4,270-->

```VB
While
  statement
Wend
```

The semantics of `While...Wend` is {{that the condition is executed first. If the condition is `True`, the statement is executed and then we repeat the above process again. If the condition is `False`, the `While...Wend` statement ends its execution}}. <!--SR:!2024-02-04,4,270-->

### `Do`

Another way is using `Do While...Loop`. A `Do While...Loop` statement consists of {{a condition and a statement block}}: <!--SR:!2024-02-04,4,270-->

```VB
Do While condition
  statements
Loop
```

The semantics of `Do While...Loop` is {{that the condition is executed first. If the condition is `True`, the statement is executed and then we repeat the above process again. If the condition is `False`, the `Do While...Loop` statement ends its execution}}. You can see it is exactly {{the same as that for [`While...Wend`](#`While`)}}. The only difference is that you cannot {{prematurely end a loop in `While...Wend`, while you can do so for `Do While...Loop`}}. <!--SR:!2024-02-04,4,281!2024-02-04,4,281!2024-02-04,4,281-->

One can also first run the statement block instead of the condition by using a `Do...Loop While` statement, which consists of {{a statement block and a condition}}: <!--SR:!2024-02-04,4,281-->

```VB
Do
  statements
Loop While condition
```

The semantics of `Do...Loop While` is {{that the statement block is executed first. Then the condition is executed. If the condition is `True`, we repeat the above process again. If the condition is `False`, the `Do...Loop While` statement ends its execution}}. <!--SR:!2024-02-04,4,270-->

As VBA is intended to be English like, it also provides the unconventional {{`Do Until...Loop` and `Do...Loop Until` constructs}}. The semantics is exactly the same except that {{the loop stops if the condition is `True`}}. <!--SR:!2024-02-04,4,281!2024-02-04,4,281-->

### `For`

VBA also has for-loops. A `For...To...Step...Next` statement consists of {{a loop variable, a starting point, a stopping point, a step (optional, by default 1), and a statement block to execute}}: <!--SR:!2024-02-04,4,281-->

```VB
For LoopVariable = start To end Step step ' `Step step` optional
  statements
Next LoopVariable
```

The semantics of `For...To...Step...Next` is a bit complicated. First, {{the loop variable is assigned the starting point. Then the loop variable is checked. If the loop variable is in between start and end, both ends inclusive, the statement block is executed. Otherwise, the `For...To...Step...Next` statement finishes}}. Each time the statement block has finished execution, {{the loop variable is incremented by `step`. Then we go back to checking the loop variable and repeat}}. <!--SR:!2024-02-04,4,281!2024-02-04,4,281-->

### ending iteration early

One can end a loop prematurely. This is done by {{`Exit Do` for `Do`-loops and `Exit For` for `For`-loops}}. As mentioned before, {{`While`-loops cannot be ended prematurely}}. <!--SR:!2024-02-04,4,270!2024-02-04,4,281-->
