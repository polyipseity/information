---
aliases:
  - DFS
  - DFT
  - DTFS
  - ELEC 2100 DFT
  - ELEC 2100 discrete Fourier transform
  - ELEC 2100 discrete-time Fourier series
  - ELEC2100 DFT
  - HKUST ELEC 2100 DFT
  - HKUST ELEC 2100 DTFS
  - discrete Fourier series
  - discrete Fourier transform
  - discrete-time Fourier series
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/discrete_Fourier_transform
  - language/in/English
---

# discrete Fourier transform

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

The discrete Fourier transform (DFT) converts $N$ samples into $N$ frequency-bin coefficients at $\Omega_k=2\pi k/N$. Two viewpoints are valid: the DFT samples the DTFT of a length-$N$ record on a uniform grid, and it treats the record as one period of a periodic extension, which is why circular shift and circular convolution appear automatically.

This note also covers the discrete-time Fourier series (DTFS/DFS). Both use a finite harmonic list indexed by $k=0,1,\dots,N-1$. The general DTFT uses continuous $\Omega=\omega T$ and represents periodic sequences by a line spectrum.

For the continuous digital-frequency viewpoint of a general sequence, see [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md). For continuous-time, use [Fourier series](Fourier%20series.md) (periodic) or [Fourier transform](Fourier%20transform.md) (aperiodic).

---

Flashcards for this section are as follows:

- What does the DFT do? ::@:: It converts $N$ samples into $N$ frequency-bin coefficients at $\Omega_k=2\pi k/N$.
- Why is the DFT not just the DTFT at fewer points? ::@:: Because the DFT treats a finite record as one period of a periodic extension, so circular shift and circular convolution are built into the model.
- Where does this note sit among the Fourier notes? ::@:: DFT: finite-grid computational transform for discrete data. DTFT: continuous digital-frequency variable for general sequences. Fourier series/transform: continuous-time periodic/aperiodic counterparts.
- What core problem does the DFT note solve in ELEC 2100? ::@:: It converts a finite record of samples into a finite set of frequency-bin coefficients so discrete data can be analyzed, computed, and reconstructed on an $N$-point grid.
- How should you compare the DTFT note and the DFT note quickly? ::@:: The DTFT note covers discrete-time spectral analysis for general and periodic sequences using the continuous digital-frequency variable $\Omega=\omega T$, while the DFT note covers the finite-data computational transform obtained by sampling that digital frequency on an $N$-point grid.

## definition and inverse transform

For a length-$N$ sequence $x[n]$ indexed by $n=0,1,\dots,N-1$, the DFT is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ for $k=0,1,\dots,N-1$, and the inverse DFT is $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$ for $n=0,1,\dots,N-1$. If we define the twiddle factor $W_N=e^{-j2\pi/N}$, the forward transform can also be written as $X[k]=\sum_{n=0}^{N-1}x[n]W_N^{kn}$.

The DFT maps an $N$-dimensional vector to another using complex exponential basis functions that are orthogonal over the finite grid, so the inverse transform recovers the original record exactly.

For real sequences, $X[N-k]=X^*[k]$. Nonzero-frequency bins come in conjugate pairs: $k$ and $N-k$ have equal magnitude and opposite phase.

Self-partner bins solve $N-k\equiv k\pmod N$, equivalently $2k\equiv0\pmod N$. So $k=0$ is always self-partner, and when $N$ is even, $k=N/2$ is also self-partner. These bins are purely real: $k=0$ is DC, $k=N/2$ is the Nyquist bin.

Two short examples help. For $x[n]=\{1,1,1,1\}$, $X[0]=4$ and $X[1]=X[2]=X[3]=0$ (the phasors cancel). For $x[n]=\{1,0,0,0\}$, every bin equals $1$. A constant record concentrates at DC; an impulse spreads uniformly.

---

Flashcards for this section are as follows:

- What is the forward DFT formula for an $N$-point sequence? ::@:: It is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ for $k=0,1,\dots,N-1$.
- What is the inverse DFT formula? ::@:: It is $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$ for $n=0,1,\dots,N-1$.
- What does the symbol $W_N$ mean in DFT notation? ::@:: It means $W_N=e^{-j2\pi/N}$, so the forward transform can be written compactly as $X[k]=\sum_{n=0}^{N-1}x[n]W_N^{kn}$.
- What do the indices $n$ and $k$ represent in the DFT? ::@:: $n$ labels time-domain sample positions inside the finite record, while $k$ labels discrete frequency bins.
- Why can the inverse DFT recover the record exactly from the $N$ coefficients? ::@:: Because the complex exponential basis vectors are orthogonal over the length-$N$ grid, so the transform coefficients give a complete coordinate description of the finite record.
- What conjugate-symmetry rule holds for real sequences? ::@:: $X[N-k]=X^*[k]$, so bins come in conjugate pairs with equal magnitude and opposite phase. Self-partner bins ($k=0$, and $k=N/2$ when $N$ even) are purely real.
- Why are $k=0$ and $k=N/2$ special in DFT conjugate symmetry? ::@:: They are their own negative-frequency partners modulo $N$. The DC bin has no distinct partner, and the Nyquist bin has none when $N$ is even, so each must equal its own conjugate and hence be real.
- Worked case: Why does $x[n]=\{1,1,1,1\}$ produce only a DC DFT? ::@:: $X[0]=4$. For $k=1,2,3$, the phasors complete full cycles and cancel, so $X[1]=X[2]=X[3]=0$.
- Worked case: Why does $x[n]=\{1,0,0,0\}$ give $X[k]=1$ for every bin? ::@:: Only the $n=0$ term is nonzero, and $e^0=1$, so every bin gets the same contribution.

## matrix viewpoint of the DFT

The DFT can also be written as a matrix multiplication. Let $\mathbf{x}=[x[0],x[1],\dots,x[N-1]]^T$ and $\mathbf{X}=[X[0],X[1],\dots,X[N-1]]^T$. Define the DFT matrix $F_N$ by $[F_N]_{k,n}=W_N^{kn}=e^{-j2\pi kn/N}$. Then $\mathbf{X}=F_N\mathbf{x}$.

