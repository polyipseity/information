---
aliases:
  - COMP 3031 Scala logic programming
  - COMP3031 Scala logic programming
  - HKUST COMP 3031 Scala logic programming
  - HKUST COMP3031 Scala logic programming
  - Scala logic programming
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/logic_programming
  - language/in/English
---

# Scala logic programming

- HKUST COMP 3031

---

- see: [general/logic programming](../../../../general/logic%20programming.md)

__Logic programming__ treats computation as deduction from logical facts and rules.  Rather than supplying a concrete sequence of operations, the programmer writes declarative statements that describe _what_ is true; a Prolog‑style interpreter then searches for solutions that satisfy those statements.

Typical programs are expressed as collections of clauses.  A clause can be read as “if the conditions on its left hand side hold, then the conclusions on its right hand side follow.”  The interpreter explores alternatives by backtracking, trying different substitutions until a goal is satisfied or all possibilities are exhausted.  Unification is the core operation that matches patterns and binds variables consistently.

## Prolog

Prolog is the canonical language for this paradigm.  Its syntax is minimal: a program consists of facts and rules written as predicates.  A predicate can be called with arguments; if any argument starts with an uppercase letter it denotes a variable, otherwise it is a constant.  The following clause demonstrates list concatenation, where `[...|...]` is the cons operator for lists:

> [!example] __Prolog append rules__
>
> Its syntax is minimal: a program consists of facts and rules written as predicates.  A predicate can be called with arguments; if any argument starts with an uppercase letter it denotes a variable, otherwise it is a constant.  The following clause demonstrates list concatenation, where `[...|...]` is the cons operator for lists:
>
> ```prolog
> append([], Ys, Ys).                                // `[] + Ys == Ys`
> append([X|Xs], Ys, [X|Zs]) :- append(Xs, Ys, Zs).  // `Xs + Ys == Zs => X::Xs + Ys == X::Zs`
> ```
>
> A query such as `?- append([1,2], [3,4], X).` yields `X = [1,2,3,4]`.

The same logic can be expressed in Scala using pattern matching:

> [!example] __Scala append__
>
> The same logic can be expressed in Scala using pattern matching:
>
> ```scala
> def append[A](xs: List[A], ys: List[A]): List[A] =
>   xs match {
>     case Nil      => ys
>     case x :: xs1 => x :: append(xs1, ys)
>   }
> ```
>
> The two Scala clauses correspond to the Prolog rules above.

### Prolog basics

In Prolog every identifier is either a constant or a variable; variables start with an uppercase letter (e.g., `X`, `Ys`).  
Lists use the cons notation `[Head|Tail]`; the empty list is written `[]`.  A clause consists of a head and, optionally, a body separated by `:-`.  The body may contain several goals that are _conjoined_ with commas.

A predicate is defined by one or more clauses.  A _fact_ has no body: `append([], Ys, Ys).` declares that concatenating the empty list with any `Ys` yields `Ys`. A _rule_ contains a body:

> [!example] __Prolog append rule__
>
> A _rule_ contains a body:
>
> ```prolog
> append([X|Xs], Ys, [X|Zs]) :- append(Xs, Ys, Zs).
> ```
>
> The symbol `:-` reads "_provided that_", i.e. the head holds whenever its body succeeds.

The interpreter treats every clause as a _predicate_ that can be true or false under some substitution of variables.  Scala functions become predicates when an extra argument is added to carry the result, e.g., `append(List(1), List(2,3)) == X` corresponds to `append([1],[2,3],X)` in Prolog.

A _query_ is a goal that the interpreter tries to satisfy.  The system backtracks over all possible bindings and reports each solution:

> [!example] __Prolog append query with multiple solutions__
>
> A _query_ is a goal that the interpreter tries to satisfy.  The system backtracks over all possible bindings and reports each solution:
>
> ```prolog
> ?- append(X, Y, [1,2,3]).
> X = []     , Y = [1,2,3]
> X = [1]    , Y = [2,3]
> X = [1,2]  , Y = [2]
> X = [1,2,3], Y = []
> ```

Variables may appear on any side of the goal; Prolog will generate all admissible substitutions.

