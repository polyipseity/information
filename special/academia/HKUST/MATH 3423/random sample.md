---
aliases:
  - Independent and identically distributed random variables
  - i.i.d.
  - iid
  - random sample
  - random samples
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/random_sample
  - language/in/English
---

# random sample

A _random sample_ is a collection of independent and identically distributed copies of a random variable $X$. Unless stated otherwise, the course assumes that $X_1, \ldots, X_n$ has this structure, which makes the joint distribution of the sample, and the behaviour of any statistic built from it, tractable.

---

Flashcards for this section are as follows:

- definition: for copies $X_1, \ldots, X_n$ of the random variable $X$ ::@:: A collection of independent and identically distributed copies of $X$, in short rs.
- requirement on the copies $X_1, \ldots, X_n$ ::@:: Independent and identically distributed, abbreviated i.i.d., unless otherwise stated.
- which value of $X_i$ is meant by $x_i$ ::@:: The actual value taken by the $i$-th copy $X_i$ of $X$.

## the i.i.d. assumption

Independence says no copy of $X$ carries information about any other, so probabilities for the sample multiply and variances of sums add: $\operatorname{Var}(X_1 + \cdots + X_n) = \operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n)$. Identical distribution says every copy follows the same distribution as $X$, so one parameter $\theta$ serves the whole sample. Together the two are abbreviated i.i.d.

---

Flashcards for this section are as follows:

- why independence is assumed: for $X_1, \ldots, X_n$ ::@:: No copy carries information about any other, so probabilities for the sample multiply and $\operatorname{Var}(X_1 + \cdots + X_n) = \operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n)$.
- why identical distribution is assumed: for $X_1, \ldots, X_n$ ::@:: Every copy follows the same distribution as $X$, so one parameter $\theta$ describes the whole sample.
- abbreviation for independent and identically distributed copies of $X$ ::@:: i.i.d.

## joint distribution under random sampling

Under random sampling the joint distribution is determined by the common distribution of the copies. For continuous copies the joint pdf is $f(x_1, \ldots, x_n \mid \theta) = \prod_{i=1}^{n} f_X(x_i \mid \theta)$; for discrete copies the joint pmf is the analogous product over $i = 1, \ldots, n$. Both use the single $\theta$ shared by all copies.

---

Flashcards for this section are as follows:

- joint pdf of a random sample: $f(x_1, \ldots, x_n \mid \theta)$ ::@:: $\prod_{i=1}^{n} f_X(x_i \mid \theta)$, a product because the copies are independent.
- joint pmf of a random sample: for $i = 1, \ldots, n$ ::@:: $\prod_{i=1}^{n} p_X(x_i \mid \theta)$, the discrete analogue of the joint pdf.
- parameter shared by a random sample: $\theta$ in the factorization ::@:: One parameter serves every copy, because the copies are identically distributed.
