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

The _sample variance_ measures how far the observations of a sample spread around their average. The two forms $S_n^2$ and $S_{n-1}^2$ differ only in the denominator: $n$ in the first, $n - 1$ in the second. Both average the squared deviations $X_i - \bar X$, so the value says how tightly the observations cluster. The deviations are taken from the sample mean rather than from the population mean $\mu$, because $\bar X$ can be computed from the data and $\mu$ cannot.

---

Flashcards for this section are as follows:

- overview: for observations $X_1, \ldots, X_n$ around their average ::@:: A statistic measuring the spread of the observations around their average, written $S_n^2$ or $S_{n-1}^2$.
- what distinguishes the two sample variances $S_n^2$ and $S_{n-1}^2$ ::@:: They differ only in the denominator, which is $n$ in the first and $n - 1$ in the second.
- why the squared deviations are taken from $\bar X$ and not from the population mean $\mu$ ::@:: Because $\bar X$ can be computed from the data, while $\mu$ is an unknown parameter of the model.

## the two sample variances

The denominator is $n$ in $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$ and $n - 1$ in $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$. The two forms satisfy $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2}$, so one is recovered from the other by a single factor. Both are statistics, since every quantity they mention is read off the data.

---

Flashcards for this section are as follows:

- definition with denominator $n$: $S_n^2$ for a sample $X_1, \ldots, X_n$ ::@:: $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$.
- definition with denominator $n - 1$: $S_{n-1}^2$ for a sample $X_1, \ldots, X_n$ ::@:: $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$.
- relation between the two forms: $S_n^2$ and $S_{n-1}^2$ for a sample $X_1, \ldots, X_n$ ::@:: $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2}$.
- why $S_n^2$ and $S_{n-1}^2$ are statistics ::@:: Each mentions only $X_1, \ldots, X_n$ and $\bar X$, and the data supply all of them.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The two sample variances share the numerator $\sum_{i=1}^{n} (X_i - \bar X)^2$ and differ only in the denominator.

The bare sum $\sum_{i=1}^{n} (X_i - \bar X)^2$ is $n$ times $S_n^2$, and being a multiple of one of them does not make it the other. It has no denominator at all. Dividing it by $n + 1$ gives a denominator, but the wrong one, since $n + 1$ is neither $n$ nor $n - 1$. The population variance $\sigma^2$ is not a statistic: it is a parameter of the population rather than a function of the sample.

---

Flashcards for this section are as follows:

- $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$ for a sample $X_1, \ldots, X_n$ as a sample variance ::@:: Yes, it is the sum of squared deviations from the sample mean over the denominator $n$.
- $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$ for a sample $X_1, \ldots, X_n$ as a sample variance ::@:: Yes, the same sum over the denominator $n - 1$, the second of the two.
- $\frac{1}{n+1} \sum_{i=1}^{n} (X_i - \bar X)^2$ as one of the two sample variances ::@:: No, it divides by $n + 1$, which is neither $n$ nor $n - 1$.
- $\sum_{i=1}^{n} (X_i - \bar X)^2$ with no denominator as a sample variance ::@:: No, it has no denominator; it is $n$ times $S_n^2$, and a multiple of a sample variance is not one with a different denominator.
- the population variance $\sigma^2$ as a sample variance ::@:: No, it is a parameter of the population, not a statistic of the sample.

## distribution of the sample variance

For a random sample of size $n > 1$ from $N(\mu, \sigma^2)$, the scaled sample variance $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2} = \frac{\sum_{i=1}^{n} (X_i - \bar X)^2}{\sigma^2}$ follows $\chi^2(n - 1)$. Normality is what makes it exact: for a general distribution the scaled sample variance is not chi-squared.

The degrees of freedom are $n - 1$ and not $n$ because the $n$ deviations are not free quantities. They satisfy $\sum_{i=1}^{n} (X_i - \bar X) = 0$ identically, so one of them is determined by the others, and $n$ numbers held to sum to zero carry $n - 1$ degrees of freedom. The mean $\mu$ drops out, cancelling inside $X_i - \bar X$, so the scaled variance depends on $\sigma^2$ alone.

