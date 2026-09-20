---
aliases:
  - inferential statistics
  - statistical inference
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/statistical_inference
  - language/in/English
---

# statistical inference

_Statistical inference_ reaches a conclusion about an unknown quantity from known evidence. The evidence is the data; the unknown quantity is a random variable $X$, described by a probability distribution because its value is unpredictable before the corresponding experiment. This course treats parametric models, in which the distribution of $X$ is known up to an unknown parameter $\theta$.

---

Flashcards for this section are as follows:

- definition ::@:: Reaching a conclusion about something from known evidence; "statistical" refers to the data and "inference" to the conclusion.
- why a probability distribution is used: for the unknown quantity $X$ ::@:: Before the corresponding experiment is performed, $X$ is unpredictable; coin flipping is the usual illustration.
- mission: with data and a parametric model for $X$ ::@:: Estimate the parameter(s) $\theta$ of the distribution of the target random variable.

## data

Data are the actual values of the target random variable $X$, whose distribution is not fully specified. Writing $x_1, \ldots, x_n$ for the $n$ observations, also called realizations, each $x_i$ is a known number once the sample is drawn, while the copies $X_1, \ldots, X_n$ that produced it are random. Data carry information about the unknown parameter.

---

Flashcards for this section are as follows:

- definition: given observations $x_1, \ldots, x_n$ of the target random variable $X$ ::@:: Actual values of $X$, each a known number after sampling.
- notation: $x_i$ versus $X_i$ ::@:: $X_i$ is the $i$-th copy of $X$ and $x_i$ its actual value; uppercase letters denote random variables and lowercase letters their realizations.
- when the values become known: for $x_1, \ldots, x_n$ ::@:: After sampling; before it, only the joint distribution of the copies is known.
- why data estimate the parameter: under a parametric model for $X$ ::@:: They carry information about the true value of the unknown parameter(s).

## modes of inference

Point estimation gives a single value for $\theta$: the sample mean or sample variance for an unknown population mean or variance, otherwise the method of moments or maximum likelihood. Interval estimation gives an interval, a confidence interval, instead of a point. Hypothesis testing tests hypotheses about the value of $\theta$. Interval estimation and hypothesis testing both need the exact or approximate distribution of the estimator.

---

Flashcards for this section are as follows:

- modes of inference: from a parametric model ::@:: Point estimation, interval estimation, and hypothesis testing.
- point estimation: as a guess for $\theta$ ::@:: A single value; the sample mean or sample variance for an unknown population mean or variance.
- general point-estimation methods: when $\theta$ is neither the population mean nor the population variance ::@:: The method of moments and maximum likelihood estimation.
- interval estimation: as a guess for $\theta$ ::@:: An interval-valued guess, a confidence interval, rather than a point.
- hypothesis testing ::@:: A statistical test of hypotheses about the value of the parameter.
- prerequisite of interval estimation and hypothesis testing ::@:: The exact or approximate distribution of the estimator.
