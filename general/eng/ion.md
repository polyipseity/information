---
aliases:
  - anion
  - anions
  - cation
  - cations
  - ion
  - ions
tags:
  - flashcard/active/general/eng/ion
  - language/in/English
---

# ion

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

An __ion__ is an [atom](atom.md) or [molecule](molecule.md) with a net electrical charge. A {@{__cation__}@} is a {@{positively charged ion}@}, while an {@{__anion__}@} is a {@{negatively charged ion}@}.<!--SR:!2027-01-19,1447,365!2027-11-08,1684,370!2026-07-20,1290,352!2027-05-12,1546,374-->

A {@{simple ion}@} is an {@{ion formed from only one atom}@}, while a {@{polyatomic ion}@} is an {@{ion formed from more than one atom}@}. <!--SR:!2026-03-02,1102,307!2028-03-17,1789,372!2028-04-22,1440,267!2025-04-11,857,334-->

## data

```Python
# pytextgen generate data
from asyncio import gather
from dataclasses import dataclass
from itertools import chain
from pytextgen import gen, read, util
import typing

COLORLESS = 'colorless'
NA_COLOR = '_(n/a)_'
BLUE = '<span style="color: blue; background-color: white;">blue</span>'
BROWN = '<span style="color: brown; background-color: white;">brown</span>'
DEEP_PURPLE = '<span style="color: darkViolet; background-color: white;">deep purple</span>'
GREEN = '<span style="color: green;">green</span>'
ORANGE = '<span style="color: orange;">orange</span>'
PINK = '<span style="color: pink;">pink</span>'
PURPLE = '<span style="color: purple; background-color: white;">purple</span>'
RED = '<span style="color: red;">red</color>'
VERY_PALE_PINK = '<span style="color: lightPink;">very pale pink</span>'
VIOLET = '<span style="color: violet;">violet</span>'
YELLOW = '<span style="color: yellow; background-color: black;">yellow</span>'

@typing.final
class Ion(typing.NamedTuple):
  name: str
  symbol: str
  charge: int
  color: str | tuple[str, ...]
cations: typing.Sequence[Ion] = (
  Ion(name='hydrogen ion', symbol='H<sup>+</sup>', charge=1, color=COLORLESS),
  Ion(name='sodium ion', symbol='Na<sup>+</sup>', charge=1, color=COLORLESS),
  Ion(name='potassium ion', symbol='K<sup>+</sup>', charge=1, color=COLORLESS),
  Ion(name='copper(I) ion', symbol='Cu<sup>+</sup>', charge=1, color=NA_COLOR),
  Ion(name='silver ion', symbol='Ag<sup>+</sup>', charge=1, color=COLORLESS),
  Ion(name='mercury(I) ion', symbol='Hg<sup>+</sup>', charge=1, color=NA_COLOR),
  Ion(name='ammonium ion', symbol='NH<sub>4</sub><sup>+</sup>', charge=1, color=COLORLESS),
  Ion(name='magnesium ion', symbol='Mg<sup>2+</sup>', charge=2, color=COLORLESS),
  Ion(name='calcium ion', symbol='Ca<sup>2+</sup>', charge=2, color=COLORLESS),
  Ion(name='barium ion', symbol='Ba<sup>2+</sup>', charge=2, color=COLORLESS),
  Ion(name='lead(II) ion', symbol='Pb<sup>2+</sup>', charge=2, color=COLORLESS),
  Ion(name='iron(II) ion', symbol='Fe<sup>2+</sup>', charge=2, color=GREEN),
  Ion(name='nickel(II) ion', symbol='Ni<sup>2+</sup>', charge=2, color=GREEN),
  Ion(name='copper(II) ion', symbol='Cu<sup>2+</sup>', charge=2, color=(BLUE, GREEN,)),
  Ion(name='zinc ion', symbol='Zn<sup>2+</sup>', charge=2, color=COLORLESS),
  Ion(name='manganese(II) ion', symbol='Mn<sup>2+</sup>', charge=2, color=VERY_PALE_PINK),
  Ion(name='mercury(II) ion', symbol='Hg<sup>2+</sup>', charge=2, color=NA_COLOR),
  Ion(name='cobalt(II) ion', symbol='Co<sup>2+</sup>', charge=2, color=PINK),
  Ion(name='aluminium ion', symbol='Al<sup>3+</sup>', charge=3, color=COLORLESS),
  Ion(name='iron(III) ion', symbol='Fe<sup>3+</sup>', charge=3, color=(f'{YELLOW} (dilute)', f'{BROWN} (concentrated)',)),
  Ion(name='chromium(III) ion', symbol='Cr<sup>3+</sup>', charge=3, color=GREEN),
  Ion(name='scandium(III) ion', symbol='Sc<sup>3+</sup>', charge=3, color=COLORLESS),
  Ion(name='titanium(III) ion', symbol='Ti<sup>3+</sup>', charge=3, color=PURPLE),
  Ion(name='vanadium(II) ion', symbol='V<sup>2+</sup>', charge=2, color=VIOLET),
  Ion(name='vanadium(III) ion', symbol='V<sup>3+</sup>', charge=3, color=GREEN),
  Ion(name='manganese(III) ion', symbol='Mn<sup>3+</sup>', charge=3, color=RED),
)
anions: typing.Sequence[Ion] = (
  Ion(name='hydride ion', symbol='H<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='fluoride ion', symbol='F<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='chloride ion', symbol='Cl<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='bromide ion', symbol='Br<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='iodide ion', symbol='I<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='hydroxide ion', symbol='OH<sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='nitrate ion', symbol='NO<sub>3</sub><sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='nitrite ion', symbol='NO<sub>2</sub><sup>-</sup>', charge=-1, color=NA_COLOR),
  Ion(name='hydrogencarbonate ion', symbol='HCO<sub>3</sub><sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='hydrogensulfite ion', symbol='HSO<sub>3</sub><sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='hydrogensulfate ion', symbol='HSO<sub>4</sub><sup>-</sup>', charge=-1, color=COLORLESS),
  Ion(name='permanganate ion', symbol='MnO<sub>4</sub><sup>-</sup>', charge=-1, color=DEEP_PURPLE),
  Ion(name='oxide ion', symbol='O<sup>2-</sup>', charge=-2, color=NA_COLOR),
  Ion(name='sulfide ion', symbol='S<sup>2-</sup>', charge=-2, color=NA_COLOR),
  Ion(name='sulfate ion', symbol='SO<sub>4</sub><sup>2-</sup>', charge=-2, color=COLORLESS),
  Ion(name='sulfite ion', symbol='SO<sub>3</sub><sup>2-</sup>', charge=-2, color=COLORLESS),
  Ion(name='carbonate ion', symbol='CO<sub>3</sub><sup>2-</sup>', charge=-2, color=COLORLESS),
  Ion(name='chromate ion', symbol='CrO<sub>4</sub><sup>2-</sup>', charge=-2, color=YELLOW),
  Ion(name='dichromate ion', symbol='Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>', charge=-2, color=ORANGE),
  Ion(name='nitride ion', symbol='N<sup>3-</sup>', charge=-3, color=NA_COLOR),
  Ion(name='phosphate ion', symbol='PO<sub>4</sub><sup>3-</sup>', charge=-3, color=COLORLESS),
  Ion(name='manganate ion', symbol='MnO<sub>4</sub><sup>2-</sup>', charge=-2, color=GREEN),
)

@typing.final
@dataclass(
  init=True,
  repr=True,
  eq=True,
  order=False,
  unsafe_hash=False,
  frozen=True,
  match_args=True,
  kw_only=True,
  slots=True,
)
class Section:
  data: typing.Sequence[Ion]
  table: str
  symbols: gen.TextCode
  charges: gen.TextCode
  colors: gen.TextCode
  EXCLUDE_COLORS: typing.ClassVar = (COLORLESS, NA_COLOR,)

  @classmethod
  def from_rows(
    cls: type[typing.Self],
    rows: typing.Iterable[Ion]
  ) -> typing.Self:
    rows = tuple(rows)
    def charge_str(charge: int):
      return f'{abs(charge)}{"+" if charge > 0 else "-" if charge < 0 else ""}'
    return cls(
      data=rows,
      table=gen.quotette(gen.rows_to_table(rows,
          names=('name', 'symbol', 'charge', 'color'),
          values=lambda datum: (
            *datum[:2],
            charge_str(datum[2]),
            datum[3] if isinstance(datum[3], str) else ', '.join(datum[3]),
            *datum[4:],
          ),
        ),
        prefix='> ',
      ),
      symbols=gen.two_columns_to_code(rows,
        left=lambda ion: gen.TextCode.escape(ion.name),
        right=lambda ion: gen.TextCode.escape(ion.symbol),
      ),
      charges=gen.two_columns_to_code(rows,
        left=lambda ion: gen.TextCode.escape(ion.name),
        right=lambda ion: gen.TextCode.escape(charge_str(ion.charge)),
      ),
      colors=gen.two_columns_to_code(rows,
        left=lambda ion: gen.TextCode.escape(ion.name),
        right=lambda ion: gen.TextCode.escape(ion.color if isinstance(ion.color, str) else ', '.join(ion.color)),
      ),
    )

  async def memorize(self, locations: tuple[util.Location, util.Location, util.Location, util.Location, util.Location]):
    states, colorR, colorL = await gather(
      read_states(locations[1:3]),
      memorize_map(
        (util.NULL_LOCATION, locations[3], util.NULL_LOCATION,),
        {ion.name: ion.color for ion in self.data if ion.color},
      ),
      memorize_map(
        (util.NULL_LOCATION, util.NULL_LOCATION, locations[4],),
        {ion.name: ion.color for ion in self.data if ion.color not in self.EXCLUDE_COLORS},
      ),
    )
    return (
      util.Result(
        location=locations[0],
        text=self.table,
      ),
      util.Result(
        location=locations[1],
        text=gen.memorize_two_sided(self.symbols,
          reversible=True,
          states=states[0],
        ),
      ),
      util.Result(
        location=locations[2],
        text=gen.memorize_two_sided(self.charges,
          reversible=False,
          states=states[1],
        ),
      ),
      *colorR,
      *colorL,
    )
cation_sect = Section.from_rows(cations)
anion_sect = Section.from_rows(anions)
return chain.from_iterable(await gather(
  cation_sect.memorize(
    (
      __env__.cwf_sect('d9192d'),
      __env__.cwf_sect('3928fd'),
      __env__.cwf_sect('8d8dee'),
      __env__.cwf_sect('a5defa'),
      __env__.cwf_sect('394a'),
    ),
  ),
  anion_sect.memorize(
    (
      __env__.cwf_sect('a9fdfe'),
      __env__.cwf_sect('2fde12'),
      __env__.cwf_sect('8c7820'),
      __env__.cwf_sect('104852'),
      __env__.cwf_sect('50ad'),
    ),
  ),
))
```

