---
aliases:
  - list of trigonometric identities
  - trigonometric identities
tags:
  - flashcard/general/list_of_trigonometric_identities
  - language/in/English
---

# list of trigonometric identities

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

## overview

%%

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('4949', 'd996',),
  ('name',),
  (
    ('[Pythagorean identities](#Pythagorean%20identities)',),
    ('[angle sum and difference](#angle%20sum%20and%20difference)',),
    ('[linear combination](#linear%20combination)',),
    ('[multiple-angle](#multiple-angle)',),
    ('[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)',),
  ),
)
```

%%

<!--pytextgen generate section="4949"--><!-- The following content is generated at 2024-01-03T09:39:48.167446+08:00. Any edits will be overridden! -->

> | name |
> |-|
> | [Pythagorean identities](#Pythagorean%20identities) |
> | [angle sum and difference](#angle%20sum%20and%20difference) |
> | [linear combination](#linear%20combination) |
> | [multiple-angle](#multiple-angle) |
> | [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) |

<!--/pytextgen-->

<!--pytextgen generate section="d996"--><!-- The following content is generated at 2024-01-04T20:17:52.198336+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[Pythagorean identities](#Pythagorean%20identities) <!--SR:!2025-05-03,383,360!2025-04-05,361,362-->
- [Pythagorean identities](#Pythagorean%20identities)→:::←[angle sum and difference](#angle%20sum%20and%20difference) <!--SR:!2024-06-17,335,330!2024-06-22,340,330-->
- [angle sum and difference](#angle%20sum%20and%20difference)→:::←[linear combination](#linear%20combination) <!--SR:!2024-12-04,229,289!2024-11-16,236,329-->
- [linear combination](#linear%20combination)→:::←[multiple-angle](#multiple-angle) <!--SR:!2024-06-18,336,330!2024-06-23,341,330-->
- [multiple-angle](#multiple-angle)→:::←[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) <!--SR:!2024-12-07,354,270!2024-06-24,342,330-->
- [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)→:::←_(end)_ <!--SR:!2024-06-19,337,330!2025-03-31,535,310-->

<!--/pytextgen-->

## Pythagorean identities

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_map(
  __env__.cwf_sects('958f', 'ba01', None,),
  items_to_map(
    ('normal', R'$\sin^2 \theta + \cos^2 \theta = 1$',),
    ('divided by sine', R'$1 + \cot^2 \theta = \csc^2 \theta$',),
    ('divided by cosine', R'$1 + \tan^2 \theta = \sec^2 \theta$',),
    ('divided by sine and cosine', R'$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$',),
  ),
)
```

%%

<!--pytextgen generate section="958f"--><!-- The following content is generated at 2023-12-29T17:59:38.650037+08:00. Any edits will be overridden! -->

> 1. normal: $\sin^2 \theta + \cos^2 \theta = 1$
> 2. divided by sine: $1 + \cot^2 \theta = \csc^2 \theta$
> 3. divided by cosine: $1 + \tan^2 \theta = \sec^2 \theta$
> 4. divided by sine and cosine: $\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$

<!--/pytextgen-->

<!--pytextgen generate section="ba01"--><!-- The following content is generated at 2024-01-04T20:17:52.215336+08:00. Any edits will be overridden! -->

- normal::$\sin^2 \theta + \cos^2 \theta = 1$ <!--SR:!2025-05-07,387,360-->
- divided by sine::$1 + \cot^2 \theta = \csc^2 \theta$ <!--SR:!2025-03-06,336,360-->
- divided by cosine::$1 + \tan^2 \theta = \sec^2 \theta$ <!--SR:!2024-07-27,148,320-->
- divided by sine and cosine::$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$ <!--SR:!2025-04-14,368,360-->

<!--/pytextgen-->

> [!example] examples
>
> - $\cos^2 6.52 + \sin^2 6.52$ ::: $1$ <!--SR:!2025-04-15,369,360!2025-03-19,350,360-->
> - $\cot^2 (-3.52) + 1$ ::: $\csc^2 (-3.52)$ <!--SR:!2024-11-23,237,340!2025-04-09,364,360-->
> - $1 + \tan^2 (-7.23)$ ::: $\sec^2 (-7.23)$ <!--SR:!2024-12-15,251,340!2024-06-14,116,320-->
> - $\csc^2 0.23 + \sec^2 0.23$ ::: $\sec^2 0.23 \csc^2 0.23$ <!--SR:!2024-11-16,233,339!2024-09-24,152,340-->

