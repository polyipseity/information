---
aliases:
  - ELEC 4110 M-PSK
  - ELEC4110 M-PSK
  - M-PSK
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/M-PSK
  - language/in/English
---

# _M_-PSK

- see: [general/phase-shift keying](../../../../general/phase-shift%20keying.md)

{@{_M-ary phase shift keying_ (M-PSK)}@} maps {@{$\log_2M$ bits onto one of $M$ equally spaced points}@} on {@{a unit circle in the constellation diagram}@}, forming {@{a regular polygon constellation}@}. {@{The modulation}@} is {@{purely phase-based}@}; {@{amplitude remains constant}@}, which makes M-PSK {@{immune to linear amplitude distortions}@} but {@{susceptible to phase noise and nonlinearities}@}. $M$ can be {@{increased without increasing bandwidth}@}, enabling {@{high spectral efficiency}@} at the expense of {@{higher bit error rates}@}.

## waveforms

For {@{an $M$-ary PSK system}@} {@{the transmitted waveform corresponding to symbol index $m\in\{0,\dots ,M-1\}$}@} is {@{$$s_m(t)=A\,\cos \!\bigl(2\pi f_c t+\varphi_m\bigr),\qquad 0\le t<T_s \,,$$}@} where {@{$f_c$ is the carrier frequency, $T_s$ is the symbol duration}@}, and {@{$\varphi_m=\frac{2\pi m}{M}$}@}. Typically, {@{$f_c$ is a multiple of $1 / T_s$}@}. {@{The constant amplitude $A=\sqrt{\dfrac{2E}{T_s} }$}@} guarantees that {@{each symbol has the same average energy $E$}@}.

## constellation

{@{The $M$-ary PSK constellation}@} consists of {@{$M$ equally spaced points lying on the circumference of a unit circle in the signal space}@}. {@{Each point}@} corresponds to {@{one symbol}@} and is distinguished {@{solely by its phase angle}@}; {@{all symbols}@} have {@{identical amplitude}@}, which yields {@{a regular polygon shape when plotted with orthogonal basis functions}@}.

