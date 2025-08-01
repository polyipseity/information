---
aliases:
  - sinusoidal model
  - sinusoidal models
tags:
  - flashcard/active/special/audio_signal_processing/sinusoidal_model
  - language/in/English
---

# sinusoidal model

- see: [general/sinusoidal model](../../general/sinusoidal%20model.md)

A {@{__sinusoidal model__}@} approximates {@{a sequence $x_i$ to a sine \(or cosine\) function}@}: {@{$$x_i = C + A \sin(\omega t_i + \phi) + e_i \,.$$}@} where {@{$C$ is the mean level, $A$ is the sine amplitude, $\omega$ is the _angular_ frequency, $t_i$ is time, $\phi$ is phase shift, and $e_i$ is the error}@}.

## generalization

We can {@{generalize the above model to include multiple sinusoids}@}: {@{$$x_i = e_i + \sum_{r = 1}^R A_r \sin(\omega_r t_i + \phi_r) \,,$$}@} where {@{$R$ is the number of sinusoids}@}. The mean level $C$ can be subsumed by {@{a sinusoid of zero frequency \(which is simply a constant function\)}@}.

By {@{windowing the sequence $x_i$ using a window function}@}, the above model {@{can be further generalized to be time-varying in both amplitude $A_r$ and angular frequency $\omega_r$ \(in a way similar to short-time Fourier transform \(STFT\)\)}@}.

## discrete Fourier transform

For convenience, {@{the cosine function will be used}@} in place of the sine function below.

