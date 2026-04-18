---
aliases:
  - ELEC 2100 singular signal
  - ELEC 2100 singular signals
  - ELEC2100 singular signal
  - ELEC2100 singular signals
  - HKUST ELEC 2100 singular signal
  - HKUST ELEC 2100 singular signals
  - HKUST ELEC2100 singular signal
  - HKUST ELEC2100 singular signals
  - singular signal
  - singular signals
  - singularity signal
  - singularity signals
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/singular_signal
  - language/in/English
---

# singular signal

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Singular signals are idealized building blocks used to model switching, sampling, and abruptly concentrated change. ELEC 2100 develops them early because later convolution, LTI modeling, and transform methods repeatedly rely on step-, impulse-, and derivative-type signals.

Within the signal-family notes, this file is the specialized continuous-time generalized-signal toolkit. The broad language of signals remains in [signal](signal.md), and the sample-indexed toolkit remains in [discrete-time signal](discrete-time%20signal.md). This separation keeps ordinary signal classification, discrete-time sequences, and generalized singular objects from being mixed together unnecessarily.

---

Flashcards for this section are as follows:

- Why do singular signals matter in ELEC 2100? ::@:: They model switching, sampling, and abruptly concentrated change, so they recur throughout later signal-and-system analysis.
- Why are singular signals introduced so early in ELEC 2100? ::@:: Later convolution, LTI modeling, and transform methods depend on them.
- How should `singular signal.md` be positioned relative to the other signal-family notes? ::@:: It is the specialized continuous-time generalized-signal toolkit for step, impulse, and derivative-type objects. The broader vocabulary stays in `signal.md`, and the sequence toolkit stays in `discrete-time signal.md`.

## singular-signal overview

The course uses the term _singular signals_ or _singularity functions_ for signals that either contain discontinuities themselves or produce concentrated discontinuities when differentiated or integrated. The main family introduced in ELEC 2100 is the chain $r(t) \to u(t) \to \delta(t) \to \delta'(t)$, where each differentiation concentrates change more sharply than the previous signal.

A useful first split is ordinary versus generalized objects. Ramp, step, gate, and signum are still ordinary piecewise-defined functions. They can be drawn as genuine curves or line segments on the time axis. By contrast, the impulse and the doublet are generalized functions: their graphs are symbolic rather than literal finite-height waveforms. For an impulse, the key quantity is area. For a doublet, the key quantity is derivative action or slope extraction.

This is why the phrase "infinitely tall narrow pulse" is only a heuristic. It is good intuition for how approximating families behave, but the generalized object itself is defined by how it acts under integration. A clean rule of thumb is therefore: ordinary singular signals are drawn as ordinary piecewise graphs, while generalized singular signals are drawn with symbolic arrows or derivative-style markers that encode location, sign, and strength rather than a literal pointwise amplitude.

---

Flashcards for this section are as follows:

- What are singular signals? ::@:: They are signals that either contain discontinuities themselves or produce concentrated discontinuities when differentiated or integrated.
- What is the main singular-signal chain introduced in the early ELEC 2100 signal material? ::@:: It is $r(t) \to u(t) \to \delta(t) \to \delta'(t)$.
- What is the difference between ordinary and generalized singular signals? ::@:: Ramp, step, gate, and signum are ordinary piecewise functions, whereas the impulse and doublet are generalized functions with symbolic graphs.
- What does the graph of an impulse represent? ::@:: It represents location, sign, and area rather than an ordinary pointwise height.
- What does the graph of a doublet represent? ::@:: It represents derivative action or slope extraction rather than an ordinary waveform amplitude.
- Why is the phrase "infinitely tall narrow pulse" only heuristic? ::@:: It is useful limiting intuition, but the generalized impulse is defined by its action under integration rather than by ordinary pointwise height.

## ramp, step, gate, and signum

