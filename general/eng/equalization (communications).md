---
aliases:
  - equalization
  - equalization (communications)
  - equalizer
  - equalizers
tags:
  - flashcard/active/general/eng/equalization__communications_
  - language/in/English
---

# equalization

In {@{[telecommunication](telecommunication.md)}@}, {@{__equalization__}@} is {@{the reversal of distortion incurred by a signal transmitted through a [channel](channel%20(communications).md)}@}. {@{__Equalizers__}@} are used to {@{render the [frequency response](frequency%20response.md)—for instance of a telephone line}@}—<!-- markdown separator -->{@{_flat_ from end-to-end}@}. When {@{a [channel](communication%20channel.md) has been equalized}@} {@{the [frequency domain](frequency%20domain.md) attributes of the signal at the input}@} are {@{faithfully reproduced at the output}@}. {@{Telephones, [DSL](DSL.md) lines and television cables}@} use {@{equalizers to prepare data signals for transmission}@}. <!--SR:!2025-11-18,59,310!2025-11-20,61,310!2025-11-15,57,310!2026-07-08,237,330!2026-07-12,241,330!2025-11-27,67,310!2025-11-27,67,310!2025-11-22,63,310!2026-07-09,238,330!2025-11-15,57,310!2025-11-27,67,310-->

Equalizers are {@{critical to the successful operation of electronic systems}@} such as {@{[analog broadcast television](analog%20television.md)}@}. In this application {@{the actual [waveform](waveform.md) of the transmitted signal}@} must {@{be preserved, not just its frequency content}@}. {@{Equalizing filters}@} must {@{cancel out any [group delay and phase delay](group%20delay%20and%20phase%20delay.md) between different frequency components}@}. <!--SR:!2025-11-16,58,310!2025-11-27,67,310!2025-11-17,58,310!2025-11-16,58,310!2026-07-05,235,330!2025-11-15,57,310-->

## analog telecommunications

### audio lines

{@{Early telephone systems}@} used {@{equalization}@} to {@{correct for the reduced level of high frequencies in long cables}@}, typically using {@{[Zobel networks](Zobel%20network.md)}@}. {@{These kinds of equalizers}@} can also be used to {@{produce a circuit with a wider bandwidth}@} than {@{the standard telephone band of 300 Hz to 3.4 kHz}@}. This was {@{particularly useful for broadcasters}@} who needed {@{"music" quality, not "telephone" quality on landlines carrying program material}@}. It is necessary to {@{remove or cancel any [loading coils](loading%20coil.md) in the line}@} before {@{equalization can be successful}@}. Equalization was also applied to {@{correct the response of the transducers}@}, for example, {@{a particular [microphone](microphone.md)}@} might be {@{more sensitive to low [frequency](frequency.md) sounds than to high frequency sounds}@}, so {@{an equalizer would be used}@} to {@{increase the volume of the higher frequencies \(_boost_\)}@}, and {@{reduce the volume of the low frequency sounds \(_cut_\)}@}. <!--SR:!2025-11-14,56,310!2025-11-27,67,310!2025-11-14,56,310!2026-04-17,168,310!2025-11-27,67,310!2025-11-14,56,310!2025-11-27,67,310!2026-07-10,239,330!2025-11-14,56,310!2025-11-27,67,310!2025-11-27,67,310!2025-11-15,57,310!2025-11-27,67,310!2026-07-03,233,330!2025-11-14,56,310!2025-11-15,57,310!2025-11-22,63,310-->

### television lines

