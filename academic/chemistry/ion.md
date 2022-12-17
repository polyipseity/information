#flashcards/chemistry/ion #academic/chemistry

# ion

An __ion__ is an atom or molecule with a net electrical charge. A ==__cation__== is a ==positively charged ion==, while an ==__anion__== is a ==negatively charged ion==.<!--SR:!2023-02-02,305,345!2023-03-30,350,350!2023-01-07,282,332!2023-02-16,318,354-->

A ==simple ion== is an ==ion formed from only one atom==, while a ==polyatomic ion== is an ==ion formed from more than one atom==. <!--SR:!2023-02-24,276,287!2023-04-24,370,352!2024-05-12,539,267!2025-04-11,857,334-->

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
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('3928fd')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('8d8dee'),
		text=gen.common.memorize_two_sided(cation_sect.charges,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('8d8dee')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('a5defa'),
		text=gen.common.memorize_two_sided(cation_sect.colors,
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
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('2fde12')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('8c7820'),
		text=gen.common.memorize_two_sided(anion_sect.charges,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('8c7820')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('104852'),
		text=gen.common.memorize_two_sided(anion_sect.colors,
			reversible=False,
			states=read.read_flashcard_states(__env__.cwf_section('104852')),
		),
	),
)
```
%%

### cation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d9192d"--><!-- The following content is generated at 2022-11-05T00:25:01.410870+08:00. Any edits will be overridden! -->

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3928fd"--><!-- The following content is generated at 2022-11-06T20:13:24.273182+08:00. Any edits will be overridden! -->

1. hydrogen ion:::H<sup>+</sup> <!--SR:!2025-05-22,945,332!2022-12-26,273,339-->
2. sodium ion:::Na<sup>+</sup> <!--SR:!2023-02-06,309,350!2023-03-17,340,353-->
3. potassium ion:::K<sup>+</sup> <!--SR:!2023-04-06,353,339!2023-04-20,367,353-->
4. copper(I) ion:::Cu<sup>+</sup> <!--SR:!2023-02-09,308,339!2023-01-20,92,290-->
5. silver ion:::Ag<sup>+</sup> <!--SR:!2023-06-03,285,270!2023-01-10,267,336-->
6. mercury(I) ion:::Hg<sup>+</sup> <!--SR:!2023-03-21,342,347!2023-02-23,303,310-->
7. ammonium ion:::NH<sub>4</sub><sup>+</sup> <!--SR:!2023-03-17,148,250!2023-05-14,328,293-->
8. magnesium ion:::Mg<sup>2+</sup> <!--SR:!2022-12-20,210,247!2024-02-04,523,316-->
9. calcium ion:::Ca<sup>2+</sup> <!--SR:!2023-03-14,337,350!2023-04-10,359,354-->
10. barium ion:::Ba<sup>2+</sup> <!--SR:!2023-01-15,87,230!2023-01-03,260,294-->
11. lead(II) ion:::Pb<sup>2+</sup> <!--SR:!2023-02-17,318,354!2024-02-24,536,314-->
12. iron(II) ion:::Fe<sup>2+</sup> <!--SR:!2023-01-28,300,339!2023-04-01,350,345-->
13. nickel(II) ion:::Ni<sup>2+</sup> <!--SR:!2023-03-15,335,339!2023-10-22,426,290-->
14. copper(II) ion:::Cu<sup>2+</sup> <!--SR:!2023-02-19,318,347!2024-09-24,705,334-->
15. zinc ion:::Zn<sup>2+</sup> <!--SR:!2024-07-29,595,273!2023-05-10,184,253-->
16. manganese(II) ion:::Mn<sup>2+</sup> <!--SR:!2023-02-23,126,250!2024-01-08,445,253-->
17. mercury(II) ion:::Hg<sup>2+</sup> <!--SR:!2026-03-20,1192,350!2022-12-29,255,293-->
18. cobalt(II) ion:::Co<sup>2+</sup> <!--SR:!2023-02-20,319,347!2023-01-31,279,294-->
19. aluminium ion:::Al<sup>3+</sup> <!--SR:!2023-09-25,383,252!2024-07-03,622,314-->
20. iron(III) ion:::Fe<sup>3+</sup> <!--SR:!2023-02-13,314,350!2023-01-06,285,354-->
21. chromium(III) ion:::Cr<sup>3+</sup> <!--SR:!2023-04-09,359,354!2023-01-24,275,294-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8d8dee"--><!-- The following content is generated at 2022-11-06T20:13:24.309183+08:00. Any edits will be overridden! -->

1. hydrogen ion::1+ <!--SR:!2023-02-10,312,353-->
2. sodium ion::1+ <!--SR:!2024-02-08,522,310-->
3. potassium ion::1+ <!--SR:!2023-08-10,418,292-->
4. copper(I) ion::1+ <!--SR:!2023-04-25,371,352-->
5. silver ion::1+ <!--SR:!2023-10-18,409,270-->
6. mercury(I) ion::1+ <!--SR:!2023-03-11,336,354-->
7. ammonium ion::1+ <!--SR:!2024-01-21,509,314-->
8. magnesium ion::2+ <!--SR:!2023-08-03,346,253-->
9. calcium ion::2+ <!--SR:!2023-01-14,238,272-->
10. barium ion::2+ <!--SR:!2024-01-27,456,254-->
11. lead(II) ion::2+ <!--SR:!2022-12-25,272,338-->
12. iron(II) ion::2+ <!--SR:!2023-05-01,376,353-->
13. nickel(II) ion::2+ <!--SR:!2023-01-17,289,332-->
14. copper(II) ion::2+ <!--SR:!2023-03-09,334,352-->
15. zinc ion::2+ <!--SR:!2023-01-25,87,224-->
16. manganese(II) ion::2+ <!--SR:!2023-01-13,289,347-->
17. mercury(II) ion::2+ <!--SR:!2023-02-21,321,354-->
18. cobalt(II) ion::2+ <!--SR:!2023-02-08,311,352-->
19. aluminium ion::3+ <!--SR:!2024-01-14,507,312-->
20. iron(III) ion::3+ <!--SR:!2023-01-05,282,345-->
21. chromium(III) ion::3+ <!--SR:!2023-01-27,299,338-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a5defa"--><!-- The following content is generated at 2022-11-06T20:13:24.330184+08:00. Any edits will be overridden! -->

1. hydrogen ion::colorless <!--SR:!2024-02-05,519,309-->
2. sodium ion::colorless <!--SR:!2023-04-28,314,293-->
3. potassium ion::colorless <!--SR:!2023-12-14,479,304-->
4. copper(I) ion::_(n/a)_ <!--SR:!2023-01-20,50,276-->
5. silver ion::colorless <!--SR:!2023-08-12,355,259-->
6. mercury(I) ion::_(n/a)_ <!--SR:!2023-01-15,46,276-->
7. ammonium ion::colorless <!--SR:!2023-03-20,339,339-->
8. magnesium ion::colorless <!--SR:!2023-01-17,241,274-->
9. calcium ion::colorless <!--SR:!2024-03-02,499,272-->
10. barium ion::colorless <!--SR:!2022-12-30,230,274-->
11. lead(II) ion::colorless <!--SR:!2023-04-15,236,253-->
12. iron(II) ion::<span style="color: green;">green</span> <!--SR:!2024-03-06,484,254-->
13. nickel(II) ion::<span style="color: green;">green</span> <!--SR:!2022-12-22,122,227-->
14. copper(II) ion::<span style="color: blue; background-color: white;">blue</span>/<span style="color: green;">green</span> <!--SR:!2023-01-02,43,190-->
15. zinc ion::colorless <!--SR:!2024-02-23,535,314-->
16. manganese(II) ion::<span style="color: lightPink;">very pale pink</span> <!--SR:!2022-12-28,128,230-->
17. mercury(II) ion::_(n/a)_ <!--SR:!2023-02-06,54,256-->
18. cobalt(II) ion::<span style="color: pink;">pink</span> <!--SR:!2024-03-03,461,239-->
19. aluminium ion::colorless <!--SR:!2024-07-04,623,314-->
20. iron(III) ion::<span style="color: yellow;">yellow</span> (dilute)/<span style="color: brown; background-color: white;">brown</span> (concentrated) <!--SR:!2023-07-08,209,190-->
21. chromium(III) ion::<span style="color: green;">green</span> <!--SR:!2023-11-29,402,238-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### anion

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9fdfe"--><!-- The following content is generated at 2022-11-05T00:25:01.448870+08:00. Any edits will be overridden! -->

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2fde12"--><!-- The following content is generated at 2022-11-06T20:13:24.353184+08:00. Any edits will be overridden! -->

1. hydride ion:::H<sup>-</sup> <!--SR:!2026-03-03,1183,354!2026-02-13,1171,356-->
2. fluoride ion:::F<sup>-</sup> <!--SR:!2024-01-09,502,310!2023-02-22,322,354-->
3. chloride ion:::Cl<sup>-</sup> <!--SR:!2023-03-04,330,353!2025-11-03,1086,354-->
4. bromide ion:::Br<sup>-</sup> <!--SR:!2023-08-04,347,253!2025-02-23,814,294-->
5. iodide ion:::I<sup>-</sup> <!--SR:!2024-11-28,760,332!2023-05-02,318,293-->
6. hydroxide ion:::OH<sup>-</sup> <!--SR:!2023-01-29,298,332!2023-02-05,308,354-->
7. nitrate ion:::NO<sub>3</sub><sup>-</sup> <!--SR:!2023-11-04,439,292!2023-06-15,349,294-->
8. nitrite ion:::NO<sub>2</sub><sup>-</sup> <!--SR:!2023-01-18,90,239!2023-05-05,319,290-->
9. hydrogencarbonate ion:::HCO<sub>3</sub><sup>-</sup> <!--SR:!2023-04-15,301,279!2023-12-08,473,312-->
10. hydrogensulfite ion:::HSO<sub>3</sub><sup>-</sup> <!--SR:!2023-10-26,415,270!2023-06-13,347,294-->
11. hydrogensulfate ion:::HSO<sub>4</sub><sup>-</sup> <!--SR:!2023-03-22,343,347!2026-01-17,1128,350-->
12. permanganate ion:::MnO<sub>4</sub><sup>-</sup> <!--SR:!2023-09-02,376,273!2023-01-29,101,213-->
13. oxide ion:::O<sup>2-</sup> <!--SR:!2024-08-09,659,310!2023-03-18,295,293-->
14. sulfide ion:::S<sup>2-</sup> <!--SR:!2024-02-13,481,267!2024-02-22,533,310-->
15. sulfate ion:::SO<sub>4</sub><sup>2-</sup> <!--SR:!2024-05-15,573,299!2025-10-13,1049,345-->
16. sulfite ion:::SO<sub>3</sub><sup>2-</sup> <!--SR:!2023-10-28,432,293!2023-08-18,296,254-->
17. carbonate ion:::CO<sub>3</sub><sup>2-</sup> <!--SR:!2024-04-18,528,270!2023-12-28,493,313-->
18. chromate ion:::CrO<sub>4</sub><sup>2-</sup> <!--SR:!2024-01-20,457,258!2024-06-29,618,313-->
19. dichromate ion:::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> <!--SR:!2024-01-25,462,258!2023-12-05,470,305-->
20. nitride ion:::N<sup>3-</sup> <!--SR:!2024-02-11,479,267!2023-04-13,175,290-->
21. phosphate ion:::PO<sub>4</sub><sup>3-</sup> <!--SR:!2023-04-03,113,219!2024-08-25,617,276-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8c7820"--><!-- The following content is generated at 2022-11-06T20:13:24.365182+08:00. Any edits will be overridden! -->

1. hydride ion::1- <!--SR:!2023-06-30,370,299-->
2. fluoride ion::1- <!--SR:!2025-04-20,869,292-->
3. chloride ion::1- <!--SR:!2023-04-21,368,354-->
4. bromide ion::1- <!--SR:!2025-03-11,823,293-->
5. iodide ion::1- <!--SR:!2023-08-18,361,259-->
6. hydroxide ion::1- <!--SR:!2023-04-23,309,293-->
7. nitrate ion::1- <!--SR:!2023-01-31,162,270-->
8. nitrite ion::1- <!--SR:!2023-10-27,431,292-->
9. hydrogencarbonate ion::1- <!--SR:!2023-10-31,435,290-->
10. hydrogensulfite ion::1- <!--SR:!2024-12-16,746,319-->
11. hydrogensulfate ion::1- <!--SR:!2023-04-18,304,284-->
12. permanganate ion::1- <!--SR:!2022-12-25,40,230-->
13. oxide ion::2- <!--SR:!2023-04-30,316,290-->
14. sulfide ion::2- <!--SR:!2022-12-30,71,230-->
15. sulfate ion::2- <!--SR:!2023-10-15,419,290-->
16. sulfite ion::2- <!--SR:!2023-01-25,249,279-->
17. carbonate ion::2- <!--SR:!2024-02-10,478,270-->
18. chromate ion::2- <!--SR:!2022-12-21,226,279-->
19. dichromate ion::2- <!--SR:!2023-05-18,328,290-->
20. nitride ion::3- <!--SR:!2023-05-22,331,290-->
21. phosphate ion::3- <!--SR:!2022-12-31,131,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="104852"--><!-- The following content is generated at 2022-11-06T20:13:24.378182+08:00. Any edits will be overridden! -->

1. hydride ion::colorless <!--SR:!2023-06-23,357,299-->
2. fluoride ion::colorless <!--SR:!2024-04-19,532,274-->
3. chloride ion::colorless <!--SR:!2024-06-23,612,314-->
4. bromide ion::colorless <!--SR:!2023-08-21,364,259-->
5. iodide ion::colorless <!--SR:!2023-11-30,465,307-->
6. hydroxide ion::colorless <!--SR:!2023-01-02,259,327-->
7. nitrate ion::colorless <!--SR:!2023-12-01,466,299-->
8. nitrite ion::_(n/a)_ <!--SR:!2023-02-09,65,276-->
9. hydrogencarbonate ion::colorless <!--SR:!2024-06-11,600,310-->
10. hydrogensulfite ion::colorless <!--SR:!2023-07-29,341,250-->
11. hydrogensulfate ion::colorless <!--SR:!2024-02-29,497,270-->
12. permanganate ion::<span style="color: darkViolet; background-color: white;">deep purple</span> <!--SR:!2024-02-16,434,250-->
13. oxide ion::_(n/a)_ <!--SR:!2023-01-27,55,276-->
14. sulfide ion::_(n/a)_ <!--SR:!2023-01-16,47,276-->
15. sulfate ion::colorless <!--SR:!2023-08-31,374,274-->
16. sulfite ion::colorless <!--SR:!2023-03-13,105,274-->
17. carbonate ion::colorless <!--SR:!2023-04-14,235,252-->
18. chromate ion::<span style="color: yellow;">yellow</span> <!--SR:!2023-01-02,74,230-->
19. dichromate ion::<span style="color: orange;">orange</span> <!--SR:!2023-09-15,389,273-->
20. nitride ion::_(n/a)_ <!--SR:!2023-01-19,48,276-->
21. phosphate ion::colorless <!--SR:!2023-09-14,388,273-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
