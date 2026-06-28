---
aliases:
  - HKUST MATH 2431 AGENTS
  - MATH 2431 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/AGENTS
  - language/in/English
---

# MATH 2431 agent instructions

General academic-note conventions (flashcard markup, solution structure, blockquote formatting, question-page layout) are in [academic-notes SKILL.md](../../../../.agents/skills/academic-notes/SKILL.md). This file covers only MATH 2431-specific guidance.

Honors course: when adding, editing, or removing notes here, think carefully, thoroughly, and rigorously about the probability theory; include clear arguments and derivations (not just statements) where appropriate, and feel free to add more high-quality flashcards than in non-honors courses.

## files

Do NOT include source files in this `AGENTS.md` file!

- `conditional expectation.md`: Comprehensive note on conditional expectation, sigma-algebras, and related probability concepts
- `convergence and limit theorems.md`: Modes of convergence, limit theorems (WLLN, SLLN, CLT), continuous mapping, Slutsky's theorem
- `expectation and variance.md`: Expectation (discrete, continuous, tail formulas, LOTUS, linearity), variance, covariance, correlation, Markov/Chebyshev/Jensen/Hölder/Cantelli inequalities
- `generating function.md`: Moment generating functions, characteristic functions, probability generating functions, Chernoff bounds
- `independence.md`: Stochastic independence, conditional independence, independent sigma-algebras, criteria, pairwise vs mutual independence
- `joint distribution.md`: Joint distributions, PMFs, densities, marginals, expectation of functions of random vectors, convolution, ratio distribution, product distribution, order statistics & extremes, joint MGF, covariance & correlation, multivariate normal distribution, triangle law & Buffon's needle
- `questions/**/*.md`: Questions, problem sets, and examinations

## Course-specific conventions

- **Convergence in distribution**: Use $\xrightarrow{d}$ (not $\Rightarrow$).
- **Ordinal suffixes**: Use `$x$-th` pattern (hyphen between math and text), e.g. `$n$-th` not `$n$th`.
- **Probability LaTeX**: Use `\operatorname{Bin}`, `\operatorname{Cau}`, `\operatorname{Exp}`, `\operatorname{Poi}` etc. for distribution names; `\mathbf 1` for indicator functions; `\binom{n}{k}` for binomial coefficients; `\lim_{y\uparrow m}` and `\lim_{y\downarrow m}` for left/right limits of CDFs; `\begin{cases}` with `[2pt]` spacing for piecewise definitions; `\xrightarrow{d}` for convergence in distribution; `\exp\!(` for tight spacing before parentheses in exponential functions.
- **Explicit initial-condition specification for recursive processes**: When defining $X_n=\alpha X_{n-1}+\sigma Z_n$, give $X_0$'s full distribution (e.g. $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$) — not just "$X_0$ independent of $\{Z_n\}$."

## Validator

```bash
uv run .agents/skills/academic-notes/check.py \
  "special/academia/HKUST/MATH 2431/conditional expectation.md" \
  "special/academia/HKUST/MATH 2431/convergence and limit theorems.md" \
  "special/academia/HKUST/MATH 2431/expectation and variance.md" \
  "special/academia/HKUST/MATH 2431/generating function.md" \
  "special/academia/HKUST/MATH 2431/independence.md" \
  "special/academia/HKUST/MATH 2431/joint distribution.md" \
  "special/academia/HKUST/MATH 2431/questions/mentimeter.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 5.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 7.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 10.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 11.md"
```

Fix all errors before committing.

## Common proof techniques

