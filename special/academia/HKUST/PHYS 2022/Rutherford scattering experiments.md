---
aliases:
  - Geiger–Marsden experiment
  - Rutherford formula
  - Rutherford scattering
  - alpha-particle scattering
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Rutherford_scattering_experiments
  - language/in/English
---

# Rutherford scattering experiments

_Rutherford scattering_ is the elastic scattering of charged particles by the Coulomb interaction. Beams of alpha particles aimed at thin metal foils made it the tool that found the atomic nucleus. Matter too small to see can be read off from how it deflects a beam. Each deflection carries a scattering angle $\theta$, set by the impact parameter $b$, the charges $Z_1 e$ and $Z_2 e$ of particle and scatterer, and the particle's kinetic energy $K$.

---

Flashcards for this section are as follows:

- overview: what Rutherford scattering is ::@:: The elastic scattering of charged particles by the Coulomb interaction, as when a beam of alpha particles deflects off the nuclei in a thin metal foil.
- what a scattering angle $\theta$ depends on ::@:: The impact parameter $b$, the charges $Z_1 e$ and $Z_2 e$ of particle and scatterer, and the particle's kinetic energy $K$.
- what a scattering experiment learns about matter too small to see ::@:: Its structure, read from the angles at which a beam deflects off it.

## backscattering results

Hans Geiger and Ernest Marsden, working under Ernest Rutherford, shot alpha particles at thin gold foils and counted where the particles went. In 1908 they watched how the beam spread out going through more and more material, looking only in the forward direction. In 1909 they found that about 1 alpha particle in 8,000 that struck the gold film bounced backward. In 1911 Rutherford derived a scattering formula that read the 1909 result as the signature of a very small, nearly point-like nucleus. In 1913 Geiger and Marsden tested the formula against angular measurements on different elements and amounts of material, and theory and experiment matched.

A narrow beam reached the foil from a radioactive source screened by a lead plate with a slit in it. The detector was a scintillating screen on an arm that swung around the foil, watched through a microscope: each scattered alpha that struck the screen gave a brief flash. The arm set the scattering angle $\theta$ at which the flashes were counted. <p> ![the Geiger–Marsden apparatus: an alpha source sends a beam through a slit in a lead plate onto a gold foil, a dashed line carries the beam straight on past the foil, and a scattered beam runs back to a scintillating screen in front of a microscope, with the angle theta between the two directions, a dashed arc for the swinging arm, and everything inside a dashed outline labelled evacuated chamber](attachments/geiger_marsden_apparatus.svg)

Most alpha particles passed straight through the foil. A small number were deflected by large angles, beyond $4^\circ$. A very small number came straight back off the foil.

The picture to hold is a bullet fired into a thin box. A homogeneous fill such as wood or water lets the bullet pass with little deviation, the way the plum pudding lets an alpha pass. A few massive steel ball bearings in the box throw occasional bullets backward, the way a compact scatterer inside an atom throws alphas back.

The plum-pudding picture of the atom could not produce those results. In that model the positive charge spreads uniformly through a sphere the size of the atom, and an alpha particle crossing it meets only weak, spread-out fields. A single collision with one of the atom's electrons changes the alpha particle's direction by about $0.016^\circ$; all 79 electrons of a gold atom together add up to roughly $0.14^\circ$. A gold film $6 \times 10^{-7}\ \text{m}$ thick holds about 2,300 atoms along the beam's path, each at a spacing near $2.6 \times 10^{-10}\ \text{m}$, and even taking the deflections as a random walk the total stays around $7^\circ$. Backscattering was absent from that estimate altogether.

Those figures come from random-walk arithmetic. $N$ independent deflections of typical size $\delta$ whose signs are uncorrelated add in quadrature, giving $\theta_{\text{rms}} = \delta\sqrt{N}$. The linear sum $N\delta$ is the worst case, in which every kick pushes the same way, so it overcounts a random walk. Per gold atom, $0.016^\circ \times \sqrt{79} \approx 0.14^\circ$. Per film, $0.14^\circ \times \sqrt{2{,}300} \approx 0.14^\circ \times 48 \approx 6.7^\circ$, which rounds to about $7^\circ$.

