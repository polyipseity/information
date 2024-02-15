---
aliases:
  - IUPAC nomenclature of organic chemistry
tags:
  - flashcards/general/IUPAC_nomenclature_of_organic_chemistry
  - languages/in/English
---

# IUPAC nomenclature of organic chemistry

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

The __IUPAC nomenclature of organic chemistry__ is {{a method of naming [organic compounds](organic%20compound.md)}}. There is also the [IUPAC nomenclature of inorganic chemistry](IUPAC%20nomenclature%20of%20inorganic%20chemistry.md). <!--SR:!2024-05-26,342,363-->

## principles

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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
    'prefix order: alphabetical order ignoring prefixes for type count',
    'bond order: single bond, double bond, triple bond, ...',
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

%%

The steps for naming an organic compound are:
<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5193cd"--><!-- The following content is generated at 2022-11-05T00:24:43.599371+08:00. Any edits will be overridden! -->

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

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="48dca2"--><!-- The following content is generated at 2024-01-04T20:17:52.046217+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain) <!--SR:!2024-07-12,389,255!2026-02-20,924,345-->
- [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)→:::←identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2024-10-23,610,262!2024-09-16,507,325-->
- identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)→:::←identify side-chains <!--SR:!2024-07-10,387,264!2024-02-17,19,130-->
- identify side-chains→:::←identify remaining functional groups <!--SR:!2026-06-02,852,230!2024-03-01,238,227-->
- identify remaining functional groups→:::←identify multiple bonds <!--SR:!2024-05-09,145,190!2024-08-06,334,207-->
- identify multiple bonds→:::←[identify numbering direction](#identify%20numbering%20direction) <!--SR:!2024-05-26,239,230!2024-02-19,11,130-->
- [identify numbering direction](#identify%20numbering%20direction)→:::←number and [prefix](#prefix%20for%20type%20count) substituents and bonds <!--SR:!2024-06-17,305,190!2026-03-01,749,265-->
- number and [prefix](#prefix%20for%20type%20count) substituents and bonds→:::←[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix <!--SR:!2024-03-10,287,247!2024-12-25,360,230-->
- [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix→:::←(optional) omit unnecessary locants <!--SR:!2024-12-01,451,230!2024-04-03,101,227-->
- (optional) omit unnecessary locants→:::←[modify words for pronunciation](#modify%20words%20for%20pronunciation) <!--SR:!2024-08-07,335,230!2024-05-10,103,225-->
- [modify words for pronunciation](#modify%20words%20for%20pronunciation)→:::←[modify punctuations](#modify%20punctuations) <!--SR:!2024-07-27,602,312!2024-05-23,211,267-->
- [modify punctuations](#modify%20punctuations)→:::←prefix notation for _cis_–_trans_ isomerism <!--SR:!2024-05-05,413,273!2024-06-14,400,307-->
- prefix notation for _cis_–_trans_ isomerism→:::←_(end)_ <!--SR:!2024-03-20,398,362!2024-05-06,376,307-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### subprinciples

#### identify parent hydrocarbon chain

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="12cd9e"--><!-- The following content is generated at 2022-11-05T00:24:43.629369+08:00. Any edits will be overridden! -->

> 1. most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)
> 2. most multiple bonds
> 3. maximum length
> 4. most prefixes
> 5. most single bonds

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="920dca"--><!-- The following content is generated at 2024-01-04T20:17:52.176781+08:00. Any edits will be overridden! -->

- _(begin)_→:::←most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2024-05-22,507,256!2024-05-02,432,362-->
- most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)→:::←most multiple bonds <!--SR:!2024-06-21,526,256!2024-06-04,391,305-->
- most multiple bonds→:::←maximum length <!--SR:!2025-02-16,416,256!2025-10-04,690,282-->
- maximum length→:::←most prefixes <!--SR:!2025-01-19,580,261!2024-12-19,541,325-->
- most prefixes→:::←most single bonds <!--SR:!2024-05-11,501,261!2024-04-04,127,262-->
- most single bonds→:::←_(end)_ <!--SR:!2024-04-27,145,325!2025-03-21,668,345-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### identify numbering direction

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10dacd"--><!-- The following content is generated at 2022-11-05T00:24:43.659370+08:00. Any edits will be overridden! -->

> 1. smallest locant for the suffix functional group
> 2. smallest locant for multiple bonds
> 3. smallest locant for prefixes

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="abacdf"--><!-- The following content is generated at 2024-01-04T20:17:52.021214+08:00. Any edits will be overridden! -->

- _(begin)_→:::←smallest locant for the suffix functional group <!--SR:!2024-07-08,545,266!2024-05-06,433,362-->
- smallest locant for the suffix functional group→:::←smallest locant for multiple bonds <!--SR:!2024-06-27,537,266!2024-09-02,481,322-->
- smallest locant for multiple bonds→:::←smallest locant for prefixes <!--SR:!2028-02-06,1523,286!2026-02-13,908,345-->
- smallest locant for prefixes→:::←_(end)_ <!--SR:!2024-02-18,371,362!2024-05-21,381,305-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### arrange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab93dd"--><!-- The following content is generated at 2022-11-05T00:24:43.690374+08:00. Any edits will be overridden! -->

> 1. prefix order: alphabetical order ignoring prefixes for type count
> 2. bond order: single bond, double bond, triple bond, ...

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="828019"--><!-- The following content is generated at 2024-01-04T20:17:52.087770+08:00. Any edits will be overridden! -->

- _(begin)_→:::←prefix order: alphabetical order ignoring prefixes for type count <!--SR:!2024-02-21,247,230!2024-11-29,563,322-->
- prefix order: alphabetical order ignoring prefixes for type count→:::←bond order: single bond, double bond, triple bond, ... <!--SR:!2026-03-04,917,292!2024-05-29,104,267-->
- bond order: single bond, double bond, triple bond, ...→:::←_(end)_ <!--SR:!2026-01-10,880,340!2024-09-08,441,322-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify words for pronunciation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299372"--><!-- The following content is generated at 2022-11-05T00:24:43.721370+08:00. Any edits will be overridden! -->

> - suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u): drop '-e'
> - bond suffix is followed by prefix for type count: keep '-e'
> - prefix for carbon count is followed by prefix for type count: add '-a'

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19fc21"--><!-- The following content is generated at 2024-01-04T20:17:51.994215+08:00. Any edits will be overridden! -->

- suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u):::drop '-e' <!--SR:!2024-04-29,345,224!2024-11-08,626,267-->
- bond suffix is followed by prefix for type count:::keep '-e' <!--SR:!2024-04-13,475,250!2024-03-25,117,201-->
- prefix for carbon count is followed by prefix for type count:::add '-a' <!--SR:!2025-08-29,636,230!2024-06-11,211,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify punctuations

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a920de"--><!-- The following content is generated at 2022-11-05T00:24:43.754371+08:00. Any edits will be overridden! -->

> 1. commas (,) between locants
> 2. hyphens (-) between word and locant
> 3. remove (most) spaces ( )

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9293da"--><!-- The following content is generated at 2024-01-04T20:17:52.218337+08:00. Any edits will be overridden! -->

- _(begin)_→:::←commas (,) between locants <!--SR:!2025-05-09,838,332!2025-03-14,596,320-->
- commas (,) between locants→:::←hyphens (-) between word and locant <!--SR:!2027-12-20,1550,313!2024-09-15,436,321-->
- hyphens (-) between word and locant→:::←remove (most) spaces ( ) <!--SR:!2026-08-11,1244,353!2027-07-15,1340,362-->
- remove (most) spaces ( )→:::←_(end)_ <!--SR:!2024-04-06,410,367!2026-02-19,925,347-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### prefix for type count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the first one is no prefix}}. <!--SR:!2024-06-22,340,363-->

### prefix for carbon count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the last character _a-_ is trimmed away and the first four are _meth-_, _eth-_, _prop-_, and _but-_}}. <!--SR:!2026-01-18,747,343-->

## functional groups

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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
  Group(clazz='ketone', group='carbonyl', formula='RCOR\'', prefix='oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR\')', suffix='-one', infix='(locant)'),
  Group(clazz='carboxylic acid', group='carboxyl', formula='RCOOH', prefix='carboxy-', suffix='-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)', infix='(locant)'),
  Group(clazz='carboxylate', group='carboxylate', formula='RCOO<sup>-</sup>', prefix='carboxy-', suffix='-ate (retained), -oate', infix='(locant)',),
  Group(clazz='alkanoyl', group='acyl', formula='RCO', prefix='(none)', suffix='-yl (retained), -oyl', infix='(locant)',),
  Group(clazz='amine', group='amino', formula='RNH<sub>2</sub>, RR\'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>', prefix='amino- (RNH<sub>2</sub>/RR\'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>)', suffix='-amine (RNH<sub>2</sub>/RR\'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>)', infix='(locant) & _N_ (R\'/R\'\'/R<sub>3</sub>/R<sub>4</sub>)'),
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

%%

Use suffixes (starts with hyphen (-)) before prefixes. Only use one suffix. Bonds must use suffixes. Always add infixes.

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="28dcee"--><!-- The following content is generated at 2023-03-20T16:20:31.074684+08:00. Any edits will be overridden! -->

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
> | ketone | carbonyl | RCOR' | oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR') | -one | (locant) |  |
> | carboxylic acid | carboxyl | RCOOH | carboxy- | -ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH) | (locant) |  |
> | carboxylate | carboxylate | RCOO<sup>-</sup> | carboxy- | -ate (retained), -oate | (locant) |  |
> | alkanoyl | acyl | RCO | (none) | -yl (retained), -oyl | (locant) |  |
> | amine | amino | RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup> | amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>) | -amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>) | (locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>) |  |
> | amide | amide | RCONH<sub>2</sub>, RCONHR', RCONR'R'' | amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>) | -amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>) | (locant) & _N_ (R', R'') |  |
> | nitrile | nitrile | RCN | cyano- | -nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN) | (locant) |  |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a39fd2"--><!-- The following content is generated at 2022-11-04T23:41:04.458936+08:00. Any edits will be overridden! -->

