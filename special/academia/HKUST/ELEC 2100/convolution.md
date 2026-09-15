---
aliases:
  - ELEC 2100 convolution
  - ELEC2100 convolution
  - HKUST ELEC 2100 convolution
  - continuous-time convolution
  - convolution
  - convolution integral
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/convolution
  - language/in/English
---

# convolution

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Convolution is the time-domain formula for zero-state response of linear time-invariant systems. In ELEC 2100 it comes from decomposing a signal into shifted impulses, transferring each through the system, and summing the shifted impulse responses.

Many later identities are convolution algebra: commutativity explains why factors can be swapped, associativity explains why LTI blocks can be regrouped in cascade, and those two properties make parallel and series simplifications work. The Dirac delta and its shifted versions model identity and time shift, its derivative models differentiation, and the unit step models integration. Most of the note reduces to reordering convolution factors or choosing a kernel with a special operator meaning.

The same idea extends to two dimensions (e.g., images). A 2D convolution kernel is a small weighting pattern that slides over pixels. Each output pixel is the weighted local sum: flip the kernel, shift it to the output location, multiply pointwise over the overlap, and sum.

---

Flashcards for this section are as follows:

- What role does convolution play in computing the zero-state response of an LTI system? ::@:: It is the time-domain formula for zero-state response of LTI systems.
- How is convolution derived from decomposing a signal into shifted impulses? ::@:: By decomposing the input into shifted impulses, transferring each through the system, and summing the shifted impulse responses.
- What does a 2D convolution kernel do when it slides across an image patch? ::@:: It weights nearby values and forms each output as a weighted local sum.
- What are the mechanical steps of 2D convolution? ::@:: Flip the kernel, shift it to the output location, multiply pointwise over the overlap, and sum.
- How does 2D convolution generalize the 1D slide-weight-sum procedure from time signals to images? ::@:: It is the same convolution logic generalized from one time axis to two spatial coordinates: slide the kernel, weight nearby values, and sum the local contributions.

## impulse-decomposition viewpoint

A signal can be written as a weighted sum of shifted impulses. In continuous time: $e(t)=\int_{-\infty}^{\infty} e(\tau)\,\delta(t-\tau)\,d\tau$. Each source time $\tau$ contributes weight $e(\tau)$, and the full signal is the integral of all those weighted contributions. The narrow-pulse approximation from the lecture is the intuition; the detailed motivation appears in `continuous-time LTI system.md` and `discrete-time LTI system.md`.

This viewpoint explains why convolution is natural for LTI systems. Once a signal is decomposed into shifted impulses, time invariance tells us what each shifted impulse becomes at the output, and linearity lets us sum all those partial outputs. This is also why the later special-kernel identities work: the algebra is already encoded in the decomposition step.

---

Flashcards for this section are as follows:

- What identity writes a signal as an integral of weighted shifted impulses? ::@:: $e(t)=\int_{-\infty}^{\infty} e(\tau)\,\delta(t-\tau)\,d\tau$.
- What does $e(\tau)$ represent as the weight of the source-time impulse in the decomposition integral? ::@:: It is the weight assigned to the impulse located at source time $\tau$.
- What does $\delta(t-\tau)$ represent in the impulse decomposition integral? ::@:: It represents a unit impulse placed at source time $\tau$ and observed at time $t$.
- Why does decomposing an input into shifted impulses make LTI zero-state analysis straightforward? ::@:: Time invariance tells us how each shifted impulse is transferred, and linearity lets us sum all the partial outputs.

## zero-state response via convolution

Suppose the system is linear, time invariant, and initially at rest. If the input contains a unit impulse at time $\tau$, then by time invariance the response at observation time $t$ is the shifted impulse response $h(t-\tau)$. If the impulse is weighted by $e(\tau)\,d\tau$, linearity says the output contribution is $e(\tau)h(t-\tau)\,d\tau$.

The derivation can be written directly in operator form. Start from the impulse decomposition $e(t)=\int_{-\infty}^{\infty}e(\tau)\delta(t-\tau)\,d\tau$. For a zero-state LTI operator $H$, linearity and time invariance give $H[e](t)=H\!\left[\int_{-\infty}^{\infty}e(\tau)\delta(t-\tau)\,d\tau\right]=\int_{-\infty}^{\infty}e(\tau)H[\delta(t-\tau)]\,d\tau=\int_{-\infty}^{\infty}e(\tau)h(t-\tau)\,d\tau$.

So convolution is not an extra postulate. It is the formula forced by three earlier ideas: impulse decomposition, linearity, and time invariance.

Adding the contributions from all source times yields the zero-state response $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty} e(\tau)h(t-\tau)\,d\tau$. This integral is the __continuous-time convolution integral__ and is written compactly as $r_{\mathrm{zs}}(t)=(e*h)(t)$. The formula should be read operationally. The input contributes its amplitude value $e(\tau)$ from each source time $\tau$, while the system contributes the delayed impulse response $h(t-\tau)$ measured at the observation time $t$. Convolution combines those two viewpoints into one accumulated output.

This is why the note treats convolution as the formula for zero-state response rather than as a separate algebraic trick. It is simply "decompose into impulses, transfer each impulse, add everything."

---

Flashcards for this section are as follows:

- How does time invariance turn a unit impulse at time $\tau$ into an output signal? ::@:: It turns the impulse at time $\tau$ into the shifted impulse response $h(t-\tau)$.
- If the impulse at time $\tau$ has weight $e(\tau)\,d\tau$, what output contribution does linearity predict? ::@:: The contribution is $e(\tau)h(t-\tau)\,d\tau$.
- What is the continuous-time convolution integral for zero-state response? ::@:: $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty} e(\tau)h(t-\tau)\,d\tau=(e*h)(t)$.
- How is the convolution integral derived from the operator viewpoint? ::@:: Write $e(t)=\int e(\tau)\delta(t-\tau)\,d\tau$, apply $H$, and use linearity plus time invariance to get $H[e](t)=\int e(\tau)h(t-\tau)\,d\tau$.
- Why is convolution the natural tool for zero-state response of an LTI system? ::@:: Because it is the formal sum of all shifted-impulse responses produced by decomposing the input into weighted impulses.
- What do the two factors in the integrand $e(\tau)h(t-\tau)$ mean? ::@:: $e(\tau)$ gives the input weight from source time $\tau$, while $h(t-\tau)$ gives how the system carries that impulse to observation time $t$.

## physical interpretation of convolution

Each symbol in the convolution integral has a direct role. $\tau$ is the source time (when a piece of input occurs). $e(\tau)$ is the input strength at that time. $t$ is the observation time. $h(t-\tau)$ is the response visible at time $t$ from a unit impulse applied at source time $\tau$.

