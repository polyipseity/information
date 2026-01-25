---
name: tools-templates
description: Note scaffolding templates and pytextgen fence generators in tools/templates/.
---
# tools/templates Workflows

Use this skill when scaffolding new notes, creating pytextgen sections, or using pre-built templates for knowledge base content.

## What tools/templates contains

The `tools/templates/` directory contains scripts for scaffolding new content:

1. **`new wiki page.py`**: Generate YAML frontmatter + Wikipedia link template for encyclopedia notes
2. **`pytextgen generate *.md`**: Templates for common pytextgen fence patterns

## When to use

- Creating new encyclopedia notes with proper frontmatter
- Scaffolding pytextgen sections (flashcards, code blocks, data exports)
- Ensuring consistent YAML structure across notes
- Quick-starting new knowledge base entries

## Workflows

### Scaffold a new wiki-sourced note

**Purpose**: Create a new encyclopedia note with pre-filled frontmatter and Wikipedia attribution.

**Command**: `python -m "templates.new wiki page"`

**Workflow**:
1. Script prompts for article name (or reads from argument)
2. Generates YAML frontmatter template:
   ```yaml
   ---
   aliases: []
   tags: [flashcard/active, language/in/English]
   ---
   ```
3. Adds Wikipedia source link comment:
   ```markdown
   <!-- Source: https://en.wikipedia.org/wiki/Article_Name -->
   ```
4. Copies template to clipboard
5. User pastes into new file in `general/` (or `special/` if specialized)

**Next steps**:
- Use `python -m "convert wiki"` to ingest Wikipedia HTML below the template
- Add content manually or from other sources
- Update `aliases` and `tags` as needed

### Create pytextgen flashcard section

**Template**: `tools/templates/pytextgen generate flashcards.md`

**Purpose**: Scaffold a new flashcard generation section in an existing note.

**Content** (example):
```markdown
## Flashcards

<!--pytextgen generate section="flashcards-main" format="cloze"-->
<!--/pytextgen-->
```

**Usage**:
1. Copy template content from `tools/templates/pytextgen generate flashcards.md`
2. Paste into target note
3. Update section ID (`flashcards-main` → unique identifier)
4. Add cloze markup to note content: `{@{ hidden text }@}`, `::@::`, `:@:`
5. Run `python -m init generate <file>` to populate flashcards

### Create pytextgen code block section

**Template**: `tools/templates/pytextgen generate code.md`

**Purpose**: Scaffold a Python code block that generates Markdown content.

**Content** (example):
````markdown
```python
# pytextgen generate module="data.courses" function="generate_course_list"

def generate_course_list():
    courses = [...]
    return export_seq(courses)
```
````

**Usage**:
1. Copy template from `tools/templates/pytextgen generate code.md`
2. Paste into target note
3. Update module/function references
4. Implement generation logic
5. Run `python -m init generate <file>` to execute and insert output

### Other templates

Additional templates may exist for:
- Data export fences (JSON/CSV → Markdown tables)
- Cross-reference generators (link indexes, backreferences)
- Structured list generators (course lists, bibliography)

Check `tools/templates/` directory for all available templates.

## Template conventions

### YAML frontmatter

**Standard fields**:
- `aliases`: Alternative names for the note (list)
- `tags`: Categories and metadata (list)
  - `flashcard/active`: Enable flashcard generation
  - `language/in/English`: Note language (or `language/in/Korean`, etc.)
  - Semester tags: `2023-fall`, `2024-spring`
  - Subject tags: `coursework`, `tutorial`, `business`

**Example**:
```yaml
---
aliases: [GDP, Gross Domestic Product]
tags: [flashcard/active, language/in/English, economics]
---
```

### pytextgen fence templates

**Critical rules** (inherited from pytextgen conventions):
- Do NOT modify `# pytextgen generate ...` comment lines in templates
- Do NOT change fence delimiters (triple backticks + language)
- Preserve section IDs in HTML comments (`<!--pytextgen generate section="id"-->`)
- Keep `return export_seq(...)` signatures intact

**Placeholder protection**:
- Templates may use `{{placeholder}}` or `<REPLACE_ME>` for user-editable parts
- Replace placeholders before running generation
- Never commit templates with unresolved placeholders into content notes

## Integration with other workflows

### wiki-ingestion workflow

1. Run `python -m "templates.new wiki page"` to create frontmatter
2. Paste template into new file `general/Article Name.md`
3. Run `python -m "convert wiki"` to ingest Wikipedia HTML
4. Content is appended below frontmatter
5. Run `python -m init generate <file>` to create flashcards from cloze markup

### Academic coursework workflow

1. Use LMS converters (`tools-special` skill) to generate course YAML
2. Use templates to scaffold course `index.md` with sections
3. Add pytextgen fences for assignment lists, grade tables
4. Regenerate with `python -m init generate`

### Custom content generation

1. Copy appropriate pytextgen template
2. Implement Python function or reference existing module
3. Update fence comment with correct module/function path
4. Test generation with `python -m init generate <file>`
5. Debug any errors (see `pytextgen` skill for troubleshooting)

## Best practices

- **Consistent frontmatter**: Use templates to ensure YAML structure matches conventions
- **Template versioning**: If templates change, update existing notes gradually
- **Section IDs**: Use descriptive, unique IDs for pytextgen sections (e.g., `flashcards-chapter-1`)
- **Template testing**: Test new templates on dummy files before using in production notes
- **Documentation**: Comment template files with usage instructions

## When to ask for help

- If template placeholders are unclear, ask user for guidance
- If new template patterns are needed, discuss requirements with user
- If pytextgen fence syntax is complex, refer to `pytextgen` skill

## Common issues

1. **Placeholder leakage**: Forgot to replace `{{placeholder}}` before generation
2. **Section ID collisions**: Multiple pytextgen sections with same ID in one file
3. **Fence syntax errors**: Broken fence delimiters or comment lines
4. **Module import errors**: Python module paths incorrect in fence comments

## Editing guidelines for tools/templates/**

When editing files in `tools/templates/`:

- **Preserve placeholder tokens**: Keep tokens like `(name)`, `(Wikipedia name)`, `(tag name)` intact; do not hardcode example values
- **Maintain clipboard-copy behavior**: Python templates like `new wiki page.py` should keep clipboard copying and normalization/replacement maps intact unless fixing bugs
- **Keep pytextgen fence syntax**: Never modify template fences/comments (`# pytextgen generate ...`, `<!--pytextgen generate section="..."-->`)
- **Avoid filename changes**: Downstream scripts expect specific file names and extensions; changing them may break workflows
- **Use UTF-8 encoding**: Keep newline handling as-is and avoid rewrapping markdown bodies in templates
- **Document changes**: If template structure changes, note impact on existing notes and update documentation


