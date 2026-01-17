---
aliases:
  - COMP 3111H quiz 17
  - COMP3111H quiz 17
  - HKUST COMP 3111H quiz 17
  - HKUST COMP3111H quiz 17
tags:
  - date/2025/11/18
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions/quiz_17
  - language/in/English
---

# quiz 17

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

1. [UML](../UML.md) / cohesion ::@:: _Cohesion_ measures how many distinct responsibilities a _class_ bears; the most cohesive design is one that performs a single, well-defined function. <!--SR:!2026-01-29,16,290!2026-01-29,16,290-->
2. [software design patterns](../software%20design%20patterns.md) / observer pattern ::@:: The _Observer pattern_ is a _behavioral_ design pattern that defines a one-to-many dependency between objects so that when one object's state changes, all its dependent objects are automatically notified and updated. <!--SR:!2026-01-29,16,290!2026-01-29,16,290-->
3. [software design patterns](../software%20design%20patterns.md) / \(top\) ::@:: Design patterns are not finished implementations that can be directly translated into code. Instead, they serve as templates or blueprints—describing the structure, behavior, and interactions between classes or objects—without specifying the exact types or instances involved. <!--SR:!2026-01-29,16,290!2026-01-29,16,290-->
4. systems analysis / architectural patterns / model—view—controller \(MVC\) ::@:: It is a design pattern that separates the user interface from the underlying data and business logic. The _model_ holds the core data structures and state; the _view_ renders this data to the screen and presents controls for interaction; the _controller_ mediates between the two, handling user actions, updating the model, and refreshing the view. The _observer design pattern_ is typically used to update the view when the model changes. <p> This decoupling improves _maintainability_ and allows _independent_ evolution of presentation \(_user interface_\), data, and control logic. <!--SR:!2026-01-29,16,290!2026-01-29,16,290-->
5. [UML](../UML.md) / boundary classes ::@:: Boundary objects interact only with control objects and actors, at least _initially_, providing an encapsulation and isolation layer that isolate changes in the system interface. Actors interact only with boundary objects. They should _never_ interact with other boundary objects directly. These result in a well structured and maintainable system. <!--SR:!2026-01-29,16,290!2026-01-29,16,290-->
