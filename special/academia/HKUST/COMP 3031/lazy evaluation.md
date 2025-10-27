---
aliases:
  - COMP 3031 Scala lazy evaluation
  - COMP 3031 Scala lazy evaluations
  - COMP3031 Scala lazy evaluation
  - COMP3031 Scala lazy evaluations
  - HKUST COMP 3031 Scala lazy evaluation
  - HKUST COMP 3031 Scala lazy evaluations
  - HKUST COMP3031 Scala lazy evaluation
  - HKUST COMP3031 Scala lazy evaluations
  - Scala lazy evaluation
  - Scala lazy evaluations
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/lazy_evaluations
  - language/in/English
---

# Scala lazy evaluation

- HKUST COMP 3031

## motivation

In {@{many search problems}@} one only needs {@{a small fragment of a potentially huge or infinite space}@}.  {@{Lazy evaluation}@} enable {@{algorithms such as breadth‑first search or prime generation}@} to generate {@{successors on demand}@} without {@{allocating the entire search tree}@}.  This leads to {@{substantial savings in both time and memory}@}, as illustrated by {@{the prime example below}@}: {@{only the first few numbers are inspected}@} until {@{the second prime is found}@}.

## lazy list

In Scala {@{a _lazy list_}@} ({@{`scala.collection.immutable.LazyList`}@}, formerly {@{`Stream`}@}) is {@{an immutable, potentially infinite sequence}@} whose elements are {@{evaluated only when they are required}@}. The concept was introduced to support {@{combinatorial search and other problems}@} where constructing {@{the entire collection would be wasteful or impossible}@}.

### lazy list properties

{@{A lazy list}@} behaves like {@{a normal Scala `Seq`}@} with respect to {@{most operations}@}: {@{mapping, filtering, folding, etc.}@}  However, {@{all of these operations}@} are {@{_lazy_}@} – they produce {@{new lazy lists whose tails are computed only on demand}@}.  Because {@{the tail is not evaluated}@} until {@{it is accessed}@} (via {@{`head`, `tail`, or an operation that forces evaluation}@}), a lazy list can represent {@{infinite sequences}@} such as {@{the natural numbers or prime numbers}@} without ever allocating {@{more than the required portion of the sequence}@}.

{@{A lazy list}@} is defined by {@{two core fields}@}: {@{`LazyList.head` and `LazyList.tail`}@}.

- `LazyList.head` ::@:: The first element, which may be computed lazily.
- `LazyList.tail` ::@:: A _by‑name_ parameter that represents the rest of the list; it is evaluated only when needed and its result is memoised so that subsequent accesses reuse the same value.

{@{The standard implementation}@} in Scala keeps {@{a lazy `state` field}@} that holds either {@{an empty state or a cons cell with head and tail}@}.  {@{This state}@} is computed {@{on first access, cached, and never recomputed}@}.

### lazy list construction

{@{Lazy lists}@} can be {@{built explicitly}@} using {@{`LazyList.cons`}@}, in which {@{both parameters are by‑name \(lazy\)}@}:

> [!example] __`LazyList.cons`__
>
> {@{Lazy lists}@} can be {@{built explicitly}@} using {@{`LazyList.cons`}@}, in which {@{both parameters are by‑name \(lazy\)}@}:
>
> ```Scala
> val xs = LazyList.cons(1, LazyList.cons(2, LazyList.empty))
> ```

or {@{more conveniently}@} via {@{the factory syntax}@}, in which {@{parameters are by-value \(eager\)}@}:

> [!example] __`LazyList.apply`__
>
> or {@{more conveniently}@} via {@{the factory syntax}@}, in which {@{parameters are by-value \(eager\)}@}:
>
> ```Scala
> val ys = LazyList(1, 2, 3)
> ```

{@{The operator corresponding to `::` for `LazyList`}@} is {@{the `#::` operator}@}, which prepends {@{a head element to a tail}@} that is {@{itself a lazy list}@}:

