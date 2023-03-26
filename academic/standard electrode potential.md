---
aliases: ['electrochemical series', 'standard electrode potential', 'standard electrode potentials',]
---

#academic/chemistry #flashcards/academic/standard_electrode_potential

# standard electrode potential

## usage

Increase in standard electrode potential {{increases [oxidizing power](oxidation.md) and decreases [reducing power](reduction.md)}}, and vice versa.

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from decimal import Decimal
from pytextgen import gen, read, util
import types, typing
bs: str = '\\'

@typing.final
class Redox(typing.NamedTuple):
	element: str
	oxidant: str
	reductant: str
	potential: Decimal
	electrons: int

	@property
	def equation(self: typing.Self) -> str:
		return f'{self.oxidant} ⇌ {self.reductant}'
data: typing.Sequence[Redox] = tuple(sorted((
	Redox(element='K', oxidant='K<sup>+</sup>(aq) + e<sup>-</sup>', reductant='K(s)', potential=Decimal('-2.931'), electrons=1),
	Redox(element='Ca', oxidant='Ca<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Ca(s)', potential=Decimal('-2.868'), electrons=2),
	Redox(element='Na', oxidant='Na<sup>+</sup>(aq) + e<sup>-</sup>', reductant='Na(s)', potential=Decimal('-2.71'), electrons=1),
	Redox(element='Mg', oxidant='Mg<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Mg(s)', potential=Decimal('-2.372'), electrons=2),
	Redox(element='Al', oxidant='Al<sup>3+</sup>(aq) + 3e<sup>-</sup>', reductant='Al(s)', potential=Decimal('-1.662'), electrons=3),
	Redox(element='Zn', oxidant='Zn<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Zn(s)', potential=Decimal('-0.7618'), electrons=2),
	Redox(element='Fe', oxidant='Fe<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Fe(s)', potential=Decimal('-0.44'), electrons=2),
	Redox(element='Pb', oxidant='Pb<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Pb(s)', potential=Decimal('-0.126'), electrons=2),
	Redox(element='C', oxidant='CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='CO(g) + H<sub>2</sub>O(l)', potential=Decimal('-0.11'), electrons=2),
	Redox(element='H', oxidant='2H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='H<sub>2</sub>(g)', potential=Decimal('0'), electrons=2),
	Redox(element='S', oxidant='S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2H<sup>+</sup>(aq)', reductant='2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)', potential=Decimal('0.08'), electrons=2),
	Redox(element='S', oxidant='HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', potential=Decimal('0.16'), electrons=2),
	Redox(element='S', oxidant='SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', potential=Decimal('0.17'), electrons=2),
	Redox(element='Cu', oxidant='Cu<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Cu(s)', potential=Decimal('0.337'), electrons=2),
	Redox(element='O', oxidant='O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup>', reductant='4OH<sup>-</sup>(aq)', potential=Decimal('0.401'), electrons=4),
	Redox(element='S', oxidant='SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup>', reductant='S(s) + 2H<sub>2</sub>O(l)', potential=Decimal('0.5'), electrons=4),
	Redox(element='C', oxidant='CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='C(s) + H<sub>2</sub>O(l)', potential=Decimal('0.52'), electrons=2),
	Redox(element='I', oxidant='I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup>', reductant='3I<sup>-</sup>(aq)', potential=Decimal('0.53'), electrons=2),
	Redox(element='I', oxidant='I<sub>2</sub>(s) + 2e<sup>-</sup>', reductant='2I<sup>-</sup>(aq)', potential=Decimal('0.54'), electrons=2),
	Redox(element='S', oxidant='S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup>', reductant='2S(s) + 3H<sub>2</sub>O(l)', potential=Decimal('0.6'), electrons=4),
	Redox(element='Fe', oxidant='Fe<sup>3+</sup>(aq) + e<sup>-</sup>', reductant='Fe<sup>2+</sup>(aq)', potential=Decimal('0.77'), electrons=1),
	Redox(element='Ag', oxidant='Ag<sup>+</sup>(aq) + e<sup>-</sup>', reductant='Ag(s)', potential=Decimal('0.7996'), electrons=1),
	Redox(element='N', oxidant='NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup>', reductant='NO<sub>2</sub>(g) + H<sub>2</sub>O(l)', potential=Decimal('0.8'), electrons=1),
	Redox(element='N', oxidant='NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup>', reductant='NO(g) + 2H<sub>2</sub>O(l)', potential=Decimal('0.958'), electrons=3),
	Redox(element='Br', oxidant='Br<sub>2</sub>(aq) + 2e<sup>-</sup>', reductant='2Br<sup>-</sup>(aq)', potential=Decimal('1.0873'), electrons=2),
	Redox(element='I', oxidant='2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup>', reductant='I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)', potential=Decimal('1.2'), electrons=10),
	Redox(element='O', oxidant='O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup>', reductant='2H<sub>2</sub>O(l)', potential=Decimal('1.229'), electrons=4),
	Redox(element='Cr', oxidant='Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup>', reductant='2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)', potential=Decimal('1.33'), electrons=6),
	Redox(element='Cl', oxidant='Cl<sub>2</sub>(g) + 2e<sup>-</sup>', reductant='2Cl<sup>-</sup>(aq)', potential=Decimal('1.36'), electrons=2),
	Redox(element='Mn', oxidant='MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup>', reductant='Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)', potential=Decimal('1.51'), electrons=5),
	Redox(element='O', oxidant='S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup>', reductant='2SO<sub>4</sub><sup>2-</sup>(aq)', potential=Decimal('2.01'), electrons=2),
	Redox(element='F', oxidant='F<sub>2</sub>(g) + 2e<sup>-</sup>', reductant='2F<sup>-</sup>(aq)', potential=Decimal('2.87'), electrons=2),
), key=lambda rdx: rdx.potential))
data_by_element: typing.Mapping[str, typing.Sequence[Redox]] = {}
for rdx in data:
	data_by_element[rdx.element] = data_by_element.get(rdx.element, ()) + (rdx,)
data_by_element = types.MappingProxyType(data_by_element)

table: str = gen.quotette(f''' 
(lowest oxidizing power/highest reducing power)

{gen.rows_to_table(data,
	names=('element', ('oxidant', 'right'), ('⇌', 'center'), ('reductant', 'left'), f'$E^{bs}ominus_{bs}text{{red}}$/V', 'electrons'),
	values=lambda rdx: (rdx.element, rdx.oxidant, '⇌', rdx.reductant, rdx.potential, rdx.electrons),
)}

(highest oxidizing power/lowest reducing power)''',
	prefix='> ',)
potentials: gen.TextCode = gen.two_columns_to_code(data,
	left=lambda rdx: gen.TextCode.escape(rdx.equation),
	right=lambda rdx: gen.TextCode.escape(str(rdx.potential))
)
elements: gen.TextCode = gen.TextCode.compile(
	'{}'.join(f'{gen.TextCode.escape(ele)}{{}}{gen.TextCode.escape("<br/>".join(rdx.equation for rdx in data_by_element[ele]))}' for ele in sorted(data_by_element))
)

return (
	util.Result(
		location=__env__.cwf_section('230419'),
		text=table,
	),
	util.Result(
		location=__env__.cwf_section('9209fd'),
		text=gen.memorize_two_sided(potentials,
			reversible=False,
			states=await read.read_flashcard_states(__env__.cwf_section('9209fd')),
		),
	),
	util.Result(
		location=__env__.cwf_section('ab92dd'),
		text=gen.memorize_two_sided(elements,
			states=await read.read_flashcard_states(__env__.cwf_section('ab92dd'))
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="230419"--><!-- The following content is generated at 2023-03-26T12:58:58.502890+08:00. Any edits will be overridden! -->

>
> (lowest oxidizing power/highest reducing power)
>
> | element | oxidant | ⇌ | reductant | $E^\ominus_\text{red}$/V | electrons |
> |-|-:|:-:|:-|-|-|
> | K | K<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | K(s) | -2.931 | 1 |
> | Ca | Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Ca(s) | -2.868 | 2 |
> | Na | Na<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Na(s) | -2.71 | 1 |
> | Mg | Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Mg(s) | -2.372 | 2 |
> | Al | Al<sup>3+</sup>(aq) + 3e<sup>-</sup> | ⇌ | Al(s) | -1.662 | 3 |
> | Zn | Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Zn(s) | -0.7618 | 2 |
> | Fe | Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Fe(s) | -0.44 | 2 |
> | Pb | Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Pb(s) | -0.126 | 2 |
> | C | CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | CO(g) + H<sub>2</sub>O(l) | -0.11 | 2 |
> | H | 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) | 0 | 2 |
> | S | S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2H<sup>+</sup>(aq) | ⇌ | 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) | 0.08 | 2 |
> | S | HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.16 | 2 |
> | S | SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.17 | 2 |
> | Cu | Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Cu(s) | 0.337 | 2 |
> | O | O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> | ⇌ | 4OH<sup>-</sup>(aq) | 0.401 | 4 |
> | S | SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | S(s) + 2H<sub>2</sub>O(l) | 0.5 | 4 |
> | C | CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | C(s) + H<sub>2</sub>O(l) | 0.52 | 2 |
> | I | I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 3I<sup>-</sup>(aq) | 0.53 | 2 |
> | I | I<sub>2</sub>(s) + 2e<sup>-</sup> | ⇌ | 2I<sup>-</sup>(aq) | 0.54 | 2 |
> | S | S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2S(s) + 3H<sub>2</sub>O(l) | 0.6 | 4 |
> | Fe | Fe<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Fe<sup>2+</sup>(aq) | 0.77 | 1 |
> | Ag | Ag<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Ag(s) | 0.7996 | 1 |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | NO<sub>2</sub>(g) + H<sub>2</sub>O(l) | 0.8 | 1 |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> | ⇌ | NO(g) + 2H<sub>2</sub>O(l) | 0.958 | 3 |
> | Br | Br<sub>2</sub>(aq) + 2e<sup>-</sup> | ⇌ | 2Br<sup>-</sup>(aq) | 1.0873 | 2 |
> | I | 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> | ⇌ | I<sub>2</sub>(s) + 6H<sub>2</sub>O(l) | 1.2 | 10 |
> | O | O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2H<sub>2</sub>O(l) | 1.229 | 4 |
> | Cr | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> | ⇌ | 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) | 1.33 | 6 |
> | Cl | Cl<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2Cl<sup>-</sup>(aq) | 1.36 | 2 |
> | Mn | MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> | ⇌ | Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) | 1.51 | 5 |
> | O | S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2SO<sub>4</sub><sup>2-</sup>(aq) | 2.01 | 2 |
> | F | F<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2F<sup>-</sup>(aq) | 2.87 | 2 |
>
> (highest oxidizing power/lowest reducing power)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### potentials

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9209fd"--><!-- The following content is generated at 2023-03-26T12:58:58.520459+08:00. Any edits will be overridden! -->

1. K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s)::-2.931
2. Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s)::-2.868
3. Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s)::-2.71
4. Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s)::-2.372
5. Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s)::-1.662
6. Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s)::-0.7618
7. Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)::-0.44
8. Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s)::-0.126
9. CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l)::-0.11
10. 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g)::0
11. S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2H<sup>+</sup>(aq) ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)::0.08
12. HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.16
13. SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.17
14. Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s)::0.337
15. O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)::0.401
16. SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l)::0.5
17. CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l)::0.52
18. I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq)::0.53
19. I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)::0.54
20. S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l)::0.6
21. Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq)::0.77
22. Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s)::0.7996
23. NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)::0.8
24. NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l)::0.958
25. Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq)::1.0873
26. 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)::1.2
27. O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l)::1.229
28. Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)::1.33
29. Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq)::1.36
30. MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)::1.51
31. S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq)::2.01
32. F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq)::2.87

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### elements

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab92dd"--><!-- The following content is generated at 2023-03-26T12:58:58.484345+08:00. Any edits will be overridden! -->

1. Ag:::Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s)
2. Al:::Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s)
3. Br:::Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq)
4. C:::CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l)<br/>CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l)
5. Ca:::Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s)
6. Cl:::Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq)
7. Cr:::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)
8. Cu:::Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s)
9. F:::F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq)
10. Fe:::Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)<br/>Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq)
11. H:::2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g)
12. I:::I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq)<br/>I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)<br/>2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)
13. K:::K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s)
14. Mg:::Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s)
15. Mn:::MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)
16. N:::NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)<br/>NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l)
17. Na:::Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s)
18. O:::O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq)
19. Pb:::Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s)
20. S:::S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2H<sup>+</sup>(aq) ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)<br/>HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l)
21. Zn:::Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
