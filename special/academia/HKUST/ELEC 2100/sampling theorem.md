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

The sampling theorem explains when a continuous-time signal can be converted into a discrete sequence and reconstructed without information loss. Its core message is geometric rather than mysterious: sampling creates repeated spectral copies, and exact recovery is possible exactly when those copies do not overlap.

In time, ideal sampling multiplies the signal by an impulse train. In frequency, that multiplication becomes convolution with a comb, replicating the original spectrum periodically. Reconstruction is a filtering problem, and aliasing is an overlap problem.

---

Flashcards for this section are as follows:

- What problem does the sampling theorem solve? ::@:: It tells when uniformly spaced samples retain all information in a bandlimited signal and how to reconstruct the original.
- What is the central frequency-domain idea? ::@:: Sampling creates repeated spectral copies; perfect recovery requires those copies to stay separated.

## sampling model and notation

Uniform sampling with interval $T$ converts $x(t)$ into $x[n]=x(nT)$. The sampling frequency is $f_s=1/T$, angular sampling frequency $\omega_s=2\pi/T$. Ideal sampling uses the impulse train $p_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$, so $x_s(t)=x(t)p_T(t)=\sum_{n=-\infty}^{\infty}x(nT)\delta(t-nT)$.

Read this literally: sampling keeps only the values at sampling instants, stored as weighted impulses. The impulse at $t=nT$ has weight $x(nT)$. This bridges to the frequency domain because multiplication in time becomes convolution in frequency.

---

Flashcards for this section are as follows:

- What is the sampled sequence for signal $x(t)$ with interval $T$? ::@:: $x[n]=x(nT)$.
- What are $f_s$ and $\omega_s$ in terms of $T$? ::@:: $f_s=1/T$ and $\omega_s=2\pi/T$.
- What impulse train models ideal sampling? ::@:: $p_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$.
- What is the sampled signal in impulse-train form? ::@:: $x_s(t)=x(t)p_T(t)=\sum_{n=-\infty}^{\infty}x(nT)\delta(t-nT)$.
- Why is the impulse-train model useful? ::@:: It turns sampling into time multiplication, which becomes spectral convolution with replicated spectra.

- What impulse weights in $x_s(t)=\sum_n x(nT)\delta(t-nT)$ represent physically? ::@:: The weight of the impulse at $t=nT$ is exactly the sample value taken from the original waveform at that sampling instant.

## choosing the sampling frequency

The sampling frequency should match the signal's frequency content. A fast-changing signal needs a high rate; a slowly changing one needs only a low rate.

Motion pictures give a familiar intuition. Human vision has persistence of about $0.1$ to $0.4\text{ s}$, so showing still images at about $24$ fps creates convincing motion. Too low a rate makes motion jerky; much higher mainly wastes storage.

The same idea extends beyond cinema. A mosquito wingbeat at roughly $600\text{ Hz}$ needs high-speed recording. Stellar rotation at roughly $1/86{,}400\text{ Hz}$ uses time-lapse.

The rule: choose the rate from the target frequency content and observation purpose.

---

Flashcards for this section are as follows:

- What principle determines the sampling frequency? ::@:: Match it to the phenomenon's frequency content and the observation purpose.
- Why is excessive sampling rate undesirable? ::@:: It produces redundant data, increasing storage and processing cost without adding information.
- Why can too low a sampling frequency be harmful? ::@:: It misses important signal changes and creates distortion such as flicker, judder, or aliasing.
- How does motion-picture playback illustrate rate selection? ::@:: $24$ fps matches what human persistence of vision perceives as smooth motion for ordinary scenes.
- Why does a mosquito wingbeat need high-speed recording while stellar rotation uses time-lapse? ::@:: The wingbeat has high frequency content; stellar rotation has very low frequency content. The sampling rate should match the phenomenon's speed.

## spectrum of a sampled signal

The Fourier transform of the sampling train is $P_T(\omega)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_s)$. The sampled signal's transform is $X_s(\omega)=\frac{1}{2\pi}(X*P_T)(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$.

Ideal sampling replicates the original spectrum every $\omega_s$, with each copy scaled by $1/T$. If the original spectrum is narrow enough, copies stay separate. If they overlap, different continuous-time frequencies become indistinguishable.

The geometry here is key. A larger sampling frequency pushes the spectral replicas farther apart; a smaller one pulls them closer. So the theorem is really about spacing between copies versus the width of each copy.

---

Flashcards for this section are as follows:

