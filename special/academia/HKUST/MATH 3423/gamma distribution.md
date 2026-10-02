---
aliases:
  - gamma density
  - gamma distribution
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/gamma_distribution
  - language/in/English
---

# gamma distribution

The _gamma distribution_ is a two-parameter family of distributions on the positive half-line, written $X \sim \text{Gamma}(\alpha, \beta)$ for a shape $\alpha > 0$ and a rate $\beta > 0$. Every positive pair of parameters gives a member.

---

Flashcards for this section are as follows:

- what are the two parameters of $X \sim \text{Gamma}(\alpha, \beta)$, and where is the family supported? ::@:: A shape $\alpha > 0$ and a rate $\beta > 0$, on the positive half-line $(0, \infty)$; every positive pair of parameters gives a member.

## probability density function

The density is $$f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x},$$ for $x > 0$, and $0$ otherwise. Near the origin the power $\alpha - 1$ on $x$ decides where the mass sits: a large $\alpha$ puts most of it away from zero, and a small $\alpha$ pulls it back towards zero, where the density may diverge. The tail decays like $e^{-\beta x}$, and $\beta$ is its rate.

The constant in front, $\Gamma(\alpha) = \int_0^\infty t^{\alpha - 1} e^{-t} \,\mathrm{d}t$, is the gamma function.

With the rate $\beta$ the parameter multiplies $x$ in the exponent. With a scale parameter $\theta = 1/\beta$ in place of the rate, the same family reads $$\frac{1}{\Gamma(\alpha) \theta^\alpha} x^{\alpha - 1} e^{-x/\theta}.$$ The shape $\alpha$ is a power of $x$ in both forms and is never ambiguous; only the second parameter changes its reading. The two forms describe one family: $\alpha/\beta$ and $\alpha\theta$ are the same number once $\theta = 1/\beta$. Read with the wrong parameterization, the same two numbers give a different distribution.

The mean is $$E[X] = \frac{\alpha}{\beta},$$ and the variance is $$\operatorname{Var}(X) = \frac{\alpha}{\beta^2}.$$ Both follow from the density: the first moment brings in $\Gamma(\alpha + 1)$, the second $\Gamma(\alpha + 2)$, and the recursion $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$ reduces each to a power of $\alpha$ times $\Gamma(\alpha)$. The variance is the second moment minus the square of the first.

---

Flashcards for this section are as follows:

- density of $X \sim \text{Gamma}(\alpha, \beta)$ for a shape $\alpha > 0$ and a rate $\beta > 0$ at $x > 0$ ::@:: $$f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}.$$
- density of $X \sim \text{Gamma}(\alpha, \beta)$ at a non-positive value $x \le 0$ ::@:: $0$, so the family is supported on the positive half-line only.
- what the shape $\alpha$ does in the gamma density $f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$ for $x > 0$ ::@:: It is the power $\alpha - 1$ of $x$.
- what the rate $\beta$ does in the gamma density $f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$ for $x > 0$ ::@:: It is the rate at which the exponential $e^{-\beta x}$ decays.
- the normalizing constant of the gamma density $f_X(x \mid \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$: what is $\Gamma(\alpha)$? ::@:: The gamma function $\Gamma(\alpha) = \int_0^\infty t^{\alpha - 1} e^{-t} \,\mathrm{d}t$, the whole normalizing integral once $\beta^\alpha$ is taken out of it.
- density of $X \sim \text{Gamma}(\alpha, \beta)$ rewritten with a scale $\theta = 1/\beta$ in place of the rate ::@:: $$\frac{1}{\Gamma(\alpha) \theta^\alpha} x^{\alpha - 1} e^{-x/\theta}.$$ Here the parameter divides $x$ instead of multiplying it.
- reading of the second parameter of $X \sim \text{Gamma}(\alpha, \beta)$: rate or scale? ::@:: A rate $\beta$ under the rate form and a scale $\theta = 1/\beta$ under the scale form; both describe one family, so a pair of numbers must be read with the parameterization it was written in.
- mean of $X \sim \text{Gamma}(\alpha, \beta)$ for a shape $\alpha > 0$ and a rate $\beta > 0$ ::@:: $\frac{\alpha}{\beta}$, the same under either parameterization since $\theta = 1/\beta$.
- variance of $X \sim \text{Gamma}(\alpha, \beta)$ for a shape $\alpha > 0$ and a rate $\beta > 0$ ::@:: $\frac{\alpha}{\beta^2}$.

## chi-squared distribution as a special case

A gamma variable is a chi-squared member exactly when its rate is $\tfrac{1}{2}$ and its shape is $k/2$ for a positive integer $k$, that is $$\text{Gamma}(\tfrac{k}{2}, \tfrac{1}{2}) = \chi^2(k).$$ A $\chi^2(k)$ variable is a sum of $k$ independent squared standard normal variables: each adds a degree of freedom and a half to the shape, nothing to the rate. The identification of the sum with the member of shape $k/2$ is taken as given. The smallest case is a single square: if $Y \sim N(0, 1)$ then $$Y^2 \sim \chi^2(1) = \text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2}).$$

