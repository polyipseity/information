#academic/chemistry #flashcards/academic/air_separation

# air separation

__Air separation__ {{separates [atmospheric air](atmosphere%20of%20Earth.md) into its components}}. It is carried out in {{an air separation plant}}.

The most common method is [cryogenic distillation](#cryogenic%20distillation).

## cryogenic distillation

- See also: [fractional distillation](fractional%20distillation.md).

Pure gases are separated by {{cooling air until it [liquefies](liquefaction.md). Then [distill](distillation.md) the components at their boiling points.}}

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import memorize_linked_seq, quote_text, seq_to_code
from pytextgen.read import read_flashcard_states
from pytextgen.util import Result
e = __env__
data = seq_to_code(
	(
		'Filter air to remove [dust](dust.md).',
		'Compress air. Most [water](water.md) is condensed out in [inter-stage coolers](intercooler.md). [Temperature](temperature.md) decreases to about 193 K.',
		'Pass air through a [molecular sieve](molecular%20sieve.md) bed to remove now-solid water vapor and [carbon dioxide](carbon%20dioxide.md).',
		'Air is cooled with [heat exchangers](heat%20exchanger.md) and [expanders](expander.md), becoming liquid. Temperature decreases to about 73 K.',
		'Liquid air is passed into [fractionating columns](fractionating%20column.md). Nitrogen, argon, and oxygen respectively boils at 77.4 K, 87.3 K, and 90.2 K. Gas that boils first are collected at the top.',
		'Products are warmed against incoming air to ambient temperatures.',
	),
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(suffix)_}',
)
return (
	Result(
		location=e.cwf_section('28370e'),
		text=quote_text(data),
	),
	Result(
		location=e.cwf_section('293842'),
		text=memorize_linked_seq(
			data,
			hinted=False,
			states=await read_flashcard_states(e.cwf_section('293842')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="28370e"--><!-- The following content is generated at 2023-03-14T22:07:25.690765+08:00. Any edits will be overridden! -->

> 1. Filter air to remove [dust](dust.md).
> 2. Compress air. Most [water](water.md) is condensed out in [inter-stage coolers](intercooler.md). [Temperature](temperature.md) decreases to about 193 K.
> 3. Pass air through a [molecular sieve](molecular%20sieve.md) bed to remove now-solid water vapor and [carbon dioxide](carbon%20dioxide.md).
> 4. Air is cooled with [heat exchangers](heat%20exchanger.md) and [expanders](expander.md), becoming liquid. Temperature decreases to about 73 K.
> 5. Liquid air is passed into [fractionating columns](fractionating%20column.md). Nitrogen, argon, and oxygen respectively boils at 77.4 K, 87.3 K, and 90.2 K. Gas that boils first are collected at the top.
> 6. Products are warmed against incoming air to ambient temperatures.

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="293842"--><!-- The following content is generated at 2023-03-14T22:09:57.718882+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←Filter air to remove [dust](dust.md).
2. Filter air to remove [dust](dust.md).→:::←Compress air. Most [water](water.md) is condensed out in [inter-stage coolers](intercooler.md). [Temperature](temperature.md) decreases to about 193 K.
3. Compress air. Most [water](water.md) is condensed out in [inter-stage coolers](intercooler.md). [Temperature](temperature.md) decreases to about 193 K.→:::←Pass air through a [molecular sieve](molecular%20sieve.md) bed to remove now-solid water vapor and [carbon dioxide](carbon%20dioxide.md).
4. Pass air through a [molecular sieve](molecular%20sieve.md) bed to remove now-solid water vapor and [carbon dioxide](carbon%20dioxide.md).→:::←Air is cooled with [heat exchangers](heat%20exchanger.md) and [expanders](expander.md), becoming liquid. Temperature decreases to about 73 K.
5. Air is cooled with [heat exchangers](heat%20exchanger.md) and [expanders](expander.md), becoming liquid. Temperature decreases to about 73 K.→:::←Liquid air is passed into [fractionating columns](fractionating%20column.md). Nitrogen, argon, and oxygen respectively boils at 77.4 K, 87.3 K, and 90.2 K. Gas that boils first are collected at the top.
6. Liquid air is passed into [fractionating columns](fractionating%20column.md). Nitrogen, argon, and oxygen respectively boils at 77.4 K, 87.3 K, and 90.2 K. Gas that boils first are collected at the top.→:::←Products are warmed against incoming air to ambient temperatures.
7. Products are warmed against incoming air to ambient temperatures.→:::←_(suffix)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
