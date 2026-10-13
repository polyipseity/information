---
aliases:
  - Bohr model
  - Bohr model of the hydrogen atom
  - Rutherford–Bohr model
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Bohr_model
  - language/in/English
---

# Bohr model

The _Bohr model_ is a model of the hydrogen atom that keeps Rutherford's picture of a heavy nucleus with a light electron and quantises the electron's orbits. It was built to answer a defect the planetary picture could not escape: an orbiting electron radiates, so classical electrodynamics drains the atom in a fraction of a second. Niels Bohr's model postulates fixed orbits that do not radiate, ties emitted light to jumps between them, and from those assumptions alone reproduces hydrogen's spectral lines. It works for one-electron systems and fails beyond them.

---

Flashcards for this section are as follows:

- overview: what the Bohr model is ::@:: A model of the hydrogen atom that keeps the nucleus-and-electron picture and quantises the electron's orbits, reproducing hydrogen's spectral lines from a few postulates.
- the defect of the planetary atom that the Bohr model answers ::@:: An orbiting electron radiates under classical electrodynamics, so the atom would drain and collapse in a fraction of a second.
- what the Bohr model reproduces from its postulates alone ::@:: Hydrogen's spectral lines, including the Balmer formula's wavelengths.

## why the classical picture fails

Rutherford's nuclear atom invites the planetary picture: a light electron held in a circular orbit by the Coulomb attraction of a heavy nucleus. Newton's second law and the Coulomb force fix the motion. The attraction provides the centripetal force, $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$, so the kinetic energy is $K = e^2/(8\pi\varepsilon_0 r)$ and the total energy, kinetic plus the Coulomb potential $-e^2/(4\pi\varepsilon_0 r)$, is $E = -e^2/(8\pi\varepsilon_0 r)$. For a hydrogen atom with $r = 0.5\ \text{Å}$ the electron speed comes out near $2.25 \times 10^6\ \text{m/s}$ and the total energy near $-14.4\ \text{eV}$.

Thomson himself had considered a planetary arrangement before Rutherford's model and rejected it. Gravity and the Coulomb force both fall off as the square of the distance, but planets attract one another as they orbit the sun while electrons repel one another. On his reading of planetary theory that made the arrangement fatally flawed.

The trouble is radiation. Maxwell's electrodynamics has any accelerating charge radiate energy, and an electron in orbit accelerates continuously towards the nucleus. Radiating drains the orbit, the electron spirals inward, and the emitted frequency climbs as the orbit shrinks. A circular orbit accelerates at $a = v^2/r$ and radiates the Larmor power $P = e^2 a^2/(6\pi\varepsilon_0 c^3)$. Substituting $v^2 = e^2/(4\pi\varepsilon_0 m r)$ turns that into $P = e^6/(96\pi^3\varepsilon_0^3 m^2 r^4 c^3)$, which grows faster than the energy as the orbit shrinks. The radiated frequency is the orbital frequency $v/(2\pi r)$, near $7 \times 10^{15}\ \text{Hz}$ at $r = 0.5\ \text{Å}$. Dividing the energy by the power at fixed radius gives the linear estimate $t = |E|/P = 12\pi^2\varepsilon_0^2 m^2 r^3 c^3/e^4$, near $4 \times 10^{-11}\ \text{s}$ at $r = 0.5\ \text{Å}$. Letting the orbit spiral in, with the power rising as it falls, shortens this by a factor of three. The standard estimate of that runaway gives the hydrogen atom a classical lifetime of $1.6 \times 10^{-11}\ \text{s}$, far too short for atoms to exist. The planetary picture explains the scattering results and then destroys the atom it describes.

---

Flashcards for this section are as follows:

- the force balance $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$ that fixes a planetary electron's orbit: what does it give for $K$ and $E$? ::@:: The Coulomb attraction provides the centripetal force, giving kinetic energy $K = e^2/(8\pi\varepsilon_0 r)$ and total energy $E = -e^2/(8\pi\varepsilon_0 r)$.
- for a planetary electron at $r = 0.5\ \text{Å}$ in hydrogen, the speed and total energy ::@:: A speed near $2.25 \times 10^6\ \text{m/s}$ and a total energy near $-14.4\ \text{eV}$.
- Thomson's ground for rejecting a planetary arrangement of the atom ::@:: Planets attract one another as they orbit while electrons repel one another, which he took as a fatal flaw from his knowledge of planetary theory.
- what Maxwell's electrodynamics does to a planetary electron ::@:: The orbiting electron accelerates continuously, so it radiates energy, spirals inward, and raises the emitted frequency as the orbit shrinks.
- the classical lifetime of the hydrogen atom that the radiation estimate gives ::@:: $1.6 \times 10^{-11}\ \text{s}$, far too short for atoms to exist. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the Larmor power $P$ radiated by a charge of acceleration $a$, and its form for the planetary electron ::@:: $P = e^2a^2/(6\pi\varepsilon_0 c^3)$, which becomes $e^6/(96\pi^3\varepsilon_0^3 m^2 r^4 c^3)$ once $v^2 = e^2/(4\pi\varepsilon_0 m r)$ is substituted.
- the frequency $f$ a circular orbit of speed $v$ and radius $r$ radiates at ::@:: the orbital frequency $v/(2\pi r)$, near $7\times10^{15}\ \text{Hz}$ at $r = 0.5\ \text{Å}$.
- the linear collapse estimate $t = |E|/P$ for a planetary electron at radius $r$ ::@:: $t = 12\pi^2\varepsilon_0^2 m^2 r^3 c^3/e^4$, near $4\times10^{-11}\ \text{s}$ at $r = 0.5\ \text{Å}$, and a factor of three above the integrated spiral time.

## assumptions

Four assumptions carry the model. Stationary states exist in the atom: orbits in which the orbiting electron does not radiate, each with a fixed definite energy $E$. Radiation is emitted or absorbed only together with a transition between two stationary states, and the photon frequency satisfies $hf = E_u - E_l$, with $E_u$ and $E_l$ the energies of the upper and lower states. Classical laws of physics do not apply to the transitions between stationary states. The angular momentum of a stationary state is an integral multiple of $\hbar = h/2\pi$, so $mvr = n\hbar$ with $n = 1, 2, 3, \ldots$

---

Flashcards for this section are as follows:

- overview: the four assumptions of the Bohr model ::@:: Stationary states that do not radiate; photon emission and absorption only on transitions with $hf = E_u - E_l$; classical laws suspended during the transitions; angular momentum quantised as $mvr = n\hbar$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the stationary-state assumption about an orbit's energy $E$ ::@:: Orbits exist in the atom in which the orbiting electron does not radiate, and each such orbit has a fixed definite energy $E$.
- the transition assumption, with photon frequency $f$ and state energies $E_u$ and $E_l$ ::@:: Radiation is emitted or absorbed only together with a transition between two stationary states, with the photon frequency set by $hf = E_u - E_l$.
- the assumption about classical physics during transitions ::@:: Classical laws of physics do not apply to the transitions between stationary states.
- the angular-momentum quantisation condition on $mvr$ in terms of $\hbar = h/2\pi$ ::@:: The angular momentum of a stationary state is an integral multiple of $\hbar$, so $mvr = n\hbar$ for $n = 1, 2, 3, \ldots$

<!-- check: ignore-next-line[header_style]: proper noun (eponym) -->
## Bohr radius

