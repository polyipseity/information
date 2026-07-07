---
name: special
description: Conventions for all Markdown content and tools under special/
applyTo: "special/**/*.md, special/**/*.py"
---

# Special Content Instructions

The `special/` directory contains specialized knowledge including coursework, tutorials, language texts, business frameworks, technical documentation, command libraries, and other curated learning materials. Unlike `general/` (Wikipedia articles), `special/` content comes from diverse sources: academic coursework, online courses, personal notes, tutorials, reference documentation, and practical guides.

## Directory Structure Overview

```text
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

__Important note__: The `special/` directory is still expanding and may include more diverse content types in the future beyond those enumerated in this document. When encountering new content types not explicitly covered by these instructions, apply the following principles:

1. __Extrapolate existing rules__: The conventions described in this document (frontmatter structure, cloze markup, pytextgen patterns, cross-references, link formatting) apply to all content types in `special/`, whether currently documented or not
2. __Maintain consistency__: New content should follow the same overall structure, tagging, and markdown principles as existing materials
3. __Adapt domain-specific guidelines__: Apply the domain-specific guidance most similar to the new content type (e.g., use programming reference guidelines for new language documentation, academia guidelines for new course materials)
4. __Preserve metadata schemas__: Maintain stable YAML frontmatter structures and tag naming conventions for any new content
5. __When in doubt__: Consult this document's general principles and existing content patterns as reference guides

Examples of potential future content: additional programming languages, specialized technical tutorials, domain-specific frameworks, curated research materials, domain-specific Q&A collections, etc.

## Content Organization by Type

### 1. Academic Coursework (`academia/`)

Academic courses organized hierarchically by institution, semester, and course code:

```text
special/academia/
├── <Institution>/              # e.g., HKUST, Korea University
│   ├── index.md               # Course listings by semester/year
│   ├── reviews.md             # Institution-specific reviews and notes
│   └── <Course Code>/         # e.g., COMP 2012, ACCT 2010, ISC213
│       ├── index.md           # Course overview, schedule, assessments
│       ├── *.md               # Lecture notes, readings, assignments
│       └── [subdirs]          # Topic-specific subdirectories if needed
```

__Institutions included__:

- __HKUST__: Hong Kong University of Science and Technology (largest collection: 40+ courses in COMP, ACCT, BIEN, CIVL, DASC, ECON, ELEC, ENGG, ESST, FINA, GNED, ISDN, ISOM, LANG, MATH, PHYS, TEMG, and Robotics Team)
- __Korea University__: ISC213 (Korean language/culture course)
- __Pusan National University__: IT3000504 (IT-related course)
- __USFQ__: Universidad San Francisco de Quito courses
- __Yonsei University__: Yonsei University courses

__Course metadata__ (in YAML frontmatter and `index.md`):

- __Aliases__: Multiple name variants (e.g., `COMP 2012`, `COMP2012`, `HKUST COMP 2012`, full course name)
- __Tags__: `flashcard/active/special/academia/<institution>/<course_code>`, `function/index`, `language/in/English`
- __Semester/year__: Listed in `index.md` (e.g., `2023 fall`, `2024 spring`, `2023 winter`)
- __Credits__: Parenthetical after course title (e.g., `(4 credits)`)
- __Status__: `taken`, `not-taken`, `transferred`, or status markers in `index.md`
- __Content organization__: Often includes "week X lecture Y" sections or topic-based sections
- __Assessments__: Separate section for midterm/final examination reports and reflections

__Index maintenance__:

- __Institution-level `index.md`__: Lists all courses by semester (most recent first)
- __Course-level `index.md`__: Overview, teaching order, week-by-week breakdown, assessments
- __Cross-references__: Link to related `general/` articles for concepts (e.g., `[most vexing parse](../../../../general/most%20vexing%20parse.md)`)
- __Academic converters__ in `scripts/special/` help maintain these indexes (see [§ Tools](#tools-in-toolsspecial))

### 2. Online Course Materials

Self-contained course materials from MOOCs and online learning platforms:

__`audio signal processing/`__: Complete course on audio signal processing

- __Structure__: 10 modules with hierarchical index showing learning order
- __Content types__:
  - Conceptual notes (signal mathematics, discrete Fourier transform, STFT, etc.)
  - Tool usage guides (Audacity, SonicVisualiser, sms-tools, Freesound)
  - Programming guides (Python/NumPy for signal processing, Essentia library)
- __Index format__: Module-by-module breakdown with subsections linking to specific topics
- __Source attribution__: References Coursera course "Audio Signal Processing for Music Applications"
- __Cross-references__: Links to related `general/` articles (e.g., `[Music Technology Group](../../general/Music%20Technology%20Group.md)`)

### 3. Programming Language References

Technical documentation for programming languages and libraries:

__`C/`__: C standard library references

- __Subdirectories__: `date and time utilities/`, `file input_output/`, `numerics/`, `strings library/`
- __Top-level files__: Overview files like `date and time utilities.md`
- __Cross-references__: Links to `general/` C documentation (e.g., `[C date and time functions](../../general/C%20date%20and%20time%20functions.md)`)

__`C++/`__: C++ language features

- __Files__: `array.md`, `implicit conversion.md`, `lambda.md`, `overload resolution.md`
- __Focus__: Specific language features and gotchas

__`MySQL/`__: MySQL database reference

- __Structure__: `index.md` + topical files (`data types.md`, `functions and operators.md`, `statements.md`)
- __Source__: Coursera "Introduction to Structured Query Language (SQL)" course
- __Cross-reference__: Links to `[general/MySQL](../../general/MySQL.md)`

__`NumPy/`__: NumPy library documentation

- __Structure__: `index.md` + `user guide/` subdirectory
- __Version-tagged__: `version/NumPy/2/1` in frontmatter
- __Licensing__: Includes `LICENSE.txt` from upstream
- __Source__: <https://numpy.org/doc/2.1/index.html>

### 4. Language Acquisition Materials

__`language acquisition/`__: Foreign language learning resources

__`language acquisition/English/`__:

- `difficult-to-spell words.md`: Spelling reference

__`language acquisition/中文/`__ (Chinese):

- `倉頡輸入法難字.md`: Difficult characters for Cangjie input method
- `简化字总表.md`: Table of simplified Chinese characters

__`International Phonetic Alphabet.md`__: Comprehensive IPA reference

- __Structure__: Phonetic symbols with audio examples (linked to `archives/Wikimedia Commons/`)
- __Content__: Official IPA chart image, detailed help for each phonetic symbol
- __Cross-references__: Links to individual phonetic articles in `general/`
- __Tags__: `flashcard/active/special/language_acquisition/International_Phonetic_Alphabet`

### 5. Business and Strategy Frameworks

Root-level files containing MBA-style frameworks and business strategy tools:

__Strategy frameworks__:

- `blue ocean strategy.md`: Red ocean vs. blue ocean, blue ocean shift process (understand "as-is", imagine "to be", create "gap"), strategy canvas
- `5-step persuasive selling.md`: Persuasive selling framework (background, big idea, how it works, key benefits/risks, next step)
- `business model canvas.md`: 9 building blocks of business model (comprehensive framework)
- `buyer utility map.md`: Customer utility analysis
- `value proposition canvas.md`: Value proposition design
- `market segmentation.md`: Segmentation strategies
- `profitability framework.md`: Profitability analysis

__Business analysis tools__:

- `IBM prioritization grid.md`: Prioritization matrix
- `PPTG change impact framework.md`: Change impact assessment
- `lift chart.md`: Model evaluation chart

__Personal documents__:

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

__Cross-references__: Many link to `general/` articles (e.g., `[GNU Debugger](../general/GNU%20Debugger.md)`)

### 7. Command and Regex Libraries

Reusable command patterns and regex snippets:

__`command library.md`__: Shell command recipes organized by tool

- __Tools covered__: ExifTool, FFmpeg, GhostScript, Git, ImageMagick, yt-dlp, etc.
- __Format__: Command templates with parameter placeholders (e.g., `$input_`, `$output`)
- __Use cases__: Copy metadata, combine audio/video, measure loudness, batch operations, etc.

__`regex library.md`__: Regular expression patterns

- __Examples__: Unicode line boundaries pattern
- __Format__: Code block + description + regex repetition for flashcards

### 8. Classical Chinese Texts

Traditional Chinese literary works with full text and annotations:

__Files__ (by title in Chinese):

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

__Structure__:

- __Frontmatter__: Author (`by/<author>`), language tags (`language/for/中文`, `language/in/中文`), flashcard tags (often `flashcard/archive/special/<title>`)
- __Content__: Full classical Chinese text with embedded notes using `notes.embed('term', 'explanation')` syntax
- __pytextgen integration__: Uses `gen.TextCode.compile()` for structured memorization of classical texts paragraph by paragraph
- __Notes system__: Inline annotations for difficult characters, phrases, and literary devices

### 9. Questions Collection

__`questions/`__: Timestamped question-answer pairs, primarily mathematical problems

__Naming convention__: ISO 8601 timestamps with timezone (e.g., `2023-08-06T225216.434+0800.md`)

__Structure__:

- __Frontmatter__: `date/<year>/<month>/<day>`, `question/<domain>/<subdomain>`, flashcard tags
- __Content sections__: Problem statement, strategy (thinking process), solution (detailed work)
- __Flashcard format__: Strategy as cloze/QA format using `:@:` for active recall
- __Subdirectory__: `attachments/` for supporting files

__Example topics__: Limits, calculus, integration, series convergence, trigonometric substitution, matrix operations, etc.

__Cross-references__: Some questions reference concepts in `general/` or `special/academia/` course materials

### 10. Worked Examples

__`examples/`__: Detailed worked examples and case studies

__Current examples__:

- `inventing the air fryer from observing French fries.md`: Innovation case study
- Additional examples in subdirectory (single file observed)

__Purpose__: Illustrative examples for concepts, problem-solving techniques, or creative thinking

### 11. Mathematical Content

Root-level mathematical notes not fitting into `general/` or `academia/`:

- `constant of integration.md`: Integration concepts
- `integration by substitution.md`: Calculus technique
- `linear—rotational motion analogy.md`: Physics/mechanics analogy
- `list of mathematical pathologies.md`: Counterexamples and edge cases

### 12. Miscellaneous Specialized Content

__Astronomy__:

- `list of Nobel laureates in Astronomy.md`: List of laureates

__Design thinking__:

- `d.school design thinking bootleg.md`: Stanford d.school design thinking guide

__Education__:

- `examination keys - HKDSE liberal studies.md`: Hong Kong exam reference

__Nutritional information__:

- `nutritional information/` subdirectory
  - `Redoxon Triple Action.md`: Supplement information
  - `VÖOST Collagen Formation.md`: Supplement information

__Attachments__:

- `attachments/` subdirectory: Supporting files like images, PDFs, and specialized scripts
  - Example: `GhostScript remove metadata pdfmark.txt`

## Markdown Conventions

Apply the same conventions as `general/` notes, with domain-specific adaptations:

### Common conventions

- __Frontmatter__: YAML with `aliases`, `tags`, `language/in/<lang>` (or `language/for/<lang>` for language texts)
- __Cloze & flashcard markup__: See [editing-conventions.instructions.md](../editing-conventions.instructions.md) for complete syntax rules.
- __pytextgen fences__: Preserve `# pytextgen generate ...` comments and `return export_seq(...)` signatures. See the pytextgen patterns section below for usage patterns.
- __Links__: Relative paths with `%20` encoding for spaces
  - Cross-references to `general/`: `[topic](../../general/topic.md)` or similar relative paths
  - Internal links: `[section](#section-header)` for same-file references
