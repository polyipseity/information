---
aliases:
  - COMP 2211
  - COMP 2211 index
  - COMP2211
  - COMP2211 index
  - HKUST COMP 2211
  - HKUST COMP 2211 index
  - HKUST COMP2211
  - HKUST COMP2211 index
tags:
  - flashcard/active/special/academia/HKUST/COMP_2211/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 2211
- name: Exploring Artificial Intelligence

The content is in teaching order.

- course logistics
  - labs
    - No labs for the first 2 weeks. Labs start at week 3.
    - format: 60 minute tutorial, 50 minute Q&A session
    - attendance: first 20 minutes
  - marking scheme: 100%
    - coursework: 40%
      - 10 lab exercises: 10%
        - formula: (attendance points + best 4 lab scores from ZINC) / 49 \* 10
      - 2 individual programming assignments: 30%
    - examination: 60%
      - midterm examination: 20%
      - final examination: 40%
  - midterm examination
    - datetime: 2024-10-31T20:00:00+08:00/2024-10-31T22:00:00+08:00, PT2H
    - venue: Lecture Theater A
    - scope
      - introduction to artificial intelligence
      - advanced Python for artificial intelligence
      - naive Bayes classifier
      - k-nearest neighbors
      - k-means clustering
      - artificial neural network - perceptron
      - artificial neural network - multi-layer perceptron (P.16)
  - final examination
- objectives ::: gentle introduction to artificial intelligence (AI), technical aspects, historical aspects, social implications, ethical implications, potentials, and limitations of AI <!--SR:!2024-11-14,10,272!2024-11-16,13,272-->
- topics
  - brief history of artificial intelligence
  - search and problem solving
  - knowledge representation
  - probabilistic reasoning
  - machine learning
  - computer vision and image processing
  - speech and language processing
  - robotics
  - social and ethical implications of AI
  - potential and limitations
  - naive Bayes
  - k-nearest neighbour
  - k-means clustering
  - perceptron and multi-layer perceptron
  - fundamentals of image processing
  - convolutional neural networks
  - minimax and alpha-beta pruning
  - artificial intelligence ethics
  - reinforcement learning (self-study)
- other materials
  - 12 self-tests
  - past exam papers: 2022 spring/midterm exam, 2022 spring/final exam

## week 1 lecture

- datetime: 2024-09-04T13:30:00+08:00/2024-09-04T14:50:00+08:00
- course logistics
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI)  
  - artificial intelligence / definition ::: no widely accepted definition <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
    - artificial intelligence / definition / Alan Turing ::: AI is the __science and engineering__ of __making intelligent machines__, especially intelligent computer programs. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
  - artificial intelligence / characteristics ::: AI borrows characteristics from human intelligence and applies them as algorithms in a computer-friendly way. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - artificial intelligence / reasons for studying ::: AI is versatile (skillful), brighter career, skill of the century <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
  - artificial intelligence / academic disciplines ::: philosophy and cognition science, mathematics, neuroscience, psychology, computer science, linguistics, ... (many, remember some) <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
  - artificial intelligence / importance ::: air transport, banking and finance, computer vision, e-commerce, expert systems (for decision making), gaming and entertainment, healthcare, hiring, logistics, natural language processing, speech recognition, ... (many, remember some) <!--SR:!2024-11-19,15,310!2024-11-15,11,290-->
  - artificial intelligence / commonly confused terms ::: artificial intelligence, deep learning, machine learning, neural network <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
    - machine learning ::: a subfield of _artificial intelligence_ that provides systems with the ability to automatically learn and improve from experience without being explicitly programmed <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - neural network ::: an _algorithm_ in _machine learning_ to solve problems <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - deep learning ::: a subfield of _machine learning_ that uses _neural networks_ to analyze different factors with a structure similar to the human neural system <!--SR:!2024-11-16,12,290!2024-11-20,16,310-->

## week 1 lab

- datetime: 2024-09-05T16:30:00+08:00/2024-09-05T18:20:00+08:00
- status: unscheduled, no lab

## week 1 lecture 2

- datetime: 2024-09-06T13:30:00+08:00/2024-09-06T14:50:00+08:00
- online, typhoon signal 8
- artificial intelligence
  - artificial intelligence / advantages ::: available always, digital assistance, faster decisions, innovation (new inventions), reduction in human errors, repetitive work helping, taking risks instead of humans <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
  - artificial intelligence / disadvantages ::: high cost of creation and maintenance, lack out-of-the-box thinking, make humans lazy, unemotional, unemployment <!--SR:!2024-11-15,11,290!2024-11-19,15,310-->
  - artificial intelligence / prerequisites ::: algorithms, data analysis, mathematics, programming, will to learn <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - artificial intelligence / periods
    - artificial intelligence / periods / 1950–1956 ::: birth of artificial intelligence <!--SR:!2024-11-16,13,290!2024-11-18,14,292-->
    - artificial intelligence / periods / 1956–1974 ::: symbolic AI <!--SR:!2024-11-16,12,290!2024-11-10,7,270-->
    - artificial intelligence / periods / 1974–1980 ::: the first AI winter <!--SR:!2024-11-16,12,290!2024-11-14,10,272-->
    - artificial intelligence / periods / 1980–1987 ::: AI boom <!--SR:!2024-11-16,13,290!2024-11-16,13,290-->
    - artificial intelligence / periods / 1987–1993 ::: the second AI winter <!--SR:!2024-11-18,14,292!2024-11-16,13,272-->
    - artificial intelligence / periods / 1993–2011 ::: AI finally achieved some of its oldest goals, beginning to be adopted throughout the technology industry due to increasing computing power <!--SR:!2024-11-18,14,292!2024-11-16,13,272-->
    - artificial intelligence / periods / 2011–present (2024) ::: artificial general intelligence, big data, deep learning <!--SR:!2024-11-21,17,310!2024-11-15,11,290-->
  - artificial intelligence / history
    - artificial intelligence / history / 1950 ::: English mathematician and computer scientist Alan Turing: __Can machines think?__ (_Computing Machinery and Intelligence_) __How would we know if we have succeeded?__ <p> He also predicted by 2000, a machine might have a 30% of fooling a layman for 5 minutes. <!--SR:!2024-11-19,15,310!2024-11-20,16,310-->
      - Turing test ::: A test to empirically determine whether a computer has achieved intelligence. A human questioner questions two respondents, one human, the other a computer function, whose identities are unknown to the human questioner. Using a specified format and context, the questioner interrogates the two respondents within a specific subject area. After a preset length of time or number of questions, the questioner is then asked to decide which respondent is human and which is a computer. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
    - artificial intelligence / history / 1956 ::: John McCarthy coined the term "__artificial intelligence__" as the topic of the Dartmouth Conference, the first conference devoted to the subject. <!--SR:!2024-11-18,14,292!2024-11-10,7,270-->
    - artificial intelligence / history / 1959 ::: Arthur Samuel coined the term "__machine learning__", reporting on programming a computer "so that it will learn to play a better game of checkers than can be played by the person who wrote the program". <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - artificial intelligence / history / 1965 ::: The _first natural language processing computer program_, __ELIZA__, was created. <!--SR:!2024-11-19,15,310!2024-11-15,11,290-->
    - artificial intelligence / history / 1980s ::: Edward Albert Feigenbaum developed the _first expert system in artificial intelligence_. <!--SR:!2024-11-16,12,290!2024-11-21,17,310-->
    - artificial intelligence / history / 1990s ::: Cynthia Breazeal, a pioneer of _social robotics_ and _human–robot interaction_, created the robot __Kismet__ at MIT in 1990s. Kismet was designed to engage in social interaction with humans, marking a significant step forward in the field of human-robot interaction. Breazeal's work has opened up new possibilities for how humans and robots can interact and coexist. <!--SR:!2024-11-10,7,252!2024-11-16,13,272-->
    - artificial intelligence / history / 1997 ::: An IBM computer called __IBM Deep Blue__ _beat the world chess champion_, Garry Kasparov, after a six-game match: two wins for IBM, one for the champion and three draws. <!--SR:!2024-11-10,7,252!2024-11-14,10,272-->
    - artificial intelligence / history / 2002 ::: iRobot launched __Roomba__, an _autonomous vacuum cleaner that avoids obstacles_. <!--SR:!2024-11-18,14,292!2024-11-19,15,292-->
    - artificial intelligence / history / 2009 ::: Google built the _first self-driving car_ to handle urban conditions. <!--SR:!2024-11-20,16,310!2024-11-16,13,290-->
    - artificial intelligence / history / 2011 ::: IBM's __Watson__ supercomputer _defeated humans in the final Jeopardy match_. <!--SR:!2024-11-14,10,272!2024-11-16,13,290-->
    - artificial intelligence / history / 2011–2014 ::: _Personal assistants_ like Siri, Google Now, Cortana use _speech recognition_ to answer questions and perform simple tasks. <!--SR:!2024-11-16,13,290!2024-11-18,14,292-->
    - artificial intelligence / history / 2014 ::: Ian Goodfellow comes up with __Generative Adversarial Network__ (__GAN__). <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
    - artificial intelligence / history / 2016 ::: __AlphaGo__ _beats professional Go player_ Lee Sedol 4-1. <!--SR:!2024-11-10,7,270!2024-11-16,13,290-->
    - artificial intelligence / history / 2018 ::: Most universities _have courses in artificial intelligence_, including HKUST. (shameless self-plug) <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
    - artificial intelligence / history / 2022 ::: The release of __ChatGPT__ (__Chat Generative Pre-trained Transformer__), a _large language model trained by OpenAI_, demonstrated the enormous potential of AI for transforming the way we communicate and interact with machines. <p> ChatGPT is an AI-powered language model developed by OpenAI, capable of _generating human-like text based on context and past conversations_. <!--SR:!2024-11-07,4,306!2024-11-07,4,306-->
    - artificial intelligence / history / 2023 ::: The release of __Bard__. Bard is an experimental conversational AI chat service developed by Google. It operates in a similar manner to ChatGPT, but with a notable distinction: Bard _retrieves information directly from the web as a source of knowledge_. <!--SR:!2024-11-21,17,310!2024-11-15,11,290-->
  - artificial intelligence / libraries ::: Keras, PyTorch, TensorFlow, scikit-learn <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - Keras ::: (moderately customizable and flexible; moderate difficulty; good for beginners) It is a high-level application programming interface (API) built on top of TensorFlow. It is incredibly user-friendly and easy to pick up. It is good for fast experimentation. <!--SR:!2024-11-21,17,310!2024-11-10,7,270-->
    - PyTorch ::: (very customizable and flexible; high difficulty; bad documentation) It is TensorFlow's direct competitor developed by Facebook, and is widely used in research projects. It allows almost unlimited customization and is well adapted to running tensor operations on GPUs. <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
    - TensorFlow ::: (most customizable and flexible; highest difficultly; good documentation) It is a machine learning framework from Google. It is a fast, flexible, and scalable open-source machine learning library for research and production. With TensorFlow 2.0 and newer versions, more efficiency and convenience was brought to the game. <!--SR:!2024-11-16,13,290!2024-11-19,15,292-->
    - scikit-learn ::: (least customizable and flexible; low difficulty; good for beginners) It is another user-friendly framework that contains a great variety of useful tools: classification, regressions and clustering models, as well as pre-processing, dimensionality reduction and evaluation tools. <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
  - artificial intelligence / Python ::: Many artificial intelligence projects are written using mostly Python. <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - artificial intelligence / Python / advantages ::: easy to integrate with other programming languages; easy to learn and read; popular and large community; vast AI ecosystem of libraries, tools, and examples <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
    - artificial intelligence / Python / disadvantages ::: design limitations; unsuitable for mobile and game development; speed limitations (addressed by interfacing native code with Python) <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
