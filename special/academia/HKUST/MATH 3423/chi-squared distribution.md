---
aliases:
  - chi-square distribution
  - chi-squared
  - chi-squared distribution
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/chi-squared_distribution
  - language/in/English
---

# chi-squared distribution

The _chi-squared distribution_ is a family of distributions on the positive half-line, written $\chi^2(r)$, where $r$ is the degrees of freedom, a positive integer. The name describes the construction: a member is a standard normal variable squared, or a sum of $r$ such squares. The index $r$ counts the independent squared terms in that sum.

The scaled sample variance of a normal sample of size $n > 1$ is distributed as $\chi^2(n - 1)$ and not as $\chi^2(n)$. It does not follow from additivity: the deviations $X_i - \bar X$ of a sample are not independent of one another, and independence is exactly what the additivity theorem needs.

---

Flashcards for this section are as follows:

- which values the degrees of freedom $r$ of a chi-squared variable may take ::@:: Positive integers only.
- how a chi-squared variable with $r$ degrees of freedom is built from standard normal variables ::@:: A sum of $r$ independent squared standard normal variables, so $r$ counts the terms.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$, the law of $\frac{(n - 1) S_{n-1}^2}{\sigma^2}$, where $S_{n-1}^2$ is the sample variance dividing the sum of squared deviations by $n - 1$ ::@:: $\chi^2(n - 1)$; the index is $n - 1$ rather than $n$.
- for $X_1, \ldots, X_n$ i.i.d. from $N(\mu, \sigma^2)$, $n > 1$: does additivity of $\chi^2$ variables give the law of $\frac{(n - 1) S_{n-1}^2}{\sigma^2}$, where $S_{n-1}^2$ is the sample variance dividing the sum of squared deviations by $n - 1$ ::@:: No: the deviations from the sample mean are not independent of one another, and additivity needs independence.
- the values a chi-squared variable can take ::@:: The positive half-line, because a member is a sum of squares and a square is never negative.

## squared standard normal

For $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$, the variable $V = (X - \mu)^2 / \sigma^2$ is the square of a standard normal variable, so it follows $\chi^2(1)$. Subtracting $\mu$ makes the square measure deviation from the center of the distribution rather than from zero. Dividing by the variance removes the scale, so the law of $V$ does not depend on the units the data are measured in.

The condition $\sigma^2 > 0$ is required. At $\sigma^2 = 0$ the variable has no spread: $X$ is the constant $\mu$, and there is no variance to divide by, so the standardization is not defined there at all. The support follows from the squaring: a square of a real number is never negative, and $V = 0$ happens with probability zero for a continuous variable.

---

Flashcards for this section are as follows:

- for $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$, the law of $(X - \mu)^2 / \sigma^2$ ::@:: $\chi^2(1)$, because $(X - \mu)/\sigma$ is standard normal and the variable is its square.
- for $X \sim N(\mu, \sigma^2)$, the condition on $\sigma^2$ that makes $(X - \mu)^2 / \sigma^2$ chi-squared ::@:: $\sigma^2 > 0$, so the standardization needs a normal variable that has spread.
- why $\mu$ is subtracted in $(X - \mu)^2 / \sigma^2$ for $X \sim N(\mu, \sigma^2)$, $\sigma^2 > 0$ ::@:: The square then measures deviation from the center of the distribution rather than from zero.
- why $(X - \mu)^2 / \sigma^2$ is divided by $\sigma^2$ for $X \sim N(\mu, \sigma^2)$, $\sigma^2 > 0$ ::@:: It removes the scale, so the law of the variable does not depend on the units the data are measured in.
- at $\sigma^2 = 0$, what is $(X - \mu)^2 / \sigma^2$ for $X \sim N(\mu, \sigma^2)$ ::@:: Undefined: $X$ is then the constant $\mu$, and there is no variance to divide by.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Take $X \sim N(3, 4)$, so the standard deviation is $2$. The squared deviation $W = (X - 3)^2 / 4$ is the one-degree-of-freedom member, because $(X - 3)/2$ is standard normal and a standard normal variable has one degree of freedom.

Omitting the division gives $W' = (X - 3)^2 = 4\chi^2(1)$, the variance times a chi-squared variable. A constant multiple of a member is a member only when the multiple is $1$. Dividing the unsquared deviation by the standard deviation instead of the variance gives $U = (X - 3)/2$, a standard normal variable. $U$ takes negative values, which a chi-squared variable never does. Dividing the squared deviation by the standard deviation gives $T = (X - 3)^2 / 2$, the standard deviation times a chi-squared variable. A factor of $\sigma$ remains in $T$ where $\sigma^2$ was needed.

