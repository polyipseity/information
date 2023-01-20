---
aliases: ['electrochemical series',]
---

#flashcards/chemistry/standard_electrode_potential #academic/chemistry

# standard electrode potential

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
import decimal, types, typing
bs: str = '\\'

@typing.final
class Redox(typing.NamedTuple):
	element: str
	oxidant: str
	reductant: str
	potential: decimal.Decimal
	electrons: int

	@property
	def equation(self: typing.Self) -> str:
		return f'{self.oxidant} ⇌ {self.reductant}'
data: typing.Sequence[Redox] = tuple(sorted((
	Redox(element='K', oxidant='K<sup>+</sup>(aq) + e<sup>-</sup>', reductant='K(s)', potential=decimal.Decimal('-2.931'), electrons=1),
	Redox(element='Ca', oxidant='Ca<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Ca(s)', potential=decimal.Decimal('-2.868'), electrons=2),
	Redox(element='Na', oxidant='Na<sup>+</sup>(aq) + e<sup>-</sup>', reductant='Na(s)', potential=decimal.Decimal('-2.71'), electrons=1),
	Redox(element='Mg', oxidant='Mg<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Mg(s)', potential=decimal.Decimal('-2.372'), electrons=2),
	Redox(element='Al', oxidant='Al<sup>3+</sup>(aq) + 3e<sup>-</sup>', reductant='Al(s)', potential=decimal.Decimal('-1.662'), electrons=3),
	Redox(element='Zn', oxidant='Zn<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Zn(s)', potential=decimal.Decimal('-0.7618'), electrons=2),
	Redox(element='Fe', oxidant='Fe<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Fe(s)', potential=decimal.Decimal('-0.44'), electrons=2),
	Redox(element='Pb', oxidant='Pb<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Pb(s)', potential=decimal.Decimal('-0.126'), electrons=2),
	Redox(element='H', oxidant='2H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='H<sub>2</sub>(g)', potential=decimal.Decimal('0'), electrons=2),
	Redox(element='S', oxidant='HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', potential=decimal.Decimal('0.16'), electrons=2),
	Redox(element='S', oxidant='SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup>', reductant='SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', potential=decimal.Decimal('0.17'), electrons=2),
	Redox(element='Cu', oxidant='Cu<sup>2+</sup>(aq) + 2e<sup>-</sup>', reductant='Cu(s)', potential=decimal.Decimal('0.337'), electrons=2),
	Redox(element='O', oxidant='O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup>', reductant='4OH<sup>-</sup>(aq)', potential=decimal.Decimal('0.401'), electrons=4),
	Redox(element='I', oxidant='I<sub>2</sub>(s) + 2e<sup>-</sup>', reductant='2I<sup>-</sup>(aq)', potential=decimal.Decimal('0.54'), electrons=2),
	Redox(element='Fe', oxidant='Fe<sup>3+</sup>(aq) + e<sup>-</sup>', reductant='Fe<sup>2+</sup>(aq)', potential=decimal.Decimal('0.77'), electrons=1),
	Redox(element='Ag', oxidant='Ag<sup>+</sup>(aq) + e<sup>-</sup>', reductant='Ag(s)', potential=decimal.Decimal('0.7996'), electrons=1),
	Redox(element='N', oxidant='NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup>', reductant='NO<sub>2</sub>(g) + H<sub>2</sub>O(l)', potential=decimal.Decimal('0.8'), electrons=1),
	Redox(element='N', oxidant='NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup>', reductant='NO(g) + 2H<sub>2</sub>O(l)', potential=decimal.Decimal('0.958'), electrons=3),
	Redox(element='Br', oxidant='Br<sub>2</sub>(aq) + 2e<sup>-</sup>', reductant='2Br<sup>-</sup>(aq)', potential=decimal.Decimal('1.0873'), electrons=2),
	Redox(element='Cr', oxidant='Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup>', reductant='2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)', potential=decimal.Decimal('1.33'), electrons=6),
	Redox(element='Cl', oxidant='Cl<sub>2</sub>(g) + 2e<sup>-</sup>', reductant='2Cl<sup>-</sup>(aq)', potential=decimal.Decimal('1.36'), electrons=2),
	Redox(element='Mn', oxidant='MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup>', reductant='Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)', potential=decimal.Decimal('1.51'), electrons=5),
	Redox(element='O', oxidant='S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup>', reductant='2SO<sub>4</sub><sup>2-</sup>(aq)', potential=decimal.Decimal('2.01'), electrons=2),
	Redox(element='F', oxidant='F<sub>2</sub>(g) + 2e<sup>-</sup>', reductant='2F<sup>-</sup>(aq)', potential=decimal.Decimal('2.87'), electrons=2),
), key=lambda rdx: rdx.potential))
data_by_element: typing.Mapping[str, typing.Sequence[Redox]] = {}
for rdx in data:
	data_by_element[rdx.element] = data_by_element.get(rdx.element, ()) + (rdx,)
data_by_element = types.MappingProxyType(data_by_element)

table: str = gen.affix_lines(f''' 
(lowest oxidizing power/highest reducing power)

{gen.common.rows_to_table(data,
	names=('element', ('oxidant', 'right'), ('⇌', 'center'), ('reductant', 'left'), f'$E^{bs}ominus_{bs}text{{red}}$/V', 'electrons'),
	values=lambda rdx: (rdx.element, rdx.oxidant, '⇌', rdx.reductant, rdx.potential, rdx.electrons),
)}

(highest oxidizing power/lowest reducing power)''',
	prefix='> ',)
potentials: gen.TextCode = gen.common.two_columns_to_code(data,
	left=lambda rdx: gen.TextCode.escape(rdx.equation),
	right=lambda rdx: gen.TextCode.escape(str(rdx.potential))
)
elements: gen.TextCode = gen.TextCode.compile(
	'{}'.join(f'{gen.TextCode.escape(ele)}{{}}{gen.TextCode.escape("<br/>".join(rdx.equation for rdx in data_by_element[ele]))}' for ele in sorted(data_by_element))
)

__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('230419'),
		text=gen.common.text(table),
	),
	gen.Result(
		location=__env__.cwf_section('9209fd'),
		text=gen.common.memorize_two_sided(potentials,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('9209fd')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('ab92dd'),
		text=gen.common.memorize_two_sided(elements,
			states=read.read_flashcard_states(__env__.cwf_section('ab92dd'))
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="230419"--><!-- The following content is generated at 2022-11-05T00:25:01.009874+08:00. Any edits will be overridden! -->

>
> (lowest oxidizing power/highest reducing power)
>
> element | oxidant | ⇌ | reductant | $E^\ominus_\text{red}$/V | electrons
> -|-:|:-:|:-|-|-
> K | K<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | K(s) | -2.931 | 1
> Ca | Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Ca(s) | -2.868 | 2
> Na | Na<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Na(s) | -2.71 | 1
> Mg | Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Mg(s) | -2.372 | 2
> Al | Al<sup>3+</sup>(aq) + 3e<sup>-</sup> | ⇌ | Al(s) | -1.662 | 3
> Zn | Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Zn(s) | -0.7618 | 2
> Fe | Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Fe(s) | -0.44 | 2
> Pb | Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Pb(s) | -0.126 | 2
> H | 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) | 0 | 2
> S | HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.16 | 2
> S | SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.17 | 2
> Cu | Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Cu(s) | 0.337 | 2
> O | O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> | ⇌ | 4OH<sup>-</sup>(aq) | 0.401 | 4
> I | I<sub>2</sub>(s) + 2e<sup>-</sup> | ⇌ | 2I<sup>-</sup>(aq) | 0.54 | 2
> Fe | Fe<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Fe<sup>2+</sup>(aq) | 0.77 | 1
> Ag | Ag<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Ag(s) | 0.7996 | 1
> N | NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | NO<sub>2</sub>(g) + H<sub>2</sub>O(l) | 0.8 | 1
> N | NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> | ⇌ | NO(g) + 2H<sub>2</sub>O(l) | 0.958 | 3
> Br | Br<sub>2</sub>(aq) + 2e<sup>-</sup> | ⇌ | 2Br<sup>-</sup>(aq) | 1.0873 | 2
> Cr | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> | ⇌ | 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) | 1.33 | 6
> Cl | Cl<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2Cl<sup>-</sup>(aq) | 1.36 | 2
> Mn | MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> | ⇌ | Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) | 1.51 | 5
> O | S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2SO<sub>4</sub><sup>2-</sup>(aq) | 2.01 | 2
> F | F<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2F<sup>-</sup>(aq) | 2.87 | 2
>
> (highest oxidizing power/lowest reducing power)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### potentials

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9209fd"--><!-- The following content is generated at 2022-11-09T18:05:20.808143+08:00. Any edits will be overridden! -->

