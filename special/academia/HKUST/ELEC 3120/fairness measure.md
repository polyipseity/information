---
aliases:
  - ELEC 3120 fairness measure
  - ELEC3120 fairness measure
  - HKUST ELEC 3120 fairness measure
  - HKUST ELEC3120 fairness measure
  - Jain's fairness index
  - fairness index
  - fairness measure
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/fairness_measure
  - language/in/English
---

# fairness measure

A fairness measure turns whether an allocation is fair into a number, so two allocations compare by one figure. Jain's fairness index is the usual measure for network bandwidth: it returns 1 when the shares are equal and falls toward the floor of $1/n$ as one flow takes more. The index needs only the shares and the number of flows.

---

Flashcards for this section are as follows:

- fairness measure: what question does a fairness measure turn into a number? ::@:: Whether the shares a set of flows receive are fairly divided.
- range: what does Jain's fairness index return for equal shares, and what is its lowest value with $n$ flows? ::@:: $1$ for equal shares, falling to $1/n$ when one flow takes everything.
- usual measure for bandwidth: which fairness measure is the usual one for comparing allocations of network bandwidth? ::@:: Jain's fairness index.
- inputs needed: what does Jain's fairness index need in order to score an allocation? ::@:: Only the shares the flows receive and the number of flows.

<!-- check: ignore-next-line[header_style]: Jain's is a proper name -->
## Jain's fairness index

For shares $x_1, \ldots, x_n$ the index is $F(x) = \left(\sum_i x_i\right)^2 / \left(n \sum_j x_j^2\right)$: the square of the summed shares, over $n$ times the sum of their squares.

---

Flashcards for this section are as follows:

- the formula: what is Jain's fairness index for shares $x_1, \ldots, x_n$? ::@:: $F(x) = \left(\sum_i x_i\right)^2 / \left(n \sum_j x_j^2\right)$.
- three flows: what does Jain's fairness index give for shares $4$, $4$, and $2$? ::@:: $(4 + 4 + 2)^2/(3 \times (16 + 16 + 4)) = 100/108 \approx 0.93$.

### expectation form

Draw one of the $n$ flows at random and let $X$ be its share. Then $E[X] = (\sum_i x_i)/n$ and $E[X^2] = (\sum_i x_i^2)/n$, so $E[X]^2/E[X^2] = (\sum_i x_i)^2/(n \sum_i x_i^2)$, the same number as the sum form.

---

Flashcards for this section are as follows:

- expectation form: with $X$ the share of a flow drawn at random from the $n$ flows, what are $E[X]$ and $E[X^2]$? ::@:: $E[X] = (\sum_i x_i)/n$ and $E[X^2] = (\sum_i x_i^2)/n$.
- expectation form of the index: with $E[X]$ and $E[X^2]$ the mean share and the mean square share, which ratio equals Jain's fairness index? ::@:: $E[X]^2/E[X^2] = (\sum_i x_i)^2/(n \sum_i x_i^2)$, the sum form.

### variance form

Because $E[X^2] = E[X]^2 + Var(X)$, the index is $F = E[X]^2/(E[X]^2 + Var(X)) = 1/(1 + Var(X)/E[X]^2) = 1/(1 + CV^2)$, where $CV = \sqrt{Var(X)}/E[X]$ is the coefficient of variation. The index is 1 exactly when $Var(X) = 0$, so when every flow receives the same share. A wider spread raises the variance and lowers the index, down to the floor of $1/n$ when one flow takes the whole link and the other $n - 1$ receive nothing.

With shares 4, 4 and 2 Mbps, $E[X] = 10/3$, $E[X^2] = 12$ and $Var(X) = 12 - 100/9 = 8/9$, giving $F = (100/9)/12 = 100/108 \approx 0.93$.

---

Flashcards for this section are as follows:

