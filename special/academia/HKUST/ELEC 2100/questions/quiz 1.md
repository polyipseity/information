---
aliases:
  - ELEC 2100 online quiz 1
  - ELEC 2100 quiz 1
  - HKUST ELEC 2100 online quiz 1
  - HKUST ELEC 2100 quiz 1
tags:
  - date/2026/02/23
  - flashcard/active/special/academia/HKUST/ELEC_2100/questions/quiz_1
  - language/in/English
---

# quiz 1

- HKUST ELEC 2100
- parent: [questions](index.md)

---

- type: online quiz
- due: 2026-02-23T23:59:59+08:00
- points: 5
- questions: 5
- available: 2026-02-23T10:00:00+08:00/2026-02-23T23:59:59+08:00, PT13H59M59S
- time limit: PT30M

## hints

1. For a DT sinusoid equality, what must the digital-frequency gap satisfy relative to $2\pi$? ::@:: Cosine and sine repeat every $2\pi$, so if two sinusoids differ by a non-integer multiple of $2\pi$, they are not the same signal. <!--SR:!2026-05-14,14,290!2026-05-16,16,290-->
2. Among options built from a constant offset, a pointwise nonlinearity, a shifted-sample sum, and signal multiplication, which pattern should look LTI? ::@:: The shifted-sample sum is the LTI-looking candidate because superposition survives and a time shift just moves both referenced samples together. <!--SR:!2026-05-16,16,290!2026-05-15,15,290-->
3. For the graph question built around $x(-2t+6)=x(-2(t-3))$, what is the safest geometric workflow? ::@:: Start from the inside form $-2(t-3)$: center the action at $t=3$, use the minus sign for reversal, then compress horizontally by a factor of $2$. <!--SR:!2026-05-16,16,290!2026-05-15,15,290-->
4. Among a time-scaled CT rule, a running sum, an even-part operator, and a one-sample delay, which option has the usual causal-and-stable signature? ::@:: The one-sample delay is the standard safe choice because it uses only a past input value and preserves boundedness. <!--SR:!2026-05-14,14,290!2026-05-15,15,290-->
5. For a unit-area pulse with width $\varepsilon$ and height $1/\varepsilon$, what energy trend should you expect? ::@:: Its energy scales like $1/\varepsilon$, so it blows up as the pulse approaches a CT impulse. <!--SR:!2026-05-16,16,290!2026-05-14,14,290-->
