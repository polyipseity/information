---
aliases:
  - Java object
  - Java objects
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/object
  - language/in/English
---

# Java object

A Java class is never complete without teaching objects!

To help with debugging objects, one can use {{the [object bench](BlueJ.md#object%20bench)}} in BlueJ. <!--SR:!2024-09-15,157,310-->

## almost everything is an object

In Java, {{everything except for primitive types}} are objects. Primitive types include {{`boolean`, `byte`, `char`, `double`, `float`, `short`, `int`, and `long`}}. <!--SR:!2024-12-20,246,330!2024-04-23,62,310-->

## equality

Comparing equality of objects uses {{`equals` in most cases. Non-objects always use `==`}}. <!--SR:!2024-11-21,224,330-->

This explains why `equals` is used instead of `==` for `String`s in [string § equality](string.md#equality).

## class

To create an object, one needs to first create a class. A class consists of {{a name, fields (i.e. properties of an object), and methods}}: <!--SR:!2024-05-05,73,310-->

```Java
public class Name {
  int aField;
  String anotherField = "asd";

  Name(int aField) {
    this.aField = aField;
  }

  void aMethod(String arg1, int arg2) {
    System.out.println(arg1 + aField + String.valueOf(arg2));
  }

  static void aStaticMethod() {
    System.out.println("aStaticMethod");
  }
}
```

To make the class accessible to code in other files, {{prepend `public` before `class` and ensure the file containing the class has the same filename (excluding the `.java` extension) as the class name. In this example, `Name.java` is the filename}}. <!--SR:!2024-04-25,64,310-->

Then to create an object, one uses {{`new`}}: <!--SR:!2024-04-30,68,310-->

```Java
Name nameObject = new Name(42);
```

The above object stored under `nameObject` is also called {{an _instance_ of the class `Name`}}. <!--SR:!2024-05-03,71,310-->

## method

A method consists of {{a return type, name, parameters, parameter names, and a statement block}}: <!--SR:!2024-09-29,166,310-->

```Java
ReturnType name(ParameterTypes parameterNames) {
  statements;
}
```

Using the example above:

```Java
void aMethod(String arg1, int arg2) {
  System.out.println(arg1 + aField + String.valueOf(arg2));
}
```

The return type indicates {{the type of the method output}}. The `void` type is {{a special return type indicating no method output}}. To return a non-`void` value, use {{`return`, like `return valueOfReturnType;`}}. <!--SR:!2024-04-22,61,310!2024-04-19,59,310!2024-09-25,166,310-->

The parameter types indicates {{the types of the method inputs}}. It is possible to have {{no parameters}}. Each parameter is {{separated by `,`, with the parameter type appearing before the parameter name}}. <!--SR:!2024-12-21,247,330!2024-10-02,170,310!2024-05-02,70,310-->

### constructor

A constructor is {{a special method that is called when you create an object of that class using `new`}}. It consists of {{a name that must be the same as the class name, parameter types, parameter names, and statements}}: <!--SR:!2024-09-11,153,310!2024-09-28,166,310-->

```Java
ClassName(ParameterTypes parameterNames) {
  statements;
}
```

Using the example above:

```Java
Name(int aField) {
  this.aField = aField;
}
```

### static

By adding `static` before {{the return type of a method, the method can be called without creating an object first. The restriction is that non-`static` methods and non-`static` fields cannot be accessed directly without an object, as there are no objects to access them on}}. For example, invoking `aStaticMethod` in the above example: <!--SR:!2024-04-21,60,310-->

```Java
Name name = new Name(42);
name.aMethod("42", 42);
// Name.aMethod("42", 42); // compilation error
Name.aStaticMethod();
```

Importantly, {{the `main` method}} is `static` and has the following form: <!--SR:!2024-10-05,173,310-->

```Java
public static void main(String[] args) {
  System.out.println("Hello, world!");
}
```
