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

The signal can be broken into {@{chunks \(usually slightly overlapping to reduce boundary artifacts\)}@} using {@{an analysis window $w$, which is essentially a function with nonzero values within a certain finite range}@}. Mathematically, it can be written as: {@{$$X_m[k] = \sum_{n = -N/2}^{N/2 - 1} x[n] w[n - m] e^{-j (2 \pi k/N) n} \,,$$}@} where $m$ is {@{how much rightward to shift the analysis window}@}. Usually, each frame {@{increments $m$ by a fixed number called the _hop size_ $H$}@} \(usually {@{slightly smaller than the analysis window size to reduce boundary artifacts}@}\). <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

We see that the analysis widow is {@{multiplied element-wise with the signal}@}, so in the frequency domain {@{the analysis window is convoluted with the signal}@}. Recall that {@{a complex sinusoid of frequency $k$ \(cycle frequency $k / N$\)}@} produce {@{a signal with its amplitude at frequency bin $k$}@} in the frequency domain. Then we see {@{windowing this complex sinusoid}@} will {@{"spread out" the signal around the frequency bin $k$ \(consider convolution\)}@} in the frequency domain. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

## window function

A window function is {@{a mathematical function that is zero-valued outside of some interval}@}. Typically, those used in STFT are {@{symmetric around the middle, approaching an maximum in the middle, and taper away from the middle}@}. Thus, their Fourier transform almost all look like {@{a large _main lobe_ in the middle, and then infinitely many _side lobes_ tapering off and approaching zero at infinity, and symmetric around the middle}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

We can characterize a window function using {@{its Fourier transform}@}. Two main metrics are {@{_main lobe width_ \(measured in bins\), and magnitude of the _highest_ side lobe _relative_ to the main lobe \(measured in dB\)}@}. The definition of _bins_ assume that {@{DFT is applied to a signal of length _M_ to produce another signal of length _M_ in the frequency domain \(i.e. the DFT size equals the window size\)}@}. The $k$-th frequency signal value represents {@{the $k / N$ cycle frequency}@} and is also called {@{the $k$-th frequency _bin_}@}. Thus, bins are {@{simply the number of samples in the frequency domain}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

There are {@{many kinds of windows}@}. Some common ones and their two main metrics are: <!--SR:!2025-07-01,4,270-->

- rectangular window ::@:: about 2 bins, −13.3&nbsp;dB <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- Hanning window ::@:: about 4 bins, −31.5&nbsp;dB <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- Hamming window ::@:: about 4 bins, −42.7&nbsp;dB <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- Blackman window ::@:: about 6 bins, −58&nbsp;dB <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- Blackman–Harris window ::@:: about 8 bins, −92&nbsp;dB <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->

We see there is a tradeoff from the above different window types: {@{relative magnitude of the highest side lobe decreases at the expense of increasing the main lobe width}@}. In practice, this means applying STFT, choosing an analysis window is a tradeoff between {@{sharp frequency peaks \(requires a thin main lobe\) and low noise \(requires weak side lobes\)}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->

## factors

There are {@{many factors}@} affecting the result of STFT: {@{window function, window size, FFT size, hop size, etc.}@} <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->

- window function ::@:: frequency resolution vs. frequency noise <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- window size ::@:: frequency resolution \(wider is better\) vs. time resolution \(narrower is better\) <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- window size evenness/oddness ::@:: Even window size cannot give a symmetric window, while odd window size can. So odd window size is better, since there will not be phase offsetting in the frequency domain. <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- FFT size ::@:: We are effectively zero-padding the window evenly on both sides if the FFT size exceeds the window size, since the window function is zero outside the window size. Remember this simply makes the resulting frequency signal have more bins, i.e. the frequency signal produced by a _continuous_ FT is sampled more often. <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->
- hop size ::@:: The hop size should be set so that when you add the shifted window functions together, a horizontal line appears in the middle, and only tapering off at the time signal boundaries. In this case, inverse STFT will recover the signal perfectly \(except for the edges\). <p> The reason is remember the time signal is weighted using the window function. Intuitively, each time signal value should ideally contribute equally to STFT. <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->

## inverse STFT

The STFT is {@{invertible}@}, that is, the original signal can be {@{recovered from the transform by the inverse STFT}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270-->

Remember that STFT is {@{simply applying DFT to the time signal weighted by a analysis window for each hop}@}. So you can simply {@{use the IDFT to get the windowed time signal for each hop}@}, and then {@{add the windowed time signals together from all hops}@}. The resulting time signal is {@{the original time signal modulated by the total weights in time \(adding the shifted window functions together\)}@}. \(If {@{the hop size is set ideally}@}, {@{the total weight should sum up to 1 for all time}@}.\) The above steps are usually implemented using {@{_overlap–add method_}@}. The overlapping is determined by {@{the window size minus the hop size}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

## STFT model

{@{Applying STFT}@} to a time signal yields {@{a magnitude spectrogram and a phase derivative spectrogram}@}. Then, we can {@{apply inverse STFT}@} to {@{approximately recover the original time signal}@}. This is known as a {@{_STFT model_}@}. Under {@{theoretical conditions \(requires the total weight to sum up to 1 for all time and integration over the infinite frequency domain\)}@}, this procedure {@{should _perfectly_ recover the original time signal}@}. In practice, {@{this is not the case}@}. We cannot integrate {@{over the infinite frequency domain}@}, and the total weights {@{cannot be made to sum up to 1 at the time signal boundaries \(this could be fixed by zero-padding the time signal\)}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->

It would seem odd to simply apply the STFT model to {@{transform the original time signal and recover an approximation of it}@}. Indeed, its utility is that {@{the intermediate magnitude spectrogram and phase derivative spectrogram can be edited}@} to {@{manipulate the original time signal in the frequency domain}@}. We can also {@{interpolate the original time signal with more samples}@} by {@{using a larger FFT size than that used in analysis using zero padding}@}. <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,270-->