> [!example] __`#::`__
>
> {@{The operator corresponding to `::` for `LazyList`}@} is {@{the `#::` operator}@}, which prepends {@{a head element to a tail}@} that is {@{itself a lazy list}@}:
>
> ```Scala
> val xs1 = ??? #:: LazyList.empty          // a single‑element list (head unspecified)
> val xs2 = 1 #:: (??? : LazyList[Int])     // head is 1, tail unspecified
> ```

{@{The companion object}@} also offers {@{a range constructor}@} that is {@{lazy by default}@}:

> [!example] __`LazyList.range`__
>
> {@{The companion object}@} also offers {@{a range constructor}@} that is {@{lazy by default}@}:
>
> ```Scala
> LazyList.range(1000, 10000)   // equivalent to (1000 until 10000).to(LazyList)
> ```

{@{A hand‑rolled recursive function}@} illustrates {@{the laziness}@}:

> [!example] __lazy construction__
>
> {@{A hand‑rolled recursive function}@} illustrates {@{the laziness}@}:
>
> ```Scala
> def lazyRange(lo: Int, hi: Int): LazyList[Int] =
>   if (lo >= hi) LazyList.empty
>   else LazyList.cons(lo, lazyRange(lo + 1, hi))  // the second argument is evaluated when needed
> def listRange(lo: Int, hi: Int): List[Int] =
>   if lo >= hi then Nil
>   else lo :: listRange(lo + 1, hi)
> ```
>
> Unlike {@{the similar `listRange`}@} that {@{returns a strict `List`}@}, {@{the recursive call in `lazyRange`}@} is wrapped {@{in a by‑name parameter}@} and therefore {@{not evaluated}@} until {@{the tail of the resulting list is needed}@}.

Unlike {@{the similar `listRange`}@} that {@{returns a strict `List`}@}, {@{the recursive call in `lazyRange`}@} is wrapped {@{in a by‑name parameter}@} and therefore {@{not evaluated}@} until {@{the tail of the resulting list is needed}@}.

### lazy list operations

{@{Most standard collection methods}@} are {@{available on lazy lists}@}.  For example, to find {@{the second prime number}@} between {@{1000 and 10&nbsp;000}@} one can write:

> [!example] __lazily finding prime numbers__
>
> {@{Most standard collection methods}@} are {@{available on lazy lists}@}.  For example, to find {@{the second prime number}@} between {@{1000 and 10&nbsp;000}@} one can write:
>
> ```Scala
> LazyList.range(1000, 10000).filter(isPrime)(1)
> ```
>
> Here {@{`filter`}@} is {@{lazily evaluated}@}; when {@{the second element is accessed}@}, it {@{filters until the second element is found}@}. Because {@{only the necessary portion of the list}@} is evaluated, this code does not build {@{a full list of all primes in that interval}@}.

Here {@{`filter`}@} is {@{lazily evaluated}@}; when {@{the second element is accessed}@}, it {@{filters until the second element is found}@}. Because {@{only the necessary portion of the list}@} is evaluated, this code does not build {@{a full list of all primes in that interval}@}.

{@{Most `LazyList` operations}@} are implemented by mirroring {@{the corresponding `List` methods}@} but deferring {@{all recursive calls to the tail}@} so that they are {@{performed only when that part of the sequence is required}@}.  For instance, {@{a strict `List.filter(p)`}@} builds {@{a new list in one pass}@}: it examines {@{every element}@} and appends {@{those satisfying `p`}@}, forcing {@{evaluation of the entire input list}@}.  In contrast, {@{`LazyList.filter(p)`}@} constructs {@{a lazy cons cell}@} whose head is {@{the first matching element}@} and whose tail is {@{itself a lazily‑filtered sublist}@}:

> [!example] __`LazyList.filter`__
>
> {@{The above simplified `LazyList`}@} was {@{only lazy in its tail}@}, leaving {@{`head` and `isEmpty` strict}@}; {@{the production‑grade implementation}@} fixes this by making {@{every part of the list lazily evaluated}@}.  It does so by storing {@{a single `state` field}@} that is {@{computed on first use}@}:
>
> ```Scala
> def filter(p: A => Boolean): LazyList[A] =
>   if (isEmpty) this
>   else if (p(head)) LazyList.cons(head, tail.filter(p))
>   else tail.filter(p)
> ```
>
> Because {@{the recursive call `tail.filter(p)`}@} is wrapped in {@{a by‑name parameter and memoised}@}, only {@{as many elements as needed are examined}@}—e.g., retrieving {@{the first prime from a huge range}@} requires evaluating {@{just enough of the list to find that prime}@}, leaving {@{the rest unevaluated}@}.

