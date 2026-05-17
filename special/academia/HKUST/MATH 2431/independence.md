---
aliases:
  - independence
  - independent events
  - stochastic independence
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/independence
  - language/in/English
---

# independence

Stochastic independence formalises the idea that the occurrence of one event does not change the probability of another. It is defined by a factorisation identity for probabilities and extends from pairs of events to families.

---

Flashcards for this section are as follows:

- overview of stochastic independence ::@:: Independence expresses that $P[A\cap B]$ factors as $P[A]P[B]$ and, more generally, that finite intersections of events have probability equal to the product of their individual probabilities. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-19,67,310!2026-07-19,67,310-->

## definitions: pairwise and joint independence

Heuristically, two events $A,B \in \mathcal{F}$ should be independent if knowing that one occurs does not change the probability of the other: we would like $P[A] = P[A\mid B] = P[A\mid B^c]$ and $P[B] = P[B\mid A] = P[B\mid A^c]$ whenever these are defined. Using the multiplication theorem, this leads to the formal definition: $A$ and $B$ are (stochastically) __independent__ if $P[A \cap B] = P[A]\,P[B]$. When $P[A]>0$ and $P[B]>0$, this factorisation condition and the heuristic conditional-probability condition are equivalent, since $P[A\mid B] = P[A \cap B]/P[B]$ and $P[B\mid A] = P[A \cap B]/P[A]$.

For more than two events, there are two common notions. A family $(A_i)_{i\in I}$ is __pairwise independent__ if every pair $(A_i,A_j)$ with $i \neq j$ is independent in the two-event sense. It is __jointly independent__ if for every finite subset $\{i_1,\ldots,i_m\} \subset I$ one has $P[A_{i_1} \cap \cdots \cap A_{i_m}] = \prod_{\ell=1}^m P[A_{i_\ell}]$. Joint independence automatically implies pairwise independence (take $m=2$), but the converse fails in general: it is possible for all pairs to factorise while some triple (or larger finite intersection) does not. The coin-toss example below illustrates this distinction. Note that independence is different from disjointness: if $A$ and $B$ are disjoint and have positive probability, then $P[A \cap B] = 0 \neq P[A]P[B]$, so they cannot be independent.

---

Flashcards for this section are as follows:

- independence of two events / factorization definition ::@:: Events $A,B$ are (stochastically) independent if $P[A \cap B] = P[A]P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-26T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-05-19T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- pairwise independence of a family of events ::@:: A family $(A_i)_{i\in I}$ is pairwise independent if every distinct pair $(A_i,A_j)$ with $i\neq j$ satisfies $P[A_i\cap A_j]=P[A_i]P[A_j]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-21T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-05-03T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- joint independence of a family of events ::@:: A family $(A_i)_{i\in I}$ is jointly independent if for every finite subset $\{i_1,\ldots,i_m\}$ one has $P[A_{i_1}\cap\cdots\cap A_{i_m}] = \prod_{\ell=1}^m P[A_{i_\ell}]$; this implies pairwise independence but not conversely. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-05-19T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-04-16T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-07T00:00:00.000Z-->
- independence versus disjointness ::@:: Disjoint events with positive probability cannot be independent, because $P[A\cap B]=0$ while $P[A]P[B]>0$; independence is about factorisation of probabilities, not set disjointness. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-21T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-04-10T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-06T00:00:00.000Z-->
- factorization criterion versus conditional-probability heuristic ::@:: If $P[A]>0$ and $P[B]>0$, then $A$ and $B$ are independent in the factorisation sense $P[A \cap B]=P[A]P[B]$ __if and only if__ $P[A\mid B]=P[A]$ and $P[B\mid A]=P[B]$: from $P[A \cap B]=P[A]P[B]$ we get $P[A\mid B]=P[A\cap B]/P[B]=P[A]$ and $P[B\mid A]=P[A\cap B]/P[A]=P[B]$, and conversely $P[A\mid B]=P[A]$ and $P[B\mid A]=P[B]$ imply $P[A\cap B]=P[B]P[A\mid B]=P[A]P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-19,67,310!fsrs,2027-05-13T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-13T00:00:00.000Z-->

### stability under complements

