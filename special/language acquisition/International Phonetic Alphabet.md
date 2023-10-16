---
tags:
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
  ('[open front unrounded vowel](open%20front%20unrounded%20vowel.md)', R'\[a\]', '![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _h**a**t_ \[hat\]',),
  ('[open central unrounded vowel](open%20central%20unrounded%20vowel.md)', R'\[ä\]', '![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _br**a**_ \[bɹäː\]',),
  ('[near-open central vowel](near-open%20central%20vowel.md)', R'\[ɐ\]', '![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _n**u**t_ \[nɐʔt\]',),
  ('[open back unrounded vowel](open%20back%20unrounded%20vowel.md)', R'\[ɑ\]', '![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]',),
  ('[nasalized open back unrounded vowel](nasal%20vowel.md)', R'\[ɑ̃\]', '![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)', R'[French](French%20language.md) _s**an**s_ [sɑ̃] "without"',),
  ('[open back rounded vowel](open%20back%20rounded%20vowel.md)', R'\[ɒ\]', '![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɒt\]',),
  ('[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)', R'\[ʌ\]', '![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)', R'[English](English%20language.md) _g**u**t_ \[ɡʌt\]',),
  ('[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)', R'\[æ\]', '![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _c**a**t_ \[kʰæt\]',),
  ('[voiced bilabial plosive](voiced%20bilabial%20plosive.md)', R'\[b\]', '![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _a**b**ack_ \[əˈbæk\]',),
  ('[voiced bilabial implosive](voiced%20bilabial%20implosive.md)', R'\[ɓ\]', '![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)', R'[English](English%20language.md) _**b**ody_ \[ɓʌdi\]',),
  ('[voiced bilabial fricative](voiced%20bilabial%20fricative.md)', R'\[β\]', '![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"',),
  ('[voiced bilabial trill](voiced%20bilabial%20trill.md)', R'\[ʙ\]', '![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)', R'[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"',),
  ('[voiceless palatal plosive](voiceless%20palatal%20plosive.md)', R'\[c\]', '![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)', R'[French](French%20language.md) _**q**ui_ \[ci\] "who"',),
  ('[voiceless palatal fricative](voiceless%20palatal%20fricative.md)', R'\[ç\]', '![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)', R'[English](English%20language.md) _**h**ue_ \[çʉː\]',),
  ('[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)', R'\[ɕ\]', '![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)', R'[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]',),
  ('[voiced alveolar plosive](voiced%20alveolar%20plosive.md)', R'\[d\]', '![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]',),
  ('[voiced alveolar implosive](voiced%20alveolar%20implosive.md)', R'\[ɗ\]', '![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)', R'[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"',),
  ('[voiced retroflex plosive](voiced%20retroflex%20plosive.md)', R'\[ɖ\]', '![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)', R'[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"',),
  ('[voiced dental fricative](voiced%20dental%20fricative.md)', R'\[ð\]', '![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**is_ \[ðɪs\]',),
  ('[voiced alveolar affricate](voiced%20alveolar%20affricate.md)', R'\[dz\]', '![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]',),
  ('[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)', R'\[dʒ\]', '![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\]',),
  ('[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)', R'\[dʑ\]', '![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"',),
  ('[voiced retroflex affricate](voiced%20retroflex%20affricate.md)', R'\[dʐ\]', '![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)', R'[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"',),
  ('[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)', R'\[e\]', '![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _m**ay**_ \[meː\]',),
  ('[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)', R'\[ɘ\]', '![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɘːd\]',),
  ('[mid central vowel](mid%20central%20vowel.md)', R'\[ə\]', '![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)', R'[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]',),
  ('[r-colored mid central vowel](r-colored%20vowel.md)', R'\[ɚ\]', '![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]',),
  ('[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)', R'\[ɛ\]', '![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**e**d_ \[bɛd\]',),
  ('[nasalized open-mid front unrounded vowel](nasal%20vowel.md)', R'\[ɛ̃\]', '![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)', R'[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"',),
  ('[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)', R'\[ɜ\]', '![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɜːd\]',),
  ('[r-colored open-mid central unrounded vowel](r-colored%20vowel.md)', R'\[ɝ\]', '![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', R'[English](English%20language.md) _b**ir**d_ \[bɝːd\]',),
  ('[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)', R'\[f\]', '![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**f**ill_ \[fɪɫ\]',),
  ('[voiced velar plosive](voiced%20velar%20plosive.md)', R'\[ɡ\]', '![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)', R'[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]',),
  ('[voiced velar implosive](voiced%20velar%20implosive.md)', R'\[ɠ\]', '![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
  ('[voiced uvular plosive](voiced%20uvular%20plosive.md)', R'\[ɢ\]', '![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)', R'[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]',),
  ('[voiceless glottal fricative](voiceless%20glottal%20fricative.md)', R'\[h\]', '![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)', R'[English](English%20language.md) _**h**igh_ \[haɪ̯\]',),
  ('[voiced glottal fricative](voiced%20glottal%20fricative.md)', R'\[ɦ\]', '![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)', R'[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]',),
  ('[aspirated consonant](aspirated%20consonant.md)', R'\[ʰ\]', '', R'[English](English%20langugae.md) _**t**op_ \[tʰɒp\]',),
  ('[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)', R'\[ħ\]', '![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)', R'[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]',),
  ('[close front unrounded vowel](close%20front%20unrounded%20vowel.md)', R'\[i\]', '![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _fr**ee**_ \[fɹiː\]',),
  ('[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)', R'\[ɪ\]', '![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _b**i**t_ \[bɪʔt\]',),
  ('[close central unrounded vowel](close%20central%20unrounded%20vowel.md)', R'\[ɨ\]', '![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)', R'[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"',),
  ('[voiced palatal approximant](voiced%20palatal%20approximant.md)', R'\[j\]', '![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)', R'[English](English%20language.md) _**y**ou_ \[juː\]',),
  ('[palatalization](palatalization%20(phonetics).md)', R'\[ʲ\]', '', R'[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"',),
  ('[voiced palatal fricative](voiced%20palatal%20fricative.md)', R'\[ʝ\]', '![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"',),
  ('[voiced palatal plosive](voiced%20palatal%20plosive.md)', R'\[ɟ\]', '![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)', R'[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"',),
  ('[voiced palatal implosive](voiced%20palatal%20implosive.md)', R'\[ʄ\]', '![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)', R'[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"',),
  ('[voiceless velar plosive](voiceless%20velar%20plosive.md)', R'\[k\]', '![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)', R'[English](English%20language.md) _**k**iss_ \[kʰɪs\]',),
  ('[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)', R'\[l\]', '![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _**l**et_ \[lɛt\]',),
  ('[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)', R'\[ɫ\]', '![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _fee**l**_ \[fiːɫ\]',),
  ('[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)', R'\[ɬ\]', '![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)', R'[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"',),
  ('[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)', R'\[ɭ\]', '![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)', R'[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"',),
  ('[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)', R'\[ɺ\]', '', R'[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"',),
  ('[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)', R'\[ɮ\]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', R'[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"',),
  ('[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)', R'\[ʟ\]', '![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)', R'[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]',),
  ('[voiced bilabial nasal](voiced%20bilabial%20nasal.md)', R'\[m\]', '![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)', R'[English](English%20language.md) _hi**m**_ \[hɪm\]',),
  ('[voiced labiodental nasal](voiced%20labiodental%20nasal.md)', R'\[ɱ\]', '![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)', R'[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]',),
  ('[voiced alveolar nasal](voiced%20alveolar%20nasal.md)', R'\[n\]', '![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)', R'[English](English%20language.md) _**n**ice_ \[naɪs\]',),
  ('[voiced velar nasal](voiced%20velar%20nasal.md)', R'\[ŋ\]', '![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)', R'[English](English%20language.md) _si**ng**_ \[sɪŋ\]',),
  ('[voiced palatal nasal](voiced%20palatal%20nasal.md)', R'\[ɲ\]', '![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)', R'[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"',),
  ('[voiced retroflex nasal](voiced%20retroflex%20nasal.md)', R'\[ɳ\]', '![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)', R'[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"',),
  ('[voiced uvular nasal](voiced%20uvular%20nasal.md)', R'\[ɴ\]', '![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)', R'[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"',),
  ('[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)', R'\[o\]', '![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _y**aw**n_ \[joːn\]',),
  ('[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)', R'\[ɔ\]', '![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _n**o**t_ \[nɔt\]',),
  ('[nasalized open-mid back rounded vowel](nasal%20vowel.md)', R'\[ɔ̃\]', '![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)', R'[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"',),
  ('[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)', R'\[ø\]', '![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _p**eu**_ \[pø\] "few"',),
  ('[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)', R'\[ɵ\]', '![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)', '[English](English%20language.md) _f**oo**t_ \[fɵʔt\]',),
  ('[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)', R'\[œ\]', '![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"',),
  ('[nasalized open-mid front rounded vowel](nasal%20vowel.md)', R'\[œ̃\]', '![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)', R'[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"',),
  ('[open front rounded vowel](open%20front%20rounded%20vowel.md)', R'\[ɶ\]', '![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)', R'[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"',),
  ('[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)', R'\[p\]', '![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)', R'[English](English%20language.md) _**p**ack_ \[pʰæk\]',),
  ('[voiceless uvular plosive](voiceless%20uvular%20plosive.md)', R'\[q\]', '![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)', R'[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"',),
  ('[voiced alveolar trill](voiced%20alveolar%20trill.md)', R'\[r\]', '![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)', R'[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"',),
  ('[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)', R'\[ɾ\]', '![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)', R'[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"',),
  ('[voiced uvular trill](voiced%20uvular%20trill.md)', R'\[ʀ\]', '![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)', R'[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"',),
  ('[voiced retroflex flap](voiced%20retroflex%20flap.md)', R'\[ɽ\]', '![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)', R'[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"',),
  ('[voiced alveolar approximant](voiced%20alveolar%20approximant.md)', R'\[ɹ\]', '![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)', R'[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"',),
  ('[voiced retroflex approximant](voiced%20retroflex%20approximant.md)', R'\[ɻ\]', '![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)', R'[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"',),
  ('[voiced uvular fricative](voiced%20uvular%20fricative.md)', R'\[ʁ\]', '![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)', R'[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"',),
  ('[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)', R'\[s\]', '![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**s**it_ \[sɪt\]',),
  ('[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)', R'\[ʃ\]', '![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]',),
  ('[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)', R'\[ʂ\]', '![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)', R'[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"',),
  ('[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)', R'\[t\]', '![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**t**ick_ \[tʰɪk\]',),
  ('[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)', R'\[ʈ\]', '![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)', R'[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"',),
  ('[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)', R'\[ts\]', '![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)', R'[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]',),
  ('[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)', R'\[tʃ\]', '![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)', R'[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]',),
  ('[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)', R'\[tɕ\]', '![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"',),
  ('[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)', R'\[tʂ\]', '![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)', R'[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"',),
  ('[close back rounded vowel](close%20back%20rounded%20vowel.md)', R'\[u\]', '![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]',),
  ('[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)', R'\[ʊ\]', '![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)', R'[English](English%20language.md) _h**oo**k_ \[hʊʔk\]',),
  ('[close central rounded vowel](close%20central%20rounded%20vowel.md)', R'\[ʉ\]', '![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)', R'[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]',),
  ('[voiced labiodental fricative](voiced%20labiodental%20fricative.md)', R'\[v\]', '![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)', R'[English](English%20language.md) _**v**al**v**e_ \[væɫv\]',),
  ('[voiced labiodental approximant](voiced%20labiodental%20approximant.md)', R'\[ʋ\]', '![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)', R'[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"',),
  ('[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)', R'\[w\]', '![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)', R'[English](English%20language.md) _**w**eep_ \[wiːp\]',),
  ('[labialization](labialization.md)', R'\[ʷ\]', '', R'[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]',),
  ('[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)', R'\[ʍ\]', '![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)', R'[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]',),
  ('[close back unrounded vowel](close%20back%20unrounded%20vowel.md)', R'\[ɯ\]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', R'[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"',),
  ('[voiced velar approximant](voiced%20velar%20approximant.md)', R'\[ɰ\]', '![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)', R'[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"',),
  ('[voiceless velar fricative](voiceless%20velar%20fricative.md)', R'\[x\]', '![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)', R'[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"',),
  ('[voiceless uvular fricative](voiceless%20uvular%20fricative.md)', R'\[χ\]', '![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)', R'[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"',),
  ('[close front rounded vowel](close%20front%20rounded%20vowel.md)', R'\[y\]', '![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)', R'[French](French%20language.md) _t**u**_ \[t̪y] "you"',),
  ('[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)', R'\[ʏ\]', '![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)', R'[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"',),
  ('[voiced velar fricative](voiced%20velar%20fricative.md)', R'\[ɣ\]', '![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)', R'[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"',),
  ('[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)', R'\[ɤ\]', '![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)', R'[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"',),
  ('[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)', R'\[ʎ\]', '![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)', R'[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]',),
  ('[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)', R'\[ɥ\]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', R'[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"',),
  ('[voiced alveolar fricative](voiced%20alveolar%20fricative.md)', R'\[z\]', '![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)', '[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]',),
  ('[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)', R'\[ʒ\]', '![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]',),
  ('[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)', R'\[ʑ\]', '![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)', R'[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"',),
  ('[voiced retroflex fricative](voiced%20retroflex%20fricative.md)', R'\[ʐ\]', '![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)', R'[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"',),
  ('[voiceless dental fricative](voiceless%20dental%20fricative.md)', R'\[θ\]', '![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**in_ \[θɪn\]',),
  ('[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)', R'\[ɸ\]', '![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)', R'[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"',),
  ('[glottal stop](glottal%20stop.md)', R'\[ʔ\]', '![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)', R'[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]',),
  ('[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)', R'\[ʕ\]', '![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)', R'[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"',),
  ('[tenuis dental click](tenuis%20dental%20click.md)', R'\[ǀ\]', '![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)', R'[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]',),
  ('[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)', R'\[ǁ\]', '![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)', R'[English](English%20language.md) _**tchick**_ \[ˈǁ\]',),
  ('[tenuis alveolar click](tenuis%20alveolar%20click.md)', R'\[ǃ\]', '![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)', R'[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"',),
  ('[tenuis bilabial click](tenuis%20bilabial%20click.md)', R'\[ʘ\]', '![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)', R'[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"',),
  ('[tenuis palatal click](tenuis%20palatal%20click.md)', R'\[ǂ\]', '![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)', R'[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"',),
)
diacritics = (
  ('[nasalized](nasal%20vowel.md)', R'\[◌̃\] (e.g. [ã])', R'[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"',),
  ('[centralized](central%20vowel.md)', R'\[◌̈\] (e.g. [ä])', R'[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"',),
  ('[extra-short](extra-shortness.md)', R'\[◌̆\] (e.g. [ă])', R'[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]',),
  ('[non-syllabic](diphthong.md)', R'\[◌̯\] (e.g. [a̯])', R'[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]',),
  ('[voiceless](voicelessness.md)', R'\[◌̥\] (e.g. [n̥])', R'[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]',),
  ('[syllabic](syllabic%20consonant.md)', R'\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])', R'[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]',),
  ('[dental/alveolar](dental%20consonant.md)', R'\[◌̪\] (e.g. [d̪])', R'[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"',),
  ('[aspirated](aspirated%20consonant.md)', R'\[◌ʰ\] (e.g. [kʰ])', R'[English](English%20language.md) _**c**ome_ \[kʰɐm\]',),
  ('[ejective](ejective%20consonant.md)', R'\[◌’\] (e.g. [k’])', R'[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"',),
  ('[long](longness%20(phonetics).md)', R'\[◌ː\] (e.g. [aː])', R'[English](English%20language.md) _shh!_ \[ʃː\]',),
  ('[half-long](half-longness%20(phonetics).md)', R'\[◌ˑ\] (e.g. [aˑ])', R'[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]',),
  ('[primary stress](stress%20(lingustics).md)', R'\[ˈ◌\] (e.g. [ˈa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
  ('[secondary stress](secondary%20stress.md)', R'\[ˌ◌\] (e.g. [ˌa])', R'[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]',),
  ('[syllable break](syllable.md)', R'\[.\]', R'[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]',),
)
return chain.from_iterable(await gather(
  memorize_table(
    (*e.cwf_sects("958a"), NULL_LOCATION,),
    ("name", "symbol", f"audio", "description",),
    letters,
    lambda datum: chain(datum[:-1], map(cloze, datum[-1:])),
  ),
  memorize_map(
    (NULL_LOCATION, *e.cwf_sects("059f", "d92e"),),
    items_to_map(*map(lambda datum: datum[:2], letters)),
  ),
  memorize_map(
    (NULL_LOCATION, *e.cwf_sects("5dfb", "f9aa"),),
    items_to_map(*((datum[0], datum[2]) for datum in letters if datum[2])),
  ),
  memorize_table(
    (*e.cwf_sects("485d"), NULL_LOCATION,),
    ("name", "symbol", "description",),
    diacritics,
    lambda datum: chain(datum[:-1], map(cloze, datum[-1:])),
  ),
  memorize_map(
    (NULL_LOCATION, *e.cwf_sects("ffa2", "94fb"),),
    items_to_map(*map(lambda datum: datum[:2], diacritics)),
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
> 18. {{sub-laminal/sub-apical ([tongue](tongue.md) underside)}} <!--SR:!2023-11-06,108,310!2023-12-19,142,318!2023-12-25,147,324!2023-11-05,101,304!2023-11-15,85,304!2023-10-18,68,304!2023-11-01,103,304!2024-04-05,193,293!2023-11-08,104,313!2023-12-02,87,253!2024-07-18,293,313!2024-01-04,156,333!2024-03-14,167,318!2023-12-02,78,317!2023-12-14,89,341-->

- [consonant](consonant.md):::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2024-05-24,244,290!2023-11-07,109,310-->
  - [airstream mechanism](airstream%20mechanism.md):::how the moving [air](air.md) is thrusted <!--SR:!2024-09-12,338,318!2023-11-28,126,323-->
    - (all) [pulmonic](pulmonic%20consonant.md) egressive:::[air](air.md) is exhaled from the [lungs](lung.md) <!--SR:!2023-10-27,94,313!2024-01-30,136,338-->
    - (16%) [glottalic](glottalic%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md) <!--SR:!2023-10-25,26,331-->
    - (13%) [glottalic](glottalic%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md) <!--SR:!2023-10-23,24,331-->
    - (<2%) lingual/[velaric](velar%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md) <!--SR:!2023-11-24,45,311-->
    - ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive:::[air](air.md) is inhaled into the [lungs](lung.md) <!--SR:!2023-11-02,99,313!2023-11-04,100,313-->
    - ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md) <!--SR:!2023-12-21,81,279!2023-12-10,86,341-->
  - [length](gemination.md):::how long the articulation of a [consonant](consonant.md) lasts <!--SR:!2023-10-21,49,278-->
    - values in ascending [length](gemination.md)::single/singleton, geminate, long geminate <!--SR:!2024-01-12,130,293-->
  - [manner of articulation](manner%20of%20articulation.md):::configuration and interaction of the [speech organs](speech%20organ.md) <!--SR:!2023-11-22,47,311-->
    - [affricate](affricate%20consonant.md):::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md) <!--SR:!2023-10-16,40,297-->
    - [approximant](approximant%20consonant.md):::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md) <!--SR:!2024-02-17,176,293!2023-12-18,102,338-->
      - [lateral approximant](lateral%20consonant.md):::approximant with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2024-03-28,185,284!2023-10-29,95,304-->
      - [semivowel/glide/semiconsonant](semivowel.md):::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary <!--SR:!2023-10-22,12,292-->
    - [flap/tap](tap%20and%20flap%20consonants.md):::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact <!--SR:!2023-11-04,59,278-->
    - [fricative/spirant](fricative%20consonant.md):::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation <!--SR:!2023-11-12,79,244!2024-03-12,171,338-->
- [lateral](lateral%20consonant.md):::fricative with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2023-10-30,18,332!2000-01-01,1,250-->
      - [sibilant](sibilant%20consonant.md):::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md) <!--SR:!2023-10-25,46,301!2023-10-28,29,331-->
    - [nasal](nasal%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow <!--SR:!2023-10-17,40,297!2023-10-11,4,312-->
    - [plosive/stop](plosive%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow <!--SR:!2023-11-13,65,321!2023-10-24,25,331-->
    - [trill](trill%20consonant.md):::consonant produced by vibrations between the active articulator and the passive articulator <!--SR:!2023-12-13,89,298!2024-01-16,116,341-->
  - [place of articulation](place%20of%20articulation.md):::location along the [vocal tract](vocal%20tract.md) producing the consonant <!--SR:!2024-04-06,213,304!2024-01-14,114,338-->
    - [alveolar](alveolar%20ridge.md):::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive) <!--SR:!2023-11-16,62,319-->
    - [aryepiglottal](pharyngeal%20consonant.md):::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active) <!--SR:!2024-03-21,209,333!2023-11-02,27,331-->
    - [coronal](coronal%20constant.md):::front of the [tongue](tongue.md) (active) <!--SR:!2024-05-24,231,293!2023-11-16,73,278-->
      - [apical](apical%20consonant.md):::tip of the [tongue](tongue.md) (active) <!--SR:!2023-10-31,96,304!2024-01-18,118,338-->
      - [laminal](laminal%20consonant.md):::blade of the [tongue](tongue.md), the upper front surface behind the tip (active) <!--SR:!2023-10-20,61,233!2023-10-19,26,240-->
      - [subapical](subapical%20consonant.md):::surface under the tip of the [tongue](tongue.md) (active) <!--SR:!2023-10-28,94,304!2023-12-24,147,333-->
