---
aliases:
  - ELEC 2100 amplitude modulation
  - ELEC 2100 modulation
  - ELEC2100 modulation
  - HKUST ELEC 2100 modulation
  - amplitude modulation
  - demodulation
  - frequency division multiplexing
  - modulation
  - time division multiplexing
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/modulation
  - language/in/English
---

# modulation

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Modulation moves a baseband signal to a carrier band suited for transmission, channel separation, and multiplexing. The path is _baseband → frequency translation → channel filtering → demodulation → low-pass recovery_.

---

Flashcards for this section are as follows:

- What is modulation? ::@:: It shifts a baseband signal to a carrier band for transmission and channel separation.
- What is demodulation? ::@:: It reverses that carrier translation to recover the original signal at baseband.

## communication setting and channel constraints

A communication system: message source $\to$ transmitter $\to$ channel $\to$ receiver $\to$ recovered message. The baseband signal $g(t)$ is the original waveform. The carrier $\cos(\omega_0 t)$ moves the message spectrum into a passband suited to the channel.

Modulation does not change the information. It puts the signal into a form that fits the channel's physics and regulation. A transmitter uses a local oscillator, mixer, filters, and sometimes an amplifier. A receiver uses a BPF, mixer, local oscillator, LPF for baseband recovery, and a gain or decision stage.

A multiplier translates spectra, a BPF picks one channel, and an LPF recovers baseband. Block diagrams make these roles visible before any algebra.

---

Flashcards for this section are as follows:

- Why does modulation not change information content? ::@:: Its purpose is spectral relocation for transmission, not message alteration.
- What blocks appear in a practical mod/demod chain? ::@:: Transmitter: local oscillator, mixer, filters, amplifier. Receiver: BPF, mixer, local oscillator, LPF, gain/decision stage.
- What is the baseband signal? ::@:: The original information-bearing waveform before carrier translation.
- What is the carrier? ::@:: A higher-frequency reference, typically $\cos(\omega_0 t)$, that moves the baseband spectrum to a new band.
- Why are BPF and LPF already needed before seeing formulas? ::@:: Because modulation is spectrum placement and selection, so channel and recovery filters are inherent to the idea.

## why modulation is needed

Modulation is motivated by channel constraints, not algebra. A baseband signal may not lie in a frequency region that propagates well, radiates efficiently through an antenna, or survives attenuation. Frequency translation moves it into a better band.

Spectrum sharing is the second reason. Radio, microwave, and fiber resources are crowded. Multiple users must coexist in nearby bands, so modulation places each message in an assigned band and filters prevent spilling into neighbors.

Three reasons: adapt to the channel, separate users spectrally, and make receiver-side recovery practical.

---

Flashcards for this section are as follows:

- Why is modulation needed? ::@:: The channel may not support the baseband spectrum, and multiple users must share the medium without interference.
- What are the three reasons for modulation? ::@:: Adapt the signal to the channel, separate users spectrally, and make receiver-side recovery practical.
- Why do closely packed channels increase filtering importance? ::@:: Poor filtering causes one channel's energy to spill into a neighboring channel's band.

## common modulation methods: ASK, FSK, and PSK

Modulation families differ in which carrier property carries information. Amplitude-based: message changes carrier height. Frequency-based: message changes oscillation rate. Phase-based: message changes cycle position.

In ASK, $s_i(t)=A_i\cos(\omega_c t)$. Same frequency and phase, different amplitudes. The envelope height is the information.

In FSK, $s_i(t)=A\cos(\omega_i t)$. Same amplitude, different frequencies. Zero-crossing spacing carries the information.

In PSK, $s_i(t)=A\cos(\omega_c t+\phi_i)$. Same amplitude and frequency, phase changes. Binary PSK flips sign when $\phi$ jumps by $\pi$.

Analog AM varies amplitude continuously; ASK uses discrete levels. FSK and PSK place information in rate or phase instead.

---

Flashcards for this section are as follows:

- What are ASK, FSK, and PSK? ::@:: ASK: $s_i=A_i\cos(\omega_c t)$, information in amplitude. FSK: $s_i=A\cos(\omega_i t)$, information in frequency. PSK: $s_i=A\cos(\omega_c t+\phi_i)$, information in phase.
- How does analog AM differ from ASK? ::@:: AM varies amplitude continuously; ASK uses discrete levels chosen by symbols.
- What does ASK transmit physically? ::@:: Carrier with same frequency/phase but varying amplitude. Envelope height carries information.
- What does FSK transmit physically? ::@:: Carrier with same amplitude but varying frequency. Zero-crossing spacing carries information.
- What does PSK transmit physically? ::@:: Carrier with same amplitude/frequency but varying phase. Phase offsets or flips carry information.

## trigonometric identities behind modulation

