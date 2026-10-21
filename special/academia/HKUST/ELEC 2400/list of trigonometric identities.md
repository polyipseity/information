---
aliases:
  - ELEC 2400 list of trigonometric identities
  - ELEC2400 list of trigonometric identities
  - HKUST ELEC 2400 list of trigonometric identities
  - HKUST ELEC2400 list of trigonometric identities
  - trig identities
  - trigonometric identities
  - trigonometric identity
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/list_of_trigonometric_identities
  - language/in/English
---

# list of trigonometric identities

Four trigonometric moves carry sinusoidal steady-state work: adding two angles, multiplying two sinusoids, squaring one, and adding two of them. Each move has its identity, and the same small set covers the capacitor and inductor derivations, the root-mean-square value, the average power, and the switch between sine and cosine references ([sine wave](sine%20wave.md), [phasor](phasor.md)).

---

Flashcards for this section are as follows:

- why these identities: which four moves does sinusoidal analysis need? ::@:: Adding two angles, multiplying two sinusoids, squaring one sinusoid, and adding two sinusoids at one frequency.

## angles added and subtracted

The sum formulas expand an angle that is itself a sum: $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$ and $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$. Only the cosine flips the sign of its second term, which follows from its derivative being minus the sine.

A quarter turn converts one function into the other, $\cos\theta = \sin\left(\theta + \pi/2\right)$ and $\sin\theta = \cos\left(\theta - \pi/2\right)$. That pair is what turns a derivative back into a cosine, $\frac{d}{dt}V_p\cos\omega t = -\omega V_p\sin\omega t = \omega V_p\cos\left(\omega t + \pi/2\right)$. The capacitor current's lead of $90^\circ$ is read off that line.

---

Flashcards for this section are as follows:

- angles added and subtracted / the cosine sum: how does $\cos(\alpha \pm \beta)$ expand? ::@:: $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$; the second term takes the opposite sign.
- angles added and subtracted / the sine sum: how does $\sin(\alpha \pm \beta)$ expand? ::@:: $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$.
- angles added and subtracted / sine to cosine: how is a sine written as a cosine? ::@:: $\sin\theta = \cos\left(\theta - \pi/2\right)$, a quarter cycle behind the cosine. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- angles added and subtracted / cosine to sine: how is a cosine written as a sine? ::@:: $\cos\theta = \sin\left(\theta + \pi/2\right)$, a quarter cycle ahead of the sine. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- angles added and subtracted / the derivative: how does the derivative of $V_p\cos\omega t$ come back as a cosine? ::@:: $-\omega V_p\sin\omega t = \omega V_p\cos\left(\omega t + \pi/2\right)$, using $\sin x = \cos\left(x - \pi/2\right)$.

## products of sinusoids

A product of two sinusoids splits into a constant and a term at twice the frequency. Three pairings matter here: $\cos A\cos B = \frac{1}{2}\left[\cos(A - B) + \cos(A + B)\right]$, $\sin A\sin B = \frac{1}{2}\left[\cos(A - B) - \cos(A + B)\right]$, and $\sin A\cos B = \frac{1}{2}\left[\sin(A + B) + \sin(A - B)\right]$.

Cosine times cosine carries the power algebra. A voltage $V_p\cos\omega t$ multiplied by a current $I_p\cos(\omega t - \phi)$ leaves $\frac{1}{2}V_pI_p\cos\phi$ plus a term at $2\omega$, so the average power is the constant part ([AC power](AC%20power.md)).

---

Flashcards for this section are as follows:

- products of sinusoids / cosine times cosine: how does $\cos A\cos B$ expand? ::@:: $\cos A\cos B = \frac{1}{2}\left[\cos(A - B) + \cos(A + B)\right]$: the difference of the angles gives the constant part and their sum the part at twice the frequency.
- products of sinusoids / sine times sine: how does $\sin A\sin B$ expand? ::@:: $\sin A\sin B = \frac{1}{2}\left[\cos(A - B) - \cos(A + B)\right]$, the same pair with the doubled-frequency term subtracted.
- products of sinusoids / sine times cosine: how does $\sin A\cos B$ expand? ::@:: $\sin A\cos B = \frac{1}{2}\left[\sin(A + B) + \sin(A - B)\right]$, a pair of sines rather than cosines.
- products of sinusoids / the power use: which product gives the average power, and what does it leave? ::@:: $\cos A\cos B$: a voltage and a current a phase $\phi$ apart leave the constant $\frac{1}{2}V_pI_p\cos\phi$ plus a ripple at $2\omega$ that averages to zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## squares and double angles

