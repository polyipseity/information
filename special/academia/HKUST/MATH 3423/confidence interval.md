---
aliases:
  - CI
  - confidence intervals
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/confidence_interval
  - language/in/English
---

# confidence interval

A _confidence interval_ is a random interval built from sample data that has a specified probability of containing the parameter it estimates. That probability is a long-run coverage rate over repeated samples, not the chance that any one interval contains the parameter.

Every confidence interval is built the same way: start from a quantity whose distribution is fully known, read off the region carrying probability $1 - \alpha$, and rearrange the probability statement until the parameter sits between two bounds. That quantity is a _pivotal quantity_.

---

Flashcards for this section are as follows:

- definition: a confidence interval at level $1 - \alpha$ ::@:: A random interval constructed from sample data that has probability $1 - \alpha$ of containing the unknown parameter, where the probability refers to the long-run coverage rate of the procedure.
- what the confidence level $1 - \alpha$ describes ::@:: The long-run proportion of intervals that would contain the true parameter if the sampling procedure were repeated indefinitely, not the probability that any particular interval contains it.

## pivotal quantity

A _pivotal quantity_ is a function of the statistic and the unknown parameter whose distribution is fully specified. It names no unknown quantity.

A quantity may mention the unknown parameter and still be perfectly well defined, because $\bar X - \mu$ exists for every sample that could be drawn. What it may not do is carry the unknown into its distribution: the law of $\bar X - \mu$ changes with the values of $\mu$ and $\sigma$, so no probability statement about it evaluates to a number.

Write $P(a < Q < b) = 1 - \alpha$ for the pivotal quantity $Q$. The bounds $a$ and $b$ are read off the central region carrying probability $1 - \alpha$, not computed from the data. Rearranging the statement gives $P(\text{lower}(\bar X) < \theta < \text{upper}(\bar X)) = 1 - \alpha$.

The interval is random, since its endpoints depend on the data through $\bar X$. Once the data are in, $\bar X$ is replaced by $\bar x$ and the endpoints become fixed numbers, and what was a random interval is a confidence interval built at the promised level $1 - \alpha$.

The test for a pivot is a question about the distribution alone: if the distribution still names an unknown quantity, the candidate is not pivotal. An estimate in the denominator is not by itself a fault, because the estimate is a function of the data and carries no unknown parameter into the law of the quotient.

---

Flashcards for this section are as follows:

- definition: a pivotal quantity for a parameter $\theta$ ::@:: A function of the statistic and $\theta$ whose distribution is fully specified, depending on neither $\theta$ nor any other unknown quantity.
- where the bounds $a$ and $b$ come from: a pivotal quantity $Q$ with $P(a < Q < b) = 1 - \alpha$ ::@:: The endpoints of the central region of $Q$'s known distribution that carries probability $1 - \alpha$, so they are read off that law rather than computed from the data.
- why a quantity that names an unknown in its law cannot serve: a candidate such as $\bar X - \mu$ ::@:: Its distribution changes with the value of the unknown parameter, so no probability statement about it evaluates to a number.
- how a pivotal quantity yields a confidence interval ::@:: Its probability statement is rearranged to place the unknown parameter between two bounds.
- general procedure for constructing a confidence interval: pivotal quantity $Q$ with $P(a < Q < b) = 1 - \alpha$ ::@:: Rearrange to $P(\text{lower}(\bar X) < \theta < \text{upper}(\bar X)) = 1 - \alpha$, then substitute $\bar x$ for $\bar X$ once the data are in.
- random interval versus confidence interval: before versus after observing data ::@:: Before data, the endpoints are random variables and the interval is random; after data, the endpoints are fixed numbers and the interval is a confidence interval.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Take a sample of size $n$ from $N(\mu, \sigma^2)$. With $\sigma^2$ known, $\frac{\bar X - \mu}{\sigma/\sqrt{n}}$ is $N(0, 1)$ and $\frac{n S_n^2}{\sigma^2}$ is $\chi^2(n - 1)$; neither law names $\mu$ or $\sigma$, and the chi-squared law carries $n - 1$ degrees of freedom. With $\sigma^2$ unknown, $\frac{\bar X - \mu}{S_n}$ is $\tfrac{1}{\sqrt{n-1}} t(n - 1)$, again with $n - 1$ degrees of freedom, since $S_n$ is independent of the numerator $\bar X - \mu$ and the unknown $\sigma$ drops out of the law.

