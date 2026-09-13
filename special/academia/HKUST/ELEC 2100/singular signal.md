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

Singular signals model switching, sampling, and sudden concentrated change. ELEC 2100 introduces them early because later convolution, LTI, and transform methods all depend on step, impulse, and derivative signals.

This file covers continuous-time singular signals. General signal language is in [signal](signal.md), and discrete-time sequences are in [discrete-time signal](discrete-time%20signal.md). Keeping these separate avoids mixing ordinary classification with generalized functions.

---

Flashcards for this section are as follows:

- Why does ELEC 2100 introduce singular signals early? ::@:: Later convolution, LTI, and transform methods depend on step, impulse, and derivative signals.

## singular-signal overview

The course calls these _singular signals_ or _singularity functions_: signals that either contain discontinuities or produce concentrated discontinuities when differentiated or integrated. The main chain is $r(t) \to u(t) \to \delta(t) \to \delta'(t)$, where each differentiation concentrates change more sharply.

Two categories: ordinary and generalized. Ramp, step, gate, and signum are ordinary piecewise functions plotted as regular curves. The impulse and doublet are generalized functions with symbolic graphs. An impulse encodes area; a doublet encodes derivative action.

The phrase "infinitely tall narrow pulse" is only a heuristic. It gives intuition for approximating families, but the generalized object is defined by its action under integration. Ordinary singular signals plot as regular piecewise graphs; generalized ones use symbolic arrows showing location, sign, and strength instead of literal height.

---

Flashcards for this section are as follows:

- What is the main singular-signal chain in ELEC 2100? ::@:: $r(t) \to u(t) \to \delta(t) \to \delta'(t)$.
- What is the difference between ordinary and generalized singular signals? ::@:: Ordinary signals (ramp, step, gate, signum) are plotted as regular piecewise graphs. Generalized signals (impulse, doublet) use symbolic arrows encoding location, sign, and area or derivative action.
- Why is "infinitely tall narrow pulse" only a heuristic? ::@:: The generalized impulse is defined by $\int \delta(t)f(t)dt=f(0)$, not by literal pointwise height.

## ramp, step, gate, and signum

The unit step is $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$, with the value at $t=0$ left undefined or set by convention. The unit ramp is $r(t)=tu(t)$, so $r(t)=0$ for $t<0$ and $r(t)=t$ for $t>0$.

The graphing rule: draw the pre-switch part, then the post-switch part. For $u(t-t_0)$, keep the graph at $0$ for $t<t_0$, place the jump at $t=t_0$, and draw the level $1$ for $t>t_0$. For $r(t-t_0)$, keep the graph at $0$ up to $t=t_0$, then begin a line of slope $1$ measured from that switching time.

A step jumps and then stays flat. A ramp turns on at one instant and keeps growing linearly. The ramp accumulates growth over an interval after switching, while the step only records that a switch happened.

Finite windows are built by subtracting shifted steps. A gate or rectangular signal active on $[a,b)$ can be written as $u(t-a)-u(t-b)$. The symmetric gate of width $\tau$ is $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, which equals $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$. To sketch a gate, locate the left and right switching instants first, then fill the graph with level $1$ between them and level $0$ outside.

The signum function is $-1$ for negative time, $+1$ for positive time, and usually $0$ at the origin. Away from the origin, $\operatorname{sgn}(t)=2u(t)-1$ or equivalently $\operatorname{sgn}(t)=u(t)-u(-t)$ (with care at $t=0$). It shows that not all singular signals are nonnegative or pulse-shaped.

---

Flashcards for this section are as follows:

- What is the unit step? ::@:: $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$ (value at $t=0$ set by convention).
- What is the unit ramp? ::@:: $r(t)=tu(t)$: $0$ for $t<0$, grows linearly for $t>0$.
- How do you draw $u(t-t_0)$? ::@:: Keep the graph at $0$ for $t<t_0$, place the jump at $t=t_0$, and draw the level $1$ for $t>t_0$.
- How do you draw $r(t-t_0)$? ::@:: Keep the graph at $0$ until $t=t_0$, then start a line of slope $1$ measured from that switching time.
- What is the difference between a step and a ramp? ::@:: A step jumps and then stays flat, whereas a ramp turns on at one instant and then continues to grow linearly.
- How can a rectangular gate on $[a,b)$ be written using steps? ::@:: It can be written as $u(t-a)-u(t-b)$.
- What is the symmetric gate of width $\tau$? ::@:: It is $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$.
- How do you draw the symmetric gate? ::@:: It equals $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$, so its graph is a centered rectangular window.
- What is the signum function? ::@:: It is $-1$ for negative time, $+1$ for positive time, and usually $0$ at the origin by convention.
- How is the signum function related to the unit step? ::@:: Away from the origin, $\operatorname{sgn}(t)=2u(t)-1$.
- What is $\operatorname{sgn}(t)$ in terms of step functions? ::@:: $\operatorname{sgn}(t)=u(t)-u(-t)$, with care at $t=0$.
- Worked example (method: gate-decomposition graphing): Given $g(t)=u(t-1)-u(t-3)$, what is its graph? ::@:: Step 1: the first step turns on at $t=1$, so the signal jumps from $0$ to $1$ there. <br/> Step 2: the second step turns on at $t=3$ with a minus sign, so the signal drops back by $1$ there. <br/> Step 3: therefore $g(t)=0$ for $t<1$, $1$ for $1<t<3$, and $0$ for $t>3$, i.e. a rectangular pulse between $1$ and $3$.
- Why does a gate differentiate to an impulse pair while a step differentiates to one impulse? ::@:: A step has one switching edge, whereas a gate has two switching edges.

## unit impulse: pulse limits and generalized functions

The course presents two viewpoints: the impulse as a limit of ordinary pulses (intuitive) and as a generalized function defined by its action on test functions (precise).

A standard rectangular delta sequence is $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$ and $0$ otherwise. Its width is $\varepsilon$, its height is $1/\varepsilon$, and its area is $\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon)dt=1$. As $\varepsilon\to 0$, the pulse becomes narrower and taller while keeping unit area. This is the core normalization idea behind all delta sequences: the detailed shape may vary, but the total area must stay equal to $1$.

Other unit-area families confirm the same idea. A triangular approximation is $\delta_\varepsilon(t)=\frac{1}{\varepsilon}(1-|t|/\varepsilon)$ for $|t|<\varepsilon$ and $0$ otherwise, with area $2\int_0^{\varepsilon}\frac{1}{\varepsilon}(1-t/\varepsilon)dt=1$. A double-sided exponential is $\delta_\varepsilon(t)=\frac{1}{2\varepsilon}e^{-|t|/\varepsilon}$, with area $2\int_0^{\infty}\frac{1}{2\varepsilon}e^{-t/\varepsilon}dt=1$. A Gaussian is $\delta_\varepsilon(t)=\frac{1}{\sqrt{\pi}\varepsilon}e^{-(t/\varepsilon)^2}$, with area $\frac{1}{\sqrt{\pi}}\int_{-\infty}^{\infty}e^{-u^2}du=1$ after substituting $u=t/\varepsilon$. A sinc-shaped family $\delta_\varepsilon(t)=\frac{1}{\pi}\frac{\sin(t/\varepsilon)}{t}=\frac{1}{\pi\varepsilon}\operatorname{Sa}(t/\varepsilon)$ also has unit area. The common feature: concentration near one point with total area $1$.

The generalized-function viewpoint defines the impulse through integration: for a smooth compactly supported test function $f(t)$, the rule is $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$. A test function is a smooth local probe: smoothness makes differentiation rules legitimate, and compact support removes boundary terms in integration by parts.

The two viewpoints connect. If $\delta_\varepsilon$ has unit area and support shrinking to the origin, then $\int\delta_\varepsilon(t)f(t)dt=\int\delta_\varepsilon(t)(f(t)-f(0))dt+f(0)\int\delta_\varepsilon(t)dt$. The second term is $f(0)$ (area is $1$). The first term vanishes because the pulse is so narrow that $f(t)-f(0)$ is tiny inside it. So unit area keeps the $f(0)$ term alive, and concentration kills the remainder.

Graphically, the impulse is a symbolic arrow showing location and weight, not literal height. The graph of $\delta(t-t_0)$ is an arrow at $t=t_0$ labeled with area $1$. The graph of $A\delta(t-t_0)$ is the same arrow labeled with weight $A$. Treating the impulse as a pointwise zero-width rectangle is a category mistake: meaning comes always from its action in integrals.

Warning: the ideal impulse has infinite energy. For the rectangular approximation, $E_\varepsilon=\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon^2)dt=1/\varepsilon\to\infty$, so energy blows up as the pulse concentrates.

