#flashcards/chemistry/IUPAC_nomenclature_of_organic_chemistry #academic/chemistry

# IUPAC nomenclature of organic chemistry

## principles

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
principles: gen.TextCode = gen.common.seq_to_code((
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
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
id_parent: gen.TextCode = gen.common.seq_to_code((
		'most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)',
		'most multiple bonds',
		'maximum length',
		'most prefixes',
		'most single bonds',
	),
	index=1,
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
id_num_dir: gen.TextCode = gen.common.seq_to_code((
		'smallest locant for the suffix functional group',
		'smallest locant for multiple bonds',
		'smallest locant for prefixes',
	),
	index=1,
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
arrange: gen.TextCode = gen.common.seq_to_code((
		'prefix order: alphabetical order ignoring prefixes for type count',
		'bond order: single bond, double bond, triple bond, ...',
	),
	index=1,
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
pronuciations: gen.TextCode = gen.TextCode.compile(
	R'''{text:- }suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u){text:\: }drop '-e'{text:
- }bond suffix is followed by prefix for type count{text:\: }keep '-e'{text:
- }prefix for carbon count is followed by prefix for type count{text:\: }add '-a'{}'''
)
punctuations: gen.TextCode = gen.common.seq_to_code((
		'commas (,) between locants',
		'hyphens (-) between word and locant',
		'remove (most) spaces ( )',
	),
	index=1,
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('5193cd'),
		text=gen.common.quote_text(principles),
	),
	gen.Result(
		location=__env__.cwf_section('48dca2'),
		text=gen.common.memorize_linked_seq(principles,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('48dca2')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('12cd9e'),
		text=gen.common.quote_text(id_parent),
	),
	gen.Result(
		location=__env__.cwf_section('920dca'),
		text=gen.common.memorize_linked_seq(id_parent,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('920dca')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('10dacd'),
		text=gen.common.quote_text(id_num_dir),
	),
	gen.Result(
		location=__env__.cwf_section('abacdf'),
		text=gen.common.memorize_linked_seq(id_num_dir,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('abacdf')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('ab93dd'),
		text=gen.common.quote_text(arrange),
	),
	gen.Result(
		location=__env__.cwf_section('828019'),
		text=gen.common.memorize_linked_seq(arrange,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('828019')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('299372'),
		text=gen.common.quote_text(pronuciations),
	),
	gen.Result(
		location=__env__.cwf_section('19fc21'),
		text=gen.common.memorize_two_sided(pronuciations,
			states=read.read_flashcard_states(__env__.cwf_section('19fc21')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('a920de'),
		text=gen.common.quote_text(punctuations),
	),
	gen.Result(
		location=__env__.cwf_section('9293da'),
		text=gen.common.memorize_linked_seq(punctuations,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('9293da')),
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

1. _(begin)_→:::←[identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain) <!--SR:!2023-02-15,229,255!2023-01-26,59,325-->
2. [identify parent hydrocarbon chain](#identify%20parent%20hydrocarbon%20chain)→:::←identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2023-02-17,231,262!2022-12-28,38,305-->
3. identify parent functional group of [highest group precedence](#precedence%20of%20functional%20groups)→:::←identify side-chains <!--SR:!2023-02-19,233,264!2023-01-04,13,245-->
4. identify side-chains→:::←identify remaining functional groups <!--SR:!2023-01-26,157,230!2023-01-17,34,247-->
5. identify remaining functional groups→:::←identify multiple bonds <!--SR:!2023-01-11,59,230!2023-01-23,33,207-->
6. identify multiple bonds→:::←[identify numbering direction](#identify%20numbering%20direction) <!--SR:!2023-01-02,198,266!2023-02-13,64,267-->
7. [identify numbering direction](#identify%20numbering%20direction)→:::←number and [prefix](#prefix%20for%20type%20count) substituents and bonds <!--SR:!2023-03-16,79,190!2023-01-22,38,265-->
8. number and [prefix](#prefix%20for%20type%20count) substituents and bonds→:::←[arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix <!--SR:!2023-02-01,221,267!2023-01-14,39,247-->
9. [arrange](#arrange): prefix(es) + [prefix for carbon count](#prefix%20for%20carbon%20count) + bond(s) + suffix→:::←(optional) omit unnecessary locants <!--SR:!2023-02-24,79,230!2023-02-10,63,267-->
10. (optional) omit unnecessary locants→:::←[modify words for pronunciation](#modify%20words%20for%20pronunciation) <!--SR:!2023-02-12,115,250!2023-02-19,68,265-->
11. [modify words for pronunciation](#modify%20words%20for%20pronunciation)→:::←[modify punctuations](#modify%20punctuations) <!--SR:!2024-07-27,602,312!2023-03-11,85,287-->
12. [modify punctuations](#modify%20punctuations)→:::←prefix notation for _cis_–_trans_ isomerism <!--SR:!2023-03-19,150,273!2023-01-01,41,307-->
13. prefix notation for _cis_–_trans_ isomerism→:::←_(end)_ <!--SR:!2023-02-13,80,342!2022-12-28,38,307-->

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

1. _(begin)_→:::←most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups) <!--SR:!2023-01-01,197,256!2023-02-25,89,342-->
2. most suffix functional groups of [highest group precedence](#precedence%20of%20functional%20groups)→:::←most multiple bonds <!--SR:!2023-01-12,205,256!2023-01-01,41,305-->
3. most multiple bonds→:::←maximum length <!--SR:!2023-07-12,324,276!2023-03-14,87,282-->
4. maximum length→:::←most prefixes <!--SR:!2022-12-30,71,241!2023-01-09,50,325-->
5. most prefixes→:::←most single bonds <!--SR:!2024-05-11,501,261!2023-03-16,88,282-->
6. most single bonds→:::←_(end)_ <!--SR:!2023-02-17,81,345!2023-05-21,147,325-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### identify numbering direction

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10dacd"--><!-- The following content is generated at 2022-11-05T00:24:43.659370+08:00. Any edits will be overridden! -->

> 1. smallest locant for the suffix functional group
> 2. smallest locant for multiple bonds
> 3. smallest locant for prefixes

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="abacdf"--><!-- The following content is generated at 2022-11-09T18:05:21.058142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←smallest locant for the suffix functional group <!--SR:!2023-01-10,205,266!2023-02-28,92,342-->
2. smallest locant for the suffix functional group→:::←smallest locant for multiple bonds <!--SR:!2023-01-05,201,266!2023-01-15,37,302-->
3. smallest locant for multiple bonds→:::←smallest locant for prefixes <!--SR:!2023-12-06,410,266!2023-01-29,62,325-->
4. smallest locant for prefixes→:::←_(end)_ <!--SR:!2023-02-11,78,342!2023-01-01,41,305-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### arrange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ab93dd"--><!-- The following content is generated at 2022-11-05T00:24:43.690374+08:00. Any edits will be overridden! -->

> 1. prefix order: alphabetical order ignoring prefixes for type count
> 2. bond order: single bond, double bond, triple bond, ...

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="828019"--><!-- The following content is generated at 2022-11-09T18:05:21.087142+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←prefix order: alphabetical order ignoring prefixes for type count <!--SR:!2023-03-07,197,250!2023-01-02,42,302-->
2. prefix order: alphabetical order ignoring prefixes for type count→:::←bond order: single bond, double bond, triple bond, ... <!--SR:!2023-08-30,314,292!2023-01-01,41,307-->
3. bond order: single bond, double bond, triple bond, ...→:::←_(end)_ <!--SR:!2023-01-28,61,320!2023-01-30,63,322-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify words for pronunciation

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299372"--><!-- The following content is generated at 2022-11-05T00:24:43.721370+08:00. Any edits will be overridden! -->

> - suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u): drop '-e'
> - bond suffix is followed by prefix for type count: keep '-e'
> - prefix for carbon count is followed by prefix for type count: add '-a'

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19fc21"--><!-- The following content is generated at 2022-11-06T20:13:24.211188+08:00. Any edits will be overridden! -->

1. suffix ends in '-e' and next suffix starts with vowel (a, e, i, o, u):::drop '-e' <!--SR:!2023-05-20,147,224!2023-02-20,234,267-->
2. bond suffix is followed by prefix for type count:::keep '-e' <!--SR:!2024-04-13,475,250!2023-03-23,145,241-->
3. prefix for carbon count is followed by prefix for type count:::add '-a' <!--SR:!2023-01-22,46,210!2023-01-14,86,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### modify punctuations

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a920de"--><!-- The following content is generated at 2022-11-05T00:24:43.754371+08:00. Any edits will be overridden! -->

> 1. commas (,) between locants
> 2. hyphens (-) between word and locant
> 3. remove (most) spaces ( )

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9293da"--><!-- The following content is generated at 2022-11-09T18:05:21.147143+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←commas (,) between locants <!--SR:!2023-01-21,252,332!2023-01-22,58,320-->
2. commas (,) between locants→:::←hyphens (-) between word and locant <!--SR:!2023-09-18,377,293!2023-01-20,56,321-->
3. hyphens (-) between word and locant→:::←remove (most) spaces ( ) <!--SR:!2023-03-16,271,333!2023-02-01,65,322-->
4. remove (most) spaces ( )→:::←_(end)_ <!--SR:!2023-02-19,83,347!2023-01-25,58,327-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### prefix for type count

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
text: gen.TextCode = gen.TextCode.compile(
	R'''{text:- }1{text:\: }(none){text:
- }2{text:\: }di-{text:
- }3{text:\: }tri-{text:
- }4/+{text:\: }([prefix for carbon count](#prefix%20for%20carbon%20count))a-'''
)
items: gen.TextCode = gen.common
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('ad83dc'),
		text=gen.common.quote_text(text),
	),
	gen.Result(
		location=__env__.cwf_section('19dcda'),
		text=gen.common.memorize_two_sided(text,
			states=read.read_flashcard_states(__env__.cwf_section('19dcda')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ad83dc"--><!-- The following content is generated at 2022-11-05T00:24:43.569371+08:00. Any edits will be overridden! -->

> - 1: (none)
> - 2: di-
> - 3: tri-
> - 4/+: ([prefix for carbon count](#prefix%20for%20carbon%20count))a-

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="19dcda"--><!-- The following content is generated at 2022-11-06T20:13:23.980184+08:00. Any edits will be overridden! -->

1. 1:::(none) <!--SR:!2024-05-18,635,330!2023-01-08,250,336-->
2. 2:::di- <!--SR:!2023-10-04,408,310!2023-01-31,249,322-->
3. 3:::tri- <!--SR:!2023-01-22,253,310!2023-02-04,253,324-->
4. 4/+:::([prefix for carbon count](#prefix%20for%20carbon%20count))a- <!--SR:!2023-06-29,311,270!2023-02-16,240,286-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### prefix for carbon count

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
text: gen.TextCode = gen.TextCode.compile(
	R'''{text:- }1{text:\: }meth-{text:
- }2{text:\: }eth-{text:
- }3{text:\: }prop-{text:
- }4{text:\: }but-{text:
- }5{text:\: }pent-{text:
- }6{text:\: }hex-{text:
- }7{text:\: }hept-{text:
- }8{text:\: }oct-{text:
- }9{text:\: }non-{text:
- }10{text:\: }dec-{text:
- }11{text:\: }undec-{text:
- }12{text:\: }dodec-{text:
- }13{text:\: }tridec-{text:
- }14{text:\: }tetradec-{text:
- }15{text:\: }pentadec-{text:
- }16{text:\: }hexadec-{text:
- }17{text:\: }heptadec-{text:
- }18{text:\: }octadec-{text:
- }19{text:\: }nonadec-{text:
- }20{text:\: }icos-'''
)
items: gen.TextCode = gen.common
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('1239c2'),
		text=gen.common.quote_text(text),
	),
	gen.Result(
		location=__env__.cwf_section('ca1123'),
		text=gen.common.memorize_two_sided(text,
			states=read.read_flashcard_states(__env__.cwf_section('ca1123')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1239c2"--><!-- The following content is generated at 2022-11-05T00:24:43.539371+08:00. Any edits will be overridden! -->

> - 1: meth-
> - 2: eth-
> - 3: prop-
> - 4: but-
> - 5: pent-
> - 6: hex-
> - 7: hept-
> - 8: oct-
> - 9: non-
> - 10: dec-
> - 11: undec-
> - 12: dodec-
> - 13: tridec-
> - 14: tetradec-
> - 15: pentadec-
> - 16: hexadec-
> - 17: heptadec-
> - 18: octadec-
> - 19: nonadec-
> - 20: icos-

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ca1123"--><!-- The following content is generated at 2022-11-06T20:13:23.930188+08:00. Any edits will be overridden! -->

1. 1:::meth- <!--SR:!2024-02-20,481,290!2023-03-29,312,330-->
2. 2:::eth- <!--SR:!2024-03-26,507,290!2023-11-08,384,256-->
3. 3:::prop- <!--SR:!2023-09-10,384,290!2023-06-09,356,301-->
4. 4:::but- <!--SR:!2023-06-28,310,270!2023-01-07,203,266-->
5. 5:::pent- <!--SR:!2024-05-17,634,330!2024-01-10,447,286-->
6. 6:::hex- <!--SR:!2023-09-06,380,290!2023-02-27,254,286-->
7. 7:::hept- <!--SR:!2023-09-03,377,290!2023-08-06,349,286-->
8. 8:::oct- <!--SR:!2023-09-13,387,290!2023-02-28,255,286-->
9. 9:::non- <!--SR:!2023-06-20,367,310!2023-01-21,88,287-->
10. 10:::dec- <!--SR:!2023-02-21,92,270!2023-02-10,237,287-->
11. 11:::undec- <!--SR:!2023-03-11,88,230!2023-12-09,415,267-->
12. 12:::dodec- <!--SR:!2023-07-03,315,270!2023-05-16,267,247-->
13. 13:::tridec- <!--SR:!2023-07-02,314,270!2023-05-27,151,227-->
14. 14:::tetradec- <!--SR:!2023-06-21,303,270!2023-01-07,203,267-->
15. 15:::pentadec- <!--SR:!2023-03-27,282,332!2024-05-19,552,312-->
16. 16:::hexadec- <!--SR:!2023-03-12,267,332!2023-01-14,205,272-->
17. 17:::heptadec- <!--SR:!2024-03-12,509,312!2023-07-27,339,292-->
18. 18:::octadec- <!--SR:!2024-06-01,562,312!2023-03-10,265,332-->
19. 19:::nonadec- <!--SR:!2023-03-08,288,352!2023-01-24,57,210-->
20. 20:::icos- <!--SR:!2023-01-06,46,300!2023-03-01,93,342-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## functional groups

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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
table: str = gen.affix_lines(
	gen.common.rows_to_table(data,
		names=('class', 'group', 'formula', 'prefix', 'suffix', 'infix', 'misc',),
		values=lambda group: (group.clazz, group.group, group.formula, group.prefix, group.suffix, group.infix,
			'\n'.join(f'- {key}: {value}' for key, value in group.misc.items()),
		),
	),
	prefix='> ',
)
text: gen.TextCode = gen.common.maps_to_code(map,
	name_cloze=True,)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('28dcee'),
		text=gen.common.text(table),
	),
	gen.Result(
		location=__env__.cwf_section('a39fd2'),
		text=gen.common.cloze_text(text,
			states=read.read_flashcard_states(__env__.cwf_section('a39fd2')),
		),
	),
)
```
%%

Use suffixes (starts with hyphen (-)) before prefixes. Only use one suffix. Bonds must use suffixes. Always add infixes.

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="28dcee"--><!-- The following content is generated at 2022-11-04T23:41:04.443936+08:00. Any edits will be overridden! -->

> class | group | formula | prefix | suffix | infix | misc
> -|-|-|-|-|-|-
> alkane | alkyl | R(CH<sub>2</sub>)<sub>n</sub>H | ([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl- | -ane | (none), (locant) | - cyclic prefix: cyclo-
> alkene | alkenyl | R<sub>2</sub>C=CR<sub>2</sub> | ([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl- | -ene | (locant) | - cyclic prefix: cyclo-
> alkyne | alkynyl | RC≡CR' | ([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl- | -yne | (locant) | - cyclic prefix: cyclo-
> benzene derivative | phenyl | RC<sub>6</sub>H<sub>5</sub>/RPh | phenyl- | -benzene | (locant) |
> ([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane | ([prefix for halogen](#affixes%20for%20halogen)), halo | RX | ([prefix for halogen](#affixes%20for%20halogen))-, halo- | ([suffix for halogen](#affixes%20for%20halogen)) | (locant) |
> alcohol | hydroxyl | ROH | hydroxy- | -ol | (locant) |
> ether | ether | ROR' | ([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-) | ether | (locant) |
> aldehyde | aldehyde | RCHO | oxo- (=O), formyl- (-CHO) | -al (=O), -carbaldehyde (-CHO) | (locant) |
> ketone | carbonyl | RCOR' | oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR') | -one | (locant) |
> carboxylic acid | carboxyl | RCOOH | carboxy- | -ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH) | (locant) |
> carboxylate | carboxylate | RCOO<sup>-</sup> | carboxy- | -ate (retained), -oate | (locant) |
> alkanoyl | acyl | RCO | (none) | -yl (retained), -oyl | (locant) |
> amine | amino | RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup> | amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>) | -amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>) | (locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>) |
> amide | amide | RCONH<sub>2</sub>, RCONHR', RCONR'R'' | amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>) | -amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>) | (locant) & _N_ (R', R'') |
> nitrile | nitrile | RCN | cyano- | -nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN) | (locant) |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a39fd2"--><!-- The following content is generated at 2022-11-04T23:41:04.458936+08:00. Any edits will be overridden! -->

> {{alkane}}
> - group: {{alkyl}}
> - formula: {{R(CH<sub>2</sub>)<sub>n</sub>H}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))yl-, alkyl-}}
> - suffix: {{-ane}}
> - infix: {{(none), (locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2023-02-22,86,348!2023-02-19,83,348!2023-01-31,68,348!2023-02-20,84,348!2023-02-20,84,348!2023-02-19,83,348!2023-02-20,84,348-->

> {{alkene}}
> - group: {{alkenyl}}
> - formula: {{R<sub>2</sub>C=CR<sub>2</sub>}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))enyl-, alkenyl-}}
> - suffix: {{-ene}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2023-02-10,77,340!2023-02-25,89,342!2023-01-23,59,322!2023-03-02,79,282!2023-02-26,90,342!2023-02-27,91,342!2023-01-05,47,307-->

> {{alkyne}}
> - group: {{alkynyl}}
> - formula: {{RC≡CR'}}
> - prefix: {{([prefix for type count](#prefix%20for%20type%20count))ynyl-, alkynyl-}}
> - suffix: {{-yne}}
> - infix: {{(locant)}}
> - cyclic prefix: {{cyclo-}} <!--SR:!2023-01-22,62,320!2023-01-01,40,280!2023-02-26,90,340!2023-03-15,88,281!2023-03-01,93,342!2023-02-09,76,342!2023-01-11,52,327-->

> {{benzene derivative}}
> - group: {{phenyl}}
> - formula: {{RC<sub>6</sub>H<sub>5</sub>/RPh}}
> - prefix: {{phenyl-}}
> - suffix: {{-benzene}}
> - infix: {{(locant)}} <!--SR:!2023-01-03,43,300!2023-01-08,39,300!2023-02-13,80,342!2023-01-14,55,322!2022-12-29,42,302!2023-02-21,85,347-->

> {{([prefix for halogen](#affixes%20for%20halogen))alkane, haloalkane}}
> - group: {{([prefix for halogen](#affixes%20for%20halogen)), halo}}
> - formula: {{RX}}
> - prefix: {{([prefix for halogen](#affixes%20for%20halogen))-, halo-}}
> - suffix: {{([suffix for halogen](#affixes%20for%20halogen))}}
> - infix: {{(locant)}} <!--SR:!2023-01-05,44,300!2023-01-02,14,281!2023-02-28,92,342!2023-03-19,90,282!2023-03-17,80,285!2023-02-24,88,347-->

> {{alcohol}}
> - group: {{hydroxyl}}
> - formula: {{ROH}}
> - prefix: {{hydroxy-}}
> - suffix: {{-ol}}
> - infix: {{(locant)}} <!--SR:!2023-02-25,89,342!2023-02-26,90,342!2023-03-01,93,342!2023-02-19,83,345!2023-02-17,81,345!2023-02-21,85,347-->

> {{ether}}
> - group: {{ether}}
> - formula: {{ROR'}}
> - prefix: {{([prefix for carbon count](#prefix%20for%20carbon%20count))oxy- (-OR'), alkoxy- (-OR'), oxa- (-O-)}}
> - suffix: {{ether}}
> - infix: {{(locant)}} <!--SR:!2023-02-24,88,340!2023-02-27,91,342!2023-02-12,79,342!2023-01-01,29,242!2023-01-27,60,325!2023-02-04,71,347-->

> {{aldehyde}}
> - group: {{aldehyde}}
> - formula: {{RCHO}}
> - prefix: {{oxo- (=O), formyl- (-CHO)}}
> - suffix: {{-al (=O), -carbaldehyde (-CHO)}}
> - infix: {{(locant)}} <!--SR:!2023-02-09,76,342!2023-02-27,91,342!2023-01-05,45,302!2023-01-17,26,225!2023-03-09,84,285!2023-02-05,72,347-->

> {{ketone}}
> - group: {{carbonyl}}
> - formula: {{RCOR'}}
> - prefix: {{oxo- (=O), ([prefix for carbon count](#prefix%20for%20carbon%20count))oyl- (-COR')}}
> - suffix: {{-one}}
> - infix: {{(locant)}} <!--SR:!2023-02-23,74,280!2023-01-19,51,280!2023-01-21,57,321!2023-01-19,43,242!2023-03-01,93,342!2023-02-26,90,342-->

> {{carboxylic acid}}
> - group: {{carboxyl}}
> - formula: {{RCOOH}}
> - prefix: {{carboxy-}}
> - suffix: {{-ic acid (-(=O)OH, retained), -oic acid (-(=O)OH), -carboxylic acid (-COOH)}}
> - infix: {{(locant)}} <!--SR:!2023-01-13,54,320!2022-12-30,43,302!2023-02-27,91,342!2022-12-30,40,302!2023-01-09,34,305!2023-02-18,82,347-->

> {{carboxylate}}
> - group: {{carboxylate}}
> - formula: {{RCOO<sup>-</sup>}}
> - prefix: {{carboxy-}}
> - suffix: {{-ate (retained), -oate}}
> - infix: {{(locant)}} <!--SR:!2023-02-08,75,342!2023-02-24,88,342!2023-02-23,87,342!2023-02-24,72,262!2023-01-05,18,262!2023-02-07,74,347-->

> {{alkanoyl}}
> - group: {{acyl}}
> - formula: {{RCO}}
> - prefix: {{(none)}}
> - suffix: {{-yl (retained), -oyl}}
> - infix: {{(locant)}} <!--SR:!2023-01-18,42,261!2023-01-06,45,302!2023-02-28,92,342!2023-01-20,44,242!2023-01-14,20,267!2023-02-23,87,347-->

> {{amine}}
> - group: {{amino}}
> - formula: {{RNH<sub>2</sub>, RR'NH, R<sub>3</sub>N, R<sub>4</sub>N<sup>+</sup>}}
> - prefix: {{amino- (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), ammonio- (N<sub>4</sub>N<sup>+</sup>)}}
> - suffix: {{-amine (RNH<sub>2</sub>/RR'NH/R<sub>3</sub>), -ammonium (N<sub>4</sub>N<sup>+</sup>)}}
> - infix: {{(locant) & _N_ (R'/R''/R<sub>3</sub>/R<sub>4</sub>)}} <!--SR:!2023-02-01,69,345!2023-02-18,82,345!2023-01-09,47,305!2023-01-08,50,325!2023-03-10,84,287!2023-01-24,62,327-->

> {{amide}}
> - group: {{amide}}
> - formula: {{RCONH<sub>2</sub>, RCONHR', RCONR'R''}}
> - prefix: {{amido- (-(=O)NX<sub>2</sub>), carbamoyl- (-CONX<sub>2</sub>)}}
> - suffix: {{-amide (-(=O)NX<sub>2</sub>), carboxamide- (-CONX<sub>2</sub>)}}
> - infix: {{(locant) & _N_ (R', R'')}} <!--SR:!2023-01-27,64,345!2023-02-21,85,345!2023-01-23,61,325!2023-02-27,77,285!2023-03-10,83,285!2023-01-31,64,327-->

> {{nitrile}}
> - group: {{nitrile}}
> - formula: {{RCN}}
> - prefix: {{cyano-}}
> - suffix: {{-nitrile (≡N)/-onitrile (≡N, replace -oic), -carbonitrile (-CN)}}
> - infix: {{(locant)}} <!--SR:!2023-02-23,87,348!2023-02-20,84,348!2023-02-22,86,348!2023-01-22,60,328!2023-01-30,49,268!2023-02-22,86,348-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### affixes for halogen

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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
table: gen.TextCode = gen.TextCode.compile(gen.common.rows_to_table(data,
		names=('element', 'prefix', 'suffix',),
		values=lambda affixes: map(gen.TextCode.escape,
			(affixes.element, f'{{{{{affixes.prefix}}}}}', f'{{{{{affixes.suffix}}}}}',)
		),
	))
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('adc061'),
		text=gen.common.cloze_text(table,
			states=read.read_flashcard_states(__env__.cwf_section('adc061')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="adc061"--><!-- The following content is generated at 2022-11-05T00:24:43.494371+08:00. Any edits will be overridden! -->

> element | prefix | suffix
> -|-|-
> fluorine | {{fluoro-}} | {{fluoride}}
> chlorine | {{chloro-}} | {{chloride}}
> bromine | {{bromo-}} | {{bromide}}
> iodine | {{iodo-}} | {{iodide}} <!--SR:!2024-01-24,520,301!2023-04-08,322,344!2023-12-25,490,304!2023-04-13,327,346!2023-11-15,442,307!2023-09-08,447,347!2024-02-25,539,312!2023-07-18,395,353-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### precedence of functional groups

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
text: gen.TextCode = gen.common.seq_to_code((
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
	prefix='{mem:_(highest)_}',
	suffix='{mem:_(lowest)_}',)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('19cfa2'),
		text=gen.common.quote_text(text),
	),
	gen.Result(
		location=__env__.cwf_section('ad92c1'),
		text=gen.common.memorize_linked_seq(text,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('ad92c1')),
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

1. _(highest)_→:::←cation <!--SR:!2023-02-02,251,324!2023-07-17,394,352-->
2. cation→:::←carboxylic acid <!--SR:!2024-05-01,517,275!2023-07-19,331,276-->
3. carboxylic acid→:::←carboxylic acid derivate <!--SR:!2024-03-27,520,306!2023-04-03,289,326-->
4. carboxylic acid derivate→:::←nitrile <!--SR:!2022-12-30,46,210!2023-01-29,219,267-->
5. nitrile→:::←aldehyde <!--SR:!2023-02-03,77,230!2023-11-12,364,250-->
6. aldehyde→:::←ketone <!--SR:!2024-01-29,423,252!2023-04-18,239,250-->
7. ketone→:::←alcohol <!--SR:!2023-02-10,45,190!2023-01-29,33,190-->
8. alcohol→:::←hydroperoxide <!--SR:!2023-03-15,205,226!2023-11-17,393,272-->
9. hydroperoxide→:::←amine <!--SR:!2023-11-20,396,264!2024-05-21,515,272-->
10. amine→:::←_(lowest)_ <!--SR:!2023-04-01,95,236!2023-04-02,99,247-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