---

Flashcards for this section are as follows:

- overview: who scattered alpha particles off gold foils, and in which years the program ran ::@:: Hans Geiger and Ernest Marsden under Ernest Rutherford, with the forward-spread work in 1908, the backscattering count in 1909, the formula in 1911, and the angular tests on several elements in 1913.
- how the Geiger–Marsden apparatus turned scattered alphas into counts at a chosen angle $\theta$ ::@:: A source behind a lead slit sent a narrow beam at the foil; a scintillating screen on a swinging arm caught each scattered alpha as a brief flash, and a microscope watching the screen counted the flashes at the arm's angle $\theta$.
- the fraction of alpha particles that bounced straight back off a gold film ::@:: About 1 in 8,000.
- the three observations from the gold-foil backscattering work ::@:: Most alpha particles passed straight through; a small number deflected by angles beyond $4^\circ$; a very small number came straight back off the foil. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the largest deflection angle $\theta$ a plum-pudding atom's electron gives a single alpha particle in one collision ::@:: About $0.016^\circ$.
- the deflection angle $\theta$ a plum-pudding gold atom's 79 electrons add up to ::@:: Roughly $0.14^\circ$.
- the total deflection expected through a gold film $6 \times 10^{-7}\ \text{m}$ thick under the plum-pudding model ::@:: About $7^\circ$, from roughly 2,300 atoms at $2.6 \times 10^{-10}\ \text{m}$ spacing, taking the per-atom deflections as a random walk.
- for $N$ independent deflections of typical size $\delta$ whose signs are uncorrelated, how does the random-walk total $\theta_{\text{rms}}$ combine the deflections ::@:: $\theta_{\text{rms}} = \delta\sqrt{N}$, since uncorrelated signs add in quadrature; the linear sum $N\delta$ is the worst case in which every kick pushes the same way, so it overcounts.
- through a gold film of about 2,300 atoms, each atom deflecting by about $0.14^\circ$ at random, what total deflection does the random walk reach ::@:: $0.14^\circ \times \sqrt{2{,}300} \approx 0.14^\circ \times 48 \approx 6.7^\circ$, which rounds to about $7^\circ$.
- why the backscattering results through a gold film $6 \times 10^{-7}\ \text{m}$ thick ruled out the plum-pudding model ::@:: That model spreads the positive charge through a sphere the size of the atom, so its largest predicted deflection stays under about $7^\circ$ through such a film, and it predicts no backward scattering at all.
- the black-box thought experiment behind the backscattering result: the two fills and what each does to a bullet ::@:: A homogeneous fill such as wood lets the bullet pass with little deviation, while a few massive steel ball bearings throw occasional bullets backward, so large-angle scattering needs compact massive scatterers.

## assumptions behind the formula

Rutherford's scattering formula rests on four assumptions. The scatterer is so massive that it barely recoils, and the alpha particle's initial and final kinetic energies are practically equal. The target is so thin that only a single scattering occurs. The bombarding particle and the target scatterer are so small that both may be treated as point masses and point charges. Only the Coulomb force acts.

One of those assumptions breaks at a measurable place. While the closest approach stays outside the nucleus, the point-charge picture holds and the counts keep following the scattering equation at every angle. Once a head-on alpha reaches the nuclear surface the charge no longer looks like a point and the nuclear force joins the Coulomb force at that separation. The backward counts then fall below the formula.

Where the departure begins measures the nucleus. The distance of closest approach in a head-on collision is $r_{\min} = Z_1 Z_2 e^2/(4\pi\varepsilon_0 K)$, which for 7.7-MeV alphas on aluminium ($Z_2 = 13$) gives $4.9 \times 10^{-15}\ \text{m}$, close to the summed radii of the alpha particle and the aluminium nucleus. Nuclear radii run from $1 \times 10^{-15}$ to $8 \times 10^{-15}\ \text{m}$, so the deviation appears where the two nuclei nearly touch.

---

Flashcards for this section are as follows:

- overview: what the four assumptions behind the Rutherford scattering formula are ::@:: No significant recoil of the scatterer, single scattering in a thin target, point masses and point charges, and the Coulomb force alone.
- the recoil assumption in the Rutherford scattering formula ::@:: The scatterer is so massive that it barely recoils, so the particle's initial and final kinetic energies are practically equal.
- the thin-target assumption in the Rutherford scattering formula ::@:: The target is so thin that only a single scattering occurs.
- the point-particle assumption in the Rutherford scattering formula ::@:: The bombarding particle and the target scatterer are so small that both act as point masses and point charges.
- the force assumption in the Rutherford scattering formula ::@:: Only the Coulomb force acts.
- how a departure of the backward counts from the Rutherford formula is read ::@:: As the point-charge assumption failing: when the closest approach of a head-on alpha reaches the nuclear surface the backward counts fall below the formula, and where the departure begins marks the size of the nucleus.
- the distance of closest approach $r_{\min} = Z_1 Z_2 e^2/(4\pi\varepsilon_0 K)$ for 7.7-MeV alphas on aluminium, $Z_2 = 13$: its value and what it fixes ::@:: $4.9 \times 10^{-15}\ \text{m}$, close to the summed radii of the alpha particle and the aluminium nucleus; nuclear radii run from $1 \times 10^{-15}$ to $8 \times 10^{-15}\ \text{m}$.

## impact parameter and scattering angle

The trajectory of a scattered particle is fixed by two numbers. The impact parameter $b$ is the perpendicular distance between the scatterer and the incident direction the particle would have taken with no force at all. The scattering angle $\theta$ is the angle between the incoming direction and the outgoing direction. A particle that comes in far from the scatterer feels a weak push and leaves at a small angle; one aimed nearly at the scatterer is thrown back. For Coulomb repulsion the scattering angle $\theta$ and the impact parameter $b$ are locked together by conservation.

A head-on particle that just turns around spends its whole kinetic energy against the Coulomb potential. The distance it reaches, the classical distance of closest approach $a$, then obeys $$K = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a}, \qquad a = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 K}.$$

Off-centre, two quantities are conserved along the whole orbit: the energy $E = K = \tfrac{1}{2}mv_0^2$, with $v_0$ the incident speed, and the angular momentum $L = mv_0 b$. Collect the charges into the repulsive Coulomb constant $k_C = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0}$, so that the potential energy reads $k_C/r$.

Eliminating time turns the energy equation into one for the orbit. The radial equation reads $$\frac{1}{2}m\left(\frac{dr}{dt}\right)^2 + \frac{L^2}{2mr^2} + \frac{k_C}{r} = E.$$ With $\varphi$ the orbit angle, the substitution $\dfrac{d}{dt} = \dfrac{L}{mr^2}\dfrac{d}{d\varphi}$ turns the radial speed into $$\frac{dr}{dt} = \frac{d(1/u)}{d\varphi}\frac{d\varphi}{dt} = -\frac{1}{u^2}\frac{du}{d\varphi}\cdot\frac{L}{mr^2} = -\frac{L}{m}\frac{du}{d\varphi},$$ once $u = 1/r$. In that chain the factor $1/u^2$ equals $r^2$, so it cancels the $1/r^2$ in $d\varphi/dt = L/(mr^2)$. Substituting this radial speed into the radial equation gives the energy equation in $u$: $$\left(\frac{du}{d\varphi}\right)^2 + u^2 + \frac{2mk_C}{L^2}u = \frac{2mE}{L^2}.$$

Differentiating that energy equation with respect to $\varphi$ term by term gives $$2\frac{du}{d\varphi}\frac{d^2u}{d\varphi^2} + 2u\frac{du}{d\varphi} + \frac{2mk_C}{L^2}\frac{du}{d\varphi} = 0,$$ because the right-hand side $2mE/L^2$ is constant. Dividing through by $2\,du/d\varphi$ then leaves the orbit equation $$\frac{d^2u}{d\varphi^2} + u = -\frac{mk_C}{L^2}.$$

