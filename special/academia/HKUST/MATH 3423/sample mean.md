---
aliases:
  - empirical mean
  - sample average
  - sample mean
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/sample_mean
  - language/in/English
---

# sample mean

The sample mean estimates the unknown population mean $\mu$ from the observed sample. Its value cannot be predicted before the sample is drawn. What is known in advance is the distribution it is drawn from, and that is what inference uses.

---

Flashcards for this section are as follows:

- which quantity of the population the sample mean $\bar X$ of a sample of size $n$ estimates ::@:: The unknown population mean $\mu$.
- predictability of $\bar X$ before a sample of size $n$ is drawn ::@:: Its value cannot be predicted. Only its distribution is known in advance.

## average of the copies

The sample mean of a random sample $X_1, \ldots, X_n$ is $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$: the average of the $n$ copies, each carrying the same weight $1/n$. Change one weight and the quantity is still a statistic of the sample, but no longer the sample mean.

Each copy $X_i$ has the population mean $\mu$, and averaging copies leaves that mean unchanged, so the sample mean is the natural guess for it. It is also a random variable, fixed by the sample size $n$ rather than by the data. Once the data $x_1, \ldots, x_n$ are in, the same average applied to them is a number rather than a random variable, written $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$.

---

Flashcards for this section are as follows:

- what the sample mean of a random sample $X_1, \ldots, X_n$ is ::@:: The average of the copies, $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$.
- the average of the observed data $x_1, \ldots, x_n$, written $\bar x$ ::@:: $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$, a number rather than a random variable.
- what makes $\sum_{i=1}^{n} w_i X_i$ the sample mean of a random sample $X_1, \ldots, X_n$ ::@:: All the weights equal $1/n$, the same weight on every copy.
- what is fixed about $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ before a sample of size $n$ is drawn ::@:: The rule, not the value. The distribution it follows comes from the population and the size $n$, and the value needs the sample.
- for one sample of size $n$, which of $\bar X$ and $\bar x$ is available before the data arrive ::@:: $\bar X$, the random variable. $\bar x$ is the value it takes once the data are in.
- the mean of the sample mean $\bar X$ for a random sample of size $n$ from a population with mean $\mu$ ::@:: $\mu$, since each copy has mean $\mu$ and $\bar X$ averages the copies.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The sample mean of $X_1, \ldots, X_n$ satisfies the definition, every copy carrying the same weight $1/n$. Each case fails on one specific ground: the weights, the number of copies averaged, or the object averaged.

Unequal positive weights that sum to one still give a statistic of the sample, but not the sample mean. The average $\frac{1}{k} \sum_{i=1}^{k} X_i$ of the first $k < n$ copies is the sample mean of the smaller sample of size $k$, not of the sample of size $n$. The unknown population mean $\mu$ averages the whole population rather than a sample.

---

Flashcards for this section are as follows:

- $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ for a random sample $X_1, \ldots, X_n$ as the sample mean of that sample ::@:: Yes, it averages all $n$ copies with equal weights $1/n$.
- $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$ computed from the collected data as the sample mean ::@:: Yes, it is the realized value of that average, the average of the data.
- $\sum_{i=1}^{n} w_i X_i$ with unequal positive weights and $\sum_{i=1}^{n} w_i = 1$ as the sample mean of $X_1, \ldots, X_n$ ::@:: No, it is a statistic of the sample, but its weights are not all $1/n$.
- $\frac{1}{k} \sum_{i=1}^{k} X_i$ with $k < n$ as the sample mean of the sample $X_1, \ldots, X_n$ ::@:: No, it is the sample mean of the smaller sample $X_1, \ldots, X_k$, leaving the other $n - k$ copies out.
- the unknown population mean $\mu$ as a sample mean ::@:: No, it averages the population, so it is the population mean.

## distribution of the sample mean

The sample mean is a sum divided by $n$, so its law is that of $\sum_{i=1}^{n} X_i$ rescaled. Independence is what makes that tractable, since the law of a sum of independent copies is built from the law of a single copy. It also gives $\operatorname{Var}(\sum_{i=1}^{n} X_i) = \sum_{i=1}^{n} \operatorname{Var}(X_i)$, so the average carries variance $\sigma^2/n$ whatever family the population follows.

Its first two moments need no family assumption, only a population mean and variance that are both finite. Identical distribution alone gives the mean. Independence is what the variance needs, since without it the covariances between copies enter.

Two families are closed under adding independent copies, which makes the sum tractable in both. For a normal population, $X \sim N(\mu, \sigma^2)$ implies $\sum_{i=1}^{n} X_i \sim N(n\mu, n\sigma^2)$ and hence $\bar X \sim N(\mu, \sigma^2 / n)$ exactly. For a binomial population, $X_i \sim \mathrm{Bin}(m_i, p)$ implies $\sum_{i=1}^{n} X_i \sim \mathrm{Bin}(\sum_{i=1}^{n} m_i, p)$, which for a common $m$ reads $\mathrm{Bin}(mn, p)$.

Outside those two the population law is not closed under addition, so the sum cannot be written down exactly. The central limit theorem supplies an approximation instead, making $\bar X$ approximately normal for large $n$, with mean $\mu$ and variance $\sigma^2/n$.

