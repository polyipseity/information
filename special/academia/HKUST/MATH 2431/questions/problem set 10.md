---
aliases:
    - HKUST MATH 2431 problem set 10
    - HKUST MATH2431 problem set 10
    - MATH 2431 problem set 10
    - MATH2431 problem set 10
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_10
    - language/in/English
---

# problem set 10

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 10.

- topics: multivariate normal distribution; conditional expectation; sigma-algebras; random powers of random variables.

> Multivariate normal distribution.
>
> Let $X=(X_1,\dots,X_d)^\top$ with density $$f(x)=\frac{1}{(2\pi)^{d/2}\sqrt{\det\Sigma}}\exp\left(-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right).$$
>
> - (a) Show that $f$ integrates to $1$.
> - (b) Show that $X_1,\dots,X_d$ are independent and normally distributed with $X_i\sim N(\mu_i,\sigma_i^2)$ if and only if $X\sim N_d(\mu,\Sigma)$, where $\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_d^2)$.
> - (c) Show that $E[X_i]=\mu_i$ and $\operatorname{Cov}(X_i,X_j)=\Sigma_{ij}$.
> - (d) Show that if $A$ has full rank and $b$ is fixed, then $AX+b$ is again multivariate normal with transformed mean and covariance.
>
> Solution:
>
> - (a) By {@{the __spectral theorem__ for symmetric positive definite matrices}@}, $\Sigma$ admits {@{an orthogonal eigendecomposition $\Sigma=Q\Lambda Q^\top$}@} where {@{$Q$ is orthogonal ($QQ^\top=I$, $\det Q=\pm1$) and $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_d)$ with eigenvalues $\lambda_i>0$}@}. Hence {@{$\det\Sigma=\prod_{i=1}^d\lambda_i$ and $\Sigma^{-1}=Q\Lambda^{-1}Q^\top$}@}. <p> Change variables to {@{$z=\Lambda^{-1/2}Q^\top(x-\mu)$ (equivalently $x=\mu+Q\Lambda^{1/2}z$)}@}. {@{The quadratic form}@} simplifies to {@{$$(x-\mu)^\top\Sigma^{-1}(x-\mu)=z^\top\Lambda^{-1/2}Q^\top Q\Lambda Q^\top Q\Lambda^{-1/2}z=z^\top z=\sum_{i=1}^d z_i^2.$$}@} The Jacobian is {@{$dx/dz=Q\Lambda^{1/2}$}@}; its absolute determinant is {@{$$|\det(Q\Lambda^{1/2})|=|\det Q|\cdot|\det\Lambda^{1/2}|=1\cdot\prod_{i=1}^d\sqrt{\lambda_i}=(\det\Sigma)^{1/2}.$$}@} <p> Therefore {@{$$\int_{\mathbb R^d}f(x)\,dx=\frac{1}{(2\pi)^{d/2}(\det\Sigma)^{1/2}}\cdot(\det\Sigma)^{1/2}\int_{\mathbb R^d}e^{-z^\top z/2}\,dz=\prod_{i=1}^d\underbrace{\int_{-\infty}^\infty\frac{e^{-z_i^2/2}}{\sqrt{2\pi}}\,dz_i}_{=1}=1,$$}@} confirming that $f$ is {@{a valid probability density}@}.
> - (b) If $\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_d^2)$, then {@{$\det\Sigma=\prod_i\sigma_i^2$ and $(x-\mu)^\top\Sigma^{-1}(x-\mu)=\sum_i (x_i-\mu_i)^2/\sigma_i^2$}@}, so {@{$$f(x)=\prod_{i=1}^d\frac{1}{\sqrt{2\pi\sigma_i^2}}\exp\!\left(-\frac{(x_i-\mu_i)^2}{2\sigma_i^2}\right)=\prod_{i=1}^d f_i(x_i),$$}@} where each $f_i$ is {@{the univariate $N(\mu_i,\sigma_i^2)$ density}@}. <p> Since {@{the joint density factors into a product of marginal densities}@}, {@{the coordinates $X_1,\dots,X_d$ are independent}@}.
> - (c) Let {@{$Z=\Sigma^{-1/2}(X-\mu)$}@}, where {@{$\Sigma^{-1/2}=Q\Lambda^{-1/2}Q^\top$}@} uses the same eigendecomposition as (a). By (a), {@{$Z\sim N(0,I)$}@}, so {@{$E[Z]=0$ and $\operatorname{Cov}(Z)=I$}@}. Transform {@{back via $X=\mu+\Sigma^{1/2}Z$ (here $\Sigma^{1/2}=Q\Lambda^{1/2}Q^\top$)}@}. Using {@{linearity of expectation and bilinearity of covariance}@}, {@{$$E[X]=\mu+\Sigma^{1/2}E[Z]=\mu,$$ $$\operatorname{Cov}(X)=E[(X-\mu)(X-\mu)^\top]=E[\Sigma^{1/2}ZZ^\top\Sigma^{1/2}]=\Sigma^{1/2}E[ZZ^\top]\Sigma^{1/2}=\Sigma^{1/2}I\Sigma^{1/2}=\Sigma.$$}@} <p> Hence {@{$E[X_i]=\mu_i$ and $\operatorname{Cov}(X_i,X_j)=\Sigma_{ij}$}@}.
> - (d) For {@{square invertible $A$}@}, {@{the change of variables $x=A^{-1}(y-b)$}@} gives {@{$dx=dy/|\det A|$ and $$f_Y(y)=\frac{1}{|\det A|}f_X(A^{-1}(y-b)).$$}@} <p> Substituting into the normal density, {@{$$f_Y(y)=\frac{1}{(2\pi)^{d/2}\sqrt{\det\Sigma}\,|\det A|}\exp\!\left(-\frac12(A^{-1}(y-b)-\mu)^\top\Sigma^{-1}(A^{-1}(y-b)-\mu)\right).$$}@} {@{Complete the square in $y$}@}: {@{$$(A^{-1}(y-b)-\mu)^\top\Sigma^{-1}(A^{-1}(y-b)-\mu)=(y-(A\mu+b))^\top(A^{-1})^\top\Sigma^{-1}A^{-1}(y-(A\mu+b))=(y-(A\mu+b))^\top(A\Sigma A^\top)^{-1}(y-(A\mu+b)).$$}@} <p> Moreover {@{$\det(A\Sigma A^\top)=(\det A)^2\det\Sigma$}@}, so {@{$|\det A|\sqrt{\det\Sigma}=\sqrt{\det(A\Sigma A^\top)}$}@}. Hence {@{$$f_Y(y)=\frac{1}{(2\pi)^{d/2}\sqrt{\det(A\Sigma A^\top)}}\exp\!\left(-\frac12(y-(A\mu+b))^\top(A\Sigma A^\top)^{-1}(y-(A\mu+b))\right),$$}@} i.e. {@{$Y\sim N(A\mu+b,\,A\Sigma A^\top)$}@}. <p> For {@{non-square $A\in\mathbb R^{p\times d}$ with full rank $p<d$}@}, extend {@{$A$ to a square $d\times d$ matrix $\tilde A$ by appending $d-p$ rows}@}, apply {@{the result to $\tilde AX+b$}@}, then {@{marginalize the extra coordinates to obtain the distribution of $AX+b$}@}.