The orbit equation has a constant particular solution plus a sinusoidal homogeneous one. A constant has zero second derivative, so the orbit equation itself fixes the particular solution as the constant $u_p = -\dfrac{mk_C}{L^2}$. The homogeneous part obeys $\dfrac{d^2u}{d\varphi^2} + u = 0$ and reads $A\cos\varphi + B\sin\varphi$, which combines into $R\cos(\varphi - \varphi_0)$ with $R = \sqrt{A^2 + B^2}$. The general solution is $u = -\dfrac{mk_C}{L^2} + R\cos(\varphi - \varphi_0)$. Choosing $\varphi = 0$ at closest approach sets $\varphi_0 = 0$, so $u$ is largest there, where $du/d\varphi = 0$. Feeding the solution back into the energy equation then fixes the amplitude scale as $R = e\,mk_C/L^2$, so $$u = \frac{mk_C}{L^2}(e\cos\varphi - 1),$$ with $e$ the eccentricity. The same substitution then fixes $$e = \sqrt{1 + \frac{2EL^2}{mk_C^2}},$$ which exceeds 1 because $E > 0$ for an unbound particle, so the orbit is a hyperbola.

The asymptotes of the hyperbola are where $u = 0$, so $e\cos\varphi_\infty = 1$ and $\cos\varphi_\infty = 1/e$. The incoming and outgoing directions sit at the angles $-\varphi_\infty$ and $+\varphi_\infty$ about the line of closest approach, so the deflection is $\theta = \pi - 2\varphi_\infty$ and $$\tan\frac{\theta}{2} = \cot\varphi_\infty.$$ The cotangent then follows by algebra: $$\cot\varphi_\infty = \frac{\cos\varphi_\infty}{\sin\varphi_\infty} = \frac{1/e}{\sqrt{1 - 1/e^2}} = \frac{1}{\sqrt{e^2 - 1}},$$ where $\sin\varphi_\infty = \sqrt{1 - 1/e^2}$ and the numerator and the denominator are both multiplied by $e$.

The eccentricity already carries the impact parameter. Substituting $L = mv_0 b$ and $E = \tfrac{1}{2}mv_0^2$ into $e^2 - 1 = \dfrac{2EL^2}{mk_C^2}$ gives $$e^2 - 1 = \frac{2 \cdot \frac{1}{2}mv_0^2 \cdot m^2v_0^2b^2}{mk_C^2} = \frac{m^2v_0^4b^2}{k_C^2},$$ so $\sqrt{e^2 - 1} = \dfrac{mv_0^2 b}{k_C}$. With $a = k_C/E = 2k_C/(mv_0^2)$ the head-on distance of closest approach this reads $\sqrt{e^2 - 1} = \dfrac{2b}{a}$, and the angle relation becomes $\tan\dfrac{\theta}{2} = \dfrac{a}{2b}$, that is $$b = \frac{a}{2}\cot\frac{\theta}{2}, \qquad b = \frac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}\cot\frac{\theta}{2},$$ with $a/2 = Z_1 Z_2 e^2/(8\pi\varepsilon_0 K)$.

Small $b$ means large $\theta$. At $b = 0$ the cotangent must be infinite, so $\theta = 180^\circ$: a head-on particle comes straight back. Since the scattering at the largest angles comes from the smallest impact parameters, counting backscattered particles bounds how small the scatterer can be: the nucleus must be smaller than the head-on distance $a$.

![scattering geometry: an incoming particle path coming from the left and bending away as it passes a scatterer, with the impact parameter between the incident line and the scatterer, the scattering angle between the incoming and outgoing directions, and the distance from the scatterer to the particle marked](attachments/rutherford_scattering_geometry.svg)

---

Flashcards for this section are as follows:

- the impact parameter $b$: how it is defined ::@:: The perpendicular distance between the scatterer and the incident direction the particle would have taken with no force acting.
- the scattering angle $\theta$: how it is defined ::@:: The angle between the particle's incoming direction and its outgoing direction.
- a head-on particle that just turns around: what energy balance sets its turning distance $a$ ::@:: The whole kinetic energy $K$ is spent against the Coulomb potential at that distance, $K = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a}$.
- solving that energy balance for the distance $a$: its value in terms of $K$, $Z_1$, and $Z_2$ ::@:: $a = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 K}$.
- the constants conserved in off-centre Rutherford scattering, with $v_0$ the incident speed: what each equals on the incoming leg ::@:: Angular momentum $mv_0 b$, and kinetic energy $K = \tfrac{1}{2}mv_0^2$.
- the chain that turns the radial speed $\dfrac{dr}{dt}$ into an expression in $u = 1/r$, with $L$ the conserved angular momentum ::@:: $\dfrac{dr}{dt} = \dfrac{d(1/u)}{d\varphi}\dfrac{d\varphi}{dt} = -\dfrac{1}{u^2}\dfrac{du}{d\varphi}\cdot\dfrac{L}{mr^2} = -\dfrac{L}{m}\dfrac{du}{d\varphi}$, because $1/u^2 = r^2$ cancels the $1/r^2$ in $\dfrac{d\varphi}{dt} = \dfrac{L}{mr^2}$.
- the step from the energy equation $\left(\dfrac{du}{d\varphi}\right)^2 + u^2 + \dfrac{2mk_C}{L^2}u = \dfrac{2mE}{L^2}$ to the orbit equation ::@:: Differentiating with respect to $\varphi$ gives $2\dfrac{du}{d\varphi}\dfrac{d^2u}{d\varphi^2} + 2u\dfrac{du}{d\varphi} + \dfrac{2mk_C}{L^2}\dfrac{du}{d\varphi} = 0$, because the right-hand side $2mE/L^2$ is constant, and dividing by $2\,du/d\varphi$ leaves $\dfrac{d^2u}{d\varphi^2} + u = -\dfrac{mk_C}{L^2}$.
- for off-centre Coulomb repulsion with conserved angular momentum $L$, what equation does $u = 1/r$ obey as a function of the orbit angle $\varphi$? ::@:: The orbit equation $\dfrac{d^2u}{d\varphi^2} + u = -\dfrac{mk_C}{L^2}$, with $k_C = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0}$ the repulsive Coulomb constant.
- the orbit equation $\dfrac{d^2u}{d\varphi^2} + u = -\dfrac{mk_C}{L^2}$ with $\varphi = 0$ at closest approach: what is its solution, and what is the eccentricity $e$? ::@:: $u = \dfrac{mk_C}{L^2}(e\cos\varphi - 1)$ with $e = \sqrt{1 + \dfrac{2EL^2}{mk_C^2}}$; since $E > 0$ for the unbound particle, $e > 1$ and the orbit is a hyperbola.
- the hyperbolic orbit $u = \dfrac{mk_C}{L^2}(e\cos\varphi - 1)$: how are its asymptotes at $u = 0$ and the scattering angle $\theta$ related to the eccentricity $e$? ::@:: The asymptotes sit at $\cos\varphi_\infty = \dfrac{1}{e}$, so $\theta = \pi - 2\varphi_\infty$ and $\tan\dfrac{\theta}{2} = \cot\varphi_\infty = \dfrac{1}{\sqrt{e^2 - 1}}$.
- the eccentricity $e = \sqrt{1 + \dfrac{2EL^2}{mk_C^2}}$ of off-centre Coulomb scattering, with $L = mv_0 b$ and $E = \tfrac{1}{2}mv_0^2$: what does $\sqrt{e^2 - 1}$ become in terms of the head-on distance $a = k_C/E$? ::@:: $\sqrt{e^2 - 1} = \dfrac{mv_0^2 b}{k_C} = \dfrac{2b}{a}$.
- the impact parameter $b$ and scattering angle $\theta$ in off-centre Coulomb repulsion, with $a = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 K}$ the head-on distance of closest approach: what formula locks $b$ and $\theta$ together? ::@:: $b = \dfrac{a}{2}\cot\dfrac{\theta}{2}$, that is $b = \dfrac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}\cot\dfrac{\theta}{2}$, with $a/2 = \dfrac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}$.
- in $b = \dfrac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}\cot\dfrac{\theta}{2}$, how does $b$ change when $K$ doubles at fixed $Z_1$, $Z_2$, and $\theta$? ::@:: It halves, since $b$ is proportional to $1/K$ at fixed charge product and angle.
- what $b = 0$ gives for $\theta$ in $b = \dfrac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}\cot\dfrac{\theta}{2}$ ::@:: $\theta = 180^\circ$, because the cotangent must then be infinite.
- how the scattering angle $\theta$ changes along a family of trajectories with decreasing impact parameter $b$ ::@:: It grows: particles that come in closer to the scatterer are thrown through larger angles.
- ![scattering geometry: an incoming particle path coming from the left and bending away as it passes a scatterer, with the impact parameter between the incident line and the scatterer, the scattering angle between the incoming and outgoing directions, and the distance from the scatterer to the particle marked](attachments/rutherford_scattering_geometry.svg) ::@:: The drawing marks the particle coming in from the left along a dashed incident line, the scatterer below it, the impact parameter $b$ between the line and the scatterer, the trajectory bending away, the scattering angle $\theta$ between the incoming and outgoing directions, and the separation $r$ from the scatterer to the particle. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## cross section