- variance form: how is $F = E[X]^2/E[X^2]$ written with the variance of the shares? ::@:: $F = 1/(1 + Var(X)/E[X]^2) = 1/(1 + CV^2)$, since $E[X^2] = E[X]^2 + Var(X)$.
- coefficient of variation: what is the coefficient of variation $CV$ of the shares? ::@:: $CV = \sqrt{Var(X)}/E[X]$, the standard deviation divided by the mean.
- when the index is one: for which shares is Jain's fairness index exactly $1$? ::@:: When $Var(X) = 0$, so every flow receives the same share.
- variance of three shares: for shares $4$, $4$ and $2$ Mbps, what are $E[X]$, $E[X^2]$ and $Var(X)$? ::@:: $E[X] = (4 + 4 + 2)/3 = 10/3$, $E[X^2] = (16 + 16 + 4)/3 = 12$ and $Var(X) = 12 - 100/9 = 8/9$.

## two-flow split

On a 50 Mbps link between two flows, equal shares of 25 Mbps each give $50^2 / (2 \times (625 + 625)) = 1$. Shares of 40 Mbps and 10 Mbps give $50^2 / (2 \times (1600 + 100)) = 0.74$. In the variance reading $E[X] = 25$, $E[X^2] = 850$, $Var(X) = 850 - 625 = 225$, and $F = 625/850 = 0.735$. Shares of 30 Mbps and 20 Mbps give $50^2 / (2 \times (900 + 400)) = 2500/2600 = 0.96$, although one flow has half again the bandwidth of the other.

---

Flashcards for this section are as follows:

- variance of an uneven split: for a $50\text{ Mbps}$ link split $40\text{ Mbps}$ and $10\text{ Mbps}$, what are $E[X]$, $E[X^2]$, $Var(X)$ and $F$? ::@:: $E[X] = (40 + 10)/2 = 25$, $E[X^2] = (1600 + 100)/2 = 850$, $Var(X) = 850 - 625 = 225$ and $F = 625/850 = 0.735$.
- reading the number: a $50\text{ Mbps}$ link split $40\text{ Mbps}$ and $10\text{ Mbps}$ scores $0.74$; what does that say about the two flows? ::@:: The shares are uneven but neither flow is starved.
- a moderate split: on a $50\text{ Mbps}$ link split $30\text{ Mbps}$ and $20\text{ Mbps}$, what does the index give? ::@:: $50^2/(2 \times (900 + 400)) = 2500/2600 \approx 0.96$, close to 1 although one flow has half again the bandwidth.

## limits of an index

An index scores equality, and equality is often not what a link should deliver. Flows want different amounts, and one may need a smaller delay rather than a larger share. A high score can then certify a division that should never happen, and a low score can flag one that is right. The index reports the division it is given. It is no target to maximise. Where demand differs, a demand-based measure such as [max-min fairness](max-min%20fairness.md) says what the allocation ought to be. Where the shares are meant to differ, the index has to be weighted by what each flow is owed.

---

Flashcards for this section are as follows:

- what it does not say: what does a fairness index leave undecided? ::@:: What the division ought to be, since it only scores the division it is given.
- when a high score is wrong: when can a fairness score be high while the division is wrong? ::@:: When the flows want different amounts, so equal shares overfeed the light ones and starve the heavy ones.
- when demands differ: what decides the allocation then, and what becomes of the index? ::@:: A demand-based measure such as max-min fairness decides it, and the index is no more than a report on what came out.
- comparing allocations: when two index values are compared, what has to match? ::@:: The flows and their demands, since the index scores equality and not what each flow needs.

### equal demand

When the flows want the same bandwidth, the fair allocation is the equal one: the index is 1 for it and below 1 for every other. Three flows that each want 4 Mbps on a 10 Mbps link should each receive $10/3$ Mbps, scoring 1. The index agrees with the answer here, the case it was built for.

---

Flashcards for this section are as follows:

- equal demand: when is the equal share the fair allocation? ::@:: When every flow wants the same bandwidth, so any flow is as deserving as any other.
- equal demand numbers: three flows that each want $4\text{ Mbps}$ share a $10\text{ Mbps}$ link; what does each receive, and what does the index score that allocation? ::@:: $10/3\text{ Mbps}$ each, which are equal shares, so the index scores $1$.

### unequal demand

