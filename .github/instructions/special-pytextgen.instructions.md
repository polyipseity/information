---
name: Special — pytextgen patterns
description: pytextgen usage patterns and regeneration guidance for `special/` content
applyTo: "special/**/*.md"
---

# Special — pytextgen patterns

## pytextgen Usage Patterns in `special/`

Different content types in `special/` use pytextgen differently and have established patterns:

1. Sequential lists (business frameworks, technical guides):

```python
return await memorize_seq(
  __env__.cwf_sects("id1", "id2"),
  items,
)
```

1. Mapped content (key-value pairs):

```python
return await memorize_map(
  __env__.cwf_sects("id1", "id2"),
  items,
)
```

1. Classical texts with annotations:

```python
notes = Notes()
text = gen.TextCode.compile(
  f"""..."""
)
return (text, notes)
```

1. Custom formatting (questions, specialized layouts):

   - Strategy/solution pairs with `:@:` separator
   - Nested cloze deletions with `{@{ }@}`
   - Hard-marked terms with `hard(...)` wrapper

**Regeneration**: Use `uv run -m init generate <path>` after editing source data to regenerate pytextgen blocks.