Every particle whose incident line falls inside the circle of radius $b$ around the scatterer is deflected by at least the angle $\theta$ that belongs to that $b$. A smaller impact parameter $b$ belongs to a larger scattering angle $\theta$, so the disc of radius $b$ collects every particle scattered at $\theta$ or beyond, and nothing outside the disc reaches those angles. The area of that circle is the cross section $\sigma = \pi b^2$.

A film of thickness $t$ holds $nt$ scatterers per unit area, where $n$ is the atomic density, so the fraction of the beam scattered beyond $\theta$ is $$f = nt\sigma = nt\pi b^2.$$

A detector counts a ring of directions around $\theta$, not one exact angle, so the cross section is also needed per unit solid angle. The annulus of impact parameters from $b$ to $b + db$ has area $2\pi b\,db$, and it maps onto the ring of solid angles from $\Omega$ to $\Omega + d\Omega$. Because $b$ falls as $\theta$ grows, the map reverses orientation, and the annulus carries an absolute value, $d\sigma = 2\pi b\,|db|$.

Summing over every angle at once runs into the range of the bare Coulomb law. The sum $\sigma_{\text{tot}} = \int d\sigma$ telescopes to the disc of the largest impact parameter it includes: with $\theta_{\min}$ the smallest angle counted, the annuli fill the disc of radius $b(\theta_{\min})$ and leave nothing behind, so $$\sigma_{\text{tot}} = \pi b(\theta_{\min})^2.$$ For the bare Coulomb law $b = \dfrac{a}{2}\cot\dfrac{\theta}{2}$ grows without bound as $\theta \to 0$, so $\sigma_{\text{tot}}$ diverges. A real atom cuts the sum off: beyond the screening radius the electron cloud cancels the nuclear field, the Coulomb force dies off, and $b$ saturates there, leaving $\sigma_{\text{tot}} = \pi b_{\text{screen}}^2$ finite.

---

Flashcards for this section are as follows:

- overview: what the cross section $\sigma = \pi b^2$ counts ::@:: The area around a scatterer inside which every incident line scatters the particle by at least the angle $\theta$ that belongs to that impact parameter $b$.
- the fraction $f$ of a beam scattered beyond an angle $\theta$ by a film of thickness $t$ ::@:: $f = nt\sigma = nt\pi b^2$, with $n$ the atomic density and $\sigma = \pi b^2$ the cross section.
- in $f = nt\pi b^2$ with $b = \dfrac{Z_1 Z_2 e^2}{8\pi\varepsilon_0 K}\cot\dfrac{\theta}{2}$, how does $f$ change when the incident kinetic energy $K$ quadruples at fixed charges, angle, and film? ::@:: It falls to a sixteenth, since $b$ scales as $1/K$ and $f$ scales as $b^2$.
- the annulus of impact parameters from $b$ to $b + db$ around a scatterer, mapped onto the ring of solid angles $[\Omega, \Omega + d\Omega]$: what differential cross section does it carry, and why the absolute value? ::@:: $d\sigma = 2\pi b\,|db|$, since the annulus area is $2\pi b\,db$ and $b$ falls as $\theta$ grows, so the map from $b$ to $\Omega$ reverses orientation.
- the total cross section $\sigma_{\text{tot}} = \int d\sigma$ summed over every angle, for the bare Coulomb law $b = \dfrac{a}{2}\cot\dfrac{\theta}{2}$, down to a smallest counted angle $\theta_{\min}$: what does the sum evaluate to, why does it diverge, and what makes it finite in a real atom? ::@:: The annuli telescope to the disc of the largest impact parameter, $\sigma_{\text{tot}} = \pi b(\theta_{\min})^2$; it diverges because $b \to \infty$ as $\theta_{\min} \to 0$; in a real atom the electron cloud screens the nuclear field beyond the screening radius, so $b$ saturates there and $\sigma_{\text{tot}} = \pi b_{\text{screen}}^2$ stays finite.