Because {@{the recursive call `tail.filter(p)`}@} is wrapped in {@{a by‑name parameter and memoised}@}, only {@{as many elements as needed are examined}@}—e.g., retrieving {@{the first prime from a huge range}@} requires evaluating {@{just enough of the list to find that prime}@}, leaving {@{the rest unevaluated}@}.

{@{A noteworthy exception}@} is {@{the cons operator `::`}@}.  When used with {@{a lazy list}@}, {@{`x :: xs`}@} always {@{produces a strict `List`, not a lazy one}@}. Scala provides {@{`#::` as an alternative}@} that {@{preserves laziness}@}:

> [!example] __`#::` preserves laziness__
>
> Scala provides {@{`#::` as an alternative}@} that {@{preserves laziness}@}:
>
> ```Scala
> val lazyX = LazyList.cons(1, LazyList.empty)
> val lazyY = 2 #:: lazyX   // still a LazyList
> ```

### lazy list implementation

{@{A `LazyList` implementation}@} the list is defined by {@{a trait that exposes three members}@}—{@{`isEmpty`, `head`, and `tail`}@}.  {@{The companion object}@} supplies {@{a constructor `cons(hd, tl)`}@} where {@{the tail argument is passed _by‑name_ (`=> TailLazyList[T]`)}@}.  Because this parameter is {@{evaluated each time `tail` is accessed}@}, {@{repeated calls to `tail`}@} will {@{recompute the entire sublist from scratch}@}.  For instance:

> [!example] __naive `LazyList` implementation__
>
> {@{A `LazyList` implementation}@} the list is defined by {@{a trait that exposes three members}@}—{@{`isEmpty`, `head`, and `tail`}@}.  {@{The companion object}@} supplies {@{a constructor `cons(hd, tl)`}@} where {@{the tail argument is passed _by‑name_ (`=> TailLazyList[T]`)}@}.  Because this parameter is {@{evaluated each time `tail` is accessed}@}, {@{repeated calls to `tail`}@} will {@{recompute the entire sublist from scratch}@}.  For instance:
>
> ```Scala
> object TailLazyList {
>   def cons[T](hd: T, tl: => TailLazyList[T]) =
>     new TailLazyList[T] {          // tail is a by‑name parameter
>       def isEmpty = false
>       def head   = hd
>       def tail   = tl              // recomputed on every access
>     }
>   val empty = ???                  // omitted
> }
> ```

Using {@{this naive construction}@}, {@{`lazyRange(1, 10).take(3)`}@} would trigger {@{the creation of `tail` three times}@}—once for {@{each element taken}@}—leading to {@{unnecessary work and potential performance degradation}@}. This issue is resolved by {@{memoising the first evaluation of the tail}@} so that {@{subsequent calls reuse the stored result}@}—{@{an optimisation justified in pure functional languages}@} where {@{expressions are deterministic}@}. This approach exemplifies {@{_lazy evaluation_}@} (as opposed to {@{plain _by‑name_ evaluation}@}, which {@{recomputes on every call}@}, or {@{strict evaluation}@} used for {@{ordinary parameters and `val`s}@}).

{@{The above simplified `LazyList`}@} was {@{only lazy in its tail}@}, leaving {@{`head` and `isEmpty` strict}@}; {@{the production‑grade implementation}@} fixes this by making {@{every part of the list lazily evaluated}@}.  It does so by storing {@{a single `state` field}@} that is {@{computed on first use}@}:

> [!example] __`LazyList.state`__
>
> {@{The above simplified `LazyList`}@} was {@{only lazy in its tail}@}, leaving {@{`head` and `isEmpty` strict}@}; {@{the production‑grade implementation}@} fixes this by making {@{every part of the list lazily evaluated}@}.  It does so by storing {@{a single `state` field}@} that is {@{computed on first use}@}:
>
> ```Scala
> class LazyList[+T](init: => State[T]) {
>   lazy val state: State[T] = init          // evaluated once, then cached
> }
> ```
>
> where `State` is {@{an enum of either `Empty` or `Cons(hd, tl)`}@}; {@{the latter's tail (`tl`)}@} is {@{a fully lazy `LazyList`}@}.

where `State` is {@{an enum of either `Empty` or `Cons(hd, tl)`}@}; {@{the latter's tail (`tl`)}@} is {@{a fully lazy `LazyList`}@}. In {@{Scala 3's standard library}@} this pattern appears as {@{a private `lazyState` function}@} that yields {@{a `State[A]` object containing `head` and `tail`}@}; thus {@{the list's structure (whether it's empty or a cons cell)}@} is {@{computed lazily}@}, but {@{individual `head` elements themselves}@} are {@{not lazy}@}—only {@{the overall shape of the sequence}@} is {@{deferred}@}.

## lazy evaluation

Scala is {@{strict by default}@}. Compare to {@{Haskell}@}, which performs {@{lazy evaluation by default}@}. Scala offers {@{several mechanisms for deferring computation}@}: \(annotation: 2 items: {@{by-name parameters, `lazy val`}@}\)

- __By‑name parameters__ (`=> T`) ::@:: – used in `LazyList.cons` to delay evaluation of the tail.
- __`lazy val`__ ::@:: – a value that is evaluated at most once, on first use.

For {@{an example}@} of {@{`lazy val`}@}:

> [!example] __`lazy val`__
>
> For {@{an example}@} of {@{`lazy val`}@}:
>
> ```Scala
> val x = { println("x"); 1 }          // strict; prints immediately
> lazy val y = { println("y"); 2 }     // lazy; prints only when `y` is used
> def z() = { println("z"); 3 }        // function, evaluated each call
> ```
>
> When evaluating {@{an expression that mixes these constructs}@}, {@{the side‑effects occur}@} in the order {@{the values are first required}@}.

When evaluating {@{an expression that mixes these constructs}@}, {@{the side‑effects occur}@} in the order {@{the values are first required}@}.

## infinite sequences

Because {@{the tail of a lazy list}@} is {@{lazily evaluated}@}, it can {@{represent sequences having infinite elements}@}:

> [!example] __`LazyList` of all natural numbers__
>
> Because {@{the tail of a lazy list}@} is {@{lazily evaluated}@}, it can {@{represent sequences having infinite elements}@}:
>
> ```Scala
> def from(n: Int): LazyList[Int] = n #:: from(n + 1)
> val nats   = from(0)                    // all natural numbers
> ```

### infinite sequence operations

{@{Other infinite sequences}@} may be obtained by {@{mapping or filtering an infinite sequence}@}. For example, {@{the list of multiples of four}@} is expressed as:

> [!example] __deriving infinite sequences__
>
> {@{Other infinite sequences}@} may be obtained by {@{mapping or filtering an infinite sequence}@}. For example, {@{the list of multiples of four}@} is expressed as:
>
> ```Scala
> nats.map(_ * 4)
> ```
>
> or
>
> ```Scala
> nats.filter(_ % 4 == 0)
> ```
>
> {@{Both approaches}@} generate {@{each element on demand}@}; however, {@{the `map` version}@} typically {@{produces values faster}@} because it {@{evaluates less elements and avoids the extra filtering step}@}.

{@{Both approaches}@} generate {@{each element on demand}@}; however, {@{the `map` version}@} typically {@{produces values faster}@} because it {@{evaluates less elements and avoids the extra filtering step}@}.

{@{Many standard operations}@} {@{terminate only}@} when they {@{encounter a finite amount of data}@}:

Evaluating {@{`nats.size` or `nats.toList`}@} requires {@{evaluating all elements}@}, which is {@{infinite}@}, so it {@{diverges–never terminates}@}. Compare to {@{`nats.drop(1).take(10).toList`}@}, which {@{converges, i.e. terminates, and returns `List(1, 2, ..., 10)`}@}. Therefore, only {@{operations that request a finite prefix of the list}@} {@{terminate}@}.

### infinite sequence examples

{@{The classic algorithm}@} for {@{generating primes}@} can be expressed {@{succinctly with lazy lists}@}:

> [!example] __sieve of Eratosthenes__
>
> {@{The classic algorithm}@} for {@{generating primes}@} can be expressed {@{succinctly with lazy lists}@}:
>
> ```Scala
> def sieve(s: LazyList[Int]): LazyList[Int] =
>   s.head #:: sieve(s.tail.filter(_ % s.head != 0))
>
> val primes = sieve(from(2))
> ```
>
> {@{`primes.take(N).toList`}@} yields {@{the first `N` prime numbers}@}. {@{Each step of the sieve}@} removes {@{multiples of the current head}@}, and because {@{the list is lazy}@}, only {@{as many sieves \(primes\) as needed}@} are {@{used to eliminate composites}@}.

{@{`primes.take(N).toList`}@} yields {@{the first `N` prime numbers}@}. {@{Each step of the sieve}@} removes {@{multiples of the current head}@}, and because {@{the list is lazy}@}, only {@{as many sieves \(primes\) as needed}@} are {@{used to eliminate composites}@}.

{@{Lazy lists}@} can also model {@{mathematical convergent sequences}@} without {@{explicit termination conditions}@}:

> [!example] __lazy fixed iteration__
>
> {@{Lazy lists}@} can also model {@{mathematical convergent sequences}@} without {@{explicit termination conditions}@}:
>
> ```Scala
> def sqrtSeq(x: Double): LazyList[Double] = {
>   def improve(guess: Double) = (guess + x / guess) / 2
>   lazy val guesses: LazyList[Double] = 1 #:: guesses.map(improve)
>   guesses
> }
> ```

{@{A predicate}@} can then {@{filter for a sufficiently accurate approximation}@}:

> [!example] __lazy fixed iteration extraction__
>
> {@{A predicate}@} can then {@{filter for a sufficiently accurate approximation}@}:
>
> ```Scala
> def isGoodEnough(guess: Double, x: Double): Boolean =
>   ((guess * guess - x) / x).abs < 0.0001
>
> sqrtSeq(2).filter(isGoodEnough(_, 2))
> ```
>
> {@{The first element that satisfies `isGoodEnough`}@} is {@{the desired square root}@}.

{@{The first element that satisfies `isGoodEnough`}@} is {@{the desired square root}@}.

{@{A combinatorial search problem}@}, such as {@{filling glasses to a target volume}@}, can be encoded with {@{lazy lists of state transitions}@}:

> [!example] __water pouring problem__
>
> {@{A combinatorial search problem}@}, such as {@{filling glasses to a target volume}@}, can be encoded with {@{lazy lists of state transitions}@}:
>
> ```Scala
> type Glass = Int
> type State = Vector[Int]
>
> enum Move:
>   case Empty(glass: Glass)
>   case Fill(glass: Glass)
>   case Pour(from: Glass, to: Glass)
>
> class Pouring(capacity: Vector[Int]):
>   extension(move: Move)
>     def change(prev: State): State =
>       move match
>         case Move.Empty(g) => prev.updated(g, 0)
>         case Move.Fill(g)  => prev.updated(g, capacity(g))
>         case Move.Pour(f, t) =>
>           val amount = math.min(prev(f), capacity(t) - prev(t))
>           prev.updated(f, prev(f) - amount).updated(t, prev(t) + amount)
>   // more ...
> ```
>

Under {@{the class `Pouring`}@}, {@{all glasses and possible moves}@} are {@{generated}@}:

> [!example] __water pouring problem encoding__
>
> Under {@{the class `Pouring`}@}, {@{all glasses and possible moves}@} are {@{generated}@}:
>
> ```Scala
> val glasses: List[Glass] = (0 until capacity.length).toList // all glasses
> val actions: List[Move] = // all possible moves
>   ( for glass <- glasses yield Empty(glass) ) ++
>   ( for glass <- glasses yield Fill(glass) ) ++
>   ( for from <- glasses; to <- glasses if from != to yield Pour(from, to) )
> ```

{@{The search space}@} of {@{the water pouring problem}@} is {@{explored lazily}@}:

> [!example] __water pouring problem search__
>
> {@{The search space}@} of {@{the water pouring problem}@} is {@{explored lazily}@}:
>
> ```Scala
> class Path(history: List[Move], val endState: State):
>   def extend(action: Move) =
>     Path(action :: history, action.change(endState))
>
> def from(current: Set[Path], explored: Set[State]): LazyList[Set[Path]] =
>   if current.isEmpty then LazyList.empty
>   else {
>     val more: Set[Path] =
>       for
>         start <- current
>         next  <- actions.map(start.extend)
>         if !explored.contains(next.endState)
>       yield next
>     current #:: from(more, explored ++ more.map(_.endState))
>   }
> ```

{@{A sequence of solution paths}@} is obtained by {@{filtering paths that reach the target amount}@}:

> [!example] __water pouring problem solution__
>
> {@{A sequence of solution paths}@} is obtained by {@{filtering paths that reach the target amount}@}:
>
> ```Scala
> val initialState = capacity.map(_ => 0)
> val initialPath = Path(Nil, initialState)
> lazy val pathSets = from(Set(initialPath), Set(initialState))
>
> def solutions(target: Int): LazyList[Path] =
>   for
>     paths <- pathSets
>     p     <- paths if p.endState.contains(target)
>   yield p
> ```

## lazy evaluation in other languages

In {@{many functional languages}@}, {@{laziness}@} is {@{built into the core language}@} rather than {@{added as a library feature}@}.

{@{Haskell}@} exemplifies {@{this approach}@}: {@{its list type}@} is {@{inherently lazy}@}, so values are {@{computed only when they are needed}@}. {@{A classic illustration}@} is {@{an infinite stream of guesses for a square root}@} defined with {@{the cons operator `:`}@}:

> [!example] __Haskell lazy evaluation example__
>
> {@{A classic illustration}@} is {@{an infinite stream of guesses for a square root}@} defined with {@{the cons operator `:`}@}:
>
> ```Haskell
> let guesses = 1 : map improve guesses
> ```
>
> Here {@{each new element}@} is produced by applying {@{`improve` to the previous one}@}, and {@{no evaluation occurs}@} until {@{a particular element is demanded}@}.

Here {@{each new element}@} is produced by applying {@{`improve` to the previous one}@}, and {@{no evaluation occurs}@} until {@{a particular element is demanded}@}.

{@{OCaml}@} takes {@{a different stance}@}. By default it {@{evaluates eagerly}@}, but it still permits {@{cyclic data structures}@} through {@{recursive definitions}@}:

> [!example] __OCaml cyclic data structure example__
>
> {@{OCaml}@} takes {@{a different stance}@}. By default it {@{evaluates eagerly}@}, but it still permits {@{cyclic data structures}@} through {@{recursive definitions}@}:
>
> ```Ocaml
> let rec alternate = 0 :: 1 :: alternate
> ```

However, to obtain {@{true laziness in OCaml}@} one must explicitly {@{wrap the deferred parts in functions}@}—known as {@{thunks}@}—using {@{the `Stream` module}@}. {@{An example of a lazy list of guesses in OCaml}@} would be:

> [!example] __OCaml lazy evaluation example__
>
> However, to obtain {@{true laziness in OCaml}@} one must explicitly {@{wrap the deferred parts in functions}@}—known as {@{thunks}@}—using {@{the `Stream` module}@}. {@{An example of a lazy list of guesses in OCaml}@} would be:
>
> ```Ocaml
> let rec guesses = Stream.cons (fun () -> (1, Stream.map improve guesses))
> ```

Thus, while Haskell relies on {@{implicit laziness for all lists}@}, OCaml requires {@{explicit constructs to defer computation}@}. {@{Scala's `LazyList`}@} is {@{similar in spirit to Haskell lists}@} but requires {@{explicit construction like OCaml}@}.
