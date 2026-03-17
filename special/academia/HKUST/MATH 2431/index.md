---
aliases:
  - HKUST MATH 2431
  - HKUST MATH 2431 index
  - HKUST MATH2431
  - HKUST MATH2431 index
  - Honors Probability
  - Honors Probability index
  - MATH 2431
  - MATH 2431 index
  - MATH2431
  - MATH2431 index
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/index
  - function/index
  - language/in/English
---

<!-- Honors course: when adding, editing, or removing notes here, think carefully, thoroughly, and rigorously about the probability theory; include clear arguments and derivations (not just statements) where appropriate, and feel free to add more high-quality flashcards than in non-honors courses. -->

# index

- HKUST MATH 2431
- name: Honors Probability
- credits: 4

---

This is an honors undergraduate course in probability theory at HKUST covering probability spaces and random variables, discrete and continuous distributions, expectations and moment inequalities, conditional expectations and distributions, generating functions, convergence concepts, laws of large numbers, and the central limit theorem.

The content is in teaching order.

## logistics

- grading
  - scheme I
    - homework problems: 15%
    - midterm exam: 35%
    - final exam: 50%
  - scheme II
    - homework problems: 15%
    - midterm exam: 0%
    - final exam: 85%
- sections:
  - lecture: L1
    - L1: Room 6573 (near Lifts 29–30); WednesdayT13:30:00+08:00/WednesdayT14:50:00+08:00, FridayT13:30:00+08:00/FridayT14:50:00+08:00
  - tutorials: T1A
    - T1A: Room 5404 (near Lifts 17–18); ThursdayT18:00:00+08:00/ThursdayT18:50:00+08:00
    - T1B: Room 2404 (near Lifts 17–18); MondayT19:30:00+08:00/MondayT20:20:00+08:00
- instructor: see Canvas or the official syllabus for contact.
- office hours: Wednesdays 11:30–13:00, or via Zoom on request.

## children

- [assignments](assignments/index.md)
- [conditional probability and independence](conditional%20probability%20and%20independence.md)
- [conditional probability](conditional%20probability.md)
- [elementary combinatorics](elementary%20combinatorics.md)
- [independence](independence.md)
- [probability measure](probability%20measure.md)
- [questions](questions.md)
- [sample space](sample%20space.md)
- [sigma-algebra](sigma-algebra.md)

## assignments

- Homework problems are assigned weekly on Wednesdays via Canvas and are due the following Friday before class (13:30 Hong Kong time), unless otherwise announced.

### week 1 lecture 1

