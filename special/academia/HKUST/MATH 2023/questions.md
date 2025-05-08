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

- Does $$f(x, y) = \frac {\sin(x^2 + y^2) } {x^2 + y^2}$$ have limit at $(0, 0)$? ::@:: Yes. We can check it more conveniently by substituting $z = x^2 + y^2$ to make it a single-variable function, and then proving its limit exist. <!--SR:!2025-05-26,66,310!2025-05-26,66,310-->
- Does $$f(x, y) = \frac {x^2 - y^2} {x^2 + y^2}$$ have limit at $(0, 0)$? ::@:: No. Consider the two single-variable functions given by restricting to the lines $x = 0$ and $y = 0$. <!--SR:!2025-05-26,66,310!2025-05-27,67,310-->
- Does $$f(x, y) = \frac {xy^2} {x^2 + y^4}$$ have limit at $(0, 0)$? ::@:: No. If you consider any _straight_ line through $(0, 0)$, you will always get a limit of 0. But you also need to consider _curved_ paths, such as the one given by $x = y^2$. <!--SR:!2025-05-26,66,310!2025-05-27,67,310-->
- Find $$\lim_{(x, y) \to (1, 2)} \left(x^2 y^3 - x^3 y^2 \right)$$ if it exists, or explain if otherwise. ::@:: Since it is a polynomial, limits exist everywhere. So direct calculation suffices: $$x^2 y^3 - x^3 y^2 = 1^2 2^3 - 1^3 2^2 = 8 - 4 = 4 \,.$$ <!--SR:!2025-05-27,67,310!2025-05-26,66,310-->
- Find $$\lim_{(x, y) \to (-2, 3)} \frac {x^2 y + 1} {x^3 y^2 - 2x}$$ if it exists, or explain if otherwise. ::@:: Since it is a rational function, limits exist if the denominator is nonzero. Check: $$x^3 y^2 - 2x = (-2)^3 3^2 - 2(-2) = -72 + 4 = -68 \,.$$ So direct calculation suffices: $$\frac {x^2 y + 1} {x^3 y^2 - 2x} = \frac {(-2)^2 3 + 1} {(-2)^3 3^2 - 2(-2)} = -\frac {13} {68} \,.$$ <!--SR:!2025-05-27,67,310!2025-05-27,67,310-->
- Find $$\lim_{(x, y) \to (0, 0)} \frac {x^2 y} {x^2 + y^2}$$ if it exists, or explain if otherwise. ::@:: No matter how hard you try, you could not find a path that makes the limit different. This is because the limit does exist. We could go through the definition, but it is easier to use the _squeeze_ theorem: $$\begin{aligned} 0 & \le \frac {x^2} {x^2 + y^2} \le 1 \\ \lvert -y \rvert & \le \frac {x^2 y} {x^2 + y^2} \le \lvert y \rvert \,, \end{aligned}$$ and it is obvious that the two functions squeezing the function in question have the same limit $0$ at $(0, 0)$. <!--SR:!2025-05-27,67,310!2025-09-24,139,290-->
