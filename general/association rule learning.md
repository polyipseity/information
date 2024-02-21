---
aliases:
  - association rule
  - association rules
  - association rule learning
tags:
  - flashcard/general/association_rule_learning
  - language/in/English
---

# association rule learning

## useful concepts

### support

Support is {{how frequently the item set appears in the data set}}. For a item set X, it is defined as {{$\operatorname{supp}(X) = P(X) = \frac {\text{number of transactions containing }X} {\text{total number of transactions} }$}}. An alternative definition is simply {{the number of transactions containing X}}, in which case adjust the equations below yourself accordingly. <!--SR:!2024-02-27,16,290!2024-02-26,15,290!2024-02-24,13,290-->

### confidence

Confidence is {{the ratio of all transactions satisfying the antecedent that also satisfies the consequent}}. For two item sets X and Y, and {{a rule $X \Rightarrow Y$ with X as the antecedent and Y as the consequent, the confidence of the rule is defined as $\operatorname{conf}(X \Rightarrow Y) = P(Y \vert X) = \frac {\operatorname{supp}(X \cup Y)} {\operatorname{supp}(X)} = \frac {\text{number of transactions containing both }X\text{ and }Y} {\text{number of transactions containing }X}$}}. <!--SR:!2024-02-25,14,290!2024-03-10,20,290-->

Confidence expresses {{how confident you can be about Y being true given X is true}}. <!--SR:!2024-02-26,15,290-->

### lift

Lift is {{the ratio of the observed support of a rule to that expected if the antecedent and the consequent are [independent](independence%20(probability%20theory).md)}}. For two item sets X and Y, and {{a rule $X \Rightarrow Y$ with X as the antecedent and Y as the consequent, the lift of the rule is defined as $\operatorname{lift}(X \Rightarrow Y) = \frac {\operatorname{conf}(X \Rightarrow Y)} {\operatorname{supp}(Y)} = \frac {\operatorname{supp}(X \cup Y)} {\operatorname{supp}(X) \times \operatorname{supp}(Y)}$}}. <!--SR:!2024-02-26,15,290!2024-02-25,14,290-->

Lift expresses {{the observed co-occurrence of X and Y compared to that expected if X and Y are [independent](independence%20(probability%20theory).md)}}. Note that the lift is unchanged even if {{the antecedent and the consequent are exchanged, i.e. $\operatorname{lift}(X \Rightarrow Y) = \operatorname{lift}(Y \Rightarrow X)$}}. <!--SR:!2024-02-27,16,290!2024-02-26,15,290-->

### conviction

Conviction is {{the ratio of the incorrectness of a rule, if the antecedent and the consequent are [independent](independence%20(probability%20theory).md), to the observed incorrectness}}. For two item sets X and Y, and {{a rule $X \Rightarrow Y$ with X as the antecedent and Y as the consequent, the lift of the rule is defined as $\operatorname{conv}(X \Rightarrow Y) = \frac {\operatorname{supp}(\lnot Y)} {\operatorname{conf}(X \Rightarrow \lnot Y)} = \frac {1 - \operatorname{supp}(Y)} {1 - \operatorname{conf}(X \Rightarrow Y)}$}}. <!--SR:!2024-02-28,17,290!2024-03-15,24,270-->

Conviction expresses {{how often X fails to predict Y if X and Y are [independent](independence%20(probability%20theory).md) compared to that observed}}. <!--SR:!2024-02-27,16,290-->

## algorithms

### naive algorithms

Assume one has two criteria for finding rules: {{minimum support and minimum confidence}}. A naive algorithm can simply {{enumerate all possible rules and filter the rules by minimum support and minimum confidence}}. However, this is impractical for even moderately-sized datasets because {{the number of all possible rules increases exponentially with the number of columns}}. A less naive approach is first filter for {{large item sets using the minimum support, enumerate all the possible rules, then filter the rules by minimum confidence}}. It significantly decreases {{the number of possible rules, though still not enough for even larger datasets}}. We can prove these two algorithms are equivalent by {{proving that their respective output sets $S_1, S_2$ are equal, i.e. $S_1 = S_2$}}, which is usually done by proving {{$S_1 \subseteq S_2$ i.e. every item in $S_1$ is in $S_2$, and $S_1 \supseteq S_2$ i.e. every item in $S_2$ is in $S_1$}}. <!--SR:!2024-02-24,13,290!2024-02-26,15,290!2024-02-24,13,290!2024-03-31,39,290!2024-03-18,26,270!2024-02-27,16,290!2024-02-28,17,290-->

