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

## power set

The _power set_ $\mathcal{P}(\Omega)$ is the set of all subsets of $\Omega$: $\mathcal{P}(\Omega) = \{A : A \subseteq \Omega\}$. When $\Omega$ is countable, the power set is often the natural event collection because every subset can then be treated as an event.

---

Flashcards for this section are as follows:

- power set ::@:: $\mathcal{P}(\Omega) = \{A : A \subseteq \Omega\}$; the set of all subsets of $\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## naive definition of event

Naively, an _event_ is a subset $A \subseteq \Omega$; we say the event $A$ _occurs_ for outcome $\omega$ if $\omega \in A$, and does not occur if $\omega \notin A$. This naive view suffices for countable $\Omega$ but not for uncountable $\Omega$, where assigning probabilities to all subsets leads to measure-theoretic obstructions.

---

Flashcards for this section are as follows:

- event (naive) ::@:: A subset $A \subseteq \Omega$; $A$ occurs for $\omega$ iff $\omega \in A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why restrict for uncountable Omega ::@:: For uncountable $\Omega$, assigning probability to every subset leads to measure-theoretic obstructions; we restrict to a smaller $\sigma$-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## definition of sigma-algebra

Let $\Omega \neq \emptyset$. A $\sigma$-algebra on $\Omega$ is a collection $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ satisfying: (S1) $\Omega \in \mathcal{F}$; (S2) if $A \in \mathcal{F}$ then $A^c = \Omega \setminus A \in \mathcal{F}$ (closed under complements); (S3) if $A_j \in \mathcal{F}$ for all $j \in \mathbb{N}$, then $\bigcup_{j=1}^{\infty} A_j \in \mathcal{F}$ (closed under countable unions). A set $A \in \mathcal{F}$ is called an _event_. The power set $\mathcal{P}(\Omega)$ is a $\sigma$-algebra (used when $\Omega$ is countable). The event $\Omega$ always occurs; the event $\emptyset = \Omega^c$ never occurs. (S2) means: if $A$ is an event, then " $A$ does not occur" is an event. (S3) means: if $A_1, A_2, \ldots$ are events, then "at least one $A_j$ occurs" is an event.

---

Flashcards for this section are as follows:

- definition (S1) ::@:: $\Omega \in \mathcal{F}$ (whole space is an event). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- definition (S2) ::@:: If $A \in \mathcal{F}$ then $A^c \in \mathcal{F}$ (closed under complement). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- definition (S3) ::@:: If $A_j \in \mathcal{F}$ for $j \in \mathbb{N}$ then $\bigcup_{j=1}^{\infty} A_j \in \mathcal{F}$ (closed under countable union). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- event (formal) ::@:: An event is a set $A \in \mathcal{F}$; only sets in $\mathcal{F}$ get a probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- P(Omega) is sigma-algebra ::@:: $\mathcal{P}(\Omega)$ satisfies (S1)–(S3); we use it when $\Omega$ is countable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## consequences: empty set, intersections, finite operations

### empty set

From the definition one deduces that $\emptyset \in \mathcal{F}$ (since $\emptyset = \Omega^c$); this is the "impossible event".

---

Flashcards for this section are as follows:

- empty set in F ::@:: $\emptyset \in \mathcal{F}$ because $\emptyset = \Omega^c$ and (S2); it is the impossible event (never occurs). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### countable intersections

Using de Morgan's laws, $\mathcal{F}$ is closed under countable intersections: for $A_j \in \mathcal{F}$, $\bigcap_{j=1}^{\infty} A_j = \big(\bigcup_{j=1}^{\infty} A_j^c\big)^c \in \mathcal{F}$, so "all of $A_1,A_2,\ldots$ occur" is an event whenever each $A_j$ is.

---

Flashcards for this section are as follows:

- countable intersection ::@:: If $A_j \in \mathcal{F}$ for all $j$, then $\bigcap_{j=1}^{\infty} A_j \in \mathcal{F}$ via de Morgan: $\bigcap_j A_j = (\bigcup_j A_j^c)^c$ and (S2),(S3); "all $A_j$ occur" is an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- de Morgan ::@:: $(\bigcup_i U_i)^c = \bigcap_i U_i^c$ and $(\bigcap_i U_i)^c = \bigcup_i U_i^c$; used to convert closure under countable unions into closure under intersections. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### finite operations

If $A, B \in \mathcal{F}$, then $A \cup B$, $A \cap B$, and $A \setminus B = A \cap B^c$ are in $\mathcal{F}$: finite unions come from (S3) by taking $A_3 = A_4 = \cdots = \emptyset$, intersections from the countable-intersection rule, and set difference from complements and intersections. Thus "at least one of $A,B$", "both $A,B$", and "A but not B" are all legitimate events.

---

Flashcards for this section are as follows:

- finite union and intersection ::@:: If $A, B \in \mathcal{F}$, then $A \cup B$, $A \cap B$, and $A \setminus B = A \cap B^c$ are in $\mathcal{F}$; finite unions come from (S3) by padding with $\emptyset$, intersections from de Morgan, and $A\setminus B$ from complements. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## generated sigma-algebras

On an uncountable space such as $\mathbb{R}$, the power set is too large for interval-length formulas to extend to a probability measure on every subset. In particular, there is no probability measure $P$ on $([0,1), \mathcal{P}([0,1)))$ such that $P[[a,b)] = b-a$ for every $0 \le a < b < 1$. Intuitively, requiring every subset to be measurable while keeping interval length and countable additivity forces incompatible constraints (the classic Vitali-set obstruction): translation-invariant “length” and countable decomposition cannot be satisfied on _all_ subsets at once. So if we want interval probabilities of the form “length of the interval”, we must work with a smaller $\sigma$-algebra than the full power set.

Given any family $\mathcal{E} \subseteq \mathcal{P}(\Omega)$, let $\mathfrak{G}_{\mathcal{E}} := \{\mathcal{F} \subseteq \mathcal{P}(\Omega) : \mathcal{F}\text{ is a }\sigma\text{-algebra and }\mathcal{E}\subseteq \mathcal{F}\}$. This class is nonempty because $\mathcal{P}(\Omega)$ is a $\sigma$-algebra and contains every subset of $\Omega$, hence contains $\mathcal{E}$.

Now define $\sigma(\mathcal{E}) := \bigcap_{\mathcal{F}\in\mathfrak{G}_{\mathcal{E}}} \mathcal{F}$.

To justify this rigorously, we use the fact that intersections of arbitrarily many $\sigma$-algebras are still $\sigma$-algebras: if $(\mathcal{F}_i)_{i\in I}$ are $\sigma$-algebras on $\Omega$ and $\mathcal{F}_\star := \bigcap_{i\in I}\mathcal{F}_i$, then (1) $\Omega\in\mathcal{F}_\star$ because $\Omega\in\mathcal{F}_i$ for every $i$; (2) if $A\in\mathcal{F}_\star$, then $A\in\mathcal{F}_i$ for every $i$, so $A^c\in\mathcal{F}_i$ for every $i$, hence $A^c\in\mathcal{F}_\star$; (3) if $A_n\in\mathcal{F}_\star$ for all $n$, then each $A_n\in\mathcal{F}_i$ for every $i$, so $\bigcup_{n=1}^\infty A_n\in\mathcal{F}_i$ for every $i$, hence $\bigcup_{n=1}^\infty A_n\in\mathcal{F}_\star$. Therefore $\mathcal{F}_\star$ is a $\sigma$-algebra.

