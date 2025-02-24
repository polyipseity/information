---
aliases:
  - Java inheritance
  - Java inheritances
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/inheritance
  - language/in/English
---

# Java inheritance

Too advanced, so inheritance will be described in very simple terms.

## inheritance

The idea of inheritance is the have {@{a base class containing common behaviors, and then derive classes that inherit behaviors from the base class and then add their own behaviors on top of it}@}. In practice, this means {@{methods and fields from the base class are usable in derived classes and other places}@}. <!--SR:!2025-10-15,458,310!2025-03-12,314,330-->

To inherit a class, one use {@{the `extends` keyword, like `class Derived extends Base`}@}. Only {@{one class}@} can be inherited. <!--SR:!2027-06-17,881,330!2028-11-06,1351,350-->

### interfaces

Interfaces are {@{like classes except that it cannot have fields}@}. It is used to {@{describe what a class can do without describing how the class does it}@}. <!--SR:!2026-08-23,698,330!2028-01-24,1128,350-->

To inherit interfaces, one use {@{the `implements` keyword, which must come after `extends`, like `class Derived extends Base implements Interface1, Interface2`}@}. {@{Multiple interfaces}@} can be inherited. <!--SR:!2026-08-30,703,330!2027-07-27,987,350-->
