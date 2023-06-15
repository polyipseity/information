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
		('[[a](open%20front%20unrounded%20vowel.md)]', '![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)', '',),
		('[[ä](open%20central%20unrounded%20vowel.md)]', '![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)', '',),
		('[[ɐ](near-open%20central%20vowel.md)]', '![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)', '',),
		('[[ɑ](open%20back%20unrounded%20vowel.md)]', '![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)', '',),
		('[[ɑ̃](nasal%20vowel.md)]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)', '',),
		('[[ɒ](open%20back%20rounded%20vowel.md)]', '![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)', '',),
		('[[ʌ](open-mid%20back%20unrounded%20vowel.md)]', '![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)', '',),
		('[[æ](near-open%20front%20unrounded%20vowel.md)]', '![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)', '',),
		('[[b](voiced%20bilabial%20plosive.md)]', '![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)', '',),
		('[[ɓ](voiced%20bilabial%20implosive.md)]', '![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)', '',),
		('[[β](voiced%20bilabial%20fricative.md)]', '![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)', '',),
		('[[ʙ](voiced%20bilabial%20trill.md)]', '![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)', '',),
		('[[c](voiceless%20palatal%20plosive.md)]', '![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)', '',),
		('[[ç](voiceless%20palatal%20fricative.md)]', '![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)', '',),
		('[[ɕ](voiceless%20alveolo-palatal%20fricative.md)]', '![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)', '',),
		('[[ɔ](open-mid%20back%20rounded%20vowel.md)]', '![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)', '',),
		('[[d](voiced%20alveolar%20plosive.md)]', '![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)', '',),
		('[[ɗ](voiced%20alveolar%20implosive.md)]', '![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)', '',),
		('[[ɖ](voiced%20retroflex%20plosive.md)]', '![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)', '',),
		('[[ð](voiced%20dental%20fricative.md)]', '![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)', '',),
		('[[dz](voiced%20alveolar%20affricate.md)]', '![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)', '',),
		('[[dʒ](voiced%20postalveolar%20affricate.md)]', '![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)', '',),
		('[[dʑ](voiced%20alveolo-palatal%20affricate.md)]', '![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)', '',),
		('[[dʐ](voiced%20retroflex%20affricate.md)]', '![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)', '',),
		('[[e](close-mid%20front%20unrounded%20vowel.md)]', '![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)', '',),
		('[[ɘ](close-mid%20central%20unrounded%20vowel.md)]', '![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)', '',),
		('[[ə](mid%20central%20vowel.md)]', '![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)', '',),
		('[[ɚ](r-colored%20vowel.md)]', '![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', '',),
		('[[ɛ](open-mid%20front%20unrounded%20vowel.md)]', '![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)', '',),
		('[[ɛ̃](nasal%20vowel.md)]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)', '',),
		('[[ɜ](open-mid%20central%20unrounded%20vowel.md)]', '![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)', '',),
		('[[ɝ](r-colored%20vowel.md)]', '![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)', '',),
		('[[f](voiceless%20labiodental%20fricative.md)]', '![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)', '',),
		('[[ɟ](voiced%20palatal%20plosive.md)]', '![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)', '',),
		('[[ʄ](voiced%20palatal%20implosive.md)]', '![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)', '',),
		('[[ɡ](voiced%20velar%20plosive.md)]', '![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)', '',),
		('[[ɠ](voiced%20velar%20implosive.md)]', '![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)', '',),
		('[[ɢ](voiced%20uvular%20plosive.md)]', '![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)', '',),
		('[[ʒ](voiced%20postalveolar%20fricative.md)]', '![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)', '',),
		('[[h](voiceless%20glottal%20fricative.md)]', '![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)', '',),
		('[[ɦ](voiced%20glottal%20fricative.md)]', '![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)', '',),
		('[[ʰ](aspirated%20consonant.md)]', '', '',),
		('[[ħ](voiceless%20pharyngeal%20fricative.md)]', '![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)', '',),
		('[[ɥ](voiced%20labial–palatal%20approximant.md)]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', '',),
		('[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', '',),
		('[[i](close%20front%20unrounded%20vowel.md)]', '![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)', '',),
		('[[ɪ](near-close%20near-front%20unrounded%20vowel.md)]', '![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)', '',),
		('[[ɨ](close%20central%20unrounded%20vowel.md)]', '![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)', '',),
		('[[j](voiced%20palatal%20approximant.md)]', '![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)', '',),
		('[[ʲ](palatalization%20(phonetics).md)]', '', '',),
		('[[ʝ](voiced%20palatal%20fricative.md)]', '![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)', '',),
		('[[ɟ](voiced%20palatal%20plosive.md)]', '![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)', '',),
		('[[ʄ](voiced%20palatal%20implosive.md)]', '![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)', '',),
		('[[k](voiceless%20velar%20plosive.md)]', '![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)', '',),
		('[[l](voiced%20alveolar%20lateral%20approximant.md)]', '![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)', '',),
		('[[ɫ](velarized%20alveolar%20lateral%20approximant.md)]', '![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)', '',),
		('[[ɬ](voiceless%20alveolar%20lateral%20fricative.md)]', '![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)', '',),
		('[[ɭ](voiced%20retroflex%20lateral%20approximant.md)]', '![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)', '',),
		('[[ɺ](voiced%20alveolar%20lateral%20flap.md)]', '', '',),
		('[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', '',),
		('[[ʟ](voiced%20velar%20lateral%20approximant.md)]', '![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)', '',),
		('[[m](voiced%20bilabial%20nasal.md)]', '![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)', '',),
		('[[ɱ](voiced%20labiodental%20nasal.md)]', '![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)', '',),
		('[[ɯ](close%20back%20unrounded%20vowel.md)]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', '',),
		('[[ʍ](voiceless%20labial–velar%20fricative.md)]', '![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)', '',),
		('[[n](voiced%20alveolar%20nasal.md)]', '![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)', '',),
		('[[ŋ](voiced%20velar%20nasal.md)]', '![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)', '',),
		('[[ɲ](voiced%20palatal%20nasal.md)]', '![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)', '',),
		('[[ɳ](voiced%20retroflex%20nasal.md)]', '![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)', '',),
		('[[ɴ](voiced%20uvular%20nasal.md)]', '![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)', '',),
		('[[o](close-mid%20back%20rounded%20vowel.md)]', '![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)', '',),
		('[[ɔ](open-mid%20back%20rounded%20vowel.md)]', '![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)', '',),
		('[[ɔ̃](nasal%20vowel.md)]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)', '',),
		('[[ø](close-mid%20front%20rounded%20vowel.md)]', '![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)', '',),
		('[[ɵ](close-mid%20central%20rounded%20vowel.md)]', '![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)', '',),
		('[[œ](open-mid%20front%20rounded%20vowel.md)]', '![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)', '',),
		('[[œ̃](nasal%20vowel.md)]', '![nasal vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)', '',),
		('[[ɶ](open%20front%20rounded%20vowel.md)]', '![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)', '',),
		('[[θ](voiceless%20dental%20fricative.md)]', '![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)', '',),
		('[[ɸ](voiceless%20bilabial%20fricative.md)]', '![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)', '',),
		('[[p](voiceless%20bilabial%20plosive.md)]', '![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)', '',),
		('[[q](voiceless%20uvular%20plosive.md)]', '![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)', '',),
		('[[r](voiced%20alveolar%20trill.md)]', '![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)', '',),
		('[[ɾ](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)]', '![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)', '',),
		('[[ʀ](voiced%20uvular%20trill.md)]', '![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)', '',),
		('[[ɽ](voiced%20retroflex%20flap.md)]', '![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)', '',),
		('[[ɹ](voiced%20alveolar%20approximant.md)]', '![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)', '',),
		('[[ɻ](voiced%20retroflex%20approximant.md)]', '![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)', '',),
		('[[ʁ](voiced%20uvular%20fricative.md)]', '![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)', '',),
		('[[s](voiceless%20alveolar%20fricative.md)]', '![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)', '',),
		('[[ʃ](voiceless%20postalveolar%20fricative.md)]', '![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)', '',),
		('[[ʂ](voiceless%20retroflex%20fricative.md)]', '![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)', '',),
		('[[t](voiceless%20alveolar%20plosive.md)]', '![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)', '',),
		('[[ʈ](voiceless%20retroflex%20plosive.md)]', '![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)', '',),
		('[[ts](voiceless%20alveolar%20affricate.md)]', '![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)', '',),
		('[[tʃ](voiceless%20postalveolar%20affricate.md)]', '![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)', '',),
		('[[tɕ](voiceless%20alveolo-palatal%20affricate.md)]', '![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)', '',),
		('[[tɕ](voiceless%20alveolo-palatal%20affricate.md)]', '![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Zh-Beijing.ogg)', '',),
		('[[tʂ](voiceless%20retroflex%20affricate.md)]', '![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)', '',),
		('[[u](close%20back%20rounded%20vowel.md)]', '![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)', '',),
		('[[ʊ](near-close%20near-back%20rounded%20vowel.md)]', '![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)', '',),
		('[[ʉ](close%20central%20rounded%20vowel.md)]', '![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)', '',),
		('[[ɥ](voiced%20labial–palatal%20approximant.md)]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', '',),
		('[[ɯ](close%20back%20unrounded%20vowel.md)]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', '',),
		('[[v](voiced%20labiodental%20fricative.md)]', '![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)', '',),
		('[[ʋ](voiced%20labiodental%20approximant.md)]', '![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)', '',),
		('[[ɤ](close-mid%20back%20unrounded%20vowel.md)]', '![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)', '',),
		('[[ɣ](voiced%20velar%20fricative.md)]', '![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)', '',),
		('[[ʌ](open-mid%20back%20unrounded%20vowel.md)]', '![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)', '',),
		('[[w](voiced%20labial–velar%20approximant.md)]', '![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)', '',),
		('[[ʷ](labialization.md)]', '', '',),
		('[[ʍ](voiceless%20labial–velar%20fricative.md)]', '![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)', '',),
		('[[ɯ](close%20back%20unrounded%20vowel.md)]', '![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)', '',),
		('[[ɰ](voiced%20velar%20approximant.md)]', '![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)', '',),
		('[[x](voiceless%20velar%20fricative.md)]', '![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)', '',),
		('[[χ](voiceless%20uvular%20fricative.md)]', '![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)', '',),
		('[[y](close%20front%20rounded%20vowel.md)]', '![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)', '',),
		('[[ʏ](near-close%20near-front%20rounded%20vowel.md)]', '![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)', '',),
		('[[ɣ](voiced%20velar%20fricative.md)]', '![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)', '',),
		('[[ɤ](close-mid%20back%20unrounded%20vowel.md)]', '![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)', '',),
		('[[ʎ](voiced%20palatal%20lateral%20approximant.md)]', '![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)', '',),
		('[[ɥ](voiced%20labial–palatal%20approximant.md)]', '![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)', '',),
		('[[z](voiced%20alveolar%20fricative.md)]', '![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)', '',),
		('[[ʒ](voiced%20postalveolar%20fricative.md)]', '![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)', '',),
		('[[ʑ](voiced%20alveolo-palatal%20fricative.md)]', '![voiced alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)', '',),
		('[[ʐ](voiced%20retroflex%20fricative.md)]', '![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)', '',),
		('[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]', '![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)', '',),
		('[[θ](voiceless%20dental%20fricative.md)]', '![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)', '',),
		('[[ɸ](voiceless%20bilabial%20fricative.md)]', '![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)', '',),
		('[[ʔ](glottal%20stop.md)]', '![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)', '',),
		('[[ʕ](voiced%20pharyngeal%20fricative.md)]', '![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)', '',),
		('[[ǀ](tenuis%20dental%20click.md)]', '![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)', '',),
		('[[ǁ](tenuis%20alveolar%20lateral%20click.md)]', '![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)', '',),
		('[[ǃ](tenuis%20alveolar%20click.md)]', '![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)', '',),
		('[[ʘ](tenuis%20bilabial%20click.md)]', '![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)', '',),
		('[[ǂ](tenuis%20palatal%20click.md)]', '![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)', '',),
	),
	lambda datum: map(cloze, datum),
), memorize_table(
	(*e.cwf_sects("485d"), NULL_LOCATION,),
	("symbol", "description",),
	(
		(R"[\[◌̃\]](nasal%20vowel.md) (e.g. [ã])", "",),
		(R"[\[◌̈\]](central%20vowel.md) (e.g. [ä])", "",),
		(R"[\[◌̆\]](extra-shortness.md) (e.g. [ă])", "",),
		(R"[\[◌̯\]](diphthong.md) (e.g. [a̯])", "",),
		(R"[\[◌̥\]](voicelessness.md) (e.g. [n̥])", "",),
		(R"[\[◌̩\], \[◌̍\]](syllabic%20consonant.md) (e.g. [n̩], [ŋ̍])", "",),
		(R"[\[◌̪\]](dental%20consonant.md) (e.g. [d̪])", "",),
		(R"[\[◌ʰ\]](aspirated%20consonant.md) (e.g. [kʰ])", "",),
		(R"[\[◌’\]](ejective%20consonant.md) (e.g. [k’])", "",),
		(R"[\[◌ː\]](longness%20(phonetics).md) (e.g. [aː])", "",),
		(R"[\[◌ˑ\]](half-longness%20(phonetics).md) (e.g. [aˑ])", "",),
		(R"[\[ˈ◌\]](stress%20(lingustics).md) (e.g. [ˈa])", "",),
		(R"[\[ˌ◌\]](secondary%20stress.md) (e.g. [ˌa])", "",),
		(R"[\[.\]](syllable.md)", "",),
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="958a"--><!-- The following content is generated at 2023-06-15T11:47:21.600228+08:00. Any edits will be overridden! -->

> | symbol | audio&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | description |
> |-|-|-|
> | {{[[a](open%20front%20unrounded%20vowel.md)]}} | {{![open front unrounded vowel](../../archives/Wikimedia%20Commons/PR-open%20front%20unrounded%20vowel.ogg)}} |  |
> | {{[[ä](open%20central%20unrounded%20vowel.md)]}} | {{![open central unrounded vowel](../../archives/Wikimedia%20Commons/Open%20central%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɐ](near-open%20central%20vowel.md)]}} | {{![near-open central vowel](../../archives/Wikimedia%20Commons/Near-open%20central%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɑ](open%20back%20unrounded%20vowel.md)]}} | {{![open back unrounded vowel](../../archives/Wikimedia%20Commons/Open%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɑ̃](nasal%20vowel.md)]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-en.ogg)}} |  |
> | {{[[ɒ](open%20back%20rounded%20vowel.md)]}} | {{![open back rounded vowel](../../archives/Wikimedia%20Commons/PR-open%20back%20rounded%20vowel.ogg)}} |  |
> | {{[[ʌ](open-mid%20back%20unrounded%20vowel.md)]}} | {{![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)}} |  |
> | {{[[æ](near-open%20front%20unrounded%20vowel.md)]}} | {{![near-open front unrounded vowel](../../archives/Wikimedia%20Commons/Near-open%20front%20unrounded%20vowel.ogg)}} |  |
> | {{[[b](voiced%20bilabial%20plosive.md)]}} | {{![voiced bilabial plosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20plosive.ogg)}} |  |
> | {{[[ɓ](voiced%20bilabial%20implosive.md)]}} | {{![voiced bilabial implosive](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20implosive.ogg)}} |  |
> | {{[[β](voiced%20bilabial%20fricative.md)]}} | {{![voiced bilabial fricative](../../archives/Wikimedia%20Commons/Voiced%20bilabial%20fricative.ogg)}} |  |
> | {{[[ʙ](voiced%20bilabial%20trill.md)]}} | {{![voiced bilabial trill](../../archives/Wikimedia%20Commons/Bilabial%20trill.ogg)}} |  |
> | {{[[c](voiceless%20palatal%20plosive.md)]}} | {{![voiceless palatal plosive](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20plosive.ogg)}} |  |
> | {{[[ç](voiceless%20palatal%20fricative.md)]}} | {{![voiceless palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20palatal%20fricative.ogg)}} |  |
> | {{[[ɕ](voiceless%20alveolo-palatal%20fricative.md)]}} | {{![voiceless alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20sibilant.ogg)}} |  |
> | {{[[ɔ](open-mid%20back%20rounded%20vowel.md)]}} | {{![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)}} |  |
> | {{[[d](voiced%20alveolar%20plosive.md)]}} | {{![voiced alveolar plosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20plosive.ogg)}} |  |
> | {{[[ɗ](voiced%20alveolar%20implosive.md)]}} | {{![voiced alveolar implosive](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20implosive.ogg)}} |  |
> | {{[[ɖ](voiced%20retroflex%20plosive.md)]}} | {{![voiced retroflex plosive](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20stop.oga)}} |  |
> | {{[[ð](voiced%20dental%20fricative.md)]}} | {{![voiced dental fricative](../../archives/Wikimedia%20Commons/Voiced%20dental%20fricative.ogg)}} |  |
> | {{[[dz](voiced%20alveolar%20affricate.md)]}} | {{![voiced alveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant%20affricate.oga)}} |  |
> | {{[[dʒ](voiced%20postalveolar%20affricate.md)]}} | {{![voiced postalveolar affricate](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20affricate.ogg)}} |  |
> | {{[[dʑ](voiced%20alveolo-palatal%20affricate.md)]}} | {{![voiced alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20affricate.ogg)}} |  |
> | {{[[dʐ](voiced%20retroflex%20affricate.md)]}} | {{![voiced retroflex affricate](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20affricate.ogg)}} |  |
> | {{[[e](close-mid%20front%20unrounded%20vowel.md)]}} | {{![close-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɘ](close-mid%20central%20unrounded%20vowel.md)]}} | {{![close-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20unrounded%20vowel.ogg)}} |  |
> | {{[[ə](mid%20central%20vowel.md)]}} | {{![mid central vowel](../../archives/Wikimedia%20Commons/Mid-central%20vowel.ogg)}} |  |
> | {{[[ɚ](r-colored%20vowel.md)]}} | {{![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)}} |  |
> | {{[[ɛ](open-mid%20front%20unrounded%20vowel.md)]}} | {{![open-mid front unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɛ̃](nasal%20vowel.md)]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-Un-fr%20FR-Paris.ogg)}} |  |
> | {{[[ɜ](open-mid%20central%20unrounded%20vowel.md)]}} | {{![open-mid central unrounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20central%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɝ](r-colored%20vowel.md)]}} | {{![r-colored vowel](../../archives/Wikimedia%20Commons/En-us-er.ogg)}} |  |
> | {{[[f](voiceless%20labiodental%20fricative.md)]}} | {{![voiceless labiodental fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-dental%20fricative.ogg)}} |  |
> | {{[[ɟ](voiced%20palatal%20plosive.md)]}} | {{![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)}} |  |
> | {{[[ʄ](voiced%20palatal%20implosive.md)]}} | {{![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)}} |  |
> | {{[[ɡ](voiced%20velar%20plosive.md)]}} | {{![voiced velar plosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20plosive%2002.ogg)}} |  |
> | {{[[ɠ](voiced%20velar%20implosive.md)]}} | {{![voiced velar implosive](../../archives/Wikimedia%20Commons/Voiced%20velar%20implosive.ogg)}} |  |
> | {{[[ɢ](voiced%20uvular%20plosive.md)]}} | {{![voiced uvular plosive](../../archives/Wikimedia%20Commons/Voiced%20uvular%20stop.oga)}} |  |
> | {{[[ʒ](voiced%20postalveolar%20fricative.md)]}} | {{![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)}} |  |
> | {{[[h](voiceless%20glottal%20fricative.md)]}} | {{![voiceless glottal fricative](../../archives/Wikimedia%20Commons/Voiceless%20glottal%20fricative.ogg)}} |  |
> | {{[[ɦ](voiced%20glottal%20fricative.md)]}} | {{![voiced glottal fricative](../../archives/Wikimedia%20Commons/Voiced%20glottal%20fricative.ogg)}} |  |
> | {{[[ʰ](aspirated%20consonant.md)]}} |  |  |
> | {{[[ħ](voiceless%20pharyngeal%20fricative.md)]}} | {{![voiceless pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiceless%20pharyngeal%20fricative.ogg)}} |  |
> | {{[[ɥ](voiced%20labial–palatal%20approximant.md)]}} | {{![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)}} |  |
> | {{[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]}} | {{![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)}} |  |
> | {{[[i](close%20front%20unrounded%20vowel.md)]}} | {{![close front unrounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɪ](near-close%20near-front%20unrounded%20vowel.md)]}} | {{![near-close near-front unrounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɨ](close%20central%20unrounded%20vowel.md)]}} | {{![close central unrounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20unrounded%20vowel.ogg)}} |  |
> | {{[[j](voiced%20palatal%20approximant.md)]}} | {{![voiced palatal approximant](../../archives/Wikimedia%20Commons/Palatal%20approximant.ogg)}} |  |
> | {{[[ʲ](palatalization%20(phonetics).md)]}} |  |  |
> | {{[[ʝ](voiced%20palatal%20fricative.md)]}} | {{![voiced palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20palatal%20fricative.ogg)}} |  |
> | {{[[ɟ](voiced%20palatal%20plosive.md)]}} | {{![voiced palatal plosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20plosive.ogg)}} |  |
> | {{[[ʄ](voiced%20palatal%20implosive.md)]}} | {{![voiced palatal implosive](../../archives/Wikimedia%20Commons/Voiced%20palatal%20implosive.ogg)}} |  |
> | {{[[k](voiceless%20velar%20plosive.md)]}} | {{![voiceless velar plosive](../../archives/Wikimedia%20Commons/Voiceless%20velar%20plosive.ogg)}} |  |
> | {{[[l](voiced%20alveolar%20lateral%20approximant.md)]}} | {{![voiced alveolar lateral approximant](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20approximant.ogg)}} |  |
> | {{[[ɫ](velarized%20alveolar%20lateral%20approximant.md)]}} | {{![velarized alveolar lateral approximant](../../archives/Wikimedia%20Commons/Velarized%20alveolar%20lateral%20approximant.ogg)}} |  |
> | {{[[ɬ](voiceless%20alveolar%20lateral%20fricative.md)]}} | {{![voiceless alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20lateral%20fricative.ogg)}} |  |
> | {{[[ɭ](voiced%20retroflex%20lateral%20approximant.md)]}} | {{![voiced retroflex lateral approximant](../../archives/Wikimedia%20Commons/Retroflex%20lateral%20approximant.ogg)}} |  |
> | {{[[ɺ](voiced%20alveolar%20lateral%20flap.md)]}} |  |  |
> | {{[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]}} | {{![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)}} |  |
> | {{[[ʟ](voiced%20velar%20lateral%20approximant.md)]}} | {{![voiced velar lateral approximant](../../archives/Wikimedia%20Commons/Velar%20lateral%20approximant.ogg)}} |  |
> | {{[[m](voiced%20bilabial%20nasal.md)]}} | {{![voiced bilabial nasal](../../archives/Wikimedia%20Commons/Bilabial%20nasal.ogg)}} |  |
> | {{[[ɱ](voiced%20labiodental%20nasal.md)]}} | {{![voiced labiodental nasal](../../archives/Wikimedia%20Commons/Labiodental%20nasal.ogg)}} |  |
> | {{[[ɯ](close%20back%20unrounded%20vowel.md)]}} | {{![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[ʍ](voiceless%20labial–velar%20fricative.md)]}} | {{![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)}} |  |
> | {{[[n](voiced%20alveolar%20nasal.md)]}} | {{![voiced alveolar nasal](../../archives/Wikimedia%20Commons/Alveolar%20nasal.ogg)}} |  |
> | {{[[ŋ](voiced%20velar%20nasal.md)]}} | {{![voiced velar nasal](../../archives/Wikimedia%20Commons/Velar%20nasal.ogg)}} |  |
> | {{[[ɲ](voiced%20palatal%20nasal.md)]}} | {{![voiced palatal nasal](../../archives/Wikimedia%20Commons/Palatal%20nasal.ogg)}} |  |
> | {{[[ɳ](voiced%20retroflex%20nasal.md)]}} | {{![voiced retroflex nasal](../../archives/Wikimedia%20Commons/Retroflex%20nasal.ogg)}} |  |
> | {{[[ɴ](voiced%20uvular%20nasal.md)]}} | {{![voiced uvular nasal](../../archives/Wikimedia%20Commons/Uvular%20nasal.ogg)}} |  |
> | {{[[o](close-mid%20back%20rounded%20vowel.md)]}} | {{![close-mid back rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20rounded%20vowel.ogg)}} |  |
> | {{[[ɔ](open-mid%20back%20rounded%20vowel.md)]}} | {{![open-mid back rounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20rounded%20vowel.ogg)}} |  |
> | {{[[ɔ̃](nasal%20vowel.md)]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-on.ogg)}} |  |
> | {{[[ø](close-mid%20front%20rounded%20vowel.md)]}} | {{![close-mid front rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20front%20rounded%20vowel.ogg)}} |  |
> | {{[[ɵ](close-mid%20central%20rounded%20vowel.md)]}} | {{![close-mid central rounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20central%20rounded%20vowel.ogg)}} |  |
> | {{[[œ](open-mid%20front%20rounded%20vowel.md)]}} | {{![open-mid front rounded vowel](../../archives/Wikimedia%20Commons/Open-mid%20front%20rounded%20vowel.ogg)}} |  |
> | {{[[œ̃](nasal%20vowel.md)]}} | {{![nasal vowel](../../archives/Wikimedia%20Commons/Fr-un-fr%20BE.ogg)}} |  |
> | {{[[ɶ](open%20front%20rounded%20vowel.md)]}} | {{![open front rounded vowel](../../archives/Wikimedia%20Commons/Open%20front%20rounded%20vowel.ogg)}} |  |
> | {{[[θ](voiceless%20dental%20fricative.md)]}} | {{![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)}} |  |
> | {{[[ɸ](voiceless%20bilabial%20fricative.md)]}} | {{![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)}} |  |
> | {{[[p](voiceless%20bilabial%20plosive.md)]}} | {{![voiceless bilabial plosive](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20plosive.ogg)}} |  |
> | {{[[q](voiceless%20uvular%20plosive.md)]}} | {{![voiceless uvular plosive](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20plosive.ogg)}} |  |
> | {{[[r](voiced%20alveolar%20trill.md)]}} | {{![voiced alveolar trill](../../archives/Wikimedia%20Commons/Alveolar%20trill.ogg)}} |  |
> | {{[[ɾ](voiced%20dental%20and%20alveolar%20taps%20and%20flaps.md)]}} | {{![voiced dental and alveolar taps and flaps](../../archives/Wikimedia%20Commons/Alveolar%20tap.ogg)}} |  |
> | {{[[ʀ](voiced%20uvular%20trill.md)]}} | {{![voiced uvular trill](../../archives/Wikimedia%20Commons/Uvular%20trill.ogg)}} |  |
> | {{[[ɽ](voiced%20retroflex%20flap.md)]}} | {{![voiced retroflex flap](../../archives/Wikimedia%20Commons/Retroflex%20flap.ogg)}} |  |
> | {{[[ɹ](voiced%20alveolar%20approximant.md)]}} | {{![voiced alveolar approximant](../../archives/Wikimedia%20Commons/Alveolar%20approximant.ogg)}} |  |
> | {{[[ɻ](voiced%20retroflex%20approximant.md)]}} | {{![voiced retroflex approximant](../../archives/Wikimedia%20Commons/Retroflex%20Approximant2.oga)}} |  |
> | {{[[ʁ](voiced%20uvular%20fricative.md)]}} | {{![voiced uvular fricative](../../archives/Wikimedia%20Commons/Voiced%20uvular%20fricative.ogg)}} |  |
> | {{[[s](voiceless%20alveolar%20fricative.md)]}} | {{![voiceless alveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant.ogg)}} |  |
> | {{[[ʃ](voiceless%20postalveolar%20fricative.md)]}} | {{![voiceless postalveolar fricative](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20sibilant.ogg)}} |  |
> | {{[[ʂ](voiceless%20retroflex%20fricative.md)]}} | {{![voiceless retroflex fricative](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20sibilant.ogg)}} |  |
> | {{[[t](voiceless%20alveolar%20plosive.md)]}} | {{![voiceless alveolar plosive](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20plosive.ogg)}} |  |
> | {{[[ʈ](voiceless%20retroflex%20plosive.md)]}} | {{![voiceless retroflex plosive](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20stop.oga)}} |  |
> | {{[[ts](voiceless%20alveolar%20affricate.md)]}} | {{![voiceless alveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolar%20sibilant%20affricate.oga)}} |  |
> | {{[[tʃ](voiceless%20postalveolar%20affricate.md)]}} | {{![voiceless postalveolar affricate](../../archives/Wikimedia%20Commons/Voiceless%20palato-alveolar%20affricate.ogg)}} |  |
> | {{[[tɕ](voiceless%20alveolo-palatal%20affricate.md)]}} | {{![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Voiceless%20alveolo-palatal%20affricate.ogg)}} |  |
> | {{[[tɕ](voiceless%20alveolo-palatal%20affricate.md)]}} | {{![voiceless alveolo-palatal affricate](../../archives/Wikimedia%20Commons/Zh-Beijing.ogg)}} |  |
> | {{[[tʂ](voiceless%20retroflex%20affricate.md)]}} | {{![voiceless retroflex affricate](../../archives/Wikimedia%20Commons/Voiceless%20retroflex%20affricate.ogg)}} |  |
> | {{[[u](close%20back%20rounded%20vowel.md)]}} | {{![close back rounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20rounded%20vowel.ogg)}} |  |
> | {{[[ʊ](near-close%20near-back%20rounded%20vowel.md)]}} | {{![near-close near-back rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-back%20rounded%20vowel.ogg)}} |  |
> | {{[[ʉ](close%20central%20rounded%20vowel.md)]}} | {{![close central rounded vowel](../../archives/Wikimedia%20Commons/Close%20central%20rounded%20vowel.ogg)}} |  |
> | {{[[ɥ](voiced%20labial–palatal%20approximant.md)]}} | {{![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)}} |  |
> | {{[[ɯ](close%20back%20unrounded%20vowel.md)]}} | {{![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[v](voiced%20labiodental%20fricative.md)]}} | {{![voiced labiodental fricative](../../archives/Wikimedia%20Commons/Voiced%20labio-dental%20fricative.ogg)}} |  |
> | {{[[ʋ](voiced%20labiodental%20approximant.md)]}} | {{![voiced labiodental approximant](../../archives/Wikimedia%20Commons/Labiodental%20approximant.ogg)}} |  |
> | {{[[ɤ](close-mid%20back%20unrounded%20vowel.md)]}} | {{![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɣ](voiced%20velar%20fricative.md)]}} | {{![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)}} |  |
> | {{[[ʌ](open-mid%20back%20unrounded%20vowel.md)]}} | {{![open-mid back unrounded vowel](../../archives/Wikimedia%20Commons/PR-open-mid%20back%20unrounded%20vowel2.ogg)}} |  |
> | {{[[w](voiced%20labial–velar%20approximant.md)]}} | {{![voiced labial–velar approximant](../../archives/Wikimedia%20Commons/Voiced%20labio-velar%20approximant.ogg)}} |  |
> | {{[[ʷ](labialization.md)]}} |  |  |
> | {{[[ʍ](voiceless%20labial–velar%20fricative.md)]}} | {{![voiceless labial–velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20labio-velar%20fricative.ogg)}} |  |
> | {{[[ɯ](close%20back%20unrounded%20vowel.md)]}} | {{![close back unrounded vowel](../../archives/Wikimedia%20Commons/Close%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[ɰ](voiced%20velar%20approximant.md)]}} | {{![voiced velar approximant](../../archives/Wikimedia%20Commons/Voiced%20velar%20approximant.ogg)}} |  |
> | {{[[x](voiceless%20velar%20fricative.md)]}} | {{![voiceless velar fricative](../../archives/Wikimedia%20Commons/Voiceless%20velar%20fricative.ogg)}} |  |
> | {{[[χ](voiceless%20uvular%20fricative.md)]}} | {{![voiceless uvular fricative](../../archives/Wikimedia%20Commons/Voiceless%20uvular%20fricative.ogg)}} |  |
> | {{[[y](close%20front%20rounded%20vowel.md)]}} | {{![close front rounded vowel](../../archives/Wikimedia%20Commons/Close%20front%20rounded%20vowel.ogg)}} |  |
> | {{[[ʏ](near-close%20near-front%20rounded%20vowel.md)]}} | {{![near-close near-front rounded vowel](../../archives/Wikimedia%20Commons/Near-close%20near-front%20rounded%20vowel.ogg)}} |  |
> | {{[[ɣ](voiced%20velar%20fricative.md)]}} | {{![voiced velar fricative](../../archives/Wikimedia%20Commons/Voiced%20velar%20fricative.ogg)}} |  |
> | {{[[ɤ](close-mid%20back%20unrounded%20vowel.md)]}} | {{![close-mid back unrounded vowel](../../archives/Wikimedia%20Commons/Close-mid%20back%20unrounded%20vowel.ogg)}} |  |
> | {{[[ʎ](voiced%20palatal%20lateral%20approximant.md)]}} | {{![voiced palatal lateral approximant](../../archives/Wikimedia%20Commons/Palatal%20lateral%20approximant.ogg)}} |  |
> | {{[[ɥ](voiced%20labial–palatal%20approximant.md)]}} | {{![voiced labial–palatal approximant](../../archives/Wikimedia%20Commons/LL-Q150%20(fra)-WikiLucas00-IPA%20%C9%A5.wav)}} |  |
> | {{[[z](voiced%20alveolar%20fricative.md)]}} | {{![voiced alveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20sibilant.ogg)}} |  |
> | {{[[ʒ](voiced%20postalveolar%20fricative.md)]}} | {{![voiced postalveolar fricative](../../archives/Wikimedia%20Commons/Voiced%20palato-alveolar%20sibilant.ogg)}} |  |
> | {{[[ʑ](voiced%20alveolo-palatal%20fricative.md)]}} | {{![voiced alveolo-palatal fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolo-palatal%20sibilant.ogg)}} |  |
> | {{[[ʐ](voiced%20retroflex%20fricative.md)]}} | {{![voiced retroflex fricative](../../archives/Wikimedia%20Commons/Voiced%20retroflex%20sibilant.ogg)}} |  |
> | {{[[ɮ](voiced%20alveolar%20lateral%20fricative.md)]}} | {{![voiced alveolar lateral fricative](../../archives/Wikimedia%20Commons/Voiced%20alveolar%20lateral%20fricative.ogg)}} |  |
> | {{[[θ](voiceless%20dental%20fricative.md)]}} | {{![voiceless dental fricative](../../archives/Wikimedia%20Commons/Voiceless%20dental%20fricative.ogg)}} |  |
> | {{[[ɸ](voiceless%20bilabial%20fricative.md)]}} | {{![voiceless bilabial fricative](../../archives/Wikimedia%20Commons/Voiceless%20bilabial%20fricative.ogg)}} |  |
> | {{[[ʔ](glottal%20stop.md)]}} | {{![glottal stop](../../archives/Wikimedia%20Commons/Glottal%20stop.ogg)}} |  |
> | {{[[ʕ](voiced%20pharyngeal%20fricative.md)]}} | {{![voiced pharyngeal fricative](../../archives/Wikimedia%20Commons/Voiced%20pharyngeal%20fricative.ogg)}} |  |
> | {{[[ǀ](tenuis%20dental%20click.md)]}} | {{![tenuis dental click](../../archives/Wikimedia%20Commons/Dental%20click.ogg)}} |  |
> | {{[[ǁ](tenuis%20alveolar%20lateral%20click.md)]}} | {{![tenuis alveolar lateral click](../../archives/Wikimedia%20Commons/Alveolar%20lateral%20click.ogg)}} |  |
> | {{[[ǃ](tenuis%20alveolar%20click.md)]}} | {{![tenuis alveolar click](../../archives/Wikimedia%20Commons/Postalveolar%20click.ogg)}} |  |
> | {{[[ʘ](tenuis%20bilabial%20click.md)]}} | {{![tenuis bilabial click](../../archives/Wikimedia%20Commons/Clic%20bilabial%20sourd.ogg)}} |  |
> | {{[[ǂ](tenuis%20palatal%20click.md)]}} | {{![tenuis palatal click](../../archives/Wikimedia%20Commons/Palatoalveolar%20click.ogg)}} |  |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### diacritics

