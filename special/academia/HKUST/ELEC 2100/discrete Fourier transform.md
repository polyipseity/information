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

The discrete Fourier transform (DFT) converts $N$ samples into $N$ frequency-bin coefficients. It is the computational form of discrete-time Fourier analysis, keeping only the $N$ equally spaced frequencies $\Omega_k=2\pi k/N$ instead of the full continuous digital-frequency variable.

Two viewpoints are equally valid. The DFT samples the DTFT of a length-$N$ record on a uniform frequency grid. It also treats that record as one period of a length-$N$ periodic extension, which is why circular shift and circular convolution appear automatically. Both viewpoints describe the same mathematics.

This note also covers the discrete-time Fourier series (DTFS/DFS). DTFS/DFS and DFT both use a finite harmonic coefficient list indexed by $k=0,1,\dots,N-1$, while the general DTFT uses the continuous digital-frequency variable $\Omega=\omega T$ and represents periodic sequences by a line spectrum. For period-$N$ sequences, discrete harmonics, orthogonality over one period, or circular operations, this is the right note.

For the continuous digital-frequency viewpoint of a general sequence, see [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md). For continuous-time, use [Fourier series](Fourier%20series.md) (periodic) or [Fourier transform](Fourier%20transform.md) (aperiodic).

---

Flashcards for this section are as follows:

- What does the DFT do? ::@:: It converts a finite record of $N$ samples into $N$ frequency-bin coefficients on an $N$-point grid.
- Why is the DFT not just the DTFT at fewer points? ::@:: Because the DFT treats a finite record as one period of a periodic extension, so circular shift and circular convolution are built into the model.
- How is DTFS/DFS grouped with the DFT rather than the DTFT? ::@:: Because DTFS/DFS and DFT both use one finite harmonic coefficient cycle for period-$N$ data, whereas the general DTFT uses the continuous variable $\Omega=\omega T$ and represents periodic sequences by a line spectrum.
- Where does this note sit among the Fourier notes? ::@:: This note is the finite-grid computational transform for discrete data. DTFT keeps a continuous digital-frequency variable for general sequences. Fourier series and Fourier transform are the continuous-time periodic and aperiodic counterparts.

## definition and inverse transform

For a length-$N$ sequence $x[n]$ indexed by $n=0,1,\dots,N-1$, the DFT is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ for $k=0,1,\dots,N-1$, and the inverse DFT is $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$ for $n=0,1,\dots,N-1$. If we define the twiddle factor $W_N=e^{-j2\pi/N}$, the forward transform can also be written as $X[k]=\sum_{n=0}^{N-1}x[n]W_N^{kn}$.

The time index $n$ labels sample positions, while $k$ labels frequency bins. The DFT maps one $N$-dimensional vector to another using complex exponential basis functions that are orthogonal over the finite grid, which is why the inverse transform recovers the original record exactly.

For real sequences, $X[N-k]=X^*[k]$. The proof uses $X[N-k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi (N-k)n/N}=\sum_{n=0}^{N-1}x[n]e^{j2\pi kn/N}=X^*[k]$ (since $x[n]$ is real and $e^{-j2\pi n}=1$). Nonzero-frequency bins come in conjugate pairs: $k$ and $N-k$ carry the same magnitude and opposite phase.

Self-partner bins solve $N-k\equiv k\pmod N$, equivalently $2k\equiv0\pmod N$. So $k=0$ is always self-partner, and when $N$ is even, $k=N/2$ is also self-partner. These bins must be purely real: $k=0$ is DC, while $k=N/2$ is the Nyquist bin whose phasor alternates between $+1$ and $-1$.

Two short examples help. For $x[n]=\{1,1,1,1\}$, $X[0]=4$ and $X[1]=X[2]=X[3]=0$ (the phasors cancel). For $x[n]=\{1,0,0,0\}$, every bin equals $1$. A constant record concentrates at DC; an impulse spreads uniformly.

---

Flashcards for this section are as follows:

- What is the forward DFT formula for an $N$-point sequence? ::@:: It is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ for $k=0,1,\dots,N-1$.
- What is the inverse DFT formula? ::@:: It is $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$ for $n=0,1,\dots,N-1$.
- What does the symbol $W_N$ mean in DFT notation? ::@:: It means $W_N=e^{-j2\pi/N}$, so the forward transform can be written compactly as $X[k]=\sum_{n=0}^{N-1}x[n]W_N^{kn}$.
- What do the indices $n$ and $k$ represent in the DFT? ::@:: $n$ labels time-domain sample positions inside the finite record, while $k$ labels discrete frequency bins.
- Why can the inverse DFT recover the record exactly from the $N$ coefficients? ::@:: Because the complex exponential basis vectors are orthogonal over the length-$N$ grid, so the transform coefficients give a complete coordinate description of the finite record.
- What conjugate-symmetry rule should you expect when the sequence is real valued? ::@:: The DFT satisfies $X[N-k]=X^*[k]$, so bins usually appear in conjugate pairs $k$ and $N-k$ with equal magnitude and opposite phase. The self-partner bins solve $N-k\equiv k\pmod N$, equivalently $2k\equiv0\pmod N$, so $k=0$ is always self-partner and $k=N/2$ is also self-partner when $N$ is even. Those bins must therefore be purely real.
- Why are $k=0$ and, when $N$ is even, $k=N/2$ special in DFT conjugate symmetry? ::@:: Because they are their own negative-frequency partners modulo $N$. The DC bin $k=0$ has no distinct partner, and the Nyquist bin $k=N/2$ also has none when $N$ is even, so each must equal its own conjugate and hence be real.
- Worked case: Why does the four-point constant sequence $x[n]=\{1,1,1,1\}$ produce only a DC DFT component? ::@:: The DC bin is $X[0]=1+1+1+1=4$. For $k=1,2,3$, the basis phasors complete one full cycle around the unit circle and cancel, so $X[1]=X[2]=X[3]=0$. Thus the DFT is $\{4,0,0,0\}$.
- Worked case: Why does the four-point impulse $x[n]=\{1,0,0,0\}$ give $X[k]=1$ for every bin? ::@:: In $X[k]=\sum_{n=0}^{3}x[n]e^{-j2\pi kn/4}$, only the $n=0$ term is nonzero. Since $e^0=1$, every bin gets the same contribution and therefore $X[k]=1$ for all $k$.

## matrix viewpoint of the DFT

The DFT is also a matrix multiplication. Let $\mathbf{x}=[x[0],x[1],\dots,x[N-1]]^T$ and $\mathbf{X}=[X[0],X[1],\dots,X[N-1]]^T$. Define the DFT matrix $F_N$ by $[F_N]_{k,n}=W_N^{kn}=e^{-j2\pi kn/N}$ for $k,n=0,1,\dots,N-1$. Then the forward transform is $\mathbf{X}=F_N\mathbf{x}$.

The inverse matrix comes from orthogonality: $F_N^H F_N=N I$, so $F_N^{-1}=\frac{1}{N}F_N^H$ and the inverse DFT is $\mathbf{x}=\frac{1}{N}F_N^H\mathbf{X}$. This is why the inverse keeps the same exponentials but flips the sign and adds $1/N$.

Each row of $F_N$ is a sampled complex exponential, so each DFT coefficient is a correlation of the data with one basis row. The DFT is a change from sample basis to exponential basis.

For $N=4$, $W_4=-j$, so $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$. If $\mathbf{h}=[1,2,-1,3]^T$, then $\mathbf{H}=F_4\mathbf{h}=\begin{bmatrix}5\\2+j\\-5\\2-j\end{bmatrix}$. The matrix form is the same DFT in linear-algebra language.

---

Flashcards for this section are as follows:

- How do you write the DFT as a matrix multiplication? ::@:: Let $\mathbf{x}=[x[0],x[1],\dots,x[N-1]]^T$ and define $[F_N]_{k,n}=W_N^{kn}=e^{-j2\pi kn/N}$. Then the DFT is $\mathbf{X}=F_N\mathbf{x}$.
- Why does the inverse DFT matrix equal $\frac{1}{N}F_N^H$? ::@:: Because the sampled complex exponentials are orthogonal, so $F_N^H F_N=N I$. Therefore $F_N^{-1}=\frac{1}{N}F_N^H$, which is the matrix form of the inverse DFT.
- What is the best interpretation of the DFT matrix rows? ::@:: Each row is one sampled complex exponential basis vector, so each DFT coefficient is a correlation or projection of the data onto one discrete harmonic.
- What is the $4$-point DFT matrix? ::@:: $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$, since $W_4=-j$.
- Matrix-form worked example: If $\mathbf{h}=[1,2,-1,3]^T$, what is its $4$-point DFT? ::@:: Using $\mathbf{H}=F_4\mathbf{h}$ with $F_4=\begin{bmatrix}1&1&1&1\\1&-j&-1&j\\1&-1&1&-1\\1&j&-1&-j\end{bmatrix}$ gives $\mathbf{H}=\begin{bmatrix}5\\2+j\\-5\\2-j\end{bmatrix}$.