Convolution mixes source time $\tau$ and observation time $t$. For each source time $\tau$, the system tells us how much of that earlier event still contributes when we observe the output at time $t$. The integral sums those contributions over all source times.

One intuition: imagine each input slice launching a copy of the impulse response. Early slices launch earlier copies, later slices launch later copies, and the output at time $t$ is the total overlap of all those shifted copies at that instant. Convolution is thus an accumulation of delayed system memories weighted by the input.

A queueing analogy makes the roles concrete. Source time $\tau$ is when one arrival occurs, observation time $t$ is when we ask how much accumulated response is visible, $x(\tau)$ is the arrival strength, and $h(t-\tau)$ is how much of that arrival's contribution is still visible at time $t$. Delayed copies of one response pattern are launched at different source times and then accumulated.

The same analogy separates three meanings that often get blurred in the algebra. A weighted impulse train models arrivals at isolated instants. A rectangular impulse response models a fixed service window. A shifted impulse response models a pure delay. Once those meanings are clear, formulas such as $x(t)*\delta(t-t_0)=x(t-t_0)$ are just operator rules for shifting when a contribution becomes visible.

---

Flashcards for this section are as follows:

- In the convolution integral, what does $\tau$ represent? ::@:: The source time at which a piece of input occurs.
- In the convolution integral, what does $t$ represent? ::@:: The observation time at which the output is evaluated.
- In the convolution integral, what does $h(t-\tau)$ represent physically? ::@:: The response visible at observation time $t$ due to a unit impulse applied at source time $\tau$.
- Why does convolution mix source time $\tau$ and observation time $t$? ::@:: Because it tracks how each earlier input event contributes later when the output is observed at time $t$.
- Why is convolution more than just multiplication inside an integral? ::@:: Because it represents accumulation of delayed system memories, not merely local pointwise interaction.
- What is the overlapping impulse-response copies intuition for convolution? ::@:: Each input slice launches a shifted copy of the impulse response, and the output at time $t$ is the total overlap of all those weighted copies at that instant.

## algebraic properties and system interconnections

Convolution also behaves like an algebra on signals, and those algebraic rules explain why block-diagram interconnections simplify.

The __commutative property__ says $f_1*f_2=f_2*f_1$. The two signals play symmetric roles inside the convolution integral. Many later shortcut identities in ELEC 2100 are this symmetry in action.

The proof is a one-line change of variables: $(f_1*f_2)(t)=\int_{-\infty}^{\infty}f_1(\tau)f_2(t-\tau)\,d\tau=\int_{-\infty}^{\infty}f_1(t-\lambda)f_2(\lambda)\,d\lambda=(f_2*f_1)(t)$, where $\lambda=t-\tau$.

The __distributive property__ says $f*(h_1+h_2)=f*h_1+f*h_2$. This is the rule for parallel LTI systems: feeding the same input into both subsystems and adding their outputs gives overall impulse response $h=h_1+h_2$.

The __associative property__ says $(f*h_1)*h_2=f*(h_1*h_2)$. This is the rule behind cascade connection: the input passes through subsystems with impulse responses $h_1$ and $h_2$, giving overall impulse response $h=h_1*h_2$. Since convolution is commutative, the order of LTI subsystems in cascade may be swapped without changing the overall response.

Course-level takeaway: commutativity explains swapping, associativity explains cascade equivalence, and distributivity explains parallel branches. These properties are not extra facts bolted onto convolution; they are why block-diagram simplification works.

These properties turn block-diagram structure into signal algebra: parallel means addition of impulse responses, cascade means convolution of impulse responses.

---

Flashcards for this section are as follows:

- What is the commutative property of convolution? ::@:: $f_1*f_2=f_2*f_1$.
- Which change of variables proves commutativity? ::@:: Use $\lambda=t-\tau$ in $(f_1*f_2)(t)=\int f_1(\tau)f_2(t-\tau)\,d\tau$ to get $(f_2*f_1)(t)$.
- What is the distributive property? ::@:: $f*(h_1+h_2)=f*h_1+f*h_2$.
- How does distributivity model parallel LTI systems? ::@:: Feeding the same input into both subsystems and adding outputs gives overall impulse response $h=h_1+h_2$.
- What is the associative property? ::@:: $(f*h_1)*h_2=f*(h_1*h_2)$.
- How does associativity model cascade connection? ::@:: The input passes through subsystems with impulse responses $h_1$ and $h_2$, giving overall $h=h_1*h_2$.
- How does convolution commutativity let you swap the roles of input and impulse response in response analysis? ::@:: It means one may view the input as being spread by the impulse response or the impulse response as being weighted by the input, and the same output results.
- Which block-diagram operation corresponds to adding impulse responses, and which to convolving them? ::@:: Parallel connection adds impulse responses; cascade connection convolves them.

## time shift and special kernels

The time-shift property says delaying one factor delays the convolution output by the same amount. If $g(t)=f_1(t)*f_2(t)$, then $f_1(t-t_0)*f_2(t)=g(t-t_0)$ and likewise $f_1(t)*f_2(t-t_0)=g(t-t_0)$. The delay may be applied before or after convolution, which is what one expects from an LTI system.

Graphically, a pure delay slides a waveform horizontally without reshaping it. If $f_1$ is shifted right by $t_0$, then at every observation time $t$ the overlap picture used in convolution is the old overlap picture viewed at the earlier time $t-t_0$. The output graph is simply the old graph shifted right by the same amount. The same holds when the delayed factor is $f_2$, because the overlap geometry depends only on relative displacement, not on which factor slides.

There is also a clean operator interpretation. Write $\delta_{t_0}(t)=\delta(t-t_0)$ for a delayed impulse. Since convolution with a delayed impulse produces a delayed copy, every pure delay can be written as $f(t-t_0)=f*\delta_{t_0}$. Therefore $\bigl(f_1*\delta_{t_0}\bigr)*f_2=f_1*\bigl(\delta_{t_0}*f_2\bigr)=(f_1*f_2)*\delta_{t_0}=g*\delta_{t_0}=g(t-t_0)$. The time-delay identities follow from three facts: delayed impulses represent pure delays, convolution is associative, and convolution is commutative. Repeated delays add because $\delta(t-t_1)*\delta(t-t_2)=\delta(t-(t_1+t_2))$.

These kernels make this rule especially transparent. Convolution with the unit impulse leaves a signal unchanged: $(f*\delta)(t)=f(t)$.

Convolution with a shifted impulse delays the signal: $(f*\delta(t-t_0))(t)=f(t-t_0)$.