- [dental](dental%20consonant.md):::upper [teeth](tooth.md) (passive) <!--SR:!2024-08-15,308,313!2000-01-01,1,250-->
    - [dorsal](dorsal%20consonant.md):::body of the [tongue](tongue.md) (active) <!--SR:!2024-04-05,222,333!2023-11-23,115,313-->
- [epiglottal](pharyngeal%20consonant.md):::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive) <!--SR:!2024-01-19,119,341!2023-10-31,19,332-->
    - [glottal](glottal%20consonant.md):::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active) <!--SR:!2024-03-13,188,293!2024-01-01,154,333-->
    - [labial](labial%20consonant.md):::lower [lip](lip.md) (active), upper [lip](lip.md) (passive) <!--SR:!2023-11-30,115,284!2023-12-13,139,333-->
    - [palatal](palatal%20consonant.md):::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2023-10-20,87,284-->
- [pharyngeal](pharyngeal%20consonant.md):::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive) <!--SR:!2024-01-03,89,278!2023-10-14,2,291-->
    - [post-alveolar](post-alveolar%20consonant.md):::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive) <!--SR:!2024-01-24,123,337!2023-10-27,28,331-->
- [uvular](uvular%20consonant.md):::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive) <!--SR:!2024-03-29,186,284!2023-10-28,16,332-->
    - [velar](velar%20consonant.md):::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2023-11-05,60,278!2024-01-14,114,337-->
  - [phonation](phonation.md):::how the [vocal cords](vocal%20folds.md) vibrate <!--SR:!2023-11-10,56,301!2024-01-13,113,341-->
    - [voiced](voice%20(phonetics).md):::the [vocal cords](vocal%20cords.md) vibrate fully <!--SR:!2023-12-04,132,324!2024-01-22,121,338-->
    - [voiceless](voicelessness.md):::the [vocal cords](vocal%20cords.md) do not vibrate <!--SR:!2023-12-05,133,333!2024-01-09,160,333-->
  - [voice onset time](voice%20onset%20time.md) (VOT):::timing of [phonation](phonation.md) <!--SR:!2023-11-11,113,333-->
