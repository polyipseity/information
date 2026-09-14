---
aliases:
  - ELEC 2100 Laplace transform
  - ELEC2100 Laplace transform
  - HKUST ELEC 2100 Laplace transform
  - Laplace transform
  - bilateral Laplace transform
  - system function in s-domain
  - unilateral Laplace transform
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/Laplace_transform
  - language/in/English
---

# Laplace transform

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

## overview and motivation

Laplace analysis extends Fourier methods to transient, causal, and differential-equation problems: derivatives and integrals become algebraic factors in $s$, unilateral Laplace keeps track of initial conditions, and poles/transfer functions are easy to analyze.

The method is named after Pierre-Simon Laplace, who introduced transform methods for differential equations in 1779.  Oliver Heaviside later developed operational-calculus methods in the late 19th century that made the same ideas practical for circuits and transmission lines.

Main advantages: differential and integral equations become algebraic in $s$; unilateral analysis incorporates initial conditions automatically; convolution, transfer functions, poles, and block-diagram interconnections become easier.

Main caveats: physical interpretation is less immediate than Fourier-transform frequency analysis; the ROC must always be tracked, because the same algebraic expression can represent different time-domain signals.

The Laplace unit in this course uses Laplace transform for four recurring tasks: direct transforms, inverse transforms, solving differential equations and dynamic circuits, and building system functions for pole-zero, stability, and block-diagram analysis.

---

Flashcards for this section are as follows:

- What is the role of Laplace transform in the course roadmap? ::@:: It is the complex-frequency bridge from time-domain differential-equation models to transfer functions, pole-zero analysis, stability tests, block-diagram interconnection, and dynamic-circuit response.
- What short historical picture should you remember for the Laplace transform? ::@:: Laplace introduced the transform method for differential equations in 1779, and Heaviside later developed operational-calculus methods that made the ideas practical for engineering.
- What are the main advantages of Laplace transform in ELEC 2100? ::@:: It turns differential/integral equations into algebraic equations in $s$, incorporates initial conditions automatically in unilateral form, and makes transfer functions, poles, convolution, and block-diagram analysis easier.
- What is the main disadvantage of Laplace transform compared with Fourier transform? ::@:: Physical interpretation is less immediate than Fourier frequency analysis, and it requires explicit ROC bookkeeping because the same algebraic expression can represent different time-domain signals.
- What are the main uses of Laplace transform in the Laplace unit of ELEC 2100? ::@:: Direct transforms, inverse transforms, solving differential equations and dynamic circuits, and forming system functions for pole-zero, stability, and block-diagram analysis.

## definition and ROC

The bilateral Laplace transform is $F(s)=\mathcal{L}\{f(t)\}=\int_{-\infty}^{\infty} f(t)e^{-st}\,dt$ with $s=\sigma+j\omega$.

For causal signals and systems, ELEC 2100 mainly uses the unilateral form $F(s)=\mathcal{L}_u\{f(t)\}=\int_{0^-}^{\infty} f(t)e^{-st}\,dt$.

The __region of convergence__ (ROC) is the set of $s$ values for which the transform integral converges absolutely.

Since $|e^{-st}|=e^{-\sigma t}$, the real part $\sigma$ controls convergence: for $t>0$, larger $\sigma$ adds decay $e^{-\sigma t}$ and helps a right-sided tail converge; for $t<0$, larger $\sigma$ makes $e^{\sigma|t|}$ grow faster, so moving left helps a left-sided tail converge.

For the right-sided exponential $e^{pt}u(t)$, the transform is $\frac{1}{s-p}$ with ROC $\Re(s)>\Re(p)$; for the left-sided signal $-e^{pt}u(-t)$, the transform is again $\frac{1}{s-p}$ but the ROC is $\Re(s)<\Re(p)$.  The same algebraic factor can represent different time-domain signals; the ROC records which side of the pole makes the weighted integral decay.

An existence criterion is __exponential order__: if $|f(t)|\le Me^{at}$ for sufficiently large $t>0$, then $\mathcal{L}_u\{f(t)\}$ converges for $\Re(s)>a$.  For bilateral transforms, both tails matter: if $|f(t)|\le M_+e^{a_+ t}$ for large positive $t$ and $|f(t)|\le M_-e^{a_- t}$ for large negative $t$, the transform converges in the strip $a_+<\Re(s)<a_-$ if that strip is nonempty.

These rules follow:

- Bounded aperiodic signals have Laplace transforms in the unilateral/right-sided setting (boundedness implies exponential order $a=0$, so ROC $\Re(s)>0$);
- polynomials grow more slowly than exponentials, so $t^n u(t)$ has ROC $\Re(s)>0$;
- $\mathcal{L}_u\{e^{\alpha t}u(t)\}=\frac{1}{s-\alpha}$ with ROC $\Re(s)>\alpha$;
- super-exponential signals such as $e^{t^2}u(t)$ have no Laplace transform for any finite $s$.

The bounded-aosped shortcut is safest in the unilateral/right-sided setting because a bounded right-sided signal has exponential order $a=0$, so $\mathcal{L}_u\{f(t)\}$ converges for $\Re(s)>0$.  For bilateral transforms, opposite tails can still demand incompatible signs of $\Re(s)$, so boundedness alone does not guarantee a common ROC strip.

For a rational form, pole real parts partition the $s$-plane into candidate ROC regions.  The signal support restriction selects which candidate is valid — the ROC depends on the signal restriction, not on the algebraic expression alone.  When components are combined, the transform is justified on the __intersection of their individual ROCs__.  For example, $e^{t}u(t)$ has ROC $\Re(s)>1$ and $e^{3t}u(t)$ has ROC $\Re(s)>3$, so their sum has ROC $\Re(s)>3$.  Likewise, $e^{-t}u(t)$ has ROC $\Re(s)>-1$ while $-e^{2t}u(-t)$ has ROC $\Re(s)<2$, so the combined two-sided signal has strip ROC $-1<\Re(s)<2$.  After algebraic simplification, pole-zero cancellation can enlarge the final ROC.

The ROC shapes are:

- Right-sided: right half-plane $\Re(s)>\sigma_{\max}$, where $\sigma_{\max}$ is the rightmost convergence boundary.
- Left-sided: left half-plane $\Re(s)<\sigma_{\min}$.
- Two-sided: vertical strip $\sigma_{\min}<\Re(s)<\sigma_{\max}$.
- Finite-duration: entire finite $s$-plane.

For rational transforms, the ROC is an open connected pole-free region, and poles lie on its boundary or outside it.  Once the ROC is specified, the inverse Laplace transform is unique.  When the ROC includes the imaginary axis $\Re(s)=0$, evaluation at $s=j\omega$ recovers the Fourier transform.

The notation $0^-$ in the lower limit of the unilateral transform denotes the left-hand limit approaching zero: the integration domain begins infinitesimally before $t=0$, so $t=0$ itself is included.

For signals without distributional components, this distinction is immaterial: a single point has Lebesgue measure zero and cannot alter an integral.  For example, $\int_{0^-}^{\infty}e^{-t}e^{-st}\,dt=\int_{0^+}^{\infty}e^{-t}e^{-st}\,dt=\frac{1}{1+s}$.

