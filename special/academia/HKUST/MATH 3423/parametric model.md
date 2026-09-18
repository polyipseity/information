---
aliases:
  - parametric distribution
  - parametric family
  - parametric model
  - parametric models
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/parametric_model
  - language/in/English
---

# parametric model

A _parametric distribution_ is a probability distribution whose pdf or pmf is given along with an unknown parameter, as in $N(\mu, 1)$ with $\mu \in \mathbb{R}$ unknown. Collecting those unknowns into $\theta$, the distribution is known up to $\theta$, and a model built from such a family is a _parametric model_.

---

Flashcards for this section are as follows:

- parametric distribution: as in $N(\mu, 1)$ with $\mu \in \mathbb{R}$ unknown ::@:: A distribution whose pdf or pmf is given together with an unknown parameter or parameters.
- parameter: denoted $\theta$ ::@:: The unknown parameter(s) of the family, collected into one symbol which inference estimates or tests.
- what uncertainty amounts to: for the distribution and its parameter $\theta$ ::@:: Uncertainty of the distribution and uncertainty of $\theta$ are the same thing, so learning the distribution means learning $\theta$.
- what follows if $\theta$ is known: in the parametric setting ::@:: The distribution is completely specified.

## parametric families

A parametric family fixes the functional form of the pdf or pmf and lets only $\theta$ vary: the normal family is $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ with $\theta = (\mu, \sigma^2)$ unknown, and the binomial family is $\{p_X : p_X = p_X(\cdot \mid \theta)\}$ with $\theta = p$ unknown. The discrete families in this course are the Poisson, binomial, discrete uniform, multinomial, geometric, negative binomial and hypergeometric distributions; the continuous ones are the normal, continuous uniform, exponential, beta, chi-square, Cauchy, F, gamma and t distributions. Some are special cases of others: the geometric lies inside the negative binomial, the exponential and chi-square inside the gamma, and the Cauchy inside the t.

---

Flashcards for this section are as follows:

- what stays fixed in a parametric family: $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ ::@:: The functional form of the pdf or pmf; only $\theta$ varies across the family.
- normal family: $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ ::@:: $\theta = (\mu, \sigma^2)$ is unknown.
- binomial family: $\{p_X : p_X = p_X(\cdot \mid \theta)\}$ ::@:: $\theta = p$ is unknown.
- discrete families in this course: including the negative binomial ::@:: Poisson, binomial, discrete uniform, multinomial, geometric, negative binomial and hypergeometric.
- continuous families in this course: including the F and t ::@:: Normal, continuous uniform, exponential, beta, chi-square, Cauchy, F, gamma and t.
- special cases among the families: the geometric, exponential, chi-square and Cauchy distributions ::@:: Inside the negative binomial, gamma and t families respectively.

## non-parametric models

A model is fully unspecified when no explicit form of the pdf or pmf is given; that is a non-parametric model. It is partially specified when the functional form is known but depends on unknown parameters; that is a parametric model. This course assumes the parametric case.

---

Flashcards for this section are as follows:

- fully unspecified model ::@:: No explicit form of the pdf or pmf is given; that is a non-parametric model.
- partially specified model ::@:: The functional form of the pdf or pmf is known but depends on unknown parameters; that is a parametric model.
- which case this course assumes ::@:: The parametric case, where the distributions are partially specified rather than fully unspecified.