### cation

<!--pytextgen generate section="d9192d"--><!-- The following content is generated at 2024-02-17T20:40:56.103599+08:00. Any edits will be overridden! -->

> | name | symbol | charge | color |
> |-|-|-|-|
> | hydrogen ion | H<sup>+</sup> | 1+ | colorless |
> | sodium ion | Na<sup>+</sup> | 1+ | colorless |
> | potassium ion | K<sup>+</sup> | 1+ | colorless |
> | copper(I) ion | Cu<sup>+</sup> | 1+ | _(n/a)_ |
> | silver ion | Ag<sup>+</sup> | 1+ | colorless |
> | mercury(I) ion | Hg<sup>+</sup> | 1+ | _(n/a)_ |
> | ammonium ion | NH<sub>4</sub><sup>+</sup> | 1+ | colorless |
> | magnesium ion | Mg<sup>2+</sup> | 2+ | colorless |
> | calcium ion | Ca<sup>2+</sup> | 2+ | colorless |
> | barium ion | Ba<sup>2+</sup> | 2+ | colorless |
> | lead(II) ion | Pb<sup>2+</sup> | 2+ | colorless |
> | iron(II) ion | Fe<sup>2+</sup> | 2+ | <span style="color: green;">green</span> |
> | nickel(II) ion | Ni<sup>2+</sup> | 2+ | <span style="color: green;">green</span> |
> | copper(II) ion | Cu<sup>2+</sup> | 2+ | <span style="color: blue; background-color: white;">blue</span>, <span style="color: green;">green</span> |
> | zinc ion | Zn<sup>2+</sup> | 2+ | colorless |
> | manganese(II) ion | Mn<sup>2+</sup> | 2+ | <span style="color: lightPink;">very pale pink</span> |
> | mercury(II) ion | Hg<sup>2+</sup> | 2+ | _(n/a)_ |
> | cobalt(II) ion | Co<sup>2+</sup> | 2+ | <span style="color: pink;">pink</span> |
> | aluminium ion | Al<sup>3+</sup> | 3+ | colorless |
> | iron(III) ion | Fe<sup>3+</sup> | 3+ | <span style="color: yellow; background-color: black;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated) |
> | chromium(III) ion | Cr<sup>3+</sup> | 3+ | <span style="color: green;">green</span> |
> | scandium(III) ion | Sc<sup>3+</sup> | 3+ | colorless |
> | titanium(III) ion | Ti<sup>3+</sup> | 3+ | <span style="color: purple; background-color: white;">purple</span> |
> | vanadium(II) ion | V<sup>2+</sup> | 2+ | <span style="color: violet;">violet</span> |
> | vanadium(III) ion | V<sup>3+</sup> | 3+ | <span style="color: green;">green</span> |
> | manganese(III) ion | Mn<sup>3+</sup> | 3+ | <span style="color: red;">red</color> |

