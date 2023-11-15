---
aliases:
  - anion
  - anions
  - cation
  - cations
  - ion
  - ions
tags:
  - flashcards/general/ion
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# ion

An __ion__ is an [atom](atom.md) or [molecule](molecule.md) with a net electrical charge. A {{__cation__}} is a {{positively charged ion}}, while an {{__anion__}} is a {{negatively charged ion}}.<!--SR:!2027-01-19,1447,365!2027-11-08,1684,370!2026-07-20,1290,352!2027-05-12,1546,374-->

A {{simple ion}} is an {{ion formed from only one atom}}, while a {{polyatomic ion}} is an {{ion formed from more than one atom}}. <!--SR:!2026-03-02,1102,307!2028-03-17,1789,372!2024-05-12,539,267!2025-04-11,857,334-->

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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
YELLOW = '<span style="color: yellow;">yellow</span>'

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
          names=('name', 'symbol', 'charage', 'color'),
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
e = __env__
return chain.from_iterable(await gather(
  cation_sect.memorize(
    (
      e.cwf_sect('d9192d'),
      e.cwf_sect('3928fd'),
      e.cwf_sect('8d8dee'),
      e.cwf_sect('a5defa'),
      e.cwf_sect('394a'),
    ),
  ),
  anion_sect.memorize(
    (
      e.cwf_sect('a9fdfe'),
      e.cwf_sect('2fde12'),
      e.cwf_sect('8c7820'),
      e.cwf_sect('104852'),
      e.cwf_sect('50ad'),
    ),
  ),
))
```
%%

### cation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d9192d"--><!-- The following content is generated at 2023-04-08T14:17:08.431600+08:00. Any edits will be overridden! -->

> | name | symbol | charage | color |
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
> | iron(III) ion | Fe<sup>3+</sup> | 3+ | <span style="color: yellow;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated) |
> | chromium(III) ion | Cr<sup>3+</sup> | 3+ | <span style="color: green;">green</span> |
> | scandium(III) ion | Sc<sup>3+</sup> | 3+ | colorless |
> | titanium(III) ion | Ti<sup>3+</sup> | 3+ | <span style="color: purple; background-color: white;">purple</span> |
> | vanadium(II) ion | V<sup>2+</sup> | 2+ | <span style="color: violet;">violet</span> |
> | vanadium(III) ion | V<sup>3+</sup> | 3+ | <span style="color: green;">green</span> |
> | manganese(III) ion | Mn<sup>3+</sup> | 3+ | <span style="color: red;">red</color> |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3928fd"--><!-- The following content is generated at 2023-04-08T14:17:08.477476+08:00. Any edits will be overridden! -->

1. hydrogen ion:::H<sup>+</sup> <!--SR:!2025-05-22,945,332!2025-07-11,927,339-->
2. sodium ion:::Na<sup>+</sup> <!--SR:!2027-03-03,1486,370!2027-09-21,1649,373-->
3. potassium ion:::K<sup>+</sup> <!--SR:!2027-10-09,1647,359!2028-03-04,1780,373-->
4. copper(I) ion:::Cu<sup>+</sup> <!--SR:!2027-02-02,1451,359!2024-01-31,376,310-->
5. silver ion:::Ag<sup>+</sup> <!--SR:!2026-05-27,1086,290!2025-06-25,897,336-->
6. mercury(I) ion:::Hg<sup>+</sup> <!--SR:!2027-09-08,1632,367!2026-09-15,1300,330-->
7. ammonium ion:::NH<sub>4</sub><sup>+</sup> <!--SR:!2024-08-17,519,270!2027-01-08,1335,313-->
8. magnesium ion:::Mg<sup>2+</sup> <!--SR:!2024-03-08,336,247!2024-02-04,523,316-->
9. calcium ion:::Ca<sup>2+</sup> <!--SR:!2027-08-21,1621,370!2028-01-19,1745,374-->
10. barium ion:::Ba<sup>2+</sup> <!--SR:!2025-06-02,665,250!2025-02-15,770,294-->
11. lead(II) ion:::Pb<sup>2+</sup> <!--SR:!2027-06-06,1566,374!2024-02-24,536,314-->
12. iron(II) ion:::Fe<sup>2+</sup> <!--SR:!2026-11-28,1400,359!2027-10-18,1661,365-->
13. nickel(II) ion:::Ni<sup>2+</sup> <!--SR:!2027-06-25,1563,359!2028-07-06,1716,310-->
14. copper(II) ion:::Cu<sup>2+</sup> <!--SR:!2027-04-27,1526,367!2024-09-24,705,334-->
15. zinc ion:::Zn<sup>2+</sup> <!--SR:!2024-07-29,595,273!2025-02-21,653,273-->
16. manganese(II) ion:::Mn<sup>2+</sup> <!--SR:!2024-05-09,441,270!2024-01-08,445,253-->
17. mercury(II) ion:::Hg<sup>2+</sup> <!--SR:!2026-03-20,1192,350!2025-11-01,1038,313-->
18. cobalt(II) ion:::Co<sup>2+</sup> <!--SR:!2027-04-28,1527,367!2025-04-30,820,294-->
19. aluminium ion:::Al<sup>3+</sup> <!--SR:!2027-07-03,1372,272!2024-07-03,622,314-->
20. iron(III) ion:::Fe<sup>3+</sup> <!--SR:!2027-04-21,1525,370!2026-10-29,1391,374-->
21. chromium(III) ion:::Cr<sup>3+</sup> <!--SR:!2028-01-18,1745,374!2026-02-20,1123,314-->
22. scandium(III) ion:::Sc<sup>3+</sup> <!--SR:!2024-09-26,427,382!2024-11-29,480,382-->
23. titanium(III) ion:::Ti<sup>3+</sup> <!--SR:!2024-09-19,422,382!2024-11-26,477,382-->
24. vanadium(II) ion:::V<sup>2+</sup> <!--SR:!2024-11-07,463,382!2024-12-10,489,382-->
25. vanadium(III) ion:::V<sup>3+</sup> <!--SR:!2024-11-10,464,382!2024-10-28,455,382-->
26. manganese(III) ion:::Mn<sup>3+</sup> <!--SR:!2024-10-19,449,382!2024-11-27,478,382-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8d8dee"--><!-- The following content is generated at 2023-04-08T14:17:08.448555+08:00. Any edits will be overridden! -->

1. hydrogen ion::1+ <!--SR:!2027-04-14,1522,373-->
2. sodium ion::1+ <!--SR:!2024-02-08,522,310-->
3. potassium ion::1+ <!--SR:!2028-04-05,1699,312-->
4. copper(I) ion::1+ <!--SR:!2028-03-23,1794,372-->
5. silver ion::1+ <!--SR:!2028-01-13,1541,290-->
6. mercury(I) ion::1+ <!--SR:!2027-08-31,1634,374-->
7. ammonium ion::1+ <!--SR:!2024-01-21,509,314-->
8. magnesium ion::2+ <!--SR:!2026-12-17,1231,273-->
9. calcium ion::2+ <!--SR:!2024-10-25,649,272-->
10. barium ion::2+ <!--SR:!2024-01-27,456,254-->
11. lead(II) ion::2+ <!--SR:!2026-06-13,1266,358-->
12. iron(II) ion::2+ <!--SR:!2028-04-27,1823,373-->
13. nickel(II) ion::2+ <!--SR:!2026-08-31,1322,352-->
14. copper(II) ion::2+ <!--SR:!2026-05-28,1176,352-->
15. zinc ion::2+ <!--SR:!2025-04-30,628,244-->
16. manganese(II) ion::2+ <!--SR:!2026-10-23,1379,367-->
17. mercury(II) ion::2+ <!--SR:!2027-06-01,1561,374-->
18. cobalt(II) ion::2+ <!--SR:!2027-04-15,1523,372-->
19. aluminium ion::3+ <!--SR:!2024-01-14,507,312-->
20. iron(III) ion::3+ <!--SR:!2026-09-16,1348,365-->
21. chromium(III) ion::3+ <!--SR:!2026-11-24,1396,358-->
22. scandium(III) ion::3+ <!--SR:!2024-10-29,456,382-->
23. titanium(III) ion::3+ <!--SR:!2024-10-27,454,382-->
24. vanadium(II) ion::2+ <!--SR:!2024-11-03,460,382-->
25. vanadium(III) ion::3+ <!--SR:!2024-11-09,463,382-->
26. manganese(III) ion::3+ <!--SR:!2024-11-30,481,382-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a5defa"--><!-- The following content is generated at 2023-04-08T14:17:08.464511+08:00. Any edits will be overridden! -->

1. hydrogen ion::colorless <!--SR:!2024-02-05,519,309-->
2. sodium ion::colorless <!--SR:!2025-11-02,919,293-->
3. potassium ion::colorless <!--SR:!2023-12-14,479,304-->
4. copper(I) ion::_(n/a)_ <!--SR:!2024-07-07,392,276-->
5. silver ion::colorless <!--SR:!2027-03-01,1295,279-->
6. mercury(I) ion::_(n/a)_ <!--SR:!2024-05-30,368,276-->
7. ammonium ion::colorless <!--SR:!2026-05-12,1149,339-->
8. magnesium ion::colorless <!--SR:!2024-11-07,660,274-->
9. calcium ion::colorless <!--SR:!2024-03-02,499,272-->
10. barium ion::colorless <!--SR:!2024-09-20,630,274-->
11. lead(II) ion::colorless <!--SR:!2024-12-02,597,253-->
12. iron(II) ion::<span style="color: green;">green</span> <!--SR:!2024-03-06,484,254-->
13. nickel(II) ion::<span style="color: green;">green</span> <!--SR:!2024-01-28,205,207-->
14. copper(II) ion::<span style="color: blue; background-color: white;">blue</span>, <span style="color: green;">green</span> <!--SR:!2024-01-03,55,130-->
15. zinc ion::colorless <!--SR:!2024-02-23,535,314-->
16. manganese(II) ion::<span style="color: lightPink;">very pale pink</span> <!--SR:!2026-07-30,1000,250-->
17. mercury(II) ion::_(n/a)_ <!--SR:!2024-06-27,366,256-->
18. cobalt(II) ion::<span style="color: pink;">pink</span> <!--SR:!2024-03-03,461,239-->
19. aluminium ion::colorless <!--SR:!2024-07-04,623,314-->
20. iron(III) ion::<span style="color: yellow;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated) <!--SR:!2024-09-04,414,190-->
21. chromium(III) ion::<span style="color: green;">green</span> <!--SR:!2023-11-29,402,238-->
22. scandium(III) ion::colorless <!--SR:!2023-12-07,171,322-->
23. titanium(III) ion::<span style="color: purple; background-color: white;">purple</span> <!--SR:!2023-12-11,26,170-->
24. vanadium(II) ion::<span style="color: violet;">violet</span> <!--SR:!2023-11-30,17,202-->
25. vanadium(III) ion::<span style="color: green;">green</span> <!--SR:!2023-11-27,24,202-->
26. manganese(III) ion::<span style="color: red;">red</color> <!--SR:!2023-12-29,53,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### color–name

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="394a"--><!-- The following content is generated at 2023-04-08T13:40:47.993725+08:00. Any edits will be overridden! -->

1. <span style="color: green;">green</span>::iron(II) ion, nickel(II) ion, copper(II) ion, chromium(III) ion, vanadium(III) ion <!--SR:!2023-12-01,129,221-->
2. <span style="color: blue; background-color: white;">blue</span>::copper(II) ion <!--SR:!2024-01-31,197,281-->
3. <span style="color: lightPink;">very pale pink</span>::manganese(II) ion <!--SR:!2025-03-30,513,321-->
4. <span style="color: pink;">pink</span>::cobalt(II) ion <!--SR:!2024-06-15,253,261-->
5. <span style="color: yellow;">yellow</span> (dilute)::iron(III) ion <!--SR:!2024-06-17,328,361-->
6. <span style="color: brown; background-color: white;">brown</span> (concentrated)::iron(III) ion <!--SR:!2024-09-11,421,381-->
7. <span style="color: purple; background-color: white;">purple</span>::titanium(III) ion <!--SR:!2024-04-20,196,242-->
8. <span style="color: violet;">violet</span>::vanadium(II) ion <!--SR:!2024-03-04,217,282-->
9. <span style="color: red;">red</color>::manganese(III) ion <!--SR:!2024-12-03,423,322-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### anion

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9fdfe"--><!-- The following content is generated at 2023-04-08T13:39:40.674419+08:00. Any edits will be overridden! -->

> | name | symbol | charage | color |
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
> | chromate ion | CrO<sub>4</sub><sup>2-</sup> | 2- | <span style="color: yellow;">yellow</span> |
> | dichromate ion | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> | 2- | <span style="color: orange;">orange</span> |
> | nitride ion | N<sup>3-</sup> | 3- | _(n/a)_ |
> | phosphate ion | PO<sub>4</sub><sup>3-</sup> | 3- | colorless |
> | manganate ion | MnO<sub>4</sub><sup>2-</sup> | 2- | <span style="color: green;">green</span> |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2fde12"--><!-- The following content is generated at 2023-04-08T13:39:40.602610+08:00. Any edits will be overridden! -->

1. hydride ion:::H<sup>-</sup> <!--SR:!2026-03-03,1183,354!2026-02-13,1171,356-->
2. fluoride ion:::F<sup>-</sup> <!--SR:!2024-01-09,502,310!2027-06-07,1566,374-->
3. chloride ion:::Cl<sup>-</sup> <!--SR:!2027-07-27,1605,373!2025-11-03,1086,354-->
4. bromide ion:::Br<sup>-</sup> <!--SR:!2026-12-18,1232,273!2025-02-23,814,294-->
5. iodide ion:::I<sup>-</sup> <!--SR:!2024-11-28,760,332!2026-11-16,1294,313-->
6. hydroxide ion:::OH<sup>-</sup> <!--SR:!2026-10-24,1364,352!2026-01-30,1090,354-->
7. nitrate ion:::NO<sub>3</sub><sup>-</sup> <!--SR:!2028-09-18,1780,312!2027-05-30,1441,314-->
8. nitrite ion:::NO<sub>2</sub><sup>-</sup> <!--SR:!2025-08-01,710,259!2026-11-11,1286,310-->
9. hydrogencarbonate ion:::HCO<sub>3</sub><sup>-</sup> <!--SR:!2026-06-28,1170,299!2023-12-08,473,312-->
10. hydrogensulfite ion:::HSO<sub>3</sub><sup>-</sup> <!--SR:!2028-02-10,1564,290!2027-04-29,1416,314-->
11. hydrogensulfate ion:::HSO<sub>4</sub><sup>-</sup> <!--SR:!2027-09-19,1641,367!2026-01-17,1128,350-->
12. permanganate ion:::MnO<sub>4</sub><sup>-</sup> <!--SR:!2027-09-07,1459,293!2023-12-01,306,233-->
13. oxide ion:::O<sup>2-</sup> <!--SR:!2024-08-09,659,310!2026-06-30,1200,313-->
14. sulfide ion:::S<sup>2-</sup> <!--SR:!2024-02-13,481,267!2024-02-22,533,310-->
15. sulfate ion:::SO<sub>4</sub><sup>2-</sup> <!--SR:!2024-05-15,573,299!2025-10-13,1049,345-->
16. sulfite ion:::SO<sub>3</sub><sup>2-</sup> <!--SR:!2028-08-21,1757,313!2026-07-16,1061,274-->
17. carbonate ion:::CO<sub>3</sub><sup>2-</sup> <!--SR:!2024-04-18,528,270!2023-12-28,493,313-->
18. chromate ion:::CrO<sub>4</sub><sup>2-</sup> <!--SR:!2024-01-20,457,258!2024-06-29,618,313-->
19. dichromate ion:::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> <!--SR:!2024-01-25,462,258!2023-12-05,470,305-->
20. nitride ion:::N<sup>3-</sup> <!--SR:!2024-02-11,479,267!2025-03-18,705,310-->
21. phosphate ion:::PO<sub>4</sub><sup>3-</sup> <!--SR:!2025-03-25,502,239!2024-08-25,617,276-->
22. manganate ion:::MnO<sub>4</sub><sup>2-</sup> <!--SR:!2024-12-04,484,382!2024-08-08,387,362-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8c7820"--><!-- The following content is generated at 2023-04-08T13:39:40.618568+08:00. Any edits will be overridden! -->

1. hydride ion::1- <!--SR:!2027-09-22,1543,319-->
2. fluoride ion::1- <!--SR:!2025-04-20,869,292-->
3. chloride ion::1- <!--SR:!2028-03-14,1789,374-->
4. bromide ion::1- <!--SR:!2025-03-11,823,293-->
5. iodide ion::1- <!--SR:!2027-03-29,1317,279-->
6. hydroxide ion::1- <!--SR:!2026-10-01,1257,313-->
7. nitrate ion::1- <!--SR:!2024-04-11,436,270-->
8. nitrite ion::1- <!--SR:!2028-08-11,1747,312-->
9. hydrogencarbonate ion::1- <!--SR:!2028-08-20,1752,310-->
10. hydrogensulfite ion::1- <!--SR:!2024-12-16,746,319-->
11. hydrogensulfate ion::1- <!--SR:!2025-08-28,863,284-->
12. permanganate ion::1- <!--SR:!2024-07-29,453,270-->
13. oxide ion::2- <!--SR:!2026-10-22,1271,310-->
14. sulfide ion::2- <!--SR:!2024-10-30,507,250-->
15. sulfate ion::2- <!--SR:!2028-06-08,1688,310-->
16. sulfite ion::2- <!--SR:!2024-12-20,695,279-->
17. carbonate ion::2- <!--SR:!2024-02-10,478,270-->
18. chromate ion::2- <!--SR:!2024-09-12,631,279-->
19. dichromate ion::2- <!--SR:!2026-12-30,1322,310-->
20. nitride ion::3- <!--SR:!2027-01-20,1338,310-->
21. phosphate ion::3- <!--SR:!2025-05-10,582,210-->
22. manganate ion::2- <!--SR:!2024-06-08,319,362-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="104852"--><!-- The following content is generated at 2023-04-08T13:39:40.653475+08:00. Any edits will be overridden! -->

1. hydride ion::colorless <!--SR:!2027-07-23,1489,319-->
2. fluoride ion::colorless <!--SR:!2024-04-19,532,274-->
3. chloride ion::colorless <!--SR:!2024-06-23,612,314-->
4. bromide ion::colorless <!--SR:!2027-04-07,1324,279-->
5. iodide ion::colorless <!--SR:!2023-11-30,465,307-->
6. hydroxide ion::colorless <!--SR:!2024-06-20,403,307-->
7. nitrate ion::colorless <!--SR:!2023-12-01,466,299-->
8. nitrite ion::_(n/a)_ <!--SR:!2023-11-19,96,256-->
9. hydrogencarbonate ion::colorless <!--SR:!2024-06-11,600,310-->
10. hydrogensulfite ion::colorless <!--SR:!2026-11-15,1203,270-->
11. hydrogensulfate ion::colorless <!--SR:!2024-02-29,497,270-->
12. permanganate ion::<span style="color: darkViolet; background-color: white;">deep purple</span> <!--SR:!2024-02-16,434,250-->
13. oxide ion::_(n/a)_ <!--SR:!2024-09-17,438,276-->
14. sulfide ion::_(n/a)_ <!--SR:!2024-01-28,177,256-->
15. sulfate ion::colorless <!--SR:!2026-08-20,1076,274-->
16. sulfite ion::colorless <!--SR:!2023-11-19,198,274-->
17. carbonate ion::colorless <!--SR:!2024-11-25,591,252-->
18. chromate ion::<span style="color: yellow;">yellow</span> <!--SR:!2025-01-11,566,250-->
19. dichromate ion::<span style="color: orange;">orange</span> <!--SR:!2027-10-05,1481,293-->
20. nitride ion::_(n/a)_ <!--SR:!2024-12-31,444,256-->
21. phosphate ion::colorless <!--SR:!2027-10-06,1482,293-->
22. manganate ion::<span style="color: green;">green</span> <!--SR:!2023-11-22,163,322-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### color–name

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50ad"--><!-- The following content is generated at 2023-04-08T13:39:40.573688+08:00. Any edits will be overridden! -->

1. <span style="color: darkViolet; background-color: white;">deep purple</span>::permanganate ion <!--SR:!2024-04-28,306,361-->
2. <span style="color: yellow;">yellow</span>::chromate ion <!--SR:!2024-01-26,215,341-->
3. <span style="color: orange;">orange</span>::dichromate ion <!--SR:!2024-06-19,348,361-->
4. <span style="color: green;">green</span>::manganate ion <!--SR:!2024-02-07,171,282-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
