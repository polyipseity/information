---
aliases:
  - HKUST MATH 2023 question
  - HKUST MATH 2023 questions
  - HKUST MATH2023 question
  - HKUST MATH2023 questions
  - MATH 2023 question
  - MATH 2023 questions
  - MATH2023 question
  - MATH2023 questions
tags:
  - flashcard/active/special/academia/HKUST/MATH_2023/questions
  - language/in/English
---

# questions

- HKUST MATH 2023

## week 3 lecture 2

- Does $$f(x, y) = \frac {\sin(x^2 + y^2) } {x^2 + y^2}$$ have limit at $(0, 0)$? ::@:: Yes. We can check it more conveniently by substituting $z = x^2 + y^2$ to make it a single-variable function, and then proving its limit exist. <!--SR:!2026-03-10,288,330!2026-03-11,289,330-->
- Does $$f(x, y) = \frac {x^2 - y^2} {x^2 + y^2}$$ have limit at $(0, 0)$? ::@:: No. Consider the two single-variable functions given by restricting to the lines $x = 0$ and $y = 0$. <!--SR:!2026-03-10,288,330!2026-03-22,294,330-->
- Does $$f(x, y) = \frac {xy^2} {x^2 + y^4}$$ have limit at $(0, 0)$? ::@:: No. If you consider any _straight_ line through $(0, 0)$, you will always get a limit of 0. But you also need to consider _curved_ paths, such as the one given by $x = y^2$. <!--SR:!2026-03-12,290,330!2026-03-19,291,330-->
- Find $$\lim_{(x, y) \to (1, 2)} \left(x^2 y^3 - x^3 y^2 \right)$$ if it exists, or explain if otherwise. ::@:: Since it is a polynomial, limits exist everywhere. So direct calculation suffices: $$x^2 y^3 - x^3 y^2 = 1^2 2^3 - 1^3 2^2 = 8 - 4 = 4 \,.$$ <!--SR:!2026-03-18,290,330!2026-03-09,287,330-->
- Find $$\lim_{(x, y) \to (-2, 3)} \frac {x^2 y + 1} {x^3 y^2 - 2x}$$ if it exists, or explain if otherwise. ::@:: Since it is a rational function, limits exist if the denominator is nonzero. Check: $$x^3 y^2 - 2x = (-2)^3 3^2 - 2(-2) = -72 + 4 = -68 \,.$$ So direct calculation suffices: $$\frac {x^2 y + 1} {x^3 y^2 - 2x} = \frac {(-2)^2 3 + 1} {(-2)^3 3^2 - 2(-2)} = -\frac {13} {68} \,.$$ <!--SR:!2026-03-21,293,330!2026-03-21,293,330-->
- Find $$\lim_{(x, y) \to (0, 0)} \frac {x^2 y} {x^2 + y^2}$$ if it exists, or explain if otherwise. ::@:: No matter how hard you try, you could not find a path that makes the limit different. This is because the limit does exist. We could go through the definition, but it is easier to use the _squeeze_ theorem: $$\begin{aligned} 0 & \le \frac {x^2} {x^2 + y^2} \le 1 \\ \lvert -y \rvert & \le \frac {x^2 y} {x^2 + y^2} \le \lvert y \rvert \,, \end{aligned}$$ and it is obvious that the two functions squeezing the function in question have the same limit $0$ at $(0, 0)$. <!--SR:!2026-03-20,292,330!2027-04-07,560,310-->

## midterm examination

- Find the limit at $(0, 0)$ for $$f(x, y) = \frac {x^{2024} y^{2025} } {x^{4048} + y^{4050} }$$ if it exists, or show that the limit does not exist. ::@:: Let $a = x^{2024}$ and $b = y^{2025}$, then it becomes $$\frac {ab} {a^2 + b^2} \,,$$ which is much easier to see that there is no limit. The proof proceeds analogously to questions above. <!--SR:!2026-08-27,356,365!2026-08-20,350,365-->

## final examination

- Find the limit at $(0, 0, 0, 0)$ for $$f(a, b, c, d) = \frac {abcd} {a^2 + b^2 + c^2 + d^2}$$ if it exists, or show that the limit does not exist. ::@:: We want a denominator expression containing the term $abcd$ so that it can be simplified with the numerator. <p> Using the AM–GM inequality \($a^2, b^2, c^2, d^2$ are nonnegative\): $$\frac {a^2 + b^2 + c^2 + d^2} 4 \ge \left(a^2 b^2 c^2 d^2\right)^{1/4} = \sqrt{abcd} \,,$$ prove using squeeze theorem: $$\frac {\lvert abcd \rvert} {a^2 + b^2 + c^2 + d^2} \le \frac {\lvert abcd \rvert} {4 \sqrt{abcd} } = \frac 1 4 \sqrt{abcd} \,.$$ Then obviously the limit is 0. <p> Alternatively, use a epsilon—delta-style proof. Consider a 4D sphere of radius $r > 0$. On that sphere, $a^2 + b^2 + c^2 + d^2 = r^2$ and $a^2, b^2, c^2, d^2 \le r^2$. Then, $$\frac {\lvert abcd \rvert} {a^2 + b^2 + c^2 + d^2} \le \frac {r^4} {r^2} = r^2 \,.$$ Then as $r \to 0$, the limit is 0. <!--SR:!2026-04-24,146,341!2026-08-21,307,361-->