{@{A similar approach to audio}@} was taken with {@{television landlines with two important additional complications}@}. {@{The first of these}@} is that {@{the television signal}@} is {@{a wide bandwidth covering many more octaves than an audio signal}@}. {@{A television equalizer}@} consequently {@{typically requires more filter sections than an audio equalizer}@}. To {@{keep this manageable}@}, {@{television equalizer sections}@} were often {@{combined into a single network using [ladder topology](ladder%20topology.md#ladder%20topologies)}@} to form {@{a [Cauer equalizer](Cauer%20equaliser.md#Cauer%20equaliser)}@}. <!--SR:!2026-07-08,237,330!2025-11-27,67,310!2025-11-16,58,310!2026-07-06,236,330!2025-11-14,56,310!2026-07-09,238,330!2025-11-20,61,310!2025-11-16,58,310!2025-11-21,62,310!2025-11-27,67,310!2025-11-21,62,310-->

{@{The second issue}@} is that {@{phase equalization is essential}@} for {@{an analog television signal}@}. {@{Without it [dispersion](material%20dispersion.md)}@} causes {@{the loss of integrity of the original wave-shape}@} and is seen as {@{smearing of what were originally sharp edges in the picture}@}. <!--SR:!2025-11-22,63,310!2025-11-16,58,310!2025-11-27,67,310!2026-07-05,235,330!2025-11-27,67,310!2026-03-21,150,310-->

### analog equalizer types

- [Zobel network](Zobel%20network.md)
- [Lattice phase equalizer](lattice%20phase%20equalizer.md)
- [Bridged T delay equalizer](bridged%20T%20delay%20equalizer.md)

## digital telecommunications

{@{Modern digital telephone systems}@} have {@{less trouble in the voice frequency range}@} as {@{only the local line to the subscriber}@} now {@{remains in analog format}@}, but {@{[DSL](digital%20subscriber%20line.md) circuits}@} operating {@{in the [MHz](megahertz.md) range on those same wires}@} may suffer {@{severe [attenuation distortion](attenuation%20distortion.md)}@}, which is dealt with by {@{automatic equalization or by abandoning the worst frequencies}@}. {@{[Picturephone](videophone.md) circuits}@} also {@{had equalizers}@}. <!--SR:!2026-07-02,232,330!2025-11-21,62,310!2025-11-16,58,310!2025-11-27,67,310!2025-11-16,58,310!2026-07-06,236,330!2025-11-22,63,310!2025-11-19,60,310!2025-11-27,67,310!2025-11-27,67,310-->

In {@{[digital communications](digital%20communications.md)}@}, {@{the equalizer's purpose}@} is to {@{reduce [intersymbol interference](intersymbol%20interference.md)}@} to allow {@{recovery of the transmit symbols}@}. It may be {@{a simple [linear filter](linear%20filter.md) or a complex algorithm}@}. <!--SR:!2025-11-27,67,310!2025-11-27,67,310!2025-11-27,67,310!2025-11-20,61,310!2025-11-21,62,310-->

### digital equalizer types

- {@{Linear equalizer}@}: {@{processes the incoming signal}@} with {@{a linear filter}@}
  - {@{[MMSE](minimum%20mean%20square%20error.md) equalizer}@}: designs the filter to {@{minimize E\[\|e\|<sup>2</sup>\]}@}, where e is {@{the error signal, which is the filter output minus the transmitted signal}@}.<sup>[\[1\]](#^ref-1)</sup>
  - {@{[Zero-forcing equalizer](zero-forcing%20equalizer.md)}@}: {@{approximates the inverse of the channel}@} with {@{a linear filter}@}. <!--SR:!2025-11-22,63,310!2025-11-27,67,310!2025-11-20,61,310!2025-11-27,67,310!2026-07-07,237,330!2025-11-22,63,310!2025-11-15,57,310!2025-11-14,56,310!2025-11-27,67,310-->

- {@{[Decision feedback equalizer](decision%20feedback%20equalizer.md)}@}: {@{augments a linear equalizer}@} by adding {@{a filtered version of previous symbol estimates}@} to {@{the original filter output}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-11-27,67,310!2025-11-15,57,310!2025-11-15,57,310!2025-11-27,67,310-->

- {@{[Blind equalizer](blind%20equalization.md)}@}: {@{estimates the transmitted signal}@} {@{without knowledge of the channel statistics}@}, using {@{only knowledge of the transmitted signal's statistics}@}. <!--SR:!2026-07-04,234,330!2025-11-14,56,310!2025-11-27,67,310!2025-11-20,61,310-->

- {@{[Adaptive equalizer](adaptive%20equalizer.md)}@}: is typically {@{a linear equalizer or a DFE}@}. It {@{updates the equalizer parameters \(such as the filter coefficients\)}@} as {@{it processes the data}@}. Typically, it uses {@{the MSE cost function}@}; it assumes that it {@{makes the correct symbol decisions}@}, and uses {@{its estimate of the symbols to compute e}@}, which is defined above. <!--SR:!2025-11-16,58,310!2025-11-19,60,310!2025-11-21,62,310!2025-11-22,63,310!2025-11-22,63,310!2025-11-27,67,310!2025-11-22,63,310-->

- {@{[Viterbi equalizer](Viterbi%20algorithm.md)}@}: {@{Finds the [maximum likelihood](maximum%20likelihood.md) \(ML\) optimal solution}@} to {@{the equalization problem}@}. Its goal is to {@{minimize the probability of making an error over the entire sequence}@}. <!--SR:!2026-07-12,241,330!2025-11-27,67,310!2026-07-11,240,330!2025-11-20,61,310-->

- {@{[BCJR equalizer](BCJR.md)}@}: {@{uses the BCJR algorithm \(also called the [Forward-backward algorithm](forward-backward%20algorithm.md)\)}@} to {@{find the [maximum _a posteriori_](maximum%20a%20posteriori.md) \(MAP\) solution}@}. Its goal is to {@{minimize the probability that a given bit was incorrectly estimated}@}. <!--SR:!2025-11-20,61,310!2025-11-21,62,310!2025-11-21,62,310!2025-11-20,61,310-->

- {@{[Turbo equalizer](turbo%20equalizer.md)}@}: {@{applies turbo decoding}@} while {@{treating the channel as a convolutional code}@}. <!--SR:!2025-11-20,61,310!2025-11-14,56,310!2025-11-21,62,310-->

## see also

- [Electronic filter](electronic%20filter.md)
- [Weighting filter](weighting%20filter.md)
- [RIAA equalization](RIAA%20equalization.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/equalization_(communications)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFCenk Toker"></a> Cenk Toker. ["Class handout on MMSE equalizers"](https://web.archive.org/web/20181222165508/http://ee.hacettepe.edu.tr/~toker/equalizers.pdf) \(PDF\). _hacettepe.edu.tr_. Archived from [the original](http://ee.hacettepe.edu.tr/~toker/equalizers.pdf) \(PDF\) on 2018-12-22. <a id="^ref-1"></a>^ref-1
2. ["A tutorial on DFEs"](https://web.archive.org/web/20110725183902/http://cnx.org/content/m15524/latest/). _cnx.org_. Archived from [the original](http://cnx.org/content/m15524/latest/) on 2011-07-25. <a id="^ref-2"></a>^ref-2

## external links

- [Interactive demonstration of various linear and non-linear equalizers](http://webdemo.inue.uni-stuttgart.de/webdemos/02_lectures/communication_3/equalization/)
- [Interactive demonstration of a Viterbi equalizer](http://webdemo.inue.uni-stuttgart.de/webdemos/02_lectures/communication_3/mlse_viterbi/)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Signal processing](https://en.wikipedia.org/wiki/Category:Signal%20processing)