The inverse matrix comes from orthogonality: $F_N^H F_N=N I$, so $F_N^{-1}=\frac{1}{N}F_N^H$. Each row of $F_N$ is a sampled complex exponential, so each DFT coefficient is a projection of the data onto one basis row.

For $N=4$, $W_4=-j$, so $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$. If $\mathbf{h}=[1,2,-1,3]^T$, then $\mathbf{H}=F_4\mathbf{h}=\begin{bmatrix}5\\2+j\\-5\\2-j\end{bmatrix}$. The matrix form is the same DFT in linear-algebra language.

---

Flashcards for this section are as follows:

- How do you write the DFT as a matrix multiplication? ::@:: Let $\mathbf{x}=[x[0],x[1],\dots,x[N-1]]^T$ and define $[F_N]_{k,n}=W_N^{kn}=e^{-j2\pi kn/N}$. Then the DFT is $\mathbf{X}=F_N\mathbf{x}$.
- Why does the inverse DFT matrix equal $\frac{1}{N}F_N^H$? ::@:: Because the sampled complex exponentials are orthogonal, so $F_N^H F_N=N I$. Therefore $F_N^{-1}=\frac{1}{N}F_N^H$, which is the matrix form of the inverse DFT.
- What is the best interpretation of the DFT matrix rows? ::@:: Each row is one sampled complex exponential basis vector, so each DFT coefficient is a correlation or projection of the data onto one discrete harmonic.
- What is the $4$-point DFT matrix? ::@:: $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$, since $W_4=-j$.
- Matrix-form worked example: If $\mathbf{h}=[1,2,-1,3]^T$, what is its $4$-point DFT? ::@:: Using $\mathbf{H}=F_4\mathbf{h}$ with $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$ gives $\mathbf{H}=\begin{bmatrix}5\\2+j\\-5\\2-j\end{bmatrix}$.

## relation to DTFT and periodic extension

Truncating the sequence to $N$ samples and evaluating the DTFT at $\Omega_k=2\pi k/N$ gives the DFT directly.

From the periodic-extension viewpoint, if the length-$N$ block is repeated periodically, $X[k]=N\tilde X[k]$ where $\tilde X[k]$ are the DTFS coefficients. Circular phenomena arise because a finite record is one period of a periodic sequence.

DTFS and DFT both use finite $k=0,1,\dots,N-1$ and work modulo $N$ without Dirac impulses. The general DTFT uses continuous $\Omega=\omega T$ and represents periodic sequences by a line spectrum.

---

Flashcards for this section are as follows:

- How is the DFT obtained from the DTFT? ::@:: Restrict the sequence to length $N$ and sample the DTFT at $\Omega_k=2\pi k/N$.
- What frequencies are sampled in an $N$-point DFT? ::@:: $\Omega_k=2\pi k/N$ for $k=0,1,\dots,N-1$.
- Why does the DFT inherit circular behavior? ::@:: Because the finite data block is interpreted as one period of a periodic extension, so shifts and convolutions wrap modulo $N$.
- How are DFT and DTFS coefficients related? ::@:: $X[k]=N\tilde X[k]$ with the normalization used here.

## relation between DTFS and DFT

For a period-$N$ sequence $\tilde x[n+N]=\tilde x[n]$, the DTFS/DFS pair used in this course is $\tilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$ and $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. For an $N$-point record, the DFT pair is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ and $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$.

The course-material distinction is interpretive: DTFS/DFS is for explicitly periodic sequences, DFT for finite records with implicit periodic extension.

Algebraically, the two are the same harmonic decomposition: $X[k]=N\tilde X[k]$. The basis functions, modulo-$N$ indexing, and orthogonality are identical. The only difference is where $1/N$ is placed.

DTFS/DFS: average-first ($1/N$ in analysis, synthesize directly). DFT: sum-first (raw forward sum, $1/N$ in the inverse).

---

Flashcards for this section are as follows:

- What is the course-material distinction between DTFS/DFS and DFT? ::@:: DTFS/DFS: explicitly periodic sequences. DFT: finite records with implicit periodic extension.
- How are DTFS/DFS and DFT related algebraically? ::@:: $X[k]=N\tilde X[k]$. Same basis functions, same modulo-$N$ indexing.
- What is the memory rule for $1/N$ placement? ::@:: DTFS: average-first ($1/N$ in analysis). DFT: sum-first ($1/N$ in the inverse).
- Why is DTFS/DFS mainly grouped with the DFT note rather than the DTFT note? ::@:: Because DTFS/DFS and DFT both use one finite harmonic coefficient cycle for period-$N$ data, whereas the general DTFT uses the continuous digital-frequency variable $\Omega=\omega T$ and represents periodic sequences by a line spectrum.

## periodic sequences and discrete-time Fourier series

For a sequence periodic with period $N$, the fundamental digital angular frequency is $\Omega_0=2\pi/N$. The DTFS synthesis formula is $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$.

The point of deriving the DTFT of a periodic sequence is to connect two descriptions: the finite DTFS coefficient list $\tilde X[k]$ and the line spectrum in continuous $\Omega$.

The notation: $\tilde x[n]$ is the period-$N$ sequence, $\tilde X[k]$ are its DTFS coefficients, $\Omega_0=2\pi/N$, and $X_{\mathrm{DTFT}}(e^{j\Omega})$ is the DTFT.

Now isolate one harmonic. Suppose $\tilde x_{k_0}[n]=\tilde X[k_0]e^{jk_0\Omega_0 n}$. Its DTFT is $X_{k_0}(e^{j\Omega})=\tilde X[k_0]\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k_0\Omega_0)n}$.

