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

To {@{create an object}@}, one needs to {@{first create a class}@}. A class consists of {@{a name, attributes, and methods}@}: <!--SR:!fsrs,2029-09-19T00:00:00.000Z,1115,1114.75652523,1,2,9,0,0,2026-08-31T00:00:00.000Z!2026-11-17,310,340!2026-11-19,312,340-->

```Python
class Name:
  def __init__(self, an_attribute):
    self.an_attribute = an_attribute # attribute `an_attribute`
    self.another_attribute = 'asd' # attribute `another_attribute`

  def a_method(arg1, arg2):
    print(str(arg1) + str(an_attribute) + str(arg2))
```

Then to create an object, one uses {@{the name of the class}@}: <!--SR:!fsrs,2029-12-05T00:00:00.000Z,1165,1164.5679841,1,2,9,0,0,2026-09-27T00:00:00.000Z-->

```Python
name_object = Name(42)
```

The above object stored under `name_object` is also called {@{an _instance_ of the class `Name`}@}. <!--SR:!fsrs,2028-09-24T00:00:00.000Z,733,732.76739939,2.49272837,2,9,0,0,2026-09-22T00:00:00.000Z-->

## attribute

Note that Python attributes are not {@{declared inside the class}@}. Instead, they are {@{assigned in the [constructor](#constructor)}@}. <!--SR:!2028-02-27,666,330!2026-11-11,311,340-->

## method

A method consists of {@{a name, parameter names, and statement block}@}: <!--SR:!fsrs,2029-12-29T00:00:00.000Z,1184,1183.64577796,1,2,9,0,0,2026-10-02T00:00:00.000Z-->

```Python
def name(parameter_names):
  statement_block
```

Using the example above:

```Python
def a_method(arg1, arg2):
  print(str(arg1) + str(an_attribute) + str(arg2))
```

It is possible to have {@{no parameters}@}. Each parameter is {@{separated by a comma `,`}@}. <!--SR:!2026-10-14,283,330!fsrs,2028-09-10T00:00:00.000Z,723,722.71793178,2.49272837,2,9,0,0,2026-09-18T00:00:00.000Z-->

### constructor

A constructor is {@{a special method that is called when you create an object of that class}@}. It consists of {@{a name that must be `__init__`, parameter names, and statement block}@}: <!--SR:!2026-10-07,276,330!fsrs,2029-08-19T00:00:00.000Z,1092,1091.66087084,1,2,9,0,0,2026-08-23T00:00:00.000Z-->

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
