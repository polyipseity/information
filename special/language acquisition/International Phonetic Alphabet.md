---
aliases:
  - IPA help
  - IPA usage
  - International Phonetic Alphabet help
  - International Phonetic Alphabet usage
tags:
  - flashcard/active/special/language_acquisition/International_Phonetic_Alphabet
  - language/in/English
---

# International Phonetic Alphabet

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

> ![official IPA chart](../../archives/Wikimedia%20Commons/IPA%20chart%202020.svg)
>
> official IPA chart

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - phonetic symbol pattern ::: notice that the symbol of each phonetic is somewhat related to its sound, and similarly-sounding phonetics usually have similar symbols <!--SR:!2024-12-08,268,354!2000-01-01,1,250-->

## help

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import NULL_LOCATION, Result
letters = (
  ('[open front unrounded vowel](open%20front%20unrounded%20vowel.md)', R'\[a\]', '![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg)', R'[English](English%20language.md) _h**a**t_ \[hat\]',),
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
  ('[voiced retroflex plosive](voiced%20retroflex%20plosive.md)', R'\[ɖ\]', '![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg)', R'[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"',),
  ('[voiced dental fricative](voiced%20dental%20fricative.md)', R'\[ð\]', '![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)', R'[English](English%20language.md) _**th**is_ \[ðɪs\]',),
  ('[voiced alveolar affricate](voiced%20alveolar%20affricate.md)', R'\[dz\]', '![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg)', R'[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]',),
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
  ('[voiced uvular plosive](voiced%20uvular%20plosive.md)', R'\[ɢ\]', '![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg)', R'[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]',),
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
  ('[voiced retroflex approximant](voiced%20retroflex%20approximant.md)', R'\[ɻ\]', '![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg)', R'[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"',),
  ('[voiced uvular fricative](voiced%20uvular%20fricative.md)', R'\[ʁ\]', '![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)', R'[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"',),
  ('[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)', R'\[s\]', '![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**s**it_ \[sɪt\]',),
  ('[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)', R'\[ʃ\]', '![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)', R'[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]',),
  ('[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)', R'\[ʂ\]', '![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)', R'[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"',),
  ('[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)', R'\[t\]', '![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)', R'[English](English%20language.md) _**t**ick_ \[tʰɪk\]',),
  ('[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)', R'\[ʈ\]', '![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg)', R'[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"',),
  ('[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)', R'\[ts\]', '![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg)', R'[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]',),
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
    __env__.cwf_sects("958a", None),
    ("name", "symbol", "audio", "description",),
    letters,
  ),
  memorize_map(
    __env__.cwf_sects(None, "059f", "d92e"),
    items_to_map(*(datum[:2] for datum in letters)),
  ),
  memorize_map(
    __env__.cwf_sects(None, "5dfb", "f9aa"),
    items_to_map(*((datum[0], datum[2]) for datum in letters if datum[2])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "50b0", None),
    items_to_map(*((datum[0], datum[3]) for datum in letters)),
  ),
  memorize_table(
    __env__.cwf_sects("485d", None),
    ("name", "symbol", "description",),
    diacritics,
  ),
  memorize_map(
    __env__.cwf_sects(None, "ffa2", "94fb"),
    items_to_map(*(datum[:2] for datum in diacritics)),
  ),
  memorize_map(
    __env__.cwf_sects(None, "50bd", None),
    items_to_map(*((datum[0], datum[2]) for datum in diacritics)),
  ),
))
```

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
> 18. {{sub-laminal/sub-apical ([tongue](tongue.md) underside)}} <!--SR:!2025-02-15,462,330!2025-09-02,623,338!2025-10-11,656,344!2025-01-07,424,324!2024-11-06,357,324!2027-03-02,922,324!2025-01-16,433,324!2025-10-21,564,293!2025-02-02,449,333!2025-05-23,353,253!2024-12-14,146,293!2025-12-19,715,353!2024-12-22,73,258!2024-12-06,122,297!2025-03-19,153,321!2025-01-20,197,230!2024-10-30,268,330!2026-09-05,732,330-->

- [consonant](consonant.md):::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2026-05-01,707,290!2025-02-21,467,330-->
  - [airstream mechanism](airstream%20mechanism.md):::how the moving [air](air.md) is thrusted <!--SR:!2028-10-05,1484,338!2025-06-18,561,343-->
    - (all) [pulmonic](pulmonic%20consonant.md) egressive:::[air](air.md) is exhaled from the [lungs](lung.md) <!--SR:!2024-12-21,406,333!2025-10-23,632,358-->
    - (16%) [glottalic](glottalic%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md) <!--SR:!2025-04-25,413,351!2024-10-28,90,290-->
    - (13%) [glottalic](glottalic%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md) <!--SR:!2025-08-05,524,371!2025-11-08,420,270-->
    - (<2%) lingual/[velaric](velar%20consonant.md) ingressive:::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md) <!--SR:!2026-03-04,638,331!2024-12-01,90,270-->
    - ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive:::[air](air.md) is inhaled into the [lungs](lung.md) <!--SR:!2025-01-14,428,333!2025-01-15,432,333-->
    - ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive:::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md) <!--SR:!2026-04-22,627,279!2025-01-18,403,361-->
  - [length](gemination.md):::how long the articulation of a [consonant](consonant.md) lasts <!--SR:!2026-07-09,776,318!2027-08-23,1068,350-->
    - values in ascending [length](gemination.md)::single/singleton, geminate, long geminate <!--SR:!2024-11-16,243,293-->
  - [manner of articulation](manner%20of%20articulation.md):::configuration and interaction of the [speech organs](speech%20organ.md) <!--SR:!2026-04-06,663,331!2027-11-28,1137,350-->
    - [affricate](affricate%20consonant.md):::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md) <!--SR:!2025-09-24,519,317!2024-11-16,282,330-->
    - [approximant](approximant%20consonant.md):::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md) <!--SR:!2026-02-01,715,313!2025-04-05,474,358-->
      - [lateral approximant](lateral%20consonant.md):::approximant with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2025-09-17,524,284!2024-12-14,399,324-->
      - [semivowel/glide/semiconsonant](semivowel.md):::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary <!--SR:!2025-07-28,445,312!2026-09-20,780,330-->
    - [flap/tap](tap%20and%20flap%20consonants.md):::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact <!--SR:!2026-05-04,677,298!2024-10-31,269,330-->
    - [fricative/spirant](fricative%20consonant.md):::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation <!--SR:!2025-11-29,429,224!2026-05-17,795,358-->
      - [lateral](lateral%20consonant.md):::fricative with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2024-11-18,291,352!2027-01-25,874,330-->
      - [sibilant](sibilant%20consonant.md):::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md) <!--SR:!2026-09-17,846,341!2025-06-25,461,351-->
    - [nasal](nasal%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow <!--SR:!2025-09-29,523,317!2025-01-27,347,372-->
    - [plosive/stop](plosive%20consonant.md):::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow <!--SR:!2028-05-07,1346,361!2025-08-29,544,371-->
    - [trill](trill%20consonant.md):::consonant produced by vibrations between the active articulator and the passive articulator <!--SR:!2027-08-28,1090,318!2025-07-12,543,361-->
  - [place of articulation](place%20of%20articulation.md):::location along the [vocal tract](vocal%20tract.md) producing the consonant <!--SR:!2026-09-24,896,324!2025-06-27,530,358-->
    - [alveolar](alveolar%20ridge.md):::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive) <!--SR:!2027-02-23,921,339!2028-01-28,1189,350-->
    - [aryepiglottal](pharyngeal%20consonant.md):::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active) <!--SR:!2026-11-04,958,353!2025-10-21,587,371-->
    - [coronal](coronal%20constant.md):::front of the [tongue](tongue.md) (active) <!--SR:!2026-12-19,939,313!2026-12-17,839,298-->
      - [apical](apical%20consonant.md):::tip of the [tongue](tongue.md) (active) <!--SR:!2024-12-17,403,324!2025-07-19,548,358-->
      - [laminal](laminal%20consonant.md):::blade of the [tongue](tongue.md), the upper front surface behind the tip (active) <!--SR:!2025-10-17,505,253!2026-01-25,474,240-->
      - [subapical](subapical%20consonant.md):::surface under the tip of the [tongue](tongue.md) (active) <!--SR:!2024-12-10,395,324!2025-10-28,674,353-->
    - [dental](dental%20consonant.md):::upper [teeth](tooth.md) (passive) <!--SR:!2027-04-06,963,313!2027-05-18,991,350-->
    - [dorsal](dorsal%20consonant.md):::body of the [tongue](tongue.md) (active) <!--SR:!2026-04-19,738,333!2025-04-04,497,333-->
    - [epiglottal](pharyngeal%20consonant.md):::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive) <!--SR:!2025-07-31,559,361!2025-04-07,425,372-->
    - [glottal](glottal%20consonant.md):::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active) <!--SR:!2026-04-16,764,313!2025-12-08,706,353-->
    - [labial](labial%20consonant.md):::lower [lip](lip.md) (active), upper [lip](lip.md) (passive) <!--SR:!2025-03-01,453,304!2025-09-10,637,353-->
    - [palatal](palatal%20consonant.md):::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2027-08-25,1041,304!2027-11-25,1141,350-->
    - [pharyngeal](pharyngeal%20consonant.md):::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive) <!--SR:!2027-04-15,952,298!2027-09-29,1084,351-->
    - [post-alveolar](post-alveolar%20consonant.md):::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive) <!--SR:!2025-08-17,570,357!2025-12-06,626,371-->
    - [uvular](uvular%20consonant.md):::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive) <!--SR:!2026-04-15,734,304!2025-01-06,347,372-->
    - [velar](velar%20consonant.md):::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2026-05-17,687,298!2025-06-24,527,357-->
  - [phonation](phonation.md):::how the [vocal cords](vocal%20folds.md) vibrate <!--SR:!2025-01-30,315,301!2025-06-25,529,361-->
    - [voiced](voice%20(phonetics).md):::the [vocal cords](vocal%20cords.md) vibrate fully <!--SR:!2025-07-15,589,344!2025-08-12,565,358-->
    - [voiceless](voicelessness.md):::the [vocal cords](vocal%20cords.md) do not vibrate <!--SR:!2025-08-05,609,353!2026-01-14,733,353-->
  - [voice onset time](voice%20onset%20time.md) (VOT):::timing of [phonation](phonation.md) <!--SR:!2024-11-22,375,333!2027-08-23,1068,350-->
    - values in ascending [VOT](voice%20onset%20time.md)::[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive) <!--SR:!2026-03-24,658,284-->
- [vowel](vowel.md):::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2025-03-08,381,372!2027-11-11,1127,350-->
  - [vowel backness](vowel.md#backness):::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md) <!--SR:!2028-07-17,1376,324!2025-08-03,556,357-->
    - values in ascending [vowel backness](vowel.md#backness)::[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md) <!--SR:!2024-12-02,387,324-->
  - [vowel height](vowel.md#height):::vertical position of the [tongue](tongue.md) <!--SR:!2026-04-28,781,358!2025-01-25,346,371-->
    - values in descending [vowel height](vowel.md#height)::[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md) <!--SR:!2026-05-16,575,336-->
  - [vowel roundedness](roundedness.md):::rounding of the [lips](lip.md) <!--SR:!2024-11-14,369,313!2025-07-04,536,358-->
    - values in ascending [vowel roundedness](roundedness.md)::unrounded, compressed, protruded <!--SR:!2025-05-15,427,351-->

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]:::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md) <!--SR:!2024-12-18,202,244!2026-12-16,910,337-->
- (principal) /[slashes](slash%20(punctuation).md)/:::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only <!--SR:!2025-12-09,597,293!2025-02-11,179,334-->
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals <!--SR:!2025-03-23,223,254!2025-08-24,372,316-->
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses)):::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md) <!--SR:!2025-07-22,307,233!2024-11-15,284,331-->
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses))):::transcription of obscured speech or description of obscuring sound <!--SR:!2026-05-11,675,284!2026-08-06,789,304-->
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]:::extra-precise transcription <!--SR:!2025-02-11,423,358!2025-01-10,398,361-->
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}:::[morphophonemic](morphophonology.md) transcription <!--SR:!2026-02-03,471,261!2025-01-03,302,291-->
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫:::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves <!--SR:!2025-10-17,583,371!2024-12-23,299,351-->

### letters

Here is a list of common IPA letters and their pronunciations:

<!--pytextgen generate section="958a"--><!-- The following content is generated at 2024-02-14T16:42:37.353397+08:00. Any edits will be overridden! -->

> | name | symbol | audio | description |
> |-|-|-|-|
> | [open front unrounded vowel](open%20front%20unrounded%20vowel.md) | \[a\] | ![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg) | [English](English%20language.md) _h**a**t_ \[hat\] |
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
> | [voiced retroflex plosive](voiced%20retroflex%20plosive.md) | \[ɖ\] | ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg) | [Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north" |
> | [voiced dental fricative](voiced%20dental%20fricative.md) | \[ð\] | ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) | [English](English%20language.md) _**th**is_ \[ðɪs\] |
> | [voiced alveolar affricate](voiced%20alveolar%20affricate.md) | \[dz\] | ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg) | [English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\] |
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
> | [voiced uvular plosive](voiced%20uvular%20plosive.md) | \[ɢ\] | ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg) | [English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\] |
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
> | [voiced retroflex approximant](voiced%20retroflex%20approximant.md) | \[ɻ\] | ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg) | [Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat" |
> | [voiced uvular fricative](voiced%20uvular%20fricative.md) | \[ʁ\] | ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) | [French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay" |
> | [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) | \[s\] | ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) | [English](English%20language.md) _**s**it_ \[sɪt\] |
> | [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) | \[ʃ\] | ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) | [English](English%20language.md) _**sh**eep_ \[ˈʃiːp\] |
> | [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) | \[ʂ\] | ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) | [Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle" |
> | [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) | \[t\] | ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) | [English](English%20language.md) _**t**ick_ \[tʰɪk\] |
> | [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) | \[ʈ\] | ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg) | [Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card" |
> | [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) | \[ts\] | ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg) | [English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\] |
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

<!--/pytextgen-->

#### name–symbol (letters)

<!--pytextgen generate section="059f"--><!-- The following content is generated at 2024-01-04T20:18:01.221392+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::\[a\] <!--SR:!2025-06-21,525,358-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::\[ä\] <!--SR:!2025-07-06,537,357-->
- [near-open central vowel](near-open%20central%20vowel.md)::\[ɐ\] <!--SR:!2025-07-06,500,371-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::\[ɑ\] <!--SR:!2025-01-22,407,361-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::\[ɑ̃\] <!--SR:!2025-07-12,543,361-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::\[ɒ\] <!--SR:!2025-02-07,420,358-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::\[ʌ\] <!--SR:!2025-01-27,411,360-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::\[æ\] <!--SR:!2025-08-28,581,361-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::\[b\] <!--SR:!2025-09-09,590,361-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::\[ɓ\] <!--SR:!2026-05-25,699,341-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::\[β\] <!--SR:!2024-12-01,258,338-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::\[ʙ\] <!--SR:!2025-08-03,556,360-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::\[c\] <!--SR:!2025-07-10,441,332-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::\[ç\] <!--SR:!2024-10-28,11,231-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::\[ɕ\] <!--SR:!2025-09-01,544,371-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::\[d\] <!--SR:!2025-01-02,339,331-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::\[ɗ\] <!--SR:!2025-03-31,397,373-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::\[ɖ\] <!--SR:!2025-01-27,412,361-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::\[ð\] <!--SR:!2025-06-25,440,317-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::\[dz\] <!--SR:!2025-01-06,347,372-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::\[dʒ\] <!--SR:!2026-06-26,687,331-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::\[dʑ\] <!--SR:!2024-11-27,293,353-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::\[dʐ\] <!--SR:!2026-03-19,597,354-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::\[e\] <!--SR:!2025-11-14,625,337-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::\[ɘ\] <!--SR:!2027-08-20,1044,337-->
- [mid central vowel](mid%20central%20vowel.md)::\[ə\] <!--SR:!2025-06-22,459,351-->
- [r-colored mid central vowel](r-colored%20vowel.md)::\[ɚ\] <!--SR:!2025-03-14,405,372-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::\[ɛ\] <!--SR:!2025-03-26,415,372-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::\[ɛ̃\] <!--SR:!2025-09-20,483,321-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::\[ɜ\] <!--SR:!2025-08-29,544,371-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::\[ɝ\] <!--SR:!2027-07-11,994,351-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::\[f\] <!--SR:!2025-01-28,349,372-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::\[ɡ\] <!--SR:!2026-01-28,540,313-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::\[ɠ\] <!--SR:!2024-12-21,381,358-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::\[ɢ\] <!--SR:!2026-02-15,630,311-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::\[h\] <!--SR:!2025-12-12,631,371-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::\[ɦ\] <!--SR:!2025-05-31,505,357-->
- [aspirated consonant](aspirated%20consonant.md)::\[ʰ\] <!--SR:!2025-01-25,328,312-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::\[ħ\] <!--SR:!2025-08-08,441,311-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::\[i\] <!--SR:!2025-01-31,295,271-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::\[ɪ\] <!--SR:!2025-01-21,343,373-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::\[ɨ\] <!--SR:!2024-12-28,338,372-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::\[j\] <!--SR:!2024-11-04,292,331-->
- [palatalization](palatalization%20(phonetics).md)::\[ʲ\] <!--SR:!2025-07-18,548,361-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::\[ʝ\] <!--SR:!2024-10-28,81,221-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::\[ɟ\] <!--SR:!2027-05-13,978,341-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::\[ʄ\] <!--SR:!2026-11-13,813,351-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::\[k\] <!--SR:!2026-08-24,810,339-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::\[l\] <!--SR:!2025-09-29,463,334-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::\[ɫ\] <!--SR:!2025-07-05,499,371-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::\[ɬ\] <!--SR:!2025-06-01,219,311-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::\[ɭ\] <!--SR:!2024-12-16,206,354-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)::\[ɺ\] <!--SR:!2026-05-07,564,300-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::\[ɮ\] <!--SR:!2024-11-29,275,354-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::\[ʟ\] <!--SR:!2026-01-12,445,293-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::\[m\] <!--SR:!2026-07-11,672,271-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::\[ɱ\] <!--SR:!2025-04-23,412,351-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::\[n\] <!--SR:!2026-03-15,683,331-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::\[ŋ\] <!--SR:!2025-03-16,416,339-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::\[ɲ\] <!--SR:!2025-06-19,379,314-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::\[ɳ\] <!--SR:!2027-03-30,952,339-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::\[ɴ\] <!--SR:!2026-05-23,728,328-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::\[o\] <!--SR:!2027-01-29,939,371-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::\[ɔ\] <!--SR:!2025-02-08,305,354-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::\[ɔ̃\] <!--SR:!2025-02-04,417,357-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::\[ø\] <!--SR:!2024-11-19,27,257-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::\[ɵ\] <!--SR:!2025-04-06,178,314-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::\[œ\] <!--SR:!2024-10-31,203,293-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::\[œ̃\] <!--SR:!2025-07-13,521,321-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::\[ɶ\] <!--SR:!2026-04-07,664,331-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::\[p\] <!--SR:!2026-04-17,554,251-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::\[q\] <!--SR:!2025-10-23,378,231-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::\[r\] <!--SR:!2025-12-10,552,331-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::\[ɾ\] <!--SR:!2025-07-07,501,371-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::\[ʀ\] <!--SR:!2025-08-07,560,360-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::\[ɽ\] <!--SR:!2024-12-09,342,300-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::\[ɹ\] <!--SR:!2024-12-31,314,311-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::\[ɻ\] <!--SR:!2026-08-31,731,331-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::\[ʁ\] <!--SR:!2025-01-15,338,373-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::\[s\] <!--SR:!2025-08-09,562,361-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::\[ʃ\] <!--SR:!2026-08-02,647,291-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::\[ʂ\] <!--SR:!2025-01-03,303,354-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::\[t\] <!--SR:!2025-01-04,393,361-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::\[ʈ\] <!--SR:!2024-11-08,84,273-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::\[ts\] <!--SR:!2025-07-30,418,375-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::\[tʃ\]
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::\[tɕ\] <!--SR:!2025-07-29,330,374-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::\[tʂ\] <!--SR:!2025-07-26,415,375-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::\[u\] <!--SR:!2025-02-01,169,334-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::\[ʊ\] <!--SR:!2025-04-18,309,356-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::\[ʉ\]
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::\[v\] <!--SR:!2025-06-05,374,375-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::\[ʋ\] <!--SR:!2024-11-29,202,335-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::\[w\]
- [labialization](labialization.md)::\[ʷ\] <!--SR:!2025-08-20,349,374-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::\[ʍ\] <!--SR:!2025-06-21,270,256-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::\[ɯ\]
- [voiced velar approximant](voiced%20velar%20approximant.md)::\[ɰ\]
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::\[x\] <!--SR:!2024-12-18,94,314-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::\[χ\] <!--SR:!2024-11-17,117,314-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::\[y\] <!--SR:!2025-09-10,449,376-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::\[ʏ\]
- [voiced velar fricative](voiced%20velar%20fricative.md)::\[ɣ\] <!--SR:!2024-11-09,100,236-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::\[ɤ\]
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::\[ʎ\] <!--SR:!2025-04-08,165,295-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::\[ɥ\] <!--SR:!2025-01-20,95,274-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::\[z\] <!--SR:!2025-07-19,409,375-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::\[ʒ\] <!--SR:!2024-10-29,93,275-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::\[ʑ\]
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::\[ʐ\]
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::\[θ\] <!--SR:!2025-06-08,370,376-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::\[ɸ\] <!--SR:!2024-10-30,41,334-->
- [glottal stop](glottal%20stop.md)::\[ʔ\]
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::\[ʕ\] <!--SR:!2024-11-20,204,335-->
- [tenuis dental click](tenuis%20dental%20click.md)::\[ǀ\] <!--SR:!2025-02-16,236,316-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::\[ǁ\] <!--SR:!2025-08-17,433,375-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::\[ǃ\]
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::\[ʘ\]
- [tenuis palatal click](tenuis%20palatal%20click.md)::\[ǂ\] <!--SR:!2025-03-25,290,356-->

<!--/pytextgen-->

<!--pytextgen generate section="d92e"--><!-- The following content is generated at 2024-01-04T20:18:00.795972+08:00. Any edits will be overridden! -->

- \[a\]::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2024-12-26,385,358-->
- \[ä\]::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2027-07-08,1042,373-->
- \[ɐ\]::[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!2025-04-24,413,351-->
- \[ɑ\]::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2026-07-29,764,337-->
- \[ɑ̃\]::[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2027-05-07,962,339-->
- \[ɒ\]::[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2026-02-14,508,272-->
- \[ʌ\]::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2024-12-13,99,214-->
- \[æ\]::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!2025-03-03,403,337-->
- \[b\]::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2025-08-14,567,358-->
- \[ɓ\]::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2025-02-24,390,371-->
- \[β\]::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2025-07-21,466,351-->
- \[ʙ\]::[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2028-03-13,1243,351-->
- \[c\]::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2026-08-04,760,321-->
- \[ç\]::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2024-11-28,283,291-->
- \[ɕ\]::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2025-01-05,329,373-->
- \[d\]::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2025-01-16,357,372-->
- \[ɗ\]::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2024-11-02,291,351-->
- \[ɖ\]::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2027-10-04,1081,341-->
- \[ð\]::[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2025-12-12,631,371-->
- \[dz\]::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2025-03-09,361,374-->
- \[dʒ\]::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2025-12-03,557,297-->
- \[dʑ\]::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2027-03-12,957,351-->
- \[dʐ\]::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2025-03-26,373,374-->
- \[e\]::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2025-02-23,349,374-->
- \[ɘ\]::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!2025-08-12,565,357-->
- \[ə\]::[mid central vowel](mid%20central%20vowel.md) <!--SR:!2025-02-23,234,301-->
- \[ɚ\]::[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2025-09-08,424,332-->
- \[ɛ\]::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!2025-01-25,142,321-->
- \[ɛ̃\]::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2025-10-19,587,371-->
- \[ɜ\]::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-12-18,105,312-->
- \[ɝ\]::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2025-05-14,427,351-->
- \[f\]::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2025-05-23,450,318-->
- \[ɡ\]::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2025-07-22,551,360-->
- \[ɠ\]::[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2025-06-01,464,351-->
- \[ɢ\]::[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2025-06-05,510,357-->
- \[h\]::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2025-11-07,602,368-->
- \[ɦ\]::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2025-06-14,519,357-->
- \[ʰ\]::[aspirated consonant](aspirated%20consonant.md) <!--SR:!2026-05-26,661,311-->
- \[ħ\]::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2025-09-09,590,361-->
- \[i\]::[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!2027-04-04,942,374-->
- \[ɪ\]::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2025-04-24,398,374-->
- \[ɨ\]::[close central unrounded vowel](close%20central%20unrounded%20vowel.md) <!--SR:!2025-12-10,481,271-->
- \[j\]::[voiced palatal approximant](voiced%20palatal%20approximant.md) <!--SR:!2027-07-18,999,351-->
- \[ʲ\]::[palatalization](palatalization%20(phonetics).md) <!--SR:!2027-05-16,950,351-->
- \[ʝ\]::[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!2024-11-01,331,341-->
- \[ɟ\]::[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2026-03-29,658,317-->
- \[ʄ\]::[voiced palatal implosive](voiced%20palatal%20implosive.md) <!--SR:!2025-06-27,286,211-->
- \[k\]::[voiceless velar plosive](voiceless%20velar%20plosive.md) <!--SR:!2026-05-07,595,292-->
- \[l\]::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) <!--SR:!2025-03-27,285,231-->
- \[ɫ\]::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) <!--SR:!2025-07-14,358,271-->
- \[ɬ\]::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2025-07-24,390,331-->
- \[ɭ\]::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!2025-04-02,313,311-->
- \[ɺ\]::[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) <!--SR:!2024-12-03,260,340-->
- \[ɮ\]::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!2026-04-15,655,301-->
- \[ʟ\]::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!2026-01-24,610,317-->
- \[m\]::[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2025-02-14,363,373-->
- \[ɱ\]::[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2026-09-24,707,314-->
- \[n\]::[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!2026-06-18,729,353-->
- \[ŋ\]::[voiced velar nasal](voiced%20velar%20nasal.md) <!--SR:!2026-06-07,647,334-->
- \[ɲ\]::[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2024-11-03,260,353-->
- \[ɳ\]::[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2025-06-27,422,311-->
- \[ɴ\]::[voiced uvular nasal](voiced%20uvular%20nasal.md) <!--SR:!2025-02-03,300,354-->
- \[o\]::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) <!--SR:!2025-07-13,542,357-->
- \[ɔ\]::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) <!--SR:!2025-06-16,431,311-->
- \[ɔ̃\]::[nasalized open-mid back rounded vowel](nasal%20vowel.md) <!--SR:!2025-02-25,255,272-->
- \[ø\]::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) <!--SR:!2024-12-28,120,311-->
- \[ɵ\]::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2025-07-01,285,301-->
- \[œ\]::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) <!--SR:!2026-10-18,731,313-->
- \[œ̃\]::[nasalized open-mid front rounded vowel](nasal%20vowel.md) <!--SR:!2025-08-23,576,358-->
- \[ɶ\]::[open front rounded vowel](open%20front%20rounded%20vowel.md) <!--SR:!2026-09-15,764,331-->
- \[p\]::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2024-10-30,287,331-->
- \[q\]::[voiceless uvular plosive](voiceless%20uvular%20plosive.md) <!--SR:!2025-09-19,482,351-->
- \[r\]::[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2027-11-30,1181,371-->
- \[ɾ\]::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2026-08-13,735,352-->
- \[ʀ\]::[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2024-11-25,74,274-->
- \[ɽ\]::[voiced retroflex flap](voiced%20retroflex%20flap.md) <!--SR:!2026-02-01,533,351-->
- \[ɹ\]::[voiced alveolar approximant](voiced%20alveolar%20approximant.md) <!--SR:!2026-12-25,847,320-->
- \[ɻ\]::[voiced retroflex approximant](voiced%20retroflex%20approximant.md) <!--SR:!2025-01-06,370,300-->
- \[ʁ\]::[voiced uvular fricative](voiced%20uvular%20fricative.md) <!--SR:!2024-10-31,239,354-->
- \[s\]::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2025-09-08,535,317-->
- \[ʃ\]::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) <!--SR:!2025-06-13,464,321-->
- \[ʂ\]::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2024-11-16,348,340-->
- \[t\]::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!2024-11-25,271,354-->
- \[ʈ\]::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!2025-03-28,282,314-->
- \[ts\]::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) <!--SR:!2025-02-08,390,340-->
- \[tʃ\]::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) <!--SR:!2025-09-11,454,271-->
- \[tɕ\]::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) <!--SR:!2025-11-14,466,294-->
- \[tʂ\]::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!2027-01-13,827,354-->
- \[u\]::[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2025-07-23,464,311-->
- \[ʊ\]::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) <!--SR:!2024-12-04,265,354-->
- \[ʉ\]::[close central rounded vowel](close%20central%20rounded%20vowel.md) <!--SR:!2025-11-19,479,279-->
- \[v\]::[voiced labiodental fricative](voiced%20labiodental%20fricative.md) <!--SR:!2025-02-23,389,371-->
- \[ʋ\]::[voiced labiodental approximant](voiced%20labiodental%20approximant.md) <!--SR:!2025-06-21,458,351-->
- \[w\]::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2025-01-21,343,373-->
- \[ʷ\]::[labialization](labialization.md) <!--SR:!2025-08-06,525,371-->
- \[ʍ\]::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) <!--SR:!2025-04-16,297,314-->
- \[ɯ\]::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2025-07-31,404,273-->
- \[ɰ\]::[voiced velar approximant](voiced%20velar%20approximant.md) <!--SR:!2025-01-21,285,311-->
- \[x\]::[voiceless velar fricative](voiceless%20velar%20fricative.md) <!--SR:!2025-06-15,396,320-->
- \[χ\]::[voiceless uvular fricative](voiceless%20uvular%20fricative.md) <!--SR:!2025-06-15,402,260-->
- \[y\]::[close front rounded vowel](close%20front%20rounded%20vowel.md)
- \[ʏ\]::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- \[ɣ\]::[voiced velar fricative](voiced%20velar%20fricative.md)
- \[ɤ\]::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- \[ʎ\]::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- \[ɥ\]::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) <!--SR:!2025-01-28,219,296-->
- \[z\]::[voiced alveolar fricative](voiced%20alveolar%20fricative.md) <!--SR:!2025-02-01,252,356-->
- \[ʒ\]::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) <!--SR:!2025-01-19,255,355-->
- \[ʑ\]::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) <!--SR:!2025-07-04,395,376-->
- \[ʐ\]::[voiced retroflex fricative](voiced%20retroflex%20fricative.md) <!--SR:!2025-03-27,209,334-->
- \[θ\]::[voiceless dental fricative](voiceless%20dental%20fricative.md)
- \[ɸ\]::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) <!--SR:!2025-07-06,398,375-->
- \[ʔ\]::[glottal stop](glottal%20stop.md)
- \[ʕ\]::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- \[ǀ\]::[tenuis dental click](tenuis%20dental%20click.md) <!--SR:!2025-06-14,275,354-->
- \[ǁ\]::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) <!--SR:!2025-08-23,434,376-->
- \[ǃ\]::[tenuis alveolar click](tenuis%20alveolar%20click.md)
- \[ʘ\]::[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2025-08-13,426,376-->
- \[ǂ\]::[tenuis palatal click](tenuis%20palatal%20click.md) <!--SR:!2024-11-06,179,315-->

<!--/pytextgen-->

#### name–audio (letters)

<!--pytextgen generate section="5dfb"--><!-- The following content is generated at 2024-02-14T16:42:37.258792+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg) <!--SR:!2025-06-06,445,351-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) <!--SR:!2026-01-21,629,284-->
- [near-open central vowel](near-open%20central%20vowel.md)::![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) <!--SR:!2026-09-15,736,264-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) <!--SR:!2028-02-26,1302,333-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) <!--SR:!2025-07-05,450,311-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) <!--SR:!2024-12-17,403,324-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) <!--SR:!2026-04-04,676,293-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) <!--SR:!2025-10-04,617,358-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) <!--SR:!2025-10-29,637,358-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) <!--SR:!2027-09-14,1059,341-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) <!--SR:!2025-07-19,547,357-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) <!--SR:!2025-09-17,513,321-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) <!--SR:!2025-04-08,383,311-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) <!--SR:!2024-11-18,275,291-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) <!--SR:!2024-11-18,371,318-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) <!--SR:!2028-03-22,1292,371-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) <!--SR:!2024-11-16,369,324-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg) <!--SR:!2026-01-16,463,334-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) <!--SR:!2026-08-21,711,278-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg) <!--SR:!2026-07-15,634,238-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) <!--SR:!2025-01-22,286,278-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) <!--SR:!2025-09-23,469,313-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) <!--SR:!2025-11-25,576,284-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2027-01-22,939,351-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2025-09-25,391,251-->
- [mid central vowel](mid%20central%20vowel.md)::![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) <!--SR:!2025-02-08,303,292-->
- [r-colored mid central vowel](r-colored%20vowel.md)::![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2026-03-23,694,318-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2024-12-20,321,278-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) <!--SR:!2026-04-20,623,332-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2025-11-21,612,371-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2026-01-22,543,334-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) <!--SR:!2027-05-03,976,338-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) <!--SR:!2025-06-23,438,311-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) <!--SR:!2026-01-11,623,331-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg) <!--SR:!2026-02-14,761,353-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) <!--SR:!2026-03-30,630,278-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) <!--SR:!2025-05-12,363,314-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) <!--SR:!2026-04-21,610,334-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) <!--SR:!2026-12-30,804,264-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) <!--SR:!2024-12-16,291,354-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) <!--SR:!2026-07-21,704,331-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) <!--SR:!2024-11-23,257,354-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) <!--SR:!2026-01-05,561,278-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) <!--SR:!2025-02-11,341,297-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) <!--SR:!2025-05-11,395,224-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) <!--SR:!2025-09-01,465,333-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) <!--SR:!2025-07-22,491,298-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) <!--SR:!2025-06-23,467,308-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) <!--SR:!2024-11-18,345,341-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) <!--SR:!2025-01-19,341,371-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) <!--SR:!2024-11-13,268,351-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) <!--SR:!2027-03-07,867,351-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) <!--SR:!2026-07-20,707,258-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) <!--SR:!2025-08-23,499,273-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) <!--SR:!2026-08-31,829,338-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) <!--SR:!2024-11-03,206,312-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) <!--SR:!2024-12-13,268,314-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) <!--SR:!2025-03-24,347,260-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) <!--SR:!2024-12-12,176,190-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) <!--SR:!2027-02-06,865,291-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) <!--SR:!2026-01-24,648,318-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) <!--SR:!2026-08-28,761,293-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) <!--SR:!2024-12-31,284,291-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) <!--SR:!2025-07-13,479,298-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) <!--SR:!2027-03-05,911,304-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) <!--SR:!2027-02-28,864,353-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) <!--SR:!2025-06-24,422,311-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) <!--SR:!2026-04-20,573,253-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) <!--SR:!2024-11-12,292,331-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) <!--SR:!2025-05-01,456,284-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) <!--SR:!2025-08-17,479,258-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) <!--SR:!2025-01-22,360,298-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) <!--SR:!2024-11-26,258,291-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) <!--SR:!2025-03-10,364,312-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg) <!--SR:!2026-08-03,711,311-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) <!--SR:!2025-04-28,383,278-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) <!--SR:!2027-07-18,999,352-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) <!--SR:!2025-06-27,431,311-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) <!--SR:!2026-08-29,729,278-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) <!--SR:!2025-06-25,471,293-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg) <!--SR:!2025-02-08,369,331-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg) <!--SR:!2026-06-24,729,320-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) <!--SR:!2025-02-05,300,354-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) <!--SR:!2025-06-07,410,311-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) <!--SR:!2025-02-03,375,278-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) <!--SR:!2025-03-13,385,371-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) <!--SR:!2025-02-13,308,312-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) <!--SR:!2024-11-01,240,354-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) <!--SR:!2025-04-10,364,312-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) <!--SR:!2025-01-15,259,213-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) <!--SR:!2026-03-21,695,304-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) <!--SR:!2027-12-17,1147,374-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) <!--SR:!2025-02-25,372,373-->
- [voiced velar approximant](voiced%20velar%20approximant.md)::![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) <!--SR:!2025-03-09,415,317-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) <!--SR:!2026-03-30,685,293-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) <!--SR:!2027-02-10,902,318-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) <!--SR:!2026-10-19,780,331-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) <!--SR:!2026-10-11,722,244-->
- [voiced velar fricative](voiced%20velar%20fricative.md)::![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) <!--SR:!2027-06-13,1002,340-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) <!--SR:!2025-02-11,393,341-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) <!--SR:!2026-08-19,737,331-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) <!--SR:!2024-12-07,207,336-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg) <!--SR:!2025-03-21,203,334-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg) <!--SR:!2025-05-31,314,315-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg) <!--SR:!2024-10-27,177,335-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) <!--SR:!2025-03-07,248,296-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) <!--SR:!2025-08-04,364,315-->
- [glottal stop](glottal%20stop.md)::![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)
- [tenuis dental click](tenuis%20dental%20click.md)::![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) <!--SR:!2025-04-12,308,355-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) <!--SR:!2024-12-02,203,335-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)
- [tenuis palatal click](tenuis%20palatal%20click.md)::![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) <!--SR:!2025-03-23,288,355-->

<!--/pytextgen-->

<!--pytextgen generate section="f9aa"--><!-- The following content is generated at 2024-02-14T16:42:37.178940+08:00. Any edits will be overridden! -->

- ![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg)::[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2024-10-31,6,130-->
- ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)::[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2025-11-14,431,251-->
- ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)::[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!2024-11-07,61,150-->
- ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)::[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2024-11-03,24,130-->
- ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)::[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2024-11-27,99,233-->
- ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)::[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2025-10-04,457,292-->
- ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)::[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2025-04-11,183,219-->
- ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)::[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!2024-10-28,4,150-->
- ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)::[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2024-10-31,37,151-->
- ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)::[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2025-10-17,526,298-->
- ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)::[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2025-01-06,185,251-->
- ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)::[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2025-03-31,267,231-->
- ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)::[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2024-11-04,25,130-->
- ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)::[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2024-11-05,11,130-->
- ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)::[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2024-11-27,34,130-->
- ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)::[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2025-03-24,151,171-->
- ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)::[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2024-11-11,25,130-->
- ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg)::[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2024-10-28,59,153-->
- ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)::[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2024-11-01,22,130-->
- ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg)::[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2024-11-15,26,134-->
- ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)::[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2024-11-10,17,130-->
- ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)::[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2024-10-31,6,130-->
- ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)::[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2024-11-22,106,214-->
- ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)::[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-12-29,262,251-->
- ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)::[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-11-10,31,150-->
- ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)::[mid central vowel](mid%20central%20vowel.md) <!--SR:!2024-11-19,29,130-->
- ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2025-02-03,337,299-->
- ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)::[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!2024-10-31,5,150-->
- ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)::[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2024-10-28,11,130-->
- ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)::[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2024-11-09,30,130-->
- ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)::[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2024-11-04,15,130-->
- ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)::[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2024-11-19,40,193-->
- ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)::[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2024-12-07,117,214-->
- ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)::[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2024-11-15,21,130-->
- ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg)::[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2024-11-05,15,130-->
- ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)::[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2024-12-13,145,220-->
- ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)::[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2025-09-17,408,221-->
- ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)::[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2025-07-28,473,351-->
- ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)::[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!2024-11-05,15,134-->
- ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)::[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2025-01-31,105,214-->
- ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)::[close central unrounded vowel](close%20central%20unrounded%20vowel.md)
- ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)::[voiced palatal approximant](voiced%20palatal%20approximant.md)
- ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)::[voiced palatal fricative](voiced%20palatal%20fricative.md)
- ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)::[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2024-11-22,43,234-->
- ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)::[voiced palatal implosive](voiced%20palatal%20implosive.md)
- ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)::[voiceless velar plosive](voiceless%20velar%20plosive.md)
- ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)::[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)
- ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)::[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)
- ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)::[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)
- ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)::[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!2024-10-31,6,130-->
- ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)::[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)
- ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)::[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!2024-10-28,4,130-->
- ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)::[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2024-12-26,77,296-->
- ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)::[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2024-12-04,125,314-->
- ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)::[voiced alveolar nasal](voiced%20alveolar%20nasal.md)
- ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)::[voiced velar nasal](voiced%20velar%20nasal.md)
- ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)::[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2024-10-27,8,174-->
- ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)::[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2024-11-14,70,294-->
- ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)::[voiced uvular nasal](voiced%20uvular%20nasal.md)
- ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)::[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
- ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)::[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) <!--SR:!2025-04-18,277,296-->
- ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)::[nasalized open-mid back rounded vowel](nasal%20vowel.md) <!--SR:!2024-11-05,42,156-->
- ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)::[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
- ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)::[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2024-11-03,79,236-->
- ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)::[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
- ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)::[nasalized open-mid front rounded vowel](nasal%20vowel.md)
- ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)::[open front rounded vowel](open%20front%20rounded%20vowel.md)
- ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)::[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2024-11-10,24,130-->
- ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)::[voiceless uvular plosive](voiceless%20uvular%20plosive.md) <!--SR:!2024-11-15,29,130-->
- ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)::[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2024-12-20,145,275-->
- ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)::[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2025-04-10,235,295-->
- ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)::[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2025-08-16,336,296-->
- ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)::[voiced retroflex flap](voiced%20retroflex%20flap.md) <!--SR:!2024-12-16,76,274-->
- ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)::[voiced alveolar approximant](voiced%20alveolar%20approximant.md)
- ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg)::[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
- ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)::[voiced uvular fricative](voiced%20uvular%20fricative.md)
- ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)::[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)
- ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)::[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)
- ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)::[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2024-11-04,18,130-->
- ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)::[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!2024-11-26,47,175-->
- ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg)::[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!2025-01-21,94,274-->
- ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg)::[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)
- ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)::[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
- ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)::[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)
- ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)::[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!2024-11-21,35,254-->
- ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)::[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2025-06-22,243,235-->
- ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)::[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
- ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)::[close central rounded vowel](close%20central%20rounded%20vowel.md)
- ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)::[voiced labiodental fricative](voiced%20labiodental%20fricative.md)
- ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)::[voiced labiodental approximant](voiced%20labiodental%20approximant.md)
- ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)::[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)
- ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)::[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
- ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)::[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2024-11-04,25,130-->
- ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)::[voiced velar approximant](voiced%20velar%20approximant.md)
- ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)::[voiceless velar fricative](voiceless%20velar%20fricative.md)
- ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)::[voiceless uvular fricative](voiceless%20uvular%20fricative.md) <!--SR:!2024-10-31,6,130-->
- ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)::[close front rounded vowel](close%20front%20rounded%20vowel.md)
- ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)::[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)::[voiced velar fricative](voiced%20velar%20fricative.md)
- ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)::[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)::[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)::[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
- ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)::[voiced alveolar fricative](voiced%20alveolar%20fricative.md) <!--SR:!2025-03-03,235,275-->
- ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)::[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
- ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)::[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) <!--SR:!2024-11-29,50,214-->
- ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)::[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
- ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)::[voiceless dental fricative](voiceless%20dental%20fricative.md)
- ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)::[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
- ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)::[glottal stop](glottal%20stop.md)
- ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)::[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)::[tenuis dental click](tenuis%20dental%20click.md)
- ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)::[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) <!--SR:!2024-12-14,65,275-->
- ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)::[tenuis alveolar click](tenuis%20alveolar%20click.md)
- ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)::[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2025-07-07,399,375-->
- ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)::[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/pytextgen-->

#### name–description (letters)

<!--pytextgen generate section="50b0"--><!-- The following content is generated at 2024-01-04T20:18:01.048113+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md)::[English](English%20language.md) _h**a**t_ \[hat\] <!--SR:!2025-01-13,154,290-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md)::[English](English%20language.md) _br**a**_ \[bɹäː\] <!--SR:!2024-11-27,35,130-->
- [near-open central vowel](near-open%20central%20vowel.md)::[English](English%20language.md) _n**u**t_ \[nɐʔt\] <!--SR:!2024-11-11,24,130-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md)::[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\] <!--SR:!2024-11-14,35,150-->
- [nasalized open back unrounded vowel](nasal%20vowel.md)::[French](French%20language.md) _s**an**s_ [sɑ̃] "without" <!--SR:!2024-11-15,28,164-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md)::[English](English%20language.md) _n**o**t_ \[nɒt\] <!--SR:!2025-06-22,373,224-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)::[English](English%20language.md) _g**u**t_ \[ɡʌt\] <!--SR:!2024-11-15,131,284-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)::[English](English%20language.md) _c**a**t_ \[kʰæt\] <!--SR:!2024-10-28,11,130-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md)::[English](English%20language.md) _a**b**ack_ \[əˈbæk\] <!--SR:!2025-03-13,242,264-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md)::[English](English%20language.md) _**b**ody_ \[ɓʌdi\] <!--SR:!2024-11-26,217,264-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md)::[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava" <!--SR:!2024-11-29,160,224-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md)::[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw" <!--SR:!2025-01-05,77,204-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md)::[French](French%20language.md) _**q**ui_ \[ci\] "who" <!--SR:!2025-10-26,374,284-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md)::[English](English%20language.md) _**h**ue_ \[çʉː\] <!--SR:!2024-12-12,63,150-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)::[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\] <!--SR:!2024-10-30,11,130-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md)::[English](English%20language.md) _**d**ash_ \[ˈdæʃ\] <!--SR:!2025-09-13,520,273-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md)::[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail" <!--SR:!2025-01-29,293,213-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md)::[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north" <!--SR:!2024-10-28,6,130-->
- [voiced dental fricative](voiced%20dental%20fricative.md)::[English](English%20language.md) _**th**is_ \[ðɪs\] <!--SR:!2025-05-26,323,233-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md)::[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\] <!--SR:!2024-11-19,33,130-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)::[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\] <!--SR:!2024-11-16,53,178-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)::[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound" <!--SR:!2024-12-30,91,218-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md)::[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam" <!--SR:!2025-02-07,161,218-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)::[English](English%20language.md) _m**ay**_ \[meː\] <!--SR:!2024-11-04,18,130-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɘːd\] <!--SR:!2024-11-23,125,218-->
- [mid central vowel](mid%20central%20vowel.md)::[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\] <!--SR:!2024-11-03,31,158-->
- [r-colored mid central vowel](r-colored%20vowel.md)::[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\] <!--SR:!2025-06-30,253,258-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)::[English](English%20language.md) _b**e**d_ \[bɛd\] <!--SR:!2024-11-06,99,218-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md)::[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand" <!--SR:!2024-10-28,4,130-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɜːd\] <!--SR:!2025-04-20,374,278-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)::[English](English%20language.md) _b**ir**d_ \[bɝːd\] <!--SR:!2025-04-24,402,317-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)::[English](English%20language.md) _**f**ill_ \[fɪɫ\] <!--SR:!2025-05-06,224,237-->
- [voiced velar plosive](voiced%20velar%20plosive.md)::[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\] <!--SR:!2024-12-31,71,177-->
- [voiced velar implosive](voiced%20velar%20implosive.md)::[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!2024-11-23,53,157-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md)::[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\] <!--SR:!2024-12-06,111,257-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md)::[English](English%20language.md) _**h**igh_ \[haɪ̯\] <!--SR:!2024-11-04,250,297-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md)::[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\] <!--SR:!2025-07-13,312,237-->
- [aspirated consonant](aspirated%20consonant.md)::[English](English%20langugae.md) _**t**op_ \[tʰɒp\] <!--SR:!2025-06-09,514,357-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)::[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\] <!--SR:!2025-03-10,140,257-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md)::[English](English%20language.md) _fr**ee**_ \[fɹiː\] <!--SR:!2024-11-05,11,137-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)::[English](English%20language.md) _b**i**t_ \[bɪʔt\] <!--SR:!2024-11-24,67,157-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md)::[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you" <!--SR:!2024-10-27,10,130-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md)::[English](English%20language.md) _**y**ou_ \[juː\] <!--SR:!2024-10-30,29,158-->
- [palatalization](palatalization%20(phonetics).md)::[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive" <!--SR:!2025-06-01,244,238-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md)::[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock" <!--SR:!2024-11-04,9,130-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md)::[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)" <!--SR:!2024-11-20,30,130-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md)::[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday" <!--SR:!2024-11-15,110,198-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md)::[English](English%20language.md) _**k**iss_ \[kʰɪs\] <!--SR:!2025-01-10,130,199-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)::[English](English%20language.md) _**l**et_ \[lɛt\] <!--SR:!2025-09-28,394,280-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)::[English](English%20language.md) _fee**l**_ \[fiːɫ\] <!--SR:!2024-11-02,207,240-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)::[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle" <!--SR:!2024-10-27,9,130-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)::[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg" <!--SR:!2024-10-29,35,130-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)::[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six" <!--SR:!2024-10-31,5,130-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)::[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat" <!--SR:!2024-11-07,21,130-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)::[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\] <!--SR:!2025-10-22,367,221-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md)::[English](English%20language.md) _hi**m**_ \[hɪm\] <!--SR:!2026-01-21,541,281-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md)::[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\] <!--SR:!2024-11-13,306,301-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md)::[English](English%20language.md) _**n**ice_ \[naɪs\] <!--SR:!2025-11-02,443,281-->
- [voiced velar nasal](voiced%20velar%20nasal.md)::[English](English%20language.md) _si**ng**_ \[sɪŋ\] <!--SR:!2024-12-13,80,261-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md)::[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion" <!--SR:!2024-10-29,158,241-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md)::[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn" <!--SR:!2024-12-28,72,150-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md)::[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled" <!--SR:!2025-01-14,184,201-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)::[English](English%20language.md) _y**aw**n_ \[joːn\] <!--SR:!2024-10-27,9,130-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)::[English](English%20language.md) _n**o**t_ \[nɔt\] <!--SR:!2024-10-28,117,211-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md)::[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound" <!--SR:!2024-11-13,43,171-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)::[French](French%20language.md) _p**eu**_ \[pø\] "few" <!--SR:!2024-11-05,11,130-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)::[English](English%20language.md) _f**oo**t_ \[fɵʔt\] <!--SR:!2024-10-28,6,130-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)::[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young" <!--SR:!2025-01-10,85,150-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md)::[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown" <!--SR:!2024-11-18,31,130-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md)::[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green" <!--SR:!2024-10-30,4,130-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)::[English](English%20language.md) _**p**ack_ \[pʰæk\] <!--SR:!2025-06-02,298,251-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md)::[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat" <!--SR:!2024-10-27,17,171-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md)::[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog" <!--SR:!2025-02-12,134,211-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)::[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive" <!--SR:!2024-11-11,179,231-->
- [voiced uvular trill](voiced%20uvular%20trill.md)::[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red" <!--SR:!2025-11-19,514,291-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md)::[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf" <!--SR:!2024-11-02,23,130-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md)::[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest" <!--SR:!2024-12-31,82,151-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md)::[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat" <!--SR:!2024-10-28,11,191-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md)::[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay" <!--SR:!2024-11-15,29,130-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)::[English](English%20language.md) _**s**it_ \[sɪt\] <!--SR:!2025-04-14,186,271-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)::[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\] <!--SR:!2024-10-31,28,231-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)::[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle" <!--SR:!2024-10-30,13,130-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)::[English](English%20language.md) _**t**ick_ \[tʰɪk\] <!--SR:!2026-05-26,586,271-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)::[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card" <!--SR:!2025-07-26,348,231-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)::[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\] <!--SR:!2025-02-19,255,251-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)::[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\] <!--SR:!2024-12-14,167,271-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)::[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)" <!--SR:!2024-10-28,6,130-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)::[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)" <!--SR:!2024-10-30,13,130-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md)::[English](English%20language.md) _b**oo**t_ \[bu̟ːt\] <!--SR:!2025-01-18,129,191-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)::[English](English%20language.md) _h**oo**k_ \[hʊʔk\] <!--SR:!2024-11-12,26,130-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md)::[English](English%20language.md) _g**oo**se_ \[ɡʉːs\] <!--SR:!2024-11-04,32,150-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md)::[English](English%20language.md) _**v**al**v**e_ \[væɫv\] <!--SR:!2025-01-10,274,312-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md)::[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby" <!--SR:!2026-01-05,478,272-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)::[English](English%20language.md) _**w**eep_ \[wiːp\] <!--SR:!2025-01-24,206,252-->
- [labialization](labialization.md)::[English](English%20language.md) _**r**eed_ \[ɹʷiːd\] <!--SR:!2025-03-11,233,232-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)::[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\] <!--SR:!2025-01-08,76,172-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md)::[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow" <!--SR:!2024-12-03,54,212-->
- [voiced velar approximant](voiced%20velar%20approximant.md)::[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine" <!--SR:!2024-10-30,20,130-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md)::[German](German%20language.md) _Bu**ch**_ \[buːx\] "book" <!--SR:!2024-11-11,25,130-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md)::[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very" <!--SR:!2024-11-21,35,130-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md)::[French](French%20language.md) _t**u**_ \[t̪y] "you" <!--SR:!2025-05-15,270,210-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)::[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect" <!--SR:!2024-11-08,29,130-->
- [voiced velar fricative](voiced%20velar%20fricative.md)::[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend" <!--SR:!2024-10-31,10,130-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)::[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry" <!--SR:!2024-11-08,14,130-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)::[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\] <!--SR:!2025-01-16,186,210-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)::[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm" <!--SR:!2024-12-05,40,130-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md)::[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\] <!--SR:!2024-12-19,79,190-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)::[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\] <!--SR:!2024-11-24,76,210-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)::[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire" <!--SR:!2024-10-28,6,130-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md)::[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife" <!--SR:!2024-10-31,5,130-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md)::[English](English%20language.md) _**th**in_ \[θɪn\] <!--SR:!2025-08-27,359,250-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)::[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay" <!--SR:!2024-10-30,204,250-->
- [glottal stop](glottal%20stop.md)::[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\] <!--SR:!2025-05-16,234,230-->
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)::[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion" <!--SR:!2024-10-29,19,130-->
- [tenuis dental click](tenuis%20dental%20click.md)::[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\] <!--SR:!2024-11-30,148,270-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)::[English](English%20language.md) _**tchick**_ \[ˈǁ\] <!--SR:!2025-04-17,222,250-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md)::[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat" <!--SR:!2024-11-15,29,130-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md)::[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two" <!--SR:!2025-02-28,234,210-->
- [tenuis palatal click](tenuis%20palatal%20click.md)::[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth" <!--SR:!2024-11-15,21,130-->

<!--/pytextgen-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--pytextgen generate section="485d"--><!-- The following content is generated at 2023-11-12T00:31:30.816306+08:00. Any edits will be overridden! -->

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

<!--/pytextgen-->

#### name–symbol (diacritics)

<!--pytextgen generate section="ffa2"--><!-- The following content is generated at 2024-01-04T20:18:01.097852+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md)::\[◌̃\] (e.g. [ã]) <!--SR:!2025-12-01,621,371-->
- [centralized](central%20vowel.md)::\[◌̈\] (e.g. [ä]) <!--SR:!2025-06-02,417,374-->
- [extra-short](extra-shortness.md)::\[◌̆\] (e.g. [ă]) <!--SR:!2024-10-28,47,141-->
- [non-syllabic](diphthong.md)::\[◌̯\] (e.g. [a̯]) <!--SR:!2025-04-10,332,314-->
- [voiceless](voicelessness.md)::\[◌̥\] (e.g. [n̥]) <!--SR:!2025-02-01,278,294-->
- [syllabic](syllabic%20consonant.md)::\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) <!--SR:!2026-10-20,828,341-->
- [dental/alveolar](dental%20consonant.md)::\[◌̪\] (e.g. [d̪]) <!--SR:!2024-12-17,378,360-->
- [aspirated](aspirated%20consonant.md)::\[◌ʰ\] (e.g. [kʰ]) <!--SR:!2025-08-06,559,360-->
- [ejective](ejective%20consonant.md)::\[◌’\] (e.g. [k’]) <!--SR:!2025-04-23,416,373-->
- [long](longness%20(phonetics).md)::\[◌ː\] (e.g. [aː]) <!--SR:!2025-09-03,586,361-->
- [half-long](half-longness%20(phonetics).md)::\[◌ˑ\] (e.g. [aˑ]) <!--SR:!2025-03-25,372,374-->
- [primary stress](stress%20(lingustics).md)::\[ˈ◌\] (e.g. [ˈa]) <!--SR:!2025-03-22,393,372-->
- [secondary stress](secondary%20stress.md)::\[ˌ◌\] (e.g. [ˌa]) <!--SR:!2026-11-10,802,352-->
- [syllable break](syllable.md)::\[.\] <!--SR:!2025-08-29,439,376-->

<!--/pytextgen-->

<!--pytextgen generate section="94fb"--><!-- The following content is generated at 2024-01-04T20:17:59.931857+08:00. Any edits will be overridden! -->

- \[◌̃\] (e.g. [ã])::[nasalized](nasal%20vowel.md) <!--SR:!2026-07-18,727,290-->
- \[◌̈\] (e.g. [ä])::[centralized](central%20vowel.md) <!--SR:!2025-01-04,421,318-->
- \[◌̆\] (e.g. [ă])::[extra-short](extra-shortness.md) <!--SR:!2025-05-17,355,264-->
- \[◌̯\] (e.g. [a̯])::[non-syllabic](diphthong.md) <!--SR:!2024-12-10,94,164-->
- \[◌̥\] (e.g. [n̥])::[voiceless](voicelessness.md) <!--SR:!2027-10-27,1097,313-->
- \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])::[syllabic](syllabic%20consonant.md) <!--SR:!2026-07-18,687,298-->
- \[◌̪\] (e.g. [d̪])::[dental/alveolar](dental%20consonant.md) <!--SR:!2025-11-11,575,318-->
- \[◌ʰ\] (e.g. [kʰ])::[aspirated](aspirated%20consonant.md) <!--SR:!2026-05-21,799,358-->
- \[◌’\] (e.g. [k’])::[ejective](ejective%20consonant.md) <!--SR:!2027-02-01,896,318-->
- \[◌ː\] (e.g. [aː])::[long](longness%20(phonetics).md) <!--SR:!2025-08-10,563,357-->
- \[◌ˑ\] (e.g. [aˑ])::[half-long](half-longness%20(phonetics).md) <!--SR:!2024-12-31,241,291-->
- \[ˈ◌\] (e.g. [ˈa])::[primary stress](stress%20(lingustics).md) <!--SR:!2027-04-15,1029,357-->
- \[ˌ◌\] (e.g. [ˌa])::[secondary stress](secondary%20stress.md) <!--SR:!2025-02-25,435,361-->
- \[.\]::[syllable break](syllable.md) <!--SR:!2025-06-19,380,376-->

<!--/pytextgen-->

#### name–description (diacritics)

<!--pytextgen generate section="50bd"--><!-- The following content is generated at 2024-01-04T20:18:01.248419+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md)::[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine" <!--SR:!2024-11-24,156,218-->
- [centralized](central%20vowel.md)::[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go" <!--SR:!2024-11-13,145,204-->
- [extra-short](extra-shortness.md)::[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\] <!--SR:!2025-05-07,324,244-->
- [non-syllabic](diphthong.md)::[English](English%20language.md) _co**w**_ \[kʰaʊ̯\] <!--SR:!2027-02-18,935,313-->
- [voiceless](voicelessness.md)::[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\] <!--SR:!2025-05-13,487,338-->
- [syllabic](syllabic%20consonant.md)::[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\] <!--SR:!2024-12-02,93,238-->
- [dental/alveolar](dental%20consonant.md)::[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two" <!--SR:!2026-04-17,583,298-->
- [aspirated](aspirated%20consonant.md)::[English](English%20language.md) _**c**ome_ \[kʰɐm\] <!--SR:!2025-10-16,627,358-->
- [ejective](ejective%20consonant.md)::[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!2025-06-03,277,197-->
- [long](longness%20(phonetics).md)::[English](English%20language.md) _shh!_ \[ʃː\] <!--SR:!2025-01-24,378,338-->
- [half-long](half-longness%20(phonetics).md)::[English](English%20language.md) _caught_ \[ˈkʰɔˑt\] <!--SR:!2025-10-07,501,279-->
- [primary stress](stress%20(lingustics).md)::[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2025-12-02,528,311-->
- [secondary stress](secondary%20stress.md)::[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2025-05-13,386,312-->
- [syllable break](syllable.md)::[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\] <!--SR:!2025-04-14,340,290-->

<!--/pytextgen-->
