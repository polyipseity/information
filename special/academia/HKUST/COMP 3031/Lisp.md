---
aliases:
  - COMP 3031 Scala Lisp
  - COMP3031 Scala Lisp
  - HKUST COMP 3031 Scala Lisp
  - HKUST COMP3031 Scala Lisp
  - Scala Lisp
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/Lisp
  - language/in/English
---

# Scala Lisp

- HKUST COMP 3031

---

- see: [general/Lisp (programming language)](../../../../general/Lisp%20(programming%20language).md)

{@{__Scala Lisp__}@} is {@{a teaching tool that embeds a tiny Scheme‑like language inside Scala}@}. It demonstrates how {@{functional programming concepts—pure functions, immutable data and first‑class code}@}—can be implemented in {@{an interpreted form while still running on the JVM}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## Lisp

{@{_Lisp_}@} is {@{the oldest functional language}@}, created by {@{John McCarthy in 1959–60as a _List processor_}@}. It was designed to manipulate {@{symbolic data structures—trees and lists}@}—while other early languages {@{handled only arrays or records}@}. {@{Lisp’s simplicity}@} enabled {@{many landmark applications}@} such as {@{Macsyma, Emacs, AutoCAD and the ITA flight‑information system}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

Over {@{five decades}@} the language has {@{branched into several dialects}@}: {@{Common Lisp (full–blown), Scheme (minimalist teaching language)}@}, {@{Racket, Clojure on the JVM, and Elisp for Emacs}@}. The version used here is {@{a small, purely functional subset of Scheme}@}. Compared with Scala, Lisp has {@{no complex syntax, no static types}@}, builds {@{everything from cons cells, and treats programs as lists that can be manipulated by code}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280!2025-12-25,4,280-->

{@{A lightweight interpreter for a subset of Scheme}@} is written in Scala by defining {@{an abstract syntax tree, an evaluator that matches on the AST, and a global environment mapping symbols to values}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

### Lisp programs

{@{A _Lisp program_}@} is written as {@{nested parentheses}@}. {@{Every expression inside a pair of brackets}@} is called {@{a _combination_}@}; {@{its first element}@} is {@{an operator (often a function)}@} and {@{the remaining elements}@} are {@{operands, separated by whitespace}@}. {@{The most common operators}@} are {@{_special forms_}@}: {@{`(define ...)` creates a binding}@}, {@{`(lambda ...)` builds an anonymous function}@}, and {@{`(if ...)` chooses between two branches}@}. These do not follow {@{ordinary function–application rules}@}; they decide how {@{their arguments are evaluated}@}. {@{All other combinations}@} are treated as {@{normal calls}@}: {@{the operator}@} is {@{first evaluated, then its operands}@}, and {@{the result of the operator}@} is {@{the evaluation result of the operator and operands enclosed in the outermost parentheses}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280-->

Because Lisp was originally {@{an intermediate language for compilers}@}, it contains only {@{a handful of rules}@}. This minimalism makes it easy to {@{write interpreters and reason about evaluation}@}, which is we can easily {@{implement a small Scheme subset}@} in Scala. The simplicity stems from the fact that {@{programs themselves are lists}@}; code can be {@{generated, transformed and executed}@} by treating them as {@{ordinary data structures}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{A simple example of a Lisp program}@} is {@{the factorial definition}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __factorial in Scheme__
>
> {@{A simple example of a Lisp program}@} is {@{the factorial definition}@}:
>
> ```Lisp
> (define (factorial n)
>   (if (zero? n)
>     1
>     (* n (factorial (- n 1))))
> )
> (factorial 10) ;; → 3628800
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,280-->

### Lisp data

{@{The primitive data types in Lisp}@} are {@{numbers, strings, symbols and lists}@}. {@{Numbers}@} can be {@{integers or floating–point values}@}; many dialects allow {@{arbitrarily large integers}@}. {@{Strings}@} behave {@{like Java strings}@}, while {@{symbols}@} are {@{unquoted identifiers that are looked up in an environment when a program is evaluated}@}. In {@{conditional expressions}@} every value counts as {@{_truthy_ except a set of specific values}@}, which represents {@{false}@}. The specific values may be {@{the empty list `nil`, the number `0`, the special falsy value `#f`, etc.}@} <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{Lists themselves}@} are constructed with {@{the function `cons`}@} and terminated by {@{the special value `nil`}@}. A list such as {@{`(quote (1 2 3))` or `' (1 2 3)`}@} is actually {@{a nested chain of pairs: `(cons 1 (cons 2 (cons 3 nil)))`}@}. Because Lisp has {@{no static type system}@}, lists can be {@{represented solely with functions}@}. {@{A cons cell}@} may be defined as {@{a function that receives a continuation `k`}@}; {@{the operations `cons`, `car` and `cdr`}@} are then just {@{applications of that function to suitable continuations}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __functional cons implementation__
>
> {@{A cons cell}@} may be defined as {@{a function that receives a continuation `k`}@}; {@{the operations `cons`, `car` and `cdr`}@} are then just {@{applications of that function to suitable continuations}@}:
>
> ```Lisp
> (define nil (lambda (k) (k 'none 'none)))
> (define (cons x y) (lambda (k) (k x y)))
> (define (car l) (l (lambda (x y) x)))
> (define (cdr l) (l (lambda (x y) y)))
> (define (null? l) (l (lambda (x y) (= y 'none))))
> ```
>
> {@{This illustrates}@} that {@{a cons cell can be built from pure functions}@}, even though in real implementations it is {@{stored as two pointers}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{The primitives `null?`, `car` and `cdr`}@} respectively {@{test for emptiness, return the first element, or return the rest of the list}@}. Their names come from {@{the original IBM 704 implementation}@} where a cons cell stored {@{an address part (`car`) and a decrement part (`cdr`)}@}. In Scala these map naturally to respectively {@{`.isEmpty`, `.head` and `.tail`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __list operations__
>
> {@{The primitives `null?`, `car` and `cdr`}@} respectively {@{test for emptiness, return the first element, or return the rest of the list}@}. Their names come from {@{the original IBM 704 implementation}@} where a cons cell stored {@{an address part (`car`) and a decrement part (`cdr`)}@}. In Scala these map naturally to respectively {@{`.isEmpty`, `.head` and `.tail`}@}.
>
> ```Lisp
> (define xs '(1 2 3))
> (car xs)   ;; → 1
> (cdr xs)   ;; → (2 3)
> (null? xs) ;; → #f
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280!2025-12-25,4,280-->

## interpreter

We will implement {@{a tiny Scheme interpreter in Scala}@}, reusing {@{the same data structures that Lisp uses internally}@}. The implementation is split into {@{four parts}@}: {@{representation, tokenization, parsing, and evaluation}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## internal representation

{@{Lisp values}@} are represented by {@{a single type `Data` that aliases `scala.Any`}@}. {@{Numbers, strings and lists}@} map to {@{their Scala counterparts}@}; {@{symbols}@} become {@{instances of `scala.Symbol`}@}. {@{A convenient syntax}@} lets the reader write {@{`'name` instead of `Symbol("name")`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`scala.Symbol`__
>
> {@{The standard Scala symbol class}@} is {@{defined in the core library}@}:
>
> ```Scala
> case class Symbol(name: String):
>   override def toString = s"'$name"
>   // ...
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{A factorial program written in Scheme}@} can be represented {@{directly as a Scala list of `Data`}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __factorial program internal representation__
>
> {@{The Scheme expression}@} as follows:
>
> ```scheme
> (define (factorial n)
>   (if (= n 0) 1 (* n (factorial (- n 1))))
> (factorial 5))
> ```
>
> becomes in {@{Scala data structures}@}:
>
> ```Scala
> List('def, 'factorial,
>   List('lambda, List('n),
>     List('if, List('=, 'n, 0), 1,
>       List('* , 'n, List('factorial, List('-', 'n, 1)))),
>   List('factorial, 5))
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

## tokenizer

{@{A lightweight lexer}@} turns {@{a source string into a stream of tokens}@}. It implements {@{`Iterator[String]`}@} and skips {@{whitespace while keeping track of the current character index}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __LispTokenizer skeleton__
>
> {@{A lightweight lexer}@} turns {@{a source string into a stream of tokens}@}. It implements {@{`Iterator[String]`}@} and skips {@{whitespace while keeping track of the current character index}@}.
>
> ```Scala
> class LispTokenizer(s: String) extends Iterator[String] {
>   private var i = 0
>   private def isDelimiter(ch: Char) =
>     ch.isWhitespace || ch == '(' || ch == ')'
>   def hasNext: Boolean = { … }
>   def next(): String = { … }
> }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{`hasNext()`}@} checks for {@{more input}@}, ignoring {@{leading whitespace in the remaining input}@}; {@{`next()`}@} returns {@{the next token}@}, which can be {@{`"("`, `")"`, a number, a string literal or an identifier}@}. If {@{the end of input is reached without matching parentheses}@}, {@{an error is raised}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## parser

{@{Parsing}@} uses {@{simple _recursive-descent parsing_ functions}@} that consume {@{tokens from the tokenizer}@}. {@{`parseExpr`}@} handles {@{atomic values}@}; {@{`parseList`}@} collects {@{elements until it meets the closing parenthesis}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __String to Lisp tree__
>
> {@{Parsing}@} uses {@{simple _recursive-descent parsing_ functions}@} that consume {@{tokens from the tokenizer}@}. {@{`parseExpr`}@} handles {@{atomic values}@}; {@{`parseList`}@} collects {@{elements until it meets the closing parenthesis}@}.
>
> ```Scala
> def string2lisp(s: String): Data = {
>   val it = new LispTokenizer(s)
>   def parseExpr(tok: String): Data =
>     if (tok == "(")  parseList()
>     else if (tok == ")") error("unmatched parenthesis")
>     else if (tok.charAt(0).isDigit) tok.toInt
>     else if (tok.head == '"' && tok.last == '"') tok.substring(1, tok.length-1)
>     else Symbol(tok)
>   def parseList(): List[Data] = {
>     val t = it.next()
>     if (t == ")") Nil else parseExpr(t) :: parseList()
>   }
>   parseExpr(it.next())
> }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{Running `string2lisp("(lambda (x) (+ (* x x) 1))")`}@} yields {@{a nested list of `Data`, ready for evaluation}@}. The next step is implementing {@{an evaluator}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## syntax

{@{The interpreter}@} evaluates {@{a single Scheme expression}@} that may contain {@{_special forms_ such as `val`, `def`, `lambda`, `quote` and `if`}@}. {@{A __`val`__}@} binds {@{an immutable value}@}, while {@{__`def`__}@} creates {@{a definition that is re‑evaluated each time it is used}@}. These two form {@{the core of local bindings}@}; {@{higher-level binders}@} like {@{`let`, `let*` or `letrec`}@} are only {@{syntactic sugar for combinations of these primitives}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __using `val` and `def`__
>
> {@{A __`val`__}@} binds {@{an immutable value}@}, while {@{__`def`__}@} creates {@{a definition that is re‑evaluated each time it is used}@}.
>
> ```scheme
> (val x (+ 1 2)   ; x = 3
>   (print x))      ; → prints 3
> (def square (x)
>   (* x x))
> (square 4)        ; → 16
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{A __`lambda`__}@} creates {@{an anonymous function}@}; {@{its parameters}@} are {@{a list of symbols}@} and {@{the body}@} is {@{a single expression}@}. {@{__`quote`__}@} returns {@{its argument without evaluation}@}, enabling {@{data to be distinguished from code}@}. {@{__`if`__}@} evaluates {@{the condition first and then chooses between two branches}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### syntactic sugar

Because Scheme has {@{many convenient syntactic sugar}@}, we first rewrite {@{those forms into the core primitives before evaluation}@}. {@{The transformation function}@} _normalize_ {@{walks over an expression tree and replaces each derived form}@} by {@{an equivalent one that only uses the primitive special forms}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{A typical rule}@} is to turn {@{logical short-circuit operators into `if`}@}. For example: <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __normalizing `and` and `or`__
>
> {@{A typical rule}@} is to turn {@{logical short-circuit operators into `if`}@}. For example:
>
> ```Scala
> def normalize(expr: Data): Data = expr match
>   case 'and :: x :: y :: Nil =>
>     normalize('if :: x :: y :: 0 :: Nil)
>   case 'or :: x :: y :: Nil =>
>     normalize('if :: x :: 1 :: y :: Nil)
>   // other rules...
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{Other derived forms}@} are handled {@{in a similar way}@}. {@{The `cond` macro}@} expands into {@{nested `if`s}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __normalizing `cond`__
>
> {@{The `cond` macro}@} expands into {@{nested `if`s}@}:
>
> ```Scala
> def normalize(expr: Data): Data = expr match
>   case 'cond :: clauses :: Nil =>
>     val ret = clauses.foldRight(List('else, Nil)) {
>       case ('else :: body :: Nil) :: _ =>
>         body
>       case (test :: body :: Nil) :: rest =>
>         'if :: test :: body :: rest :: Nil
>     }
>     normalize(ret)
>  // other rules...
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{The `def` form}@} is also {@{a derived form}@}: it expands into {@{an ordinary `def` binding plus a lambda that captures the arguments}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __normalizing `def`__
>
> {@{The `def` form}@} is also {@{a derived form}@}: it expands into {@{an ordinary `def` binding plus a lambda that captures the arguments}@}:
>
> ```Scala
> def normalize(expr: Data): Data = expr match
>   case 'def :: (name :: args) :: body :: expr2 :: Nil =>
>     val ret = 'def :: name ::
>       List('lambda, args, body) :: expr2 :: Nil
>     normalize(ret)
>  // other rules...
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280-->

With {@{these rules in place}@}, {@{every Scheme expression}@} is reduced to {@{a tree that only uses the primitive forms `val`, `def`, `lambda`, `quote` and `if`}@}. {@{The evaluator}@} can then work on {@{this simplified representation}@} without having to {@{recognise any other syntactic sugar}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## characteristics

{@{Lisp’s most striking trait}@} is {@{its _minimal syntax_}@}. The language uses {@{only parentheses and symbols}@}, so {@{every program is a nested list}@}. This eliminates {@{a dedicated lexer and makes parsing trivial}@}, but {@{the lack of syntactic sugar}@} can make {@{long expressions hard to read}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

Because Lisp has {@{no static type system}@}, {@{a value}@} may be {@{any data structure that conforms to the list representation}@}. {@{This flexibility}@} lets programmers write {@{very generic code}@}, yet it also means {@{errors such as passing a string where an integer is expected}@} are {@{only caught at run time}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{All of Lisp’s data structures}@} are built from {@{cons cells – pairs of pointers – which in turn form lists}@}. Using {@{only lists}@} gives {@{great uniformity}@}: {@{the same representation}@} works for {@{any complex data structures}@}. The downside is that {@{more specialised abstractions (e.g., hash tables or trees)}@} have to be {@{implemented on top of this core}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

Finally, {@{treating programs as data}@} enables {@{powerful macro systems and meta-programming}@}. It also means that a program can {@{generate, modify and evaluate other programs at run time}@}. While {@{this feature is very expressive}@}, it makes {@{reasoning about correctness more difficult}@} because a program may {@{change its own structure}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## evaluator

{@{The evaluator for Scheme--}@} is {@{a small interpreter written in Scala}@} that takes {@{a value of type `Data` (a number, string, symbol or list)}@} and returns {@{another `Data`}@}. For instance, evaluating {@{`List('*, 2, 7)`}@} yields {@{the numeric literal `14`}@}. It can be implemented by {@{a recursive function that walks the abstract syntax tree of a Scheme-- expression}@} and produces {@{a `Data` value}@}. It takes two arguments: {@{the expression to evaluate and an `Environment`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### environment

{@{When the input}@} is {@{a symbol such as `x`}@}, {@{its meaning}@} depends on {@{the current environment}@}: if {@{`x` has been bound to some value}@}, {@{that value is returned}@}; otherwise {@{an error is raised}@}. Thus the interpreter must maintain {@{an _environment_ mapping names to values}@}. {@{An environment}@} stores {@{bindings of symbols to `Data`}@}. Its two essential operations are {@{`lookup` and `extend`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __environment__
>
> {@{An environment}@} stores {@{bindings of symbols to `Data`}@}. Its two essential operations are {@{`lookup` and `extend`}@}.
>
> ```Scala
> def lookup(n: String): Data
> def extend(name: String, v: Data): Environment
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{A simple implementation}@} uses {@{a linked list of bindings, similar to a `List`}@}. {@{The class `Environment`}@} is defined as an abstract base that returns {@{a value for a name or throws if the name is unknown}@}. {@{Each call to `extend`}@} creates {@{a new environment whose latest binding shadows any previous one}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __environment implementation__
>
> {@{A minimal, immutable environment}@} implemented by {@{chaining objects, similar to a `List`}@}:
>
> ```Scala
> abstract class Environment {
>   def lookup(n: String): Data = throw new RuntimeException(s"undefined: $n")
>   def extend(name: String, v: Data): Environment =
>     new Environment {
>       override def lookup(m: String): Data =
>         if (m == name) v else Environment.this.lookup(m)
>     }
>  // The following will be used in recursion...
>  def extendRec(name: String, expr: Environment => Data) = ???
> }
> val EmptyEnvironment = new Environment {}
> ```
>
> {@{This version}@} has {@{linear-time lookups}@} because {@{each `lookup` walks the chain of bindings}@}. Note that {@{the environment with only `lookup` and `extend` as implemented above}@} does not {@{support using `def` to define recursive functions}@}. {@{The `extendRec` function}@} intends to {@{fix this}@}; see below. <!--SR:!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

Note that {@{the environment with only `lookup` and `extend` as implemented above}@} does not {@{support using `def` to define recursive functions}@}. {@{The `extendRec` function}@} intends to {@{fix this}@}; see below.

{@{The same structure}@} can be replaced by {@{a map for _O(log n)_ performance}@}, but {@{the simple list form}@} is often used {@{in educational settings to keep the code readable}@}. {@{The inner class `Environment.this`}@} refers to {@{the outer environment that the new object closes over}@}; this allows {@{a fresh binding to shadow older ones without mutating the existing structure}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

The evaluator uses {@{these operations during evaluation}@}: every time it {@{encounters a symbol}@}, it calls {@{`lookup`}@}; when {@{a binding is defined with `(val name expr)` or `(define name expr)`}@} it adds {@{the binding respectively via `extend` or `extendRec`}@}. Together they provide {@{lexical scoping for Scheme-- programs}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### predefined bindings

{@{The interpreter}@} needs {@{a starting environment that contains the values of built-in symbols such as `*`}@}. Those values are not {@{simple data}@}; they must represent {@{functions that can be applied to Scheme expressions}@}. We therefore introduce {@{a Scala type that captures a function from a list of `Data` to a `Data`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`Closure` for builtin operators__
>
> {@{The built-in operator `*`}@} is represented by {@{a closure whose pattern matches on two integer arguments}@}:
>
> ```Scala
> case class Closure(f: PartialFunction[List[Data], Data])
> val star = Closure { case List(arg1: Int, arg2: Int) => arg1 * arg2 }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{The partial function inside the `Closure`}@} allows us to express {@{both arity and type checks in one pattern}@}. When the interpreter evaluates {@{a list whose first element is the symbol `*`}@}, it looks up {@{this closure in the initial environment and applies its function to the evaluated operands}@}. If {@{the arguments do not match the pattern}@}, {@{the partial function throws an exception}@}; {@{a safer approach}@} would be to use {@{`f.lift(a)` which returns an `Option[Data]` whenever `f(a)` would have thrown an exception}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### evaluation rules

{@{The evaluator}@} is {@{a recursive function that walks the abstract syntax tree of a Scheme-- expression}@} and produces {@{a `Data` value}@}. It takes {@{two arguments: the expression to evaluate and an `Environment`}@}. The following sections sketch the main rules. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{Atoms}@} are {@{returned unchanged}@}, while {@{symbols}@} are {@{looked up in the current environment}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __atom evaluation__
>
> {@{Atoms}@} are {@{returned unchanged}@}, while {@{symbols}@} are {@{looked up in the current environment}@}.
>
> ```Scala
> def eval(x: Data, env: Environment): Data = x match {
>   case _: String | _: Int => x
>   case Symbol(name) => env.lookup(name)
> }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{Special forms}@}, which includes {@{`def`, `val`, `if`, `quote`, and `lambda`}@} are {@{handled explicitly}@}; all other lists are {@{treated as ordinary function applications}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,270!2025-12-25,4,280-->

{@{`__val__`}@} introduces {@{a new binding that is visible for the rest of the expression}@}. It evaluates {@{its body in an environment extended with the new pair}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`val` special form__
>
> {@{`__val__`}@} introduces {@{a new binding that is visible for the rest of the expression}@}. It evaluates {@{its body in an environment extended with the new pair}@}.
>
> ```Scala
> case 'val :: Symbol(name) :: expr :: rest :: Nil =>
>   eval(rest, env.extend(name, eval(expr, env)))
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{__`if`__}@} evaluates {@{the condition first}@}; in our specific implementation, {@{a non-zero number}@} is {@{treated as _true_}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`if` special form__
>
> {@{__`if`__}@} evaluates {@{the condition first}@}; in our specific implementation, {@{a non-zero number}@} is {@{treated as _true_}@}.
>
> ```Scala
> case 'if :: cond :: thenp :: elsep :: Nil =>
>   if (eval(cond, env) != 0) eval(thenp, env)
>   else eval(elsep, env)
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{__`quote`__}@} returns {@{its argument without evaluation}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`quote` special form__
>
> {@{__`quote`__}@} returns {@{its argument without evaluation}@}.
>
> ```Scala
> case 'quote :: y :: Nil => y
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{__`lambda`__}@} creates {@{a closure that remembers the surrounding environment}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`lambda` special form__
>
> {@{__`lambda`__}@} creates {@{a closure that remembers the surrounding environment}@}.
>
> ```Scala
> case 'lambda :: params :: body :: Nil =>
>   mkClosure(asList(params), body, env)
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

{@{__`def`__, similar to `val`}@}, also introduces {@{a new binding that is visible for the rest of the expression}@}; unlike `val`, this new binding is {@{evaluated _every time_ it is looked up (i.e. _by name_)}@}, and also {@{visible to the expression defining the binding itself}@}. Then, same as `val`, it evaluates {@{its body in an environment extended with the new pair}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`def` special form__
>
> {@{__`def`__, similar to `val`}@}, also introduces {@{a new binding that is visible for the rest of the expression}@}; unlike `val`, this new binding is {@{evaluated _every time_ it is looked up (i.e. _by name_)}@}, and also {@{visible to the expression defining the binding itself}@}. Then, same as `val`, it evaluates {@{its body in an environment extended with the new pair}@}.
>
> ```Scala
> case 'def :: Symbol(name) :: expr :: rest :: Nil =>
>   eval(rest, env.extendRec(name, env2 => eval(expr, env2)))
> ```
>
> Note {@{`extendRec` is used}@}, which is needed to support {@{using `def` to define recursive functions}@}; see below. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

When {@{an expression is not a special form}@}, it is treated as {@{a function call}@}. {@{The operator and all operands}@} are {@{first evaluated}@}, then the operator value is {@{applied to the list of operand values}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __function application__
>
> {@{The operator and all operands}@} are {@{first evaluated}@}, then the operator value is {@{applied to the list of operand values}@}.
>
> ```Scala
> case operator :: operands =>
>   apply(eval(operator, env), operands.map(x => eval(x, env)))
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{The `apply` function}@} distinguishes between {@{a user-defined closure and any other value}@}. {@{A non-closure causes an error}@}; otherwise {@{the stored partial function is invoked with the argument list}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`apply` implementation__
>
> {@{The `apply` function}@} distinguishes between {@{a user-defined closure and any other value}@}. {@{A non-closure causes an error}@}; otherwise {@{the stored partial function is invoked with the argument list}@}.
>
> ```Scala
> def apply(fn: Data, args: List[Data]): Data = fn match {
>   case Closure(f) => f(args)
>   case _ => error("application of a non‑function: " + fn + " to " + args)
> }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### closure

{@{The Scheme-- interpreter}@} implements {@{lexical scoping by capturing the environment at the moment a function is created}@}. When {@{`mkClosure` is called}@}, it packages {@{a Scala anonymous function together with the current `Environment`}@}. {@{The resulting `Closure`}@} holds {@{a function that, when invoked, evaluates its body}@} in an environment {@{extended with bindings that pair each formal parameter from `ps`}@} to {@{the actual argument value supplied in `args`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __creating a closure__
>
> When {@{`mkClosure` is called}@}, it packages {@{a Scala anonymous function together with the current `Environment`}@}. {@{The resulting `Closure`}@} holds {@{a function that, when invoked, evaluates its body}@} in an environment {@{extended with bindings that pair each formal parameter from `ps`}@} to {@{the actual argument value supplied in `args`}@}.
>
> ```Scala
> def mkClosure(ps: List[String], body: Data, env: Environment) =
>   Closure { args => eval(body, env.extendMulti(ps, args)) }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{The helper `extendMulti`}@} walks {@{two lists in parallel}@} and produces {@{a new environment that contains every binding}@}. It also checks that {@{the two lists have equal length}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __environment extension for multiple bindings__
>
> {@{The helper `extendMulti`}@} walks {@{two lists in parallel}@} and produces {@{a new environment that contains every binding}@}. It also checks that {@{the two lists have equal length}@}.
>
> ```Scala
> def extendMulti(ps: List[String], vs: List[Data]): Environment =
>   (ps, vs) match {
>     case (Nil, Nil) => this
>     case (p :: ps1, v :: vs1) =>
>       extend(p, v).extendMulti(ps1, vs1)
>     case _ => error("wrong number of arguments")
>   }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

Because the closure keeps {@{a reference to its defining environment}@}, each application {@{re-uses that same lexical context}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

### scoping

Because the closure keeps {@{a reference to its defining environment}@}, each application {@{re-uses that same lexical context}@}. This contrasts with {@{dynamic scoping used in early Lisp versions}@}, where a function would capture {@{the _current_ stack of bindings rather than the one that existed when it was defined}@}. In {@{a dynamically scoped system}@}, calling `f(1)` where <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __dynamic scoping pitfall__
>
> In {@{a dynamically scoped system}@}, calling `f(1)` where
>
> ```Scala
> def f(x: Int) = g(y => x + y)
> def g(x: Int => Int) = x(2)
> f(1)
> ```
>
> ... would {@{raise an error}@} because {@{the inner lambda}@} looks up {@{`x` in the stack after `g` has pushed its own frame}@}, finding {@{a function instead of the integer}@}. {@{Renaming parameters}@} can sometimes {@{hide the problem}@}, such as renaming {@{`x` to `z` in the function `g`}@}, but {@{not always}@}. <!--SR:!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2000-01-01,1,250-->

{@{Renaming parameters}@} can sometimes {@{hide the problem}@}, such as renaming {@{`x` to `z` in the function `g`}@}, but {@{not always}@}.

{@{Dynamic scoping}@} makes {@{higher-order functions unreliable}@}. {@{Static (lexical) scoping, which Scheme and modern Lisps use}@}, fixes these issues by ensuring that {@{a function’s free variables are resolved in the environment where it was defined}@}. This guarantees {@{referential transparency and predictable behaviour of first-class functions}@}. {@{Some legacy Lisp dialects such as Common Lisp}@} still support {@{both dynamic and lexical scopes}@}, while {@{Elisp uses only dynamic scoping}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### recursion

{@{The language supports named recursion}@} by adding {@{the special form `(def <name> <expr> <rest>)`}@}. A `def` behaves like a `val` but {@{the bound expression is evaluated _by name_}@}, and may {@{refer to `<name>` itself, enabling recursive calls}@}. The interpreter must therefore delay {@{evaluating `<expr>` until the function is actually invoked}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{The usual `val` rule fails for recursion}@} because {@{the body is evaluated immediately}@}; and {@{the name is not visible inside `<expr>`}@}. To fix this we add {@{a new environment operation `extendRec`}@}, which stores {@{a _thunk_ that receives the current environment when it is needed}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`extendRec`__
>
> To fix this we add {@{a new environment operation `extendRec`}@}, which stores {@{a _thunk_ that receives the current environment when it is needed}@}.
>
> ```Scala
> abstract class Environment {
>   def lookup(n: String): Data
>   def extendRec(name: String, expr: Environment => Data) =
>     new Environment {
>       override def lookup(m: String): Data =
>         if (m == name) expr(this) else Environment.this.lookup(m)
>     }
>   def extend(name: String, v: Data) = extendRec(name, _ => v)
> }
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

With {@{the newly defined `extendRec`}@}, {@{a `def` is evaluated}@} as <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __`def` special form with `extendRec`__
>
> With {@{the newly defined `extendRec`}@}, {@{a `def` is evaluated}@} as
>
> ```Scala
> case 'def :: Symbol(name) :: expr :: rest :: Nil =>
>   eval(rest, env.extendRec(name, ext => eval(expr, ext)))
> ```
>
> {@{The thunk passed to `extendRec`}@} evaluates {@{`expr` in the extended environment that already contains the binding for `<name>`}@}, so recursive calls find {@{the correct value}@}. <!--SR:!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,300!2025-12-25,4,280!2025-12-25,4,280-->

{@{The thunk passed to `extendRec`}@} evaluates {@{`expr` in the extended environment that already contains the binding for `<name>`}@}, so recursive calls find {@{the correct value}@}.

This technique shows how {@{recursion can be reduced to _self-application_}@}. For instance, {@{the factorial function}@} can be written {@{without explicit recursion}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __recursion to self-application__
>
> This technique shows how {@{recursion can be reduced to _self-application_}@}. For instance, {@{the factorial function}@} can be written {@{without explicit recursion}@}:
>
> ```Lisp
> (lambda (n) (
>   (val factorial (lambda (self n)   ; self is a reference to the same lambda
>     (if (= n 1) 1 (* n (self self (- n 1))))
>   ))
>   (factorial factorial n)
> ))
> ```
>
> Here `self` refers to {@{the inner lambda}@}, and each call passes {@{the lambda itself as an argument}@}. The interpreter evaluates {@{the outer lambda once}@}; the inner lambda {@{repeatedly calls its own first argument}@}, which implements {@{the factorial loop}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

### global environment  

The interpreter starts from {@{a _global_ environment}@} that contains {@{the built-in operators and constants used by most programs}@}. It is built by {@{chaining calls to `extend` on an empty base}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __minimal global env__
>
> The interpreter starts from {@{a _global_ environment}@} that contains {@{the built-in operators and constants used by most programs}@}. It is built by {@{chaining calls to `extend` on an empty base}@}:
>
> ```Scala
> val globalEnv = EmptyEnvironment
>   .extend("=", Closure { case List(a, b) => if (a == b) 1 else 0 })
>   .extend("+", Closure {
>     case List(a: Int, b: Int) => a + b
>     case List(a: String, b: String) => a + b })
>   .extend("*", Closure { case List(a: Int, b: Int) => a * b })
>   .extend("nil", Nil)
>   .extend("cons", Closure { case List(h, t) => h :: asList(t) })
>   // ...
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{The environment}@} maps {@{identifiers such as `+` or `*`}@} to {@{`Closure` objects}@} that know {@{how to perform the corresponding operation}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

## usage  

To evaluate {@{a program}@}, {@{the function `evaluate`}@} is called with {@{an expression and the global environment}@}. It first {@{normalises the syntax}@}, then {@{delegates to `eval`}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __top‑level evaluation__
>
> To evaluate {@{a program}@}, {@{the function `evaluate`}@} is called with {@{an expression and the global environment}@}. It first {@{normalises the syntax}@}, then {@{delegates to `eval`}@}.
>
> ```Scala
> def evaluate(x: Data): Data = eval(normalize(x), globalEnv)
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->

{@{A convenience overload}@} lets {@{a user enter Scheme code as a string}@}: <!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

> [!example] __string evaluation interface__
>
> {@{A convenience overload}@} lets {@{a user enter Scheme code as a string}@}:
>
> ```Scala
> def evaluate(s: String): String =
>   lisp2string(evaluate(string2lisp(s)))
> ```
<!--SR:!2025-12-25,4,280!2025-12-25,4,280-->

## extensions

One can extend {@{the Scheme-- language}@} by writing {@{a simple REPL that reads one line at a time}@}, evaluates {@{it with `evaluate`}@}, and prints {@{the outcome}@}. When {@{the input is a top-level definition (`def ...`, `val ...`)}@}, the REPL must add {@{the new binding to the global environment before continuing}@}; when {@{the input is an ordinary expression}@} it should simply evaluate {@{it in the current global state and display the result}@}. <!--SR:!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280!2025-12-25,4,280-->
