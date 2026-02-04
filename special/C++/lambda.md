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

If {@{the capture-default is `&`}@}, subsequent simple captures {@{must not begin with `&`}@}. <!--SR:!2031-01-07,1822,330!2026-10-04,251,330-->

If {@{the capture-default is `=`}@}, subsequent simple captures {@{must begin with `&`}@}. Since {@{C++17}@}, {@{`*this` is also allowed}@}. Since {@{C++20}@}, {@{`this` is also allowed}@}. <!--SR:!2026-09-10,303,190!2026-09-29,246,330!2026-10-08,255,330!2026-09-20,237,330!2026-10-08,255,330!2026-10-03,250,330-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/lambda) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
