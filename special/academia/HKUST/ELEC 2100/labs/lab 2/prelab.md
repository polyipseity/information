---
aliases:
  - ELEC 2100 lab 2 prelab
  - HKUST ELEC 2100 lab 2 prelab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_2/prelab
  - language/in/English
---

# prelab

- HKUST ELEC 2100 lab 2
- parent: [lab 2](index.md)

---

For the shared convolution and system theory, see [convolution](../../convolution.md), [discrete-time LTI system](../../discrete-time%20LTI%20system.md), and [continuous-time LTI system](../../continuous-time%20LTI%20system.md).  The sections below focus on details that are easy to miss when moving from formulas to indexed outputs and sampled data.

## convolution outputs need index ranges

For the theory of support and convolution arithmetic, see [convolution § discrete-time properties and support range](../../convolution.md#discrete-time-properties-and-support-range), [convolution § computing discrete convolution](../../convolution.md#computing-discrete-convolution), and [convolution § graphical convolution and overlap geometry](../../convolution.md#graphical-convolution-and-overlap-geometry).  The important fact here is that `conv` gives sample values only; the index vector still has to be built and checked before the output can be interpreted correctly.  Support bookkeeping is therefore part of the mathematical answer rather than presentation trivia.

If $x[n]$ is supported on `nx` and $h[n]$ is supported on `nh`, then the MATLAB line `ny = nx(1) + nh(1) : nx(end) + nh(end)` is doing the same support arithmetic as the convolution theory: first output index equals first input index plus first kernel index, and last output index equals last input index plus last kernel index.

```matlab
y = conv(x, h);
ny = nx(1) + nh(1) : nx(end) + nh(end);
stem(ny, y, 'filled')
```

---

Flashcards for this section are as follows:

- In the MATLAB fragment `y = conv(x, h); ny = nx(1) + nh(1) : nx(end) + nh(end);`, why is `conv` by itself not enough to describe the output signal? ::@:: Because `conv` gives only the output sample values, while `ny` is still needed to identify the correct sample indices and support range of the result. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- After the MATLAB line `y = conv(x, h)`, what additional MATLAB object has to be built if the input signals were labeled by explicit index vectors `nx` and `nh`? ::@:: The output index vector must be built so the convolution result can be plotted and interpreted on the correct support rather than against a misleading horizontal axis. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB fragment `ny = nx(1) + nh(1) : nx(end) + nh(end)`, what do the first and last entries of the constructed index vector `ny` represent? ::@:: They represent the first and last sample indices on which the convolution output can be nonzero, obtained by adding the endpoint indices of the two input supports. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## delays become sample offsets

For delay kernels, echo modeling, and the impulse-response viewpoint, see [convolution § time shift and special kernels](../../convolution.md#time-shift-and-special-kernels), [continuous-time LTI system § impulse response and step response](../../continuous-time%20LTI%20system.md#impulse-response-and-step-response), and [discrete-time LTI system § discrete-time impulse response](../../discrete-time%20LTI%20system.md#discrete-time-impulse-response).  A conceptual delay parameter becomes useful only after it has been turned into the sample-domain offset required by the audio representation.  That conversion is the bridge between the model and the sampled signal.

The MATLAB line `delay = round(tau * fs)` is the key bridge.  Here `tau` is a physical delay in seconds and `fs` is samples per second, so their product is the number of samples needed to encode that delay in the stored sequence.

```matlab
delay = round(tau * fs);
y = [zeros(1, delay) x];
z = [x zeros(1, delay)] + alpha*y;
```

---

Flashcards for this section are as follows:

- In the MATLAB fragment `delay = round(tau * fs); y = [zeros(1, delay) x];`, why must the physical delay parameter be converted into a sample offset first? ::@:: Because the array model of the sampled signal can only implement the delay after the time shift has been expressed as an integer number of sample positions. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB fragment `delay = round(tau * fs)`, why is the multiplication by `fs` the correct way to convert the delay? ::@:: Because `fs` converts seconds into samples, so multiplying the physical delay by samples-per-second yields the discrete-time offset needed by the array model. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB fragment `[zeros(1, delay) x]`, why does the prelab prepend zeros before the original samples? ::@:: Because a delayed copy in discrete time is formed by shifting the sequence to the right, and the newly created early sample positions must be filled with zeros. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB fragment `z = [x zeros(1, delay)] + alpha*y`, what role does the factor `alpha` play in that summed output model? ::@:: It controls the gain of the delayed branch relative to the original branch, so it sets how strong the echo contribution is in the summed output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## image filtering depends on output size and storage type

The image exercise extends the same convolution viewpoint to two spatial indices.  The general interpretation still belongs mainly to [convolution § physical interpretation of convolution](../../convolution.md#physical-interpretation-of-convolution).  Use size-preserving two-dimensional convolution when direct comparison is required, and remember that the filtered array may need conversion back to an ordinary image storage type before display.  Those details are easy to dismiss as housekeeping, but they directly affect whether the visual comparison is trustworthy.

The MATLAB snippets also encode two different averaging habits.  `h1 = ones(1, n)/n` is a one-dimensional averaging kernel, so `conv2(h1, h1, img, 'same')` applies it separably in the two spatial directions.  By contrast, `h2 = ones(n, n)/n^2` is already the full two-dimensional box mask.

```matlab
h1 = ones(1, n)/n;
h2 = ones(n, n)/n^2;

y_sep = conv2(h1, h1, img, 'same');
y_box = conv2(img, h2, 'same');
y_box = uint8(y_box);
```

---

Flashcards for this section are as follows:

- In the MATLAB fragment `y_sep = conv2(h1, h1, img, 'same'); y_box = conv2(img, h2, 'same'); y_box = uint8(y_box);`, why are output size and storage type part of the filtering result itself? ::@:: Because the `'same'` option preserves alignment with the original image size and the final type conversion affects how the filtered array can be displayed and compared visually. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB calls `conv2(..., 'same')`, why does the prelab insist on `'same'` rather than leaving the convolution output at full size? ::@:: Because the filtered image must stay aligned with the original image grid when the goal is a direct before-and-after visual comparison. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- In the MATLAB fragments `h1 = ones(1, n)/n` and `h2 = ones(n, n)/n^2`, what is the conceptual difference between those two averaging kernels? ::@:: `h1` is a one-dimensional averaging kernel used direction by direction, while `h2` is the full two-dimensional box-averaging mask already assembled as one array. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the MATLAB code convert the filtered array with `uint8(y_box)` before display? ::@:: Because convolution often produces a floating-point array, while ordinary image display and storage usually expect standard image-valued integer data. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
