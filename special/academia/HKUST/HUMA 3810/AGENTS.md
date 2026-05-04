---
aliases:
  - HKUST HUMA 3810 AGENTS
  - HUMA 3810 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/HUMA_3810/AGENTS
  - language/in/English
---

# HUMA 3810 agent instructions

## validator notes

**AGENTS.md flashcard markup rule**: The academic-notes validator flags literal flashcard separator characters (the double-sided and single-sided QA markers) anywhere in this file, even inside backtick spans. To reference flashcard separators in prose, describe them in words (e.g., "double-sided QA pairs" or "two-card format with `@` flanked by two colons on each side") rather than using the actual characters.

## topic-specific notes (Traditional Chinese)

- All four consolidated topic notes (道家概論、老子、莊子、魏晉玄學) must be written entirely in Traditional Chinese (Hong Kong register). Do not mix in English words, phrases, or labels anywhere in the note body or flashcards.
- When English aliases are present for discoverability, include both `language/in/English` and `language/in/中文` tags in frontmatter.
- Use only double-sided QA flashcard pairs (two-card format with `@` flanked by two colons on each side) in all topic-specific notes. Do not use single-sided QA pairs (the single-card format with `@` between one colon and two colons).
- Use Hong Kong Traditional Chinese vocabulary and in-register phrasing throughout (e.g., 「公元前」 not 「BC」, 「課程」 not 「course」 in prose, 「考試」 not 「exam」 in prose).

## content structure

- The four consolidated topic notes (as of 2026-04-05):
  - **道家概論**: merged from "道家與中國哲學的脈絡" + "道家的歷史背景"
  - **老子**: merged from "老子 (person)" + "《老子》重要篇章"
  - **莊子**: merged from "莊子 (person)" + "《莊子》重要篇章"
  - **魏晉玄學**: consolidated and rewritten with substantive content, pure Traditional Chinese
- These are consolidated pages; deepen them as lecture notes and primary-text excerpts arrive. Do not create new overlapping topic-note pages without a strong reason.
- If specific 《老子》 or 《莊子》 chapters are later assigned, add the chapter mapping and annotations to the existing 老子.md or 莊子.md note rather than creating separate chapter pages.

## general course guidance

- Keep the course root and assignment/question scaffolds in English unless a link or quoted title is naturally in Chinese.
- Do not add instructor or TA names, phone numbers, or email addresses to public notes; refer readers to the official syllabus or Canvas for contact details.

## historical validator fixes

**Header-style validation (2026-04-05)**: The academic-notes validator previously flagged CJK headers using `islower()`, which always returns False for non-cased scripts. This was fixed by using `unicodedata.category()` to detect CJK and other scripts (category 'Lo' = other letter), applying lowercase-except-proper-nouns only to cased letters (Lu/Ll). Result: all header-style suppressions removed from HUMA 3810 (4 files cleaned); MATH 2431 and COMP 4211 also pass cleanly.
