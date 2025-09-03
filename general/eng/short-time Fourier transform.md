---
aliases:
  - STFT
  - STFTs
  - short-time Fourier transform
  - short-time Fourier transformation
  - short-time Fourier transformations
  - short-time Fourier transforms
tags:
  - flashcard/active/general/eng/short-time_Fourier_transform
  - language/in/English
---

# short-time Fourier transform

The {@{__short-time Fourier transform__ \(__STFT__\)}@} is {@{a [Fourier-related transform](list%20of%20Fourier-related%20transforms.md) used to determine the sinusoidal frequency and phase content of local sections of a signal as it changes over time}@}.<sup>[\[1\]](#^ref-1)</sup> In practice, {@{the procedure for computing STFTs}@} is to {@{divide a longer time signal into shorter segments of equal length}@} and then {@{compute the Fourier transform separately on each shorter segment}@}. This reveals {@{the Fourier spectrum on each shorter segment}@}. One then usually {@{plots the changing spectra as a function of time}@}, known as {@{a [spectrogram](spectrogram.md) or [waterfall plot](waterfall%20plot.md)}@}, such as commonly used in {@{[software defined radio](software%20defined%20radio.md) \(SDR\) based spectrum displays}@}. {@{Full bandwidth displays covering the whole range of an SDR}@} commonly use {@{fast Fourier transforms \(FFTs\) with 2^24 points}@} on desktop computers.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> <!--SR:!2025-09-24,69,329!2026-05-11,244,330!2025-10-02,76,329!2025-09-26,71,329!2025-09-30,74,329!2025-09-13,59,310!2025-10-01,75,329!2025-09-30,74,329!2025-10-02,76,329!2025-10-02,76,329!2025-10-02,76,329-->

> {@{![A spectrogram visualizing the results of a STFT of the words "nineteenth century".](../../archives/Wikimedia%20Commons/Spectrogram-19thC.png)}@}
>
> {@{A spectrogram}@} visualizing {@{the results of a STFT of the words "nineteenth century"}@}. Here, {@{frequencies}@} are shown {@{increasing up the vertical axis}@}, and {@{time}@} on {@{the horizontal axis}@}. {@{The legend to the right}@} shows that {@{the color intensity increases with the density}@}. <!--SR:!2026-05-18,250,330!2026-05-23,254,330!2025-10-02,76,329!2025-09-28,72,329!2025-10-01,75,329!2025-10-01,75,329!2026-05-06,240,330!2025-09-21,66,310!2025-09-30,74,329-->

## forward STFT

### continuous-time STFT

Simply, in {@{the continuous-time case}@}, the function to be transformed is {@{multiplied by a [window function](window%20function.md) which is nonzero for only a short period of time}@}. {@{The [Fourier transform](Fourier%20transform.md) \(a one-dimensional function\)}@} of the resulting signal is taken, then {@{the window is slid along the time axis until the end}@} resulting in {@{a two-dimensional representation of the signal}@}. Mathematically, this is written as: {@{$$\mathbf {STFT} \{x(t)\}(\tau ,\omega )\equiv X(\tau ,\omega )=\int _{-\infty }^{\infty }x(t)w(t-\tau )e^{-i\omega t}\,dt$$}@} where {@{$w(\tau )$ is the [window function](window%20function.md)}@}, commonly a {@{[Hann window](window%20function.md#Hann%20and%20Hamming%20windows) or [Gaussian window](window%20function.md#Gaussian%20window) centered around zero}@}, and {@{$x(t)$ is the signal to be transformed}@} \(note the difference between {@{the window function $w$ and the frequency $\omega$}@}\). {@{$X(\tau ,\omega )$}@} is essentially {@{the Fourier transform of $x(t)w(t-\tau )$}@}, {@{a [complex function](complex%20function.md)}@} representing {@{the phase and magnitude of the signal over time and frequency}@}. Often {@{[phase unwrapping](phase%20unwrapping.md) is employed}@} along {@{either or both the time axis, $\tau$, and frequency axis, $\omega$}@}, to {@{suppress any [jump discontinuity](jump%20discontinuity.md#jump%20discontinuity) of the phase result of the STFT}@}. {@{The time index $\tau$}@} is normally considered to be {@{"_slow_" time}@} and usually {@{not expressed in as high resolution as time $t$}@}. Given that the STFT is essentially {@{a Fourier transform times a window function}@}, the STFT is also called {@{windowed Fourier transform or time-dependent Fourier transform}@}. <!--SR:!2025-09-27,71,329!2025-09-17,63,310!2025-10-02,76,329!2025-09-13,59,310!2025-10-02,76,329!2025-10-02,76,329!2025-10-02,76,329!2026-05-21,252,330!2025-10-01,75,329!2025-09-17,62,310!2026-04-24,229,330!2026-05-24,255,330!2025-09-28,72,329!2025-10-02,76,329!2025-09-29,73,329!2025-09-17,62,310!2025-09-29,73,329!2025-09-29,73,329!2025-09-13,59,310!2025-09-29,73,329!2026-05-19,251,330!2025-09-27,71,329-->

### discrete-time STFT

- See also: ::@:: [Modified discrete cosine transform](modified%20discrete%20cosine%20transform.md) <!--SR:!2026-04-27,232,330!2026-04-25,230,330-->

In {@{the discrete time case}@}, {@{the data to be transformed}@} could be {@{broken up into chunks or frames}@} \(which usually {@{overlap each other, to reduce artifacts at the boundary}@}\). Each chunk is {@{[Fourier transformed](Fourier%20transform.md)}@}, and {@{the complex result is added to a matrix}@}, which records {@{magnitude and phase for each point in time and frequency}@}. This can be expressed as: {@{$$\mathbf {STFT} \{x[n]\}(m,\omega )\equiv X(m,\omega )=\sum _{n=0}^{N-1}x[n]w[n-m]e^{-i\omega n}$$}@} likewise, with {@{signal $x[n]$ and window $w[n]$}@}. In this case, {@{_m_ is discrete and ω is continuous}@}, but in {@{most typical applications}@} the STFT is {@{performed on a computer using the [fast Fourier transform](fast%20Fourier%20transform.md)}@}, so both variables are {@{discrete and [quantized](quantization%20(signal%20processing).md)}@}. <!--SR:!2025-10-01,75,329!2026-05-20,251,330!2025-09-26,71,329!2025-10-02,76,329!2025-09-30,74,329!2025-10-02,76,329!2025-09-29,73,329!2025-09-17,63,310!2026-05-07,241,330!2025-09-15,61,310!2025-09-18,63,310!2025-09-28,72,329!2025-09-16,61,310-->

{@{The [magnitude](magnitude%20(mathematics).md) squared of the STFT}@} yields {@{the [spectrogram](spectrogram.md) representation of the power spectral density of the function}@}: {@{$$\operatorname {spectrogram} \{x(t)\}(\tau ,\omega )\equiv |X(\tau ,\omega )|^{2}$$}@} <!--SR:!2026-05-02,237,330!2025-10-02,76,329!2025-09-16,61,310-->

See also {@{the [modified discrete cosine transform](modified%20discrete%20cosine%20transform.md) \(MDCT\)}@}, which is also {@{a Fourier-related transform that uses overlapping windows}@}. <!--SR:!2025-09-27,71,329!2025-10-02,76,329-->

#### sliding DFT

If {@{only a small number of ω are desired}@}, or if {@{the STFT is desired to be evaluated for every shift _m_ of the window}@}, then {@{the STFT may be more efficiently evaluated}@} using a {@{[sliding DFT](sliding%20DFT.md) algorithm}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-09-28,72,329!2025-09-27,71,329!2026-05-23,254,330!2025-09-14,60,310-->

## inverse STFT

The STFT is {@{[invertible](invertible%20function.md)}@}, that is, {@{the original signal can be recovered from the transform by the inverse STFT}@}. {@{The most widely accepted way of inverting the STFT}@} is by using {@{the [overlap-add \(OLA\) method](overlap–add%20method.md)}@}, which also allows for {@{modifications to the STFT complex spectrum}@}. This makes for {@{a versatile signal processing method}@},<sup>[\[3\]](#^ref-3)</sup> referred to as {@{the _overlap and add with modifications_ method}@}. <!--SR:!2025-09-21,66,310!2025-10-02,76,329!2025-10-02,76,329!2025-09-29,73,329!2025-09-18,64,329!2025-09-16,62,310!2025-10-02,76,329-->

<!-- markdownlint-disable-next-line MD024 -->
### continuous-time STFT

Given {@{the width and definition of the window function _w_\(_t_\)}@}, we initially {@{require the area of the window function to be scaled}@} so that {@{$$\int _{-\infty }^{\infty }w(\tau )\,d\tau =1.$$}@} It easily follows that {@{$$\int _{-\infty }^{\infty }w(t-\tau )\,d\tau =1\quad \forall \ t$$}@} and {@{$$x(t)=x(t)\int _{-\infty }^{\infty }w(t-\tau )\,d\tau =\int _{-\infty }^{\infty }x(t)w(t-\tau )\,d\tau .$$}@} <!--SR:!2025-09-15,61,310!2025-09-17,62,310!2025-09-18,63,310!2025-09-28,72,329!2025-09-30,74,329-->

{@{The continuous Fourier transform}@} is {@{$$X(\omega )=\int _{-\infty }^{\infty }x(t)e^{-i\omega t}\,dt.$$}@} {@{Substituting _x_\(_t_\)}@} from above: {@{$$\begin{aligned} X(\omega ) & =\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }x(t)w(t-\tau )\,d\tau \right]\,e^{-i\omega t}\,dt \\ & =\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,d\tau \,dt. \end{aligned}$$}@} <!--SR:!2025-10-01,75,329!2025-09-21,66,310!2025-09-16,62,310!2025-10-01,75,329-->

Swapping {@{order of integration}@}: {@{$$\begin{aligned} X(\omega ) & =\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,dt\,d\tau \\ & =\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,dt\right]\,d\tau \\ & =\int _{-\infty }^{\infty }X(\tau ,\omega )\,d\tau . \end{aligned}$$}@} <!--SR:!2025-10-01,75,329!2025-09-28,72,329-->

So the Fourier transform can be seen as {@{a sort of phase coherent sum of all of the STFTs of _x_\(_t_\)}@}. Since {@{the inverse Fourier transform}@} is {@{$$x(t)={\frac {1}{2\pi } }\int _{-\infty }^{\infty }X(\omega )e^{+i\omega t}\,d\omega ,$$}@} then {@{_x_\(_t_\) can be recovered from _X_\(τ,ω\)}@} as {@{$$x(t)={\frac {1}{2\pi } }\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\tau \,d\omega .$$}@} or {@{$$x(t)=\int _{-\infty }^{\infty }\left[{\frac {1}{2\pi } }\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega \right]\,d\tau .$$}@} It can be seen, comparing to {@{above that windowed "grain" or "wavelet" of _x_\(_t_\)}@} is {@{$$x(t)w(t-\tau )={\frac {1}{2\pi } }\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega .$$}@} {@{the inverse Fourier transform of _X_\(τ,ω\)}@} for τ fixed. <!--SR:!2025-09-25,70,329!2025-09-27,71,329!2025-09-14,60,310!2025-09-25,70,329!2025-09-29,73,329!2026-01-19,139,290!2026-01-30,162,310!2025-09-27,71,329!2026-02-28,173,310-->

{@{An alternative definition}@} that is {@{valid only in the vicinity of τ}@}, {@{the inverse transform}@} is: {@{$$x(t)={\frac {1}{w(t-\tau )} }{\frac {1}{2\pi } }\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega .$$}@} <!--SR:!2025-09-27,71,329!2025-09-29,73,329!2025-09-27,71,329!2026-01-18,144,309-->

In general, {@{the window function $w(t)$}@} has the following properties: \(annotation: 3 items: {@{even symmetry, non-increasing \(for positive time\), compact support}@}\) <!--SR:!2025-10-01,75,329!2025-09-28,72,329-->

- \(a\) even symmetry: ::@:: $w(t)=w(-t)$; <!--SR:!2025-09-30,74,329!2025-09-30,74,329-->
- \(b\) non-increasing \(for positive time\): ::@:: $w(t)\geq w(s)$ if $|t|\leq |s|$; <!--SR:!2025-10-01,75,329!2026-05-18,250,330-->
- \(c\) compact support: ::@:: $w(t)$ is equal to zero when \|t\| is large. <!--SR:!2026-05-22,253,330!2025-09-30,74,329-->

## resolution issues

- Further information: ::@:: [Gabor limit](Gabor%20limit.md#signal%20processing) and [Küpfmüller's uncertainty principle](Küpfmüller's%20uncertainty%20principle.md) <!--SR:!2026-05-25,255,330!2025-09-27,71,329-->

One of {@{the pitfalls of the STFT}@} is that {@{it has a fixed resolution}@}. {@{The width of the windowing function}@} relates to {@{how the signal is represented}@}—it determines {@{whether there is good frequency resolution \(frequency components close together can be separated\)}@} or {@{good time resolution \(the time at which frequencies change\)}@}. {@{A wide window}@} gives {@{better frequency resolution but poor time resolution}@}. {@{A narrower window}@} gives {@{good time resolution but poor frequency resolution}@}. These are called {@{narrowband and wideband transforms}@}, respectively. <!--SR:!2025-09-28,72,329!2025-09-28,72,329!2025-09-29,73,329!2025-10-01,75,329!2025-09-28,72,329!2025-09-30,74,329!2025-09-29,73,329!2025-09-17,63,310!2025-09-18,64,329!2025-10-02,76,329!2025-09-18,64,329-->

> {@{![Comparison of STFT resolution. Left has better time resolution, and right has better frequency resolution.](../../archives/Wikimedia%20Commons/STFT%20-%20windows-en.svg)}@}
>
> Comparison of {@{STFT resolution}@}. Left has {@{better time resolution}@}, and {@{right has better frequency resolution}@}. <!--SR:!2026-05-12,245,330!2025-09-27,71,329!2025-10-01,75,329!2025-09-28,72,329-->

This is one of {@{the reasons for the creation of the [wavelet transform](wavelet%20transform.md) and [multiresolution analysis](multiresolution%20analysis.md)}@}, which can give {@{good time resolution for high-frequency events and good frequency resolution for low-frequency events}@}, the combination {@{best suited for many real signals}@}. <!--SR:!2025-10-02,76,329!2025-09-18,64,329!2025-09-30,74,329-->

This property is related to {@{the [Heisenberg](Werner%20Heisenberg.md) [uncertainty principle](uncertainty%20principle.md)}@}, but {@{not directly – see [Gabor limit](Gabor%20limit.md#signal%20processing) for discussion}@}. {@{The product of the standard deviation in time and frequency}@} is {@{limited}@}. {@{The boundary of the uncertainty principle}@} \(best {@{simultaneous resolution of both}@}\) is reached with {@{a Gaussian window function \(or mask function\)}@}, as {@{the Gaussian minimizes the [Fourier uncertainty principle](Fourier%20uncertainty%20principle.md#uncertainty%20principle)}@}. This is called {@{the [Gabor transform](Gabor%20transform.md)}@} \(and with {@{modifications for multiresolution}@} becomes {@{the [Morlet wavelet](Morlet%20wavelet.md) transform}@}\). <!--SR:!2026-05-07,241,330!2025-09-28,72,329!2025-09-29,73,329!2025-09-19,64,310!2025-09-28,72,329!2025-09-29,73,329!2025-10-01,75,329!2025-09-20,65,310!2025-10-01,75,329!2025-10-02,76,329!2025-09-30,74,329-->

One can consider {@{the STFT for varying window size}@} as {@{a two-dimensional domain \(time and frequency\)}@}, as illustrated in the example below, which can be {@{calculated by varying the window size}@}. However, this is {@{no longer a strictly time-frequency representation}@} – the kernel is {@{not constant over the entire signal}@}. <!--SR:!2025-09-19,65,329!2025-09-19,64,310!2025-09-27,71,329!2025-09-28,72,329!2025-10-01,75,329-->

### examples

> {@{![boxcar window function](../../archives/Wikimedia%20Commons/Window%20B.png)}@}
>
> \(annotation: {@{boxcar window function used below}@}\) <!--SR:!2025-10-02,76,329!2025-10-02,76,329-->

When the original function is: {@{$$X(t,f)=\int _{-\infty }^{\infty }w(t-\tau )x(\tau )e^{-j2\pi f\tau }d\tau$$}@} We can have {@{a simple example}@}: <!--SR:!2025-09-30,74,329!2025-09-30,74,329-->

- \(annotation: boxcar window function: within support\) ::@:: w\(t\) = 1 for \|t\| smaller than or equal B <!--SR:!2025-09-21,67,329!2025-09-28,72,329-->
- \(annotation: boxcar window function: outside support\) ::@:: w\(t\) = 0 otherwise <!--SR:!2025-09-16,61,310!2025-10-02,76,329-->
- \(annotation: boxcar window function: parameters\) ::@:: B = window <!--SR:!2026-05-05,239,330!2025-09-21,67,329-->

Now {@{the original function of the Short-time Fourier transform}@} can be changed as {@{$$X(t,f)=\int _{t-B}^{t+B}x(\tau )e^{-j2\pi f\tau }d\tau$$}@} <!--SR:!2025-10-02,76,329!2025-09-26,71,329-->

Another example:

Using {@{the following sample signal $x(t)$}@} that is {@{composed of a set of four sinusoidal waveforms joined together in sequence}@}. Each waveform is {@{only composed of one of four frequencies \(10, 25, 50, 100 [Hz](hertz.md)\)}@}. The definition of $x(t)$ is: {@{$$x(t)={\begin{cases}\cos(2\pi 10t)&0\,\mathrm {s} \leq t<5\,\mathrm {s} \\\cos(2\pi 25t)&5\,\mathrm {s} \leq t<10\,\mathrm {s} \\\cos(2\pi 50t)&10\,\mathrm {s} \leq t<15\,\mathrm {s} \\\cos(2\pi 100t)&15\,\mathrm {s} \leq t<20\,\mathrm {s} \\\end{cases} }$$}@} Then it is {@{sampled at 400 Hz}@}. The following spectrograms were produced: <!--SR:!2025-09-20,66,329!2025-09-30,74,329!2025-09-27,71,329!2025-09-28,72,329!2025-09-23,68,329-->

|                                                                                                                                                |                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| {@{![spectrogram with 25 ms window](../../archives/Wikimedia%20Commons/STFT%20colored%20spectrogram%2025ms.png)}@} <br/> {@{25 ms window}@}    | {@{![spectrogram with 125 ms window](../../archives/Wikimedia%20Commons/STFT%20colored%20spectrogram%20125ms.png)}@} <br/> {@{125 ms window}@}    |
| {@{![spectrogram with 375 ms window](../../archives/Wikimedia%20Commons/STFT%20colored%20spectrogram%20375ms.png)}@} <br/> {@{375 ms window}@} | {@{![spectrogram with 1000 ms window](../../archives/Wikimedia%20Commons/STFT%20colored%20spectrogram%201000ms.png)}@} <br/> {@{1000 ms window}@} | <!--SR:!2025-09-27,71,329!2026-05-12,245,330!2025-10-01,75,329!2026-04-29,234,330!2025-09-21,66,310!2025-09-29,73,329!2025-09-30,74,329!2025-09-29,73,329-->

{@{The 25 ms window}@} allows us to {@{identify a precise time at which the signals change}@} but {@{the precise frequencies are difficult to identify}@}. At {@{the other end of the scale, the 1000 ms window}@} allows {@{the frequencies to be precisely seen}@} but {@{the time between frequency changes is blurred}@}. <!--SR:!2025-09-27,71,329!2025-09-22,67,310!2025-09-26,71,329!2025-09-24,69,329!2025-09-28,72,329!2025-09-26,71,329-->

> {@{![Gaussian window function](../../archives/Wikimedia%20Commons/Gausian%20B.png)}@}
>
> \(annotation: {@{Gaussian window function used below}@}\) <!--SR:!2025-09-29,73,329!2025-09-30,74,329-->

Other examples: {@{$$w(t)=\exp(\sigma -t^{2}) = e^{\sigma} e^{-t^2}$$}@} Normally we call {@{$\exp(\sigma -t^{2})$ a [Gaussian function](Gaussian%20function.md) or Gabor function}@}. When we use it, the short-time Fourier transform is called {@{the "Gabor transform"}@}. <!--SR:!2025-10-02,76,329!2025-10-01,75,329!2025-09-30,74,329-->

### explanation

It can also be explained with reference to {@{the sampling and [Nyquist frequency](Nyquist%20frequency.md)}@}. <!--SR:!2025-09-23,68,329-->

Take {@{a window of _N_ samples from an arbitrary real-valued signal at sampling rate _f_<sub>s</sub>}@}. Taking {@{the Fourier transform}@} produces {@{_N_ complex coefficients}@}. Of these coefficients {@{only half are useful}@} \(the last _N/2_ being {@{the [complex conjugate](complex%20conjugate.md) of the first _N/2_ in reverse order}@}, as {@{this is a real valued signal}@}\). <!--SR:!2025-09-25,70,329!2026-04-26,231,330!2026-05-13,246,330!2025-09-28,72,329!2025-09-29,73,329!2025-09-29,73,329-->

{@{These _N/2_ coefficients}@} represent {@{the frequencies 0 to _f_<sub>s</sub>/2 \(Nyquist\)}@} and {@{two consecutive coefficients}@} are spaced apart by {@{_f_<sub>s</sub>/<!-- markdown separator -->_N_ Hz}@}. <!--SR:!2025-09-30,74,329!2025-09-16,61,310!2025-09-30,74,329!2025-09-21,67,329-->

To {@{increase the frequency resolution of the window}@} {@{the frequency spacing of the coefficients needs to be reduced}@}. There are {@{only two variables}@}, but {@{decreasing _f_<sub>s</sub> \(and keeping _N_ constant\)}@} will cause {@{the window size to increase}@} — since {@{there are now fewer samples per unit time}@}. The other alternative is {@{to increase _N_}@}, but this again causes {@{the window size to increase}@}. So {@{any attempt to increase the frequency resolution}@} causes {@{a larger window size}@} and therefore {@{a reduction in time resolution—and vice versa}@}. <!--SR:!2025-09-29,73,329!2025-10-01,75,329!2025-09-28,72,329!2025-09-30,74,329!2026-04-28,233,330!2025-09-28,72,329!2025-09-28,72,329!2025-10-01,75,329!2025-09-19,65,329!2026-05-18,250,330!2025-09-15,61,310-->

## Rayleigh frequency

As {@{the [Nyquist frequency](Nyquist%20frequency.md) is a limitation in the maximum frequency that can be meaningfully analysed}@}, so is {@{the Rayleigh frequency a limitation on the minimum frequency}@}. <!--SR:!2025-10-02,76,329!2025-09-28,72,329-->

{@{The Rayleigh frequency}@} is {@{the minimum frequency that can be resolved by a finite duration time window}@}.<sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-09-29,73,329!2025-09-27,71,329-->

Given {@{a time window that is Τ seconds long}@}, the minimum frequency {@{that can be resolved is 1/Τ Hz}@}. <!--SR:!2025-09-20,66,329!2025-09-29,73,329-->

The Rayleigh frequency is {@{an important consideration in applications of the short-time Fourier transform \(STFT\)}@}, as well as {@{any other method of harmonic analysis on a signal of finite record-length}@}.<sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-09-22,67,310!2025-09-27,71,329-->

## application

> {@{![An STFT being used to analyze an audio signal across time](../../archives/Wikimedia%20Commons/Short%20time%20fourier%20transform.PNG)}@}
>
> {@{An STFT}@} being used to {@{analyze an audio signal across time}@} <!--SR:!2025-09-21,67,329!2025-09-27,71,329!2025-10-02,76,329-->

STFTs as well as {@{standard Fourier transforms and other tools}@} are frequently used to {@{analyze music}@}. {@{The [spectrogram](spectrogram.md)}@} can, for example, show {@{frequency on the horizontal axis}@}, with {@{the lowest frequencies at left}@}, and {@{the highest at the right}@}. {@{The height of each bar \(augmented by color\)}@} represents {@{the [amplitude](amplitude.md) of the frequencies within that band}@}. {@{The depth dimension}@} represents {@{time}@}, where each new bar was {@{a separate distinct transform}@}. Audio engineers use this kind of visual to {@{gain information about an audio sample}@}, for example, to {@{locate the frequencies of specific noises}@} \(especially when used with {@{greater frequency resolution}@}\) or to find {@{frequencies which may be more or less resonant}@} in {@{the space where the signal was recorded}@}. This information can be used for {@{[equalization](equalization%20(audio).md) or tuning other audio effects}@}. <!--SR:!2025-10-02,76,329!2026-05-13,246,330!2025-09-28,72,329!2026-05-19,251,330!2025-09-14,60,310!2025-09-26,71,329!2025-09-20,66,329!2025-09-27,71,329!2025-09-29,73,329!2025-09-20,66,329!2025-09-17,63,310!2025-09-19,65,329!2025-09-30,74,329!2025-09-27,71,329!2025-09-27,71,329!2025-09-29,73,329!2025-09-26,71,329-->

## implementation

Original function {@{$$X(t,f)=\int _{-\infty }^{\infty }w(t-\tau )x(\tau )e^{-j2\pi f\tau }d\tau$$}@} \(annotation: note the different notations used: {@{the $t$ and $\tau$ have swapped places compared to that used in previous definitions}@}\) <!--SR:!2025-10-01,75,329!2026-05-24,255,330-->

Converting into {@{the discrete form}@}: {@{$$t=n\Delta _{t},f=m\Delta _{f},\tau =p\Delta _{t}$$ <br/> $$X(n\Delta _{t},m\Delta _{f})=\sum _{-\infty }^{\infty }w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f} }\Delta _{t}$$}@} <!--SR:!2025-09-16,62,310!2025-10-02,76,329-->

Suppose that {@{$$w(t)\cong 0{\text{ for } }|t|>B,{\frac {B}{\Delta _{t} } }=Q$$ \(annotation: the window function has finite support around zero\)}@} Then we can write the original function into {@{$$X(n\Delta _{t},m\Delta _{f})=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f} }\Delta _{t}$$}@} <!--SR:!2025-09-28,72,329!2025-11-10,89,270-->

### direct implementation

#### constraints

a. Nyquist criterion \(avoiding the aliasing effect\): <p> ::@:: &emsp; $\Delta _{t}<{\frac {1}{2\Omega } }$, where $\Omega$ is the bandwidth of $x(\tau )w(t-\tau )$ \(annotation: The max frequency is $\Omega$; we need the sampling rate to be twice of it, so sampling duration $\Delta t$ should be less than $1 / 2\Omega$.\) <!--SR:!2025-09-30,74,329!2025-09-25,70,329-->

### FFT-based method

#### constraint

- a. \(annotation: FFT size\) <!-- flashcard ID: 0e8fbcf9-7fc2-461e-8620-d7db321c6dbc -->::@:: $\Delta _{t}\Delta _{f}={\tfrac {1}{N} }$, where $N$ is an integer <!--SR:!2026-05-13,246,330!2025-09-16,62,310-->
- b. \(annotation: non-overlapping\) <!-- flashcard ID: 79e97c91-2df8-4cc5-b134-2683023f6642 -->::@:: $N\geq 2Q+1$ <!--SR:!2026-05-19,251,330!2025-09-29,73,329-->
- c. Nyquist criterion \(avoiding the aliasing effect\): <p> <!-- flashcard ID: dc84b487-1291-4d3f-8168-226cdf907ce4 -->::@:: &emsp; $\Delta _{t}<{\frac {1}{2\Omega } }$, $\Omega$ is the bandwidth of $x(\tau )w(t-\tau )$ \(annotation: The max frequency is $\Omega$; we need the sampling rate to be twice of it, so sampling duration $\Delta t$ should be less than $1 / 2\Omega$.\) <!--SR:!2025-09-28,72,329!2025-10-02,76,329-->

{@{$$X(n\Delta _{t},m\Delta _{f})=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-{\frac {2\pi jpm}{N} } }\Delta _{t}$$}@} If we have {@{$q=p-(n-Q)$, then $p=(n-Q)+q$}@}: {@{$$X(n\Delta _{t},m\Delta _{f})=\Delta _{t}e^{\frac {2\pi j(Q-n)m}{N} }\sum _{q=0}^{N-1}x_{1}(q)e^{-{\frac {2\pi jqm}{N} } } \,,$$}@} where {@{$$x_{1}(q)={\begin{cases}w((Q-q)\Delta _{t})x((n-Q+q)\Delta _{t})&0\leq q\leq 2Q\\0&2Q<q<N\end{cases} }$$}@} \(annotation: The motivation is {@{shifting the zero-center-windowed time signal \(window width is $2Q + 1$\) such that it starts from $q = 0$ to apply FFT}@}.\) <!--SR:!2025-10-02,76,329!2026-01-27,160,310!2025-10-01,75,329!2025-09-30,74,329!2025-10-02,76,329-->

### recursive method

<!-- markdownlint-disable-next-line MD024 -->
#### constraint

- a. \(annotation: FFT size\) <!-- flashcard ID: 02904345-6393-45ca-a915-78eb3426e8c2 -->::@:: $\Delta _{t}\Delta _{f}={\tfrac {1}{N} }$, where $N$ is an integer <!--SR:!2025-10-02,76,329!2025-09-13,59,310-->
- b. \(annotation: non-overlapping\) <!-- flashcard ID: c807688a-c9b1-4c8a-986c-69b1990d5b8d -->::@:: $N\geq 2Q+1$ <!--SR:!2025-09-27,71,329!2025-09-29,73,329-->
- c. Nyquist criterion \(avoiding the aliasing effect\): <p> <!-- flashcard ID: c73ff34f-f78f-4932-aee4-be6c8f463bc3 -->::@:: &emsp; $\Delta _{t}<{\frac {1}{2\Omega } }$, $\Omega$ is the bandwidth of $x(\tau )w(t-\tau )$ \(annotation: The max frequency is $\Omega$; we need the sampling rate to be twice of it, so sampling duration $\Delta t$ should be less than $1 / 2\Omega$.\) <!--SR:!2026-05-03,237,330!2025-09-30,74,329-->
- d. \(annotation: window function constraint\) ::@:: Only for implementing the [rectangular-STFT](Rectangular%20mask%20short-time%20Fourier%20transform.md) <!--SR:!2025-09-29,73,329!2025-09-27,71,329-->

{@{Rectangular window}@} imposes the constraint {@{$$w((n-p)\Delta _{t})=1$$}@} {@{Substitution}@} gives: {@{$${\begin{aligned}X(n\Delta _{t},m\Delta _{f})&=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})&x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N} } }\Delta _{t}\\&=\sum _{p=n-Q}^{n+Q}&x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N} } }\Delta _{t}\\\end{aligned} }$$}@} <!--SR:!2025-10-01,75,329!2025-09-27,71,329!2025-10-01,75,329!2025-09-28,72,329-->

