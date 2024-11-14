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
> - phonetic symbol pattern ::@:: notice that the symbol of each phonetic is somewhat related to its sound, and similarly-sounding phonetics usually have similar symbols

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
> 1. {@{exo-labial (outer [lip](lip.md))}@}
> 2. {@{endo-labial (inner [lip](lip.md))}@}
> 3. {@{dental ([teeth](tooth.md))}@}
> 4. {@{alveolar (front [alveolar ridge](alveolar%20ridge.md))}@}
> 5. {@{post-alveolar (rear [alveolar ridge](alveolar%20ridge.md))}@}
> 6. {@{pre-palatal (front [hard palate](hard%20palate.md))}@}
> 7. {@{palatal ([hard palate](hard%20palate.md))}@}
> 8. {@{velar ([soft palate](soft%20palate.md))}@}
> 9. {@{uvular/post-velar ([uvula](uvula.md))}@}
> 10. {@{pharyngeal ([pharyngeal](pharynx.md) wall)}@}
> 11. {@{glottal/laryngeal ([vocal cords](vocal%20cords.md))}@}
> 12. {@{epiglottal ([epiglottis](epiglottis.md))}@}
> 13. {@{radical ([tongue](tongue.md) root)}@}
> 14. {@{postero-dorsal (rear [tongue](tongue.md) body)}@}
> 15. {@{antero-dorsal (front [tongue](tongue.md) body)}@}
> 16. {@{laminal ([tongue](tongue.md) blade)}@}
> 17. {@{apical ([tongue](tongue.md) tip or apex)}@}
> 18. {@{sub-laminal/sub-apical ([tongue](tongue.md) underside)}@}

- [consonant](consonant.md)::@::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md)
  - [airstream mechanism](airstream%20mechanism.md)::@::how the moving [air](air.md) is thrusted
    - (all) [pulmonic](pulmonic%20consonant.md) egressive::@::[air](air.md) is exhaled from the [lungs](lung.md)
    - (16%) [glottalic](glottalic%20consonant.md) egressive::@::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md)
    - (13%) [glottalic](glottalic%20consonant.md) ingressive::@::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md)
    - (<2%) lingual/[velaric](velar%20consonant.md) ingressive::@::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md)
    - ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive::@::[air](air.md) is inhaled into the [lungs](lung.md)
    - ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive::@::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md)
  - [length](gemination.md)::@::how long the articulation of a [consonant](consonant.md) lasts
    - values in ascending [length](gemination.md):@:single/singleton, geminate, long geminate
  - [manner of articulation](manner%20of%20articulation.md)::@::configuration and interaction of the [speech organs](speech%20organ.md)
    - [affricate](affricate%20consonant.md)::@::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md)
    - [approximant](approximant%20consonant.md)::@::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md)
      - [lateral approximant](lateral%20consonant.md)::@::approximant with airflow directed towards one or both sides of the [tongue](tongue.md)
      - [semivowel/glide/semiconsonant](semivowel.md)::@::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary
    - [flap/tap](tap%20and%20flap%20consonants.md)::@::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact
    - [fricative/spirant](fricative%20consonant.md)::@::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation
      - [lateral](lateral%20consonant.md)::@::fricative with airflow directed towards one or both sides of the [tongue](tongue.md)
      - [sibilant](sibilant%20consonant.md)::@::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md)
    - [nasal](nasal%20consonant.md)::@::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow
    - [plosive/stop](plosive%20consonant.md)::@::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow
    - [trill](trill%20consonant.md)::@::consonant produced by vibrations between the active articulator and the passive articulator
  - [place of articulation](place%20of%20articulation.md)::@::location along the [vocal tract](vocal%20tract.md) producing the consonant
    - [alveolar](alveolar%20ridge.md)::@::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive)
    - [aryepiglottal](pharyngeal%20consonant.md)::@::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active)
    - [coronal](coronal%20constant.md)::@::front of the [tongue](tongue.md) (active)
      - [apical](apical%20consonant.md)::@::tip of the [tongue](tongue.md) (active)
      - [laminal](laminal%20consonant.md)::@::blade of the [tongue](tongue.md), the upper front surface behind the tip (active)
      - [subapical](subapical%20consonant.md)::@::surface under the tip of the [tongue](tongue.md) (active)
    - [dental](dental%20consonant.md)::@::upper [teeth](tooth.md) (passive)
    - [dorsal](dorsal%20consonant.md)::@::body of the [tongue](tongue.md) (active)
    - [epiglottal](pharyngeal%20consonant.md)::@::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive)
    - [glottal](glottal%20consonant.md)::@::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active)
    - [labial](labial%20consonant.md)::@::lower [lip](lip.md) (active), upper [lip](lip.md) (passive)
    - [palatal](palatal%20consonant.md)::@::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive)
    - [pharyngeal](pharyngeal%20consonant.md)::@::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive)
    - [post-alveolar](post-alveolar%20consonant.md)::@::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive)
    - [uvular](uvular%20consonant.md)::@::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive)
    - [velar](velar%20consonant.md)::@::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive)
  - [phonation](phonation.md)::@::how the [vocal cords](vocal%20folds.md) vibrate
    - [voiced](voice%20(phonetics).md)::@::the [vocal cords](vocal%20cords.md) vibrate fully
    - [voiceless](voicelessness.md)::@::the [vocal cords](vocal%20cords.md) do not vibrate
  - [voice onset time](voice%20onset%20time.md) (VOT)::@::timing of [phonation](phonation.md)
    - values in ascending [VOT](voice%20onset%20time.md):@:[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive)