Three near misses fail on one ground, an unknown left inside the distribution. $\bar X - \mu$ is centered on the parameter, but its distribution is $N(0, \sigma^2/n)$, which still names $\sigma$. $S_n^2$ has distribution $\frac{\sigma^2}{n}\chi^2(n-1)$, the pivotal quantity $\frac{n S_n^2}{\sigma^2}$ with $\sigma^2$ left undivided. $\bar X/\mu$ has a distribution that depends on the unknown ratio $\mu/\sigma$.

---

Flashcards for this section are as follows:

- $\frac{\bar X - \mu}{\sigma/\sqrt{n}}$ for a normal sample with $\sigma^2$ known: a pivotal quantity? ::@:: Yes, it is $N(0, 1)$, naming neither $\mu$ nor $\sigma$.
- $\frac{n S_n^2}{\sigma^2}$ for a normal sample with $\sigma^2$ known: a pivotal quantity? ::@:: Yes, it is $\chi^2(n - 1)$ with $n - 1$ degrees of freedom, naming neither $\mu$ nor $\sigma$.
- $\frac{\bar X - \mu}{S_n}$ for a normal sample: a pivotal quantity? ::@:: Yes, it is $\tfrac{1}{\sqrt{n-1}} t(n - 1)$ with $n - 1$ degrees of freedom, since $S_n$ is independent of the numerator and no $\sigma$ remains in the law.
- $\bar X - \mu$ for a normal sample with $\sigma^2$ unknown: a pivotal quantity? ::@:: No, its distribution is $N(0, \sigma^2/n)$, which still names $\sigma$.
- $S_n^2$ for a normal sample: a pivotal quantity? ::@:: No, its distribution is $\tfrac{\sigma^2}{n}\chi^2(n-1)$, which still names $\sigma^2$; only the scaled quantity $\tfrac{nS_n^2}{\sigma^2}$ is pivotal.
- $\bar X/\mu$ for a normal sample with $\mu$ and $\sigma$ unknown: a pivotal quantity? ::@:: No, its distribution depends on the unknown ratio $\mu/\sigma$.
- test for a pivotal quantity: for a candidate function of the sample and $\theta$ ::@:: Its distribution must be fully specified; if the distribution still names an unknown quantity, it is not pivotal.

## confidence interval for the mean

Let $X_1, \ldots, X_n$ be i.i.d. from $N(\mu, \sigma^2)$ with $\sigma^2$ known. Then $\bar X \sim N(\mu, \sigma^2/n)$, and the standardization $\frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ is a pivot, its law the same whatever $\mu$ and $\sigma$ turn out to be.

The $1 - \alpha$ central region of the standard normal is bounded by $\pm z_{\alpha/2}$, where $z_{\alpha/2}$ is the upper $\alpha/2$ quantile. Rearranging the probability statement around that region gives the random interval $\bar X \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$, which contains $\mu$ with probability $1 - \alpha$ over the sampling.

Observed data replace $\bar X$ by $\bar x$, and the interval reported from them, $\bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$, holds no random quantity. What survives of the probability is the coverage rate of the procedure that produced it.

---

Flashcards for this section are as follows:

- pivotal quantity for the mean: $X_i$ i.i.d. from $N(\mu, \sigma^2)$, $\sigma^2$ known, so $\bar X \sim N(\mu, \sigma^2/n)$ ::@:: $\frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$.
- random interval for $\mu$: confidence level $1 - \alpha$, $\sigma^2$ known ::@:: $\bar X \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$.
- confidence interval for $\mu$ after observing data: $\sigma^2$ known ::@:: $\bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$, where $z_{\alpha/2}$ is the upper $\alpha/2$ quantile of $N(0, 1)$.

## when the variance is unknown

The same interval cannot be built once $\sigma^2$ is unknown, because $\sigma$ sits in both of its endpoints. The obvious repair is to put the quantity estimating $\sigma$ in its place and keep the same cutoff, which produces $\bar x \pm z_{\alpha/2} \frac{S_n}{\sqrt{n}}$.

