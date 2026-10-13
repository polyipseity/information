---
aliases:
  - HKUST MATH 3423 week 2 tutorial 1 content
  - HKUST MATH 3423 week 2 tutorial 1 tutorial
  - HKUST MATH3423 week 2 tutorial 1 tutorial
  - MATH 3423 week 2 tutorial 1 content
  - MATH 3423 week 2 tutorial 1 tutorial
  - MATH3423 week 2 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/tutorials/week_2_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST MATH 3423 week 2 tutorial 1
- parent: [week 2 tutorial 1](index.md)

---

## statistical inference and parametric models

Statistical inference uses data to draw conclusions about an unknown feature of a population or a random variable.

A random variable $X$ is described by a probability distribution. A parametric model fixes the functional form of the probability mass function (pmf) or the probability density function (pdf) and leaves one or more parameters unknown. Such a model is written as the family $$\{f_X(\cdot \mid \boldsymbol{\theta}) : \boldsymbol{\theta} \in \boldsymbol{\Theta}\}$$ for a continuous $X$, or $$\{p_X(\cdot \mid \boldsymbol{\theta}) : \boldsymbol{\theta} \in \boldsymbol{\Theta}\}$$ for a discrete one.

Take $X \sim N(\mu, 1)$ with $\mu$ unknown. The model is the family of normal distributions with variance $1$. The target parameter is $\mu$.

The observed values $x_1, \ldots, x_n$ are the data, known numbers that arrive only after sampling. The corresponding $X_1, \ldots, X_n$ are the random variables before sampling.

> Suppose we are interested in a random variable called "Reaction time". Let $X$ denote the reaction time, and assume that $X \sim N(\mu, 1)$, where $\mu$ is unknown. Four observed reaction times are $x_1 = 1.3$, $x_2 = 0.8$, $x_3 = 1.5$, $x_4 = 1.0$.
>
> (a) Identify the target random variable, the parametric model, the unknown parameter, and the data.
>
> (b) Explain the difference between $X_i$ and $x_i$.
>
> - solution: (a) The target random variable is {@{the reaction time $X$}@}. The parametric model is {@{$\{N(\mu, 1) : \mu \in \mathbb{R}\}$, the family of normal distributions with variance 1}@}, and the unknown parameter is {@{$\mu$}@}. (b) Before the experiment {@{$X_i$ is a random variable whose value is uncertain}@}, and afterwards {@{$x_i$ is its realization, a known number}@}.

A random variable has no settled value until the experiment that produces it runs. The copy $X_i$ before the experiment and the observation $x_i$ after it are two faces of one sample.

---

Flashcards for this section are as follows:

- what statistical inference does with a sample ::@:: It draws conclusions about an unknown feature of a population or of a random variable.
- the parametric model of a random variable $X$ whose pmf or pdf has a known functional form ::@:: The family of every distribution of that form, $$\{f_X(\cdot \mid \boldsymbol{\theta}) : \boldsymbol{\theta} \in \boldsymbol{\Theta}\}$$ in the continuous case and $$\{p_X(\cdot \mid \boldsymbol{\theta}) : \boldsymbol{\theta} \in \boldsymbol{\Theta}\}$$ in the discrete one.
- the target parameter of the model $X \sim N(\mu, 1)$ with $\mu$ unknown ::@:: $\mu$. The model is the family of normal distributions with variance 1 over every $\mu$, so the mean is the one unknown the data will fix.
- the data $x_1, \ldots, x_n$ of a sample against the random variables $X_1, \ldots, X_n$ they come from ::@:: The observations $x_1, \ldots, x_n$ are known numbers available only after sampling, while the copies $X_1, \ldots, X_n$ are random variables fixed by the model beforehand.

## random samples

Unless otherwise stated, $X_1, \ldots, X_n$ are assumed to be independent and identically distributed (i.i.d.) copies of $X$. A collection of i.i.d. copies is a random sample.

The i.i.d. assumption has two parts.

