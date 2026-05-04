---
aliases:
  - ELEC 2100 lab 3 prelab
  - HKUST ELEC 2100 lab 3 prelab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_3/prelab
  - language/in/English
---

# prelab

- HKUST ELEC 2100 lab 3
- parent: [lab 3](index.md)

---

For the broader Fourier and system theory, see [Fourier series](../../Fourier%20series.md), [discrete Fourier transform](../../discrete%20Fourier%20transform.md), and [frequency response](../../frequency%20response.md).  The sections below keep the prelab on preparation-stage MATLAB habits and frequency-domain reading, without stepping into the solved assignment results.

## sampled audio records and time index

Before any FFT plot is meaningful, the sampled record has to be placed on a clear time grid.  The usual setup is to read the waveform, count the samples, and convert sample positions into seconds:

```matlab
[x, fs] = audioread("sample3a.wav");
N = numel(x);
t = (0:N-1) / fs;
plot(t, x)
```

That habit matters because later comparisons among waveform plots, filtered outputs, and reconstructed models are easiest to read when they all use the same physical time axis instead of switching back and forth between seconds and raw sample indices.

---

Flashcards for this section are as follows:

- In the Lab 3 MATLAB setup `[x, fs] = audioread("sample3a.wav"); N = numel(x); t = (0:N-1) / fs;`, why is the time vector `t` built immediately instead of waiting until later plots? ::@:: Because the sampled record is much easier to interpret when every later time-domain plot uses the same physical axis in seconds rather than a mix of raw sample indices and elapsed time. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
- In the Lab 3 MATLAB definition `t = (0:N-1) / fs`, what do the numerator and denominator each contribute to the physical interpretation? ::@:: The numerator lists the sample positions in order, and dividing by `fs` converts those positions from sample counts into elapsed time values in seconds. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->

## fft scaling and coefficient meaning

