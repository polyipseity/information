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

- independence / overview ::@:: Independence expresses that $P[A\cap B]$ factors as $P[A]P[B]$ and, more generally, that finite intersections of events have probability equal to the product of their individual probabilities. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## definitions: pairwise and joint independence

Heuristically, two events $A,B \in \mathcal{F}$ should be independent if knowing that one occurs does not change the probability of the other: we would like $P[A] = P[A\mid B] = P[A\mid B^c]$ and $P[B] = P[B\mid A] = P[B\mid A^c]$ whenever these are defined. Using the multiplication theorem, this leads to the formal definition: $A$ and $B$ are (stochastically) **independent** if $P[A \cap B] = P[A]\,P[B]$. When $P[A]>0$ and $P[B]>0$, this factorisation condition and the heuristic conditional-probability condition are equivalent, since $P[A\mid B] = P[A \cap B]/P[B]$ and $P[B\mid A] = P[A \cap B]/P[A]$.

For more than two events, there are two common notions. A family $(A_i)_{i\in I}$ is **pairwise independent** if every pair $(A_i,A_j)$ with $i \neq j$ is independent in the two-event sense. It is **jointly independent** if for every finite subset $\{i_1,\ldots,i_m\} \subset I$ one has $P[A_{i_1} \cap \cdots \cap A_{i_m}] = \prod_{\ell=1}^m P[A_{i_\ell}]$. Joint independence automatically implies pairwise independence (take $m=2$), but the converse fails in general: it is possible for all pairs to factorise while some triple (or larger finite intersection) does not. The coin-toss example below illustrates this distinction. Note that independence is different from disjointness: if $A$ and $B$ are disjoint and have positive probability, then $P[A \cap B] = 0 \neq P[A]P[B]$, so they cannot be independent.

---

Flashcards for this section are as follows:

- independence of two events / factorization definition ::@:: Events $A,B$ are (stochastically) independent if $P[A \cap B] = P[A]P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pairwise independence of a family of events ::@:: A family $(A_i)_{i\in I}$ is pairwise independent if every distinct pair $(A_i,A_j)$ with $i\neq j$ satisfies $P[A_i\cap A_j]=P[A_i]P[A_j]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- joint independence of a family of events ::@:: A family $(A_i)_{i\in I}$ is jointly independent if for every finite subset $\{i_1,\ldots,i_m\}$ one has $P[A_{i_1}\cap\cdots\cap A_{i_m}] = \prod_{\ell=1}^m P[A_{i_\ell}]$; this implies pairwise independence but not conversely. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- independence versus disjointness ::@:: Disjoint events with positive probability cannot be independent, because $P[A\cap B]=0$ while $P[A]P[B]>0$; independence is about factorisation of probabilities, not set disjointness. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- independence / factorization criterion versus conditional-probability heuristic ::@:: If $P[A]>0$ and $P[B]>0$, then $A$ and $B$ are independent in the factorisation sense $P[A \cap B]=P[A]P[B]$ **if and only if** $P[A\mid B]=P[A]$ and $P[B\mid A]=P[B]$: from $P[A \cap B]=P[A]P[B]$ we get $P[A\mid B]=P[A\cap B]/P[B]=P[A]$ and $P[B\mid A]=P[A\cap B]/P[A]=P[B]$, and conversely $P[A\mid B]=P[A]$ and $P[B\mid A]=P[B]$ imply $P[A\cap B]=P[B]P[A\mid B]=P[A]P[B]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### stability under complements

