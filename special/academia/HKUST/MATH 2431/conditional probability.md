---
aliases:
  - conditional probabilities
  - conditional probability
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/conditional_probability
  - language/in/English
---

# conditional probability

Conditional probability reweights probabilities when we know that some event $B$ has occurred, while keeping the same sample space $\Omega$ and $\sigma$-algebra $\mathcal{F}$ and only changing the probability measure to the conditional one. It leads to the multiplication rule, the law of total probability, and Bayes' theorem, and provides the main language for "probability given information".

A concrete illustration is the two‑dice experiment. Set $\Omega = \{1,\dots,6\}^2$ with the uniform distribution $P[\{\omega\}] = 1/36$, and let $A = \{\text{sum} \le 7\}$ and $B = \{\text{at least one die shows }6\}$. Then $P[A] = 21/36 = 7/12$. After learning that $B$ occurs, we restrict the sample space to $B$; the only outcomes in $A \cap B$ are $(1,6)$ and $(6,1)$, so $P[A\mid B] = 2/11$. This is smaller than $P[A]$ because conditioning on $B$ makes the large‑sum outcomes more probable at the expense of small‑sum ones.

---

Flashcards for this section are as follows:

- overview / reweighting after conditioning on $B$ ::@:: Conditional probability $P[A\mid B]$ reweights probabilities when we know $B$ has occurred, keeping the same sample space $\Omega$ and $\sigma$-algebra $\mathcal{F}$ and only changing the measure to $P[\cdot\mid B]$; it leads to the multiplication rule, the law of total probability, and Bayes' theorem. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- two‑dice example / computing conditional probability by restricting to $B$ ::@:: For $\Omega = \{1,\dots,6\}^2$ uniform, $A = \{\text{sum} \le 7\}$, $B = \{\text{at least one }6\}$, the conditional probability is $P[A\mid B] = |A\cap B|/|B| = 2/11$, obtained by restricting the uniform measure to the reduced sample space $B$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## conditional probability: definition and multiplication rule

Let $(\Omega, \mathcal{F}, P)$ be a probability space and $B \in \mathcal{F}$ with $P[B] > 0$. Intuitively, $P[A\mid B]$ should describe how likely $A$ is once we know that $B$ has occurred; we should restrict attention to $B$ as the new sample space. Formally, the __conditional probability__ of $A$ given $B$ is $P[A\mid B] = P[A \cap B]/P[B]$ for every $A \in \mathcal{F}$. The condition $P[B]>0$ is essential in this elementary definition: when the conditioning event has probability $0$, the ratio is not defined and one needs more advanced notions than the present notes are using.

When $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$), this gives $P[A\mid B] = 0$ whenever it is defined. Rearranging the definition yields the __multiplication theorem__ (or product rule) $P[A \cap B] = P[B]\,P[A\mid B]$. This identity is useful because it turns a conditional statement back into an ordinary intersection probability, which can then be combined with disjoint decompositions and $\sigma$-additivity.

---

Flashcards for this section are as follows:

- definition / ratio $P[A\cap B]/P[B]$ ::@:: For $B \in \mathcal{F}$ with $P[B] > 0$, $P[A\mid B] = P[A \cap B]/P[B]$ for all $A \in \mathcal{F}$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- definition / why the conditioning event must satisfy $P[B]>0$ ::@:: In the elementary definition $P[A\mid B]=P[A\cap B]/P[B]$, the denominator must be positive; conditioning on a zero-probability event is not handled by this ratio formula. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- definition / mutually exclusive events with $A \cap B = \emptyset$ ::@:: If $A \cap B = \emptyset$ and $P[B] > 0$, then $P[A\mid B] = 0$; once we know $B$ occurs, $A$ is impossible (not just almost surely). <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- definition / multiplication theorem for $P[A \cap B]$ ::@:: From the definition, $P[A \cap B] = P[B]\,P[A\mid B]$; this is the multiplication theorem (product rule). <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- multiplication theorem / why it matters ::@:: The product rule rewrites a conditional probability as an ordinary intersection probability, so it becomes the bridge between "given that" statements and algebraic manipulations of events. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## conditional probability as a probability measure

