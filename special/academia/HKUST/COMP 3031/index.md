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
  - COMP 3031 / objectives ::@:: Scala, functional programming, programming language constructs, programming language paradigms
- [programming paradigm](../../../../general/programming%20paradigm.md) ::@:: It is a relatively high-level way to conceptualize and structure the implementation of a computer program.
  - programming paradigm / common ::@:: concurrent, dependently-typed, functional, imperative, logic, object-oriented, parallel, etc.
- [imperative programming](../../../../general/imperative%20programming.md) ::@:: It is a programming paradigm of software that uses statements that change a program's state.
  - imperative programming / important elements ::@:: control structures, mutation, etc.
  - imperative programming / physical correspondence ::@:: It has strong correspondence with physical entities. <p> control structure ↔ jump <br/> field ↔ memory cell <br/> variable ↔ register <br/> variable assignment ↔ store \(instruction\) <br/> variable dereferencing ↔ load \(instruction\) <br/> ...
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms
  - von Neumann architecture / von Neumann bottleneck ::@:: The use of the same bus to fetch instructions and data leads to the von Neumann bottleneck, the limited throughput \(data transfer rate\) between the central processing unit \(CPU\) and memory compared to the amount of memory. This seriously limits the effective processing speed when the CPU is required to perform minimal processing on large amounts of data. The CPU is continually forced to wait for needed data to move to or from memory.
    - von Neumann architecture / von Neumann bottleneck / trend ::@:: Since CPU speed and memory size have increased much faster than the throughput between them, the bottleneck has become more of a problem, a problem whose severity increases with every new generation of CPU.
- [theory](../../../../general/theory%20(mathematical%20logic).md) ::@:: It is a set of sentences in a formal language.
  - theory / for programming ::@:: data type\(s\), operation\(s\) on data type\(s\), law\(s\) on data and operations <br/> usually no mutations \(but possible with some difficulty\)
  - theory / mutation ::@:: A theory without mutation is usually much less complex than one with mutation. Mutation makes theories hard to understand. So most theories do not admit mutation. <p> For programming, this leads to _functional programming_.
- [functional programming](../../../../general/functional%20programming.md) ::@:: It is a programming paradigm where programs are constructed by applying and composing functions.
  - functional programming / missing elements ::@:: imperative control structures, no mutations \(__this course__: In a _restricted sense_, these elements are strictly _forbidden_.\)
  - functional programming / important elements ::@:: functions \(as first-class citizens\), immutable data types \(__this course__: In a _wide sense_, these elements are _emphasized_ on, but unmentioned elements \(e.g. above\) are not strictly forbidden.\)
  - functional programming / function ::@:: As first-class citizens, they can be composed, definable anywhere, passed as parameters, etc.
  - functional programming / examples ::@:: restricted: FP, Pure Lisp, XPath, XQuery, XSLT, etc. <br/> wider: Clojure, F\#, Haskell, Lips, Ocaml, Racket, SML, Scala, Scheme, etc.
- COMP 3031
  - COMP 3031 / recommended books
- [Scala](../../../../general/Scala%20(programming%20language).md) ::@:: It is a strongly statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. <p> \(__this course__: Use Scala 3.\)
  - Scala / Scala 3: [Scala 3](Scala%203.md)
- [programming language](../../../../general/programming%20language.md) ::@:: It is an artificial language for expressing computer programs.
  - programming language / elements ::@:: primitive expressions, composition of expressions, abstraction of expressions \(giving names to expressions\)
