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

{@{_M_-ary phase shift keying_ (M-PSK)}@} maps {@{$\log_2M$ bits onto one of $M$ equally spaced points}@} on {@{a unit circle in the constellation diagram}@}. The points form {@{a regular polygon}@}. {@{Amplitude stays constant}@} while {@{only phase varies}@}, so {@{M-PSK}@} is {@{immune to linear amplitude distortions}@} but {@{susceptible to phase noise and nonlinearities}@}. Increasing $M$ {@{does not increase bandwidth}@}, giving {@{high spectral efficiency}@} at the cost of {@{higher bit error rates}@}. <!--SR:!2027-01-01,289,340!2027-03-17,352,358!2027-04-09,373,365!2027-04-06,372,365!2027-05-14,403,365!2027-05-16,405,365!2027-05-07,397,365!2027-03-01,340,358!2027-01-03,291,340!2027-05-16,405,365!2027-01-14,300,340!2026-11-16,251,330-->

## waveforms

For {@{an $M$-ary PSK system}@}, {@{the transmitted waveform for symbol $m\in\{0,\dots ,M-1\}$}@} is {@{$$s_m(t)=A\,\cos \!\bigl(2\pi f_c t+\varphi_m\bigr),\qquad 0\le t<T_s \,,$$}@} where {@{$\varphi_m=\frac{2\pi m}{M}$, $f_c$ is the carrier frequency, and $T_s$ is the symbol duration}@}. Usually $f_c$ is {@{a multiple of $1 / T_s$}@}. {@{The amplitude $A=\sqrt{\dfrac{2E}{T_s} }$}@} ensures each symbol has {@{the same average energy $E$}@}. <!--SR:!2027-01-04,292,340!2027-03-18,355,365!2027-01-12,283,338!2026-11-19,253,330!2027-05-05,396,365!2027-03-03,341,358!2027-05-10,400,365-->

## constellation

{@{The $M$-ary PSK constellation}@} consists of {@{$M$ equally spaced points on the unit circle}@}, each {@{distinguished solely by phase angle}@}. All have {@{the same amplitude}@}, forming {@{a regular polygon when plotted with orthogonal basis functions}@}. <!--SR:!2027-04-12,376,365!2027-04-06,369,358!2027-05-08,398,365!2027-01-21,305,340!2027-01-09,296,340-->

