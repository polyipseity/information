---
aliases:
  - Python object
  - Python objects
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/object
  - language/in/English
---

# Python object

A Python class is never complete without teaching objects! (Sounds oddly familiar...)

## class

To create an object, one needs to first create a class. A class consists of {{a name, attributes, and methods}}: <!--SR:!2024-02-19,14,290-->

```Python
class Name:
  def __init__(self, an_attribute):
    self.an_attribute = an_attribute # attribute `an_attribute`
    self.another_attribute = 'asd' # attribute `another_attribute`

  def a_method(arg1, arg2):
    print(str(arg1) + str(an_attribute) + str(arg2))
```

Then to create an object, one uses {{the name of the class}}: <!--SR:!2024-02-20,15,290-->

```Python
name_object = Name(42)
```

The above object stored under `name_object` is also called {{an _instance_ of the class `Name`}}. <!--SR:!2024-02-22,17,290-->

## attribute

Note that Python attributes are not {{declared inside the class. Instead, they are assigned in the [constructor](#constructor)}}. <!--SR:!2024-04-13,55,310-->

## method

A method consists of {{a name, parameter names, and statement_block}}: <!--SR:!2024-02-21,16,290-->

```Python
def name(parameter_names):
  statement_block
```

Using the example above:

```Python
def a_method(arg1, arg2):
  print(str(arg1) + str(an_attribute) + str(arg2))
```

It is possible to have {{no parameters}}. Each parameter is {{separated by a comma `,`}}. <!--SR:!2024-02-19,14,290!2024-04-12,54,310-->

### constructor

A constructor is {{a special method that is called when you create an object of that class}}. It consists of {{a name that must be `__init__`, parameter names, and statement_block}}: <!--SR:!2024-02-21,16,290!2024-02-22,17,290-->

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
