---
aliases:
  - ELEC 4110 M-FSK
  - ELEC4110 M-FSK
  - M-FSK
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/M-FSK
  - language/in/English
---

# _M_-FSK

- see: [general/multiple frequency-shift keying](../../../../general/multiple%20frequency-shift%20keying.md)

{@{_Frequency shift keying_ (M-FSK)}@} assigns {@{$\log_2M$ bits to one of $M$ distinct orthogonal carrier frequencies}@}. {@{Each symbol}@} is represented by {@{a single tone at a different frequency}@}, which makes FSK {@{inherently robust against amplitude fading and nonlinearities}@}—an advantage in {@{power-limited or highly distorted channels}@}. However, {@{the required bandwidth}@} expands {@{linearly with $M$}@}, as {@{each additional frequency}@} must be {@{accommodated within the channel spectrum}@}.

## waveforms

{@{The transmitted waveform corresponding to symbol index $m = 0, \ldots, M - 1$}@} is {@{a single tone at one of $M$ distinct frequencies}@}: {@{$$s_m(t)=A\,\cos \!\bigl(2\pi(f_c+\Delta f_m)t\bigr), \qquad 0\le t<T_s \,,$$}@} where {@{$\Delta f_m$ denotes the frequency offset for symbol $m$}@}. {@{The offsets are chosen}@} such that {@{the tones are orthogonal over the interval $T_s$}@} (e.g., {@{$\Delta f_m=m\,\Delta f_{\min}$ where $\Delta f_{\min} = 1 / T_s$}@}). Again, {@{setting $A=\sqrt{2E/T_s}$}@} gives {@{each tone an average energy $E$}@}.

## constellation

{@{The constellation for $M$-ary FSK}@} is {@{a set of $M$ distinct tones}@}, each represented by {@{a point at a different frequency}@} (or equivalently, {@{the unit vectors in the $M$-dimensional constellation}@}).