Applying this to $\mathfrak{G}_{\mathcal{E}}$, $\sigma(\mathcal{E})$ is a $\sigma$-algebra, contains $\mathcal{E}$ (because every member of $\mathfrak{G}_{\mathcal{E}}$ contains $\mathcal{E}$), and is minimal: if $\mathcal{H}$ is any $\sigma$-algebra with $\mathcal{E}\subseteq\mathcal{H}$, then $\mathcal{H}\in\mathfrak{G}_{\mathcal{E}}$, so $\sigma(\mathcal{E})\subseteq\mathcal{H}$. This construction is worth remembering because the generated Dynkin system below is obtained in exactly the same way: replace “sigma-algebra” by “Dynkin system” and intersect all such containing families.

There is one special case worth isolating. If $\mathcal{E}=\varnothing$, then $\sigma(\varnothing)$ is the smallest sigma-algebra on $\Omega$, namely $\{\varnothing,\Omega\}$. Indeed, every sigma-algebra contains $\varnothing$ and $\Omega$, so their two-point family is contained in every sigma-algebra and is itself a sigma-algebra.

Typical course examples:

- On a finite space, if $\Omega=\{1,2,3,4\}$ and $\mathcal{E}=\{\{1,2\}\}$, then $\sigma(\mathcal{E})=\{\emptyset,\{1,2\},\{3,4\},\Omega\}$.
- On $\mathbb{R}$, $\sigma\big(\{[a,b):a<b\}\big)$ is the Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R})$; equivalently, generating from half-lines $(-\infty,t]$ gives the same Borel $\sigma$-algebra.

---

Flashcards for this section are as follows:

- interval-length assignment cannot extend to all subsets of $[0,1)$ ::@:: There is no probability measure $P$ on $([0,1),\mathcal{P}([0,1)))$ such that $P[[a,b)] = b-a$ for every $0 \le a < b < 1$; this is why one uses a smaller sigma-algebra than the full power set on uncountable spaces.
- intuition for why interval length cannot extend to all subsets of $[0,1)$ ::@:: If every subset were measurable and interval-length plus countable additivity were enforced, translation-invariant decompositions (Vitali-set phenomenon) force contradictory values; the conflict is between “length behaves well under shifts” and “all subsets are measurable.”
- generated sigma-algebra and why the definition makes sense ::@:: For $\mathcal{E}\subseteq\mathcal{P}(\Omega)$, the generated sigma-algebra $\sigma(\mathcal{E})$ is the intersection of all sigma-algebras on $\Omega$ that contain $\mathcal{E}$; this family is nonempty because $\mathcal{P}(\Omega)$ is itself a sigma-algebra containing $\mathcal{E}$, so $\sigma(\mathcal{E})$ is well defined and is the smallest sigma-algebra containing $\mathcal{E}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- generated sigma-algebra versus generated Dynkin system construction ::@:: The definition of $\sigma(\mathcal{E})$ and the later definition of $\delta(\mathcal{E})$ are parallel: in both cases one intersects all containing structures of the given type; only the closure axioms of the target class change. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- special case $\sigma(\varnothing)$ ::@:: If $\mathcal{E}=\varnothing$, then $\sigma(\varnothing)=\{\varnothing,\Omega\}$, the smallest sigma-algebra on $\Omega$.
- intersection of arbitrarily many sigma-algebras ::@:: If $(\mathcal{F}_i)_{i\in I}$ are sigma-algebras on $\Omega$, then $\bigcap_{i\in I}\mathcal{F}_i$ is a sigma-algebra: $\Omega$ is in every $\mathcal{F}_i$, complements stay in every $\mathcal{F}_i$, and countable unions stay in every $\mathcal{F}_i$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- finite-space generated sigma-algebra example: If $\Omega=\{1,2,3,4\}$ and $\mathcal{E}=\{\{1,2\}\}$, what is $\sigma(\mathcal{E})$? ::@:: $\sigma(\mathcal{E})=\{\emptyset,\{1,2\},\{3,4\},\Omega\}$.
- interval-generator example on $\mathbb{R}$ ::@:: $\sigma(\{[a,b):a<b\})=\mathcal{B}(\mathbb{R})$, and generating from half-lines $(-\infty,t]$ gives the same Borel sigma-algebra; half-open intervals and half-lines generate the same class of Borel sets.

<!-- check: ignore-next-line[header_style_rule]: proper noun -->
### Borel sigma-algebra

The most important generated sigma-algebra for continuous probability is the _Borel sigma-algebra_ $\mathcal{B}(\mathbb{R})$, generated by the half-open intervals $[a,b)$ with $a<b$. Because $\mathcal{B}(\mathbb{R})$ is a sigma-algebra containing the half-open intervals, it also contains sets built from them by complements, countable unions, and countable intersections. In particular, singletons, closed intervals, open intervals, half-open intervals of either type, and every countable subset of $\mathbb{R}$ are Borel sets. For example, $\{a\} = \bigcap_{n=1}^{\infty}[a,a+1/n)$ shows that singletons are Borel, and every countable subset of $\mathbb{R}$ is then a countable union of Borel singletons.

---

Flashcards for this section are as follows:

- Borel sigma-algebra ::@:: The Borel sigma-algebra $\mathcal{B}(\mathbb{R})$ is the sigma-algebra generated by the half-open intervals $[a,b)$ with $a<b$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why singletons are Borel ::@:: A singleton is Borel because $\{a\}=\bigcap_{n=1}^{\infty}[a,a+1/n)$, a countable intersection of Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why countable subsets of $\mathbb{R}$ are Borel ::@:: Every countable subset of $\mathbb{R}$ is Borel because it is a countable union of singletons, and each singleton is Borel.
- why intervals like $[a,b]$, $(a,b]$, and $(a,b)$ are Borel ::@:: These intervals are Borel because they can be built from half-open intervals and singletons using complements, intersections, and set differences.

### densities induce Borel probability measures

This Borel $\sigma$-algebra is exactly the natural domain for continuous distributions with densities. If $f\colon\mathbb{R}\to\mathbb{R}$ is a probability density function, then there exists a unique probability measure $P$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ such that $P[[a,b)] = \int_a^b f(x)\,dx$ for every $a<b$. Such a probability measure $P$ is called a _continuous distribution with density_ $f$.

The theorem explains why $\mathcal{B}(\mathbb{R})$ is the right event collection for continuous probability: we first know how probabilities should behave on half-open intervals, and then we extend from those intervals to all Borel sets.

A brief proof is as follows. For existence, define $\mu([a,b)):=\int_a^b f(x)\,dx$ on half-open intervals, and more generally define $\mu$ on finite disjoint unions of such intervals by summing the corresponding integrals. Because the integral is additive on disjoint intervals, this is well defined and gives a premeasure; also $\mu(\mathbb{R})=\int_{-\infty}^{\infty} f(x)\,dx=1$. By Carathéodory's extension theorem, $\mu$ extends to a probability measure $P$ on the sigma-algebra generated by the half-open intervals, namely $\mathcal{B}(\mathbb{R})$.

For uniqueness, let $Q$ be another probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ with $Q[[a,b))=\int_a^b f(x)\,dx$ for all $a<b$. Then $P$ and $Q$ agree on the family of half-open intervals, which is a $\pi$-system generating $\mathcal{B}(\mathbb{R})$. Hence, by the pi-lambda theorem (equivalently, uniqueness of measures from agreement on a generating $\pi$-system), $P=Q$ on all Borel sets.

---

Flashcards for this section are as follows:

- density induces a unique Borel probability measure ::@:: If $f\colon\mathbb{R}\to\mathbb{R}$ is a probability density function, then there exists a unique probability measure $P$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ such that $P[[a,b)] = \int_a^b f(x)\,dx$ for every $a<b$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous distribution with density $f$ ::@:: A continuous distribution with density $f$ is the unique probability measure $P$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ satisfying $P[[a,b)] = \int_a^b f(x)\,dx$ for all $a<b$.
- why $\mathcal{B}(\mathbb{R})$ is the natural sigma-algebra for densities ::@:: We first know how to assign probability to half-open intervals by $P[[a,b)] = \int_a^b f(x)\,dx$, and those intervals generate $\mathcal{B}(\mathbb{R})$, so Borel sets are exactly the sets obtained from this interval data by sigma-algebra operations.
- brief proof of density-induced Borel measure theorem ::@:: Existence: define $\mu([a,b)):=\int_a^b f(x)\,dx$ on half-open intervals, extend additively to finite disjoint unions, note $\mu(\mathbb{R})=1$, and apply Carathéodory's extension theorem to obtain a probability measure on $\mathcal{B}(\mathbb{R})$. Uniqueness: any two such measures agree on the generating $\pi$-system of half-open intervals, so by the pi-lambda theorem they agree on all Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## concrete cases and violations

Let $\Omega = \{1, 2, 3\}$. $\mathcal{F}_1 = \{\emptyset, \{1\}, \{2,3\}, \Omega\}$ is a $\sigma$-algebra (e.g. observer cannot distinguish 2 and 3). $\mathcal{F}_2 = \{\emptyset, \{1\}, \{2,3\}\}$ is not (violates (S1): $\Omega \notin \mathcal{F}_2$). $\mathcal{F}_3 = \{\emptyset, \{1\}, \Omega\}$ is not (violates (S2): $\{1\}^c = \{2,3\} \notin \mathcal{F}_3$). $\mathcal{F}_4 = \{\emptyset, \{1\}, \{2\}, \{1,3\}, \{2,3\}, \Omega\}$ is not (violates (S3): $\{1\} \cup \{2\} = \{1,2\} \notin \mathcal{F}_4$). Rolling a die: $\Omega = \{1,\ldots,6\}$, $\mathcal{F} = \mathcal{P}(\Omega)$. Events $A = \{\text{even}\} = \{2,4,6\}$, $B = \{\text{prime}\} = \{2,3,5\}$, $C = \{\text{odd}\} = \{1,3,5\}$; then $B^c = \{1,4,6\}$, $A \cup B = \{2,3,4,5,6\}$, $A \cap B = \{2\}$, $A \cap C = \emptyset$ (mutually exclusive).

---

Flashcards for this section are as follows:

- a smaller sigma-algebra on $\{1,2,3\}$ ::@:: $\mathcal{F}_1 = \{\emptyset, \{1\}, \{2,3\}, \Omega\}$ is a $\sigma$-algebra: it contains $\Omega$ and is closed under complements and countable unions; intuitively it models an observer who cannot distinguish outcomes 2 and 3.
- violation S1 ::@:: $\mathcal{F}_2 = \{\emptyset, \{1\}, \{2,3\}\}$ fails (S1) because $\Omega \notin \mathcal{F}_2$; any candidate family missing the whole space cannot be a $\sigma$-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- violation S2 ::@:: $\mathcal{F}_3 = \{\emptyset, \{1\}, \Omega\}$ fails (S2) because $\{1\}^c = \{2,3\} \notin \mathcal{F}_3$; closure under complements means every event’s complement must also be an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- violation S3 ::@:: $\mathcal{F}_4 = \{\emptyset, \{1\}, \{2\}, \{1,3\}, \{2,3\}, \Omega\}$ fails (S3) because $\{1\} \cup \{2\} = \{1,2\} \notin \mathcal{F}_4$; a $\sigma$-algebra must contain countable unions of its sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- die events A even B prime ::@:: For $\Omega = \{1,\ldots,6\}$ and $\mathcal{F} = \mathcal{P}(\Omega)$, let $A = \{2,4,6\}$ (even) and $B = \{2,3,5\}$ (prime); then $A \cap B = \{2\}$, $A \cup B = \{2,3,4,5,6\}$, illustrating that "A or B" is non-exclusive while still an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- mutually exclusive ::@:: Events $A$ and $C$ are mutually exclusive if $A \cap C = \emptyset$ (they cannot both occur); in the die example $A = \{\text{even}\}$ and $C = \{\text{odd}\}$ satisfy $A \cap C = \emptyset$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## pi-systems and Dynkin systems

Two set systems are especially useful when proving uniqueness results for probability measures. A non-empty collection $\mathcal{E} \subseteq \mathcal{P}(\Omega)$ is a _pi-system_ (or _intersection-stable family_) if $A,B \in \mathcal{E}$ implies $A \cap B \in \mathcal{E}$. The key point is that only **finite intersections** are required: one intersects two sets at a time, and then by repeating the property one gets closure under any finite intersection. A pi-system is therefore much weaker than a sigma-algebra, because it does _not_ ask for complements or countable unions.

The intuition is that pi-systems are usually easy to construct because many natural families are already closed under taking common parts, even when they are far from being sigma-algebras. For example, on $\mathbb{R}$ the half-lines $(-\infty,t]$ form a pi-system because the intersection of two such half-lines is again a half-line of the same type, namely $(-\infty,\min\{s,t\}]$. Likewise, intervals, rectangles, and similar geometric “basic building blocks” are often stable under finite intersections. So a pi-system is a convenient starting family: it is small, concrete, and easy to recognize, yet still strong enough for many uniqueness arguments once one passes to the sigma-algebra it generates.

A collection $\mathcal{D} \subseteq \mathcal{P}(\Omega)$ is a _Dynkin system_ (or _lambda-system_) if (D1) $\Omega \in \mathcal{D}$, (D2) $A \in \mathcal{D}$ implies $A^c \in \mathcal{D}$, and (D3) whenever $(A_n)$ are pairwise disjoint members of $\mathcal{D}$, their union also belongs to $\mathcal{D}$. Compared with a sigma-algebra, the crucial difference is that a Dynkin system only assumes closure under **countable disjoint unions**, not arbitrary countable unions. This is reminiscent of countable additivity in measure theory, where measures are required to add over disjoint unions. So the definition is designed to fit naturally with measure arguments: disjoint pieces are exactly the setting where additivity is simplest.

There is another useful intuition here: Dynkin systems are often easy to verify when a class of sets is defined by a probability-theoretic property. In uniqueness proofs one frequently fixes a reference set system and then considers a class such as “all sets $A$ for which two measures agree on $A$ ”. Checking complements and countable disjoint unions is then natural, because these are exactly the operations that interact cleanly with probability measures. So a Dynkin system is not only motivated by disjoint additivity; it is also a very convenient target notion when one defines a family of sets by some measure-theoretic property and wants to prove that the family is large.

There is also a very useful equivalent reformulation of the Dynkin-system axioms. If $\mathcal{D}$ is a Dynkin system and $A,B\in\mathcal{D}$ with $A\subseteq B$, then $B\setminus A = B\cap A^c = (B^c\cup A)^c \in \mathcal{D}$. Indeed, $B^c, A\in\mathcal{D}$ by (D1) and (D2), and they are disjoint because $A\subseteq B$. So (D3) implies $B^c\cup A\in\mathcal{D}$, and then (D2) gives $(B^c\cup A)^c\in\mathcal{D}$. Thus Dynkin systems are closed under set difference whenever the smaller set is contained in the larger one.

Conversely, one can replace (D2) by this difference property: a collection $\mathcal{D}\subseteq\mathcal{P}(\Omega)$ is a Dynkin system if and only if it satisfies

