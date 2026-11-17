---
aliases:
    - HKUST MATH 2431 problem set 8
    - HKUST MATH2431 problem set 8
    - MATH 2431 problem set 8
    - MATH2431 problem set 8
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_8
    - language/in/English
---

# problem set 8

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 8.

- topics: joint distributions; independence; Bertrand's paradox; convolution; Student-$t$ distribution.

> 1.i. Joint distribution and independence. Let $A\subseteq\mathbb R^2$ be the closed triangle with vertices $(0,0)$, $(0,1)$, and $(1,0)$, and let $(X,Y)\sim U(A)$ (uniform on $A$). Find the normalizing constant $c$. Why is this called a uniform distribution?
>
> ---
>
> - solution: {@{The normalizing constant is $c=1/|A|=2$, and the name is justified because $P[(X,Y)\in B]=|A\cap B|/|A|$ for any Borel set $B$}@}
> - explanation: The triangle $A$ has {@{area $1/2$}@}, so {@{the normalizing constant is $c=1/|A|=2$}@}. The name "uniform" is justified because {@{$P[(X,Y)\in B]=|A\cap B|/|A|$ for any Borel set $B$}@}, so {@{probability is proportional to area}@}.

<!-- markdownlint MD028 -->

> 1.ii. Joint distribution and independence. Let $A\subseteq\mathbb R^2$ be the closed triangle with vertices $(0,0)$, $(0,1)$, and $(1,0)$, and let $(X,Y)\sim U(A)$ (uniform on $A$). Compute the marginal densities $f_X$, $f_Y$.
>
> ---
>
> - solution: {@{The marginals are $f_X(x)=\int_0^{1-x}2\,dy=2(1-x)\mathbf 1_{[0,1]}(x)$ and $f_Y(y)=2(1-y)\mathbf 1_{[0,1]}(y)$}@}
> - explanation: {@{Marginalizing the constant density $f=2$ along each section of the triangle gives $f_X(x)=\int_0^{1-x}2\,dy=2(1-x)\mathbf 1_{[0,1]}(x)$ and $f_Y(y)=2(1-y)\mathbf 1_{[0,1]}(y)$.}@}

<!-- markdownlint MD028 -->

> 1.iii. Joint distribution and independence. Let $A\subseteq\mathbb R^2$ be the closed triangle with vertices $(0,0)$, $(0,1)$, and $(1,0)$, and let $(X,Y)\sim U(A)$ (uniform on $A$). Are $X$ and $Y$ independent? Give a precise mathematical argument.
>
> ---
>
> - solution: {@{They are not independent}@}
> - explanation: {@{The joint density fails to factor, since $f_{X,Y}(x,y)\neq f_X(x)f_Y(y)$, because the support $x+y\le1$ is not a product set.}@}

<!-- markdownlint MD028 -->

> 1.iv. Joint distribution and independence. Let $A\subseteq\mathbb R^2$ be the closed triangle with vertices $(0,0)$, $(0,1)$, and $(1,0)$, and let $(X,Y)\sim U(A)$ (uniform on $A$). Compute $\operatorname{Cov}(X,Y)$.
>
> ---
>
> - solution: {@{The covariance is $\operatorname{Cov}(X,Y)=-1/36$}@}
> - explanation: {@{The moments are $E[X]=E[Y]=1/3$ and $E[XY]=\iint_{x+y\le1}2xy\,dx\,dy=1/12$, so the covariance is $\operatorname{Cov}(X,Y)=1/12-(1/3)^2=-1/36$.}@}

<!-- markdownlint MD028 -->

