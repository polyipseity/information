---
aliases: ['activity series',]
---

#flashcards/chemistry/reactivity_series #academic/chemistry

# reactivity series

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
import typing
data: typing.Mapping[str, typing.Mapping[str, str]] = {
	'potassium': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'water',
		'reaction with dilute HCl': 'explosive',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'explosive',
	},
	'sodium': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'water',
		'reaction with dilute HCl': 'explosive',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'explosive',
	},
	'calcium': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'water',
		'reaction with dilute HCl': 'moderate',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'moderate to none (covered by insoluble CaSO<sub>4</sub>)',
	},
	'magnesium': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'steam',
		'reaction with dilute HCl': 'moderate',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'moderate',
	},
	'aluminium': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'steam',
		'reaction with dilute HCl': 'moderate',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'moderate',
	},
	'zinc': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'steam',
		'reaction with dilute HCl': 'moderate',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'moderate',
	},
	'iron': {
		'reaction with air': 'burn',
		'reaction with H<sub>2</sub>O': 'steam',
		'reaction with dilute HCl': 'moderate',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'moderate',
	},
	'lead': {
		'reaction with air': 'heat',
		'reaction with H<sub>2</sub>O': 'none',
		'reaction with dilute HCl': 'slow',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'slow to none (covered by insoluble PbSO<sub>4</sub>)',
	},
	'copper': {
		'reaction with air': 'heat',
		'reaction with H<sub>2</sub>O': 'none',
		'reaction with dilute HCl': 'none',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'none',
	},
	'mercury': {
		'reaction with air': 'heat',
		'reaction with H<sub>2</sub>O': 'none',
		'reaction with dilute HCl': 'none',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'none',
	},
	'silver': {
		'reaction with air': 'none',
		'reaction with H<sub>2</sub>O': 'none',
		'reaction with dilute HCl': 'none',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'none',
	},
	'gold': {
		'reaction with air': 'none',
		'reaction with H<sub>2</sub>O': 'none',
		'reaction with dilute HCl': 'none',
		'reaction with dilute H<sub>2</sub>SO<sub>4</sub>': 'none',
	},
}
text: gen.TextCode = gen.common.maps_to_code(data)
series: gen.TextCode = gen.common.seq_to_code(data.keys(),
	index=1,
	prefix='{mem:_(most reactive)_}',
	suffix='{mem:_(least reactive)_}',)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('a2994d'),
		text=gen.common.cloze_text(text,
			states=read.read_flashcard_states(__env__.cwf_section('a2994d'))
		),
	),
	gen.Result(
		location=__env__.cwf_section('299018'),
		text=gen.common.memorize_linked_seq(series,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('299018')),
		),
	),
)
```
%%

Reactivity decreases down the table.

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a2994d"--><!-- The following content is generated at 2022-11-05T00:25:01.033869+08:00. Any edits will be overridden! -->

> potassium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{water}}
> - reaction with dilute HCl: {{explosive}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{explosive}} <!--SR:!2023-07-31,284,250!2023-02-27,189,250!2023-02-14,176,250!2023-07-14,267,250-->

> sodium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{water}}
> - reaction with dilute HCl: {{explosive}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{explosive}} <!--SR:!2023-07-12,265,250!2023-02-23,185,250!2023-07-17,270,250!2023-02-22,184,250-->

> calcium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{water}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate to none (covered by insoluble CaSO<sub>4</sub>)}} <!--SR:!2023-02-21,183,250!2023-02-13,175,250!2023-02-26,188,250!2023-02-18,180,250-->

> magnesium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}} <!--SR:!2023-02-20,182,250!2023-02-10,172,250!2023-07-29,282,250!2023-02-19,181,250-->

> aluminium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}} <!--SR:!2023-02-28,190,250!2023-02-24,186,250!2023-07-27,280,250!2023-02-17,179,250-->

> zinc
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}} <!--SR:!2023-02-03,12,170!2023-07-06,259,250!2023-07-12,265,250!2023-03-09,199,250-->

> iron
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}} <!--SR:!2023-03-08,198,250!2023-08-02,286,250!2023-02-24,186,250!2023-03-01,191,250-->

> lead
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{slow}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{slow to none (covered by insoluble PbSO<sub>4</sub>)}} <!--SR:!2023-08-02,286,250!2023-03-12,202,250!2023-02-20,66,190!2023-07-09,262,249-->

> copper
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}} <!--SR:!2023-08-01,285,249!2023-05-15,207,229!2023-07-13,266,249!2023-08-03,287,249-->

> mercury
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}} <!--SR:!2023-07-04,257,248!2023-07-23,276,248!2023-07-11,264,248!2023-08-06,289,248-->

> silver
> - reaction with air: {{none}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}} <!--SR:!2023-07-05,258,248!2023-07-25,278,248!2023-08-07,289,248!2023-07-21,274,248-->

> gold
> - reaction with air: {{none}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}} <!--SR:!2023-08-27,311,268!2023-07-11,264,246!2023-06-29,252,246!2023-07-30,283,246-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2022-11-09T18:05:20.837143+08:00. Any edits will be overridden! -->

1. _(most reactive)_→:::←potassium <!--SR:!2023-10-15,326,270!2023-10-14,358,289-->
2. potassium→:::←sodium <!--SR:!2023-04-27,174,230!2023-04-29,143,228-->
3. sodium→:::←calcium <!--SR:!2023-03-11,80,188!2023-07-17,270,248-->
4. calcium→:::←magnesium <!--SR:!2023-03-20,49,210!2023-02-27,29,166-->
5. magnesium→:::←aluminium <!--SR:!2023-06-10,233,230!2023-03-30,109,209-->
6. aluminium→:::←zinc <!--SR:!2023-02-21,77,168!2023-07-24,188,205-->
7. zinc→:::←iron <!--SR:!2023-03-02,75,188!2023-03-17,98,206-->
8. iron→:::←lead <!--SR:!2023-03-15,99,209!2023-02-26,72,188-->
9. lead→:::←copper <!--SR:!2023-05-06,178,230!2023-04-06,89,210-->
10. copper→:::←mercury <!--SR:!2023-02-16,18,130!2023-02-28,35,210-->
11. mercury→:::←silver <!--SR:!2023-10-09,295,250!2023-07-05,153,230-->
12. silver→:::←gold <!--SR:!2023-04-17,238,290!2024-11-22,711,309-->
13. gold→:::←_(least reactive)_ <!--SR:!2024-02-28,466,308!2023-11-16,451,324-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
