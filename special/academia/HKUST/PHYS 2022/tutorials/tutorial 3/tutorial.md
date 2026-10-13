---
aliases:
  - HKUST PHYS 2022 tutorial 3 tutorial
  - PHYS 2022 tutorial 3 tutorial
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/tutorials/tutorial_3/tutorial
  - language/in/English
---

# tutorial

- HKUST PHYS 2022 tutorial 3
- parent: [tutorial 3](index.md)

---

- title: Tutorial 3
- points: 20
- grade: 20/20
- submitting: \[missing\]

---

No additional details were added for this assignment.

## problems

> Problem:
>
> __1.__ XRD pattern of BaF $_2$ using Cu-K $\alpha$ radiation ($\lambda = 1.5418\ \text{Å}$) is shown below. Calculate the lattice parameter $a$ of BaF $_2$ using (200) and (220) peaks.
>
> The pattern plots intensity in arbitrary units against $2\theta$ from $10°$ to $90°$, labels eleven peaks (111), (200), (220), (311), (222), (400), (331), (420), (422), (511), (440), and its legend reads BaF $_2$ $0.08\ \text{mol}\%$ ErF $_2$.
>
> The $2\theta$ are $29°$ for (200) and $41°$ for (220).
>
> - solution: {@{Bragg's law $\lambda = 2d\sin\theta$}@} at $\theta = 14.5°$ gives {@{$d_{200} = \lambda/(2\sin 14.5°) = 3.080\ \text{Å}$ and $a = 2d_{200} = 6.16\ \text{Å}$}@}. The same law at $\theta = 20.5°$ gives {@{$d_{220} = \lambda/(2\sin 20.5°) = 2.201\ \text{Å}$ and $a = d_{220}\sqrt{8} = 6.23\ \text{Å}$}@}. The two readings {@{average to $a \approx 6.19\ \text{Å}$}@}.
> - explanation: {@{Bragg's law}@} turns {@{a peak position into a plane spacing}@}: {@{$d = \lambda/(2\sin\theta)$}@}. In {@{a cubic crystal}@} the lattice parameter follows from {@{$a = d_{hkl}\sqrt{h^2+k^2+l^2}$}@}, so the (200) peak {@{returns $a = 2d$}@} and the (220) peak {@{multiplies $d$ by $\sqrt{8}$}@}. The two readings differ by {@{about $1\%$, since each $2\theta$ was read to the nearest degree}@}, and their mean matches {@{the accepted $6.20\ \text{Å}$ for BaF $_2$}@}.

<!-- markdownlint MD028 -->

> __2.__ In an electron gun, electrons are accelerated using a voltage. Calculate the voltage to produce an electron beam with wavelength equivalent to Cu-K $\alpha$ X-ray wavelength. ($\lambda = 1.5418\ \text{Å}$)
>
> - solution: the accelerating voltage is {@{$V = h^2/(2me\lambda^2) \approx 63.3\ \text{V}$}@}
> - explanation: {@{The de Broglie wavelength}@} is {@{$\lambda = h/p$}@}, and {@{accelerating the electron through $V$}@} gives {@{it momentum $p = \sqrt{2meV}$}@}. Eliminating $p$ between the two leaves {@{$V = h^2/(2me\lambda^2)$}@}, the same as the shortcut {@{$V = (12.27\ \text{V}^{1/2}\text{Å}/\lambda)^2$ for $\lambda$ in Ångströms}@}.
