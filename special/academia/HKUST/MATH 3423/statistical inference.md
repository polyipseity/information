---
aliases:
  - inferential statistics
  - statistical inference
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/statistical_inference
  - language/in/English
---

# statistical inference

_Statistical inference_ draws a conclusion about an unknown quantity from evidence that is already in hand. The data are the evidence; the conclusion is the inference. Before the experiment that produces it, the value of a random variable $X$ cannot be predicted, as a coin's cannot be before it is tossed. The distribution of $X$ describes that unpredictability. The working model is parametric: the form of the distribution is fixed, and the parameters it leaves open are written $\theta$, whether there is one of them or several. A normal population whose $\mu$ and $\sigma^2$ are both unknown is the case that keeps recurring.

---

Flashcards for this section are as follows:

- what statistical inference is ::@:: Reaching a conclusion about an unknown quantity from evidence already in hand.
- why a probability distribution is used for a random variable $X$ ::@:: Before $X$ is observed its value cannot be predicted; a coin before it is tossed is the illustration.
- what inference aims at when data and a parametric model for $X$ are given ::@:: The unknown parameter or parameters $\theta$ of the distribution of $X$, estimated from the data.

## data

Data are the values that the target random variable $X$ actually took. Write $x_1, \ldots, x_n$ for the $n$ of them and $X_1, \ldots, X_n$ for the copies of $X$ that produced them. Before sampling, what is known is the joint distribution of the copies, and nothing at all about their realized values.

A quantity computed from the data, the sample mean for instance, is a fixed number once the sample is in, so a conclusion drawn from it is a statement about something settled. What connects that statement to $\theta$ is the distribution the data were drawn from: the same observed values are more likely under some values of $\theta$ than under others.

---

Flashcards for this section are as follows:

- what the data for a random variable $X$ are ::@:: The values $x_1, \ldots, x_n$ that $X$ actually took, each a known number once the sample is drawn.
- the notation $X_i$ against $x_i$ for the $i$-th copy of a random variable $X$ ::@:: $X_i$ is the $i$-th copy of $X$ and stays a random variable, $x_i$ is its realized value.
- when the data $x_1, \ldots, x_n$ of the copies $X_1, \ldots, X_n$ become known ::@:: After the sample is drawn; before it only the joint distribution of the copies is known.
- why the data estimate the parameter $\theta$ of the distribution of $X$ ::@:: The observed values are more likely under some values of $\theta$ than under others, so they carry information about which one is true.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The distinction is between a number and the variable that produced it. After sampling, $x_1 = 3.2$ is data: a known number, and the realized value of the copy $X_1$. Before sampling, $X_1$ is a random variable and $x_1$ is not yet available. An average shows the same split: $\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i$ is a random variable, and $\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i$ is the average of the data. The letter records which of the two is meant.

Writing $X_1 = 3.2$ after sampling asserts that a random variable equals a constant, which it does not. Reporting $\bar x$ before sampling states a number that cannot yet be computed; the object to report is $\bar X$. Calling the observed $x_i$ random treats the data as uncertain, but the data are settled numbers and the parameter is what stays uncertain.

---

Flashcards for this section are as follows:

- a realized value $x_1 = 3.2$ of a random variable $X$ recorded after the sample is drawn: data or a random variable? ::@:: Data, a known number; the random variable that produced it is $X_1$.
- the copy $X_1$ of a random variable $X$ before the sample is drawn: data or a random variable? ::@:: A random variable, whose realized value $x_1$ is not yet available.
- the sample mean $\bar X$ against the average $\bar x$ of the data $x_1, \ldots, x_n$, before the sample is drawn from copies $X_1, \ldots, X_n$ of a random variable $X$ ::@:: $\bar X$ is the random variable, and $\bar x$ is the average of the data, available only after sampling.
- writing $X_1 = 3.2$ for the copy $X_1$ of a random variable $X$ after sampling: correct notation? ::@:: No, it makes a random variable equal a constant; the observed value is $x_1 = 3.2$.
- the average $\bar x$ of data $x_1, \ldots, x_n$ before the sample is drawn: what can be reported? ::@:: Only the sample mean $\bar X$, a random variable; $\bar x$ is a function of data that have not been observed.
- what stays uncertain after the data $x_1, \ldots, x_n$ of a random variable $X$ with unknown parameter $\theta$ are observed ::@:: The parameter $\theta$, not the data, which are known numbers.

