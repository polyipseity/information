---
aliases:
  - HKUST MATH 2431 AGENTS
  - MATH 2431 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/AGENTS
  - language/in/English
---

# MATH 2431 agent instructions

General academic-note conventions are in [academic-notes SKILL.md](../../../../.agents/skills/academic-notes/SKILL.md). This file covers MATH 2431-specific guidance.

Honors course: be thorough, rigorous, and precise about probability theory; include clear arguments and derivations where appropriate. Feel free to add more high-quality flashcards than in non-honors courses.

## Files

Do NOT include source files in this `AGENTS.md` file!

- `assignments/`
- `conditional expectation.md`
- `conditional probability.md`
- `continuous distribution.md`
- `convergence and limit theorems.md`
- `cumulative distribution function.md`
- `discrete distribution.md`
- `elementary combinatorics.md`
- `expectation and variance.md`
- `generating function.md`
- `independence.md`
- `joint distribution.md`
- `Lindeberg CLT.md`
- `Markov chain.md`
- `multiple integral.md`
- `Poisson process.md`
- `probability measure.md`
- `questions/**/*.md`
- `random variable.md`
- `Riemann integration.md`
- `sample space.md`
- `sigma-algebra.md`

## Conventions

- Convergence in distribution: $\xrightarrow{d}$ (not $\Rightarrow$).
- Ordinal suffixes: `$x$-th` with hyphen between math and text, e.g. `$n$-th` not `$n$th`.
- Probability LaTeX: `\operatorname{Bin}`, `\operatorname{Cau}`, `\operatorname{Exp}`, `\operatorname{Poi}` etc. for distribution names; `\mathbf 1` for indicators; `\binom{n}{k}` for binomial coefficients; `\lim_{y\uparrow m}` and `\lim_{y\downarrow m}` for left/right CDF limits; `\begin{cases}` with `[2pt]` spacing for piecewise definitions; `\xrightarrow{d}` for convergence in distribution; `\exp\!(` for tight spacing before parentheses.
- When defining $X_n=\alpha X_{n-1}+\sigma Z_n$, give $X_0$'s full distribution (e.g. $X_0\sim N(0,\sigma^2/(1-\alpha^2))$ independent of $\{Z_n\}$) — not just "$X_0$ independent of $\{Z_n\}$."

## Validator

```bash
uv run .agents/skills/academic-notes/check.py \
  "special/academia/HKUST/MATH 2431/conditional expectation.md" \
  "special/academia/HKUST/MATH 2431/conditional probability.md" \
  "special/academia/HKUST/MATH 2431/continuous distribution.md" \
  "special/academia/HKUST/MATH 2431/convergence and limit theorems.md" \
  "special/academia/HKUST/MATH 2431/cumulative distribution function.md" \
  "special/academia/HKUST/MATH 2431/discrete distribution.md" \
  "special/academia/HKUST/MATH 2431/elementary combinatorics.md" \
  "special/academia/HKUST/MATH 2431/expectation and variance.md" \
  "special/academia/HKUST/MATH 2431/generating function.md" \
  "special/academia/HKUST/MATH 2431/independence.md" \
  "special/academia/HKUST/MATH 2431/joint distribution.md" \
  "special/academia/HKUST/MATH 2431/Lindeberg CLT.md" \
  "special/academia/HKUST/MATH 2431/Markov chain.md" \
  "special/academia/HKUST/MATH 2431/multiple integral.md" \
  "special/academia/HKUST/MATH 2431/Poisson process.md" \
  "special/academia/HKUST/MATH 2431/probability measure.md" \
  "special/academia/HKUST/MATH 2431/random variable.md" \
  "special/academia/HKUST/MATH 2431/Riemann integration.md" \
  "special/academia/HKUST/MATH 2431/sample space.md" \
  "special/academia/HKUST/MATH 2431/sigma-algebra.md" \
  "special/academia/HKUST/MATH 2431/questions/final examination.md" \
  "special/academia/HKUST/MATH 2431/questions/mentimeter.md" \
  "special/academia/HKUST/MATH 2431/questions/midterm examination.md" \
  "special/academia/HKUST/MATH 2431/questions/practice midterm examination.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 1.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 10.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 11.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 2.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 3.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 4.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 5.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 6.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 7.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 8.md" \
  "special/academia/HKUST/MATH 2431/questions/problem set 9.md" \
  "special/academia/HKUST/MATH 2431/questions/week 2 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 4 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 5 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 6 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 7 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 8 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 9 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 11 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 12 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 13 tutorial.md" \
  "special/academia/HKUST/MATH 2431/questions/week 14 tutorial.md"
```

Fix all errors before committing.
