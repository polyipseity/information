---
aliases:
  - Java error
  - Java errors
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/error
  - language/in/English
---

# Java error

## types

There are two types of errors: {@{syntax errors and runtime errors}@}. The former {@{occurs during compilation and is detected by the compiler, while the latter occurs during execution}@}. <!--SR:!2028-07-27,1276,350!2025-03-09,311,330-->

## exceptions

Java calls runtime errors {@{_exceptions_}@}. They occur when {@{something exceptional or unexpected}@} happens. The program {@{generally crashes}@} when an exception occurs. There are {@{many types of exceptions, such as `ArithmeticException`, `ArrayIndexOutOfBoundsException`, etc.}@} The most general runtime error type is {@{`Exception`}@}. <!--SR:!2028-02-13,1146,350!2028-12-02,1374,350!2027-08-24,1010,350!2026-06-08,596,310!2028-08-03,1280,350-->

## catching exceptions

Sometimes, we can {@{handle some exceptions using `try...catch`}@}. It consists of {@{a statement block, and one or more exception types, exception names, and exception handler statement blocks}@}: <!--SR:!2028-02-16,1147,350!2026-07-08,621,310-->

```Java
try {
  statements;
} catch (ExceptionTypes exceptionNames) {
  statements;
}
```

Multiple {@{`catch`es are allowed}@}. Additionally, to use the same exception handler statement block to handle multiple exception types, one can {@{use `|` to concatenate multiple exception types in `catch`, like `catch (ExceptionType1 | ExceptionType2 | ExceptionType3 exc)`}@}. <!--SR:!2028-04-13,1191,350!2026-02-16,511,310-->

The semantics of the `try...catch` statement is that {@{the statement block directly after the `try` are executed. If there are no exceptions, the `try...catch` statement finishes}@}. When an exception is thrown in `try` statements, {@{the execution of `try` statement block stops. The exception types in `catch` are checked in appearance order. The first `catch` with an exception type that is the same class as or a base class of the thrown exception type is selected. The statement block directly after the selected `catch` are executed and the `try...catch` statement finishes}@}. If no `catch` clauses match, {@{the exception continues to propagate upwards. If the exception reaches further upward from the main method, the program usually crashes}@}. <!--SR:!2025-03-09,310,330!2026-11-24,724,290!2028-06-22,1247,350-->
