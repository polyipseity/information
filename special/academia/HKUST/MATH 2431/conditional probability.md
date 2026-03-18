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

---

Flashcards for this section are as follows:

- overview ::@:: Conditional probability $P[A\mid B]$ reweights probabilities when we know $B$ has occurred, keeping the same sample space $\Omega$ and $\sigma$-algebra $\mathcal{F}$ and only changing the measure to $P[\cdot\mid B]$; it leads to the multiplication rule, the law of total probability, and Bayes' theorem. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## conditional probability: definition and multiplication rule

Let $(\Omega, \mathcal{F}, P)$ be a probability space and $B \in \mathcal{F}$ with $P[B] > 0$. Intuitively, $P[A\mid B]$ should describe how likely $A$ is once we know that $B$ has occurred; we should restrict attention to $B$ as the new sample space. Formally, the **conditional probability** of $A$ given $B$ is $P[A\mid B] = P[A \cap B]/P[B]$ for every $A \in \mathcal{F}$. When $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$), this gives $P[A\mid B] = 0$ whenever it is defined. Rearranging the definition yields the **multiplication theorem** (or product rule) $P[A \cap B] = P[B]\,P[A\mid B]$.

---

Flashcards for this section are as follows:

- definition ::@:: For $B \in \mathcal{F}$ with $P[B] > 0$, $P[A\mid B] = P[A \cap B]/P[B]$ for all $A \in \mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- mutually exclusive ::@:: If $A \cap B = \emptyset$ and $P[B] > 0$, then $P[A\mid B] = 0$; once we know $B$ occurs, $A$ is impossible. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- multiplication theorem ::@:: From the definition, $P[A \cap B] = P[B]\,P[A\mid B]$; this is the multiplication theorem (product rule). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## conditional probability as a probability measure

Fix $B \in \mathcal{F}$ with $P[B] > 0$ and define $P_B[A] = P[A\mid B]$ for $A \in \mathcal{F}$. Then $P_B$ is itself a probability measure on the **same** measurable space $(\Omega, \mathcal{F})$: first $0 \le P[A \cap B] \le P[B]$ implies $0 \le P[A\mid B] \le 1$; next $P[\Omega\mid B] = P[\Omega \cap B]/P[B] = P[B]/P[B] = 1$; finally, for pairwise disjoint $(A_j)_{j\in\mathbb{N}}$, the sets $A_j \cap B$ are pairwise disjoint and $P[\bigcup_{j=1}^{\infty} A_j \mid B] = P[\bigcup_j (A_j \cap B)]/P[B] = \sum_j P[A_j \cap B]/P[B] = \sum_j P[A_j\mid B]$, showing $\sigma$-additivity.

---

Flashcards for this section are as follows:

