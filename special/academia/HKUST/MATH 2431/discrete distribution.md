---
aliases:
  - discrete distribution
  - discrete distributions
  - probability mass function
  - probability mass functions
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/discrete_distribution
  - language/in/English
---

# discrete distribution

A discrete distribution is a probability measure on a countable sample space. In that setting every event probability is assembled from the masses of single outcomes, so specifying the measure is equivalent to specifying its probability mass function. The named laws in this chapter—uniform, Bernoulli, binomial, geometric, hypergeometric, and Poisson—are all special cases of this countable-space framework.

More precisely, on a countable sample space $\Omega$, the space of discrete probability measures is in bijection with the space of probability mass functions $p\colon\Omega\to[0,1]$ satisfying $\sum_{\omega\in\Omega}p(\omega)=1$. The forward map sends a measure $P$ to its singleton masses $p_P(\omega)=P[\{\omega\}]$. The reverse map sends such a function $p$ to the set function $P_p[A]=\sum_{\omega\in A}p(\omega)$.

The derivation is very concrete. If $P$ is already given and $A\subseteq\Omega$ is finite, say $A=\{\omega_1,\ldots,\omega_m\}$, then the singleton sets are pairwise disjoint and

$P[A]=\sum_{j=1}^m P[\{\omega_j\}]=\sum_{j=1}^m p_P(\omega_j)$.

If $A$ is infinite countable, write $A=\{\omega_1,\omega_2,\ldots\}$. Then $A=\bigcup_{j=1}^{\infty}\{\omega_j\}$ is a disjoint union, so $\sigma$-additivity gives

$P[A]=\sum_{j=1}^{\infty}P[\{\omega_j\}]=\sum_{j=1}^{\infty}p_P(\omega_j)$.

Thus the measure is completely recovered from its point masses. Conversely, if we start from a PMF $p$, then $P_p[A]=\sum_{\omega\in A}p(\omega)$ is automatically nonnegative, satisfies $P_p[\Omega]=1$, and is countably additive because disjoint unions just group together disjoint collections of singleton masses. These two constructions are inverse: $P_{p_P}=P$, and the PMF of $P_p$ is exactly $p$ because $P_p[\{\omega\}]=p(\omega)$.

---

Flashcards for this section are as follows:

- discrete distribution / overview ::@:: A discrete distribution is a probability measure on a countable sample space; specifying the measure is equivalent to specifying the singleton masses $p(\omega)=P[\{\omega\}]$, and the main named examples are the discrete uniform, Bernoulli, binomial, geometric, hypergeometric, and Poisson laws. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,270-->

## countable sample spaces and sums

A set $\Omega$ is countable if it is empty or there exists a surjective map $\rho \colon \mathbb{N} \to \Omega$; in particular every finite set is countable. When $\Omega$ is countable and $f \colon \Omega \to [0,\infty)$, we define the sum over $\Omega$ by $\sum_{\omega\in\Omega} f(\omega) = \sup_{F\subseteq\Omega,\,F\text{ finite}} \sum_{\omega\in F} f(\omega)$. This agrees with the usual finite sum when $\Omega$ has finitely many elements.

If $\Omega$ is infinite countable and we choose an enumeration $\Omega = \{\omega_1,\omega_2,\ldots\}$, then the same quantity can be written as $\sum_{\omega\in\Omega} f(\omega) = \sum_{j=1}^{\infty} f(\omega_j) = \lim_{N\to\infty}\sum_{j=1}^N f(\omega_j)$. The motivation is practical: once a set is countable, we want to turn an abstract sum over outcomes into an ordinary series that can actually be computed or estimated. The intuition is that a countable set can be visited one point at a time, so for a nonnegative function we may keep adding contributions without ever having to subtract previous ones. The partial sums are increasing, hence the limit exists in $[0,\infty]$, and because all terms are nonnegative the final value does not depend on the chosen enumeration. This is the version we use in practice when summing a probability mass function over a countable state space: we list the states and add their masses one by one.

More generally, if $\Omega = \bigcup_{j=1}^{\infty} A_j$ with pairwise disjoint $A_j$, then the rearrangement theorem gives $\sum_{\omega\in\Omega} f(\omega) = \sum_{j=1}^{\infty}\sum_{\omega\in A_j} f(\omega)$. The motivation here is compression: if many outcomes belong to the same natural class, it is far more efficient to sum class by class than outcome by outcome. The intuition is that the disjoint sets $A_j$ form blocks of outcomes, so we may first total the contribution of each block and then add the block totals. This is especially useful when many outcomes share a common description: for example, in the binomial model one groups strings in $\{0,1\}^n$ by their number of successes, so each block contains exactly $\binom{n}{k}$ strings with $k$ successes and the same probability $p^k(1-p)^{n-k}$. In the proof that a probability mass function defines a measure, one groups outcomes according to which disjoint event $A_j$ they belong to. Rearrangement is valid precisely because the terms are nonnegative and the blocks are disjoint, so no mass is lost or counted twice.

---

Flashcards for this section are as follows:

