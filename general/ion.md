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
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# ion

An __ion__ is an [atom](atom.md) or [molecule](molecule.md) with a net electrical charge. A {{__cation__}} is a {{positively charged ion}}, while an {{__anion__}} is a {{negatively charged ion}}.

A {{simple ion}} is an {{ion formed from only one atom}}, while a {{polyatomic ion}} is an {{ion formed from more than one atom}}.

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

1. hydrogen ion:::H<sup>+</sup>
2. sodium ion:::Na<sup>+</sup>
3. potassium ion:::K<sup>+</sup>
4. copper(I) ion:::Cu<sup>+</sup>
5. silver ion:::Ag<sup>+</sup>
6. mercury(I) ion:::Hg<sup>+</sup>
7. ammonium ion:::NH<sub>4</sub><sup>+</sup>
8. magnesium ion:::Mg<sup>2+</sup>
9. calcium ion:::Ca<sup>2+</sup>
10. barium ion:::Ba<sup>2+</sup>
11. lead(II) ion:::Pb<sup>2+</sup>
12. iron(II) ion:::Fe<sup>2+</sup>
13. nickel(II) ion:::Ni<sup>2+</sup>
14. copper(II) ion:::Cu<sup>2+</sup>
15. zinc ion:::Zn<sup>2+</sup>
16. manganese(II) ion:::Mn<sup>2+</sup>
17. mercury(II) ion:::Hg<sup>2+</sup>
18. cobalt(II) ion:::Co<sup>2+</sup>
19. aluminium ion:::Al<sup>3+</sup>
20. iron(III) ion:::Fe<sup>3+</sup>
21. chromium(III) ion:::Cr<sup>3+</sup>
22. scandium(III) ion:::Sc<sup>3+</sup>
23. titanium(III) ion:::Ti<sup>3+</sup>
24. vanadium(II) ion:::V<sup>2+</sup>
25. vanadium(III) ion:::V<sup>3+</sup>
26. manganese(III) ion:::Mn<sup>3+</sup>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8d8dee"--><!-- The following content is generated at 2023-04-08T14:17:08.448555+08:00. Any edits will be overridden! -->

1. hydrogen ion::1+
2. sodium ion::1+
3. potassium ion::1+
4. copper(I) ion::1+
5. silver ion::1+
6. mercury(I) ion::1+
7. ammonium ion::1+
8. magnesium ion::2+
9. calcium ion::2+
10. barium ion::2+
11. lead(II) ion::2+
12. iron(II) ion::2+
13. nickel(II) ion::2+
14. copper(II) ion::2+
15. zinc ion::2+
16. manganese(II) ion::2+
17. mercury(II) ion::2+
18. cobalt(II) ion::2+
19. aluminium ion::3+
20. iron(III) ion::3+
21. chromium(III) ion::3+
22. scandium(III) ion::3+
23. titanium(III) ion::3+
24. vanadium(II) ion::2+
25. vanadium(III) ion::3+
26. manganese(III) ion::3+

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a5defa"--><!-- The following content is generated at 2023-04-08T14:17:08.464511+08:00. Any edits will be overridden! -->

1. hydrogen ion::colorless
2. sodium ion::colorless
3. potassium ion::colorless
4. copper(I) ion::_(n/a)_
5. silver ion::colorless
6. mercury(I) ion::_(n/a)_
7. ammonium ion::colorless
8. magnesium ion::colorless
9. calcium ion::colorless
10. barium ion::colorless
11. lead(II) ion::colorless
12. iron(II) ion::<span style="color: green;">green</span>
13. nickel(II) ion::<span style="color: green;">green</span>
14. copper(II) ion::<span style="color: blue; background-color: white;">blue</span>, <span style="color: green;">green</span>
15. zinc ion::colorless
16. manganese(II) ion::<span style="color: lightPink;">very pale pink</span>
17. mercury(II) ion::_(n/a)_
18. cobalt(II) ion::<span style="color: pink;">pink</span>
19. aluminium ion::colorless
20. iron(III) ion::<span style="color: yellow;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated)
21. chromium(III) ion::<span style="color: green;">green</span>
22. scandium(III) ion::colorless
23. titanium(III) ion::<span style="color: purple; background-color: white;">purple</span>
24. vanadium(II) ion::<span style="color: violet;">violet</span>
25. vanadium(III) ion::<span style="color: green;">green</span>
26. manganese(III) ion::<span style="color: red;">red</color>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### color–name

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="394a"--><!-- The following content is generated at 2023-04-08T13:40:47.993725+08:00. Any edits will be overridden! -->