An ideal conductor has impulse response $\delta(t)$ and an ideal delayer has impulse response $\delta(t-t_0)$. A pure-delay system does not distort amplitudes, stretch time, or mix neighbouring source times; it waits for $t_0$ time units and then releases the same waveform.

For example, if each input event produces a fixed payment of $4$ dollars exactly $2$ seconds later, the impulse response is $h(t)=4\delta(t-2)$ and the output is $y(t)=x(t)*h(t)=4x(t-2)$. The waveform shape is preserved, shifted right by $2$ seconds, and multiplied by $4$.

Convolution with the derivative of the impulse differentiates: $f(t)*\delta'(t)=f'(t)$ and $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$. Convolution with the step accumulates: $(f*u)(t)=\int_{-\infty}^{t}f(\tau)\,d\tau$.

The three special kernels: $\delta$ gives identity, $\delta'$ gives differentiation, and $u$ gives integration.

---

Flashcards for this section are as follows:

- Why is treating a delay as a shifted impulse useful in convolution? ::@:: It lets delay be handled as an ordinary convolution factor, so the same swap and regroup logic applies.
- Why does $\delta(t)$ model an ideal conductor and $\delta(t-t_0)$ model an ideal delay line? ::@:: Convolving with $\delta(t)$ leaves the signal unchanged, which is exactly what a through-connection does; convolving with $\delta(t-t_0)$ reproduce the same waveform later in time without changing its shape, which is exactly what a pure delay does.
- What delay identity does convolution satisfy? ::@:: If $g(t)=f_1(t)*f_2(t)$, then delaying either factor by $t_0$ delays the output: $f_1(t-t_0)*f_2(t)=g(t-t_0)$ and $f_1(t)*f_2(t-t_0)=g(t-t_0)$.
- Why does delaying one convolution factor simply delay the output of an LTI system? ::@:: Because delaying the excitation before the system should simply delay the response, and convolution preserves exactly that behaviour.
- How does the overlap picture explain why a delayed factor shifts the convolution output? ::@:: A pure delay slides one factor horizontally without changing its shape, so the overlap picture at time $t$ is the old overlap picture at time $t-t_0$; the output graph shifts rigidly by the same amount.
- How does writing a delay as convolution with $\delta(t-t_0)$ prove the time-shift property? ::@:: Since $f(t-t_0)=f*\delta(t-t_0)$, associativity gives $(f_1*\delta(t-t_0))*f_2=(f_1*f_2)*\delta(t-t_0)=g(t-t_0)$.
- What does convolution with $\delta(t)$ do? ::@:: It leaves the signal unchanged: $f(t)*\delta(t)=f(t)$.
- What does convolution with $\delta(t-t_0)$ do? ::@:: It delays the signal by $t_0$: $f(t-t_0)$.
- How does the integral produce $f(t-t_0)$ when the kernel is $\delta(t-t_0)$? ::@:: The impulse samples the input at $\tau=t-t_0$, so $(f*\delta(t-t_0))(t)=\int f(\tau)\delta(t-\tau-t_0)\,d\tau=f(t-t_0)$.
- Why does $\delta(t-t_1)*\delta(t-t_2)=\delta(t-(t_1+t_2))$ mean pure delays add? ::@:: Because delaying by $t_1$ then $t_2$ gives total delay $t_1+t_2$.
- What is the result of convolving with $\delta'(t)$? ::@:: It differentiates: $f(t)*\delta'(t)=f'(t)$.
- How does the accumulation identity $f(t)*u(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$ derive from the support of $u(t-\tau)$? ::@:: Since $u(t-\tau)=1$ only when $\tau\le t$, the convolution integral reduces from $\int_{-\infty}^{\infty}f(\tau)u(t-\tau)\,d\tau$ to $\int_{-\infty}^{t}f(\tau)\,d\tau$.
- Why does $f*\delta^{(k)}=f^{(k)}$ mean $\delta^{(k)}$ acts like a differentiation kernel? ::@:: Because convolving with $\delta^{(k)}$ applies a $k$th derivative to the signal, so inserting $\delta^{(k)}$ into a convolution is the same as differentiating $k$ times.

## differentiation and integration properties

Convolution interacts cleanly with calculus. If $g(t)=f(t)*h(t)$ and the required derivatives exist, differentiating the output may be transferred onto either factor: $g'(t)=f'(t)*h(t)=f(t)*h'(t)$.

The cleanest derivation: $g'(t)=\frac{d}{dt}\int_{-\infty}^{\infty}f(\tau)h(t-\tau)\,d\tau=\int_{-\infty}^{\infty}f(\tau)h'(t-\tau)\,d\tau=(f*h')(t)$. Commutativity then lets the derivative be moved onto the other factor.

The same rule iterates. For every integer $k\ge 0$ for which the generalized derivatives are defined, $g^{(k)}(t)=f^{(k)}(t)*h(t)=f(t)*h^{(k)}(t)$. Equivalently, convolution with $\delta^{(k)}$ acts as $k$th differentiation: $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$. In particular, if $h^{(k)}$ is a short sum of shifted impulses, $f*h^{(k)}$ collapses into a weighted sum of shifted copies of $f$ or its antiderivatives.

Integration behaves similarly. If $F(t)=\int_{-\infty}^{t} f(\lambda)\,d\lambda$ and $H(t)=\int_{-\infty}^{t} h(\lambda)\,d\lambda$, then integrating the convolution output equals convolving one factor with the integrated form of the other: $\int_{-\infty}^{t} g(\lambda)\,d\lambda = F*h = f*H$ (zero-state accumulation). If $f^{(-1)}=F$, then $f*h=f^{(-1)}*h'=f'*h^{(-1)}$ whenever the relevant derivatives and zero-state antiderivatives exist.

The main intuition: convolution is built from shifting, weighting, and adding, while differentiation and integration commute with these constructions under the usual regularity assumptions. One can move derivatives or integrals through a convolution sign instead of recomputing the whole integral.

---

Flashcards for this section are as follows:

- What derivative-transfer rule does convolution satisfy? ::@:: $g'(t)=f'(t)*h(t)=f(t)*h'(t)$.
- Which basic kernel types keep reappearing in the note? ::@:: The unit impulse (identity), the shifted impulse (delay), the impulse derivative (differentiation), and the unit step (integration).
- How do you derive $g'=f*h'$? ::@:: Differentiate under the integral: $g'(t)=\frac{d}{dt}\int f(\tau)h(t-\tau)\,d\tau=\int f(\tau)h'(t-\tau)\,d\tau=(f*h')(t)$.
- What is the $k$th-order derivative-transfer rule? ::@:: $g^{(k)}(t)=f^{(k)}(t)*h(t)=f(t)*h^{(k)}(t)$.
- Why does $f*\delta^{(k)}=f^{(k)}$? ::@:: Because $\delta^{(k)}$ acts as a differentiation kernel inside convolution.
- How can integration be viewed as convolving with an antiderivative? ::@:: Integrating the output equals convolving one factor with the integrated form of the other: $\int_{-\infty}^{t} g(\lambda)\,d\lambda = F*h = f*H$.
- Why do differentiation and integration commute with convolution? ::@:: Because convolution is built from shifting, weighting, and addition, and differentiation and integration commute with those constructions.
- Why is it useful to move the derivative onto whichever factor is simpler? ::@:: Because it avoids differentiating the full convolution integral; you can differentiate the simpler factor instead.
- How can $f*h$ be rewritten using antiderivatives? ::@:: When zero-state antiderivatives exist, $f*h=f^{(-1)}*h'=f'*h^{(-1)}$, letting you move derivatives between factors.

## impulse-pair shortcut for a gate kernel

The first worked example shows how differentiation and integration can simplify a convolution before any overlap integral is drawn. Let $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, so $f(t)=1$ on $0\le t<1$, $f(t)=-1$ on $1\le t<2$, and $f(t)=0$ otherwise, while $h(t)$ is a unit-height gate on $0\le t<1$.

Instead of convolving these two piecewise signals directly, define the zero-state antiderivative $f^{(-1)}(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$. Then $f^{(-1)}(t)=0$ for $t<0$, $f^{(-1)}(t)=t$ for $0\le t<1$, $f^{(-1)}(t)=2-t$ for $1\le t<2$, and $f^{(-1)}(t)=0$ for $t\ge 2$. This is the triangular signal shown in the lecture. Since $h(t)=u(t)-u(t-1)$, its derivative is the impulse pair $h'(t)=\delta(t)-\delta(t-1)$.

Now use the bookkeeping rule: $g(t)=f(t)*h(t)=f^{(-1)}(t)*h'(t)=f^{(-1)}(t)*\bigl[\delta(t)-\delta(t-1)\bigr]$. Convolution with shifted impulses gives weighted and shifted copies of $f^{(-1)}$, so $g(t)=f^{(-1)}(t)-f^{(-1)}(t-1)$. The entire convolution reduces to subtracting a delayed triangular waveform from the original.

Writing the answer piecewise gives $g(t)=0$ for $t<0$, $g(t)=t$ for $0\le t<1$, $g(t)=3-2t$ for $1\le t<2$, $g(t)=t-3$ for $2\le t<3$, and $g(t)=0$ for $t\ge 3$. The graph rises linearly from $0$ to $1$, then falls more steeply through $0$ to $-1$, and finally rises back to $0$. The methodological point: if one factor differentiates into a short impulse sum, convolution can often be done faster by integrating the other factor once and using shift identities, instead of performing the full overlap integral. A gate or rectangular kernel often differentiates into just a few impulses, while the other factor becomes much easier after one integration.

---

Flashcards for this section are as follows:

- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, what zero-state antiderivative $f^{(-1)}(t)$ is useful for computing $g(t)=f*h$? ::@:: Step 1: define $f^{(-1)}(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$. <br/> Step 2: for $t<0$, $f^{(-1)}(t)=0$. <br/> Step 3: for $0\le t<1$, $f^{(-1)}(t)=t$. <br/> Step 4: for $1\le t<2$, $f^{(-1)}(t)=2-t$. <br/> Step 5: for $t\ge 2$, $f^{(-1)}(t)=0$. <!--SR:!fsrs,2027-06-27T00:00:00.000Z,342,341.59171226,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-04-20T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- Worked example: Given $h(t)=u(t)-u(t-1)$, what is $h'(t)$ and why is that useful in convolution? ::@:: Step 1: differentiate the rising edge $u(t)$ to get $\delta(t)$. <br/> Step 2: differentiate the falling edge $-u(t-1)$ to get $-\delta(t-1)$. <br/> Step 3: therefore $h'(t)=\delta(t)-\delta(t-1)$. <br/> Step 4: this is useful because convolution allows the derivative to be moved onto the simpler factor, so one may compute $f*h$ as $f^{(-1)}*h'$ instead. <br/> Step 5: once $h'$ becomes a short impulse pair, the convolution collapses to a difference of shifted copies of $f^{(-1)}$ rather than a full piecewise overlap integral.  <br/> Step 6: this is a general shortcut whenever differentiating one factor and integrating the other makes the algebra simpler than direct convolution. <!--SR:!fsrs,2027-04-09T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-07-31T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, how can $g(t)=f*h$ be rewritten using the integration-differentiation property? ::@:: Step 1: rewrite it as $g(t)=f^{(-1)}(t)*h'(t)$. <br/> Step 2: substitute $h'(t)=\delta(t)-\delta(t-1)$. <br/> Step 3: use $f*\delta(t-t_0)=f(t-t_0)$ term by term to obtain $g(t)=f^{(-1)}(t)-f^{(-1)}(t-1)$. <!--SR:!fsrs,2027-07-20T00:00:00.000Z,360,359.78905058,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-10-29T00:00:00.000Z,433,432.72628656,1,2,7,0,0,2026-08-22T00:00:00.000Z-->
- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, what is the final piecewise form of $g(t)=f*h$? ::@:: Step 1: for $t<0$, both $f^{(-1)}(t)$ and $f^{(-1)}(t-1)$ are $0$, so $g(t)=0$. <br/> Step 2: for $0\le t<1$, use $f^{(-1)}(t)=t$ and $f^{(-1)}(t-1)=0$, so $g(t)=t$. <br/> Step 3: for $1\le t<2$, use $f^{(-1)}(t)=2-t$ and $f^{(-1)}(t-1)=t-1$, so $g(t)=3-2t$. <br/> Step 4: for $2\le t<3$, use $f^{(-1)}(t)=0$ and $f^{(-1)}(t-1)=3-t$, so $g(t)=t-3$. <br/> Step 5: for $t\ge 3$, both terms vanish again, so $g(t)=0$. <!--SR:!fsrs,2027-07-08T00:00:00.000Z,351,350.70809524,1,2,7,0,0,2026-07-22T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-08-12T00:00:00.000Z-->
- Why is the antiderivative-plus-impulse-pair trick useful in this example? ::@:: Because differentiating the gate turns it into a short sum of shifted impulses, so convolution becomes subtraction of shifted antiderivatives instead of a longer direct overlap computation. <!--SR:!fsrs,2027-06-27T00:00:00.000Z,342,341.59171226,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z-->

## analytical convolution and integration limits

The analytical method starts from $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty} e(\tau)h(t-\tau)\,d\tau$, but the real challenge is usually not the antiderivative. It is finding the correct overlap interval where both factors are nonzero. Causality or finite support often shrinks the nominal interval $(-\infty,\infty)$ to a much smaller region.

The pulse-through-memory example makes this concrete. Let $e(t)=u(t)-u(t-t_0)$ with $t_0>0$, so the input is a unit-height rectangular pulse of width $t_0$, and let $h(t)=e^{-t}u(t)$. By linearity one may split the output as $r(t)=r_1(t)-r_2(t)$, where $r_1(t)=u(t)*h(t)$ and $r_2(t)=u(t-t_0)*h(t)$.

For $r_1(t)$, the integrand is nonzero only when $\tau>0$ and $t-\tau>0$, so for $t>0$ the overlap interval is $0<\tau<t$. Therefore $r_1(t)=\int_{0}^{t} e^{-(t-\tau)}\,d\tau=(1-e^{-t})u(t)$. For $r_2(t)$, the delayed step forces $\tau>t_0$ while causality requires $t-\tau>0$, so for $t>t_0$ the overlap interval is $t_0<\tau<t$. Hence $r_2(t)=\int_{t_0}^{t} e^{-(t-\tau)}\,d\tau=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. The full response is $r(t)=(1-e^{-t})u(t)-\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$.

This result has a useful interpretation. When the pulse turns on, the output begins to rise like a first-order memory system trying to catch up with the input. When the pulse turns off at $t=t_0$, the stored memory does not vanish instantly; the second term subtracts a delayed exponential catch-up curve. The system has memory whose output depends on both the current input and past inputs.

---

Flashcards for this section are as follows:

- What is usually the hardest part of analytical convolution in practice? ::@:: Determining the correct overlap interval on which both factors are nonzero, not performing the final antiderivative. <!--SR:!fsrs,2027-07-20T00:00:00.000Z,360,359.78905058,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,391,391.31028346,1,2,7,0,0,2026-08-17T00:00:00.000Z-->
- Why do the limits of integration in convolution often shrink from $(-\infty,\infty)$? ::@:: Because causality or finite support forces many parts of the integrand to be zero, so only the overlap region contributes. <!--SR:!fsrs,2027-08-27T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, why is it useful to write $r(t)=r_1(t)-r_2(t)$? ::@:: Step 1: split the pulse as $e(t)=u(t)-u(t-t_0)$. <br/> Step 2: apply linearity to get $r=e*h=u*h-u(t-t_0)*h=r_1-r_2$. <br/> Step 3: each term is then a simpler step-response calculation. <!--SR:!fsrs,2027-04-25T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-08-14T00:00:00.000Z-->
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what overlap interval is used for $r_1(t)=u(t)*h(t)$ and what result follows? ::@:: Step 1: require $u(\tau)\neq 0$, so $\tau>0$. <br/> Step 2: require $u(t-\tau)\neq 0$, so $\tau<t$. <br/> Step 3: therefore the overlap interval is $0<\tau<t$ for $t>0$. <br/> Step 4: compute $r_1(t)=\int_0^t e^{-(t-\tau)}\,d\tau=e^{-t}\int_0^t e^{\tau}\,d\tau=1-e^{-t}$. <br/> Step 5: attach support as $r_1(t)=(1-e^{-t})u(t)$. <!--SR:!fsrs,2027-04-25T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-04-20T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what overlap interval is used for $r_2(t)=u(t-t_0)*h(t)$ and what result follows? ::@:: Step 1: require $u(\tau-t_0)\neq 0$, so $\tau>t_0$. <br/> Step 2: require $u(t-\tau)\neq 0$, so $\tau<t$. <br/> Step 3: therefore the overlap interval is $t_0<\tau<t$ for $t>t_0$. <br/> Step 4: compute $r_2(t)=\int_{t_0}^{t} e^{-(t-\tau)}\,d\tau=e^{-t}\int_{t_0}^{t} e^{\tau}\,d\tau=1-e^{-(t-t_0)}$. <br/> Step 5: attach support as $r_2(t)=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. <!--SR:!fsrs,2027-07-20T00:00:00.000Z,360,359.78905058,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what is the full convolution output and what is its physical interpretation? ::@:: Step 1: combine the two step responses as $r=r_1-r_2$. <br/> Step 2: substitute $r_1=(1-e^{-t})u(t)$ and $r_2=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. <br/> Step 3: obtain $r(t)=(1-e^{-t})u(t)-\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. <br/> Step 4: interpret this as rise during the pulse and delayed decay after turn-off because the system remembers past input. <!--SR:!fsrs,2027-08-11T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2026-12-17T00:00:00.000Z,183,182.9495982,1.98030797,2,6,0,0,2026-06-17T00:00:00.000Z-->

## graphical convolution and overlap geometry

The graphical method turns convolution into a geometry problem on the $\tau$ axis. The procedure: write the convolution in $\tau$; keep one signal as $f_1(\tau)$; time-reverse the other to get $f_2(-\tau)$; shift it to $f_2(t-\tau)$; multiply the overlapping region; and integrate that overlap area as $t$ varies.

The method is especially helpful for piecewise-constant signals. In a standard rectangular example, take $f_1(t)=2$ for $-1\le t\le 1$ and $0$ otherwise, and take $f_2(t)=1$ for $0\le t\le 3$ and $0$ otherwise. The output is the piecewise function $g(t)=0$ for $t\le -1$, $g(t)=2t+2$ for $-1\le t\le 1$, $g(t)=4$ for $1\le t\le 2$, $g(t)=-2t+8$ for $2\le t\le 4$, and $g(t)=0$ for $t\ge 4$.

The same geometry gives a general support rule. If $f_1$ is supported on $[A,B]$ and $f_2$ is supported on $[C,D]$, the convolution support runs from $A+C$ to $B+D$. Equivalently, the width of the convolution output is the sum of the widths of the two signals. This is one of the fastest ways to sanity-check a convolution result.

The interval arithmetic behind this rule is short and worth remembering. A contribution to $(f_1*f_2)(t)$ requires $A\le \tau\le B$ and $C\le t-\tau\le D$. The second inequality is equivalent to $t-D\le \tau\le t-C$. Overlap exists exactly when the intervals $[A,B]$ and $[t-D,t-C]$ intersect. That happens if and only if $A\le t-C$ and $t-D\le B$, which simplifies to $A+C\le t\le B+D$.

---

Flashcards for this section are as follows:

- What are the main steps of the graphical convolution method? ::@:: Write the integral in $\tau$, keep one signal as $f_1(\tau)$, time-reverse the other to $f_2(-\tau)$, shift it to $f_2(t-\tau)$, multiply the overlap, and integrate the overlap area as $t$ varies. <!--SR:!fsrs,2027-07-25T00:00:00.000Z,364,364.31663824,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-04-14T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- Why is the graphical method useful when formulas are awkward? ::@:: It turns convolution into a support-overlap geometry problem, making the correct intervals easier to see than in direct symbolic integration. <!--SR:!fsrs,2027-08-27T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-07-02T00:00:00.000Z,346,346.154398,1,2,7,0,0,2026-07-21T00:00:00.000Z-->
- Worked example: Given $f_1(t)=2$ for $-1\le t\le 1$ and $0$ otherwise, and $f_2(t)=1$ for $0\le t\le 3$ and $0$ otherwise, what is $(f_1*f_2)(t)$? ::@:: Step 1: add supports to get the output support $[-1,4]$, so the result is $0$ outside that interval. <br/> Step 2: for $-1\le t\le 1$, overlap length is $t+1$, so the area is $2(t+1)=2t+2$. <br/> Step 3: for $1\le t\le 2$, full overlap gives area $2\cdot 2=4$. <br/> Step 4: for $2\le t\le 4$, overlap length is $4-t$, so the area is $2(4-t)=-2t+8$. <br/> Step 5: therefore $(f_1*f_2)(t)$ is piecewise $0$, $2t+2$, $4$, $-2t+8$, $0$. <!--SR:!fsrs,2027-07-31T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- Why does the rectangular-rectangle graphical example produce a trapezoidal output? ::@:: Because the overlap area first grows linearly, then stays constant during full overlap, and finally shrinks linearly as the rectangles separate. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-04-25T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- If $f_1$ is supported on $[A,B]$ and $f_2$ is supported on $[C,D]$, what interval supports the convolution $f_1*f_2$? ::@:: Its support runs from $A+C$ to $B+D$. <!--SR:!fsrs,2027-09-18T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-08-18T00:00:00.000Z!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z-->
- Why does the support rule for continuous-time convolution become $A+C\le t\le B+D$? ::@:: Because a nonzero overlap requires both $A\le \tau\le B$ and $C\le t-\tau\le D$, which is equivalent to overlap between $[A,B]$ and $[t-D,t-C]$; that overlap exists exactly when $A+C\le t\le B+D$. <!--SR:!fsrs,2027-09-12T00:00:00.000Z,391,391.31028346,1,2,7,0,0,2026-08-17T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- What width rule follows from the support formula for convolution? ::@:: The width of the convolution output equals the sum of the widths of the two input signals. <!--SR:!fsrs,2027-04-14T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-07-31T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-07-27T00:00:00.000Z-->

## discrete-time convolution sum

The discrete-time story follows the same logic as continuous time, but impulses become ordinary sequences and integrals become sums. Any sequence can be decomposed as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$. If the system has unit impulse response $h[n]$, the shifted impulse $\delta[n-m]$ produces the shifted response $h[n-m]$. By linearity, the zero-state output is the weighted sum $y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$.

A unifying viewpoint: discrete-time convolution is continuous-time convolution performed on impulse trains at sample instants. If the sample period is normalized to $1$, define the continuous-time embeddings $x_\delta(t)=\sum_{n=-\infty}^{\infty}x[n]\delta(t-n)$ and $h_\delta(t)=\sum_{n=-\infty}^{\infty}h[n]\delta(t-n)$. Then $x_\delta*h_\delta=\sum_{k=-\infty}^{\infty}\bigl(\sum_{m=-\infty}^{\infty}x[m]h[k-m]\bigr)\delta(t-k)$. The coefficient of the impulse at $t=k$ is the discrete convolution sum $(x*h)[k]$.

The operator derivation is exactly parallel to the continuous-time case. If $H$ is the zero-state discrete-time LTI operator, $H[x][n]=H\!\left[\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]\right]=\sum_{m=-\infty}^{\infty}x[m]H[\delta[n-m]]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$.

The convolution sum follows from decomposition into shifted unit samples together with linearity and shift invariance.

This sum is the __discrete convolution sum__, written as $y[n]=(x*h)[n]$. The index $m$ is the source index and $n$ is the observation index. The formula is read like the continuous-time convolution integral, except that the signal is built from weighted shifted unit samples rather than weighted shifted impulses with infinitesimal area.

The algebraic properties transfer automatically from continuous time. Commutativity, associativity, distributivity, and delay rules already hold for continuous-time convolution of the embedded impulse trains, so the same identities hold for the discrete coefficient sequences read off from those trains.

Still, discrete-time and continuous-time representations are not literally identical. The symbol $\delta[n]$ is the Kronecker delta (ordinary sequence, $1$ at $n=0$, $0$ elsewhere); $\delta(t)$ is the Dirac delta (generalized function defined by unit area). Discrete-time graphs are stems at integer indices; continuous-time impulse representations are symbolic arrows. Sums replace integrals, integer index shifts replace real-valued time shifts, and physical units must be handled carefully: if the actual sample spacing is $T_s$ rather than $1$, embed the sequence using impulses at $t=nT_s$, and an extra scaling factor may be needed depending on whether coefficients represent sample values, impulse weights, or approximated areas.

The conceptual importance is the same as before: once the response to one shifted impulse is known, the total zero-state response is the sum of all shifted and weighted copies. Discrete convolution is the push-through-sum rule: decompose the input into shifted unit samples, replace each by the corresponding shifted impulse response, and add.

---

Flashcards for this section are as follows:

- How is an arbitrary discrete-time sequence decomposed into shifted unit samples? ::@:: It is written as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$.
- If the impulse response is $h[n]$, what response is produced by the shifted unit sample $\delta[n-m]$? ::@:: By time invariance it produces the shifted impulse response $h[n-m]$.
- How can discrete-time convolution be viewed as continuous-time convolution of impulse trains? ::@:: Embed the sequences as $x_\delta(t)=\sum_n x[n]\delta(t-n)$ and $h_\delta(t)=\sum_n h[n]\delta(t-n)$; then the coefficient of $\delta(t-k)$ in $x_\delta*h_\delta$ is $(x*h)[k]$.
- What is the discrete convolution sum for zero-state response? ::@:: $y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]=(x*h)[n]$.
- What do the indices $m$ and $n$ mean in the sum? ::@:: $m$ is the source index from which input contributions originate, while $n$ is the observation index at which the output is evaluated.
- What are the main differences between $\delta[n]$ and $\delta(t)$? ::@:: $\delta[n]$ is an ordinary sequence ($1$ at $n=0$, $0$ elsewhere), while $\delta(t)$ is a generalized function defined by unit area; the former is a stem, the latter a symbolic arrow.
- Why is the discrete convolution sum the natural zero-state formula? ::@:: Because each shifted unit sample produces a shifted copy of $h[n]$, and linearity says the total output is the sum of all those weighted copies.

## discrete-time properties and support range

Discrete convolution obeys the same algebraic properties as continuous convolution: commutativity, associativity, and distributivity. The impulse-sequence rule is especially useful: $x[n]*\delta[n-m]=x[n-m]$. This means a shifted unit sample acts as a pure shift operator inside discrete convolution, just as a shifted impulse does in continuous time.

The lecture emphasizes output range. If $x[n]$ is supported on $[N_{1,\min},N_{1,\max}]$ and $h[n]$ is supported on $[N_{2,\min},N_{2,\max}]$, the convolution output is supported on $[N_{1,\min}+N_{2,\min},\,N_{1,\max}+N_{2,\max}]$. For finite-length sequences, this gives the length rule $N_y=N_x+N_h-1$.

The derivation mirrors the continuous-time interval argument. A nonzero term in $y[n]=\sum_m x[m]h[n-m]$ requires $N_{1,\min}\le m\le N_{1,\max}$ and $N_{2,\min}\le n-m\le N_{2,\max}$. Rearranging the second inequality gives $n-N_{2,\max}\le m\le n-N_{2,\min}$. The two intervals overlap exactly when $N_{1,\min}+N_{2,\min}\le n\le N_{1,\max}+N_{2,\max}$.

This range formula is a quick sanity check before calculation: if a proposed output starts too early, ends too late, or has the wrong finite length, the convolution has been set up incorrectly.

---

Flashcards for this section are as follows:

- What algebraic properties does discrete convolution share with continuous convolution? ::@:: It shares commutativity, associativity, and distributivity. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-06-08T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-22T00:00:00.000Z-->
- What is the discrete impulse-sequence property? ::@:: $x[n]*\delta[n-m]=x[n-m]$. <!--SR:!fsrs,2027-06-27T00:00:00.000Z,342,341.59171226,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-07-25T00:00:00.000Z,364,364.31663824,1,2,7,0,0,2026-07-26T00:00:00.000Z-->
- Why is $x[n]*\delta[n-m]=x[n-m]$ useful? ::@:: It turns a shifted unit sample into a pure shift operator, making impulse-sequence calculations fast and transparent. <!--SR:!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-09-18T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- If $x[n]$ is supported on $[N_{1,\min},N_{1,\max}]$ and $h[n]$ on $[N_{2,\min},N_{2,\max}]$, what interval supports $x*h$? ::@:: The convolution output is supported on $[N_{1,\min}+N_{2,\min},\,N_{1,\max}+N_{2,\max}]$. <!--SR:!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- Why does the discrete support rule become $N_{1,\min}+N_{2,\min}\le n\le N_{1,\max}+N_{2,\max}$? ::@:: Because a nonzero term requires both $N_{1,\min}\le m\le N_{1,\max}$ and $N_{2,\min}\le n-m\le N_{2,\max}$, and those two intervals overlap exactly on that range of $n$. <!--SR:!fsrs,2027-08-27T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-08-14T00:00:00.000Z-->
- What is the finite-length rule for the length of a convolution output? ::@:: If the input lengths are $N_x$ and $N_h$, then the output length is $N_y=N_x+N_h-1$. <!--SR:!fsrs,2027-04-20T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-08-05T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- Why is the support-range formula useful before doing the detailed sum? ::@:: It gives a quick sanity check on where the output can start, where it can end, and how long a finite convolution result should be. <!--SR:!fsrs,2027-04-14T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-08-05T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-07-28T00:00:00.000Z-->

## computing discrete convolution

Several standard ways to compute discrete convolution are direct analytical summation, graphical inversion-and-shift, use of algebraic properties, and direct sum of pairwise products. The common process is sequence inversion, shift, multiplication, and summation.

The geometric-series step-response example shows the analytical method clearly. If $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and the input is $u[n]$, the step response is $y[n]=u[n]*h[n]=\sum_{m=0}^{n}\alpha^m=\frac{1-\alpha^{n+1}}{1-\alpha}u[n]$. The overlap limits are determined by the one-sided supports: both $u[m]$ and $u[n-m]$ must be nonzero, so only $0\le m\le n$ contributes.

The finite-length example shows the pairwise-product viewpoint. Let $x[n]=1$ for $0\le n\le 4$ and $0$ otherwise, and compute $y[n]=x[n]*x[n]$. The overlap count grows as the shifted copy first begins to overlap, reaches a maximum when overlap is largest, and then shrinks symmetrically. The result is $y[n]=n+1$ for $0\le n\le 4$, $y[n]=9-n$ for $4\le n\le 8$, and $y[n]=0$ otherwise. The values are $1,2,3,4,5,4,3,2,1$ on the support interval $0\le n\le 8$.

These examples illustrate the two main intuitions of discrete convolution. For one-sided geometric sequences, the sum behaves like accumulated memory with shrinking weights. For finite rectangles, the sum counts how many overlapping pairs contribute at each shift.

---

Flashcards for this section are as follows:

- What are the main standard ways to compute discrete convolution? ::@:: Direct analytical summation, graphical inversion-and-shift, use of algebraic properties, and direct sum of pairwise products. <!--SR:!fsrs,2027-08-11T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-09-01T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-08-15T00:00:00.000Z-->
- What is the core step-by-step process behind graphical discrete convolution? ::@:: Sequence inversion, shift, multiplication, and summation. <!--SR:!fsrs,2027-08-16T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-04-09T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- Worked example: Given $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and input $u[n]$, what is the unit-step response $y[n]=u[n]*h[n]$? ::@:: Step 1: write $y[n]=\sum_m u[m]\alpha^m u[n-m]$. <br/> Step 2: the one-sided supports require $0\le m\le n$. <br/> Step 3: therefore $y[n]=\sum_{m=0}^{n}\alpha^m$. <br/> Step 4: evaluate the geometric sum to get $y[n]=\frac{1-\alpha^{n+1}}{1-\alpha}u[n]$. <!--SR:!fsrs,2027-07-25T00:00:00.000Z,364,364.31663824,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-08-21T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-08-13T00:00:00.000Z-->
- Worked example: Given $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and input $u[n]$, why does the convolution sum run only from $m=0$ to $m=n$? ::@:: Because both one-sided factors must be nonzero, so the overlap requires $m\ge 0$ and $n-m\ge 0$, which together give $0\le m\le n$. <!--SR:!fsrs,2027-04-09T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-07-25T00:00:00.000Z,364,364.31663824,1,2,7,0,0,2026-07-26T00:00:00.000Z-->
- Worked example: Given $x[n]=1$ for $0\le n\le 4$ and $0$ otherwise, what is $y[n]=x[n]*x[n]$? ::@:: Step 1: each nonzero product equals $1$, so $y[n]$ counts overlapping samples. <br/> Step 2: for $0\le n\le 4$, the count grows to $n+1$. <br/> Step 3: for $4\le n\le 8$, the count shrinks to $9-n$. <br/> Step 4: outside $0\le n\le 8$, the overlap is empty. <br/> Step 5: hence the nonzero values are $1,2,3,4,5,4,3,2,1$. <!--SR:!fsrs,2027-08-21T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z-->
- Why does the convolution of two length-5 rectangular sequences become triangular? ::@:: Because the number of overlapping sample pairs first increases, then reaches a maximum, and then decreases symmetrically as one sequence slides past the other. <!--SR:!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,391,391.31028346,1,2,7,0,0,2026-08-17T00:00:00.000Z-->

## convolution case studies and intuition

Two useful recognition patterns are worth keeping in view. The first is a weighted impulse train passing through a rectangular kernel. Let $h(t)=u(t)-u(t-T_s)$, so the impulse response is a unit-height rectangle of width $T_s$, and let the input be $f_s(t)=0.5\delta(t)+\delta(t-T_s)+1.5\delta(t-2T_s)+2\delta(t-3T_s)$. By convolution with shifted impulses, the output is $f(t)=0.5h(t)+h(t-T_s)+1.5h(t-2T_s)+2h(t-3T_s)$. Expanding the shifted rectangles gives $f(t)=0.5\bigl(u(t)-u(t-T_s)\bigr)+\bigl(u(t-T_s)-u(t-2T_s)\bigr)+1.5\bigl(u(t-2T_s)-u(t-3T_s)\bigr)+2\bigl(u(t-3T_s)-u(t-4T_s)\bigr)$. The output is a staircase signal: level $0.5$ on $[0,T_s)$, level $1$ on $[T_s,2T_s)$, level $1.5$ on $[2T_s,3T_s)$, level $2$ on $[3T_s,4T_s)$, and zero elsewhere. Convolving an impulse train with a rectangular kernel paints one rectangular segment per impulse weight.

The second pattern is the self-convolution of a unit-width pulse. If $f(t)=u(t)-u(t-1)$, then $s(t)=f(t)*f(t)$ is the triangular waveform obtained by overlap length. The overlap formula is especially compact: $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau=\min(1,t)-\max(0,t-1)$ whenever the overlap interval is nonempty. This gives the piecewise result $s(t)=0$ for $t<0$, $s(t)=t$ for $0<t<1$, $s(t)=2-t$ for $1<t<2$, and $s(t)=0$ for $t>2$. The output reaches its maximum at $t=1$ because that is the instant of full overlap between the two unit-width pulses. This is one of the most important convolution-shape intuitions: identical pulses convolved with themselves often produce a tent-like output whose height tracks overlap length.

---

Flashcards for this section are as follows:

- Worked example: Given $h(t)=u(t)-u(t-T_s)$ and $f_s(t)=0.5\delta(t)+\delta(t-T_s)+1.5\delta(t-2T_s)+2\delta(t-3T_s)$, what is the convolution output $f(t)$? ::@:: Step 1: convolve each weighted impulse separately, so each one produces a weighted shifted copy of $h$. <br/> Step 2: sum the four pieces to get $f(t)=0.5h(t)+h(t-T_s)+1.5h(t-2T_s)+2h(t-3T_s)$. <br/> Step 3: expand each shifted rectangle over its own interval. <br/> Step 4: read off the staircase levels $0.5$, $1$, $1.5$, and $2$ on $[0,T_s)$, $[T_s,2T_s)$, $[2T_s,3T_s)$, and $[3T_s,4T_s)$. <!--SR:!fsrs,2027-07-20T00:00:00.000Z,360,359.78905058,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-07-13T00:00:00.000Z,355,355.25290839,1,2,7,0,0,2026-07-23T00:00:00.000Z-->
- How do the shifted-rectangle terms expand in the staircase example with $h(t)=u(t)-u(t-T_s)$? ::@:: They expand as $0.5\bigl(u(t)-u(t-T_s)\bigr)+\bigl(u(t-T_s)-u(t-2T_s)\bigr)+1.5\bigl(u(t-2T_s)-u(t-3T_s)\bigr)+2\bigl(u(t-3T_s)-u(t-4T_s)\bigr)$, which makes each constant step interval explicit. <!--SR:!fsrs,2027-08-27T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- Why does convolving a weighted impulse train with the rectangular kernel $h(t)=u(t)-u(t-T_s)$ produce a staircase waveform? ::@:: Each shifted impulse generates one shifted rectangle, and the output places those rectangular pieces at the impulse times with the corresponding impulse weights. <!--SR:!fsrs,2027-05-23T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- Worked example: Given $f(t)=u(t)-u(t-1)$, what is $s(t)=f(t)*f(t)$? ::@:: Step 1: write $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau$. <br/> Step 2: for $t<0$, the overlap is empty, so $s(t)=0$. <br/> Step 3: for $0<t<1$, the overlap length is $t$, so $s(t)=t$. <br/> Step 4: for $1<t<2$, the overlap length is $2-t$, so $s(t)=2-t$. <br/> Step 5: for $t>2$, the overlap is empty again, so $s(t)=0$. <!--SR:!fsrs,2027-07-08T00:00:00.000Z,351,350.70809524,1,2,7,0,0,2026-07-22T00:00:00.000Z!fsrs,2027-04-25T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- What compact overlap formula produces the triangular self-convolution of $f(t)=u(t)-u(t-1)$? ::@:: It is $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau=\min(1,t)-\max(0,t-1)$ whenever the overlap interval is nonempty. <!--SR:!fsrs,2027-04-30T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-09-18T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- Worked example: Given $f(t)=u(t)-u(t-1)$, when does $s(t)=f(t)*f(t)$ reach its maximum value, and why? ::@:: Step 1: the output equals the overlap length of two unit-width pulses. <br/> Step 2: that overlap increases as $t$ moves from $0$ to $1$. <br/> Step 3: at $t=1$ the two pulses overlap fully, so the overlap is maximal. <br/> Step 4: after $t=1$ the overlap shrinks again, so the maximum occurs at $t=1$. <!--SR:!fsrs,2027-08-21T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-05-17T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-17T00:00:00.000Z-->
- What general convolution-shape lesson is taught by the self-convolution of a unit-width pulse? ::@:: The output height tracks overlap length, so identical rectangular pulses convolved with themselves produce a triangular or tent-shaped waveform. <!--SR:!fsrs,2027-07-25T00:00:00.000Z,364,364.31663824,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-07-02T00:00:00.000Z,346,346.154398,1,2,7,0,0,2026-07-21T00:00:00.000Z-->
