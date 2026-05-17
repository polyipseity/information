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

- overview ::@:: A generating function encodes a distribution by turning probabilities into a transform that is easier to differentiate, multiply, and compare. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- three types and their uses: What are the three generating functions covered and which tasks is each best suited for? ::@:: MGF: moments and exponential tail bounds; CF: uniqueness of distribution and weak convergence; PGF: integer-valued distributions and factorial moments. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## moment generating function

The MGF $M_X(t)=E[e^{tX}]$ is said to __exist__ if it is finite on an open interval $(-h,h)$ containing $0$. Whenever differentiation under the expectation is justified, $M_X^{(n)}(0)=E[X^n]$, so the MGF stores all moments. In particular, $M_X'(0)=E[X]$ and $M_X''(0)=E[X^2]$.

Existence properties:

- __Moments from MGF:__ $M_X^{(n)}(0)=E[X^n]$ (dominated convergence justifies differentiation on the interval).
- __MGF uniquely determines the law:__ if $M_X(t)=M_Y(t)$ for all $t$ in a neighborhood of $0$, then $X$ and $Y$ have the same distribution (analytic continuation to the CF, then Lévy's inversion formula).
- __Analyticity:__ $t\mapsto M_X(t)$ is infinitely differentiable and analytic on its domain; the power series $\sum_{k\ge0}E[X^k]t^k/k!$ converges to $M_X(t)$ on $(-h,h)$.
- __Affine transformation:__ $M_{aX+b}(t)=e^{tb}M_X(at)$.

MGF existence near $0$ is stronger than mere finiteness of all moments. A counterexample is the lognormal distribution: $X=e^Y$ with $Y\sim N(0,1)$. Compute $E[X^n]=E[e^{nY}]=e^{n^2/2}<\infty$ for all $n$ (the MGF of $N(0,1)$ at $t=n$). But $E[e^{tX}]=E[e^{te^Y}]=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp(te^y-y^2/2)\,dy$ diverges for $t>0$ because $te^y$ dominates $y^2/2$ as $y\to\infty$, making the integrand unbounded. So theorems requiring MGF existence (Chernoff bounds, MGF uniqueness) are genuinely stronger than moment assumptions.

---

Flashcards for this section are as follows:

- moment generating function definition: For a random variable $X$, what is $M_X(t)$? ::@:: $M_X(t)=E[e^{tX}]$ for those $t$ at which the expectation is finite. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF existence requirement: For the MGF $M_X(t)=E[e^{tX}]$ to give strong analytic control, what must its domain satisfy? ::@:: It must be finite on an open interval containing $0$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- moments from MGF derivatives: If $M_X(t)=E[e^{tX}]$ and differentiation under the expectation is justified, what is $M_X^{(n)}(0)$? ::@:: $M_X^{(n)}(0)=E[X^n]$. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF affine transformation: If $Y=aX+b$, what is $M_Y(t)$ in terms of $M_X$? ::@:: $M_{aX+b}(t)=e^{tb}M_X(at)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF uniqueness statement: If $M_X(t)=M_Y(t)$ for all $t$ in a neighborhood of $0$, what can you conclude? ::@:: $X$ and $Y$ have the same distribution; the MGF uniquely determines the law on its interval of existence. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF uniqueness proof idea: How does MGF uniqueness follow from CF uniqueness? ::@:: Agreement of MGFs near $0$ implies agreement of CFs after analytic continuation $t\mapsto it$; CFs determine the law uniquely by the inversion formula. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF analyticity: When $M_X(t)$ exists in $(-h,h)$, what are the analytic properties of $t\mapsto M_X(t)$? ::@:: It is infinitely differentiable and analytic on its domain; in particular $M_X^{(k)}(0)=E[X^k]$ and the power series $\sum_{k\ge0}E[X^k]t^k/k!$ converges to $M_X(t)$ on $(-h,h)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF vs all moments: How does MGF existence near $0$ compare with having all moments $E[X^n]$? ::@:: MGF existence near $0$ is stronger; it implies all moments exist and gives analytic control. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- lognormal counterexample: Give a distribution with all moments finite but no MGF near $0$. ::@:: $X=e^Y$ with $Y\sim N(0,1)$. Moments: $E[X^n]=E[e^{nY}]=e^{n^2/2}<\infty$ (MGF of $N(0,1)$ at $t=n$). MGF: $E[e^{tX}]=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp(te^y-y^2/2)\,dy$, which diverges for $t>0$ because $te^y$ outgrows $y^2/2$ as $y\to\infty$, so no MGF exists on any $t>0$. <!--SR:!fsrs,2026-08-27T00:00:00.000Z,44,44.09694232,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,46,46.47643997,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## relations between generating functions and uniqueness

The three generating functions are related by substitution: $M_X(it)=\varphi_X(t)$ (analytic continuation: if $M_X$ exists near $0$, then $t\mapsto M_X(it)$ is a CF on $\mathbb R$); $G_X(e^t)=M_X(t)$ for integer-valued $X\ge0$; and $\varphi_X(t)=G_X(e^{it})$ for integer-valued $X\ge0$.

Each generating function also recovers distributional information from its derivatives, and each uniquely determines the underlying law:

- __MGF:__ $M_X^{(n)}(0)=E[X^n]$ recovers moments; $M_X$ uniquely determines the distribution via analytic continuation to the CF.
- __CF:__ $\varphi_X$ uniquely determines the distribution via the inversion formula; $\varphi_X^{(n)}(0)=i^nE[X^n]$ when moments exist.
- __PGF:__ $G_X^{(k)}(0)/k!=P[X=k]$ recovers probabilities; $G_X$ uniquely determines the distribution as coefficients of its power series.

Moreover, for each transform, the existence of the first moment has a derivative-based characterisation: for the MGF, $E[X]=M_X'(0)$ (on the interval of existence); for the CF, $E[X]=-i\varphi_X'(0)$ when $E[|X|]<\infty$; and for the PGF, $E[X]=G_X'(1)=\lim_{t\uparrow 1}G_X'(t)$ (the derivative at $1$ is a left-hand limit only — the notation $G_X'(1)$ is deceptive shorthand; see the PGF section).

---

Flashcards for this section are as follows:

- How are MGF, CF, and PGF related by substitution? ::@:: $M_X(it)=\varphi_X(t)$ (analytic continuation); $G_X(e^t)=M_X(t)$ and $\varphi_X(t)=G_X(e^{it})$ for integer-valued $X\ge0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Similarity across MGF, CF, PGF: How does each generating function recover distributional information from its derivatives and uniquely determine the law? ::@:: MGF: $M_X^{(n)}(0)=E[X^n]$ (moments); uniquely via analytic continuation to CF. CF: $\varphi_X^{(n)}(0)=i^nE[X^n]$ (moments); uniquely via inversion formula. PGF: $G_X^{(k)}(0)/k!=P[X=k]$ (probabilities); uniquely as power-series coefficients. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- First moment from each generating function: Express $E[X]$ from the MGF, CF, and PGF in terms of their derivatives. ::@:: MGF: $E[X]=M_X'(0)$ on its interval of existence. CF: $E[X]=-i\varphi_X'(0)$ when $E[|X|]<\infty$. PGF: $E[X]=G_X'(1)=\lim_{t\uparrow 1}G_X'(t)$ (the derivative at $1$ is a left-hand limit only; $G_X'(1)$ is deceptive shorthand for a one-sided limit). <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### uniqueness theorem

For each generating function, the correspondence is __bidirectional__: $$\text{equal transforms (on the appropriate domain)}\quad\Longleftrightarrow\quad\text{equal probability laws}.$$

The forward direction ($\Longleftarrow$) is trivial: equal distributions give equal expectations. The converse is the uniqueness theorem:

- __CF (no condition needed):__ Fourier inversion recovers the CDF at continuity points: $F_X(b)-F_X(a)=\frac1{2\pi}\lim_{T\to\infty}\int_{-T}^T\frac{e^{-ita}-e^{-itb}}{it}\,\varphi_X(t)\,dt$. Equal CFs $\Rightarrow$ equal right-hand sides $\Rightarrow$ equal CDFs.

- __MGF (finite near $0$):__ $M_X(z)=E[e^{zX}]$ is analytic on a strip $\{z:|\operatorname{Re}z|<h\}$. Equality on $(-h,h)$ forces equality on the strip, hence on the imaginary axis where it reduces to the CF; CF uniqueness then gives $X\stackrel d=Y$.

- __PGF ($|s|\le1$):__ $G_X(s)=\sum P[X=k]s^k$ is a power series. If $G_X(s)=G_Y(s)$ on $[0,1]$, the identity theorem forces equal coefficients $P[X=k]=P[Y=k]$ for all $k$.

---

Flashcards for this section are as follows:

- bidirectional equivalence: For each generating function, equal transforms (on the appropriate domain) are equivalent to what? ::@:: Equal probability laws. ($\Longleftarrow$ is trivial; $\Longrightarrow$ is the uniqueness theorem per transform.) <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- uniqueness engine by transform: What is the proof engine for uniqueness of CF, MGF, and PGF? ::@:: CF: Fourier inversion (always works). MGF: analytic continuation $\to$ CF (needs existence near $0$). PGF: identity theorem for power series (coeffs are probabilities). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF uniqueness via Fourier inversion: How does the Fourier inversion formula prove that equal CFs imply equal distributions? ::@:: $\displaystyle F_X(b)-F_X(a)=\frac1{2\pi}\lim_{T\to\infty}\int_{-T}^T\frac{e^{-ita}-e^{-itb}}{it}\,\varphi_X(t)\,dt$; if $\varphi_X=\varphi_Y$, the right-hand sides match at all continuity points, so the CDFs are equal. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF uniqueness via analytic continuation: How does MGF equality near $0$ imply equal distributions? ::@:: $M_X(z)$ is analytic on a strip $\{z:|\operatorname{Re}z|<h\}$. Equality on $(-h,h)$ extends analytically to the whole strip, including the imaginary axis where $M_X(it)=\varphi_X(t)$; CF uniqueness then gives $X\stackrel d=Y$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF uniqueness via identity theorem: How does PGF equality on $[0,1]$ imply equal distributions? ::@:: $G_X(s)=\sum P[X=k]s^k$ is a power series; if $G_X=G_Y$ on $[0,1]$, the identity theorem for analytic functions forces $P[X=k]=P[Y=k]$ for all $k$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## convolution of independent sums through MGFs

If $X$ and $Y$ are independent, then $M_{X+Y}(t)=E[e^{t(X+Y)}]=E[e^{tX}e^{tY}]=M_X(t)M_Y(t)$.

This is the transform version of convolution: sums of independent random variables become products of MGFs.

For iid variables $X_1,\dots,X_n$ with common MGF $M_X$, one therefore has $M_{X_1+\cdots+X_n}(t)=M_X(t)^n$.

This is why MGFs prove closure properties so efficiently. For example, comparing MGFs immediately gives the addition laws for binomial, Poisson, and normal distributions.

---

Flashcards for this section are as follows:

- MGFs of independent sums: If $X$ and $Y$ are independent with MGFs $M_X$ and $M_Y$, what is $M_{X+Y}(t)$? ::@:: $M_{X+Y}(t)=M_X(t)M_Y(t)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- iid sum via MGFs: If $X_1,\dots,X_n$ are iid with common MGF $M_X$, what is $M_{X_1+\cdots+X_n}(t)$? ::@:: $M_{X_1+\cdots+X_n}(t)=M_X(t)^n$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- MGF closure properties: What distributional fact can you prove by comparing MGFs? ::@:: The addition (closure) laws for sums of independent binomial, Poisson, and normal variables. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## named MGF formulas for binomial, Poisson, normal, and exponential

For the standard named laws used throughout the course:

- If $X\sim\mathrm{Bin}(n,p)$, then $M_X(t)=E[e^{tX}]=(1-p+pe^t)^n$. This is just the binomial theorem applied to $n$ Bernoulli trials.

- If $X\sim\mathrm{Pois}(\lambda)$, then $M_X(t)=\sum_{k=0}^{\infty}e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}=\exp(\lambda(e^t-1))$.

- If $X\sim N(\mu,\sigma^2)$, then completing the square gives $M_X(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right)$.

- If $X\sim E(\lambda)$, then $M_X(t)=\int_0^{\infty}\lambda e^{-\lambda x}e^{tx}\,dx=\frac{\lambda}{\lambda-t}$ for $t<\lambda$.

These formulas are the workhorses behind Chernoff bounds and limit theorems.

---

Flashcards for this section are as follows:

- binomial MGF formula: If $X\sim\mathrm{Bin}(n,p)$, what is $M_X(t)$? ::@:: $M_X(t)=(1-p+pe^t)^n$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Poisson MGF formula: If $X\sim\mathrm{Pois}(\lambda)$, what is $M_X(t)$? ::@:: $M_X(t)=\exp(\lambda(e^t-1))$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- normal MGF formula: If $X\sim N(\mu,\sigma^2)$, what is $M_X(t)$? ::@:: $M_X(t)=\exp(\mu t+\sigma^2t^2/2)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- exponential MGF formula: If $X\sim E(\lambda)$ and $t<\lambda$, what is $M_X(t)$? ::@:: $M_X(t)=\lambda/(\lambda-t)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Bernoulli MGF formula: If $X\sim\mathrm{Bern}(p)$, what is $M_X(t)$? ::@:: $M_X(t)=1-p+pe^t$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- normal MGF derivation: What technique derives $M_X(t)=\exp(\mu t+\sigma^2t^2/2)$ for $X\sim N(\mu,\sigma^2)$? ::@:: Completing the square in the exponent of $e^{tx}$ under the normal density integral. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

## characteristic function

The characteristic function $\varphi_X(t)=E[e^{itX}]$ exists for all $t\in\mathbb R$ since $|e^{itX}|=1$ guarantees finiteness, making it the universal Fourier transform of a probability law.

Uniform continuity follows from the difference bound $|\varphi_X(t+h)-\varphi_X(t)|=|E[e^{itX}(e^{ihX}-1)]|\le E[|e^{ihX}-1|]$, where the right-hand side does not depend on $t$ and tends to $0$ as $h\to0$ by dominated convergence ($|e^{ihX}-1|\le2$).

---

Flashcards for this section are as follows:

- characteristic function definition: For a random variable $X$, what is $\varphi_X(t)$? ::@:: $\varphi_X(t)=E[e^{itX}]$ for $t\in\mathbb R$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- why characteristic functions always exist: Why does $|e^{itX}|=1$ guarantee that $\varphi_X(t)=E[e^{itX}]$ is always defined? ::@:: The modulus is always $1$, so the expectation is bounded and therefore exists. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF of independent sums: If $X$ and $Y$ are independent, what is $\varphi_{X+Y}(t)$? ::@:: $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF uniform continuity property: Derive the uniform continuity of $\varphi_X(t)=E[e^{itX}]$. ::@:: $|\varphi_X(t+h)-\varphi_X(t)|=|E[e^{itX}(e^{ihX}-1)]|\le E[|e^{ihX}-1|]$ (triangle inequality + $|e^{itX}|=1$). The RHS is independent of $t$ and $\to0$ as $h\to0$ by dominated convergence ($|e^{ihX}-1|\le2$), so $\varphi_X$ is uniformly continuous. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF boundedness: What bounds hold for $|\varphi_X(t)|$? ::@:: $|\varphi_X(t)|\le1$ for all $t$, with $\varphi_X(0)=1$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF conjugate symmetry: How is $\varphi_X(-t)$ related to $\varphi_X(t)$? ::@:: $\varphi_X(-t)=\overline{\varphi_X(t)}$ because $e^{-itX}$ is the complex conjugate of $e^{itX}$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- CF of affine transformation: If $Y=aX+b$, what is $\varphi_Y(t)$ in terms of $\varphi_X$? ::@:: $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Lévy continuity theorem (forward direction): If $X_n\xrightarrow{d}X$, what happens to the CFs? ::@:: $\varphi_{X_n}(t)\to\varphi_X(t)$ for all $t\in\mathbb R$. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

Key properties:

- __Uniform continuity:__ $|\varphi_X(t+h)-\varphi_X(t)|\le E[|e^{ihX}-1|]\to0$ as $h\to0$ (dominated convergence).
- __Boundedness:__ $|\varphi_X(t)|\le1$ for all $t$, $\varphi_X(0)=1$.
- __Conjugate symmetry:__ $\varphi_X(-t)=\overline{\varphi_X(t)}$.
- __Independent sums:__ $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$, central to the CLT (Taylor-expand $\varphi_X$ and apply Lévy's continuity theorem).
- __Affine transformation:__ $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$.
- __Moments (when they exist):__ $\varphi_X^{(n)}(0)=i^nE[X^n]$; conversely $\varphi_X^{(n)}(0)$ finite implies $E[|X|^{n}]<\infty$ (even $n$) or $E[|X|^{n-1}]<\infty$ (odd $n$).
- __Uniqueness:__ If $\varphi_X(t)=\varphi_Y(t)$ for all $t$, then $X\stackrel d=Y$ by the inversion formula.
- __Lévy's continuity theorem:__ $X_n\xrightarrow{d}X$ $\Rightarrow$ $\varphi_{X_n}(t)\to\varphi_X(t)$; conversely, if $\varphi_{X_n}$ converges pointwise to $\varphi$ continuous at $0$, $X_n\xrightarrow{d}X$ for some $X$ with CF $\varphi$.

## probability generating functions for discrete distributions

If $X$ is nonnegative integer-valued, its probability generating function is $G_X(s)=E[s^X]=\sum_{k=0}^{\infty}P[X=k]s^k$ for $|s|\le 1$. This is the discrete-counting analogue of the MGF: independent sums become products $G_{X+Y}(s)=G_X(s)G_Y(s)$, and the coefficients are exactly the probabilities $P[X=k]$.

Since $G_X$ is a power series convergent on $|s|\le1$, coefficients can be extracted by differentiating at $s=0$: $$P[X=k]=\frac{G_X^{(k)}(0)}{k!}.$$

Thus $G_X$ uniquely determines the distribution: if $G_X=G_Y$ on $[0,1]$, then $P[X=k]=P[Y=k]$ for all $k$ by the identity theorem for power series.

Derivatives at $s=1$ give factorial moments: $E[X] = G_X'(1) = \lim_{t\uparrow 1}G_X'(t)$, $G_X''(1)=E[X(X-1)]$, and more generally $G_X^{(m)}(1)=E[X(X-1)\cdots(X-m+1)]$. Ordinary moments follow via Stirling numbers, e.g. $E[X^2]=G_X''(1)+G_X'(1)$ and $E[X^3]=G_X'''(1)+3G_X''(1)+G_X'(1)$.

Named PGF formulas:

- $X\sim\mathrm{Bern}(p)$: $G_X(s)=1-p+ps$.
- $X\sim\mathrm{Bin}(n,p)$: $G_X(s)=(1-p+ps)^n$.
- $X\sim\mathrm{Geom}(p)$ (trials until first success): $G_X(s)=ps/(1-(1-p)s)$.
- $X\sim\mathrm{Pois}(\lambda)$: $G_X(s)=\exp(\lambda(s-1))$.

The notation $G_X'(1)$ is deceptive: it suggests a two-sided derivative, but only a left-hand limit is guaranteed. The PGF $G_X(s)=\sum_{k\ge 0}P[X=k]s^k$ is a power series convergent on $|s|\le 1$. Termwise differentiation gives $\sum_{k\ge 1}kP[X=k]s^{k-1}$, which converges for $|s|<1$ by the same radius of convergence. At $s=1$, the differentiated series $\sum kP[X=k]$ is exactly $E[X]$, which may be finite or infinite. This value is obtained as the left-hand limit $\lim_{t\uparrow 1}G_X'(t)$ (by Abel's theorem for power series, or by monotone convergence on $[0,1)$). A two-sided derivative at $1$ is not necessary because $G_X$ is defined only on $|s|\le 1$ — for $s>1$ the defining series may diverge (unless the distribution has finite support or light-enough tails to extend the radius). Hence $E[X]<\infty$ iff $\lim_{t\uparrow 1}G_X'(t)<\infty$, and when finite the limit equals $E[X]$.

---

Flashcards for this section are as follows:

- probability generating function definition: If $X$ is nonnegative integer-valued, what is $G_X(s)$? ::@:: $G_X(s)=E[s^X]=\sum_{k=0}^{\infty}P[X=k]s^k$ for $|s|\le 1$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGFs of independent sums: If $X$ and $Y$ are independent nonnegative integer-valued variables, what is $G_{X+Y}(s)$? ::@:: $G_{X+Y}(s)=G_X(s)G_Y(s)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF recovers probabilities: How can you recover $P[X=k]$ from the PGF $G_X(s)$? ::@:: $P[X=k]=G_X^{(k)}(0)/k!$; differentiate $k$ times and evaluate at $s=0$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF uniqueness: If $G_X(s)=G_Y(s)$ for all $s\in[0,1]$, what follows about $X$ and $Y$? ::@:: They have the same distribution, because a convergent power series is uniquely determined by its coefficients. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF as discrete-counting analogue of MGF: Why are PGFs considered the discrete-counting analogue of MGFs? ::@:: Both turn convolutions into products: $G_{X+Y}(s)=G_X(s)G_Y(s)$ and $M_{X+Y}(t)=M_X(t)M_Y(t)$; the difference is domain (nonnegative integers vs general reals), so PGFs are specialised for counting variables. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- factorial moments from PGFs: If $G_X(s)=E[s^X]$, what do derivatives of $G_X$ at $s=1$ recover? ::@:: They recover factorial moments, for example $G_X'(1)=\lim_{t\uparrow 1}G_X'(t)=E[X]$ and $G_X''(1)=E[X(X-1)]$ (the first derivative is a left-hand limit only; $G_X'(1)$ is shorthand). <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Bernoulli PGF: If $X\sim\mathrm{Bern}(p)$, what is $G_X(s)$? ::@:: $G_X(s)=1-p+ps$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Binomial PGF: If $X\sim\mathrm{Bin}(n,p)$, what is $G_X(s)$? ::@:: $G_X(s)=(1-p+ps)^n$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Geometric PGF: If $X\sim\mathrm{Geom}(p)$ (trials until first success, $P[X=k]=p(1-p)^{k-1}$ for $k\ge1$), what is $G_X(s)$? ::@:: $G_X(s)=\dfrac{ps}{1-(1-p)s}$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Poisson PGF: If $X\sim\mathrm{Pois}(\lambda)$, what is $G_X(s)$? ::@:: $G_X(s)=\exp(\lambda(s-1))$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF factorial to ordinary moments: How do you convert factorial moments $G_X^{(m)}(1)$ into $E[X^2]$ and $E[X^3]$? ::@:: $E[X^2]=G_X''(1)+G_X'(1)$; $E[X^3]=G_X'''(1)+3G_X''(1)+G_X'(1)$, using Stirling numbers of the second kind. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF mean derivation: Derive $E[X]=G_X'(1)$ from the series definition of $G_X$, being careful about the one-sided limit. ::@:: $G_X'(s)=\sum_{k=1}^\infty k P[X=k]s^{k-1}$ for $|s|<1$. Let $s\uparrow 1$; by monotone convergence (or Abel's theorem) $\lim_{s\uparrow 1}G_X'(s)=\sum_{k=1}^\infty k P[X=k]=E[X]$. The expression $G_X'(1)$ is shorthand for this one-sided limit; termwise evaluation at $s=1$ would be unjustified because $G_X$ may not be differentiable at the boundary of its convergence disk. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF mean existence condition: What condition on $G_X'$ characterises $E[X]<\infty$? ::@:: $E[X]<\infty$ iff $\lim_{t\uparrow 1}G_X'(t)$ is finite; the limit equals $E[X]$ by monotone convergence. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-08-27T00:00:00.000Z,44,44.09694232,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF factorial moments in applications: Why are factorial moments $G_X^{(m)}(1)$ natural in Poisson-type and branching-process calculations? ::@:: For $X\sim\mathrm{Pois}(\lambda)$, $G_X(s)=\exp(\lambda(s-1))$ gives $G_X^{(m)}(1)=\lambda^m$ directly, avoiding polynomial conversion; they also arise naturally in Galton-Watson branching-process recursions. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF at boundary of convergence: Why is the notation $G_X'(1)$ for $E[X]$ mathematically deceptive? ::@:: $G_X$ is a power series convergent on $|s|\le 1$; termwise differentiation gives series convergent on $|s|<1$. At $s=1$ (the boundary), evaluation at $s=1$ of the differentiated series would be unjustified because convergence at the boundary is not guaranteed. The correct expression is the left-hand limit $\lim_{t\uparrow 1}G_X'(t)$, which equals $E[X]$ by monotone convergence or Abel's theorem. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,46,46.47643997,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF why one-sided limit only: For the PGF $G_X(s)=\sum_{k\ge 0}P[X=k]s^k$, why is only a left-hand limit needed to recover $E[X]$? ::@:: The PGF is defined on $|s|\le 1$, which is the natural domain of its power series. For $s>1$ the series may diverge — unless the distribution has finite support or light-enough tails to extend the radius. So there is no right-hand side to take a limit from; a two-sided derivative at $1$ is not meaningful in general. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- PGF left-hand limit convergence justification: What theorems justify $\lim_{s\uparrow 1}G_X'(s)=E[X]$? ::@:: (1) Monotone convergence: $G_X'(s)=\sum kP[X=k]s^{k-1}$ is monotone in $s$ (nondecreasing for $s\ge0$) and the limit as $s\uparrow 1$ equals $\sum kP[X=k]=E[X]$. (2) Abel's theorem for power series: if $\sum a_k$ converges, then $\lim_{s\uparrow 1}\sum a_k s^k=\sum a_k$; applied to $kP[X=k]$ as coefficients. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: proper noun (Chernoff is a person's name) -->
## Chernoff bounds and transform methods

MGFs turn Markov's inequality into exponential tail bounds. For $t>0$, one has $P[X\ge a]=P[e^{tX}\ge e^{ta}]\le e^{-ta}M_X(t)$.

Choosing $t$ optimally gives the sharpest bound obtainable from this method. The same idea with $t<0$ controls lower tails.

Transforms also provide a route to weak convergence. If MGFs converge on a neighborhood of $0$ to the MGF of a known law, or if characteristic functions converge pointwise to a continuous limit at the origin, then the underlying random variables converge in distribution to that law.

---

Flashcards for this section are as follows:

- Chernoff bound from Markov's inequality: For $t>0$, what bound do you get by applying Markov to $e^{tX}$? ::@:: $P[X\ge a]\le e^{-ta}M_X(t)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-13T00:00:00.000Z,61,61.12602477,1,2,3,0,0,2026-07-14T00:00:00.000Z-->
- optimal Chernoff bound: How do you get the sharpest bound from $P[X\ge a]\le e^{-ta}M_X(t)$? ::@:: Choose $t>0$ to minimise $e^{-ta}M_X(t)$. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- lower-tail Chernoff bound: For $t<0$, what tail bound does applying Markov to $e^{tX}$ produce? ::@:: $P[X\le a]\le e^{-ta}M_X(t)$. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- transform method for weak convergence: If the MGFs or characteristic functions converge to the transform of a known limit law, what happens to the underlying random variables? ::@:: They converge in distribution to that law. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
- Chernoff vs Markov advantage: How does $P[X\ge a]\le e^{-ta}M_X(t)$ improve on Markov's inequality $P[X\ge a]\le E[X]/a$? ::@:: Markov decays polynomially in $a$, while Chernoff decays exponentially because $e^{ta}$ in the denominator outpaces any polynomial; optimising $t$ gives the tightest exponential bound. <!--SR:!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-09-27T00:00:00.000Z,75,75.34793403,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
