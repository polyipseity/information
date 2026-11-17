---
aliases:
    - HKUST MATH 2431 problem set 9
    - HKUST MATH2431 problem set 9
    - MATH 2431 problem set 9
    - MATH2431 problem set 9
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_9
    - language/in/English
---

# problem set 9

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 9.

- topics: covariance and correlation; autoregressive processes; Jensen's inequality; Chernoff bounds.

> 1.a. Covariance and correlation. Let $X\sim U([0,a])$. Determine $\operatorname{Cov}(X,X^2)$ and the correlation coefficient $\rho(X,X^2)$.
>
> ---
>
> - solution: {@{$\operatorname{Cov}(X,X^2)=a^3/12$ and $\rho(X,X^2)=\sqrt{15}/4$}@}
> - explanation: For {@{$X\sim U([0,a])$, the moments follow from the constant density $f(x)=1/a$}@}, giving {@{the moments $E[X^k]=a^k/(k+1)$}@}, so {@{the values are $E[X]=a/2$, $E[X^2]=a^2/3$, $E[X^3]=a^3/4$ and $E[X^4]=a^4/5$}@}. Thus {@{the covariance is $\operatorname{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=a^3/4-(a/2)(a^2/3)=a^3/12$}@}. Next {@{the variances are $\operatorname{Var}(X)=a^2/12$ and $\operatorname{Var}(X^2)=E[X^4]-E[X^2]^2=a^4/5-a^4/9=4a^4/45$}@}, so {@{the correlation is $\rho=\frac{a^3/12}{\sqrt{a^2/12\cdot4a^4/45}}=\sqrt{15}/4$}@}.

<!-- markdownlint MD028 -->

> 1.b. Covariance and correlation. Roll a fair die twice with outcomes $X_1,X_2$. Define $S=X_1+X_2$ and $M=\max\{X_1,X_2\}$. Calculate $\operatorname{Cov}(S,M)$ and describe the joint PMF.
>
> ---
>
> - solution: {@{The covariance is $\operatorname{Cov}(S,M)=35/12>0$, with joint PMF $P(M=m,S=2m)=1/36$ on the diagonal and $P(M=m,S=s)=2/36$ for $m+1\le s\le 2m-1$}@}
> - explanation: {@{The joint PMF comes first}@}: for {@{$(M,S)=(m,2m)$ (diagonal, both dice $m$)}@} the probability is {@{the value $1/36$}@}; for {@{$(M,S)=(m,s)$ with $m+1\le s\le 2m-1$ (off-diagonal, one die $m$, the other $s-m\neq m$)}@} it is {@{the value $2/36$}@}. <br/>
>     For the moments, {@{the marginal is $P(M=m)=(\frac m6)^2-(\frac{m-1}6)^2=\frac{2m-1}{36}$}@}, so {@{the mean is $E[M]=\sum_{m=1}^6 m\frac{2m-1}{36}=\frac{161}{36}$}@}, while {@{the mean $E[S]=7$}@} follows by {@{symmetry of two dice}@}. <br/>
>     Summing {@{$E[SM]$ over the support}@} gives {@{the product moment $E[SM]=\frac1{36}\sum_{m=1}^6\bigl[m(2m)+\sum_{s=m+1}^{2m-1}2ms\bigr]=\frac1{36}\sum_{m=1}^6(3m^3-m^2)=\frac1{36}(3\cdot441-91)=\frac{1232}{36}$}@}, hence {@{the covariance $\operatorname{Cov}(S,M)=E[SM]-E[S]E[M]=\frac{1232}{36}-7\cdot\frac{161}{36}=\frac{105}{36}=\frac{35}{12}>0$}@}.

<!-- markdownlint MD028 -->

> 1.c. Covariance and correlation. Let $X,Y\sim \mathrm{Ber}(p)$ be independent. Show that $\operatorname{Cov}(X+Y,X-Y)=0$, but $X+Y$ and $X-Y$ are not independent.
>
> ---
>
> - solution: {@{The covariance is $\operatorname{Cov}(X+Y,X-Y)=0$, yet $X+Y$ and $X-Y$ are not independent}@}
> - explanation: Computing directly gives {@{the covariance $\operatorname{Cov}(X+Y,X-Y)=\operatorname{Cov}(X,X)-\operatorname{Cov}(X,Y)+\operatorname{Cov}(Y,X)-\operatorname{Cov}(Y,Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)=0$}@}. Despite being {@{uncorrelated, they are dependent}@}: {@{the value $P(X+Y=0,X-Y=0)=P(X=0,Y=0)=(1-p)^2$}@} while {@{the product $P(X+Y=0)P(X-Y=0)=(1-p)^2\cdot(p^2+(1-p)^2)$}@}, and these {@{differ, so the joint law fails to factor}@}, a classic {@{counterexample that uncorrelated does not imply independence}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-23T00:00:00.000Z,297,296.59855496,1,2,3,0,0,2026-08-30T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Decay of covariances in an autoregressive process. Let $|\alpha|<1$ and define $X_n=\alpha X_{n-1}+\sigma Z_n$ for $n\ge 1$, with $Z_n\sim N(0,1)$ iid and $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$. If $X_{n-1}\sim N(m,v)$, show that $X_n\sim N(\alpha m,\alpha^2v+\sigma^2)$.
>
> ---
>
> - solution: {@{The law is $X_n\sim N(\alpha m,\alpha^2v+\sigma^2)$}@}
> - explanation: {@{The value $X_n=\alpha X_{n-1}+\sigma Z_n$ is a linear combination of independent normals, hence normal with $E[X_n]=\alpha m$ and $\operatorname{Var}(X_n)=\alpha^2v+\sigma^2$.}@}

<!-- markdownlint MD028 -->

> 2.b. Decay of covariances in an autoregressive process. Let $|\alpha|<1$ and define $X_n=\alpha X_{n-1}+\sigma Z_n$ for $n\ge 1$, with $Z_n\sim N(0,1)$ iid and $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$. Show that $N\!\left(0,\sigma^2/(1-\alpha^2)\right)$ is stationary.
>
> ---
>
> - solution: {@{The law $N\left(0,\sigma^2/(1-\alpha^2)\right)$ is stationary}@}
> - explanation: Assume {@{the law $X_{n-1}\sim N(0,\sigma^2/(1-\alpha^2))$}@}. Then {@{the update gives $$X_n\sim N(0,\;\alpha^2\cdot\sigma^2/(1-\alpha^2)+\sigma^2)=N(0,\;\sigma^2(\alpha^2/(1-\alpha^2)+1)) \,.$$}@} Simplifying {@{the variance $\sigma^2\frac{\alpha^2+(1-\alpha^2)}{1-\alpha^2}$}@} gives {@{the value $\frac{\sigma^2}{1-\alpha^2}$}@}. Hence $X_n$ has {@{the same distribution as $X_{n-1}$}@}. Since $X_0$ is {@{defined with this distribution}@}, {@{induction gives $X_n\sim N(0,\sigma^2/(1-\alpha^2))$ for all $n$}@}, so {@{the process is stationary}@}.

<!-- markdownlint MD028 -->

> 2.c. Decay of covariances in an autoregressive process. Let $|\alpha|<1$ and define $X_n=\alpha X_{n-1}+\sigma Z_n$ for $n\ge 1$, with $Z_n\sim N(0,1)$ iid and $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$. Assuming stationarity, prove that $\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\sigma^2/(1-\alpha^2)$.
>
> ---
>
> - solution: {@{The covariance is $\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\sigma^2/(1-\alpha^2)$}@}
> - explanation: {@{Expanding $X_n=\alpha^k X_{n-k}+\sigma\sum_{j=0}^{k-1}\alpha^j Z_{n-j}$ makes the noise terms independent of $X_{n-k}$, so the covariance is $\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\operatorname{Var}(X_{n-k})$, and stationarity gives $\operatorname{Var}(X_{n-k})=\sigma^2/(1-\alpha^2)$.}@} <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Applications of Jensen's inequality. Prove the finite weighted Jensen inequality: for convex $\varphi$ and weights $\lambda_i>0$ with $\sum_i\lambda_i=1$, $$\varphi(\sum_i\lambda_i x_i)\le\sum_i\lambda_i\varphi(x_i) \,.$$
>
> ---
>
> - solution: {@{The weighted inequality $\varphi\left(\sum_i\lambda_i x_i\right)\le\sum_i\lambda_i\varphi(x_i)$ holds}@}
> - explanation: {@{Define a discrete $Y$ with $P(Y=x_i)=\lambda_i$; then Jensen's inequality for expectations gives $\varphi(E[Y])\le E[\varphi(Y)]$, which is precisely the weighted inequality.}@}

<!-- markdownlint MD028 -->

> 3.b. Applications of Jensen's inequality. Deduce the arithmetic mean-geometric mean inequality: for $x_i\ge0$ and $\sum_i\lambda_i=1$, $$(\prod_i x_i^{\lambda_i})^{1/\sum_i\lambda_i}\le\sum_i\lambda_i x_i \,,$$ i.e. the weighted AM–GM bound; the special case $\lambda_i=1/n$ gives $(\prod_{i=1}^n x_i)^{1/n}\le\frac1n\sum_{i=1}^n x_i$.
>
> ---
>
> - solution: {@{The bound $(\prod_i x_i^{\lambda_i})^{1/\sum_i\lambda_i}\le\sum_i\lambda_i x_i$ holds}@}
> - explanation: {@{Since $\log$ is concave, $\log(\sum_i\lambda_i x_i)\ge\sum_i\lambda_i\log x_i$, and exponentiating gives $\sum_i\lambda_i x_i\ge\prod_i x_i^{\lambda_i}$, which is the weighted AM–GM bound.}@}

<!-- markdownlint MD028 -->

> 3.c. Applications of Jensen's inequality. Show that $E[X]\le (E[X^2])^{1/2}\le (E[X^3])^{1/3}\le\cdots$ for $X\ge 0$.
>
> ---
>
> - solution: {@{The chain $E[X]\le (E[X^2])^{1/2}\le (E[X^3])^{1/3}\le\cdots$ holds}@}
> - explanation: {@{For $X\ge 0$ the variable $Y=X^n$ under the convex map $y\mapsto y^{(n+1)/n}$ gives $E[X^{n+1}]\ge (E[X^n])^{(n+1)/n}$, so $(E[X^{n+1}])^{1/(n+1)}\ge (E[X^n])^{1/n}$.}@} <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4\. Chernoff bounds for sums of Bernoulli variables. Let $X_1,\dots,X_n$ be independent Bernoulli variables, let $X=\sum_i X_i$, and let $\mu=E[X]$. Prove that for all $\delta>0$, $$P[X\ge (1+\delta)\mu]\le \left(\frac{e^\delta}{(1+\delta)^{1+\delta}}\right)^\mu.$$
>
> ---
>
> - solution: {@{For all $\delta>0$, $P[X\ge (1+\delta)\mu]\le \left(\frac{e^\delta}{(1+\delta)^{1+\delta}}\right)^\mu$}@}
> - explanation: For {@{any $t>0$, Markov's inequality}@} gives {@{the bound $P(X\ge(1+\delta)\mu)\le e^{-t(1+\delta)\mu}E[e^{tX}]$}@}. Since {@{the sum is $X=\sum_i X_i$}@}, {@{independence gives $E[e^{tX}]=\prod_i E[e^{tX_i}]$}@}. Bounding {@{each moment generating function by $1 + x \le e^x$}@} gives {@{the value $E[e^{tX_i}]=1+p_i(e^t-1)\le\exp(p_i(e^t-1))$}@}, hence {@{the bound $P(\dots)\le e^{-t(1+\delta)\mu}\prod_i\exp(p_i(e^t-1))=\exp(-t(1+\delta)\mu+\mu(e^t-1))$}@}, where {@{the mean is $\mu=\sum p_i$}@}. <br/> <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->
>     {@{Optimizing over $t>0$}@}: differentiating {@{the exponent $\psi(t)=-t(1+\delta)\mu+\mu(e^t-1)$}@} gives {@{$\psi'(t)=-(1+\delta)\mu+\mu e^t=0$, so $t=\log(1+\delta)$}@}. Substituting back gives {@{the bound $$P(\dots)\le\exp(\mu[-(1+\delta)\log(1+\delta)+\delta])=\bigl(\frac{e^\delta}{(1+\delta)^{1+\delta}}\bigr)^\mu,$$}@} which is {@{the Chernoff bound for Bernoulli sums}@}.
