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

> Covariance and correlation.
>
> - (a) Let $X\sim U([0,a])$. Determine $\operatorname{Cov}(X,X^2)$ and the correlation coefficient $\rho(X,X^2)$.
> - (b) Roll a fair die twice with outcomes $X_1,X_2$. Define $S=X_1+X_2$ and $M=\max\{X_1,X_2\}$. Calculate $\operatorname{Cov}(S,M)$ and describe the joint PMF.
> - (c) Let $X,Y\sim \mathrm{Ber}(p)$ be independent. Show that $\operatorname{Cov}(X+Y,X-Y)=0$, but $X+Y$ and $X-Y$ are not independent.
>
> Solution:
>
> - (a) For $X\sim U([0,a])$: the moments follow from {@{$f(x)=1/a$}@}, giving {@{$E[X^k]=a^k/(k+1)$}@}, so {@{$E[X]=a/2$, $E[X^2]=a^2/3$, $E[X^3]=a^3/4$, $E[X^4]=a^4/5$}@}. Thus {@{$\operatorname{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=a^3/4-(a/2)(a^2/3)=a^3/12$}@}. <p> Next {@{$\operatorname{Var}(X)=a^2/12$, $\operatorname{Var}(X^2)=E[X^4]-E[X^2]^2=a^4/5-a^4/9=4a^4/45$}@}, so {@{$\rho=\frac{a^3/12}{\sqrt{a^2/12\cdot4a^4/45}}=\sqrt{15}/4$}@}.
> - (b) Describe {@{the joint PMF first}@}: For {@{$(M,S)=(m,2m)$ (diagonal, both dice $m$), $P=1/36$}@}; for {@{$(M,S)=(m,s)$ with $m+1\le s\le 2m-1$ (off-diagonal, one die $m$, the other $s-m\neq m$), $P=2/36$}@}. <p>Now compute moments. {@{$P(M=m)=(\frac m6)^2-(\frac{m-1}6)^2=\frac{2m-1}{36}$}@}, so {@{$E[M]=\sum_{m=1}^6 m\frac{2m-1}{36}=\frac{161}{36}$}@}. {@{$E[S]=7$}@} by {@{symmetry of two dice}@}. For {@{$E[SM]$, sum over the support}@}: {@{$E[SM]=\frac1{36}\sum_{m=1}^6\bigl[m(2m)+\sum_{s=m+1}^{2m-1}2ms\bigr]=\frac1{36}\sum_{m=1}^6(3m^3-m^2)=\frac1{36}(3\cdot441-91)=\frac{1232}{36}$}@}. Hence {@{$\operatorname{Cov}(S,M)=E[SM]-E[S]E[M]=\frac{1232}{36}-7\cdot\frac{161}{36}=\frac{105}{36}=\frac{35}{12}>0$}@}.
> - (c) Compute directly: {@{$\operatorname{Cov}(X+Y,X-Y)=\operatorname{Cov}(X,X)-\operatorname{Cov}(X,Y)+\operatorname{Cov}(Y,X)-\operatorname{Cov}(Y,Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)=0$}@}. Despite {@{being uncorrelated, they are dependent}@}: {@{$P(X+Y=0,X-Y=0)=P(X=0,Y=0)=(1-p)^2$}@}, while {@{$P(X+Y=0)P(X-Y=0)=(1-p)^2\cdot(p^2+(1-p)^2)$}@}; these {@{differ, so the joint law fails to factor}@} — a classic {@{counterexample that uncorrelated does not imply independence}@}.

<!-- markdownlint MD028 -->

> Decay of covariances in an autoregressive process.
>
> Let $|\alpha|<1$ and define $X_n=\alpha X_{n-1}+\sigma Z_n$ for $n\ge 1$, with $Z_n\sim N(0,1)$ iid and $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$.
>
> - (a) If $X_{n-1}\sim N(m,v)$, show that $X_n\sim N(\alpha m,\alpha^2v+\sigma^2)$.
> - (b) Show that $N\!\left(0,\sigma^2/(1-\alpha^2)\right)$ is stationary.
> - (c) Assuming stationarity, prove that $\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\sigma^2/(1-\alpha^2)$.
>
> Solution:
>
> - (a) $X_n=\alpha X_{n-1}+\sigma Z_n$ is {@{a linear combination of independent normals}@}, hence {@{normal with $E[X_n]=\alpha m$ and $\operatorname{Var}(X_n)=\alpha^2 v+\sigma^2$}@}.
> - (b) Assume {@{$X_{n-1}\sim N(0,\sigma^2/(1-\alpha^2))$}@}. From part (a) with {@{$m=0$, $v=\sigma^2/(1-\alpha^2)$}@}, {@{$$X_n\sim N(0,\;\alpha^2\cdot\sigma^2/(1-\alpha^2)+\sigma^2)=N(0,\;\sigma^2(\alpha^2/(1-\alpha^2)+1)) \,.$$}@} Simplify: {@{$$\sigma^2\frac{\alpha^2+(1-\alpha^2)}{1-\alpha^2}=\frac{\sigma^2}{1-\alpha^2} \,.$$}@} Hence $X_n$ has {@{the same distribution as $X_{n-1}$}@}. Since $X_0$ is {@{defined with this distribution}@}, by {@{induction $X_n\sim N(0,\sigma^2/(1-\alpha^2))$ for all $n$}@}, so {@{the process is stationary}@}.
> - (c) Expanding {@{$X_n=\alpha^k X_{n-k}+\sigma\sum_{j=0}^{k-1}\alpha^j Z_{n-j}$}@}, the noise terms are {@{independent of $X_{n-k}$}@}. Hence {@{$\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\operatorname{Var}(X_{n-k})$}@}. Under {@{stationarity, $\operatorname{Var}(X_{n-k})=\sigma^2/(1-\alpha^2)$}@}, so {@{$\operatorname{Cov}(X_n,X_{n-k})=\alpha^k\sigma^2/(1-\alpha^2)$}@}.

<!-- markdownlint MD028 -->

> Applications of Jensen's inequality.
>
> - (a) Prove the finite weighted Jensen inequality: for convex $\varphi$ and weights $\lambda_i>0$ with $\sum_i\lambda_i=1$, $$\varphi(\sum_i\lambda_i x_i)\le\sum_i\lambda_i\varphi(x_i) \,.$$
> - (b) Deduce the arithmetic mean-geometric mean inequality: for $x_i\ge0$ and $\sum_i\lambda_i=1$, $$(\prod_i x_i^{\lambda_i})^{1/\sum_i\lambda_i}\le\sum_i\lambda_i x_i \,,$$ i.e. the weighted AM–GM bound; the special case $\lambda_i=1/n$ gives $(\prod_{i=1}^n x_i)^{1/n}\le\frac1n\sum_{i=1}^n x_i$.
> - (c) Show that $E[X]\le (E[X^2])^{1/2}\le (E[X^3])^{1/3}\le\cdots$ for $X\ge 0$.
>
> Solution:
>
> - (a) Define {@{a discrete $Y$ with $P(Y=x_i)=\lambda_i$}@}. Then {@{$\varphi(E[Y])\le E[\varphi(Y)]$ by Jensen's inequality for expectations}@}, which is {@{precisely the weighted inequality}@}.
> - (b) Since {@{$\log$ is concave}@}, {@{$\log(\sum \lambda_i x_i)\ge\sum\lambda_i\log x_i$}@}; {@{exponentiating gives $\sum\lambda_i x_i\ge\prod x_i^{\lambda_i}$}@}, which is {@{AM-GM}@}.
> - (c) For {@{$X\ge 0$, let $Y=X^n$}@}. {@{The map $y\mapsto y^{(n+1)/n}$ is convex}@} for $y\ge 0$, so {@{$E[Y^{(n+1)/n}]\ge (E[Y])^{(n+1)/n}$, i.e. $E[X^{n+1}]\ge (E[X^n])^{(n+1)/n}$}@}, so {@{$(E[X^{n+1}])^{1/(n+1)}\ge (E[X^n])^{1/n}$}@}.

<!-- markdownlint MD028 -->

> Chernoff bounds for sums of Bernoulli variables.
>
> Let $X_1,\dots,X_n$ be independent Bernoulli variables, let $X=\sum_i X_i$, and let $\mu=E[X]$. Prove that for all $\delta>0$, $$P[X\ge (1+\delta)\mu]\le \left(\frac{e^\delta}{(1+\delta)^{1+\delta}}\right)^\mu.$$
>
> Solution: For {@{any $t>0$, Markov's inequality}@} gives {@{$P(X\ge(1+\delta)\mu)\le e^{-t(1+\delta)\mu}E[e^{tX}]$}@}. Since {@{$X=\sum_i X_i$}@}, {@{independence gives $E[e^{tX}]=\prod_i E[e^{tX_i}]$}@}. Bound {@{each MGF using $1 + x \le e^x$}@}, so {@{$E[e^{tX_i}]=1+p_i(e^t-1)\le\exp(p_i(e^t-1))$}@}. Hence {@{$P(\dots)\le e^{-t(1+\delta)\mu}\prod_i\exp(p_i(e^t-1))=\exp(-t(1+\delta)\mu+\mu(e^t-1))$}@}, where {@{$\mu=\sum p_i$}@}. <p> {@{Optimize over $t>0$}@}: differentiate {@{$\psi(t)=-t(1+\delta)\mu+\mu(e^t-1)$}@}; {@{$\psi'(t)=-(1+\delta)\mu+\mu e^t=0$ gives $t=\log(1+\delta)$}@}. Substituting back: {@{$P(\dots)\le\exp(\mu[-(1+\delta)\log(1+\delta)+\delta])=\bigl(\frac{e^\delta}{(1+\delta)^{1+\delta}}\bigr)^\mu$}@}, which is {@{the Chernoff bound for Bernoulli sums}@}.
