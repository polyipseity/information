---
aliases:
  - Bernoulli rule
  - Bernoulli's rule
  - Bernoulli’s rule
  - L'Hopital rule
  - L'Hopital's rule
  - L'Hospital rule
  - L'Hospital's rule
  - L'Hôpital rule
  - L'Hôpital's rule
  - L'Hôspital rule
  - L'Hôspital's rule
  - L’Hopital rule
  - L’Hopital’s rule
  - L’Hospital rule
  - L’Hospital’s rule
  - L’Hôpital rule
  - L’Hôpital’s rule
  - L’Hôspital rule
  - L’Hôspital’s rule
tags:
  - flashcard/active/general/L_Hôpital_s_rule
  - language/in/English
---

# L'Hôpital's rule

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

__{{L'Hôpital's}} rule__, also known as __{{Bernoulli's}} rule__, is {{a [theorem](theorem.md) used for evaluating [limits](limit%20of%20a%20function.md) of [indeterminate forms](indeterminate%20form.md) from [derivatives](derivative.md)}}. <!--SR:!2027-07-05,1007,340!2025-11-04,531,320!2025-01-22,326,340-->

> __L'Hôpital's rule__
>
> 1. {{Given [real-valued functions](real-valued%20function.md) $f$ and $g$ which are [differentiable](differentiable%20function.md) on, for two-sided limit, an open [interval](interval%20(mathematics).md) $I$ except possibly at an [extended real number](extended%20real%20number%20line.md) $c$ which is in $I$, or for limit at infinity or [one-sided limit](one-sided%20limit.md), an open [interval](interval%20(mathematics).md) with endpoint $c$,}}
> 2. {{if $\lim_{x\to{}c}f(x)=\lim_{x\to{}c}g(x)=0$ or $\lim_{x\to{}c}\lvert{g(x)}\rvert=\infty$, $g'(x)\ne0$ for every $x$ in $I$ except possibly $c$, and the [limit](limit%20of%20a%20functino.md) $\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$ exists or equals positive or negative [infinity](infinity.md),}}
> 3. {{then $\lim_{x\to{}c}\frac{f(x)}{g(x)}=\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$.}}
> 4. {{If $c$ is a finite endpoint of $I$, the limits can be also be [one-sided limits](one-sided%20limit.md) $x\to{}c^+$ or $x\to{}c^-$.}} <!--SR:!2024-11-09,223,280!2025-04-11,308,260!2024-11-05,245,320!2026-11-25,839,340-->

## other indeterminate forms

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = (R"indeterminate form", R"conditions", R"transformation to 0/0", R"transformation to ∞/∞",)
table = (
  (R"$\frac00$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$", R"", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$",),
  (R"$\frac\infty\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$", R"",),
  (R"$0\cdot\infty$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$",),
  (R"$\infty-\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$", R"$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$",),
  (R"$0^0$", R"$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
  (R"$1^\infty$", R"$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$",),
  (R"$\infty^0$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("948f", "dd11",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "5dab", None,),
    items_to_map(*((entry[0], entry[1],) for entry in table if entry[1])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "679d", "39ba",),
    items_to_map(*((entry[0], entry[2],) for entry in table if entry[2])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "1e32", "ff01",),
    items_to_map(*((entry[0], entry[3],) for entry in table if entry[3])),
  ),
))
```

The following table lists out transformation from other [indeterminate forms](indeterminate%20form.md) for applying L'Hôpital's rule.

<!--pytextgen generate section="948f"--><!-- The following content is generated at 2024-02-01T20:28:01.846124+08:00. Any edits will be overridden! -->

> | indeterminate form | conditions | transformation to 0/0 | transformation to ∞/∞ |
> |-|-|-|-|
> | $\frac00$ | $\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$ |  | $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ |
> | $\frac\infty\infty$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ |  |
> | $0\cdot\infty$ | $\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$ | $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$ |
> | $\infty-\infty$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$ | $\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$ |
> | $0^0$ | $\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ |
> | $1^\infty$ | $\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ |
> | $\infty^0$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ |

<!--/pytextgen-->

<!--pytextgen generate section="dd11"--><!-- The following content is generated at 2024-01-04T20:17:52.125767+08:00. Any edits will be overridden! -->

- _(begin)_→:::←$\frac00$ <!--SR:!2024-10-28,256,330!2027-05-04,973,350-->
- $\frac00$→:::←$\frac\infty\infty$ <!--SR:!2024-12-05,286,330!2027-10-01,1086,350-->
- $\frac\infty\infty$→:::←$0\cdot\infty$ <!--SR:!2025-08-28,445,310!2025-09-28,466,310-->
- $0\cdot\infty$→:::←$\infty-\infty$ <!--SR:!2025-07-29,411,290!2026-07-11,656,310-->
- $\infty-\infty$→:::←$0^0$ <!--SR:!2025-02-25,213,230!2024-11-14,68,230-->
- $0^0$→:::←$1^\infty$ <!--SR:!2024-11-06,255,310!2025-07-25,421,310-->
- $1^\infty$→:::←$\infty^0$ <!--SR:!2025-04-15,187,250!2024-12-03,44,270-->
- $\infty^0$→:::←_(end)_ <!--SR:!2027-06-20,1009,350!2025-10-25,455,290-->

<!--/pytextgen-->

### indeterminate form–conditions

<!--pytextgen generate section="5dab"--><!-- The following content is generated at 2024-01-04T20:17:52.261336+08:00. Any edits will be overridden! -->

- $\frac00$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$ <!--SR:!2028-01-07,1167,350-->
- $\frac\infty\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2027-11-17,1128,350-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-11-02,261,330-->
- $\infty-\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2027-10-11,1096,350-->
- $0^0$::$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-11-18,205,290-->
- $1^\infty$::$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-12-14,294,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$ <!--SR:!2027-05-28,991,350-->

<!--/pytextgen-->

### indeterminate form-transformation to 0/0

<!--pytextgen generate section="679d"--><!-- The following content is generated at 2024-02-01T20:28:01.809542+08:00. Any edits will be overridden! -->

- $\frac\infty\infty$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ <!--SR:!2027-11-20,1129,350-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$ <!--SR:!2024-11-03,261,330-->
- $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$ <!--SR:!2025-05-21,356,290-->
- $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-11-06,223,270-->
- $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-11-02,260,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2025-10-23,483,310-->

<!--/pytextgen-->

<!--pytextgen generate section="39ba"--><!-- The following content is generated at 2024-02-01T20:28:01.881218+08:00. Any edits will be overridden! -->

- $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$::$\frac\infty\infty$ <!--SR:!2024-11-17,273,330-->
- $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$::$0\cdot\infty$ <!--SR:!2027-04-06,950,350-->
- $\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$::$\infty-\infty$ <!--SR:!2027-08-10,1050,350-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$0^0$, $\infty^0$ <!--SR:!2025-11-22,489,290-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$1^\infty$ <!--SR:!2025-09-24,423,270-->

<!--/pytextgen-->

### indeterminate form–transformation to ∞/∞

<!--pytextgen generate section="1e32"--><!-- The following content is generated at 2024-02-01T20:28:01.927217+08:00. Any edits will be overridden! -->

- $\frac00$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ <!--SR:!2027-03-13,932,350-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$ <!--SR:!2027-10-31,1111,350-->
- $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$ <!--SR:!2024-11-30,282,330-->
- $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2026-07-25,728,330-->
- $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-11-02,261,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-11-13,269,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ff01"--><!-- The following content is generated at 2024-02-01T20:28:01.993744+08:00. Any edits will be overridden! -->

- $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$::$\frac00$ <!--SR:!2024-10-28,256,330-->
- $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$::$0\cdot\infty$ <!--SR:!2027-07-12,1027,350-->
- $\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$::$\infty-\infty$ <!--SR:!2027-01-06,853,330-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$0^0$, $\infty^0$ <!--SR:!2025-10-06,431,270-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$1^\infty$ <!--SR:!2025-03-30,297,250-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/L'Hôpital's_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