{@{Change of variable _n_-1 for _n_}@}: {@{$$X((n-1)\Delta _{t},m\Delta _{f})=\sum _{p=n-1-Q}^{n-1+Q}x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N} } }\Delta _{t}$$}@} \(annotation: The motivation is {@{expressing $X(n \Delta_t, m \Delta_f)$ in terms of $X((n - 1) \Delta_t, m \Delta_f)$}@}.\) <!--SR:!2025-09-23,68,329!2026-03-14,183,310!2026-01-22,156,310-->

Calculate {@{$X(\min {n}\Delta _{t},m\Delta _{f})$ by the _N_-point FFT}@}: {@{$$X(n_{0}\Delta _{t},m\Delta _{f})=\Delta _{t}e^{\frac {j2\pi (Q-n_{0})m}{N} }\sum _{q=0}^{N-1}x_{1}(q)e^{-j{\frac {2\pi qm}{N} } },\qquad n_{0}=\min {(n)}$$}@} \(annotation: $\min n$ is {@{the index of the first time signal value}@}. This gives {@{the base case}@} for recursion.\) where {@{$$x_{1}(q)={\begin{cases}x((n-Q+q)\Delta _{t})&q\leq 2Q\\0&q>2Q\end{cases} }$$}@} <!--SR:!2025-12-08,110,290!2025-10-18,48,269!2026-01-08,143,309!2025-09-29,73,329!2026-01-31,151,309-->