The unit step and unit ramp are the simplest singular signals. The unit step is $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$, with the value at $t=0$ either left undefined or assigned by convention. The unit ramp is $r(t)=tu(t)$, so $r(t)=0$ for $t<0$ and $r(t)=t$ for $t>0$.

The graphing rule is straightforward: draw the pre-switch part first, then the post-switch part. For $u(t-t_0)$, keep the graph at $0$ for $t<t_0$, place the jump at $t=t_0$, and draw the level $1$ for $t>t_0$. For $r(t-t_0)$, keep the graph at $0$ up to $t=t_0$, then begin a line of slope $1$ measured from that switching time.

The distinction between step and ramp is useful. A step jumps and then stays flat. A ramp turns on at one instant and then continues to grow linearly. Thus the ramp stores a whole interval of accumulated growth after the switching point, whereas the step stores only the information that a switch has occurred.

Finite windows are built by subtracting shifted steps. A gate or rectangular signal active on $[a,b)$ can be written as $u(t-a)-u(t-b)$. The symmetric gate of width $\tau$ is $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, which equals $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$. To sketch a gate, locate the left and right switching instants first, then fill the graph with level $1$ between them and level $0$ outside.

The signum function belongs to the same family even though it is not pulse-shaped. It is $-1$ for negative time, $+1$ for positive time, and is usually assigned the value $0$ at the origin by convention. It is related to the unit step by $\operatorname{sgn}(t)=2u(t)-1$ away from the origin, or equivalently $\operatorname{sgn}(t)=u(t)-u(-t)$ with care about the convention at $t=0$. This is a useful counterexample to the idea that all singular-looking signals must be nonnegative or pulse-like.

---

Flashcards for this section are as follows:

- What is the unit step? ::@:: It is $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$, with the value at $t=0$ set by convention if needed.
- What is the unit ramp? ::@:: It is $r(t)=tu(t)$, so it is $0$ for negative time and then grows linearly for positive time.
- How do you draw $u(t-t_0)$? ::@:: Keep the graph at $0$ for $t<t_0$, place the jump at $t=t_0$, and draw the level $1$ for $t>t_0$.
- How do you draw $r(t-t_0)$? ::@:: Keep the graph at $0$ until $t=t_0$, then start a line of slope $1$ measured from that switching time.
- What is the difference between a step and a ramp? ::@:: A step jumps and then stays flat, whereas a ramp turns on at one instant and then continues to grow linearly.
- How can a rectangular gate on $[a,b)$ be written using steps? ::@:: It can be written as $u(t-a)-u(t-b)$.
- What is the symmetric gate of width $\tau$? ::@:: It is $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$.
- How do you draw the symmetric gate? ::@:: It equals $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$, so its graph is a centered rectangular window.
- What is the signum function? ::@:: It is $-1$ for negative time, $+1$ for positive time, and usually $0$ at the origin by convention.
- How is the signum function related to the unit step? ::@:: Away from the origin, $\operatorname{sgn}(t)=2u(t)-1$.
- What is another step-based expression for the signum function? ::@:: It may be written as $\operatorname{sgn}(t)=u(t)-u(-t)$, with care about the convention at the origin.
- Worked example (method: gate-decomposition graphing): Given $g(t)=u(t-1)-u(t-3)$, what is its graph? ::@:: Step 1: the first step turns on at $t=1$, so the signal jumps from $0$ to $1$ there. <br/> Step 2: the second step turns on at $t=3$ with a minus sign, so the signal drops back by $1$ there. <br/> Step 3: therefore $g(t)=0$ for $t<1$, $1$ for $1<t<3$, and $0$ for $t>3$, i.e. a rectangular pulse between $1$ and $3$.
- Why does a gate differentiate to an impulse pair while a step differentiates to one impulse? ::@:: A step has one switching edge, whereas a gate has two switching edges.

## unit impulse: pulse limits and generalized functions

The course presents the unit impulse from two mutually reinforcing viewpoints: as the limit of ordinary pulses and as a generalized function defined by its action on test functions. The pulse-limit viewpoint gives intuition; the generalized-function viewpoint gives the precise mathematical rule.

