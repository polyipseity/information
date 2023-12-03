---
aliases:
  - command libraries
  - command library
tags:
  - flashcards/special/command_library
  - functional/libraries
---

# command library

## FFmpeg

### measure loudness

```shell
ffmpeg -i "$input" -af ebur128=framelog=verbose -f null -
```

- source: https://superuser.com/a/1424365

### transcode video

```shell
ffmpeg -i "$input" -map 0 -map_metadata 0 -c:v libaom-av1 -b:v 0 -crf 45 -g 300 -pix_fmt yuv420p -color_range pc -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a 320000 -cues_to_front 1 -pass 1 -f null -
ffmpeg -i "$input" -map 0 -map_metadata 0 -c:v libaom-av1 -b:v 0 -crf 45 -g 300 -pix_fmt yuv420p -color_range pc -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a 320000 -cues_to_front 1 -pass 2 "$output.webm"
```

### transcode to Advanced Audio Coding at transparency

```shell
ffmpeg -i "$input" -map 0:a -map_metadata 0:s:a -c:a aac -b:a 320000 -movflags +faststart "$output.m4a"
```

## rsync

### sync

```shell
rsync -avzuk --delete --progress "$source" "$destination"
```
