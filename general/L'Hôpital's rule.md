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

__{{L'Hôpital's} } rule__, also known as __{{Bernoulli's} } rule__, is {{a [theorem](theorem.md) used for evaluating [limits](limit%20of%20a%20function.md) of [indeterminate forms](indeterminate%20form.md) from [derivatives](derivative.md)} }.

> __L'Hôpital's rule__
>
> 1. {{Given [real-valued functions](real-valued%20function.md) $f$ and $g$ which are [differentiable](differentiable%20function.md) on, for two-sided limit, an open [interval](interval%20(mathematics).md) $I$ except possibly at an [extended real number](extended%20real%20number%20line.md) $c$ which is in $I$, or for limit at infinity or [one-sided limit](one-sided%20limit.md), an open [interval](interval%20(mathematics).md) with endpoint $c$,} }
> 2. {{if $\lim_{x\to{}c}f(x)=\lim_{x\to{}c}g(x)=0$ or $\lim_{x\to{}c}\lvert{g(x)}\rvert=\infty$, $g'(x)\ne0$ for all $x$ in $I$ except possibly $c$, and the [limit](limit%20of%20a%20functino.md) $\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$ exists or equals positive or negative [infinity](infinity.md),} }
> 3. {{then $\lim_{x\to{}c}\frac{f(x)}{g(x)}=\lim_{x\to{}c}\frac{f'(x)}{g'(x)}$.} }
> 4. {{If $c$ is a finite endpoint of $I$, the limits can be also be [one-sided limits](one-sided%20limit.md) $x\to{}c^+$ or $x\to{}c^-$.} }

## other indeterminate forms

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from itertools import chain as _chain
e = __env__
return await memorize_table(
  e.cwf_sects('948f', 'dd11'),
  (R"indeterminate form", R"conditions", R"transformation to $0/0$", R"transformation to $\infty/\infty$",),
  (
    (R"$\frac00$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$", R"", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$",),
    (R"$\frac\infty\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$",),
    (R"$0\cdot\infty$", R"$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$", R"$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$",),
    (R"$\infty-\infty$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$", R"$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$",),
    (R"$0^0$", R"$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
    (R"$1^\infty$", R"$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$"),
    (R"$\infty^0$", R"$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$", R"$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$",),
  ),
  lambda datum: _chain(datum[:1], map(cloze, datum[1:])),
)
```
%%

The following table lists out transformation from other [indeterminate forms](indeterminate%20form.md) for applying L'Hôpital's rule.

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="948f"--><!-- The following content is generated at 2023-11-27T00:27:56.638076+08:00. Any edits will be overridden! -->

> | indeterminate form | conditions | transformation to $0/0$ | transformation to $\infty/\infty$ |
> |-|-|-|-|
> | $\frac00$ | {{$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=0$}} |  | {{$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$}} |
> | $\frac\infty\infty$ | {{$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$}} | {{$\lim_{x\to{c} }\frac{f(x)}{g(x)}=\lim_{x\to{c} }\frac{1/f(x)}{1/g(x)}$}} |
> | $0\cdot\infty$ | {{$\lim_{x\to{c} }f(x)=0,\lim_{x\to{c} }g(x)=\infty$}} | {{$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{f(x)}{1/g(x)}$}} | {{$\lim_{x\to{c} }f(x)g(x)=\lim_{x\to{c} }\frac{g(x)}{1/f(x)}$}} |
> | $\infty-\infty$ | {{$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=\infty$}} | {{$\lim_{x\to{c} }(f(x)-g(x))=\lim_{x\to{c} }\frac{1/g(x)-1/f(x)}{1/(f(x)g(x))}$}} | {{$\lim_{x\to{c} }(f(x)-g(x))=\ln\lim_{x\to{c} }\frac{e^{f(x)} }{e^{g(x)} }$}} |
> | $0^0$ | {{$\lim_{x\to{c} }f(x)=0^+,\lim_{x\to{c} }g(x)=0$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$}} |
> | $1^\infty$ | {{$\lim_{x\to{c} }f(x)=1,\lim_{x\to{c} }g(x)=\infty$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$}} |
> | $\infty^0$ | {{$\lim_{x\to{c} }f(x)=\infty,\lim_{x\to{c} }g(x)=0$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{g(x)}{1/\ln{f(x)} }$}} | {{$\lim_{x\to{c} }f(x)^{g(x)}=\exp\lim_{x\to{c} }\frac{\ln{f(x)} }{1/g(x)}$}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd11"--><!-- The following content is generated at 2023-11-24T23:07:19.372288+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←$\frac00$
2. $\frac00$→:::←$\frac\infty\infty$
3. $\frac\infty\infty$→:::←$0\cdot\infty$
4. $0\cdot\infty$→:::←$\infty-\infty$
5. $\infty-\infty$→:::←$0^0$
6. $0^0$→:::←$1^\infty$
7. $1^\infty$→:::←$\infty^0$
8. $\infty^0$→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
