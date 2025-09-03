---
aliases:
  - harmonic
  - harmonics
tags:
  - flashcard/active/special/audio_signal_processing/harmonic
  - language/in/English
---

# harmonic

- see: [general/harmonic](../../general/harmonic.md)

A __harmonic__ is {@{a sinusoidal wave with a frequency that is a positive integer multiple of the fundamental frequency $f_0$ of a periodic signal}@}. <!--SR:!2025-09-14,58,310-->

## harmonic model

A harmonic model is {@{very similar to a [sinusoidal model](sinusoidal%20model.md)}@}, additionally {@{requiring the sinusoidal frequencies to be positive integer multiples of the fundamental frequency $f_0$}@}. {@{The fundamental frequency}@} is often {@{the lowest frequency}@}, and is known as {@{the _pitch_}@} of an instrument. <!--SR:!2025-09-23,67,310!2025-09-14,58,310!2025-09-23,67,310!2025-09-13,57,310!2025-09-14,58,310-->

{@{Not all instruments}@} produce timbre that can be modeled by a harmonic model, i.e. {@{their partials are not all integer multiples of its fundamental frequency}@}. <!--SR:!2025-09-23,67,310!2025-09-13,57,310-->

When {@{there are only one instrument}@}, the sound source is called {@{"monophonic"}@}. When {@{there are multiple instruments}@}, the sound source is called {@{"polyphonic"}@}. It is easy to identify {@{the fundamental frequency}@} when the source is monophonic, since {@{there is only one fundamental frequency}@}. It is more difficult to do so when {@{the source is polyphonic}@}, since {@{there are multiple fundamental frequencies}@}. <!--SR:!2026-05-12,242,330!2025-09-15,59,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-14,58,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-23,67,310-->

To detect {@{a partial across frames}@} \(e.g. in STFT\), we additionally require {@{the frequency of the detected peaks to be an integer multiple of the fundamental frequency \(up to some small tolerance\)}@}. <!--SR:!2025-09-23,67,310!2025-09-15,59,310-->

## terminology

Harmonics may be called {@{"overtones", "partials", or "upper partials"}@}, and in {@{some music contexts}@}, {@{the terms "harmonic", "overtone" and "partial"}@} are {@{used fairly interchangeably}@}. But more precisely, {@{the term "harmonic"}@} includes {@{_all_ pitches in a harmonic series \(including the fundamental frequency\)}@} while {@{the term "overtone"}@} only includes {@{pitches _above_ the fundamental}@}. <!--SR:!2025-09-15,59,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-23,67,310!2026-05-16,246,330!2025-09-23,67,310!2025-09-13,57,310-->
