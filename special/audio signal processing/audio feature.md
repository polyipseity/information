---
aliases:
  - audio feature
  - audio features
tags:
  - flashcard/active/special/audio_signal_processing/audio_feature
  - language/in/English
---

# audio feature

An {@{__audio feature__}@} captures {@{specific aspects of audio signals}@}. They are usually obtained by {@{_feature analysis_ in the frequency domain \(after DFT or STFT\)}@}. <!--SR:!2026-06-28,281,330!2029-06-02,1114,350!2028-07-04,828,330-->

## descriptors

They are {@{many different descriptors}@}. They can be mostly categorized into {@{spectral, time-domain, tonal}@}, {@{rhythm, SFX, and high-level descriptors}@} \(this is used by {@{[Essentia](https://essentia.upf.edu/)}@}\). <!--SR:!2026-07-02,283,330!2028-03-31,754,330!2029-07-21,1149,350!2027-06-20,520,400-->

## spectral features

In a {@{STFT frame}@}, we can describe {@{many different spectral features}@}. We can also {@{describe spectral features across frames}@}. <!--SR:!2026-07-07,288,330!2026-07-02,283,330!2026-06-16,271,330-->

### energy

There are many ways to {@{measure "energy" and/or loudness of a STFT frame}@}. {@{_Energy_}@} describes {@{the total "energy" in an audio or STFT frame}@} and is defined as {@{$$E = \sum_{k = 0}^{N - 1} \lvert X[k] \rvert^2 \,.$$}@} Its {@{_root mean square_}@} describes {@{the average "energy" per frequency bin}@} and is defined as {@{$$E_{\text{rms} } = \sqrt{\frac 1 N \sum_{k = 0}^{N - 1} \lvert X[k] \rvert^2 } \,.$$}@} {@{_Steven's power law_}@} describes {@{an empirical relationship in psychophysics between an increased intensity or strength in a physical stimulus and the perceived magnitude increase in the sensation created by the stimulus}@}, and for audio, is defined as {@{$$L = E^{0.67} \,,$$ where $L$ is _loudness_}@}. <!--SR:!2029-05-01,1089,350!2029-02-26,1030,350!fsrs,2029-09-07T13:29:12.301Z,1181,1180.83166378,1,2,9,0,0,2026-06-14T13:29:12.301Z!fsrs,2029-09-04T13:29:11.158Z,1178,1178.42810815,1,2,9,0,0,2026-06-14T13:29:11.158Z!2026-06-26,279,330!2026-06-22,276,330!2028-09-04,866,330!2029-07-25,1153,350!2026-07-14,294,330!2026-07-14,294,330-->

There are also many ways to {@{characterize a spectrogram of a STFT frame}@}. {@{_Spectral centroid_}@} describes {@{the center of a spectrogram}@} and is defined as {@{$$C = \frac {\sum_{k = 0}^{N / 2} k \lvert X[k] \rvert } {\sum_{k = 0}^{N / 2} \lvert X[k] \rvert } \,,$$}@} i.e. its {@{weighted average frequency \(bin\) weighted by magnitude or _center of mass_}@}. Note {@{only the _nonnegative_ frequency bins \(from 0 to $N / 2$; both ends inclusive\) are used}@} since {@{for a real signal, the magnitude of a frequency equals that of its negative frequency \(conjugate-even\)}@}; including them {@{would always result in a centroid at the zero frequency bin, which is not useful}@}. <!--SR:!2029-07-20,1148,350!2029-05-02,1090,350!2029-07-17,1145,350!2026-06-17,272,330!2029-08-04,1163,350!2026-07-09,290,330!2026-06-29,281,330!2026-06-24,277,330-->

### mel-frequency

In a {@{normal \(linear\) power spectrum}@}, frequency bands are {@{not evenly spaced}@}. The {@{_mel scale_}@} takes {@{the logarithm to make the bands evenly spaced}@}. Its equation is: {@{$$m = 2595 \log_{10} \left(1 + \frac f {700} \right) \,.$$}@} A linear power spectrum can be {@{converted into _mel-frequency cepstrum_ \(MFC\) using the above formula}@}, but we need to {@{adjust the magnitudes, since the scale changes}@}. This is usually done with {@{a frequency filter using triangular or cosine overlapping windows}@}. We can further obtain the {@{_mel-frequency cepstrum coefficients_ \(MFCC\)}@} using the following equation: {@{$$\operatorname{MFCC} = \operatorname{DCT}\left(\log_{10} X^{\ge 0}[k] \right) \,,$$}@} where {@{$X^{\ge 0}[k]$ is the _mel-frequency_ cepstrum of _nonnegative_ frequency \(from 0 to $N / 2$, both ends inclusive\) and $\operatorname{DCT}$ is _discrete cosine transform_}@}. {@{The most commonly used DCT definition, _DCT-II_}@} is: {@{$$\operatorname{DCT-II}[k] = \sum_{n = 0}^{N - 1} x[n] \cos\left(\frac {\pi k} N \left(n + \frac 1 2 \right) \right) \,.$$}@} <!--SR:!2026-06-22,276,330!2026-07-14,294,330!2029-05-20,1104,350!2029-05-05,1091,350!2028-06-18,815,330!2026-06-28,280,330!2029-05-23,1106,350!2028-09-06,868,330!2029-04-10,1073,350!2028-06-16,815,330!2029-04-25,1083,350!2029-08-21,1175,350!2027-11-05,588,310-->

### pitches

We can also {@{describe pitches in a STFT frame}@}. {@{A complex measure implemented in Essentia}@} is {@{_pitch salience_}@}. It first detects {@{the spectral peaks in a STFT frame}@}. Then it measure {@{the salience at bin frequency $b$ \(in _cent scale_\)}@} by: {@{$$S[b] = \sum_{h = 1}^H \sum_{p = 1}^P e(A_p) w(b, h, f_p) (A_p)^\beta \,,$$}@} where $h$ {@{represents harmonics, $p$ represents peaks}@}, $e(A_p)$ is {@{a threshold function \(0 below a certain threshold, otherwise 1\), and $w(b, h, f_p)$ is a complicated function weighing the spectral peaks}@}. Its motivation is that {@{a polyphonic sound source has many instruments playing at different pitches}@}. It aims to measure {@{how prominent each pitch is}@}. <!--SR:!2029-05-15,1101,350!2029-08-25,1179,350!2029-09-02,1187,350!2029-09-05,1189,350!2026-06-24,277,330!2026-07-08,289,330!2028-05-30,801,330!2029-08-13,1172,350!2029-04-04,1067,350!2026-09-06,114,390-->

Another measure is {@{_harmonic pitch class profile_ or simply _chroma_ \(a musical concept\)}@}. It divides {@{the octave into 12 semitone \(or any other frequency division\)}@}. Each semitone {@{over all possible octaves forms a _pitch class_, which has the same _chroma_}@}. Then, it finds {@{how prominent each pitch class is, thus describing tonality}@}. An example implementation is: {@{$$\operatorname{HPCP}[k] = \sum_{p = 1}^P w(k, f_p) A_p^2 \,,$$ where $p$ represents peaks and $w(k, f_p)$ is a weighing function}@}. <!--SR:!2026-06-29,280,330!2026-07-09,290,330!2029-03-20,1052,350!fsrs,2029-09-06T13:29:03.505Z,1180,1179.83367202,1,2,9,0,0,2026-06-14T13:29:03.505Z!2029-03-25,1057,350-->

After {@{measuring the pitch salience}@}, we can {@{create _pitch contours_}@}. We can further {@{perform _melody selection_}@} to {@{find the fundamental frequency sequence of a melody}@}. Commonly, we choose {@{the _prominent_ melody}@}. <!--SR:!2026-07-01,282,330!2026-06-26,279,330!fsrs,2029-09-07T13:28:46.199Z,1181,1180.83166378,1,2,9,0,0,2026-06-14T13:28:46.199Z!2026-07-14,294,330!2026-06-22,276,330-->

### multiple frames

{@{Features across frames}@} can be used for {@{detecting event onsets or segmenting events}@}. <!--SR:!2026-07-14,294,330!2026-06-16,271,330-->

A measure used to {@{segment events \(based on event onsets\)}@} is {@{_spectral flux_}@}, defined as: {@{$$\operatorname{SF}[l] = \sum_{k = 0}^{N / 2} \max\set{0, \lvert X[l, k] \rvert - \lvert X[l - 1, k] \rvert}$$}@} where {@{$l$ is the frame number}@}. It can be interpreted as {@{how much the total spectrum magnitude increases \(detects onset\), ignoring the decreases \(ignores offsets\)}@}. Whenever {@{this value exceeds a certain threshold}@}, we can say {@{a new event starts}@}, so we {@{segment the audio starting from this frame}@}. Another method is based on {@{_high-frequency content_ \(HFC\)}@}, defined as: {@{$$\operatorname{HFC}[l] = \sum_{k = 0}^{N / 2} k^2 \lvert X[l, k] \rvert \,,$$}@} which {@{weighs high-frequency magnitudes much more than low-frequency ones}@} due to {@{the factor $k^2$}@}. Then onset is detected by {@{finding the HFC difference for each two consecutive frames}@}, and then {@{say a new event starts when this difference is higher than a \(positive\) threshold}@}. The main difference between these two method is {@{the former weighs all frequencies evenly while the latter weighs high frequencies much more}@}, and which one is better {@{depends on the use case}@}. <!--SR:!2029-07-07,1135,350!2026-07-14,294,330!2029-08-26,1180,350!2029-07-10,1138,350!fsrs,2029-09-03T13:30:02.465Z,1177,1177.01902368,1,2,9,0,0,2026-06-14T13:30:02.465Z!2029-07-02,1130,350!2026-06-27,280,330!2026-07-14,294,330!2029-04-30,1088,350!2029-04-24,1082,350!2029-05-06,1092,350!2026-06-25,278,330!fsrs,2029-08-09T08:21:38.602Z,1159,1159.34014939,1,2,9,0,0,2026-06-07T08:21:38.602Z!2029-04-15,1077,350!2029-05-21,1104,350!2029-03-05,1037,350-->

## statistics

{@{Some basic statistics}@} are {@{applicable to many areas and provide reasonable insights}@}. A class of important statistics are {@{_n-th moments_}@}, where {@{the first 3 moments \(starting from the 1st moment\)}@} are {@{_arithmetic mean_, _variance_ \(centralized\), and _skewness_ \(centralized and normalized\)}@}. <!--SR:!2026-07-04,285,330!fsrs,2029-08-01T05:13:40.039Z,1153,1153.10014712,1,2,9,0,0,2026-06-05T05:13:40.039Z!2029-08-03,1162,350!2029-03-06,1038,350!2029-04-03,1066,350-->

The _arithmetic mean_ is {@{the 1st \(non-centralized and unnormalized\) moment}@}, and defined as: {@{$$\text{mean} = \frac 1 N \sum_{n = 0}^{N - 1} x[n] \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}. <!--SR:!2029-04-09,1072,350!2029-05-03,1091,350!2029-07-22,1150,350-->

The \(biased\) _variance_ is {@{the 2nd \(centralized and unnormalized\) moment}@}, and defined as: {@{$$\text{variance} = \frac 1 N \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^2 \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}. <!--SR:!2029-06-22,1120,350!2029-05-25,1107,350!2028-08-20,851,330-->

The _skewness_ is {@{the 3rd \(centralized and normalized\) moment}@}, and defined as: {@{$$\text{skewness} = \frac {\frac 1 N \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^3} {\left(\frac 1 {N - 1} \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^2\right)^{3 / 2} } \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}. You should see the denominator is {@{the normalization factor}@} and is {@{the variance but with $1 / N$ \(biased\) replaced with $1 / (N - 1)$ \(unbiased\), and then a power of $3 / 2$ is applied}@}. <!--SR:!2029-03-16,1048,350!2026-07-03,285,330!2026-07-14,294,330!2029-05-26,1108,350!2029-06-10,1120,350-->

## overall features

We can also describe {@{features of the overall sound instead of each STFT frame}@}. Features can be grouped into {@{5 main categories}@}: {@{cognitive, formal, perceptual, sensorial, and physical}@}. <!--SR:!2026-06-25,277,330!fsrs,2029-09-01T13:30:03.320Z,1175,1175.1616206,1,2,9,0,0,2026-06-14T13:30:03.320Z!fsrs,2029-08-07T08:21:40.291Z,1157,1156.92457827,1,2,9,0,0,2026-06-07T08:21:40.291Z-->

{@{Cognitive features}@} describe {@{very high-level features formed by the brain}@}, e.g. {@{emotion, genre, semantic concepts, style, etc.}@} which are {@{very difficult to quantify}@}. <!--SR:!2029-08-29,1183,350!2026-07-14,294,330!2026-07-14,294,330!2026-07-14,294,330-->

{@{Formal features}@} describe {@{objective features of the music itself}@}, e.g. {@{instruments, key, melody, rhythm, structure, voice, articulation, etc.}@} <!--SR:!2026-06-17,272,330!2026-07-08,289,330!2029-04-26,1084,350-->

{@{Perceptual features}@} describe {@{how formal features are grouped together by the brain}@}, e.g. {@{beat \(time\), dynamics, simultaneous and successive intervals, spectral envelope \(timbre\)}@}. <!--SR:!2026-07-03,284,330!2029-05-14,1100,350!2026-07-14,294,330-->

{@{Sensorial features}@} describe {@{how the sound itself \(ignoring the formal features\) is perceived}@}, e.g. {@{loudness, pitch, timbre, time, etc.}@} <!--SR:!2026-07-14,294,330!2026-06-30,281,330!2029-08-31,1185,350-->

{@{Physical features}@} describe {@{the physical features of the sound itself}@}, e.g. {@{duration, frequency, intensity, spectrum, etc.}@} <!--SR:!2029-06-07,1117,350!2029-08-02,1161,350!2029-08-12,1171,350-->

### sound

{@{A _sound_}@} is {@{a note or simple melody played by an instrument}@}. It is {@{easily characterized due to its simple structure}@}. Its features can be grouped into {@{4 main groups}@}: {@{dynamics, morphology, pitch, and timbre}@}. <!--SR:!2026-06-22,276,330!2026-06-22,276,330!fsrs,2029-09-04T13:29:04.732Z,1178,1178.00364035,1,2,9,0,0,2026-06-14T13:29:04.732Z!2026-07-05,286,330!2026-07-06,287,330-->

{@{Timbre features}@} describe {@{the quality of a sound to the ears}@}, e.g. {@{high-frequency content, spectral centroid, spectral flux, etc.}@} <!--SR:!2029-08-27,1181,350!2026-06-27,279,330!2026-06-28,281,330-->

{@{Dynamic features}@} describe {@{the energy of a sound}@}, e.g. {@{average level, loudness, etc.}@} <!--SR:!2026-06-23,276,330!fsrs,2029-09-01T13:28:47.795Z,1175,1175.1616206,1,2,9,0,0,2026-06-14T13:28:47.795Z!2026-07-01,283,330-->

{@{Pitch features}@} describe {@{pitch}@}, e.g. {@{pitch, pitch salience, etc.}@} <!--SR:!2026-06-22,276,330!2029-07-03,1131,350!2026-07-14,294,330-->

{@{Morphological features}@} describe {@{onset and offset of a sound}@}, e.g. {@{envelope, onset rate, etc.}@} <!--SR:!2029-06-05,1116,350!fsrs,2029-09-05T13:29:09.368Z,1179,1179.41935434,1,2,9,0,0,2026-06-14T13:29:09.368Z!2026-06-26,278,330-->

### music

{@{_Music_}@} is {@{a recording composed of many sounds}@}. It is {@{very hard to characterize due to its complex structure}@}. Its features can be grouped into {@{4 main groups}@}: {@{melody/harmony, rhythm, structure, and timbre}@}. The features should be {@{related to musically meaningful concepts}@}. <!--SR:!2029-07-11,1139,350!2026-07-14,294,330!2029-05-18,1104,350!2029-06-03,1115,350!2026-06-22,276,330!2029-07-12,1140,350-->

{@{Timbre features}@} describe {@{how the instruments are used}@}, e.g. {@{instrumentation, instruments used, remixing, etc.}@} <!--SR:!2029-03-04,1036,350!2026-07-14,294,330!2029-07-14,1142,350-->

{@{Melody/harmony features}@} describe {@{the melody and harmony}@}, e.g. {@{chords, keys, mode, motive, phrase patterns, tonic, etc.}@} <!--SR:!fsrs,2029-08-30T13:30:00.399Z,1173,1172.77084718,1,2,9,0,0,2026-06-14T13:30:00.399Z!2029-05-19,1103,350!2029-08-22,1176,350-->

{@{Rhythm features}@} describe {@{the beats and their patterns}@}, e.g. {@{beat, downbeat, measure, metric cycle, patterns, tempo, etc.}@} <!--SR:!fsrs,2029-09-02T13:29:05.631Z,1176,1175.60646788,1,2,9,0,0,2026-06-14T13:29:05.631Z!fsrs,2029-08-31T13:29:13.238Z,1174,1174.19039405,1,2,9,0,0,2026-06-14T13:29:13.238Z!fsrs,2029-09-03T13:27:57.690Z,1177,1176.58438079,1,2,9,0,0,2026-06-14T13:27:57.690Z-->

{@{Structure features}@} describe {@{how the music is segmented}@}, e.g. {@{movements, sections, etc.}@} <!--SR:!2029-07-16,1144,350!2026-07-02,284,330!2029-05-07,1093,350-->

## collection features

We can {@{group similar sounds or music together}@} to form {@{sound or music collections}@}. We can group sounds or music by {@{their features}@}, or for music, {@{music concepts such as artist, genre, school, style, etc.}@} <!--SR:!2026-06-22,276,330!2026-06-25,278,330!2026-06-22,276,330!2029-07-09,1137,350-->

### clustering

There are {@{many ways to cluster sounds or music}@}. For simplicity, we consider {@{sound clustering only}@}. We also only use {@{the Euclidean distance}@}: {@{$$d(x, y) = \sqrt{\sum_{k = 1}^K (x - y)^2} \,,$$}@} where {@{$x$ and $y$ are features of two sounds and $K$ is the number of features}@}. Above, we represent each sound as {@{a point in $K$-dimensional space}@}. Each coordinate {@{corresponds to one _numerical_ feature}@}, and the coordinate value of a sound is {@{its value of the feature for that coordinate}@}. Using this distance, there are {@{two main ways to cluster sounds}@}: {@{K-means and K-nearest neighbors \(KNN\)}@}. <!--SR:!fsrs,2029-09-11T03:38:02.677Z,1184,1183.64577796,1,2,9,0,0,2026-06-15T03:38:02.677Z!2029-08-28,1182,350!2029-08-31,1185,350!2029-09-04,1188,350!2026-06-30,282,330!2029-07-24,1152,350!2029-06-23,1121,350!2026-07-04,285,330!fsrs,2029-08-07T08:21:39.431Z,1157,1156.92457827,1,2,9,0,0,2026-06-07T08:21:39.431Z!2026-06-22,276,330-->

{@{K-means}@} is used to {@{categorize existing sounds into $K$ groups}@}. The {@{detailed algorithm}@} is skipped here, but the goal is to {@{find $K$ locations \(centroids\)}@} such that {@{the sum of distances of all sounds to their nearest centroid is minimized}@}: {@{$$\operatorname{argmin}_{C} \sum_{k = 1}^K \sum_{x \in C_k} d(x, \mu_{C_k})^2 \,,$$}@} where {@{$C$ are groups of sounds grouped by their nearest centroid, and $\mu_{C_k}$ is the centroid point of the group $C_k$}@}, which equals {@{the arithmetic mean of points in $C_k$}@}. The algorithm returns {@{the centroids}@}. <!--SR:!2026-07-14,294,330!2026-07-01,282,330!2026-06-22,276,330!fsrs,2029-08-09T08:21:41.155Z,1159,1159.34014939,1,2,9,0,0,2026-06-07T08:21:41.155Z!2029-05-23,1106,350!2029-08-05,1164,350!fsrs,2029-08-01T05:13:40.719Z,1153,1153.10014712,1,2,9,0,0,2026-06-05T05:13:40.719Z!2029-07-08,1136,350!2026-07-14,294,330-->

{@{K-nearest neighbors \(KNN\)}@} is used to {@{categorize a new sound based on an existing categorization of sounds}@}. Given {@{a new sound}@}, find {@{the $K$ nearest existing sounds}@}. Take {@{the majority vote of categorization \(tie-breaking if needed\)}@}, and that is {@{the categorization of the new sound}@}. <!--SR:!2029-05-28,1110,350!2026-07-14,294,330!fsrs,2029-08-01T05:13:41.678Z,1153,1153.10014712,1,2,9,0,0,2026-06-05T05:13:41.678Z!fsrs,2029-08-09T08:21:37.520Z,1159,1159.34014939,1,2,9,0,0,2026-06-07T08:21:37.520Z!2026-07-03,284,330!fsrs,2029-09-11T03:38:03.671Z,1184,1183.64577796,1,2,9,0,0,2026-06-15T03:38:03.671Z-->
