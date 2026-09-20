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

The _multivariate normal distribution_ extends the normal distribution from one variable to a $p \times 1$ vector of observations on several variables, written $\mathbf X = (X_1, \ldots, X_p)' \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$. The mean vector $\boldsymbol \mu$ and the variance-covariance matrix $\boldsymbol \Sigma$ take the places of the single mean $\mu$ and variance $\sigma^2$. Linear functions of a normal random vector are again normal, and the distributions of the sample mean and the sample variance of a normal sample follow from that fact.

---

Flashcards for this section are as follows:

- overview: for a $p \times 1$ vector $\mathbf X$ of observations on several variables ::@:: The normal distribution extended from one variable to the vector, written $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$.
- notation: for $\mathbf X = (X_1, \ldots, X_p)'$ ::@:: $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$.
- mean vector $\boldsymbol \mu$: the first parameter of $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$, a $p \times 1$ vector ::@:: The expected value of the random vector $\mathbf X$.
- variance-covariance matrix $\boldsymbol \Sigma$: the second parameter of $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$, a $p \times p$ matrix ::@:: The matrix of covariances $\operatorname{Cov}(X_i, X_j)$ of the random vector $\mathbf X$.
- bivariate case: $p = 2$ in $N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $N_2(\boldsymbol \mu, \boldsymbol \Sigma)$, the bivariate normal distribution.

## probability density function

The exponent generalizes the one-dimensional squared distance. In one dimension $((x - \mu)/\sigma)^2$ is the scalar $(x - \mu)(\sigma^2)^{-1}(x - \mu)$; on a vector the corresponding scalar is the quadratic form $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$, with $\boldsymbol \Sigma^{-1}$ in place of $(\sigma^2)^{-1}$. The symmetric matrix $\boldsymbol \Sigma$ is assumed positive-definite, that is $\mathbf z' \boldsymbol \Sigma \mathbf z > 0$ for every non-zero vector $\mathbf z$ with real entries. Positive-definiteness makes the quadratic form positive and the normalizing constant $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$ well defined, and the density is $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$ for $-\infty < x_i < \infty$ and $i = 1, \ldots, p$.

---

Flashcards for this section are as follows:

- squared distance in one dimension: $((x - \mu)/\sigma)^2$ ::@:: $(x - \mu)(\sigma^2)^{-1}(x - \mu)$, a scalar.
- exponent of the multivariate normal density: $(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)$ ::@:: The multivariate analogue of the standardized squared distance, still a scalar.
- positive-definiteness of $\boldsymbol \Sigma$: for every non-zero vector $\mathbf z$ with real entries ::@:: $\mathbf z' \boldsymbol \Sigma \mathbf z > 0$.
- normalizing constant of the multivariate normal density: multiplying $e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$ ::@:: $(2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2}$, where $\lvert \boldsymbol \Sigma \rvert$ is the determinant.
- multivariate normal density: $f(\mathbf x)$ for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $f(\mathbf x) = (2\pi)^{-p/2} \lvert \boldsymbol \Sigma \rvert^{-1/2} e^{-(\mathbf x - \boldsymbol \mu)' \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)/2}$.
- support of the multivariate normal density: each $x_i$ for $i = 1, \ldots, p$ ::@:: $-\infty < x_i < \infty$, the whole space.

## linear transformations

The family is closed under linear maps. If $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and $A$ is any $q \times p$ matrix, then $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$. The mean vector is mapped to $A \boldsymbol \mu$, and the covariance matrix is sandwiched into $A \boldsymbol \Sigma A'$.

---

Flashcards for this section are as follows:

- linear transformation of a normal random vector: $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ and a $q \times p$ matrix $A$ ::@:: $A \mathbf X \sim N_q(A \boldsymbol \mu, A \boldsymbol \Sigma A')$.
- mean of $A \mathbf X$: for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $A \boldsymbol \mu$.
- covariance matrix of $A \mathbf X$: for $\mathbf X \sim N_p(\boldsymbol \mu, \boldsymbol \Sigma)$ ::@:: $A \boldsymbol \Sigma A'$.

## independence of the components

For a bivariate normal pair $\binom{X_1}{X_2} \sim N_2\left(\binom{\mu_1}{\mu_2}, \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}\right)$, the components $X_1$ and $X_2$ are independent if and only if $\sigma_{12} = \sigma_{21} = 0$. Inside this family, zero covariance and independence are the same condition.

---

Flashcards for this section are as follows:

- independence of two components: $\binom{X_1}{X_2} \sim N_2\left(\binom{\mu_1}{\mu_2}, \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}\right)$ ::@:: $X_1$ and $X_2$ are independent if and only if $\sigma_{12} = \sigma_{21} = 0$.