Fix $B \in \mathcal{F}$ with $P[B] > 0$ and define $P_B[A] = P[A\mid B]$ for $A \in \mathcal{F}$. Then $P_B$ is itself a probability measure on the __same__ measurable space $(\Omega, \mathcal{F})$: first $0 \le P[A \cap B] \le P[B]$ implies $0 \le P[A\mid B] \le 1$; next $P[\Omega\mid B] = P[\Omega \cap B]/P[B] = P[B]/P[B] = 1$; finally, for pairwise disjoint $(A_j)_{j\in\mathbb{N}}$, the sets $A_j \cap B$ are pairwise disjoint and $P[\bigcup_{j=1}^{\infty} A_j \mid B] = P[\bigcup_j (A_j \cap B)]/P[B] = \sum_j P[A_j \cap B]/P[B] = \sum_j P[A_j\mid B]$, showing $\sigma$-additivity.

---

Flashcards for this section are as follows:

- why $P[\cdot\mid B]$ is itself a probability measure ::@:: For fixed $B$ with $P[B]>0$, $P[\cdot\mid B]$ is a probability measure on the same $(\Omega,\mathcal{F})$ as $P$: it has values in $[0,1]$, satisfies $P[\Omega\mid B]=1$, and is $\sigma$-additive on $\mathcal{F}$. <!--SR:!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-08T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-08T00:00:00.000Z-->
- conditional measure / nonnegativity and range ::@:: Nonnegativity and the range $0 \le P[A\mid B] \le 1$ follow from $0 \le P[A \cap B] \le P[B]$ and the definition $P[A\mid B] = P[A\cap B]/P[B]$ when $P[B]>0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-13T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-04-24T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- conditional measure / normalization ::@:: Normalization holds because $P[\Omega\mid B] = P[\Omega \cap B]/P[B] = P[B]/P[B] = 1$, so the conditional measure assigns total mass $1$ to $\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-29T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-04-29T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- conditional measure / sigma-additivity ::@:: For pairwise disjoint $(A_j)$, the sets $A_j \cap B$ are disjoint and $\bigcup_j (A_j \cap B) = (\bigcup_j A_j)\cap B$, so $\sigma$-additivity of $P$ gives $P[\bigcup_j A_j\mid B] = \sum_j P[A_j\mid B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-12T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-04-13T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- conditioning changes the measure, not the measurable space ::@:: The conditional measure $P_B[A]=P[A\mid B]$ is defined on the same $\sigma$-algebra $\mathcal{F}$ over the same sample space $\Omega$; only the weights assigned to events change when we condition on $B$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z!2026-07-22,67,310-->

## law of total probability and Bayes' theorem

Let $B_1,\ldots,B_n \in \mathcal{F}$ with $P[B_j] > 0$ for all $j$, such that $B_j \cap B_k = \emptyset$ for $j \neq k$ and $\bigcup_{j=1}^n B_j = \Omega$. In this situation we say that $(B_j)_{j=1}^n$ is a __finite partition__ of $\Omega$: every outcome $\omega \in \Omega$ lies in exactly one of the sets $B_j$, so the events are disjoint and cover the whole space. For any $A \in \mathcal{F}$ we then have the __law of total probability__ $P[A] = \sum_{j=1}^n P[B_j]\,P[A\mid B_j]$, obtained by expanding $A$ as a disjoint union $A = \bigcup_{j=1}^n (A \cap B_j)$ and using $\sigma$-additivity together with the multiplication rule $P[A \cap B_j] = P[B_j] P[A\mid B_j]$ for each $j$. Combining the law of total probability with the definition of conditional probability yields __Bayes' theorem__: assuming $P[A]>0$ and $P[B_k]>0$, we obtain $P[B_k\mid A] = \dfrac{P[B_k]\,P[A\mid B_k]}{\sum_{j=1}^n P[B_j]\,P[A\mid B_j]}$ for each $k$. The same formulas hold for countable partitions $(B_j)_{j\in\mathbb{N}}$ with $P[B_j]>0$, with sums extended to $j\in\mathbb{N}$.

Bayes' theorem is best read as a rescaling rule. The factor $P[B_k]$ is the prior weight of hypothesis $B_k$, the factor $P[A\mid B_k]$ measures how compatible the observed evidence $A$ is with that hypothesis, and the denominator is the total probability of seeing $A$ at all. So Bayes' theorem does not invent information; it rebalances the hypotheses after the evidence has been observed.

---

Flashcards for this section are as follows:

- finite partition of $\Omega$ used in total probability and Bayes ::@:: A family $(B_j)_{j=1}^n$ is a partition of $\Omega$ if the $B_j$ are pairwise disjoint, each has $P[B_j]>0$, and $\bigcup_{j=1}^n B_j = \Omega$, so every outcome lies in exactly one $B_j$. <!--SR:!fsrs,2027-04-18T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-09T00:00:00.000Z!2026-08-03,61,310-->
- law of total probability from a partition of hypotheses ::@:: If $(B_j)_{j=1}^n$ is a partition of $\Omega$ with $P[B_j]>0$, then for any $A \in \mathcal{F}$ we have $P[A] = \sum_{j=1}^n P[B_j]\,P[A\mid B_j]$, obtained by writing $A = \bigcup_j (A \cap B_j)$ as a disjoint union and using $\sigma$-additivity plus the multiplication rule. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-08T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- Bayes' theorem for a finite partition of hypotheses ::@:: Under the same assumptions and $P[A]>0$, Bayes' theorem reads $P[B_k\mid A] = \dfrac{P[B_k]\,P[A\mid B_k]}{\sum_{j=1}^n P[B_j]\,P[A\mid B_j]}$, i.e. posterior = prior $\times$ likelihood divided by the total evidence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-24T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-11T00:00:00.000Z!2026-07-19,63,310-->
- Bayes' theorem / prior probability of the hypothesis $B_k$ ::@:: Denote $A$ to be an evidence and $B_k$ a hypothesis. In Bayes' theorem, $P[B_k]$ is the prior probability of hypothesis $B_k$, meaning its probability before the evidence $A$ is observed. <!--SR:!fsrs,2027-04-08T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- Bayes' theorem / likelihood of the evidence under $B_k$ ::@:: Denote $A$ to be an evidence and $B_k$ a hypothesis. In Bayes' theorem, $P[A\mid B_k]$ is the likelihood: it measures how compatible the observed evidence $A$ is with the hypothesis $B_k$. <!--SR:!fsrs,2027-05-11T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-15T00:00:00.000Z!fsrs,2027-04-08T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-08T00:00:00.000Z-->
- Bayes' theorem / posterior probability after observing $A$ ::@:: Denote $A$ to be an evidence and $B_k$ a hypothesis. In Bayes' theorem, $P[B_k\mid A]$ is the posterior probability: the updated probability of hypothesis $B_k$ after the evidence $A$ has been taken into account. <!--SR:!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- Bayes' theorem / why the denominator equals total evidence probability ::@:: In Bayes' theorem, the denominator $\sum_j P[B_j]P[A\mid B_j]$ is exactly $P[A]$ from the law of total probability, so it normalizes the reweighted hypotheses into genuine posterior probabilities. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-08-06,64,310!2026-07-15,61,310-->
- law of total probability and Bayes for a countable partition ::@:: For a countable partition $(B_j)_{j\in\mathbb{N}}$ with $P[B_j]>0$, the same derivation yields $P[A] = \sum_{j=1}^{\infty} P[B_j]\,P[A\mid B_j]$ and Bayes' theorem with the denominator replaced by an infinite sum over $j\in\mathbb{N}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z!2026-07-22,67,310-->
- LOTP derivation / expanding $A$ through a partition ::@:: $P[A] = P[A \cap \Omega] = P[A \cap \bigcup_{j=1}^n B_j] = P[\bigcup_{j=1}^n (A\cap B_j)] = \sum_{j=1}^n P[A\cap B_j] = \sum_{j=1}^n P[B_j]P[A\mid B_j]$, using disjointness and the multiplication rule. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Bayes derivation / from definition and LOTP ::@:: $P[B_k\mid A] = P[B_k \cap A]/P[A] = P[B_k]P[A\mid B_k] / \sum_{j=1}^n P[B_j]P[A\mid B_j]$, combining the definition of conditional probability and the law of total probability in the denominator. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### diagnostic test for rare disease

Consider a medical test for a marker (or disease) in a population. Let $T$ be the event "test is positive" and $M$ the event "individual has the marker". Suppose the test has sensitivity $P[T\mid M] = 0.99$, specificity $P[T^c\mid M^c] = 0.99$ so that $P[T\mid M^c] = 0.01$, and the prevalence is $P[M] = 0.01$. Bayes' theorem gives $P[M\mid T] = \dfrac{P[T\mid M] P[M]}{P[T\mid M] P[M] + P[T\mid M^c] P[M^c]} = \dfrac{0.99 \cdot 0.01}{0.99 \cdot 0.01 + 0.01 \cdot 0.99} = \tfrac{1}{2}$: even with a highly accurate test, a positive result only implies a $50\%$ chance of actually having the marker when the condition is rare.

The key lesson is the base-rate effect. The test is highly accurate, but the healthy population is so much larger than the diseased population that false positives from the healthy group still contribute substantially to the event $T$. Bayes' theorem forces both true positives and false positives into the denominator, which is why the posterior probability is much lower than a naive "the test is $99\%$ accurate, so the diagnosis is $99\%$ reliable" intuition.

---

Flashcards for this section are as follows:

- diagnostic-test example / sensitivity and specificity ::@:: Sensitivity $P[T\mid M]$ is the probability the test is positive given the marker; specificity $P[T^c\mid M^c]$ is the probability the test is negative given no marker. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-12-27T00:00:00.000Z,172,171.53328362,3.24197837,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-04-13T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- diagnostic-test example / prevalence effect on the posterior ::@:: With $P[T\mid M]=0.99$, $P[T^c\mid M^c]=0.99$, and prevalence $P[M]=0.01$, Bayes' theorem gives $P[M\mid T] = \tfrac{1}{2}$; rare conditions can make even accurate tests yield many false positives. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-13T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-04-29T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- diagnostic-test example / why the posterior is only $1/2$ ::@:: The denominator counts both true positives and false positives. Here the diseased group is tiny, so the false positives coming from the much larger healthy group are numerous enough to reduce the posterior probability of disease to $1/2$ despite the test's $99\%$ sensitivity and specificity. <!--SR:!2026-08-09,67,310!fsrs,2027-04-19T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-10T00:00:00.000Z-->

## stochastic independence

Two events $A,B \in \mathcal{F}$ should be independent if the occurrence of $A$ does not influence the probability of $B$, and vice versa. Formally, if $P[B]>0$ then $P[A\mid B]=P[A]$ means that $B$ carries no information about $A$; multiplying by $P[B]$ gives the symmetric condition $P[A \cap B] = P[A]\,P[B]$, which also works when $P[B]=0$.

__Joint (stochastic) independence.__ Let $I$ be a set. A family $(A_i)_{i\in I} \subseteq \mathcal{F}$ is called (jointly) independent if for every finite subfamily $\{i_1,\dots,i_m\} \subseteq I$ with pairwise distinct indices, $$P[A_{i_1} \cap \cdots \cap A_{i_m}] = P[A_{i_1}] \cdots P[A_{i_m}].$$ In particular, two events $A,B \in \mathcal{F}$ are independent iff $P[A \cap B] = P[A]\,P[B]$.

__Remarks.__

- The definition covers the case when an event has probability $0$; if $P[A]>0$ and $P[B]>0$, independence is equivalent to $P[A] = P[A\mid B]$ (and $P[B] = P[B\mid A]$).
- $\emptyset$ and $\Omega$ are independent of every event, because $P[\emptyset \cap A] = 0 = P[\emptyset]P[A]$ and $P[\Omega \cap A] = P[A] = P[\Omega]P[A]$.
- Independence is not the same as disjointness. If $A \cap B = \emptyset$ with $A,B$ independent, then $0 = P[A \cap B] = P[A]P[B]$ forces $P[A]=0$ or $P[B]=0$; disjoint non‑null events are always dependent.
- For more than two events, pairwise independence does __not__ imply joint independence; it is possible that every pair factors while the triple intersection does not.

---

Flashcards for this section are as follows:

- independence motivation / when does $B$ give no info about $A$ ::@:: If $P[B]>0$, then $B$ carries no information about $A$ precisely when $P[A\mid B]=P[A]$, which is symmetric and equivalent to $P[A \cap B] = P[A]P[B]$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- definition / two events are independent ::@:: $A,B \in \mathcal{F}$ are (stochastically) independent iff $P[A \cap B] = P[A]\,P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- definition / joint (mutual) independence for a family $(A_i)_{i\in I}$ ::@:: The family is jointly independent if for every finite subfamily $\{i_1,\dots,i_m\}$ with distinct indices, $P[A_{i_1} \cap \cdots \cap A_{i_m}] = P[A_{i_1}] \cdots P[A_{i_m}]$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- independence vs disjointness ::@:: Disjoint events with positive probability are never independent, because $0 = P[A\cap B] \neq P[A]P[B] > 0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- zero‑probability and sure events are independent of everything ::@:: $\emptyset$ and $\Omega$ are independent of any $A \in \mathcal{F}$, since $P[\emptyset \cap A] = 0 = P[\emptyset]P[A]$ and $P[\Omega \cap A] = P[A] = P[\Omega]P[A]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- pairwise independence does not imply joint independence ::@:: It is possible for every pair in a family to satisfy the product condition while the entire family does not; joint independence requires the product to hold for __every__ finite subfamily. <!--SR:!fsrs,2026-09-28T00:00:00.000Z,76,75.34793403,1,2,3,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-08-27T00:00:00.000Z,44,44.09694232,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### card‑deck

Draw a card uniformly from a standard $52$-card deck. Let $A$ be "the card is a $\heartsuit$" and $B$ be "the card is an ace". Then $P[A] = 13/52 = 1/4$, $P[B] = 4/52 = 1/13$, and $P[A \cap B] = 1/52 = P[A]\,P[B]$, so $A$ and $B$ are independent: knowing the suit gives no information about whether it is an ace.

---

Flashcards for this section are as follows:

- card‑deck / $P[\heartsuit]=1/4$, $P[\text{ace}]=1/13$, check independence ::@:: $P[\heartsuit \cap \text{ace}] = 1/52 = (1/4)(1/13) = P[\heartsuit]P[\text{ace}]$, so knowing the card is a heart does not change the probability that it is an ace. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### coin‑toss

Toss a fair coin twice, with $\Omega = \{HH, HT, TH, TT\}$ uniform. Define $A = \{\text{first toss heads}\}$, $B = \{\text{second toss heads}\}$, $C = \{\text{exactly one head}\}$. Each has probability $1/2$. All pairwise intersections have probability $1/4$, so $(A,B)$, $(A,C)$, and $(B,C)$ are pairwise independent. But $A \cap B \cap C = \emptyset$, so $P[A \cap B \cap C] = 0 \neq 1/8 = P[A]P[B]P[C]$, showing that pairwise independence does __not__ imply joint independence.

---

Flashcards for this section are as follows:

- coin‑toss / $A=\{\text{first }H\}$, $B=\{\text{second }H\}$, $C=\{\text{exactly one }H\}$: joint independence? ::@:: $A,B,C$ are pairwise independent ($P[A\cap B]=1/4 = P[A]P[B]$, etc.) but not jointly independent because $P[A\cap B\cap C]=0 \neq 1/8$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coin‑toss counter‑example (A=first H, B=second H, C=exactly one H) / pairwise vs joint independence distinction ::@:: Pairwise independence only checks factorisation for pairs; joint independence demands factorisation for all finite subfamilies, which is strictly stronger. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coin‑toss counter‑example (A=first H, B=second H, C=exactly one H) / sample space ::@:: $\Omega = \{HH, HT, TH, TT\}$ uniform; $A = \{\text{first}=H\} = \{HH, HT\}$, $B = \{\text{second}=H\} = \{HH, TH\}$, $C = \{\text{exactly one }H\} = \{HT, TH\}$. Each $P[A]=P[B]=P[C]=1/2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coin‑toss counter‑example (A=first H, B=second H, C=exactly one H) / why A and B are pairwise independent ::@:: $A\cap B = \{HH\} \to P[A\cap B] = 1/4 = (1/2)(1/2) = P[A]P[B]$, so $A$, $B$ are independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coin‑toss counter‑example (A=first H, B=second H, C=exactly one H) / why A,C and B,C are pairwise independent ::@:: $A\cap C = \{HT\} \to P[A\cap C]=1/4 = P[A]P[C]$; $B\cap C = \{TH\} \to P[B\cap C]=1/4 = P[B]P[C]$. So $(A,C)$ and $(B,C)$ are also pairwise independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coin‑toss counter‑example (A=first H, B=second H, C=exactly one H) / why A,B,C are not jointly independent ::@:: $A\cap B\cap C = \emptyset \to P[A\cap B\cap C] = 0 \neq 1/8 = P[A]P[B]P[C]$, showing joint independence fails despite full pairwise independence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### independence and complements

If $A_1,\dots,A_n \in \mathcal{F}$ are jointly independent, then also $B_1,\dots,B_n$ with $B_i \in \{A_i, A_i^{\,c}\}$ for $1 \le i \le n$ are jointly independent.

_Proof for $n=2$._ Let $B_1 = A_1$ and $B_2 = A_2^{\,c}$. Since $(A_1 \cap A_2)$ and $(A_1 \cap A_2^{\,c})$ are disjoint and their union is $A_1$, we have $$P[A_1] = P[A_1 \cap A_2] + P[A_1 \cap A_2^{\,c}] = P[A_1]P[A_2] + P[A_1 \cap A_2^{\,c}].$$ Thus $P[A_1 \cap A_2^{\,c}] = P[A_1] - P[A_1]P[A_2] = P[A_1](1-P[A_2]) = P[A_1]P[A_2^{\,c}]$, which is the product condition for $(A_1, A_2^{\,c})$. The case $(A_1^{\,c}, A_2)$ is symmetric, and applying the same argument to $A_1^{\,c}$ and $A_2$ gives the condition for $(A_1^{\,c}, A_2^{\,c})$. The general $n$ case follows by induction.

---

Flashcards for this section are as follows:

- complements theorem / independent events remain independent when you complement any subset ::@:: If $A_1,\dots,A_n$ are jointly independent, then for any choice $B_i \in \{A_i, A_i^{\,c}\}$, the family $(B_i)_{i=1}^n$ is also jointly independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- complements theorem proof for two events / key trick ::@:: Write $P[A_1 \cap A_2^{\,c}] = P[A_1] - P[A_1 \cap A_2] = P[A_1] - P[A_1]P[A_2] = P[A_1]P[A_2^{\,c}]$, using disjointness of $A_1\cap A_2$ and $A_1\cap A_2^{\,c}$ plus joint independence of $(A_1,A_2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
