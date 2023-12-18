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
  - flashcards/general/L_Hôpital_s_rule
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# L'Hôpital's rule

__{{L'Hôpital's}} rule__, also known as __{{Bernoulli's}} rule__, is {{a [theorem](theorem.md) used for evaluating [limits](limit%20of%20a%20function.md) of [indeterminate forms](indeterminate%20form.md) from [derivatives](derivative.md)}}. <!--SR:!2023-12-19,18,300!2024-01-15,33,280!2023-12-19,18,300-->

> __L'Hôpital's rule__
>
> 1. {{Given [real-valued functions](real-valued%20function.md) $f$ and $g$ which are [differentiable](differentiable%20function.md) on, for two-sided limit, an open [interval](interval%20(mathematics).md) $I$ except possibly at an [extended real number](extended%20real%20number%20line.md) $c$ which is in $I$, or for limit at infinity or [one-sided limit](one-sided%20limit.md), an open [interval](interval%20(mathematics).md) with endpoint $c$,}}
> 2. {{if $\lim_{x\to{}c}f(x)=\lim_{x\to{}c}g(x)=0$ or $\lim_{x\to{}c}\lvert{g(x)}\rvert=\infty$, $g'(x)\ne0$ for all $x$ in $I$ except possibly $c$, and the [limit](limit%20of%20a%20functino.md) $\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$ exists or equals positive or negative [infinity](infinity.md),}}
> 3. {{then $\lim_{x\to{}c}\frac{f(x)}{g(x)}=\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$.}}
> 4. {{If $c$ is a finite endpoint of $I$, the limits can be also be [one-sided limits](one-sided%20limit.md) $x\to{}c^+$ or $x\to{}c^-$.}} <!--SR:!2024-01-10,29,280!2023-12-25,18,260!2023-12-19,18,300!2024-01-31,46,300-->

## other indeterminate forms

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = (R"indeterminate form", R"conditions", R"transformation to 0/0", R"transformation to ∞/∞",)
table = (
  (R"$\frac00$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$", R"", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$",),
  (R"$\frac\infty\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$", R"",),
  (R"$0\cdot\infty$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$",),
  (R"$\infty-\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$", R"$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$",),
  (R"$0^0$", R"$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
  (R"$1^\infty$", R"$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$",),
  (R"$\infty^0$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    e.cwf_sects("948f", "dd11",),
    headers,
    table,
  ),
  memorize_map(
    e.cwf_sects(None, "5dab", None,),
    items_to_map(*(entry[:2] for entry in table)),
  ),
  memorize_map(
    e.cwf_sects(None, "679d", "39ba",),
    items_to_map(*((entry[0], entry[2]) for entry in table if entry[2])),
  ),
  memorize_map(
    e.cwf_sects(None, "1e32", "ff01",),
    items_to_map(*((entry[0], entry[3]) for entry in table if entry[3])),
  ),
))
```
%%

The following table lists out transformation from other [indeterminate forms](indeterminate%20form.md) for applying L'Hôpital's rule.

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="948f"--><!-- The following content is generated at 2023-11-27T09:10:04.382841+08:00. Any edits will be overridden! -->

> | indeterminate form | conditions | transformation to 0/0 | transformation to ∞/∞ |
> |-|-|-|-|
> | $\frac00$ | $\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$ |  | $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$ |
> | $\frac\infty\infty$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$ |  |
> | $0\cdot\infty$ | $\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$ | $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$ |
> | $\infty-\infty$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$ | $\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$ |
> | $0^0$ | $\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ |
> | $1^\infty$ | $\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ |
> | $\infty^0$ | $\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ | $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd11"--><!-- The following content is generated at 2023-11-24T23:07:19.372288+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←$\frac00$ <!--SR:!2024-02-15,60,310!2024-02-02,50,310-->
2. $\frac00$→:::←$\frac\infty\infty$ <!--SR:!2024-02-23,67,310!2024-02-10,56,310-->
3. $\frac\infty\infty$→:::←$0\cdot\infty$ <!--SR:!2024-01-17,36,290!2023-12-24,8,270-->
4. $0\cdot\infty$→:::←$\infty-\infty$ <!--SR:!2024-01-22,38,270!2024-02-24,68,310-->
5. $\infty-\infty$→:::←$0^0$ <!--SR:!2023-12-24,6,250!2023-12-20,8,230-->
6. $0^0$→:::←$1^\infty$ <!--SR:!2023-12-23,17,270!2024-01-15,34,290-->
7. $1^\infty$→:::←$\infty^0$ <!--SR:!2023-12-22,7,270!2024-01-26,44,290-->
8. $\infty^0$→:::←_(end)_ <!--SR:!2024-02-05,52,310!2024-01-21,38,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### indeterminate form–conditions

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5dab"--><!-- The following content is generated at 2023-11-27T09:10:04.330437+08:00. Any edits will be overridden! -->

1. $\frac00$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-02-14,60,310-->
2. $\frac\infty\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-02-11,58,310-->
3. $0\cdot\infty$::$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-02-15,61,310-->
4. $\infty-\infty$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-02-09,56,310-->
5. $0^0$::$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-01-28,42,290-->
6. $1^\infty$::$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$ <!--SR:!2024-02-24,68,310-->
7. $\infty^0$::$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$ <!--SR:!2024-02-03,51,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### indeterminate form-transformation to 0/0

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="679d"--><!-- The following content is generated at 2023-11-27T09:10:42.321134+08:00. Any edits will be overridden! -->

1. $\frac\infty\infty$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$ <!--SR:!2024-02-11,58,310-->
2. $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$ <!--SR:!2024-02-16,61,310-->
3. $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$ <!--SR:!2024-01-27,42,290-->
4. $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-01-05,24,250-->
5. $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-02-16,61,310-->
6. $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-01-23,39,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="39ba"--><!-- The following content is generated at 2023-11-27T09:10:42.200047+08:00. Any edits will be overridden! -->

1. $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$::$\frac\infty\infty$ <!--SR:!2024-02-18,64,310-->
2. $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$::$0\cdot\infty$ <!--SR:!2024-02-01,49,310-->
3. $\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$::$\infty-\infty$ <!--SR:!2024-02-06,54,310-->
4. $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$0^0$, $\infty^0$ <!--SR:!2023-12-20,13,250-->
5. $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$1^\infty$ <!--SR:!2023-12-20,11,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### indeterminate form–transformation to ∞/∞

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1e32"--><!-- The following content is generated at 2023-11-27T09:10:42.252594+08:00. Any edits will be overridden! -->

1. $\frac00$::$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$ <!--SR:!2024-01-31,48,310-->
2. $0\cdot\infty$::$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$ <!--SR:!2024-02-11,57,310-->
3. $\infty-\infty$::$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$ <!--SR:!2024-02-22,66,310-->
4. $0^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-02-07,55,310-->
5. $1^\infty$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$ <!--SR:!2024-02-15,61,310-->
6. $\infty^0$::$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$ <!--SR:!2024-02-18,63,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff01"--><!-- The following content is generated at 2023-11-27T09:10:42.289138+08:00. Any edits will be overridden! -->

1. $\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$::$\frac00$ <!--SR:!2024-02-15,60,310-->
2. $\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$::$0\cdot\infty$ <!--SR:!2024-02-05,53,310-->
3. $\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$::$\infty-\infty$ <!--SR:!2024-02-19,64,310-->
4. $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$::$0^0$, $\infty^0$ <!--SR:!2023-12-26,17,250-->
5. $\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$::$1^\infty$ <!--SR:!2024-01-02,17,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
