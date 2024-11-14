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

Increase in standard electrode potential {@{increases [oxidizing power](oxidation.md) and decreases [reducing power](reduction.md)}@}, and vice versa.

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
> | H | 2H<sub>2</sub>O(l) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) + 2OH<sup>-</sup> | -0.8277 | 2 | {@{neutral/[basic](basic.md) [solution](solution%20(chemistry).md)}@} |
> | Zn | Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Zn(s) | -0.7618 | 2 |  |
> | Cr | Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> | ⇌ | Cr(s) | -0.744 | 3 |  |
> | Fe | Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Fe(s) | -0.44 | 2 |  |
> | Cr | Cr<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Cr<sup>2+</sup>(aq) | -0.407 | 1 |  |
> | Co | Co<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Co(s) | -0.28 | 2 |  |
> | Ni | Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Ni(s) | -0.257 | 2 |  |
> | Sn | Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Sn(s) | -0.13 | 2 |  |
> | Pb | Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Pb(s) | -0.126 | 2 |  |
> | C | CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | CO(g) + H<sub>2</sub>O(l) | -0.11 | 2 |  |
> | H | 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | H<sub>2</sub>(g) | 0 | 2 | {@{neutral/[acidic](acid.md) [solution](solution%20(chemistry).md)}@} |
> | S | S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) | 0.08 | 2 |  |
> | Sn | Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Sn<sup>2+</sup>(aq) | 0.151 | 2 |  |
> | S | HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.16 | 2 | {@{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)(aq, conc) ⇌ ([SO<sub>2</sub>](sulfur%20dioxide.md)(aq/g) ⇌ [HSO<sub>3</sub><sup>-</sup>](bisulfite.md)(aq) ([H<sub>2</sub>SO<sub>3</sub>](sulfurous%20acid.md)(aq)))}@} |
> | S | SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l) | 0.17 | 2 | {@{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)(aq, conc) ⇌ ([SO<sub>2</sub>](sulfur%20dioxide.md)(aq/g) ⇌ [HSO<sub>3</sub><sup>-</sup>](bisulfite.md)(aq) ([H<sub>2</sub>SO<sub>3</sub>](sulfurous%20acid.md)(aq)))}@} |
> | Cu | Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> | ⇌ | Cu(s) | 0.337 | 2 |  |
> | O | O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> | ⇌ | 4OH<sup>-</sup>(aq) | 0.401 | 4 | {@{neutral/[basic](basic.md) [solution](solution%20(chemistry).md)}@} |
> | S | SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | S(s) + 2H<sub>2</sub>O(l) | 0.5 | 4 |  |
> | C | CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> | ⇌ | C(s) + H<sub>2</sub>O(l) | 0.52 | 2 |  |
> | I | I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 3I<sup>-</sup>(aq) | 0.53 | 2 |  |
> | I | I<sub>2</sub>(s) + 2e<sup>-</sup> | ⇌ | 2I<sup>-</sup>(aq) | 0.54 | 2 |  |
> | S | S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2S(s) + 3H<sub>2</sub>O(l) | 0.6 | 4 |  |
> | Fe | Fe<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Fe<sup>2+</sup>(aq) | 0.77 | 1 |  |
> | Ag | Ag<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | Ag(s) | 0.7996 | 1 |  |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> | ⇌ | NO<sub>2</sub>(g) + H<sub>2</sub>O(l) | 0.8 | 1 | {@{[HNO<sub>3</sub>](nitric%20acid.md)(aq, conc)}@} |
> | N | NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> | ⇌ | NO(g) + 2H<sub>2</sub>O(l) | 0.958 | 3 | {@{[HNO<sub>3</sub>](nitric%20acid.md)(aq, dilu)}@} |
> | Br | Br<sub>2</sub>(aq) + 2e<sup>-</sup> | ⇌ | 2Br<sup>-</sup>(aq) | 1.0873 | 2 |  |
> | I | 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> | ⇌ | I<sub>2</sub>(s) + 6H<sub>2</sub>O(l) | 1.2 | 10 |  |
> | O | O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> | ⇌ | 2H<sub>2</sub>O(l) | 1.229 | 4 | {@{neutral/[acidic](acid.md) [solution](solution%20(chemistry).md)}@} |
> | Cr | Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> | ⇌ | 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) | 1.33 | 6 |  |
> | Cl | Cl<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2Cl<sup>-</sup>(aq) | 1.36 | 2 |  |
> | Mn | MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> | ⇌ | Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l) | 1.51 | 5 | {@{[acidic](acid.md) [solution](solution%20(chemistry).md)}@} |
> | Co | Co<sup>3+</sup>(aq) + e<sup>-</sup> | ⇌ | Co<sup>2+</sup>(aq) | 1.92 | 1 |  |
> | O | S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> | ⇌ | 2SO<sub>4</sub><sup>2-</sup>(aq) | 2.01 | 2 |  |
> | F | F<sub>2</sub>(g) + 2e<sup>-</sup> | ⇌ | 2F<sup>-</sup>(aq) | 2.87 | 2 |  |
>
> (highest oxidizing power/lowest reducing power)

<!--/pytextgen-->

### potentials

<!--pytextgen generate section="9209fd"--><!-- The following content is generated at 2024-06-09T06:27:26.493298+08:00. Any edits will be overridden! -->