In practice we often work with complements of independent events. A useful closure property says that if $A_1,\ldots,A_n$ are jointly independent, then any family $B_1,\ldots,B_n$ obtained by replacing each $A_i$ by either $A_i$ or its complement $A_i^c$ is again jointly independent. For $n=2$, we can see this directly from the definition. Independence of $A_1$ and $A_2$ gives $P[A_1 \cap A_2] = P[A_1]P[A_2]$. Writing $A_1$ as the disjoint union $(A_1 \cap A_2) \cup (A_1 \cap A_2^c)$ and using additivity shows that $P[A_1] = P[A_1 \cap A_2] + P[A_1 \cap A_2^c]$ and hence $P[A_1 \cap A_2^c] = P[A_1](1-P[A_2]) = P[A_1]P[A_2^c]$. Swapping the roles of $A_1$ and $A_2$ yields $P[A_1^c \cap A_2] = P[A_1^c]P[A_2]$, and then repeating the same decomposition with $A_1^c$ in place of $A_1$ and $A_2^c$ in place of $A_2$ shows $P[A_1^c \cap A_2^c] = P[A_1^c]P[A_2^c]$. The general case for $n>2$ follows by induction on $n$, applying the same argument to finite intersections built from the $A_i$ and their complements.

---

Flashcards for this section are as follows:

- joint independence / stability under complements ::@:: If $A_1,\ldots,A_n$ are jointly independent and $B_i$ is either $A_i$ or $A_i^c$ for each $i$, then the family $B_1,\ldots,B_n$ is also jointly independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-14,63,310!fsrs,2027-04-10T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-06T00:00:00.000Z-->
- independence and complements / step 1: split $A_1$ into $A_1\cap A_2$ and $A_1\cap A_2^c$ ::@:: For $n=2$, independence of $A_1$ and $A_2$ gives $P[A_1\cap A_2]=P[A_1]P[A_2]$; writing $A_1=(A_1\cap A_2)\cup(A_1\cap A_2^c)$ as a disjoint union and using additivity yields $P[A_1\cap A_2^c]=P[A_1](1-P[A_2])=P[A_1]P[A_2^c]$. <!--SR:!2026-07-19,67,310!2026-07-19,67,310-->
- independence and complements / step 2: swap the roles of $A_1$ and $A_2$ ::@:: Swapping the roles of $A_1$ and $A_2$ gives $P[A_1^c\cap A_2]=P[A_1^c]P[A_2]$ by the same splitting argument applied to $A_2$. <!--SR:!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z!fsrs,2027-05-08T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- independence and complements / step 3: prove the both-complements case ::@:: Applying the same decomposition with $A_1^c$ in place of $A_1$ and $A_2^c$ in place of $A_2$ shows $P[A_1^c\cap A_2^c]=P[A_1^c]P[A_2^c]$; together with the previous steps this proves stability under complements for $n=2$, and the general $n$ follows by induction. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-27T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-10T00:00:00.000Z!2026-07-14,63,310-->

### independence via cards and coins

A standard card deck has sample space $\Omega = \{(i,j) : i \in \{\clubsuit,\spadesuit,\diamondsuit,\heartsuit\}, j \in \{1,\ldots,13\}\}$ with the discrete uniform distribution. Let $A$ be "heart is drawn" and $B$ be "ace is drawn". Then $P[A] = 1/4$, $P[B] = 1/13$, and $P[A \cap B] = 1/52 = (1/4)(1/13)$, so $A$ and $B$ are independent. For two tosses of a fair coin, let $A$ be "heads on first toss", $B$ be "heads on second toss", and $C$ be "exactly one head occurs". One checks that $A,B,C$ are pairwise independent (each pair satisfies $P[\cdot \cap \cdot] = P[\cdot]P[\cdot]$) but not jointly independent, since $P[A \cap B \cap C] = 0 \neq P[A]P[B]P[C]$.

---

Flashcards for this section are as follows:

- card-deck example / hearts and aces are independent ::@:: In a uniform 52-card deck, $A=$"heart", $B=$"ace" satisfy $P[A]=1/4$, $P[B]=1/13$, $P[A\cap B]=1/52=P[A]P[B]$, so they are independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z!2026-07-19,67,310-->
- coin-toss example / pairwise independent but not jointly independent ::@:: For two fair coin tosses, take $A$="heads on first", $B$="heads on second", $C$="exactly one head"; each has $P[A]=P[B]=P[C]=1/2$ and every pair satisfies $P[A\cap B]=P[A]P[B]$, $P[A\cap C]=P[A]P[C]$, $P[B\cap C]=P[B]P[C]$, so the events are pairwise independent, but $P[A\cap B\cap C]=0$ while $P[A]P[B]P[C]=1/8$, so they are not jointly independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-19,67,310!2026-07-19,67,310-->