1. K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s)::-2.931 <!--SR:!2023-03-20,80,210-->
2. Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s)::-2.868 <!--SR:!2023-01-25,5,130-->
3. Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s)::-2.71 <!--SR:!2023-01-25,10,130-->
4. Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s)::-2.372 <!--SR:!2023-01-26,11,130-->
5. Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s)::-1.662 <!--SR:!2023-01-27,12,130-->
6. Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s)::-0.7618 <!--SR:!2023-02-07,18,130-->
7. Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)::-0.44 <!--SR:!2023-04-29,167,210-->
8. Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s)::-0.126 <!--SR:!2023-03-11,61,210-->
9. 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g)::0 <!--SR:!2023-03-07,189,250-->
10. HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.16 <!--SR:!2023-01-24,14,150-->
11. SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.17 <!--SR:!2023-05-19,187,230-->
12. Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s)::0.337 <!--SR:!2023-02-03,21,130-->
13. O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)::0.401 <!--SR:!2023-04-23,126,210-->
14. I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)::0.54 <!--SR:!2023-01-25,13,130-->
15. Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq)::0.77 <!--SR:!2023-05-25,181,190-->
16. Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s)::0.7996 <!--SR:!2023-01-30,23,170-->
17. NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)::0.8 <!--SR:!2023-02-03,64,230-->
18. NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l)::0.958 <!--SR:!2023-04-18,101,210-->
19. Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq)::1.0873 <!--SR:!2023-03-03,53,190-->
20. Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)::1.33 <!--SR:!2023-02-23,46,150-->
21. Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq)::1.36 <!--SR:!2023-02-19,37,150-->
22. MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)::1.51 <!--SR:!2023-01-23,16,130-->
23. S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq)::2.01 <!--SR:!2023-02-08,19,130-->
24. F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq)::2.87 <!--SR:!2023-02-06,24,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### elements

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab92dd"--><!-- The following content is generated at 2022-11-09T18:05:20.821142+08:00. Any edits will be overridden! -->