## angle sum and difference

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_map(
  __env__.cwf_sects('f823', '394a', None,),
  items_to_map(
    ('sine', R'$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$',),
    ('cosine', R'$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$',),
    ('tangent', R'$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$',),
  ),
)
```

%%

<!--pytextgen generate section="f823"--><!-- The following content is generated at 2023-11-21T01:16:38.253997+08:00. Any edits will be overridden! -->

> 1. sine: $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
> 2. cosine: $\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$
> 3. tangent: $\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$

<!--/pytextgen-->

<!--pytextgen generate section="394a"--><!-- The following content is generated at 2024-01-04T20:17:52.256338+08:00. Any edits will be overridden! -->

- sine::$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$ <!--SR:!2024-09-06,172,230-->
- cosine::$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$ <!--SR:!2025-03-23,527,310-->
- tangent::$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$ <!--SR:!2024-09-28,230,250-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin(1.73 \mp 2.45)$ ::: $\sin 1.73 \cos 2.45 \mp \sin 2.45 \cos 1.73$ <!--SR:!2025-01-22,260,287!2024-10-11,212,327-->
> - $\cos(-0.56 \pm 9.23)$ ::: $\cos(-0.56) \cos 9.23 \mp \sin(-0.56) \sin 9.23$ <!--SR:!2024-09-22,175,267!2024-07-03,134,307-->
> - $\tan(7.22 \mp 2.38)$ ::: $\frac{\tan 7.22 \mp \tan 2.38}{1 \pm \tan 2.38 \tan 7.22}$ <!--SR:!2024-07-16,76,247!2025-02-04,269,287-->

## multiple-angle

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_map(
  __env__.cwf_sects('b023', 'ab2d', None,),
  items_to_map(
    ('sine', R'$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$',),
    ('cosine', R'$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$',),
    ('tangent', R'$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$',),
  ),
)
```

%%

### double-angle

<!--pytextgen generate section="b023"--><!-- The following content is generated at 2023-11-21T01:16:58.994052+08:00. Any edits will be overridden! -->

> 1. sine: $\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$
> 2. cosine: $\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$
> 3. tangent: $\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$

<!--/pytextgen-->

<!--pytextgen generate section="ab2d"--><!-- The following content is generated at 2024-01-04T20:17:52.289866+08:00. Any edits will be overridden! -->

- sine::$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$ <!--SR:!2024-09-06,312,250-->
- cosine::$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$ <!--SR:!2024-08-01,314,270-->
- tangent::$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$ <!--SR:!2025-04-12,474,250-->

<!--/pytextgen-->

