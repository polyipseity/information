---
aliases:
  - Kolmogorov axioms
  - probability measure
  - probability measures
  - probability space
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/probability_measure
  - language/in/English
---

# probability measure

A probability measure assigns to each event a number in $[0,1]$ in a way that respects normalization and countable additivity. Together with a sample space $\Omega$ and a $\sigma$-algebra $\mathcal{F}$, it forms a _probability space_ $(\Omega, \mathcal{F}, P)$, the standard mathematical model for a random experiment.

## definition and Kolmogorov axioms

Let $\Omega \neq \emptyset$ and $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ a $\sigma$-algebra. A _probability measure_ (or _probability_) is a function $P \colon \mathcal{F} \to [0,1]$ satisfying: (P1) $P[\Omega] = 1$ (normalization); (P2) if $(A_j)_{j \in \mathbb{N}}$ is a sequence of pairwise disjoint events ($A_j \cap A_k = \emptyset$ for $j \neq k$), then $P\big[\bigcup_{j=1}^{\infty} A_j\big] = \sum_{j=1}^{\infty} P[A_j]$ ($\sigma$-additivity). The triple $(\Omega, \mathcal{F}, P)$ is called a _probability space_.

---

Flashcards for this section are as follows:

- definition (P1) ::@:: $P[\Omega] = 1$ (normalization). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- definition (P2) ::@:: For pairwise disjoint $A_j \in \mathcal{F}$, $P[\bigcup_{j=1}^{\infty} A_j] = \sum_{j=1}^{\infty} P[A_j]$ ($\sigma$-additivity). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- probability space ::@:: The triple $(\Omega, \mathcal{F}, P)$: sample space, $\sigma$-algebra of events, and probability measure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pairwise disjoint ::@:: Events $A_j$ are pairwise disjoint if $A_j \cap A_k = \emptyset$ for $j \neq k$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## uniform distribution and Laplace space

When $\Omega$ is finite and $\mathcal{F} = \mathcal{P}(\Omega)$, the _uniform distribution_ (or _discrete uniform_) is given by $P[A] = |A|/|\Omega|$ for all $A \subseteq \Omega$. Then $P[\{\omega\}] = 1/|\Omega|$ for every outcome $\omega$; every outcome is equally likely. The resulting space $(\Omega, \mathcal{P}(\Omega), P)$ is sometimes called a _Laplace probability space_. As a concrete illustration, consider two independent rolls of a fair die: $\Omega = \{1,\ldots,6\}^2$, $\mathcal{F} = \mathcal{P}(\Omega)$, $|\Omega| = 36$, and $P[A] = |A|/36$ for all events $A \subseteq \Omega$. The event $B = \{\text{at least one 6}\}$ consists of outcomes $(1,6), (2,6), \ldots, (6,6), (6,5), \ldots, (6,1)$; $|B| = 11$, so $P[B] = 11/36$.

---

Flashcards for this section are as follows:

- uniform on finite Omega ::@:: $P[A] = |A|/|\Omega|$ for $A \subseteq \Omega$; each outcome has probability $1/|\Omega|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Laplace space ::@:: Probability space with finite $\Omega$, $\mathcal{F} = \mathcal{P}(\Omega)$, and uniform $P$; "equally likely outcomes". <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- die twice sample space ::@:: For two independent rolls of a fair die, $\Omega = \{1,\ldots,6\}^2$, $|\Omega| = 36$, and $P[A] = |A|/36$ under the uniform distribution. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- at least one 6 in two rolls ::@:: In the two-roll die experiment, the event $B$ ("at least one 6") has 11 outcomes, so $P[B] = 11/36$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## elementary properties

### algebraic properties

Let $(\Omega, \mathcal{F}, P)$ be a probability space and $A, B \in \mathcal{F}$. (i) $P[\emptyset] = 0$. (ii) $P[A^c] = 1 - P[A]$. (iii) If $A \subseteq B$ then $P[A] \le P[B]$. (iv) $P[A \cup B] = P[A] + P[B] - P[A \cap B]$. (v) For arbitrary events $(A_j)_{j \in \mathbb{N}}$, $P[\bigcup_{j=1}^{\infty} A_j] \le \sum_{j=1}^{\infty} P[A_j]$ (subadditivity).

Proof of (i): $\emptyset = \emptyset \cup \emptyset \cup \cdots$ and $\sigma$-additivity give $P[\emptyset] = \sum P[\emptyset]$, so $P[\emptyset] = 0$.

Proof of (ii): $A \cup A^c = \Omega$, $A \cap A^c = \emptyset$, so $1 = P[\Omega] = P[A] + P[A^c]$.

For (iii), write $B$ as the disjoint union $B = A \cup (B \setminus A)$, so $P[B] = P[A] + P[B \setminus A]$ with $P[B \setminus A] \ge 0$, hence $P[B] \ge P[A]$.