Modulation algebra is sinusoid multiplication. Start from Euler: $\cos a=\frac12(e^{ja}+e^{-ja})$, $\sin a=\frac{1}{2j}(e^{ja}-e^{-ja})$. Products of exponentials add exponents, generating sum and difference frequencies.

$\cos a\cos b=\frac12[\cos(a+b)+\cos(a-b)]$.

$\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$.

$\cos^2 a=\frac12[1+\cos(2a)]$ follows by setting $b=a$.

Recall: multiplication in time $\to$ splitting in frequency. One product creates a difference-frequency part and a sum-frequency part.

---

Flashcards for this section are as follows:

- What are the key Euler formulas? ::@:: $\cos a=\frac12(e^{ja}+e^{-ja})$ and $\sin a=\frac{1}{2j}(e^{ja}-e^{-ja})$.
- What identities does sinusoid multiplication produce? ::@:: $\cos a\cos b=\frac12[\cos(a+b)+\cos(a-b)]$ and $\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$.
- Why does $\cos^2 a=\frac12[1+\cos(2a)]$? ::@:: Set $b=a$ in the cosine product identity.
- Why do modulation identities create sum and difference frequencies? ::@:: Exponentials add exponents when multiplied, so one product generates an inner difference-frequency and outer sum-frequency term.

## suppressed-carrier amplitude modulation

AM-SC: multiply baseband $g(t)$ by carrier $\cos(\omega_0 t)$ to get $f(t)=g(t)\cos(\omega_0 t)$. The multiplier is a mixer or balanced modulator.

By Euler, $F(\omega)=\frac12 G(\omega-\omega_0)+\frac12 G(\omega+\omega_0)$. The baseband spectrum is copied to $\pm\omega_0$, each scaled by $\frac12$.

For a single-tone message $g(t)=A\cos(\omega_m t)$: $f(t)=\frac{A}{2}\cos((\omega_0+\omega_m)t)+\frac{A}{2}\cos((\omega_0-\omega_m)t)$. The output is two sidebands, each at amplitude $A/2$, not the carrier plus a message riding on it.

Suppressed-carrier means no large carrier line is transmitted. The $\frac12$ factor splits the message into two copies. Practical transmitters compensate with gain stages or active mixers.

---

Flashcards for this section are as follows:

- What is AM-SC? ::@:: $f(t)=g(t)\cos(\omega_0 t)$. The baseband spectrum copies to $\pm\omega_0$, each scaled by $\frac12$.
- What does a single-tone AM-SC signal look like? ::@:: Two sidebands: $\frac{A}{2}\cos((\omega_0+\omega_m)t)+\frac{A}{2}\cos((\omega_0-\omega_m)t)$, each at amplitude $A/2$.
- Why is each sideband scaled by $\frac12$? ::@:: Because $\cos(\omega_0 t)=\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$ splits the message into two half-weight copies.
- How do transmitters compensate for the $\frac12$ scaling? ::@:: Gain stages, active mixers with conversion gain, or larger local-oscillator amplitude restore the desired passband level.

## coherent demodulation and low-pass recovery

Coherent demodulation: multiply received AM-SC by $\cos(\omega_0 t)$, then low-pass filter. The LPF is necessary because remultiplication creates both the baseband term and high-frequency images.

$f(t)\cos(\omega_0 t)=g(t)\cos^2(\omega_0 t)=\frac12 g(t)+\frac12 g(t)\cos(2\omega_0 t)$. In frequency: $\frac12 G(\omega)+\frac14 G(\omega-2\omega_0)+\frac14 G(\omega+2\omega_0)$. The baseband copy has factor $\frac12$, the residual images have factor $\frac14$ each.

Why $\frac12$? The first multiplication splits the message into two half-size sidebands. The second splits each again. Two inner quarter-copies add at baseband to $\frac12$; two outer quarter-copies land near $\pm 2\omega_0$ and are filtered out.

Recovery condition: if $G(\omega)$ is in $|\omega|<\omega_m$, choose $\omega_0>\omega_m$ and LPF cutoff $\omega_m<\omega_c<2\omega_0-\omega_m$. Coherent (synchronous) means the receiver carrier must match in frequency and phase.

Other receiver types: envelope detection (ordinary AM with carrier), I/Q demodulation, superheterodyne, PLL/Costas-loop carrier recovery, noncoherent detectors for ASK/FSK.

Worked example: $g(t)=\cos(200t)$, carrier $\cos(1000t)$. After remultiplication: baseband at $\pm 200$, unwanted images at $\pm 1800$ and $\pm 2200$. Any LPF cutoff with $200<\omega_c<1800$ works.

Spectrum trace (A $=$ input, B $=$ after first multiply, C $=$ after BPF, D $=$ after remultiply, E $=$ after LPF): $F_E(\omega)=\frac12 F(\omega)$, so $y(t)=\frac12 f(t)$. Gain-$2$ restores $y(t)=f(t)$.

---

Flashcards for this section are as follows:

- What does coherent demodulation do? ::@:: Multiplies by $\cos(\omega_0 t)$ then low-pass filters. Output: $\frac12 g(t)+\frac12 g(t)\cos(2\omega_0 t)$.
- Why is the recovered baseband scaled by $\frac12$? ::@:: The first multiply splits into two half-size sidebands; the second splits each again. Two inner quarter-copies add to $\frac12$ at baseband.
- What is the recovery condition? ::@:: $\omega_0>\omega_m$ and LPF cutoff $\omega_m<\omega_c<2\omega_0-\omega_m$.
- What does "coherent" mean here? ::@:: The receiver carrier must match the transmitter carrier in frequency and phase.
- Worked example: $g(t)=\cos(200t)$, carrier $\cos(1000t)$, what LPF cutoff works? ::@:: Any $200<\omega_c<1800$ passes the message and rejects the nearest images at $\pm 1800$, $\pm 2200$.
- What is the spectrum trace result? ::@:: $F_E(\omega)=\frac12 F(\omega)$, so $y(t)=\frac12 f(t)$. Gain-$2$ restores $y(t)=f(t)$.

## multiplexing and channel filters

FDM assigns different carriers to different messages. Channel $k$: $s_k(t)=g_k(t)\cos(\omega_k t)$, $S_k(\omega)=\frac12 G_k(\omega-\omega_k)+\frac12 G_k(\omega+\omega_k)$. If carrier spacing exceeds message bandwidths, channels coexist without overlap.

Demultiplexing: BPF selects channel $k$, multiply by $\cos(\omega_k t)$, LPF recovers baseband. The BPF is the extra block vs. single-channel demodulation.

Ideal BPF for channel at $\omega_0$ with half-bandwidth $\omega_c$: $H_{\mathrm{BP}}(\omega)=1$ for $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$. Impulse response: $h_{\mathrm{BP}}(t)=\frac{\sin((\omega_0+\omega_c)t)-\sin((\omega_0-\omega_c)t)}{\pi t}$, a shifted sinc kernel.

TDM places users in different time slots of one frame. A clocked switch interleaves transmitter inputs; synchronized switching plus reconstruction filters separate them at the receiver. FDM separates by frequency; TDM separates by timing.

In FDM, spectra form separated passband islands. In TDM, slotting broadens spectra and creates frame-related repetition. FDM cares about carrier placement and guard bands; TDM cares about timing accuracy and reconstruction.

FDM example: three signals bandlimited to $|\omega|<B$ on carriers $\omega_1<\omega_2<\omega_3$. Channel $k$ occupies $[\omega_k-B,\omega_k+B]$. Adjacent carriers must be separated enough to prevent overlap.

---

Flashcards for this section are as follows:

- What is FDM? ::@:: Different messages modulated onto different carriers. Channel $k$: $S_k=\frac12 G_k(\omega-\omega_k)+\frac12 G_k(\omega+\omega_k)$. Channels coexist if carrier spacing exceeds bandwidths.
- How is one FDM channel recovered? ::@:: BPF centered at $\omega_k$, multiply by $\cos(\omega_k t)$, LPF to baseband.
- What is TDM? ::@:: Users occupy different time slots of a repeating frame. A clocked switch interleaves at the transmitter; synchronized switching separates at the receiver.
- FDM vs. TDM? ::@:: FDM separates by frequency (BPFs, carrier placement). TDM separates by timing (synchronization, reconstruction filters).
- What is the ideal BPF formula for a channel at $\omega_0$ with half-bandwidth $\omega_c$? ::@:: $H_{\mathrm{BP}}(\omega)=1$ for $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$, impulse response $h_{\mathrm{BP}}(t)=\frac{\sin((\omega_0+\omega_c)t)-\sin((\omega_0-\omega_c)t)}{\pi t}$.
- How do you draw an FDM transmitter? ::@:: One message path per channel, each with its own modulator and local oscillator, then a BPF, then an adder combining all outputs.
- How do you draw FDM demultiplexing? ::@:: Composite signal → BPF isolating one channel → product detector with matching carrier → LPF → recovered message.

## other multiplexing methods

Beyond FDM and TDM: code-division multiplexing (separates by codes), OFDM (orthogonal multicarrier FDM), wavelength-division multiplexing (optical wavelengths), space-division multiplexing (different propagation paths or spatial modes).

All share one idea: choose a resource dimension where signals are distinguishable, then design modulation, filtering, and detection for separable channels.

Pulse shape still matters after modulation. Sharper time-domain gating spreads spectral sidelobes; smoother shaping reduces neighboring-channel interference.

---

Flashcards for this section are as follows:

- What multiplexing methods exist beyond FDM and TDM? ::@:: Code-division, OFDM, wavelength-division, and space-division multiplexing.
- What do all multiplexing methods have in common? ::@:: They choose a resource dimension where signals are distinguishable and design the system for separable channels.
