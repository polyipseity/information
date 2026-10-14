---
aliases:
  - Schrödinger equation
  - time-dependent Schrödinger equation
  - time-independent Schrödinger equation
  - wave mechanics
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Schrödinger_equation
  - language/in/English
---

# Schrödinger equation

The Schrödinger equation is the equation of motion of non-relativistic quantum mechanics. Erwin Schrödinger postulated it in 1926, building on de Broglie's matter waves; it plays the role Newton's second law plays classically, but for the wave function rather than a trajectory. Given initial conditions it determines how $\Psi(x,t)$ evolves, and its stationary solutions carry the quantised energies of bound systems.

---

Flashcards for this section are as follows:

- overview: what the Schrödinger equation does for $\Psi(x,t)$ ::@:: It governs the time evolution of the wave function $\Psi(x,t)$, the quantum analogue of Newton's second law.
- what the equation was built on ::@:: De Broglie's matter-wave postulate; Erwin Schrödinger postulated the equation in 1926 to reproduce atomic spectra.

## time-dependent equation

In one dimension the equation reads $i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi$. The left side is first order in time, the right side second order in space, which makes the equation non-relativistic. Space and time are not on equal footing. Its solutions are complex, and unlike a classical wave equation it carries an explicit factor of $i$, so wave-function phases rotate in time rather than merely shift. Any linear superposition of solutions is again a solution.

---

Flashcards for this section are as follows:

- the time-dependent Schrödinger equation for $\Psi$ in one dimension ::@:: $i\hbar\,\partial\Psi/\partial t = -\frac{\hbar^2}{2m}\,\partial^2\Psi/\partial x^2 + V(x)\Psi$.
- why the equation is called non-relativistic, given its orders in $\partial/\partial t$ and $\partial/\partial x$ ::@:: It treats time and space unequally — first order in $\partial/\partial t$, second order in $\partial^2/\partial x^2$.

## separation of variables

Try a product solution $\Psi(x,t) = \psi(x)f(t)$ and substitute. Dividing by $\psi f$ separates the equation into a time part and a space part that must each equal a constant, the energy $E$: $i\hbar\frac{1}{f}\frac{df}{dt} = E$ and $-\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V = E$. The time equation integrates immediately to $f(t) = e^{-iEt/\hbar}$, a phase that rotates without changing $|\Psi|^2$, while the space equation is the time-independent Schrödinger equation $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$, an eigenvalue problem whose allowed eigenvalues $E$ are the quantised energies.

---

Flashcards for this section are as follows:

- how separation of variables splits $\Psi(x,t) = \psi(x)f(t)$ ::@:: With $\Psi(x,t) = \psi(x)f(t)$, the time factor obeys $f = e^{-iEt/\hbar}$ and the space factor obeys the time-independent Schrödinger equation.
- what the energy eigenvalue problem for $\psi$ looks like ::@:: $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$; its allowed $E$ values are the quantised energies.

## stationary states

A separated solution $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$ is a stationary state: the phase rotates in time but $|\Psi(x,t)|^2 = |\psi(x)|^2$ does not move, so no expectation value built from $|\Psi|^2$ changes. Stationary states are energy eigenstates, the Schrödinger equation acting on $\psi$ returns $E$ times $\psi$, and any state can be expanded in them, with the phase factors keeping each component's clock. The infinite well's states $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$ with energies $E_n = n^2h^2/(8mL^2)$ in the [particle in a box](particle%20in%20a%20box.md) are the standard example.

---

Flashcards for this section are as follows:

- what makes a state stationary, given the time dependence $e^{-iEt/\hbar}$ ::@:: Its time dependence is a pure phase $e^{-iEt/\hbar}$, so $|\Psi|^2$ and every expectation value built from it are constant.
- why stationary states and energy eigenstates coincide, given $-\frac{\hbar^2}{2m}\psi'' + V\psi = E\psi$ ::@:: They coincide: a stationary state's spatial part satisfies $-\frac{\hbar^2}{2m}\psi'' + V\psi = E\psi$.

