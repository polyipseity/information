---
aliases:
  - stochastic signal
  - stochastic signals
tags:
  - flashcard/active/special/audio_signal_processing/stochastic_process
  - language/in/English
---

# stochastic signal

- see: [general/stochastic process](../../general/stochastic%20process.md)

A {@{__stochastic signal__}@} is {@{a signal that is random}@}. It can be described by {@{statistics}@}: {@{mean, variance, probability distributions, etc.}@} <!--SR:!2025-09-12,56,310!2025-09-10,54,310!2025-09-13,57,310!2025-09-23,67,310-->

## frequency domain

Stochastic signal can be {@{described in the frequency domain}@}. Two important ones are {@{autocorrelation and power spectral density}@}. <!--SR:!2025-09-23,67,310!2025-09-23,67,310-->

{@{_Autocorrelation_}@} is defined as: {@{$$Z_{xx}[k] = \sum_{n = 0}^{N - 1} x[n] x[n + k] \qquad k = -N + 1, \ldots, N - 1 \,.=,$$}@} where {@{$x[n]$ is the \(stochastic\) signal and $k$ is the _time lag_}@}. It can help {@{identify repeating patterns or hidden periodicities}@}. <!--SR:!2025-09-10,54,310!2025-09-10,54,310!2025-09-17,61,310!2025-09-12,56,310-->

{@{_Power spectral density_}@} is defined as: {@{$$Xp[k] = \lim_{N \to \infty} \frac 1 {N^2} \left\lvert \sum_{n = 0}^{N - 1} x[n] e^{-j (2 \pi k) n / N} \right\rvert^2 \qquad k = 0, \ldots, N - 1 \,.$$}@} where {@{$x[n]$ is the \(stochastic\) signal and $k$ is the frequency bin}@}. It represents {@{the "energy" per time of the signal at a frequency bin}@}. <!--SR:!2025-08-30,43,290!2025-09-23,67,310!2025-09-18,62,310!2025-09-13,57,310-->

## stochastic model

A stochastic signal can be described by {@{its power spectral density}@}. This gives an idea to {@{generate new stochastic signal that is _similar_ to the original}@}: Combine {@{its power spectral density \(or its frequency magnitude\)}@} and {@{generate random phases for each frequency \(if the original phases from the stochastic signal are used, we get back the original signal\)}@}. <!--SR:!2025-09-23,67,310!2025-09-16,60,310!2025-09-16,60,310!2025-09-12,56,310-->

To do so, we can start with {@{white noise}@}, which has {@{constant power spectral density and random phases for each frequency}@}. This has a {@{simple representation}@} in the frequency domain: {@{$$U[k] = \lvert U[k] \rvert e^{j \angle U[k]} \,.$$}@} where {@{$U[k]$ is the Fourier transform of white noise; $\lvert U[k] \rvert$ is the amplitude, which should be the same for all frequencies by definition; and $\angle U[k]$ is the _random_ phase}@}. Then, given {@{the power spectral density of an existing signal $\frac 1 {N^2} \lvert H[k] \rvert^2$}@}, we {@{multiply the white noise Fourier transform element-wise}@}: {@{$$Y[k] = \frac 1 N \lvert H[k] \rvert U[k] = \frac 1 N \lvert H[k] \rvert \lvert U[k] \rvert e^{j \angle U[k]} \,.$$}@} We ignore {@{phases of the original signal}@} since we want to {@{generate a new stochastic signal similar to but not exactly the same as the original signal}@}. Finally, element-wise multiplication in the frequency domain translates to {@{convolution in the time domain}@}, so we have: {@{$$y[n] = \sum_{k = 0}^{N - 1} u[n] h[n - k] \,,$$}@} where {@{$u[n]$ is the white noise \(in time domain\) and $h[n] = \frac 1 N \sum_{k = 0}^{N - 1} \lvert H[k] \rvert e^{j (2\pi k / N) n}$ is the _impulse response_ \(obtained using IDFT\) of $\lvert H[k] \rvert$}@}. <!--SR:!2025-09-23,67,310!2025-09-18,62,310!2025-09-23,67,310!2025-09-19,63,310!2025-09-18,62,310!2025-09-23,67,310!2025-09-15,59,310!2025-09-23,67,310!2025-09-15,59,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-16,60,310!2025-09-23,67,310-->

