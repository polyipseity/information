---
aliases:
  - ELEC 2100 sampling
  - ELEC 2100 sampling theorem
  - ELEC2100 sampling theorem
  - HKUST ELEC 2100 sampling theorem
  - aliasing
  - anti-aliasing
  - reconstruction from samples
  - sampling
  - sampling theorem
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/sampling_theorem
  - language/in/English
---

# sampling theorem

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

The sampling theorem explains when a continuous-time signal can be converted into a discrete sequence and then reconstructed without information loss. Its core message is geometric rather than mysterious: sampling creates repeated spectral copies, and exact recovery is possible exactly when those copies do not overlap.

This note keeps both the time-domain and frequency-domain viewpoints visible. In time, ideal sampling multiplies the signal by an impulse train. In frequency, that multiplication becomes convolution with a comb, so the original spectrum is replicated periodically. Reconstruction then becomes a filtering problem, and aliasing becomes an overlap problem.

---

Flashcards for this section are as follows:

- What core problem does the sampling theorem note solve in ELEC 2100? ::@:: It explains when uniformly spaced samples retain all information in a bandlimited continuous-time signal and what reconstruction rule recovers the original waveform from those samples.
- What is the central frequency-domain idea behind the sampling theorem? ::@:: Sampling creates repeated spectral copies, and perfect recovery is possible exactly when those copies remain separated instead of overlapping.

## sampling model and notation

Uniform sampling with interval $T$ converts a continuous-time signal $x(t)$ into the sequence $x[n]=x(nT)$. The sampling frequency is $f_s=1/T$, and the angular sampling frequency is $\omega_s=2\pi/T$. Ideal sampling is modeled by the impulse train $p_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$, so the sampled signal is $x_s(t)=x(t)p_T(t)=\sum_{n=-\infty}^{\infty}x(nT)\delta(t-nT)$.

This formula should be read literally. Sampling does not keep a continuous trace of the waveform; it keeps only the values at the sampling instants and stores them as weighted impulses. The weight attached to the impulse at $t=nT$ is exactly the sample value $x(nT)$. This impulse-train viewpoint is the clean bridge to the frequency domain because multiplication in time becomes convolution in frequency.

Ideal impulse sampling is a mathematical model rather than a directly physical waveform generator, but it is the right model for theorem statements because it isolates the spectral effect of sampling with almost no extra distortion built in.

---

Flashcards for this section are as follows:

- What is the uniformly sampled discrete-time sequence associated with a continuous-time signal $x(t)$ and interval $T$? ::@:: It is $x[n]=x(nT)$.
- How are the sampling frequency and angular sampling frequency related to $T$? ::@:: They are $f_s=1/T$ and $\omega_s=2\pi/T$.
- What impulse train models ideal uniform sampling? ::@:: It is $p_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$.
- How is the sampled signal written in the impulse-train model? ::@:: It is $x_s(t)=x(t)p_T(t)=\sum_{n=-\infty}^{\infty}x(nT)\delta(t-nT)$.
- Why is the impulse-train model the most useful starting point for the sampling theorem? ::@:: Because it turns sampling into multiplication in time, which becomes spectral convolution and therefore makes replicated spectra appear automatically.
- What do the impulse weights in $x_s(t)=\sum_n x(nT)\delta(t-nT)$ represent physically? ::@:: The weight of the impulse at $t=nT$ is exactly the sample value taken from the original waveform at that sampling instant.

## choosing the sampling frequency

The sampling frequency should be chosen from the frequency characteristics of the phenomenon that one wants to preserve. If the signal changes quickly, the sampling rate must be high enough to follow that rapid variation without obvious distortion. If the signal changes slowly, a much lower sampling rate may already be enough, and pushing the rate far higher mainly produces redundant data.

Motion pictures give a familiar intuition. Human vision has persistence, so after an image disappears its impression remains for roughly $0.1$ to $0.4\text{ s}$. Showing still images at about $24$ frames per second is therefore fast enough to create a convincing illusion of continuous motion for many ordinary scenes. If the frame rate is too low, motion becomes jerky or flickery. If it is much higher than the application needs, the main penalty is redundant data, storage, and transmission burden.

