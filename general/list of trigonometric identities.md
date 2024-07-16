---
aliases:
  - list of trigonometric identities
  - trigonometric identities
tags:
  - flashcard/general/list_of_trigonometric_identities
  - functional/list
  - language/in/English
---

# list of trigonometric identities

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## overview

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('4949', 'd996'),
  ('name',),
  (
    (R'[Pythagorean identities](#Pythagorean%20identities)',),
    (R'[angle sum and difference](#angle%20sum%20and%20difference)',),
    (R'[linear combination](#linear%20combination)',),
    (R'[multiple-angle](#multiple-angle)',),
    (R'[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)',),
  ),
)
```

<!--pytextgen generate section="4949"--><!-- The following content is generated at 2024-07-11T08:29:28.938003+08:00. Any edits will be overridden! -->

> | name |
> |-|
> | [Pythagorean identities](#Pythagorean%20identities) |
> | [angle sum and difference](#angle%20sum%20and%20difference) |
> | [linear combination](#linear%20combination) |
> | [multiple-angle](#multiple-angle) |
> | [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) |

<!--/pytextgen-->

<!--pytextgen generate section="d996"--><!-- The following content is generated at 2024-07-11T08:29:28.983272+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[Pythagorean identities](#Pythagorean%20identities) <!--SR:!2025-05-03,383,360!2025-04-05,361,362-->
- [Pythagorean identities](#Pythagorean%20identities)→:::←[angle sum and difference](#angle%20sum%20and%20difference) <!--SR:!2027-06-27,1105,330!2028-09-15,1546,350-->
- [angle sum and difference](#angle%20sum%20and%20difference)→:::←[linear combination](#linear%20combination) <!--SR:!2024-12-04,229,289!2024-11-16,236,329-->
- [linear combination](#linear%20combination)→:::←[multiple-angle](#multiple-angle) <!--SR:!2027-07-01,1108,330!2027-07-22,1124,330-->
- [multiple-angle](#multiple-angle)→:::←[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) <!--SR:!2024-12-07,354,270!2027-07-28,1128,330-->
- [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)→:::←_(end)_ <!--SR:!2028-08-29,1532,350!2025-03-31,535,310-->

<!--/pytextgen-->

## Pythagorean identities

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('958f', 'ba01', None),
  items_to_map(
    (R'normal', R'$$\sin^2 \theta + \cos^2 \theta = 1$$'),
    (R'divided by sine', R'$$1 + \cot^2 \theta = \csc^2 \theta$$'),
    (R'divided by cosine', R'$$1 + \tan^2 \theta = \sec^2 \theta$$'),
    (R'divided by sine and cosine', R'$$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$$'),
  ),
)
```

<!--pytextgen generate section="958f"--><!-- The following content is generated at 2024-07-10T23:14:21.879549+08:00. Any edits will be overridden! -->

> 1. normal: $$\sin^2 \theta + \cos^2 \theta = 1$$
> 2. divided by sine: $$1 + \cot^2 \theta = \csc^2 \theta$$
> 3. divided by cosine: $$1 + \tan^2 \theta = \sec^2 \theta$$
> 4. divided by sine and cosine: $$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$$

<!--/pytextgen-->

<!--pytextgen generate section="ba01"--><!-- The following content is generated at 2024-07-10T23:14:21.851131+08:00. Any edits will be overridden! -->

- normal::$$\sin^2 \theta + \cos^2 \theta = 1$$ <!--SR:!2025-05-07,387,360-->
- divided by sine::$$1 + \cot^2 \theta = \csc^2 \theta$$ <!--SR:!2025-03-06,336,360-->
- divided by cosine::$$1 + \tan^2 \theta = \sec^2 \theta$$ <!--SR:!2024-07-27,148,320-->
- divided by sine and cosine::$$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$$ <!--SR:!2025-04-14,368,360-->

<!--/pytextgen-->

