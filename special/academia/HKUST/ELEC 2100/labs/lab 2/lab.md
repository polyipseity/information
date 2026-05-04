---
aliases:
  - ELEC 2100 lab 2 assignment
  - ELEC 2100 lab 2 lab
  - HKUST ELEC 2100 lab 2 assignment
  - HKUST ELEC 2100 lab 2 lab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_2/lab
  - language/in/English
---

# lab

- HKUST ELEC 2100 lab 2
- parent: [lab 2](index.md)

---

For the shared convolution and LTI-system theory, see [convolution](../../convolution.md), [discrete-time LTI system](../../discrete-time%20LTI%20system.md), and [continuous-time LTI system](../../continuous-time%20LTI%20system.md).  The sequence, audio, and image examples below show the parts that are clearest in Lab 2 itself.

## sparse impulses and shifted rectangles

The general interconnection theory lives in [convolution § algebraic properties and system interconnections](../../convolution.md#algebraic-properties-and-system-interconnections) and [convolution § discrete-time properties and support range](../../convolution.md#discrete-time-properties-and-support-range).  Consider the specific pair $h_1[n] = \delta[n-1] + \delta[n-4]$ and $h_2[n] = u[n-A-2] - u[n-A-6]$.  Because $h_1[n]$ is the sum of two impulses, the overall impulse response can already be read structurally as $h[n] = h_1[n] * h_2[n] = h_2[n-1] + h_2[n-4]$.

```matlab
h1 = [0 1 0 0 1];
h = conv(h2, h1);
y = conv(h, x);
stem(0:length(h)-1, h, 'filled')
```

The cascade is therefore the superposition of two shifted copies of the same finite rectangle.  Sparse impulse locations determine support and overlap geometry before any numeric computation is performed.

---

Flashcards for this section are as follows:

- In the worked case $h_1[n] = \delta[n-1] + \delta[n-4]$ and $h_2[n] = u[n-A-2] - u[n-A-6]$, why can the overall impulse response be predicted even before the MATLAB line `h = conv(h2, h1)` is executed? ::@:: Because each impulse in `h_1[n]` simply creates a shifted copy of `h_2[n]`, so the convolution can already be read structurally as the sum of two shifted rectangles. <!--SR:!2026-05-11,15,290!2026-05-11,15,290-->
- In the MATLAB fragment `h1 = [0 1 0 0 1]`, why is a mostly zero vector a natural encoding of sparse impulses? ::@:: Because the zero entries mark the absence of impulses and the nonzero entries directly mark the impulse locations and gains, making the support geometry visible before any convolution is run. <!--SR:!2026-05-12,16,290!2026-05-10,14,290-->
- In the MATLAB fragment `h = conv(h2, h1); y = conv(h, x);`, why is it useful to compute the intermediate impulse response `h` first? ::@:: Because the cascade can be reduced to one equivalent impulse response before being applied to the input, so the system structure is understood before the final output is generated. <!--SR:!2026-05-11,15,290!2026-05-12,16,290-->
- In this Lab 2 sequence example, what does the sparse-impulse pattern determine before any numeric computation is performed? ::@:: It determines how many shifted copies of the rectangle appear and where they overlap, so the support geometry of the final impulse response is understood before numerical evaluation. <!--SR:!2026-05-11,15,290!2026-05-11,15,290-->

## direct-path and echo-path models

The delay-kernel theory lives in [convolution § time shift and special kernels](../../convolution.md#time-shift-and-special-kernels) and [continuous-time LTI system § impulse response and step response](../../continuous-time%20LTI%20system.md#impulse-response-and-step-response).  Consider the echo model $h(t) = \delta(t) + 0.7\,\delta(t-0.18)$.  A direct path plus a delayed attenuated path is already a complete system interpretation.

```matlab
n_delay = round(0.18 * fs);
h = [1 zeros(1, n_delay-1) 0.7];
y = conv(x, h);
sound(y, fs)
```

Once the $0.18$-second delay is converted into a sample offset, the sampled output preserves that structure: it is the dry signal plus a delayed copy scaled by $0.7$.  The important idea is continuity of meaning across continuous-time and sampled descriptions.

---

Flashcards for this section are as follows:

- In the worked case $h(t) = \delta(t) + 0.7\,\delta(t-0.18)$ and the MATLAB realization `h = [1 zeros(1, n_delay-1) 0.7]`, what remains after the delay is converted into samples? ::@:: The sampled system is still the dry signal plus one delayed copy scaled by $0.7$, now encoded as a finite impulse-response vector. <!--SR:!2026-05-12,16,290!2026-05-12,16,290-->
- In the MATLAB fragment `n_delay = round(0.18 * fs); h = [1 zeros(1, n_delay-1) 0.7];`, what do the first entry, the zero block, and the last entry each mean in that echo model? ::@:: The first entry is the direct path gain, the zeros encode the elapsed sample delay, and the last entry is the delayed path gain. <!--SR:!2026-05-10,14,290!2026-05-11,15,290-->
- In the MATLAB realization `[1 zeros(1, n_delay-1) 0.7]`, why does that vector capture the echo structure so well? ::@:: Because its first nonzero entry stands for the direct path, its later nonzero entry stands for the delayed attenuated path, and the zeros in between encode the sample delay separating the two paths. <!--SR:!2026-05-12,16,290!2026-05-11,15,290-->
- What physical system is the echo model $h(t) = \delta(t) + 0.7\,\delta(t-0.18)$ and its sampled MATLAB vector meant to represent? ::@:: It represents a two-path system with one direct branch and one delayed attenuated branch, and the sampled vector is meant to preserve exactly that interpretation. <!--SR:!2026-05-10,14,290!2026-05-12,16,290-->

## composite masks in image filtering

The broad convolution viewpoint still belongs mainly to [convolution § physical interpretation of convolution](../../convolution.md#physical-interpretation-of-convolution).  The important content here is not the existence of 2D convolution itself, but the way small kernels can be read together as one composite mask.  The sign pattern and weight distribution already suggest whether the filter behaves more like averaging, differencing, or local contrast emphasis.

```matlab
y = convn(double(img), H, 'same');
imshow(uint8(y))
```

The visible result is therefore a consequence of the mask structure rather than an isolated display artifact.

---

Flashcards for this section are as follows:

- In the MATLAB fragment `y = convn(double(img), H, 'same'); imshow(uint8(y))`, what new interpretive habit does the image worked case emphasize? ::@:: It emphasizes reading the kernel `H` as a meaningful composite mask first and then checking whether the displayed image effect matches the prediction from that mask structure. <!--SR:!2026-05-10,14,290!2026-05-12,16,290-->
- In the MATLAB fragment `convn(double(img), H, 'same')`, why is `'same'` a natural choice for the image part of the lab? ::@:: Because the filtered array has to remain on the same image grid as the original if the visual effect is going to be compared directly pixel by pixel. <!--SR:!2026-05-10,14,290!2026-05-10,14,290-->
- In the MATLAB fragment `y = convn(double(img), H, 'same'); imshow(uint8(y))`, why are both `double(img)` before filtering and `uint8(y)` before display used? ::@:: `double` lets the convolution run on numeric values without image-type clipping during computation, and `uint8` converts the result back to a standard image type for display. <!--SR:!2026-05-10,14,290!2026-05-12,16,290-->
- Before the MATLAB code filters the image with `H`, what can the sign pattern and weight distribution of that composite mask already tell you? ::@:: They can already suggest whether the filter should behave more like averaging, differencing, or local contrast emphasis, so the visible effect should not be a surprise. <!--SR:!2026-05-11,15,290!2026-05-11,15,290-->
