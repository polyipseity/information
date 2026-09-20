---
aliases:
  - Student's t distribution
  - Student's t-distribution
  - t distribution
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/Student_s_t-distribution
  - language/in/English
---

# Student's t-distribution

The _t distribution_ is a one-parameter family of distributions on the whole real line, written $t(r)$ for its degrees of freedom $r$. It is the distribution of a standard normal variable divided by the square root of an independent chi-squared variable over its degrees of freedom. The distribution approaches the standard normal as $r$ grows.

---

Flashcards for this section are as follows:

- overview: for $r$ degrees of freedom ::@:: A one-parameter family of distributions on the whole real line, written $t(r)$.
- notation: for $r$ degrees of freedom ::@:: $t(r)$.
- how a $t$ variable is built: from $Z$ and $U$ ::@:: $T \stackrel{\text{def}}{=} Z / \sqrt{U/r}$, where $Z \sim N(0, 1)$, $U \sim \chi^2(r)$, and the two are independent.
- support: the values a $t(r)$ variable takes ::@:: The whole real line, $(-\infty, \infty)$.

## probability density function

The density of $T \sim t(r)$ is $f_T(t) = \frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)} (1 + t^2/r)^{-(r+1)/2}$ for $t \in (-\infty, \infty)$.

---

Flashcards for this section are as follows:

- density of $t(r)$: $f_T(t)$ for $T \sim t(r)$ ::@:: $f_T(t) = \frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)} (1 + t^2/r)^{-(r+1)/2}$.
- normalizing constant of the $t(r)$ density: multiplying $(1 + t^2/r)^{-(r+1)/2}$ ::@:: $\frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)}$.

## convergence to the standard normal

As the number of degrees of freedom increases, the $t$ distribution tends to the standard normal distribution.

---

Flashcards for this section are as follows:

- limiting distribution of $t(r)$: as the degrees of freedom $r$ increase ::@:: The distribution tends to the standard normal $N(0, 1)$.