---

Flashcards for this section are as follows:

- What are the two main viewpoints on the unit impulse? ::@:: It is understood both as the limit of unit-area pulse families and as a generalized function defined by its action on test functions.
- What is a standard rectangular delta sequence? ::@:: It is $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$ and $0$ otherwise.
- Why does the rectangular delta sequence have unit area? ::@:: Because $\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon)dt=1$.
- Why does unit area matter for delta sequences? ::@:: It makes the limiting sampling action correctly normalized.
- What is a triangular delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\varepsilon}(1-|t|/\varepsilon)$ for $|t|<\varepsilon$ and $0$ otherwise.
- What is a double-sided exponential delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{2\varepsilon}e^{-|t|/\varepsilon}$.
- What is a Gaussian delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\sqrt{\pi}\varepsilon}e^{-(t/\varepsilon)^2}$.
- What is a sinc-shaped delta sequence? ::@:: One choice is $\delta_\varepsilon(t)=\frac{1}{\pi}\frac{\sin(t/\varepsilon)}{t}=\frac{1}{\pi\varepsilon}\operatorname{Sa}(t/\varepsilon)$.
- What is the generalized-function definition of the impulse? ::@:: For a suitable test function $f(t)$, it is defined by $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$.
- What are test functions conceptually? ::@:: They are smooth localized probe functions used to check how a generalized signal behaves inside an integral.
- Why do test functions need smoothness and compact support? ::@:: Smoothness makes derivative rules legitimate, and compact support removes boundary terms in integration-by-parts arguments.
- How does a unit-area pulse that becomes narrower and narrower lead to the impulse sampling rule? ::@:: Let $\delta_\varepsilon$ be a narrow pulse with total area $1$. <br/> Inside such a narrow pulse, a smooth function $f(t)$ is almost flat, so $f(t)$ is almost the constant value $f(0)$. <br/> That means $\int \delta_\varepsilon(t)f(t)dt$ is almost $f(0)\int \delta_\varepsilon(t)dt=f(0)$. <br/> As the pulse narrows to an impulse, the approximation becomes exact: $\int \delta(t)f(t)dt=f(0)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual bridge card -->
- How should impulse graphs be interpreted? ::@:: $\delta(t-t_0)$ is an arrow at $t=t_0$ with area $1$; $A\delta(t-t_0)$ has weight $A$. Neither is a literal finite-width pulse.
- Why does the ideal impulse have infinite energy? ::@:: For the rectangular approximation, $E_\varepsilon=1/\varepsilon\to\infty$ as the pulse concentrates.

## impulse properties and graphing

The sifting property says $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$: the impulse picks out the function value at its location. The multiplication rule $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$ says the same thing in product form: only the local value at $t_0$ survives.

The impulse is even: $\delta(-t)=\delta(t)$. It scales as $\delta(at)=\frac{1}{|a|}\delta(t)$ for $a\neq 0$: compression or expansion changes the weight to keep total sampling action correct.

To draw transformed impulses: $\delta(t-t_0)$ is $\delta(t)$ shifted to $t=t_0$, while $\delta(at)$ stays at the origin with weight $1/|a|$. Scaling changes the area label, not the location.

The proofs are quick. Parity: testing $\delta(-t)$ and $\delta(t)$ against any $f$ and substituting $\tau=-t$ gives $f(0)$ in both cases. Scaling: substituting $u=at$ produces the $1/|a|$ factor. Multiplication: two generalized functions are equal when they agree against every smooth compactly supported probe $g(t)$. Here $\langle f(t)\delta(t-t_0),g\rangle=\int f(t)\delta(t-t_0)g(t)dt=f(t_0)g(t_0)=\langle f(t_0)\delta(t-t_0),g\rangle$, so $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$.

Warning: the multiplication law simplifies only the _smooth multiplier_; it does __not__ remove the delta. The result is $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$, not $f(t_0)$ alone. This matters even more for $\delta'(t)$ and higher derivatives: multiplication reorganizes singular terms but never eliminates them.

Example: $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt=7$, since the impulse samples the multiplier at $t=3$.

---

Flashcards for this section are as follows:

- What is the sifting property of the impulse? ::@:: $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$. The impulse picks out the function value at its location.
- Why does the impulse multiplication law $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$ hold, and what must you not conclude from it? ::@:: Once the impulse pins the calculation to $t_0$, replace $f(t)$ with $f(t_0)$. Formally, $\int f(t)\delta(t-t_0)g(t)dt=f(t_0)g(t_0)=\int f(t_0)\delta(t-t_0)g(t)dt$ for every smooth probe $g$. <br/> The law simplifies only the coefficient; it does __not__ remove the delta. The result is $f(t_0)\delta(t-t_0)$, not the number $f(t_0)$.
- What is the parity of the impulse? ::@:: The impulse is even, so $\delta(-t)=\delta(t)$.
- What is the scaling law of the impulse? ::@:: For $a\neq 0$, $\delta(at)=\frac{1}{|a|}\delta(t)$.
- How do you draw $\delta(t-t_0)$? ::@:: Move the symbolic impulse arrow from the origin to $t=t_0$.
- How do you draw $\delta(at)$? ::@:: Keep the symbolic arrow at the origin and change its weight to $1/|a|$.
- Why does substituting $\tau=-t$ prove the parity law? ::@:: Compare how both $\delta(-t)$ and $\delta(t)$ act on $f$: starting from $\int \delta(-\tau)f(\tau)d\tau$, substitute $\tau=-t$ to get $\int \delta(t)f(-t)dt=f(0)$, matching $\int \delta(\tau)f(\tau)d\tau=f(0)$.
- Why does substituting $u=at$ prove the scaling law? ::@:: It introduces the $1/|a|$ Jacobian factor in the defining integral, giving $\delta(at)=\frac{1}{|a|}\delta(t)$.
- Worked example (method: sifting): Given $f(t)=2t+1$, what is $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt$? ::@:: Step 1: use the sifting property to sample the multiplier at $t=3$. <br/> Step 2: compute $2(3)+1=7$. <br/> Step 3: therefore the integral equals $7$.

## derivatives of singular signals

Differentiation climbs the singular-signal chain: the ramp gives the step ($\frac{d}{dt}r(t)=u(t)$), and the step gives the impulse ($\frac{d}{dt}u(t)=\delta(t)$). A smooth slanted segment becomes a flat slope, and a jump becomes an impulse at the switching instant.

This rule explains why gates differentiate into impulse pairs. If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, then $\frac{d}{dt}G_\tau(t)=\delta(t+\tau/2)-\delta(t-\tau/2)$. A positive impulse appears at the rising edge, and a negative impulse appears at the falling edge.

Switched exponentials work the same way. The derivative of $e^{-t}u(t)$ includes both the ordinary derivative $-e^{-t}u(t)$ on $t>0$ and an impulse from switching on at the origin: $\frac{d}{dt}(e^{-t}u(t))=-e^{-t}u(t)+\delta(t)$.

Working it out fully exposes a common mistake. The product rule gives $\frac{d}{dt}\bigl(e^{-t}u(t)\bigr)=\frac{d}{dt}(e^{-t})\,u(t)+e^{-t}\frac{d}{dt}u(t)=-e^{-t}u(t)+e^{-t}\delta(t)$. The multiplication law replaces $e^{-t}$ by $e^{0}=1$ inside the impulse term: $e^{-t}\delta(t)=\delta(t)$. So the complete derivative is $-e^{-t}u(t)+\delta(t)$. The mistake is writing only $-e^{-t}u(t)$ and dropping the delta, since the jump at $t=0$ forces the impulse to remain.

More generally, differentiate each smooth segment normally, then add a Dirac impulse at every jump. A jump of size $x(t_0^+)-x(t_0^-)$ at $t=t_0$ contributes $\bigl(x(t_0^+)-x(t_0^-)\bigr)\delta(t-t_0)$, drawn as an impulse arrow on sketches.

---

Flashcards for this section are as follows:

- What is the derivative of the unit ramp? ::@:: It is the unit step: $\frac{d}{dt}r(t)=u(t)$.
- What is the derivative of the unit step? ::@:: It is the unit impulse: $\frac{d}{dt}u(t)=\delta(t)$.
- What is the geometric meaning of differentiating a step? ::@:: A jump becomes an impulse at the switching instant.
- If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, what is its derivative? ::@:: It is $\delta(t+\tau/2)-\delta(t-\tau/2)$.
- Why does a differentiated gate produce a positive and a negative impulse? ::@:: The rising edge contributes a positive impulse, while the falling edge contributes a negative impulse.
- When differentiating the switched exponential $e^{-t}u(t)$, what is the full derivative and what common mistake should you avoid? ::@:: Product rule: $\frac{d}{dt}(e^{-t}u(t))=-e^{-t}u(t)+e^{-t}\delta(t)$. Multiply law: $e^{-t}\delta(t)=\delta(t)$. <br/> Complete derivative: $-e^{-t}u(t)+\delta(t)$. <br/> Common mistake: keeping only $-e^{-t}u(t)$ and dropping the delta.
- How should you differentiate a piecewise-smooth signal with jumps? ::@:: Differentiate each smooth piece normally, then add a Dirac impulse at each jump with weight equal to the jump size $x(t_0^+)-x(t_0^-)$.
- How is a jump's derivative contribution drawn? ::@:: As an impulse arrow at the jump location, since singular contributions are Dirac deltas, not finite spikes.
- Worked example (method: gate-differentiation): Given $G_2(t)=u(t+1)-u(t-1)$, what is its derivative? ::@:: Rising edge: $\delta(t+1)$. Falling edge: $-\delta(t-1)$. Result: $\delta(t+1)-\delta(t-1)$.

## doublet and higher impulse derivatives

The doublet $\delta'(t)$ is the derivative of the impulse. Where the impulse samples a function value, the doublet samples slope. The generalized-function rule is $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$, following from integration by parts with vanishing boundary terms.

The minus sign has an intuitive reason. Think of a tiny positive bump just left of $t_0$ and a tiny negative bump just right. When $f$ is increasing, the negative bump samples slightly larger values, so the net result is negative, giving $-f'(t_0)$.

Direct sampling and convolution give opposite signs. Convolution with a doublet gives a positive derivative: $f*\delta'=f'$. Convolution flips one factor first, and since $\delta'(t)$ is odd, that flip adds a minus sign cancelling the one from direct sampling. Memory aid: __doublet under an integral → negative derivative; doublet in convolution → positive derivative (convolution flips one factor)__.

Algebraically: in direct sampling, $\int \delta'(t-\tau)f(t)\,dt=-f'(\tau)$ from integration by parts. In convolution, $(f*\delta')(t)=\int f(\tau)\delta'(t-\tau)\,d\tau$, and $\delta'(t-\tau)=-\frac{d}{d\tau}\delta(t-\tau)$, so integration by parts in $\tau$ gives $\int f'(\tau)\delta(t-\tau)\,d\tau=f'(t)$.

A pulse-pair intuition: let $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $-1/\varepsilon^2$ on $(0,\varepsilon)$, and $0$ elsewhere. Signed area is zero, but a first-order Taylor expansion shows $\int d_\varepsilon(t)f(t)dt\to-f'(0)$. The doublet is not "two impulses": it is the limiting derivative action of a positive-negative pulse pair.

Since $\delta(t)$ is even, $\delta'(t)$ is odd. Its total signed area is zero (the positive and negative parts cancel). The multiplication law is $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$: test against a smooth probe $g(t)$ to get $\langle f\delta',g\rangle=-(fg)'(0)=-f'(0)g(0)-f(0)g'(0)=\langle f(0)\delta'-f'(0)\delta,g\rangle$. So the doublet depends on both the value and slope of $f$ at the support point.

Read this as a _reorganization_ of singular terms, not a simplification. Unlike convolution ($f*\delta'=f'$ gives an ordinary derivative), multiplication by $\delta'(t)$ keeps the answer in terms of $\delta'(t)$ and $\delta(t)$ themselves. The same holds for $\delta^{(n)}$: multiplication identifies which singular terms survive with what coefficients, but never eliminates them.

The $f(0)\delta'(t)$ term does not behave like a weighted area: $\langle f(0)\delta',1\rangle=0$ because $\delta'$ annihilates constants. The nonzero correction comes from $-f'(0)\delta(t)$, which records how the multiplier changes at the support point.

Higher derivatives follow the same pattern: $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$. The multiplication law, from the probe method and Leibniz rule, is $f(t)\delta^{(n)}(t)=\sum_{m=0}^{n}(-1)^m\binom{n}{m}f^{(m)}(0)\delta^{(n-m)}(t)$. Each higher derivative extracts finer local Taylor data.

---

Flashcards for this section are as follows:

- What is the doublet sampling rule, and why the minus sign? ::@:: $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$. The doublet measures slope, not value. The sign is negative because the right-side bump samples larger values than the left-side bump when $f$ is increasing.
- Why does integration by parts define the doublet? ::@:: It transfers the derivative onto the test function, and boundary terms vanish because the test function has compact support.
- Why does convolution with a doublet give a positive derivative while direct sampling gives a negative one? ::@:: Convolution flips one factor first; since $\delta'$ is odd, this adds a minus sign cancelling the direct-sampling one. Algebraically: $(f*\delta')(t)=\int f(\tau)\delta'(t-\tau)\,d\tau$, use $\delta'(t-\tau)=-\frac{d}{d\tau}\delta(t-\tau)$, integrate by parts in $\tau$ to get $\int f'(\tau)\delta(t-\tau)\,d\tau=f'(t)$.
- What is the pulse-pair approximation to the doublet? ::@:: $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $-1/\varepsilon^2$ on $(0,\varepsilon)$, $0$ elsewhere. Signed area is zero, but $\int d_\varepsilon(t)f(t)dt\to-f'(0)$, so it approximates derivative action, not an ordinary impulse.
- What is the parity of the doublet? ::@:: Odd: $\delta'(-t)=-\delta'(t)$, since $\delta(t)$ is even.
- What is the doublet multiplication law? ::@:: $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$. Testing against a probe $g$ gives $\langle f\delta',g\rangle=-(fg)'(0)=-f'(0)g(0)-f(0)g'(0)$. The answer stays in terms of $\delta'$ and $\delta$: multiplication reorganizes singular terms but never removes them.
- What do higher impulse derivatives extract, and why do their multiplication laws preserve singular structure? ::@:: $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$, so $\delta^{(n)}$ extracts higher-order Taylor data. The multiplication law $f(t)\delta^{(n)}(t)=\sum_{m=0}^{n}(-1)^m\binom{n}{m}f^{(m)}(0)\delta^{(n-m)}(t)$ reorganizes singular terms; it never eliminates them.
- Worked example (method: doublet sampling): Given $f(t)=3t^2-1$, what is $\int_{-\infty}^{\infty}(3t^2-1)\delta'(t-2)dt$? ::@:: Step 1: use $\int f(t)\delta'(t-t_0)dt=-f'(t_0)$. <br/> Step 2: $f'(t)=6t$. <br/> Step 3: $f'(2)=12$. <br/> Step 4: the answer is $-12$.

