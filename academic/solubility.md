---
aliases:
  - insoluble
  - soluble
tags:
  - academic/chemistry
  - flashcards/academic/Ss/solubility
---

# solubility

__Solubility__ is {{the ability of a [solute](solution%20(chemistry).md) to form a [solution](solution%20(chemistry).md) with a [solvent](solvent.md)}}. <!--SR:!2023-06-08,16,212-->

It is measured as {{the [concentration](concentration.md) of the solute in a saturated solution, in which no more solute can be [dissolved](solvation.md)}}. <!--SR:!2023-09-25,118,272-->

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
> - exception(s): {{Li<sub>3</sub>PO<sub>4</sub>}} <!--SR:!2023-06-11,234,210!2023-09-11,126,190-->

> NH<sub>4</sub><sup>+</sup> compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2026-03-15,1012,282!2024-01-21,324,289-->

> nitrates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2023-07-09,254,216!2024-07-15,454,289-->

> acetates (ethanoates)
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup> compounds}} <!--SR:!2024-10-17,551,242!2024-03-22,329,230-->

> chlorides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2025-05-13,773,268!2024-01-10,280,190-->

> bromides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-09-19,329,246!2023-09-06,196,170-->

> iodides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-08-30,310,242!2024-07-23,412,210-->

> sulfates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds}} <!--SR:!2025-06-27,797,261!2023-08-03,168,230-->

> carbonates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-09-23,328,248!2023-07-28,242,250-->

> sulfites
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2024-07-26,415,206!2024-02-07,260,210-->

> phosphates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)}} <!--SR:!2024-06-04,460,230!2023-06-10,76,190-->

> hydroxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is poorly soluble)}} <!--SR:!2023-07-20,273,230!2023-09-04,183,230-->

> oxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}} <!--SR:!2025-01-01,660,250!2023-07-15,45,170-->

> sulfides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, group II, and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2024-07-12,486,238!2023-07-08,137,190-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
