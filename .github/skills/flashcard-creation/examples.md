# Flashcard‑creation Skill Examples

This document stores **input/output pairs** that demonstrate how the flashcard
creation skill should behave.  Entries are indexed for easy lookup, and the
ingent agent is expected to consult this file whenever it needs guidance or a
reminder of past formatting decisions.

Each numbered example contains the original Markdown text provided by the
user and the revised text with `{@{ }@}`/`::@::`/`:@:` markup inserted.

---

## Index

| No. | Description                                                                     | Tags                                                                            |
| --- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1   | Dense math-heavy paragraph with inline annotations                              | dense prose, math, maximal coverage, annotation, formula, variable-substitution |
| 2   | Long technical paragraph with sequential logical steps                          | dense prose, technical, sequential facts, long-paragraph, transformation        |
| 3   | Technical circuit description illustrating cancellation                         | technical, circuit, cancellation, instability, laplace                          |
| 4   | Conceptual hierarchy statement linking transforms                               | conceptual hierarchy, transform-relationship, modern-math                       |
| 5   | Statement of inverse relationship property                                      | mathematical property, inverse-relationship, scaling, uncertainty               |
| 6   | Abstract definition of a vector-space concept                                   | definition, vector space, abstract, communications                              |
| 7   | Geometric perspective summarizing applications                                  | geometric, application, visualization, matched-filter                           |
| 8   | Dense mathematical trade-off explanation                                        | math, canonical transformation, trade-off, uncertainty, symplectic              |
| 9   | General description of design pattern constraints                               | software, patterns, OOP, language-suitability                                   |
| 10  | Classification list of pattern categories                                       | list, classification, creational, structural, behavioral                        |
| 11  | Trade‑off statement contrasting flexibility and performance                     | design tradeoff, flexibility, indirection, performance                          |
| 12  | Definition/equivalence pair in category theory                                  | math, category theory, definition, equivalence                                  |
| 13  | Definition with distinguishing criteria for anti‑patterns                       | software, anti-pattern, definition, criteria                                    |
| 14  | Sentence listing elements of a documentation format                             | software documentation, listing-elements, format                                |
| 15  | Multi‑point strategic rationale paragraph                                       | business strategy, multi-point, rationale, competitor-profiling                 |
| 16  | Definition and use-case summary for financial instrument                        | finance, derivative, definition, use-case, forwards                             |
| 17  | Simple numeric example explaining profit/loss                                   | finance, example, numeric, profit-loss                                          |
| 18  | Warning about procedural difficulty                                             | finance, contracts, warning, closing-position                                   |
| 19  | Contrast between two quoting conventions                                        | finance, market terminology, comparison, quoting                                |
| 20  | Recommendation to include nonfunctional items                                   | software requirements, recommendation                                           |
| 21  | Example of wrapping entire LaTeX equation in cloze                              | equation, latex rule, whole-equation                                            |
| 22  | Splitting long sentence into multiple clozes                                    | split, coverage, long-sentence, multi-clause                                    |
| 23  | Breaking multipart sentence for clarity                                         | split, phrase, multipart, clarity                                               |
| 24  | CAPM collapse and Markowitz estimation burden explanation                       | CAPM, SIM, Markowitz, math, comparison, two-paragraph                           |
| 25  | SIM limitations multi‑paragraph style with user’s preferred compact cloze order | SIM, multi-paragraph, user-style, macro variables                               |
| 26  | multi-factor model definition with split clozes                                 | multi-factor, split, subject-object                                             |
| 27  | factor-mimicking portfolio definition and equation                              | portfolio, equation, definition                                                 |
| 28  | interpretation paragraph with component list                                    | interpretation, list, components, multi-factor                                  |
| 29  | background & no-free-lunch sentences with highway anecdote                      | background, no-free-lunch, full-sentence, anecdote                              |
| 30  | numeric mispricing arbitrage example with portfolio weights                     | mispricing, numeric, full-sentence, weights, arbitrage                          |
| 31  | semicolon-separated clauses treated individually                                | semicolon, list, clause-splitting, APT assumptions                              |
| 32  | contrastive conjunction splitting (but/market data example)                     | contrast, conjunction, 'but', splitting, coverage                               |
| 33  | minimal cloze boundaries avoiding leading conjunctions and pronouns             | minimal-cloze, conjunction, conditional, style                                  |
| 34  | short declarative sentence split subject/predicate (mispricing/arbitrage)       | short-sentence, split-subject-predicate, minimal                                |
| 35  | articles inside clozes                                                          | article-placement, noun-phrase, style                                           |

---

(Additional entries can be appended; update the index table above with new numbers, descriptions and tags.)

## Example 1 – System prompt dense math paragraph

**Input:**

```text
Study the following Markdown text.

If _f_ is (annotation: of exponential growth; then) also causal, and
analytical, then: ${\widehat {f} }(i\tau )=F(-2\pi \tau )$. Thus,
extending the Fourier transform to the complex domain means it includes the
Laplace transform as a special case in the case of causal functions—but with
the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown
separator -->_ξ_. (annotation: That is, make any expression containing _ξ_ in
the form of that on the right hand side, then simply replace it with _s_. Now
the Fourier transform with _ξ_ as input becomes the Laplace transform with _s_
as input.)
```

