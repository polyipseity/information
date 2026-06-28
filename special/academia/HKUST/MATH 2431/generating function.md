---
aliases:
  - characteristic function
  - generating function
  - generating functions
  - moment generating function
  - probability generating function
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/generating_function
  - language/in/English
---

# generating function

Generating functions package a whole probability law into one analytic object. In this course they appear in three closely related forms: moment generating functions for moments and tail bounds, characteristic functions for uniqueness and weak convergence, and probability generating functions for integer-valued laws.

---

Flashcards for this section are as follows:

- overview ::@:: A generating function encodes a distribution by turning probabilities into a transform that is easier to differentiate, multiply, and compare.
- three types and their uses: What are the three generating functions covered and which tasks is each best suited for? ::@:: MGF: moments and exponential tail bounds; CF: uniqueness of distribution and weak convergence; PGF: integer-valued distributions and factorial moments.

## moment generating function

The MGF $M_X(t)=E[e^{tX}]$ is said to **exist** if it is finite on an open interval $(-h,h)$ containing $0$. Whenever differentiation under the expectation is justified, $M_X^{(n)}(0)=E[X^n]$, so the MGF stores all moments. In particular, $M_X'(0)=E[X]$ and $M_X''(0)=E[X^2]$.

Existence properties:

- **Moments from MGF:** $M_X^{(n)}(0)=E[X^n]$ (dominated convergence justifies differentiation on the interval).
- **MGF uniquely determines the law:** if $M_X(t)=M_Y(t)$ for all $t$ in a neighborhood of $0$, then $X$ and $Y$ have the same distribution (analytic continuation to the CF, then Lévy's inversion formula).
- **Analyticity:** $t\mapsto M_X(t)$ is infinitely differentiable and analytic on its domain; the power series $\sum_{k\ge0}E[X^k]t^k/k!$ converges to $M_X(t)$ on $(-h,h)$.
- **Affine transformation:** $M_{aX+b}(t)=e^{tb}M_X(at)$.

MGF existence near $0$ is stronger than mere finiteness of all moments. A counterexample is the lognormal distribution: $X\sim\operatorname{LogNormal}(0,1)$ has $E[X^n]=e^{n^2/2}<\infty$ for all $n$, but $E[e^{tX}]=\infty$ for all $t>0$. So theorems requiring MGF existence (Chernoff bounds, MGF uniqueness) are genuinely stronger than moment assumptions.

---

Flashcards for this section are as follows:

- moment generating function definition: For a random variable $X$, what is $M_X(t)$? ::@:: $M_X(t)=E[e^{tX}]$ for those $t$ at which the expectation is finite.
- MGF existence requirement: For the MGF $M_X(t)=E[e^{tX}]$ to give strong analytic control, what must its domain satisfy? ::@:: It must be finite on an open interval containing $0$.
- moments from MGF derivatives: If $M_X(t)=E[e^{tX}]$ and differentiation under the expectation is justified, what is $M_X^{(n)}(0)$? ::@:: $M_X^{(n)}(0)=E[X^n]$.
- MGF affine transformation: If $Y=aX+b$, what is $M_Y(t)$ in terms of $M_X$? ::@:: $M_{aX+b}(t)=e^{tb}M_X(at)$.
- MGF uniqueness statement: If $M_X(t)=M_Y(t)$ for all $t$ in a neighborhood of $0$, what can you conclude? ::@:: $X$ and $Y$ have the same distribution; the MGF uniquely determines the law on its interval of existence.
- MGF uniqueness proof idea: How does MGF uniqueness follow from CF uniqueness? ::@:: Agreement of MGFs near $0$ implies agreement of CFs after analytic continuation $t\mapsto it$; CFs determine the law uniquely by the inversion formula.
- MGF analyticity: When $M_X(t)$ exists in $(-h,h)$, what are the analytic properties of $t\mapsto M_X(t)$? ::@:: It is infinitely differentiable and analytic on its domain; in particular $M_X^{(k)}(0)=E[X^k]$ and the power series $\sum_{k\ge0}E[X^k]t^k/k!$ converges to $M_X(t)$ on $(-h,h)$.
- MGF vs all moments: How does MGF existence near $0$ compare with having all moments $E[X^n]$? ::@:: MGF existence near $0$ is stronger; it implies all moments exist and gives analytic control.
- lognormal counterexample: Give a distribution with all moments finite but no MGF near $0$. ::@:: $X\sim\operatorname{LogNormal}(0,1)$ has $E[X^n]=e^{n^2/2}<\infty$ for all $n$, but $E[e^{tX}]=\infty$ for all $t>0$ because $e^{tx}$ grows faster than any polynomial.

## relations between generating functions and uniqueness

The three generating functions are related by substitution: $M_X(it)=\varphi_X(t)$ (analytic continuation: if $M_X$ exists near $0$, then $t\mapsto M_X(it)$ is a CF on $\mathbb R$); $G_X(e^t)=M_X(t)$ for integer-valued $X\ge0$; and $\varphi_X(t)=G_X(e^{it})$ for integer-valued $X\ge0$.

Each generating function also recovers distributional information from its derivatives, and each uniquely determines the underlying law:

- **MGF:** $M_X^{(n)}(0)=E[X^n]$ recovers moments; $M_X$ uniquely determines the distribution via analytic continuation to the CF.
- **CF:** $\varphi_X$ uniquely determines the distribution via the inversion formula; $\varphi_X^{(n)}(0)=i^nE[X^n]$ when moments exist.
- **PGF:** $G_X^{(k)}(0)/k!=P[X=k]$ recovers probabilities; $G_X$ uniquely determines the distribution as coefficients of its power series.

Moreover, for each transform, the existence of the first moment has a derivative-based characterisation: for the MGF, $E[X]=M_X'(0)$ (on the interval of existence); for the CF, $E[X]=-i\varphi_X'(0)$ when $E[|X|]<\infty$; and for the PGF, $E[X]=G_X'(1)=\lim_{t\uparrow 1}G_X'(t)$.

---

Flashcards for this section are as follows:

- How are MGF, CF, and PGF related by substitution? ::@:: $M_X(it)=\varphi_X(t)$ (analytic continuation); $G_X(e^t)=M_X(t)$ and $\varphi_X(t)=G_X(e^{it})$ for integer-valued $X\ge0$.
- Similarity across MGF, CF, PGF: How does each generating function recover distributional information from its derivatives and uniquely determine the law? ::@:: MGF: $M_X^{(n)}(0)=E[X^n]$ (moments); uniquely via analytic continuation to CF. CF: $\varphi_X^{(n)}(0)=i^nE[X^n]$ (moments); uniquely via inversion formula. PGF: $G_X^{(k)}(0)/k!=P[X=k]$ (probabilities); uniquely as power-series coefficients.
- First moment from each generating function: Express $E[X]$ from the MGF, CF, and PGF in terms of their derivatives. ::@:: MGF: $E[X]=M_X'(0)$ on its interval of existence. CF: $E[X]=-i\varphi_X'(0)$ when $E[|X|]<\infty$. PGF: $E[X]=G_X'(1)=\lim_{t\uparrow 1}G_X'(t)$.

### uniqueness theorem

For each generating function, the correspondence is **bidirectional**:

$$\text{equal transforms (on the appropriate domain)}\quad\Longleftrightarrow\quad\text{equal probability laws}.$$

The forward direction ($\Longleftarrow$) is trivial: equal distributions give equal expectations. The converse is the uniqueness theorem:

- **CF (no condition needed):** Fourier inversion recovers the CDF at continuity points: $F_X(b)-F_X(a)=\frac1{2\pi}\lim_{T\to\infty}\int_{-T}^T\frac{e^{-ita}-e^{-itb}}{it}\,\varphi_X(t)\,dt$. Equal CFs $\Rightarrow$ equal right-hand sides $\Rightarrow$ equal CDFs.

- **MGF (finite near $0$):** $M_X(z)=E[e^{zX}]$ is analytic on a strip $\{z:|\operatorname{Re}z|<h\}$. Equality on $(-h,h)$ forces equality on the strip, hence on the imaginary axis where it reduces to the CF; CF uniqueness then gives $X\stackrel d=Y$.

- **PGF ($|s|\le1$):** $G_X(s)=\sum P[X=k]s^k$ is a power series. If $G_X(s)=G_Y(s)$ on $[0,1]$, the identity theorem forces equal coefficients $P[X=k]=P[Y=k]$ for all $k$.

---

Flashcards for this section are as follows:

- bidirectional equivalence: For each generating function, equal transforms (on the appropriate domain) are equivalent to what? ::@:: Equal probability laws. ($\Longleftarrow$ is trivial; $\Longrightarrow$ is the uniqueness theorem per transform.)
- uniqueness engine by transform: What is the proof engine for uniqueness of CF, MGF, and PGF? ::@:: CF: Fourier inversion (always works). MGF: analytic continuation $\to$ CF (needs existence near $0$). PGF: identity theorem for power series (coeffs are probabilities).
- CF uniqueness via Fourier inversion: How does the Fourier inversion formula prove that equal CFs imply equal distributions? ::@:: $\displaystyle F_X(b)-F_X(a)=\frac1{2\pi}\lim_{T\to\infty}\int_{-T}^T\frac{e^{-ita}-e^{-itb}}{it}\,\varphi_X(t)\,dt$; if $\varphi_X=\varphi_Y$, the right-hand sides match at all continuity points, so the CDFs are equal.
- MGF uniqueness via analytic continuation: How does MGF equality near $0$ imply equal distributions? ::@:: $M_X(z)$ is analytic on a strip $\{z:|\operatorname{Re}z|<h\}$. Equality on $(-h,h)$ extends analytically to the whole strip, including the imaginary axis where $M_X(it)=\varphi_X(t)$; CF uniqueness then gives $X\stackrel d=Y$.
- PGF uniqueness via identity theorem: How does PGF equality on $[0,1]$ imply equal distributions? ::@:: $G_X(s)=\sum P[X=k]s^k$ is a power series; if $G_X=G_Y$ on $[0,1]$, the identity theorem for analytic functions forces $P[X=k]=P[Y=k]$ for all $k$.

## convolution of independent sums through MGFs

If $X$ and $Y$ are independent, then $M_{X+Y}(t)=E[e^{t(X+Y)}]=E[e^{tX}e^{tY}]=M_X(t)M_Y(t)$.

This is the transform version of convolution: sums of independent random variables become products of MGFs.

For iid variables $X_1,\dots,X_n$ with common MGF $M_X$, one therefore has $M_{X_1+\cdots+X_n}(t)=M_X(t)^n$.

This is why MGFs prove closure properties so efficiently. For example, comparing MGFs immediately gives the addition laws for binomial, Poisson, and normal distributions.

---

Flashcards for this section are as follows:

- MGFs of independent sums: If $X$ and $Y$ are independent with MGFs $M_X$ and $M_Y$, what is $M_{X+Y}(t)$? ::@:: $M_{X+Y}(t)=M_X(t)M_Y(t)$.
- iid sum via MGFs: If $X_1,\dots,X_n$ are iid with common MGF $M_X$, what is $M_{X_1+\cdots+X_n}(t)$? ::@:: $M_{X_1+\cdots+X_n}(t)=M_X(t)^n$.
- MGF closure properties: What distributional fact can you prove by comparing MGFs? ::@:: The addition (closure) laws for sums of independent binomial, Poisson, and normal variables.

## named MGF formulas for binomial, Poisson, normal, and exponential

For the standard named laws used throughout the course:

- If $X\sim\mathrm{Bin}(n,p)$, then $M_X(t)=E[e^{tX}]=(1-p+pe^t)^n$. This is just the binomial theorem applied to $n$ Bernoulli trials.

- If $X\sim\mathrm{Pois}(\lambda)$, then $M_X(t)=\sum_{k=0}^{\infty}e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}=\exp(\lambda(e^t-1))$.

