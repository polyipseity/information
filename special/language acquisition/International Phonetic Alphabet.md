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
# import ../../scripts/utility.py.md
```

> ![official IPA chart](../../archives/Wikimedia%20Commons/IPA%20chart%202020.svg)
>
> official IPA chart

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - phonetic symbol pattern ::@:: notice that the symbol of each phonetic is somewhat related to its sound, and similarly-sounding phonetics usually have similar symbols <!--SR:!2028-07-03,1303,374!2026-09-20,374,369-->

## help

```Python
# pytextgen generate data
from asyncer import create_task_group
from itertools import chain
from pytextgen.compat.util import NULL_LOCATION, Result
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
async with create_task_group() as tg:
  results = [
    tg.soonify(memorize_table)(
      __env__.cwf_sects("958a", None),
      ("name", "symbol", "audio", "description",),
      letters,
      use_visible_len=True,
    ),
    tg.soonify(memorize_map)(
      __env__.cwf_sects(None, "059f", "d92e"),
      items_to_map(*(datum[:2] for datum in letters)),
    ),
    tg.soonify(memorize_map)(
      __env__.cwf_sects(None, "5dfb", "f9aa"),
      items_to_map(*((datum[0], datum[2]) for datum in letters if datum[2])),
    ),
    tg.soonify(memorize_map)(
      __env__.cwf_sects(None, "50b0", None),
      items_to_map(*((datum[0], datum[3]) for datum in letters)),
    ),
    tg.soonify(memorize_table)(
      __env__.cwf_sects("485d", None),
      ("name", "symbol", "description",),
      diacritics,
      use_visible_len=True,
    ),
    tg.soonify(memorize_map)(
      __env__.cwf_sects(None, "ffa2", "94fb"),
      items_to_map(*(datum[:2] for datum in diacritics)),
    ),
    tg.soonify(memorize_map)(
      __env__.cwf_sects(None, "50bd", None),
      items_to_map(*((datum[0], datum[2]) for datum in diacritics)),
    ),
  ]
return chain.from_iterable(result.value for result in results)
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
> 18. {@{sub-laminal/sub-apical ([tongue](tongue.md) underside)}@} <!--SR:!2028-06-01,976,330!2033-08-06,2895,358!2034-04-08,3101,364!2028-10-12,1374,324!2028-01-12,1162,324!2027-03-02,922,324!2030-05-07,1937,344!2032-02-02,2295,313!2029-03-07,1494,333!2028-11-09,1253,273!2030-11-23,1742,313!2035-06-16,3466,373!2029-01-08,1059,278!2032-06-12,2231,337!2026-09-26,207,281!2030-05-15,1472,250!2027-04-02,884,330!2026-09-05,732,330-->

- [consonant](consonant.md)::@::[phone](phone%20phonetics.md) articulated with partial or complete stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2034-02-19,2848,310!2029-05-13,1542,330-->
  - [airstream mechanism](airstream%20mechanism.md)::@::how the moving [air](air.md) is thrusted <!--SR:!2028-10-05,1484,338!2032-09-28,2650,363-->
    - (all) [pulmonic](pulmonic%20consonant.md) egressive::@::[air](air.md) is exhaled from the [lungs](lung.md) <!--SR:!2028-09-02,1351,333!2032-01-03,2263,358-->
    - (16%) [glottalic](glottalic%20consonant.md) egressive::@::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [glottics](glottics.md) <!--SR:!2029-04-14,1450,351!2028-08-14,1108,310-->
    - (13%) [glottalic](glottalic%20consonant.md) ingressive::@::[air](air.md) is [rarefied](rarefaction.md) by a downward movement of the [glottics](glottics.md) <!--SR:!2032-11-15,2657,391!2028-12-19,1137,270-->
    - (<2%) lingual/[velaric](velar%20consonant.md) ingressive::@::[air](air.md) is [rarefied](rarefaction.md) by a downward and sometimes rearward movement of the [tongue](tongue.md) <!--SR:!2031-12-15,2112,331!2027-02-25,488,250-->
    - ([interjection](interjection.md)) [pulmonic](pulmonic%20consonant.md) ingressive::@::[air](air.md) is inhaled into the [lungs](lung.md) <!--SR:!2030-06-01,1964,353!2028-12-24,1439,333-->
    - ([interjection](interjection.md)) lingual/[velaric](velar%20consonant.md) egressive::@::[air](air.md) is [compressed](compression%20(physics).md) by a upward movement of the [tongue](tongue.md) <!--SR:!2033-01-04,2437,299!2028-03-16,948,361-->
  - [length](gemination.md)::@::how long the articulation of a [consonant](consonant.md) lasts <!--SR:!fsrs,2034-05-07T00:00:00.000Z,2858,2858.18674294,1,2,11,0,0,2026-07-10T00:00:00.000Z!2027-08-23,1068,350-->
    - values in ascending [length](gemination.md):@:single/singleton, geminate, long geminate <!--SR:!2026-10-29,712,293-->
  - [manner of articulation](manner%20of%20articulation.md)::@::configuration and interaction of the [speech organs](speech%20organ.md) <!--SR:!2032-04-08,2194,331!2027-11-28,1137,350-->
    - [affricate](affricate%20consonant.md)::@::consonant beginning as a [plosive](plosive%20consonant.md) and releasing as a [fricative](fricative%20consonant.md) <!--SR:!2030-03-27,1645,317!2027-06-04,930,330-->
    - [approximant](approximant%20consonant.md)::@::consonant with slight stricture of the [articulators](speech%20organ.md) not narrow and precise enough to create [turbulenece](turbulence.md) <!--SR:!2034-07-27,3095,333!2029-11-30,1697,358-->
      - [lateral approximant](lateral%20consonant.md)::@::approximant with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2029-10-14,1488,284!2028-06-29,1293,324-->
      - [semivowel/glide/semiconsonant](semivowel.md)::@::approximant similar to a [vowel](vowel.md) functioning as the [syllable](syllable.md) boundary <!--SR:!2029-05-21,1388,312!2026-09-20,780,330-->
    - [flap/tap](tap%20and%20flap%20consonants.md)::@::consonant produced by a single [muscle contraction](muscle%20contraction.md) to make a single contact <!--SR:!2031-11-06,2012,298!2027-04-04,885,330-->
    - [fricative/spirant](fricative%20consonant.md)::@::consonant with continuous [turbulent](turbulence.md) and noisy airflow at articulation <!--SR:!2028-07-18,962,224!2034-03-04,2848,358-->
      - [lateral](lateral%20consonant.md)::@::fricative with airflow directed towards one or both sides of the [tongue](tongue.md) <!--SR:!2028-09-25,1407,372!2027-01-25,874,330-->
      - [sibilant](sibilant%20consonant.md)::@::fricative with airflow directed towards the [teeth](tooth.md) by the [tongue](tongue.md) <!--SR:!2026-09-17,846,341!2029-12-01,1618,351-->
    - [nasal](nasal%20consonant.md)::@::consonant with occlusion of the [vocal tract](vocal%20tract.md) with nasal airflow <!--SR:!2030-04-14,1658,317!2028-08-10,1291,372-->
    - [plosive/stop](plosive%20consonant.md)::@::consonant with occlusion of the [vocal tract](vocal%20tract.md) without nasal airflow <!--SR:!2028-05-07,1346,361!2033-03-25,2765,391-->
    - [trill](trill%20consonant.md)::@::consonant produced by vibrations between the active articulator and the passive articulator <!--SR:!2027-08-28,1090,318!2032-11-17,2684,381-->
  - [place of articulation](place%20of%20articulation.md)::@::location along the [vocal tract](vocal%20tract.md) producing the consonant <!--SR:!2026-09-24,896,324!2032-08-09,2600,378-->
    - [alveolar](alveolar%20ridge.md)::@::upper [alveolar ridge](alveolar%20ridge.md), the [gum](gums.md) line behind the upper [teeth](tooth.md) (passive) <!--SR:!2027-02-23,921,339!2028-01-28,1189,350-->
    - [aryepiglottal](pharyngeal%20consonant.md)::@::[aryepiglottic fold](aryepiglottic%20fold.md) in the [throat](throat.md) (active) <!--SR:!2026-11-04,958,353!2026-08-11,294,351-->
    - [coronal](coronal%20constant.md)::@::front of the [tongue](tongue.md) (active) <!--SR:!2026-12-19,939,313!2026-12-17,839,298-->
      - [apical](apical%20consonant.md)::@::tip of the [tongue](tongue.md) (active) <!--SR:!2028-07-13,1304,324!2032-12-05,2691,378-->
      - [laminal](laminal%20consonant.md)::@::blade of the [tongue](tongue.md), the upper front surface behind the tip (active) <!--SR:!2029-04-24,1285,253!2030-06-26,1603,260-->
      - [subapical](subapical%20consonant.md)::@::surface under the tip of the [tongue](tongue.md) (active) <!--SR:!2029-10-11,1766,344!2034-10-09,3268,373-->
    - [dental](dental%20consonant.md)::@::upper [teeth](tooth.md) (passive) <!--SR:!2027-04-06,963,313!2027-05-18,991,350-->
    - [dorsal](dorsal%20consonant.md)::@::body of the [tongue](tongue.md) (active) <!--SR:!2035-08-11,3386,353!2029-10-23,1659,333-->
    - [epiglottal](pharyngeal%20consonant.md)::@::[epiglottis](epiglottis.md), sitting at the [larynx](larynx.md) entrance (passive) <!--SR:!2033-02-28,2767,381!2031-03-14,2166,392-->
    - [glottal](glottal%20consonant.md)::@::[glottis](glottis.md), opening between the [vocal cords](vocal%20cords.md) (active) <!--SR:!2032-11-19,2391,313!2035-04-23,3423,373-->
    - [labial](labial%20consonant.md)::@::lower [lip](lip.md) (active), upper [lip](lip.md) (passive) <!--SR:!2030-05-22,1908,324!2034-02-22,3087,373-->
    - [palatal](palatal%20consonant.md)::@::[hard palate](hard%20palate.md), the front part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2027-08-25,1041,304!2027-11-25,1141,350-->
    - [pharyngeal](pharyngeal%20consonant.md)::@::base of the [tongue](tongue.md) and [throat](throat.md) (active, passive) <!--SR:!2027-04-15,952,298!2027-09-29,1084,351-->
    - [post-alveolar](post-alveolar%20consonant.md)::@::back of the upper [alveolar ridge](alveolar%20ridge.md) (passive) <!--SR:!2033-04-10,2791,377!2034-08-23,3182,391-->
    - [uvular](uvular%20consonant.md)::@::[uvula](uvula.md), hanging down at the [throat](throat.md) entrance (passive) <!--SR:!2034-10-21,3092,324!2029-11-09,1768,392-->
    - [velar](velar%20consonant.md)::@::[soft palate](soft%20palate.md), the back part of the roof of the [mouth](mouth.md) (passive) <!--SR:!2031-12-21,2044,298!2032-07-23,2584,377-->
  - [phonation](phonation.md)::@::how the [vocal cords](vocal%20folds.md) vibrate <!--SR:!2028-08-31,1309,321!2032-08-22,2615,381-->
    - [voiced](voice%20(phonetics).md)::@::the [vocal cords](vocal%20cords.md) vibrate fully <!--SR:!2033-03-13,2789,364!2033-03-12,2769,378-->
    - [voiceless](voicelessness.md)::@::the [vocal cords](vocal%20cords.md) do not vibrate <!--SR:!2033-09-08,2954,373!2035-10-09,3554,373-->
  - [voice onset time](voice%20onset%20time.md) (VOT)::@::timing of [phonation](phonation.md) <!--SR:!2029-08-09,1721,353!2027-08-23,1068,350-->
    - values in ascending [voice onset time](voice%20onset%20time.md):@:[voiced](voice%20(phonetics).md) (negative), [voiceless](voicelessness.md)/[tenius](tenius%20consonant.md) (at or near zero), [aspiriated](aspiration%20(phonetics).md) (positive) <!--SR:!2027-02-17,330,264-->
