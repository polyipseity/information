---
aliases:
  - logical equivalence
  - logical equivalences
tags:
  - flashcard/active/general/eng/logical_equivalence
  - language/in/English
---

# logical equivalence

In [logic](logic.md) and [mathematics](mathematics.md), statements $p$ and $q$ are {@{said to be __logically equivalent__ if they have the same [truth value](truth%20value.md) in every [model](structure%20(mathematical%20logic).md)}@}. The logical equivalence of $p$ and $q$ is sometimes expressed as {@{$p\equiv q$, $p : : q$, ${\textsf {E} }pq$, or $p\iff q$, depending on the notation being used}@}. However, these symbols are {@{also used for [material equivalence](if%20and%20only%20if.md), so proper interpretation would depend on the context}@}. Logical equivalence is {@{different from material equivalence, although the two concepts are intrinsically related}@}. <!--SR:!2027-03-16,700,330!2025-10-19,316,350!2028-02-28,985,350!2027-09-29,865,350-->

## logical equivalences

In logic, many common logical equivalences {@{exist and are often listed as laws or properties}@}. The following tables illustrate some of these. <!--SR:!2026-07-04,464,309-->

### general logical equivalences

- identity laws ::@:: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2027-04-05,723,341!2025-11-04,326,341-->
- domination laws ::@:: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2026-03-11,412,321!2028-10-27,1173,350-->
- idempotent or tautology laws ::@:: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2025-11-11,329,341!2028-06-24,1074,350-->
- [double negation](double%20negation.md) law ::@:: $$\neg (\neg p)\equiv p$$ <!--SR:!2028-09-16,1141,350!2028-04-29,1021,341-->
- [commutative laws](commutative%20property.md) ::@:: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2029-08-05,1403,361!2028-08-14,1115,350-->
- [associative laws](associative%20property.md) ::@:: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2029-11-25,1501,369!2027-09-03,830,330-->
- [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2027-05-04,746,341!2026-11-12,601,321-->
- [De Morgan's laws](De%20Morgan's%20laws.md) ::@:: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2027-07-14,798,341!2029-07-30,1394,356-->
- [absorption laws](absorption%20law.md) ::@:: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2027-01-24,660,330!2029-02-04,1256,356-->
- negation laws ::@:: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2025-11-22,340,349!2025-10-28,319,341-->

### logical equivalences involving conditional statements

- [material implication](material%20implication%20(rule%20of%20inference).md) & primitives ::@:: $$p\implies q\equiv \neg p\vee q$$ <!--SR:!2027-07-05,797,350!2028-04-08,1016,350-->
- [transposition](contraposition.md) ::@:: $$p\implies q\equiv \neg q\implies \neg p$$ <!--SR:!2028-09-17,1138,350!2029-09-25,1453,370-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [disjunction](logical%20disjunction.md) ::@:: $$p\vee q\equiv \neg p\implies q$$ <!--SR:!2028-05-06,1038,350!2026-10-08,579,330-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [conjunction](logical%20conjunction.md) ::@:: $$p\wedge q\equiv \neg (p\implies \neg q)$$ <!--SR:!2027-11-19,903,350!2027-12-20,930,350-->
- [material implication](material%20implication%20(rule%20of%20inference).md) & [negation](negation.md) ::@:: $$\neg (p\implies q)\equiv p\wedge \neg q$$ <!--SR:!2028-04-09,1015,350!2029-07-09,1361,350-->
- [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} (p\implies q)\wedge (p\implies r) & \equiv p\implies (q\wedge r) \\ (p\implies q)\vee (p\implies r) & \equiv p\implies (q\vee r) \end{aligned}$$ <!--SR:!2029-08-11,1419,370!2025-11-12,333,350-->
- [antidistributive laws](distributive%20property.md) ::@:: $$\begin{aligned} (p\implies r)\wedge (q\implies r) & \equiv (p\vee q)\implies r \\ (p\implies r)\vee (q\implies r) & \equiv (p\wedge q)\implies r \end{aligned}$$ <!--SR:!2028-01-19,951,350!2027-08-13,763,330-->

### logical equivalences involving biconditionals

- [material equivalence](if%20and%20only%20if.md) & [material implication](material%20implication%20(rule%20of%20inference).md) ::@:: $$p\iff q\equiv (p\implies q)\wedge (q\implies p)$$ <!--SR:!2029-11-24,1501,370!2025-11-19,340,350-->
- [material equivalence](if%20and%20only%20if.md) & inner [negation](negation.md) ::@:: $$p\iff q\equiv \neg p\iff \neg q$$ <!--SR:!2029-08-27,1429,370!2029-10-18,1473,370-->
- [material equivalence](if%20and%20only%20if.md) & primitives ::@:: $$p\iff q\equiv (p\wedge q)\vee (\neg p\wedge \neg q)$$ <!--SR:!2028-09-25,1147,350!2025-12-07,355,350-->
- [material equivalence](if%20and%20only%20if.md) & outer [negation](negation.md) ::@:: $$\neg (p\iff q)\equiv p\iff \neg q\equiv p\oplus q$$ <!--SR:!2025-12-03,350,350!2028-03-27,1006,350-->

where $\oplus$ {@{represents [XOR](exclusive%20or.md)}@}. <!--SR:!2025-10-23,317,341-->

## relation to material equivalence

Logical equivalence is {@{different from material equivalence}@}. Formulas $p$ and $q$ are {@{logically equivalent if and only if the statement of their material equivalence ($p\leftrightarrow q$) is a tautology}@}. <!--SR:!2028-05-09,1039,350!2027-11-02,886,341-->

The material equivalence of $p$ and $q$ (often written as {@{$p\leftrightarrow q$}@}) is {@{itself another statement in the same [object language](formal%20system.md) as $p$ and $q$}@}. This statement {@{expresses the idea "'$p$ if and only if $q$<!-- LaTeX separator -->'". In particular, the truth value of $p\leftrightarrow q$ can change from one model to another}@}. <!--SR:!2028-02-28,923,310!2027-12-19,917,336!2026-05-05,446,321-->

On the other hand, the claim that two formulas are logically equivalent is {@{a statement in [metalanguage](metalanguage.md), which expresses a relationship between two statements $p$ and $q$}@}. The statements are {@{logically equivalent if, in every model, they have the same truth value}@}. <!--SR:!2027-12-01,915,349!2025-10-31,299,296-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/logical_equivalence) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
