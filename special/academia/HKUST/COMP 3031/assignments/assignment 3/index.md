---
aliases:
  - COMP3031 assignment 3
  - COMP 3031 assignment 3
  - HKUST COMP3031 assignment 3
  - HKUST COMP 3031 assignment 3
tags:
  - date/2025/12/02
  - flashcard/active/special/academia/HKUST/COMP_3031/assignments/assignment_3
  - language/in/English
---

# assignment 3

- HKUST COMP 3031

---

- title: Assignment 3: Lisp Interpreter
- due: 2025-12-07T23:59:59+08:00
- points: 10
- submitting: file upload
- file types: zip

---

- [`ass3.zip`](attachments/ass3.zip)

---

Download the skeleton project at [ass3.zip](attachments/ass3.zip).

The goal of this assignment is to extend the Scheme-- interpreter from the lecture to include more features, namely class-based pattern matching and call-by-need evaluation.

The skeleton code is essentially the same as the implementation presented in the lecture. You are free to modify any of the files in `src/main/scala/ass3` _except_ `Lisp.scala` and `InterpreterInterface.scala`.

## Class declarations

The first step is to interpret class declarations and store the appropriate information in the `tydefs` environment. Class declarations are expressions in the following special form:

```Scheme
(class (<name> { <field> }) <rest>)
```

where `{ }` denotes zero or more repetitions. `<rest>` is evaluated in an environment extended with the declaration of the class `<name>` with fields `{ <field> }`, which can be used for object construction, field selection, and pattern matching.

To distinguish class names `<name>`, field names `<field>`, and variable names `<param>`, we restrict class names to begin with an upper-case alphabet; and field names and variable names to begin with a lower-case alphabet. When a class, variable, or pattern violating these restrictions is declared, a `SyntaxError` should be thrown. You can use the `paramName`, `fieldName`, and `className` helpers to convert symbols to strings while checking for the case restrictions.

The information stored in the `tydefs` environment is not examined. You are free to decide what to store.

## Object construction

An object of a class can be constructed by applying the constructor to a sequence of arguments. For example, the following constructs an object of class `Pair` with the values `1` and `2` for fields `x` and `y` respectively:

```Scheme
(class (Pair x y) (Pair 1 2))
```

The number of arguments applied to the constructor must match exactly the arity of the class declaration. Otherwise, a `ClassArityMismatch` with the message `"wrong arity for class <name>"` is thrown, where `<name>` is the class name. Just like functions, constructors cannot be partially applied. For example, both of the following result in an error:

```Scheme
(class (Pair x y) (Pair 1))
(class (Pair x y) (Pair 1 2 3))
```

The behavior of evaluating an unapplied constructor is unspecified. For example, the behavior of the following program is unspecified:

```Scheme
(class (Pair x y) Pair)
```

To implement object construction, you may want to define additional syntax forms.

## Field selection

Fields of an object can be accessed using the field selection special form:

```Scheme
(sel <expr> <field>)
```

`<expr>` is first evaluated. If `<expr>` evaluates to an object `o` of class `C`, and \(1\) `C` has field `<field>`, then the whole expression evaluates to the value of the field `<field>` of `o`; \(2\) `C` does not have field `<field>`, then a `FieldError` with message `"class C has no field <field>"` is thrown. If `<expr>` evaluates to something other than an object, then a `SelError` with the message `"selection from a non-object: o"` is thrown.

## Pattern matching

The class of an object can be inspected at runtime using pattern matching, with the following special form:

```Scheme
(case <scrut> { <branch> })
```

where case branches `<branch>` are one of the following.

```BNF
<branch> =   ((<name> { <param> }) <expr>)
           | (<param> <expr>)
```

`<scrut>` is first evaluated to `v`, then matched against `{ <branch> }` in order. If a branch is matched, then that branch is taken. The remaining branches would not be processed. If a branch is not matched, then pattern matching proceeds to the next branch. If all branches are not matched or `v` is not an object, then a MatchError with the message `"match error on: <scrut>"` is thrown.

If a branch is in the first form `((<name> { <param> }) <expr>)`, then the class definition of class `<name>` is looked up. The size of `{ <param> }` must match exactly the arity of class `<name>`, otherwise a `ClassArityMismatch` with the message `"wrong arity for class <name>"` is thrown. If `v` is an object of class `<name>`, then the branch is matched, and `<expr>` is evaluated in an environment extended by binding each of `{ <param> }` to the respective fields of `v`. For example, in the following expression, `<expr>` is evaluated in an environment extended with bindings `a -> 1` and `b -> 2`:

```Scheme
(class (Pair x y) (case (Pair 1 2) ((Pair a b) <expr>)))
```

If a branch is in the second form `(<param> <expr>)`, then it is always matched. `<expr>` is evaluated in an environment extended by binding `<param>` to `v`. For example, in the following expression, `<expr>` is evaluated in an environment extended with binding `x -> Pair 1 2`:

```Scheme
(class (Pair x y) (case (Pair 1 2) (x <expr>)))
```

If a branch does not match either form, then a `SyntaxError` with the message `"invalid case branch: <branch>"` is thrown.

## Call-by-need

