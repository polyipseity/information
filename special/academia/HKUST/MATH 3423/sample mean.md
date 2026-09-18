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

The sample mean of a random sample $X_1, \ldots, X_n$ is $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$; the average of the data $x_1, \ldots, x_n$ is written $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$. It is the natural estimator of the unknown population mean $\mu$. The first is a random variable and the second a number, and before the sample is drawn the value of $\bar X$ is unpredictable.

---

Flashcards for this section are as follows:

- definition: for a random sample $X_1, \ldots, X_n$ ::@:: The average of the copies, $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$.
- average of the data: written $\bar x$ ::@:: $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$, a number rather than a random variable.
- which quantity of the population $\bar X$ estimates ::@:: The unknown population mean $\mu$.
- predictability of $\bar X$: before drawing a sample ::@:: Its value cannot be predicted; only its distribution is known in advance.

## distribution of the sample mean

The sample mean is a sum divided by $n$, so its distribution follows from that of $\sum_{i=1}^{n} X_i$. Independence gives $\operatorname{Var}(\sum_{i=1}^{n} X_i) = \sum_{i=1}^{n} \operatorname{Var}(X_i)$. For a normal population, $X \sim N(\mu, \sigma^2)$ implies $\sum_{i=1}^{n} X_i \sim N(n\mu, n\sigma^2)$ and hence $\bar X \sim N(\mu, \sigma^2 / n)$ exactly; for a binomial population, $X_i \sim \mathrm{Bin}(m_i, p)$ implies $\sum_{i=1}^{n} X_i \sim \mathrm{Bin}(\sum_{i=1}^{n} m_i, p)$, which for a common $m$ reads $\mathrm{Bin}(mn, p)$. Otherwise the central limit theorem gives $\bar X$ an approximately normal distribution for large $n$.

---

Flashcards for this section are as follows:

- distribution of $\bar X$: general route ::@:: It is a sum divided by $n$, so its distribution follows from that of $\sum_{i=1}^{n} X_i$.
- variance of a sum of independent copies: $\operatorname{Var}(\sum_{i=1}^{n} X_i)$ ::@:: $\operatorname{Var}(\sum_{i=1}^{n} X_i) = \sum_{i=1}^{n} \operatorname{Var}(X_i)$.
- sum of independent normal copies: $X_i \sim N(\mu, \sigma^2)$ ::@:: $\sum_{i=1}^{n} X_i \sim N(n\mu, n\sigma^2)$.
- sample mean from a normal population: $X \sim N(\mu, \sigma^2)$ ::@:: $\bar X \sim N(\mu, \sigma^2 / n)$ exactly, by dividing the sum by $n$.
- sum of independent binomial copies: $X_i \sim \mathrm{Bin}(m_i, p)$ ::@:: $\sum_{i=1}^{n} X_i \sim \mathrm{Bin}(\sum_{i=1}^{n} m_i, p)$, or $\mathrm{Bin}(mn, p)$ for a common $m$.
- distribution of $\bar X$ for large $n$: without a normal population ::@:: The central limit theorem makes it approximately normal.