- sup constructions ($\alpha = \sup A$ with $A = \{x: F(x) < 1/2\}$).
- Monotone sequence arguments ($\alpha_n \uparrow \alpha$) to exploit right-continuity.
- Right-continuity contradictions when left-limit shows a discontinuity.
- Two-direction set inclusions for equality proofs.
- Explicit sequence picking for limit-based arguments.
- **Induction for $\chi^2$ density**: For $V=\sum_{i=1}^n Z_i^2$ with iid $Z_i\sim N(0,1)$, verify the $\chi^2_n$ density $f_{V_n}(v)=v^{n/2-1}e^{-v/2}/(\Gamma(n/2)2^{n/2})$ by induction on $n$. Base case $n=1$ uses the CDF of $Z^2$ and $\Gamma(1/2)=\sqrt\pi$. Inductive step convolves the $n$ and $1$ degree-of-freedom densities; $B(n/2,1/2)=\Gamma(n/2)\Gamma(1/2)/\Gamma((n+1)/2)$ resolves the integral.
- **Induction for AR(1) stationarity**: For $X_n=\alpha X_{n-1}+\sigma Z_n$ with $|\alpha|<1$ and $Z_n\sim N(0,1)$ iid, show $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ implies every $X_n$ has the same distribution — the variance fixed point. Hence strictly stationary.
- **Inverse-transform equivalence**: $F^{-1}(u)\le x \iff u\le F(x)$ where $F^{-1}(u)=\sup\{y:F(y)<u\}$. ($\Rightarrow$) uses sup definition + right-continuity; ($\Leftarrow$) uses contrapositive-style monotonicity. Pattern generalises to any generalised-inverse construction.

## Common mathematical techniques

