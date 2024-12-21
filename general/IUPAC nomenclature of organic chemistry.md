---
aliases:
  - IUPAC nomenclature of organic chemistry
tags:
  - flashcard/active/general/IUPAC_nomenclature_of_organic_chemistry
  - language/in/English
---

# IUPAC nomenclature of organic chemistry

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

The __IUPAC nomenclature of organic chemistry__ is {@{a method of naming [organic compounds](organic%20compound.md)}@}. There is also the [IUPAC nomenclature of inorganic chemistry](IUPAC%20nomenclature%20of%20inorganic%20chemistry.md). <!--SR:!2029-01-22,1702,383-->

## principles

```Python
# pytextgen generate data
from pytextgen import gen, read, util
principles: gen.TextCode = gen.seq_to_code((
    '[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)',
    'identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)',
    'identify side-chains',
    'identify remaining functional groups',
    'identify multiple bonds',
    '[identify numbering direction](#identify%20numbering%20direction)',
    'number and [prefix](#prefix%20for%20type%20count) substituents and bonds',
    '[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix',
    '(optional) omit unnecessary locants',
    '[modify words for pronunciation](#modify%20words%20for%20pronunciation)',
    '[modify punctuations](#modify%20punctuations)',
    'prefix notation for _cis_–_trans_ isomerism',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
id_parent: gen.TextCode = gen.seq_to_code((
    'most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)',
    'most multiple bonds',
    'maximum length',
    'most prefixes',
    'most single bonds',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
id_num_dir: gen.TextCode = gen.seq_to_code((
    'smallest locant for the suffix functional group',
    'smallest locant for multiple bonds',
    'smallest locant for prefixes',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
arrange: gen.TextCode = gen.seq_to_code((
    'bond order: single bond, double bond, triple bond, ...',
    'prefix order: alphabetical order ignoring prefixes for type count',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
pronuciations: gen.TextCode = gen.TextCode.compile(
  fR'''{{{gen.Tag.TEXT}:- }}suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u){{{gen.Tag.TEXT}:\: }}drop '-e'{{{gen.Tag.TEXT}:
- }}bond suffix is followed by prefix for type count{{{gen.Tag.TEXT}:\: }}keep '-e'{{{gen.Tag.TEXT}:
- }}prefix for carbon count is followed by prefix for type count{{{gen.Tag.TEXT}:\: }}add '-a'{{}}'''
)
punctuations: gen.TextCode = gen.seq_to_code((
    'commas (,) between locants',
    'hyphens (-) between word and locant',
    'remove (most) spaces ( )',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
return (
  util.Result(
    location=__env__.cwf_sect('5193cd'),
    text=gen.quote_text(principles),
  ),
  util.Result(
    location=__env__.cwf_sect('48dca2'),
    text=gen.memorize_linked_seq(principles,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('48dca2')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('12cd9e'),
    text=gen.quote_text(id_parent),
  ),
  util.Result(
    location=__env__.cwf_sect('920dca'),
    text=gen.memorize_linked_seq(id_parent,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('920dca')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('10dacd'),
    text=gen.quote_text(id_num_dir),
  ),
  util.Result(
    location=__env__.cwf_sect('abacdf'),
    text=gen.memorize_linked_seq(id_num_dir,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('abacdf')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('ab93dd'),
    text=gen.quote_text(arrange),
  ),
  util.Result(
    location=__env__.cwf_sect('828019'),
    text=gen.memorize_linked_seq(arrange,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('828019')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('299372'),
    text=gen.quote_text(pronuciations),
  ),
  util.Result(
    location=__env__.cwf_sect('19fc21'),
    text=gen.memorize_two_sided(pronuciations,
      states=await read.read_flashcard_states(__env__.cwf_sect('19fc21')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('a920de'),
    text=gen.quote_text(punctuations),
  ),
  util.Result(
    location=__env__.cwf_sect('9293da'),
    text=gen.memorize_linked_seq(punctuations,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('9293da')),
    ),
  ),
)
```

The steps for naming an organic compound are:
<!--pytextgen generate section="5193cd"--><!-- The following content is generated at 2022-11-05T00:24:43.599371+08:00. Any edits will be overridden! -->

