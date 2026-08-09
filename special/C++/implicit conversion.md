---
aliases:
  - implicit conversion
  - implicit conversions
tags:
  - flashcard/active/special/Cpp/implicit_conversion
  - language/in/English
---

# implicit conversions

## qualification conversions

### combining cv-qualifications

Loosely speaking, when adding `const` to a multilevel pointer to a certain level, {@{`const` also needs to be added to all levels above said level ignoring the topmost level}@}. For example, a pointer `T***` can be assigned to {@{`T const *const *const *const`, `T const *const *const *`, `T *const *const *const`, `T *const *const *`, `T **const *const`, `T **const *`, and `T ***const`}@}, but not {@{`T const ***const`, `T const ***`, `T *const **const`, `T *const **`, `T const **const *const`, and `T const **const *`}@}. <!--SR:!2026-09-11,588,290!2026-12-27,625,290!fsrs,2031-04-23T00:00:00.000Z,1687,1686.67781641,2.88086152,2,10,0,0,2026-09-09T00:00:00.000Z-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/implicit_conversion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
