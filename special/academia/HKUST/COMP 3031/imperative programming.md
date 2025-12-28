---
aliases:
  - COMP 3031 Scala imperative programming
  - COMP3031 Scala imperative programming
  - HKUST COMP 3031 Scala imperative programming
  - HKUST COMP3031 Scala imperative programming
  - Scala imperative programming
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/imperative_programming
  - language/in/English
---

# Scala imperative programming

- HKUST COMP 3031

---

- see: [general/imperative programming](../../../../general/imperative%20programming.md)

Scala lets programmers write code that {@{looks like traditional _imperative_ languages}@} while still {@{benefiting from the safety and abstraction mechanisms of a modern language}@}. The core ideas are simple: {@{variables, mutable state, loops and control flow}@} can be expressed {@{directly in the language}@} or modelled with {@{higher‑order functions}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## loops

{@{Imperative programs}@} rely on {@{loops for repeated computation}@}. In Scala, {@{the built‑in `while` loop}@} is written as <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __Scala `while` loop__
>
> In Scala, {@{the built‑in `while` loop}@} is written as
>
> ```Scala
> def power(x: Double, exp: Int): Double =
>   var r = 1.0
>   var i = exp
>   while i > 0 do { r = r * x; i = i - 1 }
>   r
> ```
>
> In Scala, {@{every expression}@} evaluates {@{to a value}@}. For {@{a `while` loop}@}, it always evaluates to {@{the `Unit` value `()`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The `while` loop}@} can be implemented as {@{a function that receives the condition and the body, both by name}@}, so they are {@{re‑evaluated each iteration}@}. This function is {@{tail‑recursive and uses constant stack space}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`whileDo` implementation__
>
> {@{The `while` loop}@} can be implemented as {@{a function that receives the condition and the body, both by name}@}, so they are {@{re‑evaluated each iteration}@}. This function is {@{tail‑recursive and uses constant stack space}@}.
>
> ```Scala
> def whileDo(cond: => Boolean)(body: => Unit): Unit =
>   if cond then { body; whileDo(cond)(body) } else ()
> ```
>
> {@{The `cond` and `body` arguments}@} are {@{_by‑name_ parameters}@}, allowing {@{the loop to re‑evaluate them each time}@}. It returns {@{the `Unit` value `()`}@} when {@{the loop ends}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### repeat loops

{@{The `repeatUntil` command}@} runs {@{at least once}@} and stops when {@{the condition becomes true}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`repeatUntil` function__
>
> {@{The `repeatUntil` command}@} runs {@{at least once}@} and stops when {@{the condition becomes true}@}.
>
> ```Scala
> def repeatUntil(body: => Unit)(cond: => Boolean): Unit =
>   body; if !cond then repeatUntil(body)(cond) else ()
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A repeat–until pattern}@} can also be expressed with {@{a pair of functions that form a fluent API}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`repeat`/`until` syntax__
>
> {@{A repeat–until pattern}@} can also be expressed with {@{a pair of functions that form a fluent API}@}:
>
> ```Scala
> def repeat(body: => Unit) = Repeat(body)
> class Repeat(body: => Unit):
>   infix def until(cond: => Boolean): Unit =
>     body; if !cond then until(cond)
> ```
>
> ... which may be {@{used as follows}@}:
>
> ```Scala
> repeat { /* ... */ } until cond
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### for-loops

Scala offers a {@{concise `for` syntax}@} that is essentially {@{syntactic sugar for calls to `foreach`}@}. {@{A Java‑style loop with an index variable}@} can be written as <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __Scala for‑loop with range__
>
> Scala offers a {@{concise `for` syntax}@} that is essentially {@{syntactic sugar for calls to `foreach`}@}. {@{A Java‑style loop with an index variable}@} can be written as
>
> ```Scala
> for i <- 1 until 3 do println(i)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The translation of nested Java-style loops}@} is also {@{straightforward using nested `for`}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __nested for‑loops translation__
>
> {@{The translation of nested Java-style loops}@} is also {@{straightforward using nested `for`}@}:
>
> ```Scala
> for i <- 1 until 3; j <- "abc" do println(s"$i $j")
> // ... same as...
> (1 until 3).foreach { i =>
>   "abc".foreach(j => println(s"$i $j")) }
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

## digital circuit example

Scala can be used to {@{build a simple digital‑circuit simulator}@} that demonstrates how {@{mutable state and higher‑order functions interact in a discrete‑event setting}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

### circuit description language

{@{A circuit}@} is built from {@{_wires_ carrying Boolean signals and _components_ that transform those signals}@}. {@{The basic gates—an inverter, an AND gate and an OR gate}@}—are the {@{building blocks for more complex structures such as half‑adders or full‑adders}@}. Each component has {@{a fixed delay}@}; its output is updated only {@{after that amount of simulated time}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __basic gates__
>
> {@{The implementation of a gate}@} registers {@{an action on its input wires}@}; when {@{the inputs change}@}, the action schedules {@{an update to the output after the component’s delay}@}.
>
> ```Scala
> def inverter(in: Wire, out: Wire): Unit = ...
> def andGate(a: Wire, b: Wire, out: Wire): Unit = ...
> def orGate(a: Wire, b: Wire, out: Wire): Unit = ...
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Wires}@} are {@{first‑class values}@}. They expose {@{three operations: `getSignal`, `setSignal` and `addAction`}@}. `{@{`getSignal` and setSignal}@} respectively {@{gets and sets the wire's current state}@}. `{@{addAction`}@} adds an action to {@{run whenever the wire state changes}@}. {@{A function}@} can assemble {@{gates into larger components}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __half‑adder construction__
>
> {@{A function}@} can assemble {@{gates into larger components}@}:
>
> ```Scala
> def halfAdder(a: Wire, b: Wire, s: Wire, c: Wire): Unit =
>   val d = Wire(); val e = Wire()
>   orGate(a,b,d); andGate(a,b,c)
>   inverter(c,e); andGate(d,e,s)
> ```
>
> {@{The same pattern is reused}@} to build {@{a full adder}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### simulation engine

{@{The simulation}@} is driven by {@{an agenda of delayed actions}@}. {@{The abstract `Simulation` trait}@} supplies {@{the core API}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __simulation trait skeleton__
>
> {@{The simulation}@} is driven by {@{an agenda of delayed actions}@}. {@{The abstract `Simulation` trait}@} supplies {@{the core API}@}:
>
> ```Scala
> trait Simulation {
>   type Action = () => Unit
>   def currentTime: Int
>   def afterDelay(d: Int)(block: => Unit): Unit
>   def run(): Unit
> }
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{An `afterDelay` call}@} inserts {@{an event into a sorted list}@}; {@{the `run` method}@} repeatedly executes {@{the earliest event until the agenda is empty}@}. {@{Wires react to signal changes}@} by executing {@{all attached actions}@}, which may in turn schedule {@{further events}@}, thereby producing {@{the discrete‑event dynamics of the circuit}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The simulator}@} also offers {@{_probes_}@} that print {@{a wire’s value whenever it changes}@}, making it easy to {@{observe a circuit’s behaviour}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __circuit probe__
>
> {@{The simulator}@} also offers {@{_probes_}@} that print {@{a wire’s value whenever it changes}@}, making it easy to {@{observe a circuit’s behaviour}@}.
>
> ```Scala
> def probe(name: String, wire: Wire): Unit =
>   def probeAction(): Unit =
>     println(s”$name $currentTime value = ${wire.getSignal()}”)
>   wire.addAction(probeAction)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

By composing {@{gates and probes}@} one can experiment with {@{more elaborate circuits, such as a full adder or a ripple‑carry adder}@}, while keeping {@{the simulation time model explicit}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->
