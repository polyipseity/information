---
aliases:
  - IPA help
  - IPA usage
  - International Phonetic Alphabet help
  - International Phonetic Alphabet usage
tags:
  - flashcards/special/language_acquisition/International_Phonetic_Alphabet
  - languages/in/English
---

# International Phonetic Alphabet

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../tools/utility.py.md
```

%%

> ![official IPA chart](../../archives/Wikimedia%20Commons/IPA%20chart%202020.svg)
>
> official IPA chart

<!-- markdownlint MD028 -->

> [!tip] tip
>
> - phonetic symbols: {{notice that the symbol of each phonetic is somewhat related to its sound, and similarly-sounding phonetics usually have similar symbols}} <!--SR:!2024-03-15,76,354-->

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
  ('[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)', R'\[ɵ\]', '![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)', R'[English](English%20language.md) _f**oo**t_ \[fɵʔt\]',),
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
  ('[voiced alveolar fricative](voiced%20alveolar%20fricative.md)', R'\[z\]', '![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]',),
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
    e.cwf_sects("958a", None),
    ("name", "symbol", "audio", "description",),
    letters,
  ),
  memorize_map(
    e.cwf_sects(None, "059f", "d92e"),
    items_to_map(*(datum[:2] for datum in letters)),
  ),
  memorize_map(
    e.cwf_sects(None, "5dfb", "f9aa"),
    items_to_map(*((datum[0], datum[2]) for datum in letters if datum[2])),
  ),
  memorize_map(
    e.cwf_sects(None, "50b0", None),
    items_to_map(*((datum[0], datum[3]) for datum in letters)),
  ),
  memorize_table(
    e.cwf_sects("485d", None),
    ("name", "symbol", "description",),
    diacritics,
  ),
  memorize_map(
    e.cwf_sects(None, "ffa2", "94fb"),
    items_to_map(*(datum[:2] for datum in diacritics)),
  ),
  memorize_map(
    e.cwf_sects(None, "50bd", None),
    items_to_map(*((datum[0], datum[2]) for datum in diacritics)),
  ),
))
```

%%

### glossary

> ![places of articulation](../../archives/Wikimedia%20Commons/Places%20of%20articulation.svg)
>
> [place of articulation](place%20of%20articulation.md)
>
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
> 18. {{sub-laminal/sub-apical ([tongue](tongue.md) underside)}} <!--SR:!2025-02-15,462,330!2025-09-02,623,338!2025-10-11,656,344!2025-01-07,424,324!2024-11-06,357,324!2024-08-21,285,324!2025-01-16,433,324!2024-04-05,193,293!2025-02-02,449,333!2024-06-04,140,253!2024-07-18,293,313!2025-12-19,715,353!2024-03-14,167,318!2024-08-06,246,317!2024-10-11,302,341!2024-02-23,16,230!2024-10-30,268,330!2024-09-03,222,330-->

- [consonant](consonant.md):::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2024-05-24,244,290!2025-02-21,467,330-->
  - [airstream mechanism](airstream%20mechanism.md):::how the moving [air](air.md) is thrusted <!--SR:!2024-09-12,338,318!2025-06-18,561,343-->
- (all) [pulmonic](pulmonic%20consonant.md) egressive:::[air](air.md) is exhaled from the [lungs](lung.md) <!--SR:!2024-12-21,406,333!2025-10-23,632,358-->
- (16%) [glottalic](glottalic%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md) <!--SR:!2024-03-08,118,351!2024-07-30,181,310-->
- (13%) [glottalic](glottalic%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md) <!--SR:!2024-02-27,109,351!2024-02-09,22,270-->
    - (<2%) lingual/[velaric](velar%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md) <!--SR:!2024-06-04,193,331!2024-03-01,63,290-->
    - ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive:::[air](air.md) is inhaled into the [lungs](lung.md) <!--SR:!2025-01-14,428,333!2025-01-15,432,333-->
    - ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md) <!--SR:!2024-08-02,225,279!2025-01-18,403,361-->
- [length](gemination.md):::how long the articulation of a [consonant](consonant.md) lasts <!--SR:!2024-05-17,188,298!2024-09-19,235,330-->
- values in ascending [length](gemination.md)::single/singleton, geminate, long geminate <!--SR:!2024-03-16,64,273-->
  - [manner of articulation](manner%20of%20articulation.md):::configuration and interaction of the [speech organs](speech%20organ.md) <!--SR:!2024-06-12,201,331!2024-02-13,57,310-->
    - [affricate](affricate%20consonant.md):::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md) <!--SR:!2024-04-23,164,317!2024-02-08,66,310-->
    - [approximant](approximant%20consonant.md):::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md) <!--SR:!2024-02-17,176,293!2025-04-05,474,358-->
      - [lateral approximant](lateral%20consonant.md):::approximant with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2024-03-28,185,284!2024-12-14,399,324-->
- [semivowel/glide/semiconsonant](semivowel.md):::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary <!--SR:!2024-05-09,143,312!2024-07-31,182,310-->
- [flap/tap](tap%20and%20flap%20consonants.md):::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact <!--SR:!2024-06-26,228,298!2024-10-31,269,330-->
    - [fricative/spirant](fricative%20consonant.md):::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation <!--SR:!2024-03-16,86,224!2024-03-12,171,338-->
- [lateral](lateral%20consonant.md):::fricative with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2024-11-18,291,352!2024-02-09,66,310-->
      - [sibilant](sibilant%20consonant.md):::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md) <!--SR:!2024-05-19,191,321!2024-03-21,131,351-->
    - [nasal](nasal%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow <!--SR:!2024-04-24,166,317!2024-02-15,72,352-->
    - [plosive/stop](plosive%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow <!--SR:!2024-08-26,287,341!2024-03-02,113,351-->
- [trill](trill%20consonant.md):::consonant produced by vibrations between the active articulator and the passive articulator <!--SR:!2024-09-02,264,298!2025-07-12,543,361-->
- [place of articulation](place%20of%20articulation.md):::location along the [vocal tract](vocal%20tract.md) producing the consonant <!--SR:!2024-04-06,213,304!2025-06-27,530,358-->
    - [alveolar](alveolar%20ridge.md):::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive) <!--SR:!2024-08-15,272,339!2024-02-08,61,310-->
    - [aryepiglottal](pharyngeal%20consonant.md):::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active) <!--SR:!2024-03-21,209,333!2024-03-12,122,351-->
    - [coronal](coronal%20constant.md):::front of the [tongue](tongue.md) (active) <!--SR:!2024-05-24,231,293!2024-08-25,282,298-->
- [apical](apical%20consonant.md):::tip of the [tongue](tongue.md) (active) <!--SR:!2024-12-17,403,324!2025-07-19,548,358-->
      - [laminal](laminal%20consonant.md):::blade of the [tongue](tongue.md), the upper front surface behind the tip (active) <!--SR:!2024-05-29,200,253!2024-03-21,83,240-->
      - [subapical](subapical%20consonant.md):::surface under the tip of the [tongue](tongue.md) (active) <!--SR:!2024-12-10,395,324!2025-10-28,674,353-->
- [dental](dental%20consonant.md):::upper [teeth](tooth.md) (passive) <!--SR:!2024-08-15,308,313!2024-08-30,218,330-->
    - [dorsal](dorsal%20consonant.md):::body of the [tongue](tongue.md) (active) <!--SR:!2024-04-05,222,333!2025-04-04,497,333-->
- [epiglottal](pharyngeal%20consonant.md):::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive) <!--SR:!2025-07-31,559,361!2025-04-07,425,372-->
    - [glottal](glottal%20consonant.md):::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active) <!--SR:!2024-03-13,188,293!2025-12-08,706,353-->
    - [labial](labial%20consonant.md):::lower [lip](lip.md) (active), upper [lip](lip.md) (passive) <!--SR:!2025-03-01,453,304!2025-09-10,637,353-->
- [palatal](palatal%20consonant.md):::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2024-10-18,343,304!2024-10-09,251,330-->
    - [pharyngeal](pharyngeal%20consonant.md):::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive) <!--SR:!2024-09-05,246,278!2024-02-15,55,311-->
- [post-alveolar](post-alveolar%20consonant.md):::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive) <!--SR:!2025-08-17,570,357!2024-03-20,130,351-->
- [uvular](uvular%20consonant.md):::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive) <!--SR:!2024-03-29,186,284!2025-01-06,347,372-->
- [velar](velar%20consonant.md):::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2024-06-29,231,298!2025-06-24,527,357-->
- [phonation](phonation.md):::how the [vocal cords](vocal%20folds.md) vibrate <!--SR:!2024-03-21,105,301!2025-06-25,529,361-->
- [voiced](voice%20(phonetics).md):::the [vocal cords](vocal%20cords.md) vibrate fully <!--SR:!2025-07-15,589,344!2025-08-12,565,358-->
- [voiceless](voicelessness.md):::the [vocal cords](vocal%20cords.md) do not vibrate <!--SR:!2025-08-05,609,353!2026-01-14,733,353-->
- [voice onset time](voice%20onset%20time.md) (VOT):::timing of [phonation](phonation.md) <!--SR:!2024-11-22,375,333!2024-09-19,235,330-->
    - values in ascending [VOT](voice%20onset%20time.md)::[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive) <!--SR:!2024-06-04,232,284-->
