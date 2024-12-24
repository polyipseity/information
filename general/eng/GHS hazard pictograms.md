---
tags:
  - flashcard/active/general/eng/GHS_hazard_pictograms
  - language/in/English
---

# GHS hazard pictograms

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## pictograms

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('b9a823', 'dee23a'),
  ('name & pictogram', 'description',),
  (
    ('GHS01: [explosive](explosive.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-explos.svg)', '',),
    ('GHS02: [flammable](flammability.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-flamme.svg)', '',),
    ('GHS03: [oxidizing](oxidizing%20agent.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-rondflam.svg)', '',),
    ('GHS04: [compressed gas](compressed%20fluid.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-bottle.svg)', '',),
    ('GHS05: [corrosive](corrosive%20substance.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-acid.svg)', '',),
    ('GHS06: [toxic](toxicity.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-skull.svg)', '',),
    ('GHS07: harmful', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-exclam.svg)', '',),
    ('GHS08: [health hazard](health%20hazard.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-silhouette.svg)', '',),
    ('GHS09: [environmental hazard](environmental%20hazard.md)', '![{}](../../archives/Wikimedia%20Commons/GHS-pictogram-pollu.svg)', '',),
  ),
  lambda datum: (
    f'{cloze(datum[0])}<br/>{cloze(datum[1].format(datum[0]))}',
    cloze(datum[2]),
  ),
)
```

<!--pytextgen generate section="b9a823"--><!-- The following content is generated at 2023-03-20T16:20:30.844432+08:00. Any edits will be overridden! -->

> | name & pictogram | description |
> |-|-|
> | {@{GHS01: [explosive](explosive.md)}@}<br/>{@{![GHS01: [explosive](explosive.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-explos.svg)}@} |  |
> | {@{GHS02: [flammable](flammability.md)}@}<br/>{@{![GHS02: [flammable](flammability.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-flamme.svg)}@} |  |
> | {@{GHS03: [oxidizing](oxidizing%20agent.md)}@}<br/>{@{![GHS03: [oxidizing](oxidizing%20agent.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-rondflam.svg)}@} |  |
> | {@{GHS04: [compressed gas](compressed%20fluid.md)}@}<br/>{@{![GHS04: [compressed gas](compressed%20fluid.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-bottle.svg)}@} |  |
> | {@{GHS05: [corrosive](corrosive%20substance.md)}@}<br/>{@{![GHS05: [corrosive](corrosive%20substance.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-acid.svg)}@} |  |
> | {@{GHS06: [toxic](toxicity.md)}@}<br/>{@{![GHS06: [toxic](toxicity.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-skull.svg)}@} |  |
> | {@{GHS07: harmful}@}<br/>{@{![GHS07: harmful](../../archives/Wikimedia%20Commons/GHS-pictogram-exclam.svg)}@} |  |
> | {@{GHS08: [health hazard](health%20hazard.md)}@}<br/>{@{![GHS08: [health hazard](health%20hazard.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-silhouette.svg)}@} |  |
> | {@{GHS09: [environmental hazard](environmental%20hazard.md)}@}<br/>{@{![GHS09: [environmental hazard](environmental%20hazard.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-pollu.svg)}@} |  |

<!--/pytextgen-->

<!--pytextgen generate section="dee23a"--><!-- The following content is generated at 2024-01-04T20:17:51.744625+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←GHS01: [explosive](explosive.md)
- GHS01: [explosive](explosive.md)→::@::←GHS02: [flammable](flammability.md)
- GHS02: [flammable](flammability.md)→::@::←GHS03: [oxidizing](oxidizing%20agent.md)
- GHS03: [oxidizing](oxidizing%20agent.md)→::@::←GHS04: [compressed gas](compressed%20fluid.md)
- GHS04: [compressed gas](compressed%20fluid.md)→::@::←GHS05: [corrosive](corrosive%20substance.md)
- GHS05: [corrosive](corrosive%20substance.md)→::@::←GHS06: [toxic](toxicity.md)
- GHS06: [toxic](toxicity.md)→::@::←GHS07: harmful
- GHS07: harmful→::@::←GHS08: [health hazard](health%20hazard.md)
- GHS08: [health hazard](health%20hazard.md)→::@::←GHS09: [environmental hazard](environmental%20hazard.md)
- GHS09: [environmental hazard](environmental%20hazard.md)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/GHS_hazard_pictograms) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
