---
aliases:
  - audio feature
  - audio features
tags:
  - flashcard/active/special/audio_signal_processing/audio_feature
  - language/in/English
---

# audio feature

An {@{__audio feature__}@} captures {@{specific aspects of audio signals}@}. They are usually obtained by {@{_feature analysis_ in the frequency domain \(after DFT or STFT\)}@}.

## descriptors

They are {@{many different descriptors}@}. They can be mostly categorized into {@{spectral, time-domain, tonal, rhythm, SFX, and high-level descriptors}@} \(this is used by {@{[Essentia](https://essentia.upf.edu/)}@}\).

## spectral features

In a {@{STFT frame}@}, we can describe {@{many different spectral features}@}. We can also {@{describe spectral features across frames}@}.

### energy

There are many ways to {@{measure "energy" and/or loudness of a STFT frame}@}. {@{_Energy_}@} describes {@{the total "energy" in an audio or STFT frame}@} and is defined as {@{$$E = \sum_{k = 0}^{N - 1} \lvert X[k] \rvert^2 \,.$$}@} Its {@{_root mean square_}@} describes {@{the average "energy" per frequency bin}@} and is defined as {@{$$E_{\text{rms} } = \sqrt{\frac 1 N \sum_{k = 0}^{N - 1} \lvert X[k] \rvert^2 } \,.$$}@} {@{_Steven's power law_}@} describes {@{an empirical relationship in psychophysics between an increased intensity or strength in a physical stimulus and the perceived magnitude increase in the sensation created by the stimulus}@}, and for audio, is defined as {@{$$L = E^{0.67} \,,$$ where $L$ is _loudness_}@}.

There are also many ways to {@{characterize a spectrogram of a STFT frame}@}. {@{_Spectral centroid_}@} describes {@{the center of a spectrogram}@} and is defined as {@{$$C = \frac {\sum_{k = 0}^{N / 2} k \lvert X[k] \rvert } {\sum_{k = 0}^{N / 2} \lvert X[k] \rvert } \,,$$}@} i.e. its {@{weighted average frequency \(bin\) weighted by magnitude or _center of mass_}@}. Note {@{only the _nonnegative_ frequency bins \(from 0 to $N / 2$; both ends inclusive\) are used}@} since {@{for a real signal, the magnitude of a frequency equals that of its negative frequency \(conjugate-even\)}@}; including them {@{would always result in a centroid at the zero frequency bin, which is not useful}@}.

### mel-frequency

In a {@{normal \(linear\) power spectrum}@}, frequency bands are {@{not evenly spaced}@}. The {@{_mel scale_}@} takes {@{the logarithm to make the bands evenly spaced}@}. Its equation is: {@{$$m = 2595 \log_{10} \left(1 + \frac f {700} \right) \,.$$}@} A linear power spectrum can be {@{converted into _mel-frequency cepstrum_ \(MFC\) using the above formula}@}, but we need to {@{adjust the magnitudes, since the scale changes}@}. This is usually done with {@{a frequency filter using triangular or cosine overlapping windows}@}. We can further obtain the {@{_mel-frequency cepstrum coefficients_ \(MFCC\)}@} using the following equation: {@{$$\operatorname{MFCC} = \operatorname{DCT}\left(\log_{10} X^{\ge 0}[k] \right) \,,$$}@} where {@{$X^{\ge 0}[k]$ is the _mel-frequency_ cepstrum of _nonnegative_ frequency \(from 0 to $N / 2$, both ends inclusive\) and $\operatorname{DCT}$ is _discrete cosine transform_}@}. {@{The most commonly used DCT definition, _DCT-II_}@} is: {@{$$\operatorname{DCT-II}[k] = \sum_{n = 0}^{N - 1} x[n] \cos\left(\frac {\pi k} N \left(n + \frac 1 2 \right) \right) \,.$$}@}

### pitches

We can also {@{describe pitches in a STFT frame}@}. {@{A complex measure implemented in Essentia}@} is {@{_pitch salience_}@}. It first detects {@{the spectral peaks in a STFT frame}@}. Then it measure {@{the salience at bin frequency $b$ \(in _cent scale_\)}@} by: {@{$$S[b] = \sum_{h = 1}^H \sum_{p = 1}^P e(A_p) w(b, h, f_p) (A_p)^\beta \,,$$}@} where {@{$h$ represents harmonics, $p$ represents peaks, $e(A_p)$ is a threshold function \(0 below a certain threshold, otherwise 1\), and $w(b, h, f_p)$ is a complicated function weighing the spectral peaks}@}. Its motivation is that {@{a polyphonic sound source has many instruments playing at different pitches}@}. It aims to measure {@{how prominent each pitch is}@}.

Another measure is {@{_harmonic pitch class profile_ or simply _chroma_ \(a musical concept\)}@}. It divides {@{the octave into 12 semitone \(or any other frequency division\)}@}. Each semitone {@{over all possible octaves forms a _pitch class_, which has the same _chroma_}@}. Then, it finds {@{how prominent each pitch class is, thus describing tonality}@}. An example implementation is: {@{$$\operatorname{HPCP}[k] = \sum_{p = 1}^P w(k, f_p) A_p^2 \,,$$ where $p$ represents peaks and $w(k, f_p)$ is a weighing function}@}.

After {@{measuring the pitch salience}@}, we can {@{create _pitch contours_}@}. We can further {@{perform _melody selection_}@} to {@{find the fundamental frequency sequence of a melody}@}. Commonly, we choose {@{the _prominent_ melody}@}.

### multiple frames

{@{Features across frames}@} can be used for {@{detecting event onsets or segmenting events}@}.

A measure used to {@{segment events \(based on event onsets\)}@} is {@{_spectral flux_}@}, defined as: {@{$$\operatorname{SF}[l] = \sum_{k = 0}^{N / 2} \max\set{0, \lvert X[l, k] \rvert - \lvert X[l - 1, k] \rvert}$$}@} where {@{$l$ is the frame number}@}. It can be interpreted as {@{how much the total spectrum magnitude increases \(detects onset\), ignoring the decreases \(ignores offsets\)}@}. Whenever {@{this value exceeds a certain threshold}@}, we can say {@{a new event starts}@}, so we {@{segment the audio starting from this frame}@}. Another method is based on {@{_high-frequency content_ \(HFC\)}@}, defined as: {@{$$\operatorname{HFC}[l] = \sum_{k = 0}^{N / 2} k^2 \lvert X[l, k] \rvert \,,$$}@} which {@{weighs high-frequency magnitudes much more than low-frequency ones}@} due to {@{the factor $k^2$}@}. Then onset is detected by {@{finding the HFC difference for each two consecutive frames}@}, and then {@{say a new event starts when this difference is higher than a \(positive\) threshold}@}. The main difference between these two method is {@{the former weighs all frequencies evenly while the latter weighs high frequencies much more}@}, and which one is better {@{depends on the use case}@}.

## statistics

{@{Some basic statistics}@} are {@{applicable to many areas and provide reasonable insights}@}. A class of important statistics are {@{_n-th moments_}@}, where {@{the first 3 moments \(starting from the 1st moment\)}@} are {@{_arithmetic mean_, _variance_ \(centralized\), and _skewness_ \(centralized and normalized\)}@}.

The _arithmetic mean_ is {@{the 1st \(non-centralized and unnormalized\) moment}@}, and defined as: {@{$$\text{mean} = \frac 1 N \sum_{n = 0}^{N - 1} x[n] \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}.

The \(biased\) _variance_ is {@{the 2nd \(centralized and unnormalized\) moment}@}, and defined as: {@{$$\text{variance} = \frac 1 N \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^2 \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}.

The _skewness_ is {@{the 3rd \(centralized and normalized\) moment}@}, and defined as: {@{$$\text{skewness} = \frac {\frac 1 N \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^3} {\left(\frac 1 {N - 1} \sum_{n = 0}^{N - 1} (x[n] - \text{mean})^2\right)^{3 / 2} } \,,$$}@} where {@{$x[n]$ is an arbitrary sequence \(could be time-domain, spectral, etc.\)}@}. You should see the denominator is {@{the normalization factor}@} and is {@{the variance but with $1 / N$ \(biased\) replaced with $1 / (N - 1)$ \(unbiased\), and then a power of $3 / 2$ is applied}@}.

## overall features

We can also describe {@{features of the overall sound instead of each STFT frame}@}. Features can be grouped into {@{5 main categories}@}: {@{cognitive, formal, perceptual, sensorial, and physical}@}.

{@{Cognitive features}@} describe {@{very high-level features formed by the brain}@}, e.g. {@{emotion, genre, semantic concepts, style, etc.}@} which are {@{very difficult to quantify}@}.

{@{Formal features}@} describe {@{objective features of the music itself}@}, e.g. {@{instruments, key, melody, rhythm, structure, voice, articulation, etc.}@}

{@{Perceptual features}@} describe {@{how formal features are grouped together by the brain}@}, e.g. {@{beat \(time\), dynamics, simultaneous and successive intervals, spectral envelope \(timbre\)}@}.

{@{Sensorial features}@} describe {@{how the sound itself \(ignoring the formal features\) is perceived}@}, e.g. {@{loudness, pitch, timbre, time, etc.}@}

{@{Physical features}@} describe {@{the physical features of the sound itself}@}, e.g. {@{duration, frequency, intensity, spectrum, etc.}@}

### sound

{@{A _sound_}@} is {@{a note or simple melody played by an instrument}@}. It is {@{easily characterized due to its simple structure}@}. Its features can be grouped into {@{4 main groups}@}: {@{dynamics, morphology, pitch, and timbre}@}.

{@{Timbre features}@} describe {@{the quality of a sound to the ears}@}, e.g. {@{high-frequency content, spectral centroid, spectral flux, etc.}@}

{@{Dynamic features}@} describe {@{the energy of a sound}@}, e.g. {@{average level, loudness, etc.}@}

{@{Pitch features}@} describe {@{pitch}@}, e.g. {@{pitch, pitch salience, etc.}@}

{@{Morphological features}@} describe {@{onset and offset of a sound}@}, e.g. {@{envelope, onset rate, etc.}@}

### music

{@{_Music_}@} is {@{a recording composed of many sounds}@}. It is {@{very hard to characterize due to its complex structure}@}. Its features can be grouped into {@{4 main groups}@}: {@{melody/harmony, rhythm, structure, and timbre}@}. The features should be {@{related to musically meaningful concepts}@}.

{@{Timbre features}@} describe {@{how the instruments are used}@}, e.g. {@{instrumentation, instruments used, remixing, etc.}@}

{@{Melody/harmony features}@} describe {@{the melody and harmony}@}, e.g. {@{chords, keys, mode, motive, phrase patterns, tonic, etc.}@}

{@{Rhythm features}@} describe {@{the beats and their patterns}@}, e.g. {@{beat, downbeat, measure, metric cycle, patterns, tempo, etc.}@}

{@{Structure features}@} describe {@{how the music is segmented}@}, e.g. {@{movements, sections, etc.}@}

## collection features

We can {@{group similar sounds or music together}@} to form {@{sound or music collections}@}. We can group sounds or music by {@{their features}@}, or for music, {@{music concepts such as artist, genre, school, style, etc.}@}

### clustering

There are {@{many ways to cluster sounds or music}@}. For simplicity, we consider {@{sound clustering only}@}. We also only use {@{the Euclidean distance}@}: {@{$$d(x, y) = \sqrt{\sum_{k = 1}^K (x - y)^2} \,,$$}@} where {@{$x$ and $y$ are features of two sounds and $K$ is the number of features}@}. Above, we represent each sound as {@{a point in $K$-dimensional space}@}. Each coordinate {@{corresponds to one _numerical_ feature}@}, and the coordinate value of a sound is {@{its value of the feature for that coordinate}@}. Using this distance, there are {@{two main ways to cluster sounds}@}: {@{K-means and K-nearest neighbors \(KNN\)}@}.

{@{K-means}@} is used to {@{categorize existing sounds into $K$ groups}@}. The {@{detailed algorithm}@} is skipped here, but the goal is to {@{find $K$ locations \(centroids\)}@} such that {@{the sum of distances of all sounds to their nearest centroid is minimized}@}: {@{$$\operatorname{argmin}_{C} \sum_{k = 1}^K \sum_{x \in C_k} d(x, \mu_{C_k})^2 \,,$$}@} where {@{$C$ are groups of sounds grouped by their nearest centroid, and $\mu_{C_k}$ is the centroid point of the group $C_k$}@}, which equals {@{the arithmetic mean of points in $C_k$}@}. The algorithm returns {@{the centroids}@}.

{@{K-nearest neighbors \(KNN\)}@} is used to {@{categorize a new sound based on an existing categorization of sounds}@}. Given {@{a new sound}@}, find {@{the $K$ nearest existing sounds}@}. Take {@{the majority vote of categorization \(tie-breaking if needed\)}@}, and that is {@{the categorization of the new sound}@}.
