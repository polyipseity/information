---
aliases:
  - logical equivalence
  - logical equivalences
tags:
  - flashcard/active/general/logical_equivalence
  - language/in/English
---

# logical equivalence

In [logic](logic.md) and [mathematics](mathematics.md), statements $p$ and $q$ are {{said to be __logically equivalent__ if they have the same [truth value](truth%20value.md) in every [model](structure%20(mathematical%20logic).md)}}. The logical equivalence of $p$ and $q$ is sometimes expressed as {{$p\equiv q$, $p : : q$, ${\textsf {E} }pq$, or $p\iff q$, depending on the notation being used}}. However, these symbols are {{also used for [material equivalence](if%20and%20only%20if.md), so proper interpretation would depend on the context}}. Logical equivalence is {{different from material equivalence, although the two concepts are intrinsically related}}. <!--SR:!2024-11-03,39,290!2024-12-07,68,330!2024-11-15,50,310!2024-11-07,44,310-->

## logical equivalences

In logic, many common logical equivalences {{exist and are often listed as laws or properties}}. The following tables illustrate some of these. <!--SR:!2024-10-30,35,289-->

### general logical equivalences

- identity laws ::: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2024-10-31,38,301!2024-12-13,73,321-->
- domination laws ::: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2025-01-23,97,301!2024-11-26,59,310-->
- idempotent or tautology laws ::: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2024-12-15,74,321!2024-11-21,55,310-->
- [double negation](double%20negation.md) law ::: $$\neg (\neg p)\equiv p$$ <!--SR:!2024-11-24,57,310!2024-11-25,55,301-->
- [commutative laws](commutative%20property.md) ::: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2024-12-07,67,321!2024-11-23,56,310-->
- [associative laws](associative%20property.md) ::: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2024-12-06,68,329!2024-11-14,48,290-->
- [distributive laws](distributive%20property.md) ::: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2024-11-01,39,301!2025-03-21,144,301-->
- [De Morgan's laws](De%20Morgan's%20laws.md) ::: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2024-11-06,43,301!2024-12-08,68,316-->
- [absorption laws](absorption%20law.md) ::: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2024-11-02,38,290!2024-11-29,62,316-->
$p\vee (p\wedge q)\equiv p$$p\wedge (p\vee q)\equiv p$
- negation laws ::: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2024-12-15,74,329!2024-12-12,71,321-->

### logical equivalences involving conditional statements

- [material implication](material%20implication%20(rule%20of%20inference).md) & primitives ::: $$p\implies q\equiv \neg p\vee q$$ <!--SR:!2024-11-05,40,310!2024-11-16,51,310-->
- [transposition](contraposition.md) ::: $$p\implies q\equiv \neg q\implies \neg p$$ <!--SR:!2024-11-29,58,310!2024-12-05,66,330-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [disjunction](logical%20disjunction.md) ::: $$p\vee q\equiv \neg p\implies q$$ <!--SR:!2024-11-17,52,310!2025-03-08,135,310-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [conjunction](logical%20conjunction.md) ::: $$p\wedge q\equiv \neg (p\implies \neg q)$$ <!--SR:!2024-11-10,46,310!2024-11-11,47,310-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [negation](negation.md) ::: $$\neg (p\implies q)\equiv p\wedge \neg q$$ <!--SR:!2024-11-18,52,310!2024-12-22,68,310-->
- [distributive laws](distributive%20property.md) ::: $$\begin{aligned} (p\implies q)\wedge (p\implies r) & \equiv p\implies (q\wedge r) \\ (p\implies q)\vee (p\implies r) & \equiv p\implies (q\vee r) \end{aligned}$$ <!--SR:!2024-12-01,64,330!2024-12-14,73,330-->
- [antidistributive laws](distributive%20property.md) ::: $$\begin{aligned} (p\implies r)\wedge (q\implies r) & \equiv (p\vee q)\implies r \\ (p\implies r)\vee (q\implies r) & \equiv (p\wedge q)\implies r \end{aligned}$$ <!--SR:!2024-11-12,48,310!2024-11-20,54,310-->

### logical equivalences involving biconditionals

- [material equivalence](if%20and%20only%20if.md) & [material implication](material%20implication%20(rule%20of%20inference).md) ::: $$p\iff q\equiv (p\implies q)\wedge (q\implies p)$$ <!--SR:!2024-12-06,67,330!2024-12-14,74,330-->
- [material equivalence](if%20and%20only%20if.md) & inner [negation](negation.md) ::: $$p\iff q\equiv \neg p\iff \neg q$$ <!--SR:!2024-12-04,65,330!2024-12-04,66,330-->
- [material equivalence](if%20and%20only%20if.md) & primitives ::: $$p\iff q\equiv (p\wedge q)\vee (\neg p\wedge \neg q)$$ <!--SR:!2024-11-25,58,310!2024-12-17,77,330-->
- [material equivalence](if%20and%20only%20if.md) & outer [negation](negation.md) ::: $$\neg (p\iff q)\equiv p\iff \neg q\equiv p\oplus q$$ <!--SR:!2024-12-18,77,330!2024-11-16,51,310-->

where $\oplus$ {{represents [XOR](exclusive%20or.md)}}. <!--SR:!2024-12-10,70,321-->

## relation to material equivalence

Logical equivalence is {{different from material equivalence}}. Formulas $p$ and $q$ are {{logically equivalent if and only if the statement of their material equivalence ($p\leftrightarrow q$) is a tautology}}. <!--SR:!2024-11-19,52,310!2024-11-11,47,301-->

The material equivalence of $p$ and $q$ (often written as {{$p\leftrightarrow q$}}) is {{itself another statement in the same [object language](formal%20system.md) as $p$ and $q$}}. This statement {{expresses the idea "'$p$ if and only if $q$'". In particular, the truth value of $p\leftrightarrow q$ can change from one model to another}}. <!--SR:!2025-01-02,79,290!2024-11-17,51,296!2024-10-29,36,301-->

On the other hand, the claim that two formulas are logically equivalent is {{a statement in [metalanguage](metalanguage.md), which expresses a relationship between two statements $p$ and $q$}}. The statements are {{logically equivalent if, in every model, they have the same truth value}}. <!--SR:!2024-11-10,46,309!2025-01-05,77,276-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/logical_equivalence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