1. __Identically distributed:__ every $X_i$ has the same distribution as $X$. In the continuous case this reads $$f_{X_i}(x \mid \boldsymbol{\theta}) = f_X(x \mid \boldsymbol{\theta}), \qquad i = 1, \ldots, n.$$
2. __Independent:__ the joint distribution factors into the product of the marginal distributions. For continuous random variables, $$f_{X_1, \ldots, X_n}(x_1, \ldots, x_n \mid \boldsymbol{\theta}) = \prod_{i=1}^{n} f_{X_i}(x_i \mid \boldsymbol{\theta}) = \prod_{i=1}^{n} f_X(x_i \mid \boldsymbol{\theta}).$$ For discrete random variables the statement is simply $$p_{X_1, \ldots, X_n}(x_1, \ldots, x_n \mid \boldsymbol{\theta}) = \prod_{i=1}^{n} p_X(x_i \mid \boldsymbol{\theta}).$$

> Let $X_1, \ldots, X_4$ be a random sample from a Bernoulli distribution with unknown success probability $p$, so $p_X(x \mid p) = p^x (1 - p)^{1 - x}$ for $x \in \{0, 1\}$.
>
> (a) Find the joint pmf of $(X_1, X_2, X_3, X_4)$.
>
> (b) Write the probability of observing $(x_1, x_2, x_3, x_4) = (1, 0, 1, 1)$.
>
> - solution: (a) Independence makes {@{the joint pmf a product}@}, {@{$p_{X_1, \ldots, X_4}(x_1, \ldots, x_4 \mid p) = \prod_{i=1}^{4} p^{x_i} (1 - p)^{1 - x_i} = p^{\sum_{i=1}^{4} x_i} (1 - p)^{4 - \sum_{i=1}^{4} x_i}$}@}, for $(x_1, \ldots, x_4) \in \{0, 1\}^4$. (b) The sample $(1, 0, 1, 1)$ carries {@{three successes}@}, so {@{$\Pr(X_1 = 1, X_2 = 0, X_3 = 1, X_4 = 1) = p^3 (1 - p)$}@}.

A Bernoulli variable is a binomial with one trial, so $X \sim \operatorname{Bin}(1, p)$. Its pmf carries the binomial coefficient $\binom{1}{x}$. Holding the observed values fixed, that pmf becomes a function of the unknown $p$ alone, which is the likelihood of $p$ for the data.

> For each pair, decide whether the two variables are independent, identically distributed, both, or neither, and hence whether the pair is a random sample from one common distribution.
>
> (a) $Z \sim N(0, 1)$ with $X_1 = Z$ and $X_2 = -Z$.
>
> (b) $X_1 \sim \operatorname{Bernoulli}(0.3)$ and $X_2 \sim \operatorname{Bernoulli}(0.7)$ are independent.
>
> (c) $X_1$ and $X_2$ are independent and both follow $\operatorname{Bernoulli}(p)$.
>
> - solution: (a) {@{Identically distributed but not independent}@}, because {@{$X_2$ is completely determined by $X_1$}@}. (b) {@{Independent but not identically distributed}@}, because {@{the success probabilities differ}@}. (c) {@{Both conditions hold}@}, so the pair is {@{a random sample from $\operatorname{Bernoulli}(p)$}@}.

Identical distribution says one observation leaves the distribution of the others unchanged. Independence lets the joint pmf be written out one factor at a time: for four independent Bernoulli copies $$p_{X_1, \ldots, X_4}(x_1, \ldots, x_4 \mid p) = p_{X_1}(x_1 \mid p) \cdot p_{X_2}(x_2 \mid p) \cdot p_{X_3}(x_3 \mid p) \cdot p_{X_4}(x_4 \mid p).$$ Writing the joint as a product is independence. Replacing every factor by the same $p_X$ is identical distribution.

---

Flashcards for this section are as follows:

- a random sample of $X_1, \ldots, X_n$ taken from $X$ ::@:: $n$ copies of $X$ assumed independent and identically distributed unless stated otherwise.
- the joint pmf of a Bernoulli sample from $\operatorname{Bernoulli}(p)$ once the observations are held fixed ::@:: $$p^{\sum_{i=1}^{n} x_i}(1-p)^{n - \sum_{i=1}^{n} x_i}$$, a function of $p$ alone and therefore the likelihood of $p$ for the observed data.
- a single Bernoulli trial $X \sim \operatorname{Bernoulli}(p)$ read as a binomial variable ::@:: $X \sim \operatorname{Bernoulli}(p)$ is $\operatorname{Bin}(1, p)$, so its pmf carries the binomial coefficient $\binom{1}{x}$ and the number of trials is $1$, not $0$.
- which half of i.i.d. lets the joint pmf be written one factor at a time, and which lets every factor be the same $p_X$ ::@:: Independence gives the product of the marginals; identical distribution replaces each marginal with the single $p_X$.
- the pair $(Z, -Z)$ with $Z \sim N(0, 1)$ read as a possible random sample ::@:: Identically distributed but not independent, since one copy fixes the other, so the pair is not a random sample from one common distribution.

