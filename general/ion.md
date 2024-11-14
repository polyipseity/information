---
aliases:
  - anion
  - anions
  - cation
  - cations
  - ion
  - ions
tags:
  - flashcard/active/general/ion
  - language/in/English
---

# ion

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

An __ion__ is an [atom](atom.md) or [molecule](molecule.md) with a net electrical charge. A {@{__cation__}@} is a {@{positively charged ion}@}, while an {@{__anion__}@} is a {@{negatively charged ion}@}.

A {@{simple ion}@} is an {@{ion formed from only one atom}@}, while a {@{polyatomic ion}@} is an {@{ion formed from more than one atom}@}.

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

- hydrogen ion::@::H<sup>+</sup>
- sodium ion::@::Na<sup>+</sup>
- potassium ion::@::K<sup>+</sup>
- copper(I) ion::@::Cu<sup>+</sup>
- silver ion::@::Ag<sup>+</sup>
- mercury(I) ion::@::Hg<sup>+</sup>
- ammonium ion::@::NH<sub>4</sub><sup>+</sup>
- magnesium ion::@::Mg<sup>2+</sup>
- calcium ion::@::Ca<sup>2+</sup>
- barium ion::@::Ba<sup>2+</sup>
- lead(II) ion::@::Pb<sup>2+</sup>
- iron(II) ion::@::Fe<sup>2+</sup>
- nickel(II) ion::@::Ni<sup>2+</sup>
- copper(II) ion::@::Cu<sup>2+</sup>
- zinc ion::@::Zn<sup>2+</sup>
- manganese(II) ion::@::Mn<sup>2+</sup>
- mercury(II) ion::@::Hg<sup>2+</sup>
- cobalt(II) ion::@::Co<sup>2+</sup>
- aluminium ion::@::Al<sup>3+</sup>
- iron(III) ion::@::Fe<sup>3+</sup>
- chromium(III) ion::@::Cr<sup>3+</sup>
- scandium(III) ion::@::Sc<sup>3+</sup>
- titanium(III) ion::@::Ti<sup>3+</sup>
- vanadium(II) ion::@::V<sup>2+</sup>
- vanadium(III) ion::@::V<sup>3+</sup>
- manganese(III) ion::@::Mn<sup>3+</sup>

<!--/pytextgen-->

#### name–charge (cation)

<!--pytextgen generate section="8d8dee"--><!-- The following content is generated at 2024-01-04T20:17:52.061211+08:00. Any edits will be overridden! -->

- hydrogen ion:@:1+
- sodium ion:@:1+
- potassium ion:@:1+
- copper(I) ion:@:1+
- silver ion:@:1+
- mercury(I) ion:@:1+
- ammonium ion:@:1+
- magnesium ion:@:2+
- calcium ion:@:2+
- barium ion:@:2+
- lead(II) ion:@:2+
- iron(II) ion:@:2+
- nickel(II) ion:@:2+
- copper(II) ion:@:2+
- zinc ion:@:2+
- manganese(II) ion:@:2+
- mercury(II) ion:@:2+
- cobalt(II) ion:@:2+
- aluminium ion:@:3+
- iron(III) ion:@:3+
- chromium(III) ion:@:3+
- scandium(III) ion:@:3+
- titanium(III) ion:@:3+
- vanadium(II) ion:@:2+
- vanadium(III) ion:@:3+
- manganese(III) ion:@:3+

<!--/pytextgen-->

#### name–color (cation)

<!--pytextgen generate section="a5defa"--><!-- The following content is generated at 2024-01-28T09:35:09.995261+08:00. Any edits will be overridden! -->

- hydrogen ion:@:colorless
- sodium ion:@:colorless
- potassium ion:@:colorless
- copper(I) ion:@:_(n/a)_
- silver ion:@:colorless
- mercury(I) ion:@:_(n/a)_
- ammonium ion:@:colorless
- magnesium ion:@:colorless
- calcium ion:@:colorless
- barium ion:@:colorless
- lead(II) ion:@:colorless
- iron(II) ion:@:<span style="color: green;">green</span>
- nickel(II) ion:@:<span style="color: green;">green</span>
- copper(II) ion:@:<span style="color: blue; background-color: white;">blue</span>, <span style="color: green;">green</span>
- zinc ion:@:colorless
- manganese(II) ion:@:<span style="color: lightPink;">very pale pink</span>
- mercury(II) ion:@:_(n/a)_
- cobalt(II) ion:@:<span style="color: pink;">pink</span>
- aluminium ion:@:colorless
- iron(III) ion:@:<span style="color: yellow; background-color: black;">yellow</span> (dilute), <span style="color: brown; background-color: white;">brown</span> (concentrated)
- chromium(III) ion:@:<span style="color: green;">green</span>
- scandium(III) ion:@:colorless
- titanium(III) ion:@:<span style="color: purple; background-color: white;">purple</span>
- vanadium(II) ion:@:<span style="color: violet;">violet</span>
- vanadium(III) ion:@:<span style="color: green;">green</span>
- manganese(III) ion:@:<span style="color: red;">red</color>

<!--/pytextgen-->

#### color–name (cation)

