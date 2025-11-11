---
aliases:
  - COMP 3111H quiz 16
  - COMP3111H quiz 16
  - HKUST COMP 3111H quiz 16
  - HKUST COMP3111H quiz 16
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions/quiz_16
  - language/in/English
---

# quiz 16

- HKUST COMP 3111H

---

- type: quiz
- due: 2025-11-11T23:59:59+08:00
- points: 5
- questions: 5
- available: 2025-11-04T23:59:00+08:00/2025-11-11T23:59:59+08:00, P7DT59S
- time limit: none
- allowed attempts: 2

## hints

1. [UML § state machine diagrams](UML.md#state%20machine%20diagrams) ::@:: A _state machine diagram_ is a directed graph that models the lifetime behavior of a single _object_ \(loosely speaking, _class_\). It contains _every_ possible states and transitions. Nodes represent states and arcs \(arrows, directed edges\) denote transitions triggered by events. The diagram shows all possible messages an object can send or receive during its life cycle.
2. [UML § events](UML.md#events) / handling ::@:: Events in a state machine are handled _sequentially_: each event is examined one at a time and, if no transition matches it, the event is simply _ignored_.
3. [UML § events](UML.md#events) / definition ::@:: An _event_ is something that happens at an _instantaneous_ point in time. It can be classified as: \(annotation: 4 items: call, change, signal, time\)
4. [UML § events](UML.md#events) / automaticity ::@:: A state can be exited either automatically or non‑automatically. _Automatic_ transitions fire immediately once the state's internal activity (if any) finishes, occurring when there are transitions without any _adornments_ \(labels\); _non‑automatic_ transitions are driven by an explicit event that occurs while the object remains in that state.
5. systems design / implementation environment ::@:: To manage technical differences in the deployment platform, use a design strategy that _encapsulates_ and _isolates_ the implementation environment. This is achieved by using the _bridge design pattern_. <p> Concrete occurrences of environmental components are modeled by "bridge" classes—for example, a `FileManager` "bridge" class handling file access across Windows, Unix, and Mac systems. By defining these intermediary classes, developers can add many specific implementations without cluttering the core application logic, thereby simplifying maintenance and keeping the system adaptable to new platforms.
