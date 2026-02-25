# Flashcard‑creation Skill Examples

This page provides a clean catalog of real input/output pairs the flashcard-creation skill should produce. It exists for the agent to reference when deciding how to insert `{@{ }@}`, `::@::` or `:@:` markup. Examples are numbered, described, and each shows the raw Markdown followed by the correctly annotated revision.

Consult the appropriate example when facing a similar editing challenge.

## Quick index

1. Dense math paragraph with annotations
2. Long technical paragraph with sequential logic
3. Circuit cancellation description
4. Transform hierarchy statement
5. Inverse relationship property

(Only the first five examples are shown; additional patterns follow the same format.)

## Example 1 – System prompt dense math paragraph

**Input:**

```text
If _f_ is (annotation: of exponential growth; then) also causal, and analytical, then: ${\widehat {f} }(i\tau )=F(-2\pi \tau )$. Thus, extending the Fourier transform to the complex domain means it includes the Laplace transform as a special case in the case of causal functions—but with the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown separator -->_ξ_. (annotation: That is, make any expression containing _ξ_ in the form of that on the right hand side, then simply replace it with _s_. Now the Fourier transform with _ξ_ as input becomes the Laplace transform with _s_ as input.)
```

**Output:**

```text
If _f_ is {@{(annotation: of exponential growth; then) also causal, and analytical}@}, then: {@{${\widehat {f} }(i\tau )=F(-2\pi \tau )$}@}. Thus, extending {@{the Fourier transform to the complex domain}@} means it includes {@{the Laplace transform as a special case}@} in the case of {@{causal functions}@}—but with {@{the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown separator -->_ξ_}@}. (annotation: That is, make {@{any expression containing _ξ_}@} in the form of that on {@{the right hand side}@}, then simply {@{replace it with _s_}@}. Now {@{the Fourier transform with _ξ_ as input}@} becomes {@{the Laplace transform with _s_ as input}@}.)
```

## Example 2 – Laplace/Fourier classical viewpoint long paragraph

**Input:**

```text
From another, perhaps more classical viewpoint, the Laplace transform by its form involves an additional exponential regulating term which lets it converge outside of the imaginary line where the Fourier transform is defined. As such it can converge for at most exponentially divergent series and integrals, whereas the original Fourier decomposition cannot, enabling analysis of systems with divergent or critical elements. Two particular examples from linear signal processing are the construction of allpass filter networks from critical comb and mitigating filters via exact pole-zero cancellation on the unit circle. Such designs are common in audio processing, where highly nonlinear phase response is sought for, as in reverb.
```

**Output:**

```text
From another, perhaps {@{more classical viewpoint}@}, {@{the Laplace transform by its form}@} involves {@{an additional exponential regulating term}@} which lets it converge {@{outside of the imaginary line}@} where {@{the Fourier transform is defined}@}. As such it can {@{converge for at most exponentially divergent series and integrals}@}, whereas {@{the original Fourier decomposition cannot}@}, enabling {@{analysis of systems with divergent or critical elements}@}. Two particular examples from {@{linear signal processing}@} are the construction of {@{allpass filter networks from critical comb}@} and {@{mitigating filters}@} via {@{exact pole-zero cancellation on the unit circle}@}. Such designs are {@{common in audio processing}@}, where {@{highly nonlinear phase response}@} is {@{sought for, as in reverb}@}.
```

## Example 3 – Extended pulselike impulse response circuit description

**Input:**

```text
Furthermore, when extended pulselike impulse responses are sought for signal processing work, the easiest way to produce them is to have one circuit which produces a divergent time response, and then to cancel its divergence through a delayed opposite and compensatory response. There, only the delay circuit in-between admits a classical Fourier description, which is critical. Both the circuits to the side are unstable, and do not admit a convergent Fourier decomposition. However, they do admit a Laplace domain description, with identical half-planes of convergence in the complex plane (or in the discrete case, the Z-plane), wherein their effects cancel.
```

**Output:**

```text
Furthermore, when {@{extended pulselike impulse responses}@} are {@{sought for signal processing work}@}, {@{the easiest way to produce them}@} is to have {@{one circuit which produces a divergent time response}@}, and then to {@{cancel its divergence}@} through {@{a delayed opposite and compensatory response}@}. There, only {@{the delay circuit in-between}@} admits {@{a classical Fourier description}@}, which is {@{critical}@}. {@{Both the circuits to the side}@} are {@{unstable, and do not admit a convergent Fourier decomposition}@}. However, they do admit {@{a Laplace domain description}@}, with {@{identical half-planes of convergence in the complex plane}@} (or in {@{the discrete case, the Z-plane}@}), wherein {@{their effects cancel}@}.
```

## Example 4 – Modern mathematics subsuming transforms

**Input:**

```text
In modern mathematics the Laplace transform is conventionally subsumed under the aegis Fourier methods. Both of them are subsumed by the far more general, and more abstract, idea of harmonic analysis.
```

**Output:**

```text
In {@{modern mathematics}@} {@{the Laplace transform}@} is conventionally {@{subsumed under the aegis Fourier methods}@}. {@{Both of them}@} are subsumed by {@{the far more general, and more abstract, idea of harmonic analysis}@}.
```

## Example 5 – Concentration and spread of Fourier transform

**Input:**

```text
Generally speaking, the more concentrated f(x) is, the more spread out its Fourier transform f̂(ξ) must be. In particular, the scaling property of the Fourier transform may be seen as saying: if we squeeze a function in x, its Fourier transform stretches out in ξ. It is not possible to arbitrarily concentrate both a function and its Fourier transform.
```

**Output:**

```text
Generally speaking, {@{the more concentrated f(x) is}@}, {@{the more spread out its Fourier transform f̂(ξ) must be}@}. In particular, {@{the scaling property of the Fourier transform}@} may be seen as saying: {@{if we squeeze a function in x}@}, {@{its Fourier transform stretches out in ξ}@}. {@{It is not possible to arbitrarily concentrate both a function and its Fourier transform}@}.
```

*This file now shows a handful of representative examples; add more only if
necessary.*
