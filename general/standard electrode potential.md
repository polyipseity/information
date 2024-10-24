---
aliases:
  - electrochemical series
  - standard electrode potential
  - standard electrode potentials
tags:
  - flashcard/active/general/standard_electrode_potential
  - language/in/English
---

# standard electrode potential

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## usage

Increase in standard electrode potential {{increases [oxidizing power](oxidation.md) and decreases [reducing power](reduction.md)}}, and vice versa. <!--SR:!2025-07-26,652,318-->

## data

```Python
# pytextgen generate data
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal
from pytextgen import gen, read, util
from types import MappingProxyType
from typing import final

bs = '\\'
@final
@dataclass(
  init=True,
  repr=True,
  eq=True,
  order=False,
  unsafe_hash=False,
  frozen=True,
  match_args=True,
  kw_only=False,
  slots=True,
)
class Redox:
  element: str
  oxidant: str
  reductant: str
  potential: Decimal
  electrons: int
  elaboration: str = ''

  @property
  def equation(self):
    return f'{self.oxidant} ⇌ {self.reductant}'
acidic_soln = '[acidic](acid.md) [solution](solution%20(chemistry).md)'
nacidic_soln = 'neutral/[acidic](acid.md) [solution](solution%20(chemistry).md)'
nbasic_soln = 'neutral/[basic](basic.md) [solution](solution%20(chemistry).md)'
sulfuric_acid = '[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)(aq, conc) ⇌ ([SO<sub>2</sub>](sulfur%20dioxide.md)(aq/g) ⇌ [HSO<sub>3</sub><sup>-</sup>](bisulfite.md)(aq) ([H<sub>2</sub>SO<sub>3</sub>](sulfurous%20acid.md)(aq)))'
data = (
  Redox('K', 'K<sup>+</sup>(aq) + e<sup>-</sup>', 'K(s)', Decimal('-2.931'), 1),
  Redox('Ca', 'Ca<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Ca(s)', Decimal('-2.868'), 2),
  Redox('Na', 'Na<sup>+</sup>(aq) + e<sup>-</sup>', 'Na(s)', Decimal('-2.71'), 1),
  Redox('Mg', 'Mg<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Mg(s)', Decimal('-2.372'), 2),
  Redox('Al', 'Al<sup>3+</sup>(aq) + 3e<sup>-</sup>', 'Al(s)', Decimal('-1.662'), 3),
  Redox('H', '2H<sub>2</sub>O(l) + 2e<sup>-</sup>', 'H<sub>2</sub>(g) + 2OH<sup>-</sup>', Decimal('-0.8277'), 2, nbasic_soln),
  Redox('Zn', 'Zn<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Zn(s)', Decimal('-0.7618'), 2),
  Redox('Cr', 'Cr<sup>3+</sup>(aq) + 3e<sup>-</sup>', 'Cr(s)', Decimal('-0.744'), 3),
  Redox('Fe', 'Fe<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Fe(s)', Decimal('-0.44'), 2),
  Redox('Cr', 'Cr<sup>3+</sup>(aq) + e<sup>-</sup>', 'Cr<sup>2+</sup>(aq)', Decimal('-0.407'), 1),
  Redox('Co', 'Co<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Co(s)', Decimal('-0.28'), 2),
  Redox('Ni', 'Ni<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Ni(s)', Decimal('-0.257'), 2),
  Redox('Sn', 'Sn<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Sn(s)', Decimal('-0.13'), 2),
  Redox('Pb', 'Pb<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Pb(s)', Decimal('-0.126'), 2),
  Redox('C', 'CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup>', 'CO(g) + H<sub>2</sub>O(l)', Decimal('-0.11'), 2),
  Redox('H', '2H<sup>+</sup>(aq) + 2e<sup>-</sup>', 'H<sub>2</sub>(g)', Decimal('0'), 2, nacidic_soln),
  Redox('S', 'S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup>', '2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)', Decimal('0.08'), 2),
  Redox('Sn', 'Sn<sup>4+</sup>(aq) + 2e<sup>-</sup>', 'Sn<sup>2+</sup>(aq)', Decimal('0.151'), 2),
  Redox('S', 'HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup>', 'SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', Decimal('0.16'), 2, sulfuric_acid),
  Redox('S', 'SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup>', 'SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)', Decimal('0.17'), 2, sulfuric_acid),
  Redox('Cu', 'Cu<sup>2+</sup>(aq) + 2e<sup>-</sup>', 'Cu(s)', Decimal('0.337'), 2),
  Redox('O', 'O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup>', '4OH<sup>-</sup>(aq)', Decimal('0.401'), 4, nbasic_soln),
  Redox('S', 'SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup>', 'S(s) + 2H<sub>2</sub>O(l)', Decimal('0.5'), 4),
  Redox('C', 'CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup>', 'C(s) + H<sub>2</sub>O(l)', Decimal('0.52'), 2),
  Redox('I', 'I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup>', '3I<sup>-</sup>(aq)', Decimal('0.53'), 2),
  Redox('I', 'I<sub>2</sub>(s) + 2e<sup>-</sup>', '2I<sup>-</sup>(aq)', Decimal('0.54'), 2),
  Redox('S', 'S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup>', '2S(s) + 3H<sub>2</sub>O(l)', Decimal('0.6'), 4),
  Redox('Fe', 'Fe<sup>3+</sup>(aq) + e<sup>-</sup>', 'Fe<sup>2+</sup>(aq)', Decimal('0.77'), 1),
  Redox('Ag', 'Ag<sup>+</sup>(aq) + e<sup>-</sup>', 'Ag(s)', Decimal('0.7996'), 1),
  Redox('N', 'NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup>', 'NO<sub>2</sub>(g) + H<sub>2</sub>O(l)', Decimal('0.8'), 1, '[HNO<sub>3</sub>](nitric%20acid.md)(aq, conc)'),
  Redox('N', 'NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup>', 'NO(g) + 2H<sub>2</sub>O(l)', Decimal('0.958'), 3, '[HNO<sub>3</sub>](nitric%20acid.md)(aq, dilu)'),
  Redox('Br', 'Br<sub>2</sub>(aq) + 2e<sup>-</sup>', '2Br<sup>-</sup>(aq)', Decimal('1.0873'), 2),
  Redox('I', '2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup>', 'I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)', Decimal('1.2'), 10),
  Redox('O', 'O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup>', '2H<sub>2</sub>O(l)', Decimal('1.229'), 4, nacidic_soln),
  Redox('Cr', 'Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup>', '2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)', Decimal('1.33'), 6),
  Redox('Cl', 'Cl<sub>2</sub>(g) + 2e<sup>-</sup>', '2Cl<sup>-</sup>(aq)', Decimal('1.36'), 2),
  Redox('Mn', 'MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup>', 'Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)', Decimal('1.51'), 5, acidic_soln),
  Redox('Co', 'Co<sup>3+</sup>(aq) + e<sup>-</sup>', 'Co<sup>2+</sup>(aq)', Decimal('1.92'), 1),
  Redox('O', 'S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup>', '2SO<sub>4</sub><sup>2-</sup>(aq)', Decimal('2.01'), 2),
  Redox('F', 'F<sub>2</sub>(g) + 2e<sup>-</sup>', '2F<sup>-</sup>(aq)', Decimal('2.87'), 2),
)
data_by_element = defaultdict(list)
for rdx in data:
  data_by_element[rdx.element].append(rdx)
data_by_element = MappingProxyType({key: tuple(val) for key, val in data_by_element.items()})

table = gen.TextCode.compile(f'''
(lowest oxidizing power/highest reducing power)

{gen.rows_to_table(data,
  names=('element', ('oxidant', 'right'), ('⇌', 'center'), ('reductant', 'left'), gen.TextCode.escape(f'$E^{bs}ominus_{bs}text{{red}}$/V'), 'electrons', 'elaboration',),
  values=lambda rdx: (rdx.element, rdx.oxidant, '⇌', rdx.reductant, rdx.potential, rdx.electrons, cloze(rdx.elaboration, escape=True),),
)}

(highest oxidizing power/lowest reducing power)''')
potentials = gen.two_columns_to_code(data,
  left=lambda rdx: gen.TextCode.escape(rdx.equation),
  right=lambda rdx: gen.TextCode.escape(str(rdx.potential))
)
elements = gen.TextCode.compile(
  '{}'.join(f'{gen.TextCode.escape(ele)}{{}}{gen.TextCode.escape("<br/>".join(rdx.equation for rdx in data_by_element[ele]))}' for ele in sorted(data_by_element))
)

return (
  util.Result(
    location=__env__.cwf_sect('230419'),
    text=gen.cloze_text(table,
      states=await read.read_flashcard_states(__env__.cwf_sect('230419')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('9209fd'),
    text=gen.memorize_two_sided(potentials,
      reversible=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('9209fd')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('ab92dd'),
    text=gen.memorize_two_sided(elements,
      states=await read.read_flashcard_states(__env__.cwf_sect('ab92dd'))
    ),
  ),
)
```