**Output:**

```text
If _f_ is {@{(annotation: of exponential growth; then) also causal, and analytical}@}, then: {@{${\widehat {f} }(i\tau )=F(-2\pi \tau )$}@}.
Thus, extending {@{the Fourier transform to the complex domain}@} means it includes {@{the Laplace transform as a special case}@} in the case of {@{causal functions}@}—but with {@{the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown separator -->_ξ_}@}.
(annotation: That is, make {@{any expression containing _ξ_}@} in the form of that on {@{the right hand side}@}, then simply {@{replace it with _s_}@}. Now {@{the Fourier transform with _ξ_ as input}@} becomes {@{the Laplace transform with _s_ as input}@}.)
```

## Example 2 – Laplace/Fourier classical viewpoint long paragraph

**Input:**

```text
From another, perhaps more classical viewpoint, the Laplace transform by
its form involves an additional exponential regulating term which lets it
converge outside of the imaginary line where the Fourier transform is
defined. As such it can converge for at most exponentially divergent
series and integrals, whereas the original Fourier decomposition cannot,
enabling analysis of systems with divergent or critical elements. Two
particular examples from linear signal processing are the construction
of allpass filter networks from critical comb and mitigating filters via
exact pole-zero cancellation on the unit circle. Such designs are common
in audio processing, where highly nonlinear phase response is sought for,
as in reverb.
```

**Output:**

```text
From another, perhaps {@{more classical viewpoint}@}, {@{the Laplace transform by its form}@} involves {@{an additional exponential regulating term}@} which lets it converge {@{outside of the imaginary line}@} where {@{the Fourier transform is defined}@}. As such it can {@{converge for at most exponentially divergent series and integrals}@}, whereas {@{the original Fourier decomposition cannot}@}, enabling {@{analysis of systems with divergent or critical elements}@}. Two particular examples from {@{linear signal processing}@} are the construction of {@{allpass filter networks from critical comb}@} and {@{mitigating filters}@} via {@{exact pole-zero cancellation on the unit circle}@}. Such designs are {@{common in audio processing}@}, where {@{highly nonlinear phase response}@} is {@{sought for, as in reverb}@}.
```

## Example 3 – Extended pulselike impulse response circuit description

**Input:**

```text
Furthermore, when extended pulselike impulse responses are sought for
signal processing work, the easiest way to produce them is to have one
circuit which produces a divergent time response, and then to cancel its
divergence through a delayed opposite and compensatory response. There,
only the delay circuit in-between admits a classical Fourier description,
which is critical. Both the circuits to the side are unstable, and do not
admit a convergent Fourier decomposition. However, they do admit a Laplace
domain description, with identical half-planes of convergence in the
complex plane (or in the discrete case, the Z-plane), wherein their
effects cancel.
```

**Output:**

```text
Furthermore, when {@{extended pulselike impulse responses}@} are {@{sought for signal processing work}@}, {@{the easiest way to produce them}@} is to have {@{one circuit which produces a divergent time response}@}, and then to {@{cancel its divergence}@} through {@{a delayed opposite and compensatory response}@}. There, only {@{the delay circuit in-between}@} admits {@{a classical Fourier description}@}, which is {@{critical}@}. {@{Both the circuits to the side}@} are {@{unstable, and do not admit a convergent Fourier decomposition}@}. However, they do admit {@{a Laplace domain description}@}, with {@{identical half-planes of convergence in the complex plane}@} (or in {@{the discrete case, the Z-plane}@}), wherein {@{their effects cancel}@}.
```

## Example 4 – Modern mathematics subsuming transforms

**Input:**

```text
In modern mathematics the Laplace transform is conventionally subsumed
under the aegis Fourier methods. Both of them are subsumed by the far
more general, and more abstract, idea of harmonic analysis.
```

**Output:**

```text
In {@{modern mathematics}@} {@{the Laplace transform}@} is conventionally {@{subsumed under the aegis Fourier methods}@}. {@{Both of them}@} are subsumed by {@{the far more general, and more abstract, idea of harmonic analysis}@}.
```

## Example 5 – Concentration and spread of Fourier transform

**Input:**

```text
Generally speaking, the more concentrated f(x) is, the more spread out
its Fourier transform f̂(ξ) must be. In particular, the scaling property
of the Fourier transform may be seen as saying: if we squeeze a function
in x, its Fourier transform stretches out in ξ. It is not possible to
arbitrarily concentrate both a function and its Fourier transform.
```

**Output:**

```text
Generally speaking, {@{the more concentrated f(x) is}@}, {@{the more spread out its Fourier transform f̂(ξ) must be}@}. In particular, {@{the scaling property of the Fourier transform}@} may be seen as saying: {@{if we squeeze a function in x}@}, {@{its Fourier transform stretches out in ξ}@}. {@{It is not possible to arbitrarily concentrate both a function and its Fourier transform}@}.
```

## Example 6 – Signal space definition

**Input:**

```text
A signal space is an abstract vector-space representation used in digital
communications to model transmitted waveforms as points or vectors within
a multidimensional Euclidean (or Hilbert) space. By selecting an
orthonormal set of basis functions—often derived via Gram–Schmidt
orthogonalisation—the time-domain signals are expressed as linear
combinations whose coefficients serve as coordinates.
```

