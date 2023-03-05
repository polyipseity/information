#flashcards/chemistry/solubility #academic/chemistry

# solubility

## data

### ionic compounds in water

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
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
text: gen.TextCode = gen.maps_to_code(data)
return util.Results(
	util.Result(
		location=__env__.cwf_section('901862'),
		text=gen.cloze_text(text,
			states=await read.read_flashcard_states(__env__.cwf_section('901862')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="901862"--><!-- The following content is generated at 2022-11-05T00:25:01.033869+08:00. Any edits will be overridden! -->

> group I compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Li<sub>3</sub>PO<sub>4</sub>}} <!--SR:!2023-06-11,234,210!2023-03-06,33,190-->

> NH<sub>4</sub><sup>+</sup> compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2023-06-07,276,262!2024-01-21,324,289-->

> nitrates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2023-07-09,254,216!2023-04-18,120,269-->

> acetates (ethanoates)
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup> compounds}} <!--SR:!2023-04-15,228,242!2023-04-27,142,230-->

> chlorides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-04-01,222,248!2023-04-05,148,190-->

> bromides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-09-19,329,246!2023-09-06,196,170-->

> iodides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-08-30,310,242!2023-06-03,193,210-->

> sulfates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds}} <!--SR:!2023-04-22,235,241!2023-08-03,168,230-->

> carbonates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2023-09-23,328,248!2023-07-28,242,250-->

> sulfites
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2023-06-05,196,206!2023-05-23,119,210-->

> phosphates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)}} <!--SR:!2024-06-04,460,230!2023-03-26,38,190-->

> hydroxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}} <!--SR:!2023-07-20,273,230!2023-09-04,183,230-->

> oxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}} <!--SR:!2023-03-13,203,230!2023-03-07,46,190-->

> sulfides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, group II, and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2023-03-14,204,238!2023-07-08,137,190-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