## independence of sigma-algebras and generator criteria

Two sigma-algebras $\mathcal G$ and $\mathcal H$ are independent if $P[A\cap B]=P[A]P[B]$ for all $A\in\mathcal G$ and $B\in\mathcal H$.

Random variables $X$ and $Y$ are independent exactly when the sigma-algebras $\sigma(X)$ and $\sigma(Y)$ are independent.

In practice one usually verifies independence on smaller generating classes rather than on every set in the two sigma-algebras.

__Generator criterion.__ If $\mathcal E$ and $\mathcal D$ are pi-systems generating $\mathcal G$ and $\mathcal H$, and if

$P[A\cap B]=P[A]P[B]$ for all $A\in\mathcal E$ and $B\in\mathcal D$,

then $\mathcal G$ and $\mathcal H$ are independent.

__Proof sketch.__ Fix $A\in\mathcal E$ and define

$\Lambda_A=\{B\in\mathcal H:P[A\cap B]=P[A]P[B]\}$.

One checks that $\Lambda_A$ is a Dynkin system containing $\mathcal D$, so by the pi-lambda theorem it contains all of $\mathcal H$. Repeating the argument in the other variable extends the identity from generators to the full sigma-algebras.

This criterion is the standard template for proving independence of random variables from factorization on rectangles or half-lines.

---

Flashcards for this section are as follows:

- independence of sigma-algebras ::@:: Sigma-algebras $\mathcal G$ and $\mathcal H$ are independent if $P[A\cap B]=P[A]P[B]$ for every $A\in\mathcal G$ and $B\in\mathcal H$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- random-variable independence via sigma-algebras ::@:: Random variables $X$ and $Y$ are independent exactly when the sigma-algebras $\sigma(X)$ and $\sigma(Y)$ are independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- generator criterion for independence ::@:: If $\mathcal E$ and $\mathcal D$ are pi-systems generating $\mathcal G$ and $\mathcal H$ respectively, and $P[A\cap B]=P[A]P[B]$ holds for all $A\in\mathcal E$, $B\in\mathcal D$, then $\mathcal G$ and $\mathcal H$ are independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- proof sketch of the generator criterion ::@:: Fix $A\in\mathcal E$ and let $\Lambda_A=\{B\in\mathcal H:P[A\cap B]=P[A]P[B]\}$. One checks $\Lambda_A$ is a Dynkin system containing $\mathcal D$, so by the pi-lambda theorem it contains all of $\mathcal H$. Repeating for the other variable extends independence from generators to the full sigma-algebras. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- why the generator criterion is useful ::@:: It reduces checking independence of two sigma-algebras to verifying factorization on smaller generating classes—such as rectangles or half-lines—which is much easier than checking every pair of measurable sets. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- standard template for proving independence ::@:: The generator criterion plus the pi-lambda theorem is the standard method for proving independence of random variables from factorisation on rectangles or half-lines. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## construction of i.i.d. sequences

A fundamental question in probability theory is: given a prescribed distribution $Q$ on $\mathbb R$, does there exist a probability space supporting an infinite sequence of independent random variables each having law $Q$? The answer is yes, and the construction relies on the product measure on the space of all real sequences.

__Theorem (existence of i.i.d. sequences).__ Let $Q$ be a probability measure on $(\mathbb R, \mathcal B(\mathbb R))$. Then there exists a probability space $(\Omega, \mathcal F, P)$ and a sequence $(X_n)_{n\in\mathbb N}$ of random variables $X_n : (\Omega, \mathcal F) \to (\mathbb R, \mathcal B(\mathbb R))$ that are i.i.d. with $P_{X_n} = Q$ for all $n\in\mathbb N$.