- K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s):@:-2.931
- Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s):@:-2.868
- Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s):@:-2.71
- Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s):@:-2.372
- Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s):@:-1.662
- 2H<sub>2</sub>O(l) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) + 2OH<sup>-</sup>:@:-0.8277
- Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s):@:-0.7618
- Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Cr(s):@:-0.744
- Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s):@:-0.44
- Cr<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Cr<sup>2+</sup>(aq):@:-0.407
- Co<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Co(s):@:-0.28
- Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ni(s):@:-0.257
- Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn(s):@:-0.13
- Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s):@:-0.126
- CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l):@:-0.11
- 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g):@:0
- S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq):@:0.08
- Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn<sup>2+</sup>(aq):@:0.151
- HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l):@:0.16
- SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l):@:0.17
- Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s):@:0.337
- O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq):@:0.401
- SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l):@:0.5
- CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l):@:0.52
- I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq):@:0.53
- I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq):@:0.54
- S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l):@:0.6
- Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq):@:0.77
- Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s):@:0.7996
- NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l):@:0.8
- NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l):@:0.958
- Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq):@:1.0873
- 2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l):@:1.2
- O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l):@:1.229
- Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l):@:1.33
- Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq):@:1.36
- MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l):@:1.51
- Co<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Co<sup>2+</sup>(aq):@:1.92
- S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq):@:2.01
- F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq):@:2.87

<!--/pytextgen-->

### elements

<!--pytextgen generate section="ab92dd"--><!-- The following content is generated at 2024-06-09T06:27:26.522404+08:00. Any edits will be overridden! -->

- Ag::@::Ag<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Ag(s)
- Al::@::Al<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Al(s)
- Br::@::Br<sub>2</sub>(aq) + 2e<sup>-</sup> ⇌ 2Br<sup>-</sup>(aq)
- C::@::CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ CO(g) + H<sub>2</sub>O(l)<br/>CO(g) + 2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ C(s) + H<sub>2</sub>O(l)
- Ca::@::Ca<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ca(s)
- Cl::@::Cl<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2Cl<sup>-</sup>(aq)
- Co::@::Co<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Co(s)<br/>Co<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Co<sup>2+</sup>(aq)
- Cr::@::Cr<sup>3+</sup>(aq) + 3e<sup>-</sup> ⇌ Cr(s)<br/>Cr<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Cr<sup>2+</sup>(aq)<br/>Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>-</sup> ⇌ 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)
- Cu::@::Cu<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Cu(s)
- F::@::F<sub>2</sub>(g) + 2e<sup>-</sup> ⇌ 2F<sup>-</sup>(aq)
- Fe::@::Fe<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Fe(s)<br/>Fe<sup>3+</sup>(aq) + e<sup>-</sup> ⇌ Fe<sup>2+</sup>(aq)
- H::@::2H<sub>2</sub>O(l) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g) + 2OH<sup>-</sup><br/>2H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ H<sub>2</sub>(g)
- I::@::I<sub>3</sub><sup>-</sup>(aq) + 2e<sup>-</sup> ⇌ 3I<sup>-</sup>(aq)<br/>I<sub>2</sub>(s) + 2e<sup>-</sup> ⇌ 2I<sup>-</sup>(aq)<br/>2IO<sub>3</sub><sup>-</sup>(aq) + 12H<sup>+</sup>(aq) + 10e<sup>-</sup> ⇌ I<sub>2</sub>(s) + 6H<sub>2</sub>O(l)
- K::@::K<sup>+</sup>(aq) + e<sup>-</sup> ⇌ K(s)
- Mg::@::Mg<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Mg(s)
- Mn::@::MnO<sub>4</sub><sup>-</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>-</sup> ⇌ Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l)
- N::@::NO<sub>3</sub><sup>-</sup>(aq) + 2H<sup>+</sup>(aq) + e<sup>-</sup> ⇌ NO<sub>2</sub>(g) + H<sub>2</sub>O(l)<br/>NO<sub>3</sub><sup>-</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>-</sup> ⇌ NO(g) + 2H<sub>2</sub>O(l)
- Na::@::Na<sup>+</sup>(aq) + e<sup>-</sup> ⇌ Na(s)
- Ni::@::Ni<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Ni(s)
- O::@::O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> ⇌ 4OH<sup>-</sup>(aq)<br/>O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>8</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2SO<sub>4</sub><sup>2-</sup>(aq)
- Pb::@::Pb<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Pb(s)
- S::@::S<sub>4</sub>O<sub>6</sub><sup>2-</sup>(aq) + 2e<sup>-</sup> ⇌ 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq)<br/>HSO<sub>4</sub><sup>-</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>4</sub><sup>2-</sup>(aq) + 4H<sup>+</sup>(aq) + 2e<sup>-</sup> ⇌ SO<sub>2</sub>(aq) + 2H<sub>2</sub>O(l)<br/>SO<sub>2</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ S(s) + 2H<sub>2</sub>O(l)<br/>S<sub>2</sub>O<sub>3</sub><sup>2-</sup>(aq) + 6H<sup>+</sup>(aq) + 4e<sup>-</sup> ⇌ 2S(s) + 3H<sub>2</sub>O(l)
- Sn::@::Sn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn(s)<br/>Sn<sup>4+</sup>(aq) + 2e<sup>-</sup> ⇌ Sn<sup>2+</sup>(aq)
- Zn::@::Zn<sup>2+</sup>(aq) + 2e<sup>-</sup> ⇌ Zn(s)

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/standard_electrode_potential) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