- [read–eval–print loop](../../../../general/read–eval–print%20loop.md) \(REPL\) ::@:: It is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise.
- Scala
  - Scala / Scala 3
    - [§ primitive types](Scala%203.md#primitive%20types): `Boolean`, `Int`, `Double`
    - [§ expressions](Scala%203.md#expressions): expressions, arithmetic expressions
    - [§ definitions](Scala%203.md#definitions): `def`
- [rewriting](../../../../general/rewriting.md) ::@:: It covers a wide range of methods of replacing subterms of a formula with other terms.
  - rewriting / substitution model ::@:: It is a way to _evaluate_ expressions _without side effects_. To evaluate a _function call_, each parameter to the function is evaluated from left to right. Then, replace the function call with the _function expression_, while _substituting_ each occurrence of the parameter name with the parameter value. <p> It is formalized in lambda calculus.
- [divergence](../../../../general/divergence%20(computer%20science).md) ::@:: A computation is said to __diverge__ if it does not terminate or terminates in an exceptional state. Otherwise it is said to __converge__.
  - divergence / example ::@:: Scala 3: `def loop: Int = loop; loop`
- [evaluation strategy](../../../../general/evaluation%20strategy.md) ::@:: It is a set of rules for evaluating expressions.
  - evaluation strategy / Scala 3 ::@:: 2 major evaluation strategies: call by name \(e.g., `def`, `=> <type>`\), call by value \(e.g., `val`\)
  - evaluation strategy / call by value \(CBV\) ::@:: Each parameter to the function is evaluated first. Then, to evaluate a function, each occurrence of each parameter is replaced by its corresponding value. <p> The advantage is if a parameter is used multiple times, only one evaluation is needed. The disadvantage is if a parameter is unused, one evaluation is still needed.
    - evaluation strategy / call by value / termination ::@:: If an expression terminates using CBN, it _may not_ terminate using CBV. This is because there may be some expressions evaluated by CBV are not evaluated by CBN. <p> Scala 3: Compare `def constant(x: Int) = 0; id(loop)` and `def constant(x: => Int) = 0; id(loop)`.
  - evaluation strategy / call by name \(CBN\) ::@:: Each parameter to the function is not evaluated. Rather, to evaluate a function, each occurrence of each parameter is replaced by its corresponding expression directly. <p> The advantage is if a parameter is used, no evaluation occurs. The disadvantage is each occurrence of a parameter evaluates the expression once.
    - evaluation strategy / call by name / termination ::@:: If an expression terminates using CBV, then it also terminates using CBN. This is because every expression evaluated by CBN is also evaluated by CBV.
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
- [scope](../../../../general/scope%20(computer%20science).md) ::@:: It of a name binding \(an association of a name to an entity, such as a variable\) is the part of a program where the name binding is valid; that is, where the name can be used to refer to the entity.
  - scope / motivation ::@:: It helps to avoid _namespace pollution_.
  - scope / lexical scoping ::@:: With it, a name always refers to its lexical context. This is a property of the program text and is made independent of the runtime call stack by the language implementation.
- Scala
  - Scala / Scala 3
    - [§ scoping](Scala%203.md#scoping): end marker
    - [§ expressions](Scala%203.md#expressions): semicolon

## week 1 lecture 2

- datetime: 2025-09-04T12:00:00+08:00/2025-09-04T13:20:00+08:00, PT1H20M
- topic: tail recursion
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / notation ::@:: The following notation expresses _replacing_ all occurrences of $x_i$ by $v_i$ \(or $v_i$ _substitutes_ $x_i$\) in the expression $E$: $$[v_1 / x_1, \ldots, v_n / x_n] E \,.$$
- [tail call](../../../../general/tail%20call.md) ::@:: It is a subroutine call performed as the final action of a procedure.
  - tail call / tail recursion ::@:: If the target of a tail is the same subroutine, the subroutine is said to be __tail recursive__, which is a special case of direct recursion. __Tail recursion__ \(or __tail-end recursion__\) is particularly useful, and is often easy to optimize in implementations.
    - tail call / tail recursion / substitution model ::@:: Assume _no side effects_. Under the substitution model, a tail-recursive function, when it calls itself, the expression _only contains_ a function call to itself. No matter how many times recursion occurs, the expression "_size_" will not explode.
  - tail call / tail-call elimination ::@:: Tail calls can be implemented without adding a new stack frame to the call stack. Most of the frame of the current procedure is no longer needed, and can be replaced by the frame of the tail call, modified as appropriate \(similar to overlay for processes, but for function calls\). The program can then jump to the called subroutine. Producing such code instead of a standard call sequence is called __tail-call elimination__ or __tail-call optimization__.
    - tail call / tail-call elimination / Scala 3 ::@:: In a function, only tail calls to itself are _optimized_. To ensure this is the case \(or emit a compiler error otherwise\), use the _annotation_ `@scala.annotation.tailrec`.
- Scala
  - Scala / Scala 3
    - [§ tail recursion](Scala%203.md#tail%20recursion): tail recursion
- [higher-order function](../../../../general/higher-order%20function.md) \(HOL\) ::@:: It is a function that does at least one of the following: <p> - takes one or more functions as arguments \(i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure\), <br/> - returns a function as its result.
  - higher-order function / functional language ::@:: Functional language treat functions as first-class citizens. They are treated as with other primitive types. It provides a flexible way to _compose_ programs.
- Scala
  - Scala / 3
    - [§ function types](Scala%203.md#function%20types): function types, no arguments
    - [§ anonymous functions](Scala%203.md#anonymous%20functions): anonymous functions, syntactic sugar
    - [§ multiple parameter lists](Scala%203.md#multiple%20parameter%20lists): multiple parameter lists, function application, currying
    - [§ function types](Scala%203.md#function%20types): currying
- [currying](../../../../general/currying.md) ::@:: It is the technique of translating a function that takes multiple arguments into a sequence of families of functions, each taking a single argument.
- higher-order function
  - higher-order function / examples ::@:: - `fold`/`reduce`: It is a higher-order function that analyzes a recursive data structure and through use of a given combining operation, recombines the results of recursively processing its constituent parts, building up a return value. <br/> - `map`: It is a higher-order function that applies a given function to each element of a collection, e.g. a list or set, returning the results in a collection of the same type. <br/> - `mapReduce`: `map` then `reduce`.
- [fixed point](../../../../general/fixed%20point.md) ::@:: It is a value that does not change under a given transformation. Specifically, for functions, a fixed point is an element that is mapped to itself by the function.
- [fixed-point iteration](../../../../general/fixed-point%20iteration.md) ::@:: It is a method of computing fixed points of a function. <p> More specifically, given a function $f$ defined on the [real numbers](../../../../general/real%20number.md) with real values and given a point $x_{0}$ in the [domain](../../../../general/domain%20of%20a%20function.md) of $f$, the fixed-point iteration is $$x_{n+1}=f(x_{n}),\,n=0,1,2,\dots$$ which gives rise to the [sequence](../../../../general/sequence.md) $x_{0},x_{1},x_{2},\dots$ of [iterated function](../../../../general/iterated%20function.md) applications $x_{0},f(x_{0}),f(f(x_{0})),\dots$ which is hoped to [converge](../../../../general/limit%20(mathematics).md) to a point $x_{\text{fix} }$.
  - fixed-point iteration / continuous function ::@:: If $f$ is continuous, then one can prove that the obtained $x_{\text{fix} }$ is a fixed point of $f$, i.e., $$f(x_{\text{fix} })=x_{\text{fix} }.$$ <p> More generally, the function $f$ can be defined on any [metric space](../../../../general/metric%20space.md) with values in that same space.
  - fixed-point iteration / square root ::@:: - A first simple and useful example is the [Babylonian method](../../../../general/Babylonian%20method.md#Heron's%20method) for computing the [square root](../../../../general/square%20root.md) of _a_ \> 0, which consists in taking $f(x)={\frac {1}{2} }\left({\frac {a}{x} }+x\right)$, i.e. the mean value of _x_ and _a_<!-- markdown separator -->/<!-- markdown separator -->_x_, to approach the limit $x={\sqrt {a} }$ \(from whatever starting point $x_{0}\gg 0$\). This is a special case of [Newton's method](../../../../general/Newton's%20method.md) quoted below.
- [extended Backus–Naur form](../../../../general/extended%20Backus–Naur%20form.md) \(EBNF\) ::@:: It is a family of metasyntax notations, any of which can be used to express a context-free grammar. EBNF is used to make a formal description of a formal language such as a computer programming language. They are extensions of the basic Backus–Naur form \(BNF\) metasyntax notation.
  - extended Backus–Naur form / basic syntax ::@:: definition: `<name> = <expr>` <br/> literal: `'<string>'` <br/> alternative \(choose one\): `<left expr> | <right expr>`  <br/> optional \(0 or 1 occurrence\): `[<expr>]` <br/> repetition \(0 or more occurrences\): `{<expr>}` <p> \(__this course__: Try to express Scala syntax in EBNF using the above elements only.\)
- Scala
  - Scala / Scala 3
    - [§ classes](Scala%203.md#classes): classes, constructor, members, abstraction, construction, `this`
    - [§ pre-definitions](Scala%203.md#pre-definitions): pre-definition
    - [§ checking](Scala%203.md#checking): precondition, assertion
    - [§ classes](Scala%203.md#classes): auxiliary constructor
    - [§ scoping](Scala%203.md#scoping): end marker
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / class ::@:: Assume _no side effects_. For the Scala 3 expression `C(x_1, ..., x_n).f(y_1, ..., y_m)`, it is rewritten to: $$[x_1/C_1, \ldots, x_n/C_n] [y_1/f_1, \ldots, y_m/f_m] [C(x_1, \ldots, x_n)/\text{this}] E \,.$$ That is, we replace `this` with the object _expression_, then replace function arguments, and finally replace class arguments. \(__this course__: Use this model. And we do the above 3 substitutions simultaneously.\) <p> Actually, the above model is not the best, since it does not handle constructors with side effects. A better model would evaluate `this = C(x_1, ..., x_n)`, then define `this.f` to extract the body expression of `f`, and finally evaluate `this.f(y_1, ..., y_m)` by substitution `this` in the body and the function arguments.
- Scala
  - Scala / Scala 3
    - [§ extension methods](Scala%203.md#extension%20methods): extension methods
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / class ::@:: Assume _no side effects_. For the Scala 3 expression `c.f(y_1, ..., y_m)` where `r` is the name used by the extension definition, it is rewritten to: $$[c/r] [y_1/f_1, \ldots, y_m/f_m] E \,.$$ That is, we replace function arguments, and then replace the name `r` used by the extension definition. \(__this course__: Use this model. And we do the above 2 substitutions simultaneously.\)
- Scala
  - Scala / Scala 3
    - [§ syntax](Scala%203.md#syntax): syntax
    - [§ identifiers](Scala%203.md#identifiers): identifier
    - [§ infix notation](Scala%203.md#infix%20notation): infix notation, operator, precedence

## week 2 lecture

- datetime: 2025-09-09T12:00:00+08:00/2025-09-09T13:20:00+08:00, PT1H20M
- topic: inheritance; objects; entry points; code organization; imports; traits; type system; exception handling; cons; type parameters; polymorphism; pure object-orientation
- Scala
  - Scala / Scala 3
    - [§ abstract classes](Scala%203.md#abstract%20classes): abstract class, syntax
    - [§ inheritance](Scala%203.md#inheritance): inheritance, class extension, terminology, `java.lang.Object`, implement, override
    - [§ objects](Scala%203.md#objects): object, singleton, propereties, value semantics
    - [§ companion objects](Scala%203.md#companion%20objects): companion object, properties, namespaces, visibility
    - [§ entry points](Scala%203.md#entry%20points): entry point
    - [§ traditional entry points](Scala%203.md#traditional%20entry%20points): entry point, traditional entry point, properties
    - [§ annotated entry points](Scala%203.md#annotated%20entry%20points): entry point, annotated entry point, `@scala.annotation.main`, properties
    - [§ dynamic binding](Scala%203.md#dynamic%20binding): dynamic binding, polymorphism, higher-order functions
    - [§ code organization](Scala%203.md#code%20organization): code organization, packages, imports
    - [§ packages](Scala%203.md#packages): packages
    - [§ imports](Scala%203.md#imports): imports, forms
    - [§ automatic imports](Scala%203.md#automatic%20imports): automatic imports
    - [§ Scala documentation](Scala%203.md#Scala%20documentation): Scala documentation
    - [§ traits](Scala%203.md#traits): trait
    - [§ top types](Scala%203.md#top%20types): top types, `scala.Any`, `scala.AnyRef`, `scala.AnyVal`
    - [§ nothing type](Scala%203.md#nothing%20type): nothing type, bottom type, `scala.Nothing`, abnormal termination, empty collections
    - [§ exception handling](Scala%203.md#exception%20handling): exception, exception handling, type
    - [§ type inference](Scala%203.md#type%20inference): type inference, least upper bound
    - [§ cons](Scala%203.md#cons): cons, cons-lists, immutability, structural recursion
    - [§ value parameters](Scala%203.md#value%20parameters): value parameters
    - [§ type parameters](Scala%203.md#type%20parameters): type parameters, generic types, generic functions
    - [§ generic types](Scala%203.md#generic%20types): generic types
    - [§ generic functions](Scala%203.md#generic%20functions): generic functions
    - [§ type inference in generics](Scala%203.md#type%20inference%20in%20generics): type inference in generics
    - [§ type erasure](Scala%203.md#type%20erasure): type erasure
- [polymorphism](../../../../general/polymorphism%20(computer%20science).md) ::@:: In programming language theory and type theory, it allows a value type to assume different types.
  - polymorphism / examples ::@:: A function or type can operate over many different data kinds. <p> A single function can be applied to arguments of various types. A single type can have instances of many concrete classes.  
  - polymorphism / types ::@:: The most commonly recognized major forms of polymorphism are: <p> - _Ad hoc polymorphism_: defines a common interface for an arbitrary set of individually specified types. <br/> - _Parametric polymorphism_: does not specify concrete types and instead uses abstract symbols that can substitute for any type. <br/> - _Subtyping_ (also called _subtype polymorphism_ or _inclusion polymorphism_): when a name denotes instances of many different classes related by a common superclass.
    - polymorphism / types / subtyping ::@:: an instance of a subclass may be used wherever an instance of its superclass is expected, enabling _is‑a_ relationships.  
    - polymorphism / types / parametric ::@:: functions or classes are defined with type parameters; concrete instances are created by supplying specific types, allowing the same code to work uniformly across all those types.
- Scala
  - Scala / Scala 3
    - [§ pure object-orientation](Scala%203.md#pure%20object-orientation): pure object-orientation, standard classes, idealized `scala.Boolean`, `scala.Int`, idealized `scala.Int` using `Nat`
    - [§ functions as objects](Scala%203.md#functions%20as%20objects): functions are objects, `scala.Function*`, anonymous function, function calls
    - [§ methods to functions](Scala%203.md#methods%20to%20functions): methods, methods to functions

## week 2 lecture 2

- datetime: 2025-09-11T12:00:00+08:00/2025-09-11T13:20:00+08:00, PT1H20M
- topic: pattern matching; case classes; list; enumeration
- [pattern matching](../../../../general/pattern%20matching.md) ::@:: It is the act of checking a given sequence of tokens for the presence of the constituents of some pattern. In contrast to pattern recognition, the match usually must be exact: "either it will or will not be a match." The patterns generally have the form of either sequences or tree structures.
  - pattern matching / motivation ::@:: representation → manual dispatch → manual dispatch with type tests and casts → dynamic dispatch → non-local or complex operations → pattern matching → summary
    - pattern matching / motivation / representation ::@:: Objects, and in this example, expressions are often modelled as a base type (`Expr`) with concrete subclasses such as `Number` and `Sum`. <p> Each subclass must expose classification (e.g., `isNumber`, `isSum`) and operations (`numValue`, `leftOp`, `rightOp`). Whether an operation is available or throws an runtime error depends on the classification.
    - pattern matching / motivation / manual dispatch ::@:: A evaluation function typically uses conditional checks on the classification flags. <p> Adding a new expression form (like `Prod` or `Var`) forces updates to all methods in the base type, leading to repetitive boilerplate. There is no compile‑time guarantee that the correct accessor is used for each subclass; an accidental misuse can trigger runtime errors.
    - pattern matching / motivation / manual dispatch with type tests and casts ::@:: Languages such as Scala provide `isInstanceOf[T]` and `asInstanceOf[T]`, analogous to Java's `instanceof` and casting syntax (`(T) x`). <p> This approach is verbose, error‑prone, and still offers no static type safety. The type tests and casts are effectively the classification methods.
    - pattern matching / motivation / dynamic dispatch ::@:: Move the operation (`eval`) into each subclass: `def eval: Int` implemented by `Number`, `Sum`, etc. <p> This encapsulates data with its behaviour, enabling straightforward addition of new data forms. However, operations become tightly coupled to the hierarchy; adding a new operation (e.g., pretty‑printing) requires touching every subclass, increasing maintenance burden and class dependencies.  
    - pattern matching / motivation / non-local or complex operations ::@:: Operations that need to inspect or modify multiple parts of the structure (e.g., algebraic simplification `a*b + a*c → a*(b+c)`) cannot be expressed as a method on a single node \(object\). The OO decomposition approach \(dynamic dispatch\) then collapses back into the same pattern‑matching or type‑testing problem, negating its benefits.
    - pattern matching / motivation / pattern matching ::@:: Many modern languages provide a dedicated construct for deconstructing algebraic data types (e.g., Scala's `match`, Haskell's case expressions). It cleanly separates the structure of the data from the operations performed on it, enabling new operations without modifying existing classes.
    - pattern matching / motivation / summary ::@:: Class hierarchies are natural for modelling algebraic structures but bring maintenance challenges when the set of constructors or operations changes frequently. <p> Relying on manual dispatch or type casts is brittle; better to use language features that treat data and behaviour as separate concerns (e.g., pattern matching, visitor patterns). <p> The choice between OO decomposition and a more functional style depends on whether operations are local to single objects or require global knowledge of the structure.
- Scala
  - Scala / Scala 3
    - [§ case classes](Scala%203.md#case%20classes): case classes, case classes syntax
    - [§ pattern matching](Scala%203.md#pattern%20matching): pattern matching, pattern matching syntax, variable binding, `sealed`, exhaustive matching, separation of behavior from data
    - [§ lists](Scala%203.md#lists): lists, immutability, recursive, homogeneity, constructors, right associativity, list operations, pattern matching on lists
    - [§ list sorting](Scala%203.md#list%20sorting): sorting, insertion sort
    - [§ enumerations](Scala%203.md#enumerations): pure data structures, case classes, enumerations, simple enumerations, parameterized enumerations, pattern matching on enumerations, methods, `Enum.ordinal`, `Enum.values`, domain modeling
- pattern matching
  - pattern matching / functional languages ::@:: __Functional languages__ (OCaml, Haskell) express algebraic data types with minimal syntax: <p> - OCaml: `type expr = Number of int | Sum of expr * expr` and a recursive `eval` using `match`. <br/> - Haskell: `data Expr = Number Int | Sum Expr Expr` with pattern‑matching function definitions.  
    - pattern matching / functional languages / Scala ::@:: These ADTs are typically more concise than Scala's, thanks to stronger type inference and lighter syntax. However, Scala's class hierarchies can be richer, supporting: <p> - Methods or fields in both base and derived classes. <br/> - Multi‑level sealed trait inheritance (e.g., `EitherOrBoth`, `Either`). <br/> - Open‑ended (non‑sealed) hierarchies. <br/> - Existential types resembling Generalised ADTs.  
  - pattern matching / imperative languages ::@:: They implement ADTs with tagged unions or discriminated unions: <p> - C: `typedef enum { NUMBER, SUM } ExprKind;` and a struct containing a union of concrete representations. The `eval` function uses a `switch` on the kind tag. <br/> - The pattern is verbose and prone to unsafe bugs (e.g., forgetting a case).  
  - pattern matching / popularity ::@:: Many languages now provide pattern matching over sealed class hierarchies, including Kotlin, Swift, and newer Java releases. These languages blend the expressiveness of functional ADTs with object‑oriented type systems.

## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic:

## week 3 lecture 2

- datetime: 2025-09-18T12:00:00+08:00/2025-09-18T13:20:00+08:00, PT1H20M
- topic:

## week 4 lecture

- datetime: 2025-09-23T12:00:00+08:00/2025-09-23T13:20:00+08:00, PT1H20M
- topic:

## week 4 lecture 2

- datetime: 2025-09-25T12:00:00+08:00/2025-09-25T13:20:00+08:00, PT1H20M
- topic:

## aftermath

### total

- grades: ?/100
  - statistics: ?