<!--pytextgen generate section="230419"--><!-- The following content is generated at 2024-06-09T06:27:26.549426+08:00. Any edits will be overridden! -->

>
> (lowest oxidizing power/highest reducing power)
>
> | element | oxidant | ⇌ | reductant | $E^\ominus_\text{red}$/V | electrons | elaboration |
> |-|-:|:-:|:-|-|-|-|
> | K | K<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | K(s) | -2.931 | 1 |  |
> | Ca | Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Ca(s) | -2.868 | 2 |  |
> | Na | Na<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Na(s) | -2.71 | 1 |  |
> | Mg | Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Mg(s) | -2.372 | 2 |  |
> | Al | Al<sup>3+</sup>(aq) + 3e<sup>-</sup> | ⇌ | Al(s) | -1.662 | 3 |  |
> | H | 2H<sub>2</sub>O(l) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) + 2OH<sup>-</sup> | -0.8277 | 2 | {{neutral/[basic](basic.md) [solution](solution%20(chemistry).md)}} |
> | Zn | Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Zn(s) | -0.7618 | 2 |  |
> | Cr | Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> | ⇌ | Cr(s) | -0.744 | 3 |  |
> | Fe | Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Fe(s) | -0.44 | 2 |  |
> | Cr | Cr<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Cr<sup>2+</sup>(aq) | -0.407 | 1 |  |
> | Co | Co<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Co(s) | -0.28 | 2 |  |
> | Ni | Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Ni(s) | -0.257 | 2 |  |
> | Sn | Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Sn(s) | -0.13 | 2 |  |
> | Pb | Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Pb(s) | -0.126 | 2 |  |
> | C | CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | CO(g) + H<sub>2</sub>O(l) | -0.11 | 2 |  |
> | H | 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) | 0 | 2 | {{neutral/[acidic](acid.md) [solution](solution%20(chemistry).md)}} |
> | S | S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) | 0.08 | 2 |  |
> | Sn | Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Sn<sup>2+</sup>(aq) | 0.151 | 2 |  |
> | S | HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.16 | 2 | {{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)(aq, conc) ⇌ ([SO<sub>2</sub>](sulfur%20dioxide.md)(aq/g) ⇌ [HSO<sub>3</sub><sup>-</sup>](bisulfite.md)(aq) ([H<sub>2</sub>SO<sub>3</sub>](sulfurous%20acid.md)(aq)))}} |
> | S | SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.17 | 2 | {{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)(aq, conc) ⇌ ([SO<sub>2</sub>](sulfur%20dioxide.md)(aq/g) ⇌ [HSO<sub>3</sub><sup>-</sup>](bisulfite.md)(aq) ([H<sub>2</sub>SO<sub>3</sub>](sulfurous%20acid.md)(aq)))}} |
> | Cu | Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Cu(s) | 0.337 | 2 |  |
> | O | O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> | ⇌ | 4OH<sup>-</sup>(aq) | 0.401 | 4 | {{neutral/[basic](basic.md) [solution](solution%20(chemistry).md)}} |
> | S | SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | S(s) + 2H<sub>2</sub>O(l) | 0.5 | 4 |  |
> | C | CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | C(s) + H<sub>2</sub>O(l) | 0.52 | 2 |  |
> | I | I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 3I<sup>-</sup>(aq) | 0.53 | 2 |  |
> | I | I<sub>2</sub>(s) + 2e<sup>-</sup> | ⇌ | 2I<sup>-</sup>(aq) | 0.54 | 2 |  |
> | S | S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2S(s) + 3H<sub>2</sub>O(l) | 0.6 | 4 |  |
> | Fe | Fe<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Fe<sup>2+</sup>(aq) | 0.77 | 1 |  |
> | Ag | Ag<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Ag(s) | 0.7996 | 1 |  |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | NO<sub>2</sub>(g) + H<sub>2</sub>O(l) | 0.8 | 1 | {{[HNO<sub>3</sub>](nitric%20acid.md)(aq, conc)}} |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> | ⇌ | NO(g) + 2H<sub>2</sub>O(l) | 0.958 | 3 | {{[HNO<sub>3</sub>](nitric%20acid.md)(aq, dilu)}} |
> | Br | Br<sub>2</sub>(aq) + 2e<sup>-</sup> | ⇌ | 2Br<sup>-</sup>(aq) | 1.0873 | 2 |  |
> | I | 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> | ⇌ | I<sub>2</sub>(s) + 6H<sub>2</sub>O(l) | 1.2 | 10 |  |
> | O | O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2H<sub>2</sub>O(l) | 1.229 | 4 | {{neutral/[acidic](acid.md) [solution](solution%20(chemistry).md)}} |
> | Cr | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> | ⇌ | 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) | 1.33 | 6 |  |
> | Cl | Cl<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2Cl<sup>-</sup>(aq) | 1.36 | 2 |  |
> | Mn | MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> | ⇌ | Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) | 1.51 | 5 | {{[acidic](acid.md) [solution](solution%20(chemistry).md)}} |
> | Co | Co<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Co<sup>2+</sup>(aq) | 1.92 | 1 |  |
> | O | S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2SO<sub>4</sub><sup>2-</sup>(aq) | 2.01 | 2 |  |
> | F | F<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2F<sup>-</sup>(aq) | 2.87 | 2 |  |
>
> (highest oxidizing power/lowest reducing power) <!--SR:!2028-09-07,1482,316!2025-01-26,498,316!2024-11-07,360,256!2025-03-27,185,276!2024-11-01,419,296!2025-07-10,615,316!2025-02-07,227,256!2028-09-20,1478,316!2024-12-07,442,301-->

