---
aliases:
  - Python object
  - Python objects
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/object
  - language/in/English
---

# Python object

A Python class is never complete without teaching objects! \(Sounds oddly familiar...\)

## class

To {@{create an object}@}, one needs to {@{first create a class}@}. A class consists of {@{a name, attributes, and methods}@}:

```Python
class Name:
  def __init__(self, an_attribute):
    self.an_attribute = an_attribute # attribute `an_attribute`
    self.another_attribute = 'asd' # attribute `another_attribute`

  def a_method(arg1, arg2):
    print(str(arg1) + str(an_attribute) + str(arg2))
```

Then to create an object, one uses {@{the name of the class}@}:

```Python
name_object = Name(42)
```

The above object stored under `name_object` is also called {@{an _instance_ of the class `Name`}@}.

## attribute

Note that Python attributes are not {@{declared inside the class}@}. Instead, they are {@{assigned in the [constructor](#constructor)}@}.

## method

A method consists of {@{a name, parameter names, and statement block}@}:

```Python
def name(parameter_names):
  statement_block
```

Using the example above:

```Python
def a_method(arg1, arg2):
  print(str(arg1) + str(an_attribute) + str(arg2))
```

It is possible to have {@{no parameters}@}. Each parameter is {@{separated by a comma `,`}@}.

### constructor

A constructor is {@{a special method that is called when you create an object of that class}@}. It consists of {@{a name that must be `__init__`, parameter names, and statement block}@}:

```Python
def __init__(parameter_names):
  statement_block
```

Using the example above:

```Python
def __init__(self, an_attribute):
  self.an_attribute = an_attribute
  self.another_attribute = 'asd'
```