Assume {@{equiprobable symbols and AWGN}@}. {@{The decision regions}@} for {@{an $M$-ary PSK system}@} are defined in {@{the constellation plane}@} as the set of {@{all received signal vectors that are closer to a particular transmitted symbol than to any other}@}. Since {@{the constellation points}@} lie on {@{a unit circle at angles $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}, {@{each decision region}@} is {@{an angular sector spanning $\frac{2\pi}{M}$ radians}@}, bounded by {@{lines that bisect the angle between adjacent symbols}@}.

## special cases

{@{_Binary PSK_ \(BPSK\), _quadrature PSK_ \(QPSK\), and _8-PSK_}@} are {@{the most common special cases}@}: {@{BPSK}@} uses {@{two antipodal points ($M=2$)}@} and conveys {@{one bit per symbol}@}; {@{QPSK}@} employs {@{four points arranged in a square grid ($M=4$)}@}, delivering {@{two bits per symbol}@}; {@{8-PSK}@} uses {@{eight equally spaced points on the unit circle}@} and conveys {@{three bits per symbol}@}. All preserve {@{the fixed-tone bandwidth characteristic}@} of PSK systems; {@{only two orthogonal carrier tones \(in-phase and quadrature components\)}@} is {@{used regardless of the modulation order $M$}@}.

Under {@{equal symbol energies and two-dimensional signal space}@}, {@{QSK is optimal for quartic modulation}@} as {@{any alternative quartic scheme}@} must {@{also use four symbols}@}; {@{the only way to improve performance}@} would be to {@{increase minimum Euclidean distance}@}, which is {@{already maximal for QPSK}@}.

## error analysis

Assume {@{equiprobable bits and AWGN of two-sided PSD $N_0$}@}. {@{The symbol-error probability}@} for {@{coherent $M$-phase shift keying}@} can be expressed {@{exactly as a sum of exponential terms}@} involving {@{the ratio $E_s/N_0$ and $\sin(\pi/M)$}@}: {@{$$\boxed{P_{eM} = \frac 1 {\pi} \int_0^{\pi (1 - 1/M)} \! \exp\left(\frac {E_s} {N_0} \frac {\sin^2(\pi / M) } {\sin^2(\phi)} \right) \,\mathrm d\phi } \,.$$}@} {@{This exact expression (Equation&nbsp;4-98 in Ziemer & Peterson)}@} is {@{valid for any integer $M \ge 2$}@}, but {@{closed-form results exist only}@} for {@{the simplest cases $M=2$ (BPSK) and $M=4$ (QPSK)}@}; for {@{all larger constellations}@} {@{a numerical integration of the formula}@} is required to {@{obtain the error probability}@}.

### symbol error probability bounds

For {@{coherent $M$-phase shift keying}@} {@{the exact symbol-error probability}@} can be {@{_tightly bounded_ by simple analytic expressions}@} that involve {@{only the ratio $E_s/N_0$ and the constellation size $M$}@}. In particular, for {@{all $M\ge2$}@}: {@{$$Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \;\leq\;P_{eM}\;\leq\; 2\,Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \,.$$}@} {@{This upper bound}@} becomes {@{asymptotically exact \("very tight"\)}@} as {@{$E_s/N_0$ increases}@}, as {@{_2_ is also the average number of nearest symbols}@}. Here, we see {@{increasing the _symbol_ SNR $E_s / N_0$}@} {@{decreases the symbol error probability}@}, while {@{increasing $M$}@} {@{increases it}@}.

{@{The _lower bound_}@} can be obtained {@{using the minimum distance arguments outlined in [M-ary transmission § error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)}@}; here, {@{half of the minimum distance $d_{\text{min} } / 2$}@} is: {@{$$\boxed{\frac {d_{\text{min} } } 2 = \sqrt{E_s} \sin(\pi / M) } \,.$$}@} However, {@{the _upper bound_}@} obtained would have had {@{a factor of $M - 1$ instead of 2}@}. To obtain {@{the factor 2}@}, we need to consider {@{the error regions}@}. For {@{a fixed constellation point}@}, consider {@{the union of the error regions of the 2 nearest point}@} and compare it against {@{the union of the error regions of the $M - 3$ other points}@}. We see {@{the former fully contains the latter as a subset}@}. So {@{the union bound}@} can be {@{made much tighter}@} by noting {@{the error regions contributed by the $M - 3$ other points}@} are {@{already contained in the union of the error regions for the nearest 2 points}@}, and thus {@{can be discarded}@}, resulting in {@{the factor 2 instead of $M - 1$}@}.

### bit error probability

In {@{coherent M-phase shift keying}@} the {@{bit-error probability}@} is {@{not fixed by the modulation order alone}@}; it also depends on {@{how bits are mapped to constellation points (the labeling scheme)}@}.  For {@{ordinary binary coding}@}, {@{a symbol error}@} can {@{flip several bits}@}, whereas {@{Gray coding}@} ensures that {@{adjacent symbols differ in only one bit}@}.  

Consequently, with {@{Gray coding}@} {@{most symbol errors}@}—those that are {@{statistically most likely}@} because the receiver is {@{confused between neighboring points}@}—result in {@{exactly one erroneous bit}@}, greatly reducing {@{the overall bit-error rate}@}. Thus, we have {@{the following approximation for modulation schemes using Gray coding}@}: {@{$$\boxed{P_{e, b} \approx \frac {P_{e, M} } k = \frac {P_{e, M} } {\log_2 M} } \,,$$}@} which is {@{accurate when SNR is moderate to high}@}.

## bit coding

In {@{an $M$-ary PSK system}@} {@{each symbol}@} is represented by {@{a phase angle $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}. {@{The simplest mapping}@} between {@{the transmitted bits and these phases}@} assigns {@{the binary representation of the integer $k$ to the symbol}@}, so that {@{the most significant bit (MSB) changes}@} least frequently as {@{$k$ increases}@}.  {@{This conventional "natural" coding}@} yields {@{a uniform spacing of symbols}@} but does not {@{guarantee minimal bit error probability}@}.

{@{_Gray coding_}@} addresses this by ensuring that {@{adjacent constellation points differ in only one bit}@}.  For PSK, {@{a Gray code}@} can be {@{constructed recursively}@}: start with {@{the two-point ($M=2$) code $[0,1]$}@}; for {@{each subsequent doubling of $M$}@} append {@{the reverse of the existing sequence to itself \(e.g. $[00, 01, 01, 00]$\)}@} and {@{toggle the MSB of the new entries \(e.g. $[00, 01, 11, 10]$\)}@}.  This yields {@{a binary sequence}@} where {@{successive symbols differ by a single bit}@}.

When {@{applied to PSK}@}, {@{the Gray-coded indices}@} are {@{mapped directly onto the phase angles $\theta_k$}@}.  {@{The receiver}@} therefore decodes {@{the most probable symbol}@} and interprets {@{its Gray code to recover the transmitted bits}@}, reducing {@{the probability that a symbol error causes multiple bit errors}@}.  In practice, {@{this mapping}@} is implemented by {@{an $M$-to-$m=\log_2 M$ binary encoder}@} followed by {@{a look-up table}@} that associates {@{each Gray index with the corresponding phase}@}.
