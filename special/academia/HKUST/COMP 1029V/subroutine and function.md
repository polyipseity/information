---
aliases:
  - VBA function
  - VBA function and subroutine
  - VBA functions
  - VBA functions and subroutines
  - VBA subroutine
  - VBA subroutine and function
  - VBA subroutines
  - VBA subroutines and functions
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/subroutine_and_function
  - language/in/English
---

# subroutine and function

In VBA, both subroutine `Sub...End Sub` and function `Function...End Function` {@{group code together}@}, making them very similar things. The difference is that {@{subroutines always return nothing while functions always return something}@}.

## exiting

You can exit a subroutine or function by {@{`Exit Sub` and `Exit Function`}@}.

For functions, there is no `return` keyword. Instead, it is accomplished by doing two things: {@{setting the result by `FunctionName = Result` and then exiting the function}@}:

## parameters

You can specify parameters by {@{separating each parameter name by commas `,`}@}:

```VB
Function Multiply(Left, Right)
  Multiply = Left * Right
End Function
```

You can also specify the parameter types by {@{appending `As ParameterType` and prepending `ByVal` to the parameter name}@}. `ByVal` means {@{storing the inputted value to the parameter}@}. Note that {@{`ByRef` is also another option apart from `ByVal`, but it will not be mentioned here}@}.

```VB
Function Multiply(ByVal Left As Integer, ByVal Right As Integer)
  Multiply = Left * Right
End Function
```

## return type

For functions, you can specify the return type by {@{appending `As ReturnType` after the parameters}@}:

```VB
Function SquareSize(SideLength) As Integer
  SquareSize = SideLength * SideLength
End Function
```

## parentheses

See [basics § parentheses](basics.md#parentheses).
