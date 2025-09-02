---
aliases:
  - baseband
  - baseband signal
  - baseband signals
  - basebands
tags:
  - flashcard/active/general/eng/baseband
  - language/in/English
---

# baseband

> {@{![Spectrum of a __baseband signal__, energy _E_ per unit frequency as a function of frequency _f_.](../../archives/Wikimedia%20Commons/Bandlimited2.svg)}@}
>
> {@{Spectrum of a __baseband signal__}@}, {@{energy _E_ per unit frequency}@} as {@{a function of frequency _f_}@}. {@{The total energy}@} is {@{the area under the curve}@}. <!--SR:!2025-09-24,14,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290-->

In {@{[telecommunications](telecommunications.md) and [signal processing](signal%20processing.md)}@}, {@{__baseband__}@} is {@{the range of frequencies occupied by a [signal](signal.md)}@} that has {@{not been [modulated](modulation.md) to higher frequencies}@}.<sup>[\[1\]](#^ref-1)</sup> Baseband signals typically {@{originate from [transducers](transducer.md)}@}, converting {@{some other variable into an electrical signal}@}. For example, {@{the electronic output of a microphone}@} is a baseband signal that is {@{analogous to the applied voice audio}@}. In {@{conventional [analog](analog%20signal.md) [radio broadcasting](radio%20broadcasting.md)}@}, {@{the baseband [audio signal](audio%20signal.md)}@} is used to [modulate](modulation.md) {@{an [RF carrier signal](radio%20frequency.md) of a much higher frequency}@}. <!--SR:!2025-09-24,14,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-24,14,290-->

A baseband signal may have {@{frequency components}@} going {@{all the way down to the [DC bias](DC%20bias.md)}@}, or at least it will have {@{a high [ratio bandwidth](ratio%20bandwidth.md#ratio%20bandwidth)}@}. {@{A modulated baseband signal}@} is called {@{a [passband signal](passband%20signal.md)}@}. This occupies {@{a higher range of frequencies}@} and has {@{a lower ratio and [fractional bandwidth](fractional%20bandwidth.md#fractional%20bandwidth)}@}. <!--SR:!2025-09-25,15,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-25,15,290!2025-09-24,14,290-->

## various uses

### baseband signal

{@{A _baseband signal_ or _lowpass signal_}@} is a signal that {@{can include frequencies that are very near zero}@}, by {@{comparison with its highest frequency}@} \(for example, {@{a sound waveform}@} can be considered as {@{a baseband signal}@}, whereas {@{a radio signal or any other modulated signal is not}@}\).<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-09-25,15,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-24,14,290-->

{@{A _baseband [bandwidth](bandwidth%20(signal%20processing).md)_}@} is equal to {@{the highest frequency of a signal or system, or an upper bound on such frequencies}@},<sup>[\[3\]](#^ref-3)</sup> for example {@{the upper [cut-off frequency](cut-off%20frequency.md) of a [low-pass filter](low-pass%20filter.md)}@}. By contrast, {@{[passband](passband.md) bandwidth}@} is {@{the difference between a highest frequency and a nonzero lowest frequency}@}. <!--SR:!2025-09-25,15,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-25,15,290-->

### baseband channel

{@{A _baseband channel_ or _lowpass channel_ \(or _system_, or _network_\)}@} is {@{a [communication channel](communication%20channel.md) that can transfer frequencies that are very near zero}@}.<sup>[\[4\]](#^ref-4)</sup> Examples are {@{serial cables and [local area networks](local%20area%20network.md) \(LANs\)}@}, as opposed to {@{[passband](passband.md) channels}@} such as {@{radio frequency channels and passband filtered wires of the analog telephone network}@}. {@{[Frequency division multiplexing](frequency%20division%20multiplexing.md) \(FDM\)}@} allows {@{an analog telephone wire}@} to {@{carry a baseband telephone}@} call, concurrently as {@{one or several carrier-modulated telephone calls}@}. <!--SR:!2025-09-26,16,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-24,14,290-->

### digital baseband transmission

- Main article: ::@:: [Line code](line%20code.md) <!--SR:!2025-09-25,15,290!2025-09-25,15,290-->

{@{Digital baseband transmission, also known as [line coding](line%20coding.md)}@},<sup>[\[5\]](#^ref-5)</sup> aims at {@{transferring a digital bit stream over baseband channel}@}, typically {@{an unfiltered wire}@}, contrary to {@{[passband](passband.md) transmission, also known as _carrier-modulated_ transmission}@}.<sup>[\[6\]](#^ref-6)</sup> {@{Passband transmission}@} makes communication {@{possible over a bandpass filtered channel}@}, such as {@{the telephone network local-loop or a band-limited wireless channel}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-09-25,15,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-24,14,290-->

#### baseband transmission in Ethernet

{@{The word "BASE" in [Ethernet physical layer](ethernet%20physical%20layer.md) standards}@}, for example {@{[10BASE5](10BASE5.md), [100BASE-TX](100BASE-TX.md#100BASE-TX) and [1000BASE-SX](1000BASE-SX.md#1000BASE-SX)}@}, implies {@{baseband digital transmission}@} \(i.e. that {@{a [line code](line%20code.md) and an unfiltered wire}@} are used\).<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> <!--SR:!2025-09-24,14,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-24,14,290-->

### baseband processor

{@{A [baseband processor](baseband%20processor.md) also known as BP or BBP}@} is used to process {@{the down-converted digital signal}@} to retrieve {@{essential data for a wireless digital system}@}. {@{The baseband processing block}@} in {@{[GNSS](satellite%20navigation.md) receivers}@} is responsible for providing {@{observable data}@}: that is, {@{code pseudo-ranges and carrier phase measurements, as well as navigation data}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-09-26,16,290!2025-09-25,15,290!2025-09-25,15,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-26,16,290-->

### equivalent baseband signal

> {@{![In-phase \(I\) and quadrature \(Q\) modulation and demodulation block diagram. IF stands for Intermediate frequency.](../../archives/Wikimedia%20Commons/IQ%20Mod%20Demod%20block%20diagram.svg)}@}
>
> On {@{the left is a part of the transmitter}@}, which will take in {@{a stream of baseband [IQ data](IQ%20data.md#I%2FQ%20data)}@}, and use this to amplitude {@{modulate a Local Oscillator's signal}@}, both {@{the standard sine wave from the LO}@}, and also {@{a version which phase shifted by 90°}@} \({@{in-phase and quadrature}@}\) - these modulated signals are {@{combined, to form the [Intermediate frequency](intermediate%20frequency.md) IF representation}@}. In {@{a typical transmitter}@}, the IF would get {@{up-converted, filtered, amplified}@}, then {@{transmitted from an antenna}@}. \(These are not shown\) <br/>
> On {@{the right we see an aspect of the receiver}@}. After {@{some low-noise amplification, filtering and down-conversion}@} \(not shown\) to an IF, the signal is {@{mixed with the in-phase sine from the LO}@}, and also {@{the quadrature version of the LO}@}, giving {@{a complex \(or 2-dimensional\) representation}@} of the signal. {@{This [IQ data](IQ%20data.md#I%2FQ%20data)}@} could then be supplied to {@{a [digital signal processor](digital%20signal%20processor.md)}@} to extract {@{symbols or data}@}. <!--SR:!2025-09-25,15,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-25,15,290-->

{@{An _equivalent baseband signal_ or _equivalent lowpass signal_}@} is {@{a complex valued representation of the modulated physical signal}@} \(the so-called {@{[passband](passband.md) signal or [RF](radio%20frequency.md) signal}@}\). It is a concept within {@{analog and digital modulation methods for \(passband\) signals}@} with {@{constant or varying [carrier frequency](carrier%20frequency.md)}@} \(for example {@{[ASK](amplitude-shift%20keying.md), [PSK](phase-shift%20keying.md) [QAM](quadrature%20amplitude%20modulation.md), and [FSK](frequency-shift%20keying.md)}@}\). {@{The equivalent baseband signal}@} is {@{$Z(t)=I(t)+jQ(t)\,$}@} where {@{$I(t)$ is the inphase signal, $Q(t)$ the quadrature phase signal, and $j$ the [imaginary unit](imaginary%20unit.md)}@}. This signal is sometimes called {@{_[IQ data](IQ%20data.md#I%2FQ%20data)_}@}. In {@{a digital modulation method}@}, {@{the $I(t)$ and $Q(t)$ signals}@} of {@{each modulation symbol}@} are evident from {@{the [constellation diagram](constellation%20diagram.md)}@}. {@{The frequency spectrum}@} of this signal includes {@{negative as well as positive frequencies}@}. {@{The physical passband signal}@} corresponds to {@{$$I(t)\cos(\omega t)-Q(t)\sin(\omega t)=\mathrm {Re} \{Z(t)e^{j\omega t}\}\,$$}@} where {@{$\omega$ is the carrier [angular frequency](angular%20frequency.md) in rad/s}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-09-24,14,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-21,11,270-->

## modulation

{@{A signal at baseband}@} is often used to {@{[modulate](modulation.md) a higher frequency [carrier signal](carrier%20signal.md)}@} in order that it {@{may be transmitted via radio}@}. {@{Modulation}@} results in shifting {@{the signal up to much higher frequencies \(radio frequencies, or RF\) than it originally spanned}@}. {@{A key consequence}@} of {@{the usual [double-sideband](double%20sideband.md) [amplitude modulation](amplitude%20modulation.md) \(AM\)}@} is that {@{the range of frequencies the signal spans \(its spectral [bandwidth](bandwidth%20(signal%20processing).md)\)}@} is {@{doubled}@}. Thus, {@{the RF bandwidth of a signal}@} \(measured from {@{the lowest frequency as opposed to 0 Hz}@}\) is {@{twice its baseband bandwidth}@}. {@{Steps may be taken}@} to reduce {@{this effect}@}, such as {@{[single-sideband modulation](single-sideband%20modulation.md)}@}. Conversely, {@{some transmission schemes such as [frequency modulation](frequency%20modulation.md)}@} use {@{even more bandwidth}@}. <!--SR:!2025-09-25,15,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-24,14,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-25,15,290!2025-09-26,16,290!2025-09-26,16,290-->

The figure below shows {@{AM modulation}@}: <!--SR:!2025-09-26,16,290-->

> {@{![Comparison of the equivalent baseband version of a signal and its AM-modulated \(double-[sideband](sideband.md)\) RF version, showing the typical doubling of the occupied bandwidth.](../../archives/Wikimedia%20Commons/Baseband%20to%20RF.svg)}@}
>
> {@{Comparison of the equivalent baseband version of a signal}@} and {@{its AM-modulated \(double-[sideband](sideband.md)\) RF version}@}, showing {@{the typical doubling of the occupied bandwidth}@}. <!--SR:!2025-09-25,15,290!2025-09-24,14,290!2025-09-26,16,290!2025-09-25,15,290-->

## see also

> ![Wiktionary logo](../../archives/Wikimedia%20Commons/Wiktionary-logo-en-v2.svg) Look up ___[baseband](https://en.wiktionary.org/wiki/Special%3ASearch/baseband)___ in Wiktionary, the free dictionary.

- [Complex envelope](complex%20envelope.md#complex%20envelope)
- [Broadband](broadband.md)
- [In-phase and quadrature components](in-phase%20and%20quadrature%20components.md)
- [Narrowband](narrowband.md)
- [Wideband](wideband.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/baseband) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Jeff Rutenbeck, _Tech Terms: What Every Telecommunications and Digital Media Professional Should Know_, [p. 24](https://books.google.com/books?id=dfFsAAAAQBAJ&pg=PA24), CRC Press, 2012 [ISBN](ISBN%20(identifier).md) [1136034501](https://en.wikipedia.org/wiki/Special:BookSources/1136034501) <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFSteven Alan Tretter1995"></a> Steven Alan Tretter \(1995\). [_Communication System Design Using Dsp Algorithms: With Laboratory Experiments for the TMS320C30_](https://books.google.com/books?id=deHQeNxHhyEC&dq=baseband-signal+lowpass-signal&pg=PA65). Springer. [ISBN](ISBN%20(identifier).md) [0-306-45032-1](https://en.wikipedia.org/wiki/Special:BookSources/0-306-45032-1). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFMischa Schwartz1970"></a> Mischa Schwartz \(1970\). [_Information, Transmission, Modulation and Noise: A Unified Approach to Communication Systems_](https://books.google.com/books?id=-gkjAAAAMAAJ&q=baseband-bandwidth). McGraw-Hill. [ISBN](ISBN%20(identifier).md) [9780070557611](https://en.wikipedia.org/wiki/Special:BookSources/9780070557611). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFChris C. Bissell and David A. Chapman1992"></a> Chris C. Bissell and David A. Chapman \(1992\). [_Digital Signal Transmission_](https://books.google.com/books?id=cj12nN2uW0AC&dq=called-baseband-channels&pg=PA149). Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-42557-3](https://en.wikipedia.org/wiki/Special:BookSources/0-521-42557-3). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFMikael Gustavsson and J. Jacob Wikner2000"></a> Mikael Gustavsson and J. Jacob Wikner \(2000\). [_CMOS Data Converters for Communications_](https://books.google.com/books?id=D_I2XvNOc4wC&dq=passband+baseband&pg=PA28). Springer. [ISBN](ISBN%20(identifier).md) [0-7923-7780-X](https://en.wikipedia.org/wiki/Special:BookSources/0-7923-7780-X). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFJan W. M. Bergmans1996"></a> Jan W. M. Bergmans \(1996\). [_Digital Baseband Transmission and Recording_](https://books.google.com/books?id=TN-sTybrCLsC&dq=baseband+carrier-modulated&pg=PR11). Springer. [ISBN](ISBN%20(identifier).md) [0-7923-9775-4](https://en.wikipedia.org/wiki/Special:BookSources/0-7923-9775-4). <a id="^ref-6"></a>^ref-6
7. ["Baseband Processing - Navipedia"](https://gssc.esa.int/navipedia/index.php/Baseband_Processing). _gssc.esa.int_. Retrieved 2022-07-04. <a id="^ref-7"></a>^ref-7
8. IEEE 802.3 _1.2.3 Physical layer and media notation_ <a id="^ref-8"></a>^ref-8
9. ["IEEE Get Program"](https://web.archive.org/web/20101125111240/http://standards.ieee.org/about/get/802/802.3.html). _[IEEE](IEEE.md)_. IEEE. Archived from [the original](http://standards.ieee.org/about/get/802/802.3.html) on November 25, 2010. Retrieved 29 March 2017. <a id="^ref-9"></a>^ref-9
10. Proakis, John G. _Digital Communications_, 4th edition. McGraw-Hill, 2001. p150 <a id="^ref-10"></a>^ref-10

|                                                                                                                                                                                                                                                                   |                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------- |
| __[Authority control databases](https://en.wikipedia.org/wiki/Help:Authority%20control): National [![Edit this at Wikidata](../../archives/Wikimedia%20Commons/OOjs%20UI%20icon%20edit-ltr-progressive.svg)](https://www.wikidata.org/wiki/Q575784#identifiers)__ | - [Germany](https://d-nb.info/gnd/4656240-0) |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Computer network technology](https://en.wikipedia.org/wiki/Category:Computer%20network%20technology)
> - [Signal processing](https://en.wikipedia.org/wiki/Category:Signal%20processing)
