---
aliases:
  - angular mass
  - second moment of mass
  - mass moment of inertia
  - moment of inertia
  - rotational inertia
tags:
  - flashcards/special/moment_of_inertia
---

# moment of inertia

## examples

### homogeneous thick rod, axis through one end

- definition: a homogeneous thick rod {{of density $\rho$, length $L$, and radius $R$}}, axis through one end
- equation: {{$I=\frac13ML^2+\frac14MR^2$}}
- proof:
  - okay coordinates ([cylindrical coordinates](../general/cylindrical%20coordinate%20system.md)) proof: $$\begin{aligned}
M&=\rho\pi{}R^2L\\
I&=\int_0^L\int_0^R\int_0^{2\pi}\rho\left(r^2\cos^2\theta+z^2\right)r\,\mathrm{d}\theta\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\int_0^R\int_0^{2\pi}\left(\frac12r^3+\frac12r^3\cos2\theta+rz^2\right)\,\mathrm{d}\theta\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\int_0^R\left[\frac12r^3\theta+\frac14r^3\sin2\theta+rz^2\theta\right]_{\theta=0}^{\theta=2\pi}\,\mathrm{d}r\,\mathrm{d}z\\
&=\rho\int_0^L\int_0^R\left(\pi{}r^3+2\pi{}rz^2\right)\,\mathrm{d}r\,\mathrm{d}z\\
&=\pi\rho\int_0^L\left[\frac14r^4+r^2z^2\right]_{r=0}^{r=R}\,\mathrm{d}z\\
&=\pi\rho\int_0^L\left(\frac14R^4+R^2z^2\right)\,\mathrm{d}z\\
&=\pi\rho\left[\frac14R^4z+\frac13R^2z^3\right]_{z=0}^{z=L}\\
&=\frac14\pi\rho{}R^4L+\frac13\pi\rho{}R^2L^3\\
&=\frac14MR^2+\frac13ML^2
\end{aligned}$$
  - shitty coordinates ([Cartesian coordinates](../general/Cartesian%20coordinate%20system.md)) proof: $$\begin{aligned}
M&=\rho\pi{}R^2L\\
I&=\int_0^L2\int_0^R2\rho\sqrt{R^2-r^2}\left(r^2+l^2\right)\,\mathrm{d}r\,\mathrm{d}l\\
&=4\rho\int_0^L\left(\int_0^Rr^2\sqrt{R^2-r^2}\,\mathrm{d}r+l^2\int_0^R\sqrt{R^2-r^2}\,\mathrm{d}r\right)\,\mathrm{d}l\\
&=4\rho\int_0^L\left(R^3\int_0^\frac\pi2\sin^2\theta\cos\theta\sqrt{R^2-R^2\sin^2\theta}\,\mathrm{d}\theta+Rl^2\int_0^\frac\pi2\cos\theta\sqrt{R^2-R^2\sin^2\theta}\,\mathrm{d}\theta\right)\,\mathrm{d}l&\left(r\overset{\text{def}}=R\sin\theta,\theta\in\left[-\frac\pi2,\frac\pi2\right]\right)\\
&=4\rho\int_0^L\left(R^4\int_0^\frac\pi2\sin^2\theta\cos^2\theta\,\mathrm{d}\theta+R^2l^2\int_0^\frac\pi2\cos^2\theta\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=4\rho{}R^2\int_0^L\left(\frac14R^2\int_0^\frac\pi2\sin^22\theta\,\mathrm{d}\theta+\frac12l^2\int_0^\frac\pi2(1+\cos2\theta)\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\left(\frac12\int_0^\frac\pi2(1-\cos4\theta)\,\mathrm{d}\theta+2R^2l^2\int_0^\frac\pi2(1+\cos2\theta)\,\mathrm{d}\theta\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\left(\frac12R^2\left[\theta-\frac14\sin4\theta\right]_0^\frac\pi2+2l^2\left[\theta+\frac12\sin2\theta\right]_0^\frac\pi2\right)\,\mathrm{d}l\\
&=\rho{}R^2\int_0^L\left(\frac\pi4R^2+\pi{}l^2\right)\,\mathrm{d}l\\
&=\rho{}R^2\left[\frac\pi4R^2l+\frac\pi3l^3\right]_{l=0}^{l=L}\\
&=\frac\pi4\rho{}R^4L+\frac\pi3\rho{}R^2L^3\\
&=\frac14MR^2+\frac13ML^2
\end{aligned}$$
