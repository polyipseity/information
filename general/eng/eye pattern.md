---
aliases:
  - eye diagram
  - eye diagrams
  - eye pattern
  - eye patterns
tags:
  - flashcard/active/general/eng/eye_pattern
  - language/in/English
---

# eye pattern

- Not to be confused with {@{[Optical illusion](optical%20illusion.md)}@}. <!--SR:!2026-09-08,282,330-->

> {@{![Graphical eye pattern showing an example of two power levels in an [OOK](on-off%20keying.md) modulation scheme.](../../archives/Wikimedia%20Commons/On-off%20keying%20eye%20diagram.svg)}@}
>
> {@{Graphical eye pattern}@} showing an example of {@{two power levels in an [OOK](on-off%20keying.md) modulation scheme}@}. {@{Constant binary 1 and 0 levels}@} are shown, as well as {@{transitions from 0 to 1, 1 to 0, 0 to 1 to 0, and 1 to 0 to 1}@}. <!--SR:!2026-09-17,290,330!2026-09-02,277,330!2026-09-10,284,330!2026-07-23,246,330!2026-07-17,241,330-->

In {@{[telecommunications](telecommunications.md)}@}, {@{an __eye pattern__, also known as an __eye diagram__}@}, is {@{an [oscilloscope](oscilloscope.md) display}@} in which {@{a [digital signal](digital%20signal.md) from a receiver is repetitively sampled and applied to the vertical input \(_y-axis_\)}@}, while {@{the data rate is used to trigger the horizontal sweep \(_x-axis_\)}@}. It is so called because, for {@{several types of coding}@}, the pattern looks like {@{a series of eyes between a pair of rails}@}. It is {@{a tool for the evaluation}@} of {@{the combined effects of channel noise, dispersion and [intersymbol interference](intersymbol%20interference.md)}@} on {@{the performance of a baseband pulse-transmission system}@}. The technique was first used with {@{the [WWII](WWII.md) [SIGSALY](SIGSALY.md) secure speech transmission system}@}. <!--SR:!2026-09-01,276,330!2026-08-24,271,330!2026-08-26,272,330!2026-08-21,266,330!2026-08-09,259,330!2026-07-20,243,330!2026-09-15,288,330!2026-07-30,251,330!2026-09-22,294,330!2026-08-19,267,330!2026-08-30,276,330-->

