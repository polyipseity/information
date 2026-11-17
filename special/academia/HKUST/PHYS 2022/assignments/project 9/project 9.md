---
aliases:
  - HKUST PHYS 2022 project 9 notes
  - HKUST PHYS2022 project 9 notes
  - PHYS 2022 project 9 notes
  - PHYS2022 project 9 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_9/project_9
  - language/in/English
---

# project 9

- HKUST PHYS 2022 project 9
- parent: [project 9](index.md)

Project 9 builds an energy band out of square wells from the bottom up: one well, then two at five separations, then rows of three through ten. The levels multiply, split, and widen as the wells are added, and the widening is measured at every step. The single-well levels are the bound states of the [finite potential well](../../finite%20potential%20well.md), whose infinite-walled limit is the [particle in a box](../../particle%20in%20a%20box.md).

---

Flashcards for this section are as follows:

- what project 9 measures as the wells are added, and at what settings ::@:: The energy levels of square wells of height 20.0 eV and width 0.5 nm: the levels of one well, the split pairs of two wells at five separations, and the band widths of rows of three through ten wells.
- the trend of the energy levels as a row of identical square wells grows ::@:: Each added well contributes one level per manifold, and the manifold spreads into a band whose width grows and then saturates.

## one well

A single square well of height $V_0$ and width $L$ holds the levels a particle can occupy: discrete, each below the barrier height, each with a wave function that oscillates inside the well and decays into the barrier on both sides. Every level sits below the corresponding infinite-box level, because the wave function tunnels a little way into the barrier and feels a box wider than $L$; wider box, lower energy. Spacing grows as the levels rise, the ladder crowded at the bottom the way the infinite box's is, and the levels near the top leak furthest, so a change of width moves them most.

---

Flashcards for this section are as follows:

- how the levels of one square well of height $V_0$ and width $L$ sit ::@:: Discrete, each below $V_0$ and below the infinite box's corresponding level, each with a wave function that oscillates inside the well and decays into the barrier on both sides.
- why a finite well of width $L$ has levels below the infinite box's ::@:: The wave function tunnels a little way into the barrier on both sides, so the particle feels a box wider than $L$; wider box, lower energy.
- which levels of one square well a change of width moves most, and why ::@:: The ones near the top: they leak furthest into the barrier, so their energy depends most on how far the tails reach.
- how the level spacing of one square well changes as the levels rise towards $V_0$ ::@:: It grows: the low levels crowd near the bottom like an infinite box's, while the higher ones spread out as their wave functions leak further into the barrier.

## two wells and level splitting

