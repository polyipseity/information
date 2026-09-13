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

Singular signals model switching, sampling, and sudden concentrated change. ELEC 2100 introduces them early because convolution, LTI, and transform methods all depend on step, impulse, and derivative signals.

This file covers continuous-time singular signals. General signal language is in [signal](signal.md); discrete-time sequences are in [discrete-time signal](discrete-time%20signal.md).

---

Flashcards for this section are as follows:

- Why does ELEC 2100 introduce singular signals early? ::@:: Later convolution, LTI, and transform methods depend on step, impulse, and derivative signals.

## singular-signal overview

The main chain is $r(t) \to u(t) \to \delta(t) \to \delta'(t)$, where each differentiation concentrates change more sharply.

Two categories: ordinary (ramp, step, gate, signum) plotted as regular curves, and generalized (impulse, doublet) drawn as symbolic arrows. An impulse encodes area; a doublet encodes derivative action.

"Infinitely tall narrow pulse" is only a heuristic. The generalized object is defined by its action under integration, not by pointwise height.

---

Flashcards for this section are as follows:

- What is the main singular-signal chain in ELEC 2100? ::@:: $r(t) \to u(t) \to \delta(t) \to \delta'(t)$.
- What is the difference between ordinary and generalized singular signals? ::@:: Ordinary (ramp, step, gate, signum) plot as regular piecewise graphs. Generalized (impulse, doublet) use symbolic arrows encoding location, sign, and area or derivative action.
- Why is "infinitely tall narrow pulse" only a heuristic? ::@:: The generalized impulse is defined by $\int \delta(t)f(t)dt=f(0)$, not by literal pointwise height.

## ramp, step, gate, and signum

The unit step is $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$ (value at $t=0$ set by convention). The unit ramp is $r(t)=tu(t)$, so $0$ for $t<0$ and $t$ for $t>0$.

Graphing rule: draw the pre-switch part, then the post-switch part. For $u(t-t_0)$, graph is $0$ for $t<t_0$, jump at $t=t_0$, then $1$ for $t>t_0$. For $r(t-t_0)$, graph is $0$ until $t=t_0$, then slope $1$ from that point.

A step jumps and stays flat. A ramp turns on and keeps growing linearly.

Finite windows use subtracted shifted steps. A gate on $[a,b)$ is $u(t-a)-u(t-b)$. The symmetric gate of width $\tau$ is $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, which is $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$.

The signum is $-1$ for $t<0$, $+1$ for $t>0$, usually $0$ at the origin. Away from the origin, $\operatorname{sgn}(t)=2u(t)-1=u(t)-u(-t)$.

---

Flashcards for this section are as follows:

- What is the unit step? ::@:: $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$ (value at $t=0$ set by convention).
- What is the unit ramp? ::@:: $r(t)=tu(t)$: $0$ for $t<0$, grows linearly for $t>0$.
- How do you draw $u(t-t_0)$? ::@:: Graph is $0$ for $t<t_0$, jump at $t_0$, then $1$ for $t>t_0$.
- How do you draw $r(t-t_0)$? ::@:: Graph is $0$ until $t_0$, then slope $1$ from that point.
- How can a rectangular gate on $[a,b)$ be written using steps? ::@:: $u(t-a)-u(t-b)$.
- What is the symmetric gate of width $\tau$? ::@:: $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$: equals $1$ for $|t|<\tau/2$ and $0$ for $|t|>\tau/2$.
- What is the signum function? ::@:: $-1$ for $t<0$, $+1$ for $t>0$, usually $0$ at the origin.
- How is the signum related to the unit step? ::@:: $\operatorname{sgn}(t)=2u(t)-1=u(t)-u(-t)$ (with care at $t=0$).
- Worked example: Given $g(t)=u(t-1)-u(t-3)$, what is its graph? ::@:: Step 1: step on at $t=1$ jumps to $1$. <br/> Step 2: step on at $t=3$ drops back by $1$. <br/> Step 3: $g(t)=0$ for $t<1$, $1$ for $1<t<3$, $0$ for $t>3$.

## unit impulse: pulse limits and generalized functions

The course presents two viewpoints: the impulse as a limit of ordinary pulses (intuitive) and as a generalized function defined by its action on test functions (precise).

