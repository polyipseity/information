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

For {@{an $M$-ary PSK system}@} {@{the transmitted waveform corresponding to symbol index $m\in\{0,\dots ,M-1\}$}@} is {@{$$s_m(t)=A\,\cos \!\bigl(2\pi f_c t+\varphi_m\bigr),\qquad 0\le t<T_s \,,$$}@} where {@{$f_c$ is the carrier frequency, $T_s$ is the symbol duration}@}, and {@{$\varphi_m=\frac{2\pi m}{M}\;.$}@} {@{The constant amplitude $A=\sqrt{\dfrac{2E}{T_s} }$}@} guarantees that {@{each symbol has the same average energy $E$}@}.

## constellation

{@{The $M$-ary PSK constellation}@} consists of {@{$M$ equally spaced points lying on the circumference of a unit circle in the signal space}@}. {@{Each point}@} corresponds to {@{one symbol}@} and is distinguished {@{solely by its phase angle}@}; {@{all symbols}@} have {@{identical amplitude}@}, which yields {@{a regular polygon shape when plotted with orthogonal basis functions}@}.

## special cases

{@{_Binary PSK_ \(BPSK\), _quadrature PSK_ \(QPSK\), and _8-PSK_}@} are {@{the most common special cases}@}: {@{BPSK}@} uses {@{two antipodal points ($M=2$)}@} and conveys {@{one bit per symbol}@}; {@{QPSK}@} employs {@{four points arranged in a square grid ($M=4$)}@}, delivering {@{two bits per symbol}@}; {@{8-PSK}@} uses {@{eight equally spaced points on the unit circle}@} and conveys {@{three bits per symbol}@}. All preserve {@{the fixed-tone bandwidth characteristic}@} of PSK systems; {@{only two orthogonal carrier tones \(in-phase and quadrature components\)}@} is {@{used regardless of the modulation order $M$}@}.

Under {@{equal symbol energies and two-dimensional signal space}@}, {@{QSK is optimal for quartic modulation}@} as {@{any alternative quartic scheme}@} must {@{also use four symbols}@}; {@{the only way to improve performance}@} would be to {@{increase minimum Euclidean distance}@}, which is {@{already maximal for QPSK}@}.
