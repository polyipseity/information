---
aliases:
  - COMP 3031 Scala
  - COMP 3031 Scala 3
  - COMP3031 Scala
  - COMP3031 Scala 3
  - HKUST COMP 3031 Scala
  - HKUST COMP 3031 Scala 3
  - HKUST COMP3031 Scala
  - HKUST COMP3031 Scala 3
  - Scala
  - Scala 3
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/Scala_3
  - language/in/English
---

# Scala 3

- HKUST COMP 3031

{@{__Scala__}@} is {@{a strongly statically typed high-level general-purpose programming language}@} that supports {@{both object-oriented programming and functional programming}@}. <!--SR:!2025-12-04,62,310!2025-12-03,61,310!2025-12-03,61,310-->

## types

Every piece of data in Scala has {@{a type}@}. <!--SR:!2025-11-28,57,310-->

### primitive types

{@{Primitive types}@} are {@{the most basic types in Scala}@} and {@{make up all other types}@}. The list of primitive types are {@{as in Java}@}, but {@{are capitalized}@}. <!--SR:!2025-12-04,62,310!2025-11-29,58,310!2025-12-10,67,310!2025-12-07,64,310!2025-11-29,58,310-->

- `Boolean` ::@:: Either true or false. Example: `true`, `false` <!--SR:!2025-12-06,63,310!2025-11-29,58,310-->
- `Char` ::@:: A single character. Example: `'a'`, `'3'`, `' '` <!--SR:!2025-11-26,55,310!2025-12-10,67,310-->
- `Double` ::@:: A floating point number with double precision \(15 to 17 significant figures\). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14` <!--SR:!2025-11-28,57,310!2025-12-09,66,310-->
- `Float` ::@:: A floating point number with single precision \(6 to 9 significant figures\). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F` <!--SR:!2025-12-07,64,310!2025-11-25,54,310-->
- `Int` ::@:: An integer. Example: `42` <!--SR:!2025-12-06,63,310!2025-12-05,63,310-->

## function types

{@{Function types}@} are written as {@{`(<arg type 1>, ... <arg type N>) => <return type>`}@}. If {@{there is exactly 1 argument}@}, then {@{parentheses \(`()`\) are optional}@}. <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350-->

Functions types that {@{accept no arguments}@} are written as {@{`() => <return type>`}@}. Compare this with {@{call-by-name syntax `=> <return type>`}@}. <!--SR:!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350-->

{@{_Currying_ a multiple argument function}@} converts {@{the function into a sequence of functions that each takes a single argument}@}. The curried function type is {@{`<arg type 1> => ... => <arg type N> => <return type>`}@}. To support this, {@{function type}@} is {@{right-associative}@}, i.e. {@{`A => B => C` is `A => (B => C)`}@}. <!--SR:!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350-->

## classes

To declare {@{a class}@}, use the keyword {@{`class`}@}. Conceptually, classes represent {@{a data type}@}. A class has {@{a constructor}@}, which {@{creates instances or objects of that class}@}. When defining a class, {@{two entities}@} are created: {@{the type and its constructor}@}, both of which {@{have the same name}@}. This is {@{okay}@} since they are in {@{different _namespaces_ \(type namespace and value namespace, respectively\)}@}. The correct entity will be chosen depending on {@{the use context}@}. <!--SR:!2025-10-25,19,350!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350!2025-10-26,20,359-->