<!--pytextgen generate section="394a"--><!-- The following content is generated at 2024-01-28T09:35:10.023241+08:00. Any edits will be overridden! -->

- <span style="color: green;">green</span>:@:iron(II) ion, nickel(II) ion, copper(II) ion, chromium(III) ion, vanadium(III) ion
- <span style="color: blue; background-color: white;">blue</span>:@:copper(II) ion
- <span style="color: lightPink;">very pale pink</span>:@:manganese(II) ion
- <span style="color: pink;">pink</span>:@:cobalt(II) ion
- <span style="color: yellow; background-color: black;">yellow</span> (dilute):@:iron(III) ion
- <span style="color: brown; background-color: white;">brown</span> (concentrated):@:iron(III) ion
- <span style="color: purple; background-color: white;">purple</span>:@:titanium(III) ion
- <span style="color: violet;">violet</span>:@:vanadium(II) ion
- <span style="color: red;">red</color>:@:manganese(III) ion

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

- hydride ion::@::H<sup>-</sup>
- fluoride ion::@::F<sup>-</sup>
- chloride ion::@::Cl<sup>-</sup>
- bromide ion::@::Br<sup>-</sup>
- iodide ion::@::I<sup>-</sup>
- hydroxide ion::@::OH<sup>-</sup>
- nitrate ion::@::NO<sub>3</sub><sup>-</sup>
- nitrite ion::@::NO<sub>2</sub><sup>-</sup>
- hydrogencarbonate ion::@::HCO<sub>3</sub><sup>-</sup>
- hydrogensulfite ion::@::HSO<sub>3</sub><sup>-</sup>
- hydrogensulfate ion::@::HSO<sub>4</sub><sup>-</sup>
- permanganate ion::@::MnO<sub>4</sub><sup>-</sup>
- oxide ion::@::O<sup>2-</sup>
- sulfide ion::@::S<sup>2-</sup>
- sulfate ion::@::SO<sub>4</sub><sup>2-</sup>
- sulfite ion::@::SO<sub>3</sub><sup>2-</sup>
- carbonate ion::@::CO<sub>3</sub><sup>2-</sup>
- chromate ion::@::CrO<sub>4</sub><sup>2-</sup>
- dichromate ion::@::Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>
- nitride ion::@::N<sup>3-</sup>
- phosphate ion::@::PO<sub>4</sub><sup>3-</sup>
- manganate ion::@::MnO<sub>4</sub><sup>2-</sup>

<!--/pytextgen-->

#### name–charge (anion)

<!--pytextgen generate section="8c7820"--><!-- The following content is generated at 2024-01-04T20:17:51.950669+08:00. Any edits will be overridden! -->

- hydride ion:@:1-
- fluoride ion:@:1-
- chloride ion:@:1-
- bromide ion:@:1-
- iodide ion:@:1-
- hydroxide ion:@:1-
- nitrate ion:@:1-
- nitrite ion:@:1-
- hydrogencarbonate ion:@:1-
- hydrogensulfite ion:@:1-
- hydrogensulfate ion:@:1-
- permanganate ion:@:1-
- oxide ion:@:2-
- sulfide ion:@:2-
- sulfate ion:@:2-
- sulfite ion:@:2-
- carbonate ion:@:2-
- chromate ion:@:2-
- dichromate ion:@:2-
- nitride ion:@:3-
- phosphate ion:@:3-
- manganate ion:@:2-

<!--/pytextgen-->

#### name–color (anion)

<!--pytextgen generate section="104852"--><!-- The following content is generated at 2024-01-28T09:35:10.058768+08:00. Any edits will be overridden! -->

- hydride ion:@:colorless
- fluoride ion:@:colorless
- chloride ion:@:colorless
- bromide ion:@:colorless
- iodide ion:@:colorless
- hydroxide ion:@:colorless
- nitrate ion:@:colorless
- nitrite ion:@:_(n/a)_
- hydrogencarbonate ion:@:colorless
- hydrogensulfite ion:@:colorless
- hydrogensulfate ion:@:colorless
- permanganate ion:@:<span style="color: darkViolet; background-color: white;">deep purple</span>
- oxide ion:@:_(n/a)_
- sulfide ion:@:_(n/a)_
- sulfate ion:@:colorless
- sulfite ion:@:colorless
- carbonate ion:@:colorless
- chromate ion:@:<span style="color: yellow; background-color: black;">yellow</span>
- dichromate ion:@:<span style="color: orange;">orange</span>
- nitride ion:@:_(n/a)_
- phosphate ion:@:colorless
- manganate ion:@:<span style="color: green;">green</span>

<!--/pytextgen-->

#### color–name (anion)

<!--pytextgen generate section="50ad"--><!-- The following content is generated at 2024-01-28T09:35:10.075768+08:00. Any edits will be overridden! -->

- <span style="color: darkViolet; background-color: white;">deep purple</span>:@:permanganate ion
- <span style="color: yellow; background-color: black;">yellow</span>:@:chromate ion
- <span style="color: orange;">orange</span>:@:dichromate ion
- <span style="color: green;">green</span>:@:manganate ion

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