> [!info]- details
>
> Proof of equivalency of the two naive algorithms:
>
> $$\begin{aligned}
> & \text{Let } S_* \text{ be sets of item sets and } R_* \text{ be sets of rules.} \\
> & \text{Naive algorithm: } S_0 \xrightarrow{ \text{enumerate all possible rules} } R_1 \xrightarrow{ \text{filter by minimum support and minimum confidence} } R_2 \\
> & \text{Less naive algorithm: } S_0 \xrightarrow{ \text{filter by minimum support} } S'_1 \xrightarrow{ \text{enumerate all possible rules} } R'_1 \xrightarrow{ \text{filter by minimum confidence} } R'_2 \\
> & \text{Proof of } R_2 \subseteq R'_2 \\
> & \begin{aligned} R \in R_2 & \implies \operatorname{supp}(R) \ge \mathrm{supp}_\mathrm{min} \land \operatorname{conf}(R) \ge \mathrm{conf}_\mathrm{min} && \forall R \in R_2 \\
> \operatorname{supp}(R) \ge \mathrm{supp}_\mathrm{min} & \implies \operatorname{supp}(\operatorname{ante}(R) \cup \operatorname{cons}(R)) \ge \mathrm{supp}_\mathrm{min} \\
> & \implies \operatorname{supp}(\operatorname{ante}(R)) \ge \mathrm{supp}_\mathrm{min} \land \operatorname{supp}(\operatorname{ante}(R) \cup \operatorname{cons}(R)) \ge \mathrm{supp}_\mathrm{min} && (\text{downward closure lemma}) \\
> & \implies \operatorname{ante}(R) \in S'_1 \land \operatorname{ante}(R) \cup \operatorname{cons}(R) \in S'_1 \\
> & \implies R \in R'_1 && (R'_1 \text{ enumerates all possible rules from } S'_1) \\
> R \in R'_1 \land \operatorname{conf}(R) \ge \mathrm{conf}_\mathrm{min} & \implies R \in R'_2 && (\text{filter}) \end{aligned} \\
> & \text{Proof of } R'_2 \subseteq R_2 \\
> & \begin{aligned} R' \in R'_2 & \implies \operatorname{conf}(R') \ge \mathrm{conf}_\mathrm{min} && \forall R' \in R'_2 \\
> R' \in R'_2 & \implies R' \in R'_1 && (\text{filter}) \\
> & \implies \operatorname{ante}(R') \in S'_1 \land \operatorname{ante}(R') \cup \operatorname{cons}(R') \in S'_1 && (R'_1 \text{ enumerates all possible rules from } S'_1) \\
> \operatorname{ante}(R') \cup \operatorname{cons}(R') \in S'_1 & \implies \operatorname{supp}(\operatorname{ante}(R') \cup \operatorname{cons}(R')) \ge \mathrm{supp}_\mathrm{min} \\
> & \implies \operatorname{supp}(R') \ge \mathrm{supp}_\mathrm{min} \\
> S'_1 \subseteq S_0 & \implies R'_1 \subseteq R_1 && (\text{enumeration}) \\
> R' \in R'_1 \land R'_1 \subseteq R_1 & \implies R' \in R_1 \\
> R' \in R_1 \land \operatorname{supp}(R') \ge \mathrm{supp}_\mathrm{min} \land \operatorname{conf}(R') \ge \mathrm{conf}_\mathrm{min} & \implies R' \in R_2 && (\text{filter}) \end{aligned} \\
> & \text{Finally, } R_2 \subseteq R'_2 \land R'_2 \subseteq R_2 \implies R_2 = R'_2 \\
> & \text{This completes the proof.}
> \end{aligned}$$

### Apriori algorithm

See [Apriori algorithm](Apriori%20algorithm.md).

## references

This text incorporates [content](https://en.wikipedia.org/wiki/association_rule_learning) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