**Output:**

```text
{@{A signal space}@} is {@{an abstract vector-space representation used in digital communications}@} to {@{model transmitted waveforms as points or vectors within a multidimensional Euclidean (or Hilbert) space}@}. By selecting {@{an orthonormal set of basis functions}@}—often derived via {@{Gram–Schmidt orthogonalisation}@}—{@{the time-domain signals}@} are expressed as {@{linear combinations whose coefficients serve as coordinates}@}.
```

## Example 7 – Geometric view of modulation and receivers

**Input:**

```text
This geometric view simplifies the analysis of modulation schemes,
receiver design, and error performance, enabling designers to visualize
constellations, compute Euclidean distances between symbols, and
construct matched filters that maximise signal-to-noise ratio.
```

**Output:**

```text
{@{This geometric view}@} simplifies the analysis of {@{modulation schemes, receiver design, and error performance}@}, enabling designers to visualize {@{constellations, compute Euclidean distances between symbols}@}, and construct {@{matched filters that maximise signal-to-noise ratio}@}.
```

## Example 8 – Uncertainty principle via symplectic form

**Input:**

```text
The trade-off between the compaction of a function and its Fourier
transform can be formalized in the form of an uncertainty principle by
viewing a function and its Fourier transform as conjugate variables with
respect to the symplectic form on the time–frequency domain: from the
point of view of the linear canonical transformation, the Fourier
transform is rotation by 90° in the time–frequency domain, and preserves
the symplectic form.
```

**Output:**

```text
{@{The trade-off}@} between {@{the compaction of a function and its Fourier transform}@} can be formalized in the form of {@{an uncertainty principle}@} by viewing {@{a function and its Fourier transform}@} as {@{conjugate variables with respect to the symplectic form on the time–frequency domain}@}: from the point of view of {@{the linear canonical transformation}@}, {@{the Fourier transform}@} is {@{rotation by 90° in the time–frequency domain}@}, and preserves {@{the symplectic form}@}.
```

## Example 9 – OOP design patterns relationship description

**Input:**

```text
Object-oriented design patterns typically show relationships and
interactions between classes or objects, without specifying the final
application classes or objects that are involved. Patterns that imply
mutable state may be unsuited for functional programming languages. Some
patterns can be rendered unnecessary in languages that have built-in
support for solving the problem they are trying to solve, and
object-oriented patterns are not necessarily suitable for non-object-
oriented languages.
```

**Output:**