## statistics, estimators, and estimates

Let $\boldsymbol{X} = (X_1, \ldots, X_n)^{\top}$. A statistic is a function $T(\boldsymbol{X})$ that does not contain any unknown parameter. Before sampling, a statistic is a random variable. It has its own probability distribution, called its sampling distribution.

When a statistic is used to estimate a parameter $\boldsymbol{\theta}$, it is a point estimator. Once the data $\boldsymbol{x} = (x_1, \ldots, x_n)^{\top}$ are observed, the number $T(\boldsymbol{x})$ is an estimate.

Two important statistics are $$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i, \qquad S_{n-1}^{2} = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})^2.$$ A second form of the sample variance divides the same sum by $n$ instead, $$S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar{X})^2.$$ The two differ by a single factor, $$(n - 1) S_{n-1}^{2} = n S_n^2.$$

> Let $X_1, \ldots, X_4$ be i.i.d. from $N(\mu, \sigma^2)$ with both $\mu$ and $\sigma^2$ unknown, and consider $T_1 = \bar X$, $T_2 = \frac{1}{4} \sum_{i=1}^{4} (X_i - \mu)^2$, and $T_3 = \max_i X_i - \min_i X_i$.
>
> (a) Which of $T_1, T_2, T_3$ are statistics?
>
> (b) Which one is the usual point estimator of $\mu$?
>
> (c) For the data $(2, 4, 6, 8)$, calculate $\bar x$, $s_3^2$, and $s_4^2$.
>
> - solution: (a) $T_1$ and $T_3$ are {@{statistics, being functions of the sample alone}@}, while $T_2$ is {@{not a statistic when $\mu$ is unknown, since its definition contains $\mu$}@}. (b) The usual point estimator of $\mu$ is {@{$\bar X$, random before the sample is observed}@}. (c) {@{$\bar x = \frac{2 + 4 + 6 + 8}{4} = 5$}@}. The squared deviations from $5$ sum to {@{$9 + 1 + 1 + 9 = 20$}@}, and dividing that sum by $3$ and by $4$ gives {@{$s_3^2 = \frac{20}{3}$}@} and {@{$s_4^2 = \frac{20}{4} = 5$}@}, both estimates read off from the observed data.

The parameter $\boldsymbol{\theta}$ a statistic estimates is the estimand. A candidate such as $T_0 = 0$ is a constant rather than a function of the sample, so it carries no information from the data.

---

Flashcards for this section are as follows:

- a statistic of a sample $X_1, \ldots, X_n$ ::@:: A function $T(X_1, \ldots, X_n)$ whose definition contains no unknown parameter. Before sampling it is a random variable with a sampling distribution of its own.
- a point estimator of $\boldsymbol{\theta}$, and the estimate it produces from $\boldsymbol{x}$ ::@:: A statistic chosen for a parameter $\boldsymbol{\theta}$; once the data $\boldsymbol{x} = (x_1, \ldots, x_n)^{\top}$ arrive, the number it takes is the estimate.
- the two sample variances of a sample of size $n$, and how they differ ::@:: $$S_{n-1}^{2} = \frac{1}{n-1} \sum_{i=1}^{n}(X_i - \bar X)^2$$ and $$S_{n}^{2} = \frac{1}{n} \sum_{i=1}^{n}(X_i - \bar X)^2$$, sharing the numerator and differing in the denominator, with $(n - 1) S_{n-1}^{2} = n S_n^{2}$.
- the candidate $T_0 = 0$ as an estimator of $\boldsymbol{\theta}$ ::@:: Not one. It is a constant rather than a function of the sample, so it carries no information from the data and nothing about $\boldsymbol{\theta}$.