> [!example] __Prolog append query with a solution schema__
>
> Variables may appear on any side of the goal; Prolog will generate all admissible substitutions.
>
> ```prolog
> ?- append([1], Y, Z)
> Y = X, Z = [1|X]
> ```

This backtracking search performed by Prolog is the engine behind many logic‑based applications such as expert systems and database queries.

## deductive information retrieval

The Prolog interpreter can be used as a lightweight knowledge base: facts are stored as clauses, and queries extract information by searching through those facts with backtracking. A family-tree database contains a small set of facts describes relationships such as gender, marriage and parenthood.  For example:

> [!example] __family facts__
>
> A family-tree database contains a small set of facts describes relationships such as gender, marriage and parenthood.  For example:
>
> ```prolog
> female(mary).   married(fred, mary).
> child(bob, fred).   child(sue, fred).
> ...
> ```
>
> These clauses form a static database that the interpreter can consult.

A simple query is written as a predicate followed by `?`.  The interpreter searches for substitutions that satisfy the goal and prints each solution.  For instance

> [!example] __simple query__
>
> A simple query is written as a predicate followed by `?`.  The interpreter searches for substitutions that satisfy the goal and prints each solution.  For instance
>
> ```Prolog
> prolog> child(bob, fred)?
> yes
> prolog> child(bob, X)?
> [X = fred]
> prolog> more
> no
> ```
>
> The special command `more` asks for subsequent solutions.

New facts can be inferred from existing ones by adding rules.  A rule has a head and a body separated by `:-`.  The sibling relation, for example, is defined in terms of `child`:

> [!example] __sibling rule__
>
> New facts can be inferred from existing ones by adding rules.  A rule has a head and a body separated by `:-`.  The sibling relation, for example, is defined in terms of `child`:
>
> ```prolog
> sibling(X,Y) :- child(X,Z), child(Y,Z).
> ```
>
> Running the query
>
>
> ```prolog
> ?- sibling(peter, bob).   % → yes
> ```
>
> produces all common parents of the two people, but with self-match and duplicate matches.

Because the rule above also matches a person with himself, we add a negative guard:

> [!example] __sibling without self‑match__
>
> Because the rule above also matches a person with himself, we add a negative guard:
>
> ```prolog
> same(X, X).
> sibling(X,Y) :- child(X,Z), child(Y,Z), not(same(X,Y)).
> ```

The predicate `not(P)` succeeds only when the goal `P` fails, which allows Prolog to exclude unwanted solutions.

## negation as failure

Negation (as failure) is expressed in Prolog by the predicate `not/1`.  It succeeds only when its argument fails, so it can be used to exclude unwanted solutions.  For instance, after adding facts and the rule

> [!example] __same predicate__
>
> For instance, after adding facts and the rule
>
> ```prolog
> sid(bob, 1234).
> sid(robert, 1234).
> same(X,Y) :- sid(X,ID), sid(Y,ID).
> ```
>
> allows the query `same(bob,robert)?` to succeed.  Before the facts were present it would have failed.

Negation may change earlier answers: if a new fact is added that makes a previously false goal true, the interpreter will report a different result on subsequent queries.

## recursion

Rules can refer to themselves, directly or indirectly, enabling recursion.  For example:

> [!example] __ancestor rule__
>
> Rules can refer to themselves, directly or indirectly, enabling recursion.  For example:
>
> ```prolog
> parent(X,Y) :- child(Y,X).
> ancestor(X,Y) :- parent(X,Y).
> ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
> ```
>
> The third clause is recursive and allows the interpreter to discover arbitrary‑depth ancestry.

Recursive rules give logic programming a power that most database query languages lack.  They enable reasoning about hierarchical or transitive relations such as `ancestor`.

## representation

A term is an algebraic data type with two constructors: `Var` for variables and `Constr` for compound terms.  In Scala this can be modelled as:

> [!example] __term representation__
>
> A term is an algebraic data type with two constructors: `Var` for variables and `Constr` for compound terms.  In Scala this can be modelled as:
>
> ```scala
> sealed trait Term
> case class Var(name:String) extends Term
> case class Constr(name:String, args:List[Term]) extends Term
> ```
>
> A variable `X` is represented by `Var("X")`.  The list constructor `cons(X,nil)` becomes `Constr("cons", List(Var("X"), Constr("nil", Nil))`.