- [vowel](vowel.md)::@::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md)
  - [vowel backness](vowel.md#backness)::@::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md)
    - values in ascending [vowel backness](vowel.md#backness):@:[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md)
  - [vowel height](vowel.md#height)::@::vertical position of the [tongue](tongue.md)
    - values in descending [vowel height](vowel.md#height):@:[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md)
  - [vowel roundedness](roundedness.md)::@::rounding of the [lips](lip.md)
    - values in ascending [vowel roundedness](roundedness.md):@:unrounded, compressed, protruded

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]::@::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md)
- (principal) /[slashes](slash%20(punctuation).md)/::@::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}::@::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses))::@::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md)
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses)))::@::transcription of obscured speech or description of obscuring sound
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]::@::extra-precise transcription
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}::@::[morphophonemic](morphophonology.md) transcription
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫::@::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves

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

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:\[a\]
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:\[ä\]
- [near-open central vowel](near-open%20central%20vowel.md):@:\[ɐ\]
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:\[ɑ\]
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:\[ɑ̃\]
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:\[ɒ\]
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:\[ʌ\]
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:\[æ\]
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:\[b\]
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:\[ɓ\]
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:\[β\]
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:\[ʙ\]
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:\[c\]
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:\[ç\]
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:\[ɕ\]
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:\[d\]
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:\[ɗ\]
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:\[ɖ\]
- [voiced dental fricative](voiced%20dental%20fricative.md):@:\[ð\]
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:\[dz\]
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:\[dʒ\]
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:\[dʑ\]
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:\[dʐ\]
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:\[e\]
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:\[ɘ\]
- [mid central vowel](mid%20central%20vowel.md):@:\[ə\]
- [r-colored mid central vowel](r-colored%20vowel.md):@:\[ɚ\]
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:\[ɛ\]
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:\[ɛ̃\]
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:\[ɜ\]
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:\[ɝ\]
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:\[f\]
- [voiced velar plosive](voiced%20velar%20plosive.md):@:\[ɡ\]
- [voiced velar implosive](voiced%20velar%20implosive.md):@:\[ɠ\]
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:\[ɢ\]
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:\[h\]
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:\[ɦ\]
- [aspirated consonant](aspirated%20consonant.md):@:\[ʰ\]
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:\[ħ\]
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:\[i\]
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:\[ɪ\]
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:\[ɨ\]
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:\[j\]
- [palatalization](palatalization%20(phonetics).md):@:\[ʲ\]
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:\[ʝ\]
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:\[ɟ\]
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:\[ʄ\]
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:\[k\]
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:\[l\]
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:\[ɫ\]
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:\[ɬ\]
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:\[ɭ\]
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md):@:\[ɺ\]
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:\[ɮ\]
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:\[ʟ\]
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:\[m\]
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:\[ɱ\]
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:\[n\]
- [voiced velar nasal](voiced%20velar%20nasal.md):@:\[ŋ\]
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:\[ɲ\]
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:\[ɳ\]
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:\[ɴ\]
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:\[o\]
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:\[ɔ\]
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:\[ɔ̃\]
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:\[ø\]
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:\[ɵ\]
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:\[œ\]
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:\[œ̃\]
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:\[ɶ\]
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:\[p\]
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:\[q\]
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:\[r\]
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:\[ɾ\]
- [voiced uvular trill](voiced%20uvular%20trill.md):@:\[ʀ\]
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:\[ɽ\]
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:\[ɹ\]
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:\[ɻ\]
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:\[ʁ\]
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:\[s\]
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:\[ʃ\]
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:\[ʂ\]
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:\[t\]
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:\[ʈ\]
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:\[ts\]
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:\[tʃ\]
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:\[tɕ\]
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:\[tʂ\]
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:\[u\]
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:\[ʊ\]
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:\[ʉ\]
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:\[v\]
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:\[ʋ\]
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:\[w\]
- [labialization](labialization.md):@:\[ʷ\]
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:\[ʍ\]
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:\[ɯ\]
- [voiced velar approximant](voiced%20velar%20approximant.md):@:\[ɰ\]
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:\[x\]
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:\[χ\]
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:\[y\]
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:\[ʏ\]
- [voiced velar fricative](voiced%20velar%20fricative.md):@:\[ɣ\]
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:\[ɤ\]
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:\[ʎ\]
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:\[ɥ\]
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:\[z\]
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:\[ʒ\]
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:\[ʑ\]
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:\[ʐ\]
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:\[θ\]
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:\[ɸ\]
- [glottal stop](glottal%20stop.md):@:\[ʔ\]
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:\[ʕ\]
- [tenuis dental click](tenuis%20dental%20click.md):@:\[ǀ\]
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:\[ǁ\]
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:\[ǃ\]
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:\[ʘ\]
- [tenuis palatal click](tenuis%20palatal%20click.md):@:\[ǂ\]

