---
aliases:
  - HKUST COMP 2711H
  - HKUST COMP 2711H index
  - HKUST COMP2711H
  - HKUST COMP2711H index
  - COMP 2711H
  - COMP 2711H index
  - COMP2711H
  - COMP2711H index
tags:
  - flashcard/active/special/academia/HKUST/COMP_2711H/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 2711H
- name: Honors Discrete Mathematical Tools for Computer Science

The content is in teaching order.

- grading scheme: 40% homework, 30% midterm examination, 30% final examination
  - homework: 10% × 4. It must be written in LaTeX. After submitting the homework, the instructor and TAs will read the submission and give feedback. You can then resubmit once more. The highest out of the 2 submission wills be counted. Resubmission may be disallowed if the initial submission is low quality or lacks effort.
  - midterm examination: 30%.
  - final examination: 30%. It covers the entire course.
- [questions](questions/questions.md)

## week 1 lecture

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:20:00+08:00
- topic: propositional logic
- course logistics
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ propositional calculus](../../../../general/propositional%20calculus.md#propositional%20calculus)
    - proposition ::: A declarative statement that is either true (1) or false (0). No third value is possible. Typically it is represented by _p_, _q_, _r_, and so forth.
  - [truth table](../../../../general/truth%20table.md) ::: A table representing a boolean function. There are $n + 1$ columns, where the first $n$ columns are the inputs of the boolean function, while the last column is the output of the boolean function. There are $2^n$ rows, representing all possible combinations of the $n$ inputs mapping to the corresponding $2^n$ outputs.
    - [§ truth table](../../../../general/truth%20table.md#truth%20table)
  - boolean algebra operations ::: An operation that takes connections one or more propositions. These operations can be chained.
    - negation (not) ::: $\lnot p$: $$\begin{aligned} (0) & \mapsto 1 \\ (1) & \mapsto 0 \end{aligned}$$
    - disjunction (or) ::: $p \lor q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 1 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - conjunction (and) ::: $p \land q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 0 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - implication (if-then) ::: $p \rightarrow q$: $$\begin{aligned} (0, 0) & \mapsto 1 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - boolean algebra operations / order of operations ::: $\lnot$ > $\lor, \land$ > $\rightarrow$
  - [tautology](../../../../general/tautology%20(logic).md) (true) ::: A proposition that is always true, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ tautology](../../../../general/tautology%20(logic).md#tautology)
  - [contradiction](../../../../general/contradiction.md) (false) ::: A proposition that is always false, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ contradiction](../../../../general/contradiction.md#contradiction)
  - propositional calculus / real life application ::: Consider making a one bit half adder. You want: $$\begin{aligned} 0 + 0 & = 0 \\ 1 + 0 & = 1 \\ 0 + 1 & = 1 \\ 1 + 1 & = 0 \end{aligned}$$. This can be expressed as $$\begin{aligned} \text{sum of products: } & (a \land \lnot b) \lor (\lnot a \land b) \\ \text{product of sums: } & (\lnot a \lor \lnot b) \land (a \lor b) \end{aligned}$$. This is also known as the exclusive-or (xor) operation.
  - [logical equivalence](../../../../general/logical%20equivalence.md) ::: Two propositions have the same truth values, no matter how the atomic propositions (terms with no operations) are assigned. One simple way to prove it is via a truth table and compare whether the rows are equivalent.
    - [§ logical equivalence](../../../../general/logical%20equivalence.md#logical%20equivalence)
    - [§ relation to material equivalence](../../../../general/logical%20equivalence.md#relation%20to%20material%20equivalence) ::: Material equivalence is simply a proposition that says two propositions have the same truth values. It may be false or true. Two propositions are logically equivalent if the material equivalence between them is true, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ general logical equivalences](../../../../general/logical%20equivalence.md#general%20logical%20equivalences)
  - [conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md) ::: The dual (Amir calls it inverse proposition) of a proposition $p$ is denoted $p^d$, and is formed by replacing $\land$ by $\lor$, $\lor$ by $\land$, T by F, and F by T. The dual relates to the original proposition by $\lnot p \equiv \overline p^d$, where $\overline p$ is replacing all atomic propositions (propositions without $\land$, $\lor$, and $\lnot$) by their negations. This can be interpreted as negating the "output" of $p$, i.e. $\lnot p$ is the same as negating all "inputs" of its dual $p^d$, i.e. $\overline p^d$.
    - [§ conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md#conjunction%2Fdisjunction%20duality)
    - [§ negation is semantically equivalent to dual](../../../../general/conjunction_disjunction_duality.md#negation%20is%20semantically%20equivalent%20to%20dual)
    - [§ further duality theorems](../../../../general/conjunction_disjunction_duality.md#further%20duality%20theorems)
  - [rules of inference](../../../../general/rules%20of%20inference.md) ::: Rules that allows deducing a consequence to be true, given that zero or more premises are true.
    - [rules of inference](../../../../general/rules%20of%20inference.md) / motivation ::: To prove a proposition $X := h_1 \land \ldots \land h_n \rightarrow c$ is true, where $h_i$ are _atomic_ variables (terms with no operations), one could use a proof table, but this would require $2^n$ rows. We could instead use another proposition equivalent to $X$, denoted $Y := p_1 \land \ldots \land p_n \rightarrow c$ where $p_i$ are propositions (not necessarily atomic). Coupled with _rules of inference_, we can prove $X$ via proving $Y$.
    - rules of inference / _modus ponens_ ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{p \phantom{\rightarrow q} } \\ & q & \end{aligned}$$
    - rules of inference / hypothetical syllogism ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{q \rightarrow r} \\ & p \rightarrow r & \end{aligned}$$
    - rules of inference / _modus tollens_ (not to be confused with the related _contraposition_) ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{\lnot q \!\!\!\! \phantom{\rightarrow q} } \\ & \lnot p & \end{aligned}$$
- materials
  - [lecture video](https://youtu.be/Iexw2Lg9BmI)
  - Grimaldi/Chapter 2: Fundamentals of Logic
  - [video: proofs](https://youtu.be/L3LMbpZIKhQ)

## week 1 tutorial

- time: 2024-09-02T18:00:00+08:00/2024-09-02T18:50:00+08:00
- topic: predicate logic, Peano's axioms
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ list of classically valid argument forms](../../../../general/propositional%20calculus.md#list%20of%20classically%20valid%20argument%20forms)
  - [rules of inference](../../../../general/rules%20of%20inference.md_
    - _modus ponens_
    - hypothetical syllogism
    - _modus tollens_
    - rules of inference / conjunction ::: $$\begin{aligned} & p \\ & \underline{q \phantom{\land q} } \\ & p \land q & \end{aligned}$$
    - rules of inference / disjunctive syllogism ::: $$\begin{aligned} & p \lor q \\ & \underline{\lnot p \!\!\!\! \phantom{\lor q} } \\ & q \end{aligned}$$
    - rules of inference / transposition (with $F$ as the consequent) ::: $$\begin{aligned} & \underline{\lnot p \rightarrow F} \\ & p \end{aligned}$$
    - rules of inference / simplification ::: $$\begin{aligned} & \underline{p \land q} \\ & p \end{aligned}$$
    - rules of inference / addition ::: $$\begin{aligned} & \underline{p \phantom{\lor q} } \\ & p \lor q \end{aligned}$$
    - rules of inference / importation (applied form) ::: $$\begin{aligned} & p \land q \\ & \underline{p \rightarrow (q \rightarrow r)} \\ & r \end{aligned}$$
    - rules of inference / constructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{p \lor r \phantom{s} } \\ & q \lor s \end{aligned}$$
    - rules of inference / destructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{\lnot q \lor \lnot s} \\ & \lnot p \lor \lnot r \end{aligned}$$
    - rules of inference / constructive dilemma (unapplied form, with the same consequent) ::: $$\begin{aligned} & p \rightarrow r \\ & \underline{q \rightarrow r \phantom{r \rightarrow r} } \\ & (p \lor q) \rightarrow r \end{aligned}$$
    - rules of inference / material equivalence (_modus ponens_) ::: $$\begin{aligned} & p \equiv q \\ & \underline{p \phantom{\equiv q} } \\ & q \end{aligned}$$
  - proof format ::: A proof consists of several lines. Each line, numbered, is a proof statement, which either states the premise or is a statement derived from previous statements (referenced using line numbers) by rules of inference. For example: $$\begin{aligned} 1. \quad & p \rightarrow r && (\text{premise}) \\ 2. \quad & p && (\text{premise}) \\ 3. \quad & r && (\text{from 1 and 2}) \end{aligned}$$.
- [first-order logic](../../../../general/first-order%20logic.md)
  - [§ first-order logic](../../../../general/first-order%20logic.md#first-logic%20logic)
  - [predicate](../../../../general/predicate%20(mathematical%20logic).md) ::: A statement that becomes a proposition when the one or more unknowns are replaced by specified values from the universe. The universe is the set of all possible values for the unknowns.
  - universal quantification ::: $\forall x \, p(x)$ means for all $x$ in the universe $p(x)$ is true. If the universe is empty, $\forall x \, p(x)$ is true for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to existential quantification by $$\lnot \forall x \, p(x) \equiv \exists x \, \lnot p(x)$$.
    - universal quantification / distributive law ::: It distributes over logical conjunctions: $$\forall x \, (p(x) \land q(x)) \equiv \forall x \, p(x) \land \forall x \, q(x)$$. But it does NOT distribute over logical disjunctions: $$\forall x \, (p(x) \lor q(x)) \leftarrow \forall x \, p(x) \lor \forall x \, q(x)$$ and only the converse (shown above) is true.
  - existential quantification ::: $\exists x \, p(x)$ means there is at least one $x$ in the universe that $p(x)$ is true. If the universe is empty, $\exists x \, p(x)$ is false for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to universal quantification by $$\lnot \exists x \, p(x) \equiv \forall x \, \lnot p(x)$$.
    - existential quantification / distributive law ::: It distributes over logical disjunctions: $$\exists x \, (p(x) \lor q(x)) \equiv \exists x \, p(x) \lor \exists x \, q(x)$$. But it does NOT distribute over logical conjunctions: $$\exists x \, (p(x) \land q(x)) \rightarrow \exists x \, p(x) \land \exists x \, q(x)$$ but the converse is not necessarily true.
- [Peano axioms](../../../../general/Peano%20axioms.md) ::: (The second-order formulation is used.) One, $0$ is a natural number. Two, if $n$ is a natural number, then $S(n)$ is a natural number. Third, if $S(n) = S(m)$, then $n = m$. Four, $S(n) \ne 0$ for all natural numbers $n \in \mathbb N$. Five, if $K$ is a set such that $0 \in K$, and for all natural numbers $n \in \mathbb N$, if $n \in K$ then $S(n) \in K$, then $K = \mathbb N$ (induction).
  - [§ Peano axioms](../../../../general/Peano%20axioms.md#Peano%20axioms)
  - [§ historical second-order formulation](../../../../general/Peano%20axioms.md#historical%20second-order%20formulation)
  - Peano axioms / 1st axiom motivation ::: This defines the starting $0$ as a natural number.
  - Peano axioms / 2nd axiom motivation ::: This defines a successor function $S$ that can generate more natural numbers. Equivalently, the natural numbers are closed under $S$.
  - Peano axioms / 3rd axiom motivation ::: This makes the successor function injective (but not surjective, as $0$ is not in the image of the function).
  - Peano axioms / 4th axiom motivation ::: Coupled with the injective property, this makes the successor function never go back to the starting number $0$. Otherwise, the successor function can, at one point, loop back to $0$, and there will only be finitely many natural numbers.
  - Peano axioms / 5th axiom motivation ::: The 4 axioms above are insufficient to ensure that repeatedly applying $S$ on $0$ can generate all natural numbers. Indeed, an infinite successor chain starting from $0$ that does not contain all the natural numbers, with a finite circular successor chain, is compatible with the 4 axioms above. The 5th axiom simply states that the infinite successor chain starting from $0$ is the set of all natural numbers, excluding the situation above. This is also what makes mathematical induction possible.
- materials
  - [lecture video](https://youtu.be/X_SF_o9ZwmA)
  - Grimaldi/Chapter 2: Fundamentals of Logic
  - [video: Peano axioms](https://youtu.be/5zl2zBqNAHM)

## week 1 lecture 2

- time: 2024-09-04T09:00:00+08:00/2024-09-04T11:20:00+08:00
- topic: induction, well-ordering, infinite descent
- [Peano axioms](../../../../general/Peano%20axioms.md)
  - [§ defining arithmetic operations and relations](../../../../general/Peano%20axioms.md#defining%20arithmetic%20operations%20and%20relations)
  - [§ addition](../../../../general/Peano%20axioms.md#addition) ::: 2 rules: $\forall n; n + 0 = n$, $\forall n, m; n + s(m) = s(n + m)$. All other rules that you know of everyday addition can be derived from these rules. From this we can prove that addition is commutative ($\forall n, m; n + m = m + n$) and associative ($\forall n, m, o; (n + m) + o = n + (m + o)$).
  - [§ multiplication](../../../../general/Peano%20axioms.md#multiplication) ::: Assuming addition is defined, 2 rules: $\forall n, n \cdot 0 = 0$, $\forall n, m; n \cdot s(m) = n + n \cdot m$. All other rules that you know of everyday multiplication can be derived from these rules. From this we can prove that multiplication is commutative ($\forall n, m; n \cdot m = m \cdot n$) and associative ($\forall n, m, o; (n \cdot m) \cdot o = n \cdot (m \cdot o)$).
  - [§ inequalities](../../../../general/Peano%20axioms.md#inequalities) ::: Assuming addition is defined, the inequality $\le$ is defined as $$n \le m \equiv \exists x; n + x = m$$.
- [mathematical induction](../../../../general/mathematical%20induction.md)
  - [§ mathematical induction](../../../../general/mathematical%20induction.md#mathematical%20induction)
  - [§ description](../../../../general/mathematical%20induction.md#description)
  - [§ examples](../../../../general/mathematical%20induction.md#examples)
  - [§ example of error in the induction step](../../../../general/mathematical%20induction.md#example%20of%20error%20in%20the%20induction%20step)
  - [§ relationship to the well-ordering principle](../../../../general/mathematical%20induction.md#relationship%20to%20the%20well-ordering%20principle)
- [well-ordering principle](../../../../general/well-ordering%20principle.md) ::: Every _non-empty_ subset of the natural numbers (not integers) has a least element. Proofs using this are generally by contradiction. This is implied from induction (from Peano axioms) or infinite descent. However, the well-ordering principle does not imply induction (under the other Peano axioms), and so is not equivalent to induction.
  - [§ well-ordering principle](../../../../general/well-ordering%20principle.md#well-ordering%20principle)
- [proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md) ::: There are no infinite strictly decreasing sequences of natural numbers. Proofs using this are generally by contradiction, and involve constructing an infinite descent of natural numbers, which contradicts this. Another way is assuming a minimal solution to a problem exists, but then prove that it would lead to a smaller solution. This is equivalent to induction (from Peano axioms), and implies the well-ordering principle .
  - [§ proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md#proof%20by%20infinite%20descent)
- [questions/2024-09-04](questions/2024-09-04.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/xR3jmz5WdQ4)
  - [video: induction](https://youtu.be/z8HKWUWS-lA)
  - [video: 2+2=4](https://youtu.be/TQpHVtlXuyc)
  - [Mathematical Induction](https://www.sydney.edu.au/content/dam/students/documents/mathematics-learning-centre/mathematical-induction.pdf)

## week 2 lecture

- time: 2024-09-09T10:30:00+08:00/2024-09-09T11:20:00+08:00
- topic: induction problems, strong induction
- [mathematical induction](../../../../general/mathematical%20induction.md): even more induction problems, strong induction
  - [§ variants](../../../../general/mathematical%20induction.md#variants)
  - [§ complete (strong) induction](../../../../general/mathematical%20induction.md#complete%20(strong)%20induction)
- [Nim](../../../../general/Nim.md)
  - [§ Nim](../../../../general/Nim.md#Nim)
  - [§ game play and illustration](../../../../general/Nim.md#game%20play%20and%20illustration)
- [questions/2024-09-09/lecture](questions/2024-09-09%20lecture.md)
- materials
  - [lecture video](https://youtu.be/X6l72P9QW7A)
  - [video: strong induction](https://youtu.be/NuGDkmwEObM)
  - [video: proof by strong induction](https://youtu.be/USOsVbEbOIg)
    - Pause the videos whenever a problem is posed and try to solve it on your own first, before watching the solution.
  - [video: strong induction examples](https://youtu.be/6O1s3_GsSHo)
  - Engel/Chapter 3: The Extremal Principle
    - It is really important that you give \*\*every\*\* problem an honest and serious attempt before reading its solution. You must reach mastery in using mathematical induction and its equivalent forms. All of the future modules in this course depend on such mastery.
  - Engel/Chapter 8: The Induction Principle

## week 2 tutorial

- time: 2024-09-09T18:00:00+08:00/2024-09-09T18:50:00+08:00
- topic: solving more induction problems
- [mathematical induction](../../../../general/mathematical%20induction.md): even more induction problems
- [questions/2024-09-09/tutorial](questions/2024-09-09%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/sTKBr2au1o4)
  - [video: induction problems](https://youtu.be/tHNVX3e9zd0)
  - [video: divisibility problems solved by induction](https://youtu.be/8J7Bft3BN0g)
  - [video: epic induction](https://youtu.be/bylFzBxzQ9M)
  - Engel/Chapter 3: The Extremal Principle
  - Engel/Chapter 8: The Induction Principle

## week 2 lecture 2

- time: 2024-09-11T09:00:00+08:00/2024-09-11T11:20:00+08:00
- topic: counting, permutations, combinations, balls and walls
- [combinatorial principles](../../../../general/combinatorial%20principles.md) ::: principles commonly used to solve combinatorial problems: rule of sum, rule of product, permutation, combination, ...
  - [§ combinatorial principles](../../../../general/combinatorial%20principles.md#combinatorial%20principles)
  - [§ rule of sum](../../../../general/combinatorial%20principles.md#rule%20of%20sum) ::: Also known as the principle of addition or case work principle. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ + _B_ ways to do either one thing.
  - [§ rule of product](../../../../general/combinatorial%20principles.md#rule%20of%20product) ::: Also known as the principle of multiplication. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ \* _B_ ways to do both things.
- [permutation](../../../../general/permutation.md) ::: the arrangement of $k$ things from $n$ things (order matters), calculated by $$P(n, k) = \frac {n!} {(n - k)!}$$
- [combination](../../../../general/combination.md) ::: choosing $k$ things from $n$ things (order does not matter), calculated by $$C(n, k) = \binom n k = \frac {n!} {(n - k)! k!}$$
- [questions/2024-09-11](questions/2024-09-11.md)
- [week 2 problem set](questions/week%202%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/zpeMfQT9JA0)
  - Grimaldi/Chapter 1: Fundamental Principles of Counting
  - Chen and Koh/Chapter 1: Permutations and Combinations (very important)
  - Ross/Chapter 1: Combinatorial Analysis
    - It is crucial that you solve \*\*every\*\* exercise at the end of these chapters.
  - [fun to read: Which Rectangular Chessboards Have a Knight's Tour?](https://www.jstor.org/stable/2690649)

## week 3 lecture

- time: 2024-09-16T10:30:00+08:00/2024-09-16T11:20:00+08:00
- topic: solving counting problems
- [questions/2024-09-16/lecture](questions/2024-09-16%20lecture.md)
- materials
  - [lecture video](https://youtu.be/YyNe0mgrK1A)
  - Chen and Koh/Chapter 1: Permutations and Combinations (very important)
  - Andreescu and Feng: solve problem 1 to problem 24

## week 3 tutorial

- time: 2024-09-16T18:00:00+08:00/2024-09-16T18:50:00+08:00
- topic: more counting
- [questions/2024-09-16/tutorial](questions/2024-09-16%20tutorial.md)
- [week 3 problem set](questions/week%203%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/p0Lb0odJCfU)
  - Andreescu and Feng: solve problem 25 to problem 51
- assignments: [homework 1](assignments/homework%201/submission.tex)

## week 3 lecture 2

- time: 2024-09-18T09:00:00+08:00/2024-09-18T11:20:00+08:00
- public holiday: Day after Mid-Autumn Festival

## week 3 TA session

- time: 2024-09-20T19:00:00+08:00/2024-09-20T19:50:00+08:00
- topic: solving weekly problem set 1
- [questions/2024-09-20](questions/2024-09-20.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/wbck_JlX9C4)

## week 4 lecture

- time: 2024-09-23T10:30:00+08:00/2024-09-23T11:20:00+08:00
- topic: principle of inclusion and exclusion
- [questions/2024-09-23/lecture](questions/2024-09-23%20lecture.md)
- materials
  - [lecture video](https://youtu.be/c0fb16fNpXY)
  - Chen and Koh/Chapter 2: Binomial Coefficients
  - Chen and Koh/Chapter 4: Inclusion–Exclusion
  - [video: inclusion–exclusion example](https://youtu.be/51-b2mgZVNY)
  - [video: 3-set PIE](https://youtu.be/VQmWJXeevfM)
  - [video: counting using PIE](https://youtu.be/rBLuvLDutdY)

## week 4 tutorial

- time: 2024-09-23T18:00:00+08:00/2024-09-23T18:50:00+08:00
- topic: generalized principle of inclusion and exclusion
- [questions/2024-09-23/tutorial](questions/2024-09-23%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/58cvEnENNYs)
  - Chen and Koh/Chapter 2: Binomial Coefficients
  - Chen and Koh/Chapter 4: Inclusion–Exclusion
  - Grimaldi/Chapter 8: Inclusion–Exclusion
  - [video: inclusion–exclusion](https://youtu.be/GS7dIWA6Hpo)
  - [video: PIE problems](https://youtu.be/Y0CYHMqomgI)
  - [video: generalized PIE](https://youtu.be/D1T3xy_vtxU)
  - [video: derangements](https://youtu.be/BOFWLhH0Igo)

## week 4 lecture 2

- time: 2024-09-25T09:00:00+08:00/2024-09-25T11:20:00+08:00
- topic: pigeonhole principle
- [questions/2024-09-25](questions/2024-09-25.md)
- [week 4 problem set](questions/week%204%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/Bryg6j3RExA)
  - Chen and Koh/Chapter 3: Pigeonhole and Ramsey
  - Engel/Chapter 4: Box Principle
  - Andreescu and Feng: solve advanced problem 1 to advanced problem 15
  - [video: pigeonhole principle](https://youtu.be/2-mxYrCNX60)
  - [video: pigeonhole principle examples](https://youtu.be/pPuvnD4PYNE)
  - [video: pigeonhole principle — establishing a pattern](https://youtu.be/YKsHlxnWylc)
  - [video: pigeonhole principle — generalizing the cases](https://youtu.be/W6FDiVHMo_g)
  - [playlist: more advanced pigeonhole principle problems](https://youtube.com/playlist?list=PLxdD-3GVlQSmC8gGQrRCh1VmlmAQikJ_Q)

## week 4 TA session

- time: 2024-09-27T17:00:00+08:00/2024-09-27T17:50:00+08:00
- topic: solving weekly problem set 2
- [questions/2024-09-27](questions/2024-09-27.md)
- [week 2 problem set](questions/week%202%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/7VN1ZCUpKKk)

## week 5 lecture

- time: 2024-09-30T10:30:00+08:00/2024-09-30T11:20:00+08:00
- topic: graphs, trees, paths, walks
- [questions/2024-09-30/lecture](questions/2024-09-30%20lecture.md)
- materials
  - [lecture video](https://youtu.be/rmk2RCszCt4)
  - West/Section 1.1: What is a Graph?
    - Most of the theorems we proved in class were from these sections, but the proofs are often different. So, you should read the book and also solve the exercises.
  - West/Section 1.2: Paths, Cycles, and Trails
  - [video playlist: introduction to graph theory](https://youtu.be/C7YrMRdLkqo?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS)
  - [video playlist: watch lectures 1 to 4](https://youtube.com/playlist?list=PLoAxxVQYIwM73zRO5gZL0exCw70O8ZlvJ)

## week 5 tutorial

- time: 2024-09-30T18:00:00+08:00/2024-09-30T18:50:00+08:00
- topic: more theorems on graphs and trees
- [questions/2024-09-30/tutorial](questions/2024-09-30%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/uwSD0woHeGU)
  - West/Section 1.3: Vertex Degrees & Counting
    - When reading this text, read each theorem but try to prove it yourself first before reading the proof. Also, make sure you solve all the exercises.
  - West/Section 1.4: Directed Graphs
  - Andreescu and Feng: solve advanced problem 16 to advanced problem 30
  - [video playlist: watch from 10.1.1 to 11.1.1](https://youtu.be/QHmL0AnZ3Dc?list=PLl-gb0E4MII28GykmtuBXNUNoej-vY5Rz)
  - [recommended to watch: graph theory background](https://youtu.be/SofC3dIhwRA)

## week 5 lecture 2

- time: 2024-10-02T09:00:00+08:00/2024-10-02T11:20:00+08:00
- topic: even more theorems on graphs and trees
- [questions/2024-10-02](questions/2024-10-02.md)
- [week 5 problem set](questions/week%205%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/4vL3zgdP_D4)
  - West/Section 2.1: Trees and Distance: Basic Properties
  - West/Section 2.2: Spanning Trees
  - [recommended to watch: DFS and BFS](https://youtu.be/MOlzncRyOL4)
  - Grimaldi/Chapter 11: Graph Theory
  - Grimaldi/Chapter 12: Trees

## week 5 TA session

- time: 2024-10-04T17:00:00+08:00/2024-10-04T17:50:00+08:00
- topic: solving weekly problem set 3
- [questions/2024-10-04](questions/2024-10-04.md)
- [week 3 problem set](questions/week%203%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/VDPaNbb3KVo)
  - [video: recurrence for number of partitions](https://youtu.be/F4zYDx-EfZI)

## week 6 lecture

- time: 2024-10-07T10:30:00+08:00/2024-10-07T11:20:00+08:00
- topic: minimum spanning trees, directed graphs, DAGs
- [questions/2024-10-07/lecture](questions/2024-10-07%20lecture.md)
- materials
  - [lecture video](https://youtu.be/97515nOWqAo)
  - [video: Kruskal's algorithm](https://youtu.be/JZBQLXgSGfs)
  - [video: Prim's algorithm](https://youtu.be/jsmMtJpPnhU)
    - Before watching the next video, try to prove that Prim's algorithm is correct. Can you find a proof similar to the one we saw for Kruskal?
  - [video: minimum spanning trees](https://youtu.be/aIlkwV-P4Kg?list=PLzZlJT-UOiwD1OSqOs00D0iW93BSJPjBR)
  - West/Chapter 1: Fundamental Concepts
    - You should read everything in these two chapters, including parts that are marked as "optional" in the book and solve all exercises.
  - West/Chapter 2: Trees and Distance
  - Andreescu and Feng: solve advanced problem 31 to advanced problem 40

## week 6 tutorial

- time: 2024-10-07T18:00:00+08:00/2024-10-07T18:50:00+08:00
- topic: tree-based algorithms, Huffmman coding
- [questions/2024-10-07/tutorial](questions/2024-10-07%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/4CPfs1XUg_w)
  - West/Section 2.3: Optimization and Trees
  - [video: Huffman coding and Huffman trees](https://youtu.be/JsTptu56GM8)
  - [video: Huffman coding example](https://youtu.be/apcCVfXfcqE)
  - [recommended video: Huffman coding + code](https://youtu.be/AwsNoQKcHg0)
  - [recommended video: dynamic programming on trees](https://youtu.be/tzuJeiGJvYY)

## week 6 lecture 2

- time: 2024-10-09T09:00:00+08:00/2024-10-09T11:20:00+08:00
- [questions/2024-10-09](questions/2024-10-09.md)
- [week 6 problem set](questions/week%206%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/wW0qSd3gQd8)
  - [video: BFS visualized and explained](https://youtu.be/xlVX7dXLS64)
  - [video: Dijkstra's algorithm](https://youtu.be/GazC3A4OQTE)
  - [video: strongly connected components and Dijkstra's algorithm](https://youtu.be/GUQjzYOfTgY?list=PLzZlJT-UOiwD1OSqOs00D0iW93BSJPjBR)
  - [video: matchings](https://youtu.be/chdr2aj4FUc)
  - [video: maximal and maximum matchings](https://youtu.be/bOJC93XxoFc)
  - [video: matchings and augmenting paths](https://youtu.be/IQZEURSSr30)
  - [video: incremental improvement – matching](https://youtu.be/8C_T4iTzPCU)
- assignments: [homework 6](assignments/homework%206/submission.tex)

## week 6 TA session

- time: 2024-10-11T19:00:00+08:00/2024-10-11T19:50:00+08:00
- topic: solving weekly problem set 4
- [questions/2024-10-11](questions/2024-10-11.md)
- [week 4 problem set](questions/week%204%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/jIsRmWzacfI)

## week 7 lecture

- time: 2024-10-14T10:30:00+08:00/2024-10-14T11:20:00+08:00
- [questions/2024-10-14/lecture](questions/2024-10-14%20lecture.md)

## week 7 tutorial

- time: 2024-10-14T18:00:00+08:00/2024-10-14T18:50:00+08:00
- [questions/2024-10-14/tutorial](questions/2024-10-14%20tutorial.md)

## week 7 lecture 2

- time: 2024-10-16T09:00:00+08:00/2024-10-16T11:20:00+08:00
- [questions/2024-10-16](questions/2024-10-16.md)
- [week 7 problem set](questions/week%207%20problem%20set.md)
