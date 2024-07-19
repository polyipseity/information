---
aliases:
  - derivative of trigonometric functions
  - derivatives of trigonometric functions
  - differentiation of trigonometric functions
tags:
  - flashcard/general/differentiation_of_trigonometric_functions
  - language/in/English
---

# differentiation of trigonometric functions

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## list of derivatives

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("49fa", "e934", "b023"),
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

<!--pytextgen generate section="49fa"--><!-- The following content is generated at 2023-12-13T23:33:14.053109+08:00. Any edits will be overridden! -->

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

<!--/pytextgen-->

> [!tip] tips
>
> - [mnemonic](mnemonic.md) ::: From the [derivative](derivative.md) of a trigonometric function, replace trigonometric functions with their counterparts and negate the [derivative](derivative.md) to get the [derivative](derivative.md) of the counterpart. <!--SR:!2024-08-27,208,330!2025-06-12,340,359-->

### function–derivative

<!--pytextgen generate section="e934"--><!-- The following content is generated at 2024-01-04T20:17:51.635097+08:00. Any edits will be overridden! -->

- $\sin{x}$::$\cos{x}$ <!--SR:!2024-10-07,239,330-->
- $\cos{x}$::$-\sin{x}$ <!--SR:!2024-11-24,278,330-->
- $\tan{x}$::$\sec^2{x}$ <!--SR:!2024-11-29,282,330-->
- $\cot{x}$::$-\csc^2{x}$ <!--SR:!2024-07-26,7,210-->
- $\sec{x}$::$\sec{x}\tan{x}$ <!--SR:!2024-09-24,210,290-->
- $\csc{x}$::$-\csc{x}\cot{x}$ <!--SR:!2024-09-20,203,290-->
- $\arcsin{x}$::$\frac1{\sqrt{1-x^2} }$ <!--SR:!2024-11-11,142,270-->
- $\arccos{x}$::$-\frac1{\sqrt{1-x^2} }$ <!--SR:!2024-08-23,190,310-->
- $\arctan{x}$::$\frac1{x^2+1}$ <!--SR:!2025-01-01,308,330-->
- $\operatorname{arccot}{x}$::$-\frac1{x^2+1}$ <!--SR:!2024-10-26,256,330-->
- $\operatorname{arcsec}{x}$::$\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$ <!--SR:!2025-03-15,284,250-->
- $\operatorname{arccsc}{x}$::$-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$ <!--SR:!2024-10-20,214,290-->

<!--/pytextgen-->

### derivative–function

<!--pytextgen generate section="b023"--><!-- The following content is generated at 2024-01-04T20:17:51.605095+08:00. Any edits will be overridden! -->

- $\cos{x}$::$\sin{x}$ <!--SR:!2024-10-12,244,330-->
- $-\sin{x}$::$\cos{x}$ <!--SR:!2024-09-19,226,330-->
- $\sec^2{x}$::$\tan{x}$ <!--SR:!2024-10-06,238,330-->
- $-\csc^2{x}$::$\cot{x}$ <!--SR:!2025-10-24,476,310-->
- $\sec{x}\tan{x}$::$\sec{x}$ <!--SR:!2025-01-02,269,310-->
- $-\csc{x}\cot{x}$::$\csc{x}$ <!--SR:!2024-08-21,187,310-->
- $\frac1{\sqrt{1-x^2} }$::$\arcsin{x}$ <!--SR:!2024-12-27,304,330-->
- $-\frac1{\sqrt{1-x^2} }$::$\arccos{x}$ <!--SR:!2024-12-11,291,330-->
- $\frac1{x^2+1}$::$\arctan{x}$ <!--SR:!2025-05-29,406,310-->
- $-\frac1{x^2+1}$::$\operatorname{arccot}{x}$ <!--SR:!2024-11-22,277,330-->
- $\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$::$\operatorname{arcsec}{x}$ <!--SR:!2024-08-06,67,290-->
- $-\frac1{\lvert{x}\rvert\sqrt{x^2-1} }$::$\operatorname{arccsc}{x}$ <!--SR:!2025-12-13,520,310-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/differentiation_of_trigonometric_functions) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
