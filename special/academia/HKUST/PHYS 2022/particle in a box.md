---
aliases:
  - infinite potential well
  - infinite square well
  - infinite square-well potential
  - particle in a box
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/particle_in_a_box
  - language/in/English
---

# particle in a box

The particle in a box, the infinite square well, is the simplest system with quantised energy. A particle of mass $m$ is confined to $0 < x < L$ by impenetrable walls, so $V(x) = 0$ inside and $V = \infty$ outside. Both the standing-wave argument and the Schrödinger equation give the same discrete levels $E_n = n^2h^2/(8mL^2)$ for $n = 1, 2, 3, \ldots$, and a ground-state energy that is not zero.

---

Flashcards for this section are as follows:

- overview: what the particle-in-a-box model is, and its levels $E_n$ ::@:: A particle of mass $m$ confined to $0 < x < L$ by impenetrable walls, with $V = 0$ inside and $V = \infty$ outside; its energies are quantised as $E_n = n^2h^2/(8mL^2)$.
- the ground-state energy $E_1$ of the box ::@:: $E_1 = h^2/(8mL^2)$, nonzero — the particle cannot be at rest.

## one-dimensional box

### standing-wave quantisation

Confine a wave between two fixed walls and only wavelengths that fit survive: $n(\lambda/2) = L$, so $\lambda_n = 2L/n$. A travelling electron carries momentum $p = h/\lambda_n$ and kinetic energy $E_n = p^2/2m = n^2h^2/(8mL^2)$. The same result the Schrödinger equation produces later falls out of wave optics alone, and it is exactly the de Broglie relation $\lambda = h/p$ closing the loop, the standing-wave count is the quantisation condition. The uncertainty principle reaches the same floor by a shortcut: confining the particle to $L$ forces $p \gtrsim \hbar/(2L)$, so $K \gtrsim \hbar^2/(2mL^2)$, a factor $\pi^2$ below the standing-wave level $E_1 = \pi^2\hbar^2/(2mL^2)$. Both keep the ground state above zero, and the wave count is the sharper of the two.

---

Flashcards for this section are as follows:

- the standing-wave condition between $\lambda$ and $L$ inside the box ::@:: $n(\lambda/2) = L$, hence $\lambda_n = 2L/n$ for $n = 1, 2, 3, \ldots$.
- the momentum a standing wavelength $\lambda_n = 2L/n$ carries in the box ::@:: The de Broglie relation gives $p = h/\lambda_n$, so $p_n = nh/(2L)$.
- how the energy levels $E_n$ follow from the momenta $p_n$ ::@:: $E_n = p_n^2/2m$ with $p_n = nh/(2L)$ gives $E_n = n^2h^2/(8mL^2)$.
- how the uncertainty floor $\hbar^2/(2mL^2)$ for a box of width $L$ compares with the standing-wave ground level $E_1$ ::@:: $E_1 = \pi^2\hbar^2/(2mL^2)$ sits $\pi^2$ above the floor; both keep the ground state above zero, and the standing-wave count is the sharper calculation.

<!-- check: ignore-next-line[header_style]: proper noun (eponym) -->
### Schrödinger derivation

Inside the well the time-independent Schrödinger equation is $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$. The equation $\psi'' = -k^2\psi$ is naturally solved by the complex exponentials $\psi = Ae^{ikx} + Be^{-ikx}$. Euler's formula $e^{\pm ikx} = \cos kx \pm i\sin kx$ shows that the real sine and cosine pair spans exactly the same solution space. For a real symmetric well the trigonometric basis is the more convenient one: it keeps $\psi$ real and exposes the parity of the states. The general solution $\psi = A\sin kx + B\cos kx$ with $k = \sqrt{2mE}/\hbar$ must vanish at both walls. The condition $\psi(0) = 0$ kills the cosine, leaving $B = 0$. The condition $\psi(L) = 0$ forces $\sin kL = 0$, so $kL = n\pi$ with $n = 1, 2, 3, \ldots$. The zero and negative roots give the trivial zero wave function. Forcing $\psi$ to zero across zero width makes $\psi'$ jump at each wall, the mathematical trace of an infinitely repulsive force; $V = \infty$ idealises a very steep finite wall rather than a physical potential. Substituting $k_n = n\pi/L$ back into $E = \hbar^2k^2/2m$ reproduces $E_n = n^2\pi^2\hbar^2/(2mL^2) = n^2h^2/(8mL^2)$, and normalisation over the well, $\int_0^L \sin^2(n\pi x/L)\,dx = L/2$, gives $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$. The time-dependent states follow by multiplying by the phase factor $e^{-iE_n t/\hbar}$.

---

Flashcards for this section are as follows:

- what the boundary condition $\psi(0) = 0$ does to $\psi = A\sin kx + B\cos kx$ ::@:: $\psi(0) = 0$ sets $B = 0$, killing the cosine part.
- what the boundary condition $\psi(L) = 0$ forces on $k$ ::@:: $\psi(L) = 0$ forces $\sin kL = 0$, so $k_n = n\pi/L$ with $n \geq 1$.
- the normalised ground-state wave function $\psi_1(x)$ ::@:: $\psi_1(x) = \sqrt{2/L}\,\sin(\pi x/L)$, with energy $E_1 = \pi^2\hbar^2/(2mL^2) = h^2/(8mL^2)$.
- why $n = 0$ is excluded ::@:: It gives $\psi = 0$ everywhere — no particle — and $n$ and $-n$ give the same physical state up to a sign.
- the value of the normalisation integral $\int_0^L \sin^2(n\pi x/L)\,dx$ for the box eigenfunctions ::@:: $\int_0^L \sin^2(n\pi x/L)\,dx = L/2$ for every integer $n \geq 1$.
- the normalised box eigenfunction that the integral $\int_0^L \sin^2(n\pi x/L)\,dx = L/2$ produces ::@:: $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$ on $0 < x < L$.
- what forcing $\psi$ to zero across the zero width of an infinite wall does to $\psi'$ ::@:: $\psi'$ jumps at each wall, a derivative discontinuity at the boundary.
- what the jump in $\psi'$ at an infinite wall implies physically ::@:: The discontinuity is the trace of an infinitely repulsive force; $V = \infty$ idealises a very steep finite wall rather than a physical potential.
- Euler's formula connecting $e^{\pm ikx}$ to the trigonometric functions ::@:: $e^{\pm ikx} = \cos kx \pm i\sin kx$.
- what Euler's formula $e^{\pm ikx} = \cos kx \pm i\sin kx$ implies for the solutions of $\psi'' = -k^2\psi$ ::@:: The complex exponentials $\psi = Ae^{ikx} + Be^{-ikx}$ and the real pair $\psi = A\sin kx + B\cos kx$ span the same solution space.
- why the box is solved with $\sin kx$ and $\cos kx$ rather than $e^{\pm ikx}$ ::@:: For a real symmetric well the trigonometric basis keeps $\psi$ real and exposes the parity of the states.

### probability and nodes

The probability density $|\psi_n(x)|^2 = (2/L)\sin^2(n\pi x/L)$ oscillates $n$ times across the box and has $n-1$ interior nodes where the particle is never found. The ground state is largest at the centre, $|\psi_1|^2 = (2/L)\sin^2(\pi x/L)$. Symmetry about the midpoint gives $\langle x \rangle = L/2$ for every level, and because the states are real and stationary, $\langle p \rangle = 0$, the particle is equally likely to run left as right, while $\langle p^2 \rangle = 2mE_n$ keeps a nonzero momentum spread. Higher levels pile their probability toward the walls, and in the limit of large $n$ the oscillating density averages to the uniform $1/L$ that a classical particle produces. The wave function and its density for the first three levels are drawn below, each level on its own axis. <p> ![three axes side by side, each showing psi for one level of a box: n = 1 is a single hump above the dashed zero line, n = 2 has one node at the centre of the box, n = 3 has two nodes splitting it into three lobes, and every curve starts and ends on the line at the two walls](attachments/box_state_wave_functions.svg) ![three axes side by side, each showing the square of psi for one level of a box: n = 1 is one hump centred in the box, n = 2 is two equal humps, n = 3 is three equal humps, and every set touches the dashed zero line at the walls and at the interior nodes](attachments/box_state_probability_densities.svg)

---

Flashcards for this section are as follows:

- the node count of the $n$-th level ::@:: $n-1$ interior nodes, where $|\psi_n|^2 = 0$.
- the mean position $\langle x \rangle$ and mean momentum $\langle p \rangle$ in any level ::@:: $\langle x \rangle = L/2$ by symmetry; $\langle p \rangle = 0$ because the state is real and stationary, while $\langle p^2 \rangle = 2mE_n \neq 0$.
- how the quantum density $|\psi_n|^2$ approaches the classical one ::@:: As $n$ grows, the oscillations of $|\psi_n|^2$ average to the uniform density $1/L$ — the correspondence limit.
- the level $n = 3$ of a box of width $L$: which function is drawn for it, and how many interior nodes does it have? :@: The wave function $\psi_3(x) = \sqrt{2/L}\,\sin(3\pi x/L)$, with two interior nodes at $x = L/3$ and $x = 2L/3$ splitting it into three lobes. <p> ![three axes side by side, each showing psi for one level of a box: n = 1 is a single hump above the dashed zero line, n = 2 has one node at the centre of the box, n = 3 has two nodes splitting it into three lobes, and every curve starts and ends on the line at the two walls](attachments/box_state_wave_functions.svg)

## correspondence with the vibrating string

A string fixed at both ends supports the same harmonic series: its allowed wavelengths are $\lambda_n = 2L/n$ with frequencies $f_n = nv/2L$, and each mode has $n-1$ nodes. The quantum box replaces the string's tension speed with the electron's de Broglie velocity, and energy for frequency via $E = hf$, but the mode counting is identical. Quantisation here is wave mechanics wearing atomic clothes.

