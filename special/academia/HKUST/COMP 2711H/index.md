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
  - homework: 10% × 4. It must be written in LaTeX. After submitting the homework, the instructor and TAs will read the submission and give feedback. You can then resubmit once more. The highest out of the 2 submission wills be counted. Resubmission may be disallowed if the initial submission is low quality or lack effort.
  - midterm examination: 30%.
  - final examination: 30%. It covers the entire course.
- [problems](problems.md)

## week 1 lecture

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:20:00+08:00
- course logistics
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ propositional calculus](../../../../general/propositional%20calculus.md#propositional%20calculus)
    - proposition ::: A declarative statement that is either true (1) or false (0). No third value is possible. Typically it is represented by _p_, _q_, _r_, and so forth. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - [truth table](../../../../general/truth%20table.md) ::: A table representing a boolean function. There are $n + 1$ columns, where the first $n$ columns are the inputs of the boolean function, while the last column is the output of the boolean function. There are $2^n$ rows, representing all possible combinations of the $n$ inputs mapping to the corresponding $2^n$ outputs. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - [§ truth table](../../../../general/truth%20table.md#truth%20table)
  - boolean algebra operations ::: An operation that takes connections one or more propositions. These operations can be chained. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - negation (not) ::: $\lnot p$: $$\begin{aligned} (0) & \mapsto 1 \\ (1) & \mapsto 0 \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - disjunction (or) ::: $p \lor q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 1 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
    - conjunction (and) ::: $p \land q$: $$\begin{aligned} (0, 0) & \mapsto 0 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 0 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
    - implication (if-then) ::: $p \rightarrow q$: $$\begin{aligned} (0, 0) & \mapsto 1 \\ (1, 0) & \mapsto 0 \\ (0, 1) & \mapsto 1 \\ (1, 1) & \mapsto 1 \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - boolean algebra operations / order of operations ::: $\lnot$ > $\lor, \land$ > $\rightarrow$ <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
  - [tautology](../../../../general/tautology%20(logic).md) (true) ::: A proposition that is always true, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - [§ tautology](../../../../general/tautology%20(logic).md#tautology)
  - [contradiction](../../../../general/contradiction.md) (false) ::: A proposition that is always false, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - [§ contradiction](../../../../general/contradiction.md#contradiction)
  - propositional calculus / real life application ::: Consider making a one bit half adder. You want: $$\begin{aligned} 0 + 0 & = 0 \\ 1 + 0 & = 1 \\ 0 + 1 & = 1 \\ 1 + 1 & = 0 \end{aligned}$$. This can be expressed as $$\begin{aligned} \text{sum of products: } & (a \land \lnot b) \lor (\lnot a \land b) \\ \text{product of sums: } & (\lnot a \lor \lnot b) \land (a \lor b) \end{aligned}$$. This is also known as the exclusive-or (xor) operation. <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
  - [logical equivalence](../../../../general/logical%20equivalence.md) ::: Two propositions have the same truth values, no matter how the atomic propositions (terms with no operations) are assigned. One simple way to prove it is via a truth table and compare whether the rows are equivalent. <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
    - [§ logical equivalence](../../../../general/logical%20equivalence.md#logical%20equivalence)
    - [§ relation to material equivalence](../../../../general/logical%20equivalence.md#relation%20to%20material%20equivalence) ::: Material equivalence is simply a proposition that says two propositions have the same truth values. It may be false or true. Two propositions are logically equivalent if material equivalence is true, no matter how the atomic propositions (terms with no operations) are assigned. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - [§ general logical equivalences](../../../../general/logical%20equivalence.md#general%20logical%20equivalences)
  - [conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md) ::: The dual (Amir calls it inverse proposition) of a proposition $p$ is denoted $p^d$, and is formed by replacing $\land$ by $\lor$, $\lor$ by $\land$, T by F, and F by T. The dual relates to the original proposition by $\lnot p \equiv \overline p^d$, where $\overline p$ is replacing all atomic propositions (propositions without $\land$, $\lor$, and $\lnot$) by their negations. This can be interpreted as negating the "output" of $p$, i.e. $\lnot p$ is the same as negating all "inputs" of its dual $p^d$, i.e. $\overline p^d$. <!--SR:!2024-09-18,6,263!2024-09-23,11,283-->
    - [§ conjunction/disjunction duality](../../../../general/conjunction_disjunction_duality.md#conjunction%2Fdisjunction%20duality)
    - [§ negation is semantically equivalent to dual](../../../../general/conjunction_disjunction_duality.md#negation%20is%20semantically%20equivalent%20to%20dual)
    - [§ further duality theorems](../../../../general/conjunction_disjunction_duality.md#further%20duality%20theorems)
  - [rules of inference](../../../../general/rules%20of%20inference.md) ::: Rules that allows deducing a consequence to be true, given that zero or more premises are true. <!--SR:!2024-09-13,4,300!2024-09-13,4,300-->
    - [rules of inference](../../../../general/rules%20of%20inference.md) / motivation ::: To prove a proposition $X := h_1 \land \ldots \land h_n \rightarrow c$ is true, where $h_i$ are _atomic_ variables (terms with no operations), one could use a proof table, but this would require $2^n$ rows. We could instead use another proposition equivalent to $X$, denoted $Y := p_1 \land \ldots \land p_n \rightarrow c$ where $p_i$ are propositions (not necessarily atomic). Coupled with _rules of inference_, we can prove $X$ via proving $Y$. <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
    - rules of inference / _modus ponens_ ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{p \phantom{\rightarrow q} } \\ & q & \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / hypothetical syllogism ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{q \rightarrow r} \\ & p \rightarrow r & \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / _modus tollens_ (not to be confused with the related _contraposition_) ::: $$\begin{aligned} & p \rightarrow q \\ & \underline{\lnot q \!\!\!\! \phantom{\rightarrow q} } \\ & \lnot p & \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->

## week 1 tutorial

- time: 2024-09-02T18:00:00+08:00/2024-09-02T18:50:00+08:00
- [propositional calculus](../../../../general/propositional%20calculus.md)
  - [§ list of classically valid argument forms](../../../../general/propositional%20calculus.md#list%20of%20classically%20valid%20argument%20forms)
  - [rules of inference](../../../../general/rules%20of%20inference.md_
    - _modus ponens_
    - hypothetical syllogism
    - _modus tollens_
    - rules of inference / conjunction ::: $$\begin{aligned} & p \\ & \underline{q \phantom{\land q} } \\ & p \land q & \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / disjunctive syllogism ::: $$\begin{aligned} & p \lor q \\ & \underline{\lnot p \!\!\!\! \phantom{\lor q} } \\ & q \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / transposition (with $F$ as the consequent) ::: $$\begin{aligned} & \underline{\lnot p \rightarrow F} \\ & p \end{aligned}$$ <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
    - rules of inference / simplification ::: $$\begin{aligned} & \underline{p \land q} \\ & p \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / addition ::: $$\begin{aligned} & \underline{p \phantom{\lor q} } \\ & p \lor q \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
    - rules of inference / importation (applied form) ::: $$\begin{aligned} & p \land q \\ & \underline{p \rightarrow (q \rightarrow r)} \\ & r \end{aligned}$$ <!--SR:!2024-09-20,8,250!2024-09-13,4,283-->
    - rules of inference / constructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{p \lor r \phantom{s} } \\ & q \lor s \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
    - rules of inference / destructive dilemma ::: $$\begin{aligned} & p \rightarrow q \\ & r \rightarrow s \\ & \underline{\lnot q \lor \lnot s} \\ & \lnot p \lor \lnot r \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
    - rules of inference / constructive dilemma (unapplied form, with the same consequent) ::: $$\begin{aligned} & p \rightarrow r \\ & \underline{q \rightarrow r \phantom{r \rightarrow r} } \\ & (p \lor q) \rightarrow r \end{aligned}$$ <!--SR:!2024-09-18,6,263!2024-09-13,4,283-->
    - rules of inference / material equivalence (_modus ponens_) ::: $$\begin{aligned} & p \equiv q \\ & \underline{p \phantom{\equiv q} } \\ & q \end{aligned}$$ <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - proof format ::: A proof consists of several lines. Each line, numbered, is a proof statement, which either states the premise or is a statement derived from previous statements (referenced using line numbers) by rules of inference. For example: $$\begin{aligned} 1. \quad & p \rightarrow r && (\text{premise}) \\ 2. \quad & p && (\text{premise}) \\ 3. \quad & r && (\text{from 1 and 2}) \end{aligned}$$. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
- [first-order logic](../../../../general/first-order%20logic.md)
  - [§ first-order logic](../../../../general/first-order%20logic.md#first-logic%20logic)
  - [predicate](../../../../general/predicate%20(mathematical%20logic).md) ::: A statement that becomes a proposition when the one or more unknowns are replaced by specified values from the universe. The universe is the set of all possible values for the unknowns. <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
  - universal quantification ::: $\forall x \, p(x)$ means for all $x$ in the universe $p(x)$ is true. If the universe is empty, $\forall x \, p(x)$ is true for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to existential quantification by $$\lnot \forall x \, p(x) \equiv \exists x \, \lnot p(x)$$. <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
    - universal quantification / distributive law ::: It distributes over logical conjunctions: $$\forall x \, (p(x) \land q(x)) \equiv \forall x \, p(x) \land \forall x \, q(x)$$. But it does NOT distribute over logical disjunctions: $$\forall x \, (p(x) \lor q(x)) \leftarrow \forall x \, p(x) \lor \forall x \, q(x)$$ and only the converse (shown above) is true. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - existential quantification ::: $\exists x \, p(x)$ means there is at least one $x$ in the universe that $p(x)$ is true. If the universe is empty, $\exists x \, p(x)$ is false for any predicate $p(x)$ (including predicates that look "opposite", i.e. something is true and something is not true). It relates to universal quantification by $$\lnot \exists x \, p(x) \equiv \forall x \, \lnot p(x)$$. <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
    - existential quantification / distributive law ::: It distributes over logical disjunctions: $$\exists x \, (p(x) \lor q(x)) \equiv \exists x \, p(x) \lor \exists x \, q(x)$$. But it does NOT distribute over logical conjunctions: $$\exists x \, (p(x) \land q(x)) \rightarrow \exists x \, p(x) \land \exists x \, q(x)$$ but the converse is not necessarily true. <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->
- [Peano axioms](../../../../general/Peano%20axioms.md) ::: (The second-order formulation is used.) One, $0$ is a natural number. Two, if $n$ is a natural number, then $S(n)$ is a natural number. Third, if $S(n) = S(m)$, then $n = m$. Four, $S(n) \ne 0$ for all natural numbers $n \in \mathbb N$. Five, if $K$ is a set such that $0 \in K$, and for all natural numbers $n \in \mathbb N$, if $n \in K$ then $S(n) \in K$, then $K = \mathbb N$ (induction). <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - [§ Peano axioms](../../../../general/Peano%20axioms.md#Peano%20axioms)
  - [§ historical second-order formulation](../../../../general/Peano%20axioms.md#historical%20second-order%20formulation)
  - Peano axioms / 1st axiom motivation ::: This defines the starting $0$ as a natural number. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - Peano axioms / 2nd axiom motivation ::: This defines a successor function $S$ that can generate more natural numbers. Equivalently, the natural numbers are closed under $S$. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - Peano axioms / 3rd axiom motivation ::: This makes the successor function injective (but not surjective, as $0$ is not in the image of the function). <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - Peano axioms / 4th axiom motivation ::: Coupled with the injective property, this makes the successor function never go back to the starting number $0$. Otherwise, the successor function can, at one point, loop back to $0$, and there will only be finitely many natural numbers. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - Peano axioms / 5th axiom motivation ::: The 4 axioms above are insufficient to ensure that repeatedly applying $S$ on $0$ can generate all natural numbers. Indeed, an infinite successor chain starting from $0$ that does not contain all the natural numbers, with a finite circular successor chain, is compatible with the 4 axioms above. The 5th axiom simply states that the infinite successor chain starting from $0$ is the set of all natural numbers, excluding the situation above. This is also what makes mathematical induction possible. <!--SR:!2024-09-13,4,283!2024-09-13,4,270-->

## week 1 lecture 2

- time: 2024-09-04T09:00:00+08:00/2024-09-04T11:20:00+08:00
- [Peano axioms](../../../../general/Peano%20axioms.md)
  - [§ defining arithmetic operations and relations](../../../../general/Peano%20axioms.md#defining%20arithmetic%20operations%20and%20relations)
  - [§ addition](../../../../general/Peano%20axioms.md#addition) ::: 2 rules: $\forall n; n + 0 = n$, $\forall n, m; n + s(m) = s(n + m)$. All other rules that you know of everyday addition can be derived from these rules. From this we can prove that addition is commutative ($\forall n, m; n + m = m + n$) and associative ($\forall n, m, o; (n + m) + o = n + (m + o)$). <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - [§ multiplication](../../../../general/Peano%20axioms.md#multiplication) ::: Assuming addition is defined, 2 rules: $\forall n, n \cdot 0 = 0$, $\forall n, m; n \cdot s(m) = n + n \cdot m$. All other rules that you know of everyday multiplication can be derived from these rules. From this we can prove that multiplication is commutative ($\forall n, m; n \cdot m = m \cdot n$) and associative ($\forall n, m, o; (n \cdot m) \cdot o = n \cdot (m \cdot o)$). <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - [§ inequalities](../../../../general/Peano%20axioms.md#inequalities) ::: Assuming addition is defined, the inequality $\le$ is defined as $$n \le m \equiv \exists x; n + x = m$$. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
- [well-ordering principle](../../../../general/well-ordering%20principle.md) ::: Every _non-empty_ subset of the natural numbers (not integers) has a least element. Proofs using this are generally by contradiction. This, induction (from Peano axioms), and proof by infinite descent are equivalent to each other. <!--SR:!2024-09-13,4,270!2024-09-13,4,283-->
  - [§ well-ordering principle](../../../../general/well-ordering%20principle.md#well-ordering%20principle)
- [proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md) ::: There are no infinite strictly decreasing sequences of natural numbers. Proofs using this are generally by contradiction, and involve constructing an infinite descent of natural numbers, which contradicts this. Another way is assuming a minimal solution to a problem exists, but then prove that it would lead to a smaller solution. This, induction (from Peano axioms), and well-ordering principle are equivalent to each other. <!--SR:!2024-09-13,4,283!2024-09-13,4,283-->
  - [§ proof by infinite descent](../../../../general/proof%20by%20infinite%20descent.md#proof%20by%20infinite%20descent)
- [problems § 2024-09-04](problems.md#2024-09-04)
- [problems § week 1](problems.md#week%201) (to be done out-of-class, but is not homework)