- [vowel](vowel.md):::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2024-02-21,79,352!2024-10-05,248,330-->
- [vowel backness](vowel.md#backness):::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md) <!--SR:!2024-10-03,327,304!2025-08-03,556,357-->
    - values in ascending [vowel backness](vowel.md#backness)::[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md) <!--SR:!2024-12-02,387,324-->
  - [vowel height](vowel.md#height):::vertical position of the [tongue](tongue.md) <!--SR:!2024-03-08,168,338!2024-02-14,72,351-->
    - values in descending [vowel height](vowel.md#height)::[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md)
- [vowel roundedness](roundedness.md):::rounding of the [lips](lip.md) <!--SR:!2024-11-14,369,313!2025-07-04,536,358-->
    - values in ascending [vowel roundedness](roundedness.md)::unrounded, compressed, protruded <!--SR:!2024-03-14,122,351-->

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]:::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md) <!--SR:!2024-03-07,167,264!2024-06-19,208,317-->
- (principal) /[slashes](slash%20(punctuation).md)/:::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only <!--SR:!2024-04-20,204,293-->
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals <!--SR:!2024-04-04,70,274!2000-01-01,1,250-->
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses)):::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md) <!--SR:!2024-03-12,120,253!2024-11-15,284,331-->
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses))):::transcription of obscured speech or description of obscuring sound <!--SR:!2024-07-05,238,284!2024-06-08,260,304-->
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]:::extra-precise transcription <!--SR:!2025-02-11,423,358!2025-01-10,398,361-->
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[morphophonemic](morphophonology.md) transcription <!--SR:!2024-02-09,28,261!2024-03-07,104,291-->
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫:::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves <!--SR:!2024-03-13,121,351!2024-02-27,85,351-->

### letters

Here is a list of common IPA letters and their pronunciations:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="958a"--><!-- The following content is generated at 2023-11-12T00:31:30.872283+08:00. Any edits will be overridden! -->