## convolution with impulse and impulse derivatives

Convolution is where singular signals become most useful. The impulse is the identity for continuous-time convolution: $f*\delta=f$. A shifted impulse shifts the signal: $f*\delta(t-t_0)=f(t-t_0)$, since convolution samples at the shifted support point.

Impulse derivatives turn convolution into differentiation: $f*\delta'=f'$, and more generally $f*\delta^{(n)}=f^{(n)}$.

Check with the switched exponential: $f(t)=e^{-t}u(t)$, so $f*\delta'(t)=f'(t)$. The product rule gives $\frac{d}{dt}(e^{-t}u(t))=(-e^{-t})u(t)+e^{-t}\delta(t)$, and $e^{-t}\delta(t)=\delta(t)$, so $f*\delta'(t)=-e^{-t}u(t)+\delta(t)$, matching the earlier result.

---

Flashcards for this section are as follows:

- Why is the impulse the identity for continuous-time convolution? ::@:: Because $\int f(\tau)\delta(t-\tau)d\tau=f(t)$ by the sifting property.
- What does convolution with a shifted impulse do? ::@:: It shifts the signal: $f*\delta(t-t_0)=f(t-t_0)$.
- What does convolution with the doublet do? ::@:: It differentiates: $f*\delta'=f'$.
- What does convolution with the $n$th impulse derivative do? ::@:: It gives the $n$th derivative: $f*\delta^{(n)}=f^{(n)}$.
- Why are impulse derivatives useful in convolution? ::@:: Each $\delta^{(n)}$ acts as a differentiator kernel, converting convolution into the $n$th derivative.
- Worked example (method: convolution-with-derivative identity): Given $f(t)=e^{-t}u(t)$, what is $f*\delta'(t)$? ::@:: Step 1: $f*\delta'=f'$. <br/> Step 2: product rule gives $-e^{-t}u(t)+e^{-t}\delta(t)$. <br/> Step 3: $e^{-t}\delta(t)=\delta(t)$. <br/> Step 4: $f*\delta'(t)=-e^{-t}u(t)+\delta(t)$. The delta is not removed by the multiplication law.