## operators and the energy relation

Mechanical quantities become operators on the wave function. Position multiplies, $\hat{x}\Psi = x\Psi$, and momentum differentiates, $\hat{p} = -i\hbar\,\partial/\partial x$.

The kinetic energy is $\hat{K} = \hat{p}^2/(2m)$, and the Hamiltonian operator is the total energy operator $\hat{H} = \hat{K} + \hat{V}$. In the position representation both are differential operators, $\hat{K} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$ and $\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)$.

The two central equations share one shape when written with $\hat{H}$. The time-dependent equation is $i\hbar\,\partial\Psi/\partial t = \hat{H}\Psi$, with the energy operator $\hat{E} = i\hbar\,\partial/\partial t$ acting as $\hat{E}\Psi = \hat{H}\Psi$. The time-independent equation is the eigenvalue problem $\hat{H}\psi = E\psi$. The classical relation $E = p^2/2m + V$ survives as this operator identity.

A product $\Psi = \psi(x)e^{-iEt/\hbar}$ solves the time-dependent equation exactly when $\psi$ solves $\hat{H}\psi = E\psi$, which is what [separation of variables](#separation%20of%20variables) carries out. The general solution is a superposition $\Psi = \sum_n c_n \psi_n e^{-iE_n t/\hbar}$, with each eigenfunction's phase rotating at its own frequency. [Stationary states](#stationary%20states) carries what that does to expectation values.

Position and momentum do not commute: $[\hat{x}, \hat{p}] = \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar$, a constant, and this commutator is the algebraic root of the uncertainty relation. Each operator's expectation value supplies the corresponding average, momentum through $\langle p \rangle = \int \Psi^*(-i\hbar\,\partial/\partial x)\Psi\,dx$, as detailed in the [expectation value](expectation%20value%20%28quantum%20mechanics%29.md) note.

---

Flashcards for this section are as follows:

- the momentum operator $\hat{p}$ ::@:: $\hat{p} = -i\hbar\,\partial/\partial x$.
- the energy operators $\hat{E}$ and $\hat{K}$ ::@:: $\hat{E} = i\hbar\,\partial/\partial t$ and $\hat{K} = -\frac{\hbar^2}{2m}\partial^2/\partial x^2$, with $E = K + V$ holding as an operator identity.
- the Hamiltonian operator $\hat{H}$ in the position representation ::@:: $\hat{H} = \hat{K} + \hat{V} = \hat{p}^2/(2m) + V(x) = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)$, with $\hat{p} = -i\hbar\,\partial/\partial x$.
- the time-dependent and time-independent Schrödinger equations as statements about $\hat{H}$ ::@:: $i\hbar\,\partial\Psi/\partial t = \hat{H}\Psi$ for the time evolution, and $\hat{H}\psi = E\psi$ as the energy eigenvalue problem.
- how an energy eigenfunction $\psi_n$ with $\hat{H}\psi_n = E_n\psi_n$ feeds the time-dependent equation ::@:: $\Psi_n = \psi_n e^{-iE_n t/\hbar}$ solves it exactly, and any superposition $\sum_n c_n \psi_n e^{-iE_n t/\hbar}$ solves it by linearity.
- the commutator $[\hat{x}, \hat{p}]$ of the position and momentum operators ::@:: $[\hat{x}, \hat{p}] = \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar$, the constant that is the algebraic root of the uncertainty relation.

## three dimensions

The same equations carry three spatial derivatives. The energy relation $E = p^2/2m + V$ holds with $p^2 = p_x^2 + p_y^2 + p_z^2$ and $\hat{p}_i = -i\hbar\,\partial/\partial i$ on each axis, so the kinetic term becomes $-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)$. The bracket is the Laplacian operator $\nabla^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2 + \partial^2/\partial z^2$, and the time-independent equation reads $-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$. The time-dependent form takes the same replacement, $i\hbar\,\partial\Psi/\partial t = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$, with $V$ allowed to depend on all three coordinates and on time.