<!--/pytextgen-->

<!--pytextgen generate section="d92e"--><!-- The following content is generated at 2024-01-04T20:18:00.795972+08:00. Any edits will be overridden! -->

- \[a\]:@:[open front unrounded vowel](open%20front%20unrounded%20vowel.md)
- \[ä\]:@:[open central unrounded vowel](open%20central%20unrounded%20vowel.md)
- \[ɐ\]:@:[near-open central vowel](near-open%20central%20vowel.md)
- \[ɑ\]:@:[open back unrounded vowel](open%20back%20unrounded%20vowel.md)
- \[ɑ̃\]:@:[nasalized open back unrounded vowel](nasal%20vowel.md)
- \[ɒ\]:@:[open back rounded vowel](open%20back%20rounded%20vowel.md)
- \[ʌ\]:@:[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)
- \[æ\]:@:[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)
- \[b\]:@:[voiced bilabial plosive](voiced%20bilabial%20plosive.md)
- \[ɓ\]:@:[voiced bilabial implosive](voiced%20bilabial%20implosive.md)
- \[β\]:@:[voiced bilabial fricative](voiced%20bilabial%20fricative.md)
- \[ʙ\]:@:[voiced bilabial trill](voiced%20bilabial%20trill.md)
- \[c\]:@:[voiceless palatal plosive](voiceless%20palatal%20plosive.md)
- \[ç\]:@:[voiceless palatal fricative](voiceless%20palatal%20fricative.md)
- \[ɕ\]:@:[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)
- \[d\]:@:[voiced alveolar plosive](voiced%20alveolar%20plosive.md)
- \[ɗ\]:@:[voiced alveolar implosive](voiced%20alveolar%20implosive.md)
- \[ɖ\]:@:[voiced retroflex plosive](voiced%20retroflex%20plosive.md)
- \[ð\]:@:[voiced dental fricative](voiced%20dental%20fricative.md)
- \[dz\]:@:[voiced alveolar affricate](voiced%20alveolar%20affricate.md)
- \[dʒ\]:@:[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)
- \[dʑ\]:@:[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)
- \[dʐ\]:@:[voiced retroflex affricate](voiced%20retroflex%20affricate.md)
- \[e\]:@:[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)
- \[ɘ\]:@:[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)
- \[ə\]:@:[mid central vowel](mid%20central%20vowel.md)
- \[ɚ\]:@:[r-colored mid central vowel](r-colored%20vowel.md)
- \[ɛ\]:@:[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)
- \[ɛ̃\]:@:[nasalized open-mid front unrounded vowel](nasal%20vowel.md)
- \[ɜ\]:@:[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)
- \[ɝ\]:@:[r-colored open-mid central unrounded vowel](r-colored%20vowel.md)
- \[f\]:@:[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)
- \[ɡ\]:@:[voiced velar plosive](voiced%20velar%20plosive.md)
- \[ɠ\]:@:[voiced velar implosive](voiced%20velar%20implosive.md)
- \[ɢ\]:@:[voiced uvular plosive](voiced%20uvular%20plosive.md)
- \[h\]:@:[voiceless glottal fricative](voiceless%20glottal%20fricative.md)
- \[ɦ\]:@:[voiced glottal fricative](voiced%20glottal%20fricative.md)
- \[ʰ\]:@:[aspirated consonant](aspirated%20consonant.md)
- \[ħ\]:@:[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)
- \[i\]:@:[close front unrounded vowel](close%20front%20unrounded%20vowel.md)
- \[ɪ\]:@:[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)
- \[ɨ\]:@:[close central unrounded vowel](close%20central%20unrounded%20vowel.md)
- \[j\]:@:[voiced palatal approximant](voiced%20palatal%20approximant.md)
- \[ʲ\]:@:[palatalization](palatalization%20(phonetics).md)
- \[ʝ\]:@:[voiced palatal fricative](voiced%20palatal%20fricative.md)
- \[ɟ\]:@:[voiced palatal plosive](voiced%20palatal%20plosive.md)
- \[ʄ\]:@:[voiced palatal implosive](voiced%20palatal%20implosive.md)
- \[k\]:@:[voiceless velar plosive](voiceless%20velar%20plosive.md)
- \[l\]:@:[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)
- \[ɫ\]:@:[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)
- \[ɬ\]:@:[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)
- \[ɭ\]:@:[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)
- \[ɺ\]:@:[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)
- \[ɮ\]:@:[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)
- \[ʟ\]:@:[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)
- \[m\]:@:[voiced bilabial nasal](voiced%20bilabial%20nasal.md)
- \[ɱ\]:@:[voiced labiodental nasal](voiced%20labiodental%20nasal.md)
- \[n\]:@:[voiced alveolar nasal](voiced%20alveolar%20nasal.md)
- \[ŋ\]:@:[voiced velar nasal](voiced%20velar%20nasal.md)
- \[ɲ\]:@:[voiced palatal nasal](voiced%20palatal%20nasal.md)
- \[ɳ\]:@:[voiced retroflex nasal](voiced%20retroflex%20nasal.md)
- \[ɴ\]:@:[voiced uvular nasal](voiced%20uvular%20nasal.md)
- \[o\]:@:[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
- \[ɔ\]:@:[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)
- \[ɔ̃\]:@:[nasalized open-mid back rounded vowel](nasal%20vowel.md)
- \[ø\]:@:[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
- \[ɵ\]:@:[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)
- \[œ\]:@:[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
- \[œ̃\]:@:[nasalized open-mid front rounded vowel](nasal%20vowel.md)
- \[ɶ\]:@:[open front rounded vowel](open%20front%20rounded%20vowel.md)
- \[p\]:@:[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)
- \[q\]:@:[voiceless uvular plosive](voiceless%20uvular%20plosive.md)
- \[r\]:@:[voiced alveolar trill](voiced%20alveolar%20trill.md)
- \[ɾ\]:@:[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)
- \[ʀ\]:@:[voiced uvular trill](voiced%20uvular%20trill.md)
- \[ɽ\]:@:[voiced retroflex flap](voiced%20retroflex%20flap.md)
- \[ɹ\]:@:[voiced alveolar approximant](voiced%20alveolar%20approximant.md)
- \[ɻ\]:@:[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
- \[ʁ\]:@:[voiced uvular fricative](voiced%20uvular%20fricative.md)
- \[s\]:@:[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)
- \[ʃ\]:@:[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)
- \[ʂ\]:@:[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)
- \[t\]:@:[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)
- \[ʈ\]:@:[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)
- \[ts\]:@:[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)
- \[tʃ\]:@:[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
- \[tɕ\]:@:[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)
- \[tʂ\]:@:[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)
- \[u\]:@:[close back rounded vowel](close%20back%20rounded%20vowel.md)
- \[ʊ\]:@:[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
- \[ʉ\]:@:[close central rounded vowel](close%20central%20rounded%20vowel.md)
- \[v\]:@:[voiced labiodental fricative](voiced%20labiodental%20fricative.md)
- \[ʋ\]:@:[voiced labiodental approximant](voiced%20labiodental%20approximant.md)
- \[w\]:@:[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)
- \[ʷ\]:@:[labialization](labialization.md)
- \[ʍ\]:@:[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
- \[ɯ\]:@:[close back unrounded vowel](close%20back%20unrounded%20vowel.md)
- \[ɰ\]:@:[voiced velar approximant](voiced%20velar%20approximant.md)
- \[x\]:@:[voiceless velar fricative](voiceless%20velar%20fricative.md)
- \[χ\]:@:[voiceless uvular fricative](voiceless%20uvular%20fricative.md)
- \[y\]:@:[close front rounded vowel](close%20front%20rounded%20vowel.md)
- \[ʏ\]:@:[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- \[ɣ\]:@:[voiced velar fricative](voiced%20velar%20fricative.md)
- \[ɤ\]:@:[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- \[ʎ\]:@:[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- \[ɥ\]:@:[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
- \[z\]:@:[voiced alveolar fricative](voiced%20alveolar%20fricative.md)
- \[ʒ\]:@:[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
- \[ʑ\]:@:[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)
- \[ʐ\]:@:[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
- \[θ\]:@:[voiceless dental fricative](voiceless%20dental%20fricative.md)
- \[ɸ\]:@:[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
- \[ʔ\]:@:[glottal stop](glottal%20stop.md)
- \[ʕ\]:@:[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- \[ǀ\]:@:[tenuis dental click](tenuis%20dental%20click.md)
- \[ǁ\]:@:[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)
- \[ǃ\]:@:[tenuis alveolar click](tenuis%20alveolar%20click.md)
- \[ʘ\]:@:[tenuis bilabial click](tenuis%20bilabial%20click.md)
- \[ǂ\]:@:[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/pytextgen-->

#### name–audio (letters)

<!--pytextgen generate section="5dfb"--><!-- The following content is generated at 2024-02-14T16:42:37.258792+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg)
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)
- [near-open central vowel](near-open%20central%20vowel.md):@:![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg)
- [voiced dental fricative](voiced%20dental%20fricative.md):@:![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg)
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)
- [mid central vowel](mid%20central%20vowel.md):@:![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)
- [r-colored mid central vowel](r-colored%20vowel.md):@:![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)
- [voiced velar plosive](voiced%20velar%20plosive.md):@:![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)
- [voiced velar implosive](voiced%20velar%20implosive.md):@:![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg)
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)
- [voiced velar nasal](voiced%20velar%20nasal.md):@:![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)
- [voiced uvular trill](voiced%20uvular%20trill.md):@:![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg)
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg)
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg)
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)
- [voiced velar approximant](voiced%20velar%20approximant.md):@:![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)
- [voiced velar fricative](voiced%20velar%20fricative.md):@:![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)
- [glottal stop](glottal%20stop.md):@:![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)
- [tenuis dental click](tenuis%20dental%20click.md):@:![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)
- [tenuis palatal click](tenuis%20palatal%20click.md):@:![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)

<!--/pytextgen-->

<!--pytextgen generate section="f9aa"--><!-- The following content is generated at 2024-02-14T16:42:37.178940+08:00. Any edits will be overridden! -->

- ![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg):@:[open front unrounded vowel](open%20front%20unrounded%20vowel.md)
- ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg):@:[open central unrounded vowel](open%20central%20unrounded%20vowel.md)
- ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg):@:[near-open central vowel](near-open%20central%20vowel.md)
- ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg):@:[open back unrounded vowel](open%20back%20unrounded%20vowel.md)
- ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg):@:[nasalized open back unrounded vowel](nasal%20vowel.md)
- ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg):@:[open back rounded vowel](open%20back%20rounded%20vowel.md)
- ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg):@:[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)
- ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg):@:[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)
- ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg):@:[voiced bilabial plosive](voiced%20bilabial%20plosive.md)
- ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg):@:[voiced bilabial implosive](voiced%20bilabial%20implosive.md)
- ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg):@:[voiced bilabial fricative](voiced%20bilabial%20fricative.md)
- ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg):@:[voiced bilabial trill](voiced%20bilabial%20trill.md)
- ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg):@:[voiceless palatal plosive](voiceless%20palatal%20plosive.md)
- ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg):@:[voiceless palatal fricative](voiceless%20palatal%20fricative.md)
- ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg):@:[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)
- ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg):@:[voiced alveolar plosive](voiced%20alveolar%20plosive.md)
- ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg):@:[voiced alveolar implosive](voiced%20alveolar%20implosive.md)
- ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg):@:[voiced retroflex plosive](voiced%20retroflex%20plosive.md)
- ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg):@:[voiced dental fricative](voiced%20dental%20fricative.md)
- ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg):@:[voiced alveolar affricate](voiced%20alveolar%20affricate.md)
- ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg):@:[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)
- ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg):@:[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)
- ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg):@:[voiced retroflex affricate](voiced%20retroflex%20affricate.md)
- ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg):@:[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)
- ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg):@:[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)
- ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg):@:[mid central vowel](mid%20central%20vowel.md)
- ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg):@:[r-colored mid central vowel](r-colored%20vowel.md)
- ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg):@:[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)
- ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg):@:[nasalized open-mid front unrounded vowel](nasal%20vowel.md)
- ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg):@:[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)
- ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg):@:[r-colored open-mid central unrounded vowel](r-colored%20vowel.md)
- ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg):@:[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)
- ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg):@:[voiced velar plosive](voiced%20velar%20plosive.md)
- ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg):@:[voiced velar implosive](voiced%20velar%20implosive.md)
- ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg):@:[voiced uvular plosive](voiced%20uvular%20plosive.md)
- ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg):@:[voiceless glottal fricative](voiceless%20glottal%20fricative.md)
- ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg):@:[voiced glottal fricative](voiced%20glottal%20fricative.md)
- ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg):@:[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)
- ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg):@:[close front unrounded vowel](close%20front%20unrounded%20vowel.md)
- ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg):@:[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)
- ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg):@:[close central unrounded vowel](close%20central%20unrounded%20vowel.md)
- ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg):@:[voiced palatal approximant](voiced%20palatal%20approximant.md)
- ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg):@:[voiced palatal fricative](voiced%20palatal%20fricative.md)
- ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg):@:[voiced palatal plosive](voiced%20palatal%20plosive.md)
- ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg):@:[voiced palatal implosive](voiced%20palatal%20implosive.md)
- ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg):@:[voiceless velar plosive](voiceless%20velar%20plosive.md)
- ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg):@:[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)
- ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg):@:[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)
- ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg):@:[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)
- ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg):@:[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)
- ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg):@:[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)
- ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg):@:[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)
- ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg):@:[voiced bilabial nasal](voiced%20bilabial%20nasal.md)
- ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg):@:[voiced labiodental nasal](voiced%20labiodental%20nasal.md)
- ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg):@:[voiced alveolar nasal](voiced%20alveolar%20nasal.md)
- ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg):@:[voiced velar nasal](voiced%20velar%20nasal.md)
- ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg):@:[voiced palatal nasal](voiced%20palatal%20nasal.md)
- ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg):@:[voiced retroflex nasal](voiced%20retroflex%20nasal.md)
- ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg):@:[voiced uvular nasal](voiced%20uvular%20nasal.md)
- ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg):@:[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)
- ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg):@:[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)
- ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg):@:[nasalized open-mid back rounded vowel](nasal%20vowel.md)
- ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg):@:[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)
- ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg):@:[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)
- ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg):@:[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)
- ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg):@:[nasalized open-mid front rounded vowel](nasal%20vowel.md)
- ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg):@:[open front rounded vowel](open%20front%20rounded%20vowel.md)
- ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg):@:[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)
- ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg):@:[voiceless uvular plosive](voiceless%20uvular%20plosive.md)
- ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg):@:[voiced alveolar trill](voiced%20alveolar%20trill.md)
- ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg):@:[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)
- ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg):@:[voiced uvular trill](voiced%20uvular%20trill.md)
- ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg):@:[voiced retroflex flap](voiced%20retroflex%20flap.md)
- ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg):@:[voiced alveolar approximant](voiced%20alveolar%20approximant.md)
- ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg):@:[voiced retroflex approximant](voiced%20retroflex%20approximant.md)
- ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg):@:[voiced uvular fricative](voiced%20uvular%20fricative.md)
- ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg):@:[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)
- ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg):@:[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)
- ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg):@:[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)
- ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg):@:[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)
- ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg):@:[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)
- ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg):@:[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)
- ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg):@:[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)
- ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg):@:[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)
- ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg):@:[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)
- ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg):@:[close back rounded vowel](close%20back%20rounded%20vowel.md)
- ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg):@:[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)
- ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg):@:[close central rounded vowel](close%20central%20rounded%20vowel.md)
- ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg):@:[voiced labiodental fricative](voiced%20labiodental%20fricative.md)
- ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg):@:[voiced labiodental approximant](voiced%20labiodental%20approximant.md)
- ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg):@:[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)
- ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg):@:[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)
- ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg):@:[close back unrounded vowel](close%20back%20unrounded%20vowel.md)
- ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg):@:[voiced velar approximant](voiced%20velar%20approximant.md)
- ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg):@:[voiceless velar fricative](voiceless%20velar%20fricative.md)
- ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg):@:[voiceless uvular fricative](voiceless%20uvular%20fricative.md)
- ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg):@:[close front rounded vowel](close%20front%20rounded%20vowel.md)
- ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg):@:[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)
- ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg):@:[voiced velar fricative](voiced%20velar%20fricative.md)
- ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg):@:[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)
- ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg):@:[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)
- ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav):@:[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)
- ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg):@:[voiced alveolar fricative](voiced%20alveolar%20fricative.md)
- ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg):@:[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)
- ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg):@:[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)
- ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg):@:[voiced retroflex fricative](voiced%20retroflex%20fricative.md)
- ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg):@:[voiceless dental fricative](voiceless%20dental%20fricative.md)
- ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg):@:[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)
- ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg):@:[glottal stop](glottal%20stop.md)
- ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg):@:[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)
- ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg):@:[tenuis dental click](tenuis%20dental%20click.md)
- ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg):@:[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)
- ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg):@:[tenuis alveolar click](tenuis%20alveolar%20click.md)
- ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg):@:[tenuis bilabial click](tenuis%20bilabial%20click.md)
- ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg):@:[tenuis palatal click](tenuis%20palatal%20click.md)

