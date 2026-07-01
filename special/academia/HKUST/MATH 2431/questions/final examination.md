---
aliases:
    - HKUST MATH 2431 final examination
    - HKUST MATH2431 final examination
    - MATH 2431 final examination
    - MATH2431 final examination
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/final_examination
    - language/in/English
---

# final examination

- HKUST MATH 2431

This page summarizes the written questions from the official final examination materials in paraphrased study-note form.

## multiple choice (questions 1–5)

> Suppose $X$ is a random variable on $(\Omega,\mathcal F,P)$ with values in $\Omega_X=\{-1,0,1\}$, $\mathbb E[X]=0$, and $\mathrm{Var}[X]=1$. How many choices are there for $P_X$, the distribution of $X$ on $(\{-1,0,1\},\mathcal P(\{-1,0,1\}))$?
>
> Solution: $P_X$ is {@{uniquely determined by $p_X(-1)=p$, $p_X(0)=q$, $p_X(1)=1-p-q$}@}. The constraints {@{$\mathbb E[X]=1-2p-q=0$}@} and {@{$\mathrm{Var}[X]=\mathbb E[X^2]=1-q=1$}@} give {@{$q=0$, $p=1/2$}@}. Hence {@{exactly one, $P_X=U(\{-1,1\})$}@}.

<!-- markdownlint MD028 -->
> Let $Y$ have CDF $F_Y(a)=0$ for $a<1$, $F_Y(a)=1-1/a^3$ for $a\ge1$. Find $\mathbb E[Y]$.
>
> Solution: Differentiate to get {@{$f_Y(a)=\frac{3}{a^4}\mathbf 1_{(1,\infty)}(a)$}@}; then {@{$\mathbb E[Y]=\int_1^\infty\frac{3}{a^3}\,da=3/2$}@}.

<!-- markdownlint MD028 -->
> Let $X_1,X_2$ be bounded and independent real random variables with MGFs $\psi_{X_1},\psi_{X_2}$. What is the MGF of $X_1-X_2$ at $t\in\mathbb R$?
>
> Solution: {@{$\psi_{X_1-X_2}(t)=\mathbb E[e^{tX_1-tX_2}]=\mathbb E[e^{tX_1}]\mathbb E[e^{-tX_2}]$}@} {@{${}=\psi_{X_1}(t)\psi_{X_2}(-t)$}@}.

<!-- markdownlint MD028 -->

> Which of the following statements is __not__ true?
>
> Solution: (E) is false. Take {@{$X\sim\mathrm{Pois}(1)+1$}@} and {@{$Y$ with density $f_Y(y)=\frac1{2y^3}\mathbf 1_{[1,\infty)}(y)$}@}; then $\mathbb E[Y]<\infty$ and $\psi_X(t)<\infty$ for all $t$, but {@{$\mathbb E[Y^X]=\infty$}@}.

<!-- markdownlint MD028 -->
> Let $(X_n)_{n\in\mathbb N}$ be i.i.d. with $\mathbb E[X_1^2]<\infty$ and $\mathbb E[X_1]=1$. Define $Y_n=X_n$ for $n$ even, $Y_n=2X_n$ for $n$ odd, and $S_n=\sum_{i=1}^nY_i$. Which limit holds?
>
> Solution: $S_n/n$ splits into even/odd terms. By SLLN, {@{$S_n/n\xrightarrow{\text{a.s.}}3/2$}@}.

## true/false (questions 6–10)

> (True/False) For a medical test with sensitivity $98\%$ and specificity $98\%$, the positive predictive value $P[A\mid P]$ is always at least $1/2$.
>
> Solution: False. By Bayes' theorem, {@{$P[A\mid P]=\frac{0.98P[A]}{0.98P[A]+0.02(1-P[A])}$}@}, which {@{approaches $0$ as $P[A]\to0$}@}.

<!-- markdownlint MD028 -->
> (True/False) For $X,Y$ with finite second moment and $\|Z\|=\sqrt{\mathbb E[Z^2]}$, we have $\|X+Y\|\le\|X\|+\|Y\|$.
>
> Solution: True. This is the triangle inequality for the $L^2$ norm, which follows from {@{Cauchy-Schwarz: $\mathbb E[(X+Y)^2]\le(\|X\|+\|Y\|)^2$}@}.

<!-- markdownlint MD028 -->
> (True/False) For $(X_n)_{n\in\mathbb N}$ i.i.d. with values in $[1,2026]$, let $Z_n=\frac{X_1+\cdots+X_n}{X_1^4+\cdots+X_n^4}$. Then $Z_n$ converges $P$-a.s. to a constant.
>
> Solution: True. $Z_n=\frac{\frac1n\sum X_i}{\frac1n\sum X_i^4}\xrightarrow{\text{a.s.}}$ {@{$\mathbb E[X_1]/\mathbb E[X_1^4]$}@}.

