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

The signal can be broken into {@{chunks \(usually slightly overlapping to reduce boundary artifacts\)}@} using {@{an analysis window $w$, which is essentially a function with nonzero values within a certain finite range}@}. Mathematically, it can be written as: {@{$$X_m[k] = \sum_{n = -N/2}^{N/2 - 1} x[n] w[n - m] e^{-j (2 \pi k/N) n} \,,$$}@} where $m$ is {@{how much rightward to shift the analysis window}@}. \(annotation: Commonly, {@{convolution}@} is used to {@{window the signal}@}, so in the above expression, {@{$w[m - n]$ is much more often than $w[n -m]$}@}. When {@{the window is the symmetric, which is the usual case}@}, they are {@{equivalent}@}.\) Usually, each frame {@{increments $m$ by a fixed number called the _hop size_ $H$}@} \(often {@{smaller than the analysis window size to reduce boundary artifacts}@}\). <!--SR:!fsrs,2029-07-24T05:23:27.128Z,1144,1143.9805319,1,2,9,0,0,2026-06-06T05:23:27.128Z!2029-06-09,1120,350!2028-03-23,750,330!2029-04-12,1075,350!2029-02-25,1033,350!2026-06-11,266,330!2027-10-23,624,407!2027-10-31,631,407!2027-10-08,611,407!2027-11-18,645,407!2027-12-03,658,407-->

We see that the analysis widow is {@{multiplied element-wise with the signal}@}, so in the frequency domain {@{the analysis window is convoluted with the signal}@}. Recall that {@{a complex sinusoid of frequency $k$ \(cycle frequency $k / N$\)}@} produce {@{a signal with its amplitude at frequency bin $k$}@} in the frequency domain. Then we see {@{windowing this complex sinusoid}@} will {@{"spread out" the signal around the frequency bin $k$ \(consider convolution\)}@} in the frequency domain. <!--SR:!fsrs,2029-07-25T05:23:21.781Z,1145,1145.44682681,1,2,9,0,0,2026-06-06T05:23:21.781Z!2029-03-17,1053,350!2029-06-07,1118,350!2026-07-12,292,330!fsrs,2029-07-21T05:23:26.324Z,1141,1141.03569229,1,2,9,0,0,2026-06-06T05:23:26.324Z!fsrs,2029-07-29T05:20:45.519Z,1149,1148.89604352,1,2,9,0,0,2026-06-06T05:20:45.519Z-->

## window function

A window function is {@{a mathematical function that is zero-valued outside of some interval}@}. Typically, those used in STFT are {@{symmetric around the middle, approaching an maximum in the middle, and taper away from the middle}@}. Thus, their Fourier transform almost all look like {@{a large _main lobe_ in the middle, and then infinitely many _side lobes_ tapering off and approaching zero at infinity, and symmetric around the middle}@}. <!--SR:!2029-05-04,1089,350!fsrs,2029-07-29T05:23:20.061Z,1149,1149.39084626,1,2,9,0,0,2026-06-06T05:23:20.061Z!2029-05-31,1112,350-->

We can characterize a window function using {@{its Fourier transform}@}. Two main metrics are {@{_main lobe width_ \(measured in bins\)}@}, and {@{magnitude of the _highest_ side lobe _relative_ to the main lobe \(measured in dB\)}@}. {@{The definition of _bins_}@} assume that DFT is applied to {@{a signal of length _M_ to produce another signal of length _M_ in the frequency domain}@} \(i.e. {@{the DFT size equals the window size}@}\). The $k$-th frequency signal value represents {@{the $k / N$ cycle frequency}@} and is also called {@{the $k$-th frequency _bin_}@}. Thus, bins are {@{simply the number of samples in the frequency domain under the above assumption}@}. <!--SR:!2026-06-19,273,330!2029-03-28,1061,350!2029-03-06,1042,350!2028-05-03,780,330!fsrs,2029-07-21T05:23:15.578Z,1141,1141.03569229,1,2,9,0,0,2026-06-06T05:23:15.578Z!2029-06-06,1117,350!2026-10-25,380,370!2026-08-17,118,396!2026-08-18,119,396-->

There are {@{many kinds of windows}@}. Some common ones and their two main metrics are: <!--SR:!fsrs,2029-07-30T05:23:28.821Z,1150,1150.33930012,1,2,9,0,0,2026-06-06T05:23:28.821Z-->

- rectangular window ::@:: about 2 bins; about −13.3&nbsp;dB <!--SR:!2026-06-10,266,330!2029-04-05,1068,350-->
- Hanning window ::@:: about 4 bins; about −31.5&nbsp;dB <!--SR:!2029-05-03,1088,350!2029-03-26,1059,350-->
- Hamming window ::@:: about 4 bins; about −42.7&nbsp;dB <!--SR:!2028-04-21,771,330!2029-06-05,1117,350-->
- Blackman window ::@:: about 6 bins; about −58&nbsp;dB <!--SR:!fsrs,2029-07-27T05:23:23.912Z,1147,1147.44897046,1,2,9,0,0,2026-06-06T05:23:23.912Z!fsrs,2029-07-27T05:23:14.723Z,1147,1146.90917022,1,2,9,0,0,2026-06-06T05:23:14.723Z-->
- Blackman–Harris window ::@:: about 8 bins; about −92&nbsp;dB <!--SR:!2029-05-18,1102,350!2029-05-27,1109,350-->

We see there is a tradeoff from the above different window types: {@{relative magnitude of the highest side lobe decreases at the expense of increasing the main lobe width}@}. In practice, this means applying STFT, choosing an analysis window is a tradeoff between {@{sharp frequency peaks \(requires a thin main lobe\) and low noise \(requires weak side lobes\)}@}. <!--SR:!fsrs,2029-07-30T05:23:19.054Z,1150,1150.33930012,1,2,9,0,0,2026-06-06T05:23:19.054Z!fsrs,2029-07-26T05:23:25.663Z,1146,1145.99801254,1,2,9,0,0,2026-06-06T05:23:25.663Z-->

