---
aliases:
  - Python error
  - Python errors
tags:
  - flashcards/special/academic/HKUST/COMP_1029P/error
  - languages/in/English
---

# Python error

## types

There are two types of errors: {{syntax errors and runtime errors}}. The former {{occurs during compilation and is detected by the compiler, while the latter occurs during execution}}.

## runtime errors

Runtime errors occur when {{something erroral or unexpected}} happens. The program {{generally crashes}} when an error occurs. There are {{many types of errors, such as `IndexError`, `ValueError`, `ZeroDivisionError`, etc.}}

## catching errors

Sometimes, we can {{handle some errors using `try...except...else`}}. It consists of {{a statement, and one or more error types (optional), error names (optional), error handler statements, and no-error statements (optional)}}:

```Python
try:
  statements
except ErrorTypes as errorNames: # `ErrorTypes` optional, `as errorNames` optional
  statements
else: # optional
  statements # optional
```

Multiple {{`except`s are allowed}}. Additionally, to use the same error handler statements to handle multiple error types, one can {{use `,` to concatenate the multiple error types and enclose them in parentheses `()` in `except`, like `except (errorType1, errorType2, errorType3) as exc:`}}.

The semantics of the `try...except...else` statement is that {{the statements directly after the `try` are executed. If there are no errors, the `else` statements if any are executed and the `try...except...else` statement finishes}}. When an error is thrown in `try` statements, {{the execution of `try` statements stops. The error types in `except` are checked in appearance order. The first `except` with an error type that is the same class as or a base class of the thrown error type is selected. The statements directly after the selected `except` are executed and the `try...except...else` statement finishes}}. If no `except` clauses match, {{the error continues to propagate upwards. If the error reaches upward from the main method, the program usually crashes}}.

Examples where catching errors is useful include {{parsing user inputs}}.