<!-- markdownlint MD028 -->
> (True/False) For real-valued $X,Y,U,V$, if $F_{X,Y}(x,x)=F_{U,V}(x,x)$ for all $x\in\mathbb R$, then $(X,Y)\overset{d}{=}(U,V)$.
>
> Solution: False. Take {@{$X=Y\sim U([0,1])$}@} and {@{$U,V$ i.i.d. with $F_U(x)=\sqrt x$ on $[0,1)$}@}; then diagonal CDFs match but {@{the joint laws differ}@}.

<!-- markdownlint MD028 -->
> (True/False) For independent $X,Y$ with values in $[1,2026]$, $\mathbb E[X/Y]=\mathbb E[X]/\mathbb E[Y]$.
>
> Solution: False. $\mathbb E[X/Y]=\mathbb E[X]\mathbb E[1/Y]$, and {@{$\mathbb E[1/Y]\neq1/\mathbb E[Y]$ in general}@}. Counterexample: $X=1$, $Y\sim U([1,2])$ gives $\mathbb E[X/Y]=\log2\neq2/3$.

## long-form (questions 11–14)

> - (a) Let $X$ be a real-valued random variable with expectation $\mu\in\mathbb R$ and variance $\sigma^2\ge0$. Show that for all $a\in\mathbb R$: $\mathbb E[(X-a)^2]\ge\sigma^2$. Is the maximum attained for some $a\in\mathbb R$?
> - (b) Prove that if $\mathrm{Var}[Y]=0$ for $Y$ with finite second moment, then there exists $y\in\mathbb R$ with $P[Y=y]=1$.
> - (c) Let $Z$ be a non-negative integer-valued random variable with $0<\mathbb E[Z^2]<\infty$. Show that $$\frac{\mathbb E[Z]^2}{\mathbb E[Z^2]}\le P[Z>0]\le\mathbb E[Z].$$
> - (d) Find a distribution $Q$ on $(\mathbb R,\mathcal B(\mathbb R))$ such that for $W\sim Q$, $\mathbb E[|\log W|]<\infty$ but $\mathbb E[|W|]=\infty$.
>
> Solution:
>
> - (a) $f(a)=\mathbb E[(X-a)^2]=\mathbb E[X^2]-2a\mathbb E[X]+a^2$ is minimized at {@{$a=\mathbb E[X]$}@}, giving {@{$f(\mathbb E[X])=\sigma^2$}@}, and {@{the maximum is not attained}@} since $f(a)\to\infty$ as $|a|\to\infty$.
> - (b) By Chebyshev, $P[|Y-\mathbb E[Y]|>\varepsilon]\le0$ for any $\varepsilon>0$. A union bound over $\varepsilon=1/M$ gives {@{$\bigcap_{M\ge1}\{|Y-\mathbb E[Y]|\le1/M\}$ has probability $1$}@}, so $Y=\mathbb E[Y]$ a.s.
> - (c) For the left inequality, {@{use Cauchy-Schwarz: $\mathbb E[Z]=\mathbb E[Z\mathbf 1_{\{Z>0\}}]\le\sqrt{\mathbb E[Z^2]}\sqrt{P[Z>0]}$}@}. For the right, {@{Markov: $P[Z>0]=P[Z\ge1]\le\mathbb E[Z]$}@}.
> - (d) Take density $f(w)=\frac1{w^2}\mathbf 1_{[1,\infty)}(w)$. Then {@{$\mathbb E[W]=\int_1^\infty w\cdot\frac1{w^2}\,dw=\infty$}@} but {@{$\mathbb E[|\log W|]=\int_1^\infty\frac{\log w}{w^2}\,dw<\infty$}@} (since $\log w\le\sqrt w$).

<!-- markdownlint MD028 -->
> - (a) Let $X,Y\overset{\text{i.i.d.}}{\sim}\mathcal E(\lambda)$ (exponential with rate $\lambda>0$). Define $U=\frac{X}{X+Y}$ and $V=X+Y$. Find $f_U$, $f_V$, $F_V$, and the joint density $f_{U,V}$.
> - (b) Consider an electric system where either $(A\text{ and }B)$ or $(C\text{ and }D)$ must work. The lifetimes $T_A,T_B,T_C,T_D\overset{\text{i.i.d.}}{\sim}\mathcal E(\lambda)$. Find the CDF of the system lifetime.
>
> Solution:
>
> - (a) {@{$U\sim U([0,1])$}@}, so $f_U(u)=\mathbf 1_{[0,1]}(u)$. {@{$V\sim\mathrm{Gamma}(2,\lambda)$}@} with density $f_V(v)=\lambda^2 v e^{-\lambda v}\mathbf 1_{[0,\infty)}(v)$. Integrating, $F_V(v)=\int_0^v\lambda^2 te^{-\lambda t}\,dt=$ {@{$1-e^{-\lambda v}-\lambda v e^{-\lambda v}$}@}. $U$ and $V$ are independent, with joint density {@{$f_{U,V}(u,v)=\mathbf 1_{[0,1]}(u)\lambda^2 v e^{-\lambda v}\mathbf 1_{[0,\infty)}(v)$}@}.
> - (b) The system fails at $T=\max\{\min\{T_A,T_B\},\min\{T_C,T_D\}\}$. Since {@{$\min\{T_A,T_B\}\sim\mathcal E(2\lambda)$}@}, $P[\min\{T_A,T_B\}\le t]=1-e^{-2\lambda t}$, and the two minima are independent, so $F_T(t)=$ {@{$(1-e^{-2\lambda t})^2\mathbf 1_{[0,\infty)}(t)$}@}.

