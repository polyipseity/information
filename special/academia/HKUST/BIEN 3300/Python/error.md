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

There are two types of errors: {@{syntax errors and runtime errors}@}. The former {@{occurs during compilation and is detected by the compiler}@}, while the latter {@{occurs during execution}@}. <!--SR:!fsrs,2029-12-25T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-06T00:00:00.000Z!2026-10-15,277,330!2027-01-25,375,364-->

## runtime errors

Runtime errors occur when {@{something error or unexpected}@} happens. The program {@{generally crashes}@} when an error occurs. There are {@{many types of errors, such as `IndexError`, `ValueError`, `ZeroDivisionError`, etc.}@} <!--SR:!fsrs,2029-11-13T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-09-28T00:00:00.000Z!fsrs,2029-12-04T00:00:00.000Z,1159,1159.34014939,1,2,9,0,0,2026-10-02T00:00:00.000Z!2026-10-10,272,330-->

## catching errors

Sometimes, we can {@{handle some errors using `try...except...else`}@}. It consists of {@{a statement block, and one or more error types \(optional\), error names \(optional\)}@}, {@{error handler statement blocks, and a no-error statement block \(optional\)}@}: <!--SR:!fsrs,2029-12-20T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-05T00:00:00.000Z!2026-10-08,270,330!fsrs,2030-01-27T00:00:00.000Z,1208,1207.96235895,1,2,9,0,0,2026-10-07T00:00:00.000Z-->

```Python
try:
  statement_block
except ErrorTypes as errorNames: # `ErrorTypes` optional, `as errorNames` optional
  statement_block
else: # optional
  statement_block # optional
```

Multiple {@{`except`s are allowed}@}. Additionally, to use {@{the same error handler statement block to handle multiple error types}@}, one can use {@{`,` to concatenate multiple error types and enclose them in parentheses `()` in `except`}@}, like {@{`except (errorType1, errorType2, errorType3) as exc:`}@}. <!--SR:!2026-11-01,294,330!fsrs,2029-06-25T00:00:00.000Z,1049,1049.13725568,1,2,9,0,0,2026-08-11T00:00:00.000Z!2026-10-29,291,337!2026-11-15,308,337-->

The semantics of the `try...except...else` statement is that {@{the statement block directly after the `try` are executed}@}. If {@{there are no errors}@}, {@{the `else` statement block if any are executed}@} and {@{the `try...except...else` statement finishes}@}. When {@{an error is thrown in `try` statement block}@}, {@{the execution of `try` statement block stops}@}. {@{The error types in `except`}@} are {@{checked in appearance order}@}. {@{The first `except`}@} with an error type that is {@{the same class as or a base class of the thrown error type}@} is selected. {@{The statement block directly after the selected `except`}@} is {@{executed and the `try...except...else` statement finishes}@}. If {@{no `except` clauses match}@}, {@{the error continues to propagate upwards}@}. If {@{the error reaches further upward from the entry point}@}, the program {@{usually crashes}@}. <!--SR:!2028-02-10,652,330!2028-01-20,631,330!2028-02-08,650,330!fsrs,2030-01-01T00:00:00.000Z,1187,1187.02124224,1,2,9,0,0,2026-10-02T00:00:00.000Z!2026-11-06,299,337!fsrs,2030-01-27T00:00:00.000Z,1208,1207.96235895,1,2,9,0,0,2026-10-07T00:00:00.000Z!2026-11-05,298,337!2026-10-23,285,337!fsrs,2030-01-02T00:00:00.000Z,1188,1188.44081901,1,2,9,0,0,2026-10-02T00:00:00.000Z!2026-10-30,292,337!fsrs,2030-01-22T00:00:00.000Z,1204,1204.06174443,1,2,9,0,0,2026-10-06T00:00:00.000Z!2026-11-14,307,337!2026-11-16,309,337!fsrs,2030-01-01T00:00:00.000Z,1187,1187.02124224,1,2,9,0,0,2026-10-02T00:00:00.000Z!fsrs,2030-01-02T00:00:00.000Z,1188,1188.44081901,1,2,9,0,0,2026-10-02T00:00:00.000Z!2026-11-04,297,337-->

Examples where catching errors is useful include {@{parsing user inputs}@}. <!--SR:!fsrs,2029-09-08T00:00:00.000Z,1107,1107.06552019,1,2,9,0,0,2026-08-28T00:00:00.000Z-->
