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

When a statistic $T(X)$ is used to estimate the parameter $\theta$, it is called a _(point) estimator_ of $\theta$. It is a random variable: before the sample is drawn its value is unpredictable, and only its distribution is known. Substituting the data $x = (x_1, \ldots, x_n)^\top$ gives the corresponding number, an _estimate_. Both are commonly written $\hat \theta$.

---

Flashcards for this section are as follows:

- definition: a statistic used to estimate the parameter $\theta$ ::@:: A point estimator of $\theta$; being a function of the sample, it is a random variable.
- estimator versus estimate: $T(X)$ and $T(x)$ ::@:: The estimator is the random variable $T(X)$; the estimate is the number $T(x)$ obtained by substituting the data.
- notation for an estimator or an estimate of $\theta$ ::@:: $\hat \theta$.

## estimand, estimator, and estimate

The parameter $\theta$ is the fixed unknown quantity of interest; the estimator $T(X)$ is the random variable that guesses it; the estimate $T(x)$ is the number that guess takes on the data. Only the estimator has a sampling distribution, and only the estimate is known to the analyst.

---

Flashcards for this section are as follows:

- the three objects: $\theta$, $T(X)$ and $T(x)$ ::@:: The fixed unknown parameter, the random variable that guesses it, and the number that guess takes on the data.
- which one carries a sampling distribution: among $\theta$, $T(X)$ and $T(x)$ ::@:: Only the estimator $T(X)$, the only random one.
- which one is known to the analyst: among $\theta$, $T(X)$ and $T(x)$ ::@:: Only the estimate $T(x)$, computed from the data.

## point-valued estimation

A point estimator gives one numerical guess: $\bar x$ against the unknown $\mu$ in one dimension, the pair $(\bar x, s_{n-1})$ against $(\mu, \sigma)$ in two, a triple $(\hat \theta_1, \hat \theta_2, \hat \theta_3)$ against $(\theta_1, \theta_2, \theta_3)$ in three. It reports no statement of how far off the guess may be.

---

Flashcards for this section are as follows:

- what a point estimator reports: for the parameter $\theta$ ::@:: One numerical guess, with no statement of how far off it may be.
- one-dimensional point estimation: $\bar x$ against $\mu$ ::@:: A point against the unknown point on the real line.
- two-dimensional point estimation: $(\bar x, s_{n-1})$ against $(\mu, \sigma)$ ::@:: A point in the plane against the pair of unknown parameters.
- three-dimensional point estimation: $(\hat \theta_1, \hat \theta_2, \hat \theta_3)$ against $(\theta_1, \theta_2, \theta_3)$ ::@:: A point against the triple of unknown parameters.
- before the sample is drawn: for a point estimator ::@:: Its value cannot be predicted; only its distribution is known.

## sampling distribution

Every use of an estimator rests on the sampling distribution of $T(X)$. It can be obtained exactly, which is rare, difficult or even impossible apart from the normal model, or asymptotically when $n$ is sufficiently large, the leading example being the central limit theorem. Studying properties such as unbiasedness and convergence, building confidence intervals, and formulating tests all need one of the two.

---

Flashcards for this section are as follows:

- why the sampling distribution of $T(X)$ is needed ::@:: Studying the properties of $T$, constructing confidence intervals and formulating tests all rest on it.
- exactly determining a sampling distribution: when it is feasible ::@:: Rarely, or with difficulty, or not at all; the normal model is the exception.
- asymptotically determining a sampling distribution: for $n$ sufficiently large ::@:: The distribution is approximated, the central limit theorem being the leading example.
- tools for the two routes: large-sample and not-large-sample ::@:: Large-sample: the weak law of large numbers, the central limit theorem, convergence in probability, convergence in distribution, Slutsky's lemma, the delta method and the continuous mapping theorem. Not large-sample: bootstrapping, resampling the single collected data set.