- [vowel](vowel.md)::@::[phone](phone%20(phonetics).md) articulated without any stricture in the [vocal tract](vocal%20tract.md) <!--SR:!2027-07-24,676,352!2027-11-11,1127,350-->
  - [vowel backness](vowel.md#backness)::@::position of the [tongue](tongue.md) relative to the back of the [mouth](mouth.md) <!--SR:!2028-07-17,1376,324!2033-01-23,2730,377-->
    - values in ascending [vowel backness](vowel.md#backness):@:[front](front%20vowel.md), [near-front](near-front%20vowel.md), [central](central%20vowel.md), [near-back](near-back%20vowel.md), [back](back%20vowel.md) <!--SR:!2028-05-10,1254,324-->
  - [vowel height](vowel.md#height)::@::vertical position of the [tongue](tongue.md) <!--SR:!2036-11-05,3838,378!2028-08-01,1284,371-->
    - values in descending [vowel height](vowel.md#height):@:[close](close%20vowel.md), [near-close](near-close%20vowel.md), [close-mid](close-mid%20vowel.md), [mid](mid%20vowel.md), [open-mid](open-mid%20vowel.md), [near-open](near-open%20vowel.md), [open](open%20vowel.md) <!--SR:!2033-08-28,2661,356-->
  - [vowel roundedness](roundedness.md)::@::rounding of the [lips](lip.md) <!--SR:!2028-01-20,1162,313!2032-09-17,2632,378-->
    - values in ascending [vowel roundedness](roundedness.md):@:unrounded, compressed, protruded <!--SR:!2031-01-21,2056,371-->

### transcription delimiters

Different brackets used to enclose IPA transcriptions have different meanings:

- (principal) \[[square brackets](bracket.md#square%20brackets%20or%20brackets)\]::@::[phonetic](phonetics.md) notation, board or narrow, indicating actual [pronunciation](pronunciation.md) <!--SR:!2030-12-31,1702,264!2026-12-16,910,337-->
- (principal) /[slashes](slash%20(punctuation).md)/::@::[phonemic](phoneme.md) notation, indicating features that are distinctive in the language only <!--SR:!2030-09-23,1749,293!2026-09-26,592,334-->
- (uncommon) {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}::@::[prosodic](prosody%20(linguistics).md) notation, also indicating elements of speech that are not [segments](segment%20(linguistics).md) called suprasegmentals <!--SR:!2026-10-14,569,254!2030-02-04,1625,336-->
- (uncommon) ([round brackets](bracket.md#round%20brackets%20or%20parentheses))::@::transcription of indistinguishable or unidentified [utterances](utterance.md), or [silent articulation](mouthing.md) <!--SR:!2027-07-07,713,233!2027-06-14,941,331-->
- (uncommon) (([double round brackets](bracket.md#round%20brackets%20or%20parentheses)))::@::transcription of obscured speech or description of obscuring sound <!--SR:!2033-08-30,2668,304!2026-08-06,789,304-->
- (unofficial) \[\[[double square brackets](bracket.md#square%20brackets%20or%20brackets)\]\]::@::extra-precise transcription <!--SR:!2029-04-06,1515,358!2030-06-04,1971,381-->
- (unofficial) //[double slashes](slash%20(punctuation).md)//, |[pipes](vertical%20bar.md)|, ||[double pipes](vertical%20bar.md)||, {[curly brackets](bracket.md#curly%20brackets%20or%20braces)}::@::[morphophonemic](morphophonology.md) transcription <!--SR:!2029-06-14,1226,261!2027-01-10,583,291-->
- (unofficial) ⟨[angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟩, ⟪[double angle brackets](bracket.md#angle%20brackets%20or%20chevrons)⟫::@::original [Latin](Latin.md) [orthography](orthography.md), [transliteration](transliteration.md), or IPA letters themselves <!--SR:!2031-09-19,2163,371!2027-11-07,1048,351-->

### letters

Here is a list of common IPA letters and their pronunciations:

<!--pytextgen generate section="958a"--><!-- The following content is generated at 2026-01-26T13:41:31.248267+08:00. Any edits will be overridden! -->

> | name                                                                                                  | symbol | audio                                                                                                                          | description                                                                                                      |
> | ----------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
> | [open front unrounded vowel](open%20front%20unrounded%20vowel.md)                                     | \[a\]  | ![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg)                         | [English](English%20language.md) _h**a**t_ \[hat\]                                                               |
> | [open central unrounded vowel](open%20central%20unrounded%20vowel.md)                                 | \[ä\]  | ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)                     | [English](English%20language.md) _br**a**_ \[bɹäː\]                                                              |
> | [near-open central vowel](near-open%20central%20vowel.md)                                             | \[ɐ\]  | ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)                     | [English](English%20language.md) _n**u**t_ \[nɐʔt\]                                                              |
> | [open back unrounded vowel](open%20back%20unrounded%20vowel.md)                                       | \[ɑ\]  | ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)                           | [English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\]                                                             |
> | [nasalized open back unrounded vowel](nasal%20vowel.md)                                               | \[ɑ̃\]  | ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)                                           | [French](French%20language.md) _s**an**s_ [sɑ̃] "without"                                                         |
> | [open back rounded vowel](open%20back%20rounded%20vowel.md)                                           | \[ɒ\]  | ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)                            | [English](English%20language.md) _n**o**t_ \[nɒt\]                                                               |
> | [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md)                               | \[ʌ\]  | ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)               | [English](English%20language.md) _g**u**t_ \[ɡʌt\]                                                               |
> | [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md)                           | \[æ\]  | ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)               | [English](English%20language.md) _c**a**t_ \[kʰæt\]                                                              |
> | [voiced bilabial plosive](voiced%20bilabial%20plosive.md)                                             | \[b\]  | ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)                                 | [English](English%20language.md) _a**b**ack_ \[əˈbæk\]                                                           |
> | [voiced bilabial implosive](voiced%20bilabial%20implosive.md)                                         | \[ɓ\]  | ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)                             | [English](English%20language.md) _**b**ody_ \[ɓʌdi\]                                                             |
> | [voiced bilabial fricative](voiced%20bilabial%20fricative.md)                                         | \[β\]  | ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)                             | [Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava"                                                     |
> | [voiced bilabial trill](voiced%20bilabial%20trill.md)                                                 | \[ʙ\]  | ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)                                              | [Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw"                                                      |
> | [voiceless palatal plosive](voiceless%20palatal%20plosive.md)                                         | \[c\]  | ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)                             | [French](French%20language.md) _**q**ui_ \[ci\] "who"                                                            |
> | [voiceless palatal fricative](voiceless%20palatal%20fricative.md)                                     | \[ç\]  | ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)                         | [English](English%20language.md) _**h**ue_ \[çʉː\]                                                               |
> | [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md)                     | \[ɕ\]  | ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)          | [English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\]                                                    |
> | [voiced alveolar plosive](voiced%20alveolar%20plosive.md)                                             | \[d\]  | ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)                                 | [English](English%20language.md) _**d**ash_ \[ˈdæʃ\]                                                             |
> | [voiced alveolar implosive](voiced%20alveolar%20implosive.md)                                         | \[ɗ\]  | ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)                             | [Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail"                                                |
> | [voiced retroflex plosive](voiced%20retroflex%20plosive.md)                                           | \[ɖ\]  | ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg)                                  | [Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north"                                                     |
> | [voiced dental fricative](voiced%20dental%20fricative.md)                                             | \[ð\]  | ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)                                 | [English](English%20language.md) _**th**is_ \[ðɪs\]                                                              |
> | [voiced alveolar affricate](voiced%20alveolar%20affricate.md)                                         | \[dz\] | ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg)                  | [English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\]                                                            |
> | [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md)                                 | \[dʒ\] | ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)                  | [English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\]                                                           |
> | [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md)                           | \[dʑ\] | ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)               | [Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound"                                                  |
> | [voiced retroflex affricate](voiced%20retroflex%20affricate.md)                                       | \[dʐ\] | ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)                           | [Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam"                                                         |
> | [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md)                           | \[e\]  | ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)               | [English](English%20language.md) _m**ay**_ \[meː\]                                                               |
> | [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md)                       | \[ɘ\]  | ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)           | [English](English%20language.md) _b**ir**d_ \[bɘːd\]                                                             |
> | [mid central vowel](mid%20central%20vowel.md)                                                         | \[ə\]  | ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)                                               | [English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\]                                                          |
> | [r-colored mid central vowel](r-colored%20vowel.md)                                                   | \[ɚ\]  | ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)                                                | [English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\]                                                          |
> | [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md)                             | \[ɛ\]  | ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)                 | [English](English%20language.md) _b**e**d_ \[bɛd\]                                                               |
> | [nasalized open-mid front unrounded vowel](nasal%20vowel.md)                                          | \[ɛ̃\]  | ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)                        | [French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand"                                                          |
> | [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md)                         | \[ɜ\]  | ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)             | [English](English%20language.md) _b**ir**d_ \[bɜːd\]                                                             |
> | [r-colored open-mid central unrounded vowel](r-colored%20vowel.md)                                    | \[ɝ\]  | ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)                                 | [English](English%20language.md) _b**ir**d_ \[bɝːd\]                                                             |
> | [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md)                             | \[f\]  | ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)                | [English](English%20language.md) _**f**ill_ \[fɪɫ\]                                                              |
> | [voiced velar plosive](voiced%20velar%20plosive.md)                                                   | \[ɡ\]  | ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)                                  | [English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\]                                                      |
> | [voiced velar implosive](voiced%20velar%20implosive.md)                                               | \[ɠ\]  | ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)                                   | [Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"                                                        |
> | [voiced uvular plosive](voiced%20uvular%20plosive.md)                                                 | \[ɢ\]  | ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg)                                        | [English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\]                                                          |
> | [voiceless glottal fricative](voiceless%20glottal%20fricative.md)                                     | \[h\]  | ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)                         | [English](English%20language.md) _**h**igh_ \[haɪ̯\]                                                              |
> | [voiced glottal fricative](voiced%20glottal%20fricative.md)                                           | \[ɦ\]  | ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)                               | [English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\]                                                       |
> | [aspirated consonant](aspirated%20consonant.md)                                                       | \[ʰ\]  |                                                                                                                                | [English](English%20langugae.md) _**t**op_ \[tʰɒp\]                                                              |
> | [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md)                               | \[ħ\]  | ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)                   | [English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\]                                                      |
> | [close front unrounded vowel](close%20front%20unrounded%20vowel.md)                                   | \[i\]  | ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)                       | [English](English%20language.md) _fr**ee**_ \[fɹiː\]                                                             |
> | [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md)               | \[ɪ\]  | ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)   | [English](English%20language.md) _b**i**t_ \[bɪʔt\]                                                              |
> | [close central unrounded vowel](close%20central%20unrounded%20vowel.md)                               | \[ɨ\]  | ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)                   | [Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you"                                                           |
> | [voiced palatal approximant](voiced%20palatal%20approximant.md)                                       | \[j\]  | ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)                                    | [English](English%20language.md) _**y**ou_ \[juː\]                                                               |
> | [palatalization](palatalization%20(phonetics).md)                                                     | \[ʲ\]  |                                                                                                                                | [Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive"                                                          |
> | [voiced palatal fricative](voiced%20palatal%20fricative.md)                                           | \[ʝ\]  | ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)                               | [Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock"                                                    |
> | [voiced palatal plosive](voiced%20palatal%20plosive.md)                                               | \[ɟ\]  | ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)                                   | [Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)"                  |
> | [voiced palatal implosive](voiced%20palatal%20implosive.md)                                           | \[ʄ\]  | ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)                               | [Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday"                                                 |
> | [voiceless velar plosive](voiceless%20velar%20plosive.md)                                             | \[k\]  | ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)                                 | [English](English%20language.md) _**k**iss_ \[kʰɪs\]                                                             |
> | [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md)                   | \[l\]  | ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)                | [English](English%20language.md) _**l**et_ \[lɛt\]                                                               |
> | [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md)             | \[ɫ\]  | ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) | [English](English%20language.md) _fee**l**_ \[fiːɫ\]                                                             |
> | [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md)                 | \[ɬ\]  | ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)     | [Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle"                                                    |
> | [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md)                 | \[ɭ\]  | ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)              | [French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg"                                     |
> | [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md)                                 | \[ɺ\]  |                                                                                                                                | [Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six"                                                 |
> | [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md)                       | \[ɮ\]  | ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)           | [Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat"                                                      |
> | [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md)                         | \[ʟ\]  | ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)                      | [English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\]                                                          |
> | [voiced bilabial nasal](voiced%20bilabial%20nasal.md)                                                 | \[m\]  | ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)                                              | [English](English%20language.md) _hi**m**_ \[hɪm\]                                                               |
> | [voiced labiodental nasal](voiced%20labiodental%20nasal.md)                                           | \[ɱ\]  | ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)                                        | [English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\]                                                     |
> | [voiced alveolar nasal](voiced%20alveolar%20nasal.md)                                                 | \[n\]  | ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)                                              | [English](English%20language.md) _**n**ice_ \[naɪs\]                                                             |
> | [voiced velar nasal](voiced%20velar%20nasal.md)                                                       | \[ŋ\]  | ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)                                                    | [English](English%20language.md) _si**ng**_ \[sɪŋ\]                                                              |
> | [voiced palatal nasal](voiced%20palatal%20nasal.md)                                                   | \[ɲ\]  | ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)                                                | [French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion"                                                     |
> | [voiced retroflex nasal](voiced%20retroflex%20nasal.md)                                               | \[ɳ\]  | ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)                                            | [Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn"                                                  |
> | [voiced uvular nasal](voiced%20uvular%20nasal.md)                                                     | \[ɴ\]  | ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)                                                  | [Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled"                                            |
> | [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md)                                 | \[o\]  | ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)                     | [English](English%20language.md) _y**aw**n_ \[joːn\]                                                             |
> | [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md)                                   | \[ɔ\]  | ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)                    | [English](English%20language.md) _n**o**t_ \[nɔt\]                                                               |
> | [nasalized open-mid back rounded vowel](nasal%20vowel.md)                                             | \[ɔ̃\]  | ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)                                         | [French](French%20language.md) _s**on**_ \[sɔ̃\] "sound"                                                          |
> | [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md)                               | \[ø\]  | ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)                   | [French](French%20language.md) _p**eu**_ \[pø\] "few"                                                            |
> | [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md)                           | \[ɵ\]  | ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)               | [English](English%20language.md) _f**oo**t_ \[fɵʔt\]                                                             |
> | [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md)                                 | \[œ\]  | ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)                     | [French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young"                                                       |
> | [nasalized open-mid front rounded vowel](nasal%20vowel.md)                                            | \[œ̃\]  | ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)                                | [French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown"                                                        |
> | [open front rounded vowel](open%20front%20rounded%20vowel.md)                                         | \[ɶ\]  | ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)                             | [Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green"                                                     |
> | [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md)                                       | \[p\]  | ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)                           | [English](English%20language.md) _**p**ack_ \[pʰæk\]                                                             |
> | [voiceless uvular plosive](voiceless%20uvular%20plosive.md)                                           | \[q\]  | ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)                               | [Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat"                                                     |
> | [voiced alveolar trill](voiced%20alveolar%20trill.md)                                                 | \[r\]  | ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)                                              | [Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog"                                                     |
> | [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) | \[ɾ\]  | ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)                            | [Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive"                                                |
> | [voiced uvular trill](voiced%20uvular%20trill.md)                                                     | \[ʀ\]  | ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)                                                  | [German](German%20language.md) _**r**ot_ \[ʀoːt\] "red"                                                          |
> | [voiced retroflex flap](voiced%20retroflex%20flap.md)                                                 | \[ɽ\]  | ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)                                              | [Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf"                                                   |
> | [voiced alveolar approximant](voiced%20alveolar%20approximant.md)                                     | \[ɹ\]  | ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)                                  | [Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest"                                       |
> | [voiced retroflex approximant](voiced%20retroflex%20approximant.md)                                   | \[ɻ\]  | ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg)                               | [Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat"                                                   |
> | [voiced uvular fricative](voiced%20uvular%20fricative.md)                                             | \[ʁ\]  | ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)                                 | [French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay"                                                  |
> | [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md)                                   | \[s\]  | ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)                        | [English](English%20language.md) _**s**it_ \[sɪt\]                                                               |
> | [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md)                           | \[ʃ\]  | ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)             | [English](English%20language.md) _**sh**eep_ \[ˈʃiːp\]                                                           |
> | [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md)                                 | \[ʂ\]  | ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)                      | [Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle"                                                       |
> | [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md)                                       | \[t\]  | ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)                           | [English](English%20language.md) _**t**ick_ \[tʰɪk\]                                                             |
> | [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md)                                     | \[ʈ\]  | ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg)                            | [Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card"                                                  |
> | [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md)                                   | \[ts\] | ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg)            | [English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\]                                                            |
> | [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md)                           | \[tʃ\] | ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)            | [English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\]                                                           |
> | [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md)                     | \[tɕ\] | ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)         | [Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)"                      |
> | [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md)                                 | \[tʂ\] | ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)                     | [Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)" |
> | [close back rounded vowel](close%20back%20rounded%20vowel.md)                                         | \[u\]  | ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)                             | [English](English%20language.md) _b**oo**t_ \[bu̟ːt\]                                                             |
> | [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md)                     | \[ʊ\]  | ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)         | [English](English%20language.md) _h**oo**k_ \[hʊʔk\]                                                             |
> | [close central rounded vowel](close%20central%20rounded%20vowel.md)                                   | \[ʉ\]  | ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)                       | [English](English%20language.md) _g**oo**se_ \[ɡʉːs\]                                                            |
> | [voiced labiodental fricative](voiced%20labiodental%20fricative.md)                                   | \[v\]  | ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)                      | [English](English%20language.md) _**v**al**v**e_ \[væɫv\]                                                        |
> | [voiced labiodental approximant](voiced%20labiodental%20approximant.md)                               | \[ʋ\]  | ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)                            | [Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby"                                               |
> | [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md)                             | \[w\]  | ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)                  | [English](English%20language.md) _**w**eep_ \[wiːp\]                                                             |
> | [labialization](labialization.md)                                                                     | \[ʷ\]  |                                                                                                                                | [English](English%20language.md) _**r**eed_ \[ɹʷiːd\]                                                            |
> | [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md)                           | \[ʍ\]  | ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)                | [English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\]                                                            |
> | [close back unrounded vowel](close%20back%20unrounded%20vowel.md)                                     | \[ɯ\]  | ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)                         | [Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow"                                                     |
> | [voiced velar approximant](voiced%20velar%20approximant.md)                                           | \[ɰ\]  | ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)                               | [Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine"                                                         |
> | [voiceless velar fricative](voiceless%20velar%20fricative.md)                                         | \[x\]  | ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)                             | [German](German%20language.md) _Bu**ch**_ \[buːx\] "book"                                                        |
> | [voiceless uvular fricative](voiceless%20uvular%20fricative.md)                                       | \[χ\]  | ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)                           | [French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very"                                                         |
> | [close front rounded vowel](close%20front%20rounded%20vowel.md)                                       | \[y\]  | ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)                           | [French](French%20language.md) _t**u**_ \[t̪y] "you"                                                              |
> | [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md)                   | \[ʏ\]  | ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)       | [German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect"                                               |
> | [voiced velar fricative](voiced%20velar%20fricative.md)                                               | \[ɣ\]  | ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)                                   | [Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend"                                                 |
> | [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md)                             | \[ɤ\]  | ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)                 | [Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry"                                                     |
> | [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md)                     | \[ʎ\]  | ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)                  | [English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\]                                                        |
> | [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md)                         | \[ɥ\]  | ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)          | [French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm"                                                    |
> | [voiced alveolar fricative](voiced%20alveolar%20fricative.md)                                         | \[z\]  | ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)                              | [English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\]                                                              |
> | [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md)                                 | \[ʒ\]  | ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)                   | [English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\]                                                         |
> | [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md)                           | \[ʑ\]  | ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)                | [Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire"                                               |
> | [voiced retroflex fricative](voiced%20retroflex%20fricative.md)                                       | \[ʐ\]  | ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)                            | [Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife"                                                     |
> | [voiceless dental fricative](voiceless%20dental%20fricative.md)                                       | \[θ\]  | ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)                           | [English](English%20language.md) _**th**in_ \[θɪn\]                                                              |
> | [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md)                                   | \[ɸ\]  | ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)                       | [Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay"                                            |
> | [glottal stop](glottal%20stop.md)                                                                     | \[ʔ\]  | ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)                                                         | [English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\]                                                               |
> | [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md)                                     | \[ʕ\]  | ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)                         | [Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion"                                               |
> | [tenuis dental click](tenuis%20dental%20click.md)                                                     | \[ǀ\]  | ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)                                                  | [English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\]                                                      |
> | [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md)                               | \[ǁ\]  | ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)                            | [English](English%20language.md) _**tchick**_ \[ˈǁ\]                                                             |
> | [tenuis alveolar click](tenuis%20alveolar%20click.md)                                                 | \[ǃ\]  | ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)                                          | [Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat"                                               |
> | [tenuis bilabial click](tenuis%20bilabial%20click.md)                                                 | \[ʘ\]  | ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)                                       | [ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two"                                                        |
> | [tenuis palatal click](tenuis%20palatal%20click.md)                                                   | \[ǂ\]  | ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)                                         | [Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth"                        |

<!--/pytextgen-->

#### name–symbol (letters)

<!--pytextgen generate section="059f"--><!-- The following content is generated at 2024-01-04T20:18:01.221392+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:\[a\] <!--SR:!2032-07-17,2578,378-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:\[ä\] <!--SR:!2030-10-07,1918,357-->
- [near-open central vowel](near-open%20central%20vowel.md):@:\[ɐ\] <!--SR:!2030-08-05,1855,371-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:\[ɑ\] <!--SR:!2030-07-31,2016,381-->
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:\[ɑ̃\] <!--SR:!2030-11-23,1959,361-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:\[ɒ\] <!--SR:!2030-10-03,2064,378-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:\[ʌ\] <!--SR:!2029-02-15,1480,360-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:\[æ\] <!--SR:!2033-07-11,2874,381-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:\[b\] <!--SR:!2031-07-10,2130,361-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:\[ɓ\] <!--SR:!fsrs,2034-04-11T05:53:24.480Z,2857,2857.16373824,1,2,10,0,0,2026-06-15T05:53:24.480Z-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:\[β\] <!--SR:!2027-04-23,873,338-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:\[ʙ\] <!--SR:!2031-01-26,2002,360-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:\[c\] <!--SR:!2029-07-16,1464,332-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:\[ç\] <!--SR:!2028-05-29,746,231-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:\[ɕ\] <!--SR:!fsrs,2028-02-18T03:37:45.625Z,613,612.78160087,4.48359968,2,9,0,0,2026-06-15T03:37:45.625Z-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:\[d\] <!--SR:!2028-01-29,1122,331-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:\[ɗ\] <!--SR:!2029-04-27,1480,373-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:\[ɖ\] <!--SR:!2029-02-23,1488,361-->
- [voiced dental fricative](voiced%20dental%20fricative.md):@:\[ð\] <!--SR:!2029-04-21,1395,317-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:\[dz\] <!--SR:!2028-07-18,1289,372-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:\[dʒ\] <!--SR:!fsrs,2031-04-14T00:00:00.000Z,1752,1752.37043446,2.45526587,2,10,0,0,2026-06-27T00:00:00.000Z-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:\[dʑ\] <!--SR:!2027-09-25,1032,353-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:\[dʐ\] <!--SR:!2031-12-30,2112,354-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:\[e\] <!--SR:!2031-08-24,2109,337-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:\[ɘ\] <!--SR:!2027-08-20,1044,337-->
- [mid central vowel](mid%20central%20vowel.md):@:\[ə\] <!--SR:!2029-11-24,1611,351-->
- [r-colored mid central vowel](r-colored%20vowel.md):@:\[ɚ\] <!--SR:!2029-04-27,1505,372-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:\[ɛ\] <!--SR:!2029-06-17,1544,372-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:\[ɛ̃\] <!--SR:!2029-12-20,1552,321-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:\[ɜ\] <!--SR:!2031-03-09,2018,371-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:\[ɝ\] <!--SR:!2027-07-11,994,351-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:\[f\] <!--SR:!2028-08-18,1298,372-->
- [voiced velar plosive](voiced%20velar%20plosive.md):@:\[ɡ\] <!--SR:!2030-09-27,1696,313-->
- [voiced velar implosive](voiced%20velar%20implosive.md):@:\[ɠ\] <!--SR:!2028-09-14,1363,358-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:\[ɢ\] <!--SR:!2031-06-27,1958,311-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:\[h\] <!--SR:!2026-10-26,318,351-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:\[ɦ\] <!--SR:!2030-05-12,1802,357-->
- [aspirated consonant](aspirated%20consonant.md):@:\[ʰ\] <!--SR:!2027-11-17,1026,312-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:\[ħ\] <!--SR:!2029-05-09,1369,311-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:\[i\] <!--SR:!2028-02-21,1116,291-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:\[ɪ\] <!--SR:!2029-11-08,1752,393-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:\[ɨ\] <!--SR:!2028-06-11,1261,372-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:\[j\] <!--SR:!2027-06-25,963,331-->
- [palatalization](palatalization%20(phonetics).md):@:\[ʲ\] <!--SR:!2032-12-28,2715,381-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:\[ʝ\] <!--SR:!2026-07-31,343,201-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:\[ɟ\] <!--SR:!2027-05-13,978,341-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:\[ʄ\] <!--SR:!2026-11-13,813,351-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:\[k\] <!--SR:!2026-08-24,810,339-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:\[l\] <!--SR:!2029-12-24,1547,334-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:\[ɫ\] <!--SR:!2030-07-30,1851,371-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:\[ɬ\] <!--SR:!2027-04-17,681,311-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:\[ɭ\] <!--SR:!2026-12-13,726,354-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md):@:\[ɺ\] <!--SR:!2031-01-03,1697,300-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:\[ɮ\] <!--SR:!2027-07-28,970,354-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:\[ʟ\] <!--SR:!2029-08-18,1309,293-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:\[m\] <!--SR:!fsrs,2030-06-23T00:00:00.000Z,1442,1442.31400671,4.70301587,2,10,0,0,2026-07-12T00:00:00.000Z-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:\[ɱ\] <!--SR:!2029-04-09,1447,351-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:\[n\] <!--SR:!2034-09-26,3117,351-->
- [voiced velar nasal](voiced%20velar%20nasal.md):@:\[ŋ\] <!--SR:!2029-01-27,1413,339-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:\[ɲ\] <!--SR:!2028-09-29,1190,314-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:\[ɳ\] <!--SR:!2027-03-30,952,339-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:\[ɴ\] <!--SR:!fsrs,2031-07-15T05:40:16.970Z,1856,1855.97374873,2.56765337,2,11,0,0,2026-06-15T05:40:16.970Z-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:\[o\] <!--SR:!2027-01-29,939,371-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:\[ɔ\] <!--SR:!2028-01-20,1076,354-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:\[ɔ̃\] <!--SR:!2027-08-05,703,337-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:\[ø\] <!--SR:!2027-03-01,448,237-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:\[ɵ\] <!--SR:!2026-10-20,560,314-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:\[œ\] <!--SR:!2026-07-14,621,293-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:\[œ̃\] <!--SR:!2026-08-16,133,281-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:\[ɶ\] <!--SR:!2027-03-07,334,311-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:\[p\] <!--SR:!2030-02-23,1391,251-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:\[q\] <!--SR:!2028-03-14,873,231-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:\[r\] <!--SR:!2032-11-02,2519,351-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:\[ɾ\] <!--SR:!2032-07-03,2547,391-->
- [voiced uvular trill](voiced%20uvular%20trill.md):@:\[ʀ\] <!--SR:!2031-02-07,2010,360-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:\[ɽ\] <!--SR:!2028-10-29,1419,320-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:\[ɹ\] <!--SR:!2027-09-05,978,311-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:\[ɻ\] <!--SR:!2026-08-31,731,331-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:\[ʁ\] <!--SR:!2027-02-11,589,353-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:\[s\] <!--SR:!2033-03-27,2787,381-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:\[ʃ\] <!--SR:!2026-08-02,647,291-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:\[ʂ\] <!--SR:!2027-12-12,1073,354-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:\[t\] <!--SR:!2030-05-05,1947,381-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:\[ʈ\] <!--SR:!2027-03-20,631,273-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:\[ts\] <!--SR:!2029-11-16,1567,375-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:\[tʃ\] <!--SR:!2026-08-01,64,291-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:\[tɕ\] <!--SR:!2028-12-18,1234,374-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:\[tʂ\] <!--SR:!2029-11-05,1556,375-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:\[u\] <!--SR:!2026-08-26,571,334-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:\[ʊ\] <!--SR:!2028-04-22,1100,356-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:\[ʉ\] <!--SR:!2026-07-24,170,331-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:\[v\] <!--SR:!2030-09-07,1920,395-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:\[ʋ\] <!--SR:!2026-10-10,679,335-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:\[w\] <!--SR:!fsrs,2027-07-13T06:00:20.266Z,393,392.87077442,3.24197837,2,8,0,0,2026-06-15T06:00:20.266Z-->
- [labialization](labialization.md):@:\[ʷ\] <!--SR:!2030-07-13,1788,394-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:\[ʍ\] <!--SR:!2027-05-19,691,256-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:\[ɯ\] <!--SR:!2027-06-27,630,330-->
- [voiced velar approximant](voiced%20velar%20approximant.md):@:\[ɰ\] <!--SR:!fsrs,2026-08-06T05:52:40.562Z,52,51.5290599,8.51646777,2,6,0,0,2026-06-15T05:52:40.562Z-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:\[x\] <!--SR:!fsrs,2026-11-21T03:37:38.558Z,159,159.23409015,6.40045673,2,7,0,0,2026-06-15T03:37:38.558Z-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:\[χ\] <!--SR:!2028-06-06,739,314-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:\[y\] <!--SR:!2030-04-25,1688,376-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:\[ʏ\] <!--SR:!2027-07-11,640,330-->
- [voiced velar fricative](voiced%20velar%20fricative.md):@:\[ɣ\] <!--SR:!2027-01-28,570,236-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:\[ɤ\] <!--SR:!2026-12-14,214,210-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:\[ʎ\] <!--SR:!2027-12-22,664,275-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:\[ɥ\] <!--SR:!2027-01-02,335,234-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:\[z\] <!--SR:!2031-04-23,2099,395-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:\[ʒ\] <!--SR:!2028-05-23,1033,295-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:\[ʑ\] <!--SR:!2026-07-23,169,289-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:\[ʐ\] <!--SR:!2026-11-24,510,330-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:\[θ\] <!--SR:!2029-04-18,1391,376-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:\[ɸ\] <!--SR:!2027-04-12,676,354-->
- [glottal stop](glottal%20stop.md):@:\[ʔ\] <!--SR:!2029-12-28,1416,370-->
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:\[ʕ\] <!--SR:!2028-12-23,1053,315-->
- [tenuis dental click](tenuis%20dental%20click.md):@:\[ǀ\] <!--SR:!2026-11-07,499,316-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:\[ǁ\] <!--SR:!2030-02-01,1627,375-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:\[ǃ\] <!--SR:!2027-07-30,647,330-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:\[ʘ\] <!--SR:!2029-06-08,1131,369-->
- [tenuis palatal click](tenuis%20palatal%20click.md):@:\[ǂ\] <!--SR:!2026-12-11,484,336-->

