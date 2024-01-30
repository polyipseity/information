---
aliases:
  - Java object
  - Java objects
tags:
  - flashcards/special/academic/HKUST/COMP_1029J/object
  - languages/in/English
---

# Java object

A Java class is never complete without teaching objects!

To help with debugging objects, one can use the {{[object bench](BlueJ.md#object%20bench)}} in BlueJ.

## almost everything is an object

In Java, {{everything except for primitive types}} are objects. Primitive types include {{`boolean`, `char`, `byte`, `short`, `int`, `long`, `float`, and `double`}}.

## equality

Comparing equality of objects uses {{`equals` in most cases. Non-objects always use `==`}}.

This explains why `equals` is used instead of `==` for `String`s in [string § equality](string.md#equality).

## class

To create a object, one needs to first create a class. A class consists of {{a name, fields (i.e. properties of an object), and methods}}:

```Java
class Name {
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

To make the class accessible to code in other files, {{prepend `public` before `class` and ensure the file containing the class has the same filename (excluding the `.java` extension) as the class name. In this example, `Name.java` is the filename}}.

Then to create a object, one uses {{`new`}}:

```Java
Name nameObject = new Name(42);
```

The above object stored under `nameObject` is also called {{an _instance_ of the class `Name`}}.

## method

A method consists of {{a return type, name, parameters, parameter names, and statements}}:

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

The return type indicates the {{type of the method output}}. The `void` type is {{a special return type indicating no method output}}. To return a non-`void` value, use {{`return`, like `return valueOfReturnType;`}}.

The parameter types indicates the {{type(s) of the method input(s)}}. It is possible to have {{no parameters}}. Each parameter is {{separated by `,`, with the parameter type appearing before the parameter name}}.

### constructor

A constructor is {{a special method that is called when you create a object of that class using `new`}}. It consists of {{a name that must be the same as the class name, parameter types, parameter names, and statements}}:

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

By adding `static` before {{the return type of a method, the method can be called without creating an object first. The restriction is that non-`static` methods and non-`static` fields cannot be accessed directly without an object, as there is no object to access them on}}. For example, `aStaticMethod` in the above example can be called:

```Java
Name name = new Name(42);
name.aMethod("42", 42);
// Name.aMethod("42", 42); // compilation error
Name.aStaticMethod();
```

Importantly, {{the `main` method}} is `static` and has the following form:

```Java
public static void main(String[] args) {
  System.out.println("Hello, world!");
}
```
