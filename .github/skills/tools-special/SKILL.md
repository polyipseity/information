---
name: tools-special
description: Academic LMS converters and course management tools in tools/special/.
---

# tools/special Workflows

Use this skill when working with academic LMS (Learning Management System) converters and course catalog management tools.

## What tools/special contains

The `tools/special/` directory contains specialized scripts for academic workflows:

1. **`convert Canvas submission.py`**: Converts Canvas LMS exports to YAML frontmatter
2. **`convert HKUST Zinc submission.py`**: Converts HKUST Zinc submission data to YAML
3. **`get HKUST undergraduate courses.py`**: Fetches HKUST course catalog and exports to CSV

## When to use

- Converting LMS exports (Canvas, HKUST Zinc) to structured YAML for coursework notes
- Fetching course catalogs from university APIs
- Organizing course materials in `special/academia/`
- Maintaining `index.md` files with course listings

## Workflows

### Convert Canvas submission to YAML

**Purpose**: Parse Canvas LMS submission exports and generate YAML frontmatter for course notes.

**Input**: Canvas export file (format depends on Canvas API/export structure)

**Output**: YAML frontmatter with:

- Course code and title
- Semester and year tags
- Assignment details (due dates, points, status)
- Instructor information

**Command**: `uv run -m tools.special."convert Canvas submission" <input_file>`

**Example output**:

```yaml
---
aliases: [COMP 2012]
tags: [2023-fall, coursework]
course: COMP 2012
title: Object-Oriented Programming and Data Structures
credits: 4
instructor: Prof. Example
---
```

### Convert HKUST Zinc submission to YAML

**Purpose**: Parse HKUST Zinc (HKUST's submission system) exports into structured YAML.

**Input**: Zinc submission data (JSON or other format from HKUST Zinc API)

**Output**: Similar YAML structure as Canvas converter, adapted for HKUST formats

**Command**: `uv run -m tools.special."convert HKUST Zinc submission" <input_file>`

### Fetch HKUST course catalog

**Purpose**: Retrieve current HKUST undergraduate course listings from university systems.

**Output**: CSV with columns:

- Course code (e.g., COMP 2012, ACCT 2010)
- Course title
- Credits
- Department/school
- Prerequisites
- Semesters offered

**Command**: `uv run -m tools.special."get HKUST undergraduate courses" -o courses.csv`

**Use case**: Update `special/academia/HKUST/index.md` with current course offerings

## Integration with special/academia/

These tools support the academic note organization in `special/academia/`:

```text
special/academia/
├── HKUST/
│   ├── index.md          # Course listings by semester (maintained with converters)
│   ├── reviews.md
│   └── COMP 2012/        # Individual course directories
│       ├── index.md
│       └── *.md          # Lecture notes, assignments
```

### Maintaining index.md

After converting LMS exports or fetching course catalogs:

1. Extract course metadata (code, title, semester, credits)
2. Update `special/academia/<Institution>/index.md` with new course entries
3. Organize by semester/year (most recent first)
4. Include status tags (`taken`, `not-taken`, `transferred`, `auditing`)

**Example index.md structure**:

```markdown
# HKUST Courses

## 2024 Fall
- [COMP 4901](COMP 4901/index.md) — Final Year Project (6 credits, taken)
- [COMP 4111](COMP 4111/index.md) — Software Engineering (3 credits, taken)

## 2024 Spring
- [COMP 3711](COMP 3711/index.md) — Design and Analysis of Algorithms (3 credits, taken)
```

## CLI stability requirements

**Critical**: These tools have established CLI interfaces; preserve:

- Argument names and formats
- YAML output schemas (field names, structure)
- CSV column names for course list exports
- Expected input file formats

If changes are needed, ask user for permission first.

## Best practices

- **Batch processing**: Convert multiple LMS exports at once when organizing a full semester
- **Validation**: Check generated YAML for completeness before committing
- **Consistency**: Follow institution-specific conventions (HKUST vs. Korea University course code formats)
- **Index updates**: Keep `index.md` current when adding new courses or materials
- **Cross-references**: Link between courses, prerequisites, or related `general/` encyclopedia entries

## When to ask for help

- If LMS export format has changed and converter fails, consult user
- If new institution converters are needed, discuss requirements with user
- If course catalog API changes, ask user to update fetcher script

## Common issues

1. **LMS format changes**: Canvas/Zinc APIs may update; converters may need adjustments
2. **Missing metadata**: Some exports may lack instructor, credits, or prerequisite info
3. **Encoding issues**: Handle UTF-8 properly for international course titles
4. **Duplicate courses**: Check for existing course directories before creating new ones
