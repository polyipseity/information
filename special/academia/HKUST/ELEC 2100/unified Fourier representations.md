---
aliases:
  - ELEC 2100 unified Fourier representations
  - ELEC2100 unified Fourier representations
  - HKUST ELEC 2100 unified Fourier representations
  - unified Fourier representations
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/unified_Fourier_representations
  - language/in/English
---

# unified Fourier representations

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

This note derives all four named course Fourier representations from the continuous-time Fourier transform in a uniform way, counting DTFS separately from DFT. The starting pair is $F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}\,dt$ and $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$. Every discretization follows the same pattern: multiply by a Dirac comb in the domain being discretized, use the convolution theorem to identify the corresponding operation in the other domain, then rescale variables to integer labels and fix normalization to match the course convention.

---

Flashcards for this section are as follows:

- what continuous-time Fourier pair does this note start from? ::@:: $F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}\,dt$ and $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$.
- what derivation pattern is used when discretizing an axis? ::@:: Multiply by a Dirac comb in that domain, use the convolution theorem to find the effect in the other domain, then rescale to integer labels and fix normalization.

## the comb identities used throughout

The time-domain Dirac comb of spacing $T$ is $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$. In the present Fourier-transform convention it satisfies $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta\!\left(\omega-k\frac{2\pi}{T}\right)$. If the spacing is instead named in frequency by $\omega_0$, then the frequency comb is $\operatorname{III}_{\omega_0}(\omega)=\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$ and its inverse-transform partner is $\operatorname{III}_{\omega_0}(\omega)\longleftrightarrow \frac{1}{\omega_0}\operatorname{III}_{2\pi/\omega_0}(t)=\frac{1}{\omega_0}\sum_{r=-\infty}^{\infty}\delta\!\left(t-r\frac{2\pi}{\omega_0}\right)$. So a comb in one domain always corresponds to a periodic comb in the other domain, with reciprocal spacing up to the factor $2\pi$.

Two transform rules are needed throughout. If $g(t)=f(t)h(t)$, then $G(\omega)=\frac{1}{2\pi}(F*H)(\omega)$; if $g(t)=(f*h)(t)$, then $G(\omega)=F(\omega)H(\omega)$. The first turns time sampling into spectral replication; the second turns frequency sampling into periodic time summation.

---

Flashcards for this section are as follows:

- what is the time-domain Dirac comb of spacing $T$? ::@:: It is $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$.
- what Fourier-transform pair does the time comb satisfy in this convention? ::@:: It satisfies $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)$.
- what is the inverse-transform partner of the frequency comb $\operatorname{III}_{\omega_0}(\omega)$? ::@:: It is $\operatorname{III}_{\omega_0}(\omega)\longleftrightarrow \frac{1}{\omega_0}\operatorname{III}_{2\pi/\omega_0}(t)$.
- which two transform rules are used most often? ::@:: Time multiplication → frequency convolution with $1/(2\pi)$; time convolution → frequency multiplication.

## the parent corner: Fourier transform

The continuous-time Fourier transform is the parent corner: both time and frequency are continuous. Its analysis formula is $F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}\,dt$, and its synthesis formula is $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$. The transform $F(\omega)$ is a coefficient density: the signal is reconstructed by integrating infinitesimal spectral contributions $F(\omega)d\omega/(2\pi)$.