The final part of the assignment is to implement the call-by-need evaluation strategy, for val bindings, function arguments, and constructor arguments. Call-by-need is similar to call-by-name, where the arguments are not evaluated until their value is accessed. However, unlike call-by-name, the arguments are only evaluated once, after which the result is stored for further access.

For val bindings, they are accessed only when the bound variable is evaluated inside the body. For example, in the following program, the expression `<expr>` is never evaluated:

```Scheme
(val x <expr> 0)
```

In the following program, the expression `<expr>` is only evaluated once:

```Scheme
(val x <expr> (* x x))
```

For function arguments, they are accessed only when the corresponding parameter is evaluated inside the function body. For example, in the following program, the expressions `(id <expr>)` and `<expr>` are never evaluated:

```Scheme
(def id (lambda (x) x) (def zero (lambda (x) 0) (zero (id <expr>))))
```

In the following program, the expressions `(sq (sq <expr>))`, `(sq <expr>)`, and `<expr>` are each only evaluated once:

```Scheme
(def sq (lambda (x) (* x x)) (sq (sq (sq <expr>))))
```

For constructor arguments, they are accessed only when a selection is evaluated, or when a variable bound by pattern matching is evaluated. Namely, constructing an object does not evaluate any of the arguments. For example, in the following programs, the expressions `<expr1>` and `<expr2>` are never evaluated:

```Scheme
(class (Pair x y) (def zero (lambda (x) 0) (val x (Pair <expr1> <expr2>) (zero (sel x x)))))
(class (Pair x y) (def zero (lambda (x) 0) (case (Pair <expr1> <expr2>) ((Pair a b) (zero a)))))
```

In the following programs, the expression `<expr1>` is evaluated once, while `<expr2>` is never evaluated:

```Scheme
(class (Pair x y) (val x (Pair <expr1> <expr2>) (* (sel x x) (sel x x))))
(class (Pair x y) (case (Pair <expr1> <expr2>) ((Pair a b) (* a a))))
```

To implement call-by-need, you may define a wrapper around arguments. You may also want to wrap arguments in these wrappers before applying a function or constructor to them, change what the interpreter does when it encounters these wrappers, and change the builtin functions to take these wrappers.

## Restriction

You are not allowed to use any mutable collections, or mutable variables referring to collections beside `Option`. You are not allowed to modify the files `Lisp.scala` and `InterpreterInterface.scala`.

## Submission

Please refer to the Canvas assignment page for the deadline.

Submit a single `zip` archive containing the source files. All files will be extracted to the `src/main/scala/ass3` directory of the skeleton, replacing any existing files.

## FAQ

1. Name conflict

    Q: Can we assume there won't be a conflict of class names and variable names?

    A: Class names and variable names won't conflict with each other since class names begin with upper case and variable names begin with lower case. But there may be duplicate class names and variable names. The new definition would shadow the old one, but any existing definitions would still refer to the original definition. For example, `(def f 1 (def g f (def f 2 g)))` would evaluate to 1, and `(class (Pair x y) (val p (Pair 1 2) (class (Pair y x) (sel p x))))` would evaluate to 1. There is no way to pattern match on a shadowed class but selection should still work as intended. <br/>
    You can assume that field names within a class declaration are distinct. Duplicate field names won't be tested, so you can return any one of them, or throw an exception when you encounter such declarations.
2. Class declaration scope

    Q: What would happen when an object is returned outside the scope of its class declaration? For example `(sel (class (Pair x y) (Pair 1 2)) x)`.

    A: You can assume class declarations are properly scoped, i.e. the class definition would be visible at any selection or pattern matching. So only `(class (Pair x y) (sel (Pair 1 2) x))` would be tested. \(On the other hand, it is also fine to handle this case, it just won't be tested.\)

3. Object value

    Q: What should an object evaluate to? For example `(class (Pair x y) (Pair 1 2))`.

    A: It should evaluate to your internal representation of objects. Since it would be added by you, this will not really be tested. But namely it should not be equal to representations of other values, such as integers, strings, `Lambda`s, etc. Otherwise it can be used as other types.

4. Call-by-need evaluation

    Q: Can you give an example to demonstrate how call-by-need works?

    A: Consider the following example:

    ```Scheme
    (def sq1 (lambda (x) (* x x)) (def sq2 (lambda (y) (sq1 y)) (sq2 <expr>)))
    ```

    The body of `sq2` \(`(sq1 y)`\) would be evaluated in an environment with `<expr>` bound to `y` \(`env1`\), then the body of `sq1` \(`(* x x)`\) would be evaluated in an environment with `y` bound to `x` \(`env2`\). When the multiplication is evaluated, the two operands are evaluated first. When the first operand `x` is evaluated, it is looked up from `env2` and the expression \(`y`\) is evaluated in `env1`, then `y` is looked up from `env1` and the expression \(`<expr>`\) is evaluated in the original environment. When the second operand `x` is evaluated, the result from the last evaluation is used instead of evaluating it again. Finally the multiplication evaluates to the product of the result of evaluating the two operands.

5. Forcing evaluation

    Q: When exactly is an evaluation performed under call-by-need?

    A: \(1\) Evaluating a variable, and \(2\) applying a variable to the built-in functions. Arguments to all built-in functions are evaluated.

## submission

- file: [`submission.zip`](submission.zip)
  - source: [`submission/`](submission/)
