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

To {@{create an object}@}, one needs to {@{first create a class}@}. A class consists of {@{a name, attributes, and methods}@}: <!--SR:!2026-08-30,252,330!2026-11-17,310,340!2026-11-19,312,340-->

```Python
class Name:
  def __init__(self, an_attribute):
    self.an_attribute = an_attribute # attribute `an_attribute`
    self.another_attribute = 'asd' # attribute `another_attribute`

  def a_method(arg1, arg2):
    print(str(arg1) + str(an_attribute) + str(arg2))
```

Then to create an object, one uses {@{the name of the class}@}: <!--SR:!2026-09-26,265,330-->

```Python
name_object = Name(42)
```

The above object stored under `name_object` is also called {@{an _instance_ of the class `Name`}@}. <!--SR:!2026-09-21,260,330-->

## attribute

Note that Python attributes are not {@{declared inside the class}@}. Instead, they are {@{assigned in the [constructor](#constructor)}@}. <!--SR:!2026-04-30,154,310!2026-11-11,311,340-->

## method

A method consists of {@{a name, parameter names, and statement block}@}: <!--SR:!2026-10-01,270,330-->

```Python
def name(parameter_names):
  statement_block
```

Using the example above:

```Python
def a_method(arg1, arg2):
  print(str(arg1) + str(an_attribute) + str(arg2))
```

It is possible to have {@{no parameters}@}. Each parameter is {@{separated by a comma `,`}@}. <!--SR:!2026-10-14,283,330!2026-09-17,256,330-->

### constructor

A constructor is {@{a special method that is called when you create an object of that class}@}. It consists of {@{a name that must be `__init__`, parameter names, and statement block}@}: <!--SR:!2026-10-07,276,330!2026-08-22,246,330-->

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
