---
aliases:
  - VBA object
  - VBA objects
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029V/object
  - language/in/English
---

# VBA object

A VBA class ~~is never~~ could be complete without teaching objects... But we will talk about it anyways.

## class

To create an object, one needs to first create a class. In VBA, we need to {@{add a new module for each class under "Class Modules"}@}. A class consists of {@{attributes and methods}@}: <!--SR:!2027-06-08,922,330!2025-01-03,258,330-->

```VB
Public HaHa As String
Public HeHe As Double

Sub Initialize(ByVal NewHaHa As String, ByVal NewHeHe As Double)
  HaHa = NewHaHa
  HeHe = NewHeHe
End Sub

Sub NoHeHe()
  HeHe = 0
End Sub
```

Then to create an object, one uses {@{`New`. Also call the method that is intended to be the constructor if any, commonly called `Initialize`}@}: <!--SR:!2025-07-28,356,290-->

```VB
Dim HaHaObject As HaHaClass
Set HaHaObject = New HaHaObject
HaHaObject.Initialize "omg", 123 ' constructor is not part of the language natively
```

The above object stored under the `HaHaObject` variable is also called {@{an _instance_ of the class `HaHaClass`}@}. <!--SR:!2024-12-09,222,310-->

## attribute

An attribute is declared like a {@{[variable](basics.md#variable)}@}. <!--SR:!2027-05-07,921,350-->

## method

A method is declared like a {@{[subroutine or function](subroutine%20and%20function.md)}@}. <!--SR:!2025-01-30,278,330-->

### constructor

VBA {@{only supports constructors with no parameters by having a subroutine named `Class_Initialize`, but not parameterized constructors natively}@}. However, we can emulate the latter by {@{adding a subroutine that acts like a constructor and hopes the user remembers to call the constructor after creating the object}@}. A better method is using {@{the factory pattern, but it will not be introduced here}@}. Using the example above: <!--SR:!2026-06-15,646,330!2026-09-21,720,330!2024-12-31,236,320-->

```VB
Sub Initialize(ByVal NewHaHa As String, ByVal NewHeHe As Double)
  HaHa = NewHaHa
  HeHe = NewHeHe
End Sub
```
