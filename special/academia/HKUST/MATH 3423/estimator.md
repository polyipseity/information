---
aliases:
  - estimator
  - estimators
  - point estimator
  - point estimators
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/estimator
  - language/in/English
---

# estimator

Estimation involves three different objects. A statistic $T(X)$ used to estimate the parameter $\theta$ is a _(point) estimator_ of $\theta$, a random variable rather than a number. Substituting the data $x = (x_1, \ldots, x_n)^\top$ gives an _estimate_, the number $T(x)$. Both are commonly written $\hat \theta$.

---

Flashcards for this section are as follows:

- definition: a statistic $T(X)$ used to estimate the parameter $\theta$ ::@:: A point estimator of $\theta$, a function of the sample and so a random variable. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- estimator versus estimate: $T(X)$ and $T(x)$ ::@:: The estimator is the random variable $T(X)$; the estimate is the number $T(x)$ obtained by substituting the data. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- notation for an estimator or an estimate of $\theta$ ::@:: $\hat \theta$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## estimand, estimator, and estimate

The parameter $\theta$ is the estimand: the fixed unknown quantity the estimation is about, one number settled in advance.

The estimator $T(X)$ is a rule applied to the sample. Two different samples generally give two different values of it, and that spread is what a distribution describes. The estimate $T(x)$ is that rule applied to the one sample actually collected, and it is the only one of the three the analyst can compute.

Only the estimator varies from one sample to the next, and only a quantity that varies has a distribution. Every question worth asking about an estimator is asked of that distribution rather than of the single value: how far off the rule runs, what interval to report, what to call significant. None of them can be asked of $T(x)$, which is already fixed, or of $\theta$, which was fixed before any data existed. The same asymmetry is why $\hat \theta$, which covers both, does not by itself say which one is meant.

---

Flashcards for this section are as follows:

- the three objects: $\theta$, $T(X)$ and $T(x)$ ::@:: The fixed unknown parameter, the random variable that guesses it, and the number that guess takes on the data. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- which one carries a sampling distribution: among $\theta$, $T(X)$ and $T(x)$ ::@:: The estimator $T(X)$, the only random one. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- which one is known to the analyst: among $\theta$, $T(X)$ and $T(x)$ ::@:: The estimate $T(x)$, computed from the data. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $\hat \theta$ ::@:: Either the estimator $T(X)$ or the estimate $T(x)$; the symbol alone does not say which is meant. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Take the unknown mean $\mu$ of a normal population $N(\mu, \sigma^2)$ as the quantity of interest, the estimand: fixed and unknown. The sample mean $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ is the estimator of $\mu$, a function of the sample and so a random variable. The number $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$ is the estimate that estimator takes on the collected data.

Any of the three can be mistaken for one of the others, and each mistake fails on its own ground. The realized value $\bar x$ is not an estimator, because it is a number and a number has no sampling distribution. The unknown mean $\mu$ is not an estimator either, because it is fixed rather than a function of the sample that changes from draw to draw. The sample mean $\bar X$ is not an estimate, because nothing has been observed yet and the quantity has no realized value.

---

Flashcards for this section are as follows:

- the unknown mean $\mu$ of a population $N(\mu, \sigma^2)$ as the estimand ::@:: Yes, it is the fixed unknown quantity that the estimation targets. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the sample mean $\bar X = \frac{1}{n} \sum_{i=1}^{n} X_i$ as the estimator of $\mu$ ::@:: Yes, it is a function of the random sample, so it has a sampling distribution. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the realized value $\bar x = \frac{1}{n} \sum_{i=1}^{n} x_i$ as an estimator of $\mu$ ::@:: No, it is a number, and a number has no sampling distribution. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the unknown mean $\mu$ as an estimator of $\mu$ ::@:: No, it is fixed and unknown, not a function of the sample. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the sample mean $\bar X$ as an estimate of $\mu$ ::@:: No, nothing has been observed yet, so $\bar X$ has no realized value. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## point-valued estimation

A point estimator gives one numerical guess for $\theta$ and reports nothing about how far off the guess may be.

That silence is not a matter of notation. Accuracy is a property of the rule rather than of the value it happens to take: $\bar x$ does not record which rule produced it, so on its own it cannot separate an accurate rule from an inaccurate one. Judging the guess needs the behavior of the rule over repeated samples.

How many numbers a point estimate carries is fixed by how many parameters are unknown. With one unknown parameter a point estimate is a single number on the real line, reported against the unknown $\mu$. With a mean and a standard deviation both unknown it is a pair in the plane, such as $(\bar x, s_{n-1})$ against $(\mu, \sigma)$. With three unknown parameters it is a triple, $(\hat \theta_1, \hat \theta_2, \hat \theta_3)$ against $(\theta_1, \theta_2, \theta_3)$. A point estimate is a shape set by the model, so calling an estimator a point estimate says nothing about how much information it carries.

