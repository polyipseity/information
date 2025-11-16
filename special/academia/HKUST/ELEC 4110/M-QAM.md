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

{@{_Quadrature amplitude modulation_ (M-QAM)}@} extends {@{PSK \(which only varies phase\)}@} by {@{varying both phase and amplitude}@}, arranging {@{$\sqrt{M}\times\sqrt{M}$ points}@} on {@{a rectangular grid in the complex plane}@}. {@{Each symbol}@} carries {@{$\log_2M$ bits}@}. $M$ can be {@{increased without increasing bandwidth}@}, enabling {@{equal spectral efficiency to PSK for comparable error performance}@} while operating at {@{higher signal-to-noise ratios \(higher transmit power\)}@}. M-QAM requires {@{two orthogonal carrier tones (in-phase and quadrature components)}@} regardless of {@{the modulation order $M$}@}.

## waveforms

For {@{symbol index $m = 0, \ldots, M - 1$}@} {@{the waveform}@} is {@{$$s_m(t)=I_m\,\sqrt{\frac{2E}{T_s} }\;\cos(2\pi f_c t)+Q_m\,\sqrt{\frac{2E}{T_s} }\;\sin(2\pi f_c t), \qquad 0\le t<T_s\,,$$}@} where {@{$I_m$ and $Q_m$ are the in-phase and quadrature amplitudes}@} chosen from {@{a rectangular grid}@} (e.g., {@{$\{-3,-1,1,3\}$ for 16-QAM}@}). {@{The scaling factor $\sqrt{2E/T_s}$}@} ensures that {@{each symbol has unit average energy $E$}@} before {@{any overall power scaling is applied}@}.

## constellation

{@{An $M$-ary QAM constellation}@} forms {@{a rectangular grid of points in the two-dimensional signal space}@}. {@{The horizontal axis}@} represents {@{the in-phase component}@} and {@{the vertical axis}@} {@{the quadrature component}@}, resulting in {@{$\sqrt{M}\times\sqrt{M}$ equally spaced points}@}. This arrangement {@{maximizes Euclidean distance between adjacent symbols}@} while {@{keeping the average power bounded}@}.

## comparison with M-PSK

In practice, {@{16-QAM}@} is {@{more popular than 16-PSK}@}. Both uses {@{sixteen symbols}@}, but QAM distributes {@{points on a rectangular grid}@}, allowing {@{the constellation}@} to be {@{expanded along both amplitude axes}@}. {@{This layout}@} achieves {@{higher spectral efficiency for a given minimum distance requirement}@} because it can maintain {@{larger symbol separations at lower energy per bit}@} than PSK, whose points are {@{confined to a circle}@} and must be {@{packed more tightly in phase}@}. As a result, 16-QAM delivers {@{superior error performance at moderate SNRs}@} and is therefore {@{the preferred choice for many high-rate communication systems}@}.