A standard rectangular delta sequence is $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$ and $0$ otherwise. Width $\varepsilon$, height $1/\varepsilon$, area $\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon)dt=1$. As $\varepsilon\to 0$, the pulse narrows and grows while keeping unit area. Other families (triangular, exponential, Gaussian, sinc) all share this normalization: concentration near one point with total area $1$.

The generalized-function viewpoint defines the impulse through integration: $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$ for a smooth compactly supported test function $f(t)$. Test functions are smooth local probes: smoothness makes differentiation rules valid, compact support removes boundary terms in integration by parts.

The two viewpoints connect: if $\delta_\varepsilon$ has unit area and support shrinking to the origin, then $\int\delta_\varepsilon(t)f(t)dt=\int\delta_\varepsilon(t)(f(t)-f(0))dt+f(0)\int\delta_\varepsilon(t)dt$. The second term is $f(0)$ (area $1$). The first term vanishes because $f(t)-f(0)$ is tiny inside the narrow pulse.

Graphically, the impulse is a symbolic arrow showing location and weight, not height. $\delta(t-t_0)$ is an arrow at $t=t_0$ with area $1$; $A\delta(t-t_0)$ has weight $A$. Treating the impulse as a pointwise zero-width rectangle is a category mistake: meaning comes from its action in integrals.

Warning: the ideal impulse has infinite energy. For the rectangular approximation, $E_\varepsilon=\int_{-\varepsilon/2}^{\varepsilon/2}(1/\varepsilon^2)dt=1/\varepsilon\to\infty$.

---

Flashcards for this section are as follows:

- What are the two main viewpoints on the unit impulse? ::@:: It is the limit of unit-area pulse families, and a generalized function defined by $\int \delta(t)f(t)dt=f(0)$.
- What is a standard rectangular delta sequence? ::@:: $\delta_\varepsilon(t)=1/\varepsilon$ for $|t|<\varepsilon/2$, $0$ otherwise. Area $=1$.
- Why does unit area matter for delta sequences? ::@:: It makes the limiting sampling action correctly normalized.
- What is the generalized-function definition of the impulse? ::@:: $\int_{-\infty}^{\infty}\delta(t)f(t)dt=f(0)$ for smooth compactly supported $f$.
- Why do test functions need smoothness and compact support? ::@:: Smoothness makes derivative rules valid; compact support removes boundary terms in integration by parts.
- How does a narrowing unit-area pulse lead to the sampling rule? ::@:: Inside a narrow pulse, $f(t)\approx f(0)$, so $\int \delta_\varepsilon(t)f(t)dt\approx f(0)\int \delta_\varepsilon(t)dt=f(0)$. As $\varepsilon\to 0$ the approximation becomes exact.
- How should impulse graphs be interpreted? ::@:: $\delta(t-t_0)$ is an arrow at $t_0$ with area $1$; $A\delta(t-t_0)$ has weight $A$. Neither is a literal pulse.
- Why does the ideal impulse have infinite energy? ::@:: $E_\varepsilon=1/\varepsilon\to\infty$ for the rectangular approximation.

## impulse properties and graphing

The sifting property: $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$. The multiplication rule: $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$.

The impulse is even: $\delta(-t)=\delta(t)$. Scaling: $\delta(at)=\frac{1}{|a|}\delta(t)$ for $a\neq 0$. To draw transformed impulses: $\delta(t-t_0)$ shifts the arrow to $t=t_0$; $\delta(at)$ keeps the arrow at the origin with weight $1/|a|$.

Proofs. Parity: test $\delta(-t)$ and $\delta(t)$ against any $f$; substituting $\tau=-t$ gives $f(0)$ in both cases. Scaling: substituting $u=at$ produces the $1/|a|$ Jacobian factor. Multiplication: $\langle f(t)\delta(t-t_0),g\rangle=\int f(t)\delta(t-t_0)g(t)dt=f(t_0)g(t_0)=\langle f(t_0)\delta(t-t_0),g\rangle$.

Warning: the multiplication law simplifies only the smooth multiplier; it does __not__ remove the delta. The result is $f(t_0)\delta(t-t_0)$, not $f(t_0)$ alone.

Example: $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt=7$.

---

Flashcards for this section are as follows:

- What is the sifting property? ::@:: $\int_{-\infty}^{\infty}f(t)\delta(t-t_0)dt=f(t_0)$.
- What is the impulse multiplication law and what must you not conclude? ::@:: $f(t)\delta(t-t_0)=f(t_0)\delta(t-t_0)$. It simplifies only the coefficient; the delta stays.
- What is the parity of the impulse? ::@:: Even: $\delta(-t)=\delta(t)$.
- What is the scaling law? ::@:: $\delta(at)=\frac{1}{|a|}\delta(t)$ for $a\neq 0$.
- How do you draw $\delta(t-t_0)$? ::@:: Shift the arrow to $t=t_0$.
- How do you draw $\delta(at)$? ::@:: Keep the arrow at the origin, change weight to $1/|a|$.
- Worked example: Given $f(t)=2t+1$, what is $\int_{-\infty}^{\infty}(2t+1)\delta(t-3)dt$? ::@:: Sample $f$ at $t=3$: $2(3)+1=7$.

## derivatives of singular signals

Differentiation climbs the chain: $\frac{d}{dt}r(t)=u(t)$, $\frac{d}{dt}u(t)=\delta(t)$.

Gates differentiate into impulse pairs. If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, then $\frac{d}{dt}G_\tau(t)=\delta(t+\tau/2)-\delta(t-\tau/2)$: positive impulse at the rising edge, negative at the falling edge.

Switched exponentials work the same way. The derivative of $e^{-t}u(t)$ includes the ordinary derivative $-e^{-t}u(t)$ on $t>0$ plus an impulse from switching on at the origin: $\frac{d}{dt}(e^{-t}u(t))=-e^{-t}u(t)+\delta(t)$.

A common mistake: the product rule gives $\frac{d}{dt}\bigl(e^{-t}u(t)\bigr)=-e^{-t}u(t)+e^{-t}\delta(t)$, and the multiplication law replaces $e^{-t}\delta(t)=\delta(t)$, so the complete derivative is $-e^{-t}u(t)+\delta(t)$. Dropping the delta is wrong because the jump at $t=0$ forces it to remain.

General rule: differentiate each smooth segment normally, then add a Dirac impulse at every jump. A jump of size $x(t_0^+)-x(t_0^-)$ at $t=t_0$ contributes $\bigl(x(t_0^+)-x(t_0^-)\bigr)\delta(t-t_0)$.

---

Flashcards for this section are as follows:

- What is the derivative of the unit ramp? ::@:: $\frac{d}{dt}r(t)=u(t)$.
- What is the derivative of the unit step? ::@:: $\frac{d}{dt}u(t)=\delta(t)$.
- If $G_\tau(t)=u(t+\tau/2)-u(t-\tau/2)$, what is its derivative? ::@:: $\delta(t+\tau/2)-\delta(t-\tau/2)$.
- When differentiating $e^{-t}u(t)$, what is the full derivative? ::@:: $-e^{-t}u(t)+\delta(t)$. The product rule gives $-e^{-t}u(t)+e^{-t}\delta(t)$, and $e^{-t}\delta(t)=\delta(t)$.
- How do you differentiate a piecewise-smooth signal with jumps? ::@:: Differentiate each smooth piece normally, then add an impulse at each jump with weight $x(t_0^+)-x(t_0^-)$.
- Worked example: Given $G_2(t)=u(t+1)-u(t-1)$, what is its derivative? ::@:: $\delta(t+1)-\delta(t-1)$.

## doublet and higher impulse derivatives

The doublet $\delta'(t)$ is the derivative of the impulse. Where the impulse samples a function value, the doublet samples slope. The generalized-function rule is $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$, following from integration by parts with vanishing boundary terms.

The minus sign has an intuitive reason. Think of a tiny positive bump just left of $t_0$ and a tiny negative bump just right. When $f$ is increasing, the negative bump samples slightly larger values, so the net result is negative, giving $-f'(t_0)$.

Direct sampling vs convolution: convolution with a doublet gives a positive derivative ($f*\delta'=f'$). Convolution flips one factor first, and since $\delta'$ is odd, that flip adds a minus sign cancelling the direct-sampling one.

