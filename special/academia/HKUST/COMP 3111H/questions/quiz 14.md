---
aliases:
  - COMP 3111H quiz 14
  - COMP3111H quiz 14
  - HKUST COMP 3111H quiz 14
  - HKUST COMP3111H quiz 14
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions/quiz_14
  - language/in/English
---

# quiz 14

- HKUST COMP 3111H

---

- type: quiz
- due: 2025-11-04T23:59:59+08:00
- points: 5
- questions: 5
- available: 2025-10-21T23:59:00+08:00/2025-11-04T23:59:59+08:00, P14DT59S
- time limit: none
- allowed attempts: 2

## hints

1. integration testing / nature ::@:: white-box and black-box, run by developers or independent test group
2. equivalence partitioning / boundary values ::@:: Test values just inside, on, and just outside the limits of each partition because off-by-one errors, null handling, overflows, and aliasing are _most likely_ near boundaries rather than the interior.
3. white-box testing / data flow testing ::@:: Verify that each variable's value is correct at every use point by cover each _definition use \(DU\) chain_ at least once. <p> It may be combined with basis path testing.
4. white-box testing / loop testing / nested ::@:: Start with the innermost loop using _simple loop test_, then incrementally move outward, testing each loop level while keeping \(already tested\) inner loops and outer loops fixed at their _minima_; this strategy makes test count grow _geometrically_ with the level of _nesting_.
5. white-box testing / loop testing ::@:: For a \(large\) loop with _n_ iterations, execute loops for 0, 1, 2 passes; then test _m_ passes for some _m &lt; n_, and finally _n−1_, _n_, _n+1_ passes to cover boundary behavior. So a loop in general requires at least _7 minimum test cases_.