Squaring a sinusoid is the product case with $A = B$: $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$ and $\sin^2\theta = \frac{1 - \cos 2\theta}{2}$, which are the double-angle formulas read backwards. Over a cycle the $\cos2\theta$ term averages away, so either square has mean one half. That half is why the root-mean-square value of a sinusoid is its peak divided by $\sqrt{2}$ ([AC power](AC%20power.md)).

---

Flashcards for this section are as follows:

- squares and double angles / cosine squared: how does $\cos^2\theta$ expand, and what does that say about its mean? ::@:: $\cos^2\theta = \frac{1 + \cos2\theta}{2}$; the doubled-frequency term averages to zero over a cycle, so the mean is one half.
- squares and double angles / sine squared: how does $\sin^2\theta$ expand, and what does that say about its mean? ::@:: $\sin^2\theta = \frac{1 - \cos2\theta}{2}$, whose mean over a cycle is also one half.
- squares and double angles / the root-mean-square use: why is the root-mean-square value of a sinusoid its peak over $\sqrt{2}$? ::@:: The mean of the squared sinusoid is exactly half its squared peak, and the square root of that is the peak divided by $\sqrt{2}$.

## sums of sinusoids

Two sinusoids at the same frequency add into one: $\cos A + \cos B = 2\cos\frac{A + B}{2}\cos\frac{A - B}{2}$, and $\sin A + \sin B = 2\sin\frac{A + B}{2}\cos\frac{A - B}{2}$. The result keeps the mean angle and is modulated at half the difference, so two nearby frequencies beat.

One cosine plus one sine at the same frequency collapses into a single cosine, $a\cos\theta + b\sin\theta = \sqrt{a^2 + b^2}\cos\left(\theta - \phi\right)$ with $\phi = \tan^{-1}\left(b/a\right)$ taken in the quadrant of $(a, b)$. That root and that angle are the magnitude and the phase of the sum phasor. The same step takes a complex amplitude to the pair of numbers a waveform is written with ([phasor](phasor.md)).

---

Flashcards for this section are as follows:

- sums of sinusoids / two cosines: how does $\cos A + \cos B$ collapse? ::@:: $\cos A + \cos B = 2\cos\frac{A + B}{2}\cos\frac{A - B}{2}$, one cosine at the mean angle modulated by half the difference.
- sums of sinusoids / two sines: how does $\sin A + \sin B$ collapse? ::@:: $\sin A + \sin B = 2\sin\frac{A + B}{2}\cos\frac{A - B}{2}$.
- sums of sinusoids / cosine plus sine: how does $a\cos\theta + b\sin\theta$ collapse, and what are the two quantities? ::@:: Into $\sqrt{a^2 + b^2}\cos\left(\theta - \phi\right)$ with $\phi = \tan^{-1}\left(b/a\right)$ in the quadrant of $(a, b)$: the magnitude and the phase of the sum phasor.

## quarter and half turns

Phasor arithmetic performs two rotations of its own, and both are worth knowing by heart. A quarter turn sends $\cos\theta$ to $-\sin\theta$ and $\sin\theta$ to $\cos\theta$, that is $\cos\left(\theta + \pi/2\right) = -\sin\theta$ and $\sin\left(\theta + \pi/2\right) = \cos\theta$. A half turn negates both, $\cos\left(\theta + \pi\right) = -\cos\theta$ and $\sin\left(\theta + \pi\right) = -\sin\theta$.

Multiplying by $j$ is a quarter turn and multiplying by $-1$ is a half turn, so these are the values a phasor picks up when it is differentiated or negated ([Euler's formula](Euler%27s%20formula.md)).

---

Flashcards for this section are as follows:

- quarter and half turns / the quarter turn: what do a cosine and a sine become when their angle gains $\pi/2$? ::@:: $\cos\left(\theta + \pi/2\right) = -\sin\theta$ and $\sin\left(\theta + \pi/2\right) = \cos\theta$: the pair rotates a quarter turn.
- quarter and half turns / the half turn: what do a cosine and a sine become when their angle gains $\pi$? ::@:: $\cos\left(\theta + \pi\right) = -\cos\theta$ and $\sin\left(\theta + \pi\right) = -\sin\theta$: both are negated.
- quarter and half turns / the phasor reading: which two complex factors produce the quarter turn and the half turn? ::@:: $j$ for the quarter turn and $-1$ for the half turn, so the two rotations are multiplication by those factors. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
