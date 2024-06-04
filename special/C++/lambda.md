---
aliases:
  - lambda
  - lambda expression
  - lambda expressions
tags:
  - flashcard/special/Cpp/lambda
  - language/in/English
---

# lambda expressions

## lambda capture

If the capture-default is `&`, subsequent simple captures {{must not begin with `&`}}. <!--SR:!2024-06-08,4,270-->

If the capture-default is `=`, subsequent simple captures {{must begin with `&`. Since C++17, `*this` is allowed. Since C++20, `this` is also allowed}}. <!--SR:!2024-06-08,4,270-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/lambda) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