> 1.v. Joint distribution and independence. Let $X,Y\sim N(0,1)$ be independent and define $Z=\operatorname{sign}(Y)X$. Determine the law of $Z$.
>
> ---
>
> - solution: {@{The law is $Z\sim N(0,1)$}@}
> - explanation: {@{By the law of total probability, $$F_Z(z)=\frac12P(X\le z\mid Y>0)+\frac12P(-X\le z\mid Y\le0)=\frac12\Phi(z)+\frac12\Phi(z)=\Phi(z),$$ since $X$ is independent of $Y$ and $-X\sim N(0,1)$ by symmetry of the normal, so the law is $Z\sim N(0,1)$.}@} <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 1.vi. Joint distribution and independence. Let $X,Y\sim N(0,1)$ be independent and define $Z=\operatorname{sign}(Y)X$. Compute $P(X+Z=0)$. Is $W=X+Z$ discrete, continuous, or neither?
>
> ---
>
> - solution: {@{The probability is $P(X+Z=0)=1/2$, and $W=X+Z$ is neither discrete nor continuous}@}
> - explanation: {@{The event $X+Z=0$ rewrites as $\operatorname{sign}(Y)X=-X$}@}, so {@{the probability is $P(X+Z=0)=P(Y<0)=1/2$}@}. $W=X+Z$ has {@{an atom at $0$ yet also attains uncountably many values (all of $\mathbb R$ when $Y>0$)}@}, so it is {@{neither purely discrete nor purely continuous}@}.

<!-- markdownlint MD028 -->

> 1.vii. Joint distribution and independence. Let $X,Y\sim N(0,1)$ be independent and define $Z=\operatorname{sign}(Y)X$. Are $X$ and $Z$ independent? Give a precise mathematical explanation.
>
> ---
>
> - solution: {@{They are not independent}@}
> - explanation: {@{$X$ and $Z$ are not independent, since for example $P(X\in[-1,1],\,Z\ge2)=0$ while $P(X\in[-1,1])P(Z\ge2)>0$.}@}

<!-- markdownlint MD028 -->

> 2.a. Bertrand's paradox. Compute the probability that a random chord is longer than a side of the inscribed equilateral triangle using the random-endpoints model.
>
> ---
>
> - solution: {@{The probability is $1/3$}@}
> - explanation: Endpoint model: fix {@{one endpoint at angle $0$}@}; by {@{rotational symmetry the chord length depends only on the angular separation $\theta$}@}. The chord is {@{longer than the triangle side precisely when $60^\circ<\theta<120^\circ$}@} (i.e. after normalizing to full turns, {@{$\theta$ mod $1\in(1/3,2/3)$}@}), giving {@{the probability $\frac{120^\circ-60^\circ}{180^\circ}=1/3$}@}.

<!-- markdownlint MD028 -->

> 2.b. Bertrand's paradox. Compute the probability that a random chord is longer than a side of the inscribed equilateral triangle using the random-radius model.
>
> ---
>
> - solution: {@{The probability is $1/2$}@}
> - explanation: Radius model: {@{a chord at distance $d$ from the center}@} has {@{length $2\sqrt{r^2-d^2}$}@}. It is {@{longer than the triangle side (length $\sqrt3\,r$)}@} iff {@{the condition $2\sqrt{r^2-d^2}>\sqrt3\,r$, i.e. $d<r/2$}@}. The midpoint is {@{chosen uniformly on the radius}@}, so {@{the probability is $P(d<r/2)=(r/2)/r=1/2$}@}.

<!-- markdownlint MD028 -->

> 2.c. Bertrand's paradox. Compute the probability that a random chord is longer than a side of the inscribed equilateral triangle using the random-midpoint model.
>
> ---
>
> - solution: {@{The probability is $1/4$}@}
> - explanation: Midpoint model: the chord is {@{longer than the side iff the midpoint lies inside the concentric circle of radius $r/2$}@}, which gives {@{the area fraction $(\pi(r/2)^2)/(\pi r^2)=1/4$}@}.

<!-- markdownlint MD028 -->

> 2.d. Bertrand's paradox. Explain why the answers differ.
>
> ---
>
> - solution: {@{The answers differ because "random chord" names no unique probability law}@}
> - explanation: {@{The phrase "random chord" does not specify a unique probability law, so different sampling schemes produce different answers.}@} <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.i. Convolution. Let $X\sim N(\mu_1,\sigma_1^2)$ and $Y\sim N(\mu_2,\sigma_2^2)$ be independent. Show that $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.
>
> ---
>
> - solution: {@{The sum is $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$}@}
> - explanation: Using {@{moment generating functions}@}, {@{the product is $\psi_{X+Y}(t)=\psi_X(t)\psi_Y(t)=\exp(\mu_1 t+\sigma_1^2 t^2/2)\exp(\mu_2 t+\sigma_2^2 t^2/2)=\exp((\mu_1+\mu_2)t+(\sigma_1^2+\sigma_2^2)t^2/2)$}@}, which is {@{the moment generating function of $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$}@}, so $X+Y$ is {@{normal with addition of means and variances}@}.

