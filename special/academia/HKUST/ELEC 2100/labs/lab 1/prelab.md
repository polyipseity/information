---
aliases:
  - ELEC 2100 lab 1 prelab
  - HKUST ELEC 2100 lab 1 prelab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_1/prelab
  - language/in/English
---

# prelab

- HKUST ELEC 2100 lab 1
- parent: [lab 1](index.md)

---

For the surrounding theory, see [signal](../../signal.md) and [sampling theorem](../../sampling%20theorem.md).  The sections below collect the prelab ideas that are easiest to learn from direct signal, audio, and image manipulation.

## vectorized operations and signal displays

The signal and representation theory already lives in [signal § signal meaning and representation](../../signal.md#signal-meaning-and-representation) and [signal § time transformations and basic operations](../../signal.md#time-transformations-and-basic-operations).  The MATLAB side matters immediately.  A line ending with `;` suppresses command-window output, and the contrast between `*` and `.*` matters because sampled-signal formulas usually act pointwise across an array rather than as matrix products.

```matlab
t = 0:dt:T_end;
x = exp(-0.2*t) .* cos(20*pi*t);
plot(t, x)

n = -10:10;
xn = cos(pi*n/5);
stem(n, xn, 'filled')
```

The plotting tasks also force the continuous-time versus discrete-time distinction to become operational.  A densely sampled vector such as `t = 0:dt:T_end` is used to approximate a continuous-time waveform with `plot`, whereas a true sequence indexed by integers is better shown with `stem`.  So the graphical difference is not cosmetic: line plots suggest interpolation between nearby sample locations, while stem plots emphasize that only the indexed values are actually part of the discrete-time signal.

The cosine example therefore illustrates two linked ideas: period and sampling step together decide how smooth a plot looks, and the independent variable, sampled values, and display command must be kept conceptually separate.  In MATLAB terms, `t` or `n` is not decoration; it is the domain on which the samples are being interpreted, so a mismatch between the horizontal axis and the data vector changes the meaning of the plot rather than only its appearance.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `x = exp(-0.2*t) .* cos(20*pi*t)`, why is `.*` the natural operator instead of `*`? ::@:: Because the exponential and cosine are both being evaluated sample by sample on the same grid `t`, so the intended operation is pointwise multiplication rather than matrix multiplication.
- In the pair of MATLAB fragments `x = exp(-0.2*t) .* cos(20*pi*t)` and `xn = cos(pi*n/5)`, why does the distinction between `*` and `.*` matter so much in signal arrays? ::@:: Because sampled-signal expressions usually combine values at matching sample locations, whereas `*` would ask MATLAB for matrix multiplication with a different algebraic meaning and shape requirement.
- In the MATLAB fragment `t = 0:dt:T_end; x = exp(-0.2*t) .* cos(20*pi*t); plot(t, x)`, what roles do `t` and `x` play? ::@:: `t` is the sampled time grid and `x` is the waveform evaluated on that grid, so `plot(t, x)` draws the value of the signal against its intended time locations.
- When the prelab uses `plot(t, x)` for `t = 0:dt:T_end` but `stem(n, xn, 'filled')` for `n = -10:10`, what conceptual difference between `plot` and `stem` is being emphasized? ::@:: `plot` is being used for a densely sampled curve that stands in for a continuous-time waveform, whereas `stem` is being used to emphasize that only the discrete-indexed sequence values actually belong to the signal.
- In the MATLAB fragment `n = -10:10; xn = cos(pi*n/5); stem(n, xn, 'filled')`, what part of the setup tells the reader that the signal is being treated as discrete time? ::@:: The horizontal variable `n` is an integer index set and `stem` marks isolated samples rather than connecting them into a continuous-looking curve.
- When comparing `plot(t, x)` with `stem(n, xn, 'filled')`, why must the display choice match the signal model? ::@:: Because the graph should preserve whether the signal is being interpreted as a densely sampled continuous-time waveform or as a genuinely discrete-time sequence, rather than hiding that distinction.

## multiple views of a complex signal

The corresponding theory already lives in [signal § complex numbers and orthogonal decompositions](../../signal.md#complex-numbers-and-orthogonal-decompositions).  One complex waveform usually needs several coordinated views.  Real part, imaginary part, magnitude, and phase answer different questions, so no single plot is enough.

```matlab
x = exp(1j*20*pi*t);
plot(t, real(x))
plot(t, imag(x))
plot(t, abs(x))
plot(t, angle(x))
```

This matters because Fourier and frequency-response calculations repeatedly produce complex quantities whose physical meaning is not visible from one plot alone.  The same array has to be decomposed into multiple informative projections.

---

Flashcards for this section are as follows:

- For the MATLAB fragment `x = exp(1j*20*pi*t)`, what four MATLAB calls split the same complex waveform into the four standard readable views? ::@:: `real(x)`, `imag(x)`, `abs(x)`, and `angle(x)`.
- In the MATLAB fragment `x = exp(1j*20*pi*t)` together with the plots `real(x)`, `imag(x)`, `abs(x)`, and `angle(x)`, which calls show Cartesian information and which calls show polar information? ::@:: `real(x)` and `imag(x)` show the Cartesian components, while `abs(x)` and `angle(x)` show the polar magnitude and phase.
- When the same MATLAB array `x` is displayed with `real(x)`, `imag(x)`, `abs(x)`, and `angle(x)`, why are those four views complementary rather than redundant? ::@:: Because they answer different questions about the same complex samples: Cartesian components describe horizontal and vertical parts, while magnitude and phase describe size and angular position.
- In the MATLAB fragment `x = exp(1j*20*pi*t)`, what do `abs(x)` and `angle(x)` reveal that `real(x)` and `imag(x)` do not reveal directly? ::@:: `abs(x)` gives the sample-by-sample magnitude independent of direction, and `angle(x)` gives the phase angle, so together they show the polar form of the same complex waveform.

## audio files as sampled signals

The corresponding theory already lives in [sampling theorem § sampling model and notation](../../sampling%20theorem.md#sampling-model-and-notation), [sampling theorem § choosing the sampling frequency](../../sampling%20theorem.md#choosing-the-sampling-frequency), and [sampling theorem § aliasing and anti-aliasing](../../sampling%20theorem.md#aliasing-and-anti-aliasing).  An audio file should be read as a sequence of samples together with a declared sampling rate.  Reading the file therefore produces both the sample array and the sampling frequency $f_s$, so the sampling interval is $T_s = 1/f_s$ and the duration is the number of samples divided by $f_s$.

```matlab
[x, fs] = audioread('song1.wav');
Ts = 1/fs;
duration = length(x)/fs;
sound(x, fs)
sound(x, 2*fs)
```

The experiments distinguish two related but different ideas.  If playback is performed at a different declared sampling rate, the same samples are heard with a changed time scale and pitch impression.  If samples are discarded so the record becomes sparser, then the discrete-time representation itself loses temporal detail and the reconstructed sound becomes rougher or less faithful unless careful antialiasing logic is used first.  The prelab does not turn that into a full theorem proof, but it makes the sampling-rate idea concrete enough to hear.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `[x, fs] = audioread('song1.wav'); Ts = 1/fs; duration = length(x)/fs;`, why is the file metadata really sampling information rather than mere bookkeeping? ::@:: Because the sample array `x` and the sampling frequency `fs` together determine the sampling interval, playback duration, and time interpretation of the sound.
- In the MATLAB fragment `[x, fs] = audioread('song1.wav'); Ts = 1/fs;`, why does `Ts = 1/fs` represent the sampling interval? ::@:: Because `fs` is the number of samples per second, so taking its reciprocal gives the time length represented by one stored sample.
- In the MATLAB fragment `[x, fs] = audioread('song1.wav'); duration = length(x)/fs;`, why does the specific quotient `length(x)/fs` produce the duration? ::@:: Because `length(x)` counts stored samples and `fs` tells how many samples represent one second, so their ratio gives the playback time in seconds.
- In the MATLAB pair `sound(x, fs)` and `sound(x, 2*fs)`, what changes conceptually and what stays fixed? ::@:: The stored sample values `x` stay fixed, but the declared playback rate changes, so the same discrete record is interpreted on a different time scale and pitch impression.
- When comparing the MATLAB operations `sound(x, 2*fs)` and sample discarding such as `x = x(1:M:end, :)`, what conceptual difference matters? ::@:: Changing the declared playback rate reinterprets the same stored samples in time, whereas discarding samples changes the discrete-time representation itself and therefore reduces temporal detail.

## images as multidimensional signals

The same signal viewpoint already lives in [signal § signal meaning and representation](../../signal.md#signal-meaning-and-representation).  The same viewpoint extends naturally to color images.  A color image is modeled as a three-dimensional array: row index, column index, and color channel.  So commands such as `size`, region extraction, and channel selection are not just file-manipulation conveniences; they are ways of reasoning about a sampled multidimensional signal.

```matlab
img = imread('image1.jpg');
sz = size(img);
pixel = img(r, c, :);
patch = img(r1:r2, c1:c2, :);

red = img;
red(:,:,2:3) = 0;
```

Cropping teaches support restriction in array form: choose row and column ranges and keep only that rectangular subarray.  Inspecting a pixel with a datatip or direct indexing reveals that one pixel is an RGB vector rather than one scalar intensity.  Isolating the red channel then shows that color images can be decomposed into component signals in exactly the same spirit as decomposing a complex waveform into real and imaginary parts.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `img = imread('image1.jpg'); pixel = img(r, c, :); patch = img(r1:r2, c1:c2, :)`, how should the color image be modeled mathematically? ::@:: It should be modeled as a sampled multidimensional signal whose indices are row, column, and color channel.
- In the MATLAB fragment `patch = img(r1:r2, c1:c2, :)`, what does this particular row-column-channel cropping operation correspond to in signal terms? ::@:: It corresponds to restricting the sampled image signal to the rectangular support determined by the chosen row and column ranges.
- In MATLAB, what does `img(r1:r2, c1:c2, :)` mean? ::@:: It selects all color channels on the rectangular block whose row indices run from `r1` to `r2` and whose column indices run from `c1` to `c2`.
- In the MATLAB fragment `pixel = img(r, c, :)`, why is the result conceptually a vector rather than one intensity value? ::@:: Because the third index `:` keeps all color channels, so the selected pixel contains the red, green, and blue entries at that location.
- In the MATLAB fragment `pixel = img(r, c, :)`, why is one RGB pixel not just a scalar? ::@:: Because the chosen location still has three channel values attached to it, so one pixel is a red-green-blue vector rather than one number.
- In the MATLAB fragment `red = img; red(:,:,2:3) = 0;`, why is red-channel isolation conceptually parallel to other decompositions in the course? ::@:: Because the image is being decomposed into component signals by zeroing selected channels, just as other course examples separate complex signals into real and imaginary parts or other multi-component representations.
