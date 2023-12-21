---
aliases:
  - exponentiation
  - exponentiations
tags:
  - flashcards/general/exponentiation
  - languages/in/English
---

# exponentiation

## non-integer powers of complex numbers

### complex exponentiation

#### failure of power and logarithm identities

> __examples of identities not true in general for [complex numbers](complex%20number.md)__
>
> - {{$\log\left(b^x\right) = x \log b \qquad (b \in \mathbb{R}^+, x \in \mathbb{R})$ <br/>__counterexample__: $b = -i, x = 2$ <br/>__fix__: $\log(b^x) = x \log b \pmod{2\pi i} \qquad (\log(*) \text{ is single-valued})$}}
> - {{$(bc)^x = b^x c^x \text{ and }(b / c)^x = b^x / c^x \qquad (b,c \in \mathbb{R}^+, x \in \mathbb{R} \text{ or } b,c \in \mathbb{C} \setminus \set 0, x \in \mathbb{Z})$ <br/>__counterexample__: $b = -1, c = -1, x = 0.5$ <br/>__fix__: consider $a^*$ as a [multi-valued function](multivalued%20function.md)}}
> - {{$\left(e^x\right)^y = e^{xy} \qquad (x,y \in \mathbb{R})$ <br/>__counterexample__: $x = 1 + 2n\pi i, y = 1 + 2n\pi i \quad \forall{n} \in \mathbb{Z}$ <br/>__fix__: $\left(e^x\right)^y = e^{y \log e^{x}} \qquad (e^* \text{ and } \log(*) \text{ are multi-valued})$}} <!--SR:!2023-12-22,1,230!2023-12-24,3,250!2023-12-24,3,250-->