- $P[\cdot\mid B]$ is measure ::@:: For fixed $B$ with $P[B]>0$, $P[\cdot\mid B]$ is a probability measure on the same $(\Omega,\mathcal{F})$ as $P$: it has values in $[0,1]$, satisfies $P[\Omega\mid B]=1$, and is $\sigma$-additive on $\mathcal{F}$.
- nonnegativity and range ::@:: Nonnegativity and the range $0 \le P[A\mid B] \le 1$ follow from $0 \le P[A \cap B] \le P[B]$ and the definition $P[A\mid B] = P[A\cap B]/P[B]$ when $P[B]>0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- normalization of P(.|B) ::@:: Normalization holds because $P[\Omega\mid B] = P[\Omega \cap B]/P[B] = P[B]/P[B] = 1$, so the conditional measure assigns total mass $1$ to $\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-additivity of P(.|B) ::@:: For pairwise disjoint $(A_j)$, the sets $A_j \cap B$ are disjoint and $\bigcup_j (A_j \cap B) = (\bigcup_j A_j)\cap B$, so $\sigma$-additivity of $P$ gives $P[\bigcup_j A_j\mid B] = \sum_j P[A_j\mid B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same measurable space ::@:: The conditional measure $P_B[A]=P[A\mid B]$ is defined on the same $\sigma$-algebra $\mathcal{F}$ over the same sample space $\Omega$; only the weights assigned to events change when we condition on $B$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## law of total probability and Bayes' theorem

Let $B_1,\ldots,B_n \in \mathcal{F}$ with $P[B_j] > 0$ for all $j$, such that $B_j \cap B_k = \emptyset$ for $j \neq k$ and $\bigcup_{j=1}^n B_j = \Omega$. In this situation we say that $(B_j)_{j=1}^n$ is a **finite partition** of $\Omega$: every outcome $\omega \in \Omega$ lies in exactly one of the sets $B_j$, so the events are disjoint and cover the whole space. For any $A \in \mathcal{F}$ we then have the **law of total probability** $P[A] = \sum_{j=1}^n P[B_j]\,P[A\mid B_j]$, obtained by expanding $A$ as a disjoint union $A = \bigcup_{j=1}^n (A \cap B_j)$ and using $\sigma$-additivity together with the multiplication rule $P[A \cap B_j] = P[B_j] P[A\mid B_j]$ for each $j$. Combining the law of total probability with the definition of conditional probability yields **Bayes' theorem**: assuming $P[A]>0$ and $P[B_k]>0$, we obtain $P[B_k\mid A] = \dfrac{P[B_k]\,P[A\mid B_k]}{\sum_{j=1}^n P[B_j]\,P[A\mid B_j]}$ for each $k$. The same formulas hold for countable partitions $(B_j)_{j\in\mathbb{N}}$ with $P[B_j]>0$, with sums extended to $j\in\mathbb{N}$.

---

Flashcards for this section are as follows:

- partition of Omega ::@:: A family $(B_j)_{j=1}^n$ is a partition of $\Omega$ if the $B_j$ are pairwise disjoint, each has $P[B_j]>0$, and $\bigcup_{j=1}^n B_j = \Omega$, so every outcome lies in exactly one $B_j$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- law of total probability ::@:: If $(B_j)_{j=1}^n$ is a partition of $\Omega$ with $P[B_j]>0$, then for any $A \in \mathcal{F}$ we have $P[A] = \sum_{j=1}^n P[B_j]\,P[A\mid B_j]$, obtained by writing $A = \bigcup_j (A \cap B_j)$ as a disjoint union and using $\sigma$-additivity plus the multiplication rule. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Bayes theorem finite ::@:: Under the same assumptions and $P[A]>0$, Bayes' theorem reads $P[B_k\mid A] = \dfrac{P[B_k]\,P[A\mid B_k]}{\sum_{j=1}^n P[B_j]\,P[A\mid B_j]}$, i.e. posterior = prior $\times$ likelihood divided by the total evidence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- total probability countable ::@:: For a countable partition $(B_j)_{j\in\mathbb{N}}$ with $P[B_j]>0$, the same derivation yields $P[A] = \sum_{j=1}^{\infty} P[B_j]\,P[A\mid B_j]$ and Bayes' theorem with the denominator replaced by an infinite sum over $j\in\mathbb{N}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### diagnostic test for rare disease

Consider a medical test for a marker (or disease) in a population. Let $T$ be the event "test is positive" and $M$ the event "individual has the marker". Suppose the test has sensitivity $P[T\mid M] = 0.99$, specificity $P[T^c\mid M^c] = 0.99$ so that $P[T\mid M^c] = 0.01$, and the prevalence is $P[M] = 0.01$. Bayes' theorem gives $P[M\mid T] = \dfrac{P[T\mid M] P[M]}{P[T\mid M] P[M] + P[T\mid M^c] P[M^c]} = \dfrac{0.99 \cdot 0.01}{0.99 \cdot 0.01 + 0.01 \cdot 0.99} = \tfrac{1}{2}$: even with a highly accurate test, a positive result only implies a $50\%$ chance of actually having the marker when the condition is rare.

---

Flashcards for this section are as follows:

- test sensitivity and specificity ::@:: Sensitivity $P[T\mid M]$ is the probability the test is positive given the marker; specificity $P[T^c\mid M^c]$ is the probability the test is negative given no marker. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- test prevalence effect ::@:: With $P[T\mid M]=0.99$, $P[T^c\mid M^c]=0.99$, and prevalence $P[M]=0.01$, Bayes' theorem gives $P[M\mid T] = \tfrac{1}{2}$; rare conditions can make even accurate tests yield many false positives. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
