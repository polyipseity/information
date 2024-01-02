---
aliases:
  - Leibniz integral rule
tags:
  - flashcards/general/Leibniz_integral_rule
  - languages/in/English
---

# Leibniz integral rule

In [calculus](calculus.md), the __Leibniz integral rule__ is {{a rule that allows evaluation of [differentiating](derivative.md) an [integral](integral.md) in the form of $$\int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t$$}}. <!--SR:!2024-02-19,54,310-->

> __Leibniz integral rule__
>
> 1. {{Let $f(x, t)$ be a [function](function%20(mathematics).md) such that both $f(x, t)$ and its [partial derivative](partial%20derivative.md) with respect to $x$, $f_x(x, t)$, are [continuous](continuous%20function.md) in $x$ and $t$ over the $xt$-plane (not just continuous in both $x$ and $t$ separately), including $x_0 \le x \le x_1$ and $\min(a([x_0, x_1]) \cup b([x_0, x_1])) \le t \le \max(a([x_0, x_1]) \cup b([x_0, x_1]))$.}}
> 2. {{Let $a(x)$ and $b(x)$ be [continuously differentiable functions](differentiable%20function.md) on $x_0 \le x \le x_1$.}}
> 3. {{Then, $$\frac{\mathrm{d} }{\mathrm{d}x} \int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t = f(x, b(x)) b'(x) - f(x, a(x)) a'(x) + \int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$$.}} <!--SR:!2024-01-06,4,241!2024-01-11,11,281!2024-01-08,8,261-->

> [!tip] tip
>
> - [intuition](intuition.md): {{$f(x, b(x)) b'(x)$ represents the change caused by moving the right endpoint, $-f(x, a(x)) a'(x)$ represents the change caused by moving the left endpoint, and $\int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$ represents the change of the [integral](integral.md) caused by changing $x$.}} <!--SR:!2024-01-24,33,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Leibniz_integral_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