A standard rectangular delta sequence is $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$ and $0$ otherwise. Its width is $\varepsilon$, its height is $1/\varepsilon$, and its area is $\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon)dt=1$. As $\varepsilon\to 0$, the pulse becomes narrower and taller while keeping unit area. This is the core normalization idea behind all delta sequences: the detailed shape may vary, but the total area must stay equal to $1$.

Other unit-area families show the same idea from different angles. A triangular approximation may be written as $\delta_\varepsilon(t)=\frac{1}{\varepsilon}(1-|t|/\varepsilon)$ for $|t|<\varepsilon$ and $0$ otherwise, and its area is $2\int_0^{\varepsilon}\frac{1}{\varepsilon}(1-t/\varepsilon)dt=1$. A double-sided exponential approximation is $\delta_\varepsilon(t)=\frac{1}{2\varepsilon}e^{-|t|/\varepsilon}$, whose area is $2\int_0^{\infty}\frac{1}{2\varepsilon}e^{-t/\varepsilon}dt=1$. A Gaussian approximation is $\delta_\varepsilon(t)=\frac{1}{\sqrt{\pi}\varepsilon}e^{-(t/\varepsilon)^2}$, whose area becomes $\frac{1}{\sqrt{\pi}}\int_{-\infty}^{\infty}e^{-u^2}du=1$ after substituting $u=t/\varepsilon$. A sinc-shaped family such as $\delta_\varepsilon(t)=\frac{1}{\pi}\frac{\sin(t/\varepsilon)}{t}=\frac{1}{\pi\varepsilon}\operatorname{Sa}(t/\varepsilon)$ also has unit area. The important common feature is concentration near one point together with total area $1$.

The generalized-function viewpoint says that the impulse is not an ordinary finite-valued waveform at all. Instead, for a smooth compactly supported test function $f(t)$, the defining rule is $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$. The impulse is therefore defined by its action under integration. A test function is just a smooth local probe: smoothness is what makes later differentiation rules legitimate, and compact support is what removes boundary terms in integration-by-parts arguments.

The pulse-limit and generalized-function viewpoints fit together. If $\delta_\varepsilon$ has unit area and support shrinking to the origin, then $\int\delta_\varepsilon(t)f(t)dt=\int\delta_\varepsilon(t)(f(t)-f(0))dt+f(0)\int\delta_\varepsilon(t)dt$. The second term is exactly $f(0)$ because the area is $1$. The first term vanishes because the pulse is so narrow that a smooth function looks almost flat inside it, so $f(t)-f(0)$ is tiny there. So the limit samples the value at the support point: unit area keeps the $f(0)$ term alive, and concentration kills the remainder.

Graphically, the impulse is drawn as a symbolic arrow. The arrow indicates location and weight, not literal height. The graph of $\delta(t-t_0)$ is an arrow at $t=t_0$ labeled with area $1$. The graph of $A\delta(t-t_0)$ is an arrow at the same location labeled with weight $A$. Treating the impulse as a pointwise zero-width rectangle is therefore a category mistake: the correct meaning is always through its action in integrals.

A final warning is that the ideal impulse does not fit the ordinary finite-energy framework. For the rectangular approximation above, $E_\varepsilon=\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon^2)dt=1/\varepsilon\to\infty$, so the approximating energy blows up as the pulse concentrates.

---

Flashcards for this section are as follows:

- What are the two main viewpoints on the unit impulse? ::@:: It is understood both as the limit of unit-area pulse families and as a generalized function defined by its action on test functions.
- What is a standard rectangular delta sequence? ::@:: It is $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$ and $0$ otherwise.
- Why does the rectangular delta sequence have unit area? ::@:: Because $\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon)dt=1$.
- Why is unit area the crucial normalization in delta sequences? ::@:: Keeping total area equal to $1$ is what makes the limiting sampling action nontrivial and correctly normalized.
- What is a triangular delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\varepsilon}(1-|t|/\varepsilon)$ for $|t|<\varepsilon$ and $0$ otherwise.
- Why does the triangular delta sequence have unit area? ::@:: Symmetry gives $2\int_0^{\varepsilon}\frac{1}{\varepsilon}(1-t/\varepsilon)dt=1$.
- What is a double-sided exponential delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{2\varepsilon}e^{-|t|/\varepsilon}$.
- Why does the double-sided exponential delta sequence have unit area? ::@:: Symmetry gives $2\int_0^{\infty}\frac{1}{2\varepsilon}e^{-t/\varepsilon}dt=1$.
- What is a Gaussian delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\sqrt{\pi}\varepsilon}e^{-(t/\varepsilon)^2}$.
- Why does the Gaussian delta sequence have unit area? ::@:: Substituting $u=t/\varepsilon$ gives $\frac{1}{\sqrt{\pi}}\int_{-\infty}^{\infty}e^{-u^2}du=1$.
- What is a sinc-shaped delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\pi}\frac{\sin(t/\varepsilon)}{t}=\frac{1}{\pi\varepsilon}\operatorname{Sa}(t/\varepsilon)$.
- What is the generalized-function definition of the impulse? ::@:: For a suitable test function $f(t)$, it is defined by $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$.
- What are test functions conceptually? ::@:: They are smooth localized probe functions used to check how a generalized signal behaves inside an integral.
- Why do test functions need smoothness and compact support? ::@:: Smoothness makes derivative rules legitimate, and compact support removes boundary terms in integration-by-parts arguments.
- How does a unit-area pulse that becomes narrower and narrower lead to the impulse sampling rule? ::@:: Let $\delta_\varepsilon$ be a narrow pulse with total area $1$. <br/> Inside such a narrow pulse, a smooth function $f(t)$ is almost flat, so $f(t)$ is almost the constant value $f(0)$. <br/> That means $\int \delta_\varepsilon(t)f(t)dt$ is almost $f(0)\int \delta_\varepsilon(t)dt=f(0)$. <br/> As the pulse narrows to an impulse, the approximation becomes exact: $\int \delta(t)f(t)dt=f(0)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual bridge card -->
- How should the graph of $\delta(t-t_0)$ be interpreted? ::@:: It is a symbolic arrow at $t=t_0$ labeled by area $1$, not an ordinary finite-width pulse.
- How should the graph of $A\delta(t-t_0)$ be interpreted? ::@:: It is a symbolic arrow at $t=t_0$ labeled by weight $A$.
- Why does the ideal impulse not fit the ordinary finite-energy framework? ::@:: For the rectangular approximation, $E_\varepsilon=1/\varepsilon\to\infty$, so the energy blows up as the pulse concentrates.

## impulse properties and graphing

The most important operational rule is the sifting property: $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$. In plain language, an impulse inside an integral simply picks out the value of the function at its location. The companion multiplication rule is $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$, which says that once all action has been concentrated at one instant, only the local value of the multiplier at that instant survives.

The impulse also obeys parity and scaling rules. It is even, so $\delta(-t)=\delta(t)$. It rescales according to $\delta(at)=\frac{1}{|a|}\delta(t)$ for $a\neq 0$. The geometric meaning is that horizontal compression or expansion changes the symbolic weight so that the total sampling action remains correct.

These rules explain how transformed impulses should be drawn. The graph of $\delta(t-t_0)$ is the graph of $\delta(t)$ shifted to $t=t_0$. The graph of $\delta(at)$ stays at the origin, but its weight becomes $1/|a|$. Thus scaling changes the area label, not the location.

