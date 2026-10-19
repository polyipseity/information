---
aliases:
  - expectation value
  - mean value in quantum mechanics
  - quantum expectation value
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/expectation_value_(quantum_mechanics)
  - language/in/English
---

# expectation value (quantum mechanics)

The expectation value $\langle A \rangle$ of an observable is the average result of many identical measurements on identically prepared systems. It need not be a value the observable ever actually takes: a measurement of a non-integer-valued quantity can have a non-integer mean, just as in statistics. In quantum mechanics every expectation value is an integral over the wave function weighted by $|\Psi|^2$ or by the observable's operator. Measured values are real numbers, so every observable's expectation value is real too.

---

Flashcards for this section are as follows:

- overview: what an expectation value is ::@:: The average of many measurements on identically prepared systems — not necessarily a value that ever occurs in a single measurement. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why an expectation value may never be observed ::@:: It is a weighted mean of outcomes; the mean of integer-valued outcomes can be non-integer and thus never occur. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## definition and position averages

For an observable represented by an operator $\hat{A}$, the expectation value is $\langle A \rangle = \int \Psi^* \hat{A} \Psi \, dx$ over all space, with the normalised $\Psi$. For position itself the operator just multiplies, giving $\langle x \rangle = \int x |\Psi(x,t)|^2 dx$, the position-weighted probability density. Any function of position follows the same pattern, $\langle g(x) \rangle = \int g(x) |\Psi(x,t)|^2 dx$, so $\langle x^2 \rangle$ needs no new machinery. A wave function that has not been normalised divides by the normalisation integral: $\langle x \rangle = \frac{\int x\Psi^*\Psi\,dx}{\int \Psi^*\Psi\,dx}$, which reduces to the plain integral once $\Psi$ is normalised.

---

Flashcards for this section are as follows:

- the general definition of an expectation value $\langle A \rangle$ ::@:: $\langle A \rangle = \int \Psi^* \hat{A} \Psi \, dx$ for a normalised wave function. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the mean position $\langle x \rangle$ ::@:: $\langle x \rangle = \int x |\Psi(x,t)|^2 dx$ — the operator $\hat{x}$ is plain multiplication. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the mean position $\langle x \rangle$ from a wave function that is not yet normalised ::@:: $\langle x \rangle = \frac{\int x\Psi^*\Psi\,dx}{\int \Psi^*\Psi\,dx}$, the position integral divided by the normalisation integral $\int \Psi^*\Psi\,dx$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## momentum and energy averages

Momentum is not a function of position, so its average uses the operator $\hat{p} = -i\hbar\,\partial/\partial x$: $\langle p \rangle = \int \Psi^*(-i\hbar\,\partial/\partial x)\Psi\,dx$. The mean-square momentum $\langle p^2 \rangle$ uses the second derivative form, and the mean energy follows the energy operator, $\langle E \rangle = \int \Psi^*(i\hbar\,\partial/\partial t)\Psi\,dx$, or equivalently, for a stationary state, simply the level's eigenvalue $E_n$. For any real stationary state the momentum average vanishes, and the integral shows why. With $\Psi$ real, $\Psi^* = \Psi$ and the integrand collapses to a perfect derivative: $\Psi\,\partial\Psi/\partial x = \tfrac{1}{2}\,\partial(\Psi^2)/\partial x$, so $$\langle p \rangle = -i\hbar \int \Psi\,\frac{\partial \Psi}{\partial x}\,dx = -\frac{i\hbar}{2}\Big[\Psi^2\Big]_{-\infty}^{+\infty} = 0,$$ a boundary term, since a normalised wave function falls to zero at both ends. A complex $\Psi$ gets no such cancellation: $\Psi^*\,\partial\Psi/\partial x$ is then not a total derivative, and $\langle p \rangle$ can come out nonzero.

---

Flashcards for this section are as follows:

- the momentum expectation value $\langle p \rangle$ ::@:: $\langle p \rangle = \int \Psi^*(-i\hbar\,\partial/\partial x)\Psi\,dx$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why $\langle p \rangle$ vanishes in a real stationary state ::@:: The integrand is a total derivative of $|\Psi|^2/2$, which vanishes at both infinities. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the step that shows $\langle p \rangle = 0$ for a real stationary state ::@:: $\Psi\,\partial\Psi/\partial x = \tfrac{1}{2}\,\partial(\Psi^2)/\partial x$, so $\langle p \rangle = -i\hbar[\Psi^2/2]_{-\infty}^{+\infty} = 0$; a complex $\Psi$ has no such cancellation. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the energy expectation value $\langle E \rangle$, and its shortcut for a stationary state ::@:: $\langle E \rangle = \int \Psi^*(i\hbar\,\partial/\partial t)\Psi\,dx$, or simply the level's eigenvalue $E_n$ when $\Psi$ is a stationary state. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the operator behind the mean-square momentum $\langle p^2 \rangle$ ::@:: The second-derivative form $\hat{p}^2 = -\hbar^2\,\partial^2/\partial x^2$, used as $\langle p^2 \rangle = \int \Psi^*(-\hbar^2\,\partial^2/\partial x^2)\Psi\,dx$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## spread and uncertainty

An average alone does not describe a distribution; its spread does. The variance of position is $\sigma_x^2 = \langle x^2 \rangle - \langle x \rangle^2$, and the uncertainty $\Delta x = \sigma_x$ is its square root. The same construction with $\langle p^2 \rangle - \langle p \rangle^2$ gives $\Delta p$. These spreads are exactly the quantities the [uncertainty principle](uncertainty%20principle.md) bounds below: $\Delta x \cdot \Delta p \geq \hbar/2$ for every normalised state.

---

Flashcards for this section are as follows:

- the variance $\sigma_x^2$ of position from expectation values ::@:: $\sigma_x^2 = \langle x^2 \rangle - \langle x \rangle^2$, with $\Delta x = \sigma_x$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what the uncertainty principle bounds, in terms of $\Delta x \cdot \Delta p$ ::@:: The product of the spreads, $\Delta x \cdot \Delta p \geq \hbar/2$, built from these variances. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## ground state of the box

In the infinite well's ground state $\psi_1 = \sqrt{2/L}\sin(\pi x/L)$, symmetry about the midpoint gives $\langle x \rangle = L/2$, and the real stationary state gives $\langle p \rangle = 0$: the particle is equally likely to run either way, so the two directions cancel in the mean.

The momentum spread is not zero, and the energy fixes it. Inside the well $V = 0$, so $\langle p^2 \rangle = 2m\langle E \rangle = 2mE_1 = h^2/(4L^2)$ and $\Delta p = h/(2L)$.

Position needs its own integral, $\langle x^2 \rangle = \int_0^L x^2\,(2/L)\sin^2(\pi x/L)\,dx$. Product-to-sum, $\sin^2(\pi x/L) = \tfrac{1}{2}\bigl(1 - \cos(2\pi x/L)\bigr)$, splits it into $\langle x^2 \rangle = \tfrac{1}{L}\int_0^L x^2\,dx - \tfrac{1}{L}I$, where $I = \int_0^L x^2\cos(2\pi x/L)\,dx$ and the first integral is $L^2/3$.

Two integrations by parts give $I$. The first pass yields $I = \bigl[x^2\cdot\tfrac{L}{2\pi}\sin(2\pi x/L)\bigr]_0^L - \tfrac{L}{\pi}\int_0^L x\sin(2\pi x/L)\,dx$. The boundary term vanishes because $\sin(0) = \sin(2\pi) = 0$.

The second pass gives $\int_0^L x\sin(2\pi x/L)\,dx = \bigl[-\tfrac{xL}{2\pi}\cos(2\pi x/L)\bigr]_0^L + \tfrac{L}{2\pi}\int_0^L \cos(2\pi x/L)\,dx$. The cosine integral covers a whole period and vanishes, and the boundary term leaves $-L^2/(2\pi)$.

Hence $I = L^3/(2\pi^2)$, so $\langle x^2 \rangle = L^2\bigl(\tfrac{1}{3} - \tfrac{1}{2\pi^2}\bigr)$.

With $\langle x \rangle = L/2$, this gives $\Delta x = L\sqrt{1/12 - 1/(2\pi^2)} \approx 0.18L$.

The product lands at $\Delta x \cdot \Delta p \approx 0.57\,\hbar$: comfortably above the $\hbar/2$ floor of the [uncertainty principle](uncertainty%20principle.md), so the ground state respects the bound without saturating it. What saturation would need is a Gaussian, and the box's sine is not one.

---

Flashcards for this section are as follows:

- the ground-state averages $\langle x \rangle$, $\langle p \rangle$, $\langle p^2 \rangle$ of the infinite well ::@:: $\langle x \rangle = L/2$, $\langle p \rangle = 0$, $\langle p^2 \rangle = 2mE_1 = h^2/(4L^2)$, hence $\Delta p = h/(2L)$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how the ground-state momentum spread $\Delta p$ follows from the energy $E_1$ ::@:: $\langle p^2 \rangle = 2mE_1$ with $E_1 = h^2/(8mL^2)$ gives $\Delta p = \sqrt{2mE_1} = h/(2L)$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the product-to-sum identity that splits the ground-state $\langle x^2 \rangle$ integral ::@:: $\sin^2(\pi x/L) = \tfrac{1}{2}\bigl(1 - \cos(2\pi x/L)\bigr)$ gives $\langle x^2 \rangle = L^2/3 - I/L$ with $I = \int_0^L x^2\cos(2\pi x/L)\,dx$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the first by-parts boundary term in $I = \int_0^L x^2\cos(2\pi x/L)\,dx$ vanishes ::@:: The term $\bigl[x^2\cdot\tfrac{L}{2\pi}\sin(2\pi x/L)\bigr]_0^L$ is zero because $\sin(0) = \sin(2\pi) = 0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the first integration-by-parts result for $I = \int_0^L x^2\cos(2\pi x/L)\,dx$ ::@:: $I = -\tfrac{L}{\pi}\int_0^L x\sin(2\pi x/L)\,dx$ once the boundary term drops. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the second integration-by-parts result in the ground-state $\langle x^2 \rangle$ integral ::@:: $\int_0^L x\sin(2\pi x/L)\,dx = \bigl[-\tfrac{xL}{2\pi}\cos(2\pi x/L)\bigr]_0^L + \tfrac{L}{2\pi}\int_0^L \cos(2\pi x/L)\,dx = -\tfrac{L^2}{2\pi}$: the cosine integral covers a whole period and vanishes. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the value of $I$ and the resulting ground-state $\langle x^2 \rangle$ ::@:: $I = L^3/(2\pi^2)$, so $\langle x^2 \rangle = L^2\bigl(\tfrac{1}{3} - \tfrac{1}{2\pi^2}\bigr)$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the ground-state position spread $\Delta x$ of the infinite well ::@:: $\langle x^2 \rangle = L^2(1/3 - 1/(2\pi^2))$ gives $\Delta x = L\sqrt{1/12 - 1/(2\pi^2)} \approx 0.18L$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the ground-state saturation ratio $\Delta x \cdot \Delta p$ against the bound $\hbar/2$ ::@:: $\Delta x \cdot \Delta p \approx 0.57\,\hbar$: above the floor, since only a Gaussian saturates the bound. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
