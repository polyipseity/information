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

Modulation moves a signal from its original baseband location to a new spectral location that is more convenient for transmission, channel separation, filtering, and multiplexing. The central engineering picture is _baseband message $\to$ frequency translation $\to$ channel filtering and combining $\to$ channel selection $\to$ demodulation $\to$ low-pass recovery_. This note follows that path from physical motivation, to waveform formulas, to practical block-diagram implementations.

---

Flashcards for this section are as follows:

- What core communication idea does the modulation note explain in ELEC 2100? ::@:: It explains how a baseband message is translated to a carrier-centered band so transmission, channel separation, and receiver recovery become practical. <!--SR:!2026-05-16,15,290!2026-05-18,17,310-->
- What is modulation in one sentence? ::@:: It is the process of multiplying or otherwise combining an information-carrying signal with a carrier so the message spectrum moves into a more useful frequency region. <!--SR:!2026-05-16,15,290!2026-05-18,17,310-->
- What is demodulation in one sentence? ::@:: It is the process of reversing that carrier translation so the original information-bearing signal is recovered at baseband. <!--SR:!2026-05-15,14,290!2026-05-18,17,310-->

## communication setting, channel constraints, and implementation overview

A communication system is usually drawn conceptually as message source $\to$ transmitter $\to$ channel $\to$ receiver $\to$ recovered message. The baseband signal is the original information-bearing waveform, denoted here by $g(t)$. The carrier is a higher-frequency reference such as $\cos(\omega_0 t)$ used to move the message spectrum into a passband better suited to the channel.

The point of modulation is not to change the information itself. The point is to place that information into a form that fits the physics, regulation, and sharing requirements of the channel. On the transmitter side, this often means a local oscillator, a multiplier or mixer, channel-selective filters, and sometimes a power amplifier. On the receiver side, this often means a front-end band-pass filter, a mixer or product detector, a local oscillator, a low-pass filter for baseband recovery, and a gain stage or decision stage afterward.

This already explains why modulation and demodulation are system-level ideas rather than isolated formulas. A multiplier translates spectra, a band-pass filter picks one channel, and a low-pass filter brings the message back to baseband. Good block diagrams make those roles visible before any algebra is written.

---

Flashcards for this section are as follows:

- What basic communication-chain picture underlies modulation and demodulation? ::@:: A message source produces a baseband signal, the transmitter translates it to a carrier band, the channel carries it, and the receiver translates it back to recover the original information. <!--SR:!2026-05-17,16,290!2026-05-17,16,290-->
- What is the baseband signal in this note? ::@:: It is the original information-bearing waveform before it is shifted to a carrier-centered band. <!--SR:!2026-05-18,17,310!2026-05-16,15,290-->
- What is the carrier in this modulation note? ::@:: It is a higher-frequency reference waveform, typically $\cos(\omega_0 t)$, used to move the baseband spectrum into a new frequency region. <!--SR:!2026-05-15,14,290!2026-05-16,15,290-->
- Why does modulation not change the information content in principle? ::@:: Because its purpose is to relocate the signal spectrally for transmission, not to alter the message itself. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- What blocks commonly appear in a practical modulation and demodulation chain? ::@:: A transmitter often uses a local oscillator, mixer or multiplier, filters, and sometimes an amplifier. A receiver often uses a front-end BPF, a mixer or product detector, a synchronized local oscillator, an LPF for baseband recovery, and then gain or decision circuitry. <!--SR:!2026-05-15,14,290!2026-05-18,17,310-->
- Why are BPF and LPF blocks already conceptually present before the detailed formulas? ::@:: Because modulation is really spectrum placement and spectrum selection, so channel filters and baseband-recovery filters are part of the idea from the beginning. <!--SR:!2026-05-17,16,290!2026-05-18,17,310-->

## why modulation is needed

Modulation is motivated by channel constraints rather than by algebra alone. A baseband signal may not lie in a frequency region that propagates well through the medium, radiates efficiently through an antenna, or survives channel attenuation cleanly. Frequency translation solves that by moving the signal into a more convenient transmission band.

Spectrum sharing is the second major reason. Radio, microwave, fiber, and other communication resources are crowded and highly regulated. Multiple users or services may need to coexist in nearby channels, so frequency allocation becomes both a technical and an economic problem. Good modulation moves each message to an assigned band, and good filters keep that band from spilling into its neighbors.

So the motivation for modulation is three-layered: adapt the signal to the channel, place different users in different bands, and make receiver-side separation practical.

---

Flashcards for this section are as follows:

- Why is modulation needed even if a baseband signal is already mathematically well defined? ::@:: Because the useful transmission channel may work well only over certain frequency ranges, and the message spectrum often has to be moved into that range. <!--SR:!2026-05-15,14,290!2026-05-16,15,290-->
- Why is crowded spectrum an engineering reason for modulation? ::@:: Because many users must coexist in nearby bands, so modulation is what places each signal into an assigned spectral region where filters can separate it from the others. <!--SR:!2026-05-16,15,290!2026-05-18,17,310-->
- Why do closely packed channels increase the importance of LPFs and BPFs? ::@:: Because when neighboring channels are close together, poor filtering causes one channel's energy to spill into another channel's band. <!--SR:!2026-05-16,15,290!2026-05-17,16,290-->
- What are the three main reasons for using modulation? ::@:: Adapt the signal to the transmission medium, separate different users or services spectrally, and make receiver-side filtering and recovery practical. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->

## common modulation methods: ASK, FSK, and PSK

The most common modulation families are grouped by what part of the carrier is allowed to carry the information. In amplitude-based schemes, the message changes how tall the carrier is. In frequency-based schemes, the message changes how fast the carrier oscillates. In phase-based schemes, the message changes where the carrier sits on its cycle.

In amplitude-shift keying (ASK), the transmitted waveform is $s_i(t)=A_i\cos(\omega_c t)$. The carrier frequency and phase stay the same, but different symbols choose different amplitudes. On a scope, ASK looks like the same carrier with taller or shorter bursts, so the envelope height is the information-bearing part.

In frequency-shift keying (FSK), the transmitted waveform is $s_i(t)=A\cos(\omega_i t)$. The amplitude stays fixed, but different symbols use different carrier frequencies. Visually, the waveform alternates between slower and faster oscillation rates, so the spacing of the zero crossings carries the information.

In phase-shift keying (PSK), the transmitted waveform is $s_i(t)=A\cos(\omega_c t+\phi_i)$. The amplitude and carrier frequency stay fixed, but the phase changes with the symbol. In binary PSK, for example, the two main possibilities are $A\cos(\omega_c t)$ and $A\cos(\omega_c t+\pi)=-A\cos(\omega_c t)$, so the carrier keeps the same frequency and amplitude but flips sign when the phase jumps by $\pi$.

This gives a useful comparison with analog amplitude modulation. Analog AM lets a continuous message waveform change the carrier amplitude continuously, while ASK uses only a finite set of allowed amplitude levels. So ASK is the digital cousin of AM, while FSK and PSK place the information in oscillation rate or phase instead.

---

Flashcards for this section are as follows:

- What are the three common modulation families highlighted here besides analog AM? ::@:: ASK, FSK, and PSK, corresponding to placing the information in amplitude, frequency, or phase. <!--SR:!2026-05-18,17,310!2026-05-16,15,290-->
- What is the transmitted waveform and physical interpretation of ASK? ::@:: ASK uses $s_i(t)=A_i\cos(\omega_c t)$, so the carrier keeps the same frequency but appears as taller or shorter bursts. The information rides on envelope height. <!--SR:!2026-05-17,16,290!2026-05-15,14,290-->
- What is the transmitted waveform and physical interpretation of FSK? ::@:: FSK uses $s_i(t)=A\cos(\omega_i t)$, so the amplitude stays fixed but the oscillation rate changes from one symbol to another. The information rides on which frequency is present. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- What is the transmitted waveform and physical interpretation of PSK? ::@:: PSK uses $s_i(t)=A\cos(\omega_c t+\phi_i)$, so amplitude and frequency stay fixed while the phase changes. The information rides on phase offsets or phase jumps. <!--SR:!2026-05-15,14,290!2026-05-17,16,290-->
- How should you compare analog AM with ASK? ::@:: Analog AM uses a continuous message waveform to vary carrier amplitude, while ASK uses a finite set of amplitude levels chosen by digital symbols. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- What quick comparison helps distinguish ASK, FSK, and PSK? ::@:: ASK changes how tall the carrier is, FSK changes how fast it oscillates, and PSK changes where on the cycle the carrier starts or flips. <!--SR:!2026-05-15,14,290!2026-05-17,16,290-->

## trigonometric identities behind modulation

The algebra of modulation is really the algebra of multiplying sinusoids, and the cleanest way to remember those identities is to start from Euler's formulas $\cos a=\frac12(e^{ja}+e^{-ja})$ and $\sin a=\frac{1}{2j}(e^{ja}-e^{-ja})$. Products of sinusoids generate sum and difference frequencies because products of exponentials add exponents.

