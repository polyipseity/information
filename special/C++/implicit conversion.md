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

Loosely speaking, when adding `const` to a multilevel pointer, {{`const` also needs to be added to levels above said level except for the topmost level}}. For example, a pointer `T***` can be assigned to {{`T *const *const *const`, `T *const *const *`, `T **const *const`, `T **const *`, etc., but not `T *const **` or `T **const *`}}.

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/implicit_conversion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
