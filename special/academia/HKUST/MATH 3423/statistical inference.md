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

- definition ::@:: Reaching a conclusion about something from known evidence; "statistical" refers to the data and "inference" to the conclusion. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why a probability distribution is used: for the unknown quantity $X$ ::@:: Before the corresponding experiment is performed, $X$ is unpredictable; a coin before it is tossed is the illustration. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- mission: with data and a parametric model for $X$ ::@:: Estimate the parameter(s) $\theta$ of the distribution of the target random variable. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## data

Data are the values that the target random variable $X$ actually took. Write $x_1, \ldots, x_n$ for the $n$ of them and $X_1, \ldots, X_n$ for the copies of $X$ that produced them. Each $x_i$ is a known number once the sample is in, and each $X_i$ stays a random variable until then. Before sampling, what is known is the joint distribution of the copies, and nothing at all about their realized values.

A quantity computed from the data, the sample mean for instance, is a fixed number once the sample is in, so a conclusion drawn from it is a statement about something settled. What connects that statement to $\theta$ is the distribution the data were drawn from: the same observed values are more likely under some values of $\theta$ than under others. After sampling the uncertainty that inference has to resolve is therefore in the parameter, not in the data.

---

Flashcards for this section are as follows:

- definition: given observations $x_1, \ldots, x_n$ of the target random variable $X$ ::@:: The actual values of $X$, each a known number once the sample is drawn. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- notation: $x_i$ versus $X_i$ ::@:: $X_i$ is the $i$-th copy of $X$ and $x_i$ its actual value; uppercase letters denote random variables and lowercase letters their realizations. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- when the values become known ::@:: After sampling; before it, only the joint distribution of the copies is known. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why data estimate the parameter: under a parametric model for $X$ ::@:: The observed values are more likely under some values of $\theta$ than under others, so they carry information about which one is true. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The distinction is between a number and the variable that produced it. After sampling, $x_1 = 3.2$ is data: a known number, and the realized value of the copy $X_1$. Before sampling, $X_1$ is a random variable and $x_1$ is not yet available. An average shows the same split: $\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i$ is a random variable, and $\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i$ is the average of the data. The letter records which of the two is meant.

Writing $X_1 = 3.2$ after sampling asserts that a random variable equals a constant, which it does not. Reporting $\bar x$ before sampling states a number that cannot yet be computed; the object to report is $\bar X$. Calling the observed $x_i$ random treats the data as uncertain, but the data are settled numbers and the parameter is what stays uncertain.

---

Flashcards for this section are as follows:

- $x_1 = 3.2$ after the sample is drawn: data or a random variable? ::@:: Data, a known number; the random variable that produced it is $X_1$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $X_1$ before the sample is drawn: data or a random variable? ::@:: A random variable, whose realized value $x_1$ is not yet available. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $\bar X$ versus $\bar x$ before the sample is drawn ::@:: $\bar X$ is the random variable and $\bar x$ the average of the data, available only after sampling. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- writing $X_1 = 3.2$ after sampling: correct notation? ::@:: No, it makes a random variable equal a constant; the observed value is $x_1 = 3.2$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reporting $\bar x$ before the sample is drawn ::@:: Not available, since $\bar x$ is a function of data that have not been observed; the object to report is $\bar X$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what stays uncertain after the data are observed: for observed $x_1, \ldots, x_n$ ::@:: The unknown parameter, not the data, which are known numbers. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## modes of inference

With data in hand and a model for the distribution of $X$, there are three standard ways to report what the data say about $\theta$. They differ in the kind of object they produce. Point estimation produces a single number: an estimate of $\theta$ from the data. The sample mean serves when the unknown parameter is a population mean and the sample variance when it is a population variance. Where the model is not a normal one, the estimate is usually obtained by the method of moments or by maximum likelihood. Nothing in a point estimate says how far it may be from $\theta$.

Interval estimation produces a range instead of a single value, and a confidence interval is the standard form of it. What separates an interval from a point is the level it carries. That level states how often the procedure that produced it brackets the true parameter. The statement is about repeated sampling, not about the interval already computed.

Hypothesis testing produces a decision rather than a value. The data are compared with a proposed value of $\theta$, and the outcome is a rejection or a non-rejection of that proposal. The accuracy of the decision is measured the same way: the level $\alpha$ is the rate at which a true proposal is wrongly rejected over repeated samples.

A level and an error rate are both claims about how the reported object behaves over repetitions of the sampling procedure. The distribution of the estimator is what describes that behavior, so interval estimation and hypothesis testing need it, exact or approximate, and point estimation does not.

---

Flashcards for this section are as follows:

- modes of inference: from a parametric model ::@:: Point estimation, interval estimation, and hypothesis testing. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- point estimation: as a guess for $\theta$ ::@:: A single value: the sample mean or sample variance for an unknown population mean or variance, otherwise method of moments or maximum likelihood. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- interval estimation: as a guess for $\theta$ ::@:: An interval-valued guess, a confidence interval, rather than a point. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- hypothesis testing ::@:: A test of hypotheses about the value of the parameter. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why interval estimation and hypothesis testing need the distribution of the estimator ::@:: Because their level or error rate is a claim about repeated sampling, and the estimator's distribution is what determines it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what a point estimate leaves unsaid: about how far the value may be from $\theta$ ::@:: It reports a single number and makes no claim of accuracy, so nothing about its error has to be quantified. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples for each mode

Reporting $\bar x$ as the guess for $\mu$ is point estimation, one number with no statement of how far off it may be. The interval $\bar x \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ for $\mu$ is interval estimation, carrying the level $1 - \alpha$. Testing whether the data are incompatible with $H_0: \mu = \mu_0$ at level $\alpha$ is hypothesis testing.

Giving $\bar x$ together with its standard error is point estimation, because a standard error describes the estimator rather than bracketing $\mu$. An interval with no level attached, such as $(\bar x - 1, \bar x + 1)$, is not interval estimation either, because it carries no coverage statement. Reporting $P(\mu \in A \mid x) = 0.95$ is none of the three modes: it is a statement about the distribution of $\mu$ given the data, and it needs a prior.

---

Flashcards for this section are as follows:

- reporting $\bar x$ as the guess for $\mu$: which mode of inference? ::@:: Point estimation, a single value with no statement of how far off it may be. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reporting $\bar x \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ for $\mu$: which mode of inference? ::@:: Interval estimation, an interval built at level $1 - \alpha$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- testing $H_0: \mu = \mu_0$ at level $\alpha$: which mode of inference? ::@:: Hypothesis testing, whose answer is a decision. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reporting $\bar x$ together with its standard error: which mode of inference? ::@:: Point estimation, because a standard error describes the estimator rather than bracketing $\mu$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reporting the interval $(\bar x - 1, \bar x + 1)$ with no level stated: interval estimation? ::@:: No, an interval with no level carries no coverage statement. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reporting $P(\mu \in A \mid x) = 0.95$: one of the three modes of inference? ::@:: No, it is a statement about the distribution of $\mu$ given the data, which requires a prior. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