> | name | symbol | audio | description |
> |-|-|-|-|
> | [open front unrounded vowel](open%20front%20unrounded%20vowel.md) | \[a\] | ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _h**a**t_ \[hat\] |
> | [open central unrounded vowel](open%20central%20unrounded%20vowel.md) | \[ä\] | ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) | [English](English%20language.md) _br**a**_ \[bɹäː\] |
> | [near-open central vowel](near-open%20central%20vowel.md) | \[ɐ\] | ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) | [English](English%20language.md) _n**u**t_ \[nɐʔt\] |
> | [open back unrounded vowel](open%20back%20unrounded%20vowel.md) | \[ɑ\] | ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) | [English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\] |
> | [nasalized open back unrounded vowel](nasal%20vowel.md) | \[ɑ̃\] | ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) | [French](French%20language.md) _s**an**s_ [sɑ̃] "without" |
> | [open back rounded vowel](open%20back%20rounded%20vowel.md) | \[ɒ\] | ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) | [English](English%20language.md) _n**o**t_ \[nɒt\] |
> | [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) | \[ʌ\] | ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) | [English](English%20language.md) _g**u**t_ \[ɡʌt\] |
> | [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) | \[æ\] | ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _c**a**t_ \[kʰæt\] |
> | [voiced bilabial plosive](voiced%20bilabial%20plosive.md) | \[b\] | ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) | [English](English%20language.md) _a**b**ack_ \[əˈbæk\] |
> | [voiced bilabial implosive](voiced%20bilabial%20implosive.md) | \[ɓ\] | ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) | [English](English%20language.md) _**b**ody_ \[ɓʌdi\] |
> | [voiced bilabial fricative](voiced%20bilabial%20fricative.md) | \[β\] | ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) | [Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava" |
> | [voiced bilabial trill](voiced%20bilabial%20trill.md) | \[ʙ\] | ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) | [Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw" |
> | [voiceless palatal plosive](voiceless%20palatal%20plosive.md) | \[c\] | ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) | [French](French%20language.md) _**q**ui_ \[ci\] "who" |
> | [voiceless palatal fricative](voiceless%20palatal%20fricative.md) | \[ç\] | ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) | [English](English%20language.md) _**h**ue_ \[çʉː\] |
> | [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) | \[ɕ\] | ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) | [English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\] |
> | [voiced alveolar plosive](voiced%20alveolar%20plosive.md) | \[d\] | ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) | [English](English%20language.md) _**d**ash_ \[ˈdæʃ\] |
> | [voiced alveolar implosive](voiced%20alveolar%20implosive.md) | \[ɗ\] | ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) | [Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail" |
> | [voiced retroflex plosive](voiced%20retroflex%20plosive.md) | \[ɖ\] | ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga) | [Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north" |
> | [voiced dental fricative](voiced%20dental%20fricative.md) | \[ð\] | ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) | [English](English%20language.md) _**th**is_ \[ðɪs\] |
> | [voiced alveolar affricate](voiced%20alveolar%20affricate.md) | \[dz\] | ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga) | [English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\] |
> | [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) | \[dʒ\] | ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) | [English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\] |
> | [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) | \[dʑ\] | ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) | [Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound" |
> | [voiced retroflex affricate](voiced%20retroflex%20affricate.md) | \[dʐ\] | ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) | [Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam" |
> | [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) | \[e\] | ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _m**ay**_ \[meː\] |
> | [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) | \[ɘ\] | ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) | [English](English%20language.md) _b**ir**d_ \[bɘːd\] |
> | [mid central vowel](mid%20central%20vowel.md) | \[ə\] | ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) | [English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\] |
> | [r-colored mid central vowel](r-colored%20vowel.md) | \[ɚ\] | ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | [English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\] |
> | [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) | \[ɛ\] | ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _b**e**d_ \[bɛd\] |
> | [nasalized open-mid front unrounded vowel](nasal%20vowel.md) | \[ɛ̃\] | ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) | [French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand" |
> | [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) | \[ɜ\] | ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) | [English](English%20language.md) _b**ir**d_ \[bɜːd\] |
> | [r-colored open-mid central unrounded vowel](r-colored%20vowel.md) | \[ɝ\] | ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) | [English](English%20language.md) _b**ir**d_ \[bɝːd\] |
> | [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) | \[f\] | ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) | [English](English%20language.md) _**f**ill_ \[fɪɫ\] |
> | [voiced velar plosive](voiced%20velar%20plosive.md) | \[ɡ\] | ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) | [English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\] |
> | [voiced velar implosive](voiced%20velar%20implosive.md) | \[ɠ\] | ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) | [Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" |
> | [voiced uvular plosive](voiced%20uvular%20plosive.md) | \[ɢ\] | ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga) | [English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\] |
> | [voiceless glottal fricative](voiceless%20glottal%20fricative.md) | \[h\] | ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) | [English](English%20language.md) _**h**igh_ \[haɪ̯\] |
> | [voiced glottal fricative](voiced%20glottal%20fricative.md) | \[ɦ\] | ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) | [English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\] |
> | [aspirated consonant](aspirated%20consonant.md) | \[ʰ\] |  | [English](English%20langugae.md) _**t**op_ \[tʰɒp\] |
> | [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) | \[ħ\] | ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) | [English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\] |
> | [close front unrounded vowel](close%20front%20unrounded%20vowel.md) | \[i\] | ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _fr**ee**_ \[fɹiː\] |
> | [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) | \[ɪ\] | ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) | [English](English%20language.md) _b**i**t_ \[bɪʔt\] |
> | [close central unrounded vowel](close%20central%20unrounded%20vowel.md) | \[ɨ\] | ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) | [Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you" |
> | [voiced palatal approximant](voiced%20palatal%20approximant.md) | \[j\] | ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) | [English](English%20language.md) _**y**ou_ \[juː\] |
> | [palatalization](palatalization%20(phonetics).md) | \[ʲ\] |  | [Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive" |
> | [voiced palatal fricative](voiced%20palatal%20fricative.md) | \[ʝ\] | ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) | [Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock" |
> | [voiced palatal plosive](voiced%20palatal%20plosive.md) | \[ɟ\] | ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) | [Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)" |
> | [voiced palatal implosive](voiced%20palatal%20implosive.md) | \[ʄ\] | ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) | [Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday" |
> | [voiceless velar plosive](voiceless%20velar%20plosive.md) | \[k\] | ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) | [English](English%20language.md) _**k**iss_ \[kʰɪs\] |
> | [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) | \[l\] | ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) | [English](English%20language.md) _**l**et_ \[lɛt\] |
> | [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) | \[ɫ\] | ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) | [English](English%20language.md) _fee**l**_ \[fiːɫ\] |
> | [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) | \[ɬ\] | ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) | [Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle" |
> | [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) | \[ɭ\] | ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) | [French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg" |
> | [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) | \[ɺ\] |  | [Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six" |
> | [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) | \[ɮ\] | ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) | [Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat" |
> | [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) | \[ʟ\] | ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) | [English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\] |
> | [voiced bilabial nasal](voiced%20bilabial%20nasal.md) | \[m\] | ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) | [English](English%20language.md) _hi**m**_ \[hɪm\] |
> | [voiced labiodental nasal](voiced%20labiodental%20nasal.md) | \[ɱ\] | ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) | [English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\] |
> | [voiced alveolar nasal](voiced%20alveolar%20nasal.md) | \[n\] | ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) | [English](English%20language.md) _**n**ice_ \[naɪs\] |
> | [voiced velar nasal](voiced%20velar%20nasal.md) | \[ŋ\] | ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) | [English](English%20language.md) _si**ng**_ \[sɪŋ\] |
> | [voiced palatal nasal](voiced%20palatal%20nasal.md) | \[ɲ\] | ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) | [French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion" |
> | [voiced retroflex nasal](voiced%20retroflex%20nasal.md) | \[ɳ\] | ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) | [Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn" |
> | [voiced uvular nasal](voiced%20uvular%20nasal.md) | \[ɴ\] | ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) | [Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled" |
> | [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) | \[o\] | ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) | [English](English%20language.md) _y**aw**n_ \[joːn\] |
> | [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) | \[ɔ\] | ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) | [English](English%20language.md) _n**o**t_ \[nɔt\] |
> | [nasalized open-mid back rounded vowel](nasal%20vowel.md) | \[ɔ̃\] | ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) | [French](French%20language.md) _s**on**_ \[sɔ̃\] "sound" |
> | [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) | \[ø\] | ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) | [French](French%20language.md) _p**eu**_ \[pø\] "few" |
> | [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) | \[ɵ\] | ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) | [English](English%20language.md) _f**oo**t_ \[fɵʔt\] |
> | [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) | \[œ\] | ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) | [French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young" |
> | [nasalized open-mid front rounded vowel](nasal%20vowel.md) | \[œ̃\] | ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) | [French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown" |
> | [open front rounded vowel](open%20front%20rounded%20vowel.md) | \[ɶ\] | ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) | [Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green" |
> | [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) | \[p\] | ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) | [English](English%20language.md) _**p**ack_ \[pʰæk\] |
> | [voiceless uvular plosive](voiceless%20uvular%20plosive.md) | \[q\] | ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) | [Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat" |
> | [voiced alveolar trill](voiced%20alveolar%20trill.md) | \[r\] | ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) | [Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog" |
> | [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) | \[ɾ\] | ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) | [Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive" |
> | [voiced uvular trill](voiced%20uvular%20trill.md) | \[ʀ\] | ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) | [German](German%20language.md) _**r**ot_ \[ʀoːt\] "red" |
> | [voiced retroflex flap](voiced%20retroflex%20flap.md) | \[ɽ\] | ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) | [Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf" |
> | [voiced alveolar approximant](voiced%20alveolar%20approximant.md) | \[ɹ\] | ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) | [Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest" |
> | [voiced retroflex approximant](voiced%20retroflex%20approximant.md) | \[ɻ\] | ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga) | [Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat" |
> | [voiced uvular fricative](voiced%20uvular%20fricative.md) | \[ʁ\] | ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) | [French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay" |
> | [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) | \[s\] | ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) | [English](English%20language.md) _**s**it_ \[sɪt\] |
> | [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) | \[ʃ\] | ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) | [English](English%20language.md) _**sh**eep_ \[ˈʃiːp\] |
> | [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) | \[ʂ\] | ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) | [Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle" |
> | [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) | \[t\] | ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) | [English](English%20language.md) _**t**ick_ \[tʰɪk\] |
> | [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) | \[ʈ\] | ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga) | [Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card" |
> | [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) | \[ts\] | ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga) | [English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\] |
> | [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) | \[tʃ\] | ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) | [English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\] |
> | [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) | \[tɕ\] | ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) | [Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)" |
> | [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) | \[tʂ\] | ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) | [Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)" |
> | [close back rounded vowel](close%20back%20rounded%20vowel.md) | \[u\] | ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) | [English](English%20language.md) _b**oo**t_ \[bu̟ːt\] |
> | [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) | \[ʊ\] | ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) | [English](English%20language.md) _h**oo**k_ \[hʊʔk\] |
> | [close central rounded vowel](close%20central%20rounded%20vowel.md) | \[ʉ\] | ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) | [English](English%20language.md) _g**oo**se_ \[ɡʉːs\] |
> | [voiced labiodental fricative](voiced%20labiodental%20fricative.md) | \[v\] | ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) | [English](English%20language.md) _**v**al**v**e_ \[væɫv\] |
> | [voiced labiodental approximant](voiced%20labiodental%20approximant.md) | \[ʋ\] | ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) | [Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby" |
> | [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) | \[w\] | ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) | [English](English%20language.md) _**w**eep_ \[wiːp\] |
> | [labialization](labialization.md) | \[ʷ\] |  | [English](English%20language.md) _**r**eed_ \[ɹʷiːd\] |
> | [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) | \[ʍ\] | ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) | [English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\] |
> | [close back unrounded vowel](close%20back%20unrounded%20vowel.md) | \[ɯ\] | ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) | [Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow" |
> | [voiced velar approximant](voiced%20velar%20approximant.md) | \[ɰ\] | ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) | [Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine" |
> | [voiceless velar fricative](voiceless%20velar%20fricative.md) | \[x\] | ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) | [German](German%20language.md) _Bu**ch**_ \[buːx\] "book" |
> | [voiceless uvular fricative](voiceless%20uvular%20fricative.md) | \[χ\] | ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) | [French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very" |
> | [close front rounded vowel](close%20front%20rounded%20vowel.md) | \[y\] | ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) | [French](French%20language.md) _t**u**_ \[t̪y] "you" |
> | [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) | \[ʏ\] | ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) | [German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect" |
> | [voiced velar fricative](voiced%20velar%20fricative.md) | \[ɣ\] | ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) | [Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend" |
> | [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) | \[ɤ\] | ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) | [Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry" |
> | [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) | \[ʎ\] | ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) | [English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\] |
> | [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) | \[ɥ\] | ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) | [French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm" |
> | [voiced alveolar fricative](voiced%20alveolar%20fricative.md) | \[z\] | ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) | [English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\] |
> | [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) | \[ʒ\] | ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg) | [English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\] |
> | [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) | \[ʑ\] | ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg) | [Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire" |
> | [voiced retroflex fricative](voiced%20retroflex%20fricative.md) | \[ʐ\] | ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg) | [Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife" |
> | [voiceless dental fricative](voiceless%20dental%20fricative.md) | \[θ\] | ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) | [English](English%20language.md) _**th**in_ \[θɪn\] |
> | [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) | \[ɸ\] | ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) | [Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay" |
> | [glottal stop](glottal%20stop.md) | \[ʔ\] | ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg) | [English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\] |
> | [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) | \[ʕ\] | ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg) | [Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion" |
> | [tenuis dental click](tenuis%20dental%20click.md) | \[ǀ\] | ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) | [English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\] |
> | [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) | \[ǁ\] | ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) | [English](English%20language.md) _**tchick**_ \[ˈǁ\] |
> | [tenuis alveolar click](tenuis%20alveolar%20click.md) | \[ǃ\] | ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) | [Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat" |
> | [tenuis bilabial click](tenuis%20bilabial%20click.md) | \[ʘ\] | ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg) | [ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two" |
> | [tenuis palatal click](tenuis%20palatal%20click.md) | \[ǂ\] | ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) | [Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth" |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol (letters)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="059f"--><!-- The following content is generated at 2024-01-04T20:18:01.221392+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::\[a\] <!--SR:!2025-06-21,525,358-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::\[ä\] <!--SR:!2025-07-06,537,357-->
- [near-open central vowel](near-open%20central%20vowel.md)::\[ɐ\] <!--SR:!2024-02-22,104,351-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::\[ɑ\] <!--SR:!2025-01-22,407,361-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::\[ɑ̃\] <!--SR:!2025-07-12,543,361-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::\[ɒ\] <!--SR:!2025-02-07,420,358-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::\[ʌ\] <!--SR:!2025-01-27,411,360-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::\[æ\] <!--SR:!2025-08-28,581,361-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::\[b\] <!--SR:!2025-09-09,590,361-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::\[ɓ\] <!--SR:!2024-06-25,158,321-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::\[β\] <!--SR:!2024-03-16,59,318-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::\[ʙ\] <!--SR:!2025-08-03,556,360-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::\[c\] <!--SR:!2024-04-25,133,332-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::\[ç\] <!--SR:!2024-02-18,13,291-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::\[ɕ\] <!--SR:!2024-03-05,113,351-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::\[d\] <!--SR:!2025-01-02,339,331-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::\[ɗ\] <!--SR:!2024-02-25,82,353-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::\[ɖ\] <!--SR:!2025-01-27,412,361-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::\[ð\] <!--SR:!2024-03-29,139,317-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::\[dz\] <!--SR:!2025-01-06,347,372-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::\[dʒ\] <!--SR:!2024-08-08,208,331-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::\[dʑ\] <!--SR:!2024-02-08,64,333-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::\[dʐ\] <!--SR:!2024-02-11,37,334-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::\[e\] <!--SR:!2024-02-26,143,317-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::\[ɘ\] <!--SR:!2024-10-09,310,337-->
- [mid central vowel](mid%20central%20vowel.md)::\[ə\] <!--SR:!2024-03-20,131,351-->
- [r-colored mid central vowel](r-colored%20vowel.md)::\[ɚ\] <!--SR:!2025-03-14,405,372-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::\[ɛ\] <!--SR:!2025-03-26,415,372-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::\[ɛ̃\] <!--SR:!2024-05-20,116,301-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::\[ɜ\] <!--SR:!2024-03-03,113,351-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::\[ɝ\] <!--SR:!2024-10-20,282,351-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::\[f\] <!--SR:!2024-02-14,72,352-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::\[ɡ\] <!--SR:!2024-02-15,42,293-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::\[ɠ\] <!--SR:!2024-12-21,381,358-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::\[ɢ\] <!--SR:!2024-05-26,156,291-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::\[h\] <!--SR:!2024-03-21,131,351-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::\[ɦ\] <!--SR:!2025-05-31,505,357-->
- [aspirated consonant](aspirated%20consonant.md)::\[ʰ\] <!--SR:!2024-03-02,81,292-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::\[ħ\] <!--SR:!2024-05-18,142,311-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::\[i\] <!--SR:!2024-04-05,84,251-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::\[ɪ\] <!--SR:!2024-02-13,71,353-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::\[ɨ\] <!--SR:!2024-12-28,338,372-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::\[j\] <!--SR:!2024-11-04,292,331-->
- [palatalization](palatalization%20(phonetics).md)::\[ʲ\] <!--SR:!2025-07-18,548,361-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::\[ʝ\] <!--SR:!2024-04-17,155,261-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::\[ɟ\] <!--SR:!2024-09-06,287,341-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::\[ʄ\] <!--SR:!2024-08-21,232,351-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::\[k\] <!--SR:!2024-06-05,184,319-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::\[l\] <!--SR:!2024-06-23,139,334-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::\[ɫ\] <!--SR:!2024-02-22,104,351-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::\[ɬ\] <!--SR:!2024-03-17,45,331-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::\[ɭ\] <!--SR:!2024-03-25,85,354-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)::\[ɺ\] <!--SR:!2024-02-11,127,320-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::\[ɮ\] <!--SR:!2024-02-26,60,334-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::\[ʟ\] <!--SR:!2024-02-18,68,333-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::\[m\] <!--SR:!2024-02-27,59,231-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::\[ɱ\] <!--SR:!2024-03-07,118,351-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::\[n\] <!--SR:!2024-05-01,159,311-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::\[ŋ\] <!--SR:!2025-03-16,416,339-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::\[ɲ\] <!--SR:!2024-06-05,121,314-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::\[ɳ\] <!--SR:!2024-08-20,281,339-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::\[ɴ\] <!--SR:!2024-05-24,171,308-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::\[o\] <!--SR:!2024-07-04,195,351-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::\[ɔ\] <!--SR:!2024-03-28,86,354-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::\[ɔ̃\] <!--SR:!2025-02-04,417,357-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::\[ø\] <!--SR:!2024-05-28,199,317-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::\[ɵ\] <!--SR:!2024-03-09,71,354-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::\[œ\] <!--SR:!2024-04-09,70,293-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::\[œ̃\] <!--SR:!2024-02-08,125,301-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::\[ɶ\] <!--SR:!2024-06-12,201,331-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::\[p\] <!--SR:!2024-03-01,68,231-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::\[q\] <!--SR:!2024-02-27,20,191-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::\[r\] <!--SR:!2024-06-06,167,331-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::\[ɾ\] <!--SR:!2024-02-22,104,351-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::\[ʀ\] <!--SR:!2025-08-07,560,360-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::\[ɽ\] <!--SR:!2024-12-09,342,300-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::\[ɹ\] <!--SR:!2024-02-21,78,291-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::\[ɻ\] <!--SR:!2024-08-24,221,331-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::\[ʁ\] <!--SR:!2024-02-12,70,353-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::\[s\] <!--SR:!2025-08-09,562,361-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::\[ʃ\] <!--SR:!2024-03-21,75,291-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::\[ʂ\] <!--SR:!2024-03-06,66,334-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::\[t\] <!--SR:!2025-01-04,393,361-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::\[ʈ\] <!--SR:!2024-02-29,58,293-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::\[ts\]
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::\[tʃ\]
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::\[tɕ\]
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::\[tʂ\]
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::\[u\]
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::\[ʊ\]
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::\[ʉ\]
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::\[v\]
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::\[ʋ\]
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::\[w\]
- [labialization](labialization.md)::\[ʷ\]
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::\[ʍ\]
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::\[ɯ\]
- [voiced velar approximant](voiced%20velar%20approximant.md)::\[ɰ\]
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::\[x\]
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::\[χ\]
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::\[y\]
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::\[ʏ\]
- [voiced velar fricative](voiced%20velar%20fricative.md)::\[ɣ\]
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::\[ɤ\]
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::\[ʎ\]
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::\[ɥ\]
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::\[z\]
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::\[ʒ\]
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::\[ʑ\]
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::\[ʐ\]
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::\[θ\]
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::\[ɸ\]
- [glottal stop](glottal%20stop.md)::\[ʔ\]
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::\[ʕ\]
- [tenuis dental click](tenuis%20dental%20click.md)::\[ǀ\]
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::\[ǁ\]
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::\[ǃ\]
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::\[ʘ\]
- [tenuis palatal click](tenuis%20palatal%20click.md)::\[ǂ\]

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d92e"--><!-- The following content is generated at 2024-01-04T20:18:00.795972+08:00. Any edits will be overridden! -->