Two equations now close on each other. The force balance $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$ holds on every orbit, and the quantisation condition $mvr = n\hbar$ decides which orbits survive. The quantisation sets the speed at each radius, $v = n\hbar/(mr)$, and putting that into the force balance turns it into $n^2\hbar^2/(m r^3) = e^2/(4\pi\varepsilon_0 r^2)$. Clearing denominators then leaves the allowed radii $r_n = 4\pi\varepsilon_0 n^2\hbar^2/(m e^2) = n^2 a_0$, with the Bohr radius $$a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m e^2} = 0.53\ \text{Å},$$ built from constants already known: $\hbar = 1.055 \times 10^{-34}\ \text{J s}$, $\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F/m}$, $m = 9.11 \times 10^{-31}\ \text{kg}$, and $e = 1.60 \times 10^{-19}\ \text{C}$. The ground-state orbit therefore has radius about $0.53\ \text{Å}$, and hydrogen's size, a diameter near $1\ \text{Å}$, falls out of the model instead of being put in by hand.

---

Flashcards for this section are as follows:

- the two equations $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$ and $mvr = n\hbar$ that fix the Bohr orbits: what do they give together? ::@:: The allowed radii $r_n = n^2 a_0$, with $a_0$ the Bohr radius.
- given $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$ and $mvr = n\hbar$, the allowed radius $r_n$ ::@:: $r_n = n^2 a_0$, with $a_0 = \dfrac{4\pi\varepsilon_0 \hbar^2}{m e^2}$ the Bohr radius.
- the Bohr radius $a_0 = \dfrac{4\pi\varepsilon_0 \hbar^2}{m e^2}$: its numerical value ::@:: $a_0 = 0.53\ \text{Å}$, from $\hbar = 1.055 \times 10^{-34}\ \text{J s}$, $\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F/m}$, $m = 9.11 \times 10^{-31}\ \text{kg}$, and $e = 1.60 \times 10^{-19}\ \text{C}$.
- how substituting $v = n\hbar/(mr)$ into $m v^2/r = e^2/(4\pi\varepsilon_0 r^2)$ isolates the allowed orbit radius ::@:: The force balance becomes $n^2\hbar^2/(m r^3) = e^2/(4\pi\varepsilon_0 r^2)$, so clearing denominators gives $r_n = 4\pi\varepsilon_0 n^2\hbar^2/(m e^2) = n^2 a_0$.
- the ground-state orbit radius $a_0$ and the atom's diameter in the Bohr model ::@:: The ground-state orbit has radius about $0.53\ \text{Å}$, so the atom is near $1\ \text{Å}$ across.

## fine structure constant

The model also fixes how fast the electron moves. Combining the force balance with the allowed radii gives $v_n = e^2/(4\pi\varepsilon_0 \hbar n)$, so the speed falls as $1/n$. In the ground state $v_1 = 2.2 \times 10^6\ \text{m/s}$, under one percent of the speed of light. The ratio of that speed to the speed of light is the fine structure constant, $$\alpha = \frac{v_1}{c} = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137}.$$ It is dimensionless, and the model produces it from constants that were already known.

---

Flashcards for this section are as follows:

- overview: the electron speed the Bohr model gives at principal quantum number $n$ ::@:: $v_n = e^2/(4\pi\varepsilon_0 \hbar n)$, falling as $1/n$.
- the ground-state electron speed $v_1$ in the Bohr model, and its share of $c$ ::@:: $v_1 = 2.2 \times 10^6\ \text{m/s}$, under one percent of the speed of light.
- the fine structure constant $\alpha = v_1/c = e^2/(4\pi\varepsilon_0 \hbar c)$: its value ::@:: $\alpha \approx 1/137$, a dimensionless ratio the model builds from already-known constants.

## energy levels

The total energy follows from the same orbits. Kinetic plus potential gives $E = K + V = -e^2/(8\pi\varepsilon_0 r)$, and inserting the allowed radii $r_n = n^2 a_0$ gives the stationary-state energies $$E_n = -\frac{e^2}{8\pi\varepsilon_0 a_0 n^2} = \frac{E_1}{n^2},$$ with $E_1 = -e^2/(8\pi\varepsilon_0 a_0) = -13.6\ \text{eV}$, the total energy at the ground-state radius. The magnitude $13.6\ \text{eV}$ is the energy measured to ionise hydrogen out of its ground state. The $n = 1$ level is the ground state; raising $n$ climbs the ladder towards zero, each step smaller than the last.