<!-- markdownlint MD028 -->
> - (a) Let $(\xi_i)_{i\in\mathbb N}$ be i.i.d. with $\xi_1\sim U(\{-1,1\})$ and $S_n=\sum_{i=1}^n\xi_i$. Compute $\mathbb E[S_{n+1}\mid S_n]$, $\mathbb E[S_{n+1}^2\mid S_n]$, and $\mathbb E[e^{\lambda S_{n+1}}\mid S_n]$ for $\lambda\in\mathbb R$, $n\ge1$.
> - (b) Roll a fair die to obtain $N\sim U(\{1,\dots,6\})$, then independently flip a fair coin $N$ times. What is the expected number of heads?
> - (c) Using $\mathrm{Var}[X]=\mathbb E[\mathrm{Var}[X\mid Y]]+\mathrm{Var}[\mathbb E[X\mid Y]]$, compute the variance of the number of heads from (b).
>
> Solution:
>
> - (a) Write $S_{n+1}=S_n+\xi_{n+1}$. Since {@{$\xi_{n+1}$ is independent of $S_n$ with $\mathbb E[\xi_{n+1}]=0$}@}, {@{$\mathbb E[S_{n+1}\mid S_n]=S_n$}@}. For the square, $\mathbb E[S_{n+1}^2\mid S_n]=S_n^2+2S_n\mathbb E[\xi_{n+1}\mid S_n]+\mathbb E[\xi_{n+1}^2\mid S_n]$ = {@{$S_n^2+1$}@}. For the MGF, $\mathbb E[e^{\lambda S_{n+1}}\mid S_n]=e^{\lambda S_n}\mathbb E[e^{\lambda\xi_{n+1}}]$ = {@{$\cosh(\lambda)e^{\lambda S_n}$}@}.
> - (b) Number of heads $S=\sum_{i=1}^N X_i$ where $X_i\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(1/2)$. Then $\mathbb E[S\mid N]=N/2$, so {@{$\mathbb E[S]=\mathbb E[N/2]=7/4$}@}.
> - (c) $\mathrm{Var}[S\mid N]=N/4$, so $\mathbb E[\mathrm{Var}[S\mid N]]=\mathbb E[N/4]=7/8$. Also $\mathrm{Var}[\mathbb E[S\mid N]]=\mathrm{Var}[N/2]=\frac{35}{12\cdot4}=35/48$. Hence {@{$\mathrm{Var}[S]=7/8+35/48=77/48$}@}.

<!-- markdownlint MD028 -->
> - (a) Consider $(X_n)_{n\ge1}$ with $P[X_n=0]=1-1/n^2$, $P[X_n=n^\alpha]=1/n^2$ for $\alpha>0$.
>   - Define convergence in probability and almost sure convergence.
>   - Does $X_n\xrightarrow{P}0$?
>   - For which $r>0$ does $\mathbb E[X_n^r]\to0$?
>   - Does $X_n\to0$ almost surely?
> - (b) Let $(U_n)_{n\ge1}$ be i.i.d. $U([0,1])$. For $0<a<b$, compute $$\lim_{n\to\infty}P\left[(U_1\cdots U_n)^{n^{-1/2}}e^{n^{1/2}}\in[a,b]\right].$$
>
> Solution:
>
> - (a) Convergence in probability: $Z_n\xrightarrow{P}Z$ iff $\forall\varepsilon>0:\lim_{n\to\infty}P[|Z_n-Z|>\varepsilon]=0$. Almost sure: iff $P[\lim_{n\to\infty}Z_n=Z]=1$. For any $\varepsilon>0$, eventually $n^\alpha>\varepsilon$, so $P[|X_n|>\varepsilon]=1/n^2\to0$, hence {@{$X_n\xrightarrow{P}0$}@}. $\mathbb E[X_n^r]=n^{\alpha r-2}$. This tends to $0$ iff {@{$\alpha r-2<0$, i.e., $r<2/\alpha$}@}. $\sum_{n=1}^\infty P[|X_n|>1/M]\le\sum1/n^2<\infty$, so by {@{Borel-Cantelli, $X_n\to0$ a.s.}@}.
> - (b) Let {@{$X_i=-\log U_i\sim\mathcal E(1)$}@}, so $\mathbb E[X_i]=1$, $\mathrm{Var}[X_i]=1$. Then $(U_1\cdots U_n)^{n^{-1/2}}e^{n^{1/2}}\in[a,b]$ is equivalent to {@{$\frac1{\sqrt n}\sum_{i=1}^n(X_i-1)\in[-\log b,-\log a]$}@}. By CLT, $\frac1{\sqrt n}\sum_{i=1}^n(X_i-1)\xrightarrow{d}\mathcal N(0,1)$, so the limit is {@{$\Phi(-\log a)-\Phi(-\log b)$}@}.