Applying {@{the recursive formula to calculate $X(n\Delta _{t},m\Delta _{f})$}@}: {@{$$X(n\Delta _{t},m\Delta _{f})=X((n-1)\Delta _{t},m\Delta _{f})-x((n-Q-1)\Delta _{t})e^{-{\frac {j2\pi (n-Q-1)m}{N} } }\Delta _{t}+x((n+Q)\Delta _{t})e^{-{\frac {j2\pi (n+Q)m}{N} } }\Delta _{t}$$}@} \(annotation: The motivation is {@{we can incrementally calculate the results for the current window reusing the results from the previous window}@}. Intuitively, the above equation {@{drops the contribution from the discarded time signal value and adds the contribution from the newly included time signal value}@}.\) <!--SR:!2025-10-01,75,329!2026-02-04,153,309!2025-09-27,71,329!2026-01-22,156,310-->

### chirp Z transform

<!-- markdownlint-disable-next-line MD024 -->
#### constraint

{@{$$\exp {(-j2\pi pm\Delta _{t}\Delta _{f})}=\exp {(-j\pi p^{2}\Delta _{t}\Delta _{f})}\cdot \exp {(j\pi (p-m)^{2}\Delta _{t}\Delta _{f})}\cdot \exp {(-j\pi m^{2}\Delta _{t}\Delta _{f})}$$}@} so {@{$$\begin{aligned} X(n\Delta _{t},m\Delta _{f}) & =\Delta _{t}\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f} } \\ X(n\Delta _{t},m\Delta _{f}) & =\Delta _{t}e^{-j \pi m^{2}\Delta _{t}\Delta _{f} }\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j\pi p^{2}\Delta _{t}\Delta _{f} }e^{j\pi (p-m)^{2}\Delta _{t}\Delta _{f} } \end{aligned}$$}@} <!--SR:!2025-09-20,65,310!2025-11-24,98,289-->

