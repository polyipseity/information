---
aliases:
  - list of trigonometric identities
  - trigonometric identities
tags:
  - flashcards/general/list_of_trigonometric_identities
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# list of trigonometric identities

## overview

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
  e.cwf_sects('4949', 'd996',),
  ('name',),
  (
    ('[angle sum and difference](#angle%20sum%20and%20difference)',),
    ('[linear combination](#linear%20combination)',),
    ('[multiple-angle](#multiple-angle)',),
    ('[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)',),
  ),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="4949"--><!-- The following content is generated at 2023-12-20T17:38:22.539723+08:00. Any edits will be overridden! -->

> | name |
> |-|
> | [angle sum and difference](#angle%20sum%20and%20difference) |
> | [linear combination](#linear%20combination) |
> | [multiple-angle](#multiple-angle) |
> | [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d996"--><!-- The following content is generated at 2023-12-20T17:38:22.606111+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[angle sum and difference](#angle%20sum%20and%20difference)
2. [angle sum and difference](#angle%20sum%20and%20difference)→:::←[linear combination](#linear%20combination)
3. [linear combination](#linear%20combination)→:::←[multiple-angle](#multiple-angle)
4. [multiple-angle](#multiple-angle)→:::←[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)
5. [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## angle sum and difference

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_map(
  e.cwf_sects('f823', '394a', None,),
  items_to_map(
    ('sine', R'$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$',),
    ('cosine', R'$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$',),
    ('tangent', R'$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$',),
  ),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f823"--><!-- The following content is generated at 2023-11-21T01:16:38.253997+08:00. Any edits will be overridden! -->

> 1. sine: $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
> 2. cosine: $\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$
> 3. tangent: $\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="394a"--><!-- The following content is generated at 2023-11-21T01:16:38.242448+08:00. Any edits will be overridden! -->

1. sine::$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
2. cosine::$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$
3. tangent::$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!example] examples
>
> - $\sin(1.73 \mp 2.45)$ ::: $\sin 1.73 \cos 2.45 \mp \cos 1.73 \sin 2.45$
> - $\cos(-0.56 \pm 9.23)$ ::: $\cos(-0.56) \cos 9.23 \mp \sin(-0.56) \sin 9.23$
> - $\tan(7.22 \mp 2.38)$ ::: $\frac{\tan 7.22 \mp \tan 2.38}{1 \pm \tan 7.22 \tan 2.38}$

## multiple-angle

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_map(
  e.cwf_sects('b023', 'ab2d', None,),
  items_to_map(
    ('sine', R'$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$',),
    ('cosine', R'$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$',),
    ('tangent', R'$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$',),
  ),
)
```
%%

### double-angle

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b023"--><!-- The following content is generated at 2023-11-21T01:16:58.994052+08:00. Any edits will be overridden! -->

> 1. sine: $\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$
> 2. cosine: $\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$
> 3. tangent: $\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab2d"--><!-- The following content is generated at 2023-11-21T01:16:59.014601+08:00. Any edits will be overridden! -->

1. sine::$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$
2. cosine::$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$
3. tangent::$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!tip] tip
>
> - [mnemonic](mnemonic.md): {{use [§ angle sum and difference](#angle%20sum%20and%20difference) to help with memorization}}

> [!example] examples
>
> - $\sin 7.42$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $2 \sin 3.71 \cos 3.71$
> - $\sin(-0.36)$ (square variant) ::: $(\sin(-0.18) + \cos(-0.18))^2 - 1$
> - $\sin 6.24$ (tangent variant) ::: $\frac{2 \tan 3.12}{1 + \tan^2 3.12}$
> - $\cos(-3.68)$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $\cos^2 (-1.84) - \sin^2 (-1.84)$
> - $\cos 9.98$ (cosine variant) ::: $2\cos^2 4.99 - 1$
> - $\cos 5.54$ (sine variant) ::: $1 - 2\sin^2 2.77$
> - $\cos(-9.22)$ (tangent variant) ::: $\frac{1 - \tan^2(-4.61)}{1 + \tan^2(-4.61)}$
> - $\tan 0.04$ ::: $\frac{2 \tan 0.02}{1 - \tan^2 0.02}$

## product-to-sum and sum-to-product

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import NULL_LOCATION
e = __env__
return chain.from_iterable(await gather(
  memorize_map(
    e.cwf_sects('dd91', '3213', None,),
    items_to_map(
      ('sine cosine', html_ul(R'$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$', R'$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$',),),
      ('sine sine', R'$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$',),
      ('cosine cosine', R'$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$'),
    ),
  ),
  memorize_map(
    e.cwf_sects('96fb', '39cd', None,),
    items_to_map(
      ('sine ± sine', R'$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$',),
      ('cosine + cosine', R'$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$',),
      ('cosine - cosine', R'$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$',),
      ('tangent ± tangent', R'$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$',),
    ),
  ),
))
```
%%

### product-to-sum

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd91"--><!-- The following content is generated at 2023-11-21T01:12:55.689441+08:00. Any edits will be overridden! -->

> 1. sine cosine: <ul><li>$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$</li><li>$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$</li></ul>
> 2. sine sine: $\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$
> 3. cosine cosine: $\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3213"--><!-- The following content is generated at 2023-11-21T01:12:55.772910+08:00. Any edits will be overridden! -->

1. sine cosine::<ul><li>$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$</li><li>$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$</li></ul>
2. sine sine::$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$
3. cosine cosine::$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!example] examples
>
> - $\sin 5.23 \cos 1.23$ ::: $\frac{\sin(5.23 + 1.23) + \sin(5.23 - 1.23)}2$
> - $\cos(-3.21) \sin 0.23$ ::: $\frac{\sin(-3.21 + 0.23) - \sin(-3.21 - 0.23)}2$
> - $\sin 6.22 \sin(-0.01)$ ::: $\frac{\cos(6.22 - (-0.01)) - \cos(6.22 + (-0.01))}2$
> - $\cos(-7.23) \cos(-1.23)$ ::: $\frac{\cos(-7.23 - (-1.23)) + \cos(-7.23 + (-1.23))}2$

### sum-to-product

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="96fb"--><!-- The following content is generated at 2023-11-21T01:12:55.755818+08:00. Any edits will be overridden! -->

> 1. sine ± sine: $\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$
> 2. cosine + cosine: $\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$
> 3. cosine - cosine: $\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$
> 4. tangent ± tangent: $\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="39cd"--><!-- The following content is generated at 2023-11-21T01:12:55.732650+08:00. Any edits will be overridden! -->

1. sine ± sine::$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$
2. cosine + cosine::$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$
3. cosine - cosine::$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$
4. tangent ± tangent::$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!example] examples
>
> - $\sin 3.23 \mp \sin(-1.52)$ ::: $2 \sin\left(\frac{3.23 \mp (-1.52)}2\right) \cos\left(\frac{3.23 \pm (-1.52)}2\right)$
> - $\cos(-2.23) + \cos 0.14$ ::: $2 \cos\left(\frac{-2.23 + 0.14}2\right) \cos\left(\frac{-2.23 - 0.14}2\right)$
> - $\cos(-6.88) - \cos(-2.45)$ ::: $-2 \sin\left(\frac{-6.88 + (-2.45)}2\right) \sin\left(\frac{-6.88 - (-2.45)}2\right)$
> - $\tan(-0.73) \mp \tan 2.55$ ::: $\frac{\sin(-0.73 \mp 2.55)}{\cos(-0.73) \cos 2.55}$

## linear combination

### sine and cosine

> __linear combination of sine and cosine__
>
> {{$$a \cos x + b \sin x = c \cos(x + \varphi)$$}}
>
> - where
>     - {{$c = \operatorname{sgn}(a) \sqrt{a^2 + b^2}, \varphi = \arctan(-b / a)$ or $c = \sqrt{a^2 + b^2}, \varphi = \operatorname{atan2}(-b, a)$}}
> - conditions: {{$a \ne 0$}}

> [!example] examples
>
> - $-2.64 \cos 3x + 3.22 \sin 3x$ (arctangent variant) ::: $-\sqrt{2.64^2 + 3.22^2} \cos(3x + \arctan(3.22 / 2.64))$
> - $-9.29 \cos(-2x) - 9.11 \sin(-2x)$ ([atan2](atan2.md) variant) ::: $\sqrt{9.29^2 + 9.11^2} \cos(-2x + \operatorname{atan2}(9.11, -9.29))$
> - $0 \cos 5x - 1.23 \sin 5x$ ::: $-1.23 \sin 5x$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/list_of_trigonometric_identities) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
