---
aliases:
  - insoluble
  - soluble
tags:
  - academic/chemistry
  - flashcards/academic/Ss/solubility
---

# solubility

__Solubility__ is {{the ability of a [solute](solution%20(chemistry).md) to form a [solution](solution%20(chemistry).md) with a [solvent](solvent.md)}}.

It is measured as {{the [concentration](concentration.md) of the solute in a saturated solution, in which no more solute can be [dissolved](solvation.md)}}.

## data

### ionic compounds in water

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
import typing
soluble = R'<span style="color\: green;">soluble</span>'
insoluble = R'<span style="color\: red;">insoluble</span>'
data: typing.Mapping[str, typing.Mapping[str, str]] = {
	'group I compounds': {
		'general solubility': soluble,
		'exception(s)': 'Li<sub>3</sub>PO<sub>4</sub>',
	},
	'NH<sub>4</sub><sup>+</sup> compounds': {
		'general solubility': soluble,
		'exception(s)': '_(none)_',
	},
	'nitrates': {
		'general solubility': soluble,
		'exception(s)': '_(none)_',
	},
	'acetates (ethanoates)': {
		'general solubility': soluble,
		'exception(s)': 'Ag<sup>+</sup> compounds',
	},
	'chlorides': {
		'general solubility': soluble,
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'bromides': {
		'general solubility': soluble,
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'iodides': {
		'general solubility': soluble,
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'sulfates': {
		'general solubility': soluble,
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds',
	},
	'carbonates': {
		'general solubility': insoluble,
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds',
	},
	'sulfites': {
		'general solubility': insoluble,
		'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds',
	},
	'phosphates': {
		'general solubility': insoluble,
		'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)',
	},
	'hydroxides': {
		'general solubility': insoluble,
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is poorly soluble)',
	},
	'oxides': {
		'general solubility': insoluble,
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds',
	},
	'sulfides': {
		'general solubility': insoluble,
		'exception(s)': 'group I, group II, and NH<sub>4</sub><sup>+</sup> compounds',
	},
}
text: gen.TextCode = gen.maps_to_code(data)
return (
	util.Result(
		location=__env__.cwf_sect('901862'),
		text=gen.cloze_text(text,
			states=await read.read_flashcard_states(__env__.cwf_sect('901862')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="901862"--><!-- The following content is generated at 2023-03-23T02:22:59.729037+08:00. Any edits will be overridden! -->

> group I compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Li<sub>3</sub>PO<sub>4</sub>}}

> NH<sub>4</sub><sup>+</sup> compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}}

> nitrates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}}

> acetates (ethanoates)
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup> compounds}}

> chlorides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}}

> bromides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}}

> iodides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}}

> sulfates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds}}

> carbonates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds}}

> sulfites
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds}}

> phosphates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)}}

> hydroxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is poorly soluble)}}

> oxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}}

> sulfides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, group II, and NH<sub>4</sub><sup>+</sup> compounds}}

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->