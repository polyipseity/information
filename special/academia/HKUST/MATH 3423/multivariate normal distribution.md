---
aliases:
  - joint normal distribution
  - multivariate Gaussian distribution
  - multivariate normal
  - multivariate normal distribution
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/multivariate_normal_distribution
  - language/in/English
---

# multivariate normal distribution

The _multivariate normal distribution_ extends the normal distribution from one variable to several. The object is the $p \times 1$ vector $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$. The mean vector $\boldsymbol \mu$ gives the mean of each component, and the $p \times p$ matrix $\boldsymbol \Sigma$ carries the variance of $X_i$ on its $i$-th diagonal and the covariance $\operatorname{Cov}(X_i, X_j)$ off it. Setting $p = 2$ gives the bivariate case.

A linear function of a normal random variable is normal, and a normal random vector closes the same way: every linear function of it is normal.

---

Flashcards for this section are as follows:

- for $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$, the $p$-dimensional normal vector: what does the $p \times 1$ vector $\boldsymbol \mu$ hold? ::@:: The $i$-th entry is the mean of $X_i$.
- for $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$, the $p$-dimensional normal vector: what do the entries of the $p \times p$ matrix $\boldsymbol \Sigma$ hold? ::@:: The $i$-th diagonal entry is the variance of $X_i$, and the entries off the diagonal are the covariances $\operatorname{Cov}(X_i, X_j)$.

## probability density function

In one dimension $((x - \mu)/\sigma)^2$ is the scalar $(x - \mu)(\sigma^2)^{-1}(x - \mu)$, and the density falls off as that quantity grows. A vector needs the same thing, and the quadratic form $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$ supplies it: a scalar that grows as $\mathbf x$ moves away from $\boldsymbol \mu$, on which the density can depend exactly as the one-dimensional density depends on the squared distance.

The condition on $\boldsymbol \Sigma$ rests on two requirements. The exponent must stay non-negative, or the density would grow away from $\boldsymbol \mu$ instead of decaying, and the normalizing constant must be finite, which needs $\boldsymbol \Sigma$ invertible so that $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$ is defined. Both requirements come from one demand on the quadratic form: it must be positive for every non-zero vector $\mathbf z$, which is what symmetric and positive-definite means.

The density is $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$ for $-\infty < x_i < \infty$ and $i = 1, \ldots, p$. Support is the whole space, so there is no boundary to treat separately.

Which sample statistics are normal comes down to whether they are linear or quadratic in the components. The sample mean is linear, so the closure result settles it. The sample variance squares the deviations and is a quadratic form, so it takes no normality from the family, and [sample variance](sample%20variance.md#distribution%20of%20the%20sample%20variance) sets out the distribution it has instead. It never takes a negative value, which no nondegenerate normal variable does either.

---

Flashcards for this section are as follows:

- in one dimension, what scalar plays the part of the squared distance from the mean, written with the variance $\sigma^2$? ::@:: $(x - \mu)(\sigma^2)^{-1}(x - \mu)$, equal to $((x - \mu)/\sigma)^2$.
- density of $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ evaluated at the vector $\mathbf x$: what replaces the one-dimensional squared distance $(x - \mu)(\sigma^2)^{-1}(x - \mu)$ in its exponent? ::@:: The quadratic form $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$, a scalar.
- $\boldsymbol \Sigma$ symmetric and positive-definite in the density of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what inequality does every non-zero vector $\mathbf z$ with real entries satisfy? ::@:: $\mathbf z' \boldsymbol \Sigma \mathbf z > 0$.
- normalizing constant in the density of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what constant multiplies $e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$? ::@:: $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$, where $\lvert \boldsymbol \Sigma \rvert$ is the determinant of the $p \times p$ matrix $\boldsymbol \Sigma$.
- density of $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what is $f(\mathbf x)$? ::@:: $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$.
- support of the density of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what does each component $x_i$, $i = 1, \ldots, p$, range over? ::@:: $-\infty < x_i < \infty$, the whole space.
- why the $p \times p$ matrix $\boldsymbol \Sigma$ must be positive-definite in the density of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what does it stop the exponent from doing as the value $\mathbf x$ moves away from $\boldsymbol \mu$? ::@:: It keeps the exponent non-negative, so the density decays away from $\boldsymbol \mu$ instead of growing.
- why the $p \times p$ matrix $\boldsymbol \Sigma$ must be positive-definite in the density of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: what does it do for the normalizing constant? ::@:: It makes $\boldsymbol \Sigma$ invertible, so $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$ is defined and finite.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$: is the sample variance normal? ::@:: No. It squares the deviations, so it is a quadratic form in the components and not a linear function of them, and the closure result for linear transformations does not reach it.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$: what does the scaled sample variance $\frac{(n-1) S_{n-1}^2}{\sigma^2}$ follow, where $S_{n-1}^2$ is the sample variance dividing the sum of squared deviations by $n - 1$? ::@:: $\chi^2(n - 1)$.

## linear transformations

The family is closed under linear maps: if $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and $A$ is any $q \times p$ matrix, then $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$. The shape of $A$ does not matter to the conclusion: a single row gives one linear combination of the components, and a full $q \times p$ matrix gives $q$ of them jointly, still normal.

The sample mean is one such linear combination of the components, and $A = (\tfrac{1}{n}, \ldots, \tfrac{1}{n})$ gives its mean and its variance from the two formulas above.

---

Flashcards for this section are as follows:

- for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and any $q \times p$ matrix $A$, what is the distribution of $A \mathbf X$? ::@:: $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, written $\mathbf X = (X_1, \ldots, X_n)' \sim N_n(\mu \mathbf 1, \sigma^2 I_n)$: which $1 \times n$ matrix $A$ makes $A \mathbf X$ the sample mean $\bar X$? ::@:: $A = (\tfrac{1}{n}, \ldots, \tfrac{1}{n})$.

## independence of the components

For two components of a jointly normal vector, $\operatorname{Cov}(X_i, X_j) = 0$ and independence of $X_i, X_j$ are the same condition. In general a zero covariance says nothing about dependence.

A zero cross-covariance block splits $\boldsymbol \Sigma$. The exponent becomes a sum and the normalizing constant a product, so the joint density factorizes into the two marginal densities, which is the definition of independence. The off-diagonal entries of $\boldsymbol \Sigma$ therefore decide the question by themselves. The argument does not extend outside the family, where a zero covariance and a dependence can sit together, as the uniform pair shows.

---

Flashcards for this section are as follows:

- for a bivariate normal vector $\binom{X_1}{X_2} \sim N_2\left(\binom{\mu_1}{\mu_2}, \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}\right)$, where $\sigma_{12} = \operatorname{Cov}(X_1, X_2)$ and $\sigma_{21}$ is the matching entry below it: are $X_1$ and $X_2$ independent? ::@:: Yes, if and only if $\sigma_{12} = \sigma_{21} = 0$.
- two components of a jointly normal vector with covariance matrix $\boldsymbol \Sigma$: does zero covariance $\operatorname{Cov}(X_i, X_j) = 0$ give independence? ::@:: Yes, because the zero cross-covariance block splits $\boldsymbol \Sigma$ into two blocks, the quadratic form splits into a sum, and the joint density factorizes into the product of the two marginal densities.