The factor $2\pi$ is not arbitrary; it is exactly the weight needed by the inverse DTFT. If one spectral line is $2\pi A\,\delta(\Omega-\Omega_c)$, then $\frac{1}{2\pi}\int_{-\pi}^{\pi}2\pi A\,\delta(\Omega-\Omega_c)e^{j\Omega n}\,d\Omega=Ae^{j\Omega_c n}$. So a line of area $2\pi A$ reconstructs a harmonic of amplitude $A$. That is why one harmonic in the DTFS synthesis formula becomes a $2\pi$-weighted Dirac line family in the DTFT.

---

Flashcards for this section are as follows:

- What is the fundamental digital angular frequency of a period-$N$ sequence? ::@:: It is $\Omega_0=2\pi/N$. <br/> Since digital angular frequency is defined by $\Omega=\omega T$, this means $\Omega_0$ is $1/N$ cycles per sample, and distinct digital frequencies are usually interpreted on the principal interval $[-\pi,\pi]$.
- What is the DTFS synthesis formula for a period-$N$ sequence? ::@:: It is $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{jk\Omega_0 n}=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. <br/> Here $\Omega_0=2\pi/N$ comes from $\Omega=\omega T$, so it is the fundamental digital angular frequency in radians per sample, equivalently $1/N$ cycles per sample.
- Why does a period-$N$ sequence need only $N$ distinct DTFS coefficients? ::@:: Because both the periodic sequence and the discrete-frequency description repeat modulo $N$, so one full coefficient cycle already contains all distinct information. <br/> In digital-frequency language, the harmonics are spaced by $\Omega_0=2\pi/N$, with distinct frequencies interpreted modulo $2\pi$ and usually read on $[-\pi,\pi]$.
- How should you compare DTFT and DTFS conceptually? ::@:: DTFT uses the continuous digital-frequency variable $\Omega=\omega T$, interpreted as normalized frequency or $\Omega/(2\pi)$ cycles per sample and usually read on $[-\pi,\pi]$, whereas DTFS uses a finite harmonic coefficient cycle for periodic sequences.
- Why is DTFS usually cleaner than DTFT for a truly periodic sequence? ::@:: Because the periodic sequence has energy only at discrete harmonics, so a finite harmonic coefficient list is a more direct description than a DTFT line spectrum written with impulses in the continuous digital-frequency variable $\Omega=\omega T$.
- Why is it useful to derive the DTFT of a periodic sequence from the DTFS synthesis formula? ::@:: Because DTFS and DTFT describe the same periodic sequence in different languages. DTFS stores a finite coefficient list $\tilde X[k]$, while the DTFT shows how those same harmonics appear as impulses in the continuous digital-frequency variable $\Omega$. The derivation explains exactly how the finite harmonic list turns into a line spectrum.
- In the derivation from DTFS to the periodic-sequence DTFT, what do the symbols mean? ::@:: $\tilde x[n]$ is the period-$N$ sequence, $\tilde X[k]$ are its DTFS coefficients, $\Omega_0=2\pi/N$ is the fundamental digital angular frequency, and $X_{\mathrm{DTFT}}(e^{j\Omega})$ is the DTFT of that periodic sequence as a function of the continuous variable $\Omega$. So $k$ is a discrete harmonic index, but $\Omega$ is still continuous.
- How does one harmonic in the DTFS synthesis formula appear inside the DTFT? ::@:: If $\tilde x_{k_0}[n]=\tilde X[k_0]e^{jk_0\Omega_0 n}$, then $X_{k_0}(e^{j\Omega})=\tilde X[k_0]\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k_0\Omega_0)n}$. <br/> That infinite exponential sum is interpreted distributionally as $2\pi\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$, so $X_{k_0}(e^{j\Omega})=2\pi\tilde X[k_0]\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$. <br/> So one DTFS harmonic becomes one periodic family of DTFT spectral lines.
- Why does $\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k\Omega_0)n}$ turn into Dirac deltas with weight $2\pi$? ::@:: Let $\alpha=\Omega-k\Omega_0$ and study the symmetric partial sums $S_M(\alpha)=\sum_{n=-M}^{M}e^{-j\alpha n}=\frac{\sin((2M+1)\alpha/2)}{\sin(\alpha/2)}$. As $M\to\infty$, they develop sharper peaks around $\alpha=2\pi m$. The line weight comes from the area check: $\int_{-\pi}^{\pi}S_M(\alpha)\,d\alpha=2\pi$ because only the $n=0$ exponential survives integration over one period. So the limiting impulse train must keep that same $2\pi$ area, giving $\sum_{n=-\infty}^{\infty}e^{-j\alpha n}=2\pi\sum_{m=-\infty}^{\infty}\delta(\alpha-2\pi m)$. Equivalently, the inverse-DTFT check $\frac{1}{2\pi}\int 2\pi A\,\delta(\Omega-\Omega_c)e^{j\Omega n}\,d\Omega=Ae^{j\Omega_c n}$ confirms that a harmonic of amplitude $A$ must appear as a spectral line of area $2\pi A$.
- Starting from the DTFS synthesis formula $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{jk\Omega_0 n}$, how do you derive the DTFT as the periodic line spectrum $X_{\mathrm{DTFT}}(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$? ::@:: Start from $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{jk\Omega_0 n}$. <br/> Substitute into $X_{\mathrm{DTFT}}(e^{j\Omega})=\sum_n \tilde x[n]e^{-j\Omega n}$. <br/> Interchange the $n$-sum and the $k$-sum to get $\sum_{k=0}^{N-1}\tilde X[k]\sum_n e^{-j(\Omega-k\Omega_0)n}$. <br/> Replace each inner sum by $2\pi\sum_m\delta(\Omega-k\Omega_0-2\pi m)$. <br/> Then $X_{\mathrm{DTFT}}(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$, which is the periodic DTFT line spectrum.
- Why is DTFS more closely related to the DFT than to the general DTFT? ::@:: Because DTFS and DFT both use a finite harmonic index $k=0,1,\dots,N-1$, both work modulo $N$, and both describe one period without explicit Dirac impulses in frequency. For one period of a period-$N$ sequence, the DFT coefficients satisfy $X[k]=N\tilde X[k]$, so the DFT is the finite computational version of the same harmonic data.

## orthogonality and DTFS coefficient derivation

The DTFS coefficient formula comes from orthogonality of discrete complex exponentials over one period, so it is worth making the proof explicit rather than memorizing the answer only. Define $S_{k,r}=\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}$.

If $k=r\pmod N$, then $e^{j2\pi (k-r)n/N}=1$ for every $n$, so $S_{k,r}=\sum_{n=0}^{N-1}1=N$. If $k\neq r\pmod N$, define $q=e^{j2\pi (k-r)/N}$. Then $q\neq1$, so the sum is geometric: $S_{k,r}=1+q+q^2+\cdots+q^{N-1}=\frac{1-q^N}{1-q}$. But $q^N=e^{j2\pi(k-r)}=1$, so $S_{k,r}=0$. Therefore $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=\begin{cases}N,&k=r\pmod N,\\0,&k\neq r\pmod N.\end{cases}$

The intuition is the same as in ordinary Fourier orthogonality. When $k=r$, the phasors do not rotate, so every term points in the same direction and adds coherently. When $k\neq r$, the phasors wrap around the unit circle in evenly spaced steps and close into a polygon, so the vector sum is zero.

---

Flashcards for this section are as follows:

- What orthogonality identity drives the DTFS derivation? ::@:: Over one period, $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=N$ when $k=r\pmod N$ and $0$ otherwise. So equal harmonics add coherently, while distinct harmonics cancel over the full period.
- Why does $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}$ vanish when $k\neq r\pmod N$? ::@:: Let $q=e^{j2\pi (k-r)/N}\neq1$. Then the sum is geometric: $\sum_{n=0}^{N-1}q^n=(1-q^N)/(1-q)=0$ because $q^N=e^{j2\pi(k-r)}=1$. Intuitively, the phasors complete a closed polygon on the unit circle and cancel.
- How do you derive the DTFS analysis formula from the synthesis formula step by step? ::@:: Start from $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. <br/> Multiply by $e^{-j2\pi rn/N}$ to get $\tilde x[n]e^{-j2\pi rn/N}=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi (k-r)n/N}$. <br/> Sum over $n=0,1,\dots,N-1$. <br/> Interchange the $n$-sum and the $k$-sum. <br/> Apply $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=N\delta_{k,r}$ so only the $k=r$ term survives. <br/> Then $\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi rn/N}=N\tilde X[r]$, and dividing by $N$ yields $\tilde X[r]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi rn/N}$.
- What is the DTFS analysis formula? ::@:: It is $\tilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$. <br/> The factor $2\pi k/N$ is $k\Omega_0$, where $\Omega_0=2\pi/N$ comes from the digital-frequency definition $\Omega=\omega T$.
- Why does the DTFS forward formula contain the factor $1/N$? ::@:: Because the orthogonality sum over one period returns $N$, not $1$. So after the basis function isolates the target harmonic, one must divide by $N$ to recover the actual coefficient.
- What is the geometric meaning of a DTFS coefficient? ::@:: It is the projection of the periodic sequence onto one discrete complex exponential basis function over one period. The full-period sum measures alignment with one harmonic, and the factor $1/N$ normalizes that projection.

