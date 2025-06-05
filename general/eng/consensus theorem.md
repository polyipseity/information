---
aliases:
  - consensus theorem
  - rule of consensus
tags:
  - flashcard/active/general/eng/consensus_theorem
  - language/in/English
---

# consensus theorem

| __Variable inputs__ |     |     | __Function values__            |                         |
|:-------------------:|:---:|:---:|:------------------------------:|:-----------------------:|
| _x_                 | _y_ | _z_ | $$xy\vee {\bar {x} }z\vee yz$$ | $$xy\vee {\bar {x} }z$$ |
| 0                   | 0   | 0   | 0                              | 0                       |
| 0                   | 0   | 1   | 1                              | 1                       |
| 0                   | 1   | 0   | 0                              | 0                       |
| 0                   | 1   | 1   | 1                              | 1                       |
| 1                   | 0   | 0   | 0                              | 0                       |
| 1                   | 0   | 1   | 0                              | 0                       |
| 1                   | 1   | 0   | 1                              | 1                       |
| 1                   | 1   | 1   | 1                              | 1                       |

> {@{![[Karnaugh map](Karnaugh%20map.md) of _AB_ ∨ _AC_ ∨ _BC_.](../../archives/Wikimedia%20Commons/Karnaugh%20map%20KV%20Race%20Hazard%2010.svg)}@}
>
> {@{[Karnaugh map](Karnaugh%20map.md) of _AB_ ∨ _AC_ ∨ _BC_}@}. {@{Omitting the red rectangle does not change the covered area}@}. <!--SR:!2025-10-26,176,310!2026-01-28,265,330!2026-01-27,264,330-->

