---
name: academic-video
description: Use when an academic material links to a video — reading the video's content from its subtitles, deferring a video that has none, and asking the user to have the deferred ones watched before the run ends.
---

# Academic Video

A material that links a video carries content no extraction captured: a slide, a PDF, a handout, or a Canvas page points at a talk, a news clip, or a lecture recording, and the surrounding text sets up the question that video answers. An agent that ingests the words and drops the link loses part of the source silently. This skill fixes __what counts as a video link__, __how to read its content__, __what to do when there is none__, and __how the user is asked to help__.

## The link is course material

- A video link anywhere in the source is course material and is ingested like the rest of the source: slide text, a Canvas page body, a PDF, a Markdown note, an `<iframe>` or `<video>` tag, an embedded player, or a bare URL in a list.
- __The transcript is the video's content.__ Read all of it, then treat its concepts exactly as the material's other concepts: they go through topic-note reconciliation and into the notes and cards when they are durable knowledge.
- __Never write the video into a note.__ The deferral, the fact that a video was watched, and a summary of what it shows are run state, not note content (see "Never write current status or provenance" in `academic-ingest`).
- __A claim is not a finding.__ When the material introduces a video as a myth, a stereotype, an illustration of what mass media says, or a claim to be evaluated, the video is evidence that the claim circulates, not evidence that it is true. Never state its claims as established knowledge: record the claim as a claim, or leave it out and let whatever evaluates it in the material decide.
- The video's own authorship — a talk, a named speaker, a publisher — is a real-world source, and it may be named in `## references` when the note incorporates its content, as a list entry like any other source (see "Style conventions" in `academic-crud-topic-note`). The deck or page that linked it is not a source.
- A video that only illustrates a point the surrounding text already states adds nothing: read it, and leave the note alone if it already carries the concept.

## Reading the video

Subtitles are the content. Prefer the video's own captions, fall back to its automatic captions, and never download the video itself.

1. __Resolve the link.__ A slide wraps, truncates, or mangles URLs: `...watch?v=CCz08Bw9wE` with `Q&feature=related` on the line below is really `CCz08Bw9wEQ`. A YouTube id is 11 characters, and `oembed` both repairs and identifies it:

   ```bash
   curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json"
   ```

2. __List the caption tracks.__

   ```bash
   tmp=$(mktemp -d)
   uv run --with yt-dlp --no-project yt-dlp --skip-download --list-subs --no-warnings \
     "<url>" > "$tmp/subs.txt"
   ```

3. __Download the English track.__ Prefer `en`; when the video carries only `en-orig`, use that. A track named `en-ar`, `en-ja`, or the like is machine-translated from another language and is not the video's words.

   ```bash
   uv run --with yt-dlp --no-project yt-dlp --skip-download \
     --write-sub --write-auto-sub --sub-lang "en,en-orig" --sub-format vtt \
     -o "$tmp/%(id)s.%(ext)s" --no-warnings "<url>"
   ls "$tmp"/*.vtt
   ```

4. __Verify that a file exists.__ `yt-dlp` exits 0 even when it wrote nothing, and it rate-limits with HTTP 429. No `.vtt` in `$tmp` means __no usable subtitles__: defer the video and say why, rather than guessing.

5. __Strip the timestamps.__ Rolling automatic captions repeat each line, so deduplicate before reading or the transcript is unreadable:

   ```bash
   uv run python - "$tmp"/*.vtt <<'PY'
   import re, sys
   for path in sys.argv[1:]:
       seen, out = None, []
       for line in open(path, encoding="utf-8"):
           if "-->" in line or line.startswith(("WEBVTT", "Kind:", "Language:")):
               continue
           text = re.sub(r"<[^>]+>", "", line).strip()
           if not text or text == seen:
               continue
           seen = text
           if out and (out[-1].endswith(text) or text in out[-1]):
               continue
           out.append(text)
       print(" ".join(out))
   PY
   ```

6. __A title is not content.__ The `oembed` title, the channel, and the description identify a video; they never substitute for the transcript and never justify prose about what the video shows.

Run every command from the workspace root, never inside a skill folder, and write only into the temp directory. No subtitle file and no video file ever lands in the repository or in `attachments/` — a linked video is a source, not a referenced raw file.

Non-YouTube sources (Vimeo, Canvas/Kaltura, Panopto, Echo360, Bilibili, Youku, a direct media file) go through the same steps; `yt-dlp` supports many of them. When it cannot read one, defer that video too.

## Deferring a video

A video with no usable subtitles is __deferred__: its content is not guessed, not paraphrased from its title, and not dropped in silence.

- Write nothing about the video into any note, card, or index. An empty section is better than a fabricated one.
- Keep the deferral in the run's own state: the URL, the context that introduces it, and which note would receive the content.
- Finish the rest of the ingestion normally. Captions that do exist are read now, not deferred.
- Report each deferred video with its reason — no caption track, a foreign-language original only, a failed extraction — and let the concepts that depend on it stay uncovered rather than invented.

## Asking the user to watch them

__Before returning to the user, and only then, batch every deferred video into one request.__ Do not ask mid-ingestion, and do not ask once per video.

The request names each video, the concepts waiting on it, and the way to get its content:

- __YouTube__ — ask for Gemini. The Gemini app and Google AI Studio accept a YouTube URL directly and watch the frames and the audio; NotebookLM takes the URL as well and can compare it against an uploaded source.
- __Anything not on YouTube__ — ask for a tool that takes the file: Gemini with the video uploaded, or a Whisper-based summarizer. `yt-dlp` into a local Whisper transcript works when the user wants to keep it offline.
- Ask for the content, not a verdict: the transcript when the user can get it, otherwise the summary with its timestamps. Bring it back through reconciliation, cards, the humanizer pass, and validation like any other source.

```text
3 videos have no usable subtitles, so their content is not in the notes yet:
  1. https://www.youtube.com/watch?v=<ID> — psychology (mental health: adolescent statistics, early identification)
  2. <url> — <note> (<concept>)
Paste each into the Gemini app or Google AI Studio (they take a YouTube URL directly) and send me back the summary, or the transcript, and I will incorporate it.
```

A video whose content the user cannot supply stays uncovered, and the report says so. That is a finished ingestion, not a failed one.

## References

- `academic-ingest` for where video handling sits in the ingestion pipeline and how the request is batched
- `academic-crud-topic-note` for reconciling the concepts a transcript carries
- `create-flashcards` for carding them
- `academic-lint` for validation