The convolution theorem is standard: if $y(t)=(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau$, then $Y(\omega)=F(\omega)G(\omega)$. The time-multiplication theorem follows by reversing the logic: if $y(t)=f(t)g(t)$, then $Y(\omega)=\frac{1}{2\pi}(F*G)(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\nu)G(\omega-\nu)\,d\nu$. In short: convolution in time becomes multiplication in frequency, and multiplication in time becomes convolution in frequency with the $1/(2\pi)$ factor.

For energy signals, Parseval's formula is $E=\int_{-\infty}^{\infty}|f(t)|^2\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^2\,d\omega$. Power signals are not absolutely integrable and are better handled by Fourier series or power spectral density methods, so the energy Parseval formula is the natural companion here.

Summary: Fourier transform is continuous-continuous, convolution becomes multiplication, multiplication becomes convolution with $1/(2\pi)$, and Parseval compares total energy with spectral energy density.

---

Flashcards for this section are as follows:

- what is the convolution theorem for the Fourier transform? ::@:: If $y(t)=(f*g)(t)$, then $Y(\omega)=F(\omega)G(\omega)$.
- what is the time-multiplication theorem? ::@:: If $y(t)=f(t)g(t)$, then $Y(\omega)=\frac{1}{2\pi}(F*G)(\omega)$.
- what is the Parseval formula for energy signals? ::@:: $\int_{-\infty}^{\infty}|f(t)|^2\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^2\,d\omega$.
- derivation / Fourier transform convolution theorem ::@:: Step 1: write $Y(\omega)=\int_{-\infty}^{\infty}\left(\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau\right)e^{-j\omega t}\,dt$. <br/> Step 2: interchange integrals: $Y(\omega)=\int_{-\infty}^{\infty}f(\tau)\left(\int_{-\infty}^{\infty}g(t-\tau)e^{-j\omega t}\,dt\right)d\tau$. <br/> Step 3: let $u=t-\tau$: the inner integral becomes $e^{-j\omega\tau}G(\omega)$. <br/> Step 4: factor out $G(\omega)$: $Y(\omega)=G(\omega)\int_{-\infty}^{\infty}f(\tau)e^{-j\omega\tau}d\tau=F(\omega)G(\omega)$. <br/> Step 5: convolution in time → multiplication in frequency.
- derivation / Fourier transform time-multiplication theorem ::@:: Step 1: write $Y(\omega)=\int_{-\infty}^{\infty}f(t)g(t)e^{-j\omega t}dt$. <br/> Step 2: substitute $f(t)=\frac{1}{2\pi}\int F(\nu)e^{j\nu t}d\nu$. <br/> Step 3: $Y(\omega)=\frac{1}{2\pi}\int F(\nu)\left(\int g(t)e^{-j(\omega-\nu)t}dt\right)d\nu$. <br/> Step 4: recognize $G(\omega-\nu)$, so $Y(\omega)=\frac{1}{2\pi}(F*G)(\omega)$. <br/> Step 5: multiplication in time → convolution in frequency with $1/(2\pi)$.
- derivation / Fourier transform Parseval ::@:: Step 1: $E=\int f(t)\overline{f(t)}dt$. <br/> Step 2: substitute $\overline{f(t)}=\frac{1}{2\pi}\int \overline{F(\omega)}e^{-j\omega t}d\omega$. <br/> Step 3: interchange integrals and recognize $F(\omega)$: $E=\frac{1}{2\pi}\int |F(\omega)|^2d\omega$.

## frequency discretization of Fourier transform gives Fourier series

To derive Fourier series, discretize the frequency axis. Multiply the continuous spectrum by the frequency comb of spacing $\omega_0$: $F_{\mathrm{raw,FS}}(\omega)=F(\omega)\operatorname{III}_{\omega_0}(\omega)=\sum_{k=-\infty}^{\infty}F(k\omega_0)\delta(\omega-k\omega_0)$.

Using the convolution theorem in reverse: since $\operatorname{III}_{\omega_0}(\omega)\longleftrightarrow \frac{1}{\omega_0}\operatorname{III}_{T_0}(t)$ with $T_0=2\pi/\omega_0$, frequency multiplication corresponds to time convolution, so $f_{\mathrm{raw,FS}}(t)=\frac{1}{\omega_0}\sum_{r=-\infty}^{\infty}f(t-rT_0)$. Frequency discretization produces periodic summation in time.

The inverse transform also gives this directly. Since $F_{\mathrm{raw,FS}}(\omega)$ is a sum of impulses, the inverse integral collapses to $f_{\mathrm{raw,FS}}(t)=\frac{1}{2\pi}\sum_{k=-\infty}^{\infty}F(k\omega_0)e^{jk\omega_0 t}$. Defining $F_k:=\frac{1}{2\pi}F(k\omega_0)$ gives the synthesis formula $f_{\mathrm{FS}}(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$.

The analysis formula follows from orthogonality over one period: $\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f_{\mathrm{FS}}(t)e^{-jk\omega_0 t}\,dt=F_k$. So the course Fourier-series pair is $F_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f_{\mathrm{FS}}(t)e^{-jk\omega_0 t}\,dt$ and $f_{\mathrm{FS}}(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$, with $F_{\mathrm{FS}}(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$.

Periodic convolution: if $h(t)=\int_{t_0}^{t_0+T_0}f(\tau)g(t-\tau)\,d\tau$, then $H_k=T_0F_kG_k$. Time multiplication: if $h(t)=f(t)g(t)$, then $H_k=\sum_m F_mG_{k-m}$ (discrete convolution of coefficients).

For power signals, the natural object is average power. The power Parseval formula is $P=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|f(t)|^2\,dt=\sum_{k=-\infty}^{\infty}|F_k|^2$. Nonzero periodic signals have infinite total energy, so power rather than energy is the natural norm.

Summary: frequency comb → periodic time summation, analysis by one-period orthogonality, periodic convolution → coefficient multiplication with $T_0$, pointwise multiplication → discrete coefficient convolution, Parseval measures average power.

---

Flashcards for this section are as follows:

- what is the convolution theorem for Fourier series? ::@:: Periodic convolution $h(t)=\int_{t_0}^{t_0+T_0}f(\tau)g(t-\tau)\,d\tau$ gives $H_k=T_0F_kG_k$.
- what is the time-multiplication theorem? ::@:: If $h(t)=f(t)g(t)$, then $H_k=\sum_m F_mG_{k-m}$.
- what is the Parseval formula? ::@:: $\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|f(t)|^2\,dt=\sum_k |F_k|^2$.
- derivation / Fourier series from frequency sampling ::@:: Step 1: multiply $F(\omega)$ by $\operatorname{III}_{\omega_0}(\omega)$ to get $F_{\mathrm{raw,FS}}(\omega)=\sum_k F(k\omega_0)\delta(\omega-k\omega_0)$. <br/> Step 2: frequency comb → time periodic summation: $f_{\mathrm{raw,FS}}(t)=\frac{1}{\omega_0}\sum_r f(t-rT_0)$. <br/> Step 3: invert: $f_{\mathrm{raw,FS}}(t)=\frac{1}{2\pi}\sum_k F(k\omega_0)e^{jk\omega_0 t}$. <br/> Step 4: define $F_k=F(k\omega_0)/(2\pi)$ → synthesis $f_{\mathrm{FS}}(t)=\sum_k F_k e^{jk\omega_0 t}$. <br/> Step 5: integrate one period against $e^{-jk\omega_0 t}$ → analysis $F_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f_{\mathrm{FS}}(t)e^{-jk\omega_0 t}dt$.
- derivation / Fourier series convolution ::@:: Step 1: write $f=\sum_m F_m e^{jm\omega_0 t}$, $g=\sum_n G_n e^{jn\omega_0 t}$. <br/> Step 2: substitute into $h(t)=\int_{t_0}^{t_0+T_0}f(\tau)g(t-\tau)d\tau$ and use orthogonality. <br/> Step 3: only $m=n$ terms survive with weight $T_0$, so $H_k=T_0F_kG_k$.
- derivation / Fourier series multiplication ::@:: Step 1: $h=fg=\sum_m\sum_n F_mG_n e^{j(m+n)\omega_0 t}$. <br/> Step 2: regroup by $k=m+n$ → $H_k=\sum_m F_mG_{k-m}$.
- derivation / Fourier series Parseval ::@:: Step 1: $|f|^2=\sum_k\sum_m F_k\overline{F_m}e^{j(k-m)\omega_0 t}$. <br/> Step 2: average over one period, orthogonality kills $k\neq m$. <br/> Step 3: $\frac{1}{T_0}\int|f|^2dt=\sum_k |F_k|^2$.

## time discretization of Fourier transform gives DTFT

To derive DTFT, discretize the time axis. Multiply the signal by the time comb of spacing $T$: $x_s(t)=f(t)\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}f(nT)\delta(t-nT)$.

Since $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{\omega_s}(\omega)$ with $\omega_s=2\pi/T$, time multiplication gives spectral convolution: $X_s(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}F(\omega-k\omega_s)$. Time discretization produces spectral replication.

Direct computation from the impulse train gives $X_s(\omega)=\sum_{n=-\infty}^{\infty}f(nT)e^{-j\omega nT}$. Relabeling $x[n]:=f(nT)$ and $\Omega:=\omega T$ yields the course DTFT: $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$. The inverse formula uses $2\pi$-periodicity: $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$.

Linear convolution: if $y[n]=\sum_m x[m]h[n-m]$, then $Y(e^{j\Omega})=X(e^{j\Omega})H(e^{j\Omega})$. Sequence multiplication: if $y[n]=x[n]h[n]$, then $Y(e^{j\Omega})=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\theta})H(e^{j(\Omega-\theta)})\,d\theta$ (periodic convolution with the $1/(2\pi)$ factor).

For finite-energy sequences, Parseval's formula is $E=\sum_{n=-\infty}^{\infty}|x[n]|^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}|X(e^{j\Omega})|^2\,d\Omega$. Power sequences (like periodic sequences) are better handled by DTFS, so the energy formula is the natural companion here.

Summary: DTFT is discrete-time, continuous periodic frequency, linear convolution → multiplication, pointwise multiplication → periodic spectral convolution, Parseval compares discrete energy with one-period spectral energy.

---

Flashcards for this section are as follows:

- what are the DTFT analysis and synthesis formulas? ::@:: $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$ and $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$.
- what is the convolution theorem? ::@:: If $y[n]=\sum_m x[m]h[n-m]$, then $Y(e^{j\Omega})=X(e^{j\Omega})H(e^{j\Omega})$.
- what is the sequence-multiplication theorem? ::@:: If $y[n]=x[n]h[n]$, then $Y(e^{j\Omega})=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\theta})H(e^{j(\Omega-\theta)})\,d\theta$.
- what is the Parseval formula? ::@:: $\sum_n |x[n]|^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}|X(e^{j\Omega})|^2\,d\Omega$.
- derivation / DTFT from time sampling ::@:: Step 1: multiply by time comb → $x_s(t)=\sum_n f(nT)\delta(t-nT)$. <br/> Step 2: time multiplication → spectral convolution: $X_s(\omega)=\frac{1}{T}\sum_k F(\omega-k\omega_s)$. <br/> Step 3: relabel $x[n]=f(nT)$, $\Omega=\omega T$ → $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$. <br/> Step 4: inverse via orthogonality on $[-\pi,\pi]$ → $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}d\Omega$.
- derivation / DTFT convolution ::@:: Step 1: $Y(e^{j\Omega})=\sum_n(\sum_m x[m]h[n-m])e^{-j\Omega n}$. <br/> Step 2: interchange sums, let $r=n-m$: inner sum becomes $e^{-j\Omega m}H(e^{j\Omega})$. <br/> Step 3: $Y(e^{j\Omega})=X(e^{j\Omega})H(e^{j\Omega})$.
- derivation / DTFT multiplication ::@:: Step 1: substitute inverse DTFT of $x[n]$ into $Y(e^{j\Omega})=\sum_n x[n]h[n]e^{-j\Omega n}$. <br/> Step 2: interchange sum and integral → $Y(e^{j\Omega})=\frac{1}{2\pi}\int X(e^{j\theta})H(e^{j(\Omega-\theta)})d\theta$.
- derivation / DTFT Parseval ::@:: Step 1: $E=\sum_n x[n]\overline{x[n]}$. <br/> Step 2: substitute $\overline{x[n]}=\frac{1}{2\pi}\int \overline{X(e^{j\Omega})}e^{-j\Omega n}d\Omega$. <br/> Step 3: interchange sum and integral → $E=\frac{1}{2\pi}\int |X(e^{j\Omega})|^2d\Omega$.