---

Flashcards for this section are as follows:

- the stationary-state energies $E_n$ of the Bohr model, in terms of $E_1$ ::@:: $E_n = -\dfrac{e^2}{8\pi\varepsilon_0 a_0 n^2} = E_1/n^2$ with $E_1 = -13.6\ \text{eV}$.
- the ground-state energy $E_1$ of hydrogen in the Bohr model ::@:: $E_1 = -13.6\ \text{eV}$ at $n = 1$; removing the electron from that state takes the measured $13.6\ \text{eV}$.
- how the Bohr level spacing changes as $n$ grows ::@:: The levels climb towards zero and the steps shrink, since $E_n = E_1/n^2$.
- the definition of the ground-state energy $E_1$ in the Bohr level formula $E_n = E_1/n^2$ ::@:: $E_1 = -e^2/(8\pi\varepsilon_0 a_0)$, the total energy $-e^2/(8\pi\varepsilon_0 r)$ at the ground-state radius $r = a_0$.

## spectral series

A photon emitted on a drop from level $n_u$ to level $n_l$ carries $hf = E_u - E_l$, so its wavenumber is $$\frac{1}{\lambda} = R_\infty \left(\frac{1}{n_l^2} - \frac{1}{n_u^2}\right),$$ with the Rydberg constant $R_\infty = E_0/(hc)$ built from the level spacing $E_0 = 13.6\ \text{eV}$, which gives $R_\infty \approx 1.097 \times 10^7\ \text{m}^{-1}$. Fixing $n_l$ and letting $n_u$ run gives a series. The Lyman series ends on the ground state, $n_l = 1$, and lies in the ultraviolet. The Balmer series ends on the second level and lies in the visible: the formula Johann Balmer had fitted by hand in 1885, now derived from the level energies. The Paschen series ends on the third level and lies in the infrared. A gas also takes light away at those same wavelengths, and the dark lines it leaves in a continuum are an [absorption spectrum](absorption%20spectrum.md). The matching between $E_n$ and the Balmer formula is spelled out in [Balmer series](Balmer%20series.md).

That derivation rests on treating the nucleus as infinitely heavy. The electron and the nucleus actually turn about their common centre of mass, and that two-body motion reduces to one body of the reduced mass $\mu = mM/(m + M)$ in place of the electron mass $m$ everywhere in the derivation. For hydrogen $\mu = 0.999456\,m$, which lowers the computed constant to $R = (\mu/m) R_\infty = 1.096776 \times 10^{7}\ \text{m}^{-1}$, the measured $R_{\mathrm H}$ recorded in [Balmer series](Balmer%20series.md). The correction moves with the mass of the nucleus, so isotopes show it directly: deuterium's Hα line falls at $656.29\ \text{nm}$ and tritium's at $656.23\ \text{nm}$ against hydrogen's $656.47\ \text{nm}$, a shift close enough that deuterium was found in 1932 through two closely spaced lines near $656.4\ \text{nm}$, one from hydrogen and one from deuterium.

---

Flashcards for this section are as follows:

- overview: the photon condition on a transition from level $n_u$ down to level $n_l$ ::@:: $hf = E_u - E_l$, giving $\dfrac{1}{\lambda} = R_\infty\left(\dfrac{1}{n_l^2} - \dfrac{1}{n_u^2}\right)$.
- the Rydberg constant $R_\infty = E_0/(hc)$ with $E_0 = 13.6\ \text{eV}$: its value ::@:: $R_\infty \approx 1.097 \times 10^7\ \text{m}^{-1}$.
- the end level $n_l$ and spectral range of the Lyman series ::@:: It ends on the ground state, $n_l = 1$, and lies in the ultraviolet.
- the end level $n_l$ and spectral range of the Balmer series ::@:: It ends on the second level, $n_l = 2$, and lies in the visible.
- the end level $n_l$ and spectral range of the Paschen series ::@:: It ends on the third level, $n_l = 3$, and lies in the infrared.
- what the Bohr model supplied, through $E_n = E_1/n^2$ and $R_\infty = E_0/(hc)$, that the 1885 Balmer fit lacked ::@:: A physical basis: the level energies generate the formula's wavelengths and fix its constant.
- how the mutual orbit of electron and nucleus repairs the infinite-mass assumption, and the reduced-mass factor $\mu/m$ for hydrogen ::@:: Replace the electron mass $m$ with the reduced mass $\mu = mM/(m+M)$, which gives $\mu = 0.999456\,m$ for hydrogen and lowers the computed Rydberg constant to $R = (\mu/m) R_\infty$.
- the Hα wavelengths $\lambda$ of hydrogen, deuterium, and tritium, and what sets their order ::@:: Hydrogen $656.47\ \text{nm}$, deuterium $656.29\ \text{nm}$, tritium $656.23\ \text{nm}$: the heavier nucleus gives the larger reduced mass and hence the shorter wavelength.

## correspondence principle

Bohr's quantum rules and classical electrodynamics disagree about radiating orbits, and they must not disagree where both should hold. The correspondence principle states the rule: in the limits where classical and quantum theories should agree, the quantum result must reduce to the classical one. The test case is hydrogen at large $n$, and the limit can be carried out directly. The adjacent levels differ by $$E_{n+1} - E_n = E_1\!\left[\frac{1}{(n+1)^2} - \frac{1}{n^2}\right] = -E_1\,\frac{2n+1}{n^2 (n+1)^2}.$$ At large $n$ the factor $(2n+1)/(n^2(n+1)^2)$ behaves as $2/n^3$, so a transition down from $n + 1$ emits a photon of frequency $$f = \frac{|E_{n+1} - E_n|}{h} \approx \frac{2\,|E_1|}{h\,n^3}.$$ The classical orbit radiates at its orbital frequency $f_{\text{orb}} = \omega/2\pi$ with $\omega = \sqrt{e^2/(4\pi\varepsilon_0 m r^3)}$ and $r = n^2 a_0$: the cube of the radius grows as $n^6$, so $f_{\text{orb}}$ falls as $1/n^3$ too, and the coefficient agrees with the quantum one exactly. The two descriptions therefore meet at large $n$, where each quantum transition runs at the frequency the classical orbit radiates. They part company only at small $n$, where classical electrodynamics was never applicable anyway. <!-- check: ignore-line[content_sentence_too_long]: the flagged sentence carries the closed-form adjacent-level difference $$E_{n+1}-E_n$$ that the correspondence derivation needs; splitting it from its formula would break the limit argument -->

---

Flashcards for this section are as follows:

- overview: the correspondence principle ::@:: In the limits where classical and quantum theories should agree, the quantum theory must reduce to the classical result.
- the correspondence test in the Bohr model at large $n$ ::@:: The quantum transition frequency from $n + 1$ down to $n$ approaches the electron's classical orbital frequency, both falling as $1/n^3$.
- the exact difference between the adjacent Bohr levels $E_{n+1} - E_n = E_1[1/(n+1)^2 - 1/n^2]$ ::@:: $E_{n+1} - E_n = -E_1\,(2n+1)/(n^2(n+1)^2)$.
- the large-$n$ behaviour of the adjacent-level difference $E_{n+1} - E_n = -E_1(2n+1)/(n^2(n+1)^2)$ ::@:: The factor $(2n+1)/(n^2(n+1)^2)$ behaves as $2/n^3$, so $E_{n+1} - E_n$ approaches $+2|E_1|/n^3$, positive and falling as $1/n^3$.
- the emitted photon frequency for the transition down from $n + 1$ to $n$ ::@:: $f = |E_{n+1} - E_n|/h \approx 2\,|E_1|/(h\,n^3)$ at large $n$.
- the classical orbital angular frequency $\omega$ of the Bohr electron at orbit radius $r$ ::@:: $\omega = \sqrt{e^2/(4\pi\varepsilon_0 m r^3)}$, from the Coulomb force supplying the centripetal acceleration.
- why the classical orbital frequency $f_{\text{orb}} = \omega/2\pi$ also falls as $1/n^3$ at large $n$ ::@:: With $r = n^2 a_0$ the cube $r^3$ grows as $n^6$, so $\omega = \sqrt{e^2/(4\pi\varepsilon_0 m r^3)}$ falls as $1/n^3$, and $f_{\text{orb}}$ with it.

