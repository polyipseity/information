---
aliases:
  - sound effect
  - sound effects
tags:
  - flashcard/active/special/audio_signal_processing/sound_effect
  - language/in/English
---

# sound effect

- see: [general/sound effect](../../general/sound%20effect.md)

After {@{analyzing a sound using models}@}, we can {@{modify model data and parameters}@} before {@{re-synthesizing the sound using the model}@}. This can {@{create __sound effects__}@}. <!--SR:!2025-09-23,67,310!2025-09-13,57,310!2025-09-13,57,310!2026-04-28,230,330-->

## frequency filter

{@{A _frequency filter_}@} is {@{a function in the frequency domain}@}. After {@{transforming a sound into frequency domain}@}, we simply {@{element-wise multiply with the filter}@}. Equivalently, {@{their magnitudes are multiplied together}@} and {@{their phases are added together}@}. The effect of the filter in the time domain is to {@{convolute the time signal with the impulse response \(IDFT\) of the filter}@}. <!--SR:!2025-09-14,58,310!2025-09-23,67,310!2025-09-19,63,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-14,58,310!2026-04-25,227,330-->

### equalization

{@{_Equalization_}@} is {@{simply a frequency filter that does not modify phase}@}, i.e. {@{it consists of real numbers in the frequency domain}@}. Common special cases include {@{band pass filters, which pass through a certain range of frequencies and disallow others}@}. The band pass filter is {@{often a window function \(i.e. not boxcar\) to minimize distortion}@}. <!--SR:!2025-09-23,67,310!2025-09-16,60,310!2025-09-23,67,310!2026-05-03,235,330!2025-09-13,57,310-->

## morphing

{@{_Morphing_}@} uses {@{the DFT magnitude of another sound \(but not its phase\) as a frequency filter}@}. Often, {@{the DFT magnitude is smoothened}@} first. The effect is that {@{the resulting sound is similar to the input sound but with characteristics of the other sound used to derive the filter}@}. Note that the magnitude mainly determines {@{the "content" while the phase mainly determines the "feeling"}@}. <!--SR:!2025-09-23,67,310!2026-05-04,235,330!2025-09-23,67,310!2025-09-23,67,310!2025-09-15,59,310-->

{@{_Morphing_}@} may also refer to {@{analyzing two sounds with the same model\(s\)}@}, and then {@{interpolate the model data and/or parameters between the resulting two models}@}, and finally {@{re-synthesizing the sound}@}. Often, an {@{interpolation function \(taking time as input and outputting a value between 0 and 1\)}@} is used to {@{control how much of one sound is mixed compared to the other over time}@}. The sounds may be {@{smoothened}@} first. <!--SR:!2026-05-05,236,330!2025-09-16,60,310!2025-09-23,67,310!2026-05-07,238,330!2026-05-02,234,330!2025-09-23,67,310!2026-05-06,237,330-->

## sinusoidal spectral modeling

Using {@{a sinusoidal model to analyze a sound}@}, we obtain {@{the frequencies, amplitudes, and \(initial\) phases of each sinusoid in each STFT frame}@}. Common effects include {@{amplitude scaling, pitch scaling, and time stretching}@}. If {@{a residual model is used in combination}@}, often {@{no effects or only frequency transformations are applied \(time stretching is difficult to apply\)}@}. If {@{a stochastic model used in combination}@}, it is {@{often transformed by the same effect or a different simpler effect \(e.g. only amplitude scaling\)}@}. <!--SR:!2025-09-15,59,310!2025-09-23,67,310!2025-09-19,63,310!2026-04-29,231,330!2025-09-16,60,310!2026-05-02,234,330!2026-05-15,245,330-->

### amplitude scaling \(sinusoidal\)

{@{_Amplitude scaling_}@} is done by {@{simply multiplying \(or adding if in logarithmic scale, e.g. dB\) the amplitude by a function \(or use a amplitude scaling envelope that maps old amplitudes to new amplitudes\) for each STFT frame}@}. <!--SR:!2026-04-27,229,330!2025-09-23,67,310-->