- What is the Fourier transform of $p_T(t)=\sum_n\delta(t-nT)$? ::@:: $P_T(\omega)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_s)$.
- What is $X_s(\omega)$? ::@:: $X_s(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$.
- What does this formula mean geometrically? ::@:: The original spectrum is copied and shifted every $\omega_s$.
- Why is spectral overlap the key issue? ::@:: Overlapping copies mix different original frequencies, making unique reconstruction impossible.
- Why does increasing $f_s$ make exact recovery easier? ::@:: It increases the copy spacing $\omega_s=2\pi/T$, pushing replicas farther apart so they are less likely to overlap.

## sampling theorem and Nyquist limit

If $x(t)$ is bandlimited to $|\omega|<\omega_m$ (equivalently $|f|<f_m$), exact reconstruction requires $\omega_s\ge2\omega_m$, i.e. $f_s\ge2f_m$, i.e. $T\le1/(2f_m)$. The minimum rate $2f_m$ is the Nyquist frequency; the maximum interval $1/(2f_m)$ is the Nyquist interval.

The factor $2$ comes from geometry: the baseband copy occupies $[-\omega_m,\omega_m]$, and the next replica starts at $\omega_s-\omega_m$. Non-overlap needs $\omega_s-\omega_m\ge\omega_m$.

At the Nyquist limit copies just touch. In practice one samples above the bare minimum to leave room for nonideal filters.

---

Flashcards for this section are as follows:

- What is the Nyquist condition for $|\omega|<\omega_m$? ::@:: $\omega_s\ge2\omega_m$, equivalently $f_s\ge2f_m$ or $T\le1/(2f_m)$.
- What is the Nyquist frequency? ::@:: The minimum sampling rate $2f_m$ for a signal bandlimited to $|f|<f_m$.
- What is the Nyquist interval? ::@:: The maximum sampling interval $T_{\max}=1/(2f_m)$ for exact recovery.
- Why does $2$ appear in the Nyquist condition? ::@:: The baseband spans both positive and negative frequencies, so replicas need spacing of at least twice the highest frequency.
- If voice is bandlimited to $3.4\text{ kHz}$, what Nyquist rate follows? ::@:: $f_s\ge6.8\text{ kHz}$; an $8\text{ kHz}$ telephone rate safely exceeds this.
- Why sample above the exact Nyquist limit? ::@:: Practical spectra are not perfectly sharp and filters are not ideal, so extra margin reduces aliasing risk.

## reconstruction and interpolation

When the Nyquist condition holds, an ideal reconstruction filter isolates the central replica. One choice is $H_r(\omega)=T$ on the passband containing only the central copy, $0$ elsewhere. The factor $T$ compensates the $1/T$ scaling of the sampled spectrum.

The ideal selector is rectangular in frequency, so its impulse response is sinc in time. Using $\operatorname{Sa}(x)=\sin x/x$ and $\operatorname{sinc}_{\pi}(u)=\sin(\pi u)/(\pi u)$: $H_r(\omega)=T\operatorname{rect}(\omega/(2\pi/T))$ corresponds to $h_r(t)=\operatorname{Sa}(\pi t/T)=\operatorname{sinc}_{\pi}(t/T)$.

This is why one reconstructs by convolving with a sinc kernel. If $x_r(t)=x_s(t)*h_r(t)$, the convolution theorem gives $X_r(\omega)=X_s(\omega)H_r(\omega)$. Choosing $h_r(t)$ is really choosing a frequency-domain selector that keeps one spectral copy and rejects the rest. The ideal selector is rectangular in frequency, so its impulse response is sinc in time.

Convolving the sampled impulse train with this kernel gives:

$$x(t)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{Sa}(\pi (t-nT)/T)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{sinc}_{\pi}((t-nT)/T)$$

This works because each kernel equals $1$ at its own sample location and $0$ at every other: $\operatorname{Sa}(0)=1$, $\operatorname{Sa}(m\pi)=0$ for nonzero integer $m$. So each sample reproduces itself exactly and does not disturb the others.

The kernel parameter matters. With $h_{\sigma}(t)=\operatorname{Sa}(\pi t/\sigma)$ and fixed sample spacing $T$, exact interpolation requires zero crossings at the other sampling instants, so $\sigma=T$. Larger $\sigma$ gives a wider time kernel (zero crossings farther apart) and a narrower frequency selector; smaller $\sigma$ gives the opposite. If $\sigma>T$, the kernel is too wide and neighboring samples do not cancel properly. If $\sigma<T$, the kernel is too narrow and the zero crossings come too quickly.

---

Flashcards for this section are as follows:

- How is perfect reconstruction achieved in frequency? ::@:: Use an ideal LPF to keep the central spectral replica and reject the others.
- Why must the reconstruction LPF have gain $T$? ::@:: The sampled spectrum copies are scaled by $1/T$, so the filter must multiply by $T$ to restore original amplitude.
- What is the ideal interpolation formula? ::@:: $x(t)=\sum_{n=-\infty}^{\infty}x(nT)\operatorname{Sa}(\pi (t-nT)/T)$.
- Why does the interpolation pass exactly through sample values? ::@:: Each shifted kernel equals $1$ at its own sample and $0$ at all others.
- Why is $\sigma=T$ required in $h_{\sigma}(t)=\operatorname{Sa}(\pi t/\sigma)$? ::@:: Zero crossings must land at the other sampling instants spaced by $T$.
- How does changing $\sigma$ affect the kernel and frequency selector? ::@:: Larger $\sigma$ gives a wider time kernel and narrower frequency selector; smaller $\sigma$ gives the opposite.
- Why does this section use $\sigma$ instead of $\tau$ for interpolation-kernel scale? ::@:: To avoid notation collision with $\tau$ commonly used as rectangular-pulse width in transform-pair formulas. Here $\sigma$ is reserved for interpolation-kernel scaling.
- Why is convolution with a sinc kernel the right reconstruction operation? ::@:: Because the reconstruction filter $H_r(\omega)$ is rectangular in frequency, so its impulse response is sinc in time. Convolution with this kernel selects the central spectral replica.
- Why is Sa / $\operatorname{sinc}_{\pi}$ called the ideal interpolation kernel for uniform sampling? ::@:: It is the exact reconstruction kernel from the ideal rectangular low-pass filter. Each shifted kernel equals $1$ at its own sampling instant and $0$ at all others, so neighboring samples do not interfere.
- How do you derive the sinc interpolation formula from the reconstruction filter? ::@:: Convolve the sampled impulse train $x_s(t)=\sum_n x(nT)\delta(t-nT)$ with $h_r(t)=\operatorname{Sa}(\pi t/T)$. Each shifted impulse produces $x(nT)h_r(t-nT)$; summing gives the interpolation formula.

## practical reconstruction filters

Ideal sinc reconstruction is exact but infinitely long in both time directions. Practical systems use simpler hold circuits.

The zero-order hold (ZOH) keeps each sample constant until the next arrives: $h_{\mathrm{ZOH}}(t)=u(t)-u(t-T)$, a rectangular pulse of width $T$. In frequency, $H_{\mathrm{ZOH}}(\omega)=T e^{-j\omega T/2}\operatorname{Sa}(\omega T/2)$. Each sample value drives a hold circuit (commonly modeled as a switch-plus-capacitor or DAC output stage), and the output stays flat until the next sampling instant.

The first-order hold (FOH) connects adjacent samples with straight lines: $h_{\mathrm{FOH}}(t)=\Lambda((t-T)/T)$, a delayed triangular pulse of width $2T$. In frequency, $H_{\mathrm{FOH}}(\omega)=T e^{-j\omega T}\operatorname{Sa}^{2}(\omega T/2)$. The implementation is a linear ramp generator or linear interpolator.

Both are approximate. ZOH is easy to implement but gives staircase output and high-frequency droop. FOH is smoother but still not ideal. Finite, causal circuits are easier to build than an infinite two-sided sinc filter.

---

Flashcards for this section are as follows:

- What is ZOH's impulse response and output shape? ::@:: $h_{\mathrm{ZOH}}(t)=u(t)-u(t-T)$; it produces a staircase waveform holding each sample constant.
- What is FOH's impulse response and output shape? ::@:: $h_{\mathrm{FOH}}(t)=\Lambda((t-T)/T)$; it produces piecewise linear segments between samples.
- How do ZOH and FOH compare with ideal sinc reconstruction? ::@:: Ideal sinc is exact but infinite. ZOH is simpler but staircase. FOH is smoother but still approximate.
- How do you draw the ZOH block diagram? ::@:: $x[n] \to$ ideal impulse DAC $\to h_{\mathrm{ZOH}}(t)$; output is a staircase holding each sample constant.
- How do you draw the FOH block diagram? ::@:: $x[n] \to$ ideal impulse DAC $\to h_{\mathrm{FOH}}(t)$; output is piecewise linear between samples.
- Why are ZOH and FOH used in practice? ::@:: They are finite, causal, and easy to implement, whereas ideal sinc reconstruction has an infinite two-sided impulse response.

## aliasing and anti-aliasing

Aliasing is the failure mode of undersampling. If $\omega_s<2\omega_m$, replicated spectra overlap and different continuous-time frequencies produce the same sample sequence.

The standard example: sampling $10\text{ Hz}$ and $30\text{ Hz}$ cosines at $40\text{ Hz}$ gives the same sequence, since digital frequency is modulo $2\pi$.

The remedy is anti-aliasing: a low-pass filter before the sampler removes content above $f_s/2$. Anti-aliasing after sampling cannot undo overlap that has already happened.

A direct example: $x(t)=\cos(10t)$ sampled at $\omega_s=14\text{ rad/s}$ (below the Nyquist $20\text{ rad/s}$) gives $x[n]=\cos(10\pi n/7)=\cos(4\pi n/7)$. The samples are indistinguishable from a $4\text{ rad/s}$ cosine. The alias at $\omega_s-10=4$ is baked into the samples.

The practical point: inputs are rarely strictly bandlimited. Without a prefilter, high-frequency content folds into false low-frequency components, which is worse than simply losing the high-frequency content. With a prefilter, only the removed high-frequency content is lost, but no spurious low-frequency content is added.

The block diagram: $x(t) \to$ anti-aliasing LPF $\to$ sampler $\to x_d[n]$.

This appears in many settings: digital telephony removes content above $4\text{ kHz}$ before $8\text{ kHz}$ sampling; thumbnail generation low-pass filters to avoid Moiré; cameras use optical blur before the sensor.

---

Flashcards for this section are as follows:

- What is aliasing? ::@:: Undersampling causes spectral copies to overlap, mixing different continuous-time frequencies.
- Why does aliasing destroy unique reconstruction? ::@:: Once spectral copies overlap, several different original continuous-time spectra can produce the same sampled sequence.
- What is an anti-aliasing filter? ::@:: A low-pass filter placed before the sampler to remove frequency components above half the sampling frequency so spectral replicas will not overlap.
- What is the key intuition behind aliasing? ::@:: Sampling remembers only normalized digital frequency, so different analog frequencies that differ by multiples of the sampling rate can collapse onto the same discrete-time oscillation.
- Why is anti-aliasing done before sampling? ::@:: Once aliasing folds frequencies together, the distinction cannot be recovered.
- If $x(t)=\cos(10t)$ is sampled at $\omega_s=14$, what alias appears? ::@:: The $10\text{ rad/s}$ cosine aliases to $4\text{ rad/s}$, since $\omega_s-10=4$.
- What does the anti-aliasing block diagram look like? ::@:: $x(t) \to$ LPF $\to$ sampler $\to x_d[n]$.
- With an anti-aliasing filter, what error remains? ::@:: Only the removed high-frequency content is lost. Without the filter, those components also fold into false low-frequency components, which is worse.

## reading maximum sampling interval from a spectrum

Workflow for sampling-interval questions: (1) read the highest spectral edge $\omega_m$ or $f_m$, (2) compute $T_{\max}=\pi/\omega_m=1/(2f_m)$, (3) sketch the sampled spectrum by placing copies every $\omega_s=2\pi/T$, scaling heights by $1/T$.

At the Nyquist limit, the central copy occupies $|\omega|\le\omega_m$, adjacent copies center at $\pm2\omega_m$, and they just touch at $\omega=\pm\omega_m$.

This workflow applies to the actual signal entering the sampler, not an earlier signal in the chain.

---

Flashcards for this section are as follows:

- What three-step workflow finds $T_{\max}$ and sketches the sampled spectrum? ::@:: (1) Read $\omega_m$. (2) Compute $T_{\max}=\pi/\omega_m$. (3) Sketch copies every $\omega_s=2\pi/T$.
- If $F(\omega)$ is nonzero for $|\omega|\le\omega_m$, what is $T_{\max}$ and the sampled spectrum? ::@:: $T_{\max}=\pi/\omega_m$; $F_s(\omega)=\frac{1}{T_{\max}}\sum_k F(\omega-2k\omega_m)$ with replicas just touching at $\omega=\pm\omega_m$.
- Why must the Nyquist condition use the bandwidth at the sampler input? ::@:: Spectral overlap depends on the actual highest frequency present when sampling occurs.
