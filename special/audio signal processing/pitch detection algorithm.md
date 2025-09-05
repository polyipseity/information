---
aliases:
  - pitch detection
  - pitch detection algorithm
  - pitch detection algorithms
tags:
  - flashcard/active/special/audio_signal_processing/pitch_detection_algorithm
  - language/in/English
---

# pitch detection algorithm

- see: [general/pitch detection algorithm](../../general/pitch%20detection%20algorithm.md)

A {@{__pitch detection algorithm__ \(__PDA__\)}@} is {@{an algorithm designed to estimate the pitch or fundamental frequency of a quasiperiodic or oscillating signal}@}, usually {@{a digital recording of speech or a musical note or tone}@}. This can be done in {@{the time domain, the frequency domain, or both}@}. <!--SR:!2026-05-22,251,332!2026-05-28,256,332!2026-05-26,254,332!2026-06-01,259,332-->

## autocorrelation

Autocorrelation is {@{a simple way to detect pitch in the time domain}@}. Mathematically, it is defined as: {@{$$r_x[l] = \sum_{n = 0}^{N - l - 1} x[n] x[n + l] \qquad l = 0, \ldots, N - 1 \,,$$}@} where {@{$l$ is the _lag time_}@}. <!--SR:!2026-05-28,256,332!2026-05-15,245,332!2026-05-31,258,332-->

Intuitively, when {@{the lag time is an integer multiple of the pitch}@}, {@{the original time signal $x[n]$ is very similar to the lagged time signal $x[n + l]$}@}, so {@{the autocorrelation \(their dot product\) will be large}@}. So {@{finding peaks in the resulting autocorrelation function}@} is a good pitch detection algorithm, especially for {@{monophonic sources but not polyphonic sources}@}. <!--SR:!2025-09-24,68,312!2025-09-24,68,312!2025-09-24,68,312!2025-09-24,68,312!2026-06-02,260,332-->

## YIN algorithm

\(Cheveigné and Kawahara, 2002\) Using the intuition from {@{using autocorrelation}@}, we can instead opt to use {@{the difference between the original time signal and the lagged signal instead}@}. Part of the YIN algorithm calculates: {@{$$d[l] = \sum_{n = 0}^{N - l - 1} (x[n] - x[n + l])^2 \qquad l = 0, \ldots, N - 1 \,,$$}@} where {@{$l$ is the _lag time_}@}. Then, we find {@{minima in the resulting difference function}@} instead of {@{finding peaks as in using autocorrelation}@}. The algorithm is good for {@{monophonic sources but not polyphonic sources}@}. <!--SR:!2026-06-03,261,332!2025-09-24,68,312!2026-04-27,229,330!2026-06-03,261,332!2026-05-16,246,332!2025-09-24,68,312!2026-05-27,255,332-->

## two-way mismatch algorithm

\(Maher and Beauchamp, 1994\) Two-way mismatch \(TWM\) algorithm operates on {@{the frequency domain}@}. Intuitively, given {@{a monophonic source}@}, the fundamental frequency is {@{a common divisor of the partial frequencies that best explains the spectral peaks}@}. TWM gives {@{a measure of how "good" a fundamental frequency explains the spectral peaks}@}. <!--SR:!2025-09-24,68,312!2026-05-28,256,332!2026-05-17,247,332!2025-09-23,67,312-->

The error function is {@{somewhat complicated}@}. First, we define {@{a _directional_ error function for matching a predicted frequency to actual frequencies}@}: {@{$$E_{f_n} = \Delta f_n (f_n)^{-p} + \frac {A_n} {\max A_n } \left(q \Delta f_n (f_n)^{-p} - r \right) \,,$$}@} where {@{$p, q, r$ are user-specified constants}@}; {@{$f_n$ is the _predicted_ frequency and $\Delta f_n$ is the _absolute_ difference between $f_n$ and its _nearest_ frequency in _actual_ frequencies}@}; and {@{$A_n$ is the predicted frequency amplitude and $\max A_n$ is the maximum amplitude among the predicted frequencies}@}. We see {@{the term $\Delta f_n(f_n)^{-p}$}@} appears twice; it represents {@{the difference that is increasingly weighted less as its predicted frequency increases}@}, because {@{the _absolute_ frequency difference matters less as frequency increases}@} \(compare {@{a 40&nbsp;Hz difference at 440&nbsp;Hz and 4400&nbsp;Hz}@}\). <!--SR:!2026-05-10,241,332!2026-05-21,250,332!2026-01-19,153,312!2026-02-03,165,312!2026-03-18,185,312!2025-09-24,68,312!2025-09-24,68,312!2026-05-23,252,332!2025-09-24,68,312!2026-05-20,249,332-->

Next, {@{we define the two _directional_ errors}@}. The first one is {@{the average error from matching predicted frequencies to actual frequencies}@}: {@{$$E_{p \to m} = \frac 1 N \sum_{n = 1}^N E_{f_n} \,,$$}@} where {@{$N$ is the number of predicted frequency peaks}@}. The second one is {@{the average error from matching actual frequencies to predicted frequencies}@}, swapping {@{their roles in the equation above}@}: {@{$$E_{m \to p} = \frac 1 K \sum_{k = 1}^K E_{f'_{k} } \,,$$}@} where {@{$K$ is the number of actual frequency peaks}@}. Finally, the error is {@{simply the sum of the above two errors}@}: {@{$$E = E_{p \to m} + \rho E_{m \to p} \,,$$}@} where {@{$\rho$ is a user-specified constant weighing the average error from matching actual frequencies to predicted frequencies}@}. Hence {@{the phrase "two-way"}@} in its name. <!--SR:!2026-05-15,245,332!2026-05-23,252,332!2026-05-28,256,332!2025-09-23,67,312!2026-05-11,242,332!2026-05-11,242,332!2026-05-16,246,332!2026-05-18,248,332!2026-05-28,256,332!2025-09-24,68,312!2025-09-24,68,312!2026-05-29,256,332-->

The original authors suggest setting the constants to {@{$p = 0.5, q = 1.4, r = 0.5, \rho = 0.33$}@}. <!--SR:!2025-09-24,68,312-->

## polyphonic signals

Given {@{polyphonic signals}@}, it is {@{much harder to find fundamental frequencies}@}, since we would need to {@{additionally identify which partials belong to which fundamentals}@}. But we can tackle {@{an easier problem}@}: {@{finding the _prominent pitch_}@}, i.e. {@{one of the fundamental frequencies that is the loudest among them}@}. \(Salamon and Gómez, 2012\) A proposed algorithm works by {@{considering all possible fundamental frequencies, and choosing the "best" \(kinda loudest\) fundamental frequency out of them using some weighing algorithm}@}. <!--SR:!2026-06-02,260,332!2025-09-24,68,312!2025-09-24,68,312!2026-05-11,242,332!2026-05-30,257,332!2026-05-19,248,332!2026-03-22,188,312-->
