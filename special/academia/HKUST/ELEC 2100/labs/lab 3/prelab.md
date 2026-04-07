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

For the broader Fourier and system theory, see [Fourier series](../../Fourier%20series.md), [discrete Fourier transform](../../discrete%20Fourier%20transform.md), and [frequency response](../../frequency%20response.md).  The sections below focus on what becomes clearest when FFT outputs and filter responses are read directly.

## fft scaling and coefficient meaning

The corresponding theory already lives in [discrete Fourier transform § relation between DTFS and DFT](../../discrete%20Fourier%20transform.md#relation-between-dtfs-and-dft), [discrete Fourier transform § normalization map between DTFS and DFT](../../discrete%20Fourier%20transform.md#normalization-map-between-dtfs-and-dft), and [Fourier series § spectrum concept and frequency-domain viewpoint](../../Fourier%20series.md#spectrum-concept-and-frequency-domain-viewpoint).  The finite-record interpretation $X[k] = \frac{1}{N}\operatorname{fft}(x)[k]$ puts MATLAB's FFT output on the same coefficient scale used for one-period Fourier-series-style reading.

```matlab
Xk = fft(x)/length(x);
Xkp = angle(Xk) .* (abs(Xk) > 0.001);
plot(f, abs(Xk))
```

One closely related caution is that a spectral component with extremely small magnitude does not carry a physically stable phase.  Tiny numerical noise can rotate a near-zero complex number by a large angle, so phase has to be interpreted together with magnitude rather than in isolation.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `Xk = fft(x)/length(x)`, why is the FFT divided by the record length $N$? ::@:: Because that scaling converts MATLAB's raw FFT sum into a coefficient scale that matches one-record Fourier-series-style interpretation.
- In the MATLAB fragment `Xk = fft(x)/length(x)`, what does the specific denominator `length(x)` represent physically? ::@:: It is the number of samples in the analyzed record, so dividing by it converts the raw FFT sum into a coefficient scale that matches one-record Fourier interpretation.

## centered spectra and frequency axes

The DFT ordering theory already lives in [discrete Fourier transform § principal value interval extraction](../../discrete%20Fourier%20transform.md#principal-value-interval-extraction) and [Fourier series § spectrum concept and frequency-domain viewpoint](../../Fourier%20series.md#spectrum-concept-and-frequency-domain-viewpoint).  MATLAB's display convention puts the zero-frequency bin first and wraps the negative-frequency bins to the far end, while `fftshift` rotates the output so the spectrum is visually centered at DC.  For an even-length record sampled at frequency $f_s$, the centered grid is naturally written as $f_k = \left(-\frac{N}{2},\,-\frac{N}{2}+1,\,\dots,\,\frac{N}{2}-1\right)\frac{f_s}{N}$.

```matlab
N = length(x);
f_shift = (-N/2:N/2-1) * fs/N;
plot(f_shift, fftshift(abs(Xk)))
```

The point is interpretive rather than cosmetic.  A centered axis turns the FFT output from a modulo-$N$ bin list into a readable frequency-domain picture.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `plot(f_shift, fftshift(abs(Xk)))`, why is `fftshift` used before the magnitude spectrum is read? ::@:: Because MATLAB's raw FFT output is ordered with DC first and negative frequencies wrapped to the far end, so `fftshift` recenters the bins around zero frequency and makes the spectrum physically readable. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- When the MATLAB code plots `fftshift(abs(Xk))`, what frequency grid must be paired with it for an even-length record? ::@:: It must be paired with a centered grid such as `(-N/2:N/2-1) * fs/N`, so each shifted FFT bin is shown at its correct physical frequency.
- In the MATLAB fragment `f_shift = (-N/2:N/2-1) * fs/N`, why does the factor `fs/N` convert bin numbers into physical frequency? ::@:: Because adjacent DFT bins are separated by one cycle per record, which equals `fs/N` hertz for a record of `N` samples taken at sampling rate `fs`. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- For the MATLAB plot `plot(f_shift, fftshift(abs(Xk)))` with an even-length record of length $N$ sampled at frequency $f_s$, what centered frequency grid matches `fftshift`? ::@:: A natural centered grid is $f_k = \left(-N/2,\,-N/2+1,\,\dots,\,N/2-1\right)f_s/N$, which places the shifted bins at the correct negative-to-positive frequencies.

## butterworth filters and frequency response

The corresponding system theory already lives in [frequency response § magnitude response and phase response](../../frequency%20response.md#magnitude-response-and-phase-response), [frequency response § ways to determine the system function](../../frequency%20response.md#ways-to-determine-the-system-function), and [frequency response § ideal low-pass, high-pass, and band-pass filters](../../frequency%20response.md#ideal-low-pass-high-pass-and-band-pass-filters).  Here `butter` and `freqz` connect a qualitative filtering goal directly to an inspectable frequency response.

```matlab
[B1, A1] = butter(6, 0.04);
[H1, fh] = freqz(B1, A1, 1e3, fs);
plot(fh, abs(H1))
```

The key idea is the move from a qualitative goal—keep low frequencies, or isolate one band—to an implementable filter whose passband and stopband behavior can be checked directly.

In this MATLAB form, the cutoff `0.04` is a normalized digital frequency measured relative to the Nyquist frequency.  So the design command is already encoding a frequency-domain specification, not just producing unexplained coefficients.

---

Flashcards for this section are as follows:

- In the MATLAB pair `[B1, A1] = butter(6, 0.04)` and `[H1, fh] = freqz(B1, A1, 1e3, fs)`, why are `butter` and `freqz` used together? ::@:: `butter` turns the desired qualitative filtering goal into actual filter coefficients, and `freqz` then reveals the frequency response of that designed filter so the coefficients can be interpreted.
- After the MATLAB design step `[B1, A1] = butter(6, 0.04)`, what does `freqz(B1, A1, 1e3, fs)` add? ::@:: It evaluates the designed filter on a physical frequency axis, so the passband and stopband behavior can be checked directly instead of guessed from the coefficients alone.
- In the MATLAB fragment `[B1, A1] = butter(6, 0.04)`, what does the specific number `0.04` mean on the left-hand side of that filter design? ::@:: It is the normalized cutoff frequency relative to the Nyquist frequency, so it specifies where the Butterworth transition should occur on the digital frequency axis. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- In this MATLAB filter-design context, what conceptual difference between low-pass and band-pass filtering is being made concrete? ::@:: Low-pass filtering is being used to preserve spectral content near DC, whereas band-pass filtering would preserve only a selected middle-frequency band and suppress content outside that band.

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

- In the MATLAB workflow `y1 = filter(B1, A1, x); Y1 = fft(y1)/length(y1); plot(f_shift, fftshift(abs(Y1)))`, why must the signal be compared before and after filtering in both time and frequency? ::@:: Because the filtered output is fully understood only when the time-domain change and the new spectrum agree with the filter behavior predicted by the frequency response.
- In the MATLAB fragment `y1 = filter(B1, A1, x)`, why is filtering not the end of the story in the prelab? ::@:: Because the resulting waveform still has to be examined in the frequency domain to verify that the observed attenuation or passband behavior matches what `freqz` predicted.
- In the MATLAB fragment `y1 = filter(B1, A1, x); Y1 = fft(y1)/length(y1);`, why is the FFT specifically taken again on the filtered output `y1`? ::@:: Because the filtered signal must be re-expressed in the frequency domain to verify that its spectrum matches the attenuation or passband behavior predicted by the filter response.
- When the MATLAB code applies a successful low-pass filter and then inspects the output in time, what kind of time-domain change should usually be seen? ::@:: The waveform should usually look smoother and less rapidly varying, because the high-frequency components that cause fast oscillation have been attenuated. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
