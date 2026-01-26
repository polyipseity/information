---
name: LaTeX preamble
description: Editing guardrails for preamble.sty
applyTo: "preamble.sty"
---

# LaTeX Preamble Guidelines

- Keep existing macros stable; they may be referenced across documents. Avoid renaming commands like `\argmax`, `\argmin`, `\oiiint`, `\oiint`.
- Do not introduce package dependencies or side effects; this file is intended to be lightweight and standalone.
- Preserve math formatting (`\mathop`, `\mathrm`, `\mathllap`) and avoid changing spacing tweaks unless fixing a typesetting bug with evidence.
- Use UTF-8 and maintain minimal footprint—no global layout changes.
