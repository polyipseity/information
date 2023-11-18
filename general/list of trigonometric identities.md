---
aliases:
  - list of trigonometric identities
  - trigonometric identities
tags:
  - flashcards/general/list_of_trigonometric_identities
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
    ('[multiple-angle](#multiple-angle)',),
    ('[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="4949"--><!-- The following content is generated at 2023-04-09T19:41:29.712881+08:00. Any edits will be overridden! -->

> | name |
> |-|
> | {{[angle sum and difference](#angle%20sum%20and%20difference)}} |
> | {{[multiple-angle](#multiple-angle)}} |
> | {{[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)}} | <!--SR:!2025-04-09,543,310!2024-06-20,338,330!2024-06-16,334,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d996"--><!-- The following content is generated at 2023-04-09T19:41:29.732199+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[angle sum and difference](#angle%20sum%20and%20difference) <!--SR:!2024-06-17,335,330!2024-06-22,340,330-->
2. [angle sum and difference](#angle%20sum%20and%20difference)→:::←[multiple-angle](#multiple-angle) <!--SR:!2024-06-18,336,330!2024-06-23,341,330-->
3. [multiple-angle](#multiple-angle)→:::←[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) <!--SR:!2023-12-19,101,250!2024-06-24,342,330-->
4. [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)→:::←_(end)_ <!--SR:!2024-06-19,337,330!2025-03-31,535,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## angle sum and difference

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
  (*e.cwf_sects('394a',), NULL_LOCATION,),
  ('type', 'identity',),
  (
    ('sine', R'$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$',),
    ('cosine', R'$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$',),
    ('tangent', R'$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$',),
  ),
  lambda datum: (*datum[:1], cloze(datum[1]), *datum[2:],),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="394a"--><!-- The following content is generated at 2023-04-09T19:23:12.390963+08:00. Any edits will be overridden! -->

> | type | identity |
> |-|-|
> | sine | {{$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$}} |
> | cosine | {{$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$}} |
> | tangent | {{$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$}} | <!--SR:!2024-01-03,152,250!2025-03-23,527,310!2023-11-28,144,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## multiple-angle

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
  (*e.cwf_sects('ab2d',), NULL_LOCATION,),
  ('type', 'identity',),
  (
    ('sine', R'$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$',),
    ('cosine', R'$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$',),
    ('tangent', R'$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$',),
  ),
  lambda datum: (*datum[:1], cloze(datum[1]), *datum[2:],),
)
```
%%

### double-angle

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab2d"--><!-- The following content is generated at 2023-04-09T19:43:23.769796+08:00. Any edits will be overridden! -->

> | type | identity |
> |-|-|
> | sine | {{$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$}} |
> | cosine | {{$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$}} |
> | tangent | {{$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$}} | <!--SR:!2024-09-06,312,250!2024-08-01,314,270!2023-12-25,146,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## product-to-sum and sum-to-product

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import NULL_LOCATION
e = __env__
return chain.from_iterable(await gather(
  memorize_table(
    (*e.cwf_sects('3213',), NULL_LOCATION,),
    ('type', 'identity',),
    (
      ('sine cosine', html_ul(R'$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$', R'$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$',),),
      ('sine sine', R'$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$',),
      ('cosine cosine', R'$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$')
    ),
    lambda datum: (*datum[:1], cloze(datum[1]), *datum[2:],),
  ),
  memorize_table(
    (*e.cwf_sects('39cd',), NULL_LOCATION,),
    ('type', 'identity',),
    (
      ('sine ± sine', R'$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$',),
      ('cosine + cosine', R'$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$',),
      ('cosine - cosine', R'$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$',),
      ('tangent ± tangent', R'$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$',),
    ),
    lambda datum: (*datum[:1], cloze(datum[1]), *datum[2:],),
  ),
))
```
%%

### product-to-sum

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3213"--><!-- The following content is generated at 2023-04-09T19:58:50.846533+08:00. Any edits will be overridden! -->

> | type | identity |
> |-|-|
> | sine cosine | {{<ul><li>$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$</li><li>$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$</li></ul>}} |
> | sine sine | {{$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$}} |
> | cosine cosine | {{$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$}} | <!--SR:!2023-12-02,56,190!2024-01-23,85,190!2024-10-24,342,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### sum-to-product

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="39cd"--><!-- The following content is generated at 2023-04-09T20:00:11.816087+08:00. Any edits will be overridden! -->

> | type | identity |
> |-|-|
> | sine ± sine | {{$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$}} |
> | cosine + cosine | {{$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$}} |
> | cosine - cosine | {{$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$}} |
> | tangent ± tangent | {{$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$}} | <!--SR:!2024-11-03,359,250!2024-05-30,195,230!2023-11-19,71,190!2024-01-06,58,150-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
