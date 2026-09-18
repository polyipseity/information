---
aliases:
  - sample statistic
  - statistic
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/statistic
  - language/in/English
---

# statistic

A _statistic_ is a function of the sample, written $T(X) = T(X_1, \ldots, X_n)$, whose value can be computed from the data alone: computing it must not require any unknown quantity, in particular not the parameter $\theta$ of the model. A statistic is thus observable, while the parameter it is used to learn about is not.

---

Flashcards for this section are as follows:

- definition: for a sample $X_1, \ldots, X_n$ ::@:: A real- or vector-valued function of the sample whose value contains no unknown parameter for any $X$, so it can be computed from the data alone.
- how the data are turned into an estimate: for the unknown parameter $\theta$ ::@:: By a statistic, a function of the sample containing no unknown parameter.
- restriction on a statistic: and the parameter $\theta$ ::@:: Computing it must not require any unknown quantity, so it may not depend on $\theta$.

## dependence on unknown parameters

Whether a function of the sample is a statistic depends on what must be known to evaluate it. The sample mean $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ and the sample variance $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$ both are statistics, because the data supply every quantity they mention. By contrast $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$ is not, because it mentions the unknown $\mu$.

---

Flashcards for this section are as follows:

- how to decide whether a function of the sample is a statistic: given a candidate $T(X)$ ::@:: Check what must be known to evaluate it; any unknown parameter such as $\theta$ or $\mu$ disqualifies it.
- why $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is a statistic ::@:: The data supply every quantity it mentions.
- why $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$ is a statistic ::@:: It is a function of the copies alone, so the data supply every quantity it mentions.
- why $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$ is not a statistic: case of unknown $\mu$ ::@:: It mentions the unknown $\mu$, so the data alone cannot evaluate it.

## sample mean and sample variance

The sample mean and the sample variance, which this course uses most, estimate the unknown population mean and the unknown population variance. The sample mean averages the observed values, $x_1, \ldots, x_n$ giving $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$, and the sample variance measures their spread around that average.

---

Flashcards for this section are as follows:

- population mean and the statistic that estimates it ::@:: The sample mean, the average of the observed values.
- population variance and the statistic that estimates it ::@:: The sample variance, the spread of the data around the sample mean.
