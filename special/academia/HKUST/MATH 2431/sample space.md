---
aliases:
  - outcomes
  - sample space
  - sample spaces
  - set of outcomes
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/sample_space
  - language/in/English
---

# sample space

Probability theory aims to describe random phenomena using stochastic models. A random experiment is modelled by specifying a set of possible realizations, a collection of events, and a rule that assigns probabilities to events. The first of these is the sample space.

## definition and interpretation

A _sample space_ is a non-empty set $\Omega$ whose elements represent the possible realizations (or outcomes) of a random experiment. Each element $\omega \in \Omega$ is called an _outcome_. The sample space is the set of all outcomes we distinguish; the choice of $\Omega$ is part of the modelling process.

---

Flashcards for this section are as follows:

- sample space / definition ::@:: A non-empty set $\Omega$ of possible realizations of a random experiment; each $\omega \in \Omega$ is an outcome. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space / outcome ::@:: An element $\omega \in \Omega$; one possible realization or measurement of the random experiment. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space / role in a probability space ::@:: The sample space is the first of three ingredients (with events and probability measure) in a probability space $(\Omega, \mathcal{F}, P)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## finite and countable sample spaces

The course begins with finite and countable sample spaces because they are the most concrete models and because probability on them is built directly from point masses. In a finite space one can literally list all outcomes. In a countably infinite space one can still enumerate the outcomes in a sequence, at least up to repetitions, so sums over probabilities remain manageable. This is why counting arguments, elementary combinatorics, and discrete distributions naturally appear first.

---

Flashcards for this section are as follows:

- sample space / finite versus countable ::@:: A finite sample space can be listed completely in finitely many steps, while a countably infinite sample space can still be enumerated in a sequence; both are convenient because probabilities can be assembled from singleton masses.
- sample space / why the course starts with finite and countable spaces ::@:: On finite or countable spaces, events and probabilities can be handled by explicit listing, counting, and summation, so these models are the natural starting point before one studies uncountable spaces and generated sigma-algebras.

### finite sample spaces

Classic finite examples: tossing a coin gives $\Omega_1 = \{H, T\}$; rolling a die gives $\Omega_2 = \{1, 2, 3, 4, 5, 6\}$. For combined experiments, the Cartesian product is used: coin and die yields $\Omega_3 = \Omega_1 \times \Omega_2 = \{(H,1), (H,2), \ldots, (T,6)\}$. For $n$ independent coin tosses, $\Omega_4 = \Omega_1^n = \{(\omega_1, \ldots, \omega_n) : \omega_i \in \{H,T\}\}$ with $|\Omega_4| = 2^n$.

---

Flashcards for this section are as follows:

- sample space for one coin toss ::@:: $\Omega = \{H, T\}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space for one die roll ::@:: $\Omega = \{1, 2, 3, 4, 5, 6\}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space for a combined experiment ::@:: Use Cartesian product: e.g. coin and die $\Omega_1 \times \Omega_2$; $|\Omega| = |\Omega_1| \cdot |\Omega_2|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space for $n$ coin tosses ::@:: $\Omega = \{H,T\}^n$; $|\Omega| = 2^n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### countably infinite sample spaces

Typical countably infinite sample spaces arise when the outcome is a nonnegative integer or another listable object. For example, the number of customers entering a shop in one day can be modelled by $\Omega_5 = \mathbb{N}_0 = \{0,1,2,\ldots\}$. Likewise, the trial number of the first success in repeated Bernoulli trials has sample space $\mathbb{N}$. In each case there are infinitely many possible outcomes, but they can still be listed one after another.

---

Flashcards for this section are as follows:

- countably infinite sample space / number-of-customers model ::@:: A typical countably infinite sample space is $\mathbb{N}_0=\{0,1,2,\ldots\}$, used when the outcome is a count such as the number of customers or the number of arrivals in a time window. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- countably infinite sample space / first-success trial model ::@:: The trial number of the first success in repeated Bernoulli trials has sample space $\mathbb{N}$; this is infinite but countable because the possible values can be listed as $1,2,3,\ldots$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## uncountable sample spaces

Some natural experiments have too many outcomes to be listed in a sequence. A lifetime, a waiting time, or an exact location is often modelled by a real interval such as $[0,\infty)$ or $\mathbb{R}$. Even some purely discrete-looking experiments can produce uncountable spaces: the set of all infinite coin-toss sequences, $\{H,T\}^{\mathbb{N}}$, has the cardinality of the continuum. These examples show that "infinitely many outcomes" and "countably many outcomes" are not the same idea.

---

Flashcards for this section are as follows:

- uncountable sample space / infinite coin-toss sequences ::@:: The space $\{H,T\}^{\mathbb{N}}$ of infinite coin-toss sequences is uncountable; it has the cardinality of the continuum rather than that of $\mathbb{N}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- uncountable sample space / lifetime model ::@:: A lifetime or waiting time is naturally modelled on an interval such as $[0,\infty)$, which is uncountable because its points cannot be listed in a sequence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sample space / countably infinite versus uncountable ::@:: The difference is not merely "infinite versus finite": $\mathbb{N}_0$ is infinite but countable, whereas $[0,\infty)$ and $\{H,T\}^{\mathbb{N}}$ are uncountable, so later we cannot simply treat every subset as an event. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## countable sets

A set $S$ is _countable_ if it is empty or there exists a surjective map $\rho \colon \mathbb{N} \to S$. Finite sets are countable. Equivalently, a nonempty set is countable when its elements can be listed in a sequence, possibly with repetitions. The surjection formulation is slightly more flexible than demanding a one-to-one list from the start, because it allows repetitions and still captures the idea that $\mathbb{N}$ is large enough to index all elements of $S$.

Countability matters because for countable $\Omega$ we can often take the power set as the $\sigma$-algebra and define probabilities by summing singleton masses. For uncountable $\Omega$ we cannot assign a probability to every subset in a consistent way while preserving the interval-based constructions needed in continuous probability, so one must pass to a smaller measurable family.

---

Flashcards for this section are as follows:

- countable set / formal definition via a surjection from $\mathbb{N}$ ::@:: $S$ is countable if $S = \emptyset$ or there is a surjection $\rho \colon \mathbb{N} \to S$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- countable set / listing viewpoint ::@:: A nonempty set is countable exactly when its elements can be listed in a sequence, possibly with repetitions; this is the intuition behind the formal surjection $\mathbb{N}\to S$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why countability matters for probability spaces ::@:: For countable $\Omega$, $P(\Omega)$ is typically used; for uncountable $\Omega$, we restrict to a $\sigma$-algebra to avoid measure-theoretic obstructions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuum cardinality in probability examples ::@:: The _continuum_ is the common cardinality of real intervals such as $[0,1]$ or $[0,\infty)$ and of sets like $\{H,T\}^{\mathbb{N}}$; it is uncountable and strictly larger than the size of $\mathbb{N}$ or $\mathbb{Q}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