- countable set ::@:: A set $\Omega$ is countable if it is empty or there exists a surjective map $\rho\colon\mathbb{N}\to\Omega$; in particular every finite set is countable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,282-->
- sum over countable set ::@:: For countable $\Omega$ and a nonnegative function $f\colon\Omega\to[0,\infty)$, define $\sum_{\omega\in\Omega} f(\omega)$ as the supremum of the finite partial sums $\sum_{\omega\in F} f(\omega)$ over finite $F\subseteq\Omega$; this gives a well-defined value in $[0,\infty]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- finite consistency ::@:: If $\Omega=\{\omega_1,\ldots,\omega_N\}$ is finite and $f\colon\Omega\to[0,\infty)$ is nonnegative, then the countable-set definition reduces to the ordinary finite sum $\sum_{\omega\in\Omega} f(\omega)=\sum_{i=1}^N f(\omega_i)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- enumeration formula ::@:: If $\Omega=\{\omega_1,\omega_2,\ldots\}$ is infinite countable and $f\colon\Omega\to[0,\infty)$ is nonnegative, then $\sum_{\omega\in\Omega} f(\omega)=\sum_{j=1}^{\infty} f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^N f(\omega_j)$, and the value does not depend on the chosen enumeration. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,290!2026-04-12,4,270-->
- enumeration formula intuition ::@:: If $\Omega=\{\omega_1,\omega_2,\ldots\}$ is infinite countable and $f\colon\Omega\to[0,\infty)$ is nonnegative, the motivation for the enumeration formula is that it converts an abstract sum over a countable set into an ordinary series we can compute term by term; it works because we can visit the points one by one and keep adding nonnegative terms, so the partial sums only increase and reordering does not change the final total. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- enumeration formula application ::@:: For a probability mass function $p\colon\Omega\to[0,1]$ on a countable state space $\Omega=\{\omega_1,\omega_2,\ldots\}$, the motivation for using the enumeration formula is that probabilities on countable spaces should be computable by listing states; accordingly, it lets us evaluate $\sum_{\omega\in\Omega} p(\omega)$ as $\lim_{N\to\infty}\sum_{j=1}^N p(\omega_j)$ by adding the state masses one by one. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,310-->
- rearrangement theorem ::@:: If $f\colon\Omega\to[0,\infty)$ is nonnegative and $\Omega=\bigcup_{j=1}^{\infty} A_j$ with pairwise disjoint $A_j$, then $\sum_{\omega\in\Omega} f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j} f(\omega)$; a countable sum of nonnegative terms can be rearranged across disjoint blocks. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,282-->
- rearrangement intuition ::@:: If $f\colon\Omega\to[0,\infty)$ is nonnegative and $\Omega$ is partitioned into pairwise disjoint blocks $A_j$, the motivation for rearrangement is that classifying outcomes into natural groups is often easier than summing them one by one; the theorem says we may first total the contribution inside each block and then add the block totals, with disjointness preventing double counting and nonnegativity preventing cancellation issues. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- rearrangement application ::@:: If $f\colon\Omega\to[0,\infty)$ is nonnegative and $\Omega=\bigcup_{j=1}^{\infty} A_j$ with pairwise disjoint $A_j$, the motivation for using rearrangement is that probability arguments often organize outcomes by type; for example, it is what makes $P[\bigcup_j A_j]=\sum_j P[A_j]$ work for a measure built from a probability mass function, because one groups the singleton masses according to which disjoint event $A_j$ contains each outcome. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,282!2026-04-12,4,270-->
- rearrangement and binomial grouping ::@:: In the binomial model on $\{0,1\}^n$, rearrangement groups all outcome strings with the same number of successes into one block $E_k$. Each block has $\binom{n}{k}$ strings, all with probability $p^k(1-p)^{n-k}$, so the long sum over $2^n$ strings becomes a shorter sum $\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k}$. This is why the binomial mass function has the combinatorial coefficient. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->

## probability mass functions

Let $(\Omega, \mathcal{P}(\Omega), P)$ be a probability space with countable sample space $\Omega$. Then $P$ is called a _discrete distribution_, and its _probability mass function_ is the map $p \colon \Omega \to [0,1]$ defined by $p(\omega)=P[\{\omega\}]$. The mass function is uniquely determined by the measure, because once we know the probability of every singleton, we can recover the probability of any event by adding the singleton masses over that event.

Conversely, suppose we begin not with a probability measure but with a function $p\colon\Omega\to[0,1]$ satisfying $\sum_{\omega\in\Omega} p(\omega)=1$. The motivation for this construction is that in discrete models we often know the weight of each individual outcome first, so we want a systematic way to turn those point weights into a full probability measure on all subsets of $\Omega$. Define $P[A]=\sum_{\omega\in A} p(\omega)$ for $A\subseteq\Omega$. Then $P$ is a probability measure on $(\Omega,\mathcal{P}(\Omega))$: normalization is immediate from $P[\Omega]=\sum_{\omega\in\Omega} p(\omega)=1$, and if $(A_j)_{j\in\mathbb{N}}$ are pairwise disjoint, then the rearrangement theorem turns $P[\bigcup_j A_j] = \sum_{\omega\in\bigcup_j A_j} p(\omega)$ into $\sum_j\sum_{\omega\in A_j} p(\omega)=\sum_j P[A_j]$. So the single condition "nonnegative and sums to $1$ " is exactly what is needed to promote a function on points into a probability measure on all events.