> [!example] examples
>
> - $\cos^2 6.52 + \sin^2 6.52$ ::: $1$ <!--SR:!2025-04-15,369,360!2025-03-19,350,360-->
> - $\cot^2 (-3.52) + 1$ ::: $\csc^2 (-3.52)$ <!--SR:!2024-11-23,237,340!2025-04-09,364,360-->
> - $1 + \tan^2 (-7.23)$ ::: $\sec^2 (-7.23)$ <!--SR:!2024-12-15,251,340!2025-06-19,370,320-->
> - $\csc^2 0.23 + \sec^2 0.23$ ::: $\sec^2 0.23 \csc^2 0.23$ <!--SR:!2024-11-16,233,339!2024-09-24,152,340-->

## angle sum and difference

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('f823', '394a', None),
  items_to_map(
    (R'sine', R'$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$'),
    (R'cosine', R'$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$'),
    (R'tangent', R'$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$'),
  ),
)
```

<!--pytextgen generate section="f823"--><!-- The following content is generated at 2024-07-10T23:14:21.957811+08:00. Any edits will be overridden! -->

> 1. sine: $$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$
> 2. cosine: $$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$
> 3. tangent: $$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$

<!--/pytextgen-->

<!--pytextgen generate section="394a"--><!-- The following content is generated at 2024-07-10T23:14:21.914301+08:00. Any edits will be overridden! -->

- sine::$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$ <!--SR:!2024-09-06,172,230-->
- cosine::$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$ <!--SR:!2025-03-23,527,310-->
- tangent::$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$ <!--SR:!2024-09-28,230,250-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin(1.73 \mp 2.45)$ ::: $\sin 1.73 \cos 2.45 \mp \sin 2.45 \cos 1.73$ <!--SR:!2025-01-22,260,287!2024-10-11,212,327-->
> - $\cos(-0.56 \pm 9.23)$ ::: $\cos(-0.56) \cos 9.23 \mp \sin(-0.56) \sin 9.23$ <!--SR:!2024-09-22,175,267!2025-08-17,410,307-->
> - $\tan(7.22 \mp 2.38)$ ::: $\frac{\tan 7.22 \mp \tan 2.38}{1 \pm \tan 2.38 \tan 7.22}$ <!--SR:!2025-01-22,190,247!2025-02-04,269,287-->

## multiple-angle

### double-angle

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('b023', 'ab2d', None),
  items_to_map(
    (R'sine', R'$$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$'),
    (R'cosine', R'$$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$'),
    (R'tangent', R'$$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$'),
  ),
)
```

<!--pytextgen generate section="b023"--><!-- The following content is generated at 2024-07-10T23:14:22.063540+08:00. Any edits will be overridden! -->

> 1. sine: $$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$
> 2. cosine: $$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$
> 3. tangent: $$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$

<!--/pytextgen-->

<!--pytextgen generate section="ab2d"--><!-- The following content is generated at 2024-07-10T23:14:22.112551+08:00. Any edits will be overridden! -->

- sine::$$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$ <!--SR:!2024-09-06,312,250-->
- cosine::$$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$ <!--SR:!2024-08-01,314,270-->
- tangent::$$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$ <!--SR:!2025-04-12,474,250-->

<!--/pytextgen-->