<!-- check: ignore-next-line[header_style]: proper noun (eponym) -->
## Rutherford scattering equation

Counting the particles that reach a detector at angle $\theta$ gives the scattering equation. The differential cross section follows from the impact parameter relation $$b = \frac{a}{2}\cot\frac{\theta}{2}, \qquad a = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 K},$$ with $a$ the head-on distance of closest approach.

The foil of thickness $t$ with $n$ scatterers per unit volume holds $nt$ scatterers per unit area. Each scatterer presents an effective area $d\sigma$ for landing inside the ring of directions $d\Omega$, so one incident particle is caught with probability $(nt)\,d\sigma = (nt)\dfrac{d\sigma}{d\Omega}\,d\Omega$. $N_i$ incident particles therefore give $N_i n t\,\dfrac{d\sigma}{d\Omega}\,d\Omega$ arrivals, which is the number the detector counts.

Differentiating $b$ with respect to $\theta$ gives $$\frac{db}{d\theta} = -\frac{a}{4}\csc^2\frac{\theta}{2},$$ because the derivative of $\cot(\theta/2)$ is $-\tfrac{1}{2}\csc^2(\theta/2)$.

The ring of directions around $\theta$ covers the solid angle $$d\Omega = 2\pi\sin\theta\,d\theta,$$ and the double-angle identity $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$ writes its factor in terms of $\theta/2$.

Divide the annulus $d\sigma = 2\pi b\,|db|$ by the ring $d\Omega = 2\pi\sin\theta\,d\theta$: the $2\pi$ is common to both, and $$\frac{d\sigma}{d\Omega} = \frac{2\pi b\,|db|}{2\pi\sin\theta\,d\theta} = \frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right|.$$

Substituting $b$ and $db/d\theta$ gives $$\frac{d\sigma}{d\Omega} = \frac{\frac{a}{2}\cot(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)}\cdot\frac{a}{4}\csc^2(\theta/2),$$ where the $\cos(\theta/2)$ inside $\cot(\theta/2) = \cos(\theta/2)/\sin(\theta/2)$ cancels the $\cos(\theta/2)$ from $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$. The first factor is then $\dfrac{a}{4\sin^2(\theta/2)}$, and the second is $\dfrac{a}{4\sin^2(\theta/2)}$ once $\csc^2(\theta/2)$ is written as $1/\sin^2(\theta/2)$, so $$\frac{d\sigma}{d\Omega} = \left(\frac{a}{4}\right)^2\frac{1}{\sin^4(\theta/2)}.$$

Finally $a/4 = \dfrac{Z_1 Z_2 e^2}{16\pi\varepsilon_0 K}$ turns the prefactor into charges and energy, and the scattering equation reads $$\frac{d\sigma}{d\Omega} = \left(\frac{Z_1 Z_2 e^2}{16\pi\varepsilon_0 K}\right)^2 \frac{1}{\sin^4(\theta/2)}.$$

Four scalings follow directly, and each one was tested. The count grows with the square of the atomic number of the incident particle, $Z_1 = 4$ for an alpha particle, and with the square of the atomic number of the target, $Z_2 = 79$ for gold. It falls with the inverse square of the incident kinetic energy, near 7.7 MeV in the tests on gold. It falls with the fourth power of $\sin(\theta/2)$, so large angles are rare in proportion to that steep factor. And it grows in proportion to the target thickness, $0.6\ \mu\text{m}$ in those same tests. The $Z_2^2$ and thickness scalings let [Rutherford backscattering spectrometry](Rutherford%20backscattering%20spectrometry.md) read a sample's composition and layer thickness from the backscattered count.

