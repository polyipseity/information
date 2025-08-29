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
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@}, define {@{$F$ as the [Riemann integral](Riemann%20integral.md) $$F(x)=\int_a^x\!f(t)\,\mathrm{d}t\quad\forall{x}\in[a,b]$$}@}. Then {@{$F$ is an [antiderivative](antiderivative.md) of $f$ on the open [interval](interval%20(mathematics).md) $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}. $F$ is {@{[uniformly continuous](uniformly%20continuous.md) on $[a,b]$ and [differentiable](differentiable%20function.md) on $(a,b)$}@}. <!--SR:!2028-05-23,1055,250!2025-10-11,72,331!2025-10-09,70,331!2025-10-09,70,331!2025-10-10,71,331!2025-10-09,70,331-->

The first part implies that when $f$ is [continuous](continuous%20function.md), {@{[antiderivatives](antiderivative.md) of $f$ always exists}@}. <!--SR:!2027-03-12,931,350-->

The conditions above can be relaxed. If $f$ is {@{[Lebesgue integrable](Lebesgue%20integration.md) on $[a, b]$, and [continuous](continuous%20function.md) at $x_0 \in (a, b)$}@}, then {@{$F$ is [differentiable](differentiable%20function.md) at $x_0$ and $F'(x_0) = f(x_0)$}@}. This is still valid for the more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md)}@}. <!--SR:!2028-03-15,1057,320!2026-01-12,396,260!2026-09-25,693,340-->

Additionally, if {@{$f$ is [Lebesgue integrable](Lebesgue%20integrable.md)}@}, then {@{$F$ is [absolutely continuous](absolute%20continuity.md)}@}. <!--SR:!2028-09-26,1119,300!2025-09-02,4,309-->

### corollary

> __corollary of the first fundamental theorem of calculus__
>
> {@{Given a [real-valued function](real-valued%20function.md) $f$ [continuous](continuous%20function.md) on a closed [interval](interval%20(mathematics).md) $[a,b]$ and $F$ an [antiderivative](antiderivative.md) of $f$ in $(a,b)$, i.e. $$F'(x)=f(x)\quad\forall{x}\in(a,b)$$, then $$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$$.}@} <!--SR:!2026-02-10,453,230-->

The corollary requires {@{$f$ to be [continuous](continuous%20function.md) on the entire [interval](interval%20(mathematics).md). This condition is removed in the [second part of the theorem](#second%20part)}@}. <!--SR:!2026-03-13,573,310-->

### second part

The second part is sometimes called the _second fundamental theorem of calculus_, or the __{@{Newton-Leibniz}@} theorem__. <!--SR:!2026-11-18,737,290-->

> {@{__second fundamental theorem of calculus__}@}
>
> Given {@{a [real-valued function](real-valued%20function.md) $f$ [Riemann integrable](Riemann%20integral.md#Riemann%20integrable) on a closed [interval](interval%20(mathematics).md) $[a,b]$}@} and {@{$F$ a [continuous function](continuous%20function.md) on $[a,b]$ which is an [antiderivative](antiderivative.md) of $f$ in $(a,b)$}@}, i.e. {@{$$F'(x)=f(x)\quad\forall{x}\in(a,b)$$}@}, then {@{$$\int_a^b\!f(t)\,\mathrm{d}t=F(b)-F(a)$$}@}. <!--SR:!2025-11-24,251,170!2025-10-10,71,331!2025-10-10,71,331!2025-10-11,72,331!2025-10-09,70,331-->

The second part is {@{stronger than the [corollary](#corollary) because $f$ may not be [continuous](continuous%20function.md)}@}. <!--SR:!2027-04-25,893,330-->

The conditions above can be relaxed. The result still holds if {@{$f$ is [Lebesgue integrable](Lebesgue%20integration.md) instead}@}. Continuing with the replaced definition, however, if {@{$F$ admits a derivative _[almost everywhere](almost%20everywhere.md)_ instead of everywhere}@}, this result may fail. Instead, if {@{$F$ is [absolutely continuous](absolute%20continuity.md), then it admits a derivative $f$ almost everywhere, $f$ is Lebesgue integrable, and the above result holds again. Note that we do not need to show that $f$ is integrable first (when $F$ is absolutely continuous)}@}. <!--SR:!2025-12-29,432,280!2028-05-08,1026,280!2026-03-11,432,260-->

If the even more general {@{[Henstock–Kurzweil integral](Henstock–Kurzweil%20integral.md) is used}@}, then if {@{a [continuous function](continuous%20function.md) $F$ admits an [antiderivative](antiderivative.md) $f$ at all but _countably_ many points (not the same as almost everywhere), then $f$ is Henstock–Kurzweil integrable and the above results hold. Note that we do not need to show that $f$ is integrable first}@}. <!--SR:!2027-05-29,815,300!2025-09-14,303,240-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fundamental_theorem_of_calculus) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