## normalization map between DTFS and DFT

Once the coefficient relation $X[k]=N\tilde X[k]$ is remembered, the normalization differences between DFT rules and DTFS rules can be derived rather than memorized blindly. This is the safest exam strategy, because one can start from the DFT rule already in memory and then convert it carefully into the DTFS/DFS convention.

For circular convolution, the DFT rule is $Y[k]=X[k]H[k]$. If $X[k]=N\tilde X[k]$, $H[k]=N\tilde H[k]$, and $Y[k]=N\tilde Y[k]$, then $N\tilde Y[k]=(N\tilde X[k])(N\tilde H[k])$, so $\tilde Y[k]=N\tilde X[k]\tilde H[k]$. That extra factor $N$ appears because the DTFS coefficients were already scaled down by $1/N$ during analysis.

For pointwise multiplication in time, the DFT rule is $Y[k]=\frac{1}{N}(X\circledast H)[k]$. Substituting $X=N\tilde X$, $H=N\tilde H$, and $Y=N\tilde Y$ gives $N\tilde Y[k]=\frac{1}{N}(N\tilde X\circledast N\tilde H)[k]=N(\tilde X\circledast\tilde H)[k]$, so $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$. Here the DFT factor $1/N$ cancels exactly against the two coefficient rescalings.

For energy bookkeeping, the DFT Parseval rule is $\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|X[k]|^2$. Replacing $X[k]$ by $N\tilde X[k]$ gives $\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|N\tilde X[k]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$, which is exactly the DTFS Parseval formula.

The interpretation is simple. DFT coefficients are raw finite sums, so their formulas need a compensating $1/N$ when one reconstructs the sequence or converts spectral products back into physical-scale answers. DTFS coefficients are already averages over one period, so the corresponding rules move the normalization factors to different places. The underlying harmonic algebra is the same; only the bookkeeping convention changes.

---

Flashcards for this section are as follows:

- How do you derive the DTFS circular-convolution rule from the DFT product rule? ::@:: Start from the DFT rule $Y[k]=X[k]H[k]$. <br/> Substitute $X[k]=N\tilde X[k]$, $H[k]=N\tilde H[k]$, and $Y[k]=N\tilde Y[k]$. <br/> Then $N\tilde Y[k]=(N\tilde X[k])(N\tilde H[k])$, so $\tilde Y[k]=N\tilde X[k]\tilde H[k]$. <br/> The extra factor $N$ appears because DTFS coefficients already carry the $1/N$ averaging factor.
- How do you derive the DTFS multiplication rule from the DFT multiplication rule? ::@:: Start from the DFT rule $Y[k]=\frac{1}{N}(X\circledast H)[k]$. <br/> Substitute $X=N\tilde X$, $H=N\tilde H$, and $Y=N\tilde Y$. <br/> Then $N\tilde Y[k]=\frac{1}{N}(N\tilde X\circledast N\tilde H)[k]=N(\tilde X\circledast\tilde H)[k]$. <br/> So $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$. <br/> The DFT factor $1/N$ is exactly cancelled by the coefficient rescaling.
- How do you derive the DTFS Parseval formula from the DFT Parseval formula? ::@:: Start from $\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|X[k]|^2$. <br/> Replace $X[k]$ by $N\tilde X[k]$. <br/> Then $\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}|N\tilde X[k]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$. <br/> So the DTFS energy rule is just the DFT Parseval rule rewritten with $X[k]=N\tilde X[k]$.
- Why do DFT and DTFS/DFS have different normalization factors even though they use the same harmonics? ::@:: Because they place the factor $1/N$ on opposite sides of the transform pair. DFT keeps the forward coefficients as raw sums and normalizes during inversion, while DTFS/DFS averages during analysis and synthesizes directly.

## periodicity, symmetry, and circular operations for DTFS

Time-domain periodicity is built into the data: $\tilde x[n+N]=\tilde x[n]$. The DTFS coefficients are also periodic in the frequency index: $\tilde X[k+N]=\tilde X[k]$. A delay by $n_0$ samples multiplies the coefficients by the phase factor $e^{-j2\pi kn_0/N}$, while modulation by $e^{j2\pi k_0 n/N}$ circularly shifts the coefficient sequence to $\tilde X[(k-k_0)_N]$. The word _circular_ is essential because the coefficient index wraps modulo $N$.

If the periodic sequence is real valued, then the DTFS coefficients satisfy conjugate symmetry: $\tilde X[N-k]=\tilde X^*[k]$, with the usual caveat that $k=0$ and, when $N$ is even, $k=N/2$ are their own partners. Parseval's theorem is $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$, so the harmonic coefficients account exactly for the energy over one period.