### a scalar component beside a vector

Let $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$ with mean components $\mu_i = E(Y_i)$ for $i = 0, \ldots, p$. Write $\mathbf Y_p = (Y_1, \ldots, Y_p)'$ for the remaining components. Separating one component from a block of the others is the shape a sample mean takes against the rest of a sample.

Then $Y_0$ and $\mathbf Y_p$ are independent if and only if $$ \operatorname{Cov}(Y_0, \mathbf Y_p) = \begin{pmatrix} \operatorname{Cov}(Y_0, Y_1) \\ \operatorname{Cov}(Y_0, Y_2) \\ \vdots \\ \operatorname{Cov}(Y_0, Y_p) \end{pmatrix} = \mathbf 0. $$ One vector equation stands in for $p$ scalar ones: the $p$ off-diagonal entries of the first row of $\boldsymbol\Sigma$ are what have to vanish.

---

Flashcards for this section are as follows:

- for $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$: what is the mean component $\mu_i$ for $i = 0, \ldots, p$? ::@:: $\mu_i = E(Y_i)$, so $\boldsymbol\mu = (\mu_0, \ldots, \mu_p)'$ is the mean of the whole vector $\mathbf Y$.
- for $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$ and its remaining components $\mathbf Y_p = (Y_1, \ldots, Y_p)'$: when are $Y_0$ and $\mathbf Y_p$ independent? ::@:: If and only if the covariance vector $\operatorname{Cov}(Y_0, \mathbf Y_p) = \mathbf 0$.
- for $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$ with $\boldsymbol\Sigma$ its $(p + 1) \times (p + 1)$ covariance matrix: what shape and entries does $\operatorname{Cov}(Y_0, \mathbf Y_p)$ have, where $\mathbf Y_p = (Y_1, \ldots, Y_p)'$? ::@:: A $p \times 1$ vector with one entry per component of $\mathbf Y_p$, each the off-diagonal entry $\operatorname{Cov}(Y_0, Y_i)$ in the first row of $\boldsymbol\Sigma$.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Take the bivariate normal pair with mean zero and identity covariance matrix $\boldsymbol\Sigma = I_2$. Every off-diagonal entry is zero, which makes $X_1$ and $X_2$ independent, and the unit variances make each of them standard normal. This generalizes: for a diagonal covariance matrix $\operatorname{diag}(\sigma_1^2, \ldots, \sigma_p^2)$ in $p$ dimensions, all $p(p - 1)/2$ off-diagonal covariances vanish, so the components are independent and each keeps its own $N(\mu_i, \sigma_i^2)$ marginal.

The bivariate standard normal pair with correlation $\tfrac{1}{2}$ is the near miss. Each marginal is $N(0, 1)$, and only $\sigma_{12} = \tfrac{1}{2} \ne 0$ breaks the condition. Outside the family the criterion fails. For $U \sim \text{Unif}(-1, 1)$ and $V = U^2$, the covariance $\operatorname{Cov}(U, V) = \operatorname{E}[U^3] - \operatorname{E}[U]\operatorname{E}[U^2] = 0 - 0 = 0$ vanishes: $U^3$ is odd over a symmetric interval. Yet $V$ is determined by $U$, so the two are dependent.

---

Flashcards for this section are as follows:

- a bivariate normal pair with mean zero and covariance matrix $I_2$: are the two components independent? ::@:: Yes, both off-diagonal entries are zero and each component is standard normal.
- $\mathbf X \sim N_3(\boldsymbol\mu, \operatorname{diag}(\sigma_1^2, \sigma_2^2, \sigma_3^2))$: are the components independent? ::@:: Yes, all three off-diagonal covariances are zero, so each component keeps its own $N(\mu_i, \sigma_i^2)$ marginal.
- a bivariate standard normal pair with correlation $\tfrac{1}{2}$: are the two components independent? ::@:: No, $\sigma_{12} = \tfrac{1}{2} \ne 0$, even though each marginal is $N(0, 1)$.
- $U \sim \text{Unif}(-1, 1)$ and $V = U^2$ outside the normal family: are the two independent? ::@:: No, $\operatorname{Cov}(U, V) = 0$ because $\operatorname{E}[U^3] = \operatorname{E}[U] = 0$, while $V$ is determined by $U$.