For cosine-cosine multiplication, expand everything explicitly: $\cos a\cos b=\frac12(e^{ja}+e^{-ja})\cdot\frac12(e^{jb}+e^{-jb})=\frac14(e^{j(a+b)}+e^{j(a-b)}+e^{-j(a-b)}+e^{-j(a+b)})$. Now group the sum-frequency pair and the difference-frequency pair: $\cos a\cos b=\frac14[(e^{j(a+b)}+e^{-j(a+b)})+(e^{j(a-b)}+e^{-j(a-b)})]=\frac12[\cos(a+b)+\cos(a-b)]$.

For the mixed product, do the same thing: $\sin a\cos b=\frac{1}{2j}(e^{ja}-e^{-ja})\cdot\frac12(e^{jb}+e^{-jb})=\frac{1}{4j}(e^{j(a+b)}+e^{j(a-b)}-e^{-j(a-b)}-e^{-j(a+b)})$. Group the terms again, then turn each conjugate pair back into a sine: $\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$.

The identity $\cos^2 a=\frac12[1+\cos(2a)]$ is just the special case $b=a$ of the cosine-cosine rule. Setting $b=a$ gives $\cos^2 a=\frac12[\cos 0+\cos(2a)]=\frac12[1+\cos(2a)]$. This is the exact reason coherent demodulation produces one baseband term and one doubled-carrier term.

The fastest recall cue is that time-domain multiplication becomes spectral splitting because exponentials add angles. One product creates an inner difference-frequency part and an outer sum-frequency part. In modulation, those two pieces become translated spectra.

---

Flashcards for this section are as follows:

- What are the two Euler formulas used most often in modulation derivations? ::@:: They are $\cos a=\frac12(e^{ja}+e^{-ja})$ and $\sin a=\frac{1}{2j}(e^{ja}-e^{-ja})$. <!--SR:!2026-05-17,16,290!2026-05-18,17,310-->
- How do you derive $\cos a\cos b=\frac12[\cos(a+b)+\cos(a-b)]$ step by step? ::@:: Replace each cosine by $\frac12(e^{j\cdot}+e^{-j\cdot})$, expand to get four exponentials, group the $\pm(a+b)$ terms and the $\pm(a-b)$ terms, then convert each conjugate pair back into a cosine. The result is $\frac12[\cos(a+b)+\cos(a-b)]$. <!--SR:!2026-05-15,14,290!2026-05-18,17,310-->
- How do you derive $\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)]$ step by step? ::@:: Replace $\sin a$ by $\frac{1}{2j}(e^{ja}-e^{-ja})$ and $\cos b$ by $\frac12(e^{jb}+e^{-jb})$, expand, group the $\pm(a+b)$ and $\pm(a-b)$ pairs, and convert each pair back into a sine. The result is $\frac12[\sin(a+b)+\sin(a-b)]$. <!--SR:!2026-05-18,17,310!2026-05-16,15,290-->
- Why does $\cos^2 a=\frac12[1+\cos(2a)]$ follow immediately from the cosine product identity? ::@:: Set $b=a$ in $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$. Then $\cos(a-a)=\cos 0=1$ and $\cos(a+a)=\cos(2a)$. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- Why do modulation identities naturally create sum and difference frequencies? ::@:: Because after rewriting sinusoids as exponentials, multiplication adds exponents, so one product automatically generates an inner difference-frequency term and an outer sum-frequency term. <!--SR:!2026-05-18,17,310!2026-05-15,14,290-->

## suppressed-carrier amplitude modulation

The standard model here is suppressed-carrier amplitude modulation (AM-SC). In block-diagram form, draw the baseband message $g(t)$ entering a multiplier from the left, draw the carrier $\cos(\omega_0 t)$ entering the same block from a second port, and label the output as $f(t)=g(t)\cos(\omega_0 t)$. In hardware language, that multiplier is a mixer or balanced modulator. A practical transmitter may then add a band-pass filter and a power amplifier before the channel.

Using Euler's formula, $\cos(\omega_0 t)=\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$, so $f(t)=\frac12 g(t)e^{j\omega_0 t}+\frac12 g(t)e^{-j\omega_0 t}$. If $G(\omega)$ is the transform of $g(t)$, the frequency-shifting property gives $F(\omega)=\frac12 G(\omega-\omega_0)+\frac12 G(\omega+\omega_0)$. So the baseband spectrum is copied twice, once around $+\omega_0$ and once around $-\omega_0$, and each copy has one-half the original spectral magnitude in this normalized unit-carrier model.

The waveform picture becomes especially clear for a single-tone message $g(t)=A\cos(\omega_m t)$. Then $f(t)=A\cos(\omega_m t)\cos(\omega_0 t)=\frac{A}{2}\cos((\omega_0+\omega_m)t)+\frac{A}{2}\cos((\omega_0-\omega_m)t)$. So the transmitted waveform is not one tone at the carrier frequency plus a message riding on top of it. It is the sum of an upper sideband tone and a lower sideband tone, each with amplitude $A/2$. Visually, the carrier oscillation is still present, but the information has been moved into the sideband structure around that carrier region.

