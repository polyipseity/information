---
aliases:
  - ELEC 2100 lab 3 assignment
  - ELEC 2100 lab 3 lab
  - HKUST ELEC 2100 lab 3 assignment
  - HKUST ELEC 2100 lab 3 lab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_3/lab
  - language/in/English
---

# lab

- HKUST ELEC 2100 lab 3
- parent: [lab 3](index.md)

---

For the shared Fourier-series coefficient and filter theory, see [Fourier series](../../Fourier%20series.md), [discrete Fourier transform](../../discrete%20Fourier%20transform.md), and [frequency response](../../frequency%20response.md).  The sections below keep only the lab-specific peak-reading, cosine-reconstruction, and Butterworth-interpretation habits that are clearest in Lab 3 itself.

## thresholded spectral lines and reliable phase reading

The assignment works with the sampled audio file `sample3a.wav` and computes Fourier-series-style coefficients on the sample record itself.  The archived MATLAB solution uses

```matlab
sample3a_f = fft(sample3a) ./ N;
sample3a_f = sample3a_f .* (abs(sample3a_f) > 0.001);
f_idx = ((0:N-1) - floor(N/2)) .* fs ./ N;
plot(f_idx, fftshift(angle(sample3a_f)))
```

The division by `N` puts the FFT output on the coefficient scale used throughout the course for one-period Fourier reading.  The extra magnitude threshold is a lab-specific plotting habit: a phase angle is only worth interpreting when the corresponding spectral line is materially present.  For bins whose magnitude is effectively zero, the angle can jump wildly because numerical noise rotates tiny complex numbers by large apparent phases.

In this file the sampling rate is $f_s = 100000\,\text{Hz}$ and the record length is $N = 100000$, so the spacing between adjacent DFT bins is exactly $f_s/N = 1\,\text{Hz}$.  That makes the shifted peak locations readable directly in hertz.

---

Flashcards for this section are as follows:

- Why should a phase plot of FFT coefficients be masked by a magnitude threshold before angles are interpreted? ::@:: Because bins with nearly zero magnitude do not carry a stable physical phase, so the threshold suppresses meaningless angle values caused mainly by numerical noise. <!--SR:!2026-05-06,15,290!2026-05-06,14,290-->
- For an FFT coefficient table computed as `fft(sample) ./ N`, why divide by the record length before reading amplitudes and phases? ::@:: Because the raw FFT sum has to be normalized by the record length so that the spectral lines can be interpreted on the same Fourier-series-style coefficient scale used in the course notes. <!--SR:!2026-05-06,14,290!2026-05-06,15,290-->
- If a centered DFT frequency axis is built as `((0:N-1) - floor(N/2)) .* fs ./ N` and a record has $f_s = N = 100000$, why are the spectral peaks readable directly in hertz? ::@:: Because the bin spacing is $f_s/N = 1\,\text{Hz}$, so each shifted DFT bin already lines up with an integer-hertz frequency label. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->

## fundamental frequency from the common divisor of visible tones

After the shifted magnitude spectrum is plotted, the visible positive-frequency lines occur at about $400\,\text{Hz}$, $5000\,\text{Hz}$, and $16000\,\text{Hz}$.  The archived submission then identifies the fundamental frequency as the greatest common divisor of those line frequencies: $400 = 2 \cdot 200$, $5000 = 25 \cdot 200$, and $16000 = 80 \cdot 200$.

So the waveform is periodic with fundamental frequency $f_0 = 200\,\text{Hz}$ even though the $200\,\text{Hz}$ line itself is absent.  This is the useful lab habit: the fundamental does not have to appear as the lowest nonzero plotted tone.  It can instead be inferred from the harmonic spacing of the tones that are present.

The same picture is reflected in the reported positive-frequency Fourier-series indices $k = 2, 25, 80$, since those are exactly the harmonic numbers relative to $f_0 = 200\,\text{Hz}$.

---

Flashcards for this section are as follows:

- A spectrum has visible positive-frequency lines at $400\,\text{Hz}$, $5000\,\text{Hz}$, and $16000\,\text{Hz}$. Why can the fundamental still be $200\,\text{Hz}$ even though $200\,\text{Hz}$ is absent? ::@:: Because the three visible lines are all integer multiples of $200\,\text{Hz}$, so $200\,\text{Hz}$ is their greatest common divisor and therefore the true fundamental spacing even though that line itself is missing. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- What general caution does this illustrate about identifying a fundamental from a magnitude spectrum? ::@:: The fundamental frequency of a periodic signal need not appear as the lowest visible nonzero line, because it can be absent while its harmonics are still present. <!--SR:!2026-05-07,16,290!2026-05-06,14,290-->
- If $f_0 = 200\,\text{Hz}$ and the visible tones are $400\,\text{Hz}$, $5000\,\text{Hz}$, and $16000\,\text{Hz}$, what do harmonic numbers $k = 2, 25, 80$ mean? ::@:: They mean the visible tones are the second, twenty-fifth, and eightieth harmonics of the same periodic signal. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->

