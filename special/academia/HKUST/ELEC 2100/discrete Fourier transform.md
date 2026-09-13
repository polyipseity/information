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

## periodic sequences and discrete-time Fourier series

For a sequence periodic with period $N$, the fundamental digital angular frequency is $\Omega_0=2\pi/N$. The DTFS synthesis formula is $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$.

The point of deriving the DTFT of a periodic sequence is to connect two descriptions: the finite DTFS coefficient list $\tilde X[k]$ and the line spectrum in continuous $\Omega$.

The notation: $\tilde x[n]$ is the period-$N$ sequence, $\tilde X[k]$ are its DTFS coefficients, $\Omega_0=2\pi/N$, and $X_{\mathrm{DTFT}}(e^{j\Omega})$ is the DTFT.

Now isolate one harmonic. Suppose $\tilde x_{k_0}[n]=\tilde X[k_0]e^{jk_0\Omega_0 n}$. Its DTFT is $X_{k_0}(e^{j\Omega})=\tilde X[k_0]\sum_{n=-\infty}^{\infty}e^{-j(\Omega-k_0\Omega_0)n}$.

This infinite sum must be interpreted distributionally. The symmetric partial sums $S_M(\alpha)=\sum_{n=-M}^{M}e^{-j\alpha n}$ have area $2\pi$ over $[-\pi,\pi]$. As $M\to\infty$, that area concentrates at $\alpha=2\pi m$, giving $\sum_{n=-\infty}^{\infty}e^{-j\alpha n}=2\pi\sum_{m=-\infty}^{\infty}\delta(\alpha-2\pi m)$.

Applying this with $\alpha=\Omega-k_0\Omega_0$ gives $X_{k_0}(e^{j\Omega})=2\pi\tilde X[k_0]\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$.

Summing all harmonics: $X_{\mathrm{DTFT}}(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$.

DTFS stores harmonic amplitudes directly as a finite list. DTFT describes periodic sequences by impulses in $\Omega$. DTFS is cleaner for periodic sequences.

---

Flashcards for this section are as follows:

- What is the fundamental digital angular frequency of a period-$N$ sequence? ::@:: $\Omega_0=2\pi/N$.
- What is the DTFS synthesis formula? ::@:: $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$.
- Why does a period-$N$ sequence need only $N$ DTFS coefficients? ::@:: Both the sequence and the frequency description repeat modulo $N$.
- Why is DTFS cleaner than DTFT for periodic sequences? ::@:: It stores harmonic amplitudes as a finite list, not as impulses in a continuous variable.
- How does one harmonic appear in the DTFT? ::@:: $\tilde X[k_0]e^{jk_0\Omega_0 n}$ becomes $2\pi\tilde X[k_0]\sum_m\delta(\Omega-k_0\Omega_0-2\pi m)$.
- Why does the exponential sum produce Dirac deltas with weight $2\pi$? ::@:: The symmetric partial sums have area $2\pi$ over $[-\pi,\pi]$, and as $M\to\infty$ that area concentrates at $\alpha=2\pi m$.
- What is the full DTFT of a periodic sequence? ::@:: $X_{\mathrm{DTFT}}(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_m\delta(\Omega-k\Omega_0-2\pi m)$.
- Why is DTFS closer to DFT than to DTFT? ::@:: Both use finite $k=0,1,\dots,N-1$ and work modulo $N$. DFT coefficients satisfy $X[k]=N\tilde X[k]$.

## orthogonality and DTFS coefficient derivation

The DTFS coefficient formula comes from orthogonality of discrete complex exponentials over one period. Define $S_{k,r}=\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}$.

If $k=r\pmod N$, every term equals $1$, so $S_{k,r}=N$. If $k\neq r\pmod N$, let $q=e^{j2\pi (k-r)/N}\neq1$. Then $S_{k,r}=\frac{1-q^N}{1-q}=0$ because $q^N=e^{j2\pi(k-r)}=1$.

Now derive the analysis formula. Start from $\tilde x[n]=\sum_{k=0}^{N-1}\tilde X[k]e^{j2\pi kn/N}$. Multiply by $e^{-j2\pi rn/N}$ and sum over $n$: orthogonality kills every $k\neq r$ term, the $k=r$ term contributes $N$, giving $N\tilde X[r]$. Dividing by $N$ yields $\tilde X[r]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi rn/N}$.