- If $X\sim N(\mu,\sigma^2)$, then completing the square gives $M_X(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right)$.

- If $X\sim E(\lambda)$, then $M_X(t)=\int_0^{\infty}\lambda e^{-\lambda x}e^{tx}\,dx=\frac{\lambda}{\lambda-t}$ for $t<\lambda$.

These formulas are the workhorses behind Chernoff bounds and limit theorems.

---

Flashcards for this section are as follows:

- binomial MGF formula: If $X\sim\mathrm{Bin}(n,p)$, what is $M_X(t)$? ::@:: $M_X(t)=(1-p+pe^t)^n$.
- Poisson MGF formula: If $X\sim\mathrm{Pois}(\lambda)$, what is $M_X(t)$? ::@:: $M_X(t)=\exp(\lambda(e^t-1))$.
- normal MGF formula: If $X\sim N(\mu,\sigma^2)$, what is $M_X(t)$? ::@:: $M_X(t)=\exp(\mu t+\sigma^2t^2/2)$.
- exponential MGF formula: If $X\sim E(\lambda)$ and $t<\lambda$, what is $M_X(t)$? ::@:: $M_X(t)=\lambda/(\lambda-t)$.
- Bernoulli MGF formula: If $X\sim\mathrm{Bern}(p)$, what is $M_X(t)$? ::@:: $M_X(t)=1-p+pe^t$.
- normal MGF derivation: What technique derives $M_X(t)=\exp(\mu t+\sigma^2t^2/2)$ for $X\sim N(\mu,\sigma^2)$? ::@:: Completing the square in the exponent of $e^{tx}$ under the normal density integral.

