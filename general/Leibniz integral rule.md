---
aliases:
  - Leibniz integral rule
tags:
  - flashcards/general/Leibniz_integral_rule
  - languages/in/English
---

# Leibniz integral rule

In [calculus](calculus.md), the __Leibniz integral rule__ is {{a rule that allows evaluation of [differentiating](derivative.md) an [integral](integral.md) in the form of $$\int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t$$}}. <!--SR:!2023-12-27,14,290-->

> __Leibniz integral rule__
>
> 1. {{Under the condition of $-\infty < a(x)$ and $b(x) < \infty$,}}
> 2. {{$$\frac{\mathrm{d} }{\mathrm{d}x} \int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t = f(x, b(x)) b'(x) - f(x, a(x)) a'(x) + \int_{a(x)}^{b(x)} \! \frac\partial{\partial x} f(x, t) \, \mathrm{d}x$$.}} <!--SR:!2023-12-26,13,290!2023-12-30,17,290-->

> [!tip] tip
>
> - [intuition](intuition.md): {{$f(x, b(x)) b'(x)$ represents the change caused by moving the right endpoint, $-f(x, a(x)) a'(x)$ represents the change caused by moving the left endpoint, and $\int_{a(x)}^{b(x)} \! \frac\partial{\partial x} f(x, t) \, \mathrm{d}x$ represents the change of the [integral](integral.md) caused by changing $x$.}} <!--SR:!2024-01-24,33,290-->
