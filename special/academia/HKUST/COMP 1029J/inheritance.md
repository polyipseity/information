---
aliases:
  - Java inheritance
  - Java inheritances
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/inheritance
  - language/in/English
---

# Java inheritance

Too advanced, so inheritance will be described in very simple terms.

## inheritance

The idea of inheritance is the have {{a base class containing common behaviors, and then derive classes that inherit behaviors from the base class and then add their own behaviors on top of it}}. In practice, this means {{methods and fields from the base class are usable in derived classes}}. <!--SR:!2024-07-13,114,290!2024-05-02,70,310-->

To inherit a class, one use {{the `extends` keyword, like `class Derived extends Base`}}. Only {{one class}} be be inherited. <!--SR:!2024-04-25,64,310!2024-05-03,71,310-->

### interfaces

Interfaces are {{like classes except that it cannot have fields}}. It is used to {{describe what a class can do without describing how the class does it}}. <!--SR:!2024-09-22,163,310!2024-04-18,58,310-->

To inherit interfaces, one use {{the `implements` keyword, which must come after `extends`, like `class Derived extends Base implements Interface1, Interface2`}}. {{Multiple interfaces}} can be inherited. <!--SR:!2024-04-14,55,310!2024-11-12,217,330-->
