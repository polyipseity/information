---
aliases:
  - list of angular masses
  - list of second moments of mass
  - list of mass moments of inertia
  - list of moments of inertia
  - list of rotational inertias
tags:
  - flashcard/active/general/eng/list_of_moments_of_inertia
  - language/in/English
---

# list of moment of inertia

## scalar moments of inertia

### cuboid, axis through center

- definition ::@:: a homogeneous [cuboid](cuboid.md) of density $\rho$, height $H$ ($a$), length $L$ ($b$), and width $W$ ($c$), axis through center <!--SR:!2026-03-15,543,327!2028-03-20,1156,367-->
- equation ::@:: $I_a=\frac1{12}m\left(b^2+c^2\right)$ <!--SR:!2025-12-05,447,250!2025-02-01,249,338-->
  - thin plate correction ::@:: use the same equation <!--SR:!2027-08-11,1086,350!2025-02-06,254,338-->
  - cuboid, axis through center of edge $c$ ::@:: $I_{a@c}=\frac1{12}m\left(4b^2+c^2\right)$ <!--SR:!2025-03-19,254,250!2025-05-30,297,298-->
  - thin plate with $c=0$, axis through edge $a$ ::@:: $I_{a@c=0}=\frac13mb^2$ <!--SR:!2025-12-29,554,310!2025-08-16,351,298-->
- proof: $$\begin{aligned}
m&=\rho{}HLW\\
I_H&=\int_0^W\!\int_0^L\!\int_0^H\rho\left(\left(l-\frac{L^2}2\right)^2+\left(w-\frac{W^2}2\right)^2\right)\,\mathrm{d}h\,\mathrm{d}l\,\mathrm{d}w\\
&=\rho{}H\int_0^W\!\int_0^L\!\left(l^2-Ll+\frac{L^2}4+w^2-Ww+\frac{W^2}4\right)\,\mathrm{d}l\,\mathrm{d}w\\
&=\rho{}H\int_0^W\!\left(\frac13L^3-\frac12L^3+\frac14L^3+Lw^2-LWw+\frac14LW^2\right)\,\mathrm{d}w\\
&=\rho{}HL\int_0^W\!\left(\frac1{12}L^2+w^2-Ww+\frac14W^2\right)\,\mathrm{d}w\\
&=\rho{}HL\left(\frac1{12}L^2W+\frac13W^3-\frac12W^3+\frac14W^3\right)\,\mathrm{d}w\\
&=\rho{}HLW\left(\frac1{12}L^2+\frac1{12}W^2\right)\\
&=\frac1{12}m\left(L^2+W^2\right)\\
I_L&=\frac1{12}m\left(H^2+W^2\right)\\
I_W&=\frac1{12}m\left(L^2+H^2\right)\\
\end{aligned}$ <!--SR:!2024-05-25,157,310-->

### cylindrical shell, axis through base center

- definition ::@:: a homogeneous [cylindrical](cylinder.md) shell of density $\rho$, height $H$, inner radius $R_I$, and outer radius $R_O$, axis through base center <!--SR:!2025-08-28,361,307!2026-11-02,699,347-->
- equation ::@:: $I=\frac12m\left(R_O^2+R_I^2\right)$ <!--SR:!2025-11-10,532,310!2026-10-22,726,338-->
  - solid cylinder ::@:: $I=\frac12mR_O^2$ <!--SR:!2026-12-15,831,330!2025-02-12,258,338-->
  - thin-walled hollow cylinder ::@:: $I=mR_O^2$ <!--SR:!2025-09-15,492,310!2026-12-11,720,338-->
- proof: $$\begin{aligned}
m&=\rho\pi{}H\left(R_O^2-R_I^2\right)\\
I&=\int_{R_I}^{R_O}\!\int_0^H\!\int_0^{2\pi}\!\rho{}r^3\,\mathrm{d}\theta\,\mathrm{d}h\,\mathrm{d}r\\
&=2\rho\pi{}H\int_{R_I}^{R_O}\!r^3\,\mathrm{d}r\\
&=\frac12\rho\pi{}H\left[r^4\right]_{R_I}^{R_O}\\
&=\frac12\rho\pi{}H\left(R_O^4-R_I^4\right)\\
&=\frac12\rho\pi{}H\left(R_O^2-R_I^2\right)\left(R_O^2+R_I^2\right)\\
&=\frac12m\left(R_O^2+R_I^2\right)
\end{aligned}$ <!--SR:!2024-10-12,282,330-->

