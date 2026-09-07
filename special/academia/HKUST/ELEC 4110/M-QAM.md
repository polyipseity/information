---
aliases:
  - ELEC 4110 M-QAM
  - ELEC4110 M-QAM
  - M-QAM
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/M-QAM
  - language/in/English
---

# _M_-QAM

- see: [general/quadrature amplitude modulation](../../../../general/quadrature%20amplitude%20modulation.md)

{@{_Quadrature amplitude modulation_ (M-QAM)}@} extends {@{PSK \(which only varies phase\)}@} by varying {@{both phase and amplitude}@}, arranging {@{$\sqrt{M}\times\sqrt{M}$ points}@} on {@{a rectangular grid in the complex plane}@}. {@{Each symbol}@} carries {@{$\log_2M$ bits}@}. $M$ can be {@{increased without increasing bandwidth}@}, matching {@{PSK spectral efficiency for comparable error performance}@} at {@{higher signal-to-noise ratios \(higher transmit power\)}@}. M-QAM requires {@{two orthogonal carrier tones (in-phase and quadrature components)}@} regardless of {@{the modulation order $M$}@}.

## waveforms

For {@{symbol index $m = 0, \ldots, M - 1$}@} {@{the waveform}@} is {@{$$s_m(t)=I_m\,\sqrt{\frac{2E}{T_s} }\;\cos(2\pi f_c t)-Q_m\,\sqrt{\frac{2E}{T_s} }\;\sin(2\pi f_c t), \qquad 0\le t<T_s\,,$$}@} where {@{$I_m$ and $Q_m$ are the in-phase and quadrature amplitudes}@} chosen from {@{a rectangular grid}@} (e.g., {@{$\{-3,-1,1,3\}$ for 16-QAM}@}). {@{The scaling factor $\sqrt{2E/T_s}$}@} gives each {@{symbol unit average energy $E$ before overall power scaling}@}.

Typically, {@{$\alpha = \sqrt{E}$ is written}@}, where {@{$\alpha$ is half the spacing between symbols}@}.

## constellation

{@{An $M$-ary QAM constellation}@} forms {@{a rectangular grid of points in the two-dimensional signal space}@}, with {@{the horizontal axis}@} for {@{the in-phase component}@} and {@{the vertical axis}@} for {@{the quadrature component}@}, giving {@{$\sqrt{M}\times\sqrt{M}$ equally spaced points}@}. This layout {@{maximizes Euclidean distance between adjacent symbols}@} while {@{keeping the average power bounded}@}.

Assume {@{equiprobable symbols and AWGN}@}. {@{The decision regions}@} for {@{an $M$-ary QAM constellation}@} are {@{rectangular cells surrounding each lattice point}@}. For {@{a square grid with spacing $d$}@}, {@{boundaries}@} lie {@{midway between adjacent points}@}, so {@{the region for the symbol}@} at {@{coordinates $(i,j)$}@} is {@{$$R_{i,j}=\Bigl\{(x,y)\;\big|\;(i-\tfrac12)d \le x < (i+\tfrac12)d,\; (j-\tfrac12)d \le y < (j+\tfrac12)d\Bigr\} \,,$$}@} and {@{the receiver}@} selects {@{the symbol whose cell contains the received in-phase and quadrature components}@}. This assumes {@{interior points only}@}; boundary cells are {@{extended to infinity}@} along {@{the corresponding axis}@}.

## comparison with M-PSK

In practice, {@{16-QAM}@} is {@{more popular than 16-PSK}@}. Both use {@{sixteen symbols}@}, but QAM distributes {@{points on a rectangular grid}@}, allowing {@{the constellation}@} to be {@{expanded along both amplitude axes}@}. PSK points are {@{confined to a circle}@} and must be {@{packed more tightly in phase}@}. For {@{a given minimum distance}@}, QAM achieves {@{higher spectral efficiency}@} at {@{lower energy per bit}@}. 16-QAM delivers {@{superior error performance at moderate SNRs}@} and is {@{preferred in most high-rate communication systems}@}.

## energy

