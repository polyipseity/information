---
aliases:
  - IUPAC nomenclature of organic chemistry
tags:
  - academic/chemistry
  - flashcards/academic/Ii/IUPAC_nomenclature_of_organic_chemistry
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# IUPAC nomenclature of organic chemistry

The __IUPAC nomenclature of organic chemistry__ is {{a method of naming [organic compounds](organic%20compound.md)}}. There is also the [IUPAC nomenclature of inorganic chemistry](IUPAC%20nomenclature%20of%20inorganic%20chemistry.md).

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="48dca2"--><!-- The following content is generated at 2022-11-09T18:05:20.993142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)
2. [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)→:::←identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)
3. identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)→:::←identify side-chains
4. identify side-chains→:::←identify remaining functional groups
5. identify remaining functional groups→:::←identify multiple bonds
6. identify multiple bonds→:::←[identify numbering direction](#identify%20numbering%20direction)
7. [identify numbering direction](#identify%20numbering%20direction)→:::←number and [prefix](#prefix%20for%20type%20count) substituents and bonds
8. number and [prefix](#prefix%20for%20type%20count) substituents and bonds→:::←[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix
9. [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix→:::←(optional) omit unnecessary locants
10. (optional) omit unnecessary locants→:::←[modify words for pronunciation](#modify%20words%20for%20pronunciation)
11. [modify words for pronunciation](#modify%20words%20for%20pronunciation)→:::←[modify punctuations](#modify%20punctuations)
12. [modify punctuations](#modify%20punctuations)→:::←prefix notation for _cis_–_trans_ isomerism
13. prefix notation for _cis_–_trans_ isomerism→:::←_(end)_

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="920dca"--><!-- The following content is generated at 2022-11-09T18:05:21.025142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)
2. most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)→:::←most multiple bonds
3. most multiple bonds→:::←maximum length
4. maximum length→:::←most prefixes
5. most prefixes→:::←most single bonds
6. most single bonds→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### identify numbering direction

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10dacd"--><!-- The following content is generated at 2022-11-05T00:24:43.659370+08:00. Any edits will be overridden! -->

> 1. smallest locant for the suffix functional group
> 2. smallest locant for multiple bonds
> 3. smallest locant for prefixes

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="abacdf"--><!-- The following content is generated at 2022-11-09T18:05:21.058142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←smallest locant for the suffix functional group
2. smallest locant for the suffix functional group→:::←smallest locant for multiple bonds
3. smallest locant for multiple bonds→:::←smallest locant for prefixes
4. smallest locant for prefixes→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### arrange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab93dd"--><!-- The following content is generated at 2022-11-05T00:24:43.690374+08:00. Any edits will be overridden! -->

> 1. prefix order: alphabetical order ignoring prefixes for type count
> 2. bond order: single bond, double bond, triple bond, ...

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="828019"--><!-- The following content is generated at 2022-11-09T18:05:21.087142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←prefix order: alphabetical order ignoring prefixes for type count
2. prefix order: alphabetical order ignoring prefixes for type count→:::←bond order: single bond, double bond, triple bond, ...
3. bond order: single bond, double bond, triple bond, ...→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify words for pronunciation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299372"--><!-- The following content is generated at 2022-11-05T00:24:43.721370+08:00. Any edits will be overridden! -->

> - suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u): drop '-e'
> - bond suffix is followed by prefix for type count: keep '-e'
> - prefix for carbon count is followed by prefix for type count: add '-a'

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19fc21"--><!-- The following content is generated at 2022-11-06T20:13:24.211188+08:00. Any edits will be overridden! -->

1. suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u):::drop '-e'
2. bond suffix is followed by prefix for type count:::keep '-e'
3. prefix for carbon count is followed by prefix for type count:::add '-a'

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify punctuations

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a920de"--><!-- The following content is generated at 2022-11-05T00:24:43.754371+08:00. Any edits will be overridden! -->

> 1. commas (,) between locants
> 2. hyphens (-) between word and locant
> 3. remove (most) spaces ( )

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9293da"--><!-- The following content is generated at 2022-11-09T18:05:21.147143+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←commas (,) between locants
2. commas (,) between locants→:::←hyphens (-) between word and locant
3. hyphens (-) between word and locant→:::←remove (most) spaces ( )
4. remove (most) spaces ( )→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### prefix for type count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the first one is no prefix}}.

### prefix for carbon count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the last character _a-_ is trimmed away and the first four are _meth-_, _eth-_, _prop-_, and _but-_}}.

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
> - group: {{alkyl}}
> - formula: {{R(CH<sub>2</sub>)<sub>n</sub>H}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl-}}
> - suffix: {{-ane}}
> - infix: {{(none), (locant)}}
> - cyclic prefix: {{cyclo-}}

> {{alkene}}
> - group: {{alkenyl}}
> - formula: {{R<sub>2</sub>C=CR<sub>2</sub>}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-}}
> - suffix: {{-ene}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}}