- \[a\]::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2024-12-26,385,358-->
- \[ä\]::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2024-08-27,215,353-->
- \[ɐ\]::[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!2024-03-07,118,351-->
- \[ɑ\]::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2024-06-24,227,337-->
- \[ɑ̃\]::[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2024-09-17,284,339-->
- \[ɒ\]::[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2024-03-18,66,272-->
- \[ʌ\]::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2024-02-14,12,234-->
- \[æ\]::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!2025-03-03,403,337-->
- \[b\]::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2025-08-14,567,358-->
- \[ɓ\]::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2025-02-24,390,371-->
- \[β\]::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2024-03-23,133,351-->
- \[ʙ\]::[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2024-10-13,274,331-->
- \[c\]::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2024-07-05,237,321-->
- \[ç\]::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2024-02-19,98,291-->
- \[ɕ\]::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2024-02-10,68,353-->
- \[d\]::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2025-01-16,357,372-->
- \[ɗ\]::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2024-11-02,291,351-->
- \[ɖ\]::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2024-10-18,318,341-->
- \[ð\]::[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2024-03-21,131,351-->
- \[dz\]::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2024-03-13,74,354-->
- \[dʒ\]::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2024-05-17,188,297-->
- \[dʑ\]::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2024-07-27,210,331-->
- \[dʐ\]::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2024-03-16,77,354-->
- \[e\]::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-03-10,72,354-->
- \[ɘ\]::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!2025-08-12,565,357-->
- \[ə\]::[mid central vowel](mid%20central%20vowel.md) <!--SR:!2024-04-17,158,321-->
- \[ɚ\]::[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2024-03-04,30,312-->
- \[ɛ\]::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-09-05,286,341-->
- \[ɛ̃\]::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2024-03-11,122,351-->
- \[ɜ\]::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-09-04,211,332-->
- \[ɝ\]::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2024-03-12,122,351-->
- \[f\]::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2024-02-28,109,298-->
- \[ɡ\]::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2025-07-22,551,360-->
- \[ɠ\]::[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2024-02-23,102,331-->
- \[ɢ\]::[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2025-06-05,510,357-->
- \[h\]::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2024-03-15,126,348-->
- \[ɦ\]::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2025-06-14,519,357-->
- \[ʰ\]::[aspirated consonant](aspirated%20consonant.md) <!--SR:!2024-08-03,213,311-->
- \[ħ\]::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2025-09-09,590,361-->
- \[i\]::[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!2024-02-23,42,334-->
- \[ɪ\]::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2024-03-22,82,354-->
- \[ɨ\]::[close central unrounded vowel](close%20central%20unrounded%20vowel.md) <!--SR:!2024-02-17,66,271-->
- \[j\]::[voiced palatal approximant](voiced%20palatal%20approximant.md) <!--SR:!2024-10-22,284,351-->
- \[ʲ\]::[palatalization](palatalization%20(phonetics).md) <!--SR:!2024-10-05,271,351-->
- \[ʝ\]::[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!2024-11-01,331,341-->
- \[ɟ\]::[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2024-06-09,208,317-->
- \[ʄ\]::[voiced palatal implosive](voiced%20palatal%20implosive.md) <!--SR:!2024-02-26,29,211-->
- \[k\]::[voiceless velar plosive](voiceless%20velar%20plosive.md) <!--SR:!2024-02-28,54,272-->
- \[l\]::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) <!--SR:!2024-02-10,54,231-->
- \[ɫ\]::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) <!--SR:!2024-02-17,75,271-->
- \[ɬ\]::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2024-03-02,36,331-->
- \[ɭ\]::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!2024-02-13,32,311-->
- \[ɺ\]::[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) <!--SR:!2024-03-18,59,320-->
- \[ɮ\]::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!2024-06-29,218,301-->
- \[ʟ\]::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!2024-05-22,193,317-->
- \[m\]::[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2024-02-17,75,353-->
- \[ɱ\]::[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2024-03-10,53,294-->
- \[n\]::[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!2024-06-19,159,333-->
- \[ŋ\]::[voiced velar nasal](voiced%20velar%20nasal.md) <!--SR:!2024-02-11,45,314-->
- \[ɲ\]::[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2024-02-16,74,353-->
- \[ɳ\]::[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2024-05-01,136,311-->
- \[ɴ\]::[voiced uvular nasal](voiced%20uvular%20nasal.md) <!--SR:!2024-03-25,85,354-->
- \[o\]::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) <!--SR:!2025-07-13,542,357-->
- \[ɔ\]::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) <!--SR:!2024-04-11,139,311-->
- \[ɔ̃\]::[nasalized open-mid back rounded vowel](nasal%20vowel.md) <!--SR:!2024-02-14,52,272-->
- \[ø\]::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) <!--SR:!2024-08-30,238,331-->
- \[ɵ\]::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2024-06-16,195,321-->
- \[œ\]::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) <!--SR:!2024-02-23,57,293-->
- \[œ̃\]::[nasalized open-mid front rounded vowel](nasal%20vowel.md) <!--SR:!2025-08-23,576,358-->
- \[ɶ\]::[open front rounded vowel](open%20front%20rounded%20vowel.md) <!--SR:!2024-08-12,231,331-->
- \[p\]::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2024-10-30,287,331-->
- \[q\]::[voiceless uvular plosive](voiceless%20uvular%20plosive.md) <!--SR:!2024-02-08,25,311-->
- \[r\]::[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2024-09-05,245,351-->
- \[ɾ\]::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2024-08-08,209,352-->
- \[ʀ\]::[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2024-03-24,53,294-->
- \[ɽ\]::[voiced retroflex flap](voiced%20retroflex%20flap.md) <!--SR:!2024-02-14,72,351-->
- \[ɹ\]::[voiced alveolar approximant](voiced%20alveolar%20approximant.md) <!--SR:!2024-08-28,265,320-->
- \[ɻ\]::[voiced retroflex approximant](voiced%20retroflex%20approximant.md) <!--SR:!2025-01-06,370,300-->
- \[ʁ\]::[voiced uvular fricative](voiced%20uvular%20fricative.md) <!--SR:!2024-03-05,68,354-->
- \[s\]::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2024-03-22,130,297-->
- \[ʃ\]::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) <!--SR:!2024-03-05,145,321-->
- \[ʂ\]::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2024-11-16,348,340-->
- \[t\]::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!2024-02-28,59,334-->
- \[ʈ\]::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!2024-02-21,53,334-->
- \[ts\]::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) <!--SR:!2025-02-08,390,340-->
- \[tʃ\]::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) <!--SR:!2024-06-14,168,271-->
- \[tɕ\]::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) <!--SR:!2024-02-28,41,274-->
- \[tʂ\]::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!2024-02-14,51,334-->
- \[u\]::[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2024-04-14,115,291-->
- \[ʊ\]::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) <!--SR:!2024-03-14,75,354-->
- \[ʉ\]::[close central rounded vowel](close%20central%20rounded%20vowel.md) <!--SR:!2024-07-26,172,279-->
- \[v\]::[voiced labiodental fricative](voiced%20labiodental%20fricative.md) <!--SR:!2025-02-23,389,371-->
- \[ʋ\]::[voiced labiodental approximant](voiced%20labiodental%20approximant.md) <!--SR:!2024-03-20,131,351-->
- \[w\]::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2024-02-13,71,353-->
- \[ʷ\]::[labialization](labialization.md) <!--SR:!2024-02-27,109,351-->
- \[ʍ\]::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) <!--SR:!2024-02-21,19,314-->
- \[ɯ\]::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2024-02-29,35,233-->
- \[ɰ\]::[voiced velar approximant](voiced%20velar%20approximant.md) <!--SR:!2024-03-25,92,311-->
- \[x\]::[voiceless velar fricative](voiceless%20velar%20fricative.md) <!--SR:!2024-05-15,124,320-->
- \[χ\]::[voiceless uvular fricative](voiceless%20uvular%20fricative.md) <!--SR:!2024-05-07,155,260-->
- \[y\]::[close front rounded vowel](close%20front%20rounded%20vowel.md)
- \[ʏ\]::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- \[ɣ\]::[voiced velar fricative](voiced%20velar%20fricative.md)
- \[ɤ\]::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- \[ʎ\]::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- \[ɥ\]::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
- \[z\]::[voiced alveolar fricative](voiced%20alveolar%20fricative.md)
- \[ʒ\]::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
- \[ʑ\]::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)
- \[ʐ\]::[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
- \[θ\]::[voiceless dental fricative](voiceless%20dental%20fricative.md)
- \[ɸ\]::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
- \[ʔ\]::[glottal stop](glottal%20stop.md)
- \[ʕ\]::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- \[ǀ\]::[tenuis dental click](tenuis%20dental%20click.md)
- \[ǁ\]::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)
- \[ǃ\]::[tenuis alveolar click](tenuis%20alveolar%20click.md)
- \[ʘ\]::[tenuis bilabial click](tenuis%20bilabial%20click.md)
- \[ǂ\]::[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–audio (letters)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5dfb"--><!-- The following content is generated at 2024-01-04T20:18:01.183869+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg) <!--SR:!2024-03-17,127,351-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) <!--SR:!2024-05-02,222,284-->
- [near-open central vowel](near-open%20central%20vowel.md)::![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) <!--SR:!2024-09-09,279,264-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) <!--SR:!2024-08-03,301,313-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) <!--SR:!2024-04-08,145,311-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) <!--SR:!2024-12-17,403,324-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) <!--SR:!2024-05-28,231,293-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) <!--SR:!2025-10-04,617,358-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) <!--SR:!2025-10-29,637,358-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) <!--SR:!2024-10-20,309,341-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) <!--SR:!2025-07-19,547,357-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) <!--SR:!2024-04-21,160,321-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) <!--SR:!2024-03-21,95,291-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) <!--SR:!2024-02-16,95,291-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) <!--SR:!2024-11-18,371,318-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) <!--SR:!2024-09-07,268,351-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) <!--SR:!2024-11-16,369,324-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga) <!--SR:!2024-03-26,84,354-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) <!--SR:!2024-09-09,256,278-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga) <!--SR:!2024-10-19,259,238-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) <!--SR:!2024-03-25,104,278-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) <!--SR:!2024-06-11,150,313-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) <!--SR:!2024-04-26,203,284-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2024-06-27,206,331-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2024-03-21,48,231-->
- [mid central vowel](mid%20central%20vowel.md)::![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) <!--SR:!2024-03-30,104,292-->
- [r-colored mid central vowel](r-colored%20vowel.md)::![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2024-04-27,168,298-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2024-12-20,321,278-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) <!--SR:!2024-08-05,188,332-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2024-03-19,127,351-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2024-02-11,49,334-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) <!--SR:!2024-08-28,289,338-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) <!--SR:!2024-04-04,141,311-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) <!--SR:!2024-04-27,145,311-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga) <!--SR:!2026-02-14,761,353-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) <!--SR:!2024-07-08,227,278-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) <!--SR:!2024-05-14,116,314-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) <!--SR:!2024-02-18,55,334-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) <!--SR:!2024-10-17,305,264-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) <!--SR:!2024-02-29,63,334-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) <!--SR:!2024-08-13,213,331-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) <!--SR:!2024-03-11,73,354-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) <!--SR:!2024-06-23,202,278-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) <!--SR:!2024-03-07,115,297-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) <!--SR:!2024-03-25,136,204-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) <!--SR:!2024-05-24,140,333-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) <!--SR:!2024-03-16,127,278-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) <!--SR:!2024-03-13,117,288-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) <!--SR:!2024-11-18,345,341-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) <!--SR:!2024-02-13,71,351-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) <!--SR:!2024-02-19,77,351-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) <!--SR:!2024-02-14,72,351-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) <!--SR:!2024-08-11,211,238-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) <!--SR:!2024-03-31,183,273-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) <!--SR:!2024-05-18,189,318-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) <!--SR:!2024-03-25,68,312-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) <!--SR:!2024-03-20,66,294-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) <!--SR:!2024-03-28,134,260-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) <!--SR:!2024-03-16,38,170-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) <!--SR:!2024-09-22,229,271-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) <!--SR:!2024-04-16,157,298-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) <!--SR:!2024-07-27,260,293-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) <!--SR:!2024-03-22,98,291-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) <!--SR:!2024-03-21,161,298-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) <!--SR:!2024-09-05,300,304-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) <!--SR:!2024-02-12,70,353-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) <!--SR:!2024-04-28,136,311-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) <!--SR:!2024-02-08,90,253-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) <!--SR:!2024-11-12,292,331-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) <!--SR:!2025-05-01,456,284-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) <!--SR:!2024-04-25,143,238-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) <!--SR:!2025-01-22,360,298-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) <!--SR:!2024-03-12,89,291-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) <!--SR:!2024-03-11,90,292-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga) <!--SR:!2024-08-22,229,311-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) <!--SR:!2024-03-30,138,278-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) <!--SR:!2024-10-22,282,352-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) <!--SR:!2024-04-21,139,311-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) <!--SR:!2024-08-24,263,278-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) <!--SR:!2024-03-09,161,293-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga) <!--SR:!2025-02-08,369,331-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga) <!--SR:!2024-06-25,228,320-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) <!--SR:!2024-03-27,85,354-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) <!--SR:!2024-04-23,132,311-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) <!--SR:!2025-02-03,375,278-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) <!--SR:!2024-02-22,80,351-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) <!--SR:!2024-03-23,99,312-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) <!--SR:!2024-03-05,68,354-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) <!--SR:!2024-04-07,117,312-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) <!--SR:!2024-05-01,94,193-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) <!--SR:!2024-04-25,229,304-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) <!--SR:!2024-03-04,67,354-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) <!--SR:!2024-02-19,77,353-->
- [voiced velar approximant](voiced%20velar%20approximant.md)::![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) <!--SR:!2025-03-09,415,317-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) <!--SR:!2024-05-14,234,293-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) <!--SR:!2024-08-21,284,318-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) <!--SR:!2024-08-30,236,331-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) <!--SR:!2024-10-19,288,244-->
- [voiced velar fricative](voiced%20velar%20fricative.md)::![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) <!--SR:!2024-09-14,295,340-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) <!--SR:!2025-02-11,393,341-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) <!--SR:!2024-08-12,223,331-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)
- [glottal stop](glottal%20stop.md)::![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)
- [tenuis dental click](tenuis%20dental%20click.md)::![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)
- [tenuis palatal click](tenuis%20palatal%20click.md)::![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f9aa"--><!-- The following content is generated at 2024-01-04T20:18:00.975532+08:00. Any edits will be overridden! -->

- ![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2024-02-14,60,173-->
- ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2024-03-21,69,251-->
- ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)::[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!2024-02-09,12,194-->
- ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2024-02-08,3,150-->
- ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)::[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2024-03-24,177,273-->
- ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)::[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2024-07-04,157,292-->
- ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2024-07-12,169,239-->
- ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!2024-02-23,71,213-->
- ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2024-03-21,53,251-->
- ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2024-05-08,177,298-->
- ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2024-03-22,57,271-->
- ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)::[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2024-03-12,39,211-->
- ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2024-02-08,3,134-->
- ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2024-02-19,46,260-->
- ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2024-02-13,6,151-->
- ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2024-02-09,52,211-->
- ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2024-02-17,12,193-->
- ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2024-03-05,40,273-->
- ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)::[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2024-02-11,17,153-->
- ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2024-03-22,57,254-->
- ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2024-02-08,3,150-->
- ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2024-02-15,43,213-->
- ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2024-02-14,7,254-->
- ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-04-07,104,251-->
- ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-02-10,4,130-->
- ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)::[mid central vowel](mid%20central%20vowel.md) <!--SR:!2024-02-08,3,150-->
- ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2024-03-02,113,299-->
- ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-02-23,26,251-->
- ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2024-02-08,3,130-->
- ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-02-10,3,130-->
- ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2024-02-09,2,130-->
- ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2024-04-09,72,253-->
- ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2024-02-23,41,274-->
- ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)::[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2024-02-09,56,164-->
- ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)::[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2024-02-15,8,130-->
- ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2024-02-17,48,260-->
- ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2024-08-05,185,221-->
- ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2024-03-25,135,351-->
- ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)::[close front unrounded vowel](close%20front%20unrounded%20vowel.md)
- ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)
- ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)::[close central unrounded vowel](close%20central%20unrounded%20vowel.md)
- ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)::[voiced palatal approximant](voiced%20palatal%20approximant.md)
- ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)::[voiced palatal fricative](voiced%20palatal%20fricative.md)
- ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)::[voiced palatal plosive](voiced%20palatal%20plosive.md)
- ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)::[voiced palatal implosive](voiced%20palatal%20implosive.md)
- ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)::[voiceless velar plosive](voiceless%20velar%20plosive.md)
- ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)
- ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)
- ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)
- ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)
- ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)
- ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)
- ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)::[voiced bilabial nasal](voiced%20bilabial%20nasal.md)
- ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)::[voiced labiodental nasal](voiced%20labiodental%20nasal.md)
- ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)::[voiced alveolar nasal](voiced%20alveolar%20nasal.md)
- ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)::[voiced velar nasal](voiced%20velar%20nasal.md)
- ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)::[voiced palatal nasal](voiced%20palatal%20nasal.md)
- ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)::[voiced retroflex nasal](voiced%20retroflex%20nasal.md)
- ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)::[voiced uvular nasal](voiced%20uvular%20nasal.md)
- ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
- ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)
- ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)::[nasalized open-mid back rounded vowel](nasal%20vowel.md)
- ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
- ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)
- ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
- ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)::[nasalized open-mid front rounded vowel](nasal%20vowel.md)
- ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)::[open front rounded vowel](open%20front%20rounded%20vowel.md)
- ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)
- ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)::[voiceless uvular plosive](voiceless%20uvular%20plosive.md)
- ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)::[voiced alveolar trill](voiced%20alveolar%20trill.md)
- ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)
- ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)::[voiced uvular trill](voiced%20uvular%20trill.md)
- ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)::[voiced retroflex flap](voiced%20retroflex%20flap.md)
- ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)::[voiced alveolar approximant](voiced%20alveolar%20approximant.md)
- ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)::[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
- ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)::[voiced uvular fricative](voiced%20uvular%20fricative.md)
- ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)
- ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)
- ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)
- ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)
- ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)
- ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)
- ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
- ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)
- ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)
- ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)::[close back rounded vowel](close%20back%20rounded%20vowel.md)
- ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
- ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)::[close central rounded vowel](close%20central%20rounded%20vowel.md)
- ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)::[voiced labiodental fricative](voiced%20labiodental%20fricative.md)
- ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)::[voiced labiodental approximant](voiced%20labiodental%20approximant.md)
- ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)
- ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
- ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)::[close back unrounded vowel](close%20back%20unrounded%20vowel.md)
- ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)::[voiced velar approximant](voiced%20velar%20approximant.md)
- ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)::[voiceless velar fricative](voiceless%20velar%20fricative.md)
- ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)::[voiceless uvular fricative](voiceless%20uvular%20fricative.md)
- ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)::[close front rounded vowel](close%20front%20rounded%20vowel.md)
- ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)::[voiced velar fricative](voiced%20velar%20fricative.md)
- ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
- ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)::[voiced alveolar fricative](voiced%20alveolar%20fricative.md)
- ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
- ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)
- ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)::[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
- ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)::[voiceless dental fricative](voiceless%20dental%20fricative.md)
- ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
- ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)::[glottal stop](glottal%20stop.md)
- ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)::[tenuis dental click](tenuis%20dental%20click.md)
- ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)
- ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)::[tenuis alveolar click](tenuis%20alveolar%20click.md)
- ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)::[tenuis bilabial click](tenuis%20bilabial%20click.md)
- ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)::[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–description (letters)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50b0"--><!-- The following content is generated at 2024-01-04T20:18:01.048113+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::[English](English%20language.md) _h**a**t_ \[hat\] <!--SR:!2024-08-11,310,310-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::[English](English%20language.md) _br**a**_ \[bɹäː\] <!--SR:!2024-02-24,27,210-->
- [near-open central vowel](near-open%20central%20vowel.md)::[English](English%20language.md) _n**u**t_ \[nɐʔt\] <!--SR:!2024-02-10,13,130-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\] <!--SR:!2024-02-26,21,170-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::[French](French%20language.md) _s**an**s_ [sɑ̃] "without" <!--SR:!2024-02-14,16,244-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::[English](English%20language.md) _n**o**t_ \[nɒt\] <!--SR:!2024-06-14,167,224-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::[English](English%20language.md) _g**u**t_ \[ɡʌt\] <!--SR:!2024-07-06,264,304-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::[English](English%20language.md) _c**a**t_ \[kʰæt\] <!--SR:!2024-02-10,132,224-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::[English](English%20language.md) _a**b**ack_ \[əˈbæk\] <!--SR:!2024-03-23,182,284-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::[English](English%20language.md) _**b**ody_ \[ɓʌdi\] <!--SR:!2024-04-23,82,264-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava" <!--SR:!2024-04-02,141,244-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw" <!--SR:!2024-02-13,59,244-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::[French](French%20language.md) _**q**ui_ \[ci\] "who" <!--SR:!2024-06-09,261,304-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::[English](English%20language.md) _**h**ue_ \[çʉː\] <!--SR:!2024-02-18,21,133-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\] <!--SR:!2024-02-13,6,130-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::[English](English%20language.md) _**d**ash_ \[ˈdæʃ\] <!--SR:!2024-04-07,191,273-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail" <!--SR:!2024-03-27,138,213-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north" <!--SR:!2024-02-15,31,193-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::[English](English%20language.md) _**th**is_ \[ðɪs\] <!--SR:!2024-02-18,60,233-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\] <!--SR:!2024-02-14,12,150-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\] <!--SR:!2024-03-31,92,258-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound" <!--SR:!2024-05-20,167,258-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam" <!--SR:!2024-03-02,30,238-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::[English](English%20language.md) _m**ay**_ \[meː\] <!--SR:!2024-02-11,6,158-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɘːd\] <!--SR:!2024-02-28,110,258-->
- [mid central vowel](mid%20central%20vowel.md)::[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\] <!--SR:!2024-02-27,106,238-->
- [r-colored mid central vowel](r-colored%20vowel.md)::[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\] <!--SR:!2024-03-17,159,298-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::[English](English%20language.md) _b**e**d_ \[bɛd\] <!--SR:!2024-02-26,23,258-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand" <!--SR:!2024-03-22,162,298-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɜːd\] <!--SR:!2024-03-24,135,278-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɝːd\] <!--SR:!2024-03-17,127,317-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::[English](English%20language.md) _**f**ill_ \[fɪɫ\] <!--SR:!2024-02-24,27,257-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\] <!--SR:!2024-03-01,112,257-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!2024-02-10,22,197-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\] <!--SR:!2024-08-17,232,277-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::[English](English%20language.md) _**h**igh_ \[haɪ̯\] <!--SR:!2024-02-27,84,297-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\] <!--SR:!2024-02-29,23,237-->
- [aspirated consonant](aspirated%20consonant.md)::[English](English%20langugae.md) _**t**op_ \[tʰɒp\] <!--SR:!2025-06-09,514,357-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\] <!--SR:!2024-10-21,270,277-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::[English](English%20language.md) _fr**ee**_ \[fɹiː\] <!--SR:!2024-03-19,125,237-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::[English](English%20language.md) _b**i**t_ \[bɪʔt\] <!--SR:!2024-02-22,17,217-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you" <!--SR:!2024-02-27,51,218-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::[English](English%20language.md) _**y**ou_ \[juː\] <!--SR:!2024-04-20,92,278-->
- [palatalization](palatalization%20(phonetics).md)::[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive" <!--SR:!2024-06-16,204,258-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock" <!--SR:!2024-02-16,19,150-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)" <!--SR:!2024-02-23,25,150-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday" <!--SR:!2024-03-05,115,238-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::[English](English%20language.md) _**k**iss_ \[kʰɪs\] <!--SR:!2024-02-17,23,259-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::[English](English%20language.md) _**l**et_ \[lɛt\] <!--SR:!2024-02-19,101,300-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::[English](English%20language.md) _fee**l**_ \[fiːɫ\] <!--SR:!2024-04-09,88,240-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle" <!--SR:!2024-03-02,37,180-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg" <!--SR:!2024-03-03,37,200-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)::[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six" <!--SR:!2024-02-16,19,240-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat" <!--SR:!2024-02-11,6,130-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\] <!--SR:!2024-02-19,34,221-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::[English](English%20language.md) _hi**m**_ \[hɪm\] <!--SR:!2024-07-29,193,281-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\] <!--SR:!2024-11-13,306,301-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::[English](English%20language.md) _**n**ice_ \[naɪs\] <!--SR:!2024-03-11,43,261-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::[English](English%20language.md) _si**ng**_ \[sɪŋ\] <!--SR:!2024-04-03,58,281-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion" <!--SR:!2024-03-17,127,261-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn" <!--SR:!2024-02-21,15,181-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled" <!--SR:!2024-02-24,21,201-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::[English](English%20language.md) _y**aw**n_ \[joːn\] <!--SR:!2024-02-28,31,170-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::[English](English%20language.md) _n**o**t_ \[nɔt\] <!--SR:!2024-02-23,29,251-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound" <!--SR:!2024-03-26,57,231-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::[French](French%20language.md) _p**eu**_ \[pø\] "few" <!--SR:!2024-02-18,24,190-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::[English](English%20language.md) _f**oo**t_ \[fɵʔt\] <!--SR:!2024-02-13,19,191-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young" <!--SR:!2024-02-09,4,151-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown" <!--SR:!2024-02-08,23,171-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green" <!--SR:!2024-02-11,30,171-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::[English](English%20language.md) _**p**ack_ \[pʰæk\] <!--SR:!2024-02-12,91,271-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat" <!--SR:!2024-03-18,42,251-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog" <!--SR:!2024-04-29,122,251-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive" <!--SR:!2024-02-28,34,231-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red" <!--SR:!2024-06-23,177,291-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf" <!--SR:!2024-02-20,15,170-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest" <!--SR:!2024-02-19,38,171-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat" <!--SR:!2024-02-20,17,251-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay" <!--SR:!2024-03-03,35,171-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::[English](English%20language.md) _**s**it_ \[sɪt\] <!--SR:!2024-02-11,92,331-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\] <!--SR:!2024-03-21,78,291-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle" <!--SR:!2024-02-18,11,191-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::[English](English%20language.md) _**t**ick_ \[tʰɪk\] <!--SR:!2024-03-13,80,271-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card" <!--SR:!2024-03-10,66,231-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\] <!--SR:!2024-02-25,41,251-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\] <!--SR:!2024-04-29,126,291-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)" <!--SR:!2024-02-11,16,171-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)" <!--SR:!2024-02-12,18,191-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::[English](English%20language.md) _b**oo**t_ \[bu̟ːt\] <!--SR:!2024-02-13,30,211-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::[English](English%20language.md) _h**oo**k_ \[hʊʔk\] <!--SR:!2024-02-10,7,132-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::[English](English%20language.md) _g**oo**se_ \[ɡʉːs\] <!--SR:!2024-02-18,32,212-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::[English](English%20language.md) _**v**al**v**e_ \[væɫv\] <!--SR:!2024-04-11,88,312-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby" <!--SR:!2024-03-21,65,272-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::[English](English%20language.md) _**w**eep_ \[wiːp\] <!--SR:!2024-03-08,60,272-->
- [labialization](labialization.md)::[English](English%20language.md) _**r**eed_ \[ɹʷiːd\] <!--SR:!2024-02-13,19,232-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\] <!--SR:!2024-02-21,24,272-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow" <!--SR:!2024-05-05,92,252-->
- [voiced velar approximant](voiced%20velar%20approximant.md)::[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine" <!--SR:!2024-02-09,7,152-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::[German](German%20language.md) _Bu**ch**_ \[buːx\] "book" <!--SR:!2024-02-23,37,190-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very" <!--SR:!2024-02-10,16,150-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::[French](French%20language.md) _t**u**_ \[t̪y] "you" <!--SR:!2024-04-02,62,210-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect" <!--SR:!2024-03-12,47,190-->
- [voiced velar fricative](voiced%20velar%20fricative.md)::[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend" <!--SR:!2024-02-15,40,210-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry" <!--SR:!2024-04-10,83,230-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\] <!--SR:!2024-02-09,38,230-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm" <!--SR:!2024-02-13,16,150-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\] <!--SR:!2024-02-11,4,230-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\] <!--SR:!2024-03-30,64,230-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire" <!--SR:!2024-02-15,21,170-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife" <!--SR:!2024-02-29,30,170-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::[English](English%20language.md) _**th**in_ \[θɪn\] <!--SR:!2024-03-31,58,250-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay" <!--SR:!2024-04-03,82,250-->
- [glottal stop](glottal%20stop.md)::[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\] <!--SR:!2024-03-03,73,270-->
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion" <!--SR:!2024-02-13,10,150-->
- [tenuis dental click](tenuis%20dental%20click.md)::[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\] <!--SR:!2024-05-10,118,290-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::[English](English%20language.md) _**tchick**_ \[ˈǁ\] <!--SR:!2024-02-29,72,290-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat" <!--SR:!2024-03-10,45,210-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two" <!--SR:!2024-03-19,54,210-->
- [tenuis palatal click](tenuis%20palatal%20click.md)::[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth" <!--SR:!2024-02-08,6,130-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485d"--><!-- The following content is generated at 2023-11-12T00:31:30.816306+08:00. Any edits will be overridden! -->

> | name | symbol | description |
> |-|-|-|
> | [nasalized](nasal%20vowel.md) | \[◌̃\] (e.g. [ã]) | [French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine" |
> | [centralized](central%20vowel.md) | \[◌̈\] (e.g. [ä]) | [Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go" |
> | [extra-short](extra-shortness.md) | \[◌̆\] (e.g. [ă]) | [English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\] |
> | [non-syllabic](diphthong.md) | \[◌̯\] (e.g. [a̯]) | [English](English%20language.md) _co**w**_ \[kʰaʊ̯\] |
> | [voiceless](voicelessness.md) | \[◌̥\] (e.g. [n̥]) | [English](English%20language.md) _**d**oe_ \[d̥oʊ̯\] |
> | [syllabic](syllabic%20consonant.md) | \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) | [English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\] |
> | [dental/alveolar](dental%20consonant.md) | \[◌̪\] (e.g. [d̪]) | [Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two" |
> | [aspirated](aspirated%20consonant.md) | \[◌ʰ\] (e.g. [kʰ]) | [English](English%20language.md) _**c**ome_ \[kʰɐm\] |
> | [ejective](ejective%20consonant.md) | \[◌’\] (e.g. [k’]) | [Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" |
> | [long](longness%20(phonetics).md) | \[◌ː\] (e.g. [aː]) | [English](English%20language.md) _shh!_ \[ʃː\] |
> | [half-long](half-longness%20(phonetics).md) | \[◌ˑ\] (e.g. [aˑ]) | [English](English%20language.md) _caught_ \[ˈkʰɔˑt\] |
> | [primary stress](stress%20(lingustics).md) | \[ˈ◌\] (e.g. [ˈa]) | [English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] |
> | [secondary stress](secondary%20stress.md) | \[ˌ◌\] (e.g. [ˌa]) | [English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] |
> | [syllable break](syllable.md) | \[.\] | [English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\] |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–symbol (diacritics)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ffa2"--><!-- The following content is generated at 2024-01-04T20:18:01.097852+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md)::\[◌̃\] (e.g. [ã]) <!--SR:!2024-03-20,129,351-->
- [centralized](central%20vowel.md)::\[◌̈\] (e.g. [ä]) <!--SR:!2024-03-28,86,354-->
- [extra-short](extra-shortness.md)::\[◌̆\] (e.g. [ă]) <!--SR:!2024-02-14,7,201-->
- [non-syllabic](diphthong.md)::\[◌̯\] (e.g. [a̯]) <!--SR:!2024-05-13,106,314-->
- [voiceless](voicelessness.md)::\[◌̥\] (e.g. [n̥]) <!--SR:!2024-04-29,95,294-->
- [syllabic](syllabic%20consonant.md)::\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) <!--SR:!2024-07-13,243,341-->
- [dental/alveolar](dental%20consonant.md)::\[◌̪\] (e.g. [d̪]) <!--SR:!2024-12-17,378,360-->
- [aspirated](aspirated%20consonant.md)::\[◌ʰ\] (e.g. [kʰ]) <!--SR:!2025-08-06,559,360-->
- [ejective](ejective%20consonant.md)::\[◌’\] (e.g. [k’]) <!--SR:!2024-03-01,86,353-->
- [long](longness%20(phonetics).md)::\[◌ː\] (e.g. [aː]) <!--SR:!2025-09-03,586,361-->
- [half-long](half-longness%20(phonetics).md)::\[◌ˑ\] (e.g. [aˑ]) <!--SR:!2024-03-16,77,354-->
- [primary stress](stress%20(lingustics).md)::\[ˈ◌\] (e.g. [ˈa]) <!--SR:!2024-02-23,81,352-->
- [secondary stress](secondary%20stress.md)::\[ˌ◌\] (e.g. [ˌa]) <!--SR:!2024-08-28,228,352-->
- [syllable break](syllable.md)::\[.\]

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="94fb"--><!-- The following content is generated at 2024-01-04T20:17:59.931857+08:00. Any edits will be overridden! -->

- \[◌̃\] (e.g. [ã])::[nasalized](nasal%20vowel.md) <!--SR:!2024-07-19,251,290-->
- \[◌̈\] (e.g. [ä])::[centralized](central%20vowel.md) <!--SR:!2025-01-04,421,318-->
- \[◌̆\] (e.g. [ă])::[extra-short](extra-shortness.md) <!--SR:!2024-05-27,135,264-->
- \[◌̯\] (e.g. [a̯])::[non-syllabic](diphthong.md) <!--SR:!2024-02-11,11,204-->
- \[◌̥\] (e.g. [n̥])::[voiceless](voicelessness.md) <!--SR:!2024-10-25,349,313-->
- \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])::[syllabic](syllabic%20consonant.md) <!--SR:!2024-08-30,231,298-->
- \[◌̪\] (e.g. [d̪])::[dental/alveolar](dental%20consonant.md) <!--SR:!2024-04-14,181,318-->
- \[◌ʰ\] (e.g. [kʰ])::[aspirated](aspirated%20consonant.md) <!--SR:!2024-03-13,172,338-->
- \[◌’\] (e.g. [k’])::[ejective](ejective%20consonant.md) <!--SR:!2024-08-19,282,318-->
- \[◌ː\] (e.g. [aː])::[long](longness%20(phonetics).md) <!--SR:!2025-08-10,563,357-->
- \[◌ˑ\] (e.g. [aˑ])::[half-long](half-longness%20(phonetics).md) <!--SR:!2024-02-11,29,291-->
- \[ˈ◌\] (e.g. [ˈa])::[primary stress](stress%20(lingustics).md) <!--SR:!2024-06-20,222,337-->
- \[ˌ◌\] (e.g. [ˌa])::[secondary stress](secondary%20stress.md) <!--SR:!2025-02-25,435,361-->
- \[.\]::[syllable break](syllable.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### name–description (diacritics)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50bd"--><!-- The following content is generated at 2024-01-04T20:18:01.248419+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md)::[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine" <!--SR:!2024-02-25,59,238-->
- [centralized](central%20vowel.md)::[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go" <!--SR:!2024-04-04,145,224-->
- [extra-short](extra-shortness.md)::[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\] <!--SR:!2024-06-17,133,244-->
- [non-syllabic](diphthong.md)::[English](English%20language.md) _co**w**_ \[kʰaʊ̯\] <!--SR:!2024-07-24,299,313-->
- [voiceless](voicelessness.md)::[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\] <!--SR:!2025-05-13,487,338-->
- [syllabic](syllabic%20consonant.md)::[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\] <!--SR:!2024-04-28,169,278-->
- [dental/alveolar](dental%20consonant.md)::[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two" <!--SR:!2024-02-27,51,278-->
- [aspirated](aspirated%20consonant.md)::[English](English%20language.md) _**c**ome_ \[kʰɐm\] <!--SR:!2025-10-16,627,358-->
- [ejective](ejective%20consonant.md)::[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!2024-03-24,72,197-->
- [long](longness%20(phonetics).md)::[English](English%20language.md) _shh!_ \[ʃː\] <!--SR:!2025-01-24,378,338-->
- [half-long](half-longness%20(phonetics).md)::[English](English%20language.md) _caught_ \[ˈkʰɔˑt\] <!--SR:!2024-05-22,180,279-->
- [primary stress](stress%20(lingustics).md)::[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2024-06-22,170,311-->
- [secondary stress](secondary%20stress.md)::[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2024-04-22,124,312-->
- [syllable break](syllable.md)::[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\] <!--SR:!2024-05-07,115,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
