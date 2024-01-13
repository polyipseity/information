---
aliases: []
tags:
  - date/2023/10/10
  - languages/in/English
---

# classwork 1

If we need a frequency output of 50Hz, what are the 3 possible combinations of prescaler value and auto-reload value? (Given that the clock frequency is 84MHz)

> [!success] solution
>
> $$\begin{aligned}
> \mathrm{downscaling}&=\frac{84000000}{50}\\
> &=1680000\\
> &=100\cdot16800=1000\cdot1680=10000\cdot168\\
> (\mathrm{prescaler},\mathrm{autoreload})&=(99,16799)\mathrm{\ or\ }(999,1679)\mathrm{\ or\ }(9999,167)
> \end{aligned}$$