## the sampling distribution of the sample mean

The sample mean $\bar{X}$ is a random variable before sampling. Its distribution depends on the common distribution of $X_1, \ldots, X_n$.

Linearity of expectation and independence give the mean and the variance of $\bar{X}$ for any random sample whose population mean and variance are both finite. The expectation needs identical distribution only: $$\operatorname{E}[\bar{X}] = \operatorname{E}\left[\frac{X_1 + \cdots + X_n}{n}\right] = \frac{1}{n} \left\{ \operatorname{E}(X_1) + \cdots + \operatorname{E}(X_n) \right\} = \frac{1}{n} \left\{ n \operatorname{E}(X_1) \right\} = \operatorname{E}[X_1].$$ The variance needs independence as well. Without it the variances of the copies would not simply add: $$\operatorname{Var}(\bar{X}) = \operatorname{Var}\left\{\frac{X_1 + \cdots + X_n}{n}\right\} = \frac{1}{n^2} \left\{ \operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n) \right\} = \frac{1}{n^2} \left\{ n \operatorname{Var}(X_1) \right\} = \frac{\operatorname{Var}(X_1)}{n}.$$ Averaging makes the variance smaller than any single observation carries.

> Let $X_1, \ldots, X_{10}$ be i.i.d. from $\operatorname{Bin}(5, 0.2)$ and let $\bar X = 10^{-1} \sum_{i=1}^{10} X_i$.
>
> (a) Find the distribution of $Y = \sum_{i=1}^{10} X_i$ and describe the distribution of $\bar X$.
>
> (b) Find $\operatorname{E}[\bar X]$ and $\operatorname{Var}(\bar X)$.
>
> - solution: (a) {@{Independent binomial variables with a common success probability}@} add to {@{a binomial}@}, so {@{$Y \sim \operatorname{Bin}(50, 0.2)$}@} and {@{$\bar X = \frac{Y}{10}$}@}, taking the values {@{$0, 0.1, \ldots, 5$}@}. (b) {@{$\operatorname{E}[X_i] = 5(0.2) = 1$}@} and {@{$\operatorname{Var}(X_i) = 5(0.2)(0.8) = 0.8$}@}, so {@{$\operatorname{E}[\bar X] = 1$}@} and {@{$\operatorname{Var}(\bar X) = \frac{0.8}{10} = 0.08$}@}.

<!-- markdownlint MD028 -->

> Let $X_1, X_2, X_3, X_4$ be i.i.d. with $\operatorname{E}[X_i] = \mu$ and $\operatorname{Var}(X_i) = \sigma^2$, and consider $T_1 = X_1$, $T_2 = \frac{X_1 + X_2 + X_3 + X_4}{4}$, and $T_3 = \frac{X_1 + 2X_2 + X_3}{4}$.
>
> (a) Find $\operatorname{E}[T_1]$, $\operatorname{E}[T_2]$, and $\operatorname{E}[T_3]$.
>
> (b) Find $\operatorname{Var}(T_1)$, $\operatorname{Var}(T_2)$, and $\operatorname{Var}(T_3)$.
>
> (c) Which estimator has the smallest variance, and what does that say about averaging independent observations?
>
> - solution: (a) {@{Linearity of expectation}@} gives {@{$\operatorname{E}[T_1] = \mu$}@}, {@{$\operatorname{E}[T_2] = \frac{4\mu}{4} = \mu$}@}, and {@{$\operatorname{E}[T_3] = \frac{\mu + 2\mu + \mu}{4} = \mu$}@}, so all three can be {@{used to estimate $\mu$}@}. (b) {@{Independence}@} gives {@{$\operatorname{Var}(T_1) = \sigma^2$}@}, {@{$\operatorname{Var}(T_2) = \frac{1}{16} \sum_{i=1}^{4} \operatorname{Var}(X_i) = \frac{\sigma^2}{4}$}@}, and {@{$\operatorname{Var}(T_3) = \frac{1}{16} \{\operatorname{Var}(X_1) + 4 \operatorname{Var}(X_2) + \operatorname{Var}(X_3)\} = \frac{3\sigma^2}{8}$}@}. (c) {@{$T_2 = \bar X$}@} has the smallest variance, since {@{an equal-weight average of every independent observation is steadier than one observation alone or an unequal weighting of them}@}.

