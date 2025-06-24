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

A {@{__pitch detection algorithm__ \(__PDA__\)}@} is {@{an algorithm designed to estimate the pitch or fundamental frequency of a quasiperiodic or oscillating signal}@}, usually {@{a digital recording of speech or a musical note or tone}@}. This can be done in {@{the time domain, the frequency domain, or both}@}.

## autocorrelation

Autocorrelation is {@{a simple way to detect pitch in the time domain}@}. Mathematically, it is defined as: {@{$$r_x[l] = \sum_{n = 0}^{N - l - 1} x[n] x[n + l] \qquad l = 0, \ldots, N - 1 \,,$$}@} where {@{$l$ is the _lag time_}@}.

Intuitively, when {@{the lag time is an integer multiple of the pitch}@}, {@{the original time signal $x[n]$ is very similar to the lagged time signal $x[n + l]$}@}, so {@{the autocorrelation \(their dot product\) will be large}@}. So {@{finding peaks in the resulting autocorrelation function}@} is a good pitch detection algorithm, especially for {@{monophonic sources but not polyphonic sources}@}.

## YIN algorithm

\(Cheveigné and Kawahara, 2002\) Using the intuition from {@{using autocorrelation}@}, we can instead opt to use {@{the difference between the original time signal and the lagged signal instead}@}. Part of the YIN algorithm calculates: {@{$$d[l] = \sum_{n = 0}^{N - l - 1} (x[n] - x[n + l])^2 \qquad l = 0, \ldots, N - 1 \,,$$}@} where {@{$l$ is the _lag time_}@}. Then, we find {@{minima in the resulting difference function}@} instead of {@{finding peaks as in using autocorrelation}@}. The algorithm is good for {@{monophonic sources but not polyphonic sources}@}.

## two-way mismatch algorithm

\(Maher and Beauchamp, 1994\) Two-way mismatch \(TWM\) algorithm operates on {@{the frequency domain}@}. Intuitively, given {@{a monophonic source}@}, the fundamental frequency is {@{a common divisor of the partial frequencies that best explains the spectral peaks}@}. TWM gives {@{a measure of how "good" a fundamental frequency explains the spectral peaks}@}.

The error function is {@{somewhat complicated}@}. First, we define {@{a _directional_ error function for comparing a predicted frequency with actual frequencies}@}: {@{$$E_{f_n} = \Delta f_n (f_n)^{-p} + \frac {A_n} {\max A_n } \left(q \Delta f_n (f_n)^{-p} - r \right) \,,$$}@} where {@{$p, q, r$ are user-specified constants}@}; {@{$f_n$ is the _predicted_ frequency and $\Delta f_n$ is the _absolute_ difference between $f_n$ and its _nearest_ frequency in _actual_ frequencies}@}; and {@{$A_n$ is the predicted frequency amplitude and $\max A_n$ is the maximum amplitude among the predicted frequencies}@}. We see {@{the term $\Delta f_n(f_n)^{-p}$}@} appears twice; it represents {@{the difference that is increasingly weighted less as its predicted frequency increases}@}, because {@{the absolute frequency difference matters less as frequency increases}@} \(compare {@{a 40&nbsp;Hz difference at 440&nbsp;Hz and 4400&nbsp;Hz}@}\).

Next, {@{we define the two _directional_ errors}@}. The first one is {@{the total error from predicted frequencies to actual frequencies}@}: {@{$$E_{p \to m} = \frac 1 N \sum_{n = 1}^N E_{f_n} \,,$$}@} where {@{$N$ is the number of predicted frequency peaks}@}. The second one is {@{the total error from actual frequencies to predicted frequencies}@}, swapping {@{their roles in the equation above}@}: {@{$$E_{m \to p} = \frac 1 K \sum_{k = 1}^K E_{f'_{k} } \,,$$}@} where {@{$K$ is the number of actual frequency peaks}@}. Finally, the total error is {@{simply the sum of the above two errors}@}: {@{$$E = E_{p \to m} + \rho E_{m \to p}$$ \,,}@} where {@{$\rho$ is a user-specified constant}@}. Hence {@{the phrase "two-way"}@} in its name.

The original authors suggest setting the constants to {@{$p = 0.5, q = 1.4, r = 0.5, \rho = 0.33$}@}.

## polyphonic signals

Given {@{polyphonic signals}@}, it is {@{much harder to find fundamental frequencies}@}, since we would need to {@{additionally identify which partials belong to which fundamentals}@}. But we can tackle {@{an easier problem}@}: {@{finding the _prominent pitch_}@}, i.e. {@{one of the fundamental frequencies that is the loudest among them}@}. \(Salamon and Gómez, 2012\) A proposed algorithm works by {@{considering all possible fundamental frequencies, and choosing the "best" \(kinda loudest\) fundamental frequency out of them using some weighing algorithm}@}.
