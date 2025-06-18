---
aliases:
  - most vexing parse
tags:
  - flashcard/active/general/eng/most_vexing_parse
  - language/in/English
---

# most vexing parse

The __most vexing parse__ is {@{a counterintuitive form of resolution to [ambiguous grammar](Ambiguous%20grammar.md) in the [C++](C++.md) programming language}@}. When the C++ grammar {@{cannot distinguish between [variable initialization](initialization%20(programming).md) and [function declaration](declaration%20(computer%20programming).md), it is required to interpret it as a function declaration}@}. <!--SR:!2027-12-13,1067,350!2026-10-11,719,330-->

## examples

Two common examples are caused by {@{C-style casts and unnamed temporary}@}. <!--SR:!2026-06-23,634,330-->

### C-style casts

The following grammar using C-style casts is ambiguous:

```C++
double a_double(3.14);
int an_int(int(a_double));
```

The intuitive interpretation of line 2 is {@{declaring a variable `an_int`, initializing it by converting `a_double` into an `int` first}@}. However, since {@{C allows superfluous parentheses around function parameter names, the above can also be interpreted as a function declaration, equivalent to}@}: <!--SR:!2027-02-08,806,330!2025-12-22,475,310-->

```C++
int an_int(int a_double);
```

### temporaries

The following grammar involving the creation of a temporary is ambiguous:

```C++
struct Child {};
struct Parent { explicit Parent(Child child); };
Parent parent(Child());
```

The intuitive interpretation of line 3 is {@{declaring a variable `parent`, initialized by passing a temporary instance of `Child` to the constructor parameter}@}. The alternative interpretation is {@{a function declaration named `parent` that has an unnamed parameter, whose type is (a pointer to) a function that accepts no inputs and returns a `Child`, equivalent to}@}: <!--SR:!2027-01-05,728,290!2025-09-17,367,290-->

```C++
Parent parent(Child(*)());
```

## solutions

The required interpretation of {@{a function declaration for the above ambiguous grammar is rarely the intended one}@}. To force the interpretation of a variable initialization, the typical solution is {@{using an alternative syntax that is unambiguous}@}. <!--SR:!2028-07-30,1247,350!2027-02-17,807,330-->

### solutions for C-style casts

For C-style casts, one can use two alternative syntaxes: {@{the alternative syntax for C-style casts, or more preferably in [C++](C++.md), a named cast}@}: <!--SR:!2027-02-24,819,330-->

```C++
int an_int((int)a_double); // C-style cast
int an_int(static_cast<int>(a_double)); // named cast, preferred in C++
```

### solutions for temporaries

Since [C++11](C++11.md), the preferred solution is {@{using uniform brace initialization, which uses `{}` instead of `()` to initialize variables. Additionally, sometimes the type name can be omitted with the brace syntax}@}: <!--SR:!2028-10-25,1226,310-->

```C++
// Any one works:
Parent parent(Child{});
Parent parent{Child()};
Parent parent{Child{}};
Parent parent(     {});
Parent parent{     {}};
```

Before [C++11](C++11.md), the two common solutions are {@{using extra parentheses or copy-initialization}@}: <!--SR:!2026-10-10,718,330-->

```C++
Parent parent((Child())); // extra parentheses
Parent parent = Parent(Child()); // copy-initialization
```

For copy-initialization, {@{the construction of a temporary after `=` is likely [optimized out](optimizing%20compiler.md) by the [compiler](compiler.md). Since [C++17](C++17.md), this optimization is guaranteed by the standard}@}. Note that the [C++17](C++17.md) standard {@{does not specify this as an optimization. It does not formally describe it as "[copy elision](copy%20elision.md)". Rather, it describes the temporary is not _materialized_ until the variable is initialized. This is called _deferred temporary materialization_}@}. <!--SR:!2026-03-23,543,310!2025-09-03,359,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/most_vexing_parse) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
