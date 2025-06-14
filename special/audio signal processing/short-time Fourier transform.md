---
aliases:
  - STFT
  - STFTs
  - short-time Fourier transform
  - short-time Fourier transforms
tags:
  - flashcard/active/special/audio_signal_processing/short-time_Fourier_transform
  - language/in/English
---

# short-time Fourier transform

- see: [general/short-time Fourier transform](../../general/short-time%20Fourier%20transform.md)

## discrete STFT

The signal can be broken into {@{chunks \(usually slightly overlapping to reduce boundary artifacts\)}@} using {@{an analysis window $w$, which is essentially a function with nonzero values within a certain finite range}@}. Mathematically, it can be written as: {@{$$X_m[k] = \sum_{n = -N/2}^{N/2 - 1} x[n] w[n - m] e^{-j (2 \pi k/N) n} \,,$$}@} where $m$ is {@{how much rightward to shift the analysis window}@}. Usually, each frame {@{increments $m$ by a fixed number called the _hop size_ $H$}@} \(usually {@{slightly smaller than the analysis window size to reduce boundary artifacts}@}\).

We see that the analysis widow is {@{multiplied element-wise with the signal}@}, so in the frequency domain {@{the analysis window is convoluted with the signal}@}. Recall that {@{a complex sinusoid of frequency $k$ \(cycle frequency $k / N$\)}@} produce {@{a signal with its amplitude at frequency bin $k$}@} in the frequency domain. Then we see {@{windowing this complex sinusoid}@} will {@{"spread out" the signal around the frequency bin $k$ \(consider convolution\)}@} in the frequency domain.

## window function

A window function is {@{a mathematical function that is zero-valued outside of some interval}@}. Typically, those used in STFT are {@{symmetric around the middle, approaching an maximum in the middle, and taper away from the middle}@}. Thus, their Fourier transform almost all look like {@{a large _main lobe_ in the middle, and then infinitely many _side lobes_ tapering off and approaching zero at infinity, and symmetric around the middle}@}.

We can characterize a window function using {@{its Fourier transform}@}. Two main metrics are {@{_main lobe width_ \(measured in bins\), and magnitude of the _highest_ side lobe _relative_ to the main lobe \(measured in dB\)}@}. The definition of _bins_ assume that {@{DFT is applied to a signal of length _N_ to produce another signal of length _N_ in the frequency domain}@}. The $k$-th frequency signal value represents {@{the $k / N$ cycle frequency}@} and is also called {@{the $k$-th frequency _bin_}@}. Thus, bins are {@{simply the number of samples in the frequency domain}@}.

There are {@{many kinds of windows}@}. Some common ones and their two main metrics are:

- rectangular window ::@:: 2 bins, −13.3&nbsp;dB
- Hanning window ::@:: 4 bins, −31.5&nbsp;dB
- Hamming window ::@:: 4 bins, −42.7&nbsp;dB
- Blackman window ::@:: 6 bins, −58&nbsp;dB
- Blackman–Harris window ::@:: 8 bins, −92&nbsp;dB

We see there is a tradeoff from the above different window types: {@{relative magnitude of the highest side lobe decreases at the expense of increasing the main lobe width}@}. In practice, this means applying STFT, choosing an analysis window is a tradeoff between {@{sharp frequency peaks \(requires a thin main lobe\) and low noise \(requires weak side lobes\)}@}.

## factors

There are {@{many factors}@} affecting the result of STFT: {@{window function, window size, FFT size, hop size, etc.}@}

- window function ::@:: frequency resolution vs. frequency noise
- window size ::@:: frequency resolution \(wider is better\) vs. time resolution \(narrower is better\)
- window size evenness/oddness ::@:: Even window size cannot give a symmetric window, while odd window size can. So odd window size is better, since there will not be phase offsetting in the frequency domain.
- FFT size ::@:: We are effectively zero-padding the window evenly on both sides if the FFT size exceeds the window size, since the window function is zero outside the window size. Remember this simply makes the resulting frequency signal have more bins, i.e. the frequency signal produced by a _continuous_ FT is sampled more often.
- hop size ::@:: The hop size should be set so that when you add the shifted window functions together, a horizontal line appears in the middle, and only tapering off at the boundaries. In this case, inverse STFT will recover the signal perfectly \(except for the edges\). <p> The reason is remember the time signal is weighted using the window function. Intuitively, each time signal value should ideally contribute equally to STFT.

## inverse STFT

The STFT is {@{invertible}@}, that is, the original signal can be {@{recovered from the transform by the inverse STFT}@}.

Remember that STFT is {@{simply applying DFT to the time signal weighted by a analysis window for each hop}@}. So you can simply {@{use the inverse DFT to get the windowed time signal for each hop}@}, and then {@{add the windowed time signals together from all hops}@}. The resulting time signal is {@{the original time signal weighted by the total weights in time \(adding the shifted window functions together\)}@}. \(If {@{the hop size is set ideally}@}, {@{the total weight should sum up to 1 for all time}@}.\)

The above steps are usually implemented using {@{_overlap–add method_}@}. It is very similar to {@{the above steps}@}, but {@{DFT is applied to non-overlapping windowed segments of the frequency signal instead of the whole frequency signal to save time}@}. To {@{account for edge effects in the time domain}@}, {@{each windowed segment is zero-padded by a fixed number of samples $n$}@}. This causes {@{the output time signal after IDFT to be longer so that it also accounts for edge effects}@}. Then, we {@{add the output time signals, shifted to match the position of the corresponding windowed segment position and overlapping by $n$ samples}@}.