## modes of inference

With data in hand and a model for the distribution of $X$, there are three standard ways to report what the data say about $\theta$. They differ in the kind of object they produce. Point estimation produces a single number: an estimate of $\theta$ from the data. Where the model is not a normal one, the estimate is usually obtained by the method of moments or by maximum likelihood.

Interval estimation produces a range instead of a single value, and a confidence interval is the standard form of it. What separates an interval from a point is the level it carries. That level states how often the procedure that produced it brackets the true parameter. The statement is about repeated sampling, not about the interval already computed.

Hypothesis testing produces a decision rather than a value. The data are compared with a proposed value of $\theta$, and the outcome is a rejection or a non-rejection of that proposal. The accuracy of the decision is measured the same way: the level $\alpha$ is the rate at which a true proposal is wrongly rejected over repeated samples.

A level and an error rate are both claims about how the reported object behaves over repetitions of the sampling procedure. The distribution of the estimator is what describes that behavior, so interval estimation and hypothesis testing need it, exact or approximate, and point estimation does not.

---

Flashcards for this section are as follows:

- which three modes of inference are standard under a parametric model for a random variable $X$ with unknown parameter $\theta$ ::@:: Point estimation, interval estimation, and hypothesis testing.
- what point estimation reports for an unknown parameter $\theta$ ::@:: A single value; the sample mean for an unknown population mean and the sample variance for an unknown population variance.
- how an unknown parameter $\theta$ of a non-normal model for $X$ is estimated ::@:: Usually by the method of moments or by maximum likelihood.
- what interval estimation reports for an unknown parameter $\theta$ ::@:: A range rather than a single value; a confidence interval is the standard form.
- what hypothesis testing about an unknown parameter $\theta$ reports ::@:: A decision, a rejection or a non-rejection of a proposed value of $\theta$.
- why interval estimation and hypothesis testing need the sampling distribution of an estimator of the unknown parameter $\theta$ ::@:: Their level and error rate are claims about repeated sampling, and the estimator's sampling distribution is what determines them.
- what a point estimate of the unknown parameter $\theta$ leaves unsaid ::@:: How far the value may be from $\theta$; it reports a single number and claims no accuracy.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples for each mode

Reporting $\bar x$ as the guess for $\mu$ is point estimation, one number with no statement of how far off it may be. The interval $\bar x \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ for $\mu$ is interval estimation, carrying the level $1 - \alpha$. Testing whether the data are incompatible with $H_0: \mu = \mu_0$ at level $\alpha$ is hypothesis testing.

Giving $\bar x$ together with its standard error is point estimation, because a standard error describes the estimator rather than bracketing $\mu$. An interval with no level attached, such as $(\bar x - 1, \bar x + 1)$, is not interval estimation either, because it carries no coverage statement. Reporting $P(\mu \in A \mid x) = 0.95$ is none of the three modes: it is a statement about the distribution of $\mu$ given the data, and it needs a prior.

---

Flashcards for this section are as follows:

- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the sample mean $\bar x$ reported as the guess for $\mu$: which mode of inference? ::@:: Point estimation, a single value with no statement of how far off it may be.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the interval $\bar x \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ reported for $\mu$, where $z_{\alpha/2}$ is the standard normal quantile with upper tail area $\alpha/2$: which mode of inference? ::@:: Interval estimation, an interval built at level $1 - \alpha$.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the test of $H_0: \mu = \mu_0$ at level $\alpha$: which mode of inference? ::@:: Hypothesis testing, whose answer is a decision.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the sample mean $\bar x$ reported together with its standard error: which mode of inference? ::@:: Point estimation, because a standard error describes the estimator rather than bracketing $\mu$.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the interval $(\bar x - 1, \bar x + 1)$ reported with no level stated: interval estimation? ::@:: No, an interval with no level carries no coverage statement.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the probability $P(\mu \in A \mid x) = 0.95$ reported for a set $A$ given the data $x$: one of the three modes of inference? ::@:: No, it is a statement about the distribution of $\mu$ given the data, which requires a prior.