A variable `X` is represented by `Var("X")`.  The list constructor `cons(X,nil)` becomes `Constr("cons", List(Var("X"), Constr("nil", Nil))`. `Term.freeVars` returns a list of all the names of the type variables of the term, e.g. `["X"]` in `cons(X, nil)` . A substitution is a finite map from variable names to terms.  It can be expressed as:

> [!example] __substitution type__
>
> A substitution is a finite map from variable names to terms.  It can be expressed as:
>
> ```scala
> type Binding = (String, Term)
> type Subst   = List[Binding]
> ```
>
> A helper `lookup` retrieves the term bound to a name, if any.

A helper `lookup` retrieves the term bound to a name, if any. The substitution map is applied to a term by the method `map`.  Its definition in Scala follows:

> [!example] __substitution map implementation__
>
> The substitution map is applied to a term by the method `map`.  Its definition in Scala follows:
>
> ```scala
> sealed trait Term {
>   def map(s:Subst):Term = this match {
>     case Var(a) =>
>       lookup(s,a) match {case Some(t)=>t.map(s); case None=>this}
>     case Constr(c,ts) => Constr(c, ts.map(_.map(s)))
>   }
> }
> ```

The substitution map function interprets a substitution as an idempotent map on terms: `∀t, σ(σ(t)) = σ(t)`, so applying the same substitution twice does not change the result.

## asymmetric unification

The core of pattern‑matching logic programming is expressed by two mutually recursive functions: `pmatch` and its helper `pmatchLists`.  The first takes a _pattern_ (a term that may contain variables), another _term_ that must not contain variables, and an existing substitution `s`.  It returns `Some(s')` if the pattern matches the term under the current substitution `s` or `None` otherwise, where `s'` is the _most general_ substitution that is an extension of `s`.

> [!example] __`pmatch`__
>
> `pmatch` takes a _pattern_ (a term that may contain variables), another _term_ that must not contain variables, and an existing substitution `s`.  It returns `Some(s')` if the pattern matches the term under the current substitution `s` or `None` otherwise, where `s'` is the _most general_ substitution that is an extension of `s`.
>
> ```scala
> def pmatch(pattern: Term, term: Term, s: Subst): Option[Subst] =
>   (pattern, term) match {
>     case (Var(a), _) =>
>       lookup(s, a) match {
>         case Some(term1) => pmatch(term1, term, s)
>         case None        => Some(Binding(a, term) :: s)
>       }
>     case (Constr(a, ps), Constr(b, ts)) if a == b =>
>       pmatchLists(ps, ts, s)
>     case _ => None
>   }
> ```
>
> The `pmatch` routine first checks whether the pattern is a variable.  If it has already been bound in `s`, the previously bound term must match; otherwise a new binding is added to `s`.  When both pattern and term are constructors with the same name, their argument lists are matched recursively by `pmatchLists`.

The `pmatch` routine first checks whether the pattern is a variable.  If it has already been bound in `s`, the previously bound term must match; otherwise a new binding is added to `s`.  When both pattern and term are constructors with the same name, their argument lists are matched recursively by `pmatchLists`, which operates on lists of sub‑terms.  It succeeds only if all corresponding pairs unify under the current substitution and the two lists have equal length.

> [!example] __`pmatchLists`__
>
> When both pattern and term are constructors with the same name, their argument lists are matched recursively by `pmatchLists`, which operates on lists of sub‑terms.  It succeeds only if all corresponding pairs unify under the current substitution and the two lists have equal length.
>
> ```scala
> def pmatchLists(patterns: List[Term], terms: List[Term], s: Subst)
>     : Option[Subst] =
>   (patterns, terms) match {
>     case (Nil, Nil) => Some(s)
>     case (p :: ps, t :: ts) =>
>       pmatch(p, t, s).flatMap(psub => pmatchLists(ps, ts, psub))
>     case _ => None
>   }
> ```
>
> The implementation uses pattern matching on the pair of lists; when one list ends before the other a `None` is returned.  Successful matches are accumulated by chaining the substitutions with `flatMap` from left to right.  