<!--/pytextgen-->

#### name–symbol (cation)

<!--pytextgen generate section="3928fd"--><!-- The following content is generated at 2024-01-04T20:17:52.176781+08:00. Any edits will be overridden! -->

- hydrogen ion::@::H<sup>+</sup> <!--SR:!2025-05-22,945,332!2025-07-11,927,339-->
- sodium ion::@::Na<sup>+</sup> <!--SR:!2027-03-03,1486,370!2027-09-21,1649,373-->
- potassium ion::@::K<sup>+</sup> <!--SR:!2027-10-09,1647,359!2028-03-04,1780,373-->
- copper(I) ion::@::Cu<sup>+</sup> <!--SR:!2027-02-02,1451,359!2028-06-30,1612,330-->
- silver ion::@::Ag<sup>+</sup> <!--SR:!2026-05-27,1086,290!2025-06-25,897,336-->
- mercury(I) ion::@::Hg<sup>+</sup> <!--SR:!2027-09-08,1632,367!2026-09-15,1300,330-->
- ammonium ion::@::NH<sub>4</sub><sup>+</sup> <!--SR:!2029-12-25,1956,290!2027-01-08,1335,313-->
- magnesium ion::@::Mg<sup>2+</sup> <!--SR:!2027-05-17,1165,267!2030-05-06,2283,336-->
- calcium ion::@::Ca<sup>2+</sup> <!--SR:!2027-08-21,1621,370!2028-01-19,1745,374-->
- barium ion::@::Ba<sup>2+</sup> <!--SR:!2025-06-02,665,250!2033-09-24,3143,314-->
- lead(II) ion::@::Pb<sup>2+</sup> <!--SR:!2027-06-06,1566,374!2030-07-08,2326,334-->
- iron(II) ion::@::Fe<sup>2+</sup> <!--SR:!2026-11-28,1400,359!2027-10-18,1661,365-->
- nickel(II) ion::@::Ni<sup>2+</sup> <!--SR:!2027-06-25,1563,359!2028-07-06,1716,310-->
- copper(II) ion::@::Cu<sup>2+</sup> <!--SR:!2027-04-27,1526,367!2033-08-11,3243,354-->
- zinc ion::@::Zn<sup>2+</sup> <!--SR:!2030-10-11,2265,293!2031-12-17,2490,293-->
- manganese(II) ion::@::Mn<sup>2+</sup> <!--SR:!2028-11-26,1662,290!2028-05-04,1578,273-->
- mercury(II) ion::@::Hg<sup>2+</sup> <!--SR:!2026-03-20,1192,350!2025-11-01,1038,313-->
- cobalt(II) ion::@::Co<sup>2+</sup> <!--SR:!2027-04-28,1527,367!2025-04-30,820,294-->
- aluminium ion::@::Al<sup>3+</sup> <!--SR:!2027-07-03,1372,272!2031-11-24,2700,334-->
- iron(III) ion::@::Fe<sup>3+</sup> <!--SR:!2027-04-21,1525,370!2026-10-29,1391,374-->
- chromium(III) ion::@::Cr<sup>3+</sup> <!--SR:!2028-01-18,1745,374!2026-02-20,1123,314-->
- scandium(III) ion::@::Sc<sup>3+</sup> <!--SR:!2030-11-05,2231,402!2031-10-13,2508,402-->
- titanium(III) ion::@::Ti<sup>3+</sup> <!--SR:!2030-10-02,2204,402!2031-09-24,2493,402-->
- vanadium(II) ion::@::V<sup>2+</sup> <!--SR:!2031-06-24,2420,402!2031-12-11,2557,402-->
- vanadium(III) ion::@::V<sup>3+</sup> <!--SR:!2031-07-02,2425,402!2031-05-03,2378,402-->
- manganese(III) ion::@::Mn<sup>3+</sup> <!--SR:!2031-03-23,2346,402!2031-09-30,2498,402-->