- values in ascending [VOT](voice%20onset%20time.md)::[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive) <!--SR:!2024-06-04,232,284-->
- [vowel](vowel.md):::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2023-10-11,4,312-->
  - [vowel backness](vowel.md#backness):::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md) <!--SR:!2023-10-16,83,284!2024-01-21,120,337-->
    - values in ascending [vowel backness](vowel.md#backness)::[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md) <!--SR:!2023-10-25,92,304-->
  - [vowel height](vowel.md#height):::vertical position of the [tongue](tongue.md) <!--SR:!2024-03-08,168,338!2023-10-11,4,311-->
    - values in descending [vowel height](vowel.md#height)::[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md)
  - [vowel roundedness](roundedness.md):::rounding of the [lips](lip.md) <!--SR:!2023-10-25,91,293!2024-01-15,115,338-->
    - values in ascending [vowel roundedness](roundedness.md)::unrounded, compressed, protruded <!--SR:!2023-10-26,27,331-->

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]:::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md) <!--SR:!2024-03-07,167,264!2023-11-21,66,317-->
- (principal) /[slashes](slash%20(punctuation).md)/:::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only <!--SR:!2024-04-20,204,293-->
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses)):::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md) <!--SR:!2023-11-10,48,253!2023-10-26,27,331-->
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses))):::transcription of obscured speech or description of obscuring sound <!--SR:!2023-10-17,84,284!2024-06-08,260,304-->
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]:::extra-precise transcription <!--SR:!2023-12-16,91,338!2023-12-09,85,341-->
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[morphophonemic](morphophonology.md) transcription <!--SR:!2023-10-21,22,281!2023-11-21,36,291-->
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫:::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves <!--SR:!2023-11-02,27,331!2023-10-11,4,311-->

### letters

Here is a list of common IPA letters and their pronunciations:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="958a"--><!-- The following content is generated at 2023-08-09T19:34:04.197334+08:00. Any edits will be overridden! -->

