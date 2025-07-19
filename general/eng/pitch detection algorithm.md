---
aliases:
  - pitch detection
  - pitch detection algorithm
  - pitch detection algorithms
  - pitch track
  - pitch tracking
tags:
  - flashcard/active/general/eng/pitch_detection_algorithm
  - language/in/English
---

# pitch detection algorithm

- {@{"Pitch tracking"}@} redirects here. For {@{the baseball term}@}, see {@{[Glossary of baseball \(P\) § pitch tracking](glossary%20of%20baseball%20(P).md#pitch%20tracking)}@}. <!--SR:!2025-09-21,66,310!2025-09-08,54,310!2025-09-16,61,310-->

{@{A __pitch detection algorithm__ \(__PDA__\)}@} is {@{an [algorithm](algorithm.md) designed to estimate the [pitch](pitch%20(music).md) or [fundamental frequency](fundamental%20frequency.md) of a [quasiperiodic](quasiperiodic.md) or [oscillating](oscillation.md) signal}@}, usually {@{a [digital recording](digital%20recording.md) of [speech](speech%20processing.md) or a musical note or tone}@}. This can be done in {@{the [time domain](time%20domain.md), the [frequency domain](frequency%20domain.md), or both}@}. <!--SR:!2025-09-17,63,310!2025-09-17,62,310!2025-09-15,61,310!2025-09-21,66,310-->

PDAs are used in {@{various contexts}@} \(e.g. {@{[phonetics](phonetics.md), [music information retrieval](music%20information%20retrieval.md), [speech coding](speech%20coding.md), [musical performance systems](musical%20performance%20system.md)}@}\) and so there may be {@{different demands placed upon the algorithm}@}. There is as yet<sup>\[_[when?](https://en.wikipedia.org/wiki/Wikipedia:Manual%20of%20Style/Dates%20and%20numbers#Chronological%20items)_\]</sup> {@{no single ideal PDA}@}, so {@{a variety of algorithms exist}@}, most {@{falling broadly into the classes given below}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-09-09,55,310!2025-09-19,64,310!2025-09-22,67,310!2025-09-15,61,310!2025-09-10,56,310!2025-09-16,62,310-->

A PDA typically estimates {@{the period of a quasiperiodic signal}@}, then {@{inverts that value to give the frequency}@}. <!--SR:!2025-09-08,54,310!2025-09-17,63,310-->

## general approaches

One simple approach would be to {@{measure the distance between [zero crossing](zero%20crossing.md) points of the signal}@} \(i.e. {@{the [zero-crossing rate](zero-crossing%20rate.md)}@}\). However, this {@{does not work well with complicated [waveforms](waveform.md)}@} which are composed of {@{multiple sine waves with differing periods or noisy data}@}. Nevertheless, there are cases in which {@{zero-crossing can be a useful measure}@}, e.g. in {@{some speech applications where a single source is assumed}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> {@{The algorithm's simplicity}@} makes it {@{"cheap" to implement}@}. <!--SR:!2025-09-16,62,310!2025-09-10,56,310!2025-09-18,63,310!2025-09-17,63,310!2025-09-10,56,310!2025-09-15,61,310!2025-09-10,56,310!2025-09-11,57,310-->

{@{More sophisticated approaches}@} compare {@{segments of the signal with other segments offset by a trial period to find a match}@}. {@{AMDF \([average magnitude difference function](average%20magnitude%20difference%20function.md)\), ASMDF \(Average Squared Mean Difference Function\), and other similar [autocorrelation](autocorrelation.md) algorithms}@} {@{work this way}@}. These algorithms can give {@{quite accurate results for highly periodic signals}@}. However, they have {@{false detection problems}@} \(often {@{"_octave errors_"}@}\), can sometimes {@{cope badly with noisy signals \(depending on the implementation\)}@}, and - in their basic implementations - do not deal well with {@{[polyphonic](polyphony.md) sounds \(which involve multiple musical notes of different pitches\)}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> <!--SR:!2025-09-14,60,310!2025-09-10,56,310!2025-08-18,38,290!2025-09-14,60,310!2025-09-20,65,310!2025-09-20,65,310!2025-09-11,57,310!2025-09-14,60,310!2025-09-21,66,310-->

Current<sup>\[_[when?](https://en.wikipedia.org/wiki/Wikipedia:Manual%20of%20Style/Dates%20and%20numbers#Chronological%20items)_\]</sup> time-domain pitch detector algorithms tend to {@{build upon the basic methods mentioned above}@}, with {@{additional refinements to bring the performance more in line with a human assessment of pitch}@}. For example, {@{the YIN algorithm<sup>[\[2\]](#^ref-2)</sup> and the MPM algorithm}@}<sup>[\[3\]](#^ref-3)</sup> are both {@{based upon [autocorrelation](autocorrelation.md)}@}. <!--SR:!2025-09-12,58,310!2025-09-19,64,310!2025-09-11,57,310!2025-09-17,63,310-->

## frequency-domain approaches

In the frequency domain, {@{polyphonic detection}@} is possible, usually utilizing {@{the [periodogram](periodogram.md)}@} to {@{convert the signal to an estimate of the [frequency spectrum](frequency%20spectrum.md#explanation)}@}.<sup>[\[4\]](#^ref-4)</sup> This requires {@{more processing power as the desired accuracy increases}@}, although {@{the well-known efficiency of the [FFT](fast%20Fourier%20transform.md)}@}, a key part of the periodogram algorithm, makes it {@{suitably efficient for many purposes}@}. <!--SR:!2025-09-12,58,310!2025-09-14,60,310!2025-09-19,64,310!2025-09-16,62,310!2025-09-18,63,310!2025-09-08,54,310-->

{@{Popular frequency domain algorithms}@} include: {@{the [harmonic product spectrum](harmonic%20product%20spectrum.md);<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> [cepstral](cepstrum.md) analysis<sup>[\[7\]](#^ref-7)</sup> and [maximum likelihood](maximum%20likelihood.md)}@} which attempts to {@{match the frequency domain characteristics to pre-defined frequency maps}@} \(useful for {@{detecting pitch of fixed tuning instruments}@}\); and the detection of {@{peaks due to harmonic series}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2025-09-17,63,310!2025-09-22,67,310!2025-09-18,63,310!2025-09-16,61,310!2025-09-17,62,310-->

To improve on {@{the pitch estimate derived from the discrete Fourier spectrum}@}, techniques such as {@{[spectral reassignment](reassignment%20method.md) \(phase based\) or [Grandke interpolation](Grandke%20interpolation.md) \(magnitude based\)}@} can be used to {@{go beyond the precision provided by the FFT bins}@}. Another {@{phase-based approach}@} is offered by Brown and Puckette <sup>[\[9\]](#^ref-9)</sup> <!--SR:!2025-09-20,65,310!2025-09-11,57,310!2025-09-16,62,310!2025-09-12,58,310-->

## spectral/temporal approaches

{@{Spectral/temporal pitch detection algorithms}@}, e.g. {@{the [YAAPT pitch tracking algorithm](YAAPT%20pitch%20tracking%20algorithm.md)}@},<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> are based upon {@{a combination of time domain processing using an [autocorrelation](autocorrelation.md) function such as normalized cross correlation}@}, and {@{frequency domain processing utilizing spectral information to identify the pitch}@}. Then, among {@{the candidates estimated from the two domains}@}, {@{a final pitch track}@} can be computed using {@{[dynamic programming](dynamic%20programming.md)}@}. {@{The advantage of these approaches}@} is that {@{the tracking error in one domain can be reduced by the process in the other domain}@}. <!--SR:!2025-09-17,63,310!2025-09-17,62,310!2025-09-21,66,310!2025-09-12,58,310!2025-09-09,55,310!2025-09-22,67,310!2025-09-17,62,310!2025-09-09,55,310!2025-09-09,55,310-->

## speech pitch detection

{@{The fundamental frequency of [speech](speech.md)}@} can vary from {@{40 Hz for low-pitched voices to 600 Hz for high-pitched voices}@}.<sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-09-16,61,310!2025-09-09,55,310-->

{@{Autocorrelation methods}@} need {@{at least two pitch periods to detect pitch}@}. This means that in order to {@{detect a fundamental frequency of 40 Hz}@}, at least {@{50 milliseconds \(ms\) of the speech signal must be analyzed}@}. However, during 50 ms, {@{speech with higher fundamental frequencies}@} may not necessarily have {@{the same fundamental frequency throughout the window}@}.<sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-09-08,54,310!2025-09-15,61,310!2025-09-15,61,310!2025-09-16,62,310!2025-09-14,60,310!2025-09-15,61,310-->

## see also

- [Auto-Tune](Auto-Tune.md)
- [Beat detection](beat%20detection.md)
- [Frequency estimation](frequency%20estimation.md)
- [Linear predictive coding](linear%20predictive%20coding.md)
- [MUSIC \(algorithm\)](MUSIC%20(algorithm).md)
- [Sinusoidal model](sinusoidal%20model.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/pitch_detection_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. D. Gerhard. [Pitch Extraction and Fundamental Frequency: History and Current Techniques](https://www2.cs.uregina.ca/~gerhard/publications/TRdbg-Pitch.pdf), technical report, Dept. of Computer Science, University of Regina, 2003. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFde CheveignéKawahara2002"></a> de Cheveigné, Alain; Kawahara, Hideki \(2002\). ["YIN, a fundamental frequency estimator for speech and music"](http://audition.ens.fr/adc/pdf/2002_JASA_YIN.pdf) \(PDF\). _The Journal of the Acoustical Society of America_. __111__ \(4\). Acoustical Society of America \(ASA\): 1917–1930. [Bibcode](bibcode%20(identifier).md):[2002ASAJ..111.1917D](https://ui.adsabs.harvard.edu/abs/2002ASAJ..111.1917D). [doi](doi%20(identifier).md):[10.1121/1.1458024](https://doi.org/10.1121%2F1.1458024). [ISSN](ISSN%20(identifier).md) [0001-4966](https://search.worldcat.org/issn/0001-4966). [PMID](PMID%20(identifier).md#PubMed%20identifier) [12002874](https://pubmed.ncbi.nlm.nih.gov/12002874). [S2CID](S2CID%20(identifier).md#S2CID) [1607434](https://api.semanticscholar.org/CorpusID:1607434). <a id="^ref-2"></a>^ref-2
3. P. McLeod and G. Wyvill. [A smarter way to find pitch.](http://www.cs.otago.ac.nz/tartini/papers/A_Smarter_Way_to_Find_Pitch.pdf) In Proceedings of the International Computer Music Conference \(ICMC’05\), 2005. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFHayes1996"></a> Hayes, Monson \(1996\). _Statistical Digital Signal Processing and Modeling_. John Wiley & Sons, Inc. p. 393. [ISBN](ISBN%20(identifier).md) [0-471-59431-8](https://en.wikipedia.org/wiki/Special:BookSources/0-471-59431-8). <a id="^ref-4"></a>^ref-4
5. [Pitch Detection Algorithms](http://cnx.org/content/m11714/latest/), online resource from [Connexions](OpenStax%20CNX.md) <a id="^ref-5"></a>^ref-5
6. A. Michael Noll, “Pitch Determination of Human Speech by the Harmonic Product Spectrum, the Harmonic Sum Spectrum and a Maximum Likelihood Estimate,” Proceedings of the Symposium on Computer Processing in Communications, Vol. XIX, Polytechnic Press: Brooklyn, New York, \(1970\), pp. 779–797. <a id="^ref-6"></a>^ref-6
7. A. Michael Noll, “[Cepstrum Pitch Determination](https://asa.scitation.org/doi/abs/10.1121/1.1910339),” Journal of the Acoustical Society of America, Vol. 41, No. 2, \(February 1967\), pp. 293–309. <a id="^ref-7"></a>^ref-7
8. Mitre, Adriano; Queiroz, Marcelo; Faria, Régis. [Accurate and Efficient Fundamental Frequency Determination from Precise Partial Estimates.](http://www.ime.usp.br/~mqz/Mitre_AESBR2006.pdf) Proceedings of the 4th AES Brazil Conference. 113-118, 2006. <a id="^ref-8"></a>^ref-8
9. Brown JC and Puckette MS \(1993\). A high resolution fundamental frequency determination based on phase changes of the Fourier transform. J. Acoust. Soc. Am. Volume 94, Issue 2, pp. 662–667 [\[1\]](https://archive.today/20130414073448/http://asadl.org/jasa/resource/1/jasman/v94/i2/p662_s1?isAuthorized=no) <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFZahorianHu2008"></a> Zahorian, Stephen A.; Hu, Hongbing \(2008\). ["A spectral/temporal method for robust fundamental frequency tracking"](http://bingweb.binghamton.edu/~hhu1/paper/Zahorian2008spectral.pdf) \(PDF\). _The Journal of the Acoustical Society of America_. __123__ \(6\). Acoustical Society of America \(ASA\): 4559–4571. [Bibcode](bibcode%20(identifier).md):[2008ASAJ..123.4559Z](https://ui.adsabs.harvard.edu/abs/2008ASAJ..123.4559Z). [doi](doi%20(identifier).md):[10.1121/1.2916590](https://doi.org/10.1121%2F1.2916590). [ISSN](ISSN%20(identifier).md) [0001-4966](https://search.worldcat.org/issn/0001-4966). [PMID](PMID%20(identifier).md#PubMed%20identifier) [18537404](https://pubmed.ncbi.nlm.nih.gov/18537404). <a id="^ref-10"></a>^ref-10
11. Stephen A. Zahorian and Hongbing Hu. [YAAPT Pitch Tracking MATLAB Function](http://ws2.binghamton.edu/zahorian/yaapt.htm) <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFHuangAlex AceroHsiao-Wuen Hon2001"></a> Huang, Xuedong; Alex Acero; Hsiao-Wuen Hon \(2001\). _Spoken Language Processing_. Prentice Hall PTR. p. 325. [ISBN](ISBN%20(identifier).md) [0-13-022616-5](https://en.wikipedia.org/wiki/Special:BookSources/0-13-022616-5). <a id="^ref-12"></a>^ref-12

## external links

- [Alain de Cheveigne and Hideki Kawahara: YIN, a fundamental frequency estimator for speech and music](http://audition.ens.fr/adc/pdf/2002_JASA_YIN.pdf)
- [AudioContentAnalysis.org: Matlab code for various pitch detection algorithms](http://www.audiocontentanalysis.org/code/pitch-tracking/compute-pitch/)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Audio engineering](https://en.wikipedia.org/wiki/Category:Audio%20engineering)
> - [Digital signal processing](https://en.wikipedia.org/wiki/Category:Digital%20signal%20processing)
