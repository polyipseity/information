---
aliases:
  - ELEC 4110 OFDM
  - ELEC 4110 orthogonal frequency division multiplexing
  - ELEC 4110 orthogonal frequency-division multiplexing
  - ELEC4110 OFDM
  - ELEC4110 orthogonal frequency division multiplexing
  - ELEC4110 orthogonal frequency-division multiplexing
  - OFDM
  - orthogonal frequency division multiplexing
  - orthogonal frequency-division multiplexing
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/OFDM
  - language/in/English
---

# orthogonal frequency-division multiplexing

- see: [general/orthogonal frequency-division multiplexing](../../../../general/orthogonal%20frequency-division%20multiplexing.md)

{@{__Orthogonal frequency-division multiplexing__ (__OFDM__)}@} converts a {@{frequency‑selective fading channel into many narrowband flat sub‑channels}@} that can be {@{modulated in parallel}@}. The {@{key idea}@} is to use the {@{discrete Fourier transform (DFT) as an orthogonal basis}@} (the basis is {@{$\set{e^{j 2\pi nt/T} }$}@}, where {@{$n \in \set{0, \ldots, N - 1}$}@} is the {@{subcarrier index}@} and {@{$T$}@} is the {@{OFDM symbol time}@}) so that each {@{sub‑carrier}@} experiences {@{no inter‑symbol interference (ISI) or inter‑carrier interference (ICI)}@} at {@{ideal sampling points}@}. <!--SR:!2026-01-28,16,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-28,16,290-->

## motivation

{@{OFDM}@} addresses the challenge of {@{transmitting data over a frequency‑selective fading channel}@} by {@{decomposing it into a large number of narrowband flat sub‑channels}@}, e.g. on the order of {@{$N=1024$}@}. By {@{sending independent data streams simultaneously across these sub‑channels}@}, an {@{OFDM system}@} transforms a {@{serial modulation scheme into a parallel one}@}, allowing {@{each sub‑carrier to experience only flat fading}@}. <!--SR:!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-28,16,290-->

Naively, {@{implementing such a large set of sub‑carriers}@} would require a {@{separate transmitter front end (modulator, mixer, etc.) for each tone}@} and the {@{insertion of guard bands between adjacent carriers}@} to {@{prevent overlap}@}. {@{These requirements}@} are {@{costly and waste spectral efficiency}@}. <!--SR:!2026-01-27,15,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290-->

{@{OFDM}@} performs {@{all processing in the digital domain}@} using a {@{wide baseband signal}@}. {@{A discrete Fourier transform (DFT) basis}@} generates the {@{baseband equivalent of every transmit tone}@}, after which a {@{single RF front end}@} {@{up‑converts the composite waveform to its center frequency}@}. Because the {@{DFT (IDFT) provides orthogonal sub‑carriers}@}, no {@{guard band}@} is necessary, thereby {@{preserving bandwidth and simplifying hardware implementation}@}. <!--SR:!2026-01-27,15,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-26,14,290-->

## operation

{@{Each subcarrier}@} carries a {@{data stream}@}. A {@{2-dimensional modulation scheme}@}, e.g. {@{QAM, PSK (but not M-FSK)}@}, is used to {@{modulate the data stream}@}. {@{Different schemes}@} may be used for {@{different subcarriers}@}. <!--SR:!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-28,16,290-->

The {@{2D modulation scheme}@} converts each {@{group of bits to a symbol}@}, which can be {@{plotted on a 2D constellation map}@} or {@{represented as a complex number $X_k$}@}. Normally, this complex number is {@{quadrature-mixed to passband in the standard way}@}. In {@{OFDM}@}, instead of performing {@{quadrature-mixing for every subcarrier}@}, the subcarriers are {@{multiplied by the DFT basis and then added together}@}: {@{$$\nu(t) = \sum_{k = 0}^{N - 1} X_k e^{j 2\pi k t/T} \qquad 0 \le t < T \,,$$}@} where {@{$N$}@} is the {@{number of subcarriers}@} and {@{$T$}@} is the {@{OFDM symbol time}@}. The above is equivalent to {@{the inverse DFT plus a digital-to-analog converter (DAC)}@}. Only afterwards, {@{quadrature-mixing is performed on the output of the IDFT-plus-DAC}@} and then {@{transmitted}@}. <!--SR:!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290-->

To {@{decode the OFDM symbol}@}, {@{quadrature-mix down to baseband}@}, then digitalize {@{the data with an analog-to-digital converter (ADC)}@}, then perform {@{DFT to get a complex number for each subcarrier}@}. Then apply {@{the respective 2D demodulation schemes for each subcarrier}@} to get the {@{original data stream}@}. <!--SR:!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-28,16,290-->

## principles

Conceptually, {@{OFDM}@} is a {@{specialized frequency-division multiplexing (FDM) method}@}, with {@{the additional constraint}@} that {@{all subcarrier signals within a communication channel are orthogonal to one another}@}. <!--SR:!2026-01-27,15,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-27,15,290-->

In {@{OFDM}@}, {@{the subcarrier frequencies are chosen}@} so that {@{the subcarriers are orthogonal to each other}@}, meaning that {@{crosstalk between the sub-channels is eliminated}@} and {@{inter-carrier guard bands}@} are not required. This greatly {@{simplifies the design of both the transmitter and the receiver}@}; unlike {@{conventional FDM}@}, {@{a separate filter for each sub-channel}@} is not required. <!--SR:!2026-01-27,15,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-28,16,290-->