For (iv), decompose $B$ into the disjoint union of the intersection and the part outside $A$: $B = (A \cap B) \cup (B \setminus A)$ with $B \setminus A = B \setminus (A \cap B)$. Then $A \cup B = A \cup (B \setminus A)$ is a disjoint union, so by $\sigma$-additivity (in the finite case just additivity) we have $P[A \cup B] = P[A] + P[B \setminus A]$, while from (iii) and the same disjoint-union argument we have $P[B] = P[A \cap B] + P[B \setminus A]$; solving these two equations for $P[A \cup B]$ eliminates $P[B \setminus A]$ and gives $P[A \cup B] = P[A] + P[B] - P[A \cap B]$.

For (v), define disjoint sets by $B_1 = A_1$ and $B_n = A_n \setminus \bigcup_{j=1}^{n-1} A_j$ for $n \ge 2$; by construction the $B_n$ are pairwise disjoint and each point that lies in some $A_j$ lies in exactly one $B_n$, so $\bigcup_{j=1}^{\infty} A_j = \bigcup_{j=1}^{\infty} B_j$. Moreover $B_j \subseteq A_j$ for every $j$, hence $P[B_j] \le P[A_j]$. Using $\sigma$-additivity on the disjoint family $(B_j)$ now yields $P\big[\bigcup_{j=1}^{\infty} A_j\big] = P\big[\bigcup_{j=1}^{\infty} B_j\big] = \sum_{j=1}^{\infty} P[B_j] \le \sum_{j=1}^{\infty} P[A_j]$, which is the desired subadditivity.

---

Flashcards for this section are as follows:

- P empty is 0 ::@:: $P[\emptyset] = 0$ (from $\sigma$-additivity: $P[\emptyset] = P[\emptyset \cup \emptyset \cup \cdots] = \sum P[\emptyset]$). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complement rule ::@:: $P[A^c] = 1 - P[A]$ (since $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- monotonicity ::@:: If $A \subseteq B$ then $P[A] \le P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- monotonicity proof ::@:: From $A \subseteq B$ we write $B = A \cup (B \setminus A)$ as a disjoint union, so $P[B] = P[A] + P[B \setminus A] \ge P[A]$, hence $P[A] \le P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inclusion-exclusion two sets ::@:: $P[A \cup B] = P[A] + P[B] - P[A \cap B]$, proved by writing $B = (A \cap B) \cup (B \setminus A)$ as a disjoint union, using additivity on $A \cup (B \setminus A)$ and on $(A \cap B) \cup (B \setminus A)$, and eliminating $P[B \setminus A]$ between the two equations. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- subadditivity ::@:: For $A_j \in \mathcal{F}$ define disjoint $B_1=A_1$, $B_n = A_n \setminus \bigcup_{j=1}^{n-1} A_j$; then the $B_j$ are pairwise disjoint, $\bigcup_j A_j = \bigcup_j B_j$, and $B_j \subseteq A_j$, so $\sigma$-additivity gives $P[\bigcup_j A_j] = \sum_j P[B_j] \le \sum_j P[A_j]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- intuition for proofs ::@:: In general, the important axiom is $\sigma$-additivity. That means you should try to construct a disjoint family of sets to which you can apply $\sigma$-additivity, and then use the resulting equation(s) to solve for the desired quantity. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### limit properties (continuity)

With the same probability space $(\Omega, \mathcal{F}, P)$ and events $A_j \in \mathcal{F}$, one says that $(A_n)$ is an _increasing sequence of events_ if $A_1 \subseteq A_2 \subseteq \cdots$, and a _decreasing sequence of events_ if $A_1 \supseteq A_2 \supseteq \cdots$. For such sequences, (vi) if $A_1 \subseteq A_2 \subseteq \cdots$, then $P[\bigcup_{j=1}^{\infty} A_j] = \lim_{n \to \infty} P[A_n]$ (continuity from below). (vii) If $A_1 \supseteq A_2 \supseteq \cdots$, then $P[\bigcap_{j=1}^{\infty} A_j] = \lim_{n \to \infty} P[A_n]$ (continuity from above).

---

Flashcards for this section are as follows:

- continuity from below ::@:: If $A_1 \subseteq A_2 \subseteq \cdots$ then $P[\bigcup_j A_j] = \lim_{n \to \infty} P[A_n]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuity from above ::@:: If $A_1 \supseteq A_2 \supseteq \cdots$ then $P[\bigcap_j A_j] = \lim_{n \to \infty} P[A_n]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- increasing sequence of events ::@:: A sequence $(A_n)$ is increasing if $A_1\subseteq A_2\subseteq\cdots$; then its natural limit event is $\bigcup_{n=1}^{\infty}A_n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- decreasing sequence of events ::@:: A sequence $(A_n)$ is decreasing if $A_1\supseteq A_2\supseteq\cdots$; then its natural limit event is $\bigcap_{n=1}^{\infty}A_n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