### implementation comparison

\(annotation: Below, notations include: {@{$T$ is time signal length, $F$ is number of frequencies, $Q$ is \(about half of\) bucket length, and $N$ is FFT size}@}.\) <!--SR:!2025-10-02,76,329-->

| Method                | Complexity        |
| --------------------- | ----------------- |
| Direct implementation | $O(TFQ)$          |
| FFT-based             | $O(TN\log _{2}N)$ |
| Recursive             | $O(TF)$           |
| Chirp Z transform     | $O(TN\log _{2}N)$ |

> __flashcards__
>
> - direct implementation ::@:: $O(TFQ)$ \(annotation: For each time value and frequency, $2Q+1$ multiplications are needed.\) <!--SR:!2025-09-14,60,310!2025-09-25,70,329-->
> - FFT-based ::@:: $O(TN\log _{2}N)$ \(annotation: Each time value requires a FFT. FFT gives the $F$ frequencies directly, and has a complexity of $N \log_2 N$.\) <!--SR:!2025-10-02,76,329!2025-09-30,74,329-->
> - recursive ::@:: $O(TF)$ \(annotation: Once the base case is calculated, for each time value and frequency, only 2 multiplications are needed.\) <!--SR:!2025-10-01,75,329!2025-10-02,76,329-->
> - chirp Z-transform ::@:: $O(TN\log _{2}N)$ \(annotation: It is a generalization of DFT, and can be evaluated efficiently using FFT.\) <!--SR:!2025-09-27,71,329!2025-09-20,65,310-->