### rod, axis through certain distance from one end

- definition ::@:: a homogeneous rod of density $\rho$, length $L$, and radius $R$, axis through distance $Z$ from one end <!--SR:!2027-04-09,853,347!2025-06-07,357,367-->
- equation ::@:: $I=\frac13m\left(L^2-3LZ+3Z^2\right)+\frac14mR^2$ <!--SR:!2025-03-14,83,210!2025-08-30,360,298-->
  - thin rod correction ::@:: use the same equation and set $R = 0$ <!--SR:!2028-06-14,1330,350!2025-04-10,311,358-->
  - slender rod, axis through center ::@:: $\frac1{12}mL^2$ <!--SR:!2025-04-21,406,310!2026-05-15,566,318-->
  - slender rod, axis through one end ::@:: $\frac13mL^2$ <!--SR:!2025-04-17,367,290!2026-08-21,674,338-->
- proof: $$\begin{aligned}
m&=\rho\pi{}R^2L\\
I&=\int_0^L\!\int_0^R\!\int_0^{2\pi}\!\rho\left(r^2\cos^2\theta+(z-Z)^2\right)r\,\mathrm{d}\theta\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\!\int_0^R\!\int_0^{2\pi}\!\left(\frac12r^3+\frac12r^3\cos2\theta+r(z-Z)^2\right)\,\mathrm{d}\theta\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\!\int_0^R\!\left[\frac12r^3\theta+\frac14r^3\sin2\theta+r(z-Z)^2\theta\right]_{\theta=0}^{\theta=2\pi}\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\!\int_0^R\!\left(\pi{}r^3+2\pi{}r(z-Z)^2\right)\,\mathrm{d}r\,\mathrm{d}z\\
&=\pi\rho\int_0^L\!\left[\frac14r^4+r^2(z-Z)^2\right]_{r=0}^{r=R}\,\mathrm{d}z\\
&=\pi\rho\int_0^L\!\left(\frac14R^4+R^2(z-Z)^2\right)\,\mathrm{d}z\\
&=\pi\rho\left[\frac14R^4z+\frac13R^2(z-Z)^3\right]_{z=0}^{z=L}\\
&=\frac14\pi\rho{}R^4L+\frac13\pi\rho{}R^2\left((L-Z)^3+Z^3\right)\\
&=\frac14mR^2+\frac13\pi\rho{}R^2(L-Z+Z)\left((L-Z)^2-Z(L-Z)+Z^2\right)\\
&=\frac14mR^2+\frac13m\left(L^2-2LZ+Z^2-LZ+Z^2+Z^2\right)\\
&=\frac13m\left(L^2-3LZ+3Z^2\right)+\frac14mR^2
\end{aligned}$
  - shitty coordinates ([Cartesian coordinates](Cartesian%20coordinate%20system.md)) proof: $\begin{aligned}