After this construction, the original function $p$ can be identified with the probability mass function of the newly created measure, because for every $\omega\in\Omega$ we have $P[\{\omega\}] = \sum_{\omega'\in\{\omega\}} p(\omega') = p(\omega)$. Thus there is no difference between "the function we started with" and "the PMF of the measure we constructed": they are literally the same function. On a countable sample space, specifying a discrete distribution and specifying its probability mass function are therefore equivalent pieces of data.

In fact this equivalence is bijective at the space level: the space of discrete probability measures on $\Omega$ is in bijection with the space of PMFs. The forward map is $P\mapsto p_P$ with $p_P(\omega)=P[\{\omega\}]$, and the reverse map is $p\mapsto P_p$ with $P_p[A]=\sum_{\omega\in A}p(\omega)$. The derivation of inverse-ness is direct: every event is a disjoint union of singletons, so starting from $P$ we recover it by $P_p[A]=\sum_{\omega\in A}p_P(\omega)=\sum_{\omega\in A}P[\{\omega\}]=P[A]$, while starting from $p$ we recover it on singleton sets by $P_p[\{\omega\}]=p(\omega)$. So composing either way returns the original object.

---

Flashcards for this section are as follows:

- discrete distribution / definition on a countable sample space ::@:: A discrete distribution is a probability measure on $(\Omega,\mathcal{P}(\Omega))$ when the sample space $\Omega$ is countable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->
- probability mass function ::@:: For a discrete distribution, the probability mass function is $p(\omega)=P[\{\omega\}]$; it records the probability assigned to each single outcome. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->
- why singleton masses suffice ::@:: On a countable sample space $\Omega$, the motivation for introducing a probability mass function is that once we know every singleton mass $P[\{\omega\}]$, we can recover the probability of any event $A\subseteq\Omega$ by summing those masses over $\omega\in A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,270!2026-04-12,4,282-->
- pmf determines measure ::@:: If $p\colon\Omega\to[0,1]$ satisfies $\sum_{\omega\in\Omega} p(\omega)=1$, then $P[A]=\sum_{\omega\in A} p(\omega)$ defines a probability measure on $(\Omega,\mathcal{P}(\Omega))$; on a countable sample space the measure is completely determined by singleton masses. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,297-->
- derivation of the bijection between discrete probability measures and PMFs ::@:: On countable $\Omega$, the forward map is $P\mapsto p_P$ with $p_P(\omega)=P[\{\omega\}]$, and the reverse map is $p\mapsto P_p$ with $P_p(A)=\sum_{\omega\in A}p(\omega)$. The key point is that every event is a disjoint union of singleton sets, so $\sigma$-additivity turns the measure into a sum of singleton masses, while $P_p[\{\omega\}]=p(\omega)$ recovers the original PMF. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->
- motivation for constructing P from p ::@:: If $p\colon\Omega\to[0,1]$ satisfies $\sum_{\omega\in\Omega} p(\omega)=1$, the motivation for defining $P[A]=\sum_{\omega\in A}p(\omega)$ is that in a discrete model we often know the weight of each single outcome first and need a canonical way to turn those point weights into probabilities of arbitrary events. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,297-->
- sums to unity gives normalization ::@:: If $p\colon\Omega\to[0,1]$ satisfies $\sum_{\omega\in\Omega} p(\omega)=1$ and we define $P[A]=\sum_{\omega\in A}p(\omega)$, then $P[\Omega]=1$ automatically, because $P[\Omega]=\sum_{\omega\in\Omega}p(\omega)=1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,282!2026-04-12,4,270-->
- why sigma-additivity holds ::@:: For pairwise disjoint $(A_j)$, the union $\bigcup_j A_j$ is a disjoint decomposition, so the rearrangement theorem gives $P[\bigcup_j A_j]=\sum_{\omega\in\bigcup_j A_j}p(\omega)=\sum_j\sum_{\omega\in A_j}p(\omega)=\sum_j P[A_j]$; this is the key proof idea for $\sigma$-additivity. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- original function equals pmf of constructed measure ::@:: If $p\colon\Omega\to[0,1]$ satisfies $\sum_{\omega\in\Omega} p(\omega)=1$ and $P[A]=\sum_{\omega\in A}p(\omega)$, then the probability mass function of $P$ is exactly the original function $p$, because $P[\{\omega\}]=p(\omega)$ for every $\omega\in\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->

## named distributions

The standard named discrete laws differ mainly by the sampling mechanism behind them: the discrete uniform law assigns the same mass to every outcome in a finite set; Bernoulli and binomial laws come from success/failure experiments; geometric laws record waiting for the first success, either by counting failures first or by counting the trial of the first success; the hypergeometric law samples without replacement; and the Poisson law describes counts that can, in principle, be arbitrarily large. Later, random variables will let us pass from complicated underlying sample spaces to these simpler countable state spaces.

---

Flashcards for this section are as follows:

- named laws overview ::@:: The main named discrete laws are discrete uniform (equally likely outcomes), Bernoulli and binomial (success/failure experiments), geometric (waiting for the first success, with two common counting conventions), hypergeometric (sampling without replacement), and Poisson (counts with no fixed upper bound). <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- why named laws simplify models ::@:: Named discrete distributions replace a large underlying experiment space by a smaller state space that keeps only the quantity of interest, such as the number of successes; this reduction in complexity motivates the later study of random variables. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->