{@{The orthogonality}@} requires that {@{the subcarrier spacing is $\Delta f\,=\,{\frac {k}{T_{U} } }$ Hertz}@}, where {@{_T<sub>U</sub>_ seconds}@} is the {@{useful symbol duration (the receiver-side window size)}@}, and {@{_k_}@} is {@{a positive integer, typically equal to 1}@}. This stipulates that {@{each carrier frequency}@} undergoes {@{_k_ more complete cycles per symbol period than the previous carrier}@}. Therefore, with {@{_N_ subcarriers}@}, the {@{total passband bandwidth}@} will be {@{_B_&nbsp;≈&nbsp;_N_·Δ<!-- markdown separator -->_f_&nbsp;(Hz)}@}. <!--SR:!2026-01-28,16,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-28,16,290!2026-01-27,15,290-->

### elimination of intersymbol interference

{@{One key principle of OFDM}@} is that since {@{low symbol rate modulation schemes (i.e., where the symbols are relatively long compared to the channel time characteristics)}@} suffer {@{less from intersymbol interference caused by multipath propagation}@}, it is {@{advantageous to transmit a number of low-rate streams in parallel}@} instead of a {@{single high-rate stream}@}. Since {@{the duration of each symbol is long}@}, it is feasible to insert {@{a guard interval between the OFDM symbols}@}, thus {@{eliminating the intersymbol interference}@}. <!--SR:!2026-01-28,16,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-27,15,290-->

To {@{avoid intersymbol interference in multipath fading channels}@}, an {@{OFDM block}@} is {@{preceded by a guard interval of length $T_{\mathrm g}$}@} during which a {@{cyclic prefix (CP) is transmitted}@}; the {@{CP consists of the last $T_{\mathrm g}$ seconds of the OFDM symbol}@} and is {@{appended to the front of the block}@} so that for {@{$-T_{\mathrm g}\le t<0$}@} the signal equals {@{the segment $(T-T_{\mathrm g})\le t<T$}@}. {@{This repetition}@} ensures that, when the {@{receiver performs FFT demodulation}@}, it {@{integrates over an integer number of sinusoid cycles for each multipath component}@}. The {@{resulting OFDM waveform with CP}@} can be written as {@{$$\nu(t)=\sum_{k=0}^{N-1}X_k e^{j2\pi kt/T}, \qquad -T_{\mathrm g}\le t<T,$$}@} where {@{$X_k$}@} are the {@{data symbols}@} and {@{$T$}@} is the {@{OFDM symbol duration}@}. <!--SR:!2026-01-27,15,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290-->

## advantages

{@{OFDM's main strengths}@} stem from its {@{ability to turn a frequency selective channel into a set of parallel flat fading sub‑channels}@}. {@{The cyclic prefix}@} eliminates {@{inter‑symbol interference}@} when {@{the channel impulse response fits within the guard interval}@}, effectively transforming {@{a potentially dispersive channel into independent sub‑carriers}@}. <!--SR:!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290-->

Because {@{each sub‑carrier experiences a distinct fading coefficient}@}, {@{OFDM naturally exploits _frequency diversity_}@}: even if some carriers are in {@{deep fade}@}, others can {@{carry the same information reliably}@}. {@{Forward error correction}@}—typically {@{convolutional coding with interleaving}@}—is {@{straightforward to integrate}@} because {@{each OFDM symbol can be decoded independently}@} before {@{channel estimation}@}. <!--SR:!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-28,16,290-->

By {@{equipping the transmitter with knowledge of the channel state}@}—through {@{feedback or reciprocity}@}—the system can perform {@{_bit loading_ (power water‑filling)}@} and {@{transmit a higher rate on strong sub‑carriers}@} while {@{allocating fewer bits to weak ones}@}. In practice, this mode {@{outperforms an ideal maximum‑likelihood equalizer}@} when the {@{transmitter has accurate channel information}@}. <!--SR:!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290-->

## disadvantages

Despite its benefits, OFDM incurs {@{several practical costs}@}. {@{The cyclic prefix}@} consumes {@{bandwidth and power}@}; for {@{a fixed sub‑carrier spacing}@} {@{the ratio of useful data to guard interval}@} grows as {@{the number of sub‑carriers $N$ increases}@}, so designers often {@{choose a larger $N$ to reduce this overhead}@}. However, {@{the _peak‑to‑average power_ (PAPR) rises with $N$}@}, requiring {@{a highly linear power amplifier}@}. {@{Typical OFDM systems employ $N$}@} ranging from {@{$2^7 = 128$ to $2^{11} = 2048$}@}; as {@{$N$ grows}@}, {@{both the PAPR and sensitivity to frequency offsets}@} become {@{more pronounced}@}. <!--SR:!2026-01-28,16,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-26,14,290!2026-01-28,16,290-->

{@{OFDM signals}@} are {@{highly susceptible to frequency offsets and Doppler shifts}@}: {@{a small carrier‑frequency error}@} produces {@{significant inter‑carrier interference}@} when {@{the sub‑carrier spacing $\Delta f = k/T_{\text{sym} }$ is small ($k$ is typically 1)}@}, which {@{typically occurs for large $N$}@}. For {@{high PAPR due to large $N$}@}, {@{the power amplifier must be _highly linear_}@} to {@{avoid distortion}@}. <!--SR:!2026-01-26,14,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-26,14,290!2026-01-26,14,290!2026-01-28,16,290-->

{@{Adjacent‑band rejection of OFDM spectra}@} is {@{limited (≈20–30&nbsp;dB)}@}, so an {@{access point in a wireless LAN}@} can {@{sometimes decode packets from neighboring channels}@}—an effect that {@{arises because the spectral skirts of OFDM symbols overlap substantially}@}. <!--SR:!2026-01-26,14,290!2026-01-28,16,290!2026-01-27,15,290!2026-01-27,15,290!2026-01-26,14,290-->
