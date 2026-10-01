---
aliases:
  - cavity mode count
  - density of modes
  - mode density
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/mode_density_of_a_cavity
  - language/in/English
---

# mode density of a cavity

A mode is one independent standing wave of the electromagnetic field. Every law of black-body radiation is then one calculation with one quantity changed: the average energy a single mode holds, written $\overline{E}$ here. The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md), the [Wien approximation](Wien%20approximation.md) and [Planck's law](Planck%27s%20law.md) supply that one quantity and nothing else.

---

Flashcards for this section are as follows:

- overview: what a mode is ::@:: One independent standing wave of the electromagnetic field.
- overview: what the three laws of black-body radiation share, and the one quantity $\overline{E}$ each supplies for itself ::@:: The mode density and the two solid-angle factors relating energy density, radiance and flux are shared; each law supplies only its own average energy $\overline{E}$ for a mode.
- overview: the single step on which the three laws differ ::@:: The average energy $\overline{E}$ assigned to one mode, which is $k_BT$ for Rayleigh–Jeans, $hf\,e^{-hf/(k_BT)}$ for Wien, and $\frac{hf}{e^{hf/(k_BT)}-1}$ for Planck. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the mode count

Take a cubic box of side $L$. A standing wave inside it carries a wavevector $\mathbf{k}$, a vector recording how many cycles fit along each axis, and $k = |\mathbf{k}|$ is its size.

The field must vanish at each pair of opposite walls, so along each axis the box holds a whole number of half-wavelengths. That fixes the three components: $k_x = \frac{\pi n_x}{L}$ along the first axis, and likewise $k_y = \frac{\pi n_y}{L}$ and $k_z = \frac{\pi n_z}{L}$, where $n_x$, $n_y$ and $n_z$ are the half-wavelength counts along the three axes. The integers are positive: a cosine built on $-k$ is the same standing wave as one built on $+k$, so negative integers would count every wave twice.

Those permitted points lie on a cubic lattice of spacing $\pi/L$ along each axis, so the wavevectors fill $k$-space uniformly at $(L/\pi)^3$ points per unit volume, and the box size enters the count only here.

Group the modes by magnitude. Every mode whose wavelength falls within one narrow range has nearly the same $k$, so those modes occupy a thin spherical shell of radius $k$ and radial thickness $dk$, the change in $k$ across that range. The shell's volume is $4\pi k^2\,dk$.

The lattice fills one octant of $k$-space, where $k_x$, $k_y$ and $k_z$ are all positive, while a whole shell holds eight of them, so the count is divided by $8$. Each standing-wave pattern also admits two independent transverse polarisations of the electromagnetic field, and each polarisation carries its own energy, so the count is multiplied by two. The number of modes in the shell is $\left(\frac{L}{\pi}\right)^3 4\pi k^2\,dk \times \frac{2}{8}$, and no further correction applies to the $\pm\mathbf{k}$ pair, since the positive integers have already excluded the negative half of the shell.

Divide by the volume $V = L^3$ to get modes per unit volume. The lattice factor cancels against the volume, leaving $\dfrac{1}{L^3}\left(\frac{L}{\pi}\right)^3 4\pi k^2\,dk \times \dfrac{2}{8} = \dfrac{k^2\,dk}{\pi^2}$.

Now put $\lambda$ in place of $k$. Since $k = 2\pi/\lambda$, $\dfrac{dk}{d\lambda} = -\dfrac{2\pi}{\lambda^2}$, negative because $k$ shrinks as $\lambda$ grows. A count of modes is positive, so the density per unit wavelength takes the magnitude, $|dk| = \dfrac{2\pi}{\lambda^2}\,d\lambda$; keeping the minus sign would give a negative density.

That substitution produces the fourth power of the wavelength: $\dfrac{k^2\,dk}{\pi^2} = \dfrac{4\pi^2}{\lambda^2} \times \dfrac{2\pi}{\lambda^2}\,d\lambda \times \dfrac{1}{\pi^2} = \dfrac{8\pi}{\lambda^4}\,d\lambda$, and the mode density per unit wavelength is $n(\lambda) = 8\pi/\lambda^4$.

None of this assumes anything about energy. The count asks only which standing waves fit inside a box of a given size, so it survives into all three laws unaltered and their failures lie elsewhere.

---

Flashcards for this section are as follows:

- the wavevector $\mathbf{k}$ of a standing wave, and the size $k$ ::@:: $\mathbf{k}$ records how many cycles fit along each axis, and $k = |\mathbf{k}|$ is its magnitude.
- the standing-wave condition in a cubic box of side $L$, and what the integers $n_x$, $n_y$, $n_z$ count ::@:: $k_x = \frac{\pi n_x}{L}$ along the first axis, and likewise $k_y$ and $k_z$, with each $n$ the half-wavelength count along that axis and each positive.
- why the integers $n$ run over positive values and not over all integers ::@:: A cosine built on $-k$ is the same standing wave as one built on $+k$, so negative integers would list every wave twice.
- where the permitted wavenumbers sit in $k$-space, how densely, and where the box size drops out ::@:: On a cubic lattice of spacing $\pi/L$ along each axis, filling $k$-space uniformly at $(L/\pi)^3$ points per unit volume, and that lattice factor is the only place $L$ enters and cancels against the volume $V = L^3$ on the way to a density per unit volume.
- the region of $k$-space holding all modes of one narrow wavelength range, and its volume ::@:: A thin spherical shell of radius $k = |\mathbf{k}|$ and thickness $dk$, the change in $k$ across that range, of volume $4\pi k^2\,dk$.
- the factor $\frac{1}{8}$ in the shell count, and what it accounts for ::@:: The lattice was built from positive integers and so fills one octant of $k$-space, where $k_x$, $k_y$ and $k_z$ are all positive, while a whole shell holds eight of them.
- the factor of $2$ in the shell count, and what it accounts for ::@:: The two independent transverse polarisations of the electromagnetic field, each of which carries its own energy.
- the number of modes in a thin shell of $k$-space, with both corrections combined ::@:: $\left(\frac{L}{\pi}\right)^3 4\pi k^2\,dk \times \frac{2}{8}$.
- why there is no further correction for the $\pm\mathbf{k}$ pair ::@:: The positive integers have already excluded the negative half of the shell, so a factor for it would count those waves twice.
- the mode count per unit volume, after dividing the shell count by $V = L^3$ ::@:: $\dfrac{k^2\,dk}{\pi^2}$, the lattice factor $(L/\pi)^3$ having cancelled against the volume.
- the change of variable that turns $k^2\,dk/\pi^2$ into a density per unit wavelength ::@:: $k = 2\pi/\lambda$, with $\dfrac{dk}{d\lambda} = -\dfrac{2\pi}{\lambda^2}$ negative because $k$ and $\lambda$ run opposite ways, so the density uses $|dk| = \dfrac{2\pi}{\lambda^2}\,d\lambda$ and $\frac{k^2\,dk}{\pi^2} = \frac{4\pi^2}{\lambda^2} \times \frac{2\pi}{\lambda^2} \times \frac{1}{\pi^2} = \frac{8\pi}{\lambda^4}\,d\lambda$.
- the sign of $\dfrac{dk}{d\lambda}$, and why the mode density uses its magnitude instead ::@:: It is negative, since $k = 2\pi/\lambda$ falls as $\lambda$ rises; a count of modes is positive, so the density per unit wavelength takes $|dk|$, and keeping the minus sign would give a negative density.
- the mode density $n(\lambda)$ per unit volume per unit wavelength ::@:: $8\pi/\lambda^4$.
- why the mode count needs no assumption about energy ::@:: It asks only which standing waves fit inside a box of a given size, so it survives into all three laws unchanged and their failures must lie elsewhere.

## from the count to a flux

The count gives modes per unit volume per unit wavelength. Three further quantities sit between it and the power a surface radiates, and any of the three laws may quote any of them:

| quantity | what it measures | symbol |
| --- | --- | --- |
| mode density | modes per unit volume, per unit wavelength | $n(\lambda)$ |
| energy density | energy per unit volume, per unit wavelength | $u_\lambda$ |
| spectral radiance | power per unit area, per steradian, per unit wavelength | $B_\lambda$ |
| flux | power per unit area, per unit wavelength leaving a surface | $I_\lambda$ |

Each step multiplies by a constant fixed by solid angle. The chain reads $u_\lambda = n(\lambda)\,\overline{E}$, then $B_\lambda = \frac{c}{4\pi}\,u_\lambda$, then $I_\lambda = \pi\,B_\lambda = \frac{1}{4}c\,u_\lambda$.

The factor $\frac{1}{4\pi}$ comes from the cavity being isotropic. Its field radiates in every direction at once, so the energy leaves through the full solid angle of a sphere. A steradian is the unit of solid angle, and a whole sphere measures $4\pi$ of them. Divide the energy density by that angle and multiply by $c$, and the radiance follows.

The factor $\pi$ comes from a flat surface's geometry, and no solid angle enters it. A surface radiates into a hemisphere of $2\pi$ steradians, and its emission per unit area falls off across that hemisphere as $\cos\theta$, where $\theta$ is the angle away from the surface normal, because a tilted patch presents less area to the sky. The flux is the cosine-weighted angular integral, $\int_0^{2\pi}d\phi\int_0^{\pi/2} B_\lambda\cos\theta\,\sin\theta\,d\theta = 2\pi \times \frac{1}{2} = \pi$, with $\phi$ the angle around the normal. The azimuth integral supplies the $2\pi$ and the polar integral the $\tfrac{1}{2}$. Counting steradians alone would not give $\pi$: a plain $2\pi$ multiplier with no cosine puts the flux a factor of two too high.

For a given mean energy $\overline{E}$, the energy density is $8\pi\,\overline{E}/\lambda^4$, the radiance $2c\,\overline{E}/\lambda^4$ and the flux $2\pi c\,\overline{E}/\lambda^4$.

That fourth power appears in every law. A fifth appears only because the mean energy carries a factor of $1/\lambda$: for a mode of frequency $f$, $\overline{E} = hf$ and $f = c/\lambda$ give $\overline{E} = hc/\lambda$.

Both multipliers in the chain are constants, so the peak of the curve sits at the same wavelength whichever quantity you plot. Only the height changes.

---

Flashcards for this section are as follows:

- the four quantities $n(\lambda)$, $u_\lambda$, $B_\lambda$, $I_\lambda$, and what each measures ::@:: Modes per unit volume per unit wavelength; energy per unit volume per unit wavelength; power per unit area per steradian per unit wavelength; and power per unit area per unit wavelength leaving a surface.
- the chain that joins $u_\lambda$, $B_\lambda$ and $I_\lambda$, in order ::@:: $u_\lambda = n(\lambda)\,\overline{E}$, then $B_\lambda = \frac{c}{4\pi}\,u_\lambda$, then $I_\lambda = \pi\,B_\lambda = \frac{1}{4}c\,u_\lambda$, each step a multiplication by a constant fixed by solid angle, with the $4\pi$ of the cavity cancelling against the $\pi$ of the hemisphere.
- a steradian, and the solid angle of a whole sphere ::@:: The unit of solid angle, so a whole sphere measures $4\pi$ of them. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the factor $\frac{1}{4\pi}$ in $B_\lambda = \frac{c}{4\pi}u_\lambda$, and what it accounts for ::@:: The isotropy of a cavity, whose field radiates through the full solid angle of a sphere, $4\pi$ steradians, so the energy density is divided by that angle and multiplied by $c$.
- the angle $\theta$ in the cosine-weighted integral, and the angle $\phi$ beside it ::@:: $\theta$ is the angle away from the surface normal, and $\phi$ is the angle around it.
- the factor $\pi$ in $I_\lambda = \pi B_\lambda$, and what it accounts for ::@:: A cosine-weighted angular integral over a hemisphere, not a solid angle: $\int_0^{2\pi}d\phi\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta = 2\pi\times\frac12 = \pi$.
- the solid angle of a hemisphere, and why the flux factor is nevertheless $\pi$ ::@:: $2\pi$ steradians, half of a sphere; the flux is a cosine-weighted integral rather than a plain solid-angle count, the cosine supplying the extra factor of $\tfrac{1}{2}$, and leaving it out would put the flux a factor of two too high.
- the prefactor each quantity carries for a given mean energy $\overline{E}$, with $n(\lambda) = 8\pi/\lambda^4$ ::@:: The energy density is $8\pi\,\overline{E}/\lambda^4$, the radiance $2c\,\overline{E}/\lambda^4$, and the flux $2\pi c\,\overline{E}/\lambda^4$, so the three differ by factors of $\pi$ and $4$ and nothing else.
- why the mode density carries a fourth power of $\lambda$ and the laws a fifth ::@:: $n(\lambda) = 8\pi/\lambda^4$ is already a density per unit wavelength, so its fourth power comes from the geometry; the fifth appears only once the mean energy contributes a factor of $1/\lambda$ of its own, since $\overline{E} = hf = hc/\lambda$ for a mode of frequency $f$.
- why the choice among the four quantities does not move the peak of the curve, given the multipliers $c/(4\pi)$ and $\pi$ ::@:: Both are constants in $\lambda$, so they change the height of the curve and leave the peak wavelength where it is.

## where each law plugs in

The chain is fixed apart from one factor. Each law supplies its own $\overline{E}$ and shares everything else:

| law | average energy per mode $\overline{E}$ | agrees with measurement when |
| --- | --- | --- |
| [Rayleigh–Jeans](Rayleigh%E2%80%93Jeans%20law.md) | $k_BT$ | $hf \ll k_BT$, long wavelengths |
| [Wien approximation](Wien%20approximation.md) | $hf\,e^{-hf/(k_BT)}$ | $hf \gg k_BT$, short wavelengths |
| [Planck's law](Planck%27s%20law.md) | $\dfrac{hf}{e^{hf/(k_BT)} - 1}$ | everywhere |

Only the middle column differs between the three rows. Each law is a single expression for $\overline{E}$ multiplied by the shared prefactor $\dfrac{2\pi c}{\lambda^4}\,\overline{E}$ for $I_\lambda$, once $f = c/\lambda$ has turned the $f$ in $hf$ into $\lambda$.

The first two rows fail in opposite directions and the third gives both as limits, which is the argument made in [ultraviolet catastrophe](ultraviolet%20catastrophe.md). Both limits appear in [Planck's law](Planck%27s%20law.md).

---

Flashcards for this section are as follows:

- the expression all three laws share for $I_\lambda$ once the mean energy is written separately ::@:: $I_\lambda = \dfrac{2\pi c}{\lambda^4}\,\overline{E}$, the same prefactor for Rayleigh–Jeans, Wien and Planck.
- the mean energy $\overline{E}$ the [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) supplies, and where it is right ::@:: $k_BT$ from equipartition, right where $hf \ll k_BT$ and so at long wavelengths.
- the mean energy $\overline{E}$ the [Wien approximation](Wien%20approximation.md) supplies, and where it is right ::@:: $hf\,e^{-hf/(k_BT)}$, right where $hf \gg k_BT$ and so at short wavelengths.
- the mean energy $\overline{E}$ [Planck's law](Planck%27s%20law.md) supplies, and where it is right ::@:: $\dfrac{hf}{e^{hf/(k_BT)} - 1}$, right at every wavelength.
- the flux the Rayleigh–Jeans law gives, from $\overline{E} = k_BT$ in $I_\lambda = \frac{2\pi c}{\lambda^4}\overline{E}$ ::@:: $I_\lambda = \dfrac{2\pi c k_BT}{\lambda^4}$.
- the flux the Wien approximation gives, from $\overline{E} = hf\,e^{-hf/(k_BT)}$ in $I_\lambda = \frac{2\pi c}{\lambda^4}\overline{E}$ ::@:: $I_\lambda = \dfrac{2\pi c}{\lambda^4}\cdot\dfrac{hc}{\lambda}e^{-hc/(\lambda k_BT)} = \dfrac{2\pi hc^2}{\lambda^5}e^{-hc/(\lambda k_BT)}$, using $f = c/\lambda$.
- the flux Planck's law gives, from $\overline{E} = \frac{hf}{e^{hf/(k_BT)}-1}$ in $I_\lambda = \frac{2\pi c}{\lambda^4}\overline{E}$ ::@:: $I_\lambda = \dfrac{2\pi c}{\lambda^4}\cdot\dfrac{hc}{\lambda}\,\dfrac{1}{e^{hc/(\lambda k_BT)}-1} = \dfrac{2\pi hc^2}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)}-1}$.
- the two limiting mean energies as limits of the Planck form, and what they pin down ::@:: $k_BT$ as $hf/(k_BT) \to 0$, which is Rayleigh–Jeans, and $hf\,e^{-hf/(k_BT)}$ as $hf/(k_BT) \to \infty$, which is Wien, and only $\frac{hf}{e^{hf/(k_BT)}-1}$ does both. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
