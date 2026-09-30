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

The _chi-squared distribution_ is a family of distributions on the positive half-line, written $\chi^2(r)$, where $r$ is the degrees of freedom, a positive integer. The name describes the construction: a member is a standard normal variable squared, or a sum of such squares. The index $r$ counts the independent squared terms in that sum, and independent members add their indices.

The scaled sample variance of a normal sample of size $n$ is distributed as $\chi^2(n - 1)$. The index is $n - 1$ and not $n$, and that gap is the content of the result. It does not follow from additivity: the deviations $X_i - \bar X$ of a sample are not independent of one another, and independence is exactly what the additivity theorem needs.

---

Flashcards for this section are as follows:

- overview: for $r$ degrees of freedom ::@:: A family of distributions on the positive half-line, written $\chi^2(r)$.
- degrees of freedom $r$: the parameter of $\chi^2(r)$ ::@:: A positive integer.
- how the family is generated: starting from $\chi^2(1)$ and adding independent members ::@:: Degrees of freedom add, so a sum of $r$ independent squared standard normal variables is $\chi^2(r)$.
- the scaled sample variance of a normal sample of size $n$ and its index ::@:: It follows $\chi^2(n - 1)$, with $n - 1$ rather than $n$ because the deviations are not independent.
- whether the sample variance result comes from additivity of $\chi^2(r)$ ::@:: No, the deviations $X_i - \bar X$ are not independent, and independence is the condition additivity needs.
- support of a $\chi^2(r)$ variable: the values it can take ::@:: The positive half-line, because a member is a sum of squares and a square is never negative.

## squared standard normal

Subtracting $\mu$ makes the square measure deviation from the center of the distribution rather than from zero, and dividing by $\sigma$ removes the scale, so the law of the result does not depend on the units the data are measured in. For $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$, the variable $V = (X - \mu)^2 / \sigma^2$ is the square of a standard normal variable and follows $\chi^2(1)$.

The condition $\sigma^2 > 0$ is not a matter of convenience: at $\sigma^2 = 0$ the variable has no spread, $X$ is the constant $\mu$, and there is no variance to divide by, so the standardization is not defined there at all. The support of the family comes from the same construction: a square of a real number is never negative, and $V = 0$ happens with probability zero for a continuous variable, which is why the family sits on the positive half-line rather than on the whole line.

---

Flashcards for this section are as follows:

- distribution of a standardized normal variable squared: $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$ ::@:: $V = (X - \mu)^2 / \sigma^2 \sim \chi^2(1)$.
- why $(X - \mu)^2 / \sigma^2$ is $\chi^2(1)$: writing $Z = (X - \mu)/\sigma$ ::@:: $Z \sim N(0, 1)$, so $V = Z^2$ is its square.
- condition on $\sigma^2$: in $(X - \mu)^2 / \sigma^2 \sim \chi^2(1)$ with $X \sim N(\mu, \sigma^2)$ ::@:: $\sigma^2 > 0$.
- why the mean is subtracted in $V = (X - \mu)^2 / \sigma^2$ ::@:: So that the square measures deviation from the center of the distribution rather than from zero.
- why the variance is divided out in $V = (X - \mu)^2 / \sigma^2$ ::@:: To remove the scale, so the law of $V$ does not depend on the units the data are measured in.
- what happens to $(X - \mu)^2 / \sigma^2$ at $\sigma^2 = 0$ ::@:: It is undefined, since $X$ is then the constant $\mu$ and there is no variance to divide by.

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

For independent $X_1, X_2, \ldots, X_k$ with distributions $\chi^2(r_1), \chi^2(r_2), \ldots, \chi^2(r_k)$, $$Y = \sum_{i=1}^{k} X_i \sim \chi^2(r_1 + \cdots + r_k).$$ The theorem is taken as given here, and the representation rests on it.

A $\chi^2(1)$ variable is one squared standard normal, so $k$ independent ones give a sum of $k$ squared standard normals, which the theorem calls $\chi^2(k)$. A member with $r$ degrees of freedom is therefore a sum of $r$ squared standard normal terms. The two moments follow from the terms rather than from the density of a member, because a mean and a variance of a sum are the sums of the means and variances of the independent terms.

Each squared standard normal term has mean $1$ and variance $2$, and both come from the standard normal density by integration by parts. Each step takes one power off the integrand and leaves the unweighted integral of the exponential in its place; the boundary term is 0 at both ends, since the power is 0 at the origin and the exponential drives the product to 0 at infinity. The same step applied to the fourth power gives the fourth moment the same way, $$E[Z^2] = \frac{2}{\sqrt{2\pi}}\int_0^\infty z^2 e^{-z^2/2}\,dz = 1$$ and $$E[Z^4] = \frac{2}{\sqrt{2\pi}}\int_0^\infty z^4 e^{-z^2/2}\,dz = 3.$$ The variance of $Z^2$ is then $3 - 1^2 = 2$, and a sum of $r$ independent terms has mean $r$ and variance $2r$, so $$E[\chi^2(r)] = r$$ and $$\operatorname{Var}[\chi^2(r)] = 2r.$$

Independence is what carries the theorem, because the law of a sum is not fixed by the laws of its parts. Let the two variables be the same member instead, $X_1 = X_2 = W$ with $W \sim \chi^2(1)$. Both marginals are $\chi^2(1)$ and both are non-negative, but their sum is $2W$, a constant multiple of a member rather than a member, so it is not $\chi^2(2)$ however the indices are added.

---

Flashcards for this section are as follows:

- sum of chi-squared variables: $X_i \sim \chi^2(r_i)$ for $i = 1, \ldots, k$ ::@:: If the variables are independent, $Y = \sum_{i=1}^{k} X_i \sim \chi^2(r_1 + \cdots + r_k)$.
- mean of a chi-squared variable: for $\chi^2(r)$ with $r$ degrees of freedom ::@:: $r$, the index itself, because each squared standard normal term has mean $1$ and there are $r$ of them.
- variance of a chi-squared variable: for $\chi^2(r)$ with $r$ degrees of freedom ::@:: $2r$, twice the index, because each squared standard normal term has variance $2$.
- the sum of two $\chi^2(1)$ variables that are the same variable, $X_1 = X_2 = W$ with $W \sim \chi^2(1)$: is the sum $\chi^2(2)$? ::@:: No, the sum is $2W$, a constant multiple of a member rather than a member, because the two summands are not independent.
- mean of a squared standard normal variable: for $Z \sim N(0, 1)$ ::@:: $1$, since the standard normal density gives $\frac{2}{\sqrt{2\pi}}\int_0^\infty z^2 e^{-z^2/2}\,dz = 1$ by integration by parts.
- variance of a squared standard normal variable: for $Z \sim N(0, 1)$ ::@:: $2$, the gap between $E[Z^4] = 3$ and the square of $E[Z^2] = 1$.
