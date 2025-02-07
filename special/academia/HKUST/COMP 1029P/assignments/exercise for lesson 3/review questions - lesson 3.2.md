---
aliases:
  - HKUST COMP 1029P review questions - lesson 3.2
tags:
  - language/in/English
---

# review questions - lesson 3.2

- HKUST COMP 1029P

## The nextgen\(\) Function

In this review question you will develop a function called __nextgen\(\)__, which you will need for the next exercise.

You already started the exercise in [Review Questions 3.1](review%20questions%20-%20lesson%203.1.md). Now, let's add another function which we will need.

Write a function called __nextgen\(\)__ that takes as input a list which is a 2D array of the current generation of creatures and returns a ___new___ list which is a 2D array of the same size representing the next generation of the array, according to the rules of Life.

Your __nextgen\(\)__ function should call your __neighbors\(\)__ function which you have developed in [Review Questions 3.1](review%20questions%20-%20lesson%203.1.md). Remember, the nextgen\(\) function should return a ___new___ list rather than modifying the original list!

Here is an example of running nextgen\(\):

```Python
>>> start = [[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
>>> firstGen = nextgen(start)
>>> firstGen
[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 0]]
>>> start
[[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
>>> secondGen = nextgen(firstGen)
>>> secondGen
[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0]]
>>> thirdGen = nextgen(secondGen)
>>> thirdGen
[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0]]
>>> fourthGen = nextgen(thirdGen)
>>> fourthGen
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> fifthGen = nextgen(fourthGen)
>>> fifthGen
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

As you can see in the example above, for this particular pattern, it dies out very quickly.

In fact, most \(random\) patterns will die out in the long run. Only some special patterns can survive forever.