## relation to DTFT and periodic extension

Truncating the sequence to $N$ samples and evaluating the DTFT at $\Omega_k=2\pi k/N$ gives the DFT directly: if $x[n]$ is zero outside $0\le n\le N-1$, then $X(e^{j\Omega})=\sum_{n=0}^{N-1}x[n]e^{-j\Omega n}$, and at $\Omega=\Omega_k$ this equals $X[k]$.

From the periodic-extension viewpoint, if the length-$N$ block is repeated periodically, $X[k]=N\tilde X[k]$ where $\tilde X[k]$ are the DTFS coefficients. Circular phenomena arise because a finite record is one period of a periodic sequence.

DTFS and DFT both use finite coefficient index $k=0,1,\dots,N-1$ and work modulo $N$ without Dirac impulses. The general DTFT uses continuous $\Omega=\omega T$ and represents periodic sequences by a line spectrum. The DFT keeps only one sampled frequency grid, making it the transform used in numerical computation.

---

Flashcards for this section are as follows:

- How is the DFT obtained from the DTFT? ::@:: Restrict the sequence to length $N$ and sample the DTFT at $\Omega_k=2\pi k/N$, so $X[k]=X(e^{j\Omega_k})$.
- What frequencies are sampled in an $N$-point DFT? ::@:: $\Omega_k=2\pi k/N$ for $k=0,1,\dots,N-1$, equivalently $k/N$ cycles per sample, interpreted modulo $2\pi$ on $[-\pi,\pi]$.
- Why does the DFT inherit circular behavior from the periodic-sequence viewpoint? ::@:: Because the finite data block is interpreted as one period of a periodic extension, so shifts and convolutions wrap modulo $N$.
- How are DFT coefficients related to DTFS coefficients? ::@:: With the normalization used here, $X[k]=N\tilde X[k]$.
- Why is DFT closer to DTFS than to DTFT? ::@:: Because both DFT and DTFS use finite index $k=0,1,\dots,N-1$, work modulo $N$, and describe one period without Dirac impulses. The general DTFT uses continuous $\Omega=\omega T$.
- How do the DTFT note and DFT note compare? ::@:: The DTFT note covers discrete-time spectral analysis using the continuous variable $\Omega=\omega T$. The DFT note covers the finite-data transform obtained by sampling on an $N$-point grid.

## relation between DTFS and DFT

For a period-$N$ sequence $\tilde x[n+N]=\tilde x[n]$, the DTFS/DFS pair used in this course is $\tilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$ and $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. For an $N$-point record, the DFT pair is $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ and $x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$.

The course-material distinction is interpretive. DTFS/DFS is used for an explicitly periodic sequence, while DFT is used for a finite record with an implicit periodic extension. That difference matters in exams.

In algebra, the two are the same harmonic decomposition once one period is identified: if $x[n]=\tilde x[n]$ for $0\le n\le N-1$, then $X[k]=N\tilde X[k]$. The basis functions, harmonic grid, modulo-$N$ indexing, and orthogonality are all identical. The only difference is where $1/N$ is placed.

This gives a clean memory rule. DTFS/DFS is the _average-first_ convention: divide by $N$ during analysis, then synthesize directly. DFT is the _sum-first_ convention: keep the forward transform as a raw sum, then divide by $N$ during reconstruction.

---

Flashcards for this section are as follows:

- What is the course-material distinction between DTFS/DFS and DFT? ::@:: DTFS/DFS is for explicitly periodic sequences; DFT is for finite records with an implicit periodic extension. Remember this interpretive distinction in exams.
- How are DTFS/DFS and DFT related algebraically? ::@:: They are the same harmonic decomposition: $X[k]=N\tilde X[k]$. The basis functions, modulo-$N$ indexing, and orthogonality are identical.
- What is the memory rule for $1/N$ placement? ::@:: DTFS/DFS: average-first ($1/N$ in analysis, synthesize directly). DFT: sum-first (raw forward sum, $1/N$ in the inverse).