The corresponding theory already lives in [discrete Fourier transform § relation between DTFS and DFT](../../discrete%20Fourier%20transform.md#relation-between-dtfs-and-dft), [discrete Fourier transform § normalization map between DTFS and DFT](../../discrete%20Fourier%20transform.md#normalization-map-between-dtfs-and-dft), and [Fourier series § spectrum concept and frequency-domain viewpoint](../../Fourier%20series.md#spectrum-concept-and-frequency-domain-viewpoint).  The finite-record interpretation $X[k] = \frac{1}{N}\operatorname{fft}(x)[k]$ puts MATLAB's FFT output on the same coefficient scale used for one-period Fourier-series-style reading.

```matlab
N = length(x);
Xk = fft(x) / N;
Xkp = angle(Xk) .* (abs(Xk) > 0.001);
plot(f, abs(Xk))
```

One closely related caution is that a spectral component with extremely small magnitude does not carry a physically stable phase.  Tiny numerical noise can rotate a near-zero complex number by a large angle, so phase has to be interpreted together with magnitude rather than in isolation.  The thresholded angle line `Xkp = angle(Xk) .* (abs(Xk) > 0.001)` is therefore not cosmetic; it is a way to keep the phase plot focused on bins that actually carry signal energy.

---

Flashcards for this section are as follows:

- In the Lab 3 MATLAB line `Xkp = angle(Xk) .* (abs(Xk) > 0.001)`, why is the phase array multiplied by a magnitude mask before plotting? ::@:: Because a bin with negligible magnitude does not have a reliable physical phase, so the mask suppresses angle values that are dominated by numerical noise rather than by meaningful signal content. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
- In the MATLAB fragment `Xk = fft(x)/length(x)`, why is the FFT divided by the record length $N$? ::@:: Because that scaling converts MATLAB's raw FFT sum into a coefficient scale that matches one-record Fourier-series-style interpretation. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- In the MATLAB fragment `Xk = fft(x)/length(x)`, what does the specific denominator `length(x)` represent physically? ::@:: It is the number of samples in the analyzed record, so dividing by it converts the raw FFT sum into a coefficient scale that matches one-record Fourier interpretation. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->

## centered spectra and frequency axes

The DFT ordering theory already lives in [discrete Fourier transform § principal value interval extraction](../../discrete%20Fourier%20transform.md#principal-value-interval-extraction) and [Fourier series § spectrum concept and frequency-domain viewpoint](../../Fourier%20series.md#spectrum-concept-and-frequency-domain-viewpoint).  MATLAB's display convention puts the zero-frequency bin first and wraps the negative-frequency bins to the far end, while `fftshift` rotates the output so the spectrum is visually centered at DC.  For an even-length record sampled at frequency $f_s$, the centered grid is naturally written as $f_k = \left(-\frac{N}{2},\,-\frac{N}{2}+1,\,\dots,\,\frac{N}{2}-1\right)\frac{f_s}{N}$.

```matlab
N = length(x);
f_shift = (-N/2:N/2-1) * fs/N;
plot(f_shift, fftshift(abs(Xk)))
```

The point is interpretive rather than cosmetic.  A centered axis turns the FFT output from a modulo-$N$ bin list into a readable frequency-domain picture.  It also lets negative-frequency and positive-frequency components be compared around DC in the same visual frame, which makes symmetry and conjugate-pair structure much easier to notice.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `plot(f_shift, fftshift(abs(Xk)))`, why is `fftshift` used before the magnitude spectrum is read? ::@:: Because MATLAB's raw FFT output is ordered with DC first and negative frequencies wrapped to the far end, so `fftshift` recenters the bins around zero frequency and makes the spectrum physically readable. <!--SR:!2026-05-14,16,290!2026-05-14,16,297-->
- When the MATLAB code plots `fftshift(abs(Xk))`, what frequency grid must be paired with it for an even-length record? ::@:: It must be paired with a centered grid such as `(-N/2:N/2-1) * fs/N`, so each shifted FFT bin is shown at its correct physical frequency. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- In the MATLAB fragment `f_shift = (-N/2:N/2-1) * fs/N`, why does the factor `fs/N` convert bin numbers into physical frequency? ::@:: Because adjacent DFT bins are separated by one cycle per record, which equals `fs/N` hertz for a record of `N` samples taken at sampling rate `fs`. <!--SR:!2026-05-14,16,290!2026-05-14,16,297-->
- For the MATLAB plot `plot(f_shift, fftshift(abs(Xk)))` with an even-length record of length $N$ sampled at frequency $f_s$, what centered frequency grid matches `fftshift`? ::@:: A natural centered grid is $f_k = \left(-N/2,\,-N/2+1,\,\dots,\,N/2-1\right)f_s/N$, which places the shifted bins at the correct negative-to-positive frequencies. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- In the Lab 3 centered-spectrum workflow, why is `fftshift` especially helpful for spotting conjugate symmetry of a real-valued record? ::@:: Because after centering, the negative-frequency and positive-frequency bins appear on opposite sides of zero frequency in one symmetric picture, so mirrored magnitude structure is much easier to recognize. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->

## normalized low-pass and band-pass specifications

The corresponding system theory already lives in [frequency response § magnitude response and phase response](../../frequency%20response.md#magnitude-response-and-phase-response), [frequency response § ways to determine the system function](../../frequency%20response.md#ways-to-determine-the-system-function), and [frequency response § ideal low-pass, high-pass, and band-pass filters](../../frequency%20response.md#ideal-low-pass-high-pass-and-band-pass-filters).  The prelab habit is to convert a filter idea stated in hertz into the normalized digital format expected by MATLAB.

```matlab
Wlow = flow * 2 / fs;
Wband = [flow fhigh] * 2 / fs;
[Blow, Alow] = butter(6, Wlow);
[Bband, Aband] = butter(6, Wband);
[Hband, fh] = freqz(Bband, Aband, 1e3, fs);
plot(fh, abs(Hband))
```

The key idea is the move from a qualitative goal—keep low frequencies, or isolate one band—to an implementable filter whose passband and stopband behavior can be checked directly.

In this MATLAB form, every cutoff is normalized relative to the Nyquist frequency $f_s/2$.  A scalar cutoff produces a low-pass or high-pass design, while a two-entry vector produces a band-pass or band-stop design.  So the design command is already encoding a frequency-domain specification, not just producing unexplained coefficients.

---

Flashcards for this section are as follows:

- In the Lab 3 MATLAB normalization `Wlow = flow * 2 / fs`, why is the physical cutoff multiplied by `2 / fs` before being passed to `butter`? ::@:: Because MATLAB expects the cutoff in units normalized by the Nyquist frequency, so multiplying by `2 / fs` converts a cutoff expressed in hertz into the digital frequency scale required by the design function. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
- In the Lab 3 MATLAB normalization `Wband = [flow fhigh] * 2 / fs`, what does the two-entry vector mean conceptually before MATLAB ever computes coefficients? ::@:: It means the filter should preserve the band between `flow` and `fhigh` while attenuating frequencies below the lower edge and above the upper edge. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
- In the MATLAB pair `[Bband, Aband] = butter(6, Wband)` and `[Hband, fh] = freqz(Bband, Aband, 1e3, fs)`, why are `butter` and `freqz` used together? ::@:: `butter` turns the desired qualitative filtering goal into actual filter coefficients, and `freqz` then reveals the frequency response of that designed filter so the coefficients can be interpreted. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
- In this MATLAB filter-design context, what conceptual difference between low-pass and band-pass filtering is being made concrete? ::@:: Low-pass filtering is used to preserve spectral content near DC, whereas band-pass filtering preserves only a selected middle-frequency band and suppresses content outside that band. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->

## filtered signals in time and frequency

The final idea is consistency between domains.  A filter should be interpreted before and after application in both the time domain and the frequency domain.  If low-frequency content dominates after low-pass filtering, the waveform often becomes smoother in time and less rich in high-frequency detail.  If a band-pass filter isolates one region, the output should sound or look more concentrated around the chosen spectral band.

```matlab
y1 = filter(B1, A1, x);
Y1 = fft(y1)/length(y1);
plot(f_shift, fftshift(abs(Y1)))
```

The important idea is that a filtered output is understood only when the observed result matches the spectral change predicted by the filter response.

---

Flashcards for this section are as follows:

- In the MATLAB workflow `y1 = filter(B1, A1, x); Y1 = fft(y1)/length(y1); plot(f_shift, fftshift(abs(Y1)))`, why must the signal be compared before and after filtering in both time and frequency? ::@:: Because the filtered output is fully understood only when the time-domain change and the new spectrum agree with the filter behavior predicted by the frequency response. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- In the MATLAB fragment `y1 = filter(B1, A1, x)`, why is filtering not the end of the story in the prelab? ::@:: Because the resulting waveform still has to be examined in the frequency domain to verify that the observed attenuation or passband behavior matches what `freqz` predicted. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- In the MATLAB fragment `y1 = filter(B1, A1, x); Y1 = fft(y1)/length(y1);`, why is the FFT specifically taken again on the filtered output `y1`? ::@:: Because the filtered signal must be re-expressed in the frequency domain to verify that its spectrum matches the attenuation or passband behavior predicted by the filter response. <!--SR:!2026-05-14,16,297!2026-05-14,16,297-->
- When the MATLAB code applies a successful low-pass filter and then inspects the output in time, what kind of time-domain change should usually be seen? ::@:: The waveform should usually look smoother and less rapidly varying, because the high-frequency components that cause fast oscillation have been attenuated. <!--SR:!2026-05-14,16,290!2026-05-14,16,297-->
- In a Lab 3 prelab workflow that compares `x`, `y1`, `Xk`, and `Y1`, why is it useful to inspect both waveform plots and spectra instead of trusting only one domain? ::@:: Because the filter's meaning is fully checked only when the time-domain simplification and the frequency-domain attenuation pattern agree with each other. <!--SR:!2026-05-15,17,309!2026-05-15,17,309-->
