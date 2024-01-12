---
aliases:
  - Bernoulli rule
  - Bernoulli's rule
  - L'Hopital rule
  - L'Hôpital rule
  - L'Hopital's rule
  - L'Hôpital's rule
  - L'Hospital rule
  - L'Hôspital rule
  - L'Hospital's rule
  - L'Hôspital's rule
tags:
  - flashcards/general/L_Hôpital_s_rule
  - languages/in/English
---

# indeterminate form

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

## evaluating indeterminate forms

### equivalent infinitesimal

#### x→0

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from itertools import chain as _chain
e = __env__
return await memorize_map(
  e.cwf_sects("499f", "39dd", "f234",),
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="499f"--><!-- The following content is generated at 2023-11-21T12:44:22.983521+08:00. Any edits will be overridden! -->

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

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="39dd"--><!-- The following content is generated at 2024-01-04T20:17:52.099769+08:00. Any edits will be overridden! -->

- $\sin{x}$::$x$ <!--SR:!2024-02-23,67,310-->
- $\arcsin{x}$::$x$ <!--SR:!2024-02-17,63,310-->
- $\sinh{x}$::$x$ <!--SR:!2024-02-16,62,310-->
- $\tan{x}$::$x$ <!--SR:!2024-02-04,52,310-->
- $\arctan{x}$::$x$ <!--SR:!2024-02-29,73,310-->
- $\ln(1+x)$::$x$ <!--SR:!2024-02-17,62,310-->
- $1-\cos{x}$::$\frac{x^2}2$ <!--SR:!2024-01-27,44,290-->
- $\cosh{x}-1$::$\frac{x^2}2$ <!--SR:!2024-01-25,43,290-->
- $a^x-1$::$x\ln{a}$ <!--SR:!2024-02-17,62,310-->
- $e^x-1$::$x$ <!--SR:!2024-02-10,57,310-->
- $(1+x)^a-1$::$ax$ <!--SR:!2024-02-04,36,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f234"--><!-- The following content is generated at 2024-01-04T20:17:52.183338+08:00. Any edits will be overridden! -->

- $x$::$\sin{x}$, $\arcsin{x}$, $\sinh{x}$, $\tan{x}$, $\arctan{x}$, $\ln(1+x)$, $e^x-1$ <!--SR:!2024-02-15,34,230-->
- $\frac{x^2}2$::$1-\cos{x}$, $\cosh{x}-1$ <!--SR:!2024-02-07,51,290-->
- $x\ln{a}$::$a^x-1$ <!--SR:!2024-01-22,40,290-->
- $ax$::$(1+x)^a-1$ <!--SR:!2024-03-17,71,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### L'Hôpital's rule

- see: [L'Hôpital's rule](L'Hôpital's%20rule.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/indeterminate_form) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