- [Python](../../../../general/Python%20(programming%20language).md)
  - Python / version ::: We use Python 3.10.2. Check your version via `print(sys.version)` after `import sys`. <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
  - advanced Python
    - advanced Python / `type(value)` ::: Returns the type of `value`. When the type is printed, it produces, for example, `<class 'int'>`. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
    - advanced Python / list comprehension ::: `[<expression> for <element> in <iterable> if <condition>]` <p> `if <condition>` is optional. It produces a `list` consisting of elements after evaluating `<expression>` on each `<element>` in `<iterable>`. If `<condition>` is present and returns false for an `<element>`, `<expression>` is not evaluated and not added to the `list`. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->

## week 2 lecture

- datetime: 2024-09-11T13:30:00+08:00/2024-09-11T14:50:00+08:00
- Python
  - advanced Python
    - advanced Python / dictionary comprehension ::: `{<key expression>: <value expression> for <element> in <iterable> if <condition>}` <p> `if <condition>` is optional. It produces a `dict` consisting of the key-value pairs after evaluating `<key expression>: <value expression>` on each `<element>` in `<iterable>`. If `<condition>` is present and returns false for an `<element>`, `<key expression>: <value expression>` is not evaluated and not added to the `dict`. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
    - advanced Python / set comprehension ::: `{<expression> for <element> in <iterable> if <condition>}` <p> `if <condition>` is optional. It produces a `set` consisting of elements after evaluating `<expression>` on each `<element>` in `<iterable>`. If `<condition>` is present and returns false for an `<element>`, `<expression>` is not evaluated and not added to the `set`. <p> Note that a `set` cannot contain duplicate elements and is unordered (order may change randomly after performing operations on it). <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
    - advanced Python / `list` vs `tuple` ::: Both can store a ordered sequence of elements of any or mixed types. However, `list` is mutable (modifiable) while `tuple` is immutable (unmodifiable). <p> `list` can neither be used as `dict` keys (values are fine) nor stored inside a `set`. `tuple` can be used as `dict` keys and stored inside a `set`. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
    - advanced Python / `zip(iterables...)` ::: `zip` takes one or more iterables, and returns an iterator. Every time you extract an element from the iterator, each of the passed iterables has an element extracted in the order of being passed into `zip`, and then the elements are zipped together into a `tuple`. <p> The iterable with the least number of elements determines how many elements you  can extract from the iterator. <p> Example: `for fruit, color in zip(fruits, colors): ...`. <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
    - advanced Python / variable (positional) arguments ::: One can accept a variable number of (positional) arguments by adding a parameter `*<parameter name>` at the end. Any extra (positional) arguments will go into `<parameter name>` as a `tuple`. <p> Example: `def haha(a_parameter, *extra_parameters_as_a_tuple): ...`. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
    - advanced Python / variable keyword arguments ::: One can accept a variable number of _keyword_ arguments by adding a parameter `**<parameter name>` at the end. Any extra _keyword_ arguments will go into `<parameter name>` as a `dict`. <p> Example: `def haha(a_parameter, **extra_keyword_parameters_as_a_dict): ...`. <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
    - advanced Python / object-oriented programming (OOP) ::: __Object-oriented programming__ structures programs by bundling related properties (instance variables) and behaviors (methods) into individual objects. Fundamental concepts include _class_ and _object_. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
    - advanced Python / class ::: A __class__ is a user-defined type, created using the keyword `class`. It bundles data (instance variables) and functionalities (methods) together. <p> __Instance variables__ are variables that belong to an object, accessed using the dot `.` operator. <p> __Methods__ are functions that operate on a particular class of an object. They have an extra first parameter `self` (though it could be any other name). We do not need to give a value to this parameter, and Python automatically assigns `self` the object we are operating on (calling the dot `.` operator on). <p> __Constructors__ in Python is a method named `__init__`. It can be used to initialize instance variables of an new object. <!--SR:!2024-11-18,14,292!2024-11-20,16,310-->
      - advanced Python / class / syntax ::: See [Python class syntax](#^Python-class-syntax). <!--SR:!2024-11-18,14,292!2024-11-20,16,310-->
      - advanced Python / class / example ::: See [Python class example](#^Python-class-example). <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->

__Python class syntax__ <a id="^Python-class-syntax"></a> ^Python-class-syntax

```Python
class <class-name>:
  # __init__ is a constructor
  def __init__(self, <arguments0>):
    self.<instance-variable1> = <value1>
    self.<instance-variable2> = <value2>
    ...
  def <method1-name>(self, <arguments1>):
    <statement1>
    <statement2>
    ...
  def <method2-name>(self, <arguments2>):
    <statement1>
    <statement2>
    ...

<object-name> = <class-name>(<arguments>)        # Create an object
<object-name>.<method-name>(<arguments>)         # Call a method
<object-name>.<instance-variable-name> = <value> # Modify an instance variable
```

__Python class example__ <a id="^Python-class-example"></a> ^Python-class-example

```Python
import math                                            # Import math library

class Circle:                                          # Define a new type Circle
  def __init__(self, radius):                          # Define a constructor with parameter, radius
    self.radius = radius                               # Define an instance variable radius
                                                         # and assign it with parameter radius

  def area(self):                                      # Define the method: area
    return math.pi * self.radius**2                    # Compute the area of circle

  def circumference(self):                             # Define the method: circumference
    return 2 * math.pi * self.radius                   # Compute the circumference of circle

circle_object = Circle(10)                             # Define an object of Circle named circle_object
circle_object.radius = 100                             # Modify circle_object's radius to 100
print("Area:", circle_object.area())                   # Call area()
print("Circumference:", circle_object.circumference()) # Call circumference()
```

```text
Area: 31415.926535897932
Circumference: 628.3185307179587
```

## week 2 lab

- datetime: 2024-09-12T16:30:00+08:00/2024-09-12T18:20:00+08:00
- status: unscheduled, no lab

## week 2 additional lecture

- datetime: 2024-09-12T19:00:00+08:00/2024-09-12T21:00:00+08:00
- hybrid
- Python
  - advanced Python
    - advanced Python / public, protected, private ::: There is little accessibility control in Python. Instead, it is usually enforced by convention. <p> Members in a class are by default __public__. Any code can access them. <p> __Protected__ members are accessible from within the class and its subclass. The prefix `_` (single underscore) is prepended before the member name to denote it. This is enforced only by convention. <p> __Private__ members are accessible from within the class only. The prefix `__` (double underscores) is prepended before the member name to denote it. This is enforced by convention and also name mangling. <!--SR:!2024-11-19,15,310!2024-11-19,15,292-->
      - advanced Python / private / name mangling ::: Private members with names starting with `__` (double underscores) have their names mangled. That is, their names and references to them _within the class_ are _changed when the code is actually run_. <p> So if you try to reference them _outside the class_, as said references do not have their names changed, they are not referring to the private member. If you try to read from it outside the class, an `AttributeError` is raised. If you try to write to it outside the class, a property with the _unmangled_ name is created, which is unrelated to the actual private property with the _mangled_ name. <!--SR:!2024-11-18,14,292!2024-11-18,14,292-->
        - advanced Python / private / name mangling / example ::: See [Python private member name mangling example](#^Python-private-member-name-mangling-example). <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
  - advanced Python / accessor, mutator ::: __Accessors__ and __mutators__ are _public_ methods used to respectively read from and write to _protected_ and _private_ instance variables of a class. <p> (This is rather un-Pythonic... we should be using `@property` instead...) <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - advanced Python / accessor, mutator / example ::: See [Python accessor and mutator example](#^Python-accessor-and-mutator-example). <!--SR:!2024-11-21,17,310!2024-11-20,16,292-->
  - advanced Python / class variable ::: __Class variable__ is a variable to belongs to a _class_, not any _object_ of that class (or alternatively, shared by all _objects_ of that class). They are defined within a class but not inside any method of the class. They can be initialized within the class or outside the class (after the class). They are accessed using the class name, the dot `.` operator, and then the class variable name. <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
    - advanced Python / class variable / example ::: See [Python class variable example](#^Python-class-variable-example). <!--SR:!2024-11-20,16,292!2024-11-20,16,310-->
  - advanced Python / inheritance ::: __Inheritance__ is a mechanism to define new classes based on existing classes. The existing classes' attributes (instance and class variables) and methods are inherited by the new class. <p> The existing classes are called __base classes__/__parent classes__/__superclasses__. The new class is called a __child class__/__derived class__/__subclass__. <!--SR:!2024-11-19,15,310!2024-11-20,16,310-->
    - advanced Python / inheritance / syntax ::: See [Python inheritance syntax](#^Python-inheritance-syntax). <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
    - advanced Python / inheritance / example ::: See [Python inheritance example](#^Python-inheritance-example). <!--SR:!2024-11-20,16,310!2024-11-15,11,290-->
  - advanced Python / module ::: A __module__ is a bunch of related code in a Python (`.py`) file. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
  - advanced Python / package ::: A __package__ is a directory of _modules_. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
  - advanced Python / library ::: A __library__ is a collection of _packages_. <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
  - advanced Python / `import` ::: The `import` keyword  can be used to import external modules. <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
    - advanced Python / `import` directly ::: `import <module> [as <name>]` <br/> `import <package>.<module> [as <name>]` <p> The module is accessible as `<module>` or `<package>.<module>`. If `as <name>` is present, then it is accessible as `<name>`. <!--SR:!2024-11-20,16,310!2024-11-19,15,292-->
    - advanced Python / `import` some ::: `from <module> import <entity> [as <name>]` <br/> `from <package>.<module> import <entity> [as <name>]` <p> The named entity is accessible as `<entity>`. If `as <name>` is present, then it is accessible as `<name>`. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
    - advanced Python / `import` all ::: `from <module> import *` <br/> `from <package>.<module> import *` <p> All named entities inside the module are accessible with their names preserved. It is not recommended to use this as it may result in ambiguity. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->

__Python private member name mangling example__ <a id="^Python-private-member-name-mangling-example"></a> ^Python-private-member-name-mangling-example

```Python
class Person:
  def __init__(self, name="Tom", age=18, gender='M'):
    # private instance
    # variable __name
    self.__name = name
    # private instance
    # variable __age
    self.__age = age
    # private instance
    # variable __gender
    self.__gender = gender

  def print(self):
    print('--- Print Person ---')
    print('Name: ' + self.__name)
    print('Age: ' + str(self.__age))
    print('Gender: ' + self.__gender)

desmond = Person('Haha', 18, 'M')

print('Name: ' + desmond.__name)     # Error
print('Age: ' + str(desmond.__age))  # Error
print('Gender: ' + desmond.__gender) # Error
# Okay, but do not change desmond.__name
desmond.__name = 'Desmond'
# Okay, but do not change desmond.__age
desmond.__age = 19
desmond.print() # Okay
```

__Python accessor and mutator example__ <a id="^Python-accessor-and-mutator-example"></a> ^Python-accessor-and-mutator-example

```Python
class Person:
  def __init__(self, name='Tom', age=18, gender='M'):
    self.__name = name
    self.__age = age
    self.__gender = gender

  def get_name(self): # Accessor
    return self.__name

  def get_age(self): # Accessor
    return self.__age

  def get_gender(self): # Accessor
    return self.__gender

  def set_name(self, name): # Mutator
    self.__name = name

  def set_age(self, age): # Mutator
    self.__age = age

  def set_gender(self, gender): # Mutator
    self.__gender = gender

  def print(self):
    print('--- Print Person ---')
    print('Name: ' + self.__name)
    print('Age: ' + str(self.__age))
    print('Gender: ' + self.__gender)

desmond = Person('Haha', 18, 'M')
print('Name: ' + desmond.get_name())
print('Age: ' + str(desmond.get_age()))
print('Gender: ' + desmond.get_gender())
desmond.set_name('Desmond')
desmond.set_age(19)
desmond.print()
```

__Python class variable example__ <a id="^Python-class-variable-example"></a> ^Python-class-variable-example

```Python
class Person:
  num_person = 0 # Class variable
  def __init__(self, name="Tom", age=18, gender='M'):
    self.__name = name
    self.__age = age
    self.__gender = gender
    Person.num_person = Person.num_person + 1

  def print(self):
    print('--- Print Person ---')
    print('Name: ' + self.__name)
    print('Age: ' + str(self.__age))
    print('Gender: ' + self.__gender)

desmond = Person('Desmond', 18, 'M')
pearl = Person('Pearl', 17, 'F')
desmond.print()
pearl.print()
print("Total number of objects:", Person.num_person)
```

```text
--- Print Person ---
Name: Desmond
Age: 18
Gender: M
--- Print Person ---
Name: Pearl
Age: 17
Gender: F
Total number of objects: 2
```

__Python inheritance syntax__ <a id="^Python-inheritance-syntax"></a> ^Python-inheritance-syntax

```Python
class <subclass-name>(<superclass-name>):
  # __init__ is a constructor
  def __init__(self, <arguments0>):
    super().__init__(<attributes>)
    self.<instance-variable1> = <value1>
    self.<instance-variable2> = <value2>
    ...
  def <method1-name>(self, <arguments1>):
    <statement1>
    <statement2>
    ...
```

__Python inheritance example__ <a id="^Python-inheritance-example"></a> ^Python-inheritance-example

```Python
class Person:
  def __init__(self, name='Tom', age=18, gender='M'):
    self.__name = name
    self.__age = age
    self.__gender = gender

  def get_name(self): # Accessor
    return self.__name

  def get_age(self): # Accessor
    return self.__age

  def get_gender(self): # Accessor
    return self.__gender

  def set_name(self, name): # Mutator
    self.__name = name

  def set_age(self, age): # Mutator
    self.__age = age

  def set_gender(self, gender): # Mutator
    self.__gender = gender

  def print(self):
    print('--- Print Person ---')
    print('Name: ' + self.__name)
    print('Age: ' + str(self.__age))
    print('Gender: ' + self.__gender)

# Define a new type Student that inherits Person class
class Student(Person):
  def __init__(self, name="Tom", age=18, gender='M', id="12345678"): # Constructor
    super().__init__(name, age, gender) # Invoke superclass' constructor
    self.__id = id # Define an instance variable id and assign it with parameter id

  def get_id(self): return self.__id # Accessor

  def set_id(self, id): self.__id = id # Mutator

  def print(self): # Override print method
    super().print() # Invoke superclass' print method
    print('ID: ' + self.__id) # Print ID

tony = Student('Lala', 18, 'M', "23456789") # Define an object of Student named tony
tony.print() # Print tony
```

```text
--- Print Person ---
Name: Lala
Age: 18
Gender: M
ID: 23456789
```

## week 2 lecture 2

- datetime: 2024-09-13T13:30:00+08:00/2024-09-13T14:50:00+08:00
- Python
  - Python / importing data ::: Data can come in many forms. We will only teach reading comma-separated values (CSV, `.csv`), which is a common file format for storing tabular data. <!--SR:!2024-11-18,14,292!2024-11-18,14,292-->
    - Python / importing data / `google.colab.drive.mount(<local directory>)` ::: This makes your Google Drive accessible from the directory named `<local directory>`. <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
    - Python / importing data / `pandas.read_csv(<file>, index_col=<False, int, str>)` ::: This uses `pandas` to read a CSV file `<file>`. The 1st row of the file is treated as the column names, by default. <p> If `index_col` is `False`, then a new column counting up from 0 is inserted at the start and is used as the index column. If `index_col` is an `int`, the column of the specified (0-based) index in the file is used as the index column. If `index_col` is a `str`, the column of the specified name (as determined by the 1st row) is used as the index column. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - Python / exporting data ::: Data can be expressed in many forms. We will only teach exporting comma-separated values (CSV, `.csv`), which is a common file format for storing tabular data. <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
    - Python / exporting data / `pandas.DataFrame(<data>)` ::: Convert `<data>` into `DataFrame`. <p> There are many forms of `<data>` accepted. One common form is: `{'column1': numpy.array([0, 1, ...]), 'column2': numpy.array([2, 3, ...]), ...}`. <!--SR:!2024-11-21,17,310!2024-11-19,15,292-->
    - Python / exporting data / `pandas.DataFrame.to_csv(self, <file>)` ::: Use `pandas` to export the `DataFrame` as a CSV file `<file>`. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
- [NumPy](../../../../general/NumPy.md) ::: __NumPy__ (__Numerical Python__, but no one uses this...) is a Python library supporting _high-performance, large, multi-dimensional arrays and matrices_, along with high-level mathematical functions to operate on these arrays. It is used for _numeric and scientific computing_. <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
  - NumPy / array ::: A __NumPy array__ is a grid of values, all of the _same type_, and is indexed by _a tuple of non-negative integers_. The _number of dimensions_ is the __rank__ of the array. The __shape__ of an array is a _tuple of integers giving the size of the array along each dimensions_. <p> We can initialize NumPy arrays from _nested Python lists_, and access elements using _square brackets_. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
    - [NumPy § array creation](../../../NumPy/user%20guide/fundamentals/array%20creation.md)
  - NumPy / indexing ::: NumPy arrays can be indexed, sliced, integer-indexed, or boolean-indexed. The former two are also called __simple indexing__. The latter two are also called __advanced indexing__. If _any advanced indexing is involved_, the resulting array is a _copy_ of the original array. Otherwise, it is a _view_ of the original array. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
    - NumPy / indexing / `a[i]` ::: a[i] Select element at index i, where i is an integer (start counting from 0). <!--SR:!2024-11-21,17,310!2024-11-20,16,292-->
    - NumPy / indexing / `a[-i]` ::: Select the i-th element from the end of the list, where n is an integer. The last element in the list is addressed as -1, the second to last element as -2, and so on. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
    - NumPy / indexing / `a[i:j]` ::: Select elements with indexing starting at i and ending at j-1. <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
    - NumPy / indexing / `a[:]` or `a[0:]` ::: Select all elements in the given axis. <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
    - NumPy / indexing / `a[:i]` ::: Select elements starting with index 0 and going up to index i - 1. <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
    - NumPy / indexing / `a[i:]` ::: Select elements starting with index i and going up to the last element in the array. <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
    - NumPy / indexing / `a[i:j:n]` ::: Select elements with index i through j (exclusive), with increment n. <!--SR:!2024-11-19,15,310!2024-11-20,16,310-->
    - NumPy / indexing / `a[::-1]` ::: Select all the elements, in reverse order. <!--SR:!2024-11-18,14,292!2024-11-19,15,292-->
    - NumPy / indexing / integer indexing ::: Integer arrays can be used to index another array. Let's call said arrays __indexing arrays__. The shapes of all indexing arrays are broadcasted together. The resulting shape is the shape of the output array. Each of the indexing arrays is made into the resulting shape. Then, each element of the resulting array is determined by `result[i_1, ..., i_M] == x[ind_1[i_1, ..., i_M], ind_2[i_1, ..., i_M], ..., ind_N[i_1, ..., i_M]]`. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
    - NumPy / indexing / boolean indexing ::: Boolean arrays can be used to index another array. Practically, for a boolean array `b`, `x[b]` is identical to `x[b.nonzero()]`, where `b.nonzero()` returns a tuple (of length `obj.ndim`) of 1D integer index arrays showing the `True` elements of obj. This turns the boolean indexing into integer indexing. If mixed with other indexing, then, for example, `x[ind_1, b, ind_2]` is equivalent to `x[(ind_1,) + b.nonzero() + (ind_2,)]`. <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
    - [NumPy § indexing on `ndarrays`](../../../NumPy/user%20guide/fundamentals/indexing%20on%20ndarrays.md)
  - NumPy / data types ::: A NumPy array have elements all of the same type. NumPy provides a large set of numeric data types (e.g. `np.float64`, `np.int64`) and some other types. <p> NumPy tries to guess the data type when you create an array, but you can control this using the `dtype` optional parameter. <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
    - [NumPy § data types](../../../NumPy/user%20guide/fundamentals/data%20types.md)
  - NumPy / element-wise operations ::: `+`, `-`, `*`, `/`, `np.sqrt`, and many other Numpy functions operates element-wise on arrays (with broadcasting, to be mentioned later). <!--SR:!2024-11-18,14,292!2024-11-18,14,292-->
  - NumPy / vector ::: 1-dimensional array of numbers (in general, elements of a field) <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
  - NumPy / matrix ::: 2-dimensional array of numbers (in general, elements of a field) <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - NumPy / tensor ::: _N_-dimensional array of numbers (in general, elements of a field) for _N_ ≥ 0 <!--SR:!2024-11-19,15,292!2024-11-21,17,310-->
  - NumPy / [dot product](../../../../general/dot%20product.md) ::: The __dot product__ of two same-sized _vectors_ is the sum of products of corresponding values in the two vectors. <p> Complex conjugation is ignored for this course. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
  - NumPy / [matrix multiplication](../../../../general/matrix%20multiplication.md) ::: The __matrix multiplication__ of `(n, k)` matrix on the left and `(k, m)` matrix on the right is a `(n, m)` matrix, with each element being the _dot product_ of the corresponding row of the matrix on the left and the corresponding column of the matrix on the right. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
    - [NumPy § `numpy.dot`](../../../NumPy/API%20reference/generated/numpy.dot.md) ::: `numpy.dot(a, b, out=None)` <p> `np.dot` is also available as an array instance method. <p> If both `a` and `b` are 1-D arrays, it is inner product of vectors (without complex conjugation). <br/> If both `a` and `b` are 2-D arrays, it is matrix multiplication, but using `numpy.matmul(a, b)` or `a @ b` is preferred. <br/> If either `a` or `b` is 0-D (scalar), it is equivalent to multiply and using `numpy.multiply(a, b)` or `a * b` is preferred. <br/> If `a` is an N-D array and `b` is a 1-D array, it is a sum product over the last axis of a and b. <br/> If `a` is an N-D array and `b` is an M-D array (where `M>=2`), it is a sum product over the last axis of `a` and the second-to-last axis of `b`: `numpy.dot(a, b)[i,j,k,m] = numpy.sum(a[i,j,:] * b[k,:,m])`. <!--SR:!2024-11-14,10,272!2024-11-16,13,272-->
    - [NumPy § `numpy.matmul`](../../../NumPy/API%20reference/generated/numpy.matmul.md), `@` ::: `numpy.matmul(x1, x2)` <p> `x1 @ x2`, since Python 3.5, is equivalent to `numpy.matmul(x1, x2)`. <p> If both `x1` and `x2` are 2-D they are multiplied like conventional matrices. <br/> If either `x1` or `x2` is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly. <br/> If `x1` is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed. (`x1` is treated as a row vector.) <br/> If `x2` is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed. (`x2` is treated as a column vector.) <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
    - [NumPy § `numpy.dot`](../../../NumPy/API%20reference/generated/numpy.dot.md) vs. [NumPy § `numpy.matmul`](../../../NumPy/API%20reference/generated/numpy.matmul.md) ::: `numpy.matmul` differs from `numpy.dot` in two important ways: <p> Multiplication by scalars is not allowed, use `*` instead. <br/> Stacks of matrices are broadcast together as if the matrices were elements, respecting the signature `(n,k),(k,m)->(n,m)`. <br/> (Additional: `np.dot` is also available as an array instance method, but not for the other.) <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
  - [NumPy § `numpy.sum`](../../../NumPy/API%20reference/generated/numpy.sum.md) ::: `numpy.sum(a, axis=None, keepdims=<no value>)` <p> Sum of array elements over the given one or more axes. If `axis` is `None`, it sums all array elements. If `keepdims` is `True`, the axes which are reduced are left in the result as dimensions with size one. <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  
## week 3 additional lecture

- datetime: 2024-09-16T19:00:00+08:00/2024-09-16T21:00:00+08:00
- hybrid
- [NumPy](../../../../general/NumPy.md)
  - [NumPy § `numpy.transpose`](../../../NumPy/API%20reference/generated/numpy.transpose.md) ::: `numpy.transpose(a, axes=None)` <p> A view is returned if possible; otherwise, a copy is returned. `np.transpose` is also available as an array instance method, which _additionally_ allows passing a `tuple` of `axes` as separate arguments. <p> If `axes` is specified, it must be a `tuple` or `list` which contains a permutation of [0, 1, ..., N-1] where N is the number of axes of `a`. The i-th axis of the returned array will correspond to the axis numbered `axes[i]` of the input. If not specified (`axes is None`), defaults to `range(a.ndim)[::-1]`, which reverses the order of the axes. This implies `transpose(a).shape == a.shape[::-1]`. <!--SR:!2024-11-18,14,292!2024-11-14,10,272-->
  - [NumPy § `numpy.reshape`](../../../NumPy/API%20reference/generated/numpy.reshape.md) ::: `numpy.reshape(a, /, shape=None)` <p> A view is returned if possible; otherwise, a copy is returned. It is also available as an array instance method, which _additionally_ allows passing a `tuple` of `shape` as separate arguments. (Note that in this course, we are using the old version of NumPy, which has the parameter `newshape` instead of `shape`.) <p> The new `shape` should be compatible with the original shape. If an integer, then the result will be a 1-D array of that length. One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions. <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
  - [NumPy § `numpy.newaxis`](../../../NumPy/API%20reference/constants.md#numpy.newaxis), `None` ::: A convenient alias for `None`, useful for indexing arrays: `numpy.newaxis is None`. Note that this is considered _simple indexing_, and as thus returns a view if there are no other _advanced indices_. <p> Each `numpy.newaxis` object in the selection tuple serves to expand the dimensions of the resulting selection by one unit-length dimension. The added dimension is the position of the `numpy.newaxis` object in the selection tuple. <!--SR:!2024-11-18,14,292!2024-11-18,14,290-->
  - [NumPy § `numpy.expand_dims`](../../../NumPy/API%20reference/generated/numpy.expand_dims.md) ::: `numpy.expand_dims(a, axis)` <p> A view is returned. `np.expand_dims` is also available as an array instance method, which _additionally_ allows passing a `tuple` of `axis` as separate arguments. <p> `axis` is an `int` or a `tuple` of `int`s specifying the position in the expanded axes where the new axis (or axes) is placed. (Annotation: The new axis is inserted after the specified position, similar to `list.insert`.) <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->

## week 3 lecture

- datetime: 2024-09-18T13:30:00+08:00/2024-09-18T14:50:00+08:00
- status: unscheduled, public holiday: Day after Mid-Autumn Festival

## week 3 lab

- datetime: 2024-09-19T16:30:00+08:00/2024-09-19T18:20:00+08:00

## week 3 lecture 2

- datetime: 2024-09-20T13:30:00+08:00/2024-09-20T14:50:00+08:00
- [NumPy](../../../../general/NumPy.md)
  - NumPy / broadcasting ::: Allows operations between arrays of shapes that differ in a "reasonable" way by replicating the smaller array along the mismatched dimensions. <!--SR:!2024-11-18,14,292!2024-11-19,15,292-->
    - NumPy / broadcasting / rules :::  When operating on two arrays, NumPy compares their shapes element-wise. It _starts with the trailing (i.e. rightmost) dimension and works its way left_ (Not the other way around!). Two dimensions are compatible when _they are equal_, or _one of them is 1_. <p> If these conditions are not met, a `ValueError: operands could not be broadcast together` exception is thrown, indicating that the arrays have incompatible shapes. <p> Input arrays do not need to have the same number of dimensions. The resulting array will have the same number of dimensions as the input array with the greatest number of dimensions, where the size of each dimension is the largest size of the corresponding dimension among the input arrays. Note that missing dimensions are assumed to have size one. <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
    - [NumPy § broadcasting](../../../NumPy/user%20guide/fundamentals/broadcasting.md)
    - NumPy / broadcasting / examples ::: calculating pairwise distances, centering an array (subtracting its means) <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - NumPy / array advantages ::: consume less memory than Python lists (Python lists store pointers to objects), faster than Python lists, more convenient (but also harder) to use <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->

## week 3 makeup lecture

- datetime: 2024-09-20T15:00:00+08:00/2024-09-20T16:20:00+08:00 (probably, unsure)
- makeup lecture for public holiday: Day after Mid-Autumn Festival
- [machine learning](../../../../general/machine%20learning.md) ::: __Machine learning__ is the science and engineering of _getting computers to act without being explicitly programmed_. <p> Common types include supervised learning, unsupervised learning, reinforcement learning (not covered in this course), and more. <!--SR:!2024-11-19,15,292!2024-11-21,17,310-->
- [supervised learning](../../../../general/supervised%20learning.md) ::: __Supervised learning__ (__SL__) is a paradigm in _machine learning_ where input objects (for example, a vector of predictor variables) and a desired output value (also known as a _human-labeled supervisory signal_) train a model. <p> Training time is usually _shorter_. Accuracy is usually _higher_. Optimal strategy _depends on the data and learning algorithm_. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - supervised learning / types ::: __classification__: predict categories/classes; __regression__: predict a continuous value <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
  - supervised learning / examples ::: image classification, signature recognition, spam detection, visual recognition, weather forecasting <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
- [unsupervised learning](../../../../general/unsupervised%20learning.md) ::: __Unsupervised learning__ is a framework in _machine learning_ where, in contrast to supervised learning, algorithms learn patterns exclusively from _unlabeled data_. <p> Training time is usually _longer_. Accuracy is usually _lower_. Optimal strategy _depends on the data_. <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  - unsupervised learning / types ::: __association__: rule-based machine learning to discover probability of co-occurrence of items in a collection; __clustering__: group similar data and separate dissimilar data into clusters <!--SR:!2024-11-21,17,310!2024-11-20,16,292-->
  - unsupervised learning / examples ::: identifying accident-prone areas, semantic clustering (audios, images, videos, words) <!--SR:!2024-11-18,14,292!2024-11-20,16,310-->
- [conditional probability](../../../../general/conditional%20probability.md) ::: The __conditional probability__ of an event _A_ given that an event _B_, where _P_(_B_) > 0, has happened is: $$P(A \mid B) = \frac {P(A \cap B)} {P(B)} \,.$$ A property: $P(A \mid B) \ge P(A \cap B)$. <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  - conditional probability / multiplicative rule ::: If _P_(_B_) > 0, then $$P(A \cap B) = P(A \mid B) P(B) \,.$$ <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
- [law of total probability](../../../../general/law%20of%20total%20probability.md#statement) ::: If $$\left\{{B_n : n = 1, 2, 3, \ldots}\right\}$$ is a _finite or countably infinite_ set of _mutually exclusive_ and _collectively exhaustive_ events $$P(A)=\sum_n P(A\mid B_n)P(B_n) \,,$$ where, for any $n$, if $P(B_n) = 0$, then these terms are simply omitted from the summation since $P(A\mid B_n)$ is finite. <p> The set of $B_n$ is also known as a __partition__ of the sample space. <!--SR:!2024-11-19,15,310!2024-11-20,16,310-->
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20the%20theorem) ::: __Bayes' theorem__ relates _P_(_A_|_B_) to _P_(_B_|_A_). It states $$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) \ne 0 \,.$$ Sometimes the theorem is stated in the form where the denominator is replaced using the _law of total probability_. <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
  - Bayes' theorem / names ::: `B`: belief/class, `E`: evidence/feature <p> posterior `P(B|E)` = likelihood `P(E|B)` × prior `P(B)` ÷ marginal probability `P(E)` <!--SR:!2024-11-16,13,272!2024-11-20,16,310-->

## week 4 lecture

- datetime: 2024-09-25T13:30:00+08:00/2024-09-25T14:50:00+08:00
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20the%20theorem)
  - Bayes' theorem / slight generalizations ::: As mentioned before, if there are multiple beliefs/classes, the _law of total probability_ may be used. <p> If we have multiple evidences, we treat the multiple evidences as one evidence. <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
- [naive Bayes classifier](../../../../general/naive%20Bayes%20classifier.md) ::: __Naive Bayes classifiers__ are a family of linear "probabilistic classifiers" which assumes that the features are conditionally independent, given the target class. The strength (naivety) of this assumption is what gives the classifier its name. <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
  - naive Bayes classifier / assumption ::: _Features_ (but not _beliefs_!) are conditionally mutually independent, given the target class. <p> This assumption is incorrect in general, but works well in practice. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - naive Bayes classifier / details ::: We only care about the relative probabilities of the possible beliefs given the same evidence, since we are trying to classify a piece of evidence. So the probability of the evidence is a constant in this scenario. <p> $$\begin{aligned} & \phantom = P(B_i \mid (e_1, \ldots, e_d)) \\ & = \frac {P(B_i) P((e_1, \ldots, e_d) \mid B_i)} {P((e_1, \ldots, e_d))} && \text{Bayes' theorem} \\ & \propto P(B_i) P((e_1, \ldots, e_d) \mid B_i) && \text{only care about relative probabilities} \\ & = P(B_i) P(e_1 | B_i) \cdots P(e_d | B_i) && \text{mutual independence} \end{aligned}$$ <p> Then our classifier simply chooses the belief with the highest relative probability given the same piece of evidence. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - naive Bayes classifier / [additive smoothing](../../../../general/additive%20smoothing.md) ::: __Additive smoothing__ is also called __(_α_-)Laplace smoothing__ or __(_α_-)Lidstone smoothing__. In the context of naive Bayes classifier, this is $$P(e = v_e | B = v_b) = \frac {\text{count of }e = v_e\text{ and }B = v_b + \alpha} {\text{count of }B = v_0 + N \alpha }\,, $$ where _α_ is a real number called the __pseudocount__, and _N_ is the number of possible values for the evidence _e_. The pseudocount is usually 1. <p> This eliminates problems with zero probabilities wiping any chance of a belief being selected if a combination of individual evidence and belief has never been seen in the training data set (__zero frequency problem__). <p> An interpretation of the _pseudocount_ is that even if we have no data, we assume that we have seen a belief and a evidence for each possible values of an evidence together for _pseudocount_ number of times. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - naive Bayes classifier / scikit-learn ::: `sklearn.naive_bayes.CategoricalNB(alpha=<additive smoothing parameter>)` → `fit(training_x, training_y)` → `predict(new_x)` or `predict_proba(new_x)` <!--SR:!2024-11-20,16,310!2024-11-10,7,252-->

## week 4 lab

- datetime: 2024-09-26T16:30:00+08:00/2024-09-26T18:20:00+08:00

## week 4 lecture 2

- datetime: 2024-09-27T13:30:00+08:00/2024-09-27T14:50:00+08:00
- [normal distribution](../../../../general/normal%20distribution.md) ::: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <!--SR:!2024-11-18,14,292!2024-11-18,14,292-->
  - normal distribution / probability _density_ function ::: For $X \sim \mathcal N(\mu, \sigma^2) \,,$ $$f(x) = \frac 1 {\sqrt{2\pi \sigma^2} } \exp\left(-\frac {(x - \mu)^2} {2 \sigma^2} \right) \,.$$ <!--SR:!2024-11-19,15,310!2024-11-14,10,272-->
- [naive Bayes classifier](../../../../general/naive%20Bayes%20classifier.md)
  - naive Bayes classifier / continuous feature ::: We usually assume the continuous feature follows a normal distribution (but it could be other distributions). <p> To calculate its _relative_ probability (_relative_ because continuous variable, and is sufficient for our purposes because naive Bayes classifier only requires _relative_ probabilities), we find its sample mean and _corrected_ (divide by _n − 1_ instead of _n_) variance or standard deviation. Then evaluate the _probability density function_ of the resulting normal distribution. <p> Note: The _probability density function_ may return a number larger than 1, and the resulting relative probability of a belief may also be larger than 1 due to this. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - naive Bayes classifier / floating-point underflow ::: In a naive Bayes classifier, we are multiplying many probabilities together, so the probabilities get really really small. <p> In mathematics, this is not a problem. But in practice, we are using floating-point numbers, which are susceptible to __floating-point underflow__, that is if the probability is so small that the representing floating-point number is zero. <p> A simple way to fix this is calculating the logarithm of probabilities instead. Multiplication of probabilities turns into addition of logarithms of probabilities. Importantly, logarithm is a monotonic function, so the highest relative probability is still the highest after applying logarithm. <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
  - naive Bayes classifier / applications ::: multi-class prediction, recommendation system, real-time prediction (fast algorithm), text classification (good at this; sentient analysis, spam filtering) <!--SR:!2024-11-16,12,290!2024-11-14,10,272-->
  - naive Bayes classifier / advantages ::: computationally efficient, easy to implement, natural language processing (text classification), supports multiple categories, works well on a _large data set_ <!--SR:!2024-11-10,7,270!2024-11-19,15,292-->
  - naive Bayes classifier / disadvantages ::: very biased _predicted probabilities_ (rather than simply asking to classify), hardly true assumption of feature independence, low _precision_ on a _small data set_, zero frequency problem (mitigated by additive smoothening) <!--SR:!2024-11-10,7,270!2024-11-21,17,310-->

## week 5 lecture

- datetime: 2024-10-02T13:30:00+08:00/2024-10-02T14:50:00+08:00
- [_k_-nearest neighbors algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md) ::: ___k_-nearest neighbors algorithm__ is a _lazy_ (generalization of the training data is delayed until a query to the algorithm) learning algorithm. It is also _non-parametric_ as it does not make any assumptions on the data being studied (e.g. the distribution of the data). Note that _k_ is a _hyperparameter_, not a _parameter_. <!--SR:!2024-11-20,16,310!2024-11-19,15,292-->
  - [_k_-nearest neighbors algorithm § algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md#algorithm) ::: Prepare training data and test data. Choose the hyperparameter _k_. Choose a _distance function_. Choose a _tie-breaking_ method. Compute the _k_ nearest _training_ data to the _test_ data. Use the _majority vote_ and then the tie-breaking method, if needed, to classify the test data. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - _k_-nearest neighbors algorithm / scikit-learn ::: `sklearn.neighbors.KNeighborsClassifier(n_neighbors=<number of nearest neighbors>)` → `fit(training_x, training_y)` → `predict(new_x)` <p> encode labels: `sklearn.preprocessing.LabelEncoder().fit_transform(training_y)` <br/> decode labels: `inverse_transform(predicted_y)` <!--SR:!2024-11-10,7,270!2024-11-16,12,290-->
  - _k_-nearest neighbors algorithm / standardization ::: When features of the training data is measured in different units or scales, we should standardize the data. Imagine a feature that ranges from 0 to 1 and another feature that ranges from 0 to 100&nbsp;000. <p> To standardize the data, replace the feature values with their z-scores (which is unitless) using the _corrected_ standard deviation: $$X_{\text{new} } = \frac {X - \text{mean} } {\text{corrected standard deviation} } \,.$$ <!--SR:!2024-11-18,14,292!2024-11-20,16,310-->
- [NumPy](../../../../general/NumPy.md)
  - [NumPy § `numpy.mean`](../../../NumPy/API%20reference/generated/numpy.mean.md) ::: `numpy.mean(a, axis=None, keepdims=<no value>)` <p> Mean of array elements over the given one or more axes. If `axis` is `None`, it sums all array elements. If `keepdims` is `True`, the axes which are reduced are left in the result as dimensions with size one. <!--SR:!2024-11-21,17,310!2024-11-20,16,292-->
  - [NumPy § `numpy.std`](../../../NumPy/API%20reference/generated/numpy.std.md) ::: `numpy.std(a, axis=None, ddof=0, keepdims=<no value>)` <p> Standard deviation of array elements over the given one or more axes. If `axis` is `None`, it sums all array elements. If `keepdims` is `True`, the axes which are reduced are left in the result as dimensions with size one. `ddof` is an `int` or `float` specifying the _means delta degrees of freedom_. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements. For the _corrected_ standard deviation, set `ddof` to `1`. <!--SR:!2024-11-16,13,272!2024-11-21,17,310-->
- [_k_-nearest neighbors algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md)
  - _k_-nearest neighbors algorithm / distance functions ::: Euclidean distance (the distance we are most familiar with), Hamming distance, Manhattan distance (city block distance, taxicab distance), cosine distance <!--SR:!2024-11-19,15,292!2024-11-18,14,292-->

## week 5 lab

- datetime: 2024-10-03T16:30:00+08:00/2024-10-03T18:20:00+08:00

## week 5 lecture 2

- datetime: 2024-10-04T13:30:00+08:00/2024-10-04T14:50:00+08:00
- Euclidean distance ::: $$d(\mathbf x, \mathbf y) = \sqrt{ \sum_{k = 1}^n (x_k - y_k)^2 }$$ <p> Sometimes, the _squared Euclidean distance_ is used instead if we only care about relative distances, which omits the square root. <!--SR:!2024-11-18,14,292!2024-11-20,16,292-->
- Manhattan distance ::: $$d(\mathbf x, \mathbf y) = \sum_{k = 1}^n \lvert x_k - y_k \rvert$$ <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
- cosine distance ::: $$d(\mathbf x, \mathbf y) = 1 - \frac {\langle \mathbf x, \mathbf y \rangle} {\lVert \mathbf x \rVert_2 \lVert \mathbf y \rVert_2} \,,$$ where $\langle \mathbf x, \mathbf y \rangle$ is the dot product of __x__ and __y__, and $\lVert \mathbf x \rVert_2$ is the length/magnitude (2-norm) of __x__. <p> Ranges from 0 (100% similar, same direction) to 2 (absolutely different, opposite direction). (We disregard complex conjugation here.) <!--SR:!2024-11-19,15,310!2024-11-18,14,292-->
- Hamming distance ::: Suppose there are two data with _n_ binary (true or false, 1 or 0) variables. Their __Hamming distance__ is the number of binary variables that differs between them. It ranges from 0 to _n_. <o> This distance function may be used if the variables are discrete instead of continuous. <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
- [_k_-nearest neighbors algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md)
  - _k_-nearest neighbors algorithm / tie-breaking ::: Decrease _k_ by 1 until we break the tie. <p> Or, put more weight for training points that are closer, such as weighing by 1/_d_, where _d_ is the distance between the training point and the test point. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - _k_-nearest neighbors algorithm / choosing _k_ ::: _k_ should not be too large or too small. Larger _k_ reduces effect of the noise on the classification, but make boundaries between classes less distinct, and vice versa. <p> A good rule of thumb is setting _k_ to $\sqrt N$, where _N_ is the _number of training samples_. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
- [cross-validation](../../../../general/cross-validation%20(statistics).md) ::: __Cross-validation__, sometimes called __rotation estimation__ or __out-of-sample testing__, is any of various similar model validation techniques for assessing how the results of a statistical analysis will generalize to an independent data set. Cross-validation includes resampling and sample splitting methods that use different portions of the data to test and train a model on different iterations. It is often used in settings where the goal is prediction, and one wants to estimate how accurately a predictive model will perform in practice. It can also be used to assess the quality of a fitted model and the stability of its parameters. <!--SR:!2024-11-20,16,310!2024-11-16,13,290-->
  - [§ _k_-fold cross-validation](../../../../general/cross-validation%20(statistics).md#_k_-fold%20cross-validation) ::: (The course uses _d_ instead of _k_ instead, to distinguish it from the hyperparameter _k_ of _k_-NN.) <p> First, shuffle the data and split it into _k_ groups or folds of (approximately) equal size. Train the model _k_ times to obtain _k_ models. Each time, a different fold is selected as the validation set, and the rest are used to train the model. Calculate the error using an _error measurement_, such as mean absolute error (MAE), mean square error (MSE), mean absolute percentage error (MAPE), etc. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
    - [§ _k_-fold cross-validation](../../../../general/cross-validation%20(statistics).md#_k_-fold%20cross-validation) / choosing _k_ in _k_-NN ::: To use _d_-fold cross-validation (renamed from _k_) for choosing _k_ in _k_-NN, run _d_-fold cross-validation for each choice _k_. After each run, find the mean error across the _d_ validation set for each fixed _k_. Choose the _k_ with the lowest mean error. <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
    - [§ _k_-fold cross-validation](../../../../general/cross-validation%20(statistics).md#_k_-fold%20cross-validation) / advantage ::: The advantage of this method over repeated random sub-sampling (see below) is that all observations are used for both training and validation, and each observation is used for validation exactly once. 10-fold cross-validation is commonly used, but in general _k_ remains an unfixed parameter. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
- error measurement ::: F1-score error, mean absolute error (MAE), mean square error (MSE), mean absolute percentage error (MAPE) <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
  - mean absolute error (MAE) ::: $$\text{MAE} = \frac 1 n \sum_{k = 1}^n \lvert p_k - a_k \rvert \,,$$ where $p_k$ are predicted values and $a_k$ are actual values (ground truths) <!--SR:!2024-11-18,14,292!2024-11-18,14,292-->
  - mean square error (MSE) ::: $$\text{MSE} = \frac 1 n \sum_{k = 1}^n (p_k - a_k)^2 \,,$$ where $p_k$ are predicted values and $a_k$ are actual values (ground truths) <!--SR:!2024-11-21,17,310!2024-11-21,17,310-->
  - mean absolute percentage error (MAPE) ::: $$\text{MAPE} = \frac 1 n \sum_{k = 1}^n \left\lvert \frac {p_k - a_k} {a_k} \right\rvert \,,$$ where $p_k$ are predicted values and $a_k$ are actual values (ground truths) <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  - [F1-score](../../../../general/F-score.md) error ::: $$\text{F1-score error} = 1 - \frac {2\text{TP} } {2\text{TP} + \text{FP} + \text{FN} } \,,$$ where TP are true positives, FP are false positives, and FN are false negatives. <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
- [_k_-nearest neighbors algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md)
  - _k_-nearest neighbors algorithm / advantages ::: applicable to classification and regression, easy to understand, multi-class problems, no assumptions about data <!--SR:!2024-11-16,13,290!2024-11-19,15,292-->
  - _k_-nearest neighbors algorithm / classification, regression ::: For classification, we use the majority vote of the _k_ nearest neighbors and a tie-breaking method. For regression, we take the average of outputs of the _k_ nearest neighbors. <!--SR:!2024-11-16,13,290!2024-11-18,14,292-->
  - _k_-nearest neighbors algorithm / disadvantages ::: bad with categorical features (distances not well-defined), bad with many attributes (curse of dimensionality), computationally expensive, memory intensive <!--SR:!2024-11-18,14,292!2024-11-20,16,310-->
  - _k_-nearest neighbors algorithm / optimizations ::: parallelize distance calculations, reduce data dimension (e.g. using principle component analysis (PCA)), use good data structure to store the data (e.g. KD-tree) <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
  - _k_-nearest neighbors algorithm / applications ::: fast content-based image retrieval, fault detection for semiconductor manufacturing processes, handwritten character classification, intrusion detection <!--SR:!2024-11-20,16,310!2024-11-15,11,290-->

## week 6 lecture

- datetime: 2024-10-09T13:30:00+08:00/2024-10-09T14:50:00+08:00
- [cluster analysis](../../../../general/cluster%20analysis.md) ::: __Cluster analysis__ or __clustering__ is the task of grouping a set of objects in such a way that objects in the same group (called a __cluster__) are more similar (in some specific sense defined by the analyst) to each other than to those in other groups (clusters). <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - cluster analysis / motivations ::: finding features useful later for categorization, labeling a large data set may be costly <!--SR:!2024-11-18,14,292!2024-11-19,15,310-->
  - cluster analysis / applications ::: group people of similar body size, organize text documents by their content similarities, segment customers in marketing, segment image into regions (image segmentation) <!--SR:!2024-11-16,12,290!2024-11-20,16,310-->
- [_k_-means clustering](../../../../general/k-means%20clustering.md) ::: ___k_-means clustering__ is a method of vector quantization, originally from signal processing, that aims to partition _n_ observations into _k_ clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. <!--SR:!2024-11-19,15,292!2024-11-20,16,310-->
  - _k_-means clustering / characteristics ::: does not require data to be labeled, hyperparameter _k_, parametric (centroid locations), unsupervised <!--SR:!2024-11-21,17,310!2024-11-19,15,310-->
  - _k_-means clustering / algorithm ::: Choose _k_ initial centroids. They are usually data points in the training dataset. <p> Find distances (using a distance function) of training data to the centroids. Assign each data point to the closest centroid (a tie-breaking method may be required). Re-compute the centroids using the centroid memberships (_k_-means use the mean, _k_-medians use the median, _k_-modes use the mode, _k_-medoids use an actual training point). If a _stopping criterion_ is not met, repeat the above steps again. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
  - _k_-means clustering / scikit-learn ::: `sklearn.cluster.KMeans(n_clusters=<number of clusters>, init=<initial centroids>, n_init=<number of times to initialize centroids>, max_iter=<maximum number of iterations>)` → `fit(training_data)` → `cluster_centers_`, `predict(new_data)` <!--SR:!2024-11-16,13,290!2024-11-19,15,310-->

## week 6 lab

- datetime: 2024-10-10T16:30:00+08:00/2024-10-10T18:20:00+08:00

## week 6 lecture 2

- datetime: 2024-10-11T13:30:00+08:00/2024-10-11T14:50:00+08:00
- status: unscheduled, public holiday: Chung Yeung Festival

## week 7 lecture

- datetime: 2024-10-16T13:30:00+08:00/2024-10-16T14:50:00+08:00
- [_k_-means clustering](../../../../general/k-means%20clustering.md)
  - _k_-means clustering / stopping criterion ::: minimum decrease in sum of squared error (SSE), no or minimum change of centroids, no or minimum reassignment of membership <!--SR:!2024-11-19,15,310!2024-11-19,15,310-->
    - sum of squared error (SSE) ::: $$\text{SSE} = \sum_{j = 1}^k \sum_{\mathbf x \in C_j} (\operatorname{distance}(\mathbf m_j, \mathbf x))^2 \,,$$ where $C_j$ are the clusters and $\mathbf m_j$ are the centroids. <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
  - _k_-means clustering / choosing _k_ ::: elbow method, silhouette method <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
  - _k_-means clustering / [elbow method](../../../../general/elbow%20method%20(clustering).md) ::: The __elbow method__ is a heuristic used in determining the number of clusters in a data set. The method consists of plotting the explained variation (sum of squared error is used in this case) as a function of the number of clusters and picking the elbow of the curve as the number of clusters to use. <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
  - _k_-means clustering / [silhouette method](../../../../general/silhouette%20(clustering).md) ::: __Silhouette__ is a method of interpretation and validation of consistency within clusters of data. The technique provides a succinct graphical representation of how well each object has been classified. <p> The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette ranges from −1 to +1, where a high value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters. If most objects have a high value, then the clustering configuration is appropriate. If many points have a low or negative value, then the clustering configuration may have too many or too few clusters. A clustering with an average silhouette width of over 0.7 is considered to be "strong", a value over 0.5 "reasonable" and over 0.25 "weak", but with increasing dimensionality of the data, it becomes difficult to achieve such high values because of the curse of dimensionality, as the distances become more similar. <p> The silhouette score is specialized for measuring cluster quality when the clusters are convex-shaped, and may not perform well if the data clusters have irregular shapes or are of varying sizes. The silhouette can be calculated with any distance metric, such as the Euclidean distance or the Manhattan distance. <!--SR:!2024-11-20,16,310!2024-11-16,13,290-->
  - _k_-means clustering / distance function ::: Similar to _k_-nearest neighbors, there are many choices of distance functions, which depends on the data used. <p> Euclidean distance is most frequently used. However, using a different distance function other than (squared) Euclidean distance may prevent the algorithm from converging. (In this course, we assume we only use Euclidean distance, so the algorithm always converges.) <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  - _k_-means clustering / standardization ::: Similar to _k_-nearest neighbors, it is usually a good idea to standardize the dataset. <!--SR:!2024-11-21,17,310!2024-11-15,11,290-->
  - _k_-means clustering / cluster quality ::: maximizes inter-cluster distances, minimizes intra-cluster distances <!--SR:!2024-11-20,16,310!2024-11-21,17,310-->
  - _k_-means clustering / outlier ::: _k_-means clustering is sensitive to outliers. A cluster may, in an attempt to accommodate an outlier, has its centroid far away from the non-outlier points. <p> Ideally, we would like _k_-means clustering to ignore outliers. Two possible ways (but there can be more) are removing outliers that are much further away from the centroids than other data points, and performing random sampling so that the chance of selecting an outlier is very small. <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
  - _k_-means clustering / initial centroid ::: The result of _k_-means clustering is sensitive to initial centroids. <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
  - _k_-means clustering / advantages ::: easy to understand and implement, efficient given _k_ and the number of iterations are small <!--SR:!2024-11-18,14,292!2024-11-10,7,270-->
  - _k_-means clustering / disadvantages ::: applicable only if a mean is defined (_k_-modes may be used for categorical data), _k_ is arbitrary, sensitive to initial centroids, sensitive to outliers, unsuitable for non-hyper-ellipsoids (hyper-spheres) clusters <!--SR:!2024-11-10,7,252!2024-11-15,11,290-->
- [principal component analysis](../../../../general/principal%20component%20analysis.md) (PCA) ::: __Principal component analysis__ (__PCA__) is a linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing. <p> The data is linearly transformed onto a new coordinate system such that the directions (principal components) capturing the largest variation in the data can be easily identified. <!--SR:!2024-11-21,17,310!2024-11-18,14,292-->
  - principal component analysis / _k_-means clustering ::: It is common to apply PCA before performing _k_-means clustering. It may improve the clustering results via noise reduction. <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
- classification
  - classification / examples ::: email spam detection: not spam, spam (2 classes); handwritten digit recognition: 0 to 9 (10 classes); image classification: cat, dog, none of them (3 classes) <!--SR:!2024-11-21,17,310!2024-11-20,16,310-->
  - image classification
    - image classification / motivations ::: subdomain of __computer vision__: face recognition, labelling objects in an image, medical imaging, robotics <!--SR:!2024-11-16,12,290!2024-11-21,17,310-->
- [neural network](../../../../general/neural%20network%20(machine%20learning).md) ::: __(Artificial) neural network__ (__(A)NN__) is one of the most powerful artificial intelligence and machine learning algorithms. It can approximate any [function](../../../../general/function%20(mathematics).md) from a certain [function space](../../../../general/function%20space.md), i.e. an _universal approximator_, by the [universal approximation theorem](../../../../general/universal%20approximation%20theorem.md). <p> As the name suggests, it draws inspiration from neurons in our brain and the way they are connected. <!--SR:!2024-11-20,16,310!2024-11-20,16,310-->
  - [§ artificial neurons](../../../../general/neural%20network%20(machine%20learning).md#artificial%20neurons)
- [artificial neuron](../../../../general/artificial%20neuron.md)
  - [§ basic structure](../../../../general/artificial%20neuron.md#basic%20structure)

## week 7 makeup lecture

- datetime: 2024-10-16T15:00:00+08:00/2024-10-16T16:20:00+08:00 (probably, unsure)
- makeup lecture for public holiday: Chung Yeung Festival
- [neural network](../../../../general/neural%20network%20(machine%20learning).md)
  - [§ artificial neurons](../../../../general/neural%20network%20(machine%20learning).md#artificial%20neurons)
- [artificial neuron](../../../../general/artificial%20neuron.md)
  - artificial neuron vs. biological neuron ::: inputs: dendrites; node/computation unit: cell nucleus; outputs: axons; weights: synapses <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
  - [§ basic structure](../../../../general/artificial%20neuron.md#basic%20structure)
- [perceptron](../../../../general/perceptron.md) ::: A __perceptron__ is a simple biological neuron model in an artificial neural network. It performs certain calculations to detect input data capabilities. It is also the name of an early algorithm for supervised learning of binary classifiers (i.e., only two classes). <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
  - perceptron / history ::: Frank Rosenblatt invented perceptron in 1957, what he described as the first machine "capable of having an original idea". <!--SR:!2024-11-20,16,310!2024-11-19,15,310-->
  - [§ steps](../../../../general/perceptron.md#steps)
    - [perceptron § steps](../../../../general/perceptron.md#steps) / initialization ::: Initialize the weights arbitrarily. Weights may be initialized to 0 or small random values. <!--SR:!2024-11-18,14,292!2024-11-21,17,310-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / training ::: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$: <!--SR:!2024-11-21,17,310!2024-11-19,15,292-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / forward ::: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <!--SR:!2024-11-21,17,310!2024-11-19,15,292-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / backward ::: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <p> Since $x_{j, 0} = 1$ always, $w_0$ is effectively the bias $b$. Thus the above algorithm already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t)) \,.$$ <!--SR:!2024-11-19,15,310!2024-11-21,17,310-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / termination ::: For [offline training](offline%20training.md), the second step may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <!--SR:!2024-11-20,16,310!2024-11-18,14,292-->
- [artificial neuron](../../../../general/artificial%20neuron.md)
  - [§ types of activation functions](../../../../general/artificial%20neuron.md#types%20of%20activation%20function) ::: step function, sigmoid, linear combination, rectifier, ... <!--SR:!2024-11-23,17,323!2024-11-24,18,323-->
  - [artificial neuron § step function](../../../../general/artificial%20neuron.md#step%20function) ::: $$y = \begin{cases} 1 & \text{if }u > \theta \\ 0 & \text{if }u \le \theta \end{cases}$$ <p> Usually, the threshold _θ_ is chosen to be 0. (For some reason, if _u_ = _θ_, the step function returns 0 instead of 1 in this course.) <!--SR:!2024-11-24,18,323!2024-11-23,17,323-->
  - [artificial neuron § rectifier](../../../../general/artificial%20neuron.md#rectifier) ::: $$y = u^+ = \max(0, u) = \frac {u + \lvert u \rvert} 2 = \begin{cases} u & \text{if }u > 0 \\ 0 & \text{otherwise} \end{cases}$$ <!--SR:!2024-11-23,17,323!2024-11-22,16,323-->
  - [artificial neuron § sigmoid](../../../../general/artificial%20neuron.md#sigmoid) ::: [logistic function](../../../../general/logistic%20function.md) with _L_ = 1, _k = 1_, and _x_<sub>0</sub> = 0: $$y = \frac L {1 + e^{-k(u - x_0)} } = \frac 1 {1 + e^{-u} }$$ <p> [hyperbolic tangent](../../../../general/hyperbolic%20functions.md) ($\tanh$): $$y = \frac {\sinh u} {\cosh u} = \frac {e^u - e^{-u} } {e^u + e^{-u} } = \frac {e^{2u} - 1} {e^{2u} + 1}$$ <!--SR:!2024-11-17,11,303!2024-11-16,11,303-->

## week 7 lab

- datetime: 2024-10-17T16:30:00+08:00/2024-10-17T18:20:00+08:00

## week 7 lecture 2

- datetime: 2024-10-18T13:30:00+08:00/2024-10-18T14:50:00+08:00
- [perceptron](../../../../general/perceptron.md)
  - perceptron / scikit-learn ::: `sklearn.linear_model.Perceptron(eta0=<learning rate>)` → `fit(training_x, training_y)` → `coef_`, `intercept_`, `predict(new_x)` <!--SR:!2024-11-16,11,303!2024-11-23,17,323-->
  - perceptron / stopping condition ::: We can limit the maximum training time, maximum number of training cycles/epochs, or require minimum accuracy. <!--SR:!2024-11-24,18,323!2024-11-24,18,323-->
  - perceptron / error trends ::: Generally, the error decreases, increasingly slowly. Eventually, the error stops decreasing. <!--SR:!2024-11-16,11,303!2024-11-22,16,323-->
  - perceptron / terminologies ::: __learning__: process of updating weights; __epoch__: one cycle through the full training dataset (not simply one _iteration_) <!--SR:!2024-11-23,17,323!2024-11-24,18,323-->
  - perceptron / [decision boundary](../../../../general/decision%20boundary.md) ::: For example: $$y = \begin{cases} 0 & \text{if }0.5x_1 + 0.5x_2 - 0.8 \le 0 \\ 1 & \text{otherwise} \end{cases}$$ <!--SR:!2024-11-24,18,323!2024-11-24,18,323-->
  - [perceptron § convergence of one perceptron on a linearly separable dataset](../../../../general/perceptron.md#convergence%20of%20one%20perceptron%20on%20a%20linearly%20separable%20dataset) ::: A single perceptron is a linear classifier. It only converges (reaches a stable state) if the training samples are linearly separable, i.e. can always be classified correctly by a linear classifier. <p> For example, a single perceptron cannot learn the XOR gate. A multi-layer perceptron with a nonlinear activation function is required. <!--SR:!2024-11-22,16,323!2024-11-22,16,323-->
- [multilayer perceptron](../../../../general/multilayer%20perceptron.md) (MLP) ::: A __multilayer perceptron__ (__MLP__) is a name for a modern _feedforward artificial neural network_ (_feedforward_ means do not form a cycle), consisting of _fully connected neurons_ with a _nonlinear activation function_, organized in at least three layers, notable for being able to _distinguish data that is not linearly separable_. <!--SR:!2024-11-24,18,323!2024-11-23,17,323-->
  - multilayer perceptron / motivations ::: Perceptron is a simple biological neuron model. It can only represent a limited set of functions, and distinguish linearly separable inputs. <p> A multilayer perception remedies this by connecting the output of perceptron to more perceptrons. <!--SR:!2024-11-23,17,323!2024-11-16,11,303-->
  - multilayer perceptron / initialization ::: Initialize the weights and biases to some small random values. <!--SR:!2024-11-22,16,323!2024-11-24,18,323-->
  - multilayer perceptron / training ::: Calculate the outputs given some inputs (__forward propagation__). Calculate the error/loss function, i.e. the difference between the calculated outputs and the target outputs. Starting from the output layer to the input layer, update the weights and biases between two layers using __gradient descent__ (__backward propagation__). Repeat until a _stopping condition_ is reached. <p> Note that training can be very slow in networks with multiple hidden layers! <!--SR:!2024-11-23,17,323!2024-11-23,17,323-->
  - multilayer perceptron / stopping condition ::: We can limit the maximum training time, maximum number of training cycles/epochs, or require training or validation error to fall below a threshold. <p> They are basically the same as that for a single perceptron. <!--SR:!2024-11-24,18,323!2024-11-23,17,323-->
- [gradient descent](../../../../general/gradient%20descent.md) ::: __Gradient descent__ is a method for unconstrained mathematical optimization. It is a first-order iterative algorithm for minimizing a differentiable multivariate function. <!--SR:!2024-11-23,17,323!2024-11-24,18,323-->
  - gradient descent / specific algorithm for dummies ::: Assume the activation function is the sigmoid function, $$\sigma(x) = \frac 1 {1 + e^{-x} } \,,$$  and the error function is one half the sum of squared error: $$E = \frac 1 2 \sum_{k = 1}^n \left(O_k - T_k \right)^2 \,,$$ where _T<sub>k</sub>_ are the _n_ target outputs and _O<sub>k</sub>_ are the _k_ actual outputs. <!--SR:!2024-11-24,18,323!2024-11-16,11,303-->
    - gradient descent / specific algorithm for dummies / compute gradient ::: Compute the gradient of a weight from neuron _x_ to neuron _y_ (this includes biases by letting the "input neuron" _x_ to always output 1): $$\delta w_{x \rightarrow y} = \frac {\partial E} {\partial w_{x \rightarrow y} } = \begin{cases} O_y (1 - O_y) (O_y - T_y) & \text{if }y\text{ is in the output layer,} \\ O_y (1 - O_y) \sum_{z} w_{y \rightarrow z} \delta w_{y \rightarrow z} & \text{otherwise,} \end{cases}$$ where _O<sub>y</sub>_ is the output (after activation function) of _y_. <p> Notice that if we are using the sigmoid activation function, we can effectively ignore the output (after activation function) of the input neuron _x_. This is thanks to some mathematical trick. This may not be the case for other activation functions. <p> _Backpropagation_ may be used to speed up the above calculation for _all layers_ by calculating the gradients starting from the output layer to the input layer, while saving and reusing $\delta w_{x \rightarrow y}$. <p> Note that we compute all gradients before updating the weights and biases, so when computing gradients, we always use the old values for weights. <!--SR:!2024-11-17,11,303!2024-11-14,9,283-->
      - gradient descent / specific algorithm for dummies / compute gradient / mathematical trick ::: Where does $O_y(1 - O_y)$ come from? It is the derivative of the _sigmoid_ activation function. We can check this by letting $f(x) := O_y$ (_x_ is _O<sub>x</sub>_ in the above context): $$\begin{aligned} f(x) & := \frac 1 {1 - e^{-x} } \\ & = \frac {e^x} {e^x - 1} \\ f'(x) & = \frac {e^x \left(e^x - 1\right) - e^{2x} } {\left(e^x - 1\right)^2} \\ & = \frac {e^x} {e^x - 1} - \left(\frac {e^x} {e^x - 1} \right)^2 \\ & = f(x) - (f(x))^2 \\ & = f(x) (1 - f(x)) \,. \end{aligned}$$ This explains the expression $O_y (1 - O_y)$. <!--SR:!2024-11-17,11,303!2024-11-22,16,323-->
    - gradient descent / specific algorithm for dummies / update weights and biases ::: After computing the gradient, update the weights (and biases, by treating them as "neurons" that always output 1) according to a real number called the _learning rate_ $\eta$. <p> For a weight $w_{x \rightarrow y}$ from neuron _x_ (for biases, the "input neuron" always output 1) to neuron _y_ with the gradient $\delta w_{x \rightarrow y}$, update the weight as follows: $$w_{x \rightarrow y} \gets w_{x \rightarrow y} - \eta O_x \delta w_{x \rightarrow y} \,,$$, where _O<sub>x</sub>_ is the output (after activation function) of _x_. Remember to update the biases as well. <!--SR:!2024-11-17,11,303!2024-11-16,11,303-->

## week 8 lecture

- datetime: 2024-10-23T13:30:00+08:00/2024-10-23T14:50:00+08:00
- [gradient descent](../../../../general/gradient%20descent.md)
  - gradient descent / intuition ::: Let $f(x)$ be the error function of a perceptron with only a parameter (e.g. weight) given a fixed input. <p> You can graph $f(x)$. You do not know what the $f(x)$ looks like, but you assume it is continuous, differentiable, and has one or more local minima. Your goal is to minimize the error, i.e. $f(x)$ is minimum. <p> Gradient descent is computing its derivative $f'(x)$ to find the error function $f(x)$'s slope. Then you change the perceptron parameter (e.g. weight) $x$ to _go down said slope a bit_ to try to make $f(x)$ smaller, but not too much that you _overshoot_. Repeating this enough times will result a $x$ that is one of the local minima of $f(x)$. <p> This is simplified. In multilayer perceptron, there are many parameters, i.e. weights and biases, so the error function is actually a multivariable function, making it hard or impossible to graph. Also, we cannot know the minima of said error function beforehand, so that is why we use _gradient descent_. <!--SR:!2024-11-24,18,323!2024-11-16,11,303-->
  - gradient descent / multiple local minima ::: Note that the error function can (and often) has multiple local minima. Given different starting points, a different local minima may be reached. <!--SR:!2024-11-23,17,323!2024-11-24,18,323-->
  - gradient descent / overshooting ::: If the learning rate $\eta$ is too high, __overshooting__ can occur. This is very similar to a ball rolling down a hill in between the two hills. If the ball is moving too fast, the ball does not stop in between the two hills, but instead goes up the other hill for a bit. This causes it to take longer for the ball to settle down in between the two hills. <!--SR:!2024-11-23,17,323!2024-11-23,17,323-->
  - gradient descent / motivations ::: Why do we use gradient descent? For _most nonlinear regression problems_, there is no closed form solution to minimize the error function, so we cannot just "find the minimum of the error function" directly. Even if _there is a closed form solution_, gradient descent is _computationally cheaper_ (faster). <!--SR:!2024-11-23,17,323!2024-11-22,16,323-->
  - gradient descent / activation function
    - gradient descent / activation function / requirements ::: Since gradient descent finds the local derivative of the error function, the activation function should be continuous and differentiable almost everywhere (not differentiable in only some points). <p> For example, sigmoid is differentiable everywhere. ReLU is differentiable almost everywhere (not differentiable at _x_ = 0), so we often assign a fixed value (e.g. 0, 0.5, 1, ...) to be its "derivative" if _x_ happens to be 0 during calculation. <!--SR:!2024-11-22,16,323!2024-11-24,18,323-->

## week 8 lab

- datetime: 2024-10-24T16:30:00+08:00/2024-10-24T18:20:00+08:00

## week 8 lecture 2

- datetime: 2024-10-25T13:30:00+08:00/2024-10-25T14:50:00+08:00

## midterm examination

- datetime: 2024-10-31T20:00:00+08:00/2024-10-31T22:00:00+08:00, PT2H
- venue: Lecture Theater A
- scope
  - introduction to artificial intelligence
  - advanced Python for artificial intelligence
  - naive Bayes classifier
  - k-nearest neighbors
  - k-means clustering
  - artificial neural network - perceptron
  - artificial neural network - multi-layer perceptron (P.16)
- format: closed book, calculator, no cheatsheet
- grades: ?/100
- report
  - TODO

## final examination

## aftermath