Algebraically: $\int \delta'(t-\tau)f(t)\,dt=-f'(\tau)$ from integration by parts. In convolution, $(f*\delta')(t)=\int f(\tau)\delta'(t-\tau)\,d\tau$, and $\delta'(t-\tau)=-\frac{d}{d\tau}\delta(t-\tau)$, so integration by parts in $\tau$ gives $\int f'(\tau)\delta(t-\tau)\,d\tau=f'(t)$.

Pulse-pair intuition: let $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $-1/\varepsilon^2$ on $(0,\varepsilon)$, $0$ elsewhere. Signed area is zero, but $\int d_\varepsilon(t)f(t)dt\to-f'(0)$. The doublet is not "two impulses": it is the limiting derivative action of a positive-negative pulse pair.

Since $\delta(t)$ is even, $\delta'(t)$ is odd (signed area $0$). The multiplication law: $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$, from $\langle f\delta',g\rangle=-(fg)'(0)=-f'(0)g(0)-f(0)g'(0)=\langle f(0)\delta'-f'(0)\delta,g\rangle$. The doublet depends on both value and slope of $f$ at the support point.

This is a reorganization of singular terms, not a simplification. Unlike convolution ($f*\delta'=f'$ gives an ordinary derivative), multiplication by $\delta'(t)$ keeps the answer in terms of $\delta'$ and $\delta$. The same holds for $\delta^{(n)}$: multiplication never eliminates singular terms.

The $f(0)\delta'(t)$ term does not behave like a weighted area: $\langle f(0)\delta',1\rangle=0$ because $\delta'$ annihilates constants. The nonzero correction is $-f'(0)\delta(t)$, recording how $f$ changes at the support point.

Higher derivatives: $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$. Multiplication law: $f(t)\delta^{(n)}(t)=\sum_{m=0}^{n}(-1)^m\binom{n}{m}f^{(m)}(0)\delta^{(n-m)}(t)$.

---

Flashcards for this section are as follows:

- What is the doublet sampling rule? ::@:: $\int_{-\infty}^{\infty}\delta'(t-t_0)f(t)dt=-f'(t_0)$. Minus sign because negative bump samples larger values when $f$ increases.
- Why does convolution with a doublet give a positive derivative? ::@:: Convolution flips one factor; since $\delta'$ is odd, this cancels the direct-sampling minus sign. So $(f*\delta')(t)=f'(t)$.
- What is the doublet multiplication law? ::@:: $f(t)\delta'(t)=f(0)\delta'(t)-f'(0)\delta(t)$. It reorganizes singular terms but never removes them.
- What is the pulse-pair approximation to the doublet? ::@:: $d_\varepsilon(t)=1/\varepsilon^2$ on $(-\varepsilon,0)$, $-1/\varepsilon^2$ on $(0,\varepsilon)$, $0$ elsewhere. Signed area $0$, but $\int d_\varepsilon(t)f(t)dt\to-f'(0)$.
- What is the parity of the doublet? ::@:: Odd: $\delta'(-t)=-\delta'(t)$.
- What do higher impulse derivatives extract? ::@:: $\int_{-\infty}^{\infty}\delta^{(n)}(t)f(t)dt=(-1)^n f^{(n)}(0)$.
- Worked example: Given $f(t)=3t^2-1$, what is $\int_{-\infty}^{\infty}(3t^2-1)\delta'(t-2)dt$? ::@:: $-f'(2)=-6(2)=-12$.

## convolution with impulse and impulse derivatives

The impulse is the identity for continuous-time convolution: $f*\delta=f$. A shifted impulse shifts: $f*\delta(t-t_0)=f(t-t_0)$. Impulse derivatives differentiate: $f*\delta'=f'$, more generally $f*\delta^{(n)}=f^{(n)}$.

Check with $f(t)=e^{-t}u(t)$: $f*\delta'(t)=f'(t)=-e^{-t}u(t)+\delta(t)$, matching the earlier derivative result.

---

Flashcards for this section are as follows:

- Why is the impulse the identity for continuous-time convolution? ::@:: $\int f(\tau)\delta(t-\tau)d\tau=f(t)$ by sifting.
- What does convolution with $\delta(t-t_0)$ do? ::@:: Shifts: $f*\delta(t-t_0)=f(t-t_0)$.
- What does convolution with $\delta^{(n)}$ do? ::@:: Differentiates $n$ times: $f*\delta^{(n)}=f^{(n)}$.
- Worked example: Given $f(t)=e^{-t}u(t)$, what is $f*\delta'(t)$? ::@:: $f*\delta'=f'=-e^{-t}u(t)+\delta(t)$.