The class concept in Scala is more alike to {@{a function but with exposed names and a fixed return value and type}@}. Indeed, {@{the constructor of a class}@} is represented using {@{a function-like syntax}@}: {@{parameter lists}@} are used, e.g. {@{`class T(a: A, ..., z: Z): <expr>`, `class T(a: A, ..., z: Z) { <expr> }`, etc.}@} It even supports {@{call-by-name arguments}@} and {@{[multiple parameter lists](#multiple%20parameter%20lists)}@}, e.g. {@{`class T(a: A)(b: B)...(z: Z): <expr>`, `class T(a: A)(b: B)...(z: Z): { <expr> }`, etc.}@} Its body can contain {@{any expression you can put in a function}@}. When {@{the constructor is run}@}, the expressions in the body are {@{run as if it is in a function from top to bottom}@}. The major differences are {@{any names _directly_ under the class are exposed via the object}@} unless {@{you use the `private` keyword}@}; and {@{the return value and type is always the constructed object and class itself respectively}@}, instead of {@{the last expression}@}. Thus, {@{the _substitution model_}@} can be used for classes as well when {@{reasoning about their execution}@}. <!--SR:!2025-10-19,13,339!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-19,13,339!2025-10-26,20,359!2025-10-25,19,350!2025-10-19,13,339!2025-10-25,19,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-19,13,339!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350!2025-10-26,20,359-->

Thus, {@{names _directly_ under the class}@} are called {@{_members_}@}. {@{Names associated with values}@} are called {@{_data}@}. {@{Names associated with functions}@} are called {@{_methods_}@}. The keyword {@{`private`}@} is used to {@{hide names directly under the class}@}. From {@{the user of the class}@}, {@{`private` members do not exist}@}, so we can {@{change, add, or remove them}@} without {@{affecting the user}@}. This is {@{one of the advantage}@} of {@{_data abstraction_}@}. <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-19,13,339!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350-->

To {@{construct a class}@}, simply {@{call it like a function, e.g. `T()`}@} or {@{prepend the optional `new`, e.g. `new T()`}@}. `new` is {@{mandatory when there is another non-type entity, e.g. function of the same name, in the same value namespace}@}. Indeed, <!--SR:!2025-10-25,19,359!2025-10-26,20,359!2025-10-25,19,359!2025-10-19,13,339-->

To {@{access a member \(data or method\) of an object of a class}@}, use the syntax {@{`<instance>.<member name>`}@}, e.g. {@{`a.b`, `a.c()`, etc.}@} <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350-->

To {@{refer to the current object inside the class expression}@}, use {@{the keyword `this`}@}. When {@{referring to a member of the current object}@}, `this` {@{can be omitted when unambiguous}@}. Ambiguous cases include a method having {@{a parameter of the same name as a data member}@}. `this` is also used to {@{call other constructors of the current class and define auxiliary constructors}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359-->

{@{Auxiliary constructors}@} provide {@{other ways to construct the same type apart from the \(primary\) constructor}@}. To {@{define auxiliary constructor}@}, add {@{a method but with the name `this`}@}. Its body expression should {@{start with `this(...)`, which calls either the primary constructor or other auxiliary constructors}@}. Then the rest can be {@{any expression valid in a function body}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359-->

## expressions

Scala supports {@{expressions}@}, including {@{arithmetic expressions}@}. {@{Parentheses \(`()`\)}@} can be used to {@{prioritize evaluating some expressions over others first}@}. {@{Semicolons \(`;`\) to end an expression}@} are {@{optional in most cases}@}. You need it if you {@{put multiple expressions in one line}@}. <!--SR:!2025-12-04,62,310!2025-12-04,62,310!2025-12-05,63,310!2025-11-28,57,310!2025-11-27,56,310!2025-12-05,63,310!2025-11-28,57,310-->

Scala supports {@{conditional expressions}@}. Its syntax is {@{`if <predicate> then <expr if true> else <expr if false>`}@}. `<predicate>` is {@{always evaluated}@}. If {@{it is `true`}@}, then {@{`<expr if true>` is evaluated}@}. Else, {@{`<expr if false>` is evaluated}@}. <!--SR:!2025-12-08,65,310!2025-12-08,65,310!2025-12-03,61,310!2025-11-25,54,310!2025-11-28,57,310!2025-12-06,63,310-->

Scala supports {@{logical expressions}@}. They are {@{as in Java}@}, and includes {@{`true`, `false`, `!<expr>`, `<expr 1> && <expr 2>`, and `<expr 1> || <expr 2>`}@}. Evaluation uses {@{short circuiting}@}: If {@{`<expr 1>` evaluates to `true`}@}, then {@{`<expr 2>` is not evaluated in `<expr 1> || <expr 2>`}@}; if {@{`<expr 1>` evaluates to `false`}@}, then {@{`<expr 2>` is not evaluated in `<expr 1> && <expr 2>`}@}. <!--SR:!2025-11-26,55,310!2025-12-04,62,310!2025-11-25,54,310!2025-12-10,67,310!2025-12-10,67,310!2025-12-03,61,310!2025-12-05,63,310!2025-12-04,62,310-->

Scala supports {@{comparisons}@}. They are {@{as in Java}@}. <!--SR:!2025-12-07,64,310!2025-11-29,58,310-->

### anonymous functions

{@{Anonymous functions}@} allow us to {@{define functions without _naming_ them}@}. The full syntax is {@{`(<arg name 1>: <arg type 1>, ..., <arg name N>: <arg type N>) => <expr>`}@}. {@{The return type}@} {@{cannot be specified and is inferred from `<expr>`}@}. {@{The argument types}@} {@{can be omitted if it can be inferred}@}, e.g. {@{when defining an anonymous function to pass to an argument in a function call}@}. If {@{there is exactly 1 argument with an omitted argument type}@}, then {@{parentheses \(`()`\) are optional}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-18,12,330!2025-10-25,19,359!2025-10-25,19,350-->

For some reason, {@{call-by-name syntax}@} {@{does not work with anonymous functions}@}. <!--SR:!2025-10-26,20,359!2025-10-26,20,359-->

It can be treated as {@{_syntactic sugar_}@} for the following more verbose syntax: {@{`{ def f(<arg name 1>: <arg type 1>, ..., <arg name N>: <arg type N>) = <expr>; f }`}@} <!--SR:!2025-10-25,19,350!2025-10-26,20,359-->

## definitions

To {@{give a name `<name>`}@} to {@{an expression `<expr>`}@}, use {@{`def <name>: <type> = <expr>`}@}. {@{`<type>`}@} is {@{optional if the type of `<expr>` can be _inferred_}@}. In particular, if {@{`<expr>` uses `<name>` \(recursion\)}@}, then {@{the type of `<expr>` needs to be specified}@}. Note that {@{`<expr>`}@} is not evaluated when {@{`<name>` is defined}@}. To {@{evaluate `<expr>` when `<name>` is defined}@}, use {@{`val` instead of `def`}@}. <!--SR:!2025-11-29,58,310!2025-11-28,57,310!2025-12-06,63,310!2025-12-08,65,310!2025-12-09,66,310!2025-12-03,61,310!2025-12-06,63,310!2025-11-28,57,310!2025-12-08,65,310!2025-11-27,56,310!2025-12-05,63,310-->

Expressions can be {@{parameterized}@}. Use {@{`def <name>(<parm name 1>: <parm type 1>, ... <parm name N>: <parm type N>): <return type> = <expr>`}@}. {@{`<return type>`}@} is {@{optional if the type of `<expr>` can be _inferred_}@}. Expressions are evaluated by {@{replacing each occurrence of `<para name K>` by the actual parameters}@} when {@{the function is evaluated \(see [§ evaluation](#evaluation)\)}@}. <!--SR:!2025-11-28,57,310!2025-11-19,46,290!2025-12-07,64,310!2025-12-04,62,310!2025-12-09,66,310!2025-12-04,62,310-->

### multiple parameter lists

Scala 3 supports {@{multiple parameter lists}@}, e.g. {@{`def <name>(<param list 1>)...(<param list N>): <return type> = <expr>`}@}. <!--SR:!2025-10-25,19,359!2025-10-26,20,359-->

When {@{you call the function \(function application\)}@}, you need to {@{provide _all_ arguments in _all_ parameter lists}@} with {@{the _same_ grouping as the function parameter lists}@} too. To support this, {@{function application}@} is {@{left-associative}@}, i.e. {@{`f(a)(b)` is `(f(a))(b)`}@}. <!--SR:!2025-10-25,19,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359-->

Strictly speaking, {@{multiple parameter lists}@} is {@{distinct from _currying_}@}. However, if {@{you use one parameter list for each argument}@}, then you are {@{currying a function}@} by converting {@{the function into a sequence of functions that each takes a single argument}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-18,12,330!2025-10-25,19,350!2025-10-25,19,350-->

### extension methods

{@{Extension methods}@} define {@{extra members to a class while being outside the class definition}@}. They are useful for {@{adding utility methods to a class}@}. To define an extension, start with the syntax {@{`extension (<arg name>: <arg type>)`}@}, and then {@{start a newline and indent}@} to {@{add the extra methods}@}. <!--SR:!2025-10-26,20,359!2025-10-18,12,339!2025-10-25,19,350!2025-10-19,13,339!2025-10-26,20,359!2025-10-25,19,350-->

When {@{defining extension methods}@}, they cannot {@{access `private` members of the class}@}. They also cannot {@{access `this`}@} but must use {@{the name defined in the starting `extension` line}@}. <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359-->

To {@{call extension methods}@}, they need to be {@{visible in the calling context}@}. {@{The exact rules}@} are {@{hard to explain now}@}, and some common cases are {@{companion object of the type \(code `object <name>` where `<name>` is the same as that of the type\)}@} and {@{defined or imported in the current scope}@}. <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359-->

## evaluation

The {@{2 major evaluation strategies for functions}@} are {@{call by value \(CBV\) and call by name \(CBN\)}@}. Scala by default uses {@{CBV}@}. To {@{specify CBN for a particular parameter}@}, {@{specify the type using `=> <type>` instead of `<type>`}@}. <!--SR:!2025-12-03,61,310!2025-11-29,58,310!2025-12-07,64,310!2025-12-08,65,310!2025-12-03,61,310-->

### tail recursion

Scala 3 optimizes {@{_direct_ tail calls to the _current_ function}@} by {@{reusing the current stack frame}@}. To ensure {@{this optimization occurs}@}, {@{annotate the function with `@scala.annotation.tailrec`}@}. This will {@{cause a compilation error if the optimization cannot be applied}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359-->

## scoping

Scala {@{creates a new scope}@} using {@{braces \(`{}`\)}@}. Since {@{Scala 3}@}, {@{indentation after `=`, `then`, `else`, etc. can be used as well \(like Python\)}@}. The {@{last element \(statement\) of a scope}@} is {@{the expression that determines the value of that scope}@}. The motivation of scoping is to {@{avoid _namespace pollution_}@}. <!--SR:!2025-11-26,55,310!2025-11-27,56,310!2025-11-29,58,310!2025-12-03,61,310!2025-12-03,61,310!2025-11-26,55,310!2025-12-05,63,310-->

Scala uses {@{lexical scoping}@} with {@{\(variable\) shadowing}@}. That is, {@{each occurrence of a name}@} refers to {@{the definition of the name appearing in the _innermost_ scope \(shadowing\) according to the _source code_ \(lexical scoping\)}@}. <!--SR:!2025-12-07,64,310!2025-12-05,63,310!2025-11-27,56,310!2025-12-04,62,310-->

Scala supports {@{_optional_ end markers}@} to {@{mark the end of a scope}@}. It must have {@{the same indentation as the opening keyword}@}.  The end marker has the syntax {@{`end <name or keyword>`}@}, using {@{`<name>` if the scope is named \(e.g. classes, functions, etc.\)}@} or {@{repeat the starting keyword if not}@}. <!--SR:!2025-12-10,67,310!2025-12-05,63,310!2025-12-09,66,310!2025-10-26,20,359!2025-10-18,12,330!2025-10-25,19,350-->

## syntax

### identifiers

In Scala, {@{identifier names}@} are {@{much more relaxed}@} compared to {@{most other programming languages}@}. An identifier can {@{start with a letter \(`_` is also a letter\) or symbols}@}. Then it can be followed by {@{any combination of letters, symbols, or digits}@}. <!--SR:!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350-->

### infix notation

Normally, to {@{call a function}@}, you use the syntax {@{`a.f(...)`}@}, known as {@{the _dot notation_}@}. If your function {@{accepts exactly 1 argument `b`}@}, you can opt to use the syntax {@{`a f b`}@}, known as {@{the _infix notation_}@}, to call the function. To do so, {@{prepend `infix` before `def` in the function definition}@}. <!--SR:!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350-->

Since {@{identifier names in Scala}@} is {@{much more relaxed}@}, this, coupled with {@{infix notation}@}, allows you to {@{"overload" operators}@}. <!--SR:!2025-10-25,19,359!2025-10-25,19,350!2025-10-25,19,350!2025-10-25,19,350-->

With {@{infix notation}@}, this is {@{ambiguity with _precedence_}@}. In Scala, {@{the precedence of an infix function call}@} is based on {@{the _first_ character of the infix function name}@}. Starting from {@{the highest priority \(parenthesized first\)}@}, we have {@{any other special characters not listed below}@}, then {@{precedence rules for common operators similar to other programming languages}@} \({@{multiply, divide, modulus}@} &gt; {@{addition, subtraction}@} &gt; {@{colon \(`:`\)}@} &gt; {@{equality and inequality}@} &gt; {@{comparison}@} &gt; {@{and}@} &gt; {@{xor}@} &gt; {@{or}@}\), and finally {@{all other letters \(including `_`\)}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350!2025-10-18,12,330!2025-10-25,19,350!2025-10-26,20,359!2025-10-26,20,359!2025-10-26,20,359-->

## pre-definitions

The Scala {@{`Predef` object}@} provides {@{definitions that are accessible without explicit quantification}@}. They contain {@{useful utilities}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359-->

### checking

Scala provides {@{several functions}@} to check {@{preconditions, assertions, and more}@}. They {@{throw an error \(but of a different type\)}@} when {@{a condition fails}@}, optionally with {@{an error message}@}. They are used {@{in different situations}@}. <!--SR:!2025-10-25,19,350!2025-10-25,19,350!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350-->

{@{Preconditions}@} are used to {@{ensure arguments to a class or function}@} satisfies {@{certain constraints}@}. The syntax is {@{`require(<precondition>[, <message>])`}@}. It throws {@{`IllegalArgumentException`}@} if {@{`<precondition>` is false}@}. <!--SR:!2025-10-26,20,359!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,359!2025-10-26,20,359!2025-10-25,19,350-->

{@{Assertions}@} are used to {@{ensure a condition}@} is {@{satisfied in a general context}@}. The syntax is {@{`assert(<assertion>[, <message>])`}@}. It throws {@{`AssertionError`}@} if {@{`<assertion>` is false}@}. <!--SR:!2025-10-26,20,359!2025-10-25,19,350!2025-10-26,20,359!2025-10-25,19,350!2025-10-25,19,350!2025-10-26,20,359-->
