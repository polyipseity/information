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

The _t distribution_ is a one-parameter family of distributions on the whole real line, written $t(r)$ for a positive integer $r$, the degrees of freedom of the chi-squared variable in the construction of $t(r)$. A small $r$ leaves more probability far from the center than the normal does, and the tails move back toward the normal as $r$ grows.

---

Flashcards for this section are as follows:

- overview: for $r$ degrees of freedom ::@:: A one-parameter family of distributions, written $t(r)$, indexed by its degrees of freedom $r$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- support: the values a $t(r)$ variable takes ::@:: The whole real line, $(-\infty, \infty)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## construction from a normal and a chi-squared variable

$$T \stackrel{\text{def}}{=} \frac{Z}{\sqrt{U/r}},$$ where $Z \sim N(0, 1)$, $U \sim \chi^2(r)$, and $r$ is a positive integer.

Each of the three requirements does a different job.

The numerator has to be standard normal, so that its center is zero and its scale is one.

The $r$ belongs inside the square root because $U/r$ has mean one. Dividing by a quantity whose mean is one leaves the numerator's scale alone, so $t(r)$ keeps the scale of $Z$. Leave the $r$ out and the divisor has mean $\sqrt r$, which shrinks the ratio by that factor.

Independence is needed because the law of a ratio is not settled by the two marginal laws. $Z$ and $U$ can each have exactly the right distribution and still produce a ratio with some other law.

With the three requirements fixed, $r$ is the only free quantity. A known constant multiple of the ratio still satisfies the construction, but it changes the scale, giving a scaled $t$; the family is not closed under rescaling.

---

Flashcards for this section are as follows:

- how a $t(r)$ variable is built: from $Z$ and $U$ ::@:: $T \stackrel{\text{def}}{=} Z / \sqrt{U/r}$, where $Z \sim N(0, 1)$, $U \sim \chi^2(r)$, and the two are independent. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- requirements on $Z$ and $U$ in the construction of $t(r)$ ::@:: $Z$ must be standard normal, $U$ must be chi-squared divided by its own degrees of freedom, and the two must be independent. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the $r$ sits inside the square root in $T \stackrel{\text{def}}{=} Z/\sqrt{U/r}$ ::@:: So that the divisor $U/r$ has mean one, which keeps the ratio at the scale of the numerator instead of shrinking it by the factor $\sqrt r$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why $Z$ and $U$ have to be independent in the construction of $t(r)$ ::@:: Because the law of a ratio is not settled by the two marginal laws, so $Z$ and $U$ can each have the right distribution and still produce a ratio with a different law. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a known constant multiple of $T \stackrel{\text{def}}{=} Z/\sqrt{U/r}$ ::@:: It keeps the construction and gives a scaled $t$ rather than a $t$, so the family is not closed under rescaling. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

With $Z \sim N(0, 1)$ and $U \sim \chi^2(5)$ independent, $Z/\sqrt{U/5}$ is a $t(5)$ variable, built from a standard normal and a chi-squared variable divided by its degrees of freedom.

Breaking independence leaves both marginals correct and still ruins the ratio. Taking $U = 5Z^2$ from the same $Z$ gives $Z/\sqrt{U/5} = Z/\sqrt{Z^2}$, which is $\pm 1$ almost surely: the result takes only two values, so it is not a $t(5)$ variable.

Dropping the $r$ from the denominator leaves $\frac{1}{\sqrt r}t(r)$, a $t$ distribution scaled down by $\sqrt r$. The degrees of freedom are right and the scale is wrong. A chi-squared variable of $r + 1$ degrees of freedom, still divided by $r + 1$, gives $\sqrt{\frac{r + 1}{r}}\,t(r)$. The law follows the degrees of freedom $U$ actually carries, which are $r$ and not the $r + 1$ written in the denominator.

Centering the numerator away from zero gives a family of translates: with $(\mu + Z)/\sqrt{U/r}$ and $\mu \ne 0$, the distribution shifts and stops being a $t$ distribution.

---

Flashcards for this section are as follows:

- $Z/\sqrt{U/5}$ with $Z \sim N(0, 1)$ and $U \sim \chi^2(5)$ independent: a $t(5)$ variable? ::@:: Yes, the construction holds with a standard normal numerator, a chi-squared denominator divided by its degrees of freedom, and independence. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $Z/\sqrt{U/5}$ with $U = 5Z^2$ and $Z \sim N(0, 1)$: a $t(5)$ variable? ::@:: No, $Z$ and $U$ are not independent, and the ratio is $Z/\sqrt{Z^2} = \pm 1$ almost surely, so it takes only two values. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $Z/\sqrt{U}$ with $Z \sim N(0, 1)$ and $U \sim \chi^2(r)$ independent: a $t(r)$ variable? ::@:: No, it is $\tfrac{1}{\sqrt r}t(r)$, since the denominator is missing the division by the degrees of freedom. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $(\mu + Z)/\sqrt{U/r}$ with $Z \sim N(0, 1)$, $U \sim \chi^2(r)$ independent, and $\mu \ne 0$: a $t(r)$ variable? ::@:: No, the numerator must be standard normal, so a non-zero $\mu$ shifts the distribution. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $Z/\sqrt{U/(r + 1)}$ with $Z \sim N(0, 1)$ and $U \sim \chi^2(r)$ independent: a $t(r + 1)$ variable? ::@:: No, it is $\sqrt{\tfrac{r + 1}{r}}\,t(r)$, because the law follows from the $r$ degrees of freedom that $U$ actually carries. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- degrees of freedom of the chi-squared variable in $t(r)$: which value of $r$ ::@:: A positive integer, the degrees of freedom of the chi-squared variable in the denominator. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## probability density function

The density is $f_T(t) = \frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)} (1 + t^2/r)^{-(r + 1)/2}$ for $t \in (-\infty, \infty)$.

It depends on $t$ only through $t^2$, so the density is symmetric about zero and the family is centered there. Everything $r$ enters is the $t^2/r$ inside the exponent.

As $|t|$ grows, $(1 + t^2/r)^{-(r + 1)/2}$ falls off like $|t|^{-(r + 1)}$, a power of the distance rather than the normal's exponential decay. So $t(r)$ keeps more probability in its tails than $N(0, 1)$ does. As $r$ grows the exponent $(r + 1)/2$ grows rather than shrinks, while $t^2/r$ shrinks toward zero. The two effects offset, and the density approaches the standard normal's.

---

Flashcards for this section are as follows:

- density of $t(r)$: $f_T(t)$ for $T \sim t(r)$ ::@:: $f_T(t) = \frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)} (1 + t^2/r)^{-(r + 1)/2}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- normalizing constant of the $t(r)$ density: multiplying $(1 + t^2/r)^{-(r + 1)/2}$ ::@:: $\frac{\Gamma((r + 1)/2)}{\sqrt{\pi r} \Gamma(r/2)}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,7,7.31530068,2.11121424,2,2,0,0,2026-11-03T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what the density of $t(r)$ depends on $t$ through ::@:: $t^2$ alone, so it is symmetric about zero. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the tail of the density $f_T(t)$ of $t(r)$ for large $|t|$ ::@:: $(1 + t^2/r)^{-(r + 1)/2}$ falls off like $|t|^{-(r + 1)}$, a power of the distance rather than the normal's exponential decay, so $t(r)$ keeps more probability in the tails. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## convergence to the standard normal

As $r$ grows, $t(r)$ tends to the standard normal $N(0, 1)$. Because the convergence is in distribution, the tail quantiles follow it. The upper $\alpha/2$ quantile $t_{r,\alpha/2}$ approaches the corresponding $z_{\alpha/2}$ of the normal, so a normal cutoff is adequate once there are enough degrees of freedom.

Convergence is what makes the family a correction rather than a replacement. A confidence interval is bounded in the tails, which is exactly where $t(r)$ and $N(0, 1)$ differ. The $t$ cutoff at level $1 - \alpha$ is the wider of the two because its tails are heavier. Reach for the normal cutoff with too few degrees of freedom and more than $\alpha/2$ of the mass falls outside on each side, so the achieved coverage drops below $1 - \alpha$. The limit is a statement about large $r$ only, and it does not say how small $r$ may be before the correction is needed.

---

Flashcards for this section are as follows:

- limiting distribution of $t(r)$: as the degrees of freedom $r$ increase ::@:: The distribution tends to the standard normal $N(0, 1)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the upper $\alpha/2$ quantile $t_{r,\alpha/2}$ of $t(r)$ as $r$ grows ::@:: It approaches the upper $\alpha/2$ quantile $z_{\alpha/2}$ of the normal, so a normal cutoff is adequate for large $r$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a confidence interval at level $1 - \alpha$ bounded with $t_{r,\alpha/2}$ when the standard error is estimated ::@:: Its endpoints are tail quantiles, where $t(r)$ and $N(0, 1)$ differ most, so the heavier $t$ tails are what widen it; using the normal cutoff instead under-covers. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the convergence $t(r) \to N(0, 1)$ applied to a small $r$ ::@:: Nothing, because it is a statement about large $r$; a small-$r$ member has much heavier tails than the normal's, and the correction is largest there. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
