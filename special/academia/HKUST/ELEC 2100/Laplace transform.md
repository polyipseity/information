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

Laplace analysis is the continuous-time complex-frequency toolkit used in ELEC 2100 after Fourier analysis and DTFT/DFT.  It extends transform methods from steady-state spectral analysis to transient, causal, and differential-equation problems: derivatives and integrals become algebraic factors in $s$, unilateral Laplace keeps track of initial conditions, and poles/transfer functions become easy to analyze.

Historically, the method is named after Pierre-Simon Laplace (1749–1827), who introduced transform methods for solving differential equations in 1779.  In engineering practice it became especially influential after Oliver Heaviside (1850–1925) developed operational-calculus methods in the late 19th century that effectively matched Laplace-transform techniques and made them useful for circuits and transmission lines.

Main advantages in this course are:

- differential and integral equations become algebraic equations in $s$;
- unilateral analysis incorporates initial conditions automatically;
- convolution, transfer functions, poles, and block-diagram interconnections become easier to study in one framework.

Main disadvantages/caveats are:

- the physical interpretation is less immediate than Fourier-transform frequency analysis;
- the ROC must always be tracked, because the same algebraic expression can represent different time-domain signals.

Practically, the Laplace unit in this course uses Laplace transform for four recurring tasks: direct transforms, inverse transforms, solving differential equations and dynamic circuits, and building system functions for pole-zero, stability, and block-diagram analysis.

---

Flashcards for this section are as follows:

- Why does ELEC 2100 introduce Laplace transform after time-domain and Fourier tools? ::@:: Because Laplace extends transform methods from steady-state spectral analysis to transient and causal problems: differential/integral operations become algebraic operations in $s$, dynamic-system and circuit analysis become easier, and unilateral Laplace retains initial-condition information. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- What is the role of Laplace transform in the course roadmap? ::@:: It is the complex-frequency-domain bridge from time-domain differential-equation models to transfer functions, pole-zero analysis, stability tests, block-diagram interconnection, and dynamic-circuit response.
- What short historical picture should you remember for the Laplace transform? ::@:: Pierre-Simon Laplace introduced the transform method for differential equations in 1779, and Oliver Heaviside later developed operational-calculus methods in the late 19th century that made the same ideas powerful in engineering practice.
- What are the main practical advantages of Laplace transform in ELEC 2100? ::@:: It turns differential/integral equations into algebraic equations in $s$, automatically incorporates initial conditions in unilateral form, and makes transfer functions, poles, convolution, and block-diagram analysis easier.
- What is the main disadvantage/caveat of Laplace transform compared with Fourier transform? ::@:: Its physical interpretation is less immediate than Fourier frequency analysis, and it requires explicit ROC bookkeeping because the same algebraic expression can represent different time-domain signals.
- What are the main practical uses of Laplace transform in the Laplace unit of ELEC 2100? ::@:: Direct transforms, inverse transforms, solving differential equations and dynamic circuits, and forming system functions for pole-zero, stability, and block-diagram analysis.

## definition and ROC

The bilateral Laplace transform is $F(s)=\mathcal{L}\{f(t)\}=\int_{-\infty}^{\infty} f(t)e^{-st}\,dt$ with $s=\sigma+j\omega$.

For physically causal signals and systems, ELEC 2100 mainly uses the unilateral form $F(s)=\mathcal{L}_u\{f(t)\}=\int_{0^-}^{\infty} f(t)e^{-st}\,dt$.

The __region of convergence__ (ROC) is the set of $s$ values for which the transform integral converges absolutely.

Write $s=\sigma+j\omega$.  The factor $e^{-j\omega t}$ changes only phase, not magnitude, while $|e^{-st}|=e^{-\sigma t}$.  Therefore the real part $\sigma$ controls convergence:

- for $t>0$, moving right in the $s$-plane (larger $\sigma$) adds stronger decay $e^{-\sigma t}$ and helps a right-sided tail converge;
- for $t<0$, moving right makes $e^{-\sigma t}=e^{+\sigma|t|}$ grow faster, so moving left helps a left-sided tail converge.

This is the actual meaning of being to the left or right of a pole.  For the right-sided exponential $e^{pt}u(t)$, the transform is $\frac{1}{s-p}$ with ROC $\Re(s)>\Re(p)$; for the left-sided signal $-e^{pt}u(-t)$, the transform is again $\frac{1}{s-p}$ but the ROC is $\Re(s)<\Re(p)$.  The same algebraic factor can therefore represent different time-domain signals; the ROC records which side of the pole makes the weighted integral decay.  So ROC depends not only on the algebraic expression but also on the restriction placed on the signal class: right-sided, left-sided, two-sided, or finite-duration.

A compact existence criterion is __exponential order__.  If there exist real numbers $a_+$ and $a_-$ and positive constants $M_+$, $M_-$ such that $|f(t)|\le M_+e^{a_+ t}$ for sufficiently large positive $t$ and $|f(t)|\le M_-e^{a_- t}$ for sufficiently large negative $t$, then the bilateral Laplace transform converges at least in the strip $a_+<\Re(s)<a_-$, provided the strip is nonempty.  For unilateral/right-sided analysis, only the positive-time tail matters: if $|f(t)|\le Me^{a t}$ for sufficiently large $t>0$, then $\mathcal{L}_u\{f(t)\}$ converges for $\Re(s)>a$.

This makes several common engineering rules of thumb precise:

- the common shortcut "bounded aperiodic signals always have a Laplace transform" is rigorously safest in the unilateral/right-sided setting, where boundedness implies exponential order $a=0$ and hence ROC $\Re(s)>0$;
- polynomials grow more slowly than exponentials, so right-sided power functions such as $t^n u(t)$ still have ROC $\Re(s)>0$;
- unilateral exponentials satisfy $\mathcal{L}_u\{e^{\alpha t}u(t)\}=\frac{1}{s-\alpha}$ with ROC $\Re(s)>\alpha$;
- super-exponential signals such as $e^{t^2}u(t)$ have no Laplace transform for any finite $s$, because $e^{t^2-\sigma t}\to\infty$ as $t\to\infty$ for every fixed $\sigma$.

For a rational algebraic form, the vertical lines $\Re(s)=\Re(p_k)$ through pole real parts partition the $s$-plane into candidate ROC regions.  Right half-planes, left half-planes, and strips are all special cases of this partition.  The support restriction on the signal then selects which candidate region is valid.  When several components are combined, the transform is first justified on the __intersection of their individual ROCs__.  This means choosing one common vertical line $\Re(s)=\sigma$ on which every constituent integral converges simultaneously.  For example, $e^{t}u(t)$ has ROC $\Re(s)>1$ and $e^{3t}u(t)$ has ROC $\Re(s)>3$, so their sum has ROC $\Re(s)>3$.  Likewise, $e^{-t}u(t)$ has ROC $\Re(s)>-1$ while $-e^{2t}u(-t)$ has ROC $\Re(s)<2$, so the combined two-sided signal has strip ROC $-1<\Re(s)<2$.  After algebraic simplification, pole-zero cancellation can enlarge the final ROC because a cancelled pole no longer blocks convergence.

Hence the precise shape statements are:

- Right-sided signal: ROC is a right half-plane $\Re(s)>\sigma_{\max}$, where $\sigma_{\max}$ is the rightmost convergence boundary.
- Left-sided signal: ROC is a left half-plane $\Re(s)<\sigma_{\min}$.
- Two-sided signal: ROC is a vertical strip $\sigma_{\min}<\Re(s)<\sigma_{\max}$.  It is not merely "the middle of two poles"; with many poles, the boundaries come from the nearest left- and right-side growth constraints.
- Finite-duration signal: ROC is the entire finite $s$-plane, because exponential weighting on a bounded time interval cannot diverge.

For rational transforms, the ROC is an open connected pole-free region, and poles lie on its boundary or outside it.  Once the ROC is specified, the inverse Laplace transform is unique; without the ROC, the same algebraic $F(s)$ can correspond to different time-domain signals.  When the ROC includes the imaginary axis $\Re(s)=0$, evaluation at $s=j\omega$ recovers the Fourier transform.

The notation $0^-$ in the lower limit of the unilateral transform deserves explicit attention.  The symbol $0^-$ denotes the left-hand limit approaching zero: the integration domain begins infinitesimally before $t=0$, so the instant $t=0$ itself is included.

For signals without distributional components, this distinction is immaterial.  In the Lebesgue sense a single point has measure zero and cannot alter an integral's value, so integrating over $[0,\infty)$, $(0,\infty)$, or with any limit that merely includes or excludes $\{0\}$ gives the same result.  Concretely, for $f(t)=e^{-t}$:

$\int_{0^-}^{\infty}e^{-t}e^{-st}\,dt=\int_{0^+}^{\infty}e^{-t}e^{-st}\,dt=\frac{1}{1+s}$.

The distinction becomes critical for signals containing a Dirac delta at the origin.  By the sifting property, $\int\delta(t)\varphi(t)\,dt=\varphi(0)$ for any suitable test function $\varphi$.  The choice of lower limit therefore determines whether the impulse mass at $t=0$ is included:

$\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=e^{-s\cdot 0}=1,\qquad\text{but}\qquad\int_{0^+}^{\infty}\delta(t)e^{-st}\,dt=0$.

Using $0^+$ places the entire mass of $\delta(0)$ outside the domain; using $0^-$ includes it.  Engineering Laplace analysis adopts $0^-$ uniformly so that: (i) an impulsive excitation $\delta(t)$ applied at $t=0$ is fully captured, and (ii) initial conditions of reactive elements stored just before $t=0$ are automatically retained.

---

Flashcards for this section are as follows:

- What is the bilateral Laplace transform definition? ::@:: $F(s)=\int_{-\infty}^{\infty} f(t)e^{-st}\,dt$ with $s=\sigma+j\omega$.
- For the unilateral transform formula $F(s)=\mathcal{L}_u\{f(t)\}=\int_{0^-}^{\infty} f(t)e^{-st}\,dt$, what definition is used most often in ELEC 2100? ::@:: The unilateral Laplace transform integrates from $0^-$ to $\infty$ so initial-condition information is retained for causal-system analysis.
- What is the ROC in Laplace analysis? ::@:: The set of complex-frequency values $s$ for which the transform integral converges absolutely.
- What does the real part $\sigma=\Re(s)$ actually do to convergence in the Laplace kernel $e^{-st}$? ::@:: Since $|e^{-st}|=e^{-\sigma t}$, the real part controls exponential weighting. <br/> For $t>0$, larger $\sigma$ gives stronger decay and helps right-sided tails converge. <br/> For $t<0$, larger $\sigma$ gives stronger growth $e^{+\sigma|t|}$, so moving left helps left-sided tails converge.
- For the same algebraic factor $\frac{1}{s-p}$, how do the right-sided signal $e^{pt}u(t)$ and the left-sided signal $-e^{pt}u(-t)$ differ? ::@:: They have the same algebraic transform $\frac{1}{s-p}$ but different ROCs. <br/> Right-sided $e^{pt}u(t)$ requires $\Re(s)>\Re(p)$. <br/> Left-sided $-e^{pt}u(-t)$ requires $\Re(s)<\Re(p)$. <br/> The ROC identifies which side of the pole makes the weighted integral decay.
- What does it mean for a signal to be of exponential order, and what does that imply for ROC? ::@:: Exponential order means the signal tails are bounded by exponentials: for large positive time $|f(t)|\le M_+e^{a_+ t}$ and for large negative time $|f(t)|\le M_-e^{a_- t}$. <br/> Then the bilateral Laplace transform converges at least in the strip $a_+<\Re(s)<a_-$ if that strip is nonempty; for unilateral/right-sided analysis, order $a$ guarantees convergence for $\Re(s)>a$.
- Why is the common shortcut about bounded aperiodic signals safest in the unilateral/right-sided setting? ::@:: Because a bounded right-sided signal has exponential order $a=0$, so $\mathcal{L}_u\{f(t)\}$ converges for $\Re(s)>0$. <br/> For bilateral transforms, opposite tails can still demand incompatible signs of $\Re(s)$, so boundedness alone does not guarantee a common ROC strip.
- Why do right-sided power functions such as $t^n u(t)$ still have a Laplace transform? ::@:: Because polynomials grow more slowly than exponentials, so the weight $e^{-\sigma t}$ dominates $t^n$ for every $\sigma>0$. <br/> Therefore $t^n u(t)$ has ROC $\Re(s)>0$.
- What is the ROC of the unilateral exponential signal $e^{\alpha t}u(t)$, and why? ::@:: $\mathcal{L}_u\{e^{\alpha t}u(t)\}=\frac{1}{s-\alpha}$ with ROC $\Re(s)>\alpha$, because the weighted tail is $e^{-(s-\alpha)t}$ and must decay as $t\to\infty$.
- Why does a super-exponential signal such as $e^{t^2}u(t)$ have no Laplace transform? ::@:: For every fixed $\sigma$, the weighted signal behaves like $e^{t^2-\sigma t}$, which still goes to infinity as $t\to\infty$. <br/> So no finite choice of $\Re(s)=\sigma$ can force convergence, meaning there is no ROC.
- Why does ROC depend on the signal restriction rather than on the algebraic expression alone? ::@:: The algebraic form determines candidate pole boundaries, but the support class chooses which side or strip is valid. <br/> The same $F(s)$ can represent a right-sided, left-sided, or two-sided signal depending on which candidate ROC is selected.
- What does "take the intersection of ROCs" mean when several Laplace-transformable components are combined? ::@:: It means choose the set of $s$ values where every constituent integral converges simultaneously. <br/> Example: $\Re(s)>1$ intersected with $\Re(s)>3$ gives $\Re(s)>3$. <br/> After algebraic simplification, pole-zero cancellation can enlarge the final ROC if a blocking pole disappears.
- For right-sided, left-sided, two-sided, and finite-duration signals, what are the exact ROC shapes in the $s$-plane? ::@:: Right-sided: $\Re(s)>\sigma_{\max}$. <br/> Left-sided: $\Re(s)<\sigma_{\min}$. <br/> Two-sided: $\sigma_{\min}<\Re(s)<\sigma_{\max}$. <br/> Finite-duration: entire finite $s$-plane.
- For a rational Laplace transform, what is the relation between poles and the ROC? ::@:: The ROC is an open connected region containing no poles. <br/> Poles lie on the boundary of the ROC or outside it, and the boundary is determined by the growth rates that the exponential weight must overcome.
- Why is the inverse Laplace transform unique only after the ROC is specified? ::@:: The same algebraic rational form can correspond to different time-domain signals with different supports. <br/> The pair (algebraic form + ROC) determines the inverse uniquely; the algebraic form alone does not.
- Why does ROC matter beyond existence? ::@:: Because different time-domain signals can share the same algebraic $F(s)$ but differ by ROC, and stability/Fourier-existence conclusions depend on ROC placement. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- When does the Laplace transform reduce to the Fourier transform? ::@:: When the ROC includes the imaginary axis $\Re(s)=0$, so evaluation at $s=j\omega$ is valid and yields the Fourier transform.
- What does the lower limit $0^-$ in $\int_{0^-}^{\infty}f(t)e^{-st}\,dt$ denote? ::@:: The left-hand limit approaching zero: the integration path begins infinitesimally before $t=0$, so the point $t=0$ is included in the integration domain.
- Why does replacing $0^-$ with $0^+$ as the lower limit make no difference for an ordinary locally integrable signal? ::@:: A single point has Lebesgue measure zero and cannot change the value of an integral, so including or excluding the endpoint $t=0$ is irrelevant when $f$ carries no distributional mass there.
- Compute $\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt$ and $\int_{0^+}^{\infty}\delta(t)e^{-st}\,dt$ and explain why they differ. ::@:: The $0^-$ integral equals $1$: by the sifting property, $\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=e^{-s\cdot 0}=1$, since $t=0$ is inside the domain. <br/> The $0^+$ integral equals $0$: the Dirac mass at $t=0$ is excluded from $(0,\infty)$, so the sifting property is not activated.
- Why does engineering Laplace analysis adopt $0^-$ rather than $0^+$ as the unilateral lower limit? ::@:: To include both impulsive excitations at $t=0$ (which would be missed with $0^+$) and initial conditions at $t=0^-$, ensuring consistent treatment of systems with distributional inputs and non-zero initial states.

## common transform pairs and core properties

Common unilateral pairs used in this course include:

- $u(t) \longleftrightarrow \frac{1}{s}$, ROC $\Re(s)>0$
- $e^{-\alpha t}u(t) \longleftrightarrow \frac{1}{s+\alpha}$, ROC $\Re(s)>-\alpha$
- $\delta(t) \longleftrightarrow 1$
- $t^n u(t) \longleftrightarrow \frac{n!}{s^{n+1}}$
- $\sin(\omega_0 t)u(t) \longleftrightarrow \frac{\omega_0}{s^2+\omega_0^2}$, ROC $\Re(s)>0$
- $\cos(\omega_0 t)u(t) \longleftrightarrow \frac{s}{s^2+\omega_0^2}$, ROC $\Re(s)>0$

Brief derivation skeletons for these pairs:

- $u(t)$ pair: $\int_{0^-}^{\infty}e^{-st}\,dt=\left[-\frac{1}{s}e^{-st}\right]_{0^-}^{\infty}=\frac{1}{s}$, valid when $\Re(s)>0$ so the upper-limit exponential decays.
- $e^{-\alpha t}u(t)$ pair: $\int_{0^-}^{\infty}e^{-(s+\alpha)t}\,dt=\frac{1}{s+\alpha}$, so ROC is $\Re(s+\alpha)>0\iff\Re(s)>-\alpha$.
- $\delta(t)$ pair: $\int_{0^-}^{\infty}\delta(t)e^{-st}\,dt=e^{-s\cdot 0}=1$ by the sifting property.
- $t^n u(t)$ pair: repeated integration by parts (or the Gamma integral) gives $\int_0^{\infty}t^n e^{-st}\,dt=\frac{n!}{s^{n+1}}$ for $\Re(s)>0$.  A faster reconstruction starts from $u(t)\leftrightarrow\frac{1}{s}$ and repeatedly uses the $t$-multiplication rule $\mathcal{L}\{t f(t)\}=-\frac{dF}{ds}$, giving $\mathcal{L}\{t^n u(t)\}=(-1)^n\frac{d^n}{ds^n}\!\left(\frac{1}{s}\right)=\frac{n!}{s^{n+1}}$.
- $\sin(\omega_0 t)u(t)$ pair: use Euler's identity $\sin(\omega_0 t)=\frac{e^{j\omega_0 t}-e^{-j\omega_0 t}}{2j}$, transform the two exponentials, then combine to get $\frac{1}{2j}\left(\frac{1}{s-j\omega_0}-\frac{1}{s+j\omega_0}\right)=\frac{\omega_0}{s^2+\omega_0^2}$.
- $\cos(\omega_0 t)u(t)$ pair: use $\cos(\omega_0 t)=\frac{e^{j\omega_0 t}+e^{-j\omega_0 t}}{2}$, transform the two exponentials, then combine to get $\frac{1}{2}\left(\frac{1}{s-j\omega_0}+\frac{1}{s+j\omega_0}\right)=\frac{s}{s^2+\omega_0^2}$.

Fourier comparison for these common pairs should be kept in mind.  The pair $\delta(t)\leftrightarrow 1$ matches Fourier exactly.  For $e^{-\alpha t}u(t)$ with $\alpha>0$, evaluating the Laplace transform on the imaginary axis gives the ordinary Fourier transform $\frac{1}{\alpha+j\omega}$ because the ROC includes $j\omega$.  By contrast, $u(t)$, $t^n u(t)$, and the causal sinusoids $\sin(\omega_0 t)u(t)$ and $\cos(\omega_0 t)u(t)$ sit on or beyond the Fourier boundary and therefore require generalized-function treatment in Fourier analysis.  Non-causal sinusoids have the familiar Fourier impulse lines at $\pm\omega_0$, whereas causal sinusoids become rational Laplace expressions with ROC $\Re(s)>0$.

Core properties repeatedly used in this note and in standard transform work, each with a compact derivation idea:

- __Linearity__: pull constants through the integral and split sums termwise.
- __Time shift (bilateral)__: $\mathcal{L}_b\{f(t-t_0)\}=e^{-st_0}F_b(s)$, obtained by substituting $\tau=t-t_0$ in an integral over the whole real line.
- __Time shift (unilateral)__: direction matters.  For a delay by $t_0>0$, $\mathcal{L}_u\{f(t-t_0)u(t-t_0)\}=e^{-st_0}F_u(s)$, obtained by the same substitution after the shifted step moves the lower limit from $t_0^-$ back to $0^-$.  The factor $u(t-t_0)$ is essential: it delays the causal start of the signal together with the waveform.  Without it, $\mathcal{L}_u\{f(t-t_0)u(t)\}$ still samples the interval $0\le t<t_0$ and does not reduce to a pure factor $e^{-st_0}$ times $F_u(s)$.  For an advance by $t_0>0$, the opposite-direction shift is not symmetric:

$\mathcal{L}_u\{f(t+t_0)u(t)\}=e^{st_0}\!\left[F_u(s)-\int_{0^-}^{t_0^-} f(\tau)e^{-s\tau}\,d\tau\right]$.

The startup-correction integral appears because advancing the waveform exposes a segment of $f$ that the unilateral window starts sampling immediately at $t=0$.

- __$s$-domain shift__: $\mathcal{L}\{e^{-\alpha t}f(t)\}=\int f(t)e^{-(s+\alpha)t}dt=F(s+\alpha)$.
- __Scaling__ ($a>0$): $\mathcal{L}\{f(at)\}=\int f(at)e^{-st}dt$; substitute $\tau=at$ to get $\frac{1}{a}F\!\left(\frac{s}{a}\right)$.
- __Convolution theorem__: same syntactic statement as Fourier after replacing $j\omega$ by $s$: time-domain convolution maps to multiplication in the transform domain, $\mathcal{L}\{f_1*f_2\}=F_1(s)F_2(s)$.  Derivation cue: insert $(f_1*f_2)(t)=\int f_1(\tau)f_2(t-\tau)d\tau$, swap integration order (Fubini), then separate factors.  The practical Laplace difference is ROC bookkeeping: the derivation is first valid on the intersection of the two ROCs, and pole-zero cancellation can enlarge the final ROC after simplification.
- __Multiplication theorem (bilateral)__: time-domain multiplication maps not to an ordinary real-axis convolution but to a complex contour convolution in the $s$-plane:

$\mathcal{L}_b\{f(t)g(t)\}(s)=\frac{1}{2\pi j}\int_{\gamma-j\infty}^{\gamma+j\infty}F(\sigma)G(s-\sigma)\,d\sigma$,

where the vertical contour $\Re(\sigma)=\gamma$ is chosen so that both $F(\sigma)$ and $G(s-\sigma)$ are evaluated inside valid ROCs.  Derivation cue: write one factor, say $g(t)$, through its inverse Laplace transform, substitute into $\int f(t)g(t)e^{-st}dt$, interchange integrals, and identify the remaining transform of $f$.  Intuition: multiplying in time mixes every exponential mode of $f$ with every exponential mode of $g$, so the transform-domain description accumulates contributions over all splits $s=\sigma+(s-\sigma)$.

- __Multiplication theorem (unilateral/course practice)__: for causal signals, treat unilateral multiplication as bilateral multiplication of windowed signals $f(t)u(t)$ and $g(t)u(t)$.  There is no simpler course-default unilateral product formula routinely used in ELEC 2100, so the multiplication theorem is conceptually useful but much less convenient in practice than the convolution theorem.

Whenever a property combines several transforms, the derivation is first justified on the intersection of the participating ROCs.  Only after simplification can pole-zero cancellation enlarge the final ROC.

For derivatives and integrals, compare bilateral and unilateral carefully.

