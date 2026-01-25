---
name: special
description: Conventions for all Markdown content and tools under special/
applyTo: "special/**/*.md, special/**/*.py"
---

# Special Content Instructions

The `special/` directory contains specialized knowledge including coursework, tutorials, language texts, business frameworks, technical documentation, command libraries, and other curated learning materials. Unlike `general/` (Wikipedia articles), `special/` content comes from diverse sources: academic coursework, online courses, personal notes, tutorials, reference documentation, and practical guides.

## Directory Structure Overview

```
special/
├── academia/                       # Academic coursework by institution
│   ├── HKUST/                     # Hong Kong University of Science and Technology
│   ├── Korea University/          # Korea University courses
│   ├── Pusan National University/ # Pusan National University courses
│   ├── USFQ/                      # Universidad San Francisco de Quito
│   └── Yonsei University/         # Yonsei University courses
├── audio signal processing/       # Audio signal processing course materials
├── C/                             # C programming language reference
├── C++/                           # C++ programming language reference
├── MySQL/                         # MySQL database reference
├── NumPy/                         # NumPy library documentation
├── language acquisition/          # Language learning materials
│   ├── English/                   # English language resources
│   └── 中文/                      # Chinese language resources
├── questions/                     # Timestamped Q&A entries
├── examples/                      # Worked examples and case studies
├── attachments/                   # Supporting files (images, PDFs, etc.)
├── nutritional information/       # Nutritional data and supplements
├── [Business frameworks].md       # MBA/strategy frameworks (individual files)
├── [Technical guides].md          # Usage guides for tools and software
├── [Command/regex libraries].md   # Reusable command and regex patterns
└── [Classical Chinese texts].md   # Traditional Chinese literary works
```

## Scope and Future Expansion

**Important note**: The `special/` directory is still expanding and may include more diverse content types in the future beyond those enumerated in this document. When encountering new content types not explicitly covered by these instructions, apply the following principles:

1. **Extrapolate existing rules**: The conventions described in this document (frontmatter structure, cloze markup, pytextgen patterns, cross-references, link formatting) apply to all content types in `special/`, whether currently documented or not
2. **Maintain consistency**: New content should follow the same overall structure, tagging, and markdown principles as existing materials
3. **Adapt domain-specific guidelines**: Apply the domain-specific guidance most similar to the new content type (e.g., use programming reference guidelines for new language documentation, academia guidelines for new course materials)
4. **Preserve metadata schemas**: Maintain stable YAML frontmatter structures and tag naming conventions for any new content
5. **When in doubt**: Consult this document's general principles and existing content patterns as reference guides

Examples of potential future content: additional programming languages, specialized technical tutorials, domain-specific frameworks, curated research materials, domain-specific Q&A collections, etc.

## Content Organization by Type

### 1. Academic Coursework (`academia/`)

Academic courses organized hierarchically by institution, semester, and course code:

```
special/academia/
├── <Institution>/              # e.g., HKUST, Korea University
│   ├── index.md               # Course listings by semester/year
│   ├── reviews.md             # Institution-specific reviews and notes
│   └── <Course Code>/         # e.g., COMP 2012, ACCT 2010, ISC213
│       ├── index.md           # Course overview, schedule, assessments
│       ├── *.md               # Lecture notes, readings, assignments
│       └── [subdirs]          # Topic-specific subdirectories if needed
```

**Institutions included**:
- **HKUST**: Hong Kong University of Science and Technology (largest collection: 40+ courses in COMP, ACCT, BIEN, CIVL, DASC, ECON, ELEC, ENGG, ESST, FINA, GNED, ISDN, ISOM, LANG, MATH, PHYS, TEMG, and Robotics Team)
- **Korea University**: ISC213 (Korean language/culture course)
- **Pusan National University**: IT3000504 (IT-related course)
- **USFQ**: Universidad San Francisco de Quito courses
- **Yonsei University**: Yonsei University courses