That repair is not a valid interval. $\frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ holds because $\sigma$ is a number. A random variable in the denominator changes the law of the quotient, to $\sqrt{\frac{n}{n-1}}\,t(n - 1)$ for $\frac{\bar X - \mu}{S_n/\sqrt{n}}$, which has heavier tails. The cutoff $z_{\alpha/2}$ then leaves more than $\alpha/2$ of the mass outside on each side, so the coverage drops below $1 - \alpha$ at every level.

The pivot has to keep $S_n$ in the denominator without pretending the quotient is standard normal. Write it as $$\frac{\bar X - \mu}{S_n} = \frac{(\bar X - \mu)/(\sigma/\sqrt{n})}{S_n\sqrt{n}/\sigma}.$$ The numerator is standard normal and independent of $S_n$, because $\bar X$ and $S_n^2$ are. The denominator is $\sqrt{U}$ for $U = \frac{n S_n^2}{\sigma^2} \sim \chi^2(n-1)$, so $$\frac{\bar X - \mu}{S_n} = \frac{Z}{\sqrt{U}} = \frac{1}{\sqrt{n-1}}\frac{Z}{\sqrt{U/(n-1)}} \sim \frac{1}{\sqrt{n-1}}t(n-1)$$ with $Z \sim N(0, 1)$ and $U \sim \chi^2(n-1)$ independent. A standard normal over the square root of an independent chi-squared is a scaled $t$, and the interval inverts its scale.

The interval at level $1 - \alpha$ is $$\bar x \pm t_{n-1,\alpha/2}\frac{S_n}{\sqrt{n-1}} = \bar x \pm t_{n-1,\alpha/2}\frac{S_{n-1}}{\sqrt{n}}.$$ The two forms agree, because $S_{n-1} = \sqrt{\frac{n}{n-1}}S_n$.

---

Flashcards for this section are as follows:

- interval obtained by substituting $S_n$ for $\sigma$: a normal sample with $\sigma^2$ unknown ::@:: $\bar x \pm z_{\alpha/2} \frac{S_n}{\sqrt{n}}$, which is not a valid confidence interval at level $1 - \alpha$.
- why replacing $\sigma$ by $S_n$ invalidates the standard normal pivot: for a normal sample ::@:: $\frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ holds because $\sigma$ is a number, and a random variable in the denominator changes the distribution of the quotient.
- distribution of $\frac{\bar X - \mu}{S_n/\sqrt{n}}$ for a normal sample with $\sigma^2$ unknown ::@:: Not $N(0, 1)$ but $\sqrt{\frac{n}{n-1}}\,t(n - 1)$, which has heavier tails, so the cutoff $z_{\alpha/2}$ under-covers.
- distribution of the numerator of the substituted pivot: $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: $(\bar X - \mu)/(\sigma/\sqrt{n}) \sim N(0, 1)$, independent of $S_n$ because $\bar X$ and $S_n^2$ are.
- distribution of the denominator of the substituted pivot: $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ with $n > 1$ ::@:: $(S_n/\sigma)^2 = \frac{n S_n^2}{\sigma^2} \sim \chi^2(n - 1)$.
- pivotal quantity for $\mu$ when $\sigma^2$ is unknown: for a normal sample of size $n > 1$ ::@:: $\frac{\bar X - \mu}{S_n} \sim \frac{1}{\sqrt{n-1}}t(n - 1)$.
- why the two forms of the $t$ interval are equal ::@:: Because $S_{n-1} = \sqrt{\frac{n}{n-1}}S_n$, which makes the two denominators the same number.
- confidence interval for $\mu$ after observing data: $\sigma^2$ unknown, normal sample of size $n > 1$ ::@:: $\bar x \pm t_{n-1,\alpha/2}\frac{S_n}{\sqrt{n-1}} = \bar x \pm t_{n-1,\alpha/2}\frac{S_{n-1}}{\sqrt{n}}$, where $t_{n-1,\alpha/2}$ is the upper $\alpha/2$ quantile of $t(n-1)$.