The generalized-function proofs are short and instructive. The parity law follows by testing against $f$ and substituting $\tau=-t$. The scaling law follows by substituting $u=at$ in the defining integral. The multiplication law says something very simple: if an impulse forces the calculation to happen only at $t_0$, then $f(t)$ may be replaced by the single number $f(t_0)$. Formally, generalized functions are equal when they give the same value against every smooth compactly supported probe $g(t)$. Here $\langle f(t)\delta(t-t_0),g\rangle=\int f(t)\delta(t-t_0)g(t)dt=f(t_0)g(t_0)=\langle f(t_0)\delta(t-t_0),g\rangle$, so $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$.

A concrete worked example is $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt=7$, because the impulse samples the multiplier at $t=3$.

---

Flashcards for this section are as follows:

- What is the sifting property of the impulse? ::@:: It is $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$. <br/> In plain language, the impulse picks out the value of the function at the point where the impulse sits.
- What does a shifted impulse $\delta(t-t_0)$ do? ::@:: It samples the attached function at $t=t_0$ rather than at the origin.
- Why does the impulse multiplication law $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$ hold? ::@:: Plain language first: once the impulse pins everything to the single instant $t_0$, the varying factor $f(t)$ can be replaced by the single number $f(t_0)$. <br/> Formally, test both sides against a smooth probe $g(t)$: $\int f(t)\delta(t-t_0)g(t)dt=f(t_0)g(t_0)=\int f(t_0)\delta(t-t_0)g(t)dt$. <br/> Since both sides act the same way on every probe, the multiplication law follows. <!-- check: ignore-line[two_sided_calc_warning]: conceptual law -->
- What is the parity of the impulse? ::@:: The impulse is even, so $\delta(-t)=\delta(t)$.
- What is the scaling law of the impulse? ::@:: For $a\neq 0$, $\delta(at)=\frac{1}{|a|}\delta(t)$.
- How do you draw $\delta(t-t_0)$? ::@:: Move the symbolic impulse arrow from the origin to $t=t_0$.
- How do you draw $\delta(at)$? ::@:: Keep the symbolic arrow at the origin and change its weight to $1/|a|$.
- Why does substituting $\tau=-t$ prove the parity law? ::@:: It shows $\delta(-t)$ has the same action on every test function as $\delta(t)$.
- Why does substituting $u=at$ prove the scaling law? ::@:: It produces the factor $1/|a|$ in the defining integral, giving $\delta(at)=\frac{1}{|a|}\delta(t)$.
- Worked example (method: sifting): Given $f(t)=2t+1$, what is $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt$? ::@:: Step 1: use the sifting property to sample the multiplier at $t=3$. <br/> Step 2: compute $2(3)+1=7$. <br/> Step 3: therefore the integral equals $7$.

## derivatives of singular signals

Differentiation moves the singular-signal ladder one step upward. The ramp differentiates to the step, $\frac{d}{dt}r(t)=u(t)$, and the step differentiates to the impulse, $\frac{d}{dt}u(t)=\delta(t)$. The geometric meaning is simple: a smooth slanted segment becomes a constant slope, and a jump becomes a concentrated spike at the switching instant.

This rule immediately explains why gates differentiate into impulse pairs. If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, then $\frac{d}{dt}G_\tau(t)=\delta(t+\tau/2)-\delta(t-\tau/2)$. A positive impulse appears at the rising edge, and a negative impulse appears at the falling edge.

The same principle explains switched exponentials. The derivative of $e^{-t}u(t)$ is not just the ordinary derivative $-e^{-t}u(t)$ on $t>0$; it also includes the impulsive contribution created by switching on at the origin: $\frac{d}{dt}(e^{-t}u(t))=-e^{-t}u(t)+\delta(t)$. This is a good model example because it shows how ordinary differentiation and singular contributions coexist in one formula.

More generally, the course treats the derivative of a piecewise-smooth signal in two layers: differentiate each smooth segment in the ordinary way, and then add a Dirac impulse at every jump discontinuity. If the jump at $t=t_0$ is $x(t_0^+)-x(t_0^-)$, then the derivative contains the singular term $\bigl(x(t_0^+)-x(t_0^-)\bigr)\delta(t-t_0)$. On sketches, this jump contribution is drawn as an impulse arrow at the jump location rather than as an ordinary finite spike.

