---
aliases:
  - list of trigonometric identities
  - trigonometric identities
tags:
  - flashcard/active/general/eng/list_of_trigonometric_identities
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

<!--pytextgen generate section="4949"--><!-- The following content is generated at 2026-01-25T23:32:18.858846+08:00. Any edits will be overridden! -->

> | name                                                                        |
> | --------------------------------------------------------------------------- |
> | [Pythagorean identities](#Pythagorean%20identities)                         |
> | [angle sum and difference](#angle%20sum%20and%20difference)                 |
> | [linear combination](#linear%20combination)                                 |
> | [multiple-angle](#multiple-angle)                                           |
> | [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product) |

<!--/pytextgen-->

<!--pytextgen generate section="d996"--><!-- The following content is generated at 2024-07-11T08:29:28.983272+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[Pythagorean identities](#Pythagorean%20identities)
- [Pythagorean identities](#Pythagorean%20identities)→::@::←[angle sum and difference](#angle%20sum%20and%20difference)
- [angle sum and difference](#angle%20sum%20and%20difference)→::@::←[linear combination](#linear%20combination)
- [linear combination](#linear%20combination)→::@::←[multiple-angle](#multiple-angle)
- [multiple-angle](#multiple-angle)→::@::←[product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)
- [product-to-sum and sum-to-product](#product-to-sum%20and%20sum-to-product)→::@::←_(end)_

<!--/pytextgen-->

## Pythagorean identities

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("958f", "ba01", None),
  items_to_map(
    (R"normal", R"$$\sin^2 \theta + \cos^2 \theta = 1$$"),
    (R"divided by sine", R"$$1 + \cot^2 \theta = \csc^2 \theta$$"),
    (R"divided by cosine", R"$$1 + \tan^2 \theta = \sec^2 \theta$$"),
    (R"divided by sine and cosine", R"$$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$$"),
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

- normal:@:$$\sin^2 \theta + \cos^2 \theta = 1$$
- divided by sine:@:$$1 + \cot^2 \theta = \csc^2 \theta$$
- divided by cosine:@:$$1 + \tan^2 \theta = \sec^2 \theta$$
- divided by sine and cosine:@:$$\sec^2 \theta + \csc^2 \theta = \sec^2 \theta \csc^2 \theta$$

<!--/pytextgen-->

> [!example] examples
>
> - $\cos^2 6.52 + \sin^2 6.52$ ::@:: $1$
> - $\cot^2 (-3.52) + 1$ ::@:: $\csc^2 (-3.52)$
> - $1 + \tan^2 (-7.23)$ ::@:: $\sec^2 (-7.23)$
> - $\csc^2 0.23 + \sec^2 0.23$ ::@:: $\sec^2 0.23 \csc^2 0.23$

## angle sum and difference

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("f823", "394a", None),
  items_to_map(
    (R"sine", R"$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$"),
    (R"cosine", R"$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$"),
    (R"tangent", R"$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$"),
  ),
)
```

<!--pytextgen generate section="f823"--><!-- The following content is generated at 2024-07-10T23:14:21.957811+08:00. Any edits will be overridden! -->

> 1. sine: $$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$
> 2. cosine: $$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$
> 3. tangent: $$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$

<!--/pytextgen-->

<!--pytextgen generate section="394a"--><!-- The following content is generated at 2024-07-10T23:14:21.914301+08:00. Any edits will be overridden! -->

- sine:@:$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$
- cosine:@:$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$
- tangent:@:$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$

<!--/pytextgen-->

> [!example] examples
>
> - $\sin(1.73 \mp 2.45)$ ::@:: $\sin 1.73 \cos 2.45 \mp \sin 2.45 \cos 1.73$
> - $\cos(-0.56 \pm 9.23)$ ::@:: $\cos(-0.56) \cos 9.23 \mp \sin(-0.56) \sin 9.23$
> - $\tan(7.22 \mp 2.38)$ ::@:: $\frac{\tan 7.22 \mp \tan 2.38}{1 \pm \tan 2.38 \tan 7.22}$

## multiple-angle

### double-angle

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("b023", "ab2d", None),
  items_to_map(
    (R"sine", R"$$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$"),
    (R"cosine", R"$$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$"),
    (R"tangent", R"$$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$"),
  ),
)
```

<!--pytextgen generate section="b023"--><!-- The following content is generated at 2024-07-10T23:14:22.063540+08:00. Any edits will be overridden! -->

> 1. sine: $$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$
> 2. cosine: $$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$
> 3. tangent: $$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$

<!--/pytextgen-->

<!--pytextgen generate section="ab2d"--><!-- The following content is generated at 2024-07-10T23:14:22.112551+08:00. Any edits will be overridden! -->

- sine:@:$$\sin(2\theta)=2\sin\theta\cos\theta=(\sin\theta+\cos\theta)^2-1=\frac{2\tan\theta}{1+\tan^2\theta}$$
- cosine:@:$$\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$$
- tangent:@:$$\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}$$

<!--/pytextgen-->

> [!tip] tips
>
> - [mnemonic](mnemonic.md) ::@:: use [§ angle sum and difference](#angle%20sum%20and%20difference) to help with memorization

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $\sin 7.42$ ([angle sum](#angle%20sum%20and%20difference) variant) ::@:: $2 \cos 3.71 \sin 3.71$
> - $\sin(-0.36)$ (square variant) ::@:: $(\cos 0.18 - \sin 0.18)^2 - 1$
> - $\sin 6.24$ (tangent variant) ::@:: $\frac{2 \tan 3.12}{1 + \tan^2 3.12}$
> - $\cos(-3.68)$ ([angle sum](#angle%20sum%20and%20difference) variant) ::@:: $\cos^2 1.84 - \sin^2 1.84$
> - $\cos 9.98$ (cosine variant) ::@:: $2\cos^2 4.99 - 1$
> - $\cos 5.54$ (sine variant) ::@:: $1 - 2\sin^2 2.77$
> - $\cos(-9.22)$ (tangent variant) ::@:: $\frac{1 - \tan^2 4.61}{1 + \tan^2 4.61}$
> - $\tan 0.04$ ::@:: $\frac{2 \tan 0.02}{1 - \tan^2 0.02}$

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

- sine:@:$$\sin \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac {1 - \cos \theta} 2}$$
- cosine:@:$$\cos \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac {1 + \cos \theta} 2}$$
- tangent:@:$$\tan \frac \theta 2 = \frac {1 - \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 + \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 - \cos \theta} {1 + \cos \theta} } = \csc \theta - \cot \theta = \frac {\tan \theta} {1 + \sec \theta} = \frac {-1 + \operatorname{sgn}(\cos \theta)\sqrt{1 + \tan^2 \theta} } {\tan \theta}$$
- secant:@:$$\sec \frac \theta 2 = \operatorname{sgn}\left(\cos \frac \theta 2\right) \sqrt{\frac 2 {1 + \cos \theta} }$$
- cosecant:@:$$\csc \frac \theta 2 = \operatorname{sgn}\left(\sin \frac \theta 2\right) \sqrt{\frac 2 {1 - \cos \theta} }$$
- cotangent:@:$$\cot \frac \theta 2 = \frac {1 + \cos \theta} {\sin \theta} = \frac {\sin \theta} {1 - \cos \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac {1 + \cos \theta} {1 - \cos \theta} } = \csc \theta + \cot \theta$$

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 4.2$ ::@:: $\operatorname{sgn}(\sin 4.2) \sqrt{\frac {1 - \cos 8.4} 2}$
> - $\cos (-3.6)$ ::@:: $\operatorname{sgn}(\cos 3.6) \sqrt{\frac {1 + \cos 7.2} 2}$
> - $\tan (-3.14)$ (sine and cosine) ::@:: $\frac {\cos 6.28 - 1} {\sin 6.28} = -\frac {\sin 6.28} {1 + \cos 6.28}$
> - $\tan 3.42$ (cosine) ::@:: $\operatorname{sgn}(\sin 6.82) \sqrt{\frac {1 - \cos 6.82} {1 + \cos 6.82} }$
> - $\tan (-2.01)$ (addition) ::@:: $-\csc 4.02 + \cot 4.02$
> - $\tan (-9.6)$ (tangent and secant) ::@:: $-\frac {\tan 19.2} {1 + \sec 19.2}$
> - $\tan (-4.96)$ (tangent) ::@:: $\frac {1 - \operatorname{sgn}(\cos 9.92) \sqrt{1 + \tan^2 9.92} } {\tan 9.92}$
> - $\sec (-7.24)$ ::@:: $\operatorname{sgn}(\cos 7.24) \sqrt{\frac 2 {1 + \cos 14.48} }$
> - $\csc (-1.7)$ ::@:: $-\operatorname{sgn}(\sin 1.7) \sqrt{\frac 2 {1 - \cos 3.4} }$
> - $\cot 3.14$ (sine and cosine) ::@:: $\frac {1 + \cos 6.28} {\sin 6.28} = \frac {\sin 6.28} {1 - \cos 6.28}$
> - $\cot (-69)$ (cosine) ::@:: $-\operatorname{sgn}(\sin 138) \sqrt{\frac {1 + \cos 138} {1 - \cos 138} }$
> - $\cot 17$ (addition) ::@:: $\csc 34 + \cot 34$

## product-to-sum and sum-to-product

### product-to-sum

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("dd91", "3213", None),
  items_to_map(
    (R"sine cosine", R"$$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$$"),
    (R"cosine sine", R"$$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$$"),
    (R"sine sine", R"$$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$$"),
    (R"cosine cosine", R"$$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$$"),
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

- sine cosine:@:$$\sin\theta\cos\varphi=\frac{\sin(\theta+\varphi)+\sin(\theta-\varphi)}2$$
- cosine sine:@:$$\cos\theta\sin\varphi=\frac{\sin(\theta+\varphi)-\sin(\theta-\varphi)}2$$
- sine sine:@:$$\sin\theta\sin\varphi=\frac{\cos(\theta-\varphi)-\cos(\theta+\varphi)}2$$
- cosine cosine:@:$$\cos\theta\cos\varphi=\frac{\cos(\theta-\varphi)+\cos(\theta+\varphi)}2$$

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 5.23 \cos 1.23$ ::@:: $\frac{\sin 6.46 + \sin 4}2$
> - $\cos(-3.21) \sin 0.23$ ::@:: $\frac{\sin 3.44 - \sin 2.98}2$
> - $\sin 6.22 \sin(-0.01)$ ::@:: $\frac{\cos 6.23 - \cos 6.21}2$
> - $\cos(-7.23) \cos(-1.23)$ ::@:: $\frac{\cos 6 + \cos 8.46}2$

### sum-to-product

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects("96fb", "39cd", None),
  items_to_map(
    (R"sine ± sine", R"$$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$$"),
    (R"cosine + cosine", R"$$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$$"),
    (R"cosine - cosine", R"$$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$$"),
    (R"tangent ± tangent", R"$$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$$"),
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

- sine ± sine:@:$$\sin\theta\pm\sin\varphi=2\sin\left(\frac{\theta\pm\varphi}2\right)\cos\left(\frac{\theta\mp\varphi}2\right)$$
- cosine + cosine:@:$$\cos\theta+\cos\varphi=2\cos\left(\frac{\theta+\varphi}2\right)\cos\left(\frac{\theta-\varphi}2\right)$$
- cosine - cosine:@:$$\cos\theta-\cos\varphi=-2\sin\left(\frac{\theta+\varphi}2\right)\sin\left(\frac{\theta-\varphi}2\right)$$
- tangent ± tangent:@:$$\tan\theta\pm\tan\varphi=\frac{\sin(\theta\pm\varphi)}{\cos\theta\cos\varphi}$$

<!--/pytextgen-->

> [!example] examples
>
> - $\sin 3.23 \mp \sin(-1.52)$ ::@:: $2 \sin\left(\frac{3.23 \pm 1.52}2\right) \cos\left(\frac{3.23 \mp 1.52}2\right)$
> - $\cos(-2.23) + \cos 0.14$ ::@:: $2 \cos 1.045 \cos 1.185$
> - $\cos(-6.88) - \cos(-2.45)$ ::@:: $-2 \sin 4.665 \sin 2.215$
> - $\tan(-0.73) \mp \tan 2.55$ ::@:: $\frac{\sin(-0.73 \mp 2.55)}{\cos 0.73 \cos 2.55}$

## linear combination

### sine and cosine

> __linear combination of sine and cosine__
>
> - conditions: {@{$(a, b) \ne (0, 0)$}@}
>
> {@{$$a \cos x + b \sin x = c \cos(x + \varphi)$$}@}
>
> where
>
> - {@{$c = \operatorname{sgn}(a) \sqrt{a^2 + b^2}, \varphi = \arctan(-b / a)$ or $c = \sqrt{a^2 + b^2}, \varphi = \operatorname{atan2}(-b, a)$}@}, assuming {@{$\arctan(\pm \infty) = \pm \pi / 2$}@}

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $-2.64 \cos 3x + 3.22 \sin 3x$ (arctangent variant) ::@:: $-\sqrt{2.64^2 + 3.22^2} \cos(3x + \arctan(3.22 / 2.64))$
> - $-9.29 \cos(-2x) - 9.11 \sin(-2x)$ ([atan2](atan2.md) variant) ::@:: $\sqrt{9.29^2 + 9.11^2} \cos(2x - \operatorname{atan2}(9.11, -9.29))$
> - $0 \cos 5x - 1.23 \sin 5x$ (arctangent variant, [atan2](atan2.md) variant) ::@:: $1.23 \cos(5x + \pi / 2)$
> - $0 \cos 4.2x + 0 \sin 4.2x$ ::@:: $0$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/list_of_trigonometric_identities) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