## real-cosine reconstruction from positive-frequency coefficients

The archived submission records the positive-frequency coefficients as $|X_2| = 0.1$ with $\angle X_2 = -\pi/2$, $|X_{25}| = 0.15$ with $\angle X_{25} = -\pi/4$, and $|X_{80}| = 0.2$ with $\angle X_{80} = 0$.

For a real signal, every positive-frequency coefficient has a conjugate partner at the corresponding negative frequency.  So one positive-frequency line with magnitude $|X_k|$ and phase $\phi_k$ contributes the real cosine term $2|X_k|\cos(2\pi f_k t + \phi_k)$.  Applying that rule to the three reported lines gives $\mathrm{sample3a}(t) = 0.2\cos(800\pi t - \pi/2) + 0.3\cos(10000\pi t - \pi/4) + 0.4\cos(32000\pi t)$.

The archived MATLAB comparison starts from the original sample grid, using `[sample3a, fs] = audioread("sample3a.wav")`, `N = numel(sample3a)`, and `t_idx = (0:N-1) ./ fs`, then reconstructs those three tones directly on that same grid and plots the first $800$ points against the recorded waveform:

```matlab
sample3a_math = 0.2*cos(800*pi*t_idx - pi/2) ...
             + 0.3*cos(10000*pi*t_idx - pi/4) ...
             + 0.4*cos(32000*pi*t_idx);
plot(t_idx(1:800), sample3a_math(1:800))
```

That check is not just cosmetic.  It verifies that the peak magnitudes, phases, and harmonic labels have been translated back into a time-domain expression consistently.

---

Flashcards for this section are as follows:

- For a real signal, why does a positive-frequency coefficient with magnitude $|X_k| = 0.15$ produce a cosine amplitude $0.3$ after reconstruction? ::@:: Because a real signal contains equal positive- and negative-frequency conjugate partners, so the pair combines into one real cosine with amplitude $2|X_k| = 0.3$. <!--SR:!2026-05-05,14,290!2026-05-08,16,290-->
- If a positive-frequency coefficient at $5000\,\text{Hz}$ has phase $-\pi/4$, how does that phase appear in the reconstructed real cosine term? ::@:: It reappears directly as the phase term of the corresponding cosine, so the $5000\,\text{Hz}$ component becomes $0.3\cos(10000\pi t - \pi/4)$. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->
- Why should a reconstructed cosine sum be evaluated on the same sample grid `t_idx = (0:N-1) ./ fs` as the recorded waveform before the two are compared? ::@:: Because the point-by-point comparison is only meaningful if the reconstructed cosine sum and the original sample record are placed on exactly the same time grid. <!--SR:!2026-05-07,15,290!2026-05-06,15,290-->
- What does a point-by-point comparison between the original samples and the reconstructed cosine sum actually check? ::@:: It checks that the spectral peak reading, harmonic identification, and phase extraction have been converted back into a time-domain model without a scaling or alignment mistake. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->

<!-- check: ignore-next-line[header_style]: Butterworth is a proper noun -->
## Butterworth band-pass cutoffs chosen from the spectrum

Part II asks for a Butterworth band-pass filter that completely removes the lowest and highest visible tones while preserving the middle one.  Since the three detected spectral lines are at $400\,\text{Hz}$, $5000\,\text{Hz}$, and $16000\,\text{Hz}$, the archived submission chooses $f_{\mathrm{low}} = 2700\,\text{Hz}$ and $f_{\mathrm{high}} = 10500\,\text{Hz}$, which puts $400\,\text{Hz}$ well below the passband, $16000\,\text{Hz}$ well above it, and $5000\,\text{Hz}$ inside it.

The corresponding MATLAB realization is

```matlab
[b, a] = butter(8, [2700 * 2 / fs, 10500 * 2 / fs]);
[h, w] = freqz(b, a, fs / 2, fs);
```

The factor `2 / fs` converts the physical cutoff frequencies into the normalized digital frequencies expected by `butter`, where $1$ corresponds to the Nyquist frequency $f_s/2$.  The call to `freqz` samples the response directly on a frequency axis measured in hertz, so the response can be queried at the same tone frequencies that were found in the spectrum.

---

Flashcards for this section are as follows:

- A signal has unwanted tones at $400\,\text{Hz}$ and $16000\,\text{Hz}$ and a desired tone at $5000\,\text{Hz}$. Why are cutoffs such as $2700\,\text{Hz}$ and $10500\,\text{Hz}$ reasonable for a band-pass Butterworth design? ::@:: Because they place the unwanted $400\,\text{Hz}$ and $16000\,\text{Hz}$ components outside the passband while keeping the desired $5000\,\text{Hz}$ component inside the passband. <!--SR:!2026-05-07,16,290!2026-05-08,16,290-->
- Why does MATLAB's `butter` call use cutoff frequencies in the form `2f_c/fs` rather than raw hertz? ::@:: Because MATLAB's digital Butterworth design expects frequencies normalized by the Nyquist frequency, so multiplying by `2 / fs` converts hertz into that normalized scale. <!--SR:!2026-05-07,16,290!2026-05-07,16,290-->
- If `freqz` is called with the sampling frequency argument included, why is that useful when the tones of interest are already known in hertz? ::@:: It makes the returned frequency axis `w` appear directly in hertz, so the filter response can be read at those same physical tone frequencies. <!--SR:!2026-05-05,14,290!2026-05-08,16,290-->