<!-- markdownlint MD028 -->

> Conditional expectation for continuous and discrete random variables.
>
> - (a) If $f_{X,Y}(x,y)=e^{-y}\mathbf 1_{\{0\le x\le y\}}$, calculate $E[X\mid Y]$ and $E[Y\mid X]$.
> - (b) Let $r,p\in\mathbb R$ satisfy $0\le r\le p\le 1$ and $1-2p+r\ge0$. The joint distribution of $(X,Y)$ is $$P(X=1,Y=1)=r,\; P(X=0,Y=1)=p-r,\\ P(X=1,Y=0)=p-r,\; P(X=0,Y=0)=1-2p+r.$$ Determine the marginal law of $Y$ and compute $E[X\mid Y]$.
>
> Solution:
>
> - (a) {@{Marginal of $Y$}@}: {@{$$f_Y(y)=\int_0^y e^{-y}\,dx=y e^{-y}\mathbf 1_{[0,\infty)}(y).$$}@} Hence the conditional density of $X$ given $Y$ is {@{$$f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}=\frac{e^{-y}}{y e^{-y}}=\frac1y,\qquad 0\le x\le y.$$}@} Thus {@{$X\mid Y=y\sim U([0,y])$ and $E[X\mid Y]=Y/2$}@}. <p> {@{Marginal of $X$}@}: {@{$$f_X(x)=\int_x^\infty e^{-y}\,dy=e^{-x}\mathbf 1_{[0,\infty)}(x).$$}@} Hence {@{$$f_{Y\mid X}(y\mid x)=\frac{e^{-y}}{e^{-x}}=e^{-(y-x)},\qquad y\ge x,$$}@} so $Y\mid X=x$ is {@{$\text{Exp}(1)$ shifted by $x$}@}. The conditional mean: {@{$$E[Y\mid X=x]=\int_x^\infty y e^{-(y-x)}\,dy.$$}@} Substitute {@{$u=y-x$: $$E[Y\mid X=x]=\int_0^\infty (u+x)e^{-u}\,du=\underbrace{\int_0^\infty u e^{-u}\,du}_{=1}+x\underbrace{\int_0^\infty e^{-u}\,du}_{=1}=x+1,$$}@} i.e. {@{$E[Y\mid X]=X+1$}@}.
> - (b) From the given joint PMF, {@{the marginal of $Y$}@} is {@{$$\begin{aligned} P(Y=0)&=P(X=1,Y=0)+P(X=0,Y=0)=(p-r)+(1-2p+r)=1-p \,, \\ P(Y=1)&=P(X=1,Y=1)+P(X=0,Y=1)=r+(p-r)=p \,, \end{aligned}$$}@} so {@{$Y\sim\operatorname{Ber}(p)$}@}. The conditional expectations are {@{$$\begin{aligned} E[X\mid Y=0]&=0\cdot\frac{P(X=0,Y=0)}{P(Y=0)}+1\cdot\frac{P(X=1,Y=0)}{P(Y=0)}=\frac{p-r}{1-p} \,, \\ E[X\mid Y=1]&=0\cdot\frac{P(X=0,Y=1)}{P(Y=1)}+1\cdot\frac{P(X=1,Y=1)}{P(Y=1)}=\frac{r}{p} \,. \end{aligned}$$}@} Packaging the two cases gives {@{$E[X\mid Y]=\frac{p-r}{1-p}\mathbf 1_{\{Y=0\}}+\frac{r}{p}\mathbf 1_{\{Y=1\}}$}@}.

