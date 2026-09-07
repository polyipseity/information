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

{@{_M_-ary phase shift keying_ (M-PSK)}@} maps {@{$\log_2M$ bits onto one of $M$ equally spaced points}@} on {@{a unit circle in the constellation diagram}@}. The points form {@{a regular polygon}@}. {@{Amplitude stays constant}@} while {@{only phase varies}@}, so {@{M-PSK}@} is {@{immune to linear amplitude distortions}@} but {@{susceptible to phase noise and nonlinearities}@}. Increasing $M$ {@{does not increase bandwidth}@}, giving {@{high spectral efficiency}@} at the cost of {@{higher bit error rates}@}.

## waveforms

For {@{an $M$-ary PSK system}@}, {@{the transmitted waveform for symbol $m\in\{0,\dots ,M-1\}$}@} is {@{$$s_m(t)=A\,\cos \!\bigl(2\pi f_c t+\varphi_m\bigr),\qquad 0\le t<T_s \,,$$}@} where {@{$\varphi_m=\frac{2\pi m}{M}$, $f_c$ is the carrier frequency, and $T_s$ is the symbol duration}@}. Usually $f_c$ is {@{a multiple of $1 / T_s$}@}. {@{The amplitude $A=\sqrt{\dfrac{2E}{T_s} }$}@} ensures each symbol has {@{the same average energy $E$}@}.

## constellation

{@{The $M$-ary PSK constellation}@} consists of {@{$M$ equally spaced points on the unit circle}@}, each {@{distinguished solely by phase angle}@}. All have {@{the same amplitude}@}, forming {@{a regular polygon when plotted with orthogonal basis functions}@}.

Assume {@{equiprobable symbols and AWGN}@}. {@{The decision regions}@} in {@{the constellation plane}@} are {@{the sets of received signal vectors closer to one symbol than any other}@}. Since points sit on {@{the unit circle at angles $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}, each region is {@{an angular sector spanning $\frac{2\pi}{M}$}@}, bounded by {@{lines bisecting the angle between adjacent symbols}@}.

## special cases

{@{_Binary PSK_ \(BPSK\), _quadrature PSK_ \(QPSK\), and _8-PSK_}@} are the most common cases. {@{BPSK}@} has {@{two antipodal points ($M=2$)}@} conveying {@{one bit per symbol}@}; {@{QPSK}@} has {@{four points ($M=4$)}@} conveying {@{two bits per symbol}@}; {@{8-PSK}@} uses {@{eight points}@} conveying {@{three bits per symbol}@}. All share {@{the same carrier bandwidth}@}: only {@{two orthogonal tones (in-phase and quadrature)}@} are used {@{regardless of modulation order $M$}@}.

Under {@{equal symbol energies and two-dimensional signal space}@}, {@{QPSK is optimal among quartic schemes}@} since {@{any four-point constellation}@} must have {@{the same symbols}@}; {@{the only way to improve performance}@} is to increase {@{minimum Euclidean distance}@}, which {@{QPSK already maximizes}@}.

## error analysis

Assume {@{equiprobable bits and AWGN of two-sided PSD $N_0$}@}. {@{The symbol-error probability for coherent $M$-PSK}@} equals the integral {@{$$\boxed{P_{eM} = \frac 1 {\pi} \int_0^{\pi (1 - 1/M)} \! \exp\left(\frac {E_s} {N_0} \frac {\sin^2(\pi / M) } {\sin^2(\phi)} \right) \,\mathrm d\phi } \,.$$}@} {@{This expression (Equation&nbsp;4-98 in Ziemer & Peterson)}@} holds for {@{any integer $M \ge 2$}@}, but {@{closed-form results exist}@} only for {@{$M=2$ (BPSK) and $M=4$ (QPSK)}@}. {@{Larger constellations}@} require {@{numerical evaluation}@}.

### symbol error probability bounds

For {@{coherent $M$-PSK}@}, {@{the symbol-error probability}@} is {@{tightly bounded}@}: {@{$$Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \;\leq\;P_{eM}\;\leq\; 2\,Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \,.$$}@} {@{The upper bound}@} becomes {@{asymptotically exact}@} as {@{$E_s/N_0$ increases}@}, since {@{the average number of nearest neighbors is 2}@}. {@{Increasing $E_s / N_0$}@} decreases {@{error probability}@}; {@{increasing $M$}@} increases it.

{@{The lower bound}@} comes from {@{the minimum distance argument in [M-ary transmission § error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)}@}, giving {@{half the minimum distance}@}: {@{$$\boxed{\frac {d_{\text{min} } } 2 = \sqrt{E_s} \sin(\pi / M) } \,.$$}@} {@{The upper bound}@} would naively use {@{$M - 1$ (one per non-matching constellation point)}@}, but this {@{can be improved}@}. For {@{any fixed point}@}, the error regions of {@{the $M - 3$ farthest points}@} lie inside {@{the union of the 2 nearest neighbors' error regions}@}, so they can be dropped, reducing {@{the factor from $M - 1$ to 2}@}.

### bit error probability

In {@{coherent $M$-PSK}@}, {@{the bit-error probability}@} depends on {@{how bits are mapped to constellation points}@}. With {@{ordinary binary coding}@}, a single {@{symbol error can flip several bits}@}, but {@{Gray coding}@} ensures {@{adjacent symbols differ in only one bit}@}, so most errors cause {@{exactly one bit error}@}.

Thus, with {@{Gray coding}@} the approximation holds: {@{$$\boxed{P_{e, b} \approx \frac {P_{e, M} } k = \frac {P_{e, M} } {\log_2 M} } \,,$$}@} which is {@{accurate at moderate to high SNR}@}.

## bit coding

In {@{an $M$-ary PSK system}@}, {@{each symbol}@} is assigned {@{a phase angle $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}. {@{Natural coding}@} maps {@{the binary representation of $k$ to the symbol}@}, so {@{the most significant bit changes least frequently}@} as $k$ grows. This yields {@{uniform phase spacing}@} but does not {@{minimize bit error probability}@}.

{@{_Gray coding_}@} instead ensures that {@{adjacent points differ in only one bit}@}. For PSK, {@{a Gray code is built recursively}@}: start with {@{the two-point code $[0,1]$}@}; for each {@{doubling of $M$}@}, append {@{the reverse of the current sequence with its MSB toggled}@} (e.g. from {@{$[00,01]$ to $[00,01,11,10]$}@}). The result is {@{a binary sequence where successive entries differ by one bit}@}.

When {@{applied to PSK}@}, {@{Gray indices}@} are mapped {@{onto the phase angles $\theta_k$}@}. {@{The receiver}@} decodes {@{the most probable symbol and reads its Gray code}@}, reducing {@{multi-bit errors from single symbol errors}@}. In practice this uses {@{an $M$-to-$\log_2 M$ binary encoder}@} followed by {@{a look-up table}@} mapping {@{each Gray index to the corresponding phase}@}.
