---
aliases:
  - mathematical induction
  - mathematical inductions
  - mathematics induction
  - mathematics inductions
tags:
  - flashcard/active/general/mathematical_induction
  - language/in/English
---

# mathematical induction

- Not to be confused with {{[inductive reasoning](inductive%20reasoning.md)}}. <!--SR:!2024-10-29,14,290-->

__Mathematical induction__ is {{a method for [proving](mathematical%20proof.md) that a statement $P(n)$ is true for every [natural number](natural%20number.md) $n$}}, that is, that {{the infinitely many cases $P(0),P(1),P(2),P(3),\dots$ all hold}}. This is done by {{first proving a simple case, then also showing that if we assume the claim is true for a given case, then the next case is also true}}. Informal metaphors help to explain this technique, such as {{falling dominoes or climbing a ladder}}: <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290-->

> Mathematical induction proves that {{we can climb as high as we like on a ladder}}, by proving that {{we can climb onto the bottom rung (the __basis__) and that from each rung we can climb up to the next one (the __step__)}}.
>
> — _[Concrete Mathematics](Concrete%20Mathematics.md)_, page 3 margins. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

A __proof by induction__ consists of {{two cases}}. The first, {{the __base case__, proves the statement for $n=0$ without assuming any knowledge of other cases}}. The second case, {{the __induction step__, proves that _if_ the statement holds for any given case $n=k$, _then_ it must also hold for the next case $n=k+1$}}. These two steps establish that {{the statement holds for every natural number $n$}}. The base case does not {{necessarily begin with $n=0$, but often with $n=1$, and possibly with any fixed natural number $n=N$}}, establishing {{the truth of the statement for all natural numbers $n\geq N$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290!2024-10-29,14,290-->

The method can be extended to {{prove statements about more general [well-founded](well-founded%20relation.md) structures, such as [trees](tree%20(set%20theory).md)}}; this generalization, known as {{[structural induction](structural%20induction.md), is used in [mathematical logic](mathematical%20logic.md) and [computer science](computer%20science.md)}}. Mathematical induction in this extended sense is closely related to {{[recursion](recursion.md)}}. Mathematical induction is {{an [inference rule](rule%20of%20inference.md) used in [formal proofs](formal%20proof.md)}}, and is the foundation of {{most [correctness](correctness%20(computer%20science).md) proofs for computer programs}}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2024-12-03,38,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

Despite its name, mathematical induction differs fundamentally from {{[inductive reasoning](inductive%20reasoning.md) as [used in philosophy](problem%20of%20induction.md), in which the examination of many cases results in a probable conclusion}}. The mathematical method {{examines infinitely many cases to prove a general statement, but it does so by a finite chain of [deductive reasoning](deductive%20reasoning.md) involving the [variable](variable%20(mathematics).md) $n$, which can take infinitely many values}}. The result is {{a rigorous proof of the statement, not an assertion of its probability}}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

## history

In 370 BC, [Plato](plato.md)'s [Parmenides](parmenides%20(dialogue).md) may have contained traces of an early example of an implicit inductive proof,<sup>[\[5\]](#^ref-5)</sup> however, the earliest implicit proof by mathematical induction was written by [al-Karaji](Al-Karaji.md) around 1000 AD, who applied it to [arithmetic sequences](arithmetic%20progression.md) to prove the [binomial theorem](binomial%20theorem.md) and properties of [Pascal's triangle](pascal's%20triangle.md). Whilst the original work was lost, it was later referenced by [Al-Samawal al-Maghribi](Al-Samawal%20al-Maghribi.md) in his treatise _al-Bahir fi'l-jabr (The Brilliant in Algebra)_ in around 1150 AD.<sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup>

Katz says in his history of mathematics

> Another important idea introduced by al-Karaji and continued by al-Samaw'al and others was that of an inductive argument for dealing with certain arithmetic sequences. Thus al-Karaji used such an argument to prove the result on the sums of integral cubes already known to [Aryabhata](aryabhata.md) [...] Al-Karaji did not, however, state a general result for arbitrary _n_. He stated his theorem for the particular integer 10 [...] His proof, nevertheless, was clearly designed to be extendable to any other integer. [...] Al-Karaji's argument includes in essence the two basic components of a modern argument by induction, namely the [truth](truth.md) of the statement for _n_ = 1 (1 = 1<sup>3</sup>) and the deriving of the truth for _n_ = _k_ from that of _n_ = _k_ - 1. Of course, this second component is not explicit since, in some sense, al-Karaji's argument is in reverse; this is, he starts from _n_ = 10 and goes down to 1 rather than proceeding upward. Nevertheless, his argument in _al-Fakhri_ is the earliest extant proof of [the sum formula for integral cubes](squared%20triangular%20number.md).<sup>[\[8\]](#^ref-8)</sup>

In India, early implicit proofs by mathematical induction appear in [Bhaskara](Bhāskara%20II.md)'s "[cyclic method](chakravala%20method.md)".<sup>[\[9\]](#^ref-9)</sup>

None of these ancient mathematicians, however, explicitly stated the induction hypothesis. Another similar case (contrary to what Vacca has written, as Freudenthal carefully showed)<sup>[\[10\]](#^ref-10)</sup> was that of [Francesco Maurolico](Francesco%20Maurolico.md) in his _Arithmeticorum libri duo_ (1575), who used the technique to prove that the sum of the first _n_ [odd](parity%20(mathematics).md) [integers](integer.md) is _n_<sup>2</sup>.

The earliest [rigorous](rigour.md#mathematical%20proof) use of induction was by [Gersonides](gersonides.md) (1288–1344).<sup>[\[11\]](#^ref-11)</sup><sup>[\[12\]](#^ref-12)</sup> The first explicit formulation of the principle of induction was given by [Pascal](Blaise%20Pascal.md) in his _Traité du triangle arithmétique_ (1665). Another Frenchman, [Fermat](Pierre%20de%20Fermat.md), made ample use of a related principle: indirect proof by [infinite descent](proof%20by%20infinite%20descent.md).

The induction hypothesis was also employed by the Swiss [Jakob Bernoulli](Jacob%20Bernoulli.md), and from then on it became well known. The modern formal treatment of the principle came only in the 19th century, with [George Boole](George%20Boole.md),<sup>[\[13\]](#^ref-13)</sup> [Augustus De Morgan](Augustus%20De%20Morgan.md), [Charles Sanders Peirce](Charles%20Sanders%20Peirce.md),<sup>[\[14\]](#^ref-14)</sup><sup>[\[15\]](#^ref-15)</sup> [Giuseppe Peano](Giuseppe%20Peano.md), and [Richard Dedekind](Richard%20Dedekind.md).<sup>[\[9\]](#^ref-9)</sup>

## description

The simplest and most common form of mathematical induction infers that {{a statement involving a [natural number](natural%20number.md) _n_ (that is, an integer _n_ ≥ 0 or 1) holds for all values of _n_}}. The proof consists of two steps: <!--SR:!2024-10-29,14,290-->

1. The __base case__ (or __initial case__) ::: prove that the statement holds for 0, or 1. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->
2. The __induction step__ (or __inductive step__, or __step case__) ::: prove that for every _n_, if the statement holds for _n_, then it holds for _n_ + 1. In other words, assume that the statement holds for some arbitrary natural number _n_, and prove that the statement holds for _n_ + 1. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

{{The hypothesis in the induction step, that the statement holds for a particular _n_}}, is called {{the __induction hypothesis__ or __inductive hypothesis__}}. To prove the induction step, one {{assumes the induction hypothesis for _n_ and then uses this assumption to prove that the statement holds for _n_ + 1}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

Authors who prefer to define natural numbers to begin at 0 use that value in the base case; those who define natural numbers to begin at 1 use that value.

## examples

### sum of consecutive natural numbers

Mathematical induction can be used to prove the following statement _P_(_n_) for all natural numbers _n_: {{$$P(n)\!:\ \ 0+1+2+\cdots +n={\frac {n(n+1)}{2} }$$}} <!--SR:!2024-10-29,14,290-->

This states {{a general formula for the sum of the natural numbers less than or equal to a given number; in fact an infinite sequence of statements}}: {{$0={\tfrac {(0)(0+1)}{2} }$, $0+1={\tfrac {(1)(1+1)}{2} }$, $0+1+2={\tfrac {(2)(2+1)}{2} }$, etc.}} <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

__<u>Proposition.</u>__ ::: For every $n\in \mathbb {N}$, $0+1+2+\cdots +n={\tfrac {n(n+1)}{2} }$. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

__Proof.__ ::: Let _P_(_n_) be the statement $0+1+2+\cdots +n={\tfrac {n(n+1)}{2} }$. We give a proof by induction on _n_. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Base case_ ::: Show that the statement holds for the smallest natural number _n_ = 0. _P_(0) is clearly true: $0={\tfrac {0(0+1)}{2} }$. <!--SR:!2024-10-29,14,290!2024-12-03,38,290-->

_Induction step_ ::: Show that for every _k_ ≥ 0, if _P_(_k_) holds, then _P_(_k_ + 1) also holds. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

Assume the induction hypothesis that for a particular _k_, the single case _n_ = _k_ holds, meaning _P_(_k_) is true: $$0+1+\cdots +k={\frac {k(k+1)}{2} }.$$ It follows that: $$(0+1+2+\cdots +k)+(k+1)={\frac {k(k+1)}{2} }+(k+1).$$

[Algebraically](algebra.md), the right hand side simplifies as: $${\begin{aligned}{\frac {k(k+1)}{2} }+(k+1)&={\frac {k(k+1)+2(k+1)}{2} }\\&={\frac {(k+1)(k+2)}{2} }\\&={\frac {(k+1)((k+1)+1)}{2} }.\end{aligned} }$$

Equating the extreme left hand and right hand sides, we deduce that: $$0+1+2+\cdots +k+(k+1)={\frac {(k+1)((k+1)+1)}{2} }.$$ That is, the statement _P_(_k_ + 1) also holds true, establishing the induction step.

_Conclusion_ ::: Since both the base case and the induction step have been proved as true, by mathematical induction the statement _P_(_n_) holds for every natural number _n_. [Q.E.D.](Q.E.D..md) <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

### a trigonometric inequality

Induction is often used to {{prove [inequalities](inequality%20(mathematics).md)}}. As an example, we prove that {{$\left|\sin nx\right|\leq n\left|\sin x\right|$ for any [real number](real%20number.md) $x$ and natural number $n$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

At first glance, it may appear that {{a more general version, $\left|\sin nx\right|\leq n\left|\sin x\right|$ for any _real_ numbers $n,x$, could be proven without induction}}; but {{the case $n={\frac {1}{2} },\,x=\pi$ shows it may be false for non-integer values of $n$}}. This suggests {{we examine the statement specifically for _natural_ values of $n$, and induction is the readiest tool}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

__<u>Proposition.</u>__ ::: For any $x\in \mathbb {R}$ and $n\in \mathbb {N}$, $\left|\sin nx\right|\leq n\left|\sin x\right|$. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

__Proof.__ ::: Fix an arbitrary real number $x$, and let $P(n)$ be the statement $\left|\sin nx\right|\leq n\left|\sin x\right|$. We induce on $n$. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Base case_ ::: The calculation $\left|\sin 0x\right|=0\leq 0=0\left|\sin x\right|$ verifies $P(0)$. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Induction step_ ::: We show the [implication](logical%20consequence.md) $P(k)\implies P(k+1)$ for any natural number $k$. Assume the induction hypothesis: for a given value $n=k\geq 0$, the single case $P(k)$ is true. Using the [angle addition formula](list%20of%20trigonometric%20identities.md) and the [triangle inequality](absolute%20value.md#real%20numbers), we deduce: $${\begin{aligned}\left|\sin(k+1)x\right|&=\left|\sin kx\cos x+\sin x\cos kx\right|&&{\text{(angle addition)} }\\&\leq \left|\sin kx\cos x\right|+\left|\sin x\,\cos kx\right|&&{\text{(triangle inequality)} }\\&=\left|\sin kx\right|\left|\cos x\right|+\left|\sin x\right|\left|\cos kx\right|\\&\leq \left|\sin kx\right|+\left|\sin x\right|&&(\left|\cos t\right|\leq 1)\\&\leq k\left|\sin x\right|+\left|\sin x\right|&&{\text{(induction hypothesis)} }\\&=(k+1)\left|\sin x\right|.\end{aligned} }$$ <p> The inequality between the extreme left-hand and right-hand quantities shows that $P(k+1)$ is true, which completes the induction step. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Conclusion_ ::: The proposition $P(n)$ holds for all natural numbers $n$.  Q.E.D. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

## variants

In practice, proofs by induction are often {{structured differently, depending on the exact nature of the property to be proven}}. All variants of induction are {{special cases of [transfinite induction](transfinite%20induction.md)}}; see [below](#transfinite%20induction). <!--SR:!2024-12-03,38,290!2024-10-29,14,290-->

### base case other than 0 or 1

If {{one wishes to prove a statement, not for all natural numbers, but only for all numbers _n_ greater than or equal to a certain number _b_}}, then the proof by induction consists of the following: <!--SR:!2024-10-29,14,290-->

1. Showing that the statement holds when _n_ = _b_.
2. Showing that if the statement holds for an arbitrary number _n_ ≥ _b_, then the same statement also holds for _n_ + 1.

This can be used, for example, to show that 2<sup>_n_</sup> ≥ _n_ + 5 for _n_ ≥ 3.

In this way, one can prove that some statement _P_(_n_) holds for {{all _n_ ≥ 1, or even for all _n_ ≥ −5}}. This form of mathematical induction is {{actually a special case of the previous form}}, because if {{the statement to be proved is _P_(_n_)}} then {{proving it with these two rules is equivalent with proving _P_(_n_ + _b_) for all natural numbers _n_ with an induction base case 0}}.<sup>[\[16\]](#^ref-16)</sup> <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

#### example: forming dollar amounts by coins

Assume {{an infinite supply of 4- and 5-dollar coins}}. Induction can be used to prove that {{any whole amount of dollars greater than or equal to 12 can be formed by a combination of such coins}}. Let _S_(_k_) denote the statement "_k_ dollars can be formed by a combination of 4- and 5-dollar coins". The proof that _S_(_k_) is true for all _k_ ≥ 12 can then be achieved by induction on _k_ as follows: <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Base case_ ::: Showing that _S_(_k_) holds for _k_ = 12 is simple: take three 4-dollar coins. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Induction step_ ::: Given that _S_(_k_) holds for some value of _k_ ≥ 12 (_induction hypothesis_), prove that _S_(_k_ + 1) holds, too. Assume _S_(_k_) is true for some arbitrary _k_ ≥ 12. If there is a solution for _k_ dollars that includes at least one 4-dollar coin, replace it by a 5-dollar coin to make _k_ + 1 dollars. Otherwise, if only 5-dollar coins are used, _k_ must be a multiple of 5 and so at least 15; but then we can replace three 5-dollar coins by four 4-dollar coins to make _k_ + 1 dollars. In each case, _S_(_k_ + 1) is true. <p> Therefore, by the principle of induction, _S_(_k_) holds for all _k_ ≥ 12, and the proof is complete. <!--SR:!2024-11-21,26,270!2024-10-29,14,290-->

In this example, although {{_S_(_k_) also holds for $k\in \{4,5,8,9,10\}$}}, the above proof {{cannot be modified to replace the minimum amount of 12 dollar to any lower value _m_}}. For _m_ = 11, {{the base case is actually false}}; for _m_ = 10, {{the second case in the induction step (replacing three 5- by four 4-dollar coins)}} will not work; let alone for even lower _m_. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

### induction on more than one counter

It is sometimes desirable to prove {{a statement involving two natural numbers, _n_ and _m_, by iterating the induction process}}. That is, {{one proves a base case and an induction step for _n_, and in each of those proves a base case and an induction step for _m_}}. See, for example, the [proof of commutativity](proofs%20involving%20the%20addition%20of%20natural%20numbers.md) accompanying _[addition of natural numbers](addition.md#natural%20numbers)_. More complicated arguments involving three or more counters are also possible. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

### infinite descent

- see: [infinite descent](proof%20by%20infinite%20descent.md)

The method of infinite descent is {{a variation of mathematical induction which was used by [Pierre de Fermat](Pierre%20de%20Fermat.md)}}. It is used to show that {{some statement _Q_(_n_) is false for all natural numbers _n_}}. Its traditional form consists of {{showing that if _Q_(_n_) is true for some natural number _n_, it also holds for some strictly smaller natural number _m_}}. Because {{there are no infinite decreasing sequences of natural numbers}}, this situation would be impossible, thereby {{showing ([by contradiction](proof%20by%20contradiction.md)) that _Q_(_n_) cannot be true for any _n_}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

The validity of this method can be {{verified from the usual principle of mathematical induction}}. Using mathematical induction on {{the statement _P_(_n_) defined as "_Q_(_m_) is false for all natural numbers _m_ less than or equal to _n_"}}, it follows that {{_P_(_n_) holds for all _n_}}, which means that {{_Q_(_n_) is false for every natural number _n_}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

### limited mathematical induction

If one wishes to prove that {{a property _P_ holds for all natural numbers less than or equal to _n_}}, proving _P_ satisfies the following conditions suffices:<sup>[\[17\]](#^ref-17)</sup> <!--SR:!2024-10-29,14,290-->

1. _P_ holds for 0,
2. For any natural number _x_ less than _n_, if _P_ holds for _x_, then _P_ holds for _x_ + 1

### prefix induction

The most common form of proof by mathematical induction requires {{proving in the induction step that $$\forall k\,(P(k)\to P(k+1)).$$}} <!--SR:!2024-10-29,14,290-->

whereupon the induction principle {{"automates" _n_ applications of this step in getting from _P_(0) to _P_(_n_)}}. This could be called {{"predecessor induction"}} because {{each step proves something about a number from something about that number's predecessor}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290-->

A variant of {{interest in [computational complexity](computational%20complexity.md)}} is {{"prefix induction"}}, in which one {{proves the following statement in the induction step: $$\forall k\,(P(k)\to P(2k)\land P(2k+1))$$ or equivalently $$\forall k\,\left(P\!\left(\left\lfloor {\frac {k}{2} }\right\rfloor \right)\to P(k)\right).$$}} <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290-->

The induction principle then {{"automates" [log<sub>2</sub>](binary%20logarithm.md) _n_ applications of this inference in getting from _P_(0) to _P_(_n_)}}. In fact, it is called "prefix induction" because {{each step proves something about a number from something about the "prefix" of that number}} — as formed by {{truncating the low bit of its [binary representation](binary%20number.md)}}. It can also be viewed as {{an application of traditional induction on the length of that binary representation}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

If {{traditional predecessor induction is interpreted computationally as an _n_-step loop}}, then prefix induction would {{correspond to a log-_n_-step loop}}. Because of that, proofs using prefix induction are {{"more feasibly constructive" than proofs using predecessor induction}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

Predecessor induction can {{trivially simulate prefix induction on the same statement}}. Prefix induction can {{simulate predecessor induction, but only at the cost of making the statement more syntactically complex (adding a [bounded](bounded%20quantifier.md) [universal quantifier](universal%20quantification.md))}}, so the interesting results {{relating prefix induction to [polynomial-time](time%20complexity.md#polynomial%20time) computation}} depend on {{excluding unbounded quantifiers entirely, and limiting the alternation of bounded universal and [existential](existential%20quantification.md) quantifiers allowed in the statement}}.<sup>[\[18\]](#^ref-18)</sup> <!--SR:!2024-10-29,14,290!2024-11-21,26,270!2024-10-29,14,290!2024-11-21,26,270-->

One can take the idea a step further: {{one must prove $$\forall k\,\left(P\!\left(\left\lfloor {\sqrt {k} }\right\rfloor \right)\to P(k)\right)$$}} whereupon the induction principle {{"automates" log log _n_ applications of this inference in getting from _P_(0) to _P_(_n_)}}. This form of induction has been used, {{analogously, to study log-time parallel computation}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

### complete (strong) induction

Another variant, called {{__complete induction__, __course of values induction__ or __strong induction__ (in contrast to which the basic form of induction is sometimes known as __weak induction__)}}, makes {{the induction step easier to prove by using a stronger hypothesis}}: one proves {{the statement $P(m+1)$ under the assumption that $P(n)$ holds for _all_ natural numbers $n$ less than $m+1$; by contrast, the basic form only assumes $P(m)$}}. The name "strong induction" {{does not mean that this method can prove more than "weak induction", but merely refers to the stronger hypothesis used in the induction step}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-11-21,26,270-->

In fact, it can be shown that {{the two methods are actually equivalent, as explained below}}. In this form of complete induction, one still has to {{prove the base case, $P(0)$, and it may even be necessary to prove extra-base cases such as $P(1)$ before the general argument applies}}, as {{in the example below of the [Fibonacci number](Fibonacci%20sequence.md) $F_{n}$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

Although {{the form just described requires one to prove the base case}}, this is {{unnecessary if one can prove $P(m)$ (assuming $P(n)$ for all lower $n$) for all $m\geq 0$}}. This is {{a special case of [transfinite induction](#transfinite%20induction) as described below, although it is no longer equivalent to ordinary induction}}. In this form {{the base case is subsumed by the case $m=0$, where $P(0)$ is proved with no other $P(n)$ assumed}}; this case may {{need to be handled separately, but sometimes the same argument applies for $m=0$ and $m>0$, making the proof simpler and more elegant}}. In this method, however, it is vital to {{ensure that the proof of $P(m)$ does not implicitly assume that $m>0$}}, e.g. {{by saying "choose an arbitrary $n<m$", or by assuming that a set of _m_ elements has an element}}. <!--SR:!2024-12-03,38,290!2024-11-21,26,270!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

#### equivalence with ordinary induction

Complete induction is {{equivalent to ordinary mathematical induction as described above, in the sense that a proof by one method can be transformed into a proof by the other}}. Suppose {{there is a proof of $P(n)$ by complete induction}}. Then, this proof {{can be transformed into an ordinary induction proof by assuming a stronger inductive hypothesis}}. Let $Q(n)$ be {{the statement "$P(m)$ holds for all $m$ such that $0\leq m\leq n$"}}—this {{becomes the inductive hypothesis for ordinary induction}}. We can then show {{$Q(0)$ and $Q(n+1)$ for $n\in \mathbb {N}$ assuming only $Q(n)$}} and show that {{$Q(n)$ implies $P(n)$}}.<sup>[\[19\]](#^ref-19)</sup> <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-11-21,26,270!2024-10-29,14,290-->

If, {{on the other hand, $P(n)$ had been proven by ordinary induction}}, the proof would {{already effectively be one by complete induction}}: $P(0)$ is {{proved in the base case, using no assumptions}}, and $P(n+1)$ is {{proved in the induction step, in which one may assume all earlier cases but need only use the case $P(n)$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

#### example: Fibonacci numbers

Complete induction is most useful when {{several instances of the inductive hypothesis are required for each induction step}}. For example, complete induction can be used to show that {{$F_{n}={\frac {\varphi ^{n}-\psi ^{n} }{\varphi -\psi } }$ where $F_{n}$ is the _n_-th [Fibonacci number](Fibonacci%20sequence.md)}}, and {{$\varphi ={\frac {1}{2} }(1+{\sqrt {5} })$ (the [golden ratio](golden%20ratio.md)) and $\psi ={\frac {1}{2} }(1-{\sqrt {5} })$ are the [roots](zero%20of%20a%20function.md) of the [polynomial](polynomial.md) $x^{2}-x-1$}}. By using the fact that {{$F_{n+2}=F_{n+1}+F_{n}$ for each $n\in \mathbb {N}$}}, the identity above can be verified by {{direct calculation for $F_{n+2}$ if one assumes that it already holds for both $F_{n+1}$ and $F_{n}$}}. To complete the proof, the identity {{must be verified in the two base cases: $n=0$ and $n=1$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

#### example: prime factorization

Another proof by complete induction uses {{the hypothesis that the statement holds for _all_ smaller $n$ more thoroughly}}. Consider the statement that {{"every [natural number](natural%20number.md) greater than 1 is a product of (one or more) [prime numbers](prime%20number.md)"}}, which is {{the "[existence](fundamental%20theorem%20of%20arithmetic.md#existence)" part of the [fundamental theorem of arithmetic](fundamental%20theorem%20of%20arithmetic.md)}}. For proving the induction step, the induction hypothesis is that {{for a given $n>1$ the statement holds for all smaller $n>1$}}. If {{$m$ is prime then it is certainly a product of primes}}, and if not, then {{by definition it is a product: $m=n_{1}n_{2}$, where neither of the factors is equal to 1}}; hence {{neither is equal to $m$, and so both are greater than 1 and smaller than $m$}}. The induction hypothesis {{now applies to $n_{1}$ and $n_{2}$, so each one is a product of primes}}. Thus {{$m$ is a product of products of primes, and hence by extension a product of primes itself}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290-->

#### example: dollar amounts revisited

We shall look to prove the same example as [above](#example%20forming%20dollar%20amounts%20by%20coins), this time with _strong induction_. The statement remains the same: {{$$S(n):\,\,n\geq 12\implies \,\exists \,a,b\in \mathbb {N} .\,\,n=4a+5b$$}} <!--SR:!2024-10-29,14,290-->

However, there will be slight differences in {{the structure and the assumptions of the proof, starting with the extended base case}}. <!--SR:!2024-10-29,14,290-->

__Proof.__

_Base case_ ::: Show that $S(k)$ holds for $k=12,13,14,15$. $${\begin{aligned}4\cdot 3+5\cdot 0=12\\4\cdot 2+5\cdot 1=13\\4\cdot 1+5\cdot 2=14\\4\cdot 0+5\cdot 3=15\end{aligned} }$$ <p> The base case holds. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Induction step_ ::: Given some $j>15$, assume $S(m)$ holds for all $m$ with $12\leq m<j$. Prove that $S(j)$ holds. <p> Choosing $m=j-4$, and observing that $15<j\implies 12\leq j-4<j$ shows that $S(j-4)$ holds, by the inductive hypothesis. That is, the sum $j-4$ can be formed by some combination of $4$ and $5$ dollar coins. Then, simply adding a $4$ dollar coin to that combination yields the sum $j$. That is, $S(j)$ holds<sup>[\[20\]](#^ref-20)</sup> Q.E.D. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

### forward-backward induction

- see: [forward-backward induction](AM–GM%20inequality.md#proof%20by%20Cauchy%20using%20forward%E2%80%93backward%20induction)

Sometimes, it is {{more convenient to deduce backwards, proving the statement for $n-1$, given its validity for $n$}}. However, {{proving the validity of the statement for no single number suffices to establish the base case; instead, one needs to prove the statement for an infinite subset of the natural numbers}}. For example, {{[Augustin Louis Cauchy](Augustin-Louis%20Cauchy.md)}} first used {{forward (regular) induction to prove the [inequality of arithmetic and geometric means](AM–GM%20inequality.md#proof%20by%20Cauchy%20using%20forward%E2%80%93backward%20induction) for all [powers of 2](power%20of%20two.md)}}, and then {{used backwards induction to show it for all natural numbers}}.<sup>[\[21\]](#^ref-21)</sup><sup>[\[22\]](#^ref-22)</sup> <!--SR:!2024-12-03,38,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290-->

## example of error in the induction step

- see: [all horses are the same color](all%20horses%20are%20the%20same%20color.md)

The induction step {{must be proved for all values of _n_}}. To illustrate this, {{Joel E. Cohen}} proposed the following argument, which purports to {{prove by mathematical induction that [all horses are of the same color](all%20horses%20are%20the%20same%20color.md)}}:<sup>[\[23\]](#^ref-23)</sup> <!--SR:!2024-10-29,14,290!2024-11-21,26,270!2024-10-29,14,290-->

_Base case_ ::: in a set of only _one_ horse, there is only one color. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

_Induction step_ ::: assume as induction hypothesis that within any set of $n$ horses, there is only one color. Now look at any set of $n+1$ horses. Number them: $1,2,3,\dotsc ,n,n+1$. Consider the sets $\left\{1,2,3,\dotsc ,n\right\}$ and $\left\{2,3,4,\dotsc ,n+1\right\}$. Each is a set of only $n$ horses, therefore within each there is only one color. But the two sets overlap, so there must be only one color among all $n+1$ horses. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

The base case $n=1$ is {{trivial, and the induction step is correct in all cases $n>1$}}. However, the argument used in the induction step is {{incorrect for $n+1=2$, because the statement that "the two sets overlap" is false for $\left\{1\right\}$ and $\left\{2\right\}$}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

## formalization

In {{__[second-order logic](second-order%20logic.md)__}}, one can {{write down the "[axiom](axiom.md) of induction" as follows}}: {{$$\forall P\,{\Bigl (}P(0)\land \forall k{\bigl (}P(k)\to P(k+1){\bigr )}\to \forall n\,{\bigl (}P(n){\bigr )}{\Bigr )},$$}} where {{_P_(·) is a variable for predicates involving one natural number and _k_ and _n_ are variables for [natural numbers](natural%20number.md)}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

In words, {{the base case _P_(0) and the induction step (namely, that the induction hypothesis _P_(_k_) implies _P_(_k_ + 1)) together}} imply that {{_P_(_n_) for any natural number _n_}}. The axiom of induction {{asserts the validity of inferring that _P_(_n_) holds for any natural number _n_ from the base case and the induction step}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

The first quantifier in the axiom {{ranges over _predicates_ rather than over individual numbers}}. This is {{a second-order quantifier, which means that this axiom is stated in [second-order logic](second-order%20logic.md)}}. {{Axiomatizing arithmetic induction in [first-order logic](first-order%20logic.md)}} requires {{an [axiom schema](axiom%20schema.md) containing a separate axiom for each possible predicate}}. The article [Peano axioms](Peano%20axioms.md) contains further discussion of this issue. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

The axiom of structural induction for the natural numbers was first formulated by {{Peano}}, who {{used it to specify the natural numbers together with the following four other axioms}}: <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

1. 0 is a natural number.
2. The successor function _s_ of every natural number yields a natural number (_s_(_x_) = _x_ + 1).
3. The successor function is [injective](injective%20function.md).
4. 0 is not in the [range](range%20of%20a%20function.md) of _s_.

In {{__[first-order](first-order%20logic.md) [ZFC set theory](Zermelo–Fraenkel%20set%20theory.md)__}}, {{quantification over predicates is not allowed}}, but {{one can still express induction by quantification over sets}}: {{$$\forall A{\Bigl (}0\in A\land \forall k\in \mathbb {N} {\bigl (}k\in A\to (k+1)\in A{\bigr )}\to \mathbb {N} \subseteq A{\Bigr )}.$$}} _A_ may be read as {{a set representing a proposition, and containing natural numbers, for which the proposition holds}}. This is {{not an axiom, but a theorem, given that natural numbers are defined in the language of ZFC set theory by axioms, analogous to Peano's}}. See [construction of the natural numbers](axiom%20of%20infinity.md#alternative%20method) using the [axiom of infinity](axiom%20of%20infinity.md) and [axiom schema of specification](axiom%20schema%20of%20specification.md). <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290-->

## transfinite induction

- see: [transfinite induction](transfinite%20induction.md)

One variation of the principle of complete induction can be {{generalized for statements about elements of any [well-founded set](well-founded%20relation.md)}}, that is, {{a set with an [irreflexive relation](reflexive%20relation.md) < that contains no [infinite descending chains](total%20order.md#chains)}}. {{Every set representing an [ordinal number](ordinal%20number.md)}} is well-founded, {{the set of natural numbers}} is one of them. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-12-03,38,290!2024-10-29,14,290-->

Applied to {{a well-founded set}}, transfinite induction can be {{formulated as a single step}}. To prove that a statement _P_(_n_) holds for each ordinal number: <p> {{Show, for each ordinal number _n_, that if _P_(_m_) holds for all _m_ < _n_, then _P_(_n_) also holds.}} <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

This form of induction, when {{applied to a set of ordinal numbers (which form a [well-ordered](well-order.md) and hence well-founded [class](class%20(set%20theory).md))}}, is called _[transfinite induction](transfinite%20induction.md)_. It is {{an important proof technique in [set theory](set%20theory.md), [topology](topology.md) and other fields}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

Proofs by transfinite induction typically {{distinguish three cases}}: <!--SR:!2024-10-29,14,290-->

1. when _n_ is a minimal element, ... ::: ... i.e. there is no element smaller than _n_; <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->
2. when _n_ has a direct predecessor, ... ::: ... i.e. the set of elements which are smaller than _n_ has a largest element; <!--SR:!2024-11-21,25,270!2024-10-29,14,290-->
3. when _n_ has no direct predecessor, ... ::: ... i.e. _n_ is a so-called [limit ordinal](limit%20ordinal.md). <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

Strictly speaking, it is {{not necessary in transfinite induction to prove a base case}}, because {{it is a [vacuous](vacuous%20truth.md) special case of the proposition that if _P_ is true of all _n_ < _m_, then _P_ is true of _m_}}. It is vacuously true precisely because {{there are no values of _n_ < _m_ that could serve as counterexamples}}. So the special cases are special cases of the general case. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

## relationship to the well-ordering principle

The principle of mathematical induction is usually stated as {{an [axiom](axiom.md) of the natural numbers; see [Peano axioms](Peano%20axioms.md)}}. It is strictly stronger than {{the [well-ordering principle](well-ordering%20principle.md) in the context of the other Peano axioms}}. Suppose the following: <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

- The [trichotomy](law%20of%20trichotomy.md) axiom ::: For any natural numbers _n_ and _m_, _n_ is less than or equal to _m_ if and only if _m_ is not less than _n_. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->
- For any natural number _n_, _n_ + 1 is... ::: ... greater than _n_. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->
- For any natural number _n_, no natural number is... ::: ... ::: between _n_ and _n_ + 1. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->
- No natural number is... ::: ... less than zero. <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

It can then be proved that {{induction, given the above-listed axioms, implies the well-ordering principle}}. The following proof {{uses complete induction and the first and fourth axioms}}. <!--SR:!2024-12-03,38,290!2024-10-29,14,290-->

__Proof.__ ::: Suppose there exists a [non-empty](empty%20set.md) set, _S_, of natural numbers that has no least element. Let _P_(_n_) be the assertion that _n_ is not in _S_. Then _P_(0) is true, for if it were false then 0 is the least element of _S_. Furthermore, let _n_ be a natural number, and suppose _P_(_m_) is true for all natural numbers _m_ less than _n_ + 1. Then if _P_(_n_ + 1) is false _n_ + 1 is in _S_, thus being a minimal element in _S_, a contradiction. Thus _P_(_n_ + 1) is true. Therefore, by the complete induction principle, _P_(_n_) holds for all natural numbers _n_; so _S_ is empty, a contradiction. Q.E.D. <!--SR:!2024-10-29,14,290!2024-12-03,38,290-->

On the other hand, the set {{$\{(0,n):n\in \mathbb {N} \}\cup \{(1,n):n\in \mathbb {N} \}$}}<!--, shown in the picture,--> is {{well-ordered<sup>[\[24\]](#^ref-24)</sup><sup>[\[35\]](#^ref-35)</sup> by the [lexicographic order](lexicographic%20order.md)}}. Moreover, {{except for the induction axiom, it satisfies all Peano axioms}}, where {{Peano's constant 0 is interpreted as the pair (0, 0), and Peano's _successor_ function is defined on pairs by succ(_x_, _n_) = (_x_, _n_ + 1) for all $x\in \{0,1\}$ and $n\in \mathbb {N}$}}. As an example for the violation of the induction axiom, define {{the predicate _P_(_x_, _n_) as (_x_, _n_) = (0, 0) or (_x_, _n_) = succ(_y_, _m_) for some $y\in \{0,1\}$ and $m\in \mathbb {N}$}}. Then {{the base case _P_(0, 0) is trivially true, and so is the induction step: if _P_(_x_, _n_), then _P_(succ(_x_, _n_))}}. However, _P_ is {{not true for all pairs in the set, since _P_(1,0) is false}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

Peano's axioms with the induction principle {{uniquely model the natural numbers}}. Replacing the induction principle with the well-ordering principle {{allows for more exotic models that fulfill all the axioms}}.<sup>[\[24\]](#^ref-24)</sup> <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

It is {{mistakenly printed in several books<sup>[\[24\]](#^ref-24)</sup> and sources}} that {{the well-ordering principle is equivalent to the induction axiom}}. In {{the context of the other Peano axioms, this is not the case}}, but in {{the context of other axioms, they are equivalent}};<sup>[\[24\]](#^ref-24)</sup> specifically, the well-ordering principle implies the induction axiom in {{the context of the first two above listed axioms and: <p> Every natural number is either 0 or _n_ + 1 for some natural number _n_}}. <!--SR:!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290!2024-10-29,14,290-->

A common mistake in many erroneous proofs is {{to assume that _n_ − 1 is a unique and well-defined natural number}}, a property which is {{not implied by the other Peano axioms}}.<sup>[\[24\]](#^ref-24)</sup> <!--SR:!2024-10-29,14,290!2024-10-29,14,290-->

## see also

- [induction puzzles](induction%20puzzles.md)
- [proof by exhaustion](proof%20by%20exhaustion.md)

## notes

1. Matt DeVos, [_Mathematical Induction_](https://www.sfu.ca/~mdevos/notes/graph/induction.pdf), [Simon Fraser University](Simon%20Fraser%20University.md) <a id="^ref-1"></a>^ref-1
2. Gerardo con Diaz, _[Mathematical Induction](http://www.math.harvard.edu/archive/23a_fall_05/Handouts/induction.pdf) [Archived](https://web.archive.org/web/20130502163438/http://www.math.harvard.edu/archive/23a_fall_05/Handouts/induction.pdf) 2 May 2013 at the [Wayback Machine](Wayback%20Machine.md)_, [Harvard University](Harvard%20University.md) <a id="^ref-2"></a>^ref-2
3. Anderson, Robert B. (1979). [_Proving Programs Correct_](https://archive.org/details/provingprogramsc0000ande). New York: John Wiley & Sons. p. [1](https://archive.org/details/provingprogramsc0000ande/page/1). [ISBN](ISBN.md) [978-0471033950](https://en.wikipedia.org/wiki/Special%3ABookSources/978-0471033950). <a id="^ref-3"></a>^ref-3
4. Suber, Peter. ["Mathematical Induction"](https://web.archive.org/web/20110524104121/http://www.earlham.edu/~peters/courses/logsys/math-ind.htm). Earlham College. Archived from [the original](http://www.earlham.edu/~peters/courses/logsys/math-ind.htm) on 24 May 2011. Retrieved 26 March 2011. <a id="^ref-4"></a>^ref-4
5. [Acerbi 2000](#CITEREFAcerbi2000). <a id="^ref-5"></a>^ref-5
6. [Rashed 1994](#CITEREFRashed1994), pp. 62–84. <a id="^ref-6"></a>^ref-6
7. [Mathematical Knowledge and the Interplay of Practices](https://books.google.com/books?id=HGMXCgAAQBAJ&pg=PA193) "The earliest implicit proof by mathematical induction was given around 1000 in a work by the Persian mathematician Al-Karaji" <a id="^ref-7"></a>^ref-7
8. Katz (1998), p. 255 <a id="^ref-8"></a>^ref-8
9. [Cajori (1918)](#CITEREFCajori1918), p. 197: 'The process of reasoning called "Mathematical Induction" has had several independent origins. It has been traced back to the Swiss Jakob (James) Bernoulli, the Frenchman B. Pascal and P. Fermat, and the Italian F. Maurolycus. [...] By reading a little between the lines one can find traces of mathematical induction still earlier, in the writings of the Hindus and the Greeks, as, for instance, in the "cyclic method" of Bhaskara, and in Euclid's proof that the number of primes is infinite.' <a id="^ref-9"></a>^ref-9
10. [Rashed 1994](#CITEREFRashed1994), p. 62. <a id="^ref-10"></a>^ref-10
11. [Simonson 2000](#CITEREFSimonson2000). <a id="^ref-11"></a>^ref-11
12. [Rabinovitch 1970](#CITEREFRabinovitch1970). <a id="^ref-12"></a>^ref-12
13. "It is sometimes required to prove a theorem which shall be true whenever a certain quantity _n_ which it involves shall be an integer or whole number and the method of proof is usually of the following kind. _1st_. The theorem is proved to be true when _n_ = 1. _2ndly_. It is proved that if the theorem is true when _n_ is a given whole number, it will be true if _n_ is the next greater integer. Hence the theorem is true universally. … This species of argument may be termed a continued _[sorites](polysyllogism.md)_" (Boole c. 1849 _Elementary Treatise on Logic not mathematical_ pp. 40–41 reprinted in [Grattan-Guinness, Ivor](Ivor%20Grattan-Guinness.md) and Bornet, Gérard (1997), _George Boole: Selected Manuscripts on Logic and its Philosophy_, Birkhäuser Verlag, Berlin, [ISBN](ISBN.md) [3-7643-5456-9](https://en.wikipedia.org/wiki/Special%3ABookSources/3-7643-5456-9)) <a id="^ref-13"></a>^ref-13
14. [Peirce 1881](#CITEREFPeirce1881). <a id="^ref-14"></a>^ref-14
15. [Shields 1997](#CITEREFShields1997). <a id="^ref-15"></a>^ref-15
16. Ted Sundstrom, _Mathematical Reasoning_, p. 190, Pearson, 2006, [ISBN](ISBN.md) [978-0131877184](https://en.wikipedia.org/wiki/Special%3ABookSources/978-0131877184) <a id="^ref-16"></a>^ref-16
17. Smullyan, Raymond (2014). _A Beginner's Guide to Mathematical Logic_. Dover. p. 41. [ISBN](ISBN.md) [0486492370](https://en.wikipedia.org/wiki/Special%3ABookSources/0486492370). <a id="^ref-17"></a>^ref-17
18. Buss, Samuel (1986). _Bounded Arithmetic_. Naples: Bibliopolis. <a id="^ref-18"></a>^ref-18
19. ["Proof:Strong induction is equivalent to weak induction"](https://courses.cs.cornell.edu/cs2800/wiki/index.php/Proof:Strong_induction_is_equivalent_to_weak_induction). _[Cornell University](Cornell%20University.md)_. Retrieved 4 May 2023. <a id="^ref-19"></a>^ref-19
20. .Shafiei, Niloufar. ["Strong Induction and Well-Ordering"](https://www.eecs.yorku.ca/course_archive/2008-09/S/1019/Website_files/16-stong-induction-and-well-ordering.pdf) (PDF). _York University_. Retrieved 28 May 2023. <a id="^ref-20"></a>^ref-20
21. ["Forward-Backward Induction | Brilliant Math & Science Wiki"](https://brilliant.org/wiki/forward-backwards-induction/). _brilliant.org_. Retrieved 23 October 2019. <a id="^ref-21"></a>^ref-21
22. Cauchy, Augustin-Louis (1821). [_Cours d'analyse de l'École Royale Polytechnique, première partie, Analyse algébrique,_](http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-29058) [Archived](https://web.archive.org/web/20171014135801/http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-29058) 14 October 2017 at the [Wayback Machine](Wayback%20Machine.md) Paris. The proof of the inequality of arithmetic and geometric means can be found on pages 457ff. <a id="^ref-22"></a>^ref-22
23. Cohen, Joel E. (1961). "On the nature of mathematical proof". _Opus_.. Reprinted in _A Random Walk in Science_ (R. L. Weber, ed.), Crane, Russak & Co., 1973. <a id="^ref-23"></a>^ref-23
24. Öhman, Lars–Daniel (6 May 2019). ["Are Induction and Well-Ordering Equivalent?"](https://doi.org/10.1007%2Fs00283-019-09898-4). _The Mathematical Intelligencer_. __41__ (3): 33–40. [doi](digital%20object%20identifier.md):[10.1007/s00283-019-09898-4](https://doi.org/10.1007%2Fs00283-019-09898-4). <a id="^ref-24"></a>^ref-24

## references

This text incorporates [content](https://en.wikipedia.org/wiki/mathematical_induction) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

### introduction

- [Franklin, J.](James%20Franklin%20(philosopher).md); Daoud, A. (2011). [_Proof in Mathematics: An Introduction_](http://www.maths.unsw.edu.au/~jim/proofs.html). Sydney: Kew Books. [ISBN](ISBN.md) [978-0-646-54509-7](https://en.wikipedia.org/wiki/Special%3ABookSources/978-0-646-54509-7). (Ch. 8.)
- ["Mathematical induction"](https://www.encyclopediaofmath.org/index.php?title=Mathematical_induction). _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_. [EMS Press](European%20Mathematical%20Society.md). 2001 [1994].
- [Hermes, Hans](Hans%20Hermes.md) (1973). _Introduction to Mathematical Logic_. Hochschultext. London: Springer. [ISBN](ISBN.md) [978-3540058199](https://en.wikipedia.org/wiki/Special%3ABookSources/978-3540058199). [ISSN](ISSN.md) [1431-4657](https://search.worldcat.org/issn/1431-4657). [MR](Mathematical%20Reviews.md) [0345788](https://mathscinet.ams.org/mathscinet-getitem?mr=0345788).
- [Knuth, Donald E.](Donald%20Knuth.md) (1997). [_The Art of Computer Programming, Volume 1: Fundamental Algorithms_](The%20Art%20of%20Computer%20Programming.md) (3rd ed.). Addison-Wesley. [ISBN](ISBN.md) [978-0-201-89683-1](https://en.wikipedia.org/wiki/Special%3ABookSources/978-0-201-89683-1). (Section 1.2.1: Mathematical Induction, pp. 11–21.)
- [Kolmogorov, Andrey N.](Andrey%20Kolmogorov.md); [Fomin, Sergei V.](Sergei%20Fomin.md) (1975). [_Introductory Real Analysis_](https://archive.org/details/introductoryreal00kolm_0). Silverman, R. A. (trans., ed.). New York: Dover. [ISBN](ISBN.md) [978-0-486-61226-3](https://en.wikipedia.org/wiki/Special%3ABookSources/978-0-486-61226-3). (Section 3.8: Transfinite induction, pp. 28–29.)

### history

- Acerbi, Fabio (August 2000). ["Plato: _Parmenides_ 149a7-c3. A Proof by Complete Induction?"](https://www.academia.edu/8016024). _[Archive for History of Exact Sciences](Archive%20for%20History%20of%20Exact%20Sciences.md)_. __55__ (1): 57–76. [doi](digital%20object%20identifier.md):[10.1007/s004070000020](https://doi.org/10.1007%2Fs004070000020). [JSTOR](JSTOR.md) [41134098](https://www.jstor.org/stable/41134098). [S2CID](Semantic%20Scholar.md#S2CID) [123045154](https://api.semanticscholar.org/CorpusID:123045154).
- Bussey, W. H. (1917). "The Origin of Mathematical Induction". _[The American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md)_. __24__ (5): 199–207. [doi](digital%20object%20identifier.md):[10.2307/2974308](https://doi.org/10.2307%2F2974308). [JSTOR](JSTOR.md) [2974308](https://www.jstor.org/stable/2974308).
- [Cajori, Florian](Florian%20Cajori.md) (1918). "Origin of the Name "Mathematical Induction"". _[The American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md)_. __25__ (5): 197–201. [doi](digital%20object%20identifier.md):[10.2307/2972638](https://doi.org/10.2307%2F2972638). [JSTOR](JSTOR.md) [2972638](https://www.jstor.org/stable/2972638).
- [Fowler, D.](David%20Fowler%20(mathematician).md) (1994). "Could the Greeks Have Used Mathematical Induction? Did They Use It?". _Physis_. __31__: 253–265.
- [Freudenthal, Hans](Hans%20Freudenthal.md) (1953). "Zur Geschichte der vollständigen Induction". _[Archives Internationales d'Histoire des Sciences](International%20Academy%20of%20the%20History%20of%20Science.md#publications)_. __6__: 17–37.
- [Katz, Victor J.](Victor%20J.%20Katz.md) (1998). _History of Mathematics: An Introduction_. [Addison-Wesley](Addison-Wesley.md). [ISBN](ISBN.md) [0-321-01618-1](https://en.wikipedia.org/wiki/Special%3ABookSources/0-321-01618-1).
- [Peirce, Charles Sanders](Charles%20Sanders%20Peirce.md) (1881). ["On the Logic of Number"](https://books.google.com/books?id=LQgPAAAAIAAJ). _[American Journal of Mathematics](American%20Journal%20of%20Mathematics.md)_. __4__ (1–4): 85–95. [doi](digital%20object%20identifier.md):[10.2307/2369151](https://doi.org/10.2307%2F2369151). [JSTOR](JSTOR.md) [2369151](https://www.jstor.org/stable/2369151). [MR](Mathematical%20Reviews.md) [1507856](https://mathscinet.ams.org/mathscinet-getitem?mr=1507856). Reprinted (CP 3.252–288), (W 4:299–309)
- [Rabinovitch, Nachum L.](Nahum%20Rabinovitch.md) (1970). "Rabbi Levi Ben Gershon and the origins of mathematical induction". _Archive for History of Exact Sciences_. __6__ (3): 237–248. [doi](digital%20object%20identifier.md):[10.1007/BF00327237](https://doi.org/10.1007%2FBF00327237). [MR](Mathematical%20Reviews.md) [1554128](https://mathscinet.ams.org/mathscinet-getitem?mr=1554128). [S2CID](Semantic%20Scholar.md#S2CID) [119948133](https://api.semanticscholar.org/CorpusID:119948133).
- [Rashed, Roshdi](Roshdi%20Rashed.md) (1972). "L'induction mathématique: al-Karajī, as-Samaw'al". _[Archive for History of Exact Sciences](Archive%20for%20History%20of%20Exact%20Sciences.md)_ (in French). __9__ (1): 1–21. [doi](digital%20object%20identifier.md):[10.1007/BF00348537](https://doi.org/10.1007%2FBF00348537). [MR](Mathematical%20Reviews.md) [1554160](https://mathscinet.ams.org/mathscinet-getitem?mr=1554160). [S2CID](Semantic%20Scholar.md#S2CID) [124040444](https://api.semanticscholar.org/CorpusID:124040444).
- Rashed, R. (1994). "Mathematical induction: al-Karajī and al-Samawʾal". [_The Development of Arabic Mathematics: Between Arithmetic and Algebra_](https://books.google.com/books?id=vSkClSvU_9AC&pg=PA62). Boston Studies in the Philosophy of Science. Vol. 156. Springer Science & Business Media. [ISBN](ISBN.md) [9780792325659](https://en.wikipedia.org/wiki/Special%3ABookSources/9780792325659).
- Shields, Paul (1997). "Peirce's Axiomatization of Arithmetic". In Houser, Nathan; Roberts, Don D.; Evra, James Van (eds.). [_Studies in the Logic of Charles S. Peirce_](https://archive.org/details/studiesinlogicof00nath). Indiana University Press. pp. 43–52. [ISBN](ISBN.md) [0-253-33020-3](https://en.wikipedia.org/wiki/Special%3ABookSources/0-253-33020-3). [MR](Mathematical%20Reviews.md) [1720827](https://mathscinet.ams.org/mathscinet-getitem?mr=1720827).
- Simonson, Charles G. (Winter 2000). ["The Mathematics of Levi ben Gershon, the Ralbag"](http://web.stonehill.edu/compsci/Shai_papers/MathofLevi.pdf) (PDF). _Bekhol Derakhekha Daehu_. __10__. Bar-Ilan University Press: 5–21.
- [Unguru, S.](Sabetai%20Unguru.md) (1991). "Greek Mathematics and Mathematical Induction". _Physis_. __28__: 273–289.
- [Unguru, S.](Sabetai%20Unguru.md) (1994). "Fowling after Induction". _Physis_. __31__: 267–272.
- Vacca, G. (1909). ["Maurolycus, the First Discoverer of the Principle of Mathematical Induction"](https://doi.org/10.1090%2FS0002-9904-1909-01860-9). _[Bulletin of the American Mathematical Society](Bulletin%20of%20the%20American%20Mathematical%20Society.md)_. __16__ (2): 70–73. [doi](digital%20object%20identifier.md):[10.1090/S0002-9904-1909-01860-9](https://doi.org/10.1090%2FS0002-9904-1909-01860-9). [MR](Mathematical%20Reviews.md) [1558845](https://mathscinet.ams.org/mathscinet-getitem?mr=1558845).
- Yadegari, Mohammad (1978). "The Use of Mathematical Induction by Abū Kāmil Shujā' Ibn Aslam (850-930)". _[Isis](isis%20(journal).md)_. __69__ (2): 259–262. [doi](digital%20object%20identifier.md):[10.1086/352009](https://doi.org/10.1086%2F352009). [JSTOR](JSTOR.md) [230435](https://www.jstor.org/stable/230435). [S2CID](Semantic%20Scholar.md#S2CID) [144112534](https://api.semanticscholar.org/CorpusID:144112534).