The implementation uses pattern matching on the pair of lists; when one list ends before the other a `None` is returned.  Successful matches are accumulated by chaining the substitutions with `flatMap` from left to right.

These two functions, `pmatch` and `pmatchLists`, realise unification for first‑order terms, which underpins the whole logic programming interpreter in Scala.

## unification

Unification is the symmetric extension of pattern matching that allows variables to appear on both sides of a rule head.  It searches for the _most general_ substitution σ such that applying σ to each term yields identical terms: given the current substitution `s`, find the _most general_ substitution `s'` that is an extension of `s` such that `x.map(s')` matches `y.map(s')`.

Unification becomes essential when a rule head contains variables that must be matched against the arguments of a query or another rule.  For instance, the clause `sibling(X,Y) :- child(X,Z), child(Y,Z), not(same(X, Y))` cannot be applied to the query `sibling(peter,Z)?` unless the variables `X` and `Y` are first respectively unified with `peter` and an unknown `Z`.  The unification algorithm produces substitutions `[X=peter, Y=Z]`, which then allows the body goals to be evaluated.  Without this symmetric matching step, Prolog would not be able to connect a generic rule head to a concrete query.

When infinite terms are disallowed, unification must also reject ill‑formed bindings that would create infinite terms; for instance `unify(X,cons(1,X))` fails because no finite term `X` satisfies the equation. The infinite term representing an infinite list of 1s would have satisfied `X`. Finite terms composed of variables and constructors are called _Herbrand terms_, named after the logician Jacques Herbrand.

The `unify` algorithm follows the same recursive structure as `pmatch`, but treats two variables as equal, swaps the arguments when one side is a variable and performs an _occurrence check_ to avoid infinite bindings.

> [!example] __unify function__
>
> The `unify` algorithm follows the same recursive structure as `pmatch`, but treats two variables as equal, swaps the arguments when one side is a variable and performs an _occurrence check_ to avoid infinite bindings.
>
> ```scala
> def unify(x: Term, y: Term, s: Subst): Option[Subst] = (x, y) match {
>   case (Var(a), Var(b)) if a == b => Some(s)
>   case (Var(a), _) =>
>     lookup(s, a) match {
>       case Some(t1) => unify(t1, y, s)
>       case None =>
>         if y.map(s).freevars.contains(a) then None  // occurrence check
>         else Some(Binding(a, y) :: s)
>     }
>   case (_, Var(b)) => unify(y, x, s)
>   case (Constr(c1, xs), Constr(c2, ys)) if c1 == c2 =>
>     unifyLists(xs, ys, s)
>   case _ => None
> }
> ```
>
> The helper `unifyLists` recursively matches two lists of sub‑terms and propagates the accumulated substitution from left to right.

The helper `unifyLists` recursively matches two lists of sub‑terms and propagates the accumulated substitution from left to right. Below are some examples of running `unify`:

> [!example] __`unify` examples__
>
> Below are some examples of running `unify`:
>
> ```prolog
> unify(sibling(peter, Z), sibling(X, Y)) = [X = peter, Z = Y]
> unify(cons(X,nil), cons(X,Y))           = [Y = nil]
> unify(cons(X,nil), cons(X,a))           = <failure>
> unify(X, cons(1, X))                    = <failure>
> ```
>
> In the last case the attempted binding `X = cons(1, X)` would create an infinite tree; the occurrence check rejects it.  When the check is omitted a Prolog interpreter may loop instead of failing.

### complexity of unification

When the occurrence check is omitted, the algorithm visits each node of both terms once, giving a linear‑time bound in the size of the input.  The resulting most general unifier can, however, grow exponentially because repeated substitutions may duplicate sub‑terms.  Even though the result can be huge, the implementation shares trees rather than copying them, so the time spent is still proportional to the size of the two arguments. The following unification demonstrates how an exponential‑size most general unifier can be produced while the algorithm remains linear in the input size:

> [!example] __unifying two nested sequences__
>
> The following unification demonstrates how an exponential‑size most general unifier can be produced while the algorithm remains linear in the input size:
>
> ```prolog
> unify(seq(X1, b(X2,X2), X2, d(X3,X3)), seq(a(Y1,Y1), Y1, c(Y2,Y2), Y2))
> % X1 = a(Y1, Y1)
> % Y1 = b(X2, X2)
> % X2 = c(Y2, Y2)
> % Y2 = d(X3, X3)
> ```
>
> The computed most general unifier is deeply nested. Its length grows exponentially with the depth of the sequences, yet the unification procedure still processes each input node only once.

