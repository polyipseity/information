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

The _chi-squared distribution_ is a family of distributions on the positive half-line, indexed by its degrees of freedom $r$, a positive integer, and written $\chi^2(r)$. It is generated from the normal distribution: a squared standard normal variable is the one-degree-of-freedom member, and independent members add their degrees of freedom. The scaled sample variance of a normal sample of size $n$ is distributed as $\chi^2(n - 1)$.

---

Flashcards for this section are as follows:

- overview: for $r$ degrees of freedom ::@:: A family of distributions on the positive half-line, written $\chi^2(r)$.
- degrees of freedom $r$: the parameter of $\chi^2(r)$ ::@:: A positive integer.
- how the family is generated: starting from $\chi^2(1)$ and adding independent members ::@:: Independent chi-squared variables add their degrees of freedom, so a sum of $r$ independent squared standard normal variables is $\chi^2(r)$.

## squared standard normal

If the random variable $X$ follows $N(\mu, \sigma^2)$ with $\sigma^2 > 0$, then $V = (X - \mu)^2 / \sigma^2$ follows $\chi^2(1)$. Subtracting the mean and dividing by the standard deviation standardizes $X$, so $V$ is the square of a standard normal variable. That square is the one-degree-of-freedom member of the family.

---

Flashcards for this section are as follows:

- distribution of a standardized normal variable squared: $X \sim N(\mu, \sigma^2)$ with $\sigma^2 > 0$ ::@:: $V = (X - \mu)^2 / \sigma^2 \sim \chi^2(1)$.
- why $(X - \mu)^2 / \sigma^2$ is $\chi^2(1)$: writing $Z = (X - \mu)/\sigma$ ::@:: $Z \sim N(0, 1)$, so $V = Z^2$ is the square of a standard normal variable.
- condition on $\sigma^2$: for $V = (X - \mu)^2 / \sigma^2 \sim \chi^2(1)$ with $X \sim N(\mu, \sigma^2)$ ::@:: $\sigma^2 > 0$.

## additivity

Independent chi-squared variables add. If $X_1, X_2, \ldots, X_k$ have distributions $\chi^2(r_1), \chi^2(r_2), \ldots, \chi^2(r_k)$ respectively and are independent, then $Y = \sum_{i=1}^{k} X_i$ follows $\chi^2(r_1 + \cdots + r_k)$.

---

Flashcards for this section are as follows:

- sum of chi-squared variables: $X_i \sim \chi^2(r_i)$ for $i = 1, \ldots, k$ ::@:: If the variables are independent, $Y = \sum_{i=1}^{k} X_i \sim \chi^2(r_1 + \cdots + r_k)$.
- degrees of freedom of a sum: $X_i \sim \chi^2(r_i)$, independent, for $i = 1, \ldots, k$ ::@:: They add, giving $r_1 + \cdots + r_k$.
