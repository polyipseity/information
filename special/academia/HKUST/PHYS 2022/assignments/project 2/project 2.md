---
aliases:
  - HKUST PHYS 2022 project 2 notes
  - HKUST PHYS2022 project 2 notes
  - PHYS 2022 project 2 notes
  - PHYS2022 project 2 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_2/project_2
  - language/in/English
---

# project 2

- HKUST PHYS 2022 project 2
- parent: [project 2](index.md)

Project 2 runs two experiments side by side: the spectrum a hot body emits, and the electrons light frees from a metal surface. Each experiment sweeps one parameter across five values, plots the measured quantity against it, and reads a formula off the plot. The full treatments live in [black-body radiation](../../black-body%20radiation.md) and [photoelectric effect](../../photoelectric%20effect.md).

---

Flashcards for this section are as follows:

- overview: the two experiments of project 2 ::@:: The spectrum a hot body emits at different temperatures, and the electrons light frees from a metal surface at different frequencies and intensities.
- the method both experiments share ::@:: Sweep one parameter across five values, plot the measured quantity against it, and read a formula off the plot.

## black-body radiation

A black body is held at ten temperatures in turn. At each temperature three numbers are taken: the wavelength where the spectrum peaks, the intensity at that peak, and the total intensity across the whole spectrum.

Each number follows its own power of the temperature. The peak wavelength falls as $\lambda_{\max} = b/T$ with Wien's displacement constant $b = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$: twice the temperature, half the peak wavelength. The peak intensity rises as the fifth power of the temperature, and the total intensity rises as the fourth power, which is the Stefan–Boltzmann law.

The fifth and fourth powers differ because the peak itself moves. The peak sits at $\lambda_{\max} \propto 1/T$, so evaluating the spectrum there brings one extra factor of $T$; integrating over every wavelength, as the total does, leaves the fourth power alone.

---

Flashcards for this section are as follows:

- overview: the peak wavelength $\lambda_{\max}$, the peak intensity, and the total intensity of a black body, each against the absolute temperature $T$: how does each scale ::@:: The peak wavelength, which falls as $b/T$; the peak intensity, which rises as $T^5$; and the total intensity, which rises as $T^4$.
- Wien's displacement law as a plot of peak wavelength against temperature ::@:: $\lambda_{\max} = b/T$ with $b = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$: the peak moves to shorter wavelengths in inverse proportion to the absolute temperature. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the peak intensity of a black-body spectrum against the absolute temperature $T$ ::@:: Proportional to the fifth power of the absolute temperature, $T^5$.
- the total intensity of a black-body spectrum against temperature (the Stefan–Boltzmann law) ::@:: Proportional to the fourth power of the absolute temperature, $T^4$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the peak intensity scales as $T^5$ while the total scales as $T^4$ ::@:: The peak sits at $\lambda_{\max} \propto 1/T$, so the spectrum evaluated there carries one extra factor of $T$; the integral over wavelength does not.

## photoelectric effect

Light falls on a metal surface and frees electrons. For sodium the stopping voltage is measured at five colours, which sets the frequency, and then the photocurrent is measured at five intensities with no retarding voltage; zinc, copper, and platinum repeat both sweeps.

The stopping voltage against frequency is a straight line, $V_s = (h/e)f - \Phi/e$, where $\Phi$ is the metal's work function. Its slope $h/e$ is the same for every metal, and its intercept fixes the work function; a larger work function pushes the line down and moves the threshold frequency $f_0 = \Phi/h$ up. The photocurrent against intensity, at a fixed frequency above threshold, runs straight through the origin: the current is proportional to the intensity, and it stays zero below the threshold whatever the intensity.

---

Flashcards for this section are as follows:

- overview: what the photoelectric experiment measures against frequency and against intensity ::@:: The stopping voltage against the light frequency, and the photocurrent against the light intensity above threshold.
- the stopping voltage against frequency for a metal with work function $\Phi$ ::@:: A straight line $V_s = (h/e)f - \Phi/e$: slope $h/e$, the same for every metal, and intercept $-\Phi/e$, set by the metal.
- sodium, zinc, copper, and platinum: the order of their work functions $\Phi$ ::@:: Sodium about $2.3\ \text{eV}$, then zinc at $4.3$, copper at $4.7$, and platinum at $6.35$: the larger the work function, the higher the threshold frequency $f_0 = \Phi/h$.
- the photocurrent against light intensity at a fixed frequency above threshold ::@:: Proportional to the intensity, through the origin; below the threshold frequency the current stays zero at every intensity.
- what the equal slopes $h/e$ of the stopping-voltage lines across metals show ::@:: The slope is $h/e$ everywhere: the photon energy $hf$ is universal, and each metal contributes only its work function $\Phi$.
