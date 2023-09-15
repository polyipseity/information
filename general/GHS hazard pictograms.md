---
tags:
  - flashcards/general/GHS_hazard_pictograms
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# GHS hazard pictograms

## pictograms

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
	e.cwf_sects('b9a823', 'dee23a'),
	('name & pictogram', 'description',),
	(
		('GHS01: [explosive](explosive.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-explos.svg)', '',),
		('GHS02: [flammable](flammability.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-flamme.svg)', '',),
		('GHS03: [oxidizing](oxidizing%20agent.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-rondflam.svg)', '',),
		('GHS04: [compressed gas](compressed%20fluid.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-bottle.svg)', '',),
		('GHS05: [corrosive](corrosive%20substance.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-acid.svg)', '',),
		('GHS06: [toxic](toxicity.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-skull.svg)', '',),
		('GHS07: harmful', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-exclam.svg)', '',),
		('GHS08: [health hazard](health%20hazard.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-silhouette.svg)', '',),
		('GHS09: [environmental hazard](environmental%20hazard.md)', '![{}](../archives/Wikimedia%20Commons/GHS-pictogram-pollu.svg)', '',),
	),
	lambda datum: (
		f'{cloze(datum[0])}<br/>{cloze(datum[1].format(datum[0]))}',
		cloze(datum[2]),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b9a823"--><!-- The following content is generated at 2023-03-20T16:20:30.844432+08:00. Any edits will be overridden! -->

> | name & pictogram | description |
> |-|-|
> | {{GHS01: [explosive](explosive.md)}}<br/>{{![GHS01: [explosive](explosive.md)](../archives/Wikimedia%20Commons/GHS-pictogram-explos.svg)}} |  |
> | {{GHS02: [flammable](flammability.md)}}<br/>{{![GHS02: [flammable](flammability.md)](../archives/Wikimedia%20Commons/GHS-pictogram-flamme.svg)}} |  |
> | {{GHS03: [oxidizing](oxidizing%20agent.md)}}<br/>{{![GHS03: [oxidizing](oxidizing%20agent.md)](../archives/Wikimedia%20Commons/GHS-pictogram-rondflam.svg)}} |  |
> | {{GHS04: [compressed gas](compressed%20fluid.md)}}<br/>{{![GHS04: [compressed gas](compressed%20fluid.md)](../archives/Wikimedia%20Commons/GHS-pictogram-bottle.svg)}} |  |
> | {{GHS05: [corrosive](corrosive%20substance.md)}}<br/>{{![GHS05: [corrosive](corrosive%20substance.md)](../archives/Wikimedia%20Commons/GHS-pictogram-acid.svg)}} |  |
> | {{GHS06: [toxic](toxicity.md)}}<br/>{{![GHS06: [toxic](toxicity.md)](../archives/Wikimedia%20Commons/GHS-pictogram-skull.svg)}} |  |
> | {{GHS07: harmful}}<br/>{{![GHS07: harmful](../archives/Wikimedia%20Commons/GHS-pictogram-exclam.svg)}} |  |
> | {{GHS08: [health hazard](health%20hazard.md)}}<br/>{{![GHS08: [health hazard](health%20hazard.md)](../archives/Wikimedia%20Commons/GHS-pictogram-silhouette.svg)}} |  |
> | {{GHS09: [environmental hazard](environmental%20hazard.md)}}<br/>{{![GHS09: [environmental hazard](environmental%20hazard.md)](../archives/Wikimedia%20Commons/GHS-pictogram-pollu.svg)}} |  | <!--SR:!2024-04-05,285,330!2023-11-17,173,310!2023-12-31,203,310!2024-05-16,319,330!2024-03-13,268,330!2024-01-12,215,310!2024-04-22,300,330!2024-03-11,266,330!2024-05-17,320,330!2023-12-17,194,310!2024-04-23,301,330!2024-01-19,208,310!2023-12-07,184,310!2023-11-18,172,310!2024-03-15,269,330!2023-11-14,154,290!2024-04-04,284,330!2024-01-12,194,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dee23a"--><!-- The following content is generated at 2023-03-15T19:16:17.252430+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←GHS01: [explosive](explosive.md) <!--SR:!2024-03-12,267,330!2024-04-15,295,330-->
2. GHS01: [explosive](explosive.md)→:::←GHS02: [flammable](flammability.md) <!--SR:!2024-01-22,174,250!2024-03-16,271,330-->
3. GHS02: [flammable](flammability.md)→:::←GHS03: [oxidizing](oxidizing%20agent.md) <!--SR:!2024-03-15,270,330!2024-02-11,243,330-->
4. GHS03: [oxidizing](oxidizing%20agent.md)→:::←GHS04: [compressed gas](compressed%20fluid.md) <!--SR:!2023-10-21,52,250!2024-10-14,403,290-->
5. GHS04: [compressed gas](compressed%20fluid.md)→:::←GHS05: [corrosive](corrosive%20substance.md) <!--SR:!2024-01-20,186,270!2024-02-12,238,310-->
6. GHS05: [corrosive](corrosive%20substance.md)→:::←GHS06: [toxic](toxicity.md) <!--SR:!2023-10-27,154,290!2024-10-13,402,290-->
7. GHS06: [toxic](toxicity.md)→:::←GHS07: harmful <!--SR:!2024-01-07,214,310!2023-10-14,88,270-->
8. GHS07: harmful→:::←GHS08: [health hazard](health%20hazard.md) <!--SR:!2024-01-18,207,310!2024-07-16,305,270-->
9. GHS08: [health hazard](health%20hazard.md)→:::←GHS09: [environmental hazard](environmental%20hazard.md) <!--SR:!2024-04-14,294,330!2024-01-04,212,310-->
10. GHS09: [environmental hazard](environmental%20hazard.md)→:::←_(end)_ <!--SR:!2024-05-05,308,330!2024-04-21,299,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