## periodic sequences and discrete-time Fourier series

For a sequence periodic with period $N$, the fundamental digital angular frequency is $\Omega_0=2\pi/N$ ($1/N$ cycles per sample). The DTFS synthesis formula is $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{jk\Omega_0 n}=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$.

The point of deriving the DTFT of a periodic sequence is to connect two descriptions of the same object. DTFS stores a finite coefficient list $\tilde X[k]$. The DTFT describes the same sequence by a line spectrum in the continuous variable $\Omega$. The derivation shows how the finite list becomes a periodic impulse train.

The notation: $\tilde x[n]$ is the period-$N$ sequence, $\tilde X[k]$ are its DTFS coefficients, $\Omega_0=2\pi/N$, and $X_{\mathrm{DTFT}}(e^{j\Omega})$ is the DTFT as a function of the continuous variable $\Omega$. The index $k$ labels harmonics, while $\Omega$ is continuous.

Now isolate one harmonic. Suppose $\tilde x_{k_0}[n]=\tilde X[k_0]e^{jk_0\Omega_0 n}$. Its DTFT is $X_{k_0}(e^{j\Omega})=\tilde X[k_0]\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k_0\Omega_0)n}$.

This infinite sum must be interpreted distributionally. The symmetric partial sums $S_M(\alpha)=\sum_{n=-M}^{M}e^{-j\alpha n}$ have area $2\pi$ over $[-\pi,\pi]$ (only the $n=0$ term survives integration). As $M\to\infty$, that area concentrates at $\alpha=2\pi m$, giving $\sum_{n=-\infty}^{\infty}e^{-j\alpha n}=2\pi\sum_{m=-\infty}^{\infty}\delta(\alpha-2\pi m)$. The weight $2\pi$ is confirmed by the inverse DTFT: a line $2\pi A\,\delta(\Omega-\Omega_c)$ reconstructs $Ae^{j\Omega_c n}$.

Applying this with $\alpha=\Omega-k_0\Omega_0$ gives $X_{k_0}(e^{j\Omega})=2\pi\tilde X[k_0]\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$. One DTFS harmonic becomes a periodic family of spectral lines, repeated every $2\pi$.

Summing all harmonics: $X_{\mathrm{DTFT}}(e^{j\Omega})=\sum_{k=0}^{N-1}\tilde X[k]\sum_n e^{-j(\Omega-k\Omega_0)n}=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$. The DTFT of a periodic sequence is a periodic line spectrum.

DTFT describes periodic sequences by impulses in $\Omega$. DTFS records only the finite list of line weights $\tilde X[k]$. DTFS is cleaner for periodic sequences because it stores harmonic amplitudes directly.

---

Flashcards for this section are as follows:

- If a discrete-time sequence is periodic with period $N$, what is its fundamental digital angular frequency? ::@:: It is $\Omega_0=2\pi/N$. <br/> Since digital angular frequency is defined by $\Omega=\omega T$, this means $\Omega_0$ is $1/N$ cycles per sample, and distinct digital frequencies are usually interpreted on the principal interval $[-\pi,\pi]$.
- What is the DTFS synthesis formula for a period-$N$ sequence? ::@:: It is $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{jk\Omega_0 n}=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. <br/> Here $\Omega_0=2\pi/N$ comes from $\Omega=\omega T$, so it is the fundamental digital angular frequency in radians per sample, equivalently $1/N$ cycles per sample.
- Why does a period-$N$ sequence need only $N$ DTFS coefficients? ::@:: Because both the sequence and the discrete-frequency description repeat modulo $N$, so one coefficient cycle is complete.
- Why is DTFS cleaner than DTFT for periodic sequences? ::@:: It stores harmonic amplitudes directly as a finite list, rather than as impulses in a continuous variable.
- Why derive the DTFT of a periodic sequence from DTFS? ::@:: To connect the finite harmonic list to the impulse line spectrum that the DTFT produces.
- In the derivation, what do the symbols mean? ::@:: $\tilde x[n]$ is the period-$N$ sequence, $\tilde X[k]$ are DTFS coefficients, $\Omega_0=2\pi/N$ is the fundamental digital angular frequency, $X_{\mathrm{DTFT}}(e^{j\Omega})$ is the DTFT as a function of continuous $\Omega$.
- How does one harmonic appear in the DTFT? ::@:: One DTFS harmonic $\tilde X[k_0]e^{jk_0\Omega_0 n}$ becomes $2\pi\tilde X[k_0]\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$, a periodic family of spectral lines repeated every $2\pi$.
- Why does $\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k\Omega_0)n}$ produce Dirac deltas with weight $2\pi$? ::@:: The symmetric partial sums $S_M(\alpha)=\sum_{n=-M}^{M}e^{-j\alpha n}$ have area $2\pi$ over $[-\pi,\pi]$ (only the $n=0$ term survives integration). As $M\to\infty$, that area concentrates at $\alpha=2\pi m$, giving $2\pi\sum_m\delta(\alpha-2\pi m)$.
- What is the full DTFT of a periodic sequence? ::@:: $X_{\mathrm{DTFT}}(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$, a periodic line spectrum.
- Why is DTFS more closely related to the DFT than to the general DTFT? ::@:: Because DTFS and DFT both use a finite harmonic index $k=0,1,\dots,N-1$, both work modulo $N$, and both describe one period without explicit Dirac impulses in frequency. For one period of a period-$N$ sequence, the DFT coefficients satisfy $X[k]=N\tilde X[k]$, so the DFT is the finite computational version of the same harmonic data.

## orthogonality and DTFS coefficient derivation

The DTFS coefficient formula comes from orthogonality of discrete complex exponentials over one period. Define $S_{k,r}=\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}$.