<!-- markdownlint MD028 -->

> Seen as information rather than as arithmetic, why does an equal-weight average of every observation carry less variance than one observation alone, or an unequal weighting of them?
>
> - solution: All three of the estimators above have {@{mean $\mu$}@}, so they {@{differ in variance alone}@}. {@{Independence}@} leaves {@{no cross terms in the variance of a weighted average}@}, so each copy enters {@{with the square of its weight}@}. {@{$T_2 = \bar X$}@} is {@{the only one of the three whose weights are equal}@}.

---

Flashcards for this section are as follows:

- the sample mean $\bar X$ before the sample is observed ::@:: A random variable whose distribution is fixed by the common distribution of $X_1, \ldots, X_n$.
- the expectation of the sample mean of a random sample of size $n$ with finite population mean ::@:: $$\operatorname{E}[\bar X] = \operatorname{E}[X_1]$$ Linearity of expectation needs identical distribution and nothing more.
- the variance of the sample mean of a random sample of size $n$ with finite population variance ::@:: $$\operatorname{Var}(\bar X) = \frac{\operatorname{Var}(X_1)}{n}.$$ The variances of the copies add only because the copies are independent, and each enters with the square of its weight, here $\frac{1}{n}$.

## each definition in one line

The $i$-th observation is the random variable $X_i$ before the experiment and the number $x_i$ after it.

The two halves of i.i.d. are separate claims. Either can hold without the other. Identical distribution says one observation leaves the distribution of the others where it was. Independence says no observation carries information about another.

A statistic is a function of the sample that involves no unknown parameter. The same function, used to estimate a parameter, is an estimator. With the data substituted for the sample, it is an estimate.

Linearity of expectation and independence together fix the mean and the variance of the sample mean, for a random sample of size $n$ whose population mean and variance are both finite: $$\operatorname{E}[\bar X] = \operatorname{E}[X_1]$$ and $$\operatorname{Var}(\bar X) = \frac{\operatorname{Var}(X_1)}{n}.$$

With the observed values held fixed, the joint pmf of a Bernoulli sample is the likelihood of the unknown success probability $p$.

---

Flashcards for this section are as follows:

- the copy $X_i$ of a random variable $X$ and the observation $x_i$, before and after the experiment that produces them ::@:: $X_i$ is the random variable, with no settled value before the experiment; $x_i$ is its realized value, known afterwards.
- a collection $X_1, \ldots, X_n$ of copies of a random variable $X$ that is a random sample ::@:: The copies are independent of one another and share the distribution of $X$, which is assumed unless stated otherwise.
- the two halves of i.i.d. for copies $X_1, \ldots, X_n$ of a random variable $X$, and what each contributes ::@:: Identical distribution gives every copy the same distribution as $X$, so one parameter describes all of them; independence makes the joint distribution a product of the marginals.
- the joint pmf of a Bernoulli sample read as a function of the unknown success probability $p$ ::@:: The joint pmf is the likelihood of $p$ for the observed data.
- the two sample variances of a sample of size $n$ ::@:: $S_{n-1}^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar X)^2$ and $S_n^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar X)^2$, sharing the numerator and differing in the denominator, with $(n-1) S_{n-1}^2 = n S_n^2$.

## the multivariate normal

A normal vector is a random vector whose every linear combination is normal. The construction below follows Larry Wasserman's _All of Statistics_; [multivariate normal distribution](../../multivariate%20normal%20distribution.md) covers the same ground.

The distribution starts from one component. For $X_1 \sim N(\mu, \sigma^2)$ the density is $$f(x_1) = \frac{1}{\sqrt{2\pi} \sigma} \cdot e^{-\frac{(x - \mu)^2}{2 \sigma^2} }.$$

