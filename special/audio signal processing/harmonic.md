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

A __harmonic__ is {@{a sinusoidal wave with a frequency that is a positive integer multiple of the fundamental frequency $f_0$ of a periodic signal}@}. <!--SR:!2029-07-30,1158,350-->

## harmonic model

A harmonic model is {@{very similar to a [sinusoidal model](sinusoidal%20model.md)}@}, additionally {@{requiring the sinusoidal frequencies to be positive integer multiples of the fundamental frequency $f_0$}@}. {@{The fundamental frequency}@} is often {@{the lowest frequency}@}, and is known as {@{the _pitch_}@} of an instrument. <!--SR:!fsrs,2029-11-18T00:00:00.000Z,1233,1233.04800529,1,2,9,0,0,2026-07-04T00:00:00.000Z!2029-07-18,1146,350!fsrs,2029-11-28T00:00:00.000Z,1241,1240.62340626,1,2,9,0,0,2026-07-06T00:00:00.000Z!2029-06-11,1121,350!2029-08-08,1167,350-->

{@{Not all instruments}@} produce timbre that can be modeled by a harmonic model, i.e. {@{their partials are not all integer multiples of its fundamental frequency}@}. <!--SR:!2026-07-13,293,330!2029-07-15,1143,350-->

When {@{there are only one instrument}@}, the sound source is called {@{"monophonic"}@}. When {@{there are multiple instruments}@}, the sound source is called {@{"polyphonic"}@}. It is easy to identify {@{the fundamental frequency}@} when the source is monophonic, since {@{there is only one fundamental frequency}@}. It is more difficult to do so when {@{the source is polyphonic}@}, since {@{there are multiple fundamental frequencies}@}. <!--SR:!2029-05-19,1103,350!2029-08-25,1181,350!2026-07-09,289,330!fsrs,2029-12-02T00:00:00.000Z,1244,1244.40857912,1,2,9,0,0,2026-07-07T00:00:00.000Z!2029-07-23,1151,350!2026-07-14,294,330!2026-07-11,291,330!2026-07-08,288,330-->

To detect {@{a partial across frames}@} \(e.g. in STFT\), we additionally require {@{the frequency of the detected peaks to be an integer multiple of the fundamental frequency}@} up to {@{some small tolerance}@}. <!--SR:!2026-07-08,288,330!2028-05-24,796,330!2027-04-19,459,384-->

## terminology

Harmonics may be called {@{"overtones", "partials", or "upper partials"}@}, and in {@{some music contexts}@}, {@{the terms "harmonic", "overtone" and "partial"}@} are {@{used fairly interchangeably}@}. But more precisely, {@{the term "harmonic"}@} includes {@{_all_ pitches in a harmonic series \(including the fundamental frequency\)}@} while {@{the term "overtone"}@} only includes {@{pitches _above_ the fundamental}@}. <!--SR:!2029-08-26,1182,350!fsrs,2029-11-23T00:00:00.000Z,1237,1236.83645167,1,2,9,0,0,2026-07-05T00:00:00.000Z!2026-07-07,287,330!2026-07-10,290,330!2026-07-12,292,330!2029-06-10,1121,350!fsrs,2029-12-02T00:00:00.000Z,1244,1244.40857912,1,2,9,0,0,2026-07-07T00:00:00.000Z!2029-06-24,1122,350-->