The distinction becomes critical for signals containing a Dirac delta at the origin.  By the sifting property, $\int\delta(t)\varphi(t)\,dt=\varphi(0)$, so the choice of lower limit determines whether the impulse mass at $t=0$ is included:

$\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=1,\qquad\text{but}\qquad\int_{0^+}^{\infty}\delta(t)e^{-st}\,dt=0$.

Engineering Laplace analysis adopts $0^-$ so that impulsive excitations $\delta(t)$ at $t=0$ are fully captured and initial conditions stored just before $t=0$ are automatically retained.

---

Flashcards for this section are as follows:

- What is the bilateral Laplace transform definition? ::@:: $F(s)=\int_{-\infty}^{\infty} f(t)e^{-st}\,dt$ with $s=\sigma+j\omega$.
- For the unilateral transform formula $F(s)=\mathcal{L}_u\{f(t)\}=\int_{0^-}^{\infty} f(t)e^{-st}\,dt$, what definition is used most often in ELEC 2100? ::@:: The unilateral Laplace transform integrates from $0^-$ to $\infty$ so initial-condition information is retained for causal-system analysis.
- What is the ROC in Laplace analysis? ::@:: The set of complex-frequency values $s$ for which the transform integral converges absolutely.
- For the same algebraic factor $\frac{1}{s-p}$, how do right-sided $e^{pt}u(t)$ and left-sided $-e^{pt}u(-t)$ differ? ::@:: Same transform $\frac{1}{s-p}$ but different ROCs.  Right-sided requires $\Re(s)>\Re(p)$; left-sided requires $\Re(s)<\Re(p)$.  The ROC identifies which side of the pole makes the integral decay.
- What is exponential order, and what does it imply for ROC? ::@:: If $|f(t)|\le Me^{at}$ for large $t>0$, then $\mathcal{L}_u\{f(t)\}$ converges for $\Re(s)>a$.  For bilateral transforms, both tails matter: convergence holds in the strip $a_+<\Re(s)<a_-$ if nonempty.
- Why do right-sided power functions such as $t^n u(t)$ have a Laplace transform? ::@:: Polynomials grow more slowly than exponentials, so $e^{-\sigma t}$ dominates $t^n$ for every $\sigma>0$.  Therefore $t^n u(t)$ has ROC $\Re(s)>0$.
- What is the ROC of $e^{\alpha t}u(t)$? ::@:: $\mathcal{L}_u\{e^{\alpha t}u(t)\}=\frac{1}{s-\alpha}$ with ROC $\Re(s)>\alpha$.
- Why do $e^{\alpha t}u(t)$ and $e^{t^2}u(t)$ differ in transformability? ::@:: $e^{\alpha t}u(t)$ converges for $\Re(s)>\alpha$, but $e^{t^2}u(t)$ grows faster than any exponential so no finite $\Re(s)$ forces convergence.
- What are the four ROC shapes and what determines which one applies? ::@:: Right-sided: $\Re(s)>\sigma_{\max}$.  Left-sided: $\Re(s)<\sigma_{\min}$.  Two-sided: $\sigma_{\min}<\Re(s)<\sigma_{\max}$.  Finite-duration: entire $s$-plane.  The signal support class selects which candidate is valid.
- When components are combined, how does the ROC change? ::@:: The ROC is the intersection of individual ROCs.  After simplification, pole-zero cancellation can enlarge the final ROC.
- When does the Laplace transform reduce to the Fourier transform? ::@:: When the ROC includes the imaginary axis $\Re(s)=0$, evaluation at $s=j\omega$ yields the Fourier transform.
- What does the lower limit $0^-$ denote in $\int_{0^-}^{\infty}f(t)e^{-st}\,dt$? ::@:: The left-hand limit approaching zero: the integration path begins infinitesimally before $t=0$, including $t=0$ in the domain.
- Why does $0^-$ vs $0^+$ matter for signals with a Dirac delta at the origin? ::@:: $\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=1$ (impulse included) while $\int_{0^+}^{\infty}\delta(t)e^{-st}\,dt=0$ (impulse excluded).  Engineering Laplace uses $0^-$ to capture impulses at $t=0$ and initial conditions at $t=0^-$.

## common transform pairs and core properties

Common unilateral pairs used in this course include:

- $u(t) \longleftrightarrow \frac{1}{s}$, ROC $\Re(s)>0$
- $e^{-\alpha t}u(t) \longleftrightarrow \frac{1}{s+\alpha}$, ROC $\Re(s)>-\alpha$
- $\delta(t) \longleftrightarrow 1$
- $t^n u(t) \longleftrightarrow \frac{n!}{s^{n+1}}$
- $\sin(\omega_0 t)u(t) \longleftrightarrow \frac{\omega_0}{s^2+\omega_0^2}$, ROC $\Re(s)>0$
- $\cos(\omega_0 t)u(t) \longleftrightarrow \frac{s}{s^2+\omega_0^2}$, ROC $\Re(s)>0$

Brief derivation cues:

- $u(t)$: $\int_{0^-}^{\infty}e^{-st}\,dt=\frac{1}{s}$, valid for $\Re(s)>0$.
- $e^{-\alpha t}u(t)$: $\int_{0^-}^{\infty}e^{-(s+alpha)t}\,dt=\frac{1}{s+\alpha}$, ROC $\Re(s)>-\alpha$.
- $\delta(t)$: sifting gives $\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=1$.
- $t^n u(t)$: repeated integration by parts gives $\int_0^{\infty}t^n e^{-st}\,dt=\frac{n!}{s^{n+1}}$ for $\Re(s)>0$.  Alternatively, start from $u(t)\leftrightarrow\frac{1}{s}$ and repeatedly apply $\mathcal{L}\{t f(t)\}=-\frac{dF}{ds}$.
- $\sin(\omega_0 t)u(t)$: write $\sin(\omega_0 t)=\frac{e^{j\omega_0 t}-e^{-j\omega_0 t}}{2j}$, transform the two exponentials, combine to get $\frac{\omega_0}{s^2+\omega_0^2}$.
- $\cos(\omega_0 t)u(t)$: write $\cos(\omega_0 t)=\frac{e^{j\omega_0 t}+e^{-j\omega_0 t}}{2}$, transform and combine to get $\frac{s}{s^2+\omega_0^2}$.

Fourier comparison: $\delta(t)\leftrightarrow 1$ matches Fourier exactly.  For $e^{-\alpha t}u(t)$ with $\alpha>0$, evaluating the Laplace transform on the imaginary axis gives $\frac{1}{\alpha+j\omega}$ because the ROC includes $j\omega$.  By contrast, $u(t)$, $t^n u(t)$, and causal sinusoids require generalized-function treatment in Fourier analysis.

Core properties, each with a short derivation idea:

- __Linearity__: pull constants through the integral and split sums termwise.
- __Time shift (bilateral)__: $\mathcal{L}_b\{f(t-t_0)\}=e^{-st_0}F_b(s)$, by substituting $\tau=t-t_0$.
- __Time shift (unilateral)__: for delay by $t_0>0$, $\mathcal{L}_u\{f(t-t_0)u(t-t_0)\}=e^{-st_0}F_u(s)$; the factor $u(t-t_0)$ is essential.  For advance by $t_0>0$, the shift is not symmetric:

$\mathcal{L}_u\{f(t+t_0)u(t)\}=e^{st_0}\!\left[F_u(s)-\int_{0^-}^{t_0^-} f(\tau)e^{-s\tau}\,d\tau\right]$

- __$s$-domain shift__: $\mathcal{L}\{e^{-\alpha t}f(t)\}=F(s+\alpha)$, by combining exponentials in the kernel.
- __Scaling__ ($a>0$): $\mathcal{L}\{f(at)\}=\frac{1}{a}F\!\left(\frac{s}{a}\right)$, by substituting $\tau=at$.
- __Convolution theorem__: $\mathcal{L}\{f_1*f_2\}=F_1(s)F_2(s)$, same syntax as Fourier after $j\omega\to s$.  Derivation cue: insert $(f_1*f_2)(t)=\int f_1(\tau)f_2(t-\tau)d\tau$, swap integration order, separate factors.  The Laplace difference is ROC bookkeeping: valid on the intersection of the two ROCs, and pole-zero cancellation can enlarge the final ROC.
- __Multiplication theorem (bilateral)__: time-domain multiplication maps to complex contour convolution in the $s$-plane:

$\mathcal{L}_b\{f(t)g(t)\}(s)=\frac{1}{2\pi j}\int_{\gamma-j\infty}^{\gamma+j\infty}F(\sigma)G(s-\sigma)\,d\sigma$,

where $\Re(\sigma)=\gamma$ stays inside valid ROCs.  In practice, this is much less convenient than the convolution theorem.

- __Multiplication theorem (unilateral)__: for causal signals, treat as bilateral multiplication of $f(t)u(t)$ and $g(t)u(t)$.  No simpler course-default product formula is routinely used in ELEC 2100.

Whenever a property combines several transforms, the derivation is first justified on the intersection of the participating ROCs.  Only after simplification can pole-zero cancellation enlarge the final ROC.

For derivatives and integrals, compare bilateral and unilateral.

