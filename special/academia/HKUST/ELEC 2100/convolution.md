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

Convolution is the time-domain formula for zero-state response of linear time-invariant systems. In ELEC 2100 it is introduced as the result of decomposing a signal into shifted impulses, transferring each impulse through the system, and summing the resulting shifted impulse responses.

Many later identities are convolution algebra in disguise: commutativity explains why the two factors can be swapped, associativity explains why LTI blocks can be regrouped in cascade, and those two properties are the reason parallel and series simplifications work. The Dirac delta and its shifted versions model identity and time shift, its derivative models differentiation, and the unit step models integration. Most of the note reduces to reordering convolution factors or choosing a kernel with a special operator meaning.

The same idea works for two-dimensional settings such as images. A 2D convolution kernel is a small weighting pattern that slides over horizontal and vertical coordinates. The output at each pixel is the weighted local sum produced by that sliding window: flip the kernel in both coordinates, shift it to the output location, multiply pointwise over the overlap region, and sum. So the 1D impulse-response idea generalizes from signals in time to signals over two spatial coordinates.

---

Flashcards for this section are as follows:

- What role does convolution play in computing the zero-state response of an LTI system? ::@:: It is the time-domain formula for zero-state response of LTI systems.
- How does the lecture derive convolution from decomposing a signal into shifted impulses? ::@:: By decomposing the input into shifted impulses, transferring each impulse through the system, and summing the shifted impulse responses.
- What does a 2D convolution kernel do when it slides across an image patch? ::@:: It weights nearby values and forms each output as a weighted local sum.
- How does 2D convolution generalize the 1D slide-weight-sum procedure from time signals to images? ::@:: It is the same logic applied to two spatial coordinates instead of one time axis: slide, weight, and sum.
- What are the mechanical steps of 2D convolution? ::@:: Flip the kernel in both coordinates, shift it to the output location, multiply pointwise over the overlap region, and sum.

## impulse-decomposition viewpoint

A signal can be represented as a weighted superposition of shifted impulses. In continuous time the identity is $e(t)=\int_{-\infty}^{\infty} e(\tau)\,\delta(t-\tau)\,d\tau$. For each source time $\tau$, the factor $e(\tau)$ is the weight of the impulse located there, and the full signal is assembled by integrating all those weighted contributions. The narrow-pulse approximation from the lecture is only the intuition; the detailed impulse-response motivation appears in `continuous-time LTI system.md` and `discrete-time LTI system.md`.

This viewpoint matters because it explains why convolution is natural for LTI systems. Once a signal is decomposed into shifted impulses, time invariance tells us what each shifted impulse becomes at the output, and linearity lets us sum all those partial outputs. This is also why the later special-kernel identities work: the algebra is already encoded in the decomposition step.

---

Flashcards for this section are as follows:

- What identity writes a signal as an integral of weighted shifted impulses? ::@:: It is $e(t)=\int_{-\infty}^{\infty} e(\tau)\,\delta(t-\tau)\,d\tau$.
- What does $e(\tau)$ represent as the weight of the source-time impulse in the decomposition integral? ::@:: It is the weight assigned to the impulse located at source time $\tau$.
- What does $\delta(t-\tau)$ represent in the impulse decomposition integral? ::@:: It represents a unit impulse placed at source time $\tau$ and observed at time $t$.
- Why does decomposing an input into shifted impulses make LTI zero-state analysis straightforward? ::@:: Time invariance tells us how each shifted impulse is transferred, and linearity lets us sum all the partial outputs.
- Which earlier notes give the impulse-response motivation used before the decomposition argument? ::@:: The earlier motivation lives in `continuous-time LTI system.md` and `discrete-time LTI system.md`.

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
- What is the continuous-time convolution integral for zero-state response? ::@:: It is $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty} e(\tau)h(t-\tau)\,d\tau$.
- How is the convolution integral derived directly from the operator viewpoint? ::@:: Write $e(t)=\int e(\tau)\delta(t-\tau)\,d\tau$, apply $H$, and use linearity plus time invariance to get $H[e](t)=\int e(\tau)H[\delta(t-\tau)]\,d\tau=\int e(\tau)h(t-\tau)\,d\tau$.
- What compact notation is used for the convolution integral? ::@:: It is written as $r_{\mathrm{zs}}(t)=(e*h)(t)$.
- What do the two factors in the integrand $e(\tau)h(t-\tau)$ mean? ::@:: $e(\tau)$ gives the input weight from source time $\tau$, while $h(t-\tau)$ gives how the system carries that impulse to observation time $t$.
- Why is convolution the formula for zero-state response of an LTI system? ::@:: It is the formal sum of all shifted-impulse responses produced by decomposing the input into weighted impulses.

## physical interpretation of convolution

Each symbol in the convolution integral has a direct role. The variable $\tau$ is the time at which a small piece of the input occurs. The value $e(\tau)$ is the strength of the input at that source time. The variable $t$ is the time at which we observe the output. The factor $h(t-\tau)$ is the amount of response visible at time $t$ due to a unit impulse applied earlier at time $\tau$.

Convolution mixes a source time and an observation time. For each candidate source time $\tau$, the system tells us how much of that earlier event still contributes when we observe the output at time $t$. The integral adds those surviving contributions over all possible source times.

One useful intuition is to imagine each input slice launching a copy of the impulse response. Early slices launch earlier copies, later slices launch later copies, and the observed output at time $t$ is the total overlap of all those shifted copies at that instant. Convolution is therefore not just multiplication under an integral sign; it is an accumulation of delayed system memories weighted by the input.

A queueing-and-revenue analogy makes the roles concrete without changing the mathematics. The source time $\tau$ is when one arrival occurs, the observation time $t$ is when we ask how much accumulated response is visible, $x(\tau)$ is the strength of that arrival, and $h(t-\tau)$ is the amount of contribution from that one-unit arrival that is still visible at time $t$. Delayed copies of one response pattern are launched at different source times and then accumulated.

The same analogy separates three meanings that often get blurred in the algebra. A weighted impulse train models arrivals only at isolated instants. A rectangular impulse response models a fixed service or payment window. A shifted impulse response models a pure delay. Once those meanings are clear, formulas such as $x(t)*\delta(t-t_0)=x(t-t_0)$ are just operator rules for shifting when a contribution becomes visible.

---

Flashcards for this section are as follows:

- In the convolution integral, what does the variable $\tau$ represent? ::@:: It represents the source time at which a small piece of the input occurs.
- In the convolution integral, what does $e(\tau)$ represent? ::@:: It represents the strength of the input at source time $\tau$.
- In the convolution integral, what does the variable $t$ represent? ::@:: It represents the observation time at which the output is being evaluated.
- In the convolution integral, what does $h(t-\tau)$ represent physically? ::@:: It is the amount of response visible at observation time $t$ due to a unit impulse applied at source time $\tau$.
- Why does convolution mix source time $\tau$ and observation time $t$? ::@:: Because it tracks how each earlier input event contributes later when the output is observed at time $t$.
- What is the overlapping impulse-response copies intuition for convolution? ::@:: Each input slice launches a shifted copy of the impulse response, and the output at time $t$ is the total overlap of all those weighted copies at that instant.
- Why is convolution more than multiplication inside an integral? ::@:: Because it represents accumulation of delayed system memories, not just local pointwise interaction.

## algebraic properties and system interconnections

Convolution also behaves like an algebra on signals, and those algebraic rules explain why block-diagram interconnections simplify the way they do.

The __commutative property__ says $f_1*f_2=f_2*f_1$. The two signals play symmetric roles inside the convolution integral. In response analysis, one may think of the input being spread by the impulse response or the impulse response being weighted by the input; the same output results. Many later shortcut identities in ELEC 2100 are this symmetry in action.

The proof is a one-line change of variables: $(f_1*f_2)(t)=\int_{-\infty}^{\infty}f_1(\tau)f_2(t-\tau)\,d\tau=\int_{-\infty}^{\infty}f_1(t-\lambda)f_2(\lambda)\,d\lambda=(f_2*f_1)(t)$, where $\lambda=t-\tau$.

The __distributive property__ says $f*(h_1+h_2)=f*h_1+f*h_2$. This is the rule for parallel LTI systems. If one subsystem has impulse response $h_1$ and another has impulse response $h_2$, feeding the same input into both and adding their outputs gives an overall impulse response $h=h_1+h_2$.

The __associative property__ says $(f*h_1)*h_2=f*(h_1*h_2)$. This is the rule behind cascade or series connection. If an input first passes through a subsystem with impulse response $h_1$ and then through another with impulse response $h_2$, the overall impulse response is $h=h_1*h_2$. Since convolution is also commutative, the order of LTI subsystems in cascade may be swapped without changing the overall response.

The course-level takeaway: commutativity explains swapping, associativity explains regrouping and cascade equivalence, and distributivity explains parallel branches. These properties are not extra facts bolted onto convolution; they are why block-diagram simplification works.

When a later card asks about a swap, a regrouping, or a cascade of blocks, the answer is usually one of these three rules rather than a new theorem.

These properties turn block-diagram structure into signal algebra: parallel means addition of impulse responses, and cascade means convolution of impulse responses.

---

Flashcards for this section are as follows:

- What is the commutative property of convolution? ::@:: It is $f_1*f_2=f_2*f_1$.
- Which change of variables proves that convolution is commutative? ::@:: Use $\lambda=t-\tau$ in $(f_1*f_2)(t)=\int f_1(\tau)f_2(t-\tau)\,d\tau$ to get $\int f_2(\lambda)f_1(t-\lambda)\,d\lambda=(f_2*f_1)(t)$.
- How does convolution commutativity let you swap the roles of input and impulse response in response analysis? ::@:: One may view the input as being spread by the impulse response or the impulse response as being weighted by the input; the same output results.
- What is the distributive property of convolution? ::@:: It is $f*(h_1+h_2)=f*h_1+f*h_2$.
- How does distributivity model two parallel LTI systems with impulse responses $h_1$ and $h_2$? ::@:: Feeding the same input into both parallel subsystems and adding their outputs gives overall impulse response $h=h_1+h_2$.
- What is the associative property of convolution? ::@:: It is $(f*h_1)*h_2=f*(h_1*h_2)$.
- How does associativity model a cascade of LTI subsystems with impulse responses $h_1$ then $h_2$? ::@:: The input passes through subsystems with impulse responses $h_1$ and $h_2$, giving overall impulse response $h=h_1*h_2$.
- Why does convolution commutativity let you swap the order of LTI blocks in cascade? ::@:: Because convolution is commutative, so $h_1*h_2=h_2*h_1$.
- Which block-diagram operation corresponds to adding impulse responses, and which corresponds to convolving them? ::@:: Parallel connection adds impulse responses; cascade connection convolves them.

## time shift and special kernels

The time-shift property says that delaying one factor delays the convolution output by the same amount. If $g(t)=f_1(t)*f_2(t)$, then $f_1(t-t_0)*f_2(t)=g(t-t_0)$ and likewise $f_1(t)*f_2(t-t_0)=g(t-t_0)$. The delay may be applied before or after convolution, which is what one expects from an LTI system.

The graphical intuition is that a pure delay slides a waveform horizontally without reshaping it. If $f_1$ is shifted right by $t_0$, then at every observation time $t$ the overlap picture used in convolution is the old overlap picture viewed at the earlier time $t-t_0$. The output graph is simply the old graph shifted right by the same amount. The same holds when the delayed factor is $f_2$, because the overlap geometry depends only on relative displacement, not on which factor slides.

There is also a clean operator interpretation. Write $\delta_{t_0}(t)=\delta(t-t_0)$ for a delayed impulse. Since convolution with a delayed impulse produces a delayed copy, every pure delay can be written as $f(t-t_0)=f*\delta_{t_0}$. Therefore $\bigl(f_1*\delta_{t_0}\bigr)*f_2=f_1*\bigl(\delta_{t_0}*f_2\bigr)=(f_1*f_2)*\delta_{t_0}=g*\delta_{t_0}=g(t-t_0)$. The time-delay identities follow from three facts: delayed impulses represent pure delays, convolution is associative, and convolution is commutative. Delaying the second factor gives the same result by the same argument, and repeated delays add because $\delta(t-t_1)*\delta(t-t_2)=\delta(t-(t_1+t_2))$.

These kernels make this rule especially transparent. Convolution with the unit impulse leaves a signal unchanged because $(f*\delta)(t)=\int_{-\infty}^{\infty}f(\tau)\delta(t-\tau)\,d\tau=f(t)$.

Convolution with a shifted impulse delays the signal because $(f*\delta(t-t_0))(t)=\int_{-\infty}^{\infty}f(\tau)\delta(t-\tau-t_0)\,d\tau=f(t-t_0)$.

The lecture interprets an ideal conductor as having impulse response $\delta(t)$ and an ideal delayer as having impulse response $\delta(t-t_0)$. A pure-delay system does not distort amplitudes, stretch time, or mix neighbouring source times; it waits for $t_0$ time units and then releases the same waveform. The delayed impulse kernel is the most compact description of "same shape, later in time."

For example, if each input event produces a fixed payment of $4$ dollars exactly $2$ seconds later, the impulse response is $h(t)=4\delta(t-2)$ and the output is $y(t)=x(t)*h(t)=4x(t-2)$. The waveform shape is preserved, shifted right by $2$ seconds, and multiplied by $4$.