## characteristic function

The characteristic function $\varphi_X(t)=E[e^{itX}]$ exists for all $t\in\mathbb R$ since $|e^{itX}|=1$ guarantees finiteness, making it the universal Fourier transform of a probability law.

---

Flashcards for this section are as follows:

- characteristic function definition: For a random variable $X$, what is $\varphi_X(t)$? ::@:: $\varphi_X(t)=E[e^{itX}]$ for $t\in\mathbb R$.
- why characteristic functions always exist: Why does $|e^{itX}|=1$ guarantee that $\varphi_X(t)=E[e^{itX}]$ is always defined? ::@:: The modulus is always $1$, so the expectation is bounded and therefore exists.
- CF of independent sums: If $X$ and $Y$ are independent, what is $\varphi_{X+Y}(t)$? ::@:: $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$.
- CF uniform continuity property: What is the modulus-of-continuity property of $\varphi_X$? ::@:: $\varphi_X$ is uniformly continuous on $\mathbb R$; $|\varphi_X(t+h)-\varphi_X(t)|\le E[|e^{ihX}-1|]\to0$ as $h\to0$ by dominated convergence.
- CF boundedness: What bounds hold for $|\varphi_X(t)|$? ::@:: $|\varphi_X(t)|\le1$ for all $t$, with $\varphi_X(0)=1$.
- CF conjugate symmetry: How is $\varphi_X(-t)$ related to $\varphi_X(t)$? ::@:: $\varphi_X(-t)=\overline{\varphi_X(t)}$ because $e^{-itX}$ is the complex conjugate of $e^{itX}$.
- CF of affine transformation: If $Y=aX+b$, what is $\varphi_Y(t)$ in terms of $\varphi_X$? ::@:: $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$.
- Lévy continuity theorem (forward direction): If $X_n\xrightarrow{d}X$, what happens to the CFs? ::@:: $\varphi_{X_n}(t)\to\varphi_X(t)$ for all $t\in\mathbb R$.

