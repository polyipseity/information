---
aliases:
  - COMP 3111H quiz 14
  - COMP3111H quiz 14
  - HKUST COMP 3111H quiz 14
  - HKUST COMP3111H quiz 14
tags:
  - date/2025/11/04
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

1. integration testing / nature ::@:: white-box and black-box, run by developers or independent test group <!--SR:!fsrs,2028-07-12T00:00:00.000Z,662,662.08050273,2.49272837,2,9,0,0,2026-09-19T00:00:00.000Z!2026-10-10,249,330-->
2. equivalence partitioning / boundary values ::@:: Test values just inside, on, and just outside the limits of each partition because off-by-one errors, null handling, overflows, and aliasing are _most likely_ near boundaries rather than the interior. <!--SR:!fsrs,2028-07-09T00:00:00.000Z,660,659.5406844,2.49272837,2,9,0,0,2026-09-18T00:00:00.000Z!fsrs,2028-08-11T00:00:00.000Z,760,759.95962134,1,2,8,0,0,2026-07-13T00:00:00.000Z-->
3. white-box testing / data flow testing ::@:: Verify that each variable's value is correct at every use point by cover each _definition use \(DU\) chain_ at least once. <p> It may be combined with basis path testing. <!--SR:!2026-10-16,255,330!fsrs,2029-08-26T00:00:00.000Z,1065,1064.62815785,1,2,9,0,0,2026-09-26T00:00:00.000Z-->
4. white-box testing / loop testing / nested ::@:: Start with the innermost loop using _simple loop test_, then incrementally move outward, testing each loop level while keeping \(already tested\) inner loops and outer loops fixed at their _minima_; this strategy makes test count grow _geometrically_ with the level of _nesting_. <!--SR:!2026-10-03,246,330!fsrs,2028-06-18T00:00:00.000Z,719,718.52900463,1,2,8,0,0,2026-06-30T00:00:00.000Z-->
5. white-box testing / loop testing ::@:: For a \(large\) loop with _n_ iterations, execute loops for 0, 1, 2 passes; then test _m_ passes for some _m &lt; n_, and finally _n−1_, _n_, _n+1_ passes to cover boundary behavior. So a loop in general requires at least _7 minimum test cases_. <!--SR:!fsrs,2029-08-21T00:00:00.000Z,1061,1060.7584061,1,2,9,0,0,2026-09-25T00:00:00.000Z!fsrs,2028-07-04T00:00:00.000Z,730,729.86072057,1,2,8,0,0,2026-07-05T00:00:00.000Z-->