## the Fourier-series branch reaches DFT by discretizing time again

Starting from the Fourier-series branch (discrete frequency, continuous time), sample one period uniformly with spacing $T_s=T_0/N$, so $\omega_s=2\pi/T_s=N\omega_0$. Multiplying by the time comb gives $x_s(t)=f_{\mathrm{FS}}(t)\operatorname{III}_{T_s}(t)=\sum_{n=-\infty}^{\infty}f_{\mathrm{FS}}(nT_s)\delta(t-nT_s)$.

Time multiplication gives spectral convolution: $X_s(\omega)=\frac{1}{T_s}\sum_{q=-\infty}^{\infty}F_{\mathrm{FS}}(\omega-qN\omega_0)$. Harmonics whose indices differ by multiples of $N$ collapse into the same sampled class.

Define $\widetilde X[m]:=\sum_{q=-\infty}^{\infty}F_{m+qN}$ for $m=0,1,\dots,N-1$. Then $x[n]=\sum_{m=0}^{N-1}\widetilde X[m]e^{j2\pi mn/N}$. Finite-grid orthogonality gives $\widetilde X[m]=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j2\pi mn/N}$. Defining $X[m]:=N\widetilde X[m]$ yields the course DFT pair $X[m]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi mn/N}$ and $x[n]=\frac{1}{N}\sum_{m=0}^{N-1}X[m]e^{j2\pi mn/N}$.