<!--/pytextgen-->

### potentials

<!--pytextgen generate section="9209fd"--><!-- The following content is generated at 2024-06-09T06:27:26.493298+08:00. Any edits will be overridden! -->

- K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s)::-2.931 <!--SR:!2025-03-15,185,190-->
- Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s)::-2.868 <!--SR:!2024-11-09,235,150-->
- Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s)::-2.71 <!--SR:!2025-01-01,78,130-->
- Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s)::-2.372 <!--SR:!2024-10-27,24,130-->
- Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s)::-1.662 <!--SR:!2024-11-10,26,130-->
- 2H<sub>2</sub>O(l) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) + 2OH<sup>-</sup>::-0.8277 <!--SR:!2024-11-10,24,130-->
- Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s)::-0.7618 <!--SR:!2024-11-18,34,150-->
- Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Cr(s)::-0.744 <!--SR:!2025-03-02,167,156-->
- Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)::-0.44 <!--SR:!2024-11-27,50,130-->
- Cr<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Cr<sup>2+</sup>(aq)::-0.407 <!--SR:!2024-10-28,13,130-->
- Co<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Co(s)::-0.28 <!--SR:!2024-11-14,37,130-->
- Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ni(s)::-0.257 <!--SR:!2024-12-07,48,150-->
- Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn(s)::-0.13 <!--SR:!2025-01-04,74,150-->
- Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s)::-0.126 <!--SR:!2024-10-31,23,130-->
- CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l)::-0.11 <!--SR:!2025-02-17,237,230-->
- 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g)::0 <!--SR:!2026-06-10,899,336-->
- S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)::0.08 <!--SR:!2024-12-26,70,170-->
- Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn<sup>2+</sup>(aq)::0.151 <!--SR:!2024-10-27,6,130-->
- HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.16 <!--SR:!2024-12-08,69,130-->
- SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)::0.17 <!--SR:!2025-01-23,204,210-->
- Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s)::0.337 <!--SR:!2024-10-27,17,130-->
- O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)::0.401 <!--SR:!2026-09-06,703,210-->
- SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l)::0.5 <!--SR:!2024-10-27,19,130-->
- CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l)::0.52 <!--SR:!2024-11-01,22,130-->
- I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq)::0.53 <!--SR:!2026-04-14,564,199-->
- I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)::0.54 <!--SR:!2025-01-31,102,130-->
- S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l)::0.6 <!--SR:!2024-10-25,1,130-->
- Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq)::0.77 <!--SR:!2026-04-03,683,190-->
- Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s)::0.7996 <!--SR:!2024-12-05,155,150-->
- NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)::0.8 <!--SR:!2026-11-09,843,230-->
- NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l)::0.958 <!--SR:!2024-12-26,98,150-->
- Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq)::1.0873 <!--SR:!2024-12-11,193,170-->
- 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)::1.2 <!--SR:!2024-12-04,70,150-->
- O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l)::1.229 <!--SR:!2024-11-11,34,130-->
- Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)::1.33 <!--SR:!2024-11-23,132,130-->
- Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq)::1.36 <!--SR:!2024-12-13,95,130-->
- MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)::1.51 <!--SR:!2024-11-18,34,150-->
- Co<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Co<sup>2+</sup>(aq)::1.92 <!--SR:!2024-10-31,7,130-->
- S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq)::2.01 <!--SR:!2024-11-18,34,150-->
- F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq)::2.87 <!--SR:!2024-12-18,71,130-->

