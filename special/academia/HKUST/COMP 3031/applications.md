---
aliases:
  - COMP 3031 Scala application
  - COMP 3031 Scala applications
  - COMP3031 Scala application
  - COMP3031 Scala applications
  - HKUST COMP 3031 Scala application
  - HKUST COMP 3031 Scala applications
  - HKUST COMP3031 Scala application
  - HKUST COMP3031 Scala applications
  - Scala application
  - Scala applications
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/applications
  - language/in/English
---

# Scala applications

- HKUST COMP 3031

## word coder

{@{A __word coder__}@} translates {@{a telephone number into all possible mnemonic phrases}@} using {@{a supplied dictionary of words}@}. Prior to the era of {@{smartphone predictive-text}@}, {@{each numeric key on a phone}@} keypad had {@{an associated set of letters}@}; for instance, {@{the digit `2` represented "ABC"}@}, {@{the digit `3` represented "DEF"}@}, and so forth. In {@{Scala this mapping}@} can be expressed as <!--SR:!2026-10-21,277,330!2026-09-20,252,330!2026-09-17,249,330!2026-09-22,254,330!2026-11-03,290,330!2026-08-31,232,330!2026-10-13,273,330!2026-09-21,253,330!2026-10-22,278,330-->

> [!example] __mnemonics__
>
> Prior to the era of {@{smartphone predictive-text}@}, {@{each numeric key on a phone}@} keypad had {@{an associated set of letters}@}; for instance, {@{the digit `2` represented "ABC"}@}, {@{the digit `3` represented "DEF"}@}, and so forth. In {@{Scala this mapping}@} can be expressed as
>
> ```Scala
> val mnemonics = Map('2' -> "ABC", '3' -> "DEF", /* ... */ '9' -> "WXYZ")
> ```
<!--SR:!2026-11-04,290,330!2026-10-13,273,330!2026-10-10,270,330!2026-10-13,273,330!2026-10-16,276,330!2026-10-26,282,330-->

The goal is to implement {@{a method `encode(phoneNumber)`}@} that returns {@{every sequence of dictionary words}@} whose {@{concatenated numeric encodings match the input number}@}. For example, {@{the phone number `"7225247386"`}@} can be expressed as the single mnemonic phrase {@{`"Scala is fun"`}@}. <!--SR:!2026-09-16,248,330!2026-10-24,280,330!2026-10-19,275,330!2026-10-16,276,330!2026-10-13,273,330-->

### `Coder`

{@{A natural way to structure the solution}@} is {@{a small class}@} that encapsulates {@{the dictionary and all derived data structures}@}: <!--SR:!2026-10-19,275,330!2026-10-13,273,330!2026-09-19,251,330-->

> [!example] __`Coder`__
>
> {@{A natural way to structure the solution}@} is {@{a small class}@} that encapsulates {@{the dictionary and all derived data structures}@}:
>
> ```Scala
> class Coder(words: List[String]):
>   val mnemonics = Map(/* ... same mapping as above ... */)
>   /* ... */
> ```
<!--SR:!2026-09-22,254,330!2026-08-31,232,330!2026-10-20,276,330-->

#### `Coder.charCode`

{@{The first helper, `charCode`}@}, maps {@{any alphabetic character to its corresponding digit}@}. Using {@{a for-comprehension}@} we {@{invert the `mnemonics` map}@}: <!--SR:!2026-10-27,283,330!2026-09-15,247,330!2026-09-16,248,330!2026-10-11,271,330-->

> [!example] __`Coder.charCode`__
>
> {@{The first helper, `charCode`}@}, maps {@{any alphabetic character to its corresponding digit}@}. Using {@{a for-comprehension}@} we {@{invert the `mnemonics` map}@}:
>
> ```Scala
> private val charCode: Map[Char, Char] =
>   for
>     (digit, letters) <- mnemonics
>     letter <- letters
>   yield letter -> digit
> ```
<!--SR:!2026-10-22,278,330!2026-10-14,274,330!2026-11-08,294,330!2026-09-06,238,330-->

#### `Coder.wordCode`

With {@{`charCode` available}@}, {@{any word}@} can be turned {@{into the numeric string it represents}@}.  The method simply {@{upper-cases the word and looks up each character}@}: <!--SR:!2026-10-31,287,330!2026-10-16,276,330!2026-09-13,245,330!2026-10-12,272,330-->