## factors

There are {@{many factors}@} affecting the result of STFT: {@{window function, window size, FFT size, hop size, etc.}@} <!--SR:!2029-05-10,1095,350!2029-03-11,1047,350-->

- window function ::@:: frequency resolution vs. frequency noise <!--SR:!fsrs,2029-07-23T05:23:24.719Z,1143,1142.51012048,1,2,9,0,0,2026-06-06T05:23:24.719Z!2026-06-30,281,330-->
- window size ::@:: frequency resolution \(wider is better\) vs. time resolution \(narrower is better\) <!--SR:!fsrs,2029-07-23T05:21:50.155Z,1143,1142.51012048,1,2,9,0,0,2026-06-06T05:21:50.155Z!fsrs,2029-07-27T05:20:46.402Z,1147,1147.44897046,1,2,9,0,0,2026-06-06T05:20:46.402Z-->
- window size evenness/oddness ::@:: Even window size cannot give a symmetric window, while odd window size can. So odd window size is better, since there will not be phase offsetting in the frequency domain. <!--SR:!2028-04-22,772,330!fsrs,2029-08-02T05:21:55.004Z,1153,1152.69207274,1,2,9,0,0,2026-06-06T05:21:55.004Z-->
- FFT size ::@:: We are effectively zero-padding the window evenly on both sides if the FFT size exceeds the window size, since the window function is zero outside the window size. Remember this simply makes the resulting frequency signal have more bins, i.e. the frequency signal produced by a _continuous_ FT is sampled more often. <!--SR:!fsrs,2029-07-29T05:23:20.899Z,1149,1148.89604352,1,2,9,0,0,2026-06-06T05:23:20.899Z!2029-03-01,1037,350-->
- hop size ::@:: The hop size should be set so that when you add the shifted window functions together, a horizontal line appears in the middle, and only tapering off at the time signal boundaries. In this case, inverse STFT will recover the signal perfectly \(except for the edges\). <p> The reason is remember the time signal is weighted using the window function. Intuitively, each time signal value should ideally contribute equally to STFT. <!--SR:!2029-06-08,1119,350!2026-06-20,274,330-->

## inverse STFT

The STFT is {@{invertible}@}, that is, the original signal can be {@{recovered from the transform by the inverse STFT}@}. <!--SR:!2026-06-24,277,330!2029-06-09,1119,350-->

Remember that STFT is {@{simply applying DFT to the time signal weighted by a analysis window for each hop}@}. So you can simply {@{use the IDFT to get the windowed time signal for each hop}@}, and then {@{add the windowed time signals together from all hops}@}. The resulting time signal is {@{the original time signal modulated by the total weights in time \(adding the shifted window functions together\)}@}. \(If {@{the hop size is set ideally}@}, {@{the total weight should sum up to 1 for all time}@}.\) The above steps are usually implemented using {@{_overlap–add method_}@}. The overlapping is determined by {@{the window size minus the hop size}@}. <!--SR:!2029-04-19,1081,350!fsrs,2029-07-29T05:23:28.031Z,1149,1148.89604352,1,2,9,0,0,2026-06-06T05:23:28.031Z!2029-05-30,1111,350!2029-05-22,1105,350!2029-04-30,1085,350!2029-05-29,1110,350!2029-05-12,1097,350!fsrs,2029-07-30T05:21:56.429Z,1150,1150.33930012,1,2,9,0,0,2026-06-06T05:21:56.429Z-->

## STFT model

{@{Applying STFT}@} to a time signal yields {@{a magnitude spectrogram and a phase derivative spectrogram}@}. Then, we can {@{apply inverse STFT}@} to {@{approximately recover the original time signal}@}. This is known as a {@{_STFT model_}@}. Under {@{theoretical conditions \(requires the total weight to sum up to 1 for all time and integration over the infinite frequency domain\)}@}, this procedure {@{should _perfectly_ recover the original time signal}@}. In practice, {@{this is not the case}@}. We cannot integrate {@{over the infinite frequency domain}@}, and the total weights {@{cannot be made to sum up to 1 at the time signal boundaries \(this could be fixed by zero-padding the time signal\)}@}. <!--SR:!2029-06-08,1118,350!fsrs,2029-07-31T05:21:53.009Z,1151,1151.27417371,1,2,9,0,0,2026-06-06T05:21:53.009Z!2026-07-03,285,330!2029-04-07,1069,350!2029-04-29,1084,350!2026-06-23,276,330!fsrs,2029-07-31T05:23:17.539Z,1151,1150.82315263,1,2,9,0,0,2026-06-06T05:23:17.539Z!2029-04-03,1067,350!2029-03-27,1060,350!fsrs,2029-07-27T05:23:16.807Z,1147,1147.44897046,1,2,9,0,0,2026-06-06T05:23:16.807Z-->

It would seem odd to simply apply the STFT model to {@{transform the original time signal and recover an approximation of it}@}. Indeed, its utility is that {@{the intermediate magnitude spectrogram and phase derivative spectrogram can be edited}@} to {@{manipulate the original time signal in the frequency domain}@}. We can also {@{interpolate the original time signal with more samples}@} by {@{using a larger FFT size than that used in analysis using zero padding}@}. <!--SR:!2029-04-24,1079,350!2029-04-25,1080,350!2029-03-29,1062,350!fsrs,2029-07-27T05:21:51.803Z,1147,1146.90917022,1,2,9,0,0,2026-06-06T05:21:51.803Z!2026-07-03,285,330-->