### discrete uniform distribution

On a finite set $\Omega$, the discrete uniform distribution assigns equal mass to every point: $p(\omega)=1/|\Omega|$ for all $\omega\in\Omega$. Its interpretation is that the experiment has finitely many possible outcomes and no outcome is favored over any other, as in a fair die roll or a uniformly chosen card from a finite labeled set.

The intuition for the formula is simple symmetry plus normalization. If there are $|\Omega|$ outcomes and each must receive the same probability, then the total mass $1$ must be split evenly into $|\Omega|$ identical pieces, so each piece has size $1/|\Omega|$. In other words, the PMF is forced by the two requirements that all outcomes are equally likely and that the probabilities must sum to $1$.

---

Flashcards for this section are as follows:

- on finite $\Omega$, $p(\omega)=1/|\Omega|$ for every $\omega\in\Omega$ ::@:: This is the discrete uniform distribution on $\Omega$; it models a finite experiment in which every outcome is equally likely. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- discrete uniform interpretation ::@:: The discrete uniform distribution models a finite experiment in which all outcomes are symmetric or equally likely, such as a fair die roll or a uniformly chosen element of a finite set. <!--SR:!2026-04-12,4,310!2026-04-12,4,282-->
- why $p(\omega)=1/|\Omega|$ on finite $\Omega$ ::@:: In a discrete uniform distribution, symmetry makes all point masses equal and normalization forces those $|\Omega|$ equal masses to add up to $1$. <!--SR:!2026-04-12,4,297!2026-04-12,4,310-->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Bernoulli distribution

The Bernoulli distribution $\mathrm{Ber}(p)$ is the two-point law on $\Omega=\{0,1\}$ with $p(1)=p$ and $p(0)=1-p$, where $1$ represents success and $0$ failure. Its interpretation is a single success/failure experiment, such as one toss of a biased coin, one inspection that either passes or fails, or one indicator random variable for whether an event occurs.

The PMF formula is intuitive because there are only two outcomes. Once we decide that the success outcome should have probability $p$, the only remaining probability mass available for failure is $1-p$. So the Bernoulli law is the simplest possible discrete distribution: one parameter fixes the success chance, and normalization automatically determines the failure chance.

---

Flashcards for this section are as follows:

- on $\{0,1\}$, $p(1)=p$ and $p(0)=1-p$ ::@:: This is the Bernoulli distribution $\mathrm{Ber}(p)$; it models a single success/failure experiment. <!--SR:!2026-04-12,4,310!2026-04-12,4,297-->
- Bernoulli interpretation ::@:: A Bernoulli random quantity records one yes/no or success/failure outcome, so it is the natural model for a single trial or for the indicator of an event. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $p(1)=p$ and $p(0)=1-p$ on $\{0,1\}$ ::@:: This PMF has that form because there are only two outcomes: once success is assigned probability $p$, normalization leaves exactly $1-p$ for failure. <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->

### binomial distribution

For $n\in\mathbb{N}$ and $p\in[0,1]$, the binomial distribution $\mathrm{Bin}(n,p)$ is the law on $\{0,1,\ldots,n\}$ with mass function $p(k)=\binom{n}{k}p^k(1-p)^{n-k}$. Its interpretation is the number of successes in $n$ independent Bernoulli trials with common success probability $p$. So instead of remembering the entire ordered success/failure pattern, the binomial law remembers only the total count of successes.

A rigorous way to see this is to work first on the product space $\{0,1\}^n$, where a string $(\omega_1,\ldots,\omega_n)$ records the ordered success/failure pattern and has probability $p^{\sum_j \omega_j}(1-p)^{n-\sum_j \omega_j}$. The event $E_k=\{(\omega_1,\ldots,\omega_n):\sum_{j=1}^n \omega_j=k\}$ consists of all strings with exactly $k$ successes, so $|E_k|=\binom{n}{k}$ and therefore $Q[E_k]=\binom{n}{k}p^k(1-p)^{n-k}$.

The intuition for the PMF formula is that every ordered pattern with exactly $k$ successes has the same probability $p^k(1-p)^{n-k}$, because it contains $k$ success factors and $n-k$ failure factors. The only remaining question is how many such patterns there are, and the answer is $\binom{n}{k}$. So the binomial PMF is "number of admissible patterns" times "probability of one such pattern". For example, the number of sixes in four throws of a fair die has distribution $\mathrm{Bin}(4,1/6)$: we code "six" as success and "not six" as failure. The point of the binomial law is that it lets us work directly on the smaller state space $\{0,1,2,3,4\}$ instead of the much larger pattern space $\{0,1\}^4$.

---

Flashcards for this section are as follows:

- on $\{0,1,\ldots,n\}$, $p(k)=\binom{n}{k}p^k(1-p)^{n-k}$ ::@:: This is the binomial distribution $\mathrm{Bin}(n,p)$; it counts how many successes occur in $n$ independent Bernoulli trials with success probability $p$. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- $X\sim \mathrm{Bin}(n,p)$ ::@:: This means $X$ records the total number of successes in $n$ independent Bernoulli trials, so it forgets the order of the trials and remembers only the success count. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- on $\{0,1\}^n$, $Q[(\omega_1,\ldots,\omega_n)]=p^{\sum_j \omega_j}(1-p)^{n-\sum_j \omega_j}$ ::@:: This is the ordered Bernoulli-trial model underlying the binomial law: each string records the full success/failure pattern, and grouping strings by total successes produces $\mathrm{Bin}(n,p)$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $E_k=\{(\omega_1,\ldots,\omega_n):\sum_{j=1}^n \omega_j=k\}$ and $|E_k|=\binom{n}{k}$ ::@:: Therefore $Q[E_k]=\binom{n}{k}p^k(1-p)^{n-k}$; there are $\binom{n}{k}$ ordered patterns with exactly $k$ successes. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $\binom{n}{k}p^k(1-p)^{n-k}$ ::@:: This binomial PMF equals "number of success/failure patterns with exactly $k$ successes" times "probability of one such pattern": there are $\binom{n}{k}$ such patterns, and each has probability $p^k(1-p)^{n-k}$. <!--SR:!2026-04-12,4,297!2026-04-12,4,310-->
- if $X$ is the number of sixes in four throws of a fair die ::@:: Then $X\sim \mathrm{Bin}(4,1/6)$, because each throw is a Bernoulli experiment with success = "a six appears". <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $\{0,1,\ldots,n\}$ versus $\{0,1\}^n$ when only the success count matters ::@:: The smaller state space is more efficient than the full pattern space, and this kind of reduction in complexity motivates the later use of random variables. <!--SR:!2026-04-12,4,290!2026-04-12,4,310-->

### geometric distribution

There are two common geometric conventions, and both come from repeated independent Bernoulli trials with success probability $p\in(0,1)$. One version is supported on $\mathbb{N}_0=\{0,1,2,\ldots\}$ and counts the number of failures before the first success; if we call this random variable $X$, then $P[X=k]=(1-p)^k p$ for $k\in\mathbb{N}_0$. Another version is supported on $\mathbb{N}=\{1,2,3,\ldots\}$ and counts the trial number of the first success; if we call this random variable $Y$, then $P[Y=k]=(1-p)^{k-1}p$ for $k\in\mathbb{N}$.

The interpretations are different but closely related. The $\mathbb{N}_0$-supported version asks how many failures occur before the first success, whereas the $\mathbb{N}$-supported version asks on which trial the first success occurs. So $X=0$ means immediate success on the first trial, whereas $Y=1$ means exactly the same underlying event described with a different counting convention.

The PMF formulas are intuitive because to get a first success at a specified stage, all earlier trials must fail and then the next trial must succeed. For $X=k$, the factor $(1-p)^k p$ corresponds to $k$ failures followed by one success. For $Y=k$, the factor $(1-p)^{k-1}p$ corresponds to $k-1$ failures followed by success on trial $k$. The two variants are therefore related by the simple shift $Y=X+1$. Many books write both laws as $\mathrm{Geo}(p)$, so one must always check which support and interpretation are intended.

---

Flashcards for this section are as follows:

- $P[X=k]=(1-p)^k p$ for $k\in\mathbb{N}_0$ ::@:: This is the geometric convention supported on $\mathbb{N}_0$; it counts the number of failures before the first success. <!--SR:!2026-04-12,4,310!2026-04-12,4,282-->
- $P[Y=k]=(1-p)^{k-1}p$ for $k\in\mathbb{N}$ ::@:: This is the geometric convention supported on $\mathbb{N}$; it counts the trial number of the first success. <!--SR:!2026-04-12,4,290!2026-04-12,4,282-->
- $X\in\mathbb{N}_0$ counts failures before first success, while $Y\in\mathbb{N}$ counts the first-success trial ::@:: These are the two common geometric interpretations; they describe the same experiment using different counting conventions. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- why $(1-p)^k p$ on $\mathbb{N}_0$ and $(1-p)^{k-1}p$ on $\mathbb{N}$ ::@:: In either geometric convention, the PMF comes from a run of failures followed by the first success: $(1-p)^k p$ corresponds to $k$ failures followed by success, and $(1-p)^{k-1}p$ corresponds to $k-1$ failures followed by success on trial $k$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $Y=X+1$ ::@:: If $X$ counts failures before the first success and $Y$ counts the trial number of the first success, then the two geometric conventions differ only by this shift of $1$. <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->
- $\mathrm{Geo}(p)$ with support $\mathbb{N}_0$ versus support $\mathbb{N}$ ::@:: Different books use this notation for different geometric conventions, so one must check whether it counts failures before the first success or the trial number of the first success. <!--SR:!2026-04-12,4,310!2026-04-12,4,297-->

### hypergeometric distribution

