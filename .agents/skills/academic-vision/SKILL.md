---
name: academic-vision
description: Use when an academic ingestion depends on what an image shows — reading page renders and embedded figures, deciding what a graphic is, and verifying a generated drawing or an attached crop by looking at it before it reaches a note.
---

# Academic Vision

Part of the material states its content only in a picture: a slide render, an embedded figure, a photograph, or a drawing whose meaning is the drawing itself. An agent that skims the extracted text ingests the words and silently drops the rest. This skill fixes __when looking is mandatory__, __how to look__, and __what to check before an image reaches a note__.

## When looking is mandatory

- __Classifying a figure__ — deciding whether it is a definitional drawing, a text-bearing figure, or purely pictorial (see "Page image handling" in `academic-ingest`). The decision is made from the image, not from its filename or the prose around it.
- __Extracting content that lives in the picture__ — labels inside a diagram, a formula rendered as an image, a table whose layout carries meaning, superscripts and subscripts, Greek letters, unit symbols, or handwriting added to a slide.
- __Checking a doubtful extraction__ — when `text.md` has a gap, a mangled formula, or a missing row, compare it with the page render before writing anything.
- __Drawing something__ — building the SVG for a definitional drawing, and every time that drawing changes (see `academic-crud-attachments`).
- __Attaching a picture__ — before a crop is referenced from a note or a question, and before alt text is written for any image.
- __Carding a diagram__ — before a drawing goes onto either side of a card (see `create-flashcards`).

__Hard rule: never write about an image you have not looked at.__ Reading its path, its size, a manifest entry, an extraction log, or the generator that produced it is not looking. A description, a crop, an attachment, or a verdict written without looking is a fabrication.

## How to look

1. __Open the highest-resolution version available.__ Embedded images in `.extracted/images/` beat the page render in `.extracted/pages/`, which is downscaled; a slide's own text is usually legible in the render, its small labels often are not.
2. __Crop and zoom when detail is unclear.__ A full page hides what a region shows:

   ```bash
   magick images/page_035_img_1.png -crop 200x70+320+235 +repage -resize 500% /tmp/zoom.png
   ```

3. __Look at the image itself.__ Read the rendered file; do not infer from the source HTML, the filename, or the slide's text.
4. __State what it shows before using it.__ One sentence of plain description, written while looking, is what later prose, alt text, and figure classification are built from.
5. __Compare rather than recall.__ To reproduce a drawing, do not work from memory of the slide: crop the source (or re-open the slide), render your version, place the two side by side at the same height, and look at the pair:

   ```bash
   magick source_crop.png -resize x300 /tmp/cmp/deck.png
   rsvg-convert -z 2 -o /tmp/cmp/mine.png attachments/<name>.svg
   magick /tmp/cmp/deck.png /tmp/cmp/mine.png +append /tmp/cmp/pair.png
   ```

6. __Iterate until clean.__ Geometry is wrong far more often than it looks. Fix, re-render, look again, and treat the first passing glance as unverified.
7. __Record what cannot be read.__ An illegible label, a blurred signboard, or a symbol that could be either of two things is reported as unreadable; it is never filled in with a plausible value.

## Checklist before an image reaches a note

For a drawing the notes generate:

- every element of the source drawing is present, in the same order and orientation (`A` above `B`, `+` above `−`);
- nothing overlaps, retraces, or lands on top of something else;
- each label sits beside the element it names, not on another element's line;
- no label overflows its box or runs into its neighbour;
- drawings shown side by side as one set look like one set (same height, same weight);
- everything is legible at the size the note renders it, not only at 3× zoom.

For a picture the notes attach:

- it shows the whole thing the note or question refers to, with no neighbouring content cut into it;
- it is the material's own image or a crop of it — never a page render, never a screenshot of a slide (see `academic-crud-attachments`);
- the alt text matches what the image actually shows.

## When the model cannot see images

Vision requires a model that accepts image input; the ingest skill's vision-awareness check (`PI_MODEL` / `PI_PROVIDER`) is what decides whether the current one does. Without it, the images still have to be accounted for:

- extract what the text carries and write only that;
- list every page and figure that was not looked at, and say what it appears to hold from the text around it;
- report them as needing a vision-capable pass instead of inventing a description or skipping them silently.

A figure nobody looked at is an open item, never an empty one.

## Traps that only the rendered image reveals

Generic, with the `schemdraw` cases that produced them as the worked instance:

- __A drawing library's element already includes its terminal leads.__ Adding leads on top multiplies the drawing's height and turns a symbol into a bump on a wire — `schemdraw`'s default element length is `3` units, so a battery plus two `Line()` leads is three times taller than it should be.
- __Chaining the next element against the current direction retraces the previous segment__, drawing the wire back through the symbol. Chain every element of one branch in the same direction.
- __Label positions offered by a library are element-relative, not screen-relative.__ `loc="right"` on an element drawn upwards lands on top of it; on an element drawn downwards the same keyword lands on the left.
- __A library's own PNG export is not the committed artifact.__ Rasterise the file that was saved (`rsvg-convert -z 2 -o /tmp/look.png attachments/<name>.svg`) and look at that, because that is what the note shows.
- __Defaults that suit one drawing can break another__: a box sized for a long label, a font that fits a wide glyph set, or a default stub shown at 3× may still overlap at the size the note renders.

## Reporting a defective image

Report what the image shows, what the defect is, and where it was seen (path, and the crop or zoom level that exposed it). Never silently accept an image that fails a check, and never state that an image is verified when it has not been looked at in the same session.

## References

- `academic-ingest` for where images enter the flow ("Page image handling", "Definitional drawings", "Embedded image extraction")
- `academic-crud-attachments` for the drawing's home, generator script, naming, and embedding rules
- `create-flashcards` for diagram cards in both directions
- `academic-lint` for the deterministic checks that follow the visual ones