The same idea extends to derivatives and integration. Convolution with the derivative of the impulse differentiates the signal, so $f(t)*\delta'(t)=f'(t)$ and more generally $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$. Convolution with the step accumulates the signal because $(f*u)(t)=\int_{-\infty}^{\infty}f(\tau)u(t-\tau)\,d\tau=\int_{-\infty}^{t}f(\tau)\,d\tau$.

These kernels are the cleanest way to remember the three special actions: $\delta$ gives identity, $\delta'$ gives differentiation, and $u$ gives integration.

---

Flashcards for this section are as follows:

- Why is treating a delay as a shifted impulse useful in convolution? ::@:: It lets delay be handled as an ordinary convolution factor, so the same swap and regroup logic applies.
- What delay identity does convolution satisfy when one factor is shifted by $t_0$? ::@:: If $g(t)=f_1(t)*f_2(t)$, then delaying either factor by $t_0$ delays the output by the same amount, so $f_1(t-t_0)*f_2(t)=g(t-t_0)$ and $f_1(t)*f_2(t-t_0)=g(t-t_0)$.
- Why does delaying one convolution factor simply delay the output of an LTI system? ::@:: Because delaying the excitation before the system should simply delay the response, and convolution preserves exactly that behaviour.
- How does the overlap picture explain why a delayed factor shifts the convolution output? ::@:: A pure delay slides one factor horizontally without changing its shape, so the overlap picture at time $t$ is exactly the old overlap picture at time $t-t_0$; the output graph is therefore shifted rigidly by the same amount.
- How does writing a delay as convolution with $\delta(t-t_0)$ prove the time-shift property? ::@:: Since $f(t-t_0)=f*\delta(t-t_0)$, associativity gives $\bigl(f_1*\delta(t-t_0)\bigr)*f_2=(f_1*f_2)*\delta(t-t_0)=g(t-t_0)$, and commutativity gives the same result when the delay is applied to the second factor.
- What does convolution with $\delta(t)$ do to a signal? ::@:: It leaves the signal unchanged: $f(t)*\delta(t)=f(t)$.
- How does the sampling property of the impulse give $f*\delta=f$? ::@:: Evaluate $(f*\delta)(t)=\int f(\tau)\delta(t-\tau)\,d\tau$ using the sampling property to get $f(t)$.
- What does convolution with $\delta(t-t_0)$ do to a signal? ::@:: It delays the signal by $t_0$, giving $f(t-t_0)$.
- How does the convolution integral produce $f(t-t_0)$ when the kernel is $\delta(t-t_0)$? ::@:: Evaluate $(f*\delta(t-t_0))(t)=\int f(\tau)\delta(t-\tau-t_0)\,d\tau$, so the impulse samples the input at $\tau=t-t_0$.
- Why does $\delta(t-t_1)*\delta(t-t_2)=\delta(t-(t_1+t_2))$ mean pure delays add? ::@:: Because delaying by $t_1$ and then by $t_2$ is convolution with $\delta(t-t_1)*\delta(t-t_2)=\delta(t-(t_1+t_2))$, so the total delay is $t_1+t_2$.
- Why is $\delta(t)$ the impulse response of an ideal through-connection? ::@:: Because convolving with $\delta(t)$ leaves the signal unchanged, which is exactly the behaviour of an ideal through connection.
- Why is $\delta(t-t_0)$ the impulse response of an ideal delay line? ::@:: Because convolution with $\delta(t-t_0)$ reproduces the same waveform later in time without changing its shape, so it is the exact kernel for a pure delay.
- If each input event produces a fixed payment of $4$ dollars exactly $2$ seconds later, what impulse response models the rule and what output does it give for input $x(t)$? ::@:: Step 1: a pure delay of $2$ seconds with fixed amount $4$ is $h(t)=4\delta(t-2)$. <br/> Step 2: convolving with a shifted impulse delays and scales the input. <br/> Step 3: therefore $y(t)=x(t)*4\delta(t-2)=4x(t-2)$, shifting the waveform right by $2$ seconds and multiplying by $4$.
- What is the result of convolving a signal with $\delta'(t)$ or more generally with $\delta^{(k)}(t)$? ::@:: It differentiates the signal, giving $f(t)*\delta'(t)=f'(t)$ and $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$.
- What is the result of convolving a signal with the unit step? ::@:: It accumulates: $f(t)*u(t)=\int_{-\infty}^{t} f(\lambda)\,d\lambda$.
- How does the accumulation identity $f(t)*u(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$ derive from the support of $u(t-\tau)$? ::@:: Since $u(t-\tau)=1$ only when $\tau\le t$, the convolution integral reduces from $\int_{-\infty}^{\infty}f(\tau)u(t-\tau)\,d\tau$ to $\int_{-\infty}^{t}f(\tau)\,d\tau$.

## differentiation and integration properties

Convolution interacts cleanly with calculus. If $g(t)=f(t)*h(t)$ and the required derivatives exist, differentiating the output may be transferred onto either factor: $g'(t)=f'(t)*h(t)=f(t)*h'(t)$. This lets one differentiate whichever factor is simpler.

The cleanest derivation starts from the integral form: $g'(t)=\frac{d}{dt}\int_{-\infty}^{\infty}f(\tau)h(t-\tau)\,d\tau=\int_{-\infty}^{\infty}f(\tau)h'(t-\tau)\,d\tau=(f*h')(t)$. Commutativity then lets the derivative be moved onto the other factor as well.

The same rule iterates. For every integer $k\ge 0$ for which the generalized derivatives are defined, $g^{(k)}(t)=f^{(k)}(t)*h(t)=f(t)*h^{(k)}(t)$. Equivalently, because convolution with the kth derivative of the Dirac delta acts as kth differentiation, $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$. One may rewrite kth-order convolution calculus as inserting the kernel $\delta^{(k)}$ where convenient. In particular, if $h^{(k)}$ is a short weighted sum of shifted impulses, $f*h^{(k)}$ collapses into a weighted sum of shifted copies of $f$ or its antiderivatives.

Integration behaves similarly. If $F(t)=\int_{-\infty}^{t} f(\lambda)\,d\lambda$ and $H(t)=\int_{-\infty}^{t} h(\lambda)\,d\lambda$, then integrating the convolution output is convolving one factor with the integrated form of the other: $\int_{-\infty}^{t} g(\lambda)\,d\lambda = F*h = f*H$, understood in the same zero-state accumulation sense used throughout the lecture. If $f^{(-1)}=F$, the bookkeeping identity becomes $f*h=f^{(-1)}*h'=f'*h^{(-1)}$ whenever the relevant derivatives and zero-state antiderivatives exist. This is why step response, convolution with $u(t)$, and integration keep reappearing as the same idea.

The main intuition is that convolution is built from shifting, weighting, and adding, while differentiation and integration commute with these constructions under the usual regularity assumptions. One can move derivatives or integrals through a convolution sign instead of recomputing the whole integral. The note keeps returning to the same few kernel types instead of inventing a fresh rule for each property.

---

Flashcards for this section are as follows:

- What two structural properties explain most later convolution shortcuts? ::@:: Commutativity and associativity.
- Which basic kernel types keep reappearing in the note? ::@:: The unit impulse, the shifted impulse, the impulse derivative, and the unit step; together they model identity, delay, differentiation, and integration.
- What derivative-transfer rule does convolution satisfy for $g=f*h$? ::@:: One may differentiate either factor: $g'(t)=f'(t)*h(t)=f(t)*h'(t)$.
- How do you derive $g'=f*h'$ by differentiating under the integral sign? ::@:: Differentiate under the integral: if $g(t)=\int f(\tau)h(t-\tau)\,d\tau$, then $g'(t)=\int f(\tau)h'(t-\tau)\,d\tau=(f*h')(t)$.
- What is the $k$-th-order derivative-transfer rule for convolution? ::@:: For every integer $k\ge 0$ for which the generalized derivatives exist, $g^{(k)}(t)=f^{(k)}(t)*h(t)=f(t)*h^{(k)}(t)$.
- Why does $f*\delta^{(k)}=f^{(k)}$ mean $\delta^{(k)}$ acts like a differentiation kernel? ::@:: Because $f(t)*\delta^{(k)}(t)=f^{(k)}(t)$, so inserting $\delta^{(k)}$ into a convolution is the same as applying a kth derivative.
- Why is it useful to move the derivative onto whichever factor is simpler? ::@:: It avoids differentiating the full convolution integral directly.
- How can integration be viewed as convolving with an antiderivative in zero-state form? ::@:: Integrating the output equals convolving one factor with the integrated form of the other in zero-state accumulation.
- How can $f*h$ be rewritten as $f^{(-1)}*h'=f'*h^{(-1)}$ when zero-state antiderivatives exist? ::@:: When the relevant derivatives and antiderivatives exist, $f*h=f^{(-1)}*h'=f'*h^{(-1)}$.
- Why do differentiation and integration commute with convolution under the usual regularity assumptions? ::@:: Because convolution is built from shifting, weighting, and addition, and differentiation and integration commute with those constructions.
- Why do the derivative and unit-step kernels feel like operator shortcuts? ::@:: Because they let differentiation and accumulation be moved through the convolution sign without recomputing the integral.

## impulse-pair shortcut for a gate kernel

The first worked property example shows how differentiation and integration can simplify a convolution before any overlap integral is drawn. Let $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, so $f(t)=1$ on $0\le t<1$, $f(t)=-1$ on $1\le t<2$, and $f(t)=0$ otherwise, while $h(t)$ is a unit-height gate on $0\le t<1$.

Instead of convolving these two piecewise signals directly, define the zero-state antiderivative $f^{(-1)}(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$. Then $f^{(-1)}(t)=0$ for $t<0$, $f^{(-1)}(t)=t$ for $0\le t<1$, $f^{(-1)}(t)=2-t$ for $1\le t<2$, and $f^{(-1)}(t)=0$ for $t\ge 2$. This is the triangular signal shown in the lecture. Since $h(t)=u(t)-u(t-1)$, its derivative is the impulse pair $h'(t)=\delta(t)-\delta(t-1)$.

Now use the bookkeeping rule from the previous section: $g(t)=f(t)*h(t)=f^{(-1)}(t)*h'(t)=f^{(-1)}(t)*\bigl[\delta(t)-\delta(t-1)\bigr]$. Convolution with shifted impulses turns immediately into weighted and shifted copies of the original signal, so $g(t)=f^{(-1)}(t)-f^{(-1)}(t-1)$. The entire convolution reduces to subtracting a delayed triangular waveform from the original triangular waveform.

Writing the answer piecewise gives $g(t)=0$ for $t<0$, $g(t)=t$ for $0\le t<1$, $g(t)=3-2t$ for $1\le t<2$, $g(t)=t-3$ for $2\le t<3$, and $g(t)=0$ for $t\ge 3$. The graph rises linearly from $0$ to $1$, then falls more steeply through $0$ to $-1$, and finally rises back to $0$. The point of the example is methodological: if one factor differentiates into a short impulse sum, convolution can often be done faster by integrating the other factor once and then using shift identities, instead of performing the full overlap integral. More broadly, convolution lets us move derivatives and antiderivatives to whichever factor becomes simpler. A gate or rectangular kernel often differentiates into just a few impulses, while the other factor becomes much easier after one integration. So the same convolution can be computed by a strategically chosen derivative/integral split rather than by direct overlap geometry.

---

Flashcards for this section are as follows:

- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, what zero-state antiderivative $f^{(-1)}(t)$ is useful for computing $g(t)=f*h$? ::@:: Step 1: define $f^{(-1)}(t)=\int_{-\infty}^{t}f(\lambda)\,d\lambda$. <br/> Step 2: for $t<0$, $f^{(-1)}(t)=0$. <br/> Step 3: for $0\le t<1$, $f^{(-1)}(t)=t$. <br/> Step 4: for $1\le t<2$, $f^{(-1)}(t)=2-t$. <br/> Step 5: for $t\ge 2$, $f^{(-1)}(t)=0$.
- Worked example: Given $h(t)=u(t)-u(t-1)$, what is $h'(t)$ and why is that useful in convolution? ::@:: Step 1: differentiate the rising edge $u(t)$ to get $\delta(t)$. <br/> Step 2: differentiate the falling edge $-u(t-1)$ to get $-\delta(t-1)$. <br/> Step 3: therefore $h'(t)=\delta(t)-\delta(t-1)$. <br/> Step 4: this is useful because convolution allows the derivative to be moved onto the simpler factor, so one may compute $f*h$ as $f^{(-1)}*h'$ instead. <br/> Step 5: once $h'$ becomes a short impulse pair, the convolution collapses to a difference of shifted copies of $f^{(-1)}$ rather than a full piecewise overlap integral. <br/> Step 6: this is a general shortcut whenever differentiating one factor and integrating the other makes the algebra simpler than direct convolution.
- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, how can $g(t)=f*h$ be rewritten using the integration-differentiation property? ::@:: Step 1: rewrite it as $g(t)=f^{(-1)}(t)*h'(t)$. <br/> Step 2: substitute $h'(t)=\delta(t)-\delta(t-1)$. <br/> Step 3: use $f*\delta(t-t_0)=f(t-t_0)$ term by term to obtain $g(t)=f^{(-1)}(t)-f^{(-1)}(t-1)$.
- Worked example: Given $f(t)=u(t)-2u(t-1)+u(t-2)$ and $h(t)=u(t)-u(t-1)$, what is the final piecewise form of $g(t)=f*h$? ::@:: Step 1: for $t<0$, both $f^{(-1)}(t)$ and $f^{(-1)}(t-1)$ are $0$, so $g(t)=0$. <br/> Step 2: for $0\le t<1$, use $f^{(-1)}(t)=t$ and $f^{(-1)}(t-1)=0$, so $g(t)=t$. <br/> Step 3: for $1\le t<2$, use $f^{(-1)}(t)=2-t$ and $f^{(-1)}(t-1)=t-1$, so $g(t)=3-2t$. <br/> Step 4: for $2\le t<3$, use $f^{(-1)}(t)=0$ and $f^{(-1)}(t-1)=3-t$, so $g(t)=t-3$. <br/> Step 5: for $t\ge 3$, both terms vanish again, so $g(t)=0$.
- Why is the antiderivative-plus-impulse-pair trick useful in this example? ::@:: Because differentiating the gate turns it into a short sum of shifted impulses, so convolution becomes subtraction of shifted antiderivatives instead of a longer direct overlap computation.

## analytical convolution and integration limits

The analytical method starts from $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty} e(\tau)h(t-\tau)\,d\tau$, but the real challenge is usually not the antiderivative. It is finding the correct interval on which both factors are simultaneously nonzero. Integration limits are important because causality or finite support often shrinks the nominal interval $(-\infty,\infty)$ to a much smaller overlap region.

The pulse-through-memory example makes this concrete. Let $e(t)=u(t)-u(t-t_0)$ with $t_0>0$, so the input is a unit-height rectangular pulse of width $t_0$, and let $h(t)=e^{-t}u(t)$. By linearity one may split the output as $r(t)=r_1(t)-r_2(t)$, where $r_1(t)=u(t)*h(t)$ and $r_2(t)=u(t-t_0)*h(t)$.

For $r_1(t)$, the integrand is nonzero only when $\tau>0$ and $t-\tau>0$, so for $t>0$ the overlap interval is $0<\tau<t$. Therefore $r_1(t)=\int_{0}^{t} e^{-(t-\tau)}\,d\tau=(1-e^{-t})u(t)$. For $r_2(t)$, the delayed step forces $\tau>t_0$ while causality requires $t-\tau>0$, so for $t>t_0$ the overlap interval is $t_0<\tau<t$. Hence $r_2(t)=\int_{t_0}^{t} e^{-(t-\tau)}\,d\tau=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. The full response is $r(t)=(1-e^{-t})u(t)-\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$.

This result has a useful interpretation. When the pulse turns on, the output begins to rise like a first-order memory system trying to catch up with the input. When the pulse turns off at $t=t_0$, the stored memory does not vanish instantly; the second term subtracts a delayed exponential catch-up curve. The system has memory whose output depends on both the current input and past inputs.

---

Flashcards for this section are as follows:

- What is usually the hardest part of analytical convolution in practice? ::@:: Determining the correct overlap interval on which both factors are nonzero, not performing the final antiderivative.
- Why do the limits of integration in convolution often shrink from $(-\infty,\infty)$? ::@:: Because causality or finite support forces many parts of the integrand to be zero, so only the overlap region contributes.
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, why is it useful to write $r(t)=r_1(t)-r_2(t)$? ::@:: Step 1: split the pulse as $e(t)=u(t)-u(t-t_0)$. <br/> Step 2: apply linearity to get $r=e*h=u*h-u(t-t_0)*h=r_1-r_2$. <br/> Step 3: each term is then a simpler step-response calculation.
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what overlap interval is used for $r_1(t)=u(t)*h(t)$ and what result follows? ::@:: Step 1: require $u(\tau)\neq 0$, so $\tau>0$. <br/> Step 2: require $u(t-\tau)\neq 0$, so $\tau<t$. <br/> Step 3: therefore the overlap interval is $0<\tau<t$ for $t>0$. <br/> Step 4: compute $r_1(t)=\int_0^t e^{-(t-\tau)}\,d\tau=e^{-t}\int_0^t e^{\tau}\,d\tau=1-e^{-t}$. <br/> Step 5: attach support as $r_1(t)=(1-e^{-t})u(t)$.
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what overlap interval is used for $r_2(t)=u(t-t_0)*h(t)$ and what result follows? ::@:: Step 1: require $u(\tau-t_0)\neq 0$, so $\tau>t_0$. <br/> Step 2: require $u(t-\tau)\neq 0$, so $\tau<t$. <br/> Step 3: therefore the overlap interval is $t_0<\tau<t$ for $t>t_0$. <br/> Step 4: compute $r_2(t)=\int_{t_0}^{t} e^{-(t-\tau)}\,d\tau=e^{-t}\int_{t_0}^{t} e^{\tau}\,d\tau=1-e^{-(t-t_0)}$. <br/> Step 5: attach support as $r_2(t)=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$.
- Worked example: Given $e(t)=u(t)-u(t-t_0)$ with $t_0>0$ and $h(t)=e^{-t}u(t)$, what is the full convolution output and what is its physical interpretation? ::@:: Step 1: combine the two step responses as $r=r_1-r_2$. <br/> Step 2: substitute $r_1=(1-e^{-t})u(t)$ and $r_2=\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. <br/> Step 3: obtain $r(t)=(1-e^{-t})u(t)-\bigl(1-e^{-(t-t_0)}\bigr)u(t-t_0)$. <br/> Step 4: interpret this as rise during the pulse and delayed decay after turn-off because the system remembers past input.

## graphical convolution and overlap geometry

The graphical method is designed for cases where the formulas are awkward but the supports are easy to draw. The procedure is: write the convolution in the variable $\tau$; keep one signal as $f_1(\tau)$; time-reverse the other to get $f_2(-\tau)$; shift it to $f_2(t-\tau)$; multiply the overlapping region; and integrate that overlap area as $t$ varies. This turns convolution into a geometry problem on the $\tau$ axis.

The method is especially helpful for piecewise-constant signals. In a standard rectangular example, take $f_1(t)=2$ for $-1\le t\le 1$ and $0$ otherwise, and take $f_2(t)=1$ for $0\le t\le 3$ and $0$ otherwise. As the shifted reversed rectangle slides across the fixed rectangle, the overlap area first grows linearly, then stays constant while one rectangle lies fully inside the other, and then shrinks linearly. The output is the piecewise function $g(t)=0$ for $t\le -1$, $g(t)=2t+2$ for $-1\le t\le 1$, $g(t)=4$ for $1\le t\le 2$, $g(t)=-2t+8$ for $2\le t\le 4$, and $g(t)=0$ for $t\ge 4$.

The same geometry also gives a general support rule. If $f_1$ is supported on $[A,B]$ and $f_2$ is supported on $[C,D]$, the convolution support runs from $A+C$ to $B+D$. Equivalently, the width of the convolution output is the sum of the widths of the two signals. This is one of the fastest ways to sanity-check a convolution result.

The interval arithmetic behind this rule is short and worth remembering. A contribution to $(f_1*f_2)(t)$ requires $A\le \tau\le B$ and $C\le t-\tau\le D$. The second inequality is equivalent to $t-D\le \tau\le t-C$. Overlap exists exactly when the intervals $[A,B]$ and $[t-D,t-C]$ intersect. That happens if and only if $A\le t-C$ and $t-D\le B$, which simplifies to $A+C\le t\le B+D$.

---

Flashcards for this section are as follows:

- What are the main steps of the graphical convolution method? ::@:: Write the integral in $\tau$, keep one signal as $f_1(\tau)$, time-reverse the other to get $f_2(-\tau)$, shift it to $f_2(t-\tau)$, multiply the overlap, and integrate the overlap area as $t$ varies.
- Why is the graphical method useful when formulas are awkward? ::@:: It turns convolution into a support-overlap geometry problem, making the correct intervals easier to see than in direct symbolic integration.
- Worked example: Given $f_1(t)=2$ for $-1\le t\le 1$ and $0$ otherwise, and $f_2(t)=1$ for $0\le t\le 3$ and $0$ otherwise, what is $(f_1*f_2)(t)$? ::@:: Step 1: add supports to get the output support $[-1,4]$, so the result is $0$ outside that interval. <br/> Step 2: for $-1\le t\le 1$, overlap length is $t+1$, so the area is $2(t+1)=2t+2$. <br/> Step 3: for $1\le t\le 2$, full overlap gives area $2\cdot 2=4$. <br/> Step 4: for $2\le t\le 4$, overlap length is $4-t$, so the area is $2(4-t)=-2t+8$. <br/> Step 5: therefore $(f_1*f_2)(t)$ is piecewise $0$, $2t+2$, $4$, $-2t+8$, $0$.
- Why does the rectangular-rectangle graphical example produce a trapezoidal output? ::@:: Because the overlap area first grows linearly, then stays constant during full overlap, and finally shrinks linearly as the rectangles separate.
- If $f_1$ is supported on $[A,B]$ and $f_2$ is supported on $[C,D]$, what interval supports the convolution $f_1*f_2$? ::@:: Its support runs from $A+C$ to $B+D$.
- Why does the support rule for continuous-time convolution become $A+C\le t\le B+D$? ::@:: Because a nonzero overlap requires both $A\le \tau\le B$ and $C\le t-\tau\le D$, which is equivalent to overlap between $[A,B]$ and $[t-D,t-C]$; that overlap exists exactly when $A+C\le t\le B+D$.
- What width rule follows from the support formula for convolution? ::@:: The width of the convolution output equals the sum of the widths of the two input signals.

## discrete-time convolution sum

The discrete-time story follows the same logic as continuous time, but impulses become ordinary sequences and integrals become sums. Any sequence can be decomposed as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$. If the system has unit impulse response $h[n]$, the shifted impulse $\delta[n-m]$ produces the shifted response $h[n-m]$. By linearity, the zero-state output is the weighted sum $y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$.

A useful unifying viewpoint: discrete-time convolution is continuous-time convolution performed on impulse trains located at sample instants. If the sample period is normalized to $1$, define the continuous-time embeddings $x_\delta(t)=\sum_{n=-\infty}^{\infty}x[n]\delta(t-n)$ and $h_\delta(t)=\sum_{n=-\infty}^{\infty}h[n]\delta(t-n)$. Then $x_\delta*h_\delta=\sum_{k=-\infty}^{\infty}\bigl(\sum_{m=-\infty}^{\infty}x[m]h[k-m]\bigr)\delta(t-k)$. The coefficient of the impulse at $t=k$ is the discrete convolution sum $(x*h)[k]$. Discrete convolution is the same mechanism applied to signals made of Dirac impulses sitting on a sampling lattice.

The operator derivation is exactly parallel to the continuous-time case. If $H$ is the zero-state discrete-time LTI operator, $H[x][n]=H\!\left[\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]\right]=\sum_{m=-\infty}^{\infty}x[m]H[\delta[n-m]]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$.

The convolution sum is again not an arbitrary definition; it is dictated by decomposition into shifted unit samples together with linearity and shift invariance.

This sum is the __discrete convolution sum__, written as $y[n]=(x*h)[n]$. The index $m$ is the source index and the index $n$ is the observation index. The formula is read like the continuous-time convolution integral, except that the signal is built from weighted shifted unit samples rather than weighted shifted impulses with infinitesimal area.

This impulse-train viewpoint also explains why the algebraic properties transfer automatically. Commutativity, associativity, distributivity, and delay rules already hold for continuous-time convolution of the embedded impulse trains, so the same identities hold for the discrete coefficient sequences read off from those trains.

Still, discrete-time and continuous-time representations are not literally identical. The symbol $\delta[n]$ is the Kronecker delta or unit sample sequence, an ordinary sequence with value $1$ at $n=0$ and $0$ elsewhere; $\delta(t)$ is the Dirac delta, a generalized function defined by unit area under integration. Discrete-time graphs are drawn as stems at integer indices, whereas continuous-time impulse representations are symbolic arrows on the real line. Sums replace integrals, integer index shifts replace real-valued time shifts, and physical units must be handled carefully: if the actual sample spacing is $T_s$ rather than $1$, one should embed the sequence using impulses at $t=nT_s$, and an extra scaling factor may be needed depending on whether one wants coefficients to represent sample values, impulse weights, or approximated areas.

The conceptual importance is the same as before: once the response to one shifted impulse is known, the total zero-state response is obtained by adding all shifted and weighted copies. Discrete convolution is the push-through-sum rule for LTI systems: decompose the input into shifted unit samples, replace each by the corresponding shifted impulse response, and add.

---

Flashcards for this section are as follows:

- How is an arbitrary discrete-time sequence decomposed into shifted unit samples? ::@:: It is written as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$.
- If the impulse response is $h[n]$, what response is produced by the shifted unit sample $\delta[n-m]$? ::@:: By time invariance it produces the shifted impulse response $h[n-m]$.
- How can discrete-time convolution be viewed as continuous-time convolution of impulse trains? ::@:: Embed the sequences as $x_\delta(t)=\sum_n x[n]\delta(t-n)$ and $h_\delta(t)=\sum_n h[n]\delta(t-n)$; then the coefficient of $\delta(t-k)$ in $x_\delta*h_\delta$ is $\sum_m x[m]h[k-m]=(x*h)[k]$.
- What is the discrete convolution sum for zero-state response? ::@:: It is $y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$.
- How is the discrete convolution sum derived directly from the operator viewpoint? ::@:: Write $x[n]=\sum_m x[m]\delta[n-m]$, apply the LTI operator $H$, and use linearity plus time invariance to get $H[x][n]=\sum_m x[m]H[\delta[n-m]]=\sum_m x[m]h[n-m]$.
- What compact notation is used for the discrete convolution sum? ::@:: It is written as $y[n]=(x*h)[n]$.
- What do the indices $m$ and $n$ mean in the sum $y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$? ::@:: $m$ is the source index from which input contributions originate, while $n$ is the observation index at which the output is evaluated.
- Why do the standard algebraic properties of discrete convolution follow from the impulse-train viewpoint? ::@:: Because they already hold for continuous-time convolution of the embedded Dirac-impulse trains, so the discrete coefficient sequences inherit them directly.
- What are the main differences between the discrete-time unit sample $\delta[n]$ and the continuous-time Dirac delta $\delta(t)$? ::@:: $\delta[n]$ is an ordinary sequence equal to $1$ at one index and $0$ elsewhere, whereas $\delta(t)$ is a generalized function defined by unit area under integration; the former is drawn as a stem, the latter as a symbolic impulse arrow, and their unit conventions differ.
- Why is the discrete convolution sum the natural zero-state formula for an LTI system? ::@:: Because each shifted unit sample produces a shifted copy of $h[n]$, and linearity says the total output is the sum of all those weighted copies.

## discrete-time properties and support range

Discrete convolution obeys the same algebraic properties as continuous convolution: commutativity, associativity, and distributivity. The impulse-sequence rule is especially useful: $x[n]*\delta[n-m]=x[n-m]$. This means a shifted unit sample acts as a pure shift operator inside discrete convolution, just as a shifted impulse does in continuous time.

The lecture emphasizes output range. If $x[n]$ is supported on $[N_{1,\min},N_{1,\max}]$ and $h[n]$ is supported on $[N_{2,\min},N_{2,\max}]$, the convolution output is supported on $[N_{1,\min}+N_{2,\min},\,N_{1,\max}+N_{2,\max}]$. For finite-length sequences, this gives the length rule $N_y=N_x+N_h-1$.

The derivation mirrors the continuous-time interval argument. A nonzero term in $y[n]=\sum_m x[m]h[n-m]$ requires $N_{1,\min}\le m\le N_{1,\max}$ and $N_{2,\min}\le n-m\le N_{2,\max}$. Rearranging the second inequality gives $n-N_{2,\max}\le m\le n-N_{2,\min}$. The two intervals overlap exactly when $N_{1,\min}+N_{2,\min}\le n\le N_{1,\max}+N_{2,\max}$.

This range formula is a quick sanity check before calculation: if a proposed output starts too early, ends too late, or has the wrong finite length, the convolution has been set up incorrectly.

---

Flashcards for this section are as follows:

- What algebraic properties does discrete convolution share with continuous convolution? ::@:: It shares commutativity, associativity, and distributivity.
- What is the discrete impulse-sequence property inside convolution? ::@:: It is $x[n]*\delta[n-m]=x[n-m]$.
- Why is the property $x[n]*\delta[n-m]=x[n-m]$ useful? ::@:: It turns a shifted unit sample into a pure shift operator, making impulse-sequence calculations fast and transparent.
- If $x[n]$ is supported on $[N_{1,\min},N_{1,\max}]$ and $h[n]$ is supported on $[N_{2,\min},N_{2,\max}]$, what interval supports $x*h$? ::@:: The convolution output is supported on $[N_{1,\min}+N_{2,\min},\,N_{1,\max}+N_{2,\max}]$.
- Why does the discrete support rule become $N_{1,\min}+N_{2,\min}\le n\le N_{1,\max}+N_{2,\max}$? ::@:: Because a nonzero term requires both $N_{1,\min}\le m\le N_{1,\max}$ and $N_{2,\min}\le n-m\le N_{2,\max}$, and those two intervals overlap exactly on that range of $n$.
- What is the finite-length rule for the length of a convolution output? ::@:: If the input lengths are $N_x$ and $N_h$, then the output length is $N_y=N_x+N_h-1$.
- Why is the support-range formula useful before doing the detailed sum? ::@:: It gives a quick sanity check on where the output can start, where it can end, and how long a finite convolution result should be.

## computing discrete convolution

Several standard ways to compute discrete convolution are direct analytical summation, graphical inversion-and-shift, use of algebraic properties, and direct sum of pairwise products. The common process is sequence inversion, shift, multiplication, and summation. Discrete convolution is the sample-by-sample version of the same overlap logic used in graphical continuous-time convolution.

The geometric-series step-response example shows the analytical method clearly. If $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and the input is $u[n]$, the step response is $y[n]=u[n]*h[n]=\sum_{m=0}^{n}\alpha^m=\frac{1-\alpha^{n+1}}{1-\alpha}u[n]$. The overlap limits are determined by the one-sided supports: both $u[m]$ and $u[n-m]$ must be nonzero, so only $0\le m\le n$ contributes.

The finite-length example shows the pairwise-product viewpoint. Let $x[n]=1$ for $0\le n\le 4$ and $0$ otherwise, and compute $y[n]=x[n]*x[n]$. The overlap count grows as the shifted copy first begins to overlap, reaches a maximum when overlap is largest, and then shrinks symmetrically. The result is $y[n]=n+1$ for $0\le n\le 4$, $y[n]=9-n$ for $4\le n\le 8$, and $y[n]=0$ otherwise. The values are $1,2,3,4,5,4,3,2,1$ on the support interval $0\le n\le 8$.

These examples illustrate the two main intuitions of discrete convolution. For one-sided geometric sequences, the sum behaves like accumulated memory with shrinking weights. For finite rectangles, the sum counts how many overlapping pairs contribute at each shift.

---

Flashcards for this section are as follows:

- What are the main standard ways to compute discrete convolution? ::@:: Direct analytical summation, graphical inversion-and-shift, use of algebraic properties, and direct sum of pairwise products.
- What is the core step-by-step process behind graphical discrete convolution? ::@:: Sequence inversion, shift, multiplication, and summation.
- Worked example: Given $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and input $u[n]$, what is the unit-step response $y[n]=u[n]*h[n]$? ::@:: Step 1: write $y[n]=\sum_m u[m]\alpha^m u[n-m]$. <br/> Step 2: the one-sided supports require $0\le m\le n$. <br/> Step 3: therefore $y[n]=\sum_{m=0}^{n}\alpha^m$. <br/> Step 4: evaluate the geometric sum to get $y[n]=\frac{1-\alpha^{n+1}}{1-\alpha}u[n]$.
- Worked example: Given $h[n]=\alpha^n u[n]$ with $0<\alpha<1$ and input $u[n]$, why does the convolution sum run only from $m=0$ to $m=n$? ::@:: Because both one-sided factors must be nonzero, so the overlap requires $m\ge 0$ and $n-m\ge 0$, which together give $0\le m\le n$.
- Worked example: Given $x[n]=1$ for $0\le n\le 4$ and $0$ otherwise, what is $y[n]=x[n]*x[n]$? ::@:: Step 1: each nonzero product equals $1$, so $y[n]$ counts overlapping samples. <br/> Step 2: for $0\le n\le 4$, the count grows to $n+1$. <br/> Step 3: for $4\le n\le 8$, the count shrinks to $9-n$. <br/> Step 4: outside $0\le n\le 8$, the overlap is empty. <br/> Step 5: hence the nonzero values are $1,2,3,4,5,4,3,2,1$.
- Why does the convolution of two length-5 rectangular sequences become triangular? ::@:: Because the number of overlapping sample pairs first increases, then reaches a maximum, and then decreases symmetrically as one sequence slides past the other.

## convolution case studies and intuition

Two useful recognition patterns are worth keeping in view. The first is a weighted impulse train passing through a rectangular kernel. Let $h(t)=u(t)-u(t-T_s)$, so the impulse response is a unit-height rectangle of width $T_s$, and let the input be $f_s(t)=0.5\delta(t)+\delta(t-T_s)+1.5\delta(t-2T_s)+2\delta(t-3T_s)$. By convolution with shifted impulses, the output is $f(t)=0.5h(t)+h(t-T_s)+1.5h(t-2T_s)+2h(t-3T_s)$. Expanding the shifted rectangles gives $f(t)=0.5\bigl(u(t)-u(t-T_s)\bigr)+\bigl(u(t-T_s)-u(t-2T_s)\bigr)+1.5\bigl(u(t-2T_s)-u(t-3T_s)\bigr)+2\bigl(u(t-3T_s)-u(t-4T_s)\bigr)$. The output is a staircase signal: level $0.5$ on $[0,T_s)$, level $1$ on $[T_s,2T_s)$, level $1.5$ on $[2T_s,3T_s)$, level $2$ on $[3T_s,4T_s)$, and zero elsewhere. Convolving an impulse train with a rectangular kernel paints one rectangular segment per impulse weight.

The second pattern is the self-convolution of a unit-width pulse. If $f(t)=u(t)-u(t-1)$, then $s(t)=f(t)*f(t)$ is the triangular waveform obtained by overlap length. The overlap formula is especially compact: $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau=\min(1,t)-\max(0,t-1)$ whenever the overlap interval is nonempty. This gives the piecewise result $s(t)=0$ for $t<0$, $s(t)=t$ for $0<t<1$, $s(t)=2-t$ for $1<t<2$, and $s(t)=0$ for $t>2$. The output reaches its maximum at $t=1$ because that is the instant of full overlap between the two unit-width pulses. This is one of the most important convolution-shape intuitions: identical pulses convolved with themselves often produce a tent-like output whose height tracks overlap length.

---

Flashcards for this section are as follows:

- Worked example: Given $h(t)=u(t)-u(t-T_s)$ and $f_s(t)=0.5\delta(t)+\delta(t-T_s)+1.5\delta(t-2T_s)+2\delta(t-3T_s)$, what is the convolution output $f(t)$? ::@:: Step 1: convolve each weighted impulse separately, so each one produces a weighted shifted copy of $h$. <br/> Step 2: sum the four pieces to get $f(t)=0.5h(t)+h(t-T_s)+1.5h(t-2T_s)+2h(t-3T_s)$. <br/> Step 3: expand each shifted rectangle over its own interval. <br/> Step 4: read off the staircase levels $0.5$, $1$, $1.5$, and $2$ on $[0,T_s)$, $[T_s,2T_s)$, $[2T_s,3T_s)$, and $[3T_s,4T_s)$.
- How do the shifted-rectangle terms expand in the staircase example with $h(t)=u(t)-u(t-T_s)$? ::@:: They expand as $0.5\bigl(u(t)-u(t-T_s)\bigr)+\bigl(u(t-T_s)-u(t-2T_s)\bigr)+1.5\bigl(u(t-2T_s)-u(t-3T_s)\bigr)+2\bigl(u(t-3T_s)-u(t-4T_s)\bigr)$, which makes each constant step interval explicit.
- Why does convolving a weighted impulse train with the rectangular kernel $h(t)=u(t)-u(t-T_s)$ produce a staircase waveform? ::@:: Each shifted impulse generates one shifted rectangle, and the output places those rectangular pieces at the impulse times with the corresponding impulse weights.
- Worked example: Given $f(t)=u(t)-u(t-1)$, what is $s(t)=f(t)*f(t)$? ::@:: Step 1: write $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau$. <br/> Step 2: for $t<0$, the overlap is empty, so $s(t)=0$. <br/> Step 3: for $0<t<1$, the overlap length is $t$, so $s(t)=t$. <br/> Step 4: for $1<t<2$, the overlap length is $2-t$, so $s(t)=2-t$. <br/> Step 5: for $t>2$, the overlap is empty again, so $s(t)=0$.
- What compact overlap formula produces the triangular self-convolution of $f(t)=u(t)-u(t-1)$? ::@:: It is $s(t)=\int_{\max(0,t-1)}^{\min(1,t)}1\,d\tau=\min(1,t)-\max(0,t-1)$ whenever the overlap interval is nonempty.
- Worked example: Given $f(t)=u(t)-u(t-1)$, when does $s(t)=f(t)*f(t)$ reach its maximum value, and why? ::@:: Step 1: the output equals the overlap length of two unit-width pulses. <br/> Step 2: that overlap increases as $t$ moves from $0$ to $1$. <br/> Step 3: at $t=1$ the two pulses overlap fully, so the overlap is maximal. <br/> Step 4: after $t=1$ the overlap shrinks again, so the maximum occurs at $t=1$.
- What general convolution-shape lesson is taught by the self-convolution of a unit-width pulse? ::@:: The output height tracks overlap length, so identical rectangular pulses convolved with themselves produce a triangular or tent-shaped waveform.
