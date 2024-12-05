---
aliases: []
tags:
  - date/2023/10/10
  - language/in/English
---

# classwork 2

If we need a frequency output of 50Hz and on-time of 0.5ms, what are the possible combinations of prescaler value, auto-reload value and compare value? (Given that the clock frequency is 84MHz)

> [!success] solution
>
> $$\begin{aligned}
> \mathrm{duty\ cycle}&=\frac{\frac{0.5}{1000} }{\frac1{50} }\\
> &=\frac{25}{1000}\\
> &=\frac1{40}\\
> 40&\mid\mathrm{autoreload}+1\\
> \mathrm{downscaling}&=\frac{84000000}{50}\\
> &=1680000\\
> &=40\cdot42000=80\cdot21000=120\cdot14000\\
> (\mathrm{prescaler},\mathrm{autoreload},\mathrm{compare})&=(39,41999,1)\mathrm{\ or\ }(79,20999,2)\mathrm{\ or\ }(119,13999,3)
> \end{aligned}$$
