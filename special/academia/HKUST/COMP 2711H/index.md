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

## children

- [questions](questions/questions.md)

## assessments

- [homework 1](assignments/homework%201/submission.md): 10/10
- [homework 2](assignments/homework%202/submission.md): 7.5/10 → 9/10
- [homework 3](assignments/homework%203/submission.md): 9/10
- [homework 4](assignments/homework%204/submission.md): 8/10 → 10/10

## week 1 lecture

- datetime: 2024-09-02T09:00:00+08:00/2024-09-02T10:20:00+08:00
- topic: propositional logic
- course logistics
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ propositional calculus](../../../../general/propositional%20calculus.md#propositional%20calculus)
    - proposition ::@:: A declarative statement that is either true (1) or false (0). No third value is possible. Typically it is represented by _p_, _q_, _r_, and so forth.
  - [truth table](../../../../general/truth%20table.md) ::@:: A table representing a boolean function. There are $n + 1$ columns, where the first $n$ columns are the inputs of the boolean function, while the last column is the output of the boolean function. There are $2^n$ rows, representing all possible combinations of the $n$ inputs mapping to the corresponding $2^n$ outputs.
    - [§ truth table](../../../../general/truth%20table.md#truth%20table)
  - boolean algebra operations ::@:: An operation that takes and connects one or more propositions. These operations can be chained.
    - negation (not) ::@:: $\lnot p$: $$\begin{aligned} (0) & \mapsto 1 \\ (1) & \mapsto 0 \end{aligned}$$
    - disjunction (or) ::@:: $p \lor q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 1 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - conjunction (and) ::@:: $p \land q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 0 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - implication (if-then) ::@:: $p \rightarrow q$: $$\begin{aligned} (0, 0) & \mapsto 1 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$
    - boolean algebra operations / order of operations ::@:: $\lnot$ > $\lor, \land$ > $\rightarrow$
  - [tautology](../../../../general/tautology%20(logic).md) (true) ::@:: A proposition that is always true, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ tautology](../../../../general/tautology%20(logic).md#tautology)
  - [contradiction](../../../../general/contradiction.md) (false) ::@:: A proposition that is always false, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ contradiction](../../../../general/contradiction.md#contradiction)
  - propositional calculus / real life application ::@:: Consider making a one bit half adder. You want: $$\begin{aligned} 0 + 0 & = 0 \\ 1 + 0 & = 1 \\ 0 + 1 & = 1 \\ 1 + 1 & = 0 \end{aligned}$$. This can be expressed as $$\begin{aligned} \text{sum of products: } & (a \land \lnot b) \lor (\lnot a \land b) \\ \text{product of sums: } & (\lnot a \lor \lnot b) \land (a \lor b) \end{aligned}$$. This is also known as the exclusive-or (xor) operation.
  - [logical equivalence](../../../../general/logical%20equivalence.md) ::@:: Two propositions have the same truth values, no matter how the atomic propositions (terms with no operations) are assigned. One simple way to prove it is via a truth table and compare whether the rows are equivalent.
    - [§ logical equivalence](../../../../general/logical%20equivalence.md#logical%20equivalence)
    - [§ relation to material equivalence](../../../../general/logical%20equivalence.md#relation%20to%20material%20equivalence) ::@:: Material equivalence is simply a proposition that says two propositions have the same truth values. It may be false or true. Two propositions are logically equivalent if the material equivalence between them is true, no matter how the atomic propositions (terms with no operations) are assigned.
    - [§ general logical equivalences](../../../../general/logical%20equivalence.md#general%20logical%20equivalences)
  - [conjunction/disjunction duality](../../../../general/conjunction_disjunction%20duality.md) ::@:: The dual (Amir calls it inverse proposition) of a proposition $p$ is denoted $p^d$, and is formed by replacing $\land$ by $\lor$, $\lor$ by $\land$, T by F, and F by T. The dual relates to the original proposition by $\lnot p \equiv \overline p^d$, where $\overline p$ is replacing all atomic propositions (propositions without $\land$, $\lor$, and $\lnot$) by their negations. This can be interpreted as negating the "output" of $p$, i.e. $\lnot p$ is the same as negating all "inputs" of its dual $p^d$, i.e. $\overline p^d$.
    - [§ conjunction/disjunction duality](../../../../general/conjunction_disjunction%20duality.md#conjunction%2Fdisjunction%20duality)
    - [§ negation is semantically equivalent to dual](../../../../general/conjunction_disjunction%20duality.md#negation%20is%20semantically%20equivalent%20to%20dual)
    - [§ further duality theorems](../../../../general/conjunction_disjunction%20duality.md#further%20duality%20theorems)
  - [rules of inference](../../../../general/rules%20of%20inference.md) ::@:: Rules that allows deducing a consequence to be true, given that zero or more premises are true.
    - [rules of inference](../../../../general/rules%20of%20inference.md) / motivation ::@:: To prove a proposition $X := h_1 \land \ldots \land h_n \rightarrow c$ is true, where $h_i$ are _atomic_ variables (terms with no operations), one could use a proof table, but this would require $2^n$ rows. We could instead use another proposition equivalent to $X$, denoted $Y := p_1 \land \ldots \land p_n \rightarrow c$ where $p_i$ are propositions (not necessarily atomic). Coupled with _rules of inference_, we can prove $X$ via proving $Y$.
    - rules of inference / _modus ponens_ ::@:: $$\begin{aligned} & p \rightarrow q \\ & \underline{p \phantom{\rightarrow q} } \\ & q & \end{aligned}$$
    - rules of inference / hypothetical syllogism ::@:: $$\begin{aligned} & p \rightarrow q \\ & \underline{q \rightarrow r} \\ & p \rightarrow r & \end{aligned}$$
    - rules of inference / _modus tollens_ (not to be confused with the related _contraposition_) ::@:: $$\begin{aligned} & p \rightarrow q \\ & \underline{\lnot q \!\!\!\! \phantom{\rightarrow q} } \\ & \lnot p & \end{aligned}$$
- materials
  - [lecture video](https://youtu.be/Iexw2Lg9BmI)
  - Grimaldi/Chapter 2: Fundamentals of Logic
  - [video: proofs](https://youtu.be/L3LMbpZIKhQ)

## week 1 tutorial

- datetime: 2024-09-02T18:00:00+08:00/2024-09-02T18:50:00+08:00
- topic: predicate logic, Peano's axioms
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ list of classically valid argument forms](../../../../general/propositional%20calculus.md#list%20of%20classically%20valid%20argument%20forms)
  - [rules of inference](../../../../general/rules%20of%20inference.md_
    - _modus ponens_
    - hypothetical syllogism
    - _modus tollens_
    - rules of inference / conjunction ::@:: $$\begin{aligned} & p \\ & \underline{q \phantom{\land q} } \\ & p \land q & \end{aligned}$$
    - rules of inference / disjunctive syllogism ::@:: $$\begin{aligned} & p \lor q \\ & \underline{\lnot p \!\!\!\! \phantom{\lor q} } \\ & q \end{aligned}$$
    - rules of inference / transposition (with $F$ as the consequent) ::@:: $$\begin{aligned} & \underline{\lnot p \rightarrow F} \\ & p \end{aligned}$$
    - rules of inference / simplification ::@:: $$\begin{aligned} & \underline{p \land q} \\ & p \end{aligned}$$
    - rules of inference / addition ::@:: $$\begin{aligned} & \underline{p \phantom{\lor q} } \\ & p \lor q \end{aligned}$$
    - rules of inference / importation (applied form) ::@:: $$\begin{aligned} & p \land q \\ & \underline{p \rightarrow (q \rightarrow r)} \\ & r \end{aligned}$$
    - rules of inference / constructive dilemma ::@:: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{p \lor r \phantom{s} } \\ & q \lor s \end{aligned}$$
    - rules of inference / destructive dilemma ::@:: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{\lnot q \lor \lnot s} \\ & \lnot p \lor \lnot r \end{aligned}$$
    - rules of inference / constructive dilemma (unapplied form, with the same consequent) ::@:: $$\begin{aligned} & p \rightarrow r \\ & \underline{q \rightarrow r \phantom{r \rightarrow r} } \\ & (p \lor q) \rightarrow r \end{aligned}$$
    - rules of inference / material equivalence (_modus ponens_) ::@:: $$\begin{aligned} & p \equiv q \\ & \underline{p \phantom{\equiv q} } \\ & q \end{aligned}$$
  - proof format ::@:: A proof consists of several lines. Each line, numbered, is a proof statement, which either states the premise or is a statement derived from previous statements (referenced using line numbers) by rules of inference. For example: $$\begin{aligned} 1. \quad & p \rightarrow r && (\text{premise}) \\ 2. \quad & p && (\text{premise}) \\ 3. \quad & r && (\text{from 1 and 2}) \end{aligned}$$.
- [first-order logic](../../../../general/first-order%20logic.md)
  - [§ first-order logic](../../../../general/first-order%20logic.md#first-logic%20logic)
  - [predicate](../../../../general/predicate%20(mathematical%20logic).md) ::@:: A statement that becomes a proposition when the one or more unknowns are replaced by specified values from the universe. The universe is the set of all possible values for the unknowns.
  - universal quantification ::@:: $\forall x \, p(x)$ means for all $x$ in the universe $p(x)$ is true. If the universe is empty, $\forall x \, p(x)$ is true for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to existential quantification by $$\lnot \forall x \, p(x) \equiv \exists x \, \lnot p(x)$$.
    - universal quantification / distributive law ::@:: It distributes over logical conjunctions: $$\forall x \, (p(x) \land q(x)) \equiv \forall x \, p(x) \land \forall x \, q(x)$$. But it does NOT distribute over logical disjunctions: $$\forall x \, (p(x) \lor q(x)) \leftarrow \forall x \, p(x) \lor \forall x \, q(x)$$ and only the converse (shown above) is true.
  - existential quantification ::@:: $\exists x \, p(x)$ means there is at least one $x$ in the universe that $p(x)$ is true. If the universe is empty, $\exists x \, p(x)$ is false for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to universal quantification by $$\lnot \exists x \, p(x) \equiv \forall x \, \lnot p(x)$$.
    - existential quantification / distributive law ::@:: It distributes over logical disjunctions: $$\exists x \, (p(x) \lor q(x)) \equiv \exists x \, p(x) \lor \exists x \, q(x)$$. But it does NOT distribute over logical conjunctions: $$\exists x \, (p(x) \land q(x)) \rightarrow \exists x \, p(x) \land \exists x \, q(x)$$ but the converse is not necessarily true.
- [Peano axioms](../../../../general/Peano%20axioms.md) ::@:: (The second-order formulation is used.) One, $0$ is a natural number. Two, if $n$ is a natural number, then $S(n)$ is a natural number. Third, if $S(n) = S(m)$, then $n = m$. Four, $S(n) \ne 0$ for all natural numbers $n \in \mathbb N$. Five, if $K$ is a set such that $0 \in K$, and for all natural numbers $n \in \mathbb N$, if $n \in K$ then $S(n) \in K$, then $K = \mathbb N$ (induction).
  - [§ Peano axioms](../../../../general/Peano%20axioms.md#Peano%20axioms)
  - [§ historical second-order formulation](../../../../general/Peano%20axioms.md#historical%20second-order%20formulation)
  - Peano axioms / 1st axiom motivation ::@:: This defines the starting $0$ as a natural number.
  - Peano axioms / 2nd axiom motivation ::@:: This defines a successor function $S$ that can generate more natural numbers. Equivalently, the natural numbers are closed under $S$.
  - Peano axioms / 3rd axiom motivation ::@:: This makes the successor function injective (but not surjective, as $0$ is not in the image of the function).
  - Peano axioms / 4th axiom motivation ::@:: Coupled with the injective property, this makes the successor function never go back to the starting number $0$. Otherwise, the successor function can, at one point, loop back to $0$, and there will only be finitely many natural numbers.
  - Peano axioms / 5th axiom motivation ::@:: The 4 axioms above are insufficient to ensure that repeatedly applying $S$ on $0$ can generate all natural numbers. Indeed, an infinite successor chain starting from $0$ that does not contain all the natural numbers, with a finite circular successor chain, is compatible with the 4 axioms above. The 5th axiom simply states that the infinite successor chain starting from $0$ is the set of all natural numbers, excluding the situation above. This is also what makes mathematical induction possible.
- materials
  - [lecture video](https://youtu.be/X_SF_o9ZwmA)
  - Grimaldi/Chapter 2: Fundamentals of Logic
  - [video: Peano axioms](https://youtu.be/5zl2zBqNAHM)

## week 1 lecture 2

- datetime: 2024-09-04T09:00:00+08:00/2024-09-04T10:20:00+08:00
- topic: induction, well-ordering, infinite descent
- [Peano axioms](../../../../general/Peano%20axioms.md)
  - [§ defining arithmetic operations and relations](../../../../general/Peano%20axioms.md#defining%20arithmetic%20operations%20and%20relations)
  - [§ addition](../../../../general/Peano%20axioms.md#addition) ::@:: 2 rules: $\forall n; n + 0 = n$, $\forall n, m; n + s(m) = s(n + m)$. All other rules that you know of everyday addition can be derived from these rules. From this we can prove that addition is commutative ($\forall n, m; n + m = m + n$) and associative ($\forall n, m, o; (n + m) + o = n + (m + o)$).
  - [§ multiplication](../../../../general/Peano%20axioms.md#multiplication) ::@:: Assuming addition is defined, 2 rules: $\forall n, n \cdot 0 = 0$, $\forall n, m; n \cdot s(m) = n + n \cdot m$. All other rules that you know of everyday multiplication can be derived from these rules. From this we can prove that multiplication is commutative ($\forall n, m; n \cdot m = m \cdot n$) and associative ($\forall n, m, o; (n \cdot m) \cdot o = n \cdot (m \cdot o)$).
  - [§ inequalities](../../../../general/Peano%20axioms.md#inequalities) ::@:: Assuming addition is defined, the inequality $\le$ is defined as $$n \le m \equiv \exists x; n + x = m$$.
- [mathematical induction](../../../../general/mathematical%20induction.md)
  - [§ mathematical induction](../../../../general/mathematical%20induction.md#mathematical%20induction)
  - [§ description](../../../../general/mathematical%20induction.md#description)
  - [§ examples](../../../../general/mathematical%20induction.md#examples)
  - [§ example of error in the induction step](../../../../general/mathematical%20induction.md#example%20of%20error%20in%20the%20induction%20step)
  - [§ relationship to the well-ordering principle](../../../../general/mathematical%20induction.md#relationship%20to%20the%20well-ordering%20principle)
- [well-ordering principle](../../../../general/well-ordering%20principle.md) ::@:: Every _non-empty_ subset of the natural numbers (not integers) has a least element. Proofs using this are generally by contradiction. This is implied from induction (from Peano axioms) or infinite descent. However, the well-ordering principle does not imply induction (under the other Peano axioms), and so is not equivalent to induction.
  - [§ well-ordering principle](../../../../general/well-ordering%20principle.md#well-ordering%20principle)
- [proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md) ::@:: There are no infinite strictly decreasing sequences of natural numbers. Proofs using this are generally by contradiction, and involve constructing an infinite descent of natural numbers, which contradicts this. Another way is assuming a minimal solution to a problem exists, but then prove that it would lead to a smaller solution. This is equivalent to induction (from Peano axioms), and implies the well-ordering principle .
  - [§ proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md#proof%20by%20infinite%20descent)
- [questions/2024-09-04](questions/2024-09-04.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/xR3jmz5WdQ4)
  - [video: induction](https://youtu.be/z8HKWUWS-lA)
  - [video: 2+2=4](https://youtu.be/TQpHVtlXuyc)
  - [Mathematical Induction](https://www.sydney.edu.au/content/dam/students/documents/mathematics-learning-centre/mathematical-induction.pdf)

## week 2 lecture

- datetime: 2024-09-09T09:00:00+08:00/2024-09-09T10:20:00+08:00
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

- datetime: 2024-09-09T18:00:00+08:00/2024-09-09T18:50:00+08:00
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

- datetime: 2024-09-11T09:00:00+08:00/2024-09-11T10:20:00+08:00
- topic: counting, permutations, combinations, balls and walls
- [combinatorial principles](../../../../general/combinatorial%20principles.md) ::@:: principles commonly used to solve combinatorial problems: rule of sum, rule of product, permutation, combination, ...
  - [§ combinatorial principles](../../../../general/combinatorial%20principles.md#combinatorial%20principles)
  - [§ rule of sum](../../../../general/combinatorial%20principles.md#rule%20of%20sum) ::@:: Also known as the principle of addition or case work principle. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ + _B_ ways to do either one thing.
  - [§ rule of product](../../../../general/combinatorial%20principles.md#rule%20of%20product) ::@:: Also known as the principle of multiplication. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ \* _B_ ways to do both things.
- [permutation](../../../../general/permutation.md) ::@:: the arrangement of $k$ things from $n$ things (order matters), calculated by $$P(n, k) = \frac {n!} {(n - k)!}$$
- [combination](../../../../general/combination.md) ::@:: choosing $k$ things from $n$ things (order does not matter), calculated by $$C(n, k) = \binom n k = \frac {n!} {(n - k)! k!}$$
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

- datetime: 2024-09-16T09:00:00+08:00/2024-09-16T10:20:00+08:00
- topic: solving counting problems
- [permutation](../../../../general/permutation.md)
- [combination](../../../../general/combination.md)
- [questions/2024-09-16/lecture](questions/2024-09-16%20lecture.md)
- materials
  - [lecture video](https://youtu.be/YyNe0mgrK1A)
  - Chen and Koh/Chapter 1: Permutations and Combinations (very important)
  - Andreescu and Feng: solve problem 1 to problem 24

## week 3 tutorial

- datetime: 2024-09-16T18:00:00+08:00/2024-09-16T18:50:00+08:00
- topic: more counting
- assignments: [homework 1](assignments/homework%201/submission.md)
- [permutation](../../../../general/permutation.md)
- [combination](../../../../general/combination.md)
- [questions/2024-09-16/tutorial](questions/2024-09-16%20tutorial.md)
- [week 3 problem set](questions/week%203%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/p0Lb0odJCfU)
  - Andreescu and Feng: solve problem 25 to problem 51

## week 3 lecture 2

- datetime: 2024-09-18T09:00:00+08:00/2024-09-18T10:20:00+08:00
- status: unscheduled, public holiday: Day after Mid-Autumn Festival

## week 3 TA session

- datetime: 2024-09-20T19:00:00+08:00/2024-09-20T19:50:00+08:00
- topic: solving weekly problem set 1
- [questions/2024-09-20](questions/2024-09-20.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/wbck_JlX9C4)

## week 4 lecture

- datetime: 2024-09-23T09:00:00+08:00/2024-09-23T10:20:00+08:00
- topic: principle of inclusion and exclusion
- [inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md)
  - [§ inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md#inclusion–exclusion%20principle)
  - Look at other sections as well, especially the examples.
- [questions/2024-09-23/lecture](questions/2024-09-23%20lecture.md)
- materials
  - [lecture video](https://youtu.be/c0fb16fNpXY)
  - Chen and Koh/Chapter 2: Binomial Coefficients
  - Chen and Koh/Chapter 4: Inclusion–Exclusion
  - [video: inclusion–exclusion example](https://youtu.be/51-b2mgZVNY)
  - [video: 3-set PIE](https://youtu.be/VQmWJXeevfM)
  - [video: counting using PIE](https://youtu.be/rBLuvLDutdY)

## week 4 tutorial

- datetime: 2024-09-23T18:00:00+08:00/2024-09-23T18:50:00+08:00
- topic: generalized principle of inclusion and exclusion
- [inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md)
  - [§ inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md)
  - [§ formula generalization](../../../../general/inclusion–exclusion%20principle.md#formula%20generalization)
  - Look at other sections as well, especially the examples.
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

- datetime: 2024-09-25T09:00:00+08:00/2024-09-25T10:20:00+08:00
- topic: pigeonhole principle
- pigeonhole principle ::@:: Let _f_ be a mapping from a finite nonempty set _A_ to another nonempty finite set _B_ such that |_A_| > _k_|_B_| for some natural number _k_. Let _f_<sup>-1</sup> be the inverse mapping from _B_ to the power set of _A_. Then there is an element _b_ in _B_ such that |_f_<sup>-1</sup>(_b_)| ≥ _k_ + 1.
  - pigeonhole principle / proof ::@:: Prove by contradiction. Using the definitions above, assume every element _b_ in _B_ has the property |_f_<sup>-1</sup>(_b_)| < _k_ + 1. Then the maximum cardinality (size) of _A_ is _k_|_B_|. But this contradicts |_A_| > _k_|_B_|.
  - pigeonhole principle / in practice ::@:: The pigeonhole principle is straight forward. However, the difficult part is identifying the pigeons and holes, which is nontrivial.
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

- datetime: 2024-09-27T17:00:00+08:00/2024-09-27T17:50:00+08:00
- topic: solving weekly problem set 2
- [questions/2024-09-27](questions/2024-09-27.md)
- [week 2 problem set](questions/week%202%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/7VN1ZCUpKKk)

## week 5 lecture

- datetime: 2024-09-30T09:00:00+08:00/2024-09-30T10:20:00+08:00
- topic: graphs, trees, paths, walks
- [graph theory](../../../../general/graph%20theory.md)
  - graph theory / graph ::@:: A __graph__ is denoted $G = (V, E)$, where $V$ is a finite set of __vertices__ and _E_ is a finite set of __edges__.
  - graph theory / edge ::@:: An __edge__ in a graph $G = (V, E)$ is a two-element set $\set{u, v} \subseteq V$, which represents a connection between the vertex _u_ and _v_.
  - graph theory / loop ::@:: A __loop__ is an edge connecting a vertex to itself, i.e. $\set{u, u}$. But in this course, we do not consider graphs with this case. Graphs without this case (and without _multiple edges_) are called __simple__.
  - graph theory / neighbor ::@:: If an edge connects two vertices, the two vertices are said to be __neighbors__ of each other.
  - graph theory / complement of a graph ::@:: The __complement of a graph__ $G = (V, E)$ is denoted $\overline G = (V, \overline E)$, where $\set{u, v} \in \overline E \equiv \set{u, v} \notin E$. That is, the graph has the same vertices, but for all possible edges between the vertices in the graph, if the edge is present in $G$ then it is not in $\overline G$, and vice versa.
  - graph theory / subgraph ::@:: A graph is a __subgraph__ of another graph $G$ if its vertices are a subset of those of $G$ and its edges are also a subset of those of $G$.
  - graph theory / isomorphism ::@:: An __isomorphism__ between two graphs is a bijective mapping of vertices between them that preserves the edges. Informally, the graphs are the same if we do not care about the identities of the vertices.
  - graph theory / degree ::@:: The __degree__ of a vertex is the number of other vertices connecting to it. <p> A obvious theorem: the sum of degrees of all vertices is twice the number of edges.
  - graph theory / adjacency matrix ::@:: The __adjacency matrix__ of a graph with _n_ vertices is a _n_-by-_n_ matrix _A_, where $$A_{ij} = \begin{cases} 1 & \text{if }\set{i, j} \in E \\ 0 & \text{otherwise} \,. \end{cases}$$
  - graph theory / walk ::@:: A __walk__ is a sequence of alternating vertices and edges. The sequence starts and ends with a vertex. The edges connects the two vertices adjacent to it in the sequence. Informally, you are walking on the graph.
  - graph theory / trail ::@:: A __trail__ is a walk with no repeated edges.
  - graph theory / path ::@:: A __path__ is a walk with no repeated vertices. In the same graph, paths are a subset of trails. In particular, trails include cycles while paths exclude them.
  - graph theory / closed walk, closed trail ::@:: A walk or trail is __closed__ if it starts and ends at the same vertex.
  - graph theory / cycle ::@:: A __cycle__ is a closed walk with no repeat vertices, ignoring the ending vertex (which is the same as the starting vertex).
- theorem: number of possible edges in a graph ::@:: There are $\binom n 2$ such edges in a graph of _n_ vertices. <p> This is trivial to prove.
- theorem: non-closed walk contains path, closed walk contains cycle ::@:: Any non-closed walk contains a path. <p> An algorithm (which also proves the theorem) exists for doing so: If a vertex appears two or more times in a walk, remove the sequence from the first appearance of the vertex (exclusive) to its appearance. The resulting walk is still valid. When there are no more repeated vertices, then the walk is also a path. <p> We can prove that any closed walk contains a cycle using the same steps.
- graph theory
  - graph theory / connected vertices ::@:: Two vertices in a graph are __connected__ if there is a path from one to the other.
  - graph theory / connected graph ::@:: A graph is __connected__ if every pair of vertices in it are connected.
  - graph theory / connected component (CC) ::@:: A __connected component__ (__CC__) of a graph _G_ is a __maximal connected subset__ of vertices. It is a subgraph of the graph _G_ to which no vertex of the graph _G_ can be added and make the subgraph still connected. More intuitively and informally, it is the connected subgraphs the graph _G_ is made of.
  - graph theory / tree ::@:: A __tree__ is (1) a connected graph, (2) has _n_ - 1 edges, and (3) has no cycles. The definition actually only requires two properties out of the properties (1), (2), (3), since the third property can be proven from any other two.
- theorem: minimum number of connected components (CC) ::@:: A graph has at least |_V_| - |_E_| connected components. <p> To prove this, consider the |_V_| vertices without any edges. There are _V_ CCs, by definition. Now consider the effect of adding an edge. This decreases the number of CCs by at most 1. After adding |_E_| edges, the number of CCs has decreased by at most |_E_|.
  - theorem: minimum number of connected components (CC) / corollary: connected graph ::@:: Every connected graph has |_E_| ≥ |_V_| - 1.
- theorem: definition of a tree ::@:: Given three properties of a tree: (1) a connected graph, (2) has _n_ - 1 edges, and (3) has no cycles. Any two properties implies the third property. <p> To prove this, consider adding |_E_| edges one by one to a graph of |_V_| vertices with no edges, and make use of the theorem relating the number of connected components to |_V_| - |_E_|.
- graph theory
  - graph theory / [cut](../../../../general/cut%20(graph%20theory).md) ::@:: A __cut__ is a partition of the vertices of a graph into two disjoint subsets. Any cut determines a __cut-set__, the set of edges that have one endpoint in each subset of the partition. These edges are said to __cross__ the cut.
- theorem: connected graph, one-edge cut-set, cycle ::@:: If a cut-set of a connected graph consists of one edge only, the edge is not part of any cycle. The converse also holds: If an edge is not part of any cycle, it is a cut-set. <p> To prove theorem and its converse, prove by contradiction.
- [questions/2024-09-30/lecture](questions/2024-09-30%20lecture.md)
- materials
  - [lecture video](https://youtu.be/rmk2RCszCt4)
  - West/Section 1.1: What is a Graph?
    - Most of the theorems we proved in class were from these sections, but the proofs are often different. So, you should read the book and also solve the exercises.
  - West/Section 1.2: Paths, Cycles, and Trails
  - [video playlist: introduction to graph theory](https://youtu.be/C7YrMRdLkqo?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS)
  - [video playlist: watch lectures 1 to 4](https://youtube.com/playlist?list=PLoAxxVQYIwM73zRO5gZL0exCw70O8ZlvJ)

## week 5 tutorial

- datetime: 2024-09-30T18:00:00+08:00/2024-09-30T18:50:00+08:00
- topic: more theorems on graphs and trees
- graph theory
  - graph theory / leaf ::@:: A __leaf__ is a vertex of degree 1.
- theorem: minimum number of leaves in a tree ::@:: Every tree on _n_ ≥ 2 vertices has at least 2 leaves. <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that vertices cannot be added to the path ends without either making the path longer or violate the graph being a tree.
- theorem: number of possible graphs ::@:: There are $2^{\binom {\lvert V \rvert} 2}$ possible graphs. <p> To prove this, we can select whether to put an edge for each of the $\binom {\lvert V \rvert} 2$ possible edges.
- [Prüfer sequence](../../../../general/Prüfer%20sequence.md) ::@:: A sequence of |_V_| - 2 nodes to uniquely encode all possible trees on |_V_| vertices. This means encoding a Prüfer sequence from a tree in the domain of all possible trees is a bijection.
  - theorem: number of possible trees ::@:: There are $\lvert V \rvert^{\lvert V \rvert - 2}$ possible trees. <p> To prove this, we can use the Prüfer sequence, which can uniquely encode all possible trees. The length of a Prüfer sequence is _n_ - 2 and there are _n_ possible choice for each element. <p> The Prüfer sequence also provides a way to find the number of possible trees with restrictions. For example, the number of possible trees on a complete bipartite graph, with _x_ and _y_ vertices in the two partitions, is $x^{y - 1} y^{x - 1}$.
    - theorem: number of possible trees / [combinatorial proof](../../../../general/combinatorial%20proof.md#the%20difference%20between%20bijective%20and%20double%20counting%20proofs) ::@:: We can also use a combinatorial proof to prove the above identity. See the linked section.
  - Prüfer sequence / encoding ::@:: Assume the nodes are labelled from 1 to |_V_|. Let the Prüfer sequence be empty. Find the leaf with the smallest node. Append the node of the leaf's only neighbor to the Prüfer sequence. Remove the leaf. Repeat until there is only 1 edge (or 2 vertices) left.
  - Prüfer sequence / properties ::@:: The number of times a node appearing in the Prüfer sequence is its degree minus 1. As a special case, nodes that are not in the Prüfer sequence are leaves.
  - Prüfer sequence / decoding ::@:: Let there be a sequence _N_ of _n_ labelled vertices and a Prüfer sequence. <p> Find the leaf (a node that is not in the Prüfer sequence) with the smallest label in the sequence _N_. Join it with the first node in the Prüfer sequence. Remove said leaf from the sequence _N_ and the first node from the Prüfer sequence. This may make a node in _N_ that was not a leaf now a leaf. <p> Repeat until there are only 2 nodes left in the sequence _N_. Connect those 2 nodes to get the tree.
- theorem: connected graph, one-vertex cut-set (different from the edge-based cut-set above) ::@:: Every connected graph with |_V_| ≥ 2 has at least two non-cut vertices (vertices that when removed from the graph, will not result in two separate connected graphs). <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that vertices at the path ends cannot be removed such that any two neighbors of them become disconnected, which proves the theorem.
- graph theory
  - graph theory / even cycle ::@:: An __even cycle__ is a cycle with an even number of vertices.
  - graph theory / odd cycle ::@:: An __odd cycle__ is an cycle with an odd number of vertices.
- theorem: odd closed walk contains an odd cycle ::@:: Every odd closed walk contains an odd cycle. <p> To prove this, consider a closed odd walk, with the start being the same as the end. If there are no repeated vertices in between, it is already an odd cycle. Otherwise, we try to remove contagious subsequences in between two repeated vertices of it so that it becomes an odd cycle. If we can keep removing an even number of edges, we will eventually get an odd cycle. If we need to remove an odd number of edges at any point, said removed edges are an odd cycle itself.
- graph theory
  - graph theory / [bipartite graph](../../../../general/bipartite%20graph.md) ::@:: A __bipartite graph__ is a graph whose vertices can be divided into two disjoint and independent sets _U_ and _V_, that is, every edge connects a vertex in _U_ connects to one in _V_. Equivalently, the graph does not contain any odd-length cycles.
    - theorem: bipartite graph, no odd cycles ::@:: A graph is bipartite iff it has no odd cycles. <p> It is easy to prove a bipartite graph has no odd cycles by considering trying to form a cycle in it. <p> The converse is more difficult. But we can show its existence by an algorithm: Start from an arbitrary vertex, then put it into _X_. Put its neighbors into _Y_. Then put the neighbors of its neighbors, ignoring those already visited into _X_. Its correctness can be proven by consider that between any two distinct vertices, either all walks between them are odd non-closed walks or all walks between them are even non-closed walks. This shows the algorithm can assign all vertices consistently to either _X_ or _Y_.
- theorem: minimum degree, cycle ::@:: If the minimum degree of any vertex is 2, the graph has a cycle. <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that a neighbor of a path end cannot be outside the path.
- theorem: maximum degree, cycle ::@:: If the maximum degree of any vertex is 2, every connected component is either a cycle or path. <p> To prove this, use the extremal principle on the possible paths for each connected component. In particular, assert the existence of a longest path for each connected component. Then show that the path cannot have edges added to it without making it a cycle.
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

- datetime: 2024-10-02T09:00:00+08:00/2024-10-02T10:20:00+08:00
- topic: even more theorems on graphs and trees
- theorem: even degree, cycle ::@:: If every vertex has an even degree, the edge set is a disjoint union of cycles. <p> To prove this, we can apply induction on the number of edges. The base cases are 0 and 1 edges. The induction step can be proved by starting from a vertex and show that it eventually ends at the same vertex; remove that cycle and the induction hypothesis can be applied.
- graph theory
  - graph theory / [Eulerian path](../../../../general/Eulerian%20path.md), Eulerian circuit ::@:: The first one is a walk that passes over every edge exactly once. The second one additionally requires the walk to be closed.
    - theorem: connected graph, even degree, Eulerian circuit ::@:: A connected graph has an Eulerian circuit iff every vertex has an even degree. <p> To prove that an Eulerian circuit implies every vertex has an even degree, consider the sequence of vertices and edges in an Eulerian circuit. (Joining the sequence at the ends to make it circular may help.) Consider the every appearance of a vertex in the sequence. <p> To prove the converse, decompose the graph into a disjoint union of edge sets of cycles. Then an Eulerian circuit can be constructed from it. Induction on the number of disjoint edge sets of cycles may be used.
  - graph theory / [Hamiltonian path](../../../../general/Hamiltonian%20path.md), Hamiltonian cycle ::@:: The first one is a walk that visits all vertices exactly once. The second one additionally requires the walk to be closed.
- theorem: minimum bipartite subgraph ::@:: A graph has a bipartite subgraph with at least |_E_| / 2 edges. <p> To prove this, show that we can always construct such a subgraph. Partition all vertices of a graph arbitrary into two sets. The edges that has an endpoint in both sets form a bipartite subgraph. Then consider any vertex in the graph. The vertex has some edges to its own set and the remaining edges to the other set. The remaining edges to the other sets is in the bipartite subgraph. If the edges to its own set is more than the edges to the other set, we can move the vertex to the other set such that these two sets of edges are swapped. Finally, we obtain a configuration where every vertex has edges to the other set as many as that to its own set. So the bipartite graph includes at least |_E_| / 2 edges. <p> A hint of the above method comes from the division by 2... which hints at some greater than or equal to argument.
- graph theory
  - graph theory / degree sequence ::@:: A __degree sequence__ is the non-increasing sequence of an undirected graph's vertex degrees. (Amir uses non-decreasing for some reason... but it should be equivalent).
    - theorem: degree sequence, not necessarily simple graph ::@:: An arbitrary sequence is the degree sequence of a not necessarily simple (simple: no multiple edges, no self-loops) graph if the sum of the arbitrary sequence is even. <p> To prove it, pair up vertices with odd degrees together to make them even. There must be an even number of them. Then add a lot of self-loops to satisfy the degree sequence. <p> Note: Such a degree sequence is graphic if it is the degree sequence of a _simple_ graph. It may be found using the Havel–Hakimi algorithm, a greedy algorithm.
- [Havel–Hakimi algorithm](../../../../general/Havel–Hakimi%20algorithm.md) ::@:: Let there be an arbitrary sequence _A_. Sort the sequence in non-increasing order. Remove the first element, which has the value _s_. Decrement 1 from the first _s_ element of the sequence. This produces a new sequence _A_'. Repeat the above (including the sorting). If the sequence is graphic, then it must eventually reduce to an sequence of zeros. <p> _A_ is graphic iff _A_' is graphic. Proving this property proves the algorithm. <p> The forward and backward cases are kind of easy to prove: If _A_ is graphic, the above operations corresponds to removing a vertex with maximum degree. If the vertex's edges connect to the _s_ vertices with the max _s_ degrees, then the graph is represented by _A_'. If not, we note that any degree surplus and deficit can always be corrected to obtain a graph represented by _A_'. <p> If _A_' is graphic, the inverse of the above operation corresponds to adding a vertex and connecting them to a graph represented by _A_'.
- theorem: tree, unique paths ::@:: A graph is a tree iff there are unique paths between every pair of vertices. To prove this, make use of the three properties of a tree. <p> If a graph is a tree, consider any pair of vertices. A path must exist, or otherwise the tree is not connected. But there must not be more than a path between them, or otherwise a closed walk exist, which implies the tree has a cycle. <p> If there are unique paths between every pair of vertices, the graph is connected. There are also no cycles, or otherwise there is a pair of vertices with more than a path. So the graph is a tree.
- theorem: connected graph, subgraph, tree ::@:: Every _connected_ graph has a tree subgraph connecting all vertices in the graph. The tree subgraph is known as a _spanning tree_. <p> Apply depth-first search (DFS) to visit all vertices. Show that the edges used by DFS is a tree. <p> The graph is connected, trivially. To show that the graph has _n_ - 1 edges, note that DFS uses an edge per vertex visited except for the stating vertex. To show that the graph has no cycles, note that every edge only ever connects a vertex at distance _d_ to _d_ + 1, which is monotonic.
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

- datetime: 2024-10-04T17:00:00+08:00/2024-10-04T17:50:00+08:00
- topic: solving weekly problem set 3
- [questions/2024-10-04](questions/2024-10-04.md)
- [week 3 problem set](questions/week%203%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/VDPaNbb3KVo)
  - [video: recurrence for number of partitions](https://youtu.be/F4zYDx-EfZI)

## week 6 lecture

- datetime: 2024-10-07T09:00:00+08:00/2024-10-07T10:20:00+08:00
- topic: minimum spanning trees, directed graphs, DAGs
- theorem: adding an edge, tree, cycle ::@:: Adding an edge to a tree creates exactly one cycle. <p> Recall that in a tree, every pair of vertex has an unique path. Adding an edge to any pair of vertex makes this unique path a cycle. <p> However, there is only one cycle created. We note that any cycles created must pass through the new edge, because there were no cycles before we have added the edge. If there were multiple cycles created, then the pair of vertex we have added an edge to would have multiple paths before adding the edge.
- graph theory
  - graph theory / weighted graph ::@:: A __weighted graph__ is a graph with an function that maps every edge to a real number. Or, informally, every edge has a real number as its weight.
  - graph theory / spanning tree ::@:: A __spanning tree__ of a graph is a tree that connects all vertices in the graph. We have already shown this must exist for a _connected_ graph by a theorem before.
  - graph theory / minimum spanning tree ::@:: A __minimum spanning tree__ of a weighted graph is the spanning tree of a weighted graph with the least total weight in its vertices. <p> There are two greedy algorithms for this that we will learn: Kruskal's algorithm and Prim's algorithm.
- [Kruskal's algorithm](../../../../general/Kruskal's%20algorithm.md) ::@:: Sort the edges in non-decreasing weight. For each edge, add it to the resulting tree if adding it does not create a cycle, otherwise discard the edge. Repeat until all edges are processed. <p> To prove that the resulting edges spans all vertices given the graph is connected, prove by contradiction. If the resulting edges do not connect all vertices, that means there are multiple connected components in the resulting tree. But since the original graph is connected, there are edges connecting in between the multiple connected components which are discarded. Consider the first such edge examined by the algorithm. It should not be discarded, because adding it must not create a cycle. <p> To prove that the resulting edges is a minimum spanning tree (MST) given the graph is connected, also prove by contradiction. If the resulting edges are not a MST, there is a different selection of edges that is a MST. Consider the first edge _e_ examined by the algorithm that is in the resulting edges but not in the MST. Add said edge to the MST to add exactly one cycle. Since the resulting edges form a tree and have no cycles, there is an edge _e_' in the cycle that is not in the resulting edges. Remove that edge to get another spanning tree. _e_ must be examined before _e_' because otherwise _e_ instead of _e_' would have been discarded for forming a cycle. The above operations replace the edge _e_' with _e_, which must not increase the total weight by the above. This means either the MST is not minimum, a contradiction; or the MST can be eventually be made into the resulting edges without decreasing its weight by repeating the above arguments, so the resulting edges are also a MST.
- [Prim's algorithm](../../../../general/Prim's%20algorithm.md) ::@:: Start with an empty tree. Add an arbitrary vertex to it. Grow the tree by one edge at a time: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and add it to the tree. Repeat until all vertices are added. <p> The resulting tree is obviously a tree. To prove that the resulting tree is also a minimum spanning tree (MST) given that the graph is connected, prove by contradiction. Assume the resulting tree is not a MST. Then consider each step of the algorithm. Either the algorithm adds an edge that is in the MST or not. Consider the first instance when the algorithm adds an edge _e_ that is not in the MST. Let _V_ be the set of vertices in the tree before the algorithm adds the edge _e_, noting that _V_ is a subgraph of the MST. The edge _e_ connects a vertex _v_ in _V_ and another vertex _u_ not in _V_. Since MST is a spanning tree and _V_ is a subgraph of the MST, there is also an edge _f_ of MST that connects the vertex _v_ and another vertex not in _V_ that is in the path from _v_ to _u_. Edge _e_ and _f_ are not the same, otherwise the edge added is in the MST. The weight of edge _f_ must be not less than _e_ or otherwise the algorithm would have added edge _f_ instead. Consider adding the edge _e_ to the MST. This creates exactly one cycle. Edge _f_ must be in the cycle because both edge _e_ and edge _f_ are in paths from _v_ to _u_. Removing _f_ breaks this cycle, so the resulting graph is another spanning tree. So we have effectively replaced edge _f_ in the MST with edge _e_ to get another spanning tree. But since the weight of _f_ is not less than _e_, the new spanning tree either has equal or smaller weight. This means either the MST is not minimum, a contradiction; or the MST can be eventually be made into the resulting tree without decreasing its weight by repeating the above arguments, so the resulting tree is also a MST. <p> The argument, especially the last part, is similar to that for Kruskal's algorithm.
- graph theory
  - graph theory / directed graph ::@:: __Directed graph__ is a graph, but the edges are the two-element tuples $(u, v)$ instead of the two-element set $\set{u, v}$. The tuple means an arrow connects from the vertex _u_ to vertex _v_.
  - graph theory / strongly connected ::@:: Two vertices _u_ and _v_ in a graph is __strongly connected__ if there is a path from _u_ to _v_ and from _v_ to _u_. <p> For undirected graphs, two vertices are strongly connected if there is a path between from _u_ to _v_, because we can easily reverse the path to get a path from _v_ to _u_. For directed graphs, however, this is not the case.
  - graph theory / strongly connected component (SCC) ::@:: A __strong connected component__ (__SCC__) is a connected component (CC) such that every pair of vertices are strongly connected.
- theorem: directed simple graph, cycle, strongly connected component ::@:: A directed simple graph (no multiple edges, no self-loops) has no cycles iff every vertex is a strongly connected component by itself. <p> To prove this and its converse, use contradiction.
- graph theory
  - graph theory / [topological ordering](../../../../general/topological%20sorting.md) ::@:: A __topological sort__ or __topological ordering__ of a directed graph is a linear ordering (permutation) of its vertices such that for every directed edge (_u_, _v_) from vertex _u_ to vertex _v_, _u_ comes before _v_ in the ordering.
  - graph theory / [directed acyclic graph](../../../../general/directed%20acyclic%20graph.md) (DAG) ::@:: A __directed acyclic graph__ (__DAG__) is a directed graph with no directed cycles.
- theorem: directed acyclic graph, topological ordering ::@:: A directed graph is a directed acyclic graph (DAG) iff the graph has a topological ordering. <p> To prove this and is converse, use contradiction. Two lemmas below and depth-first search (DFS) are useful here.
  - lemma: directed graph and minimum out-degree ::@:: If the out-degree of every vertex of a directed graph is 1, then there is a directed cycle. <p> To prove this, we can keep moving to new nodes if there are no directed cycles.
  - lemma: directed graph and minimum in-degree ::@:: If the in-degree of every vertex of a directed graph is 1, the there is a directed cycle. <p> To prove this, we can keep moving to new nodes backwards if there are no directed cycles.
- directed acyclic graph game ::@:: Two players start at a vertex of a loopless directed acyclic graph. In each turn, each player can move the current vertex through one outgoing edge. A player who cannot make a move loses. <p> We can prove the game always ends because there are no directed cycles. Also, we can also mark each vertex as a winning and losing position, starting from vertices with 0 out-degrees as losing, and alternating between winning and losing (with the winning position overriding the losing position) as we go through the directed edges in reverse.
- graph theory
  - graph theory / rooted tree ::@:: A __rooted tree__ is a tree with a vertex designated as the root. We can keep the tree undirected, or make it directed such that any other vertices can be reached from the root following the arrows.
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

- datetime: 2024-10-07T18:00:00+08:00/2024-10-07T18:50:00+08:00
- topic: tree-based algorithms, Huffmman coding
- graph theory
  - graph theory / [independent set](../../../../general/independent%20set%20(graph%20theory).md) ::@:: An __independent set__ is a set of vertices in a graph, no two of which are adjacent.
- [Huffman coding](../../../../general/Huffman%20coding.md) ::@:: A particular type of optimal prefix code (no code is a prefix of any other code) that is commonly used for lossless data compression.
  - Huffman coding / algorithm ::@:: Suppose there are _n_ words that appears _w_<sub>_i_</sub> times. Keep merging 2 words that appears least frequently to become one word with their appearance frequencies combined. Keep track of how the words are merged and represent it as a tree. <p> The resulting tree is a binary tree for its Huffman coding. The leaves represent each word. The route it takes to reach a word is the Huffman coding for that word.
- [questions/2024-10-07/tutorial](questions/2024-10-07%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/4CPfs1XUg_w)
  - West/Section 2.3: Optimization and Trees
  - [video: Huffman coding and Huffman trees](https://youtu.be/JsTptu56GM8)
  - [video: Huffman coding example](https://youtu.be/apcCVfXfcqE)
  - [recommended video: Huffman coding + code](https://youtu.be/AwsNoQKcHg0)
  - [recommended video: dynamic programming on trees](https://youtu.be/tzuJeiGJvYY)

## week 6 lecture 2

- datetime: 2024-10-09T09:00:00+08:00/2024-10-09T10:20:00+08:00
- topic: distance, shortest paths, matchings
- assignments: [homework 2](assignments/homework%202/submission.md)
- graph theory
  - graph theory / distance ::@:: The __distance__ between two vertices (repeats allowed) in a graph is the minimum number of edges in a path connecting the two vertices.
  - graph theory / eccentricity ::@:: The __eccentricity__ of a vertex in a graph is the maximum distance it can have with any vertex in the same graph.
  - graph theory / center ::@:: The __center__ of a graph is a vertex with the minimum eccentricity among all of its vertices.
  - graph theory / radius ::@:: The __radius__ of a graph is the minimum eccentricity of its vertices, i.e. the eccentricity of its center.
  - graph theory / diameter ::@:: The __diameter__ fo a graph is the maximum distances any pair of vertices (repeats allowed) can have.
- theorem: radius and diameter of a graph ::@:: For any graph, the following relationship holds: radius ≤ diameter ≤ 2 · radius. <p> To prove this, draw its diameter (which is a shortest path between the two points) and its center. Consider the case if the center is in the diameter path and if not in the diameter path.
- theorem: tree, leaf, center ::@:: No leaf can be a center of a tree with 3 or more vertices. <p> To prove this, suppose a leaf is a center. We can write the leaf's only neighbor's distance to any other vertex in terms of the distance of the leaf to any other vertex. This would produce a contradiction.
- theorem: tree, center ::@:: A tree either has one center or two _neighboring_ centers. <p> This can be proven using strong induction. Prove the base case for |_V_| = 1 and |_V_| = 2. Then realize that any tree can be transformed into a smaller one by removing all of its leaves so that we can apply the induction hypothesis. After applying the hypothesis, re-adding the leaves preserves the centers. Consider the smaller tree with its centers as the roots to figure out why re-adding the leaves preserves the centers.
- [Dijkstra's algorithm](../../../../general/Dijkstra's%20algorithm.md) ::@:: A common algorithm for finding the shortest paths between nodes in a weighted graph.
  - Dijkstra's algorithm / algorithm ::@:: Say we are finding the shortest distance from the vertex _u_ to every other vertices. Start by initializing distances: $d(u) = 0, d(v) = \infty$. Create a priority queue containing all vertices in the graph, ordered by non-decreasing distance $d(v)$. While the priority queue is nonempty, extract the first vertex _v_. For each neighbor _n_ of the vertex _v_, assign $d(n) = \min\set{d(n), d(v) + w(v \rightarrow n)}$. Update the priority queue if needed. Repeat until the queue is empty. <p> To prove the correctness of Dijkstra's algorithm, notice that for a shortest path from _a_ to _z_: _a_ → ... → _y_ → _z_, this implies the path from _a_ to _y_ must also be the shortest between them: _a_ → ... → _y_.
- graph theory
  - graph theory / matching ::@:: A __matching__ of a graph is the set of edges in which no two edges share an endpoint.
  - graph theory / maximal matching (not to be confused with _maximum matching_) ::@:: A __maximal matching__, not to be confused with _maximum matching_, of a graph is a matching that is not a proper subset of any other matching. A maximal matching is not necessarily a maximum matching, but the converse is true.
  - graph theory / maximum matching (not to be confused with _maximal matching_) ::@:: A __maximum matching__, not to be confused with _maximal matching_, of a graph is a matching with a maximum number of edges. A maximum matching is a maximal matching, but the converse is false.
  - graph theory / alternating walk, alternating path ::@:: An __alternating walk__ of a matching is a walk that alternates between edges in the matching and not in the matching. An __alternating path__ is defined analogously. <p> Outside this course, an __alternating walk__ is more commonly defined to additionally require beginning with an unmatched vertex.
  - graph theory / augmenting path ::@:: An __augmenting path__ of a matching is an alternating _path_ that starts and ends with a vertex not covered by the matching.
- theorem: maximum matching, augmenting path ::@:: A matching is _maximum_ (which implies _maximal_) iff it does not contain an augmenting path. <p> It is easy to prove that a maximum matching does not contain an augmenting path. Simply switch the edges in the augmenting path, if it exists, to get a larger matching. Use this to prove by contradiction. <p> The converse is harder. Assume there is a matching _M_ without augmenting paths. Consider any other matching _M_'. Define a new graph consisting of the original vertices and edges that are in either _M_ or _M_' but not both (exclusive-or). This operation will not increase the number of edges in _M_ and that in _M_' in the new graph. Also, the decrease in number of edges in _M_ and that in _M_' is also the same. The new graph consists of either paths or cycles because the degree of each vertex is at most 2. In the new graph, any path and cycle alternates between _M_ and _M_'. Since _M_ has no augmenting paths, any path must start and end at a vertex that is covered by _M_. For any cycle, the number of edges in _M_ and _M'_ must be the same. So, in the new graph, |_M_'| ≤ |_M_|. Then, since the decrease in edges is the same for both matchings, |_M_'| ≤ |_M_| in the original graph.
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

## week 6 TA session

- datetime: 2024-10-11T19:00:00+08:00/2024-10-11T19:50:00+08:00
- topic: solving weekly problem set 4
- [questions/2024-10-11](questions/2024-10-11.md)
- [week 4 problem set](questions/week%204%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/jIsRmWzacfI)

## week 7 lecture

- datetime: 2024-10-14T09:00:00+08:00/2024-10-14T10:20:00+08:00
- topic: matchings, vertex covers, edge covers, independent sets
- theorem: bipartite graph, matching ::@:: In an bipartite of a graph into _X_ and _Y_, where |_X_| ≤ |_Y_|, there is a matching saturating _X_ iff for every subset of _X_, the number of its neighbors (which must all be in _Y_) is at least the size of the subset. <p> Proving the number of its neighbors is at least the size of the subset is trivial. The converse is much harder. <p> To prove the converse, we use contradiction. Suppose there is a _maximum_ matching _M_ that does not saturate _X_. Take any element _x_ in _X_ not covered by _M_ and produce a subset {_x_}. Since {_x_} must have at least one neighbor as a subset of _X_, it must connect to an element _y_ in _Y_. But the element _y_ must be covered by _M_, or otherwise the matching is not maximum. Then consider the element _y_. It is in _M_, so there is another element in _X_ that is not _x_ that connects to _y_. Add that element to the subset. Now the minimum number of neighbors is 2. So there must be another edge to connect to an new element in _Y_. The edge either connects _x_ to an element in _Y_ that is in _M_, or connects elements that are not _x_ to any element in _Y_ but not already connected by any edge. In both case, the above argument can be repeated again and again. If at any point, an element in _Y_ that is not in _M_ is connected, the matching can be shifted, then _x_ can finally match with _y_, producing a larger matching. This must eventually happen because we will run out of elements of _Y_ that are in _M_ before running out of elements of _X_, because _M_ does not saturate _X_.
  - theorem: bipartite graph, matching / corollary: _k_-regular bipartite graph, perfect matching ::@:: Let _G_ be a _k_-regular bipartite graph _k_ ≥ 1. _G_ has a perfect matching. <p> To prove this, consider an arbitrary subset _S_ of one of the partition, and consider the number of edges between _S_ and _N_(_S_) to show that _S_ ≤ |_N_(_S_)|. Finally, apply the theorem.
- graph theory
  - graph theory / [vertex cover](../../../../general/vertex%20cover.md) ::@:: A __vertex cover__ |_A_| is a set of vertices such that every edge has at least one endpoint in the cover.
- theorem: minimum vertex cover, maximum matching ::@:: In every graph, the minimum vertex cover has a size of at least that of _maximum_ matching. <p> To prove this, consider a maximum matching. For every edge in the maximum matching, one point must be in the vertex cover.
- theorem: minimum vertex cover, maximum matching, bipartite graph ::@:: In every bipartite graph, the minimum vertex cover has a size equals that of maximum matching. <p> To prove this, we can prove the minimum vertex cover has a size smaller than or equal to that of maximum matching. Consider a maximum matching in a bipartite graph. Then consider a minimum vertex cover and split the two bipartition sets into two separate bipartitions depending on if the element is in the minimum vertex cover. Show that the minimum vertex cover implies the existence of a maximum matching on both bipartitions, which can be merged back to get a maximum matching on the original bipartition. <p> Combining with the previous theorem gives us the equality result.
- theorem: vertex cover, independent set, complement ::@:: For any graph, the vertex complement of a vertex cover of a graph is an independent set, and vice versa. <p> For every edge, at least one endpoint is in the vertex cover. After the vertex complement operation, at most one endpoint is in the complement. This means no two vertices are adjacent, so the complement is an independent set.
  - theorem: vertex cover, independent set, complement / corollary: minimum vertex cover, maximum independent set ::@:: For any graph, the size of a minimum vertex cover plus the size of a maximum independent set equals |_V_|.
- graph theory
  - graph theory / [edge cover](../../../../general/edge%20cover.md) ::@:: An edge cover _L_ of a graph is a set of edges such that every vertex of the graph is incident to at least one edge of the set. <p> For graphs with isolated vertices, an edge cover does not exist.
- theorem: maximum matching, minimum edge cover (Gallai) ::@:: For graphs with isolated vertices, the size of a maximum matching _M_ plus the size of a minimum edge cover _L_ equals |_V_|. <p> For vertices covered by a maximum matching _M_, take said edges in the matching into the edge cover. 2|_M_| vertices are covered. For each of the remaining (non-isolated) |_V_| − 2|_M_| vertices, add one adjacent edge to the edge cover. The size of this edge cover is |_M_| + |_V_| − 2|_M_| = |_V_| − |_M_|. So a maximum matching _M_ implies the size of a minimum edge cover is at most |_V_| − |_M_|. <p> Consider an minimum edge cover _L_. Remove all edges not in _L_. There are no isolated vertices, or otherwise _L_ is not an edge cover. The resulting graph has no paths with 3 edges or above, otherwise _L_ is not minimum. So the resulting graph is a collection of stars. In fact, there are |_V_| − |_L_| stars (connected components), because each edge must decrease the number of CCs by exactly 1 (as there are no cycles). Each CC has at least one edge, since there are no isolated vertices. Take one edge from each CC to get a matching. So the size of a maximum matching is at least |_V_| − |_L_|. <p> Combine the above two proofs.
  - theorem: maximum matching, minium edge cover (Gallai) / corollary: subgraph ::@:: A minimum edge cover contains a maximum matching as a subgraph. <p> Realize that one of the proof above only removes edges from a minimum edge cover _L_ to get a maximum matching _M_.
- [questions/2024-10-14/lecture](questions/2024-10-14%20lecture.md)
- materials
  - [lecture video](https://youtu.be/ZIeLPZmvAU4)
  - West/Section 3.1: Matchings and Covers

## week 7 tutorial

- datetime: 2024-10-14T18:00:00+08:00/2024-10-14T18:50:00+08:00
- topics: network flow, Ford-Fulkerson Algorithm
- graph theory
  - graph theory / [flow network](../../../../general/flow%20network.md) ::@:: A __flow network__ (also known as a __transportation network__) is a directed graph where each edge has a __capacity__ and each edge receives a __flow__. The amount of _flow_ on an edge cannot exceed the _capacity_ of the edge.
- [flow network](../../../../general/flow%20network.md)
  - flow network / properties ::@:: The amount of flow of an edge $f(u, v)$ cannot exceed its capacity $c(u, v)$. Flow (__not__ capacity) is skew symmetric: $f(u, v) = -f(v, u)$. The amount of flow is conserved for non-source and non-sink vertices: $\sum_{u \to v} f(u, v) = 0 = \sum_{v \to u} f(v, u)$ for a fixed $v$ that is neither a source $s$ nor a sink $t$.
  - flow network / residual network ::@:: Given a flow $f$ on a flow network, its __residual network__ is a network with capacities that are the remaining capacities of the original flow network with the flow $f$ flowing through it. <p> Note that if the flow flows from $u$ to $v$, the capacity from $u$ to $v$ has the flow amount subtracted, but the capacity from $v$ to $u$ has the flow amount added (by skew-symmetry of flow). The resulting network is different from the original flow network in that the capacities are no longer symmetric, i.e. $c(u, v) = c(v, u)$ is not always true.
  - flow network / augmenting path ::@:: An __augmenting path__ is an available flow path from the source to the sink. <p> A network is at maximum flow iff there is no augmenting path in the residual network.
  - flow network / s–t cut ::@:: A __s–t cut__ of the flow network that requires the source vertex and the sink vertex to be in different subsets. The capacity of an s–t cut is the sum of capacities (weights) of the cut-set.
- [Ford–Fulkerson algorithm](../../../../general/Ford–Fulkerson%20algorithm.md) ::@:: The __Ford–Fulkerson method__ or __Ford–Fulkerson algorithm__ (__FFA__) is a greedy algorithm that computes the maximum flow in a flow network. <p> The idea is simple: Given a flow network and an initially empty flow, compute any _augmenting path_. Add the flow through the augmenting path to the existing flow. When there are no more augmenting paths, stop the algorithm. The resulting flow is a maximum flow. The algorithm may not terminate if the flow values are irrational. <p> Its correctness can be easily seen: Adding an augmenting flow makes the resulting flow still a legal flow in the original network. For as long as there are augmenting flow, there are still more flow to be added, and when there are none, the resulting flow is maximum.
  - [Ford–Fulkerson algorithm](../../../../general/Ford–Fulkerson%20algorithm.md) / s-t cut ::@:: Obviously, the maximum flow cannot exceed the capacity of any s–t cut, since any flow must flow through the cut-set of any s–t cut, so the flow amount cannot exceed the capacity of any s–t cut. <p> This can be used to prove that the Ford–Fulkerson algorithm produces a optimal flow (if it terminates). When it terminates, there are no augmenting paths from the source to the sink. Consider the residual network now. We can cut the residual network into two by checking if a vertex can be reached from the source in the residual network. This creates a s–t cut. Since the flow amount cannot exceed the capacity of any s–t cut, the flow is optimal.
- [questions/2024-10-14/tutorial](questions/2024-10-14%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/VWvgNOCDBrs)
  - West/Section 4.3: Network Flow Problems
  - [video: maximum flow and Ford-Fulkerson](https://youtu.be/cofuiL8inWI)
  - [video: flow networks and maximum flow](https://youtu.be/rlftCrW8t9s)
  - [video: maximum-flow minimum-cut algorithm](https://youtu.be/RjX9zUsKaDU)
  - [video: max-flow and Ford-Fulkerson](https://youtu.be/LdOnanfc5TM)
  - [video: Ford-Fulkerson in 5 minutes](https://youtu.be/Tl90tNtKvxs)

## week 7 lecture 2

- datetime: 2024-10-16T09:00:00+08:00/2024-10-16T10:20:00+08:00
- topic: stable matchings, graph coloring
- theorem: maximum matching, bipartite graph, flow network ::@:: The Ford–Fulkerson algorithm may be used to find a maximum matching on a bipartite graph. Add a source vertex and connect it to each vertex in a partition with an edge of capacity 1. Add a sink vertex and connect it to each vertex in a partition with an edge of capacity 1. Run the Ford–Fulkerson algorithm. The maximum flow is a maximum matching, and vice versa. <p> This can be proved by proving that a flow can be used to construct a matching of the same size, and a matching can be used to construct a flow of the same flow amount. Then the size of a maximum matching equals the max flow amount.
- [stable marriage problem](../../../../general/stable%20marriage%20problem.md) ::@:: The __stable marriage problem__ (also __stable matching problem__) is the problem of finding a stable matching between two equally sized sets of elements given an ordering of preferences for each element. A matching is _stable_ when there does not exist any pair (_A_, _B_) which both prefer each other to their current partner under the matching.
  - stable marriage problem / [Gale–Shapley algorithm](../../../../general/Gale–Shapley%20algorithm.md) ::@:: The __Gale–Shapley algorithm__ is an algorithm for finding a solution stable marriage (matching) problem. The algorithm runs in several rounds. In each round, each unengaged man to the most-preferred woman to whom he has not yet proposed (regardless of whether the woman is already engaged). Each woman replies "maybe" if she is currently not engaged or if she prefers this man over her current provisional partner (in this case, she rejects her current provisional partner who becomes unengaged). In this case, the man and the woman are provisionally (temporarily) engaged. When everyone is (provisionally) engaged, the marriage (matching) is stable. <p> To prove its correctness, suppose there is an unstable pair, and prove by contradiction.
- graph theory
  - graph theory / [graph coloring](../../../../general/graph%20coloring.md) ::@:: In its simplest form, it is a way of coloring the vertices of a graph such that no two adjacent vertices are of the same color; this is called a __vertex coloring__. <p> A coloring using at most _k_ colors is called a (proper) ___k_-coloring__. The smallest number of colors needed to color a graph _G_ is called its __chromatic number__, and is often denoted _χ_(_G_).
  - graph theory / [clique](../../../../general/clique%20(graph%20theory).md) ::@:: A __clique__ is a subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent. That is, a clique of a graph _G_ is an induced subgraph of _G_ that is complete.
- theorem: chromatic number, maximum clique ::@:: The chromatic number is at least the size of a largest clique $\omega(G)$. <p> This is easy to prove by considering a maximum clique.
- theorem: chromatic number, maximum independent set ::@:: The chromatic number is at least $\lvert V \rvert / \alpha(G)$, where $\alpha(G)$ is the size of a largest independent set. <p> If we have a $k$ coloring, we can take vertices of the same color and make an independent set. At least one such independent set obtained this way has a size of at least $\lvert V \rvert / k$ by the pigeonhole principle. So if the maximum independent set is $\alpha(G)$, then $$\alpha(G) \ge \lvert V \rvert / k \implies k \ge \lvert V \rvert / \alpha(G) \,.$$
- theorem: [greedy coloring](../../../../general/greedy%20coloring.md) ::@:: The greedy coloring algorithm simply iterates each vertex in an arbitrary order, and assigns each vertex the first available color. This easily shows that the chromatic number is at most the maximum degree plus 1.
  - theorem: [greedy coloring](../../../../general/greedy%20coloring.md) / corollary: Brook's theorem ::@:: This bound can be slightly improved for all other graphs except for a complete graph or an odd cycle graph. The improved bound becomes the maximum degree instead of the maximum degree plus 1. This is known as __Brook's theorem__.
  - theorem: [greedy coloring](../../../../general/greedy%20coloring.md) / corollary: non-increasing degree sequence ::@:: If the greedy coloring algorithm is run on vertices in order of non-increasing degree, this bound can be slightly improved to: $$\chi(G) \le 1 + \max_i \min\set{d_i, i - 1}$$ for a non-increasing degree sequence $d_1 \ge \cdots \ge d_n$. <p> The $\min\set{d_i, i - 1}$ can be obtained by considering the algorithm when coloring the vertex $i$. The $d_i$ comes from the same upper bound as in the greedy algorithm on an arbitrary sequence of vertices, and the $i - 1$ comes from that only $i - 1$ vertices has been colored when coloring the vertex $i$.
- graph theory
  - graph theory / [Cartesian product of graphs](../../../../general/Cartesian%20product%20of%20graphs.md) ::@:: The __Cartesian product__ _G_ □ _H_ or __box product__ of graphs _G_ and _H_ is a graph such that: 1) the vertex set of _G_ □ _H_ is the Cartesian product _V_(_G_) × _V_(_H_); and 2) two vertices (_u_, _v_) (do not interpret this as an edge or arc) and (_u'_ , _v'_) are adjacent in _G_ □ _H_ if and only if either _u_ = _u'_ and _v_ is adjacent to _v'_ in _H_, or _v = v'_ and _u_ is adjacent to _u'_ in G. <p> Intuitively and graphically, we start with a graph _G_. Then we extrude new copies of _G_, connected to the old copy of _G_, with the new copy offset following an edge in _H_.
- theorem: Cartesian product of graphs, chromatic number ::@:: The chromatic number of the Cartesian product of two graphs, _G_ □ _H_, is the maximum of the two graphs' own chromatic numbers. <p> This is easy to see if you have a graphical interpretation of the Cartesian product. Start with a minimum coloring on the graph _G_ with the larger (or equal) chromatic number _k_. Then extrude-copy _G_, following the edges of _H_. While extrude-copying, cycle the colors (only up to _k_ − 1 times, since we have _k_ colors). Since the chromatic number of _H_ is not larger than _k_, we will not need to cycle the colors more than _k_ − 1 times. The final graph, which is the Cartesian product, has a chromatic number that is the same as that of _G_, i.e. _k_.
- [questions/2024-10-16](questions/2024-10-16.md)
- Due to the midterm exam, there will be no weekly problem set or tutorial this week.
- materials
  - [lecture video](https://youtu.be/VWvgNOCDBrs)
  - West/Section 3.2.3: Stable Matchings
  - West/Section 5.1: Vertex Colorings and Upper Bounds (Brooks' Theorem is not part of the syllabus)
  - [video: introduction to graph colouring](https://youtu.be/RSSfO0lnEp8)
  - [video: coloring code - how compilers use graph theory](https://youtu.be/K3mi2m7ccDQ)
  - [video: applications of graph colouring](https://youtu.be/y4RAYQjKb5Y)

## midterm examination

- datetime: 2024-10-18T18:00:00+08:00/2024-10-18T21:00:00+08:00, PT3H
- venue: Lecture Theater C
- format: closed book
- grades: 15.5/30
  - statistics
    - note: The department told instructors to not release statistics.
    - mean: ?
    - standard deviation: ?
    - low: ?
    - lower quartile: ?
    - median: ?
    - upper quartile: ?
    - high: ?
    - distribution: ?
- report
  - How to do Amir's examinations? ::@:: I had spent too much time on writing things that were later discarded. This led to extremely messy layout (not enough papers) and wasted time. <p> What I should have done instead is to think carefully and make use of pencils for drafting.
  - time limit ::@:: It depends on if you have the insight... whatever that is. Very difficult...
- check
  - note: You will receive a scanned copy of your examination. Send email to Amir to appeal.
- materials
  - [lecture video](https://youtu.be/eLwNjIOM8QE)
  - [midterm examination](attachments/midterm.pdf) (source: <https://canvas.ust.hk/courses/58174/modules/items/1444251>)

> Total Score: 15.5/30
>
> Grader: Amir
>
> Problem 1: 10/10
>
> i) Correct - 2 points <br/>
> ii and iii) Correct, but extremely hard to read due to both untidiness and a bad choice of pen. Please make sure this does not happen in the final. Otherwise, we will simply not grade the solution.
>
> Problem 2: 5.5/10
>
> i) Correct solution, but no closed-form - 1.5 points <br/>
> ii and iii) Nice job - 4 points
>
> Problem 3: 0/10
>
> Not chosen
>
> Problem 4: 0/10
>
> Wrong answer
>
> Note: Your answer sheet was extremely hard to understand and grade. Please make sure this does not happen in the final. Otherwise, you will get a 0. The grader should not struggle with reading your solution.
>
> Please write an email to Amir if you would like to submit a reasonable appeal. Be patient after sending the email. There are hundreds of messages in the queue, mostly because people submit unreasonable appeals that get rejected!

## week 8 lecture

- datetime: 2024-10-21T09:00:00+08:00/2024-10-21T10:20:00+08:00
- topic: divisibility, greatest common divisor
- [integer](../../../../general/ineger.md)
  - integer / definition ::@:: The natural numbers are the nonnegative integers. The negation of nonzero natural numbers are the negative integers.
  - integer / order ::@:: The total order on integers extend the total order on natural numbers, i.e. if a comparison holds in the latter, then it also holds in the former: $$a <_{\mathbb N} b \implies a <_{\mathbb Z} b \quad \forall a, b \in \mathbb N\,.$$ <p> We have: $$-a < 0 < b \text{ and } -a < -b \implies b < a \quad \forall a, b \in \mathbb N_{\ne 0} \,.$$
  - integer / predecessor ::@:: The predecessor on the positive integers are defined using natural numbers. The predecessor on 0 is defined to be -1. The predecessor on negative integers is defined as the negation of the successor of the absolute value of the negative integer. That is: $$p(a) = \begin{cases} s^{-1}(a) & a \in \mathbb N_{\ne 0} \\ -1 & a = 0 \\ -s(a) & \text{otherwise} \,. \end{cases}$$
  - integer / addition ::@:: Addition on integers is defined as: $$\begin{aligned} a + 0 & = 0 && a \in \mathbb Z \\ a + b & = s(a + p(b)) && a \in \mathbb Z, b \in \mathbb N_{\ne 0} \\ a + (-b) & = p(a + s(-b)) && a \in \mathbb Z, b \in \mathbb N_{\ne 0} \,. \end{aligned}$$
    - integer / subtraction ::@:: Subtraction on integers is easily defined in terms of addition on integers.
  - integer / multiplication ::@:: Multiplication on integers is defined as: $$\begin{aligned} a \cdot 0 & = 0 && a \in \mathbb Z \\ a \cdot b & = a \cdot p(b) + a && a \in \mathbb Z, b \in \mathbb N_{\ne 0} \\ a \cdot (-b) & = a \cdot s(-b) + (-a) && a \in \mathbb Z, b \in \mathbb N_{\ne 0} \,. \end{aligned}$$
  - integer / absolute value ::@:: The absolute value function on integers is defined as: $$\begin{aligned} \lvert n \rvert & = n && n \in \mathbb N_0 \\ \lvert -n \rvert & = n && n \in \mathbb N_{\ne 0} \,. \end{aligned}$$
- theorem: [Euclidean division](../../../../general/Euclidean%20division.md) ::@:: Given two integers _a_ (_dividend_) and _b_ (_divisor_), there exists unique integers _q_ (_quotient_) and _r_ (_remainder_) such that $$a = bq + r \qquad 0 \le r < \lvert b \rvert \,.$$ <p> To prove existence, consider the set of integers in the form of $a - qb \ge 0$. The set can be proved to be nonempty. Then prove that the minimum element of the set must have $0 \le r < \lvert b \rvert$. <p> To prove uniqueness, assume there are two distinct $(q, r)$ satisfying the above conditions. Then by contradiction: $$b \le \lvert q_1 - q_2 \rvert b = \lvert r_1 - r_2 \rvert < b \,.$$
- [divisor](../../../../general/divisor.md) ::@:: _a_ divides _b_ is defined as $$a \mid b \iff b = aq \quad q \in \mathbb Z \,.$$ (Some definitions require $a \ne 0$. We do not require it here.)
  - divisor / trivial theorems ::@:: Any integer divides 0. <br/> -1 and 1 divide any integer. <br/> Any integer divides itself and its negation. <br/> Only -1 and 1 divides 1.
  - divisor / multiplication ::@:: If $a \mid b$ and $c \mid d$, then $ac \mid bd$. The converse does not always hold.
  - divisor / transitivity ::@:: If $a \mid b$ and $b \mid c$, then $a \mid c$. It does not make sense to talk about the converse because you need to choose $b$ somehow without the conditions.
  - divisor / equality ::@:: If $a \mid b$ and $b \mid a$, then $a = \pm b$. The converse holds.
  - divisor / linearity ::@:: If $a \mid b$ and $a \mid c$, then $a \mid (bx + cy) \quad x, y \in \mathbb Z$. The converse does not always hold.
- [greatest common divisor](../../../../general/greatest%20common%20divisor.md) ::@:: The _greatest common divisor_ (GCD) of integers _a_ and _b_ (denoted gcd(_a_, _b_)), at least one of which is nonzero, is the greatest positive integer _d_ such that _d_ is a divisor of both _a_ and _b_.
  - greatest common divisor / [Bézout's identity](../../../../general/Bézout's%20identity.md) ::@:: For every two nonzero integers _a_, _b_, there exists two integers _x_, _y_, such that $$\gcd(a, b) = ax + by \,.$$
    - greatest common divisor / [Bézout's identity](../../../../general/Bézout's%20identity.md) / corollary ::@:: For every two nonzero integers _a_, _b_, $$\set{ax + by \mid x, y \in \mathbb Z} = \set{q \cdot \gcd(a, b) \mid q \in \mathbb Z} \,.$$
- [coprime integers](../../../../general/coprime%20integers.md) ::@:: Two integers are coprime iff their greatest common divisor is 1. It is denoted with $a \perp b$.
- theorem: coprime integers, greatest common divisor ::@:: If $\gcd(a, b) = d$, then $\gcd(a / d, b / d) = 1$.
- theorem: coprime integers, divisor, multiplication ::@:: If two coprime integers $a, b$ divide the same number $c$, then $ab \mid c$.
- theorem: [Euclid's lemma](../../../../general/Euclid's%20lemma.md) ::@:: If $a \mid bc$ and $\gcd(a, b) = 1$, then $a \mid c$.
- [questions/2024-10-21/lecture](questions/2024-10-21%20lecture.md)
- materials
  - [lecture video](https://youtu.be/Bq42S8vZ16g)
  - Burton/Chapter 1: Preliminaries
  - Burton/Chapter 2: Divisibility Theory
  - [video: number theory I](https://youtu.be/NuY7szYSXSw)
  - [playlist: introduction to number theory (watch lectures 3 and 4)](https://youtu.be/EzE6it9kAsI?list=PL8yHsr3EFj53L8sMbzIhhXSAOpuZ1Fov8)

## week 8 tutorial

- datetime: 2024-10-21T18:00:00+08:00/2024-10-21T18:50:00+08:00
- topic: prime factorizations, fundamental theorem of arithmetic
- [Euclidean algorithm](../../../../general/Euclidean%20algorithm.md) ::@:: The __Euclidean algorithm__ is an efficient method for computing the greatest common divisor (GCD) of two integers, the largest number that divides them both without a remainder. <p> Given two integers $1 \le a \le b$, let $r$ be the remainder of $a$ dividing $b$. Then $\gcd(a, b) = \gcd(b, r)$. The Euclidean algorithm is simply using this fact over and over again.
- [least common multiple](../../../../general/least%20common%20multiple.md) ::@:: The least common multiple, lowest common multiple, or smallest common multiple of two integers _a_ and _b_, usually denoted by lcm(_a_, _b_), is the smallest positive integer that is divisible by both _a_ and _b_.
- theorem: greatest common divisor, least common divisor ::@:: $$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = \lvert a \cdot b \rvert$$ (if we define the cases where one or both integers are zero properly)
  - theorem: greater common divisor, least common divisor / corollary: coprime integers ::@:: $a \perp b$ iff $\operatorname{lcm}(a, b) = \lvert a \cdot b \rvert$.
- [prime number](../../../../general/prime%20number.md) ::@:: A __prime number__ (or a __prime__) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a __composite number__.
- theorem: divisor, prime number ::@:: If $p$ is a prime and $p \mid ab$, then $p \mid a$ or $p \mid b$ (or both).
  - theorem: divisor, prime number / corollary: generalization ::@:: If $p$ is a prime number and $p \mid a_1 a_2 \ldots a_n$, $p$ divides at least one of the $a_i$-s.
  - theorem: divisor, prime number / corollary: generalization, prime number ::@:: If $p$ is a prime number and $p \mid q_1 q_2 \ldots q_n$, where $q_i$ are all prime numbers, $p$ equals at least one of the $q_i$-s.
- [fundamental theorem of arithmetic](../../../../general/fundamental%20theorem%20of%20arithmetic.md) ::@:: The __fundamental theorem of arithmetic__ states that every integer greater than 1 can be represented uniquely as a product of prime numbers, up to the order of the factors. <p> Existence can be proved by induction, starting from 2. Uniqueness can be proved by assuming the existence of two prime factorizations, but then find that each prime factor equals one in the other.
- theorem: irrationality of $\sqrt 2$ ::@:: $\sqrt 2$ is irrational. Prove by contradiction: start with a fraction _a_/_b_ with gcd(_a_, _b_) = 1, and then square it.
- theorem: number of primes ::@:: There are infinitely many primes. <p> Suppose there are finitely many primes. We can construct a new prime by multiplying them together and add 1. This leads to a contradiction.
  - theorem: number of primes / corollary: _n_-th prime number upper bound ::@:: The above proof for infinitely many primes also give a very loose upper bound on the _n_-th prime number: $$p_n \le 2^{2^{n - 1} } \,.$$
- [questions/2024-10-21/tutorial](questions/2024-10-21%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/T6lNCyZ0SvM)
  - Burton/Chapter 2.4: Euclid
    - to: Burton/Chapter 3.3: Goldbach
  - [video: primes](https://youtu.be/VRrP4US7idg)
  - [solve problems 1 to 10 of ProjectEuler.net](https://projecteuler.net/archives)
  - [fun to read: Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
    - [Collatz conjecture](../../../../general/Collatz%20conjecture.md)

## week 8 lecture 2

- datetime: 2024-10-23T09:00:00+08:00/2024-10-23T10:20:00+08:00
- topic: congruence, modular multiplicative inverse, Chinese remainder theorem
- [modular arithmetic](../../../../general/modular%20arithmetic.md) ::@:: Given an integer _m_ ≥ 1, called a __modulus__, two integers _a_ and _b_ are said to be __congruent__ modulo _m_, iff _m_ is a divisor of their difference; that is, $$a \equiv b \pmod m \iff m \mid (a - b) \,.$$
  - modular arithmetic / equality ::@:: $$a \equiv a \pmod m$$
  - modular arithmetic / symmetry ::@:: $$a \equiv b \pmod m \iff b \equiv a \pmod m$$
  - modular arithmetic / transitivity ::@:: $$a \equiv b \pmod m \text{ and } b \equiv c \pmod m \implies a \equiv c \pmod m$$
  - modular arithmetic / linearity ::@:: $$a \equiv c \pmod m \text{ and } b \equiv d \pmod m \implies a + b \equiv c + d \pmod m$$
    - modular arithmetic / linearity / corollary: subtraction ::@:: $$a + c \equiv b + c \pmod m \iff a \equiv b \pmod m$$ (subtract $c$ from both sides)
  - modular arithmetic / multiplicative ::@:: $$a \equiv c \pmod m \text{ and } b \equiv d \pmod m \implies ab \equiv cd \pmod m$$
    - modular arithmetic / multiplicative / non-theorem: division ::@:: $$\begin{aligned} a \equiv b \pmod m & \implies ac \equiv bc \pmod m \\ ac \equiv bc \pmod m & \;\;\not\nobreak\!\!\!\!\implies a \equiv b \pmod m \end{aligned}$$ (since the _modular multiplicative inverse_ of $c$, $c^{-1}$, may not be defined; see below)
    - modular arithmetic / multiplicative / corollary: power ::@:: $$\begin{aligned} a \equiv b \pmod m & \implies a^k \equiv b^k \pmod m \\ a^k \equiv b^k \pmod m & \;\;\not\nobreak\!\!\!\!\implies a \equiv b \pmod m \end{aligned}$$ (since the _modular multiplicative inverses_ of $a$ and $b$, $a^{-1}$ and $b^{-1}$, may not be defined; see below)
- [modular multiplicative inverse](../../../../general/modular%20multiplicative%20inverse.md) ::@:: A __modular multiplicative inverse__ of an integer _a_ is an integer _x_ such that the product _ax_ is congruent to 1 with respect to the modulus _m_. In the standard notation of modular arithmetic this congruence is written as $$ax \equiv 1 \pmod m\,.$$ In an notation that some consider as an abuse of notation, $x$ in the above context is written as $a^{-1}$ instead.
- modular arithmetic
  - modular arithmetic / cycles ::@:: Consider repeating an operation modulo _m_. Since there are _m_ numbers (more accurately, congruent classes), the operation must eventually produce a number that you start with. The operation may go through up to _m_ − 1 other numbers before going back to the number that you start with, and can be less. <p> For example, consider the shift function that adds 2 to a number modulo 6. It creates 2 cycles: 0 → 2 → 4, 1 → 3 → 5. We can do the same for multiplication modulo _n_, and is the main character here.
    - [cyclic group](../../../../general/cyclic%20group.md)
    - modular arithmetic / cycles / multiplication ::@:: Consider $a^k \equiv 1 \pmod m$ for a fixed $a$ and $m$. The smallest positive integer _k_ satisfying this equation, if it exists, is the number of times it takes to multiply by $a$ and get back the same number, since $b a^{k} \equiv b \pmod m$.
- modular multiplicative inverse
  - modular multiplicative inverse / existence ::@:: _a_ has a modular multiplicative inverse modulo _m_ iff $\gcd(a, m) = 1$. <p> Prove by applying Bézout's identity on $$ax \equiv 1 \pmod m \iff \exists y \in \mathbb Z \quad ax + my = 1 \,.$$
  - modular multiplicative inverse / uniqueness ::@:: The modular multiplicative inverse of _a_ modulo _m_, if it exists, is unique. <p> Assume there exists two distinct multiplicative inverse _x_ and _x'_. Prove by contradiction: $$\begin{aligned} ax - ax' & \equiv 1 - 1 \pmod m \\ a(x - x') & \equiv 0 \pmod m \\ x - x' & \equiv 0 && a \not\equiv 0 \pmod m \\ x & \equiv x' \pmod m \,. \end{aligned}$$
- [modular exponentiation](../../../../general/modular%20exponentiation.md)
  - modular exponentiation / fast modular exponentiation ::@:: Fast modular exponentiation is simply exponentiation by squaring, but with modulus. <p> Exponentiation by squaring calculates $a^k$ for an integer _k_ and makes use of that $k$ can be expressed as the sum of powers of 2 (binary representation), and that $a^{2^{k'} }$ can be calculated in _k'_ multiplications, e.g.: $a^8 = \left(a^4\right)^2 = \left( \left(a^2 \right)^2 \right)^2$. <p> Fast modular exponentiation is simply doing the same thing, but after each multiplication, the number will be modulo _m_ to make the number smaller while keeping the final answer correct.
    - [exponentiation by squaring](../../../../general/exponentiation%20by%20squaring.md)  
- theorem: divisibility of 3 ::@:: A number is divisible by 3 iff the sum of its digits is divisible by 3. <p> Prove using modular arithmetic.
- theorem: modular arithmetic, polynomial ::@:: Let _P_(_x_) be a polynomial with _integer coefficients_. Then $$a \equiv b \pmod m \implies P(a) \equiv P(b) \pmod m \,.$$ This is easily seen because _P_(_x_) only involves addition and multiplication with integers. The converse may not be true, however.
- theorem: [Chinese remainder theorem](../../../../general/Chinese%20remainder%20theorem.md) ::@:: Let $n_1, \ldots, n_k$ be pairwise co-prime integers greater than 1. Then the system $$\begin{aligned}x&\equiv a_{1}{\pmod {n_{1} } }\\&\,\,\,\vdots \\x&\equiv a_{k}{\pmod {n_{k} } }\end{aligned}$$ has an unique solution $x$ modulo $n_1 \ldots n_k$. <p> This can be proved by considering a solution modulo $n_1$, which is unique, to the first equation: $x_1 \equiv a_1 \pmod{n_1} \iff x_1 = a_1 + n_1 y \quad y \in \mathbb Z$. Then consider the second equation. Since $n_1$ and $n_2$ are co-prime, $x_1$ iterates through all numbers modulo $n_2$ as we increase $y$. A complete cycle increases $x_1$ by $n_1 n_2$. So there is an unique solution $x_{1, 2}$ modulo $n_1 n_2$ that satisfies both the first and the second equation. Thus, we can combine the two equations into one: $x_{1, 2} \equiv a_{1, 2} \pmod{n_1 n_2}$, and $x_{1, 2}$. Repeat the above procedure until there is only an equation with an unique solution $x$ modulo $n_1 \ldots n_k$ left.
- [questions/2024-10-23](questions/2024-10-23.md)
- [week 8 problem set](questions/week%208%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/RZ4J0BSKhLQ)
  - Burton/Chapter 4: Congruences
    - It is really important that you read the book since it provides different proofs than the ones covered in the lecture.
  - [video playlist: Chinese remainder theorem](https://youtu.be/EolotL9HN8k?list=PL22w63XsKjqyg3TEfDGsWoMQgWMUMjYhl)
    - Make sure you watch all of this playlist, especially the last video.
  - [solve problems 14, 20, 27, 47, 50, 69, 77, 112, 122 and 451 of ProjectEuler.net](https://projecteuler.net/archives)

## week 8 TA session

- datetime: 2024-10-25T19:00:00+08:00/2024-10-25T19:50:00+08:00
- topic: solving weekly problem set 5
- [questions/2024-10-25](questions/2024-10-25.md)
- [week 5 problem set](questions/week%205%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/UXYUmObELF0)

## week 9 lecture

- datetime: 2024-10-28T09:00:00+08:00/2024-10-28T10:20:00+08:00
- topic: Fermat's little theorem, Euler's Theorem, Wilson's Theorem
- Chinese remainder theorem
- [Fermat's little theorem](../../../../general/Fermat's%20little%20theorem.md) ::@:: For a prime number $p$, $$\begin{aligned} a^p & \equiv a \pmod p \\ a^{p - 1} & \equiv 1 \pmod p \,. \end{aligned}$$ The converse fails for Carmichael numbers. <p> This is a special case of Euler's theorem for prime numbers, since $\varphi(p) = p - 1$. <p> As a note, $p$ is also the smallest exponent greater than 1 satisfying the above equations for all $a$.
  - [proofs of Fermat's little theorem](../../../../general/proofs%20of%20Fermat's%20little%20theorem.md)
- [Euler's totient function](../../../../general/Euler's%20totient%20function.md) ::@:: Euler's totient function counts the positive integers up to a given integer _n_ that are relatively prime (co-prime) to _n_. <p> Obviously, $\varphi(p) = p - 1$ for a prime number $p$.
- theorem: Euler's totient function, prime factorization ::@:: Let $n = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$. Then $$\varphi(n) = n (1 - 1 / p_1) \cdots (1 - 1 / p_k) \,.$$ <p> To prove this, consider a positive integer co-prime to $n$. That number does not have any common prime factors with $n$. Each term $(1 - 1 / p_i)$ counts the proportion of positive integers that does not have $p_i$ as a prime factor. Said proportions are mutually independent, i.e. the proportion of an integer having a prime factor $p_i$ equals the proportion of an integer having a prime factor $p_i$, given that it already has certain other prime factors. So we can multiply the terms together to get the correct proportion. Finally, multiply by $n$ to turn this from a proportion to a count.
- lemma: Euler's totient function, co-prime ::@:: $$a \perp b \implies \varphi(ab) = \varphi(a) \varphi(b)$$ (i.e. Euler's totient function, since it also satisfies $\varphi(1) = 1$, is a multiplicative function)
- [Euler's theorem](../../../../general/Euler's%20theorem.md) ::@:: For two co-prime positive integers $a, n$, $$a^{\varphi(n)} \equiv 1 \pmod n \,,$$ where $\varphi(n)$ is Euler's totient function. The converse is true. <p> As a note, $\varphi(n)$ may NOT be the smallest exponent greater than 1 that satisfies the above equation for all $a$ co-prime to $n$. It could be a divisor of $\varphi(n)$ instead. <p> Consider the set of numbers $A$ that are modular multiplicative inverses of modulus _n_. There are $\varphi(n)$ such numbers. The multiplication of any two numbers from such a set yields a number in the set (i.e. multiplication is closed): $ax_a \equiv 1 \pmod n \text{ and } bx_b \equiv 1 \pmod n \implies (ab) (x_a x_b) \equiv 1 \pmod n$, so $ab$ has a modular multiplicative inverse and is in $A$ by definition. Take any $b \in A$. Consider multiplying each number in $A$ modulo $n$. Multiplying by $b$ modulo $n$ is injective since $b$ has a multiplicative inverse. It is also surjective because the operation maps $A$ back to itself, and is injective. So after multiplying each number in $A$ modulo $n$, we get back $A$ again. Finally: $$\begin{aligned} \prod_{a \in A} ba & \equiv \prod_{a \in A} a \pmod n \\ b^{\varphi(n)} \prod_{a \in A} a & \equiv \prod_{a \in A} a \pmod n \\ b^{\varphi(n)} & \equiv 1 \pmod n && \text{all }a\text{ have multiplicative inverses} \,. \end{aligned}$$
- [Wilson's theorem](../../../../general/Wilson's%20theorem.md) ::@:: For a prime number $p$, $$\begin{aligned} (p - 1)! & \equiv -1 \pmod p \\ (p - 2)! & \equiv 1 \pmod p \,. \end{aligned}$$ The converse is true. <p> This can be proved using modular multiplicative inverses and Fermat's little theorem.
- [questions/2024-10-28/lecture](questions/2024-10-28%20lecture.md)
- materials
  - [lecture video](https://youtu.be/rgidnudZ3TU)
  - [`cycles.cpp`](attachments/cycles.cpp)
  - [video: order of an integer modulo n](https://youtu.be/dFz2SCFwies)
  - [video: Fermat's little theorem](https://youtu.be/OkQJGql8os8)
  - [video: Euler's theorem](https://youtu.be/ijT3pmmal00)
  - [video: Wilson's theorem](https://youtu.be/uWoKhyKcEH4)
  - [playlist: introduction to number theory (watch lectures 5 to 14, primes to Euler's totient)](https://youtu.be/8I0z_Lobtso?list=PL8yHsr3EFj53L8sMbzIhhXSAOpuZ1Fov8)
  - [video: COMP 4541's number theory tutorial - part II](https://youtu.be/WQRTZWb5Idc)
  - [video: proof that the totient function is multiplicative](https://youtu.be/qpYqvNBQZ4g)
  - [video: explicit formula for Euler's totient function](https://youtu.be/HgUfBx8Pvz0)
  - [video: Euler's totient function and Fermat's little theorem](https://youtu.be/5pswKNgVZSg)
  - Burton/Chapter 5: Fermat's Theorem
  - Burton/Chapter 7: Euler's Generalization of Fermat's Theorem

## week 9 tutorial

- datetime: 2024-10-28T18:00:00+08:00/2024-10-28T18:50:00+08:00
- topic: Diffie–Hellman–Merkle key exchange, ElGamal encryption
- [symmetric-key algorithm](../../../../general/symmetric-key%20algorithm.md) ::@:: Alice and Bob have a shared key that is secret (should not be known to Eve). The encryption and decryption algorithm uses the same shared key.
- [one-time pad](../../../../general/one-time%20pad.md) ::@:: Every time Alice and Bob sends a message, a different truly random shared key that is at least as long as the message and secret (should not be known to Eve) is used. The message is encrypted using modular addition and decrypted using modular subtraction. <p> Eve cannot get any information (not even probabilistic information) from the encrypted message without knowing the key, because there exists an key that gives the encrypted message for every possible message.
- [discrete logarithm](../../../../general/discrete%20logarithm.md) ::@:: The discrete logarithm log<sub>_b_</sub> _a_ is an integer _k_ such that _b_<sup>_k_</sup> = _a_. No efficient method is known for computing them in general (e.g. in modular arithmetic).
- [Diffie–Hellman key exchange](../../../../general/Diffie–Hellman%20key%20exchange.md) ::@:: How can Alice and Bob share a secret key without Eve knowing for encryption later? <p> They can both compute $g^{ab} \pmod m \,.$ First they publicly share a prime number $m$ and a primitive root modulo $g$ ($g^k$ generates all possible numbers modulo $m$). Alice chooses a secret key $a$. Bob chooses a secret key $b$. Alice calculates $g^a \pmod m$ and sends it to Bob. Bob calculates $g^b \pmod m$ and sends it to Alice. Then both Alice and Bob calculates $\left(g^a\right)^b \equiv \left(g^b\right)^a \equiv g^{ab} \pmod m$ together to get a shared secret key. <p> In the process, Eve only knows $g$, $m$, $g^a \pmod m$ and $g^b \pmod m$. Computing $a$ or $b$ from the above information is the discrete logarithm problem, for which there is no efficient method is known for computing them in general. There may be efficient methods in specific cases, e.g. $g^a \le m$, $g^b \le m$, etc.
- [public-key cryptography](../../../../general/public-key%20cryptography.md) ::@:: __Public-key cryptography__ is the field of cryptographic systems that use pairs of related keys. Each key pair consists of a public key and a corresponding private key. ElGamal encryption and RSA are examples.
- [ElGamal encryption](../../../../general/ElGamal%20encryption.md) ::@:: A part of ElGamal uses the Diffie–Hellman key exchange to exchange a shared secret. <p> ElGamal is similar to the Diffie–Hellman key exchange, but with some differences. Say Alice wants to send a message $M$ to Bob. The tuple $\left(g, m, g^a \pmod m\right)$ sent by Alice is the public key. $a$ kept private by Alice is the private key. Then Bob, instead of sending $g^b \pmod m$ only, sends $\left(g^b \pmod m, g^{ab} + M \pmod m\right)$. Then Alice can decrypt the message by subtracting $g^{ab} \pmod m$. Bob can use a different $b$ for every message $M$ he sends.
- [RSA](../../../../general/RSA%20(cryptosystem).md)
  - RSA / principle ::@:: It is practical to find three very large positive integers _e_, _d_, and _n_, such that for all integers _m_ (0 ≤ _m_ < _n_), $$\left(m^e\right)^d \equiv m \pmod n \,.$$ However, when given only _e_ and _n_, it is extremely difficult to find _d_. <p> A naive example is as below. If _n_ is a prime number _p_, then $m^{p - 1} \equiv 1 \pmod p$ by Fermat's little theorem. Choose 1 < _e_ < $\lambda(p) = \varphi(p) = p - 1$ such that _e_ is co-prime to _p_ − 1. Then find _d_ in $de \equiv 1 \pmod {p - 1}$, which must exist. The tuple $(n, e)$ is the public key. $d$ is the private key. Encrypting $m$ is calculating $m^e \pmod n$. Decrypting $m^e \pmod n$ is calculating $\left(m^e\right)^d \equiv m^{de} \equiv m^{k(p - 1) + 1} \equiv m \pmod n$. <p> The example is naive because if _n_ is a prime, $n = p$, we can find _d_ easily from $(e, n)$ as we can find $\lambda(p) = \varphi(p) = p - 1$. Normally, _n_ is a semi-prime, a product of two primes: $n = pq$. Then $\lambda(pq) = \operatorname{lcm}(p - 1, q - 1)$, which requires factorizing $n$ first if we only know $(e, n)$. Factorizing large numbers is difficult in general.
- [Carmichael function](../../../../general/Carmichael%20function.md) ::@:: The __Carmichael function__ _λ_(_n_) of a positive integer _n_ is the smallest positive integer _m_ such that $$a^m \equiv 1\pmod n$$ holds for every integer _a_ co-prime to _n_. <p> $\lambda(n) \mid \varphi(n)$ is always true. For prime numbers _p_, $\lambda(p) = \varphi(p) = p - 1$.
- [questions/2024-10-28/tutorial](questions/2024-10-28%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/B5xa4ig13AY)
  - [video: secret key exchange](https://youtu.be/NmM9HA2MQGI)
  - [video: the mathematics behind Diffie–Hellman](https://youtu.be/NmM9HA2MQGI)
  - [video: COMP 4541's Diffie–Hellman lecture](https://youtu.be/-R0FYB2O7RM)
  - [video: COMP 4541's number theory tutorial - part I](https://youtu.be/C1NWehXA6YY)
  - [video: COMP 4541's ElGamal lecture](https://youtu.be/12ZC8ntNFY4)
  - [video: ElGamal encryption](https://youtu.be/tKNY1zhK3sQ)
  - Burton/Chapter 10: Intro to Crypto

## week 9 lecture 2

- datetime: 2024-10-30T09:00:00+08:00/2024-10-30T10:20:00+08:00
- topic: RSA encryption, digital signatures
- [integer factorization](../../../../general/integer%20factorization.md) ::@:: __Integer factorization__ is the decomposition of a positive integer into a product of integers. No efficient non-quantum integer factorization algorithm is known (as of 2024).
- [RSA](../../../../general/RSA%20(cryptosystem).md) ::@:: If _n_ is a semi-prime, a product of two primes: $n = pq$, then $m^{\varphi(n)} \equiv 1 \pmod n$ by Euler's theorem. Choose 1 < _e_ < $\varphi(n)$ such that _e_ is co-prime to $\varphi(n)$. Then find _d_ in $de \equiv 1 \pmod {\varphi(n)}$, which must exist. The tuple $(n, e)$ is the public key. $d$ is the private key. Encrypting $m$ is calculating $m^e \pmod n$. Decrypting $m^e \pmod n$ is calculating $\left(m^e\right)^d \equiv m^{de} \equiv m^{k \cdot \varphi(n) + 1} \equiv m \pmod n$. <p> Actually, $\varphi(n) = \varphi(pq) = \varphi(p) \varphi(q) = (p - 1)(q - 1)$ above can be replaced with $\lambda(n) = \lambda(pq) = \operatorname{lcm}(p - 1, q - 1)$. Using the Chinese remainder theorem, $m^{de - 1} \equiv 1 \pmod n$ has the same unique solution as $$\begin{aligned} m^{de - 1} & \equiv 1 \pmod p \\ m^{de - 1} & \equiv 1 \pmod q \end{aligned} \,.$$ It suffices that $p - 1 \mid de - 1$ and $q - 1 \mid de - 1$, so $\operatorname{lcm}(p - 1, q - 1) \mid de - 1$.
  - RSA / encryption & authenticity ::@:: Alice wants to send a message to Bob. While Alice can encrypt a message, Eve can also encrypt a message as well. Eve can also multiply two encrypted messages together. <p> Something else is needed to guarantee authenticity, i.e. ensure the message is sent by Alice.
  - RSA / signature ::@:: Notice that $$\left(m^e\right)^d \equiv \left(m^d\right)^e \pmod n \,.$$ So we can swap the role of private key and public key. To send an encrypted message, public key encrypts a message and private key decrypts a message. In a digital signature scheme, private key signs a message and public keys validates that the message is signed. <p> A naive digital signature protocol simply swaps the role of the private key and the public key, and sends a signed message. We can send both the encrypted message and the signed message together. <p> While this protects against simply making up a new message, this does not protect against multiplying two encrypted messages together. A more sophisticated scheme is needed.
    - RSA / signature / sophisticated scheme ::@:: The naive scheme signs and encrypts separately. <p> Instead, Alice signs the message with Alice's private key and appends the signature to the message. Then encrypt and send the message with Bob's public key. When Bob receives the message, Bob decrypts the message with Bob's private key. Bob gets the signature and validates it using Alice's public key. <p> You can also reverse the order of signing and encryption, i.e. encrypt and then sign instead.
- [digital signature](../../../../general/digital%20signature.md)
- [questions/2024-10-30](questions/2024-10-30.md)
- [week 9 problem set](questions/week%209%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/Pz5K4GCg4Hg)
  - [video: breaking RSA](https://youtu.be/-ShwJqAalOk)
  - [video: What are digital signatures?](https://youtu.be/s22eJ1eVLTU)
  - [video: COMP 4541's RSA lecture](https://youtu.be/1h7yex387pk)
  - [video: COMP 4541's digital signatures lecture](https://youtu.be/Z7ugkxTmwdY)
  - [video: the RSA cryptosystem and efficient exponentiation](https://youtu.be/QSlWzKNbKrU)
  - [video: Diffie–Hellman key exchange and the discrete log problem](https://youtu.be/aeOzBCbwxUo)
  - [reading: side-channel attacks (Wikipedia)](https://en.wikipedia.org/wiki/Side-channel_attack)
  - [reading: power analysis (Wikipedia)](https://en.wikipedia.org/wiki/Power_analysis)

## week 9 TA session

- datetime: 2024-11-01T17:00:00+08:00/2024-11-01T17:50:00+08:00
- topic: solving weekly problem set 6
- [questions/2024-11-01](questions/2024-11-01.md)
- [week 6 problem set](questions/week%206%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/4NMJ6GqW_T0)
  - [lecture video: addendum on problem 3](https://youtu.be/13j1nr9UgxA)

## week 10 lecture

- datetime: 2024-11-04T09:00:00+08:00/2024-11-04T10:20:00+08:00
- topic: Russell's paradox, Zermelo–Fraenkel set theory
- [Russell's paradox](../../../../general/Russell's%20paradox.md) ::@:: $$\text{Let }R=\{x\mid x\not \in x\}{\text{, then } }R\in R\iff R\not \in R$$ <p> This highlights inconsistencies in naive set theory. Zermelo–Fraenkel set theory formalizes the set theory while avoiding the above paradox.
- [Zermelo–Fraenkel set theory](../../../../general/Zermelo–Fraenkel%20set%20theory.md)
  - Zermelo–Fraenkel set theory / axiom of extensionality ::@:: Two sets are equal if and only if they have the same elements. $$\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow x=y]$$
  - Zermelo–Fraenkel set theory / axiom of empty set ::@:: There exists a set with no elements. $$\exists A\,\forall x\,(x\notin A)$$
  - Zermelo–Fraenkel set theory / axiom of pairing ::@:: If _x_ and _y_ are sets, there exists a set {_x_, _y_} whose elements are exactly _x_ and _y_. $$\forall x\forall y\exists z((x\in z)\land (y\in z))$$
  - Zermelo–Fraenkel set theory / axiom of union ::@:: The axiom of union states that for any set of sets $\mathcal F$, there is a set $A$ containing every element that is a member of some member of $\mathcal F$. $$\forall {\mathcal {F} }\,\exists A\,\forall Y\,\forall x[(x\in Y\land Y\in {\mathcal {F} })\Rightarrow x\in A]$$
  - Zermelo–Fraenkel set theory / axiom of restricted comprehension ::@:: The axiom schema of specification states that this subset always exists \(it is an [axiom _schema_](../../../../general/axiom%20schema.md) because there is one axiom for each $\varphi$\). Formally, let $\varphi$ be any formula in the language of ZFC with all free variables among $x,z,w_{1},\ldots ,w_{n}$ \($y$ is not free in $\varphi$\). Then: $$\forall z\forall w_{1}\forall w_{2}\ldots \forall w_{n}\exists y\forall x[x\in y\Leftrightarrow ((x\in z)\land \varphi (x,w_{1},w_{2},...,w_{n},z))]\,.$$ <p> Notice that $y$ cannot be inputted to $\varphi$, so this avoids Russell's paradox.
  - Zermelo–Fraenkel set theory / axiom of power set ::@:: For any set $x$, there is a set $y$ that contains every subset of $x$: $$\forall x\exists y\forall z(z\subseteq x\Rightarrow z\in y) \,.$$
- theorem: existence and uniqueness of the empty set ::@:: By the axiom of empty set, there is an empty set $x$. Let $y$ be a set with no elements. By the axiom of extensionality, they are the same.
- [ordered pair](../../../../general/ordered%20pair.md) ::@:: $$(a, b) := \set{\set{a}, \set{a, b} }$$ <p> A equality property: $(a, b) = (c, d)$ iff $a = b$ and $c = d$.
- union of sets ::@:: $$a \cup b = \bigcup \set{a, b}$$
- [Cartesian product](../../../../general/Cartesian%20product.md) ::@:: $$\begin{aligned} A\times B & =\{(a,b)\mid a\in A\ {\text{ and } }\ b\in B\} \\ A \times B & = \{x\in {\mathcal {P} }({\mathcal {P} }(A\cup B))\mid \exists a\in A\ \exists b\in B:x=(a,b) \}\end{aligned}$$
- [relation](../../../../general/relation%20(mathematics).md) ::@:: A __relation__ from $X$ to $Y$ is a subset of $X \times Y$.
- [function](../../../../general/function%20(mathematics).md) ::@:: A __function__ from $X$ to $Y$ is a relation from $X$ to $Y$ that is right-unique (for a fixed $x \in X$ in the left, $y \in Y$ is unique in the right; i.e. each $x \in X$ pairs to _at most_ 1 $y \in Y$) and left-total (there is a ordered pair with $x$ in the left for every $x \in X$; i.e. each $x \in X$ pairs to _at least_ 1 $y \in Y$).
- [questions/2024-11-04/lecture](questions/2024-11-04%20lecture.md)
- materials
  - [video playlist: intro to set theory (watch the first 10 lectures)](https://youtu.be/f_MrWycJRZ8?list=PLjJhPCaCziSQyON7NLc8Ac8ibdm6_iDQf)

## week 10 tutorial

- datetime: 2024-11-04T18:00:00+08:00/2024-11-04T18:50:00+08:00
- topic: axiom of infinity, bijections
- [Zermelo–Fraenkel set theory](../../../../general/Zermelo–Fraenkel%20set%20theory.md)
  - Zermelo–Fraenkel set theory / natural numbers ::@:: 0 is empty set. The successor is defined as: $s(n) := n \cup \set{n}$. Define inequalities: $$\begin{aligned} n & \le m && \text{if }n \subseteq m \\ n & < m && \text{if }n \subsetneq m\text{ (in this case, }n \in m\text{ also works and is equivalent)} \,.\end{aligned}$$
  - Zermelo–Fraenkel set theory / inductive set ::@:: An __inductive set__ $X$ is a set satisfying $$\begin{aligned} \emptyset & \in X \\ \forall x \quad x \in X & \implies s(x) \in X \,. \end{aligned}$$ <p> This is somewhat similar to induction using Peano axioms, but there are important differences. In particular, induction is not an axiom but a theorem using ZFC set theory.
  - Zermelo–Fraenkel set theory / unique minimal inductive set ::@:: There is an unique inductive set $\mathbb N$ that is a member of every inductive set. <p> To construct such a set, informally, take the intersection of all inductive sets. Formally, let $\Phi(I)$ is the formula that says "_I_ is inductive". There is an unique set $W$ such that $$\forall x(x\in W\leftrightarrow \forall I(\Phi (I)\to x\in I)) \,.$$ It is constructed: $$W=\{x\in I:\forall J(\Phi (J)\to x\in J)\}\,,$$ where $I$ is an inductive set.
- [axiom of infinity](../../../../general/axiom%20of%20infinity.md) ::@:: It guarantees the existence of at least one infinite set, namely a set containing the natural numbers.
- [class function](../../../../general/class%20(set%20theory).md) ::@:: In ZF, the concept of a [function](../../../../general/function%20(mathematics).md) can also be generalized to classes. A __class function__ is not a function in the usual sense, since it is not a set; it is rather a formula $\Phi (x,y)$ with the property that for any set $x$ there is no more than one set $y$ such that the pair $(x,y)$ satisfies $\Phi$. For example, the class function mapping each set to its powerset may be expressed as the formula $y={\mathcal {P} }(x)$. The fact that the ordered pair $(x,y)$ satisfies $\Phi$ may be expressed with the shorthand notation $\Phi (x)=y$.
- [finite set](../../../../general/finite%20set.md) ::@:: Formally, a set $S$ is called __finite__ if there exists a [bijection](../../../../general/bijection.md) $$f\colon S\to n$$for some natural number $n$ \(natural numbers are defined as sets in [Zermelo-Fraenkel set theory](../../../../general//Zermelo–Fraenkel%20set%20theory.md)\). The number $n$ is the set's cardinality, denoted as $|S|$.
- [infinite set](../../../../general/infinite%20set.md) ::@:: In set theory, an __infinite set__ is a set that is not a finite set. Infinite sets may be countable or uncountable.
- [bijection](../../../../general/bijection.md) ::@:: A __bijection__, __bijective function__, or __one-to-one correspondence__ between two mathematical [sets](../../../../general/set%20(mathematics).md) is a [function](../../../../general/function%20(mathematics).md) such that each element of the second set \(the [codomain](../../../../general/codomain.md)\) is the image of exactly one element of the first set \(the [domain](../../../../general/domain%20of%20a%20function.md)\). <p> Simple properties: $$\begin{aligned} \lvert x \rvert & = \lvert x \rvert \\ \lvert x \rvert = \lvert y \rvert & \iff \lvert y \rvert = \lvert x \rvert \\ \lvert x \rvert = \lvert y \rvert \text{ and } \lvert y \rvert = \lvert z \rvert & \implies \lvert x \rvert = \lvert z \rvert \,. \end{aligned}$$
  - bijection / countable examples ::@:: $$\begin{aligned} \lvert \mathbb N \rvert & = \lvert E \rvert && \text{even numbers} \\ & = \lvert \mathbb P \rvert \\ & = \lvert \mathbb N^k \rvert && k \in \mathbb N \\ & = \left\lvert \bigcup_{k = 1}^\infty \mathbb N^k \right\rvert && \text{countable union of countable sets is countable} \,. \end{aligned}$$ <p> (The countably infinite union case additionally requires the axiom of countable choice.)
- [injective function](../../../../general/injective%20function.md)
  - injective function / cardinality ::@:: If there is an injective function from $X$ to $Y$, then $\lvert X \rvert \le \lvert Y \rvert$.
- [questions/2024-11-04/tutorial](questions/2024-11-04%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/BrOH1_eoAaA)
  - [reading: Oxford lecture notes on set theory (pages 1-20)](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf)
  - [video: Hilbert hotel](https://youtu.be/OxGsU8oIWjY)

## week 10 lecture 2

- datetime: 2024-11-06T09:00:00+08:00/2024-11-06T10:20:00+08:00
- topic: countability, Cantor's theorem, Tarski's theorem, Schröder–Bernstein theorem
- assignments: [homework 3](assignments/homework%203/submission.md)
- bijection & cardinality
- injection & cardinality
- image of a function
- [countable set](../../../../general/countable%20set.md) ::@:: A set is countable iff it has the same cardinality as the natural numbers.
- [uncountable set](../../../../general/uncountable%20set.md)
- theorem: infinite set minus finite set ::@:: An infinite set minus a finite set is still infinite.
- theorem: countably infinite subset in an infinite set ::@:: There is a countably infinite subset in an infinite set. One can keep extracting an element from an infinite set to make a countably infinite subset.
- theorem: countable (finite or infinite) set plus countable (finite or infinite) set ::@:: A countable union of countable sets is countable. <p> (The countably infinite union case additionally requires the axiom of countable choice.)
- theorem: natural numbers, rational numbers ::@:: $$\lvert \mathbb N \rvert = \lvert \mathbb Q \rvert$$
- theorem: set of functions from the natural numbers to either 0 or 1 ::@:: The set of functions from the natural numbers to either 0 or 1 is uncountable. First, interpret the functions as "real numbers". For example, for a function _f_, the _i_-th digit is _f_(_i_). Apply Cantor's diagonal argument.
- [Cantor's theorem](../../../../general/Cantor's%20theorem.md) ::@:: For every set $A$ (including the empty set), $\lvert A \rvert < \lvert P(A) \rvert$. <p> To prove this, assume the existence of a bijection $f$ between $A$ and $P(A)$ and consider the set $T = \set{a \in A \mid a \notin f(a)} \subseteq P(A)$.
- Tarski's theorem ([Knaster–Tarski theorem](../../../../general/Knaster–Tarski%20theorem.md)) ::@:: Let $X$ be a set and $h : P(X) \to P(X)$ be a monotone map, i.e. $A \subseteq B \implies h(A) \subseteq h(B)$. Then $X$ admits an _invariant set_ $A \in P(X)$, i.e. $A = h(A)$. <p> To prove this, consider an _expansive set_, i.e. $A \subseteq h(A)$. Then the union of expansive sets is expansive itself. Now consider the union of all expansive sets, e.g. $$C = \bigcup \set{A \in P(X) \mid A \subseteq h(A)} \,.$$ We claim that $C = h(C)$. First $C$ is expansive, so $C \subseteq h(C)$. Next, since $C \subseteq h(C)$, so $h(C) \subseteq h(h(C))$, thus $h(C)$ is expansive. Since $h(C)$ is expansive, $h(C) \subseteq C$. Combining the above results, $C = h(C)$.
- [Schröder–Bernstein theorem](../../../../general/Schröder–Bernstein%20theorem.md) ::@:: If $\lvert X \rvert \le \lvert Y \rvert$ and $\lvert Y \rvert \le \lvert X \rvert$, then $\lvert X \rvert = \lvert Y \rvert$. Equivalently, if there are two injective functions $f: X \to Y$ and $g: Y \to X$, then there is an bijection between them. <p> If we assume the axiom of choice, then a pair of surjective functions $f$ and $g$ also implies the existence of a bijection, by constructing injective functions from their inverses $f^{-1}$ and $g^{-1}$. <p> To prove this, consider two injective functions $f: A \to B$ and $g: B \to A$. Consider double-ended chains alternating between elements in $A$ and $B$ starting from any element in either $A$ or $B$. As an example: $$\cdots \rightarrow f^{-1}(g^{-1}(a))\rightarrow g^{-1}(a)\rightarrow a\rightarrow f(a)\rightarrow g(f(a))\rightarrow \cdots$$. There may be infinitely many above such chains. However, for any fixed element in either $A$ or $B$, the element is in exactly one chain only, by the injective-ness of $f$ and $g$. The chain may start at an element of $A$ (if $g^{-1}(a)$ is undefined), an element of $B$ (if $f^{-1}(b)$ is undefined), is doubly infinite, or is a cycle. In all of the above cases, a bijection can be defined for elements in the chain.
- [questions/2024-11-06](questions/2024-11-06.md)
- [week 10 problem set](questions/week%2010%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/jDqQlQLODzQ)
  - [reading: Oxford lecture notes on set theory (pages 1-26)](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf)

## week 10 TA session

- datetime: 2024-11-08T13:00:00+08:00/2024-11-08T13:50:00+08:00
- topic: solving weekly problem set 7
- [questions/2024-11-08](questions/2024-11-08.md)
- [week 8 problem set](questions/week%208%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/DuKFaBTdHt0)

## week 11 lecture

- datetime: 2024-11-11T09:00:00+08:00/2024-11-11T10:20:00+08:00
- topic: set of real numbers
- [decimal](../../../../general/decimal.md) ::@:: The __decimal numeral system__ is the standard system for denoting integer and non-integer numbers.
- [decimal representation](../../../../general/decimal%20representation.md) ::@:: A decimal representation is an infinite sequence. Terminating decimals can be treated as an infinite sequence by considering it as finite sequence followed by an infinite sequence of repeating 0s. <p> If a number can be represented by a finite sequence followed by a infinite sequence that is a repeat of a finite sequence, then it is rational. The converse is also true.
- [total order](../../../../general/total%20order.md) ::@:: (non-formal) A __total order__ on a set $A$ is a relation $<$ or $\le$ such that for every $a, b \in A$ exactly one of $a < b$, $a = b$, or $a > b$ is true, and for every $a, b, c \in A$, $a < b \land b < c \implies a < c$.
- [upper and lower bounds](../../../../general/upper%20and%20lower%20bounds.md) ::@:: An __upper bound__ or __majorant__ of a [subset](../../../../general/subset.md) _S_ of some [preordered set](../../../../general/preorder.md) \(_K_, ≤\) is an element of _K_ that is [greater than or equal to](../../../../general/inequality%20(mathematics).md) every element of _S_.
- [infimum and supremum](../../../../general/infimum%20and%20supremum.md)
  - [infimum and supremum](../../../../general/infimum%20and%20supremum.md) / supremum ::@:: The __supremum__ \(abbreviated __sup__; pl.: __suprema__\) of a subset $S$ of a partially ordered set $P$ is the [least element](../../../../general/greatest%20element%20and%20least%20element.md) in $P$ that is greater than or equal to each element of $S,$ if such an element exists. If the supremum of $S$ exists, it is unique, and if _b_ is an [upper bound](../../../../general/upper%20and%20lower%20bounds.md) of $S$, then the supremum of $S$ is less than or equal to _b_. Consequently, the supremum is also referred to as the _least upper bound_ \(or LUB\).
  - [infimum and supremum](../../../../general/infimum%20and%20supremum.md) / infimum ::@:: The __infimum__ \(abbreviated __inf__; pl.: __infima__\) of a [subset](../../../../general/subset.md) $S$ of a [partially ordered set](../../../../general/partially%20ordered%20set.md) $P$ is the [greatest element](../../../../general/greatest%20element%20and%20least%20element.md) in $P$ that is less than or equal to each element of $S,$ if such an element exists. If the infimum of $S$ exists, it is unique, and if _b_ is a [lower bound](../../../../general/upper%20and%20lower%20bounds.md) of $S$, then _b_ is less than or equal to the infimum of $S$. Consequently, the term _greatest lower bound_ \(abbreviated as GLB\) is also commonly used.
- [least-upper-bound property](../../../../general/least-upper-bound%20property.md) ::@:: In [mathematics](../../../../general/mathematics.md), the __least-upper-bound property__ \(sometimes called __completeness__, __supremum property__ or __l.u.b. property__\) is a fundamental property of the [real numbers](../../../../general/real%20number.md). More generally, a [partially ordered set](../../../../general/partially%20ordered%20set.md) _X_ has the least-upper-bound property if every non-empty [subset](../../../../general/set%20(mathematics).md) of _X_ with an [upper bound](../../../../general/upper%20and%20lower%20bounds.md) has a [_least_ upper bound](../../../../general/infimum%20and%20supremum.md) \(supremum\) in _X_. Not every \(partially\) ordered set has the least upper bound property. For example, the set $\mathbb {Q}$ of all [rational numbers](../../../../general/rational%20number.md) with its natural order does _not_ have the least upper bound property.
  - least-upper-bound property / rational numbers counterexample ::@:: Consider the set $\set{p \in \mathbb Q \mid 0 \le x \land x^2 \le 2}$. If we were working with real numbers, the supremum of such a set would be $\sqrt 2$. But we know that $\sqrt 2$ is not a rational number. <p> We can show that while there are upper bounds for the above set, there is no _least_ upper bound. <p> To prove this, assume there is a least upper bound $s$. Split into three cases: $s^2 < 2$, $s^2 = 2$, and $s^2 > 2$. For the middle case, we can easily show $s$ is not a rational number. For the first case, construct a rational number $q \in \mathbb Q$ such that $s^2 < q < 2$. This proves $s$ is not a upper bound. For the third case, construct a rational number $q \in \mathbb Q$ such that $2 < q < s^2$. This proves $s$ is not the _least_ upper bound.
  - least-upper-bound property / greatest-lower-bound property ::@:: The __greatest-lower-bound property__ can be defined analogously. However, we generally do not care since it is equivalent to the _least-upper-bound property_. <p> To prove this from the _least-upper-bound property_, consider the a set $A$ that is bounded below. Consider the set of $A$<!-- LaTeX separator -->'s lower bounds, $L$. The set of its lower bounds $L$ has $A$ as a subset of $L$<!-- LaTeX separator -->'s upper bounds. By the _least-upper-bound property_, $L$ has a supremum $a$. By the definition of supremum and above, $a$ is a lower bound of $A$. $a$ is also the greatest lower bound as a supremum of $L$. <p> The opposite direction can be proved analogously.
- [Dedekind cut](../../../../general/Dedekind%20cut.md) ::@:: __Dedekind cuts__ are а method of [construction of the real numbers](../../../../general/construction%20of%20the%20real%20numbers.md) from the [rational numbers](../../../../genera/rational%20number.md). A Dedekind cut is a [partition](../../../../general/partition%20of%20a%20set.md) of the rational numbers into two [sets](../../../../general/set%20(mathematics).md) _A_ and _B_, such that each element of _A_ is less than every element of _B_, and _A_ contains no [greatest element](../../../../general/greatest%20element%20and%20least%20element.md). The set _B_ may or may not have a smallest element among the rationals. If _B_ has a smallest element among the rationals, the cut corresponds to that rational. Otherwise, that cut defines a unique [irrational number](../../../../general/irrational%20number.md) which, loosely speaking, fills the "gap" between _A_ and _B_. In other words, _A_ contains every rational number less than the cut, and _B_ contains every rational number greater than or equal to the cut. An irrational cut is equated to an irrational number which is in neither set. Every real number, rational or not, is equated to one and only one cut of rationals.
  - Dedekind cut / least-upper-bound property ::@:: Construct the real numbers using Dedekind cuts: $$\mathbb R = \set{A \subseteq Q \mid A\text{ is the left partition of a Dedekind cut} } \,.$$ The real numbers have the least-upper-bound property. <p> Consider an nonempty set of real numbers $X$. We note that $a \le b$ corresponds to $a \subseteq b$ in the Dedekind cut definition. The least upper bound of $X$ is then $\bigcup X$. <p> We can prove that $\bigcup X$ is itself a Dedekind cut, so $X \in \mathbb R$. To prove this, prove if any rational number $q \in \mathbb Q$ is smaller than any real number in $X$, then $q \in \bigcup X$. Then prove $\bigcup U$ does not have a maximum.
  - Dedekind cut / decimal representation ::@:: Any decimal representation is a real number. <p> If the decimal is a finite sequence followed by a repeating infinite sequence, then it is rational, and thus real. <p> Otherwise, the decimal representation is an infinite sequence. We can always truncate the decimal representation after a finite number of digits. Any truncation produces a rational number. Then the real number represented by the decimal representation is defined by a left partition of a Dedekind cut that contains the rational numbers produced by all truncations of the decimal representation. So it is also a real number.
- [questions/2024-11-11/lecture](questions/2024-11-11%20lecture.md)
- materials
  - [lecture video](https://youtu.be/3ug4MK_VNZQ)
  - [video: real numbers](https://youtu.be/N4I0Ay4RvjU?list=PLjJhPCaCziSQyON7NLc8Ac8ibdm6_iDQf&index=19)
  - [video: equinumerosity](https://youtu.be/avXuA-yDQwc?list=PLjJhPCaCziSQyON7NLc8Ac8ibdm6_iDQf&index=20)

## week 11 tutorial

- datetime: 2024-11-11T18:00:00+08:00/2024-11-11T18:50:00+08:00
- topic: $\lvert \mathbb R \rvert = \lvert P(\mathbb N) \rvert$, axiom of choice
- [interval](../../../../general/interval%20(mathematics).md) ::@:: Amir defines intervals! Examples: $[a, b]$, $(a, b)$, $(a, +\infty)$, $(-\infty, a)$, $(a, b]$ $[a, b)$, $(-\infty, a]$, and $[a, +\infty)$.
- theorem: cardinality, real interval ::@:: All nontrivial real intervals (regardless if the endpoints are included or not) have the same cardinality. <p> To prove this, we need to prove two things. If two intervals have the same $a$ and $b$ but the endpoints differ in whether they are included, we can extract a countably infinite set from each interval, including the endpoints if the endpoints are included in the interval. These countably infinite sets have the same cardinality, thus has a bijection. Then the remaining real numbers in the interval has the identity function as a bijection. <p> If two intervals have differing $a$ and $b$ but the same endpoint inclusiveness, we can easily make a bijection by "scaling" an interval onto the other. <p> The above two cases can handle any nontrivial real intervals, since bijection is transitive.
- theorem: rational numbers are a dense subset of the real numbers ::@:: There always exists a rational number in between two different real numbers. <p> This is easy to see using the Dedekind cut definition.
  - [dense set](../../../../general/dense%20set.md)
  - [rational number § real numbers and topological properties](../../../../general/rational%20number.md#real%20numbers%20and%20topological%20properties)
- theorem: power set of natural numbers, real numbers ::@:: $$\lvert \mathbb R \rvert = \lvert P(\mathbb N) \rvert$$ <p> To prove this, prove $\lvert \mathbb R \rvert \le \lvert P(\mathbb Q) \rvert = \lvert P(\mathbb N) \rvert$ by constructing an injection. This is easily seen using the Dedekind cut definition of the real numbers. <p> Next, prove $\lvert P(\mathbb N) \rvert \le \lvert \mathbb R \rvert$ by constructing an injection. Consider a set from the power set of all natural numbers. The set can be mapped into a real number. If $n$ is in the set, then the $n$-th digit is 1, otherwise 0. If the set has a largest natural number $n'$ (implying the set is finite), then after doing the above replacement, we perform the additional replacement: the $n'$-th digit becomes 0 back from 1, but the digits after the $n'$-th digit becomes all 9s from all 0s.
- [axiom of choice](../../../../general/axiom%20of%20choice.md) :;@:: The __axiom of choice__, abbreviated __AC__ or __AoC__, is an [axiom](../../../../general/axiom.md) of [set theory](../../../../general/set%20theory.md) equivalent to the statement that _a [Cartesian product](../../../../general/Cartesian%20product.md) of a collection of non-empty sets is non-empty_. Informally put, the axiom of choice says that given any collection of sets, each containing at least one element, it is possible to construct a new set by choosing one element from each set, even if the collection is [infinite](infinite%20set.md).
  - axiom of choice / non-usage ::@:: In many cases, a set created by choosing elements can be made without invoking the axiom of choice, particularly if the number of sets from which to choose the elements is finite, or if a canonical rule on how to choose the elements is available — some distinguishing property that happens to hold for exactly one element in each set.
  - axiom of choice / equivalents: [trichotomy](../../../../general/law%20of%20trichotomy.md) ::@:: For any two sets $A$ and $B$, exactly one of the following holds: $\lvert A \rvert < \lvert B \rvert$, $\lvert A \rvert = \lvert B \rvert$, and $\lvert A \rvert > \lvert B \rvert$. <p> The above statement is equivalent to the axiom of choice, but the proof is not given here.
    - [law of trichotomy](../../../../general/law%20of%20trichotomy.md)
  - axiom of choice / equivalents: function, relation ::@:: For any relation _R_ from set _X_ to set _Y_, there exists a function from the domain of the relation on set _X_ to set _Y_, using the axiom of choice. <p> This is simple to see: For each element _x_ in the domain of _R_, we can choose one mapping out of the many possible mapping containing _x_. Since the domain may be infinite, and we are choosing one mapping from a possibly infinite set, we need to invoke the axiom of choice. <p> The above statement is equivalent to the axiom of choice, but the converse proof is not given here.
  - axiom of choice / equivalents: function, power set to set ::@:: There exists a function $F : P(A) \setminus \set{\emptyset} \to A$ such that $\forall B \in P(A) \setminus \set{\emptyset} \quad F(B) \in B$, invoking the axiom of choice. <p> This is simple to see: For any nonempty set in the power set, we can always choose an element in the set to be the output of the function. This invokes the axiom of choice since the power set may be infinite. <p> The above statement is equivalent to the axiom of choice, but the converse proof is not given here.
  - axiom of choice / equivalents: [Zorn's lemma](../../../../general/Zorn's%20lemma.md) ::@:: __Zorn's lemma__ is a proposition of [set theory](../../../../general/set%20theory.md). It states that a [partially ordered set](../../../../general/partially%20ordered%20set.md) containing [upper bounds](../../../../general/upper%20and%20lower%20bounds.md) for every [chain](../../../../general/total%20order.md#chains) \(that is, every [totally ordered](../../../../general/total%20order.md) [subset](../../../../general/subset.md)\) <!-- [necessarily](../../../../general/necessity%20and%20sufficiency.md) --> contains at least one [maximal element](../../../../general/maximal%20and%20minimal%20elements.md) (an element that is not smaller than any other element, but it need not be the maximum, which is an element that is greater or equal to all other elements).
    - [Zorn's lemma](../../../../general/Zorn's%20lemma.md)
  - axiom of choice / equivalents: Zorn's lemma → trichotomy ::@:: Consider two sets $A$ and $B$. Consider the set of all bijections between a subset of $A$ to a subset of $B$. For convenience, treat each bijection as a bipartite graph. The set of said functions is a partially ordered set by defining the $f \le g$ iff $f$ is a subgraph of $g$ (non-graph theorist: $f$ is a restriction of $g$: $g$ maps the domain of $f$ to the co-domain of $f$ in the exact way as $f$). Any chain in this partially ordered set has a upper bound: simply take the union of edges of all bijections in the chain, which is still a bijection. By Zorn's lemma, there is a maximal bijection, a bijection that is not a subset of any other bijection. Then we can prove this maximal bijection either covers all of $A$ or all of $B$, or both. If this is not the case, the maximal bijection can be expanded by adding an additional edge, which is a contradiction.
- [questions/2024-11-11/tutorial](questions/2024-11-11%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/alEZAD8u-5k)
  - [video: the halting problem (watch the first 18 minutes)](https://youtu.be/-y2iOKPEX9U)
  - [video: cardinality of the continuum](https://youtu.be/iaUwNuaSLUk)
  - [video: comparability of cardinals](https://youtu.be/ObyrXnEnj0k?list=PLjJhPCaCziSQyON7NLc8Ac8ibdm6_iDQf&index=28)
  - [video: axiom of choice](https://youtu.be/qH_4UwExY0w?list=PLjJhPCaCziSQyON7NLc8Ac8ibdm6_iDQf&index=30)
  - [recommended: history of the axiom of choice](https://youtu.be/5UJWIwKa8vk)
  - [recommended to read: Banach–Tarski paradox](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox)
    - [Banach–Tarski paradox](../../../../general/Banach–Tarski%20paradox.md)

## week 11 lecture 2

- datetime: 2024-11-13T09:00:00+08:00/2024-11-13T10:20:00+08:00
- topic: introduction to probability theory
- [probability theory](../../../../general/probability%20theory.md)
  - probability theory / introduction ::@:: Consider tossing a coin. We are interested in the proportion of the number of heads over the number of tosses as the number of tosses approaches infinity.
- [Monty Hall problem](../../../../general/Monty%20Hall%20problem.md) ::@:: Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice? <p> Savant's response was that the contestant should switch to the other door. By the standard assumptions, the switching strategy has a ⁠2/3⁠ [probability](../../../../general/probability.md) of winning the car, while the strategy of keeping the initial choice has only a ⁠1/3⁠ probability.
- [Sleeping Beauty problem](../../../../general/Sleeping%20Beauty%20problem.md) ::@:: The __Sleeping Beauty problem__, also known as the __Sleeping Beauty paradox__, is a puzzle in [decision theory](../../../../general/decision%20theory.md) in which an ideally rational [epistemic](../../../../general/epistemology.md) agent is told she will be awoken from sleep either once or twice according to the [toss of a coin](../../../../general/coin%20flipping.md). Each time she will have no memory of whether she has been awoken before, and is asked what her [degree of belief](../../../../general/credence%20(statistics).md) that the outcome of the coin toss is Heads ought to be when she is first awakened. <p> This problem continues to produce ongoing debate. Amir talks about the thirder position, that is, the probability of heads is 1/3.
- [base rate fallacy](../../../../general/base%20rate%20fallacy.md)
  - base rate fallacy / example ::@:: If you have/do not have cancer, the test says positive/negative with 0.9 probability. You take the test and it's positive. What is the probability you have cancer? <p> Idea: The actual probability that you have cancer is not only dependent on the test, but is also dependent on what proportion of the population has cancer.
- [extended real number line](../../../../general/extended%20real%20number%20line.md) ::@:: It extends the real number line by adding positive infinity and negative infinity. <p> Not to be confused with the [projectively extended real line](../../../../general/projectively%20extended%20real%20line.md), which adds a single infinity that represents both "positive" infinity and "negative" infinity.
  - [projectively extended real line](../../../../general/projectively%20extended%20real%20line.md)
- [measure space](../../../../general/measure%20space.md) ::@:: A __measure space__ is a triple $(X,{\mathcal {A} },\mu )$, where $X$ is a set, ${\mathcal {A} }$ is a [_σ_-algebra](../../../../general/σ-algebra.md) on the set $X$, and $\mu$ is a [measure](../../../../general/measure%20(mathematics).md) on $(X,{\mathcal {A} })$ <p> In other words, a measure space consists of a [measurable space](../../../../general/measurable%20space.md) $(X,{\mathcal {A} })$ together with a [measure](../../../../general/measure%20(mathematics).md) on it.
- [_σ_-algebra](../../../../general/σ-algebra.md) ::@:: A __σ-algebra__ on a set _X_ is a nonempty collection Σ of [subsets](../../../../general/subset.md) of _X_ [closed](../../../../general/closure%20(mathematics).md) under [complement](../../../../general/complement%20(set%20theory).md), countable [unions](../../../../general/union%20(set%20theory).md), and countable [intersections](../../../../general/intersection%20(set%20theory).md) (the last one is not part of the definition, but can be obtained by applying [De Morgan's laws](../../../../general/De%20Morgan's%20laws.md)). The ordered pair $(X,\Sigma )$ is called a [measurable space](../../../../general/measurable%20space.md). <p> The smallest possible σ-algebra on _X_ is $\set{X, \emptyset}$. The largest possible σ-algebra on _X_ is $P(X)$.
- [measure](../../../../general/measure%20(mathematics).md) ::@:: The concept of a __measure__ is a generalization and formalization of [geometrical measures](../../../../general/geometry.md#measures) \([length](../../../../general/length.md), [area](../../../../general/area.md), [volume](../../../../general/volume.md)\) and other common notions, such as [magnitude](../../../../general/magnitude%20(mathematics).md), [mass](../../../../general/mass.md), and [probability](../../../../general/probability.md) of events. <p> Let $X$ be a set and $\Sigma$ a [$\sigma$-algebra](../../../../general/σ-algebra.md) over $X$. A [set function](../../../../general/set%20function.md) $\mu$ from $\Sigma$ to the [extended real number line](../../../../general/extended%20real%20number%20line.md) is called a __measure__ if the following conditions hold: <br/> __Non-negativity__: For all $E\in \Sigma ,\ \ \mu (E)\geq 0.$ <br/> $\mu (\varnothing )=0.$ <br/> __Countable additivity__ \(or [$\sigma$-additivity](../../../../general/sigma-additive%20set%20function.md)\): For all [countable](../../../../general/countable%20set.md) collections $\{E_{k}\}_{k=1}^{\infty }$ of pairwise [disjoint sets](../../../../general/disjoint%20sets.md) in Σ, $\mu \left(\bigcup _{k=1}^{\infty }E_{k}\right)=\sum _{k=1}^{\infty }\mu (E_{k}) \,.$
- [Lebesgue measure](../../../../general/Lebesgue%20measure.md) ::@:: For any [interval](../../../../general/interval%20(mathematics).md) $I=[a,b]$, or $I=(a,b)$, in the set $\mathbb {R}$ of real numbers, let $\ell (I)=b-a$ denote its length. For any subset $E\subseteq \mathbb {R}$, the Lebesgue [outer measure](../../../../general/outer%20measure.md) $\lambda ^{\!*\!}(E)$ is defined as an [infimum](../../../../general/infimum%20and%20supremum.md) $$\lambda ^{\!*\!}(E)=\inf \left\{\sum _{k=1}^{\infty }\ell (I_{k}):{(I_{k})_{k\in \mathbb {N} } }{\text{ is a sequence of open intervals with } }E\subset \bigcup _{k=1}^{\infty }I_{k}\right\}.$$ <p> The first part of the definition states that the subset $E$ of the real numbers is reduced to its outer measure by coverage by sets of open intervals. Each of these sets of intervals $I$ covers $E$ in a sense, since the union of these intervals contains $E$. The total length of any covering interval set may overestimate the measure of $E,$ because $E$ is a subset of the union of the intervals, and so the intervals may include points which are not in $E$. The Lebesgue outer measure emerges as the [greatest lower bound \(infimum\)](../../../../general/infimum%20and%20supremum.md) of the lengths from among all possible such sets. Intuitively, it is the total length of those interval sets which fit $E$ most tightly and do not overlap.
  - [Carathéodory's criterion](../../../../general/Carathéodory's%20criterion.md) ::@:: Some sets $E$ satisfy the [Carathéodory criterion](../../../../general/Carathéodory's%20criterion.md), which requires that for every $A\subseteq \mathbb {R}$, $$\lambda ^{\!*\!}(A)=\lambda ^{\!*\!}(A\cap E)+\lambda ^{\!*\!}(A\cap E^{c}).$$ <p> The sets $E$ that satisfy the Carathéodory criterion are said to be Lebesgue-measurable, with its Lebesgue measure being defined as its Lebesgue outer measure: $\lambda (E)=\lambda ^{\!*\!}(E)$. The set of all such $E$ forms a [_σ_-algebra](../../../../general/σ-algebra.md).
- [probability measure](../../../../general/probability%20measure.md) ::@:: A __probability measure__ is a [real-valued function](../../../../general/real-valued%20function.md) defined on a set of events in a [σ-algebra](../../../../general/σ-algebra.md) that satisfies [measure](../../../../general/measure%20(mathematics).md) properties such as _countable additivity_. The difference between a probability measure and the more general notion of measure \(which includes concepts like [area](../../../../general/area.md) or [volume](../../../../general/volume.md)\) is that a probability measure must assign value 1 to the entire space.
- [questions/2024-11-13](questions/2024-11-13.md)
- [week 11 problem set](questions/week%2011%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/oGnHcUPsdYA)
  - [`coin.cpp`](attachments/coin.cpp)
  - [`doors.cpp`](attachments/doors.cpp)
  - [`sleeping.cpp`](attachments/sleeping.cpp)
  - [`cancer.cpp`](attachments/cancer.cpp)
  - Ross/Chapter 2: Axioms of Probability \(including sections marked by \*\)

## week 11 TA session

- datetime: 2024-11-15T17:00:00+08:00/2024-11-15T17:50:00+08:00
- topic: solving weekly problem set 8
- [questions/2024-11-15](questions/2024-11-15.md)
- [week 9 problem set](questions/week%209%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/NKTfCcjnF-Q)

## week 12 lecture

- datetime: 2024-11-18T09:00:00+08:00/2024-11-18T10:20:00+08:00
- topic: conditional probability, independence, expectation
- [conditional probability](../../../../general/conditional%20probability.md) ::@:: The __conditional probability__ of an event _A_ given that an event _B_, where _P_(_B_) > 0, has happened is: $$P(A \mid B) = \frac {P(A \cap B)} {P(B)} \,.$$ A property: $P(A \mid B) \ge P(A \cap B)$.
  - conditional probability / motivation ::@:: Knowing an event has happened may modify the probability of other events. Conditional probability can model this.
  - conditional probability / multiplicative rule ::@:: If _P_(_B_) > 0, then $$P(A \cap B) = P(A \mid B) P(B) \,.$$ This may be directly proved from the definition of conditional probability. Sometimes, the above is taken to be the definition of conditional probability instead (but not in this course).
  - conditional probability / conserved properties ::@:: Many other properties of probability hold under conditional probability. This can be easily seen by making the event that has happened to be the sample space instead. Example: $$\begin{aligned} P(A \mid B) & = 1 - P\left(A^\complement \mid B \right) \\ P(A \cup B \mid C) & = P(A \mid C) + P(B \mid C) - P(A \cap B \mid C) \\ P(A \cap B \mid C) & = P(A \mid B \cap C) P(B \mid C) \,. \end{aligned}$$ For the last example, if you reinterpret _C_ as the sample space, then $P(A \mid B \cap C)$ becomes $P(A \mid B)$.
- [independence](../../../../general/independence%20(probability%20theory).md) ::@:: Two events _A_ and _B_ are __independent__ iff $$P(A \cap B) = P(A) P(B) \,.$$ otherwise they are __dependent__. <p> Informally speaking, knowing either of the event has happened does not affect the probability of the other.
  - independence / equivalence ::@:: The following statements are equivalent: <ul> <li>_A_ and _B_ are independent.</li> <li>_A_ and _B_<sup>c</sup> are independent.</li> <li>_A_<sup>c</sup> and _B_ are independent.</li> <li>_A_<sup>c</sup> and _B_<sup>c</sup> are independent.</li> </ul> The above can be seen by seeing that the complement of an event is uniquely defined by the event. There is a one-to-one correspondence between a set and its complement (unless the sample space is the empty set, which is impossible for probability).
  - independence vs disjoint ::@:: Independent is not disjoint. End of story.
  - independence / pairwise independence ::@:: A finite set of events is __pairwise independent__ iff any two events from the set is _independent_. <p> Pairwise independence does NOT automatically imply _mutual independence_.
  - independence / mutual independence ::@:: A finite set of _n_ events is __mutually independent__ iff any 2 ≤ _k_ ≤ _n_ events from the set is _independent_. For the _independence_ of 2 ≤ _k_ events, this is simply: $$P\left(\bigcap_{i = 1}^k A_k \right) = \prod_{i = 1}^k A_k \,.$$ <p> Mutual independence automatically implies _pairwise independence_. However, note that the above statement must hold for all 2 ≤ _k_ ≤ _n_, not just _k_ = _n_. It is possible to create a sample space such that three events _A_, _B_, and _C_ are independent but none of the three events are _pairwise independent_.
- [law of total probability](../../../../general/law%20of%20total%20probability.md#statement) ::@:: If $$\left\{ B_n : n = 1, 2, 3, \ldots \right\}$$ is a _finite or countably infinite_ set of _mutually exclusive_ and _collectively exhaustive_ events $$P(A)=\sum_n P(A\mid B_n)P(B_n) \,,$$ where, for any $n$, if $P(B_n) = 0$, then these terms are simply omitted from the summation since $P(A\mid B_n)$ is finite. <p> The set of $B_n$ is also known as a __partition__ of the sample space.
- [random variable](../../../../general/random%20variable.md) (r.v.) ::@:: A __random variable__ (__r.v.__) is a mathematical function. Its _domain_ is the sample space. Its _range_ is a measurable space, usually a finite set of integers or the real numbers. The function need not be _injective_ (different samples need not map to different values). It is commonly denoted by capital letters, with its possible numerical values (also called __realizations__) by the same but lowercase letters. <p> A way to think about random variable is that it maps each outcome to a real number.
  - random variable / motivation ::@:: How do we describe random process more mathematically? Random variables can do so.
  - random variable / notations ::@:: Some notations for a random variable _X_ on the sample space _S_: $$\begin{aligned} \set{X = x} & = \set{s \in S \mid X(s) = x} \\ \set{X \le x} & = \set{s \in S \mid X(s) \le x} \\ P(X = x) & = P(\set{X = x}) \\ P(X \le x) & = P(\set{X \le x}) \end{aligned}$$
  - random variable / types ::@:: There are two common types: _discrete_ random variables and _continuous_ random variables. If a random variable's range is _countable_ (finite or infinite), then the random variable is discrete. if a random variable's range is _uncountable_ and its _cumulative probability distribution_ (CDF) is _continuous everywhere_, then the random variable is continuous. <p> Other types not discussed here are _mixed_ random variables (a mix of discrete and continuous) and _singular_ random variables (neither discrete nor continuous).
- [expected value](../../../../general/expected%20value.md) ::@:: The __expected value__ (__population mean__, __first moment__) is a generalization of the weighted average. Informally, the expected value is the mean of the possible values a random variable can take, weighted by the probability of those outcomes. It is commonly denoted $E(X)$.
  - expected value / discrete random variable ::@:: The expected value of a discrete random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \sum_{x \in \mathcal X} x p(x) \,.$$ This is only defined if the sum converges absolutely, so it is possible for a discrete random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \sum_{x \in \mathcal X} g(x) p(x) \,.$$ for an arbitrary function $g(x)$.
  - expected value / linearity ::@:: An important property is its linearity: $$\begin{aligned} E(b) & = b \\ E(aX) & = a E(X) \\ E(aX + b) & = a E(x) + b \\ E(aX + bY) & = a E(x) + b E(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$
- [Monty Hall problem](../../../../general/Monty%20Hall%20problem.md)
- [Sleeping Beauty problem](../../../../general/Sleeping%20Beauty%20problem.md)
- not taught in class
  - [variance](../../../../general/variance.md) ::@:: __Variance__ is the expected value of the squared deviation from the mean of a random variable. It is often represented by $\sigma ^{2}$, $s^{2}$, $\operatorname {Var} (X)$, $V(X)$, or $\mathbb {V} (X)$.
    - variance / discrete random variable ::@:: The variance fo a discrete random variable is $$\operatorname{Var}(X) = \sum_{x \in \mathcal X} \left((x - \mu)^2 p(x) \right) \,.$$ This is only defined if the sum exists, so it is possible for a discrete random variable to have undefined variance.
    - variance / properties ::@:: A well-known identity relating variance to expected value is $$\operatorname{Var}(X) = \operatorname E\left[X^2\right] - (\operatorname E[X])^2 = \operatorname E\left[X^2\right] - \mu^2 \,.$$ With this identity, the following properties can be proved: $$\begin{aligned} \operatorname{Var}(b) = 0 \\ \operatorname{Var}(aX) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + b) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + bY) & = a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$
  - [binomial distribution](../../../../general/binomial%20distribution.md) ::@:: The __binomial distribution__ with parameters _n_ and _p_ is the discrete probability distribution of the number of successes in a sequence of $n \in \mathbb N_0$ independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability $p \in [0, 1]$) or failure (with probability $q = 1 - p$). It is denoted $B(n, p)$.
    - binomial distribution / random variable ::@:: A single trial (_n_ = 1) is also known as a __Bernoulli trial__. Its random variable is: $$p(x) = \begin{cases} p & \text{for }x = 1 \\ 1 - p & \text{for }x = 0 \\ 0 & \text{otherwise} \,, \end{cases}$$ or sometimes more conveniently, $$p(x) = \begin{cases} p^x (1 - p)^{1 - x} & \text{for }x \in \set{0, 1} \\ 0 & \text{otherwise} \,. \end{cases}$$
    - binomial distribution / proof of being probability distribution ::@:: It is very easy to see that its probability mass function is nonnegative. To see that it sums up to 1, apply the binomial theorem in reverse.
    - binomial distribution / probability _mass_ function ::@:: For $X \sim B(n, p) \,,$ $$p_X(k) = \binom n k p^k (1 - p)^{n - k}\,.$$
    - binomial distribution / mean ::@:: For $X \sim B(n, p) \,,$ $$\operatorname E[X] = np \,.$$
    - binomial distribution / variance ::@:: For $X \sim B(n, p) \,,$ $$\operatorname{Var}(X) = np(1 - p) \,.$$
  - [Poisson distribution](../../../../general/Poisson%20distribution.md) ::@:: The __Poisson distribution__ is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time if these events occur with a known constant mean rate and independently of the time since the last event. It can also be used for the number of events in other types of intervals than time, and in dimension greater than 1 (e.g., number of events in a given area or volume). It is denoted $\operatorname{Pois}(\lambda)$, where $\lambda \in (0, \infty)$ is the expectation of number of events in a given interval.
    - Poisson distribution / probability _mass_ function ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$p_X(k) = \begin{cases} e^{-\lambda} \frac {\lambda^k} {k!} & \text{for }k \in \mathbb N_0 \\ 0 & \text{otherwise} \,. \end{cases}$$
    - Poisson distribution / proof of being probability distribution ::@:: It is also very easy to see its probability mass function is nonnegative (in fact, positive). To see it sums up to 1, realize that the sum actually contains a Maclaurin expansion of $e^\lambda$.
    - Poisson distribution / mean ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname E[X] = \lambda \,.$$ To prove this, one will need to cancel _k_ in the denominator with the numerator in the sum when finding its expectation value.
    - Poisson distribution / variance ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname{Var}(X) = \lambda \,.$$ To prove this, one will need to cancel $k (k - 1)$ in the denominator with the numerator in the sum when finding its expectation value.
  - [Poisson limit theorem](../../../../general/Poisson%20limit%20theorem.md) ::@:: The Poisson distribution may be used as an approximation to the binomial distribution, if $p_n$ is a sequence of real numbers in $[0, 1]$ such that the sequence $n p_n$ converges to a finite limit $\lambda$: $$\lim_{n \to \infty} \binom n k p_n^k (1 - p_n)^{n - k} = e^{-\lambda} \frac {\lambda^k} {k!} \,.$$. Informally, the Poisson distribution closely approximates the binomial distribution when _n_ is large.
  - [continuous uniform distribution](../../../../general/continuous%20uniform%20distribution.md) ::@:: The __continuous uniform distribution__ describes uniform relative likelihood in between the interval _a_ and _b_ (both inclusive). It is denoted $U(a, b)$, where $-\infty < a < b < +\infty$.
    - continuous uniform distribution / probability _density_ function ::@:: For $X \sim U(a, b) \,,$ $$f(x) = \begin{cases} \frac 1 {b - a} & \text{for }a \le x \le b \\ 0 & \text{otherwise} \,. \end{cases}$$
    - continuous uniform distribution / proof of being probability distribution ::@:: It is extremely easy to see its probability density function is nonnegative and integrates up to 1 over the real numbers.
    - continuous uniform distribution / mean ::@:: For $X \sim U(a, b) \,,$ $$\operatorname E[X] = \frac {a + b} 2 \,.$$
    - continuous uniform distribution / variance ::@:: For $X \sim U(a, b) \,,$ $$\operatorname{Var}(X) = \frac {(b - a)^2} {12} \,.$$
  - [normal distribution](../../../../general/normal%20distribution.md) ::@:: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> Note: When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance. Almost screwed this up in the midterm examination...
    - normal distribution / probability _density_ function ::@:: For $X \sim \mathcal N(\mu, \sigma^2) \,,$ $$f(x) = \frac 1 {\sqrt{2\pi \sigma^2} } \exp\left(-\frac {(x - \mu)^2} {2 \sigma^2} \right) \,.$$
    - normal distribution / proof of being probability distribution ::@:: It is also very easy to see its probability density function is nonnegative (in fact, positive). To see it integrates up to 1 over the real numbers, integrate with respect to $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$ first (substitution), then the resulting integral contains a Gaussian integral $\int_{-\infty}^\infty \! e^{-t^2} \,\mathrm{d}x$, which has no elementary antiderivative, but when evaluated over the real numbers, yields $\sqrt \pi$.
    - normal distribution / mean ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$\operatorname E[X] = \mu \,.$$ To prove this, turn the additional $x$ in the integrand into $(x - \mu + \mu)$, apply linearity of integration (split into $(x - \mu)$ and $\mu$), and then substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$. Then the expression should contain a Gaussian integral and an integral that has an odd function as the integrand. The former integral is $\sqrt \pi$ and the latter integral is 0 by symmetry.
    - normal distribution / variance ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2\right) \,,$ $$\operatorname{Var}(X) = \sigma^2 \,.$$ To prove this, substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$, then substitute $e^{-t^2}$, and finally apply integration by part. The resulting expression should contain an expression that is 0 and a Gaussian integral, which evaluates to $\sqrt \pi$.
    - normal distribution / shape ::@:: All normal distribution have the bell-shaped regardless of its parameters. Changing the mean simply translates the shape, while increasing the variance fattens (becomes wider) and flattens (the maximum value becomes lower) the shape.
    - normal distribution / examples ::@:: human height, one component of the velocity of a turbulent wind flow, Galton board
    - normal distribution / standard normal distribution ::@:: The __standard normal distribution__ has the mean, $\mu$, 0, and the variance, $\sigma^2$, 1. Its CDF is commonly denoted by $\Phi(z)$ while its PDF is commonly denoted by $\varphi(z)$. <p> A property of its CDF due to the even symmetry of its PDF: $$\Phi(-z) = 1 - \Phi(z) \,.$$
    - normal distribution / standardization ::@:: Any normal distribution can be __standardized__ by defining the random variable $$Z = \frac {X - \mu} {\sigma} \qquad X = \sigma Z + \mu \,.$$ Further, $$z = \frac {x - \mu} \sigma$$ is also known as the __standard score__ of the data _x_. <p> After standardization, a standard normal table that provides $\Phi(z)$ for different values of _z_ may be used to evaluate the CDF of any normal distribution. (The table may not show negative values of _z_. In that case, you need to use the property of its CDF above.)
  - [Bayes' theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20the%20theorem) ::@:: __Bayes' theorem__ relates _P_(_A_|_B_) to _P_(_B_|_A_). It states $$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) \ne 0 \,.$$ Sometimes the theorem is stated in the form where the denominator is replaced using the _law of total probability_.
- [questions/2024-11-18/lecture](questions/2024-11-18%20lecture.md)
- materials
  - [lecture video](https://youtu.be/7Kka7h-YMXk)
  - [read: the Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
    - [Monty Hall problem](../../../../general/Monty%20Hall%20problem.md)
  - [read: the Sleeping Beauty problem](https://en.wikipedia.org/wiki/Sleeping_Beauty_problem)
    - [Sleeping Beauty problem](../../../../general/Sleeping%20Beauty%20problem.md)
  - [watch: Philosophers are not smart enough for probability theory!](https://youtu.be/XeSu9fBJ2sI)
  - Ross/Chapter 3: Conditional Probability, Independence
  - Ross/Chapter 4: Random Variables
    - Note: We did not cover variance and common probability distributions in the lectures (due to being too easy), but they are part of the syllabus. So, make sure you read everything in these chapters.
  - [video: Bayes theorem](https://youtu.be/HZGCoVF3YvM)
  - [video: the Bayesian trap](https://youtu.be/R13BD8qKeTg)

## week 12 tutorial

- datetime: 2024-11-18T18:00:00+08:00/2024-11-18T18:50:00+08:00
- topic: solving problems using linearity of expectation
- [indicator function](../../../../general/indicator%20function.md) ::@:: An __indicator function__ or a __characteristic function__ of a [subset](../../../../general/subset.md) of a [set](../../../../general/set%20(mathematics).md) is a [function](../../../../general/function%20(mathematics).md) that maps elements of the subset to one, and all other elements to zero. That is, if _A_ is a subset of some set _X_, then $\mathbf {1} _{A}(x)=1$ if $x\in A,$ and $\mathbf {1} _{A}(x)=0$ otherwise, where $\mathbf {1} _{A}$ is a common notation for the indicator function. Other common notations are $I_{A},$ and $\chi _{A}.$ <p> The indicator function of _A_ is the [Iverson bracket](../../../../general/Iverson%20bracket.md) of the property of belonging to _A_; that is, $$\mathbf {1} _{A}(x)=[x\in A].$$ <p> For example, the [Dirichlet function](../../../../general/Dirichlet%20function.md) is the indicator function of the [rational numbers](../../../../general/rational%20number.md) as a subset of the [real numbers](../../../../general/real%20number.md).
- solving problems using linearity of expectation ::@:: Make use of indicator random variables, induction (e.g. express the expectation of a random variable parameterized by _n_ in terms of the expectation of a random variable parameterized by _n_ − 1), and splitting problems into sub-problems.
- [questions/2024-11-18/tutorial](questions/2024-11-18%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/CNhxNUIpAoI)
  - [video: linearity of expectation](https://youtu.be/0IJFBMIU6x4)
  - [video: expectation, indicator random variables, linearity](https://youtu.be/LX2q356N2rU)
  - [video: expectation](https://youtu.be/P1fSFvhPf7Q)

## week 12 lecture 2

- datetime: 2024-11-20T09:00:00+08:00/2024-11-20T10:20:00+08:00
- topic: Markov chains
- assignments: [homework 4](assignments/homework%204/submission.md)
- [stochastic process](../../../../general/stochastic%20process.md) ::@:: A __stochastic process__ is defined as a sequence of random variables.
- [Markov chain](../../../../general/Markov%20chain.md) ::@:: In probability theory and statistics, a __Markov chain__ or __Markov process__ is a [stochastic process](../../../../general/stochastic%20process.md) describing a [sequence](../../../../general/sequence.md) of possible events in which the [probability](../../../../general/probability.md) of each event depends only on the state attained in the previous event. Informally, this may be thought of as, "What happens next depends only on the state of affairs _now_."
  - Markov chain / graph ::@:: A Markov chain can be represented by a weighted directed graph. The weights are such that that are within $(0, 1]$, and the total weight of outgoing edges from any vertex is 1.
  - Markov chain / extending a finite walk ::@:: Consider a finite walk on a Markov chain. The probability of extending such a finite walk to an infinite walk (i.e. an infinite walk having the finite walk as a prefix), is the products of the weights of the edges in the finite walk. <p> Extending such a finite walk is an event, and denoted $\operatorname{Ext}(w)$, where $w$ is a finite walk. The set of infinite walks with $w$ as prefix is denoted $\overline w$.
  - Markov chain / reachability event ::@:: The event that a particular set of vertices in the Markov chain is defined as the set of infinite walks that has at least one of its vertex in the particular set. It is denoted $\Diamond T$, where $T$ is the particular set of vertices. <p> Consider the set of all finite walks that has its last vertex in the particular set. Then the union of extending all of said finite walks is an event and is equivalent to the reachability event described above. (Note that in the union, the events of extending finite walks are not pairwise disjoint and may overlap.)
- Büchi set ::@:: A Büchi set of a subset of a Markov chain is the set of infinite walks that visits the subset infinitely many times. It is an event, and is denoted $\operatorname{Büchi}(T)$, where $T$ is a subset of a Markov chain. <p> It can also be defined as the intersection of infinite walks that visits the subset _k_ times for _k_ = 1 to +∞.
  - Büchi set / strongly connected component ::@:: The __condensation__ of the a directed graph (e.g. Markov chain) is formed by contracting each _strongly connected component_ of the graph into a single vertex. The condensation is a directed acyclic graph. As a special case, if the original graph is strongly connected, the entire graph condenses to a single vertex. <p> Then the probability of a Büchi set of a single vertex in a Markov chain equals 0 if the corresponding vertex in the condensation of the Markov chain has an outgoing edge (non-sinks). <p> In an infinite walk, almost all infinite walks goes to the sinks in the condensation, i.e. strongly connected components without outgoing edges in the Markov chain. This is somewhat intuitive.
    - [strongly connected component](../../../../general/strongly%20connected%20component.md)
- not taught in class
  - [Markov decision process](../../../../general/Markov%20decision%20process.md) ::@:: __Markov decision process__ \(__MDP__\), also called a [stochastic dynamic program](../../../../general/stochastic%20dynamic%20programming.md) or stochastic control problem, is a model for [sequential decision making](../../../../general/sequential%20decision%20making.md) when [outcomes](../../../../general/outcome%20(probability).md) are uncertain.
- [questions/2024-11-20](questions/2024-11-20.md)
- [week 12 problem set](questions/week%2012%20problem%20set.md)
- materials
  - [video: Markov chains](https://youtu.be/i3AkTO9HLXo)
  - [video: recurrence and irreducibility](https://youtu.be/VNHeFp6zXKU)
  - [video: n-step transition matrix](https://youtu.be/Zo3ieESzr4E)
  - [video: Markov decision processes](https://youtu.be/2iF9PRriA7w)
  - [recommended to read: what Amir does when he is not teaching](https://canvas.ust.hk/courses/58174/modules/items/1458606)

<!-- ## week 12 TA session -->
<!-- -->
<!-- - datetime: 2024-11-22T19:00:00+08:00/2024-11-22T19:50:00+08:00 -->
<!-- - topic: solving weekly problem set 9 -->
<!-- - [questions/2024-11-22](questions/2024-11-22.md) -->
<!-- - [week 10 problem set](questions/week%2010%20problem%20set.md) -->
<!-- - materials -->

## week 13 lecture

- datetime: 2024-11-25T09:00:00+08:00/2024-11-25T10:20:00+08:00
- topic: Nim, Sprague–Grundy theorem
- [Nim](../../../../general/Nim.md) ::@:: __Nim__ is a [mathematical](../../../../general/mathematical%20game.md) [game of strategy](../../../../general/strategy%20game.md) in which two players take turns removing \(or "nimming"\) objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object. <p> Nim is fundamental to the [Sprague–Grundy theorem](../../../../general/Sprague–Grundy%20theorem.md), which essentially says that every [impartial game](../../../../general/impartial%20game.md) is equivalent to a nim game with a single pile.
  - Nim / graph ::@:: Use a tuple of natural numbers to represent the current state of Nim. Then Nim can be represented by an directed acyclic graph (DAG). <p> We can analyze this by labelling all vertices without outgoing edges as a losing position (for the current player). Then label all vertices with at least one outgoing edge to a losing position winning positions. Label all vertices with all outgoing edges to winning positions losing positions. Repeat this until the entire graph is labeled. We can label the vertices in reverse topological order, since any DAG has a topological order (and vice versa).
  - Nim / XOR-sum ::@:: The XOR-sum may be used to calculate a winning strategy for Nim.
- [impartial game](../../../../general/impartial%20game.md) ::@:: In [combinatorial game theory](../../../../general/combinatorial%20game%20theory.md), an __impartial game__ is a [game](../../../../general/mathematical%20game.md) in which the allowable moves depend only on the position and not on which of the two players is currently moving, and where the payoffs are symmetric.
- [nimber](../../../../general/nimber.md) ::@:: In [mathematics](../../../../general/mathematics.md), the __nimbers__, also called __Grundy numbers__, are introduced in [combinatorial game theory](../../../../general/combinatorial%20game%20theory.md), where they are defined as the values of heaps in the game [Nim](../../../../general/Nim.md). The nimbers are the [ordinal numbers](../../../../general/ordinal%20number.md) endowed with _nimber addition_ and _nimber multiplication_, which are distinct from [ordinal addition](../../../../general/ordinal%20arithmetic.md#addition) and [ordinal multiplication](../../../../general/ordinal%20arithmetic.md#multiplication). <p> Because of the [Sprague–Grundy theorem](../../../../general/Sprague–Grundy%20theorem.md) which states that every [impartial game](../../../../general/impartial%20game.md) is equivalent to a Nim heap of a certain size, nimbers arise in a much larger class of impartial games.
  - [mex](../../../../general/mex%20(mathematics).md) ::@:: The __mex__ \("__m__inimum __ex__cluded value"\) of a [subset](../../../../general/subset.md) of a [well-ordered](../../../../general/well-order.md) set is the smallest value from the whole set that does not belong to the subset. That is, it is the [minimum](../../../../general/maximum%20and%20minimum.md) value of the [complement set](../../../../general/complement%20(set%20theory).md).
  - Nimber / graph ::@:: Use a natural number to represent the current state of Nim with 1 lump. The natural number used this way is known as a __Nimber__. Then Nim can be represented by an directed acyclic graph (DAG). <p> We can analyze this by labelling all vertices without outgoing edges as 0. Then label vertices with outgoing edges by the [mex](../../../../general/mex%20(mathematics).md) (not _max_) of the labels of the vertices the outgoing edges reach. Repeat this until the entire graph is labeled. We can label the vertices in reverse topological order, since any DAG has a topological order (and vice versa). If the label is 0, it is a losing position, and otherwise it is a winning position. <p> By the Sprague–Grundy theorem, a Nim with several lumps is equivalent to a single Nimber (and thus is equivalent to a Nim with 1 lump), which is given by the mex of the several Nimbers representing the several lumps. Indeed, if the mex gives 0, the current state of Nim with several lumps is a losing position, and otherwise it is a winning position.
- [Sprague–Grundy theorem](../../../../general/Sprague–Grundy%20theorem.md) ::@:: In [combinatorial game theory](../../../../general/combinatorial%20game%20theory.md), the __Sprague–Grundy theorem__ states that every [impartial game](../../../../general/impartial%20game.md) under the [normal play convention](../../../../general/normal%20play%20convention.md) is equivalent to a one-heap game of [nim](../../../../general/Nim.md), or to an infinite generalization of nim. It can therefore be represented as a [natural number](../../../../general/natural%20number.md), the size of the heap in its equivalent game of nim, as an [ordinal number](../../../../general/ordinal%20number.md) in the infinite generalization, or alternatively as a [nimber](../../../../general/nimber.md), the value of that one-heap game in an algebraic system whose addition operation combines multiple heaps to form a single equivalent heap in nim.
  - [Sprague–Grundy theorem](../../../../general/Sprague–Grundy%20theorem.md) / nim-value ::@:: The __Grundy value__ or __nim-value__ of any impartial game is the unique nimber that the game is equivalent to. In the case of a game whose positions are indexed by the natural numbers \(like nim itself, which is indexed by its heap sizes\), the sequence of nimbers for successive positions of the game is called the __nim-sequence__ of the game.
- [questions/2024-11-25/lecture](questions/2024-11-25%20lecture.md)
- materials
  - [lecture video](https://youtu.be/xo_c4mpYC2A)
  - [reading: Ferguson's lecture notes \(chapters 1-4\)](https://www.cs.cmu.edu/afs/cs/academic/class/15859-s05/www/ferguson/comb.pdf)

## week 13 tutorial

- datetime: 2024-11-25T18:00:00+08:00/2024-11-25T18:50:00+08:00
- topic: one-shot games, Nash equilibria
- [prisoners' dilemma](../../../../general/prisoners'%20dilemma.md) ::@:: The __prisoner's dilemma__ is a [game theory](../../../../general/game%20theory.md) thought experiment involving two [rational agents](../../../../general/rational%20agent.md), each of whom can either cooperate for mutual benefit or betray their partner \("defect"\) for individual gain. The dilemma arises from the fact that while defecting is rational for each agent, cooperation yields a higher payoff for each.
  - [prisoners' dilemma](../../../../general/prisoners'%20dilemma.md) / variants: pollution game ::@:: If a country does not pollute, it costs the country 5 (payoff is -5). If a country pollutes, it costs everyone 1 (payoff is -1 for everyone). <p> This is similar to prisoners' dilemma, but with negative payoffs.
  - [prisoners' dilemma](../../../../general/prisoners'%20dilemma.md) / variants: battle of the sexes
- one-shot game ::@:: A __one-shot game__ is a game that is played once only. Assume there are $n$ players. We can describe it with a set of strategies $S_i$ for player $i$, and a payoff function $u_i : S_1 \times \cdot \times S_n \to \mathbb R$ for player $i$. <p> A player is __rational__ if they are interested in maximizing their payoff function, given they can only choose their own strategy.
- [strategy](../../../../general/strategy%20(game%20theory).md)
  - [strategic dominance](../../../../general/strategic%20dominance.md) ::@:: In [game theory](../../../../general/game%20theory.md), a __dominant strategy__ is a [strategy](../../../../general/strategy%20(game%20theory).md) that is better than any other strategy for a player, no matter how that player's opponent or opponents play. Strategies that are dominated by another strategy can be eliminated from consideration, as they can be strictly improved upon. Some very simple games can be solved using dominance. <p> For example, in prisoners' dilemma, defecting is the dominant strategy. So rational players would both defect.
- [Nash equilibrium](../../../../general/Nash%20equilibrium.md) ::@:: In [game theory](../../../../general/game%20theory.md), the __Nash equilibrium__ is the most commonly-used [solution concept](../../../../general/solution%20concept.md) for [non-cooperative games](../../../../general/non-cooperative%20game%20theory.md). A Nash equilibrium is a situation where no player could gain by changing their own strategy \(holding all other players' strategies fixed\). <p> If each player has chosen a [strategy](../../../../general/strategy%20(game%20theory).md) – an action plan based on what has happened so far in the game – and no one can increase one's own expected payoff by changing one's strategy while the other players keep theirs unchanged, then the current set of strategy choices constitutes a Nash equilibrium. <p> Note that the strategy may be pure (one could also considered pure as a degenerate form of mixed) or mixed.
- [rock paper scissors](../../../../general/rock%20paper%20scissors.md) ::@:: I think you should know what this is, right...?
- [battle of the sexes](../../../../general/battle%20of%20the%20sexes%20(game%20theory).md) ::@:: Imagine that a man and a woman hope to meet this evening, but have a choice between two events to attend: a prize fight and a ballet. The man would prefer to go to prize fight. The woman would prefer the ballet. Both would prefer to go to the same event rather than different ones. If they cannot communicate, where should they go?
- [matching pennies](../../../../general/matching%20pennies.md) ::@:: __Matching pennies__ is a [non-cooperative game](../../../../general/non-cooperative%20game%20theory.md) studied in [game theory](../../../../general/game%20theory.md). It is played between two players, Even and Odd. Each player has a [penny](../../../../general/penny.md) and must secretly turn the penny to heads or tails. The players then reveal their choices simultaneously. If the pennies match \(both heads or both tails\), then Even wins and keeps both pennies. If the pennies do not match \(one heads and one tails\), then Odd wins and keeps both pennies.
- [strategy](../../../../general/strategy%20(game%20theory).md)
  - [strategy](../../../../general/strategy%20(game%20theory).md) / pure strategy ::@:: A __pure strategy__ means a strategy where the player must play a particular strategy from their strategy set.
  - [strategy](../../../../general/strategy%20(game%20theory).md) / mixed strategy ::@:: A __mixed strategy__ means a strategy where the player plays a strategy in their strategy set with a probability. Pure strategy can be treated as a degenerate form of mixed strategy, where one strategy is assigned the probability of 1 and the rest assigned 0. <p> In this context, the payoff may be called _expected payoff_ instead.
- [Nash equilibrium](../../../../general/Nash%20equilibrium.md)
  - [Nash equilibrium](../../../../general/Nash%20equilibrium.md) / Nash's existence theorem ::@:: Nash proved that if [mixed strategies](../../../../general/strategy%20(game%20theory).md#pure%20and%20mixed%20strategies) \(where a player chooses probabilities of using various pure strategies\) are allowed, then every game with a finite number of players in which each player can choose from finitely many pure strategies has at least one Nash equilibrium, which might be a pure strategy for each player or might be a probability distribution over strategies for each player. <p> Nash equilibria need not exist if the set of choices is infinite and non-compact. However, a Nash equilibrium exists if the set of choices is [compact](../../../../general/compact%20space.md) with each player's payoff continuous in the strategies of all the players.
- not taught in class
  - [solution concept](../../../../general/solution%20concept.md) ::@:: In [game theory](../../../../general/game%20theory.md), a __solution concept__ is a formal rule for predicting how a game will be played. These predictions are called "solutions", and describe which strategies will be adopted by players and, therefore, the result of the game. The most commonly used solution concepts are [equilibrium concepts](../../../../general/economic%20equilibrium.md), most famously [Nash equilibrium](../../../../general/Nash%20equilibrium.md).
  - [game theory](../../../../general/game%20theory.md) ::@:: __Game theory__ is the study of [mathematical models](../../../../general/mathematical%20model.md) of strategic interactions.
- [questions/2024-11-25/tutorial](questions/2024-11-25%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/rDOGtmT8FdM)
  - [video: Nash equilibrium in 5 minutes](https://youtu.be/tDQ4_W3eUiw)
  - [video: prisoners' dilemma](https://youtu.be/7Cqv_gdTkg4)
  - [video: repeated prisoners' dilemma](https://youtu.be/mScpHTIi-kM)
  - Algorithmic Game Theory Book/Chapter 1: Basic Solution Concepts

## week 13 lecture 2

- datetime: 2024-11-27T09:00:00+08:00/2024-11-27T10:20:00+08:00
- topic: two-player infinite-duration games on graphs
- two-player infinite-duration games on graphs
  - two-player infinite-duration games on graphs / arena ::@:: An __arena__ is a directed finite graph (possibly with self-loops) $G = (V, E, V_1, V_2)$. Each vertex has an outdegree of at least 1. The vertices of the graph are partitioned into two $V_1, V_2$, respectively corresponding to player 1 and 2. Player 1 is in control if the current vertex is in $V_1$, and similarly for player 2 and $V_2$.
  - two-player infinite-duration games on graphs / game ::@:: A __game__ on an arena starts at an arbitrary vertex $v_0$.
  - two-player infinite-duration games on graphs / strategy ::@:: A __strategy__ for player $i$ is a function that takes the current history and the current vertex as inputs and outputs the next vertex: $\sigma_i: V^* \times V_i \to V$. The current vertex must have an outgoing edge to the next vertex. $V^*$ is the domain of the current history (a tuple of previously visited vertices). $V_i$ is the current vertex, which must be in $V_i$ since player $i$ is in control.
  - two-player infinite-duration games on graphs / outcome ::@:: An __outcome__ $o$ is an infinite walk on an arena $G$ starting at vertex $v_0$. The set of all outcomes is denoted $O$.
  - two-player infinite-duration games on graphs / objective ::@:: An __objective__ $\mathrm{obj}_i$ for player $i$ is a subset of all outcomes. <p> In a _zero-sum game_ for two players, $\mathrm{obj}_2 = O \setminus \mathrm{obj}_1$.
  - two-player infinite-duration games on graphs / winning strategy ::@:: A player $i$ has a __winning strategy__ if for every strategy other players can have, the outcome is in player $i$<!-- LaTeX separator -->'s objective, i.e. $o \in \mathrm{obj}_i$.
  - two-player infinite-duration games on graphs / determined ::@:: A game is __determined__ if for every starting vertex, either player 1 or player 2 has a winning strategy.
- reachability game/safety game ::@:: A game where player 1's objective is to reach a particular subset of the graph. This is the __reachability game__ for player 1. For player 2, player 2's objective is to prevent the above particular subset of the graph from being ever reached. his is the __safety game__ for player 2. These two games are dual in the aforementioned sense. <p> This game is a determined game, and the solution is given below.
  - reachability game/safety game / solution ::@:: Let $T$ be the subset of the graph to be reached by player 1. Consider the "winning" vertices in at most $i$ steps as $T_i$. Clearly, $$T_0 = T \,.$$ We can derive a recurrence relation: $$\begin{aligned} T_{i + 1} & = T_i \\ & \cup \set{v \in V_1 \mid \exists (v, u) \in E \text{ s.t. } u \in T_i} \\ & \cup \set{v \in V_2 \mid \forall (v, u) \in E \text{ s.t. } u \in T_i} \,. \end{aligned}$$ $T_i$ is included because player 1 has already won. The second set considers vertices that player 1 controls: if there is an edge that goes to $T_i$, then player 1 has a winning strategy by choosing said edge. The third set considers vertices that player 2 controls: if all edges goes to $T_i$, then player 2 is forced to make a move that makes player 1 has a winning strategy. <p> The union of $T_i$ for all natural numbers $i$ are the vertices for which player 1 has a winning strategy. The remaining vertices are the vertices for which player 2 has a winning strategy.
  - reachability game/safety game / attractor, trap ::@:: Let $T$ be the subset of the graph to be reached by player $i$. The vertices for which player $i$ has a winning strategy for doing so is also known as the __attractor__ of $T$ in $G$ for player $i$, denoted by $\operatorname{Attr}_i(T, G)$. If $G$ is clear, it may be omitted. <p> The complement of an attractor is a __trap__.
- Büchi game ::@:: A game where player 1's objective is to visit a particular subset of the graph infinitely many times. For player 2, player 2's objective is to prevent the above particular subset of the graph from being reached for infinitely many times. This is the __Büchi game__. <p> This game is a determined game, and the solution is given below. <p> Hint: Make use of the __attractor__ and __trap__ of $T$, and try to reduce the graph into smaller graphs.
  - Büchi game / solution ::@:: Consider the winning vertices for player 2. If the starting vertex is in the _trap_ of $T$ for player 1, player 2 has a winning strategy. If the starting vertex is in the _attractor_ of the above trap for player 2, then player 2 still has a winning strategy. So now the vertices in the walk are restricted to the graph not in the above _attractor_ for player 1 to possibly win, because if at any point, the walk walks into the above _attractor_, then player 2 has a winning strategy. Make a new graph without the above attractor, and repeat the above arguments again. <p> From above, we can derive $C_i$ representing a subset of the starting vertices where player 2 wins. The base cases are: $$G_1 = G \qquad C_1 = \operatorname{Attr}_2(\operatorname{Trap}_1(T, G_1), G_1) \,$$ and the induction steps are: $$G_i = G_{i - 1} \setminus C_{i - 1} \qquad C_i = \operatorname{Attr}_2(\operatorname{Trap}_1(T, G_i), G_i) \,.$$ <p> The union of $C_i$ for all natural numbers $i$ are the vertices for which player 2 has a winning strategy. The remaining vertices are the vertices for which player 1 has a winning strategy.
- [questions/2024-11-27](questions/2024-11-27.md)
- [week 13 problem set](questions/week%2013%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/U8NNtDIlO4U)
  - [playlist: COMP 6613B's lectures on graph games (watch lectures 6 and 7, lecture 8 is optional)](https://youtu.be/zu20Q5EJu7I?list=PLzZlJT-UOiwDluuV0Ypq17M-X-Ujdj_0B&index=5)
  - [recommended playlist: linear-time temporal logic](https://youtu.be/a9fo3dUly8A?list=PLMBx8HjvK7672qEl6bdnXdzYEbLP_lWPw)
    - LTL is not part of the syllabus. It's just a recommendation for you to see what the deal with ♢s and □s was.
    - [linear temporal logic](../../../../general/linear%20temporal%20logic.md)

## week 13 TA session

- datetime: 2024-11-27T18:00:00+08:00/2024-11-27T18:50:00+08:00
- topic: solving weekly problem set 9
- [questions/2024-11-27 TA session](questions/2024-11-27%20TA%20session.md)
- [week 10 problem set](questions/week%2010%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/ib3lByadEvI)

## week 14 TA session

- datetime: 2024-12-06T16:00:00+08:00/2024-12-16:50:00+08:00
- topic: solving weekly problem set 11
- [questions/2024-12-06 TA session](questions/2024-12-06%20TA%20session.md)
- [week 11 problem set](questions/week%2011%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/S7l6OKfqFb4)

## week 15 TA session

- datetime: 2024-12-14T16:00:00+08:00/2024-12-14T16:50:00+08:00
- topic: solving weekly problem set 10, 12
- [questions/2024-12-14 TA session](questions/2024-12-14%20TA%20session.md)
- [week 10 problem set](questions/week%2010%20problem%20set.md)
- [week 12 problem set](questions/week%2012%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/CnG19S0ifu8)

## final examination

- datetime: 2024-12-20T16:30:00+08:00/2024-12-20T19:00:00+08:00, PT2H30M
- venue: \[SEAFRONT\]TST Sports Ctr ARENA
- format: closed book
- grades: 18.5/30
  - statistics
    - note: The department told instructors to not release statistics.
    - mean: ?
    - standard deviation: ?
    - low: ?
    - lower quartile: ?
    - median: ?
    - upper quartile: ?
    - high: ?
    - distribution: ?
- report
  - overall ::@:: It's acceptable, given the time constraints... It is not an ideal environment for solving complex problems.
- check
  - note: You will receive a scanned copy of your examination. Send email to Amir to appeal.
- materials
  - lecture video: (none)
  - [final examination](attachments/final.pdf) (source: <https://canvas.ust.hk/courses/58174/modules/items/1462902>)

> Total Score: 18.5/30
>
> Grader: Amir
>
> Problem 1: 4.5/10
>
> i) 2 pts - correct <br/>
> ii) 0.5 pts - This doesn't count all cases, e.g. this one is missed: <br/>
> 1AA <br/>
> BB1 <br/>
> iii) Wrong answer with messy explanations. I could not understand what you were doing here. <br/>
> iv) Correct - 2 pts <br/>
> v) Incorrect, |B|=|A|
>
> Problem 2: 6/10
>
> i and ii are OK - 5 pts. <br/>
> iii) 1 pt - How about double-jump from b to d and then a reverse jump to b?
>
> Problem 3: 8/10
>
> i and ii) Excellent method - 4 pts <br/>
> iii) wrong answer <br/>
> iv) 2 pts - Correct method <br/>
> v) 2 pts
>
> We hope you enjoyed this semester and wish you a happy new year!

## aftermath
