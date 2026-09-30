---
aliases:
  - Independent and identically distributed random variables
  - i.i.d.
  - iid
  - random sample
  - random samples
tags:
  - flashcard/active/special/academia/HKUST/MATH_3423/random_sample
  - language/in/English
---

# random sample

A _random sample_ is a collection of independent and identically distributed copies of a random variable $X$, and $X_1, \ldots, X_n$ has this structure unless stated otherwise. Independence and identical distribution are two conditions rather than one, and a collection can satisfy either of them without the other.

---

Flashcards for this section are as follows:

- definition: for copies $X_1, \ldots, X_n$ of the random variable $X$ ::@:: A collection of independent and identically distributed copies of $X$.
- requirement on the copies $X_1, \ldots, X_n$ ::@:: Independent and identically distributed, abbreviated i.i.d., unless otherwise stated.
- which value of $X_i$ is meant by $x_i$ ::@:: The actual value taken by the $i$-th copy $X_i$ of $X$.

## the i.i.d. assumption

Independence says no copy of $X$ carries information about any other. Probabilities for the sample then multiply, and $\operatorname{Var}(X_1 + \cdots + X_n) = \operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n)$. A copy whose law changes once the earlier draws are known is carrying information about them.

Identical distribution says every copy follows the same law as $X$. One parameter $\theta$ then describes all $n$ copies at once, and the sample is $n$ repetitions of one problem rather than $n$ separate problems with a parameter apiece.

Failing both at once is the easy one to recognize. Failing exactly one is the harder case, because the condition that still holds keeps the familiar calculations working and nothing in the arithmetic announces the failure.

---

Flashcards for this section are as follows:

- why independence is assumed: for $X_1, \ldots, X_n$ ::@:: No copy carries information about any other, so probabilities for the sample multiply and $\operatorname{Var}(X_1 + \cdots + X_n) = \operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n)$.
- why identical distribution is assumed: for $X_1, \ldots, X_n$ ::@:: Every copy follows the same distribution as $X$, so one parameter $\theta$ describes the whole sample.
- abbreviation for independent and identically distributed copies of $X$ ::@:: i.i.d.
- independence and identical distribution: one requirement or two ::@:: Two, and a collection can satisfy either without the other, as the urn draws and the unequal-variance pair show.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples

Each case passes or fails on one specific ground. Four hold the marginals identical and fail independence, one is independent without a common law, and one fails both at once.

A sample of $n$ independent rolls of a fair die is a random sample. The copies are independent, and each has the uniform law on $\{1, \ldots, 6\}$. Independent copies of a normal variable with common mean $\mu$ and common variance $\sigma^2$ form a random sample in continuous form.

Drawing $n$ balls without replacement from an urn is not a random sample. The urn holds $N$ balls, of which $W$ are white. The white indicator $X_i$ of draw $i$ satisfies $\operatorname{Cov}(X_1, X_2) = -\frac{p(1-p)}{N-1} < 0$ with $p = \frac{W}{N}$, because a white first draw leaves fewer white balls behind. Removing balls changes what the next draw can be, so the conditional law of $X_{i+1}$ given the earlier draws differs from its unconditional law. The draws are exchangeable, so the marginals stay identical. Independence is what fails.

A pair with $X_2 = X_1$ is dependent on the same ground. Here $\operatorname{Cov}(X_1, X_2) = \operatorname{Var}(X_1) > 0$, and knowing $X_1$ fixes $X_2$. The pair $U$ and $1-U$ for $U \sim \text{Unif}(0, 1)$ is the same failure with the sign reversed. Both marginals are $\text{Unif}(0, 1)$, yet $\operatorname{Cov}(U, 1-U) = -\operatorname{Var}(U) < 0$ and knowing $U$ fixes $1-U$.

The mean-reverting series $X_{i+1} = \rho X_i + \varepsilon_{i+1}$ with $0 < \rho < 1$ and i.i.d. errors $\varepsilon_i \sim N(0, \sigma^2)$ independent of $X_1 \sim N\left(0, \frac{\sigma^2}{1-\rho^2}\right)$ has identical marginals by construction, so independence is the only thing it can fail on. Every copy has the same law $N\left(0, \frac{\sigma^2}{1-\rho^2}\right)$, and $\operatorname{Cov}(X_i, X_{i+1}) = \rho\frac{\sigma^2}{1-\rho^2} > 0$. The sample is not random.

Drop the $\rho$ and the series $X_{i+1} = X_i + \varepsilon_{i+1}$ is a random walk. The copies are neither independent nor identically distributed, since $\operatorname{Var}(X_i) = i\sigma^2$ grows with $i$.

---

Flashcards for this section are as follows:

- $n$ independent rolls of a fair die: random sample or not ::@:: Yes, the rolls are independent and each copy has the uniform law on $\{1, \ldots, 6\}$, so the copies are i.i.d.
- independent copies of $N(\mu, \sigma^2)$ with a common $\mu$ and a common $\sigma^2$: random sample or not ::@:: Yes, every copy is independent of the others and shares the single law $N(\mu, \sigma^2)$.
- $n$ draws without replacement from an urn of $N$ balls, $W$ of them white: random sample or not ::@:: No, $\operatorname{Cov}(X_1, X_2) = -\frac{p(1-p)}{N-1} < 0$ for the white indicators, since a white first draw depletes the white balls.
- a pair with $X_2 = X_1$: random sample or not ::@:: No, $\operatorname{Cov}(X_1, X_2) = \operatorname{Var}(X_1) > 0$ and knowing $X_1$ fixes $X_2$.
- the pair $U$ and $1-U$ for $U \sim \text{Unif}(0, 1)$: random sample or not ::@:: No, both marginals are $\text{Unif}(0, 1)$ but $\operatorname{Cov}(U, 1-U) = -\operatorname{Var}(U) < 0$ and $1-U$ is determined by $U$.
- mean-reverting series $X_{i+1} = \rho X_i + \varepsilon_{i+1}$ with $0 < \rho < 1$: random sample or not ::@:: No, every copy has the same law, but $\operatorname{Cov}(X_i, X_{i+1}) = \frac{\rho\sigma^2}{1-\rho^2} > 0$ makes the copies dependent.
- random walk $X_{i+1} = X_i + \varepsilon_{i+1}$ with i.i.d. errors $\varepsilon_i \sim N(0, \sigma^2)$: random sample or not ::@:: No, both conditions fail, since $\operatorname{Var}(X_i) = i\sigma^2$ grows with $i$ so the copies are neither independent nor identically distributed.

## joint distribution under random sampling

For continuous copies the joint pdf is $f(x_1, \ldots, x_n \mid \theta) = \prod_{i=1}^{n} f_X(x_i \mid \theta)$. For discrete copies the joint pmf is the analogous product over $i = 1, \ldots, n$.

That product is independence written as a factorization. Identical distribution is what lets all $n$ factors be the same $f_X$ rather than $n$ different ones, and the single $\theta$ carried by every factor is the one parameter the whole sample shares.

The two directions of that equality are not equally deep. Independent copies have a product density by the definition of independence, and the product form above rests on it. A density that splits into one factor per copy belongs to independent copies by that same definition read backwards. The one implication that is not definitional is the normal-family one, where a zero cross-covariance forces the split: for components of a jointly normal vector a zero covariance and independence are the same condition, and the factorization behind it is carried out in [independence of the components](multivariate%20normal%20distribution.md#independence%20of%20the%20components). Outside that family a zero covariance and a dependence can sit together, so the implication is not available elsewhere.

Without independence the joint law is not a product at all, and the calculation route closes. Without identical distribution the product survives but its factors differ, one for each copy, so there is no single $f_X$ to write and no single unknown left to solve for.

---

Flashcards for this section are as follows:

- joint pdf of a random sample: $f(x_1, \ldots, x_n \mid \theta)$ for independent copies ::@:: $\prod_{i=1}^{n} f_X(x_i \mid \theta)$.
- joint pmf of a random sample: for independent copies, $i = 1, \ldots, n$ ::@:: $\prod_{i=1}^{n} p_X(x_i \mid \theta)$.
- how many parameters a random sample carries: $\theta$ in the joint factorization ::@:: One, shared by every copy.
- independent copies that are not identically distributed: is the joint density still a product over $i = 1, \ldots, n$? ::@:: Yes, but of $n$ different factors, one per copy, instead of $n$ copies of a single $f_X$.
- dependent copies: is the joint density a product? ::@:: No, the split into one factor per copy is what independence gives, and a joint density that fails to split shows the copies are not independent.
- product density of a random sample: definitional or something to prove? ::@:: Definitional in both directions, since a product density is independence read the other way round.
- for components of a jointly normal vector, does a zero cross-covariance imply independence? ::@:: Yes, and it is the one direction that is not definitional: the zero block splits the covariance matrix, the density factorizes, and a factorized density is independence.
- outside the normal family, does a zero covariance imply independence? ::@:: No, a zero covariance and a dependence can sit together.

<!-- check: ignore-next-line[section_example_heading]: a matched pair of cases for the definition, kept together so the counterexample sits beside the definition it violates -->
### examples and counterexamples for the product form

Independent copies $X_1 \sim N(0, 1)$ and $X_2 \sim N(0, 4)$ leave the product intact while failing on identical distribution. Independence holds, so the joint density is a product, $f_{X_1}(x_1) f_{X_2}(x_2)$. What it is not is $n$ copies of a single $f_X$, and the single $\theta$ the whole sample shares is gone. A product on its own is therefore not enough to make a random sample.

A bivariate normal pair with covariance matrix $I_2$ is the case where a zero cross-covariance does force the split. Both off-diagonal entries vanish, which makes the components independent, and the density splits into the product of the two marginals.

Outside the normal family the same covariance buys nothing. Take $U \sim \text{Unif}(-1, 1)$ and $V = U^2$. Symmetry about zero gives $\operatorname{E}[U] = \operatorname{E}[U^3] = 0$, so $\operatorname{Cov}(U, V) = \operatorname{E}[U^3] - \operatorname{E}[U]\operatorname{E}[U^2] = 0$, yet $V$ is determined by $U$ and the two are dependent.

---

Flashcards for this section are as follows:

- independent pair with $\operatorname{Var}(X_1) = 1$ and $\operatorname{Var}(X_2) = 4$: random sample or not ::@:: No, independence holds but the two copies have different laws, so they are not identically distributed.
- bivariate normal pair with covariance matrix $I_2$: does a zero cross-covariance force the joint density to split? ::@:: Yes, both off-diagonal entries are zero, so the components are independent and the density factorizes into the two marginals.
- $U \sim \text{Unif}(-1, 1)$ and $V = U^2$ outside the normal family: does a zero covariance force the joint density to split? ::@:: No, $\operatorname{Cov}(U, V) = 0$ because $\operatorname{E}[U^3] = \operatorname{E}[U] = 0$, but $V$ is determined by $U$, so the copies are dependent.
