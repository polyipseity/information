---
aliases:
    - HKUST MATH 2431 week 13 tutorial
    - HKUST MATH2431 week 13 tutorial
    - MATH 2431 week 13 tutorial
    - MATH2431 week 13 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_13_tutorial
    - language/in/English
---

# week 13 tutorial

- HKUST MATH 2431

The questions on this page combine T1B tutorial session problems with supplementary examples from solution notes for week 13. The emphasis is on maxima, covariance, correlation, explicit joint PMFs, and the supplementary topics of AM-GM via Jensen, Minkowski via Hölder, and conditional expectation orthogonality.

- topics: maxima of iid variables; covariance and correlation; zero covariance versus independence; joint PMFs; AM-GM via Jensen; Minkowski via Hölder; conditional expectation orthogonality

> Let $X_1,\dots,X_n$ be iid with Fréchet CDF $$F(x)=\exp\!\left(-\left(\frac{x}{\beta}\right)^{-\alpha}\right)\mathbf 1_{[0,\infty)}(x).$$ Find the law of $\max\{X_1,\dots,X_n\}$.
>
> Solution: {@{Independence}@} gives {@{$$P(\max_i X_i\le x)=\prod_{i=1}^n P(X_i\le x)=F(x)^n.$$}@} Hence {@{$$P(\max_i X_i\le x)=\exp\!\left(-n\left(\frac{x}{\beta}\right)^{-\alpha}\right)\mathbf 1_{[0,\infty)}(x),$$}@} so the maximum is again {@{Fréchet with the same shape parameter and rescaled scale parameter}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $X\sim U([0,a])$. Compute $\operatorname{Cov}(X,X^2)$ and the correlation coefficient $\rho(X,X^2)$.
>
> Solution: For $X\sim U([0,a])$, {@{the $k$-th moment is $E[X^k]=a^k/(k+1)$}@}. Hence {@{$E[X]=a/2$, $E[X^2]=a^2/3$, $E[X^3]=a^3/4$, and $E[X^4]=a^4/5$}@}. Therefore {@{$$\operatorname{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=\frac{a^3}{4}-\frac{a}{2}\cdot\frac{a^2}{3}= \frac{a^3}{12}.$$}@} Compute {@{the variances from these moments}@}: {@{$$\operatorname{Var}(X)=E[X^2]-E[X]^2=\frac{a^2}{3}-\frac{a^2}{4}= \frac{a^2}{12},$$}@} {@{$$\operatorname{Var}(X^2)=E[X^4]-E[X^2]^2=\frac{a^4}{5}-\frac{a^4}{9}= \frac{4a^4}{45}.$$}@} Hence {@{$$\rho(X,X^2)=\frac{a^3/12}{\sqrt{(a^2/12)(4a^4/45)}}=\frac{\sqrt{15}}{4}.$$}@} <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $X,Y\sim \mathrm{Ber}(p)$ be independent. Show that $\operatorname{Cov}(X+Y,X-Y)=0$, but $X+Y$ and $X-Y$ are not independent.
>
> Solution: {@{Bilinearity}@} gives {@{$$\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)=0.$$}@} However, zero covariance {@{does not imply independence}@}. For an explicit counterexample, note that {@{$X+Y=0$ forces $X=Y=0$}@}, while {@{$X-Y=-1$ forces $X=0,\,Y=1$}@}; these cannot {@{happen simultaneously, so $P(X+Y=0,\,X-Y=-1)=0$}@}. But {@{$P(X+Y=0)=(1-p)^2>0$ and $P(X-Y=-1)=p(1-p)>0$ for $0<p<1$}@}, so {@{the product of the marginals is positive while the joint probability is zero}@}. Thus {@{uncorrelated does not imply independent}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Roll a fair die twice. Let $S=X_1+X_2$ and $M=\max\{X_1,X_2\}$. Describe the joint PMF of $(S,M)$.
>
> Solution: {@{The support}@} is determined by {@{$1\le M\le 6$ and $M+1\le S\le 2M$}@}. If {@{$S=2M$}@}, then {@{only $(M,M)$ contributes, so the probability is $1/36$}@}. If {@{$M<S<2M$}@}, then {@{exactly two ordered outcomes contribute, so the probability is $2/36$}@}. {@{Outside this support}@} {@{the probability is $0$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

---

<!-- Source: Solution of Tutorial Notes 10 (Supplementary Examples) -->

> - (a) Let $n\ge 1$ and $a_1,\dots,a_n>0$. Use Jensen's inequality (with $-\log x$ convex) to prove $$\frac{a_1+\cdots+a_n}{n}\ge (a_1a_2\cdots a_n)^{1/n}.$$ Determine when equality holds.
> - (b) Let $A$ be a real symmetric positive definite $n\times n$ matrix. Prove $$\frac{1}{n}\operatorname{tr}(A)\ge (\det A)^{1/n}.$$ Determine when equality holds.
>
> Solution:
>
> - (a) Let $X$ be {@{uniformly distributed on $\{a_1,\dots,a_n\}$}@}. Then {@{$E[X]=\frac{1}{n}\sum a_i$ and $E[-\log X]=-\frac{1}{n}\sum\log a_i=-\log(\prod a_i)^{1/n}$}@}. Since {@{$-\log$ is convex, Jensen gives $-\log E[X]\le E[-\log X]$}@}, i.e. {@{$$-\log\!\left(\frac{1}{n}\sum a_i\right)\le -\frac{1}{n}\sum\log a_i.$$}@} {@{Exponentiating}@} yields {@{the AM–GM inequality}@}. Equality holds {@{if all $a_i$ are equal}@}.
> - (b) {@{Diagonalize $A=UDU^\top$}@} where {@{$D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$}@} and {@{$\lambda_i>0$ since $A$ is positive definite}@}. Then {@{$\operatorname{tr}(A)=\sum_{i=1}^n\lambda_i$}@} and {@{$\det A=\prod_{i=1}^n\lambda_i$}@}. Apply {@{part (a) to the eigenvalues $\lambda_1,\dots,\lambda_n$}@}: {@{$$\frac{1}{n}\sum_{i=1}^n\lambda_i\ge\Bigl(\prod_{i=1}^n\lambda_i\Bigr)^{\!1/n},$$}@} i.e. {@{$\dfrac{1}{n}\operatorname{tr}(A)\ge(\det A)^{1/n}$}@}. Equality holds {@{iff all eigenvalues are equal, i.e. $A=cI$ for some $c>0$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Use Hölder's inequality to prove Minkowski's inequality: for $1\le p<\infty$ and $f,g\in L^p(\mathbb R)$, $$\|f+g\|_p\le\|f\|_p+\|g\|_p.$$
>
> Solution: The intuition is that {@{Minkowski's inequality resembles the triangle inequality for norms}@}; to {@{prove it using Hölder}@}, we need to turn {@{$\|f+g\|_p$ into a product so that Hölder applies}@}. Write {@{$|f+g|^p = |f+g|\cdot|f+g|^{p-1}$ and bound $|f+g|\le|f|+|g|$ pointwise (triangle inequality)}@}. Then {@{Hölder with exponents $p$ and $q=p/(p-1)$}@} handles each term.
>
> Concretely: {@{$$\int|f+g|^p\le\int|f||f+g|^{p-1}+\int|g||f+g|^{p-1}.$$}@} Let {@{$q=p/(p-1)$ so that $1/p+1/q=1$}@}. Apply {@{Hölder's inequality with exponents $p,q$ to each term}@}: {@{$$\int|f||f+g|^{p-1}\le\Bigl(\int|f|^p\Bigr)^{\!1/p}\Bigl(\int|f+g|^{(p-1)q}\Bigr)^{\!1/q} =\|f\|_p\Bigl(\int|f+g|^p\Bigr)^{\!1/q},$$ and similarly for $g$}@}. Therefore {@{$$\int|f+g|^p\le\bigl(\|f\|_p+\|g\|_p\bigr)\Bigl(\int|f+g|^p\Bigr)^{\!1/q}.$$}@} {@{Dividing by $(\int|f+g|^p)^{1/q}>0$}@} gives {@{$$\Bigl(\int|f+g|^p\Bigr)^{1-1/q}\le\|f\|_p+\|g\|_p.$$}@} Since {@{$1-1/q=1/p$}@}, we obtain {@{$\bigl(\int|f+g|^p\bigr)^{1/p}\le\|f\|_p+\|g\|_p$, i.e. $\|f+g\|_p\le\|f\|_p+\|g\|_p$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Suppose $X$ and $Y$ are jointly continuous. Prove that the conditional expectation $E[Y\mid X]$ satisfies $$E[\,E[Y\mid X]\,g(X)]=E[Y g(X)],$$ for any function $g$ for which both expectations exist.
>
> Solution: By {@{definition, $E[Y\mid X]$ is $\sigma(X)$-measurable}@}. Since $g(X)$ is {@{also $\sigma(X)$-measurable, it factors out of the conditional expectation}@}: {@{$E[Y\mid X]\,g(X)=E[Y g(X)\mid X]$}@}. Hence {@{$$E[E[Y\mid X]\,g(X)]=E[E[Y g(X)\mid X]].$$}@} By {@{the law of iterated expectations, the outer expectation collapses the inner one}@}, giving {@{$E[Y g(X)]$}@}. Thus {@{$$E[E[Y\mid X]\,g(X)]=E[Y g(X)],$$}@} which is {@{the orthogonality property}@}: {@{the residual $Y-E[Y\mid X]$ is uncorrelated with any function of $X$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
