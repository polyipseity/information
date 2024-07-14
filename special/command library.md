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

### combine audio and video

```shell
ffmpeg -itsoffset "$offset_v" -i "$input_v" -itsoffset "$offset_a" -i "$input_a" -map 0 -map 1 -c copy "$output"
```

- parameters
  - `$offset_a` = `0`: audio offset
  - `$offset_v` = `0`: video offset
  - `$input_a`: input audio filename
  - `$input_v`: input video filename
  - `$output`: output filename

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
ffmpeg -i "$input" -map 0:a -c:a aac -b:a "$bitrate" -movflags +faststart "$output.m4a"
```

- parameters
  - `$bitrate` = `320000`: bitrate in bits per second (bps)
  - `$input`: input filename
  - `$output`: output filename without extension

#### AV1 and Opus in WebM

```shell
ffmpeg -i "$input" -map 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libaom-av1 -b:v 0 -crf 45 -g "$($fps * 5)" -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a "$audio_bitrate" -cues_to_front 1 -pass 1 -f null -
ffmpeg -i "$input" -map 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libaom-av1 -b:v 0 -crf 45 -g "$($fps * 5)" -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -row-mt 1 -tile-columns 2 -tile-rows 1 -cpu-used 4 -c:a libopus -b:a "$audio_bitrate" -cues_to_front 1 -pass 2 "$output.webm"
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
ffmpeg -i "$input" -map 0 -vf "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v libx265 -tag:v hvc1 -b:v 0 -crf 28 -g "$($fps * 5)" -preset medium -pix_fmt "$pixel_format" -color_range "$color_range" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -c:a aac -b:a "$audio_bitrate" -movflags +faststart "$output.mov"
```

- parameters
  - `$audio_bitrate` = `320000`: audio bitrate in bits per second (bps)
  - `$color_range` = `full`: `full` or `limited`; color range
  - `$fps` = `60`: frames per second
  - `$input`: input filename
  - `$output`: output filename without extension
  - `$pixel_format` = `yuv420p`: pixel format

## GhostScript

### optimize PDF

```shell
gs -dBATCH -dNOPAUSE -dQUIET -sDEVICE=pdfwrite "-dPDFSETTINGS=$preset" '-dCompatibilityLevel=2.0' "-sOutputFile=$output" "$input"
```

- parameters
  - `$preset` = `/default`: `/default` or (`/screen` < `/ebook` < `/printer` < `/prepress`); distiller parameters preset
  - `$input`: input filename
  - `$output`: output filename
- source: <https://askubuntu.com/a/256449>

## ImageMagick

### images to PDF

```shell
magick $inputs "$output.pdf"
```

- parameters
  - `$inputs`: input filenames
  - `$output`: output filename without extension

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