The normal case admits a second derivation, which needs no theory of sums. Write the i.i.d. observations as the vector $\mathbf X = (X_1, \ldots, X_n)'$, whose joint density $f_{\mathbf X}(\mathbf x) = \prod_{i=1}^{n} f_X(x_i) = (2\pi\sigma^2)^{-n/2} \exp\!\bigl(-\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2\bigr)$ is the $N_n(\boldsymbol \mu, \sigma^2 I_n)$ density with $\boldsymbol \mu = (\mu, \ldots, \mu)'$. The sample mean is then a linear function of $\mathbf X$ rather than a sum to be analysed, so [linear transformations of a normal random vector](multivariate%20normal%20distribution.md#linear%20transformations) apply with $A = (\tfrac{1}{n} \;\; \tfrac{1}{n} \;\; \cdots \;\; \tfrac{1}{n})$ and gives $\bar X = A\mathbf X \sim N(A\boldsymbol \mu, A\boldsymbol \Sigma A') = N(\mu, \sigma^2/n)$, the same law reached above by a different route.

---

Flashcards for this section are as follows:

- where the distribution of the sample mean $\bar X$ of a random sample of size $n$ comes from, with no family assumed for the population ::@:: From the sum. $\bar X$ is $\sum_{i=1}^{n} X_i$ divided by $n$, so its law is that of the sum, rescaled.
- variance of the sum of $n$ independent copies $X_1, \ldots, X_n$ of a random variable with finite variance ::@:: $\operatorname{Var}(\sum_{i=1}^{n} X_i) = \sum_{i=1}^{n} \operatorname{Var}(X_i)$, which is $n\sigma^2$ when each copy has variance $\sigma^2$.
- sum of $n$ independent copies $X_i \sim N(\mu, \sigma^2)$ ::@:: $\sum_{i=1}^{n} X_i \sim N(n\mu, n\sigma^2)$.
- sample mean of size $n$ from a normal population $N(\mu, \sigma^2)$ ::@:: $\bar X \sim N(\mu, \sigma^2 / n)$ exactly, by dividing the sum by $n$.
- sum of independent copies $X_i \sim \mathrm{Bin}(m_i, p)$ ::@:: $\sum_{i=1}^{n} X_i \sim \mathrm{Bin}(\sum_{i=1}^{n} m_i, p)$, or $\mathrm{Bin}(mn, p)$ for a common $m$.
- distribution of the sample mean of size $n$ from a population whose family is not closed under addition ::@:: The central limit theorem makes it approximately normal for large $n$, with mean $\mu$ and variance $\sigma^2/n$.
- joint distribution of the observation vector $\mathbf X = (X_1, \ldots, X_n)'$ for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: $\mathbf X \sim N_n(\boldsymbol \mu, \sigma^2 I_n)$, where $\boldsymbol \mu = (\mu, \ldots, \mu)'$ and $I_n$ is the $n \times n$ identity matrix.
- joint density of the observation vector $\mathbf X = (X_1, \ldots, X_n)'$ for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: $f_{\mathbf X}(\mathbf x) = (2\pi\sigma^2)^{-n/2} \exp\!\bigl(-\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2\bigr)$, which is the $N_n(\boldsymbol \mu, \sigma^2 I_n)$ density.
- the law of $\bar X$ for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, reached through the multivariate normal rather than a theory of sums ::@:: $\bar X = A\mathbf X$ with $A = (\tfrac{1}{n}, \ldots, \tfrac{1}{n})$, so $\bar X \sim N(A\boldsymbol \mu, A\boldsymbol \Sigma A') = N(\mu, \sigma^2/n)$ with $\boldsymbol \Sigma = \sigma^2 I_n$.
- variance of the sample mean $\bar X$ for a random sample of size $n$ with population variance $\sigma^2$ ::@:: $\sigma^2/n$, since independence gives $\operatorname{Var}(\sum_{i=1}^{n} X_i) = \sum_{i=1}^{n} \operatorname{Var}(X_i)$ and dividing by $n$ divides the variance by $n$.
- which two properties of a random sample of size $n$ give $\operatorname{E}[\bar X] = \operatorname{E}[X_1]$ and $\operatorname{Var}(\bar X) = \operatorname{Var}(X_1)/n$ ::@:: Identical distribution gives the mean, and needs no independence. Independence gives the variance, and without it the covariances between copies enter.
- is the law of $\bar X$ for $X_i$ i.i.d. from $N(\mu, \sigma^2)$ or from $\mathrm{Bin}(m_i, p)$ exact, and why ::@:: Exact in both families, because each is closed under adding independent copies.
- law of the sample mean $\bar X$ of a random sample of size $n$ from a population whose family is not closed under addition ::@:: Not available exactly. The central limit theorem supplies an approximation for large $n$ instead.
- deriving $\bar X \sim N(\mu, \sigma^2/n)$ via the multivariate normal: $\mathbf X = (X_1, \ldots, X_n)'$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: $\mathbf X \sim N_n(\boldsymbol \mu, \sigma^2 I_n)$, where $\boldsymbol \mu = (\mu, \ldots, \mu)'$ and $I_n$ is the $n \times n$ identity matrix; [linear transformations](multivariate%20normal%20distribution.md#linear%20transformations) with $A = (\tfrac{1}{n} \;\; \cdots \;\; \tfrac{1}{n})$ then give $\bar X = A\mathbf X \sim N(\mu, \sigma^2/n)$.
- joint density of the observation vector $\mathbf X$ is not the only route: what the multivariate normal treats $\bar X$ as for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: A linear function $A\mathbf X$ of the observation vector, so the linear-transformation rule applies instead of any theory of sums.