Using {@{$E = \alpha^2$}@}. To calculate {@{the average symbol energy $E_s$}@}, sum {@{the squares of all point coordinates and divide by $M$}@}. Start with {@{positive $x$-coordinates}@}: {@{$$\alpha^2 + (3\alpha)^2 + (5\alpha)^2 + \cdots = E \sum_{k = 1}^{\sqrt M / 2} (2k - 1)^2 \,.$$}@} Multiply by {@{2 for the negative $x$-coordinates}@}, by {@{$\sqrt{M}$ for the rows}@}, and by {@{2 for the $y$-coordinates}@}: {@{$$4E \sqrt M \sum_{k = 1}^{\sqrt M / 2} (2k - 1)^2 \,.$$}@} Divide by {@{$M$ for the average}@}: {@{$$\boxed{E_s = \frac {4E} {\sqrt M} \sum_{k = 1}^{\sqrt M / 2} (2k - 1)^2} \,.$$}@}

{@{This expression}@} is {@{cumbersome for large $M$}@}. Using {@{the sum of odd squares}@}: {@{$$\sum_{k = 1}^n (2n - 1)^2 = \frac {n(2n + 1)(2n - 1)} 3 \,,$$}@} with {@{$n = \sqrt M / 2$}@} gives {@{$$\boxed{E_s = \frac {4E} {\sqrt M} \frac {\sqrt M(\sqrt M + 1)(\sqrt M - 1)} 6 = \frac 2 3 (M - 1) E } \,,$$}@}. Conversely, {@{$E$ from $E_s$}@}: {@{$$\boxed{E = \frac 3 2 \frac {E_s} {M - 1} } \,.$$}@}

## error analysis

{@{A M-QAM}@} can be analyzed as {@{two independent M-PAM}@}, each having {@{$\sqrt M = 2^{k / 2}$ points}@}, since {@{the noise variance in the two coordinates}@} is {@{independent with variance $N_0 / 2$}@} each.

Assuming {@{equiprobable bits and AWGN}@}, {@{a $\sqrt M$-PAM}@} has the error probability: {@{$$P_{\mathrm{\sqrt M-PAM} } = 2 (1 - 1 / \sqrt M) Q\left(\sqrt {\frac {2E} {N_0} } \right) = \boxed {2 \left( \frac {\sqrt M - 1} {\sqrt M} \right) Q\left(\sqrt {\frac 3 {M - 1} \frac {E_s} {N_0} } \right) } \,.$$}@} Within {@{$Q(\cdot)$}@}, the argument comes from {@{half the shortest distance $\sqrt E$}@} divided by {@{the noise standard deviation $\sqrt{N_0/2}$}@}. {@{The factor $2(1 - 1 / \sqrt M)$}@} reflects that {@{error regions are two-sided (factor 2)}@} except for {@{the two edge symbols (factor $1 - 1 / \sqrt M$)}@}.

{@{The M-QAM}@} {@{symbol error probability}@} is: {@{$$P_{eM} = 1 - (1 - P_{\sqrt M} )^2 \le 1 - (1 - 2P_{\sqrt M}) = 2P_{\sqrt M} = \boxed{4 \left(\frac {\sqrt M - 1} {\sqrt M} \right) Q\left(\sqrt {\frac 3 {M - 1} \frac {E_s} {N_0} } \right) } \,,$$}@} where {@{the inequality}@} is {@{tight for small $P_{\sqrt M}$}@}.

Comparing {@{M-QAM with M-PSK}@}: {@{$$\begin{aligned} P_{\text{M-QAM} } & \approx 4 \left(\frac {\sqrt M - 1} {\sqrt M} \right) Q\left(\sqrt{\frac 3 {M - 1} \frac {E_s} {N_0} } \right) \\ P_{\text{M-PSK} } & \approx 2 Q\left(\sqrt{\frac {2E_s \sin^2(\pi / M) } {N_0} } \right) \,. \end{aligned}$$}@} {@{The _gain_ of M-QAM over M-PSK}@} is {@{the ratio of $Q(\cdot)$ arguments at fixed $E_s$}@}: {@{$$\text{gain} = \frac {3 / (M - 1)} {2 \sin^2(\pi / M) } \,.$$}@} This gain {@{increases rapidly with $M$}@}.

### symbol error probability bounds