<!--/pytextgen-->

#### name–charge (cation)

<!--pytextgen generate section="8d8dee"--><!-- The following content is generated at 2024-01-04T20:17:52.061211+08:00. Any edits will be overridden! -->

- hydrogen ion:@:1+ <!--SR:!2027-04-14,1522,373-->
- sodium ion:@:1+ <!--SR:!2030-03-26,2238,330-->
- potassium ion:@:1+ <!--SR:!2028-04-05,1699,312-->
- copper(I) ion:@:1+ <!--SR:!2028-03-23,1794,372-->
- silver ion:@:1+ <!--SR:!2028-01-13,1541,290-->
- mercury(I) ion:@:1+ <!--SR:!2027-08-31,1634,374-->
- ammonium ion:@:1+ <!--SR:!2030-02-09,2209,334-->
- magnesium ion:@:2+ <!--SR:!2026-12-17,1231,273-->
- calcium ion:@:2+ <!--SR:!2031-07-25,2464,292-->
- barium ion:@:2+ <!--SR:!2027-03-30,1157,254-->
- lead(II) ion:@:2+ <!--SR:!2026-06-13,1266,358-->
- iron(II) ion:@:2+ <!--SR:!2028-04-27,1823,373-->
- nickel(II) ion:@:2+ <!--SR:!2026-08-31,1322,352-->
- copper(II) ion:@:2+ <!--SR:!2026-05-28,1176,352-->
- zinc ion:@:2+ <!--SR:!2025-04-30,628,244-->
- manganese(II) ion:@:2+ <!--SR:!2026-10-23,1379,367-->
- mercury(II) ion:@:2+ <!--SR:!2027-06-01,1561,374-->
- cobalt(II) ion:@:2+ <!--SR:!2027-04-15,1523,372-->
- aluminium ion:@:3+ <!--SR:!2030-01-09,2187,332-->
- iron(III) ion:@:3+ <!--SR:!2026-09-16,1348,365-->
- chromium(III) ion:@:3+ <!--SR:!2026-11-24,1396,358-->
- scandium(III) ion:@:3+ <!--SR:!2031-05-08,2382,402-->
- titanium(III) ion:@:3+ <!--SR:!2031-04-26,2372,402-->
- vanadium(II) ion:@:2+ <!--SR:!2031-06-04,2404,402-->
- vanadium(III) ion:@:3+ <!--SR:!2031-06-26,2420,402-->
- manganese(III) ion:@:3+ <!--SR:!2031-10-19,2514,402-->