Key properties:

- **Uniform continuity:** $|\varphi_X(t+h)-\varphi_X(t)|\le E[|e^{ihX}-1|]\to0$ as $h\to0$ (dominated convergence).
- **Boundedness:** $|\varphi_X(t)|\le1$ for all $t$, $\varphi_X(0)=1$.
- **Conjugate symmetry:** $\varphi_X(-t)=\overline{\varphi_X(t)}$.
- **Independent sums:** $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$, central to the CLT (Taylor-expand $\varphi_X$ and apply Lévy's continuity theorem).
- **Affine transformation:** $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$.
- **Moments (when they exist):** $\varphi_X^{(n)}(0)=i^nE[X^n]$; conversely $\varphi_X^{(n)}(0)$ finite implies $E[|X|^{n}]<\infty$ (even $n$) or $E[|X|^{n-1}]<\infty$ (odd $n$).
- **Uniqueness:** If $\varphi_X(t)=\varphi_Y(t)$ for all $t$, then $X\stackrel d=Y$ by the inversion formula.
- **Lévy's continuity theorem:** $X_n\xrightarrow{d}X$ $\Rightarrow$ $\varphi_{X_n}(t)\to\varphi_X(t)$; conversely, if $\varphi_{X_n}$ converges pointwise to $\varphi$ continuous at $0$, $X_n\xrightarrow{d}X$ for some $X$ with CF $\varphi$.

## probability generating functions for discrete distributions

If $X$ is nonnegative integer-valued, its probability generating function is $G_X(s)=E[s^X]=\sum_{k=0}^{\infty}P[X=k]s^k$ for $|s|\le 1$. This is the discrete-counting analogue of the MGF: independent sums become products $G_{X+Y}(s)=G_X(s)G_Y(s)$, and the coefficients are exactly the probabilities $P[X=k]$.

Since $G_X$ is a power series convergent on $|s|\le1$, coefficients can be extracted by differentiating at $s=0$:

$$P[X=k]=\frac{G_X^{(k)}(0)}{k!}.$$

Thus $G_X$ uniquely determines the distribution: if $G_X=G_Y$ on $[0,1]$, then $P[X=k]=P[Y=k]$ for all $k$ by the identity theorem for power series.

Derivatives at $s=1$ give factorial moments: $G_X'(1)=E[X]$, $G_X''(1)=E[X(X-1)]$, and more generally $G_X^{(m)}(1)=E[X(X-1)\cdots(X-m+1)]$. Ordinary moments follow via Stirling numbers, e.g. $E[X^2]=G_X''(1)+G_X'(1)$ and $E[X^3]=G_X'''(1)+3G_X''(1)+G_X'(1)$.

Named PGF formulas:

- $X\sim\mathrm{Bern}(p)$: $G_X(s)=1-p+ps$.
- $X\sim\mathrm{Bin}(n,p)$: $G_X(s)=(1-p+ps)^n$.
- $X\sim\mathrm{Geom}(p)$ (trials until first success): $G_X(s)=ps/(1-(1-p)s)$.
- $X\sim\mathrm{Pois}(\lambda)$: $G_X(s)=\exp(\lambda(s-1))$.

The mean $E[X]=G_X'(1)$ exists finitely iff $\lim_{t\uparrow1}G_X'(t)<\infty$.

---

Flashcards for this section are as follows:

- probability generating function definition: If $X$ is nonnegative integer-valued, what is $G_X(s)$? ::@:: $G_X(s)=E[s^X]=\sum_{k=0}^{\infty}P[X=k]s^k$ for $|s|\le 1$.
- PGFs of independent sums: If $X$ and $Y$ are independent nonnegative integer-valued variables, what is $G_{X+Y}(s)$? ::@:: $G_{X+Y}(s)=G_X(s)G_Y(s)$.
- PGF recovers probabilities: How can you recover $P[X=k]$ from the PGF $G_X(s)$? ::@:: $P[X=k]=G_X^{(k)}(0)/k!$; differentiate $k$ times and evaluate at $s=0$.
- PGF uniqueness: If $G_X(s)=G_Y(s)$ for all $s\in[0,1]$, what follows about $X$ and $Y$? ::@:: They have the same distribution, because a convergent power series is uniquely determined by its coefficients.
- PGF as discrete-counting analogue of MGF: Why are PGFs considered the discrete-counting analogue of MGFs? ::@:: Both turn convolutions into products: $G_{X+Y}(s)=G_X(s)G_Y(s)$ and $M_{X+Y}(t)=M_X(t)M_Y(t)$; the difference is domain (nonnegative integers vs general reals), so PGFs are specialised for counting variables.
- factorial moments from PGFs: If $G_X(s)=E[s^X]$, what do derivatives of $G_X$ at $s=1$ recover? ::@:: They recover factorial moments, for example $G_X'(1)=E[X]$ and $G_X''(1)=E[X(X-1)]$.
- Bernoulli PGF: If $X\sim\mathrm{Bern}(p)$, what is $G_X(s)$? ::@:: $G_X(s)=1-p+ps$.
- Binomial PGF: If $X\sim\mathrm{Bin}(n,p)$, what is $G_X(s)$? ::@:: $G_X(s)=(1-p+ps)^n$.
- Geometric PGF: If $X\sim\mathrm{Geom}(p)$ (trials until first success, $P[X=k]=p(1-p)^{k-1}$ for $k\ge1$), what is $G_X(s)$? ::@:: $G_X(s)=\dfrac{ps}{1-(1-p)s}$.
- Poisson PGF: If $X\sim\mathrm{Pois}(\lambda)$, what is $G_X(s)$? ::@:: $G_X(s)=\exp(\lambda(s-1))$.
- PGF factorial to ordinary moments: How do you convert factorial moments $G_X^{(m)}(1)$ into $E[X^2]$ and $E[X^3]$? ::@:: $E[X^2]=G_X''(1)+G_X'(1)$; $E[X^3]=G_X'''(1)+3G_X''(1)+G_X'(1)$, using Stirling numbers of the second kind.
- PGF mean derivation: Derive $E[X]=G_X'(1)$ from the series definition of $G_X$. ::@:: $G_X'(s)=\sum_{k=1}^\infty k P[X=k]s^{k-1}$; evaluating at $s=1$ gives $G_X'(1)=\sum_{k=1}^\infty k P[X=k]=E[X]$.
- PGF mean existence condition: What condition on $G_X'$ characterises $E[X]<\infty$? ::@:: $E[X]<\infty$ iff $\lim_{t\uparrow 1}G_X'(t)$ is finite; the limit equals $E[X]$ by monotone convergence.
- PGF factorial moments in applications: Why are factorial moments $G_X^{(m)}(1)$ natural in Poisson-type and branching-process calculations? ::@:: For $X\sim\mathrm{Pois}(\lambda)$, $G_X(s)=\exp(\lambda(s-1))$ gives $G_X^{(m)}(1)=\lambda^m$ directly, avoiding polynomial conversion; they also arise naturally in Galton-Watson branching-process recursions.

## Chernoff bounds and transform methods

MGFs turn Markov's inequality into exponential tail bounds. For $t>0$, one has $P[X\ge a]=P[e^{tX}\ge e^{ta}]\le e^{-ta}M_X(t)$.

Choosing $t$ optimally gives the sharpest bound obtainable from this method. The same idea with $t<0$ controls lower tails.

Transforms also provide a route to weak convergence. If MGFs converge on a neighborhood of $0$ to the MGF of a known law, or if characteristic functions converge pointwise to a continuous limit at the origin, then the underlying random variables converge in distribution to that law.

---

Flashcards for this section are as follows:

- Chernoff bound from Markov's inequality: For $t>0$, what bound do you get by applying Markov to $e^{tX}$? ::@:: $P[X\ge a]\le e^{-ta}M_X(t)$.
- optimal Chernoff bound: How do you get the sharpest bound from $P[X\ge a]\le e^{-ta}M_X(t)$? ::@:: Choose $t>0$ to minimise $e^{-ta}M_X(t)$.
- lower-tail Chernoff bound: For $t<0$, what tail bound does applying Markov to $e^{tX}$ produce? ::@:: $P[X\le a]\le e^{-ta}M_X(t)$.
- transform method for weak convergence: If the MGFs or characteristic functions converge to the transform of a known limit law, what happens to the underlying random variables? ::@:: They converge in distribution to that law.
- Chernoff vs Markov advantage: How does $P[X\ge a]\le e^{-ta}M_X(t)$ improve on Markov's inequality $P[X\ge a]\le E[X]/a$? ::@:: Markov decays polynomially in $a$, while Chernoff decays exponentially because $e^{ta}$ in the denominator outpaces any polynomial; optimising $t$ gives the tightest exponential bound.
