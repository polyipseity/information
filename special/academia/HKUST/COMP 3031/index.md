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

- Scala
  - Scala / [actor model](actor%20model.md)
  - Scala / [algorithms](algorithms.md)
  - Scala / [collections](collections.md)
  - Scala / [context](context.md)
  - Scala / [futures and promises](futures%20and%20promises.md)
  - Scala / [imperative programming](imperative%20programming.md)
  - Scala / [kind](kind.md)
  - Scala / [lazy evaluation](lazy%20evaluation.md)
  - Scala / [Lisp](Lisp.md)
  - Scala / [logic programming](logic%20programming.md)
  - Scala / [monad](monad.md)
  - Scala / [proofs](proofs.md)
  - Scala / [reactive programming](reactive%20programming.md)
  - [Scala 3](Scala%203.md)
  - Scala / [state](state.md)
- [assignments](assignments/index.md)
- [`hkust-comp-3031-labs.git.7z`](attachments/hkust-comp-3031-labs.git.7z)
  - source: <https://github.com/polyipseity/hkust-comp-3031-labs.git>
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
  - COMP 3031 / objectives ::@:: Scala, functional programming, programming language constructs, programming language paradigms <!--SR:!2026-08-22,261,330!2026-05-10,175,310-->
- [programming paradigm](../../../../general/programming%20paradigm.md) ::@:: It is a relatively high-level way to conceptualize and structure the implementation of a computer program. <!--SR:!2026-09-19,285,330!2026-05-03,170,310-->
  - programming paradigm / common ::@:: concurrent, dependently-typed, functional, imperative, logic, object-oriented, parallel, etc. <!--SR:!2026-08-10,254,330!2026-09-30,294,330-->
- [imperative programming](../../../../general/imperative%20programming.md) ::@:: It is a programming paradigm of software that uses statements that change a program's state. <!--SR:!2026-08-24,263,330!2026-08-20,260,330-->
  - imperative programming / important elements ::@:: control structures, mutation, etc. <!--SR:!2026-09-30,294,330!2026-08-22,262,330-->
  - imperative programming / physical correspondence ::@:: It has strong correspondence with physical entities. <p> control structure ↔ jump <br/> field ↔ memory cell <br/> variable ↔ register <br/> variable assignment ↔ store \(instruction\) <br/> variable dereferencing ↔ load \(instruction\) <br/> ... <!--SR:!2026-08-28,265,330!2026-08-01,246,330-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <!--SR:!2026-03-17,126,290!2026-08-27,265,330-->
  - von Neumann architecture / von Neumann bottleneck ::@:: The use of the same bus to fetch instructions and data leads to the von Neumann bottleneck, the limited throughput \(data transfer rate\) between the central processing unit \(CPU\) and memory compared to the amount of memory. This seriously limits the effective processing speed when the CPU is required to perform minimal processing on large amounts of data. The CPU is continually forced to wait for needed data to move to or from memory. <!--SR:!2026-08-24,264,330!2026-09-23,288,330-->
    - von Neumann architecture / von Neumann bottleneck / trend ::@:: Since CPU speed and memory size have increased much faster than the throughput between them, the bottleneck has become more of a problem, a problem whose severity increases with every new generation of CPU. <!--SR:!2026-08-31,270,330!2026-08-09,253,330-->
- [theory](../../../../general/theory%20(mathematical%20logic).md) ::@:: It is a set of sentences in a formal language. <!--SR:!2026-09-11,278,330!2026-09-29,293,330-->
  - theory / for programming ::@:: data type\(s\), operation\(s\) on data type\(s\), law\(s\) on data and operations <br/> usually no mutations \(but possible with some difficulty\) <!--SR:!2026-09-25,290,330!2026-09-02,270,330-->
  - theory / mutation ::@:: A theory without mutation is usually much less complex than one with mutation. Mutation makes theories hard to understand. So most theories do not admit mutation. <p> For programming, this leads to _functional programming_. <!--SR:!2026-08-08,252,330!2026-09-23,288,330-->
- [functional programming](../../../../general/functional%20programming.md) ::@:: It is a programming paradigm where programs are constructed by applying and composing functions. <!--SR:!2026-08-07,251,330!2026-08-19,259,330-->
  - functional programming / missing elements ::@:: imperative control structures, no mutations \(__this course__: In a _restricted sense_, these elements are strictly _forbidden_.\) <!--SR:!2026-08-03,248,330!2026-09-16,282,330-->
  - functional programming / important elements ::@:: functions \(as first-class citizens\), immutable data types \(__this course__: In a _wide sense_, these elements are _emphasized_ on, but unmentioned elements \(e.g. above\) are not strictly forbidden.\) <!--SR:!2026-05-04,171,310!2026-09-09,276,330-->
  - functional programming / function ::@:: As first-class citizens, they can be composed, definable anywhere, passed as parameters, etc. <!--SR:!2026-08-04,249,330!2026-08-11,255,330-->
  - functional programming / examples ::@:: restricted: FP, Pure Lisp, XPath, XQuery, XSLT, etc. <br/> wider: Clojure, F\#, Haskell, Lips, Ocaml, Racket, SML, Scala, Scheme, etc. <!--SR:!2026-09-10,277,330!2026-08-25,265,330-->
- COMP 3031
  - COMP 3031 / recommended books
- [Scala](../../../../general/Scala%20(programming%20language).md) ::@:: It is a strongly statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. <p> \(__this course__: Use Scala 3.\) <!--SR:!2026-08-08,252,330!2026-09-11,278,330-->
  - Scala / Scala 3: [Scala 3](Scala%203.md)
- [programming language](../../../../general/programming%20language.md) ::@:: It is an artificial language for expressing computer programs. <!--SR:!2026-08-05,250,330!2026-09-17,283,330-->
  - programming language / elements ::@:: primitive expressions, composition of expressions, abstraction of expressions \(giving names to expressions\) <!--SR:!2026-08-21,260,330!2026-09-01,271,330-->
