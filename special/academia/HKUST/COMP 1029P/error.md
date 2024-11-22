---
aliases:
  - Python error
  - Python errors
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/error
  - language/in/English
---

# Python error

## types

There are two types of errors: {@{syntax errors and runtime errors}@}. The former {@{occurs during compilation and is detected by the compiler, while the latter occurs during execution}@}. <!--SR:!2027-02-01,832,330!2024-11-26,225,330-->

## runtime errors

Runtime errors occur when {@{something error or unexpected}@} happens. The program {@{generally crashes}@} when an error occurs. There are {@{many types of errors, such as `IndexError`, `ValueError`, `ZeroDivisionError`, etc.}@} <!--SR:!2024-12-19,246,330!2025-01-29,275,330!2025-01-18,269,330-->

## catching errors

Sometimes, we can {@{handle some errors using `try...except...else`}@}. It consists of {@{a statement block, and one or more error types (optional), error names (optional), error handler statement blocks, and a no-error statement block (optional)}@}: <!--SR:!2026-12-22,796,330!2025-10-28,458,310-->

```Python
try:
  statement_block
except ErrorTypes as errorNames: # `ErrorTypes` optional, `as errorNames` optional
  statement_block
else: # optional
  statement_block # optional
```

Multiple {@{`except`s are allowed}@}. Additionally, to use the same error handler statement block to handle multiple error types, one can {@{use `,` to concatenate multiple error types and enclose them in parentheses `()` in `except`, like `except (errorType1, errorType2, errorType3) as exc:`}@}. <!--SR:!2025-01-22,269,330!2026-07-20,673,330-->

The semantics of the `try...except...else` statement is that {@{the statement block directly after the `try` are executed. If there are no errors, the `else` statement block if any are executed and the `try...except...else` statement finishes}@}. When an error is thrown in `try` statement block, {@{the execution of `try` statement block stops. The error types in `except` are checked in appearance order. The first `except` with an error type that is the same class as or a base class of the thrown error type is selected. The statement block directly after the selected `except` are executed and the `try...except...else` statement finishes}@}. If no `except` clauses match, {@{the error continues to propagate upwards. If the error reaches further upward from the entry point, the program usually crashes}@}. <!--SR:!2026-10-28,748,330!2025-04-27,298,290!2024-11-28,213,310-->

Examples where catching errors is useful include {@{parsing user inputs}@}. <!--SR:!2027-05-01,890,330-->