## see also

- [Least-squares spectral analysis](least-squares%20spectral%20analysis.md)
- [Spectral density estimation](spectral%20density%20estimation.md)
- [Time-frequency analysis](time-frequency%20analysis.md)
- [Time-frequency representation](time-frequency%20representation.md)
- [Reassignment method](reassignment%20method.md)

Other time-frequency transforms:

- [Cone-shape distribution function](cone-shape%20distribution%20function.md)
- [Constant-Q transform](constant-Q%20transform.md)
- [Fractional Fourier transform](fractional%20Fourier%20transform.md)
- [Gabor transform](Gabor%20transform.md)
- [Newland transform](Newland%20transform.md)
- [S transform](S%20transform.md)
- [Wavelet transform](wavelet%20transform.md)
- [Chirplet transform](chirplet%20transform.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/short-time_Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFSejdić E.Djurović I.Jiang J.2009"></a> Sejdić E.; Djurović I.; Jiang J. \(2009\). "Time-frequency feature representation using energy concentration: An overview of recent advances". _Digital Signal Processing_. __19__ \(1\): 153–183. [Bibcode](bibcode%20(identifier).md):[2009DSP....19..153S](https://ui.adsabs.harvard.edu/abs/2009DSP....19..153S). [doi](doi%20(identifier).md):[10.1016/j.dsp.2007.12.004](https://doi.org/10.1016%2Fj.dsp.2007.12.004). <a id="^ref-1"></a>^ref-1
2. E. Jacobsen and R. Lyons, [The sliding DFT](https://ieeexplore.ieee.org/document/1184347/;jsessionid=4C7542A520E95FD20371713367DD1C7F?arnumber=1184347), _Signal Processing Magazine_ vol. 20, issue 2, pp. 74–80 \(March 2003\). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFJont B. Allen1977"></a> Jont B. Allen \(June 1977\). "Short Time Spectral Analysis, Synthesis, and Modification by Discrete Fourier Transform". _IEEE Transactions on Acoustics, Speech, and Signal Processing_. ASSP-25 \(3\): 235–238. [doi](doi%20(identifier).md):[10.1109/TASSP.1977.1162950](https://doi.org/10.1109%2FTASSP.1977.1162950). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFKleinfeldMitra2014"></a> Kleinfeld, David; Mitra, Partha P. \(March 2014\). ["Spectral methods for functional brain imaging"](https://scholar.archive.org/work/ofowcbyne5gdpbtmogxvpdp5au). _Cold Spring Harbor Protocols_. __2014__ \(3\): 248–262. [doi](doi%20(identifier).md):[10.1101/pdb.top081075](https://doi.org/10.1101%2Fpdb.top081075). [PMID](PMID%20(identifier).md#PubMed%20identifier) [24591695](https://pubmed.ncbi.nlm.nih.gov/24591695). <a id="^ref-4"></a>^ref-4
5. ["What does "padding not sufficient for requested frequency resolution" mean? – FieldTrip toolbox"](http://fieldtrip.fcdonders.nl/faq/what_does_padding_not_sufficient_for_requested_frequency_resolution_mean). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFZeitlerFriesGielen2008"></a> Zeitler M, Fries P, Gielen S \(2008\). ["Biased competition through variations in amplitude of gamma-oscillations"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2441488). _J Comput Neurosci_. __25__ \(1\): 89–107. [doi](doi%20(identifier).md):[10.1007/s10827-007-0066-2](https://doi.org/10.1007%2Fs10827-007-0066-2). [PMC](PMC%20(identifier).md#PMCID) [2441488](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2441488). [PMID](PMID%20(identifier).md#PubMed%20identifier) [18293071](https://pubmed.ncbi.nlm.nih.gov/18293071). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFWingerdenVinckLankelmaPennartz2010"></a> Wingerden, Marijn van; Vinck, Martin; Lankelma, Jan; [Pennartz, Cyriel M. A.](Cyriel%20Pennartz.md) \(2010-05-19\). ["Theta-Band Phase Locking of Orbitofrontal Neurons during Reward Expectancy"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6632657). _Journal of Neuroscience_. __30__ \(20\): 7078–7087. [doi](doi%20(identifier).md):[10.1523/JNEUROSCI.3860-09.2010](https://doi.org/10.1523%2FJNEUROSCI.3860-09.2010). [ISSN](ISSN%20(identifier).md) [0270-6474](https://search.worldcat.org/issn/0270-6474). [PMC](PMC%20(identifier).md#PMCID) [6632657](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6632657). [PMID](PMID%20(identifier).md#PubMed%20identifier) [20484650](https://pubmed.ncbi.nlm.nih.gov/20484650). <a id="^ref-7"></a>^ref-7

## external links

- [DiscreteTFDs – software for computing the short-time Fourier transform and other time-frequency distributions](http://tfd.sourceforge.net/)
- [Singular Spectral Analysis – MultiTaper Method Toolkit](http://www.atmos.ucla.edu/tcd/ssa/) – a free software program to analyze short, noisy time series
- [kSpectra Toolkit for Mac OS X from SpectraWorks](http://www.spectraworks.com/)
- [Time stretched short time Fourier transform for time frequency analysis of ultra wideband signals](https://www.researchgate.net/publication/3091384_Time-stretched_short-time_Fourier_transform)
- [A BSD-licensed Matlab class to perform STFT and inverse STFT](http://www.mathworks.fr/matlabcentral/fileexchange/33451-stft-mdct-and-inverses-onset-and-pitch-detection)
- [LTFAT – A free \(GPL\) Matlab / Octave toolbox to work with short-time Fourier transforms and time-frequency analysis](http://ltfat.sourceforge.net/)
- [Sonogram visible speech – A free \(GPL\)Freeware for short-time Fourier transforms and time-frequency analysis](https://github.com/Christoph-Lauer/Sonogram)
- [National Taiwan University, Time-Frequency Analysis and Wavelet Transform 2021, Professor of Jian-Jiun Ding, Department of Electrical Engineering](http://djj.ee.ntu.edu.tw/TFW_Writing1.pdf)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Fourier analysis](https://en.wikipedia.org/wiki/Category:Fourier%20analysis)
> - [Time–frequency analysis](https://en.wikipedia.org/wiki/Category:Time%E2%80%93frequency%20analysis)
> - [Transforms](https://en.wikipedia.org/wiki/Category:Transforms)
> - [Signal processing](https://en.wikipedia.org/wiki/Category:Signal%20processing)
