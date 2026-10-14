---
aliases:
  - HKUST PHYS 2022 project 4 notes
  - HKUST PHYS2022 project 4 notes
  - PHYS 2022 project 4 notes
  - PHYS2022 project 4 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_4/project_4
  - language/in/English
---

# project 4

- HKUST PHYS 2022 project 4
- parent: [project 4](index.md)

Project 4 measures the wavelength that particles carry. Electrons fired through two slits leave an interference pattern whose fringe spacing fixes their wavelength; the same wavelength is then read straight off the wave function one particle at a time. Sweeping the gun velocity, and repeating everything for neutrons and helium atoms, turns the measurements into one formula. The full treatment lives in [matter wave](../../matter%20wave.md).

---

Flashcards for this section are as follows:

- overview: what project 4 measures, and for which particles ::@:: The de Broglie wavelength from interference fringes and from the single-particle wave function, for electrons, neutrons, and helium atoms at five gun velocities each.
- the two ways project 4 reads a particle's wavelength ::@:: From the fringe spacing of a double-slit interference pattern, and directly from the wave function of a single particle.

## wavelength from interference

A gun fires electrons through two slits onto a distant screen, and the fringes of the accumulated pattern sit at a spacing $\Delta x = \lambda L/d$, set by the slit separation $d$ and the screen distance $L$. Reading $\Delta x$ off the pattern returns the wavelength, $\lambda = \Delta x\, d/L$, at each of five gun velocities.

The same five velocities are then run in single-particle mode, where only one particle is in flight at a time and the real part of its wave function is displayed. The measuring tape measures the wavelength along that wave function, and it matches the wavelength the fringes gave. One particle interferes with itself: the wave whose wavelength the tape reads is the wave whose interference the fringes record. The simulation prints its own velocity and wavelength values, but the wavelength stays a measurement, taken from the tape rather than read off the display. The older version of the simulation remains usable, and its wavelength readout runs about twice the true value, since it displays the wave's amplitude rather than its length.

---

Flashcards for this section are as follows:

- overview: how the fringe spacing $\Delta x$ of a double-slit pattern yields a wavelength ::@:: The fringe spacing $\Delta x = \lambda L/d$ inverts to $\lambda = \Delta x\, d/L$, with slit separation $d$ and screen distance $L$.
- comparing the fringe-derived wavelength with the wave-function wavelength at the same gun velocity ::@:: They match, so the wave function of a single particle carries the wavelength whose interference the accumulated fringes show.
- what the match between the two measurements establishes ::@:: One particle interferes with itself: the wave the measuring tape reads off its wave function is the wave the double-slit fringes record.
- the tool that gives the wavelength in single-particle mode, where the simulation also prints its own values ::@:: The measuring tape: the wavelength comes from the measurement, not from the display.
- the older simulation version's wavelength readout ::@:: About twice the true value, since it shows the wave's amplitude rather than its length; the version itself remains usable.

## de Broglie relation

Plotting the measured wavelength against the gun velocity gives a falling curve, and the same curve serves every particle type once mass enters. One relation covers all of it: $\lambda = h/(mv)$, the de Broglie wavelength of a particle of mass $m$ moving at speed $v$.

At fixed mass the wavelength falls as the inverse of the speed, so doubling the velocity halves the wavelength. At fixed speed it falls as the inverse of the mass: the electrons of the same velocity setting carry the longest wavelength, the neutrons the next, and the helium atoms the shortest, because helium's nucleus is the heaviest of the three.

---

Flashcards for this section are as follows:

- overview: the relation $\lambda = h/(mv)$ every measurement of project 4 collapses onto ::@:: $\lambda = h/(mv)$, the de Broglie wavelength of a particle of mass $m$ at speed $v$.
- the de Broglie wavelength of a particle of mass $m$ moving at speed $v$ ::@:: $\lambda = h/(mv)$: inverse in the speed at fixed mass, inverse in the mass at fixed speed.
- at the same velocity setting $v$, electrons, neutrons, and helium atoms of masses $m$: the order of their wavelengths $\lambda$ ::@:: Electrons longest, neutrons next, helium atoms shortest, since $\lambda \propto 1/m$.
- doubling a particle's velocity $v$ at fixed mass $m$: what happens to its de Broglie wavelength $\lambda$ ::@:: It halves, since $\lambda \propto 1/v$.