If the occurrence check is performed naively, each subtree may be traversed many times, yielding a worst‑case exponential complexity.  By marking already visited sub‑terms the test becomes linear in the number of nodes, so the overall unification algorithm becomes quadratic; with more sophisticated data structures the overall unification algorithm can reach $O(n\log n)$.

Unfortunately, most practical Prolog systems skip the occurrence check to avoid this overhead. This is fine if infinite terms are allowed, such as _Prolog 3_, also developed by Colmerauer. Howevver, most other Prolog interpreters disallow infinite terms; and when a variable that appears inside its own binding is introduced, they may behave unpredictably or loop infinitely.

## backtracking

Prolog clause has a head and an optional body separated by `:-`.  The interpreter processes clauses sequentially: for every goal it tries to unify the first predicate with a clause head.  If unification succeeds, the body is evaluated; otherwise the next clause is tried.  When no clause matches, the query fails.  For example:

> [!example] __Prolog append rule and backtracking__
>
> The interpreter processes clauses sequentially: for every goal it tries to unify the first predicate with a clause head.  If unification succeeds, the body is evaluated; otherwise the next clause is tried.  When no clause matches, the query fails.  For example:
>
> ```prolog
> append([], Ys, Ys).                                % fact
> append([X|Xs], Ys, [X|Zs]) :- append(Xs, Ys, Zs).  % rule
> ```
>
> A query `?- append([1], [2,3], X).` forces the interpreter to try the two clauses in order.  The first clause fails because `[1]` does not unify with `[]`.  The second succeeds after recursively unifying the head and then the tail; backtracking stops as soon as a solution is found.

Unification binds variables consistently across all parts of the goal in the _most general_ way, enabling Prolog to search for any assignment that satisfies the whole query.  When several clauses match, the interpreter explores each alternative in turn, yielding multiple solutions if they exist.

### backtracking implementation

To implement backtracking, instead of returning a single result, we can return _all_ solutions as a lazy list.  Each failure becomes an empty list, while a successful derivation yields at least one element.  The search for paths in an acyclic graph illustrates this idea:

> [!example] __paths with lazy list__
>
> To implement backtracking, instead of returning a single result, we can return _all_ solutions as a lazy list.  Each failure becomes an empty list, while a successful derivation yields at least one element.  The search for paths in an acyclic graph illustrates this idea:
>
> ```scala
> def paths(x: Node, y: Node): LazyList[List[Node]] =
>   if (x == y) LazyList.cons(List(x), LazyList.empty)
>   else for {
>     z <- LazyList.from(x.successors)
>     p <- paths(z, y)
>   } yield x :: p
> ```
>
> The `flatMap` in the for‑comprehension concatenates the lists of solutions from each successor, giving a lazy stream of all possible paths between `x` and `y`.  Because the list is lazy, new paths are generated only when requested.

## implementation

The core routine that turns a Prolog query into answers is the `solve` function.  It produces a lazy list of substitutions, one per solution.  Its public signature is  

> [!example] __`solve` signature__
>
> The core routine that turns a Prolog query into answers is the `solve` function.  It produces a lazy list of substitutions, one per solution.  Its public signature is  
>
> ```scala
> def solve(query: List[Term], clauses: List[Clause]): LazyList[Subst]
> ```

A Prolog clause is stored as a head and a body.  Because a clause may be reused many times during a derivation, each use must see fresh variables.  The `Clause` class generates new variable names on demand:

> [!example] __`Clause`__
>
> Because a clause may be reused many times during a derivation, each use must see fresh variables.  The `Clause` class generates new free variable names on demand:
>
> ```scala
> case class Clause(lhs: Term, rhs: List[Term]) {
>   lazy val freevars = (lhs.freevars ++ rhs.flatMap(_.freevars)).distinct
>   def newInstance =
>     var s: Subst = Nil
>     for a <- freevars do s = Binding(a, newVar(a)) :: s
>     Clause(lhs.map(s), rhs.map(_.map(s)))
> }
> ```
>
> `newInstance` replaces every free variable in the clause body with a fresh copy, ensuring that different uses of the same rule do not interfere.