A chi-squared variable of $n - 1$ degrees of freedom has expectation $n - 1$, which gives $E[S_{n-1}^2] = \sigma^2$: the $n - 1$ form recovers the population variance without bias. The $n$ form does not: $E[S_n^2] = \frac{n - 1}{n} \sigma^2$, short of $\sigma^2$ by $\frac{n - 1}{n}$.

---

Flashcards for this section are as follows:

- distribution of the scaled sample variance: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\frac{(n-1) S_{n-1}^2}{\sigma^2} = \frac{n S_n^2}{\sigma^2} = \frac{\sum_{i=1}^{n} (X_i - \bar X)^2}{\sigma^2} \sim \chi^2(n - 1)$.
- degrees of freedom of the sample variance: for a sample of size $n$ ::@:: $n - 1$.
- parameters the distribution of $S_{n-1}^2$ depends on: $\mu$ and $\sigma^2$ of the normal sample ::@:: $\sigma^2$ alone, because $\mu$ cancels in $X_i - \bar X$.
- is the $\chi^2(n - 1)$ result exact ::@:: Yes, for a sample from a normal population; for a general distribution the scaled sample variance is not chi-squared.
- why the degrees of freedom are $n - 1$ and not $n$ ::@:: The deviations satisfy $\sum_{i=1}^{n} (X_i - \bar X) = 0$ identically, so one is determined by the others and only $n - 1$ of the $n$ are free.
- expectation of $S_{n-1}^2$ for a normal sample of size $n$ ::@:: $\sigma^2$, since a chi-squared variable of $n - 1$ degrees of freedom has expectation $n - 1$.
- expectation of $S_n^2$ for a normal sample of size $n$ ::@:: $\frac{n - 1}{n} \sigma^2$, short of $\sigma^2$ by the factor $\frac{n - 1}{n}$.

## independence from the sample mean

For a random sample of size $n > 1$ from $N(\mu, \sigma^2)$, $\bar X$ and $S_n^2$ are independent. The two statistics describe different features of a sample, its location and its spread, and independence says that knowledge of one gives nothing about the other.

In the quotient $\frac{\bar X - \mu}{S_n}$ independence is what makes the law computable. Neither part is known on its own, since the law of $S_n$ still carries $\sigma$, but independent parts combine, and the law of the quotient is then fixed with no unknown left in it. Without independence the two laws do not combine, so the quotient gives no interval for $\mu$ while $\sigma^2$ is unknown.

---

Flashcards for this section are as follows:

- independence of the sample mean and the sample variance: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\bar X$ and $S_n^2$ are independent.
- does $\bar X$ of a normal sample tell you anything about $S_n^2$ ::@:: No, the two are independent, so $\bar X$ carries no information about $S_n^2$ and $S_n^2$ none about $\bar X$.
- what the independence of $\bar X$ and $S_n^2$ licenses ::@:: The law of the quotient $\frac{\bar X - \mu}{S_n}$ can be read off, since independent parts combine; neither part is known on its own, because the law of $S_n$ still carries $\sigma$.

### proof by the multivariate normal route

The claim strengthens to the whole vector of deviations: $\bar X$ is independent of $(X_1 - \bar X, \ldots, X_n - \bar X)'$, of which $S_n^2$ is a function.

Take the observations as a vector $\mathbf X = (X_1, \ldots, X_n)' \sim N_n(\mu \mathbf 1, \sigma^2 I_n)$. One linear map produces the mean and the deviations, $$ \begin{pmatrix} \bar X \\ X_1 - \bar X \\ \vdots \\ X_n - \bar X \end{pmatrix} = \underbrace{\begin{pmatrix} \tfrac{1}{n} & \tfrac{1}{n} & \cdots & \tfrac{1}{n} \\ 1 - \tfrac{1}{n} & \tfrac{1}{n} & \cdots & \tfrac{1}{n} \\ \tfrac{1}{n} & 1 - \tfrac{1}{n} & \cdots & \tfrac{1}{n} \\ \vdots & \vdots & \ddots & \vdots \\ \tfrac{1}{n} & \tfrac{1}{n} & \cdots & 1 - \tfrac{1}{n} \end{pmatrix}}_{A \; (n+1) \times n} \mathbf X, $$ with mean vector $(\mu, 0, \ldots, 0)'$ because $E(X_i - \bar X) = 0$ for every $i$.