Two identical wells close enough for their wave functions to overlap turn every single-well level into a pair. Take $|L\rangle$ and $|R\rangle$ for the single-well state sitting in the left and the right well, and write $S = \langle L|R\rangle$ for their overlap, $E_1 = \langle L|\hat H|L\rangle$ for the single-well level, and $H_{12} = \langle L|\hat H|R\rangle$ for the coupling. In this basis the whole problem is a $2 \times 2$ matrix equation, the generalized eigenproblem $\hat H c = E\mathbf{S}c$ with $\hat H = \begin{pmatrix} E_1 & H_{12} \\ H_{12} & E_1 \end{pmatrix}$ and the overlap matrix $\mathbf{S} = \begin{pmatrix} 1 & S \\ S & 1 \end{pmatrix}$: generalized because $|L\rangle$ and $|R\rangle$ are not orthogonal. Symmetry fixes the eigenvectors, the symmetric and antisymmetric combinations $c_\pm = (1, \pm 1)/\sqrt{2(1\pm S)}$, the [superposition](../../wave%20function.md#superposition%20and%20interference) of the two well states, and feeding them into the matrix gives the energies in closed form: $E_\pm = (E_1 \pm H_{12})/(1 \pm S)$. The symmetric state of the lowest pair keeps amplitude in both wells with no node between them, while the antisymmetric state must vanish at the midpoint, and that extra bending is kinetic energy, which is why it costs more. Two coupled pendulums split the same way, one mode swinging together and the other against, at slightly different frequencies.

The gap between the pair is the splitting. Subtracting the two energies gives $\Delta E = 2|H_{12} - E_1 S|/(1 - S^2)$, and with the weak overlap the project works in, that is $\Delta E \approx 2|t|$ with $t = H_{12} - E_1 S$ the tunnelling matrix element between the wells. The two levels sit at $E_1 \mp t$, one below the single-well value and one above it, so the factor of two is what separates them. Dropping $S$ to zero, the idealization the many-well section runs on, leaves the ordinary eigenproblem on $\begin{pmatrix} E_1 & t \\ t & E_1 \end{pmatrix}$, the $2 \times 2$ member of a family whose rows carry $E_1$ on the diagonal and $t$ between neighbours. Which combination lands on which side follows the sign of $t$, which alternates from level to level, so the gap $\Delta E$ is what every pair measures the same way.

The splitting closes fast as the wells separate. $t$ is the wave function's tail evaluated across the barrier, and that tail decays as $e^{-\kappa d}$ with $\kappa$ the decay constant in the barrier and $d$ the separation, so $\Delta E \approx 2|t|$ falls exponentially and the project's five separations trace that fall for each pair of levels. The splitting is also the coupling itself: a particle left in one well tunnels over to the other in about $\hbar/\Delta E$. In the other extreme, two wells pushed into contact merge into one well of double width, and the pair levels become that wider well's levels.

---

Flashcards for this section are as follows:

- what the level $E_1$ of one well becomes when a second identical well is brought close ::@:: A pair of levels, the symmetric and antisymmetric combinations $c_\pm = (1, \pm 1)/\sqrt{2(1\pm S)}$ at $E_\pm = (E_1 \pm H_{12})/(1 \pm S)$, split by $\Delta E$.
- the two-well problem in matrix form, in the basis $|L\rangle, |R\rangle$ ::@:: The generalized eigenproblem $\hat H c = E\mathbf{S}c$ with $\hat H = \begin{pmatrix} E_1 & H_{12} \\ H_{12} & E_1 \end{pmatrix}$ and $\mathbf{S} = \begin{pmatrix} 1 & S \\ S & 1 \end{pmatrix}$: generalized because $|L\rangle$ and $|R\rangle$ are not orthogonal.
- the two-well matrix as the $2 \times 2$ member of the many-well family ::@:: With $S$ dropped to zero it is the ordinary eigenproblem on $\begin{pmatrix} E_1 & t \\ t & E_1 \end{pmatrix}$ at $E_1 \mp t$; the $N$-well row carries the same pattern at $N \times N$.
- the splitting of a two-well level, from the overlap $S$, the coupling $H_{12}$, and the level $E_1$ ::@:: $\Delta E = 2|H_{12} - E_1 S|/(1 - S^2) \approx 2|t|$, with the tunnelling matrix element $t = H_{12} - E_1 S$.
- which member of the lowest two-well pair lies lower, and why ::@:: The symmetric one: it keeps amplitude in both wells with no node between them, while the antisymmetric state vanishes at the midpoint, and that bending is kinetic energy.
- how the splitting $\Delta E$ depends on the well separation $d$ ::@:: Exponentially down, through $\Delta E \approx 2|t|$ with $t \propto e^{-\kappa d}$: $t$ is the tail's value across the barrier, with $\kappa$ the decay constant in the barrier.
- the tunnelling time a particle in one well takes to reach the other, in terms of the splitting $\Delta E$ ::@:: About $\hbar/\Delta E = \hbar/2|t|$: the splitting is the coupling energy between the wells.
- the limit of two identical wells pushed into contact ::@:: They merge into one well of double width, carrying that well's single-particle levels.

## many wells and the band

Each of the $N$ wells holds a copy of the same single-well state; label them $|1\rangle \ldots |N\rangle$ by the well they sit in. The two-well matrix grows into its $N \times N$ member: $\hat H = \begin{pmatrix} E_1 & t & & \\ t & E_1 & t & \\ & \ddots & \ddots & t \\ & & t & E_1 \end{pmatrix}$, coupling neighbours only. The overlap is dropped here, the idealization that turns the generalized problem of the previous section into an ordinary one. An $N \times N$ matrix has exactly $N$ eigenvalues, so the count is settled before any wave is drawn: $N$ wells hand over $N$ levels, no more and no fewer.

Those $N$ levels descending from one parent level are one manifold, and the band is what the manifold becomes as the row grows. The levels pack into a fixed energy range, denser as $N$ rises, and at $N \rightarrow \infty$ they fill the whole interval $[E_1 - 2|t|, E_1 + 2|t|]$ without gaps; the filled interval is the band. So a band is not a level: it is the whole family of levels descended from one parent level $E_1$, and a finite row shows the band at finite $N$, $N$ distinct lines inside that interval closing up as wells are added. One parent level brings one band, so a row of wells carries as many bands as the single well carried levels, each sitting where its parent stood.

The eigenvectors are standing waves. A row of the matrix reads $t\psi(j-1) + E_1\psi(j) + t\psi(j+1) = E\psi(j)$ for the amplitude $\psi(j)$ on well $j$. The first and last rows are the short ones: well 1 has no well 0 to its left, well $N$ has no well $N+1$ to its right, and the missing terms are read as amplitudes on empty sites just outside the row, $\psi(0) = \psi((N+1)a) = 0$. That is the whole boundary condition: the ends of the matrix carry Dirichlet zeros one spacing beyond the last well. Inside, the standing wave $\psi(j) \propto \sin(kja)$ satisfies the recursion whenever $\sin(k(j-1)a) + \sin(k(j+1)a) = 2\cos(ka)\sin(kja)$, the addition formula, giving $E(k) = E_1 + 2t\cos(ka)$ with $a$ the well separation: the band's levels are the cosine sampled at the $N$ allowed wave numbers. The two zeros then split the work: $\sin(k\cdot 0) = 0$ every wave satisfies, while $\sin(k(N+1)a) = 0$ fixes $k_m = m\pi/((N+1)a)$ for $m = 1 \ldots N$. Nothing higher survives: $m = N+1$ puts $\sin(\pi j) = 0$ on every well, a wave too short to live on the row. So the $N$ levels sample one cosine from end to end. Setting $N = 2$ returns the two-well pair of the previous section: $k_1 = \pi/(3a)$ and $k_2 = 2\pi/(3a)$ give $E_1 + 2t\cos(\pi/3) = E_1 + t$ and $E_1 + 2t\cos(2\pi/3) = E_1 - t$, the levels at $E_1 \mp t$ and the splitting $2|t|$, exactly the two-well matrix with the overlap dropped. The band's edges are $E_1 \pm 2|t|$, where the cosine turns over, and its width, the highest level minus the lowest, is $4|t|$: twice the double-well splitting $2|t|$ at the same separation, so the project's two runs check each other against that factor of two. The cosine flattens near the edges, so the levels crowd there and stand furthest apart in the middle.

A band state belongs to no single well: its standing wave spreads the particle over the whole row, so an electron in it is bound to the row as a whole, not to any one atom. The edges come from the coupling between neighbours, not from the row's length, so the width approaches $4|t|$ quickly: added wells put levels inside the band instead of extending it.

---

Flashcards for this section are as follows:

- the number of levels a manifold takes when $N$ identical wells stand in a row ::@:: $N$: the single-well states $|1\rangle \ldots |N\rangle$ span an $N$-dimensional space, and the $N \times N$ Hamiltonian on it has exactly $N$ eigenvalues.
- the shape of the $N \times N$ Hamiltonian in the localized single-well basis ::@:: $\hat H = \begin{pmatrix} E_1 & t & & \\ t & E_1 & t & \\ & \ddots & \ddots & t \\ & & t & E_1 \end{pmatrix}$: $E_1$ on the diagonal, $t$ in the two neighbour slots of each row, zero elsewhere, so each well couples only to its neighbours.
- why the row's standing waves $\psi(j) \propto \sin(kja)$ carry the energy $E(k) = E_1 + 2t\cos(ka)$ ::@:: The matrix row $t\psi(j-1) + E_1\psi(j) + t\psi(j+1) = E\psi(j)$ is satisfied by the addition formula $\sin(k(j-1)a) + \sin(k(j+1)a) = 2\cos(ka)\sin(kja)$.
- where the boundary condition enters the $N \times N$ matrix ::@:: In the first and last rows: well 1 has no well 0 and well $N$ no well $N+1$, so the missing terms are amplitudes on empty sites, $\psi(0) = \psi((N+1)a) = 0$, Dirichlet zeros one spacing beyond the row.
- the allowed wave numbers $k_m$ of a row of $N$ coupled wells, and where they stop ::@:: $k_m = m\pi/((N+1)a)$, $m = 1 \ldots N$, from $\sin(k(N+1)a) = 0$ at the far empty site; $m = N+1$ would give $\sin(\pi j) = 0$ on every well.
- what one band is, in a row of $N$ coupled wells ::@:: The family of $N$ levels descended from one parent level $E_1$: packed between the edges $E_1 \pm 2|t|$, and at $N \rightarrow \infty$ filling that interval without gaps.
- how many bands a row of $N$ coupled wells carries ::@:: One per single-well level: each parent level $E_1$ spawns its own band, so the bands stand where the single-well levels stood.
- the difference between a level and a band in a row of $N$ coupled wells ::@:: A level is one energy of the row, an eigenvalue of the $N \times N$ matrix; a band is the whole family descended from one parent level, the $N$ levels packed into the range $E_1 \pm 2|t|$.
- what setting $N = 2$ in $E(k) = E_1 + 2t\cos(ka)$ gives ::@:: $k_1 = \pi/(3a)$ and $k_2 = 2\pi/(3a)$ at $E_1 + t$ and $E_1 - t$: the two-well pair at splitting $2|t|$, exactly the $2 \times 2$ matrix with the overlap dropped.
- the band edges and the band width of a row of coupled wells, in the coupling $t$ ::@:: Edges at $E_1 \pm 2|t|$, width $4|t|$: twice the double-well splitting $2|t|$ at the same separation $a$, which ties the two-well and many-well runs together.
- where the levels of $E(k) = E_1 + 2t\cos(ka)$ crowd ::@:: Near the edges $E_1 \pm 2|t|$, where the cosine flattens; in the middle they stand furthest apart.
- the band width of a row of $N$ coupled wells, and the direction it travels as $N$ grows ::@:: The highest level minus the lowest of the manifold; it grows with $N$ and levels off at the infinite chain's $4|t|$.
- why a band forms at all as identical wells are added ::@:: The wells couple through their overlapping wave functions, so each single level splits into one state per well, and the split states fill one band.
- what a band state looks like in real space ::@:: A standing wave spread over every well in the row: the particle belongs to the row as a whole, not to any one well.
- the limit of the band width $4|t|$ as the row of wells grows without end ::@:: The infinite chain's band, edges $E_1 \pm 2|t|$: the edges come from the neighbour-to-neighbour coupling, so added wells then place levels inside the band instead of extending it.