The `solve` implementation delegates to a recursive helper `solveRec` that keeps the current substitution and the remaining part of the query.  A successful match yields a substitution that is then passed on to the rest of the goal. The recursive routine that performs backtracking is defined inside the public `solve` method so it can see the list of clauses supplied by the caller:

> [!example] __`solveRec` implementation__
>
> `solveRec` returns a lazy list of all substitutions that satisfy the remaining part of the query.  The loop over `clauses` embodies backtracking: each clause is tried in order, and every successful unification spawns a recursive descent on the rest of the goal.
>
> ```scala
> def solve(query: List[Term], clauses: List[Clause]): LazyList[Subst] = {
>   def solveRec(q: List[Term], s: Subst): LazyList[Subst] = q match
>     case Nil => LazyList.cons(s, LazyList.empty)
>     case h :: t =>
>       for clause <- LazyList.from(clauses)           // try every clause in order
>         s1 <- tryClause(clause.newInstance, h, s)   // unify head with goal
>         s2 <- solveRec(t, s1)                       // continue with rest of query
>         yield s2                                      
>   solveRec(query, Nil)
> }
> ```
>
> The helper `tryClause` is responsible for attempting to use a single clause against the current goal.

The helper `tryClause` is responsible for attempting to use a single clause against the current goal.  It first tries to unify the head of the clause with the goal term under the present substitution.  If unification succeeds, it returns all substitutions that arise from recursively solving the clause’s body; otherwise it yields an empty lazy list so that backtracking can move on to the next rule.

> [!example] __`tryClause`__
>
> It first tries to unify the head of the clause with the goal term under the present substitution.  If unification succeeds, it returns all substitutions that arise from recursively solving the clause’s body; otherwise it yields an empty lazy list so that backtracking can move on to the next rule.
>
> ```scala
> def tryClause(c: Clause, q: Term, s: Subst): LazyList[Subst] =
>   unify(q, c.lhs, s) match {
>     case Some(s1) => solveRec(c.rhs, s1)  // head succeeds → continue search
>     case None     => LazyList.empty       // failure → backtrack
>   }
> ```
>
> The `unify` function produces an optional substitution; the pattern matching above converts that into a lazy list of solutions.  If the clause cannot be applied, `LazyList.empty` represents a dead‑end in the search tree.

Negation as failure (`not(P)`) is handled by trying to solve the sub‑goal and checking if it succeeds.  If it fails, `not` succeeds; otherwise it fails:

> [!example] __negation handling__
>
> Negation as failure (`not(P)`) is handled by trying to solve the sub‑goal and checking if it succeeds.  If it fails, `not` succeeds; otherwise it fails:
>
> ```scala
> def solveRec(query: List[Term], s: Subst): LazyList[Subst] = query match
>   // ...
>   case Constr("not", qs) :: queryRest =>
>     if (solveRec(qs, s).isEmpty) solveRec(queryRest, s)
>     else LazyList.empty
>   // ...
> ```
>
> This simple rule turns the presence of a failure into a success and vice‑versa, allowing classical logic programming to be expressed in the same framework.

## formal reasoning

Logic programming can be viewed as a form of deductive computation.  A Prolog program is a set of clauses that act like logical axioms; a query is true when it follows from those axioms by repeated application of the unification rule.  In this view the interpreter should return substitutions that make the goal a logical consequence of the program.

### soundness

Unification in most Prolog implementations ignores the _occurrence check_, so terms may be bound to structures that contain themselves.  This permits answers that are not genuine solutions when infinite terms are disallowed. For instance, with the rules:

> [!example] __`same/2` and `strangeNum/1`__
>
> Unification in most Prolog implementations ignores the _occurrence check_, so terms may be bound to structures that contain themselves.  This permits answers that are not genuine solutions when infinite terms are disallowed. For instance, with the rules:
>
> ```prolog
> same(X,X).
> strangeNum(X) :- same(X,succ(X)).
> ```
>
> In some Prolog interpreter without the occurrence check, querying `?- strangeNum(X).` succeeds with `[X = succ(X)]`, which is disallowed.