<!--/pytextgen-->

<!--pytextgen generate section="d92e"--><!-- The following content is generated at 2024-01-04T20:18:00.795972+08:00. Any edits will be overridden! -->

- \[a\]:@:[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!2028-10-11,1385,358-->
- \[ä\]:@:[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!2027-07-08,1042,373-->
- \[ɐ\]:@:[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!2028-06-25,951,351-->
- \[ɑ\]:@:[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2026-07-29,764,337-->
- \[ɑ̃\]:@:[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2027-05-07,962,339-->
- \[ɒ\]:@:[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2029-11-27,1382,272-->
- \[ʌ\]:@:[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!2026-11-01,465,214-->
- \[æ\]:@:[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!2028-11-22,1357,337-->
- \[b\]:@:[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!2033-04-02,2788,378-->
- \[ɓ\]:@:[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!2029-02-10,1447,371-->
- \[β\]:@:[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2031-09-22,2251,371-->
- \[ʙ\]:@:[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2028-03-13,1243,351-->
- \[c\]:@:[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2026-08-04,760,321-->
- \[ç\]:@:[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!2027-02-28,822,291-->
- \[ɕ\]:@:[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!2027-02-07,590,353-->
- \[d\]:@:[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!2030-01-13,1823,392-->
- \[ɗ\]:@:[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2027-08-20,1021,351-->
- \[ɖ\]:@:[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!2027-10-04,1081,341-->
- \[ð\]:@:[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2026-10-27,319,351-->
- \[dz\]:@:[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2028-11-17,1349,374-->
- \[dʒ\]:@:[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2030-06-11,1651,297-->
- \[dʑ\]:@:[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!2027-03-12,957,351-->
- \[dʐ\]:@:[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2029-01-19,1395,374-->
- \[e\]:@:[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2028-09-21,1306,374-->
- \[ɘ\]:@:[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!2031-02-19,2017,357-->
- \[ə\]:@:[mid central vowel](mid%20central%20vowel.md) <!--SR:!2027-01-28,704,301-->
- \[ɚ\]:@:[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2029-07-17,1408,332-->
- \[ɛ\]:@:[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!2030-05-16,1473,321-->
- \[ɛ̃\]:@:[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!2026-08-05,290,351-->
- \[ɜ\]:@:[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!2028-09-03,1025,312-->
- \[ɝ\]:@:[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!2029-07-15,1501,351-->
- \[f\]:@:[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2030-10-29,1972,338-->
- \[ɡ\]:@:[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2033-01-05,2722,380-->
- \[ɠ\]:@:[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2029-11-20,1629,351-->
- \[ɢ\]:@:[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!2032-04-09,2500,377-->
- \[h\]:@:[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!2031-11-27,2211,368-->
- \[ɦ\]:@:[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2030-07-23,1853,357-->
- \[ʰ\]:@:[aspirated consonant](aspirated%20consonant.md) <!--SR:!2034-03-11,2843,331-->
- \[ħ\]:@:[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!fsrs,2028-11-15T00:00:00.000Z,861,860.84107693,2.08064087,2,9,0,0,2026-07-08T00:00:00.000Z-->
- \[i\]:@:[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!2027-04-04,942,374-->
- \[ɪ\]:@:[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2029-05-22,1489,374-->
- \[ɨ\]:@:[close central unrounded vowel](close%20central%20unrounded%20vowel.md) <!--SR:!2029-07-01,1299,271-->
- \[j\]:@:[voiced palatal approximant](voiced%20palatal%20approximant.md) <!--SR:!2027-07-18,999,351-->
- \[ʲ\]:@:[palatalization](palatalization%20(phonetics).md) <!--SR:!2027-05-16,950,351-->
- \[ʝ\]:@:[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!2027-12-05,1129,341-->
- \[ɟ\]:@:[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2027-02-28,336,297-->
- \[ʄ\]:@:[voiced palatal implosive](voiced%20palatal%20implosive.md) <!--SR:!2027-02-19,602,211-->
- \[k\]:@:[voiceless velar plosive](voiceless%20velar%20plosive.md) <!--SR:!2031-02-07,1736,292-->
- \[l\]:@:[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) <!--SR:!2027-01-15,659,231-->
- \[ɫ\]:@:[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) <!--SR:!2028-03-24,974,271-->
- \[ɬ\]:@:[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2029-02-05,1291,331-->
- \[ɭ\]:@:[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!2027-12-07,973,311-->
- \[ɺ\]:@:[voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md) <!--SR:!2027-05-06,884,340-->
- \[ɮ\]:@:[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!2031-09-22,1967,301-->
- \[ʟ\]:@:[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!2031-05-21,1932,317-->
- \[m\]:@:[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2028-10-30,1354,373-->
- \[ɱ\]:@:[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2026-09-24,707,314-->
- \[n\]:@:[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!fsrs,2031-10-26T00:00:00.000Z,1956,1956.47634605,1.63109087,2,11,0,0,2026-06-18T00:00:00.000Z-->
- \[ŋ\]:@:[voiced velar nasal](voiced%20velar%20nasal.md) <!--SR:!fsrs,2029-12-06T04:00:35.758Z,1270,1269.96989831,4.90680188,2,10,0,0,2026-06-15T04:00:35.758Z-->
- \[ɲ\]:@:[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2027-05-06,914,353-->
- \[ɳ\]:@:[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2029-01-28,1311,311-->
- \[ɴ\]:@:[voiced uvular nasal](voiced%20uvular%20nasal.md) <!--SR:!2027-12-29,1059,354-->
- \[o\]:@:[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) <!--SR:!2032-10-20,2656,377-->
- \[ɔ\]:@:[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) <!--SR:!2027-04-01,301,271-->
- \[ɔ̃\]:@:[nasalized open-mid back rounded vowel](nasal%20vowel.md) <!--SR:!2027-01-21,695,272-->
- \[ø\]:@:[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) <!--SR:!2027-12-27,663,271-->
- \[ɵ\]:@:[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2027-11-09,860,301-->
- \[œ\]:@:[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) <!--SR:!2026-10-18,731,313-->
- \[œ̃\]:@:[nasalized open-mid front rounded vowel](nasal%20vowel.md) <!--SR:!2031-04-16,2062,358-->
- \[ɶ\]:@:[open front rounded vowel](open%20front%20rounded%20vowel.md) <!--SR:!2026-09-15,764,331-->
- \[p\]:@:[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!2028-06-01,1309,351-->
- \[q\]:@:[voiceless uvular plosive](voiceless%20uvular%20plosive.md) <!--SR:!fsrs,2028-06-14T05:52:38.322Z,730,730.22869558,2.45526587,2,9,0,0,2026-06-15T05:52:38.322Z-->
- \[r\]:@:[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2027-11-30,1181,371-->
- \[ɾ\]:@:[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2026-08-13,735,352-->
- \[ʀ\]:@:[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2028-11-19,1169,314-->
- \[ɽ\]:@:[voiced retroflex flap](voiced%20retroflex%20flap.md) <!--SR:!2026-10-23,261,331-->
- \[ɹ\]:@:[voiced alveolar approximant](voiced%20alveolar%20approximant.md) <!--SR:!2026-12-25,847,320-->
- \[ɻ\]:@:[voiced retroflex approximant](voiced%20retroflex%20approximant.md) <!--SR:!2026-12-09,514,280-->
- \[ʁ\]:@:[voiced uvular fricative](voiced%20uvular%20fricative.md) <!--SR:!2027-02-24,846,354-->
- \[s\]:@:[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2032-02-07,2343,337-->
- \[ʃ\]:@:[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) <!--SR:!2029-07-24,1489,321-->
- \[ʂ\]:@:[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2028-02-12,1183,340-->
- \[t\]:@:[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!2028-07-03,1316,374-->
- \[ʈ\]:@:[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!2027-08-30,885,314-->
- \[ts\]:@:[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) <!--SR:!2028-09-25,1325,340-->
- \[tʃ\]:@:[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) <!--SR:!2029-01-23,1230,271-->
- \[tɕ\]:@:[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) <!--SR:!2029-08-15,1370,294-->
- \[tʂ\]:@:[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!2027-01-13,827,354-->
- \[u\]:@:[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2031-01-10,1996,331-->
- \[ʊ\]:@:[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) <!--SR:!2027-06-29,936,354-->
- \[ʉ\]:@:[close central rounded vowel](close%20central%20rounded%20vowel.md) <!--SR:!2029-07-18,1337,279-->
- \[v\]:@:[voiced labiodental fricative](voiced%20labiodental%20fricative.md) <!--SR:!2029-02-03,1441,371-->
- \[ʋ\]:@:[voiced labiodental approximant](voiced%20labiodental%20approximant.md) <!--SR:!2029-11-20,1607,351-->
- \[w\]:@:[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2028-07-23,1279,373-->
- \[ʷ\]:@:[labialization](labialization.md) <!--SR:!2032-11-29,2671,391-->
- \[ʍ\]:@:[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) <!--SR:!2027-01-23,264,254-->
- \[ɯ\]:@:[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!2029-10-19,1539,293-->
- \[ɰ\]:@:[voiced velar approximant](voiced%20velar%20approximant.md) <!--SR:!2027-06-26,886,311-->
- \[x\]:@:[voiceless velar fricative](voiceless%20velar%20fricative.md) <!--SR:!2028-12-14,1268,320-->
- \[χ\]:@:[voiceless uvular fricative](voiceless%20uvular%20fricative.md) <!--SR:!2029-06-28,1463,280-->
- \[y\]:@:[close front rounded vowel](close%20front%20rounded%20vowel.md) <!--SR:!2027-01-28,441,329-->
- \[ʏ\]:@:[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) <!--SR:!2027-06-09,617,330-->
- \[ɣ\]:@:[voiced velar fricative](voiced%20velar%20fricative.md) <!--SR:!2026-07-24,266,289-->
- \[ɤ\]:@:[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) <!--SR:!2026-11-19,507,330-->
- \[ʎ\]:@:[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) <!--SR:!2027-05-25,566,290-->
- \[ɥ\]:@:[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) <!--SR:!2026-11-16,338,256-->
- \[z\]:@:[voiced alveolar fricative](voiced%20alveolar%20fricative.md) <!--SR:!2027-07-16,895,356-->
- \[ʒ\]:@:[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) <!--SR:!2027-07-15,905,355-->
- \[ʑ\]:@:[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) <!--SR:!2029-07-28,1485,376-->
- \[ʐ\]:@:[voiced retroflex fricative](voiced%20retroflex%20fricative.md) <!--SR:!2027-02-16,691,334-->
- \[θ\]:@:[voiceless dental fricative](voiceless%20dental%20fricative.md) <!--SR:!2027-07-14,642,330-->
- \[ɸ\]:@:[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) <!--SR:!2031-02-10,2044,395-->
- \[ʔ\]:@:[glottal stop](glottal%20stop.md) <!--SR:!2026-09-10,367,369-->
- \[ʕ\]:@:[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) <!--SR:!2026-07-18,152,330-->
- \[ǀ\]:@:[tenuis dental click](tenuis%20dental%20click.md) <!--SR:!2028-02-26,974,354-->
- \[ǁ\]:@:[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) <!--SR:!2030-02-09,1631,376-->
- \[ǃ\]:@:[tenuis alveolar click](tenuis%20alveolar%20click.md) <!--SR:!2028-09-11,861,349-->
- \[ʘ\]:@:[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2029-12-28,1598,376-->
- \[ǂ\]:@:[tenuis palatal click](tenuis%20palatal%20click.md) <!--SR:!fsrs,2030-05-16T05:52:43.190Z,1431,1431.24226655,3.05466587,2,10,0,0,2026-06-15T05:52:43.190Z-->

<!--/pytextgen-->

#### name–audio (letters)

<!--pytextgen generate section="5dfb"--><!-- The following content is generated at 2024-02-14T16:42:37.258792+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg) <!--SR:!2029-09-08,1555,351-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg) <!--SR:!2026-12-16,315,264-->
- [near-open central vowel](near-open%20central%20vowel.md):@:![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg) <!--SR:!2026-09-15,736,264-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg) <!--SR:!2028-02-26,1302,333-->
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg) <!--SR:!2029-05-06,1401,311-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg) <!--SR:!2028-07-12,1303,324-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg) <!--SR:!2031-09-06,1981,293-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg) <!--SR:!2031-10-22,2209,358-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg) <!--SR:!2026-09-09,315,338-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg) <!--SR:!2027-09-14,1059,341-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg) <!--SR:!2030-11-29,1954,357-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg) <!--SR:!2030-03-22,1647,321-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg) <!--SR:!2028-07-12,1191,311-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg) <!--SR:!2027-01-27,800,291-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg) <!--SR:!2028-02-15,1184,318-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg) <!--SR:!2028-03-22,1292,371-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg) <!--SR:!2028-02-24,1195,324-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg) <!--SR:!2030-04-12,1546,334-->
- [voiced dental fricative](voiced%20dental%20fricative.md):@:![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg) <!--SR:!2026-08-21,711,278-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg) <!--SR:!2026-07-15,634,238-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg) <!--SR:!2027-03-29,796,278-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg) <!--SR:!2029-09-29,1467,313-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg) <!--SR:!2026-09-03,282,264-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2027-01-22,939,351-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2028-06-03,981,251-->
- [mid central vowel](mid%20central%20vowel.md):@:![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg) <!--SR:!2027-07-13,885,292-->
- [r-colored mid central vowel](r-colored%20vowel.md):@:![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2027-03-06,348,298-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg) <!--SR:!2027-06-01,892,278-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg) <!--SR:!2032-01-02,2069,332-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg) <!--SR:!2034-05-29,3111,391-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg) <!--SR:!2031-01-23,1814,334-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg) <!--SR:!2027-05-03,976,338-->
- [voiced velar plosive](voiced%20velar%20plosive.md):@:![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg) <!--SR:!2029-03-20,1362,311-->
- [voiced velar implosive](voiced%20velar%20implosive.md):@:![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg) <!--SR:!2031-09-09,2061,331-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg) <!--SR:!2033-06-27,2690,353-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg) <!--SR:!2027-02-10,317,258-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg) <!--SR:!2028-07-19,1140,314-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg) <!--SR:!2031-12-01,2037,334-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg) <!--SR:!2026-12-30,804,264-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg) <!--SR:!2027-10-14,1031,354-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg) <!--SR:!2026-07-21,704,331-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg) <!--SR:!2027-05-22,910,354-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg) <!--SR:!2026-10-30,286,258-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg) <!--SR:!2027-11-21,1013,297-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg) <!--SR:!2028-11-06,1250,244-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg) <!--SR:!2029-11-28,1549,333-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg) <!--SR:!2029-07-26,1463,298-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg) <!--SR:!2029-05-30,1433,308-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg) <!--SR:!2028-02-13,1182,341-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg) <!--SR:!2028-07-12,1268,371-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg) <!--SR:!2027-06-14,943,351-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg) <!--SR:!2027-03-07,867,351-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg) <!--SR:!2026-07-20,707,258-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg) <!--SR:!2029-05-23,1369,273-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg) <!--SR:!2026-08-31,829,338-->
- [voiced velar nasal](voiced%20velar%20nasal.md):@:![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg) <!--SR:!2026-08-10,645,312-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg) <!--SR:!2027-04-04,842,314-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg) <!--SR:!2027-09-12,902,260-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg) <!--SR:!2027-08-12,637,190-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg) <!--SR:!2027-02-06,865,291-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg) <!--SR:!2031-09-27,2061,318-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg) <!--SR:!2026-08-28,761,293-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg) <!--SR:!2027-04-12,832,291-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg) <!--SR:!2029-06-08,1426,298-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg) <!--SR:!2027-03-05,911,304-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg) <!--SR:!2027-02-28,864,353-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg) <!--SR:!2029-01-29,1312,311-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg) <!--SR:!2030-04-22,1450,253-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg) <!--SR:!2027-07-06,966,331-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg) <!--SR:!2028-11-22,1294,284-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg) <!--SR:!2029-01-05,1235,258-->
- [voiced uvular trill](voiced%20uvular%20trill.md):@:![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg) <!--SR:!2027-12-30,1072,298-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg) <!--SR:!2026-12-17,751,291-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg) <!--SR:!2028-04-19,1136,312-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg) <!--SR:!2026-08-03,711,311-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg) <!--SR:!2029-05-31,1484,298-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg) <!--SR:!2027-07-18,999,352-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg) <!--SR:!2030-07-26,1855,331-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg) <!--SR:!2026-08-29,729,278-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg) <!--SR:!2030-09-26,1917,313-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg) <!--SR:!2028-06-14,1222,331-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg) <!--SR:!fsrs,2030-03-25T00:00:00.000Z,1370,1369.63121286,5.25532134,2,11,0,0,2026-06-24T00:00:00.000Z-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg) <!--SR:!2027-12-28,1056,354-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg) <!--SR:!2028-12-23,1275,311-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg) <!--SR:!2027-12-09,1039,278-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg) <!--SR:!2029-02-12,1432,371-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg) <!--SR:!2027-09-30,959,312-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg) <!--SR:!2027-07-28,615,314-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg) <!--SR:!2026-09-12,238,272-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg) <!--SR:!2026-07-25,556,213-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg) <!--SR:!2027-03-04,348,284-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg) <!--SR:!2027-12-17,1147,374-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg) <!--SR:!2028-12-15,1389,373-->
- [voiced velar approximant](voiced%20velar%20approximant.md):@:![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg) <!--SR:!2028-10-15,1316,317-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg) <!--SR:!2027-03-11,346,273-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg) <!--SR:!2027-02-10,902,318-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg) <!--SR:!2026-10-19,780,331-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg) <!--SR:!2026-10-11,722,244-->
- [voiced velar fricative](voiced%20velar%20fricative.md):@:![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg) <!--SR:!2027-06-13,1002,340-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg) <!--SR:!2028-10-14,1341,341-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg) <!--SR:!2026-08-19,737,331-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav) <!--SR:!2026-10-31,693,336-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg) <!--SR:!2027-01-16,257,291-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg) <!--SR:!2027-01-29,678,334-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg) <!--SR:!2028-02-17,987,315-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg) <!--SR:!fsrs,2029-11-12T00:00:00.000Z,1220,1220.40297417,4.88190763,2,10,0,0,2026-07-11T00:00:00.000Z-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg) <!--SR:!2027-03-13,736,296-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg) <!--SR:!2028-09-28,1148,315-->
- [glottal stop](glottal%20stop.md):@:![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg) <!--SR:!fsrs,2028-09-19T00:00:00.000Z,822,822.31651291,1.78094087,2,9,0,0,2026-06-20T00:00:00.000Z-->
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg) <!--SR:!2027-06-23,627,330-->
- [tenuis dental click](tenuis%20dental%20click.md):@:![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg) <!--SR:!2028-04-11,1093,355-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg) <!--SR:!2026-08-06,183,330-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg) <!--SR:!2026-10-16,682,335-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg) <!--SR:!2028-06-26,810,349-->
- [tenuis palatal click](tenuis%20palatal%20click.md):@:![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg) <!--SR:!2028-01-12,1024,355-->