There are two more symmetry rules that are easy to forget but very useful in problem solving. If $y[n]=\tilde x^*[n]$, then $\tilde Y[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x^*[n]e^{-j2\pi kn/N}=\left(\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{j2\pi kn/N}\right)^*=\tilde X^*[(-k)_N]$. So conjugation in time becomes conjugation plus frequency reversal in the DTFS coefficients.

If $y[n]=\tilde x^*[(-n)_N]$, let $m=(-n)_N$ in the analysis sum. Then $\tilde Y[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x^*[(-n)_N]e^{-j2\pi kn/N}=\frac{1}{N}\sum_{m=0}^{N-1}\tilde x^*[m]e^{j2\pi km/N}=\tilde X^*[k]$. So conjugation together with time reversal removes the frequency reversal and leaves only coefficient conjugation.

For periodic sequences, convolution is naturally circular. If $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$ denotes period-$N$ circular convolution, then the DTFS coefficients satisfy $\tilde Y[k]=N\tilde X[k]\tilde H[k]$, exactly the DFT product rule rewritten through $X[k]=N\tilde X[k]$. Conversely, pointwise multiplication in time corresponds to circular convolution in frequency without an extra factor when written in DTFS coefficients: $\widetilde{xh}[k]=(\tilde X\circledast\tilde H)[k]$. The conceptual reason is simple: a periodic sequence already wraps every $N$ samples, so shifting beyond one edge re-enters from the other edge.

Worked examples make this wrapping easier to remember. For the period-$4$ constant sequence $\tilde x[n]=1$, the only nonzero coefficient is $\tilde X[0]=1$ and the other coefficients vanish by cancellation of discrete phasors. So just as a constant finite record concentrates at DC in the DFT, a constant periodic sequence concentrates at the zero harmonic in DTFS.

---

Flashcards for this section are as follows:

- What are the time-domain and frequency-domain periodicity rules in DTFS? ::@:: They are $\tilde x[n+N]=\tilde x[n]$ and $\tilde X[k+N]=\tilde X[k]$.
- What happens to DTFS coefficients when the sequence is delayed by $n_0$ samples? ::@:: The delay $\tilde x[n-n_0]$ multiplies the coefficients by the phase factor $e^{-j2\pi kn_0/N}$.
- What happens to DTFS coefficients when the sequence is multiplied by $e^{j2\pi k_0 n/N}$? ::@:: The coefficients shift circularly so that $\tilde X[k]$ becomes $\tilde X[(k-k_0)_N]$.
- What conjugate-symmetry rule holds for the DTFS of a real sequence? ::@:: It is $\tilde X[N-k]=\tilde X^*[k]$.
- What DTFS property corresponds to conjugation in time? ::@:: If $y[n]=\tilde x^*[n]$, then $\tilde Y[k]=\tilde X^*[(-k)_N]=\tilde X^*[N-k]$. So time conjugation becomes conjugation plus frequency reversal.
- What DTFS property corresponds to conjugation together with time reversal? ::@:: If $y[n]=\tilde x^*[(-n)_N]$, then $\tilde Y[k]=\tilde X^*[k]$. So time reversal cancels the frequency reversal that appears under plain conjugation.
- What is Parseval's theorem for DTFS? ::@:: It is $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$.
- What rule connects circular convolution and DTFS coefficients? ::@:: If $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$, then $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.
- Why is circular convolution the natural convolution for periodic sequences? ::@:: Because the sequence already wraps modulo $N$, so shifting beyond one edge automatically re-enters from the other edge.
- Worked example: For the period-$4$ constant sequence $\tilde x[n]=1$, what DTFS coefficients should you expect? ::@:: The zero-harmonic coefficient is $\tilde X[0]=\frac{1}{4}(1+1+1+1)=1$, while the coefficients for $k=1,2,3$ vanish because the corresponding discrete phasors cancel over one full period. So the only nonzero coefficient is the DC term.

## linearity and zero padding

The DFT is linear: $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$. In practice, however, both sequences must be represented at the same transform length. If one record is shorter, it must be zero-padded before combining or comparing transforms so that both transforms refer to the same bin spacing and the same modulo-$N$ interpretation.

To describe zero padding precisely, suppose the original finite record has length $L$ and is stored on $0\le n\le L-1$. The $N$-point zero-padded sequence with $N\ge L$ is $x_N[n]=\begin{cases}x[n],&0\le n\le L-1,\\0,&L\le n\le N-1.\end{cases}$

Its $N$-point DFT is $X_N[k]=\sum_{n=0}^{N-1}x_N[n]e^{-j2\pi kn/N}=\sum_{n=0}^{L-1}x[n]e^{-j2\pi kn/N}=X\!\left(e^{j2\pi k/N}\right)$,
where $X(e^{j\Omega})=\sum_{n=0}^{L-1}x[n]e^{-j\Omega n}$ is the DTFT of the original finite record. This formula is the key interpretation: zero padding does not create a new spectrum; it samples the same underlying DTFT on a finer grid. If one increases the transform length from $M$ to $N$, then the digital-frequency spacing shrinks from $2\pi/M$ to $2\pi/N$. So the plotted spectrum looks smoother because more grid points lie on the same DTFT curve, not because the data contain more physical information.

This is why zero padding improves interpolation of the plotted spectrum but does not improve the true frequency resolution set by the observation length. The record length $L$ determines the underlying DTFT features such as main-lobe width and the ability to distinguish nearby tones, whereas the chosen DFT length $N$ only determines how densely that same DTFT is sampled.

It is also important to pad in the right place. If the record is naturally indexed from $0$ to $L-1$, the standard choice is to append zeros at the tail so the original sample locations stay fixed. More generally, zeros should be inserted only outside the actual support while preserving the original index origin and relative sample positions. Padding in the middle changes the sequence itself unless one is deliberately redefining the indexing.

In convolution problems zero padding has a second role: it provides extra room so circular wrap-around does not contaminate the desired linear result. If $x[n]$ has length $N_x$ and $h[n]$ has length $N_h$, then the linear convolution has length $N_x+N_h-1$. So choose a DFT length $N\ge N_x+N_h-1$ and define $x_N[n]=\begin{cases}x[n],&0\le n\le N_x-1,\\0,&N_x\le n\le N-1,\end{cases}\qquad h_N[n]=\begin{cases}h[n],&0\le n\le N_h-1,\\0,&N_h\le n\le N-1.\end{cases}$

Then the $N$-point circular convolution of $x_N[n]$ and $h_N[n]$ agrees with the ordinary linear convolution, because the output support fits entirely inside one length-$N$ period and therefore no tail wraps back to the front. Intuitively, zero padding creates a guard interval that absorbs what would otherwise fold around the circular boundary.

---

Flashcards for this section are as follows:

- What is the linearity property of the DFT? ::@:: It is $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$.
- Why must sequences use the same DFT length in practical linearity calculations? ::@:: Because the DFT length fixes the frequency-bin spacing and the modulo-$N$ wrap-around interpretation, so different lengths describe different transform problems.
- What does zero padding change and what does it preserve? ::@:: It preserves the original nonzero sample values and their relative positions, but changes the transform length $N$, the bin spacing $2\pi/N$, and the amount of room available before circular wrap-around occurs.
- Why does zero padding sample the same DTFT more densely rather than create new spectral information? ::@:: For a length-$L$ record padded to length $N$, $X_N[k]=\sum_{n=0}^{N-1}x_N[n]e^{-j2\pi kn/N}=\sum_{n=0}^{L-1}x[n]e^{-j2\pi kn/N}=X(e^{j2\pi k/N})$. So zero padding only changes which DTFT grid points are sampled; it does not change the underlying DTFT itself.
- Why does zero padding make a spectrum plot look smoother without increasing true resolution? ::@:: Because increasing $N$ shrinks the bin spacing from $2\pi/M$ to $2\pi/N$, so more sampled points lie on the same DTFT curve. The plot becomes denser, but no new physical information has been added to the record.
- Where should zeros be inserted when zero padding a sequence? ::@:: Insert zeros only outside the true support while preserving the original index origin and relative sample positions. For a record stored on $0,1,\dots,L-1$, the standard choice is to append zeros at the tail. Padding in the middle changes the sequence unless one is deliberately redefining its indexing.
- How do you zero-pad properly to compute linear convolution with DFTs? ::@:: If $x[n]$ has length $N_x$ and $h[n]$ has length $N_h$, choose a transform length $N\ge N_x+N_h-1$ and pad both sequences to that same length. Then the $N$-point circular convolution equals the ordinary linear convolution because the output support fits within one period and no wrap-around occurs.

## principal value interval extraction

The periodic-extension viewpoint becomes much clearer if one names the operation of keeping one representative block. Suppose a finite record $x[n]$ is supported on $0\le n\le N-1$. Its period-$N$ periodic summation is $x_p[n]=\sum_{r=-\infty}^{\infty}x[n-rN]$. This copies the same record every $N$ samples, so $x_p[n+N]=x_p[n]$.

If the original support is shorter than the repeat period, then periodic summation simply lays down disjoint copies of the same record every $N$ samples. So to recover the original record, one does not need a complicated cancellation picture: one simply windows back one chosen copy. Define the rectangular window $G_N[n]=u[n]-u[n-N]$. Then $G_N[n]=1$ for $0\le n\le N-1$ and $0$ otherwise, so $x[n]=x_p[n]G_N[n]$. This operation is called principal value interval extraction: one takes the periodic sequence and keeps only one chosen interval of length $N$.

The same idea can be written in the form that often appears in course notes: $x[n]=x_p[n]u[n]-x_p[n-N]u[n-N]$. Since $x_p[n-N]=x_p[n]$ by periodicity, this is exactly the same as $x[n]=x_p[n](u[n]-u[n-N])=x_p[n]G_N[n]$. So this subtraction formula is best read as an algebraic way to implement the window, not as a new intuition competing with the simpler picture of repeat then window back.

This viewpoint explains circular shift cleanly. If the periodic extension is shifted by $m$ samples, then the extracted length-$N$ record is $x_c[n]=x_p[n-m]G_N[n]$. So a circular shift is not an ordinary open-axis delay; it is principal-interval extraction after shifting a periodic sequence on a ring and then keeping one principal interval.

---

Flashcards for this section are as follows:

- What is principal value interval extraction in DFT language? ::@:: It is the operation of taking a period-$N$ periodic extension and keeping exactly one representative block of length $N$, usually $0\le n\le N-1$.
- How do you define the periodic summation of a length-$N$ record? ::@:: If $x[n]$ is supported on $0\le n\le N-1$, its period-$N$ periodic summation is $x_p[n]=\sum_{r=-\infty}^{\infty}x[n-rN]$, so $x_p[n+N]=x_p[n]$.
- How do you extract the principal interval from a periodic summation? ::@:: Define $G_N[n]=u[n]-u[n-N]$. Then $x[n]=x_p[n]G_N[n]$, so the window keeps the samples on $0\le n\le N-1$ and removes the other periodic copies.
- What is the right intuition for principal value interval extraction when the support is shorter than the repeat period? ::@:: Periodic summation simply repeats the same record every $N$ samples. To recover the original record, just window back one chosen copy. The formula $x[n]=x_p[n]G_N[n]$ is exactly that windowing operation.
- What does the identity $x[n]=x_p[n]u[n]-x_p[n-N]u[n-N]$ mean? ::@:: It is an algebraic rewriting of the same windowing idea, because $x_p[n-N]=x_p[n]$ by periodicity and therefore $x[n]=x_p[n](u[n]-u[n-N])=x_p[n]G_N[n]$. So it is still just principal interval extraction.
- How does principal value interval extraction explain circular shift? ::@:: If the periodic extension is shifted by $m$ samples, then the extracted stored block is $x_c[n]=x_p[n-m]G_N[n]$. So a circular shift means: shift on a ring, then keep one principal interval.

Define the circularly shifted sequence by $x_c[n]=x[(n-m)_N]$, where $(\cdot)_N$ means reduction modulo $N$. To derive its DFT, write $X_c[k]=\sum_{n=0}^{N-1}x[(n-m)_N]e^{-j2\pi kn/N}$. Re-index with $r=(n-m)_N$, so $n=(r+m)_N$ and the finite sum still runs over one complete set of residues. This gives $X_c[k]=\sum_{r=0}^{N-1}x[r]e^{-j2\pi k(r+m)/N}=e^{-j2\pi km/N}\sum_{r=0}^{N-1}x[r]e^{-j2\pi kr/N}=e^{-j2\pi km/N}X[k]$.
So a circular time shift produces a linear phase factor, just as an ordinary delay does in other Fourier settings. The key difference from linear shift is geometric. A linear delay moves a sequence along an open index axis and may enlarge the visible support interval. A circular shift instead moves samples around a closed loop of $N$ positions, so samples leaving one edge re-enter from the other edge.

Circular shift of the frequency bins has the dual effect: it corresponds to multiplying the time-domain sequence by a complex exponential. This is the finite-length analogue of discrete-time frequency shifting.

---

Flashcards for this section are as follows:

- What is a circular shift of a length-$N$ sequence? ::@:: It is the modulo-$N$ shift $x_c[n]=x[(n-m)_N]$, which moves samples by $m$ positions and wraps any samples that pass one edge back to the other side.
- If $x_c[n]=x[(n-m)_N]$, how do you derive the DFT of the shifted sequence? ::@:: Start from $X_c[k]=\sum_{n=0}^{N-1}x[(n-m)_N]e^{-j2\pi kn/N}$. <br/> Re-index with $r=(n-m)_N$. <br/> Then factor out the term $e^{-j2\pi km/N}$ and recognize the remaining sum as $X[k]$. <br/> So $X_c[k]=e^{-j2\pi km/N}X[k]=W_N^{mk}X[k]$.
- Why is the DFT shift law called circular rather than ordinary delay? ::@:: Because the finite transform assumes a periodic extension of length $N$, so the shifted record wraps around modulo $N$ instead of moving on an open index axis.
- What is the difference between linear shift and circular shift? ::@:: Linear shift can create empty space and extend support, whereas circular shift preserves exactly $N$ stored sample positions and wraps outgoing samples back into the record.
- What time-domain effect corresponds to circularly shifting the DFT bins? ::@:: It corresponds to multiplying the time-domain sequence by a complex exponential, the finite-length analogue of frequency shifting.

## circular convolution and its relation to linear convolution

For two length-$N$ sequences, the circular convolution is $y[n]=(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$. Its DFT satisfies the product rule $Y[k]=X[k]H[k]$. Conversely, pointwise multiplication in time corresponds to circular convolution in frequency with scaling: $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.

Circular convolution differs from ordinary linear convolution because the index arithmetic is modulo $N$. The expression $h[(n-m)_N]$ means that as soon as the shift runs past one edge of the stored interval, it wraps around and re-enters from the other edge. So circular convolution is the natural convolution on a ring, whereas ordinary convolution is the natural convolution on an infinite line.

It is helpful to compare the matching conditions directly. In ordinary linear convolution, $y_{\mathrm{lin}}[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$, so the two argument indices must satisfy $m+(n-m)=n$ as an ordinary integer equality. In circular convolution, $y_c[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$, so the matching rule is only modulo $N$: $m+(n-m)_N\equiv n\pmod N$. That extra modulo operation is exactly what makes contributions wrap around the finite record instead of staying on an open line.

The relation to principal value interval extraction is very important. Let $x[n]$ and $h[n]$ be supported on $0\le n\le N-1$, and let their ordinary linear convolution be $y_{\mathrm{lin}}[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]$. Then the $N$-point circular convolution is $y_c[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]=\sum_{r=-\infty}^{\infty}y_{\mathrm{lin}}[n-rN]$ for $0\le n\le N-1$. So circular convolution is the periodic summation, or aliasing, of the linear convolution, followed by principal-interval extraction.

This formula explains zero padding immediately. If $N\ge N_x+N_h-1$, then the linear-convolution support fits inside one interval of length $N$, so in $y_c[n]=\sum_{r=-\infty}^{\infty}y_{\mathrm{lin}}[n-rN]$ only the $r=0$ term survives on the principal interval. That is exactly why enough zero padding makes circular convolution agree with ordinary linear convolution.

An explicit example shows how to compute circular convolution operationally. Let $N=3$, $x[n]=[1,2,3]$, and $h[n]=[4,5,6]$. Then $y_c[0]=x[0]h[(0-0)_3]+x[1]h[(0-1)_3]+x[2]h[(0-2)_3]=1\cdot4+2\cdot6+3\cdot5=31$, $y_c[1]=x[0]h[(1-0)_3]+x[1]h[(1-1)_3]+x[2]h[(1-2)_3]=1\cdot5+2\cdot4+3\cdot6=31$, and $y_c[2]=x[0]h[(2-0)_3]+x[1]h[(2-1)_3]+x[2]h[(2-2)_3]=1\cdot6+2\cdot5+3\cdot4=28$. Therefore the $3$-point circular convolution is $y_c=[31,31,28]$.

Now compare with ordinary linear convolution. Without the modulo reduction, $y_{\mathrm{lin}}[n]=\sum_m x[m]h[n-m]$ gives $y_{\mathrm{lin}}=[4,13,28,27,18]$. The circular result is obtained by wrapping the tail back modulo $3$: $y_c[0]=4+27=31$, $y_c[1]=13+18=31$, and $y_c[2]=28$. So the calculation procedure is: compute with wrapped indices directly, or equivalently compute the linear convolution first and then add together terms whose indices are congruent modulo $N$.

The wrap-around interpretation is the real concept to remember. Circular convolution is what happens when the sequence is imagined on a ring. Linear convolution is what happens when the sequence lives on a line and is allowed to grow in support. For example, if $x[n]=[1,1,1]$ and $h[n]=[1,1,1]$ are treated as length-$3$ sequences, the ordinary linear convolution is $[1,2,3,2,1]$, but the length-$3$ circular convolution folds the tail back and becomes $[3,3,3]$.

---

Flashcards for this section are as follows:

- What is the formula for circular convolution of two length-$N$ sequences? ::@:: It is $(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$.
- What DFT rule corresponds to circular convolution in time? ::@:: If $y[n]=x[n]\circledast h[n]$, then $Y[k]=X[k]H[k]$.
- What happens in the DFT frequency domain when two sequences are multiplied pointwise in time? ::@:: Pointwise multiplication in time gives circular convolution in frequency with the scaling factor $1/N$, namely $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.
- Why is direct DFT multiplication not automatically equal to ordinary linear convolution? ::@:: Because DFT multiplication produces circular convolution, which wraps contributions modulo $N$ instead of allowing the support to extend naturally.
- What is the operational difference between linear convolution and circular convolution? ::@:: In linear convolution, the matching rule is $m+(n-m)=n$ on an open index line, so the support can grow. In circular convolution, the rule is $m+(n-m)_N\equiv n\pmod N$, so the second index is reduced modulo $N$ and contributions wrap around the finite record.
- How is circular convolution related mathematically to ordinary linear convolution? ::@:: If $y_{\mathrm{lin}}[n]=\sum_m x[m]h[n-m]$ is the ordinary linear convolution of two finite records supported on $0\le n\le N-1$, then the $N$-point circular convolution is $y_c[n]=\sum_{r=-\infty}^{\infty}y_{\mathrm{lin}}[n-rN]$ for $0\le n\le N-1$. So circular convolution is the periodic summation, or aliasing, of the linear convolution followed by principal-interval extraction.
- Why is circular convolution naturally tied to principal value interval extraction? ::@:: Because the DFT treats each finite record as one period of a periodic extension. Multiplying spectra therefore produces convolution on that periodic extension, and the stored output is one extracted principal interval of the wrapped result.
- How do you use DFTs to compute an ordinary linear convolution correctly? ::@:: Zero-pad the sequences to a transform length $N\ge N_x+N_h-1$ before taking DFTs, so the circular result matches the linear convolution over the full support.
- Worked example: If $x[n]=[1,2,3]$ and $h[n]=[4,5,6]$ are treated as length-$3$ sequences, how do you compute the circular convolution explicitly? ::@:: Use $y_c[n]=\sum_{m=0}^{2}x[m]h[(n-m)_3]$. <br/> Then $y_c[0]=1\cdot4+2\cdot6+3\cdot5=31$, $y_c[1]=1\cdot5+2\cdot4+3\cdot6=31$, and $y_c[2]=1\cdot6+2\cdot5+3\cdot4=28$. <br/> So the $3$-point circular convolution is $[31,31,28]$.
- Worked example: For $x[n]=[1,2,3]$ and $h[n]=[4,5,6]$, how does the circular result differ from the ordinary linear convolution? ::@:: The linear convolution is $[4,13,28,27,18]$. <br/> Reducing indices modulo $3$ wraps the tail back, so $y_c[0]=4+27=31$, $y_c[1]=13+18=31$, and $y_c[2]=28$. <br/> Therefore the circular convolution is the aliased version $[31,31,28]$ of the linear result.
- Worked example: If $x[n]=[1,1,1]$ and $h[n]=[1,1,1]$ are treated as length-$3$ sequences, why does circular convolution differ from linear convolution? ::@:: The linear convolution is $[1,2,3,2,1]$. <br/> In length $3$, the late samples wrap around, so $y[0]=1+2=3$, $y[1]=2+1=3$, and $y[2]=3$. <br/> Thus the $3$-point circular convolution is $[3,3,3]$, which is different because wrap-around has folded the tail back into the beginning.
