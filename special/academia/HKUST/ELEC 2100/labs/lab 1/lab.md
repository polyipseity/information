---
aliases:
  - ELEC 2100 lab 1 assignment
  - ELEC 2100 lab 1 lab
  - HKUST ELEC 2100 lab 1 assignment
  - HKUST ELEC 2100 lab 1 lab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_1/lab
  - language/in/English
---

# lab

- HKUST ELEC 2100 lab 1
- parent: [lab 1](index.md)

---

For the broader signal and sampling theory, see [signal](../../signal.md) and [sampling theorem](../../sampling%20theorem.md).  The waveform, audio, and image cases below focus on the specific ideas that are easiest to see in Lab 1 itself.

## parameter-dependent complex signals

The underlying signal ideas already live in [signal § periodicity, energy, and power](../../signal.md#periodicity-energy-and-power) and [signal § complex numbers and orthogonal decompositions](../../signal.md#complex-numbers-and-orthogonal-decompositions).  Here the important twist is that digits such as $A$ and $B$ can control the signal parameters, the meaningful plotting interval, or both.  A complex waveform is therefore not fully understood until the parameter-dependent period and sampling grid have been identified.

```matlab
freq = f(A, B);
t_idx = t0:dt:t1;
x = 3 .* exp(-2j*pi*freq*t_idx);

plot(t_idx, real(x))
plot(t_idx, imag(x))
plot(t_idx, abs(x))
plot(t_idx, angle(x))
```

Once those parameter-dependent choices are fixed, the real part, imaginary part, magnitude, and phase become coordinated views of one signal rather than unrelated plots.  Every later interpretation therefore depends on the original symbolic specification.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `freq = f(A, B); t_idx = t0:dt:t1; x = 3 .* exp(-2j*pi*freq*t_idx);`, why do parameter digits such as $A$ and $B$ matter? ::@:: Because they determine quantities such as the oscillation frequency and therefore affect the sampled waveform and the meaningful plotting interval rather than merely renaming a fixed example. <!--SR:!2026-05-18,16,290!2026-05-17,15,290-->
- In the MATLAB fragment `freq = f(A, B); t_idx = t0:dt:t1; x = 3 .* exp(-2j*pi*freq*t_idx);`, which quantities in that setup must be settled before any plot is meaningful? ::@:: The parameter-controlled frequency and the sampled time grid must be settled first, because they determine how the complex exponential is sampled and interpreted. <!--SR:!2026-05-17,15,290!2026-05-16,14,290-->
- In the MATLAB fragment `x = 3 .* exp(-2j*pi*freq*t_idx)`, why is `exp(-2j*pi*freq*t_idx)` a natural form for the complex waveform? ::@:: Because it keeps the oscillation frequency and the complex phase rotation in one expression, so real part, imaginary part, magnitude, and phase can all be read from the same sampled array. <!--SR:!2026-05-16,14,290!2026-05-16,14,290-->
- After the MATLAB code plots `real(x)`, `imag(x)`, `abs(x)`, and `angle(x)` for the same array `x`, why must those four views be read together? ::@:: Because they are coordinated descriptions of the same parameter-dependent complex waveform, so none of the plots alone tells the whole story about the sampled signal. <!--SR:!2026-05-18,16,290!2026-05-18,16,290-->

## sparse sampling in audio signals

The sampling ideas already live in [sampling theorem § sampling model and notation](../../sampling%20theorem.md#sampling-model-and-notation), [sampling theorem § choosing the sampling frequency](../../sampling%20theorem.md#choosing-the-sampling-frequency), and [sampling theorem § aliasing and anti-aliasing](../../sampling%20theorem.md#aliasing-and-anti-aliasing).  The local case here combines ordinary metadata reading with a deliberately sparse retained sample set.

```matlab
[x, fs] = audioread('song1a.mp4');
info = audioinfo('song1a.mp4');
player = audioplayer(x, fs);
playblocking(player)

x_sparse = x(1:M:end, :);
```

Once the retained sample count becomes much smaller, the change is not only numerical.  The discrete-time representation carries less temporal detail, so the audible result can become rougher or less faithful.  Metadata such as duration and sampling frequency therefore remain conceptually tied to perceptual interpretation rather than to file bookkeeping alone.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `[x, fs] = audioread('song1a.mp4'); info = audioinfo('song1a.mp4'); x_sparse = x(1:M:end, :);`, what does sparse sampling add beyond ordinary audio metadata reading? ::@:: It connects file metadata such as sampling frequency and duration to the perceptual effect of representing the same sound with a much sparser retained sample set. <!--SR:!2026-05-18,16,290!2026-05-17,15,290-->
- In the MATLAB fragment `[x, fs] = audioread('song1a.mp4')`, why is reading both `x` and `fs` essential before any playback or downsampling interpretation? ::@:: Because `x` contains the stored samples while `fs` tells how those samples map to time, so both are needed to reason about duration, playback, and sparse retention. <!--SR:!2026-05-16,14,290!2026-05-17,15,290-->
- In the MATLAB fragment `x_sparse = x(1:M:end, :)`, how is the audio array `x` being re-indexed on the left-hand side of that assignment? ::@:: The pattern `1:M:end` keeps one out of every `M` time samples, while `:` keeps every channel, so the operation sparsifies the time axis without discarding stereo or multichannel structure. <!--SR:!2026-05-18,16,290!2026-05-18,16,290-->
- In the lab's MATLAB setting, why is sparse retention in sampled audio a signal-processing question rather than only a storage question? ::@:: Because reducing the retained time samples changes how faithfully the waveform is represented and therefore changes the audible signal quality, not just the amount of stored data. <!--SR:!2026-05-16,14,290!2026-05-17,15,290-->

## image regions and color channels

The general signal viewpoint already lives in [signal § signal meaning and representation](../../signal.md#signal-meaning-and-representation).  The local content here is the geometric indexing procedure: partition the image into twelve regions, use a parameter-dependent rule to choose one region, and convert that rule into the correct row and column index ranges.

```matlab
img = imread('image1a.jpg');
roi = img(r1:r2, c1:c2, :);

red = roi;
red(:,:,2:3) = 0;
imshow(red)
```

Once the region is chosen, direct data inspection becomes meaningful: identify total pixel count and bit depth, inspect RGB values at a chosen location, and isolate the red channel.  The image is therefore treated as structured sampled data rather than as a picture that is only meant to be displayed.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `roi = img(r1:r2, c1:c2, :)`, what must a geometric rule become before the image region can be extracted correctly? ::@:: It must become the correct row and column index ranges on the image array, because those ranges specify which sampled pixels belong to the chosen region. <!--SR:!2026-05-17,15,290!2026-05-16,14,290-->
- In the MATLAB fragment `roi = img(r1:r2, c1:c2, :)`, why are the row limits `r1:r2` and column limits `c1:c2` part of the mathematics rather than just coding syntax? ::@:: Because they specify the actual support of the chosen image region, so changing them changes which sampled data belong to the extracted patch. <!--SR:!2026-05-18,16,290!2026-05-16,14,290-->
- In MATLAB, why does `red(:,:,2:3) = 0` isolate the red component? ::@:: Because the second and third slices are the green and blue channels, so zeroing them leaves only the first-channel red contribution visible. <!--SR:!2026-05-16,14,290!2026-05-17,15,290-->
- Once the MATLAB code has formed `roi = img(r1:r2, c1:c2, :)` and then `red(:,:,2:3) = 0`, why does region indexing naturally lead to RGB inspection and red-channel extraction? ::@:: Because once the image is treated as sampled array data on a chosen support, channel values can be measured and separated directly instead of being treated as undifferentiated picture content. <!--SR:!2026-05-17,15,290!2026-05-18,16,290-->
