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

A linear function of a normal random variable is normal, and a normal random vector behaves the same way: every linear function of it is normal, with the mean and covariance transformed along with it. The sample mean of a normal sample is one such linear function.

---

Flashcards for this section are as follows:

- overview: for a $p \times 1$ vector $\mathbf X$ ::@:: The normal distribution extended from one variable to several variables, written $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- notation: for $\mathbf X = (X_1, \ldots, X_p)'$ ::@:: $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- mean vector $\boldsymbol \mu$: the first parameter of $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: The expected value of $\mathbf X$, a $p \times 1$ vector. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- variance-covariance matrix $\boldsymbol \Sigma$: the second parameter of $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: The $p \times p$ matrix of covariances $\operatorname{Cov}(X_i, X_j)$ of $\mathbf X$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- bivariate case: $p = 2$ ::@:: $N_2(\boldsymbol \mu, \boldsymbol \Sigma)$, the bivariate normal distribution. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the sample mean and the sample variance of a normal sample: which of them is a linear function of $\mathbf X$? ::@:: Only the sample mean. The sample variance squares the deviations before summing them, so it is a quadratic form in $\mathbf X$ and is not normal. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## probability density function

In one dimension $((x - \mu)/\sigma)^2$ is the scalar $(x - \mu)(\sigma^2)^{-1}(x - \mu)$, and the density falls off as that quantity grows. A vector needs the same thing, and the quadratic form $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$ supplies it: a scalar that grows as $\mathbf x$ moves away from $\boldsymbol \mu$, on which the density can depend exactly as the one-dimensional density depends on the squared distance.

The condition on $\boldsymbol \Sigma$ rests on two requirements. The exponent must stay non-negative, or the density would grow away from $\boldsymbol \mu$ instead of decaying, and the normalizing constant must be finite, which needs $\boldsymbol \Sigma$ invertible so that $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$ is defined. Both requirements come from one demand on the quadratic form: it must be positive for every non-zero vector $\mathbf z$, which is what symmetric and positive-definite means.

The density is $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$ for $-\infty < x_i < \infty$ and $i = 1, \ldots, p$. Support is the whole space, so there is no boundary to treat separately.

Which sample statistics are normal comes down to whether they are linear or quadratic in the components. The sample mean is linear, so the closure result settles it. The sample variance squares the deviations and is a quadratic form, so it takes no normality from the family: for a normal sample of size $n > 1$ the scaled sample variance follows $\chi^2(n - 1)$, as [sample variance](sample%20variance.md#distribution%20of%20the%20sample%20variance) sets out, which makes it a multiple of a chi-squared variable rather than a normal one. It never takes a negative value, which no nondegenerate normal variable does either.

---

Flashcards for this section are as follows:

- squared distance in one dimension: $((x - \mu)/\sigma)^2$ ::@:: $(x - \mu)(\sigma^2)^{-1}(x - \mu)$, a scalar. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- exponent of the multivariate normal density: the vector analogue of the one-dimensional squared distance $(x - \mu)(\sigma^2)^{-1}(x - \mu)$ ::@:: The quadratic form $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$, still a scalar. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- positive-definiteness of $\boldsymbol \Sigma$: for every non-zero vector $\mathbf z$ with real entries ::@:: $\mathbf z' \boldsymbol \Sigma \mathbf z > 0$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- normalizing constant of the multivariate normal density: multiplying $e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$ ::@:: $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$, where $\lvert \boldsymbol \Sigma \rvert$ is the determinant. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- multivariate normal density: $f(\mathbf x)$ for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- support of the multivariate normal density: each $x_i$ for $i = 1, \ldots, p$ ::@:: $-\infty < x_i < \infty$, the whole space. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why $\boldsymbol \Sigma$ must be positive-definite in the density $f(\mathbf x)$ ::@:: So the exponent stays non-negative as $\mathbf x$ moves away from $\boldsymbol \mu$, and so the normalizing constant $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$ is defined. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- distribution of the sample variance for a normal sample of size $n > 1$: normal, or something else? ::@:: Not normal. The sample variance is a quadratic form in the components, and its scaled form $\frac{(n-1) S_{n-1}^2}{\sigma^2}$ follows $\chi^2(n - 1)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the sample variance does not inherit normality from a normal sample while the sample mean does: what separates them? ::@:: The sample variance is a quadratic form in the components rather than a linear function of them, so the closure property for linear transformations does not reach it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## linear transformations

The family is closed under linear maps: if $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and $A$ is any $q \times p$ matrix, then $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$. The shape of $A$ does not matter to the conclusion: a single row gives one linear combination of the components, and a full $q \times p$ matrix gives $q$ of them jointly, still normal.

The sample mean is one such linear combination of the components, and $A = (\tfrac{1}{n}, \ldots, \tfrac{1}{n})$ gives its mean and its variance from the two formulas above. The argument reaches linear functions of the components and stops there. A statistic that squares them does not come under this result at all.

---

Flashcards for this section are as follows:

- linear transformation of a normal random vector: $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and a $q \times p$ matrix $A$ ::@:: $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- mean of $A \mathbf X$: for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $A \boldsymbol \mu$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- covariance matrix of $A \mathbf X$: for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $A \boldsymbol \Sigma A'$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a linear combination of the components of $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$: normal or not ::@:: Yes, the mean becomes $A \boldsymbol \mu$ and the covariance becomes $A \boldsymbol \Sigma A'$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## independence of the components

For two components of a jointly normal vector, $\operatorname{Cov}(X_i, X_j) = 0$ and independence of $X_i, X_j$ are the same condition. In general a zero covariance says nothing about dependence.

A zero cross-covariance block splits $\boldsymbol \Sigma$. The exponent becomes a sum and the normalizing constant a product, so the joint density factorizes into the marginal densities of the two blocks. A factorized density is the definition of independence, which means the off-diagonal entries of $\boldsymbol \Sigma$ decide the question by themselves. The argument does not extend outside the family, where a zero covariance and a dependence can sit together, as the uniform pair shows.

---

Flashcards for this section are as follows:

- independence of two components: $\binom{X_1}{X_2} \sim N_2\left(\binom{\mu_1}{\mu_2}, \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}\right)$ ::@:: $X_1$ and $X_2$ are independent if and only if $\sigma_{12} = \sigma_{21} = 0$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- two components of a jointly normal vector with zero covariance: independent? ::@:: Yes, and the equivalence runs only one way: outside this family a zero covariance can coexist with dependence. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- reason zero covariance implies independence here: for two components of a jointly normal vector with covariance $\boldsymbol \Sigma$ ::@:: The zero cross-covariance block splits $\boldsymbol \Sigma$ into two blocks, the quadratic form splits into a sum, and the joint density factorizes into the product of the marginal densities. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

