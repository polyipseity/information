---
aliases:
  - Dedekind cut
  - Dedekind cuts
tags:
  - flashcard/active/general/eng/Dedekind_cut
  - language/in/English
---

# Dedekind cut

- For {@{the American record producer known professionally as Dedekind Cut}@}, see {@{[Fred Warmsley](Fred%20Warmsley.md)}@}. <!--SR:!2025-10-31,239,330!2026-02-13,283,290-->

> {@{![Dedekind used his cut to construct the [irrational](irrational%20number.md), [real numbers](real%20number.md).](../../archives/Wikimedia%20Commons/Dedekind%20cut%20at%20square%20root%20of%20two.svg)}@}
>
> {@{Dedekind used his cut to construct the [irrational](irrational%20number.md), [real numbers](real%20number.md).}@} <!--SR:!2025-12-26,284,330!2026-01-02,290,330-->

In [mathematics](mathematics.md), {@{__Dedekind cuts__}@}, named after {@{German mathematician [Richard Dedekind](Richard%20Dedekind.md) \(but previously considered by [Joseph Bertrand](Joseph%20Bertrand.md)<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup>\)}@}, are {@{а method of [construction of the real numbers](construction%20of%20the%20real%20numbers.md) from the [rational numbers](rational%20number.md)}@}. A Dedekind cut is {@{a [partition](partition%20of%20a%20set.md) of the rational numbers into two [sets](set%20(mathematics).md) _A_ and _B_}@}, such that {@{each element of _A_ is less than every element of _B_, and _A_ contains no [greatest element](greatest%20element%20and%20least%20element.md)}@}. The set _B_ {@{may or may not have a smallest element among the rationals}@}. If {@{_B_ has a smallest element among the rationals, the cut corresponds to that rational}@}. Otherwise, {@{that cut defines a unique [irrational number](irrational%20number.md)}@} which, {@{loosely speaking, fills the "gap" between _A_ and <!-- markdown separator -->_B_}@}.<sup>[\[3\]](#^ref-3)</sup> In other words, {@{_A_ contains every rational number less than the cut}@}, and {@{_B_ contains every rational number greater than or equal to the cut}@}. An irrational cut is {@{equated to an irrational number which is in neither set}@}. {@{Every real number, rational or not}@}, is {@{equated to one and only one cut of rationals}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2028-09-07,1052,350!2026-04-23,343,290!2025-12-15,276,330!2028-09-11,1055,350!2025-10-27,236,330!2025-12-12,273,330!2025-12-24,282,330!2025-11-08,246,330!2025-11-06,245,330!2025-11-12,250,330!2027-01-13,551,310!2027-10-23,789,330!2025-12-20,279,330!2026-07-01,412,310-->

Dedekind cuts can be {@{generalized from the rational numbers to any [totally ordered set](total%20order.md)}@} by {@{defining a Dedekind cut as a partition of a totally ordered set into two non-empty parts _A_ and _B_}@}, such that {@{_A_ is closed downwards \(meaning that for all _a_ in _A_, _x_ ≤ _a_ implies that _x_ is in _A_ as well\) and _B_ is closed upwards, and _A_ contains no greatest element}@}. See also {@{[completeness \(order theory\)](completeness%20(order%20theory).md)}@}. <!--SR:!2025-11-05,244,330!2025-10-25,234,330!2027-01-12,550,310!2025-11-30,263,330-->

It is straightforward to show that {@{a Dedekind cut among the real numbers is uniquely defined by the corresponding cut among the rational numbers}@}. Similarly, {@{every cut of reals is identical to the cut produced by a specific real number \(which can be identified as the smallest element of the _B_ set\)}@}. In other words, {@{the [number line](number%20line.md) where every [real number](real%20number.md) is defined as a Dedekind cut of rationals}@} is {@{a [complete](complete%20metric%20space.md) [continuum](linear%20continuum.md) without any further gaps}@}. <!--SR:!2027-11-16,809,330!2026-12-27,540,310!2026-10-07,491,310!2025-12-31,288,330-->

## definition

A Dedekind cut is {@{a partition of the rationals $\mathbb {Q}$ into two subsets $A$ and $B$}@} such that <!--SR:!2025-11-01,240,330-->

1. non-emptyness ::@:: $A$ is nonempty. <!--SR:!2025-11-26,260,330!2025-10-24,233,330-->
2. non-emptyness of complement ::@:: $A\neq \mathbb {Q}$ \(equivalently, $B$ is nonempty\). <!--SR:!2025-12-14,275,330!2025-11-18,255,330-->
3. downward closure ::@:: If $x,y\in \mathbb {Q}$, $x<y$, and $y\in A$, then $x\in A$. \($A$ is "closed downwards".\) <!--SR:!2025-12-20,279,330!2025-12-27,283,330-->
4. no greatest element ::@:: If $x\in A$, then there exists a $y\in A$ such that $y>x$. \($A$ does not contain a greatest element.\) <!--SR:!2025-11-11,249,330!2028-01-01,841,330-->

By {@{omitting the first two requirements (annotation: non-emptyness of both $A$ and $B$)}@}, we {@{formally obtain the [extended real number line](extended%20real%20number%20line.md)}@}. <!--SR:!2025-12-26,282,330!2026-11-01,507,310-->

## representations

It is {@{more symmetrical to use the \(_A_, _B_\) notation for Dedekind cuts}@}, but {@{each of _A_ and _B_ does determine the other}@}. It can be {@{a simplification, in terms of notation if nothing more}@}, to {@{concentrate on one "half" — say, the lower one}@} — and {@{call any downward-closed set _A_ without greatest element a "Dedekind cut"}@}. <!--SR:!2025-11-07,246,330!2025-11-01,241,330!2025-11-23,257,330!2025-12-05,268,330!2027-05-01,588,310-->

If {@{the ordered set _S_ is complete}@}, then, {@{for every Dedekind cut \(_A_, _B_\) of _S_}@}, {@{the set _B_ must have a minimal element _b_}@}, hence we must have that {@{_A_ is the [interval](interval%20(mathematics).md) \(−∞, _b_\), and _B_ the interval \[_b_, +∞\)}@}. In this case, we say that {@{_b_ _is represented by_ the cut \(_A_, _B_\)}@}. <!--SR:!2025-12-29,285,330!2025-12-21,280,330!2026-01-02,289,330!2025-12-30,287,330!2025-11-12,249,330-->

{@{The important purpose of the Dedekind cut}@} is to {@{work with number sets that are _not_ complete}@}. The cut itself can {@{represent a number not in the original collection of numbers \(most often [rational numbers](rational%20number.md)\)}@}. The cut can represent {@{a number _b_}@}, even though {@{the numbers contained in the two sets _A_ and _B_ do not actually include the number _b_ that their cut represents}@}. <!--SR:!2025-12-02,265,330!2025-12-28,284,330!2027-09-10,745,330!2025-12-18,277,330!2025-12-10,272,330-->

For example if {@{_A_ and _B_ only contain [rational numbers](rational%20number.md)}@}, they can still be {@{cut at ${\sqrt {2} }$}@} by {@{putting every negative rational number in _A_, along with every non-negative rational number whose square is less than 2}@}; similarly {@{_B_ would contain every positive rational number whose square is greater than or equal to 2}@}. Even though {@{there is no rational value for ${\sqrt {2} }$}@}, if {@{the rational numbers are partitioned into _A_ and _B_ this way}@}, {@{the partition itself represents an [irrational number](irrational%20number.md)}@}. <!--SR:!2025-11-24,258,330!2027-11-12,806,330!2025-12-10,272,330!2025-12-19,278,330!2025-12-27,285,330!2027-04-11,639,330!2025-12-10,272,330-->

## ordering of cuts

Regard {@{one Dedekind cut \(_A_, _B_\) as _less than_ another Dedekind cut \(_C_, _D_\) \(of the same superset\)}@} if {@{_A_ is a proper subset of _C_}@}. Equivalently, if {@{_D_ is a proper subset of _B_}@}, {@{the cut \(_A_, _B_\) is again _less than_ \(_C_, _D_\)}@}. In this way, {@{set inclusion can be used to represent the ordering of numbers}@}, and {@{all other relations \(_greater than_, _less than or equal to_, _equal to_, and so on\) can be similarly created from set relations}@}. <!--SR:!2025-11-18,255,330!2027-06-16,691,330!2025-10-30,239,330!2027-07-30,725,330!2025-12-10,272,330!2026-01-01,288,330-->

{@{The set of all Dedekind cuts}@} is {@{itself a linearly ordered set \(of sets\)}@}. Moreover, {@{the set of Dedekind cuts has the [least-upper-bound property](least-upper-bound%20property.md)}@}, i.e., {@{every nonempty subset of it that has any upper bound has a _least_ upper bound}@}. Thus, {@{constructing the set of Dedekind cuts}@} serves the purpose of {@{embedding the original ordered set _S_, which might not have had the least-upper-bound property}@}, within {@{a \(usually larger\) linearly ordered set that does have this useful property}@}. <!--SR:!2028-09-02,1048,350!2025-12-04,267,330!2026-01-01,289,330!2025-12-13,274,330!2025-12-26,284,330!2025-12-10,272,330!2025-11-13,251,330-->

## construction of the real numbers

- See also: [Construction of the real numbers § Construction by Dedekind cuts](construction%20of%20the%20real%20numbers.md#construction%20by%20Dedekind%20cuts)

{@{A typical Dedekind cut of the [rational numbers](rational%20number.md) $\mathbb {Q}$}@} is given by {@{the partition $(A,B)$ with <p> $A=\{a\in \mathbb {Q} :a^{2}<2{\text{ or } }a<0\},$ <br/> $B=\{b\in \mathbb {Q} :b^{2}\geq 2{\text{ and } }b\geq 0\}.$}@}<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-11-10,248,330!2025-12-25,283,330-->

This cut represents {@{the [irrational number](irrational%20number.md) ${\sqrt {2} }$}@} in Dedekind's construction. The essential idea is that we use a set $A$, which is the set of all rational numbers whose squares are less than 2, to "represent" number ${\sqrt {2} }$, and further, by defining properly arithmetic operators over these sets \(addition, subtraction, multiplication, and division\), these sets \(together with these arithmetic operations\) form the familiar real numbers. <!--SR:!2025-10-31,240,330-->

To establish this, one must show that {@{$A$ really is a cut \(according to the definition\)}@} and {@{the square of $A$, that is $A\times A$ \(please refer to the link above for the precise definition of how the multiplication of cuts is defined\), is $2$}@} \(note that rigorously speaking {@{this number 2 is represented by a cut $\{x\ |\ x\in \mathbb {Q} ,x<2\}$}@}\). To {@{show the first part}@}, we show that {@{for any positive rational $x$ with $x^{2}<2$, there is a rational $y$ with $x<y$ and $y^{2}<2$}@}. {@{The choice $y={\frac {2+2x}{x+2} }$}@} works (annotation: In general, {@{to approximate $\sqrt[n] a$ while not overshooting, one can use $y = \frac {a \sum_{k = 0}^{n - 1} x^k} {x^{n - 1} + a \sum_{k = 0}^{n - 2} x^k}$}@}.), thus {@{$A$ is indeed a cut}@}. Now {@{armed with the multiplication between cuts}@}, it is easy to check that {@{$A\times A\leq 2$ \(essentially, this is because $x\times y\leq 2,\forall x,y\in A,x,y\geq 0$\)}@}. Therefore to {@{show that $A\times A=2$, we show that $A\times A\geq 2$}@}, and it suffices {@{to show that for any $r<2$, there exists $x\in A$, $x^{2}>r$}@}. For this we notice that {@{if $x>0,2-x^{2}=\epsilon >0$}@}, then {@{$2-y^{2}\leq {\frac {\epsilon }{2} }$ for the $y$ constructed above}@}, this means that {@{we have a sequence in $A$ whose square can become arbitrarily close to $2$}@}, which finishes the proof. <!--SR:!2025-12-29,286,330!2027-04-09,583,310!2025-11-28,262,330!2025-12-27,285,330!2025-12-03,266,330!2026-12-21,535,310!2026-12-22,534,310!2028-01-11,850,330!2025-12-30,287,330!2028-08-21,1037,350!2025-10-23,233,330!2028-01-17,842,330!2026-02-12,282,290!2025-11-01,225,290!2027-02-21,601,328-->

Note that {@{the equality _b_<sup>2</sup> = 2 cannot hold}@} since {@{[${\sqrt {2} }$ is not rational](square%20root%20of%202.md#proofs%20of%20irrationality)}@}. <!--SR:!2025-11-15,252,330!2025-12-13,274,330-->

## relation to interval arithmetic

Given {@{a Dedekind cut representing the real number $r$}@} by {@{splitting the rationals into $(A,B)$ where rationals in $A$ are less than $r$ and rationals in $B$ are greater than $r$}@}, it can be equivalently {@{represented as the set of pairs $(a,b)$ with $a\in A$ and $b\in B$}@}, with {@{the lower cut and the upper cut being given by projections}@}. This corresponds {@{exactly to the set of intervals approximating $r$}@}. <!--SR:!2025-12-10,272,330!2025-12-28,285,330!2027-10-27,789,330!2025-11-09,247,330!2025-11-16,253,330-->

This allows {@{the basic arithmetic operations on the real numbers to be defined in terms of [interval arithmetic](interval%20arithmetic.md)}@}. {@{This property and its relation with real numbers given only in terms of $A$ and $B$}@} is {@{particularly important in weaker foundations such as [constructive analysis](constructive%20analysis.md)}@}. <!--SR:!2025-12-11,272,330!2025-11-14,251,330!2025-12-23,281,330-->

## generalizations

### arbitrary linearly ordered sets

In the general case of {@{an arbitrary linearly ordered set _X_}@}, a __cut__ is {@{a pair $(A,B)$ such that $A\cup B=X$ and $a\in A$, $b\in B$ imply $a<b$}@}. Some authors {@{add the requirement that both _A_ and _B_ are nonempty}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2026-07-02,413,310!2025-12-10,272,330!2026-01-03,290,330-->

If {@{neither _A_ has a maximum, nor _B_ has a minimum}@}, {@{the cut is called a __gap__}@}. {@{A linearly ordered set endowed with the order topology is compact}@} {@{if and only if it has no gap}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-12-01,264,330!2025-12-02,265,330!2025-11-28,262,330!2025-12-03,266,330-->

### surreal numbers

{@{A construction resembling Dedekind cuts}@} is used for {@{\(one among many possible\) constructions of [surreal numbers](surreal%20number.md)}@}. The relevant notion in this case is {@{a Cuesta-Dutari cut}@},<sup>[\[7\]](#^ref-7)</sup> named after {@{the Spanish mathematician [Norberto Cuesta Dutari](Norberto%20Cuesta%20Dutari.md) \[[es](../spa/Norberto%20Cuesta%20Dutari.md)\]}@}. <!--SR:!2026-01-04,291,330!2027-11-03,795,330!2027-08-25,742,330!2027-11-01,794,330-->

### partially ordered sets

- Main article: [Dedekind–MacNeille completion](Dedekind–MacNeille%20completion.md)

More generally, if {@{_S_ is a [partially ordered set](partially%20ordered%20set.md)}@}, {@{a _completion_ of _S_}@} means {@{a [complete lattice](complete%20lattice.md) _L_ with an order-embedding of _S_ into _L_}@}. {@{The notion of _complete lattice_}@} {@{generalizes the least-upper-bound property of the reals}@}. <!--SR:!2025-12-14,275,330!2025-10-29,238,330!2025-12-15,276,330!2025-11-25,259,330!2025-11-29,263,330-->

{@{One completion of _S_}@} is {@{the set of its _downwardly closed_ subsets, ordered by [inclusion](subset.md)}@}. {@{A related completion that preserves all existing sups and infs of _S_}@} is obtained by the following construction: For {@{each subset _A_ of _S_}@}, let {@{_A_<sup>u</sup> denote the set of upper bounds of _A_, and let _A_<sup>l</sup> denote the set of lower bounds of _A_}@}. \(These operators form {@{a [Galois connection](Galois%20connection.md)}@}.\) Then {@{the [Dedekind–MacNeille completion](Dedekind–MacNeille%20completion.md) of _S_}@} consists of {@{all subsets _A_ for which \(_A_<sup>u</sup>\)<sup>l</sup> = _A_; it is ordered by inclusion}@}. {@{The Dedekind-MacNeille completion}@} is {@{the smallest complete lattice with _S_ embedded in it}@}. <!--SR:!2025-12-10,272,330!2026-12-01,520,310!2027-07-23,720,330!2026-12-11,527,310!2025-12-10,272,330!2027-11-13,806,330!2027-12-06,825,330!2027-01-11,549,310!2028-08-18,1035,350!2027-09-18,751,330-->

## notes

This text incorporates [content](https://en.wikipedia.org/wiki/Dedekind_cut) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFBertrand1849"></a> Bertrand, Joseph \(1849\). [_Traité d'Arithmétique_](https://gallica.bnf.fr/ark:/12148/bpt6k77735p/f209.image.r=%22joseph%20bertrand%22). page 203. An incommensurable number can be defined only by indicating how the magnitude it expresses can be formed by means of unity. In what follows, we suppose that this definition consists of indicating which are the commensurable numbers smaller or larger than it .... <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFSpalt2019"></a> Spalt, Detlef \(2019\). _Eine kurze Geschichte der Analysis_. Springer. [doi](digital%20object%20identifier.md):[10.1007/978-3-662-57816-2](https://doi.org/10.1007%2F978-3-662-57816-2). [ISBN](ISBN.md) [978-3-662-57815-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-662-57815-5). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFDedekind1872"></a> Dedekind, Richard \(1872\). [_Continuity and Irrational Numbers_](http://www.math.ubc.ca/~cass/courses/m446-05b/dedekind-book.pdf#page=15) \(PDF\). Section IV. Whenever, then, we have to do with a cut produced by no rational number, we create a new _irrational_ number, which we regard as completely defined by this cut ... . From now on, therefore, to every definite cut there corresponds a definite rational or irrational number .... <a id="^ref-3"></a>^ref-3
4. In the second line, {@{$\geq$ may be replaced by $>$ without any difference}@} as {@{there is no solution for $x^{2}=2$ in $\mathbb {Q}$ and $b=0$ is already forbidden by the first condition}@}. This results in {@{the equivalent expression $$B=\{b\in \mathbb {Q} :b^{2}>2{\text{ and } }b>0\}.$$}@} <a id="^ref-4"></a>^ref-4
5. R. Engelking, General Topology, I.3 <a id="^ref-5"></a>^ref-5
6. Jun-Iti Nagata, Modern General Topology, Second revised edition, Theorem VIII.2, p. 461. Actually, the theorem holds in the setting of generalized ordered spaces, but in this more general setting pseudo-gaps should be taken into account. <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFAlling1987"></a> Alling, Norman L. \(1987\). _Foundations of Analysis over Surreal Number Fields_. Mathematics Studies 141. North-Holland. [ISBN](ISBN.md) [0-444-70226-1](https://en.wikipedia.org/wiki/Special:BookSources/0-444-70226-1). <a id="^ref-7"></a>^ref-7 <!--SR:!2025-12-22,281,330!2025-11-27,261,330!2025-11-17,254,330-->

## references

- Dedekind, Richard, _Essays on the Theory of Numbers_, "Continuity and Irrational Numbers," Dover Publications: New York, [ISBN](ISBN.md) [0-486-21010-3](https://en.wikipedia.org/wiki/Special:BookSources/0-486-21010-3). Also [available](https://www.gutenberg.org/ebooks/21016) at Project Gutenberg.

## external links

- ["Dedekind cut"](https://www.encyclopediaofmath.org/index.php?title=Dedekind_cut), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]

| <!-- hide- [v](https://en.wikipedia.org/wiki/Template:Rational%20numbers) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Rational%20numbers) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ARational%20numbers) <p>  <br/> --> [Rational numbers](rational%20number.md) |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [Integer](integer.md) <br/> - __Dedekind cut__ <br/> - [Dyadic rational](dyadic%20rational.md) <br/> - [Half-integer](half-integer.md) <br/> - [Superparticular ratio](superparticular%20ratio.md)                                                                                                      |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Order theory](https://en.wikipedia.org/wiki/Category:Order%20theory)
> - [Rational numbers](https://en.wikipedia.org/wiki/Category:Rational%20numbers)
> - [Real numbers](https://en.wikipedia.org/wiki/Category:Real%20numbers)