- __Bilateral differentiation__: $\mathcal{L}_b\{f'(t)\}=sF(s)$, provided $f(t)e^{-st}\to0$ at both $t\to\pm\infty$ within ROC.
- __Unilateral differentiation__:

$\mathcal{L}_u\{f'(t)\}=sF(s)-f(0^-)$.

Derivation: define $x(t)=f(t)u(t)$, so $X(s)=F(s)$.  Differentiate: $\frac{d}{dt}[f(t)u(t)]=f'(t)u(t)+f(0^-)\delta(t)$.  Take bilateral Laplace of both sides: $sF(s)=\mathcal{L}_u\{f'(t)\}+f(0^-)$, giving the rule.  Intuition: multiplying by $u(t)$ creates a boundary at $t=0$; differentiation of that boundary contributes the impulse term, which becomes the $f(0^-)$ correction.

- __Repeated differentiation__: bilateral keeps the Fourier-like pattern $\mathcal{L}_b\{f^{(n)}(t)\}=s^nF_b(s)$.  Unilateral records every initial derivative:

$\mathcal{L}_u\{f^{(n)}(t)\}=s^nF(s)-\sum_{k=0}^{n-1}s^{n-1-k}f^{(k)}(0^-)$.

This is obtained by applying the first-derivative rule recursively.

- __Bilateral integration__: $\mathcal{L}_b\{g(t)\}=F_b(s)/s$, same syntax as Fourier after $j\omega\to s$.
- __Unilateral integration__ with $g(t)=\int_{0^-}^{t}f(\tau)d\tau$:

$\mathcal{L}_u\{g(t)\}=\frac{F(s)}{s}$.

More generally, if $g'(t)=f(t)$, then $G(s)=\frac{F(s)+g(0^-)}{s}$.  The common formula $F(s)/s$ is the special case $g(0^-)=0$.  Intuition: a causal integrator contributes $1/s$; any nonzero pre-existing stored value contributes $g(0^-)/s$.

- __Repeated integration__: for unilateral $n$-fold causal integration with zero initial primitives, $\mathcal{L}_u\{g_n(t)\}=\frac{F(s)}{s^n}$.  More generally, if $g_n^{(n)}(t)=f(t)$:

$G_n(s)=\frac{F(s)+\sum_{k=0}^{n-1}s^{n-1-k}g_n^{(k)}(0^-)}{s^n}$.

This gives the bilateral-vs-unilateral/Fourier comparison: the syntactic rule form is mostly the same as Fourier after $j\omega\to s$, but the differences are ROC constraints, endpoint/boundary terms, and unilateral initial-condition terms.

The initial and final value theorems are:

$f(0^+)=\lim_{s\to\infty}sF(s),\qquad f(\infty)=\lim_{s\to0}sF(s)$.

The kernel intuition: $sF(s)=\int_{0}^{\infty} f\!\left(\frac{u}{s}\right)e^{-u}\,du$.  As $s\to\infty$, the kernel concentrates near $t=0^+$; as $s\to0^+$, it samples the long-time tail.  For the IVT, this requires no impulsive component at the origin; for rational transforms, strict properness of $F(s)$ is a sufficient check.  For the FVT, all poles of $sF(s)$ must lie strictly in the open left half-plane.

If conditions are violated: IVT fails when impulses or distributional terms are present at $t=0$; FVT fails for RHP poles (growth), imaginary-axis poles (non-settling oscillation), or repeated poles at the origin (ramp-like divergence).

The proper-fraction caveat: if $F(s)$ is not proper, first do polynomial long division $F(s)=P(s)+F_1(s)$.  The polynomial part corresponds to impulses at $t=0$; the ordinary initial value must be read from the proper remainder: $f(0^+)=\lim_{s\to\infty}sF_1(s)$.

---

Flashcards for this section are as follows:

- State the six common unilateral Laplace pairs and their ROCs. ::@:: $u(t)\leftrightarrow\frac{1}{s}$ ($\Re(s)>0$); $e^{-\alpha t}u(t)\leftrightarrow\frac{1}{s+\alpha}$ ($\Re(s)>-\alpha$); $\delta(t)\leftrightarrow 1$; $t^n u(t)\leftrightarrow\frac{n!}{s^{n+1}}$ ($\Re(s)>0$); $\sin(\omega_0 t)u(t)\leftrightarrow\frac{\omega_0}{s^2+\omega_0^2}$ ($\Re(s)>0$); $\cos(\omega_0 t)u(t)\leftrightarrow\frac{s}{s^2+\omega_0^2}$ ($\Re(s)>0$).
- How are the sinusoidal pairs derived from the exponential form? ::@:: Write $\sin(\omega_0 t)=\frac{e^{j\omega_0 t}-e^{-j\omega_0 t}}{2j}$ (or cosine with $+$), transform the two exponentials, and combine.
- Which common Laplace pairs also match Fourier directly, and which require Fourier boundary treatment? ::@:: $\delta(t)\leftrightarrow1$ matches directly, and $e^{-\alpha t}u(t)$ with $\alpha>0$ reduces to $\frac{1}{\alpha+j\omega}$ on the imaginary axis.  $u(t)$, $t^n u(t)$, and causal sinusoids require generalized-function treatment in Fourier.
- What is the one-line derivation idea for Laplace linearity? ::@:: Start from $\mathcal{L}\{a f+b g\}=\int (a f+b g)e^{-st}dt$ and split the integral termwise.
- How do bilateral and unilateral time shifts differ? ::@:: Bilateral delay/advance are pure factors: $e^{\mp st_0}F_b(s)$.  Unilateral delay by $t_0>0$ is also a pure factor $e^{-st_0}F_u(s)$, but unilateral advance adds a correction term: $\mathcal{L}_u\{f(t+t_0)u(t)\}=e^{st_0}[F_u(s)-\int_{0^-}^{t_0^-}f(\tau)e^{-s\tau}d\tau]$.
- How is the $s$-domain shift rule derived? ::@:: Combine exponentials: $e^{-\alpha t}e^{-st}=e^{-(s+\alpha)t}$, so the transform is $F$ evaluated at $s+\alpha$.
- How is the scaling rule derived? ::@:: Substitute $\tau=at$ in $\int f(at)e^{-st}dt$; then $dt=d\tau/a$ and $e^{-st}=e^{-(s/a)\tau}$.
- Compare the Laplace and Fourier convolution theorems. ::@:: Syntactically they match after $j\omega\to s$.  For Laplace, the extra issue is ROC bookkeeping: valid on the intersection of participating ROCs.
- Compare bilateral and unilateral differentiation rules. ::@:: Bilateral: $\mathcal{L}_b\{f'(t)\}=sF_b(s)$ (boundary terms vanish).  Unilateral first: $\mathcal{L}_u\{f'(t)\}=sF(s)-f(0^-)$.  Unilateral $n$th: $\mathcal{L}_u\{f^{(n)}(t)\}=s^nF(s)-\sum_{k=0}^{n-1}s^{n-1-k}f^{(k)}(0^-)$.
- Compare bilateral and unilateral integration rules. ::@:: Bilateral: $\mathcal{L}_b\{g(t)\}=F_b(s)/s$.  Unilateral: $G(s)=\frac{F(s)+g(0^-)}{s}$.  The common formula $F(s)/s$ is the special case $g(0^-)=0$.
- State the concise initial and final value theorems with conditions. ::@:: IVT: $f(0^+)=\lim_{s\to\infty}sF(s)$, valid when $f$ has no impulse at $t=0$; for rational transforms, strict properness suffices.  FVT: $\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$, valid when the time limit exists and all poles of $sF(s)$ lie strictly in the open left half-plane.
- What kernel intuition explains the IVT and FVT conditions? ::@:: $sF(s)=\int_{0}^{\infty} f(\frac{u}{s})e^{-u}\,du$: as $s\to\infty$, the kernel concentrates near $t=0^+$; as $s\to0^+$, it samples the long-time tail.  RHP poles cause growth, imaginary-axis poles cause oscillation, and repeated origin poles cause divergence.

- Why must an improper rational $F(s)$ be split before applying IVT? ::@:: The polynomial part corresponds to impulses at $t=0$; $sP(s)$ diverges as $s\to\infty$, so a naive limit gives the wrong result.  Write $F(s)=P(s)+F_1(s)$ and apply IVT only to the proper remainder.
- Why are complex-conjugate poles handled as a pair during inverse Laplace? ::@:: To produce real damped sinusoid expressions directly and avoid unnecessary complex-arithmetic detours.
- State the bilateral Laplace multiplication theorem, and explain why it is less convenient than convolution. ::@:: $\mathcal{L}_b\{f(t)g(t)\}(s)=\frac{1}{2\pi j}\int_{\gamma-j\infty}^{\gamma+j\infty}F(\sigma)G(s-\sigma)\,d\sigma$.  Unlike Fourier's ordinary frequency-axis convolution, Laplace uses a complex vertical-contour convolution whose contour must stay inside valid ROCs.  That ROC/contour bookkeeping makes it much less convenient than $f_1*f_2\leftrightarrow F_1F_2$.

## inverse Laplace transform by partial fractions

ELEC 2100 uses three inverse-Laplace routes:

1. __Contour inversion via the Bromwich integral__: the definition-level method using contour integration and the residue theorem.
2. __Partial fraction expansion + table lookup__: the main hand-computation technique for proper rational transforms.
3. __Computer-aided inversion__: tools such as MATLAB for checking algebra or handling higher-order expressions.

Method 2 is the default computational shortcut, method 1 supplies the contour justification, and method 3 is a verification aid.

Partial-fraction expansion applies when $F(s)=\frac{N(s)}{D(s)}$ is __rational__ and __proper__: $\deg N<\deg D$.  If improper, first do polynomial long division: $F(s)=P(s)+F_{\text{proper}}(s)$.  The polynomial part corresponds to impulses at $t=0$; the proper remainder is handled by partial fractions.

The workflow:

1. make the rational function proper;
2. factor the denominator over the reals;
3. identify poles and their multiplicities;
4. write the correct decomposition template;
5. solve coefficients;
6. map each term to a standard inverse-Laplace pair;
7. combine complex-conjugate poles into real damped cosine/sine form;
8. check by recombination or pole/order consistency.

The standard templates are as follows.

- __Distinct real poles__: if $F(s)=\frac{N(s)}{(s-p_1)(s-p_2)\cdots(s-p_n)}$ with distinct real poles $p_k$, then

$F(s)=\sum_{k=1}^{n}\frac{A_k}{s-p_k}$.

- __Repeated pole__: if $p$ is a pole of order $r$, then the contribution takes the ladder form

$\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$.

- __Irreducible quadratic / complex-conjugate pair__: for a real quadratic factor $(s-\alpha)^2+\omega^2$, use a linear numerator,

$\frac{Bs+C}{(s-\alpha)^2+\omega^2}$,

or more conveniently rewrite the numerator as $B(s-\alpha)+C$ so the cosine and sine pairs appear directly.

Coefficient-solving tricks:

- __Heaviside cover-up__ for a simple pole $p_k$: $A_k=(s-p_k)F(s)\big|_{s=p_k}$.
- __Coefficient comparison__: multiply through by the common denominator, expand, then compare powers of $s$.
- __Differentiation for repeated poles__: if $p$ has order $r$, then $A_r=(s-p)^rF(s)\big|_{s=p}$, and $A_{r-k}=\frac{1}{k!}\frac{d^k}{ds^k}\!\left[(s-p)^rF(s)\right]\big|_{s=p}$ for $k=0,1,\ldots,r-1$.

The inverse-transform table then turns pole structure into time-domain modes:

- $\frac{1}{s-p}\longleftrightarrow e^{pt}u(t)$;
- $\frac{1}{(s-p)^k}\longleftrightarrow \frac{t^{k-1}}{(k-1)!}e^{pt}u(t)$;
- $\frac{s-\alpha}{(s-\alpha)^2+\omega^2}\longleftrightarrow e^{\alpha t}\cos(\omega t)u(t)$;
- $\frac{\omega}{(s-\alpha)^2+\omega^2}\longleftrightarrow e^{\alpha t}\sin(\omega t)u(t)$.

### representative cases

__Example 1: distinct real poles.__ Let $F(s)=\frac{s+1}{(s+2)(s+3)}$.  The poles are $-2$ and $-3$, so write

$F(s)=\frac{k_1}{s+2}+\frac{k_2}{s+3}$.

Cover-up gives $k_1=(s+2)F(s)\big|_{s=-2}=-1$ and $k_2=(s+3)F(s)\big|_{s=-3}=2$.  Therefore

$F(s)=\frac{-1}{s+2}+\frac{2}{s+3}$,

so

$f(t)=(-e^{-2t}+2e^{-3t})u(t)$.

__Example 2: complex-conjugate poles.__ Let $F(s)=\frac{s+2}{(s+1)^2+4}$.  The poles are $-1\pm 2j$.  Rewrite the numerator as $s+2=(s+1)+1$, so

$F(s)=\frac{s+1}{(s+1)^2+4}+\frac{1}{(s+1)^2+4}$.

Now match directly with the cosine/sine pairs:

$f(t)=e^{-t}\cos(2t)u(t)+\frac{1}{2}e^{-t}\sin(2t)u(t)$.

This example shows why conjugate poles should be treated together: the paired real form avoids unnecessary complex arithmetic.

__Example 3: repeated pole.__ Let $F(s)=\frac{2s+3}{(s+1)^2(s+2)}$.  The pole at $-1$ has multiplicity $2$, so write

$F(s)=\frac{A}{s+2}+\frac{B}{s+1}+\frac{C}{(s+1)^2}$.

The highest repeated-pole coefficient is $C=(s+1)^2F(s)\big|_{s=-1}=1$.

Cover-up at the simple pole gives $A=(s+2)F(s)\big|_{s=-2}=-1$.

There are then two clean ways to find the lower-order coefficient $B$.

__Method 1: differentiation.__ Let $G(s)=(s+1)^2F(s)=\frac{2s+3}{s+2}$.  Since the repeated pole has order $2$, the previous formula gives $B=\frac{d}{ds}G(s)\big|_{s=-1}$.  Differentiate:

$G'(s)=\frac{2(s+2)-(2s+3)}{(s+2)^2}=\frac{1}{(s+2)^2}$,

so $B=G'(-1)=1$.

__Method 2: coefficient comparison.__ Multiply through by $(s+1)^2(s+2)$:

$2s+3=A(s+1)^2+B(s+1)(s+2)+C(s+2)$.

Substituting $A=-1$ and $C=1$ gives $2s+3=-(s+1)^2+B(s+1)(s+2)+(s+2)$.  Expand the right-hand side:

$2s+3=(B-1)s^2+(3B-1)s+(2B+1)$.

Now compare coefficients of equal powers of $s$.  The left-hand side has zero $s^2$ coefficient, so $B-1=0$, giving $B=1$.  (The constant term also checks: $2(1)+1=3$.)  Therefore

$F(s)=\frac{-1}{s+2}+\frac{1}{s+1}+\frac{1}{(s+1)^2}$,

so

$f(t)=(-e^{-2t}+e^{-t}+te^{-t})u(t)$.

Intuitively, partial fractions works because a proper rational transform can be decomposed into a sum of simpler pole-generated building blocks.  Under inverse Laplace, each block becomes one basic time-domain mode: a simple pole gives an exponential, a repeated pole gives polynomial-times-exponential behavior, and a complex-conjugate pair gives a damped sinusoid.  So partial fractions is really a modal decomposition of the response.

There is also a useful linear-algebra viewpoint.  Once the denominator factorization is fixed, all proper rational functions with that denominator form a finite-dimensional vector space after reduction, and the partial-fraction terms act like a basis for that space.  Solving for the coefficients is then just finding the coordinates of $F(s)$ in that basis.  Under inverse Laplace, those basis functions become the familiar time-domain modes $e^{pt}u(t)$, $te^{pt}u(t)$, and damped sinusoids.

---

Flashcards for this section are as follows:

- What are the three inverse-Laplace methods in ELEC 2100? ::@:: (1) Bromwich contour inversion with residues.  (2) Partial fractions + table lookup (main hand method).  (3) Computer-aided tools such as MATLAB (verification).
- Before applying partial fractions, what prerequisite must be checked? ::@:: Properness: $\deg N<\deg D$.  If improper, first do polynomial long division.
- What is the full partial-fraction workflow? ::@:: Make proper → factor denominator → identify poles/multiplicities → write template → solve coefficients → map via table → combine conjugate pairs → check.
- What templates are used for distinct poles, repeated poles, and irreducible quadratics? ::@:: Distinct: $\sum_k \frac{A_k}{s-p_k}$.  Repeated at $p$ order $r$: $\frac{A_1}{s-p}+\cdots+\frac{A_r}{(s-p)^r}$.  Quadratic: $\frac{Bs+C}{(s-\alpha)^2+\omega^2}$ or $\frac{B(s-\alpha)+C}{(s-\alpha)^2+\omega^2}$.
- What are the coefficient-solving tricks? ::@:: Cover-up for simple poles, coefficient comparison after clearing denominators, differentiation for repeated poles.
- For a repeated pole $p$ of order $r$, how are coefficients extracted? ::@:: Highest: $A_r=(s-p)^rF(s)|_{s=p}$.  General: $A_{r-k}=\frac{1}{k!}\frac{d^k}{ds^k}[(s-p)^rF(s)]|_{s=p}$ for $k=0,\ldots,r-1$.
- For $F(s)=\frac{s+2}{(s+1)^2+4}$, why rewrite the numerator as $(s+1)+1$? ::@:: To expose the standard cosine/sine numerators: $F(s)=\frac{s+1}{(s+1)^2+4}+\frac{1}{(s+1)^2+4}$, giving $f(t)=e^{-t}\cos(2t)u(t)+\frac{1}{2}e^{-t}\sin(2t)u(t)$.
- For $F(s)=\frac{2s+3}{(s+1)^2(s+2)}$, what is the partial-fraction form and inverse Laplace? ::@:: $\frac{A}{s+2}+\frac{B}{s+1}+\frac{C}{(s+1)^2}$ with $A=-1$, $B=1$, $C=1$, giving $f(t)=(-e^{-2t}+e^{-t}+te^{-t})u(t)$.

## applications of Laplace transform

The main application payoff: start from a physical model, move to an algebraic equation in $s$, read a response transform or transfer function, interpret poles, damping, and stability, then return to time domain.

The recurring application chain:

physical model $\to$ initial conditions and constitutive laws $\to$ $s$-domain equivalent model or transformed differential equation $\to$ algebraic solve in $s$ $\to$ response transform or transfer function $\to$ pole/stability interpretation $\to$ inverse Laplace transform.

Standard examples are a series RLC circuit and a coupled electromechanical DC motor.  Laplace transform replaces coupled differential equations by algebraic relations while preserving the same input-output physics.

---

Flashcards for this section are as follows:

- What is the recurring Laplace-transform application chain? ::@:: Physical model $\to$ initial conditions/constitutive laws $\to$ $s$-domain model $\to$ algebraic solve $\to$ response transform/transfer function $\to$ pole/stability interpretation $\to$ inverse Laplace.

### analysis of dynamic circuits in Laplace domain

Two equivalent starting points:

1. Write the time-domain differential/integral equation, then transform.
2. Draw the $s$-domain equivalent circuit directly, then write KVL/KCL there.

ELEC 2100 mainly uses route 2 because it keeps the circuit structure visible.

To draw the $s$-domain model: keep the same topology, switch position, and reference directions.  Relabel signals by their Laplace transforms and replace each element by its $s$-domain counterpart.  The $s$-domain model is the same circuit skeleton, with branches labeled by $V(s)$, $I(s)$, and element transfer relations.

Basic element models:

- resistor: $V_R(s)=RI_R(s)$;
- inductor: $V_L(s)=LsI_L(s)-L i_L(0^-)$;
- capacitor: $V_C(s)=\frac{1}{sC}I_C(s)+\frac{v_C(0^-)}{s}$.

So a resistor stays $R$; an inductor becomes impedance $Ls$ plus a source $L i_L(0^-)$; a capacitor becomes impedance $\frac{1}{sC}$ plus a source $\frac{v_C(0^-)}{s}$.  With zero initial conditions, the extra sources vanish.

KCL and KVL keep the same form: $\sum I(s)=0$ and $\sum V(s)=0$.

The workflow: determine $i_L(0^-)$ and $v_C(0^-)$ from the $t=0^-$ circuit → draw the $t>0$ $s$-domain equivalent → write algebraic KVL/KCL → solve for $I(s)$ or $V(s)$ → inverse-transform and interpret the pole pattern.

__Example: zero-state series RLC excited by a DC step.__ Let the source be $E u(t)$, so in the $s$-domain the source is $\frac{E}{s}$.  With zero initial conditions, the series loop contains the impedances $R$, $Ls$, and $\frac{1}{sC}$, so KVL gives

$\frac{E}{s}=\left(R+Ls+\frac{1}{sC}\right)I(s)$.

Hence

$I(s)=\frac{E}{Ls^2+Rs+\frac{1}{C}}=\frac{E/L}{s^2+\frac{R}{L}s+\frac{1}{LC}}$.

If the poles are written as $p_{1,2}$, then

$I(s)=\frac{E/L}{(s-p_1)(s-p_2)}$.

Now define

$\alpha=\frac{R}{2L},\qquad \omega_0=\frac{1}{\sqrt{LC}},\qquad p_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$.

The damping classes are then read from the pole locations.

- __Undamped__: $R=0$, so $\alpha=0$ and $p_{1,2}=\pm j\omega_0$.
- __Underdamped__: $\alpha<\omega_0$, so the poles are complex-conjugate.
- __Critically damped__: $\alpha=\omega_0$, so the poles coincide.
- __Overdamped__: $\alpha>\omega_0$, so the poles are distinct real negatives.

Rewriting the same denominator in the standard second-order form

$s^2+2\zeta\omega_0 s+\omega_0^2$,

where $\zeta=\frac{\alpha}{\omega_0}$ is the damping ratio.  In that notation:

- $\zeta=0$ gives the undamped poles $\pm j\omega_0$;
- $0<\zeta<1$ gives underdamped poles $-\zeta\omega_0\pm j\omega_d$, where $\omega_d=\omega_0\sqrt{1-\zeta^2}$;
- $\zeta=1$ gives the repeated real pole $-\omega_0$;
- $\zeta>1$ gives two distinct real poles $-\zeta\omega_0\pm \omega_0\sqrt{\zeta^2-1}$.

Note that $\omega_d$ is __not__ the same thing as $\omega_0$.  The underdamped oscillation frequency is

$\omega_d=\omega_0\sqrt{1-\zeta^2}=\sqrt{\omega_0^2-\alpha^2}$,

while $\omega_0=\frac{1}{\sqrt{LC}}$ is the undamped natural frequency.  Likewise, in the overdamped case the square-root term is a real number $\omega_0\sqrt{\zeta^2-1}$, not $\omega_0$ itself.

The inverse Laplace result now follows the damping case.

- __Underdamped__: since $I(s)=\frac{E/L}{(s+\alpha)^2+\omega_d^2}$ after completing the square, the current is

$i(t)=\frac{E}{L\omega_d}e^{-\alpha t}\sin(\omega_d t)u(t)$.

- __Critically damped__: with $I(s)=\frac{E/L}{(s+\alpha)^2}$, the current is

$i(t)=\frac{E}{L}t e^{-\alpha t}u(t)$.

- __Overdamped__: for two distinct poles,

$i(t)=\frac{E}{L(p_1-p_2)}\left(e^{p_1 t}-e^{p_2 t}\right)u(t)$.

- __Undamped__: with $R=0$ and poles $\pm j\omega_0$,

$i(t)=\frac{E}{L\omega_0}\sin(\omega_0 t)u(t)$.

Unilateral Laplace transform preserves initial conditions, converts the dynamic circuit into an algebraic $s$-domain circuit, and lets the pole pattern classify the response.

---

Flashcards for this section are as follows:

- When analyzing a dynamic circuit with Laplace transform, what are the two starting routes, and which is used most? ::@:: Route 1: write the time-domain equation first, then transform.  Route 2: draw the $s$-domain equivalent directly, then write KVL/KCL.  ELEC 2100 mainly uses route 2.
- How should you draw the $s$-domain model? ::@:: Keep the same topology, $t>0$ switch position, and reference directions.  Replace variables by $V(s), I(s)$, sources by their transforms, and elements by their $s$-domain models with initial-condition sources.
- What are the unilateral $s$-domain element models for $R$, $L$, and $C$? ::@:: $V_R=RI_R$, $V_L=LsI_L-Li_L(0^-)$, $V_C=\frac{1}{sC}I_C+\frac{v_C(0^-)}{s}$.
- Why do KCL and KVL still work in the $s$-domain? ::@:: Laplace transform converts linear differential/integral element laws into algebraic relations without changing the circuit topology.
- What is the dynamic-circuit workflow? ::@:: Find $i_L(0^-)$ and $v_C(0^-)$ from the $t=0^-$ circuit $\to$ draw $s$-domain equivalent $\to$ write algebraic KVL/KCL $\to$ solve for $I(s)$ or $V(s)$ $\to$ inverse-transform and interpret poles.
- For a zero-state series RLC driven by $E u(t)$, what is the KVL and resulting current transform? ::@:: KVL: $\frac{E}{s}=(R+Ls+\frac{1}{sC})I(s)$.  Hence $I(s)=\frac{E/L}{s^2+\frac{R}{L}s+\frac{1}{LC}}$.
- What are $\alpha$, $\omega_0$, and poles for the series-RLC denominator? ::@:: $\alpha=\frac{R}{2L}$, $\omega_0=\frac{1}{\sqrt{LC}}$, $p_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$.
- How are the four damping cases described using $\zeta$? ::@:: $\zeta=0$: undamped ($\pm j\omega_0$).  $0<\zeta<1$: underdamped ($-\zeta\omega_0\pm j\omega_d$).  $\zeta=1$: critically damped ($-\omega_0$).  $\zeta>1$: overdamped.
- What notation pitfall must be avoided? ::@:: The oscillation frequency is $\omega_d=\omega_0\sqrt{1-\zeta^2}$, not $\omega_0$ itself.
- What are the current forms for the four damping cases? ::@:: Underdamped: $\frac{E}{L\omega_d}e^{-\alpha t}\sin(\omega_d t)u(t)$.  Critically damped: $\frac{E}{L}te^{-\alpha t}u(t)$.  Overdamped: $\frac{E}{L(p_1-p_2)}(e^{p_1 t}-e^{p_2 t})u(t)$.  Undamped: $\frac{E}{L\omega_0}\sin(\omega_0 t)u(t)$.

### transfer-function viewpoint and routes

The other major application is building system functions and transfer functions.  The detailed material lives in [transfer function](transfer%20function.md); this note keeps only the application bridge.

For zero-state LTI analysis,

$H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$.

So the same Laplace algebra used to solve a single response also gives the system description.  The main questions become: what excitation-response pair defines $H(s)$; how poles and zeros are arranged; how cascade, parallel, and feedback interconnections change $H(s)$; what pole locations say about stability.

A standard example is a DC motor with voltage input $v(t)$, armature current $i(t)$, and shaft speed $\omega(t)$ satisfying

$L\frac{di}{dt}+Ri+K_b\omega=v(t),\qquad J\frac{d\omega}{dt}+b\omega=K_t i(t)$.

With zero initial conditions, Laplace transform gives

$(Ls+R)I(s)+K_b\Omega(s)=V(s),\qquad (Js+b)\Omega(s)=K_t I(s)$.

Eliminating $I(s)$ yields the speed plant

$G_\omega(s)=\frac{\Omega(s)}{V(s)}=\frac{K_t}{(Ls+R)(Js+b)+K_tK_b}$,

and since $\Theta(s)=\frac{\Omega(s)}{s}$, the position plant is

$G_\theta(s)=\frac{\Theta(s)}{V(s)}=\frac{K_t}{s[(Ls+R)(Js+b)+K_tK_b]}$.

That example shows the full chain: physical laws → algebraic equations in $s$ → transfer function → pole/stability analysis → feedback design language.

The quick stability rule: for a causal rational system, all poles strictly in the left half-plane imply asymptotic BIBO stability.  Simple poles on the imaginary axis give marginal behavior; any RHP pole or repeated imaginary-axis pole gives instability.

---

Flashcards for this section are as follows:

- What does $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$ mean? ::@:: The zero-state input-output ratio equals the Laplace transform of the impulse response, so the same framework describes both a single response and the system itself.
- What transfer functions does the DC motor example produce? ::@:: Speed: $G_\omega(s)=\frac{K_t}{(Ls+R)(Js+b)+K_tK_b}$.  Position: $G_\theta(s)=\frac{K_t}{s[(Ls+R)(Js+b)+K_tK_b]}$.
- Where should the full transfer-function material be studied? ::@:: In [transfer function](transfer%20function.md).  This note keeps the application bridge.
- What is the quick causal-rational stability rule? ::@:: All poles strictly in the left half-plane imply asymptotic BIBO stability; simple poles on the imaginary axis give marginal behavior; any RHP pole or repeated imaginary-axis pole gives instability.

## relation between Laplace transform and Fourier transform

Laplace and Fourier are connected syntactically, operationally, and semantically.

__Syntactic connection.__ The bilateral Laplace transform $F(s)$ is obtained from the Fourier transform by substituting $j\omega\to s$.  Evaluating at $s=j\omega$ recovers the Fourier transform when the imaginary axis lies in the ROC.

__Operational connection.__ The right-sided unilateral transform equals the bilateral Laplace of the windowed signal $f(t)u(t)$: $\mathcal{L}_u\{f\}(s)=\mathcal{L}_{bilateral}\{f(t)u(t)\}(s)$.  Operationally: (1) multiply by $u(t)$, (2) apply bilateral Laplace.  Symmetrically, the left-sided transform uses $u(-t)$.

__Semantic connection.__ Writing $s=\sigma+j\omega$, $F(\sigma+j\omega)=\mathcal{F}\{f(t)e^{-\sigma t}\}(\omega)$: the Laplace transform at $s=\sigma+j\omega$ is the Fourier transform of the exponentially weighted signal.  The real part $\sigma$ controls an exponential weight: $\sigma>0$ decays forward in time, expanding the class of transformable signals; $\sigma=0$ reduces to ordinary Fourier; $\sigma<0$ grows forward in time.  The ROC is the vertical strip for which $f(t)e^{-\sigma t}$ is Fourier-transformable.

__Why Fourier has duality but Laplace generally does not.__ Fourier has a genuine duality theorem because its kernel is symmetric between time and frequency.  Laplace loses that symmetry: exponential weighting changes convergence, the ROC must be tracked, and unilateral Laplace adds boundary/initial-condition terms.

__Recovery of Fourier transform, ROC cases, and impulse corrections.__ The test $F(j\omega)=F(s)\vert_{s=j\omega}$ has three cases:

- __Imaginary axis inside the ROC__: ordinary Fourier exists, obtained by direct substitution.  Example: $e^{-\alpha t}u(t)$ with $\alpha>0$ has $F(s)=\frac{1}{s+\alpha}$ with ROC $\Re\{s\}>-\alpha$, so $\hat f(\omega)=\frac{1}{\alpha+j\omega}$.
- __Imaginary axis outside the ROC__: no classical Fourier exists.  Example: $e^{\alpha t}u(t)$ with $\alpha>0$ has ROC $\Re\{s\}>\alpha$, so $F(j\omega)$ is invalid.
- __Imaginary axis on the ROC boundary__: approach from inside the ROC to get a generalized Fourier transform with principal-value and impulse terms.

The unit step is the canonical boundary example: $F(s)=\frac{1}{s}$ with ROC $\Re\{s\}>0$.  Approaching the boundary gives $\mathcal{F}\{u(t)\}=\pi\delta(\omega)+\operatorname{PV}\!\left(\frac{1}{j\omega}\right)$.

The shifted simple-pole rule: if $F(s)$ has a boundary pole $\frac{R}{s-j\omega_0}$, the boundary limit gives $\operatorname{PV}\!\left(\frac{R}{j(\omega-\omega_0)}\right)+\pi R\,\delta(\omega-\omega_0)$.  So a first-order imaginary-axis pole contributes both a principal-value term and an impulse whose coefficient is $\pi$ times the residue.

Repeated boundary poles: an order-$m$ pole $\frac{a_m}{(s-j\omega_0)^m}$ contributes $\operatorname{PV}\!\left(\frac{a_m}{[j(\omega-\omega_0)]^m}\right)+\frac{\pi a_m}{(m-1)!(-j)^{m-1}}\,\delta^{(m-1)}(\omega-\omega_0)$.

The recovery rule: locate the imaginary axis relative to the ROC, separate boundary-pole principal parts, and write the generalized Fourier transform as the ordinary $F(j\omega)$ plus principal-value limits plus impulse corrections.

---

Flashcards for this section are as follows:

- How does the bilateral Laplace transform relate syntactically to Fourier? ::@:: $F(s)=\hat f(\omega)|_{j\omega\to s}$.  Evaluating at $s=j\omega$ recovers $\hat f(\omega)$ when the imaginary axis is in the ROC.
- How is the unilateral Laplace transform expressed as a two-step bilateral procedure? ::@:: Step 1: multiply $f(t)$ by $u(t)$ to zero out $t<0$.  Step 2: apply bilateral Laplace.  Result: $\mathcal{L}_u\{f\}(s)=\mathcal{L}_{bilateral}\{f(t)u(t)\}(s)$.
- What is the semantic meaning of $F(\sigma+j\omega)$? ::@:: $F(\sigma+j\omega)=\mathcal{F}\{f(t)e^{-\sigma t}\}(\omega)$: the Laplace transform is the Fourier transform of the exponentially weighted signal.
- What are the three cases for recovering Fourier from $F(s)$? ::@:: Imaginary axis inside ROC: ordinary Fourier via direct substitution.  Outside ROC: no classical Fourier.  On ROC boundary: generalized Fourier with principal-value and impulse terms.
- Why does $e^{\alpha t}u(t)$ with $\alpha>0$ have Laplace but no Fourier transform? ::@:: Its ROC $\Re\{s\}>\alpha$ excludes the imaginary axis, so $F(j\omega)$ is invalid.
- Derive $\mathcal{F}\{u(t)\}$ from the boundary limit of $F(s)=\frac{1}{s}$. ::@:: Approach the boundary: $\frac{1}{\sigma+j\omega}=\frac{\sigma}{\sigma^2+\omega^2}-j\frac{\omega}{\sigma^2+\omega^2}$.  As $\sigma\to0^+$, the real part (Poisson kernel) tends to $\pi\delta(\omega)$, the imaginary part tends to $\operatorname{PV}(\frac{1}{j\omega})$.  Hence $\mathcal{F}\{u(t)\}=\pi\delta(\omega)+\operatorname{PV}(\frac{1}{j\omega})$.
- If $F(s)$ has a simple boundary pole $\frac{R}{s-j\omega_0}$, what Fourier correction appears? ::@:: $\operatorname{PV}(\frac{R}{j(\omega-\omega_0)})+\pi R\,\delta(\omega-\omega_0)$.
- Why is there no standard Laplace duality theorem? ::@:: Fourier has true time-frequency symmetry; Laplace does not, because exponential weighting changes convergence, ROC must be tracked, and unilateral Laplace adds boundary terms.

## inverse Laplace transform via Bromwich integral

The inversion formula is the __Bromwich contour integral__: $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}\,ds$, where $\sigma$ is any value within the ROC.

