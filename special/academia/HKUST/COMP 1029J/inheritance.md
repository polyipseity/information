---
aliases:
  - Java inheritance
  - Java inheritances
tags:
  - flashcards/special/academia/HKUST/COMP_1029J/inheritance
  - languages/in/English
---

# Java inheritance

Too advanced, so inheritance will be described in very simple terms.

## inheritance

The idea of inheritance is the have {{a base class containing common behaviors, and then derive classes that inherit behaviors from the base class and then add their own behaviors on top of it}}. In practice, this means {{methods and fields from the base class are usable in derived classes}}. <!--SR:!2024-02-03,3,250!2024-02-04,4,270-->

To inherit a class, one use {{the `extends` keyword, like `class Derived extends Base`}}. Only {{one class}} be be inherited. <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

### interfaces

Interfaces are {{like classes except that it cannot have fields}}. It is used to {{describe what a class can do without describing how the class does it}}. <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->

To inherit interfaces, one use {{the `implements` keyword, which must come after `extends`, like `class Derived extends Base implements Interface1, Interface2`}}. {{Multiple interfaces}} can be inherited. <!--SR:!2024-02-04,4,270!2024-02-04,4,270-->
