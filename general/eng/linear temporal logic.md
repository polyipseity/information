---
aliases:
  - LTL
  - LTLs
  - linear temporal logic
  - linear temporal logics
tags:
  - flashcard/active/general/eng/linear_temporal_logic
  - language/in/English
---

# linear temporal logic

In [logic](logic.md), {@{__linear temporal logic__ or __linear-time temporal logic__<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> \(__LTL__\)}@} is {@{a [modal](modal%20logic.md) [temporal logic](temporal%20logic.md) with modalities referring to time}@}. In LTL, one can {@{encode [formulae](well-formed%20formula.md) about the future of [paths](path%20(graph%20theory).md)}@}, e.g., {@{a condition will eventually be true, a condition will be true until another fact becomes true}@}, etc. It is a fragment of {@{the more complex [CTL\*](CTL*.md)}@}, which {@{additionally allows branching time and [quantifiers](quantifier%20(logic).md)}@}. LTL is sometimes called {@{_propositional temporal logic_, abbreviated _PTL_}@}.<sup>[\[3\]](#^ref-3)</sup> In terms of {@{[expressive power](expressive%20power%20(computer%20science).md)}@}, linear temporal logic \(LTL\) is {@{a fragment of [first-order logic](first-order%20logic.md)}@}.<sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-09-28,228,343!2025-03-06,70,330!2025-03-16,79,343!2025-07-19,167,317!2025-03-16,79,343!2025-02-27,64,330!2025-02-20,58,317!2025-02-22,60,317!2025-03-16,79,343-->

LTL was first {@{proposed for the [formal verification](formal%20verification.md) of computer programs}@} by {@{[Amir Pnueli](Amir%20Pnueli.md) in 1977}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-03-10,74,343!2025-05-26,115,303-->

## syntax

LTL is built up from {@{a finite set of [propositional variables](propositional%20variable.md) _AP_, the [logical operators](logical%20connective.md) ¬ and ∨}@}, and {@{the [temporal](temporal%20logic.md) [modal operators](modal%20operator.md) __X__ \(some literature uses __O__ or __N__\) and __U__}@}. Formally, {@{the set of LTL formulas over _AP_}@} is {@{inductively defined as follows}@}: <!--SR:!2025-03-16,79,343!2025-03-16,79,343!2025-03-01,66,330!2025-06-02,131,323-->

- if _p_ ∈ _AP_ ::@:: then _p_ is an LTL formula; <!--SR:!2025-03-16,79,343!2025-03-15,78,343-->
- if _ψ_ and _φ_ are LTL formulas ::@:: then ¬ψ, φ ∨ ψ, __X__ ψ, and φ __U__ ψ are LTL formulas.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-03-15,78,343!2025-02-27,64,330-->

__X__ is read as {@{ne<!-- markdown separator -->__x__<!-- markdown separator -->t and __U__ is read as __u__<!-- markdown separator -->ntil}@}. Other than {@{these fundamental operators}@}, there are {@{additional logical and temporal operators defined in terms of the fundamental operators, in order to write LTL formulas succinctly}@}. The additional logical operators are {@{∧, →, ↔, __true__, and __false__}@}. Following are {@{the additional temporal operators}@}. <!--SR:!2025-09-08,208,330!2025-03-20,82,343!2025-03-15,78,343!2025-03-10,74,343!2025-03-01,66,330-->

- __G__ ::@:: for always \(__g__<!-- markdown separator -->lobally\) <!--SR:!2025-03-15,78,343!2025-03-16,79,343-->
- __F__ ::@:: for __f__<!-- markdown separator -->inally <!--SR:!2025-03-15,78,343!2025-02-22,57,323-->
- __R__ ::@:: for __r__<!-- markdown separator -->elease <!--SR:!2025-03-16,79,343!2025-03-17,79,343-->
- __W__ ::@:: for __w__<!-- markdown separator -->eak until <!--SR:!2025-03-15,78,343!2025-03-17,79,343-->
- __M__ ::@:: for __m__<!-- markdown separator -->ighty release <!--SR:!2025-08-03,183,330!2025-02-22,60,317-->

## semantics

An LTL formula can be {@{_[satisfied](satisfiability.md)_ by an infinite sequence of truth valuations of variables in _AP_}@}. These sequences can be viewed as {@{a word on a path of a [Kripke structure](Kripke%20structure%20(model%20checking).md)}@} \({@{an [ω-word](omega%20language.md) over [alphabet](alphabet%20(formal%20languages).md) 2<sup>_AP_</sup>}@}\). Let {@{_w_ = a<sub>0</sub>,a<sub>1</sub>,a<sub>2</sub>,... be such an ω-word}@}. Let {@{_w_\(_i_\) = _a<sub>i</sub>_. Let _w_<sup>i</sup> = _a<sub>i</sub>_,_a_<sub>_i_+1</sub>,..., which is a suffix of _w_}@}. Formally, {@{the satisfaction relation ⊨ between a word and an LTL formula}@} is defined as follows: <!--SR:!2025-03-19,81,343!2025-02-19,54,310!2025-03-05,69,330!2025-03-12,75,330!2025-02-20,55,310!2025-03-12,75,330-->

- satisfaction of a propositional variable ::@:: _w_ ⊨ _p_ if _p_ ∈ _w_\(0\) <!--SR:!2025-03-10,74,343!2025-03-10,74,343-->
- law of the excluded middle ::@:: _w_ ⊨ ¬ψ if _w_ ⊭ ψ <!--SR:!2025-03-08,72,330!2025-02-28,65,330-->
- or ::@:: _w_ ⊨ φ ∨ ψ if _w_ ⊨ φ or _w_ ⊨ ψ <!--SR:!2025-03-10,74,343!2025-02-20,58,317-->
- ne<!-- markdown separator -->__x__<!-- markdown separator -->t ::@:: _w_ ⊨ __X__ ψ if _w_<sup>1</sup> ⊨ ψ \(in the ne<!-- markdown separator -->__x__<!-- markdown separator -->t time step ψ must be true\) <!--SR:!2025-02-22,57,323!2025-03-18,80,343-->
- __u__<!-- markdown separator -->ntil ::@:: _w_ ⊨ φ __U__ ψ if there exists _i_ ≥ 0 such that _w_<sup>_i_</sup> ⊨ ψ and for all 0 ≤ _k_ \< i, _w_<sup>_k_</sup> ⊨ φ \(φ must remain true __u__<!-- markdown separator -->ntil ψ becomes true\) <!--SR:!2025-03-13,76,330!2025-02-17,53,323-->

We say {@{an ω-word _w_ satisfies an LTL formula ψ when _w_ ⊨ ψ}@}. {@{The [ω-language](omega%20language.md) _L_\(ψ\) defined by ψ}@} is {@{<!-- flashcard separator -->{_w_ \| _w_ ⊨ ψ}, which is the set of ω-words that satisfy ψ}@}. {@{A formula ψ is _satisfiable_}@} if {@{there exist an ω-word _w_ such that _w_ ⊨ ψ}@}. {@{A formula ψ is _valid_}@} if {@{for each ω-word _w_ over alphabet 2<sup>_AP_</sup>, we have _w_ ⊨ ψ}@}. <!--SR:!2025-03-01,66,330!2025-03-20,82,343!2025-03-21,83,343!2025-03-15,78,343!2025-03-13,76,330!2025-06-14,133,310!2025-03-16,79,343-->

The additional logical operators are defined as follows:

- and ::@:: φ ∧ ψ ≡ ¬\(¬φ ∨ ¬ψ\) <!--SR:!2025-03-21,83,343!2025-03-02,67,330-->
- implies ::@:: φ → ψ ≡ ¬φ ∨ ψ <!--SR:!2025-02-28,65,317!2025-03-02,67,330-->
- material equivalence ::@:: φ ↔ ψ ≡ \(φ → ψ\) ∧ \( ψ → φ\) <!--SR:!2025-02-28,65,330!2025-03-16,79,343-->
- true ::@:: __true__ ≡ _p_ ∨ ¬<!-- markdown separator -->_p_, where _p_ ∈ _AP_ <!--SR:!2025-03-16,79,343!2025-03-15,78,343-->
- false ::@:: __false__ ≡ ¬<!-- markdown separator -->__true__ <!--SR:!2025-03-17,79,343!2025-02-19,57,317-->

The additional temporal operators {@{__R__, __F__, and __G__}@} are defined as follows: <!--SR:!2025-03-15,78,343-->

- __r__<!-- markdown separator -->elease ::@:: ψ __R__ φ ≡ ¬\(¬ψ __U__ ¬φ\) \(φ remains true until and including once ψ becomes true. If ψ never becomes true, φ must remain true forever. ψ __r__<!-- markdown separator -->eleases φ.\) <!--SR:!2025-04-17,96,290!2025-02-22,60,317-->
- __f__<!-- markdown separator -->inally ::@:: __F__ ψ ≡ __true__ __U__ ψ \(eventually ψ becomes true\) <!--SR:!2025-05-29,127,297!2025-02-19,57,317-->
- __g__<!-- markdown separator -->lobally ::@:: __G__ ψ ≡ __false__ __R__ ψ ≡ ¬<!-- markdown separator -->__F__ ¬ψ \(ψ always remains true\) <!--SR:!2025-02-28,65,330!2025-02-21,59,317-->

### weak until and strong release

Some authors also define {@{a _weak until_ binary operator, denoted __W__}@}, with semantics {@{similar to that of the until operator but the stop condition is not required to occur \(similar to release\)}@}.<sup>[\[8\]](#^ref-8)</sup> It is sometimes useful since {@{both __U__ and __R__ can be defined in terms of the weak until}@}: <!--SR:!2025-03-19,81,343!2025-03-15,78,343!2025-07-14,152,310-->

- __w__<!-- markdown separator -->eak until (annotation: in terms of _<!-- markdown separator -->__u__<!-- markdown separator -->ntil_, _<!-- markdown separator -->__u__<!-- markdown separator -->ntil_, _<!-- markdown separator -->__r__<!-- markdown separator -->elease_) ::@:: _ψ_ __W__ _φ_ ≡ \(_ψ_ __U__ _φ_\) ∨ __G__ _ψ_ ≡ _ψ_ __U__ \(_φ_ ∨ __G__ _ψ_\) ≡ _φ_ __R__ \(_φ_ ∨ _ψ_\) <!--SR:!2025-05-06,102,303!2025-03-02,58,277-->
- __u__<!-- markdown separator -->ntil (annotation: in terms of _<!-- markdown separator -->__w__<!-- markdown separator -->eak until_) ::@:: _ψ_ __U__ _φ_ ≡ __F__<!-- markdown separator -->_φ_ ∧ \(_ψ_ __W__ _φ_\) <!--SR:!2025-05-26,124,297!2025-06-16,143,323-->
- __r__<!-- markdown separator -->elease (annotation: in terms of _<!-- markdown separator -->__w__<!-- markdown separator -->eak until_) ::@:: _ψ_ __R__ _φ_ ≡ _φ_ __W__ \(_φ_ ∧ _ψ_\) <!--SR:!2025-05-15,97,263!2025-05-25,114,303-->

{@{The _strong release_ binary operator, denoted __M__}@}, is {@{the dual of weak until}@}. It is defined {@{similar to the until operator, so that the release condition has to hold at some point}@}. Therefore, {@{it is stronger than the release operator}@}. <!--SR:!2025-03-11,74,330!2025-03-15,78,343!2025-02-22,57,323!2025-07-15,163,317-->

- strong release (__M__) (annotation: in terms of _<!-- markdown separator -->__w__<!-- markdown separator -->eak util_, _<!-- markdown separator -->__r__<!-- markdown separator -->elease_, _<!-- markdown separator -->__r__<!-- markdown separator -->elease_, _<!-- markdown separator -->__u__<!-- markdown separator -->ntil_) ::@:: _ψ_ __M__ _φ_ ≡ ¬\(¬<!-- markdown separator -->_ψ_ __W__ ¬<!-- markdown separator -->_φ_\) ≡ \(_ψ_ __R__ _φ_\) ∧ __F__ _ψ_ ≡ _ψ_ __R__ \(_φ_ ∧ __F__ _ψ_\) ≡ _φ_ __U__ \(_ψ_ ∧ _φ_\) <!--SR:!2025-03-04,39,243!2025-02-23,54,283-->

{@{The semantics for the temporal operators}@} are pictorially presented as follows. <!--SR:!2025-03-15,78,343-->

| Textual                                    | Symbolic                                | Explanation                                                                                                                                                                         | Diagram                                                                                                                                                                                        |
| ------------------------------------------ | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Unary operators](unary%20operation.md):   |                                         |                                                                                                                                                                                     |                                                                                                                                                                                                |
| {@{__X__ _φ_}@}                            | {@{$$\bigcirc \varphi$$}@}                | {@{ne<!-- markdown separator -->__X__<!-- markdown separator -->t: _φ_ has to hold at the next state.}@}                                                                              | {@{![LTI next diagram](../../archives/Wikimedia%20Commons/Ltlnext.svg)}@}                                                                                                                           |
| {@{__F__ _φ_}@}                            | {@{$$\Diamond \varphi$$}@}                | {@{__F__<!-- markdown separator -->inally: _φ_ eventually has to hold \(somewhere on the subsequent path\).}@}                                                                        | {@{![LTI finally diagram](../../archives/Wikimedia%20Commons/Ltleventually.svg)}@}                                                                                                                  |
| {@{__G__ _φ_}@}                            | {@{$$\Box \varphi$$}@}                    | {@{__G__<!-- markdown separator -->lobally: _φ_ has to hold on the entire subsequent path.}@}                                                                                         | {@{![LTI globally diagram](../../archives/Wikimedia%20Commons/Ltlalways.svg)}@}                                                                                                                     |
| [Binary operators](binary%20operation.md): |                                         |                                                                                                                                                                                     |                                                                                                                                                                                                |
| {@{_ψ_ __U__ _φ_}@}                          | {@{$$\psi \;{\mathcal {U} }\,\varphi$$}@} | {@{__U__<!-- markdown separator -->ntil: _ψ_ has to hold _at least_ until _φ_ becomes true, which must hold at the current or a future position.}@}                                   | {@{![LTI until diagram](../../archives/Wikimedia%20Commons/Ltluntil.svg)}@}                                                                                                                         |
| {@{_ψ_ __R__ _φ_}@}                          | {@{$$\psi \;{\mathcal {R} }\,\varphi$$}@} | {@{__R__<!-- markdown separator -->elease: _φ_ has to be true until and including the point where _ψ_ first becomes true; if _ψ_ never becomes true, _φ_ must remain true forever.}@} | {@{![LTI release diagram with release](../../archives/Wikimedia%20Commons/Ltlrelease-stop.svg) <p> ![LTI release diagram without release](../../archives/Wikimedia%20Commons/Ltlrelease-nostop.svg)}@} |
| {@{_ψ_ __W__ _φ_}@}                          | {@{$$\psi \;{\mathcal {W} }\,\varphi$$}@} | {@{__W__<!-- markdown separator -->eak until: _ψ_ has to hold _at least_ until _φ_<!-- markdown separator -->; if _φ_ never becomes true, _ψ_ must remain true forever.}@}            | {@{![LTI weak until diagram with until](../../archives/Wikimedia%20Commons/Ltluntil.svg) <p> ![LTI weak until diagram without until](../../archives/Wikimedia%20Commons/Ltlweakuntil2.svg)}@}          |
| {@{_ψ_ __M__ _φ_}@}                          | {@{$$\psi \;{\mathcal {M} }\,\varphi$$}@} | {@{Strong release: _φ_ has to be true until and including the point where _ψ_ first becomes true, which must hold at the current or a future position.}@}                             | {@{![LTI strong release diagram](../../archives/Wikimedia%20Commons/Ltlrelease-stop.svg)}@}                                                                                                         | <!--SR:!2025-03-16,79,343!2025-02-20,58,317!2025-02-26,63,310!2025-03-02,67,330!2025-09-06,206,330!2025-02-16,52,310!2025-03-02,67,330!2025-02-22,60,317!2025-03-18,80,343!2025-03-01,66,330!2025-02-28,65,330!2025-03-16,79,343!2025-03-15,78,343!2025-03-16,79,343!2025-03-15,78,343!2025-06-28,143,310!2025-03-15,78,343!2025-02-27,64,330!2025-02-22,57,323!2025-03-15,78,343!2025-03-01,66,330!2025-03-12,75,330!2025-02-21,59,317!2025-07-13,151,310!2025-03-16,79,343!2025-08-21,193,317!2025-03-16,79,343!2025-07-12,150,310-->

## equivalences

Let φ, ψ, and ρ be LTL formulas. The following tables list {@{some of the useful equivalences that extend standard equivalences among the usual logical operators}@}. <!--SR:!2025-02-22,57,323-->

| Distributivity                                                                                    |                                                                                                   |                                                                                                          |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| __X__ \(φ ∨ ψ\) ≡ \(<!-- markdown separator -->__X__ φ\) ∨ \(<!-- markdown separator -->__X__ ψ\) | __X__ \(φ ∧ ψ\) ≡ \(<!-- markdown separator -->__X__ φ\) ∧ \(<!-- markdown separator -->__X__ ψ\) | __X__ \(φ __U__ ψ\)≡ \(<!-- markdown separator -->__X__ φ\) __U__ \(<!-- markdown separator -->__X__ ψ\) |
| __F__ \(φ ∨ ψ\) ≡ \(<!-- markdown separator -->__F__ φ\) ∨ \(<!-- markdown separator -->__F__ ψ\) | __G__ \(φ ∧ ψ\) ≡ \(<!-- markdown separator -->__G__ φ\) ∧ \(<!-- markdown separator -->__G__ ψ\) |                                                                                                          |
| ρ __U__ \(φ ∨ ψ\) ≡ \(ρ __U__ φ\) ∨ \(ρ __U__ ψ\)                                                 | \(φ ∧ ψ\) __U__ ρ ≡ \(φ __U__ ρ\) ∧ \(ψ __U__ ρ\)                                                 |                                                                                                          |

> __flashcards__
>
> - next distributivity ::@:: __X__ \(φ ∨ ψ\) ≡ \(<!-- markdown separator -->__X__ φ\) ∨ \(<!-- markdown separator -->__X__ ψ\) <br/> __X__ \(φ ∧ ψ\) ≡ \(<!-- markdown separator -->__X__ φ\) ∧ \(<!-- markdown separator -->__X__ ψ\) <br/> __X__ \(φ __U__ ψ\)≡ \(<!-- markdown separator -->__X__ φ\) __U__ \(<!-- markdown separator -->__X__ ψ\) <!--SR:!2025-03-01,66,330!2025-03-10,73,330-->
> - finally and globally distributivity ::@:: __F__ \(φ ∨ ψ\) ≡ \(<!-- markdown separator -->__F__ φ\) ∨ \(<!-- markdown separator -->__F__ ψ\) <br/> __G__ \(φ ∧ ψ\) ≡ \(<!-- markdown separator -->__G__ φ\) ∧ \(<!-- markdown separator -->__G__ ψ\) <!--SR:!2025-05-30,127,297!2025-07-30,168,323-->
> - until distributivity ::@:: ρ __U__ \(φ ∨ ψ\) ≡ \(ρ __U__ φ\) ∨ \(ρ __U__ ψ\) <br/> \(φ ∧ ψ\) __U__ ρ ≡ \(φ __U__ ρ\) ∧ \(ψ __U__ ρ\) <!--SR:!2025-05-12,106,303!2025-04-29,99,290-->

| Negation propagation                            |                                                       |                                                       |                                                       |
| ----------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| _<!-- markdown separator -->__X__ is self-dual_ | _<!-- markdown separator -->__F__ and __G__ are dual_ | _<!-- markdown separator -->__U__ and __R__ are dual_ | _<!-- markdown separator -->__W__ and __M__ are dual_ |
| ¬<!-- markdown separator -->__X__ φ ≡ __X__ ¬φ  | ¬<!-- markdown separator -->__F__ φ ≡ __G__ ¬φ        | ¬ \(φ __U__ ψ\) ≡ \(¬φ __R__ ¬ψ\)                     | ¬ \(φ __W__ ψ\) ≡ \(¬φ __M__ ¬ψ\)                     |
|                                                 | ¬<!-- markdown separator -->__G__ φ ≡ __F__ ¬φ        | ¬ \(φ __R__ ψ\) ≡ \(¬φ __U__ ¬ψ\)                     | ¬ \(φ __M__ ψ\) ≡ \(¬φ __W__ ¬ψ\)                     |

> __flashcards__
>
> - _<!-- markdown separator -->__X__ is self-dual_ ::@:: ¬<!-- markdown separator -->__X__ φ ≡ __X__ ¬φ <!--SR:!2025-02-28,65,330!2025-02-21,59,317-->
> - _<!-- markdown separator -->__F__ and __G__ are dual_ ::@:: ¬<!-- markdown separator -->__F__ φ ≡ __G__ ¬φ <br/> ¬<!-- markdown separator -->__G__ φ ≡ __F__ ¬φ <!--SR:!2025-03-15,78,343!2025-03-02,67,330-->
> - _<!-- markdown separator -->__U__ and __R__ are dual_ ::@:: ¬ \(φ __U__ ψ\) ≡ \(¬φ __R__ ¬ψ\) <br/> ¬ \(φ __R__ ψ\) ≡ \(¬φ __U__ ¬ψ\) <!--SR:!2025-06-13,141,323!2025-02-20,58,310-->
> - _<!-- markdown separator -->__W__ and __M__ are dual_ ::@:: ¬ \(φ __W__ ψ\) ≡ \(¬φ __M__ ¬ψ\) <br/> ¬ \(φ __M__ ψ\) ≡ \(¬φ __W__ ¬ψ\) <!--SR:!2025-03-15,78,343!2025-03-10,73,330-->

| Special temporal properties                                                          |                                                                                      |                                                                        |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| __F__ φ ≡ __F__ __F__ φ                                                              | __G__ φ ≡ __G__ __G__ φ                                                              | φ __U__ ψ ≡ φ __U__ \(φ __U__ ψ\)                                      |
| φ __U__ ψ ≡ ψ ∨ \( φ ∧ __X__<!-- markdown separator -->\(φ __U__ ψ\) \)              | φ __W__ ψ ≡ ψ ∨ \( φ ∧ __X__<!-- markdown separator -->\(φ __W__ ψ\) \)              | φ __R__ ψ ≡ ψ ∧ \(φ ∨ __X__<!-- markdown separator -->\(φ __R__ ψ\) \) |
| __G__ φ ≡ φ ∧ __X__<!-- markdown separator -->\(<!-- markdown separator -->__G__ φ\) | __F__ φ ≡ φ ∨ __X__<!-- markdown separator -->\(<!-- markdown separator -->__F__ φ\) |                                                                        |

> __flashcards__
>
> - temporal idempotency ::@:: __F__ φ ≡ __F__ __F__ φ <br/> __G__ φ ≡ __G__ __G__ φ <br/> φ __U__ ψ ≡ φ __U__ \(φ __U__ ψ\) <!--SR:!2025-09-08,208,330!2025-05-08,103,290-->
> - temporal expansion ::@:: φ __U__ ψ ≡ ψ ∨ \( φ ∧ __X__<!-- markdown separator -->\(φ __U__ ψ\) \) <br/> φ __W__ ψ ≡ ψ ∨ \( φ ∧ __X__<!-- markdown separator -->\(φ __W__ ψ\) \) <br/> φ __R__ ψ ≡ ψ ∧ \(φ ∨ __X__<!-- markdown separator -->\(φ __R__ ψ\) \) <!--SR:!2025-05-26,117,303!2025-03-15,65,270-->

## negation normal form

All the formulas of LTL can be {@{transformed into _negation normal form_}@}, where <!--SR:!2025-03-16,79,343-->

- all negations ::@:: appear only in front of the atomic propositions, <!--SR:!2025-02-20,58,317!2025-03-08,72,330-->
- only other logical operators ::@:: __true__, __false__, ∧, and ∨ can appear, and <!--SR:!2025-02-27,64,317!2025-02-20,58,310-->
- only the temporal operators ::@:: __X__, __U__, and __R__ can appear. <!--SR:!2025-03-16,79,343!2025-03-15,78,343-->

{@{Using the above equivalences for negation propagation}@}, it is possible to {@{derive the normal form}@}. This normal form allows {@{__R__, __true__, __false__, and ∧ to appear in the formula, which are not fundamental operators of LTL}@}. Note that the transformation {@{to the negation normal form does not blow up the length of the formula}@}. This normal form is useful in {@{[translation from an LTL formula to a Büchi automaton](linear%20temporal%20logic%20to%20Büchi%20automaton.md)}@}. <!--SR:!2025-03-13,76,330!2025-02-21,59,317!2025-03-09,73,343!2025-03-02,67,330!2025-03-11,74,330-->

## relations with other logics

LTL can be shown to be {@{equivalent to the [monadic first-order logic of order](monadic%20predicate%20calculus.md), FO\[\<\]}@}—a result known as {@{[Kamp's theorem](Kamp's%20theorem.md)}@}—<sup>[\[9\]](#^ref-9)</sup> or {@{equivalently to [star-free languages](star-free%20language.md)}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-03-16,79,343!2025-03-16,79,343!2025-03-16,79,343-->

{@{[Computation tree logic](computation%20tree%20logic.md) \(CTL\) and linear temporal logic \(LTL\)}@} are {@{both a subset of [CTL\*](CTL*.md), but are incomparable}@}. For example, <!--SR:!2025-03-16,79,343!2025-03-07,71,330-->

- No formula in CTL ::@:: can define the language that is defined by the LTL formula __F__\(__G__ p\). <!--SR:!2025-02-18,53,310!2025-05-06,101,290-->
- No formula in LTL ::@:: can define the language that is defined by the CTL formulas __AG__\( p → \(__EX__<!-- markdown separator -->q ∧ __EX__<!-- markdown separator -->¬q\) \) or __AG__\(__EF__\(p\)\). <!--SR:!2025-03-07,58,257!2025-05-07,102,290-->

## computational problems

{@{[Model checking](model%20checking.md) and satisfiability against an LTL formula}@} are {@{[PSPACE-complete](PSPACE-complete.md) problems}@}. {@{LTL synthesis and the problem of verification of games against an LTL winning condition}@} is {@{[2EXPTIME-complete](2-EXPTIME.md)}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2025-06-25,137,297!2025-03-15,78,343!2025-02-14,19,283!2025-03-09,73,343-->

## applications

<!-- markdownlint-disable-next-line MD036 -->
__automata-theoretic linear temporal logic model checking__

LTL formulas are commonly used to {@{express constraints, specifications, or processes that a system should follow}@}. {@{The field of model checking}@} aims to {@{formally verify whether a system meets a given specification}@}. In the case of {@{automata-theoretic model checking}@}, {@{both the system of interest and a specification}@} are {@{expressed as separate [finite-state machines](finite-state%20machine.md), or automata}@}, and then {@{compared to evaluate whether the system is guaranteed to have the specified property}@}. In computer science, {@{this type of model checking}@} is often used to {@{verify that an algorithm is structured correctly}@}. <!--SR:!2025-09-07,207,330!2025-03-21,83,343!2025-02-21,59,317!2025-07-11,149,310!2025-03-15,78,343!2025-03-09,73,343!2025-03-15,78,343!2025-03-19,81,343!2025-02-22,60,317-->

To {@{check LTL specifications on infinite system runs}@}, a common technique is to {@{obtain a [Büchi automaton](Büchi%20automaton.md) that is equivalent to the model \(accepts an ω-word precisely if it is the model\)}@} and {@{another one that is equivalent to the negation of the property \(accepts an ω-word precisely it satisfies the negated property\)}@} \(cf. [linear temporal logic to Büchi automaton](linear%20temporal%20logic%20to%20Büchi%20automaton.md)\). In this case, if {@{there is an overlap in the set of ω-words accepted by the two automata}@}, it implies that {@{the model accepts some behaviors which violate the desired property}@}. If {@{there is no overlap, there are no property-violating behaviors which are accepted by the model}@}. Formally, {@{the intersection of the two non-deterministic Büchi automata is empty}@} {@{if and only if the model satisfies the specified property}@}.<sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-02-19,57,310!2025-03-10,74,343!2025-03-11,74,330!2025-09-05,205,330!2025-03-15,78,343!2025-02-22,60,317!2025-03-10,74,343!2025-03-16,79,343-->

<!-- markdownlint-disable-next-line MD036 -->
__expressing important properties in formal verification__

There are {@{two main types of properties that can be expressed using linear temporal logic}@}: {@{__[safety](safety%20and%20liveness%20properties.md)__ properties usually state that _something bad never happens_ \(__G__<!-- markdown separator -->¬<!-- markdown separator -->_ϕ_\)}@}, while {@{__[liveness](safety%20and%20liveness%20properties.md)__ properties state that _something good keeps happening_ \(__GF__<!-- markdown separator -->_ψ_ or __G__\(_ϕ_ →<!-- markdown separator -->__F__<!-- markdown separator -->_ψ_\)\)}@}.<sup>[\[13\]](#^ref-13)</sup> For example, a safety property may require that {@{an autonomous rover never drives over a cliff, or that a software product never allows a successful login with an incorrect password}@}. A liveness property may require that {@{the rover always continues to collect data samples, or that a software product repeatedly sends telemetry data}@}. <!--SR:!2025-03-18,80,343!2025-03-09,73,343!2025-03-15,78,343!2025-02-21,59,317!2025-03-10,74,343-->

More generally, safety properties are {@{those for which every [counterexample](counterexample.md) has a finite prefix such that, however it is extended to an infinite path, it is still a counterexample}@}. For liveness properties, on the other hand, {@{every finite path (that may not satisfy the formula yet) can be extended to an infinite path that satisfies the formula}@}. <!--SR:!2025-03-15,78,343!2025-02-21,59,317-->

<!-- markdownlint-disable-next-line MD036 -->
__specification language__

{@{One of the applications of linear temporal logic}@} is {@{the specification of [preferences](preference.md)}@} in {@{the [Planning Domain Definition Language](Planning%20Domain%20Definition%20Language.md)}@} for {@{the purpose of [preference-based planning](preference-based%20planning.md)}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> <!--SR:!2025-03-16,79,343!2025-03-02,67,330!2025-03-10,73,330!2025-03-12,75,330-->

## extensions

{@{Parametric linear temporal logic}@} extends LTL with {@{variables on the until-modality}@}.<sup>[\[14\]](#^ref-14)</sup> <!--SR:!2025-03-16,79,343!2025-02-22,60,317-->

## see also

> ![Wikimedia Commons](../../archives/Wikimedia%20Commons/Commons-logo.svg)
>
> Wikimedia Commons has media related to ___[Linear temporal logic](https://commons.wikimedia.org/wiki/Category:Linear%20temporal%20logic)___.

- [action language](action%20language.md)
- [metric temporal logic](metric%20temporal%20logic.md)
- [safety and liveness properties](safety%20and%20liveness%20properties.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/linear_temporal_logic) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Logic in Computer Science: Modelling and Reasoning about Systems](https://books.google.com/books?id=eUggAwAAQBAJ&q=%22temporal+logic%22): page 175 <a id="^ref-1"></a>^ref-1
2. ["Linear-time Temporal Logic"](https://web.archive.org/web/20170430084134/http://www-step.stanford.edu/tutorial/temporal-logic/temporal-logic.html). Archived from [the original](http://www-step.stanford.edu/tutorial/temporal-logic/temporal-logic.html) on 2017-04-30. Retrieved 2012-03-19. <a id="^ref-2"></a>^ref-2
3. [Dov M. Gabbay](Dov%20Gabbay.md); A. Kurucz; F. Wolter; M. Zakharyaschev \(2003\). [_Many-dimensional modal logics: theory and applications_](https://books.google.com/books?id=P8jZwiExZYEC&pg=PA46). Elsevier. p. 46. [ISBN](ISBN.md) [978-0-444-50826-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-444-50826-3). <a id="^ref-3"></a>^ref-3
4. Diekert, Volker. ["First-order Definable Languages"](http://www.lsv.fr/~gastin/Verif/DiekertGastin-FO-07.pdf) \(PDF\). University of Stuttgart. <a id="^ref-4"></a>^ref-4
5. [Kamp, Hans](Hans%20Kamp.md) \(1968\). _Tense Logic and the Theory of Linear Order_ \(PhD\). University of California Los Angeles. <a id="^ref-5"></a>^ref-5
6. [Amir Pnueli](Amir%20Pnueli.md), The temporal logic of programs. _Proceedings of the 18th Annual [Symposium on Foundations of Computer Science](Symposium%20on%20Foundations%20of%20Computer%20Science.md) \(FOCS\)_, 1977, 46–57. [doi](digital%20object%20identifier.md):[10.1109/SFCS.1977.32](https://doi.org/10.1109%2FSFCS.1977.32) <a id="^ref-6"></a>^ref-6
7. Sec. 5.1 of [Christel Baier](Christel%20Baier.md) and [Joost-Pieter Katoen](Joost-Pieter%20Katoen.md), _[Principles of Model Checking](Principles%20of%20Model%20Checking.md)_, MIT Press ["Principles of Model Checking - the MIT Press"](https://web.archive.org/web/20101204043002/http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=11481). Archived from [the original](http://mitpress.mit.edu/catalog/item/default.asp?tid%3D11481%26ttype%3D2) on 2010-12-04. Retrieved 2011-05-17. <a id="^ref-7"></a>^ref-7
8. Sec. 5.1.5 "Weak Until, Release, and Positive Normal Form" of Principles of Model Checking. <a id="^ref-8"></a>^ref-8
9. [Abramsky, Samson](Samson%20Abramsky.md); Gavoille, Cyril; Kirchner, Claude; Spirakis, Paul \(2010-06-30\). [_Automata, Languages and Programming: 37th International Colloquium, ICALP ... - Google Books_](https://books.google.com/books?id=TLpcI2axv8kC&pg=PA22). [ISBN](ISBN.md) [9783642141614](https://en.wikipedia.org/wiki/Special:BookSources/9783642141614). Retrieved 2014-07-30. <a id="^ref-9"></a>^ref-9
10. [Moshe Y. Vardi](Moshe%20Vardi.md) \(2008\). "From [Church](Alonzo%20Church.md) and Prior to [PSL](Property%20Specification%20Language.md)". In [Orna Grumberg](Orna%20Grumberg.md); [Helmut Veith](Helmut%20Veith.md) \(eds.\). _25 years of model checking: history, achievements, perspectives_. Springer. [ISBN](ISBN.md) [978-3-540-69849-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-69849-4). [preprint](http://www.cs.rice.edu/~vardi/papers/25mc.ps.gz) <a id="^ref-10"></a>^ref-10
11. A. Pnueli and R. Rosner. "On the synthesis of a reactive module" In Proceedings of the 16th ACM SIGPLAN-SIGACT [Symposium on Principles of programming languages](Symposium%20on%20Principles%20of%20Programming%20Languages.md) \(POPL '89\). Association for Computing Machinery, New York, NY, USA, 179–190. [https://doi.org/10.1145/75277.75293](https://doi.org/10.1145/75277.75293) <a id="^ref-11"></a>^ref-11
12. Moshe Y. Vardi. _An Automata-Theoretic Approach to Linear Temporal Logic._ Proceedings of the 8th Banff Higher Order Workshop \(Banff'94\). [Lecture Notes in Computer Science](Lecture%20Notes%20in%20Computer%20Science.md), vol. 1043, pp. 238–266, Springer-Verlag, 1996. [ISBN](ISBN.md) [3-540-60915-6](https://en.wikipedia.org/wiki/Special:BookSources/3-540-60915-6). <a id="^ref-12"></a>^ref-12
13. Bowen Alpern, [Fred B. Schneider](Fred%20B.%20Schneider.md), _Defining Liveness_, [Information Processing Letters](Information%20Processing%20Letters.md), Volume 21, Issue 4, 1985, Pages 181-185, ISSN 0020-0190, [https://doi.org/10.1016/0020-0190\(85\)90056-0](https://doi.org/10.1016/0020-0190(85)90056-0) <a id="^ref-13"></a>^ref-13
14. Chakraborty, Souymodip; Katoen, Joost-Pieter \(2014\). Diaz, Josep; Lanese, Ivan; Sangiorgi, Davide \(eds.\). "Parametric LTL on Markov Chains". _[Theoretical Computer Science](Theoretical%20Computer%20Science%20(journal).md)_. Lecture Notes in Computer Science. __7908__. Springer Berlin Heidelberg: 207–221. [arXiv](ArXiv.md):[1406.6683](https://arxiv.org/abs/1406.6683). [Bibcode](bibcode.md):[2014arXiv1406.6683C](https://ui.adsabs.harvard.edu/abs/2014arXiv1406.6683C). [doi](digital%20object%20identifier.md):[10.1007/978-3-662-44602-7\_17](https://doi.org/10.1007%2F978-3-662-44602-7_17). [ISBN](ISBN.md) [978-3-662-44602-7](https://en.wikipedia.org/wiki/Special:BookSources/978-3-662-44602-7). [S2CID](Semantic%20Scholar.md#S2CID) [12538495](https://api.semanticscholar.org/CorpusID:12538495). <a id="^ref-14"></a>^ref-14

## external links

- [A presentation of LTL](http://www.dcs.qmul.ac.uk/~pm/SaR/2004ltl.pdf)
- [Linear-Time Temporal Logic and Büchi Automata](http://www.cmi.ac.in/~madhavan/papers/pdf/isical97.pdf)
- [LTL Teaching slides](http://www.inf.unibz.it/~artale/FM/slide3.pdf) of professor [Alessandro Artale](Alessandro%20Artale.md) at the [Free University of Bozen-Bolzano](Free%20University%20of%20Bozen-Bolzano.md)
- [LTL to Buchi translation algorithms](https://web.archive.org/web/20090830133455/http://spot.lip6.fr/wiki/LtlTranslationAlgorithms) a genealogy, from the website of [Spot](http://spot.lip6.fr/) a library for model checking.
