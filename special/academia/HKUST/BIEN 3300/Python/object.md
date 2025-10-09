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

To {@{create an object}@}, one needs to {@{first create a class}@}. A class consists of {@{a name, attributes, and methods}@}: <!--SR:!2025-12-21,58,310!2025-10-27,17,300!2025-10-27,17,300-->

```Python
class Name:
  def __init__(self, an_attribute):
    self.an_attribute = an_attribute # attribute `an_attribute`
    self.another_attribute = 'asd' # attribute `another_attribute`

  def a_method(arg1, arg2):
    print(str(arg1) + str(an_attribute) + str(arg2))
```

Then to create an object, one uses {@{the name of the class}@}: <!--SR:!2025-12-26,61,310-->

```Python
name_object = Name(42)
```

The above object stored under `name_object` is also called {@{an _instance_ of the class `Name`}@}. <!--SR:!2025-12-24,60,310-->

## attribute

Note that Python attributes are not {@{declared inside the class}@}. Instead, they are {@{assigned in the [constructor](#constructor)}@}. <!--SR:!2025-11-27,38,290!2025-10-27,17,300-->

## method

A method consists of {@{a name, parameter names, and statement block}@}: <!--SR:!2025-12-27,62,310-->

```Python
def name(parameter_names):
  statement_block
```

Using the example above:

```Python
def a_method(arg1, arg2):
  print(str(arg1) + str(an_attribute) + str(arg2))
```

It is possible to have {@{no parameters}@}. Each parameter is {@{separated by a comma `,`}@}. <!--SR:!2025-12-31,66,310!2025-12-23,59,310-->

### constructor

A constructor is {@{a special method that is called when you create an object of that class}@}. It consists of {@{a name that must be `__init__`, parameter names, and statement block}@}: <!--SR:!2025-12-27,63,310!2025-12-19,56,310-->

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
