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

A _parametric distribution_ is one whose pdf or pmf is written down with its parameters left unknown, as in $N(\mu, 1)$ with $\mu \in \mathbb{R}$ unknown.

---

Flashcards for this section are as follows:

- parametric distribution: as in $N(\mu, 1)$ with $\mu \in \mathbb{R}$ unknown ::@:: A distribution whose pdf or pmf is given together with an unknown parameter or parameters.
- parameter: denoted $\theta$ ::@:: The unknown parameter(s) of the family, collected into one symbol which inference estimates or tests.
- what uncertainty amounts to: for the distribution and its parameter $\theta$ ::@:: Uncertainty of the distribution and uncertainty of $\theta$ are the same thing, so learning the distribution means learning $\theta$.
- what follows if $\theta$ is known: in the parametric setting ::@:: The distribution is completely specified.

## parametric distribution and model

Writing the form out settles what the law looks like and leaves only the entries of $\theta$ open, so collecting them into one symbol makes the distribution known up to $\theta$, and an unknown distribution is not a separate problem from an unknown $\theta$. A model built from such a family is a _parametric model_.

A model is non-parametric when no explicit form of the pdf or pmf is given, as in a model that says only that $X$ has some distribution function $F$. A known functional form with unknown parameters leaves a model partially specified rather than fully unspecified, and that is what makes it parametric.

---

Flashcards for this section are as follows:

- fully unspecified model ::@:: No explicit form of the pdf or pmf is given; that is a non-parametric model.
- partially specified model ::@:: The functional form of the pdf or pmf is known but depends on unknown parameters; that is a parametric model.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

The cases split three ways: models with a written form, a model with none, and a model written down with nothing left open.

A normal model in which both $\mu$ and $\sigma^2$ are unknown is parametric: the pdf is written down and only the pair $\theta = (\mu, \sigma^2)$ is left open. A binomial model with an unknown success probability is parametric for the same reason, with $\theta = p$ and $n$ fixed.

With $\sigma^2$ known and $\mu$ unknown the form is still given and one unknown remains, so the model is parametric over the smaller parameter set. A model is parametric because the form is written down, not because of how many parameters are left.

A model that says only that $X$ has some distribution function $F$ is non-parametric: no family is named and there is no parameter to estimate inside one.

A fully specified standard normal $N(0, 1)$ is parametric only trivially: the form is given and $\mu = 0$, $\sigma^2 = 1$ are fixed, so the family holds a single member and inference has nothing to work on.

---

Flashcards for this section are as follows:

- normal model with both $\mu$ and $\sigma^2$ unknown: parametric or not ::@:: Yes, the pdf is given and the unknown $\theta = (\mu, \sigma^2)$ is a finite-dimensional parameter.
- binomial model with success probability $p$ unknown and $n$ fixed: parametric or not ::@:: Yes, the pmf is given and the single unknown $p$ ranges over a known family.
- normal model with $\sigma^2$ known and $\mu$ unknown: parametric or not ::@:: Yes, the form is still given and one unknown parameter remains, and a smaller parameter set stays parametric.
- model given only by an arbitrary distribution function $F$: parametric or not ::@:: No, no form of the pdf or pmf is given, so there is no known family to estimate a parameter in.
- fully specified $N(0, 1)$: parametric or not ::@:: Yes, but trivially, the normal family is pinned at $\mu = 0$ and $\sigma^2 = 1$, so no unknown parameter is left to estimate.

## parametric families

A parametric family is a set of laws indexed by a parameter space, the functional form fixed and only $\theta$ varying: a candidate value of $\theta$ names a law, and the data say which members are compatible with them. The normal family is $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ with $\theta = (\mu, \sigma^2)$ unknown. The binomial family is $\{p_X : p_X = p_X(\cdot \mid \theta)\}$ with $\theta = p$ unknown.

The discrete families are Poisson, binomial, discrete uniform, multinomial, geometric, negative binomial and hypergeometric. The continuous families are normal, continuous uniform, exponential, beta, chi-square, Cauchy, $F$ and gamma, together with the $t$ distribution. Some sit inside others rather than standing apart: the geometric is a special case of the negative binomial, the exponential and chi-square are special cases of the gamma, and the Cauchy is a special case of the $t$.

---

Flashcards for this section are as follows:

- what stays fixed in a parametric family: $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ ::@:: The functional form of the pdf or pmf; only $\theta$ varies across the family.
- what a candidate value of $\theta$ can be checked against, once the form is fixed ::@:: A named law, because the family pins down the form and leaves only a parameter space to range over.
- normal family: $\{f_X : f_X = f_X(\cdot \mid \theta)\}$ ::@:: $\theta = (\mu, \sigma^2)$ is unknown.
- binomial family: $\{p_X : p_X = p_X(\cdot \mid \theta)\}$ ::@:: $\theta = p$ is unknown.
- discrete families in use ::@:: Poisson, binomial, discrete uniform, multinomial, geometric, negative binomial and hypergeometric.
- continuous families in use ::@:: Normal, continuous uniform, exponential, beta, chi-square, Cauchy, F, gamma and t.
- special cases among the families: the geometric, exponential, chi-square and Cauchy distributions ::@:: Inside the negative binomial, gamma and t families respectively.

## non-parametric models

Without a form there is no law to compute: the probability of the observed data cannot be worked out from the model, and no named distribution is available to take a quantile from. Inference runs on the parametric case instead, where the distributions are partially specified rather than fully unspecified.

---

Flashcards for this section are as follows:

- what a non-parametric model cannot supply: with no form of the pdf or pmf given ::@:: The probability of the observed data from the model, and a named distribution to take a quantile from.
- which case a model assumes: the parametric one or the non-parametric one ::@:: The parametric case, where the distributions are partially specified rather than fully unspecified.