- __Math__: KaTeX `$inline$` and `$$display$$` formats (heavily used in questions, mathematical notes)
- __Media__: Reference files in `archives/` with relative paths (e.g., IPA audio files, images)

### Special-specific patterns

- __Code blocks__: Command libraries, regex libraries, and programming references use fenced code blocks with language tags (`shell,`regex, ```Python, etc.)
- __Classical Chinese annotations__: `notes.embed('term', 'explanation')` within `gen.TextCode.compile()` blocks (see pytextgen patterns section below for examples)
- __Parameter placeholders__: `$variable` format in command library templates
- __Index cross-references__: Course indexes often use `[§ section](file.md#section)` format for sub-topic links

### pytextgen patterns in special/

Different content types use pytextgen differently. Common patterns:

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
   - Strategy/solution pairs with `:@:` separator (one-sided Q/A); two-sided pairs use `::@::`, and arbitrary cloze deletions use `{@{ }@}`
   - Nested cloze deletions with `{@{ }@}`
   - Hard-marked terms with `hard(...)` wrapper

__Regeneration__: Generated content is handled by the repository's build workflows; agents should never run `uv run -m init generate` themselves.

## Special Differences from general/

1. __Sources__: Content originates from:
   - Academic coursework (lectures, assignments, exams)
   - Online courses (Coursera, self-paced MOOCs)
   - Personal notes and learning materials
   - Official documentation (NumPy, MySQL, C/C++ standards)
   - Classical literature and cultural texts
   - Business/MBA curriculum
   - Practical experience and command-line workflows

2. __Structure__: Highly variable hierarchies depending on content type:
   - Academia: institution → semester → course → topics (up to 5 levels deep)
   - Online courses: module → topic → subtopic (3 levels)
   - Programming refs: language → library → function (3 levels)
   - Root-level files: Single-file guides with internal sections (2 levels)

3. __Metadata__: Additional fields beyond `general/` conventions:
   - Academic: semester tags, credits, course status, prerequisites
   - Versioned docs: `version/<software>/<major>/<minor>` tags
   - Questions: `date/<year>/<month>/<day>`, `question/<domain>/<subdomain>`
   - Classical texts: `by/<author>`, `language/for/<lang>` (target language)
   - Licensing: Some include `LICENSE.txt` files from upstream sources

4. __Updates__:
   - Academic: Manual editing or via `scripts/special/` LMS converters
   - Online courses: Manual note-taking and synthesis
   - Programming refs: Manual extraction from documentation
   - Classical texts: Manual transcription with scholarly annotations
   - NOT updated via `convert_wiki.py` (that's for `general/` only)

5. __Flashcard status__: More varied than `general/`:
   - `flashcard/active/special/<path>`: Active learning materials
   - `flashcard/archive/special/<title>`: Archived (e.g., older classical texts)
   - No flashcard tag: Reference materials not for memorization (e.g., command libraries)

6. __Cross-references__:
   - Bidirectional links between `special/` and `general/` (e.g., course notes reference encyclopedia articles)
   - Links between related `special/` content (e.g., prerequisites between courses)
   - Links to external sources (official docs, course websites)

## Tools in scripts/special/

__Academic converters__ (LMS export processors):

- `convert_canvas_submission.py`: Canvas LMS submission exports → YAML frontmatter + formatted notes
- `convert_hkust_zinc_submission.py`: HKUST Zinc LMS submission files → YAML frontmatter
- `get_hkust_undergraduate_courses.py`: Fetch HKUST course catalog from web → CSV file (`get_hkust_undergraduate_courses.py.csv`)

__Usage__: See the `tools` agent skill (templates & special/tooling sections) for detailed workflows and converter interfaces.

__Stability requirements__:

- Preserve CLI interfaces (argument names, input/output formats)
- Keep YAML output schemas stable (field names, tag structure)
- Maintain CSV column names and structure for course list exports
- Coordinate with main `init.py` wrapper for pytextgen integration

__Files__:

- Each tool has `.py`, `.bat`, `.sh`, and symlink variants for cross-platform support
- Output files follow consistent naming (e.g., `get_hkust_undergraduate_courses.py.csv`)

## Editing Guidelines

### General principles

- __Academic integrity__: Preserve academic honesty; cite sources appropriately; do not expose exam solutions publicly
- __Attribution__: Include source references in frontmatter or bottom of files (e.g., Coursera course links, documentation URLs)
- __Consistency__: Follow domain-specific conventions (institution naming, course code formats, etc.)
- __Index maintenance__: Keep `index.md` files current when adding/removing courses, modules, or materials
- __Cross-references__: Actively link between:
  - Related courses (prerequisites, follow-ups)
  - `general/` encyclopedia entries for concepts
  - Other `special/` materials (e.g., programming ref from course notes)

### Developer tooling & tests (special/)

- Any new tool or helper script that transforms or ingests `special/` content requires unit tests and integration tests; tests should be placed under `tests/` using `tmp_path: os.PathLike[str]` (annotate the `tmp_path` fixture as `PathLike[str]`) to avoid mutating the repo. For conversion tools, add regression tests that verify expected output for representative inputs and that guard against accidental format drift. When converting path-like objects to strings in tests or code, __always__ use `os.fspath(path_like)`.
- Async helpers in this directory should follow the repository-wide AnyIO/Asyncer conventions instead of using `asyncio`. Agents should import from Asyncer (`create_task_group`, `soonify`, `asyncify`, `syncify`, `runnify`) when writing or refactoring scripts or tools here.
- For content changes that affect pytextgen fences, add round-trip tests that verify the fences remain unchanged except for intentional updates; these tests should not invoke `uv run -m init generate`, and agents are explicitly forbidden from running that command.
- Ensure `bun run check`, `bun run format`, and `bun run test` pass locally before opening a PR. Whenever possible include explicit file arguments (e.g. `bun run check:md --no-globs special/academia/...`) so commands complete faster and avoid touching unrelated content.

### Academia-specific

- __Course codes__: Preserve institution-specific formatting (e.g., HKUST uses `COMP 2012`, not `COMP2012` in titles, but both in aliases)
- __Semester notation__: Use consistent format (`2023 fall`, `2024 spring`, `2023 winter`)
- __Status markers__: Keep course status up-to-date in institution `index.md` (`taken`, `not-taken`, `transferred`)
- __Assessment sections__: Separate section at bottom of course `index.md` for exam/assignment reflections
- __Privacy__: Do not include personal student IDs, grades, or identifying information
- __Content organization__: Follow "teaching order" or "recommended learning order" in index files

### Programming references

- __Version tags__: Include version information in frontmatter when applicable
- __License files__: Keep upstream `LICENSE.txt` files when content is derived from open-source documentation
- __Code examples__: Use proper syntax highlighting with language tags in fenced code blocks
- __Links to general__: Always cross-reference to `general/` main article if it exists

### Classical Chinese texts

- __Text preservation__: Preserve original classical Chinese text exactly as written
- __Annotations__: Use `notes.embed()` for inline annotations without disrupting text flow
- __Author attribution__: Include `by/<author>` tag in frontmatter
- __Language tags__: Use both `language/for/中文` (target language) and `language/in/中文` (language of instruction)
- __pytextgen structure__: Maintain paragraph markers (e.g., `_（第一段）_`) for structured memorization

### Command/regex libraries

- __Parameter naming__: Use consistent placeholder format (`$input_`, `$output`, `$variable`)
- __Tool organization__: Group commands by tool name (ExifTool, FFmpeg, etc.)
- __Testing__: Verify commands work as documented before adding
- __Documentation__: Include parameter descriptions and use case explanations

### Questions collection

- __Naming__: Use ISO 8601 timestamp format for new questions
- __Structure__: Maintain three-part structure (problem, strategy, solution)
- __Tagging__: Include `date/<year>/<month>/<day>` and `question/<domain>/<subdomain>`
- __Flashcard format__: Strategy sections (and similar QA content)
  should use the appropriate separator. Use `::@::` for two-sided cards
  (producing both question→answer and answer→question) or `:@:` for
  one-sided cards (recall the right-hand text only). Lines must remain
  single‑line; use `<br/>`/`<p>` for visual breaks.
- __Math typesetting__: Use proper KaTeX for all mathematical expressions

## Integration with Other Directories

- __`general/`__: `special/` notes frequently reference `general/` encyclopedia articles for foundational concepts
  - Use relative paths: `../../general/article.md` or deeper as needed
  - `general/` articles may backlink to `special/` materials (e.g., course notes, detailed tutorials)

- __`archives/`__: Media files (images, audio, videos) referenced in `special/` notes
  - Common: `../../archives/Wikimedia%20Commons/` for IPA audio, images
  - Less common: `../../archives/sparse/` for specialized content

- __`scripts/`__:
  - `scripts/special/`: Academic LMS converters for maintaining `special/academia/`
  - `scripts/utility.py.md`: Utility module imported by many `special/` notes for pytextgen helpers