> {{alkane}}
>
> - group: {{alkyl}}
> - formula: {{R(CH<sub>2</sub>)<sub>n</sub>H}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl-}}
> - suffix: {{-ane}}
> - infix: {{(none), (locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2024-04-09,412,368!2024-04-07,411,368!2024-12-06,523,348!2027-10-17,1405,368!2024-04-03,407,368!2026-09-16,1012,348!2024-04-04,408,368-->

<!-- markdownlint MD028 -->

> {{alkene}}
>
> - group: {{alkenyl}}
> - formula: {{R<sub>2</sub>C=CR<sub>2</sub>}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-}}
> - suffix: {{-ene}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2024-02-17,370,360!2024-05-07,437,362!2027-04-03,1256,362!2026-07-29,935,302!2024-05-02,430,362!2024-04-30,428,362!2025-03-06,644,327-->

<!-- markdownlint MD028 -->

> {{alkyne}}
>
> - group: {{alkynyl}}
> - formula: {{RC≡CR'}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-}}
> - suffix: {{-yne}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2026-02-11,918,340!2025-03-16,649,320!2024-04-28,426,360!2025-09-25,682,281!2024-05-31,456,362!2024-02-19,372,362!2026-10-21,1140,367-->

<!-- markdownlint MD028 -->

> {{benzene derivative}}
>
> - group: {{phenyl}}
> - formula: {{RC<sub>6</sub>H<sub>5</sub>/RPh}}
> - prefix: {{phenyl-}}
> - suffix: {{-benzene}}
> - infix: {{(locant)}} <!--SR:!2024-06-29,406,300!2025-06-11,723,340!2027-07-13,1326,362!2026-12-12,1177,362!2024-05-22,383,302!2026-10-01,1023,347-->

<!-- markdownlint MD028 -->

> {{([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane}}
>
> - group: {{([prefix for halogen](#affixes%20for%20halogen)), halo}}
> - formula: {{RX}}
> - prefix: {{([prefix for halogen](#affixes%20for%20halogen))-, halo-}}
> - suffix: {{([suffix for halogen](#affixes%20for%20halogen))}}
> - infix: {{(locant)}} <!--SR:!2026-11-16,1064,320!2025-06-25,688,321!2024-05-26,453,362!2024-03-06,353,302!2026-04-24,903,305!2024-04-27,428,367-->

<!-- markdownlint MD028 -->

> {{alcohol}}
>
> - group: {{hydroxyl}}
> - formula: {{ROH}}
> - prefix: {{hydroxy-}}
> - suffix: {{-ol}}
> - infix: {{(locant)}} <!--SR:!2024-05-06,436,362!2024-05-03,431,362!2024-05-28,453,362!2024-03-28,401,365!2027-08-18,1353,365!2024-04-01,405,367-->

<!-- markdownlint MD028 -->

> {{ether}}
>
> - group: {{ether}}
> - formula: {{ROR'}}
> - prefix: {{([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-)}}
> - suffix: {{ether}}
> - infix: {{(locant)}} <!--SR:!2024-04-26,427,360!2024-04-27,425,362!2024-02-20,373,362!2024-08-08,211,210!2026-02-24,925,345!2028-09-02,1699,387-->

<!-- markdownlint MD028 -->

> {{aldehyde}}
>
> - group: {{aldehyde}}
> - formula: {{RCHO}}
> - prefix: {{oxo- (=O), formyl- (-CHO)}}
> - suffix: {{-al (=O), -carbaldehyde (-CHO)}}
> - infix: {{(locant)}} <!--SR:!2024-02-21,374,362!2028-01-06,1463,362!2025-01-20,605,322!2024-02-24,21,130!2025-09-10,677,285!2028-10-10,1730,387-->

<!-- markdownlint MD028 -->

> {{ketone}}
>
> - group: {{carbonyl}}
> - formula: {{RCOR'}}
> - prefix: {{oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR')}}
> - suffix: {{-one}}
> - infix: {{(locant)}} <!--SR:!2025-12-23,823,300!2024-06-28,295,280!2025-03-13,595,321!2024-02-21,21,130!2024-06-02,458,362!2024-05-01,429,362-->

<!-- markdownlint MD028 -->

> {{carboxylic acid}}
>
> - group: {{carboxyl}}
> - formula: {{RCOOH}}
> - prefix: {{carboxy-}}
> - suffix: {{-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)}}
> - infix: {{(locant)}} <!--SR:!2025-08-29,784,340!2024-11-03,544,322!2024-04-29,427,362!2024-12-13,543,322!2024-03-05,317,305!2024-04-02,406,367-->

<!-- markdownlint MD028 -->

> {{carboxylate}}
>
> - group: {{carboxylate}}
> - formula: {{RCOO<sup>-</sup>}}
> - prefix: {{carboxy-}}
> - suffix: {{-ate (retained), -oate}}
> - infix: {{(locant)}} <!--SR:!2024-02-16,369,362!2024-04-25,426,362!2024-04-21,423,362!2025-11-12,732,282!2026-01-09,832,302!2028-12-05,1775,387-->

<!-- markdownlint MD028 -->

> {{alkanoyl}}
>
> - group: {{acyl}}
> - formula: {{RCO}}
> - prefix: {{(none)}}
> - suffix: {{-yl (retained), -oyl}}
> - infix: {{(locant)}} <!--SR:!2024-06-17,405,281!2024-06-28,147,282!2024-05-25,452,362!2024-10-16,314,222!2024-06-14,252,227!2024-04-22,424,367-->

<!-- markdownlint MD028 -->

> {{amine}}
>
> - group: {{amino}}
> - formula: {{RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>}}
> - prefix: {{amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>)}}
> - suffix: {{-amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>)}}
> - infix: {{(locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>)}} <!--SR:!2027-03-08,1174,365!2024-03-24,397,365!2025-02-17,627,325!2024-11-18,518,325!2024-10-03,419,287!2025-06-09,664,327-->

<!-- markdownlint MD028 -->

> {{amide}}
>
> - group: {{amide}}
> - formula: {{RCONH<sub>2</sub>, RCONHR', RCONR'R''}}
> - prefix: {{amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)}}
> - suffix: {{-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)}}
> - infix: {{(locant) & _N_ (R', R'')}} <!--SR:!2026-08-17,1073,365!2024-03-25,398,365!2026-05-02,984,345!2026-01-13,733,285!2026-04-27,911,305!2027-08-26,1378,367-->

<!-- markdownlint MD028 -->

> {{nitrile}}
>
> - group: {{nitrile}}
> - formula: {{RCN}}
> - prefix: {{cyano-}}
> - suffix: {{-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)}}
> - infix: {{(locant)}} <!--SR:!2024-04-23,425,368!2027-10-13,1401,368!2024-04-08,411,368!2026-03-30,958,348!2025-07-18,623,268!2024-04-14,417,368-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### affixes for halogen

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="adc061"--><!-- The following content is generated at 2023-03-20T16:20:31.116658+08:00. Any edits will be overridden! -->

> | element | prefix | suffix |
> |-|-|-|
> | fluorine | {{fluoro-}} | {{fluoride}} |
> | chlorine | {{chloro-}} | {{chloride}} |
> | bromine | {{bromo-}} | {{bromide}} |
> | iodine | {{iodo-}} | {{iodide}} | <!--SR:!2030-01-01,2169,321!2027-06-10,1524,364!2029-08-18,2063,324!2027-07-17,1556,366!2029-01-05,1878,327!2029-07-16,2137,367!2024-02-25,539,312!2028-10-14,1915,373-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### precedence of functional groups

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19cfa2"--><!-- The following content is generated at 2023-11-27T13:04:06.855552+08:00. Any edits will be overridden! -->

> 1. cation
> 2. carboxylic acid
> 3. carboxylic acid derivative
> 4. nitrile
> 5. aldehyde
> 6. ketone
> 7. alcohol
> 8. hydroperoxide
> 9. amine

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ad92c1"--><!-- The following content is generated at 2024-01-04T20:17:52.277346+08:00. Any edits will be overridden! -->

- _(highest)_→:::←cation <!--SR:!2025-04-25,813,324!2028-10-09,1910,372-->
- cation→:::←carboxylic acid <!--SR:!2024-05-01,517,275!2026-01-18,914,276-->
- carboxylic acid→:::←carboxylic acid derivative <!--SR:!2024-03-27,520,306!2026-10-25,1301,346-->
- carboxylic acid derivative→:::←nitrile <!--SR:!2024-12-29,427,210!2024-09-05,585,267-->
- nitrile→:::←aldehyde <!--SR:!2024-05-15,194,210!2024-05-11,181,230-->
- aldehyde→:::←ketone <!--SR:!2026-12-29,1065,252!2024-12-06,598,250-->
- ketone→:::←alcohol <!--SR:!2024-05-29,229,230!2024-03-10,42,130-->
- alcohol→:::←hydroperoxide <!--SR:!2024-06-25,468,226!2026-10-20,1068,272-->
- hydroperoxide→:::←amine <!--SR:!2024-06-08,197,244!2024-05-21,515,272-->
- amine→:::←_(lowest)_ <!--SR:!2025-04-28,532,236!2024-03-10,343,267-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## trivial names

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
  e.cwf_sects('f91a', 'dd91'),
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f91a"--><!-- The following content is generated at 2023-04-04T23:50:24.828005+08:00. Any edits will be overridden! -->

> | trivial name | systematic name |
> |-|-|
> | {{[acetic acid](acetic%20acid.md)}} | {{ethanoic acid}} |
> | {{[acetone](acetone.md)}} | {{propanone}} |
> | {{[chloroform](chloroform.md)}} | {{trichloromethane}} |
> | {{[formaldehyde](formaldehyde.md)}} | {{methanal}} |
> | {{[isopropyl alcohol](isopropyl%20alochol.md)}} | {{propan-2-ol}} | <!--SR:!2024-07-14,349,364!2025-08-15,625,344!2024-12-20,501,384!2024-06-01,253,364!2024-04-25,303,364!2024-07-16,350,364!2025-06-13,493,324!2024-05-10,237,364!2024-02-29,263,364!2024-04-29,307,364-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd91"--><!-- The following content is generated at 2024-01-04T20:17:52.316866+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[acetic acid](acetic%20acid.md) <!--SR:!2024-11-11,469,384!2024-11-22,478,384-->
- [acetic acid](acetic%20acid.md)→:::←[acetone](acetone.md) <!--SR:!2024-02-17,237,364!2024-12-05,489,384-->
- [acetone](acetone.md)→:::←[chloroform](chloroform.md) <!--SR:!2024-05-22,302,344!2024-05-20,117,344-->
- [chloroform](chloroform.md)→:::←[formaldehyde](formaldehyde.md) <!--SR:!2024-07-08,282,364!2024-02-24,162,324-->
- [formaldehyde](formaldehyde.md)→:::←[isopropyl alcohol](isopropyl%20alochol.md) <!--SR:!2024-05-06,104,324!2024-07-17,351,364-->
- [isopropyl alcohol](isopropyl%20alochol.md)→:::←_(end)_ <!--SR:!2024-09-09,418,384!2024-09-20,233,304-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/IUPAC_nomenclature_of_organic_chemistry) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
