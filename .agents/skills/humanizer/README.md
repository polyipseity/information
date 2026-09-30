# Humanizer

A Clawdbot skill that removes common AI-writing patterns while preserving meaning and voice.

`SKILL.md` is the canonical behavior spec. Keep detailed pattern definitions and rewrite rules there.

## Installation

Install via ClawdHub:

```bash
clawdhub install humanizer
```

## Usage

Ask your agent to humanize text:

```text
Please humanize this text: [your text]
```

Or invoke directly when editing documents.

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.

### Key Insight

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## Patterns

The skill detects 24 patterns across five groups:

- Content
- Language and grammar
- Style
- Communication
- Filler and hedging

For the full numbered list with before/after examples, see `SKILL.md`.

## Example

__Before (AI-sounding):__
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently.

__After (Humanized):__
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## License

MIT