The omission of the occurrence check therefore makes the interpreter _unsound_.

### completeness

Even a sound interpreter can miss solutions because it typically uses depth‑first search.  With a graph containing a cycle, the recursion never terminates:

> [!example] __`path/2` with a cycle__
>
> With a graph containing a cycle, the recursion never terminates:
>
> ```prolog
> successor(a,b).  successor(b,a).  successor(b,c).
> path(X,X).
> path(X,Y) :- successor(X,Z), path(Z,Y).
> ```
>
> Query `?- path(a,c).` follows the loop: `path(a,c)` → `successor(a,b), path(b,c)` → `path(b, c)` → `successor(b, a), path(a, c)` → `path(a, c)` → ... → stack overflow.

The recursive helper `solveRec` continually tries the same clause without detecting that the current goal has already been explored, so it never backtracks to a different branch.

A common remedy is to detect repeated goals and stop recursion when a cycle is detected.  This works for simple cycles but fails in general because new instances of clauses introduce fresh variables, making the set of possible goals unbounded. An alternative is to replace depth‑first search by breadth‑first search: it guarantees that every reachable goal is examined, but it uses far more memory and still may diverge on infinite derivations.

In practice, Prolog programmers must order clauses carefully and avoid rules that can lead to non‑terminating searches.  The formal reasoning behind these behaviours explains why the interpreter’s results are only an _approximation_ of pure logical consequence.

### problems with negation

The _not_ predicate implements the _closed‑world assumption_: a goal succeeds when its body cannot be proven.  With only concrete terms this is harmless, but it can lead to unexpected behaviour when variables remain free.  For instance, in the program  

> [!example] __dietary rules__
>
> The _not_ predicate implements the _closed‑world assumption_: a goal succeeds when its body cannot be proven.  With only concrete terms this is harmless, but it can lead to unexpected behaviour when variables remain free.  For instance, in the program  
>
> ```prolog
> vegetable(bean).          % facts
> vegetable(tomato).
> food(hamburger).
> junkFood(X) :- not(vegetable(X)).
> healthy(X) :- not(junkFood(X)).
> ```
>
> `junkFood(hamburger)?` succeeds, yet `junkFood(X)?` and `junkFood(X), same(X, hamburger)?` fails, but the query `same(X,hamburger), junkFood(X)?` succeeds.

`junkFood(hamburger)?` succeeds, yet `junkFood(X)?` and `junkFood(X), same(X, hamburger)?` fails, but the query `same(X,hamburger), junkFood(X)?` succeeds.  In the first two cases, The interpreter cannot discover that _hamburger_ is a possible junk food when the variable remains free. In the last case, by first unifying with the substitution `[X = hamburger]`, the interpreter _can_ find that _hamburger_ is a possible junk food. These cases show that negation causes _incompleteness_.

Adding another negation (`junkFood/1` negates `healthy/1`) turns the situation around from incompleteness to _unsoundness_:

> [!example] __re‑ordering of negations__
>
> Adding another negation (`junkFood/1` negates `healthy/1`) turns the situation around from incompleteness to _unsoundness_:
>
> ```prolog
> ?- healthy(hamburger).              % fails, which is sound
> ?- healthy(X), same(X, hamburger).  % succeeds with X = hamburger, which is unsound
> ```
>
> The second query does _not_ instantiate `X` before evaluating `not(junkFood(X))`, so `junkFood(X)` is false and `healthy(X)` is true, eventually producing a result that is not a logical consequence of the program.  This shows that Prolog’s negation is not true logical negation.

This shows that Prolog’s negation is not true logical negation. These limitations motivate careful clause ordering and the use of advanced negation constructs when expressive power is required. Modern dialects replace `not` by predicates such as `dif(A, B)`, the proper negation of `same(A, B)`. `dif/2` performs a _constraint_ that succeeds only when it can be shown that two terms are different; it delays the test until enough information is available, avoiding both unsoundness and many completeness problems.

An alternative approach is to forbid negation altogether or restrict it by stratification, yielding Datalog‑style programs that guarantee termination. Datalog is at the core of many database theories and implementations.