The factor $1/N$ is needed because the basis vectors are not unit-length: their inner product with themselves is $N$, not $1$. Geometrically, $\tilde X[r]$ is the normalized projection of the periodic sequence onto one discrete exponential basis vector.

---

Flashcards for this section are as follows:

- What orthogonality identity drives the DTFS derivation? ::@:: $\sum_{n=0}^{N-1}e^{j2\pi (k-r)n/N}=N$ when $k=r\pmod N$, $0$ otherwise.
- How do you derive the DTFS analysis formula? ::@:: Multiply $\tilde x[n]=\sum_k\tilde X[k]e^{j2\pi kn/N}$ by $e^{-j2\pi rn/N}$, sum over $n$, apply orthogonality ($k=r$ gives $N$), divide by $N$.
- What is the DTFS analysis formula? ::@:: $\tilde X[k]=\frac{1}{N}\sum_{n=0}^{N-1}\tilde x[n]e^{-j2\pi kn/N}$.
- Why does the DTFS forward formula contain $1/N$? ::@:: Because the orthogonality sum returns $N$, not $1$.

## normalization map between DTFS and DFT

The normalization map is straightforward once $X[k]=N\tilde X[k]$ is remembered. For circular convolution, $Y[k]=X[k]H[k]$ becomes $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.

For pointwise multiplication, $Y[k]=\frac{1}{N}(X\circledast H)[k]$ becomes $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$.

For Parseval, $\sum|x[n]|^2=\frac{1}{N}\sum|X[k]|^2$ becomes $\sum|x[n]|^2=N\sum|\tilde X[k]|^2$.

DFT coefficients are raw sums, so their formulas need compensating $1/N$ factors. DTFS coefficients are already averages, so the $1/N$ appears on opposite sides.

---

Flashcards for this section are as follows:

- How do you derive the DTFS circular-convolution rule? ::@:: Substitute $X=N\tilde X$, $H=N\tilde H$, $Y=N\tilde Y$ into $Y[k]=X[k]H[k]$ to get $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.
- How do you derive the DTFS multiplication rule? ::@:: Substitute into $Y[k]=\frac{1}{N}(X\circledast H)[k]$ to get $\tilde Y[k]=(\tilde X\circledast\tilde H)[k]$.
- How do you derive DTFS Parseval? ::@:: Replace $X[k]$ by $N\tilde X[k]$ in $\sum|x[n]|^2=\frac{1}{N}\sum|X[k]|^2$ to get $\sum|x[n]|^2=N\sum|\tilde X[k]|^2$.
- Why do DFT and DTFS have different normalization factors? ::@:: They place $1/N$ on opposite sides of the transform pair.

## periodicity, symmetry, and circular operations for DTFS

Time-domain periodicity: $\tilde x[n+N]=\tilde x[n]$. Frequency-domain periodicity: $\tilde X[k+N]=\tilde X[k]$. A delay by $n_0$ multiplies coefficients by $e^{-j2\pi kn_0/N}$, while modulation by $e^{j2\pi k_0 n/N}$ circularly shifts coefficients to $\tilde X[(k-k_0)_N]$.

For real sequences: $\tilde X[N-k]=\tilde X^*[k]$, with $k=0$ and (when $N$ even) $k=N/2$ as self-partner. Parseval: $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$.

