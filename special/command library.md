---
aliases:
  - command libraries
  - command library
tags:
  - flashcard/special/command_library
  - functional/library
  - language/in/English
---

# command library

## FFmpeg

### measure loudness

```shell
ffmpeg -i "$input" -af ebur128=framelog=verbose -f null -
```

- parameters
  - `$input`: input filename
- source: <https://superuser.com/a/1424365>

### transcode

#### AAC in MP4

```shell
ffmpeg -i "$input" -map 0:a -map_metadata 0:g -map_metadata 0:s:a -c:a aac -b:a "$bitrate" -movflags +faststart "$output.m4a"
```

- parameters
  - `$bitrate` = `320000`: bitrate in bits per second (bps)
  - `$input`: input filename
  - `$output`: output filename without extension

#### AV1 and Opus in WebM

```shell
ffmpeg -i "$input" -map 0 -map_metadata 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libaom-av1 -b:v 0 -crf 45 -g "$($fps * 5)" -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a "$audio_bitrate" -cues_to_front 1 -pass 1 -f null -
ffmpeg -i "$input" -map 0 -map_metadata 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libaom-av1 -b:v 0 -crf 45 -g "$($fps * 5)" -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a "$audio_bitrate" -cues_to_front 1 -pass 2 "$output.webm"
```

- parameters
  - `$audio_bitrate` = `320000`: audio bitrate in bits per second (bps)
  - `$color_range` = `full`: `full` or `limited`; color range
  - `$fps` = `60`: frames per second
  - `$input`: input filename
  - `$output`: output filename without extension
  - `$pixel_format` = `yuv420p`: pixel format

#### HEVC and AAC in QTFF

```shell
ffmpeg -i "$input" -map 0 -map_metadata 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libx265 -tag:v hvc1 -b:v 0 -crf 28 -g "$($fps * 5)" -preset medium -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -c:a aac -b:a "$audio_bitrate" -movflags +faststart "$output.mov"
```

- parameters
  - `$audio_bitrate` = `320000`: audio bitrate in bits per second (bps)
  - `$color_range` = `full`: `full` or `limited`; color range
  - `$fps` = `60`: frames per second
  - `$input`: input filename
  - `$output`: output filename without extension
  - `$pixel_format` = `yuv420p`: pixel format

## PowerShell

### create hard link

```PowerShell
New-Item -ItemType HardLink -Path "$from" -Value "$to" # for file
New-Item -ItemType Junction -Path "$from" -Value "$to" # for directory
```

- parameters
  - `$from`: link name
  - `$to`: link target

### create symbolic link

```PowerShell
New-Item -ItemType SymbolicLink -Path "$from" -Value "$to"
```

- parameters
  - `$from`: link name
  - `$to`: link target

## rsync

### sync

```shell
rsync -avzuk --delete --progress "$source" "$destination"
```

- parameters
  - `$source`: source
  - `$destination`: destination