We can extend the above to {@{stochastic signals with time-varying power spectral density}@} using {@{short-time Fourier transform \(STFT\)}@}. That is, for each frame, {@{we perform the above steps}@}. <!--SR:!2025-09-23,67,310!2025-09-17,61,310!2025-09-23,67,310-->

## denoising

Sometimes, we want to {@{denoise a stochastic signal}@}. We can do it in {@{the time domain or the frequency domain}@}. In both cases, we {@{find an envelope of the signal in the interested domain}@}. <!--SR:!2025-09-10,54,310!2025-09-11,55,310!2025-09-14,58,310-->

For denoising in {@{the frequency domain}@}, we can use {@{_linear predictive coding_ \(LPC\)}@}. We approximate the time signal $x[n]$ using {@{$$\tilde x[n] = \sum_{k = 1}^K a_k x[n - k] \,,$$ where $\tilde x[n]$ is the approximated signal, $a_k$ are constant coefficients, and $K$ is the window}@}. Intuitively, the above equation {@{approximates each time signal value using a linear combination of $K$ previous time signal values}@}. The $a_k$ coefficients are found by {@{minimizing the squared error}@}: {@{$$E = \sum_n (x[n] - \tilde x[n])^2 \,.$$}@} The resulting signal $\tilde x[n]$ will {@{have a power spectral density \(proportional to squared frequency magnitude\) that is an envelope of the original}@}. LPC can also be used {@{to synthesis sounds}@} by {@{using previously obtained coefficients $a_k$ with a white noise $u[n]$}@}: {@{$$y[n] = \sum_{k = 1}^n a_k u[n - k] \,.$$}@} <!--SR:!2025-09-15,59,310!2025-09-17,61,310!2025-09-10,54,310!2025-09-19,63,310!2025-09-23,67,310!2025-09-16,60,310!2025-09-11,55,310!2025-09-19,63,310!2025-09-19,63,310!2025-09-11,55,310-->

For denoising in {@{the time domain}@}, we can {@{apply DFT}@}, then {@{apply a low-pass filter in the frequency domain}@}, and then {@{apply IDFT}@}. The low-pass filter lets {@{low frequencies pass through while removing high frequencies}@}. It does so by {@{windowing the frequency domain so that values in low frequency bins are mostly unchanged while those in high frequency bins are significantly reduced/removed}@}. \(You may further {@{zero-pad in the frequency domain to increase the time signal sampling rate after IDFT}@}.\) The resulting signal looks like {@{a smoothened-out version of the original one}@}. The above method also applies for denoising in {@{the frequency domain}@} by {@{reversing the roles of the time and frequency signals}@}, e.g {@{smoothing the spectral power density \(squared frequency magnitude\) in a stochastic model}@}. <!--SR:!2025-09-23,67,310!2025-09-14,58,310!2025-09-13,57,310!2025-09-13,57,310!2025-09-23,67,310!2025-09-23,67,310!2025-09-18,62,310!2025-08-20,38,290!2025-09-14,58,310!2025-09-10,54,310!2025-09-10,54,310-->

## combining with other models

Given a signal, often {@{other models \(e.g. sinusoidal models, harmonic models\) are used to approximate it}@}. Then, subtracting {@{the original signal by the signal produced by the model}@} in the {@{time or frequency domain \(due to linearity of DFT\)}@}, we obtain {@{the _residual_ respectively in the time or frequency domain}@}. <!--SR:!2025-09-23,67,310!2025-09-23,67,310!2025-09-17,61,310!2025-09-12,56,310-->

The simplest way to {@{handle this residual}@} is to {@{simply add the residual albeit to the output by the other model}@}, which is called {@{a _residual model_}@}. By linearity, its DFT {@{is also added as-is}@}. This also means the original signal can be {@{recovered perfectly}@}. However, this means {@{the residual is always the same and highly specific to the sample used to obtain the residual model}@} when we want to {@{create a similar signal}@}. <!--SR:!2025-09-23,67,310!2025-09-23,67,310!2025-09-10,54,310!2025-09-23,67,310!2025-09-11,55,310!2025-09-10,54,310!2025-09-15,59,310-->

We notice the residual usually {@{somewhat looks like a weak random signal}@}, which inspires the second way of handling it: {@{using a stochastic model to approximate this residual}@}. This allows us to {@{generalize and randomize}@} the residual. <!--SR:!2025-09-14,58,310!2025-09-23,67,310!2025-09-11,55,310-->