When the flows want different amounts, equal shares overfeed the flow that wants little and starve the flow that wants a lot, so the allocation that respects demand scores lower on the index. Three flows that want 8, 6 and 2 Mbps on a 10 Mbps link get 4, 4 and 2 Mbps under max-min fairness, since the flow wanting 2 Mbps takes all of it and the other two split the rest. That allocation scores $(4 + 4 + 2)^2/(3 \times (16 + 16 + 4)) = 100/108 \approx 0.93$, while the equal split of $10/3$ Mbps each scores 1 and starves the flow that wanted 8 Mbps.

A surgical robot sharing a link with downloads needs more than a quarter of it, so an equal split of four flows satisfies the index but starves the robot. The ranking is upside down: the split that ignores demand scores highest, so raising the index makes the allocation worse.

---

Flashcards for this section are as follows:

- unequal demand: three flows that want $8$, $6$ and $2\text{ Mbps}$ share a $10\text{ Mbps}$ link; what does max-min fairness give them, and what does the index score that allocation? ::@:: $4$, $4$ and $2\text{ Mbps}$, scoring $(4 + 4 + 2)^2/(3 \times (16 + 16 + 4)) = 100/108 \approx 0.93$.
- max-min step: three flows want $8$, $6$ and $2$ Mbps from a $10$ Mbps link; why does max-min fairness award the third flow only $2$ Mbps? ::@:: The flow that wants $2$ Mbps takes it, and the remaining $10 - 2 = 8$ Mbps splits as $8/2 = 4$ Mbps each.
- index prefers the equal split: three flows want $8$, $6$ and $2$ Mbps of a $10$ Mbps link; which allocation scores higher, the equal split or the max-min allocation? ::@:: The equal split of $10/3$ Mbps each scores $1$, against $100/108 \approx 0.93$ for max-min's $4$, $4$ and $2$ Mbps.
- what that ranking means: the equal split of three flows wanting $8$, $6$ and $2$ Mbps scores $1$ where the demand-respecting split scores $0.93$; what follows for using the index as a target? ::@:: The split that ignores demand scores highest, so raising the index would make the allocation worse and starve the flow that wants most.

### low scores from two causes

A low score has two causes and the index reports both as one number. Two flows on the same path with round trips of 10 ms and 50 ms settle at $5/6$ and $1/6$ of the link, scoring $36/52 \approx 0.69$. That division really is unfair, and congestion control at the ends cannot repair it.

An idle flow scores low for the other reason. Shares of 10 Mbps and 0 Mbps give $100/(2 \times 100) = 0.5$, and a third flow that also sent nothing drops the score to $100/300 \approx 0.33$. Nothing is unfair there: those flows wanted less than an equal share, so the score reports idle capacity as unfairness. Only the demand tells the two cases apart.

---

Flashcards for this section are as follows:

- round-trip unfairness: two flows share a link with round trips of $10\text{ ms}$ and $50\text{ ms}$; what fraction does each flow receive, and what does Jain's fairness index then report? ::@:: Shares in the inverse ratio of the round trips, $50 : 10 = 5 : 1$, so $5/6$ and $1/6$ of the link; the index is $(5/6 + 1/6)^2 / (2 \times (25/36 + 1/36)) = 36/52 \approx 0.69$, a shortfall rather than fairness.
- an idle flow: what does Jain's fairness index give for shares $10\text{ Mbps}$ and $0\text{ Mbps}$, and what does that show? ::@:: $(10 + 0)^2/(2 \times (100 + 0)) = 100/200 = 0.5$; the low score comes from a flow with nothing to send, not from an unfair division.
- a third idle flow: what does the index give for shares $10\text{ Mbps}$, $0\text{ Mbps}$, and $0\text{ Mbps}$? ::@:: $(10 + 0 + 0)^2/(3 \times (100 + 0 + 0)) = 100/300 \approx 0.33$, lower than the $0.5$ of the two-flow case.
- two causes, one number: which two situations give a low fairness score, and why does the score not separate them? ::@:: A division that really is unfair, and flows that wanted less than an equal share; both land in one number, so it has to be read against the demand.
