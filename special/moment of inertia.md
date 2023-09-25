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

### homogeneous slender rod, axis through center


### homogeneous slender rod, axis through one end

- definition: a homogeneous slender rod {{of density $\rho$, length $L$, and radius $R$}}
- prove: $$\begin{aligned}
M&=\rho\pi{}R^2L\\
L&=\frac{M}{\rho\pi{}R^2}\\
I&=\int_0^L\int_0^R2\rho\pi{}r\left(r^2+l^2\right)\,\mathrm{d}r\,\mathrm{d}l\\
&=\int_0^L\int_{r=0}^{r=R}\rho\pi\left(r^2+l^2\right)\,\mathrm{d}\left(r^2\right)\,\mathrm{d}l\\
&=\int_0^L\left[\frac12\rho\pi{}r^4+\rho\pi{}l^2r^2\right]_{r=0}^{r=R}\,\mathrm{d}l\\
&=\int_0^L\left(\frac12\rho\pi{}R^4+\rho\pi{}l^2R^2\right)\,\mathrm{d}l\\
&=\left[\frac12\rho\pi{}R^4l+\frac13\rho\pi{}l^3R^2\right]_{l=0}^{l=L}\\
&=\frac12\rho\pi{}R^4L+\frac13\rho\pi{}L^3R^2\\
&=\rho\pi{}R^2L\left(\frac12R^2+\frac13L^2\right)
\end{aligned}$$
