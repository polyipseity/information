---
aliases:
  - Peano axiom
  - Peano axioms
tags:
  - flashcard/active/general/Peano_axioms
  - language/in/English
---

# Peano axioms

In [mathematical logic](mathematical%20logic.md), the __Peano axioms__ (/piˈɑːnoʊ/, \[peˈaːno\]), also known as {@{the __Dedekind–Peano axioms__ or the __Peano postulates__}@}, are {@{[axioms](axiom.md) for the [natural numbers](natural%20number.md) presented by the 19th-century Italian mathematician [Giuseppe Peano](Giuseppe%20Peano.md)}@}. These axioms have been used {@{nearly unchanged in a number of [metamathematical](metamathematics.md) investigations, including research into fundamental questions of whether [number theory](number%20theory.md) is [consistent](consistency.md) and [complete](completeness%20(logic).md)}@}.

The [axiomatization](axiomatic%20system.md#axiomatization) of [arithmetic](arithmetic.md) provided by Peano axioms is commonly called {@{__Peano arithmetic__}@}.

The importance of formalizing [arithmetic](arithmetic.md) was not well appreciated until {@{the work of [Hermann Grassmann](Hermann%20Grassmann.md)}@}, who showed {@{in the 1860s that many facts in arithmetic could be derived from more basic facts about the [successor operation](successor%20function.md) and [induction](mathematical%20induction.md)}@}. In {@{1881, [Charles Sanders Peirce](Charles%20Sanders%20Peirce.md)}@} provided {@{an [axiomatization](axiomatic%20system.md#axiomatization) of natural-number arithmetic}@}. In {@{1888, [Richard Dedekind](Richard%20Dedekind.md)}@} proposed {@{another axiomatization of natural-number arithmetic}@}, and in {@{1889, Peano}@} published {@{a simplified version of them as a collection of axioms in his book _The principles of arithmetic presented by a new method_ ([Latin](Latin.md): _[Arithmetices principia, nova methodo exposita](arithmetices%20principia,%20nova%20methodo%20exposita.md)_)}@}.

{@{The nine Peano axioms}@} contain {@{three types of statements}@}. The first axiom {@{asserts the existence of at least one member of the set of natural numbers}@}. The next {@{four are general statements about [equality](equality%20(mathematics).md)}@}; in modern treatments {@{these are often not taken as part of the Peano axioms, but rather as axioms of the "underlying logic"}@}. The next three axioms are {@{[first-order](first-order%20logic.md) statements about natural numbers expressing the fundamental properties of the successor operation}@}. The ninth, final axiom is {@{a [second-order](second-order%20logic.md) statement of the principle of mathematical induction over the natural numbers, which makes this formulation close to [second-order arithmetic](second-order%20arithmetic.md)}@}. {@{A weaker first-order system}@} is obtained by {@{explicitly adding the addition and multiplication operation symbols and replacing the [second-order induction](second-order%20arithmetic.md#induction%20and%20comprehension%20schema) axiom with a first-order [axiom schema](axiom%20schema.md)}@}. The term _Peano arithmetic_ is sometimes used for {@{specifically naming this restricted system}@}.

## historical second-order formulation

When Peano formulated his axioms, {@{the language of [mathematical logic](mathematical%20logic.md) was in its infancy}@}. The system of logical notation he created to present the axioms did not prove to be popular, although it was {@{the genesis of the modern notation for [set membership](element%20(mathematics).md) (∈, which comes from Peano's ε)}@}. Peano {@{maintained a clear distinction between mathematical and logical symbols, which was not yet common in mathematics}@}; such a separation had first been introduced in {@{the _[Begriffsschrift](begriffsschrift.md)_ by [Gottlob Frege](Gottlob%20Frege.md), published in 1879}@}. Peano was {@{unaware of Frege's work and independently recreated his logical apparatus}@} based on {@{the work of [Boole](George%20Boole.md) and [Schröder](Ernst%20Schröder%20(mathematician).md)}@}.

The Peano axioms {@{define the arithmetical properties of _[natural numbers](natural%20number.md)_, usually represented as a [set](set%20(mathematics).md) __N__ or $\mathbb {N}$}@}. The [non-logical symbols](non-logical%20symbol.md) for the axioms consist of {@{a constant symbol 0 and a unary function symbol _S_}@}.

The first axiom states {@{that the constant 0 is a natural number}@}:

1. 1st axiom ::@:: 0 is a natural number.

Peano's original formulation of the axioms {@{used 1 instead of 0 as the "first" natural number, while the axioms in _[Formulario mathematico](formulario%20mathematico.md)_ include zero}@}.

The next four axioms describe {@{the [equality](equality%20(mathematics).md) [relation](relation%20(mathematics).md)}@}. Since {@{they are logically valid in first-order logic with equality}@}, they are {@{not considered to be part of "the Peano axioms" in modern treatments}@}.

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD029 -->
2. 2nd axiom ::@:: For every natural number _x_, _x_ = _x_. That is, equality is [reflexive](reflexive%20relation.md).
3. 3rd axiom ::@:: For all natural numbers _x_ and _y_, if _x_ = _y_, then _y_ = _x_. That is, equality is [symmetric](symmetric%20relation.md).
4. 4th axiom ::@:: For all natural numbers _x_, _y_ and _z_, if _x_ = _y_ and _y_ = _z_, then _x_ = _z_. That is, equality is [transitive](transitive%20relation.md).
5. 5th axiom ::@:: For all _a_ and _b_, if _b_ is a natural number and _a_ = _b_, then _a_ is also a natural number. That is, the natural numbers are [closed](closure%20(mathematics).md) under equality.
<!-- markdownlint-restore -->

The remaining axioms {@{define the arithmetical properties of the natural numbers}@}. The naturals are {@{assumed to be closed under a single-valued "[successor](successor%20function.md)" [function](function%20(mathematics).md) _S_}@}.

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD029 -->
6. 6th axiom ::@:: For every natural number _n_, _S_(_n_) is a natural number. That is, the natural numbers are [closed](closure%20(mathematics).md) under _S_.
7. 7th axiom ::@:: For all natural numbers _m_ and _n_, if _S_(_m_) = _S_(_n_), then _m_ = _n_. That is, _S_ is an [injection](injective%20function.md).
8. 8th axiom ::@:: For every natural number _n_, _S_(_n_) = 0 is false. That is, there is no natural number whose successor is 0.
<!-- markdownlint-restore -->

The chain of light dominoes on the right, starting with the nearest, can {@{represent the set __N__ of natural numbers}@}. However, axioms 1–8 are {@{_also_ satisfied by the set of all dominoes — whether light (am infinite chain of dominoes) or dark (a finite circular chain of dominoes) — taken together}@}. The 9th axiom {@{([induction](mathematical%20induction.md)) limits __N__ to the chain of light pieces ("no junk") as only light dominoes will fall when the nearest is toppled}@}. {@{Axioms 1, 6, 7, 8}@} define {@{a [unary representation](unary%20numeral%20system.md) of the intuitive notion of natural numbers: the number 1 can be defined as _S_(0), 2 as _S_(_S_(0)), etc.}@} However, considering {@{the notion of natural numbers as being defined by these axioms}@}, axioms 1, 6, 7, 8 {@{do not imply that the successor function generates all the natural numbers different from 0}@}.

The intuitive notion that {@{each natural number can be obtained by applying _successor_ sufficiently many times to zero}@} requires {@{an additional axiom, which is sometimes called the _[axiom of induction](mathematical%20induction.md#axiom%20of%20induction)_}@}.

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD029 -->
9. 9th axiom condition (set) ::@:: If _K_ is a set such that: 0 is in _K_, and for every natural number _n_, _n_ being in _K_ implies that _S_(_n_) is in _K_, then _K_ contains every natural number.
<!-- markdownlint-restore -->

The induction axiom is sometimes stated in the following form:

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD029 -->
9. 9th axiom condition (predicate) ::@:: If _φ_ is a unary [predicate](predicate%20(mathematical%20logic).md) such that: _φ_(0) is true, and for every natural number _n_, _φ_(_n_) being true implies that _φ_(_S_(_n_)) is true, then _φ_(_n_) is true for every natural number _n_.
<!-- markdownlint-restore -->

In Peano's original formulation, the induction axiom is {@{a [second-order axiom](second-order%20logic.md)}@}. It is now common to {@{replace this second-order principle with a weaker [first-order](first-order%20logic.md) induction scheme}@}. There are {@{important differences between the second-order and first-order formulations, as discussed in the section [§ Peano arithmetic as first-order theory](#peano%20arithmetic%20as%20first-order%20theory) below}@}.

### defining arithmetic operations and relations

If we use the second-order induction axiom, it is {@{possible to define [addition](addition.md), [multiplication](multiplication.md), and [total (linear) ordering](total%20order.md) on [__N__](natural%20number.md#notation) directly using the axioms}@}. However, with first-order induction, this is {@{not possible and addition and multiplication are often added as axioms}@}. The respective functions and relations are {@{constructed in [set theory](set%20theory.md) or [second-order logic](second-order%20logic.md), and can be shown to be unique using the Peano axioms}@}.

#### addition

[Addition](addition.md#natural%20numbers) is {@{a function that [maps](map%20(mathematics).md) two natural numbers (two elements of __N__) to another one}@}. It is defined [recursively](recursion.md) as: {@{$${\begin{aligned}a+0&=a,&{\textrm {(1)} }\\a+S(b)&=S(a+b).&{\textrm {(2)} }\end{aligned} }$$}@}

For example:

$${\begin{aligned}a+1&=a+S(0)&{\text{by definition} }\\&=S(a+0)&{\text{using (2)} }\\&=S(a),&{\text{using (1)} }\\\\a+2&=a+S(1)&{\text{by definition} }\\&=S(a+1)&{\text{using (2)} }\\&=S(S(a))&{\text{using } }a+1=S(a)\\\\a+3&=a+S(2)&{\text{by definition} }\\&=S(a+2)&{\text{using (2)} }\\&=S(S(S(a)))&{\text{using } }a+2=S(S(a)) \\ {\text{etc.} }&\\\end{aligned} }$$

To {@{prove commutativity of addition}@}, first {@{prove $0+b=b$ and $S(a)+b=S(a+b)$, each by induction on $b$. Using both results, then prove $a+b=b+a$ by induction on $b$}@}. The [structure](mathematical%20structure.md) (__N__, +) is {@{a [commutative](commutative%20property.md) [monoid](monoid.md) with identity element 0. (__N__, +) is also a [cancellative](cancellation%20property.md) [magma](magma%20(algebra).md), and thus [embeddable](embedding.md) in a [group](group%20(mathematics).md)}@}. The smallest group embedding __N__ is {@{the [integers](integer.md)}@}.

> [!tip] tips
>
> - intuition of the definition ::@:: The 1st statement defines the base case, and the 2nd statement unwraps (decrements) the 2nd argument, i.e. $a + b \mapsto a + S(b - 1) \mapsto S(a + (b - 1))$. The 2nd statement can be applied recursively until the 2nd argument becomes $0$, at which point the 1st statement can be applied to terminate the addition chain.

#### multiplication

Similarly, [multiplication](multiplication.md) is {@{a function mapping two natural numbers to another one}@}. Given {@{addition}@}, it is defined recursively as: {@{$${\begin{aligned}a\cdot 0&=0,\\a\cdot S(b)&=a+(a\cdot b).\end{aligned} }$$}@}.

It is easy to see that $S(0)$ is {@{the multiplicative [right identity](identity%20element.md): $$a\cdot S(0)=a+(a\cdot 0)=a+0=a$$}@}.

To show that $S(0)$ is {@{also the multiplicative left identity requires the induction axiom due to the way multiplication is defined}@}:

- multiplicative left identity / base case ::@:: $S(0)$ is the left identity of 0: $S(0)\cdot 0=0$.
- multiplication left identity / induction ::@:: If $S(0)$ is the left identity of $a$ (that is $S(0)\cdot a=a$), then $S(0)$ is also the left identity of $S(a)$: $S(0)\cdot S(a)=S(0)+S(0)\cdot a=S(0)+a=a+S(0)=S(a+0)=S(a)$, using commutativity of addition.

Therefore, by {@{the induction axiom $S(0)$ is the multiplicative left identity of all natural numbers}@}. Moreover, it can be shown that {@{multiplication is commutative and [distributes over](distributive%20property.md) addition: $$a\cdot (b+c)=(a\cdot b)+(a\cdot c)$$}@}.

Thus, {@{$(\mathbb {N} ,+,0,\cdot ,S(0))$}@} is {@{a commutative [semiring](semiring.md)}@}.

> [!tip] tips
>
> - intuition of the definition ::@:: The 1st statement defines the base case, and the 2nd statement unwraps (decrements) the 2nd argument, i.e. $a \cdot b \mapsto a \cdot S(b - 1) \mapsto a + (a \cdot (b - 1))$. The 2nd statement can be applied recursively until the 2nd argument becomes $0$, at which point the 1st statement can be applied to terminate the multiplication chain.

#### inequalities

{@{The usual [total order](total%20order.md) relation ≤ on natural numbers}@} can be defined as follows, assuming 0 is a natural number: {@{For all _a_, _b_ ∈ __N__, _a_ ≤ _b_ if and only if there exists some _c_ ∈ __N__ such that _a_ + _c_ = _b_}@}.

This relation is {@{stable under addition and multiplication}@}: for $a,b,c\in \mathbb {N}$, if _a_ ≤ _b_, then:

- _a_ + _c_ ≤ _b_ + _c_, and
- _a_ · _c_ ≤ _b_ · _c_.

Thus, {@{the structure (__N__, +, ·, 1, 0, ≤)}@} is {@{an [ordered semiring](ordered%20ring.md); because there is no natural number between 0 and 1, it is a discrete ordered semiring}@}.

The axiom of induction is {@{sometimes stated in the following form that uses a stronger hypothesis, making use of the order relation "≤"}@}:

For any [predicate](predicate%20(mathematical%20logic).md) _φ_, if

- _φ_(0) is true, and
- axiom of induction condition with inequalities ::@:: for every _n_ ∈ __N__, if _φ_(_k_) is true for every _k_ ∈ __N__ such that _k_ ≤ _n_, then _φ_(_S_(_n_)) is true,
- then for every _n_ ∈ __N__, _φ_(_n_) is true.

This form of the induction axiom, called {@{_strong induction_, is a consequence of the standard formulation}@}, but is {@{often better suited for reasoning about the ≤ order}@}. For example, to {@{show that the naturals are [well-ordered](well-order.md)—every [nonempty](empty%20set.md) [subset](subset.md) of __N__ has a [least element](greatest%20element%20and%20least%20element.md)}@}—one can reason as follows.

- proving the naturals are well-ordered / base case ::@:: Let a nonempty _X_ ⊆ __N__ be given and assume _X_ has no least element. Because 0 is the least element of __N__, it must be that 0 ∉ _X_.
- proving the naturals are well-ordered / induction ::@:: For any _n_ ∈ __N__, suppose for every _k_ ≤ _n_, _k_ ∉ _X_. Then _S_(_n_) ∉ _X_, for otherwise it would be the least element of _X_.

Thus, by {@{the strong induction principle, for every _n_ ∈ __N__, _n_ ∉ _X_. Thus, _X_ ∩ __N__ = ∅, which [contradicts](contradiction.md) _X_ being a nonempty subset of __N__}@}. Thus {@{_X_ has a least element}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Peano_axioms) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