- (D1) $\Omega\in\mathcal{D}$,
- (D2') if $A,B\in\mathcal{D}$ and $A\subseteq B$, then $B\setminus A\in\mathcal{D}$,
- (D3) if $(A_n)$ are pairwise disjoint members of $\mathcal{D}$, then $\bigcup_{n=1}^{\infty}A_n\in\mathcal{D}$.

To see why, first note that (D1), (D2), and (D3) imply (D2') by the previous argument. For the reverse implication, assume (D1), (D2'), and (D3). Since $A\subseteq\Omega$ for every $A\in\mathcal{D}$, applying (D2') with $B=\Omega$ gives $\Omega\setminus A=A^c\in\mathcal{D}$. So (D2) is recovered, and therefore (D1), (D2), and (D3) hold. This equivalent definition is often easier to use in proofs, because set differences arise naturally when peeling off already-counted parts of sets.

The comparison with sigma-algebras is therefore complementary. A pi-system remembers finite intersections, which are good for describing generating families such as intervals or rectangles. A Dynkin system remembers complements and countable disjoint unions, which are good for uniqueness arguments because they mirror the structural properties of measures. A sigma-algebra combines both kinds of closure in one object.

These notions matter because a collection is a sigma-algebra exactly when it is both a Dynkin system and intersection-stable. The forward implication is immediate: every sigma-algebra is closed under complements, arbitrary countable unions, and hence in particular under countable disjoint unions and finite intersections.

For the converse, suppose $\mathcal{D}$ is a Dynkin system and also a pi-system. Because it is a pi-system, it is closed under finite intersections. From complements and finite intersections we get finite set differences: if $A,B\in\mathcal{D}$, then $A\setminus B = A\cap B^c \in \mathcal{D}$. Now let $A_1,A_2,\ldots \in \mathcal{D}$ be arbitrary, not necessarily disjoint. The problem is that a Dynkin system only knows how to take unions when the pieces are disjoint, so we first convert the $A_n$ into disjoint pieces.

Define

- $B_1 = A_1$,
- $B_n = A_n \setminus \bigcup_{j=1}^{n-1} A_j$ for $n\ge 2$.

Each $B_n$ is the “new part” of $A_n$ not already covered by earlier sets. This is the key idea: instead of letting a point be counted every time it appears in another $A_n$, we force it to appear only at the first stage where it shows up.

Why are the $B_n$ pairwise disjoint? Suppose $m<n$ and $x\in B_m$. Then by definition $x\in A_m$, so $x\in \bigcup_{j=1}^{n-1}A_j$. But membership in $B_n$ requires $x\notin \bigcup_{j=1}^{n-1}A_j$. Hence $x\notin B_n$. Since this works for every pair $m<n$, no point can belong to two different $B_n$.

Why does the union stay the same? First, each $B_n\subseteq A_n$, so automatically $\bigcup_n B_n\subseteq \bigcup_n A_n$. For the reverse inclusion, take any $x\in\bigcup_n A_n$. Then there exists at least one index $n$ with $x\in A_n$. Let $m$ be the smallest such index. By minimality, $x\notin A_1\cup\cdots\cup A_{m-1}$, so $x\in B_m$. Therefore $x\in\bigcup_n B_n$. Thus every point of $\bigcup_n A_n$ appears in exactly one of the disjoint pieces $B_n$, namely the first time it shows up.

It remains to justify that each $B_n$ still lies in $\mathcal{D}$. This is where finite-intersection closure is used. Since $\bigcup_{j=1}^{n-1} A_j$ is a finite union, one may build it from complements and finite intersections, or inductively from the identity $A\cup B = (A^c\cap B^c)^c$. Thus $\bigcup_{j=1}^{n-1} A_j \in \mathcal{D}$, so its complement is in $\mathcal{D}$, and then $B_n = A_n \cap \big(\bigcup_{j=1}^{n-1} A_j\big)^c \in \mathcal{D}$ because $\mathcal{D}$ is a pi-system.

Now the point of the trick becomes clear: the original family $(A_n)$ may overlap too much to use the Dynkin-system axiom, but the replacement family $(B_n)$ is disjoint and has exactly the same union. Therefore (D3) applies to $(B_n)$ and gives $\bigcup_n B_n \in \mathcal{D}$. Since $\bigcup_n A_n = \bigcup_n B_n$, we conclude that $\bigcup_n A_n \in \mathcal{D}$. This proves closure under arbitrary countable unions. Hence $\mathcal{D}$ is a sigma-algebra.

---

Flashcards for this section are as follows:

- pi-system ::@:: A non-empty collection $\mathcal{E}\subseteq\mathcal{P}(\Omega)$ is a pi-system if $A,B\in\mathcal{E}$ implies $A\cap B\in\mathcal{E}$; the condition only requires **finite** intersections, unlike a sigma-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pi-system versus sigma-algebra ::@:: A pi-system keeps the finite-intersection part of a sigma-algebra but does not require complements or countable unions, so it is much weaker than a sigma-algebra.
- pi-system intuition ::@:: A pi-system is often easy to construct because many natural basic families—such as half-lines, intervals, or rectangles—are automatically stable under taking finite intersections, even though they are not closed under complements or countable unions; this makes pi-systems convenient small starting families for uniqueness and generation arguments.
- Dynkin system ::@:: A collection $\mathcal{D}\subseteq\mathcal{P}(\Omega)$ is a Dynkin system if $\Omega\in\mathcal{D}$, $A\in\mathcal{D}\Rightarrow A^c\in\mathcal{D}$, and every countable pairwise disjoint family in $\mathcal{D}$ has its union in $\mathcal{D}$; unlike a sigma-algebra, it assumes only countable **disjoint** unions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Dynkin system intuition ::@:: A Dynkin system is built to match measure-theoretic additivity: its closure under countable disjoint unions mirrors the fact that measures add most naturally over disjoint sets.
- Dynkin system intuition from property-defined families ::@:: Dynkin systems are also convenient because if a class of sets is defined by a probability-theoretic property—such as “all sets on which two measures agree”—then complements and countable disjoint unions are often exactly the operations that are easiest to verify, so the class naturally wants to be a Dynkin system.
- Dynkin system versus sigma-algebra ::@:: A Dynkin system keeps the complement and countable-disjoint-union part of a sigma-algebra, but it does not by itself guarantee closure under arbitrary intersections or arbitrary countable unions.
- Dynkin system difference property ::@:: If $\mathcal{D}$ is a Dynkin system and $A,B\in\mathcal{D}$ with $A\subseteq B$, then $B\setminus A\in\mathcal{D}$ because $B\setminus A=(B^c\cup A)^c$, the sets $B^c$ and $A$ are disjoint, and Dynkin systems are closed under complements and countable disjoint unions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equivalent definition of Dynkin system ::@:: A collection $\mathcal{D}$ is a Dynkin system iff it satisfies (D1) $\Omega\in\mathcal{D}$, (D2') $A\subseteq B$ with $A,B\in\mathcal{D}$ implies $B\setminus A\in\mathcal{D}$, and (D3) closure under countable pairwise disjoint unions; the usual complement axiom is recovered from $A^c=\Omega\setminus A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sigma-algebra iff pi-system plus Dynkin system ::@:: A collection of sets is a sigma-algebra exactly when it is both a Dynkin system and a pi-system: a sigma-algebra clearly has both properties, and conversely the pi-system part handles the intersection/difference steps while the Dynkin-system part handles the final countable disjoint union after disjointification.
- sigma-algebra iff pi-system plus Dynkin system / disjointification
  - sigma-algebra iff pi-system plus Dynkin system / disjointification / setup ::@:: To recover closure under arbitrary countable unions, define $B_1=A_1$ and $B_n=A_n\setminus\bigcup_{j=1}^{n-1}A_j$ for $n\ge2$; each $B_n$ is the new part of $A_n$, so each point is kept only at the first stage where it appears. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - sigma-algebra iff pi-system plus Dynkin system / disjointification / disjointness ::@:: If $m<n$ and $x\in B_m$, then $x\in A_m\subseteq\bigcup_{j=1}^{n-1}A_j$, so $x$ cannot belong to $B_n=A_n\setminus\bigcup_{j=1}^{n-1}A_j$; therefore the $B_n$ are pairwise disjoint. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - sigma-algebra iff pi-system plus Dynkin system / disjointification / same union ::@:: Every $B_n$ is contained in $A_n$, so $\bigcup_n B_n\subseteq\bigcup_n A_n$. Conversely, if $x\in\bigcup_n A_n$, let $m$ be the smallest index with $x\in A_m$; then $x\notin\bigcup_{j=1}^{m-1}A_j$, so $x\in B_m$. Hence $\bigcup_n A_n=\bigcup_n B_n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - sigma-algebra iff pi-system plus Dynkin system / disjointification / why it works ::@:: The point of disjointification is to combine the two closure properties: the pi-system part gives $B_n=A_n\cap(\bigcup_{j<n}A_j)^c\in\mathcal{D}$ by supplying the needed finite-intersection/difference step, while the Dynkin-system part then applies to the pairwise disjoint family $(B_n)$ and yields $\bigcup_n B_n\in\mathcal{D}$. Since $\bigcup_n A_n=\bigcup_n B_n$, arbitrary countable unions also belong to $\mathcal{D}$, so the family is a sigma-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### generated Dynkin systems

Just as one generates a sigma-algebra from a family $\mathcal{E}$ by intersecting all sigma-algebras containing it, one may generate a Dynkin system by intersecting all Dynkin systems containing $\mathcal{E}$. Define $\delta(\mathcal{E})=\bigcap\{\mathcal{D}\subseteq\mathcal{P}(\Omega):\mathcal{D}\text{ is a Dynkin system and }\mathcal{E}\subseteq\mathcal{D}\}$. So the recipe is completely parallel to the definition of $\sigma(\mathcal{E})$: only the ambient closure class has changed.

This is well defined because $\mathcal{P}(\Omega)$ is itself a Dynkin system containing $\mathcal{E}$, so the family being intersected is nonempty. Any intersection of Dynkin systems is again a Dynkin system, since the axioms (contain $\Omega$, closure under complements, closure under countable disjoint unions) are all preserved under arbitrary intersections. Therefore $\delta(\mathcal{E})$ is the smallest Dynkin system containing $\mathcal{E}$.

Again there is a special empty-family case. If $\mathcal{E}=\varnothing$, then $\delta(\varnothing)=\{\varnothing,\Omega\}$. Indeed, every Dynkin system must contain $\Omega$ by definition and then also $\varnothing=\Omega^c$, so the two-point family is contained in every Dynkin system and is itself a Dynkin system.

The relation between $\delta(\mathcal{E})$ and $\sigma(\mathcal{E})$ can be understood operationally. Every operation allowed in a Dynkin system—containing $\Omega$, taking complements, and taking countable disjoint unions—is also allowed in a sigma-algebra. But a sigma-algebra allows more operations, such as arbitrary countable unions and intersections. So any set that can be generated from $\mathcal{E}$ using only Dynkin-system operations can certainly also be generated using sigma-algebra operations. That is why $\delta(\mathcal{E})\subseteq \sigma(\mathcal{E})$.

This inclusion is usually strict at first. The real content of Dynkin's theorem is that if $\mathcal{E}$ is already a pi-system, then this smaller-looking object is in fact large enough to recover the whole generated sigma-algebra.

---

Flashcards for this section are as follows:

- generated Dynkin system ::@:: For $\mathcal{E}\subseteq\mathcal{P}(\Omega)$, the generated Dynkin system is $\delta(\mathcal{E})=\bigcap\{\mathcal{D}\subseteq\mathcal{P}(\Omega):\mathcal{D}\text{ is a Dynkin system and }\mathcal{E}\subseteq\mathcal{D}\}$; it is the smallest Dynkin system containing $\mathcal{E}$, and the construction is parallel to that of $\sigma(\mathcal{E})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $\delta(\mathcal{E})$ is well defined ::@:: The family in the definition of $\delta(\mathcal{E})$ is nonempty because $\mathcal{P}(\Omega)$ is itself a Dynkin system containing every subset of $\Omega$, hence containing $\mathcal{E}$.
- intersection of Dynkin systems ::@:: An arbitrary intersection of Dynkin systems is again a Dynkin system, because the properties $\Omega\in\mathcal{D}$, closure under complements, and closure under countable disjoint unions are all preserved under intersection. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- special case $\delta(\varnothing)$ ::@:: If $\mathcal{E}=\varnothing$, then $\delta(\varnothing)=\{\varnothing,\Omega\}$, the smallest Dynkin system on $\Omega$.
- relation between $\delta(\mathcal{E})$ and $\sigma(\mathcal{E})$ ::@:: Every operation allowed in a Dynkin system is also allowed in a sigma-algebra, but not conversely, so any set obtainable from $\mathcal{E}$ by Dynkin-system operations is also obtainable by sigma-algebra operations; hence $\delta(\mathcal{E})\subseteq\sigma(\mathcal{E})$.

### pi-lambda theorem

The decisive bridge between pi-systems and sigma-algebras is Dynkin's pi-lambda theorem: if $\mathcal{E}$ is a pi-system and $\mathcal{D}$ is a Dynkin system with $\mathcal{E}\subseteq\mathcal{D}$, then $\sigma(\mathcal{E})\subseteq\mathcal{D}$.

Equivalently, if $\mathcal{E}$ is a pi-system, then its generated Dynkin system already equals its generated sigma-algebra: $\delta(\mathcal{E})=\sigma(\mathcal{E})$. The two formulations are equivalent in both directions.

The practical intuition is as follows. The theorem is useful when the sets we _really_ care about form a sigma-algebra, but the property we want to prove is only easy to check on a smaller family and is naturally stable under Dynkin-system operations. So the typical workflow is:

- pick a small generating pi-system $\mathcal{E}$ (intervals, half-lines, rectangles, cylinder sets, ...),
- define a class $\mathcal{D}$ of all sets having the desired property,
- prove that $\mathcal{D}$ is a Dynkin system,
- verify that $\mathcal{E}\subseteq\mathcal{D}$,
- conclude from the pi-lambda theorem that $\sigma(\mathcal{E})\subseteq\mathcal{D}$.

So the theorem is a _bootstrap principle_: once a property survives complements and countable disjoint unions, it is enough to verify it on a convenient intersection-stable generating core.

It is worth pausing to summarize how one _uses_ the theorem in practice. One does **not** normally try to describe every set in $\sigma(\mathcal{E})$ explicitly. Instead, one chooses a pi-system that already generates the sigma-algebra of interest and then packages the desired statement into a Dynkin system. For example:

- to prove uniqueness of a probability measure on $\mathcal{B}(\mathbb{R})$, one may check agreement only on half-lines $(-\infty,t]$ or half-open intervals $[a,b)$;
- to show that a family of Borel sets has some measure-theoretic property, one often proves the property is preserved by complements and countable disjoint unions, so the relevant class is a Dynkin system;
- once the generating pi-system lies inside that class, the theorem automatically promotes the property from the small test family to the whole generated sigma-algebra.

---

Flashcards for this section are as follows:

- Dynkin's pi-lambda theorem ::@:: If $\mathcal{E}$ is a pi-system and $\mathcal{D}$ is a Dynkin system with $\mathcal{E}\subseteq\mathcal{D}$, then $\sigma(\mathcal{E})\subseteq\mathcal{D}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equivalent form with generated Dynkin system ::@:: For a pi-system $\mathcal{E}$, Dynkin's pi-lambda theorem is equivalent to $\delta(\mathcal{E})=\sigma(\mathcal{E})$: saying every Dynkin system containing $\mathcal{E}$ must also contain $\sigma(\mathcal{E})$ is the same as saying the smallest Dynkin system containing $\mathcal{E}$ already is the generated sigma-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pi-lambda theorem / usage intuition ::@:: To use the theorem, choose a small generating pi-system $\mathcal{E}$, define a class $\mathcal{D}$ of sets with the desired property, prove $\mathcal{D}$ is a Dynkin system, verify $\mathcal{E}\subseteq\mathcal{D}$, and then conclude that the property holds on all of $\sigma(\mathcal{E})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pi-lambda theorem / why this strategy is efficient ::@:: The theorem lets you avoid describing every set in the generated sigma-algebra explicitly: you only verify the property on a small intersection-stable generator and check that the property is preserved by Dynkin-system operations, then the theorem promotes it automatically to the whole sigma-algebra.
- pi-lambda theorem / example families: half-lines $(-\infty,t]$, half-open intervals $[a,b)$, rectangles, cylinder sets ::@:: These are typical generating pi-systems; the theorem upgrades a property checked on those basic sets to the whole sigma-algebra they generate.

#### proof via compatibility classes

For theorem $\Rightarrow$ equality, take $\mathcal{D}=\delta(\mathcal{E})$. Since $\mathcal{E}\subseteq\delta(\mathcal{E})$ and $\delta(\mathcal{E})$ is a Dynkin system by definition, the pi-lambda theorem gives $\sigma(\mathcal{E})\subseteq\delta(\mathcal{E})$. The reverse inclusion $\delta(\mathcal{E})\subseteq\sigma(\mathcal{E})$ always holds, so equality follows.

For equality $\Rightarrow$ theorem, assume $\delta(\mathcal{E})=\sigma(\mathcal{E})$ for every pi-system $\mathcal{E}$. If $\mathcal{D}$ is a Dynkin system containing $\mathcal{E}$, then minimality of the generated Dynkin system gives $\delta(\mathcal{E})\subseteq\mathcal{D}$. Replacing $\delta(\mathcal{E})$ by $\sigma(\mathcal{E})$ using the assumed equality yields $\sigma(\mathcal{E})\subseteq\mathcal{D}$, which is exactly the pi-lambda theorem.

The strategy is elegant. Since $\delta(\mathcal{E})\subseteq\sigma(\mathcal{E})$ always holds, it is enough to show that $\delta(\mathcal{E})$ is actually a sigma-algebra. By the earlier proposition, that reduces to proving that $\delta(\mathcal{E})$ is closed under finite intersections.

The most natural way to organize the proof is to turn “intersects well with a fixed set” into a property of sets. For a fixed subset $S\subseteq\Omega$, define $\Gamma(S):=\{A\subseteq\Omega:A\cap S\in\delta(\mathcal{E})\}$.

So $\Gamma(S)$ is the class of all sets that are _compatible_ with the fixed test set $S$. This is the right construction because the target statement has the form “for every relevant left-hand set $A$, the intersection $A\cap S$ stays inside $\delta(\mathcal{E})$.” Instead of proving that separately for each $A$, we package all successful left-hand sets into one class and try to show that this whole class is a Dynkin system. If we succeed and the class contains the generators, then minimality of $\delta(\mathcal{E})$ forces $\delta(\mathcal{E})\subseteq\Gamma(S)$. In this formulation, the method upgrades the _left-hand side_ of the intersection from generators to all of $\delta(\mathcal{E})$, while the chosen test set $S$ stays fixed.

The method itself is not asymmetric, however. If we wanted, we could reverse the roles and define a class of admissible _test sets_ for a fixed left-hand set. Then minimality would upgrade the right-hand side instead. So the real choice is not “which side is upgradable in principle?”, but “which side do we choose to encode into the compatibility class at this stage of the proof?”

That observation explains the whole two-step proof. In step 1 the best possible choice is to put a generator on the right, say $S=G\in\mathcal{E}$. Then for every generator $E\in\mathcal{E}$ we already know $E\cap G\in\mathcal{E}$ by the pi-system property, so the generators lie inside $\Gamma(G)$. Minimality can therefore upgrade the left-hand slot from “generator” to “arbitrary element of $\delta(\mathcal{E})$ ”, while the right-hand slot is still just the chosen generator $G$. Thus step 1 proves the strongest statement available at that stage: any generated set may appear on the left, but on the right we can only guarantee generators.

Step 2 is then chosen to upgrade the other side. After step 1, every generated set already intersects correctly with every generator. So if we now fix an arbitrary $H\in\delta(\mathcal{E})$ as the test set on the right, the generators satisfy $H\cap G\in\delta(\mathcal{E})$ for every $G\in\mathcal{E}$, which means exactly that $\mathcal{E}\subseteq\Gamma(H)$. Minimality can now be used once more, so the left-hand slot is upgraded again to an arbitrary element of $\delta(\mathcal{E})$. Since $H$ itself was arbitrary, the right-hand slot has also been upgraded from “generator” to “arbitrary element of $\delta(\mathcal{E})$ ”.

So the overarching intuition is: step 1 upgrades _generator intersect generator_ to _generated set intersect generator_; step 2 upgrades that to _generated set intersect generated set_. The two steps are not repetitive. They upgrade the two sides of the intersection one at a time. In the way we have written the proof, step 1 uses a compatibility class that upgrades the left-hand side, and then step 2 changes the chosen test set so that the right-hand side is upgraded as well. One could formulate the same method with the roles reversed, but the present orientation makes the bootstrap especially transparent.

This also makes clear why one cannot jump directly to step 2. If one starts with an arbitrary $H\in\delta(\mathcal{E})$ and defines $\Gamma(H)$ immediately, then to use minimality one must prove $\mathcal{E}\subseteq\Gamma(H)$, i.e. $H\cap G\in\delta(\mathcal{E})$ for every generator $G\in\mathcal{E}$. But that is exactly the missing statement. At the start we know only that $\delta(\mathcal{E})$ is a Dynkin system, not that it is closed under intersections with arbitrary $H$. Step 1 is what manufactures this missing input.

Now carry this out.

First fix a generator $G\in\mathcal{E}$ and consider $\Gamma(G)=\{A\subseteq\Omega:A\cap G\in\delta(\mathcal{E})\}$. This is a Dynkin system: $\Omega\in\Gamma(G)$ because $\Omega\cap G=G\in\mathcal{E}\subseteq\delta(\mathcal{E})$; if $A\in\Gamma(G)$, then $A^c\cap G=G\setminus(A\cap G)\in\delta(\mathcal{E})$, because $A\cap G\in\delta(\mathcal{E})$, the set $G$ itself is in $\delta(\mathcal{E})$, and Dynkin systems are closed under nested differences; and if $(A_n)$ are pairwise disjoint members of $\Gamma(G)$, then $(A_n\cap G)$ are pairwise disjoint members of $\delta(\mathcal{E})$, so $(\bigcup_{n=1}^{\infty}A_n)\cap G=\bigcup_{n=1}^{\infty}(A_n\cap G)\in\delta(\mathcal{E})$.

It is worth making the logic of those three checks completely explicit. The condition $\Omega\in\Gamma(G)$ handles the “whole space” axiom. The identity $A^c\cap G=G\setminus(A\cap G)$ is exactly what makes complements manageable: once we know $A\cap G$ is already in $\delta(\mathcal{E})$, intersecting the complement $A^c$ with $G$ just removes that old piece from $G$. Finally, disjointness is preserved after intersecting with a fixed set $G$, so the disjoint-union axiom of a Dynkin system applies directly to the family $(A_n\cap G)$.

Moreover, $\mathcal{E}\subseteq\Gamma(G)$ because $\mathcal{E}$ is a pi-system: for every generator $E\in\mathcal{E}$, one has $E\cap G\in\mathcal{E}\subseteq\delta(\mathcal{E})$. Since $\Gamma(G)$ is a Dynkin system containing $\mathcal{E}$, minimality gives $\delta(\mathcal{E})\subseteq\Gamma(G)$. So every set in $\delta(\mathcal{E})$ intersects well with every generator $G\in\mathcal{E}$.

Next fix an arbitrary generated set $H\in\delta(\mathcal{E})$ and consider the same construction, namely $\Gamma(H)=\{B\subseteq\Omega:H\cap B\in\delta(\mathcal{E})\}$.

Again $\Gamma(H)$ is a Dynkin system by the same three checks as above. The new point is to prove that it contains the generators. But this is exactly what the first step already gave: if $G\in\mathcal{E}$, then $H\cap G\in\delta(\mathcal{E})$. Hence $\mathcal{E}\subseteq\Gamma(H)$. Minimality of $\delta(\mathcal{E})$ therefore yields $\delta(\mathcal{E})\subseteq\Gamma(H)$. In particular, every $B\in\delta(\mathcal{E})$ satisfies $H\cap B\in\delta(\mathcal{E})$.

Here the important point is that no new ingenuity is needed in the second step: the same Dynkin-system verification is reused verbatim. What changes is only the reason why the generators lie inside the compatibility class. For $\Gamma(G)$ this came from the pi-system property $E\cap G\in\mathcal{E}$. For $\Gamma(H)$ it comes from the output of step 1, namely that every generated set—and therefore in particular $H$ —already intersects correctly with every generator. So step 1 does not directly upgrade the right-hand side by minimality; rather, it proves that an arbitrary generated set may now be used as a valid future test set on the right, which is precisely the missing input needed to start step 2.

Since $H\in\delta(\mathcal{E})$ was arbitrary, we conclude that any two sets in $\delta(\mathcal{E})$ have their intersection in $\delta(\mathcal{E})$. So $\delta(\mathcal{E})$ is intersection-stable.

Now $\delta(\mathcal{E})$ is both a Dynkin system and a pi-system, so by Proposition 4.15 it is a sigma-algebra. Because it contains $\mathcal{E}$, minimality of $\sigma(\mathcal{E})$ gives $\sigma(\mathcal{E})\subseteq\delta(\mathcal{E})$, and together with the reverse inclusion we obtain $\delta(\mathcal{E})=\sigma(\mathcal{E})$.

---

Flashcards for this section are as follows:

- proof via compatibility classes / equivalence proof ::@:: The statement that a pi-system $\mathcal{E}$ and a Dynkin system $\mathcal{D}\supseteq\mathcal{E}$ must satisfy $\sigma(\mathcal{E})\subseteq\mathcal{D}$ is equivalent to $\delta(\mathcal{E})=\sigma(\mathcal{E})$; theorem $\Rightarrow$ equality comes from taking $\mathcal{D}=\delta(\mathcal{E})$, and equality $\Rightarrow$ theorem comes from using minimality of $\delta(\mathcal{E})$ inside any Dynkin system $\mathcal{D}$ that contains $\mathcal{E}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof via compatibility classes / proof strategy ::@:: To prove Dynkin's pi-lambda theorem, it is enough to show that $\delta(\mathcal{E})$ is a sigma-algebra; by the criterion “Dynkin system + pi-system = sigma-algebra”, this reduces to proving that $\delta(\mathcal{E})$ is intersection-stable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof via compatibility classes
  - proof via compatibility classes / compatibility-class idea ::@:: To prove $\delta(\mathcal{E})$ is closed under intersections, fix one test set $S$ and look at the class $\Gamma(S)=\{A\subseteq\Omega:A\cap S\in\delta(\mathcal{E})\}$. If this class is a Dynkin system containing $\mathcal{E}$, then minimality forces $\delta(\mathcal{E})\subseteq\Gamma(S)$, meaning every generated set intersects well with the chosen test set $S$. Another possible upgrade mechanism is to keep the same kind of class but replace the test set itself by a larger one; step 2 does exactly that when it moves from a generator $G$ to an arbitrary $H\in\delta(\mathcal{E})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - proof via compatibility classes / why $\Gamma(S)$ is built this way ::@:: The point is to package the target statement “ $A\cap S\in\delta(\mathcal{E})$ ” into a membership test. Then one can try to prove this whole class is a Dynkin system containing the generators, and minimality upgrades the side that has been encoded into the class. In the present proof, that encoded side is the left-hand factor $A$, while the test set $S$ is held fixed. But there is another way to enlarge what is allowed: keep the same class orientation and change the test set itself. That is exactly what step 2 does when it replaces the generator $G$ by an arbitrary $H\in\delta(\mathcal{E})$.
  - proof via compatibility classes / overarching intuition ::@:: The two-step proof upgrades the two sides of the intersection one at a time. Step 1 proves “generated set intersect generator”, and step 2 upgrades this to “generated set intersect generated set”. The compatibility-class method is flexible: it can be set up to upgrade either the left-hand factor or the collection of test sets, depending on which side is encoded into the class. In this proof we keep the same compatibility-class orientation and change the chosen test set between the two steps.
  - proof via compatibility classes / why the test set in step 1 is a generator ::@:: In step 1 the right-hand test set is chosen to be a generator $G\in\mathcal{E}$ because then every generator $E\in\mathcal{E}$ satisfies $E\cap G\in\mathcal{E}$ by the pi-system property. This is exactly what is needed to show $\mathcal{E}\subseteq\Gamma(G)$ and let minimality upgrade the left-hand side to all of $\delta(\mathcal{E})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - proof via compatibility classes / step 1 with generator $G$ ::@:: First take the test set to be a generator $G\in\mathcal{E}$. The class $\Gamma(G)=\{A:A\cap G\in\delta(\mathcal{E})\}$ is a Dynkin system, and because $\mathcal{E}$ is a pi-system every generator $E\in\mathcal{E}$ satisfies $E\cap G\in\mathcal{E}\subseteq\delta(\mathcal{E})$. Hence $\mathcal{E}\subseteq\Gamma(G)$, so minimality gives $\delta(\mathcal{E})\subseteq\Gamma(G)$. Conclusion: every generated set intersects well with every generator.
  - proof via compatibility classes / why $\Gamma(G)$ contains $\Omega$ ::@:: For the fixed generator $G$, one has $\Omega\cap G=G\in\mathcal{E}\subseteq\delta(\mathcal{E})$, so $\Omega\in\Gamma(G)$.
  - proof via compatibility classes / why $\Gamma(G)$ is closed under complements ::@:: If $A\in\Gamma(G)$, then $A\cap G\in\delta(\mathcal{E})$. Hence $A^c\cap G=G\setminus(A\cap G)\in\delta(\mathcal{E})$ because $G\in\delta(\mathcal{E})$ and Dynkin systems are closed under nested differences, so $A^c\in\Gamma(G)$.
  - proof via compatibility classes / why $\Gamma(G)$ is closed under countable disjoint unions ::@:: If $(A_n)$ are pairwise disjoint members of $\Gamma(G)$, then $(A_n\cap G)$ are still pairwise disjoint members of $\delta(\mathcal{E})$, and $(\bigcup_n A_n)\cap G=\bigcup_n(A_n\cap G)$ lies in $\delta(\mathcal{E})$ by the Dynkin-system disjoint-union axiom.
  - proof via compatibility classes / what step 1 achieves ::@:: Step 1 proves the strongest statement available at that moment: the left-hand side of the intersection may now be any element of $\delta(\mathcal{E})$, but the right-hand side is still only a generator. That is exactly “generated set intersect generator”. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - proof via compatibility classes / why the test set in step 2 is arbitrary $H\in\delta(\mathcal{E})$ ::@:: After step 1, every generated set already intersects correctly with every generator. So if we now put an arbitrary $H\in\delta(\mathcal{E})$ on the right, the generators satisfy $H\cap G\in\delta(\mathcal{E})$ for all $G\in\mathcal{E}$, which is exactly the input needed to show $\mathcal{E}\subseteq\Gamma(H)$ and use minimality again.
  - proof via compatibility classes / step 2 with arbitrary $H$ ::@:: Now take the test set to be an arbitrary $H\in\delta(\mathcal{E})$. The same construction gives a Dynkin system $\Gamma(H)=\{B:H\cap B\in\delta(\mathcal{E})\}$. Step 1 already tells us that every generator $G\in\mathcal{E}$ satisfies $H\cap G\in\delta(\mathcal{E})$, so $\mathcal{E}\subseteq\Gamma(H)$. Minimality then gives $\delta(\mathcal{E})\subseteq\Gamma(H)$, hence $H\cap B\in\delta(\mathcal{E})$ for every $B\in\delta(\mathcal{E})$.
  - proof via compatibility classes / why step 2 cannot be done directly ::@:: If one starts with an arbitrary $H\in\delta(\mathcal{E})$ and defines $\Gamma(H)$ immediately, minimality can only be used after proving $\mathcal{E}\subseteq\Gamma(H)$, i.e. $H\cap G\in\delta(\mathcal{E})$ for every generator $G\in\mathcal{E}$. But that is exactly the intersection property still missing, because a Dynkin system is not yet known to be closed under intersections. Step 1 supplies precisely this missing input. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - proof via compatibility classes / why $\Gamma(H)$ is a Dynkin system too ::@:: The same three checks used for $\Gamma(G)$ work again for $\Gamma(H)$: $\Omega\cap H=H\in\delta(\mathcal{E})$, complements satisfy $B^c\cap H=H\setminus(B\cap H)$, and disjoint unions satisfy $(\bigcup_n B_n)\cap H=\bigcup_n(B_n\cap H)$. So no new structure is needed; only the reason $\mathcal{E}\subseteq\Gamma(H)$ changes.
  - proof via compatibility classes / what step 2 achieves ::@:: Step 2 upgrades the right-hand side from “generator” to “arbitrary element of $\delta(\mathcal{E})$ ”. Since the left-hand side was already upgraded in step 1, this finishes the proof of “generated set intersect generated set”. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - proof via compatibility classes / why the two steps fit together ::@:: Step 1 first proves “generated set intersect generator”. That does not yet prove the final statement, but it shows that an arbitrary generated set can now serve as a valid test set on the right. Step 2 then keeps the same left-hand-oriented compatibility class but changes the test set from a generator to an arbitrary $H\in\delta(\mathcal{E})$, thereby upgrading the right-hand side as well. So the two steps upgrade the two sides separately and together establish closure under finite intersections. One could equivalently reverse the viewpoint and package admissible test sets instead. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof via compatibility classes / why the theorem finishes the proof ::@:: Once $\delta(\mathcal{E})$ is shown to be intersection-stable, it is both a Dynkin system and a pi-system, hence a sigma-algebra. Since it contains $\mathcal{E}$, minimality of $\sigma(\mathcal{E})$ gives $\sigma(\mathcal{E})\subseteq\delta(\mathcal{E})$, and together with $\delta(\mathcal{E})\subseteq\sigma(\mathcal{E})$ this yields equality. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### uniqueness from agreement on a generating pi-system

Dynkin's theorem becomes powerful because it gives an easy uniqueness principle for probability measures. Let $\mathcal{E}\subseteq\mathcal{P}(\Omega)$ be a pi-system and let $\mathcal{F}=\sigma(\mathcal{E})$. If two probability measures $P$ and $Q$ agree on every set in $\mathcal{E}$, then they agree on all of $\mathcal{F}$.

The standard proof defines $\mathcal{D}:=\{A\in\mathcal{F}:P[A]=Q[A]\}$.

The intuition is that $\mathcal{D}$ is the class of sets on which the two measures are already indistinguishable. Agreement is hard to verify directly on every set in $\mathcal{F}$, but it is easy to check that this agreement class behaves well under the Dynkin-system operations: probabilities of complements are determined by total mass $1$, and probabilities of pairwise disjoint unions are determined by sigma-additivity. So the pi-lambda theorem exactly fits the situation: prove that the “agreement class” is a Dynkin system, note that it contains the generating pi-system, and then let the theorem enlarge agreement from the test family to the whole generated sigma-algebra.

This class is a Dynkin system. First, $\Omega\in\mathcal{D}$ because $P[\Omega]=Q[\Omega]=1$. Second, if $A\in\mathcal{D}$, then $P[A^c]=1-P[A]=1-Q[A]=Q[A^c]$, so $A^c\in\mathcal{D}$. Third, if $(A_n)$ are pairwise disjoint members of $\mathcal{D}$, then sigma-additivity of both measures gives $P\big[\bigcup_{n=1}^{\infty}A_n\big]=\sum_{n=1}^{\infty}P[A_n]=\sum_{n=1}^{\infty}Q[A_n]=Q\big[\bigcup_{n=1}^{\infty}A_n\big]$, so $\bigcup_n A_n\in\mathcal{D}$. Thus $\mathcal{D}$ is indeed a Dynkin system.

Because $P$ and $Q$ agree on $\mathcal{E}$ by assumption, we have $\mathcal{E}\subseteq\mathcal{D}$. Dynkin's pi-lambda theorem therefore yields $\sigma(\mathcal{E})\subseteq\mathcal{D}$. Since $\mathcal{D}\subseteq\mathcal{F}=\sigma(\mathcal{E})$ by definition, we conclude that $\mathcal{D}=\mathcal{F}$. In other words, agreement on the small generating pi-system already forces agreement on the whole sigma-algebra.

This is exactly the uniqueness mechanism used for continuous distributions with densities and later for probability laws described by cumulative distribution functions: one first checks agreement on a convenient generating pi-system, such as half-open intervals or left half-lines, and then extends the equality to all Borel sets.

For example, suppose $P$ and $Q$ are probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ and you can show that $P[(-\infty,t]]=Q[(-\infty,t]]$ for every $t\in\mathbb{R}$. The half-lines $(-\infty,t]$ form a pi-system and generate $\mathcal{B}(\mathbb{R})$, so the theorem implies $P=Q$ on every Borel set. This is why equality of cumulative distribution functions implies equality of the corresponding probability laws.

---

Flashcards for this section are as follows:

- uniqueness from a generating pi-system ::@:: If $\mathcal{E}$ is a pi-system, $\mathcal{F}=\sigma(\mathcal{E})$, and two probability measures $P,Q$ agree on every set in $\mathcal{E}$, then $P$ and $Q$ agree on all of $\mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- defining the comparison class ::@:: To prove uniqueness, define $\mathcal{D}=\{A\in\mathcal{F}:P[A]=Q[A]\}$ and show that $\mathcal{D}$ is a Dynkin system containing the generating pi-system $\mathcal{E}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- uniqueness from a generating pi-system / proof intuition ::@:: The key idea is to collect all sets on which the two measures already agree. This agreement class is easy to prove is a Dynkin system because complements preserve equality through $1-P[A]$ and disjoint unions preserve equality through sigma-additivity; then the pi-lambda theorem expands agreement from the small generating pi-system to the whole sigma-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $\mathcal{D}$ is a Dynkin system ::@:: The class $\mathcal{D}=\{A\in\mathcal{F}:P[A]=Q[A]\}$ contains $\Omega$ because both measures give it probability $1$, is closed under complements because $P[A^c]=1-P[A]=1-Q[A]=Q[A^c]$, and is closed under countable disjoint unions by sigma-additivity of both measures.
- how Dynkin's theorem gives uniqueness ::@:: Since $\mathcal{E}\subseteq\mathcal{D}$ and $\mathcal{D}$ is a Dynkin system, Dynkin's pi-lambda theorem gives $\sigma(\mathcal{E})\subseteq\mathcal{D}$. Because $\mathcal{D}\subseteq\sigma(\mathcal{E})$ by definition, it follows that $\mathcal{D}=\sigma(\mathcal{E})$, so $P=Q$ on the whole sigma-algebra. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- uniqueness from half-lines example ::@:: If two probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ agree on every half-line $(-\infty,t]$, then they agree on all Borel sets, because the half-lines form a generating pi-system. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
