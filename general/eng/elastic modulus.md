---
aliases:
  - elastic modulus
tags:
  - flashcard/active/general/eng/elastic_modulus
  - language/in/English
---

# elastic modulus

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

An __elastic modulus__ (also known as {@{__modulus of elasticity__}@}) is {@{a measure of an object's resistance to being deformed elastically when [stress](stress%20(mechanics).md) is applied}@}.

## definition

An elastic modulus has the form: {@{$$\delta \overset {\text{def} } = \frac {\text{stress} } {\text{strain} }$$}@}.

## types of elastic modulus

```Python
# pytextgen generate data
from asyncio import gather
from pytextgen.util import Result

items = R"""
_[Young's modulus](Young's%20modulus.md)_ ($E$)
_[bulk modulus](bulk%20modulus.md)_ ($K$)
_[flexural modulus](flexural%20modulus.md)_ ($E_{\text{flex} }$)
_[shear modulus](shear%20modulus.md)_ or _modulus of rigidity_ ($G$, $S$, or $\mu$)
""".strip().splitlines()
return (
  Result(
    location=__env__.cwf_sect("28ba"),
    text=str(len(items)),
  ),
  *await memorize_seq(
    __env__.cwf_sects("98ba", "cc19"),
    items,
  ),
)
```

There are many types of elastic moduli that can be defined. The {@{<!--pytextgen generate section="28ba"--><!-- The following content is generated at 2024-05-14T01:02:39.496907+08:00. Any edits will be overridden! -->4<!--/pytextgen-->}@} primary ones are:

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-13T21:24:01.864042+08:00. Any edits will be overridden! -->

> 1. _[Young's modulus](Young's%20modulus.md)_ ($E$)
> 2. _[bulk modulus](bulk%20modulus.md)_ ($K$)
> 3. _[flexural modulus](flexural%20modulus.md)_ ($E_{\text{flex} }$)
> 4. _[shear modulus](shear%20modulus.md)_ or _modulus of rigidity_ ($G$, $S$, or $\mu$)

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-13T21:24:01.873248+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←_[Young's modulus](Young's%20modulus.md)_ ($E$)
- _[Young's modulus](Young's%20modulus.md)_ ($E$)→::@::←_[bulk modulus](bulk%20modulus.md)_ ($K$)
- _[bulk modulus](bulk%20modulus.md)_ ($K$)→::@::←_[flexural modulus](flexural%20modulus.md)_ ($E_{\text{flex} }$)
- _[flexural modulus](flexural%20modulus.md)_ ($E_{\text{flex} }$)→::@::←_[shear modulus](shear%20modulus.md)_ or _modulus of rigidity_ ($G$, $S$, or $\mu$)
- _[shear modulus](shear%20modulus.md)_ or _modulus of rigidity_ ($G$, $S$, or $\mu$)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/elastic_modulus) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
