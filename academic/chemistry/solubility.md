#flashcards/chemistry/solubility #academic/chemistry

# solubility

## data

### ionic compounds in water

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
import typing
data: typing.Mapping[str, typing.Mapping[str, str]] = {
	'group I compounds': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Li<sub>3</sub>PO<sub>4</sub>',
	},
	'NH<sub>4</sub><sup>+</sup> compounds': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': '_(none)_',
	},
	'nitrates': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': '_(none)_',
	},
	'acetates (ethanoates)': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Ag<sup>+</sup> compounds',
	},
	'chlorides': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'bromides': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'iodides': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
	},
	'sulfates': {
		'general solubility': R'<span style="color\: green;">soluble</span>',
		'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds',
	},
	'carbonates': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds',
	},
	'sulfites': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds',
	},
	'phosphates': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)',
	},
	'hydroxides': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds',
	},
	'oxides': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds',
	},
	'sulfides': {
		'general solubility': R'<span style="color\: red;">insoluble</span>',
		'exception(s)': 'group I, group II, and NH<sub>4</sub><sup>+</sup> compounds',
	},
}
text: gen.TextCode = gen.common.maps_to_code(data)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('901862'),
		text=gen.common.cloze_text(text,
			states=read.read_flashcard_states(__env__.cwf_section('901862')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="901862"--><!-- The following content is generated at 2022-11-05T00:25:01.033869+08:00. Any edits will be overridden! -->

> group I compounds
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Li<sub>3</sub>PO<sub>4</sub>==

> NH<sub>4</sub><sup>+</sup> compounds
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==_(none)_==

> nitrates
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==_(none)_==

> acetates (ethanoates)
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Ag<sup>+</sup> compounds==

> chlorides
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds==

> bromides
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds==

> iodides
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds==

> sulfates
> - general solubility: ==<span style="color: green;">soluble</span>==
> - exception(s): ==Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds==

> carbonates
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds==

> sulfites
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I and NH<sub>4</sub><sup>+</sup> compounds==

> phosphates
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)==

> hydroxides
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds==

> oxides
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds==

> sulfides
> - general solubility: ==<span style="color: red;">insoluble</span>==
> - exception(s): ==group I, group II, and NH<sub>4</sub><sup>+</sup> compounds==

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