<!--/pytextgen-->

#### name–color (cation)

<!--pytextgen generate section="a5defa"--><!-- The following content is generated at 2024-01-28T09:35:09.995261+08:00. Any edits will be overridden! -->

- hydrogen ion:@:colorless <!--SR:!2030-03-04,2219,329-->
- sodium ion:@:colorless <!--SR:!2025-11-02,919,293-->
- potassium ion:@:colorless <!--SR:!2029-06-22,2017,324-->
- copper(I) ion:@:_(n/a)_ <!--SR:!2027-06-23,1081,276-->
- silver ion:@:colorless <!--SR:!2027-03-01,1295,279-->
- mercury(I) ion:@:_(n/a)_ <!--SR:!2028-04-14,1415,296-->
- ammonium ion:@:colorless <!--SR:!2026-05-12,1149,339-->
- magnesium ion:@:colorless <!--SR:!2029-10-22,1810,274-->
- calcium ion:@:colorless <!--SR:!2029-05-08,1893,292-->
- barium ion:@:colorless <!--SR:!2031-04-27,2407,294-->
- lead(II) ion:@:colorless <!--SR:!2029-01-17,1506,253-->
- iron(II) ion:@:<span style="color: green;">green</span> <!--SR:!2027-07-17,1228,254-->
- nickel(II) ion:@:<span style="color: green;">green</span> <!--SR:!2025-03-26,423,207-->
- copper(II) ion:@:<span style="color: blue; background-color: white;">blue</span>, <span style="color: green;">green</span> <!--SR:!2025-03-30,46,130-->
- zinc ion:@:colorless <!--SR:!2030-07-03,2322,334-->
- manganese(II) ion:@:<span style="color: lightPink;">very pale pink</span> <!--SR:!2026-07-30,1000,250-->
- mercury(II) ion:@:_(n/a)_ <!--SR:!2028-01-30,1312,276-->
- cobalt(II) ion:@:<span style="color: pink;">pink</span> <!--SR:!2027-03-09,1101,239-->
- aluminium ion:@:colorless <!--SR:!2031-11-29,2704,334-->
- iron(III) ion:@:<span style="color: yellow; background-color: black;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated) <!--SR:!2026-10-30,786,190-->
- chromium(III) ion:@:<span style="color: green;">green</span> <!--SR:!2027-08-09,1347,258-->
- scandium(III) ion:@:colorless <!--SR:!2025-05-08,212,282-->
- titanium(III) ion:@:<span style="color: purple; background-color: white;">purple</span> <!--SR:!2025-04-07,42,130-->
- vanadium(II) ion:@:<span style="color: violet;">violet</span> <!--SR:!2025-03-01,23,130-->
- vanadium(III) ion:@:<span style="color: green;">green</span> <!--SR:!2025-05-20,203,190-->
- manganese(III) ion:@:<span style="color: red;">red</color> <!--SR:!2025-10-25,509,250-->

