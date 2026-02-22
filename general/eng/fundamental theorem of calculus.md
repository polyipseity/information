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
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@}, define {@{$F$ as the [Riemann integral](Riemann%20integral.md) $$F(x)=\int_a^x\!f(t)\,\mathrm{d}t\quad\forall{x}\in[a,b]$$}@}. Then {@{$F$ is an [antiderivative](antiderivative.md) of $f$ on the open [interval](interval%20(mathematics).md) $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}. $F$ is {@{[uniformly continuous](uniformly%20continuous.md) on $[a,b]$ and [differentiable](differentiable%20function.md) on $(a,b)$}@}. <!--SR:!2028-05-23,1055,250!2026-09-12,336,351!2026-08-26,321,351!2026-08-27,322,351!2026-08-30,324,351!2026-08-22,317,351-->

The first part implies that when $f$ is [continuous](continuous%20function.md), {@{[antiderivatives](antiderivative.md) of $f$ always exists}@}. <!--SR:!2027-03-12,931,350-->

The conditions above can be relaxed. If $f$ is {@{[Lebesgue integrable](Lebesgue%20integration.md) on $[a, b]$, and [continuous](continuous%20function.md) at $x_0 \in (a, b)$}@}, then {@{$F$ is [differentiable](differentiable%20function.md) at $x_0$ and $F'(x_0) = f(x_0)$}@}. This is still valid for the more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md)}@}. <!--SR:!2028-03-15,1057,320!2028-11-09,1030,260!2026-09-25,693,340-->

Additionally, if {@{$f$ is [Lebesgue integrable](Lebesgue%20integrable.md)}@}, then {@{$F$ is [absolutely continuous](absolute%20continuity.md)}@}. <!--SR:!2028-09-26,1119,300!2026-12-19,376,369-->

### corollary

> __corollary of the first fundamental theorem of calculus__
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@} and $F$ {@{an [antiderivative](antiderivative.md) of $f$ in $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b) \,,$$}@} then {@{$$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a) \,.$$}@} <!--SR:!2028-12-14,1038,230!2026-03-17,19,342!2026-03-17,19,342!2026-03-17,19,342-->

The corollary requires {@{$f$ to be [continuous](continuous%20function.md) on the entire [interval](interval%20(mathematics).md)}@}. This condition is {@{relaxed in the [second part of the theorem](#second%20part)}@}. <!--SR:!2026-03-13,573,310!2026-03-17,19,342-->

### second part

{@{The second part}@} is sometimes called {@{the _second fundamental theorem of calculus_}@}, or {@{the __Newton-Leibniz theorem__}@}. <!--SR:!2026-11-18,737,290!2026-03-17,19,342!2026-03-17,19,342-->

> {@{__second fundamental theorem of calculus__}@}
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [Riemann integrable](Riemann%20integral.md#Riemann%20integrable) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@} and $F$ {@{a [continuous function](continuous%20function.md) on $[a,b]$ which is an [antiderivative](antiderivative.md) of $f$ in $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}, then {@{$$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$$}@}. <!--SR:!2027-08-05,619,190!2026-08-29,323,351!2026-08-31,325,351!2026-09-12,336,351!2026-08-28,323,351-->

The second part is {@{stronger than the [corollary](#corollary)}@} because $f$ {@{may not be [continuous](continuous%20function.md)}@}. <!--SR:!2027-04-25,893,330!2026-03-17,19,342-->

{@{The conditions above}@} can be relaxed. The result still holds if {@{$f$ is [Lebesgue integrable](Lebesgue%20integration.md) instead}@}. Continuing with the replaced definition, however, if {@{$F$ admits a derivative _[almost everywhere](almost%20everywhere.md)_ instead of everywhere}@}, this result may fail. Instead, if {@{$F$ is [absolutely continuous](absolute%20continuity.md)}@}, then it admits {@{a derivative $f$ almost everywhere, $f$ is Lebesgue integrable}@}, and {@{the above result holds}@} again. Note that we do not {@{need to show that $f$ is integrable first (when $F$ is absolutely continuous)}@}. <!--SR:!2030-08-22,1685,300!2028-05-08,1026,280!2026-03-11,432,260!2026-03-11,13,322!2026-03-17,19,347!2026-03-17,19,347!2026-03-17,19,347-->

If the even more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md) is used}@}, then if {@{a [continuous function](continuous%20function.md) $F$ admits an [antiderivative](antiderivative.md) $f$ at all but _countably_ many points \(not equivalent to "almost everywhere"\)}@}, then {@{$f$ is Henstock–Kurzweil integrable and the above results hold}@}. Note that we do not {@{need to show that $f$ is integrable first}@}. <!--SR:!2027-05-29,815,300!2027-09-12,728,240!2026-10-14,277,350!2026-12-04,351,370-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fundamental_theorem_of_calculus) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