---

Flashcards for this section are as follows:

- $W = (X - 3)^2 / 4$ for $X \sim N(3, 4)$: a chi-squared variable? ::@:: Yes, it is $\chi^2(1)$, since $(X - 3)/2$ is standard normal and $W$ is that variable squared.
- $W' = (X - 3)^2$ for $X \sim N(3, 4)$: a chi-squared variable? ::@:: No, it is $4$ times a $\chi^2(1)$ variable, and a constant multiple of a member is a member only when the multiple is $1$.
- $U = (X - 3)/2$ for $X \sim N(3, 4)$: a chi-squared variable? ::@:: No, it is standard normal, taking negative values instead of being supported on the positive half-line.
- $T = (X - 3)^2 / 2$ for $X \sim N(3, 4)$: a chi-squared variable? ::@:: No, it is the standard deviation $2$ times a $\chi^2(1)$ variable, so a factor of $\sigma$ remains where $\sigma^2$ was needed.

## additivity

For independent $X_1, X_2, \ldots, X_k$ with distributions $\chi^2(r_1), \chi^2(r_2), \ldots, \chi^2(r_k)$, $$Y = \sum_{i=1}^{k} X_i \sim \chi^2(r_1 + \cdots + r_k).$$ The theorem is taken as given, and the representation rests on it.

A $\chi^2(1)$ variable is one squared standard normal, so $k$ independent ones give a sum of $k$ squared standard normals, which the theorem calls $\chi^2(k)$. A member with $r$ degrees of freedom is therefore a sum of $r$ squared standard normal terms. The two moments follow from the terms rather than from the density of a member, because a mean and a variance of a sum are the sums of the means and variances of the independent terms.

Each squared standard normal term has mean $1$ and variance $2$, and both come from the standard normal density by integration by parts. Each step takes one power off the integrand and leaves the unweighted integral of the exponential in its place; the boundary term is 0 at both ends, since the power is 0 at the origin and the exponential drives the product to 0 at infinity. The same step applied to the fourth power gives the fourth moment the same way, $$E[Z^2] = \frac{2}{\sqrt{2\pi}}\int_0^\infty z^2 e^{-z^2/2}\,dz = 1$$ and $$E[Z^4] = \frac{2}{\sqrt{2\pi}}\int_0^\infty z^4 e^{-z^2/2}\,dz = 3.$$ The variance of $Z^2$ is then $3 - 1^2 = 2$, and a sum of $r$ independent terms has mean $r$ and variance $2r$, so $$E[\chi^2(r)] = r$$ and $$\operatorname{Var}[\chi^2(r)] = 2r.$$

Independence is what carries the theorem, because the law of a sum is not fixed by the laws of its parts. Let the two variables be the same member instead, $X_1 = X_2 = W$ with $W \sim \chi^2(1)$. Both marginals are $\chi^2(1)$ and both are non-negative, but their sum is $2W$, a constant multiple of a member rather than a member, so it is not $\chi^2(2)$ however the indices are added.

---

Flashcards for this section are as follows:

- the sum of independent chi-squared variables $X_i \sim \chi^2(r_i)$, $i = 1, \ldots, k$ ::@:: $Y = \sum_{i=1}^{k} X_i \sim \chi^2(r_1 + \cdots + r_k)$: independent members add their indices.
- the mean of a chi-squared variable with $r$ degrees of freedom ::@:: $r$, the index itself, because each of the $r$ squared standard normal terms has mean $1$.
- the variance of a chi-squared variable with $r$ degrees of freedom ::@:: $2r$, twice the index, because each squared standard normal term has variance $2$.
- the sum of two $\chi^2(1)$ variables that are the same variable, $X_1 = X_2 = W$ with $W \sim \chi^2(1)$: is the sum $\chi^2(2)$? ::@:: No, the sum is $2W$, a constant multiple of a member rather than a member, because the two summands are not independent.
- the mean of a squared standard normal variable $Z^2$ for $Z \sim N(0, 1)$ ::@:: $1$, since the standard normal density gives $\frac{2}{\sqrt{2\pi}}\int_0^\infty z^2 e^{-z^2/2}\,dz = 1$ by integration by parts.
- the variance of a squared standard normal variable $Z^2$ for $Z \sim N(0, 1)$ ::@:: $2$, the gap between $E[Z^4] = 3$ and the square of $E[Z^2] = 1$.
