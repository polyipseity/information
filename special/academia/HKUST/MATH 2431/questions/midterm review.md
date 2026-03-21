---
aliases:
    - HKUST MATH 2431 midterm review
    - HKUST MATH2431 midterm review
    - MATH 2431 midterm review
    - MATH2431 midterm review
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/midterm_review
    - language/in/English
---

# midterm review

- HKUST MATH 2431

These prompts cover the material through week 6. They are designed for an honors-style review: some are direct computations, some ask for proof structure, and some test whether the main concepts have become part of your working vocabulary rather than staying as decorative notation. They are review prompts written for this repository and are _not_ part of the official course materials.

## foundational structures

1. Explain why the set of all infinite coin-toss sequences $\{H,T\}^{\mathbb{N}}$ is uncountable, while $\mathbb{N}_0$ is countable. Why does this matter for event collections?
    - solution sketch: $\mathbb{N}_0$ is countable because it is already listed as $0,1,2,\ldots$. The sequence space $\{H,T\}^{\mathbb{N}}$ has continuum cardinality, for example by binary-expansion coding, so it cannot be listed in a sequence. This matters because on countable spaces one can often use the full power set and sum singleton masses, whereas on uncountable spaces one must restrict to a smaller $\sigma$-algebra.

2. Let $\Omega=\{1,2,3,4\}$ and let $\mathcal{E}=\{\{1,2\}\}$. Compute $\sigma(\mathcal{E})$ and explain why no smaller $\sigma$-algebra containing $\{1,2\}$ can exist.
    - solution sketch: $\sigma(\mathcal{E})=\{\emptyset,\{1,2\},\{3,4\},\Omega\}$. Any $\sigma$-algebra containing $\{1,2\}$ must also contain its complement $\{3,4\}$, the empty set, and the whole space, so this four-set family is forced and is already closed under the $\sigma$-algebra operations.

3. Prove that if $\mathcal{F}$ is a $\sigma$-algebra, then it is closed under countable intersections and finite set differences.
    - solution sketch: Countable intersections follow from de Morgan: $\bigcap_j A_j=(\bigcup_j A_j^c)^c$. Finite set differences follow from $A\setminus B=A\cap B^c$, so once complements and intersections are known to stay inside $\mathcal{F}$, differences stay inside too.

## counting and finite probability spaces

1. A password has four symbols: the first two are letters and the last two are digits. Count the number of possible passwords and identify the combinatorial principle being used.
    - solution sketch: There are $26$ choices for each letter position and $10$ choices for each digit position, so the total is $26\cdot26\cdot10\cdot10=67\,600$. The principle is the product rule on a Cartesian-product sample space.

2. Derive the formula $\binom{n+r-1}{r}$ for unordered samples of size $r$ from $n$ symbols with repetition allowed.
    - solution sketch: Encode the multiset by $r$ dots and $n-1$ bars. The number of dots before the first bar records how many copies of symbol $1$ are chosen, the number between successive bars records the copies of the next symbols, and so on. Choosing which $r$ of the $n+r-1$ positions are dots gives $\binom{n+r-1}{r}$.

3. In a Laplace space with equally likely outcomes, explain why probability reduces to counting and illustrate with the event "at least one 6 in two fair die rolls."
    - solution sketch: In a finite equally likely space, $P[A]=|A|/|\Omega|$. For two die rolls, $|\Omega|=36$. The event "at least one 6" contains $11$ outcomes, so its probability is $11/36$.

## conditioning and independence

1. Starting from the definition $P[A\mid B]=P[A\cap B]/P[B]$, derive the multiplication rule and the law of total probability for a partition $(B_j)$ of $\Omega$.
    - solution sketch: Rearranging gives $P[A\cap B]=P[B]P[A\mid B]$. If $(B_j)$ is a partition, then $A=\bigcup_j (A\cap B_j)$ is a disjoint union, so $P[A]=\sum_j P[A\cap B_j]=\sum_j P[B_j]P[A\mid B_j]$.

2. A diagnostic test has sensitivity $0.99$, specificity $0.99$, and disease prevalence $0.01$. Compute $P[M\mid T]$ and explain in words why the answer is not close to $0.99$.
    - solution sketch: Bayes gives $P[M\mid T]=\frac{0.99\cdot0.01}{0.99\cdot0.01+0.01\cdot0.99}=1/2$. The answer is not near $0.99$ because the large healthy population generates enough false positives to compete with the true positives.

3. Give an example of events that are pairwise independent but not jointly independent, and explain exactly where the stronger condition fails.
    - solution sketch: For two fair coin tosses, let $A =$ "first toss is heads", $B =$ "second toss is heads", and $C =$ "exactly one head occurs". Each pair factorizes, so the events are pairwise independent. But $P[A\cap B\cap C]=0$ while $P[A]P[B]P[C]=1/8$, so joint independence fails at the three-way intersection.

## discrete and continuous distributions