Here is a list of common IPA diacritics and their descriptions:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485d"--><!-- The following content is generated at 2023-06-15T13:39:40.690037+08:00. Any edits will be overridden! -->

> | symbol | description |
> |-|-|
> | {{[\[◌̃\]](nasal%20vowel.md) (e.g. [ã])}} |  |
> | {{[\[◌̈\]](central%20vowel.md) (e.g. [ä])}} |  |
> | {{[\[◌̆\]](extra-shortness.md) (e.g. [ă])}} |  |
> | {{[\[◌̯\]](diphthong.md) (e.g. [a̯])}} |  |
> | {{[\[◌̥\]](voicelessness.md) (e.g. [n̥])}} |  |
> | {{[\[◌̩\], \[◌̍\]](syllabic%20consonant.md) (e.g. [n̩], [ŋ̍])}} |  |
> | {{[\[◌̪\]](dental%20consonant.md) (e.g. [d̪])}} |  |
> | {{[\[◌ʰ\]](aspirated%20consonant.md) (e.g. [kʰ])}} |  |
> | {{[\[◌’\]](ejective%20consonant.md) (e.g. [k’])}} |  |
> | {{[\[◌ː\]](longness%20(phonetics).md) (e.g. [aː])}} |  |
> | {{[\[◌ˑ\]](half-longness%20(phonetics).md) (e.g. [aˑ])}} |  |
> | {{[\[ˈ◌\]](stress%20(lingustics).md) (e.g. [ˈa])}} |  |
> | {{[\[ˌ◌\]](secondary%20stress.md) (e.g. [ˌa])}} |  |
> | {{[\[.\]](syllable.md)}} |  |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
