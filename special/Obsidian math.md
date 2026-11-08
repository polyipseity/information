---
aliases:
  - Obsidian math
  - Obsidian math macros
tags:
  - software/Obsidian
  - language/in/English
---

# Obsidian math

Obsidian renders note math with MathJax, so a note may use every macro MathJax defines. The vault's preamble, `.obsidian/plugins/obsidian-latex/preamble.sty`, adds whatever MathJax lacks, but only while the preamble loads; see [migrating to Shared TeX Preamble](#migrating%20to%20shared%20tex%20preamble) for its current state. Names MathJax already supplies stay out of the preamble, and the rest are polyfilled.

## native macros

MathJax 4.1.3 (the MathJax that Obsidian 1.15.0 bundles) already supplies these, so `preamble.sty` does not define them:

- `\AA`: the ångström unit
- `\nobreak`: forbid a line break at that point
- `\oiint`: integral over a closed surface
- `\oiiint`: integral over a closed volume
- `\bra`, `\ket`: Dirac bra and ket
- `\cancel`: strike through a term
- `\ce`: chemical formula, as in mhchem
- `\textcolor`: coloured text

The four core names are recorded as native in the header comment of `preamble.sty`. The five extension names are autoloaded: they come from MathJax's own extension set (bra-ket, cancel, chemistry, colour) and are loaded on first use, so defining them in the preamble would only shadow the upstream definition.

## polyfills

These names are not in MathJax 4.1.3, so `preamble.sty` defines them:

- `\Eta`: `\mathrm{H}` (capital eta is the upright letter H)
- `\argmax`: `\mathop{\mathrm{arg\,max}}`
- `\argmin`: `\mathop{\mathrm{arg\,min}}`
- `\Z`: `\mathbb{Z}`
- `\degree`: `{}^\circ`
- `\texteuro`: `\text{€}`

## preamble syntax

__Why `\def`__: `\def` replaces whatever the name currently means, including a definition an extension installed, so a polyfill wins over a partial or differing upstream definition. `\newcommand` refuses to define a name that already exists, and `\renewcommand` fails on a name that nothing has defined yet, so neither command covers both cases on its own.

__Why `\newcommand \Name` fails in MathJax 4__: MathJax parses the arguments of `\newcommand` itself and expects the brace form `\newcommand{\Name}{...}`. The space-separated form, which LaTeX accepts, does not define the macro here, so the name stays undefined and every use of it renders as an error. This vault's preamble used that form before it was rewritten for MathJax 4; the current file uses `\def` throughout.

__Why redefining a native name with `\newcommand` fails__: `\newcommand` only defines a name that does not exist yet, so `\newcommand{\oiint}{...}` stops at MathJax's own `\oiint` with an "already defined" error and the definition is rejected. That is why no native name from the list above appears in the preamble as a definition, and why an overriding polyfill has to use `\def`.

## migrating to Shared TeX Preamble

Extended MathJax 0.4.1 is a MathJax 3 plugin: its `main.js` calls `obsidian.loadMathJax()` and then hands the preamble text to `MathJax.tex2chtml`, both MathJax 3 APIs. It is MathJax 3 only and does not load on Obsidian 1.15.0, so the preamble is currently not read at all and every polyfill above renders as an error.

Shared TeX Preamble 1.1.2 reads the same macro file on MathJax 4. These steps are done by hand in the Obsidian UI, not by anything in this repository:

1. Install Shared TeX Preamble 1.1.2.
2. Set its macro file to `.obsidian/plugins/obsidian-latex/preamble.sty`.
3. Disable Extended MathJax.
4. Restart Obsidian.

`.obsidian/community-plugins.json` still lists `obsidian-latex` until the user saves that plugin change and commits the file; the macro file itself keeps its path, so no note has to change.

## audit

```sh
uv run python -m scripts.audit_math_macros
```

The audit reads the math in `general`, `special`, and `self`, then prints each cataloged polyfill and typo with its definition, its file count, and up to three example paths. `--all` adds every macro it found, so a name missing from the polyfill catalog shows up there; pass paths to audit a subset.