<!-- markdownlint MD028 -->

> 3.ii. Convolution. Let $X_1,\dots,X_n$ be i.i.d. $N(\mu,\sigma^2)$ and let $\bar X_n=\frac1n\sum_{i=1}^n X_i$. Determine the law of $Z_n=\sqrt n\,(\bar X_n-\mu)/\sigma$.
>
> ---
>
> - solution: {@{The law is $Z_n\sim N(0,1)$ for every $n$}@}
> - explanation: {@{For iid $X_i\sim N(\mu,\sigma^2)$, $$\sum_{i=1}^n X_i\sim N(n\mu,n\sigma^2)\quad\Longrightarrow\quad\bar X_n=\frac1n\sum X_i\sim N(\mu,\sigma^2/n).$$ Hence the standardized mean $Z_n=\sqrt n\,(\bar X_n-\mu)/\sigma$ is $N(0,1)$ for every $n$.}@}

<!-- markdownlint MD028 -->

> 3.iii. Convolution. Let $X\sim\operatorname{Pois}(\lambda)$ and $Y\sim\operatorname{Pois}(\mu)$ be independent. Show that $X+Y\sim\operatorname{Pois}(\lambda+\mu)$.
>
> ---
>
> - solution: {@{The sum is $X+Y\sim\operatorname{Pois}(\lambda+\mu)$}@}
> - explanation: {@{Using moment generating functions, the product is $\psi_{X+Y}(t)=\psi_X(t)\psi_Y(t)=\exp(\lambda(e^t-1))\exp(\mu(e^t-1))=\exp((\lambda+\mu)(e^t-1))$, which is the moment generating function of $\operatorname{Pois}(\lambda+\mu)$, so independent Poisson variables add to $\operatorname{Pois}(\lambda+\mu)$.}@}

<!-- markdownlint MD028 -->

