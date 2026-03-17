---
aliases:
  - events
  - sigma-algebra
  - sigma-algebras
  - σ-algebra
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/sigma-algebra
  - language/in/English
---

# sigma-algebra

Once a sample space $\Omega$ is fixed, we want to assign probabilities to certain subsets of $\Omega$, called _events_. For countable $\Omega$, the naive choice "every subset is an event" works and we take $\mathcal{F} = \mathcal{P}(\Omega)$. For uncountable $\Omega$, we cannot consistently assign a probability to every subset; we restrict to a $\sigma$-algebra $\mathcal{F} \subseteq \mathcal{P}(\Omega)$.

## power set and naive definition of event

The _power set_ $\mathcal{P}(\Omega)$ is the set of all subsets of $\Omega$: $\mathcal{P}(\Omega) = \{A : A \subseteq \Omega\}$. Naively, an _event_ is a subset $A \subseteq \Omega$; we say the event $A$ _occurs_ for outcome $\omega$ if $\omega \in A$, and does not occur if $\omega \notin A$. This naive view suffices for countable $\Omega$ but not for uncountable $\Omega$.

---

Flashcards for this section are as follows:

- sigma-algebra / power set ::@:: $\mathcal{P}(\Omega) = \{A : A \subseteq \Omega\}$; the set of all subsets of $\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / event (naive) ::@:: A subset $A \subseteq \Omega$; $A$ occurs for $\omega$ iff $\omega \in A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / why restrict for uncountable Omega ::@:: For uncountable $\Omega$, assigning probability to every subset leads to measure-theoretic obstructions; we restrict to a smaller $\sigma$-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## definition of sigma-algebra

Let $\Omega \neq \emptyset$. A $\sigma$-algebra on $\Omega$ is a collection $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ satisfying: (S1) $\Omega \in \mathcal{F}$; (S2) if $A \in \mathcal{F}$ then $A^c = \Omega \setminus A \in \mathcal{F}$ (closed under complements); (S3) if $A_j \in \mathcal{F}$ for all $j \in \mathbb{N}$, then $\bigcup_{j=1}^{\infty} A_j \in \mathcal{F}$ (closed under countable unions). A set $A \in \mathcal{F}$ is called an _event_. The power set $\mathcal{P}(\Omega)$ is a $\sigma$-algebra (used when $\Omega$ is countable). The event $\Omega$ always occurs; the event $\emptyset = \Omega^c$ never occurs. (S2) means: if $A$ is an event, then " $A$ does not occur" is an event. (S3) means: if $A_1, A_2, \ldots$ are events, then "at least one $A_j$ occurs" is an event.

---

Flashcards for this section are as follows:

- sigma-algebra / definition (S1) ::@:: $\Omega \in \mathcal{F}$ (whole space is an event). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / definition (S2) ::@:: If $A \in \mathcal{F}$ then $A^c \in \mathcal{F}$ (closed under complement). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / definition (S3) ::@:: If $A_j \in \mathcal{F}$ for $j \in \mathbb{N}$ then $\bigcup_{j=1}^{\infty} A_j \in \mathcal{F}$ (closed under countable union). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / event (formal) ::@:: An event is a set $A \in \mathcal{F}$; only sets in $\mathcal{F}$ get a probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / P(Omega) is sigma-algebra ::@:: $\mathcal{P}(\Omega)$ satisfies (S1)–(S3); we use it when $\Omega$ is countable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## consequences: empty set, intersections, finite operations

### empty set

From the definition one deduces that $\emptyset \in \mathcal{F}$ (since $\emptyset = \Omega^c$); this is the "impossible event".

---

Flashcards for this section are as follows:

- sigma-algebra / empty set in F ::@:: $\emptyset \in \mathcal{F}$ because $\emptyset = \Omega^c$ and (S2); it is the impossible event (never occurs). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### countable intersections

Using de Morgan's laws, $\mathcal{F}$ is closed under countable intersections: for $A_j \in \mathcal{F}$, $\bigcap_{j=1}^{\infty} A_j = \big(\bigcup_{j=1}^{\infty} A_j^c\big)^c \in \mathcal{F}$, so "all of $A_1,A_2,\ldots$ occur" is an event whenever each $A_j$ is.

---

Flashcards for this section are as follows:

