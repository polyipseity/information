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

1. In the output-sketch question, if you see two gain-$3$ replicas arriving at $t=4$ and $t=5$, what impulse-response pattern should you expect? ::@:: Expect two shifted impulses at those delays, each weighted by $3$, because each impulse term creates one delayed copy of the input. <!--SR:!fsrs,2027-06-01T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-06-01T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-19T00:00:00.000Z-->
2. In the Fourier-series applicability question, which candidate type should survive the test? ::@:: The periodically repeated pulse-train type survives, because Fourier series needs exact repetition over a nonzero period rather than a one-shot, switched-on, or growing signal. <!--SR:!fsrs,2027-05-22T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
3. For the periodic impulse train $\sum_n \delta(t-nT)$, what coefficient pattern should you anticipate before integrating? ::@:: One impulse lands in every period with the same harmonic effect, so all exponential Fourier-series coefficients should come out equal rather than only the DC term surviving. <!--SR:!fsrs,2027-05-16T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-05-27T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
4. In the interconnection question with one cascade branch and one parallel branch, what rule order should you apply? ::@:: Reduce the cascade branch by convolution first, then add the branch that joins in parallel. <!--SR:!fsrs,2027-06-06T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-20T00:00:00.000Z!2026-07-21,67,310-->
5. In the periodic-versus-aperiodic spectrum question, what shape belongs to Fourier series? ::@:: A periodic signal gives discrete harmonic lines spaced by the fundamental frequency, not a continuous frequency curve. <!--SR:!fsrs,2027-06-12T00:00:00.000Z,326,325.58679272,1,2,7,0,0,2026-07-21T00:00:00.000Z!2026-07-21,67,310-->
