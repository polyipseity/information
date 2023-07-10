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
letters = (
	(R'[open front unrounded vowel](open%20front%20unrounded%20vowel.md) \[a\]', '![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _h**a**t_ \[hat\]',),
	(R'[open central unrounded vowel](open%20central%20unrounded%20vowel.md) \[ä\]', '![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _br**a**_ \[bɹäː\]',),
	(R'[near-open central vowel](near-open%20central%20vowel.md) \[ɐ\]', '![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _n**u**t_ \[nɐʔt\]',),
	(R'[open back unrounded vowel](open%20back%20unrounded%20vowel.md) \[ɑ\]', '![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]',),
	(R'[nasalized open back unrounded vowel](nasal%20vowel.md) \[ɑ̃\]', '![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)', R'[French](French%20language.md) _s**an**s_ [sɑ̃] "without"',),
	(R'[open back rounded vowel](open%20back%20rounded%20vowel.md) \[ɒ\]', '![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɒt\]',),
	(R'[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) \[ʌ\]', '![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)', R'[English](English%20language.md) _g**u**t_ \[ɡʌt\]',),
	(R'[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) \[æ\]', '![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _c**a**t_ \[kʰæt\]',),
	(R'[voiced bilabial plosive](voiced%20bilabial%20plosive.md) \[b\]', '![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _a**b**ack_ \[əˈbæk\]',),
	(R'[voiced bilabial implosive](voiced%20bilabial%20implosive.md) \[ɓ\]', '![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)', R'[English](English%20language.md) _**b**ody_ \[ɓʌdi\]',),
	(R'[voiced bilabial fricative](voiced%20bilabial%20fricative.md) \[β\]', '![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"',),
	(R'[voiced bilabial trill](voiced%20bilabial%20trill.md) \[ʙ\]', '![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)', R'[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"',),
	(R'[voiceless palatal plosive](voiceless%20palatal%20plosive.md) \[c\]', '![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)', R'[French](French%20language.md) _**q**ui_ \[ci\] "who"',),
	(R'[voiceless palatal fricative](voiceless%20palatal%20fricative.md) \[ç\]', '![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)', R'[English](English%20language.md) _**h**ue_ \[çʉː\]',),
	(R'[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) \[ɕ\]', '![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)', R'[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]',),
	(R'[voiced alveolar plosive](voiced%20alveolar%20plosive.md) \[d\]', '![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]',),
	(R'[voiced alveolar implosive](voiced%20alveolar%20implosive.md) \[ɗ\]', '![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)', R'[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"',),
	(R'[voiced retroflex plosive](voiced%20retroflex%20plosive.md) \[ɖ\]', '![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)', R'[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"',),
	(R'[voiced dental fricative](voiced%20dental%20fricative.md) \[ð\]', '![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**is_ \[ðɪs\]',),
	(R'[voiced alveolar affricate](voiced%20alveolar%20affricate.md) \[dz\]', '![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]',),
	(R'[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) \[dʒ\]', '![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _**g**ene_ 	\[ˈd͡ʒiːn\]',),
	(R'[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) \[dʑ\]', '![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"',),
	(R'[voiced retroflex affricate](voiced%20retroflex%20affricate.md) \[dʐ\]', '![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"',),
	(R'[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) \[e\]', '![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _m**ay**_ \[meː\]',),
	(R'[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) \[ɘ\]', '![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɘːd\]',),
	(R'[mid central vowel](mid%20central%20vowel.md) \[ə\]', '![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)', R'[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]',),
	(R'[r-colored mid central vowel](r-colored%20vowel.md) \[ɚ\]', '![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]',),
	(R'[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) \[ɛ\]', '![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**e**d_ \[bɛd\]',),
	(R'[nasalized open-mid front unrounded vowel](nasal%20vowel.md) \[ɛ̃\]', '![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)', R'[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"',),
	(R'[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) \[ɜ\]', '![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɜːd\]',),
	(R'[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) \[ɝ\]', '![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɝːd\]',),
	(R'[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) \[f\]', '![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**f**ill_ \[fɪɫ\]',),
	(R'[voiced velar plosive](voiced%20velar%20plosive.md) \[ɡ\]', '![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)', R'[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]',),
	(R'[voiced velar implosive](voiced%20velar%20implosive.md) \[ɠ\]', '![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
	(R'[voiced uvular plosive](voiced%20uvular%20plosive.md) \[ɢ\]', '![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)', R'[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]',),
	(R'[voiceless glottal fricative](voiceless%20glottal%20fricative.md) \[h\]', '![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)', R'[English](English%20language.md) _**h**igh_ \[haɪ̯\]',),
	(R'[voiced glottal fricative](voiced%20glottal%20fricative.md) \[ɦ\]', '![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)', R'[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]',),
	(R'[aspirated consonant](aspirated%20consonant.md) \[ʰ\]', '', R'[English](English%20langugae.md) _**t**op_ \[tʰɒp\]',),
	(R'[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) \[ħ\]', '![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)', R'[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]',),
	(R'[close front unrounded vowel](close%20front%20unrounded%20vowel.md) \[i\]', '![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _fr**ee**_ \[fɹiː\]',),
	(R'[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) \[ɪ\]', '![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**i**t_ \[bɪʔt\]',),
	(R'[close central unrounded vowel](close%20central%20unrounded%20vowel.md) \[ɨ\]', '![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)', R'[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"',),
	(R'[voiced palatal approximant](voiced%20palatal%20approximant.md) \[j\]', '![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)', R'[English](English%20language.md) _**y**ou_ \[juː\]',),
	(R'[palatalization](palatalization%20(phonetics).md) \[ʲ\]', '', R'[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"',),
	(R'[voiced palatal fricative](voiced%20palatal%20fricative.md) \[ʝ\]', '![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"',),
	(R'[voiced palatal plosive](voiced%20palatal%20plosive.md) \[ɟ\]', '![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)', R'[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"',),
	(R'[voiced palatal implosive](voiced%20palatal%20implosive.md) \[ʄ\]', '![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)', R'[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"',),
	(R'[voiceless velar plosive](voiceless%20velar%20plosive.md) \[k\]', '![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)', R'[English](English%20language.md) _**k**iss_ \[kʰɪs\]',),
	(R'[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) \[l\]', '![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _**l**et_ \[lɛt\]',),
	(R'[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) \[ɫ\]', '![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _fee**l**_ \[fiːɫ\]',),
	(R'[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) \[ɬ\]', '![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)', R'[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"',),
	(R'[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) \[ɭ\]', '![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)', R'[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"',),
	(R'[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) \[ɺ\]', '', R'[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"',),
	(R'[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) \[ɮ\]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', R'[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"',),
	(R'[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) \[ʟ\]', '![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]',),
	(R'[voiced bilabial nasal](voiced%20bilabial%20nasal.md) \[m\]', '![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)', R'[English](English%20language.md) _hi**m**_ \[hɪm\]',),
	(R'[voiced labiodental nasal](voiced%20labiodental%20nasal.md) \[ɱ\]', '![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)', R'[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]',),
	(R'[voiced alveolar nasal](voiced%20alveolar%20nasal.md) \[n\]', '![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)', R'[English](English%20language.md) _**n**ice_ \[naɪs\]',),
	(R'[voiced velar nasal](voiced%20velar%20nasal.md) \[ŋ\]', '![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)', R'[English](English%20language.md) _si**ng**_ \[sɪŋ\]',),
	(R'[voiced palatal nasal](voiced%20palatal%20nasal.md) \[ɲ\]', '![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)', R'[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"',),
	(R'[voiced retroflex nasal](voiced%20retroflex%20nasal.md) \[ɳ\]', '![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)', R'[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"',),
	(R'[voiced uvular nasal](voiced%20uvular%20nasal.md) \[ɴ\]', '![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)', R'[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"',),
	(R'[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) \[o\]', '![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _y**aw**n_ \[joːn\]',),
	(R'[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) \[ɔ\]', '![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɔt\]',),
	(R'[nasalized open-mid back rounded vowel](nasal%20vowel.md) \[ɔ̃\]', '![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)', R'[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"',),
	(R'[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) \[ø\]', '![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _p**eu**_ \[pø\] "few"',),
	(R'[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) \[ɵ\]', '![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)', '[English](English%20language.md) _f**oo**t_ \[fɵʔt\]',),
	(R'[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) \[œ\]', '![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"',),
	(R'[nasalized open-mid front rounded vowel](nasal%20vowel.md) \[œ̃\]', '![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)', R'[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"',),
	(R'[open front rounded vowel](open%20front%20rounded%20vowel.md) \[ɶ\]', '![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)', R'[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"',),
	(R'[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) \[p\]', '![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _**p**ack_ \[pʰæk\]',),
	(R'[voiceless uvular plosive](voiceless%20uvular%20plosive.md) \[q\]', '![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)', R'[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"',),
	(R'[voiced alveolar trill](voiced%20alveolar%20trill.md) \[r\]', '![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)', R'[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"',),
	(R'[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) \[ɾ\]', '![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)', R'[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"',),
	(R'[voiced uvular trill](voiced%20uvular%20trill.md) \[ʀ\]', '![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)', R'[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"',),
	(R'[voiced retroflex flap](voiced%20retroflex%20flap.md) \[ɽ\]', '![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)', R'[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"',),
	(R'[voiced alveolar approximant](voiced%20alveolar%20approximant.md) \[ɹ\]', '![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)', R'[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"',),
	(R'[voiced retroflex approximant](voiced%20retroflex%20approximant.md) \[ɻ\]', '![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)', R'[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"',),
	(R'[voiced uvular fricative](voiced%20uvular%20fricative.md) \[ʁ\]', '![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)', R'[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"',),
	(R'[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) \[s\]', '![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**s**it_ \[sɪt\]',),
	(R'[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) \[ʃ\]', '![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]',),
	(R'[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) \[ʂ\]', '![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)', R'[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"',),
	(R'[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) \[t\]', '![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**t**ick_ \[tʰɪk\]',),
	(R'[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) \[ʈ\]', '![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)', R'[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"',),
	(R'[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) \[ts\]', '![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]',),
	(R'[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) \[tʃ\]', '![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]',),
	(R'[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) \[tɕ\]', '![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"',),
	(R'[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) \[tʂ\]', '![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"',),
	(R'[close back rounded vowel](close%20back%20rounded%20vowel.md) \[u\]', '![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]',),
	(R'[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) \[ʊ\]', '![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _h**oo**k_ \[hʊʔk\]',),
	(R'[close central rounded vowel](close%20central%20rounded%20vowel.md) \[ʉ\]', '![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)', R'[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]',),
	(R'[voiced labiodental fricative](voiced%20labiodental%20fricative.md) \[v\]', '![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**v**al**v**e_ \[væɫv\]',),
	(R'[voiced labiodental approximant](voiced%20labiodental%20approximant.md) \[ʋ\]', '![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)', R'[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"',),
	(R'[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) \[w\]', '![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)', R'[English](English%20language.md) _**w**eep_ \[wiːp\]',),
	(R'[labialization](labialization.md) \[ʷ\]', '', R'[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]',),
	(R'[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) \[ʍ\]', '![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)', R'[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]',),
	(R'[close back unrounded vowel](close%20back%20unrounded%20vowel.md) \[ɯ\]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', R'[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"',),
	(R'[voiced velar approximant](voiced%20velar%20approximant.md) \[ɰ\]', '![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)', R'[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"',),
	(R'[voiceless velar fricative](voiceless%20velar%20fricative.md) \[x\]', '![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)', R'[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"',),
	(R'[voiceless uvular fricative](voiceless%20uvular%20fricative.md) \[χ\]', '![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)', R'[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"',),
	(R'[close front rounded vowel](close%20front%20rounded%20vowel.md) \[y\]', '![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _t**u**_ \[t̪y] "you"',),
	(R'[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) \[ʏ\]', '![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)', R'[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"',),
	(R'[voiced velar fricative](voiced%20velar%20fricative.md) \[ɣ\]', '![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"',),
	(R'[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) \[ɤ\]', '![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)', R'[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"',),
	(R'[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) \[ʎ\]', '![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)', R'[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]',),
	(R'[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) \[ɥ\]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', R'[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"',),
	(R'[voiced alveolar fricative](voiced%20alveolar%20fricative.md) \[z\]', '![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)', '[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]',),
	(R'[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) \[ʒ\]', '![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]',),
	(R'[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) \[ʑ\]', '![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)', R'[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"',),
	(R'[voiced retroflex fricative](voiced%20retroflex%20fricative.md) \[ʐ\]', '![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)', R'[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"',),
	(R'[voiceless dental fricative](voiceless%20dental%20fricative.md) \[θ\]', '![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**in_ \[θɪn\]',),
	(R'[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) \[ɸ\]', '![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)', R'[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"',),
	(R'[glottal stop](glottal%20stop.md) \[ʔ\]', '![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)', R'[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]',),
	(R'[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) \[ʕ\]', '![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)', R'[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"',),
	(R'[tenuis dental click](tenuis%20dental%20click.md) \[ǀ\]', '![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)', R'[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]',),
	(R'[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) \[ǁ\]', '![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)', R'[English](English%20language.md) _**tchick**_ \[ˈǁ\]',),
	(R'[tenuis alveolar click](tenuis%20alveolar%20click.md) \[ǃ\]', '![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)', R'[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"',),
	(R'[tenuis bilabial click](tenuis%20bilabial%20click.md) \[ʘ\]', '![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)', R'[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"',),
	(R'[tenuis palatal click](tenuis%20palatal%20click.md) \[ǂ\]', '![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)', R'[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"',),
)
diacritics = (
	(R'[nasalized](nasal%20vowel.md) \[◌̃\] (e.g. [ã])', R'[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"',),
	(R'[centralized](central%20vowel.md) \[◌̈\] (e.g. [ä])', R'[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"',),
	(R'[extra-short](extra-shortness.md) \[◌̆\] (e.g. [ă])', R'[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]',),
	(R'[non-syllabic](diphthong.md) \[◌̯\] (e.g. [a̯])', R'[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]',),
	(R'[voiceless](voicelessness.md) \[◌̥\] (e.g. [n̥])', R'[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]',),
	(R'[syllabic](syllabic%20consonant.md) \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])', R'[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]',),
	(R'[dental/alveolar](dental%20consonant.md) \[◌̪\] (e.g. [d̪])', R'[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"',),
	(R'[aspirated](aspirated%20consonant.md) \[◌ʰ\] (e.g. [kʰ])', R'[English](English%20language.md) _**c**ome_ \[kʰɐm\]',),
	(R'[ejective](ejective%20consonant.md) \[◌’\] (e.g. [k’])', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
	(R'[long](longness%20(phonetics).md) \[◌ː\] (e.g. [aː])', R'[English](English%20language.md) _shh!_ \[ʃː\]',),
	(R'[half-long](half-longness%20(phonetics).md) \[◌ˑ\] (e.g. [aˑ])', R'[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]',),
	(R'[primary stress](stress%20(lingustics).md) \[ˈ◌\] (e.g. [ˈa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
	(R'[secondary stress](secondary%20stress.md) \[ˌ◌\] (e.g. [ˌa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
	(R'[syllable break](syllable.md) \[.\]', R'[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]',),
)
return chain.from_iterable(await gather(
	memorize_table(
		(*e.cwf_sects("958a"), NULL_LOCATION,),
		("symbol", f"audio", "description",),
		letters,
		lambda datum: chain(datum[:2], map(cloze, datum[2:])),
	),
	memorize_map(
		(NULL_LOCATION, *e.cwf_sects("5dfb", "f9aa"),),
		items_to_map(*map(lambda datum: datum[:2], letters)),
	),
	memorize_table(
		(*e.cwf_sects("485d"), NULL_LOCATION,),
		("symbol", "description",),
		diacritics,
		lambda datum: map(cloze, datum),
	),
))
```
%%

### glossary

> ![places of articulation](../../archives/Wikimedia%20Commons/Places%20of%20articulation.svg)
>
> [place of articulation](place%20of%20articulation.md)
> 1. {{exo-labial (outer [lip](lip.md))}}
> 2. {{endo-labial (inner [lip](lip.md))}}
> 3. {{dental ([teeth](tooth.md))}}
> 4. {{alveolar (front [alveolar ridge](alveolar%20ridge.md))}}
> 5. {{post-alveolar (rear [alveolar ridge](alveolar%20ridge.md))}}
> 6. {{pre-palatal (front [hard palate](hard%20palate.md))}}
> 7. {{palatal ([hard palate](hard%20palate.md))}}
> 8. {{velar ([soft palate](soft%20palate.md))}}
> 9. {{uvular/post-velar ([uvula](uvula.md))}}
> 10. {{pharyngeal ([pharyngeal](pharynx.md) wall)}}
> 11. {{glottal/laryngeal ([vocal cords](vocal%20cords.md))}}
> 12. {{epiglottal ([epiglottis](epiglottis.md))}}
> 13. {{radical ([tongue](tongue.md) root)}}
> 14. {{postero-dorsal (rear [tongue](tongue.md) body)}}
> 15. {{antero-dorsal (front [tongue](tongue.md) body)}}
> 16. {{laminal ([tongue](tongue.md) blade)}}
> 17. {{apical ([tongue](tongue.md) tip or apex)}}
> 18. {{sub-laminal/sub-apical ([tongue](tongue.md) underside)}} <!--SR:!2023-07-20,25,290!2023-07-30,34,298!2023-07-31,35,304!2023-07-27,32,304!2023-08-01,36,304!2023-07-25,30,304!2023-07-11,16,284!2023-07-12,17,293!2023-07-27,32,313!2023-07-13,17,273!2023-07-16,20,293!2023-08-01,36,313-->

- [consonant](consonant.md):::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2023-07-14,18,270!2023-07-21,26,290-->
	- [airstream mechanism](airstream%20mechanism.md):::how the moving [air](air.md) is thrusted <!--SR:!2023-07-19,24,298!2023-07-25,30,303-->
		- (all) [pulmonic](pulmonic%20consonant.md) egressive:::[air](air.md) is exhaled from the [lungs](lung.md) <!--SR:!2023-07-25,30,313-->
		- (16%) [glottalic](glottalic%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md)
		- (13%) [glottalic](glottalic%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md)
		- (<2%) lingual/[velaric](velar%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md)
		- ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive:::[air](air.md) is inhaled into the [lungs](lung.md) <!--SR:!2023-07-26,31,313!2023-07-27,32,313-->
		- ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md)
	- [length](gemination.md):::how long the articulation of a [consonant](consonant.md) lasts
		- values in ascending [length](gemination.md)::single/singleton, geminate, long geminate <!--SR:!2023-07-15,19,293-->
	- [manner of articulation](manner%20of%20articulation.md):::configuration and interaction of the [speech organs](speech%20organ.md)
		- [affricate](affricate%20consonant.md):::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md)
		- [approximant](approximant%20consonant.md):::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md) <!--SR:!2023-08-24,45,273-->
			- [lateral approximant](lateral%20consonant.md):::approximant with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2023-07-13,18,284!2023-07-26,31,304-->
			- [semivowel/glide/semiconsonant](semivowel.md):::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary
		- [flap/tap](tap%20and%20flap%20consonants.md):::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact
		- [fricative/spirant](fricative%20consonant.md):::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation <!--SR:!2023-07-13,17,264-->
			- [lateral](lateral%20consonant.md):::fricative with airflow directed towards one or both sides of the [tongue](tongue.md)
			- [sibilant](sibilant%20consonant.md):::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md)
		- [nasal](nasal%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow
		- [plosive/stop](plosive%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow
		- [trill](trill%20consonant.md):::consonant produced by vibrations between the active articulator and the passive articulator
	- [place of articulation](place%20of%20articulation.md):::location along the [vocal tract](vocal%20tract.md) producing the consonant <!--SR:!2023-07-11,16,284-->
		- [alveolar](alveolar%20ridge.md):::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive)
		- [aryepiglottal](pharyngeal%20consonant.md):::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active) <!--SR:!2023-08-24,47,313-->
		- [coronal](coronal%20constant.md):::front of the [tongue](tongue.md) (active) <!--SR:!2023-07-19,24,293-->
			- [apical](apical%20consonant.md):::tip of the [tongue](tongue.md) (active) <!--SR:!2023-07-27,32,304-->
			- [laminal](laminal%20consonant.md):::blade of the [tongue](tongue.md), the upper front surface behind the tip (active) <!--SR:!2023-07-11,15,253-->
			- [subapical](subapical%20consonant.md):::surface under the tip of the [tongue](tongue.md) (active) <!--SR:!2023-07-26,31,304!2023-07-30,34,313-->
		- [dental](dental%20consonant.md):::upper [teeth](tooth.md) (passive) <!--SR:!2023-07-28,26,293-->
		- [dorsal](dorsal%20consonant.md):::body of the [tongue](tongue.md) (active) <!--SR:!2023-08-26,49,313!2023-07-31,35,313-->
		- [epiglottal](pharyngeal%20consonant.md):::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive)
		- [glottal](glottal%20consonant.md):::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active) <!--SR:!2023-07-15,13,273!2023-07-31,35,313-->
		- [labial](labial%20consonant.md):::lower [lip](lip.md) (active), upper [lip](lip.md) (passive) <!--SR:!2023-08-06,29,264!2023-07-27,32,313-->
		- [palatal](palatal%20consonant.md):::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2023-07-24,29,284-->
		- [pharyngeal](pharyngeal%20consonant.md):::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive)
		- [post-alveolar](post-alveolar%20consonant.md):::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive)
		- [uvular](uvular%20consonant.md):::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive) <!--SR:!2023-07-12,17,284-->
		- [velar](velar%20consonant.md):::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive)
	- [phonation](phonation.md):::how the [vocal cords](vocal%20folds.md) vibrate
		- [voiced](voice%20(phonetics).md):::the [vocal cords](vocal%20cords.md) vibrate fully <!--SR:!2023-07-22,27,304-->
		- [voiceless](voicelessness.md):::the [vocal cords](vocal%20cords.md) do not vibrate <!--SR:!2023-07-25,30,313!2023-08-02,37,313-->
	- [voice onset time](voice%20onset%20time.md) (VOT):::timing of [phonation](phonation.md) <!--SR:!2023-07-21,26,313-->
		- values in ascending [VOT](voice%20onset%20time.md)::[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive) <!--SR:!2023-07-25,29,284-->
- [vowel](vowel.md):::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md)
	- [vowel backness](vowel.md#backness):::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md) <!--SR:!2023-07-22,27,284-->
		- values in ascending [vowel backness](vowel.md#backness)::[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md) <!--SR:!2023-07-25,30,304-->
	- [vowel height](vowel.md#height):::vertical position of the [tongue](tongue.md)
		- values in descending [vowel height](vowel.md#height)::[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md)
	- [vowel roundedness](roundedness.md):::rounding of the [lips](lip.md) <!--SR:!2023-07-26,31,293-->
		- values in ascending [vowel roundedness](roundedness.md)::unrounded, compressed, protruded

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]:::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md) <!--SR:!2023-07-12,16,264-->
- (principal) /[slashes](slash%20(punctuation).md)/:::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only <!--SR:!2023-07-16,20,293-->
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses)):::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md) <!--SR:!2023-07-15,19,293-->
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses))):::transcription of obscured speech or description of obscuring sound <!--SR:!2023-07-23,28,284!2023-07-12,17,284-->
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]:::extra-precise transcription
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[morphophonemic](morphophonology.md) transcription
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫:::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves

### letters

Here is a list of common IPA letters and their pronunciations:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="958a"--><!-- The following content is generated at 2023-07-10T23:58:13.198861+08:00. Any edits will be overridden! -->

> | symbol | audio | description |
> |-|-|-|
> | [open front unrounded vowel](open%20front%20unrounded%20vowel.md) \[a\] | ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _h**a**t_ \[hat\]}} |
> | [open central unrounded vowel](open%20central%20unrounded%20vowel.md) \[ä\] | ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _br**a**_ \[bɹäː\]}} |
> | [near-open central vowel](near-open%20central%20vowel.md) \[ɐ\] | ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _n**u**t_ \[nɐʔt\]}} |
> | [open back unrounded vowel](open%20back%20unrounded%20vowel.md) \[ɑ\] | ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]}} |
> | [nasalized open back unrounded vowel](nasal%20vowel.md) \[ɑ̃\] | ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) | {{[French](French%20language.md) _s**an**s_ [sɑ̃] "without"}} |
> | [open back rounded vowel](open%20back%20rounded%20vowel.md) \[ɒ\] | ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _n**o**t_ \[nɒt\]}} |
> | [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) \[ʌ\] | ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) | {{[English](English%20language.md) _g**u**t_ \[ɡʌt\]}} |
> | [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) \[æ\] | ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _c**a**t_ \[kʰæt\]}} |
> | [voiced bilabial plosive](voiced%20bilabial%20plosive.md) \[b\] | ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) | {{[English](English%20language.md) _a**b**ack_ \[əˈbæk\]}} |
> | [voiced bilabial implosive](voiced%20bilabial%20implosive.md) \[ɓ\] | ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) | {{[English](English%20language.md) _**b**ody_ \[ɓʌdi\]}} |
> | [voiced bilabial fricative](voiced%20bilabial%20fricative.md) \[β\] | ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"}} |
> | [voiced bilabial trill](voiced%20bilabial%20trill.md) \[ʙ\] | ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) | {{[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"}} |
> | [voiceless palatal plosive](voiceless%20palatal%20plosive.md) \[c\] | ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) | {{[French](French%20language.md) _**q**ui_ \[ci\] "who"}} |
> | [voiceless palatal fricative](voiceless%20palatal%20fricative.md) \[ç\] | ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) | {{[English](English%20language.md) _**h**ue_ \[çʉː\]}} |
> | [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) \[ɕ\] | ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) | {{[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]}} |
> | [voiced alveolar plosive](voiced%20alveolar%20plosive.md) \[d\] | ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) | {{[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]}} |
> | [voiced alveolar implosive](voiced%20alveolar%20implosive.md) \[ɗ\] | ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) | {{[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"}} |
> | [voiced retroflex plosive](voiced%20retroflex%20plosive.md) \[ɖ\] | ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga) | {{[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"}} |
> | [voiced dental fricative](voiced%20dental%20fricative.md) \[ð\] | ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) | {{[English](English%20language.md) _**th**is_ \[ðɪs\]}} |
> | [voiced alveolar affricate](voiced%20alveolar%20affricate.md) \[dz\] | ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga) | {{[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]}} |
> | [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) \[dʒ\] | ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) | {{[English](English%20language.md) _**g**ene_ 	\[ˈd͡ʒiːn\]}} |
> | [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) \[dʑ\] | ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) | {{[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"}} |
> | [voiced retroflex affricate](voiced%20retroflex%20affricate.md) \[dʐ\] | ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) | {{[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"}} |
> | [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) \[e\] | ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _m**ay**_ \[meː\]}} |
> | [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) \[ɘ\] | ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɘːd\]}} |
> | [mid central vowel](mid%20central%20vowel.md) \[ə\] | ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) | {{[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]}} |
> | [r-colored mid central vowel](r-colored%20vowel.md) \[ɚ\] | ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | {{[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]}} |
> | [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) \[ɛ\] | ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**e**d_ \[bɛd\]}} |
> | [nasalized open-mid front unrounded vowel](nasal%20vowel.md) \[ɛ̃\] | ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) | {{[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"}} |
> | [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) \[ɜ\] | ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɜːd\]}} |
> | [r-colored open-mid central unrounded vowel](r-colored%20vowel.md) \[ɝ\] | ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɝːd\]}} |
> | [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) \[f\] | ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) | {{[English](English%20language.md) _**f**ill_ \[fɪɫ\]}} |
> | [voiced velar plosive](voiced%20velar%20plosive.md) \[ɡ\] | ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) | {{[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]}} |
> | [voiced velar implosive](voiced%20velar%20implosive.md) \[ɠ\] | ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | [voiced uvular plosive](voiced%20uvular%20plosive.md) \[ɢ\] | ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga) | {{[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]}} |
> | [voiceless glottal fricative](voiceless%20glottal%20fricative.md) \[h\] | ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) | {{[English](English%20language.md) _**h**igh_ \[haɪ̯\]}} |
> | [voiced glottal fricative](voiced%20glottal%20fricative.md) \[ɦ\] | ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) | {{[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]}} |
> | [aspirated consonant](aspirated%20consonant.md) \[ʰ\] |  | {{[English](English%20langugae.md) _**t**op_ \[tʰɒp\]}} |
> | [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) \[ħ\] | ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) | {{[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]}} |
> | [close front unrounded vowel](close%20front%20unrounded%20vowel.md) \[i\] | ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _fr**ee**_ \[fɹiː\]}} |
> | [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) \[ɪ\] | ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**i**t_ \[bɪʔt\]}} |
> | [close central unrounded vowel](close%20central%20unrounded%20vowel.md) \[ɨ\] | ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) | {{[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"}} |
> | [voiced palatal approximant](voiced%20palatal%20approximant.md) \[j\] | ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) | {{[English](English%20language.md) _**y**ou_ \[juː\]}} |
> | [palatalization](palatalization%20(phonetics).md) \[ʲ\] |  | {{[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"}} |
> | [voiced palatal fricative](voiced%20palatal%20fricative.md) \[ʝ\] | ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"}} |
> | [voiced palatal plosive](voiced%20palatal%20plosive.md) \[ɟ\] | ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) | {{[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"}} |
> | [voiced palatal implosive](voiced%20palatal%20implosive.md) \[ʄ\] | ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) | {{[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"}} |
> | [voiceless velar plosive](voiceless%20velar%20plosive.md) \[k\] | ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) | {{[English](English%20language.md) _**k**iss_ \[kʰɪs\]}} |
> | [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) \[l\] | ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _**l**et_ \[lɛt\]}} |
> | [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) \[ɫ\] | ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _fee**l**_ \[fiːɫ\]}} |
> | [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) \[ɬ\] | ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) | {{[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"}} |
> | [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) \[ɭ\] | ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) | {{[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"}} |
> | [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) \[ɺ\] |  | {{[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"}} |
> | [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) \[ɮ\] | ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) | {{[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"}} |
> | [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) \[ʟ\] | ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]}} |
> | [voiced bilabial nasal](voiced%20bilabial%20nasal.md) \[m\] | ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) | {{[English](English%20language.md) _hi**m**_ \[hɪm\]}} |
> | [voiced labiodental nasal](voiced%20labiodental%20nasal.md) \[ɱ\] | ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) | {{[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]}} |
> | [voiced alveolar nasal](voiced%20alveolar%20nasal.md) \[n\] | ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) | {{[English](English%20language.md) _**n**ice_ \[naɪs\]}} |
> | [voiced velar nasal](voiced%20velar%20nasal.md) \[ŋ\] | ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) | {{[English](English%20language.md) _si**ng**_ \[sɪŋ\]}} |
> | [voiced palatal nasal](voiced%20palatal%20nasal.md) \[ɲ\] | ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) | {{[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"}} |
> | [voiced retroflex nasal](voiced%20retroflex%20nasal.md) \[ɳ\] | ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) | {{[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"}} |
> | [voiced uvular nasal](voiced%20uvular%20nasal.md) \[ɴ\] | ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) | {{[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"}} |
> | [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) \[o\] | ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _y**aw**n_ \[joːn\]}} |
> | [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) \[ɔ\] | ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _n**o**t_ \[nɔt\]}} |
> | [nasalized open-mid back rounded vowel](nasal%20vowel.md) \[ɔ̃\] | ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) | {{[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"}} |
> | [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) \[ø\] | ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _p**eu**_ \[pø\] "few"}} |
> | [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) \[ɵ\] | ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) | {{[English](English%20language.md) _f**oo**t_ \[fɵʔt\]}} |
> | [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) \[œ\] | ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"}} |
> | [nasalized open-mid front rounded vowel](nasal%20vowel.md) \[œ̃\] | ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) | {{[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"}} |
> | [open front rounded vowel](open%20front%20rounded%20vowel.md) \[ɶ\] | ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) | {{[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"}} |
> | [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) \[p\] | ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) | {{[English](English%20language.md) _**p**ack_ \[pʰæk\]}} |
> | [voiceless uvular plosive](voiceless%20uvular%20plosive.md) \[q\] | ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) | {{[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"}} |
> | [voiced alveolar trill](voiced%20alveolar%20trill.md) \[r\] | ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) | {{[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"}} |
> | [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) \[ɾ\] | ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) | {{[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"}} |
> | [voiced uvular trill](voiced%20uvular%20trill.md) \[ʀ\] | ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) | {{[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"}} |
> | [voiced retroflex flap](voiced%20retroflex%20flap.md) \[ɽ\] | ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) | {{[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"}} |
> | [voiced alveolar approximant](voiced%20alveolar%20approximant.md) \[ɹ\] | ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) | {{[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"}} |
> | [voiced retroflex approximant](voiced%20retroflex%20approximant.md) \[ɻ\] | ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga) | {{[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"}} |
> | [voiced uvular fricative](voiced%20uvular%20fricative.md) \[ʁ\] | ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) | {{[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"}} |
> | [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) \[s\] | ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**s**it_ \[sɪt\]}} |
> | [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) \[ʃ\] | ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]}} |
> | [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) \[ʂ\] | ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) | {{[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"}} |
> | [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) \[t\] | ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) | {{[English](English%20language.md) _**t**ick_ \[tʰɪk\]}} |
> | [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) \[ʈ\] | ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga) | {{[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"}} |
> | [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) \[ts\] | ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga) | {{[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]}} |
> | [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) \[tʃ\] | ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) | {{[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]}} |
> | [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) \[tɕ\] | ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) | {{[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"}} |
> | [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) \[tʂ\] | ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) | {{[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"}} |
> | [close back rounded vowel](close%20back%20rounded%20vowel.md) \[u\] | ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]}} |
> | [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) \[ʊ\] | ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _h**oo**k_ \[hʊʔk\]}} |
> | [close central rounded vowel](close%20central%20rounded%20vowel.md) \[ʉ\] | ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) | {{[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]}} |
> | [voiced labiodental fricative](voiced%20labiodental%20fricative.md) \[v\] | ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) | {{[English](English%20language.md) _**v**al**v**e_ \[væɫv\]}} |
> | [voiced labiodental approximant](voiced%20labiodental%20approximant.md) \[ʋ\] | ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) | {{[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"}} |
> | [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) \[w\] | ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) | {{[English](English%20language.md) _**w**eep_ \[wiːp\]}} |
> | [labialization](labialization.md) \[ʷ\] |  | {{[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]}} |
> | [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) \[ʍ\] | ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) | {{[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]}} |
> | [close back unrounded vowel](close%20back%20unrounded%20vowel.md) \[ɯ\] | ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) | {{[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"}} |
> | [voiced velar approximant](voiced%20velar%20approximant.md) \[ɰ\] | ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) | {{[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"}} |
> | [voiceless velar fricative](voiceless%20velar%20fricative.md) \[x\] | ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) | {{[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"}} |
> | [voiceless uvular fricative](voiceless%20uvular%20fricative.md) \[χ\] | ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) | {{[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"}} |
> | [close front rounded vowel](close%20front%20rounded%20vowel.md) \[y\] | ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _t**u**_ \[t̪y] "you"}} |
> | [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) \[ʏ\] | ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) | {{[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"}} |
> | [voiced velar fricative](voiced%20velar%20fricative.md) \[ɣ\] | ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"}} |
> | [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) \[ɤ\] | ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) | {{[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"}} |
> | [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) \[ʎ\] | ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) | {{[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]}} |
> | [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) \[ɥ\] | ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) | {{[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"}} |
> | [voiced alveolar fricative](voiced%20alveolar%20fricative.md) \[z\] | ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]}} |
> | [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) \[ʒ\] | ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg) | {{[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]}} |
> | [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) \[ʑ\] | ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg) | {{[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"}} |
> | [voiced retroflex fricative](voiced%20retroflex%20fricative.md) \[ʐ\] | ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg) | {{[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"}} |
> | [voiceless dental fricative](voiceless%20dental%20fricative.md) \[θ\] | ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) | {{[English](English%20language.md) _**th**in_ \[θɪn\]}} |
> | [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) \[ɸ\] | ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) | {{[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"}} |
> | [glottal stop](glottal%20stop.md) \[ʔ\] | ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg) | {{[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]}} |
> | [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) \[ʕ\] | ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg) | {{[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"}} |
> | [tenuis dental click](tenuis%20dental%20click.md) \[ǀ\] | ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) | {{[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]}} |
> | [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) \[ǁ\] | ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) | {{[English](English%20language.md) _**tchick**_ \[ˈǁ\]}} |
> | [tenuis alveolar click](tenuis%20alveolar%20click.md) \[ǃ\] | ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) | {{[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"}} |
> | [tenuis bilabial click](tenuis%20bilabial%20click.md) \[ʘ\] | ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg) | {{[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"}} |
> | [tenuis palatal click](tenuis%20palatal%20click.md) \[ǂ\] | ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) | {{[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"}} | <!--SR:!2023-07-21,26,290!2023-08-21,42,250!2023-07-11,1,184!2023-07-14,12,244!2023-07-30,34,304!2023-07-18,10,224!2023-07-20,25,284!2023-07-12,3,204!2023-07-12,17,284!2023-08-23,44,264!2023-08-21,42,264!2023-08-22,43,264!2023-07-14,18,284!2023-07-11,2,193!2023-07-12,3,213!2023-07-12,10,253!2023-07-11,9,213!2023-07-15,5,233!2023-07-11,16,273-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5dfb"--><!-- The following content is generated at 2023-06-18T11:06:10.499505+08:00. Any edits will be overridden! -->

1. [open front unrounded vowel](open%20front%20unrounded%20vowel.md) \[a\]::![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)
2. [open central unrounded vowel](open%20central%20unrounded%20vowel.md) \[ä\]::![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) <!--SR:!2023-07-11,15,264-->
3. [near-open central vowel](near-open%20central%20vowel.md) \[ɐ\]::![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) <!--SR:!2023-08-17,39,264-->
4. [open back unrounded vowel](open%20back%20unrounded%20vowel.md) \[ɑ\]::![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) <!--SR:!2023-07-16,20,293-->
5. [nasalized open back unrounded vowel](nasal%20vowel.md) \[ɑ̃\]::![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)
6. [open back rounded vowel](open%20back%20rounded%20vowel.md) \[ɒ\]::![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) <!--SR:!2023-07-26,31,304-->
7. [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) \[ʌ\]::![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) <!--SR:!2023-07-16,20,293-->
8. [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) \[æ\]::![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)
9. [voiced bilabial plosive](voiced%20bilabial%20plosive.md) \[b\]::![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)
10. [voiced bilabial implosive](voiced%20bilabial%20implosive.md) \[ɓ\]::![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)
11. [voiced bilabial fricative](voiced%20bilabial%20fricative.md) \[β\]::![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)
12. [voiced bilabial trill](voiced%20bilabial%20trill.md) \[ʙ\]::![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)
13. [voiceless palatal plosive](voiceless%20palatal%20plosive.md) \[c\]::![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)
14. [voiceless palatal fricative](voiceless%20palatal%20fricative.md) \[ç\]::![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)
15. [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) \[ɕ\]::![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)
16. [voiced alveolar plosive](voiced%20alveolar%20plosive.md) \[d\]::![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) <!--SR:!2023-07-24,29,298-->
17. [voiced alveolar implosive](voiced%20alveolar%20implosive.md) \[ɗ\]::![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)
18. [voiced retroflex plosive](voiced%20retroflex%20plosive.md) \[ɖ\]::![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)
19. [voiced dental fricative](voiced%20dental%20fricative.md) \[ð\]::![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) <!--SR:!2023-07-22,27,304-->
20. [voiced alveolar affricate](voiced%20alveolar%20affricate.md) \[dz\]::![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)
21. [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) \[dʒ\]::![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)
22. [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) \[dʑ\]::![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)
23. [voiced retroflex affricate](voiced%20retroflex%20affricate.md) \[dʐ\]::![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)
24. [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) \[e\]::![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)
25. [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) \[ɘ\]::![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)
26. [mid central vowel](mid%20central%20vowel.md) \[ə\]::![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) <!--SR:!2023-07-13,18,284-->
27. [r-colored mid central vowel](r-colored%20vowel.md) \[ɚ\]::![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)
28. [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) \[ɛ\]::![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)
29. [nasalized open-mid front unrounded vowel](nasal%20vowel.md) \[ɛ̃\]::![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)
30. [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) \[ɜ\]::![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)
31. [r-colored open-mid central unrounded vowel](r-colored%20vowel.md) \[ɝ\]::![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)
32. [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) \[f\]::![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)
33. [voiced velar plosive](voiced%20velar%20plosive.md) \[ɡ\]::![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)
34. [voiced velar implosive](voiced%20velar%20implosive.md) \[ɠ\]::![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)
35. [voiced uvular plosive](voiced%20uvular%20plosive.md) \[ɢ\]::![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)
36. [voiceless glottal fricative](voiceless%20glottal%20fricative.md) \[h\]::![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)
37. [voiced glottal fricative](voiced%20glottal%20fricative.md) \[ɦ\]::![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)
38. [aspirated consonant](aspirated%20consonant.md) \[ʰ\]:: <!--SR:!2023-07-23,28,304-->
39. [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) \[ħ\]::![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)
40. [close front unrounded vowel](close%20front%20unrounded%20vowel.md) \[i\]::![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) <!--SR:!2023-08-02,37,313-->
41. [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) \[ɪ\]::![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)
42. [close central unrounded vowel](close%20central%20unrounded%20vowel.md) \[ɨ\]::![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)
43. [voiced palatal approximant](voiced%20palatal%20approximant.md) \[j\]::![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)
44. [palatalization](palatalization%20(phonetics).md) \[ʲ\]::
45. [voiced palatal fricative](voiced%20palatal%20fricative.md) \[ʝ\]::![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) <!--SR:!2023-08-23,44,264-->
46. [voiced palatal plosive](voiced%20palatal%20plosive.md) \[ɟ\]::![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)
47. [voiced palatal implosive](voiced%20palatal%20implosive.md) \[ʄ\]::![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)
48. [voiceless velar plosive](voiceless%20velar%20plosive.md) \[k\]::![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)
49. [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) \[l\]::![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)
50. [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) \[ɫ\]::![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)
51. [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) \[ɬ\]::![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) <!--SR:!2023-07-17,9,204-->
52. [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) \[ɭ\]::![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)
53. [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) \[ɺ\]:: <!--SR:!2023-07-12,17,270-->
54. [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) \[ɮ\]::![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)
55. [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) \[ʟ\]::![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)
56. [voiced bilabial nasal](voiced%20bilabial%20nasal.md) \[m\]::![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)
57. [voiced labiodental nasal](voiced%20labiodental%20nasal.md) \[ɱ\]::![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)
58. [voiced alveolar nasal](voiced%20alveolar%20nasal.md) \[n\]::![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)
59. [voiced velar nasal](voiced%20velar%20nasal.md) \[ŋ\]::![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)
60. [voiced palatal nasal](voiced%20palatal%20nasal.md) \[ɲ\]::![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)
61. [voiced retroflex nasal](voiced%20retroflex%20nasal.md) \[ɳ\]::![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)
62. [voiced uvular nasal](voiced%20uvular%20nasal.md) \[ɴ\]::![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) <!--SR:!2023-07-11,16,273-->
63. [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) \[o\]::![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)
64. [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) \[ɔ\]::![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)
65. [nasalized open-mid back rounded vowel](nasal%20vowel.md) \[ɔ̃\]::![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)
66. [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) \[ø\]::![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)
67. [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) \[ɵ\]::![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)
68. [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) \[œ\]::![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) <!--SR:!2023-07-29,21,244-->
69. [nasalized open-mid front rounded vowel](nasal%20vowel.md) \[œ̃\]::![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)
70. [open front rounded vowel](open%20front%20rounded%20vowel.md) \[ɶ\]::![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)
71. [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) \[p\]::![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) <!--SR:!2023-07-24,29,293-->
72. [voiceless uvular plosive](voiceless%20uvular%20plosive.md) \[q\]::![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)
73. [voiced alveolar trill](voiced%20alveolar%20trill.md) \[r\]::![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)
74. [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) \[ɾ\]::![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) <!--SR:!2023-07-27,32,304-->
75. [voiced uvular trill](voiced%20uvular%20trill.md) \[ʀ\]::![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)
76. [voiced retroflex flap](voiced%20retroflex%20flap.md) \[ɽ\]::![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)
77. [voiced alveolar approximant](voiced%20alveolar%20approximant.md) \[ɹ\]::![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) <!--SR:!2023-07-11,16,273-->
78. [voiced retroflex approximant](voiced%20retroflex%20approximant.md) \[ɻ\]::![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)
79. [voiced uvular fricative](voiced%20uvular%20fricative.md) \[ʁ\]::![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)
80. [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) \[s\]::![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)
81. [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) \[ʃ\]::![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) <!--SR:!2023-08-23,44,264-->
82. [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) \[ʂ\]::![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)
83. [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) \[t\]::![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)
84. [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) \[ʈ\]::![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)
85. [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) \[ts\]::![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)
86. [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) \[tʃ\]::![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)
87. [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) \[tɕ\]::![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)
88. [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) \[tʂ\]::![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)
89. [close back rounded vowel](close%20back%20rounded%20vowel.md) \[u\]::![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)
90. [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) \[ʊ\]::![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)
91. [close central rounded vowel](close%20central%20rounded%20vowel.md) \[ʉ\]::![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)
92. [voiced labiodental fricative](voiced%20labiodental%20fricative.md) \[v\]::![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)
93. [voiced labiodental approximant](voiced%20labiodental%20approximant.md) \[ʋ\]::![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)
94. [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) \[w\]::![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) <!--SR:!2023-07-13,18,293-->
95. [labialization](labialization.md) \[ʷ\]::
96. [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) \[ʍ\]::![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)
97. [close back unrounded vowel](close%20back%20unrounded%20vowel.md) \[ɯ\]::![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)
98. [voiced velar approximant](voiced%20velar%20approximant.md) \[ɰ\]::![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)
99. [voiceless velar fricative](voiceless%20velar%20fricative.md) \[x\]::![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)
100. [voiceless uvular fricative](voiceless%20uvular%20fricative.md) \[χ\]::![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)
101. [close front rounded vowel](close%20front%20rounded%20vowel.md) \[y\]::![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)
102. [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) \[ʏ\]::![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)
103. [voiced velar fricative](voiced%20velar%20fricative.md) \[ɣ\]::![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)
104. [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) \[ɤ\]::![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)
105. [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) \[ʎ\]::![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)
106. [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) \[ɥ\]::![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) <!--SR:!2023-07-12,4,253-->
107. [voiced alveolar fricative](voiced%20alveolar%20fricative.md) \[z\]::![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) <!--SR:!2023-07-13,18,284-->
108. [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) \[ʒ\]::![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)
109. [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) \[ʑ\]::![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)
110. [voiced retroflex fricative](voiced%20retroflex%20fricative.md) \[ʐ\]::![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)
111. [voiceless dental fricative](voiceless%20dental%20fricative.md) \[θ\]::![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)
112. [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) \[ɸ\]::![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) <!--SR:!2023-07-18,16,273-->
113. [glottal stop](glottal%20stop.md) \[ʔ\]::![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)
114. [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) \[ʕ\]::![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)
115. [tenuis dental click](tenuis%20dental%20click.md) \[ǀ\]::![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)
116. [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) \[ǁ\]::![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) <!--SR:!2023-07-12,16,264-->
117. [tenuis alveolar click](tenuis%20alveolar%20click.md) \[ǃ\]::![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)
118. [tenuis bilabial click](tenuis%20bilabial%20click.md) \[ʘ\]::![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)
119. [tenuis palatal click](tenuis%20palatal%20click.md) \[ǂ\]::![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f9aa"--><!-- The following content is generated at 2023-06-18T11:06:15.561456+08:00. Any edits will be overridden! -->

1. ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) \[a\]
2. ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) \[ä\] <!--SR:!2023-07-15,19,293-->
3. ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)::[near-open central vowel](near-open%20central%20vowel.md) \[ɐ\]
4. ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) \[ɑ\]
5. ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)::[nasalized open back unrounded vowel](nasal%20vowel.md) \[ɑ̃\]
6. ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)::[open back rounded vowel](open%20back%20rounded%20vowel.md) \[ɒ\]
7. ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) \[ʌ\]
8. ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) \[æ\]
9. ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) \[b\]
10. ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) \[ɓ\]
11. ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) \[β\]
12. ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)::[voiced bilabial trill](voiced%20bilabial%20trill.md) \[ʙ\]
13. ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) \[c\]
14. ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) \[ç\]
15. ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) \[ɕ\]
16. ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) \[d\] <!--SR:!2023-07-12,16,273-->
17. ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) \[ɗ\]
18. ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) \[ɖ\]
19. ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)::[voiced dental fricative](voiced%20dental%20fricative.md) \[ð\]
20. ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) \[dz\]
21. ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) \[dʒ\]
22. ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) \[dʑ\]
23. ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) \[dʐ\]
24. ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) \[e\]
25. ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) \[ɘ\]
26. ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)::[mid central vowel](mid%20central%20vowel.md) \[ə\]
27. ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored mid central vowel](r-colored%20vowel.md) \[ɚ\]
28. ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) \[ɛ\]
29. ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) \[ɛ̃\]
30. ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) \[ɜ\]
31. ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) \[ɝ\]
32. ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) \[f\] <!--SR:!2023-07-18,10,233-->
33. ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)::[voiced velar plosive](voiced%20velar%20plosive.md) \[ɡ\]
34. ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)::[voiced velar implosive](voiced%20velar%20implosive.md) \[ɠ\]
35. ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)::[voiced uvular plosive](voiced%20uvular%20plosive.md) \[ɢ\]
36. ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) \[h\]
37. ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)::[voiced glottal fricative](voiced%20glottal%20fricative.md) \[ɦ\]
38. ::[aspirated consonant](aspirated%20consonant.md) \[ʰ\], [palatalization](palatalization%20(phonetics).md) \[ʲ\], [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) \[ɺ\], [labialization](labialization.md) \[ʷ\]
39. ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) \[ħ\]
40. ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)::[close front unrounded vowel](close%20front%20unrounded%20vowel.md) \[i\]
41. ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) \[ɪ\]
42. ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)::[close central unrounded vowel](close%20central%20unrounded%20vowel.md) \[ɨ\]
43. ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)::[voiced palatal approximant](voiced%20palatal%20approximant.md) \[j\]
44. ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)::[voiced palatal fricative](voiced%20palatal%20fricative.md) \[ʝ\]
45. ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)::[voiced palatal plosive](voiced%20palatal%20plosive.md) \[ɟ\]
46. ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)::[voiced palatal implosive](voiced%20palatal%20implosive.md) \[ʄ\]
47. ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)::[voiceless velar plosive](voiceless%20velar%20plosive.md) \[k\]
48. ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) \[l\]
49. ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) \[ɫ\]
50. ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) \[ɬ\]
51. ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) \[ɭ\]
52. ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) \[ɮ\]
53. ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) \[ʟ\]
54. ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)::[voiced bilabial nasal](voiced%20bilabial%20nasal.md) \[m\]
55. ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)::[voiced labiodental nasal](voiced%20labiodental%20nasal.md) \[ɱ\]
56. ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)::[voiced alveolar nasal](voiced%20alveolar%20nasal.md) \[n\] <!--SR:!2023-07-11,1,193-->
57. ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)::[voiced velar nasal](voiced%20velar%20nasal.md) \[ŋ\]
58. ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)::[voiced palatal nasal](voiced%20palatal%20nasal.md) \[ɲ\]
59. ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)::[voiced retroflex nasal](voiced%20retroflex%20nasal.md) \[ɳ\]
60. ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)::[voiced uvular nasal](voiced%20uvular%20nasal.md) \[ɴ\]
61. ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) \[o\]
62. ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) \[ɔ\]
63. ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)::[nasalized open-mid back rounded vowel](nasal%20vowel.md) \[ɔ̃\]
64. ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) \[ø\]
65. ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) \[ɵ\] <!--SR:!2023-07-14,4,213-->
66. ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) \[œ\]
67. ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)::[nasalized open-mid front rounded vowel](nasal%20vowel.md) \[œ̃\]
68. ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)::[open front rounded vowel](open%20front%20rounded%20vowel.md) \[ɶ\]
69. ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) \[p\] <!--SR:!2023-07-13,17,273-->
70. ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)::[voiceless uvular plosive](voiceless%20uvular%20plosive.md) \[q\]
71. ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)::[voiced alveolar trill](voiced%20alveolar%20trill.md) \[r\]
72. ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) \[ɾ\]
73. ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)::[voiced uvular trill](voiced%20uvular%20trill.md) \[ʀ\]
74. ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)::[voiced retroflex flap](voiced%20retroflex%20flap.md) \[ɽ\]
75. ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)::[voiced alveolar approximant](voiced%20alveolar%20approximant.md) \[ɹ\]
76. ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)::[voiced retroflex approximant](voiced%20retroflex%20approximant.md) \[ɻ\]
77. ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)::[voiced uvular fricative](voiced%20uvular%20fricative.md) \[ʁ\]
78. ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) \[s\]
79. ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) \[ʃ\]
80. ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) \[ʂ\]
81. ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) \[t\]
82. ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) \[ʈ\]
83. ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) \[ts\]
84. ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) \[tʃ\]
85. ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) \[tɕ\]
86. ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) \[tʂ\]
87. ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)::[close back rounded vowel](close%20back%20rounded%20vowel.md) \[u\]
88. ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) \[ʊ\]
89. ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)::[close central rounded vowel](close%20central%20rounded%20vowel.md) \[ʉ\]
90. ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)::[voiced labiodental fricative](voiced%20labiodental%20fricative.md) \[v\]
91. ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)::[voiced labiodental approximant](voiced%20labiodental%20approximant.md) \[ʋ\]
92. ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) \[w\]
93. ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) \[ʍ\]
94. ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) \[ɯ\]
95. ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)::[voiced velar approximant](voiced%20velar%20approximant.md) \[ɰ\]
96. ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)::[voiceless velar fricative](voiceless%20velar%20fricative.md) \[x\]
97. ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)::[voiceless uvular fricative](voiceless%20uvular%20fricative.md) \[χ\]
98. ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)::[close front rounded vowel](close%20front%20rounded%20vowel.md) \[y\] <!--SR:!2023-07-20,12,253-->
99. ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) \[ʏ\]
100. ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)::[voiced velar fricative](voiced%20velar%20fricative.md) \[ɣ\]
101. ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) \[ɤ\]
102. ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) \[ʎ\]
103. ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) \[ɥ\]
104. ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)::[voiced alveolar fricative](voiced%20alveolar%20fricative.md) \[z\] <!--SR:!2023-07-13,17,264-->
105. ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) \[ʒ\]
106. ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) \[ʑ\]
107. ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)::[voiced retroflex fricative](voiced%20retroflex%20fricative.md) \[ʐ\]
108. ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)::[voiceless dental fricative](voiceless%20dental%20fricative.md) \[θ\]
109. ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) \[ɸ\]
110. ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)::[glottal stop](glottal%20stop.md) \[ʔ\]
111. ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) \[ʕ\]
112. ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)::[tenuis dental click](tenuis%20dental%20click.md) \[ǀ\]
113. ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) \[ǁ\]
114. ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)::[tenuis alveolar click](tenuis%20alveolar%20click.md) \[ǃ\]
115. ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)::[tenuis bilabial click](tenuis%20bilabial%20click.md) \[ʘ\]
116. ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)::[tenuis palatal click](tenuis%20palatal%20click.md) \[ǂ\]

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485d"--><!-- The following content is generated at 2023-06-17T10:26:00.891761+08:00. Any edits will be overridden! -->

> | symbol | description |
> |-|-|
> | {{[nasalized](nasal%20vowel.md) \[◌̃\] (e.g. [ã])}} | {{[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"}} |
> | {{[centralized](central%20vowel.md) \[◌̈\] (e.g. [ä])}} | {{[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"}} |
> | {{[extra-short](extra-shortness.md) \[◌̆\] (e.g. [ă])}} | {{[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]}} |
> | {{[non-syllabic](diphthong.md) \[◌̯\] (e.g. [a̯])}} | {{[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]}} |
> | {{[voiceless](voicelessness.md) \[◌̥\] (e.g. [n̥])}} | {{[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]}} |
> | {{[syllabic](syllabic%20consonant.md) \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])}} | {{[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]}} |
> | {{[dental/alveolar](dental%20consonant.md) \[◌̪\] (e.g. [d̪])}} | {{[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"}} |
> | {{[aspirated](aspirated%20consonant.md) \[◌ʰ\] (e.g. [kʰ])}} | {{[English](English%20language.md) _**c**ome_ \[kʰɐm\]}} |
> | {{[ejective](ejective%20consonant.md) \[◌’\] (e.g. [k’])}} | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | {{[long](longness%20(phonetics).md) \[◌ː\] (e.g. [aː])}} | {{[English](English%20language.md) _shh!_ \[ʃː\]}} |
> | {{[half-long](half-longness%20(phonetics).md) \[◌ˑ\] (e.g. [aˑ])}} | {{[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]}} |
> | {{[primary stress](stress%20(lingustics).md) \[ˈ◌\] (e.g. [ˈa])}} | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | {{[secondary stress](secondary%20stress.md) \[ˌ◌\] (e.g. [ˌa])}} | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | {{[syllable break](syllable.md) \[.\]}} | {{[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]}} | <!--SR:!2023-07-23,28,290!2023-07-14,12,258!2023-07-30,34,298!2023-07-17,9,224!2023-07-20,25,284!2023-08-22,43,264!2023-07-19,24,284!2023-07-16,20,293!2023-07-24,29,293-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