- datetime: 2026-02-04T13:30:00+08:00/2026-02-04T14:50:00+08:00
- topic: introduction; motivating example (random walk); guiding questions; course outline; outcomes and sample spaces; elementary combinatorics
- MATH 2431
  - MATH 2431 / random walk on Z (motivating example) ::@:: Model: $\xi_1,\xi_2,\ldots$ iid with $P[\xi_j=+1]=P[\xi_j=-1]=\frac{1}{2}$; $X_0=0$, $X_n=\xi_1+\cdots+\xi_n$ for $n\ge 1$. The process $(X_n)_{n\in\mathbb{N}_0}$ is the _discrete-time simple random walk_ on $\mathbb{Z}$. Historically linked to Pascal–Fermat correspondence (1654–1660). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - MATH 2431 / random walk on $\mathbb{Z}^d$ ::@:: For $d\ge 1$, the walker at each step jumps to a nearest neighbour in $\mathbb{Z}^d$ with probability $1/(2d)$ each direction; $(X_n)_{n\in\mathbb{N}_0}$ is the discrete-time simple random walk on $\mathbb{Z}^d$ (includes $d=1$ as special case).
  - MATH 2431 / guiding questions (random walk) ::@:: (1) What is the average $\frac{1}{n}X_n$ for large $n$, and in what sense does it converge? (2) What is the approximate distribution of the position after $n$ steps? (3) How often does the walker return to the origin? <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - MATH 2431 / course outline (blocks) ::@:: (1) Probability spaces, conditional probability, independence, discrete and continuous distributions (~4 weeks). <br/> (2) Random variables, joint distributions, expectation, moments, generating functions (~5.5 weeks). <br/> (3) Convergence modes, laws of large numbers, central limit theorem (~1.5 weeks). <br/> (4) Overview of stochastic processes (~0.5 week, time-permitting).
  - MATH 2431 / course not covering ::@:: Measure-theory based proofs (→ MATH 5411); detailed stochastic processes e.g. Markov chains, Brownian motion (→ MATH 3425); statistics (→ MATH 2411 or MATH 5431). Tools from measure theory will be invoked; MATH 3033 Real Analysis is relevant.
  - MATH 2431 / references and organization ::@:: No single textbook; lecture notes provided on Canvas. Main and further references available via HKUST Library course reserve. Grading: Scheme I (homework 15%, midterm 35%, final 50%) or Scheme II (homework 15%, midterm 0%, final 85%); higher score taken. Homework assigned weekly on Wednesdays from 04/02/2026, 11 problem sets in total; tutorial and exam details on Canvas.
  - MATH 2431 / stochastic model ::@:: Probability theory describes random phenomena using stochastic models: specify sample space $\Omega$, events ($\sigma$-algebra $\mathcal{F}$), and probability measure $P$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - MATH 2431 / equally likely and counting ::@:: When all outcomes in finite $\Omega$ are equally likely, $P[A] = |A|/|\Omega|$; counting $|\Omega|$ and $|A|$ is the role of elementary combinatorics. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- [sample space](sample%20space.md)
  - sample space / [§ definition and interpretation](sample%20space.md#definition%20and%20interpretation)
  - sample space / [§ finite and countable sample spaces](sample%20space.md#finite%20and%20countable%20sample%20spaces)
  - sample space / [§ countable sets](sample%20space.md#countable%20sets)
- [elementary combinatorics](elementary%20combinatorics.md)
  - elementary combinatorics / [§ cartesian product and product rule](elementary%20combinatorics.md#cartesian%20product%20and%20product%20rule)
  - elementary combinatorics / [§ samples of size r from n elements](elementary%20combinatorics.md#samples%20of%20size%20r%20from%20n%20elements)

### week 1 lecture 2

- datetime: 2026-02-06T13:30:00+08:00/2026-02-06T14:50:00+08:00
- topic: elementary combinatorics (continued); events and sigma-algebras; probability measures
- MATH 2431
  - MATH 2431 / sigma-algebras ::@:: A $\sigma$-algebra on $\Omega$ is $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ with $\Omega \in \mathcal{F}$, closed under complements and countable unions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - MATH 2431 / probability space triple ::@:: $(\Omega, \mathcal{F}, P)$: sample space, $\sigma$-algebra of events, and probability measure satisfying $P[\Omega]=1$ and $\sigma$-additivity. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- [elementary combinatorics](elementary%20combinatorics.md)
  - elementary combinatorics / [§ multinomial coefficient and division into groups](elementary%20combinatorics.md#multinomial%20coefficient%20and%20division%20into%20groups)
  - elementary combinatorics / [§ multinomial and binomial theorems](elementary%20combinatorics.md#multinomial%20and%20binomial%20theorems)
- [sigma-algebra](sigma-algebra.md)
  - sigma-algebra / [§ power set and naive definition of event](sigma-algebra.md#power%20set%20and%20naive%20definition%20of%20event)
  - sigma-algebra / [§ definition of sigma-algebra](sigma-algebra.md#definition%20of%20sigma-algebra)
  - sigma-algebra / [§ consequences: empty set, intersections, finite operations](sigma-algebra.md#consequences%3A%20empty%20set%2C%20intersections%2C%20finite%20operations) <!-- check: ignore-line[numeric_text_not_latex]: link anchor -->
  - sigma-algebra / [§ concrete cases and violations](sigma-algebra.md#concrete%20cases%20and%20violations)
- [probability measure](probability%20measure.md)
  - probability measure / [§ definition and Kolmogorov axioms](probability%20measure.md#definition%20and%20Kolmogorov%20axioms)
  - probability measure / [§ uniform distribution and Laplace space](probability%20measure.md#uniform%20distribution%20and%20Laplace%20space)
  - probability measure / [§ elementary properties](probability%20measure.md#elementary%20properties)

### week 2 lecture 1

- datetime: 2026-02-11T13:30:00+08:00/2026-02-11T14:50:00+08:00
- topic: elementary properties of probabilities; conditional probability; multiplication theorem
- [probability measure](probability%20measure.md)
  - probability measure / [§ elementary properties](probability%20measure.md#elementary%20properties)
- [conditional probability](conditional%20probability.md)
  - conditional probability / [§ conditional probability: definition and multiplication rule](conditional%20probability.md#conditional%20probability-definition-and-multiplication-rule)
  - conditional probability / [§ conditional probability as a probability measure](conditional%20probability.md#conditional%20probability%20as%20a%20probability%20measure)

### week 2 lecture 2

- datetime: 2026-02-13T13:30:00+08:00/2026-02-13T14:50:00+08:00
- topic: law of total probability; Bayes' theorem; stochastic independence
- [conditional probability](conditional%20probability.md)
  - conditional probability / [§ law of total probability and Bayes' theorem](conditional%20probability.md#law-of-total-probability-and-bayes-theorem)
  - conditional probability / [§ diagnostic test for rare disease](conditional%20probability.md#diagnostic-test-for-rare-disease)
- [independence](independence.md)
  - independence / [§ definitions: pairwise and joint independence](independence.md#definitions-pairwise-and-joint-independence)
  - independence / [§ independence via cards and coins](independence.md#independence-via-cards-and-coins)

## midterm examination

- datetime: 2026-03-20T13:30:00+08:00/2026-03-20T14:50:00+08:00
- venue: Room 6573, near Lifts 29–30