Different choices of $\sigma$ within the ROC yield the same $f(t)$ by the Cauchy integral theorem: $F(s)$ is analytic in the ROC interior, so shifting the vertical contour within that region does not change the integral.

When the imaginary axis lies in the ROC, set $\sigma=0$ and substitute $s=j\omega$ to recover the inverse Fourier transform.

For a rational $F(s)$ with a right-sided ROC, the practical residue workflow:

1. Choose the Bromwich line to the right of all finite poles.
2. For $t>0$, close the contour with a left semicircle $\Gamma_R$ and let $R\to\infty$.  On $\Gamma_R$, $e^{st}$ decays and $F(s)=O(1/R)$, so the arc integral vanishes by Jordan's lemma.
3. The Bromwich integral equals $2\pi j$ times the sum of residues of $F(s)e^{st}$ at the enclosed poles.
4. For a causal right-sided signal, multiply by $u(t)$.

Residue computation:

- Simple pole at $p$: multiply by $(s-p)$, evaluate at $s=p$.
- Repeated pole of order $m$: multiply by $(s-p)^m$, differentiate $m-1$ times, divide by $(m-1)!$, evaluate at $s=p$.
- Conjugate pair: compute one residue and combine with its conjugate partner.

Bromwich inversion is a theorem-based version of the same pole collection used in partial fractions: contour integration sums modal contributions from poles, while partial fractions lists those same terms directly.