<!--/pytextgen-->

<!--pytextgen generate section="f9aa"--><!-- The following content is generated at 2024-02-14T16:42:37.178940+08:00. Any edits will be overridden! -->

- ![open front unrounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20unrounded%20vowel.ogg):@:[open front unrounded vowel](open%20front%20unrounded%20vowel.md) <!--SR:!fsrs,2026-07-26T05:52:35.324Z,41,40.66101918,9.98522837,2,6,0,0,2026-06-15T05:52:35.324Z-->
- ![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg):@:[open central unrounded vowel](open%20central%20unrounded%20vowel.md) <!--SR:!fsrs,2027-05-30T05:54:18.890Z,349,348.70492644,7.47090938,2,9,0,0,2026-06-15T05:54:18.890Z-->
- ![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg):@:[near-open central vowel](near-open%20central%20vowel.md) <!--SR:!fsrs,2026-08-21T00:00:00.000Z,59,58.56281169,9.98522837,2,7,0,0,2026-06-23T00:00:00.000Z-->
- ![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg):@:[open back unrounded vowel](open%20back%20unrounded%20vowel.md) <!--SR:!2026-08-01,83,130-->
- ![nasalized open back unrounded vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg):@:[nasalized open back unrounded vowel](nasal%20vowel.md) <!--SR:!2027-01-21,547,233-->
- ![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg):@:[open back rounded vowel](open%20back%20rounded%20vowel.md) <!--SR:!2028-01-18,611,272-->
- ![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg):@:[open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md) <!--SR:!fsrs,2028-02-29T04:00:26.709Z,624,623.79048254,7.76964035,2,10,0,0,2026-06-15T04:00:26.709Z-->
- ![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg):@:[near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md) <!--SR:!fsrs,2026-09-16T00:00:00.000Z,75,75.30923395,9.98522837,2,7,0,0,2026-07-03T00:00:00.000Z-->
- ![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg):@:[voiced bilabial plosive](voiced%20bilabial%20plosive.md) <!--SR:!fsrs,2026-09-23T00:00:00.000Z,74,74.08182209,9.98522837,2,7,0,0,2026-07-11T00:00:00.000Z-->
- ![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg):@:[voiced bilabial implosive](voiced%20bilabial%20implosive.md) <!--SR:!fsrs,2028-04-11T00:00:00.000Z,639,639.43835987,4.44077837,2,9,0,0,2026-07-12T00:00:00.000Z-->
- ![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg):@:[voiced bilabial fricative](voiced%20bilabial%20fricative.md) <!--SR:!2026-12-22,232,231-->
- ![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg):@:[voiced bilabial trill](voiced%20bilabial%20trill.md) <!--SR:!2026-12-09,610,231-->
- ![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg):@:[voiceless palatal plosive](voiceless%20palatal%20plosive.md) <!--SR:!2026-08-05,84,130-->
- ![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg):@:[voiceless palatal fricative](voiceless%20palatal%20fricative.md) <!--SR:!fsrs,2026-07-16T03:59:07.430Z,31,30.75334967,9.98522837,2,5,0,0,2026-06-15T03:59:07.430Z-->
- ![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg):@:[voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md) <!--SR:!fsrs,2026-08-09T00:00:00.000Z,31,30.89063477,9.97047151,2,6,0,0,2026-07-09T00:00:00.000Z-->
- ![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg):@:[voiced alveolar plosive](voiced%20alveolar%20plosive.md) <!--SR:!fsrs,2026-10-07T00:00:00.000Z,87,87.01619319,9.94776587,2,7,0,0,2026-07-12T00:00:00.000Z-->
- ![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg):@:[voiced alveolar implosive](voiced%20alveolar%20implosive.md) <!--SR:!2026-09-08,127,150-->
- ![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.ogg):@:[voiced retroflex plosive](voiced%20retroflex%20plosive.md) <!--SR:!fsrs,2026-08-04T00:00:00.000Z,28,28.09363714,9.97047151,2,6,0,0,2026-07-07T00:00:00.000Z-->
- ![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg):@:[voiced dental fricative](voiced%20dental%20fricative.md) <!--SR:!2026-08-12,100,190-->
- ![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.ogg):@:[voiced alveolar affricate](voiced%20alveolar%20affricate.md) <!--SR:!2026-07-25,69,130-->
- ![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg):@:[voiced postalveolar affricate](voiced%20postalveolar%20affricate.md) <!--SR:!2026-07-16,162,130-->
- ![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg):@:[voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md) <!--SR:!fsrs,2026-07-15T00:00:00.000Z,17,16.76590028,9.97047151,2,5,0,0,2026-06-28T00:00:00.000Z-->
- ![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg):@:[voiced retroflex affricate](voiced%20retroflex%20affricate.md) <!--SR:!2026-11-11,486,214-->
- ![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg):@:[close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md) <!--SR:!2026-10-18,658,251-->
- ![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg):@:[close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md) <!--SR:!fsrs,2026-08-11T00:00:00.000Z,32,32.36622591,9.97047151,2,6,0,0,2026-07-10T00:00:00.000Z-->
- ![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg):@:[mid central vowel](mid%20central%20vowel.md) <!--SR:!2026-07-28,156,150-->
- ![r-colored mid central vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg):@:[r-colored mid central vowel](r-colored%20vowel.md) <!--SR:!2027-11-07,1007,299-->
- ![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg):@:[open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md) <!--SR:!fsrs,2026-07-26T00:00:00.000Z,18,17.88367862,9.95572941,2,6,0,0,2026-07-08T00:00:00.000Z-->
- ![nasalized open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg):@:[nasalized open-mid front unrounded vowel](nasal%20vowel.md) <!--SR:!fsrs,2026-07-17T00:00:00.000Z,14,13.96407764,9.95572941,2,5,0,0,2026-07-03T00:00:00.000Z-->
- ![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg):@:[open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md) <!--SR:!fsrs,2026-09-09T04:00:11.098Z,86,85.5541997,6.98822837,2,6,0,0,2026-06-15T04:00:11.098Z-->
- ![r-colored open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg):@:[r-colored open-mid central unrounded vowel](r-colored%20vowel.md) <!--SR:!fsrs,2026-07-30T00:00:00.000Z,43,43.14290937,9.98522837,2,6,0,0,2026-06-17T00:00:00.000Z-->
- ![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg):@:[voiceless labiodental fricative](voiceless%20labiodental%20fricative.md) <!--SR:!2026-09-25,144,173-->
- ![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg):@:[voiced velar plosive](voiced%20velar%20plosive.md) <!--SR:!2027-03-11,418,194-->
- ![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg):@:[voiced velar implosive](voiced%20velar%20implosive.md) <!--SR:!2026-08-02,84,130-->
- ![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.ogg):@:[voiced uvular plosive](voiced%20uvular%20plosive.md) <!--SR:!fsrs,2027-01-12T03:37:26.281Z,211,211.47091561,9.98522837,2,8,0,0,2026-06-15T03:37:26.281Z-->
- ![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg):@:[voiceless glottal fricative](voiceless%20glottal%20fricative.md) <!--SR:!fsrs,2026-09-11T00:00:00.000Z,65,65.34996832,9.73628589,2,7,0,0,2026-07-08T00:00:00.000Z-->
- ![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg):@:[voiced glottal fricative](voiced%20glottal%20fricative.md) <!--SR:!2028-03-07,902,221-->
- ![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg):@:[voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md) <!--SR:!2030-02-17,1660,351-->
- ![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg):@:[close front unrounded vowel](close%20front%20unrounded%20vowel.md) <!--SR:!fsrs,2026-09-08T03:44:06.816Z,85,84.6488389,9.98522837,2,7,0,0,2026-06-15T03:44:06.816Z-->
- ![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg):@:[near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md) <!--SR:!2027-01-04,479,214-->
- ![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg):@:[close central unrounded vowel](close%20central%20unrounded%20vowel.md) <!--SR:!2027-02-08,255,250-->
- ![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg):@:[voiced palatal approximant](voiced%20palatal%20approximant.md) <!--SR:!fsrs,2027-07-19T05:58:09.690Z,399,399.35279769,3.20451587,2,8,0,0,2026-06-15T05:58:09.690Z-->
- ![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg):@:[voiced palatal fricative](voiced%20palatal%20fricative.md) <!--SR:!fsrs,2027-02-17T05:53:16.241Z,247,247.22914057,5.45226587,2,8,0,0,2026-06-15T05:53:16.241Z-->
- ![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg):@:[voiced palatal plosive](voiced%20palatal%20plosive.md) <!--SR:!2027-06-07,576,234-->
- ![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg):@:[voiced palatal implosive](voiced%20palatal%20implosive.md) <!--SR:!fsrs,2026-12-23T05:52:00.681Z,191,191.35778505,4.70301587,2,7,0,0,2026-06-15T05:52:00.681Z-->
- ![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg):@:[voiceless velar plosive](voiceless%20velar%20plosive.md) <!--SR:!2027-03-23,412,230-->
- ![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg):@:[voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md) <!--SR:!fsrs,2027-07-15T06:00:37.993Z,395,395.39466129,7.49580362,2,9,0,0,2026-06-15T06:00:37.993Z-->
- ![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg):@:[velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md) <!--SR:!fsrs,2026-07-31T00:00:00.000Z,18,17.8858568,9.96891253,2,6,0,0,2026-07-13T00:00:00.000Z-->
- ![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg):@:[voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md) <!--SR:!2026-07-23,55,251-->
- ![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg):@:[voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md) <!--SR:!fsrs,2026-08-11T06:01:20.395Z,57,57.42424931,8.49157352,2,6,0,0,2026-06-15T06:01:20.395Z-->
- ![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg):@:[voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md) <!--SR:!fsrs,2026-08-04T03:59:56.171Z,50,50.07902218,7.96879432,2,6,0,0,2026-06-15T03:59:56.171Z-->
- ![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg):@:[voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md) <!--SR:!fsrs,2026-07-27T05:51:29.974Z,42,41.73352078,9.98522837,2,6,0,0,2026-06-15T05:51:29.974Z-->
- ![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg):@:[voiced bilabial nasal](voiced%20bilabial%20nasal.md) <!--SR:!2026-10-15,316,276-->
- ![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg):@:[voiced labiodental nasal](voiced%20labiodental%20nasal.md) <!--SR:!2026-08-02,197,294-->
- ![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg):@:[voiced alveolar nasal](voiced%20alveolar%20nasal.md) <!--SR:!2027-08-02,562,270-->
- ![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg):@:[voiced velar nasal](voiced%20velar%20nasal.md) <!--SR:!fsrs,2026-09-20T00:00:00.000Z,94,94.09467237,6.50003372,2,7,0,0,2026-06-18T00:00:00.000Z-->
- ![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg):@:[voiced palatal nasal](voiced%20palatal%20nasal.md) <!--SR:!2026-08-19,107,190-->
- ![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg):@:[voiced retroflex nasal](voiced%20retroflex%20nasal.md) <!--SR:!2028-01-24,737,274-->
- ![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg):@:[voiced uvular nasal](voiced%20uvular%20nasal.md) <!--SR:!2028-07-20,808,270-->
- ![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg):@:[close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md) <!--SR:!2027-01-13,254,290-->
- ![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg):@:[open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md) <!--SR:!2027-07-24,827,296-->
- ![nasalized open-mid back rounded vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg):@:[nasalized open-mid back rounded vowel](nasal%20vowel.md) <!--SR:!fsrs,2026-08-01T05:54:01.743Z,47,47.0387257,9.98522837,2,6,0,0,2026-06-15T05:54:01.743Z-->
- ![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg):@:[close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md) <!--SR:!2026-08-11,99,230-->
- ![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg):@:[close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md) <!--SR:!2026-08-16,104,196-->
- ![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg):@:[open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md) <!--SR:!fsrs,2026-07-24T00:00:00.000Z,16,15.78431141,9.96562598,2,5,0,0,2026-07-08T00:00:00.000Z-->
- ![nasalized open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg):@:[nasalized open-mid front rounded vowel](nasal%20vowel.md) <!--SR:!fsrs,2026-07-27T00:00:00.000Z,25,24.53940073,9.44821509,2,5,0,0,2026-07-02T00:00:00.000Z-->
- ![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg):@:[open front rounded vowel](open%20front%20rounded%20vowel.md) <!--SR:!2027-01-30,271,290-->
- ![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg):@:[voiceless bilabial plosive](voiceless%20bilabial%20plosive.md) <!--SR:!fsrs,2026-09-17T05:51:47.817Z,94,93.57235333,9.98522837,2,7,0,0,2026-06-15T05:51:47.817Z-->
- ![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg):@:[voiceless uvular plosive](voiceless%20uvular%20plosive.md) <!--SR:!fsrs,2026-10-08T06:01:24.447Z,115,115.31141688,9.98522837,2,7,0,0,2026-06-15T06:01:24.447Z-->
- ![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg):@:[voiced alveolar trill](voiced%20alveolar%20trill.md) <!--SR:!2029-02-02,1094,275-->
- ![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg):@:[voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md) <!--SR:!2027-03-03,692,295-->
- ![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg):@:[voiced uvular trill](voiced%20uvular%20trill.md) <!--SR:!2027-05-27,476,276-->
- ![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg):@:[voiced retroflex flap](voiced%20retroflex%20flap.md) <!--SR:!2026-07-27,131,214-->
- ![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg):@:[voiced alveolar approximant](voiced%20alveolar%20approximant.md) <!--SR:!2026-07-30,87,251-->
- ![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.ogg):@:[voiced retroflex approximant](voiced%20retroflex%20approximant.md) <!--SR:!2026-07-24,56,250-->
- ![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg):@:[voiced uvular fricative](voiced%20uvular%20fricative.md) <!--SR:!fsrs,2026-11-21T03:59:39.974Z,159,158.99165094,6.99791867,2,7,0,0,2026-06-15T03:59:39.974Z-->
- ![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg):@:[voiceless alveolar fricative](voiceless%20alveolar%20fricative.md) <!--SR:!2026-10-07,143,250-->
- ![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg):@:[voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md) <!--SR:!2026-08-12,147,250-->
- ![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg):@:[voiceless retroflex fricative](voiceless%20retroflex%20fricative.md) <!--SR:!2026-07-22,54,130-->
- ![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg):@:[voiceless alveolar plosive](voiceless%20alveolar%20plosive.md) <!--SR:!fsrs,2026-08-19T05:56:58.823Z,65,64.72605691,9.98522837,2,7,0,0,2026-06-15T05:56:58.823Z-->
- ![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.ogg):@:[voiceless retroflex plosive](voiceless%20retroflex%20plosive.md) <!--SR:!fsrs,2026-08-20T03:43:48.159Z,66,66.17439996,7.89411158,2,6,0,0,2026-06-15T03:43:48.159Z-->
- ![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.ogg):@:[voiceless alveolar affricate](voiceless%20alveolar%20affricate.md) <!--SR:!fsrs,2026-07-28T00:00:00.000Z,17,16.55380692,9.96891253,2,6,0,0,2026-07-11T00:00:00.000Z-->
- ![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg):@:[voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md) <!--SR:!2027-01-29,474,270-->
- ![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg):@:[voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md) <!--SR:!fsrs,2027-04-08T05:59:48.417Z,297,297.20873746,4.74047837,2,8,0,0,2026-06-15T05:59:48.417Z-->
- ![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg):@:[voiceless retroflex affricate](voiceless%20retroflex%20affricate.md) <!--SR:!fsrs,2026-07-26T00:00:00.000Z,16,16.20317466,9.96891253,2,6,0,0,2026-07-10T00:00:00.000Z-->
- ![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg):@:[close back rounded vowel](close%20back%20rounded%20vowel.md) <!--SR:!2027-01-19,571,235-->
- ![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg):@:[near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md) <!--SR:!fsrs,2026-08-07T00:00:00.000Z,29,29.15109677,9.97047151,2,6,0,0,2026-07-09T00:00:00.000Z-->
- ![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg):@:[close central rounded vowel](close%20central%20rounded%20vowel.md) <!--SR:!2027-01-08,249,291-->
- ![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg):@:[voiced labiodental fricative](voiced%20labiodental%20fricative.md) <!--SR:!2027-06-16,583,290-->
- ![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg):@:[voiced labiodental approximant](voiced%20labiodental%20approximant.md) <!--SR:!2026-10-12,136,190-->
- ![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg):@:[voiced labial–velar approximant](voiced%20labial–velar%20approximant.md) <!--SR:!2027-01-30,271,291-->
- ![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg):@:[voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md) <!--SR:!fsrs,2026-07-26T00:00:00.000Z,22,21.76843692,9.97542228,2,5,0,0,2026-07-04T00:00:00.000Z-->
- ![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg):@:[close back unrounded vowel](close%20back%20unrounded%20vowel.md) <!--SR:!fsrs,2026-08-26T00:00:00.000Z,64,64.23813052,9.98522837,2,7,0,0,2026-06-23T00:00:00.000Z-->
- ![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg):@:[voiced velar approximant](voiced%20velar%20approximant.md) <!--SR:!2026-08-04,67,291-->
- ![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg):@:[voiceless velar fricative](voiceless%20velar%20fricative.md) <!--SR:!fsrs,2026-09-16T03:48:49.327Z,92,92.48987238,6.47513947,2,6,0,0,2026-06-16T03:48:49.327Z-->
- ![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg):@:[voiceless uvular fricative](voiceless%20uvular%20fricative.md) <!--SR:!fsrs,2026-08-01T00:00:00.000Z,25,25.41404429,9.97542228,2,6,0,0,2026-07-07T00:00:00.000Z-->
- ![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg):@:[close front rounded vowel](close%20front%20rounded%20vowel.md) <!--SR:!fsrs,2026-11-30T06:00:51.610Z,168,167.58447547,6.50003372,2,7,0,0,2026-06-15T06:00:51.610Z-->
- ![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg):@:[near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md) <!--SR:!2026-08-04,92,230-->
- ![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg):@:[voiced velar fricative](voiced%20velar%20fricative.md) <!--SR:!fsrs,2026-10-16T00:00:00.000Z,96,95.55744238,8.98945847,2,7,0,0,2026-07-12T00:00:00.000Z-->
- ![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg):@:[close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md) <!--SR:!2026-07-18,75,270-->
- ![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg):@:[voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md) <!--SR:!fsrs,2026-11-08T00:00:00.000Z,117,116.92876556,8.48672837,2,7,0,0,2026-07-14T00:00:00.000Z-->
- ![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav):@:[voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md) <!--SR:!fsrs,2026-08-18T05:53:32.606Z,64,63.78318235,7.47090938,2,6,0,0,2026-06-15T05:53:32.606Z-->
- ![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg):@:[voiced alveolar fricative](voiced%20alveolar%20fricative.md) <!--SR:!2026-12-10,644,275-->
- ![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg):@:[voiced postalveolar fricative](voiced%20postalveolar%20fricative.md) <!--SR:!fsrs,2026-07-15T03:44:14.171Z,30,29.6137433,9.98522837,2,5,0,0,2026-06-15T03:44:14.171Z-->
- ![voiced alveolo–palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg):@:[voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md) <!--SR:!fsrs,2026-07-30T00:00:00.000Z,19,18.65127049,9.96067523,2,6,0,0,2026-07-11T00:00:00.000Z-->
- ![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg):@:[voiced retroflex fricative](voiced%20retroflex%20fricative.md) <!--SR:!fsrs,2026-10-27T00:00:00.000Z,130,129.61380588,4.70301587,2,7,0,0,2026-06-19T00:00:00.000Z-->
- ![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg):@:[voiceless dental fricative](voiceless%20dental%20fricative.md) <!--SR:!fsrs,2027-04-20T06:00:17.397Z,309,308.53986267,4.74047837,2,8,0,0,2026-06-15T06:00:17.397Z-->
- ![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg):@:[voiceless bilabial fricative](voiceless%20bilabial%20fricative.md) <!--SR:!2027-05-20,369,310-->
- ![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg):@:[glottal stop](glottal%20stop.md) <!--SR:!2026-07-17,75,250-->
- ![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg):@:[voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md) <!--SR:!2026-12-17,316,310-->
- ![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg):@:[tenuis dental click](tenuis%20dental%20click.md) <!--SR:!fsrs,2027-01-26T00:00:00.000Z,205,205.25611234,7.49580362,2,8,0,0,2026-07-05T00:00:00.000Z-->
- ![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg):@:[tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md) <!--SR:!2026-11-01,492,275-->
- ![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg):@:[tenuis alveolar click](tenuis%20alveolar%20click.md) <!--SR:!fsrs,2027-08-19T00:00:00.000Z,404,403.66667662,6.50003372,2,9,0,0,2026-07-11T00:00:00.000Z-->
- ![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg):@:[tenuis bilabial click](tenuis%20bilabial%20click.md) <!--SR:!2029-08-18,1497,375-->
- ![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg):@:[tenuis palatal click](tenuis%20palatal%20click.md) <!--SR:!2027-09-24,508,250-->

