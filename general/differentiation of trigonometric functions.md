---
aliases:
  - derivative of trigonometric functions
  - derivatives of trigonometric functions
  - differentiation of trigonometric functions
tags:
  - flashcards/general/differentiation_of_trigonometric_functions
  - languages/in/English
---

# differentiation of trigonometric functions

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

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
    R"$\arcsin{x}$": R"$\frac1{\sqrt{1-x^2} }$",
    R"$\arccos{x}$": R"$-\frac1{\sqrt{1-x^2} }$",
    R"$\arctan{x}$": R"$\frac1{x^2+1}$",
    R"$\operatorname{arccot}{x}$": R"$-\frac1{x^2+1}$",
    R"$\operatorname{arcsec}{x}$": R"$\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$",
    R"$\operatorname{arccsc}{x}$": R"$-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$",
  },
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="49fa"--><!-- The following content is generated at 2023-12-13T23:33:14.053109+08:00. Any edits will be overridden! -->

> 1. $\sin{x}$: $\cos{x}$
> 2. $\cos{x}$: $-\sin{x}$
> 3. $\tan{x}$: $\sec^2{x}$
> 4. $\cot{x}$: $-\csc^2{x}$
> 5. $\sec{x}$: $\sec{x}\tan{x}$
> 6. $\csc{x}$: $-\csc{x}\cot{x}$
> 7. $\arcsin{x}$: $\frac1{\sqrt{1-x^2} }$
> 8. $\arccos{x}$: $-\frac1{\sqrt{1-x^2} }$
> 9. $\arctan{x}$: $\frac1{x^2+1}$
> 10. $\operatorname{arccot}{x}$: $-\frac1{x^2+1}$
> 11. $\operatorname{arcsec}{x}$: $\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$
> 12. $\operatorname{arccsc}{x}$: $-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!tip] tip
>
> - [mnemonic](mnemonic.md): {{From the [derivative](derivative.md) of a trigonometric function, replace trigonometric functions with their counterparts and negate the [derivative](derivative.md) to get the [derivative](derivative.md) of the counterpart.}} <!--SR:!2024-02-01,49,310-->

### function–derivative

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="e934"--><!-- The following content is generated at 2024-01-04T20:17:51.635097+08:00. Any edits will be overridden! -->

- $\sin{x}$::$\cos{x}$ <!--SR:!2024-02-10,56,310-->
- $\cos{x}$::$-\sin{x}$ <!--SR:!2024-02-20,65,310-->
- $\tan{x}$::$\sec^2{x}$ <!--SR:!2024-02-21,66,310-->
- $\cot{x}$::$-\csc^2{x}$ <!--SR:!2024-01-29,44,290-->
- $\sec{x}$::$\sec{x}\tan{x}$ <!--SR:!2024-02-27,56,270-->
- $\csc{x}$::$-\csc{x}\cot{x}$ <!--SR:!2024-01-07,20,270-->
- $\arcsin{x}$::$\frac1{\sqrt{1-x^2} }$ <!--SR:!2024-01-13,29,270-->
- $\arccos{x}$::$-\frac1{\sqrt{1-x^2} }$ <!--SR:!2024-02-15,61,310-->
- $\arctan{x}$::$\frac1{x^2+1}$ <!--SR:!2024-02-28,72,310-->
- $\operatorname{arccot}{x}$::$-\frac1{x^2+1}$ <!--SR:!2024-02-13,60,310-->
- $\operatorname{arcsec}{x}$::$\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$ <!--SR:!2024-02-10,46,250-->
- $\operatorname{arccsc}{x}$::$-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$ <!--SR:!2024-01-06,25,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### derivative–function

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b023"--><!-- The following content is generated at 2024-01-04T20:17:51.605095+08:00. Any edits will be overridden! -->

- $\cos{x}$::$\sin{x}$ <!--SR:!2024-02-11,57,310-->
- $-\sin{x}$::$\cos{x}$ <!--SR:!2024-02-06,53,310-->
- $\sec^2{x}$::$\tan{x}$ <!--SR:!2024-02-10,56,310-->
- $-\csc^2{x}$::$\cot{x}$ <!--SR:!2024-02-02,50,310-->
- $\sec{x}\tan{x}$::$\sec{x}$ <!--SR:!2024-01-12,22,290-->
- $-\csc{x}\cot{x}$::$\csc{x}$ <!--SR:!2024-02-16,61,310-->
- $\frac1{\sqrt{1-x^2} }$::$\arcsin{x}$ <!--SR:!2024-02-27,71,310-->
- $-\frac1{\sqrt{1-x^2} }$::$\arccos{x}$ <!--SR:!2024-02-24,68,310-->
- $\frac1{x^2+1}$::$\arctan{x}$ <!--SR:!2024-01-08,27,270-->
- $-\frac1{x^2+1}$::$\operatorname{arccot}{x}$ <!--SR:!2024-02-19,64,310-->
- $\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$::$\operatorname{arcsec}{x}$ <!--SR:!2024-01-16,34,290-->
- $-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$::$\operatorname{arccsc}{x}$ <!--SR:!2024-01-24,42,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/differentiation_of_trigonometric_functions) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
