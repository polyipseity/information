---
aliases:
  - Bézout's identity
tags:
  - flashcard/active/general/eng/Bézout_s_identity
  - language/in/English
---

# Bézout's identity

- This article is about {@{Bézout's theorem in arithmetic}@}. For {@{Bézout's theorem in algebraic geometry}@}, see {@{[Bézout's theorem](Bézout's%20theorem.md)}@}.

In {@{[mathematics](mathematics.md)}@}, {@{__Bézout's identity__ \(also called __Bézout's lemma__\)}@}, named after {@{[Étienne Bézout](Étienne%20Bézout.md) who proved it for polynomials}@}, is {@{a [theorem](theorem.md) which relates two arbitrary [integers](integers.md) with their [greatest common divisor](greatest%20common%20divisor.md)}@}. {@{The theorem's statement}@} is as follows:

> {@{__Bézout's identity__}@}—Let _a_ and _b_ be {@{integers with greatest common divisor _d_}@}. Then there exist {@{integers _x_ and _y_ such that _ax_ + _by_ = _d_}@}. Moreover, {@{the integers of the form _az_ + _bt_}@} are {@{exactly the multiples of _d_}@}.

\({@{The greatest common divisor of 0 and 0}@} is {@{taken to be 0}@}.\) {@{The integers _x_ and _y_}@} are called {@{__Bézout coefficients__ for \(_a_, _b_\)}@}; they are {@{not unique}@}. {@{The [extended Euclidean algorithm](extended%20Euclidean%20algorithm.md)}@} can be used to {@{compute a minimal pair of Bézout coefficients}@}, meaning they {@{satisfy $|x|\leq |b/d|$ and $|y|<|a/d|$}@}; equality {@{occurs only if one of _a_ and _b_ is a multiple of the other}@}, and otherwise there {@{exist exactly two minimal pairs}@}.

As an example, {@{the greatest common divisor of $a=15$ and $b=69$}@} is {@{$d=3$}@}, which can be written as {@{the linear combination $ax+by = 15(-9)+69(2) = 3$}@} with {@{Bézout coefficients $(x,y)=(-9,2)$}@}, which are {@{minimal since $9<69/3=23$ and $2 < 15/3=5$}@}. {@{The other minimal Bézout coefficients}@} are {@{$(x,y)=(-9+23, 2-5)=(14, -3)$}@}.

Many {@{other theorems in [elementary number theory](elementary%20number%20theory.md#elementary%20number%20theory)}@}, such as {@{[Euclid's lemma](Euclid's%20lemma.md) or the [Chinese remainder theorem](Chinese%20remainder%20theorem.md)}@}, can be {@{formally deduced from Bézout's identity}@}.

{@{A [Bézout domain](Bézout%20domain.md)}@} is {@{an [integral domain](integral%20domain.md) in which Bézout's identity holds}@}. In particular, {@{Bézout's identity}@} holds in {@{[principal ideal domains](principal%20ideal%20domain.md)}@}. Every {@{theorem that results from Bézout's identity}@} is thus {@{true in all principal ideal domains}@}.

## structure of solutions

If {@{_a_ and _b_ are not both zero}@} and {@{one pair of Bézout coefficients \(_x_, _y_\)}@} has been {@{computed \(for example, using the [extended Euclidean algorithm](extended%20Euclidean%20algorithm.md)\)}@}, {@{all pairs}@} can be represented in {@{the form $$\left(x-k\frac{b}{d},\ y+k\frac{a}{d}\right),$$}@} where _k_ is {@{an arbitrary integer}@}, _d_ is {@{the greatest common divisor of _a_ and _b_}@}, and the fractions {@{simplify to integers}@}.

If {@{_a_ and _b_ are both nonzero}@} and {@{none of them divides the other}@}, then {@{exactly two of the pairs of Bézout coefficients}@} satisfy {@{$$|x| < \left |\frac{b}{d}\right |\quad \text{and}\quad |y| < \left |\frac{a}{d}\right |.$$}@} If {@{_a_ and _b_ are both positive}@}, one has {@{$x>0$ and $y<0$ for one of these pairs}@}, and {@{$x<0$ and $y>0$ for the other}@}. If {@{_a_ \> 0 is a divisor of _b_ \(including the case $b=0$\)}@}, then {@{one pair of Bézout coefficients is \(1, 0\)}@}.

This relies on {@{a property of [Euclidean division](Euclidean%20division.md)}@}: given {@{two non-zero integers _c_ and _d_}@}, if {@{_d_ does not divide _c_}@}, there is {@{exactly one pair \(_q_, _r_\) such that _c_ = _dq_ + _r_ and 0 \< _r_ \< \|_d_\|}@}, and {@{another one such that _c_ = _dq_ + _r_ and −\|_d_\| \< _r_ \< 0}@}.

{@{The two pairs of minimal Bézout coefficients}@} are obtained from {@{the given one \(_x_, _y_\)}@} by choosing for {@{_k_ in the above formula (annotation: $\left(x-k\frac{b}{d},\ y+k\frac{a}{d}\right)$)}@} {@{either of the two integers nearest to $\frac{x}{b/d}$}@}.

{@{The extended Euclidean algorithm}@} always produces {@{one of these two minimal pairs}@}.

### example

Let {@{_a_ = 12 and _b_ = 42}@}, then {@{gcd \(12, 42\) = 6}@}. Then {@{the following Bézout's identities}@} are displayed with {@{the Bézout coefficients written in red for the minimal pairs}@} and in {@{blue for the other ones}@}. {@{$$\begin{aligned} \vdots \\ 12 &\times ({\color{blue}{-10} }) & + \;\; 42 &\times \color{blue}{3} &= 6 \\ 12 &\times ({\color{red}{-3} }) & + \;\;42 &\times \color{red}{1} &= 6 \\ 12 &\times \color{red}{4} & + \;\;42 &\times({\color{red}{-1} }) &= 6 \\ 12 &\times \color{blue}{11} & + \;\;42 &\times ({\color{blue}{-3} }) &= 6 \\ 12 &\times \color{blue}{18} & + \;\;42 &\times ({\color{blue}{-5} }) &= 6 \\ \vdots \end{aligned}$$}@} If {@{\(_x_, _y_\) = \(18, −5\)}@} is {@{the original pair of Bézout coefficients}@}, then {@{$\frac{18}{42/6}∈ [2, 3]$}@} yields {@{the minimal pairs via _k_ = 2, respectively _k_ = 3}@}; that is, {@{\(18 − 2 ⋅ 7, −5 + 2 ⋅ 2\) = \(4, −1\), and \(18 − 3 ⋅ 7, −5 + 3 ⋅ 2\) = \(−3, 1\)}@}.

## existence proof

Given {@{any nonzero integers _a_ and _b_}@}, let {@{_S_ = {_ax_ + _by_ \| _x_, _y_ ∈ __Z__ and _ax_ + _by_ \> 0}<!-- flashcard separator -->}@}. {@{The set _S_ is nonempty}@} since it {@{contains either _a_ or –_a_ \(with _x_ = ±1 and _y_ = 0\)}@}. Since {@{_S_ is a nonempty set of positive integers}@}, it has {@{a minimum element _d_ = _as_ + _bt_, by the [well-ordering principle](well-ordering%20principle.md)}@}. To prove that _d_ is {@{the greatest common divisor of _a_ and _b_}@}, it must be proven that {@{_d_ is a common divisor of _a_ and _b_, and that for any other common divisor _c_, one has _c_ ≤ _d_}@}.

{@{The [Euclidean division](Euclidean%20division.md) of _a_ by _d_ (annotation: _d_ is the minimum element of _S_}@} may be written as {@{$$a=dq+r\quad\text{with}\quad 0\le r<d.$$}@} {@{The remainder _r_}@} is {@{in _S_ ∪ {0}<!-- flashcard separator -->}@}, because {@{$$\begin{aligned} r & = a - qd \\ & = a - q(as+bt)\\ & = a(1-qs) - bqt. \end{aligned}$$}@} Thus _r_ is {@{of the form _ax_ + _by_, and hence _r_ ∈ _S_ ∪ {0}<!-- flashcard separator -->}@}. However, {@{0 ≤ _r_ \< _d_}@}, and _d_ is {@{the smallest positive integer in _S_}@}: the remainder _r_ can therefore {@{not be in _S_, making _r_ necessarily 0}@}. This implies that {@{_d_ is a divisor of _a_}@}. Similarly _d_ is also {@{a divisor of _b_, and therefore _d_ is a common divisor of _a_ and _b_}@}.

Now, let _c_ be {@{any common divisor of _a_ and _b_}@}; that is, there exist {@{_u_ and _v_ such that _a_ = _cu_ and _b_ = _cv_}@}. One has thus {@{$$\begin{aligned} d&=as + bt\\ & =cus+cvt\\ &=c(us+vt). \end{aligned}$$}@} That is, {@{_c_ is a divisor of _d_}@}. Since {@{_d_ \> 0, this implies _c_ ≤ _d_}@}.

## corollaries

### writing any integer as a linear combination

{@{An immediate [corollary](corollary.md) of Bézout's identity}@} is that {@{_any_ integer _n_}@} can be {@{written as a [linear combination](linear%20combination.md) of _any_ two [coprime](coprime%20integers.md) integers}@}.<sup>[\[1\]](#^ref-1)</sup> Indeed, if {@{_a_ and _b_ are coprime}@}, then Bézout's identity guarantees {@{the existence of integers _x_ and _y_ such that _ax_ + _by_ = 1}@}. Multiplying {@{both sides by _n_ gives $a(xn)+b(yn) = n$}@}.

## generalizations

### for three or more integers

{@{Bézout's identity can be extended}@} to {@{more than two integers}@}: if {@{$$\gcd(a_1, a_2, \ldots, a_n) = d$$}@} then there are {@{integers $x_1, x_2, \ldots, x_n$ such that $$d = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n$$}@} has the following properties: (annotation: 2 items: {@{minimality of _d_, solutions of this form}@})

- (annotation: minimality of _d_) ::@:: _d_ is the smallest positive integer of this form
- (annotation: solutions of this form) ::@:: every number of this form is a multiple of _d_

### for polynomials

- Main article: ::@:: [Polynomial greatest common divisor § Bézout's identity and extended GCD algorithm](polynomial%20greatest%20common%20divisor.md#Bézout's%20identity%20and%20extended%20GCD%20algorithm)

{@{Bézout's identity does not always hold}@} for {@{polynomials with coefficients in a ring}@}. For example, when working in {@{the [polynomial ring](polynomial%20ring.md) with integer coefficients}@}: {@{the greatest common divisor of 2<!-- markdown separator -->_x_ and _x_<sup>2</sup>}@} is {@{_x_}@}, but there are {@{no integer-coefficient polynomials $p(x)$ and $q(x)$}@} satisfying {@{$2xp(x)+x^2q(x)=x$}@}.

However, Bézout's identity works for {@{[univariate polynomials](univariate%20polynomial.md#univariate) with coefficients in a [field](field%20(mathematics).md)}@}, exactly as for {@{the original case of integers}@}. In particular {@{the Bézout's coefficients and the greatest common divisor}@} may be computed with {@{the [extended Euclidean algorithm](extended%20Euclidean%20algorithm.md)}@}.

As {@{the common [roots](root%20of%20a%20polynomial.md) of two polynomials}@} are {@{the roots of their greatest common divisor}@}, {@{Bézout's identity and the [fundamental theorem of algebra](fundamental%20theorem%20of%20algebra.md)}@} imply the following result: (annotation: relating {@{greatest common divisor being 1 with the lack of common roots}@})

> For {@{univariate polynomials $a(x)$ and $b(x)$ with coefficients in a field}@}, there exist {@{polynomials $p(x)$ and $q(x)$ such that $a(x)p(x)+b(x)q(x)=1$}@} {@{if and only if $a(x)$ and $b(x)$ have no common root in any [algebraically closed field](algebraically%20closed%20field.md)}@} \(commonly {@{the field of [complex numbers](complex%20number.md)}@}\).

{@{The generalization of this result (annotation: relating greatest common divisor with the lack of common roots)}@} to {@{any number of polynomials and indeterminates}@} is {@{[Hilbert's Nullstellensatz](Hilbert's%20Nullstellensatz.md)}@}.

### for principal ideal domains

As noted {@{in the introduction, Bézout's identity}@} works {@{not only in the [ring](ring%20(algebra).md) of integers, but also in any other [principal ideal domain](principal%20ideal%20domain.md) \(PID\)}@}. That is, if _R_ is {@{a PID}@}, and _a_ and _b_ are {@{elements of _R_}@}, and _d_ is {@{a greatest common divisor of _a_ and _b_}@}, then there are {@{elements _x_ and _y_ in _R_ such that _ax_ + _by_ = _d_}@}. The reason is that {@{the [ideal](ideal%20(ring%20theory).md) _Ra_ + _Rb_}@} is {@{principal and equal to _Rd_}@}.

{@{An integral domain}@} in which {@{Bézout's identity holds}@} is called {@{a [Bézout domain](Bézout%20domain.md)}@}.

## history and attribution

{@{The French mathematician [Étienne Bézout](Étienne%20Bézout.md) \(1730–1783\)}@} proved {@{this identity for polynomials}@}.<sup>[\[2\]](#^ref-2)</sup> {@{The statement for integers}@} can be found {@{already in the work of an earlier French mathematician, [Claude Gaspard Bachet de Méziriac](Claude%20Gaspard%20Bachet%20de%20Méziriac.md) \(1581–1638\)}@}.<sup>[\[3\]](#^ref-3)</sup><sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> {@{[Andrew Granville](Andrew%20Granville.md) traced the association of Bézout's name}@} with {@{the identity to [Bourbaki](Nicolas%20Bourbaki.md)}@}, arguing that it is {@{a misattribution since the identity is implicit in [Euclid's _Elements_](Euclid's%20Elements.md)}@}.<sup>[\[6\]](#^ref-6)</sup>

## applications

{@{Bézout's identity strictly}@} determines {@{exactly which [water pouring puzzles](water%20pouring%20puzzles.md)}@} are {@{solvable}@}.

## see also

- [AF+BG theorem](AF+BG%20theorem.md) ::@:: – About algebraic curves passing through all intersection points of two other curves, an analogue of Bézout's identity for homogeneous polynomials in three indeterminates
- [Diophantine equation](Diophantine%20equation.md) ::@:: – Polynomial equation whose integer solutions are sought
- [Euclid's lemma](Euclid's%20lemma.md) ::@:: – On prime factors of integer products
- [Fundamental theorem of arithmetic](fundamental%20theorem%20of%20arithmetic.md) ::@:: – Integers have unique prime factorizations

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bézout's_identity) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFBressoud2022"></a> Bressoud, David \(2022-02-01\). ["My Mathematical Journey: The Stamp Problem"](https://maa.org/math-values/my-mathematical-journey-the-stamp-problem/#:~:text=if%20a%20and%20b%20are%20relatively%20prime%2C%20then%20every%20integer%20is%20a%20linear%20combination%20of%20a%20and%20b.). _[Mathematical Association of America](Mathematical%20Association%20of%20America.md)_. [Archived](https://web.archive.org/web/20260125061928/https://maa.org/math-values/my-mathematical-journey-the-stamp-problem/) from the original on 2026-01-25. Retrieved 2026-03-09. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFBézout, É.1779"></a> [Bézout, É.](Étienne%20Bézout.md) \(1779\). [_Théorie générale des équations algébriques_](https://archive.org/details/bub_gb_RDEVAAAAQAAJ). Paris, France: Ph.-D. Pierres. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFTignol2001"></a> [Tignol, Jean-Pierre](Jean-Pierre%20Tignol.md) \(2001\). _Galois' Theory of Algebraic Equations_. Singapore: World Scientific. [ISBN](ISBN%20(identifier).md) [981-02-4541-6](https://en.wikipedia.org/wiki/Special:BookSources/981-02-4541-6). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFClaude Gaspard Bachet (sieur de Méziriac)1624"></a> Claude Gaspard Bachet \(sieur de Méziriac\) \(1624\). [_Problèmes plaisants & délectables qui se font par les nombres_](http://www.bsb-muenchen-digital.de/~web/web1008/bsb10081407/images/index.html?digID=bsb10081407&pimage=38&v=100&nav=0&l=de) \(2nd ed.\). Lyon, France: Pierre Rigaud & Associates. pp. 18–33. On these pages, Bachet proves \(without equations\) "Proposition XVIII. Deux nombres premiers entre eux estant donnez, treuver le moindre multiple de chascun d’iceux, surpassant de l'unité un multiple de l'autre." \(Given two numbers \[which are\] relatively prime, find the lowest multiple of each of them \[such that\] one multiple exceeds the other by unity \(1\).\) This problem \(namely, _ax_ − _by_ = 1\) is a special case of Bézout's equation and was used by Bachet to solve the problems appearing on pages 199 ff. <a id="^ref-4"></a>^ref-4
5. See also: <a id="CITEREFMaarten Bullynck2009"></a> Maarten Bullynck \(February 2009\). ["Modular arithmetic before C.F. Gauss: Systematizations and discussions on remainder problems in 18th-century Germany"](http://hal.inria.fr/docs/00/66/32/92/PDF/Gauss_Modular_Oct2008.pdf) \(PDF\). _Historia Mathematica_. __36__ \(1\): 48–72. [doi](doi%20(identifier).md):[10.1016/j.hm.2008.08.009](https://doi.org/10.1016%2Fj.hm.2008.08.009). [Archived](https://ghostarchive.org/archive/20221009/http://hal.inria.fr/docs/00/66/32/92/PDF/Gauss_Modular_Oct2008.pdf) \(PDF\) from the original on 2022-10-09. <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFGranville2024"></a> Granville, Andrew \(2024\). "It is not "Bézout's identity"". [arXiv](ArXiv%20(identifier).md):[2406.15642](https://arxiv.org/abs/2406.15642) \[[math.HO](https://arxiv.org/archive/math.HO)\]. <a id="^ref-6"></a>^ref-6

## external links

- [Online calculator](http://wims.unice.fr/wims/wims.cgi?module=tool/arithmetic/bezout.en) for Bézout's identity
- <a id="CITEREFWeisstein"></a> [Weisstein, Eric W.](Eric%20W.%20Weisstein.md) ["Bézout's Identity"](https://mathworld.wolfram.com/BezoutsIdentity.html). _[MathWorld](MathWorld.md)_.

|                   | [Authority control databases](https://en.wikipedia.org/wiki/Help:Authority%20control) <!-- [![Edit this at Wikidata](../../archives/Wikimedia%20Commons/OOjs%20UI%20icon%20edit-ltr-progressive.svg)](https://www.wikidata.org/wiki/Q513028#identifiers) --> |
| ----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| __International__ | - [GND](https://d-nb.info/gnd/4336292-8) <br/> - [FAST](https://id.worldcat.org/fast/1749056)                                                                                                                                                                |
|      __National__ | - [United States](https://id.loc.gov/authorities/sh2007006114) <br/> - [Israel](https://www.nli.org.il/en/authorities/987007535386805171)                                                                                                                    |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Diophantine equations](https://en.wikipedia.org/wiki/Category:Diophantine%20equations)
> - [Lemmas in number theory](https://en.wikipedia.org/wiki/Category:Lemmas%20in%20number%20theory)