m&=\rho\pi{}R^2L\\
I&=\int_0^L2\!\int_0^R2\!\rho\sqrt{R^2-r^2}\left(r^2+(l-Z)^2\right)\,\mathrm{d}r\,\mathrm{d}l\\
&=4\rho\int_0^L\!\left(\int_0^Rr^2\!\sqrt{R^2-r^2}\,\mathrm{d}r+(l-Z)^2\int_0^R\!\sqrt{R^2-r^2}\,\mathrm{d}r\right)\,\mathrm{d}l\\
&=4\rho\int_0^L\!\left(R^3\int_0^\frac\pi2\!\sin^2\theta\cos\theta\sqrt{R^2-R^2\sin^2\theta}\,\mathrm{d}\theta+R(l-Z)^2\int_0^\frac\pi2\!\cos\theta\sqrt{R^2-R^2\sin^2\theta}\,\mathrm{d}\theta\right)\,\mathrm{d}l && \left(r\overset{\text{def} }=R\sin\theta,\theta\in\left[-\frac\pi2,\frac\pi2\right]\right)\\
&=4\rho\int_0^L\!\left(R^4\int_0^\frac\pi2\!\sin^2\theta\cos^2\theta\,\mathrm{d}\theta+R^2(l-Z)^2\int_0^\frac\pi2\!\cos^2\theta\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=4\rho{}R^2\int_0^L\!\left(\frac14R^2\int_0^\frac\pi2\!\sin^22\theta\,\mathrm{d}\theta+\frac12(l-Z)^2\int_0^\frac\pi2\!(1+\cos2\theta)\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\!\left(\frac12\int_0^\frac\pi2\!(1-\cos4\theta)\,\mathrm{d}\theta+2R^2(l-Z)^2\int_0^\frac\pi2\!(1+\cos2\theta)\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\!\left(\frac12R^2\left[\theta-\frac14\sin4\theta\right]_0^\frac\pi2+2(l-Z)^2\left[\theta+\frac12\sin2\theta\right]_0^\frac\pi2\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\!\left(\frac\pi4R^2+\pi{}(l-Z)^2\right)\,\mathrm{d}l\\
&=\rho{}R^2\left[\frac\pi4R^2l+\frac\pi3(l-Z)^3\right]_{l=0}^{l=L}\\
&=\frac\pi4\rho{}R^4L+\frac\pi3\rho{}R^2\left((L-Z)^3+Z^3\right)\\
&=\frac14mR^2+\frac\pi3\rho{}R^2(L-Z+Z)\left((L-Z)^2-Z(L-Z)+Z^2\right)\\
&=\frac14mR^2+\frac13m\left(L^2-2LZ+Z^2-LZ+Z^2+Z^2\right)\\
&=\frac13m\left(L^2-3LZ+3Z^2\right)+\frac14mR^2
\end{aligned}$ <!--SR:!2024-09-27,269,330-->

### spherical shell, axis through center

- definition ::@:: a homogeneous [spherical](sphere.md) shell of density $\rho$, inner radius $R_I$, and outer radius $R_O$, axis through center <!--SR:!2025-02-01,251,347!2025-08-05,404,367-->
- equation ::@:: $I=\frac25m\frac{R_O^5-R_I^5}{R_O^3-R_I^3}$ <!--SR:!2025-02-19,279,250!2026-04-30,539,318-->
  - solid sphere ::@:: $I=\frac25mR_O^2$ <!--SR:!2026-01-26,573,310!2025-10-06,386,298-->
  - thin-walled hollow sphere ::@:: $I=\frac25m\lim_{r_I\to{}R_O}\frac{R_O^5-r_I^5}{R_O^3-r_I^3}=\frac25m\lim_{r_I\to{}R_O}\frac{5r_I^4}{3r_I^2}=\frac23mR_O^2$ <!--SR:!2027-07-10,893,290!2025-05-18,288,298-->
- proof: $$\begin{aligned}
m&=\frac43\rho\pi\left(R_O^3-R_I^3\right)\\
I&=\int_{R_I}^{R_O}\!\int_0^{2\pi}\!\int_0^\pi\!\rho{}r^4\sin^3\theta\,\mathrm{d}\theta\,\mathrm{d}\phi\,\mathrm{d}r\\
&=-\rho\int_{R_I}^{R_O}\!r^4\int_0^{2\pi}\!\int_{\theta=0}^{\theta=\pi}\!\left(1-\cos^2\theta\right)\,\mathrm{d}\!(\cos\theta)\,\mathrm{d}\phi\,\mathrm{d}r\\
&=-\rho\int_{R_I}^{R_O}\!r^4\int_0^{2\pi}\!\left[\cos\theta-\frac13\cos^3\theta\right]_0^\pi\,\mathrm{d}\phi\,\mathrm{d}r\\
&=-\rho\int_{R_I}^{R_O}\!r^4\int_0^{2\pi}\!\left(-1+\frac13-1+\frac13\right)\,\mathrm{d}\phi\,\mathrm{d}r\\
&=\frac43\rho\int_{R_I}^{R_O}\!r^4\int_0^{2\pi}\!\mathrm{d}\phi\,\mathrm{d}r\\
&=\frac83\pi\rho\int_{R_I}^{R_O}\!r^4\,\mathrm{d}r\\
&=\frac8{15}\pi\rho\left[r^5\right]_{R_I}^{R_O}\\
&=\frac8{15}\pi\rho\left(R_O^5-R_I^5\right)\\
&=\frac25m\frac{R_O^5-R_I^5}{R_O^3-R_I^3}
\end{aligned}$$ <!--SR:!2024-06-11,170,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/list_of_moments_of_inertia) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