The same idea applies far beyond cinema. A mosquito wingbeat around $600\text{ Hz}$ is much faster than ordinary human motion, so capturing it clearly requires high-speed recording with a very large frame rate, followed by standard playback if we want to slow the motion down visually. Stellar rotation can be extremely slow, for example on the order of $1/86{,}400\text{ Hz}$ for a one-day cycle, so time-lapse recording uses a very low sampling rate during acquisition and then ordinary playback to speed the phenomenon up for human viewing.

So the rule of thumb is simple: choose the sampling rate from the target frequency content and from the purpose of observation. Too high gives redundancy. Too low gives distortion, flicker, judder, or aliasing. The right rate depends on what dynamics must be preserved.

---

Flashcards for this section are as follows:

- What principle should determine the sampling frequency in practice? ::@:: It should be determined by the frequency characteristics of the phenomenon that must be preserved and by the purpose of the observation or reconstruction.
- Why can an excessively high sampling frequency still be undesirable even if aliasing is avoided? ::@:: Because it can produce a large amount of redundant data, increasing storage, transmission, and processing cost without adding useful information for the application.
- Why can too low a sampling frequency be visually or physically harmful? ::@:: Because it can miss important changes in the signal and create distortion such as flicker, judder, or aliasing.
- How does motion-picture playback illustrate sampling-frequency selection? ::@:: Human persistence of vision lets about $24$ frames per second create an illusion of smooth motion for ordinary scenes, so the frame rate is chosen to match the temporal characteristics that viewers need to perceive.
- Why does a mosquito wingbeat require high-speed recording while stellar rotation suggests time-lapse recording? ::@:: Because the wingbeat is a fast phenomenon with high frequency content, whereas stellar rotation is a very slow phenomenon with low frequency content. The sampling rate should match the speed of the phenomenon being captured.

## spectrum of a sampled signal