1. Ag:::Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s) <!--SR:!2023-02-09,168,250!2024-08-11,636,330-->
2. Al:::Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s) <!--SR:!2023-05-08,143,250!2024-08-15,639,330-->
3. Br:::Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq) <!--SR:!2023-05-04,140,250!2024-08-05,631,330-->
4. Ca:::Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s) <!--SR:!2023-02-04,165,250!2024-08-26,648,330-->
5. Cl:::Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq) <!--SR:!2023-02-24,178,250!2024-07-19,618,330-->
6. Cr:::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) <!--SR:!2023-02-25,179,250!2024-02-12,456,310-->
7. Cu:::Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s) <!--SR:!2023-08-07,251,250!2024-08-10,636,330-->
8. F:::F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq) <!--SR:!2023-02-05,167,250!2024-07-02,604,330-->
9. Fe:::Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)<br/>Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq) <!--SR:!2023-06-25,205,210!2023-08-19,303,290-->
10. H:::2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) <!--SR:!2023-07-23,251,230!2023-08-28,312,290-->
11. I:::I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq) <!--SR:!2023-02-17,171,250!2023-08-28,312,290-->
12. K:::K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s) <!--SR:!2024-03-31,449,250!2023-07-07,205,290-->
13. Mg:::Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s) <!--SR:!2023-02-11,170,250!2024-08-08,634,330-->
14. Mn:::MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) <!--SR:!2024-02-21,462,310!2024-02-09,453,310-->
15. N:::NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)<br/>NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l) <!--SR:!2023-03-14,101,230!2023-08-09,293,270-->
16. Na:::Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s) <!--SR:!2023-02-18,172,250!2024-08-31,652,330-->
17. O:::O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq) <!--SR:!2023-11-30,324,230!2024-08-04,630,330-->
18. Pb:::Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s) <!--SR:!2023-04-10,120,230!2024-01-22,441,310-->
19. S:::HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) <!--SR:!2023-12-22,338,230!2023-08-29,313,290-->
20. Zn:::Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s) <!--SR:!2023-11-18,315,230!2024-01-28,446,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
