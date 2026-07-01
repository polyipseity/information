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

__AGENTS.md flashcard markup rule__: The academic-notes validator flags literal flashcard separator characters (the double-sided and single-sided QA markers) anywhere in this file, even inside backtick spans. To reference flashcard separators in prose, describe them in words (e.g., "double-sided QA pairs" or "two-card format with `@` flanked by two colons on each side") rather than using the actual characters.

## topic-specific notes (Traditional Chinese)

- __請使用繁體中文和香港就地用語。__ All four consolidated topic notes (道家概論、老子、莊子、魏晉玄學) must be written entirely in Traditional Chinese (Hong Kong register). Do not mix in English words, phrases, or labels anywhere in the note body or flashcards.
- 如需標註字音，請統一使用粵語讀音；可用「音某字」或粵拼（Jyutping）標示。請勿使用普通話拼音（漢語拼音）作為主標註。
- When English aliases are present for discoverability, include both `language/in/English` and `language/in/中文` tags in frontmatter.
- Use only double-sided QA flashcard pairs (two-card format with `@` flanked by two colons on each side) in all topic-specific notes. Do not use single-sided QA pairs (the single-card format with `@` between one colon and two colons).
- Use Hong Kong Traditional Chinese vocabulary and in-register phrasing throughout (e.g., 「公元前」 not 「BC」, 「課程」 not 「course」 in prose, 「考試」 not 「exam」 in prose).
- 《老子》與《莊子》筆記宜長期維護三類索引：章節╱篇章索引、關鍵引句索引（含來源章名章號）、起首字提示背誦索引；新增引句時優先補進索引並建立語義關聯。

## content structure

- The four consolidated topic notes (as of 2026-04-05):
  - __道家概論__: merged from "道家與中國哲學的脈絡" + "道家的歷史背景"
  - __老子__: merged from "老子 (person)" + "《老子》重要篇章"
  - __莊子__: merged from "莊子 (person)" + "《莊子》重要篇章"
  - __魏晉玄學__: consolidated and rewritten with substantive content, pure Traditional Chinese
- These are consolidated pages; deepen them as lecture notes and primary-text excerpts arrive. Do not create new overlapping topic-note pages without a strong reason.
- If specific 《老子》 or 《莊子》 chapters are later assigned, add the chapter mapping and annotations to the existing 老子.md or 莊子.md note rather than creating separate chapter pages.
- 索引與背誦卡可集中於單一輔助頁（現用：`老莊索引與背誦卡.md`），以保持 `老子.md`、`莊子.md` 主文流暢；主文仍以講解內容為主。

## general course guidance

- Prefer Hong Kong Traditional Chinese in `index.md` lecture prose and flashcards; avoid mixing English and Chinese in the same sentence when a clear Chinese term exists.
- In course-root pages, keep unavoidable proper nouns or system labels (for example Canvas, ISO datetime literals, and existing fixed course codes) as-is, but local explanatory text should remain in Hong Kong Traditional Chinese.
- Do not add instructor or TA names, phone numbers, or email addresses to public notes; refer readers to the official syllabus or Canvas for contact details.

## transcript alignment notes (2026-05)

- When aligning `index.md` with `.tmp/` transcripts, prioritize transcript evidence for the specific date over placeholder status text in the index.
- If a class is listed as "no class" but a transcript exists and contains full lecture content, update the lecture entry with topic/notes/links instead of keeping only status.
- For STT transcripts, avoid over-committing to noisy single-word details unless corroborated by lecture context and the target note page (e.g., avoid adding secondary anecdotes not clearly spoken in that lecture).
- Keep `index.md` week topics synchronized with the section anchors actually present in `老子.md` and `莊子.md`; prefer anchored links (e.g., `#第一章道體論`) over file-level links where possible.
- Course logistics announced at lecture openings/closings (draft deadlines, exam format, attendance reminders, AI policy) should be captured as two-sided QA flashcards in `index.md`.

## historical validator fixes

__Header-style validation (2026-04-05)__: The academic-notes validator previously flagged CJK headers using `islower()`, which always returns False for non-cased scripts. This was fixed by using `unicodedata.category()` to detect CJK and other scripts (category 'Lo' = other letter), applying lowercase-except-proper-nouns only to cased letters (Lu/Ll). Result: all header-style suppressions removed from HUMA 3810 (4 files cleaned); MATH 2431 and COMP 4211 also pass cleanly.
