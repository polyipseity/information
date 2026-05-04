---
aliases:
  - ELEC 2100 online quiz 2
  - ELEC 2100 quiz 2
  - HKUST ELEC 2100 online quiz 2
  - HKUST ELEC 2100 quiz 2
tags:
  - date/2026/03/16
  - flashcard/active/special/academia/HKUST/ELEC_2100/questions/quiz_2
  - language/in/English
---

# quiz 2

- HKUST ELEC 2100
- parent: [questions](index.md)

---

- type: online quiz
- due: 2026-03-16T23:59:59+08:00
- points: 5
- questions: 5
- available: 2026-03-16T10:00:00+08:00/2026-03-16T23:59:59+08:00, PT13H59M59S
- time limit: PT30M

## hints

1. In the output-sketch question, if you see two gain-$3$ replicas arriving at $t=4$ and $t=5$, what impulse-response pattern should you expect? ::@:: Expect two shifted impulses at those delays, each weighted by $3$, because each impulse term creates one delayed copy of the input. <!--SR:!2026-05-15,16,290!2026-05-15,16,290-->
2. In the Fourier-series applicability question, which candidate type should survive the test? ::@:: The periodically repeated pulse-train type survives, because Fourier series needs exact repetition over a nonzero period rather than a one-shot, switched-on, or growing signal. <!--SR:!2026-05-15,16,290!2026-05-14,15,290-->
3. For the periodic impulse train $\sum_n \delta(t-nT)$, what coefficient pattern should you anticipate before integrating? ::@:: One impulse lands in every period with the same harmonic effect, so all exponential Fourier-series coefficients should come out equal rather than only the DC term surviving. <!--SR:!2026-05-15,16,290!2026-05-15,16,290-->
4. In the interconnection question with one cascade branch and one parallel branch, what rule order should you apply? ::@:: Reduce the cascade branch by convolution first, then add the branch that joins in parallel. <!--SR:!2026-05-15,16,290!2026-05-15,16,290-->
5. In the periodic-versus-aperiodic spectrum question, what shape belongs to Fourier series? ::@:: A periodic signal gives discrete harmonic lines spaced by the fundamental frequency, not a continuous frequency curve. <!--SR:!2026-05-15,16,290!2026-05-15,16,290-->