> [!tip] tips
>
> - [mnemonic](mnemonic.md) ::: use [§ angle sum and difference](#angle%20sum%20and%20difference) to help with memorization <!--SR:!2024-12-21,286,345!2025-04-25,303,354-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $\sin 7.42$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $2 \cos 3.71 \sin 3.71$ <!--SR:!2024-08-09,178,327!2024-11-21,241,327-->
> - $\sin(-0.36)$ (square variant) ::: $(\cos 0.18 - \sin 0.18)^2 - 1$ <!--SR:!2025-03-20,300,287!2024-10-14,168,287-->
> - $\sin 6.24$ (tangent variant) ::: $\frac{2 \tan 3.12}{1 + \tan^2 3.12}$ <!--SR:!2025-07-12,389,307!2024-09-11,121,247-->
> - $\cos(-3.68)$ ([angle sum](#angle%20sum%20and%20difference) variant) ::: $\cos^2 1.84 - \sin^2 1.84$ <!--SR:!2024-11-26,265,347!2024-12-05,231,287-->
> - $\cos 9.98$ (cosine variant) ::: $2\cos^2 4.99 - 1$ <!--SR:!2024-11-25,244,327!2024-12-19,283,347-->
> - $\cos 5.54$ (sine variant) ::: $1 - 2\sin^2 2.77$ <!--SR:!2024-12-28,290,347!2024-09-28,202,327-->
> - $\cos(-9.22)$ (tangent variant) ::: $\frac{1 - \tan^2 4.61}{1 + \tan^2 4.61}$ <!--SR:!2024-08-09,159,307!2024-10-28,211,287-->
> - $\tan 0.04$ ::: $\frac{2 \tan 0.02}{1 - \tan^2 0.02}$ <!--SR:!2025-02-13,291,307!2024-10-28,186,287-->

### half-angle

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("d7f1", "3759", None),
  items_to_map(
    (R"sine", R"$$\sin \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac {1 - \cos \theta} 2}$$"),
    (R"cosine", R"$$\cos \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac {1 + \cos \theta} 2}$$"),
    (R"tangent", R"$$\tan \frac \theta 2 = \frac {1 - \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 + \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 - \cos \theta} {1 + \cos \theta} } = \csc \theta - \cot \theta = \frac {\tan \theta} {1 + \sec \theta} = \frac {-1 + \operatorname{sgn}(\cos \theta)\sqrt{1 + \tan^2 \theta} } {\tan \theta}$$"),
    (R"secant", R"$$\sec \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac 2 {1 + \cos \theta} }$$"),
    (R"cosecant", R"$$\csc \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac 2 {1 - \cos \theta} }$$"),
    (R"cotangent", R"$$\cot \frac \theta 2 = \frac {1 + \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 - \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 + \cos \theta} {1 - \cos \theta} } = \csc \theta + \cot \theta$$"),
  ),
)
```

<!--pytextgen generate section="d7f1"--><!-- The following content is generated at 2024-07-10T23:43:06.900914+08:00. Any edits will be overridden! -->

> 1. sine: $$\sin \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac {1 - \cos \theta} 2}$$
> 2. cosine: $$\cos \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac {1 + \cos \theta} 2}$$
> 3. tangent: $$\tan \frac \theta 2 = \frac {1 - \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 + \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 - \cos \theta} {1 + \cos \theta} } = \csc \theta - \cot \theta = \frac {\tan \theta} {1 + \sec \theta} = \frac {-1 + \operatorname{sgn}(\cos \theta)\sqrt{1 + \tan^2 \theta} } {\tan \theta}$$
> 4. secant: $$\sec \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac 2 {1 + \cos \theta} }$$
> 5. cosecant: $$\csc \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac 2 {1 - \cos \theta} }$$
> 6. cotangent: $$\cot \frac \theta 2 = \frac {1 + \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 - \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 + \cos \theta} {1 - \cos \theta} } = \csc \theta + \cot \theta$$

<!--/pytextgen-->

<!--pytextgen generate section="3759"--><!-- The following content is generated at 2024-07-10T23:43:06.932525+08:00. Any edits will be overridden! -->

- sine::$$\sin \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac {1 - \cos \theta} 2}$$ <!--SR:!2024-07-24,10,316-->
- cosine::$$\cos \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac {1 + \cos \theta} 2}$$ <!--SR:!2024-07-25,10,316-->
- tangent::$$\tan \frac \theta 2 = \frac {1 - \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 + \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 - \cos \theta} {1 + \cos \theta} } = \csc \theta - \cot \theta = \frac {\tan \theta} {1 + \sec \theta} = \frac {-1 + \operatorname{sgn}(\cos \theta)\sqrt{1 + \tan^2 \theta} } {\tan \theta}$$ <!--SR:!2024-07-24,8,256-->
- secant::$$\sec \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac 2 {1 + \cos \theta} }$$ <!--SR:!2024-07-20,7,296-->
- cosecant::$$\csc \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac 2 {1 - \cos \theta} }$$ <!--SR:!2024-07-22,8,296-->
- cotangent::$$\cot \frac \theta 2 = \frac {1 + \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 - \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 + \cos \theta} {1 - \cos \theta} } = \csc \theta + \cot \theta$$ <!--SR:!2024-07-20,6,276-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 4.2$ ::: $\operatorname{sgn}(\sin 4.2) \sqrt{\frac {1 - \cos 8.4} 2}$ <!--SR:!2024-07-20,7,296!2024-07-30,16,336-->
> - $\cos (-3.6)$ ::: $\operatorname{sgn}(\cos 3.6) \sqrt{\frac {1 + \cos 7.2} 2}$ <!--SR:!2024-07-25,11,316!2024-08-01,18,336-->
> - $\tan (-3.14)$ (sine and cosine) ::: $\frac {\cos 6.28 - 1} {\sin 6.28} = -\frac {\sin 6.28} {1 + \cos 6.28}$ <!--SR:!2024-07-22,8,296!2024-07-22,8,296-->
> - $\tan 3.42$ (cosine) ::: $\operatorname{sgn}(\sin 6.82) \sqrt{\frac {1 - \cos 6.82} {1 + \cos 6.82} }$ <!--SR:!2024-07-22,8,296!2024-07-21,7,276-->
> - $\tan (-2.01)$ (addition) ::: $-\csc 4.02 + \cot 4.02$ <!--SR:!2024-07-24,11,316!2024-07-26,12,316-->
> - $\tan (-9.6)$ (tangent and secant) ::: $-\frac {\tan 19.2} {1 + \sec 19.2}$ <!--SR:!2024-07-22,8,296!2024-07-25,11,316-->
> - $\tan (-4.96)$ (tangent) ::: $\frac {1 - \operatorname{sgn}(\cos 9.92) \sqrt{1 + \tan^2 9.92} } {\tan 9.92}$ <!--SR:!2024-07-22,8,296!2024-07-22,8,296-->
> - $\sec (-7.24)$ ::: $\operatorname{sgn}(\cos 7.24) \sqrt{\frac 2 {1 + \cos 14.48} }$ <!--SR:!2024-07-24,10,316!2024-07-29,15,336-->
> - $\csc (-1.7)$ ::: $-\operatorname{sgn}(\sin 1.7) \sqrt{\frac 2 {1 - \cos 3.4} }$ <!--SR:!2024-07-24,10,316!2024-07-26,12,316-->
> - $\cot 3.14$ (sine and cosine) ::: $\frac {1 + \cos 6.28} {\sin 6.28} = \frac {\sin 6.28} {1 - \cos 6.28}$ <!--SR:!2024-07-28,14,296!2024-07-23,10,316-->
> - $\cot (-69)$ (cosine) ::: $-\operatorname{sgn}(\sin 138) \sqrt{\frac {1 + \cos 138} {1 - \cos 138} }$ <!--SR:!2024-07-21,7,296!2024-07-31,17,336-->
> - $\cot 17$ (addition) ::: $\csc 34 + \cot 34$ <!--SR:!2024-07-26,12,316!2024-08-02,19,336-->

## product-to-sum and sum-to-product

### product-to-sum

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('dd91', '3213', None),
  items_to_map(
    (R'sine cosine', R'$$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$$'),
    (R'cosine sine', R'$$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$$'),
    (R'sine sine', R'$$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$$'),
    (R'cosine cosine', R'$$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$$'),
  ),
)
```

<!--pytextgen generate section="dd91"--><!-- The following content is generated at 2024-07-10T23:14:22.164185+08:00. Any edits will be overridden! -->

> 1. sine cosine: $$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$$
> 2. cosine sine: $$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$$
> 3. sine sine: $$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$$
> 4. cosine cosine: $$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$$

<!--/pytextgen-->

<!--pytextgen generate section="3213"--><!-- The following content is generated at 2024-07-10T23:14:22.138589+08:00. Any edits will be overridden! -->

- sine cosine::$$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$$ <!--SR:!2025-02-27,235,190-->
- cosine sine::$$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$$ <!--SR:!2025-03-06,240,190-->
- sine sine::$$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$$ <!--SR:!2024-09-10,231,210-->
- cosine cosine::$$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$$ <!--SR:!2024-10-24,342,250-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 5.23 \cos 1.23$ ::: $\frac{\sin 6.46 + \sin 4}2$ <!--SR:!2025-06-29,380,307!2025-04-16,318,287-->
> - $\cos(-3.21) \sin 0.23$ ::: $\frac{\sin 3.44 - \sin 2.98}2$ <!--SR:!2024-08-22,173,307!2024-10-04,98,207-->
> - $\sin 6.22 \sin(-0.01)$ ::: $\frac{\cos 6.23 - \cos 6.21}2$ <!--SR:!2025-03-09,306,307!2024-07-30,124,227-->
> - $\cos(-7.23) \cos(-1.23)$ ::: $\frac{\cos 6 + \cos 8.46}2$ <!--SR:!2024-08-11,92,267!2024-08-25,168,287-->

### sum-to-product

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('96fb', '39cd', None),
  items_to_map(
    (R'sine ± sine', R'$$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$$'),
    (R'cosine + cosine', R'$$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$$'),
    (R'cosine - cosine', R'$$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$$'),
    (R'tangent ± tangent', R'$$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$$'),
  ),
)
```

<!--pytextgen generate section="96fb"--><!-- The following content is generated at 2024-07-10T23:14:22.188212+08:00. Any edits will be overridden! -->

> 1. sine ± sine: $$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$$
> 2. cosine + cosine: $$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$$
> 3. cosine - cosine: $$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$$
> 4. tangent ± tangent: $$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$$

<!--/pytextgen-->

<!--pytextgen generate section="39cd"--><!-- The following content is generated at 2024-07-10T23:14:22.210248+08:00. Any edits will be overridden! -->

- sine ± sine::$$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$$ <!--SR:!2024-11-03,359,250-->
- cosine + cosine::$$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$$ <!--SR:!2025-08-21,448,230-->
- cosine - cosine::$$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$$ <!--SR:!2024-12-18,254,190-->
- tangent ± tangent::$$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$$ <!--SR:!2024-08-17,134,150-->

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 3.23 \mp \sin(-1.52)$ ::: $2 \sin\left(\frac{3.23 \pm 1.52}2\right) \cos\left(\frac{3.23 \mp 1.52}2\right)$ <!--SR:!2024-10-23,115,227!2024-11-18,210,267-->
> - $\cos(-2.23) + \cos 0.14$ ::: $2 \cos 1.045 \cos 1.185$ <!--SR:!2024-07-25,165,327!2024-08-07,146,267-->
> - $\cos(-6.88) - \cos(-2.45)$ ::: $-2 \sin 4.665 \sin 2.215$ <!--SR:!2024-08-14,167,307!2024-09-11,167,267-->
> - $\tan(-0.73) \mp \tan 2.55$ ::: $\frac{\sin(-0.73 \mp 2.55)}{\cos 0.73 \cos 2.55}$ <!--SR:!2025-05-12,346,307!2024-08-25,174,287-->

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
> - $-9.29 \cos(-2x) - 9.11 \sin(-2x)$ ([atan2](atan2.md) variant) ::: $\sqrt{9.29^2 + 9.11^2} \cos(2x - \operatorname{atan2}(9.11, -9.29))$ <!--SR:!2024-09-27,120,269!2024-09-04,86,229-->
> - $0 \cos 5x - 1.23 \sin 5x$ ::: $1.23 \sin(-5x)$ <!--SR:!2024-10-17,213,329!2024-12-02,249,329-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/list_of_trigonometric_identities) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