<!--/pytextgen-->

#### color–name (cation)

<!--pytextgen generate section="394a"--><!-- The following content is generated at 2024-01-28T09:35:10.023241+08:00. Any edits will be overridden! -->

- <span style="color: green;">green</span>:@:iron(II) ion, nickel(II) ion, copper(II) ion, chromium(III) ion, vanadium(III) ion <!--SR:!2025-04-04,46,130-->
- <span style="color: blue; background-color: white;">blue</span>:@:copper(II) ion <!--SR:!2025-08-06,553,281-->
- <span style="color: lightPink;">very pale pink</span>:@:manganese(II) ion <!--SR:!2025-03-30,513,321-->
- <span style="color: pink;">pink</span>:@:cobalt(II) ion <!--SR:!2025-09-01,317,241-->
- <span style="color: yellow; background-color: black;">yellow</span> (dilute):@:iron(III) ion <!--SR:!2027-09-13,1183,361-->
- <span style="color: brown; background-color: white;">brown</span> (concentrated):@:iron(III) ion <!--SR:!2029-01-31,1603,381-->
- <span style="color: purple; background-color: white;">purple</span>:@:titanium(III) ion <!--SR:!2025-08-06,473,242-->
- <span style="color: violet;">violet</span>:@:vanadium(II) ion <!--SR:!2025-10-27,314,242-->
- <span style="color: red;">red</color>:@:manganese(III) ion <!--SR:!2025-07-03,212,302-->

<!--/pytextgen-->

### anion

<!--pytextgen generate section="a9fdfe"--><!-- The following content is generated at 2024-02-17T20:40:56.159738+08:00. Any edits will be overridden! -->

> | name | symbol | charge | color |
> |-|-|-|-|
> | hydride ion | H<sup>-</sup> | 1- | colorless |
> | fluoride ion | F<sup>-</sup> | 1- | colorless |
> | chloride ion | Cl<sup>-</sup> | 1- | colorless |
> | bromide ion | Br<sup>-</sup> | 1- | colorless |
> | iodide ion | I<sup>-</sup> | 1- | colorless |
> | hydroxide ion | OH<sup>-</sup> | 1- | colorless |
> | nitrate ion | NO<sub>3</sub><sup>-</sup> | 1- | colorless |
> | nitrite ion | NO<sub>2</sub><sup>-</sup> | 1- | _(n/a)_ |
> | hydrogencarbonate ion | HCO<sub>3</sub><sup>-</sup> | 1- | colorless |
> | hydrogensulfite ion | HSO<sub>3</sub><sup>-</sup> | 1- | colorless |
> | hydrogensulfate ion | HSO<sub>4</sub><sup>-</sup> | 1- | colorless |
> | permanganate ion | MnO<sub>4</sub><sup>-</sup> | 1- | <span style="color: darkViolet; background-color: white;">deep purple</span> |
> | oxide ion | O<sup>2-</sup> | 2- | _(n/a)_ |
> | sulfide ion | S<sup>2-</sup> | 2- | _(n/a)_ |
> | sulfate ion | SO<sub>4</sub><sup>2-</sup> | 2- | colorless |
> | sulfite ion | SO<sub>3</sub><sup>2-</sup> | 2- | colorless |
> | carbonate ion | CO<sub>3</sub><sup>2-</sup> | 2- | colorless |
> | chromate ion | CrO<sub>4</sub><sup>2-</sup> | 2- | <span style="color: yellow; background-color: black;">yellow</span> |
> | dichromate ion | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> | 2- | <span style="color: orange;">orange</span> |
> | nitride ion | N<sup>3-</sup> | 3- | _(n/a)_ |
> | phosphate ion | PO<sub>4</sub><sup>3-</sup> | 3- | colorless |
> | manganate ion | MnO<sub>4</sub><sup>2-</sup> | 2- | <span style="color: green;">green</span> |