The Fourier transform of the sampling train is another comb: $P_T(\omega)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_s)$. Therefore the transform of the sampled signal is $X_s(\omega)=\frac{1}{2\pi}(X*P_T)(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$. So ideal sampling replicates the original spectrum every $\omega_s$ radians per second, and each copy is scaled by $1/T$.

This is the decisive picture behind the theorem. If the original spectrum is narrow enough, the shifted copies remain separate. If the copies overlap, different continuous-time frequencies become indistinguishable after sampling.

The geometry is worth emphasizing. A larger sampling frequency pushes the spectral replicas farther apart. A smaller sampling frequency pulls them closer together. So the theorem is really about spacing between copies versus the width of each copy.

---

Flashcards for this section are as follows:

- What is the Fourier transform of the sampling train $p_T(t)=\sum_n\delta(t-nT)$? ::@:: It is $P_T(\omega)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_s)$ with $\omega_s=2\pi/T$.
- Starting from $x_s(t)=x(t)p_T(t)$, what sampled-spectrum formula follows from the multiplication theorem? ::@:: It is $X_s(\omega)=\frac{1}{2\pi}(X*P_T)(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$.
- What does the sampled-spectrum formula mean geometrically? ::@:: The original spectrum is copied and shifted every $\omega_s$, so the sampled spectrum is a periodic train of replicated spectral shapes.
- Why is spectral overlap the decisive issue in sampling? ::@:: Because once replicated copies overlap, several different original continuous-time frequencies contribute to the same sampled-spectrum region and can no longer be separated uniquely.
- Why does increasing $f_s$ make exact recovery easier from the spectrum picture? ::@:: Because increasing $f_s$ increases the copy spacing $\omega_s=2\pi/T$, so the replicated spectra are pushed farther apart and are less likely to overlap.

## sampling theorem and Nyquist limit

Suppose $x(t)$ is bandlimited to $|\omega|<\omega_m$, equivalently to $|f|<f_m$ where $\omega_m=2\pi f_m$. Then exact reconstruction from uniform samples is possible if $\omega_s\ge2\omega_m$, equivalently $f_s\ge2f_m$ or $T\le\pi/\omega_m=1/(2f_m)$. The minimum allowed sampling frequency $2f_m$ is the Nyquist sampling frequency, and the largest allowed sampling interval $1/(2f_m)$ is the Nyquist sampling interval.

The factor $2$ comes from geometry, not from magic. If the baseband copy occupies $[-\omega_m,\omega_m]$, then the next positive replica begins at $\omega_s-\omega_m$. Non-overlap requires $\omega_s-\omega_m\ge\omega_m$, which is exactly $\omega_s\ge2\omega_m$.

At the exact Nyquist limit, the copies just touch. In ideal theorem statements that is acceptable when the signal is perfectly bandlimited and the edge behavior is well controlled. In engineering practice one usually samples above the bare minimum to leave room for nonideal filters and uncertainty in the actual bandwidth.

---

Flashcards for this section are as follows:

- What is the Nyquist sampling condition for a signal bandlimited to $|\omega|<\omega_m$ or $|f|<f_m$? ::@:: It is $\omega_s\ge2\omega_m$, equivalently $f_s\ge2f_m$ or $T\le1/(2f_m)=\pi/\omega_m$.
- What is the Nyquist sampling frequency? ::@:: It is the minimum allowed sampling frequency $2f_m$ for a signal bandlimited to $|f|<f_m$.
- What is the Nyquist sampling interval? ::@:: It is the largest allowed sampling interval $T_{\max}=1/(2f_m)=\pi/\omega_m$ for exact recovery of a signal bandlimited to $|f|<f_m$.
- Why does the factor $2$ appear in the Nyquist condition? ::@:: Because the baseband spectrum extends over both positive and negative frequencies, so adjacent replicas avoid overlap only when the copy spacing is at least twice the highest baseband frequency.
- Worked example (method: Nyquist-rate determination): If a voice signal is bandlimited to $3.4\text{ kHz}$, what Nyquist-rate conclusion follows? ::@:: Step 1: use $f_s\ge2f_m$. <br/> Step 2: substitute $f_m=3.4\text{ kHz}$ to get $f_s\ge6.8\text{ kHz}$. <br/> Step 3: so an $8\text{ kHz}$ telephone sampling rate safely exceeds the Nyquist minimum.
- Why do engineers often sample above the exact Nyquist limit instead of exactly at it? ::@:: Because practical spectra are rarely perfectly sharp and practical filters are not ideal brick walls, so extra margin reduces aliasing risk and eases implementation.

## reconstruction and interpolation

When the Nyquist condition is satisfied, the replicated spectra do not overlap. Then an ideal reconstruction filter can isolate the central replica and restore the original amplitude scaling. In the frequency domain, one convenient ideal choice is $H_r(\omega)=T$ for the passband containing only the central copy and $0$ outside. The factor $T$ is important because the sampled spectrum is $X_s(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$, so after filtering we want $X_r(\omega)=X_s(\omega)H_r(\omega)=X(\omega)$ on the original baseband.

This is why one reconstructs by convolving with a sinc or Sa impulse response. If $x_r(t)=x_s(t)*h_r(t)$, then the convolution theorem gives $X_r(\omega)=X_s(\omega)H_r(\omega)$. So choosing $h_r(t)$ is really choosing a frequency-domain selector $H_r(\omega)$ that keeps one copy of the spectrum and rejects the other replicas. The ideal selector is rectangular in frequency, so its impulse response is sinc in time.

Using both common notations together, define $\operatorname{Sa}(x)=\sin x/x$ and $\operatorname{sinc}_{\pi}(u)=\sin(\pi u)/(\pi u)$, so $\operatorname{Sa}(\pi u)=\operatorname{sinc}_{\pi}(u)$. Then $H_r(\omega)=T\operatorname{rect}(\omega/(2\pi/T))$ corresponds to $h_r(t)=\operatorname{Sa}(\pi t/T)=\operatorname{sinc}_{\pi}(t/T)$. Convolving the sampled impulse train with this kernel gives $x(t)=x_s*h_r=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{Sa}(\pi (t-nT)/T)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{sinc}_{\pi}((t-nT)/T)$.

The interpolation works because each kernel is $1$ at its own sample location and $0$ at every other sample location: $\operatorname{Sa}(0)=\operatorname{sinc}_{\pi}(0)=1$, while $\operatorname{Sa}(m\pi)=\operatorname{sinc}_{\pi}(m)=0$ for every nonzero integer $m$. So each sample reproduces itself exactly at its own time instant and does not disturb the other sample instants.

This is exactly why the Sa / $\operatorname{sinc}_{\pi}$ kernel is the _ideal interpolation kernel_ for uniform sampling. At the instant $t=nT$, the shifted kernel centered on that sample contributes full amplitude $1$, while every other shifted kernel contributes $0$ because its argument is a nonzero integer multiple of $\pi$ (or a nonzero integer in $\operatorname{sinc}_{\pi}$ notation). So the interpolation sum has no cross-talk between different sample instants: one sample is preserved, all the others are nulled there. In the frequency domain this matches the ideal rectangular reconstruction filter, so the time-domain zero-crossing pattern and the frequency-domain ideal low-pass selector are two views of the same exact reconstruction rule.

It is also useful to vary the kernel parameter mentally. To avoid symbol collision with $\tau$ that is often used as a rectangular-pulse width parameter in transform-pair notation, use $\sigma$ here for interpolation-kernel scale. If one tries $h_{\sigma}(t)=\operatorname{Sa}(\pi t/\sigma)=\operatorname{sinc}_{\pi}(t/\sigma)$ while keeping the sample spacing $T$ fixed, then exact interpolation requires the zero crossings to land at the other sampling instants, so the natural choice is $\sigma=T$. In this formula, $\sigma$ is a _time-domain scale parameter_, so larger $\sigma$ means a wider time-domain kernel because the zero crossings move out to $t=\pm\sigma,\pm2\sigma,\dots$. By Fourier scaling, that same wider time-domain kernel corresponds to a narrower rectangular selector in frequency. Conversely, smaller $\sigma$ means a narrower time-domain kernel but a wider frequency-domain selector.

So the corrected intuition is: if $\sigma>T$, the time-domain interpolation kernel is too wide, the zero crossings are too far apart, and neighboring samples do not cancel properly at each other's sample times. If $\sigma<T$, the time-domain kernel is too narrow, the zero crossings come too quickly, and the neighboring sample contributions no longer line up correctly for exact reconstruction. The memory cue is that $\sigma$ sets the time-domain zero-crossing spacing, while the corresponding rectangular passband width in frequency moves in the opposite direction.

---

Flashcards for this section are as follows:

- How is perfect reconstruction described in the frequency domain once the sampling condition is satisfied? ::@:: Use an ideal low-pass filter to keep the central replicated spectrum and reject all other shifted copies.
- Why must the ideal reconstruction LPF have gain $T$ rather than gain $1$ in the passband? ::@:: Because the sampled spectrum copies are scaled by $1/T$, so the reconstruction filter must multiply by $T$ while selecting the central copy in order to recover the original spectrum amplitude.
- Why is convolution with a sinc or Sa kernel the right reconstruction operation? ::@:: Because if $x_r(t)=x_s(t)*h_r(t)$, then the convolution theorem gives $X_r(\omega)=X_s(\omega)H_r(\omega)$. Choosing $H_r(\omega)$ to be an ideal low-pass selector keeps one spectral replica, so the corresponding $h_r(t)$ must be a sinc or Sa kernel.
- What is the ideal sinc or Sa interpolation formula for reconstructing a continuous-time signal from its samples? ::@:: It is $x(t)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{Sa}(\pi (t-nT)/T)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{sinc}_{\pi}((t-nT)/T)$.
- Why does the ideal Sa or $\operatorname{sinc}_{\pi}$ interpolation pass exactly through the sample values? ::@:: Because each shifted interpolation kernel equals $1$ at its own sampling instant and $0$ at all the other sampling instants. So at $t=nT$ the term built from $x(nT)$ survives with unit weight, while every term from the other samples vanishes.
- Why is Sa / $\operatorname{sinc}_{\pi}$ called the ideal interpolation kernel for uniform sampling? ::@:: It is the exact reconstruction kernel obtained from the ideal rectangular low-pass filter. In time domain it preserves the sample at its own location with value $1$ and forces zero contribution from all other samples at that same instant, so there is no interference between neighboring sample values.
- How do you derive the sinc or Sa interpolation formula from the reconstruction filter? ::@:: Start with the sampled impulse train $x_s(t)=\sum_n x(nT)\delta(t-nT)$. <br/> Convolve it with the reconstruction kernel $h_r(t)=\operatorname{Sa}(\pi t/T)=\operatorname{sinc}_{\pi}(t/T)$. <br/> Each shifted impulse produces a shifted copy $x(nT)h_r(t-nT)$. <br/> Summing all those shifted kernels gives $x(t)=\sum_n x(nT)\operatorname{Sa}(\pi (t-nT)/T)=\sum_n x(nT)\operatorname{sinc}_{\pi}((t-nT)/T)$.
- Why is $\sigma=T$ the natural choice in $h_{\sigma}(t)=\operatorname{Sa}(\pi t/\sigma)=\operatorname{sinc}_{\pi}(t/\sigma)$? ::@:: Because $\sigma$ sets the time-domain zero-crossing spacing of the interpolation kernel, and exact interpolation requires those zero crossings to land exactly at the other sampling instants spaced by $T$.
- How does changing $\sigma$ affect the time-domain kernel and the corresponding frequency-domain selector? ::@:: In $h_{\sigma}(t)=\operatorname{Sa}(\pi t/\sigma)=\operatorname{sinc}_{\pi}(t/\sigma)$, larger $\sigma$ means a wider time-domain kernel and therefore a narrower rectangular selector in frequency. Smaller $\sigma$ means a narrower time-domain kernel and therefore a wider selector in frequency.
- Why does this section use $\sigma$ instead of $\tau$ for interpolation-kernel scale? ::@:: To avoid notation collision with $\tau$ commonly used as rectangular-pulse width in transform-pair formulas. Here $\sigma$ is reserved for interpolation-kernel scaling, and equals the argument of the first zero-crossing of the kernel.
- What happens intuitively if $\sigma>T$ or $\sigma<T$ while $T$ is fixed? Here, $\sigma$ is the interpolation-kernel scale, and equals the argument of the first zero-crossing of the kernel. ::@:: If $\sigma>T$, the time-domain kernel is too wide, so the zero crossings are too far apart and neighboring samples do not cancel properly. If $\sigma<T$, the time-domain kernel is too narrow, so the zero crossings come too quickly and the neighboring sample contributions no longer line up for exact interpolation.

## practical reconstruction filters

Ideal sinc or Sa reconstruction is exact for bandlimited signals, but it is not the most convenient physical implementation because the impulse response is infinitely long and extends in both time directions. Practical systems therefore often use simpler hold circuits after digital-to-analog conversion.

The zero-order hold (ZOH) keeps each sample constant until the next sample arrives. Its impulse response is $h_{\mathrm{ZOH}}(t)=u(t)-u(t-T)$, a one-sided rectangular pulse of width $T$. In frequency, $H_{\mathrm{ZOH}}(\omega)=T e^{-j\omega T/2}\operatorname{Sa}(\omega T/2)=T e^{-j\omega T/2}\operatorname{sinc}_{\pi}(\omega T/(2\pi))$. The implementation picture is simple: each sample value drives a hold circuit, commonly modeled as a switch-plus-capacitor or DAC output stage, and the output stays flat until the next sampling instant. To draw the block diagram, draw $x[n]$ entering a block labeled _zero-order hold_ and draw a staircase continuous-time output on the right. If one wants to show the idealized structure more explicitly, draw $x[n] \to$ impulse DAC $\to h_{\mathrm{ZOH}}(t)$.

The first-order hold (FOH) joins adjacent samples by straight lines instead of flat plateaus. A convenient interpolation-kernel viewpoint is $h_{\mathrm{FOH}}(t)=\Lambda((t-T)/T)$ for the causal version, where $\Lambda$ is the triangular function, or equivalently a one-sample-delayed triangular pulse of width $2T$. In frequency, $H_{\mathrm{FOH}}(\omega)=T e^{-j\omega T}\operatorname{Sa}^{2}(\omega T/2)=T e^{-j\omega T}\operatorname{sinc}_{\pi}^{2}(\omega T/(2\pi))$. The implementation idea is a linear ramp generator or linear interpolator that uses adjacent samples to create line segments between them. To draw the block diagram, draw $x[n]$ entering a block labeled _first-order hold_ or _linear interpolator_ and draw a piecewise linear continuous-time output. In a more filter-based view, draw $x[n] \to$ impulse DAC $\to h_{\mathrm{FOH}}(t)$.

Compared with the ideal sinc or Sa reconstruction filter, both holds are approximate. The ideal filter is exact for perfectly bandlimited signals because its frequency response selects one spectral copy exactly. ZOH is much easier to implement, but it creates a staircase output and introduces high-frequency droop. FOH is also practical, gives a smoother output, and usually tracks low-frequency behavior better than ZOH, but it is still not exact ideal reconstruction. The practical motivation is clear: finite, causal, simple circuits are easier to build than an infinite two-sided sinc filter.

---

Flashcards for this section are as follows:

- What is the impulse response of a zero-order hold, and what waveform does it produce? ::@:: The impulse response is $h_{\mathrm{ZOH}}(t)=u(t)-u(t-T)$, a one-sided rectangular pulse of width $T$. It produces a staircase waveform that holds each sample value constant until the next sample arrives.
- How should you draw the block diagram of a zero-order hold implementation? ::@:: Draw the sample sequence $x[n]$ entering a block labeled _zero-order hold_ and show a staircase continuous-time output. In a more structural version, draw $x[n] \to$ ideal impulse DAC $\to h_{\mathrm{ZOH}}(t)$.
- What is the impulse response of a first-order hold, and what waveform does it produce? ::@:: A convenient causal description is $h_{\mathrm{FOH}}(t)=\Lambda((t-T)/T)$, a delayed triangular kernel of width $2T$. It produces piecewise linear segments connecting adjacent sample values.
- How should you draw the block diagram of a first-order hold implementation? ::@:: Draw the sample sequence $x[n]$ entering a block labeled _first-order hold_ or _linear interpolator_ and show a piecewise linear continuous-time output. In a filter view, draw $x[n] \to$ ideal impulse DAC $\to h_{\mathrm{FOH}}(t)$.
- How do ZOH and FOH compare with the ideal sinc or Sa reconstruction filter? ::@:: The ideal sinc or Sa filter is exact for bandlimited reconstruction but has infinite support. ZOH is simpler and causal but gives staircase output and droop. FOH is also practical and smoother than ZOH but is still only an approximation to the ideal reconstruction filter.
- Why are zero-order and first-order holds widely used in practice? ::@:: Because they are finite, causal, and easy to implement physically, whereas an ideal sinc or Sa reconstruction filter has an infinite two-sided impulse response.

## aliasing and anti-aliasing

Aliasing is the failure mode of undersampling. If $\omega_s<2\omega_m$, the replicated spectra overlap, so different continuous-time frequencies produce the same sample sequence. Once that happens, unique reconstruction of the original signal is impossible from those samples alone.

The standard intuition example is that sampling $10\text{ Hz}$ and $30\text{ Hz}$ cosines at $40\text{ Hz}$ gives the same discrete-time sequence. The sequence only remembers digital frequency modulo $2\pi$, not the original continuous-time band placement. So after sampling, two different analog sinusoids can become indistinguishable because they land on the same normalized frequency.

The preventive remedy is anti-aliasing: place a low-pass filter before the sampler so the input entering the sampler is already bandlimited to below half the sampling frequency. That placement matters. An anti-aliasing filter after sampling cannot undo overlap that has already happened.

A direct undersampling example is worth keeping in mind. Suppose $x(t)=\cos(10t)$ but the sampling angular frequency is only $\omega_s=14\text{ rad/s}$, so the Nyquist limit would have required at least $20\text{ rad/s}$. The sampled sequence is $x[n]=\cos(10nT)$ with $T=2\pi/14$, so $x[n]=\cos(10\pi n/7)=\cos((2\pi-4\pi/7)n)=\cos(4\pi n/7)$. This means the discrete-time samples are indistinguishable from those of a continuous-time cosine at angular frequency $4\text{ rad/s}$. In spectral language, the original line at $\omega=10$ folds back to the aliased line at $\omega_s-10=4$. So the wrong low-frequency sinusoid is not created by the reconstruction filter; it is already baked into the samples once undersampling has happened.

The practical reason for anti-aliasing is subtle but important. In many continuous-time to discrete-time conversion systems, the original input is not strictly bandlimited to half the sampling frequency. If we still want to sample at a relatively low rate, then a prefilter is needed. With an anti-aliasing low-pass filter, the unavoidable error is only that the too-high-frequency content is removed before sampling. Without the filter, that high-frequency content is not merely lost; it folds into false low-frequency components that were never really present in the original baseband.

The block-diagram description is therefore: $x(t) \to$ low-pass anti-aliasing filter $\to x_l(t) \to$ sampler $\to x_d[n]$. To draw it, put the continuous-time signal on the left, a block labeled _LPF (anti-aliasing filter)_ in the middle, and the sampling block on the right. The point of the first block is to make the signal bandlimited before the sampling operation happens.

This idea appears in many engineering settings. Digital telephony samples voice at $8\text{ kHz}$, so the analog front end removes components above about $4\text{ kHz}$ before sampling. When generating a thumbnail image, one should first low-pass filter the image to suppress high spatial frequencies; otherwise Moiré patterns can appear after spatial resampling. Likewise, digital cameras often use an optical blur or low-pass filter ahead of the sensor array so that very fine spatial detail does not alias into false lower-frequency patterns at the pixel grid.

---

Flashcards for this section are as follows:

- What is aliasing? ::@:: It is the phenomenon in which undersampling causes replicated spectra to overlap, making different continuous-time frequencies indistinguishable after sampling.
- Why does aliasing destroy unique reconstruction? ::@:: Because once spectral copies overlap, several different original continuous-time spectra can produce the same sampled sequence.
- Worked example (method: digital-frequency periodicity and aliasing): Why do $10\text{ Hz}$ and $30\text{ Hz}$ cosines sampled at $40\text{ Hz}$ produce the same discrete-time sequence? ::@:: Step 1: normalize the frequencies to get $10/40=1/4$ and $30/40=3/4$. <br/> Step 2: the digital angular frequencies are $\pi/2$ and $3\pi/2=-\pi/2\pmod{2\pi}$. <br/> Step 3: cosine is even, so the two sampled cosines match at every integer sample. <br/> Step 4: therefore the same sequence is produced even though the continuous-time frequencies are different.
- What is an anti-aliasing filter? ::@:: It is a low-pass filter placed before the sampler to remove frequency components above half the sampling frequency so spectral replicas will not overlap.
- Why must anti-aliasing be done before sampling rather than after sampling? ::@:: Because once aliasing has already folded different continuous-time frequencies onto the same discrete-time sequence, the lost distinction cannot be recovered afterward.
- What is the key intuition behind aliasing in one sentence? ::@:: Sampling remembers only normalized digital frequency, so different analog frequencies that differ by multiples of the sampling rate can collapse onto the same discrete-time oscillation.
- Worked example (method: spectral-folding and aliasing calculation): If $x(t)=\cos(10t)$ is sampled with angular sampling frequency $\omega_s=14\text{ rad/s}$, why does aliasing make it look like a lower-frequency cosine? ::@:: Step 1: the sampling interval is $T=2\pi/14$. <br/> Step 2: the samples are $x[n]=\cos(10nT)=\cos(10\pi n/7)$. <br/> Step 3: since $10\pi/7=2\pi-4\pi/7$, the same samples equal $\cos(4\pi n/7)$. <br/> Step 4: that normalized frequency corresponds to the analog alias at $\omega=14-10=4\text{ rad/s}$. <br/> Step 5: so undersampling makes the original $10\text{ rad/s}$ cosine indistinguishable from a reconstructed $4\text{ rad/s}$ cosine.
- With an anti-aliasing filter, what error remains, and why is it better than no filter? ::@:: With the filter, only the removed high-frequency content is lost. Without the filter, those high-frequency components also fold into false low-frequency components, which is worse because spurious content is added where it should not exist.
- How should you draw the anti-aliasing block diagram? ::@:: Draw $x(t)$ entering a block labeled _LPF (anti-aliasing filter)_, then a sampler block, and finally the discrete-time output $x_d[n]$. The LPF must appear before sampling.
- What are three common anti-aliasing examples to remember? ::@:: Voice sampled at $8\text{ kHz}$ needs analog filtering above $4\text{ kHz}$; thumbnail generation needs low-pass filtering to avoid Moir\'e patterns; and digital cameras often blur the optical image slightly before sensor sampling to suppress spatial aliasing.

## reading maximum sampling interval from a spectrum

Sampling-interval questions use a short standard workflow. First, read the highest occupied spectral edge of the original continuous-time signal and call it $\omega_m$ or $f_m$. Second, compute $T_{\max}=\pi/\omega_m=1/(2f_m)$. Third, when asked to sketch the sampled spectrum, place copies of the original spectrum every $\omega_s=2\pi/T$ or every $f_s=1/T$, and scale the copy heights by $1/T$ if the plot is meant quantitatively.

A standard lecture-style example is exactly the borderline Nyquist case. Suppose the original continuous-time spectrum is nonzero only for $|\omega|\le\omega_m$, and the question asks for the largest sampling interval that still allows distortionless recovery together with the corresponding sampled spectrum. Then $T_{\max}=\pi/\omega_m$. At this value the sampling angular frequency is $\omega_s=2\pi/T_{\max}=2\omega_m$, so the sampled spectrum is $F_s(\omega)=\frac{1}{T_{\max}}\sum_{k=-\infty}^{\infty}F(\omega-2k\omega_m)$. The central copy occupies $|\omega|\le\omega_m$, the adjacent copies are centered at $\pm2\omega_m$, and they just touch the central copy at $\omega=\pm\omega_m$. So the Nyquist-limit sketch is the just-touching picture: no interior overlap, but no guard band either.

This workflow is especially important when the sampled signal is obtained indirectly, for example after some prior filtering or modulation. The sampling theorem must be applied to the actual bandwidth of the signal entering the sampler, not to whichever earlier signal is easiest to read from memory.

---

Flashcards for this section are as follows:

- In a sampling-theorem question with a drawn spectrum, what three-step workflow should you use to find the maximum sampling interval and sketch the sampled spectrum? ::@:: Step 1: read the highest spectral edge of the original signal and call it $\omega_m$ or $f_m$. <br/> Step 2: compute $T_{\max}=\pi/\omega_m=1/(2f_m)$. <br/> Step 3: sketch the sampled spectrum by placing copies of the original spectrum every $\omega_s=2\pi/T$ or every $f_s=1/T$.
- Worked example (method: Nyquist-limit spectrum calculation): If a spectrum $F(\omega)$ is nonzero only for $|\omega|\le\omega_m$, what are the largest distortionless sampling interval and the sampled spectrum at that limiting case? ::@:: Step 1: the highest occupied angular frequency is $\omega_m$, so the largest distortionless interval is $T_{\max}=\pi/\omega_m$. <br/> Step 2: at this limit, $\omega_s=2\pi/T_{\max}=2\omega_m$. <br/> Step 3: therefore $F_s(\omega)=\frac{1}{T_{\max}}\sum_{k=-\infty}^{\infty}F(\omega-2k\omega_m)$. <br/> Step 4: the central replica occupies $|\omega|\le\omega_m$, the nearest replicas are centered at $\pm2\omega_m$, and they just touch the central copy at $\omega=\pm\omega_m$. <br/> Step 5: so the Nyquist-limit sketch is the just-touching replica picture.
- Why must the bandwidth used in the Nyquist condition be the bandwidth of the final signal entering the sampler? ::@:: Because spectral overlap after sampling depends on the actual highest frequency present at the sampler input, so the Nyquist test must use that final bandwidth.
- Why is the sampled-spectrum sketch drawn by repeating the original spectrum at spacing $\omega_s$? ::@:: Because ideal sampling multiplies by an impulse train in time, which replicates the spectrum every sampling angular frequency $\omega_s=2\pi/T$.
- Why is it dangerous to use the bandwidth of an earlier signal instead of the bandwidth right at the sampler input? ::@:: Because any filtering, modulation, or system processing before the sampler can change the occupied frequency range, and aliasing depends only on what is actually present when sampling occurs.