If $k=r\pmod N$, then $e^{j2\pi (k-r)n/N}=1$ for every $n$, so $S_{k,r}=N$. If $k\neq r\pmod N$, let $q=e^{j2\pi (k-r)/N}\neq1$. Then $S_{k,r}=\frac{1-q^N}{1-q}=0$ because $q^N=e^{j2\pi(k-r)}=1$. So $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=\begin{cases}N,&k=r\pmod N,\\0,&k\neq r\pmod N.\end{cases}$

When $k=r$, the phasors do not rotate and add coherently. When $k\neq r$, they wrap around the unit circle and cancel.

Now derive the DTFS analysis formula. Start from $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. Multiply by $e^{-j2\pi rn/N}$ and sum over $n$:

$\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi rn/N}=\sum_{k=0}^{N-1}\tilde X[k]\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}$.

Orthogonality kills every $k\neq r$ term. The $k=r$ term contributes $N$, giving $N\tilde X[r]$. Dividing by $N$ yields $\tilde X[r]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi rn/N}$.

The factor $1/N$ is needed because the basis vectors are not unit-length: their inner product with themselves is $N$, not $1$. Geometrically, $\tilde X[r]$ is the normalized projection of the periodic sequence onto one discrete exponential basis vector.

---

Flashcards for this section are as follows:

- What orthogonality identity drives the DTFS derivation? ::@:: $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=N$ when $k=r\pmod N$, $0$ otherwise.
- How do you derive the DTFS analysis formula? ::@:: Start from $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. Multiply by $e^{-j2\pi rn/N}$, sum over $n$, interchange sums, apply orthogonality ($k=r$ term gives $N$), divide by $N$.
- What is the DTFS analysis formula? ::@:: $\tilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$.
- Why does the DTFS forward formula contain $1/N$? ::@:: Because the orthogonality sum returns $N$, not $1$.
- What is the geometric meaning of a DTFS coefficient? ::@:: It is the normalized projection of the periodic sequence onto one discrete exponential basis vector over one period.

## normalization map between DTFS and DFT

The normalization map is straightforward once $X[k]=N\tilde X[k]$ is remembered. For circular convolution, $Y[k]=X[k]H[k]$ becomes $N\tilde Y[k]=(N\tilde X[k])(N\tilde H[k])$, so $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.

For pointwise multiplication, $Y[k]=\frac{1}{N}(X\circledast H)[k]$ becomes $N\tilde Y[k]=\frac{1}{N}(N\tilde X\circledast N\tilde H)[k]=N(\tilde X\circledast\tilde H)[k]$, so $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$.

For Parseval, $\sum|x[n]|^2=\frac{1}{N}\sum|X[k]|^2$ becomes $\sum|x[n]|^2=\frac{1}{N}\sum|N\tilde X[k]|^2=N\sum|\tilde X[k]|^2$.

DFT coefficients are raw sums, so their formulas need compensating $1/N$ factors. DTFS coefficients are already averages, so the $1/N$ appears on opposite sides. The underlying harmonic algebra is the same.

---

Flashcards for this section are as follows:

- How do you derive the DTFS circular-convolution rule from the DFT? ::@:: Start from $Y[k]=X[k]H[k]$, substitute $X=N\tilde X$, $H=N\tilde H$, $Y=N\tilde Y$. Then $\tilde Y[k]=N\tilde X[k]\tilde H[k]$. The extra $N$ appears because DTFS coefficients carry the $1/N$ averaging.
- How do you derive the DTFS multiplication rule from the DFT? ::@:: Start from $Y[k]=\frac{1}{N}(X\circledast H)[k]$, substitute $X=N\tilde X$, $H=N\tilde H$, $Y=N\tilde Y$. Then $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$. The DFT factor $1/N$ cancels against the rescalings.
- How do you derive the DTFS Parseval from DFT Parseval? ::@:: Replace $X[k]$ by $N\tilde X[k]$ in $\sum|x[n]|^2=\frac{1}{N}\sum|X[k]|^2$ to get $\sum|x[n]|^2=N\sum|\tilde X[k]|^2$.
- Why do DFT and DTFS/DFS have different normalization factors even though they use the same harmonics? ::@:: Because they place the factor $1/N$ on opposite sides of the transform pair. DFT keeps the forward coefficients as raw sums and normalizes during inversion, while DTFS/DFS averages during analysis and synthesizes directly.

## periodicity, symmetry, and circular operations for DTFS

Time-domain periodicity is built in: $\tilde x[n+N]=\tilde x[n]$. The DTFS coefficients are also periodic: $\tilde X[k+N]=\tilde X[k]$. A delay by $n_0$ multiplies coefficients by $e^{-j2\pi kn_0/N}$, while modulation by $e^{j2\pi k_0 n/N}$ circularly shifts the coefficient sequence to $\tilde X[(k-k_0)_N]$.

For real sequences, conjugate symmetry holds: $\tilde X[N-k]=\tilde X^*[k]$, with $k=0$ and (when $N$ even) $k=N/2$ as their own partners. Parseval: $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$.

Two useful symmetry rules. If $y[n]=\tilde x^*[n]$, then $\tilde Y[k]=\tilde X^*[(-k)_N]$, so time conjugation becomes conjugation plus frequency reversal. If $y[n]=\tilde x^*[(-n)_N]$, then $\tilde Y[k]=\tilde X^*[k]$, so time reversal cancels the frequency reversal.

For periodic sequences, convolution is naturally circular: $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$ gives $\tilde Y[k]=N\tilde X[k]\tilde H[k]$. Pointwise multiplication in time gives circular convolution in frequency: $\widetilde{xh}[k]=(\tilde X\circledast\tilde H)[k]$.

For the period-$4$ constant sequence $\tilde x[n]=1$, only $\tilde X[0]=1$ is nonzero; the others vanish by phasor cancellation.

---

Flashcards for this section are as follows:

- What are the time-domain and frequency-domain periodicity rules in DTFS? ::@:: They are $\tilde x[n+N]=\tilde x[n]$ and $\tilde X[k+N]=\tilde X[k]$.
- What happens to DTFS coefficients when the sequence is delayed by $n_0$ samples? ::@:: The delay $\tilde x[n-n_0]$ multiplies the coefficients by the phase factor $e^{-j2\pi kn_0/N}$.
- What happens to DTFS coefficients when the sequence is multiplied by $e^{j2\pi k_0 n/N}$? ::@:: The coefficients shift circularly so that $\tilde X[k]$ becomes $\tilde X[(k-k_0)_N]$.
- What conjugate-symmetry rule holds for the DTFS of a real sequence? ::@:: It is $\tilde X[N-k]=\tilde X^*[k]$.
- What DTFS property corresponds to time conjugation? ::@:: $y[n]=\tilde x^*[n]$ gives $\tilde Y[k]=\tilde X^*[(-k)_N]$, so conjugation plus frequency reversal.
- What DTFS property corresponds to time conjugation plus reversal? ::@:: $y[n]=\tilde x^*[(-n)_N]$ gives $\tilde Y[k]=\tilde X^*[k]$, so the frequency reversal is cancelled.
- What is Parseval's theorem for DTFS? ::@:: It is $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$.
- What rule connects circular convolution and DTFS coefficients? ::@:: If $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$, then $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.
- Why is circular convolution natural for periodic sequences? ::@:: Because the sequence wraps modulo $N$, so shifting past one edge re-enters from the other.
- Worked example: For period-$4$ constant $\tilde x[n]=1$, what DTFS coefficients do you get? ::@:: Only $\tilde X[0]=1$; the rest vanish by phasor cancellation.

