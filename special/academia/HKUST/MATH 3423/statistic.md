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

Every quantity a statistic needs is therefore in hand once the sample has been drawn, which is what makes a statistic observable. The parameter it is used to learn about is not.

---

Flashcards for this section are as follows:

- what is a statistic of a sample $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ with $\mu$ and $\sigma$ unknown ::@:: A real- or vector-valued function of the sample that no unknown parameter enters for any realization, so the data alone give its value.
- when must a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ be evaluable ::@:: The moment the data arrive, since the rule is fixed in advance and $\mu$ and $\sigma$ are still unknown then.
- why is a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ computable once the sample is drawn ::@:: Every quantity it needs is a function of the data, so all of them are in hand.

## dependence on unknown parameters

The test is what must be known to evaluate a candidate: if an unknown parameter is on that list, the candidate is not a statistic. By that test $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is one, and every symbol in it is a data value. So is $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$.

The test asks about the parameter, not about the notation. A quantity may stand in for an unknown parameter whenever it is itself computable from the data. Nor does the definition impose a shape on the function, so a statistic need not be an average and need not be linear.

---

Flashcards for this section are as follows:

- how to decide whether a candidate function $T$ of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ is a statistic ::@:: List what must be known to evaluate $T$; an unknown parameter such as $\mu$ or $\sigma$ disqualifies it.
- must a formula for a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ mention $\mu$ or $\sigma$ to be about them ::@:: No; the test asks whether an unknown parameter was used, not which letters the formula contains.
- must a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ be an average or a linear function of the observations ::@:: No; any function of the data qualifies, however indirect.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The sample mean $\bar X$, the sample variance $S_{n-1}^{2}$, and the sample median are all statistics, because every quantity they mention is read off the data. The median is the order statistic $X_{(\lceil n/2 \rceil)}$, found by sorting the observed values.

The average squared deviation from the unknown mean, $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$, is not a statistic. Evaluating it requires $\mu$, and no data can supply it. A term that mentions an unknown $\sigma$ fails on the same ground, with $\bar X + \frac{1}{\sigma}$ staying uncomputable until $\sigma$ is known.

Dividing one observation's deviation from the sample mean by the sample standard deviation measures it in units of the spread, which removes the scale of the data. In $\frac{X_1 - \bar X}{S_{n-1}}$ the $\bar X$ and $S_{n-1}$ sit where $\mu$ and $\sigma$ would sit, but both are functions of the sample, so no unknown parameter enters and the expression is a statistic. The general point holds: a function that mentions an estimator of a parameter is still a statistic, because the estimator is itself a function of the data.

The reciprocal $\frac{1}{\bar X}$ is a statistic too, being a function of the sample mean. It is undefined at $\bar X = 0$, an event of probability zero for a continuous variable.

---

Flashcards for this section are as follows:

- is $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ with $\mu$ and $\sigma$ unknown ::@:: Yes; the data give every $X_i$ and no unknown parameter is needed.
- is the sample median $X_{(\lceil n/2 \rceil)}$ of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ a statistic ::@:: Yes; it is an order statistic, read off once the observed values are sorted.
- is $\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2$ a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ with $\mu$ unknown ::@:: No; evaluating it needs $\mu$, which the sample cannot supply.
- is $\frac{X_1 - \bar X}{S_{n-1}}$ a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$, $n > 1$, where $\bar X$ is the sample mean and $S_{n-1}$ the sample standard deviation ::@:: Yes; both are functions of the data and the formula names no unknown parameter.
- is $\frac{1}{\bar X}$ a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ on the samples with $\bar X \ne 0$ ::@:: Yes; it is a function of the sample mean, defined wherever the sample mean is nonzero.

## sample mean and sample variance

$\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is a random variable, so its value is not settled until the sample is drawn. The average of the data, $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$, is that statistic evaluated on the observed values, and is a number. The sample variance splits the same way: a statistic before the sample is drawn, a number after it.

The sample mean is the estimator of the unknown population mean and $\bar x$ the estimate it yields. The sample variance measures the spread of the data around the sample mean.

---

Flashcards for this section are as follows:

- which statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ estimates the population variance $\sigma^2$ ::@:: The sample variance, the spread of the data around the sample mean.
- how does the average of the data $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$ differ from the statistic $\bar X$ of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ ::@:: $\bar x$ is $\bar X$ evaluated on the observed values, so the average is a number while the statistic remains a random variable.
- for $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ with $\mu$ unknown, which is the estimator of the population mean and which is the estimate it yields ::@:: The sample mean $\bar X$ is the estimator, and the average of the data $\bar x$ is the estimate.
- what is fixed about a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ before the sample is drawn ::@:: The rule, not the value.
- where does the distribution of a statistic of $X_1, \ldots, X_n$ from $N(\mu, \sigma^2)$ come from ::@:: From the model, not from the data.
