---
aliases:
  - gamma density
  - gamma distribution
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/gamma_distribution
  - language/in/English
---

# gamma distribution

The _gamma distribution_ is a two-parameter family of distributions on the positive half-line, written $X \sim \text{Gamma}(\alpha, \beta)$ for a shape $\alpha > 0$ and a rate $\beta > 0$. Every positive pair of parameters gives a member. One part of the family is the chi-squared family: choosing the rate to be $\tfrac{1}{2}$ makes it contain every chi-squared distribution.

---

Flashcards for this section are as follows:

- overview: for a shape $\alpha > 0$ and a rate $\beta > 0$ ::@:: A two-parameter family of distributions on the positive half-line, written $X \sim \text{Gamma}(\alpha, \beta)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- relation to the chi-squared distribution: for a positive integer $k$ ::@:: $\text{Gamma}(\tfrac{k}{2}, \tfrac{1}{2}) = \chi^2(k)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## probability density function

The density is $$f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x},$$ for $x > 0$, and $0$ otherwise. The power $\alpha - 1$ on $x$ decides the shape near the origin: a large $\alpha$ puts most of the mass away from zero, and a small $\alpha$ pulls it back towards zero, where the density may diverge. The exponential $e^{-\beta x}$ decides the tail, with $\beta$ the rate at which the density decays.

The constant in front, $\Gamma(\alpha) = \int_0^\infty t^{\alpha - 1} e^{-t} \,\mathrm{d}t$, is the gamma function. It is the whole of the normalizing integral once the rate's power has been taken out of it, so what is left to divide by depends on the shape alone.

The second parameter has two standard names, and the same number is a rate in one and a scale in the other. With the rate $\beta$ the parameter multiplies $x$ in the exponent. Substituting a scale parameter $\theta = 1/\beta$ in place of the rate, the same family reads $$\frac{1}{\Gamma(\alpha) \theta^\alpha} x^{\alpha - 1} e^{-x/\theta}.$$ Here the parameter divides $x$ instead. The shape $\alpha$ is a power of $x$ in both forms and is never ambiguous; only the second parameter changes its reading. The two forms do not describe two families: $\alpha/\beta$ and $\alpha\theta$ are the same number once $\theta = 1/\beta$. A pair of numbers still has to be read with the parameterization it was written in; assume the other and the same two symbols give a different distribution.

The mean is $$E[X] = \frac{\alpha}{\beta},$$ and the variance is $$\operatorname{Var}(X) = \frac{\alpha}{\beta^2}.$$ Both follow from the density: the first moment brings in $\Gamma(\alpha + 1)$, the second $\Gamma(\alpha + 2)$, and the recursion $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$ reduces each to a power of $\alpha$ times $\Gamma(\alpha)$. The variance is the second moment minus the square of the first.

---

Flashcards for this section are as follows:

- density of $X \sim \text{Gamma}(\alpha, \beta)$: for $x > 0$ ::@:: $$f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}.$$ <!--SR:!fsrs,2026-11-02T00:10:00.000Z,0,2.3065,2.11810397,1,1,0,1,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- density of $X \sim \text{Gamma}(\alpha, \beta)$: for $x \le 0$ ::@:: $0$, so the family is supported on the positive half-line only. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- role of $\alpha$ in the gamma density ::@:: The shape parameter, appearing as the power $\alpha - 1$ of $x$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- role of $\beta$ in the gamma density ::@:: The rate parameter, appearing as the exponential rate in $e^{-\beta x}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $\Gamma(\cdot)$ in the gamma density ::@:: The gamma function, $\Gamma(\alpha) = \int_0^\infty t^{\alpha - 1} e^{-t} \,\mathrm{d}t$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- scale parameterization of the gamma density: in place of the rate $\beta$ ::@:: $\frac{1}{\Gamma(\alpha) \theta^\alpha} x^{\alpha - 1} e^{-x/\theta}$, where $\theta = 1/\beta$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- second parameter of $X \sim \text{Gamma}(\alpha, \beta)$: rate or scale ::@:: A rate $\beta$ in one parameterization and a scale $\theta = 1/\beta$ in the other; both describe the same family, so a pair of numbers has to be read with the parameterization it was written in. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- mean of $X \sim \text{Gamma}(\alpha, \beta)$ ::@:: $\frac{\alpha}{\beta}$, in either parameterization since $\theta = 1/\beta$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- variance of $X \sim \text{Gamma}(\alpha, \beta)$ ::@:: $\frac{\alpha}{\beta^2}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## chi-squared distribution as a special case