- [read–eval–print loop](../../../../general/read–eval–print%20loop.md) \(REPL\) ::@:: It is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise. <!--SR:!2026-05-05,171,310!2026-09-06,275,330-->
- Scala
  - Scala / Scala 3
    - [§ primitive types](Scala%203.md#primitive%20types): `Boolean`, `Int`, `Double`
    - [§ expressions](Scala%203.md#expressions): expressions, arithmetic expressions
    - [§ definitions](Scala%203.md#definitions): `def`
- [rewriting](../../../../general/rewriting.md) ::@:: It covers a wide range of methods of replacing subterms of a formula with other terms. <!--SR:!2026-08-11,255,330!2026-08-04,249,330-->
  - rewriting / substitution model ::@:: It is a way to _evaluate_ expressions _without side effects_. To evaluate a _function call_, each parameter to the function is evaluated from left to right. Then, replace the function call with the _function expression_, while _substituting_ each occurrence of the parameter name with the parameter value. <p> It is formalized in lambda calculus. <!--SR:!2026-08-30,269,330!2026-05-26,178,310-->
- [divergence](../../../../general/divergence%20(computer%20science).md) ::@:: A computation is said to __diverge__ if it does not terminate or terminates in an exceptional state. Otherwise it is said to __converge__. <!--SR:!2026-08-06,251,330!2026-08-10,254,330-->
  - divergence / example ::@:: Scala 3: `def loop: Int = loop; loop` <!--SR:!2026-09-24,289,330!2026-08-27,264,330-->
- [evaluation strategy](../../../../general/evaluation%20strategy.md) ::@:: It is a set of rules for evaluating expressions. <!--SR:!2026-08-07,251,330!2026-08-28,266,330-->
  - evaluation strategy / Scala 3 ::@:: 2 major evaluation strategies: call by name \(e.g., `def`, `=> <type>`\), call by value \(e.g., `val`\) <!--SR:!2026-09-07,275,330!2026-09-18,284,330-->
  - evaluation strategy / call by value \(CBV\) ::@:: Each parameter to the function is evaluated first. Then, to evaluate a function, each occurrence of each parameter is replaced by its corresponding value. <p> The advantage is if a parameter is used multiple times, only one evaluation is needed. The disadvantage is if a parameter is unused, one evaluation is still needed. <!--SR:!2026-06-14,191,310!2026-09-05,274,330-->
    - evaluation strategy / call by value / termination ::@:: If an expression terminates using CBN, it _may not_ terminate using CBV. This is because there may be some expressions evaluated by CBV are not evaluated by CBN. <p> Scala 3: Compare `def constant(x: Int) = 0; id(loop)` and `def constant(x: => Int) = 0; id(loop)`. <!--SR:!2026-08-23,262,330!2026-09-28,292,330-->
  - evaluation strategy / call by name \(CBN\) ::@:: Each parameter to the function is not evaluated. Rather, to evaluate a function, each occurrence of each parameter is replaced by its corresponding expression directly. <p> The advantage is if a parameter is used, no evaluation occurs. The disadvantage is each occurrence of a parameter evaluates the expression once. <!--SR:!2026-04-29,167,310!2026-08-21,261,330-->
    - evaluation strategy / call by name / termination ::@:: If an expression terminates using CBV, then it also terminates using CBN. This is because every expression evaluated by CBN is also evaluated by CBV. <!--SR:!2026-02-05,103,290!2026-01-13,68,270-->
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
- [scope](../../../../general/scope%20(computer%20science).md) ::@:: It of a name binding \(an association of a name to an entity, such as a variable\) is the part of a program where the name binding is valid; that is, where the name can be used to refer to the entity. <!--SR:!2026-08-03,248,330!2026-08-23,263,330-->
  - scope / motivation ::@:: It helps to avoid _namespace pollution_. <!--SR:!2026-08-06,251,330!2026-08-02,247,330-->
  - scope / lexical scoping ::@:: With it, a name always refers to its lexical context. This is a property of the program text and is made independent of the runtime call stack by the language implementation. <!--SR:!2026-09-08,276,330!2026-09-04,273,330-->
- Scala
  - Scala / Scala 3
    - [§ scoping](Scala%203.md#scoping): end marker
    - [§ expressions](Scala%203.md#expressions): semicolon

## week 1 lecture 2

- datetime: 2025-09-04T12:00:00+08:00/2025-09-04T13:20:00+08:00, PT1H20M
- topic: tail recursion
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / notation ::@:: The following notation expresses _replacing_ all occurrences of $x_i$ by $v_i$ \(or $v_i$ _substitutes_ $x_i$\) in the expression $E$: $$[v_1 / x_1, \ldots, v_n / x_n] E \,.$$ <!--SR:!2026-01-25,92,367!2026-01-25,92,367-->
- [tail call](../../../../general/tail%20call.md) ::@:: It is a subroutine call performed as the final action of a procedure. <!--SR:!2026-01-27,94,367!2026-01-26,93,367-->
  - tail call / tail recursion ::@:: If the target of a tail is the same subroutine, the subroutine is said to be __tail recursive__, which is a special case of direct recursion. __Tail recursion__ \(or __tail-end recursion__\) is particularly useful, and is often easy to optimize in implementations. <!--SR:!2026-01-23,90,367!2026-01-26,93,367-->
    - tail call / tail recursion / substitution model ::@:: Assume _no side effects_. Under the substitution model, a tail-recursive function, when it calls itself, the expression _only contains_ a function call to itself. No matter how many times recursion occurs, the expression "_size_" will not explode. <!--SR:!2026-01-24,91,367!2026-01-02,69,347-->
  - tail call / tail-call elimination ::@:: Tail calls can be implemented without adding a new stack frame to the call stack. Most of the frame of the current procedure is no longer needed, and can be replaced by the frame of the tail call, modified as appropriate \(similar to overlay for processes, but for function calls\). The program can then jump to the called subroutine. Producing such code instead of a standard call sequence is called __tail-call elimination__ or __tail-call optimization__. <!--SR:!2026-01-01,68,347!2026-05-16,174,347-->
    - tail call / tail-call elimination / Scala 3 ::@:: In a function, only tail calls to itself are _optimized_. To ensure this is the case \(or emit a compiler error otherwise\), use the _annotation_ `@scala.annotation.tailrec`. <!--SR:!2026-01-02,69,347!2026-01-27,94,367-->
- Scala
  - Scala / Scala 3
    - [§ tail recursion](Scala%203.md#tail%20recursion): tail recursion
- [higher-order function](../../../../general/higher-order%20function.md) \(HOL\) ::@:: It is a function that does at least one of the following: <p> - takes one or more functions as arguments \(i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure\), <br/> - returns a function as its result. <!--SR:!2026-01-25,92,367!2026-09-25,283,367-->
  - higher-order function / functional language ::@:: Functional language treat functions as first-class citizens. They are treated as with other primitive types. It provides a flexible way to _compose_ programs. <!--SR:!2026-05-09,168,347!2026-01-23,90,367-->
- Scala
  - Scala / 3
    - [§ function types](Scala%203.md#function%20types): function types, no arguments
    - [§ anonymous functions](Scala%203.md#anonymous%20functions): anonymous functions, syntactic sugar
    - [§ multiple parameter lists](Scala%203.md#multiple%20parameter%20lists): multiple parameter lists, function application, currying
    - [§ function types](Scala%203.md#function%20types): currying
- [currying](../../../../general/currying.md) ::@:: It is the technique of translating a function that takes multiple arguments into a sequence of families of functions, each taking a single argument. <!--SR:!2026-01-26,93,367!2026-01-25,92,367-->
- higher-order function
  - higher-order function / examples ::@:: - `fold`/`reduce`: It is a higher-order function that analyzes a recursive data structure and through use of a given combining operation, recombines the results of recursively processing its constituent parts, building up a return value. <br/> - `map`: It is a higher-order function that applies a given function to each element of a collection, e.g. a list or set, returning the results in a collection of the same type. <br/> - `mapReduce`: `map` then `reduce`. <!--SR:!2026-08-20,253,367!2026-01-24,91,367-->
- [fixed point](../../../../general/fixed%20point.md) ::@:: It is a value that does not change under a given transformation. Specifically, for functions, a fixed point is an element that is mapped to itself by the function. <!--SR:!2026-01-27,94,367!2026-01-27,94,367-->
- [fixed-point iteration](../../../../general/fixed-point%20iteration.md) ::@:: It is a method of computing fixed points of a function. <p> More specifically, given a function $f$ defined on the [real numbers](../../../../general/real%20number.md) with real values and given a point $x_{0}$ in the [domain](../../../../general/domain%20of%20a%20function.md) of $f$, the fixed-point iteration is $$x_{n+1}=f(x_{n}),\,n=0,1,2,\dots$$ which gives rise to the [sequence](../../../../general/sequence.md) $x_{0},x_{1},x_{2},\dots$ of [iterated function](../../../../general/iterated%20function.md) applications $x_{0},f(x_{0}),f(f(x_{0})),\dots$ which is hoped to [converge](../../../../general/limit%20(mathematics).md) to a point $x_{\text{fix} }$. <!--SR:!2026-10-01,288,367!2026-01-24,91,367-->
  - fixed-point iteration / continuous function ::@:: If $f$ is continuous, then one can prove that the obtained $x_{\text{fix} }$ is a fixed point of $f$, i.e., $$f(x_{\text{fix} })=x_{\text{fix} }.$$ <p> More generally, the function $f$ can be defined on any [metric space](../../../../general/metric%20space.md) with values in that same space. <!--SR:!2026-01-23,90,367!2026-01-27,94,367-->
  - fixed-point iteration / square root ::@:: - A first simple and useful example is the [Babylonian method](../../../../general/Babylonian%20method.md#Heron's%20method) for computing the [square root](../../../../general/square%20root.md) of _a_ \> 0, which consists in taking $f(x)={\frac {1}{2} }\left({\frac {a}{x} }+x\right)$, i.e. the mean value of _x_ and _a_<!-- markdown separator -->/<!-- markdown separator -->_x_, to approach the limit $x={\sqrt {a} }$ \(from whatever starting point $x_{0}\gg 0$\). This is a special case of [Newton's method](../../../../general/Newton's%20method.md) quoted below. <!--SR:!2026-08-26,257,367!2026-10-01,288,367-->
- [extended Backus–Naur form](../../../../general/extended%20Backus–Naur%20form.md) \(EBNF\) ::@:: It is a family of metasyntax notations, any of which can be used to express a context-free grammar. EBNF is used to make a formal description of a formal language such as a computer programming language. They are extensions of the basic Backus–Naur form \(BNF\) metasyntax notation. <!--SR:!2026-08-24,256,367!2026-01-26,93,367-->
  - extended Backus–Naur form / basic syntax ::@:: definition: `<name> = <expr>` <br/> literal: `'<string>'` <br/> alternative \(choose one\): `<left expr> | <right expr>`  <br/> optional \(0 or 1 occurrence\): `[<expr>]` <br/> repetition \(0 or more occurrences\): `{<expr>}` <p> \(__this course__: Try to express Scala syntax in EBNF using the above elements only.\) <!--SR:!2026-10-01,288,367!2026-01-25,92,367-->
- Scala
  - Scala / Scala 3
    - [§ classes](Scala%203.md#classes): classes, constructor, members, abstraction, construction, `this`
    - [§ pre-definitions](Scala%203.md#pre-definitions): pre-definition
    - [§ checking](Scala%203.md#checking): precondition, assertion
    - [§ classes](Scala%203.md#classes): auxiliary constructor
    - [§ scoping](Scala%203.md#scoping): end marker
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / class ::@:: Assume _no side effects_. For the Scala 3 expression `C(x_1, ..., x_n).f(y_1, ..., y_m)`, it is rewritten to: $$[x_1/C_1, \ldots, x_n/C_n] [y_1/f_1, \ldots, y_m/f_m] [C(x_1, \ldots, x_n)/\text{this}] E \,.$$ That is, we replace `this` with the object _expression_, then replace function arguments, and finally replace class arguments. \(__this course__: Use this model. And we do the above 3 substitutions simultaneously.\) <p> Actually, the above model is not the best, since it does not handle constructors with side effects. A better model would evaluate `this = C(x_1, ..., x_n)`, then define `this.f` to extract the body expression of `f`, and finally evaluate `this.f(y_1, ..., y_m)` by substituting `this` in the body and the function arguments. <!--SR:!2026-04-12,147,347!2026-04-10,134,327-->
- Scala
  - Scala / Scala 3
    - [§ extension methods](Scala%203.md#extension%20methods): extension methods
- rewriting
  - rewriting / substitution model
    - rewriting / substitution model / class ::@:: Assume _no side effects_. For the Scala 3 expression `c.f(y_1, ..., y_m)` where `r` is the name used by the extension definition, it is rewritten to: $$[c/r] [y_1/f_1, \ldots, y_m/f_m] E \,.$$ That is, we replace function arguments, and then replace the name `r` used by the extension definition. \(__this course__: Use this model. And we do the above 2 substitutions simultaneously.\) <!--SR:!2026-05-17,175,347!2026-01-26,93,367-->
- Scala
  - Scala / Scala 3
    - [§ syntax](Scala%203.md#syntax): syntax
    - [§ identifiers](Scala%203.md#identifiers): identifier
    - [§ infix notation](Scala%203.md#infix%20notation): infix notation, operator, precedence

## week 2 lab

- datetime: 2025-09-08T15:00:00+08:00/2025-09-08T16:20:00+08:00, PT1H20M
- status: online; typhoon signal 8
- topic: tools; lab 0; project structure; sbt; IDE; REPL; worksheet; coding
- COMP 3031
  - COMP 3031 / tools ::@:: Coursier \(<https://get-coursier.io>\): Java Development Kit \(JDK\), simple build tool \(sbt\) <br/> Visual Studio Code, extensions: Scala \(Metals\) <!--SR:!2026-02-26,102,384!2026-02-25,101,384-->
  - COMP 3031 / lab 0
    - COMP 3031 / lab 0 / project structure ::@:: Download the skeleton project from Canvas; after extraction you'll see a standard sbt layout. All files ending in `.sbt` or inside `project/` are configuration; modify only the Scala source and test files. <!--SR:!2026-02-21,97,384!2026-02-21,97,384-->
    - COMP 3031 / lab 0 / sbt ::@:: Start the build tool with `sbt`. Compile your code with `compile`; run all tests with `test`, which will automatically compile if needed. <p> If compilation fails, no tests run – address compiler errors first. The first test run usually fails intentionally; read the stack trace to locate the failing line in your source. <!--SR:!2026-02-24,100,384!2026-02-25,101,384-->
    - COMP 3031 / lab 0 / navigation ::@:: When a test throws `NotImplementedError`, locate the call site via the stack trace (`Lists.scala:25` for example). Hover over the method name in the editor to see its signature and documentation. Use "Go to Definition" (Ctrl/Cmd-click or right-click) to jump straight to the offending implementation. <p> Replace placeholder `???` with a proper algorithm before re-running tests. <!--SR:!2026-02-23,99,384!2026-02-27,103,384-->
    - COMP 3031 / lab 0 / IDE tips ::@:: - New lines are auto-indented; manual indentation uses Tab/Shift-Tab. <br/> - Do not rename existing methods or classes, as automated grading relies on their names. <br/> - View compiler warnings/errors by clicking the "Problems" pane in VS Code. <br/> - Documentation for Scala \(<https://scala-lang.org/api/3.x/>\) and Java \(<https://docs.oracle.com/en/java/javase/25/docs/api/index.html>\) is available online if IDE hover support falls short. <!--SR:!2026-02-22,98,384!2026-02-21,97,384-->
    - COMP 3031 / lab 0 / test ::@:: In a terminal inside the project, start sbt and then run `~test` to enable watch mode; every file save automatically re-runs tests. For targeted testing use `testOnly`, e.g. `testOnly org.example.*Slow org.example.MyTest1`. <!--SR:!2026-02-24,100,384!2026-04-10,129,364-->
    - COMP 3031 / lab 0 / REPL ::@:: Launch the REPL with `console` from sbt (`scala>` prompt). <p> Evaluate expressions directly, e.g., `List(3,7,2)` or import lab methods: `import lab0.Lists.*`. Exit the REPL back to sbt with `Ctrl+D`. <p> For multiline input use Alt+Enter (or Option+Enter on macOS after setting "Use Option as Meta key" in Terminal preferences). <!--SR:!2025-12-22,43,344!2026-02-27,103,384-->
    - COMP 3031 / lab 0 / worksheet ::@:: Create a file ending in `.worksheet.sc`; each line is executed automatically and its result shown as a comment. Save the file to trigger re-evaluation; auto-save is enabled by default. <!--SR:!2026-02-23,99,384!2026-02-22,98,384-->
    - COMP 3031 / lab 0 / troubleshooting ::@:: - If sbt fails, run `sbt clean cleanFile` or delete the global cache (`rm -r ~/.sbt`). <br/> - If IDE features like hover or go-to-definition are broken, manually import the build via the "m" icon → "Import build", then restart VS Code. <br/> - Address Bloop server warnings by following the on-screen prompts ("Turn off old server"). <!--SR:!2026-02-21,97,384!2026-02-22,98,384-->
    - COMP 3031 / lab 0 / coding ::@:: - `Lists.scala` implements two tail-recursive functions: <br/> &emsp; - `sum(xs: List[Int])`: accumulates list elements, returning `0` for an empty list. <br/> &emsp; - `max(xs: List[Int])`: throws `NoSuchElementException` on an empty list; otherwise returns the maximum value by comparing head with accumulator. <br/> - `ListsSuite.scala` contains sanity checks (e.g., one plus one equals two) and additional tests: <br/> &emsp; - Verifies that `sum(Nil)` yields `0`. <br/> &emsp; - Confirms that calling `max(Nil)` raises the expected exception, using a try-catch block to fail if no exception occurs. <!--SR:!2026-02-24,100,384!2026-02-27,103,384-->

---

> \[redacted\] — 12:29
> We will still hold the lab, as it's quite helpful to people who want to know how to set up the Scala toolchains. But you are free to not attend it. I will also ask the TAs to make a Zoom session for people to join online <br/>
> Basically the lab is formally cancelled, but feel free to still attend it @everyone
>
> ---
>
> \[redacted\] — 14:59
> Here is the zoom link: \[redacted\] <br/>
> Zoom <br/>
> Join our Cloud HD Video Meeting <br/>
> Zoom is the leader in modern enterprise cloud communications.

## week 2 lecture

- datetime: 2025-09-09T12:00:00+08:00/2025-09-09T13:20:00+08:00, PT1H20M
- topic: inheritance; objects; entry points; code organization; imports; traits; type system; exceptions; cons; type parameters; polymorphism; pure object-orientation
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
    - [§ exceptions](Scala%203.md#exceptions): exceptions, exception handling, type
    - [§ type inference](Scala%203.md#type%20inference): type inference, least upper bound
    - [§ cons](Scala%203.md#cons): cons, cons-lists, immutability, structural recursion
    - [§ value parameters](Scala%203.md#value%20parameters): value parameters
    - [§ type parameters](Scala%203.md#type%20parameters): type parameters, generic types, generic functions
    - [§ generic types](Scala%203.md#generic%20types): generic types
    - [§ generic functions](Scala%203.md#generic%20functions): generic functions
    - [§ type inference in generics](Scala%203.md#type%20inference%20in%20generics): type inference in generics
    - [§ type erasure](Scala%203.md#type%20erasure): type erasure
- [polymorphism](../../../../general/polymorphism%20(computer%20science).md) ::@:: In programming language theory and type theory, it allows a value type to assume different types. <!--SR:!2026-02-27,103,384!2026-02-20,97,384-->
  - polymorphism / examples ::@:: A function or type can operate over many different data kinds. <p> A single function can be applied to arguments of various types. A single type can have instances of many concrete classes. <!--SR:!2026-02-22,98,384!2026-02-25,101,384-->
  - polymorphism / types ::@:: The most commonly recognized major forms of polymorphism are: <p> - _Ad hoc polymorphism_: defines a common interface for an arbitrary set of individually specified types. <br/> - _Parametric polymorphism_: does not specify concrete types and instead uses abstract symbols that can substitute for any type. <br/> - _Subtyping_ (also called _subtype polymorphism_ or _inclusion polymorphism_): when a name denotes instances of many different classes related by a common superclass. <!--SR:!2026-02-21,98,384!2026-02-25,101,384-->
    - polymorphism / types / subtyping ::@:: an instance of a subclass may be used wherever an instance of its superclass is expected, enabling _is-a_ relationships. <!--SR:!2026-02-15,93,384!2026-02-27,103,384-->
    - polymorphism / types / parametric ::@:: functions or classes are defined with type parameters; concrete instances are created by supplying specific types, allowing the same code to work uniformly across all those types. <!--SR:!2026-02-13,91,384!2026-02-22,98,384-->
- Scala
  - Scala / Scala 3
    - [§ pure object-orientation](Scala%203.md#pure%20object-orientation): pure object-orientation, standard classes, idealized `scala.Boolean`, `scala.Int`, idealized `scala.Int` using `Nat`
    - [§ functions as objects](Scala%203.md#functions%20as%20objects): functions are objects, `scala.Function*`, anonymous function, function calls
    - [§ methods to functions](Scala%203.md#methods%20to%20functions): methods, methods to functions

## week 2 lecture 2

- datetime: 2025-09-11T12:00:00+08:00/2025-09-11T13:20:00+08:00, PT1H20M
- topic: pattern matching; case classes; list; enumeration
- [pattern matching](../../../../general/pattern%20matching.md) ::@:: It is the act of checking a given sequence of tokens for the presence of the constituents of some pattern. In contrast to pattern recognition, the match usually must be exact: "either it will or will not be a match." The patterns generally have the form of either sequences or tree structures. <!--SR:!2026-02-21,98,384!2026-02-22,98,384-->
  - pattern matching / motivation ::@:: representation → manual dispatch → manual dispatch with type tests and casts → dynamic dispatch → non-local or complex operations → pattern matching → summary <!--SR:!2026-02-13,91,384!2026-02-26,102,384-->
    - pattern matching / motivation / representation ::@:: Objects, and in this example, expressions are often modelled as a base type (`Expr`) with concrete subclasses such as `Number` and `Sum`. <p> Each subclass must expose classification (e.g., `isNumber`, `isSum`) and operations (`numValue`, `leftOp`, `rightOp`). Whether an operation is available or throws an runtime error depends on the classification. <!--SR:!2026-02-24,100,384!2026-02-22,98,384-->
    - pattern matching / motivation / manual dispatch ::@:: A evaluation function typically uses conditional checks on the classification flags. <p> Adding a new expression form (like `Prod` or `Var`) forces updates to all methods in the base type, leading to repetitive boilerplate. There is no compile-time guarantee that the correct accessor is used for each subclass; an accidental misuse can trigger runtime errors. <!--SR:!2026-02-15,93,384!2026-02-23,99,384-->
    - pattern matching / motivation / manual dispatch with type tests and casts ::@:: Languages such as Scala provide `isInstanceOf[T]` and `asInstanceOf[T]`, analogous to Java's `instanceof` and casting syntax (`(T) x`). <p> This approach is verbose, error-prone, and still offers no static type safety. The type tests and casts are effectively the classification methods. <!--SR:!2026-02-24,100,384!2026-01-13,65,364-->
    - pattern matching / motivation / dynamic dispatch ::@:: Move the operation (`eval`) into each subclass: `def eval: Int` implemented by `Number`, `Sum`, etc. <p> This encapsulates data with its behaviour, enabling straightforward addition of new data forms. However, operations become tightly coupled to the hierarchy; adding a new operation (e.g., pretty-printing) requires touching every subclass, increasing maintenance burden and class dependencies. <!--SR:!2026-02-27,103,384!2026-02-27,103,384-->
    - pattern matching / motivation / non-local or complex operations ::@:: Operations that need to inspect or modify multiple parts of the structure (e.g., algebraic simplification `a*b + a*c → a*(b+c)`) cannot be expressed as a method on a single node \(object\). The OO decomposition approach \(dynamic dispatch\) then collapses back into the same pattern-matching or type-testing problem, negating its benefits. <!--SR:!2026-02-27,103,384!2026-02-19,96,384-->
    - pattern matching / motivation / pattern matching ::@:: Many modern languages provide a dedicated construct for deconstructing algebraic data types (e.g., Scala's `match`, Haskell's case expressions). It cleanly separates the structure of the data from the operations performed on it, enabling new operations without modifying existing classes. <!--SR:!2026-02-25,101,384!2026-02-26,102,384-->
    - pattern matching / motivation / summary ::@:: Class hierarchies are natural for modelling algebraic structures but bring maintenance challenges when the set of constructors or operations changes frequently. <p> Relying on manual dispatch or type casts is brittle; better to use language features that treat data and behaviour as separate concerns (e.g., pattern matching, visitor patterns). <p> The choice between OO decomposition and a more functional style depends on whether operations are local to single objects or require global knowledge of the structure. <!--SR:!2026-02-22,98,384!2026-02-19,96,384-->
- Scala
  - Scala / Scala 3
    - [§ case classes](Scala%203.md#case%20classes): case classes, case classes syntax
    - [§ pattern matching](Scala%203.md#pattern%20matching): pattern matching, pattern matching syntax, variable binding, `sealed`, exhaustive matching, separation of behavior from data
  - Scala / [collections](collections.md)
    - [§ list](collections.md#list): lists, immutability, recursive, homogeneity, constructors, right associativity, list operations, pattern matching on lists
  - Scala / [algorithms](algorithms.md)
    - [§ insertion sort](algorithms.md#insertion%20sort): sorting, insertion sort
  - Scala / Scala 3
    - [§ enumerations](Scala%203.md#enumerations): pure data structures, case classes, enumerations, simple enumerations, parameterized enumerations, pattern matching on enumerations, methods, `Enum.ordinal`, `Enum.values`, domain modeling
- pattern matching
  - pattern matching / functional languages ::@:: __Functional languages__ (OCaml, Haskell) express algebraic data types with minimal syntax: <p> - OCaml: `type expr = Number of int | Sum of expr * expr` and a recursive `eval` using `match`. <br/> - Haskell: `data Expr = Number Int | Sum Expr Expr` with pattern-matching function definitions. <!--SR:!2026-02-27,103,384!2026-02-25,101,384-->
    - pattern matching / functional languages / Scala ::@:: These ADTs are typically more concise than Scala's, thanks to stronger type inference and lighter syntax. However, Scala's class hierarchies can be richer, supporting: <p> - Methods or fields in both base and derived classes. <br/> - Multi-level sealed trait inheritance (e.g., `EitherOrBoth`, `Either`). <br/> - Open-ended (non-sealed) hierarchies. <br/> - Existential types resembling Generalised ADTs. <!--SR:!2026-02-27,103,384!2026-02-24,100,384-->
  - pattern matching / imperative languages ::@:: They implement ADTs with tagged unions or discriminated unions: <p> - C: `typedef enum { NUMBER, SUM } ExprKind;` and a struct containing a union of concrete representations. The `eval` function uses a `switch` on the kind tag. <br/> - The pattern is verbose and prone to unsafe bugs (e.g., forgetting a case). <!--SR:!2026-02-26,102,384!2026-02-25,101,384-->
  - pattern matching / popularity ::@:: Many languages now provide pattern matching over sealed class hierarchies, including Kotlin, Swift, and newer Java releases. These languages blend the expressiveness of functional ADTs with object-oriented type systems. <!--SR:!2026-02-26,102,384!2026-02-22,98,384-->

## week 3 lab

- datetime: 2025-09-15T15:00:00+08:00/2025-09-15T16:20:00+08:00, PT1H20M
- topic: tools; lab 0; project structure; sbt; IDE; REPL; worksheet; coding; functional programming
- [§ week 2 lab](#week%202%20lab)
- COMP 3031
  - COMP 3031 / lab 0
  - COMP 3031 / lab 1
    - COMP 3031 / lab 1 / functional programming ::@:: All solutions must avoid state mutation: you cannot use `var`, loops such as `while`, or explicit `return` statements. The Scala collection package `scala.collection.mutable` is forbidden; only immutable collections may be employed. <!--SR:!2026-02-14,92,384!2026-02-26,102,384-->
    - COMP 3031 / lab 1 / Pascal's triangle You are asked to compute the value that appears in a particular column `c` (0-based) of row `r` in Pascal's triangle. The triangle is defined such that every entry on its edges equals 1, and each interior entry equals the sum of the two numbers directly above it. Your implementation must be purely recursive—no loops or mutable state are allowed.
      - COMP 3031 / lab 1 / Pascal's triangle / solution ::@:: The function checks whether the requested position lies on an edge (`c == 0` or `c == r`). If so, it returns 1 immediately. Otherwise it recursively evaluates the two parents: `pascal(c-1, r-1)` for the upper-left value and `pascal(c, r-1)` for the upper-right value, then returns their sum. This straightforward recursion follows exactly the mathematical definition of Pascal's triangle. <!--SR:!2026-02-15,93,384!2026-02-15,93,384-->
    - COMP 3031 / lab 1 / parentheses balancing ::@:: Given a list of characters representing a string, determine whether all parentheses in the sequence are properly matched and nested. The function must be tail-recursive, cannot use mutation, and should handle arbitrary other characters by ignoring them. <!--SR:!2026-02-22,98,384!2026-02-23,99,384-->
      - COMP 3031 / lab 1 / parentheses balancing / solution ::@:: An inner helper `rec(chars: List[Char], acc: Int)` processes the list one element at a time while keeping an accumulator that counts unmatched opening brackets. When encountering `'('`, it increments `acc`; for `')'` it decrements; any other character leaves `acc` unchanged. If `acc` ever becomes negative, the function returns false immediately because a closing bracket has no matching opener. When the list ends, the string is balanced only if `acc` equals zero. The outer function simply calls this helper with an initial accumulator of 0. <!--SR:!2026-02-14,92,384!2026-02-27,103,384-->
    - COMP 3031 / lab 1 / counting change ::@:: You must compute how many distinct ways exist to make change for a given amount using a provided list of coin denominations (each denomination can be used unlimited times). The algorithm should be recursive and handle edge cases such as zero amount or an empty coin set. <!--SR:!2026-02-24,100,384!2026-02-26,102,384-->
      - COMP 3031 / lab 1 / counting change / solution ::@:: The function first deals with base cases: if the target money is negative, return 0; if it equals zero, there is exactly one way (use no coins). If the list of coins is empty while the amount remains positive, return 0. For a non-empty list, let `coin` be the head and `tail` the remainder. The total number of ways is the sum of two recursive calls: one that includes at least one `coin` (`countChange(money - coin, coins)`) and another that excludes it entirely (`countChange(money, tail)`). This recurrence explores all combinations systematically without duplication. <!--SR:!2026-02-22,98,384!2026-02-21,97,384-->
    - COMP 3031 / lab 1 / tips ::@:: - Use the immutable List operations (`isEmpty`, `head`, `tail`) to navigate lists instead of indices. <br/> - Think carefully about degenerate cases (zero amount, empty coin set) to avoid infinite recursion or incorrect counts. <br/> - For tail-recursion, annotate the helper with `@tailrec` to ensure the compiler verifies termination and stack safety. <!--SR:!2026-02-24,100,384!2026-02-24,100,384-->

## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance; variance of functions; list covariance; list methods
- Scala
  - Scala / Scala 3
    - [§ polymorphism](Scala%203.md#polymorphism): polymorphism, subtyping polymorphism, parametric polymorphism
    - [§ type bounds](Scala%203.md#type%20bounds): type bounds, upper bounds, lower bounds, mixed bounds
    - [§ variance](Scala%203.md#variance): variance, covariance, contravariance, invariance
    - [§ variance pitfalls](Scala%203.md#variance%20pitfalls): variance pitfalls, Java arrays, covariance of Java arrays
    - [§ variance checks](Scala%203.md#variance%20checks): variance checks
    - [§ function type variance](Scala%203.md#function%20type%20variance): function type variance, contravariant parameter types, covariant return types, multiple arguments, currying, function types as argument types
  - Scala / collections
    - [§ list covariance](collections.md#list%20covariance): list covariance, list covariance implementation
    - [§ list methods](collections.md#list%20methods): list methods

## week 3 lecture 2

- datetime: 2025-09-18T12:00:00+08:00/2025-09-18T13:20:00+08:00, PT1H20M
- topic: merge sort
- Scala
  - Scala / algorithms
    - [§ merge sort](algorithms.md#merge%20sort): sorting, merge sort
    - [§ merge sort splitting](algorithms.md#merge%20sort%20splitting): splitting in merge sort
  - Scala / Scala 3
    - [§ tuples](Scala%203.md#tuples): tuples
  - Scala / algorithms
    - [§ merge sort merging](algorithms.md#merge%20sort%20merging): merging in merge sort
    - [§ sorting arbitrary types](algorithms.md#sorting%20arbitrary%20types): sorting arbitrary types, comparator
  - Scala / Scala 3
    - [§ tuple as the only function argument](Scala%203.md#tuple%20as%20the%20only%20function%20argument): tuple as the only function argument, function call syntax
  - Scala / collections
    - [§ higher-order methods](collections.md#higher-order%20methods): higher-order methods, map, filter, reduce
    - [§ map](collections.md#map): map, map example
    - [§ filter](collections.md#filter): filter, filter example
    - [§ pack](collections.md#pack): pack, pack example
    - [§ reduce](collections.md#reduce): reduce, `reduceLeft`, `foldLeft`, initial value, `reduceRight`, `foldRight`, reduce example

## week 4 lab

- datetime: 2025-09-22T15:00:00+08:00/2025-09-22T16:20:00+08:00, PT1H20M
- topic: higher-order functions; generic programming
- COMP 3031
  - COMP 3031 / exercise 1 ::@:: Students explore higher-order functions (functions that take or return other functions) in Scala, then apply generic programming to design a type-safe binary search tree (BST) without duplicates. <!--SR:!2026-02-27,103,384!2026-02-19,96,384-->
    - COMP 3031 / exercise 1 / `flip` ::@:: Takes a two-argument function `f: (Int, Double) => Int` and returns a new function that calls `f` with its arguments swapped: `(x, y) => f(y, x)`. <!--SR:!2026-02-20,97,384!2026-02-26,102,384-->
    - COMP 3031 / exercise 1 / `identity` ::@:: `id: Int => Int = x => x`. <!--SR:!2026-02-24,100,384!2026-02-26,102,384-->
    - COMP 3031 / exercise 1 / `compose` ::@:: `compose(f,g)(x) = f(g(x))`; implemented as `x => f(g(x))`. <!--SR:!2026-02-23,99,384!2026-02-21,97,384-->
    - COMP 3031 / exercise 1 / `repeated` ::@:: - Recursively builds a function that applies its argument `f` exactly `n` times. <br/> - Base case: `n == 0` returns the identity; otherwise `compose(f, repeated(f,n-1))`. <br/> - Examples: `repeated(x=>x+1,0)` is `id`; `repeated(x=>x+1,3)(0)` yields `3`. <!--SR:!2026-02-26,102,384!2026-02-23,99,384-->
    - COMP 3031 / exercise 1 / `curry2` ::@:: `curry2(f)(x)(y) = f(x,y)`; implementation `x => y => f(x,y)`. <!--SR:!2026-02-27,103,384!2026-02-22,98,384-->
    - COMP 3031 / exercise 1 / `uncurry2` ::@:: `uncurry2(g)(x,y) = g(x)(y)`; implemented as `(x,y)=>g(x)(y)`. <!--SR:!2026-02-25,101,384!2026-02-26,102,384-->
    - COMP 3031 / exercise 1 / `fixedPoint` ::@:: `fixedPoint(f)` returns a function that repeatedly applies `f` until a fixed point is reached (`f(x)=x`). Tail-recursive helper: `@tailrec def rec(x:Int): Int = { val fx = f(x); if (fx==x) x else rec(fx) }` <!--SR:!2026-02-23,99,384!2026-02-26,102,384-->
      - COMP 3031 / exercise 1 / `fixedPoint` / `fixedPoint(x=>x/2)(4)` ::@:: `fixedPoint(x=>x/2)(4)` → `0` (halves until zero). <!--SR:!2026-02-23,99,384!2026-02-18,95,384-->
      - COMP 3031 / exercise 1 / `fixedPoint` / `fixedPoint(id)(123456)` ::@:: `fixedPoint(id)(123456)` → `123456`. <!--SR:!2026-02-25,101,384!2026-02-23,99,384-->
      - COMP 3031 / exercise 1 / `fixedPoint` / `fixedPoint(x=>x+1)(0)` ::@:: `fixedPoint(x=>x+1)(0)` diverges (no fixed point). <!--SR:!2026-02-25,101,384!2026-02-18,95,384-->
      - COMP 3031 / exercise 1 / `fixedPoint` / `fixedPoint(x => if (x%10==0) x else x+1)(35)` ::@:: `fixedPoint(x => if (x%10==0) x else x+1)(35)` → `40` (increments to next multiple of 10). <!--SR:!2026-02-27,103,384!2026-02-23,99,384-->
      - COMP 3031 / exercise 1 / `fixedPoint` / `fixedPoint(x => x/2 + 5)(20)` ::@:: `fixedPoint(x => x/2 + 5)(20)` → `10`. <!--SR:!2026-02-22,98,384!2026-02-23,99,384-->
    - COMP 3031 / exercise 1 / `sum` ::@:: `sum(f)(a,b)` accumulates `f(i)` for all integers `i` in `[a,b]`. Tail-recursive implementation uses an accumulator. <!--SR:!2026-02-22,98,384!2026-02-23,99,384-->
    - COMP 3031 / exercise 1 / `quadratic` ::@:: `quadratic(c)` produces a function `x => (x-c)^2`. <!--SR:!2026-02-24,100,384!2026-02-21,97,384-->
    - COMP 3031 / exercise 1 / `quad3Integrate` ::@:: `quad3Integrate(a,b)` is shorthand for `sum(quadratic(3))(a, b)`, computing the sum of `(i-3)^2` over `[a, b]`. <!--SR:!2026-02-26,102,384!2026-02-27,103,384-->
    - COMP 3031 / exercise 1  / comparator ::@:: A binary relation satisfying transitivity, reflexivity, anti-symmetry, and totality. Used to enforce a total order on elements of a structure, e.g. list elements, tree elements. <!--SR:!2026-02-22,98,384!2026-02-25,101,384-->
      - COMP 3031 / exercise 1 / comparator / equality ::@:: `eq(leq)(x,y) = leq(x,y) && leq(y,x)`; returns true iff both directions hold. <!--SR:!2026-02-25,101,384!2026-02-25,101,384-->
      - COMP 3031 / exercise 1 / comparator / strict less-than ::@:: `lt(leq)(x,y) = !leq(y,x)`; true when `x` is not greater or equal to `y`. <!--SR:!2026-02-24,100,384!2026-02-24,100,384-->
    - COMP 3031 / exercise 1 / tree ADT ::@:: - __`Tree`__: `sealed abstract class Tree[T]` <br/> - __`EmptyTree`__: `case class EmptyTree[T](leq: (T, T) => Boolean) extends Tree[T]` <br/> - __`Node`__: `case class Node[T](left: Tree[T], elem: T, right: Tree[T], leq: (T, T) => Boolean) extends Tree[T]` <!--SR:!2026-02-20,93,364!2026-02-23,99,384-->
      - COMP 3031 / exercise 1 / tree ADT / size ::@:: - _Pattern-matching version_: `def size = this match { Empty => 0; Node(l, _, r, _)= > l.size + r.size + 1 }`. <br/> - _Subclass override_: each case class implements its own `size` method. <!--SR:!2026-02-26,102,384!2026-02-26,102,384-->
      - COMP 3031 / exercise 1 / tree ADT / `add` ::@:: - Recursive: empty tree → new node. <br/> - On a node: compare target `t` with the node's element using `leq`; insert into left or right subtree accordingly; if equal, return unchanged to avoid duplicates. <!--SR:!2026-02-23,99,384!2026-02-27,103,384-->
      - COMP 3031 / exercise 1 / tree ADT / `toList` ::@:: - Accumulator version (linear time) – builds result in reverse order: `acc` for empty nodes and `rec(left, elem :: rec(right, acc))` for nonempty nodes, where `rec` is the accumulator helper function. <br/> - Naïve concatenation (`:::`) – quadratic but conceptually simple: `left.toList ::: elem :: right.toList`. <!--SR:!2026-02-22,98,384!2026-02-24,100,384-->
      - COMP 3031 / exercise 1 / tree ADT / `sortedList` ::@:: Build a BST by folding over the input list with `add`, then convert to list: `ls.foldLeft[Tree[T]](EmptyTree(leq))((t, e) => t.add(e)).toList` <!--SR:!2026-02-25,101,384!2026-02-20,97,384-->
      - COMP 3031 / exercise 1 / tree ADT / enumeration ::@:: When all behaviour is defined in a single place (no subclass methods), the tree can be expressed using Scala 3's `enum` syntax with pattern-matching inside each case. <!--SR:!2026-02-24,100,384!2026-02-21,97,384-->

## week 4 lecture

- datetime: 2025-09-23T12:00:00+08:00/2025-09-23T13:20:00+08:00, PT1H20M
- topic: proofs in Scala; list properties; structural induction; referential transparency; vector; collection hierarchy; Java sequences; range; sequence methods; mapping; map methods; option; varargs
- Scala
  - Scala / [proofs](proofs.md)
    - [§ list properties](proofs.md#list%20properties): concatenation, associativity of concatenation, neutral element of concatenation, structural induction
    - [§ structural induction](proofs.md#structural%20induction): natural induction, structural induction, structural induction on lists
    - [§ referential transparency](proofs.md#referential%20transparency): pure functions, referential transparency
    - [§ proofs](proofs.md#proofs): proving lower bounds on factorial, proving associativity of `:::`, proving `xs ::: Nil = xs`, proving reverse is its own inverse, proving `map` is distributive over concatenation
    - [§ proving lower bounds on factorial](proofs.md#proving%20lower%20bounds%20on%20factorial): proving lower bounds on factorial
    - [§ proving associativity of `:::`](proofs.md#proving%20associativity%20of%20`:::`): proving associativity of `:::`
    - [§ proving `xs ::: Nil = xs`](proofs.md#proving%20`xs%20Nil%20=%20xs`): proving `xs ::: Nil = xs`
    - [§ proving reverse is its own inverse](proofs.md#proving%20reverse%20is%20its%20own%20inverse): proving reverse is its own inverse
    - [§ proving `map` is distributive over concatenation](proofs.md#proving%20`map`%20is%20distributive%20over%20concatenation): proving `map` is distributive over concatenation
  - Scala / collections
    - [§ vector](collections.md#vector): vector, `+:`, `:+`
    - [§ hierarchy](collections.md#hierarchy): collection hierarchy, `Seq`, `Iterable`, `Array`, `String`, `Set`, `Map`
    - [§ Java sequences](collections.md#Java%20sequences): `Array`, `String`, implicit conversion to `Seq`
    - [§ range](collections.md#range): `Range`
    - [§ sequence methods](collections.md#sequence%20methods): sequence methods
    - [§ mapping](collections.md#mapping): `Map`, `Map` is iterable, `Map` is function, `Option`
  - Scala / Scala 3
    - [§ options](Scala%203.md#options): `Option`, pattern matching on `Option`
  - Scala / collections
    - [§ map update](collections.md#map%20update): `Map` update
    - [§ map methods](collections.md#map%20methods): `Map` methods, varargs
  - Scala / Scala 3
    - [§ varargs](Scala%203.md#varargs): varargs

## week 4 lecture 2

- datetime: 2025-09-25T12:00:00+08:00/2025-09-25T13:20:00+08:00, PT1H20M
- topic: `for` expression; set
- Scala
  - Scala / Scala 3
    - [§ for expressions](Scala%203.md#for%20expressions): `for` expression, `for` expression syntax, `for` generator, `for` filter
  - Scala / collections
    - [§ set](collections.md#set): `Set`
  - Scala / Scala 3
    - [§ for expression examples](Scala%203.md#for%20expression%20examples): `for` expression examples
    - [§ for expressions in other languages](Scala%203.md#for%20expressions%20in%20other%20languages): `for` expression in other languages, `for` expression in Python, `for` expression in Haskell, `for` expression in F\#

## week 5 lab

- datetime: 2025-09-29T15:00:00+08:00/2025-09-29T16:20:00+08:00, PT1H20M
- topic: higher-order functions; characteristic function
- COMP 3031
  - COMP 3031 / lab 2 ::@:: In this lab, sets of integers are modeled as _characteristic functions_: a value is in the set iff the function returns `true` for that integer. In code this is expressed with a type alias `type FunSet = Int => Boolean`, allowing any set to be represented by a simple predicate. <!--SR:!2026-02-23,99,384!2026-02-23,99,384-->
    - COMP 3031 / lab 2 / `contains` ::@:: A helper called `contains(s: FunSet, elem: Int): Boolean = s(elem)` lets us query membership without exposing the underlying function. <!--SR:!2026-02-12,90,384!2026-02-21,97,384-->
    - COMP 3031 / lab 2 / `singletonSet` ::@:: _Singleton construction_ (`singletonSet`) takes one integer and returns a set that contains exactly that element; implemented as `_ == elem`. <!--SR:!2026-02-22,98,384!2026-02-25,101,384-->
    - COMP 3031 / lab 2 / `union` ::@:: `union(s, t)` yields a set where an integer belongs if it is in either `s` or `t`: `x => contains(s, x) || contains(t, x)` <!--SR:!2026-02-24,100,384!2026-02-25,101,384-->
    - COMP 3031 / lab 2 / `intersect` ::@:: `intersect(s, t)` returns a set of integers belonging to both: `x => contains(s, x) && contains(t, x)` <!--SR:!2026-02-23,99,384!2026-02-27,103,384-->
    - COMP 3031 / lab 2 / `diff` ::@:: `diff(s, t)` produces the set of elements that are in `s` but not in `t`: `x => contains(s, x) && !contains(t, x)` <!--SR:!2026-02-26,102,384!2026-02-27,103,384-->
    - COMP 3031 / lab 2 / `filter` ::@:: The `filter` function selects those members of a given set that also satisfy an arbitrary predicate `p`. Its implementation is a simple logical conjunction: `x => contains(s, x) && p(x)`, returning a new characteristic function. <!--SR:!2026-02-26,102,384!2026-02-26,102,384-->
    - COMP 3031 / lab 2 / `forall` ::@:: Since we cannot enumerate all integers in a purely functional representation, the lab limits attention to the range `[-bound, bound]` (with `bound = 1000`). <p> The `forall(s, p)` routine checks whether every element of `s` satisfies predicate `p`. It uses a tail-recursive helper `iter(a)` that walks from `-bound` up to `bound`, stopping early if it finds an element in `s` that fails `p`. <!--SR:!2026-02-25,101,384!2026-02-27,103,384-->
    - COMP 3031 / lab 2 / `exists` ::@:: From this universal quantifier, the _existential_ test is derived simply by negation: `exists(s, p) = !forall(s, !p(_))`. <!--SR:!2026-02-22,98,384!2026-02-23,99,384-->
    - COMP 3031 / lab 2 / `map` ::@:: The `map` operation constructs a new set by applying a function `f` to each element of the original set. <p> Because we can only query membership via `contains`, the map is defined as: `x => exists(s, y => f(y) == x)`. For any candidate `x`, it checks whether there exists some `y` in the source set whose image under `f` equals `x`. <!--SR:!2026-02-12,90,384!2026-02-24,100,384-->
    - COMP 3031 / lab 2 / remarks ::@:: All functions can be expressed as one-liners; the challenge lies in reasoning about function composition rather than writing boilerplate. <p> Think of a set not as a collection but as a _predicate_ that tells whether a given integer is included. <!--SR:!2026-02-23,99,384!2026-02-23,99,384-->

## week 5 lecture

- datetime: 2025-09-30T12:00:00+08:00/2025-09-30T13:20:00+08:00, PT1H20M
- topic: case class; enumeration; collection; higher-order function; for expression; word coder; database query; desugaring for expressions; monad; generator monad
- Scala
  - Scala / Scala 3
    - [§ case classes](Scala%203.md#case%20classes): case classes, case classes syntax, case class examples
      - Scala 3 / § case classes / examples ::@:: JSON can be represented _concisely_ and _naturally_ using case classes. <!--SR:!2026-02-24,100,384!2026-02-22,98,384-->
    - [§ enumerations](Scala%203.md#enumerations): pure data structures, case classes, enumerations, simple enumerations, parameterized enumerations, pattern matching on enumerations
      - Scala 3 / § case classes / examples ::@:: JSON can be represented _concisely_ and _naturally_ using enumeration. <!--SR:!2026-02-26,102,384!2026-02-25,101,384-->
  - Scala / collections
    - [§ higher-order methods](collections.md#higher-order%20methods): higher-order methods, map, filter, reduce
  - Scala / Scala 3
    - [§ for expressions](Scala%203.md#for%20expressions): `for` expression, `for` expression syntax, `for` generator pattern matching
  - Scala / [applications](applications.md)
    - [§ word coder](applications.md#word%20coder): word coder
    - [§ `Coder`](applications.md#`Coder`): `Coder`, encapsulation
    - [§ `Coder.charCode`](applications.md#`Coder.charCode`): `Coder.charCode`, for expression
    - [§ `Coder.wordCode`](applications.md#`Coder.wordCode`): `Coder.wordCode`, higher-order function
    - [§ `Coder.wordsForNum`](applications.md#`Coder.wordsForNum`): `Coder.wordsForNum`, higher-order function, `Map`
    - [§ `Coder.encode`](applications.md#`Coder.encode`): `Coder.encode`, divide and conquer, for expression, recursion
    - [§ word coder usage](applications.md#word%20coder%20results): word coder usage
    - [§ word coder conclusion](applications.md#word%20coder%20conclusion): word coder conclusion, word coder in other languages
    - [§ database](applications.md#database): for expression, database, database query
    - [§ simple database queries](applications.md#simple%20database%20queries): simple database queries
    - [§ complex database queries](applications.md#complex%20database%20queries): complex database queries
  - Scala / Scala 3
    - [§ desugaring for expressions](Scala%203.md#desugaring%20for%20expressions): `for` expression, desugaring `for` expressions
  - Scala / [applications](applications.md)
    - [§ translating queries to higher-order functions](applications.md#translating%20queries%20to%20higher-order%20functions): translating queries to higher-order functions
  - Scala / Scala 3
    - [§ desugaring for expressions](Scala%203.md#desugaring%20for%20expressions): `for` expression, desugaring `for` expressions, `for` expression generalization
  - Scala / [monad](monad.md)
    - [§ motivation](monad.md#motivation): monad motivation
    - [§ generator](monad.md#generator): generator, `Generator`
    - [§ generator monad](monad.md#generator%20monad): generator monad, `Generator.map`, `Generator.flatMap`
    - [§ generator monad recursion](monad.md#generator%20monad%20recursion): generator monad recursion
    - [§ generator monad usage](monad.md#generator%20monad%20usage): generator monad usage

## week 5 lecture 2

- datetime: 2025-10-02T12:00:00+08:00/2025-10-02T13:20:00+08:00, PT1H20M
- topic: monad; option monad; exceptional monad; structural induction on trees
- [monad](../../../../general/monad%20(functional%20programming).md) ::@:: They are a way to structure computations as a sequence of steps, where each step not only produces a value but also some extra information about the computation, such as a potential failure, non-determinism, or side effect. <!--SR:!2026-02-24,100,384!2026-02-18,95,384-->
  - monad / formal definition ::@:: More formally, a monad is a type constructor M equipped with two operations, `return : <A>(a : A) -> M(A)` which lifts a value into the monadic context, and `bind : <A,B>(m_a : M(A), f : A -> M(B)) -> M(B)` which chains monadic computations. <!--SR:!2026-02-21,98,384!2026-02-25,101,384-->
- Scala
  - Scala / monad
    - [§ monad](monad.md#monad): monad
    - [§ definition](monad.md#definition): monad definition, monad in Scala
    - [§ examples](monad.md#examples): examples
    - [§ `map`](monad.md#`map`): monad `map`
    - [§ monad laws](monad.md#monad%20lwas): monad laws, monad associativity, monad left identity, monad right identity
    - [§ `Option`](monad.md#`Option`): `Option`, `Option` respects monad laws
    - [§ significance for `for`-expressions](monad.md#significance%20for%20`for`%20expressions): significance for `for`-expressions
  - Scala / Scala 3
    - [§ exceptions](Scala%203.md#exceptions): exceptions
    - [§ exception handling](Scala%203.md#exception%20handling): exception handling, `try`, `catch`
  - Scala / monad
    - [§ `Try`](monad.md#`Try`): exceptions, exceptional monad, `Try`, exceptional monad does not respect monad laws
  - Scala / proofs
    - [§ structural induction on trees](proofs.md#structural%20induction%20on%20trees): structural induction on trees
    - [§ set properties](proofs.md#set%20properties): set properties
    - [§ proving set properties](proofs.md#proving%20set%20properties): proving set properties
    - [§ proving set union property](proofs.md#proving%20set%20properties): proving set union property
- assignment: [assignment 1](assignments/assignment%201/index.md)

## week 6 lab

- datetime: 2025-10-06T15:00:00+08:00/2025-10-06T16:20:00+08:00, PT1H20M
- topic: pattern matching; for expression
- COMP 3031
  - COMP 3031 / exercise 2 ::@:: Deepen understanding of _pattern matching_ in Scala/functional style by tackling three concrete problems: triangle detection, symbolic differentiation, and expression simplification. <!--SR:!2026-04-14,129,407!2026-04-15,130,407-->
    - COMP 3031 / exercise 2 / detecting triangles ::@:: Return all unique directed cycles of length 3 with distinct nodes. Use a non-recursive `for` comprehension; assume each cycle appears only once. <!--SR:!2026-04-17,131,407!2026-04-10,125,407-->
      - COMP 3031 / exercise 2 / detecting triangles / definitions ::@:: - `type NodeId = Int` <br/> - `type DirectedEdge = (NodeId, NodeId)` <br/> - `type DirectedGraph = List[DirectedEdge]` <!--SR:!2026-04-11,126,407!2026-04-28,141,407-->
      - COMP 3031 / exercise 2 / detecting triangles / solution ::@:: Enforce an ordering rule on the vertices of the triangle to guarantee a canonical representation. You can chain three edge selections with guards, requiring 2 `<` comparisons. An alternative concise form use _case extractors_ and _references_ to previous values: ``case (`b`, c) <- edges if a < c``, ``case (`c`,`a`) <- edges`` etc. <!--SR:!2026-04-10,125,407!2026-04-12,127,407-->
    - COMP 3031 / exercise 2 / symbolic partial derivative ::@:: Symbolically find the partial derivative. Implement the function `deriv`. <!--SR:!2026-04-28,141,407!2026-04-12,127,407-->
      - COMP 3031 / exercise 2 / symbolic partial derivative / definitions ::@:: `enum Expr` with 4 case classes: <p> - `case Number(x: Int)` <br/> - `case Var(name: String)` <br/> - `case Sum(e1: Expr, e2: Expr)` <br/> - `case Prod(e1: Expr, e2: Expr)` <p> To avoid naming `Expr`, `import Expr.*` is used. <!--SR:!2026-04-09,124,407!2026-04-15,130,407-->
      - COMP 3031 / exercise 2 / symbolic partial derivative / solution ::@:: Pattern match on the expression tree according to the following rules: <p> - `Number(_)` → `Number(0)` (constant derivative) <br/> - `Var(name)` → `Number(1)` if `name == v`, else `Number(0)` <br/> - `Sum(l,r)` → `Sum(deriv(l,v), deriv(r,v))` (linearity) <br/> - `Prod(l,r)` → `Sum(Prod(deriv(l,v), r), Prod(l, deriv(r,v)))` \(product rule\) <!--SR:!2026-04-10,125,407!2026-04-19,133,407-->
    - COMP 3031 / exercise 2 / expression simplifier ::@:: Reduce algebraic expressions by applying arithmetic identities. Convert the derivative output into a more readable form (e.g. `Sum(Sum(Prod(Var("x"), Number(1)), Prod(Number(1), Var("x"))), Number(0))` is simplified to `Prod(Var("x"), Number(2))`). <!--SR:!2026-04-18,132,407!2026-04-20,134,407-->
      - COMP 3031 / exercise 2 / expression simplifier / solution ::@:: Recursively simplify sub-expressions, then apply pattern-based rewrites: <p> - `Sum(a,b)`: If both are numbers → add them. If one operand is `Number(0)` → return the other. If operands equal → collapse to `Prod(Number(2), x)`. <br/> - `Prod(a,b)`: Numeric multiplication if both numbers. Zero handling: any factor `0` → `Number(0)`. Identity handling: factor `1` removed. <br/> - Base cases (`Number`, `Var`) return unchanged. <!--SR:!2026-04-28,141,407!2026-04-15,130,407-->
      - COMP 3031 / exercise 2 / expression simplifier / limitations ::@:: Current rules miss deeper simplifications (e.g., nested sums or products). <p> Suggested improvement: Convert expression to a _normalized form_ such as a sum of product terms, each term being a list of factors. Then perform arithmetic on the normalized representation and reconstruct the final expression from it. <p> It is an open-ended problem, because there is no good definition of the "_most simplified_ form" of an arbitrary expression. <!--SR:!2026-04-28,141,407!2026-04-15,130,407-->

## week 6 lecture

- datetime: 2025-10-07T12:00:00+08:00/2025-10-07T13:20:00+08:00, PT1H20M
- status: unscheduled; public holiday: Mid-Autumn Festival

## week 6 lecture 2

- datetime: 2025-10-09T12:00:00+08:00/2025-10-09T13:20:00+08:00, PT1H20M
- topic: lazy evaluation; `LazyList`; infinite sequences; infinite sequence examples
- [lazy evaluation](../../../../general/lazy%20evaluation.md) ::@:: It is an evaluation strategy which delays the evaluation of an expression until its value is needed (non-strict evaluation) and which avoids repeated evaluations (by the use of sharing). <!--SR:!2026-04-20,134,407!2026-04-18,132,407-->
- Scala
  - Scala / [lazy evaluation](lazy%20evaluation.md)
    - [§ motivation](lazy%20evaluation.md#motivation): motivation for lazy evaluation
    - [§ lazy list](lazy%20evaluation.md#lazy%20list): `LazyList`
    - [§ lazy list properties](lazy%20evaluation.md#lazy%20list%20properties): laziness of `LazyList`, `LazyList.head`, `LazyList.tail`
    - [§ lazy list construction](lazy%20evaluation.md#lazy%20list%20construction): `LazyList.cons`, `LazyList.apply`, `LazyList.range`, laziness of `LazyList` construction
    - [§ lazy list operations](lazy%20evaluation.md#lazy%20list%20operations): `LazyList.filter`, laziness of `LazyList` operations, `#::`
    - [§ lazy evaluation](lazy%20evaluation.md#lazy%20evaluation): by-name parameters, `lazy val`
    - [§ lazy list implementation](lazy%20evaluation.md#lazy%20list%20implementation): `LazyList` implementations
    - [§ infinite sequences](lazy%20evaluation.md#infinite%20sequences): infinite sequences
    - [§ infinite sequence operations](lazy%20evaluation.md#infinite%20sequence%20operations): infinite sequence operations, divergence of infinite sequence operations
    - [§ infinite sequence examples](lazy%20evaluation.md#infinite%20sequence%20examples): sieve of Eratosthenes, lazy fixed iteration, water pouring problem
    - [§ lazy evaluation in other languages](lazy%20evaluation.md#lazy%20evaluation%20in%20other%20languages): lazy evaluation in Haskell, lazy evaluation in OCaml

## week 7 lab

- datetime: 2025-10-13T15:00:00+08:00/2025-10-13T16:20:00+08:00, PT1H20M
- topic: Huffman coding; Huffman tree
- [Huffman coding](../../../../general/Huffman%20coding.md) ::@:: It is a particular type of optimal prefix code that is commonly used for lossless data compression. <!--SR:!2026-04-20,134,407!2026-04-11,126,407-->
- COMP 3031
  - COMP 3031 / lab 3 ::@:: Implement Huffman coding using Scala. <!--SR:!2026-04-12,127,407!2026-04-28,141,407-->
    - COMP 3031 / lab 3 / Huffman coding ::@:: A lossless compression scheme that assigns variable-length bit strings to characters. Characters that occur more frequently receive shorter codes; rare ones get longer codes. <p> The optimality of a code depends on the match between the character frequencies in the text and the weights stored in the tree. <!--SR:!2026-04-09,124,407!2026-04-17,131,407-->
    - COMP 3031 / lab 3 / Huffman tree ::@:: Every Huffman code can be visualized as a binary tree whose leaves are the symbols to encode. A leaf node stores a character and its weight (frequency); an internal node stores the combined weight of all leaves beneath it. <p> The set of characters in any subtree is simply the union of the character sets of its child subtrees. <!--SR:!2026-04-28,141,407!2026-04-15,130,407-->
    - COMP 3031 / lab 3 / Huffman encoding ::@:: To encode a symbol, start at the root and traverse down to the leaf that contains that symbol. Append a `0` for each left branch taken, and a `1` for each right branch; the resulting bit list is the code for that character. <!--SR:!2026-04-11,126,407!2026-04-15,130,407-->
    - COMP 3031 / lab 3 / Huffman decoding ::@:: Begin at the root of the tree and read bits sequentially. A `0` moves to the left child; a `1` moves to the right child. Upon reaching a leaf, output its character and restart from the root for the next bit sequence. <!--SR:!2026-04-28,141,407!2026-04-28,141,407-->
    - COMP 3031 / lab 3 / Huffman data types ::@:: - __`CodeTree`__: `sealed abstract class CodeTree` <br/> - __`Fork`__: `case class Fork(left: CodeTree, right: CodeTree, chars: List[Char], weight: Int) extends CodeTree` <br/> &emsp; It contains the union of characters from both children and a combined weight. <br/> - __`Leaf`__: `case class Leaf(char: Char, weight: Int) extends CodeTree` <br/> &emsp; It holds a single character and its frequency. <!--SR:!2026-04-22,135,407!2026-04-28,141,407-->
      - COMP 3031 / lab 3 / Huffman data types / utilities ::@:: - `weight(tree)` – returns the total weight stored in a tree (pattern-matched on `Fork` or `Leaf`). <br/> - `chars(tree)` – yields the list of characters represented by a tree (again via pattern matching). <!--SR:!2026-04-28,141,407!2026-04-14,129,407-->
      - COMP 3031 / lab 3 / Huffman data types / construction ::@:: `makeCodeTree(left, right)` automatically builds a `Fork` node, concatenating character lists and summing weights. <!--SR:!2026-04-25,138,407!2026-04-14,129,407-->
    - COMP 3031 / lab 3 / Huffman tree construction ::@:: frequency counting → leaves → combine iteratively <p> `createCodeTree` – orchestrates the above steps: frequency counting → leaf list → iterative combining → return single tree. <!--SR:!2026-04-13,128,407!2026-04-13,128,407-->
      - COMP 3031 / lab 3 / Huffman tree construction / frequency counting ::@:: `times` – produce `List[(Char, Int)]` of character frequencies. Implemented either with a fold over the list or by using a mutable map for efficiency. <!--SR:!2026-04-28,141,407!2026-04-13,128,407-->
      - COMP 3031 / lab 3 / Huffman tree construction / leaves ::@:: `makeOrderedLeafList` – convert frequency pairs into sorted `Leaf` nodes (ascending weight). Uses an insertion routine that keeps the list ordered after each addition. <!--SR:!2026-04-28,141,407!2026-04-13,128,407-->
      - COMP 3031 / lab 3 / Huffman tree construction / singleton check ::@:: `singleton` – tests whether only one tree remains in a list. <!--SR:!2026-04-15,130,407!2026-04-28,141,407-->
      - COMP 3031 / lab 3 / Huffman tree construction / combine ::@:: `combine` – removes the first two elements of the list, merges them into a new `Fork`, and re-inserts it while preserving order. <!--SR:!2026-04-09,124,407!2026-04-09,124,407-->
      - COMP 3031 / lab 3 / Huffman tree construction / iterate ::@:: `until` – repeatedly applies `combine` until `singleton` returns true; the remaining tree is the optimal code tree. <!--SR:!2026-04-10,125,407!2026-04-14,129,407-->
    - COMP 3031 / lab 3 / Huffman decoding implementation ::@:: decode character → decode <!--SR:!2026-04-21,135,407!2026-04-28,141,407-->
      - COMP 3031 / lab 3 / Huffman decoding implementation / decode character ::@:: Recursive helper `decodeIt(subTree, bits)` traverses the tree based on current bit; when a leaf is reached it emits the character and restarts from the root. <!--SR:!2026-04-16,130,407!2026-04-12,127,407-->
      - COMP 3031 / lab 3 / Huffman decoding implementation / decode ::@:: The top-level `decode(tree, bits)` simply invokes this helper with the original tree as starting point. <!--SR:!2026-04-28,141,407!2026-04-15,130,407-->
    - COMP 3031 / lab 3 / Huffman encoding implementation ::@:: `encode(tree)(text)` traverses the tree for each character in `text` to accumulate its bit sequence. <p> An inner function `bitsOf(tree)(c)` performs the traversal: <p> - If the current node is a leaf matching `c`, it returns an empty list (all bits have been collected). <br/> - Otherwise, it recurses into the appropriate child (`left` if `c` belongs to that subtree, otherwise `right`) and prefixes the corresponding bit (`0` or `1`). <!--SR:!2026-04-21,135,407!2026-04-26,139,407-->
    - COMP 3031 / lab 3 / code table ::@:: It is a list of `(Char, List[Bit])` pairs of character and the corresponding bits to represent the character. <!--SR:!2026-04-18,132,407!2026-04-11,126,407-->
      - COMP 3031 / lab 3 / code table / conversion ::@:: `convert(tree)` walks the tree once to build this table, carrying along the current prefix of bits; it reverses the prefix at each leaf so that the resulting bit lists are in correct order. <!--SR:!2026-04-19,133,407!2026-04-16,130,407-->
      - COMP 3031 / lab 3 / code table / merge ::@:: `mergeCodeTables(a,b)` simply concatenates two tables (`a ::: b`). <!--SR:!2026-04-28,141,407!2026-03-04,93,387-->
      - COMP 3031 / lab 3 / code table / lookup ::@:: `codeBits(table)(char)` looks up a character's code in the table and returns its bit list; an error is thrown if the character isn't present. <!--SR:!2026-04-20,134,407!2026-04-28,141,407-->
      - COMP 3031 / lab 3 / code table / encode ::@:: `quickEncode(tree)(text)` first converts the tree into a table, then maps each character of `text` to its pre-computed bit list via `codeBits`, flattening the result. <!--SR:!2026-04-28,141,407!2026-04-14,129,407-->

## week 7 lecture

- datetime: 2025-10-14T12:00:00+08:00/2025-10-14T13:20:00+08:00, PT1H20M
- status: unscheduled; special leave for conference

## week 7 lecture 2

- datetime: 2025-10-16T12:00:00+08:00/2025-10-16T13:20:00+08:00, PT1H20M
- status: unscheduled; special leave for conference

## week 8 lab

- datetime: 2025-10-20T15:00:00+08:00/2025-10-20T16:20:00+08:00, PT1H20M
- topic: look-and-say sequence; lazy sequences
- [look-and-say sequence](../../../../general/look-and-say%20sequence.md) ::@:: It is the sequence of integers in which to generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. <!--SR:!2026-04-09,124,407!2026-04-23,136,407-->
- COMP 3031
  - COMP 3031 / exercise 3 ::@:: Deepen understanding of Scala's lazy collections by implementing and manipulating infinite streams—generating the look-and-say sequence, building lazy lists of arithmetic progressions, binary strings, and palindromes, and interleaving multiple streams—thereby reinforcing concepts of laziness, recursion, and functional stream composition. <!--SR:!2026-04-17,131,407!2026-04-12,127,407-->
    - COMP 3031 / exercise 3 / look-and-say sequence ::@:: - Identify the next term in the series that begins: <p> - `1` <br/> - `1 1` <br/> - `2 1` <br/> - `1 2 1 1` <br/> - `1 1 1 2 2 1` <br/> - `3 1 2 2 1 1` <br/> - ... <br/> - Encode each term as a `List[Int]` and write a function `nextLine(currentLine: List[Int]): List[Int]` that produces the succeeding list. <br/> - Construct an infinite lazy sequence (`LazyList[List[Int]]`) named `funSeq` that starts with `[1]` and repeatedly applies `nextLine` to generate all following terms, using `#::` (or `LazyList.cons`) to build the stream. <!--SR:!2026-04-21,135,407!2026-04-16,130,407-->
      - COMP 3031 / exercise 3 / look-and-say sequence / identification ::@:: Essentially, reading the sequence aloud yields the next sequence: <p> - `1` <br/> - `1 1` <br/> - `2 1` <br/> - `1 2 1 1` <br/> - `1 1 1 2 2 1` <br/> - `3 1 2 2 1 1` <br/> - `1 3 1 1 2 2 2 1` <br/> - ... <!--SR:!2026-03-07,96,387!2026-04-20,134,407-->
      - COMP 3031 / exercise 3 / look-and-say sequence / `nextLine` ::@:: Uses a left fold to accumulate runs of equal numbers and increment their counts. Reverse the sequence at the end. <p> _References_ may be used in pattern matching: ``case `x` :: count :: rest => ...``. <!--SR:!2026-04-15,130,407!2026-04-19,133,407-->
      - COMP 3031 / exercise 3 / look-and-say sequence / `funSeq` ::@:: Starts with `[1]` and recursively maps `nextLine` over itself to generate the infinite stream: <p> `lazy val funSeq: LazyList[List[Int]] = (1 :: Nil) #:: funSeq.map(nextLine)` <!--SR:!2026-04-28,141,407!2026-04-15,130,407-->
    - COMP 3031 / exercise 3 / lazy sequences ::@:: - Create a lazy list of squares for every integer ≥ 1. <br/> - Generate an infinite lazy list of _all non-empty binary strings_ built from the characters `"0"` and `"1"`, where each string appears eventually in the stream (order is irrelevant). <br/> - From that string stream, produce a lazy list containing only the palindromic strings (strings equal to their reverse). <br/> - Show an alternative construction of the palindrome stream _without_ using `filter`. <br/> - Given another potentially finite or infinite lazy list called `otherCodes`, interleave it with the palindrome stream to form a new stream `allCodes`. <!--SR:!2026-04-11,126,407!2026-04-21,135,407-->
      - COMP 3031 / exercise 3 / lazy sequences / `squares` ::@:: Builds on `LazyList.from(1)` and applies a simple squaring transformation: <p> `val squares: LazyList[Int] = LazyList.from(1).map(x => x * x)` <!--SR:!2026-04-21,135,407!2026-04-10,125,407-->
      - COMP 3031 / exercise 3 / lazy sequences / `palCodes` ::@:: Retains only those binary strings that read the same forwards and backwards.: <p> `val palCodes: LazyList[String] = codes.filter(x => x.reverse == x)` <!--SR:!2026-04-27,140,407!2026-04-21,135,407-->
        - COMP 3031 / exercise 3 / lazy sequences / `palCodes` / for-comprehension ::@:: Constructs each palindrome explicitly by sandwiching a middle segment (`""`, `"0"`, or `"1"`) between a string and its reverse: <p> `val palCodes = "0" #:: "1" #:: (for (c <- codes; middle  <- "" :: "0" :: "1" :: Nil) yield c + middle + c.reverse)` <!--SR:!2026-04-28,141,407!2026-04-19,133,407-->
      - COMP 3031 / exercise 3 / lazy sequences / interleaving ::@:: Alternates elements from `xs` and `ys`; if one list is exhausted it appends the remainder of the other: <p> Pattern match on both `xs` and `ys` using a tuple: `(xs, ys)`. Then split cases as: `case (x #:: xr, y #:: yr)`, `case (LazyList(), ys)`, `case (xs, LazyList())`. <p> Usage: `interleave(palCodes, otherCodes)`: Merges the palindrome stream with an external source of codes to produce a single lazy list containing both kinds of strings in alternating order. <!--SR:!2026-04-11,126,407!2026-04-12,127,407-->

## week 8 lecture

- datetime: 2025-10-21T12:00:00+08:00/2025-10-21T13:20:00+08:00, PT1H20M
- status: unscheduled; special leave for conference

## week 8 lecture 2

- datetime: 2025-10-23T12:00:00+08:00/2025-10-23T13:20:00+08:00, PT1H20M
- topic: contextual abstraction; `using`; `given`; context inference; type class; conditional `given`; recursive `given` resolution; type class extension; type class in other languages
- [monkey patch](../../../../general/monkey%20patch.md) ::@:: It is the act of dynamically modifying the runtime code (not the source code) of a dynamic programming language, and it is the information (data/code) used to modify the runtime code. <!--SR:!2026-04-18,132,407!2026-04-15,130,407-->
- [dependency injection](../../../../general/dependency%20injection.md) ::@:: It is a programming technique in which an object or function receives other objects or functions that it requires, as opposed to creating them internally. <!--SR:!2026-04-13,128,407!2026-04-17,131,407-->
- Scala
  - Scala / [context](context.md)
    - [§ motivation](context.md#motivation): context motivation
    - [§ higher-order functions](context.md#higher-order%20functions): context motivation using higher-order functions
    - [§ `using`](context.md#`using`): `using`, explicitly provide `using`, implicitly infer `using`
    - [§ `using` syntax](context.md#`using`%20syntax): `using` in method, `using` in method call, `using` multiple parameters, `using` in multiple parameter lists, anonymous `using` clauses
    - [§ context bound](context.md#context%20bound): context bound
    - [§ `given`](context.md#`given`): `given`, `given` instance, anonymous `given` instance
    - [§ `summon`](context.md#`summon`): `summon`
    - [§ importing `given`s](context.md#importing%20`given`s): import `given`s by name, import `given`s by type, import `given`s by wildcard
    - [§ context inference](context.md#context%20inference): context inference
    - [§ type class](context.md#type%20class): type class
    - [§ type class pattern](context.md#type%20class%20pattern): type class pattern
    - [§ retroactive extension](context.md#retroactive%20extension): retroactive extension
    - [§ conditional `given`](context.md#conditional%20`given`): conditional `given`
    - [§ recursive `given` resolution](context.md#recursive%20`given`%20resolution): recursive `given` resolution
    - [§ extension methods](context.md#extension%20methods): extension methods
    - [§ type class in other languages](context.md#type%20class%20in%20other%20languages): type class in other languages, type class in Haskell, type class in Rust

## week 9 lab

- datetime: 2025-10-27T15:00:00+08:00/2025-10-27T16:20:00+08:00, PT1H20M
- topic: anagram; word anagram; sentence anagram; recursion
- [anagram](../../../../general/anagram.md) ::@:: It is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
- COMP 3031
  - COMP 3031 / lab 4 ::@:: Compute sentence anagrams in Scala using occurrence lists, dictionary lookups, subset generation, subtraction, and recursion. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / problem ::@:: An anagram rearranges letters to form new meaningful words. Extend from word anagrams to sentence anagrams by ignoring case and punctuation and using a provided dictionary. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / representation ::@:: - `type Word = String` <br/> - `type Sentence = List[Word]` <br/> - `type Occurrences = List[(Char, Int)]` &emsp; Sorted by character (ascending), lowercase-only, positive, counts. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / dictionary ::@:: `val dictionary: List[Word] = loadDictionary` &emsp; Preloaded list of meaningful words used to validate anagrams. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / `wordOccurrences` ::@:: Produce `(Char, Int)` pairs from a word, case-insensitive, sorted by character. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / `sentenceOccurrences` ::@:: Concatenate words in a sentence and reuse `wordOccurrences`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / index ::@:: Group the dictionary by occurrences for efficient lookup; words sharing the same occurrence list are anagrams. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / combinations ::@:: Generate all subsets of an occurrence list, varying counts from `0..freq` for each char and combining recursively. <p> The empty list has exactly one subset: itself (`List(Nil)`). <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / `subtractOccurrences` ::@:: Remove counts of one occurrence list `y` from another `x`; assume `y` is a subset of `x`. Drop zero-count entries and keep result sorted. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 4 / sentence anagrams ::@:: Recursively pick any valid word from subsets of the sentence's occurrence list; subtract its occurrences and continue until empty. Base case returns `List(Nil)`. <p> 1. Compute `allOccurrences = sentenceOccurrences(sentence)`. <br/> 2. For each `combination` in `combinations(allOccurrences)`: For each `possibleWord` in `dictionaryByOccurrences(combination)`, recurse on `subtract(allOccurrences, combination)` to get `otherWords`, and then prepend `possibleWord` to each `otherWords`. <br/> 3. Collect all sentences produced; the empty sentence maps to `List(Nil)`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->

## week 9 lecture

- datetime: 2025-10-28T12:00:00+08:00/2025-10-28T13:20:00+08:00, PT1H20M
- status: unscheduled; midterm examination
- [§ midterm examination](#midterm%20examination)

---

> __<big><big>Midterm exam scheduled on 28 Oct 2025 (Tue) 12:00-14:00 in Rm 4621</big></big>__
>
> Dear all,
>
> The midterm exam will take place as follows
>
> Date:  28 Oct 2025 <br/>
> Time:  12pm to 2pm <br/>
> Venue: room 4621
>
> If you have any concerns about this arrangement, please let us know ASAP.
>
> A few important pieces of information:
>
> 1. The exam will be open book. Naturally, no electronic devices will be permitted. You will be able to bring and use only printed hardcopies from this course (and not from any other course) as well as your own notes.
> 2. __Please arrive _at least_ 5min before the start of the exam. That is, arrive at Room 4621 no later than 11:55am.__
> 3. The midterm exam will cover all material up to and including Lecture 11.
> 4. I have posted some exam preparation material on Canvas, in the "Midterm preparation" module. Be sure to try and solve the exercises on your own before looking at the solutions!
>
> Best regards,
>
> — \[redacted\]

## midterm examination

- datetime: 2025‑10‑28T12:00:00+08:00/2025‑10‑28T14:00:00+08:00, PT2H  
- venue: Room 4621, Academic Building
- format  
  - calculator: no  
  - cheatsheet: yes (unlimited)
  - referencing: closed books, closed notes
  - provided: (none)
  - questions: long question ×4 (with subquestions)
- grades: 40/40 → 40/30 → 30/30+10/10
  - statistics
    - timestamps: 2025-11-03T14:46+08:00 → 2025-11-04T18:16+08:00 → 2025-12-22T12:23+08:00
    - count: 65 → 65 → 65
    - mean: 19.28 (provided: 19.08203125) → 19.28 → 18.81
    - standard deviation: ? → ? → ?
    - low: 2.5 (provided: 2.5) → 2.5 → 2.5
    - lower quartile: 11 (provided: 11) → 11 → 11.75
    - median: 20 (provided: 19.5) → 20 → 20
    - upper quartile: 25.5 (provided: 25.5) → 25.5 → 26
    - high: 40 (provided: 40) → 40 → 30
    - graph: [`Screenshot_2025-11-03_at_14.53.26.png`](attachments/Screenshot_2025-11-03_at_14.53.26.png) → ? → ?
    - data: ? → ? → ?
  - breakdown
    - question 1: 1 → 1 → 1  
    - question 2: 3 → 3 → 3  
    - question 3: 3 → 3 → 3  
    - question 4: 3 → 3 → 3  
    - question 5: 5 → 5 → 5  
    - question 6: 7 → 7 → 7  
    - question 7: 3 → 3 → 3  
    - question 8: 2 → 2 → 2  
    - question 9: 2 → 2 → 2  
    - question 10: 1 → 1 → 1  
    - question 11: 2 → 2 → 2  
    - question 12: 2 → 2 → 2  
    - question 13: 4 → 4 → 4  
    - question 14: 2 → 2 → 2  
- report: (none)
- check
  - datetime: 2025-11-03T15:00:00+08:00/2025-11-03T16:20:00+08:00, PT1H20M
  - venue: Room 4214 (Lift 19), Academic Building
  - report: (none)

---

> __<big><big>Midterm exam scheduled on 28 Oct 2025 (Tue) 12:00-14:00 in Rm 4621</big></big>__
>
> Dear all,
>
> The midterm exam will take place as follows
>
> Date:  28 Oct 2025 <br/>
> Time:  12pm to 2pm <br/>
> Venue: room 4621
>
> If you have any concerns about this arrangement, please let us know ASAP.
>
> A few important pieces of information:
>
> 1. The exam will be open book. Naturally, no electronic devices will be permitted. You will be able to bring and use only printed hardcopies from this course (and not from any other course) as well as your own notes.
> 2. __Please arrive _at least_ 5min before the start of the exam. That is, arrive at Room 4621 no later than 11:55am.__
> 3. The midterm exam will cover all material up to and including Lecture 11.
> 4. I have posted some exam preparation material on Canvas, in the "Midterm preparation" module. Be sure to try and solve the exercises on your own before looking at the solutions!
>
> Best regards,
>
> — \[redacted\]

---

> __<big><big>Midterm exam marking scheme adjustment</big></big>__
>
> Dear students,
>
> After discussing with many of you and reflecting on it, the TAs and I now realize that the mid-term exam was in fact harder than previous years. A particular example was Exercise 2 which, while not fundamentally difficult, did not follow the typical pattern seen in previous midterms. We realize that there was not enough time to properly think through that exercise, given that the other two exercises were already quite challenging.
>
> Therefore, we have decided to retro-actively declare Exercise 2 optional, meaning that the total marks of the exam should actually be 30 instead of 40, and that any points gotten in Exercise 2 will be considered bonus points. This will increase the average grade from 50% to 60%, bringing it close to the average from previous years. And for the few students who then have total points over 30, these points will be carried over (not clamped). This way, no one is penalized, and the unintended extra difficulty of the midterm exam is corrected for.
>
> Do note that our goal is to make most people pass with good grades, as long as you demonstrably acquire the required knowledge. We try to design the assessments so as to maximize the grade distribution in the end, to the extent allowable by the university. In other words, we will make sure to make the final exam less challenging. Still, if you would like to withdraw for the course, I have no objection to it.
>
> Best regards,
>
> — \[redacted\]

## week 9 lecture 2

- datetime: 2025-10-30T12:00:00+08:00/2025-10-30T13:20:00+08:00, PT1H20M
- topic: monoid; kind; type function; monad; context management; execution context; opaque type alias
- Scala
  - Scala / [context](context.md)
    - [§ monoid example](context.md#monoid%20example)
  - Scala / [kind](kind.md)
    - [§ type functions](kind.md#type%20functions)
    - [§ monad example](kind.md#monad%20example)
    - [§ monad example motivation](kind.md#monad%20example%20motivation)
    - [§ monad related kinds](kind.md#monad%20related%20kinds)
    - [§ other languages](kind.md#other%20languages)
  - Scala / [context](context.md)
    - [§ context management](context.md#context%20management)
    - [§ execution contexts](context.md#execution%20contexts)
    - [§ opaque type aliases for safety](context.md#opaque%20type%20aliases%20for%20safety)

## week 10 lab

- datetime: 2025-11-03T15:00:00+08:00/2025-11-03T16:20:00+08:00, PT1H20M
- topic: midterm examination; midterm examination paper checking
- [§ midterm examination](#midterm%20examination)

## week 10 lecture

- datetime: 2025-11-04T12:00:00+08:00/2025-11-04T13:20:00+08:00, PT1H20M
- topic: state; substitution model; statefulness; `var`; operational equivalence; loops; digital circuit example
- Scala
  - Scala / [state](state.md)
    - [§ substitution model](state.md#substitution%20model)
    - [§ statefulness](state.md#statefulness)
    - [§ `var`](state.md#`var`)
    - [§ operational equivalence](state.md#operational%20equivalence)
  - Scala / [imperative programming](imperative%20programming.md)
    - [§ loops](imperative%20programming.md#loops)
    - [§ repeat loops](imperative%20programming.md#repeat%20loops)
    - [§ for-loops](imperative%20programming.md#for-loops)
    - [§ digital circuit example](imperative%20programming.md#digital%20circuit%20example)
    - [§ circuit description language](imperative%20programming.md#circuit%20description%20language)
    - [§ simulation engine](imperative%20programming.md#simulation%20engine)

## week 10 lecture 2

- datetime: 2025-11-06T12:00:00+08:00/2025-11-06T13:20:00+08:00, PT1H20M
- topic: observer pattern; reactive programming; functional reactive programming; signal; signal dependency tracking; context passing example; implicit function type
- Scala
  - Scala / [reactive programming](reactive%20programming.md)
    - [§ observer pattern](reactive%20programming.md#observer%20pattern)
    - [§ observer pattern example](reactive%20programming.md#observer%20pattern%20example)
    - [§ shortcomings of the observer pattern](reactive%20programming.md#shortcomings%20of%20the%20observer%20pattern)
    - [§ functional reactive programming](reactive%20programming.md#functional%20reactive%20programming)
    - [§ signals](reactive%20programming.md#signals)
    - [§ signal example](reactive%20programming.md#signal%20example)
    - [§ signal reassignment](reactive%20programming.md#signal%20reassignment)
    - [§ signal implementation](reactive%20programming.md#signal%20implementation)
    - [§ dependency tracking](reactive%20programming.md#dependency%20tracking)
  - Scala / [context](context.md)
    - [§ implicit function types](context.md#implicit%20function%20types)
- assignment: [assignment 2](assignments/assignment%202/index.md)

## week 11 lab

- datetime: 2025-11-10T15:00:00+08:00/2025-11-10T16:20:00+08:00, PT1H20M
- topic: abstract syntax tree
- [abstract syntax tree](../../../../general/abstract%20syntax%20tree.md) (AST) ::@:: It is a data structure used in computer science to represent the structure of a program or code snippet. It is a tree representation of the abstract syntactic structure of text (often source code) written in a formal language. Each node of the tree denotes a construct occurring in the text. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
- COMP 3031
  - COMP 3031 / exercise 4 ::@:: Implement GCD, List primitives (`map`, `foldLeft`), and memory CAS in a small expression language using the given `Expr` AST. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / `Expr` ::@:: Core syntax for expressions and binary ops. <p> - __`Expr`__: `Constant`, `Name`, `BinOp`, `IfNonzero`, `Call`, `Fun` <br/> - __`Expr`__ (lists): `Cons`, `EmptyList`, `Match` <br/> - __`Expr`__ (memory): `Read`, `Write` <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / `BinOp` instances ::@:: Shorthands for binary ops. <p> - `minus(e1, e2) = BinOp(Minus, e1, e2)` <br/> - `plus(e1, e2) = BinOp(Plus, e1, e2)` <br/> - `leq(e1, e2) = BinOp(LessEq, e1, e2)` &emsp; (returns `1` if `e1 <= e2`, else `0`) <br/> - `times(e1, e2) = BinOp(Times, e1, e2)` <br/> - `modulo(e1, e2) = BinOp(Modulo, e1, e2)` <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / global environment ::@:: A sequence of `(String, Expr)` bindings; each definition can reference any name in the environment (mutually recursive bindings supported). Example: `div` defined via recursion using `LessEq` and subtraction. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / implement `gcd` ::@:: Implement Euclid’s algorithm: if `b == 0` then `a` else `gcd(b, a % b)`. <p> Encode recursion using `Fun` + `Call`; condition uses `IfNonzero(Name("b"), ...)` with `modulo`. <p> Curried calls: `Call(Call(Name("gcd"), arg1), arg2)`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / implement `map` ::@:: Apply `f` to each element; rebuild list. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / implement `foldLeft` ::@:: Accumulate left-to-right using a binary function `f`. <p> Functions are curried; compute `f(acc, x)` as `Call(Call(Name("f"), acc), x)`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / exercise 4 / implement `cas` ::@:: Compare-and-swap returns `1` on success (write performed) or `0` if the current value differs from `old`. <p> In `Expr`: use `Read` to fetch, `Write` to store and then continue with `andThen`. `IfNonzero(minus(Read(idx), old), ...)` effectively tests `mem(idx) != old`. `Write(idx, nw, Constant(1))` performs the write, then evaluates to `1`. <p> In this toy language, execution is sequential; real CAS is atomic in concurrent settings. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->

## week 11 lecture

- datetime: 2025-11-11T12:00:00+08:00/2025-11-11T13:20:00+08:00, PT1H20M
- topic: Lisp; Scheme; Lisp program; Lisp data; interpreter; tokenizer; parser; Lisp syntax; Lisp syntactic sugar
- Scala
  - Scala / [Lisp](Lisp.md)
    - [§ Lisp](Lisp.md#Lisp)
    - [§ Lisp programs](Lisp.md#Lisp%20programs)
    - [§ Lisp data](Lisp.md#Lisp%20data)
    - [§ interpreter](Lisp.md#interpreter)
    - [§ internal representation](Lisp.md#internal%20representation)
    - [§ tokenizer](Lisp.md#tokenizer)
    - [§ parser](Lisp.md#parser)
    - [§ syntax](Lisp.md#syntax)
    - [§ syntactic sugar](Lisp.md#syntactic%20sugar)
    - [§ characteristics](Lisp.md#characteristics)
  
## week 11 lecture 2

- datetime: 2025-11-13T12:00:00+08:00/2025-11-13T13:20:00+08:00, PT1H20M
- topic: evaluator; environment; closure; dynamic scoping; lexical scoping; Lisp recursion
- Scala
  - Scala / [Lisp](Lisp.md)
    - [§ evaluator](Lisp.md#evaluator)
    - [§ environment](Lisp.md#environment)
    - [§ predefined bindings](Lisp.md#predefined%20bindings)
    - [§ evaluation rules](Lisp.md#evaluation%20rules)
    - [§ closure](Lisp.md#closure)
    - [§ scoping](Lisp.md#scoping)
    - [§ recursion](Lisp.md#recursion)
    - [§ global environment](Lisp.md#global%20environment)
    - [§ usage](Lisp.md#usage)
    - [§ extensions](Lisp.md#extensions)

## week 12 lab

- datetime: 2025-11-17T15:00:00+08:00/2025-11-17T16:20:00+08:00, PT1H20M
- topic: Bloxorz; lazy evaluation; `LazyList`
- COMP 3031
  - COMP 3031 / lab 5 ::@:: Solve a simplified Bloxorz puzzle in Scala using lazy evaluation and breadth‑first search (BFS) to find the shortest move sequence. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / problem ::@:: In a Bloxorz puzzle, explore a state space of block positions on a terrain; generate legal neighbors by rolling the block; search for a shortest path from start to goal using lazy streams (`LazyList`). <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / setup ::@:: The logic is split across `GameDef.scala` (positions, terrain, block, moves) and `Solver.scala` (lazy BFS over block states). <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `Pos` ::@:: `case class Pos(row: Int, y: Int)` where `row` increases downward (vertical axis) and `y` increases rightward (horizontal axis). <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `Terrain` ::@:: The board (walkable cells) is a function: `type Terrain = Pos => Boolean` &emsp; `true` means inside terrain; `false` means out of bounds. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `terrainFunction(levelVector)` ::@:: Return a function that checks whether a position is within any non-`-` cell. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `findChar(c, levelVector)` ::@:: Locate the coordinates of a specific character (e.g., `S` for start, `T` for goal) <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `Block` ::@:: A 2×1×1 cuboid represented by two positions: `case class Block(b1: Pos, b2: Pos)`. <p> It is _standing_ when `b1 == b2`. It is _legal_ when `terrain(b1) && terrain(b2)`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / `Move` ::@:: `left`, `right`, `up`, `down` roll the block, yielding new `Block`s with updated `(b1, b2)` according to orientation. The four possible moves recorded as case objects. <p> - `neighbors: List[(Block, Move)]`: Returns `(blockAfterMove, move)` for all four directions. <br/> - `legalNeighbors: List[(Block, Move)]`: Filter `neighbors` to those with `block.isLegal`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / solver ::@:: Search in breadth-first order using `LazyList[(Block, List[Move])]`, where the move history is stored with the most recent move at the head of the list. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / goal test ::@:: `done(b: Block)` returns `true` if the block is standing on the goal position `T`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / `neighborsWithHistory`, `newNeighborsOnly` ::@:: `neighborsWithHistory` extends from a node `(block, history)` to all legal neighbors, prepending the move to `history`. <p> `newNeighborsOnly` filters away already explored blocks to avoid cycles. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / `from` ::@:: Build layers of paths lazily, always expanding the current frontier before moving to the next. This ensures breadth-first traversal, so the first time you reach the goal, the path is shortest. <p> 1. If `initial` is empty, return empty `LazyList`. <br/> 2. Otherwise, compute `next` by: `neighborsWithHistory` for each `(b, hist)` in `initial`; `newNeighborsOnly(next, explored)` to remove revisits. <br/> 3. Return `initial #::: from(next, explored ++ next.map(_._1).toSet)`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / `pathsFromStart` ::@:: Start from the initial block with empty history: `from(LazyList((startBlock, Nil)), Set(startBlock))` <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / `pathsToGoal` ::@::  Filter all paths in `pathsFromStart` whose block satisfies `done`. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
      - COMP 3031 / lab 5 / solver / `solution` ::@:: Extract the move list from the first path in `pathsToGoal` to the goal and reverse it so that the head is the first move to play. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / laziness ::@:: `LazyList` ensures you only compute as much of the search frontier as needed; BFS guarantees the first goal path discovered is shortest. Avoid recomputation by tracking `explored` blocks; only expand fresh neighbors. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
    - COMP 3031 / lab 5 / summary ::@:: Parse terrain → define block & moves → generate legal neighbors → lazy BFS (`from`) with cycle avoidance → filter goal paths → reverse history for final `solution`. <p> This pattern generalizes to other shortest‑path problems on implicit graphs. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->

## week 12 lecture

- datetime: 2025-11-18T12:00:00+08:00/2025-11-18T13:20:00+08:00, PT1H20M
- topic: logic programming; Prolog; Prolog basics; deductive information retrieval; Prolog implementation; unification; complexity of unification
- Scala
  - Scala / [logic programming](logic%20programming.md)
    - [§ Prolog](logic%20programming.md#Prolog)
    - [§ Prolog basics](logic%20programming.md#Prolog%20basics)
    - [§ deductive information retrieval](logic%20programming.md#deductive%20information%20retrieval)
    - [§ negation as failure](logic%20programming.md#negation%20as%20failure)
    - [§ recursion](logic%20programming.md#recursion)
    - [§ representation](logic%20programming.md#representation)
    - [§ asymmetric unification](logic%20programming.md#asymmetric%20unification)
    - [§ unification](logic%20programming.md#unification)
    - [§ complexity of unification](logic%20programming.md#complexity%20of%20unification)

## week 12 lecture 2

- datetime: 2025-11-20T12:00:00+08:00/2025-11-20T13:20:00+08:00, PT1H20M
- topic: backtracking; Prolog implementation; formal reasoning; soundness; completeness; problems with negation
- Scala
  - Scala / [logic programming](logic%20programming.md)
    - [§ backtracking](logic%20programming.md#backtracking)
    - [§ backtracking implementation](logic%20programming.md#backtracking%20implementation)
    - [§ implementation](logic%20programming.md#implementation)
    - [§ formal reasoning](logic%20programming.md#formatl%20reasoning)
    - [§ soundness](logic%20programming.md#soundness)
    - [§ completeness](logic%20programming.md#completeness)
    - [§ problems with negation](logic%20programming.md#problems%20with%20negation)

## week 13 lab

- datetime: 2025-11-24T15:00:00+08:00/2025-11-24T16:20:00+08:00, PT1H20M
- topic: final examination preparation
- [§ final examination](logic%20programming.md#final%20examination)

## week 13 lecture

- datetime: 2025-11-25T12:00:00+08:00/2025-11-25T13:20:00+08:00, PT1H20M
- topic: asynchronous programming; continuation-passing style; callback; direct style; future; `Future`; promise; `Promise`; transformation on futures; dataflow programming; future execution
- Scala
  - Scala / [futures and promises](futures%20and%20promises.md)
    - [§ motivation](futures%20and%20promises.md#motivation)
    - [§ continuation-passing style](futures%20and%20promises.md#continuation-passing%20style)
    - [§ drawbacks of CPS](futures%20and%20promises.md#drawbacks%20of%20CPS)
    - [§ CPS to direct style](futures%20and%20promises.md#CPS%20to%20direct%20style)
    - [§ future](futures%20and%20promises.md#future)
    - [§ promise](futures%20and%20promises.md#promise)
    - [§ transformations](futures%20and%20promises.md#transformations)
    - [§ for-comprehensions](futures%20and%20promises.md#for-comprehensions)
    - [§ dataflow programming](futures%20and%20promises.md#dataflow%20programming)
    - [§ execution context](futures%20and%20promises.md#execution%20context)
    - [§ API mitigation](futures%20and%20promises.md#API%20mitigation)

## week 13 lecture 2

- datetime: 2025-11-27T12:00:00+08:00/2025-11-27T13:20:00+08:00, PT1H20M
- topic: synchronization; actor model; actor; actor state; actor lifecycle; message passing; message processing; actor application
- Scala
  - Scala / [actor model](actor%20model.md)
    - [§ motivation](actor%20model.md#motivation)
    - [§ actor vs. thread](actor%20model.md#actor%20vs.%20thread)
    - [§ avoiding synchronization](actor%20model.md#avoiding%20synchronization)
    - [§ history](actor%20model.md#history)
    - [§ actor](actor%20model.md#actor)
    - [§ actor creation](actor%20model.md#actor%20creation)
    - [§ message passing](actor%20model.md#message%20processing)
    - [§ actor state](actor%20model.md#actor%20state)
    - [§ actor lifecycle](actor%20model.md#actor%20lifecycle)
    - [§ entry point](actor%20model.md#entry%20point)
    - [§ actor encapsulation](actor%20model.md#actor%20encapsulation)
    - [§ message processing](actor%20model.md#message%20processing)
    - [§ bank account example](actor%20model.md#bank%20account%20example)
    - [§ message delivery](actor%20model.md#message%20delivery)
    - [§ web client example](actor%20model.md#web%20client%20example)
    - [§ actor application](actor%20model.md#actor%20application)
- assignment: [assignment 3](assignments/assignment%203/index.md)

## final examination

- datetime: 2025‑12-15T08:30:00+08:00/2025‑12-15T10:30:00+08:00, PT2H  
- venue: Lecture Theater L, CYT Building
- format
  - calculator: no  
  - cheatsheet: yes (unlimited)
  - referencing: closed books, closed notes
  - provided: (none)
  - questions: long question ×3 (with subquestions)
- grades: 40/40+5/5 → 40/40+5/5
  - statistics
    - timestamps: 2025-12-19T14:46+08:00 → 2025-12-22T12:23+08:00
    - count: 65 → 65
    - mean: 21.93 → 21.93
    - standard deviation: ? → ?
    - low: 5 → 5
    - lower quartile: 13.13 → 13.13
    - median: 22 → 22
    - upper quartile: 28.88 → 28.88
    - high: 40 → 40
    - graph: ? → ?
    - data: ? → ?
  - breakdown
    - question 1: 2 → 2
    - question 2: 1 → 1
    - question 2 bonus: 1 → 1
    - question 3: 6 → 6
    - question 3 bonus: 3 → 3
    - question 4: 3 → 3
    - question 5: 2 → 2
    - question 6: 2 → 2
    - question 7: 2 → 2
    - question 8: 3 → 3
    - question 9: 3 → 3
    - question 10: 3 → 3
    - question 10 bonus: 1 → 1
    - question 11: 4 → 4
    - question 12: 1 → 1
    - question 13: 5 → 5
    - question 14: 3 → 3
- report
  - lateness due to traffic jam (0) ::@:: Due to a big traffic jam, was 20 minutes late; which was fine in the end. <!--SR:!2025-12-26,5,396!2025-12-26,5,396-->
- check
  - datetime: 2025‑12-22T09:30:00+08:00/2025‑12‑22T11:30:00+08:00, PT2H  
  - venue: Room 3523, Academic Building
  - report: (none)

---

> __<big><big>Final exam paper checking session</big></big>__
>
> Dear all,
>
> The final exam papers have been graded and the grades have been posted on Canvas. The paper checking session will take place on Monday, December 22, 2025 between 9:30am and 11:30am in Rm 3523. You can check the exam solutions on Canvas.
>
> Best, <br/>
> \[redacted\]

## aftermath

### total

- grades: 100/100+15/15
  - statistics: ?