---

Flashcards for this section are as follows:

- the time-independent Schrödinger equation in three dimensions, with the Laplacian $\nabla^2$ ::@:: $-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$, with $\nabla^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2 + \partial^2/\partial z^2$.
- how the Laplacian form of the equation follows from $E = p^2/2m + V$ ::@:: With $\hat{p}_i = -i\hbar\,\partial/\partial i$ on each axis, $p^2 = p_x^2 + p_y^2 + p_z^2$ turns the kinetic term into $-\frac{\hbar^2}{2m}\nabla^2$, so $-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$.
- the three-dimensional time-dependent Schrödinger equation in terms of $\nabla^2$ ::@:: $i\hbar\,\partial\Psi/\partial t = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$, with $V$ a function of position and time.

## momentum representation

The plane waves $e^{ikx}$ are the eigenfunctions of the momentum operator: $\hat{p}\,e^{ikx} = -i\hbar(ik)e^{ikx} = \hbar k\,e^{ikx}$, so the eigenvalue is $\hbar k$. Any $\psi$ can be rewritten as a superposition of them, $\tilde{\psi}(k) = \frac{1}{\sqrt{2\pi}}\int \psi(x)e^{-ikx}\,dx$, the Fourier transform. In that momentum representation $\hat{p}$ becomes multiplication by $\hbar k$, while $\hat{x}$ becomes $i\,\partial/\partial k$. The two representations therefore trade which operator is simple.

---

Flashcards for this section are as follows:

- the eigenfunctions of the momentum operator $\hat{p} = -i\hbar\,\partial/\partial x$ and their eigenvalues ::@:: The plane waves $e^{ikx}$: $\hat{p}\,e^{ikx} = -i\hbar(ik)e^{ikx} = \hbar k\,e^{ikx}$, so the eigenvalue is $\hbar k$.
- what rewriting $\psi$ as $\tilde{\psi}(k) = \frac{1}{\sqrt{2\pi}}\int \psi(x)e^{-ikx}\,dx$ buys ::@:: In the momentum representation $\hat{p}$ becomes multiplication by $\hbar k$ while $\hat{x}$ becomes $i\,\partial/\partial k$: the two representations trade which operator is simple.

## free-particle plane waves

A quick check on the equation takes the free case, $V = 0$, and tries the plane wave $\psi(x,t) = e^{i(kx - \omega t)}$. Substituting gives $i\hbar(-i\omega)\psi = -\frac{\hbar^2}{2m}(ik)^2\psi$, which reduces to $\hbar\omega = \hbar^2k^2/2m$. So the plane wave solves the equation when $E = \hbar\omega$ and $p = \hbar k$ satisfy the classical free relation $E = p^2/2m$, and $\omega = \hbar k^2/2m$ then carries de Broglie's $\lambda = h/p$ with $E = hf$. The check ties the equation's constants to the matter-wave relations it was built to respect.

---

Flashcards for this section are as follows:

- what substituting the plane wave $\psi = e^{i(kx - \omega t)}$ into the free Schrödinger equation with $V = 0$ reduces to ::@:: It reduces to $i\hbar(-i\omega)\psi = -\frac{\hbar^2}{2m}(ik)^2\psi$, hence $\hbar\omega = \hbar^2k^2/2m$.
- what the identifications $E = \hbar\omega$ and $p = \hbar k$ do with $\hbar\omega = \hbar^2k^2/2m$ ::@:: They give $E = p^2/2m$, the classical free relation, so the plane wave solves the free Schrödinger equation.
- what the free-plane-wave dispersion $\omega = \hbar k^2/2m$ carries for a matter wave ::@:: With $p = \hbar k$ and $E = \hbar\omega$ it reproduces de Broglie's $\lambda = h/p$ and Planck's $E = hf$.