```text
{@{Object-oriented design patterns}@} typically show {@{relationships and interactions between classes or objects}@}, without specifying the {@{final application classes or objects}@} that are involved. {@{Patterns that imply mutable state}@} may be {@{unsuited for functional programming languages}@}. {@{Some patterns}@} can be {@{rendered unnecessary in languages}@} that have {
``

## Example 10 – Classification of design patterns

**Input:**

```text
Design patterns can be organized into groups based on what kind of problem
they solve. Creational patterns create objects. Structural patterns
organize classes and objects to form larger structures that provide new
functionality. Behavioral patterns describe collaboration between objects.
```

**Output:**

```text
{@{Design patterns}@} can be {@{organized into groups based on what kind of problem they solve}@}. {@{Creational patterns}@} create {@{objects}@}. {@{Structural patterns}@} organize {@{classes and objects to form larger structures that provide new functionality}@}. {@{Behavioral patterns}@} describe {@{collaboration between objects}@}.
```

## Example 11 – Indirection trade-off in patterns

**Input:**

```text
In order to achieve flexibility, design patterns may introduce additional
levels of indirection, which may complicate the resulting design and
decrease runtime performance.
```

**Output:**

```text
In order to {@{achieve flexibility}@}, {@{design patterns}@} may introduce {@{additional levels of indirection}@}, which may {@{complicate the resulting design}@} and {@{decrease runtime performance}@}.
```

## Example 12 – Category theory equivalence

**Input:**

```text
Two categories are the same if they have the same collection of objects,
the same collection of arrows, and the same associative method of
composing any pair of arrows. Two different categories may also be
considered "equivalent" for purposes of category theory, even if they do
not have precisely the same structure.
```

**Output:**

```text
{@{Two categories are the same}@} if {@{they have the same collection of objects, the same collection of arrows, and the same associative method of composing any pair of arrows}@}. {@{Two different categories}@} may also be {@{considered "equivalent" for purposes of category theory}@}, even if they {@{do not have precisely the same structure}@}.
```

## Example 13 – Anti-pattern distinguishing aspects

**Input:**

```text
According to the authors of Design Patterns, there are two key aspects of
an anti-pattern that distinguish it from a bad habit, bad practice, or bad
idea. First, an anti-pattern is a commonly used process, structure or
pattern of action that, despite initially appearing to be appropriate and
effective, has more bad consequences than good ones. Second, another
solution exists to the problem that the anti-pattern is attempting to
address. This solution is documented, repeatable, and proven to be
effective where the anti-pattern is not.
```

**Output:**

```text
According to {@{the authors of Design Patterns}@}, there are {@{two key aspects of an anti-pattern}@} that distinguish it from {@{a bad habit, bad practice, or bad idea}@}. First, {@{an anti-pattern}@} is a {@{commonly used process, structure or pattern of action}@} that, despite {@{initially appearing to be appropriate and effective}@}, has {@{more bad consequences than good ones}@}. Second, {@{another solution}@} exists to {@{the problem that the anti-pattern is attempting to address}@}. {@{This solution}@} is {@{documented, repeatable, and proven to be effective}@} where {@{the anti-pattern is not}@}.
```

## Example 14 – Design pattern documentation format

**Input:**

```text
The documentation for a design pattern describes the context in which the
pattern is used, the forces within the context that the pattern seeks to
resolve, and the suggested solution. There is no single, standard format
for documenting design patterns. Rather, a variety of different formats
have been used by different pattern authors. However, according to Martin
Fowler, certain pattern forms have become more well-known than others, and
consequently become common starting points for new pattern-writing
efforts. One example of a commonly used documentation format is the one
used by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides in
their book Design Patterns. It contains the following sections:
```

**Output:**

```text
{@{The documentation for a design pattern}@} describes {@{the context in which the pattern is used}@}, {@{the forces within the context}@} that {@{the pattern seeks to resolve}@}, and {@{the suggested solution}@}. There is {@{no single, standard format}@} for {@{documenting design patterns}@}. Rather, {@{a variety of different formats}@} have been {@{used by different pattern authors}@}. However, {@{according to Martin Fowler}@}, {@{certain pattern forms}@} have become {@{more well-known than others}@}, and consequently become {@{common starting points for new pattern-writing efforts}@}. {@{One example of a commonly used documentation format}@} is {@{the one used by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides}@} in {@{their book Design Patterns}@}. It contains {@{the following sections}@}:
```

## Example 15 – Competitor profiling rationale

**Input:**

```text
The strategic rationale of competitor profiling is simple. Superior knowledge
of rivals offers a legitimate source of competitive advantage. The raw
material of competitive advantage consists of offering superior customer
value in the firm's chosen market. The definitive characteristic of customer
value is the adjective, superior. Customer value is defined relative to
rival offerings making competitor knowledge an intrinsic component of
corporate strategy. Profiling facilitates this strategic objective in three
important ways. First, profiling can reveal strategic weaknesses in rivals
that the firm may exploit. Second, the proactive stance of competitor
profiling will allow the firm to anticipate the strategic response of their
rivals to the firm's planned strategies, the strategies of other competing
firms, and changes in the environment. Third, this proactive knowledge will
give the firms strategic agility. Offensive strategy can be implemented more
quickly in order to exploit opportunities and capitalize on strengths.
Similarly, defensive strategy can be employed more deftly in order to
counter the threat of rival firms from exploiting the firm's own weaknesses.
```

**Output:**

```text
{@{The strategic rationale of competitor profiling}@} is {@{simple}@}. {@{Superior knowledge of rivals}@} offers a {@{legitimate source of competitive advantage}@}. {@{The raw material of competitive advantage}@} consists of {@{offering superior customer value in the firm's chosen market}@}. {@{The definitive characteristic of customer value}@} is the {@{adjective, superior}@}. {@{Customer value}@} is {@{defined relative to rival offerings}@} making {@{competitor knowledge}@} an {@{intrinsic component of corporate strategy}@}. {@{Profiling}@} facilitates this strategic objective in {@{three important ways}@}. First, {@{profiling}@} can {@{reveal strategic weaknesses in rivals}@} that the firm may {@{exploit}@}. Second, {@{the proactive stance}@} of {@{competitor profiling}@} will allow the firm to {@{anticipate the strategic response of their rivals}@} to {@{the firm's planned strategies, the strategies of other competing firms, and changes in the environment}@}. Third, {@{this proactive knowledge}@} will give the {@{firms strategic agility}@}. {@{Offensive strategy}@} can be {@{implemented more quickly}@} in order to {@{exploit opportunities and capitalize on strengths}@}. {@{Similarly, defensive strategy}@} can be {@{employed more deftly}@} in order to {@{counter the threat of rival firms from exploiting the firm's own weaknesses}@}.
``````

## Example 16 – Forward contract pricing and usage

**Input:**

```text
The price of the underlying instrument, in whatever form, is paid before
control of the instrument changes. This is one of the many forms of buy/sell
orders where the time and date of trade are not the same as the value date
where the securities themselves are exchanged. Forwards, like other derivative
securities, can be used to hedge risk (typically currency or exchange rate
risk), as a means of speculation, or to allow a party to take advantage of a
quality of the underlying instrument which is time-sensitive.
```

**Output:**

```text
{@{The price of the underlying instrument}@}, in whatever form, is {@{paid before control of the instrument changes}@}. This is one of {@{the many forms of buy/sell orders}@} where {@{the time and date of trade}@} are {@{not the same as the value date}@} where {@{the securities themselves are exchanged}@}. {@{Forwards, like other derivative securities}@}, can be used to {@{hedge risk (typically currency or exchange rate risk)}@}, as a means of {@{speculation}@}, or to allow a party to take {@{advantage of a quality of the underlying instrument which is time-sensitive}@}.
```

## Example 17 – Alice-Bob house valuation

**Input:**

```text
At the end of one year, suppose that the current market valuation of Alice's
house is $110,000. Then, because Alice is obliged to sell to Bob for only
$104,000, Bob will make a profit of $6,000. To see why this is so, one needs
only to recognize that Bob can buy from Alice for $104,000 and immediately
sell to the market for $110,000. Bob has made the difference in profit. In
contrast, Alice has made a potential loss of $6,000, and an actual profit of
$4,000.
```

**Output:**

```text
At {@{the end of one year}@}, suppose that {@{the current market valuation of Alice's house}@} is {@{$110,000}@}. Then, because {@{Alice is obliged to sell to Bob for only $104,000}@}, Bob will {@{make a profit of $6,000}@}. To see {@{why this is so}@}, one needs only to recognize that Bob can {@{buy from Alice for $104,000 and immediately sell to the market for $110,000}@}. Bob has made {@{the difference in profit}@}. In contrast, Alice has made {@{a potential loss of $6,000}@}, and {@{an actual profit of $4,000}@}.
```

## Example 18 – Closing out forward contracts difficulty

**Input:**

```text
Compared to the futures markets it is very difficult to close out one's
position, that is to rescind the forward contract. For instance while being
long in a forward contract, entering short into another forward contract
might cancel out delivery obligations but adds to credit risk exposure as
there are now three parties involved. Closing out a contract almost always
involves reaching out to the counterparty.
```

**Output:**

```text
Compared to {@{the futures markets}@} it is {@{very difficult to close out one's position}@}, that is to {@{rescind the forward contract}@}. For instance while being {@{long in a forward contract}@}, entering {@{short into another forward contract}@} might {@{cancel out delivery obligations}@} but {@{adds to credit risk exposure}@} as there are {@{now three parties involved}@}. {@{Closing out a contract}@} almost always {@{involves reaching out to the counterparty}@}.
```

## Example 19 – Outright prices explanation

**Input:**

```text
Outright prices, as opposed to premium points or forward points, are quoted
in absolute price units. Outrights are used in markets where there is no
(unitary) spot price or rate for reference, or where the spot price (rate)
is not easily accessible.
```

**Output:**

```text
{@{Outright prices}@}, as opposed to {@{premium points or forward points}@}, are {@{quoted in absolute price units}@}. {@{Outrights}@} are used in {@{markets where there is no (unitary) spot price or rate for reference}@}, or where {@{the spot price (rate) is not easily accessible}@}.
```

## Example 20 – Nonfunctional requirements in UML

**Input:**

```text
Nonfunctional requirements (e.g. performance, reliability, security)
should be represented alongside functional ones. Yet students often leave
these out of their use-case diagrams or class models, resulting in a
specification that looks complete but misses critical quality attributes.
The root cause is the misconception that UML only describes behaviour and
structure. To fix this, add text describing nonfunctional requirements to
the relevant use cases; or the entire system for whole-system requirements.
```

**Output:**

```text
{@{Nonfunctional requirements}@} (e.g. {@{performance, reliability, security}@}) should be {@{represented alongside functional ones}@}. Yet students often leave {@{these out of their use-case diagrams or class models}@}, resulting in a {@{specification that looks complete}@} but {@{misses critical quality attributes}@}. {@{The root cause}@} is the {@{misconception that UML only describes behaviour and structure}@}. To {@{fix this}@}, add {@{text describing nonfunctional requirements}@} to {@{the relevant use cases}@}; or {@{the entire system for whole-system requirements}@}.
```

## Example 21 – Entire equation cloze rule

**Input:**

```text
Einstein’s mass–energy relation is given by $$E=mc^2 \,,$$ which shows that
mass and energy are equivalent.
```

**Output:**

```text
{@{Einstein’s mass–energy relation}@} is given by {@{$$E=mc^2 \,,$$}@} which shows that
{@{mass and energy are equivalent}@}.
```

## Example 22 – splitting long clause

**Input:**

```text
Markowitz portfolio theory requires estimating n variance and n(n+1)/2 terms, which becomes infeasible when n is large.
```

**Output:**

```text
{@{Markowitz portfolio theory}@} requires estimating {@{n variance and n(n+1)/2 terms}@}. This becomes {@{infeasible when n is large}@}.
```

## Example 23 – breaking multi‑part sentence

**Input:**

```text
From the SIM model, the total variance of asset i decomposes into systematic and idiosyncratic parts: $$\sigma_i^2 = b_i^2\sigma_M^2 + \sigma_{\varepsilon,i}^2 \,.$$
```

**Output:**

```text
From {@{the SIM model}@}, {@{the total variance of asset i}@} decomposes {@{into systematic and idiosyncratic parts}@}: {@{$$\sigma_i^2 = b_i^2\sigma_M^2 + \sigma_{\varepsilon,i}^2 \,.$$}@}
```

## Example 24 – CAPM and SIM comparison with Markowitz burden

**Input:**

```text
### CAPM and SIM

When the intercept term in the single‑index equation is set to zero, the model collapses to the standard CAPM: $$r_{i,t}-r_f = \beta_{i,M}(r_{M,t}-r_f)+\varepsilon_{i,t},$$ with $\beta_{i,M}=b_i=\sigma_{i,M}/\sigma_M^2$. Thus, CAPM can be viewed as a SIM in which the constant term is zero. The relationship between expected excess returns follows $$\mu_i-r_f = \beta_{i,M}(\mu_M-r_f),$$ matching the familiar CAPM expression.

Markowitz portfolio theory requires estimating $n$ variance and $n(n - 1) / 2$ covariance, for a total of $n(n+1)/2$ variance‑covariance terms, which becomes infeasible when $n$ is large (e.g., 5 000 assets imply 12.5 million parameters). The single‑index model and CAPM avoid this by summarising risk with a few factor loadings (only the factor loadings need to be estimated), thereby reducing estimation error and computational cost.
```

**Output:**

```text
### CAPM and SIM

{@{When the intercept term in the single‑index equation is set to zero}@}, {@{the model collapses to the standard CAPM}@}: {@{$$r_{i,t}-r_f = \beta_{i,M}(r_{M,t}-r_f)+\varepsilon_{i,t},$$}@} with {@{$\beta_{i,M}=b_i=\sigma_{i,M}/\sigma_M^2$}@}. Thus, {@{CAPM can be viewed as a SIM in which the constant term is zero}@}. {@{The relationship between expected excess returns}@} follows {@{$$\mu_i-r_f = \beta_{i,M}(\mu_M-r_f),$$}@} {@{matching the familiar CAPM expression}@}.

{@{Markowitz portfolio theory}@} requires estimating {@{$n$ variance and $n(n - 1) / 2$ covariance}@}, for a total of {@{$n(n+1)/2$ variance‑covariance terms}@}, which becomes {@{infeasible when $n$ is large (e.g., 5 000 assets imply 12.5 million parameters)}@}. {@{The single‑index model and CAPM avoid this}@} by summarising {@{risk with a few factor loadings (only the factor loadings need to be estimated)}@}, thereby reducing {@{estimation error and computational cost}@}.
```

## Example 25 – SIM limitations multi‑paragraph style

**Input:**

```text
The single‑factor assumption may be too restrictive because many macro variables—GDP growth, inflation, interest rates—could influence returns. Introducing additional factors leads to _multi‑factor models_, the foundation of APT. These models retain the linear factor structure while allowing for a richer set of systematic drivers.

In practice, estimating $b_i$ and $\sigma_{\varepsilon,i}$ from historical data can still suffer from sampling noise, but the reduced dimensionality of SIM and CAPM mitigates this problem relative to full covariance estimation. The theory remains useful as a first‑order approximation, with multi‑factor extensions providing greater realism when warranted.
```

**Output:**

```text
{@{The single‑factor assumption}@} may be {@{too restrictive because many macro variables}@}—{@{GDP growth, inflation, interest rates}@}—could {@{influence returns}@}. {@{Introducing additional factors}@} leads to {@{_multi‑factor models_, the foundation of APT}@}. These models retain {@{the linear factor structure}@} while allowing for {@{a richer set of systematic drivers}@}.

In practice, estimating {@{$b_i$ and $\sigma_{\varepsilon,i}$ from historical data}@} can still {@{suffer from sampling noise}@}, but {@{the reduced dimensionality of SIM and CAPM}@} mitigates {@{this problem relative to full covariance estimation}@}. The theory remains {@{useful as a first‑order approximation}@}, with multi‑factor {@{extensions providing greater realism when warranted}@}.
```

## Example 26 – multi‑factor model definition with split clozes

**Input:**

```text
A multiple factors model generalises the single‑index framework by allowing $K$ common factors to explain asset returns. For each security $i$, excess return is written as $$r_{i,t}= \bar r_i+\sum_{k=1}^{K}b_{ik}\,f_{k,t}+u_{i,t},$$ where $\bar r_i$ is the sample mean of $r_i$, $f_{k,t}$ denotes the surprise on factor $k$ (the deviation of that factor from its expectation), and $u_{i,t}$ is an idiosyncratic shock with zero mean. The coefficient $b_{ik}$ is called the factor loading or sensitivity to factor $k$. By construction $\mathbb E[f_{k,t}]=\mathbb E[u_{i,t}]=0$ for all $i$ and $k$.
```

**Output:**

```text
{@{A _multiple factors model_}@} generalises {@{the single‑index framework}@} by {@{allowing $K$ common factors to explain asset returns}@}.  For {@{security $i$, excess return}@} is written as {@{$$r_{i,t}= \bar r_i+\sum_{k=1}^{K}b_{ik}\,f_{k,t}+u_{i,t},$$}@} where $\bar r_i$ is {@{the sample mean of $r_i$}@}, $f_{k,t}$ denotes {@{the surprise on factor $k$ (the deviation of that factor from its expectation)}@}, and $u_{i,t}$ is {@{an idiosyncratic shock with zero mean}@}. {@{The coefficient $b_{ik}$}@} is called {@{the factor loading or sensitivity to factor $k$}@}. By construction {@{$\mathbb E[f_{k,t}]=\mathbb E[u_{i,t}]=0$}@} for {@{all $i$ and $k$}@}.
```

## Example 27 – factor‑mimicking portfolio definition and equation

**Input:**

```text
A factor‑mimicking portfolio is constructed so that its return equals the excess return of a particular factor. For factor $k$ we seek weights $\mathbf w_k=(w_{1},\dots ,w_{N})$ such that $$r_{k,t}=\bar r_k+f_{k,t},\qquad b_{ik}= \sum_{j=1}^{N}w_j\,b_{jk},$$ with $b_{kk}=1$ and $b_{hk}=0$ for $h\neq k$. The expected excess return of the factor portfolio is its factor premium, $r_k-\!r_f$, which rewards investors for bearing that specific systematic risk.

Using data on United Airlines (UA) and Shell (S), suppose their loadings on GDP ($b_{\text{GDP} }$) and inflation ($b_{\text{INF} }$) are known. To build a portfolio that loads only on GDP, solve $$0.3\,w_{UA}+0.057\,w_S =1,\qquad-0.79\,w_{UA}-1.22\,w_S=0 .$$

The solution is $w_{UA}=3.8$, $w_S=-2.46$; the short position in Shell balances the long position in United Airlines. The residual weight on a risk‑free asset is $w_F=1-(w_{UA}+w_S)=-0.34$, indicating that an investor would borrow at the risk‑free rate to finance the factor portfolio.
```

**Output:**

```text
{@{A _factor‑mimicking portfolio_}@} is constructed so that its {@{return equals the excess return of a particular factor}@}.  For {@{factor $k$}@} we seek {@{weights $\mathbf w_k=(w_{1},\dots ,w_{N})$}@} such that {@{$$r_{k,t}=\bar r_k+f_{k,t},\qquad b_{ik}= \sum_{j=1}^{N}w_j\,b_{jk},$$}@} with {@{$b_{kk}=1$}@} and {@{$b_{hk}=0$ for $h\neq k$}@}.  {@{The expected excess return of the factor portfolio}@} is {@{its factor premium, $r_k-\!r_f$}@}, which rewards {@{investors for bearing that specific systematic risk}@}.

Using data on {@{United Airlines (UA) and Shell (S)}@}, suppose their {@{loadings on GDP ($b_{\text{GDP} }$) and inflation ($b_{\text{INF} }$)}@} are known.  {@{To build a portfolio that loads only on GDP, solve}} {@{$$0.3\,w_{UA}+0.057\,w_S =1,\qquad-0.79\,w_{UA}-1.22\,w_S=0 .$$}@}

The solution is {@{$w_{UA}=3.8$, $w_S=-2.46$}@}; {@{the short position in Shell}@} balances {@{the long position in United Airlines}@}.  {@{The residual weight on a risk‑free asset}@} is {@{$w_F=1-(w_{UA}+w_S)=-0.34$}@}, indicating that an investor would {@{borrow at the risk‑free rate to finance the factor portfolio}@}.
```

## Example 28 – interpretation paragraph with component list

**Input:**

```text
Rewriting the multi‑factor equation in excess terms yields $$r_{i,t}-r_f=(\bar r_i-r_f)-\sum_{k=1}^{K}b_{ik}\,(\bar r_k-r_f)+\sum_{k=1}^{K}b_{ik}(f_{k,t}-\!r_F)+u_{i,t}.$$ The right‑hand side contains three components: a constant term $a_i=(\bar r_i-r_f)-\sum_{k}b_{ik}(\bar r_k-r_f)$, the product of each factor’s excess return and its loading on asset $i$, and an idiosyncratic shock $u_{i,t}$.
```

**Output:**

```text
Rewriting {@{the multi‑factor equation in excess terms}@} yields {@{$$r_{i,t}-r_f=(\bar r_i-r_f)-\sum_{k=1}^{K}b_{ik}\,(\bar r_k-r_f)+\sum_{k=1}^{K}b_{ik}(f_{k,t}-\!r_F)+u_{i,t}. $$}@} The right‑hand side {@{contains three components}@}: {@{a constant term $a_i=(\bar r_i-r_f)-\sum_{k}b_{ik}(\bar r_k-r_f)$}@}, {@{the product of each factor’s excess return and its loading on asset $i$}@}, and {@{an idiosyncratic shock $u_{i,t}$}@}.
```

## Example 29 – background sentences and no-free-lunch

**Input:**

```text
Arbitrage Pricing Theory (APT) was introduced by Prof. Stephan Ross in 1976 and gives a different route to the security‑market line.  Its foundation rests on three realistic assumptions: prices follow a factor model; firm‑specific risk can be diversified away; and persistent arbitrage opportunities cannot exist.

The idea of _no free lunch_ means that there is no way to earn a guaranteed profit with zero net investment or risk.  If such an opportunity existed, traders would exploit it until prices adjusted and the advantage disappeared, as illustrated by the anecdote in which a large sum was accidentally dropped on a highway, temporarily creating a fleeting arbitrage that vanished when traffic resumed.
```

**Output:**

```text
{@{Arbitrage Pricing Theory (APT)}@} was introduced by {@{Prof. Stephan Ross in 1976}@} and gives {@{a different route to the security‑market line}@}.  Its foundation rests on {@{three realistic assumptions}@}: prices {@{follow a factor model}@}; firm‑specific {@{risk can be diversified away}@}; and persistent {@{arbitrage opportunities cannot exist}@}.

{@{The idea of _no free lunch_}@} means that {@{there is no way to earn a guaranteed profit with zero net investment or risk}@}.  If {@{such an opportunity existed}@}, traders would {@{exploit it until prices adjusted and the advantage disappeared}@}, as illustrated by the anecdote in which {@{a large sum was accidentally dropped on a highway}@}, temporarily creating {@{a fleeting arbitrage that vanished when traffic resumed}@}.
```

## Example 30 – mispricing numeric scenario

**Input:**

```text
Mispricing leads to arbitrage. Consider a diversified portfolio A with factor loadings $b_{GDP}=0.5, b_{IR}=0.75$. The risk-free rate is $r_F=4\%$, the mean returns of GDP and interest rate are $10\%$ and $12\%$. APT predicts $E[r_A]=0.04+0.5(0.10-0.04)+0.75(0.12-0.04)=13\%$, but market data show a lower return of $12\%$, revealing overpricing so one would want to sell it by setting $x_A = -1$. To eliminate exposure to each systematic factor, one chooses weights equal to the asset’s loadings: $x_k=b_{ik}$, and interest-free weight $x_F$ equal the residual weight such that there is no initial investment: $x_A + x_F + \sum_k x_k = 0$. In that case the portfolio return simplifies to $-a_i$; if $a_i<0$ the arbitrage profit is $-a_i>0$. The construction involves shorting the mispriced asset, long factor-mimicking portfolios, and possibly borrowing or lending at the risk-free rate.
```

**Output:**

```text
{@{Mispricing}@} leads to {@{arbitrage}@}.  Consider {@{a diversified portfolio A}@} with {@{factor loadings $b_{GDP}=0.5, b_{IR}=0.75$}@}.  The risk-free rate is {@{$r_F=4\%$}@}, the mean returns of GDP and interest rate are {@{$10\%$ and $12\%$}@}.  APT predicts {@{$E[r_A]=0.04+0.5(0.10-0.04)+0.75(0.12-0.04)=13\%$}@}, but market data show {@{a lower return of $12\%$}@}, revealing {@{overpricing so one would want to sell it}@} by setting {@{$x_A = -1$}@}.  To eliminate {@{exposure to each systematic factor}@}, one chooses {@{weights equal to the asset’s loadings}@}: {@{$x_k=b_{ik}$}@}, and {@{interest-free weight $x_F$ equal the residual weight}@} such that there is {@{no initial investment}@}: {@{$x_A + x_F + \sum_k x_k = 0$}@}.  In that case the portfolio return simplifies to {@{$-a_i$}@}; if {@{$a_i<0$}@} the arbitrage profit is {@{$-a_i>0$}@}.  The construction involves {@{shorting the mispriced asset}@}, {@{long factor-mimicking portfolios}@}, and possibly {@{borrowing or lending at the risk-free rate}@}.
```

---

## Example 31 – semicolon-separated clauses

**Input:**

```text
Its foundation rests on three realistic assumptions: prices follow a factor model; firm-specific risk can be diversified away; and persistent arbitrage opportunities cannot exist.
```

**Output:**

```text
Its foundation rests on {@{three realistic assumptions}@}: prices {@{follow a factor model}@}; firm-specific {@{risk can be diversified away}@}; and persistent {@{arbitrage opportunities cannot exist}@}.
```

## Example 32 – contrastive conjunction splitting

**Input:**

```text
APT predicts $E[r_A]=13\%$, but market data show a lower return of $12\%$, revealing overpricing.
```

**Output:**

```text
APT predicts {@{$E[r_A]=13\%$}@}, but market data show {@{a lower return of $12\%$}@}, revealing {@{overpricing}@}.
```

## Example 33 – minimal cloze boundaries avoiding leading conjunctions and pronouns

**Input:**

```text
The idea of _no free lunch_ means that there is no way to earn a guaranteed profit with zero net investment or risk.  If such an opportunity existed, traders would exploit it until prices adjusted and the advantage disappeared, as illustrated by the anecdote in which a large sum was accidentally dropped on a highway, temporarily creating a fleeting arbitrage that vanished when traffic resumed.
```

**Output:**

```text
{@{The idea of _no free lunch_}@} means that there is {@{no way to earn a guaranteed profit with zero net investment or risk}@}.  If {@{such an opportunity existed}@}, traders would {@{exploit it until prices adjusted and the advantage disappeared}@}, as illustrated by the anecdote in which {@{a large sum was accidentally dropped on a highway}@}, temporarily creating {@{a fleeting arbitrage that vanished when traffic resumed}@}.
```

## Example 34 – short declarative sentence split subject/predicate (mispricing/arbitrage)

**Input:**

```text
Mispricing leads to arbitrage.
```

**Output:**

```text
{@{Mispricing}@} leads to {@{arbitrage}@}.
```

## Example 35 – articles inside clozes

**Input:**

```text
The market exposure (beta) is measured by b_i.
```

**Output:**

```text
{@{The market exposure (beta)}@} is measured by {@{b_i}@}.
```

---

(Additional entries can be appended; update the index table above with new numbers, descriptions and tags.)
