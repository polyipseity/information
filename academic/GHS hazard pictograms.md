#flashcards/academic/GHS_hazard_pictograms #academic/chemistry

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# GHS hazard pictograms

## pictograms

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
	(e.cwf_section('b9a823'), e.cwf_section('dee23a'),),
	('name & pictogram', 'description',),
	(
		('GHS01: [explosive](explosive.md)', '![{}](../attachments/GHS-pictogram-explos.svg)', '',),
		('GHS02: [flammable](flammability.md)', '![{}](../attachments/GHS-pictogram-flamme.svg)', '',),
		('GHS03: [oxidizing](oxidizing%20agent.md)', '![{}](../attachments/GHS-pictogram-rondflam.svg)', '',),
		('GHS04: [compressed gas](compressed%20fluid.md)', '![{}](../attachments/GHS-pictogram-bottle.svg)', '',),
		('GHS05: [corrosive](corrosive%20substance.md)', '![{}](../attachments/GHS-pictogram-acid.svg)', '',),
		('GHS06: [toxic](toxicity.md)', '![{}](../attachments/GHS-pictogram-skull.svg)', '',),
		('GHS07: harmful', '![{}](../attachments/GHS-pictogram-exclam.svg)', '',),
		('GHS08: [health hazard](health%20hazard.md)', '![{}](../attachments/GHS-pictogram-silhouette.svg)', '',),
		('GHS09: [environmental hazard](environmental%20hazard.md)', '![{}](../attachments/GHS-pictogram-pollu.svg)', '',),
	),
	lambda datum: (
		f'{cloze(datum[0])}<br/>{cloze(datum[1].format(datum[0]))}',
		cloze(datum[2]),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b9a823"--><!-- The following content is generated at 2023-03-14T16:08:57.065471+08:00. Any edits will be overridden! -->

> name & pictogram | description
> -|-
> {{GHS01: [explosive](explosive.md)}}<br/>{{![GHS01: [explosive](explosive.md)](../attachments/GHS-pictogram-explos.svg)}} |
> {{GHS02: [flammable](flammability.md)}}<br/>{{![GHS02: [flammable](flammability.md)](../attachments/GHS-pictogram-flamme.svg)}} |
> {{GHS03: [oxidizing](oxidizing%20agent.md)}}<br/>{{![GHS03: [oxidizing](oxidizing%20agent.md)](../attachments/GHS-pictogram-rondflam.svg)}} |
> {{GHS04: [compressed gas](compressed%20fluid.md)}}<br/>{{![GHS04: [compressed gas](compressed%20fluid.md)](../attachments/GHS-pictogram-bottle.svg)}} |
> {{GHS05: [corrosive](corrosive%20substance.md)}}<br/>{{![GHS05: [corrosive](corrosive%20substance.md)](../attachments/GHS-pictogram-acid.svg)}} |
> {{GHS06: [toxic](toxicity.md)}}<br/>{{![GHS06: [toxic](toxicity.md)](../attachments/GHS-pictogram-skull.svg)}} |
> {{GHS07: harmful}}<br/>{{![GHS07: harmful](../attachments/GHS-pictogram-exclam.svg)}} |
> {{GHS08: [health hazard](health%20hazard.md)}}<br/>{{![GHS08: [health hazard](health%20hazard.md)](../attachments/GHS-pictogram-silhouette.svg)}} |
> {{GHS09: [environmental hazard](environmental%20hazard.md)}}<br/>{{![GHS09: [environmental hazard](environmental%20hazard.md)](../attachments/GHS-pictogram-pollu.svg)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dee23a"--><!-- The following content is generated at 2023-03-15T19:16:17.252430+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←GHS01: [explosive](explosive.md)
2. GHS01: [explosive](explosive.md)→:::←GHS02: [flammable](flammability.md)
3. GHS02: [flammable](flammability.md)→:::←GHS03: [oxidizing](oxidizing%20agent.md)
4. GHS03: [oxidizing](oxidizing%20agent.md)→:::←GHS04: [compressed gas](compressed%20fluid.md)
5. GHS04: [compressed gas](compressed%20fluid.md)→:::←GHS05: [corrosive](corrosive%20substance.md)
6. GHS05: [corrosive](corrosive%20substance.md)→:::←GHS06: [toxic](toxicity.md)
7. GHS06: [toxic](toxicity.md)→:::←GHS07: harmful
8. GHS07: harmful→:::←GHS08: [health hazard](health%20hazard.md)
9. GHS08: [health hazard](health%20hazard.md)→:::←GHS09: [environmental hazard](environmental%20hazard.md)
10. GHS09: [environmental hazard](environmental%20hazard.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