In practice we often work with complements of independent events. A useful closure property says that if $A_1,\ldots,A_n$ are jointly independent, then any family $B_1,\ldots,B_n$ obtained by replacing each $A_i$ by either $A_i$ or its complement $A_i^c$ is again jointly independent. For $n=2$, we can see this directly from the definition. Independence of $A_1$ and $A_2$ gives $P[A_1 \cap A_2] = P[A_1]P[A_2]$. Writing $A_1$ as the disjoint union $(A_1 \cap A_2) \cup (A_1 \cap A_2^c)$ and using additivity shows that $P[A_1] = P[A_1 \cap A_2] + P[A_1 \cap A_2^c]$ and hence $P[A_1 \cap A_2^c] = P[A_1](1-P[A_2]) = P[A_1]P[A_2^c]$. Swapping the roles of $A_1$ and $A_2$ yields $P[A_1^c \cap A_2] = P[A_1^c]P[A_2]$, and then repeating the same decomposition with $A_1^c$ in place of $A_1$ and $A_2^c$ in place of $A_2$ shows $P[A_1^c \cap A_2^c] = P[A_1^c]P[A_2^c]$. The general case for $n>2$ follows by induction on $n$, applying the same argument to finite intersections built from the $A_i$ and their complements.

---

Flashcards for this section are as follows:

- joint independence / stability under complements ::@:: If $A_1,\ldots,A_n$ are jointly independent and $B_i$ is either $A_i$ or $A_i^c$ for each $i$, then the family $B_1,\ldots,B_n$ is also jointly independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- independence and complements / step 1: split $A_1$ into $A_1\cap A_2$ and $A_1\cap A_2^c$ ::@:: For $n=2$, independence of $A_1$ and $A_2$ gives $P[A_1\cap A_2]=P[A_1]P[A_2]$; writing $A_1=(A_1\cap A_2)\cup(A_1\cap A_2^c)$ as a disjoint union and using additivity yields $P[A_1\cap A_2^c]=P[A_1](1-P[A_2])=P[A_1]P[A_2^c]$.
- independence and complements / step 2: swap the roles of $A_1$ and $A_2$ ::@:: Swapping the roles of $A_1$ and $A_2$ gives $P[A_1^c\cap A_2]=P[A_1^c]P[A_2]$ by the same splitting argument applied to $A_2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- independence and complements / step 3: prove the both-complements case ::@:: Applying the same decomposition with $A_1^c$ in place of $A_1$ and $A_2^c$ in place of $A_2$ shows $P[A_1^c\cap A_2^c]=P[A_1^c]P[A_2^c]$; together with the previous steps this proves stability under complements for $n=2$, and the general $n$ follows by induction. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### independence via cards and coins

A standard card deck has sample space $\Omega = \{(i,j) : i \in \{\clubsuit,\spadesuit,\diamondsuit,\heartsuit\}, j \in \{1,\ldots,13\}\}$ with the discrete uniform distribution. Let $A$ be "heart is drawn" and $B$ be "ace is drawn". Then $P[A] = 1/4$, $P[B] = 1/13$, and $P[A \cap B] = 1/52 = (1/4)(1/13)$, so $A$ and $B$ are independent. For two tosses of a fair coin, let $A$ be "heads on first toss", $B$ be "heads on second toss", and $C$ be "exactly one head occurs". One checks that $A,B,C$ are pairwise independent (each pair satisfies $P[\cdot \cap \cdot] = P[\cdot]P[\cdot]$) but not jointly independent, since $P[A \cap B \cap C] = 0 \neq P[A]P[B]P[C]$.

---

Flashcards for this section are as follows:

- card-deck example / hearts and aces are independent ::@:: In a uniform 52-card deck, $A=$"heart", $B=$"ace" satisfy $P[A]=1/4$, $P[B]=1/13$, $P[A\cap B]=1/52=P[A]P[B]$, so they are independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- coin-toss example / pairwise independent but not jointly independent ::@:: For two fair coin tosses, take $A$="heads on first", $B$="heads on second", $C$="exactly one head"; each has $P[A]=P[B]=P[C]=1/2$ and every pair satisfies $P[A\cap B]=P[A]P[B]$, $P[A\cap C]=P[A]P[C]$, $P[B\cap C]=P[B]P[C]$, so the events are pairwise independent, but $P[A\cap B\cap C]=0$ while $P[A]P[B]P[C]=1/8$, so they are not jointly independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
