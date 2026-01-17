---
aliases:
  - Python error
  - Python errors
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/error
  - language/in/English
---

# Python error

## types

There are two types of errors: {@{syntax errors and runtime errors}@}. The former {@{occurs during compilation and is detected by the compiler}@}, while the latter {@{occurs during execution}@}. <!--SR:!2026-10-06,268,330!2026-10-15,277,330!2027-01-25,375,364-->

## runtime errors

Runtime errors occur when {@{something error or unexpected}@} happens. The program {@{generally crashes}@} when an error occurs. There are {@{many types of errors, such as `IndexError`, `ValueError`, `ZeroDivisionError`, etc.}@} <!--SR:!2026-09-27,259,330!2026-10-01,263,330!2026-10-10,272,330-->

## catching errors

Sometimes, we can {@{handle some errors using `try...except...else`}@}. It consists of {@{a statement block, and one or more error types \(optional\), error names \(optional\)}@}, {@{error handler statement blocks, and a no-error statement block \(optional\)}@}: <!--SR:!2026-10-05,267,330!2026-10-08,270,330!2026-10-07,269,337-->

```Python
try:
  statement_block
except ErrorTypes as errorNames: # `ErrorTypes` optional, `as errorNames` optional
  statement_block
else: # optional
  statement_block # optional
```

Multiple {@{`except`s are allowed}@}. Additionally, to use {@{the same error handler statement block to handle multiple error types}@}, one can use {@{`,` to concatenate multiple error types and enclose them in parentheses `()` in `except`}@}, like {@{`except (errorType1, errorType2, errorType3) as exc:`}@}. <!--SR:!2026-11-01,294,330!2026-08-10,235,330!2026-10-29,291,337!2026-11-15,308,337-->

The semantics of the `try...except...else` statement is that {@{the statement block directly after the `try` are executed}@}. If {@{there are no errors}@}, {@{the `else` statement block if any are executed}@} and {@{the `try...except...else` statement finishes}@}. When {@{an error is thrown in `try` statement block}@}, {@{the execution of `try` statement block stops}@}. {@{The error types in `except`}@} are {@{checked in appearance order}@}. {@{The first `except`}@} with an error type that is {@{the same class as or a base class of the thrown error type}@} is selected. {@{The statement block directly after the selected `except`}@} is {@{executed and the `try...except...else` statement finishes}@}. If {@{no `except` clauses match}@}, {@{the error continues to propagate upwards}@}. If {@{the error reaches further upward from the entry point}@}, the program {@{usually crashes}@}. <!--SR:!2026-04-27,151,310!2026-04-22,147,310!2026-04-25,150,310!2026-10-01,263,337!2026-11-06,299,337!2026-10-07,269,337!2026-11-05,298,337!2026-10-23,285,337!2026-10-02,264,337!2026-10-30,292,337!2026-10-06,268,337!2026-11-14,307,337!2026-11-16,309,337!2026-10-01,263,337!2026-10-02,264,337!2026-11-04,297,337-->

Examples where catching errors is useful include {@{parsing user inputs}@}. <!--SR:!2026-08-27,250,330-->