---

Flashcards for this section are as follows:

- What is the derivative of the unit ramp? ::@:: It is the unit step: $\frac{d}{dt}r(t)=u(t)$.
- What is the derivative of the unit step? ::@:: It is the unit impulse: $\frac{d}{dt}u(t)=\delta(t)$.
- What is the geometric meaning of differentiating a step? ::@:: Differentiating a jump concentrates the change at one instant, so the derivative becomes an impulse.
- If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, what is its derivative? ::@:: It is $\delta(t+\tau/2)-\delta(t-\tau/2)$.
- Why does a differentiated gate produce a positive and a negative impulse? ::@:: The rising edge contributes a positive impulse, while the falling edge contributes a negative impulse.
- What is the derivative of $e^{-t}u(t)$? ::@:: It is $-e^{-t}u(t)+\delta(t)$.
- Why do switched signals acquire impulse terms when differentiated? ::@:: Differentiation gives the ordinary derivative on smooth intervals plus an impulse at the switching instant.
- How should this course differentiate a piecewise-smooth signal with jump discontinuities? ::@:: Differentiate each smooth piece normally, then add a Dirac impulse at each jump with weight equal to the jump size $x(t_0^+)-x(t_0^-)$.
- How is the derivative contribution of a jump drawn on a graph? ::@:: It is drawn as an impulse arrow at the jump location, because the singular contribution is a Dirac delta rather than an ordinary finite-height spike.
- Worked example (method: gate-differentiation): Given $G_2(t)=u(t+1)-u(t-1)$, what is its derivative? ::@:: Step 1: differentiate the rising edge $u(t+1)$ to get $\delta(t+1)$. <br/> Step 2: differentiate the falling edge $-u(t-1)$ to get $-\delta(t-1)$. <br/> Step 3: add the two contributions to obtain $\delta(t+1)-\delta(t-1)$.

## doublet and higher impulse derivatives

The derivative of the impulse is the doublet, written $\delta'(t)$. Conceptually, the impulse samples a function value, whereas the doublet samples derivative information. The generalized-function definition is $\int_{-\infty}^{\infty}\delta'(t)f(t)dt=-f'(0)$, and more generally $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$. This follows from integration by parts, with boundary terms vanishing because the test function has compact support.

The minus sign is worth understanding intuitively. Imagine a tiny positive bump just to the left of the support point and a tiny negative bump just to the right. If $f$ is increasing near $t_0$, then the negative bump samples slightly larger values than the positive bump does, so the net result is negative. That is why the doublet samples $-f'(t_0)$ rather than $+f'(t_0)$.

This is also a good place to compare direct sampling with convolution. Convolution with a doublet gives a positive derivative: $f*\delta'=f'$. The difference is that convolution flips one factor first. Since $\delta'(t)$ is odd, that flip reverses its sign. This extra sign flip cancels the minus sign from direct sampling. A reliable memory aid is therefore: __doublet acting directly under an integral gives negative derivative; doublet used as a convolution kernel gives positive derivative because convolution reverses one factor first__.

One can see the sign cancellation algebraically too. In direct sampling, $\int_{-\infty}^{\infty}\delta'(t-\tau)f(t)\,dt=-f'(\tau)$ because the derivative acts on the test function after integration by parts. But in convolution, $(f*\delta')(t)=\int_{-\infty}^{\infty}f(\tau)\delta'(t-\tau)\,d\tau$. Now $\delta'(t-\tau)=-\frac{d}{d\tau}\delta(t-\tau)$, so integrating by parts in $\tau$ gives $(f*\delta')(t)=\int_{-\infty}^{\infty}f'(\tau)\delta(t-\tau)\,d\tau=f'(t)$. The direct-action minus sign is exactly cancelled by the minus sign coming from differentiating the flipped kernel with respect to $\tau$.