1. <span style="color: green;">green</span>::iron(II) ion, nickel(II) ion, copper(II) ion, chromium(III) ion, vanadium(III) ion
2. <span style="color: blue; background-color: white;">blue</span>::copper(II) ion
3. <span style="color: lightPink;">very pale pink</span>::manganese(II) ion
4. <span style="color: pink;">pink</span>::cobalt(II) ion
5. <span style="color: yellow;">yellow</span> (dilute)::iron(III) ion
6. <span style="color: brown; background-color: white;">brown</span> (concentrated)::iron(III) ion
7. <span style="color: purple; background-color: white;">purple</span>::titanium(III) ion
8. <span style="color: violet;">violet</span>::vanadium(II) ion
9. <span style="color: red;">red</color>::manganese(III) ion

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

1. hydride ion:::H<sup>-</sup>
2. fluoride ion:::F<sup>-</sup>
3. chloride ion:::Cl<sup>-</sup>
4. bromide ion:::Br<sup>-</sup>
5. iodide ion:::I<sup>-</sup>
6. hydroxide ion:::OH<sup>-</sup>
7. nitrate ion:::NO<sub>3</sub><sup>-</sup>
8. nitrite ion:::NO<sub>2</sub><sup>-</sup>
9. hydrogencarbonate ion:::HCO<sub>3</sub><sup>-</sup>
10. hydrogensulfite ion:::HSO<sub>3</sub><sup>-</sup>
11. hydrogensulfate ion:::HSO<sub>4</sub><sup>-</sup>
12. permanganate ion:::MnO<sub>4</sub><sup>-</sup>
13. oxide ion:::O<sup>2-</sup>
14. sulfide ion:::S<sup>2-</sup>
15. sulfate ion:::SO<sub>4</sub><sup>2-</sup>
16. sulfite ion:::SO<sub>3</sub><sup>2-</sup>
17. carbonate ion:::CO<sub>3</sub><sup>2-</sup>
18. chromate ion:::CrO<sub>4</sub><sup>2-</sup>
19. dichromate ion:::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>
20. nitride ion:::N<sup>3-</sup>
21. phosphate ion:::PO<sub>4</sub><sup>3-</sup>
22. manganate ion:::MnO<sub>4</sub><sup>2-</sup>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–charge

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8c7820"--><!-- The following content is generated at 2023-04-08T13:39:40.618568+08:00. Any edits will be overridden! -->

1. hydride ion::1-
2. fluoride ion::1-
3. chloride ion::1-
4. bromide ion::1-
5. iodide ion::1-
6. hydroxide ion::1-
7. nitrate ion::1-
8. nitrite ion::1-
9. hydrogencarbonate ion::1-
10. hydrogensulfite ion::1-
11. hydrogensulfate ion::1-
12. permanganate ion::1-
13. oxide ion::2-
14. sulfide ion::2-
15. sulfate ion::2-
16. sulfite ion::2-
17. carbonate ion::2-
18. chromate ion::2-
19. dichromate ion::2-
20. nitride ion::3-
21. phosphate ion::3-
22. manganate ion::2-

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–color

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="104852"--><!-- The following content is generated at 2023-04-08T13:39:40.653475+08:00. Any edits will be overridden! -->

1. hydride ion::colorless
2. fluoride ion::colorless
3. chloride ion::colorless
4. bromide ion::colorless
5. iodide ion::colorless
6. hydroxide ion::colorless
7. nitrate ion::colorless
8. nitrite ion::_(n/a)_
9. hydrogencarbonate ion::colorless
10. hydrogensulfite ion::colorless
11. hydrogensulfate ion::colorless
12. permanganate ion::<span style="color: darkViolet; background-color: white;">deep purple</span>
13. oxide ion::_(n/a)_
14. sulfide ion::_(n/a)_
15. sulfate ion::colorless
16. sulfite ion::colorless
17. carbonate ion::colorless
18. chromate ion::<span style="color: yellow;">yellow</span>
19. dichromate ion::<span style="color: orange;">orange</span>
20. nitride ion::_(n/a)_
21. phosphate ion::colorless
22. manganate ion::<span style="color: green;">green</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### color–name

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50ad"--><!-- The following content is generated at 2023-04-08T13:39:40.573688+08:00. Any edits will be overridden! -->

1. <span style="color: darkViolet; background-color: white;">deep purple</span>::permanganate ion
2. <span style="color: yellow;">yellow</span>::chromate ion
3. <span style="color: orange;">orange</span>::dichromate ion
4. <span style="color: green;">green</span>::manganate ion

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