> 3.iv. Convolution. Give a concrete counterexample showing that $X+Y$ does not generally follow a Poisson distribution when independence is dropped.
>
> ---
>
> - solution: {@{With $Y=X\sim\operatorname{Pois}(\lambda)$, the sum $X+Y=2X$ is not Poisson}@}
> - explanation: Without {@{independence this can fail}@}: for {@{the degenerate choice $Y=X\sim\operatorname{Pois}(\lambda)$}@}, {@{$X+Y=2X$ only takes even values}@}, so $2X$ {@{cannot be Poisson (for a Poisson variable $P(\cdot=1)>0$, but $P(2X=1)=0$)}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4.a. The Student-$t$ distribution. Let $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}N(0,1)$ and $V=\sum_{i=1}^n Z_i^2$, and recall the gamma function $\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du$ for $\alpha>0$. Show that $V$ has probability density $f_V(x)=c_n x^{n/2-1}e^{-x/2}\mathbf 1_{[0,\infty)}(x)$, with an appropriate constant $c_n\in\mathbb R$.
>
> ---
>
> - solution: {@{The density holds with $c_n=1/(\Gamma(n/2)2^{n/2})$}@}
> - explanation: The density is {@{verified by induction on $n$}@}. <br/>
>     __Base case $n=1$:__ For $Z\sim N(0,1)$, the CDF of {@{$Y=Z^2$ is $F_Y(y)=P(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$}@}; differentiating gives {@{the density $$f_Y(y)=\frac d{dy}F_Y(y)=\frac1{\sqrt{2\pi}}y^{-1/2}e^{-y/2},\qquad y>0,$$}@} which is {@{the claimed density with $c_1=1/\sqrt{2\pi}=1/(\Gamma(1/2)2^{1/2})$, since $\Gamma(1/2)=\sqrt\pi$}@}. <br/>
>     __Inductive step:__ {@{the density of $V_n\sim\chi^2_n$ is $$f_{V_n}(v)=\frac{v^{n/2-1}e^{-v/2}}{\Gamma(n/2)2^{n/2}},\qquad v>0.$$}@} <br/>
>     For {@{$V_{n+1}=V_n+Z_{n+1}^2$ with $Z_{n+1}^2$ independent of $V_n$}@}, convolution gives {@{the density $$f_{V_{n+1}}(v)=\int_0^v f_{V_n}(u)\,f_{Z^2}(v-u)\,du =\int_0^v \frac{u^{n/2-1}e^{-u/2}}{\Gamma(n/2)2^{n/2}}\cdot\frac{(v-u)^{-1/2}e^{-(v-u)/2}}{\sqrt{2\pi}}\,du.$$}@} <br/>
>     Factoring {@{$e^{-v/2}$ out of the integral}@} gives {@{the value $$f_{V_{n+1}}(v)=\frac{e^{-v/2}}{\Gamma(n/2)2^{n/2}\sqrt{2\pi}}\int_0^v u^{n/2-1}(v-u)^{-1/2}\,du.$$}@} Substituting {@{the change of variable $u=vt$ with $du=v\,dt$}@} turns it into {@{the density $$f_{V_{n+1}}(v)=\frac{e^{-v/2}v^{(n+1)/2-1}}{\Gamma(n/2)2^{n/2}\sqrt{2\pi}}\int_0^1 t^{n/2-1}(1-t)^{-1/2}\,dt.$$}@} <br/>
>     The remaining integral is {@{the Beta function}@}: {@{the value $$B\!\left(\frac n2,\frac12\right)=\frac{\Gamma(n/2)\Gamma(1/2)}{\Gamma((n+1)/2)}=\frac{\Gamma(n/2)\sqrt\pi}{\Gamma((n+1)/2)}.$$}@} Substituting it back reduces the formula to {@{the value $$f_{V_{n+1}}(v)=\frac{e^{-v/2}v^{(n+1)/2-1}}{\Gamma(n/2)2^{n/2}\sqrt{2\pi}}\cdot\frac{\Gamma(n/2)\sqrt\pi}{\Gamma((n+1)/2)}=\frac{v^{(n+1)/2-1}e^{-v/2}}{\Gamma((n+1)/2)2^{(n+1)/2}},$$}@} which is {@{exactly the $\chi^2_{n+1}$ density}@}. <br/>
>     By induction the formula {@{holds for all $n\ge1$, with $c_n=1/(\Gamma(n/2)2^{n/2})$}@}.

<!-- markdownlint MD028 -->

> 4.b. The Student-$t$ distribution. Let $V=\sum_{i=1}^n Z_i^2$ for $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}N(0,1)$, and let $T=Z/\sqrt{V/n}$ with $Z\sim N(0,1)$ independent of $V$. Find the joint density of $(T,V)$, starting from the joint CDF $F_{T,V}(t,v)$.
>
> ---
>
> - solution: {@{The joint density is $f_{T,V}(t,v)=f_Z\bigl(t\sqrt{v/n}\bigr)\,f_V(v)\,\sqrt{v/n}$}@}
> - explanation: Consider {@{the $2$-dimensional transformation $(Z,V)\mapsto(T,V)$ where $T=Z/\sqrt{V/n}$}@}. {@{The inverse transformation}@} is {@{the map $$(t,v)\longmapsto\bigl(z(t,v),\,v(t,v)\bigr)=\bigl(t\sqrt{v/n},\,v\bigr).$$}@} <br/>
>     {@{The Jacobian matrix of the inverse transformation and its determinant}@} are {@{the pair $$J=\begin{pmatrix}\partial z/\partial t&\partial z/\partial v\\\partial v/\partial t&\partial v/\partial v\end{pmatrix}=\begin{pmatrix}\sqrt{v/n}&t/(2\sqrt{nv})\\0&1\end{pmatrix},\qquad|\det J|=\sqrt{v/n}.$$}@} By {@{the $n$-dimensional change-of-variables formula (here $n=2$)}@}, {@{the joint density is $$f_{T,V}(t,v)=f_{Z,V}\bigl(z(t,v),v\bigr)\,|\det J|=f_Z\bigl(t\sqrt{v/n}\bigr)\,f_V(v)\,\sqrt{v/n},$$}@} where {@{the last equality uses independence of $Z$ and $V$}@}. <br/>
>     __Alternative (CDF method, per hint):__ Starting from {@{the joint CDF}@}, {@{the value $$F_{T,V}(t,v)=P(T\le t,\;V\le v)=P\!\left(\frac{Z}{\sqrt{V/n}}\le t,\;V\le v\right)=\int_0^v P\!\left(Z\le t\sqrt{u/n}\right)f_V(u)\,du=\int_0^v \Phi\!\left(t\sqrt{u/n}\right)f_V(u)\,du,$$}@} where the second equality {@{conditions on $V=u$ and uses independence of $Z$ and $V$}@}. {@{Differentiating with respect to $t$ and $v$}@} gives {@{the density $$f_{T,V}(t,v)=\frac{\partial}{\partial v}\left[\int_0^v f_Z\!\left(t\sqrt{u/n}\right)\sqrt{u/n}\,f_V(u)\,du\right]=f_Z\!\left(t\sqrt{v/n}\right)\sqrt{v/n}\,f_V(v),$$}@} which {@{agrees with the Jacobian result}@}.