<!--/pytextgen-->

### elements

<!--pytextgen generate section="ab92dd"--><!-- The following content is generated at 2024-06-09T06:27:26.522404+08:00. Any edits will be overridden! -->

- Ag:::Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s) <!--SR:!2028-05-03,1484,270!2030-05-11,2098,330-->
- Al:::Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s) <!--SR:!2030-03-17,1979,290!2032-07-31,2906,350-->
- Br:::Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq) <!--SR:!2030-01-19,1937,290!2030-04-17,2081,330-->
- C:::CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l)<br/>CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l) <!--SR:!2024-12-14,199,196!2026-07-07,921,336-->
- Ca:::Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s) <!--SR:!2030-09-01,2186,290!2032-09-20,2947,350-->
- Cl:::Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq) <!--SR:!2024-11-10,625,270!2032-03-30,2811,350-->
- Co:::Co<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Co(s)<br/>Co<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Co<sup>2+</sup>(aq) <!--SR:!2025-01-16,440,296!2026-08-15,947,336-->
- Cr:::Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Cr(s)<br/>Cr<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Cr<sup>2+</sup>(aq)<br/>Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) <!--SR:!2028-09-28,1589,270!2027-12-26,1413,310-->
- Cu:::Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s) <!--SR:!2026-02-02,910,270!2032-07-12,2893,350-->
- F:::F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq) <!--SR:!2028-04-06,1466,270!2032-01-09,2747,350-->
- Fe:::Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)<br/>Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq) <!--SR:!2025-02-17,603,230!2026-12-27,1225,310-->
- H:::2H<sub>2</sub>O(l) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) + 2OH<sup>-</sup><br/>2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) <!--SR:!2025-02-24,580,230!2027-02-10,1261,310-->
- I:::I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq)<br/>I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)<br/>2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l) <!--SR:!2024-10-26,613,270!2027-02-09,1260,310-->
- K:::K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s) <!--SR:!2028-07-24,1575,270!2025-10-10,826,310-->
- Mg:::Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s) <!--SR:!2026-08-03,922,270!2032-07-01,2884,350-->
- Mn:::MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) <!--SR:!2028-01-22,1431,310!2029-06-04,1942,330-->
- N:::NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)<br/>NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l) <!--SR:!2024-11-02,110,170!2026-08-18,1105,290-->
- Na:::Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s) <!--SR:!2024-10-27,614,270!2032-10-14,2966,350-->
- Ni:::Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ni(s) <!--SR:!2025-07-08,613,316!2026-07-23,929,336-->
- O:::O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq) <!--SR:!2024-12-04,90,190!2030-04-13,2078,330-->
- Pb:::Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s) <!--SR:!2028-04-13,1424,270!2029-03-29,1891,330-->
- S:::S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)<br/>HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l) <!--SR:!2024-10-30,20,150!2026-02-22,908,290-->
- Sn:::Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn(s)<br/>Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn<sup>2+</sup>(aq) <!--SR:!2027-06-21,1050,296!2025-10-10,707,336-->
- Zn:::Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s) <!--SR:!2026-09-12,1023,250!2029-04-23,1912,330-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/standard_electrode_potential) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