Take $d$ components with zero mean and spherical covariance, so $\boldsymbol{X} = (X_1, \ldots, X_d)^{\top} \sim N(0, \sigma^2 I_d)$. The components are independent, so the joint density is the product of the marginals: $$p(\boldsymbol{X}) = \prod_{i=1}^{d} p(X_i) = \frac{1}{(\sqrt{2\pi} \sigma)^{d} } \cdot e^{-\frac{\sum_{i=1}^{d} x_i^2}{2 \sigma^2} } = \frac{1}{(\sqrt{2\pi} \sigma)^{d} } \cdot e^{-\frac{\lVert \boldsymbol{x} \rVert^2}{2 \sigma^2} }.$$

An affine map of a normal vector stays normal: $Y = A\boldsymbol{X} + H \sim N(H, \sigma^2 \cdot AA^{\top})$, with mean vector $H$ and covariance $\sigma^2 \cdot AA^{\top}$.

To take the mean of two components of $Y$, multiply the whole vector by the row of ones and zeros that picks them out. The mean of $Y$ is $H$, so $$\operatorname{E}[Y_1 + Y_2] = \operatorname{E}\left[(1 \;\; 1 \;\; 0 \;\; 0 \cdots 0) Y\right] = \operatorname{E}\left[(1 \;\; 1 \;\; 0 \cdots 0) (A\boldsymbol{X} + H)\right] = (1 \;\; 1 \;\; 0 \cdots 0) H = H_1 + H_2.$$

The covariance matrix $\Sigma = \operatorname{Cov}(Y)$ carries a variance on the diagonal and a covariance in each off-diagonal slot: $$\Sigma = \begin{pmatrix} \operatorname{Var}(Y_1) & \operatorname{Cov}(Y_1, Y_2) & \cdots & \operatorname{Cov}(Y_1, Y_d) \\ \operatorname{Cov}(Y_2, Y_1) & \operatorname{Var}(Y_2) & \cdots & \operatorname{Cov}(Y_2, Y_d) \\ \vdots & \vdots & \ddots & \vdots \end{pmatrix}.$$

Inverting $\Sigma$ turns the distance from the mean into the quadratic form $$(Y - H)^{\top} \Sigma^{-1} (Y - H),$$ which is a row of centered components times the inverse covariance times a column of the same centered components: $$(Y - H)^{\top} \Sigma^{-1} (Y - H) = (Y_1 - H_1, Y_2 - H_2, \ldots, Y_d - H_d) \begin{pmatrix} (\Sigma^{-1})_{11} & (\Sigma^{-1})_{12} & \cdots \\ \vdots & \ddots & \\ (\Sigma^{-1})_{d1} & & (\Sigma^{-1})_{dd} \end{pmatrix} \begin{pmatrix} Y_1 - H_1 \\ \vdots \\ Y_d - H_d \end{pmatrix}.$$

---

Flashcards for this section are as follows:

- the density of one component $X_1 \sim N(\mu, \sigma^2)$ of a normal vector ::@:: $$f(x_1) = \frac{1}{\sqrt{2\pi} \sigma} \cdot e^{-\frac{(x - \mu)^2}{2 \sigma^2} }$$
- the standard multivariate normal with zero mean and spherical covariance $\sigma^2 \cdot I_d$, and its density over $d$ components ::@:: $$\boldsymbol{X} = (X_1, \ldots, X_d)^{\top} \sim N(0, \sigma^2 I_d)$$ with density $$p(\boldsymbol{X}) = \prod_{i=1}^{d} p(X_i) = \frac{1}{(\sqrt{2\pi} \sigma)^{d} } \cdot e^{-\frac{\sum_{i=1}^{d} x_i^2}{2 \sigma^2} } = \frac{1}{(\sqrt{2\pi} \sigma)^{d} } \cdot e^{-\frac{\lVert \boldsymbol{x} \rVert^2}{2 \sigma^2} }.$$
- the law of an affine map $Y = A\boldsymbol{X} + H$ of a normal vector $\boldsymbol{X}$, with $H$ a vector and $A$ a matrix ::@:: $Y = A\boldsymbol{X} + H \sim N(H, \sigma^2 \cdot AA^{\top})$, with mean vector $H$ and covariance $\sigma^2 \cdot AA^{\top}$.
- the quadratic form that measures how far a draw sits from the mean vector $H$, in the units the covariance matrix $\Sigma$ sets ::@:: $$(Y - H)^{\top} \Sigma^{-1} (Y - H),$$ a row of centered components times the inverse covariance times a column of the same centered components.