- sigma-algebra / countable intersection ::@:: If $A_j \in \mathcal{F}$ for all $j$, then $\bigcap_{j=1}^{\infty} A_j \in \mathcal{F}$ via de Morgan: $\bigcap_j A_j = (\bigcup_j A_j^c)^c$ and (S2),(S3); "all $A_j$ occur" is an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / de Morgan ::@:: $(\bigcup_i U_i)^c = \bigcap_i U_i^c$ and $(\bigcap_i U_i)^c = \bigcup_i U_i^c$; used to convert closure under countable unions into closure under intersections. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### finite operations

If $A, B \in \mathcal{F}$, then $A \cup B$, $A \cap B$, and $A \setminus B = A \cap B^c$ are in $\mathcal{F}$: finite unions come from (S3) by taking $A_3 = A_4 = \cdots = \emptyset$, intersections from the countable-intersection rule, and set difference from complements and intersections. Thus "at least one of $A,B$", "both $A,B$", and "A but not B" are all legitimate events.

---

Flashcards for this section are as follows:

- sigma-algebra / finite union and intersection ::@:: If $A, B \in \mathcal{F}$, then $A \cup B$, $A \cap B$, and $A \setminus B = A \cap B^c$ are in $\mathcal{F}$; finite unions come from (S3) by padding with $\emptyset$, intersections from de Morgan, and $A\setminus B$ from complements. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## concrete cases and violations

Let $\Omega = \{1, 2, 3\}$. $\mathcal{F}_1 = \{\emptyset, \{1\}, \{2,3\}, \Omega\}$ is a $\sigma$-algebra (e.g. observer cannot distinguish 2 and 3). $\mathcal{F}_2 = \{\emptyset, \{1\}, \{2,3\}\}$ is not (violates (S1): $\Omega \notin \mathcal{F}_2$). $\mathcal{F}_3 = \{\emptyset, \{1\}, \Omega\}$ is not (violates (S2): $\{1\}^c = \{2,3\} \notin \mathcal{F}_3$). $\mathcal{F}_4 = \{\emptyset, \{1\}, \{2\}, \{1,3\}, \{2,3\}, \Omega\}$ is not (violates (S3): $\{1\} \cup \{2\} = \{1,2\} \notin \mathcal{F}_4$). Rolling a die: $\Omega = \{1,\ldots,6\}$, $\mathcal{F} = \mathcal{P}(\Omega)$. Events $A = \{\text{even}\} = \{2,4,6\}$, $B = \{\text{prime}\} = \{2,3,5\}$, $C = \{\text{odd}\} = \{1,3,5\}$; then $B^c = \{1,4,6\}$, $A \cup B = \{2,3,4,5,6\}$, $A \cap B = \{2\}$, $A \cap C = \emptyset$ (mutually exclusive).

---

Flashcards for this section are as follows:

- sigma-algebra / a smaller sigma-algebra on $\{1,2,3\}$ ::@:: $\mathcal{F}_1 = \{\emptyset, \{1\}, \{2,3\}, \Omega\}$ is a $\sigma$-algebra: it contains $\Omega$ and is closed under complements and countable unions; intuitively it models an observer who cannot distinguish outcomes 2 and 3.
- sigma-algebra / violation S1 ::@:: $\mathcal{F}_2 = \{\emptyset, \{1\}, \{2,3\}\}$ fails (S1) because $\Omega \notin \mathcal{F}_2$; any candidate family missing the whole space cannot be a $\sigma$-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / violation S2 ::@:: $\mathcal{F}_3 = \{\emptyset, \{1\}, \Omega\}$ fails (S2) because $\{1\}^c = \{2,3\} \notin \mathcal{F}_3$; closure under complements means every event’s complement must also be an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / violation S3 ::@:: $\mathcal{F}_4 = \{\emptyset, \{1\}, \{2\}, \{1,3\}, \{2,3\}, \Omega\}$ fails (S3) because $\{1\} \cup \{2\} = \{1,2\} \notin \mathcal{F}_4$; a $\sigma$-algebra must contain countable unions of its sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / die events A even B prime ::@:: For $\Omega = \{1,\ldots,6\}$ and $\mathcal{F} = \mathcal{P}(\Omega)$, let $A = \{2,4,6\}$ (even) and $B = \{2,3,5\}$ (prime); then $A \cap B = \{2\}$, $A \cup B = \{2,3,4,5,6\}$, illustrating that "A or B" is non-exclusive while still an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra / mutually exclusive ::@:: Events $A$ and $C$ are mutually exclusive if $A \cap C = \emptyset$ (they cannot both occur); in the die example $A = \{\text{even}\}$ and $C = \{\text{odd}\}$ satisfy $A \cap C = \emptyset$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