For {@{$M$-quadrature amplitude keying}@}, {@{the exact symbol-error probability}@} is {@{_tightly bounded_ by simple analytic expressions}@} involving {@{only the _symbol_ SNR $E_s/N_0$ and constellation size $M$}@}. For {@{all $M\ge2$}@}: {@{$$Q\!\left(\sqrt{\frac {3E_s} {(M - 1)N_0} } \right) \;\leq\;P_{eM}\;\leq\; 4 \frac {\sqrt M - 1} {\sqrt M} \,Q\!\left(\sqrt{\frac {3E_s} {(M - 1)N_0} } \right) \,.$$}@} {@{The upper bound}@} becomes {@{asymptotically exact}@} as {@{$E_s/N_0$ increases}@}, since {@{$4 \frac {\sqrt M - 1} {\sqrt M}$ is the average number of nearest symbols}@}. {@{Increasing the _symbol_ SNR $E_s / N_0$}@} decreases {@{the symbol error probability}@}; {@{increasing $M$}@} increases it.

{@{The _lower bound_}@} uses {@{minimum distance arguments from [M-ary transmission § error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)}@}: {@{$$\boxed{\frac {d_{\text{min} } } 2 = \sqrt{E} = \sqrt{\frac {3E_s} {2(M - 1)} } } \,.$$}@} {@{A naive minimum-distance bound}@} yields {@{a factor of $M - 1$}@}, but examining {@{the error regions}@} gives {@{a tighter result}@}. For {@{an interior point}@}, {@{only 4 neighbors matter}@} since their error regions {@{contain those of the other $M - 5$ points}@}, giving {@{factor 4 instead of $M - 1$}@}. {@{Boundary points}@} have {@{fewer neighbors}@}: {@{factor 3 for non-corner edge points}@}, {@{2 for corners}@}. {@{Averaging over all equiprobable points}@} gives {@{$4 \frac {\sqrt M - 1} {\sqrt M}$}@}. Some sources use {@{factor 4}@} by assuming {@{all points have 4 neighbors}@}.

### bit error probability

In {@{M-quadrature amplitude modulation}@}, {@{the bit-error probability}@} depends on {@{the labeling scheme}@} as well as the modulation order. With {@{ordinary binary coding}@}, {@{a symbol error}@} can {@{flip several bits}@}. With {@{Gray coding}@}, {@{adjacent symbols differ in only one bit}@}, so {@{most symbol errors}@}—those between {@{neighboring points}@}—produce {@{exactly one erroneous bit}@}. This yields: {@{$$\boxed{P_{e, b} \approx \frac {P_{e, M} } k = \frac {P_{e, M} } {\log_2 M} } \,,$$}@} accurate at {@{moderate to high SNR}@}.

## bit coding

In {@{an $M$-ary QAM constellation}@}, {@{the symbols}@} sit on {@{a two-dimensional grid}@} (typically {@{$\sqrt{M}\times\sqrt{M}$}@}).  {@{Each symbol}@} is indexed by {@{an integer $k\in[0,M-1]$}@} whose {@{binary representation of length $\log_2 M$}@} serves as {@{the bit pattern}@}.  With {@{this natural mapping}@}, {@{adjacent symbols}@} can {@{differ in several bits}@}.

{@{Gray coding for QAM}@} ensures {@{neighboring points differ in only one bit}@} so that {@{a single symbol error}@} produces {@{at most one erroneous bit}@}.  {@{A Gray code}@} is built by constructing {@{a one-dimensional Gray sequence of length $\sqrt{M}$}@} via {@{the recursive "mirror and toggle" method}@}, then forming {@{the two-dimensional grid}@} while preserving {@{the Gray property along both axes}@}.

{@{The assignment of Gray codes to QAM points}@} works {@{row-by-row}@}: {@{the Gray index}@} for {@{a point at coordinates $(i,j)$}@} concatenates {@{the $j$-th Gray bit (column) with the $i$-th Gray bit (row)}@}.  The result: {@{horizontal and vertical neighbors differ in one bit}@}, {@{diagonal neighbors in two bits}@}, reducing {@{the average bit-error probability}@} under {@{additive white Gaussian noise}@}.

{@{Another possible assignment \(different from above\)}@} for {@{16-QAM}@}. First, write {@{$[00, 01, 10, 11]$ in Z-order at the top left quadrant}@}. Then {@{_mirror_ \(not simply copying\) this quadrant across both axes}@} to generate {@{the remaining quadrants}@} — these are {@{the upper 2 bits}@}. For {@{the lower 2 bits}@}, write {@{the corresponding element of $[00, 01, 10, 11]$ 4 times}@} {@{for each quadrant in Z-order}@}. {@{The upper bits}@} {@{"vary" faster over shorter distances}@}. \(annotation: __this course__: Maybe {@{use this}@}?\)