<!--/pytextgen-->

#### name–description (letters)

<!--pytextgen generate section="50b0"--><!-- The following content is generated at 2024-01-04T20:18:01.048113+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _h**a**t_ \[hat\]
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _br**a**_ \[bɹäː\]
- [near-open central vowel](near-open%20central%20vowel.md):@:[English](English%20language.md) _n**u**t_ \[nɐʔt\]
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _s**an**s_ [sɑ̃] "without"
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:[English](English%20language.md) _n**o**t_ \[nɒt\]
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:[English](English%20language.md) _g**u**t_ \[ɡʌt\]
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _c**a**t_ \[kʰæt\]
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:[English](English%20language.md) _a**b**ack_ \[əˈbæk\]
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:[English](English%20language.md) _**b**ody_ \[ɓʌdi\]
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:[French](French%20language.md) _**q**ui_ \[ci\] "who"
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:[English](English%20language.md) _**h**ue_ \[çʉː\]
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:[English](English%20language.md) _**d**ash_ \[ˈdæʃ\]
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"
- [voiced dental fricative](voiced%20dental%20fricative.md):@:[English](English%20language.md) _**th**is_ \[ðɪs\]
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\]
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _m**ay**_ \[meː\]
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɘːd\]
- [mid central vowel](mid%20central%20vowel.md):@:[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]
- [r-colored mid central vowel](r-colored%20vowel.md):@:[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _b**e**d_ \[bɛd\]
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɜːd\]
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɝːd\]
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:[English](English%20language.md) _**f**ill_ \[fɪɫ\]
- [voiced velar plosive](voiced%20velar%20plosive.md):@:[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]
- [voiced velar implosive](voiced%20velar%20implosive.md):@:[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:[English](English%20language.md) _**h**igh_ \[haɪ̯\]
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]
- [aspirated consonant](aspirated%20consonant.md):@:[English](English%20langugae.md) _**t**op_ \[tʰɒp\]
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _fr**ee**_ \[fɹiː\]
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:[English](English%20language.md) _b**i**t_ \[bɪʔt\]
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:[English](English%20language.md) _**y**ou_ \[juː\]
- [palatalization](palatalization%20(phonetics).md):@:[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:[English](English%20language.md) _**k**iss_ \[kʰɪs\]
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:[English](English%20language.md) _**l**et_ \[lɛt\]
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:[English](English%20language.md) _fee**l**_ \[fiːɫ\]
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md):@:[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:[English](English%20language.md) _hi**m**_ \[hɪm\]
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:[English](English%20language.md) _**n**ice_ \[naɪs\]
- [voiced velar nasal](voiced%20velar%20nasal.md):@:[English](English%20language.md) _si**ng**_ \[sɪŋ\]
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:[English](English%20language.md) _y**aw**n_ \[joːn\]
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:[English](English%20language.md) _n**o**t_ \[nɔt\]
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:[French](French%20language.md) _p**eu**_ \[pø\] "few"
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:[English](English%20language.md) _f**oo**t_ \[fɵʔt\]
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:[English](English%20language.md) _**p**ack_ \[pʰæk\]
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"
- [voiced uvular trill](voiced%20uvular%20trill.md):@:[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:[English](English%20language.md) _**s**it_ \[sɪt\]
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:[English](English%20language.md) _**t**ick_ \[tʰɪk\]
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)"
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:[English](English%20language.md) _b**oo**t_ \[bu̟ːt\]
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:[English](English%20language.md) _h**oo**k_ \[hʊʔk\]
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:[English](English%20language.md) _g**oo**se_ \[ɡʉːs\]
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:[English](English%20language.md) _**v**al**v**e_ \[væɫv\]
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:[English](English%20language.md) _**w**eep_ \[wiːp\]
- [labialization](labialization.md):@:[English](English%20language.md) _**r**eed_ \[ɹʷiːd\]
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"
- [voiced velar approximant](voiced%20velar%20approximant.md):@:[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:[German](German%20language.md) _Bu**ch**_ \[buːx\] "book"
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:[French](French%20language.md) _t**u**_ \[t̪y] "you"
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"
- [voiced velar fricative](voiced%20velar%20fricative.md):@:[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:[English](English%20language.md) _**th**in_ \[θɪn\]
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"
- [glottal stop](glottal%20stop.md):@:[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"
- [tenuis dental click](tenuis%20dental%20click.md):@:[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:[English](English%20language.md) _**tchick**_ \[ˈǁ\]
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"
- [tenuis palatal click](tenuis%20palatal%20click.md):@:[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"

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

- [nasalized](nasal%20vowel.md):@:\[◌̃\] (e.g. [ã])
- [centralized](central%20vowel.md):@:\[◌̈\] (e.g. [ä])
- [extra-short](extra-shortness.md):@:\[◌̆\] (e.g. [ă])
- [non-syllabic](diphthong.md):@:\[◌̯\] (e.g. [a̯])
- [voiceless](voicelessness.md):@:\[◌̥\] (e.g. [n̥])
- [syllabic](syllabic%20consonant.md):@:\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍])
- [dental/alveolar](dental%20consonant.md):@:\[◌̪\] (e.g. [d̪])
- [aspirated](aspirated%20consonant.md):@:\[◌ʰ\] (e.g. [kʰ])
- [ejective](ejective%20consonant.md):@:\[◌’\] (e.g. [k’])
- [long](longness%20(phonetics).md):@:\[◌ː\] (e.g. [aː])
- [half-long](half-longness%20(phonetics).md):@:\[◌ˑ\] (e.g. [aˑ])
- [primary stress](stress%20(lingustics).md):@:\[ˈ◌\] (e.g. [ˈa])
- [secondary stress](secondary%20stress.md):@:\[ˌ◌\] (e.g. [ˌa])
- [syllable break](syllable.md):@:\[.\]

<!--/pytextgen-->

<!--pytextgen generate section="94fb"--><!-- The following content is generated at 2024-01-04T20:17:59.931857+08:00. Any edits will be overridden! -->

- \[◌̃\] (e.g. [ã]):@:[nasalized](nasal%20vowel.md)
- \[◌̈\] (e.g. [ä]):@:[centralized](central%20vowel.md)
- \[◌̆\] (e.g. [ă]):@:[extra-short](extra-shortness.md)
- \[◌̯\] (e.g. [a̯]):@:[non-syllabic](diphthong.md)
- \[◌̥\] (e.g. [n̥]):@:[voiceless](voicelessness.md)
- \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]):@:[syllabic](syllabic%20consonant.md)
- \[◌̪\] (e.g. [d̪]):@:[dental/alveolar](dental%20consonant.md)
- \[◌ʰ\] (e.g. [kʰ]):@:[aspirated](aspirated%20consonant.md)
- \[◌’\] (e.g. [k’]):@:[ejective](ejective%20consonant.md)
- \[◌ː\] (e.g. [aː]):@:[long](longness%20(phonetics).md)
- \[◌ˑ\] (e.g. [aˑ]):@:[half-long](half-longness%20(phonetics).md)
- \[ˈ◌\] (e.g. [ˈa]):@:[primary stress](stress%20(lingustics).md)
- \[ˌ◌\] (e.g. [ˌa]):@:[secondary stress](secondary%20stress.md)
- \[.\]:@:[syllable break](syllable.md)

<!--/pytextgen-->

#### name–description (diacritics)

<!--pytextgen generate section="50bd"--><!-- The following content is generated at 2024-01-04T20:18:01.248419+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md):@:[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine"
- [centralized](central%20vowel.md):@:[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"
- [extra-short](extra-shortness.md):@:[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]
- [non-syllabic](diphthong.md):@:[English](English%20language.md) _co**w**_ \[kʰaʊ̯\]
- [voiceless](voicelessness.md):@:[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]
- [syllabic](syllabic%20consonant.md):@:[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]
- [dental/alveolar](dental%20consonant.md):@:[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"
- [aspirated](aspirated%20consonant.md):@:[English](English%20language.md) _**c**ome_ \[kʰɐm\]
- [ejective](ejective%20consonant.md):@:[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"
- [long](longness%20(phonetics).md):@:[English](English%20language.md) _shh!_ \[ʃː\]
- [half-long](half-longness%20(phonetics).md):@:[English](English%20language.md) _caught_ \[ˈkʰɔˑt\]
- [primary stress](stress%20(lingustics).md):@:[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]
- [secondary stress](secondary%20stress.md):@:[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]
- [syllable break](syllable.md):@:[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]

<!--/pytextgen-->
