---
aliases:
  - proof by infinite descent
  - proofs by infinite descent
tags:
  - flashcard/active/general/proof_by_infinite_descent
  - language/in/English
---

# proof by infinite descent

In [mathematics](mathematics.md), a proof by __infinite descent__, also known as {{__Fermat's method of descent__}}, is {{a particular kind of [proof by contradiction](proof%20by%20contradiction.md) used to show that a statement cannot possibly hold for any number, by showing that if the statement were to hold for a number, then the same would be true for a smaller number, leading to an infinite descent and ultimately a contradiction}}. It is a method which relies on {{the [well-ordering principle](well-ordering%20principle.md), and is often used to show that a given equation, such as a [Diophantine equation](diophantine%20equation.md), has no solutions}}. <!--SR:!2024-11-23,56,310!2024-11-17,47,290!2025-03-10,135,310-->

Typically, one shows that if {{a solution to a problem existed, which in some sense was related to one or more [natural numbers](natural%20number.md)}}, it would necessarily imply that {{a second solution existed, which was related to one or more 'smaller' natural numbers}}. This in turn would {{imply a third solution related to smaller natural numbers, implying a fourth solution, therefore a fifth solution, and so on}}. However, there {{cannot be an infinity of ever-smaller natural numbers}}, and therefore by {{[mathematical induction](mathematical%20induction.md)}}, the original premise—that {{any solution exists—is incorrect: its correctness produces a [contradiction](contradiction.md)}}. <!--SR:!2024-11-08,43,290!2024-11-08,42,290!2024-11-24,57,310!2024-12-02,63,310!2024-12-08,68,310!2024-11-27,59,310-->

An alternative way to express this is to {{assume one or more solutions or examples exists, from which a smallest solution or example—a [minimal counterexample](minimal%20counterexample.md)—can then be inferred}}. Once there, one would try to {{prove that if a smallest solution exists, then it must imply the existence of a smaller solution (in some sense), which again proves that the existence of any solution would lead to a contradiction}}. <!--SR:!2025-03-07,133,310!2025-02-14,113,290-->

The earliest uses of the method of infinite descent appear in {{[Euclid's _Elements_](Euclid's%20Elements.md)}}. A typical example is {{Proposition 31 of Book 7, in which [Euclid](euclid.md) proves that every composite integer is divided (in Euclid's terminology "measured") by some prime number}}. <!--SR:!2024-11-26,58,310!2025-01-29,92,270-->

The method was much later developed by {{[Fermat](Pierre%20de%20Fermat.md), who coined the term and often used it for [Diophantine equations](diophantine%20equation.md)}}. Two typical examples are {{showing the non-solvability of the Diophantine equation $r^{2}+s^{4}=t^{4}$}} and {{proving [Fermat's theorem on sums of two squares](Fermat's%20theorem%20on%20sums%20of%20two%20squares.md), which states that an odd prime _p_ can be expressed as a sum of two [squares](square%20number.md) when $p\equiv 1{\pmod {4} }$ (see [modular arithmetic](modular%20arithmetic.md) and [proof by infinite descent](Fermat's%20theorem%20on%20sums%20of%20two%20squares.md#euler.27s%20proof%20by%20infinite%20descent))}}. In this way Fermat was able to {{show the non-existence of solutions in many cases of Diophantine equations of classical interest (for example, the problem of four perfect squares in [arithmetic progression](arithmetic%20progression.md))}}. <!--SR:!2024-11-05,39,290!2025-01-06,77,270!2025-01-11,80,270!2025-02-27,116,270-->

In some cases, to the modern eye, his "method of infinite descent" is {{an exploitation of the [inversion](inversive%20geometry.md) of the doubling function for [rational points](rational%20point.md) on an [elliptic curve](elliptic%20curve.md) _E_}}. The context is {{of a hypothetical non-trivial rational point on _E_}}. Doubling a point on _E_ roughly {{doubles the length of the numbers required to write it (as number of digits)}}, so that {{"halving" a point gives a rational with smaller terms. Since the terms are positive, they cannot decrease forever}}. <!--SR:!2024-12-02,64,310!2024-12-15,60,270!2024-11-05,38,290!2025-02-09,110,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/proof_by_infinite_descent) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