<!--/pytextgen-->

#### name–description (letters)

<!--pytextgen generate section="50b0"--><!-- The following content is generated at 2024-01-04T20:18:01.048113+08:00. Any edits will be overridden! -->

- [open front unrounded vowel](open%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _h**a**t_ \[hat\] <!--SR:!2026-09-27,622,310-->
- [open central unrounded vowel](open%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _br**a**_ \[bɹäː\] <!--SR:!2026-08-27,179,130-->
- [near-open central vowel](near-open%20central%20vowel.md):@:[English](English%20language.md) _n**u**t_ \[nɐʔt\] <!--SR:!fsrs,2026-08-05T00:00:00.000Z,38,38.13361923,9.98522837,2,6,0,0,2026-06-28T00:00:00.000Z-->
- [open back unrounded vowel](open%20back%20unrounded%20vowel.md):@:[English](English%20language.md) _p**a**lm_ \[pɑ̟ːm\] <!--SR:!fsrs,2026-09-01T03:37:36.498Z,78,77.51803347,9.98522837,2,7,0,0,2026-06-15T03:37:36.498Z-->
- [nasalized open back unrounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _s**an**s_ [sɑ̃] "without" <!--SR:!fsrs,2026-12-30T00:00:00.000Z,193,193.35257046,9.46075337,2,8,0,0,2026-06-20T00:00:00.000Z-->
- [open back rounded vowel](open%20back%20rounded%20vowel.md):@:[English](English%20language.md) _n**o**t_ \[nɒt\] <!--SR:!2027-10-11,836,224-->
- [open-mid back unrounded vowel](open-mid%20back%20unrounded%20vowel.md):@:[English](English%20language.md) _g**u**t_ \[ɡʌt\] <!--SR:!2026-11-14,478,264-->
- [near-open front unrounded vowel](near-open%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _c**a**t_ \[kʰæt\] <!--SR:!2026-07-17,129,130-->
- [voiced bilabial plosive](voiced%20bilabial%20plosive.md):@:[English](English%20language.md) _a**b**ack_ \[əˈbæk\] <!--SR:!2026-12-12,639,264-->
- [voiced bilabial implosive](voiced%20bilabial%20implosive.md):@:[English](English%20language.md) _**b**ody_ \[ɓʌdi\] <!--SR:!fsrs,2029-02-13T00:00:00.000Z,965,964.91115952,6.64939921,2,10,0,0,2026-06-24T00:00:00.000Z-->
- [voiced bilabial fricative](voiced%20bilabial%20fricative.md):@:[Spanish](Spanish%20language.md) _la**v**a_ \[ˈläβ̞ä\] "lava" <!--SR:!fsrs,2028-02-23T00:00:00.000Z,597,597.47249674,7.21300337,2,9,0,0,2026-07-06T00:00:00.000Z-->
- [voiced bilabial trill](voiced%20bilabial%20trill.md):@:[Nias](Nias%20language.md) _si**mb**i_ \[siʙi\] "lower jaw" <!--SR:!fsrs,2027-08-17T05:57:27.358Z,428,427.63126942,7.96225337,2,9,0,0,2026-06-15T05:57:27.358Z-->
- [voiceless palatal plosive](voiceless%20palatal%20plosive.md):@:[French](French%20language.md) _**q**ui_ \[ci\] "who" <!--SR:!2027-08-30,483,264-->
- [voiceless palatal fricative](voiceless%20palatal%20fricative.md):@:[English](English%20language.md) _**h**ue_ \[çʉː\] <!--SR:!fsrs,2026-08-31T14:12:00.622Z,78,78.02952558,9.98522837,2,7,0,0,2026-06-14T14:12:00.622Z-->
- [voiceless alveolo-palatal fricative](voiceless%20alveolo-palatal%20fricative.md):@:[English](English%20language.md) _**t**uesday_ \[ˈt̺ʲɕuːzdeɪ\] <!--SR:!fsrs,2026-07-28T00:00:00.000Z,15,15.08838962,9.95417199,2,6,0,0,2026-07-13T00:00:00.000Z-->
- [voiced alveolar plosive](voiced%20alveolar%20plosive.md):@:[English](English%20language.md) _**d**ash_ \[ˈdæʃ\] <!--SR:!2029-08-03,1420,273-->
- [voiced alveolar implosive](voiced%20alveolar%20implosive.md):@:[Vietnamese](Vietnamese%20language.md) _**đ**uôi_ \[ɗuəj\] "tail" <!--SR:!2027-11-07,552,193-->
- [voiced retroflex plosive](voiced%20retroflex%20plosive.md):@:[Swedish](Swedish%20language.md) _no**rd**_ \[nuːɖ\] "north" <!--SR:!fsrs,2026-07-31T00:00:00.000Z,26,26.41809106,9.97047151,2,6,0,0,2026-07-05T00:00:00.000Z-->
- [voiced dental fricative](voiced%20dental%20fricative.md):@:[English](English%20language.md) _**th**is_ \[ðɪs\] <!--SR:!2027-06-27,752,233-->
- [voiced alveolar affricate](voiced%20alveolar%20affricate.md):@:[English](English%20language.md) _**d**ay_ \[ˈd͡zeˑɪ̯\] <!--SR:!2026-08-12,75,130-->
- [voiced postalveolar affricate](voiced%20postalveolar%20affricate.md):@:[English](English%20language.md) _**g**ene_ \[ˈd͡ʒiːn\] <!--SR:!2027-03-28,303,158-->
- [voiced alveolo-palatal affricate](voiced%20alveolo-palatal%20affricate.md):@:[Polish](Polish%20language.md) _**dź**więk_ \[d͡ʑvʲɛŋk\] "sound" <!--SR:!fsrs,2026-07-17T00:00:00.000Z,18,18.16168775,9.97047151,2,5,0,0,2026-06-29T00:00:00.000Z-->
- [voiced retroflex affricate](voiced%20retroflex%20affricate.md):@:[Polish](Polish%20language.md) _**dż**em_ \[ɖ͡ʐɛm\] "jam" <!--SR:!2026-08-18,106,158-->
- [close-mid front unrounded vowel](close-mid%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _m**ay**_ \[meː\] <!--SR:!2026-07-27,53,130-->
- [close-mid central unrounded vowel](close-mid%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɘːd\] <!--SR:!fsrs,2026-11-09T08:09:10.807Z,155,155.15705834,9.23597837,2,8,0,0,2026-06-07T08:09:10.807Z-->
- [mid central vowel](mid%20central%20vowel.md):@:[English](English%20language.md) _Tin**a**_ \[ˈtʰiːnə\] <!--SR:!2026-12-20,221,138-->
- [r-colored mid central vowel](r-colored%20vowel.md):@:[English](English%20language.md) _runn**er**_ \[ˈɹʌnɚ\] <!--SR:!2026-08-26,295,238-->
- [open-mid front unrounded vowel](open-mid%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _b**e**d_ \[bɛd\] <!--SR:!fsrs,2027-03-03T05:52:26.829Z,261,260.96511023,8.93627837,2,8,0,0,2026-06-15T05:52:26.829Z-->
- [nasalized open-mid front unrounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _m**ain**_ \[mɛ̃\] "hand" <!--SR:!fsrs,2026-07-19T00:00:00.000Z,21,20.55472178,9.96552075,2,5,0,0,2026-06-28T00:00:00.000Z-->
- [open-mid central unrounded vowel](open-mid%20central%20unrounded%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɜːd\] <!--SR:!2028-02-25,1039,278-->
- [r-colored open-mid central unrounded vowel](r-colored%20vowel.md):@:[English](English%20language.md) _b**ir**d_ \[bɝːd\] <!--SR:!2027-06-10,581,297-->
- [voiceless labiodental fricative](voiceless%20labiodental%20fricative.md):@:[English](English%20language.md) _**f**ill_ \[fɪɫ\] <!--SR:!2026-10-23,533,237-->
- [voiced velar plosive](voiced%20velar%20plosive.md):@:[English](English%20language.md) _**g**a**gg**le_ \[ˈɡæɡɫ̩\] <!--SR:!2027-01-05,389,177-->
- [voiced velar implosive](voiced%20velar%20implosive.md):@:[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!fsrs,2027-03-04T00:00:00.000Z,249,249.3555891,9.63501311,2,8,0,0,2026-06-28T00:00:00.000Z-->
- [voiced uvular plosive](voiced%20uvular%20plosive.md):@:[English](English%20language.md) _**g**audy_ \[ˈɡ̠oːɾi\] <!--SR:!2026-10-20,159,217-->
- [voiceless glottal fricative](voiceless%20glottal%20fricative.md):@:[English](English%20language.md) _**h**igh_ \[haɪ̯\] <!--SR:!2026-11-24,750,297-->
- [voiced glottal fricative](voiced%20glottal%20fricative.md):@:[English](English%20language.md) _be**h**ind_ \[bɪˈɦaɪ̯nd\] <!--SR:!2028-05-20,1042,257-->
- [aspirated consonant](aspirated%20consonant.md):@:[English](English%20langugae.md) _**t**op_ \[tʰɒp\] <!--SR:!2032-05-16,2517,377-->
- [voiceless pharyngeal fricative](voiceless%20pharyngeal%20fricative.md):@:[English](English%20language.md) _**h**orrible_ \[ħɒɹɪbəl\] <!--SR:!2026-08-29,177,237-->
- [close front unrounded vowel](close%20front%20unrounded%20vowel.md):@:[English](English%20language.md) _fr**ee**_ \[fɹiː\] <!--SR:!fsrs,2026-11-04T00:00:00.000Z,133,133.25183221,9.98522837,2,8,0,0,2026-06-24T00:00:00.000Z-->
- [near-close near-front unrounded vowel](near-close%20near-front%20unrounded%20vowel.md):@:[English](English%20language.md) _b**i**t_ \[bɪʔt\] <!--SR:!fsrs,2027-05-19T14:11:57.200Z,339,339.43416587,9.31308369,2,9,0,0,2026-06-14T14:11:57.200Z-->
- [close central unrounded vowel](close%20central%20unrounded%20vowel.md):@:[Russian](Russian%20language.md) _т**ы**_ \[t̪ɨ\] "you" <!--SR:!fsrs,2026-11-07T00:00:00.000Z,136,136.49516346,9.98522837,2,8,0,0,2026-06-24T00:00:00.000Z-->
- [voiced palatal approximant](voiced%20palatal%20approximant.md):@:[English](English%20language.md) _**y**ou_ \[juː\] <!--SR:!fsrs,2026-08-13T03:37:06.993Z,59,59.25901572,9.98522837,2,6,0,0,2026-06-15T03:37:06.993Z-->
- [palatalization](palatalization%20(phonetics).md):@:[Irish](Irish%20language.md) _**be**o_ \[bʲoː\] "alive" <!--SR:!2027-01-06,580,238-->
- [voiced palatal fricative](voiced%20palatal%20fricative.md):@:[Spanish](Spanish%20language.md) _sa**y**o_ \[ˈsäʝo̞\] "smock" <!--SR:!fsrs,2026-08-04T00:00:00.000Z,36,35.64591396,9.98522837,2,6,0,0,2026-06-29T00:00:00.000Z-->
- [voiced palatal plosive](voiced%20palatal%20plosive.md):@:[Irish](Irish%20language.md) _Gaeil**g**e_ \[ˈɡeːlʲɟə\] "[Irish language](Irish%20language.md)" <!--SR:!fsrs,2026-08-05T00:00:00.000Z,38,38.13361923,9.98522837,2,6,0,0,2026-06-28T00:00:00.000Z-->
- [voiced palatal implosive](voiced%20palatal%20implosive.md):@:[Swahili](Swahili%20language.md) _**j**ana_ \[ʄana\] "yesterday" <!--SR:!2026-09-10,441,198-->
- [voiceless velar plosive](voiceless%20velar%20plosive.md):@:[English](English%20language.md) _**k**iss_ \[kʰɪs\] <!--SR:!2027-02-27,519,199-->
- [voiced alveolar lateral approximant](voiced%20alveolar%20lateral%20approximant.md):@:[English](English%20language.md) _**l**et_ \[lɛt\] <!--SR:!2028-10-04,1102,280-->
- [velarized alveolar lateral approximant](velarized%20alveolar%20lateral%20approximant.md):@:[English](English%20language.md) _fee**l**_ \[fiːɫ\] <!--SR:!2026-12-13,259,220-->
- [voiceless alveolar lateral fricative](voiceless%20alveolar%20lateral%20fricative.md):@:[Welsh](Welsh%20language.md) _tege**ll**_ \[ˈtɛɡɛɬ\] "kettle" <!--SR:!fsrs,2026-10-13T00:00:00.000Z,97,96.6578485,9.98522837,2,7,0,0,2026-07-08T00:00:00.000Z-->
- [voiced retroflex lateral approximant](voiced%20retroflex%20lateral%20approximant.md):@:[French](French%20language.md) _be**ll**e jambe_ \[bɛɭ ʒɑ̃b\] "beautiful leg" <!--SR:!fsrs,2026-07-17T05:47:59.807Z,32,31.88326137,9.98522837,2,5,0,0,2026-06-15T05:47:59.807Z-->
- [voiced alveolar lateral flap](voiced%20alveolar%20lateral%20flap.md):@:[Japanese](Japanese%20language.md) 六/_**r**oku_ \[ɺo̞kɯ̟ᵝ\] "six" <!--SR:!2026-08-19,77,130-->
- [voiced alveolar lateral fricative](voiced%20alveolar%20lateral%20fricative.md):@:[Zulu](Zulu%20language.md) _uku**dl**a_ \[úɠù:ɮá\] "to eat" <!--SR:!fsrs,2026-07-31T00:00:00.000Z,17,16.94943162,9.94594292,2,6,0,0,2026-07-14T00:00:00.000Z-->
- [voiced velar lateral approximant](voiced%20velar%20lateral%20approximant.md):@:[English](English%20language.md) _midd**l**e_ \[ˈmɪɾʟ̩\] <!--SR:!2027-05-05,366,201-->
- [voiced bilabial nasal](voiced%20bilabial%20nasal.md):@:[English](English%20language.md) _hi**m**_ \[hɪm\] <!--SR:!2031-11-21,2117,301-->
- [voiced labiodental nasal](voiced%20labiodental%20nasal.md):@:[English](English%20language.md) _sy**m**phony_ \[ˈsɪɱfəni\] <!--SR:!2027-07-26,537,261-->
- [voiced alveolar nasal](voiced%20alveolar%20nasal.md):@:[English](English%20language.md) _**n**ice_ \[naɪs\] <!--SR:!2029-04-06,1251,281-->
- [voiced velar nasal](voiced%20velar%20nasal.md):@:[English](English%20language.md) _si**ng**_ \[sɪŋ\] <!--SR:!2027-02-10,389,221-->
- [voiced palatal nasal](voiced%20palatal%20nasal.md):@:[French](French%20language.md) _oi**gn**on_ \[ɔ.ɲɔ̃\] "onion" <!--SR:!fsrs,2027-06-28T08:12:45.760Z,386,386.314019,6.57614087,2,9,0,0,2026-06-07T08:12:45.760Z-->
- [voiced retroflex nasal](voiced%20retroflex%20nasal.md):@:[Norwegian](Norwegian%20language.md) _ga**rn**_ \[ɡɑːɳ\] "yarn" <!--SR:!2026-09-03,122,150-->
- [voiced uvular nasal](voiced%20uvular%20nasal.md):@:[Spanish](Spanish%20language.md) _e**n**juto_ \[ẽ̞ɴˈχuto̞\] "shriveled" <!--SR:!2026-08-01,98,150-->
- [close-mid back rounded vowel](close-mid%20back%20rounded%20vowel.md):@:[English](English%20language.md) _y**aw**n_ \[joːn\] <!--SR:!2026-09-09,128,130-->
- [open-mid back rounded vowel](open-mid%20back%20rounded%20vowel.md):@:[English](English%20language.md) _n**o**t_ \[nɔt\] <!--SR:!2027-01-27,552,211-->
- [nasalized open-mid back rounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _s**on**_ \[sɔ̃\] "sound" <!--SR:!fsrs,2026-07-19T15:30:49.185Z,35,34.86191827,9.98522837,2,6,0,0,2026-06-14T15:30:49.185Z-->
- [close-mid front rounded vowel](close-mid%20front%20rounded%20vowel.md):@:[French](French%20language.md) _p**eu**_ \[pø\] "few" <!--SR:!fsrs,2026-08-04T00:00:00.000Z,28,27.70551504,9.97047151,2,6,0,0,2026-07-07T00:00:00.000Z-->
- [close-mid central rounded vowel](close-mid%20central%20rounded%20vowel.md):@:[English](English%20language.md) _f**oo**t_ \[fɵʔt\] <!--SR:!2026-12-20,222,170-->
- [open-mid front rounded vowel](open-mid%20front%20rounded%20vowel.md):@:[French](French%20language.md) _j**eu**ne_ \[ʒœn\] "young" <!--SR:!fsrs,2026-08-27T03:37:47.546Z,73,72.59289718,9.98522837,2,7,0,0,2026-06-15T03:37:47.546Z-->
- [nasalized open-mid front rounded vowel](nasal%20vowel.md):@:[French](French%20language.md) _br**un**_ \[bʁœ̃\] "brown" <!--SR:!fsrs,2026-08-21T00:00:00.000Z,59,58.56281169,9.98522837,2,7,0,0,2026-06-23T00:00:00.000Z-->
- [open front rounded vowel](open%20front%20rounded%20vowel.md):@:[Danish](Danish%20language.md) _gr**ø**n_ \[ˈkʁɶ̝nˀ\] "green" <!--SR:!fsrs,2026-07-28T00:00:00.000Z,27,26.6694074,9.96552075,2,5,0,0,2026-07-01T00:00:00.000Z-->
- [voiceless bilabial plosive](voiceless%20bilabial%20plosive.md):@:[English](English%20language.md) _**p**ack_ \[pʰæk\] <!--SR:!2028-04-13,1043,271-->
- [voiceless uvular plosive](voiceless%20uvular%20plosive.md):@:[Arabic](Arabic%20language.md) قط/_**q**iṭṭ_ \[qitˤː\] "cat" <!--SR:!fsrs,2026-07-23T00:00:00.000Z,16,16.06319005,9.96067523,2,6,0,0,2026-07-07T00:00:00.000Z-->
- [voiced alveolar trill](voiced%20alveolar%20trill.md):@:[Spanish](Spanish%20language.md) _pe**rr**o_ \[ˈpe̞ro̞\] "dog" <!--SR:!2026-07-29,86,171-->
- [voiced dental and alveolar taps and flaps](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md):@:[Spanish](Spanish%20language.md) _ca**r**o_ \[ˈkaɾo̞\] "expensive" <!--SR:!fsrs,2026-08-01T05:57:59.923Z,47,46.62779875,9.94776587,2,6,0,0,2026-06-15T05:57:59.923Z-->
- [voiced uvular trill](voiced%20uvular%20trill.md):@:[German](German%20language.md) _**r**ot_ \[ʀoːt\] "red" <!--SR:!2029-12-24,1496,291-->
- [voiced retroflex flap](voiced%20retroflex%20flap.md):@:[Swedish](Swedish%20language.md) _b**l**ad_ \[bɽɑː(d)\] "leaf" <!--SR:!2026-10-07,149,130-->
- [voiced alveolar approximant](voiced%20alveolar%20approximant.md):@:[Swedish](Swedish%20language.md) _sta**r**kast_ \[ˈs̪t̪äɹːkäs̪t̪\] "strongest" <!--SR:!2026-09-08,127,130-->
- [voiced retroflex approximant](voiced%20retroflex%20approximant.md):@:[Chinese](Chinese%20language.md) 肉/_**r**òu_ \[ɻ̺oʊ̯˥˩\] "meat" <!--SR:!fsrs,2026-08-03T00:00:00.000Z,24,23.67033291,9.95572941,2,6,0,0,2026-07-10T00:00:00.000Z-->
- [voiced uvular fricative](voiced%20uvular%20fricative.md):@:[French](French%20language.md) _**r**ester_ \[ʁɛste\] "to stay" <!--SR:!fsrs,2026-10-08T00:00:00.000Z,109,108.9618966,8.98461332,2,7,0,0,2026-06-21T00:00:00.000Z-->
- [voiceless alveolar fricative](voiceless%20alveolar%20fricative.md):@:[English](English%20language.md) _**s**it_ \[sɪt\] <!--SR:!2026-08-31,504,271-->
- [voiceless postalveolar fricative](voiceless%20postalveolar%20fricative.md):@:[English](English%20language.md) _**sh**eep_ \[ˈʃiːp\] <!--SR:!2026-08-04,265,191-->
- [voiceless retroflex fricative](voiceless%20retroflex%20fricative.md):@:[Polish](Polish%20language.md) _**sz**um_ \[ʂ̻um\] "rustle" <!--SR:!2026-07-31,84,130-->
- [voiceless alveolar plosive](voiceless%20alveolar%20plosive.md):@:[English](English%20language.md) _**t**ick_ \[tʰɪk\] <!--SR:!fsrs,2029-12-26T05:59:30.974Z,1290,1289.92569925,4.70301587,2,10,0,0,2026-06-15T05:59:30.974Z-->
- [voiceless retroflex plosive](voiceless%20retroflex%20plosive.md):@:[Norwegian](Norwegian%20language.md) _ko**rt**_ \[kɔʈː\] "card" <!--SR:!fsrs,2026-09-22T00:00:00.000Z,83,82.94106728,8.44926587,2,7,0,0,2026-07-01T00:00:00.000Z-->
- [voiceless alveolar affricate](voiceless%20alveolar%20affricate.md):@:[English](English%20language.md) _**t**ea_ \[ˈt͡sɪˑi̯\] <!--SR:!fsrs,2026-08-12T05:59:53.885Z,58,57.66052468,8.96456423,2,6,0,0,2026-06-15T05:59:53.885Z-->
- [voiceless postalveolar affricate](voiceless%20postalveolar%20affricate.md):@:[English](English%20language.md) _bea**ch**_ \[biːt͡ʃ\] <!--SR:!2026-10-15,253,231-->
- [voiceless alveolo-palatal affricate](voiceless%20alveolo-palatal%20affricate.md):@:[Chinese](Chinese%20language.md) 北京/_Běi**j**īng_ \[peɪ˨˩ t͡ɕiŋ˥\] "[Beijing](Beijing.md)" <!--SR:!fsrs,2026-08-22T00:00:00.000Z,41,41.10115707,9.22197076,2,6,0,0,2026-07-12T00:00:00.000Z-->
- [voiceless retroflex affricate](voiceless%20retroflex%20affricate.md):@:[Chinese](Chinese%20language.md) 中文/_**Zh**ōngwén_ \[ʈ̺͡ʂ̺ʊŋ˥ u̯ən˧˥\] "[Chinese language](Chinese%20language.md)" <!--SR:!fsrs,2026-07-27T00:00:00.000Z,19,19.14411938,9.96891253,2,6,0,0,2026-07-08T00:00:00.000Z-->
- [close back rounded vowel](close%20back%20rounded%20vowel.md):@:[English](English%20language.md) _b**oo**t_ \[bu̟ːt\] <!--SR:!2027-01-15,476,191-->
- [near-close near-back rounded vowel](near-close%20near-back%20rounded%20vowel.md):@:[English](English%20language.md) _h**oo**k_ \[hʊʔk\] <!--SR:!2026-09-10,131,150-->
- [close central rounded vowel](close%20central%20rounded%20vowel.md):@:[English](English%20language.md) _g**oo**se_ \[ɡʉːs\] <!--SR:!2026-10-22,146,130-->
- [voiced labiodental fricative](voiced%20labiodental%20fricative.md):@:[English](English%20language.md) _**v**al**v**e_ \[væɫv\] <!--SR:!2027-05-15,855,312-->
- [voiced labiodental approximant](voiced%20labiodental%20approximant.md):@:[Finnish](Finnish%20language.md) _**v**au**v**a_ \[ˈʋɑu̯ʋɑ\] "baby" <!--SR:!2026-09-13,239,252-->
- [voiced labial–velar approximant](voiced%20labial–velar%20approximant.md):@:[English](English%20language.md) _**w**eep_ \[wiːp\] <!--SR:!fsrs,2027-02-16T06:00:54.778Z,246,246.22881531,6.91330337,2,8,0,0,2026-06-15T06:00:54.778Z-->
- [labialization](labialization.md):@:[English](English%20language.md) _**r**eed_ \[ɹʷiːd\] <!--SR:!2026-08-03,129,192-->
- [voiceless labial–velar fricative](voiceless%20labial–velar%20fricative.md):@:[English](English%20language.md) _**wh**ine_ \[ʍaɪ̯n\] <!--SR:!fsrs,2026-07-26T03:43:52.618Z,41,40.66101918,9.98522837,2,6,0,0,2026-06-15T03:43:52.618Z-->
- [close back unrounded vowel](close%20back%20unrounded%20vowel.md):@:[Turkish](Turkish%20language.md) _s**ı**ğ_ \[sɯː\] "shallow" <!--SR:!2027-04-02,500,212-->
- [voiced velar approximant](voiced%20velar%20approximant.md):@:[Irish](Irish%20language.md) _n**ao**i_ \[n̪ˠɰiː\] "nine" <!--SR:!fsrs,2026-08-18T03:30:09.450Z,64,63.77685899,9.98522837,2,7,0,0,2026-06-15T03:30:09.450Z-->
- [voiceless velar fricative](voiceless%20velar%20fricative.md):@:[German](German%20language.md) _Bu**ch**_ \[buːx\] "book" <!--SR:!2026-12-08,218,170-->
- [voiceless uvular fricative](voiceless%20uvular%20fricative.md):@:[French](French%20language.md) _t**r**ès_ \[t̪χɛ\] "very" <!--SR:!fsrs,2026-11-29T00:00:00.000Z,149,149.29286638,9.98522837,2,8,0,0,2026-07-03T00:00:00.000Z-->
- [close front rounded vowel](close%20front%20rounded%20vowel.md):@:[French](French%20language.md) _t**u**_ \[t̪y] "you" <!--SR:!2026-12-24,567,210-->
- [near-close near-front rounded vowel](near-close%20near-front%20rounded%20vowel.md):@:[German](German%20language.md) _sch**ü**tzen_ \[ˈʃʏ̞t͡sn̩\] "protect" <!--SR:!2026-07-25,57,130-->
- [voiced velar fricative](voiced%20velar%20fricative.md):@:[Spanish](Spanish%20language.md) _ami**g**o_ \[a̠ˈmiɣo̟\] "friend" <!--SR:!fsrs,2026-07-17T15:30:53.438Z,33,33.00436459,9.98522837,2,6,0,0,2026-06-14T15:30:53.438Z-->
- [close-mid back unrounded vowel](close-mid%20back%20unrounded%20vowel.md):@:[Chinese](Chinese%20language.md) 餓/_**è**_ \[ɤ˥˩\] "hungry" <!--SR:!fsrs,2026-07-20T05:54:27.035Z,35,35.22317512,9.98522837,2,6,0,0,2026-06-15T05:54:27.035Z-->
- [voiced palatal lateral approximant](voiced%20palatal%20lateral%20approximant.md):@:[English](English%20language.md) _mi**lli**on_ \[ˈmɪʎən\] <!--SR:!2026-10-03,152,150-->
- [voiced labial–palatal approximant](voiced%20labial–palatal%20approximant.md):@:[French](French%20language.md) _n**u**ire_ \[nɥiʁ\] "to harm" <!--SR:!fsrs,2026-07-26T00:00:00.000Z,18,17.88367862,9.95572941,2,6,0,0,2026-07-08T00:00:00.000Z-->
- [voiced alveolar fricative](voiced%20alveolar%20fricative.md):@:[English](English%20language.md) _**z**oo_ \[z̪ʏˑy̯\] <!--SR:!2027-09-16,548,190-->
- [voiced postalveolar fricative](voiced%20postalveolar%20fricative.md):@:[English](English%20language.md) _vi**si**on_ \[ˈvɪʒən\] <!--SR:!2026-10-24,173,190-->
- [voiced alveolo–palatal fricative](voiced%20alveolo–palatal%20fricative.md):@:[Japanese](Japanese%20language.md) 火事/_ka**j**i_ \[kaʑi\] "fire" <!--SR:!fsrs,2026-08-05T00:00:00.000Z,23,23.37402747,9.9507836,2,6,0,0,2026-07-13T00:00:00.000Z-->
- [voiced retroflex fricative](voiced%20retroflex%20fricative.md):@:[Russian](Russian%20language.md) _**ж**ена_ \[ʐɨ̞ˈna\] "wife" <!--SR:!fsrs,2026-07-21T00:00:00.000Z,15,14.86765584,9.96067523,2,6,0,0,2026-07-06T00:00:00.000Z-->
- [voiceless dental fricative](voiceless%20dental%20fricative.md):@:[English](English%20language.md) _**th**in_ \[θɪn\] <!--SR:!2028-02-13,900,250-->
- [voiceless bilabial fricative](voiceless%20bilabial%20fricative.md):@:[Japanese](Japanese%20language.md) 腐敗/_**f**uhai_ \[ɸɯhai\] "decay" <!--SR:!fsrs,2026-10-18T00:00:00.000Z,99,98.68678895,9.23597837,2,7,0,0,2026-07-11T00:00:00.000Z-->
- [glottal stop](glottal%20stop.md):@:[English](English%20language.md) _uh-oh_ \[ˈɐʔəʊ\] <!--SR:!2026-11-25,538,230-->
- [voiced pharyngeal fricative](voiced%20pharyngeal%20fricative.md):@:[Arabic](Arabic%20language.md) _عَقْرَب/ʿaqrab_ \[ʕaqrab\] "scorpion" <!--SR:!2026-09-16,135,130-->
- [tenuis dental click](tenuis%20dental%20click.md):@:[English](English%20language.md) _**tut**-**tut**_ \[ˈǀˈǀ\] <!--SR:!2028-12-21,1069,270-->
- [tenuis alveolar lateral click](tenuis%20alveolar%20lateral%20click.md):@:[English](English%20language.md) _**tchick**_ \[ˈǁ\] <!--SR:!2026-10-20,258,210-->
- [tenuis alveolar click](tenuis%20alveolar%20click.md):@:[Zulu](Zulu%20language.md) _i**q**a**q**a_ \[íːk͜ǃaːk͜ǃá\] "polecat" <!--SR:!fsrs,2026-09-25T00:00:00.000Z,91,91.47220885,9.98522837,2,7,0,0,2026-06-26T00:00:00.000Z-->
- [tenuis bilabial click](tenuis%20bilabial%20click.md):@:[ǂʼAmkoe](ǂʼAmkoe%20language.md) _**ʘ**oa_ \[k͡ʘoa\] "two" <!--SR:!2026-09-06,125,150-->
- [tenuis palatal click](tenuis%20palatal%20click.md):@:[Khoekhoe](Khoekhoe%20lalnguage.md) _**ǂg**ā-amǃnâ_ \[k͜ǂààʔám̀ŋ͜ǃã̀ã̀\] "to put in the mouth" <!--SR:!fsrs,2026-09-01T05:53:21.721Z,78,78.04297264,9.98522837,2,7,0,0,2026-06-15T05:53:21.721Z-->

<!--/pytextgen-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--pytextgen generate section="485d"--><!-- The following content is generated at 2026-01-26T13:41:30.378520+08:00. Any edits will be overridden! -->

> | name                                        | symbol                      | description                                                                |
> | ------------------------------------------- | --------------------------- | -------------------------------------------------------------------------- |
> | [nasalized](nasal%20vowel.md)               | \[◌̃\] (e.g. [ã])            | [French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine" |
> | [centralized](central%20vowel.md)           | \[◌̈\] (e.g. [ä])            | [Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go"                |
> | [extra-short](extra-shortness.md)           | \[◌̆\] (e.g. [ă])            | [English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\]                  |
> | [non-syllabic](diphthong.md)                | \[◌̯\] (e.g. [a̯])            | [English](English%20language.md) _co**w**_ \[kʰaʊ̯\]                        |
> | [voiceless](voicelessness.md)               | \[◌̥\] (e.g. [n̥])            | [English](English%20language.md) _**d**oe_ \[d̥oʊ̯\]                         |
> | [syllabic](syllabic%20consonant.md)         | \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) | [English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\]                    |
> | [dental/alveolar](dental%20consonant.md)    | \[◌̪\] (e.g. [d̪])            | [Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two"                  |
> | [aspirated](aspirated%20consonant.md)       | \[◌ʰ\] (e.g. [kʰ])          | [English](English%20language.md) _**c**ome_ \[kʰɐm\]                       |
> | [ejective](ejective%20consonant.md)         | \[◌’\] (e.g. [k’])          | [Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come"                  |
> | [long](longness%20(phonetics).md)           | \[◌ː\] (e.g. [aː])          | [English](English%20language.md) _shh!_ \[ʃː\]                             |
> | [half-long](half-longness%20(phonetics).md) | \[◌ˑ\] (e.g. [aˑ])          | [English](English%20language.md) _caught_ \[ˈkʰɔˑt\]                       |
> | [primary stress](stress%20(lingustics).md)  | \[ˈ◌\] (e.g. [ˈa])          | [English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]       |
> | [secondary stress](secondary%20stress.md)   | \[ˌ◌\] (e.g. [ˌa])          | [English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\]       |
> | [syllable break](syllable.md)               | \[.\]                       | [English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\]                |

<!--/pytextgen-->

#### name–symbol (diacritics)

<!--pytextgen generate section="ffa2"--><!-- The following content is generated at 2024-01-04T20:18:01.097852+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md):@:\[◌̃\] (e.g. [ã]) <!--SR:!2034-07-24,3157,391-->
- [centralized](central%20vowel.md):@:\[◌̈\] (e.g. [ä]) <!--SR:!2031-04-11,2136,394-->
- [extra-short](extra-shortness.md):@:\[◌̆\] (e.g. [ă]) <!--SR:!2026-07-17,107,150-->
- [non-syllabic](diphthong.md):@:\[◌̯\] (e.g. [a̯]) <!--SR:!2029-03-22,1442,334-->
- [voiceless](voicelessness.md):@:\[◌̥\] (e.g. [n̥]) <!--SR:!2027-04-29,817,294-->
- [syllabic](syllabic%20consonant.md):@:\[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]) <!--SR:!2026-10-20,828,341-->
- [dental/alveolar](dental%20consonant.md):@:\[◌̪\] (e.g. [d̪]) <!--SR:!2027-11-17,873,360-->
- [aspirated](aspirated%20consonant.md):@:\[◌ʰ\] (e.g. [kʰ]) <!--SR:!2033-02-25,2759,380-->
- [ejective](ejective%20consonant.md):@:\[◌’\] (e.g. [k’]) <!--SR:!2029-07-23,1552,373-->
- [long](longness%20(phonetics).md):@:\[◌ː\] (e.g. [aː]) <!--SR:!2033-08-18,2906,381-->
- [half-long](half-longness%20(phonetics).md):@:\[◌ˑ\] (e.g. [aˑ]) <!--SR:!2029-01-08,1385,374-->
- [primary stress](stress%20(lingustics).md):@:\[ˈ◌\] (e.g. [ˈa]) <!--SR:!2030-09-15,2003,392-->
- [secondary stress](secondary%20stress.md):@:\[ˌ◌\] (e.g. [ˌa]) <!--SR:!2026-11-10,802,352-->
- [syllable break](syllable.md):@:\[.\] <!--SR:!2031-11-06,2260,396-->

<!--/pytextgen-->

<!--pytextgen generate section="94fb"--><!-- The following content is generated at 2024-01-04T20:17:59.931857+08:00. Any edits will be overridden! -->

- \[◌̃\] (e.g. [ã]):@:[nasalized](nasal%20vowel.md) <!--SR:!2026-07-18,727,290-->
- \[◌̈\] (e.g. [ä]):@:[centralized](central%20vowel.md) <!--SR:!2028-09-01,1336,318-->
- \[◌̆\] (e.g. [ă]):@:[extra-short](extra-shortness.md) <!--SR:!2029-01-01,1306,284-->
- \[◌̯\] (e.g. [a̯]):@:[non-syllabic](diphthong.md) <!--SR:!2027-03-11,595,204-->
- \[◌̥\] (e.g. [n̥]):@:[voiceless](voicelessness.md) <!--SR:!2027-10-27,1097,313-->
- \[◌̩\]/\[◌̍\] (e.g. [n̩], [ŋ̍]):@:[syllabic](syllabic%20consonant.md) <!--SR:!2026-07-18,687,298-->
- \[◌̪\] (e.g. [d̪]):@:[dental/alveolar](dental%20consonant.md) <!--SR:!2030-11-14,1829,318-->
- \[◌ʰ\] (e.g. [kʰ]):@:[aspirated](aspirated%20consonant.md) <!--SR:!2034-03-27,2859,358-->
- \[◌’\] (e.g. [k’]):@:[ejective](ejective%20consonant.md) <!--SR:!2027-02-01,896,318-->
- \[◌ː\] (e.g. [aː]):@:[long](longness%20(phonetics).md) <!--SR:!2033-03-04,2762,377-->
- \[◌ˑ\] (e.g. [aˑ]):@:[half-long](half-longness%20(phonetics).md) <!--SR:!2026-08-11,460,291-->
- \[ˈ◌\] (e.g. [ˈa]):@:[primary stress](stress%20(lingustics).md) <!--SR:!2027-04-15,1029,357-->
- \[ˌ◌\] (e.g. [ˌa]):@:[secondary stress](secondary%20stress.md) <!--SR:!2029-06-14,1570,361-->
- \[.\]:@:[syllable break](syllable.md) <!--SR:!2030-11-09,1961,396-->

<!--/pytextgen-->

#### name–description (diacritics)

<!--pytextgen generate section="50bd"--><!-- The following content is generated at 2024-01-04T20:18:01.248419+08:00. Any edits will be overridden! -->

- [nasalized](nasal%20vowel.md):@:[French](French%20language.md) _vi**n** bla**n**c_ \[vɛ̃ blɑ̃\] "white wine" <!--SR:!2026-10-29,153,178-->
- [centralized](central%20vowel.md):@:[Portuguese](Protuguese%20language.md) _v**á**_ \[vä\] "go" <!--SR:!2027-05-23,618,204-->
- [extra-short](extra-shortness.md):@:[English](English%20language.md) _p**o**lice_ \[pə̆ˈliˑs\] <!--SR:!2027-07-08,791,244-->
- [non-syllabic](diphthong.md):@:[English](English%20language.md) _co**w**_ \[kʰaʊ̯\] <!--SR:!2027-02-18,935,313-->
- [voiceless](voicelessness.md):@:[English](English%20language.md) _**d**oe_ \[d̥oʊ̯\] <!--SR:!2029-12-07,1647,338-->
- [syllabic](syllabic%20consonant.md):@:[English](English%20language.md) _butt**on**_ \[ˈbʌʔn̩\] <!--SR:!2027-03-23,469,218-->
- [dental/alveolar](dental%20consonant.md):@:[Spanish](Spanish%20language.md) _**d**os_ \[ˈd̪os\] "two" <!--SR:!2027-02-23,295,278-->
- [aspirated](aspirated%20consonant.md):@:[English](English%20language.md) _**c**ome_ \[kʰɐm\] <!--SR:!2031-12-09,2245,358-->
- [ejective](ejective%20consonant.md):@:[Zulu](Zulu%20language.md) _u**k**uza_ \[uˈɠuːza\] "come" <!--SR:!2026-12-03,546,197-->
- [long](longness%20(phonetics).md):@:[English](English%20language.md) _shh!_ \[ʃː\] <!--SR:!2028-07-25,1278,338-->
- [half-long](half-longness%20(phonetics).md):@:[English](English%20language.md) _caught_ \[ˈkʰɔˑt\] <!--SR:!2029-08-10,1403,279-->
- [primary stress](stress%20(lingustics).md):@:[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2032-02-23,2274,331-->
- [secondary stress](secondary%20stress.md):@:[English](English%20language.md) _pronunciation_ \[pɹ̥əʊ̯ˌnɐnsiˈeɪʃn̩\] <!--SR:!2028-09-21,1204,312-->
- [syllable break](syllable.md):@:[English](English%20language.md) _courtship_ \[ˈkʰɔrt.ʃɪp\] <!--SR:!2027-12-26,986,290-->

<!--/pytextgen-->
