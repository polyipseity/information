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

A __harmonic__ is {@{a sinusoidal wave with a frequency that is a positive integer multiple of the fundamental frequency $f_0$ of a periodic signal}@}. <!--SR:!2026-05-26,254,330-->

## harmonic model

A harmonic model is {@{very similar to a [sinusoidal model](sinusoidal%20model.md)}@}, additionally {@{requiring the sinusoidal frequencies to be positive integer multiples of the fundamental frequency $f_0$}@}. {@{The fundamental frequency}@} is often {@{the lowest frequency}@}, and is known as {@{the _pitch_}@} of an instrument. <!--SR:!2026-07-03,283,330!2026-05-24,252,330!2026-07-05,285,330!2026-05-17,246,330!2026-05-27,255,330-->

{@{Not all instruments}@} produce timbre that can be modeled by a harmonic model, i.e. {@{their partials are not all integer multiples of its fundamental frequency}@}. <!--SR:!2026-07-13,293,330!2026-05-22,251,330-->

When {@{there are only one instrument}@}, the sound source is called {@{"monophonic"}@}. When {@{there are multiple instruments}@}, the sound source is called {@{"polyphonic"}@}. It is easy to identify {@{the fundamental frequency}@} when the source is monophonic, since {@{there is only one fundamental frequency}@}. It is more difficult to do so when {@{the source is polyphonic}@}, since {@{there are multiple fundamental frequencies}@}. <!--SR:!2026-05-12,242,330!2026-05-31,258,330!2026-07-09,289,330!2026-07-06,286,330!2026-05-25,253,330!2026-07-14,294,330!2026-07-11,291,330!2026-07-08,288,330-->

To detect {@{a partial across frames}@} \(e.g. in STFT\), we additionally require {@{the frequency of the detected peaks to be an integer multiple of the fundamental frequency}@} up to {@{some small tolerance}@}. <!--SR:!2026-07-08,288,330!2026-03-20,186,310!2026-01-07,92,364-->

## terminology

Harmonics may be called {@{"overtones", "partials", or "upper partials"}@}, and in {@{some music contexts}@}, {@{the terms "harmonic", "overtone" and "partial"}@} are {@{used fairly interchangeably}@}. But more precisely, {@{the term "harmonic"}@} includes {@{_all_ pitches in a harmonic series \(including the fundamental frequency\)}@} while {@{the term "overtone"}@} only includes {@{pitches _above_ the fundamental}@}. <!--SR:!2026-06-01,259,330!2026-07-04,284,330!2026-07-07,287,330!2026-07-10,290,330!2026-07-12,292,330!2026-05-16,246,330!2026-07-06,286,330!2026-05-18,247,330-->
