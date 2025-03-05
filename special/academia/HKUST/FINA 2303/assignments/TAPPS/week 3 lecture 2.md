---
aliases:
  - FINA 2303 TAPPS - week 3 lecture 2
  - FINA 2303 thinking aloud paired problem solving - week 3 lecture 2
  - FINA2303 TAPPS - week 3 lecture 2
  - FINA2303 thinking aloud paired problem solving - week 3 lecture 2
  - HKUST FINA 2303 TAPPS - week 3 lecture 2
  - HKUST FINA 2303 thinking aloud paired problem solving - week 3 lecture 2
  - HKUST FINA2303 TAPPS - week 3 lecture 2
  - HKUST FINA2303 thinking aloud paired problem solving - week 3 lecture 2
tags:
  - date/2025/02/21
  - flashcard/active/special/academia/HKUST/FINA_2303/assignments/TAPPS/week_3_lecture_2
  - language/in/English
---

# thinking aloud paired problem solving (TAPPS) - week 3 lecture 2

- HKUST FINA 2303
- thinking aloud paired problem solving (TAPPS)

## problem

Ellen is 35 years old now. She has a retirement saving target of \$3 million when she retires at 65. She plans to save monthly in an account which pays 6% annual interest, compounded monthly.

How much will Ellen need to save monthly to reach her retirement target?

## submission

Manipulate: $$\begin{aligned}
PV & = \frac C r \left(1 - \frac 1 {(1 + r)^n} \right) \\
FV & = (1+r)^n \frac C r \left(1 - \frac 1 {(1 + r)^n} \right) \\
FV & = \frac C r \left((1 + r)^n - 1 \right) \\
C &= FV \frac r {(1 + r)^n - 1} \,.
\end{aligned}$$

We consider a month instead of a year as a period. So we have $12(65 - 35) = 360$ months (periods). The interest rate for a month is $6\% / 12 = 0.5\%$. Calculate: $$C = 3\,000\,000 \frac {0.5\%} {(1 + 0.5\%)^{360} - 1} \approx 2988 \,.$$