In {@{[Boolean algebra](Boolean%20algebra%20(logic).md)}@}, {@{the __consensus theorem__ or __rule of consensus__}@}<sup>[\[1\]](#^ref-1)</sup> is {@{the identity: $$xy\vee {\bar {x} }z\vee yz=xy\vee {\bar {x} }z$$}@} {@{The __consensus__ or __resolvent__ of the terms $xy$ and ${\bar {x} }z$}@} is {@{$yz$}@}. It is {@{the conjunction of all the unique literals of the terms, excluding the literal that appears unnegated in one term and negated in the other}@}. If {@{$y$ includes a term that is negated in $z$ \(or vice versa\) (annotation: e.g. $y = ab$, $z = \bar a b$, then $a$ is the term)}@}, {@{the consensus term $yz$ is false}@}; in other words, {@{there is no consensus term}@}. <!--SR:!2026-01-14,253,330!2026-02-23,285,330!2025-10-27,177,310!2026-01-12,251,330!2026-02-28,290,330!2025-09-19,157,310!2026-01-17,256,330!2026-01-15,254,330!2026-01-06,248,330-->

{@{The conjunctive [dual](De%20Morgan's%20laws.md) of this equation}@} is: {@{$$(x\vee y)({\bar {x} }\vee z)(y\vee z)=(x\vee y)({\bar {x} }\vee z)$$}@} <!--SR:!2026-02-11,273,330!2026-01-13,252,330-->

## proof

(annotation: proof, starting from $xy\vee {\bar {x} }z\vee yz$) ::@:: $${\begin{aligned}xy\vee {\bar {x} }z\vee yz&=xy\vee {\bar {x} }z\vee (x\vee {\bar {x} })yz\\&=xy\vee {\bar {x} }z\vee xyz\vee {\bar {x} }yz\\&=(xy\vee xyz)\vee ({\bar {x} }z\vee {\bar {x} }yz)\\&=xy(1\vee z)\vee {\bar {x} }z(1\vee y)\\&=xy\vee {\bar {x} }z\end{aligned} }$$ <!--SR:!2026-03-12,294,330!2025-09-16,154,310-->

## consensus

{@{The __consensus__ or __consensus term__ of two conjunctive terms of a disjunction}@} is {@{defined when one term contains the literal $a$ and the other the literal ${\bar {a} }$, an __opposition__}@}. The consensus is {@{the conjunction of the two terms, omitting both $a$ and ${\bar {a} }$, and repeated literals}@}. For example, {@{the consensus of ${\bar {x} }yz$ and $w{\bar {y} }z$}@} is {@{$w{\bar {x} }z$}@}.<sup>[\[2\]](#^ref-2)</sup> The consensus is {@{undefined if there is more than one opposition}@}. <!--SR:!2026-03-12,294,330!2026-01-16,255,330!2026-01-15,254,330!2026-01-11,250,330!2026-02-27,289,330!2026-02-13,275,330-->

For {@{the conjunctive dual of the rule}@}, {@{the consensus $y\vee z$}@} can be {@{derived from $(x\vee y)$ and $({\bar {x} }\vee z)$ through the [resolution](resolution%20(logic).md) [inference rule](inference%20rule.md)}@}. This shows that {@{the LHS is derivable from the RHS}@} \(if {@{_A_ → _B_ then _A_ → _AB_}@}; replacing {@{_A_ with RHS and _B_ with \(_y_ ∨ _z_\)}@} \). The RHS can be {@{derived from the LHS simply through the [conjunction elimination](conjunction%20elimination.md) inference rule}@}. Since {@{RHS → LHS and LHS → RHS \(in [propositional calculus](propositional%20calculus.md)\)}@}, then {@{LHS = RHS \(in Boolean algebra\)}@}. <!--SR:!2026-01-12,251,330!2026-01-16,255,330!2026-02-23,285,330!2026-01-24,262,330!2026-01-20,259,330!2025-11-08,185,310!2026-02-23,285,330!2026-02-17,279,330!2026-01-16,255,330-->

## applications

In {@{Boolean algebra}@}, {@{repeated consensus}@} is {@{the core of one algorithm for calculating the [Blake canonical form](Blake%20canonical%20form.md) of a formula}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2026-02-16,278,330!2026-01-14,253,330!2026-01-15,254,330-->

In {@{[digital logic](digital%20logic.md)}@}, including the consensus term {@{in a circuit can eliminate [race hazards](race%20hazard.md)}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-01-31,268,330!2026-02-09,271,330-->

## history

The concept of consensus was introduced by {@{[Archie Blake](Archie%20Blake%20(mathematician).md) in 1937}@}, related to {@{the [Blake canonical form](Blake%20canonical%20form.md)}@}.<sup>[\[4\]](#^ref-4)</sup> It was rediscovered by {@{Samson and Mills in 1954<sup>[\[5\]](#^ref-5)</sup> and by [Quine](Willard%20van%20Orman%20Quine.md) in 1955}@}.<sup>[\[6\]](#^ref-6)</sup> Quine coined {@{the term 'consensus'}@}. {@{[Robinson](John%20Alan%20Robinson.md) used it for clauses in 1965}@} as {@{the basis of his "[resolution principle](resolution%20(logic).md)"}@}.<sup>[\[7\]](#^ref-7)</sup><sup>[\[8\]](#^ref-8)</sup> <!--SR:!2026-02-10,272,330!2026-02-14,276,330!2025-08-08,124,290!2026-01-13,252,330!2025-08-10,126,290!2026-02-12,274,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/consensus_theorem) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Frank Markham Brown](Frank%20Markham%20Brown.md) \[[d](d_Q112500339.md)\], _Boolean Reasoning: The Logic of Boolean Equations_, 2nd edition 2003, p. 44 <a id="^ref-1"></a>^ref-1
2. Frank Markham Brown, _Boolean Reasoning: The Logic of Boolean Equations_, 2nd edition 2003, p. 81 <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFRafiquzzaman2014"></a> [Rafiquzzaman, Mohamed](Mohamed%20Rafiquzzaman.md) \(2014\). _Fundamentals of Digital Logic and Microcontrollers_ \(6 ed.\). John Wiley & Sons. p. 65. [ISBN](ISBN%20(identifier).md) [978-1118855799](https://en.wikipedia.org/wiki/Special:BookSources/978-1118855799). <a id="^ref-3"></a>^ref-3
4. "Canonical expressions in Boolean algebra", Dissertation, Department of Mathematics, University of Chicago, 1937, [ProQuest](ProQuest.md) [301838818](https://www.proquest.com/docview/301838818), reviewed in J. C. C. McKinsey, _[The Journal of Symbolic Logic](The%20Journal%20of%20Symbolic%20Logic.md)_ __3__:2:93 \(June 1938\) [doi](doi%20(identifier).md):[10.2307/2267634](https://doi.org/10.2307%2F2267634) [JSTOR](JSTOR%20(identifier).md#content) [2267634](https://www.jstor.org/stable/2267634). The consensus function is denoted $\sigma$ and defined on pp. 29–31. <a id="^ref-4"></a>^ref-4
5. Edward W. Samson, Burton E. Mills, Air Force Cambridge Research Center, Technical Report 54-21, April 1954 <a id="^ref-5"></a>^ref-5
6. [Willard van Orman Quine](Willard%20van%20Orman%20Quine.md), "The problem of simplifying truth functions", _American Mathematical Monthly_ __59__:521-531, 1952 [JSTOR](JSTOR%20(identifier).md#content) [2308219](https://www.jstor.org/stable/2308219) <a id="^ref-6"></a>^ref-6
7. [John Alan Robinson](John%20Alan%20Robinson.md), "A Machine-Oriented Logic Based on the Resolution Principle", _[Journal of the ACM](Journal%20of%20the%20ACM.md)_ __12__:1: 23–41. <a id="^ref-7"></a>^ref-7
8. [Donald Ervin Knuth](Donald%20Ervin%20Knuth.md), _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_ __4A__: _Combinatorial Algorithms_, part 1, p. 539 <a id="^ref-8"></a>^ref-8

## further reading

- Roth, Charles H. Jr. and Kinney, Larry L. \(2004, 2010\). "Fundamentals of Logic Design", 6th Ed., p. 66ff.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Boolean algebra](https://en.wikipedia.org/wiki/Category:Boolean%20algebra)
> - [Theorems in lattice theory](https://en.wikipedia.org/wiki/Category:Theorems%20in%20lattice%20theory)
> - [Theorems in propositional logic](https://en.wikipedia.org/wiki/Category:Theorems%20in%20propositional%20logic)
