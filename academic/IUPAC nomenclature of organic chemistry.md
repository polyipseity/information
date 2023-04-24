---
aliases:
  - IUPAC nomenclature of organic chemistry
---

#academic/chemistry #flashcards/academic/Ii/IUPAC_nomenclature_of_organic_chemistry

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# IUPAC nomenclature of organic chemistry

The __IUPAC nomenclature of organic chemistry__ is {{a method of naming [organic compounds](organic%20compound.md)}}. There is also the [IUPAC nomenclature of inorganic chemistry](IUPAC%20nomenclature%20of%20inorganic%20chemistry.md). <!--SR:!2023-06-16,69,343-->

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

1. _(begin)_→:::←[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain) <!--SR:!2023-06-14,118,235!2023-08-11,197,325-->
2. [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)→:::←identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2024-10-23,610,262!2023-04-28,120,305-->
3. identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)→:::←identify side-chains <!--SR:!2023-06-18,117,244!2023-04-29,15,130-->
4. identify side-chains→:::←identify remaining functional groups <!--SR:!2024-02-01,371,230!2023-07-05,104,227-->
5. identify remaining functional groups→:::←identify multiple bonds <!--SR:!2023-04-27,70,210!2023-09-06,154,207-->
6. identify multiple bonds→:::←[identify numbering direction](#identify%20numbering%20direction) <!--SR:!2023-05-07,16,230!2023-05-19,41,227-->
7. [identify numbering direction](#identify%20numbering%20direction)→:::←number and [prefix](#prefix%20for%20type%20count) substituents and bonds <!--SR:!2023-08-17,154,190!2023-05-04,102,265-->
8. number and [prefix](#prefix%20for%20type%20count) substituents and bonds→:::←[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix <!--SR:!2023-05-28,116,247!2023-05-20,28,230-->
9. [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix→:::←(optional) omit unnecessary locants <!--SR:!2023-09-03,191,230!2023-08-09,178,267-->
10. (optional) omit unnecessary locants→:::←[modify words for pronunciation](#modify%20words%20for%20pronunciation) <!--SR:!2023-09-04,144,230!2023-08-31,191,265-->
11. [modify words for pronunciation](#modify%20words%20for%20pronunciation)→:::←[modify punctuations](#modify%20punctuations) <!--SR:!2024-07-27,602,312!2023-08-20,118,267-->
12. [modify punctuations](#modify%20punctuations)→:::←prefix notation for _cis_–_trans_ isomerism <!--SR:!2024-05-05,413,273!2023-05-11,130,307-->
13. prefix notation for _cis_–_trans_ isomerism→:::←_(end)_ <!--SR:!2024-03-20,398,362!2023-04-26,118,307-->

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

1. _(begin)_→:::←most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2024-05-22,507,256!2024-05-02,432,362-->
2. most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)→:::←most multiple bonds <!--SR:!2024-06-21,526,256!2023-05-10,129,305-->
3. most multiple bonds→:::←maximum length <!--SR:!2023-07-12,324,276!2023-11-14,245,282-->
4. maximum length→:::←most prefixes <!--SR:!2023-06-17,169,241!2023-06-26,168,325-->
5. most prefixes→:::←most single bonds <!--SR:!2024-05-11,501,261!2023-11-27,256,282-->
6. most single bonds→:::←_(end)_ <!--SR:!2023-12-04,286,345!2023-05-21,147,325-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### identify numbering direction

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10dacd"--><!-- The following content is generated at 2022-11-05T00:24:43.659370+08:00. Any edits will be overridden! -->

> 1. smallest locant for the suffix functional group
> 2. smallest locant for multiple bonds
> 3. smallest locant for prefixes

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="abacdf"--><!-- The following content is generated at 2022-11-09T18:05:21.058142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←smallest locant for the suffix functional group <!--SR:!2024-07-08,545,266!2024-05-06,433,362-->
2. smallest locant for the suffix functional group→:::←smallest locant for multiple bonds <!--SR:!2024-06-27,537,266!2023-05-10,115,302-->
3. smallest locant for multiple bonds→:::←smallest locant for prefixes <!--SR:!2023-12-06,410,266!2023-08-19,202,325-->
4. smallest locant for prefixes→:::←_(end)_ <!--SR:!2024-02-18,371,362!2023-05-06,125,305-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### arrange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab93dd"--><!-- The following content is generated at 2022-11-05T00:24:43.690374+08:00. Any edits will be overridden! -->

> 1. prefix order: alphabetical order ignoring prefixes for type count
> 2. bond order: single bond, double bond, triple bond, ...

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="828019"--><!-- The following content is generated at 2022-11-09T18:05:21.087142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←prefix order: alphabetical order ignoring prefixes for type count <!--SR:!2023-06-16,101,230!2023-05-15,133,302-->
2. prefix order: alphabetical order ignoring prefixes for type count→:::←bond order: single bond, double bond, triple bond, ... <!--SR:!2023-08-30,314,292!2023-05-13,132,307-->
3. bond order: single bond, double bond, triple bond, ...→:::←_(end)_ <!--SR:!2023-08-12,196,320!2023-06-21,106,302-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify words for pronunciation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299372"--><!-- The following content is generated at 2022-11-05T00:24:43.721370+08:00. Any edits will be overridden! -->

> - suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u): drop '-e'
> - bond suffix is followed by prefix for type count: keep '-e'
> - prefix for carbon count is followed by prefix for type count: add '-a'

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19fc21"--><!-- The following content is generated at 2022-11-06T20:13:24.211188+08:00. Any edits will be overridden! -->

1. suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u):::drop '-e' <!--SR:!2023-05-20,147,224!2024-11-08,626,267-->
2. bond suffix is followed by prefix for type count:::keep '-e' <!--SR:!2024-04-13,475,250!2023-05-31,69,221-->
3. prefix for carbon count is followed by prefix for type count:::add '-a' <!--SR:!2023-05-03,101,210!2023-08-04,201,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify punctuations

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a920de"--><!-- The following content is generated at 2022-11-05T00:24:43.754371+08:00. Any edits will be overridden! -->

> 1. commas (,) between locants
> 2. hyphens (-) between word and locant
> 3. remove (most) spaces ( )

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9293da"--><!-- The following content is generated at 2022-11-09T18:05:21.147143+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←commas (,) between locants <!--SR:!2025-05-09,838,332!2023-07-27,186,320-->
2. commas (,) between locants→:::←hyphens (-) between word and locant <!--SR:!2023-09-18,377,293!2023-07-07,136,321-->
3. hyphens (-) between word and locant→:::←remove (most) spaces ( ) <!--SR:!2026-08-11,1244,353!2023-11-13,285,342-->
4. remove (most) spaces ( )→:::←_(end)_ <!--SR:!2024-04-06,410,367!2023-08-09,196,327-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### prefix for type count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the first one is no prefix}}. <!--SR:!2023-07-15,92,363-->

### prefix for carbon count

See [IUPAC numerical multiplier § data](IUPAC%20numerical%20multiplier.md#data) except that {{the last character _a-_ is trimmed away and the first four are _meth-_, _eth-_, _prop-_, and _but-_}}. <!--SR:!2023-05-27,48,323-->

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
> - cyclic prefix: {{cyclo-}} <!--SR:!2024-04-09,412,368!2024-04-07,411,368!2023-07-01,115,328!2023-12-12,294,348!2024-04-03,407,368!2023-12-09,291,348!2024-04-04,408,368-->

> {{alkene}}
> - group: {{alkenyl}}
> - formula: {{R<sub>2</sub>C=CR<sub>2</sub>}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-}}
> - suffix: {{-ene}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2024-02-17,370,360!2024-05-07,437,362!2023-10-18,267,342!2024-01-06,310,302!2024-05-02,430,362!2024-04-30,428,362!2023-06-01,145,307-->

> {{alkyne}}
> - group: {{alkynyl}}
> - formula: {{RC≡CR'}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-}}
> - suffix: {{-yne}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2023-08-08,198,320!2023-06-06,156,300!2024-04-28,426,360!2023-11-13,243,281!2024-05-31,456,362!2024-02-19,372,362!2023-09-04,236,347-->

> {{benzene derivative}}
> - group: {{phenyl}}
> - formula: {{RC<sub>6</sub>H<sub>5</sub>/RPh}}
> - prefix: {{phenyl-}}
> - suffix: {{-benzene}}
> - infix: {{(locant)}} <!--SR:!2023-05-20,133,300!2023-06-16,159,320!2023-11-25,282,342!2023-09-21,249,342!2023-05-05,127,302!2023-12-13,295,347-->

> {{([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane}}
> - group: {{([prefix for halogen](#affixes%20for%20halogen)), halo}}
> - formula: {{RX}}
> - prefix: {{([prefix for halogen](#affixes%20for%20halogen))-, halo-}}
> - suffix: {{([suffix for halogen](#affixes%20for%20halogen))}}
> - infix: {{(locant)}} <!--SR:!2023-12-18,256,300!2023-08-06,171,301!2024-05-26,453,362!2024-03-06,353,302!2023-10-31,228,285!2024-04-27,428,367-->

> {{alcohol}}
> - group: {{hydroxyl}}
> - formula: {{ROH}}
> - prefix: {{hydroxy-}}
> - suffix: {{-ol}}
> - infix: {{(locant)}} <!--SR:!2024-05-06,436,362!2024-05-03,431,362!2024-05-28,453,362!2024-03-28,401,365!2023-12-03,285,345!2024-04-01,405,367-->

> {{ether}}
> - group: {{ether}}
> - formula: {{ROR'}}
> - prefix: {{([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-)}}
> - suffix: {{ether}}
> - infix: {{(locant)}} <!--SR:!2024-04-26,427,360!2024-04-27,425,362!2024-02-20,373,362!2023-04-25,56,202!2023-08-13,197,325!2024-01-08,338,367-->

> {{aldehyde}}
> - group: {{aldehyde}}
> - formula: {{RCHO}}
> - prefix: {{oxo- (=O), formyl- (-CHO)}}
> - suffix: {{-al (=O), -carbaldehyde (-CHO)}}
> - infix: {{(locant)}} <!--SR:!2024-02-21,374,362!2024-01-04,311,342!2023-05-26,139,302!2023-05-01,7,130!2023-11-02,238,285!2024-01-15,344,367-->

> {{ketone}}
> - group: {{carbonyl}}
> - formula: {{RCOR'}}
> - prefix: {{oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR')}}
> - suffix: {{-one}}
> - infix: {{(locant)}} <!--SR:!2023-09-18,207,280!2023-06-17,148,280!2023-07-26,185,321!2023-05-03,14,142!2024-06-02,458,362!2024-05-01,429,362-->

> {{carboxylic acid}}
> - group: {{carboxyl}}
> - formula: {{RCOOH}}
> - prefix: {{carboxy-}}
> - suffix: {{-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)}}
> - infix: {{(locant)}} <!--SR:!2023-07-05,173,320!2023-05-09,130,302!2024-04-29,427,362!2023-06-14,166,322!2024-03-05,317,305!2024-04-02,406,367-->

> {{carboxylate}}
> - group: {{carboxylate}}
> - formula: {{RCOO<sup>-</sup>}}
> - prefix: {{carboxy-}}
> - suffix: {{-ate (retained), -oate}}
> - infix: {{(locant)}} <!--SR:!2024-02-16,369,362!2024-04-25,426,362!2024-04-21,423,362!2023-11-11,260,282!2023-09-25,207,282!2024-01-26,353,367-->

> {{alkanoyl}}
> - group: {{acyl}}
> - formula: {{RCO}}
> - prefix: {{(none)}}
> - suffix: {{-yl (retained), -oyl}}
> - infix: {{(locant)}} <!--SR:!2023-05-09,111,261!2024-02-02,295,302!2024-05-25,452,362!2023-05-10,110,242!2023-04-30,18,227!2024-04-22,424,367-->

> {{amine}}
> - group: {{amino}}
> - formula: {{RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>}}
> - prefix: {{amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>)}}
> - suffix: {{-amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>)}}
> - infix: {{(locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>)}} <!--SR:!2023-12-20,322,365!2024-03-24,397,365!2023-06-01,143,305!2023-06-14,157,325!2023-08-11,112,267!2023-08-15,203,327-->

> {{amide}}
> - group: {{amide}}
> - formula: {{RCONH<sub>2</sub>, RCONHR', RCONR'R''}}
> - prefix: {{amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)}}
> - suffix: {{-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)}}
> - infix: {{(locant) & _N_ (R', R'')}} <!--SR:!2023-09-08,223,345!2024-03-25,398,365!2023-08-22,210,325!2023-05-01,21,245!2023-10-26,230,285!2023-11-16,289,347-->

> {{nitrile}}
> - group: {{nitrile}}
> - formula: {{RCN}}
> - prefix: {{cyano-}}
> - suffix: {{-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)}}
> - infix: {{(locant)}} <!--SR:!2024-04-23,425,368!2023-12-11,293,348!2024-04-08,411,368!2023-08-15,205,328!2023-05-07,69,248!2024-04-14,417,368-->

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
> | iodine | {{iodo-}} | {{iodide}} | <!--SR:!2024-01-24,520,301!2027-06-10,1524,364!2023-12-25,490,304!2027-07-17,1556,366!2023-11-15,442,307!2023-09-08,447,347!2024-02-25,539,312!2023-07-18,395,353-->

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

1. _(highest)_→:::←cation <!--SR:!2025-04-25,813,324!2023-07-17,394,352-->
2. cation→:::←carboxylic acid <!--SR:!2024-05-01,517,275!2023-07-19,331,276-->
3. carboxylic acid→:::←carboxylic acid derivate <!--SR:!2024-03-27,520,306!2026-10-25,1301,346-->
4. carboxylic acid derivate→:::←nitrile <!--SR:!2023-10-27,204,210!2024-09-05,585,267-->
5. nitrile→:::←aldehyde <!--SR:!2023-07-31,177,230!2023-11-12,364,250-->
6. aldehyde→:::←ketone <!--SR:!2024-01-29,423,252!2024-12-06,598,250-->
7. ketone→:::←alcohol <!--SR:!2023-04-26,2,230!2023-05-21,59,170-->
8. alcohol→:::←hydroperoxide <!--SR:!2024-06-25,468,226!2023-11-17,393,272-->
9. hydroperoxide→:::←amine <!--SR:!2023-11-20,396,264!2024-05-21,515,272-->
10. amine→:::←_(lowest)_ <!--SR:!2023-11-13,226,236!2024-03-10,343,267-->

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
> | {{[isopropyl alcohol](isopropyl%20alochol.md)}} | {{propan-2-ol}} | <!--SR:!2023-04-27,19,344!2023-05-29,40,324!2023-04-28,20,344!2023-04-28,20,344!2023-04-26,18,344!2023-04-28,20,344!2023-04-27,18,324!2023-04-27,19,344!2023-06-08,50,344!2023-04-26,18,344-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd91"--><!-- The following content is generated at 2023-04-04T22:14:28.241195+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[acetic acid](acetic%20acid.md) <!--SR:!2023-04-28,20,344!2023-04-27,19,344-->
2. [acetic acid](acetic%20acid.md)→:::←[acetone](acetone.md) <!--SR:!2023-04-26,18,344!2023-04-27,19,344-->
3. [acetone](acetone.md)→:::←[chloroform](chloroform.md) <!--SR:!2023-04-28,19,324!2023-06-07,49,344-->
4. [chloroform](chloroform.md)→:::←[formaldehyde](formaldehyde.md) <!--SR:!2023-04-27,19,344!2023-04-28,19,324-->
5. [formaldehyde](formaldehyde.md)→:::←[isopropyl alcohol](isopropyl%20alochol.md) <!--SR:!2023-04-26,18,344!2023-04-28,20,344-->
6. [isopropyl alcohol](isopropyl%20alochol.md)→:::←_(end)_ <!--SR:!2023-04-26,18,344!2023-04-27,10,304-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
