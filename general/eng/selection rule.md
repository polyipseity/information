---
aliases:
  - selection rule
tags:
  - flashcard/active/general/eng/selection_rule
  - language/in/English
---

# selection rule

In {@{[physics](physics.md) and [chemistry](chemistry.md)}@}, {@{a __selection rule__, or __transition rule__}@}, formally {@{constrains the possible transitions of a system from one [quantum state](quantum%20state.md) to another}@}. {@{Selection rules}@} have been derived for {@{[electromagnetic](electromagnetic.md) transitions}@} in {@{[molecules](molecule.md), in [atoms](atom.md), in [atomic nuclei](atomic%20nucleus.md)}@}, and so on. {@{The selection rules may differ}@} according to {@{the technique used to observe the transition}@}. {@{The selection rule also plays a role}@} in {@{[chemical reactions](chemical%20reaction.md)}@}, where some are {@{formally [spin-forbidden reactions](spin-forbidden%20reactions.md)}@}, that is, reactions where {@{the spin state changes at least once from [reactants](reagent.md) to [products](product%20(chemistry).md)}@}.

In the following, {@{mainly atomic and molecular transitions}@} are {@{considered}@}.

## overview

In {@{[quantum mechanics](quantum%20mechanics.md)}@} {@{the basis for a spectroscopic selection rule}@} is {@{the value of the _transition moment integral_}@}<sup>[\[1\]](#^ref-1)</sup> {@{$$m_{1,2}=\int \psi _{1}^{*}\,\mu \,\psi _{2}\,\mathrm {d} \tau ,$$}@} where {@{$\psi _{1}$ and $\psi _{2}$}@} are {@{the [wave functions](wave%20function.md) of the two states, "state 1" and "state 2", involved in the transition}@}, and _μ_ is {@{the [transition moment operator](transition%20dipole%20moment.md)}@}. This integral represents {@{the [propagator](propagator.md) \(and thus the probability\)}@} of {@{the transition between states 1 and 2}@}; if {@{the value of this integral is _zero_}@} then {@{the transition is "[forbidden](#anchor%20forbidden%20trans)"}@}.

In {@{practice, to determine a selection rule}@} {@{the integral itself does not need to be calculated}@}: It is {@{sufficient to determine the [symmetry](symmetry.md) of the _transition moment function_ $\psi _{1}^{*}\,\mu \,\psi _{2}$}@}. If {@{the transition moment function is symmetric over all}@} of {@{the totally symmetric representation of the [point group](point%20group.md) to which the atom or molecule belongs}@}, then {@{the integral's value is \(in general\) _not_ zero}@} and {@{the transition _is_ allowed}@}. Otherwise, {@{the transition is "[forbidden](#anchor%20forbidden%20trans)"}@}.

{@{The transition moment integral is zero}@} if {@{the _transition moment function_, $\psi _{1}^{*}\,\mu \,\psi _{2}$}@}, is {@{anti-symmetric or [odd](odd%20functions.md#odd%20functions), i.e. $y(x)=-y(-x)$ holds}@}. {@{The symmetry of the transition moment function}@} is {@{the [direct product](direct%20product%20of%20groups.md) of the [parities](even%20and%20odd%20functions.md) of its three components}@}. {@{The symmetry characteristics of each component}@} can be obtained from {@{standard [character tables](character%20tables.md)}@}. {@{Rules for obtaining the symmetries of a direct product}@} can be found in {@{texts on character tables}@}.<sup>[\[2\]](#^ref-2)</sup>

<!-- markdownlint-disable-next-line MD036 -->
__Symmetry characteristics of transition moment operator<sup>[\[2\]](#^ref-2)</sup>__

|       Transition type       | _μ_ transforms as                                         | Context                                                        |
| :-------------------------: | --------------------------------------------------------- | -------------------------------------------------------------- |
|     __Electric dipole__     | _x, y, z_                                                 | Optical spectra                                                |
|   __Electric quadrupole__   | _x<sup>2</sup>, y<sup>2</sup>, z<sup>2</sup>, xy, xz, yz_ | Constraint _x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup>_ = 0 |
| __Electric polarizability__ | _x<sup>2</sup>, y<sup>2</sup>, z<sup>2</sup>, xy, xz, yz_ | Raman spectra                                                  |
|     __Magnetic dipole__     | _R_<sub>x</sub>, _R_<sub>y</sub>, _R_<sub>z</sub>         | Optical spectra \(weak\)                                       |

> __flashcards__
>
> - __Electric dipole__
>     - __Electric dipole__ / _μ_ transforms as::@:: _x, y, z_
>     - __Electric dipole__ / Context ::@:: Optical spectra
> - __Electric quadrupole__
>     - __Electric quadrupole__ / _μ_ transforms as ::@:: _x<sup>2</sup>, y<sup>2</sup>, z<sup>2</sup>, xy, xz, yz_
>     - __Electric quadrupole__ / Context ::@:: Constraint _x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup>_ = 0
> - __Electric polarizability__
>     - __Electric polarizability__ / _μ_ transforms as ::@:: _x<sup>2</sup>, y<sup>2</sup>,z<sup>2</sup>, xy, xz, yz_
>     - __Electric polarizability__ / Context ::@:: Raman spectra
> - __Magnetic dipole__
>     - __Magnetic dipole__ / _μ_ transforms as::@:: _R_<sub>x</sub>, _R_<sub>y</sub>, _R_<sub>z</sub>
>     - __Magnetic dipole__ / Context ::@:: Optical spectra \(weak\)

## examples

### electronic spectra

{@{The [Laporte rule](Laporte%20rule.md)}@} is {@{a selection rule formally stated}@} as follows: In {@{a [centrosymmetric](centrosymmetric.md) environment}@}, {@{transitions between like [atomic orbitals](atomic%20orbitals.md)}@} such as {@{_s_–_s_, _p_–_p_, _d_–_d_, or _f_–_f_}@}, {@{transitions are forbidden}@}. {@{The Laporte rule \(law\)}@} applies to {@{[electric dipole transitions](electric%20dipole%20transition.md)}@}, so {@{the operator (annotation: given by $\boldsymbol{\mu} = -e \sum_i \mathbf{r}_i$)}@} has {@{_u_ symmetry \(meaning _ungerade_, odd\)}@}.<sup>[\[3\]](#^ref-3)</sup> {@{_p_ orbitals}@} also have {@{_u_ symmetry}@}, so {@{the symmetry of the transition moment function}@} is given by {@{the product \(formally, the product is taken in the [group](group%20(mathematics).md)\)}@} {@{_u_<!-- markdown separator -->×<!-- markdown separator -->_u_<!-- markdown separator -->×<!-- markdown separator -->_u_}@}, which has {@{_u_ symmetry}@}. The transitions are {@{therefore forbidden}@}. Likewise, {@{_d_ orbitals}@} have {@{_g_ symmetry \(meaning _gerade_, even\)}@}, so {@{the triple product _g_<!-- markdown separator -->×<!-- markdown separator -->_u_<!-- markdown separator -->×<!-- markdown separator -->_g_}@} also has {@{_u_ symmetry and the transition is forbidden}@}.<sup>[\[4\]](#^ref-4)</sup>

{@{The wave function of a single electron}@} is {@{the product of a space-dependent wave function and a [spin](spin%20(physics).md) wave function}@}. Spin is {@{directional}@} and can be said to have {@{odd [parity](parity%20(physics).md)}@}. It follows that {@{transitions in which the spin "direction" changes are forbidden}@}. In formal terms, {@{only states with the same total [spin quantum number](spin%20quantum%20number.md)}@} are {@{"spin-allowed"}@}.<sup>[\[5\]](#^ref-5)</sup> (annotation: {@{The spin transition operator}@} is {@{the total spin operator $\hat{\mathbf{S} }$}@}, requiring {@{$\Delta S = 0$ for spin-allowed transitions}@}.) In {@{[crystal field theory](crystal%20field%20theory.md)}@}, {@{_d_–_d_ transitions that are spin-forbidden}@} are {@{much weaker than spin-allowed transitions}@}. Both can be {@{observed, in spite of the Laporte rule}@}, because {@{the actual transitions are coupled to vibrations}@} that are {@{anti-symmetric and have the same symmetry as the dipole moment operator}@}.<sup>[\[6\]](#^ref-6)</sup> (annotation: {@{Asymmetric vibrational modes with odd parity}@} couple to {@{the electronic wavefunctions}@} such that {@{the direct product representation $\Gamma_{\text{elec} } \otimes \Gamma_{\text{vib} }$}@} transforms {@{identically to the odd-parity electric dipole operator $\boldsymbol{\mu}$}@}, resulting in {@{a non-vanishing transition matrix element}@} {@{$\langle \psi_f \psi_{\text{vib}, f} \vert{} \boldsymbol{\mu} \vert{} \psi_i \psi_{\text{vib}, i} \rangle \neq 0$}@} that bypasses {@{the Laporte rule to permit otherwise forbidden $d-d$ transitions}@}.)

### vibrational spectra

- Main articles: ::@:: [infrared spectroscopy](infrared%20spectroscopy.md) and [Raman spectroscopy](Raman%20spectroscopy.md)

In {@{vibrational spectroscopy}@}, {@{transitions are observed}@} between {@{different [vibrational states](molecular%20vibration.md)}@}. In {@{a fundamental vibration}@}, {@{the molecule is excited}@} from its {@{[ground state](ground%20state.md) \(_v_ = 0\) to the first excited state \(_v_ = 1\)}@}. {@{The symmetry of the ground-state wave function}@} is {@{the same as that of the molecule}@}. It is, therefore, {@{a basis for the totally symmetric representation}@} in {@{the [point group](point%20group.md) of the molecule}@}. It follows that, for {@{a vibrational transition to be allowed}@}, {@{the symmetry of the excited state wave function}@} must be {@{the same as the symmetry of the transition moment operator}@}.<sup>[\[7\]](#^ref-7)</sup>

In {@{[infrared spectroscopy](infrared%20spectroscopy.md)}@}, {@{the transition moment operator}@} transforms as {@{either _x_ and/or _y_ and/or _z_}@}. {@{The excited state wave function}@} must also {@{transform as at least one of these vectors}@}. In {@{[Raman spectroscopy](Raman%20spectroscopy.md)}@}, the operator transforms as {@{one of the second-order terms in the right-most column of the [character](character%20theory.md) table}@}, below.<sup>[\[2\]](#^ref-2)</sup>

<!-- markdownlint-disable-next-line MD036 -->
__Character table for the _T<sub>d</sub>_ point group__

|                   |  E  | 8 _C_<sub>3</sub> | 3 _C_<sub>2</sub> | 6 _S_<sub>4</sub> | 6 _σ<sub>d</sub>_ |                                                       |                                                                                              |
| :---------------: | :-: | :---------------: | :---------------: | :---------------: | :---------------: | :---------------------------------------------------: | :------------------------------------------------------------------------------------------: |
| __A<sub>1</sub>__ |  1  |         1         |         1         |         1         |         1         |                                                       |                     _x_<sup>2</sup> + _y_<sup>2</sup> + _z_<sup>2</sup>                      |
| __A<sub>2</sub>__ |  1  |         1         |         1         |         −1        |         −1        |                                                       |                                                                                              |
|       __E__       |  2  |         −1        |         2         |         0         |         0         |                                                       | \(2 _z_<sup>2</sup> − _x_<sup>2</sup> − _y_<sup>2</sup>, _x_<sup>2</sup> − _y_<sup>2</sup>\) |
| __T<sub>1</sub>__ |  3  |         0         |         −1        |         1         |         −1        | \(_R<sub>x</sub>_, _R<sub>y</sub>_, _R<sub>z</sub>_\) |                                                                                              |
| __T<sub>2</sub>__ |  3  |         0         |         −1        |         −1        |         1         |                   \(_x_, _y_, _z_\)                   |                                     \(_xy_, _xz_, _yz_\)                                     |

> __flashcards__
>
> - __methane, CH<sub>4</sub>__
>     - methane, CH<sub>4</sub> / point group ::@:: _T_<sub>d</sub>, order 24: _E_, eight _C_<sub>3</sub>, three _C_<sub>2</sub>, six _S_<sub>4</sub> and six _σ_<sub>d</sub>, with the carbon at the centre and the four hydrogens at the corners of a regular tetrahedron
>     - methane, CH<sub>4</sub> / the operation it lacks ::@:: inversion, since inverting each hydrogen through the carbon lands on an empty point, so the molecule is not left unchanged
>     - methane, CH<sub>4</sub> / the four _C_<sub>3</sub> axes ::@:: each line runs through one hydrogen, the carbon, and the middle of the face formed by the other three hydrogens; a 120° turn cycles those three and fixes the first. Four axes turn two ways each, giving the 8 operations
>     - methane, CH<sub>4</sub> / the three _C_<sub>2</sub> axes ::@:: each runs through the carbon and the midpoints of two opposite H–H edges, edges that share no hydrogen; a half turn exchanges the hydrogen at either end of each of those two edges, pairing all four
>     - methane, CH<sub>4</sub> / the three _S_<sub>4</sub> axes ::@:: they lie on the three _C_<sub>2</sub> lines; the operation turns 90° about the line, then reflects in the plane through the carbon perpendicular to it. Three axes turn two ways each, giving the 6 operations
>     - methane, CH<sub>4</sub> / the six _σ_<sub>d</sub> planes ::@:: each plane contains the carbon and two of the four hydrogens, so both of their C–H bonds lie flat inside it, while the other two hydrogens sit on opposite sides as mirror images of each other; a pair of hydrogens forces one plane, and four hydrogens form six pairs
> - __the table__
>     - _T_<sub>d</sub> character table / a number inside the grid ::@:: a character, the trace of the matrix that the class applies to the basis of that row
>     - _T_<sub>d</sub> character table / the small number in a column head ::@:: how many operations share that class, as the 8 of 8 _C_<sub>3</sub>; the _E_ column carries none because the identity stands alone
>     - _T_<sub>d</sub> character table / what a character of 0 means ::@:: the operation mixes the basis functions among themselves so that nothing returns as itself, and the trace cancels to zero
>     - _T_<sub>d</sub> character table / what characters of 1 and −1 mean ::@:: the basis function comes back unchanged, or with its sign flipped
>     - _T_<sub>d</sub> character table / why one column per class instead of per operation ::@:: conjugate operations are related by turning the whole molecule, so every representation gives them the same trace; the 24 operations fit in five columns without losing anything
>     - _T_<sub>d</sub> character table / the two rightmost columns ::@:: the functions that carry each row: $x, y, z$ and $R_x, R_y, R_z$ for translations and rotations, then the quadratic products; a blank means no function of that kind belongs to the row
> - __the row labels__
>     - _T_<sub>d</sub> row label $A_1$ / how to read it ::@:: $A$ is one-dimensional and symmetric under the principal _C_<sub>3</sub>, and the 1 adds symmetry under _S_<sub>4</sub>
>     - _T_<sub>d</sub> row label $A_2$ / how to read it ::@:: $A$ is one-dimensional and symmetric under _C_<sub>3</sub>, and the 2 adds antisymmetry under _S_<sub>4</sub>
>     - _T_<sub>d</sub> row label $E$ / how to read it ::@:: $E$ is two-dimensional, a degenerate pair; this group has only one pair, so the label needs no subscript
>     - _T_<sub>d</sub> row label $T_1$ / how to read it ::@:: $T$ is three-dimensional, and the 1 adds symmetry under _S_<sub>4</sub>
>     - _T_<sub>d</sub> row label $T_2$ / how to read it ::@:: $T$ is three-dimensional, and the 2 adds antisymmetry under _S_<sub>4</sub>
> - __the rows__
>     - _T_<sub>d</sub> table, row $A_1$ ::@:: 1, 1, 1, 1, 1, one per class. Its basis $x^2 + y^2 + z^2$ is the squared distance from the carbon. A rotation carries the hydrogens round, a reflection mirrors them, and neither changes a distance, so the single function comes back unchanged in every class and the trace stays 1
>         - _T_<sub>d</sub> table, row $A_1$ / extra columns ::@:: only $x^2 + y^2 + z^2$, the one quadratic combination that survives every operation
>     - _T_<sub>d</sub> table, row $A_2$ ::@:: 1, 1, 1, −1, −1. Its basis $xyz$ behaves like the signed volume of the box that the three coordinates span. A proper rotation, _C_<sub>3</sub> or _C_<sub>2</sub>, turns that box without flipping it, so both return +1. The improper operations _S_<sub>4</sub> and _σ_<sub>d</sub> reverse its orientation, so both return −1
>         - _T_<sub>d</sub> table, row $A_2$ / extra columns ::@:: both blank, since $xyz$ is cubic and no coordinate or quadratic product is symmetric under _C_<sub>3</sub> while flipping under _σ_<sub>d</sub>
>     - _T_<sub>d</sub> table, row $E$ ::@:: 2, −1, 2, 0, 0. The basis is the pair $u = 2z^2 - x^2 - y^2$ and $v = x^2 - y^2$, and every trace adds up what the two partners do. _E_ and _C_<sub>2</sub> send both back untouched, $1 + 1 = 2$; a half turn only reverses the signs of $x$ and $y$, and both squares ignore that. _C_<sub>3</sub> mixes $u$ and $v$ into each other, with the trace of a 120° turn in a plane, $2\cos 120° = -1$. The mirror in _σ_<sub>d</sub> swaps $x$ and $y$, which leaves $u$ alone and turns $v$ into $-v$, so $1 - 1 = 0$; the same reflection sits inside _S_<sub>4</sub> and gives 0 again
>         - _T_<sub>d</sub> table, row $E$ / extra columns ::@:: $2z^2 - x^2 - y^2$ and $x^2 - y^2$, the two independent quadratic combinations with zero trace, which is why a mode in this row is Raman active
>     - _T_<sub>d</sub> table, row $T_1$ ::@:: 3, 0, −1, 1, −1. The basis is $R_x$, $R_y$, $R_z$, the three components of a rotation. _E_ gives 3. _C_<sub>3</sub> cycles the three axes, and a cycle has trace 0. _C_<sub>2</sub> keeps the component along its own axis and reverses the other two, $1 - 1 - 1 = -1$. _S_<sub>4</sub> and _σ_<sub>d</sub> give +1 and −1, which are the _T_<sub>2</sub> values with the sign flipped, because a rotation is an axial vector and carries the extra sign of $xyz$ under every improper operation
>         - _T_<sub>d</sub> table, row $T_1$ / why the basis matters ::@:: $R_x$, $R_y$, $R_z$ are the components of a rotation, so a mode in this row couples to a magnetic dipole
>     - _T_<sub>d</sub> table, row $T_2$ ::@:: 3, 0, −1, −1, 1. The basis is $x, y, z$ taken along the three _C_<sub>2</sub> axes. _E_ gives 3. _C_<sub>3</sub> cycles the three coordinates and a cycle has trace 0. _C_<sub>2</sub> keeps the coordinate along its own axis and reverses the other two, $1 - 1 - 1 = -1$. _S_<sub>4</sub> reverses the coordinate along its axis and swaps the other two, $−1 + 0 + 0 = -1$. _σ_<sub>d</sub> swaps two coordinates and keeps the third, $0 + 0 + 1 = 1$. Choose the axes inside the mirror plane instead and only one coordinate is reversed, $1 + 1 - 1 = 1$; the trace does not care which frame you use
>         - _T_<sub>d</sub> table, row $T_2$ / extra columns ::@:: $x, y, z$ for translations and $xy, xz, yz$ for the quadratic products, so a mode in this row is infrared and Raman active
> - __the great orthogonality theorem__
>     - _T_<sub>d</sub> table, the great orthogonality theorem / statement ::@:: for two rows $i$ and $j$, the sum of class size times $\chi_i$ times $\chi_j$ over all classes gives 24 when $i = j$ and 0 when they differ
>     - _T_<sub>d</sub> table, the great orthogonality theorem / why the rows must be independent ::@:: a group with five classes has exactly five irreducible representations, so no row can be built out of the others
>     - _T_<sub>d</sub> table, the great orthogonality theorem / checking it on the table ::@:: row $A_1$ against itself gives $1 + 8 + 3 + 6 + 6 = 24$, the group order, and $A_1$ against $E$ gives $2 - 8 + 6 + 0 + 0 = 0$, so the rows come out normalised and mutually orthogonal
> - __using the table on methane__
>     - methane, CH<sub>4</sub> / what the table is used for ::@:: to decide which vibrations absorb infrared light and which scatter Raman light, without writing any wave functions: turn the displacements into rows, drop the translation and rotation rows, then keep the rows that carry a linear or a quadratic function
>     - methane, CH<sub>4</sub> / step 1, the character of all 15 displacements in each class ::@:: count the atoms the class leaves in place and multiply by $1 + 2\cos\theta$, using $-1 + 2\cos\theta$ for the improper classes. _E_ keeps 5 atoms at 0°, _C_<sub>3</sub> keeps 2 at 120°, _C_<sub>2</sub> keeps 1 at 180°, _S_<sub>4</sub> keeps 1 at 90° and _σ_<sub>d</sub> keeps 3 at 0°, so the row reads 15, 0, −1, −1, 3 in the table's column order _E_, _C_<sub>3</sub>, _C_<sub>2</sub>, _S_<sub>4</sub>, _σ_<sub>d</sub>. This row is called $\chi_{3N}$, and it is not yet a table row
>     - methane, CH<sub>4</sub> / step 2, turning that row into table rows ::@:: take a table row such as $T_2$ and read its numbers off the same five classes, here 3, 0, −1, −1, 1. Pair each of them with the step 1 number in the same column and with the class size from the column head, giving $1 \times 15 \times 3$, $8 \times 0 \times 0$, $3 \times (-1) \times (-1)$, $6 \times (-1) \times (-1)$ and $6 \times 3 \times 1$. The pairs add to 72, and $72/24 = 3$, so $T_2$ appears three times. Running the same sum once per row gives $A_1 + E + T_1 + 3T_2$ for the 15 displacements
>     - methane, CH<sub>4</sub> / step 3, dropping translation and rotation to leave the vibrations ::@:: $T_2$ covers the three translations $x, y, z$ and $T_1$ covers the three rotations $R_x, R_y, R_z$, so what remains is $A_1 + E + 2T_2$, which counts $1 + 2 + 6 = 9$ vibrations
>     - methane, CH<sub>4</sub> / step 4, which vibrations absorb infrared light ::@:: absorption needs the dipole components $x$, $y$ or $z$, so the row must carry one of them. Only $T_2$ does, so the two $T_2$ vibrations give infrared lines and $A_1$ and $E$ give none
>     - methane, CH<sub>4</sub> / step 4, which vibrations scatter Raman light ::@:: scattering needs a quadratic component, so the row must carry one: $x^2 + y^2 + z^2$ sits in $A_1$, $2z^2 - x^2 - y^2$ and $x^2 - y^2$ sit in $E$, and $xy$, $xz$, $yz$ sit in $T_2$. Every vibration carries one, so all four give Raman lines
>     - methane, CH<sub>4</sub> / the answer the four steps give ::@:: four Raman lines and two infrared lines. $A_1$ and $E$ are Raman only, the two $T_2$ vibrations are both Raman and infrared, and $T_1$ never belongs to a vibration at all

{@{The molecule methane, CH<sub>4</sub>}@}, may be used as {@{an example to illustrate the application of these principles}@}. {@{The molecule}@} is {@{[tetrahedral](tetrahedral.md) and has _T<sub>d</sub>_ symmetry}@}. {@{The vibrations of methane}@} span {@{the representations A<sub>1</sub> + E + 2T<sub>2</sub>}@}.<sup>[\[8\]](#^ref-8)</sup> {@{Examination of the character table}@} shows that all {@{four vibrations are Raman-active}@}, but only {@{the T<sub>2</sub> vibrations can be seen in the infrared spectrum}@}.<sup>[\[9\]](#^ref-9)</sup>

In {@{the [harmonic approximation](quantum%20harmonic%20oscillator.md)}@}, it can be shown that {@{[overtones](overtone%20band.md) are forbidden in both infrared and Raman spectra}@}. However, when {@{[anharmonicity](anharmonicity.md) is taken into account}@}, the transitions are {@{weakly allowed}@}.<sup>[\[10\]](#^ref-10)</sup>

In {@{Raman and infrared spectroscopy}@}, {@{the selection rules}@} predict {@{certain vibrational modes to have zero intensities in the Raman and/or the IR}@}.<sup>[\[11\]](#^ref-11)</sup> {@{Displacements from the ideal structure}@} can result in {@{relaxation of the selection rules and appearance of these unexpected phonon modes in the spectra}@}. Therefore, {@{the appearance of new modes in the spectra}@} can be {@{a useful indicator of symmetry breakdown}@}.<sup>[\[12\]](#^ref-12)</sup><sup>[\[13\]](#^ref-13)</sup>

### rotational spectra

- Main article: ::@:: [Rigid rotor](rigid%20rotor.md)

{@{The [selection rule](rigid%20rotor.md#selection%20rules) for rotational transitions}@}, derived from {@{the symmetries of the rotational wave functions in a rigid rotor}@}, is {@{Δ<!-- markdown separator -->_J_ = ±1}@}, where _J_ is {@{a rotational quantum number}@}.<sup>[\[14\]](#^ref-14)</sup>

### coupled transitions

|                                                                                                                          [Coupling in science](coupling%20(physics).md)                                                                                                                         |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                        Classical coupling                                                                                                                                       |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                            - [Rotational–vibrational coupling](rotational–vibrational%20coupling.md)                                                                                                            |
|                                                                                                                                         Quantum coupling                                                                                                                                        |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| - [Angular momentum coupling](angular%20momentum%20coupling.md) <br/> - [J-coupling](J-coupling.md) <br/> - [Vibronic coupling](vibronic%20coupling.md) <br/> - [Ro–vibrational spectroscopy](rotational–vibrational%20spectroscopy.md) <br/> - [Rovibronic coupling](rovibronic%20coupling.md) |
|                 <!-- - [v](https://en.wikipedia.org/wiki/Template:Coupling%20in%20science) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Coupling%20in%20science) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ACoupling%20in%20science) -->                |

> {@{![An IR rotational/vibrational spectrum of HCl gas.](../../archives/Wikimedia%20Commons/HCl%20rotiational%20spectrum.jpg)}@}
>
> {@{The infrared spectrum}@} of {@{[HCl](HCl.md) gas}@}

There are many {@{types of coupled transition such as are observed in [vibration–rotation](rotational–vibrational%20coupling.md) spectra}@}. {@{The excited-state wave function}@} is {@{the product of two wave functions such as vibrational and rotational}@}. {@{The general principle}@} is that {@{the symmetry of the excited state}@} is obtained as {@{the direct product of the symmetries of the component wave functions}@}.<sup>[\[15\]](#^ref-15)</sup> In {@{[rovibronic](rovibronic%20coupling.md) transitions}@}, {@{the excited states}@} involve {@{three wave functions}@}.

{@{The infrared spectrum of [hydrogen chloride](hydrogen%20chloride.md) gas}@} shows {@{rotational fine structure superimposed on the vibrational spectrum}@}. This is typical of {@{the infrared spectra of heteronuclear diatomic molecules}@}. It shows {@{the so-called _P_ and _R_ branches}@}. {@{The _Q_ branch}@}, located at {@{the vibration frequency}@}, is {@{absent}@}. {@{[Symmetric top](rotational%20spectroscopy.md) molecules}@} display {@{the _Q_ branch}@}. This follows from {@{the application of selection rules}@}.<sup>[\[16\]](#^ref-16)</sup>

{@{[Resonance Raman spectroscopy](resonance%20Raman%20spectroscopy.md)}@} involves {@{a kind of vibronic coupling}@}. It results in {@{much-increased intensity of fundamental and overtone transitions}@} as the vibrations {@{"steal" intensity from an allowed electronic transition}@}.<sup>[\[17\]](#^ref-17)</sup> In {@{spite of appearances}@}, {@{the selection rules}@} are {@{the same as in Raman spectroscopy}@}.<sup>[\[18\]](#^ref-18)</sup>

### angular momentum

- See also: ::@:: [angular momentum coupling](angular%20momentum%20coupling.md)

In general, {@{electric \(charge\) radiation or magnetic \(current, magnetic moment\) radiation}@} can be classified into {@{[multipoles](multipole%20moments.md) E<!-- markdown separator -->_λ_ \(electric\) or M<!-- markdown separator -->_λ_ \(magnetic\) of order 2<sup>_λ_</sup>}@}, e.g., {@{E1 for electric [dipole](dipole.md), E2 for [quadrupole](quadrupole.md), or E3 for octupole}@}. In {@{transitions where the change in angular momentum between the initial and final states}@} makes {@{several multipole radiations possible}@}, usually {@{the lowest-order multipoles are overwhelmingly more likely}@}, and dominate {@{the transition}@}.<sup>[\[19\]](#^ref-19)</sup>

{@{The emitted particle}@} carries {@{away angular momentum, with quantum number _λ_}@}, which for {@{the photon must be at least 1}@}, since it is {@{a vector particle \(i.e., it has [_J_](total%20angular%20momentum%20quantum%20number.md)<sup>[_P_](parity%20(physics).md)</sup> = 1<sup>−</sup>\)}@}. Thus, there is no {@{radiation from E0 \(electric monopoles\) or M0 \([magnetic monopoles](magnetic%20monopole.md), which do not seem to exist\)}@}.

Since {@{the total angular momentum}@} has to be {@{conserved during the transition}@}, we have that {@{$$\mathbf {J} _{\text{i} }=\mathbf {J} _{\text{f} }+{\boldsymbol {\lambda } },$$}@} where {@{$\|{\boldsymbol {\lambda } }\|={\sqrt {\lambda (\lambda +1)} }\,\hbar$}@}, and its {@{_z_ projection is given by $\lambda _{z}=\mu \hbar ;$}@} and where {@{$\mathbf {J} _{\text{i} }$ and $\mathbf {J} _{\text{f} }$}@} are, respectively, {@{the initial and final angular momenta of the atom}@}. {@{The corresponding quantum numbers _λ_ and _μ_ \(_z_-axis angular momentum\)}@} must satisfy {@{$$|J_{\text{i} }-J_{\text{f} }|\leq \lambda \leq J_{\text{i} }+J_{\text{f} }$$}@} and {@{$$\mu =M_{\text{i} }-M_{\text{f} }.$$}@} {@{Parity}@} is {@{also preserved}@}. For {@{electric multipole transitions}@} {@{$$\pi (\mathrm {E} \lambda )=\pi _{\text{i} }\pi _{\text{f} }=(-1)^{\lambda },$$}@} while for {@{magnetic multipoles}@} {@{$$\pi (\mathrm {M} \lambda )=\pi _{\text{i} }\pi _{\text{f} }=(-1)^{\lambda +1}.$$}@} Thus, {@{parity does not change}@} for {@{E-even or M-odd multipoles}@}, while it {@{changes for E-odd or M-even multipoles}@}.

<a id="anchor forbidden trans"></a> These considerations generate {@{different sets of transitions rules depending on the multipole order and type}@}. {@{The expression _[forbidden transitions](forbidden%20transition.md)_}@} is often {@{used, but this does not mean that these transitions _cannot_ occur}@}, only that {@{they are _electric-dipole-forbidden_}@}. These transitions are {@{perfectly possible; they merely occur at a lower rate}@}. If {@{the rate for an E1 transition is non-zero}@}, {@{the transition is said to be permitted}@}; if {@{it is zero}@}, then {@{M1, E2, etc. transitions can still produce radiation, albeit with much lower transitions rates}@}. {@{The transition rate decreases}@} by {@{a factor of about 1000 from one multipole to the next one}@}, so {@{the lowest multipole transitions are most likely to occur}@}.<sup>[\[20\]](#^ref-20)</sup>

{@{Semi-forbidden transitions \(resulting in so-called intercombination lines\)}@} are {@{electric dipole \(E1\) transitions}@} for which {@{the selection rule that the spin does not change is violated}@}. This is a result of {@{the failure of [LS coupling](LS%20coupling.md#LS%20coupling)}@}.

#### summary table

{@{$J=L+S$}@} is {@{the total angular momentum}@}, $L$ is {@{the [azimuthal quantum number](azimuthal%20quantum%20number.md)}@}, $S$ is {@{the [spin quantum number](spin%20quantum%20number.md)}@}, and $M_{J}$ is {@{the [secondary total angular momentum quantum number](total%20angular%20momentum%20quantum%20number.md)}@}. Which transitions are {@{allowed is based on the [hydrogen-like atom](hydrogen-like%20atom.md)}@}. {@{The symbol $\not \leftrightarrow$}@} is used to indicate {@{a forbidden transition}@}.

|    Allowed transitions    |     \<    |                                        Electric dipole \(E1\)                                       |                  Magnetic dipole \(M1\)                 |                                                                                   Electric quadrupole \(E2\)                                                                                   |                                        Magnetic quadrupole \(M2\)                                       |                                                                                                                         Electric octupole \(E3\)                                                                                                                        |                                             Magnetic octupole \(M3\)                                            |
| :-----------------------: | :-------: | :-------------------------------------------------------------------------------------------------: | :-----------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
|     __Rigorous rules__    | __\(1\)__ |            $${\begin{matrix}\Delta J=0,\pm 1\\(J=0\not \leftrightarrow 0)\end{matrix} }$$           |                            \<                           | $${\begin{matrix}\Delta J=0,\pm 1,\pm 2\\(J=0\not \leftrightarrow 0,1;\ {\begin{matrix}{1 \over 2}\end{matrix} }\not \leftrightarrow {\begin{matrix}{1 \over 2}\end{matrix} })\end{matrix} }$$ |                                                    \<                                                   | $${\begin{matrix}\Delta J=0,\pm 1,\pm 2,\pm 3\\(0\not \leftrightarrow 0,1,2;\ {\begin{matrix}{1 \over 2}\end{matrix} }\not \leftrightarrow {\begin{matrix}{1 \over 2}\end{matrix} },{\begin{matrix}{3 \over 2}\end{matrix} };\ 1\not \leftrightarrow 1)\end{matrix} }$$ |                                                        \<                                                       |
|             ^             | __\(2\)__ |               $\Delta M_{J}=0,\pm 1\ (M_{J}=0\not \leftrightarrow 0$ if $\Delta J=0)$               |                            \<                           |                                                                                 $$\Delta M_{J}=0,\pm 1,\pm 2$$                                                                                 |                                                    \<                                                   |                                                                                                                   $$\Delta M_{J}=0,\pm 1,\pm 2,\pm 3$$                                                                                                                  |                                                        \<                                                       |
|             ^             | __\(3\)__ |                                $$\pi _{\text{f} }=-\pi _{\text{i} }$$                               |          $$\pi _{\text{f} }=\pi _{\text{i} }$$          |                                                                                               \<                                                                                               |                                  $$\pi _{\text{f} }=-\pi _{\text{i} }$$                                 |                                                                                                                                    \<                                                                                                                                   |                                      $$\pi _{\text{f} }=\pi _{\text{i} }$$                                      |
|      __LS coupling__      | __\(4\)__ |                               One-electron jump <br/> $\Delta L=\pm 1$                              | No electron jump <br/> $\Delta L=0$, <br/> $\Delta n=0$ |                                                                       None or one-electron jump <br/> $\Delta L=0,\pm 2$                                                                       |                                 One-electron jump <br/> $\Delta L=\pm 1$                                |                                                                                                              One-electron jump <br/> $\Delta L=\pm 1,\pm 3$                                                                                                             |                                    One-electron jump <br/> $\Delta L=0,\pm 2$                                   |
|             ^             | __\(5\)__ | If $\Delta S=0$: <br/> ${\begin{matrix}\Delta L=0,\pm 1\\(L=0\not \leftrightarrow 0)\end{matrix} }$ |          If $\Delta S=0$: <br/> $\Delta L=0\,$          |                                          If $\Delta S=0$: <br/> ${\begin{matrix}\Delta L=0,\pm 1,\pm 2\\(L=0\not \leftrightarrow 0,1)\end{matrix} }$                                           |                                                    \<                                                   |                                                              If $\Delta S=0$: <br/> ${\begin{matrix}\Delta L=0,\pm 1,\pm 2,\pm 3\\(L=0\not \leftrightarrow 0,1,2;\ 1\not \leftrightarrow 1)\end{matrix} }$                                                              |                                                        \<                                                       |
| __Intermediate coupling__ | __\(6\)__ |                        If $\Delta S=\pm 1$: <br/> $\Delta L=0,\pm 1,\pm 2\,$                        |                            \<                           |                                     If $\Delta S=\pm 1$: <br/> ${\begin{matrix}\Delta L=0,\pm 1,\\\pm 2,\pm 3\\(L=0\not \leftrightarrow 0)\end{matrix} }$                                      | If $\Delta S=\pm 1$: <br/> ${\begin{matrix}\Delta L=0,\pm 1\\(L=0\not \leftrightarrow 0)\end{matrix} }$ |                                                                      If $\Delta S=\pm 1$: <br/> ${\begin{matrix}\Delta L=0,\pm 1,\\\pm 2,\pm 3,\pm 4\\(L=0\not \leftrightarrow 0,1)\end{matrix} }$                                                                      | If $\Delta S=\pm 1$: <br/> ${\begin{matrix}\Delta L=0,\pm 1,\\\pm 2\\(L=0\not \leftrightarrow 0)\end{matrix} }$ |

> __flashcards__
>
> - __the six columns__
>     - allowed transitions table / what the six columns are ::@:: the multipole orders, each electric one followed by its magnetic partner: _E1_ electric dipole, _M1_ magnetic dipole, _E2_ electric quadrupole, _M2_ magnetic quadrupole, _E3_ electric octupole and _M3_ magnetic octupole
>     - allowed transitions table / what _E_ and _M_ mean and what the number counts ::@:: electric multipoles come from the charge distribution and magnetic ones from currents and spin, while the number is the multipole order $l$, so _E2_ carries two units of angular momentum and _E3_ three
>     - allowed transitions table / what the three row groups are ::@:: rules (1) to (3) are rigorous and hold for every atom, rules (4) and (5) apply on top of them when _LS_ coupling holds, and rule (6) replaces the _LS_ rules when the coupling is intermediate
> - __the rigorous rules__
>     - allowed transitions table / rule (1), $\Delta J$ for _E1_ and _M1_ ::@:: $\Delta J = 0, \pm 1$, with $J = 0 \not\leftrightarrow 0$. A photon carries one unit of angular momentum, so a state with $J = 0$ cannot stay at $J = 0$ once it emits or absorbs one
>     - allowed transitions table / rule (1), $\Delta J$ for _E2_ and _M2_ ::@:: $\Delta J = 0, \pm 1, \pm 2$, with $J = 0 \not\leftrightarrow 0, 1$ and $\frac{1}{2} \not\leftrightarrow \frac{1}{2}$. The multipole carries $l = 2$, so the three angular momenta have to form a triangle: $|J_i - J_f| \le 2 \le J_i + J_f$. The $\Delta J$ range is the left half and these three pairs fail the right half. A pair such as $\frac{1}{2} \not\leftrightarrow 0$ never enters, since $\Delta J = \frac{1}{2}$ is not one of the listed steps
>     - allowed transitions table / rule (1), $\Delta J$ for _E3_ and _M3_ ::@:: $\Delta J = 0, \pm 1, \pm 2, \pm 3$, with $0 \not\leftrightarrow 0, 1, 2$, $\frac{1}{2} \not\leftrightarrow \frac{1}{2}, \frac{3}{2}$ and $1 \not\leftrightarrow 1$. With $l = 3$ the triangle reads $|J_i - J_f| \le 3 \le J_i + J_f$, and these six pairs pass the left half while failing the right one
>     - allowed transitions table / rule (2), $\Delta M_J$ ::@:: $\Delta M_J = 0, \pm 1$ for _E1_ and _M1_, with the extra condition $M_J = 0 \not\leftrightarrow 0$ when $\Delta J = 0$; up to $\pm 2$ for _E2_ and _M2_; up to $\pm 3$ for _E3_ and _M3_
>     - allowed transitions table / rule (3), the parity change ::@:: _E1_ reverses parity, _M1_ and _E2_ keep it, _M2_ and _E3_ reverse it, and _M3_ keeps it
>     - allowed transitions table / where the parity pattern comes from ::@:: an electric $2^l$-pole reverses parity when $l$ is odd and a magnetic one when $l$ is even, which puts the reversals at _E1_, _M2_ and _E3_ and the unchanged cases at _M1_, _E2_ and _M3_
> - __the LS coupling rules__
>     - allowed transitions table / rule (4), the jump for _E1_ ::@:: one electron jumps to another orbital, with $\Delta L = \pm 1$, since the dipole photon carries a single unit of angular momentum
>     - allowed transitions table / rule (4), the jump for _M1_ ::@:: no electron changes orbital, so $\Delta L = 0$ and $\Delta n = 0$, and only the magnetic moment turns over
>     - allowed transitions table / rule (4), the jump for _E2_ ::@:: none or one electron jumps, with $\Delta L = 0, \pm 2$
>     - allowed transitions table / rule (4), the jump for _M2_, _E3_ and _M3_ ::@:: _M2_ one electron jumps with $\Delta L = \pm 1$; _E3_ one jumps with $\Delta L = \pm 1, \pm 3$; _M3_ one jumps with $\Delta L = 0, \pm 2$
>     - allowed transitions table / rule (5), $\Delta L$ for _E1_ and _M1_ when $\Delta S = 0$ ::@:: _E1_ allows $\Delta L = 0, \pm 1$ with $L = 0 \not\leftrightarrow 0$, and _M1_ allows only $\Delta L = 0$
>     - allowed transitions table / rule (5), $\Delta L$ for _E2_ and _M2_ when $\Delta S = 0$ ::@:: $\Delta L = 0, \pm 1, \pm 2$ with $L = 0 \not\leftrightarrow 0, 1$, the pairs inside that range which fail $L_i + L_f \ge 2$
>     - allowed transitions table / rule (5), $\Delta L$ for _E3_ and _M3_ when $\Delta S = 0$ ::@:: $\Delta L = 0, \pm 1, \pm 2, \pm 3$ with $L = 0 \not\leftrightarrow 0, 1, 2$ and $1 \not\leftrightarrow 1$, the pairs inside that range which fail $L_i + L_f \ge 3$
> - __intermediate coupling__
>     - allowed transitions table / rule (6), what intermediate coupling changes ::@:: the spin no longer fixes the states, so a transition with $\Delta S = \pm 1$ becomes possible and the orbital limits move: one unit wider for _E1_, _E2_ and _E3_, and one unit tighter for _M2_ and _M3_
>     - allowed transitions table / rule (6), $\Delta L$ for _E1_ and _M1_ ::@:: $\Delta L = 0, \pm 1, \pm 2$, the joined limit for the two dipoles: one unit past the spin-fixed range of _E1_ and two past that of _M1_, which allowed only $\Delta L = 0$
>     - allowed transitions table / rule (6), $\Delta L$ for _E2_ ::@:: $\Delta L = 0, \pm 1, \pm 2, \pm 3$, with $L = 0 \not\leftrightarrow 0$. That reaches one unit past the spin-fixed range, and the zero-to-zero exclusion stays
>     - allowed transitions table / rule (6), $\Delta L$ for _M2_ ::@:: $\Delta L = 0, \pm 1$, with $L = 0 \not\leftrightarrow 0$. That stops one unit short of the spin-fixed range, and the zero-to-zero exclusion stays
>     - allowed transitions table / rule (6), $\Delta L$ for _E3_ ::@:: $\Delta L = 0, \pm 1, \pm 2, \pm 3, \pm 4$, with $L = 0 \not\leftrightarrow 0, 1$. That reaches one unit past the spin-fixed range, and both exclusions stay
>     - allowed transitions table / rule (6), $\Delta L$ for _M3_ ::@:: $\Delta L = 0, \pm 1, \pm 2$, with $L = 0 \not\leftrightarrow 0$. That stops one unit short of the spin-fixed range, and the zero-to-zero exclusion stays
> - __reading the table__
>     - allowed transitions table / how to test a candidate transition ::@:: take the column of the multipole that dominates, check rule (1) on $\Delta J$, rule (2) on $\Delta M_J$ and rule (3) on parity, and stop if any of them fails; then apply rules (4) and (5) if _LS_ coupling holds, or rule (6) if the spin changes

In {@{[hyperfine structure](hyperfine%20structure.md)}@}, {@{the total angular momentum of the atom}@} is {@{$F=I+J$}@}, where $I$ is {@{the [nuclear spin angular momentum](quantum%20number.md#nuclear%20angular%20momentum%20quantum%20numbers)}@} and $J$ is {@{the total angular momentum of the electron\(s\)}@}. Since {@{$F=I+J$}@} has {@{a similar mathematical form as $J=L+S$}@}, it obeys {@{a selection rule table similar to the table above}@}.

### surface

In {@{[surface vibrational spectroscopy](vibrational%20spectroscopy.md)}@}, {@{the _surface selection rule_ is applied}@} to identify {@{the peaks observed in vibrational spectra}@}. When {@{a [molecule](molecule.md) is [adsorbed](adsorption.md) on a substrate}@}, the molecule induces {@{opposite image charges in the substrate}@}. {@{The [dipole moment](dipole.md) of the molecule and the image charges perpendicular to the surface}@} {@{reinforce each other}@}. In contrast, {@{the dipole moments of the molecule and the image charges parallel to the surface}@} {@{cancel out}@}. Therefore, only {@{molecular vibrational peaks giving rise to a dynamic dipole moment perpendicular to the surface}@} will be {@{observed in the vibrational spectrum}@}.

## see also

- [Superselection rule](superselection%20rule.md)
- [Spin-forbidden reactions](spin-forbidden%20reactions.md)
- [Singlet fission](singlet%20fission.md)

## notes

1. Harris & Bertolucci, p. 130. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFSalthouseWare1972"></a> Salthouse, J. A.; Ware, M. J. \(1972\). _Point Group Character Tables and Related Data_. [Cambridge University Press](Cambridge%20University%20Press.md). [ISBN](ISBN%20(identifier).md) [0-521-08139-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-08139-4). <a id="^ref-2"></a>^ref-2
3. {@{Anything with _u_ \([German](German%20language.md): _ungerade_\) symmetry}@} is {@{antisymmetric with respect to the centre of symmetry}@}. {@{_g_ \([German](German%20language.md): _gerade_\)}@} signifies {@{symmetric with respect to the centre of symmetry}@}. If {@{the transition moment function has _u_ symmetry}@}, {@{the positive and negative parts}@} will be {@{equal to each other}@}, so {@{the integral has a value of zero}@}. <a id="^ref-3"></a>^ref-3
4. Harris & Berolucci, p. 330. <a id="^ref-4"></a>^ref-4
5. Harris & Berolucci, p. 336. <a id="^ref-5"></a>^ref-5
6. Cotton Section 9.6, Selection rules and polarizations. <a id="^ref-6"></a>^ref-6
7. Cotton, Section 10.6 Selection rules for fundamental vibrational transitions. <a id="^ref-7"></a>^ref-7
8. Cotton, Chapter 10 Molecular Vibrations. <a id="^ref-8"></a>^ref-8
9. Cotton p. 327. <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFCalifano1976"></a> Califano, S. \(1976\). "Chapter 9: Anharmonicity". _Vibrational states_. Wiley. [ISBN](ISBN%20(identifier).md) [0-471-12996-8](https://en.wikipedia.org/wiki/Special:BookSources/0-471-12996-8). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFFateleyMcDevittBentley1971"></a> Fateley, W. G.; McDevitt, Neil T.; Bentley, Freeman F. \(1971\). "Infrared and Raman Selection Rules for Lattice Vibrations: The Correlation Method". _Applied Spectroscopy_. __25__ \(2\): 155–173. [Bibcode](bibcode%20(identifier).md):[1971ApSpe..25..155F](https://ui.adsabs.harvard.edu/abs/1971ApSpe..25..155F). [doi](doi%20(identifier).md):[10.1366/000370271779948600](https://doi.org/10.1366%2F000370271779948600). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFArenasGasparovQiuNino2010"></a> Arenas, D. J.; Gasparov, L. V.; Qiu, Wei; Nino, J. C.; Patterson, Charles H.; Tanner, D. B. \(2010\). "Raman study of phonon modes in bismuth pyrochlores". _Physical Review B_. __82__ \(21\) 214302. [Bibcode](bibcode%20(identifier).md):[2010PhRvB..82u4302A](https://ui.adsabs.harvard.edu/abs/2010PhRvB..82u4302A). [doi](doi%20(identifier).md):[10.1103/PhysRevB.82.214302](https://doi.org/10.1103%2FPhysRevB.82.214302). [hdl](hdl%20(identifier).md):[2262/72900](https://hdl.handle.net/2262%2F72900). <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFZhaoChuaGanZhang2011"></a> Zhao, Yanyuan; Chua, Kun Ting Eddie; Gan, Chee Kwan; Zhang, Jun; Peng, Bo; Peng, Zeping; Xiong, Qihua \(2011\). "Phonons in Bi<sub>2</sub>S<sub>3</sub> nanostructures: Raman scattering and first-principles studies". _Physical Review B_. __84__ \(20\) 205330. [Bibcode](bibcode%20(identifier).md):[2011PhRvB..84t5330Z](https://ui.adsabs.harvard.edu/abs/2011PhRvB..84t5330Z). [doi](doi%20(identifier).md):[10.1103/PhysRevB.84.205330](https://doi.org/10.1103%2FPhysRevB.84.205330). <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFKroto1992"></a> Kroto, H. W. \(1992\). _Molecular Rotation Spectra_. New York: Dover. [ISBN](ISBN%20(identifier).md) [0-486-49540-X](https://en.wikipedia.org/wiki/Special:BookSources/0-486-49540-X). <a id="^ref-14"></a>^ref-14
15. Harris & Berolucci, p. 339. <a id="^ref-15"></a>^ref-15
16. Harris & Berolucci, p. 123. <a id="^ref-16"></a>^ref-16
17. <a id="CITEREFLong2001"></a> Long, D. A. \(2001\). "Chapter 7: Vibrational Resonance Raman Scattering". _The Raman Effect: A Unified Treatment of the Theory of Raman Scattering by Molecules_. Wiley. [ISBN](ISBN%20(identifier).md) [0-471-49028-8](https://en.wikipedia.org/wiki/Special:BookSources/0-471-49028-8). <a id="^ref-17"></a>^ref-17
18. Harris & Berolucci, p. 198. <a id="^ref-18"></a>^ref-18
19. <a id="CITEREFSoftley1994"></a> Softley, T. P. \(1994\). _Atomic Spectra_. Oxford, UK: [Oxford University Press](Oxford%20University%20Press.md). [ISBN](ISBN%20(identifier).md) [0-19-855688-8](https://en.wikipedia.org/wiki/Special:BookSources/0-19-855688-8). <a id="^ref-19"></a>^ref-19
20. <a id="CITEREFCondonShortley1999"></a> Condon, E. V.; Shortley, G. H. \(1999\) \[1935\]. [_The Theory of Atomic Spectra_](https://archive.org/details/in.ernet.dli.2015.212979). Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-09209-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-09209-4). <a id="^ref-20"></a>^ref-20

## references

This text incorporates [content](https://en.wikipedia.org/wiki/selection_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFHarrisBertolucci, M. D.1978"></a> Harris, D. C.; Bertolucci, M. D. \(1978\). _Symmetry and Spectroscopy_. Oxford University Press. [ISBN](ISBN%20(identifier).md) [0-19-855152-5](https://en.wikipedia.org/wiki/Special:BookSources/0-19-855152-5).
- <a id="CITEREFCotton1990"></a> Cotton, F. A. \(1990\). [_Chemical Applications of Group Theory_](https://archive.org/details/isbn_9780471510949) \(3rd ed.\). Wiley. [ISBN](ISBN%20(identifier).md) [978-0-471-51094-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-51094-9).

## further reading

- <a id="CITEREFStanton1973"></a> Stanton, L. \(1973\). "Selection rules for pure rotation and vibration-rotation hyper-Raman spectra". _Journal of Raman Spectroscopy_. __1__ \(1\): 53–70. [Bibcode](bibcode%20(identifier).md):[1973JRSp....1...53S](https://ui.adsabs.harvard.edu/abs/1973JRSp....1...53S). [doi](doi%20(identifier).md):[10.1002/jrs.1250010105](https://doi.org/10.1002%2Fjrs.1250010105).
- <a id="CITEREFBowerMaddams, W. F.1989"></a> Bower, D. I.; Maddams, W. F. \(1989\). "Section 4.1.5: Selection rules for Raman activity". _The vibrational spectroscopy of polymers_. Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-24633-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-24633-4).
- <a id="CITEREFSherwood1972"></a> Sherwood, P. M. A. \(1972\). "Chapter 4: The interaction of radiation with a crystal". _Vibrational Spectroscopy of Solids_. Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-08482-2](https://en.wikipedia.org/wiki/Special:BookSources/0-521-08482-2).

## external links

- [National Institute of Standards and Technology](https://web.archive.org/web/20110514025717/http://physics.nist.gov/Pubs/AtSpec/node17.html)
- [Lecture notes from The University of Sheffield](https://web.archive.org/web/20050426215707/http://www.shef.ac.uk/physics/teaching/phy332/atomic_physics3.pdf)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Quantum mechanics](https://en.wikipedia.org/wiki/Category:Quantum%20mechanics)
> - [Spectroscopy](https://en.wikipedia.org/wiki/Category:Spectroscopy)
> - [Nuclear magnetic resonance](https://en.wikipedia.org/wiki/Category:Nuclear%20magnetic%20resonance)
