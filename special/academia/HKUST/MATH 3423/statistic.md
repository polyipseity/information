---
aliases:
  - sample statistic
  - statistic
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/statistic
  - language/in/English
---

# statistic

A _statistic_ is a function of the sample, written $T(X) = T(X_1, \ldots, X_n)$, that can be evaluated from the data alone. It may not require any unknown quantity, including the parameter $\theta$ of the model.

A statistic is a rule fixed in advance, and it has to be evaluable at the moment the data arrive, when $\theta$ is still unknown.

Every quantity a statistic needs is therefore in hand once the sample has been drawn, which is what makes a statistic observable. The parameter it is used to learn about is not.

---

Flashcards for this section are as follows:

- definition: for a sample $X_1, \ldots, X_n$ ::@:: A real- or vector-valued function of the sample whose value contains no unknown parameter for any $X$, so it can be computed from the data alone.
- restriction on a statistic: and the parameter $\theta$ ::@:: Computing it must not require any unknown quantity, so it may not depend on $\theta$.
- why a statistic may not use an unknown parameter: for a rule meant to be applied once the data arrive ::@:: It is fixed in advance and has to be evaluable at that moment, when the parameter is still out of reach.
- why a statistic is observable: for a sample that has been drawn ::@:: Every quantity it needs is in hand, since none of them was unknown.

## dependence on unknown parameters

The test is what must be known to evaluate a candidate: if an unknown parameter is on that list, the candidate is not a statistic. By that test $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is one, and every symbol in it is a data value. So is $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$.

The test asks about the parameter, not about the notation. Nothing requires a formula to mention $\mu$ or $\sigma$ in order to be about them, and a quantity may stand in for an unknown parameter whenever it is itself computable from the data. Nor does the definition impose a shape on the function, so a statistic need not be an average and need not be linear.

---

Flashcards for this section are as follows:

- how to decide whether a function of the sample is a statistic: given a candidate $T(X)$ ::@:: Check what must be known to evaluate it; any unknown parameter such as $\theta$ or $\mu$ disqualifies it.
- what the test actually examines: for a formula that mentions an unfamiliar-looking quantity ::@:: Whether an unknown parameter was used, not which letters the formula happens to contain.
- must a statistic be an average or a linear function of the observations ::@:: No, any function of the data qualifies, however indirect.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The sample mean $\bar X$, the sample variance $S_{n-1}^{2}$, and the sample median are all statistics, because every quantity they mention is read off the data. The median is the order statistic $X_{(\lceil n/2 \rceil)}$, found by sorting the observed values.

The average squared deviation from the unknown mean, $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$, is not a statistic. Evaluating it requires $\mu$, and no data can supply it. A term that mentions an unknown $\sigma$ fails on the same ground, with $\bar X + \frac{1}{\sigma}$ staying uncomputable until $\sigma$ is known.

Dividing one observation's deviation from the sample mean by the sample standard deviation measures it in units of the spread, which removes the scale of the data. In $\frac{X_1 - \bar X}{S_{n-1}}$ the $\bar X$ and $S_{n-1}$ sit where $\mu$ and $\sigma$ would sit, but both are functions of the sample, so no unknown parameter enters and the expression is a statistic. The general point holds: a function that mentions an estimator of a parameter is still a statistic, because the estimator is itself a function of the data.

The reciprocal $\frac{1}{\bar X}$ is a statistic too, being a function of the sample mean. It is undefined at $\bar X = 0$, an event of probability zero for a continuous variable.

---

Flashcards for this section are as follows:

- sample mean $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$: statistic or not, in a model with unknown $\mu$ and $\sigma$ ::@:: Yes, it is a statistic, since the data give every $X_i$ and no unknown parameter is needed.
- sample median $X_{(\lceil n/2 \rceil)}$ of a continuous variable: statistic or not ::@:: Yes, it is an order statistic, read off after the observed values are sorted.
- $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$ for unknown $\mu$: statistic or not ::@:: No, it mentions the unknown $\mu$, which the sample cannot supply.
- $\frac{X_1 - \bar X}{S_{n-1}}$: statistic or not, though it mentions estimators of $\mu$ and $\sigma$ ::@:: Yes, $\bar X$ and $S_{n-1}$ are functions of the data, and the formula names no unknown parameter.
- $\frac{1}{\bar X}$ on the samples with $\bar X \ne 0$: statistic or not ::@:: Yes, it is a function of the statistic $\bar X$, defined wherever the sample mean is nonzero.

## sample mean and sample variance

$\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is a random variable, so its value is not settled until the sample is drawn. The average of the data, $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$, is that statistic evaluated on the observed values, and is a number. The sample variance splits the same way: a statistic before the sample is drawn, a number after it.

The sample mean is the estimator of the unknown population mean and $\bar x$ the estimate it yields, while the sample variance measures the spread of the data around the sample mean.

---

Flashcards for this section are as follows:

- population variance and the statistic that estimates it ::@:: The sample variance, the spread of the data around the sample mean.
- the average of the data $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$ against the statistic $\bar X$ ::@:: The statistic evaluated on the observed values, so the average is a number while the statistic remains a random variable.
- the estimator of the unknown population mean, and the estimate it yields ::@:: The sample mean is the estimator, and the average of the data is the estimate.
- what is fixed about a statistic before the sample is drawn ::@:: The rule, not the value. The distribution the statistic follows comes from the model, not from the data.
