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

After {@{analyzing a sound using models}@}, we can {@{modify model data and parameters}@} before {@{re-synthesizing the sound using the model}@}. This can {@{create __sound effects__}@}. <!--SR:!2026-07-09,289,330!2029-06-30,1128,350!2029-07-04,1132,350!2029-03-10,1046,350-->

## frequency filter

{@{A _frequency filter_}@} is {@{a function in the frequency domain}@}. After {@{transforming a sound into frequency domain}@}, we simply {@{element-wise multiply with the filter}@}. Equivalently, {@{their magnitudes are multiplied together}@} and {@{their phases are added together}@}. The effect of the filter in the time domain is to {@{convolute the time signal with the impulse response \(IDFT\) of the filter}@}. <!--SR:!2029-07-26,1154,350!2026-07-14,294,330!fsrs,2029-10-01T00:00:00.000Z,1199,1198.87680538,1,2,9,0,0,2026-06-20T00:00:00.000Z!fsrs,2029-11-28T00:00:00.000Z,1241,1240.62340626,1,2,9,0,0,2026-07-06T00:00:00.000Z!2026-07-10,290,330!2029-07-13,1141,350!2029-02-24,1032,350-->

### equalization

{@{_Equalization_}@} is {@{simply a frequency filter that does not modify phase}@}, i.e. {@{it consists of real numbers in the frequency domain}@}. Common special cases include {@{band pass filters, which pass through a certain range of frequencies and disallow others}@}. The band pass filter is {@{often a window function \(i.e. not boxcar\) to minimize distortion}@}. <!--SR:!2026-07-13,293,330!fsrs,2029-08-05T06:11:12.888Z,1156,1155.51731222,1,2,9,0,0,2026-06-06T06:11:12.888Z!fsrs,2029-12-07T00:00:00.000Z,1248,1248.19227538,1,2,9,0,0,2026-07-08T00:00:00.000Z!2029-04-11,1074,350!2029-07-05,1133,350-->

## morphing

{@{_Morphing_}@} uses {@{the DFT magnitude of another sound \(but not its phase\) as a frequency filter}@}. Often, {@{the DFT magnitude is smoothened}@} first. The effect is that {@{the resulting sound is similar to the input sound but with characteristics of the other sound used to derive the filter}@}. Note that the magnitude mainly determines {@{the "content" while the phase mainly determines the "feeling"}@}. <!--SR:!2026-07-10,290,330!2029-04-14,1076,350!2026-07-11,291,330!2026-07-12,292,330!2029-08-20,1176,350-->

{@{_Morphing_}@} may also refer to {@{analyzing two sounds with the same model\(s\)}@}, and then {@{interpolate the model data and/or parameters between the resulting two models}@}, and finally {@{re-synthesizing the sound}@}. Often, an {@{interpolation function \(taking time as input and outputting a value between 0 and 1\)}@} is used to {@{control how much of one sound is mixed compared to the other over time}@}. The sounds may be {@{smoothened}@} first. <!--SR:!2029-04-24,1078,350!fsrs,2029-08-06T06:11:12.061Z,1157,1156.92457827,1,2,9,0,0,2026-06-06T06:11:12.061Z!2026-07-11,291,330!2029-05-06,1090,350!2029-04-02,1066,350!2026-07-11,291,330!2029-04-30,1084,350-->

## sinusoidal spectral modeling

Using {@{a sinusoidal model to analyze a sound}@}, we obtain {@{the frequencies, amplitudes, and \(initial\) phases of each sinusoid in each STFT frame}@}. Common effects include {@{amplitude scaling, pitch scaling, and time stretching}@}. If {@{a residual model is used in combination}@}, often {@{no effects or only frequency transformations are applied \(time stretching is difficult to apply\)}@}. If {@{a stochastic model used in combination}@}, it is {@{often transformed by the same effect or a different simpler effect \(e.g. only amplitude scaling\)}@}. <!--SR:!2029-08-24,1180,350!2026-07-14,294,330!fsrs,2029-10-06T00:00:00.000Z,1203,1202.68030072,1,2,9,0,0,2026-06-21T00:00:00.000Z!2029-03-15,1051,350!2029-09-07,1191,350!2029-04-08,1072,350!2029-05-28,1109,350-->

### amplitude scaling \(sinusoidal\)

{@{_Amplitude scaling_}@} is done by {@{simply multiplying \(or adding if in logarithmic scale, e.g. dB\) the amplitude}@} by {@{a factor \(or as a function of time\)}@} for {@{each STFT frame}@}. <!--SR:!2029-02-28,1036,350!2027-11-02,596,330!2028-01-20,683,409!2027-11-12,626,409-->

### pitch scaling \(sinusoidal\)