The pulse-limit intuition is an antisymmetric pulse pair. A simple family is $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $d_\varepsilon(t)=-1/\varepsilon^2$ on $(0,\varepsilon)$, and $0$ elsewhere. Its total signed area is zero, but for a smooth test function $f$ a first-order Taylor expansion near $0$ shows that $\int d_\varepsilon(t)f(t)dt\to-f'(0)$. Thus the doublet is not "two impulses" in the ordinary sense; it is the limiting derivative-type action represented symbolically by a nearby positive-negative pattern.

Several structural properties follow immediately. Because $\delta(t)$ is even, $\delta'(t)$ is odd. Because the positive and negative parts cancel, its total signed area is zero in the generalized sense. The multiplication law becomes more delicate than for the impulse itself: $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$. Its derivation is short but worth keeping visible. Test against a smooth probe $g(t)$: $\langle f\delta',g\rangle=\langle \delta',fg\rangle=-(fg)'(0)=-f'(0)g(0)-f(0)g'(0)=\langle f(0)\delta'-f'(0)\delta,g\rangle$. So the doublet is sensitive both to the local value and to the local slope of the multiplier.

This also explains why the term $f(0)\delta'(t)$ does not behave like an ordinary weighted area contribution. If the probe is the constant function $1$, then $\langle f(0)\delta',1\rangle=0$ because $\delta'$ annihilates constants. The nonzero correction is carried by the accompanying $-f'(0)\delta(t)$ term, which records how the multiplier changes at the support point.

Higher derivatives continue the same pattern. Their generalized-function rule is $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$. The corresponding multiplication law is obtained by the same probe method together with the Leibniz rule: $f(t)\delta^{(n)}(t)=\sum_{m=0}^{n}(-1)^m\binom{n}{m}f^{(m)}(0)\delta^{(n-m)}(t)$. So higher impulse derivatives react to progressively finer local Taylor data rather than merely to value or first slope.

---

Flashcards for this section are as follows:

- What is the doublet? ::@:: It is the derivative of the impulse and is written $\delta'(t)$.
- What is the generalized-function sampling rule for the doublet, and why does it carry a minus sign? ::@:: The rule is $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$, with origin case $\int\delta'(t)f(t)dt=-f'(0)$. <br/> In plain language, the doublet measures local slope instead of local value. <br/> The sign is negative because the small negative bump on the right samples slightly larger values than the small positive bump on the left when $f$ is increasing.
- Why does integration by parts define the doublet correctly? ::@:: It transfers the derivative onto the test function, and the boundary terms vanish because the test function has compact support.
- Why does convolution with a doublet produce a positive derivative even though direct doublet sampling gives a negative derivative? ::@:: Because convolution flips one factor first, and since $\delta'$ is odd that flip contributes an extra minus sign; this cancels the minus sign in the direct sampling rule, so $f*\delta'=f'$.
- What is the short algebraic reason that $(f*\delta')(t)=f'(t)$ has a positive sign? ::@:: Write $(f*\delta')(t)=\int f(\tau)\delta'(t-\tau)\,d\tau$, use $\delta'(t-\tau)=-\frac{d}{d\tau}\delta(t-\tau)$, then integrate by parts in $\tau$ to get $\int f'(\tau)\delta(t-\tau)\,d\tau=f'(t)$.
- What is the pulse-pair intuition for the doublet? ::@:: It is the limit of a very narrow positive-negative pulse pair whose total area is zero but whose first-moment effect remains finite.
- What is a concrete pulse-pair approximation to the doublet? ::@:: One choice is $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $-1/\varepsilon^2$ on $(0,\varepsilon)$, and $0$ elsewhere. <!-- check: ignore-line[two_sided_calc_warning]: conceptual formula card -->
- Why does the doublet have zero signed area? ::@:: The positive and negative parts of the pulse-pair approximation cancel, so the total signed area is zero in the generalized sense.
- What is the parity of the doublet? ::@:: Since the impulse is even, its derivative $\delta'(t)$ is odd.
- What is the doublet multiplication law, and how does the derivation explain both terms? ::@:: The law is $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$. <br/> Plain language: the doublet reacts to both the value of $f$ at the impulse location and the way $f$ is changing there. <br/> Test against a smooth probe $g(t)$: $\langle f\delta',g\rangle=\langle \delta',fg\rangle=-(fg)'(0)=-f'(0)g(0)-f(0)g'(0)$. <br/> This is exactly the action of $f(0)\delta'(t)-f'(0)\delta(t)$. <br/> So one term keeps the local value and the other corrects for local slope. <!-- check: ignore-line[two_sided_calc_warning]: conceptual law -->
- What do higher impulse derivatives do, and what multiplication law do they satisfy? ::@:: They satisfy $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$, so each higher derivative reads off a higher-order local slope of $f$. <br/> The matching multiplication law is $f(t)\delta^{(n)}(t)=\sum_{m=0}^{n}(-1)^m\binom{n}{m}f^{(m)}(0)\delta^{(n-m)}(t)$, obtained by testing against a probe and expanding $(fg)^{(n)}(0)$ with Leibniz's rule.
- Why are higher impulse derivatives more singular? ::@:: Each higher derivative reacts to finer local Taylor data of the test function rather than only to value or first slope.
- Worked example (method: doublet sampling and differentiation): Given $f(t)=3t^2-1$, what is $\int_{-\infty}^{\infty}(3t^2-1)\delta'(t-2)dt$? ::@:: Step 1: use the doublet sampling rule $\int f(t)\delta'(t-t_0)dt=-f'(t_0)$. <br/> Step 2: differentiate $f(t)$ to get $f'(t)=6t$. <br/> Step 3: evaluate at $t_0=2$ to get $f'(2)=12$. <br/> Step 4: apply the minus sign, giving $-12$.

## convolution with impulse and impulse derivatives

Convolution gives the operational payoff of singular signals. The impulse is the identity element for continuous-time convolution: $f*\delta=f$. A shifted impulse simply shifts the signal, so $f*\delta(t-t_0)=f(t-t_0)$, because the convolution integral samples the integrand at the shifted support point.

Impulse derivatives turn convolution into differentiation. For a sufficiently regular signal, $f*\delta'=f'$, and more generally $f*\delta^{(n)}=f^{(n)}$. This is one reason singular signals are so useful: they convert structural properties of convolution into compact differentiation rules.

The switched exponential again provides a good check. If $f(t)=e^{-t}u(t)$, then $f*\delta'(t)=f'(t)=-e^{-t}u(t)+\delta(t)$, which matches the derivative formula obtained earlier directly from singular-signal calculus.

---

Flashcards for this section are as follows:

- Why is the impulse the identity element for continuous-time convolution? ::@:: Because $f*\delta=f$.
- What does convolution with a shifted impulse do? ::@:: It shifts the signal: $f*\delta(t-t_0)=f(t-t_0)$.
- What does convolution with the doublet do? ::@:: It differentiates the signal: $f*\delta'=f'$.
- What does convolution with the nth impulse derivative do? ::@:: It gives the order-$n$ derivative: $f*\delta^{(n)}=f^{(n)}$.
- Why are impulse derivatives useful in convolution? ::@:: They convert convolution identities into compact differentiation rules, so they encode system calculus efficiently.
- Worked example (method: convolution-with-derivative identity): Given $f(t)=e^{-t}u(t)$, what is $f*\delta'(t)$? ::@:: Step 1: use the rule $f*\delta'=f'$. <br/> Step 2: differentiate $e^{-t}u(t)$ using the product rule for switched signals. <br/> Step 3: the smooth part gives $-e^{-t}u(t)$ and the switching at $t=0$ contributes $\delta(t)$. <br/> Step 4: therefore $f*\delta'(t)=-e^{-t}u(t)+\delta(t)$.