**Course metadata** (in YAML frontmatter and `index.md`):
- **Aliases**: Multiple name variants (e.g., `COMP 2012`, `COMP2012`, `HKUST COMP 2012`, full course name)
- **Tags**: `flashcard/active/special/academia/<institution>/<course_code>`, `function/index`, `language/in/English`
- **Semester/year**: Listed in `index.md` (e.g., `2023 fall`, `2024 spring`, `2023 winter`)
- **Credits**: Parenthetical after course title (e.g., `(4 credits)`)
- **Status**: `taken`, `not-taken`, `transferred`, or status markers in `index.md`
- **Content organization**: Often includes "week X lecture Y" sections or topic-based sections
- **Assessments**: Separate section for midterm/final examination reports and reflections

**Index maintenance**:
- **Institution-level `index.md`**: Lists all courses by semester (most recent first)
- **Course-level `index.md`**: Overview, teaching order, week-by-week breakdown, assessments
- **Cross-references**: Link to related `general/` articles for concepts (e.g., `[most vexing parse](../../../../general/most%20vexing%20parse.md)`)
- **Academic converters** in `tools/special/` help maintain these indexes (see [§ Tools](#tools-in-toolsspecial))

### 2. Online Course Materials

Self-contained course materials from MOOCs and online learning platforms:

**`audio signal processing/`**: Complete course on audio signal processing
- **Structure**: 10 modules with hierarchical index showing learning order
- **Content types**: 
  - Conceptual notes (signal mathematics, discrete Fourier transform, STFT, etc.)
  - Tool usage guides (Audacity, SonicVisualiser, sms-tools, Freesound)
  - Programming guides (Python/NumPy for signal processing, Essentia library)
- **Index format**: Module-by-module breakdown with subsections linking to specific topics
- **Source attribution**: References Coursera course "Audio Signal Processing for Music Applications"
- **Cross-references**: Links to related `general/` articles (e.g., `[Music Technology Group](../../general/Music%20Technology%20Group.md)`)

### 3. Programming Language References

Technical documentation for programming languages and libraries:

**`C/`**: C standard library references
- **Subdirectories**: `date and time utilities/`, `file input_output/`, `numerics/`, `strings library/`
- **Top-level files**: Overview files like `date and time utilities.md`
- **Cross-references**: Links to `general/` C documentation (e.g., `[C date and time functions](../../general/C%20date%20and%20time%20functions.md)`)

**`C++/`**: C++ language features
- **Files**: `array.md`, `implicit conversion.md`, `lambda.md`, `overload resolution.md`
- **Focus**: Specific language features and gotchas

**`MySQL/`**: MySQL database reference
- **Structure**: `index.md` + topical files (`data types.md`, `functions and operators.md`, `statements.md`)
- **Source**: Coursera "Introduction to Structured Query Language (SQL)" course
- **Cross-reference**: Links to `[general/MySQL](../../general/MySQL.md)`

**`NumPy/`**: NumPy library documentation
- **Structure**: `index.md` + `user guide/` subdirectory
- **Version-tagged**: `version/NumPy/2/1` in frontmatter
- **Licensing**: Includes `LICENSE.txt` from upstream
- **Source**: <https://numpy.org/doc/2.1/index.html>

### 4. Language Acquisition Materials

**`language acquisition/`**: Foreign language learning resources

**`language acquisition/English/`**:
- `difficult-to-spell words.md`: Spelling reference

**`language acquisition/中文/`** (Chinese):
- `倉頡輸入法難字.md`: Difficult characters for Cangjie input method
- `简化字总表.md`: Table of simplified Chinese characters

**`International Phonetic Alphabet.md`**: Comprehensive IPA reference
- **Structure**: Phonetic symbols with audio examples (linked to `archives/Wikimedia Commons/`)
- **Content**: Official IPA chart image, detailed help for each phonetic symbol
- **Cross-references**: Links to individual phonetic articles in `general/`
- **Tags**: `flashcard/active/special/language_acquisition/International_Phonetic_Alphabet`

### 5. Business and Strategy Frameworks

Root-level files containing MBA-style frameworks and business strategy tools:

**Strategy frameworks**:
- `blue ocean strategy.md`: Red ocean vs. blue ocean, blue ocean shift process (understand "as-is", imagine "to be", create "gap"), strategy canvas
- `5-step persuasive selling.md`: Persuasive selling framework (background, big idea, how it works, key benefits/risks, next step)
- `business model canvas.md`: 9 building blocks of business model (comprehensive framework)
- `buyer utility map.md`: Customer utility analysis
- `value proposition canvas.md`: Value proposition design
- `market segmentation.md`: Segmentation strategies
- `profitability framework.md`: Profitability analysis

**Business analysis tools**:
- `IBM prioritization grid.md`: Prioritization matrix
- `PPTG change impact framework.md`: Change impact assessment
- `lift chart.md`: Model evaluation chart

**Personal documents**:
- `cover letter.md`: Cover letter writing guide (format, use cases, structure)
- `résumé.md`: Resume/CV writing guide
- `name tag.md`: Name tag conventions

### 6. Technical Usage Guides

Root-level usage documentation for software tools:

- `GNU Debugger.md`: GDB command reference (common commands, abbreviations)
- `Vim usage.md`: Vim editor commands (autocomplete, motion, patterns, write/quit)
- `Microsoft Windows usage.md`: Windows-specific usage tips
- `Blender usage.md`: Blender 3D software usage
- `Analytic Solver usage.md`: Analytic Solver tool usage

**Cross-references**: Many link to `general/` articles (e.g., `[GNU Debugger](../general/GNU%20Debugger.md)`)

### 7. Command and Regex Libraries

Reusable command patterns and regex snippets:

**`command library.md`**: Shell command recipes organized by tool
- **Tools covered**: ExifTool, FFmpeg, GhostScript, Git, ImageMagick, yt-dlp, etc.
- **Format**: Command templates with parameter placeholders (e.g., `$input_`, `$output`)
- **Use cases**: Copy metadata, combine audio/video, measure loudness, batch operations, etc.

**`regex library.md`**: Regular expression patterns
- **Examples**: Unicode line boundaries pattern
- **Format**: Code block + description + regex repetition for flashcards

### 8. Classical Chinese Texts

Traditional Chinese literary works with full text and annotations:

**Files** (by title in Chinese):
- `六國論.md` (On the Six States) by 蘇洵 (Su Xun)
- `出師表.md` (Memorial on Dispatching the Army)
- `勸學（節錄）.md` (Encouraging Learning, Excerpt)
- `名言警句.md` (Famous sayings and aphorisms)
- `始得西山宴遊記.md` (Record of a Banquet and Excursion to Xishan)
- `孝.md` (Filial Piety)
- `山居秋暝.md` (Autumn Evening in the Mountain Dwelling)
- `岳陽樓記.md` (Record of Yueyang Tower)
- `師說.md` (On Teachers)
- `廉頗藺相如列傳（節錄）.md` (Biographies of Lian Po and Lin Xiangru, Excerpt)
- `念奴嬌·赤壁懷古.md` (Niannu Jiao - Memories at Red Cliff)
- `指定文言經典學習材料篇目.md` (Index of designated classical Chinese texts)
- `月下獨酌（其一）.md` (Drinking Alone Under the Moon, Part 1)
- `登樓.md` (Ascending the Tower)
- `聲聲慢·秋情.md` (Sheng Sheng Man - Autumn Sentiment)
- `論仁.md` (On Benevolence)
- `論君子.md` (On the Noble Person)
- `論孝.md` (On Filial Piety)
- `逍遙遊（節錄）.md` (Free and Easy Wandering, Excerpt)
- `青玉案·元夕.md` (Qingyu An - Lantern Festival Night)
- `魚我所欲也.md` (Fish is What I Desire)

**Structure**:
- **Frontmatter**: Author (`by/<author>`), language tags (`language/for/中文`, `language/in/中文`), flashcard tags (often `flashcard/archive/special/<title>`)
- **Content**: Full classical Chinese text with embedded notes using `notes.embed('term', 'explanation')` syntax
- **pytextgen integration**: Uses `gen.TextCode.compile()` for structured memorization of classical texts paragraph by paragraph
- **Notes system**: Inline annotations for difficult characters, phrases, and literary devices

### 9. Questions Collection

**`questions/`**: Timestamped question-answer pairs, primarily mathematical problems

**Naming convention**: ISO 8601 timestamps with timezone (e.g., `2023-08-06T225216.434+0800.md`)

**Structure**:
- **Frontmatter**: `date/<year>/<month>/<day>`, `question/<domain>/<subdomain>`, flashcard tags
- **Content sections**: Problem statement, strategy (thinking process), solution (detailed work)
- **Flashcard format**: Strategy as cloze/QA format using `:@:` for active recall
- **Subdirectory**: `attachments/` for supporting files

**Example topics**: Limits, calculus, integration, series convergence, trigonometric substitution, matrix operations, etc.

**Cross-references**: Some questions reference concepts in `general/` or `special/academia/` course materials

### 10. Worked Examples

**`examples/`**: Detailed worked examples and case studies

**Current examples**:
- `inventing the air fryer from observing French fries.md`: Innovation case study
- Additional examples in subdirectory (single file observed)

**Purpose**: Illustrative examples for concepts, problem-solving techniques, or creative thinking

### 11. Mathematical Content

Root-level mathematical notes not fitting into `general/` or `academia/`:

- `constant of integration.md`: Integration concepts
- `integration by substitution.md`: Calculus technique
- `linear—rotational motion analogy.md`: Physics/mechanics analogy
- `list of mathematical pathologies.md`: Counterexamples and edge cases

### 12. Miscellaneous Specialized Content

**Astronomy**:
- `list of Nobel laureates in Astronomy.md`: List of laureates

**Design thinking**:
- `d.school design thinking bootleg.md`: Stanford d.school design thinking guide

**Education**:
- `examination keys - HKDSE liberal studies.md`: Hong Kong exam reference

**Nutritional information**:
- `nutritional information/` subdirectory
  - `Redoxon Triple Action.md`: Supplement information
  - `VÖOST Collagen Formation.md`: Supplement information

**Attachments**:
- `attachments/` subdirectory: Supporting files like images, PDFs, and specialized scripts
  - Example: `GhostScript remove metadata pdfmark.txt`

## Markdown Conventions

Apply the same conventions as `general/` notes, with domain-specific adaptations:

### Common conventions

- **Frontmatter**: YAML with `aliases`, `tags`, `language/in/<lang>` (or `language/for/<lang>` for language texts)
- **Cloze markup**: Preserve `{@{ ... }@}`, `::@::`, and `:@:` exactly as-is for flashcard generation
- **pytextgen fences**: Do not modify `# pytextgen generate ...` comments or `return export_seq(...)` signatures
  - Academic notes often use `await memorize_seq()` for ordered content
  - Classical Chinese texts use `gen.TextCode.compile()` with embedded notes
- **Links**: Relative paths with `%20` encoding for spaces
  - Cross-references to `general/`: `[topic](../../general/topic.md)` or similar relative paths
  - Internal links: `[section](#section-header)` for same-file references
- **Math**: KaTeX `$inline$` and `$$display$$` formats (heavily used in questions, mathematical notes)
- **Media**: Reference files in `archives/` with relative paths (e.g., IPA audio files, images)

### Special-specific patterns

- **Code blocks**: Command libraries, regex libraries, and programming references use fenced code blocks with language tags (```shell, ```regex, ```Python, etc.)
- **Embedded notes** (Classical Chinese): `notes.embed('term', 'explanation')` within `gen.TextCode.compile()` blocks
- **Difficulty markers**: `hard(...)` function in pytextgen blocks for challenging terms
- **Parameter placeholders**: `$variable` format in command library templates
- **Section markers**: pytextgen sections use `__env__.cwf_sects("id1", "id2")` for stable section identification
- **Index cross-references**: Course indexes often use `[§ section](file.md#section)` format for sub-topic links

## Special Differences from general/

1. **Sources**: Content originates from:
   - Academic coursework (lectures, assignments, exams)
   - Online courses (Coursera, self-paced MOOCs)
   - Personal notes and learning materials
   - Official documentation (NumPy, MySQL, C/C++ standards)
   - Classical literature and cultural texts
   - Business/MBA curriculum
   - Practical experience and command-line workflows

2. **Structure**: Highly variable hierarchies depending on content type:
   - Academia: institution → semester → course → topics (up to 5 levels deep)
   - Online courses: module → topic → subtopic (3 levels)
   - Programming refs: language → library → function (3 levels)
   - Root-level files: Single-file guides with internal sections (2 levels)

3. **Metadata**: Additional fields beyond `general/` conventions:
   - Academic: semester tags, credits, course status, prerequisites
   - Versioned docs: `version/<software>/<major>/<minor>` tags
   - Questions: `date/<year>/<month>/<day>`, `question/<domain>/<subdomain>`
   - Classical texts: `by/<author>`, `language/for/<lang>` (target language)
   - Licensing: Some include `LICENSE.txt` files from upstream sources

4. **Updates**: 
   - Academic: Manual editing or via `tools/special/` LMS converters
   - Online courses: Manual note-taking and synthesis
   - Programming refs: Manual extraction from documentation
   - Classical texts: Manual transcription with scholarly annotations
   - NOT updated via `convert wiki.py` (that's for `general/` only)

5. **Flashcard status**: More varied than `general/`:
   - `flashcard/active/special/<path>`: Active learning materials
   - `flashcard/archive/special/<title>`: Archived (e.g., older classical texts)
   - No flashcard tag: Reference materials not for memorization (e.g., command libraries)

6. **Cross-references**: 
   - Bidirectional links between `special/` and `general/` (e.g., course notes reference encyclopedia articles)
   - Links between related `special/` content (e.g., prerequisites between courses)
   - Links to external sources (official docs, course websites)

## Tools in tools/special/

**Academic converters** (LMS export processors):
- `convert Canvas submission.py`: Canvas LMS submission exports → YAML frontmatter + formatted notes
- `convert HKUST Zinc submission.py`: HKUST Zinc LMS submission files → YAML frontmatter
- `get HKUST undergraduate courses.py`: Fetch HKUST course catalog from web → CSV file (`get HKUST undergraduate courses.py.csv`)

**Usage**: See the `tools-special` agent skill for detailed workflows and converter interfaces.

**Stability requirements**:
- Preserve CLI interfaces (argument names, input/output formats)
- Keep YAML output schemas stable (field names, tag structure)
- Maintain CSV column names and structure for course list exports
- Coordinate with main `init.py` wrapper for pytextgen integration

**Files**:
- Each tool has `.py`, `.bat`, `.sh`, and symlink variants for cross-platform support
- Output files follow consistent naming (e.g., `get HKUST undergraduate courses.py.csv`)

## Editing Guidelines

### General principles

- **Academic integrity**: Preserve academic honesty; cite sources appropriately; do not expose exam solutions publicly
- **Attribution**: Include source references in frontmatter or bottom of files (e.g., Coursera course links, documentation URLs)
- **Consistency**: Follow domain-specific conventions (institution naming, course code formats, etc.)
- **Index maintenance**: Keep `index.md` files current when adding/removing courses, modules, or materials
- **Cross-references**: Actively link between:
  - Related courses (prerequisites, follow-ups)
  - `general/` encyclopedia entries for concepts
  - Other `special/` materials (e.g., programming ref from course notes)

### Academia-specific

- **Course codes**: Preserve institution-specific formatting (e.g., HKUST uses `COMP 2012`, not `COMP2012` in titles, but both in aliases)
- **Semester notation**: Use consistent format (`2023 fall`, `2024 spring`, `2023 winter`)
- **Status markers**: Keep course status up-to-date in institution `index.md` (`taken`, `not-taken`, `transferred`)
- **Assessment sections**: Separate section at bottom of course `index.md` for exam/assignment reflections
- **Privacy**: Do not include personal student IDs, grades, or identifying information
- **Content organization**: Follow "teaching order" or "recommended learning order" in index files

### Programming references

- **Version tags**: Include version information in frontmatter when applicable
- **License files**: Keep upstream `LICENSE.txt` files when content is derived from open-source documentation
- **Code examples**: Use proper syntax highlighting with language tags in fenced code blocks
- **Links to general**: Always cross-reference to `general/` main article if it exists

### Classical Chinese texts

- **Text preservation**: Preserve original classical Chinese text exactly as written
- **Annotations**: Use `notes.embed()` for inline annotations without disrupting text flow
- **Author attribution**: Include `by/<author>` tag in frontmatter
- **Language tags**: Use both `language/for/中文` (target language) and `language/in/中文` (language of instruction)
- **pytextgen structure**: Maintain paragraph markers (e.g., `_（第一段）_`) for structured memorization

### Command/regex libraries

- **Parameter naming**: Use consistent placeholder format (`$input_`, `$output`, `$variable`)
- **Tool organization**: Group commands by tool name (ExifTool, FFmpeg, etc.)
- **Testing**: Verify commands work as documented before adding
- **Documentation**: Include parameter descriptions and use case explanations

### Questions collection

- **Naming**: Use ISO 8601 timestamp format for new questions
- **Structure**: Maintain three-part structure (problem, strategy, solution)
- **Tagging**: Include `date/<year>/<month>/<day>` and `question/<domain>/<subdomain>`
- **Flashcard format**: Strategy section should use `:@:` or `::@::` for active recall
- **Math typesetting**: Use proper KaTeX for all mathematical expressions

## Integration with Other Directories

- **`general/`**: `special/` notes frequently reference `general/` encyclopedia articles for foundational concepts
  - Use relative paths: `../../general/article.md` or deeper as needed
  - `general/` articles may backlink to `special/` materials (e.g., course notes, detailed tutorials)
  
- **`archives/`**: Media files (images, audio, videos) referenced in `special/` notes
  - Common: `../../archives/Wikimedia%20Commons/` for IPA audio, images
  - Less common: `../../archives/sparse/` for specialized content
  
- **`tools/`**: 
  - `tools/special/`: Academic LMS converters for maintaining `special/academia/`
  - `tools/pytextgen/`: Content generation library used throughout `special/` for flashcards
  - `tools/utility.py.md`: Utility module imported by many `special/` notes for pytextgen helpers

## pytextgen Usage Patterns in special/

Different content types use pytextgen differently:

1. **Sequential lists** (business frameworks, technical guides):
   ```python
   return await memorize_seq(
     __env__.cwf_sects("id1", "id2"),
     items,
   )
   ```

2. **Mapped content** (key-value pairs):
   ```python
   return await memorize_map(
     __env__.cwf_sects("id1", "id2"),
     items,
   )
   ```

3. **Classical texts with annotations**:
   ```python
   notes = Notes()
   text = gen.TextCode.compile(
     f"""..."""
   )
   return (text, notes)
   ```

4. **Custom formatting** (questions, specialized layouts):
   - Strategy/solution pairs with `:@:` separator
   - Nested cloze deletions with `{@{ }@}`
   - Hard-marked terms with `hard(...)` wrapper

**Regeneration**: Use `python -m init generate <path>` to regenerate pytextgen blocks after editing source data
