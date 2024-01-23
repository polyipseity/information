---
aliases:
  - Newton–Leibniz theorem
  - first fundamental theorem of calculus
  - fundamental theorem of calculus
  - fundamental theorems of calculus
  - second fundamental theorem of calculus
tags:
  - flashcards/general/fundamental_theorem_of_calculus
  - languages/in/English
---

# fundamental theorem of calculus

## formal statements

### first part

The first part is sometimes called the _first fundamental theorem of calculus_.

> __first fundamental theorem of calculus__
>
> {{Given a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$, define $F$ as $F(x)=\int_a^x\!f(t)\,\mathrm{d}t\quad\forall{x}\in[a,b]$. Then $F$ is an [antiderivative](antiderivative.md) of $f$ on the open [interval](interval%20(mathematics).md) $(a,b)$, i.e. $F'(x)=f(x)\quad\forall{x}\in(a,b)$. $F$ is [uniformly continuous](uniformly%20continuous.md) on $[a,b]$ and [differentiable](differentiable%20function.md) on $(a,b)$.}} <!--SR:!2024-03-24,61,230-->

The first part implies that when $f$ is [continuous](continuous%20function.md), {{[antiderivatives](antiderivative.md) of $f$ always exists}}. <!--SR:!2024-01-31,48,310-->

### corollary

> __corollary of the first fundamental theorem of calculus__
>
> {{Given a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$ and $F$ an [antiderivative](antiderivative.md) of $f$ in $(a,b)$, i.e. $F'(x)=f(x)\quad\forall{x}\in(a,b)$, then $\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$.}} <!--SR:!2024-02-05,38,230-->

The corollary requires {{$f$ to be [continuous](continuous%20function.md) on the entire [interval](interval%20(mathematics).md). This condition is removed in the [second part of the theorem](#second%20part)}}. <!--SR:!2024-02-14,60,310-->

### second part

The second part is sometimes called the _second fundamental theorem of calculus_, or the __{{Newton-Leibniz}} theorem__. <!--SR:!2024-03-02,66,270-->

> __second fundamental theorem of calculus__
>
> {{Given a [real-valued function](real-valued%20function.md) $f$ [Riemann integrable](Riemann%20integral.md#Riemann%20integrable) on a closed [interval](interval%20(mathematics).md) $[a,b]$ and $F$ a [continuous function](continuous%20function.md) on $[a,b]$ which is an [antiderivative](antiderivative.md) of $f$ in $(a,b)$, i.e. $F'(x)=f(x)\quad\forall{x}\in(a,b)$, then $\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$.}} <!--SR:!2024-01-28,12,190-->

The second part is {{stronger than the [corollary](#corollary) because $f$ may not be [continuous](continuous%20function.md)}}. <!--SR:!2024-02-18,63,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fundamental_theorem_of_calculus) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