The phrase suppressed-carrier means that the message is translated without adding a separate large carrier line for transmission. The factor $1/2$ in each sideband is also important physically: without additional amplification, modulation by a unit-amplitude cosine splits the message into two translated copies rather than preserving the original amplitude in each one. Practical transmitters often compensate with later gain stages, higher local-oscillator amplitude inside the mixer, or active mixers that provide conversion gain.

---

Flashcards for this section are as follows:

- How should you draw and interpret the basic AM-SC transmitter block diagram? ::@:: Draw $g(t)$ entering a multiplier or mixer, draw $\cos(\omega_0 t)$ entering the same block from a second input, label the output $f(t)=g(t)\cos(\omega_0 t)$, and then place any channel BPF or amplifier to the right. The multiplier is what actually performs the frequency translation. <!--SR:!2026-05-16,15,290!2026-05-16,15,290-->
- What is the formula for suppressed-carrier amplitude modulation? ::@:: It is $f(t)=g(t)\cos(\omega_0 t)$, where $g(t)$ is the modulating signal and $\omega_0$ is the carrier angular frequency. <!--SR:!2026-05-15,14,290!2026-05-16,15,290-->
- Starting from $f(t)=g(t)\cos(\omega_0 t)$, how do Euler's formula and frequency shifting produce the modulation spectrum? ::@:: Write $\cos(\omega_0 t)=\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$, expand the product into two terms, and then apply frequency shifting to obtain $F(\omega)=\frac12 G(\omega-\omega_0)+\frac12 G(\omega+\omega_0)$. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- What is the most important geometric picture to remember for AM-SC in frequency? ::@:: The baseband spectrum is copied twice and shifted to be centered at $+\omega_0$ and $-\omega_0$, with each copy scaled by $1/2$. <!--SR:!2026-05-15,14,290!2026-05-18,17,310-->
- If $g(t)=A\cos(\omega_m t)$, what transmitted waveform does AM-SC produce, and how should you interpret it? ::@:: It gives $f(t)=\frac{A}{2}\cos((\omega_0+\omega_m)t)+\frac{A}{2}\cos((\omega_0-\omega_m)t)$. <br/> So the passband signal is the sum of an upper sideband and a lower sideband, each with amplitude $A/2$. <!--SR:!2026-05-17,16,290!2026-05-12,11,270-->
- Why does modulation by a unit-amplitude cosine produce one-half scaling in each sideband? ::@:: Because $\cos(\omega_0 t)=\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$ already contains two half-weight complex exponentials, so the message is split into two translated copies rather than copied once at full strength. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- How do practical transmitters compensate for the one-half scaling introduced by normalized modulation? ::@:: They use later gain stages, active mixers with conversion gain, or a larger effective local-oscillator scaling, so the transmitted passband level is restored to the desired power. <!--SR:!2026-05-15,14,290!2026-05-15,14,290-->

## coherent demodulation, low-pass recovery, and implementation

Coherent demodulation multiplies the received AM-SC signal by a synchronized copy of the carrier and then _low-pass filters_ the result. The low-pass filter is essential, not optional: the multiplier creates the desired baseband term and also creates new high-frequency images, and the LPF is what discards those images. A clear receiver block diagram is therefore: received signal $\to$ channel-selecting BPF $\to$ multiplier with synchronized local oscillator $\cos(\omega_0 t)$ $\to$ LPF $\to$ gain or decision stage.

Starting from $f(t)=g(t)\cos(\omega_0 t)$, multiply again by $\cos(\omega_0 t)$ to get $f(t)\cos(\omega_0 t)=g(t)\cos^2(\omega_0 t)=\frac12 g(t)+\frac12 g(t)\cos(2\omega_0 t)$. In the frequency domain this becomes $\frac12 G(\omega)+\frac14 G(\omega-2\omega_0)+\frac14 G(\omega+2\omega_0)$. So after demodulation but before low-pass filtering, the baseband copy has magnitude factor $1/2$, while the residual translated copies at the doubled-carrier region have magnitude factor $1/4$ each.

This scaling has a clean intuition. The first multiplication split the original message spectrum into an upper and a lower sideband, each with factor $1/2$. The second multiplication splits each sideband again. The two inner quarter-copies land back at baseband and add to $1/2$, while the two outer quarter-copies land around $\pm 2\omega_0$. The LPF keeps the inner pieces and discards the outer ones. So if no gain compensation is added, the recovered baseband is still scaled by $1/2$.

