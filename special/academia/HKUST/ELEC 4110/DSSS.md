---
aliases:
  - DSSS
  - ELEC 4110 DSSS
  - ELEC 4110 direct sequence spread spectrum
  - ELEC 4110 direct-sequence spread spectrum
  - ELEC4110 DSSS
  - ELEC4110 direct sequence spread spectrum
  - ELEC4110 direct-sequence spread spectrum
  - direct sequence spread spectrum
  - direct-sequence spread spectrum
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/DSSS
  - language/in/English
---

# direct-sequence spread spectrum

- see: [general/direct-sequence spread spectrum](../../../../general/direct-sequence%20spread%20spectrum.md)

{@{__Direct-sequence spread spectrum__ (__DSSS__)}@} transmits a data stream by {@{modulating it in the usual way—typically BPSK}@}—then {@{multiplying the baseband signal by a high‑frequency spreading sequence}@}. The result is {@{a wideband waveform}@} whose {@{spectrum is spread over many more chips than the original data bandwidth}@}.

## spread spectrum

{@{_Spread‑spectrum_ techniques}@} were introduced to {@{mitigate _frequency‑selective fading_}@}, notably {@{_inter‑symbol interference_ (ISI) and the irreducible error floor}@} from {@{multiple propagation paths}@}. While {@{diversity}@} handles {@{flat‑fading}@}, {@{spread spectrum}@} widens {@{the transmitted bandwidth as a complementary approach}@}.

{@{A system is classified as _spread‑spectrum_}@} when its {@{transmitted bandwidth $B_s$ greatly exceeds the message bandwidth $B_m$}@}, and this relationship remains {@{independent of the data rate}@}: {@{$$B_s \gg B_m, \qquad B_s\;\text{is independent of}\; B_m \,.$$}@} By transmitting {@{over a wide spectrum}@}, {@{narrowband interference}@} is {@{suppressed}@} and {@{ISI in multipath channels}@} is {@{reduced}@}, allowing {@{reliable communication over frequency‑selective channels}@}.

## spreading

{@{The binary data $b(t)$ and the PN (pseudo-noise) spreading sequence $c(t)$}@} are both {@{bipolar, taking values $\pm 1$}@}: {@{$$b(t)= \pm 1 \quad\text{(binary message)} , \qquad c(t)= \pm 1 \quad\text{(PN spreading code)}$$}@} {@{Each data bit}@} occupies {@{a _bit period_ $t_m$}@}; {@{each PN chip}@} occupies {@{a much shorter _chip period_ $t_c$}@}. A single bit {@{spans many chips}@}—for example, {@{spread over 1024 chips}@}.

{@{The baseband BPSK output}@} is {@{$$s_{BPSK}(t) = \sqrt{2P_t}\;b(t)\;\cos(\omega_c t + \phi)$$}@} where {@{$P_t$}@} is {@{transmitted power (_not_ bit energy)}@} and {@{$\omega_c$}@} {@{the carrier frequency}@}. After spreading, {@{the transmitted signal}@} becomes {@{$$s(t)=\sqrt{2P_t}\;c(t)\,b(t)\;\cos(\omega_c t+\phi) \,.$$}@} {@{Multiplying by $c(t)$}@} {@{spreads the spectrum}@} because {@{$c(t)$ changes many times within a single bit interval (chip period $t_c$)}@}. The carrier becomes {@{a band whose width is determined by the chip rate, not a narrow spike}@}.

### spreading in time domain

{@{Each bit}@} is {@{replaced by a sequence of chips}@}, so the receiver sees {@{a long "spread" waveform}@} even though {@{only one bit was sent}@}. {@{The resulting _spread signal_}@} is {@{a train of chips}@} whose {@{polarity follows the data bits}@}.

### spreading in frequency domain

In {@{the frequency domain}@} the {@{spreading operation}@} can be seen as a {@{convolution between the data spectrum and the PN‑code spectrum}@}.

{@{The spectrum of the _spread signal_}@} {@{occupies a band $W_s$}@} much {@{wider than the original narrowband carrier}@}. {@{A non‑spread BPSK signal}@} has {@{_passband_ bandwidth $W_{\text{non-spread} } = 1/t_b$}@}, while {@{the DSSS signal}@} has {@{_passband_ bandwidth $W_{\text{spread} } \approx 1/t_c$}@}.

## despreading