For each {@{sinusoid of amplitude $A$, frequency bin $k_0$ \(cycle frequency $k_0 / N$\), and phase offset $\phi$, i.e. $$A \cos(2 \pi (k_0 / N) n + \phi) = \frac 1 2 e^{j 2 \pi (k_0 / N) n} e^{j \phi} + \frac 1 2 e^{-j 2 \pi (k_0 / N) n} e^{-j \phi} \,,$$}@} in the model, it contributes to {@{two frequency bins in the resulting DFT}@}: {@{$$X[k] = \frac {AN} 2 e^{j \phi} \delta[k - k_0] + \frac {AN} 2 e^{-j \phi} \delta[k + k_0] \,.$$}@} If {@{a window function $w$ is used \(element-wise multiplied with the sinusoid\)}@}, then the above DFT is {@{convoluted with the window function DFT $W$}@}, producing: {@{$$X'[k] = \frac {AN} 2 e^{j \phi} W[k - k_0] + \frac {AN} 2 e^{-j \phi} W[k + k_0] \,.$$}@}

By above, we see that DFT can be used to {@{obtain a sinusoidal model directly}@}. Assuming the time signal is {@{real}@}, then {@{its DFT is conjugate symmetric \(as seen in the above equations\)}@}: {@{$$X[k] = X^*[-k] \,.$$}@} Then we only need to {@{look at the positive frequencies}@}, since {@{the negative frequencies provide the same information but conjugated}@}. For {@{each positive frequency bin value \(which is a complex number\) in the DFT}@}, its corresponding sinusoid has amplitude $A$ given by {@{multiplying the complex number magnitude by 2}@}, and has phase offset given by {@{the complex number angle}@}.

## practical considerations

In practice, the DFT is subject to {@{noise}@}, so often {@{only significant peaks in the DFT are considered}@}. This gives a sinusoidal model that is {@{an approximation of the original time signal}@}.

Another consideration is {@{spatial \(frequency\) resolution}@}. To {@{distinguish two sinusoids with \(linear\) frequency difference $\Delta f$}@}, we need two adjacent frequency bins to {@{represent frequencies that differ by at most $\Delta f$}@}. Since in DFT, this frequency spacing equals {@{the reciprocal of the duration of the input signal}@}, we require: {@{$$\Delta f \ge \frac 1 T = \frac 1 {T_s N} = \frac {f_s} N \implies N \ge \frac {f_s} {\Delta f} \,,$$}@} where {@{$T$ is the time signal duration, $T_s$ is the sample duration, $N$ is the number of samples, and $f_s$ is the sampling frequency}@}. In STFT, we further use {@{a windowing function}@}, which is characterized by {@{a main-lobe width $B$ in terms of frequency bins assuming the window size $M$ equals the DFT size $N$}@}. The main-lobe width can be interpreted as {@{how much a frequency is spread out by the windowing function}@}. Then we require {@{a frequency spacing of at most $\Delta f / B$ instead to distinguish these two now spread out frequencies}@}, producing: {@{$$\Delta f \ge \frac B T \implies N = M \ge B \frac {f_s} {\Delta f} \,.$$}@}

### peak detection

To detect peak, an naive way is {@{to simply find samples where the adjacent samples to the immediate left and right have magnitudes that are both lower than that of the sample itself}@}. There are {@{two problems with this approach}@}. One, there will be {@{many false positives}@}. This can be resolved by {@{also considering the phase \(derivative\) of the sample}@}. A peak should have {@{a stable phase \(or almost zero derivative\)}@}. Intuitively, this is because {@{the samples of a frequency peak formed by a single \(non-time-varying\) sinusoid should have the same phase, since they are produced by the same sinusoid}@}. Two, the peak location {@{may be in between samples}@}, and its actual magnitude {@{may be higher than that of its adjacent samples}@}. One way is to {@{simply zero-pad the input time signal so that the frequency signal will be interpolated enough}@}. The other is to {@{use parabolic interpolation}@}, described below.

A parabola is characterized by {@{its center $p$, its concavity $a$, and its offset $b$}@}: {@{$$y = a(x - p)^2 + b \,.$$}@} In parabolic interpolation, we are interested in {@{interpolating $p$ and $b$ using 3 points \(separated by a fixed $x$-distance; and the middle point is higher than the other two points\)}@}; that is, we fit {@{a parabola to these 3 points}@}. Once this is done, {@{the fitted $p$ is _approximately_ the actual peak location and $b$ is _approximately_ the actual peak amplitude}@}. For our purposes, assume the 3 points are {@{at $k - 1, k, k + 1$ \(_x_-values\) and have \(_y_-\)values $y_1, y_2, y_3$}@}. Then $p$ is: {@{$$p = k + \frac 1 2 \frac {y_1 - y_3} {y_1 - 2y_2 + y_3} \,.$$}@} and $b$ is: {@{$$b = y_2 - \frac 1 4 (p - k) (y_1 - y_3) = y_2 - \frac 1 8 \frac {(y_1 - y_3)^2} {y_1 - 2y_2 + y_3} \,.$$}@} After approximating the actual peak location $p$ and amplitude $b$, the sinusoid amplitude is given by {@{$2b$}@} and angle is given by {@{the phase at $p$ \(linearly interpolating if in between two sample points\)}@}.

The above steps detects constant sinusoids {@{lasting for the entire time signal}@}. We may be interested in {@{constant sinusoids lasting for shorter amount of times \(e.g. in a music track\)}@}. In this case, we can apply {@{short-time Fourier transform \(STFT\)}@}. For each frame, we {@{find its peaks}@}. Then we {@{compare across frames}@}. We say we detect a sinusoid of certain frequency when {@{we find a peak of that certain frequency \(within certain tolerance\) that last for at least $L$ frames, where $L$ is user-specified}@}. Note in this case, the sinusoid has {@{a time-varying amplitude and maybe even time-varying frequency}@}, so the amplitude and frequency in the above equations should be {@{replaced by a function of time}@}. There are {@{other more advanced ways}@}, which uses {@{the phase \(derivative\) of a peak across frames \(time\)}@}.

## additive synthesis

In {@{_additive synthesis_}@}, {@{sine waves are added together to create timbre}@}.

A sinusoidal model can be used to for additive synthesis. The idea is we start with {@{the frequency domain}@}, then {@{apply inverse DFT to get the time signal}@}, which will consist of {@{sine waves added together}@}. A naive way is to {@{simply set certain frequency bins to certain values}@}. However, the resulting time signal {@{will consist of sine waves that last forever}@}. Instead, we can again {@{use inverse STFT}@}. Then, when setting the frequencies, {@{we add the DFT of a windowing function instead of simply setting a single frequency bin}@} for each frequency. We could also only use {@{the main lobe of the DFT instead as an approximation}@} for simplicity. Then, we get {@{sine waves that taper off within the window according to the used windowing functions}@}, which can approximate {@{a sine wave that last for a certain amount of time}@}. Finally, using {@{the overlap–add method to add the individual windows at different frames \(time\)}@}, we can {@{synthesis the entire track}@}.

The window functions used could be {@{any of the conventional windowing functions}@}, or {@{a combination of them}@}. For example, the Blackman–Harris window is good at {@{producing windowed sine waves with only the main lobe, since its side lobes are weak}@}. But its tapering in the time signal is {@{very strong, so it is not good for generating a time-bearing signal \(a signal that last across multiple STFT frames\)}@}. We would need {@{a lot of overlap in between the STFT frames}@}. However, this can be fixed by {@{post-processing the generated time signal}@}, e.g. {@{dividing the time signal by the Blackman–Harris window and then multiply by the triangular window}@}. Effectively, we {@{undo the Blackman–Harris window and replace it by a triangular window}@}, which has a {@{much weaker tapering effect}@}, which allows for {@{less overlap in between the STFT frames}@}. The reason why we {@{do not directly use a triangular window}@} is because {@{its side lobes are stronger, so using only the main lobe would result in more noise in the time signal}@}.
