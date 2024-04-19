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
  - flashcard/general/L_Hôpital_s_rule
  - language/in/English
---

# L'Hôpital's rule

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

__{{L'Hôpital's}} rule__, also known as __{{Bernoulli's}} rule__, is {{a [theorem](theorem.md) used for evaluating [limits](limit%20of%20a%20function.md) of [indeterminate forms](indeterminate%20form.md) from [derivatives](derivative.md)}}. <!--SR:!2024-09-27,228,320!2024-05-22,128,300!2025-01-22,326,340-->

> __L'Hôpital's rule__
>
> 1. {{Given [real-valued functions](real-valued%20function.md) $f$ and $g$ which are [differentiable](differentiable%20function.md) on, for two-sided limit, an open [interval](interval%20(mathematics).md) $I$ except possibly at an [extended real number](extended%20real%20number%20line.md) $c$ which is in $I$, or for limit at infinity or [one-sided limit](one-sided%20limit.md), an open [interval](interval%20(mathematics).md) with endpoint $c$,}}
> 2. {{if $\lim_{x\to{}c}f(x)=\lim_{x\to{}c}g(x)=0$ or $\lim_{x\to{}c}\lvert{g(x)}\rvert=\infty$, $g'(x)\ne0$ for every $x$ in $I$ except possibly $c$, and the [limit](limit%20of%20a%20functino.md) $\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$ exists or equals positive or negative [infinity](infinity.md),}}
> 3. {{then $\lim_{x\to{}c}\frac{f(x)}{g(x)}=\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$.}}
> 4. {{If $c$ is a finite endpoint of $I$, the limits can be also be [one-sided limits](one-sided%20limit.md) $x\to{}c^+$ or $x\to{}c^-$.}} <!--SR:!2024-11-09,223,280!2024-06-07,119,260!2024-11-05,245,320!2024-08-08,190,320-->

## other indeterminate forms

%%

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

%%

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

- _(begin)_→:::←$\frac00$ <!--SR:!2024-10-28,256,330!2024-09-03,214,330-->
- $\frac00$→:::←$\frac\infty\infty$ <!--SR:!2024-12-05,286,330!2024-10-07,239,330-->
- $\frac\infty\infty$→:::←$0\cdot\infty$ <!--SR:!2024-06-09,144,310!2024-06-19,116,290-->
- $0\cdot\infty$→:::←$\infty-\infty$ <!--SR:!2024-06-13,142,290!2024-09-23,212,310-->
- $\infty-\infty$→:::←$0^0$ <!--SR:!2024-04-21,41,230!2024-06-04,46,250-->
- $0^0$→:::←$1^\infty$ <!--SR:!2024-11-06,255,310!2024-05-30,136,310-->
- $1^\infty$→:::←$\infty^0$ <!--SR:!2024-07-24,142,270!2024-07-22,178,310-->
- $\infty^0$→:::←_(end)_ <!--SR:!2024-09-14,222,330!2024-07-24,121,270-->

<!--/pytextgen-->

### indeterminate form–conditions

<!--pytextgen generate section="5dab"--><!-- The following content is generated at 2024-01-04T20:17:52.261336+08:00. Any edits will be overridden! -->

- $\frac00$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-10-27,256,330-->
- $\frac\infty\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-10-15,247,330-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-11-02,261,330-->
- $\infty-\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-10-07,241,330-->
- $0^0$::$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-04-27,71,290-->
- $1^\infty$::$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-12-14,294,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-09-08,218,330-->

<!--/pytextgen-->

### indeterminate form-transformation to 0/0

<!--pytextgen generate section="679d"--><!-- The following content is generated at 2024-02-01T20:28:01.809542+08:00. Any edits will be overridden! -->

- $\frac\infty\infty$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ <!--SR:!2024-10-16,248,330-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$ <!--SR:!2024-11-03,261,330-->
- $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$ <!--SR:!2024-05-30,123,290-->
- $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-11-06,223,270-->
- $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-11-02,260,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-06-27,156,310-->

<!--/pytextgen-->

<!--pytextgen generate section="39ba"--><!-- The following content is generated at 2024-02-01T20:28:01.881218+08:00. Any edits will be overridden! -->

- $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$::$\frac\infty\infty$ <!--SR:!2024-11-17,273,330-->
- $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$::$0\cdot\infty$ <!--SR:!2024-08-28,209,330-->
- $\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$::$\infty-\infty$ <!--SR:!2024-09-24,231,330-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$0^0$, $\infty^0$ <!--SR:!2024-07-21,169,290-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$1^\infty$ <!--SR:!2024-07-28,157,270-->

<!--/pytextgen-->

### indeterminate form–transformation to ∞/∞

<!--pytextgen generate section="1e32"--><!-- The following content is generated at 2024-02-01T20:28:01.927217+08:00. Any edits will be overridden! -->

- $\frac00$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$ <!--SR:!2024-08-23,205,330-->
- $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$ <!--SR:!2024-10-11,243,330-->
- $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$ <!--SR:!2024-11-30,282,330-->
- $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-07-26,170,310-->
- $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-11-02,261,330-->
- $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-11-13,269,330-->

<!--/pytextgen-->

<!--pytextgen generate section="ff01"--><!-- The following content is generated at 2024-02-01T20:28:01.993744+08:00. Any edits will be overridden! -->

- $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/g(x)}{1/f(x)}$::$\frac00$ <!--SR:!2024-10-28,256,330-->
- $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$::$0\cdot\infty$ <!--SR:!2024-09-18,226,330-->
- $\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$::$\infty-\infty$ <!--SR:!2024-09-05,199,310-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$0^0$, $\infty^0$ <!--SR:!2024-08-01,160,270-->
- $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$1^\infty$ <!--SR:!2024-06-06,119,250-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/L'Hôpital's_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
