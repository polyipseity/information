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

{@{__Orthogonal frequency-division multiplexing__ (__OFDM__)}@} is {@{a modulation scheme}@} that {@{divides a frequency-selective fading channel into many narrowband flat sub-channels}@} and {@{transmits data on them in parallel}@}. {@{The subcarrier frequencies are spaced}@} so that {@{each subcarrier is orthogonal to the others}@} — using {@{the DFT basis $\set{e^{j 2\pi nt/T} }$}@}, where {@{$n \in \set{0, \ldots, N - 1}$}@} is {@{the subcarrier index}@} and {@{$T$}@} is {@{the OFDM symbol time}@} — which {@{eliminates inter-carrier interference (ICI)}@} and {@{inter-symbol interference (ISI)}@} at {@{the ideal sampling points}@}.

## motivation

{@{Orthogonal subcarrier spacing}@} removes {@{the need for guard bands, saving bandwidth}@}. {@{The subcarrier spacing}@} is {@{$\Delta f\,=\,{\frac {k}{T_{U} } }$ Hz}@}, where {@{_T<sub>U</sub>_ seconds}@} is {@{the useful symbol duration}@} and {@{_k_}@} is {@{a positive integer, typically 1}@}. {@{Each carrier frequency}@} completes {@{_k_ more cycles per symbol period than the previous carrier}@}, so {@{_N_ subcarriers}@} give {@{a total bandwidth of _B_&nbsp;≈&nbsp;_N_·Δ<!-- markdown separator -->_f_&nbsp;(Hz)}@}. {@{The orthogonality}@} also simplifies {@{transmitter and receiver design}@}: unlike {@{conventional FDM}@}, {@{a separate filter per sub-channel is unnecessary}@}.

## operation

{@{Each subcarrier}@} carries {@{a data stream}@}. {@{A 2D modulation scheme}@} — {@{QAM, PSK, but not M-FSK}@} — maps {@{groups of bits to complex symbols $X_k$}@} on {@{a constellation diagram}@}. In {@{OFDM}@}, instead of {@{quadrature-mixing each subcarrier separately}@}, all subcarriers are {@{multiplied by the DFT basis and summed}@}: {@{$$\nu(t) = \sum_{k = 0}^{N - 1} X_k e^{j 2\pi k t/T} \qquad 0 \le t < T \,,$$}@} where {@{$N$}@} is {@{the number of subcarriers}@} and {@{$T$}@} is {@{the OFDM symbol time}@}. This sum is {@{the IDFT followed by a DAC}@}; {@{quadrature-mixing to passband}@} happens only {@{once on the composite waveform}@}.

To {@{decode}@}: {@{downconvert to baseband}@}, {@{digitize via ADC}@}, {@{apply DFT to recover each $X_k$}@}, then {@{demodulate each subcarrier independently}@}. Different subcarriers may use {@{different modulation schemes}@}.

### elimination of intersymbol interference

To {@{avoid ISI in multipath channels}@}, each {@{OFDM block}@} is {@{prepended with a cyclic prefix (CP)}@}: {@{the last $T_{\mathrm g}$ seconds of the symbol}@} are {@{copied to the front}@}, giving {@{a guard interval of length $T_{\mathrm g}$}@}. When {@{$-T_{\mathrm g}\le t<0$}@}, the signal equals {@{the segment $(T-T_{\mathrm g})\le t<T$}@}. {@{The receiver FFT}@} then {@{integrates over an integer number of cycles per multipath component}@}. {@{The signal with CP}@} is: {@{$$\nu(t)=\sum_{k=0}^{N-1}X_k e^{j2\pi kt/T}, \qquad -T_{\mathrm g}\le t<T,$$}@}

## advantages

- Converts {@{a frequency-selective channel into parallel flat sub-channels}@}; {@{CP eliminates ISI}@} when {@{the channel impulse response fits in the guard interval}@}.
- {@{Frequency diversity}@}: {@{independent fading per subcarrier}@} means {@{FEC (e.g. convolutional coding with interleaving)}@} can {@{recover data even when some carriers are in deep fade}@}.
- {@{Power loading (water-filling)}@}: when {@{the transmitter has channel state info via feedback or reciprocity}@}, it sends {@{more bits on strong sub-carriers and fewer on weak ones}@}, outperforming {@{a maximum-likelihood equalizer}@}.

## disadvantages

- {@{CP overhead}@}: {@{the ratio of useful data to guard interval grows with $N$}@}, but {@{increasing $N$}@} raises {@{peak-to-average power ratio (PAPR)}@}, requiring {@{a linear power amplifier}@}. Typical systems use {@{$N = 128$ to $2048$}@}.
- {@{Frequency sensitivity}@}: {@{small carrier-frequency errors}@} cause {@{significant ICI}@} because {@{sub-carrier spacing $\Delta f = k/T_{\text{sym} }$ is small for large $N$}@}.
- {@{Limited adjacent-band rejection (≈20–30&nbsp;dB)}@}: {@{spectral skirts overlap}@}, so {@{an access point may decode packets}@} from {@{neighboring channels}@}.