> [!example] __`Coder.wordCode`__
>
> With {@{`charCode` available}@}, {@{any word}@} can be turned {@{into the numeric string it represents}@}.  The method simply {@{upper-cases the word and looks up each character}@}:
>
> ```Scala
> private def wordCode(word: String): String =
>   word.toUpperCase.map(charCode)
> ```
<!--SR:!2026-08-28,229,330!2026-10-12,272,330!2026-10-30,286,330!2026-09-14,246,330-->

#### `Coder.wordsForNum`

{@{The dictionary}@} is then {@{indexed by these digit strings}@} so that {@{a lookup of "7225"}@} immediately yields {@{all words whose encoding equals that sequence}@}. {@{The `withDefaultValue`}@} ensures {@{missing keys return an empty list rather than throwing}@}: <!--SR:!2026-11-08,294,330!2026-09-18,250,330!2026-09-19,251,330!2026-10-23,279,330!2026-10-25,281,330!2026-11-01,288,330-->

> [!example] __`Coder.wordsForNum`__
>
> {@{The dictionary}@} is then {@{indexed by these digit strings}@} so that {@{a lookup of "7225"}@} immediately yields {@{all words whose encoding equals that sequence}@}. {@{The `withDefaultValue`}@} ensures {@{missing keys return an empty list rather than throwing}@}:
>
> ```Scala
> private val wordsForNum: Map[String, List[String]] =
>   words.groupBy(wordCode).withDefaultValue(Nil)
> ```
<!--SR:!2026-10-04,266,330!2026-10-09,269,330!2026-09-01,233,330!2026-09-21,253,330!2026-10-16,276,330!2026-10-19,275,330-->

### `Coder.encode`

{@{The core algorithm}@} is {@{a classic recursive split}@}.  If {@{the input number is empty}@}, {@{the only encoding}@} is {@{the empty list}@}; otherwise we try {@{every possible prefix length}@} and combine {@{the results of the suffix recursively}@}: <!--SR:!2026-09-12,244,330!2026-10-05,267,330!2026-10-21,277,330!2026-10-27,283,330!2026-10-16,276,330!2026-10-11,271,330!2026-11-02,289,330-->

> [!example] __`Coder.encode`__
>
> {@{The core algorithm}@} is {@{a classic recursive split}@}.  If {@{the input number is empty}@}, {@{the only encoding}@} is {@{the empty list}@}; otherwise we try {@{every possible prefix length}@} and combine {@{the results of the suffix recursively}@}:
>
> ```Scala
> def encode(number: String): Set[List[String]] =
>   if (number.isEmpty) Set(Nil)
>   else for {
>     splitPoint <- (1 to number.length).toSet
>     word       <- wordsForNum(number.take(splitPoint))
>     rest       <- encode(number.drop(splitPoint))
>   } yield word :: rest
> ```
<!--SR:!2026-09-18,250,330!2026-10-14,274,330!2026-09-11,243,330!2026-10-12,272,330!2026-09-03,235,330!2026-10-09,269,330!2026-10-12,272,330-->

{@{This comprehension}@} enumerates {@{all ways of partitioning the digit string into dictionary words}@}, accumulating {@{each complete phrase as a list}@}. <!--SR:!2026-11-06,292,330!2026-11-04,290,330!2026-11-06,292,330-->

### word coder usage

{@{A minimal test harness}@} {@{demonstrates usage}@}: <!--SR:!2026-09-02,234,330!2026-10-09,269,330-->

> [!example] __word coder results__
>
> {@{A minimal test harness}@} {@{demonstrates usage}@}:
>
> ```Scala
> @main def code(number: String) =
>   val coder = Coder(List("Scala","Python","Ruby","C",
>                          "rocks","socks","sucks","works","pack"))
>   println(coder.encode(number).map(_.mkString(" ")))
> ```
<!--SR:!2026-10-15,275,330!2026-09-02,234,330-->

Thus the implementation finds {@{all valid mnemonic phrases in a handful of lines}@}. <!--SR:!2026-09-06,238,330-->

### word coder conclusion