None of this can be anticipated before the sample is drawn. What is known in advance is the estimator itself, and the distribution of the value it will take.

---

Flashcards for this section are as follows:

- what a point estimator reports: for the parameter $\theta$ ::@:: One numerical guess, with no statement of how far off it may be. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the single realized value $\bar x$ on its own: can it show how far off the rule behind it runs? ::@:: No, accuracy is a property of the rule over repeated samples, and the value does not record which rule produced it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- one-dimensional point estimation: $\bar x$ against $\mu$ ::@:: A point against the unknown point on the real line. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- two-dimensional point estimation: $(\bar x, s_{n-1})$ against $(\mu, \sigma)$ ::@:: A point in the plane against the pair of unknown parameters. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- three-dimensional point estimation: $(\hat \theta_1, \hat \theta_2, \hat \theta_3)$ against $(\theta_1, \theta_2, \theta_3)$ ::@:: A point against the triple of unknown parameters. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- before the sample is drawn: for a point estimator ::@:: Its value cannot be predicted; only its distribution is known. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## sampling distribution

The sampling distribution of $T(X)$ is the distribution of the value the rule takes over repeated samples. It is the only one of the three objects with a distribution, and it is what makes a statement about accuracy possible before any data arrive. Three things rest on it, all questions about the rule rather than the value: the properties of the estimator, the construction of a confidence interval, and the formulation of a test.

The first of the three is about the estimator itself, and it begins with where that distribution sits. An estimator is _biased_ for $\theta$ when the mean of its sampling distribution differs from $\theta$, and the size of the difference is its _bias_. Where the bias is zero the estimator is _unbiased_ for $\theta$. The spread of a distribution and its center are separate properties: an unbiased rule can still miss $\theta$ on almost every sample, since it says where the values gather and not how tightly. What centring rules out is a rule that leans one way.

The sample mean is where this lands. Each copy $X_i$ has the population mean $\mu$ and $\bar X$ averages the copies, so the mean of $\bar X$ is $\mu$. The distribution of $\bar X$ is therefore centered on the parameter it estimates, and $\bar X$ is unbiased for $\mu$. A rule carrying a bias gathers its values around a point away from the parameter, and drawing more samples of the same size would not move the center there. The center is what a rule is judged by.

The exact route computes the distribution from the model itself, with nothing assumed about the size of $n$. It is rare and difficult apart from the normal model, the exception that makes it available. The asymptotic route gives up on computing it exactly and approximates once $n$ is sufficiently large, the central limit theorem being the leading example.

The large-sample route needs machinery: a sample mean being normal does not make a function of it normal. The continuous mapping theorem passes a limit through a function of the data, and the delta method does the same to first order, at rate $\sqrt{n}$. Slutsky's lemma allows a factor converging in probability to be added or multiplied in without spoiling the result. Where a component is not normal to begin with, the central limit theorem supplies the normality and the weak law of large numbers supplies consistency.

The not-large-sample route ignores the model. Bootstrapping resamples the single collected data set and reads the resamples as if they were samples, which is why it needs no assumption about how large $n$ is.

---

Flashcards for this section are as follows:

- sampling distribution of $T(X)$: what it is ::@:: The distribution of the value $T(X)$ takes over repeated samples. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- an estimator whose sampling distribution has its mean equal to the parameter $\theta$ ::@:: Unbiased for that parameter, its bias being zero. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the bias of an estimator for the parameter $\theta$ ::@:: The gap between the center of its sampling distribution and the parameter, so zero for an unbiased estimator. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $E[T(X)] = \theta + 3$ for a parameter $\theta$ ::@:: Biased, since the center of its sampling distribution is not the parameter. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the mean of the sampling distribution of $\bar X$ for a random sample from a population with mean $\mu$ ::@:: $\mu$, since each copy has mean $\mu$ and $\bar X$ averages the copies, which makes $\bar X$ unbiased for $\mu$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- an unbiased estimator, on a single sample: does the value it takes equal the parameter? ::@:: No, since centring says where the values gather and not how tightly, a single value is off the parameter except on a set of samples of probability zero. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the sampling distribution of $T(X)$ is needed ::@:: Studying the properties of $T$, constructing confidence intervals and formulating tests all rest on it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- exactly determining a sampling distribution: when it is feasible ::@:: Rarely, or with difficulty, or not at all; the normal model is the exception. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- asymptotically determining a sampling distribution: for $n$ sufficiently large ::@:: The distribution is approximated, the central limit theorem being the leading example. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- tools for the large-sample route ::@:: The weak law of large numbers, the central limit theorem, convergence in probability, convergence in distribution, Slutsky's lemma, the delta method and the continuous mapping theorem. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- tools for the not-large-sample route ::@:: Bootstrapping, which resamples the single collected data set. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