## limitations

Three limitations bound the model. It works only for atoms with a single electron: hydrogen itself and hydrogen-like ions such as $\text{He}^+$ and $\text{Li}^{2+}$, to which the same derivation extends with $r_n = n^2 a_0/Z$ and $E_n = -13.6\,Z^2/n^2\ \text{eV}$ for a nucleus of charge $Ze$. The single-electron scope made a prediction in 1913: spectral lines seen in starlight and in hydrogen-helium discharge tubes, then ascribed to hydrogen, came from singly ionized helium instead, its lines falling between hydrogen's with extra lines of their own.

It cannot account for the intensities of spectral lines, nor for their fine structure. Higher-resolution spectroscopy resolves each line once taken as single into two or more components. This splitting is the fine structure, and Sommerfeld's relativistic treatment of elliptical orbits accounts for part of it while the electron's spin accounts for more. External fields split the lines further: a magnetic field does it through the Zeeman effect, which classical electrodynamics handles in its normal form, while the electric-field Stark effect defeated classical theory and took the Bohr-Sommerfeld quantum model. Running either effect as a measurement is a technique of its own: apply a controlled field and read the level structure off the split lines. Zeeman spectroscopy returns the magnetic moments of the levels that way, and its anomalous form is where the electron's spin enters atomic spectra.

It cannot explain why atoms bind into molecules. Quantum mechanics later replaced the model while keeping the results it got right.

---

Flashcards for this section are as follows:

- overview: the three limitations of the Bohr model ::@:: It works only for single-electron atoms; it cannot account for spectral line intensities or fine structure; it cannot explain the binding of atoms into molecules.
- the atoms to which $r_n = n^2 a_0/Z$ and $E_n = -13.6\,Z^2/n^2\ \text{eV}$ extend beyond hydrogen ::@:: Hydrogen-like ions such as $\text{He}^+$ and $\text{Li}^{2+}$, for nuclear charge $Ze$.
- what the Bohr model could not do with spectral lines ::@:: It could not account for their intensities, nor for their fine structure.
- what the Bohr model could not explain about molecules ::@:: It could not explain the binding of atoms into molecules.
- what the Bohr model identified in 1913 that had been ascribed to hydrogen ::@:: Singly ionized helium: lines from starlight and from hydrogen-helium tubes came from $\text{He}^+$, with the helium lines sitting between hydrogen's. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what higher-resolution spectroscopy shows of a spectral line once taken as single, and what accounts for the splitting ::@:: It resolves into two or more lines, the fine structure; Sommerfeld's relativistic elliptical orbits account for part of the splitting and the electron's spin for more.
- the two external-field effects on spectral lines, and which one classical theory could handle ::@:: A magnetic field splits and broadens them through the Zeeman effect, which classical electrodynamics explains in its normal form; an electric field does it through the Stark effect, which classical theory could not account for.
- the technique that applies a controlled magnetic field and reads atomic level structure off the split lines ::@:: Zeeman spectroscopy, a member of the external-field spectroscopy family; the splitting returns the levels' magnetic moments, and the anomalous form carries the electron's spin.