<!--/pytextgen-->

#### name–symbol (anion)

<!--pytextgen generate section="2fde12"--><!-- The following content is generated at 2024-01-04T20:17:52.102773+08:00. Any edits will be overridden! -->

- hydride ion::@::H<sup>-</sup> <!--SR:!2026-03-03,1183,354!2026-02-13,1171,356-->
- fluoride ion::@::F<sup>-</sup> <!--SR:!2029-12-03,2153,330!2027-06-07,1566,374-->
- chloride ion::@::Cl<sup>-</sup> <!--SR:!2027-07-27,1605,373!2025-11-03,1086,354-->
- bromide ion::@::Br<sup>-</sup> <!--SR:!2026-12-18,1232,273!2034-03-31,3323,314-->
- iodide ion::@::I<sup>-</sup> <!--SR:!2034-06-07,3478,352!2026-11-16,1294,313-->
- hydroxide ion::@::OH<sup>-</sup> <!--SR:!2026-10-24,1364,352!2026-01-30,1090,354-->
- nitrate ion::@::NO<sub>3</sub><sup>-</sup> <!--SR:!2028-09-18,1780,312!2027-05-30,1441,314-->
- nitrite ion::@::NO<sub>2</sub><sup>-</sup> <!--SR:!2025-08-01,710,259!2026-11-11,1286,310-->
- hydrogencarbonate ion::@::HCO<sub>3</sub><sup>-</sup> <!--SR:!2026-06-28,1170,299!2029-07-09,2040,332-->
- hydrogensulfite ion::@::HSO<sub>3</sub><sup>-</sup> <!--SR:!2028-02-10,1564,290!2027-04-29,1416,314-->
- hydrogensulfate ion::@::HSO<sub>4</sub><sup>-</sup> <!--SR:!2027-09-19,1641,367!2026-01-17,1128,350-->
- permanganate ion::@::MnO<sub>4</sub><sup>-</sup> <!--SR:!2027-09-07,1459,293!2026-09-01,1005,253-->
- oxide ion::@::O<sup>2-</sup> <!--SR:!2032-05-06,2826,330!2026-06-30,1200,313-->
- sulfide ion::@::S<sup>2-</sup> <!--SR:!2029-01-11,1794,287!2030-05-27,2286,330-->
- sulfate ion::@::SO<sub>4</sub><sup>2-</sup> <!--SR:!2030-11-15,2375,319!2025-10-13,1049,345-->
- sulfite ion::@::SO<sub>3</sub><sup>2-</sup> <!--SR:!2028-08-21,1757,313!2026-07-16,1061,274-->
- carbonate ion::@::CO<sub>3</sub><sup>2-</sup> <!--SR:!2029-09-29,1990,290!2029-10-30,2133,333-->
- chromate ion::@::CrO<sub>4</sub><sup>2-</sup> <!--SR:!2028-07-31,1651,278!2031-10-25,2674,333-->
- dichromate ion::@::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> <!--SR:!2028-08-20,1669,278!2029-05-12,1985,325-->
- nitride ion::@::N<sup>3-</sup> <!--SR:!2029-01-01,1786,287!2025-03-18,705,310-->
- phosphate ion::@::PO<sub>4</sub><sup>3-</sup> <!--SR:!2025-03-25,502,239!2031-02-25,2373,296-->
- manganate ion::@::MnO<sub>4</sub><sup>2-</sup> <!--SR:!2031-11-07,2529,402!2029-11-11,1921,382-->

<!--/pytextgen-->

#### name–charge (anion)

<!--pytextgen generate section="8c7820"--><!-- The following content is generated at 2024-01-04T20:17:51.950669+08:00. Any edits will be overridden! -->

