---
aliases:
  - equivalent infinitesimal
  - equivalent infinitesimals
  - indeterminate form
  - indeterminate forms
tags:
  - flashcard/active/general/L_Hôpital_s_rule
  - language/in/English
---

# indeterminate form

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## evaluating indeterminate forms

### equivalent infinitesimal

#### x→0

```Python
# pytextgen generate data
from itertools import chain as _chain
return await memorize_map(
  __env__.cwf_sects("499f", "39dd", "f234",),
  {
    R"$\sin{x}$": R"$x$",
    R"$\arcsin{x}$": R"$x$",
    R"$\sinh{x}$": R"$x$",
    R"$\tan{x}$": R"$x$",
    R"$\arctan{x}$": R"$x$",
    R"$\ln(1+x)$": R"$x$",
    R"$1-\cos{x}$": R"$\frac{x^2}2$",
    R"$\cosh{x}-1$": R"$\frac{x^2}2$",
    R"$a^x-1$": R"$x\ln{a}$",
    R"$e^x-1$": R"$x$",
    R"$(1+x)^a-1$": R"$ax$",
  },
  delimiter=R" $\sim$ ",
)
```

<!--pytextgen generate section="499f"--><!-- The following content is generated at 2023-11-21T12:44:22.983521+08:00. Any edits will be overridden! -->

> 1. $\sin{x}$ $\sim$ $x$
> 2. $\arcsin{x}$ $\sim$ $x$
> 3. $\sinh{x}$ $\sim$ $x$
> 4. $\tan{x}$ $\sim$ $x$
> 5. $\arctan{x}$ $\sim$ $x$
> 6. $\ln(1+x)$ $\sim$ $x$
> 7. $1-\cos{x}$ $\sim$ $\frac{x^2}2$
> 8. $\cosh{x}-1$ $\sim$ $\frac{x^2}2$
> 9. $a^x-1$ $\sim$ $x\ln{a}$
> 10. $e^x-1$ $\sim$ $x$
> 11. $(1+x)^a-1$ $\sim$ $ax$

<!--/pytextgen-->

<!--pytextgen generate section="39dd"--><!-- The following content is generated at 2024-01-04T20:17:52.099769+08:00. Any edits will be overridden! -->

- $\sin{x}$::$x$ <!--SR:!2024-12-04,285,330-->
- $\arcsin{x}$::$x$ <!--SR:!2024-11-12,269,330-->
- $\sinh{x}$::$x$ <!--SR:!2024-11-07,265,330-->
- $\tan{x}$::$x$ <!--SR:!2027-06-22,1011,350-->
- $\arctan{x}$::$x$ <!--SR:!2025-01-06,312,330-->
- $\ln(1+x)$::$x$ <!--SR:!2024-11-08,265,330-->
- $1-\cos{x}$::$\frac{x^2}2$ <!--SR:!2026-08-15,754,330-->
- $\cosh{x}-1$::$\frac{x^2}2$ <!--SR:!2025-12-29,532,310-->
- $a^x-1$::$x\ln{a}$ <!--SR:!2026-12-03,827,330-->
- $e^x-1$::$x$ <!--SR:!2024-10-09,241,330-->
- $(1+x)^a-1$::$ax$ <!--SR:!2024-11-01,188,230-->

<!--/pytextgen-->

<!--pytextgen generate section="f234"--><!-- The following content is generated at 2024-01-04T20:17:52.183338+08:00. Any edits will be overridden! -->

- $x$::$\sin{x}$, $\arcsin{x}$, $\sinh{x}$, $\tan{x}$, $\arctan{x}$, $\ln(1+x)$, $e^x-1$ <!--SR:!2025-01-09,117,190-->
- $\frac{x^2}2$::$1-\cos{x}$, $\cosh{x}-1$ <!--SR:!2024-11-05,180,270-->
- $x\ln{a}$::$a^x-1$ <!--SR:!2024-10-24,54,250-->
- $ax$::$(1+x)^a-1$ <!--SR:!2024-10-09,205,290-->

<!--/pytextgen-->

#### x→∞

To derive the equivalent infinitesimals when $x \to \pm\infty$, {{replace all $x$ with $\frac 1 x$ in the [equivalent infinitesimals when $x \to 0^\pm$](#x→0) ($x \to +\infty$ becomes $x \to 0^+$, $x \to -\infty$ becomes $x \to 0^-$)}}. <!--SR:!2025-08-14,401,364-->

### L'Hôpital's rule

- see: [L'Hôpital's rule](L'Hôpital's%20rule.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/indeterminate_form) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