> {{alkyne}}
> - group: {{alkynyl}}
> - formula: {{RC≡CR'}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-}}
> - suffix: {{-yne}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}}

> {{benzene derivative}}
> - group: {{phenyl}}
> - formula: {{RC<sub>6</sub>H<sub>5</sub>/RPh}}
> - prefix: {{phenyl-}}
> - suffix: {{-benzene}}
> - infix: {{(locant)}}

> {{([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane}}
> - group: {{([prefix for halogen](#affixes%20for%20halogen)), halo}}
> - formula: {{RX}}
> - prefix: {{([prefix for halogen](#affixes%20for%20halogen))-, halo-}}
> - suffix: {{([suffix for halogen](#affixes%20for%20halogen))}}
> - infix: {{(locant)}}

> {{alcohol}}
> - group: {{hydroxyl}}
> - formula: {{ROH}}
> - prefix: {{hydroxy-}}
> - suffix: {{-ol}}
> - infix: {{(locant)}}

> {{ether}}
> - group: {{ether}}
> - formula: {{ROR'}}
> - prefix: {{([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-)}}
> - suffix: {{ether}}
> - infix: {{(locant)}}

> {{aldehyde}}
> - group: {{aldehyde}}
> - formula: {{RCHO}}
> - prefix: {{oxo- (=O), formyl- (-CHO)}}
> - suffix: {{-al (=O), -carbaldehyde (-CHO)}}
> - infix: {{(locant)}}

> {{ketone}}
> - group: {{carbonyl}}
> - formula: {{RCOR'}}
> - prefix: {{oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR')}}
> - suffix: {{-one}}
> - infix: {{(locant)}}

> {{carboxylic acid}}
> - group: {{carboxyl}}
> - formula: {{RCOOH}}
> - prefix: {{carboxy-}}
> - suffix: {{-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)}}
> - infix: {{(locant)}}

> {{carboxylate}}
> - group: {{carboxylate}}
> - formula: {{RCOO<sup>-</sup>}}
> - prefix: {{carboxy-}}
> - suffix: {{-ate (retained), -oate}}
> - infix: {{(locant)}}

> {{alkanoyl}}
> - group: {{acyl}}
> - formula: {{RCO}}
> - prefix: {{(none)}}
> - suffix: {{-yl (retained), -oyl}}
> - infix: {{(locant)}}

> {{amine}}
> - group: {{amino}}
> - formula: {{RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>}}
> - prefix: {{amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>)}}
> - suffix: {{-amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>)}}
> - infix: {{(locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>)}}

> {{amide}}
> - group: {{amide}}
> - formula: {{RCONH<sub>2</sub>, RCONHR', RCONR'R''}}
> - prefix: {{amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)}}
> - suffix: {{-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)}}
> - infix: {{(locant) & _N_ (R', R'')}}

> {{nitrile}}
> - group: {{nitrile}}
> - formula: {{RCN}}
> - prefix: {{cyano-}}
> - suffix: {{-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)}}
> - infix: {{(locant)}}

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
> | iodine | {{iodo-}} | {{iodide}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### precedence of functional groups

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
text: gen.TextCode = gen.seq_to_code((
	'cation',
	'carboxylic acid',
	'carboxylic acid derivate',
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19cfa2"--><!-- The following content is generated at 2022-11-05T00:24:43.463369+08:00. Any edits will be overridden! -->

> 1. cation
> 2. carboxylic acid
> 3. carboxylic acid derivate
> 4. nitrile
> 5. aldehyde
> 6. ketone
> 7. alcohol
> 8. hydroperoxide
> 9. amine

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ad92c1"--><!-- The following content is generated at 2022-11-05T00:24:43.478367+08:00. Any edits will be overridden! -->

1. _(highest)_→:::←cation
2. cation→:::←carboxylic acid
3. carboxylic acid→:::←carboxylic acid derivate
4. carboxylic acid derivate→:::←nitrile
5. nitrile→:::←aldehyde
6. aldehyde→:::←ketone
7. ketone→:::←alcohol
8. alcohol→:::←hydroperoxide
9. hydroperoxide→:::←amine
10. amine→:::←_(lowest)_

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
> | {{[isopropyl alcohol](isopropyl%20alochol.md)}} | {{propan-2-ol}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd91"--><!-- The following content is generated at 2023-04-04T22:14:28.241195+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[acetic acid](acetic%20acid.md)
2. [acetic acid](acetic%20acid.md)→:::←[acetone](acetone.md)
3. [acetone](acetone.md)→:::←[chloroform](chloroform.md)
4. [chloroform](chloroform.md)→:::←[formaldehyde](formaldehyde.md)
5. [formaldehyde](formaldehyde.md)→:::←[isopropyl alcohol](isopropyl%20alochol.md)
6. [isopropyl alcohol](isopropyl%20alochol.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->