Transforming a normal vector gives the joint law $$ (\bar X, X_1 - \bar X, \ldots, X_n - \bar X)' \sim N_{n+1}(A \boldsymbol\mu, \sigma^2 A I_n A') = N_{n+1}(A \boldsymbol\mu, \sigma^2 A A'). $$

The covariance $\sigma^2 A A'$ is singular. The deviations sum to zero identically, $\sum_{i=1}^{n} (X_i - \bar X) = 0$, which makes $(0, 1, \ldots, 1)'$ a null vector.

Independence of a jointly normal scalar and vector reduces to covariances, and one index suffices. The rows of $A$ differ only in which coordinate carries the $1 - \tfrac{1}{n}$. For the first, $$ \operatorname{Cov}(\bar X, X_1 - \bar X) = \operatorname{Cov}(\bar X, X_1) - \operatorname{Cov}(\bar X, \bar X) = \operatorname{Cov}(\bar X, X_1) - \operatorname{Var}(\bar X). $$ The subtracted term is $\operatorname{Var}(\bar X) = \sigma^2/n$. The first term is $$ \operatorname{Cov}(\bar X, X_1) = \operatorname{Cov}\bigl(\tfrac{1}{n} X_1 + \tfrac{1}{n} \textstyle\sum_{j=2}^{n} X_j, \; X_1\bigr) = \tfrac{1}{n} \operatorname{Cov}(X_1, X_1) + \tfrac{1}{n} \textstyle\sum_{j=2}^{n} \operatorname{Cov}(X_j, X_1) = \tfrac{\sigma^2}{n} + 0 = \tfrac{\sigma^2}{n}, $$ since $X_1, \ldots, X_n$ are independent. Both terms are $\sigma^2/n$, so the covariance vanishes. Joint normality then gives independence.

---

Flashcards for this section are as follows:

- stronger form of the independence: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\bar X$ is independent of the whole vector $(X_1 - \bar X, \ldots, X_n - \bar X)'$, not only of $S_n^2$.
- linear map producing the sample mean and the deviations: $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$ ::@:: $(\bar X, X_1 - \bar X, \ldots, X_n - \bar X)' = A\mathbf X$ for the $(n+1) \times n$ matrix $A$ whose first row is $(\tfrac{1}{n} \cdots \tfrac{1}{n})$ and whose remaining rows each carry a $1 - \tfrac{1}{n}$ in one position.
- mean of the transformed vector: $A\boldsymbol\mu$ for $\mathbf X \sim N_n(\boldsymbol\mu, \sigma^2 I_n)$ ::@:: $(\mu, 0, \ldots, 0)'$, each deviation having mean zero.
- joint law of the sample mean and the deviations: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $(\bar X, X_1 - \bar X, \ldots, X_n - \bar X)' \sim N_{n+1}(A\boldsymbol\mu, \sigma^2 A A')$.
- null vector of the covariance $\sigma^2 A A'$: for the transform producing the mean and the deviations ::@:: $(0, 1, \ldots, 1)'$, because $\sum_{i=1}^{n} (X_i - \bar X) = 0$ identically.
- covariance whose vanishing proves the independence: $\operatorname{Cov}(\bar X, X_1 - \bar X)$ between $\bar X$ and the first deviation ::@:: $\operatorname{Cov}(\bar X, X_1) - \operatorname{Var}(\bar X) = \tfrac{\sigma^2}{n} - \tfrac{\sigma^2}{n} = 0$.
- value of $\operatorname{Cov}(\bar X, X_1)$: a random sample of size $n > 1$ from $N(\mu, \sigma^2)$ ::@:: $\tfrac{\sigma^2}{n}$, since $\operatorname{Cov}(X_j, X_1) = 0$ for every $j \ge 2$.
- variance of the sample mean: for a random sample of size $n$ from $N(\mu, \sigma^2)$ ::@:: $\operatorname{Var}(\bar X) = \sigma^2/n$.