Assume {@{equiprobable symbols and AWGN}@}. {@{The decision regions}@} in {@{the constellation plane}@} are {@{the sets of received signal vectors closer to one symbol than any other}@}. Since points sit on {@{the unit circle at angles $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}, each region is {@{an angular sector spanning $\frac{2\pi}{M}$}@}, bounded by {@{lines bisecting the angle between adjacent symbols}@}. <!--SR:!2027-04-04,367,358!2027-01-26,309,340!2027-01-06,294,340!2027-01-13,299,340!2027-04-23,384,358!2027-03-26,362,365!2027-04-08,371,358-->

## special cases

{@{_Binary PSK_ \(BPSK\), _quadrature PSK_ \(QPSK\), and _8-PSK_}@} are the most common cases. {@{BPSK}@} has {@{two antipodal points ($M=2$)}@} conveying {@{one bit per symbol}@}; {@{QPSK}@} has {@{four points ($M=4$)}@} conveying {@{two bits per symbol}@}; {@{8-PSK}@} uses {@{eight points}@} conveying {@{three bits per symbol}@}. All share {@{the same carrier bandwidth}@}: only {@{two orthogonal tones (in-phase and quadrature)}@} are used {@{regardless of modulation order $M$}@}. <!--SR:!2027-03-20,356,365!2026-11-09,245,330!2027-05-15,404,365!2027-03-09,346,358!2027-03-05,344,365!2027-01-03,291,340!2027-03-08,347,365!2027-04-07,370,358!2027-01-01,289,340!2027-05-06,396,365!2027-04-20,381,358!2027-04-19,380,358!2027-01-01,289,340-->

Under {@{equal symbol energies and two-dimensional signal space}@}, {@{QPSK is optimal among quartic schemes}@} since {@{any four-point constellation}@} must have {@{the same symbols}@}; {@{the only way to improve performance}@} is to increase {@{minimum Euclidean distance}@}, which {@{QPSK already maximizes}@}. <!--SR:!2027-01-04,292,340!2027-03-31,365,365!2027-04-28,389,365!2027-01-15,301,340!2027-01-28,311,340!2026-11-20,254,330!2027-02-07,320,340-->

## error analysis

Assume {@{equiprobable bits and AWGN of two-sided PSD $N_0$}@}. {@{The symbol-error probability for coherent $M$-PSK}@} equals the integral {@{$$\boxed{P_{eM} = \frac 1 {\pi} \int_0^{\pi (1 - 1/M)} \! \exp\left(\frac {E_s} {N_0} \frac {\sin^2(\pi / M) } {\sin^2(\phi)} \right) \,\mathrm d\phi } \,.$$}@} {@{This expression (Equation&nbsp;4-98 in Ziemer & Peterson)}@} holds for {@{any integer $M \ge 2$}@}, but {@{closed-form results exist}@} only for {@{$M=2$ (BPSK) and $M=4$ (QPSK)}@}. {@{Larger constellations}@} require {@{numerical evaluation}@}. <!--SR:!2027-04-10,375,365!2027-05-11,401,365!2027-01-20,305,340!2027-02-10,322,340!2027-03-24,360,365!fsrs,2028-11-03T00:00:00.000Z,761,760.63601177,2.23046173,2,9,0,0,2026-10-04T00:00:00.000Z!2027-01-05,293,340!2027-05-10,400,365!2027-05-17,406,365-->

### symbol error probability bounds

For {@{coherent $M$-PSK}@}, {@{the symbol-error probability}@} is {@{tightly bounded}@}: {@{$$Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \;\leq\;P_{eM}\;\leq\; 2\,Q\!\left(\sqrt{\frac{2E_s}{N_0} }\sin\frac{\pi}{M}\right) \,.$$}@} {@{The upper bound}@} becomes {@{asymptotically exact}@} as {@{$E_s/N_0$ increases}@}, since {@{the average number of nearest neighbors is 2}@}. {@{Increasing $E_s / N_0$}@} decreases {@{error probability}@}; {@{increasing $M$}@} increases it. <!--SR:!2027-01-16,301,340!2027-03-14,352,365!2027-05-15,404,365!2026-10-25,233,338!2027-01-04,292,340!fsrs,2027-11-05T00:00:00.000Z,413,413.00268788,2.86735337,2,8,0,0,2026-09-18T00:00:00.000Z!2026-11-15,250,330!2027-01-17,303,340!2027-05-06,396,365!2027-01-16,302,340!2027-04-11,375,365-->

{@{The lower bound}@} comes from {@{the minimum distance argument in [M-ary transmission § error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)}@}, giving {@{half the minimum distance}@}: {@{$$\boxed{\frac {d_{\text{min} } } 2 = \sqrt{E_s} \sin(\pi / M) } \,.$$}@} {@{The upper bound}@} would naively use {@{$M - 1$ (one per non-matching constellation point)}@}, but this {@{can be improved}@}. For {@{any fixed point}@}, the error regions of {@{the $M - 3$ farthest points}@} lie inside {@{the union of the 2 nearest neighbors' error regions}@}, so they can be dropped, reducing {@{the factor from $M - 1$ to 2}@}. <!--SR:!2027-04-17,378,358!2026-11-24,259,345!2027-04-18,379,358!2027-05-08,398,365!2027-02-11,323,340!2027-01-05,293,340!2027-04-22,384,365!2027-02-06,319,340!2027-05-11,401,365!2027-03-30,365,365!2027-04-11,376,365-->

### bit error probability

In {@{coherent $M$-PSK}@}, {@{the bit-error probability}@} depends on {@{how bits are mapped to constellation points}@}. With {@{ordinary binary coding}@}, a single {@{symbol error can flip several bits}@}, but {@{Gray coding}@} ensures {@{adjacent symbols differ in only one bit}@}, so most errors cause {@{exactly one bit error}@}. <!--SR:!2027-01-12,299,340!2027-05-12,401,365!2027-04-20,381,358!2027-05-06,396,365!2027-01-27,310,340!2027-03-31,364,358!2027-05-13,402,365!2027-03-06,345,365-->

Thus, with {@{Gray coding}@} the approximation holds: {@{$$\boxed{P_{e, b} \approx \frac {P_{e, M} } k = \frac {P_{e, M} } {\log_2 M} } \,,$$}@} which is {@{accurate at moderate to high SNR}@}. <!--SR:!2027-03-29,363,365!2027-04-16,378,358!2027-04-13,375,358-->

## bit coding

In {@{an $M$-ary PSK system}@}, {@{each symbol}@} is assigned {@{a phase angle $\theta_k=\frac{2\pi k}{M}$ ($k=0,\dots,M-1$)}@}. {@{Natural coding}@} maps {@{the binary representation of $k$ to the symbol}@}, so {@{the most significant bit changes least frequently}@} as $k$ grows. This yields {@{uniform phase spacing}@} but does not {@{minimize bit error probability}@}. <!--SR:!2027-01-12,299,340!2027-05-17,406,365!2027-05-09,399,365!2027-04-05,368,358!2027-01-06,294,340!2027-02-08,321,340!2027-01-22,306,340!2027-04-22,383,358-->

{@{_Gray coding_}@} instead ensures that {@{adjacent points differ in only one bit}@}. For PSK, {@{a Gray code is built recursively}@}: start with {@{the two-point code $[0,1]$}@}; for each {@{doubling of $M$}@}, append {@{the reverse of the current sequence with its MSB toggled}@} (e.g. from {@{$[00,01]$ to $[00,01,11,10]$}@}). The result is {@{a binary sequence where successive entries differ by one bit}@}. <!--SR:!2027-05-14,403,365!2027-04-29,390,365!2027-05-13,402,365!2027-01-13,299,340!2027-01-02,290,340!2027-04-15,377,358!2027-05-08,398,365!2027-04-17,378,358-->

When {@{applied to PSK}@}, {@{Gray indices}@} are mapped {@{onto the phase angles $\theta_k$}@}. {@{The receiver}@} decodes {@{the most probable symbol and reads its Gray code}@}, reducing {@{multi-bit errors from single symbol errors}@}. In practice this uses {@{an $M$-to-$\log_2 M$ binary encoder}@} followed by {@{a look-up table}@} mapping {@{each Gray index to the corresponding phase}@}. <!--SR:!2026-11-03,240,330!2027-01-14,300,340!2027-05-09,399,365!2027-05-14,403,365!2027-04-21,382,358!2027-05-11,401,365!2027-02-05,318,340!2027-04-19,380,358!2027-05-07,397,365-->
