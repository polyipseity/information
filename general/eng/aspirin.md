---
aliases:
  - 2-acetoxybenzoic acid
  - ASA
  - acetylsaylicylic acid
  - aspirin
tags:
  - flashcard/active/general/eng/aspirin
  - language/in/English
---

# aspirin

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

> {@{![skeletal formula of aspirin](../../archives/Wikimedia%20Commons/Aspirin-skeletal.svg)}@}
>
> {@{[skeletal formula](skeletal%20formula.md) of aspirin}@}

## medical use

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('332a', '45af'),
  ('name', 'description',),
  (
    ('[analgesic](analgesic.md)', '',),
    ('[anti-inflammation](anti-inflammatory.md)', 'It can treat [arthritis](arthritis.md).',),
    ('prevention of [heart attack](myocardial%20infarction.md)', 'It has [blood thinning](anticoagulant.md) and [antiplatelet](antiplatelet%20drug.md) effect.',),
    ('relieve [fever](fever.md)', '',),
  ),
  lambda datum: map(cloze, datum),
)
```

<!--pytextgen generate section="332a"--><!-- The following content is generated at 2026-01-25T23:32:18.042781+08:00. Any edits will be overridden! -->

> | name                                                           | description                                                                                        |
> | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
> | {@{[analgesic](analgesic.md)}@}                                |                                                                                                    |
> | {@{[anti-inflammation](anti-inflammatory.md)}@}                | {@{It can treat [arthritis](arthritis.md).}@}                                                      |
> | {@{prevention of [heart attack](myocardial%20infarction.md)}@} | {@{It has [blood thinning](anticoagulant.md) and [antiplatelet](antiplatelet%20drug.md) effect.}@} |
> | {@{relieve [fever](fever.md)}@}                                |                                                                                                    |

<!--/pytextgen-->

<!--pytextgen generate section="45af"--><!-- The following content is generated at 2024-01-04T20:17:51.291378+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[analgesic](analgesic.md)
- [analgesic](analgesic.md)→::@::←[anti-inflammation](anti-inflammatory.md)
- [anti-inflammation](anti-inflammatory.md)→::@::←prevention of [heart attack](myocardial%20infarction.md)
- prevention of [heart attack](myocardial%20infarction.md)→::@::←relieve [fever](fever.md)
- relieve [fever](fever.md)→::@::←_(end)_

<!--/pytextgen-->

### side effects

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('11af', '78ae'),
  ('name', 'description',),
  (
    ('increased bleeding risk', '',),
    ('[stomach ulcer](peptic%20ulcer%20disease.md)', '',),
    ('[stomach upset](abdominal%20pain.md)', '',),
  ),
  lambda datum: map(cloze, datum),
)
```

<!--pytextgen generate section="11af"--><!-- The following content is generated at 2026-01-25T23:32:18.059210+08:00. Any edits will be overridden! -->

> | name                                               | description |
> | -------------------------------------------------- | ----------- |
> | {@{increased bleeding risk}@}                      |             |
> | {@{[stomach ulcer](peptic%20ulcer%20disease.md)}@} |             |
> | {@{[stomach upset](abdominal%20pain.md)}@}         |             |

<!--/pytextgen-->

<!--pytextgen generate section="78ae"--><!-- The following content is generated at 2024-01-04T20:17:51.327355+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←increased bleeding risk
- increased bleeding risk→::@::←[stomach ulcer](peptic%20ulcer%20disease.md)
- [stomach ulcer](peptic%20ulcer%20disease.md)→::@::←[stomach upset](abdominal%20pain.md)
- [stomach upset](abdominal%20pain.md)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/aspirin) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