- __Bilateral differentiation__: same syntactic pattern as Fourier with $j\omega\to s$: $\mathcal{L}_b\{f'(t)\}=sF(s)$, provided boundary terms vanish, i.e. $f(t)e^{-st}\to0$ at both $t\to\pm\infty$ within ROC.
- __Unilateral differentiation__:

$\mathcal{L}_u\{f'(t)\}=sF(s)-f(0^-)$.

Windowing derivation: define $x(t)=f(t)u(t)$, so $X(s)=\mathcal{L}_b\{x(t)\}=\mathcal{L}_u\{f(t)\}=F(s)$.  Differentiate the product in distribution form,

$\frac{d}{dt}[f(t)u(t)]=f'(t)u(t)+f(0^-)\delta(t)$,

then apply bilateral Laplace term-by-term:

$\mathcal{L}_b\{x'(t)\}=sX(s)=sF(s)$,

while also

$\mathcal{L}_b\{x'(t)\}=\mathcal{L}_b\{f'(t)u(t)\}+f(0^-)\mathcal{L}_b\{\delta(t)\}=\mathcal{L}_u\{f'(t)\}+f(0^-)$.

Comparing the two expressions gives

$sF(s)=\mathcal{L}_u\{f'(t)\}+f(0^-)$,

which rearranges to the unilateral rule. Intuition: multiplying by $u(t)$ creates a boundary at $t=0$; differentiation of that boundary contributes the impulse term, which becomes the extra $f(0^-)$ correction.

- __Repeated differentiation__: bilateral Laplace keeps the Fourier-like pattern $\mathcal{L}_b\{f^{(n)}(t)\}=s^nF_b(s)$, provided all required exponential-weighted boundary terms vanish.  Unilateral Laplace records every initial derivative:

$\mathcal{L}_u\{f''(t)\}=s^2F(s)-sf(0^-)-f'(0^-)$,

and in general

$\mathcal{L}_u\{f^{(n)}(t)\}=s^nF(s)-\sum_{k=0}^{n-1}s^{n-1-k}f^{(k)}(0^-)$.

This is obtained by applying the first-derivative rule recursively.  The pattern shows why an $n$-th-order differential equation needs $n$ initial-condition values under unilateral Laplace analysis.

- __Bilateral integration__: same syntactic pattern as Fourier with $j\omega\to s$: integrating in time corresponds to division by $s$ (with the usual zero-constant/boundary assumptions).
- __Unilateral integration__ with $g(t)=\int_{0^-}^{t}f(\tau)d\tau$:

$\mathcal{L}_u\{g(t)\}=\frac{F(s)}{s}$.

More generally, if $g'(t)=f(t)$ on $t>0$, then unilateral differentiation gives

$F(s)=sG(s)-g(0^-)$,

so

$G(s)=\frac{F(s)+g(0^-)}{s}$.

Therefore "divide by $s$" is the special case in which the primitive is anchored so that $g(0^-)=0$, for example $g(t)=\int_{0^-}^{t}f(\tau)d\tau$.  Intuition: accumulation from $0^-$ forward is a causal integrator, and a causal integrator contributes one factor $1/s$; any nonzero pre-existing stored value of the primitive contributes the extra boundary term $g(0^-)/s$.

- __Repeated integration__: bilateral Laplace keeps the same Fourier-like syntax $\frac{1}{s^n}$, again subject to boundary/primitive choices.  For unilateral $n$-fold causal integration,

$g_n(t)=\underbrace{\int_{0^-}^{t}\int_{0^-}^{\tau_n}\cdots\int_{0^-}^{\tau_2}}_{n\text{ times}} f(\tau_1)\,d\tau_1\cdots d\tau_n$,

the transform is

$\mathcal{L}_u\{g_n(t)\}=\frac{F(s)}{s^n}$.

More generally, if $g_n^{(n)}(t)=f(t)$, then repeated unilateral differentiation gives

$F(s)=s^nG_n(s)-\sum_{k=0}^{n-1}s^{n-1-k}g_n^{(k)}(0^-)$,

so

$G_n(s)=\frac{F(s)+\sum_{k=0}^{n-1}s^{n-1-k}g_n^{(k)}(0^-)}{s^n}$.

In particular, twice integration gives $\mathcal{L}_u\{g_2(t)\}=\frac{F(s)+s g_2(0^-)+g_2'(0^-)}{s^2}$, and this reduces to $\frac{F(s)}{s^2}$ when the primitive and its first derivative both start from zero.

This gives the bilateral-vs-unilateral/Fourier comparison used repeatedly in ELEC 2100:

- Syntactic rule form is mostly the same as Fourier after replacing $j\omega$ by $s$.
- The minor but crucial differences are ROC constraints, endpoint/boundary terms, and unilateral initial-condition terms.

The concise exact statements are

$f(0^+)=\lim_{s\to\infty}sF(s),\qquad f(\infty)=\lim_{s\to0}sF(s)$.

More rigorous kernel intuition comes from

$sF(s)=\int_{0}^{\infty} f(t)\,s e^{-st}\,dt$.

For the initial value theorem, substitute $u=st$ and let $s\to\infty$:

$sF(s)=\int_{0}^{\infty} f\!\left(\frac{u}{s}\right)e^{-u}\,du\to f(0^+)\int_{0}^{\infty}e^{-u}\,du=f(0^+)$,

so the kernel $s e^{-st}$ acts like a unit-area pulse concentrating near $t=0^+$.  This requires that $f$ have no impulsive component at the origin; otherwise the "point-mass" at $t=0$ dominates the limit and the ordinary initial value is no longer what $sF(s)$ extracts.  For rational transforms, a convenient sufficient condition is that $F(s)$ be strictly proper.

For the final value theorem, use the same identity and let $s\to0^+$:

$sF(s)=\int_{0}^{\infty} f\!\left(\frac{u}{s}\right)e^{-u}\,du\to f(\infty)\int_{0}^{\infty}e^{-u}\,du=f(\infty)$,

provided the time limit exists and all poles of $sF(s)$ lie strictly in the open left half-plane.  This exact pole condition is the rigorous version of the usual "stable poles only" warning.

If these conditions are violated, the limit formulas fail for understandable reasons:

- IVT fails when impulses or higher-order distributional terms are present at $t=0$, because then the kernel samples a singular startup event rather than an ordinary finite value.
- FVT fails for any right-half-plane pole of $sF(s)$ because the response grows instead of settling.
- FVT fails for imaginary-axis poles of $sF(s)$ because the response oscillates forever and has no final value.
- FVT fails for repeated poles at the origin because the response behaves like a ramp or higher-order polynomial and diverges.

The proper-fraction caveat makes this precise for rational transforms.  If $F(s)$ is not proper, first perform polynomial long division:

$F(s)=P(s)+F_1(s)$,

where $F_1(s)$ is proper and $P(s)=k_m s^m+\cdots+k_1 s+k_0$ is the polynomial part.  In time domain,

$P(s)\longleftrightarrow k_m\delta^{(m)}(t)+\cdots+k_1\delta'(t)+k_0\delta(t)$.

These impulse terms are supported only at $t=0$: for every ordinary time $t>0$ they contribute nothing, which is the practical meaning of saying that the polynomial part does not determine the ordinary right-hand initial value.  But their contribution to $\lim_{s\to\infty}sF(s)$ is disastrous, because $sP(s)$ diverges.  Therefore the ordinary initial value must be read from the proper remainder only:

$f(0^+)=\lim_{s\to\infty}sF_1(s)$,

provided $F_1$ satisfies the usual IVT conditions.  In short: improper polynomial parts correspond to impulsive startup singularities, not to ordinary finite values of the signal.

---

Flashcards for this section are as follows:

- For the pair $u(t)\leftrightarrow\frac{1}{s}$, derive the transform briefly and state ROC. ::@:: $\mathcal{L}_u\{u(t)\}=\int_{0^-}^{\infty}e^{-st}dt=\left[-\frac{1}{s}e^{-st}\right]_{0^-}^{\infty}=\frac{1}{s}$. <br/> ROC: $\Re(s)>0$.
- For the pair $e^{-\alpha t}u(t)\leftrightarrow\frac{1}{s+\alpha}$, derive the transform briefly and state ROC. ::@:: $\mathcal{L}_u\{e^{-\alpha t}u(t)\}=\int_{0^-}^{\infty}e^{-(s+\alpha)t}dt=\frac{1}{s+\alpha}$. <br/> ROC: $\Re(s+\alpha)>0\iff\Re(s)>-\alpha$.
- For the pair $\delta(t)\leftrightarrow 1$, derive the transform and explain the role of $0^-$. ::@:: $\mathcal{L}_u\{\delta(t)\}=\int_{0^-}^{\infty}\delta(t)e^{-st}dt=e^{-s\cdot0}=1$ by sifting. <br/> The $0^-$ lower limit includes the impulse mass at $t=0$.
- For the pair $t^n u(t)\leftrightarrow\frac{n!}{s^{n+1}}$, what derivation methods and ROC should you recall? ::@:: Method 1: repeated integration by parts on $\int_0^{\infty}t^n e^{-st}dt$ gives $\frac{n!}{s^{n+1}}$. <br/> Method 2: start from $u(t)\leftrightarrow\frac{1}{s}$ and repeatedly apply $\mathcal{L}\{t f(t)\}=-\frac{dF}{ds}$, so $\mathcal{L}\{t^n u(t)\}=(-1)^n\frac{d^n}{ds^n}\!\left(\frac{1}{s}\right)=\frac{n!}{s^{n+1}}$. <br/> ROC: $\Re(s)>0$.
- For the pair $\sin(\omega_0 t)u(t)\leftrightarrow\frac{\omega_0}{s^2+\omega_0^2}$, what derivation cue, ROC, and Fourier comparison should you recall? ::@:: Derivation: write $\sin(\omega_0 t)=\frac{e^{j\omega_0 t}-e^{-j\omega_0 t}}{2j}$ and combine the two exponential transforms. <br/> ROC: $\Re(s)>0$. <br/> Comparison: the non-causal Fourier transform of a sinusoid gives impulse lines at $\pm\omega_0$, whereas the causal Laplace transform gives a rational expression with right-half-plane ROC.
- For the pair $\cos(\omega_0 t)u(t)\leftrightarrow\frac{s}{s^2+\omega_0^2}$, what derivation cue, ROC, and Fourier comparison should you recall? ::@:: Derivation: write $\cos(\omega_0 t)=\frac{e^{j\omega_0 t}+e^{-j\omega_0 t}}{2}$ and combine the two exponential transforms. <br/> ROC: $\Re(s)>0$. <br/> Comparison: the non-causal Fourier transform of a cosine gives impulse lines at $\pm\omega_0$, whereas the causal Laplace transform gives a rational expression with right-half-plane ROC.
- Which common Laplace transform pair also matches its ordinary Fourier counterpart directly, and which common pairs generally require Fourier boundary/distribution treatment? ::@:: $\delta(t)\leftrightarrow1$ matches directly in both transforms, and $e^{-\alpha t}u(t)$ with $\alpha>0$ reduces to $\frac{1}{\alpha+j\omega}$ on the imaginary axis because its ROC includes it. <br/> By contrast, $u(t)$, $t^n u(t)$, and causal sinusoids lie on or beyond the Fourier boundary and generally require generalized-function treatment in Fourier analysis.
- What is the one-line derivation idea for Laplace linearity? ::@:: Start from $\mathcal{L}\{a f+b g\}=\int (a f+b g)e^{-st}dt$ and split the integral termwise to obtain $aF(s)+bG(s)$.
- Compare bilateral and unilateral time shifts for both delay and advance, and explain why direction matters in the unilateral case. ::@:: Bilateral delay: $\mathcal{L}_b\{f(t-t_0)\}=e^{-st_0}F_b(s)$; bilateral advance: $\mathcal{L}_b\{f(t+t_0)\}=e^{st_0}F_b(s)$, assuming the bilateral transform exists. <br/> Unilateral delay: $\mathcal{L}_u\{f(t-t_0)u(t-t_0)\}=e^{-st_0}F_u(s)$ because the step delays the causal start together with the waveform. <br/> Unilateral advance is not a pure factor: $\mathcal{L}_u\{f(t+t_0)u(t)\}=e^{st_0}\!\left[F_u(s)-\int_{0^-}^{t_0^-}f(\tau)e^{-s\tau}d\tau\right]$. <br/> Direction matters because unilateral analysis always starts sampling at $t=0^-$.
- How is the $s$-domain shift rule $e^{-\alpha t}f(t)\leftrightarrow F(s+\alpha)$ derived? ::@:: Combine exponentials in the kernel: $e^{-\alpha t}e^{-st}=e^{-(s+\alpha)t}$, so the transform is $F$ evaluated at $s+\alpha$.
- How is the scaling rule $f(at)\leftrightarrow\frac{1}{a}F(s/a)$ (for $a>0$) derived? ::@:: Use substitution $\tau=at$ in $\int f(at)e^{-st}dt$; then $dt=d\tau/a$ and $e^{-st}=e^{-(s/a)\tau}$.
- Compare the Laplace convolution theorem with the Fourier convolution theorem, and state the practical Laplace difference. ::@:: Syntactically they match after $j\omega\to s$: time-domain convolution maps to multiplication of transforms. <br/> For Laplace, the practical extra issue is ROC bookkeeping: the derivation is first valid on the intersection of the participating ROCs, and only after simplification can pole-zero cancellation enlarge the final ROC.
- State the bilateral Laplace multiplication theorem, and explain why it is less convenient in practice than the convolution theorem. ::@:: $\mathcal{L}_b\{f(t)g(t)\}(s)=\frac{1}{2\pi j}\int_{\gamma-j\infty}^{\gamma+j\infty}F(\sigma)G(s-\sigma)\,d\sigma$. <br/> Unlike Fourier's ordinary frequency-axis convolution, Laplace uses a complex vertical-contour convolution whose contour must stay inside valid ROCs. <br/> That ROC/contour bookkeeping makes the theorem much less convenient in practice than $f_1*f_2\leftrightarrow F_1F_2$.
- How should unilateral time-domain multiplication be understood in ELEC 2100 Laplace work? ::@:: Treat unilateral multiplication as bilateral multiplication of the windowed causal signals $f(t)u(t)$ and $g(t)u(t)$. <br/> There is no simpler course-default unilateral product rule routinely used, so the multiplication theorem is mainly a conceptual companion to the convolution theorem.
- Compare the bilateral and unilateral first-differentiation rules, and explain the unilateral correction term explicitly. ::@:: Bilateral: $\mathcal{L}_b\{f'(t)\}=sF_b(s)$, the same syntax as Fourier after $j\omega\to s$, provided boundary terms vanish. <br/> Unilateral: let $x(t)=f(t)u(t)$. Then $x'(t)=f'(t)u(t)+f(0^-)\delta(t)$, so $sF_u(s)=\mathcal{L}_u\{f'(t)\}+f(0^-)$ and therefore $\mathcal{L}_u\{f'(t)\}=sF_u(s)-f(0^-)$. <br/> The extra term comes from differentiating the causal window at $t=0$.
- State the bilateral and unilateral formulas for second differentiation and general repeated differentiation. ::@:: Bilateral: $\mathcal{L}_b\{f''(t)\}=s^2F_b(s)$ and, more generally, $\mathcal{L}_b\{f^{(n)}(t)\}=s^nF_b(s)$, assuming the required weighted boundary terms vanish. <br/> Unilateral: $\mathcal{L}_u\{f''(t)\}=s^2F_u(s)-sf(0^-)-f'(0^-)$ and, in general, $\mathcal{L}_u\{f^{(n)}(t)\}=s^nF_u(s)-\sum_{k=0}^{n-1}s^{n-1-k}f^{(k)}(0^-)$.
- Compare the bilateral and unilateral first-integration rules, and state the unilateral boundary-term correction. ::@:: Bilateral: if $g'(t)=f(t)$ and the primitive is chosen so weighted boundary terms vanish, then $\mathcal{L}_b\{g(t)\}=F_b(s)/s$, matching Fourier syntax after $j\omega\to s$. <br/> Unilateral: if $g'(t)=f(t)$, then $G_u(s)=\frac{F_u(s)+g(0^-)}{s}$. <br/> The common formula $F_u(s)/s$ is the special case $g(0^-)=0$, for example when $g(t)=\int_{0^-}^{t}f(\tau)d\tau$.
- State the bilateral and unilateral formulas for twice integration and general repeated integration, including unilateral boundary terms. ::@:: Bilateral keeps the same pattern $F_b(s)/s^n$, subject to boundary/primitive choices. <br/> Unilateral repeated integration satisfies $F_u(s)=s^nG_u(s)-\sum_{k=0}^{n-1}s^{n-1-k}g^{(k)}(0^-)$, so $G_u(s)=\frac{F_u(s)+\sum_{k=0}^{n-1}s^{n-1-k}g^{(k)}(0^-)}{s^n}$. <br/> For zero initial primitive terms this reduces to $F_u(s)/s^n$, and twice integration reduces to $F_u(s)/s^2$.
- State the concise exact initial and final value theorems with their exact conditions. ::@:: Initial value theorem: $f(0^+)=\lim_{s\to\infty}sF(s)$, valid when $f$ has no impulse at $t=0$; for rational transforms, strict properness of $F(s)$ is a convenient sufficient check. <br/> Final value theorem: $\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$, valid when the time limit exists and all poles of $sF(s)$ lie strictly in the open left half-plane.
- What rigorous kernel intuition explains the conditions behind the initial and final value theorems, and what happens if those conditions are violated? ::@:: The identity $sF(s)=\int_0^{\infty} f(t) e^{-st} (s\,dt)=\int_{0}^{\infty} f\!\left(\frac{u}{s}\right)e^{-u}\,du$ shows that as $s\to\infty$, the kernel concentrates near $t=0^+$, while as $s\to0^+$ it samples farther into the long-time tail. <br/> If IVT conditions fail, impulses at $t=0$ dominate and the limit no longer gives an ordinary startup value. <br/> If FVT conditions fail, then RHP poles cause growth, imaginary-axis poles cause non-settling oscillation, and repeated poles at the origin cause ramp-like divergence.
- Why must you split an improper rational $F(s)$ into a polynomial part plus a proper remainder before applying the ordinary IVT? ::@:: Because the polynomial part corresponds to impulsive terms at $t=0$ such as $\delta(t),\delta'(t),\ldots$, while the ordinary initial value theorem is meant for the nonsingular causal remainder. <br/> So write $F(s)=P(s)+F_1(s)$ and read the ordinary initial value from $f(0^+)=\lim_{s\to\infty}sF_1(s)$.
- What does the polynomial part $P(s)=k_m s^m+\cdots+k_1 s+k_0$ represent in time domain, and why does it spoil a naive IVT calculation? ::@:: It represents $k_m\delta^{(m)}(t)+\cdots+k_1\delta'(t)+k_0\delta(t)$, which is concentrated at $t=0$. <br/> These terms do not define an ordinary finite right-hand value for $t>0$, but $sP(s)$ diverges as $s\to\infty$, so a naive limit on the full improper transform gives the wrong conclusion.

## inverse Laplace transform by partial fractions

ELEC 2100 uses three inverse-Laplace routes, with different practical roles.

1. __Complex contour inversion via the Bromwich integral__: this is the definition-level method.  It uses contour integration and the residue theorem to recover $f(t)$ from $F(s)$ directly.
2. __Partial fraction expansion + table lookup__: this is the key hand-computation technique for proper rational transforms.  It decomposes $F(s)$ into standard first-order or repeated-pole terms, then matches each term to a known time-domain pair.
3. __Computer-aided inversion__: tools such as MATLAB can symbolically or numerically invert transforms, and are useful for checking algebra or handling higher-order expressions, but they do not replace pole/ROC reasoning.

In this course, method 2 is the default computational shortcut for proper rational functions, method 1 supplies the rigorous contour justification behind residue-based inversion, and method 3 is mainly a verification or automation aid.

Partial-fraction expansion applies when $F(s)$ is a __rational function__ $F(s)=\frac{N(s)}{D(s)}$.  The main prerequisite is __properness__: $\deg N<\deg D$.  If $F(s)$ is improper, first do polynomial long division:

$F(s)=P(s)+F_{\text{proper}}(s)$.

The polynomial part corresponds to impulses or derivatives of impulses at $t=0$, while the proper remainder is the part handled by partial fractions.  For the proper rational part, factor the denominator over the reals into linear and irreducible quadratic factors, record the pole locations and multiplicities, and then write the correct decomposition template before solving any coefficients.  The numerator roots are the zeros of $F(s)$, but the partial-fraction structure is determined by the denominator factorization, i.e. by the poles.

The full ELEC 2100 workflow is:

1. make the rational function proper;
2. factor the denominator completely over the reals;
3. identify poles and their multiplicities;
4. write the correct partial-fraction template from the pole structure;
5. solve the coefficients by the easiest available trick;
6. map each term to a standard inverse-Laplace pair;
7. for complex-conjugate poles, combine them into real damped cosine/sine form;
8. check the result by recombining algebraically or by verifying pole/order consistency.

The standard templates are as follows.

- __Distinct real poles__: if $F(s)=\frac{N(s)}{(s-p_1)(s-p_2)\cdots(s-p_n)}$ with distinct real poles $p_k$, then

$F(s)=\sum_{k=1}^{n}\frac{A_k}{s-p_k}$.

- __Repeated pole__: if $p$ is a pole of order $r$, then the contribution takes the ladder form

$\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$.

- __Irreducible quadratic / complex-conjugate pair__: for a real quadratic factor $(s-\alpha)^2+\omega^2$, use a linear numerator,

$\frac{Bs+C}{(s-\alpha)^2+\omega^2}$,

or more conveniently rewrite the numerator as $B(s-\alpha)+C$ so the cosine and sine pairs appear directly.

Useful coefficient-solving tricks are:

- __Heaviside cover-up__ for a simple pole $p_k$:

$A_k=(s-p_k)F(s)\big|_{s=p_k}$.

- __Coefficient comparison or strategic substitution__: multiply through by the common denominator, expand, then compare powers of $s$ or plug in convenient values of $s$.
- __Differentiation trick for repeated poles__: if $p$ has order $r$, then the highest-order coefficient is

$A_r=(s-p)^rF(s)\big|_{s=p}$,

and lower-order coefficients are obtained by differentiating $(s-p)^rF(s)$ and then evaluating at $s=p$.  More precisely, if the repeated-pole ladder is $\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$, then $A_{r-k}=\frac{1}{k!}\frac{d^k}{ds^k}\!\left[(s-p)^rF(s)\right]\big|_{s=p}$ for $k=0,1,\ldots,r-1$.  The case $k=0$ gives the highest-order coefficient $A_r$, one derivative gives $A_{r-1}$, and so on.  This is the practical repeated-pole version of the higher-order residue formula.

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

- What are the three inverse-Laplace methods emphasized in ELEC 2100, and what is each one mainly used for? ::@:: (1) Bromwich contour inversion with residues: the definition-level theorem-based method. <br/> (2) Partial fractions + table lookup: the main hand-computation technique for proper rational transforms. <br/> (3) Computer-aided tools such as MATLAB: verification, symbolic assistance, or handling messy higher-order expressions.
- What makes partial-fraction expansion the default hand method for proper rational $F(s)$ in ELEC 2100? ::@:: Once the denominator is factored, a proper rational transform can be decomposed into simple-pole, repeated-pole, or conjugate-pole building blocks that match directly to standard inverse-Laplace table entries.
- Before applying partial fractions to a rational $F(s)=N(s)/D(s)$, what prerequisite must be checked and what should be done if it fails? ::@:: Check properness: partial fractions is applied directly when $\deg N<\deg D$. <br/> If $F(s)$ is improper, first do polynomial long division $F(s)=P(s)+F_{\text{proper}}(s)$, then apply partial fractions to the proper remainder.
- What is the full ELEC 2100 workflow for inverse Laplace by partial fractions? ::@:: Make the function proper → factor the denominator over the reals → identify poles and multiplicities → write the correct decomposition template → solve coefficients by the easiest trick → map each term through the inverse-Laplace table → combine conjugate-pair terms into real damped cosine/sine form → check by recombination or pole/order sanity.
- What partial-fraction template is used for distinct real poles, repeated poles, and irreducible quadratic factors? ::@:: Distinct real poles: $\sum_k \frac{A_k}{s-p_k}$. <br/> Repeated pole of order $r$ at $p$: $\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$. <br/> Irreducible quadratic / conjugate pair: use a linear numerator such as $\frac{Bs+C}{(s-\alpha)^2+\omega^2}$, or rewrite it as $\frac{B(s-\alpha)+C}{(s-\alpha)^2+\omega^2}$.
- What are the main coefficient-solving tricks for partial fractions in ELEC 2100? ::@:: Use cover-up for simple poles, coefficient comparison or strategic substitution after clearing denominators for mixed cases, and the differentiation trick / higher-order residue idea for repeated poles.
- For a repeated pole $p$ of order $r$, how does coefficient extraction differ from the simple-pole case? ::@:: Use the ladder $\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$. <br/> The highest-order coefficient is $A_r=(s-p)^rF(s)\big|_{s=p}$ and more generally $A_{r-k}=\frac{1}{k!}\frac{d^k}{ds^k}\!\left[(s-p)^rF(s)\right]\big|_{s=p}$ for $k=0,1,\ldots,r-1$. <br/> In practice, lower-order coefficients can also be recovered by clearing denominators and comparing polynomial coefficients.
- For $F(s)=\frac{s+2}{(s+1)^2+4}$, why should the numerator be rewritten as $(s+1)+1$, and what inverse Laplace results? ::@:: Rewriting $s+2=(s+1)+1$ exposes the standard cosine/sine numerators. <br/> Then $F(s)=\frac{s+1}{(s+1)^2+4}+\frac{1}{(s+1)^2+4}$, so $f(t)=e^{-t}\cos(2t)u(t)+\frac{1}{2}e^{-t}\sin(2t)u(t)$.
- In the repeated-pole example $F(s)=\frac{2s+3}{(s+1)^2(s+2)}$, how does differentiation recover the lower-order coefficient $B$? ::@:: Let $G(s)=(s+1)^2F(s)=\frac{2s+3}{s+2}$. <br/> Since the repeated pole has order $2$, $B=G'(s)\big|_{s=-1}$. <br/> Differentiate: $G'(s)=\frac{2(s+2)-(2s+3)}{(s+2)^2}=\frac{1}{(s+2)^2}$, so $B=G'(-1)=1$.
- In the repeated-pole example $F(s)=\frac{2s+3}{(s+1)^2(s+2)}$, how does coefficient comparison recover $B$ after $A=-1$ and $C=1$ are known? ::@:: Clear denominators to get $2s+3=A(s+1)^2+B(s+1)(s+2)+C(s+2)$. <br/> Substitute $A=-1$ and $C=1$, expand to $2s+3=(B-1)s^2+(3B-1)s+(2B+1)$, then compare the $s^2$ coefficient: $B-1=0$. <br/> Hence $B=1$.
- Why are complex-conjugate poles handled as a pair during inverse Laplace? ::@:: To produce real damped sinusoid expressions directly and avoid unnecessary complex-arithmetic detours.
- What extra structure appears in partial fractions when poles are repeated? ::@:: A repeated pole at $p$ of order $r$ requires the ladder $\frac{A_1}{s-p}+\frac{A_2}{(s-p)^2}+\cdots+\frac{A_r}{(s-p)^r}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- For $F(s)=\frac{s+1}{(s+2)(s+3)}$, compute the partial-fraction coefficients and give $f(t)$. ::@:: $k_1=(s+2)F(s)|_{s=-2}=-1$, $k_2=(s+3)F(s)|_{s=-3}=2$, so $F(s)=\frac{-1}{s+2}+\frac{2}{s+3}$ and $f(t)=(-e^{-2t}+2e^{-3t})u(t)$.
- For a simple pole $p_j$ of a proper rational $F(s)$, what is the cover-up residue formula? ::@:: $k_j=(s-p_j)F(s)\big|_{s=p_j}$.
- For $F(s)=\frac{2s+3}{(s+1)^2(s+2)}$, what partial-fraction form and inverse Laplace should you obtain? ::@:: Use $\frac{A}{s+2}+\frac{B}{s+1}+\frac{C}{(s+1)^2}$. <br/> Solving gives $A=-1$, $B=1$, $C=1$, so $F(s)=\frac{-1}{s+2}+\frac{1}{s+1}+\frac{1}{(s+1)^2}$ and $f(t)=(-e^{-2t}+e^{-t}+te^{-t})u(t)$.
- What is the intuitive meaning of partial-fraction expansion in inverse Laplace? ::@:: It decomposes a complicated proper rational transform into simple pole-generated modal blocks. <br/> Under inverse Laplace, simple poles become exponentials, repeated poles become polynomial-times-exponential terms, and conjugate pairs become damped sinusoids.
- What is the legitimate linear-algebra viewpoint behind partial fractions? ::@:: Once the denominator factorization is fixed, the corresponding proper rational functions form a finite-dimensional vector space, and the partial-fraction terms behave like a basis. <br/> Solving for the coefficients means finding the coordinates of $F(s)$ in that basis, and inverse Laplace maps those basis functions to the familiar time-domain modes.

## applications of Laplace transform

The main application payoff of Laplace transform is this workflow: start from a physical model, move to an algebraic equation in $s$, read a response transform or transfer function, and then interpret poles, damping, and stability before returning to time domain.

The recurring application chain in ELEC 2100 is

physical model $\to$ initial conditions and constitutive laws $\to$ $s$-domain equivalent model or transformed differential equation $\to$ algebraic solve in $s$ $\to$ response transform or transfer function $\to$ pole/stability interpretation $\to$ inverse Laplace transform.

A standard pair of examples is a series RLC circuit and a coupled electromechanical DC motor.  In both cases, Laplace transform is valuable because it replaces coupled differential equations by algebraic relations while preserving the same input-output physics.

---

Flashcards for this section are as follows:

- What is the recurring Laplace-transform application chain in ELEC 2100? ::@:: Physical model $\to$ initial conditions and constitutive laws $\to$ $s$-domain equivalent model or transformed differential equation $\to$ algebraic solve in $s$ $\to$ response transform or transfer function $\to$ pole/stability interpretation $\to$ inverse Laplace transform.
- Why is Laplace transform so effective for application problems in circuits and system models? ::@:: Because it converts differential and integral relations into algebraic relations in $s$, so the same framework can handle response calculation, transfer-function construction, pole interpretation, and inverse recovery to time domain.
- What two major application families are emphasized after the core Laplace rules are established? ::@:: Dynamic-circuit analysis in the Laplace domain and zero-state system-function / transfer-function analysis for networks, interconnections, and stability.

### analysis of dynamic circuits in Laplace domain

There are two mathematically equivalent starting points for dynamic-circuit analysis.

1. Write the time-domain differential/integral equation first, then apply Laplace-transform properties.
2. Draw the $s$-domain equivalent circuit directly, then write KVL/KCL there.

In this course, the second route is the main practical method because it keeps the circuit structure visible.

To draw the $s$-domain model of a dynamic circuit, keep the same electrical topology, switch position for the $t>0$ configuration, and the same reference directions for voltage and current as in the original circuit.  Then relabel every signal by its Laplace transform and replace each source and element law by its $s$-domain counterpart.  So the $s$-domain model is not a different circuit topology; it is the same circuit skeleton, but its branches are labeled by $V(s)$, $I(s)$, and element transfer relations in $s$.

The basic element models are:

- resistor: $V_R(s)=RI_R(s)$;
- inductor: $V_L(s)=LsI_L(s)-L i_L(0^-)$;
- capacitor: $V_C(s)=\frac{1}{sC}I_C(s)+\frac{v_C(0^-)}{s}$.

These formulas tell you how to draw the equivalent model.

- A resistor stays a resistor $R$.
- An inductor becomes an impedance $Ls$ together with an explicit source term carrying the stored-current information $L i_L(0^-)$.
- A capacitor becomes an impedance $\frac{1}{sC}$ together with an explicit source term carrying the stored-voltage information $\frac{v_C(0^-)}{s}$.

If the initial state is zero, those extra source terms vanish, so the $s$-domain model becomes especially simple: the same circuit with source transforms and impedances $R$, $Ls$, and $\frac{1}{sC}$.

At the network level, the standard linear circuit theorems keep the same form:

- KCL: $\sum i(t)=0 \Rightarrow \sum I(s)=0$;
- KVL: $\sum v(t)=0 \Rightarrow \sum V(s)=0$.

So once the equivalent model is drawn, ordinary linear-circuit methods still work; only the quantities have moved from time-domain waveforms to algebraic functions of $s$.

The practical solution workflow is therefore:

1. determine the pre-switch initial values $i_L(0^-)$ and $v_C(0^-)$ from the $t=0^-$ circuit;
2. draw the $t>0$ $s$-domain equivalent circuit;
3. write algebraic KVL/KCL equations;
4. solve for the desired response transform $I(s)$ or $V(s)$;
5. inverse-transform and interpret the pole pattern.

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

It is often clearer to rewrite the same denominator in the standard second-order form

$s^2+2\zeta\omega_0 s+\omega_0^2$,

where $\zeta=\frac{\alpha}{\omega_0}$ is the damping ratio.  In that notation:

- $\zeta=0$ gives the undamped poles $\pm j\omega_0$;
- $0<\zeta<1$ gives underdamped poles $-\zeta\omega_0\pm j\omega_d$, where $\omega_d=\omega_0\sqrt{1-\zeta^2}$;
- $\zeta=1$ gives the repeated real pole $-\omega_0$;
- $\zeta>1$ gives two distinct real poles $-\zeta\omega_0\pm \omega_0\sqrt{\zeta^2-1}$.

The important notation warning is that $\omega_d$ is __not__ the same thing as $\omega_0$.  The underdamped oscillation frequency is

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

This is the core dynamic-circuit message of Laplace-domain circuit analysis: unilateral Laplace transform preserves initial conditions, converts the dynamic circuit into an algebraic $s$-domain circuit, and lets the pole pattern classify the response immediately.

---

Flashcards for this section are as follows:

- When analyzing a dynamic circuit with Laplace transform, what are the two mathematically equivalent starting routes, and which one is used most in ELEC 2100? ::@:: Route 1: write the time-domain differential/integral equation first, then transform it. <br/> Route 2: draw the $s$-domain equivalent circuit directly, then write KVL/KCL there. <br/> ELEC 2100 mainly uses route 2 because it keeps the circuit structure visible.
- How should you draw the $s$-domain model of a dynamic circuit? ::@:: Keep the same topology, the same $t>0$ switch position, and the same reference directions as the original circuit. <br/> Replace time-domain variables by $V(s), I(s)$, replace sources by their Laplace transforms, and replace each element by its $s$-domain model with any initial-condition source terms included.
- What are the unilateral $s$-domain element models for ideal $R$, $L$, and $C$ (with initial states for reactive elements)? ::@:: $V_R(s)=RI_R(s)$, $V_L(s)=LsI_L(s)-Li_L(0^-)$, and $V_C(s)=\frac{1}{sC}I_C(s)+\frac{v_C(0^-)}{s}$.
- Why do KCL and KVL still work in the $s$-domain? ::@:: Because Laplace transform converts linear differential and integral element laws into algebraic relations without changing the circuit topology, so the network laws keep the same form: $\sum I(s)=0$ and $\sum V(s)=0$.
- What is the practical ELEC 2100 workflow for solving a dynamic-circuit response by Laplace transform? ::@:: Determine $i_L(0^-)$ and $v_C(0^-)$ from the $t=0^-$ circuit $\to$ draw the $t>0$ $s$-domain equivalent circuit $\to$ write algebraic KVL/KCL equations $\to$ solve for $I(s)$ or $V(s)$ $\to$ inverse-transform and interpret the pole pattern.
- For a zero-state series RLC driven by $E u(t)$, what is the $s$-domain KVL equation and the resulting current transform? ::@:: KVL is $\frac{E}{s}=\left(R+Ls+\frac{1}{sC}\right)I(s)$. <br/> Hence $I(s)=\frac{E}{Ls^2+Rs+\frac{1}{C}}=\frac{E/L}{s^2+\frac{R}{L}s+\frac{1}{LC}}$.
- For the series-RLC denominator, what are $\alpha$, $\omega_0$, and poles $p_{1,2}$? ::@:: $\alpha=\frac{R}{2L}$, $\omega_0=\frac{1}{\sqrt{LC}}$, and $p_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$.
- How are the four damping cases described using the damping ratio $\zeta$ in the standard denominator $s^2+2\zeta\omega_0 s+\omega_0^2$? ::@:: $\zeta=0$: undamped, poles $\pm j\omega_0$. <br/> $0<\zeta<1$: underdamped, poles $-\zeta\omega_0\pm j\omega_d$ with $\omega_d=\omega_0\sqrt{1-\zeta^2}$. <br/> $\zeta=1$: critically damped, repeated pole $-\omega_0$. <br/> $\zeta>1$: overdamped, two distinct real poles $-\zeta\omega_0\pm \omega_0\sqrt{\zeta^2-1}$.
- What notation pitfall must be avoided for the underdamped second-order circuit? ::@:: The oscillation frequency is the damped natural frequency $\omega_d=\omega_0\sqrt{1-\zeta^2}=\sqrt{\omega_0^2-\alpha^2}$, not the undamped natural frequency $\omega_0$ itself.
- What are the time-domain current forms for the zero-state series-RLC step response in the underdamped, critically damped, overdamped, and undamped cases? ::@:: Underdamped: $i(t)=\frac{E}{L\omega_d}e^{-\alpha t}\sin(\omega_d t)u(t)$. <br/> Critically damped: $i(t)=\frac{E}{L}t e^{-\alpha t}u(t)$. <br/> Overdamped: $i(t)=\frac{E}{L(p_1-p_2)}\left(e^{p_1 t}-e^{p_2 t}\right)u(t)$. <br/> Undamped: $i(t)=\frac{E}{L\omega_0}\sin(\omega_0 t)u(t)$.

### transfer-function viewpoint and routes

The other major Laplace-transform application is to build system functions and transfer functions from circuit diagrams, differential equations, and interconnected blocks.  The detailed system-function note now lives in [transfer function](transfer%20function.md); this Laplace note keeps only the application bridge.

For zero-state LTI analysis,

$H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$.

So the same Laplace algebra used to solve a single response also gives the system description itself.  From there, the main application questions become:

- what excitation-response pair defines the transfer function;
- how the poles and zeros are arranged in the $s$-plane;
- how cascade, parallel, and feedback interconnections change $H(s)$;
- what the pole locations say about stability and long-time behavior.

A standard electromechanical example is a DC motor with voltage input $v(t)$, armature current $i(t)$, and shaft speed $\omega(t)$ satisfying

$L\frac{di}{dt}+Ri+K_b\omega=v(t),\qquad J\frac{d\omega}{dt}+b\omega=K_t i(t)$.

With zero initial conditions, Laplace transform gives

$(Ls+R)I(s)+K_b\Omega(s)=V(s),\qquad (Js+b)\Omega(s)=K_t I(s)$.

Eliminating $I(s)$ yields the speed plant

$G_\omega(s)=\frac{\Omega(s)}{V(s)}=\frac{K_t}{(Ls+R)(Js+b)+K_tK_b}$,

and since $\Theta(s)=\frac{\Omega(s)}{s}$, the position plant is

$G_\theta(s)=\frac{\Theta(s)}{V(s)}=\frac{K_t}{s[(Ls+R)(Js+b)+K_tK_b]}$.

That example shows the full Laplace-application chain in one place: physical laws $\to$ algebraic equations in $s$ $\to$ transfer function $\to$ pole/stability analysis $\to$ feedback design language.

The quick stability rule used throughout the course is: for a causal rational system, all poles strictly in the left half-plane imply asymptotic BIBO stability.  Simple poles on the imaginary axis give marginal (non-decaying but non-growing) behavior, while any right-half-plane pole or any repeated pole on the imaginary axis gives instability.

---

Flashcards for this section are as follows:

- In the Laplace-transform application viewpoint, what does $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$ mean? ::@:: It means the zero-state input-output ratio of an LTI system equals the Laplace transform of its impulse response, so the same transform framework describes both a single response and the system itself.
- How does the DC motor example show the application chain from physical laws to transfer function? ::@:: The motor equations $L\dot i+Ri+K_b\omega=v$ and $J\dot\omega+b\omega=K_t i$ become two algebraic equations in $s$, which can be combined into $G_\omega(s)=\frac{K_t}{(Ls+R)(Js+b)+K_tK_b}$ and $G_\theta(s)=\frac{K_t}{s[(Ls+R)(Js+b)+K_tK_b]}$. <br/> So Laplace transform turns coupled dynamics into transfer functions whose poles can be analyzed directly.
- Where should the full system-function / transfer-function / stability material now be studied? ::@:: In [transfer function](transfer%20function.md). <br/> `Laplace transform.md` keeps the application bridge, while the dedicated note holds the full system-function development.
- What is the quick causal-rational stability rule used in the Laplace application notes? ::@:: All poles strictly in the left half-plane imply asymptotic BIBO stability; simple poles on the imaginary axis give marginal behavior; any RHP pole or repeated imaginary-axis pole gives instability.

## relation between Laplace transform and Fourier transform

Laplace and Fourier are connected syntactically, operationally, and semantically.

__Syntactic connection (bilateral Laplace).__ Recall the Fourier transform $\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}\,dt$.  The bilateral Laplace transform $F(s)=\int_{-\infty}^{\infty}f(t)e^{-st}\,dt$ is obtained by formally substituting $j\omega\to s$, so $F(s)=\hat f(\omega)\big|_{j\omega\,\to\,s}$.

Evaluating back at $s=j\omega$ recovers the Fourier transform, provided the imaginary axis lies in the ROC; evaluating outside the ROC is undefined.  Boundary cases on the imaginary axis (e.g. unit step, sinusoids) can require distributional (impulse-containing) Fourier representations.

__Operational connection (unilateral Laplace as windowing then bilateral transform).__ The right-sided unilateral transform equals the bilateral Laplace transform of the windowed signal $f(t)u(t)$, namely $\mathcal{L}_u\{f\}(s)=\int_{0^-}^{\infty}f(t)e^{-st}\,dt=\int_{-\infty}^{\infty}f(t)u(t)e^{-st}\,dt=\mathcal{L}_{bilateral}\{f(t)u(t)\}(s)$.

Operationally, two steps are applied in order: (1) multiply $f(t)$ by $u(t)$, zeroing out $t<0$; (2) apply the bilateral Laplace transform.  In the $s$-domain, time-domain multiplication by a function corresponds, via the complex-convolution theorem (the Laplace analogue of Fourier's frequency-domain convolution rule), to convolving with the Laplace transform of that function along a vertical contour; since the bilateral Laplace of $u(t)$ is $1/s$, the windowing step corresponds to convolving $F(s)$ with $1/s$ in this complex-contour sense.

Symmetrically, the left-sided unilateral transform uses $u(-t)$, so $\mathcal{L}_{-}\{f\}(s)=\mathcal{L}_{bilateral}\{f(t)u(-t)\}(s)$, zeroing out $t>0$ before applying the bilateral transform.

__Semantic connection (Laplace as Fourier of an exponentially weighted signal).__ Writing $s=\sigma+j\omega$, the bilateral Laplace transform factors as $F(\sigma+j\omega)=\int_{-\infty}^{\infty}\bigl[f(t)e^{-\sigma t}\bigr]e^{-j\omega t}\,dt=\mathcal{F}\!\left\{f(t)e^{-\sigma t}\right\}(\omega)$.

The roles of the two parts of $s$ are now explicit:

- The imaginary part $j\omega$ is the ordinary Fourier frequency variable; it provides the oscillatory probe $e^{-j\omega t}$ for spectral decomposition.
- The real part $\sigma=\text{Re}\{s\}$ controls an exponential weight $e^{-\sigma t}$ applied before the Fourier transform:
    - $\sigma>0$: the weight decays forward in time, suppressing exponential growth in $f(t)$ and expanding the class of transformable signals beyond those with a classical Fourier transform.
    - $\sigma=0$: the weight is unity; $F(j\omega)$ reduces to the ordinary Fourier transform $\hat f(\omega)$ (when the imaginary axis is in the ROC).
    - $\sigma<0$: the weight grows forward in time; convergence requires $f(t)$ to decay rapidly enough to compensate.

The ROC is therefore the vertical strip $\sigma_1<\text{Re}\{s\}<\sigma_2$ for which the exponentially weighted signal $f(t)e^{-\sigma t}$ is Fourier-transformable.

__Why Fourier has duality but Laplace generally does not.__ Fourier transform has a genuine duality theorem because its kernel is symmetric between the time and frequency variables up to constants and sign reversal.  Laplace transform loses that symmetry: exponential weighting changes convergence, the ROC must be tracked explicitly, and unilateral Laplace adds boundary/initial-condition terms.  Therefore ELEC 2100 treats convolution theorem and multiplication theorem as separate statements, but does not rely on a single standard Laplace "duality theorem" analogous to Fourier duality.

__Recovery of Fourier transform, ROC cases, and impulse corrections.__ The test $F(j\omega)=F(s)\vert_{s=j\omega}$ has three distinct cases, depending on where the imaginary axis sits relative to the ROC.

- __Imaginary axis strictly inside the ROC__: the exponential weighting is no longer needed at $\sigma=0$, so the ordinary Fourier transform exists and is obtained by direct substitution.  Example: for $f(t)=e^{-\alpha t}u(t)$ with $\alpha>0$, $F(s)=\frac{1}{s+\alpha}$ and ROC $\operatorname{Re}\{s\}>-\alpha$, so the imaginary axis lies inside the ROC and $\hat f(\omega)=F(j\omega)=\frac{1}{\alpha+j\omega}$.
- __Imaginary axis outside the ROC__: evaluating at $s=j\omega$ is invalid because the weighting needed for convergence has been removed too early.  Example: for $f(t)=e^{\alpha t}u(t)$ with $\alpha>0$, $F(s)=\frac{1}{s-\alpha}$ and ROC $\operatorname{Re}\{s\}>\alpha$, so the imaginary axis lies outside the ROC and no classical Fourier transform exists.
- __Imaginary axis on the ROC boundary__: direct substitution hits a boundary singularity.  The correct object is then a __generalized Fourier transform__, obtained by approaching the imaginary axis from inside the ROC, separating the principal-value part from the impulse part, and only then taking the limit.

The unit step is the canonical boundary example.  Its unilateral and bilateral Laplace transform is $F(s)=\frac{1}{s}$ with ROC $\operatorname{Re}\{s\}>0$.  Approach the boundary from the right: $F(\sigma+j\omega)=\frac{1}{\sigma+j\omega}=\frac{\sigma}{\sigma^2+\omega^2}-j\frac{\omega}{\sigma^2+\omega^2}$.  As $\sigma\to0^+$, the real part $\frac{\sigma}{\sigma^2+\omega^2}$ is the Poisson kernel, whose integral over $\omega$ is always $\pi$, so it collapses to $\pi\delta(\omega)$.  The imaginary part tends to the Cauchy principal value $\operatorname{PV}\!\left(\frac{1}{j\omega}\right)$.  Therefore $\mathcal{F}\{u(t)\}=\pi\delta(\omega)+\operatorname{PV}\!\left(\frac{1}{j\omega}\right)$.  The factor $\pi$ is not guessed; it is the total area of the boundary-approach kernel.

The same mechanism gives the shifted simple-pole rule.  If the principal part of $F(s)$ near a boundary pole $s=j\omega_0$ is $\frac{R}{s-j\omega_0}$, where $R$ is the residue, then approaching from the ROC side gives $\frac{R}{\sigma+j(\omega-\omega_0)}\to \operatorname{PV}\!\left(\frac{R}{j(\omega-\omega_0)}\right)+\pi R\,\delta(\omega-\omega_0)$.  So a first-order pole on the imaginary axis contributes both a principal-value rational term and an impulse whose coefficient is $\pi$ times the residue.  This recovers, for example, $e^{j\omega_0 t}u(t)\longleftrightarrow \operatorname{PV}\!\left(\frac{1}{j(\omega-\omega_0)}\right)+\pi\delta(\omega-\omega_0)$.

Repeated boundary poles sharpen the singular part.  If the principal part near $s=j\omega_0$ is $\sum_{m=1}^{M}\frac{a_m}{(s-j\omega_0)^m}$, then each order-$m$ term contributes $\frac{a_m}{(\sigma+j(\omega-\omega_0))^m}\to \operatorname{PV}\!\left(\frac{a_m}{[j(\omega-\omega_0)]^m}\right)+\frac{\pi a_m}{(m-1)!(-j)^{m-1}}\,\delta^{(m-1)}(\omega-\omega_0)$.  In particular, $\frac{1}{(s-j\omega_0)^2}$ produces $\operatorname{PV}\!\left(\frac{1}{[j(\omega-\omega_0)]^2}\right)+j\pi\delta'(\omega-\omega_0)$.  The derivative order rises because higher-order poles correspond in time to factors such as $t^{m-1}e^{j\omega_0 t}u(t)$, and multiplication by powers of $t$ becomes differentiation with respect to frequency, so the impulse term is differentiated too.

Therefore the practical recovery rule is: first locate the imaginary axis relative to the ROC; next separate any boundary-pole principal parts; finally write the generalized Fourier transform as the ordinary $F(j\omega)$ contribution away from boundary poles, plus the principal-value limits, plus the impulse or impulse-derivative corrections generated by the imaginary-axis poles.

---

Flashcards for this section are as follows:

- Syntactically, how does the bilateral Laplace transform relate to the Fourier transform? ::@:: The bilateral Laplace transform $F(s)$ is obtained from the Fourier transform $\hat f(\omega)$ by substituting $j\omega\to s$: $F(s)=\hat f(\omega)|_{j\omega\to s}$. <br/> Evaluating at $s=j\omega$ recovers $\hat f(\omega)$ when the imaginary axis is in the ROC.
- How is the right-sided unilateral Laplace transform expressed as a two-step bilateral procedure? ::@:: Step 1: multiply $f(t)$ by $u(t)$ to zero out $t<0$. <br/> Step 2: apply the bilateral Laplace transform. <br/> Result: $\mathcal{L}_u\{f\}(s)=\mathcal{L}_{bilateral}\{f(t)u(t)\}(s)$. <br/> In the $s$-domain this windowing corresponds (via the complex-convolution theorem) to convolving with $1/s$, the bilateral Laplace of $u(t)$.
- What is the analogous two-step procedure for the left-sided unilateral Laplace transform? ::@:: Step 1: multiply $f(t)$ by $u(-t)$ to zero out $t>0$. <br/> Step 2: apply the bilateral Laplace transform. <br/> Result: $\mathcal{L}_{-}\{f\}(s)=\mathcal{L}_{bilateral}\{f(t)u(-t)\}(s)$.
- Semantically, what is $F(\sigma+j\omega)$ equal to in terms of a Fourier transform? ::@:: $F(\sigma+j\omega)=\mathcal{F}\{f(t)e^{-\sigma t}\}(\omega)$: the Laplace transform at $s=\sigma+j\omega$ is the Fourier transform of the exponentially weighted signal $f(t)e^{-\sigma t}$.
- In the semantic Laplace–Fourier decomposition, what role does $\text{Re}\{s\}=\sigma>0$ play? ::@:: The factor $e^{-\sigma t}$ decays forward in time, suppressing exponential growth in $f(t)$ and expanding the set of signals whose transform exists beyond those that are directly Fourier-transformable.
- What are the three cases for recovering a Fourier transform from $F(s)$ by testing the imaginary axis against the ROC? ::@:: If the imaginary axis lies strictly inside the ROC, the ordinary Fourier transform exists and is obtained by direct substitution $F(j\omega)$. <br/> If the imaginary axis lies outside the ROC, direct substitution is invalid and no classical Fourier transform exists. <br/> If the imaginary axis is the ROC boundary, one must take a boundary limit from within the ROC and write a generalized Fourier transform containing principal-value and impulse terms.
- Why does $f(t)=e^{\alpha t}u(t)$ with $\alpha>0$ have a Laplace transform but no classical Fourier transform? ::@:: Its Laplace transform is $F(s)=\frac{1}{s-\alpha}$ with ROC $\operatorname{Re}\{s\}>\alpha$, so the imaginary axis lies outside the ROC. <br/> The exponential weight is still needed for convergence at $\sigma=0$, so $F(j\omega)$ is not a valid Fourier-transform evaluation.
- Derive the Fourier transform of $u(t)$ from the boundary limit of $F(s)=\frac{1}{s}$. ::@:: Step 1: approach the imaginary axis from inside the ROC: $\frac{1}{\sigma+j\omega}=\frac{\sigma}{\sigma^2+\omega^2}-j\frac{\omega}{\sigma^2+\omega^2}$. <br/> Step 2: as $\sigma\to0^+$, the real part is the Poisson kernel, whose area is $\pi$, so it tends to $\pi\delta(\omega)$. <br/> Step 3: the imaginary part tends to the principal value $\operatorname{PV}\!\left(\frac{1}{j\omega}\right)$. <br/> Step 4: therefore $\mathcal{F}\{u(t)\}=\pi\delta(\omega)+\operatorname{PV}\!\left(\frac{1}{j\omega}\right)$.
- If $F(s)$ has a simple boundary pole with principal part $\frac{R}{s-j\omega_0}$, what generalized Fourier-transform correction appears? ::@:: The boundary limit becomes $\operatorname{PV}\!\left(\frac{R}{j(\omega-\omega_0)}\right)+\pi R\,\delta(\omega-\omega_0)$. <br/> So a first-order imaginary-axis pole contributes both a principal-value rational term and an impulse whose coefficient is $\pi$ times the residue.
- If $F(s)$ has an order-$m$ boundary pole term $\frac{a_m}{(s-j\omega_0)^m}$, what singular Fourier term appears, and why does its order increase? ::@:: It contributes $\operatorname{PV}\!\left(\frac{a_m}{[j(\omega-\omega_0)]^m}\right)+\frac{\pi a_m}{(m-1)!(-j)^{m-1}}\,\delta^{(m-1)}(\omega-\omega_0)$. <br/> The derivative order rises because higher-order poles correspond to time-domain factors such as $t^{m-1}e^{j\omega_0 t}u(t)$, and multiplying by powers of $t$ becomes differentiation with respect to frequency.
- Why is there no standard Laplace duality theorem analogous to Fourier duality in ELEC 2100? ::@:: Fourier has a true symmetry between time and frequency variables, so it has a standard duality theorem. <br/> Laplace generally does not, because exponential weighting changes convergence, the ROC must be tracked explicitly, and unilateral Laplace adds boundary/initial-condition terms. <br/> So ELEC 2100 uses separate convolution and multiplication theorems instead of one duality rule.

## inverse Laplace transform via Bromwich integral

The inversion formula for the Laplace transform is the __Bromwich contour integral__: $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}\,ds$, where $\sigma$ is any real number such that the vertical line $\text{Re}\{s\}=\sigma$ lies within the ROC of $F$.  Integration runs along this entire vertical line in the complex $s$-plane.

__Independence from the choice of $\sigma$ within the ROC.__ Different choices of $\sigma$ within the ROC yield the same $f(t)$.  This follows from the __Cauchy integral theorem__: $F(s)$ is analytic (holomorphic, pole-free) throughout the interior of the ROC.  Shifting the vertical integration contour left or right while staying inside the ROC traces a path through a region where $F(s)e^{st}$ is analytic; by the Cauchy theorem, the integral of an analytic function is unchanged under such a homotopic deformation of the contour.  In practice, this means one may choose any convenient $\sigma$ in the ROC—e.g.\ one that simplifies closing the contour for residue evaluation.

__Recovering inverse Fourier transform as a special case.__ When the imaginary axis $\text{Re}\{s\}=0$ lies within the ROC, set $\sigma=0$ and substitute $s=j\omega$, $ds=j\,d\omega$; then $f(t)=\frac{1}{2\pi j}\int_{-j\infty}^{j\infty}F(j\omega)e^{j\omega t}j\,d\omega=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(j\omega)e^{j\omega t}\,d\omega$, which is exactly the inverse Fourier transform formula.  Laplace inversion on the imaginary axis is therefore Fourier inversion in disguise: a variable substitution $s=j\omega$ converts one into the other.

In practice, for a rational $F(s)$ with a right-sided ROC, Bromwich inversion is evaluated by a concrete residue workflow.

1. Choose the Bromwich line $\Re(s)=\sigma$ inside the ROC, so for a right-sided ROC it lies to the right of every finite pole.
2. Write the inverse integral for $F(s)e^{st}$.
3. For $t>0$, close the contour with a semicircular arc $\Gamma_R$ of radius $R$ in the __left__ half-plane, so the full contour consists of the Bromwich segment plus $\Gamma_R$.
4. Let $R\to\infty$.  On $\Gamma_R$, the factor $e^{st}=e^{\Re(s)t}e^{j\Im(s)t}$ decays because $\Re(s)\to-\infty$, and for a strictly proper rational $F(s)$ we also have $F(s)=O(1/R)$ on the arc.  Hence the arc integral over $\Gamma_R$ vanishes as $R\to\infty$ by the ML estimate (equivalently, Jordan's lemma).
5. The remaining integral is therefore the Bromwich line integral, and the closed contour encloses all finite poles of $F(s)$ to the left of the Bromwich line.  By the residue theorem, the Bromwich integral equals $2\pi j$ times the sum of residues of $F(s)e^{st}$ at those poles.
6. For a causal right-sided signal, write the recovered expression multiplied by $u(t)$.

Residue calculation itself should also be done step by step.

- __Simple pole at $p$__: compute $\operatorname*{Res}_{s=p}[F(s)e^{st}]$ by multiplying by $(s-p)$, then evaluating at $s=p$.
- __Repeated pole of order $m$ at $p$__: compute $\operatorname*{Res}_{s=p}[F(s)e^{st}]$ by first multiplying by $(s-p)^m$, then differentiating $m-1$ times, dividing by $(m-1)!$, and finally evaluating at $s=p$.
- __Complex-conjugate poles__: compute one residue and use the conjugate partner to combine the pair into a real damped sinusoid.

This makes Bromwich inversion a theorem-based version of the same pole collection used in partial fractions: contour integration sums modal contributions from the poles, while partial fractions lists those same modal terms directly.

A concrete example is $F(s)=\frac{1}{s(s+1)}$, with ROC $\Re(s)>0$.  Then the Bromwich integral is $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}\frac{e^{st}}{s(s+1)}\,ds$, where $\sigma>0$.

For $t>0$, close the contour to the left and let $R\to\infty$, so the arc contribution vanishes and only residues remain.  The enclosed poles are at $s=0$ and $s=-1$, both simple.

- At $s=0$, multiply by $s$: $\operatorname*{Res}_{s=0}\frac{e^{st}}{s(s+1)}=\left.s\frac{e^{st}}{s(s+1)}\right|_{s=0}=\left.\frac{e^{st}}{s+1}\right|_{s=0}=1$.
- At $s=-1$, multiply by $s+1$: $\operatorname*{Res}_{s=-1}\frac{e^{st}}{s(s+1)}=\left.(s+1)\frac{e^{st}}{s(s+1)}\right|_{s=-1}=\left.\frac{e^{st}}{s}\right|_{s=-1}=-e^{-t}$.

Add the residues to get $f(t)=1-e^{-t}$ for $t>0$, so the causal inverse is $(1-e^{-t})u(t)$.

This is exactly the same answer obtained from partial fractions, since $\frac{1}{s(s+1)}=\frac{1}{s}-\frac{1}{s+1}$, showing how Bromwich inversion justifies the table-lookup shortcut.

A repeated-pole example makes the higher-order residue rule concrete.  Let $F(s)=\frac{1}{(s+1)^3}$ with ROC $\Re(s)>-1$.  Then $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}\frac{e^{st}}{(s+1)^3}\,ds$ with $\sigma>-1$.

For $t>0$, close the contour to the left and let $R\to\infty$.  Again the arc contribution vanishes, and now the only enclosed pole is $s=-1$, but it is a __triple pole__.

Use the order-$3$ residue formula:

$\operatorname*{Res}_{s=-1}\frac{e^{st}}{(s+1)^3}=\frac{1}{2!}\left.\frac{d^2}{ds^2}\left[(s+1)^3\frac{e^{st}}{(s+1)^3}\right]\right|_{s=-1}=\frac{1}{2}\left.\frac{d^2}{ds^2}e^{st}\right|_{s=-1}$.

Differentiate step by step:

$\frac{d}{ds}e^{st}=t e^{st},\qquad \frac{d^2}{ds^2}e^{st}=t^2 e^{st}$.

So the residue is

$\operatorname*{Res}_{s=-1}\frac{e^{st}}{(s+1)^3}=\frac{1}{2}t^2 e^{-t}$.

Since this is the only enclosed pole, the inverse Laplace transform is

$f(t)=\frac{t^2}{2}e^{-t}u(t)$.

This matches the standard table pair $\frac{1}{(s+1)^3}\longleftrightarrow \frac{t^2}{2}e^{-t}u(t)$ and shows explicitly how Bromwich inversion handles a repeated pole of order $m=3$.

---

Flashcards for this section are as follows:

- State the Bromwich integral formula for the inverse Laplace transform. ::@:: $f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}\,ds$, where $\sigma=\text{Re}\{s\}$ is any value within the ROC of $F$.
- Why does the Bromwich integral give the same $f(t)$ for any $\sigma$ chosen within the ROC? ::@:: $F(s)$ is analytic (holomorphic, pole-free) in the interior of the ROC. <br/> By the Cauchy integral theorem, shifting the vertical integration line within an analytic region (a homotopic deformation through a pole-free domain) does not change the contour integral.
- Derive how the Bromwich integral on the imaginary axis reduces to the inverse Fourier transform. ::@:: Set $\sigma=0$ (valid when the imaginary axis is in the ROC), substitute $s=j\omega$ and $ds=j\,d\omega$: <br/> $\frac{1}{2\pi j}\int_{-j\infty}^{j\infty}F(j\omega)e^{j\omega t}j\,d\omega=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(j\omega)e^{j\omega t}\,d\omega$, <br/> which is the inverse Fourier transform formula.
- For a rational $F(s)$ with a right-sided ROC, what is the concrete Bromwich-evaluation workflow in practice? ::@:: Choose the Bromwich line inside the ROC and to the right of all finite poles. <br/> For $t>0$, close it with a left semicircle $\Gamma_R$, then let $R\to\infty$. <br/> On $\Gamma_R$, $e^{st}$ decays and a strictly proper rational $F(s)$ is $O(1/R)$, so the arc integral vanishes by the ML estimate / Jordan's lemma. <br/> The Bromwich line integral is therefore $2\pi j$ times the sum of residues of $F(s)e^{st}$ at the enclosed poles, and the final right-sided answer is written with $u(t)$.
- How are residues of $F(s)e^{st}$ computed in Bromwich inversion for simple poles, repeated poles, and conjugate pairs? ::@:: Simple pole: multiply by $(s-p)$ and evaluate at $s=p$. <br/> Repeated pole of order $m$: multiply by $(s-p)^m$, differentiate $m-1$ times, divide by $(m-1)!$, then evaluate at $s=p$. <br/> Conjugate pair: compute one residue and combine it with its conjugate partner to form a real damped sinusoid.
- Use Bromwich inversion to evaluate $F(s)=\frac{1}{s(s+1)}$ with ROC $\Re(s)>0$, including the residue steps. ::@:: Write $f(t)=\frac{1}{2\pi j}\int \frac{e^{st}}{s(s+1)}ds$ with the Bromwich line to the right of $0$ and $-1$. <br/> For $t>0$, close left and let $R\to\infty$, so the arc vanishes. <br/> At $s=0$, multiply by $s$ to get the residue $\frac{e^{st}}{s+1}\big|_{s=0}=1$. <br/> At $s=-1$, multiply by $s+1$ to get the residue $\frac{e^{st}}{s}\big|_{s=-1}=-e^{-t}$. <br/> Hence $f(t)=1-e^{-t}$ for $t>0$, so the causal inverse is $(1-e^{-t})u(t)$.
- Use Bromwich inversion to evaluate $F(s)=\frac{1}{(s+1)^3}$ with ROC $\Re(s)>-1$, including the repeated-pole residue steps. ::@:: Write $f(t)=\frac{1}{2\pi j}\int \frac{e^{st}}{(s+1)^3}ds$ with the Bromwich line to the right of $-1$. <br/> For $t>0$, close left and let $R\to\infty$, so the arc vanishes. <br/> The only enclosed pole is the triple pole $s=-1$, so use the order-3 residue rule: $\operatorname*{Res}_{s=-1}=\frac{1}{2!}\frac{d^2}{ds^2}e^{st}\big|_{s=-1}=\frac{1}{2}t^2e^{-t}$. <br/> Hence $f(t)=\frac{t^2}{2}e^{-t}u(t)$.
- Why does Bromwich inversion and partial fractions give the same answer for a proper rational $F(s)$? ::@:: Because both methods are summing the same pole contributions. <br/> Bromwich contour integration collects them through residues of $F(s)e^{st}$, while partial fractions writes those same modal terms explicitly for direct table lookup.