Substituting shape $k/2$ and rate $\tfrac{1}{2}$ into the mean $\alpha/\beta$ and the variance $\alpha/\beta^2$ gives $$E[\chi^2(k)] = k$$ and $$\operatorname{Var}[\chi^2(k)] = 2k.$$

A squared normal variable is written $$N^{(2)}(0, 1) = \chi^2(1),$$ with the square marked by a superscript. $N_2$ with a subscript instead denotes a bivariate normal vector.

---

Flashcards for this section are as follows:

- which member of the gamma family $X \sim \text{Gamma}(\alpha, \beta)$ is the chi-squared variable $\chi^2(k)$ for a positive integer $k$? ::@:: $\text{Gamma}(\tfrac{k}{2}, \tfrac{1}{2})$: rate exactly $\tfrac{1}{2}$ and shape $k/2$, and failing either condition rules out membership.
- law of the square $Y^2$ of a standard normal variable $Y \sim N(0, 1)$ ::@:: $\chi^2(1)$, which is $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$.
- what the notation $N^{(2)}(0, 1)$ denotes, and how it differs from $N_2$ with a subscript ::@:: The squared standard normal variable, equal in distribution to $\chi^2(1)$; the superscript $2$ marks the square, whereas the subscript $2$ marks a bivariate normal vector.
- mean of the chi-squared variable $\chi^2(k)$ for a positive integer $k$, from the gamma mean $\alpha/\beta$ at $\alpha = k/2$ and $\beta = 1/2$ ::@:: $k$, because $(k/2)/(1/2) = k$.
- variance of the chi-squared variable $\chi^2(k)$ for a positive integer $k$, from the gamma variance $\alpha/\beta^2$ at $\alpha = k/2$ and $\beta = 1/2$ ::@:: $2k$.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Each case below is checked against the two conditions: rate $\tfrac{1}{2}$ and shape $k/2$ for a positive integer $k$.

Two cases satisfy both. With $Y \sim N(0, 1)$ the square $Y^2$ is $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$, the member with one degree of freedom, and a sum of two independent such squares is $\text{Gamma}(1, \tfrac{1}{2}) = \chi^2(2)$.

Three cases fail on the rate. Doubling a single square divides the rate by two, so $2Y^2$ keeps the shape one half and takes the rate $\tfrac{1}{4}$, giving $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{4})$. The mean alone does not separate it from $\chi^2(2)$, since both have mean 2, while the variance of $2Y^2$ is 8 and the variance of $\chi^2(2)$ is 4. The gamma with shape $2$ and rate $1$ has the shape required for $k = 4$, which is $4/2 = 2$, but its rate is $1$ and not $\tfrac{1}{2}$. The squared deviation $(X - \mu)^2$ of $X \sim N(\mu, \sigma^2)$ is the variance times a $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2})$ variable, so its shape is one half and its rate is $1/(2\sigma^2)$, which is $\tfrac{1}{2}$ only when $\sigma^2 = 1$.

The last case fails on the centering rather than on the rate. The square $X^2$ of a normal variable with unknown mean and standard deviation is not centered: dividing by the standard deviation leaves a normal variable whose mean is the unknown $\mu$ and not zero, and the law of its square changes with that mean, so $X^2$ is not a member.

---

Flashcards for this section are as follows:

- $Y^2$ for $Y \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: Yes: rate $\tfrac{1}{2}$ and shape $k/2$ at $k = 1$, so $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{2}) = \chi^2(1)$.
- $Y_1^2 + Y_2^2$ for independent $Y_1, Y_2 \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: Yes: rate $\tfrac{1}{2}$ and shape $k/2$ at $k = 2$, so $\chi^2(2) = \text{Gamma}(1, \tfrac{1}{2})$.
- $2Y^2$ for $Y \sim N(0, 1)$: a chi-squared member of the gamma family? ::@:: No, it fails on the rate: doubling divides the rate by two, giving $\text{Gamma}(\tfrac{1}{2}, \tfrac{1}{4})$, while the shape stays one half.
- a variable with distribution $\text{Gamma}(2, 1)$: a chi-squared member of the gamma family? ::@:: No, its rate is $1$, and every chi-squared member has rate $\tfrac{1}{2}$.
- $(X - \mu)^2$ for $X \sim N(\mu, \sigma^2)$: a chi-squared member of the gamma family? ::@:: No, its rate is $1/(2\sigma^2)$ rather than $\tfrac{1}{2}$, and the rate is one half only when $\sigma^2 = 1$.
- $X^2$ for $X \sim N(\mu, \sigma^2)$ with $\mu$ and $\sigma$ unknown: a chi-squared member of the gamma family? ::@:: No, it fails on the centering: the mean is not zero, so the unknown $\mu$ is never divided out and the law of the square depends on it.
