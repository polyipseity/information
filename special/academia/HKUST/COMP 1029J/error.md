---
aliases:
  - Java error
  - Java errors
tags:
  - flashcards/special/academic/HKUST/COMP_1029J/error
  - languages/in/English
---

# Java error

## types

There are two types of errors: {{syntax errors and runtime errors}}. The former {{occurs during compilation and is detected by the compiler, while the latter occurs during execution}}.

## exceptions

Java calls runtime errors {{_exceptions_}}. They occur when {{something exceptional or unexpected}} happens. The program {{generally crashes}} when an exception occurs. There are {{many types of exceptions, such as `ArrayIndexOutOfBoundsException`, `ArithmeticException`, etc.}} The most general runtime error type is {{`Exception`}}.

## catching exceptions

Sometimes, we can {{handle some exceptions using `try...catch`}}. It consists of {{a statement, and one or more exception types, exception names, and exception handler statements}}:

```Java
try {
  statements;
} catch (ExceptionTypes exceptionNames) {
  statements;
}
```

Multiple {{`catch` are allowed}}. Additionally, to use the same exception handler statements to handle multiple exception types, one can {{use `|` to concatenate the multiple exception types in `catch`, like `catch (ExceptionType1 | ExceptionType2 | ExceptionType3 exc)`}}.

The semantics of the `try...catch` statement is that {{the statements directly after the `try` are executed. If there are no exceptions, the `try...catch` statement finishes}}. When an exception is thrown in `try` statements, {{the execution of `try` statements stops. The exception types in `catch` are checked in appearance order. The first `catch` with an exception type that is the same class as or a base class of the thrown exception type is selected. The statements directly after the selected `catch` are executed and the `try...catch` statement finishes}}. If no `catch` clauses match, {{the exception continues to propagate upwards. If the exception reaches upward from the main method, the program usually crashes}}.