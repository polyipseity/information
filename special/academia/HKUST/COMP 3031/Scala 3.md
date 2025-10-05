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

{@{__Scala__}@} is {@{a strongly statically typed high-level general-purpose programming language}@} that supports {@{both object-oriented programming and functional programming}@}.

## entry points

Unlike {@{the interactive REPL or worksheet}@}, {@{a _stand‑alone_ Scala application}@} is packaged as {@{a compiled class that can be launched from the command line}@}. {@{Every executable program}@} must expose {@{an entry point}@}—typically {@{a `main` method inside an object}@}.

### traditional entry points

> [!example] __example__
>
> {@{This pattern}@} mirrors {@{Java's classic `public static void main(String[] args)`}@}.
>
> ```Scala
> object Hello {
>  def main(args: Array[String]): Unit =
>     println("hello world!")
> }
> ```

- __Object__ ::@:: – The container for the static‑like entry point.
- __Main signature__ ::@:: – `def main(args: Array[String]): Unit` is required; it receives command‑line arguments as a string array and returns `Unit`.
- __Invocation__ ::@:: – After compilation, run with `scala Hello`.

### annotated entry points

{@{Scala 3}@} introduces {@{the `@main` annotation}@} to {@{simplify program entry points}@}. {@{A top‑level function annotated with `@scala.annotation.main`}@} becomes {@{an executable}@}:

> [!example] __example__
>
> {@{A top‑level function annotated with `@main`}@} becomes {@{an executable}@}:
>
> ```Scala
> import scala.annotation.main
>
> @main def birthday(name: String, age: Int): Unit =
>   println(s"Happy birthday, $name! $age years old already!")
> ```

- __Parameters__ ::@:: – Each parameter corresponds to a command‑line argument.
- __Automatic conversion__ ::@:: – Argument types are inferred from the function signature (e.g., `String`, `Int`).
- __Invocation__ ::@:: – Compile and run with `scala birthday Peter 11`.

{@{The annotated function}@} automatically generates {@{a `main` method}@}, {@{eliminating boilerplate}@}.

## type system

Every piece of data in Scala has {@{a type}@}.

### primitive types

{@{Primitive types}@} are {@{the most basic types in Scala}@} and {@{make up all other types}@}. The list of primitive types are {@{as in Java}@}, but {@{are capitalized}@}.

- `Boolean` ::@:: Either true or false. Example: `true`, `false`
- `Char` ::@:: A single character. Example: `'a'`, `'3'`, `' '`
- `Double` ::@:: A floating point number with double precision \(15 to 17 significant figures\). One can effectively treat it as a decimal number for most purposes. Example: `42d`, `5.`, `6.29d`, `3.12D`, `3.14`
- `Float` ::@:: A floating point number with single precision \(6 to 9 significant figures\). One can effectively treat it as a decimal number for most purposes. Example: `42f`, `1.f`, `3.14f`, `9.20F`
- `Int` ::@:: An integer. Example: `42`

{@{This categorization of "primitive types"}@} is not {@{very _rigorous_}@}. See {@{_top types_}@} instead.

### function types

{@{Function types}@} are written as {@{`(<arg type 1>, ... <arg type N>) => <return type>`}@}. If {@{there is exactly 1 argument}@}, then {@{parentheses \(`()`\) are optional}@}.

Functions types that {@{accept no arguments}@} are written as {@{`() => <return type>`}@}. Compare this with {@{call-by-name syntax `=> <return type>`}@}.

{@{_Currying_ a multiple argument function}@} converts {@{the function into a sequence of functions that each takes a single argument}@}. The curried function type is {@{`<arg type 1> => ... => <arg type N> => <return type>`}@}. To support this, {@{function type}@} is {@{right-associative}@}, i.e. {@{`A => B => C` is `A => (B => C)`}@}.

#### function type variance

{@{A unary function type `A => B`}@} is {@{__contravariant__ in its parameter type `A`}@} and {@{__covariant__ in its result type `B`}@}. Formally, for {@{any types `A1`, `A2`, `B1`, `B2`}@} we have {@{`If A2 <: A1 and B1 <: B2 then A1 => B1 <: A2 => B2`}@}. The rule can be read as: a function that accepts {@{a _more general_ argument (`A1`)}@} and produces {@{a _more specific_ result (`B1`)}@} is itself {@{more specialized than one}@} that accepts {@{a _specific_ argument (`A2`)}@} and returns {@{a _general_ result (`B2`)}@}.

For example, {@{`AnyVal => Orange`}@} is {@{a subtype of `Int => Fruit`}@}, because {@{the parameter type `AnyVal` is a supertype of `Int`}@} and {@{the result type `Orange` is a subtype of `Fruit`}@}.

When a function has {@{several parameters}@}, {@{each parameter's variance}@} is {@{considered independently}@}. {@{The general rule for _n_‑ary functions}@} is that the overall function type is {@{contravariant in all argument positions}@} and {@{covariant in the result}@}. This may be derived by {@{currying the _n_-ary function}@}. Curried functions are {@{simply nested unary functions}@}. {@{Variance rules}@} apply {@{at each level}@}: {@{`f: (A, B) => C  ≡  f : A => B => C  ≡  f : A => (B => C)`}@}. For {@{the outermost function}@}, {@{`A` is contravariant while `B => C` is covariant}@}. {@{Covariance of `B => C`}@} means that {@{`B` is contravariant and `C` is covariant}@}. Thus {@{`AnyVal => AnyRef => Orange`}@} can be used where {@{an `Int => String => Fruit` is required}@}.

The above {@{nested application of variance}@} also applies if function types are used as {@{argument types of another function type}@}.

### top types

At {@{the apex}@} of Java's \(not Scala's\) type system sits {@{`java.lang.Object`}@}, the root of {@{all Java‑based classes}@}. {@{Above and beneath}@} this, Scala introduces {@{three core abstract types}@} that form {@{the foundation for its own hierarchy}@}.

- `scala.Any` ::@:: The ultimate base type of every value in Scala (both primitives and references). Key methods include `==`, `!=`, `equals`, `hashCode`, `toString`.
- `scala.AnyRef` ::@:: Alias for `java.lang.Object`; the root of all reference types. Inherited by Java and Scala classes.
- `scala.AnyVal` ::@:: Base type for all value types (the Scala equivalents of Java primitives). Provides a lightweight, non‑boxed representation.

{@{These three types}@} form {@{a _diamond_ at the top of the hierarchy}@}: {@{`scala.Any`}@} is {@{the supertype of both `scala.AnyRef` and `scala.AnyVal`}@}, and these two subtypes are {@{otherwise disjoint}@}.

### nothing type

At {@{the opposite extreme}@} lies {@{`scala.Nothing`}@}, {@{a _bottom type_}@} that is {@{a subtype of every other type in Scala}@}. Although it has {@{no runtime representation}@}—there is {@{never an actual value of type `Nothing`}@}—it plays {@{a pivotal role}@}: \(annotation: 2 items: {@{abnormal termination, empty collections}@}\)

- __Abnormal termination__ ::@:: – Functions that throw exceptions or otherwise terminate abruptly can be typed as returning `Nothing`.
- __Empty collections__ ::@:: – An empty list, for example, can be given the type `List[Nothing]`, which is then safely subtyped to any `List[T]`.

Because {@{`Nothing` can inhabit any type position}@}, it provides a powerful tool for expressing {@{impossibility or divergence within Scala's static type system}@}.

### type inference

{@{Scala's compiler}@} performs {@{_type inference_}@} by examining {@{the syntactic structure of an expression}@} and determining {@{the most specific type that can represent all possible values it may evaluate to}@}. For {@{complex expressions such as conditionals}@}, the compiler follows {@{a two‑step process}@}: \(annotation: 2 items: {@{infer branches → compute least upper bound}@}\)

1. __Infer the types of each branch__ ::@:: – Each `then` and `else` clause is typed independently in the surrounding context.
2. __Compute the least upper bound (LUB)__ ::@:: – The resulting type of the conditional is the _least common supertype_ of the two branch types, the smallest type that subsumes both.

If one branch's type {@{cannot be a subtype of the other}@}, Scala may {@{widen to a more general type}@} or, in {@{certain contexts}@}, resort to {@{intersection types}@}. However, for {@{simple cases involving primitive values}@}, {@{the LUB}@} is usually {@{a value class such as `AnyVal`}@}.

> [!example] __example__
>
> Example: {@{`if true then 1 else false`}@}
>
> - {@{The _then_ branch}@} contains {@{the integer literal `1`}@}, which has {@{type `Int`}@}.
> - {@{The _else_ branch}@} contains {@{the boolean literal `false`}@}, which has {@{type `Boolean`}@}.
>
> {@{`Int` and `Boolean`}@} are both {@{direct subclasses of `AnyVal`}@}. {@{Their least upper bound}@} is therefore {@{`AnyVal`}@}. Consequently, {@{the compiler}@} infers {@{the entire conditional expression to have type `AnyVal`}@}, not {@{`Int`, `Boolean`, `Object`, or `Any`}@}.

{@{The inference algorithm}@} guarantees that {@{the resulting type}@} can represent {@{every possible runtime value of the expression}@} while remaining {@{as specific as the language’s type hierarchy permits}@}.

#### type inference in generics

When {@{a generic function is invoked}@}, the compiler examines {@{the concrete arguments supplied at call site}@} and deduces {@{the appropriate type parameter automatically}@}.

> [!example] __example__
>
> Consider {@{the previously defined `singleton` factory}@}:
>
> ```Scala
> def singleton[T](elem: T): List[T] = Cons(elem, Nil)
> ```
>
> Instead of {@{explicitly naming the type argument}@}, a programmer can {@{simply write}@}:
>
> ```Scala
> val intList   = singleton(1)      // inferred as List[Int]
> val boolList  = singleton(true)   // inferred as List[Boolean]
> ```

The compiler infers {@{`T` to be `Int` or `Boolean`}@} respectively by inspecting {@{the type of the argument}@}. {@{This inference mechanism}@} {@{reduces verbosity and keeps code concise}@}, while still guaranteeing that {@{the resulting list's element type matches the supplied value}@}.

Inference is {@{not always possible}@}; if a function has {@{multiple polymorphic parameters whose types are interdependent}@} or if {@{no arguments provide enough information}@}, the programmer must {@{specify the type explicitly}@}. However, for {@{most common patterns—especially single‑parameter generic functions}@}—the compiler can {@{resolve the type without assistance}@}.

Thus, {@{Scala's type inference}@} seamlessly blends with {@{its generics feature}@}, enabling {@{concise yet type‑safe code}@}.

### polymorphism

{@{_Polymorphism_}@} refers to the ability of {@{a function or data structure}@} to handle {@{values of multiple types while preserving type safety}@}. In {@{statically‑typed languages}@} such as Scala, {@{the two principal forms}@} of polymorphism in this context are {@{__subtyping__ itself and __generics__, which provide parametric polymorphism}@}. Understanding {@{how these two interact}@} requires attention to {@{_bounds_ on type variables and to the _variance_ of type constructors}@}.

{@{Subtyping polymorphism}@} is realized when {@{a value of a subtype can be used wherever its supertype is expected}@}, as in treating {@{a `NonEmpty` set where an `IntSet` is required}@}. It captures {@{"is‑a" relationships}@}.

{@{Generic classes and methods}@} achieve {@{parametric polymorphism}@}: {@{`def assertAllPos[S <: IntSet](s: S): S = …`}@} accepts {@{any subtype of `IntSet`}@} and returns {@{the same concrete subtype}@}. {@{Generics (or type parameters)}@} allow us to write {@{code that works uniformly over any type within type bounds}@}.

### type parameters

Defining {@{a separate class \(e.g. `IntList`, `BooleanList`, etc.\) hierarchy}@} for {@{each element type}@} is {@{impractical}@}. Scala solves this by allowing {@{__type parameters__}@}, written in {@{square brackets after the name of a function, a trait, or class}@}. {@{A type parameter}@} behaves like {@{an abstract type}@} that can be {@{instantiated with any concrete type when the class is used}@}.

By parameterising {@{both data structures and functions}@}, Scala achieves {@{full _type safety_ while remaining highly reusable}@}.

#### generic types

By parameterising {@{both data structures and functions}@}, Scala achieves {@{full _type safety_ while remaining highly reusable}@}. {@{The same `List`}@} trait can represent {@{sequences of integers, booleans, user‑defined classes, or even nested lists}@}, all without {@{duplicating code}@}.

> [!example] __example__
>
> ```Scala
> package ppl3
>
> trait List[T] {
>   def isEmpty: Boolean
>   def head: T
>   def tail: List[T]
> }
>
> class Cons[T](val head: T, val tail: List[T]) extends List[T] {
>   def isEmpty = false
> }
>
> class Nil[T] extends List[T] {
>   def isEmpty = true
>   def head = throw new NoSuchElementException("Nil.head")
>   def tail = throw new NoSuchElementException("Nil.tail")
> }
> ```
>
> Here {@{`T`}@} represents {@{the element type}@}. {@{The concrete subclasses `Cons` and `Nil`}@} are {@{parameterised in exactly the same way}@}, ensuring that {@{a `Cons[Int]` can only be paired with another `List[Int]`}@}, and likewise for {@{any other type}@}.

#### generic functions

{@{Functions}@} may also be {@{generic}@} by declaring {@{type parameters in parentheses after the function name}@}:

> [!example] __example__
>
> {@{Functions}@} may also be {@{generic}@} by declaring {@{type parameters in parentheses after the function name}@}:
>
> ```Scala
> def singleton[T](elem: T): List[T] = Cons(elem, Nil)
> ```

{@{This factory method}@} constructs {@{a single‑element list}@} regardless of {@{the element's concrete type}@}. Its usage is {@{explicit}@}:

> [!example] __example__
>
> Its usage is {@{explicit}@}:
>
> ```Scala
> val intList   = singleton[Int](1)      // List[Int]
> val boolList  = singleton[Boolean](true) // List[Boolean]
> ```

{@{The compiler}@} infers {@{the appropriate type parameter in most cases}@}, but it can be {@{supplied explicitly when desired}@}.

#### type bounds

{@{_Upper bounds_}@} constrain {@{a type variable to be a subtype of some type}@}: {@{`[S <: IntSet]`}@}. Conversely, {@{_lower bounds_}@} restrict the variable to be {@{a supertype of a given type: `[S >: NonEmpty]`}@}. {@{Mixed bounds}@} {@{combine both}@}, e.g. {@{`[S >: NonEmpty <: IntSet]`}@}, which narrows `S` to {@{any type between `NonEmpty` and `IntSet`}@}. These bounds are crucial when we want the compiler to {@{infer the most precise return type or to enforce safe substitutions}@}.

> [!example] __example__
>
> Example of {@{an upper‑bounded generic method}@}:
>
> ```Scala
> def assertAllPos[S <: IntSet](s: S): S = if (s.isPositive) s else throw new IllegalArgumentException
> ```
>
> Here {@{`S`}@} can be {@{any concrete subclass of `IntSet`}@}, and the method returns {@{exactly that same subclass}@}.

#### variance

Scala lets us annotate {@{variance explicitly}@}:

> [!example] __example__
>
> Scala lets us annotate variance explicitly:
>
> ```Scala
> class C[+A]  // covariant
> class D[-A]  // contravariant
> class E[A]   // invariant
> ```

{@{A type constructor `C[T]`}@} is {@{_covariant_ (`+T`)}@} if, for {@{all types `A <: B`, we have `C[A] <: C[B]`}@}. This mirrors the intuitive idea that {@{a collection of more specific elements}@} is also {@{a collection of more general ones}@}. For instance, given {@{`NonEmpty <: IntSet`}@}, covariance would imply {@{`List[NonEmpty] <: List[IntSet]`}@}. Covariance is safe for {@{immutable collections where elements are never mutated after construction}@}. It is unsafe for {@{mutable collections that allow element updates}@}.

{@{A type constructor `D[T]`}@} is {@{_contravariant_ (`-T`)}@} if {@{for all types `A <: B`, we have `D[B] <: D[A]` \(note `A` and `B` are reversed\)}@}. This is less intuitive but arises naturally in {@{function types and certain consumer roles}@}. For example, a {@{comparator that can compare any `IntSet`}@} can also compare {@{specifically `NonEmpty` sets}@}, hence {@{`Comparator[IntSet] <: Comparator[NonEmpty]`}@}. Contravariance is safe for {@{types that only consume values of type `T` (e.g., function parameters)}@}. It is unsafe for {@{types that produce values of type `T`}@}.

{@{A type constructor `E[T]`}@} is {@{_invariant_ (no prefix)}@} if {@{neither covariance nor contravariance holds}@}. This is {@{the default}@} and safest choice when {@{neither relationship is appropriate}@}. Invariance is common for {@{mutable collections that both produce and consume elements}@}, as {@{mixing subtypes and supertypes}@} could lead to {@{type errors}@}. For {@{a bad example}@}, see {@{Java arrays \(not Scala arrays\), which are covariant _inappropriately_}@}.

##### variance pitfalls

{@{Java arrays}@} are {@{covariant (`NonEmpty[] <: IntSet[]`)}@}, but this leads to {@{runtime type‑errors}@}:

> [!example] __example__
>
> {@{Java arrays}@} are {@{covariant (`NonEmpty[] <: IntSet[]`)}@}, but this leads to {@{runtime type‑errors}@}:
>
> ```Java
> NonEmpty[] a = new NonEmpty[]{new NonEmpty()};
> IntSet[] b = a;
> b[0] = new Empty();   // compile‑time OK, but fails at run time
> ```

##### variance checks

The compiler enforces {@{_variance checks_}@}: {@{a covariant type parameter}@} may {@{only appear in output positions (method return types)}@}, while {@{a contravariant one}@} may {@{only appear in input positions}@}. If a method {@{violates this rule}@}, the definition is {@{rejected}@}.

To {@{understand this intuitively}@}, consider {@{the Liskov Substitution Principle (LSP)}@}, which states that {@{subtypes must be substitutable for their supertypes}@}: if {@{`A <: B`}@}, then {@{any program using an object of type `B`}@} should work {@{correctly when an object of type `A` is supplied}@}. Variance checks ensure that {@{this principle is upheld}@}.

Consider {@{covariance}@}: if {@{`C[+T]` is covariant}@}, then {@{`C[A] <: C[B]` for `A <: B`}@}. If `C[T]` had {@{a method that accepted a parameter of type `T`}@}, then `C[A]` would have {@{a method that accepts an `A`}@}. However, since {@{`A <: B`}@}, this method could be {@{called with a `B`}@}, which violates the expectation that {@{`C[A]` only works with `A`}@}. Thus, allowing {@{covariant types to appear in input positions}@} would {@{break substitutability}@}.

Consider {@{contravariance}@}: if {@{`C[-T]` is contravariant}@}, then {@{`C[B] <: C[A]` for `A <: B`}@}. If `C[T]` had {@{a method that returns a `T`}@}, then `C[B]` would have {@{a method that returns a `B`}@}. However, since {@{`A <: B`}@}, this method could be {@{expected to return an `A`}@}, which violates the expectation that {@{`C[B]` only produces `B`}@}. Thus, allowing {@{contravariant types to appear in output positions}@} would also {@{break substitutability}@}.

By enforcing {@{these variance checks}@}, the compiler ensures that {@{the LSP is maintained}@}, preserving {@{type safety and preventing runtime errors}@}.

## classes

To declare {@{a class}@}, use the keyword {@{`class`}@}. Conceptually, classes represent {@{a data type}@}. A class has {@{a constructor}@}, which {@{creates instances or objects of that class}@}. When defining a class, {@{two entities}@} are created: {@{the type and its constructor}@}, both of which {@{have the same name}@}. This is {@{okay}@} since they are in {@{different _namespaces_ \(type namespace and value namespace, respectively\)}@}. The correct entity will be chosen depending on {@{the use context}@}.

The class concept in Scala is more alike to {@{a function but with exposed names and a fixed return value and type}@}. Indeed, {@{the constructor of a class}@} is represented using {@{a function-like syntax}@}: {@{parameter lists}@} are used, e.g. {@{`class T(a: A, ..., z: Z): <expr>`, `class T(a: A, ..., z: Z): { <expr> }`, etc.}@} It even supports {@{call-by-name arguments}@} and {@{[multiple parameter lists](#multiple%20parameter%20lists)}@}, e.g. {@{`class T(a: A)(b: B)...(z: Z): <expr>`, `class T(a: A)(b: B)...(z: Z): { <expr> }`, etc.}@} Its body can contain {@{any expression you can put in a function}@}. When {@{the constructor is run}@}, the expressions in the body are {@{run as if it is in a function from top to bottom}@}. The major differences are {@{any names _directly_ under the class are exposed via the object}@} unless {@{you use the `private` keyword}@}; and {@{the return value and type is always the constructed object and class itself respectively}@}, instead of {@{the last expression}@}. Thus, {@{the _substitution model_}@} can be used for {@{classes without _side effects_}@} as well when {@{reasoning about their execution}@}.

Thus, {@{names _directly_ under the class}@} are called {@{_members_}@}. {@{Names associated with values}@} are called {@{_data_}@}. {@{Names associated with functions}@} are called {@{_methods_}@}. The keyword {@{`private`}@} is used to {@{hide names directly under the class}@}. From {@{the user of the class}@}, {@{`private` members do not exist}@}, so we can {@{change, add, or remove them}@} without {@{affecting the user}@}. This is {@{one of the advantage}@} of {@{_data abstraction_}@}.

To {@{construct a class}@}, simply {@{call it like a function, e.g. `T()`}@} or {@{prepend the optional `new`, e.g. `new T()`}@}. `new` is {@{mandatory when there is another non-type entity in the same value namespace}@}, e.g. {@{function of the same name}@}.

To {@{access a member \(data or method\) of an object of a class}@}, use the syntax {@{`<instance>.<member name>`}@}, e.g. {@{`a.b`, `a.c()`, etc.}@}

To {@{refer to the current object inside the class expression}@}, use {@{the keyword `this`}@}. When {@{referring to a member of the current object}@}, `this` {@{can be omitted when unambiguous}@}. Ambiguous cases include a method having {@{a parameter of the same name as a data member}@}. `this` is also used to {@{call other constructors of the current class and define auxiliary constructors}@}.

{@{Auxiliary constructors}@} provide {@{other ways to construct the same type apart from the \(primary\) constructor}@}. To {@{define auxiliary constructor}@}, add {@{a method but with the name `this`}@}. Its body expression should {@{start with `this(...)`, which calls either the primary constructor or other auxiliary constructors}@}. Then the rest can be {@{any expression valid in a function body}@}.

### abstract classes

In Scala, {@{an _abstract class_}@} serves as {@{a partial blueprint for concrete subclasses}@}. It can declare {@{methods and fields}@} that are {@{either fully implemented or left unimplemented \(abstract\)}@}. {@{The latter}@} are called {@{_abstract members_}@}; they must be {@{supplied by any non‑abstract subclass}@} before {@{objects of that type can be instantiated}@}.

> [!example] __example__
>
> {@{A <!-- classic --> illustration}@} is {@{the design of an integer set abstraction}@}:
>
> ```Scala
> abstract class IntSet {
>   def incl(x: Int): IntSet        // abstract member – no body provided
>   def contains(x: Int): Boolean   // abstract member – no body provided
> }
> ```

Here, {@{`IntSet`}@} declares {@{two operations—adding an element (`incl`) and testing membership (`contains`)}@}. Because {@{the class is marked `abstract`}@}, it {@{cannot be instantiated directly}@}; attempting to {@{write `new IntSet()`}@} would result in {@{a compile‑time error}@}.

> [!example] __example__
>
> Instead, {@{concrete subclasses such as `EmptySet` or `NonemptySet`}@} must {@{provide concrete implementations of these methods}@}:
>
> ```Scala
> class EmptySet extends IntSet {
>   def incl(x: Int): IntSet = new NonemptySet(x, this)
>   def contains(x: Int): Boolean = false
> }
> ```

{@{Only after all abstract members have been implemented}@} does a class become {@{_concrete_ and eligible for instantiation}@}. Abstract classes thus enable {@{the definition of common interfaces}@} while enforcing that {@{subclasses supply the missing behavior}@}.

### inheritance

In Scala, {@{a _class extension_ (or inheritance)}@} allows {@{one class to inherit the members of another}@}.

> [!example] __example__
>
> When {@{implementing sets as binary trees}@}, we typically define {@{two concrete subclasses of an abstract `IntSet`}@}:
>
> ```Scala
> class Empty extends IntSet {
>   def contains(x: Int): Boolean = false
>   def incl(x: Int): IntSet       = NonEmpty(x, new Empty(), new Empty())
> }
> ```
>
> and
>
> ```Scala
> class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
>   def contains(x: Int): Boolean =
>     if (x < elem) left.contains(x)
>     else if (x > elem) right.contains(x)
>     else true
>
>   def incl(x: Int): IntSet =
>     if (x < elem) NonEmpty(elem, left.incl(x), right)
>     else if (x > elem) NonEmpty(elem, left, right.incl(x))
>     else this
> }
> ```

{@{The two subclasses}@} model {@{the empty set and a non‑empty node respectively}@}. {@{This inheritance hierarchy}@} ensures that {@{an instance of `Empty` or `NonEmpty`}@} can be used wherever {@{an `IntSet` is expected}@}.

Because they are {@{immutable}@}, the operations {@{share structure}@}: {@{inserting an element}@} returns {@{a new tree that reuses unchanged sub‑trees (`left` or `right`)}@} rather than {@{copying them}@}.

Some terminology:

- __Superclass / Base class__ ::@:: – The class from which another inherits. <p> _Example:_ `IntSet` is the superclass of both `Empty` and `NonEmpty`.
- __Subclass / Derived class__ ::@:: – A class that extends a superclass. <p> _Example:_ `Empty` and `NonEmpty` are subclasses of `IntSet`.
- __Base classes of a class__ ::@:: – All superclasses, direct or indirect. <p> _Example:_ For `NonEmpty`, the base classes are `IntSet` and Scala’s root `Object`.

When {@{a subclass does not specify a superclass explicitly}@}, Scala implicitly {@{extends `java.lang.Object`}@}.

{@{The concrete definitions of `contains` and `incl`}@} in {@{`Empty` and `NonEmpty`}@} provide {@{the required implementations for the abstract members}@} declared in {@{`IntSet`}@}. Scala also permits {@{_overriding_ an existing, non‑abstract method}@}:

> [!example] __example__
>
> Scala also permits {@{_overriding_ an existing, non‑abstract method}@}:
>
> ```Scala
> abstract class Base {
>   def foo: Int = 1
> }
> class Sub extends Base {
>   override def foo: Int = 2   // redefines Base.foo
> }
> ```

{@{The keyword `override`}@} is {@{mandatory when redefining a concrete member \(but not implementing an abstract member\)}@}, ensuring that {@{accidental overrides are avoided}@}. {@{This mechanism}@} allows subclasses to {@{refine or replace behaviour defined in their superclasses}@} while still adhering to {@{the contract established by the abstract class}@}.

### value parameters

Scala's {@{constructor syntax}@} offers {@{a concise way to declare both __parameters__ and __immutable fields__ simultaneously}@}.

> [!example] __examples__
>
> In {@{the `Cons` class below}@}, {@{the keywords `val` preceding each parameter}@} create {@{read‑only members}@}:
>
> ```Scala
> class Cons(val head: Int, val tail: IntList) extends IntList
> ```
>
> {@{This single line}@} expands into {@{a constructor that takes two arguments (`head`, `tail`)}@} and automatically generates {@{corresponding fields accessible from outside the class}@}. {@{The implicit code}@} generated by the compiler is {@{equivalent to writing}@}:
>
> ```Scala
> class Cons(_head: Int, _tail: IntList) extends IntList {
>   val head = _head
>   val tail = _tail
> }
> ```
>
> Here {@{`_head` and `_tail`}@} are merely {@{local names used only during construction}@}; they are {@{not exposed as public members}@}. By contrast, {@{omitting `val` (or `var`)}@} would {@{produce constructor parameters}@} that are {@{private to the primary constructor}@} and would not become {@{fields of the class}@}.

{@{This shorthand}@} is a powerful feature for defining {@{simple data containers}@} such as {@{case classes or algebraic data types}@}, allowing developers to declare {@{immutable state in one concise expression}@}.

### case classes

In Scala {@{the idiomatic way to model heterogeneous data}@} is {@{through __case classes__}@}. {@{A case class definition}@} is identical to {@{a normal class}@} but is prefixed with the {@{keyword `case`}@}. For example:

> [!example] __example__
>
> {@{A case class definition}@} is identical to {@{a normal class}@} but is prefixed with the {@{keyword `case`}@}. For example:
>
> ```Scala
> abstract class Expr
> case class Number(n: Int) extends Expr
> case class Sum(e1: Expr, e2: Expr) extends Expr
> ```

Unlike {@{ordinary classes}@}, {@{case classes}@} automatically generate {@{structural equality, hash codes, and most importantly pattern‑matching support}@}. {@{The body of each case class}@} is {@{effectively empty}@}; {@{the constructor arguments}@} are treated as {@{immutable fields that can be extracted by patterns}@}.

### enumerations

{@{Pure data structures}@} are those that {@{carry information without any associated behaviour}@}; they exist solely to be {@{composed, decomposed, and examined by other parts of a program}@}. In Scala, {@{__case classes__}@} provide {@{an elegant way to model such data}@}. {@{A typical hierarchy}@} for {@{arithmetic expressions}@} might be written as:

> [!example] __example__
>
> {@{A typical hierarchy}@} for {@{arithmetic expressions}@} might be written as:
>
> ```Scala
> sealed abstract class Expr
> object Expr:
>   case class Var(s: String) extends Expr
>   case class Number(n: Int) extends Expr
>   case class Sum(e1: Expr, e2: Expr) extends Expr
>   case class Prod(e1: Expr, e2: Expr) extends Expr
> ```

By placing {@{the case classes inside a companion object (`Expr`)}@} we keep {@{the global namespace uncluttered}@}; construction then takes {@{the form `Expr.Number(1)` instead of a bare `Number(1)`}@}. {@{A convenient import (`import Expr.*`)}@} restores {@{the shorter syntax when desired}@}. Such structures are known as {@{__algebraic data types__ (ADTs)}@}, {@{a staple of functional programming}@} that combine {@{product and sum types}@} to describe {@{complex data in a concise, type‑safe manner}@}.

Scala's {@{__enumeration__ (`enum`) construct}@} offers {@{an even more compact notation for ADTs}@} whose {@{variants do not share a common superclass}@}. {@{The expression hierarchy}@} for {@{arithmetic expressions above}@} can be rewritten as:

> [!example] __example__
>
> {@{The expression hierarchy}@} for {@{arithmetic expressions above}@} can be rewritten as:
>
> ```Scala
> enum Expr:
>   case Var(s: String)
>   case Number(n: Int)
>   case Sum(e1: Expr, e2: Expr)
>   case Prod(e1: Expr, e2: Expr)
> ```

The compiler expands {@{this into a sealed abstract class and companion object automatically}@}, eliminating {@{boilerplate}@}. Enums can be {@{used with pattern matching exactly as case classes}@}:

> [!example] __example__
>
> Enums can be {@{used with pattern matching exactly as case classes}@}:
>
> ```Scala
> def show(e: Expr): String = e match
>   case Expr.Var(x)     => x
>   case Expr.Number(n)  => n.toString
>   case Expr.Sum(a,b)   => s"${show(a)} + ${show(b)}"
>   case Expr.Prod(a,b)  => s"${showFactor(a)} * ${showFactor(b)}"
>
> def showFactor(e: Expr): String = e match
>   case _: Expr.Sum => s"(${show(e)})"
>   case _           => show(e)
> ```

For {@{simple, parameterless variants}@}, {@{enums}@} resemble {@{traditional enumerations}@}. For example:

> [!example] __example__
>
> Enums can be {@{used with pattern matching exactly as case classes}@}:
>
> ```Scala
> enum Color:
>   case Red, Green, Blue
> ```

{@{Pattern matching}@} treats {@{these cases as constants}@} as {@{they start with capital letters}@}:

> [!example] __example__
>
> {@{Pattern matching}@} treats {@{these cases as constants}@} as {@{they start with capital letters}@}:
>
> ```Scala
> enum DayOfWeek:
>   case Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
>
> def isWeekend(day: DayOfWeek) = day match
>   case Saturday | Sunday => true
>   case _                 => false
> ```

Enums also support {@{parameters and methods}@}. {@{The `Direction` example}@} demonstrates {@{a parametric enum with four cardinal directions}@}, each {@{carrying an `(dx, dy)` offset}@}:

> ![example] __example__
>
> {@{The `Direction` example}@} demonstrates {@{a parametric enum with four cardinal directions}@}, each {@{carrying an `(dx, dy)` offset}@}:
>
> ```Scala
> enum Direction(val dx: Int, val dy: Int):
>   case Right extends Direction(1, 0)
>   case Up    extends Direction(0, 1)
>   case Left  extends Direction(-1, 0)
>   case Down  extends Direction(0, -1)
>
>   def leftTurn = Direction.values((ordinal + 1) % 4)
> ```

Here {@{`ordinal` \(`Direction.ordinal`\)}@} yields {@{the zero‑based index of a variant}@}, and {@{`values` \(`Direction.values`\)}@} is {@{an immutable array containing all simple (non‑parameterised) variants}@}. {@{Parameterised cases}@} do not {@{appear in this array}@}; only {@{simple ones receive ordinal numbers}@}.

> [!example] __example__
>
> The compiler generates {@{code roughly equivalent to}@}:
>
> ```Scala
> abstract class Direction(val dx: Int, val dy: Int):
>   def leftTurn = Direction.values((ordinal - 1) % 4)
>
> object Direction:
>   val Right = new Direction(1,0){ }
>   val Up    = new Direction(0,1){ }
>   val Left  = new Direction(-1,0){ }
>   val Down  = new Direction(0,-1){ }
> ```

Because enums are {@{essentially syntactic sugar}@} for {@{a sealed class and companion object}@}, they are {@{ideal for __domain modelling__}@} where {@{the data structure is large}@} but {@{operations on it are defined elsewhere}@}.

> [!example] __example__
>
> {@{A payment‑method model}@} might look like:
>
> ```Scala
> enum PaymentMethod:
>   case CreditCard(kind: CardKind, holder: String, number: Long, expires: Date)
>   case PayPal(email: String)
>   case Cash
>
> enum CardKind:
>   case Visa, Mastercard, Amex
> ```

In summary, Scala's enums provide {@{a succinct and type‑safe way to declare pure data structures}@}. They can be used as {@{compact replacements for case‑class hierarchies}@}, or as {@{finite sets of values}@}, and may combine {@{parameterised and simple cases within the same declaration}@}. {@{Operations on these data types}@} are typically {@{expressed elsewhere—often via pattern matching or functional combinators}@}—keeping the data definitions {@{clean and focused solely on representation}@}.

## objects

When {@{the semantics of a program}@} allow {@{only one logical value for a concept}@}, it is idiomatic to {@{represent it as a singleton object}@}. For example, {@{the empty set}@} in {@{an integer‑set library}@}:

> [!example] __example__
>
> For example, {@{the empty set}@} in {@{an integer‑set library}@}:
>
> ```Scala
> object Empty extends IntSet {
>   def contains(x: Int): Boolean = false
>   def incl(x: Int): IntSet       = NonEmpty(x, Empty, Empty)
> }
> ```

Properties:

- __Singleton__ ::@:: – `Empty` exists only once; any reference to it evaluates to the same instance.
- __No construction needed__ ::@:: – Users do not create new `Empty()` objects; they simply refer to `Empty`.
- __Value semantics__ ::@:: – Because objects live in Scala's _term_ namespace, `Empty` is a value rather than a type.

### companion objects

Scala permits {@{a class and an object}@} to {@{share the same name}@} when {@{declared in the same source file}@}. These are called {@{__companions__}@}:

> [!example] __example__
>
> These are called {@{__companions__}@}:
>
> ```Scala
> class IntSet { /* ... */ }
>
> object IntSet {
>   def singleton(x: Int): IntSet = NonEmpty(x, Empty, Empty)
> }
> ```

Properties of companion objects:

- __Separate namespaces__ ::@:: – Types reside in the _type_ namespace; values (including objects) reside in the _term_ namespace.
- __Mutual access__ ::@:: – A companion object can access private members of its class and vice versa.
- __Static‑like behaviour__ ::@:: – Since Scala lacks Java's `static` keyword, companion objects serve the same purpose for grouping utility functions or constants related to a class.
  - Static‑like behaviour / __Factory methods__ ::@:: – Companion objects often provide convenient constructors, analogous to static factory methods in Java (`IntSet.singleton`).

Together, {@{singleton objects and companions}@} give Scala {@{concise, type‑safe mechanisms}@} for {@{representing unique values and packaging helper functionality}@} without resorting to {@{mutable global state}@}.

## traits

Scala's {@{_trait_ mechanism}@} extends {@{the classical single‑inheritance model of classes and objects}@} by allowing {@{a type to acquire functionality from an arbitrary number of traits}@}. {@{A trait}@} is declared with {@{the keyword `trait` instead of `abstract class`}@}, but it can contain {@{both abstract and concrete members}@}.

> [!example] __example__
>
> {@{A trait}@} is declared with {@{the keyword `trait` instead of `abstract class`}@}, but it can contain {@{both abstract and concrete members}@}.
>
> ```Scala
> trait Planar {
>   def height: Int
>   def width: Int
>   def surface = height * width          // concrete method
> }
> ```

A trait may declare {@{_abstract fields or methods_}@}, which must be {@{supplied by a concrete subclass}@}. It may also declare {@{_concrete implementations_}@} that are {@{inherited automatically}@}.

Unlike {@{Java interfaces \(prior to Java 8\)}@}, traits can {@{maintain state and provide full method bodies}@}.

While {@{Scala classes}@} can {@{extend at most one superclass}@}, they may {@{mix in any number of traits}@}:

> [!example] __example__
>
> While {@{Scala classes}@} can {@{extend at most one superclass}@}, they may {@{mix in any number of traits}@}:
>
> ```Scala
> class Square extends Shape with Planar with Movable { /* … */ }
> ```

Here `Square` inherits from {@{the concrete class}@} `Shape` and incorporates {@{the contracts and implementations}@} of `Planar` and `Movable`. {@{The order of mixing}@} matters because {@{trait linearization}@} determines {@{which implementation is used when multiple traits provide the same member}@}.

Traits therefore provide {@{a flexible way}@} to {@{compose behavior}@}, enabling {@{classes to conform to multiple supertypes}@} without violating {@{the single‑inheritance rule for concrete classes}@}.

## expressions

Scala supports {@{expressions}@}, including {@{arithmetic expressions}@}. {@{Parentheses \(`()`\)}@} can be used to {@{prioritize evaluating some expressions over others first}@}. {@{Semicolons \(`;`\) to end an expression}@} are {@{optional in most cases}@}. You need it if you {@{put multiple expressions in one line}@}.

Scala supports {@{conditional expressions}@}. Its syntax is {@{`if <predicate> then <expr if true> else <expr if false>`}@}. `<predicate>` is {@{always evaluated}@}. If {@{it is `true`}@}, then {@{`<expr if true>` is evaluated}@}. Else, {@{`<expr if false>` is evaluated}@}.

Scala supports {@{logical expressions}@}. They are {@{as in Java}@}, and includes {@{`true`, `false`, `!<expr>`, `<expr 1> && <expr 2>`, and `<expr 1> || <expr 2>`}@}. Evaluation uses {@{short circuiting}@}: If {@{`<expr 1>` evaluates to `true`}@}, then {@{`<expr 2>` is not evaluated in `<expr 1> || <expr 2>`}@}; if {@{`<expr 1>` evaluates to `false`}@}, then {@{`<expr 2>` is not evaluated in `<expr 1> && <expr 2>`}@}.

Scala supports {@{comparisons}@}. They are {@{as in Java}@}.

### anonymous functions

{@{Anonymous functions}@} allow us to {@{define functions without _naming_ them}@}. The full syntax is {@{`(<arg name 1>: <arg type 1>, ..., <arg name N>: <arg type N>) => <expr>`}@}. {@{The return type}@} {@{cannot be specified and is inferred from `<expr>`}@}. {@{The argument types}@} {@{can be omitted if it can be inferred}@}, e.g. {@{when defining an anonymous function to pass to an argument in a function call}@}. If {@{there is exactly 1 argument with an omitted argument type}@}, then {@{parentheses \(`()`\) are optional}@}.

For some reason, {@{call-by-name syntax}@} {@{does not work with anonymous functions}@}.

It can be treated as {@{_syntactic sugar_}@} for the following more verbose syntax: {@{`{ def f(<arg name 1>: <arg type 1>, ..., <arg name N>: <arg type N>) = <expr>; f }`}@}

### exception handling

Scala adopts {@{a familiar exception‑handling model from Java}@}. {@{An exception}@} can be {@{raised at any point during evaluation}@} by using {@{the `throw` keyword}@}:

> [!example] __example__
>
> {@{An exception}@} can be {@{raised at any point during evaluation}@} by using {@{the `throw` keyword}@}:
>
> ```Scala
> throw exn
> ```

The expression immediately {@{terminates the current computation}@} and propagates {@{the supplied exception object (`exn`) up the call stack}@} until it is {@{caught by an appropriate handler}@} (e.g., {@{a surrounding `try‑catch` block}@}). Because this construct {@{never yields a normal value}@}, {@{its type}@} is {@{the bottom type `Nothing`}@}, which fits {@{seamlessly into Scala's type system}@}. This guarantees that {@{any code following a `throw` statement}@} is {@{unreachable}@} and can be {@{omitted from static analysis}@}.

### pattern matching

{@{__Pattern matching__}@} is {@{a functional programming technique}@} that allows {@{concise and type‑safe deconstruction of algebraic data types}@}. It was introduced in languages such as {@{Haskell, ML, and later adopted by Scala}@}. It can replace {@{ad‑hoc classification methods, unsafe casts, and tightly coupled object‑oriented designs}@}.

{@{The __match__ construct}@} generalises {@{a `switch` statement to arbitrary data structures}@}. {@{A match expressio}@} consists of {@{a _scrutinee_ followed by one or more case clauses}@}, each written as {@{`pattern => result`}@}. For instance, {@{evaluating an arithmetic expression}@} becomes:

> [!example] __example__
>
> For instance, {@{evaluating an arithmetic expression}@} becomes:
>
> ```Scala
> def eval(e: Expr): Int = e match {
>   case Number(n)       => n
>   case Sum(left, right) => eval(left) + eval(right)
> }
> ```

Patterns are built from {@{constructor names (`Number`, `Sum`), variable bindings (`n`, `left`, `right`)}@}, {@{wildcards (`_`), constants (`1`, `true`), and type tests (`x: Number`)}@}. {@{Variables in patterns}@} must {@{start with a lowercase letter}@}, while {@{constant identifiers}@} {@{begin with an uppercase letter (unless they are reserved words such as `null`, `true`, or `false`)}@}. A pattern may {@{only bind a particular variable name once}@}; therefore a pattern like {@{`Sum(x, x)` is illegal}@} because it would {@{attempt to bind the same variable twice}@}.

When {@{a match expression is evaluated}@}, {@{the scrutinee value}@} is {@{compared against each pattern in order}@}. {@{The first matching pattern}@} determines {@{the result of the whole expression}@}. If {@{no pattern matches}@}, Scala {@{throws a `MatchError`}@}. {@{This behaviour}@} is illustrated by the following sequence:

> [!example] __example__
>
> When {@{a match expression is evaluated}@}, {@{the scrutinee value}@} is {@{compared against each pattern in order}@}. {@{The first matching pattern}@} determines {@{the result of the whole expression}@}. If {@{no pattern matches}@}, Scala {@{throws a `MatchError`}@}. {@{This behaviour}@} is illustrated by the following sequence:
>
> ```Scala
> eval(Sum(Number(1), Number(2)))
> ```
>
> which expands to:
>
> ```Scala
> Sum(Number(1), Number(2)) match {
>   case Number(n)       => n
>   case Sum(e1, e2)     => eval(e1) + eval(e2)
> }
> ```
>
> and ultimately {@{yields `3`}@}.

{@{A common pitfall}@} is {@{the absence of compile‑time guarantees}@} that {@{all cases have been handled}@}. Consider:

> [!example] __example__
>
> {@{A common pitfall}@} is {@{the absence of compile‑time guarantees}@} that {@{all cases have been handled}@}. Consider:
>
> ```Scala
> def eval(e: Expr): Int = e match {
>   case Sum(left, right) => eval(left) + eval(right)
> }
> ```
>
> This {@{compiles fine}@} but will {@{throw a runtime `MatchError` when invoked with a `Number`}@}.

To {@{enforce exhaustive matching}@}, Scala allows {@{the __sealed__ modifier on an abstract class or trait}@}. {@{A sealed type}@} restricts {@{its subclasses to be defined in the same file}@}, enabling the compiler to {@{verify that every possible subclass is covered by pattern clauses}@}:

> [!example] __example__
>
> To {@{enforce exhaustive matching}@}, Scala allows {@{the __sealed__ modifier on an abstract class or trait}@}. {@{A sealed type}@} restricts {@{its subclasses to be defined in the same file}@}, enabling the compiler to {@{verify that every possible subclass is covered by pattern clauses}@}:
>
> ```Scala
> sealed abstract class Expr
> case class Number(n: Int) extends Expr
> case class Sum(left: Expr, right: Expr) extends Expr
> ```
>
> With {@{this sealed hierarchy}@}, {@{the previous incomplete `eval` definition}@} will {@{no longer compile}@}; the compiler reports {@{a missing case for `Number`}@}.

{@{Pattern matching}@} can also be {@{embedded directly in type definitions}@}. For example, {@{adding an `eval` method to the base trait}@} leverages {@{pattern matching internally}@}:

> [!example] __example__
>
> {@{Pattern matching}@} can also be {@{embedded directly in type definitions}@}. For example, {@{adding an `eval` method to the base trait}@} leverages {@{pattern matching internally}@}:
>
> ```Scala
> sealed abstract class Expr {
>   def eval: Int = this match {
>     case Number(n)       => n
>     case Sum(left, right) => left.eval + right.eval
>   }
> }
> ```
>
> Here each subclass inherits {@{a uniform `eval` implementation}@} that relies on {@{the structural patterns of the hierarchy}@}.

Here each subclass inherits {@{a uniform `eval` implementation}@} that relies on {@{the structural patterns of the hierarchy}@}. This approach decouples {@{data representation from behaviour}@} while still permitting {@{concise and type‑safe operations across all constructors}@}.

### for expressions

{@{A Scala _for‑expression_}@} is {@{a syntactic construct}@} that combines {@{one or more _generators_ and optional _filters_}@} to produce {@{a new collection from existing ones}@}. {@{Its canonical form}@} is

> [!example] __`for` expression__
>
> {@{A Scala _for‑expression_}@} is {@{a syntactic construct}@} that combines {@{one or more _generators_ and optional _filters_}@} to produce {@{a new collection from existing ones}@}. {@{Its canonical form}@} is
>
> ```Scala
> for s yield e
> ```
>
> where `s` denotes {@{a sequence of generators and filters}@}, and `e` is {@{an expression whose value becomes an element of the resulting collection}@}.

{@{A __generator__}@} has {@{the shape `p <- expr`}@}. Here {@{`expr`}@} must {@{evaluate to a collection}@} (such as {@{a `Seq`, `Set`, or any type that implements `GenTraversableOnce`}@}), while {@{`p`}@} is {@{a pattern that will be bound to each element produced by `expr` during iteration}@}. For example, in

> [!example] __`for` generator__
>
> {@{A __generator__}@} has {@{the shape `p <- expr`}@}. Here {@{`expr`}@} must {@{evaluate to a collection}@} (such as {@{a `Seq`, `Set`, or any type that implements `GenTraversableOnce`}@}), while {@{`p`}@} is {@{a pattern that will be bound to each element produced by `expr` during iteration}@}. For example, in
>
> ```Scala
> for i <- 1 until n yield i * 2
> ```
>
> {@{the generator `i <- 1 until n`}@} iterates over {@{the range `1 until n`}@}, binding {@{each integer to `i`}@}.

For‑expressions also support {@{pattern matching in _generator_ positions}@}. This feature allows {@{_filtering_ and deconstructing complex data structures directly}@} within the loop:

> [!example] __`for` generator with pattern matching__
>
> For‑expressions also support {@{pattern matching in _generator_ positions}@}. This feature allows {@{_filtering_ and deconstructing complex data structures directly}@} within the loop:
>
> ```Scala
> def bindings(x: JSON): List[(String, JSON)] = x match
>   case JSON.Obj(bindings) => bindings.toList
>   case _                  => Nil
> for
>   case ("phoneNumbers", JSON.Seq(numberInfos)) <- bindings(jsData)
>   numberInfo <- numberInfos
>   case ("number", JSON.Str(number)) <- bindings(numberInfo)
>   if number.startsWith("852")
> yield number
> ```
>
> {@{The resulting sequence}@} contains {@{phone numbers beginning with the country code `"852"`}@}.

Here, {@{the `case` prefixes}@} act as {@{guards that keep only those elements matching the specified pattern}@}.

{@{A __filter__}@} is written as {@{`if cond`}@}, where {@{`cond`}@} is {@{a boolean expression evaluated for each element of the preceding generators}@}. Filters prune {@{the intermediate results before they reach the final expression}@}.

{@{Two important rules}@} govern {@{for‑expressions}@}. First, {@{the sequence of generators and filters}@} must {@{begin with a generator}@}; {@{a filter}@} cannot {@{appear before all generators}@}. Second, when {@{multiple generators are present}@}, {@{the _last_ one}@} {@{varies fastest}@}, analogous to {@{nested loops in imperative languages}@}. Consequently, {@{the first generator}@} is {@{evaluated once per outer iteration}@}, while {@{subsequent generators iterate fully}@} for each {@{value of their predecessors}@}.

{@{These rules}@} enable {@{concise expression of complex iterations}@}, automatically translating into {@{calls to `map`, `flatMap`, and `filter` behind the scenes}@}. In summary, {@{`for` expressions}@} {@{enhance readability}@} by hiding {@{the boilerplate of nested function calls while preserving the underlying functional structure}@}.

#### for expression examples

In {@{many algorithmic problems}@} one must enumerate {@{combinations of elements that satisfy a set of constraints}@}. An example is the search for {@{all pairs of positive integers $(i,j)$}@} such that {@{$1\le j<i<n$ and the sum $i+j$ is prime}@}. {@{The natural way to solve this}@} in Scala is to generate {@{the Cartesian product of two ranges, filter the result, and collect the admissible pairs}@}. {@{The generation step}@} can be expressed as {@{a nested sequence construction}@}:

> [!example] __all pairs of positive integers that sum to prime__
>
> {@{The generation step}@} can be expressed as {@{a nested sequence construction}@}:
>
> ```Scala
> (1 until n).map(i => (1 until i).map(j => (i, j))).foldRight(Seq.empty[(Int, Int)])(_ ++ _)
> // The last operation is common, and is called `flatten`
> (1 until n).map(i => (1 until i).map(j => (i, j))).flatten
> // Equivalent code using the law: `xs.flatMap(f) = xs.map(f).flatten`
> (1 until n).flatMap(i => (1 until i).map(j => (i, j)))
> ```

Here {@{`until`}@} creates {@{an exclusive range}@}; for each {@{outer element `i`}@}, we build {@{an inner range from 1 to $i-1$}@} and map it to {@{the pair `(i,j)`}@}. {@{The `flatMap`}@} then concatenates {@{all these inner sequences into a single flat sequence of pairs}@}. The latter operation is equivalent to {@{first mapping \(`map`\) and then flattening \(`flatten`\)}@}. Both approaches yield {@{a sequence of all admissible $(i,j)$ pairs}@}. {@{A more idiomatic Scala solution}@} uses a {@{_for‑comprehension_}@}:

> [!example] __all pairs of positive integers that sum to prime__
>
> {@{A more idiomatic Scala solution}@} uses a {@{_for‑comprehension_}@}:
>
> ```Scala
> for {
>   i <- 1 until n
>   j <- 1 until i
>   if isPrime(i + j)
> } yield (i, j)
> ```

{@{The comprehension}@} automatically expands into {@{the `flatMap`/`map`/`filter` chain}@} shown above. Once {@{the sequence of pairs is available}@}, {@{a simple filter}@} extracts {@{those whose sum is prime}@}:

> [!example] __all pairs of positive integers that sum to prime__
>
> Once {@{the sequence of pairs is available}@}, {@{a simple filter}@} extracts {@{those whose sum is prime}@}:
>
> ```Scala
> xs.filter { case (x, y) => isPrime(x + y) }
> ```
>
> {@{Combining these steps}@} gives {@{a concise expression}@} that performs {@{the combinatorial search in one line}@}.

{@{The classic eight‑queens problem}@} asks for {@{all ways to place eight queens on an $8\times 8$ chessboard}@} so that {@{no two threaten each other}@}. {@{The constraints}@} are that queens cannot {@{share a row, column, or diagonal}@}. {@{A general solution for an arbitrary board size $n$}@} can be {@{expressed recursively}@}: for {@{each partially constructed placement of $k-1$ queens}@}, extend it by {@{placing the $k^{th}$ queen in every safe column}@}. {@{A concise Scala implementation}@} uses {@{a nested `for`‑comprehension}@} that {@{naturally encodes the recursion}@}:

> [!example] __<!-- markdown separator -->_n_-queens problem__
>
> {@{A concise Scala implementation}@} uses {@{a nested `for`‑comprehension}@} that {@{naturally encodes the recursion}@}:
>
> ```Scala
> def queens(n: Int): Set[List[Int]] = {
>   def placeQueens(k: Int): Set[List[Int]] =
>     if (k == 0) Set(Nil)
>     else for {
>       prevSol <- placeQueens(k - 1)  // existing solutions with k-1 queens
>       col     <- 0 until n           // try every column in the new row
>       if isSafe(col, prevSol)        // check safety against earlier queens
>     } yield col :: prevSol
>   placeQueens(n)
> }
> ```

{@{The list `prevSol`}@} records {@{the columns of previously placed queens}@}, with {@{the most recent queen}@} at {@{the head of the list}@}. {@{The helper `isSafe`}@} determines whether {@{a queen can be added in column `col`}@} on {@{the next row (row index equal to `prevSol.length`)}@}. {@{A straightforward recursive definition}@} is:

> [!example] __<!-- markdown separator -->_n_-queens problem__
>
> {@{The helper `isSafe`}@} determines whether {@{a queen can be added in column `col`}@} on {@{the next row (row index equal to `prevSol.length`)}@}. {@{A straightforward recursive definition}@} is:
>
> ```Scala
> def isSafe(col: Int, queens: List[Int]): Boolean =
>   !checks(col, 1, queens)
>
> private def checks(col: Int, delta: Int, queens: List[Int]): Boolean = queens match {
>   case qcol :: others =>
>     qcol == col
>     || (qcol - col).abs == delta       // vertical or diagonal attack
>     || checks(col, delta + 1, others)
>   case Nil => false
> }
> ```
>
> Here {@{`delta`}@} represents {@{the row distance between the new queen and each already‑placed queen}@}. If any queen {@{shares a column}@} ({@{`qcol == col`}@}) or {@{lies on a diagonal}@} ({@{absolute difference of columns equals `delta`}@}), {@{the placement is unsafe}@}.

#### for expressions in other languages

{@{Many other languages}@} offer {@{similar declarative mechanisms for combinatorial enumeration}@}. For instance, {@{Python's list comprehensions, Haskell's list comprehensions, and F\#'s sequence expressions}@} all allow {@{concise generation of nested pairs subject to predicates}@}:

> [!example] __for expressions in other languages__
>
> For instance, {@{Python's list comprehensions}@}:
>
> ```Python
> [(i, j) for i in range(1, n) for j in range(1, i) if is_prime(i + j)]
> ```
>
> {@{Haskell's list comprehensions}@}, and:
>
> ```Haskell
> [(i, j) | i <- [1..n], j <- [1..i], isPrime (i+j)]
> ```
>
> {@{F\#'s sequence expressions}@}:
>
> ```F#
> [for i in 1 .. n-1 do for j in 1 .. i-1 do if isPrime(i + j) then yield (i, j)]
> ```
>
> all allow {@{concise generation of nested pairs subject to predicates}@}.

These examples mirror {@{the Scala `for`‑comprehension shown above}@}, illustrating {@{a common functional paradigm}@}: iterate {@{over nested ranges}@}, filter {@{by a condition}@}, and collect {@{the results into a new collection}@}.

#### desugaring for expressions

{@{The Scala _for_ notation}@} is a concise syntax for expressing {@{compositional queries over collections}@}. {@{Its semantics}@} are essentially equivalent to {@{the map–flatMap–filter pipeline}@} that underlies {@{many database query languages}@}, and it can be applied to {@{any type that supplies `map`, `flatMap` and `withFilter` \(lazy version of `filter`\)}@}.

The compiler rewrites {@{a `for` expression}@} as {@{a composition of `map`, `flatMap` and a lazy variant of `filter` called `withFilter`}@}.  For instance, {@{the simple generator}@}:

> [!example] __rewriting `for` generator__
>
> For instance, {@{the simple generator}@}:
>
> ```Scala
> for x <- e1 yield e2
> ```
>
> becomes, using {@{`map`}@},
>
> ```Scala
> e1.map(x => e2)
> ```

{@{A more elaborate form}@} that mixes {@{generators and guards}@}:

> [!example] __rewriting `for` guard__
>
> {@{A more elaborate form}@} that mixes {@{generators and guards}@}:
>
> ```Scala
> for x <- e1 if pred; s yield e2
> ```
>
> is rewritten using {@{`withFilter` \(lazy version of `filter`\)}@} as
>
> ```Scala
> for x <- e1.withFilter(x => pred); s yield e2
> ```

and {@{a nested generator}@}:

> ![example] __rewriting `for` nested generators=__
>
> and {@{a nested generator}@}:
>
> ```Scala
> for x <- e1; y <- e2; s yield e3
> ```
>
> using {@{`flatMap`}@}, turns into
>
> ```Scala
> e1.flatMap(x => for y <- e2; s yield e3)
> ```

An example is {@{the prime‑pair generator}@}:

> [!example] __prime pair generator__
>
> An example is {@{the prime‑pair generator}@}:
>
> ```Scala
> for {
>   i <- 1 until n
>   j <- 1 until i
>   if isPrime(i + j)
> } yield (i, j)
> ```
>
> which expands to
>
> ```Scala
> (1 until n).flatMap(i =>
>   (1 until i).withFilter(j => isPrime(i + j)).map(j => (i, j)))
> ```

Because `for` desugars to {@{calls on `map`, `flatMap` and `withFilter`}@}, {@{any type that implements these methods}@} can be {@{queried with the same syntax}@}.  {@{This abstraction}@} is exploited by {@{database access libraries}@} such as {@{_Slick_ or _Quill_, and big‑data engines like _Spark_}@}, where {@{a collection of rows in a remote table}@} can be treated like {@{an ordinary Scala collection}@}.

Thus, {@{the _for_ notation}@} serves as a bridge between {@{functional programming idioms and declarative query languages}@}, providing {@{a uniform, type‑safe, and compositional way}@} to express {@{data transformations across a wide range of contexts}@}.

## definitions

To {@{give a name `<name>`}@} to {@{an expression `<expr>`}@}, use {@{`def <name>: <type> = <expr>`}@}. {@{`<type>`}@} is {@{optional if the type of `<expr>` can be _inferred_}@}. In particular, if {@{`<expr>` uses `<name>` \(recursion\)}@}, then {@{the type of `<expr>` needs to be specified}@}. Note that {@{`<expr>`}@} is not evaluated when {@{`<name>` is defined}@}. To {@{evaluate `<expr>` when `<name>` is defined}@}, use {@{`val` instead of `def`}@}.

Expressions can be {@{parameterized}@}. Use {@{`def <name>(<parm name 1>: <parm type 1>, ... <parm name N>: <parm type N>): <return type> = <expr>`}@}. {@{`<return type>`}@} is {@{optional if the type of `<expr>` can be _inferred_}@}. Expressions are evaluated by {@{replacing each occurrence of `<para name K>` by the actual parameters}@} when {@{the function is evaluated \(see [§ evaluation](#evaluation)\)}@}.

### multiple parameter lists

Scala 3 supports {@{multiple parameter lists}@}, e.g. {@{`def <name>(<param list 1>)...(<param list N>): <return type> = <expr>`}@}.

When {@{you call the function \(function application\)}@}, you need to {@{provide _all_ arguments in _all_ parameter lists}@} with {@{the _same_ grouping as the function parameter lists}@} too. To support this, {@{function application}@} is {@{left-associative}@}, i.e. {@{`f(a)(b)` is `(f(a))(b)`}@}.

Strictly speaking, {@{multiple parameter lists}@} is {@{distinct from _currying_}@}. However, if {@{you use one parameter list for each argument}@}, then you are {@{currying a function}@} by converting {@{the function into a sequence of functions that each takes a single argument}@}.

### extension methods

{@{Extension methods}@} define {@{extra members to a class while being outside the class definition}@}. They are useful for {@{adding utility methods to a class}@}. To define an extension, start with the syntax {@{`extension (<arg name>: <arg type>)` \(no trailing colon\)}@}, and then {@{start a newline and indent}@} to {@{add the extra methods}@}.

When {@{defining extension methods}@}, they cannot {@{access `private` members of the class}@}. They also cannot {@{access `this`}@} but must use {@{the name defined in the starting `extension` line}@}.

To {@{call extension methods}@}, they need to be {@{visible in the calling context}@}. {@{The exact rules}@} are {@{hard to explain now}@}, and some common cases are {@{companion object of the type \(code `object <name>` where `<name>` is the same as that of the type\)}@} and {@{defined or imported in the current scope}@}.

### varargs

Scala permits {@{a single method or constructor parameter}@} to be {@{declared as _repeated_}@}, meaning the caller may {@{supply any number of arguments of that type}@}. {@{A repeated parameter}@} is written with {@{an asterisk (`*`) after the element type}@}, e.g.:

> [!example] __example__
>
> {@{A repeated parameter}@} is written with {@{an asterisk (`*`) after the element type}@}, e.g.:
>
> ```Scala
> def sum(nums: Int*): Int = nums.sum
> ```

The compiler {@{desugars `nums` to a `Seq[Int]`}@}, so inside the method it behaves {@{like any other sequence}@}. {@{The call syntax}@} remains {@{that of ordinary arguments}@}:

> [!example] __example__
>
> {@{The call syntax}@} remains {@{that of ordinary arguments}@}:
>
> ```Scala
> sum(1, 2, 3)  // returns 6
> sum()         // returns 0
> ```

Repeated parameters are especially handy for {@{constructing collections without an explicit intermediate `List` or `Vector`}@}. For instance, {@{the `Polynomial` class}@} can accept {@{an arbitrary number of `(Int, Double)` bindings}@}:

> [!example] __example__
>
> For instance, {@{the `Polynomial` class}@} can accept {@{an arbitrary number of `(Int, Double)` bindings}@}:
>
> ```Scala
> 
> class Polynomial(nonZeroTerms: Map[Int, Double]) {
>   def this(bindings: (Int, Double)*) = this(bindings.toMap)
>   /* ... */
> }
> ```
>
> Now one can {@{write succinctly}@}:
>
> ```Scala
> val p = Polynomial(1 -> 2.0, 3 -> 4.5, 5 -> -1.0)
> ```
>
> because the compiler bundles {@{the supplied pairs into a `Seq[(Int, Double)]`}@}.

{@{Varargs}@} provide {@{a concise and type‑safe alternative to variadic C functions}@} while preserving {@{Scala's functional collection APIs}@}.

## evaluation

The {@{2 major evaluation strategies for functions}@} are {@{call by value \(CBV\) and call by name \(CBN\)}@}. Scala by default uses {@{CBV}@}. To {@{specify CBN for a particular parameter}@}, {@{specify the type using `=> <type>` instead of `<type>`}@}.

### tail recursion

Scala 3 optimizes {@{_direct_ tail calls to the _current_ function}@} by {@{reusing the current stack frame}@}. To ensure {@{this optimization occurs}@}, {@{annotate the function with `@scala.annotation.tailrec`}@}. This will {@{cause a compilation error if the optimization cannot be applied}@}.

## scoping

Scala {@{creates a new scope}@} using {@{braces \(`{}`\)}@}. Since {@{Scala 3}@}, {@{indentation after `=`, `then`, `else`, etc. can be used as well \(like Python\)}@}. The {@{last element \(statement\) of a scope}@} is {@{the expression that determines the value of that scope}@}. The motivation of scoping is to {@{avoid _namespace pollution_}@}.

Scala uses {@{lexical scoping}@} with {@{\(variable\) shadowing}@}. That is, {@{each occurrence of a name}@} refers to {@{the definition of the name appearing in the _innermost_ scope \(shadowing\) according to the _source code_ \(lexical scoping\)}@}.

Scala supports {@{_optional_ end markers}@} to {@{mark the end of a scope}@}. It must have {@{the same indentation as the opening keyword}@}. The end marker has the syntax {@{`end <name or keyword>`}@}, using {@{`<name>` if the scope is named \(e.g. classes, functions, etc.\)}@} or {@{repeat the starting keyword if not}@}.

## syntax

### identifiers

In Scala, {@{identifier names}@} are {@{much more relaxed}@} compared to {@{most other programming languages}@}. An identifier can {@{start with a letter \(`_` is also a letter\) or symbols}@}. Then it can be followed by {@{any combination of letters, symbols, or digits}@}.

### infix notation

Normally, to {@{call a function}@}, you use the syntax {@{`a.f(...)`}@}, known as {@{the _dot notation_}@}. If your function {@{accepts exactly 1 argument `b`}@}, you can opt to use the syntax {@{`a f b`}@}, known as {@{the _infix notation_}@}, to call the function. To do so, {@{prepend `infix` before `def` in the function definition}@}.

Since {@{identifier names in Scala}@} is {@{much more relaxed}@}, this, coupled with {@{infix notation}@}, allows you to {@{"overload" operators}@}.

With {@{infix notation}@}, this is {@{ambiguity with _precedence_}@}. In Scala, {@{the precedence of an infix function call}@} is based on {@{the _first_ character of the infix function name}@}. Starting from {@{the highest priority \(parenthesized first\)}@}, we have {@{any other special characters not listed below}@}, then {@{precedence rules for common operators similar to other programming languages}@} \({@{multiply, divide, modulo}@} &gt; {@{addition, subtraction}@} &gt; {@{colon \(`:`\)}@} &gt; {@{equality and inequality}@} &gt; {@{comparison}@} &gt; {@{and}@} &gt; {@{xor}@} &gt; {@{or}@}\), and finally {@{all other letters \(including `_`\)}@}.

## code organization

Scala structures {@{code into a hierarchical namespace}@} called {@{_packages_}@}. {@{A package declaration}@} at {@{the top of a source file}@} determines {@{the fully qualified name of every class or object}@} defined in that file.

### packages

> [!example] __example__
>
> {@{The `Hello` object}@} resides in {@{the package `ppl.examples`}@}.
>
> ```Scala
> package ppl.examples
>
> object Hello { /* ... */ }
> ```
>
> It can be {@{referenced elsewhere}@} by {@{its full name}@}:
>
> ```shell
> scala ppl.examples.Hello
> ```

{@{_Packages_}@} therefore provide a way to {@{avoid naming collisions}@} and to {@{group related functionality}@}.

### imports

When {@{a class}@} is defined {@{in a different package}@}, you may refer to it either with {@{its fully qualified name}@} or by {@{importing it into the current scope}@}.

> [!example] __example__
>
> When {@{a class}@} is defined {@{in a different package}@}, you may refer to it either with {@{its fully qualified name}@} or by {@{importing it into the current scope}@}.
>
> ```Scala
> val r = ppl2.Rational(1, 2)          // full qualification
> ```
>
> or
>
> ```Scala
> import ppl2.Rational
> val r = Rational(1, 2)                // after import
> ```

There are {@{several forms}@} of imports:

- __Named imports__ ::@:: – Bring specific members into scope. <p> - only `Rational`: `import ppl2.Rational           // only Rational` <br/> - both `Rational` and `Hello`: `import ppl2.{Rational, Hello} // both Rational and Hello`
- __Wildcard imports__ ::@:: – Bring all members of a package or object. <p> - all in package `ppl2`: `import ppl2.*                  // all in package ppl2`

Imports may target either {@{packages}@} or {@{singleton objects}@}.

### automatic imports

{@{Certain namespaces}@} are {@{implicitly imported}@} into every Scala program, eliminating {@{the need for explicit statements}@}: \(annotation: 3 items: {@{`package scala`, `package java.lang`, `object scala.Predef`}@}\)

- `package scala` ::@:: – Core language types and utilities (e.g., `Int`, `Boolean`).
- `package java.lang` ::@:: – Java’s base classes (e.g., `Object`).
- `object scala.Predef` ::@:: – Standard library helpers (`require`, `assert`, etc.).

Examples of fully qualified names:

| Symbol    | Qualified name         |
| --------- | ---------------------- |
| `Int`     | `scala.Int`            |
| `Boolean` | `scala.Boolean`        |
| `Object`  | `java.lang.Object`     |
| `require` | `scala.Predef.require` |
| `assert`  | `scala.Predef.assert`  |

{@{These implicit imports}@} ensure that {@{the most common types and functions}@} are {@{always available without cluttering source files}@}.

## runtime

Scala runs on {@{the Java Virtual Machine \(JVM\)}@}, which {@{provides platform independence and access to a vast ecosystem of Java libraries}@}. Scala {@{code is compiled into Java bytecode}@}, allowing {@{seamless interoperability with Java code}@}.

### dynamic binding

{@{Object‑oriented languages}@}, including Scala, employ {@{_dynamic method dispatch_ (also called _late binding_)}@} to determine {@{which implementation of a method is executed at runtime}@}. When {@{a call such as `obj.method(args)`}@} is made, {@{the actual code that runs}@} depends on {@{the concrete type of `obj`}@}, not {@{merely its declared static type}@}.

> [!example] __example__
>
> Compare {@{these 2 examples}@}:
>
> ```Scala
> val xx: IntSet = Empty
> xx.contains(1)
> ```
>
> ```Scala
> val xx: IntSet = NonEmpty(7, Empty, Empty)
> xx.contains(7)
> ```
>
> {@{A stepwise expansion}@} illustrates {@{dynamic dispatch}@}. Thus, regardless of {@{the static type of the expression}@} is {@{`IntSet`}@}, {@{the runtime dispatch}@} chooses {@{different implementations}@} depending on {@{its actual type at runtime}@}.

{@{Dynamic dispatch}@} can be viewed as {@{a form of _polymorphism_}@} that parallels {@{higher‑order functions}@}:

- __Objects in terms of functions__ ::@:: – A method can be represented by a function value; passing an object's behavior is equivalent to passing a function reference.
- __Functions in terms of objects__ ::@:: – Conversely, a function that accepts other functions as parameters can be reinterpreted as an object whose methods embody those functions.

{@{Both paradigms}@} rely on {@{_late resolution_}@}: {@{the actual code executed}@} is decided {@{at runtime rather than compile time}@}. {@{This correspondence}@} suggests that one could {@{implement an object‑oriented hierarchy}@} using {@{only higher‑order functions}@} \(e.g., by {@{encoding dispatch tables}@}\) and vice versa, illustrating {@{the deep equivalence}@} between {@{object‑based and functional abstractions}@} in Scala.

### type erasure

In {@{many statically typed languages}@}, {@{the _type parameters_ used in generic definitions}@} do not {@{influence how a program is executed at runtime}@}. Before {@{the interpreter or virtual machine}@} {@{evaluates the code}@}, {@{all type information}@} is discarded—a process known as {@{__type erasure__}@}. Consequently, {@{the compiled bytecode}@} contains only {@{the concrete operations required for execution}@}; {@{the generic structure}@} is represented by {@{its non‑generic skeleton}@}.

Languages such as {@{Java, Scala, Haskell, and OCaml}@} rely on type erasure to keep {@{their runtime systems lightweight}@}. For example, {@{a `List[Int]` and a `List[String]`}@} are both {@{compiled to the same underlying class structure (`List`) at runtime}@}; only {@{the compile‑time type checker}@} {@{distinguishes between them}@}.

Some languages maintain {@{_reified_ generics}@}, preserving {@{type information after compilation}@} so that it can {@{influence execution}@}. {@{C++, C#, and F#}@} are notable examples: they allow generic types to participate in {@{reflection, dynamic dispatch, or runtime checks}@}, which can {@{alter control flow or data representation}@}.

Thus, while type parameters provide {@{powerful compile‑time guarantees}@} in Scala and similar languages, their presence is {@{largely invisible at runtime due to erasure}@}. This design choice simplifies {@{the virtual machine}@} but limits {@{certain metaprogramming capabilities that rely on runtime type inspection}@}.

## libraries

### Scala documentation

{@{The Scala standard library}@} is {@{a web‑based API reference}@}. {@{The current documentation}@} can be accessed at: {@{<https://scala-lang.org/api/current>}@}

Here developers can browse {@{package hierarchies, view class and method signatures, and read explanatory notes}@}, facilitating effective use of {@{the language's rich set of libraries}@}.

### cons

In {@{functional programming}@} {@{the canonical immutable sequence}@} is {@{the _cons‑list_}@}: {@{a singly linked structure}@} built from {@{an empty list `Nil` and a recursive constructor `Cons`}@}:

- `Nil` ::@:: – represents the empty list.
- `Cons` ::@:: – packages an element together with another list (its "tail").

Because {@{every `Cons` node}@} contains only {@{references to its head \(the first element\) and tail \(the remaining elements\)}@}, lists can be {@{constructed, deconstructed, and traversed purely}@} through {@{recursion without mutation}@}.

> [!example] __examples__
>
> This use of {@{`List`}@}
>
> ```Scala
> List(1, 2, 3)
> ```
>
> expands to
>
> ```Scala
> Cons(1, Cons(2, Cons(3, Nil())))
> ```
>
> {@{A nested list}@} such as {@{`List(List(true, false), List(3))`}@} becomes
>
> ```Scala
> Cons(
>   Cons(true, Cons(false, Nil())),
>   Cons(
>     Cons(3, Nil()),
>     Nil()
>   )
> )
> ```

{@{These expansions}@} highlight how {@{each element is wrapped in a `Cons`}@}, with {@{the final cell being `Nil`}@}.

{@{A typical Scala representation}@} of {@{an integer list using cons‑lists}@} might look like this:

> [!example] __example__
>
> {@{A typical Scala representation}@} of {@{an integer list using cons‑lists}@} might look like this:
>
> ```Scala
> package ppl3
>
> trait IntList                     // common supertype for all lists
>
> class Cons(val head: Int, val tail: IntList) extends IntList
> class Nil() extends IntList          // sentinel for the empty list
> ```

Under {@{this hierarchy}@}, {@{any value of type `IntList`}@} is either: \(annotation: 2 items: {@{`Nil`, `Cons`}@}\)

- an instance of `Nil`, ::@:: denoting the empty sequence, or
- an instance of `Cons`, ::@:: carrying a head element (`head`) and a recursive tail (`tail`).

{@{The immutability of the data structure}@} is guaranteed by making {@{all fields `val`s (read‑only) and by never providing mutation methods}@}. {@{This simple algebraic type definition}@} forms {@{the backbone of many functional algorithms}@}—{@{folds, maps, filters}@}—that rely on {@{structural recursion over cons‑lists}@}.

### tuples

{@{A two‑element pair `(x, y)`}@} is syntactic sugar for {@{a tuple of type `Tuple2[T1, T2]`}@}. {@{The tuple expression `(e1, e2)`}@} is equivalent to {@{the constructor call `scala.Tuple2(e1, e2)`}@}. The pattern {@{extends to more elements}@}: {@{the expression `(p1, ..., pN)`}@} expands to {@{`scala.TupleN(p1, ..., p2)`}@}. For {@{small tuples (up to 22 elements)}@}, Scala provides {@{the type aliases `TupleN` and the corresponding case classes}@}:

> [!example] __example__
>
> For {@{small tuples (up to 22 elements)}@}, Scala provides {@{the type aliases `TupleN` and the corresponding case classes}@}:
>
> ```Scala
> case class Tuple2[+T1, +T2](_1: T1, _2: T2)
> ```

{@{The fields of a tuple}@} are {@{accessed through the names `_1`, `_2`, etc.}@}:

> [!example] __example__
>
> {@{The fields of a tuple}@} are {@{accessed through the names `_1`, `_2`, etc.}@}:
>
> ```Scala
> val label = pair._1
> val value = pair._2
> ```

{@{Pattern matching}@} on tuples is usually {@{preferred for readability}@}.

#### tuple as the only function argument

Scala distinguishes between {@{functions that take two or more separate arguments}@} and those that {@{take a single tuple argument}@}:

- `f: (T, T) => Boolean` ::@:: – a function expecting two parameters.
- `g: ((T, T)) => Boolean` ::@:: – a function whose single parameter is a pair.

The compiler accepts {@{both calling syntaxes for the latter}@}, while the former {@{must be called with separate arguments}@}. For example:

> [!example] __example__
>
> The compiler accepts {@{both calling syntaxes for the latter}@}, while the former {@{must be called with separate arguments}@}. For example:
>
> ```Scala
> val g: ((Int, Int)) => Boolean = _ => true
> g((0, 1))   // correct and formal
> g(0, 1)     // also compiles
>
> val f: (Int, Int) => Boolean = _ > _
> f(0, 1)     // correct
> f((0, 1))   // does NOT compile
> ```

### options

In Scala {@{the type `Option[+A]`}@} is {@{a container that may or may not hold a value of type `A`}@}. It is defined as {@{an abstract sealed class with two concrete subclasses}@}:  

> [!example] __example__
>
> In Scala {@{the type `Option[+A]`}@} is {@{a container that may or may not hold a value of type `A`}@}. It is defined as {@{an abstract sealed class with two concrete subclasses}@}:  
>
> ```Scala
> sealed abstract class Option[+A]
> case class Some[A](value: A) extends Option[A]
> object None extends Option[Nothing]
> ```

{@{An instance of `Option`}@} represents {@{the presence (`Some`) or absence (`None`) of a value}@}, thereby {@{avoiding null references}@}. Because `Option` is {@{an algebraic data type}@}, it can be {@{pattern‑matched safely}@}:

> [!example] __example__
>
> Because `Option` is {@{an algebraic data type}@}, it can be {@{pattern‑matched safely}@}:
>
> ```Scala
> def describe(opt: Option[Int]): String = opt match {
>   case Some(n) => s"The number is $n"
>   case None    => "No number provided"
> }
> ```

{@{The standard library}@} supplies {@{numerous combinators (`map`, `flatMap`, `getOrElse`, etc.)}@} that let callers manipulate {@{the contained value when it exists while propagating absence otherwise}@}. This design makes {@{optional values explicit}@}, enabling {@{more robust and expressive code}@}.

### pre-definitions

The Scala {@{`Predef` object}@} provides {@{definitions that are accessible without explicit quantification}@}. They contain {@{useful utilities}@}.

#### checking

Scala provides {@{several functions}@} to check {@{preconditions, assertions, and more}@}. They {@{throw an error \(but of a different type\)}@} when {@{a condition fails}@}, optionally with {@{an error message}@}. They are used {@{in different situations}@}.

{@{Preconditions}@} are used to {@{ensure arguments to a class or function}@} satisfies {@{certain constraints}@}. The syntax is {@{`require(<precondition>[, <message>])`}@}. It throws {@{`IllegalArgumentException`}@} if {@{`<precondition>` is false}@}.

{@{Assertions}@} are used to {@{ensure a condition}@} is {@{satisfied in a general context}@}. The syntax is {@{`assert(<assertion>[, <message>])`}@}. It throws {@{`AssertionError`}@} if {@{`<assertion>` is false}@}.

## philosophy

### pure object-orientation

{@{A language}@} is deemed {@{_purely object‑oriented_}@} when {@{every value that can appear at runtime is an instance of a class}@}. In {@{such a system}@}, {@{even seemingly primitive values}@} are {@{objects whose types are defined as classes}@}. Scala appears to {@{violate this rule superficially}@} because it offers {@{primitives (`Int`, `Boolean`) and first‑class functions}@}, yet a closer examination reveals that these too are {@{_conceptually_ class instances}@}, only that {@{the _runtime_ representation is different for efficiency}@}.

Scala _conceptually_ treats {@{the familiar types `scala.Int` and `scala.Boolean`}@} like {@{any other user‑defined class}@}: they reside in {@{the package `scala`}@}. For {@{performance reasons}@}, the compiler maps {@{these classes to JVM primitives (`int`, `boolean`) when emitting bytecode}@}. Nevertheless, from {@{a type‑system perspective}@} they are {@{ordinary classes with methods such as `+`, `-`, and logical operators}@}.

> [!example] __idealized `scala.Boolean`__
>
> If we strip away {@{the JVM optimisations}@}, a Boolean can be {@{defined purely in Scala}@}:
>
> ```Scala
> abstract class Boolean extends AnyVal {
>   def ifThenElse[T](t: => T, e: => T): T
>   def &&(x: => Boolean): Boolean = ifThenElse(x, false)
>   def ||(x: => Boolean): Boolean = ifThenElse(true, x)
>   // … other logical operators …
> }
> ```
>
> {@{Concrete constants}@} are represented as {@{singleton objects}@}:
>
> ```Scala
> object true extends Boolean { def ifThenElse[T](t: => T, e: => T) = t }
> object false extends Boolean{ def ifThenElse[T](t: => T, e: => T) = e }
> ```

This construction shows that {@{the logical connectives}@} are {@{merely methods on a class}@}; {@{no primitive boolean type}@} is required. Indeed, using Scala's {@{extension syntax}@}, one can add {@{an implication operator to the idealized Boolean}@}:

> [!example] __idealized `scala.Boolean` with new operators__
>
> Indeed, using Scala's {@{extension syntax}@}, one can add {@{an implication operator to the idealized Boolean}@}:
>
> ```Scala
> extension (x: Boolean)
>   def ==> (y: Boolean) = x.ifThenElse(y, true)
> ```
>
> {@{The semantics}@} follow {@{classical logic}@}: if {@{`x` is true then `y` must be true}@}; otherwise {@{(`x` false) any value of `y` satisfies the implication}@}.

<!-- markdownlint MD028 -->

> [!example] __`scale.Int`__
>
> {@{The class `scala.Int`}@} declares {@{a rich set of arithmetic and bit‑wise operations}@}:
>
> ```Scala
> class Int {
>   def +(that: Double): Double
>   def +(that: Float):  Float
>   def +(that: Long):   Long
>   def +(that: Int):    Int      // similarly for -, *, /, %
>   def <<(cnt: Int):   Int       // also >>, >>> *
>   def &(that: Long):  Long
>   def &(that: Int):   Int       // also |, ^
>   // comparison operators …
> }
> ```
>
> Scala compiles {@{these to native machine instructions}@}. In principle, the class could be {@{re‑implemented from first principles without resorting to JVM primitives}@}.

For example, to represent {@{nonnegative integers without using `scala.Int`}@}, we can define {@{an abstract class `Nat` \(natural numbers\)}@} and have {@{two concrete subclasses `Zero` and `Succ`}@}. The construction is {@{the same as that used in the Peano axioms}@}, just {@{translated to Scala}@}. This illustrates that even {@{seemingly primitive types}@} can be expressed as {@{ordinary classes with method definitions}@}.

{@{This purely object‑oriented construction}@} demonstrates how {@{numeric types, usually treated as primitives for efficiency}@}, can be expressed {@{entirely in terms of classes and objects}@}. It also reinforces the principle that {@{Scala's type system is fully expressive enough}@} to model {@{any data structure without leaving the realm of objects}@}.

#### functions as objects

In Scala {@{every value is an object}@}, and this extends to {@{first‑class functions}@}. {@{A function from a type `A` to a type `B`}@} is represented by {@{the _function class_ `scala.Function1[A, B]`}@}. {@{The arrow notation (`=>`)}@} is merely {@{syntactic sugar for this trait}@}:

> [!example] __example__
>
> {@{A function from a type `A` to a type `B`}@} is represented by {@{the _function class_ `scala.Function1[A, B]`}@}. {@{The arrow notation (`=>`)}@} is merely {@{syntactic sugar for this trait}@}:
>
> ```Scala
> package scala
> trait Function1[-A, +B] {
>   def apply(x: A): B
> }
> ```

{@{The single abstract method `apply`}@} makes the function {@{callable with the familiar parentheses syntax}@}. {@{A function application}@} {@{`f(a, b)`}@} becomes:

> [!example] __example__
>
> {@{A function application}@} {@{`f(a, b)`}@} becomes:
>
> ```Scala
> f.apply(a, b)
> ```

{@{Additional arity‑specific traits}@}—{@{`Function2`, `Function3`, and so forth}@}—are defined {@{analogously for functions that take more parameters}@}.

{@{An anonymous lambda}@} such as {@{`(x: Int) => x * x`}@} is translated {@{by the compiler into an instance of the appropriate function trait}@}:

> [!example] __example__
>
> {@{An anonymous lambda}@} such as {@{`(x: Int) => x * x`}@} is translated {@{by the compiler into an instance of the appropriate function trait}@}:
>
> ```Scala
> new Function1[Int, Int] {
>   def apply(x: Int): Int = x * x
> }
> ```

{@{This generated class}@} can itself be viewed as {@{a local anonymous class defined inside a block}@}:

> [!example] _-example__
>
> {@{This generated class}@} can itself be viewed as {@{a local anonymous class defined inside a block}@}:
>
> ```Scala
> {
>   class $anonfun() extends Function1[Int, Int] {
>     def apply(x: Int) = x * x
>   }
>   new $anonfun()
> }
> ```

{@{The `$anonfun` name}@} is {@{an internal placeholder}@}; the compiler typically generates {@{a unique identifier for each anonymous function}@}. At {@{runtime}@} this object behaves {@{like any other Scala object}@}: it can be {@{stored, passed around, and invoked via `apply`}@}.

Because {@{functions are objects}@}, they inherit {@{all traits of ordinary classes}@}—such as {@{`equals`, `hashCode`, and `toString`}@}—and can participate in {@{generic type parameterization}@}. {@{This uniform treatment}@} underpins {@{many Scala features}@}: {@{higher‑order functions, implicit conversions}@}, and {@{pattern matching on function types}@} all rely on the fact that {@{a lambda}@} is an instance of {@{a concrete class implementing `Function1`}@}.

#### methods to functions

{@{A _method_}@} declared inside {@{a class or trait}@}—e.g., {@{`def f(x: Int): Boolean`}@}—is {@{not itself a first‑class value}@}. However, Scala automatically {@{lifts such methods to function values}@} when they are {@{passed as arguments or used without application}@}:

> [!example] __example__
>
> Scala automatically {@{lifts such methods to function values}@} when they are {@{passed as arguments or used without application}@}:
>
> ```Scala
> fixedPoint(f)(42)
> ```
>
> {@{The compiler}@} inserts {@{the conversion}@}
>
> ```Scala
> (x: Int) => f(x)
> ```
>
> which expands to {@{an instance of `Function1`}@}:
>
> ```Scala
> new Function1[Int, Boolean] {
>   def apply(x: Int): Boolean = f(x)
> }
> ```

{@{This implicit "eta‑expansion" \(terminology used by Scala\)}@} allows {@{methods to be treated seamlessly as functions in higher‑order contexts}@}.