{@{_Pitch scaling_}@} is done by {@{first multiplying the frequencies by a factor \(or as a function of time\) across all STFT frame}@}. Then {@{the \(initial\) phases of each sinusoid needs to be re-generated}@} to {@{maintain phase coherence between \(overlapping\) STFT frames}@}. This is done by, for {@{each frequency}@}, {@{start with a zero or random initial phase for the first frame}@}, and then {@{offset the initial phase based on the previous frame for each next frame}@}. This {@{offset \(in radian\)}@} is {@{_angular_ frequency times the STFT duration}@}. This also {@{unwraps the phase automagically}@}. <!--SR:!2026-07-12,292,330!2029-07-15,1143,350!fsrs,2029-09-05T09:57:31.874Z,1179,1179.41935434,1,2,9,0,0,2026-06-14T09:57:31.874Z!fsrs,2029-09-03T09:57:35.268Z,1177,1176.58438079,1,2,9,0,0,2026-06-14T09:57:35.268Z!2026-07-13,293,330!fsrs,2029-09-26T00:00:00.000Z,1195,1195.07164214,1,2,9,0,0,2026-06-19T00:00:00.000Z!2029-05-17,1101,350!2029-06-11,1122,350!2029-05-21,1104,350!fsrs,2029-11-23T00:00:00.000Z,1237,1236.83645167,1,2,9,0,0,2026-07-05T00:00:00.000Z-->

### time stretching \(sinusoidal\)

{@{_Time stretching_}@} is done by {@{multiplying the time indices to amplitudes and frequencies by a factor \(or use a time scaling envelope that maps old time to new time\) across all STFT frame}@}. Then {@{the \(initial\) phases of each sinusoid needs to be re-generated}@} to {@{maintain phase coherence between \(overlapping\) STFT frames}@}. This is done by, for {@{each frequency}@}, {@{start with a zero or random initial phase for the first frame}@}, and then {@{offset the initial phase based on the previous frame for each next frame}@}. This {@{offset \(in radian\)}@} is {@{_angular_ frequency times the STFT duration or 2 pi times _cycle frequency_ times the \(fractional\) frequency bin index}@}. This also {@{unwraps the phase automagically}@}. <!--SR:!2029-07-08,1136,350!2029-08-09,1168,350!2029-05-07,1091,350!2029-05-02,1086,350!2029-02-26,1034,350!2029-08-23,1179,350!2029-05-01,1085,350!2029-07-11,1139,350!fsrs,2029-08-30T09:57:34.319Z,1173,1172.77084718,1,2,9,0,0,2026-06-14T09:57:34.319Z!2029-04-17,1079,350-->

## harmonic spectral modelling

Using {@{a harmonic model to analyze a sound}@}, we obtain {@{the frequencies, amplitudes, harmonics, and \(initial\) phases of each sinusoid in each STFT frame}@}. Common effects include {@{amplitude scaling, pitch scaling, and time stretching}@}. They are quite similar to {@{that for sinusoidal models}@}. If {@{a residual model is used in combination}@}, often {@{no effects or only frequency transformations are applied \(time stretching is difficult to apply\)}@}. If {@{a stochastic model used in combination}@}, it is {@{often transformed by the same effect or a different simpler effect \(e.g. only amplitude scaling\)}@}. <!--SR:!2029-03-21,1056,350!2026-07-10,290,330!2026-07-14,294,330!fsrs,2029-12-02T00:00:00.000Z,1244,1244.40857912,1,2,9,0,0,2026-07-07T00:00:00.000Z!2029-05-14,1098,350!fsrs,2029-09-04T09:57:36.093Z,1178,1178.00364035,1,2,9,0,0,2026-06-14T09:57:36.093Z!fsrs,2029-09-04T09:57:32.748Z,1178,1178.42810815,1,2,9,0,0,2026-06-14T09:57:32.748Z!2029-04-01,1065,350-->

### pitch scaling \(harmonic\)

There are {@{3 commons ways to scale pitch}@}: {@{_transposition_, _shifting_, and _stretching_}@}. The first one {@{simply multiplies the frequencies}@}, which {@{preserves harmonics}@}. The second one {@{simply adds to the frequencies}@}, which {@{does not preserve harmonics}@}. The third one {@{scales the frequencies by $h^{s - 1}$, where $h$ is the harmonic number and $s$ is the scaling factor}@}, which {@{also does not preserve harmonics but rather stretches them}@}. <!--SR:!2026-07-14,294,330!2026-07-12,292,330!fsrs,2029-12-07T00:00:00.000Z,1248,1248.19227538,1,2,9,0,0,2026-07-08T00:00:00.000Z!2029-05-13,1097,350!2029-05-29,1111,350!2026-07-13,293,330!2029-07-19,1147,350!2026-07-08,288,330-->