Conjugation: $y[n]=\tilde x^*[n]$ gives $\tilde Y[k]=\tilde X^*[(-k)_N]$ (conjugation plus reversal). $y[n]=\tilde x^*[(-n)_N]$ gives $\tilde Y[k]=\tilde X^*[k]$ (reversal cancelled).

For periodic sequences, convolution is naturally circular: $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$ gives $\tilde Y[k]=N\tilde X[k]\tilde H[k]$. Pointwise multiplication in time gives circular convolution in frequency: $\widetilde{xh}[k]=(\tilde X\circledast\tilde H)[k]$.

---

Flashcards for this section are as follows:

- What are the periodicity rules? ::@:: $\tilde x[n+N]=\tilde x[n]$ and $\tilde X[k+N]=\tilde X[k]$.
- What happens with a delay of $n_0$ samples? ::@:: Coefficients multiply by $e^{-j2\pi kn_0/N}$.
- What happens with modulation by $e^{j2\pi k_0 n/N}$? ::@:: Coefficients shift circularly: $\tilde X[k]\to\tilde X[(k-k_0)_N]$.
- What conjugate-symmetry rule holds for real sequences? ::@:: $\tilde X[N-k]=\tilde X^*[k]$.
- What is DTFS Parseval? ::@:: $\sum_{n=0}^{N-1}|\tilde x[n]|^2=N\sum_{k=0}^{N-1}|\tilde X[k]|^2$.
- What rule connects circular convolution and DTFS coefficients? ::@:: $\tilde y[n]=\tilde x[n]\circledast\tilde h[n]$ gives $\tilde Y[k]=N\tilde X[k]\tilde H[k]$.
- Worked example: For period-$4$ constant $\tilde x[n]=1$, what are the DTFS coefficients? ::@:: Only $\tilde X[0]=1$; the rest vanish by phasor cancellation.

## linearity and zero padding

The DFT is linear: $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$. Both sequences must use the same transform length.

For a length-$L$ record zero-padded to length $N$, the $N$-point DFT is $X_N[k]=X(e^{j2\pi k/N})$. Zero padding samples the same DTFT on a finer grid. Increasing $N$ shrinks the bin spacing from $2\pi/M$ to $2\pi/N$, so the plot looks smoother. The record length $L$ sets the true frequency resolution; $N$ controls only the density of DTFT samples.

Zeros should be appended at the tail, outside the true support, preserving original index positions.

For convolution, zero padding prevents circular wrap-around. If $x[n]$ has length $N_x$ and $h[n]$ has length $N_h$, choose $N\ge N_x+N_h-1$. Then the $N$-point circular convolution equals the linear convolution.

---

Flashcards for this section are as follows:

- What is the linearity property of the DFT? ::@:: $\operatorname{DFT}\{ax_1[n]+bx_2[n]\}=aX_1[k]+bX_2[k]$.
- Why must sequences use the same DFT length? ::@:: Different lengths describe different transform problems.
- What does zero padding change? ::@:: It changes $N$ and bin spacing $2\pi/N$. The original nonzero values and their positions are preserved.
- Why does zero padding not improve resolution? ::@:: Resolution depends on $L$, not $N$. Zero padding only samples the same DTFT on a finer grid.
- Where do zeros go when padding? ::@:: At the tail, outside the true support.
- How do you compute linear convolution with DFTs? ::@:: Pad both to $N\ge N_x+N_h-1$, then circular equals linear.

## principal value interval extraction

Its period-$N$ periodic summation is $x_p[n]=\sum_{r=-\infty}^{\infty}x[n-rN]$. To recover the original record, multiply by the rectangular window $G_N[n]=u[n]-u[n-N]$: $x[n]=x_p[n]G_N[n]$.

Circular shift follows directly: if the periodic extension is shifted by $m$, the extracted record is $x_c[n]=x_p[n-m]G_N[n]$. A circular shift is a shift on a periodic sequence followed by principal-interval extraction.

---

Flashcards for this section are as follows:

- What is principal value interval extraction? ::@:: Taking a period-$N$ periodic extension and keeping one representative block, usually $0\le n\le N-1$.
- How do you extract the principal interval? ::@:: Multiply by $G_N[n]=u[n]-u[n-N]$: $x[n]=x_p[n]G_N[n]$.

Define the circularly shifted sequence by $x_c[n]=x[(n-m)_N]$, where $(\cdot)_N$ means modulo $N$. Its DFT is $X_c[k]=e^{-j2\pi km/N}X[k]$. A circular time shift produces a linear phase factor.

A circular shift differs from a linear delay: a linear delay moves a sequence along an open axis, while a circular shift wraps samples that leave one edge back to the other.

---

Flashcards for this section are as follows:

- What is a circular shift? ::@:: $x_c[n]=x[(n-m)_N]$, moving samples by $m$ positions and wrapping any that pass one edge.
- What is the DFT of a circularly shifted sequence? ::@:: $X_c[k]=e^{-j2\pi km/N}X[k]$.
- Why is the DFT shift law circular? ::@:: Because the transform assumes a periodic extension of length $N$.
- What is the difference between linear and circular shift? ::@:: Linear shift can extend support; circular shift wraps.

## circular convolution and its relation to linear convolution

For two length-$N$ sequences, circular convolution is $y[n]=(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$. Its DFT satisfies $Y[k]=X[k]H[k]$. Pointwise multiplication in time gives circular convolution in frequency: $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.

The index arithmetic is modulo $N$: $h[(n-m)_N]$ wraps around and re-enters from the other edge. This is convolution on a ring, whereas ordinary convolution is on an infinite line.

The relation to linear convolution: if $x[n]$ and $h[n]$ are supported on $0\le n\le N-1$, the $N$-point circular convolution is $y_c[n]=\sum_{r=-\infty}^{\infty}y_{\mathrm{lin}}[n-rN]$ for $0\le n\le N-1$. Circular convolution is the periodic summation (aliasing) of the linear convolution, followed by principal-interval extraction. If $N\ge N_x+N_h-1$, only the $r=0$ term survives.

An explicit example: let $N=3$, $x[n]=[1,2,3]$, $h[n]=[4,5,6]$. Then $y_c[0]=1\cdot4+2\cdot6+3\cdot5=31$, $y_c[1]=1\cdot5+2\cdot4+3\cdot6=31$, $y_c[2]=1\cdot6+2\cdot5+3\cdot4=28$, so $y_c=[31,31,28]$. The linear convolution is $y_{\mathrm{lin}}=[4,13,28,27,18]$. Reducing modulo $3$ wraps the tail: $y_c[0]=4+27=31$, $y_c[1]=13+18=31$, $y_c[2]=28$.

Another example: $x[n]=[1,1,1]$, $h[n]=[1,1,1]$. Linear convolution is $[1,2,3,2,1]$; the length-$3$ circular convolution folds the tail and becomes $[3,3,3]$.

---

Flashcards for this section are as follows:

- What is circular convolution? ::@:: $(x\circledast h)[n]=\sum_{m=0}^{N-1}x[m]h[(n-m)_N]$.
- What DFT rule corresponds to circular convolution? ::@:: $Y[k]=X[k]H[k]$.
- What happens with pointwise multiplication in time? ::@:: The DFT gives circular convolution in frequency: $\operatorname{DFT}\{x[n]h[n]\}=\frac{1}{N}(X\circledast H)[k]$.
- Why is DFT multiplication not ordinary convolution? ::@:: DFT multiplication produces circular convolution, which wraps modulo $N$.
- How is circular convolution related to linear convolution? ::@:: It is the periodic summation (aliasing) of the linear convolution: $y_c[n]=\sum_{r}y_{\mathrm{lin}}[n-rN]$.
- How do you compute linear convolution with DFTs? ::@:: Pad both to $N\ge N_x+N_h-1$, then circular equals linear.