From {@{a mathematical perspective}@}, an eye pattern is a visualization of {@{the [probability density function](probability%20density%20function.md) \(PDF\) of the signal}@}, {@{[modulo](modular%20arithmetic.md) the [unit interval](unit%20interval%20(data%20transmission).md) \(UI\)}@}. In other words, it shows the probability of {@{the signal being at each possible voltage across the duration of the UI}@}. Typically {@{a [color ramp](false%20color.md#pseudocolor) is applied to the PDF}@} in order to {@{make small brightness differences easier to visualize}@}. <!--SR:!2026-08-25,272,330!2026-08-03,255,330!2026-09-10,284,330!2026-07-22,245,330!2026-08-18,266,330!2026-08-22,267,330-->

{@{Several [system](system.md) performance measurements}@} can be derived by {@{analyzing the display}@}. If the signals are {@{too long, too short, poorly synchronized with the system clock}@}, {@{too high, too low, too [noisy](noise%20(electronics).md)}@}, or {@{too slow to change, or have too much undershoot or [overshoot](overshoot%20(signal).md)}@}, this can be {@{observed from the eye diagram}@}. {@{An open eye pattern}@} corresponds to {@{minimal signal [distortion](distortion.md)}@}. {@{Distortion of the signal [waveform](waveform.md)}@} due to {@{[intersymbol interference](intersymbol%20interference.md) and noise}@} appears as {@{closure of the eye pattern}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-07-21,244,330!2026-07-25,247,330!2026-08-15,263,330!2026-08-30,276,330!2026-07-15,239,330!2026-08-10,259,330!2026-07-26,248,330!2026-08-25,272,330!2026-07-09,234,330!2026-09-01,276,330!2026-07-08,233,330-->

## calculation

### source data

{@{The first step of computing an eye pattern}@} is normally to {@{obtain the waveform being analyzed in a quantized form}@}. This may be done by {@{measuring an actual electrical system}@} with {@{an oscilloscope of sufficient bandwidth}@}, or by creating {@{synthetic data with a [circuit simulator](circuit%20simulator.md)}@} in order to {@{evaluate the signal integrity of a proposed design}@}. {@{A combination of the two approaches}@} may be used as well: simulating the effects of {@{an arbitrary circuit or [transmission line](transmission%20line.md) on a measured signal}@}, perhaps to determine {@{whether a signal will still be intelligible after passing through a long cable}@}. {@{[Interpolation](interpolation.md)}@} may also be applied at this time in order to {@{increase the number of samples per unit interval \(UI\)}@} and produce {@{a smooth, gap-free plot}@} which is {@{more visually appealing and easier to understand}@}. <!--SR:!2026-08-25,272,330!2026-09-05,279,330!2026-08-23,268,330!2026-08-27,272,330!2026-07-31,251,330!2026-09-15,288,330!2026-09-16,289,330!2026-08-25,270,330!2026-07-11,236,330!2026-08-08,258,330!2026-07-15,239,330!2026-09-07,281,330!2026-07-12,237,330-->

### slicing

Next, {@{the position of each sample within the UI}@} must be {@{determined}@}. There are {@{several methods for doing this}@} depending on {@{the characteristics of the signal and the capabilities of the oscilloscope and software}@} in use. This step is {@{critically important}@} for {@{accurate visualization of [jitter](jitter.md) in the eye}@}. <!--SR:!2026-08-30,276,330!2026-08-29,275,330!2026-08-20,268,330!2026-08-22,269,330!2026-07-12,237,330!2026-07-25,247,330-->

#### triggering

{@{A very simple method of slicing}@} is to {@{set the oscilloscope display}@} to be {@{slightly more than one UI wide}@}, trigger on {@{both rising and falling edges in the signal}@}, and {@{enable display persistence}@} so that {@{all measured waveforms "stack" into a single plot}@}. This has the advantage of being {@{possible on almost any oscilloscope \(even fully analog ones\)}@} and can provide {@{decent visualization of noise and overall signal shape}@}, but completely {@{destroys the jitter content of the signal}@} since {@{the instrument's trigger re-synchronizes the plot to each UI}@}. {@{The only jitter visible with this method}@} is {@{that of the oscilloscope itself}@}, as well as {@{extremely high frequency jitter}@} \({@{frequencies with period less than the UI}@}\). <!--SR:!2026-08-02,253,330!2026-08-19,267,330!2026-09-11,284,330!2026-08-09,258,330!2026-09-01,276,330!2026-09-19,291,330!2026-09-21,293,330!2026-09-05,279,330!2026-09-01,275,330!2026-07-15,239,330!2026-07-13,237,330!2026-08-17,265,330!2026-07-15,239,330!2026-09-21,293,330-->

#### fixed rate

A simple way to have {@{the eye pattern display jitter in the signal}@} is to estimate {@{the [symbol rate](symbol%20rate.md) of the signal}@} \(perhaps by counting {@{the average number of zero crossings in a known window of time}@}\) and acquiring {@{many UIs in a single oscilloscope capture}@}. {@{The first zero crossing in the capture}@} is {@{located and declared to be the start of the first UI}@}, and {@{the remainder of the waveform}@} is divided {@{into chunks one UI long}@}. <!--SR:!2026-07-19,242,330!2026-09-20,292,330!2026-07-09,234,330!2026-08-01,253,330!2026-09-06,280,330!2026-07-14,238,330!2026-08-17,265,330!2026-08-12,261,330-->

This approach can {@{work adequately}@} for {@{stable signals in which the symbol rate remains exactly the same over time}@}, however {@{inaccuracies in the system}@} mean that {@{some drift is inevitable}@} so it is {@{rarely used in practice}@}. In {@{some protocols, such as [SATA](SATA.md)}@}, {@{the symbol rate is intentionally varied}@} by use of {@{[spread spectrum clocking](spread%20spectrum%20clocking.md#clock%20signal%20generation)}@}, so {@{assuming a fixed rate}@} will lead to the eye {@{grossly exaggerating the actual jitter present on the signal}@}. \(While {@{spread spectrum modulation on a clock}@} is {@{technically jitter in the strict sense}@}, {@{receivers for these systems}@} are designed to {@{track the modulation}@}. {@{The only jitter of interest to a signal integrity engineer}@} is jitter {@{much faster than the modulation rate}@}, which {@{the receiver cannot track effectively}@}.\) <!--SR:!2026-08-03,255,330!2026-07-30,251,330!2026-08-01,253,330!2026-08-06,256,330!2026-08-30,275,330!2026-08-01,253,330!2026-08-26,271,330!2026-08-24,271,330!2026-07-08,233,330!2026-08-02,254,330!2026-08-06,256,330!2026-07-24,246,330!2026-07-09,234,330!2026-07-21,244,330!2026-08-21,268,330!2026-07-30,250,330!2026-07-19,242,330-->

#### reference clock

With {@{some protocols, such as [HDMI](HDMI.md)}@}, {@{a reference clock}@} is supplied {@{along with the signal}@}, either {@{at the symbol rate or at a lower \(but synchronized\) frequency}@} from which {@{a symbol clock can be reconstructed}@}. Since {@{the actual receiver in the system}@} uses {@{the reference clock to sample the data}@}, {@{using this clock to determine UI boundaries}@} allows the eye pattern to {@{faithfully display the signal as the receiver sees it}@}: {@{only jitter between the signal and the reference clock}@} is {@{displayed}@}. <!--SR:!2026-09-13,286,330!2026-09-22,294,330!2026-09-14,287,330!2026-07-31,252,330!2026-08-18,266,330!2026-07-19,242,330!2026-07-23,246,330!2026-08-26,272,330!2026-09-19,291,330!2026-09-18,290,330!2026-07-22,245,330-->

#### clock recovery

{@{Most high speed serial signals}@}, such as {@{[PCIe](PCIe.md), [DisplayPort](DisplayPort.md), and most variants of [Ethernet](ethernet.md)}@}, use {@{a [line code](line%20code.md)}@} which is intended to allow {@{easy [clock recovery](clock%20recovery.md) by means of a [PLL](PLL.md)}@}. Since this is {@{how the actual receiver works}@}, {@{the most accurate way to slice data}@} for the eye pattern is to implement {@{a PLL with the same characteristics in software}@}. {@{Correct PLL configuration}@} allows for the eye to conceal {@{the effects of spread spectrum clocking}@} and other {@{long-term variation in the symbol rate}@} which {@{do not contribute to errors at the receiver}@}, while still {@{displaying higher frequency jitter}@}. <!--SR:!2026-08-14,263,330!2026-09-13,286,330!2026-08-26,272,330!2026-09-12,285,330!2026-08-26,272,330!2026-09-02,277,330!2026-08-23,270,330!2026-07-21,244,330!2026-07-22,245,330!2026-07-08,233,330!2026-07-20,243,330!2026-09-13,286,330-->

### integration

{@{The samples}@} are then accumulated {@{into a two-dimensional [histogram](histogram.md)}@}, with {@{the X axis representing time within the UI and the Y axis representing voltage}@}. This is {@{then [normalized](feature%20scaling.md)}@} by dividing {@{the value in each histogram bin by the value in the largest bin}@}. {@{[Tone mapping](tone%20mapping.md), logarithmic scaling}@}, or other {@{mathematical transformations}@} may be applied in order to emphasize {@{different portions of the distribution}@}, and {@{a color gradient}@} is applied to {@{the final eye for display}@}. <!--SR:!2026-08-24,269,330!2026-08-01,253,330!2026-07-18,241,330!2026-08-29,275,330!2026-08-13,262,330!2026-08-20,265,330!2026-09-12,285,330!2026-07-17,241,330!2026-08-23,270,330!2026-07-21,244,330-->

{@{Large amounts of data}@} may be needed to provide {@{an accurate representation of the signal}@}; {@{tens to hundreds of millions of UIs}@} are frequently {@{used for a single eye pattern}@}. In the example below, {@{the eye using twelve thousand UIs}@} only shows {@{the basic shape of the eye}@}, while {@{the eye using eight million UIs}@} shows {@{far more nuance on the rising and falling edges}@}. <!--SR:!2026-08-22,269,330!2026-08-18,266,330!2026-08-20,268,330!2026-08-05,255,330!2026-08-14,263,330!2026-08-02,254,330!2026-08-17,265,330!2026-07-29,251,330-->

> {@{![Eye pattern of twelve thousand UIs of a 1.25 Gbit/s signal](../../archives/Wikimedia%20Commons/Eye%20pattern%202.png)}@}
>
> {@{Eye pattern}@} of {@{twelve thousand UIs}@} of {@{a 1.25 Gbit/s signal}@} <!--SR:!2026-08-15,263,330!2026-08-29,275,330!2026-08-13,262,330!2026-08-07,257,330-->

<!-- markdownlint MD028 -->

> {@{![Eye pattern of eight million UIs \(unit intervals\) of a 1.25 Gbit/s signal](../../archives/Wikimedia%20Commons/Eye%20pattern%20example.png)}@}
>
> {@{Eye pattern}@} of {@{eight million UIs \(unit intervals\)}@} of {@{a 1.25 Gbit/s signal}@} <!--SR:!2026-08-02,254,330!2026-08-02,254,330!2026-09-02,276,330!2026-08-08,258,330-->

## modulation

Each form of {@{baseband modulation}@} produces {@{an eye pattern with a unique appearance}@}. <!--SR:!2026-09-09,283,330!2026-09-10,283,330-->

### NRZ

The eye pattern of {@{a [NRZ](non-return-to-zero.md) \(annotation: non-return-to-zero\) signal}@} should consist of {@{two clearly distinct levels with smooth transitions between them}@}. <!--SR:!2026-08-29,275,330!2026-08-06,256,330-->

> {@{![Eye pattern of a 1.25 Gbit/s NRZ signal](../../archives/Wikimedia%20Commons/Eye%20pattern%20example.png)}@}
>
> {@{Eye pattern}@} of {@{a 1.25 Gbit/s NRZ signal}@} <!--SR:!2026-08-10,259,330!2026-07-16,240,330!2026-07-12,237,330-->

### MLT-3

The eye pattern of {@{a [MLT-3](MLT-3%20encoding.md) \(annotation: multi-level transmit\) signal}@} should consist of {@{three clearly distinct levels \(nominally -1, 0, +1 from bottom to top\)}@}. {@{The 0 level}@} should be located {@{at zero volts}@} and {@{the overall shape}@} should be {@{symmetric about the horizontal axis}@}. {@{The +1 and -1 states}@} should {@{have equal amplitude}@}. There should be {@{smooth transitions from the 0 state to the +1 and -1 states}@}, however there should be {@{no direct transitions from the -1 to +1 state}@} \(which would indicate the signal is {@{PAM-3 rather than MLT-3}@}\). <!--SR:!2026-07-17,241,330!2026-07-27,249,330!2026-08-13,262,330!2026-08-13,262,330!2026-08-08,257,330!2026-07-10,235,330!2026-09-04,279,330!2026-08-28,274,330!2026-08-30,273,330!2026-09-22,294,330!2026-08-14,263,330-->

> {@{![Eye pattern of a 125 Mbit/s MLT-3 signal](../../archives/Wikimedia%20Commons/Eye%20pattern%20MLT3.png)}@}
>
> {@{Eye pattern}@} of {@{a 125 Mbit/s MLT-3 signal}@} <!--SR:!2026-08-30,275,330!2026-07-18,241,330!2026-08-27,273,330-->

### PAM

The eye pattern of {@{a [PAM](pulse-amplitude%20modulation.md) \(annotation: pulse-amplitude modulation\) signal}@} should consist of {@{N clearly distinct levels}@} \(depending on {@{the PAM order}@}, for example {@{PAM-4 should have four levels and PAM-3 should have three}@}\). {@{The overall shape}@} should be {@{symmetric about the horizontal axis}@} and {@{the spacing of all levels}@} should be {@{uniform}@}. <!--SR:!2026-08-28,274,330!2026-08-16,264,330!2026-09-10,284,330!2026-09-01,276,330!2026-09-05,280,330!2026-07-23,246,330!2026-07-25,247,330!2026-08-12,261,330-->

> {@{![Eye pattern of a PAM-3 signal \([100BASE-T1](100BASE-T1.md#100BASE-T1) automotive Ethernet\)](../../archives/Wikimedia%20Commons/Eye%20pattern%20PAM3.png)}@}
>
> {@{Eye pattern}@} of {@{a PAM-3 signal}@} \({@{[100BASE-T1](100BASE-T1.md#100BASE-T1) automotive Ethernet}@}\) <!--SR:!2026-08-21,268,330!2026-09-04,279,330!2026-08-10,259,330!2026-08-19,267,330-->

### PSK

- Main article: ::@:: [Phase-shift keying](phase-shift%20keying.md) <!--SR:!2026-07-08,233,330!2026-09-02,277,330-->

> {@{![Eye pattern of a binary PSK system](../../archives/Wikimedia%20Commons/Binary%20PSK%20eye%20diagram.svg)}@}
>
> {@{Eye pattern}@} of {@{a binary PSK system}@}
>
> {@{![Eye pattern of the same system with multipath interference \(MI\) effects added](../../archives/Wikimedia%20Commons/Multipath%20system%20eye%20diagram.svg)}@}
>
> {@{Eye pattern}@} of {@{the same system}@} with {@{multipath interference \(MI\) effects added}@} <!--SR:!2026-09-11,285,330!2026-08-09,259,330!2026-09-19,291,330!2026-07-09,234,330!2026-09-18,290,330!2026-08-06,256,330!2026-08-21,266,330-->

## channel effects

{@{Many properties of a [channel](communication%20channel.md)}@} can be seen in {@{the eye pattern}@}. <!--SR:!2026-07-23,246,330!2026-07-27,249,330-->

### emphasis

{@{[Emphasis](emphasis%20(telecommunications).md)}@} applied to a signal produces {@{an additional level for each value of the signal}@} which is {@{higher \(for pre-emphasis\) or lower \(for de-emphasis\) than the nominal value}@}. <!--SR:!2026-07-28,250,330!2026-08-31,276,330!2026-08-25,272,330-->

{@{The eye pattern for a signal with emphasis}@} may be mistaken for that of {@{a PAM signal}@} at first glance, however {@{closer inspection}@} reveals {@{some key differences}@}. Most notably, {@{an emphasized signal}@} has {@{a limited set of legal transitions}@}: <!--SR:!2026-08-16,264,330!2026-08-28,273,330!2026-09-15,288,330!2026-07-14,238,330!2026-07-22,245,330!2026-07-16,240,330-->

- Strong state to corresponding weak state ::@:: \(1-1 or 0-0 bit pattern\) <!--SR:!2026-07-12,237,330!2026-09-01,276,330-->
- Strong state to opposite strong state ::@:: \(second transition of a 1-0-1 or 0-1-0 bit pattern\) <!--SR:!2026-07-11,236,330!2026-09-18,290,330-->
- Weak state to opposite strong state ::@:: \(second transition of a 1-1-0 or 0-0-1 bit pattern\) <!--SR:!2026-08-02,254,330!2026-08-23,270,330-->

{@{An emphasized signal}@} will never {@{transition from a weak state to the corresponding strong state}@}, {@{a weak state to another weak state}@}, or {@{remain in the same strong state for more than one UI}@}. {@{A PAM signal}@} also normally {@{has equally spaced levels}@} while {@{emphasized levels}@} are normally {@{closer to the nominal signal level}@}. <!--SR:!2026-07-31,252,330!2026-09-16,289,330!2026-09-22,294,330!2026-08-31,274,330!2026-08-19,264,330!2026-09-20,292,330!2026-09-03,277,330!2026-09-18,290,330-->

> {@{![Eye pattern of a 1.25 Gbps NRZ signal with 6 dB of pre-emphasis](../../archives/Wikimedia%20Commons/Eye%20pattern%20emphasis.png)}@}
>
> {@{Eye pattern}@} of {@{a 1.25 Gbps NRZ signal}@} with {@{6 dB of pre-emphasis}@} <!--SR:!2026-08-28,274,330!2026-09-16,289,330!2026-07-27,249,330!2026-08-03,255,330-->

### high-frequency loss

{@{Loss \(annotation: power loss\)}@} of {@{printed circuit board traces and cables}@} {@{increases with frequency due to [dielectric loss](dielectric%20loss.md)}@}, which causes {@{the channel}@} to {@{behave as a [low-pass filter](low-pass%20filter.md)}@}. {@{The effect of this}@} is {@{an increase in signal rise/fall time}@}. If {@{the data rate is high enough or the channel is lossy enough}@}, the signal {@{may not even reach its full value}@} during {@{a fast 0–1–0 or 1–0–1 transition}@}, and only {@{stabilize after a run of several identical bits}@}. This results in {@{vertical closure of the eye}@}. <!--SR:!2026-09-08,282,330!2026-07-10,235,330!2026-08-22,267,330!2026-07-11,236,330!2026-09-21,293,330!2026-07-13,237,330!2026-08-29,274,330!2026-08-28,274,330!2026-09-06,280,330!2026-08-12,261,330!2026-07-26,248,330!2026-08-27,273,330-->

The image below shows {@{a 1.25 Gbit/s NRZ signal}@} after passing {@{through a lossy channel}@} – {@{an RG-188 coaxial cable}@} {@{approximately 12 feet \(3.7 m\) in length}@}. {@{This channel}@} has {@{loss increasing in a fairly linear fashion}@} {@{from 0.1 dB at DC to 9 dB at 6 GHz}@}. <!--SR:!2026-08-01,253,330!2026-07-29,251,330!2026-09-02,277,330!2026-07-14,238,330!2026-08-29,274,330!2026-08-07,257,330!2026-09-20,292,330-->

{@{The top and bottom "rails"}@} of {@{the eye}@} show {@{the final voltage the signal reaches}@} after {@{several consecutive bits with the same value}@}. Since the channel has {@{minimal loss at DC}@}, {@{the maximum signal amplitude}@} is {@{largely unaffected}@}. Looking at {@{the rising edge of the signal \(a 0–1 pattern\)}@} we can see that {@{the signal starts to level off}@} {@{around −300 [ps](picosecond.md)}@}, but {@{continues to rise slowly over the duration of the UI}@}. At {@{around +300 ps}@}, the signal {@{either begins falling again \(a 0–1–0 pattern\)}@} or {@{continues rising slowly \(a 0–1–1 pattern\)}@}. <!--SR:!2026-07-26,248,330!2026-09-06,281,330!2026-08-21,268,330!2026-08-14,263,330!2026-08-03,254,330!2026-09-04,278,330!2026-08-22,269,330!2026-09-02,277,330!2026-07-16,240,330!2026-08-22,269,330!2026-09-11,285,330!2026-09-17,290,330!2026-07-13,237,330!2026-07-20,243,330-->

> {@{![Eye pattern of a 1.25 Gbit/s NRZ signal through a lossy channel](../../archives/Wikimedia%20Commons/Eye%20pattern%20LPF.png)}@}
>
> {@{Eye pattern}@} of {@{a 1.25 Gbit/s NRZ signal}@} through {@{a lossy channel}@} <!--SR:!2026-08-30,276,330!2026-09-20,292,330!2026-08-07,257,330!2026-08-21,268,330-->

As {@{high frequency losses increase}@} {@{the overall shape of the eye}@} gradually {@{degrades into a sinusoid}@} \(once {@{higher frequency harmonics of the data has been eliminated}@}, {@{all that remains}@} is {@{the fundamental}@}\) and {@{decreases in amplitude}@}. <!--SR:!2026-09-17,290,330!2026-07-28,250,330!2026-08-15,263,330!2026-08-04,255,330!2026-08-01,252,330!2026-07-28,250,330!2026-09-09,283,330-->

### impedance mismatches

{@{Stubs, impedance mismatches}@}, and {@{other defects in a transmission line}@} can cause {@{[reflections](signal%20reflection.md)}@} visible as {@{defects in the edges of the signal}@}. {@{Reflections with a delay greater than one UI}@} often {@{render the eye completely unreadable}@} due to {@{[inter-symbol interference \(ISI\)](intersymbol%20interference.md)}@}, however {@{those with a shorter delay}@} can be easily {@{seen in the shape of the eye}@}. <!--SR:!2026-09-19,291,330!2026-07-14,238,330!2026-09-12,285,330!2026-07-27,249,330!2026-07-13,237,330!2026-09-03,278,330!2026-07-30,251,330!2026-08-05,255,330!2026-08-24,271,330-->

In the image below, {@{a roughly 1-inch \(25 mm\) open circuited stub}@} is {@{present in the line}@}, causing {@{an initial low-impedance effect \(reduced amplitude\)}@} followed by {@{a positive reflection from the end of the stub}@} with {@{a delay of about 320 ps or 0.4 UIs}@}. This can be clearly seen as {@{a "step" in the rising edge}@} in which the signal {@{rises to a fraction of the full value}@}, {@{levels off for the round trip delay of the stub}@}, then {@{rises to its full value when the reflection arrives}@}. <!--SR:!2026-09-01,276,330!2026-07-20,243,330!2026-08-08,258,330!2026-07-26,248,330!2026-09-07,281,330!2026-08-11,260,330!2026-09-03,278,330!2026-09-14,287,330!2026-07-29,251,330-->

> {@{![Eye pattern of a 1.25 Gbit/s NRZ signal with a one-inch stub](../../archives/Wikimedia%20Commons/Eye%20pattern%20mismatch.png)}@}
>
> {@{Eye pattern}@} of {@{a 1.25 Gbit/s NRZ signal}@} with {@{a one-inch stub}@} <!--SR:!2026-08-09,259,330!2026-08-28,273,330!2026-04-04,157,310!2026-08-27,273,330-->

In the image below, {@{an additional three inches of cable}@} is {@{added to the end of the same stub}@}. {@{The same "step" is present}@} but is now {@{four times as long}@}, producing {@{reflections at about 1280 ps or 1.6 UI}@}. This produces {@{extreme ISI}@} \(since {@{the reflection of each UI arrives during the subsequent UI}@}\) which {@{completely closes the eye}@}. <!--SR:!2026-08-31,276,330!2026-09-01,276,330!2026-09-02,277,330!2026-07-17,241,330!2026-09-02,277,330!2026-08-20,268,330!2026-09-14,287,330!2026-08-03,255,330-->

> {@{![Eye pattern of a 1.25 Gbit/s NRZ signal with a four-inch stub](../../archives/Wikimedia%20Commons/Eye%20pattern%20long%20stub.png)}@}
>
> {@{Eye pattern}@} of {@{a 1.25 Gbit/s NRZ signal}@} with {@{a four-inch stub}@} <!--SR:!2026-08-03,255,330!2026-08-15,263,330!2026-08-16,264,330!2026-08-05,255,330-->

## measurements

There are {@{many measurements}@} that can be {@{obtained from an eye diagram}@}:<sup>[\[4\]](#^ref-4)</sup> \(annotation: 2 items: {@{amplitude measurements, time measurements}@}\) <!--SR:!2026-07-28,250,330!2026-09-17,290,330!2026-07-10,235,330-->

Amplitude measurements

- Eye amplitude
- Eye crossing amplitude
- Eye crossing percentage
- Eye height
- Eye level
- Eye signal-to-noise ratio
- Quality factor
- Vertical eye opening

Time measurements

- Deterministic jitter
- Eye crossing time
- Eye delay
- Eye fall time
- Eye rise time
- Eye width
- Horizontal eye opening
- Peak-to-peak jitter
- Random jitter
- RMS jitter
- CRC jitter
- Total jitter

### interpreting measurements

| Eye-diagram feature                  | What it measures                                                    |
| ------------------------------------ | ------------------------------------------------------------------- |
| Eye opening \(height, peak to peak\) | Additive [noise](noise.md) in the signal                            |
| Eye overshoot/undershoot             | [distortion](distortion.md) due to interruptions in the signal path |
| Eye width                            | Timing synchronization and [jitter](jitter.md) effects              |
| Eye closure                          | Intersymbol interference, additive noise                            |

> __flashcards__
>
> - Eye opening \(height, peak to peak\) ::@:: Additive [noise](noise.md) in the signal <!--SR:!2026-08-11,260,330!2026-08-27,273,330-->
> - Eye overshoot/undershoot ::@:: [distortion](distortion.md) due to interruptions in the signal path <!--SR:!2026-07-31,252,330!2026-08-05,255,330-->
> - Eye width ::@:: Timing synchronization and [jitter](jitter.md) effects <!--SR:!2026-08-11,260,330!2026-08-07,257,330-->
> - Eye closure ::@:: Intersymbol interference, additive noise <!--SR:!2026-07-29,251,330!2026-07-19,242,330-->

## see also

- [Constellation diagram](constellation%20diagram.md)
- [Signal integrity](signal%20integrity.md)
- [Raised-cosine filter](raised-cosine%20filter.md)
- [Extinction ratio](extinction%20ratio.md)

## notes

1. Christopher M. Miller "High-Speed Digital Transmitter Characterization Using Eye Diagram Analysis". [1266 Hewlett-Packard Journal 45\(1994\) Aug., No,4](http://www.hpl.hp.com/hpjournal/pdfs/IssuePDFs/1994-08.pdf) [Archived](https://web.archive.org/web/20210126091059/http://www.hpl.hp.com/hpjournal/pdfs/IssuePDFs/1994-08.pdf) 2021-01-26 at the [Wayback Machine](Wayback%20Machine.md), pp. 29-37. <a id="^ref-1"></a>^ref-1
2. ![Public Domain](../../archives/Wikimedia%20Commons/PD-icon.svg) This article incorporates [public domain material](Copyright%20status%20of%20works%20by%20the%20federal%20government%20of%20the%20United%20States.md) from [_Federal Standard 1037C_](https://web.archive.org/web/20220122224547/https://www.its.bldrdoc.gov/fs-1037/fs-1037c.htm). [General Services Administration](General%20Services%20Administration.md). Archived from [the original](https://www.its.bldrdoc.gov/fs-1037/fs-1037c.htm) on 2022-01-22. \(in support of [MIL-STD-188](MIL-STD-188.md)\). <a id="^ref-2"></a>^ref-2
3. John G Proakis, Digital Communications 3rd ed, 2001 <a id="^ref-3"></a>^ref-3
4. ["Matlab's help file description of how to use the Eye Diagram Functions in the Communications Toolbox"](http://www.mathworks.com/access/helpdesk/help/toolbox/comm/index.html?/access/helpdesk/help/toolbox/comm/ref/commscope.eyediagram.html). <a id="^ref-4"></a>^ref-4

## references

This text incorporates [content](https://en.wikipedia.org/wiki/eye_pattern) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- ["HP E4543A Q Factor and Eye Contours Application Software Operating Manual"](http://literature.cdn.keysight.com/litweb/pdf/E4543-90004.pdf) \(PDF\). 1999. [Archived](https://ghostarchive.org/archive/20221009/http://literature.cdn.keysight.com/litweb/pdf/E4543-90004.pdf) \(PDF\) from the original on 2022-10-09.
- ["Agilent 71501D Eye-Diagram Analysis User's Guide"](http://literature.cdn.keysight.com/litweb/pdf/70874-90023.pdf) \(PDF\). [Archived](https://ghostarchive.org/archive/20221009/http://literature.cdn.keysight.com/litweb/pdf/70874-90023.pdf) \(PDF\) from the original on 2022-10-09.

## external links

> ![Wikimedia Commons logo](../../archives/Wikimedia%20Commons/Commons-logo.svg) Wikimedia Commons has media related to ___[Eye diagrams](https://commons.wikimedia.org/wiki/Category%3AEye_diagrams)___.

- <a id="CITEREFRuckerbauer2009"></a> Ruckerbauer, Hermann \(29 June 2009\). ["An Eye is Born"](https://www.youtube.com/watch?v=my7CI84le5g). _[YouTube](YouTube.md)_. Gives an example video of construction of an eye pattern
- [Understanding Data Eye Diagram Methodology for Analyzing High Speed Digital Signals](http://www.onsemi.com/pub_link/Collateral/AND9075-D.PDF)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Data transmission](https://en.wikipedia.org/wiki/Category:Data%20transmission)