A gamma variable is a chi-squared member exactly when its rate is $\tfrac{1}{2}$ and its shape is $k/2$ for a positive integer $k$, that is $$\text{Gamma}(\tfrac{k}{2}, \tfrac{1}{2}) = \chi^2(k).$$ Both conditions are needed, since a shape of $k/2$ with any other rate is not a member. A $\chi^2(k)$ variable is a sum of $k$ independent squared standard normal variables, so its shape is built one half at a time while its rate stays at $\tfrac{1}{2}$: each squared standard normal adds one degree of freedom and one half to the shape, and changes nothing in the rate. The identification of the sum with the member of shape $k/2$ is taken as given. The smallest case is a single square: if $Y \sim N(0, 1)$ then $$Y^2 \sim \chi^2(1) = \text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2}).$$

Substituting shape $k/2$ and rate $\tfrac{1}{2}$ into the mean $\alpha/\beta$ and the variance $\alpha/\beta^2$ gives $$E[\chi^2(k)] = k$$ and $$\operatorname{Var}[\chi^2(k)] = 2k.$$

A squared normal variable is written $$N^{(2)}(0, 1) = \chi^2(1),$$ with the square marked by a superscript. $N_2$ with a subscript instead denotes a bivariate normal vector.

---

Flashcards for this section are as follows:

- gamma member equal to a chi-squared variable: for a positive integer $k$ ::@:: $\text{Gamma}(\tfrac{k}{2}, \tfrac{1}{2}) = \chi^2(k)$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- distribution of the square of a standard normal variable: $Y \sim N(0, 1)$ ::@:: $Y^2 \sim \chi^2(1)$, which is $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- meaning of the notation $N^{(2)}(0, 1)$ ::@:: The squared standard normal variable, equal in distribution to $\chi^2(1)$; the superscript $2$ marks the square, not a bivariate normal. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- condition for $X \sim \text{Gamma}(\alpha, \beta)$ to be a chi-squared member: the rate and the shape ::@:: Exactly when the rate is $\tfrac{1}{2}$ and the shape is $k/2$ for a positive integer $k$; either condition failing is enough to rule out membership. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- mean of $\chi^2(k)$ by substitution: for a positive integer $k$ ::@:: $k$, since $\alpha/\beta$ at $\alpha = k/2$ and $\beta = 1/2$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- variance of $\chi^2(k)$ by substitution: for a positive integer $k$ ::@:: $2k$, since $\alpha/\beta^2$ at $\alpha = k/2$ and $\beta = 1/2$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

A gamma is a chi-squared member when its rate is $\tfrac{1}{2}$ and its shape is $k/2$ for a positive integer $k$, and each case below is checked against those two conditions.

Two cases satisfy both. With $Y \sim N(0, 1)$ the square $Y^2$ is $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$, the member with one degree of freedom, and a sum of two independent such squares is $\text{Gamma}(1, \tfrac{1}{2}) = \chi^2(2)$.

Three cases fail on the rate. Doubling a single square divides the rate by two, so $2Y^2$ keeps the shape one half and takes the rate $\tfrac{1}{4}$, giving $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{4})$. The mean alone does not separate it from $\chi^2(2)$, since both have mean 2, while the variance of $2Y^2$ is 8 and the variance of $\chi^2(2)$ is 4. The gamma with shape $2$ and rate $1$ has the shape required for $k = 4$, which is $4/2 = 2$, but its rate is $1$ and not $\tfrac{1}{2}$. The squared deviation $(X - \mu)^2$ of $X \sim N(\mu, \sigma^2)$ is the variance times a $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$ variable, so its shape is one half and its rate is $1/(2\sigma^2)$, which is $\tfrac{1}{2}$ only when $\sigma^2 = 1$.

The last case fails on the centering rather than on the rate. The square $X^2$ of a normal variable with unknown mean and standard deviation is not centered: dividing by the standard deviation leaves a normal variable whose mean is the unknown $\mu$ and not zero, and the law of its square changes with that mean, so $X^2$ is not a member.

---

Flashcards for this section are as follows:

- $Y^2$ for $Y \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: Yes, it is $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2}) = \chi^2(1)$, with the rate one half. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $Y_1^2 + Y_2^2$ for independent $Y_1, Y_2 \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: Yes, it is $\chi^2(2) = \text{Gamma}(1, \tfrac{1}{2})$, with shape one and rate one half. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $2Y^2$ for $Y \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: No, it fails on the rate: doubling divides the rate by two, giving $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{4})$, while the shape stays one half. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a variable with distribution $\text{Gamma}(2, 1)$: a chi-squared member of the gamma family? ::@:: No, its rate is $1$, and every chi-squared member has rate $\tfrac{1}{2}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $(X - \mu)^2$ for $X \sim N(\mu, \sigma^2)$: a chi-squared member of the gamma family? ::@:: No, its rate is $1/(2\sigma^2)$ rather than $\tfrac{1}{2}$, and the rate is one half only when $\sigma^2 = 1$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- $X^2$ for $X \sim N(\mu, \sigma^2)$ with $\mu$ and $\sigma$ unknown: a chi-squared member of the gamma family? ::@:: No, it fails on the centering: the mean is not zero, so the unknown $\mu$ is never divided out and the law of the square depends on it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
