---
aliases:
  - ELEC 2100 in-class online quiz 3
  - ELEC 2100 quiz 3
  - HKUST ELEC 2100 in-class online quiz 3
  - HKUST ELEC 2100 quiz 3
tags:
  - date/2026/03/31
  - flashcard/active/special/academia/HKUST/ELEC_2100/questions/quiz_3
  - language/in/English
---

# quiz 3

- HKUST ELEC 2100
- parent: [questions](index.md)

---

- type: in-class online quiz
- due: 2026-03-31T13:22:59+08:00
- points: 5
- questions: 5
- available: 2026-03-31T13:00:00+08:00/2026-03-31T13:22:59+08:00, PT22M59S
- time limit: PT20M

## hints

1. In the question with $H(\omega)=e^{-j5\omega}$ and a real band-limited input, what kind of wrong output claim should you reject first? ::@:: Reject any claim that the system creates a brand-new sinusoid, because an all-pass delay only shifts the existing waveform in time. <!--SR:!2026-05-13,14,290!2026-05-13,14,290-->
2. In the question where $X(\omega)$ simplifies to a real even function like $1/(\omega^2+4)$, what option should look suspicious? ::@:: The suspicious choice is the one claiming the time-domain signal is complex, because a real even spectrum points to a real even signal. <!--SR:!2026-05-13,14,290!2026-05-13,14,290-->
3. In the multiple-choice delay question, imagine choices like a unit-magnitude exponential, a frequency spike, a real slope, and a differentiator law; what feature should the correct $H(\omega)$ have? ::@:: A pure delay keeps unit magnitude and contributes only a phase term that is linear in $\omega$. <!--SR:!2026-05-13,14,290!2026-05-13,14,290-->
4. When shifting signals using a mixer, how do we choose a carrier frequency that moves the content to a new band while leaving a "waste" copy at baseband for easy removal? ::@:: A carrier frequency equal to the original center frequency. Because modulation creates both sum and difference frequencies, using $f_c$ equal to the signal's current position shifts one copy to the double-frequency target ($\pm 2 f_c$ kHz) and the other copy to baseband ($0$ Hz), where an LTI filter can easily reject it. <!--SR:!2026-05-13,14,290!2026-05-13,14,290-->
5. In the Fourier-transform-properties question, what theorem direction must you not reverse? ::@:: Time-domain convolution corresponds to frequency-domain multiplication; if someone says filtering means convolving the spectra, that is the incorrect swap. <!--SR:!2026-05-13,14,290!2026-05-13,14,290-->
