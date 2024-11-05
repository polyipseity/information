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

- datetime: 2024-09-02T10:30:00+08:00/2024-09-02T11:20:00+08:00
- topic: propositional logic
- course logistics
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ propositional calculus](../../../../general/propositional%20calculus.md#propositional%20calculus)
    - proposition ::: A declarative statement that is either true (1) or false (0). No third value is possible. Typically it is represented by _p_, _q_, _r_, and so forth. <!--SR:!2024-11-07,42,303!2024-12-08,67,323-->
  - [truth table](../../../../general/truth%20table.md) ::: A table representing a boolean function. There are $n + 1$ columns, where the first $n$ columns are the inputs of the boolean function, while the last column is the output of the boolean function. There are $2^n$ rows, representing all possible combinations of the $n$ inputs mapping to the corresponding $2^n$ outputs. <!--SR:!2024-12-11,70,323!2025-03-30,150,323-->
    - [§ truth table](../../../../general/truth%20table.md#truth%20table)
  - boolean algebra operations ::: An operation that takes connections one or more propositions. These operations can be chained. <!--SR:!2024-12-19,78,323!2024-12-18,77,323-->
    - negation (not) ::: $\lnot p$: $$\begin{aligned} (0) & \mapsto 1 \\ (1) & \mapsto 0 \end{aligned}$$ <!--SR:!2024-12-20,79,323!2024-12-21,80,323-->
    - disjunction (or) ::: $p \lor q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 1 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-12-03,64,310!2024-12-02,63,323-->
    - conjunction (and) ::: $p \land q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 0 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-11-20,51,310!2024-12-06,66,323-->
    - implication (if-then) ::: $p \rightarrow q$: $$\begin{aligned} (0, 0) & \mapsto 1 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-12-02,63,323!2024-12-10,71,323-->
    - boolean algebra operations / order of operations ::: $\lnot$ > $\lor, \land$ > $\rightarrow$ <!--SR:!2024-11-17,48,290!2024-12-04,64,323-->
  - [tautology](../../../../general/tautology%20(logic).md) (true) ::: A proposition that is always true, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2024-12-20,79,323!2024-12-17,75,323-->
    - [§ tautology](../../../../general/tautology%20(logic).md#tautology)
  - [contradiction](../../../../general/contradiction.md) (false) ::: A proposition that is always false, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2025-03-30,152,323!2024-12-05,66,323-->
    - [§ contradiction](../../../../general/contradiction.md#contradiction)
  - propositional calculus / real life application ::: Consider making a one bit half adder. You want: $$\begin{aligned} 0 + 0 & = 0 \\ 1 + 0 & = 1 \\ 0 + 1 & = 1 \\ 1 + 1 & = 0 \end{aligned}$$. This can be expressed as $$\begin{aligned} \text{sum of products: } & (a \land \lnot b) \lor (\lnot a \land b) \\ \text{product of sums: } & (\lnot a \lor \lnot b) \land (a \lor b) \end{aligned}$$. This is also known as the exclusive-or (xor) operation. <!--SR:!2025-03-28,148,323!2024-11-20,51,310-->
  - [logical equivalence](../../../../general/logical%20equivalence.md) ::: Two propositions have the same truth values, no matter how the atomic propositions (terms with no operations) are assigned. One simple way to prove it is via a truth table and compare whether the rows are equivalent. <!--SR:!2024-12-16,75,323!2024-11-16,45,290-->
    - [§ logical equivalence](../../../../general/logical%20equivalence.md#logical%20equivalence)
    - [§ relation to material equivalence](../../../../general/logical%20equivalence.md#relation%20to%20material%20equivalence) ::: Material equivalence is simply a proposition that says two propositions have the same truth values. It may be false or true. Two propositions are logically equivalent if the material equivalence between them is true, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2024-12-14,73,323!2024-11-28,59,323-->
    - [§ general logical equivalences](../../../../general/logical%20equivalence.md#general%20logical%20equivalences)
  - [conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md) ::: The dual (Amir calls it inverse proposition) of a proposition $p$ is denoted $p^d$, and is formed by replacing $\land$ by $\lor$, $\lor$ by $\land$, T by F, and F by T. The dual relates to the original proposition by $\lnot p \equiv \overline p^d$, where $\overline p$ is replacing all atomic propositions (propositions without $\land$, $\lor$, and $\lnot$) by their negations. This can be interpreted as negating the "output" of $p$, i.e. $\lnot p$ is the same as negating all "inputs" of its dual $p^d$, i.e. $\overline p^d$. <!--SR:!2025-01-26,101,303!2025-05-03,179,323-->
    - [§ conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md#conjunction%2Fdisjunction%20duality)
    - [§ negation is semantically equivalent to dual](../../../../general/conjunction_disjunction_duality.md#negation%20is%20semantically%20equivalent%20to%20dual)
    - [§ further duality theorems](../../../../general/conjunction_disjunction_duality.md#further%20duality%20theorems)
  - [rules of inference](../../../../general/rules%20of%20inference.md) ::: Rules that allows deducing a consequence to be true, given that zero or more premises are true. <!--SR:!2024-12-30,83,340!2024-11-13,48,320-->
    - [rules of inference](../../../../general/rules%20of%20inference.md) / motivation ::: To prove a proposition $X := h_1 \land \ldots \land h_n \rightarrow c$ is true, where $h_i$ are _atomic_ variables (terms with no operations), one could use a proof table, but this would require $2^n$ rows. We could instead use another proposition equivalent to $X$, denoted $Y := p_1 \land \ldots \land p_n \rightarrow c$ where $p_i$ are propositions (not necessarily atomic). Coupled with _rules of inference_, we can prove $X$ via proving $Y$. <!--SR:!2025-01-11,79,270!2024-12-03,63,323-->
    - rules of inference / _modus ponens_ ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{p \phantom{\rightarrow q} } \\ & q & \end{aligned}$$ <!--SR:!2024-12-03,64,323!2024-11-19,50,303-->
    - rules of inference / hypothetical syllogism ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{q \rightarrow r} \\ & p \rightarrow r & \end{aligned}$$ <!--SR:!2024-11-28,59,323!2024-12-03,64,323-->
    - rules of inference / _modus tollens_ (not to be confused with the related _contraposition_) ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{\lnot q \!\!\!\! \phantom{\rightarrow q} } \\ & \lnot p & \end{aligned}$$ <!--SR:!2024-11-23,54,303!2024-12-04,64,323-->
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
    - rules of inference / conjunction ::: $$\begin{aligned} & p \\ & \underline{q \phantom{\land q} } \\ & p \land q & \end{aligned}$$ <!--SR:!2024-12-10,69,323!2024-12-14,72,323-->
    - rules of inference / disjunctive syllogism ::: $$\begin{aligned} & p \lor q \\ & \underline{\lnot p \!\!\!\! \phantom{\lor q} } \\ & q \end{aligned}$$ <!--SR:!2024-11-11,47,303!2024-12-06,66,323-->
    - rules of inference / transposition (with $F$ as the consequent) ::: $$\begin{aligned} & \underline{\lnot p \rightarrow F} \\ & p \end{aligned}$$ <!--SR:!2024-11-30,61,310!2024-11-25,56,323-->
    - rules of inference / simplification ::: $$\begin{aligned} & \underline{p \land q} \\ & p \end{aligned}$$ <!--SR:!2024-12-16,75,323!2024-12-04,65,323-->
    - rules of inference / addition ::: $$\begin{aligned} & \underline{p \phantom{\lor q} } \\ & p \lor q \end{aligned}$$ <!--SR:!2024-12-01,62,323!2025-03-28,147,310-->
    - rules of inference / importation (applied form) ::: $$\begin{aligned} & p \land q \\ & \underline{p \rightarrow (q \rightarrow r)} \\ & r \end{aligned}$$ <!--SR:!2025-02-23,120,290!2024-12-09,69,323-->
    - rules of inference / constructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{p \lor r \phantom{s} } \\ & q \lor s \end{aligned}$$ <!--SR:!2025-02-21,112,303!2024-11-10,41,290-->
    - rules of inference / destructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{\lnot q \lor \lnot s} \\ & \lnot p \lor \lnot r \end{aligned}$$ <!--SR:!2024-11-18,48,303!2024-12-08,69,323-->
    - rules of inference / constructive dilemma (unapplied form, with the same consequent) ::: $$\begin{aligned} & p \rightarrow r \\ & \underline{q \rightarrow r \phantom{r \rightarrow r} } \\ & (p \lor q) \rightarrow r \end{aligned}$$ <!--SR:!2024-12-09,62,283!2024-11-19,49,303-->
    - rules of inference / material equivalence (_modus ponens_) ::: $$\begin{aligned} & p \equiv q \\ & \underline{p \phantom{\equiv q} } \\ & q \end{aligned}$$ <!--SR:!2024-12-09,68,323!2024-12-15,74,323-->
  - proof format ::: A proof consists of several lines. Each line, numbered, is a proof statement, which either states the premise or is a statement derived from previous statements (referenced using line numbers) by rules of inference. For example: $$\begin{aligned} 1. \quad & p \rightarrow r && (\text{premise}) \\ 2. \quad & p && (\text{premise}) \\ 3. \quad & r && (\text{from 1 and 2}) \end{aligned}$$. <!--SR:!2024-12-20,78,323!2024-11-11,46,303-->
- [first-order logic](../../../../general/first-order%20logic.md)
  - [§ first-order logic](../../../../general/first-order%20logic.md#first-logic%20logic)
  - [predicate](../../../../general/predicate%20(mathematical%20logic).md) ::: A statement that becomes a proposition when the one or more unknowns are replaced by specified values from the universe. The universe is the set of all possible values for the unknowns. <!--SR:!2024-11-24,55,310!2024-11-15,46,303-->
  - universal quantification ::: $\forall x \, p(x)$ means for all $x$ in the universe $p(x)$ is true. If the universe is empty, $\forall x \, p(x)$ is true for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to existential quantification by $$\lnot \forall x \, p(x) \equiv \exists x \, \lnot p(x)$$. <!--SR:!2024-12-05,66,323!2024-11-22,53,310-->
    - universal quantification / distributive law ::: It distributes over logical conjunctions: $$\forall x \, (p(x) \land q(x)) \equiv \forall x \, p(x) \land \forall x \, q(x)$$. But it does NOT distribute over logical disjunctions: $$\forall x \, (p(x) \lor q(x)) \leftarrow \forall x \, p(x) \lor \forall x \, q(x)$$ and only the converse (shown above) is true. <!--SR:!2024-11-21,52,303!2024-12-04,64,323-->
  - existential quantification ::: $\exists x \, p(x)$ means there is at least one $x$ in the universe that $p(x)$ is true. If the universe is empty, $\exists x \, p(x)$ is false for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to universal quantification by $$\lnot \exists x \, p(x) \equiv \forall x \, \lnot p(x)$$. <!--SR:!2024-11-13,44,290!2024-12-17,76,323-->
    - existential quantification / distributive law ::: It distributes over logical disjunctions: $$\exists x \, (p(x) \lor q(x)) \equiv \exists x \, p(x) \lor \exists x \, q(x)$$. But it does NOT distribute over logical conjunctions: $$\exists x \, (p(x) \land q(x)) \rightarrow \exists x \, p(x) \land \exists x \, q(x)$$ but the converse is not necessarily true. <!--SR:!2024-11-27,58,323!2024-12-07,66,310-->
- [Peano axioms](../../../../general/Peano%20axioms.md) ::: (The second-order formulation is used.) One, $0$ is a natural number. Two, if $n$ is a natural number, then $S(n)$ is a natural number. Third, if $S(n) = S(m)$, then $n = m$. Four, $S(n) \ne 0$ for all natural numbers $n \in \mathbb N$. Five, if $K$ is a set such that $0 \in K$, and for all natural numbers $n \in \mathbb N$, if $n \in K$ then $S(n) \in K$, then $K = \mathbb N$ (induction). <!--SR:!2024-12-19,77,323!2025-02-09,104,303-->
  - [§ Peano axioms](../../../../general/Peano%20axioms.md#Peano%20axioms)
  - [§ historical second-order formulation](../../../../general/Peano%20axioms.md#historical%20second-order%20formulation)
  - Peano axioms / 1st axiom motivation ::: This defines the starting $0$ as a natural number. <!--SR:!2025-04-17,166,323!2024-12-05,66,323-->
  - Peano axioms / 2nd axiom motivation ::: This defines a successor function $S$ that can generate more natural numbers. Equivalently, the natural numbers are closed under $S$. <!--SR:!2024-11-16,47,303!2024-12-08,67,323-->
  - Peano axioms / 3rd axiom motivation ::: This makes the successor function injective (but not surjective, as $0$ is not in the image of the function). <!--SR:!2024-12-03,63,323!2025-01-17,92,303-->
  - Peano axioms / 4th axiom motivation ::: Coupled with the injective property, this makes the successor function never go back to the starting number $0$. Otherwise, the successor function can, at one point, loop back to $0$, and there will only be finitely many natural numbers. <!--SR:!2024-12-04,64,323!2024-12-12,71,323-->
  - Peano axioms / 5th axiom motivation ::: The 4 axioms above are insufficient to ensure that repeatedly applying $S$ on $0$ can generate all natural numbers. Indeed, an infinite successor chain starting from $0$ that does not contain all the natural numbers, with a finite circular successor chain, is compatible with the 4 axioms above. The 5th axiom simply states that the infinite successor chain starting from $0$ is the set of all natural numbers, excluding the situation above. This is also what makes mathematical induction possible. <!--SR:!2024-11-26,57,323!2025-04-02,153,310-->
- materials
  - [lecture video](https://youtu.be/X_SF_o9ZwmA)
  - Grimaldi/Chapter 2: Fundamentals of Logic
  - [video: Peano axioms](https://youtu.be/5zl2zBqNAHM)

## week 1 lecture 2

- datetime: 2024-09-04T09:00:00+08:00/2024-09-04T11:20:00+08:00
- topic: induction, well-ordering, infinite descent
- [Peano axioms](../../../../general/Peano%20axioms.md)
  - [§ defining arithmetic operations and relations](../../../../general/Peano%20axioms.md#defining%20arithmetic%20operations%20and%20relations)
  - [§ addition](../../../../general/Peano%20axioms.md#addition) ::: 2 rules: $\forall n; n + 0 = n$, $\forall n, m; n + s(m) = s(n + m)$. All other rules that you know of everyday addition can be derived from these rules. From this we can prove that addition is commutative ($\forall n, m; n + m = m + n$) and associative ($\forall n, m, o; (n + m) + o = n + (m + o)$). <!--SR:!2024-12-10,69,323!2024-12-04,65,323-->
  - [§ multiplication](../../../../general/Peano%20axioms.md#multiplication) ::: Assuming addition is defined, 2 rules: $\forall n, n \cdot 0 = 0$, $\forall n, m; n \cdot s(m) = n + n \cdot m$. All other rules that you know of everyday multiplication can be derived from these rules. From this we can prove that multiplication is commutative ($\forall n, m; n \cdot m = m \cdot n$) and associative ($\forall n, m, o; (n \cdot m) \cdot o = n \cdot (m \cdot o)$). <!--SR:!2024-12-17,75,323!2024-11-22,51,303-->
  - [§ inequalities](../../../../general/Peano%20axioms.md#inequalities) ::: Assuming addition is defined, the inequality $\le$ is defined as $$n \le m \equiv \exists x; n + x = m$$. <!--SR:!2024-12-16,74,323!2024-11-27,58,323-->
- [mathematical induction](../../../../general/mathematical%20induction.md)
  - [§ mathematical induction](../../../../general/mathematical%20induction.md#mathematical%20induction)
  - [§ description](../../../../general/mathematical%20induction.md#description)
  - [§ examples](../../../../general/mathematical%20induction.md#examples)
  - [§ example of error in the induction step](../../../../general/mathematical%20induction.md#example%20of%20error%20in%20the%20induction%20step)
  - [§ relationship to the well-ordering principle](../../../../general/mathematical%20induction.md#relationship%20to%20the%20well-ordering%20principle)
- [well-ordering principle](../../../../general/well-ordering%20principle.md) ::: Every _non-empty_ subset of the natural numbers (not integers) has a least element. Proofs using this are generally by contradiction. This is implied from induction (from Peano axioms) or infinite descent. However, the well-ordering principle does not imply induction (under the other Peano axioms), and so is not equivalent to induction. <!--SR:!2024-11-19,50,290!2025-04-20,169,323-->
  - [§ well-ordering principle](../../../../general/well-ordering%20principle.md#well-ordering%20principle)
- [proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md) ::: There are no infinite strictly decreasing sequences of natural numbers. Proofs using this are generally by contradiction, and involve constructing an infinite descent of natural numbers, which contradicts this. Another way is assuming a minimal solution to a problem exists, but then prove that it would lead to a smaller solution. This is equivalent to induction (from Peano axioms), and implies the well-ordering principle . <!--SR:!2024-12-18,76,323!2024-12-08,67,323-->
  - [§ proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md#proof%20by%20infinite%20descent)
- [questions/2024-09-04](questions/2024-09-04.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/xR3jmz5WdQ4)
  - [video: induction](https://youtu.be/z8HKWUWS-lA)
  - [video: 2+2=4](https://youtu.be/TQpHVtlXuyc)
  - [Mathematical Induction](https://www.sydney.edu.au/content/dam/students/documents/mathematics-learning-centre/mathematical-induction.pdf)

## week 2 lecture

- datetime: 2024-09-09T10:30:00+08:00/2024-09-09T11:20:00+08:00
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

- datetime: 2024-09-11T09:00:00+08:00/2024-09-11T11:20:00+08:00
- topic: counting, permutations, combinations, balls and walls
- [combinatorial principles](../../../../general/combinatorial%20principles.md) ::: principles commonly used to solve combinatorial problems: rule of sum, rule of product, permutation, combination, ... <!--SR:!2024-11-06,20,353!2024-11-06,20,353-->
  - [§ combinatorial principles](../../../../general/combinatorial%20principles.md#combinatorial%20principles)
  - [§ rule of sum](../../../../general/combinatorial%20principles.md#rule%20of%20sum) ::: Also known as the principle of addition or case work principle. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ + _B_ ways to do either one thing. <!--SR:!2024-11-06,20,353!2024-11-06,20,353-->
  - [§ rule of product](../../../../general/combinatorial%20principles.md#rule%20of%20product) ::: Also known as the principle of multiplication. If there are _A_ ways to do a thing and _B_ ways to do another thing, then there are _A_ \* _B_ ways to do both things. <!--SR:!2024-11-06,20,353!2024-11-06,20,353-->
- [permutation](../../../../general/permutation.md) ::: the arrangement of $k$ things from $n$ things (order matters), calculated by $$P(n, k) = \frac {n!} {(n - k)!}$$ <!--SR:!2024-11-06,20,353!2024-11-06,20,353-->
- [combination](../../../../general/combination.md) ::: choosing $k$ things from $n$ things (order does not matter), calculated by $$C(n, k) = \binom n k = \frac {n!} {(n - k)! k!}$$ <!--SR:!2024-11-06,20,353!2024-11-06,20,353-->
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

- datetime: 2024-09-16T10:30:00+08:00/2024-09-16T11:20:00+08:00
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
- [permutation](../../../../general/permutation.md)
- [combination](../../../../general/combination.md)
- [questions/2024-09-16/tutorial](questions/2024-09-16%20tutorial.md)
- [week 3 problem set](questions/week%203%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/p0Lb0odJCfU)
  - Andreescu and Feng: solve problem 25 to problem 51
- assignments: [homework 1](assignments/homework%201/submission.tex)

## week 3 lecture 2

- datetime: 2024-09-18T09:00:00+08:00/2024-09-18T11:20:00+08:00
- status: unscheduled, public holiday: Day after Mid-Autumn Festival

## week 3 TA session

- datetime: 2024-09-20T19:00:00+08:00/2024-09-20T19:50:00+08:00
- topic: solving weekly problem set 1
- [questions/2024-09-20](questions/2024-09-20.md)
- [week 1 problem set](questions/week%201%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/wbck_JlX9C4)

## week 4 lecture

- datetime: 2024-09-23T10:30:00+08:00/2024-09-23T11:20:00+08:00
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

- datetime: 2024-09-25T09:00:00+08:00/2024-09-25T11:20:00+08:00
- topic: pigeonhole principle
- pigeonhole principle ::: Let _f_ be a mapping from a finite nonempty set _A_ to another nonempty finite set _B_ such that |_A_| > _k_|_B_| for some natural number _k_. Let _f_<sup>-1</sup> be the inverse mapping from _B_ to the power set of _A_. Then there is an element _b_ in _B_ such that |_f_<sup>-1</sup>(_b_)| ≥ _k_ + 1. <!--SR:!2024-11-08,18,357!2025-01-14,70,357-->
  - pigeonhole principle / proof ::: Prove by contradiction. Using the definitions above, assume every element _b_ in _B_ has the property |_f_<sup>-1</sup>(_b_)| < _k_ + 1. Then the maximum cardinality (size) of _A_ is _k_|_B_|. But this contradicts |_A_| > _k_|_B_|. <!--SR:!2024-11-11,21,357!2024-11-08,18,357-->
  - pigeonhole principle / in practice ::: The pigeonhole principle is straight forward. However, the difficult part is identifying the pigeons and holes, which is nontrivial. <!--SR:!2024-11-11,21,357!2024-11-11,21,357-->
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

- datetime: 2024-09-30T10:30:00+08:00/2024-09-30T11:20:00+08:00
- topic: graphs, trees, paths, walks
- [graph theory](../../../../general/graph%20theory.md)
  - graph theory / graph ::: A __graph__ is denoted $G = (V, E)$, where $V$ is a finite set of __vertices__ and _E_ is a finite set of __edges__. <!--SR:!2024-11-11,21,357!2024-11-08,18,357-->
  - graph theory / edge ::: An __edge__ in a graph $G = (V, E)$ is a two-element set $\set{u, v} \subseteq V$, which represents a connection between the vertex _u_ and _v_. <!--SR:!2024-11-08,18,357!2025-01-05,62,357-->
  - graph theory / loop ::: A __loop__ is an edge connecting a vertex to itself, i.e. $\set{u, u}$. But in this course, we do not consider graphs with this case. Graphs without this case are called __simple__. <!--SR:!2024-11-11,21,357!2024-11-08,18,357-->
  - graph theory / neighbor ::: If an edge connects two vertices, the two vertices are said to be __neighbors__ of each other. <!--SR:!2024-11-08,18,357!2024-11-11,21,357-->
  - graph theory / complement of a graph ::: The __complement of a graph__ $G = (V, E)$ is denoted $\overline G = (V, \overline E)$, where $\set{u, v} \in \overline E \equiv \set{u, v} \notin E$. That is, the graph has the same vertices, but for all possible edges between the vertices in the graph, if the edge is present in $G$ then it is not in $\overline G$, and vice versa. <!--SR:!2024-11-11,21,357!2024-11-08,18,357-->
  - graph theory / subgraph ::: A graph is a __subgraph__ of another graph $G$ if its vertices are a subset of those of $G$ and its edges are also a subset of those of $G$. <!--SR:!2024-11-09,19,357!2024-11-09,19,357-->
  - graph theory / isomorphism ::: An __isomorphism__ between two graphs is a bijective mapping of vertices between them that preserves the edges. Informally, the graphs are the same if we do not care about the identities of the vertices. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
  - graph theory / degree ::: The __degree__ of a vertex is the number of other vertices connecting to it. A obvious theorem: the sum of degrees of all vertices is twice the number of edges. <!--SR:!2024-11-11,21,357!2025-01-05,62,357-->
  - graph theory / adjacency matrix ::: The __adjacency matrix__ of a graph with _n_ vertices is a _n_-by-_n_ matrix _A_, where $$A_{ij} = \begin{cases} 1 & \text{if }\set{i, j} \in E \\ 0 & \text{otherwise} \,. \end{cases}$$ <!--SR:!2024-11-08,18,357!2024-11-11,21,357-->
  - graph theory / walk ::: A __walk__ is a sequence of alternating vertices and edges. The sequence starts and ends with a vertex. The edges connects the two vertices adjacent to it in the sequence. Informally, you are walking on the graph. <!--SR:!2024-11-08,18,357!2024-11-11,21,357-->
  - graph theory / trail ::: A __trail__ is a walk with no repeated edges. <!--SR:!2024-12-05,38,337!2024-12-27,52,337-->
  - graph theory / path ::: A __path__ is a walk with no repeated vertices. In the same graph, paths are a subset of trails. In particular, trails include cycles while paths exclude them. <!--SR:!2024-12-27,52,337!2024-11-08,18,357-->
  - graph theory / closed walk, closed trail ::: A walk or trail is __closed__ if it starts and ends at the same vertex. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
  - graph theory / cycle ::: A __cycle__ is a closed walk with no repeat vertices, ignoring the ending vertex (which is the same as the starting vertex). <!--SR:!2025-01-17,73,357!2024-12-21,47,337-->
- theorem: number of possible edges in a graph ::: There are $\binom n 2$ such edges in a graph of _n_ vertices. <p> This is trivial to prove. <!--SR:!2025-01-07,64,357!2024-11-09,19,357-->
- theorem: non-closed walk contains path, closed walk contains cycle ::: Any non-closed walk contains a path. <p> An algorithm (which also proves the theorem) exists for doing so: If a vertex appears two or more times in a walk, remove the sequence from the first appearance of the vertex (exclusive) to its appearance. The resulting walk is still valid. When there are no more repeated vertices, then the walk is also a path. <p> We can prove that any closed walk contains a cycle using the same steps. <!--SR:!2025-01-17,73,357!2024-11-08,18,357-->
- graph theory
  - graph theory / connected vertices ::: Two vertices in a graph are __connected__ if there is a path from one to the other. <!--SR:!2024-11-08,18,357!2024-11-11,21,357-->
  - graph theory / connected graph ::: A graph is __connected__ if every pair of vertices in it are connected. <!--SR:!2025-01-14,70,357!2024-11-11,21,357-->
  - graph theory / connected component (CC) ::: A __connected component__ (__CC__) of a graph _G_ is a __maximal connected subset__ of vertices. It is a subgraph of the graph _G_ to which no vertex of the graph _G_ can be added and make the subgraph still connected. More intuitively and informally, it is the connected subgraphs the graph _G_ is made of. <!--SR:!2024-11-11,21,357!2025-01-17,73,357-->
  - graph theory / tree ::: A __tree__ is (1) a connected graph, (2) has _n_ - 1 edges, and (3) has no cycles. The definition actually only requires two properties out of the properties (1), (2), (3), since the third property can be proven from any other two. <!--SR:!2024-11-11,21,357!2024-11-11,21,357-->
- theorem: minimum number of connected components (CC) ::: A graph has at least |_V_| - |_E_| connected components. <p> To prove this, consider the |_V_| vertices without any edges. There are _V_ CCs, by definition. Now consider the effect of adding an edge. This decreases the number of CCs by at most 1. After adding |_E_| edges, the number of CCs has decreased by at most |_E_|. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
  - theorem: minimum number of connected components (CC) / corollary: connected graph ::: Every connected graph has |_E_| ≥ |_V_| - 1. <!--SR:!2024-11-09,19,357!2024-11-11,21,357-->
- theorem: definition of a tree ::: Given three properties of a tree: (1) a connected graph, (2) has _n_ - 1 edges, and (3) has no cycles. Any two properties implies the third property. <p> To prove this, consider adding |_E_| edges one by one to a graph of |_V_| vertices with no edges, and make use of the theorem relating the number of connected components to |_V_| - |_E_|. <!--SR:!2025-01-05,62,357!2024-11-08,18,357-->
- graph theory
  - graph theory / [cut](../../../../general/cut%20(graph%20theory).md) ::: A __cut__ is a partition of the vertices of a graph into two disjoint subsets. Any cut determines a __cut-set__, the set of edges that have one endpoint in each subset of the partition. These edges are said to __cross__ the cut. <!--SR:!2024-11-08,18,357!2024-12-27,52,337-->
- theorem: connected graph, one-edge cut-set, cycle ::: If a cut-set of a connected graph consists of one edge only, the edge is not part of any cycle. The converse also holds: If an edge is not part of any cycle, it can be a cut-set. <p> To prove theorem and its converse, prove by contradiction. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
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
  - graph theory / leaf ::: A __leaf__ is a vertex of degree 1. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
- theorem: minimum number of leaves in a tree ::: Every tree on _n_ ≥ 2 vertices has at least 2 leaves. <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that vertices cannot be added to the path ends without either making the path longer or violate the graph being a tree. <!--SR:!2024-11-08,18,357!2024-11-11,21,357-->
- theorem: number of possible graphs ::: There are $2^{\binom {\lvert V \rvert} 2}$ possible graphs. <p> To prove this, we can select whether to put an edge for each of the $\binom {\lvert V \rvert} 2$ possible edges. <!--SR:!2024-11-08,18,357!2025-01-05,62,357-->
- [Prüfer sequence](../../../../general/Prüfer%20sequence.md) ::: A sequence of |_V_| - 2 nodes to uniquely encode all possible trees on |_V_| vertices. This means encoding a Prüfer sequence from a tree in the domain of all possible trees is a bijection. <!--SR:!2024-11-08,18,357!2024-11-09,19,357-->
  - theorem: number of possible trees ::: There are $\lvert V \rvert^{\lvert V \rvert - 2}$ possible trees. <p> To prove this, we can use the Prüfer sequence, which can uniquely encode all possible trees. The length of a Prüfer sequence is _n_ - 2 and there are _n_ possible choice for each element. <p> The Prüfer sequence also provides a way to find the number of possible trees with restrictions. For example, the number of possible trees on a complete bipartite graph, with _x_ and _y_ vertices in the two partitions, is $x^{y - 1} y^{x - 1}$. <!--SR:!2025-01-14,71,357!2025-01-17,73,357-->
    - theorem: number of possible trees / [combinatorial proof](../../../../general/combinatorial%20proof.md#the%20difference%20between%20bijective%20and%20double%20counting%20proofs) ::: We can also use a combinatorial proof to prove the above identity. See the linked section. <!--SR:!2024-11-08,18,357!2025-01-14,71,357-->
  - Prüfer sequence / encoding ::: Assume the nodes are labelled from 1 to |_V_|. Let the Prüfer sequence be empty. Find the leaf with the smallest node. Append the node of the leaf's only neighbor to the Prüfer sequence. Remove the leaf. Repeat until there is only 1 edge (or 2 vertices) left. <!--SR:!2025-01-05,62,357!2024-11-11,21,357-->
  - Prüfer sequence / properties ::: The number of times a node appearing in the Prüfer sequence is its degree minus 1. As a special case, nodes that are not in the Prüfer sequence are leaves. <!--SR:!2024-11-11,21,357!2025-01-14,70,357-->
  - Prüfer sequence / decoding ::: Let there be a sequence _N_ of _n_ labelled vertices and a Prüfer sequence. <p> Find the leaf (a node that is not in the Prüfer sequence) with the smallest label in the sequence _N_. Join it with the first node in the Prüfer sequence. Remove said leaf from the sequence _N_ and the first node from the Prüfer sequence. This may make a node in _N_ that was not a leaf now a leaf. <p> Repeat until there are only 2 nodes left in the sequence _N_. Connect those 2 nodes to get the tree. <!--SR:!2024-11-19,18,317!2025-01-17,73,357-->
- theorem: connected graph, one-vertex cut-set (different from the edge-based cut-set above) ::: Every connected graph with |_V_| ≥ 2 has at least two non-cut vertices (vertices that when removed from the graph, will not result in two separate connected graphs). <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that vertices at the path ends cannot be removed such that any two neighbors of them become disconnected, which proves the theorem. <!--SR:!2025-01-05,62,357!2025-01-17,73,357-->
- graph theory
  - graph theory / even cycle ::: An __even cycle__ is a cycle with an even number of vertices. <!--SR:!2024-11-08,18,357!2025-01-05,62,357-->
  - graph theory / odd cycle ::: An __odd cycle__ is an cycle with an odd number of vertices. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
- theorem: odd closed walk contains an odd cycle ::: Every odd closed walk contains an odd cycle. <p> To prove this, consider a odd walk on even (not odd, because the first and last vertices are repeated) number of vertices, with the start being the same as the end. If there are no repeats in between, it is already an odd cycle. Otherwise, we try to remove contagious subsequences in between two repeated vertices of it so that it becomes an odd cycle. If we can keep removing an even number of vertices, we will eventually get an odd cycle. If we need to remove an odd number of vertices at any point, said removed vertices is an odd cycle itself. <!--SR:!2024-11-11,21,357!2025-01-14,70,357-->
- graph theory
  - graph theory / [bipartite graph](../../../../general/bipartite%20graph.md) ::: A __bipartite graph__ is a graph whose vertices can be divided into two disjoint and independent sets _U_ and _V_, that is, every edge connects a vertex in _U_ connects to one in _V_. Equivalently, the graph does not contain any odd-length cycles. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
    - theorem: bipartite graph, no odd cycles ::: A graph is bipartite iff it has no odd cycles. <p> It is easy to prove a bipartite graph has no odd cycles by considering trying to form a cycle in it. <p> The converse is more difficult. But we can show its existence by an algorithm: Start from an arbitrary vertex, then put it into _X_. Put its neighbors into _Y_. Then put the neighbors of its neighbors, ignoring those already visited into _X_. Its correctness can be proven by consider that between any two distinct vertices, either all walks between them are odd non-closed walks or all walks between them are even non-closed walks. This shows the algorithm can assign all vertices consistently to either _X_ or _Y_. <!--SR:!2024-11-11,21,357!2025-01-17,73,357-->
- theorem: minimum degree, cycle ::: If the minimum degree of any vertex is 2, the graph has a cycle. <p> To prove this, use the extremal principle on the possible paths in a tree. In particular, assert the existence of a longest path. Then show that a neighbor of a path end cannot be outside the path. <!--SR:!2025-01-05,62,357!2024-11-11,21,357-->
- theorem: maximum degree, cycle ::: If the maximum degree of any vertex is 2, every connected component is either a cycle or path. <p> To prove this, use the extremal principle on the possible paths for each connected component. In particular, assert the existence of a longest path for each connected component. Then show that the path cannot have edges added to it without making it a cycle. <!--SR:!2025-01-17,73,357!2025-01-05,62,357-->
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

- datetime: 2024-10-02T09:00:00+08:00/2024-10-02T11:20:00+08:00
- topic: even more theorems on graphs and trees
- theorem: even degree, cycle ::: If every vertex has an even degree, the edge set is a disjoint union of cycles. <p> To prove this, we can apply induction on the number of edges. The base cases are 0 and 1 edges. The induction step can be proved by starting from a vertex and show that it eventually ends at the same vertex; remove that cycle and the induction hypothesis can be applied. <!--SR:!2025-01-07,64,357!2025-01-05,62,357-->
- graph theory
  - graph theory / [Eulerian path](../../../../general/Eulerian%20path.md), Eulerian circuit ::: The first one is a walk that passes over every edge exactly once. The second one additionally requires the walk to be closed. <!--SR:!2024-11-11,21,357!2025-01-17,73,357-->
    - theorem: connected graph, even degree, Eulerian circuit ::: A connected graph has an Eulerian circuit iff every vertex has an even degree. <p> To prove that an Eulerian circuit implies every vertex has an even degree, consider the sequence of vertices and edges in a Eulerian circuit. (Joining the sequence at the ends to make it circular may help.) Consider the every appearance of a vertex in the sequence. <p> To prove the converse, decompose the graph into a disjoint union of edge sets of cycles. Then a Eulerian circuit can be constructed from it. Induction on the number of disjoint edge sets of cycles may be used. <!--SR:!2025-01-07,64,357!2024-12-22,48,337-->
  - graph theory / [Hamiltonian path](../../../../general/Hamiltonian%20path.md), Hamiltonian cycle ::: The first one is a walk that visits all vertices exactly once. The second one additionally requires the walk to be closed. <!--SR:!2025-01-17,73,357!2025-01-05,62,357-->
- theorem: minimum bipartite subgraph ::: A graph has a bipartite subgraph with at least |_E_| / 2 edges. <p> To prove this, show that we can always construct such a subgraph. Partition all vertices of a graph arbitrary into two sets. The edges that has an endpoint in both sets form a bipartite subgraph. Then consider any vertex in the graph. The vertex has some edges to its own set and the remaining edges to the other set. The remaining edges to the other sets is in the bipartite subgraph. If the edges to its own set is more than the edges to the other set, we can move the vertex to the other set such that these two sets of edges are swapped. Finally, we obtain a configuration where every vertex has edges to the other set as many as that to its own set. So the bipartite graph includes at least |_E_| / 2 edges. <p> A hint of the above method comes from the division by 2... which hints at some greater than or equal to argument. <!--SR:!2025-01-17,73,357!2024-12-21,47,337-->
- graph theory
  - graph theory / degree sequence ::: A __degree sequence__ is the non-increasing sequence of an undirected graph's vertex degrees. (Amir uses non-decreasing for some reason... but it should be equivalent). <!--SR:!2024-11-08,18,357!2025-01-17,73,357-->
    - theorem: degree sequence, not necessarily simple graph ::: An arbitrary sequence is the degree sequence of a not necessarily simple (no self-loops) graph if the sum of the arbitrary sequence is even. <p> To prove it, pair up vertices with odd degrees together to make them even. There must be an even number of them. Then add a lot of self-loops to satisfy the degree sequence. <p> Note: Such a degree sequence is graphic if it is the degree sequence of a _simple_ graph. It may be found using the Havel–Hakimi algorithm, a greedy algorithm. <!--SR:!2025-01-07,64,357!2024-11-08,18,357-->
- [Havel–Hakimi algorithm](../../../../general/Havel–Hakimi%20algorithm.md) ::: Let there be an arbitrary sequence _A_. Sort the sequence in non-increasing order. Remove the first element, which has the value _s_. Decrement 1 from the first _s_ element of the sequence. This produces a new sequence _A_'. Repeat the above (including the sorting). If the sequence is graphic, then it must eventually reduce to an sequence of zeros. <p> _A_ is graphic iff _A_' is graphic. Proving this property proves the algorithm. <p> The forward and backward cases are kind of easy to prove: If _A_ is graphic, the above operations corresponds to removing a vertex with maximum degree. If the vertex's edges connect to the _s_ vertices with the max _s_ degrees, then the graph is represented by _A_'. If not, we note that any degree surplus and deficit can always be corrected to obtain a graph represented by _A_'. <p> If _A_' is graphic, the inverse of the above operation corresponds to adding a vertex and connecting them to a graph represented by _A_'. <!--SR:!2025-01-17,73,357!2025-01-07,64,357-->
- theorem: tree, unique paths ::: A graph is a tree iff there are unique paths between every pair of vertices. To prove this, make use of the three properties of a tree. <p> If a graph is a tree, consider any pair of vertices. A path must exist, or otherwise the tree is not connected. But there must not be more than a path between them, or otherwise a closed walk exist, which implies the tree has a cycle. <p> If there are unique paths between every pair of vertices, the graph is connected. There are also no cycles, or otherwise there is a pair of vertices with more than a path. So the graph is a tree. <!--SR:!2025-01-07,64,357!2025-01-14,71,357-->
- theorem: connected graph, subgraph, tree ::: Every _connected_ graph has a tree subgraph connecting all vertices in the graph. The tree subgraph is known as a _spanning tree_. <p> Apply depth-first search (DFS) to visit all vertices. Show that the edges used by DFS is a tree. <p> The graph is connected, trivially. To show that the graph has _n_ - 1 edges, note that DFS uses an edge per vertex visited except for the stating vertex. To show that the graph has no cycles, note that every edge only ever connects a vertex at distance _d_ to _d_ + 1, which is monotonic. <!--SR:!2024-11-11,21,357!2025-01-05,62,357-->
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

- datetime: 2024-10-07T10:30:00+08:00/2024-10-07T11:20:00+08:00
- topic: minimum spanning trees, directed graphs, DAGs
- theorem: adding an edge, tree, cycle ::: Adding an edge to a tree creates exactly one cycle. <p> Recall that in a tree, every pair of vertex has an unique path. Adding an edge to any pair of vertex makes this unique path a cycle. <p> However, there is only one cycle created. We note that any cycles created must pass through the new edge, because there were no cycles before we have added the edge. If there were multiple cycles created, then the pair of vertex we have added an edge to would have multiple paths before adding the edge. <!--SR:!2025-01-14,71,357!2025-01-05,62,357-->
- graph theory
  - graph theory / weighted graph ::: A __weighted graph__ is a graph with an function that maps every edge to a real number. Or, informally, every edge has a real number as its weight. <!--SR:!2024-11-11,21,357!2025-01-17,73,357-->
  - graph theory / spanning tree ::: A __spanning tree__ of a graph is a tree that connects all vertices in the graph. We have already shown this must exist for a _connected_ graph by a theorem before. <!--SR:!2024-11-09,19,357!2024-11-09,19,357-->
  - graph theory / minimum spanning tree ::: A __minimum spanning tree__ of a weighted graph is the spanning tree of a weighted graph with the least total weight in its vertices. <p> There are two greedy algorithms for this that we will learn: Kruskal's algorithm and Prim's algorithm. <!--SR:!2024-11-08,18,357!2024-11-08,18,357-->
- [Kruskal's algorithm](../../../../general/Kruskal's%20algorithm.md) ::: Sort the edges in non-decreasing weight. For each edge, add it to the resulting tree if adding it does not create a cycle, otherwise discard the edge. Repeat until all edges are processed. <p> To prove that the resulting edges spans all vertices given the graph is connected, prove by contradiction. If the resulting edges do not connect all vertices, that means there are multiple connected components in the resulting tree. But since the original graph is connected, there are edges connecting in between the multiple connected components which are discarded. Consider the first such edge examined by the algorithm. It should not be discarded, because adding it must not create a cycle. <p> To prove that the resulting edges is a minimum spanning tree (MST) given the graph is connected, also prove by contradiction. If the resulting edges are not a MST, there is a different selection of edges that is a MST. Consider the first edge _e_ examined by the algorithm that is in the resulting edges but not in the MST. Add said edge to the MST to add exactly one cycle. Since the resulting edges form a tree and have no cycles, there is an edge _e_' in the cycle that is not in the resulting edges. Remove that edge to get another spanning tree. _e_ must be examined before _e_' because otherwise _e_ instead of _e_' would have been discarded for forming a cycle. The above operations replaced the edge _e_' with _e_, which must not increase the total weight by the above. This means either the MST is not minimum, a contradiction; or the MST can be eventually be made into the resulting edges without decreasing its weight by repeating the above arguments, so the resulting edges are also a MST. <!--SR:!2024-12-27,52,337!2025-01-05,62,357-->
- [Prim's algorithm](../../../../general/Prim's%20algorithm.md) ::: Start with an empty tree. Add an arbitrary vertex to it. Grow the tree by one edge at a time: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and add it to the tree. Repeat until all vertices are added. <p> The resulting tree is obviously a tree. To prove that the resulting tree is also a minimum spanning tree (MST) given that the graph is connected, prove by contradiction. Assume the resulting tree is not a MST. Then consider each step of the algorithm. Either the algorithm adds an edge that is in the MST or not. Consider the first instance when the algorithm adds an edge _e_ that is not in the MST. Let _V_ be the set of vertices in the tree before the algorithm adds the edge _e_, noting that _V_ is a subgraph of the MST. The edge _e_ connects a vertex _v_ in _V_ and another vertex _u_ not in _V_. Since MST is a spanning tree and _V_ is a subgraph of the MST, there is also an edge _f_ of MST that connects the vertex _v_ and another vertex not in _V_ that is in the path from _v_ to _u_. Edge _e_ and _f_ are not the same, otherwise the edge added is in the MST. The weight of edge _f_ must be not less than _e_ or otherwise the algorithm would have added edge _f_ instead. Consider adding the edge _e_ to the MST. This creates exactly one cycle. Edge _f_ must be in the cycle because both edge _e_ and edge _f_ are in paths from _v_ to _u_. Removing _f_ breaks this cycle, so the resulting graph is another spanning tree. So we have effectively replaced edge _f_ in the MST with edge _e_ to get another spanning tree. But since the weight of _f_ is not less than _e_, the new spanning tree either has equal or smaller weight. This means either the MST is not minimum, a contradiction; or the MST can be eventually be made into the resulting tree without decreasing its weight by repeating the above arguments, so the resulting tree is also a MST. <p> The argument, especially the last part, is similar to that for Kruskal's algorithm. <!--SR:!2024-11-21,24,317!2025-01-05,62,357-->
- graph theory
  - graph theory / directed graph ::: __Directed graph__ is a graph, but the edges are the two-element tuples $(u, v)$ instead of the two-element set $\set{u, v}$. The tuple means an arrow connects from the vertex _u_ to vertex _v_. <!--SR:!2024-11-12,21,369!2025-01-14,70,369-->
  - graph theory / strongly connected ::: Two vertices _u_ and _v_ in a graph is __strongly connected__ if there is a path from _u_ to _v_ and from _v_ to _u_. <p> For undirected graphs, two vertices are strongly connected if there is a path between from _u_ to _v_, because we can easily reverse the path to get a path from _v_ to _u_. For directed graphs, however, this is not the case. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / strongly connected component (SCC) ::: A __strong connected component__ (__SCC__) is a connected component (CC) such that every pair of vertices are strongly connected. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
- theorem: directed simple graph, cycle, strongly connected component ::: A directed simple graph (no self-loops) has no cycles iff every vertex is a strongly connected component by itself. <p> To prove this and its converse, use contradiction. <!--SR:!2024-11-12,21,369!2024-12-15,45,349-->
- graph theory
  - graph theory / [topological ordering](../../../../general/topological%20sorting.md) ::: A __topological sort__ or __topological ordering__ of a directed graph is a linear ordering (permutation) of its vertices such that for every directed edge (_u_, _v_) from vertex _u_ to vertex _v_, _u_ comes before _v_ in the ordering. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / [directed acyclic graph](../../../../general/directed%20acyclic%20graph.md) (DAG) ::: A __directed acyclic graph__ (__DAG__) is a directed graph with no directed cycles. <!--SR:!2024-12-15,45,349!2024-11-12,21,369-->
- theorem: directed acyclic graph, topological ordering ::: A directed graph is a directed acyclic graph (DAG) iff the graph has a topological ordering. <p> To prove this and is converse, use contradiction. Two lemmas below and depth-first search (DFS) are useful here. <!--SR:!2024-11-06,16,348!2024-11-12,21,369-->
  - lemma: directed graph and minimum out-degree ::: If the out-degree of every vertex of a directed graph is 1, then there is a directed cycle. <p> To prove this, we can keep moving to new nodes if there are no directed cycles. <!--SR:!2024-11-19,27,368!2024-11-19,27,368-->
  - lemma: directed graph and minimum in-degree ::: If the in-degree of every vertex of a directed graph is 1, the there is a directed cycle. <p> To prove this, we can keep moving to new nodes backwards if there are no directed cycles. <!--SR:!2024-11-12,21,369!2024-12-15,45,349-->
- directed acyclic graph game ::: Two players start at a vertex of a loopless directed acyclic graph. In each turn, each player can move the current vertex through one outgoing edge. A player who cannot make a move loses. <p> We can prove the game always ends because there are no directed cycles. Also, we can also mark each vertex as a winning and losing position, starting from vertices with 0 out-degrees as losing, and alternating between winning and losing (with the winning position overriding the losing position) as we go through the directed edges in reverse. <!--SR:!2024-11-12,21,369!2024-12-15,45,349-->
- graph theory
  - graph theory / rooted tree ::: A __rooted tree__ is a tree with a vertex designated as the root. We can keep the tree undirected, or make it directed such that any other vertices can be reached from the root following the arrows. <!--SR:!2024-11-19,27,368!2024-11-12,21,369-->
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
  - graph theory / independent set ::: An __independent set__ is a set of vertices in a graph, no two of which are adjacent. <!--SR:!2024-11-12,21,369!2024-11-19,27,368-->
- [Huffman coding](../../../../general/Huffman%20coding.md) ::: A particular type of optimal prefix code (no code is a prefix of any other code) that is commonly used for lossless data compression. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - Huffman coding / algorithm ::: Suppose there are _n_ words that appears _w_<sub>_i_</sub> times. Keep merging 2 words that appears least frequently to become one word with their appearance frequencies combined. Keep track of how the words are merged and represent it as a tree. <p> The resulting tree is a binary tree for its Huffman coding. The leaves represent each word. The route it takes to reach a word is the Huffman coding for that word. <!--SR:!2024-11-19,27,368!2024-11-19,27,368-->
- [questions/2024-10-07/tutorial](questions/2024-10-07%20tutorial.md)
- materials
  - [lecture video](https://youtu.be/4CPfs1XUg_w)
  - West/Section 2.3: Optimization and Trees
  - [video: Huffman coding and Huffman trees](https://youtu.be/JsTptu56GM8)
  - [video: Huffman coding example](https://youtu.be/apcCVfXfcqE)
  - [recommended video: Huffman coding + code](https://youtu.be/AwsNoQKcHg0)
  - [recommended video: dynamic programming on trees](https://youtu.be/tzuJeiGJvYY)

## week 6 lecture 2

- datetime: 2024-10-09T09:00:00+08:00/2024-10-09T11:20:00+08:00
- topic: distance, shortest paths, matchings
- graph theory
  - graph theory / distance ::: The __distance__ between two vertices (repeats allowed) in a graph is the minimum number of edges in a path connecting the two vertices. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / eccentricity ::: The __eccentricity__ of a vertex in a graph is the maximum distance it can have with any vertex in the same graph. <!--SR:!2024-11-12,21,369!2024-11-10,18,349-->
  - graph theory / center ::: The __center__ of a graph is a vertex with the minimum eccentricity among all of its vertices. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / radius ::: The __radius__ of a graph is the minimum eccentricity of its vertices, i.e. the eccentricity of its center. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / diameter ::: The __diameter__ fo a graph is the maximum distances any pair of vertices (repeats allowed) can have. <!--SR:!2024-11-19,27,368!2024-11-12,21,369-->
- theorem: radius and diameter of a graph ::: For any graph, the following relationship holds: radius ≤ diameter ≤ 2 · radius. <p> To prove this, draw its diameter (which is a shortest path between the two points) and its center. Consider the case if the center is in the diameter path and if not in the diameter path. <!--SR:!2024-11-12,21,369!2024-11-19,27,368-->
- theorem: tree, leaf, center ::: No leaf can be a center of a tree with 3 or more vertices. <p> To prove this, suppose a leaf is a center. We can write the leaf's only neighbor's distance to any other vertex in terms of the distance of the leaf to any other vertex. This would produce a contradiction. <!--SR:!2024-12-15,45,349!2025-01-14,70,369-->
- theorem: tree, center ::: A tree either has one center or two _neighboring_ centers. <p> This can be proven using strong induction. Prove the base case for |_V_| = 1 and |_V_| = 2. Then realize that any tree can be transformed into a smaller one by removing all of its leaves so that we can apply the induction hypothesis. After applying the hypothesis, re-adding the leaves preserves the centers. Consider the smaller tree with its centers as the roots to figure out why re-adding the leaves preserves the centers. <!--SR:!2024-11-28,28,329!2024-11-10,18,348-->
- [Dijkstra's algorithm](../../../../general/Dijkstra's%20algorithm.md) ::: A common algorithm for finding the shortest paths between nodes in a weighted graph. <!--SR:!2024-11-19,27,368!2025-01-14,70,369-->
  - Dijkstra's algorithm / algorithm ::: Say we are finding the shortest distance from the vertex _u_ to every other vertices. Start by initializing distances: $d(u) = 0, d(v) = \infty$. Create a priority queue containing all vertices in the graph, ordered by non-decreasing distance $d(v)$. While the priority queue is nonempty, extract the first vertex _v_. For each neighbor _n_ of the vertex _v_, assign $d(n) = \min\set{d(n), d(v) + w(v \rightarrow n)}$. Update the priority queue if needed. Repeat until the queue is empty. <p> To prove the correctness of Dijkstra's algorithm, notice that for a shortest path from _a_ to _z_: _a_ → ... → _y_ → _z_, this implies the path from _a_ to _y_ must also be the shortest between them: _a_ → ... → _y_. <!--SR:!2024-12-15,45,348!2024-11-19,27,368-->
- graph theory
  - graph theory / matching ::: A __matching__ of a graph is the set of edges in which no two edges share an endpoint. <!--SR:!2024-11-12,21,369!2024-11-12,21,369-->
  - graph theory / maximal matching (not to be confused with _maximum matching_) ::: A __maximal matching__, not to be confused with _maximum matching_, of a graph is a matching that is not a proper subset of any other matching. A maximal matching is not necessarily a maximum matching, but the converse is true. <!--SR:!2024-11-17,20,380!2024-11-17,20,380-->
  - graph theory / maximum matching (not to be confused with _maximal matching_) ::: A __maximum matching__, not to be confused with _maximal matching_, of a graph is a matching with a maximum number of edges. A maximum matching is a maximal matching, but the converse is false. <!--SR:!2024-11-19,27,368!2024-11-19,27,368-->
  - graph theory / alternating walk, alternating path ::: An __alternating walk__ of a matching is a walk that alternates between edges in the matching and not in the matching. An __alternating path__ is defined analogously. <!--SR:!2024-11-19,27,368!2024-11-12,21,369--> <p> Outside this course, an __alternating walk__ is more commonly defined to additionally require beginning with an unmatched vertex.
  - graph theory / augmenting path ::: An __augmenting path__ of a matching is an alternating _path_ that starts and ends with a vertex not covered by the matching. <!--SR:!2024-11-06,16,349!2024-11-06,16,347-->
- theorem: maximum matching, augmenting path ::: A matching is _maximum_ (which implies _maximal_) iff it does not contain an augmenting path. <p> It is easy to prove that a maximum matching does not contain an augmenting path. Simply switch the edges in the augmenting path, if it exists, to get a larger matching. Use this to prove by contradiction. <p> The converse is harder. Assume there is a matching _M_ without augmenting paths. Consider any other matching _M_'. Define a new graph consisting of the original vertices and edges that are in either _M_ or _M_' but not both (exclusive-or). This operation will not increase the number of edges in _M_ and that in _M_' in the new graph. Also, the decrease in number of edges in _M_ and that in _M_' is also the same. The new graph consists of either paths or cycles because the degree of each vertex is at most 2. In the new graph, any path and cycle alternates between _M_ and _M_'. Since _M_ has no augmenting paths, any path must start and end at a vertex that is covered by _M_. For any cycle, the number of edges in _M_ and _M'_ must be the same. So, in the new graph, |_M_'| ≤ |_M_|. Then, since the decrease in edges is the same for both matchings, |_M_'| ≤ |_M_| in the original graph. <!--SR:!2024-12-15,45,348!2024-11-12,21,369-->
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

- datetime: 2024-10-11T19:00:00+08:00/2024-10-11T19:50:00+08:00
- topic: solving weekly problem set 4
- [questions/2024-10-11](questions/2024-10-11.md)
- [week 4 problem set](questions/week%204%20problem%20set.md)
- materials
  - [lecture video](https://youtu.be/jIsRmWzacfI)

## week 7 lecture

- datetime: 2024-10-14T10:30:00+08:00/2024-10-14T11:20:00+08:00
- topic: matchings, vertex covers, edge covers, independent sets
- theorem: bipartite graph, matching ::: In an bipartite of a graph into _X_ and _Y_, where |_X_| ≤ |_Y_|, there is a matching saturating _X_ iff for every subset of _X_, the number of its neighbors (which must all be in _Y_) is at least the size of the subset. <p> Proving the number of its neighbors is at least the size of the subset is trivial. The converse is much harder. <p> To prove the converse, we use contradiction. Suppose there is a _maximum_ matching _M_ that does not saturate _X_. Take any element _x_ in _X_ not covered by _M_ and produce a subset {_x_}. Since {_x_} must have at least one neighbor as a subset of _X_, it must connect to an element _y_ in _Y_. But the element _y_ must be covered by _M_, or otherwise the matching is not maximum. Then consider the element _y_. It is in _M_, so there is another element in _X_ that is not _x_ that connects to _y_. Add that element to the subset. Now the minimum number of neighbors is 2. So there must be another edge to connect to an new element in _Y_. The edge either connects _x_ to an element in _Y_ that is in _M_, or connects elements that are not _x_ to any element in _Y_ but not already connected by any edge. In both case, the above argument can be repeated again and again. If at any point, an element in _Y_ that is not in _M_ is connected, the matching can be shifted, then _x_ can finally match with _y_, producing a larger matching. This must eventually happen because we will run out of elements of _Y_ that are in _M_ before running out of elements of _X_, because _M_ does not saturate _X_. <!--SR:!2024-11-19,27,368!2024-11-28,28,329-->
  - theorem: bipartite graph, perfect matching / corollary: _k_-regular bipartite graph ::: Let _G_ be a _k_-regular bipartite graph _k_ ≥ 1. _G_ has a perfect matching. <p> To prove this, consider an arbitrary subset _S_ of one of the partition, and consider the number of edges between _S_ and _N_(_S_) to show that _S_ ≤ |_N_(_S_)|. Finally, apply the theorem. <!--SR:!2025-01-14,70,367!2024-12-15,45,349-->
- graph theory
  - graph theory / vertex cover ::: A __vertex cover__ |_A_| is a set of vertices such that every edge has at least one endpoint in the cover. <!--SR:!2025-01-14,70,369!2025-01-14,70,369-->
- theorem: minimum vertex cover, maximum matching ::: In every graph, the minimum vertex cover has a size of at least that of _maximum_ matching. <p> To prove this, consider a maximum matching. For every edge in the maximum matching, one point must be in the vertex cover. <!--SR:!2024-11-12,21,369!2024-12-22,47,349-->
- theorem: minimum vertex cover, maximum matching, bipartite graph ::: In every bipartite graph, the minimum vertex cover has a size equals that of maximum matching. <p> To prove this, we can prove the minimum vertex cover has a size smaller than or equal to that of maximum matching. Consider a maximum matching in a bipartite graph. Then consider a minimum vertex cover and split the two bipartition sets into two separate bipartitions depending on if the element is in the minimum vertex cover. Show that the minimum vertex cover implies the existence of a maximum matching on both bipartitions, which can be merged back to get a maximum matching on the original bipartition. <p> Combining with the previous theorem gives us the equality result. <!--SR:!2024-11-28,28,329!2024-12-22,47,349-->
- [questions/2024-10-14/lecture](questions/2024-10-14%20lecture.md)

## week 7 tutorial

- datetime: 2024-10-14T18:00:00+08:00/2024-10-14T18:50:00+08:00
- [questions/2024-10-14/tutorial](questions/2024-10-14%20tutorial.md)

## week 7 lecture 2

- datetime: 2024-10-16T09:00:00+08:00/2024-10-16T11:20:00+08:00
- [questions/2024-10-16](questions/2024-10-16.md)
- [week 7 problem set](questions/week%207%20problem%20set.md)

## midterm exam

- datetime: 2024-10-18T18:00:00+08:00/2024-10-18T21:00:00+08:00, PT3H
- venue: Lecture Theater C
- grades: ?/30
- report
  - TODO
