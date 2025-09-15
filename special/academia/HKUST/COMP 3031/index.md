---
aliases:
  - COMP 3031
  - COMP 3031 index
  - COMP3031
  - COMP3031 index
  - HKUST COMP 3031
  - HKUST COMP 3031 index
  - HKUST COMP3031
  - HKUST COMP3031 index
  - Principles of Programming Languages
  - Principles of Programming Languages index
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031
  - function/index
  - language/in/English
---

# index

- HKUST COMP 3031
- name: Principles of Programming Languages

The content is in teaching order.

- grading
  - scheme
    - assignments ×3: 30%
    - midterm examination: 30%
    - final examination: 40%

## children

- [assignments](assignments/index.md)
- [questions](questions.md)

## week 1 lab

- datetime: 2025-09-01T15:00:00+08:00/2025-09-01T16:20:00+08:00, PT1H20M
- status: unscheduled

---

> __<big><big>No lab/tutorial today</big></big>__
>
> Dear all,
>
> Thanks for registering in the course!
>
> To clarify one thing, just in case: there is no tutorial today, as there has not been a lecture yet.
>
> Best,
>
> — \[redacted\]

## week 1 lecture

- datetime: 2025-09-02T12:00:00+08:00/2025-09-02T13:20:00+08:00, PT1H20M
- topic: logistics; introduction; elements of programming; termination; evaluation strategy; scoping
- COMP 3031
  - COMP 3031 / logistics
  - COMP 3031 / objectives ::@:: Scala, functional programming, programming language constructs, programming language paradigms <!--SR:!2025-10-03,15,290!2025-10-03,15,290-->
- [programming paradigm](../../../../general/programming%20paradigm.md) ::@:: It is a relatively high-level way to conceptualize and structure the implementation of a computer program. <!--SR:!2025-10-04,16,290!2025-10-02,14,290-->
  - programming paradigm / common ::@:: concurrent, dependently-typed, functional, imperative, logic, object-oriented, parallel, etc. <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
- [imperative programming](../../../../general/imperative%20programming.md) ::@:: It is a programming paradigm of software that uses statements that change a program's state. <!--SR:!2025-10-03,15,290!2025-10-03,15,290-->
  - imperative programming / important elements ::@:: control structures, mutation, etc. <!--SR:!2025-10-04,16,290!2025-10-03,15,290-->
  - imperative programming / physical correspondence ::@:: It has strong correspondence with physical entities. <p> control structure ↔ jump <br/> field ↔ memory cell <br/> variable ↔ register <br/> variable assignment ↔ store \(instruction\) <br/> variable dereferencing ↔ load \(instruction\) <br/> ... <!--SR:!2025-10-04,16,290!2025-10-02,14,290-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <!--SR:!2025-11-11,43,290!2025-10-03,15,290-->
  - von Neumann architecture / von Neumann bottleneck ::@:: The use of the same bus to fetch instructions and data leads to the von Neumann bottleneck, the limited throughput \(data transfer rate\) between the central processing unit \(CPU\) and memory compared to the amount of memory. This seriously limits the effective processing speed when the CPU is required to perform minimal processing on large amounts of data. The CPU is continually forced to wait for needed data to move to or from memory. <!--SR:!2025-10-03,15,290!2025-10-04,16,290-->
    - von Neumann architecture / von Neumann bottleneck / trend ::@:: Since CPU speed and memory size have increased much faster than the throughput between them, the bottleneck has become more of a problem, a problem whose severity increases with every new generation of CPU. <!--SR:!2025-10-03,15,290!2025-10-02,14,290-->
- [theory](../../../../general/theory%20(mathematical%20logic).md) ::@:: It is a set of sentences in a formal language. <!--SR:!2025-10-04,16,290!2025-10-04,16,290-->
  - theory / for programming ::@:: data type\(s\), operation\(s\) on data type\(s\), law\(s\) on data and operations <br/> usually no mutations \(but possible with some difficulty\) <!--SR:!2025-10-04,16,290!2025-10-04,16,290-->
  - theory / mutation ::@:: A theory without mutation is usually much less complex than one with mutation. Mutation makes theories hard to understand. So most theories do not admit mutation. <p> For programming, this leads to _functional programming_. <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
- [functional programming](../../../../general/functional%20programming.md) ::@:: It is a programming paradigm where programs are constructed by applying and composing functions. <!--SR:!2025-10-02,14,290!2025-10-03,15,290-->
  - functional programming / missing elements ::@:: imperative control structures, no mutations \(__this course__: In a _restricted sense_, these elements are strictly _forbidden_.\) <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
  - functional programming / important elements ::@:: functions \(as first-class citizens\), immutable data types \(__this course__: In a _wide sense_, these elements are _emphasized_ on, but unmentioned elements \(e.g. above\) are not strictly forbidden.\) <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
  - functional programming / function ::@:: As first-class citizens, they can be composed, definable anywhere, passed as parameters, etc. <!--SR:!2025-10-02,14,290!2025-10-02,14,290-->
  - functional programming / examples ::@:: restricted: FP, Pure Lisp, XPath, XQuery, XSLT, etc. <br/> wider: Clojure, F\#, Haskell, Lips, Ocaml, Racket, SML, Scala, Scheme, etc. <!--SR:!2025-10-04,16,290!2025-10-03,15,290-->
- COMP 3031
  - COMP 3031 / recommended books
- [Scala](../../../../general/Scala%20(programming%20language).md) ::@:: It is a strongly statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. <p> \(__this course__: Use Scala 3.\) <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
  - Scala / Scala 3: [Scala 3](Scala%203.md)
