---
aliases:
  - empirical variance
  - sample variance
  - sample variances
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/sample_variance
  - language/in/English
---

# sample variance

The _sample variance_ measures how far the observations of a sample spread around their average. It is written with one of two denominators, $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$ or $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$, related by $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2}$. Like the sample mean, it is a statistic, and for a normal sample both its distribution and its relation to the sample mean are known exactly.

---

Flashcards for this section are as follows:

- overview: for observations $X_1, \ldots, X_n$ around their average ::@:: A statistic measuring how far the observations spread around their average, written $S_n^2$ or $S_{n-1}^2$ according to the denominator.
- definition with denominator $n$: $S_n^2$ for a sample $X_1, \ldots, X_n$ ::@:: $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$.
- definition with denominator $n - 1$: $S_{n-1}^2$ for a sample $X_1, \ldots, X_n$ ::@:: $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$.
- relation between the two forms: $S_n^2$ and $S_{n-1}^2$ for a sample $X_1, \ldots, X_n$ ::@:: $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2}$, so they differ only by the choice of denominator, $n$ or $n - 1$.

## distribution of the sample variance

For a random sample of size $n > 1$ from $N(\mu, \sigma^2)$, the scaled sample variance $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2} = \frac{\sum_{i=1}^{n} (X_i - \bar X)^2}{\sigma^2}$ follows $\chi^2(n - 1)$. The degrees of freedom are one less than the sample size, and the mean $\mu$ cancels in $X_i - \bar X$, so the distribution depends on $\sigma^2$ alone.

---

Flashcards for this section are as follows:

- distribution of the scaled sample variance: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2} = \frac{\sum_{i=1}^{n} (X_i - \bar X)^2}{\sigma^2} \sim \chi^2(n - 1)$.
- degrees of freedom of the sample variance: for a sample of size $n$ ::@:: $n - 1$, one less than the sample size.
- parameters the distribution of $S_{n-1}^2$ depends on: $\mu$ and $\sigma^2$ of the normal sample ::@:: $\sigma^2$ alone, because $\mu$ cancels in $X_i - \bar X$.

## independence from the sample mean

For a random sample of size $n > 1$ from $N(\mu, \sigma^2)$, $\bar X$ and $S_n^2$ are independent. The sample mean of a normal sample carries no information about the spread of the observations.

---

Flashcards for this section are as follows:

- independence of the sample mean and the sample variance: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\bar X$ and $S_n^2$ are independent.