This is often described informally as losing power in modulation and demodulation, but the more precise statement is that the normalized multiplication and the filtering redistribute signal power among spectral images, and the receiver intentionally throws some of those images away. In practice, systems compensate by using a gain-$2$ product detector, a stronger local oscillator or active mixer with conversion gain, a post-LPF amplifier, or automatic-gain control. The information is not destroyed by the scaling; it is just not automatically restored to unit amplitude by the normalized mixer model.

Exact baseband recovery is easiest to state spectrally. If $G(\omega)$ is concentrated in $|\omega|<\omega_m$, then the doubled-carrier images occupy bands near $\pm 2\omega_0$. Ideal low-pass recovery is possible when those bands do not overlap the baseband, which is ensured by $\omega_0>\omega_m$ together with a low-pass cutoff satisfying $\omega_m<\omega_c<2\omega_0-\omega_m$. The word coherent or synchronous means the receiver's local oscillator must match the transmitter carrier closely enough in frequency and phase; otherwise the recovered signal is attenuated or distorted. This product-detector-plus-LPF structure is not the only demodulation architecture. Other common options include envelope detection for ordinary AM with a transmitted carrier, I/Q or quadrature demodulation, superheterodyne receivers with intermediate frequency stages, phase-locked-loop or Costas-loop carrier recovery, and noncoherent detectors for some ASK or FSK systems.

A compact worked example makes the LPF choice more concrete. Suppose the baseband message is $g(t)=\cos(200t)$ and the carrier is $\cos(1000t)$. After AM-SC transmission the spectrum lives around $\pm 1000$ with sidebands at $1000\pm 200$. After coherent remultiplication, the signal becomes $g(t)\cos^2(1000t)=\frac12\cos(200t)+\frac12\cos(200t)\cos(2000t)$. Using the product identity again, the second term splits into frequencies at $2000\pm 200$, so before low-pass filtering the receiver contains the desired baseband term at $\pm 200$ and unwanted images at $\pm 1800$ and $\pm 2200$. Therefore an LPF that passes $200$ but rejects $1800$ is enough; any cutoff satisfying $200<\omega_c<1800$ works ideally. The lesson is not the exact number itself, but the geometry: the LPF must sit between the message bandwidth and the nearest remodulated image.

A standard lecture-style spectrum-tracing example fits directly into this section. Let point A be the input spectrum $F(\omega)$ of $f(t)$, point B the output of the first multiplier by $\cos(\omega_0 t)$, point C the output of an ideal BPF that passes the desired modulated channel without distortion, point D the output of a coherent product detector using the same carrier $\cos(\omega_0 t)$, and point E the output of the final LPF. Then

- point A: $F_A(\omega)=F(\omega)$,
- point B: $F_B(\omega)=\frac12 F(\omega-\omega_0)+\frac12 F(\omega+\omega_0)$,
- point C: $F_C(\omega)=H_{\mathrm{BP}}(\omega)F_B(\omega)$, and if the BPF simply keeps the whole desired DSB-SC channel, then this equals $F_B(\omega)$ on that passed band,
- point D: $F_D(\omega)=\frac12 F_C(\omega-\omega_0)+\frac12 F_C(\omega+\omega_0)$,
- point E: after low-pass filtering, only the baseband copy remains.

In the common normalized case where the BPF passes the desired DSB-SC channel unchanged, one gets $F_D(\omega)=\frac14F(\omega-2\omega_0)+\frac12F(\omega)+\frac14F(\omega+2\omega_0)$, so the LPF output is $F_E(\omega)=\frac12F(\omega)$. Therefore the final relation is $y(t)=\frac12 f(t)$. If the receiver includes gain $2$ in the product detector or after the LPF, then the recovered output becomes exactly $y(t)=f(t)$.

---

Flashcards for this section are as follows:

- How should you draw and interpret the coherent-demodulation receiver block diagram? ::@:: Draw the received signal entering a channel-selecting BPF, then a multiplier fed by a synchronized local oscillator $\cos(\omega_0 t)$, then an LPF, and finally any gain or decision stage. The BPF chooses the channel, the multiplier translates spectra, and the LPF recovers baseband. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- Why must coherent demodulation include a low-pass filter after the multiplier? ::@:: Because remultiplying by the carrier creates both the desired baseband term and new high-frequency images, and the LPF is what removes those images and keeps the message. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- Starting from $f(t)=g(t)\cos(\omega_0 t)$, what expression results after multiplying by the carrier again? ::@:: It becomes $f(t)\cos(\omega_0 t)=g(t)\cos^2(\omega_0 t)=\frac12 g(t)+\frac12 g(t)\cos(2\omega_0 t)$. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- What frequency-domain picture corresponds to coherent demodulation before the LPF? ::@:: It is $\frac12 G(\omega)+\frac14 G(\omega-2\omega_0)+\frac14 G(\omega+2\omega_0)$, so there is one recovered baseband copy and two residual images around the doubled carrier. <!--SR:!2026-05-16,15,290!2026-05-17,16,290-->
- Why is the recovered baseband still scaled by $1/2$, while the residual images have factor $1/4$ each? ::@:: Because the first multiplication splits the message into two half-size sidebands, and the second multiplication splits each sideband again. The two inner quarter-copies add at baseband to make $1/2$, while the two outer quarter-copies stay near $\pm 2\omega_0$. <!--SR:!2026-05-16,15,290!2026-05-16,15,290-->
- How should you explain the apparent power loss in normalized modulation and demodulation? ::@:: The multiplier redistributes energy among several spectral copies, and the LPF later throws some of those copies away. So without gain compensation the recovered baseband is scaled, but practical systems restore level with mixer conversion gain, a gain-$2$ detector, post-LPF amplification, or AGC. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- What spectral condition allows ideal low-pass recovery after coherent demodulation? ::@:: If the message is concentrated in $|\omega|<\omega_m$, choose the carrier so that $\omega_0>\omega_m$ and choose the LPF cutoff so that $\omega_m<\omega_c<2\omega_0-\omega_m$, ensuring the baseband and doubled-carrier bands do not overlap. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- Why is coherent demodulation also called synchronous detection, and what other receiver styles exist? ::@:: It is called synchronous because the receiver must use a local carrier matched in frequency and phase to the transmitter carrier. Other receiver styles include envelope detection, I/Q demodulation, superheterodyne receivers, PLL or Costas-loop carrier recovery, and noncoherent detectors for some digital schemes. <!--SR:!2026-05-17,16,290!2026-05-18,17,310-->
- Worked example: If $g(t)=\cos(200t)$ is transmitted by AM-SC with carrier $\cos(1000t)$, what appears after coherent remultiplication and what LPF cutoff range allows ideal baseband recovery? ::@:: Step 1: the transmitted signal is $g(t)\cos(1000t)$. <br/> Step 2: coherent remultiplication gives $g(t)\cos^2(1000t)=\frac12\cos(200t)+\frac12\cos(200t)\cos(2000t)$. <br/> Step 3: expand the second term to get unwanted images at frequencies $2000\pm 200$, i.e. at $1800$ and $2200\text{ rad/s}$. <br/> Step 4: the desired baseband sits at $\pm 200\text{ rad/s}$. <br/> Step 5: therefore any ideal LPF cutoff satisfying $200<\omega_c<1800$ passes the message while rejecting the nearest remodulated image. <!--SR:!2026-05-17,16,290!2026-05-18,17,310-->
- Worked example: In the standard chain A=input $F(\omega)$, B=after multiplying by $\cos(\omega_0 t)$, C=after an ideal BPF that passes the desired DSB-SC channel unchanged, D=after coherent remultiplication by $\cos(\omega_0 t)$, and E=after the final LPF, what spectra appear at A, B, C, D, and E, and what is the relation between $y(t)$ and $f(t)$? ::@:: Point A: $F_A(\omega)=F(\omega)$. <br/> Point B: $F_B(\omega)=\frac12F(\omega-\omega_0)+\frac12F(\omega+\omega_0)$. <br/> Point C: the ideal BPF keeps that desired modulated channel unchanged, so $F_C(\omega)=F_B(\omega)$ on the passed band. <br/> Point D: remultiplication gives $F_D(\omega)=\frac12F_C(\omega-\omega_0)+\frac12F_C(\omega+\omega_0)=\frac14F(\omega-2\omega_0)+\frac12F(\omega)+\frac14F(\omega+2\omega_0)$. <br/> Point E: the LPF keeps only the baseband term, so $F_E(\omega)=\frac12F(\omega)$. <br/> Therefore the normalized recovered signal is $y(t)=\frac12f(t)$, and a gain-$2$ compensation stage would restore $y(t)=f(t)$. <!--SR:!2026-05-12,11,290!2026-05-16,15,290-->

## multiplexing, demultiplexing, and channel filters

Frequency-division multiplexing (FDM) assigns different carrier bands to different messages. If the $k$-th baseband message is $g_k(t)$ and it is modulated by $\cos(\omega_k t)$, then $s_k(t)=g_k(t)\cos(\omega_k t)$ and $S_k(\omega)=\frac12 G_k(\omega-\omega_k)+\frac12 G_k(\omega+\omega_k)$. The transmitted composite waveform is $s(t)=\sum_k s_k(t)$, so the composite spectrum is the sum of several translated message pairs. If the carriers and message bandwidths are chosen so the translated bands do not overlap, the channels coexist in one medium without spectral collision. In a practical FDM transmitter, each message path usually has its own modulator, local oscillator, and often a BPF before all channels are summed.