> | name | symbol | audio | description |
> |-|-|-|-|
> | [open front unrounded vowel](open%20front%20unrounded%20vowel.md) | \[a\] | ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _h**a**t_ \[hat\]}} |
> | [open central unrounded vowel](open%20central%20unrounded%20vowel.md) | \[ä\] | ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _br**a**_ \[bɹäː\]}} |
> | [near-open central vowel](near-open%20central%20vowel.md) | \[ɐ\] | ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _n**u**t_ \[nɐʔt\]}} |
> | [open back unrounded vowel](open%20back%20unrounded%20vowel.md) | \[ɑ\] | ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]}} |
> | [nasalized open back unrounded vowel](nasal%20vowel.md) | \[ɑ̃\] | ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) | {{[French](French%20language.md) _s**an**s_ [sɑ̃] "without"}} |
> | [open back rounded vowel](open%20back%20rounded%20vowel.md) | \[ɒ\] | ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _n**o**t_ \[nɒt\]}} |
> | [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) | \[ʌ\] | ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) | {{[English](English%20language.md) _g**u**t_ \[ɡʌt\]}} |
> | [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) | \[æ\] | ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _c**a**t_ \[kʰæt\]}} |
> | [voiced bilabial plosive](voiced%20bilabial%20plosive.md) | \[b\] | ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) | {{[English](English%20language.md) _a**b**ack_ \[əˈbæk\]}} |
> | [voiced bilabial implosive](voiced%20bilabial%20implosive.md) | \[ɓ\] | ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) | {{[English](English%20language.md) _**b**ody_ \[ɓʌdi\]}} |
> | [voiced bilabial fricative](voiced%20bilabial%20fricative.md) | \[β\] | ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"}} |
> | [voiced bilabial trill](voiced%20bilabial%20trill.md) | \[ʙ\] | ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) | {{[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"}} |
> | [voiceless palatal plosive](voiceless%20palatal%20plosive.md) | \[c\] | ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) | {{[French](French%20language.md) _**q**ui_ \[ci\] "who"}} |
> | [voiceless palatal fricative](voiceless%20palatal%20fricative.md) | \[ç\] | ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) | {{[English](English%20language.md) _**h**ue_ \[çʉː\]}} |
> | [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) | \[ɕ\] | ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) | {{[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]}} |
> | [voiced alveolar plosive](voiced%20alveolar%20plosive.md) | \[d\] | ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) | {{[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]}} |
> | [voiced alveolar implosive](voiced%20alveolar%20implosive.md) | \[ɗ\] | ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) | {{[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"}} |
> | [voiced retroflex plosive](voiced%20retroflex%20plosive.md) | \[ɖ\] | ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga) | {{[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"}} |
> | [voiced dental fricative](voiced%20dental%20fricative.md) | \[ð\] | ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) | {{[English](English%20language.md) _**th**is_ \[ðɪs\]}} |
> | [voiced alveolar affricate](voiced%20alveolar%20affricate.md) | \[dz\] | ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga) | {{[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]}} |
> | [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) | \[dʒ\] | ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) | {{[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\]}} |
> | [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) | \[dʑ\] | ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) | {{[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"}} |
> | [voiced retroflex affricate](voiced%20retroflex%20affricate.md) | \[dʐ\] | ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) | {{[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"}} |
> | [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) | \[e\] | ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _m**ay**_ \[meː\]}} |
> | [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) | \[ɘ\] | ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɘːd\]}} |
> | [mid central vowel](mid%20central%20vowel.md) | \[ə\] | ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) | {{[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]}} |
> | [r-colored mid central vowel](r-colored%20vowel.md) | \[ɚ\] | ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | {{[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]}} |
> | [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) | \[ɛ\] | ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**e**d_ \[bɛd\]}} |
> | [nasalized open-mid front unrounded vowel](nasal%20vowel.md) | \[ɛ̃\] | ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) | {{[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"}} |
> | [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) | \[ɜ\] | ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɜːd\]}} |
> | [r-colored open-mid central unrounded vowel](r-colored%20vowel.md) | \[ɝ\] | ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | {{[English](English%20language.md) _b**ir**d_ \[bɝːd\]}} |
> | [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) | \[f\] | ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) | {{[English](English%20language.md) _**f**ill_ \[fɪɫ\]}} |
> | [voiced velar plosive](voiced%20velar%20plosive.md) | \[ɡ\] | ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) | {{[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]}} |
> | [voiced velar implosive](voiced%20velar%20implosive.md) | \[ɠ\] | ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | [voiced uvular plosive](voiced%20uvular%20plosive.md) | \[ɢ\] | ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga) | {{[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]}} |
> | [voiceless glottal fricative](voiceless%20glottal%20fricative.md) | \[h\] | ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) | {{[English](English%20language.md) _**h**igh_ \[haɪ̯\]}} |
> | [voiced glottal fricative](voiced%20glottal%20fricative.md) | \[ɦ\] | ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) | {{[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]}} |
> | [aspirated consonant](aspirated%20consonant.md) | \[ʰ\] |  | {{[English](English%20langugae.md) _**t**op_ \[tʰɒp\]}} |
> | [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) | \[ħ\] | ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) | {{[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]}} |
> | [close front unrounded vowel](close%20front%20unrounded%20vowel.md) | \[i\] | ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _fr**ee**_ \[fɹiː\]}} |
> | [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) | \[ɪ\] | ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) | {{[English](English%20language.md) _b**i**t_ \[bɪʔt\]}} |
> | [close central unrounded vowel](close%20central%20unrounded%20vowel.md) | \[ɨ\] | ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) | {{[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"}} |
> | [voiced palatal approximant](voiced%20palatal%20approximant.md) | \[j\] | ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) | {{[English](English%20language.md) _**y**ou_ \[juː\]}} |
> | [palatalization](palatalization%20(phonetics).md) | \[ʲ\] |  | {{[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"}} |
> | [voiced palatal fricative](voiced%20palatal%20fricative.md) | \[ʝ\] | ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"}} |
> | [voiced palatal plosive](voiced%20palatal%20plosive.md) | \[ɟ\] | ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) | {{[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"}} |
> | [voiced palatal implosive](voiced%20palatal%20implosive.md) | \[ʄ\] | ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) | {{[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"}} |
> | [voiceless velar plosive](voiceless%20velar%20plosive.md) | \[k\] | ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) | {{[English](English%20language.md) _**k**iss_ \[kʰɪs\]}} |
> | [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) | \[l\] | ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _**l**et_ \[lɛt\]}} |
> | [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) | \[ɫ\] | ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _fee**l**_ \[fiːɫ\]}} |
> | [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) | \[ɬ\] | ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) | {{[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"}} |
> | [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) | \[ɭ\] | ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) | {{[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"}} |
> | [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) | \[ɺ\] |  | {{[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"}} |
> | [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) | \[ɮ\] | ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) | {{[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"}} |
> | [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) | \[ʟ\] | ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) | {{[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]}} |
> | [voiced bilabial nasal](voiced%20bilabial%20nasal.md) | \[m\] | ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) | {{[English](English%20language.md) _hi**m**_ \[hɪm\]}} |
> | [voiced labiodental nasal](voiced%20labiodental%20nasal.md) | \[ɱ\] | ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) | {{[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]}} |
> | [voiced alveolar nasal](voiced%20alveolar%20nasal.md) | \[n\] | ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) | {{[English](English%20language.md) _**n**ice_ \[naɪs\]}} |
> | [voiced velar nasal](voiced%20velar%20nasal.md) | \[ŋ\] | ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) | {{[English](English%20language.md) _si**ng**_ \[sɪŋ\]}} |
> | [voiced palatal nasal](voiced%20palatal%20nasal.md) | \[ɲ\] | ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) | {{[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"}} |
> | [voiced retroflex nasal](voiced%20retroflex%20nasal.md) | \[ɳ\] | ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) | {{[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"}} |
> | [voiced uvular nasal](voiced%20uvular%20nasal.md) | \[ɴ\] | ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) | {{[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"}} |
> | [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) | \[o\] | ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _y**aw**n_ \[joːn\]}} |
> | [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) | \[ɔ\] | ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _n**o**t_ \[nɔt\]}} |
> | [nasalized open-mid back rounded vowel](nasal%20vowel.md) | \[ɔ̃\] | ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) | {{[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"}} |
> | [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) | \[ø\] | ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _p**eu**_ \[pø\] "few"}} |
> | [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) | \[ɵ\] | ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) | {{[English](English%20language.md) _f**oo**t_ \[fɵʔt\]}} |
> | [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) | \[œ\] | ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"}} |
> | [nasalized open-mid front rounded vowel](nasal%20vowel.md) | \[œ̃\] | ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) | {{[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"}} |
> | [open front rounded vowel](open%20front%20rounded%20vowel.md) | \[ɶ\] | ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) | {{[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"}} |
> | [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) | \[p\] | ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) | {{[English](English%20language.md) _**p**ack_ \[pʰæk\]}} |
> | [voiceless uvular plosive](voiceless%20uvular%20plosive.md) | \[q\] | ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) | {{[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"}} |
> | [voiced alveolar trill](voiced%20alveolar%20trill.md) | \[r\] | ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) | {{[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"}} |
> | [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) | \[ɾ\] | ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) | {{[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"}} |
> | [voiced uvular trill](voiced%20uvular%20trill.md) | \[ʀ\] | ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) | {{[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"}} |
> | [voiced retroflex flap](voiced%20retroflex%20flap.md) | \[ɽ\] | ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) | {{[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"}} |
> | [voiced alveolar approximant](voiced%20alveolar%20approximant.md) | \[ɹ\] | ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) | {{[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"}} |
> | [voiced retroflex approximant](voiced%20retroflex%20approximant.md) | \[ɻ\] | ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga) | {{[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"}} |
> | [voiced uvular fricative](voiced%20uvular%20fricative.md) | \[ʁ\] | ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) | {{[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"}} |
> | [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) | \[s\] | ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**s**it_ \[sɪt\]}} |
> | [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) | \[ʃ\] | ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]}} |
> | [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) | \[ʂ\] | ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) | {{[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"}} |
> | [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) | \[t\] | ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) | {{[English](English%20language.md) _**t**ick_ \[tʰɪk\]}} |
> | [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) | \[ʈ\] | ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga) | {{[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"}} |
> | [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) | \[ts\] | ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga) | {{[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]}} |
> | [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) | \[tʃ\] | ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) | {{[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]}} |
> | [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) | \[tɕ\] | ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) | {{[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"}} |
> | [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) | \[tʂ\] | ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) | {{[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"}} |
> | [close back rounded vowel](close%20back%20rounded%20vowel.md) | \[u\] | ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]}} |
> | [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) | \[ʊ\] | ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) | {{[English](English%20language.md) _h**oo**k_ \[hʊʔk\]}} |
> | [close central rounded vowel](close%20central%20rounded%20vowel.md) | \[ʉ\] | ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) | {{[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]}} |
> | [voiced labiodental fricative](voiced%20labiodental%20fricative.md) | \[v\] | ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) | {{[English](English%20language.md) _**v**al**v**e_ \[væɫv\]}} |
> | [voiced labiodental approximant](voiced%20labiodental%20approximant.md) | \[ʋ\] | ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) | {{[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"}} |
> | [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) | \[w\] | ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) | {{[English](English%20language.md) _**w**eep_ \[wiːp\]}} |
> | [labialization](labialization.md) | \[ʷ\] |  | {{[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]}} |
> | [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) | \[ʍ\] | ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) | {{[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]}} |
> | [close back unrounded vowel](close%20back%20unrounded%20vowel.md) | \[ɯ\] | ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) | {{[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"}} |
> | [voiced velar approximant](voiced%20velar%20approximant.md) | \[ɰ\] | ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) | {{[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"}} |
> | [voiceless velar fricative](voiceless%20velar%20fricative.md) | \[x\] | ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) | {{[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"}} |
> | [voiceless uvular fricative](voiceless%20uvular%20fricative.md) | \[χ\] | ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) | {{[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"}} |
> | [close front rounded vowel](close%20front%20rounded%20vowel.md) | \[y\] | ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) | {{[French](French%20language.md) _t**u**_ \[t̪y] "you"}} |
> | [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) | \[ʏ\] | ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) | {{[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"}} |
> | [voiced velar fricative](voiced%20velar%20fricative.md) | \[ɣ\] | ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) | {{[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"}} |
> | [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) | \[ɤ\] | ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) | {{[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"}} |
> | [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) | \[ʎ\] | ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) | {{[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]}} |
> | [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) | \[ɥ\] | ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) | {{[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"}} |
> | [voiced alveolar fricative](voiced%20alveolar%20fricative.md) | \[z\] | ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) | {{[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]}} |
> | [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) | \[ʒ\] | ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg) | {{[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]}} |
> | [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) | \[ʑ\] | ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg) | {{[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"}} |
> | [voiced retroflex fricative](voiced%20retroflex%20fricative.md) | \[ʐ\] | ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg) | {{[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"}} |
> | [voiceless dental fricative](voiceless%20dental%20fricative.md) | \[θ\] | ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) | {{[English](English%20language.md) _**th**in_ \[θɪn\]}} |
> | [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) | \[ɸ\] | ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) | {{[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"}} |
> | [glottal stop](glottal%20stop.md) | \[ʔ\] | ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg) | {{[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]}} |
> | [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) | \[ʕ\] | ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg) | {{[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"}} |
> | [tenuis dental click](tenuis%20dental%20click.md) | \[ǀ\] | ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) | {{[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]}} |
> | [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) | \[ǁ\] | ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) | {{[English](English%20language.md) _**tchick**_ \[ˈǁ\]}} |
> | [tenuis alveolar click](tenuis%20alveolar%20click.md) | \[ǃ\] | ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) | {{[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"}} |
> | [tenuis bilabial click](tenuis%20bilabial%20click.md) | \[ʘ\] | ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg) | {{[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"}} |
> | [tenuis palatal click](tenuis%20palatal%20click.md) | \[ǂ\] | ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) | {{[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"}} | <!--SR:!2024-08-11,310,310!2023-12-06,106,250!2023-11-07,32,164!2023-10-17,45,204!2023-11-10,103,304!2023-12-30,75,224!2024-07-06,264,304!2024-02-10,132,224!2024-03-23,182,284!2024-02-01,162,284!2023-11-12,58,244!2023-12-16,116,264!2024-06-09,261,304!2023-12-10,65,173!2023-10-16,23,193!2024-04-07,191,273!2023-10-23,64,213!2023-11-05,30,213!2023-10-22,16,233!2023-11-12,48,218!2023-11-24,70,278!2023-11-27,65,258!2023-10-19,47,278!2023-10-28,18,198!2023-10-18,33,238!2023-11-13,45,238!2024-03-17,159,298!2023-12-17,92,298!2024-03-22,162,298!2023-10-17,49,278!2023-10-16,31,297!2023-10-18,41,297!2023-11-05,44,257!2023-11-04,50,277!2023-12-29,84,277!2023-10-22,43,297!2023-12-26,81,277!2024-01-11,111,337!2024-01-22,98,277!2023-11-15,53,237!2023-10-17,32,277!2023-11-04,43,258!2023-10-14,29,298!2023-11-25,61,238!2023-10-11,5,138!2023-10-11,11,158!2023-11-09,48,238!2023-10-26,33,299!2023-10-29,34,300!2023-11-09,30,260!2023-11-06,38,200!2023-11-10,35,220!2023-12-19,80,280!2023-10-20,13,181!2023-10-12,27,241!2023-10-20,25,281!2024-01-10,102,301!2023-10-21,15,281!2023-12-08,77,321!2023-11-11,49,261!2023-11-01,26,221!2023-12-27,76,241!2023-10-18,12,228!2023-10-24,8,291!2023-10-23,13,271!2023-10-19,13,251!2023-10-18,6,271!2023-10-19,13,251!2023-10-17,7,191!2023-10-11,1,191!2023-11-13,34,271!2023-11-10,31,271!2023-10-26,20,251!2023-11-25,46,291!2023-10-24,18,271!2023-10-11,1,191!2023-10-27,11,191!2023-11-23,48,311!2023-10-13,3,151!2023-10-27,28,331!2023-12-07,52,311!2023-10-19,13,271!2023-10-16,4,271!2023-10-18,2,231!2023-10-17,1,231!2023-10-31,15,291!2023-10-16,4,271!2023-10-18,2,231!2023-10-18,6,271!2023-10-13,1,252!2023-10-16,4,272!2023-10-24,14,312!2023-10-19,9,292!2023-10-21,11,292!2023-10-20,10,292!2023-10-19,7,292!2023-10-17,3,252!2023-10-15,3,252!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2023-10-17,1,230!2000-01-01,1,250!2053-07-14,10864,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="059f"--><!-- The following content is generated at 2023-08-09T19:34:04.118545+08:00. Any edits will be overridden! -->

1. [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::\[a\] <!--SR:!2024-01-13,113,338-->
2. [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::\[ä\] <!--SR:!2024-01-16,116,337-->
3. [near-open central vowel](near-open%20central%20vowel.md)::\[ɐ\]
4. [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::\[ɑ\] <!--SR:!2023-10-22,23,331-->
5. [nasalized open back unrounded vowel](nasal%20vowel.md)::\[ɑ̃\] <!--SR:!2023-12-11,87,341-->
6. [open back rounded vowel](open%20back%20rounded%20vowel.md)::\[ɒ\] <!--SR:!2024-01-16,116,341-->
7. [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::\[ʌ\]
8. [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::\[æ\]
9. [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::\[b\] <!--SR:!2023-12-15,90,338-->
10. [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::\[ɓ\] <!--SR:!2023-12-13,88,340-->
11. [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::\[β\] <!--SR:!2024-01-25,124,341-->
12. [voiced bilabial trill](voiced%20bilabial%20trill.md)::\[ʙ\] <!--SR:!2024-01-27,126,341-->
13. [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::\[c\]
14. [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::\[ç\] <!--SR:!2023-12-11,80,321-->
15. [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::\[ɕ\]
16. [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::\[d\] <!--SR:!2024-01-17,116,338-->
17. [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::\[ɗ\] <!--SR:!2024-01-20,119,340-->
18. [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::\[ɖ\] <!--SR:!2023-10-18,8,292-->
19. [voiced dental fricative](voiced%20dental%20fricative.md)::\[ð\] <!--SR:!2023-10-24,14,311-->
20. [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::\[dz\] <!--SR:!2023-10-24,25,331-->
21. [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::\[dʒ\]
22. [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::\[dʑ\] <!--SR:!2023-11-01,26,311-->
23. [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::\[dʐ\]
24. [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::\[e\] <!--SR:!2023-12-12,88,341-->
25. [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::\[ɘ\]
26. [mid central vowel](mid%20central%20vowel.md)::\[ə\] <!--SR:!2023-10-13,34,297-->
27. [r-colored mid central vowel](r-colored%20vowel.md)::\[ɚ\] <!--SR:!2023-11-01,16,332-->
28. [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::\[ɛ\] <!--SR:!2023-10-13,14,311-->
29. [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::\[ɛ̃\]
30. [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::\[ɜ\]
31. [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::\[ɝ\] <!--SR:!2024-02-26,143,317-->
32. [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::\[f\] <!--SR:!2023-12-02,71,317-->
33. [voiced velar plosive](voiced%20velar%20plosive.md)::\[ɡ\] <!--SR:!2023-11-04,29,331-->
34. [voiced velar implosive](voiced%20velar%20implosive.md)::\[ɠ\] <!--SR:!2023-10-30,18,332-->
35. [voiced uvular plosive](voiced%20uvular%20plosive.md)::\[ɢ\]
36. [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::\[h\] <!--SR:!2023-10-31,19,332-->
37. [voiced glottal fricative](voiced%20glottal%20fricative.md)::\[ɦ\] <!--SR:!2023-12-10,79,321-->
38. [aspirated consonant](aspirated%20consonant.md)::\[ʰ\] <!--SR:!2023-10-24,25,331-->
39. [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::\[ħ\]
40. [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::\[i\] <!--SR:!2023-11-04,19,331-->
41. [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::\[ɪ\] <!--SR:!2023-10-11,4,312-->
42. [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::\[ɨ\]
43. [voiced palatal approximant](voiced%20palatal%20approximant.md)::\[j\]
44. [palatalization](palatalization%20(phonetics).md)::\[ʲ\] <!--SR:!2023-12-06,82,338-->
45. [voiced palatal fricative](voiced%20palatal%20fricative.md)::\[ʝ\]
46. [voiced palatal plosive](voiced%20palatal%20plosive.md)::\[ɟ\] <!--SR:!2023-10-22,16,271-->
47. [voiced palatal implosive](voiced%20palatal%20implosive.md)::\[ʄ\]
48. [voiceless velar plosive](voiceless%20velar%20plosive.md)::\[k\] <!--SR:!2023-10-28,29,331-->
49. [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::\[l\]
50. [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::\[ɫ\] <!--SR:!2024-01-09,109,337-->
51. [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::\[ɬ\] <!--SR:!2023-10-20,10,292-->
52. [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::\[ɭ\] <!--SR:!2023-10-14,15,311-->
53. [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)::\[ɺ\]
54. [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::\[ɮ\] <!--SR:!2023-11-05,24,271-->
55. [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::\[ʟ\]
56. [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::\[m\] <!--SR:!2023-10-27,15,332-->
57. [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::\[ɱ\] <!--SR:!2023-10-27,17,291-->
58. [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::\[n\] <!--SR:!2024-01-17,117,341-->
59. [voiced velar nasal](voiced%20velar%20nasal.md)::\[ŋ\] <!--SR:!2023-11-14,46,241-->
60. [voiced palatal nasal](voiced%20palatal%20nasal.md)::\[ɲ\] <!--SR:!2023-11-20,65,321-->
61. [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::\[ɳ\] <!--SR:!2023-10-24,12,311-->
62. [voiced uvular nasal](voiced%20uvular%20nasal.md)::\[ɴ\] <!--SR:!2023-11-26,58,319-->
63. [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::\[o\]
64. [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::\[ɔ\]
65. [nasalized open-mid back rounded vowel](nasal%20vowel.md)::\[ɔ̃\]
66. [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::\[ø\]
67. [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::\[ɵ\]
68. [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::\[œ\]
69. [nasalized open-mid front rounded vowel](nasal%20vowel.md)::\[œ̃\]
70. [open front rounded vowel](open%20front%20rounded%20vowel.md)::\[ɶ\]
71. [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::\[p\] <!--SR:!2023-10-22,23,331-->
72. [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::\[q\]
73. [voiced alveolar trill](voiced%20alveolar%20trill.md)::\[r\] <!--SR:!2023-10-30,18,331-->
74. [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::\[ɾ\]
75. [voiced uvular trill](voiced%20uvular%20trill.md)::\[ʀ\] <!--SR:!2024-02-11,127,320-->
76. [voiced retroflex flap](voiced%20retroflex%20flap.md)::\[ɽ\]
77. [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::\[ɹ\]
78. [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::\[ɻ\]
79. [voiced uvular fricative](voiced%20uvular%20fricative.md)::\[ʁ\] <!--SR:!2023-10-22,12,251-->
80. [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::\[s\] <!--SR:!2023-10-25,26,331-->
81. [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::\[ʃ\]
82. [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::\[ʂ\] <!--SR:!2023-11-20,39,291-->
83. [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::\[t\] <!--SR:!2024-01-24,123,339-->
84. [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::\[ʈ\]
85. [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::\[ts\] <!--SR:!2023-11-12,64,319-->
86. [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::\[tʃ\]
87. [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::\[tɕ\] <!--SR:!2023-12-01,56,308-->
88. [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::\[tʂ\]
89. [close back rounded vowel](close%20back%20rounded%20vowel.md)::\[u\] <!--SR:!2023-10-22,10,311-->
90. [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::\[ʊ\]
91. [close central rounded vowel](close%20central%20rounded%20vowel.md)::\[ʉ\]
92. [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::\[v\] <!--SR:!2023-12-15,90,337-->
93. [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::\[ʋ\] <!--SR:!2023-11-11,63,317-->
94. [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::\[w\]
95. [labialization](labialization.md)::\[ʷ\]
96. [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::\[ʍ\]
97. [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::\[ɯ\]
98. [voiced velar approximant](voiced%20velar%20approximant.md)::\[ɰ\]
99. [voiceless velar fricative](voiceless%20velar%20fricative.md)::\[x\]
100. [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::\[χ\] <!--SR:!2024-02-08,125,301-->
101. [close front rounded vowel](close%20front%20rounded%20vowel.md)::\[y\] <!--SR:!2023-11-22,47,311-->
102. [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::\[ʏ\]
103. [voiced velar fricative](voiced%20velar%20fricative.md)::\[ɣ\] <!--SR:!2023-10-17,7,231-->
104. [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::\[ɤ\] <!--SR:!2023-10-18,8,231-->
105. [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::\[ʎ\]
106. [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::\[ɥ\] <!--SR:!2023-10-29,13,311-->
107. [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::\[z\] <!--SR:!2023-10-22,23,331-->
108. [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::\[ʒ\] <!--SR:!2024-01-21,120,340-->
109. [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::\[ʑ\] <!--SR:!2024-01-02,88,280-->
110. [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::\[ʐ\] <!--SR:!2023-10-17,7,271-->
111. [voiceless dental fricative](voiceless%20dental%20fricative.md)::\[θ\] <!--SR:!2023-10-15,16,311-->
112. [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::\[ɸ\]
113. [glottal stop](glottal%20stop.md)::\[ʔ\] <!--SR:!2024-01-20,120,341-->
114. [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::\[ʕ\]
115. [tenuis dental click](tenuis%20dental%20click.md)::\[ǀ\]
116. [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::\[ǁ\] <!--SR:!2023-10-23,13,291-->
117. [tenuis alveolar click](tenuis%20alveolar%20click.md)::\[ǃ\]
118. [tenuis bilabial click](tenuis%20bilabial%20click.md)::\[ʘ\] <!--SR:!2023-12-08,84,341-->
119. [tenuis palatal click](tenuis%20palatal%20click.md)::\[ǂ\]

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d92e"--><!-- The following content is generated at 2023-08-09T19:34:04.091616+08:00. Any edits will be overridden! -->

1. \[a\]::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2023-12-07,83,338-->
2. \[ä\]::[open central unrounded vowel](open%20central%20unrounded%20vowel.md)
3. \[ɐ\]::[near-open central vowel](near-open%20central%20vowel.md)
4. \[ɑ\]::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2023-10-25,26,331-->
5. \[ɑ̃\]::[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2023-10-28,52,317-->
6. \[ɒ\]::[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2023-12-08,84,339-->
7. \[ʌ\]::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2023-10-14,2,292-->
8. \[æ\]::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)
9. \[b\]::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2024-01-21,120,337-->
10. \[ɓ\]::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2024-01-23,122,338-->
11. \[β\]::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2023-10-30,18,331-->
12. \[ʙ\]::[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2023-11-03,28,331-->
13. \[c\]::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2023-10-20,21,311-->
14. \[ç\]::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2023-11-11,57,301-->
15. \[ɕ\]::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2023-11-13,34,291-->
16. \[d\]::[voiced alveolar plosive](voiced%20alveolar%20plosive.md)
17. \[ɗ\]::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2023-11-01,16,332-->
18. \[ɖ\]::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2023-10-14,15,311-->
19. \[ð\]::[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2023-12-03,72,321-->
20. \[dz\]::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2023-10-28,29,331-->
21. \[dʒ\]::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)
22. \[dʑ\]::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2023-11-03,49,277-->
23. \[dʐ\]::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2023-10-15,16,311-->
24. \[e\]::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)
25. \[ɘ\]::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)
26. \[ə\]::[mid central vowel](mid%20central%20vowel.md) <!--SR:!2024-01-23,122,337-->
27. \[ɚ\]::[r-colored mid central vowel](r-colored%20vowel.md)
28. \[ɛ\]::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)
29. \[ɛ̃\]::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2023-10-14,38,301-->
30. \[ɜ\]::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2023-10-11,4,312-->
31. \[ɝ\]::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2023-11-19,65,321-->
32. \[f\]::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2023-10-26,27,331-->
33. \[ɡ\]::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2023-10-11,4,312-->
34. \[ɠ\]::[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2023-11-02,27,331-->
35. \[ɢ\]::[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2023-10-13,37,298-->
36. \[h\]::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2024-01-18,118,340-->
37. \[ɦ\]::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2023-10-23,24,311-->
38. \[ʰ\]::[aspirated consonant](aspirated%20consonant.md) <!--SR:!2024-01-10,110,337-->
39. \[ħ\]::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2023-10-21,28,328-->
40. \[i\]::[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!2024-01-12,112,337-->
41. \[ɪ\]::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2023-10-19,13,271-->
42. \[ɨ\]::[close central unrounded vowel](close%20central%20unrounded%20vowel.md) <!--SR:!2024-01-27,126,341-->
43. \[j\]::[voiced palatal approximant](voiced%20palatal%20approximant.md)
44. \[ʲ\]::[palatalization](palatalization%20(phonetics).md)
45. \[ʝ\]::[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!2023-10-12,2,271-->
46. \[ɟ\]::[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2023-10-31,19,331-->
47. \[ʄ\]::[voiced palatal implosive](voiced%20palatal%20implosive.md) <!--SR:!2023-10-30,18,331-->
48. \[k\]::[voiceless velar plosive](voiceless%20velar%20plosive.md) <!--SR:!2023-12-06,75,321-->
49. \[l\]::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)
50. \[ɫ\]::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) <!--SR:!2023-11-14,66,317-->
51. \[ɬ\]::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2023-10-25,15,251-->
52. \[ɭ\]::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!2023-10-19,9,292-->
53. \[ɺ\]::[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)
54. \[ɮ\]::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!2023-10-25,19,251-->
55. \[ʟ\]::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!2023-10-20,8,251-->
56. \[m\]::[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2023-10-29,17,331-->
57. \[ɱ\]::[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2023-10-31,19,331-->
58. \[n\]::[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!2024-01-19,119,340-->
59. \[ŋ\]::[voiced velar nasal](voiced%20velar%20nasal.md)
60. \[ɲ\]::[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2023-11-18,56,281-->
61. \[ɳ\]::[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2023-10-26,47,297-->
62. \[ɴ\]::[voiced uvular nasal](voiced%20uvular%20nasal.md)
63. \[o\]::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
64. \[ɔ\]::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)
65. \[ɔ̃\]::[nasalized open-mid back rounded vowel](nasal%20vowel.md)
66. \[ø\]::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
67. \[ɵ\]::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)
68. \[œ\]::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
69. \[œ̃\]::[nasalized open-mid front rounded vowel](nasal%20vowel.md) <!--SR:!2023-10-11,12,291-->
70. \[ɶ\]::[open front rounded vowel](open%20front%20rounded%20vowel.md)
71. \[p\]::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2024-01-18,117,337-->
72. \[q\]::[voiceless uvular plosive](voiceless%20uvular%20plosive.md)
73. \[r\]::[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2023-11-20,45,311-->
74. \[ɾ\]::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2023-10-11,4,312-->
75. \[ʀ\]::[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2023-10-17,18,311-->
76. \[ɽ\]::[voiced retroflex flap](voiced%20retroflex%20flap.md)
77. \[ɹ\]::[voiced alveolar approximant](voiced%20alveolar%20approximant.md) <!--SR:!2023-11-29,61,321-->
78. \[ɻ\]::[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
79. \[ʁ\]::[voiced uvular fricative](voiced%20uvular%20fricative.md)
80. \[s\]::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2024-01-25,124,338-->
81. \[ʃ\]::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) <!--SR:!2023-12-25,70,331-->
82. \[ʂ\]::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2023-10-21,22,311-->
83. \[t\]::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!2023-10-11,4,311-->
84. \[ʈ\]::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!2023-10-28,16,331-->
85. \[ts\]::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) <!--SR:!2023-10-11,4,312-->
86. \[tʃ\]::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
87. \[tɕ\]::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) <!--SR:!2023-10-11,4,311-->
88. \[tʂ\]::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!2023-12-07,83,320-->
89. \[u\]::[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2024-01-02,95,280-->
90. \[ʊ\]::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
91. \[ʉ\]::[close central rounded vowel](close%20central%20rounded%20vowel.md)
92. \[v\]::[voiced labiodental fricative](voiced%20labiodental%20fricative.md)
93. \[ʋ\]::[voiced labiodental approximant](voiced%20labiodental%20approximant.md) <!--SR:!2023-10-23,44,297-->
94. \[w\]::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2024-03-05,145,321-->
95. \[ʷ\]::[labialization](labialization.md)
96. \[ʍ\]::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
97. \[ɯ\]::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2023-12-03,79,320-->
98. \[ɰ\]::[voiced velar approximant](voiced%20velar%20approximant.md)
99. \[x\]::[voiceless velar fricative](voiceless%20velar%20fricative.md)
100. \[χ\]::[voiceless uvular fricative](voiceless%20uvular%20fricative.md)
101. \[y\]::[close front rounded vowel](close%20front%20rounded%20vowel.md) <!--SR:!2024-01-15,115,340-->
102. \[ʏ\]::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) <!--SR:!2023-10-26,20,251-->
103. \[ɣ\]::[voiced velar fricative](voiced%20velar%20fricative.md)
104. \[ɤ\]::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
105. \[ʎ\]::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
106. \[ɥ\]::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) <!--SR:!2023-10-20,14,291-->
107. \[z\]::[voiced alveolar fricative](voiced%20alveolar%20fricative.md)
108. \[ʒ\]::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) <!--SR:!2023-10-19,42,299-->
109. \[ʑ\]::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) <!--SR:!2023-10-30,18,331-->
110. \[ʐ\]::[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
111. \[θ\]::[voiceless dental fricative](voiceless%20dental%20fricative.md) <!--SR:!2023-11-04,29,331-->
112. \[ɸ\]::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
113. \[ʔ\]::[glottal stop](glottal%20stop.md) <!--SR:!2023-10-23,24,331-->
114. \[ʕ\]::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
115. \[ǀ\]::[tenuis dental click](tenuis%20dental%20click.md)
116. \[ǁ\]::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) <!--SR:!2023-10-11,4,311-->
117. \[ǃ\]::[tenuis alveolar click](tenuis%20alveolar%20click.md)
118. \[ʘ\]::[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2023-12-04,80,340-->
119. \[ǂ\]::[tenuis palatal click](tenuis%20palatal%20click.md) <!--SR:!2023-11-28,60,260-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–audio

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5dfb"--><!-- The following content is generated at 2023-08-24T20:02:35.307234+08:00. Any edits will be overridden! -->

1. [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg) <!--SR:!2023-10-27,28,331-->
2. [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) <!--SR:!2024-05-02,222,284-->
3. [near-open central vowel](near-open%20central%20vowel.md)::![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) <!--SR:!2023-12-01,106,264-->
4. [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) <!--SR:!2024-08-03,301,313-->
5. [nasalized open back unrounded vowel](nasal%20vowel.md)::![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) <!--SR:!2023-11-15,36,291-->
6. [open back rounded vowel](open%20back%20rounded%20vowel.md)::![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) <!--SR:!2023-10-30,96,304-->
7. [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) <!--SR:!2024-05-28,231,293-->
8. [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)
9. [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) <!--SR:!2024-01-26,133,338-->
10. [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) <!--SR:!2024-01-31,137,338-->
11. [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) <!--SR:!2023-12-16,91,341-->
12. [voiced bilabial trill](voiced%20bilabial%20trill.md)::![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) <!--SR:!2024-01-19,118,337-->
13. [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) <!--SR:!2023-10-18,38,301-->
14. [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) <!--SR:!2023-10-11,12,291-->
15. [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) <!--SR:!2023-11-12,33,291-->
16. [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) <!--SR:!2023-10-23,90,298-->
17. [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) <!--SR:!2023-12-14,59,331-->
18. [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)
19. [voiced dental fricative](voiced%20dental%20fricative.md)::![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) <!--SR:!2023-10-21,88,304-->
20. [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)
21. [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)
22. [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) <!--SR:!2023-12-26,71,258-->
23. [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) <!--SR:!2023-10-30,38,218-->
24. [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2023-10-26,57,278-->
25. [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)
26. [mid central vowel](mid%20central%20vowel.md)::![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) <!--SR:!2024-04-26,203,284-->
27. [r-colored mid central vowel](r-colored%20vowel.md)::![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2023-11-29,48,311-->
28. [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2023-10-12,6,251-->
29. [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) <!--SR:!2023-10-21,11,292-->
30. [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2023-10-30,57,298-->
31. [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2024-02-03,116,278-->
32. [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) <!--SR:!2023-10-11,4,312-->
33. [voiced velar plosive](voiced%20velar%20plosive.md)::![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) <!--SR:!2023-10-27,28,331-->
34. [voiced velar implosive](voiced%20velar%20implosive.md)::![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)
35. [voiced uvular plosive](voiced%20uvular%20plosive.md)::![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)
36. [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) <!--SR:!2023-11-03,66,318-->
37. [voiced glottal fricative](voiced%20glottal%20fricative.md)::![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) <!--SR:!2023-11-14,35,291-->
38. [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) <!--SR:!2023-11-28,47,311-->
39. [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) <!--SR:!2024-01-15,166,333-->
40. [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) <!--SR:!2023-11-24,63,258-->
41. [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)
42. [voiced palatal approximant](voiced%20palatal%20approximant.md)::![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)
43. [voiced palatal fricative](voiced%20palatal%20fricative.md)::![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) <!--SR:!2023-12-17,116,264-->
44. [voiced palatal plosive](voiced%20palatal%20plosive.md)::![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)
45. [voiced palatal implosive](voiced%20palatal%20implosive.md)::![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) <!--SR:!2023-10-14,15,311-->
46. [voiceless velar plosive](voiceless%20velar%20plosive.md)::![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)
47. [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) <!--SR:!2023-11-27,73,278-->
48. [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) <!--SR:!2023-10-15,39,297-->
49. [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) <!--SR:!2023-10-31,67,204-->
50. [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)
51. [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) <!--SR:!2023-10-18,46,278-->
52. [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) <!--SR:!2023-11-16,41,288-->
53. [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) <!--SR:!2023-12-09,78,321-->
54. [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) <!--SR:!2023-10-11,4,311-->
55. [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)
56. [voiced velar nasal](voiced%20velar%20nasal.md)::![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) <!--SR:!2023-10-11,4,311-->
57. [voiced palatal nasal](voiced%20palatal%20nasal.md)::![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) <!--SR:!2023-10-11,4,311-->
58. [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) <!--SR:!2024-01-13,89,238-->
59. [voiced uvular nasal](voiced%20uvular%20nasal.md)::![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) <!--SR:!2024-03-31,183,273-->
60. [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) <!--SR:!2023-10-14,46,298-->
61. [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) <!--SR:!2023-10-11,4,312-->
62. [nasalized open-mid back rounded vowel](nasal%20vowel.md)::![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)
63. [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) <!--SR:!2023-11-14,52,260-->
64. [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)
65. [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) <!--SR:!2023-10-22,6,130-->
66. [nasalized open-mid front rounded vowel](nasal%20vowel.md)::![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) <!--SR:!2023-11-11,32,271-->
67. [open front rounded vowel](open%20front%20rounded%20vowel.md)::![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) <!--SR:!2023-11-08,54,298-->
68. [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) <!--SR:!2023-10-22,89,293-->
69. [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) <!--SR:!2023-10-11,12,291-->
70. [voiced alveolar trill](voiced%20alveolar%20trill.md)::![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) <!--SR:!2024-03-21,161,298-->
71. [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) <!--SR:!2023-11-03,99,304-->
72. [voiced uvular trill](voiced%20uvular%20trill.md)::![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)
73. [voiced retroflex flap](voiced%20retroflex%20flap.md)::![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) <!--SR:!2023-10-11,12,291-->
74. [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) <!--SR:!2023-11-04,36,253-->
75. [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)
76. [voiced uvular fricative](voiced%20uvular%20fricative.md)::![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) <!--SR:!2023-10-24,17,291-->
77. [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)
78. [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) <!--SR:!2024-01-31,161,284-->
79. [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) <!--SR:!2023-12-02,47,218-->
80. [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) <!--SR:!2024-01-28,121,298-->
81. [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)
82. [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)
83. [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) <!--SR:!2023-10-11,12,291-->
84. [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) <!--SR:!2023-10-21,11,292-->
85. [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) <!--SR:!2023-11-05,20,291-->
86. [close back rounded vowel](close%20back%20rounded%20vowel.md)::![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)
87. [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) <!--SR:!2023-10-22,50,278-->
88. [close central rounded vowel](close%20central%20rounded%20vowel.md)::![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) <!--SR:!2023-11-04,19,332-->
89. [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) <!--SR:!2023-11-30,45,311-->
90. [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) <!--SR:!2023-12-05,73,258-->
91. [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) <!--SR:!2024-03-09,161,293-->
92. [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) <!--SR:!2023-11-07,28,311-->
93. [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) <!--SR:!2023-11-09,55,300-->
94. [voiced velar approximant](voiced%20velar%20approximant.md)::![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)
95. [voiceless velar fricative](voiceless%20velar%20fricative.md)::![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) <!--SR:!2023-10-21,11,291-->
96. [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) <!--SR:!2024-01-22,104,258-->
97. [close front rounded vowel](close%20front%20rounded%20vowel.md)::![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) <!--SR:!2023-10-11,4,311-->
98. [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)
99. [voiced velar fricative](voiced%20velar%20fricative.md)::![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) <!--SR:!2023-10-27,11,312-->
100. [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)
101. [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) <!--SR:!2023-10-21,11,292-->
102. [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) <!--SR:!2023-10-20,14,193-->
103. [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) <!--SR:!2024-04-25,229,304-->
104. [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)
105. [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)
106. [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)
107. [voiceless dental fricative](voiceless%20dental%20fricative.md)::![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) <!--SR:!2024-01-19,101,297-->
108. [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) <!--SR:!2024-05-14,234,293-->
109. [glottal stop](glottal%20stop.md)::![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg) <!--SR:!2023-11-10,69,298-->
110. [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)
111. [tenuis dental click](tenuis%20dental%20click.md)::![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) <!--SR:!2023-10-17,18,311-->
112. [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) <!--SR:!2024-01-05,91,224-->
113. [tenuis alveolar click](tenuis%20alveolar%20click.md)::![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) <!--SR:!2023-11-22,67,320-->
114. [tenuis bilabial click](tenuis%20bilabial%20click.md)::![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg) <!--SR:!2024-01-15,115,341-->
115. [tenuis palatal click](tenuis%20palatal%20click.md)::![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) <!--SR:!2023-10-16,17,311-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f9aa"--><!-- The following content is generated at 2023-08-24T20:02:35.341149+08:00. Any edits will be overridden! -->

1. ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)::[open front unrounded vowel](open%20front%20unrounded%20vowel.md)
2. ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2023-10-21,21,173-->
3. ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)::[near-open central vowel](near-open%20central%20vowel.md)
4. ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2023-10-16,6,251-->
5. ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)::[nasalized open back unrounded vowel](nasal%20vowel.md)
6. ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)::[open back rounded vowel](open%20back%20rounded%20vowel.md)
7. ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)
8. ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)
9. ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)::[voiced bilabial plosive](voiced%20bilabial%20plosive.md)
10. ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)::[voiced bilabial implosive](voiced%20bilabial%20implosive.md)
11. ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2023-11-15,36,291-->
12. ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)::[voiced bilabial trill](voiced%20bilabial%20trill.md)
13. ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)::[voiceless palatal plosive](voiceless%20palatal%20plosive.md)
14. ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)::[voiceless palatal fricative](voiceless%20palatal%20fricative.md)
15. ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)
16. ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2024-03-24,177,273-->
17. ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)::[voiced alveolar implosive](voiced%20alveolar%20implosive.md)
18. ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)::[voiced retroflex plosive](voiced%20retroflex%20plosive.md)
19. ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)::[voiced dental fricative](voiced%20dental%20fricative.md)
20. ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)::[voiced alveolar affricate](voiced%20alveolar%20affricate.md)
21. ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)
22. ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)
23. ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)::[voiced retroflex affricate](voiced%20retroflex%20affricate.md)
24. ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2023-10-14,2,292-->
25. ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)
26. ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)::[mid central vowel](mid%20central%20vowel.md)
27. ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2023-11-06,30,239-->
28. ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)
29. ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)::[nasalized open-mid front unrounded vowel](nasal%20vowel.md)
30. ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)
31. ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md)
32. ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2023-10-29,70,233-->
33. ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2023-10-13,14,311-->
34. ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)::[voiced velar implosive](voiced%20velar%20implosive.md)
35. ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)::[voiced uvular plosive](voiced%20uvular%20plosive.md)
36. ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2023-10-18,46,278-->
37. ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2023-10-25,18,291-->
38. ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)
39. ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)::[close front unrounded vowel](close%20front%20unrounded%20vowel.md)
40. ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)
41. ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)::[close central unrounded vowel](close%20central%20unrounded%20vowel.md)
42. ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)::[voiced palatal approximant](voiced%20palatal%20approximant.md)
43. ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)::[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!2023-10-15,5,251-->
44. ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)::[voiced palatal plosive](voiced%20palatal%20plosive.md)
45. ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)::[voiced palatal implosive](voiced%20palatal%20implosive.md)
46. ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)::[voiceless velar plosive](voiceless%20velar%20plosive.md)
47. ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) <!--SR:!2024-01-04,90,280-->
48. ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)
49. ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2023-10-19,9,231-->
50. ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)
51. ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!2023-10-17,11,231-->
52. ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)
53. ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)::[voiced bilabial nasal](voiced%20bilabial%20nasal.md)
54. ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)::[voiced labiodental nasal](voiced%20labiodental%20nasal.md)
55. ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)::[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!2023-12-15,75,193-->
56. ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)::[voiced velar nasal](voiced%20velar%20nasal.md)
57. ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)::[voiced palatal nasal](voiced%20palatal%20nasal.md)
58. ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)::[voiced retroflex nasal](voiced%20retroflex%20nasal.md)
59. ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)::[voiced uvular nasal](voiced%20uvular%20nasal.md)
60. ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
61. ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)
62. ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)::[nasalized open-mid back rounded vowel](nasal%20vowel.md)
63. ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
64. ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2023-10-18,8,153-->
65. ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
66. ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)::[nasalized open-mid front rounded vowel](nasal%20vowel.md)
67. ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)::[open front rounded vowel](open%20front%20rounded%20vowel.md)
68. ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2023-11-03,35,253-->
69. ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)::[voiceless uvular plosive](voiceless%20uvular%20plosive.md)
70. ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)::[voiced alveolar trill](voiced%20alveolar%20trill.md)
71. ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)
72. ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)::[voiced uvular trill](voiced%20uvular%20trill.md)
73. ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)::[voiced retroflex flap](voiced%20retroflex%20flap.md)
74. ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)::[voiced alveolar approximant](voiced%20alveolar%20approximant.md)
75. ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)::[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
76. ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)::[voiced uvular fricative](voiced%20uvular%20fricative.md)
77. ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2023-11-02,17,251-->
78. ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)
79. ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)
80. ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)
81. ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)
82. ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)
83. ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
84. ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)
85. ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)
86. ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)::[close back rounded vowel](close%20back%20rounded%20vowel.md)
87. ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
88. ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)::[close central rounded vowel](close%20central%20rounded%20vowel.md)
89. ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)::[voiced labiodental fricative](voiced%20labiodental%20fricative.md) <!--SR:!2023-10-18,38,299-->
90. ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)::[voiced labiodental approximant](voiced%20labiodental%20approximant.md)
91. ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2023-11-15,36,291-->
92. ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
93. ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2023-10-11,12,291-->
94. ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)::[voiced velar approximant](voiced%20velar%20approximant.md) <!--SR:!2023-10-18,2,191-->
95. ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)::[voiceless velar fricative](voiceless%20velar%20fricative.md) <!--SR:!2023-10-22,6,130-->
96. ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)::[voiceless uvular fricative](voiceless%20uvular%20fricative.md)
97. ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)::[close front rounded vowel](close%20front%20rounded%20vowel.md) <!--SR:!2024-01-27,145,273-->
98. ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
99. ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)::[voiced velar fricative](voiced%20velar%20fricative.md)
100. ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
101. ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
102. ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
103. ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)::[voiced alveolar fricative](voiced%20alveolar%20fricative.md) <!--SR:!2023-10-29,22,164-->
104. ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
105. ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)
106. ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)::[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
107. ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)::[voiceless dental fricative](voiceless%20dental%20fricative.md)
108. ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) <!--SR:!2023-10-16,6,211-->
109. ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)::[glottal stop](glottal%20stop.md) <!--SR:!2023-10-28,12,260-->
110. ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) <!--SR:!2023-11-08,29,201-->
111. ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)::[tenuis dental click](tenuis%20dental%20click.md)
112. ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)
113. ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)::[tenuis alveolar click](tenuis%20alveolar%20click.md)
114. ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)::[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2023-10-28,29,331-->
115. ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)::[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485d"--><!-- The following content is generated at 2023-08-09T19:34:04.169408+08:00. Any edits will be overridden! -->

> | name | symbol | description |
> |-|-|-|
> | [nasalized](nasal%20vowel.md) | \[◌̃\] (e.g. [ã]) | {{[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"}} |
> | [centralized](central%20vowel.md) | \[◌̈\] (e.g. [ä]) | {{[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"}} |
> | [extra-short](extra-shortness.md) | \[◌̆\] (e.g. [ă]) | {{[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]}} |
> | [non-syllabic](diphthong.md) | \[◌̯\] (e.g. [a̯]) | {{[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]}} |
> | [voiceless](voicelessness.md) | \[◌̥\] (e.g. [n̥]) | {{[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]}} |
> | [syllabic](syllabic%20consonant.md) | \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) | {{[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]}} |
> | [dental/alveolar](dental%20consonant.md) | \[◌̪\] (e.g. [d̪]) | {{[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"}} |
> | [aspirated](aspirated%20consonant.md) | \[◌ʰ\] (e.g. [kʰ]) | {{[English](English%20language.md) _**c**ome_ \[kʰɐm\]}} |
> | [ejective](ejective%20consonant.md) | \[◌’\] (e.g. [k’]) | {{[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"}} |
> | [long](longness%20(phonetics).md) | \[◌ː\] (e.g. [aː]) | {{[English](English%20language.md) _shh!_ \[ʃː\]}} |
> | [half-long](half-longness%20(phonetics).md) | \[◌ˑ\] (e.g. [aˑ]) | {{[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]}} |
> | [primary stress](stress%20(lingustics).md) | \[ˈ◌\] (e.g. [ˈa]) | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | [secondary stress](secondary%20stress.md) | \[ˌ◌\] (e.g. [ˌa]) | {{[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]}} |
> | [syllable break](syllable.md) | \[.\] | {{[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]}} | <!--SR:!2023-12-26,115,258!2023-10-24,65,224!2023-12-12,112,264!2024-07-24,299,313!2024-01-11,111,318!2023-10-20,47,258!2023-11-12,71,318!2024-01-28,135,338!2023-11-06,37,217!2024-01-12,112,338!2023-11-18,50,259!2023-10-17,18,311!2023-10-20,10,292-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ffa2"--><!-- The following content is generated at 2023-08-09T19:34:04.142481+08:00. Any edits will be overridden! -->

1. [nasalized](nasal%20vowel.md)::\[◌̃\] (e.g. [ã]) <!--SR:!2023-11-03,28,331-->
2. [centralized](central%20vowel.md)::\[◌̈\] (e.g. [ä])
3. [extra-short](extra-shortness.md)::\[◌̆\] (e.g. [ă]) <!--SR:!2023-11-02,56,321-->
4. [non-syllabic](diphthong.md)::\[◌̯\] (e.g. [a̯])
5. [voiceless](voicelessness.md)::\[◌̥\] (e.g. [n̥])
6. [syllabic](syllabic%20consonant.md)::\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) <!--SR:!2023-11-01,55,321-->
7. [dental/alveolar](dental%20consonant.md)::\[◌̪\] (e.g. [d̪]) <!--SR:!2023-12-05,81,340-->
8. [aspirated](aspirated%20consonant.md)::\[◌ʰ\] (e.g. [kʰ]) <!--SR:!2024-01-20,119,340-->
9. [ejective](ejective%20consonant.md)::\[◌’\] (e.g. [k’])
10. [long](longness%20(phonetics).md)::\[◌ː\] (e.g. [aː])
11. [half-long](half-longness%20(phonetics).md)::\[◌ˑ\] (e.g. [aˑ]) <!--SR:!2024-01-26,125,341-->
12. [primary stress](stress%20(lingustics).md)::\[ˈ◌\] (e.g. [ˈa])
13. [secondary stress](secondary%20stress.md)::\[ˌ◌\] (e.g. [ˌa]) <!--SR:!2023-10-11,4,312-->
14. [syllable break](syllable.md)::\[.\] <!--SR:!2023-10-11,4,312-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="94fb"--><!-- The following content is generated at 2023-08-09T19:34:04.066684+08:00. Any edits will be overridden! -->

1. \[◌̃\] (e.g. [ã])::[nasalized](nasal%20vowel.md) <!--SR:!2023-10-19,86,290-->
2. \[◌̈\] (e.g. [ä])::[centralized](central%20vowel.md) <!--SR:!2023-11-09,102,298-->
3. \[◌̆\] (e.g. [ă])::[extra-short](extra-shortness.md) <!--SR:!2023-12-05,81,264-->
4. \[◌̯\] (e.g. [a̯])::[non-syllabic](diphthong.md) <!--SR:!2023-11-08,39,264-->
5. \[◌̥\] (e.g. [n̥])::[voiceless](voicelessness.md) <!--SR:!2023-10-19,86,293-->
6. \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])::[syllabic](syllabic%20consonant.md) <!--SR:!2023-11-02,17,258-->
7. \[◌̪\] (e.g. [d̪])::[dental/alveolar](dental%20consonant.md) <!--SR:!2024-04-14,181,318-->
8. \[◌ʰ\] (e.g. [kʰ])::[aspirated](aspirated%20consonant.md) <!--SR:!2024-03-13,172,338-->
9. \[◌’\] (e.g. [k’])::[ejective](ejective%20consonant.md) <!--SR:!2023-11-09,68,298-->
10. \[◌ː\] (e.g. [aː])::[long](longness%20(phonetics).md) <!--SR:!2024-01-22,121,337-->
11. \[◌ˑ\] (e.g. [aˑ])::[half-long](half-longness%20(phonetics).md) <!--SR:!2023-10-20,21,311-->
12. \[ˈ◌\] (e.g. [ˈa])::[primary stress](stress%20(lingustics).md)
13. \[ˌ◌\] (e.g. [ˌa])::[secondary stress](secondary%20stress.md) <!--SR:!2023-10-27,51,317-->
14. \[.\]::[syllable break](syllable.md) <!--SR:!2023-12-18,93,341-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