---

Flashcards for this section are as follows:

- the shared structure: which $\lambda_n$ do the box and the fixed string allow? ::@:: Both allow $\lambda_n = 2L/n$ with $n-1$ interior nodes; the box adds $E_n = n^2h^2/(8mL^2)$ through $E = p^2/2m$.
- how the box's energy ladder compares with the string's frequency ladder $f_n = nv/2L$ ::@:: String frequencies are equally spaced; box energies grow as $n^2$, so the level gaps widen with $n$, though both count modes through $\lambda_n = 2L/n$.

## higher dimensions

### three-dimensional box

Confining the particle to a rectangular box of sides $L_x, L_y, L_z$ adds two more hard walls and two more quantum numbers. The potential is separable, so the wave function factorises as $\psi(x,y,z) = \psi_x(x)\psi_y(y)\psi_z(z)$ and the energy splits into three one-dimensional pieces, $E = E_x + E_y + E_z$ with $E_i = n_i^2\pi^2\hbar^2/(2mL_i^2)$. For a cubic box of side $L$ this gives $E = \frac{\pi^2\hbar^2}{2mL^2}(n_x^2 + n_y^2 + n_z^2)$ with $\psi = A\sin\frac{n_x\pi x}{L}\sin\frac{n_y\pi y}{L}\sin\frac{n_z\pi z}{L}$. Distinct quantum-number triples can share one energy, $(2,1,1)$, $(1,2,1)$, and $(1,1,2)$ all give $n_x^2+n_y^2+n_z^2 = 6$, a degeneracy produced by the box's symmetry. A perturbation that breaks the symmetry, stretching one side to $2L$ for instance, splits the shared level.

---

Flashcards for this section are as follows:

- the energies of a rectangular box $L_x, L_y, L_z$ ::@:: $E = \frac{\pi^2\hbar^2}{2m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right)$ from three separable one-dimensional factors.
- the degeneracy of the cubic box at $n_x^2+n_y^2+n_z^2 = 6$ ::@:: Three states — $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ — share $E = \frac{6\pi^2\hbar^2}{2mL^2}$; any symmetry-breaking perturbation splits them.

### confinement energy scales

The ladder runs as $E_n = n^2h^2/(8mL^2)$, so mass and width decide where quantum structure shows up. Put a macroscopic body in a macroscopic box and $E_1 = h^2/(8mL^2)$ is astronomically small. It sits at an enormous quantum number $n$, and adjacent levels stay so close together that no measurement resolves one from the next.

Shrink the box to nuclear size and the same formula lands on real nuclear energies. A proton confined to a $10^{-14}$ m box has $E_1 \approx 2$ MeV and $E_2 = 4E_1 \approx 8$ MeV, so the jump from the first excited state down to the ground state releases $\Delta E \approx 6$ MeV, a sensible size for a nuclear level spacing. An electron in the same box fares differently because $E_1 \propto 1/m$: its much smaller mass lifts $E_1$ to about $10^4$ MeV, thousands of times its own 0.511 MeV rest energy, where the nonrelativistic equation no longer applies. Even a relativistic treatment leaves energies far above those of electrons observed leaving nuclei in β decay, and the estimate indicates that electrons do not sit inside nuclei.

---

Flashcards for this section are as follows:

- what the box formula $E_n = n^2h^2/(8mL^2)$ says about mass and width ::@:: Every level falls as $m$ or $L^2$ grows, so confinement energies are largest for light particles in small boxes.
- what the box model with $E_1 = h^2/(8mL^2)$ predicts for a macroscopic object ::@:: $E_1 = h^2/(8mL^2)$ is astronomically small, the object sits at a huge $n$, and adjacent levels are too close together to resolve.
- the ground-state and first-excited energies of a proton in a $10^{-14}$ m box ::@:: $E_1 \approx 2$ MeV and $E_2 = 4E_1 \approx 8$ MeV, so the transition energy is $\Delta E \approx 6$ MeV.
- what the same $10^{-14}$ m box gives an electron ::@:: $E_1 \propto 1/m$ puts it near $10^4$ MeV, thousands of times the 0.511 MeV rest energy, where the nonrelativistic treatment fails and the estimate rules electrons out of nuclei.

### beyond one dimension

The three-dimensional box is the base for further problems: relaxing the walls to a finite depth $V_0$ lowers every level and binds only finitely many, as the [finite potential well](finite%20potential%20well.md) sets out. A particle that can tunnel through a finite barrier instead of bouncing off an infinite one is the [quantum tunnelling](quantum%20tunnelling.md) problem.

---

Flashcards for this section are as follows:

- what relaxing the infinite walls of the box to a finite depth $V_0$ does to the levels ::@:: Every level drops below its infinite-well value and only finitely many bound states remain — the finite potential well.
- the two problems the three-dimensional box leads into in this course ::@:: Relaxing the walls to finite depth gives the finite potential well; a finite barrier instead of an infinite wall gives quantum tunnelling.