DFT convolution: if $y[n]=(x\circledast h)[n]$ (circular), then $Y[k]=X[k]H[k]$. Time multiplication: if $y[n]=x[n]h[n]$, then $Y[k]=\frac{1}{N}(X\circledast H)[k]$ (circular in bin index). Energy Parseval: $E=\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|X[k]|^2$. Average power of the periodic extension: $P=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N^2}\sum_{k=0}^{N-1}|X[k]|^2$.

Summary: time sampling of Fourier-series branch aliases harmonics modulo $N$, circular convolution → binwise multiplication, pointwise multiplication → circular bin convolution, Parseval works for both finite-record energy and periodic-extension power.

---

Flashcards for this section are as follows:

- what are the DFT analysis and synthesis formulas? ::@:: $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ and $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$.
- what is the convolution theorem? ::@:: Circular convolution $y[n]=(x\circledast h)[n]$ gives $Y[k]=X[k]H[k]$.
- what is the time-multiplication theorem? ::@:: If $y[n]=x[n]h[n]$, then $Y[k]=\frac{1}{N}(X\circledast H)[k]$.
- what is the energy Parseval formula? ::@:: $\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|X[k]|^2$.
- derivation / DFT from Fourier-series branch ::@:: Step 1: sample $f_{\mathrm{FS}}(t)$ at $T_s=T_0/N$ → $x[n]=\sum_r F_r e^{j2\pi rn/N}$. <br/> Step 2: harmonics modulo $N$ alias → $\widetilde X[m]=\sum_q F_{m+qN}$. <br/> Step 3: finite-grid orthogonality → $\widetilde X[m]=\frac{1}{N}\sum_n x[n]e^{-j2\pi mn/N}$. <br/> Step 4: define $X[m]=N\widetilde X[m]$ → course DFT.
- derivation / DFT convolution ::@:: Step 1: substitute inverse DFT into circular convolution. <br/> Step 2: finite-grid orthogonality → only equal bin indices survive. <br/> Step 3: $Y[k]=X[k]H[k]$.
- derivation / DFT multiplication ::@:: Step 1: substitute inverse DFT expansions of $x[n]$ and $h[n]$ into $y[n]=x[n]h[n]$. <br/> Step 2: regroup by bin difference modulo $N$ → $Y[k]=\frac{1}{N}(X\circledast H)[k]$.
- derivation / DFT Parseval ::@:: Step 1: substitute inverse DFT into $\sum|x[n]|^2$. <br/> Step 2: orthogonality kills cross terms → $\sum|x[n]|^2=\frac{1}{N}\sum|X[k]|^2$.