> [!tip] tips
>
> - [mnemonic](mnemonic.md) ::: use [§ angle sum and difference](#angle%20sum%20and%20difference) to help with memorization <!--SR:!2024-12-21,286,345!2024-06-26,86,354-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $\sin 7.42$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $2 \cos 3.71 \sin 3.71$ <!--SR:!2024-08-09,178,327!2024-11-21,241,327-->
> - $\sin(-0.36)$ (square variant) ::: $(\cos 0.18 - \sin 0.18)^2 - 1$ <!--SR:!2024-05-24,105,287!2024-10-14,168,287-->
> - $\sin 6.24$ (tangent variant) ::: $\frac{2 \tan 3.12}{1 + \tan^2 3.12}$ <!--SR:!2024-06-18,127,307!2024-09-11,121,247-->
> - $\cos(-3.68)$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $\cos^2 1.84 - \sin^2 1.84$ <!--SR:!2024-11-26,265,347!2024-12-05,231,287-->
> - $\cos 9.98$ (cosine variant) ::: $2\cos^2 4.99 - 1$ <!--SR:!2024-11-25,244,327!2024-12-19,283,347-->
> - $\cos 5.54$ (sine variant) ::: $1 - 2\sin^2 2.77$ <!--SR:!2024-12-28,290,347!2024-09-28,202,327-->
> - $\cos(-9.22)$ (tangent variant) ::: $\frac{1 - \tan^2 4.61}{1 + \tan^2 4.61}$ <!--SR:!2024-08-09,159,307!2024-10-28,211,287-->
> - $\tan 0.04$ ::: $\frac{2 \tan 0.02}{1 - \tan^2 0.02}$ <!--SR:!2025-02-13,291,307!2024-10-28,186,287-->

## product-to-sum and sum-to-product

%%

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import NULL_LOCATION
return chain.from_iterable(await gather(
  memorize_map(
    __env__.cwf_sects('dd91', '3213', None,),
    items_to_map(
      ('sine cosine', R'$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$',),
      ('cosine sine', R'$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$',),
      ('sine sine', R'$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$',),
      ('cosine cosine', R'$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$'),
    ),
  ),
  memorize_map(
    __env__.cwf_sects('96fb', '39cd', None,),
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

<!--pytextgen generate section="dd91"--><!-- The following content is generated at 2023-12-31T17:50:22.105562+08:00. Any edits will be overridden! -->

> 1. sine cosine: $\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$
> 2. cosine sine: $\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$
> 3. sine sine: $\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$
> 4. cosine cosine: $\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$

<!--/pytextgen-->

<!--pytextgen generate section="3213"--><!-- The following content is generated at 2024-01-04T20:17:52.372879+08:00. Any edits will be overridden! -->

- sine cosine::$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$ <!--SR:!2024-07-06,124,190-->
- cosine sine::$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$ <!--SR:!2024-07-09,127,190-->
- sine sine::$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$ <!--SR:!2024-09-10,231,210-->
- cosine cosine::$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$ <!--SR:!2024-10-24,342,250-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 5.23 \cos 1.23$ ::: $\frac{\sin 6.46 + \sin 4}2$ <!--SR:!2024-06-14,124,307!2024-06-02,111,287-->
> - $\cos(-3.21) \sin 0.23$ ::: $\frac{\sin 3.44 - \sin 2.98}2$ <!--SR:!2024-08-22,173,307!2024-06-28,48,207-->
> - $\sin 6.22 \sin(-0.01)$ ::: $\frac{\cos 6.23 - \cos 6.21}2$ <!--SR:!2025-03-09,306,307!2024-07-30,124,227-->
> - $\cos(-7.23) \cos(-1.23)$ ::: $\frac{\cos 6 + \cos 8.46}2$ <!--SR:!2024-08-11,92,267!2024-08-25,168,287-->

### sum-to-product

<!--pytextgen generate section="96fb"--><!-- The following content is generated at 2023-11-21T01:12:55.755818+08:00. Any edits will be overridden! -->

> 1. sine ± sine: $\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$
> 2. cosine + cosine: $\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$
> 3. cosine - cosine: $\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$
> 4. tangent ± tangent: $\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$

<!--/pytextgen-->

<!--pytextgen generate section="39cd"--><!-- The following content is generated at 2024-01-04T20:17:52.322868+08:00. Any edits will be overridden! -->

- sine ± sine::$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$ <!--SR:!2024-11-03,359,250-->
- cosine + cosine::$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$ <!--SR:!2024-05-30,195,230-->
- cosine - cosine::$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$ <!--SR:!2024-12-18,254,190-->
- tangent ± tangent::$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$ <!--SR:!2024-08-17,134,150-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 3.23 \mp \sin(-1.52)$ ::: $2 \sin\left(\frac{3.23 \pm 1.52}2\right) \cos\left(\frac{3.23 \mp 1.52}2\right)$ <!--SR:!2024-06-30,50,227!2024-11-18,210,267-->
> - $\cos(-2.23) + \cos 0.14$ ::: $2 \cos 1.045 \cos 1.185$ <!--SR:!2024-07-25,165,327!2024-08-07,146,267-->
> - $\cos(-6.88) - \cos(-2.45)$ ::: $-2 \sin 4.665 \sin 2.215$ <!--SR:!2024-08-14,167,307!2024-09-11,167,267-->
> - $\tan(-0.73) \mp \tan 2.55$ ::: $\frac{\sin(-0.73 \mp 2.55)}{\cos 0.73 \cos 2.55}$ <!--SR:!2024-05-31,113,307!2024-08-25,174,287-->

## linear combination

### sine and cosine

> __linear combination of sine and cosine__
>
> {{$$a \cos x + b \sin x = c \cos(x + \varphi)$$}}
>
> - where
>   - {{$c = \operatorname{sgn}(a) \sqrt{a^2 + b^2}, \varphi = \arctan(-b / a)$ or $c = \sqrt{a^2 + b^2}, \varphi = \operatorname{atan2}(-b, a)$}}
> - conditions: {{$a \ne 0$}} <!--SR:!2024-08-02,157,309!2024-11-07,213,289!2024-10-23,219,329-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $-2.64 \cos 3x + 3.22 \sin 3x$ (arctangent variant) ::: $-\sqrt{2.64^2 + 3.22^2} \cos(3x + \arctan(3.22 / 2.64))$ <!--SR:!2024-12-20,245,289!2024-07-29,126,249-->
> - $-9.29 \cos(-2x) - 9.11 \sin(-2x)$ ([atan2](atan2.md) variant) ::: $\sqrt{9.29^2 + 9.11^2} \cos(2x - \operatorname{atan2}(9.11, -9.29))$ <!--SR:!2024-05-30,45,269!2024-06-10,37,229-->
> - $0 \cos 5x - 1.23 \sin 5x$ ::: $1.23 \sin(-5x)$ <!--SR:!2024-10-17,213,329!2024-12-02,249,329-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/list_of_trigonometric_identities) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