For integers $N,M,n\in\mathbb{N}$ with $0\le n,M\le N$, the hypergeometric distribution $\mathrm{H}(N,M,n)$ is the law on $\{0,1,\ldots,n\}$ given by $p(k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$. Its interpretation is the number of favorable items in an unordered sample of size $n$ drawn uniformly without replacement from a population of size $N$ containing $M$ favorable items.

The intuition for the PMF formula is purely combinatorial. To get exactly $k$ favorable items in the sample, we must choose $k$ objects from the $M$ favorable ones and $n-k$ objects from the $N-M$ unfavorable ones. That gives $\binom{M}{k}\binom{N-M}{n-k}$ admissible samples. Since every sample of size $n$ is equally likely and there are $\binom{N}{n}$ of them in total, the probability is the ratio of favorable samples to all samples. This is the discrete law naturally attached to sampling without replacement.

A fundamental asymptotic link with the binomial law is the hypergeometric approximation to binomial. Suppose $n$ is fixed and we have a sequence $M_N$ with $0\le M_N\le N$ and $M_N/N\to p\in[0,1]$. If $X_N\sim \mathrm{H}(N,M_N,n)$, then for each fixed $k\in\{0,1,\ldots,n\}$ we have $P[X_N=k]\to \binom{n}{k}p^k(1-p)^{n-k}$ as $N\to\infty$. This says that when the population is very large compared with the sample size, sampling without replacement behaves almost like sampling with replacement, so the hypergeometric law is well approximated by $\mathrm{Bin}(n,p)$.

The intuition is that dependence created by sampling without replacement becomes negligible when the sample is tiny relative to the population. If the favorable fraction is about $p$, then the first draw is favorable with probability about $p$, and after removing one item the composition changes only by about $1/N$. So later draws still look almost like independent Bernoulli trials with success chance about $p$. That is why the without-replacement model approaches the with-replacement binomial model.

To prove the approximation, start from the exact PMF and rewrite it in falling-factorial form: $P[X_N=k]=\dfrac{\binom{M_N}{k}\binom{N-M_N}{n-k}}{\binom{N}{n}}=\binom{n}{k}\dfrac{(M_N)_k\,(N-M_N)_{n-k}}{(N)_n}$, where $(a)_r=a(a-1)\cdots(a-r+1)$ is the falling factorial. Now split the ratio into two products: $P[X_N=k]=\binom{n}{k}\left(\prod_{j=0}^{k-1}\dfrac{M_N-j}{N-j}\right)\left(\prod_{j=0}^{n-k-1}\dfrac{N-M_N-j}{N-k-j}\right)$. Because $n$ and $k$ are fixed, each factor in the first product tends to $p$, so the first product tends to $p^k$. Likewise, each factor in the second product tends to $1-p$, so the second product tends to $(1-p)^{n-k}$. Therefore $P[X_N=k]\to \binom{n}{k}p^k(1-p)^{n-k}$, which is exactly the PMF of $\mathrm{Bin}(n,p)$.

---

Flashcards for this section are as follows:

- $p(k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$ on $\{0,1,\ldots,n\}$ ::@:: This is the hypergeometric distribution $\mathrm{H}(N,M,n)$; it gives the probability of drawing exactly $k$ favorable items when $n$ items are sampled uniformly without replacement from a population of size $N$ containing $M$ favorable ones. <!--SR:!2026-04-12,4,310!2026-04-12,4,297-->
- $X\sim \mathrm{H}(N,M,n)$ ::@:: This means $X$ records how many favorable items appear in a sample of size $n$ drawn uniformly without replacement from a finite population. <!--SR:!2026-04-12,4,310!2026-04-12,4,290-->
- $\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$ ::@:: This hypergeometric probability is a counting ratio: the numerator counts samples with exactly $k$ favorable and $n-k$ unfavorable items, and the denominator counts all samples of size $n$. <!--SR:!2026-04-12,4,290!2026-04-12,4,297-->
- why $p(k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$ in the hypergeometric model ::@:: The PMF is a counting ratio: choose the favorable and unfavorable items separately to count admissible samples, then divide by the total number of samples of size $n$. <!--SR:!2026-04-12,4,310!2026-04-12,4,270-->
- hypergeometric approximation
  - hypergeometric approximation / statement ::@:: If $n$ is fixed, $M_N/N\to p$, and $X_N\sim \mathrm{H}(N,M_N,n)$, then for each fixed $k\in\{0,\ldots,n\}$ one has $P[X_N=k]\to \binom{n}{k}p^k(1-p)^{n-k}$; a large-population hypergeometric law approaches $\mathrm{Bin}(n,p)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
  - hypergeometric approximation / intuition ::@:: (1) Sampling without replacement creates dependence between draws. <br/> (1.1) But if $N$ is huge and $n$ is fixed, the favorable fraction changes only slightly: $M_N/N\approx p$, while after one removal it is still about $(M_N-1)/(N-1)\approx p$. <br/> (1.2) So the successive draw probabilities are all close to $p$ and the count of favorable draws should resemble $\mathrm{Bin}(n,p)$. <br/> (2) Therefore $P[X_N=k]$ should be close to $\binom{n}{k}p^k(1-p)^{n-k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,290!2026-04-12,4,282-->
  - hypergeometric approximation / derivation strategy ::@:: (1) Start from $P[X_N=k]=\dfrac{\binom{M_N}{k}\binom{N-M_N}{n-k}}{\binom{N}{n}}$. <br/> (1.1) Rewrite it as $\binom{n}{k}\dfrac{(M_N)_k(N-M_N)_{n-k}}{(N)_n}$. <br/> (1.2) Then split it into the products $\prod_{j=0}^{k-1}\dfrac{M_N-j}{N-j}$ and $\prod_{j=0}^{n-k-1}\dfrac{N-M_N-j}{N-k-j}$. <br/> (2) Since $n,k$ are fixed and $M_N/N\to p$, these products tend to $p^k$ and $(1-p)^{n-k}$, giving the binomial PMF. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
  - hypergeometric approximation / exact factorization ::@:: For $X_N\sim \mathrm{H}(N,M_N,n)$, $P[X_N=k]=\binom{n}{k}\dfrac{(M_N)_k(N-M_N)_{n-k}}{(N)_n}=\binom{n}{k}\left(\prod_{j=0}^{k-1}\dfrac{M_N-j}{N-j}\right)\left(\prod_{j=0}^{n-k-1}\dfrac{N-M_N-j}{N-k-j}\right)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,290!2026-04-12,4,297-->
  - hypergeometric approximation / factor limits ::@:: If $M_N/N\to p$ and $n,k$ are fixed, then $\prod_{j=0}^{k-1}\dfrac{M_N-j}{N-j}\to p^k$ and $\prod_{j=0}^{n-k-1}\dfrac{N-M_N-j}{N-k-j}\to (1-p)^{n-k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,282!2026-04-12,4,297-->
  - hypergeometric approximation / full proof ::@:: Combine the exact factorization of $P[X_N=k]$ with the factor limits to obtain $P[X_N=k]\to \binom{n}{k}p^k(1-p)^{n-k}$, which is the PMF of $\mathrm{Bin}(n,p)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,310-->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Poisson distribution

For $\lambda>0$, the Poisson distribution $\mathrm{Pois}(\lambda)$ is the law on $\mathbb{N}_0$ with $p(k)=\dfrac{\lambda^k}{k!}e^{-\lambda}$. Its interpretation is a count of events that may happen any nonnegative number of times in a fixed window, such as the number of goals in a football match or the number of raindrops landing in a region during a fixed time interval.

The PMF formula has two intuitive pieces. The factor $\lambda^k/k!$ is the natural weight for seeing $k$ events when the typical count level is governed by $\lambda$: the power $\lambda^k$ favors larger counts when $\lambda$ is larger, and the division by $k!$ compensates for overcounting the order of $k$ indistinguishable events. The extra factor $e^{-\lambda}$ is the normalization constant. Indeed, the exponential power series says $e^{\lambda}=\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}$, so multiplying by $e^{-\lambda}$ makes the total mass equal to $\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}e^{-\lambda}=e^{-\lambda}e^{\lambda}=1$. This explains exactly why the factor $e^{-\lambda}$ appears in the PMF.

A fundamental asymptotic link with the binomial law is the Poisson approximation: if $p_n=\lambda/n$ and $k\in\mathbb{N}_0$ is fixed, then $\binom{n}{k}p_n^k(1-p_n)^{n-k}\to \frac{\lambda^k}{k!}e^{-\lambda}$ as $n\to\infty$. The intuition for deriving the proof is to rewrite the binomial mass so that the candidate Poisson factors become visible. Under the scaling $p_n=\lambda/n$, each individual trial is a rare event, but the expected number of successes stays fixed at $np_n=\lambda$. So one expects the combinatorial term to behave like $n^k/k!$, the success-probability term to contribute $\lambda^k/n^k$, and the large block of failures to behave like $(1-\lambda/n)^n\approx e^{-\lambda}$.

Now carry this out exactly. For fixed $k$, $\binom{n}{k}p_n^k(1-p_n)^{n-k}=\frac{n!}{k!(n-k)!}\left(\frac{\lambda}{n}\right)^k\left(1-\frac{\lambda}{n}\right)^{n-k}$. Rewriting the factorial ratio as a finite product gives $\binom{n}{k}p_n^k(1-p_n)^{n-k}=\frac{\lambda^k}{k!}\left(\prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right)\right)\left(1-\frac{\lambda}{n}\right)^n\left(1-\frac{\lambda}{n}\right)^{-k}$. Since $k$ is fixed, each factor in the finite product tends to $1$, so the product tends to $1$. Also, $\left(1-\frac{\lambda}{n}\right)^n\to e^{-\lambda}$, and because $\left(1-\frac{\lambda}{n}\right)\to 1$, we also have $\left(1-\frac{\lambda}{n}\right)^{-k}\to 1$. Therefore $\lim_{n\to\infty}\binom{n}{k}p_n^k(1-p_n)^{n-k}=\frac{\lambda^k}{k!}\cdot 1\cdot e^{-\lambda}\cdot 1=\frac{\lambda^k}{k!}e^{-\lambda}$, so a binomial model with many trials and very small success probability but fixed mean $np_n=\lambda$ converges pointwise to the Poisson law.

An independent derivation uses Poisson-process small-time assumptions. Let $P_n(t)=P(N_t=n)$ for a rate-$\lambda$ counting process. From $P(1\text{ jump in }(t,t+h])=\lambda h+o(h)$ and $P(\ge2\text{ jumps in }(t,t+h])=o(h)$, we have $P_0(t+h)=P_0(t)(1-\lambda h)+o(h)$, hence $P_0'(t)=-\lambda P_0(t)$ with $P_0(0)=1$, so $P_0(t)=e^{-\lambda t}$. For $n\ge1$, conditioning on 0 or 1 jump in $(t,t+h]$ gives $P_n(t+h)=P_n(t)(1-\lambda h)+P_{n-1}(t)(\lambda h)+o(h)$, which yields $P_n'(t)=-\lambda P_n(t)+\lambda P_{n-1}(t)$ with $P_n(0)=0$. Solving recursively (induction or integrating factors) gives $P_n(t)=e^{-\lambda t}(\lambda t)^n/n!$ for $n=0,1,2,\dots$, so $N_t\sim\mathrm{Pois}(\lambda t)$.

---

Flashcards for this section are as follows:

- on $\mathbb{N}_0$, $p(k)=\dfrac{\lambda^k}{k!}e^{-\lambda}$ for $\lambda>0$ ::@:: This is the Poisson distribution $\mathrm{Pois}(\lambda)$; it models counts that can in principle be arbitrarily large. <!--SR:!2026-04-12,4,290!2026-04-12,4,297-->
- $X\sim \mathrm{Pois}(\lambda)$ ::@:: This is the natural model for count data such as goals in a football match or raindrops in a region during a time interval, where there is no fixed upper bound on the number of events. <!--SR:!2026-04-12,4,270!2026-04-12,4,310-->
- $\dfrac{\lambda^k}{k!}e^{-\lambda}$ ::@:: In the Poisson PMF, the factor $\lambda^k/k!$ weights the count at value $k$ when the typical count level is $\lambda$, and the factor $e^{-\lambda}$ is the normalization constant that makes the total mass equal to $1$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- $e^{\lambda}=\sum_{k=0}^{\infty}\lambda^k/k!$ ::@:: This exponential power series explains the factor $e^{-\lambda}$ in the Poisson PMF, because multiplying $\lambda^k/k!$ by $e^{-\lambda}$ makes the total probability sum to $e^{-\lambda}e^{\lambda}=1$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- Poisson approximation
  - Poisson approximation / statement ::@:: If $p_n=\lambda/n$ and $k$ is fixed, then $\binom{n}{k}p_n^k(1-p_n)^{n-k}\to\dfrac{\lambda^k}{k!}e^{-\lambda}$ as $n\to\infty$; a rare-event binomial law with fixed mean converges to $\mathrm{Pois}(\lambda)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-12,4,270-->
  - Poisson approximation / intuition ::@:: (1) Set $p_n=\lambda/n$, so each trial is rare but the mean stays fixed: $np_n=\lambda$. <br/> (1.1) For fixed $k$, the success part behaves like $\binom{n}{k}(\lambda/n)^k\approx \lambda^k/k!$. <br/> (1.2) The failure block behaves like $(1-\lambda/n)^n\to e^{-\lambda}$. <br/> (2) So $\binom{n}{k}p_n^k(1-p_n)^{n-k}$ should approach $\dfrac{\lambda^k}{k!}e^{-\lambda}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,282!2026-04-12,4,282-->
  - Poisson approximation / derivation strategy ::@:: (1) Start from $\binom{n}{k}(\lambda/n)^k(1-\lambda/n)^{n-k}$. <br/> (1.1) Rewrite it as $\dfrac{\lambda^k}{k!}\left(\prod_{j=0}^{k-1}(1-j/n)\right)(1-\lambda/n)^n(1-\lambda/n)^{-k}$. <br/> (1.2) Then isolate the three limits: $\prod_{j=0}^{k-1}(1-j/n)\to1$, $(1-\lambda/n)^n\to e^{-\lambda}$, and $(1-\lambda/n)^{-k}\to1$. <br/> (2) Multiplying these limits gives the Poisson PMF. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,290!2026-04-12,4,310-->
  - Poisson approximation / exact factorization ::@:: For fixed $k$ and $p_n=\lambda/n$, one has $\binom{n}{k}p_n^k(1-p_n)^{n-k}=\dfrac{\lambda^k}{k!}\left(\prod_{j=0}^{k-1}\left(1-\dfrac{j}{n}\right)\right)\left(1-\dfrac{\lambda}{n}\right)^n\left(1-\dfrac{\lambda}{n}\right)^{-k}$; this factorization exposes the Poisson limit term by term. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,310!2026-04-11,3,257-->
  - Poisson approximation / factor limits ::@:: In the Poisson approximation proof with fixed $k$, the finite product $\prod_{j=0}^{k-1}(1-j/n)$ tends to $1$, the factor $(1-\lambda/n)^n$ tends to $e^{-\lambda}$, and $(1-\lambda/n)^{-k}$ tends to $1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
  - Poisson approximation / full proof ::@:: Combine the exact factorization with those three limits to obtain $\binom{n}{k}p_n^k(1-p_n)^{n-k}\to\dfrac{\lambda^k}{k!}e^{-\lambda}$, which is the full proof of the Poisson approximation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,310-->
  - Poisson process / small-time ODE derivation ::@:: For $P_n(t)=P(N_t=n)$, small-time assumptions give $P_0'(t)=-\lambda P_0(t)$ and, for $n\ge1$, $P_n'(t)=-\lambda P_n(t)+\lambda P_{n-1}(t)$ with $P_0(0)=1$, $P_n(0)=0$; solving yields $P(N_t=n)=e^{-\lambda t}(\lambda t)^n/n!$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-12,4,297!2026-04-12,4,282-->