1. Explain why a probability mass function on a countable space determines the whole probability measure, and indicate where nonnegativity is used in the proof of $\sigma$-additivity.
    - solution sketch: If $p(\omega)=P[\{\omega\}]$, then $P[A]=\sum_{\omega\in A}p(\omega)$ for every event $A$. For pairwise disjoint $A_j$, one groups singleton contributions by which event contains each outcome. Nonnegativity is what makes the rearrangement of the series legitimate and prevents cancellation.

2. Compare the binomial, hypergeometric, and Poisson models. For each one, state the experiment it models and one asymptotic relation linking it to another named law.
    - solution sketch: Binomial counts successes in independent Bernoulli trials. Hypergeometric counts favorable items in sampling without replacement and approaches the binomial law when the population is large and the sample size is fixed. Poisson models unbounded counts of rare events and appears as the rare-event limit of $\mathrm{Bin}(n,\lambda/n)$.

3. Why can a density exceed $1$ without violating the axioms of probability? Give an example.
    - solution sketch: A density is probability per unit length, not a point probability, so only its integral must equal $1$. For example, the uniform density on $[0,1/2]$ is $f(x)=2\mathbf{1}_{[0,1/2]}(x)$, which is larger than $1$ but still integrates to $1$.

## cumulative distribution functions and real random variables

1. State and prove the four basic properties of a cumulative distribution function. Then explain why the jump formula $F(x)-F(x-)=P[\{x\}]$ identifies atoms.
    - solution sketch: Use the half-line definition $F(x)=P(( -\infty,x])$. The range is inherited from the probability axioms, monotonicity from inclusion of half-lines, right-continuity from continuity from above, and the limits at $\pm\infty$ from continuity from above/below on shrinking and expanding half-lines. The jump formula follows from $(-\infty,x]=(-\infty,x)\cup\{x\}$ as a disjoint union.

2. Give a counterexample showing that equal distributions do not imply pointwise equality of random variables.
    - solution sketch: On a fair-coin space, let $X(H)=1$, $X(T)=0$, $Y(H)=0$, and $Y(T)=1$. Then both have the Bernoulli $(1/2)$ law, so their cumulative distribution functions agree, but they are never equal pointwise.

3. Explain why equality of cumulative distribution functions implies equality of probability measures on $\mathcal{B}(\mathbb{R})$.
    - solution sketch: Equal cumulative distribution functions mean the two measures agree on every left half-line $(-\infty,x]$. Those half-lines form a generating pi-system for $\mathcal{B}(\mathbb{R})$, so the pi-lambda uniqueness theorem upgrades agreement from the generator to the whole Borel sigma-algebra.

4. Describe the generalized inverse construction for the Lebesgue-Stieltjes theorem and prove the key equivalence $F^{-1}(u)\le x \iff u\le F(x)$.
    - solution sketch: Set $A_u=\{y:F(y)<u\}$, let $s=\sup A_u$, and show that $\{x:F(x)\ge u\}=[s,\infty)$. Then $F^{-1}(u)=s$, so $F^{-1}(u)\le x$ exactly when $x\in[s,\infty)$, which is exactly when $F(x)\ge u$, i.e. $u\le F(x)$.

## proof-oriented prompts

1. Explain in one clean paragraph why a pi-system is weaker than a $\sigma$-algebra but still strong enough to serve as a generator for uniqueness arguments.
    - solution sketch: A pi-system remembers only finite intersections, so it is much weaker than a $\sigma$-algebra, which also requires complements and countable unions. But pi-systems are often concrete and easy to describe, and Dynkin's pi-lambda theorem lets agreement or another measure-theoretic property verified on such a generator extend to the full generated $\sigma$-algebra.

2. Reconstruct the disjointification trick $B_1=A_1$, $B_n=A_n\setminus\bigcup_{j<n}A_j$ and say which part of the proof uses the pi-system property and which part uses the Dynkin-system property.
    - solution sketch: The sets $B_n$ are the new parts of the $A_n$, so they are pairwise disjoint and have the same union as the original family. The pi-system property handles the finite-intersection/difference step needed to keep $B_n$ inside the class, while the Dynkin-system property handles the countable disjoint union $\bigcup_n B_n$.

3. State exactly what it means for a real random variable to be measurable, and explain why the half-line criterion is enough.
    - solution sketch: A real random variable is a map $X\colon(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$ such that $X^{-1}(B)\in\mathcal{F}$ for every Borel set $B$. It is enough to check $\{X\le a\}\in\mathcal{F}$ for all $a\in\mathbb{R}$ because the left half-lines form a generating pi-system for $\mathcal{B}(\mathbb{R})$.

4. Distinguish clearly between a continuous cumulative distribution function, an absolutely continuous cumulative distribution function, and a singular continuous distribution.
    - solution sketch: A continuous cumulative distribution function has no jumps, so there are no atoms. An absolutely continuous cumulative distribution function is stronger: it comes from integrating a density and satisfies the usual epsilon-delta absolute continuity condition. A singular continuous distribution still has a continuous cumulative distribution function but concentrates all its mass on a Lebesgue-null set, so it has no density.