Demultiplexing is the reverse operation. To recover channel $k$, the receiver first uses a BPF centered on that channel's passband, then multiplies the isolated channel by the matching local carrier, and then applies an LPF to return to baseband. So the demultiplexing block diagram is explicitly: composite received signal $\to$ channel-selecting BPF $\to$ product detector $\to$ LPF $\to$ recovered message. The extra BPF is the structural difference between ordinary one-channel demodulation and channel-by-channel demultiplexing.

This is where the ideal band-pass filter becomes important. If the desired channel is centered at $\omega_0$ with half-bandwidth $\omega_c$, then $H_{\mathrm{BP}}(\omega)=\operatorname{rect}((\omega-\omega_0)/(2\omega_c))+\operatorname{rect}((\omega+\omega_0)/(2\omega_c))$, or equivalently $H_{\mathrm{BP}}(\omega)=1$ for $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$ and $0$ elsewhere. Its impulse response is $h_{\mathrm{BP}}(t)=2\cos(\omega_0 t)\,\frac{\omega_c}{\pi}\operatorname{sinc}_{\pi}(\omega_c t/\pi)=\frac{\sin((\omega_0+\omega_c)t)-\sin((\omega_0-\omega_c)t)}{\pi t}$. The interpretation is simple: it is an ideal low-pass window shifted away from the origin. The sinc envelope determines channel width, while the cosine determines channel location.

Time-division multiplexing (TDM) shares one channel differently. Instead of placing users in different frequency bands, it places them in different time slots of one repeating frame. A practical TDM transmitter can be drawn as several message inputs feeding a clocked commutator or electronic switch, which interleaves the signals into one stream. A practical TDM receiver uses synchronized clock recovery, a decommutator or electronic switch, and then sample-and-hold or reconstruction filtering on each branch. FDM separates by BPFs and carrier frequency, whereas TDM separates by timing and synchronization.

The spectral behavior also differs. In FDM, each channel spectrum is translated to a separate passband and then added, so the overall spectrum looks like several nonoverlapping channel-shaped islands. In TDM, rapid slotting multiplies each message by a pulse train or gating waveform, which broadens the spectrum and creates frame-related repetition effects. That is why TDM design worries more about timing accuracy and reconstruction filtering, while FDM design worries more about carrier placement, guard bands, and BPF selectivity.

A compact FDM design example helps turn the rule into a picture. Suppose three baseband messages are each bandlimited to $|\omega|<B$, and we modulate them onto carriers $\omega_1<\omega_2<\omega_3$. After AM-SC, channel $k$ occupies the positive-frequency band $[\omega_k-B,\,\omega_k+B]$ together with its mirror at negative frequency. To prevent channel collision, the practical carrier-spacing condition is therefore not merely "different carriers", but "enough separation that adjacent translated bands plus guard margins do not overlap". Demultiplexing then becomes a repeated three-step workflow: select one channel with a BPF centered at $\omega_k$, remultiply by $\cos(\omega_k t)$, and low-pass filter back to baseband.

---

Flashcards for this section are as follows:

- What is frequency-division multiplexing, and how does it change the spectra? ::@:: FDM modulates different messages onto different carriers, so channel $k$ becomes $S_k(\omega)=\frac12 G_k(\omega-\omega_k)+\frac12 G_k(\omega+\omega_k)$. The transmitted spectrum is the sum of several separated passband copies, one channel cluster per carrier. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- How should you draw the main FDM transmitter structure? ::@:: Draw one message path per channel, with each path going through its own modulator and local oscillator, then usually a BPF, and finally an adder that combines all channel outputs into one transmitted waveform. <!--SR:!2026-05-16,15,290!2026-05-17,16,290-->
- How should you draw the main FDM demultiplexing structure? ::@:: Draw the received composite signal entering a BPF that isolates one channel, then a product detector with the matching local carrier, then an LPF that returns the selected channel to baseband. <!--SR:!2026-05-16,15,290!2026-05-17,16,290-->
- Why is the BPF an essential extra block in demultiplexing? ::@:: Because before demodulation the receiver must first isolate one channel band from the multiplexed composite spectrum; otherwise the product detector would mix several channels at once. <!--SR:!2026-05-15,14,290!2026-05-16,15,290-->
- What is the ideal band-pass filter formula for a channel centered at $\omega_0$ with half-bandwidth $\omega_c$? ::@:: It is $H_{\mathrm{BP}}(\omega)=\operatorname{rect}((\omega-\omega_0)/(2\omega_c))+\operatorname{rect}((\omega+\omega_0)/(2\omega_c))$, or equivalently $1$ for $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$ and $0$ elsewhere. <!--SR:!2026-05-15,14,290!2026-05-15,14,290-->
- What impulse response and intuition correspond to that ideal band-pass filter? ::@:: The impulse response is $h_{\mathrm{BP}}(t)=2\cos(\omega_0 t)\,\frac{\omega_c}{\pi}\operatorname{sinc}_{\pi}(\omega_c t/\pi)=\frac{\sin((\omega_0+\omega_c)t)-\sin((\omega_0-\omega_c)t)}{\pi t}$. <br/> It is a shifted low-pass kernel: the sinc envelope sets channel width and the cosine sets center frequency. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- What is time-division multiplexing, and how is it implemented? ::@:: TDM lets several users share one channel by occupying different time slots of a repeating frame. A transmitter interleaves the inputs with a clocked switch or commutator, and a receiver uses synchronized switching plus sample-and-hold or reconstruction filters to separate them again. <!--SR:!2026-05-18,17,310!2026-05-15,14,290-->
- How should you compare the spectral behavior of FDM and TDM? ::@:: FDM moves each channel to its own passband, so the spectrum becomes several separated channel islands. TDM gates signals in time, so it broadens spectra and creates frame-related repetition effects instead of distinct carrier-centered passbands. <!--SR:!2026-05-18,17,310!2026-05-15,14,290-->
- What quick comparison helps distinguish FDM and TDM? ::@:: FDM partitions the channel by frequency bands and uses BPFs for separation, whereas TDM partitions the channel by time slots and relies on clock synchronization and reconstruction. <!--SR:!2026-05-15,14,290!2026-05-18,17,310-->
- Worked example: If three baseband signals are each bandlimited to $|\omega|<B$ and are modulated onto carriers $\omega_1<\omega_2<\omega_3$ by AM-SC, what bands do they occupy and how is one channel recovered? ::@:: Step 1: channel $k$ is shifted to the positive-frequency band $[\omega_k-B,\,\omega_k+B]$ together with the mirrored negative-frequency band. <br/> Step 2: adjacent carriers must therefore be separated enough that these translated bands, plus any guard margin, do not overlap. <br/> Step 3: to recover channel $k$, use a BPF centered at $\omega_k$, then remultiply by $\cos(\omega_k t)$, and finally low-pass filter the result back to baseband. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->

## other multiplexing methods

FDM and TDM are only two members of a larger multiplexing family. Code-division multiplexing separates users by distinct codes rather than by pure bands or pure time slots. Orthogonal frequency-division multiplexing can be viewed as a carefully orthogonal multicarrier version of FDM. Wavelength-division multiplexing plays the same role in optical systems by assigning different optical wavelengths. Space-division multiplexing uses physically different propagation paths or spatial modes. In advanced optical systems, even orbital-angular-momentum modes or optical vortices can serve as distinct parallel channels.

The common idea across all of them is the same: choose some resource dimension in which signals can be made distinguishable, then design modulation, filtering, synchronization, and detection so that those channels can later be separated with manageable interference.

Even after choosing a multiplexing scheme, pulse shape and window shape still matter. Modulation determines where a channel is placed, but pulse shaping influences how tightly its energy is confined. Sharper time-domain gating tends to spread spectral sidelobes more broadly, while smoother shaping makes it easier to keep neighboring channels from interfering with one another.

---

Flashcards for this section are as follows:

- What other multiplexing methods should you at least recognize beyond FDM and TDM? ::@:: Code-division multiplexing, orthogonal frequency-division multiplexing, wavelength-division multiplexing, and space-division multiplexing; advanced optical systems may even use orbital-angular-momentum or optical-vortex modes as separate channels. <!--SR:!2026-05-18,17,310!2026-05-17,16,290-->
- What unifying idea links these other multiplexing methods? ::@:: They all choose some resource dimension—code, orthogonal subcarrier, wavelength, spatial mode, or vortex mode—and design the transmitter and receiver so different users become separable along that dimension. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- Why does pulse or window shape still matter after modulation has shifted the spectrum to a carrier? ::@:: Because modulation moves the spectrum, but the waveform shape still determines how concentrated or spread that spectrum is within the new band. <!--SR:!2026-05-18,17,310!2026-05-18,17,310-->
- What broad design lesson links modulation to bandwidth control? ::@:: Spectral translation alone is not enough; pulse shaping determines occupied bandwidth and interference with neighboring channels. <!--SR:!2026-05-18,17,310!2026-05-16,15,290-->
- What is the big engineering lesson of modulation in one sentence? ::@:: Modulation is not just multiplication by a carrier; it is frequency translation plus filtering plus spectral shaping so information fits a crowded channel cleanly. <!--SR:!2026-05-15,14,290!2026-05-16,15,290-->