- Gamma moment derivation: $E[X^k] = \Gamma(\alpha+k)/(\Gamma(\alpha)\lambda^k)$, using $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$.
- Beta-function identification: $\int_0^1 t^{a-1}(1-t)^{b-1}dt = B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$.
- Tail-sum expectation: $E[X]=\sum_{n\ge1}P(X\ge n)$ (discrete), $E[X]=\int_0^\infty(1-F(x))dx$ (continuous), via Tonelli/Fubini.
- **Zero-expectation sandwich for nonnegative variables**: For $X\ge0$ a.s. with $E[X]=0$, $A_n=\{X\ge1/n\}$ gives $0=E[X]\ge\frac1nP(A_n)$, so $P(A_n)=0$; by continuity from below $P(X>0)=0$, hence $X=0$ a.s. Also Markov's inequality at $\varepsilon=1/n$.
- Hazard-rate ODE: $\lambda(t)=f(t)/(1-F(t)) = -\frac{d}{dt}\log(1-F(t))$ → $F(t)=1-\exp\bigl(-\int_0^t\lambda(s)ds\bigr)$.
- Ratio comparison for discrete max arg: $a_{n+1}/a_n$ to find the peak (birthday-problem style).
- **Binomial MGF for transformed expectations**: When $Y\sim\operatorname{Bin}(n,p)$, $E[g(Y)]=\sum_{k=0}^n g(k)\binom{n}{k}p^k(1-p)^{n-k}$. Recognise $(1+p)^n$ as $E[e^{tY}]$ at $t=\log(g(1)/g(0))$ when $g$ is exponential.
- **Chernoff bound optimisation chain**: (1) $M_X(t)=E[e^{tX}]$, (2) $P(X\ge a)\le e^{-ta}M_X(t)$ for $t>0$, (3) minimise exponent over $t>0$. For Gaussians: $P(X\ge a)\le e^{-a^2/2}$.
- **Swap sum order for double-series**: $\sum_{k}\sum_{j<k}$ → $\sum_j\sum_{k>j}$ to make inner sum geometric.
- **LOTUS with trigonometric parametrisation**: For $\Theta\sim\operatorname{Unif}(-\pi/2,\pi/2)$, $E[g(\Theta)]=\frac1\pi\int g(\theta)d\theta$ with symmetry or substitution.
- **Mixed partial derivative test for joint CDFs**: Candidate $F:\mathbb R^2\to[0,1]$ must satisfy (i) limits, (ii) right-continuity, (iii) $\Delta F(a,c;b,d)\ge0$ for all $a\le b,c\le d$. Start by checking $\partial^2 F/\partial x\partial y\ge0$.
- **Renewal argument for waiting-time/run problems**: For $n$ consecutive heads, $E[X_1]=1/p$, then $E[X_n]=E[X_{n-1}]+1+(1-p)E[X_n]$, giving $pE[X_n]=E[X_{n-1}]+1$. Unwinding: $E[X_n]=\sum_{k=1}^n p^{-k}$.
- **Bernoulli thinning**: $X\sim\operatorname{Bin}(n,\phi)$, $Y\mid X\sim\operatorname{Bin}(X,\delta)$ ⇒ $Y\sim\operatorname{Bin}(n,\phi\delta)$. For $E[X\mid Y]$, decompose into per-robot indicators, compute $E[X_i\mid Y_i]$ via posterior, aggregate by linearity.
- **Exponential kernel recognition**: To marginalise $f_{X,Y}(x,y)=g(x,y)e^{-h(y)}$, recognise $\frac1y e^{-x/y}$ as $\operatorname{Exp}(1/y)$ kernel so $x$-integral $=1$ and $f_Y(y)=e^{-y}$ up to normalisation.
- **Gamma substitution for Poisson-Exp**: $N\sim\operatorname{Poisson}(\lambda)$, $\lambda\sim\operatorname{Exp}(\mu)$ ⇒ $P(N=n)=\mu/(1+\mu)^{n+1}$ (geometric at $0$), via $\int_0^\infty\lambda^n e^{-(1+\mu)\lambda}d\lambda$ and $t=(1+\mu)\lambda$.
- **Jacobian for 2D transformations**: $(Z,V)\mapsto(T,V)$ where $T=Z/\sqrt{V/n}$, inverse $(t,v)\mapsto(z,v)=(t\sqrt{v/n},\,v)$, $|\det J|=\sqrt{v/n}$, $f_{T,V}(t,v)=f_{Z,V}(z(t,v),v)\,|\det J|$.
- **CDF method for joint densities**: Alternative to Jacobian: $F_{T,V}(t,v)=P(T\le t,V\le v)$, condition on $V$, differentiate w.r.t. both arguments.
- **$1+x\le e^x$ for Bernoulli MGF**: $E[e^{tX_i}]=1+p_i(e^t-1)\le\exp(p_i(e^t-1))$ → standard Chernoff exponent.
- **Independence-disproof template**: $\operatorname{Cov}=0$ via bilinearity, then find explicit event pair where joint probability fails to factor — often at $(0,0)$ for sums and differences of symmetric variables.
- **Spectral theorem for multivariate normal**: $\Sigma=Q\Lambda Q^\top$, standardise via $z=\Lambda^{-1/2}Q^\top(x-\mu)$, quadratic form collapses to $z^\top z$, Jacobian $=(\det\Sigma)^{1/2}$.
- **Conditional expectation contrast (continuous vs discrete)**: Same workflow in both regimes: marginal → conditional distribution → expectation.
- **Random powers via MGF trick**: $Z=X^Y$, condition on $X$: $E[X^Y\mid X]=M_Y(\log X)$. Then $E[Z]=E_X[M_Y(\log X)]$.
- **Explicit $\sigma$-algebra for finite $\Omega$**: $\sigma(Y)$ consists of all unions of level sets $\{\omega:Y(\omega)=c\}$, plus $\emptyset,\Omega$. List atoms before computing conditional expectations.
- **Split-sum bound for log-denominator**: $\sum_{m=2}^n m/\log m$, split at $\lfloor\sqrt n\rfloor$: $\log m\ge\log2$ for $m\le\sqrt n$, $\log m\ge\frac12\log n$ for $m>\sqrt n$. Total $O(n^2/\log n)$.
- **Direct contradiction for disproving a.s. convergence**: Show $X_n/n\not\to0$ a.s. via BC2, then assume $\frac1n\sum X_i\to c$ a.s., giving $X_n/n\to0$ a.s. by Cesàro algebra, contradiction.
- **Non-monotonic transformation (two-branch formula)**: For $Y=g(X)$ with non-monotonic $g$, write preimage as disjoint intervals. For even $g(x)=x^n$: $F_Y(y)=F_X(y^{1/n})-F_X(-y^{1/n})$, $f_Y(y)=\frac1n y^{1/n-1}(f_X(y^{1/n})+f_X(-y^{1/n}))$.
- **Discrete iid probability patterns**: For iid $X,Y$ with PMF $p$: $P(\min\ge m)=P(X\ge m)^2$; $P(X=Y)=\sum_n p(n)^2$; $P(X>Y)=\frac12(1-P(X=Y))$.
- **Indicator expansion for inclusion-exclusion**: $\mathbf1_{\bigcup A_j}=1-\prod(1-\mathbf1_{A_j})$, expand, take expectations. Algebraic identity on indicators before any probability.
- **Rademacher counterexample**: $X\equiv0$, $Y$ Rademacher ($\pm1$ equally likely). $E[X]=E[Y]$ but $P(X=Y)=0$.
