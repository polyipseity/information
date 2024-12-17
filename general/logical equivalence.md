---
aliases:
  - logical equivalence
  - logical equivalences
tags:
  - flashcard/active/general/logical_equivalence
  - language/in/English
---

# logical equivalence

In [logic](logic.md) and [mathematics](mathematics.md), statements $p$ and $q$ are {@{said to be __logically equivalent__ if they have the same [truth value](truth%20value.md) in every [model](structure%20(mathematical%20logic).md)}@}. The logical equivalence of $p$ and $q$ is sometimes expressed as {@{$p\equiv q$, $p : : q$, ${\textsf {E} }pq$, or $p\iff q$, depending on the notation being used}@}. However, these symbols are {@{also used for [material equivalence](if%20and%20only%20if.md), so proper interpretation would depend on the context}@}. Logical equivalence is {@{different from material equivalence, although the two concepts are intrinsically related}@}. <!--SR:!2025-04-15,163,310!2025-10-19,316,350!2025-06-18,215,330!2025-05-16,190,330-->

## logical equivalences

In logic, many common logical equivalences {@{exist and are often listed as laws or properties}@}. The following tables illustrate some of these. <!--SR:!2025-03-27,148,309-->

### general logical equivalences

- identity laws ::@:: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2025-04-12,163,321!2025-11-04,326,341-->
- domination laws ::@:: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2025-01-23,97,301!2025-08-11,258,330-->
- idempotent or tautology laws ::@:: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2025-11-11,329,341!2025-07-15,236,330-->
- [double negation](double%20negation.md) law ::@:: $$\neg (\neg p)\equiv p$$ <!--SR:!2025-08-02,251,330!2025-07-13,230,321-->
- [commutative laws](commutative%20property.md) ::@:: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2025-10-02,299,341!2025-07-26,245,330-->
- [associative laws](associative%20property.md) ::@:: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2025-10-16,313,349!2025-05-26,193,310-->
- [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2025-04-18,168,321!2025-03-21,144,301-->
- [De Morgan's laws](De%20Morgan's%20laws.md) ::@:: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2025-05-05,180,321!2025-10-05,301,336-->
- [absorption laws](absorption%20law.md) ::@:: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2025-04-04,153,310!2025-08-28,272,336-->
$p\vee (p\wedge q)\equiv p$$p\wedge (p\vee q)\equiv p$
- negation laws ::@:: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2025-11-22,340,349!2025-10-28,319,341-->

### logical equivalences involving conditional statements

- [material implication](material%20implication%20(rule%20of%20inference).md) & primitives ::@:: $$p\implies q\equiv \neg p\vee q$$ <!--SR:!2025-04-29,175,330!2025-06-27,223,330-->
- [transposition](contraposition.md) ::@:: $$p\implies q\equiv \neg q\implies \neg p$$ <!--SR:!2025-08-06,250,330!2025-10-03,302,350-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [disjunction](logical%20disjunction.md) ::@:: $$p\vee q\equiv \neg p\implies q$$ <!--SR:!2025-07-03,228,330!2025-03-08,135,310-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [conjunction](logical%20conjunction.md) ::@:: $$p\wedge q\equiv \neg (p\implies \neg q)$$ <!--SR:!2025-05-29,200,330!2025-06-03,204,330-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [negation](negation.md) ::@:: $$\neg (p\implies q)\equiv p\wedge \neg q$$ <!--SR:!2025-06-29,223,330!2024-12-22,68,310-->
- [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} (p\implies q)\wedge (p\implies r) & \equiv p\implies (q\wedge r) \\ (p\implies q)\vee (p\implies r) & \equiv p\implies (q\vee r) \end{aligned}$$ <!--SR:!2025-09-22,295,350!2025-11-12,333,350-->
- [antidistributive laws](distributive%20property.md) ::@:: $$\begin{aligned} (p\implies r)\wedge (q\implies r) & \equiv (p\vee q)\implies r \\ (p\implies r)\vee (q\implies r) & \equiv (p\wedge q)\implies r \end{aligned}$$ <!--SR:!2025-06-09,209,330!2025-07-11,233,330-->

### logical equivalences involving biconditionals

- [material equivalence](if%20and%20only%20if.md) & [material implication](material%20implication%20(rule%20of%20inference).md) ::@:: $$p\iff q\equiv (p\implies q)\wedge (q\implies p)$$ <!--SR:!2025-10-15,312,350!2025-11-19,340,350-->
- [material equivalence](if%20and%20only%20if.md) & inner [negation](negation.md) ::@:: $$p\iff q\equiv \neg p\iff \neg q$$ <!--SR:!2025-09-28,298,350!2025-10-06,306,350-->
- [material equivalence](if%20and%20only%20if.md) & primitives ::@:: $$p\iff q\equiv (p\wedge q)\vee (\neg p\wedge \neg q)$$ <!--SR:!2025-08-04,252,330!2025-12-07,355,350-->
- [material equivalence](if%20and%20only%20if.md) & outer [negation](negation.md) ::@:: $$\neg (p\iff q)\equiv p\iff \neg q\equiv p\oplus q$$ <!--SR:!2024-12-18,77,330!2025-06-25,221,330-->

where $\oplus$ {@{represents [XOR](exclusive%20or.md)}@}. <!--SR:!2025-10-23,317,341-->

## relation to material equivalence

Logical equivalence is {@{different from material equivalence}@}. Formulas $p$ and $q$ are {@{logically equivalent if and only if the statement of their material equivalence ($p\leftrightarrow q$) is a tautology}@}. <!--SR:!2025-07-05,228,330!2025-05-29,199,321-->

The material equivalence of $p$ and $q$ (often written as {@{$p\leftrightarrow q$}@}) is {@{itself another statement in the same [object language](formal%20system.md) as $p$ and $q$}@}. This statement {@{expresses the idea "'$p$ if and only if $q$<!-- LaTeX separator -->'". In particular, the truth value of $p\leftrightarrow q$ can change from one model to another}@}. <!--SR:!2025-01-02,79,290!2025-06-15,210,316!2025-02-13,107,301-->

On the other hand, the claim that two formulas are logically equivalent is {@{a statement in [metalanguage](metalanguage.md), which expresses a relationship between two statements $p$ and $q$}@}. The statements are {@{logically equivalent if, in every model, they have the same truth value}@}. <!--SR:!2025-05-30,201,329!2025-01-05,77,276-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/logical_equivalence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