<!-- markdownlint MD028 -->

> Sigma-algebras generated by random variables.
>
> - (a) Show that $\sigma(Y)=\{Y^{-1}(B):B\in\mathcal B(\mathbb R)\}$ is a sigma-algebra and is the smallest one making $Y$ measurable.
> - (b) For discrete random variables, show that $E[Z\mid \sigma(Y)]=E[Z\mid Y]$.
> - (c) Let $(\Omega,\mathcal F,P)=(\{1,\dots,6\},\mathcal P(\{1,\dots,6\}),U(\{1,\dots,6\}))$, $Z(\omega)=\omega$, and $Y(\omega)=\mathbf 1_{\{1,3,5\}}(\omega)$. Compute $\sigma(Y)$ and $E[Z\mid Y]$.
>
> Solution:
>
> - (a) Define {@{$\sigma(Y)=\{Y^{-1}(B):B\in\mathcal B(\mathbb R)\}$}@}. To show it is {@{a $\sigma$-algebra, verify the three axioms}@}: (i) {@{$\Omega=Y^{-1}(\mathbb R)\in\sigma(Y)$ since $\mathbb R\in\mathcal B(\mathbb R)$}@}. (ii) If {@{$A=Y^{-1}(B)\in\sigma(Y)$, then $A^c=Y^{-1}(B^c)\in\sigma(Y)$}@}. (iii) If {@{$A_n=Y^{-1}(B_n)\in\sigma(Y)$, then $\bigcup_n A_n=Y^{-1}(\bigcup_n B_n)\in\sigma(Y)$}@}. Hence {@{$\sigma(Y)$ is a $\sigma$-algebra}@}. <p> Minimality: {@{any $\sigma$-algebra $\mathcal F$ that makes $Y$ measurable}@} must contain {@{$Y^{-1}(B)$ for every Borel set $B$ (by definition of measurability)}@}. Therefore {@{$\sigma(Y)\subseteq\mathcal F$}@}, so $\sigma(Y)$ is {@{indeed the smallest $\sigma$-algebra with respect to which $Y$ is measurable}@}.
> - (b) For {@{discrete $Y$ taking values $\{y_1,y_2,\dots\}$}@}, $\sigma(Y)$ is generated by {@{the partition $\{\{Y=y_1\},\{Y=y_2\},\dots\}$}@}. {@{The conditional expectation $E[Z\mid\sigma(Y)]$}@} is {@{the unique $\sigma(Y)$-measurable random variable}@} satisfying {@{$\int_A Z\,dP=\int_A E[Z\mid\sigma(Y)]\,dP$ for every $A\in\sigma(Y)$}@}. Define {@{$g(y)=E[Z\mid Y=y]$, so $E[Z\mid Y]=g(Y)$}@}, which is {@{$\sigma(Y)$-measurable}@}. It suffices to {@{check the singletons}@}. For {@{any $A=\{Y=y_k\}$}@}, {@{$\int_A Z\,dP=E[Z\mathbf1_{\{Y=y_k\}}]=g(y_k)P(Y=y_k)=\int_A g(Y)\,dP$}@}. By {@{uniqueness of conditional expectation}@}, {@{$E[Z\mid\sigma(Y)]=E[Z\mid Y]$}@}.
> - (c) Note {@{$Y=1$ on the odd outcomes $\{1,3,5\}$}@} and {@{$Y=0$ on the even outcomes $\{2,4,6\}$}@}. {@{The generated $\sigma$-algebra}@} is {@{$$\sigma(Y)=\{\emptyset,\;\{1,3,5\},\;\{2,4,6\},\;\Omega\},$$}@} which contains {@{precisely the information of whether the outcome is odd or even}@}. For $Z(\omega)=\omega$, {@{$$E[Z\mid Y=0]=E[Z\mid\{2,4,6\}]=\frac{2+4+6}{3}=4,\qquad E[Z\mid Y=1]=E[Z\mid\{1,3,5\}]=\frac{1+3+5}{3}=3.$$}@} Hence {@{$$E[Z\mid Y]=4\cdot\mathbf 1_{\{Y=0\}}+3\cdot\mathbf 1_{\{Y=1\}} \,.$$}@}

<!-- markdownlint MD028 -->

> Random powers of random variables.
>
> Let $X$ and $Y$ be independent Poisson variables with parameters $\alpha$ and $\beta$, and define $Z=X^Y$. Compute $E[Z]$.
>
> Solution:
>
> {@{Condition on $X$}@}: since {@{$Y\mid X=x\sim\text{Pois}(\beta)$}@}, {@{$$E[X^Y\mid X=x]=\sum_{k=0}^{\infty}x^k\frac{\beta^k}{k!}e^{-\beta}=e^{-\beta}\sum_{k=0}^{\infty}\frac{(\beta x)^k}{k!}=e^{-\beta}e^{\beta x}=e^{\beta(x-1)}.$$}@} {@{Averaging again over $X$}@} we obtain {@{the MGF of $X$}@}: {@{$$E[Z]=E_X\!\big[e^{\beta(X-1)}\big]=e^{-\beta}E\!\big[e^{\beta X}\big]=e^{-\beta}\cdot\exp\!\big(\alpha(e^{\beta}-1)\big),$$}@} hence {@{$E[Z]=\exp\big(\alpha(e^{\beta}-1)-\beta\big)$}@}.
