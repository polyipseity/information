---
aliases:
  - derivative of trigonometric functions
  - derivatives of trigonometric functions
  - differentiation of trigonometric functions
tags:
  - flashcards/general/differentiation_of_trigonometric_functions
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# differentiation of trigonometric functions

## list of derivatives

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_map(
  e.cwf_sects("49fa", "e934", "b023"),
  {
    R"$\sin{x}$": R"$\cos{x}$",
    R"$\cos{x}$": R"$-\sin{x}$",
    R"$\tan{x}$": R"$\sec^2{x}$",
    R"$\cot{x}$": R"$-\csc^2{x}$",
    R"$\sec{x}$": R"$\sec{x}\tan{x}$",
    R"$\csc{x}$": R"$-\csc{x}\cot{x}$",
    R"$\arcsin{x}$": R"$\frac1{\sqrt{1-x^2}}$",
    R"$\arccos{x}$": R"$-\frac1{\sqrt{1-x^2}}$",
    R"$\arctan{x}$": R"$\frac1{x^2+1}$",
    R"$\operatorname{arccot}{x}$": R"$-\frac1{x^2+1}$",
    R"$\operatorname{arcsec}{x}$": R"$\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$",
    R"$\operatorname{arccsc}{x}$": R"$-\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$",
  },
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="49fa"--><!-- The following content is generated at 2023-11-20T23:53:31.214607+08:00. Any edits will be overridden! -->

> 1. $\sin{x}$: $\cos{x}$
> 2. $\cos{x}$: $-\sin{x}$
> 3. $\tan{x}$: $\sec^2{x}$
> 4. $\cot{x}$: $-\csc^2{x}$
> 5. $\sec{x}$: $\sec{x}\tan{x}$
> 6. $\csc{x}$: $-\csc{x}\cot{x}$
> 7. $\arcsin{x}$: $\frac1{\sqrt{1-x^2}}$
> 8. $\arccos{x}$: $-\frac1{\sqrt{1-x^2}}$
> 9. $\arctan{x}$: $\frac1{x^2+1}$
> 10. $\operatorname{arccot}{x}$: $-\frac1{x^2+1}$
> 11. $\operatorname{arcsec}{x}$: $\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$
> 12. $\operatorname{arccsc}{x}$: $-\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!tip]
>
> - [mnemonic](mnemonic.md): {{From the [derivative](derivative.md) of a trigonometric function, replace trigonometric functions with their counterparts and negate the [derivative](derivative.md) to get the [derivative](derivative.md) of the counterpart.}} <!--SR:!2023-12-14,13,290-->

### function–derivative

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="e934"--><!-- The following content is generated at 2023-11-20T23:53:31.184573+08:00. Any edits will be overridden! -->

1. $\sin{x}$::$\cos{x}$ <!--SR:!2023-12-16,15,290-->
2. $\cos{x}$::$-\sin{x}$ <!--SR:!2023-12-17,16,290-->
3. $\tan{x}$::$\sec^2{x}$ <!--SR:!2023-12-17,16,290-->
4. $\cot{x}$::$-\csc^2{x}$ <!--SR:!2023-12-16,15,290-->
5. $\sec{x}$::$\sec{x}\tan{x}$ <!--SR:!2024-01-02,21,270-->
6. $\csc{x}$::$-\csc{x}\cot{x}$ <!--SR:!2023-12-18,6,250-->
7. $\arcsin{x}$::$\frac1{\sqrt{1-x^2}}$ <!--SR:!2023-12-15,11,270-->
8. $\arccos{x}$::$-\frac1{\sqrt{1-x^2}}$ <!--SR:!2023-12-16,15,290-->
9. $\arctan{x}$::$\frac1{x^2+1}$ <!--SR:!2023-12-18,17,290-->
10. $\operatorname{arccot}{x}$::$-\frac1{x^2+1}$ <!--SR:!2023-12-15,14,290-->
11. $\operatorname{arcsec}{x}$::$\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$ <!--SR:!2023-12-26,18,250-->
12. $\operatorname{arccsc}{x}$::$-\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$ <!--SR:!2024-01-06,25,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### derivative–function

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b023"--><!-- The following content is generated at 2023-11-20T23:53:31.288520+08:00. Any edits will be overridden! -->

1. $\cos{x}$::$\sin{x}$ <!--SR:!2023-12-16,15,290-->
2. $-\sin{x}$::$\cos{x}$ <!--SR:!2023-12-15,14,290-->
3. $\sec^2{x}$::$\tan{x}$ <!--SR:!2023-12-16,15,290-->
4. $-\csc^2{x}$::$\cot{x}$ <!--SR:!2023-12-14,13,290-->
5. $\sec{x}\tan{x}$::$\sec{x}$ <!--SR:!2023-12-15,14,290-->
6. $-\csc{x}\cot{x}$::$\csc{x}$ <!--SR:!2023-12-17,16,290-->
7. $\frac1{\sqrt{1-x^2}}$::$\arcsin{x}$ <!--SR:!2023-12-18,17,290-->
8. $-\frac1{\sqrt{1-x^2}}$::$\arccos{x}$ <!--SR:!2023-12-18,17,290-->
9. $\frac1{x^2+1}$::$\arctan{x}$ <!--SR:!2024-01-08,27,270-->
10. $-\frac1{x^2+1}$::$\operatorname{arccot}{x}$ <!--SR:!2023-12-17,16,290-->
11. $\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$::$\operatorname{arcsec}{x}$ <!--SR:!2023-12-13,9,270-->
12. $-\frac1{\lvert{x}\rvert\sqrt{x^2-1}}$::$\operatorname{arccsc}{x}$ <!--SR:!2023-12-13,12,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
