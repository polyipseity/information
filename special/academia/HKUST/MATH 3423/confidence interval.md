---
aliases:
  - CI
  - confidence intervals
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/confidence_interval
  - language/in/English
---

# confidence interval

A _confidence interval_ is a random interval constructed from sample data that has a specified probability of containing the unknown parameter it estimates. The probability refers to the long-run frequency of the procedure: if the sampling process were repeated many times, the stated proportion of resulting intervals would contain the true parameter. After data are observed, the interval is either fixed or not, and the confidence level describes the method, not any single interval.

---

Flashcards for this section are as follows:

- definition: a confidence interval at level $1 - \alpha$ ::@:: A random interval constructed from sample data that has probability $1 - \alpha$ of containing the unknown parameter, where the probability refers to the long-run coverage rate of the procedure.
- what the confidence level $1 - \alpha$ describes ::@:: The long-run proportion of intervals that would contain the true parameter if the sampling procedure were repeated indefinitely, not the probability that any particular interval contains it.

## pivotal quantity

A _pivotal quantity_ is a function of the statistic and the unknown parameter whose distribution is fully specified — it does not depend on any unknown quantity. Constructing a confidence interval requires finding a pivotal quantity: one rearranges its probability statement to isolate the unknown parameter between the interval endpoints.

The general procedure is: write $P(a < Q < b) = 1 - \alpha$ for the pivotal quantity $Q$, where $a$ and $b$ come from the known distribution of $Q$, then rearrange to $P(\text{lower}(\bar X) < \theta < \text{upper}(\bar X)) = 1 - \alpha$. The left-hand side is a random interval because its endpoints depend on the data through $\bar X$. Once the data are observed and $\bar X = \bar x$ is computed, the interval becomes a fixed set of numbers — the confidence interval for $\theta$.

---

Flashcards for this section are as follows:

- definition: a pivotal quantity for a parameter $\theta$ ::@:: A function of the statistic and $\theta$ whose distribution is fully specified, depending on neither $\theta$ nor any other unknown quantity.
- how a pivotal quantity yields a confidence interval ::@:: Its probability statement is rearranged to place the unknown parameter between two bounds, yielding the random interval.
- general procedure for constructing a confidence interval: pivotal quantity $Q$ with $P(a < Q < b) = 1 - \alpha$ ::@:: Rearrange to $P(\text{lower}(\bar X) < \theta < \text{upper}(\bar X)) = 1 - \alpha$, giving a random interval; substitute $\bar x$ after observing the data.
- random interval versus confidence interval: before versus after observing data ::@:: Before data, the endpoints are random variables and the interval is random; after data, the endpoints are fixed numbers and the interval is a confidence interval.

## confidence interval for the mean

When $X_1, \ldots, X_n$ are i.i.d. from $N(\mu, \sigma^2)$ with $\sigma^2$ known, the sample mean $\bar X$ follows $N(\mu, \sigma^2/n)$, so the quantity $\frac{\bar X - \mu}{\sigma/\sqrt{n}}$ follows $N(0, 1)$ and is a pivotal quantity. The random interval $\bar X \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ has probability $1 - \alpha$ of containing $\mu$. After observing the data, the confidence interval is $\bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$.

---

Flashcards for this section are as follows:

- pivotal quantity for the mean: $X_i$ i.i.d. from $N(\mu, \sigma^2)$, $\sigma^2$ known, so $\bar X \sim N(\mu, \sigma^2/n)$ ::@:: $\frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$.
- random interval for $\mu$: confidence level $1 - \alpha$, $\sigma^2$ known ::@:: $\bar X \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$.
- confidence interval for $\mu$ after observing data: $\sigma^2$ known ::@:: $\bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$, where $z_{\alpha/2}$ is the upper $\alpha/2$ quantile of $N(0, 1)$.
