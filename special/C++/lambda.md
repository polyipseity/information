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

If {@{the capture-default is `&`}@}, subsequent simple captures {@{must not begin with `&`}@}. <!--SR:!2031-01-07,1822,330!fsrs,2029-10-19T00:00:00.000Z,1111,1110.91195779,1,2,9,0,0,2026-10-04T00:00:00.000Z-->

If {@{the capture-default is `=`}@}, subsequent simple captures {@{must begin with `&`}@}. Since {@{C++17}@}, {@{`*this` is also allowed}@}. Since {@{C++20}@}, {@{`this` is also allowed}@}. <!--SR:!fsrs,2028-07-29T00:00:00.000Z,687,687.46191962,6.98338322,2,9,0,0,2026-09-11T00:00:00.000Z!fsrs,2029-09-26T00:00:00.000Z,1092,1091.66087084,1,2,9,0,0,2026-09-30T00:00:00.000Z!fsrs,2029-11-07T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2028-07-27T00:00:00.000Z,675,674.76322068,2.49272837,2,9,0,0,2026-09-21T00:00:00.000Z!fsrs,2029-11-07T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2029-10-14T00:00:00.000Z,1107,1107.06552019,1,2,9,0,0,2026-10-03T00:00:00.000Z-->

## references

This text incorporates [content](https://en.cppreference.com/w/cpp/language/lambda) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