{@{The receiver}@} performs the {@{inverse of the transmitter's spreading operation}@}. First it {@{multiplies the incoming signal $s(t)$ by the _known_ PN sequence $c(t)$}@}. Because {@{the sequence is bipolar, $$c(t)\,c(t)=1$$}@}, {@{the spread spectrum collapses to its underlying data waveform}@}: {@{$$s_{demod}(t)=c(t)\,s(t)\;\longrightarrow\; \text{data carrier}$$}@}

After {@{despreading}@}, the signal is {@{demodulated normally (e.g., coherent BPSK detection)}@}. {@{The data modulation}@} {@{need not be BPSK; any scheme}@} works. Often {@{the same modulation format}@} is used {@{for both spreading and data to simplify hardware}@}. {@{The order of spreading and data modulation}@} can be {@{swapped}@}: both yield {@{the same transmitted waveform}@} because {@{multiplication is commutative}@}.

To {@{recover the data reliably}@} a receiver must {@{know exactly which PN sequence was used for spreading}@}; and {@{align its local replica of $c(t)$}@} with the {@{received signal at the correct chip‑rate timing}@}. When these conditions hold, {@{despreading recovers the original data stream}@} with the {@{same spectral properties as an ordinary narrowband link}@}.

## advantages

{@{The advantages}@} of {@{DS spreading}@} are: (annotation: 3 items: {@{interference suppression, low probability of interception, no additional channel-noise penalty}@})

- _Interference suppression_ ::@:: – spreading reduces narrowband interference because the energy is spread over a larger spectrum; this is the _primary_ benefit.
- _Low probability of interception (LPI)_ ::@:: – an unintended receiver that does not know the PN sequence sees only noise, making detection difficult.
- _No additional channel‑noise penalty_ ::@:: – the process preserves the signal‑to‑noise ratio of the underlying channel.

If {@{no external interference exists}@}, the {@{bandwidth cost outweighs the benefit}@}. {@{Spreading}@} helps in two cases: {@{frequency‑selective fading}@} causing {@{inter‑symbol interference}@}, and {@{multi‑user interference in CDMA systems}@} where {@{many users share the same time/frequency resources}@}.

## DS-CDMA

In {@{_DS-CDMA_ systems}@} each user is {@{assigned a unique PN code}@}. The {@{transmitted data}@} are {@{multiplied by that code before transmission}@}; at the receiver, {@{correlation with the same code}@} recovers {@{the data while simultaneously rejecting signals from other users}@}. This {@{code division multiple access}@} allows {@{many users to share the same frequency band}@}.

When {@{several users transmit simultaneously over the same time slot and bandwidth}@}, {@{their spectra completely overlap}@} and {@{conventional filtering}@} in {@{either the time or frequency domain}@} {@{cannot separate them}@}; {@{all user signals}@} look {@{indistinguishable at the front‑end}@}. Treating {@{unwanted signals as additive noise}@} yields a {@{very low SINR (e.g., <0&nbsp;dB for BPSK)}@} and {@{prohibitively high error rates}@}.

{@{The main advantage of DS-CDMA}@} is that {@{each user's data}@} is {@{spread by its unique PN sequence}@}. At {@{the intended receiver}@}, {@{multiplying the received waveform by the correct code}@} {@{"despreads" the desired signal}@}: it {@{collapses back into a narrowband BPSK spectrum}@}, while {@{other users' signals remain widely spread}@}. {@{A band‑pass filter}@} can then {@{pass only the despread desired component}@} and {@{reject most residual interference}@}. This filtering {@{reduces the effective interference power of _each interfering user_}@} to {@{roughly its original value divided by the _spreading factor_}@} (e.g., a 1/64 {@{discount factor per interfering user}@} for {@{a spreading factor of 64}@}), improving {@{the SINR enough for reliable demodulation}@}.

## pseudo-noise code

A {@{spread‑spectrum system}@} relies on the {@{statistical properties of its pseudorandom noise (PN) codes}@}.

The {@{_correlation_ function}@} measures {@{how similar two sequences are as one is shifted relative to the other}@}: {@{$$R_{xy}(\tau)=\sum_n x[n]\,y^*[n-\tau]$$}@} When {@{the two sequences are identical}@}, this is {@{the _auto‑correlation_ of $c[n]$}@}: {@{$$R_{cc}(\tau)=\sum_n c[n]\,c^*[n-\tau].$$}@}

For {@{DS/CDMA}@}, {@{a _good PN code_}@} has {@{auto‑correlation}@} with {@{a sharp peak at zero shift}@} and {@{very small values for all non‑zero offsets}@}. This gives {@{near‑perfect orthogonality between different shifts}@}: {@{correlation with the correct code}@} yields {@{a strong response}@} while {@{cross‑correlation with other codes or shifted versions}@} stays {@{negligible}@}, minimizing {@{interference}@} and improving {@{security}@}.

## intersymbol interference

DSSS {@{expands a data signal}@} by {@{multiplying it with a pseudo‑random noise (PN) code}@}. Since {@{the spreading bandwidth is large}@}, DS‑SS signals propagate over {@{_frequency‑selective fading channels_ with many resolvable echoes}@}. {@{The superposition of delayed replicas}@} produces {@{_inter‑symbol interference_ (ISI)}@}, which {@{drives the error floor high}@} without a countermeasure.

{@{The standard way a DS‑SS system suppresses ISI}@} is to {@{employ a _RAKE receiver_}@}. {@{A RAKE receiver}@} contains {@{one or more _fingers_}@}. Each finger {@{despreads the received waveform}@} with {@{a PN sequence that has been time‑aligned to one of the multipath delays}@}. Because {@{the autocorrelation of a good PN code is sharply peaked}@}, {@{cross‑correlation terms from non‑matched paths}@} are {@{small}@}; thus {@{each finger}@} sees only {@{a weak ISI contribution from the other paths}@}.

### rake receiver

{@{The received signal}@} is {@{a combination of $L = \lfloor W / B_c \rfloor$ resolved paths}@} ({@{$W$}@} is {@{spread passband bandwidth}@}, {@{$B_c$}@} {@{the coherence bandwidth}@}): {@{$$y(t)=\sum_{i=1}^{L}\alpha_i\,s(t-\tau_i)c(t-\tau_i)+n(t),$$}@} where {@{$s(\cdot)$}@} is {@{the modulated data}@}, {@{$c(\cdot)$}@} {@{the PN code}@}, {@{$\alpha_i$}@} {@{the complex channel coefficient for path $i$}@}, and {@{$\tau_i$}@} its {@{delay}@}.

{@{A finger that targets path $j$}@} computes {@{$$r_j(t)=\text{Despread}\!\bigl(y(t),\,c(t-\tau_j)\bigr) =\alpha_j\,s(t-\tau_j)\;\!+\! \sum_{i\neq j}\alpha_i\,s(t-\tau_i)\,\underbrace{\langle c(t-\tau_i), c(t-\tau_j)\rangle}_{\text{small} }\; +\;\langle c(t-\tau_i), n(t)\rangle.$$}@} The {@{term $\langle c(t-\tau_i), c(t-\tau_j)\rangle$}@} is {@{the _normalized cross‑correlation_}@} ("normalized" means {@{divided by the number of chips $N$}@}) of {@{two PN sequences that are misaligned in time}@}.

For {@{an i.i.d. PN sequence}@} {@{the _normalized_ cross-correlation of two misaligned ($i \ne j$) PN sequences}@} tends to {@{zero variance as the code length $N$ grows}@}: {@{$$\operatorname E[\langle c(t-\tau_i), c(t-\tau_j)\rangle] = 0\,, \qquad \operatorname{Var}(\langle c(t-\tau_i), c(t-\tau_j)\rangle) = \frac 1 N \,.$$}@} Thus {@{each finger}@} extracts {@{a clean observation of the desired data}@} with only {@{residual ISI from other paths and additive noise}@}, which has {@{a power of roughly $1/N$ of the original power}@}. {@{The set of observations $\{r_1,r_2,\dots ,r_L\}$}@} are {@{effectively independent}@}, which yields {@{_diversity gain_}@} in addition to {@{the _processing gain_ from DSSS}@}.

## effective SINR

{@{The spread spectrum}@} introduces {@{a _processing gain_}@} {@{$\text{PG} = W_{\text{spread} }/W_{\text{non-spread} }$}@}. {@{The _signal‑to‑interference‑plus‑noise ratio_ (SINR) per bit}@} at {@{each finger}@} is {@{multiplied by this factor}@}: {@{$$\text{SINR}_{\text{effective} } = \frac {\lvert a_i \rvert^2 E_b} {N_0 + \frac {(\text{\# users}) \cdot \lvert a_i \rvert^2 E_b} {\text{PG} } } \approx \frac {\text{PG} } {\text{\# users} } \,,$$}@} where {@{$E_b$}@} is {@{energy per bit}@}, {@{$N_0$}@} {@{the noise spectral density}@}, and {@{$(\text{\# users})$}@} {@{the number of _other_ users interfering with the current user}@}. {@{The final approximation}@} holds for {@{high SNR}@} (so {@{$N_0$}@} is {@{small relative to $E_b$}@}), where {@{the error rate is interference‑limited}@} and {@{the _BER floor_ from ISI}@} is {@{the limiting factor}@}.

Because each {@{finger provides an independent measurement of the same bit}@}, combining {@{(e.g., maximal ratio combining or equal‑gain combining)}@} steepens {@{the BER curve}@}: {@{the diversity order}@} equals {@{the number of fingers $L$}@}.

## performance

Compare three scenarios: {@{_BPSK_ without spreading}@}, {@{_BPSK + DSSS_ with a single RAKE finger}@}, and {@{_BPSK + DSSS_ with multiple ($L>1$) RAKE fingers}@}. One finger {@{dramatically reduces the BER floor}@} via {@{the processing gain}@}; adding more fingers {@{steepens the curve further via diversity gain}@}. {@{Full diversity is exploited}@} when {@{the number of fingers equals the number of resolvable paths $L$}@}. (annotation: __this course__: Tested in {@{the final examination}@}.) {@{Processing gain and finger diversity}@} jointly reduce {@{ISI in frequency‑selective fading channels}@}.

## implementation

In {@{a DSSS receiver}@}, {@{each incoming chip}@} is multiplied by {@{the locally stored spreading sequence}@} and {@{accumulated over one spread period (e.g., 64 chips, 1024 chips)}@}. {@{The multiplication}@} reduces to {@{sign inversion for the $\pm1$ chips}@}—no {@{dedicated multiplier needed}@}; {@{a full‑adder}@} suffices. After {@{accumulation}@} the result is {@{right‑shifted six times to divide by 64}@}, exploiting {@{$64=2^6$}@}. {@{Two or more parallel despreaders}@} process {@{distinct multipath components (the "fingers" of a rake receiver)}@}, each producing {@{an observation $W_i$}@} fed into {@{a diversity combiner operating at symbol rate}@}.

{@{Practical receivers (e.g., 3G handsets)}@} often have {@{only four despreaders}@} because {@{each operates at a high clock rate}@}, yet still capture {@{_almost_ full diversity by selecting the strongest paths}@}. This is why {@{spread‑spectrum systems (3G and earlier)}@} remain {@{power‑efficient despite supporting many multipaths}@}.

### time and power considerations

{@{The despreader core}@} runs at {@{the chip rate}@}, typically {@{many times (e.g. 64, 1024) faster than the symbol clock}@}. Since {@{dynamic power scales with frequency}@}, {@{the high‑speed despreader dominates the power budget}@}. {@{The combinatorial logic between clocks (adders, sign‐inverters)}@} must {@{finish within one chip period}@}; {@{oversized logic}@} forces a {@{lower clock or higher energy consumption}@}.

{@{The core arithmetic for spreading and despreading}@} is {@{deliberately simple}@}: {@{full adders for accumulation}@} and {@{bit‑shift units for division by powers of two}@}. {@{Multiplication by $\pm1$}@} uses {@{sign inversion}@}, eliminating the need for {@{a multiplier}@}. This keeps {@{the data path short and power‑efficient}@} while meeting {@{chip‑clock timing constraints}@}.

### rake receiver architecture

{@{A rake receiver}@} has {@{multiple "fingers"}@}, each {@{correlating with one delayed copy of the incoming waveform}@}. Each finger outputs {@{a weighted observation $W_i$}@}; these are {@{combined (selection, equal‑gain or maximal‑ratio)}@} for {@{diversity and interference suppression}@}. {@{The number of fingers}@} sets {@{the complexity cost}@}; {@{adding more paths}@} does not {@{significantly increase hardware cost}@} because {@{the spreading sequence and pilot channel give the receiver structure to exploit}@}.

{@{Accurate chip‑level timing}@} is {@{essential for despreading}@}. {@{A pilot channel}@}, transmitted with {@{the same timing as data}@}, provides {@{a known sequence the receiver correlates against}@}. {@{An exhaustive search over possible despreading timings $D_1, D_2, \ldots$}@} runs {@{frame by frame}@}, feeding {@{the best estimate to the despreaders}@}. {@{The auto‑correlation of the spreading sequence}@} must be {@{sharply peaked}@}; otherwise {@{timing resolution degrades}@}.

### implementation with a single RF chain

Even with {@{only one despreader}@}, diversity is possible by combining {@{observations across time or frequency (e.g., selection combining)}@}. {@{A single RF/ADC chain}@} can {@{realise a two‑branch diversity order}@} by moving {@{the selection switch to the front end}@}. This mirrors {@{Wi‑Fi's antenna‑diversity technique}@}, where {@{pilot bits of each frame}@} are {@{split into two in time to estimate the SNR}@}. It shows that {@{low‑complexity receivers}@} can exploit {@{multipath without additional hardware chains}@}.