## the DTFT branch reaches the same DFT by discretizing frequency again

The same DFT can also be reached from the DTFT branch by discretizing frequency. Start with the course DTFT $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$. To sample one $2\pi$ period at $N$ equally spaced points, multiply by the weighted comb $C_N(\Omega):=\frac{2\pi}{N}\operatorname{III}_{2\pi/N}(\Omega)=\frac{2\pi}{N}\sum_{k=-\infty}^{\infty}\delta\!\left(\Omega-k\frac{2\pi}{N}\right)$. The weight $2\pi/N$ is exactly what becomes the $1/N$ factor in the inverse finite sum.

The raw sampled spectrum is $X_{\mathrm{raw,DFT}}(\Omega)=\frac{2\pi}{N}\sum_{k=-\infty}^{\infty}X\!\left(e^{j2\pi k/N}\right)\delta\!\left(\Omega-k\frac{2\pi}{N}\right)$. Under the DTFT pair this comb corresponds to $c_N[n]=\sum_{r=-\infty}^{\infty}\delta[n-rN]$, so the sequence-domain effect is periodic summation: $x_{\mathrm{raw,DFT}}[n]=\sum_{r=-\infty}^{\infty}x[n-rN]$. If $x[n]$ is already supported on $0\le n\le N-1$, this just reproduces the stored record.

Inverting gives $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_{\mathrm{raw,DFT}}(\Omega)e^{j\Omega n}\,d\Omega=\frac{1}{N}\sum_{k=0}^{N-1}X\!\left(e^{j2\pi k/N}\right)e^{j2\pi kn/N}$. Defining $X[k]:=X\!\left(e^{j2\pi k/N}\right)$ yields the same DFT pair. The DFT bins can be read as either normalized harmonic classes (Fourier-series branch) or sampled DTFT values (DTFT branch).

This also shows why the DFT theorems are branch-independent. Once the same DFT pair is obtained, the same convolution, multiplication, and Parseval theorems follow regardless of which derivation route was taken. The two routes differ only in the interpretation of what the bins came from.

---

Flashcards for this section are as follows:

- what raw spectrum results from frequency sampling the DTFT? ::@:: $X_{\mathrm{raw,DFT}}(\Omega)=\frac{2\pi}{N}\sum_k X(e^{j2\pi k/N})\delta(\Omega-2\pi k/N)$.
- what sequence-domain operation corresponds to multiplying by the comb? ::@:: Convolution with $c_N[n]=\sum_r\delta[n-rN]$, giving periodic summation $x_{\mathrm{raw,DFT}}[n]=\sum_r x[n-rN]$.
- why are the DFT theorems branch-independent? ::@:: Both branches produce the same DFT pair, so the same theorems follow once the bins are defined.
- derivation / DFT from DTFT branch ::@:: Step 1: multiply DTFT by $C_N(\Omega)=\frac{2\pi}{N}\operatorname{III}_{2\pi/N}(\Omega)$ → sample one $2\pi$ period. <br/> Step 2: raw spectrum $X_{\mathrm{raw,DFT}}(\Omega)=\frac{2\pi}{N}\sum_k X(e^{j2\pi k/N})\delta(\Omega-2\pi k/N)$. <br/> Step 3: sequence-domain effect is periodic summation modulo $N$. <br/> Step 4: invert → $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X(e^{j2\pi k/N})e^{j2\pi kn/N}$. <br/> Step 5: define $X[k]=X(e^{j2\pi k/N})$ → course DFT.
- derivation / why the two DFT routes agree ::@:: Step 1: from Fourier-series branch, $x[n]=\sum_r F_r e^{j2\pi rn/N}$. <br/> Step 2: compute $X[m]=\sum_n x[n]e^{-j2\pi mn/N}$. <br/> Step 3: interchange sums, inner sum is $N$ when $r\equiv m\pmod N$. <br/> Step 4: $X[m]=N\sum_q F_{m+qN}=N\widetilde X[m]$. <br/> Step 5: on DTFT branch, same number is $X(e^{j2\pi m/N})$. <br/> Step 6: $X(e^{j2\pi m/N})=X[m]=N\sum_q F_{m+qN}$.

## why the two DFT derivations agree

The two DFT derivations must agree because they are just two ways of discretizing the parent Fourier-transform picture twice. The agreement is explicit. From the Fourier-series branch, $x[n]=\sum_r F_r e^{j2\pi rn/N}$. Computing its DFT: $X[m]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi mn/N}=\sum_r F_r\sum_{n=0}^{N-1}e^{j2\pi (r-m)n/N}$. The inner sum is $N$ when $r\equiv m\pmod N$ and $0$ otherwise, so $X[m]=N\sum_q F_{m+qN}$. On the Fourier-series branch, $\widetilde X[m]=\sum_q F_{m+qN}$, so $X[m]=N\widetilde X[m]$. On the DTFT branch, the same number is $X(e^{j2\pi m/N})$. Therefore $X(e^{j2\pi m/N})=X[m]=N\sum_q F_{m+qN}$. One DFT bin is simultaneously a sampled DTFT value and the grouped sum of all continuous-time Fourier-series harmonics whose indices are congruent modulo $N$.

DFT remembers only what survives after one more discretization, and that surviving object can be read as either a sampled periodic spectrum or aliased harmonic classes.

---

Flashcards for this section are as follows:

- why must the Fourier-series branch and the DTFT branch produce the same DFT? ::@:: Because both branches are obtained by discretizing the parent Fourier-transform picture twice, so they must meet at the same fully discrete representation.
- how does direct DFT computation show agreement with the Fourier-series branch? ::@:: Substitute $x[n]=\sum_r F_r e^{j2\pi rn/N}$ into $X[m]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi mn/N}$, interchange the sums, use finite-grid orthogonality, and obtain $X[m]=N\sum_q F_{m+qN}$.
- what is the unified identity for one DFT bin? ::@:: $X(e^{j2\pi m/N})=X[m]=N\sum_q F_{m+qN}$: it is simultaneously a sampled DTFT value and the grouped sum of Fourier-series harmonics congruent modulo $N$.

## one short periodic signal through the four mathematical corners

Take $f(t)=1+\cos(\omega_0 t)$ with period $T_0=2\pi/\omega_0$. Fourier series: $f(t)=1+\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$, so $F_0=1$, $F_1=1/2$, $F_{-1}=1/2$. Fourier transform: $F(\omega)=2\pi\delta(\omega)+\pi\delta(\omega-\omega_0)+\pi\delta(\omega+\omega_0)$. Note $F(\omega)$ line weights are $2\pi F_k$.

Sample one period at $N=4$: $T_s=T_0/4$, $x[n]=f(nT_s)=1+\cos(2\pi n/4)$. The four samples: $x[0]=2$, $x[1]=1$, $x[2]=0$, $x[3]=1$, so $[2,1,0,1]$. DTFT: $X(e^{j\Omega})=2+e^{-j\Omega}+e^{-j3\Omega}$. Sampling at $\Omega_k=2\pi k/4$: $X[0]=4$, $X[1]=2$, $X[2]=0$, $X[3]=2$, so DFT is $[4,2,0,2]$.

Fourier-series branch gives the same answer. Group harmonics modulo $4$: $\widetilde X[0]=1$, $\widetilde X[1]=1/2$, $\widetilde X[2]=0$, $\widetilde X[3]=1/2$. Converting by $X[m]=4\widetilde X[m]$ gives again $[4,2,0,2]$. This one signal shows the whole square: line spectrum in angular frequency, harmonic coefficients in Fourier series, continuous periodic DTFT after time sampling, and finite DFT after one more discretization.