### a scalar component beside a vector

Let $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$ with mean components $\mu_i = E(Y_i)$ for $i = 0, \ldots, p$. Write $\mathbf Y_p = (Y_1, \ldots, Y_p)'$ for the remaining components. Separating one component from a block of the others is the shape a sample mean takes against the rest of a sample.

Then $Y_0$ and $\mathbf Y_p$ are independent if and only if $$ \operatorname{Cov}(Y_0, \mathbf Y_p) = \begin{pmatrix} \operatorname{Cov}(Y_0, Y_1) \\ \operatorname{Cov}(Y_0, Y_2) \\ \vdots \\ \operatorname{Cov}(Y_0, Y_p) \end{pmatrix} = \mathbf 0. $$ One vector equation stands in for $p$ scalar ones: the $p$ off-diagonal entries of the first row of $\boldsymbol\Sigma$ are what have to vanish. The factorization is the same one, the zero block splitting $\boldsymbol\Sigma$ and the density becoming a product of marginals.

---

Flashcards for this section are as follows:

- mean components of $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)'$: for $i = 0, \ldots, p$ ::@:: $\mu_i = E(Y_i)$, so $\boldsymbol\mu = (\mu_0, \ldots, \mu_p)'$ is the mean of the whole vector $\mathbf Y$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- independence of a scalar and a vector component: $\mathbf Y = (Y_0, Y_1, \ldots, Y_p)' \sim N_{p+1}(\boldsymbol\mu, \boldsymbol\Sigma)$ ::@:: $Y_0$ and $\mathbf Y_p = (Y_1, \ldots, Y_p)'$ are independent if and only if $\operatorname{Cov}(Y_0, \mathbf Y_p) = \mathbf 0$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- vector of covariances $\operatorname{Cov}(Y_0, \mathbf Y_p)$: with $\mathbf Y_p = (Y_1, \ldots, Y_p)'$ ::@:: A $p \times 1$ vector, one entry per component of $\mathbf Y_p$, each an off-diagonal entry of the first row of $\boldsymbol\Sigma$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Take the bivariate normal pair with mean zero and identity covariance matrix $\boldsymbol\Sigma = I_2$. Every off-diagonal entry is zero, which makes $X_1$ and $X_2$ independent, and the unit variances make each of them standard normal. This generalizes: for a diagonal covariance matrix $\operatorname{diag}(\sigma_1^2, \ldots, \sigma_p^2)$ in $p$ dimensions, all $p(p - 1)/2$ off-diagonal covariances vanish, so the components are independent and each keeps its own $N(\mu_i, \sigma_i^2)$ marginal.

The bivariate standard normal pair with correlation $\tfrac{1}{2}$ is the near miss. Each marginal is $N(0, 1)$, and only $\sigma_{12} = \tfrac{1}{2} \ne 0$ breaks the condition. Outside the family the criterion fails. For $U \sim \text{Unif}(-1, 1)$ and $V = U^2$, the covariance $\operatorname{Cov}(U, V) = \operatorname{E}[U^3] - \operatorname{E}[U]\operatorname{E}[U^2] = 0 - 0 = 0$ vanishes: $U^3$ is odd over a symmetric interval. Yet $V$ is determined by $U$, so the two are dependent.

---

Flashcards for this section are as follows:

- a bivariate normal pair with mean zero and covariance matrix $I_2$: are the two components independent? ::@:: Yes, both off-diagonal entries are zero and each component is standard normal. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $\mathbf X \sim N_3(\boldsymbol\mu, \operatorname{diag}(\sigma_1^2, \sigma_2^2, \sigma_3^2))$: are the components independent? ::@:: Yes, all three off-diagonal covariances are zero, so each component keeps its own $N(\mu_i, \sigma_i^2)$ marginal. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a bivariate standard normal pair with correlation $\tfrac{1}{2}$: are the two components independent? ::@:: No, $\sigma_{12} = \tfrac{1}{2} \ne 0$, even though each marginal is $N(0, 1)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $U \sim \text{Unif}(-1, 1)$ and $V = U^2$ outside the normal family: are the two independent? ::@:: No, $\operatorname{Cov}(U, V) = 0$ because $\operatorname{E}[U^3] = \operatorname{E}[U] = 0$, while $V$ is determined by $U$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
