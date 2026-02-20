---
aliases:
  - Newton–Leibniz theorem
  - first fundamental theorem of calculus
  - fundamental theorem of calculus
  - fundamental theorems of calculus
  - second fundamental theorem of calculus
tags:
  - flashcard/active/general/eng/fundamental_theorem_of_calculus
  - language/in/English
---

# fundamental theorem of calculus

## formal statements

### first part

The first part is sometimes called the _first fundamental theorem of calculus_.

> {@{__first fundamental theorem of calculus__}@}
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@}, define {@{$F$ as the [Riemann integral](Riemann%20integral.md) $$F(x)=\int_a^x\!f(t)\,\mathrm{d}t\quad\forall{x}\in[a,b]$$}@}. Then {@{$F$ is an [antiderivative](antiderivative.md) of $f$ on the open [interval](interval%20(mathematics).md) $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}. $F$ is {@{[uniformly continuous](uniformly%20continuous.md) on $[a,b]$ and [differentiable](differentiable%20function.md) on $(a,b)$}@}.

The first part implies that when $f$ is [continuous](continuous%20function.md), {@{[antiderivatives](antiderivative.md) of $f$ always exists}@}.

The conditions above can be relaxed. If $f$ is {@{[Lebesgue integrable](Lebesgue%20integration.md) on $[a, b]$, and [continuous](continuous%20function.md) at $x_0 \in (a, b)$}@}, then {@{$F$ is [differentiable](differentiable%20function.md) at $x_0$ and $F'(x_0) = f(x_0)$}@}. This is still valid for the more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md)}@}.

Additionally, if {@{$f$ is [Lebesgue integrable](Lebesgue%20integrable.md)}@}, then {@{$F$ is [absolutely continuous](absolute%20continuity.md)}@}.

### corollary

> __corollary of the first fundamental theorem of calculus__
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@} and $F$ {@{an [antiderivative](antiderivative.md) of $f$ in $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b) \,,$$}@} then {@{$$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a) \,.$$}@}

The corollary requires {@{$f$ to be [continuous](continuous%20function.md) on the entire [interval](interval%20(mathematics).md)}@}. This condition is {@{relaxed in the [second part of the theorem](#second%20part)}@}.

### second part

{@{The second part}@} is sometimes called {@{the _second fundamental theorem of calculus_}@}, or {@{the __Newton-Leibniz theorem__}@}.

> {@{__second fundamental theorem of calculus__}@}
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [Riemann integrable](Riemann%20integral.md#Riemann%20integrable) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@} and $F$ {@{a [continuous function](continuous%20function.md) on $[a,b]$ which is an [antiderivative](antiderivative.md) of $f$ in $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}, then {@{$$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$$}@}.

The second part is {@{stronger than the [corollary](#corollary)}@} because $f$ {@{may not be [continuous](continuous%20function.md)}@}.

{@{The conditions above}@} can be relaxed. The result still holds if {@{$f$ is [Lebesgue integrable](Lebesgue%20integration.md) instead}@}. Continuing with the replaced definition, however, if {@{$F$ admits a derivative _[almost everywhere](almost%20everywhere.md)_ instead of everywhere}@}, this result may fail. Instead, if {@{$F$ is [absolutely continuous](absolute%20continuity.md)}@}, then it admits {@{a derivative $f$ almost everywhere, $f$ is Lebesgue integrable}@}, and {@{the above result holds}@} again. Note that we do not {@{need to show that $f$ is integrable first (when $F$ is absolutely continuous)}@}.

If the even more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md) is used}@}, then if {@{a [continuous function](continuous%20function.md) $F$ admits an [antiderivative](antiderivative.md) $f$ at all but _countably_ many points \(not equivalent to "almost everywhere"\)}@}, then {@{$f$ is Henstock–Kurzweil integrable and the above results hold}@}. Note that we do not {@{need to show that $f$ is integrable first}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fundamental_theorem_of_calculus) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