---

Flashcards for this section are as follows:

- for $f(t)=1+\cos(\omega_0 t)$, what are the nonzero Fourier-series coefficients and Fourier-transform line weights? ::@:: Step 1: Euler's formula: $f(t)=1+\frac12 e^{j\omega_0 t}+\frac12 e^{-j\omega_0 t}$. <br/> Step 2: $F_0=1$, $F_1=1/2$, $F_{-1}=1/2$. <br/> Step 3: $F(\omega)=2\pi\delta(\omega)+\pi\delta(\omega-\omega_0)+\pi\delta(\omega+\omega_0)$.
- for $N=4$, what is the sampled sequence and its DFT? ::@:: Step 1: $x[n]=1+\cos(2\pi n/4)$ → $[2,1,0,1]$. <br/> Step 2: $X[k]=\sum_{n=0}^{3}x[n]e^{-j2\pi kn/4}$ → $[4,2,0,2]$.
- how does the Fourier-series branch give the same DFT? ::@:: Step 1: $F_0=1$, $F_1=1/2$, $F_{-1}=1/2$. <br/> Step 2: group modulo $4$ → $\widetilde X=[1,1/2,0,1/2]$. <br/> Step 3: $X[m]=4\widetilde X[m]$ → $[4,2,0,2]$.

## the course keeps DTFS as a fifth named convention

Mathematically, DFT and DTFS live in the same discrete-time/discrete-frequency corner. The course uses a different normalization and signal model for each. For DFT, a stored block $x[n]$ for $n=0,\dots,N-1$ is a finite record: $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ and $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$. For DTFS, the sequence is already $N$-periodic: $\widetilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ and $x[n]=\sum_{k=0}^{N-1}\widetilde X[k]e^{j2\pi kn/N}$. So $X[k]=N\widetilde X[k]$. DTFS is natural for explicitly periodic sequences; DFT is natural for finite records in computation.

---

Flashcards for this section are as follows:

- why does the course count DTFS as a fifth convention? ::@:: DTFS is for explicitly periodic sequences (harmonic amplitudes), DFT is for finite records (computation). Both share the same discrete/discrete corner but use different normalization: $X[k]=N\widetilde X[k]$.

## one aperiodic parent with a triangular spectrum through all five conventions

Let $\Lambda(u)=\max(1-|u|,0)$ and start from the aperiodic parent spectrum $F(\omega)=\Lambda(\omega/\omega_c)$, a triangle of height $1$ on $|\omega|\le \omega_c$. Since a triangle is the convolution of two equal rectangles, the inverse transform is $f(t)=\frac{\omega_c}{2\pi}\operatorname{Sa}^2(\omega_c t/2)$.

If we discretize frequency with spacing $\omega_0$, the Fourier-series branch samples the triangle on the harmonic lattice: $F_k=\frac{1}{2\pi}\Lambda(k\omega_0/\omega_c)$. The line spectrum is $F_{\mathrm{FS}}(\omega)=\sum_k \Lambda(k\omega_0/\omega_c)\delta(\omega-k\omega_0)$.

If we sample time with period $T$, then $x[n]=f(nT)=\frac{\omega_c}{2\pi}\operatorname{Sa}^2(\omega_c Tn/2)$. The DTFT is $X(e^{j\Omega})=\frac{1}{T}\sum_m \Lambda\!\left(\frac{\Omega-2\pi m}{\omega_c T}\right)$. Two key facts: time sampling scales the DTFT height by $1/T$, and the physical cutoff $|\omega|=\omega_c$ maps to the digital cutoff $|\Omega|=\omega_c T$. Decreasing $T$ makes replicas taller but narrower in normalized frequency; increasing $T$ spreads them wider and causes aliasing once $\omega_c T>\pi$.

Sampling the DTFT on $\Omega_k=2\pi k/N$ gives $X[k]=X(e^{j2\pi k/N})=\frac{1}{T}\sum_m \Lambda\!\left(\frac{2\pi(k-mN)/N}{\omega_c T}\right)$. When alias-free in the principal interval, $X[k]=\frac{1}{T}\Lambda\!\left(\frac{2\pi k_c}{N\omega_c T}\right)$ using centered bin index $k_c$. DTFS coefficients are $\widetilde X[k]=\frac{1}{N}X[k]$. So DFT and DTFS place the same nonzero bins at the same indices; only the $1/N$ normalization and interpretation differ.

