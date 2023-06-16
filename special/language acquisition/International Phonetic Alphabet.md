---
tags:
  - categories/language_acquisition
  - flashcards/special/language_acquisition/International_Phonetic_Alphabet
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../tools/utility.py.md
```
%%

# International Phonetic Alphabet

> ![official IPA chart](../../archives/Wikimedia%20Commons/IPA%20chart%202020.svg)
>
> official IPA chart

## help

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import NULL_LOCATION, Result
e = __env__
return chain.from_iterable(await gather(memorize_table(
	(*e.cwf_sects("958a"), NULL_LOCATION,),
	("symbol", f"audio{'&nbsp;' * 8}", "description",),
	(
		(R'\[[a](open%20front%20unrounded%20vowel.md)\]', '![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _h**a**t_ \[hat\]',),
		(R'\[[ä](open%20central%20unrounded%20vowel.md)\]', '![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _br**a**_ \[bɹɐ̞ː\]',),
		(R'\[[ɐ](near-open%20central%20vowel.md)\]', '![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _n**u**t_ \[nɐʔt\]',),
		(R'\[[ɑ](open%20back%20unrounded%20vowel.md)\]', '![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]',),
		(R'\[[ɑ̃](nasal%20vowel.md)\]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)', R'[French](French%20language.md) _s**an**s_ [sɑ̃] "without"',),
		(R'\[[ɒ](open%20back%20rounded%20vowel.md)\]', '![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɒt\]',),
		(R'\[[ʌ](open-mid%20back%20unrounded%20vowel.md)\]', '![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)', R'[English](English%20language.md) _g**u**t_ \[ɡʌt\]',),
		(R'\[[æ](near-open%20front%20unrounded%20vowel.md)\]', '![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _c**a**t_ \[kʰæt\]',),
		(R'\[[b](voiced%20bilabial%20plosive.md)\]', '![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _a**b**ack_ \[əˈbæk\]',),
		(R'\[[ɓ](voiced%20bilabial%20implosive.md)\]', '![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)', R'[English](English%20language.md) _**b**ody_ \[ɓʌdi\]',),
		(R'\[[β](voiced%20bilabial%20fricative.md)\]', '![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"',),
		(R'\[[ʙ](voiced%20bilabial%20trill.md)\]', '![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)', R'[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"',),
		(R'\[[c](voiceless%20palatal%20plosive.md)\]', '![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)', R'[French](French%20language.md) _**q**ui_ \[ci\] "who"',),
		(R'\[[ç](voiceless%20palatal%20fricative.md)\]', '![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)', R'[English](English%20language.md) _**h**ue_ \[çʉː\]',),
		(R'\[[ɕ](voiceless%20alveolo-palatal%20fricative.md)\]', '![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)', R'[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]',),
		(R'\[[d](voiced%20alveolar%20plosive.md)\]', '![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]',),
		(R'\[[ɗ](voiced%20alveolar%20implosive.md)\]', '![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)', R'[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"',),
		(R'\[[ɖ](voiced%20retroflex%20plosive.md)\]', '![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)', R'[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"',),
		(R'\[[ð](voiced%20dental%20fricative.md)\]', '![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**is_ \[ðɪs\]',),
		(R'\[[dz](voiced%20alveolar%20affricate.md)\]', '![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]',),
		(R'\[[dʒ](voiced%20postalveolar%20affricate.md)\]', '![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _**g**ene_ 	\[ˈd͡ʒiːn\]',),
		(R'\[[dʑ](voiced%20alveolo-palatal%20affricate.md)\]', '![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"',),
		(R'\[[dʐ](voiced%20retroflex%20affricate.md)\]', '![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"',),
		(R'\[[e](close-mid%20front%20unrounded%20vowel.md)\]', '![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _m**ay**_ \[meː\]',),
		(R'\[[ɘ](close-mid%20central%20unrounded%20vowel.md)\]', '![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɘːd\]',),
		(R'\[[ə](mid%20central%20vowel.md)\]', '![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)', R'[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]',),
		(R'\[[ɚ](r-colored%20vowel.md)\]', '![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]',),
		(R'\[[ɛ](open-mid%20front%20unrounded%20vowel.md)\]', '![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**e**d_ \[bɛd\]',),
		(R'\[[ɛ̃](nasal%20vowel.md)\]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)', R'[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"',),
		(R'\[[ɜ](open-mid%20central%20unrounded%20vowel.md)\]', '![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɜːd\]',),
		(R'\[[ɝ](r-colored%20vowel.md)\]', '![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɝːd\]',),
		(R'\[[f](voiceless%20labiodental%20fricative.md)\]', '![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**f**ill_ \[fɪɫ\]',),
		(R'\[[ɡ](voiced%20velar%20plosive.md)\]', '![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)', R'[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]',),
		(R'\[[ɠ](voiced%20velar%20implosive.md)\]', '![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
		(R'\[[ɢ](voiced%20uvular%20plosive.md)\]', '![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)', R'[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]',),
		(R'\[[h](voiceless%20glottal%20fricative.md)\]', '![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)', R'[English](English%20language.md) _**h**igh_ \[haɪ̯\]',),
		(R'\[[ɦ](voiced%20glottal%20fricative.md)\]', '![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)', R'[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]',),
		(R'\[[ʰ](aspirated%20consonant.md)\]', '', R'[English](English%20langugae.md) _**t**op_ \[tʰɒp\]',),
		(R'\[[ħ](voiceless%20pharyngeal%20fricative.md)\]', '![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)', R'[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]',),
		(R'\[[i](close%20front%20unrounded%20vowel.md)\]', '![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _fr**ee**_ \[fɹiː\]',),
		(R'\[[ɪ](near-close%20near-front%20unrounded%20vowel.md)\]', '![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**i**t_ \[bɪʔt\]',),
		(R'\[[ɨ](close%20central%20unrounded%20vowel.md)\]', '![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)', R'[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"',),
		(R'\[[j](voiced%20palatal%20approximant.md)\]', '![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)', R'[English](English%20language.md) _**y**ou_ \[juː\]',),
		(R'\[[ʲ](palatalization%20(phonetics).md)\]', '', R'[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"',),
		(R'\[[ʝ](voiced%20palatal%20fricative.md)\]', '![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"',),
		(R'\[[ɟ](voiced%20palatal%20plosive.md)\]', '![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)', R'[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"',),
		(R'\[[ʄ](voiced%20palatal%20implosive.md)\]', '![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)', R'[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"',),
		(R'\[[k](voiceless%20velar%20plosive.md)\]', '![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)', R'[English](English%20language.md) _**k**iss_ \[kʰɪs\]',),
		(R'\[[l](voiced%20alveolar%20lateral%20approximant.md)\]', '![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _**l**et_ \[lɛt\]',),
		(R'\[[ɫ](velarized%20alveolar%20lateral%20approximant.md)\]', '![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _fee**l**_ \[fiːɫ\]',),
		(R'\[[ɬ](voiceless%20alveolar%20lateral%20fricative.md)\]', '![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)', R'[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"',),
		(R'\[[ɭ](voiced%20retroflex%20lateral%20approximant.md)\]', '![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)', R'[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"',),
		(R'\[[ɺ](voiced%20alveolar%20lateral%20flap.md)\]', '', R'[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"',),
		(R'\[[ɮ](voiced%20alveolar%20lateral%20fricative.md)\]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', R'[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"',),
		(R'\[[ʟ](voiced%20velar%20lateral%20approximant.md)\]', '![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]',),
		(R'\[[m](voiced%20bilabial%20nasal.md)\]', '![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)', R'[English](English%20language.md) _hi**m**_ \[hɪm\]',),
		(R'\[[ɱ](voiced%20labiodental%20nasal.md)\]', '![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)', R'[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]',),
		(R'\[[n](voiced%20alveolar%20nasal.md)\]', '![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)', R'[English](English%20language.md) _**n**ice_ \[naɪs\]',),
		(R'\[[ŋ](voiced%20velar%20nasal.md)\]', '![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)', R'[English](English%20language.md) _si**ng**_ \[sɪŋ\]',),
		(R'\[[ɲ](voiced%20palatal%20nasal.md)\]', '![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)', R'[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"',),
		(R'\[[ɳ](voiced%20retroflex%20nasal.md)\]', '![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)', R'[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"',),
		(R'\[[ɴ](voiced%20uvular%20nasal.md)\]', '![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)', R'[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"',),
		(R'\[[o](close-mid%20back%20rounded%20vowel.md)\]', '![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _y**aw**n_ \[joːn\]',),
		(R'\[[ɔ](open-mid%20back%20rounded%20vowel.md)\]', '![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɔt\]',),
		(R'\[[ɔ̃](nasal%20vowel.md)\]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)', R'[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"',),
		(R'\[[ø](close-mid%20front%20rounded%20vowel.md)\]', '![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _p**eu**_ \[pø\] "few"',),
		(R'\[[ɵ](close-mid%20central%20rounded%20vowel.md)\]', '![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)', '[English](English%20language.md) _f**oo**t_ \[fɵʔt\]',),
		(R'\[[œ](open-mid%20front%20rounded%20vowel.md)\]', '![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"',),
		(R'\[[œ̃](nasal%20vowel.md)\]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)', R'[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"',),
		(R'\[[ɶ](open%20front%20rounded%20vowel.md)\]', '![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)', R'[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"',),
		(R'\[[p](voiceless%20bilabial%20plosive.md)\]', '![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _**p**ack_ \[pʰæk\]',),
		(R'\[[q](voiceless%20uvular%20plosive.md)\]', '![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)', R'[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"',),
		(R'\[[r](voiced%20alveolar%20trill.md)\]', '![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)', R'[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"',),
		(R'\[[ɾ](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)\]', '![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)', R'[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"',),
		(R'\[[ʀ](voiced%20uvular%20trill.md)\]', '![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)', R'[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"',),
		(R'\[[ɽ](voiced%20retroflex%20flap.md)\]', '![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)', R'[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"',),
		(R'\[[ɹ](voiced%20alveolar%20approximant.md)\]', '![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)', R'[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"',),
		(R'\[[ɻ](voiced%20retroflex%20approximant.md)\]', '![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)', R'[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"',),
		(R'\[[ʁ](voiced%20uvular%20fricative.md)\]', '![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)', R'[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"',),
		(R'\[[s](voiceless%20alveolar%20fricative.md)\]', '![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**s**it_ \[sɪt\]',),
		(R'\[[ʃ](voiceless%20postalveolar%20fricative.md)\]', '![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]',),
		(R'\[[ʂ](voiceless%20retroflex%20fricative.md)\]', '![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)', R'[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"',),
		(R'\[[t](voiceless%20alveolar%20plosive.md)\]', '![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**t**ick_ \[tʰɪk\]',),
		(R'\[[ʈ](voiceless%20retroflex%20plosive.md)\]', '![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)', R'[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"',),
		(R'\[[ts](voiceless%20alveolar%20affricate.md)\]', '![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]',),
		(R'\[[tʃ](voiceless%20postalveolar%20affricate.md)\]', '![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]',),
		(R'\[[tɕ](voiceless%20alveolo-palatal%20affricate.md)\]', '![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"',),
		(R'\[[tʂ](voiceless%20retroflex%20affricate.md)\]', '![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"',),
		(R'\[[u](close%20back%20rounded%20vowel.md)\]', '![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]',),
		(R'\[[ʊ](near-close%20near-back%20rounded%20vowel.md)\]', '![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _h**oo**k_ \[hʊʔk\]',),
		(R'\[[ʉ](close%20central%20rounded%20vowel.md)\]', '![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)', R'[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]',),
		(R'\[[v](voiced%20labiodental%20fricative.md)\]', '![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**v**al**v**e_ \[væɫv\]',),
		(R'\[[ʋ](voiced%20labiodental%20approximant.md)\]', '![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)', R'[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"',),
		(R'\[[w](voiced%20labial–velar%20approximant.md)\]', '![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)', R'[English](English%20language.md) _**w**eep_ \[wiːp\]',),
		(R'\[[ʷ](labialization.md)\]', '', R'[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]',),
		(R'\[[ʍ](voiceless%20labial–velar%20fricative.md)\]', '![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)', R'[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]',),
		(R'\[[ɯ](close%20back%20unrounded%20vowel.md)\]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', R'[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"',),
		(R'\[[ɰ](voiced%20velar%20approximant.md)\]', '![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)', R'[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"',),
		(R'\[[x](voiceless%20velar%20fricative.md)\]', '![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)', R'[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"',),
		(R'\[[χ](voiceless%20uvular%20fricative.md)\]', '![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)', R'[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"',),
		(R'\[[y](close%20front%20rounded%20vowel.md)\]', '![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _t**u**_ \[t̪y] "you"',),
		(R'\[[ʏ](near-close%20near-front%20rounded%20vowel.md)\]', '![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)', R'[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"',),
		(R'\[[ɣ](voiced%20velar%20fricative.md)\]', '![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"',),
		(R'\[[ɤ](close-mid%20back%20unrounded%20vowel.md)\]', '![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)', R'[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"',),
		(R'\[[ʎ](voiced%20palatal%20lateral%20approximant.md)\]', '![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)', R'[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]',),
		(R'\[[ɥ](voiced%20labial–palatal%20approximant.md)\]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', R'[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"',),
		(R'\[[z](voiced%20alveolar%20fricative.md)\]', '![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)', '[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]',),
		(R'\[[ʒ](voiced%20postalveolar%20fricative.md)\]', '![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]',),
		(R'\[[ʑ](voiced%20alveolo-palatal%20fricative.md)\]', '![voiced alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)', R'[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"',),
		(R'\[[ʐ](voiced%20retroflex%20fricative.md)\]', '![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)', R'[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"',),
		(R'\[[θ](voiceless%20dental%20fricative.md)\]', '![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**in_ \[θɪn\]',),
		(R'\[[ɸ](voiceless%20bilabial%20fricative.md)\]', '![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)', R'[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"',),
		(R'\[[ʔ](glottal%20stop.md)\]', '![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)', R'[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]',),
		(R'\[[ʕ](voiced%20pharyngeal%20fricative.md)\]', '![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)', R'[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"',),
		(R'\[[ǀ](tenuis%20dental%20click.md)\]', '![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)', R'[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]',),
		(R'\[[ǁ](tenuis%20alveolar%20lateral%20click.md)\]', '![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)', R'[English](English%20language.md) _**tchick**_ \[ˈǁ\]',),
		(R'\[[ǃ](tenuis%20alveolar%20click.md)\]', '![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)', R'[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"',),
		(R'\[[ʘ](tenuis%20bilabial%20click.md)\]', '![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)', R'[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"',),
		(R'\[[ǂ](tenuis%20palatal%20click.md)\]', '![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)', R'[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"',),
	),
	lambda datum: map(cloze, datum),
), memorize_table(
	(*e.cwf_sects("485d"), NULL_LOCATION,),
	("symbol", "description",),
	(
		(R'[\[◌̃\]](nasal%20vowel.md) (e.g. [ã])', R'[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"',),
		(R'[\[◌̈\]](central%20vowel.md) (e.g. [ä])', R'[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"',),
		(R'[\[◌̆\]](extra-shortness.md) (e.g. [ă])', R'[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]',),
		(R'[\[◌̯\]](diphthong.md) (e.g. [a̯])', R'[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]',),
		(R'[\[◌̥\]](voicelessness.md) (e.g. [n̥])', R'[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]',),
		(R'[\[◌̩\], \[◌̍\]](syllabic%20consonant.md) (e.g. [n̩], [ŋ̍])', R'[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]',),
		(R'[\[◌̪\]](dental%20consonant.md) (e.g. [d̪])', R'[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"',),
		(R'[\[◌ʰ\]](aspirated%20consonant.md) (e.g. [kʰ])', R'[English](English%20language.md) _**c**ome_ \[kʰɐm\]',),
		(R'[\[◌’\]](ejective%20consonant.md) (e.g. [k’])', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
		(R'[\[◌ː\]](longness%20(phonetics).md) (e.g. [aː])', R'[English](English%20language.md) _shh!_ \[ʃː\]',),
		(R'[\[◌ˑ\]](half-longness%20(phonetics).md) (e.g. [aˑ])', R'[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]',),
		(R'[\[ˈ◌\]](stress%20(lingustics).md) (e.g. [ˈa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
		(R'[\[ˌ◌\]](secondary%20stress.md) (e.g. [ˌa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
		(R'[\[.\]](syllable.md)', R'[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]',),
	),
	lambda datum: map(cloze, datum),
),))
```
%%

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:
- (principal) {{\[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]}}: {{[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md)}}
- (principal) {{/[slashes](slash%20(punctuation).md)/}}: {{[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only}}
- (uncommon) {{{[curly brackets](bracket.md#curly%20brackets%20or%20braces)}}}: {{[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md), i.e. suprasegmentals}}
- (uncommon) {{([round brackets](bracket.md#round%20brackets%20or%20parentheses))}}: {{transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md)}}
- (uncommon) {{(([double round brackets](bracket.md#round%20brackets%20or%20parentheses)))}}: {{transcription of obscured speech or description of obscuring sound}}
- (unofficial) {{\[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]}}: {{extra-precise transcription}}
- (unofficial) {{//[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}}}: {{[morphophonemic](morphophonology.md) transcription}}
- (unofficial) {{⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫}}: {{original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves}}

### letters

Here is a list of common IPA letters and their pronunciations:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="958a"--><!-- The following content is generated at 2023-06-16T15:47:09.074846+08:00. Any edits will be overridden! -->

> | symbol | audio&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | description |
> |-|-|-|
> | {{\[[a](open%20front%20unrounded%20vowel.md)\]}} | {{![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _h**a**t_ \[hat\]}} |
> | {{\[[ä](open%20central%20unrounded%20vowel.md)\]}} | {{![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _br**a**_ \[bɹɐ̞ː\]}} |
> | {{\[[ɐ](near-open%20central%20vowel.md)\]}} | {{![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _n**u**t_ \[nɐʔt\]}} |
> | {{\[[ɑ](open%20back%20unrounded%20vowel.md)\]}} | {{![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]}} |
> | {{\[[ɑ̃](nasal%20vowel.md)\]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)}} | {{[French](French%20language.md) _s**an**s_ [sɑ̃] "without"}} |
> | {{\[[ɒ](open%20back%20rounded%20vowel.md)\]}} | {{![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _n**o**t_ \[nɒt\]}} |
> | {{\[[ʌ](open-mid%20back%20unrounded%20vowel.md)\]}} | {{![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)}} | {{[English](English%20language.md) _g**u**t_ \[ɡʌt\]}} |
> | {{\[[æ](near-open%20front%20unrounded%20vowel.md)\]}} | {{![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _c**a**t_ \[kʰæt\]}} |
> | {{\[[b](voiced%20bilabial%20plosive.md)\]}} | {{![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)}} | {{[English](English%20language.md) _a**b**ack_ \[əˈbæk\]}} |
> | {{\[[ɓ](voiced%20bilabial%20implosive.md)\]}} | {{![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)}} | {{[English](English%20language.md) _**b**ody_ \[ɓʌdi\]}} |
> | {{\[[β](voiced%20bilabial%20fricative.md)\]}} | {{![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)}} | {{[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"}} |
> | {{\[[ʙ](voiced%20bilabial%20trill.md)\]}} | {{![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)}} | {{[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"}} |
> | {{\[[c](voiceless%20palatal%20plosive.md)\]}} | {{![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)}} | {{[French](French%20language.md) _**q**ui_ \[ci\] "who"}} |
> | {{\[[ç](voiceless%20palatal%20fricative.md)\]}} | {{![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)}} | {{[English](English%20language.md) _**h**ue_ \[çʉː\]}} |
> | {{\[[ɕ](voiceless%20alveolo-palatal%20fricative.md)\]}} | {{![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)}} | {{[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]}} |
> | {{\[[d](voiced%20alveolar%20plosive.md)\]}} | {{![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)}} | {{[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]}} |
> | {{\[[ɗ](voiced%20alveolar%20implosive.md)\]}} | {{![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)}} | {{[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"}} |
> | {{\[[ɖ](voiced%20retroflex%20plosive.md)\]}} | {{![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)}} | {{[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"}} |
> | {{\[[ð](voiced%20dental%20fricative.md)\]}} | {{![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)}} | {{[English](English%20language.md) _**th**is_ \[ðɪs\]}} |
> | {{\[[dz](voiced%20alveolar%20affricate.md)\]}} | {{![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)}} | {{[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]}} |
> | {{\[[dʒ](voiced%20postalveolar%20affricate.md)\]}} | {{![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)}} | {{[English](English%20language.md) _**g**ene_ 	\[ˈd͡ʒiːn\]}} |
> | {{\[[dʑ](voiced%20alveolo-palatal%20affricate.md)\]}} | {{![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)}} | {{[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"}} |
> | {{\[[dʐ](voiced%20retroflex%20affricate.md)\]}} | {{![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)}} | {{[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"}} |
> | {{\[[e](close-mid%20front%20unrounded%20vowel.md)\]}} | {{![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _m**ay**_ \[meː\]}} |
> | {{\[[ɘ](close-mid%20central%20unrounded%20vowel.md)\]}} | {{![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _b**ir**d_ \[bɘːd\]}} |
> | {{\[[ə](mid%20central%20vowel.md)\]}} | {{![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)}} | {{[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]}} |
> | {{\[[ɚ](r-colored%20vowel.md)\]}} | {{![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)}} | {{[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]}} |
> | {{\[[ɛ](open-mid%20front%20unrounded%20vowel.md)\]}} | {{![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _b**e**d_ \[bɛd\]}} |
> | {{\[[ɛ̃](nasal%20vowel.md)\]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)}} | {{[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"}} |
> | {{\[[ɜ](open-mid%20central%20unrounded%20vowel.md)\]}} | {{![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _b**ir**d_ \[bɜːd\]}} |
> | {{\[[ɝ](r-colored%20vowel.md)\]}} | {{![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)}} | {{[English](English%20language.md) _b**ir**d_ \[bɝːd\]}} |
> | {{\[[f](voiceless%20labiodental%20fricative.md)\]}} | {{![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)}} | {{[English](English%20language.md) _**f**ill_ \[fɪɫ\]}} |
> | {{\[[ɡ](voiced%20velar%20plosive.md)\]}} | {{![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)}} | {{[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]}} |
> | {{\[[ɠ](voiced%20velar%20implosive.md)\]}} | {{![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)}} | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | {{\[[ɢ](voiced%20uvular%20plosive.md)\]}} | {{![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)}} | {{[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]}} |
> | {{\[[h](voiceless%20glottal%20fricative.md)\]}} | {{![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)}} | {{[English](English%20language.md) _**h**igh_ \[haɪ̯\]}} |
> | {{\[[ɦ](voiced%20glottal%20fricative.md)\]}} | {{![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)}} | {{[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]}} |
> | {{\[[ʰ](aspirated%20consonant.md)\]}} |  | {{[English](English%20langugae.md) _**t**op_ \[tʰɒp\]}} |
> | {{\[[ħ](voiceless%20pharyngeal%20fricative.md)\]}} | {{![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)}} | {{[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]}} |
> | {{\[[i](close%20front%20unrounded%20vowel.md)\]}} | {{![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _fr**ee**_ \[fɹiː\]}} |
> | {{\[[ɪ](near-close%20near-front%20unrounded%20vowel.md)\]}} | {{![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)}} | {{[English](English%20language.md) _b**i**t_ \[bɪʔt\]}} |
> | {{\[[ɨ](close%20central%20unrounded%20vowel.md)\]}} | {{![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)}} | {{[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"}} |
> | {{\[[j](voiced%20palatal%20approximant.md)\]}} | {{![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)}} | {{[English](English%20language.md) _**y**ou_ \[juː\]}} |
> | {{\[[ʲ](palatalization%20(phonetics).md)\]}} |  | {{[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"}} |
> | {{\[[ʝ](voiced%20palatal%20fricative.md)\]}} | {{![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)}} | {{[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"}} |
> | {{\[[ɟ](voiced%20palatal%20plosive.md)\]}} | {{![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)}} | {{[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"}} |
> | {{\[[ʄ](voiced%20palatal%20implosive.md)\]}} | {{![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)}} | {{[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"}} |
> | {{\[[k](voiceless%20velar%20plosive.md)\]}} | {{![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)}} | {{[English](English%20language.md) _**k**iss_ \[kʰɪs\]}} |
> | {{\[[l](voiced%20alveolar%20lateral%20approximant.md)\]}} | {{![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)}} | {{[English](English%20language.md) _**l**et_ \[lɛt\]}} |
> | {{\[[ɫ](velarized%20alveolar%20lateral%20approximant.md)\]}} | {{![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)}} | {{[English](English%20language.md) _fee**l**_ \[fiːɫ\]}} |
> | {{\[[ɬ](voiceless%20alveolar%20lateral%20fricative.md)\]}} | {{![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)}} | {{[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"}} |
> | {{\[[ɭ](voiced%20retroflex%20lateral%20approximant.md)\]}} | {{![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)}} | {{[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"}} |
> | {{\[[ɺ](voiced%20alveolar%20lateral%20flap.md)\]}} |  | {{[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"}} |
> | {{\[[ɮ](voiced%20alveolar%20lateral%20fricative.md)\]}} | {{![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)}} | {{[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"}} |
> | {{\[[ʟ](voiced%20velar%20lateral%20approximant.md)\]}} | {{![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)}} | {{[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]}} |
> | {{\[[m](voiced%20bilabial%20nasal.md)\]}} | {{![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)}} | {{[English](English%20language.md) _hi**m**_ \[hɪm\]}} |
> | {{\[[ɱ](voiced%20labiodental%20nasal.md)\]}} | {{![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)}} | {{[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]}} |
> | {{\[[n](voiced%20alveolar%20nasal.md)\]}} | {{![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)}} | {{[English](English%20language.md) _**n**ice_ \[naɪs\]}} |
> | {{\[[ŋ](voiced%20velar%20nasal.md)\]}} | {{![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)}} | {{[English](English%20language.md) _si**ng**_ \[sɪŋ\]}} |
> | {{\[[ɲ](voiced%20palatal%20nasal.md)\]}} | {{![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)}} | {{[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"}} |
> | {{\[[ɳ](voiced%20retroflex%20nasal.md)\]}} | {{![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)}} | {{[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"}} |
> | {{\[[ɴ](voiced%20uvular%20nasal.md)\]}} | {{![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)}} | {{[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"}} |
> | {{\[[o](close-mid%20back%20rounded%20vowel.md)\]}} | {{![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _y**aw**n_ \[joːn\]}} |
> | {{\[[ɔ](open-mid%20back%20rounded%20vowel.md)\]}} | {{![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _n**o**t_ \[nɔt\]}} |
> | {{\[[ɔ̃](nasal%20vowel.md)\]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)}} | {{[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"}} |
> | {{\[[ø](close-mid%20front%20rounded%20vowel.md)\]}} | {{![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)}} | {{[French](French%20language.md) _p**eu**_ \[pø\] "few"}} |
> | {{\[[ɵ](close-mid%20central%20rounded%20vowel.md)\]}} | {{![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _f**oo**t_ \[fɵʔt\]}} |
> | {{\[[œ](open-mid%20front%20rounded%20vowel.md)\]}} | {{![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)}} | {{[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"}} |
> | {{\[[œ̃](nasal%20vowel.md)\]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)}} | {{[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"}} |
> | {{\[[ɶ](open%20front%20rounded%20vowel.md)\]}} | {{![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)}} | {{[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"}} |
> | {{\[[p](voiceless%20bilabial%20plosive.md)\]}} | {{![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)}} | {{[English](English%20language.md) _**p**ack_ \[pʰæk\]}} |
> | {{\[[q](voiceless%20uvular%20plosive.md)\]}} | {{![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)}} | {{[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"}} |
> | {{\[[r](voiced%20alveolar%20trill.md)\]}} | {{![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)}} | {{[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"}} |
> | {{\[[ɾ](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)\]}} | {{![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)}} | {{[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"}} |
> | {{\[[ʀ](voiced%20uvular%20trill.md)\]}} | {{![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)}} | {{[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"}} |
> | {{\[[ɽ](voiced%20retroflex%20flap.md)\]}} | {{![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)}} | {{[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"}} |
> | {{\[[ɹ](voiced%20alveolar%20approximant.md)\]}} | {{![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)}} | {{[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"}} |
> | {{\[[ɻ](voiced%20retroflex%20approximant.md)\]}} | {{![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)}} | {{[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"}} |
> | {{\[[ʁ](voiced%20uvular%20fricative.md)\]}} | {{![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)}} | {{[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"}} |
> | {{\[[s](voiceless%20alveolar%20fricative.md)\]}} | {{![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)}} | {{[English](English%20language.md) _**s**it_ \[sɪt\]}} |
> | {{\[[ʃ](voiceless%20postalveolar%20fricative.md)\]}} | {{![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)}} | {{[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]}} |
> | {{\[[ʂ](voiceless%20retroflex%20fricative.md)\]}} | {{![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)}} | {{[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"}} |
> | {{\[[t](voiceless%20alveolar%20plosive.md)\]}} | {{![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)}} | {{[English](English%20language.md) _**t**ick_ \[tʰɪk\]}} |
> | {{\[[ʈ](voiceless%20retroflex%20plosive.md)\]}} | {{![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)}} | {{[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"}} |
> | {{\[[ts](voiceless%20alveolar%20affricate.md)\]}} | {{![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)}} | {{[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]}} |
> | {{\[[tʃ](voiceless%20postalveolar%20affricate.md)\]}} | {{![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)}} | {{[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]}} |
> | {{\[[tɕ](voiceless%20alveolo-palatal%20affricate.md)\]}} | {{![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)}} | {{[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"}} |
> | {{\[[tʂ](voiceless%20retroflex%20affricate.md)\]}} | {{![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)}} | {{[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"}} |
> | {{\[[u](close%20back%20rounded%20vowel.md)\]}} | {{![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]}} |
> | {{\[[ʊ](near-close%20near-back%20rounded%20vowel.md)\]}} | {{![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _h**oo**k_ \[hʊʔk\]}} |
> | {{\[[ʉ](close%20central%20rounded%20vowel.md)\]}} | {{![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)}} | {{[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]}} |
> | {{\[[v](voiced%20labiodental%20fricative.md)\]}} | {{![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)}} | {{[English](English%20language.md) _**v**al**v**e_ \[væɫv\]}} |
> | {{\[[ʋ](voiced%20labiodental%20approximant.md)\]}} | {{![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)}} | {{[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"}} |
> | {{\[[w](voiced%20labial–velar%20approximant.md)\]}} | {{![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)}} | {{[English](English%20language.md) _**w**eep_ \[wiːp\]}} |
> | {{\[[ʷ](labialization.md)\]}} |  | {{[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]}} |
> | {{\[[ʍ](voiceless%20labial–velar%20fricative.md)\]}} | {{![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)}} | {{[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]}} |
> | {{\[[ɯ](close%20back%20unrounded%20vowel.md)\]}} | {{![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)}} | {{[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"}} |
> | {{\[[ɰ](voiced%20velar%20approximant.md)\]}} | {{![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)}} | {{[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"}} |
> | {{\[[x](voiceless%20velar%20fricative.md)\]}} | {{![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)}} | {{[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"}} |
> | {{\[[χ](voiceless%20uvular%20fricative.md)\]}} | {{![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)}} | {{[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"}} |
> | {{\[[y](close%20front%20rounded%20vowel.md)\]}} | {{![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)}} | {{[French](French%20language.md) _t**u**_ \[t̪y] "you"}} |
> | {{\[[ʏ](near-close%20near-front%20rounded%20vowel.md)\]}} | {{![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)}} | {{[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"}} |
> | {{\[[ɣ](voiced%20velar%20fricative.md)\]}} | {{![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)}} | {{[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"}} |
> | {{\[[ɤ](close-mid%20back%20unrounded%20vowel.md)\]}} | {{![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)}} | {{[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"}} |
> | {{\[[ʎ](voiced%20palatal%20lateral%20approximant.md)\]}} | {{![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)}} | {{[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]}} |
> | {{\[[ɥ](voiced%20labial–palatal%20approximant.md)\]}} | {{![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)}} | {{[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"}} |
> | {{\[[z](voiced%20alveolar%20fricative.md)\]}} | {{![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)}} | {{[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]}} |
> | {{\[[ʒ](voiced%20postalveolar%20fricative.md)\]}} | {{![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)}} | {{[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]}} |
> | {{\[[ʑ](voiced%20alveolo-palatal%20fricative.md)\]}} | {{![voiced alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)}} | {{[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"}} |
> | {{\[[ʐ](voiced%20retroflex%20fricative.md)\]}} | {{![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)}} | {{[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"}} |
> | {{\[[θ](voiceless%20dental%20fricative.md)\]}} | {{![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)}} | {{[English](English%20language.md) _**th**in_ \[θɪn\]}} |
> | {{\[[ɸ](voiceless%20bilabial%20fricative.md)\]}} | {{![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)}} | {{[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"}} |
> | {{\[[ʔ](glottal%20stop.md)\]}} | {{![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)}} | {{[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]}} |
> | {{\[[ʕ](voiced%20pharyngeal%20fricative.md)\]}} | {{![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)}} | {{[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"}} |
> | {{\[[ǀ](tenuis%20dental%20click.md)\]}} | {{![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)}} | {{[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]}} |
> | {{\[[ǁ](tenuis%20alveolar%20lateral%20click.md)\]}} | {{![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)}} | {{[English](English%20language.md) _**tchick**_ \[ˈǁ\]}} |
> | {{\[[ǃ](tenuis%20alveolar%20click.md)\]}} | {{![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)}} | {{[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"}} |
> | {{\[[ʘ](tenuis%20bilabial%20click.md)\]}} | {{![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)}} | {{[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"}} |
> | {{\[[ǂ](tenuis%20palatal%20click.md)\]}} | {{![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)}} | {{[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485d"--><!-- The following content is generated at 2023-06-16T15:46:31.735258+08:00. Any edits will be overridden! -->

> | symbol | description |
> |-|-|
> | {{[\[◌̃\]](nasal%20vowel.md) (e.g. [ã])}} | {{[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"}} |
> | {{[\[◌̈\]](central%20vowel.md) (e.g. [ä])}} | {{[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"}} |
> | {{[\[◌̆\]](extra-shortness.md) (e.g. [ă])}} | {{[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]}} |
> | {{[\[◌̯\]](diphthong.md) (e.g. [a̯])}} | {{[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]}} |
> | {{[\[◌̥\]](voicelessness.md) (e.g. [n̥])}} | {{[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]}} |
> | {{[\[◌̩\], \[◌̍\]](syllabic%20consonant.md) (e.g. [n̩], [ŋ̍])}} | {{[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]}} |
> | {{[\[◌̪\]](dental%20consonant.md) (e.g. [d̪])}} | {{[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"}} |
> | {{[\[◌ʰ\]](aspirated%20consonant.md) (e.g. [kʰ])}} | {{[English](English%20language.md) _**c**ome_ \[kʰɐm\]}} |
> | {{[\[◌’\]](ejective%20consonant.md) (e.g. [k’])}} | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | {{[\[◌ː\]](longness%20(phonetics).md) (e.g. [aː])}} | {{[English](English%20language.md) _shh!_ \[ʃː\]}} |
> | {{[\[◌ˑ\]](half-longness%20(phonetics).md) (e.g. [aˑ])}} | {{[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]}} |
> | {{[\[ˈ◌\]](stress%20(lingustics).md) (e.g. [ˈa])}} | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | {{[\[ˌ◌\]](secondary%20stress.md) (e.g. [ˌa])}} | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | {{[\[.\]](syllable.md)}} | {{[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