{@{The problem}@} originates from Lutz Prechelt's 2000 study _An Empirical Comparison of Seven Programming Languages_ \(IEEE Computer 33(10): 23-29\), where he compared {@{code sizes for the same task}@} across {@{Tcl, Python, Perl, Rexx, Java, C++, and C}@}. {@{Scripting languages}@} typically required {@{about 100 lines of code}@}; {@{compiled languages}@} needed {@{200–300 lines}@}.  In Scala {@{the equivalent solver}@} is {@{roughly 20 lines long}@}, yet it remains {@{statically typed, purely functional, and free of side effects}@}—attributes that make {@{reasoning and refactoring straightforward}@}. <!--SR:!2026-09-08,240,330!2026-10-14,274,330!2026-10-28,284,330!2026-10-10,270,330!2026-10-13,273,330!2026-09-10,242,330!2026-10-08,268,330!2026-09-19,251,330!2026-10-14,274,330!2026-10-15,275,330!2026-10-06,268,330-->

{@{The concise implementation}@} hinges on {@{several features of Scala's collection library}@}: \(annotation: 4 items: {@{concise, fast, safe, universal}@}\) <!--SR:!2026-10-20,276,330!2026-09-20,252,330!2026-10-29,285,330-->

- _concise_ ::@:: A single for-comprehension or higher-order function replaces multiple nested loops. As a result, few steps are needed. <!--SR:!2026-10-10,270,330!2026-10-21,277,330-->
- _fast_ ::@:: Operations on collections may be optimized and parallelized. <!--SR:!2026-10-23,279,330!2026-10-14,274,330-->
- _safe_ ::@:: The type checker guarantees that collections are manipulated in a valid way. <!--SR:!2026-10-09,269,330!2026-09-08,240,330-->
- _universal_ ::@:: The API interfaces exposed by lists, vectors, sets, maps, etc. are almost the same. <!--SR:!2026-10-22,278,330!2026-10-19,275,330-->

These qualities illustrate why {@{immutable Scala collections}@} are considered {@{a powerful tool for modern software development}@}. <!--SR:!2026-10-23,279,330!2026-10-12,272,330-->

## database

{@{The Scala _for_ notation}@} is a concise syntax for expressing {@{compositional queries over collections}@}. {@{Its semantics}@} are essentially equivalent to {@{the map–flatMap–filter pipeline}@} that underlies {@{many database query languages}@}, and it can be applied to {@{any type that supplies `map`, `flatMap` and `withFilter` \(lazy version of `filter`\)}@}. <!--SR:!2026-09-12,244,330!2026-09-04,236,330!2026-09-13,245,330!2026-11-07,293,330!2026-10-20,276,330!2026-09-23,255,330-->

Consider {@{a simple in-memory catalog of books}@} represented as {@{a list}@}: <!--SR:!2026-08-29,230,330!2026-10-29,285,330-->

> [!example] __database__
>
> Consider {@{a simple in-memory catalog of books}@} represented as {@{a list}@}:
>
> ```Scala
> case class Book(title: String, authors: List[String])
> val books: List[Book] = List(
>   Book("Structure and Interpretation of Computer Programs",
>        List("Abelson, Harald", "Sussman, Gerald J.")),
>   Book("Introduction to Functional Programming",
>        List("Bird, Richard", "Wadler, Phil")),
>   Book("Effective Java", List("Bloch, Joshua")),
>   Book("Java Puzzlers", List("Bloch, Joshua", "Gafter, Neal")),
>   Book("Programming in Scala",
>        List("Odersky, Martin", "Spoon, Lex", "Venners, Bill")))
> ```
<!--SR:!2026-08-30,231,330!2026-11-06,292,330-->

### simple database queries

To retrieve {@{the titles of books written by an author}@} whose {@{name begins with "Bird"}@}, one can write: <!--SR:!2026-09-17,249,330!2026-11-05,291,330-->

> [!example] __simple database query filtering by author__
>
> To retrieve {@{the titles of books written by an author}@} whose {@{name begins with "Bird"}@}, one can write:
>
> ```Scala
> for {
>   b <- books
>   a <- b.authors
>   if a.startsWith("Bird,")
> } yield b.title
> ```
<!--SR:!2026-10-15,275,330!2026-10-10,270,330-->

The same syntax can be used to {@{find all books whose title}@} contains {@{the word "Program"}@}: <!--SR:!2026-09-20,252,330!2026-10-12,272,330-->

> [!example] __simple database query filtering by title__
>
> The same syntax can be used to {@{find all books whose title}@} contains {@{the word "Program"}@}:
>
> ```Scala
> for (b <- books if b.title.indexOf("Program") >= 0) yield b.title
> ```
<!--SR:!2026-10-10,270,330!2026-10-11,271,330-->

### complex database queries

{@{A slightly more involved query}@} finds {@{authors}@} who appear in {@{at least two distinct book records}@}: <!--SR:!2026-10-19,275,330!2026-10-12,272,330!2026-09-15,247,330-->

> [!example] __complex database query filtering by author with duplicates__
>
> {@{A slightly more involved query}@} finds {@{authors}@} who appear in {@{at least two distinct book records}@}:
>
> ```Scala
> for {
>   b1 <- books
>   b2 <- books
>   if b1 != b2
>   a1 <- b1.authors
>   a2 <- b2.authors
>   if a1 == a2
> } yield a1
> ```
<!--SR:!2026-09-01,233,330!2026-11-07,293,330!2026-10-08,268,330-->

Running {@{this against the sample list}@} returns {@{each qualifying author twice}@}, because {@{the pair of book records}@} can be {@{ordered in two ways}@}. To {@{eliminate duplicates}@} we may {@{impose an ordering on the books}@} by {@{changing `if b1 != b2` to `b1.title < b2.title`}@}. However, {@{an author who has written three books}@} will still {@{appear three times}@}, as there are {@{3 ways to choose 2 books from 3 books}@}.  {@{A straightforward remedy}@} is to {@{call `distinct` on the result}@}: <!--SR:!2026-10-25,281,330!2026-09-09,241,330!2026-10-24,280,330!2026-08-27,228,330!2026-10-09,269,330!2026-10-15,275,330!2026-10-30,286,330!2026-09-23,255,330!2026-10-15,275,330!2026-09-09,241,330!2026-11-05,291,330!2026-10-31,287,330-->

> [!example] __complex database query filtering by author__
>
> However, {@{an author who has written three books}@} will still {@{appear three times}@}, as there are {@{3 ways to choose 2 books from 3 books}@}.  {@{A straightforward remedy}@} is to {@{call `distinct` on the result}@}:
>
> ```Scala
> val repeated = for {
>   b1 <- books
>   b2 <- books
>   if b1.title < b2.title
>   a1 <- b1.authors
>   a2 <- b2.authors
>   if a1 == a2
> } yield a1
> repeated.distinct  // removes duplicate author names
> ```
<!--SR:!2026-09-05,237,330!2026-10-11,271,330!2026-11-01,288,330!2026-11-02,289,330!2026-10-20,276,330-->

{@{An alternative to avoid duplicate book results}@} is to use {@{a `Set` to store the starting collection `books`}@}. Remember {@{`for` expressions}@} {@{desugar to `map`, `flatMap`, and `withFilter`}@}. Since these operations {@{usually return the same type as that of the original collection}@}, this means {@{the resulting type of `repeated` is a `Set` as well}@}, which {@{automagically deduplicates}@}. In most cases, {@{a `for` expression}@} returns {@{the same type as the starting collection type}@}. <!--SR:!2026-10-19,275,330!2026-10-20,276,330!2026-09-07,239,330!2026-10-12,272,330!2026-10-15,275,330!2026-09-10,242,330!2026-09-14,246,330!2026-10-14,274,330!2026-09-13,245,330-->

### translating queries to higher-order functions

{@{The query}@} that extracts {@{titles of books}@} with an author whose {@{name starts with "Bird"}@} can be expressed using higher-order functions as: <!--SR:!2026-10-26,282,330!2026-11-03,290,330!2026-10-16,276,330-->

> [!example] __simple database query filtering by author__
>
> {@{The query}@} that extracts {@{titles of books}@} with an author whose {@{name starts with "Bird"}@} can be expressed using higher-order functions as:
>
> ```Scala
> books.flatMap(b =>
>   b.authors.withFilter(a => a.startsWith("Bird")).map(_ => b.title))
> ```
<!--SR:!2026-09-05,237,330!2026-09-07,239,330!2026-07-06,176,310-->
