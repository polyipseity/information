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
> | {@{GHS09: [environmental hazard](environmental%20hazard.md)}@}<br/>{@{![GHS09: [environmental hazard](environmental%20hazard.md)](../../archives/Wikimedia%20Commons/GHS-pictogram-pollu.svg)}@} |  | <!--SR:!2027-10-22,1295,350!2025-11-27,741,330!2026-05-19,870,330!2027-04-03,1052,330!2027-07-14,1218,350!2026-07-21,921,330!2027-01-05,988,330!2027-07-03,1209,350!2028-05-13,1455,350!2025-08-08,600,310!2027-01-10,992,330!2026-06-28,891,330!2032-03-05,2441,330!2025-11-30,737,330!2027-07-21,1223,350!2025-07-26,620,310!2027-10-16,1290,350!2026-03-03,781,310-->

<!--/pytextgen-->

<!--pytextgen generate section="dee23a"--><!-- The following content is generated at 2024-01-04T20:17:51.744625+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←GHS01: [explosive](explosive.md) <!--SR:!2027-07-09,1214,350!2027-12-17,1341,350-->
- GHS01: [explosive](explosive.md)→::@::←GHS02: [flammable](flammability.md) <!--SR:!2029-05-26,1516,270!2027-08-02,1232,350-->
- GHS02: [flammable](flammability.md)→::@::←GHS03: [oxidizing](oxidizing%20agent.md) <!--SR:!2026-08-22,890,330!2026-04-22,801,330-->
- GHS03: [oxidizing](oxidizing%20agent.md)→::@::←GHS04: [compressed gas](compressed%20fluid.md) <!--SR:!2027-04-04,805,250!2028-01-01,1173,290-->
- GHS04: [compressed gas](compressed%20fluid.md)→::@::←GHS05: [corrosive](corrosive%20substance.md) <!--SR:!2029-02-28,1357,270!2029-02-13,1369,310-->
- GHS05: [corrosive](corrosive%20substance.md)→::@::←GHS06: [toxic](toxicity.md) <!--SR:!2030-10-14,1921,310!2027-12-23,1164,290-->
- GHS06: [toxic](toxicity.md)→::@::←GHS07: harmful <!--SR:!2025-10-30,662,310!2027-04-26,959,290-->
- GHS07: harmful→::@::←GHS08: [health hazard](health%20hazard.md) <!--SR:!2025-10-20,641,310!2027-09-08,1149,290-->
- GHS08: [health hazard](health%20hazard.md)→::@::←GHS09: [environmental hazard](environmental%20hazard.md) <!--SR:!2026-12-10,969,330!2025-10-21,656,310-->
- GHS09: [environmental hazard](environmental%20hazard.md)→::@::←_(end)_ <!--SR:!2028-03-08,1402,350!2028-01-13,1361,350-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/GHS_hazard_pictograms) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
