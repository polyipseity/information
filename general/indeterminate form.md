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
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# indeterminate form

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="39dd"--><!-- The following content is generated at 2023-11-21T12:42:55.893815+08:00. Any edits will be overridden! -->

1. $\sin{x}$::$x$
2. $\arcsin{x}$::$x$
3. $\sinh{x}$::$x$
4. $\tan{x}$::$x$
5. $\arctan{x}$::$x$
6. $\ln(1+x)$::$x$
7. $1-\cos{x}$::$\frac{x^2}2$
8. $\cosh{x}-1$::$\frac{x^2}2$
9. $a^x-1$::$x\ln{a}$
10. $e^x-1$::$x$
11. $(1+x)^a-1$::$ax$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f234"--><!-- The following content is generated at 2023-11-21T12:42:55.830785+08:00. Any edits will be overridden! -->

1. $x$::$\sin{x}$, $\arcsin{x}$, $\sinh{x}$, $\tan{x}$, $\arctan{x}$, $\ln(1+x)$, $e^x-1$
2. $\frac{x^2}2$::$1-\cos{x}$, $\cosh{x}-1$
3. $x\ln{a}$::$a^x-1$
4. $ax$::$(1+x)^a-1$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### L'Hôpital's rule

- see: [L'Hôpital's rule](L'Hôpital's%20rule.md)