> 1. [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)
> 2. identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)
> 3. identify side-chains
> 4. identify remaining functional groups
> 5. identify multiple bonds
> 6. [identify numbering direction](#identify%20numbering%20direction)
> 7. number and [prefix](#prefix%20for%20type%20count) substituents and bonds
> 8. [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix
> 9. (optional) omit unnecessary locants
> 10. [modify words for pronunciation](#modify%20words%20for%20pronunciation)
> 11. [modify punctuations](#modify%20punctuations)
> 12. prefix notation for _cis_–_trans_ isomerism

<!--/pytextgen-->

<!--pytextgen generate section="48dca2"--><!-- The following content is generated at 2024-01-04T20:17:52.046217+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain) <!--SR:!2027-04-01,991,255!2026-02-20,924,345-->
- [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)→::@::←identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2029-03-07,1596,262!2029-03-21,1647,325-->
- identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)→::@::←identify side-chains <!--SR:!2027-04-28,1021,264!2025-01-06,77,130-->
- identify side-chains→::@::←identify remaining functional groups <!--SR:!2026-06-02,852,230!2025-02-25,243,207-->
- identify remaining functional groups→::@::←identify multiple bonds <!--SR:!2025-02-08,275,190!2026-06-27,690,207-->
- identify multiple bonds→::@::←[identify numbering direction](#identify%20numbering%20direction) <!--SR:!2025-11-26,549,230!2025-02-20,114,190-->
- [identify numbering direction](#identify%20numbering%20direction)→::@::←number and [prefix](#prefix%20for%20type%20count) substituents and bonds <!--SR:!2026-01-17,579,190!2026-03-01,749,265-->
- number and [prefix](#prefix%20for%20type%20count) substituents and bonds→::@::←[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix <!--SR:!2025-03-21,156,207!2024-12-25,360,230-->
- [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix→::@::←(optional) omit unnecessary locants <!--SR:!2027-10-04,1037,230!2025-04-05,214,207-->
- (optional) omit unnecessary locants→::@::←[modify words for pronunciation](#modify%20words%20for%20pronunciation) <!--SR:!2026-09-17,770,230!2024-12-28,231,225-->
- [modify words for pronunciation](#modify%20words%20for%20pronunciation)→::@::←[modify punctuations](#modify%20punctuations) <!--SR:!2029-09-16,1877,312!2025-12-06,562,267-->
- [modify punctuations](#modify%20punctuations)→::@::←prefix notation for _cis_–_trans_ isomerism <!--SR:!2026-05-05,523,253!2027-10-24,1227,307-->
- prefix notation for _cis_–_trans_ isomerism→::@::←_(end)_ <!--SR:!2029-08-16,1975,382!2027-07-03,1153,307-->

<!--/pytextgen-->

### subprinciples

#### identify parent hydrocarbon chain

<!--pytextgen generate section="12cd9e"--><!-- The following content is generated at 2022-11-05T00:24:43.629369+08:00. Any edits will be overridden! -->

> 1. most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)
> 2. most multiple bonds
> 3. maximum length
> 4. most prefixes
> 5. most single bonds

<!--/pytextgen-->

<!--pytextgen generate section="920dca"--><!-- The following content is generated at 2024-01-04T20:17:52.176781+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2027-12-10,1297,256!2030-03-16,2144,382-->
- most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)→::@::←most multiple bonds <!--SR:!2028-02-27,1346,256!2027-09-09,1192,305-->
- most multiple bonds→::@::←maximum length <!--SR:!2025-02-16,416,256!2025-10-04,690,282-->
- maximum length→::@::←most prefixes <!--SR:!2025-01-19,580,261!2029-10-12,1758,325-->
- most prefixes→::@::←most single bonds <!--SR:!2027-12-09,1307,261!2025-03-02,332,262-->
- most single bonds→::@::←_(end)_ <!--SR:!2025-08-10,470,325!2025-03-21,668,345-->

<!--/pytextgen-->

#### identify numbering direction

<!--pytextgen generate section="10dacd"--><!-- The following content is generated at 2022-11-05T00:24:43.659370+08:00. Any edits will be overridden! -->

> 1. smallest locant for the suffix functional group
> 2. smallest locant for multiple bonds
> 3. smallest locant for prefixes

<!--/pytextgen-->

<!--pytextgen generate section="abacdf"--><!-- The following content is generated at 2024-01-04T20:17:52.021214+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←smallest locant for the suffix functional group <!--SR:!2028-06-26,1449,266!2030-03-25,2149,382-->
- smallest locant for the suffix functional group→::@::←smallest locant for multiple bonds <!--SR:!2029-12-14,1996,286!2030-07-11,2138,342-->
- smallest locant for multiple bonds→::@::←smallest locant for prefixes <!--SR:!2028-02-06,1523,286!2026-02-13,908,345-->
- smallest locant for prefixes→::@::←_(end)_ <!--SR:!2029-03-04,1841,382!2027-07-26,1161,305-->

<!--/pytextgen-->

#### arrange

<!--pytextgen generate section="ab93dd"--><!-- The following content is generated at 2024-02-17T20:15:49.350229+08:00. Any edits will be overridden! -->

> 1. bond order: single bond, double bond, triple bond, ...
> 2. prefix order: alphabetical order ignoring prefixes for type count

<!--/pytextgen-->

<!--pytextgen generate section="828019"--><!-- The following content is generated at 2024-02-17T20:15:49.262704+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←bond order: single bond, double bond, triple bond, ... <!--SR:!2026-03-04,917,292!2025-06-20,387,287-->
- bond order: single bond, double bond, triple bond, ...→::@::←prefix order: alphabetical order ignoring prefixes for type count <!--SR:!2026-05-03,802,250!2031-10-07,2502,342-->
- prefix order: alphabetical order ignoring prefixes for type count→::@::←_(end)_ <!--SR:!2026-01-10,880,340!2025-04-17,220,302-->

<!--/pytextgen-->

#### modify words for pronunciation

<!--pytextgen generate section="299372"--><!-- The following content is generated at 2022-11-05T00:24:43.721370+08:00. Any edits will be overridden! -->

> - suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u): drop '-e'
> - bond suffix is followed by prefix for type count: keep '-e'
> - prefix for carbon count is followed by prefix for type count: add '-a'

<!--/pytextgen-->

<!--pytextgen generate section="19fc21"--><!-- The following content is generated at 2024-01-04T20:17:51.994215+08:00. Any edits will be overridden! -->

- suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u)::@::drop '-e' <!--SR:!2026-06-12,774,224!2029-06-07,1672,267-->
- bond suffix is followed by prefix for type count::@::keep '-e' <!--SR:!2027-07-16,1187,250!2026-02-28,471,201-->
- prefix for carbon count is followed by prefix for type count::@::add '-a' <!--SR:!2025-08-29,636,230!2025-08-27,442,210-->

<!--/pytextgen-->

#### modify punctuations

<!--pytextgen generate section="a920de"--><!-- The following content is generated at 2022-11-05T00:24:43.754371+08:00. Any edits will be overridden! -->

> 1. commas (,) between locants
> 2. hyphens (-) between word and locant
> 3. remove (most) spaces ( )

<!--/pytextgen-->

<!--pytextgen generate section="9293da"--><!-- The following content is generated at 2024-01-04T20:17:52.218337+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←commas (,) between locants <!--SR:!2025-05-09,838,332!2025-03-14,596,320-->
- commas (,) between locants→::@::←hyphens (-) between word and locant <!--SR:!2027-12-20,1550,313!2028-07-15,1399,321-->
- hyphens (-) between word and locant→::@::←remove (most) spaces ( ) <!--SR:!2026-08-11,1244,353!2027-07-15,1340,362-->
- remove (most) spaces ( )→::@::←_(end)_ <!--SR:!2028-05-21,1504,367!2026-02-19,925,347-->

<!--/pytextgen-->

### prefix for type count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {@{the first one is no prefix}@}. <!--SR:!2029-02-08,1692,383-->

### prefix for carbon count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {@{the last character _a-_ is trimmed away and the first four are _meth-_, _eth-_, _prop-_, and _but-_}@}. <!--SR:!2026-01-18,747,343-->

## functional groups

```Python
# pytextgen generate data
from pytextgen import gen, read, util
import typing
@typing.final
class Group(typing.NamedTuple):
  clazz: str
  group: str
  formula: str
  prefix: str
  suffix: str
  infix: str
  misc: typing.Mapping[str, str] = {}
data: typing.Sequence[Group] = (
  Group(clazz='alkane', group='alkyl', formula='R(CH<sub>2</sub>)<sub>n</sub>H', prefix='([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl-', suffix='-ane', infix='(none), (locant)', misc={'cyclic prefix': 'cyclo-'},),
  Group(clazz='alkene', group='alkenyl', formula='R<sub>2</sub>C=CR<sub>2</sub>', prefix='([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-', suffix='-ene', infix='(locant)', misc={'cyclic prefix': 'cyclo-'},),
  Group(clazz='alkyne', group='alkynyl', formula='RC≡CR\'', prefix='([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-', suffix='-yne', infix='(locant)', misc={'cyclic prefix': 'cyclo-'},),
  Group(clazz='benzene derivative', group='phenyl', formula='RC<sub>6</sub>H<sub>5</sub>/RPh', prefix='phenyl-', suffix='-benzene', infix='(locant)',),
  Group(clazz='([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane', group='([prefix for halogen](#affixes%20for%20halogen)), halo', formula='RX', prefix='([prefix for halogen](#affixes%20for%20halogen))-, halo-', suffix='([suffix for halogen](#affixes%20for%20halogen))', infix='(locant)',),
  Group(clazz='alcohol', group='hydroxyl', formula='ROH', prefix='hydroxy-', suffix='-ol', infix='(locant)',),
  Group(clazz='ether', group='ether', formula='ROR\'', prefix='([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR\'), alkoxy- (-OR\'), oxa- (-O-)', suffix='ether', infix='(locant)',),
  Group(clazz='aldehyde', group='aldehyde', formula='RCHO', prefix='oxo- (=O), formyl- (-CHO)', suffix='-al (=O), -carbaldehyde (-CHO)', infix='(locant)',),
  Group(clazz='ketone', group='carbonyl', formula='RCOR\'', prefix='oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR\'), alkoyl- (-COR\')', suffix='-one', infix='(locant)'),
  Group(clazz='carboxylic acid', group='carboxyl', formula='RCOOH', prefix='carboxy-', suffix='-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)', infix='(locant)'),
  Group(clazz='carboxylate', group='carboxylate', formula='RCOO<sup>-</sup>', prefix='carboxy-', suffix='-ate (retained), -oate', infix='(locant)',),
  Group(clazz='alkanoyl', group='acyl', formula='RCO', prefix='(none)', suffix='-yl (retained), -oyl', infix='(locant)',),
  Group(clazz='amine', group='amino', formula='RNH<sub>2</sub>, RR\'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>', prefix='amino- (RNH<sub>2</sub>/RR\'NH/R<sub>3</sub>), ammonio- (R<sub>4</sub>N<sup>+</sup>)', suffix='-amine (RNH<sub>2</sub>/RR\'NH/R<sub>3</sub>), -ammonium (R<sub>4</sub>N<sup>+</sup>)', infix='(locant) & _N_ (R\'/R\'\'/R<sub>3</sub>/R<sub>4</sub>)'),
  Group(clazz='amide', group='amide', formula='RCONH<sub>2</sub>, RCONHR\', RCONR\'R\'\'', prefix='amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)', suffix='-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)', infix='(locant) & _N_ (R\', R\'\')'),
  Group(clazz='nitrile', group='nitrile', formula='RCN', prefix='cyano-', suffix='-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)', infix='(locant)'),
)
map: typing.Mapping[str, typing.Mapping[str, str]] = {
  group.clazz: {
    'group': group.group,
    'formula': group.formula,
    'prefix': group.prefix,
    'suffix': group.suffix,
    'infix': group.infix,
    **group.misc,
  } for group in data
}
table: str = gen.quotette(
  gen.rows_to_table(data,
    names=('class', 'group', 'formula', 'prefix', 'suffix', 'infix', 'misc',),
    values=lambda group: (group.clazz, group.group, group.formula, group.prefix, group.suffix, group.infix,
      '\n'.join(f'- {key}: {value}' for key, value in group.misc.items()),
    ),
  ),
  prefix='> ',
)
text: gen.TextCode = gen.maps_to_code(map,
  name_cloze=True,)
return (
  util.Result(
    location=__env__.cwf_sect('28dcee'),
    text=table,
  ),
  util.Result(
    location=__env__.cwf_sect('a39fd2'),
    text=gen.cloze_text(text,
      separator="\n\n<!-- markdownlint MD028 -->\n\n",
      states=await read.read_flashcard_states(__env__.cwf_sect('a39fd2')),
    ),
  ),
)
```

Use suffixes (starts with hyphen (-)) before prefixes. Only use one suffix. Bonds must use suffixes. Always add infixes.

<!--pytextgen generate section="28dcee"--><!-- The following content is generated at 2024-10-09T17:40:50.221476+08:00. Any edits will be overridden! -->

> | class | group | formula | prefix | suffix | infix | misc |
> |-|-|-|-|-|-|-|
> | alkane | alkyl | R(CH<sub>2</sub>)<sub>n</sub>H | ([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl- | -ane | (none), (locant) | - cyclic prefix: cyclo- |
> | alkene | alkenyl | R<sub>2</sub>C=CR<sub>2</sub> | ([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl- | -ene | (locant) | - cyclic prefix: cyclo- |
> | alkyne | alkynyl | RC≡CR' | ([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl- | -yne | (locant) | - cyclic prefix: cyclo- |
> | benzene derivative | phenyl | RC<sub>6</sub>H<sub>5</sub>/RPh | phenyl- | -benzene | (locant) |  |
> | ([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane | ([prefix for halogen](#affixes%20for%20halogen)), halo | RX | ([prefix for halogen](#affixes%20for%20halogen))-, halo- | ([suffix for halogen](#affixes%20for%20halogen)) | (locant) |  |
> | alcohol | hydroxyl | ROH | hydroxy- | -ol | (locant) |  |
> | ether | ether | ROR' | ([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-) | ether | (locant) |  |
> | aldehyde | aldehyde | RCHO | oxo- (=O), formyl- (-CHO) | -al (=O), -carbaldehyde (-CHO) | (locant) |  |
> | ketone | carbonyl | RCOR' | oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR'), alkoyl- (-COR') | -one | (locant) |  |
> | carboxylic acid | carboxyl | RCOOH | carboxy- | -ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH) | (locant) |  |
> | carboxylate | carboxylate | RCOO<sup>-</sup> | carboxy- | -ate (retained), -oate | (locant) |  |
> | alkanoyl | acyl | RCO | (none) | -yl (retained), -oyl | (locant) |  |
> | amine | amino | RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup> | amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (R<sub>4</sub>N<sup>+</sup>) | -amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (R<sub>4</sub>N<sup>+</sup>) | (locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>) |  |
> | amide | amide | RCONH<sub>2</sub>, RCONHR', RCONR'R'' | amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>) | -amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>) | (locant) & _N_ (R', R'') |  |
> | nitrile | nitrile | RCN | cyano- | -nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN) | (locant) |  |

<!--/pytextgen-->

<!--pytextgen generate section="a39fd2"--><!-- The following content is generated at 2024-10-09T17:40:50.193892+08:00. Any edits will be overridden! -->

> {@{alkane}@}
>
> - group: {@{alkyl}@}
> - formula: {@{R(CH<sub>2</sub>)<sub>n</sub>H}@}
> - prefix: {@{([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl-}@}
> - suffix: {@{-ane}@}
> - infix: {@{(none), (locant)}@}
> - cyclic prefix: {@{cyclo-}@} <!--SR:!2029-12-16,2077,388!2028-05-28,1511,368!2031-10-14,2502,368!2027-10-17,1405,368!2028-05-09,1497,368!2026-09-16,1012,348!2029-11-21,2057,388-->

<!-- markdownlint MD028 -->

> {@{alkene}@}
>
> - group: {@{alkenyl}@}
> - formula: {@{R<sub>2</sub>C=CR<sub>2</sub>}@}
> - prefix: {@{([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-}@}
> - suffix: {@{-ene}@}
> - infix: {@{(locant)}@}
> - cyclic prefix: {@{cyclo-}@} <!--SR:!2029-02-17,1827,380!2030-04-15,2169,382!2027-04-03,1256,362!2026-07-29,935,302!2030-03-06,2134,382!2030-02-22,2124,382!2025-03-06,644,327-->

<!-- markdownlint MD028 -->

> {@{alkyne}@}
>
> - group: {@{alkynyl}@}
> - formula: {@{RC≡CR'}@}
> - prefix: {@{([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-}@}
> - suffix: {@{-yne}@}
> - infix: {@{(locant)}@}
> - cyclic prefix: {@{cyclo-}@} <!--SR:!2026-02-11,918,340!2025-03-16,649,320!2030-01-30,2103,380!2025-09-25,682,281!2030-08-11,2263,382!2029-03-10,1846,382!2026-10-21,1140,367-->

<!-- markdownlint MD028 -->

> {@{benzene derivative}@}
>
> - group: {@{phenyl}@}
> - formula: {@{RC<sub>6</sub>H<sub>5</sub>/RPh}@}
> - prefix: {@{phenyl-}@}
> - suffix: {@{-benzene}@}
> - infix: {@{(locant)}@} <!--SR:!2029-02-11,1688,320!2025-06-11,723,340!2027-07-13,1326,362!2026-12-12,1177,362!2028-10-10,1602,322!2026-10-01,1023,347-->

<!-- markdownlint MD028 -->

> {@{([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane}@}
>
> - group: {@{([prefix for halogen](#affixes%20for%20halogen)), halo}@}
> - formula: {@{RX}@}
> - prefix: {@{([prefix for halogen](#affixes%20for%20halogen))-, halo-}@}
> - suffix: {@{([suffix for halogen](#affixes%20for%20halogen))}@}
> - infix: {@{(locant)}@} <!--SR:!2026-11-16,1064,320!2025-06-25,688,321!2030-07-23,2249,382!2028-03-22,1477,322!2026-04-24,903,305!2030-03-19,2152,387-->

<!-- markdownlint MD028 -->

> {@{alcohol}@}
>
> - group: {@{hydroxyl}@}
> - formula: {@{ROH}@}
> - prefix: {@{hydroxy-}@}
> - suffix: {@{-ol}@}
> - infix: {@{(locant)}@} <!--SR:!2030-04-09,2164,382!2028-08-09,1559,362!2030-07-25,2249,382!2028-03-30,1463,365!2027-08-18,1353,365!2029-10-29,2037,387-->

<!-- markdownlint MD028 -->

> {@{ether}@}
>
> - group: {@{ether}@}
> - formula: {@{ROR'}@}
> - prefix: {@{([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-)}@}
> - suffix: {@{ether}@}
> - infix: {@{(locant)}@} <!--SR:!2030-02-03,2108,380!2030-02-05,2110,382!2029-03-16,1851,382!2025-06-06,198,190!2026-02-24,925,345!2028-09-02,1699,387-->

<!-- markdownlint MD028 -->

> {@{aldehyde}@}
>
> - group: {@{aldehyde}@}
> - formula: {@{RCHO}@}
> - prefix: {@{oxo- (=O), formyl- (-CHO)}@}
> - suffix: {@{-al (=O), -carbaldehyde (-CHO)}@}
> - infix: {@{(locant)}@} <!--SR:!2029-03-22,1856,382!2028-01-06,1463,362!2025-01-20,605,322!2025-02-18,76,150!2025-09-10,677,285!2028-10-10,1730,387-->

<!-- markdownlint MD028 -->

> {@{ketone}@}
>
> - group: {@{carbonyl}@}
> - formula: {@{RCOR'}@}
> - prefix: {@{oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR'), alkoyl- (-COR')}@}
> - suffix: {@{-one}@}
> - infix: {@{(locant)}@} <!--SR:!2025-12-23,823,300!2026-10-01,825,280!2025-03-13,595,321!2025-03-19,92,130!2025-01-16,228,342!2028-07-31,1552,362-->

<!-- markdownlint MD028 -->

> {@{carboxylic acid}@}
>
> - group: {@{carboxyl}@}
> - formula: {@{RCOOH}@}
> - prefix: {@{carboxy-}@}
> - suffix: {@{-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)}@}
> - infix: {@{(locant)}@} <!--SR:!2025-08-29,784,340!2031-06-19,2419,342!2028-07-22,1545,362!2029-09-25,1747,322!2026-10-27,966,305!2029-11-05,2042,387-->

<!-- markdownlint MD028 -->

> {@{carboxylate}@}
>
> - group: {@{carboxylate}@}
> - formula: {@{RCOO<sup>-</sup>}@}
> - prefix: {@{carboxy-}@}
> - suffix: {@{-ate (retained), -oate}@}
> - infix: {@{(locant)}@} <!--SR:!2029-02-20,1831,382!2030-02-08,2115,382!2030-01-21,2100,382!2025-11-12,732,282!2026-01-09,832,302!2028-12-05,1775,387-->

<!-- markdownlint MD028 -->

> {@{alkanoyl}@}
>
> - group: {@{acyl}@}
> - formula: {@{RCO}@}
> - prefix: {@{(none)}@}
> - suffix: {@{-yl (retained), -oyl}@}
> - infix: {@{(locant)}@} <!--SR:!2027-07-29,1137,281!2026-01-25,576,302!2030-07-17,2244,382!2027-07-06,993,242!2026-01-06,571,227!2028-07-25,1555,367-->

<!-- markdownlint MD028 -->

> {@{amine}@}
>
> - group: {@{amino}@}
> - formula: {@{RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>}@}
> - prefix: {@{amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (R<sub>4</sub>N<sup>+</sup>)}@}
> - suffix: {@{-amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (R<sub>4</sub>N<sup>+</sup>)}@}
> - infix: {@{(locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>)}@} <!--SR:!2027-03-08,1174,365!2029-09-01,1986,385!2025-02-17,627,325!2031-03-29,2322,345!2028-01-18,1202,287!2025-06-09,664,327-->

<!-- markdownlint MD028 -->

> {@{amide}@}
>
> - group: {@{amide}@}
> - formula: {@{RCONH<sub>2</sub>, RCONHR', RCONR'R''}@}
> - prefix: {@{amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)}@}
> - suffix: {@{-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)}@}
> - infix: {@{(locant) & _N_ (R', R'')}@} <!--SR:!2026-08-17,1073,365!2029-09-06,1991,385!2026-05-02,984,345!2026-01-13,733,285!2026-04-27,911,305!2027-08-26,1378,367-->

<!-- markdownlint MD028 -->

> {@{nitrile}@}
>
> - group: {@{nitrile}@}
> - formula: {@{RCN}@}
> - prefix: {@{cyano-}@}
> - suffix: {@{-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)}@}
> - infix: {@{(locant)}@} <!--SR:!2030-03-06,2143,388!2027-10-13,1401,368!2028-05-27,1510,368!2026-03-30,958,348!2025-07-18,623,268!2028-06-27,1534,368-->

<!--/pytextgen-->

### affixes for halogen

```Python
# pytextgen generate data
from pytextgen import gen, read, util
import typing
@typing.final
class Affixes(typing.NamedTuple):
  element: str
  prefix: str
  suffix: str
data: typing.Sequence[Affixes] = (
  Affixes(element='fluorine', prefix='fluoro-', suffix='fluoride',),
  Affixes(element='chlorine', prefix='chloro-', suffix='chloride',),
  Affixes(element='bromine', prefix='bromo-', suffix='bromide',),
  Affixes(element='iodine', prefix='iodo-', suffix='iodide',),
)
table: gen.TextCode = gen.TextCode.compile(gen.rows_to_table(data,
    names=('element', 'prefix', 'suffix',),
    values=lambda affixes: map(gen.TextCode.escape,
      (affixes.element, cloze(affixes.prefix), cloze(affixes.suffix),)
    ),
  ))
return (
  util.Result(
    location=__env__.cwf_sect('adc061'),
    text=gen.cloze_text(table,
      states=await read.read_flashcard_states(__env__.cwf_sect('adc061')),
    ),
  ),
)
```

<!--pytextgen generate section="adc061"--><!-- The following content is generated at 2023-03-20T16:20:31.116658+08:00. Any edits will be overridden! -->

> | element | prefix | suffix |
> |-|-|-|
> | fluorine | {@{fluoro-}@} | {@{fluoride}@} |
> | chlorine | {@{chloro-}@} | {@{chloride}@} |
> | bromine | {@{bromo-}@} | {@{bromide}@} |
> | iodine | {@{iodo-}@} | {@{iodide}@} | <!--SR:!2030-01-01,2169,321!2027-06-10,1524,364!2029-08-18,2063,324!2027-07-17,1556,366!2029-01-05,1878,327!2029-07-16,2137,367!2030-07-08,2325,332!2028-10-14,1915,373-->

<!--/pytextgen-->

### precedence of functional groups

```Python
# pytextgen generate data
from pytextgen import gen, read, util
text: gen.TextCode = gen.seq_to_code((
  'cation',
  'carboxylic acid',
  'carboxylic acid derivative',
  'nitrile',
  'aldehyde',
  'ketone',
  'alcohol',
  'hydroperoxide',
  'amine',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(highest)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(lowest)_}}',)
return (
  util.Result(
    location=__env__.cwf_sect('19cfa2'),
    text=gen.quote_text(text),
  ),
  util.Result(
    location=__env__.cwf_sect('ad92c1'),
    text=gen.memorize_linked_seq(text,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('ad92c1')),
    ),
  ),
)
```

<!--pytextgen generate section="19cfa2"--><!-- The following content is generated at 2023-11-27T13:04:06.855552+08:00. Any edits will be overridden! -->

> 1. cation
> 2. carboxylic acid
> 3. carboxylic acid derivative
> 4. nitrile
> 5. aldehyde
> 6. ketone
> 7. alcohol
> 8. hydroperoxide
> 9. amine

<!--/pytextgen-->

<!--pytextgen generate section="ad92c1"--><!-- The following content is generated at 2024-01-04T20:17:52.277346+08:00. Any edits will be overridden! -->

- _(highest)_→::@::←cation <!--SR:!2025-04-25,813,324!2028-10-09,1910,372-->
- cation→::@::←carboxylic acid <!--SR:!2028-03-22,1421,275!2026-01-18,914,276-->
- carboxylic acid→::@::←carboxylic acid derivative <!--SR:!2028-08-04,1590,306!2026-10-25,1301,346-->
- carboxylic acid derivative→::@::←nitrile <!--SR:!2024-12-29,427,210!2025-06-24,292,247-->
- nitrile→::@::←aldehyde <!--SR:!2024-12-25,4,130!2025-05-14,154,190-->
- aldehyde→::@::←ketone <!--SR:!2026-12-29,1065,252!2025-10-08,305,230-->
- ketone→::@::←alcohol <!--SR:!2026-06-11,743,250!2025-01-11,52,150-->
- alcohol→::@::←hydroperoxide <!--SR:!2027-05-18,1057,226!2026-10-20,1068,272-->
- hydroperoxide→::@::←amine <!--SR:!2025-04-21,219,224!2025-02-02,257,252-->
- amine→::@::←_(lowest)_ <!--SR:!2025-04-28,532,236!2025-10-24,421,247-->

<!--/pytextgen-->

## trivial names

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('f91a', 'dd91'),
  ('trivial name', 'systematic name',),
  (
    ('[acetic acid](acetic%20acid.md)', 'ethanoic acid',),
    ('[acetone](acetone.md)', 'propanone',),
    ('[chloroform](chloroform.md)', 'trichloromethane',),
    ('[formaldehyde](formaldehyde.md)', 'methanal',),
    ('[isopropyl alcohol](isopropyl%20alochol.md)', 'propan-2-ol',),
  ),
  lambda datum: map(cloze, datum),
)
```

<!--pytextgen generate section="f91a"--><!-- The following content is generated at 2023-04-04T23:50:24.828005+08:00. Any edits will be overridden! -->

> | trivial name | systematic name |
> |-|-|
> | {@{[acetic acid](acetic%20acid.md)}@} | {@{ethanoic acid}@} |
> | {@{[acetone](acetone.md)}@} | {@{propanone}@} |
> | {@{[chloroform](chloroform.md)}@} | {@{trichloromethane}@} |
> | {@{[formaldehyde](formaldehyde.md)}@} | {@{methanal}@} |
> | {@{[isopropyl alcohol](isopropyl%20alochol.md)}@} | {@{propan-2-ol}@} | <!--SR:!2025-01-04,174,344!2025-08-15,625,344!2030-03-29,1924,384!2027-11-15,1262,384!2027-05-02,1102,364!2028-01-10,1273,364!2025-06-13,493,324!2027-08-06,1182,384!2026-10-12,956,364!2027-05-20,1116,364-->

<!--/pytextgen-->

<!--pytextgen generate section="dd91"--><!-- The following content is generated at 2024-01-04T20:17:52.316866+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[acetic acid](acetic%20acid.md) <!--SR:!2029-10-15,1799,384!2031-10-07,2510,404-->
- [acetic acid](acetic%20acid.md)→::@::←[acetone](acetone.md) <!--SR:!2026-06-28,862,364!2030-01-25,1877,384-->
- [acetone](acetone.md)→::@::←[chloroform](chloroform.md) <!--SR:!2027-03-26,1038,344!2025-11-25,553,364-->
- [chloroform](chloroform.md)→::@::←[formaldehyde](formaldehyde.md) <!--SR:!2026-03-22,482,344!2025-01-11,242,304-->
- [formaldehyde](formaldehyde.md)→::@::←[isopropyl alcohol](isopropyl%20alochol.md) <!--SR:!2025-04-07,336,324!2025-01-11,177,344-->
- [isopropyl alcohol](isopropyl%20alochol.md)→::@::←_(end)_ <!--SR:!2029-01-30,1604,384!2026-08-30,707,304-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/IUPAC_nomenclature_of_organic_chemistry) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