## datatips as point evaluations of the frequency response

The assignment does not stop at plotting the Butterworth response qualitatively.  It explicitly asks for datatips at the three audio-tone frequencies, and the archived submission implements that by locating the corresponding response-grid indices first:

```matlab
resp_idx1 = find(w == 400);
resp_idx2 = find(w == 5000);
resp_idx3 = find(w == 16000);

datatip(resp_mag, 400, h_abs(resp_idx1))
datatip(resp_mag, 5000, h_abs(resp_idx2))
datatip(resp_mag, 16000, h_abs(resp_idx3))
```

The same pattern is then repeated on the phase-response plot with `h_ang`.  Conceptually, each datatip is a pointwise evaluation of the system function at a frequency already known to matter.  The useful habit is to stop reading the curve as one smooth picture only and instead ask: what multiplier and what phase shift does this filter apply to each tone that is actually present in the input?

For this signal the interpretation is immediate.  The out-of-band $400\,\text{Hz}$ and $16000\,\text{Hz}$ components should see near-zero magnitude response, while the in-band $5000\,\text{Hz}$ component should survive with a magnitude near one but with a nonzero phase shift.

---

Flashcards for this section are as follows:

- Why place datatips on the frequency response exactly at the tone frequencies present in the input spectrum? ::@:: Because the frequency-response plot becomes most useful when it is read at the exact tone frequencies present in the input, so the gain applied to each actual spectral line can be interpreted directly. <!--SR:!2026-05-07,15,290!2026-05-06,14,290-->
- Why inspect both magnitude and phase datatips instead of magnitude alone when predicting a filtered sinusoid? ::@:: Because one needs both the attenuation information and the phase-shift information to explain the final filtered waveform in the time domain. <!--SR:!2026-05-07,15,290!2026-05-07,16,290-->
- For a correctly designed band-pass, what should the response magnitude look like at out-of-band tones such as $400\,\text{Hz}$ and $16000\,\text{Hz}$? ::@:: Their magnitude responses should be close to zero because those tones lie outside the designed passband. <!--SR:!2026-05-07,15,290!2026-05-05,14,290-->
- For a correctly designed band-pass, what should the response at the in-band tone $5000\,\text{Hz}$ look like? ::@:: Its magnitude response should stay near one because it lies inside the passband, but its phase response should generally be nonzero because a Butterworth filter is not phase-free. <!--SR:!2026-05-06,14,290!2026-05-05,14,290-->

## butterworth output versus the ideal-filter picture

After filtering, the archived solution writes the output approximately as one surviving cosine: $y(t) \approx 0.3\cos\!\left(10000\pi t - \pi/4 + 0.506822\right)$.

That expression is consistent with the spectral reading: the $5000\,\text{Hz}$ component is the only one kept by the chosen passband, and its original cosine amplitude $0.3$ is preserved to first approximation.  The extra phase term comes from the filter's phase response at that in-band frequency.

The archived submission also states the key comparison with an ideal band-pass filter.  A Butterworth filter suppresses out-of-band tones strongly but not with mathematically perfect zero gain, and it introduces phase distortion in the passband.  An ideal band-pass picture, by contrast, would remove the rejected tones exactly and would preserve the surviving tone without adding a phase shift.

---

Flashcards for this section are as follows:

- If a band-pass keeps only the $5000\,\text{Hz}$ tone from an original three-tone mixture, where does an extra phase term such as $0.506822$ in the output cosine come from? ::@:: It comes from the Butterworth filter's phase response at that tone, so the output cosine inherits both the original signal phase and the filter-induced phase shift. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- If the original three-tone mixture contains $400\,\text{Hz}$, $5000\,\text{Hz}$, and $16000\,\text{Hz}$, why does the filtered output collapse to one dominant cosine when only the middle tone lies inside the passband? ::@:: Because the designed band-pass keeps the middle $5000\,\text{Hz}$ component while strongly attenuating the lower $400\,\text{Hz}$ and higher $16000\,\text{Hz}$ components. <!--SR:!2026-05-08,16,290!2026-05-07,15,290-->
- What qualitative difference separates a realizable Butterworth band-pass from an ideal band-pass? ::@:: The Butterworth filter only approximates perfect rejection and adds phase distortion, whereas the ideal band-pass would eliminate the rejected tones exactly and would not add passband phase shift. <!--SR:!2026-05-06,15,290!2026-05-05,14,290-->
- Why is a one-cosine output a good sanity check after the response analysis predicts that only one in-band tone survives? ::@:: Because the response analysis predicted that only the in-band spectral line should remain, so the time-domain waveform should collapse from a three-tone mixture to one dominant sinusoid. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