---

Flashcards for this section are as follows:

- overview: the Rutherford differential cross section for a particle of charge $Z_1 e$ scattered by a nucleus of charge $Z_2 e$ at kinetic energy $K$ ::@:: $\dfrac{d\sigma}{d\Omega} = \left(\dfrac{Z_1 Z_2 e^2}{16\pi\varepsilon_0 K}\right)^2 \dfrac{1}{\sin^4(\theta/2)}$, and the detector count is $N_i n t$ times this times the solid angle covered.
- a foil of thickness $t$ with $n$ scatterers per unit volume is hit by $N_i$ particles, and each scatterer presents an effective area $d\sigma$ for landing inside the ring of directions $d\Omega$; how many particles reach the detector? ::@:: The foil holds $nt$ scatterers per unit area; one incident particle is caught with probability $(nt)\,d\sigma = (nt)\,\dfrac{d\sigma}{d\Omega}\,d\Omega$; $N_i$ incident particles give $N_i n t\,\dfrac{d\sigma}{d\Omega}\,d\Omega$ arrivals.
- the annulus of impact parameters $d\sigma = 2\pi b\,|db|$ and the ring of directions $d\Omega = 2\pi\sin\theta\,d\theta$; what does dividing the first by the second give? ::@:: The $2\pi$ cancels, so $\dfrac{d\sigma}{d\Omega} = \dfrac{2\pi b\,|db|}{2\pi\sin\theta\,d\theta} = \dfrac{b}{\sin\theta}\left|\dfrac{db}{d\theta}\right|$.
- for the annulus $d\sigma = 2\pi b\,|db|$ of impact parameters and the ring $d\Omega = 2\pi\sin\theta\,d\theta$ of directions, with $b = \dfrac{a}{2}\cot\dfrac{\theta}{2}$ and $\left|\dfrac{db}{d\theta}\right| = \dfrac{a}{4}\csc^2\dfrac{\theta}{2}$, what is the differential cross section $d\sigma/d\Omega$? ::@:: $\dfrac{d\sigma}{d\Omega} = \dfrac{b}{\sin\theta}\left|\dfrac{db}{d\theta}\right| = \left(\dfrac{a}{4}\right)^2\dfrac{1}{\sin^4(\theta/2)}$: the $\cos(\theta/2)$ of $\cot(\theta/2)$ cancels the $\cos(\theta/2)$ from $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$, and $(a/2)\cdot(a/4)$ divided by the 2 of $\sin\theta$ is $(a/4)^2$.
- with $a = \dfrac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 K}$ the head-on distance of closest approach in $b = \dfrac{a}{2}\cot\dfrac{\theta}{2}$, what is $a/4$, and what does $\left(\dfrac{a}{4}\right)^2\dfrac{1}{\sin^4(\theta/2)}$ then read? ::@:: $a/4 = \dfrac{Z_1 Z_2 e^2}{16\pi\varepsilon_0 K}$, so $\dfrac{d\sigma}{d\Omega} = \left(\dfrac{Z_1 Z_2 e^2}{16\pi\varepsilon_0 K}\right)^2\dfrac{1}{\sin^4(\theta/2)}$.
- the atomic numbers $Z_1$ and $Z_2$ entering the Rutherford cross section for alpha particles on gold ::@:: $Z_1 = 4$ for the alpha particle and $Z_2 = 79$ for gold, and the count grows with the square of each.
- how the Rutherford scattering count depends on the incident kinetic energy $K$ ::@:: It falls with the inverse square of $K$, near 7.7 MeV in the alpha-on-gold tests.
- how the Rutherford scattering count depends on the scattering angle $\theta$ ::@:: It falls with the fourth power of $\sin(\theta/2)$, so large-angle scattering is rare.
- how the Rutherford scattering count depends on the target thickness $t$ ::@:: It grows in proportion to $t$, at $0.6\ \mu\text{m}$ in the alpha-on-gold tests, through the factor $nt$.
