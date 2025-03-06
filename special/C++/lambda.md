---
aliases:
  - lambda
  - lambda expression
  - lambda expressions
tags:
  - flashcard/active/special/Cpp/lambda
  - language/in/English
---

# lambda expressions

## lambda capture

If the capture-default is `&`, subsequent simple captures {@{must not begin with `&`}@}. <!--SR:!2026-01-09,425,310-->

If the capture-default is `=`, subsequent simple captures {@{must begin with `&`. Since C++17, `*this` is also allowed. Since C++20, `this` is also allowed}@}. <!--SR:!2025-05-29,85,190-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/lambda) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