- hydride ion:@:1- <!--SR:!2027-09-22,1543,319-->
- fluoride ion:@:1- <!--SR:!2025-04-20,869,292-->
- chloride ion:@:1- <!--SR:!2028-03-14,1789,374-->
- bromide ion:@:1- <!--SR:!2025-03-11,823,293-->
- iodide ion:@:1- <!--SR:!2027-03-29,1317,279-->
- hydroxide ion:@:1- <!--SR:!2026-10-01,1257,313-->
- nitrate ion:@:1- <!--SR:!2027-07-01,1176,270-->
- nitrite ion:@:1- <!--SR:!2028-08-11,1747,312-->
- hydrogencarbonate ion:@:1- <!--SR:!2028-08-20,1752,310-->
- hydrogensulfite ion:@:1- <!--SR:!2033-12-18,3288,339-->
- hydrogensulfate ion:@:1- <!--SR:!2025-08-28,863,284-->
- permanganate ion:@:1- <!--SR:!2025-03-12,226,250-->
- oxide ion:@:2- <!--SR:!2026-10-22,1271,310-->
- sulfide ion:@:2- <!--SR:!2028-04-19,1267,250-->
- sulfate ion:@:2- <!--SR:!2028-06-08,1688,310-->
- sulfite ion:@:2- <!--SR:!2030-04-12,1938,279-->
- carbonate ion:@:2- <!--SR:!2029-01-16,1801,290-->
- chromate ion:@:2- <!--SR:!2029-07-07,1759,279-->
- dichromate ion:@:2- <!--SR:!2026-12-30,1322,310-->
- nitride ion:@:3- <!--SR:!2027-01-20,1338,310-->
- phosphate ion:@:3- <!--SR:!2025-05-10,582,210-->
- manganate ion:@:2- <!--SR:!2027-08-06,1154,362-->

<!--/pytextgen-->

#### name–color (anion)

<!--pytextgen generate section="104852"--><!-- The following content is generated at 2024-01-28T09:35:10.058768+08:00. Any edits will be overridden! -->

- hydride ion:@:colorless <!--SR:!2027-07-23,1489,319-->
- fluoride ion:@:colorless <!--SR:!2029-11-11,2032,294-->
- chloride ion:@:colorless <!--SR:!2031-10-01,2656,334-->
- bromide ion:@:colorless <!--SR:!2027-04-07,1324,279-->
- iodide ion:@:colorless <!--SR:!2027-10-28,1427,307-->
- hydroxide ion:@:colorless <!--SR:!2029-02-26,1712,327-->
- nitrate ion:@:colorless <!--SR:!2027-09-23,1392,299-->
- nitrite ion:@:_(n/a)_ <!--SR:!2026-04-14,626,256-->
- hydrogencarbonate ion:@:colorless <!--SR:!2031-06-28,2573,330-->
- hydrogensulfite ion:@:colorless <!--SR:!2026-11-15,1203,270-->
- hydrogensulfate ion:@:colorless <!--SR:!2027-11-01,1341,270-->
- permanganate ion:@:<span style="color: darkViolet; background-color: white;">deep purple</span> <!--SR:!2026-01-28,496,230-->
- oxide ion:@:_(n/a)_ <!--SR:!2029-04-28,1684,296-->
- sulfide ion:@:_(n/a)_ <!--SR:!2025-04-24,452,256-->
- sulfate ion:@:colorless <!--SR:!2026-08-20,1076,274-->
- sulfite ion:@:colorless <!--SR:!2025-12-21,758,294-->
- carbonate ion:@:colorless <!--SR:!2030-08-15,2089,272-->
- chromate ion:@:<span style="color: yellow; background-color: black;">yellow</span> <!--SR:!2028-11-28,1416,250-->
- dichromate ion:@:<span style="color: orange;">orange</span> <!--SR:!2027-10-05,1481,293-->
- nitride ion:@:_(n/a)_ <!--SR:!2029-05-18,1599,276-->
- phosphate ion:@:colorless <!--SR:!2027-10-06,1482,293-->
- manganate ion:@:<span style="color: green;">green</span> <!--SR:!2025-05-11,306,282-->

<!--/pytextgen-->

#### color–name (anion)

<!--pytextgen generate section="50ad"--><!-- The following content is generated at 2024-01-28T09:35:10.075768+08:00. Any edits will be overridden! -->

- <span style="color: darkViolet; background-color: white;">deep purple</span>:@:permanganate ion <!--SR:!2028-06-21,1515,381-->
- <span style="color: yellow; background-color: black;">yellow</span>:@:chromate ion <!--SR:!2026-10-30,1008,361-->
- <span style="color: orange;">orange</span>:@:dichromate ion <!--SR:!2029-03-08,1723,381-->
- <span style="color: green;">green</span>:@:manganate ion <!--SR:!2025-06-23,215,222-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