__Example 1: distinct poles.__ $F(s)=\frac{1}{s(s+1)}$, ROC $\Re(s)>0$.  Enclosed poles: $s=0$ and $s=-1$, both simple.

- $\operatorname*{Res}_{s=0}=\frac{e^{st}}{s+1}\big|_{s=0}=1$.
- $\operatorname*{Res}_{s=-1}=\frac{e^{st}}{s}\big|_{s=-1}=-e^{-t}$.

Hence $f(t)=(1-e^{-t})u(t)$, matching partial fractions.

__Example 2: repeated pole.__ $F(s)=\frac{1}{(s+1)^3}$, ROC $\Re(s)>-1$.  The only enclosed pole is the triple pole $s=-1$.

$\operatorname*{Res}_{s=-1}=\frac{1}{2!}\frac{d^2}{ds^2}e^{st}\big|_{s=-1}=\frac{1}{2}t^2e^{-t}$.

Hence $f(t)=\frac{t^2}{2}e^{-t}u(t)$, matching the standard table pair.

---

Flashcards for this section are as follows:

- State the Bromwich integral formula. ::@:: $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}\,ds$, where $\sigma$ is any value within the ROC.
- Why does the integral give the same result for any $\sigma$ in the ROC? ::@:: By the Cauchy integral theorem, shifting the contour within the analytic region of the ROC does not change the integral.
- How does Bromwich inversion on the imaginary axis reduce to inverse Fourier? ::@:: Set $\sigma=0$, substitute $s=j\omega$ and $ds=j\,d\omega$ to get $\frac{1}{2\pi}\int_{-\infty}^{\infty}F(j\omega)e^{j\omega t}\,d\omega$.
- What is the practical residue workflow for rational $F(s)$? ::@:: Choose Bromwich line right of all poles → close left for $t>0$ → arc vanishes by Jordan's lemma → Bromwich integral = $2\pi j$ times sum of enclosed residues → multiply by $u(t)$.
- How are residues computed for simple, repeated, and conjugate poles? ::@:: Simple: multiply by $(s-p)$, evaluate at $p$.  Repeated order $m$: multiply by $(s-p)^m$, differentiate $m-1$ times, divide by $(m-1)!$, evaluate at $p$.  Conjugate: compute one, combine with partner.
- Evaluate $F(s)=\frac{1}{s(s+1)}$ by Bromwich inversion. ::@:: Residues at $s=0$ and $s=-1$: $1$ and $-e^{-t}$.  Hence $f(t)=(1-e^{-t})u(t)$.
- Evaluate $F(s)=\frac{1}{(s+1)^3}$ by Bromwich inversion. ::@:: Triple pole at $s=-1$: residue $=\frac{1}{2}t^2e^{-t}$.  Hence $f(t)=\frac{t^2}{2}e^{-t}u(t)$.
