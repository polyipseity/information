---
aliases: ['activity series',]
---

#flashcards/chemistry/reactivity_series #academic/chemistry

# reactivity series

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
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
return util.Results(
	util.Result(
		location=__env__.cwf_section('a2994d'),
		text=gen.common.cloze_text(text,
			states=await read.read_flashcard_states(__env__.cwf_section('a2994d'))
		),
	),
	util.Result(
		location=__env__.cwf_section('299018'),
		text=gen.common.memorize_linked_seq(series,
			hinted=False,
			states=await read.read_flashcard_states(__env__.cwf_section('299018')),
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
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{explosive}}

> sodium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{water}}
> - reaction with dilute HCl: {{explosive}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{explosive}}

> calcium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{water}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate to none (covered by insoluble CaSO<sub>4</sub>)}}

> magnesium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}}

> aluminium
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}}

> zinc
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}}

> iron
> - reaction with air: {{burn}}
> - reaction with H<sub>2</sub>O: {{steam}}
> - reaction with dilute HCl: {{moderate}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{moderate}}

> lead
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{slow}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{slow to none (covered by insoluble PbSO<sub>4</sub>)}}

> copper
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}}

> mercury
> - reaction with air: {{heat}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}}

> silver
> - reaction with air: {{none}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}}

> gold
> - reaction with air: {{none}}
> - reaction with H<sub>2</sub>O: {{none}}
> - reaction with dilute HCl: {{none}}
> - reaction with dilute H<sub>2</sub>SO<sub>4</sub>: {{none}}

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2022-11-09T18:05:20.837143+08:00. Any edits will be overridden! -->

1. _(most reactive)_→:::←potassium
2. potassium→:::←sodium
3. sodium→:::←calcium
4. calcium→:::←magnesium
5. magnesium→:::←aluminium
6. aluminium→:::←zinc
7. zinc→:::←iron
8. iron→:::←lead
9. lead→:::←copper
10. copper→:::←mercury
11. mercury→:::←silver
12. silver→:::←gold
13. gold→:::←_(least reactive)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
