#flashcards/chemistry/ion #academic/chemistry

# ion

An __ion__ is an atom or molecule with a net electrical charge. A ==__cation__== is a ==positively charged ion==, while an ==__anion__== is a ==negatively charged ion==.

A ==simple ion== is an ==ion formed from only one atom==, while a ==polyatomic ion== is an ==ion formed from more than one atom==.

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
import typing

@typing.final
class Ion(typing.NamedTuple):
	name: str
	symbol: str
	charge: str
	color: str
cations: typing.Sequence[Ion] = (
	Ion(name='hydrogen ion', symbol='H<sup>+</sup>', charge='1+', color='colorless'),
	Ion(name='sodium ion', symbol='Na<sup>+</sup>', charge='1+', color='colorless'),
	Ion(name='potassium ion', symbol='K<sup>+</sup>', charge='1+', color='colorless'),
	Ion(name='copper(I) ion', symbol='Cu<sup>+</sup>', charge='1+', color='_(n/a)_'),
	Ion(name='silver ion', symbol='Ag<sup>+</sup>', charge='1+', color='colorless'),
	Ion(name='mercury(I) ion', symbol='Hg<sup>+</sup>', charge='1+', color='_(n/a)_'),
	Ion(name='ammonium ion', symbol='NH<sub>4</sub><sup>+</sup>', charge='1+', color='colorless'),
	Ion(name='magnesium ion', symbol='Mg<sup>2+</sup>', charge='2+', color='colorless'),
	Ion(name='calcium ion', symbol='Ca<sup>2+</sup>', charge='2+', color='colorless'),
	Ion(name='barium ion', symbol='Ba<sup>2+</sup>', charge='2+', color='colorless'),
	Ion(name='lead(II) ion', symbol='Pb<sup>2+</sup>', charge='2+', color='colorless'),
	Ion(name='iron(II) ion', symbol='Fe<sup>2+</sup>', charge='2+', color='<span style="color: green;">green</span>'),
	Ion(name='nickel(II) ion', symbol='Ni<sup>2+</sup>', charge='2+', color='<span style="color: green;">green</span>'),
	Ion(name='copper(II) ion', symbol='Cu<sup>2+</sup>', charge='2+', color='<span style="color: blue; background-color: white;">blue</span>/<span style="color: green;">green</span>'),
	Ion(name='zinc ion', symbol='Zn<sup>2+</sup>', charge='2+', color='colorless'),
	Ion(name='manganese(II) ion', symbol='Mn<sup>2+</sup>', charge='2+', color='<span style="color: lightPink;">very pale pink</span>'),
	Ion(name='mercury(II) ion', symbol='Hg<sup>2+</sup>', charge='2+', color='_(n/a)_'),
	Ion(name='cobalt(II) ion', symbol='Co<sup>2+</sup>', charge='2+', color='<span style="color: pink;">pink</span>'),
	Ion(name='aluminium ion', symbol='Al<sup>3+</sup>', charge='3+', color='colorless'),
	Ion(name='iron(III) ion', symbol='Fe<sup>3+</sup>', charge='3+', color='<span style="color: yellow;">yellow</span> (dilute)/<span style="color: brown; background-color: white;">brown</span> (concentrated)'),
	Ion(name='chromium(III) ion', symbol='Cr<sup>3+</sup>', charge='3+', color='<span style="color: green;">green</span>'),
)
anions: typing.Sequence[Ion] = (
	Ion(name='hydride ion', symbol='H<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='fluoride ion', symbol='F<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='chloride ion', symbol='Cl<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='bromide ion', symbol='Br<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='iodide ion', symbol='I<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='hydroxide ion', symbol='OH<sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='nitrate ion', symbol='NO<sub>3</sub><sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='nitrite ion', symbol='NO<sub>2</sub><sup>-</sup>', charge='1-', color='_(n/a)_'),
	Ion(name='hydrogencarbonate ion', symbol='HCO<sub>3</sub><sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='hydrogensulfite ion', symbol='HSO<sub>3</sub><sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='hydrogensulfate ion', symbol='HSO<sub>4</sub><sup>-</sup>', charge='1-', color='colorless'),
	Ion(name='permanganate ion', symbol='MnO<sub>4</sub><sup>-</sup>', charge='1-', color='<span style="color: darkViolet; background-color: white;">deep purple</span>'),
	Ion(name='oxide ion', symbol='O<sup>2-</sup>', charge='2-', color='_(n/a)_'),
	Ion(name='sulfide ion', symbol='S<sup>2-</sup>', charge='2-', color='_(n/a)_'),
	Ion(name='sulfate ion', symbol='SO<sub>4</sub><sup>2-</sup>', charge='2-', color='colorless'),
	Ion(name='sulfite ion', symbol='SO<sub>3</sub><sup>2-</sup>', charge='2-', color='colorless'),
	Ion(name='carbonate ion', symbol='CO<sub>3</sub><sup>2-</sup>', charge='2-', color='colorless'),
	Ion(name='chromate ion', symbol='CrO<sub>4</sub><sup>2-</sup>', charge='2-', color='<span style="color: yellow;">yellow</span>'),
	Ion(name='dichromate ion', symbol='Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>', charge='2-', color='<span style="color: orange;">orange</span>'),
	Ion(name='nitride ion', symbol='N<sup>3-</sup>', charge='3-', color='_(n/a)_'),
	Ion(name='phosphate ion', symbol='PO<sub>4</sub><sup>3-</sup>', charge='3-', color='colorless'),
)

@typing.final
class Section(typing.NamedTuple):
	table: str
	symbols: gen.TextCode
	charges: gen.TextCode
	colors: gen.TextCode

	@classmethod
	def from_rows(cls: type[typing.Self],
		rows: typing.Iterable[Ion]
		)-> typing.Self:
		return cls(
			table=gen.affix_lines(gen.common.rows_to_table(rows,
					names=('name', 'symbol', 'charage', 'color'),
					values=util.identity,
				),
				prefix='> ',
			),
			symbols=gen.common.two_columns_to_code(rows,
				left=lambda ion: gen.TextCode.escape(ion.name),
				right=lambda ion: gen.TextCode.escape(ion.symbol),
			),
			charges=gen.common.two_columns_to_code(rows,
				left=lambda ion: gen.TextCode.escape(ion.name),
				right=lambda ion: gen.TextCode.escape(ion.charge),
			),
			colors=gen.common.two_columns_to_code(rows,
				left=lambda ion: gen.TextCode.escape(ion.name),
				right=lambda ion: gen.TextCode.escape(ion.color),
			),
		)
cation_sect: Section = Section.from_rows(cations)
anion_sect: Section = Section.from_rows(anions)

__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('d9192d'),
		text=gen.common.text(cation_sect.table),
	),
	gen.Result(
		location=__env__.cwf_section('3928fd'),
		text=gen.common.memorize_two_sided(cation_sect.symbols,
			hinted=False,
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('3928fd')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('8d8dee'),
		text=gen.common.memorize_two_sided(cation_sect.charges,
			hinted=False,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('8d8dee')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('a5defa'),
		text=gen.common.memorize_two_sided(cation_sect.colors,
			hinted=False,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('a5defa')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('a9fdfe'),
		text=gen.common.text(anion_sect.table),
	),
	gen.Result(
		location=__env__.cwf_section('2fde12'),
		text=gen.common.memorize_two_sided(anion_sect.symbols,
			hinted=False,
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('2fde12')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('8c7820'),
		text=gen.common.memorize_two_sided(anion_sect.charges,
			hinted=False,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('8c7820')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('104852'),
		text=gen.common.memorize_two_sided(anion_sect.colors,
			hinted=False,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('104852')),
		),
	),
)
```
%%

### cation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d9192d"--><!-- The following content is generated at 2022-11-01T23:30:11.543479+08:00. Any edits will be overridden! -->

> name | symbol | charage | color
> -|-|-|-
> hydrogen ion | H<sup>+</sup> | 1+ | colorless
> sodium ion | Na<sup>+</sup> | 1+ | colorless
> potassium ion | K<sup>+</sup> | 1+ | colorless
> copper(I) ion | Cu<sup>+</sup> | 1+ | _(n/a)_
> silver ion | Ag<sup>+</sup> | 1+ | colorless
> mercury(I) ion | Hg<sup>+</sup> | 1+ | _(n/a)_
> ammonium ion | NH<sub>4</sub><sup>+</sup> | 1+ | colorless
> magnesium ion | Mg<sup>2+</sup> | 2+ | colorless
> calcium ion | Ca<sup>2+</sup> | 2+ | colorless
> barium ion | Ba<sup>2+</sup> | 2+ | colorless
> lead(II) ion | Pb<sup>2+</sup> | 2+ | colorless
> iron(II) ion | Fe<sup>2+</sup> | 2+ | <span style="color: green;">green</span>
> nickel(II) ion | Ni<sup>2+</sup> | 2+ | <span style="color: green;">green</span>
> copper(II) ion | Cu<sup>2+</sup> | 2+ | <span style="color: blue; background-color: white;">blue</span>/<span style="color: green;">green</span>
> zinc ion | Zn<sup>2+</sup> | 2+ | colorless
> manganese(II) ion | Mn<sup>2+</sup> | 2+ | <span style="color: lightPink;">very pale pink</span>
> mercury(II) ion | Hg<sup>2+</sup> | 2+ | _(n/a)_
> cobalt(II) ion | Co<sup>2+</sup> | 2+ | <span style="color: pink;">pink</span>
> aluminium ion | Al<sup>3+</sup> | 3+ | colorless
> iron(III) ion | Fe<sup>3+</sup> | 3+ | <span style="color: yellow;">yellow</span> (dilute)/<span style="color: brown; background-color: white;">brown</span> (concentrated)
> chromium(III) ion | Cr<sup>3+</sup> | 3+ | <span style="color: green;">green</span>
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3928fd"--><!-- The following content is generated at 2022-10-31T21:51:04.555706+08:00. Any edits will be overridden! -->

1. hydrogen ion→:::←H<sup>+</sup>
2. sodium ion→:::←Na<sup>+</sup>
3. potassium ion→:::←K<sup>+</sup>
4. copper(I) ion→:::←Cu<sup>+</sup>
5. silver ion→:::←Ag<sup>+</sup>
6. mercury(I) ion→:::←Hg<sup>+</sup>
7. ammonium ion→:::←NH<sub>4</sub><sup>+</sup>
8. magnesium ion→:::←Mg<sup>2+</sup>
9. calcium ion→:::←Ca<sup>2+</sup>
10. barium ion→:::←Ba<sup>2+</sup>
11. lead(II) ion→:::←Pb<sup>2+</sup>
12. iron(II) ion→:::←Fe<sup>2+</sup>
13. nickel(II) ion→:::←Ni<sup>2+</sup>
14. copper(II) ion→:::←Cu<sup>2+</sup>
15. zinc ion→:::←Zn<sup>2+</sup>
16. manganese(II) ion→:::←Mn<sup>2+</sup>
17. mercury(II) ion→:::←Hg<sup>2+</sup>
18. cobalt(II) ion→:::←Co<sup>2+</sup>
19. aluminium ion→:::←Al<sup>3+</sup>
20. iron(III) ion→:::←Fe<sup>3+</sup>
21. chromium(III) ion→:::←Cr<sup>3+</sup>
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8d8dee"--><!-- The following content is generated at 2022-10-31T21:51:04.571709+08:00. Any edits will be overridden! -->

1. hydrogen ion→::←1+
2. sodium ion→::←1+
3. potassium ion→::←1+
4. copper(I) ion→::←1+
5. silver ion→::←1+
6. mercury(I) ion→::←1+
7. ammonium ion→::←1+
8. magnesium ion→::←2+
9. calcium ion→::←2+
10. barium ion→::←2+
11. lead(II) ion→::←2+
12. iron(II) ion→::←2+
13. nickel(II) ion→::←2+
14. copper(II) ion→::←2+
15. zinc ion→::←2+
16. manganese(II) ion→::←2+
17. mercury(II) ion→::←2+
18. cobalt(II) ion→::←2+
19. aluminium ion→::←3+
20. iron(III) ion→::←3+
21. chromium(III) ion→::←3+
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a5defa"--><!-- The following content is generated at 2022-10-31T21:51:04.584709+08:00. Any edits will be overridden! -->

1. hydrogen ion→::←colorless
2. sodium ion→::←colorless
3. potassium ion→::←colorless
4. copper(I) ion→::←_(n/a)_
5. silver ion→::←colorless
6. mercury(I) ion→::←_(n/a)_
7. ammonium ion→::←colorless
8. magnesium ion→::←colorless
9. calcium ion→::←colorless
10. barium ion→::←colorless
11. lead(II) ion→::←colorless
12. iron(II) ion→::←<span style="color: green;">green</span>
13. nickel(II) ion→::←<span style="color: green;">green</span>
14. copper(II) ion→::←<span style="color: blue; background-color: white;">blue</span>/<span style="color: green;">green</span>
15. zinc ion→::←colorless
16. manganese(II) ion→::←<span style="color: lightPink;">very pale pink</span>
17. mercury(II) ion→::←_(n/a)_
18. cobalt(II) ion→::←<span style="color: pink;">pink</span>
19. aluminium ion→::←colorless
20. iron(III) ion→::←<span style="color: yellow;">yellow</span> (dilute)/<span style="color: brown; background-color: white;">brown</span> (concentrated)
21. chromium(III) ion→::←<span style="color: green;">green</span>
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### anion

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9fdfe"--><!-- The following content is generated at 2022-11-01T23:30:11.579477+08:00. Any edits will be overridden! -->

> name | symbol | charage | color
> -|-|-|-
> hydride ion | H<sup>-</sup> | 1- | colorless
> fluoride ion | F<sup>-</sup> | 1- | colorless
> chloride ion | Cl<sup>-</sup> | 1- | colorless
> bromide ion | Br<sup>-</sup> | 1- | colorless
> iodide ion | I<sup>-</sup> | 1- | colorless
> hydroxide ion | OH<sup>-</sup> | 1- | colorless
> nitrate ion | NO<sub>3</sub><sup>-</sup> | 1- | colorless
> nitrite ion | NO<sub>2</sub><sup>-</sup> | 1- | _(n/a)_
> hydrogencarbonate ion | HCO<sub>3</sub><sup>-</sup> | 1- | colorless
> hydrogensulfite ion | HSO<sub>3</sub><sup>-</sup> | 1- | colorless
> hydrogensulfate ion | HSO<sub>4</sub><sup>-</sup> | 1- | colorless
> permanganate ion | MnO<sub>4</sub><sup>-</sup> | 1- | <span style="color: darkViolet; background-color: white;">deep purple</span>
> oxide ion | O<sup>2-</sup> | 2- | _(n/a)_
> sulfide ion | S<sup>2-</sup> | 2- | _(n/a)_
> sulfate ion | SO<sub>4</sub><sup>2-</sup> | 2- | colorless
> sulfite ion | SO<sub>3</sub><sup>2-</sup> | 2- | colorless
> carbonate ion | CO<sub>3</sub><sup>2-</sup> | 2- | colorless
> chromate ion | CrO<sub>4</sub><sup>2-</sup> | 2- | <span style="color: yellow;">yellow</span>
> dichromate ion | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> | 2- | <span style="color: orange;">orange</span>
> nitride ion | N<sup>3-</sup> | 3- | _(n/a)_
> phosphate ion | PO<sub>4</sub><sup>3-</sup> | 3- | colorless
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2fde12"--><!-- The following content is generated at 2022-10-31T21:51:04.604716+08:00. Any edits will be overridden! -->

1. hydride ion→:::←H<sup>-</sup>
2. fluoride ion→:::←F<sup>-</sup>
3. chloride ion→:::←Cl<sup>-</sup>
4. bromide ion→:::←Br<sup>-</sup>
5. iodide ion→:::←I<sup>-</sup>
6. hydroxide ion→:::←OH<sup>-</sup>
7. nitrate ion→:::←NO<sub>3</sub><sup>-</sup>
8. nitrite ion→:::←NO<sub>2</sub><sup>-</sup>
9. hydrogencarbonate ion→:::←HCO<sub>3</sub><sup>-</sup>
10. hydrogensulfite ion→:::←HSO<sub>3</sub><sup>-</sup>
11. hydrogensulfate ion→:::←HSO<sub>4</sub><sup>-</sup>
12. permanganate ion→:::←MnO<sub>4</sub><sup>-</sup>
13. oxide ion→:::←O<sup>2-</sup>
14. sulfide ion→:::←S<sup>2-</sup>
15. sulfate ion→:::←SO<sub>4</sub><sup>2-</sup>
16. sulfite ion→:::←SO<sub>3</sub><sup>2-</sup>
17. carbonate ion→:::←CO<sub>3</sub><sup>2-</sup>
18. chromate ion→:::←CrO<sub>4</sub><sup>2-</sup>
19. dichromate ion→:::←Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>
20. nitride ion→:::←N<sup>3-</sup>
21. phosphate ion→:::←PO<sub>4</sub><sup>3-</sup>
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8c7820"--><!-- The following content is generated at 2022-10-31T21:51:04.620710+08:00. Any edits will be overridden! -->

1. hydride ion→::←1-
2. fluoride ion→::←1-
3. chloride ion→::←1-
4. bromide ion→::←1-
5. iodide ion→::←1-
6. hydroxide ion→::←1-
7. nitrate ion→::←1-
8. nitrite ion→::←1-
9. hydrogencarbonate ion→::←1-
10. hydrogensulfite ion→::←1-
11. hydrogensulfate ion→::←1-
12. permanganate ion→::←1-
13. oxide ion→::←2-
14. sulfide ion→::←2-
15. sulfate ion→::←2-
16. sulfite ion→::←2-
17. carbonate ion→::←2-
18. chromate ion→::←2-
19. dichromate ion→::←2-
20. nitride ion→::←3-
21. phosphate ion→::←3-
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="104852"--><!-- The following content is generated at 2022-10-31T21:51:04.630707+08:00. Any edits will be overridden! -->

1. hydride ion→::←colorless
2. fluoride ion→::←colorless
3. chloride ion→::←colorless
4. bromide ion→::←colorless
5. iodide ion→::←colorless
6. hydroxide ion→::←colorless
7. nitrate ion→::←colorless
8. nitrite ion→::←_(n/a)_
9. hydrogencarbonate ion→::←colorless
10. hydrogensulfite ion→::←colorless
11. hydrogensulfate ion→::←colorless
12. permanganate ion→::←<span style="color: darkViolet; background-color: white;">deep purple</span>
13. oxide ion→::←_(n/a)_
14. sulfide ion→::←_(n/a)_
15. sulfate ion→::←colorless
16. sulfite ion→::←colorless
17. carbonate ion→::←colorless
18. chromate ion→::←<span style="color: yellow;">yellow</span>
19. dichromate ion→::←<span style="color: orange;">orange</span>
20. nitride ion→::←_(n/a)_
21. phosphate ion→::←colorless
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