## linearity and zero padding

The DFT is linear: $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$. In practice both sequences must use the same transform length, since different lengths describe different bin spacings and modulo-$N$ interpretations.

For a length-$L$ record zero-padded to length $N$, the $N$-point DFT is $X_N[k]=\sum_{n=0}^{L-1}x[n]e^{-j2\pi kn/N}=X(e^{j2\pi k/N})$. Zero padding does not create new information; it samples the same underlying DTFT on a finer grid. Increasing $N$ shrinks the bin spacing from $2\pi/M$ to $2\pi/N$, so the plot looks smoother because more points lie on the same DTFT curve. The record length $L$ sets the true frequency resolution (main-lobe width, ability to distinguish nearby tones); $N$ only controls the density of the DTFT samples.

Zeros should be appended at the tail, outside the true support, while preserving the original index positions. Padding in the middle changes the sequence.

For convolution, zero padding provides room so circular wrap-around does not contaminate the linear result. If $x[n]$ has length $N_x$ and $h[n]$ has length $N_h$, choose $N\ge N_x+N_h-1$ and pad both to length $N$. Then the $N$-point circular convolution equals the ordinary linear convolution.

---

Flashcards for this section are as follows:

- What is the linearity property of the DFT? ::@:: It is $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$.
- Why must sequences use the same DFT length in practical linearity calculations? ::@:: Because the DFT length fixes the frequency-bin spacing and the modulo-$N$ wrap-around interpretation, so different lengths describe different transform problems.
- What does zero padding change and what does it preserve? ::@:: It preserves the original nonzero sample values and their relative positions, but changes the transform length $N$, the bin spacing $2\pi/N$, and the amount of room available before circular wrap-around occurs.
- Why does zero padding sample the same DTFT without new information? ::@:: For length $L$ padded to $N$, $X_N[k]=X(e^{j2\pi k/N})$. Zero padding only changes which DTFT grid points are sampled.
- Why does zero padding make a spectrum look smoother without better resolution? ::@:: More grid points lie on the same DTFT curve. Resolution depends on $L$, not $N$.
- Where do zeros go when padding? ::@:: Append at the tail, outside the true support, preserving the original index positions.
- How do you compute linear convolution with DFTs? ::@:: Pad both sequences to $N\ge N_x+N_h-1$, then the circular result equals the linear convolution.

## principal value interval extraction

Its period-$N$ periodic summation is $x_p[n]=\sum_{r=-\infty}^{\infty}x[n-rN]$, so $x_p[n+N]=x_p[n]$. To recover the original record, multiply by the rectangular window $G_N[n]=u[n]-u[n-N]$: $x[n]=x_p[n]G_N[n]$. This is principal value interval extraction.

The alternative form $x[n]=x_p[n]u[n]-x_p[n-N]u[n-N]$ is the same thing, since $x_p[n-N]=x_p[n]$ by periodicity.

Circular shift follows directly: if the periodic extension is shifted by $m$, the extracted record is $x_c[n]=x_p[n-m]G_N[n]$. A circular shift is not an open-axis delay; it is a shift on a periodic sequence followed by principal-interval extraction.

---

Flashcards for this section are as follows:

- What is principal value interval extraction? ::@:: Taking a period-$N$ periodic extension and keeping one representative block, usually $0\le n\le N-1$.
- How do you extract the principal interval? ::@:: Multiply by $G_N[n]=u[n]-u[n-N]$: $x[n]=x_p[n]G_N[n]$.

## circular shift

Define the circularly shifted sequence by $x_c[n]=x[(n-m)_N]$, where $(\cdot)_N$ means modulo $N$. Its DFT is $X_c[k]=\sum_{n=0}^{N-1}x[(n-m)_N]e^{-j2\pi kn/N}$. Re-index with $r=(n-m)_N$ to get $X_c[k]=\sum_{r=0}^{N-1}x[r]e^{-j2\pi k(r+m)/N}=e^{-j2\pi km/N}X[k]$. A circular time shift produces a linear phase factor.

A circular shift differs from a linear delay: a linear delay moves a sequence along an open axis, while a circular shift moves samples around a closed loop of $N$ positions, wrapping any that leave one edge back to the other.

