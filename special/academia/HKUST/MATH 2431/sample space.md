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

- definition ::@:: A non-empty set $\Omega$ of possible realizations of a random experiment; each $\omega \in \Omega$ is an outcome. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- outcome ::@:: An element $\omega \in \Omega$; one possible realization or measurement of the random experiment. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- role in model ::@:: The sample space is the first of three ingredients (with events and probability measure) in a probability space $(\Omega, \mathcal{F}, P)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## types of sample spaces

We meet three broad types of sample spaces in this course: finite sets (coins, dice, finite products), infinite discrete sets (counting variables), and continuous spaces (intervals of real numbers).

---

Flashcards for this section are as follows:

- three types of sample space ::@:: Finite (e.g. coin, die, finite products), infinite discrete (e.g. $\mathbb{N}_0$), and continuous (e.g. $[0,\infty)$); all appear as sample spaces in probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### finite sample spaces

Classic finite examples: tossing a coin gives $\Omega_1 = \{H, T\}$; rolling a die gives $\Omega_2 = \{1, 2, 3, 4, 5, 6\}$. For combined experiments, the Cartesian product is used: coin and die yields $\Omega_3 = \Omega_1 \times \Omega_2 = \{(H,1), (H,2), \ldots, (T,6)\}$. For $n$ independent coin tosses, $\Omega_4 = \Omega_1^n = \{(\omega_1, \ldots, \omega_n) : \omega_i \in \{H,T\}\}$ with $|\Omega_4| = 2^n$.

---

Flashcards for this section are as follows:

- coin once ::@:: $\Omega = \{H, T\}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- die once ::@:: $\Omega = \{1, 2, 3, 4, 5, 6\}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- combined experiment ::@:: Use Cartesian product: e.g. coin and die $\Omega_1 \times \Omega_2$; $|\Omega| = |\Omega_1| \cdot |\Omega_2|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- n-fold coin ::@:: $\Omega = \{H,T\}^n$; $|\Omega| = 2^n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### infinite discrete sample spaces

Infinitely many coin tosses use $\Omega_5 = \Omega_1^{\mathbb{N}} = \{(\omega_1, \omega_2, \ldots) : \omega_i \in \{H,T\}\}$, which already has the size of the continuum (the same cardinality as $[0,1]$ via binary expansions). The number of customers in a shop in one day can be modelled by $\Omega_6 = \mathbb{N}_0 = \{0, 1, 2, \ldots\}$ (countable).

---

Flashcards for this section are as follows:

- infinite coin sequence ::@:: $\Omega = \{H,T\}^{\mathbb{N}}$; uncountable (continuum many sequences). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- countable vs uncountable ::@:: $\Omega_1$ – $\Omega_4$ are finite product spaces (coin, die, finite sequences of tosses) so they are countable; $\Omega_6 = \mathbb{N}_0$ is countable via listing $0,1,2,\ldots$; $\Omega_5 = \{H,T\}^{\mathbb{N}}$ (infinite coin sequences) and $\Omega_7 = [0,\infty)$ have the cardinality of the continuum (like $[0,1]$), strictly larger than any countable set, so we cannot take all subsets as events later. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### continuous sample spaces

The lifetime of a light bulb is $\Omega_7 = \mathbb{R}_0^+ = [0, \infty)$ (another example of a continuum-size sample space).

---

Flashcards for this section are as follows:

- continuum ::@:: The _continuum_ is the common cardinality of real intervals such as $[0,1]$ or $[0,\infty)$ and of sets like $\{H,T\}^{\mathbb{N}}$; it is uncountable and strictly larger than the size of $\mathbb{N}$ or $\mathbb{Q}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## countable sets

A set $S$ is _countable_ if it is empty or there exists a surjective map $\rho \colon \mathbb{N} \to S$. Finite sets are countable. Countability matters because for countable $\Omega$ we can often take the power set as the $\sigma$-algebra; for uncountable $\Omega$ we cannot assign a probability to every subset in a consistent way without running into technical problems.

---

Flashcards for this section are as follows:

- countable definition ::@:: $S$ is countable if $S = \emptyset$ or there is a surjection $\rho \colon \mathbb{N} \to S$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why countability matters ::@:: For countable $\Omega$, $P(\Omega)$ is typically used; for uncountable $\Omega$, we restrict to a $\sigma$-algebra to avoid measure-theoretic obstructions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