<!-- markdownlint MD028 -->

> 4.c. The Student-$t$ distribution. Let $V=\sum_{i=1}^n Z_i^2$ for $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}N(0,1)$, let $T=Z/\sqrt{V/n}$ with $Z\sim N(0,1)$ independent of $V$, and recall the densities $f_Z(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2}$ and $f_V(v)=\frac{v^{n/2-1}e^{-v/2}}{\Gamma(n/2)2^{n/2}}$ for $v>0$. Compute the density of $T$ by marginalization.
>
> ---
>
> - solution: {@{The density is $f_T(t)=\frac{\Gamma((n+1)/2)}{\sqrt{n\pi}\,\Gamma(n/2)}\left(1+\frac{t^2}{n}\right)^{-(n+1)/2}$}@}
> - explanation: Substituting {@{the pair $f_Z(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2}$ and $f_V(v)=\frac{v^{n/2-1}e^{-v/2}}{\Gamma(n/2)2^{n/2}}$ into the joint density}@} and integrating gives {@{the density $$f_T(t)=\int_0^\infty\frac1{\sqrt{2\pi}}e^{-t^2v/(2n)}\sqrt{\frac{v}{n}}\frac{v^{n/2-1}e^{-v/2}}{\Gamma(n/2)2^{n/2}}\,dv=\frac{1}{\sqrt{2\pi n}\,\Gamma(n/2)2^{n/2}}\int_0^\infty v^{(n-1)/2}e^{-v(1+t^2/n)/2}\,dv.$$}@} <br/> <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-17T00:00:00.000Z,292,292.05080696,1,2,3,0,0,2026-08-29T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-23T00:00:00.000Z,297,296.59855496,1,2,3,0,0,2026-08-30T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-17T00:00:00.000Z,292,292.05080696,1,2,3,0,0,2026-08-29T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-23T00:00:00.000Z,297,296.59855496,1,2,3,0,0,2026-08-30T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->
>     Set {@{$u=v(1+t^2/n)/2$, so $dv=2/(1+t^2/n)\,du$}@}, and the integral becomes {@{the value $\int_0^\infty u^{(n+1)/2-1}e^{-u}\,du$}@}. Recall {@{the gamma function definition}@}, so the integral equals {@{the value $\Gamma((n+1)/2)\bigl(2/(1+t^2/n)\bigr)^{(n+1)/2}$}@}. <br/>
>     Simplifying yields {@{the density $f_T(t)=\frac{\Gamma((n+1)/2)}{\sqrt{n\pi}\,\Gamma(n/2)}\left(1+\frac{t^2}{n}\right)^{-(n+1)/2}$}@}.