In one line, the same triangular parent appears as follows.

- FT: $F(\omega)=\Lambda(\omega/\omega_c)$.
- Fourier-series line spectrum: $2\pi F_k=\Lambda(k\omega_0/\omega_c)$ at $\omega=k\omega_0$.
- DTFT: periodic triangle replicas of height $1/T$.
- DFT: sampled DTFT values $X[k]$ on $\Omega_k=2\pi k/N$.
- DTFS: the same sampled bins scaled to $\widetilde X[k]=X[k]/N$.

---

Flashcards for this section are as follows:

- for the triangular-spectrum parent, what are the FT, Fourier-series, DTFT, DFT, and DTFS descriptions? ::@:: FT: $F(\omega)=\Lambda(\omega/\omega_c)$. Fourier-series: $2\pi F_k=\Lambda(k\omega_0/\omega_c)$. DTFT: periodic triangles of height $1/T$. DFT: $X[k]=X(e^{j2\pi k/N})$. DTFS: $\widetilde X[k]=X[k]/N$.
- how do $T$ and $N$ affect magnitude and aliasing? ::@:: Smaller $T$ makes replicas taller but narrower in normalized frequency. The digital cutoff is $|\Omega|=\omega_c T$, so aliasing starts once $\omega_c T>\pi$. <br/> On $N$ points, the edge sits near $k_c\approx N\omega_c T/(2\pi)$.
- derivation / FT to Fourier-series ::@:: Step 1: $F(\omega)=\Lambda(\omega/\omega_c)$. <br/> Step 2: multiply by $\operatorname{III}_{\omega_0}(\omega)$ → $F_k=\frac{1}{2\pi}\Lambda(k\omega_0/\omega_c)$. <br/> Step 3: line spectrum $F_{\mathrm{FS}}(\omega)=\sum_k \Lambda(k\omega_0/\omega_c)\delta(\omega-k\omega_0)$.
- derivation / FT to DTFT ::@:: Step 1: sample time with period $T$. <br/> Step 2: spectral replication → $X(e^{j\Omega})=\frac{1}{T}\sum_m \Lambda\!\left(\frac{\Omega-2\pi m}{\omega_c T}\right)$.
- derivation / FT to DFT ::@:: Step 1: time-sample → DTFT replica formula. <br/> Step 2: sample DTFT on $N$-point grid → $X[k]=X(e^{j2\pi k/N})$. <br/> Step 3: alias-free case → $X[k]=\frac{1}{T}\Lambda\!\left(\frac{2\pi k_c}{N\omega_c T}\right)$.
- derivation / FT to DTFS ::@:: Step 1: obtain DFT bins $X[k]$. <br/> Step 2: $\widetilde X[k]=\frac{1}{N}X[k]$.

## the five final course-convention formulas

After all derivations, the five course-convention formulas are:

- Fourier transform: $F(\omega)=\int f(t)e^{-j\omega t}\,dt$, $f(t)=\frac{1}{2\pi}\int F(\omega)e^{j\omega t}\,d\omega$.
- Fourier series: $F_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)e^{-jk\omega_0 t}\,dt$, $f(t)=\sum_k F_k e^{jk\omega_0 t}$.
- DTFT: $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$, $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$.
- DFT: $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$, $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$.
- DTFS: $\widetilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$, $x[n]=\sum_{k=0}^{N-1}\widetilde X[k]e^{j2\pi kn/N}$.

There are four mathematical corners (continuous/continuous, continuous/discrete, discrete/continuous, discrete/discrete), but the course names five conventions because DFT and DTFS share the last corner with different normalization. The exponential basis is the same everywhere; what changes is which axis has been discretized and where the normalization factor sits.

---

Flashcards for this section are as follows:

- what are the five course-convention formulas? ::@:: FT: $F(\omega)=\int f(t)e^{-j\omega t}dt$, $f(t)=\frac{1}{2\pi}\int F(\omega)e^{j\omega t}d\omega$. Fourier series: $F_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)e^{-jk\omega_0 t}dt$, $f(t)=\sum_k F_k e^{jk\omega_0 t}$. DTFT: $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$, $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}d\Omega$. DFT: $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$, $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$. DTFS: $\widetilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$, $x[n]=\sum_{k=0}^{N-1}\widetilde X[k]e^{j2\pi kn/N}$.
- what are the four mathematical corners and why five conventions? ::@:: FT is continuous/continuous, Fourier series is continuous/discrete, DTFT is discrete/continuous, DFT/DTFS share discrete/discrete. Five conventions because DFT (finite records, sum-first) and DTFS (periodic sequences, average-first) use different normalization in the same corner.