- [programming language](../../../../general/programming%20language.md) ::@:: It is an artificial language for expressing computer programs. <!--SR:!2025-10-02,14,290!2025-10-04,16,290-->
  - programming language / elements ::@:: primitive expressions, composition of expressions, abstraction of expressions \(giving names to expressions\) <!--SR:!2025-10-03,15,290!2025-10-03,15,290-->
- [read–eval–print loop](../../../../general/read–eval–print%20loop.md) \(REPL\) ::@:: It is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise. <!--SR:!2025-10-03,15,290!2025-10-03,15,290-->
- Scala
  - Scala / Scala 3
    - [§ primitive types](Scala%203.md#primitive%20types): `Boolean`, `Int`, `Double`
    - [§ expressions](Scala%203.md#expressions): expressions, arithmetic expressions
    - [§ definitions](Scala%203.md#definitions): `def`
- [rewriting](../../../../general/rewriting.md) ::@:: It covers a wide range of methods of replacing subterms of a formula with other terms. <!--SR:!2025-10-02,14,290!2025-10-02,14,290-->
  - rewriting / substitution model ::@:: It is a way to _evaluate_ expressions _without side effects_. To evaluate a _function call_, each parameter to the function is evaluated from left to right. Then, replace the function call with the _function expression_, while _substituting_ each occurrence of the parameter name with the parameter value. <p> It is formalized in lambda calculus. <!--SR:!2025-10-03,15,290!2025-10-02,14,290-->
- [divergence](../../../../general/divergence%20(computer%20science).md) ::@:: A computation is said to __diverge__ if it does not terminate or terminates in an exceptional state. Otherwise it is said to __converge__. <!--SR:!2025-10-02,14,290!2025-10-02,14,290-->
  - divergence / example ::@:: Scala 3: `def loop: Int = loop; loop` <!--SR:!2025-10-04,16,290!2025-10-04,16,290-->
- [evaluation strategy](../../../../general/evaluation%20strategy.md) ::@:: It is a set of rules for evaluating expressions. <!--SR:!2025-10-02,14,290!2025-10-03,15,290-->
  - evaluation strategy / Scala 3 ::@:: 2 major evaluation strategies: call by name \(e.g., `def`, `=> <type>`\), call by value \(e.g., `val`\) <!--SR:!2025-10-04,16,290!2025-10-04,16,290-->
  - evaluation strategy / call by value \(CBV\) ::@:: Each parameter to the function is evaluated first. Then, to evaluate a function, each occurrence of each parameter is replaced by its corresponding value. <p> The advantage is if a parameter is used multiple times, only one evaluation is needed. The disadvantage is if a parameter is unused, one evaluation is still needed. <!--SR:!2025-10-03,15,290!2025-10-03,15,290-->
    - evaluation strategy / call by value / termination ::@:: If an expression terminates using CBV, then it also terminates using CBN. This is because every expression evaluated by CBN is also evaluated by CBV. <!--SR:!2025-10-03,15,290!2025-10-04,16,290-->
  - evaluation strategy / call by name \(CBN\) ::@:: Each parameter to the function is not evaluated. Rather, to evaluate a function, each occurrence of each parameter is replaced by its corresponding expression directly. <p> The advantage is if a parameter is used, no evaluation occurs. The disadvantage is each occurrence of a parameter evaluates the expression once. <!--SR:!2025-10-02,14,290!2025-10-03,15,290-->
    - evaluation strategy / call by name / termination ::@:: If an expression terminates using CBN, it _may not_ terminate using CBV. This is because there may be some expressions evaluated by CBV are not evaluated by CBN. <p> Scala 3: `def id(x: Int) = x; id(loop)` <!--SR:!2025-10-25,27,270!2025-10-03,15,290-->
- Scala
  - Scala / Scala 3
    - [§ evaluation](Scala%203.md#evaluation): call by value, call by name
    - [§ expressions](Scala%203.md#expressions): conditionals, logical expressions, comparisons
    - [§ definitions](Scala%203.md#definitions): `val`, recursion
- COMP 3031
  - COMP 3031 / exercises: `and(x: Boolean, y: Boolean): Boolean`, `or(x: Boolean, y: Boolean): Boolean`, `sqrt(x: Double): Double` using Newton's method
- Scala
  - Scala / Scala 3
    - [§ scoping](Scala%203.md#scoping): scope creation, lexical scoping, shadowing
- [scope](../../../../general/scope%20(computer%20science).md) ::@:: It of a name binding \(an association of a name to an entity, such as a variable\) is the part of a program where the name binding is valid; that is, where the name can be used to refer to the entity. <!--SR:!2025-10-02,14,290!2025-10-03,15,290-->
  - scope / motivation ::@:: It helps to avoid _namespace pollution_. <!--SR:!2025-10-02,14,290!2025-10-02,14,290-->
  - scope / lexical scoping ::@:: With it, a name always refers to its lexical context. This is a property of the program text and is made independent of the runtime call stack by the language implementation. <!--SR:!2025-10-04,16,290!2025-10-03,15,290-->
- Scala
  - Scala / Scala 3
    - [§ scoping](Scala%203.md#scoping): end markers
    - [§ expressions](Scala%203.md#expressions): semicolons

## week 1 lecture 2

- datetime: 2025-09-04T12:00:00+08:00/2025-09-04T13:20:00+08:00, PT1H20M
- topic:

## aftermath

### total

- grades: ?/100
  - statistics: ?
