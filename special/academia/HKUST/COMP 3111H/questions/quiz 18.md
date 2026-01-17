---
aliases:
  - COMP 3111H quiz 18
  - COMP3111H quiz 18
  - HKUST COMP 3111H quiz 18
  - HKUST COMP3111H quiz 18
tags:
  - date/2025/11/18
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions/quiz_18
  - language/in/English
---

# quiz 18

- HKUST COMP 3111H

---

- type: quiz
- due: 2025-11-18T23:59:59+08:00
- points: 5
- questions: 5
- available: 2025-11-11T23:59:00+08:00/2025-11-18T23:59:59+08:00, P7DT59S
- time limit: none
- allowed attempts: 2

## hints

1. [software design patterns](../software%20design%20patterns.md) / bridge pattern ::@:: The _bridge_ is a _structural_ design pattern that separates an abstraction from its implementation so that the two can vary independently. It solves the tight coupling that arises when a class hierarchy of abstractions is directly tied to a parallel hierarchy of concrete implementations. <!--SR:!2026-01-25,14,290!2026-01-25,14,290-->
2. [software design patterns](../software%20design%20patterns.md) / mediator pattern ::@::  The _Mediator_ pattern is a _behavioral_ design pattern that centralizes communication between many objects, reducing tight coupling. In Bob's House of the Future each appliance (alarm, coffee pot, sprinkler, calendar) runs its own logic but talks only to a central Mediator instead of directly to one another. <!--SR:!2026-01-25,14,290!2026-01-25,14,290-->
3. [software design patterns](../software%20design%20patterns.md) / strategy pattern ::@::  The _strategy pattern_ is a _behavioral_ design pattern that allows an object to vary its behavior at runtime by encapsulating different algorithms or behaviors within separate objects. Instead of hardcoding behavior into a class, the behavior is delegated to a set of interchangeable, reusable components—each implementing a common interface. <!--SR:!2026-01-25,14,290!2026-01-25,14,290-->
4. systems design / implementation environment ::@:: To manage technical differences in the deployment platform, use a design strategy that _encapsulates_ and _isolates_ the implementation environment. This is achieved by using the _bridge design pattern_. <!--SR:!2026-01-25,14,290!2026-01-25,14,290-->
5. [software design patterns](../software%20design%20patterns.md) / singleton pattern ::@::  A _singleton_ is a _creational_ design pattern that guarantees a class has _exactly one_ instance and provides a global point of access to it. Typical use cases include thread pools, caches, dialog boxes, logging facilities, system-wide configuration managers (e.g., `System.out`), or any object whose multiple instances would be redundant or harmful. <!--SR:!2026-01-25,14,290!2026-01-25,14,290-->
