---
aliases:
  - implicit conversion
  - implicit conversions
tags:
  - flashcard/special/Cpp/implicit_conversion
  - language/in/English
---

# implicit conversions

## qualification conversions

### combining cv-qualifications

Loosely speaking, when adding `const` to a multilevel pointer, {{`const` also needs to be added to all levels above said level ignoring the topmost level}}. For example, a pointer `T***` can be assigned to {{`T const *const *const *const`, `T const *const *const *`, `T *const *const *const`, `T *const *const *`, `T **const *const`, `T **const *`, and `T ***const`}}, but not {{`T const ***const`, `T const ***`, `T *const **const`, `T *const **`, `T const **const *const`, and `T const **const *`}}. <!--SR:!2024-08-30,59,270!2024-09-05,58,270!2024-07-23,26,272-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/implicit_conversion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