__Proof.__ Set $\Omega = \mathbb R^{\mathbb N}$, the space of all real sequences $\omega = (\omega_1, \omega_2, \ldots)$, and equip it with the product sigma-algebra $\mathcal F = \mathcal B(\mathbb R)^{\otimes \mathbb N}$, i.e., the sigma-algebra generated by cylinder sets of the form $C = A_1 \times \cdots \times A_n \times \mathbb R \times \mathbb R \times \cdots$ with $A_i \in \mathcal B(\mathbb R)$. Define a pre-measure $P_0$ on the semiring of cylinder sets by $P_0\bigl(A_1 \times \cdots \times A_n \times \mathbb R \times \cdots\bigr) = \prod_{i=1}^n Q(A_i)$, which is well defined because the factorisation is consistent under marginalisation. By the Kolmogorov extension theorem (or, equivalently, by Carathéodory's extension theorem applied to this semiring), $P_0$ extends uniquely to a probability measure $P$ on $(\Omega, \mathcal F)$. Now define the coordinate projections $X_n(\omega) = \omega_n$. Each $X_n$ is measurable because pre-images of Borel sets are cylinder sets. The law of $X_n$ is $Q$: $P[X_n \in A] = P[\mathbb R \times \cdots \times \mathbb R \times A \times \mathbb R \times \cdots] = Q(A)$. Finally, for any finite collection $n_1,\ldots,n_k$ and Borel sets $A_{n_1},\ldots,A_{n_k}$, we have $P\bigl[X_{n_1} \in A_{n_1}, \ldots, X_{n_k} \in A_{n_k}\bigr] = P_0\bigl(A_{n_1} \times \cdots \times A_{n_k} \times \mathbb R \times \cdots\bigr) = \prod_{i=1}^k Q(A_{n_i}) = \prod_{i=1}^k P[X_{n_i} \in A_{n_i}]$, so the $X_n$ are independent. Together with the identical law, the sequence is i.i.d.

__Remark.__ For the special case of a product of countably many copies of the same measurable space, one can also construct $P$ directly as the product measure $Q^{\otimes \mathbb N}$ via Carathéodory's extension theorem on the semiring of cylinder sets. The Kolmogorov extension theorem is the more general tool that handles arbitrary projective families of finite-dimensional distributions, but the present construction reduces to the same idea.

---

Flashcards for this section are as follows:

- existence of i.i.d. sequences / theorem statement ::@:: Let $Q$ be a probability measure on $(\mathbb R, \mathcal B(\mathbb R))$. Then there exists a probability space $(\Omega, \mathcal F, P)$ and a sequence $(X_n)_{n\in\mathbb N}$ of random variables $X_n : (\Omega, \mathcal F) \to (\mathbb R, \mathcal B(\mathbb R))$ that are i.i.d. with $P_{X_n} = Q$ for all $n\in\mathbb N$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- sample space and sigma-algebra in i.i.d. construction ::@:: $\Omega = \mathbb R^{\mathbb N}$ (all real sequences), $\mathcal F = \mathcal B(\mathbb R)^{\otimes \mathbb N}$, the sigma-algebra generated by cylinder sets $A_1\times\cdots\times A_n\times\mathbb R\times\cdots$ with $A_i\in\mathcal B(\mathbb R)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- cylinder sets in the product-space construction ::@:: Cylinder sets have the form $C = A_1\times\cdots\times A_n\times\mathbb R\times\mathbb R\times\cdots$ with $A_i\in\mathcal B(\mathbb R)$; they form a semiring that generates $\mathcal F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- pre-measure on cylinder sets ::@:: Define $P_0(A_1\times\cdots\times A_n\times\mathbb R\times\cdots) = \prod_{i=1}^n Q(A_i)$; this is well-defined because the factorisation is consistent under marginalisation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- extension of the pre-measure to a probability measure ::@:: By the Kolmogorov extension theorem (or Carathéodory on the semiring of cylinder sets), $P_0$ extends uniquely to a probability measure $P$ on $(\Omega,\mathcal F)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- coordinate projections are measurable in the construction ::@:: $X_n(\omega)=\omega_n$; the pre-image of a Borel set $A$ is the cylinder set $\mathbb R\times\cdots\times\mathbb R\times A\times\mathbb R\times\cdots$, which lies in $\mathcal F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- why the constructed $X_n$ are i.i.d. ::@:: $P[X_n\in A]=Q(A)$ by the pre-measure formula, and finite-dimensional distributions factorise as $\prod_i Q(A_{n_i})=\prod_i P[X_{n_i}\in A_{n_i}]$, proving independence; identical law is immediate from the coordinate projection definition. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- existence of i.i.d. sequences / key idea of construction ::@:: Take $\Omega = \mathbb R^{\mathbb N}$ with the product measure $Q^{\otimes \mathbb N}$ and define $X_n$ as coordinate projections. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