---

Flashcards for this section are as follows:

- What is a circular shift of a length-$N$ sequence? ::@:: It is the modulo-$N$ shift $x_c[n]=x[(n-m)_N]$, which moves samples by $m$ positions and wraps any samples that pass one edge back to the other side.
- If $x_c[n]=x[(n-m)_N]$, how do you derive the DFT of the shifted sequence? ::@:: Start from $X_c[k]=\sum_{n=0}^{N-1}x[(n-m)_N]e^{-j2\pi kn/N}$. <br/> Re-index with $r=(n-m)_N$. <br/> Then factor out the term $e^{-j2\pi km/N}$ and recognize the remaining sum as $X[k]$. <br/> So $X_c[k]=e^{-j2\pi km/N}X[k]=W_N^{mk}X[k]$.
- Why is the DFT shift law circular? ::@:: Because the transform assumes a periodic extension of length $N$, so the shifted record wraps modulo $N$.
- What is the difference between linear and circular shift? ::@:: Linear shift can extend support; circular shift wraps samples back into the record.
- What time-domain effect corresponds to circularly shifting DFT bins? ::@:: Multiplying the time-domain sequence by a complex exponential.

## circular convolution and its relation to linear convolution

For two length-$N$ sequences, circular convolution is $y[n]=(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$. Its DFT satisfies the product rule $Y[k]=X[k]H[k]$. Pointwise multiplication in time gives circular convolution in frequency with scaling: $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.

The index arithmetic is modulo $N$: $h[(n-m)_N]$ wraps around and re-enters from the other edge. This is convolution on a ring, whereas ordinary convolution is on an infinite line.

The matching conditions differ. Linear convolution: $m+(n-m)=n$ on an open line. Circular convolution: $m+(n-m)_N\equiv n\pmod N$, with the second index reduced modulo $N$.

The relation to principal value interval extraction: if $x[n]$ and $h[n]$ are supported on $0\le n\le N-1$, the $N$-point circular convolution is $y_c[n]=\sum_{r=-\infty}^{\infty}y_{\mathrm{lin}}[n-rN]$ for $0\le n\le N-1$, where $y_{\mathrm{lin}}$ is the ordinary linear convolution. So circular convolution is the periodic summation (aliasing) of the linear convolution, followed by principal-interval extraction. If $N\ge N_x+N_h-1$, the linear-convolution support fits inside one period, so only the $r=0$ term survives on the principal interval.

An explicit example: let $N=3$, $x[n]=[1,2,3]$, $h[n]=[4,5,6]$. Then $y_c[0]=1\cdot4+2\cdot6+3\cdot5=31$, $y_c[1]=1\cdot5+2\cdot4+3\cdot6=31$, $y_c[2]=1\cdot6+2\cdot5+3\cdot4=28$, so $y_c=[31,31,28]$. The linear convolution is $y_{\mathrm{lin}}=[4,13,28,27,18]$. Reducing modulo $3$ wraps the tail: $y_c[0]=4+27=31$, $y_c[1]=13+18=31$, $y_c[2]=28$.

Another example: $x[n]=[1,1,1]$, $h[n]=[1,1,1]$. Linear convolution is $[1,2,3,2,1]$; the length-$3$ circular convolution folds the tail and becomes $[3,3,3]$.

---

Flashcards for this section are as follows:

- What is the formula for circular convolution? ::@:: $(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$.
- What DFT rule corresponds to circular convolution? ::@:: $y[n]=x[n]\circledast h[n]$ gives $Y[k]=X[k]H[k]$.
- What happens when two sequences are multiplied pointwise in time? ::@:: The DFT gives circular convolution in frequency with scaling $1/N$: $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.
- Why is DFT multiplication not automatically ordinary convolution? ::@:: DFT multiplication produces circular convolution, which wraps contributions modulo $N$.
- What is the difference between linear and circular convolution? ::@:: Linear convolution uses an open index line and support can grow. Circular convolution reduces indices modulo $N$, so contributions wrap.
- How is circular convolution related to linear convolution? ::@:: The $N$-point circular convolution is the periodic summation (aliasing) of the linear convolution: $y_c[n]=\sum_{r}y_{\mathrm{lin}}[n-rN]$.
- How do you compute linear convolution with DFTs? ::@:: Pad both sequences to $N\ge N_x+N_h-1$, then the circular result matches the linear convolution.