### pitch scaling \(sinusoidal\)

{@{_Pitch scaling_}@} is done by {@{first multiplying the frequencies by a factor \(or use a frequency scaling envelope that maps old frequencies to new frequencies\) across all STFT frame}@}. Then {@{the \(initial\) phases of each sinusoid needs to be re-generated}@} to {@{maintain phase coherence between \(overlapping\) STFT frames}@}. This is done by, for {@{each frequency}@}, {@{start with a zero or random initial phase for the first frame}@}, and then {@{offset the initial phase based on the previous frame for each next frame}@}. This {@{offset \(in radian\)}@} is {@{_angular_ frequency times the STFT duration}@}. This also {@{unwraps the phase automagically}@}. <!--SR:!2025-09-23,67,310!2025-09-13,57,310!2025-09-17,61,310!2025-09-17,61,310!2025-09-23,67,310!2025-09-19,63,310!2026-05-12,242,330!2026-05-16,246,330!2026-05-13,243,330!2025-09-23,67,310-->

### time stretching \(sinusoidal\)

{@{_Time stretching_}@} is done by {@{multiplying the time indices to amplitudes and frequencies by a factor \(or use a time scaling envelope that maps old time to new time\) across all STFT frame}@}. Then {@{the \(initial\) phases of each sinusoid needs to be re-generated}@} to {@{maintain phase coherence between \(overlapping\) STFT frames}@}. This is done by, for {@{each frequency}@}, {@{start with a zero or random initial phase for the first frame}@}, and then {@{offset the initial phase based on the previous frame for each next frame}@}. This {@{offset \(in radian\)}@} is {@{_angular_ frequency times the STFT duration or 2 pi times _cycle frequency_ times the \(fractional\) frequency bin index}@}. This also {@{unwraps the phase automagically}@}. <!--SR:!2025-09-13,57,310!2025-09-15,59,310!2026-05-08,239,330!2026-05-07,238,330!2026-04-26,228,330!2025-09-15,59,310!2026-05-05,237,330!2025-09-13,57,310!2025-09-18,62,310!2026-05-04,236,330-->

## harmonic spectral modelling

Using {@{a harmonic model to analyze a sound}@}, we obtain {@{the frequencies, amplitudes, harmonics, and \(initial\) phases of each sinusoid in each STFT frame}@}. Common effects include {@{amplitude scaling, pitch scaling, and time stretching}@}. They are quite similar to {@{that for sinusoidal models}@}. If {@{a residual model is used in combination}@}, often {@{no effects or only frequency transformations are applied \(time stretching is difficult to apply\)}@}. If {@{a stochastic model used in combination}@}, it is {@{often transformed by the same effect or a different simpler effect \(e.g. only amplitude scaling\)}@}. <!--SR:!2026-04-30,232,330!2025-09-23,67,310!2025-09-23,67,310!2025-09-23,67,310!2026-05-09,240,330!2025-09-17,61,310!2025-09-18,62,310!2026-05-01,233,330-->

### pitch scaling \(harmonic\)

There are {@{3 commons ways to scale pitch}@}: {@{_transposition_, _shifting_, and _stretching_}@}. The first one {@{simply multiplies the frequencies}@}, which {@{preserves harmonics}@}. The second one {@{simply adds to the frequencies}@}, which {@{does not preserve harmonics}@}. The third one {@{scales the frequencies by $h^{s - 1}$, where $h$ is the harmonic number and $s$ is the scaling factor}@}, which {@{also does not preserve harmonics but rather stretches them}@}. <!--SR:!2025-09-23,67,310!2025-09-23,67,310!2025-09-23,67,310!2026-05-10,241,330!2026-05-14,244,330!2025-09-23,67,310!2025-09-14,58,310!2025-09-23,67,310-->
