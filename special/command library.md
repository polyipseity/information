---
aliases:
  - command libraries
  - command library
tags:
  - flashcard/active/special/command_library
  - language/in/English
---

# command library

## ExifTool

### copy metadata

```shell
exiftool -tagsFromFile "$input_" -all:all -extractEmbedded -FileModifyDate -overwrite_original "$output"
```

- parameters
  - `$input_`: input filename
  - `$output`: output filename

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
ffmpeg -i "$input_" -af ebur128=framelog=verbose -f null -
```

- parameters
  - `$input_`: input filename
- source: <https://superuser.com/a/1424365>

### transcode

#### AAC in MP4

```shell
ffmpeg -i "$input_" -map 0:a -c:a aac -b:a "$bitrate" -movflags +faststart "$output.m4a"
exiftool -tagsFromFile "$input_" -all:all -extractEmbedded -FileModifyDate -overwrite_original "$output.m4a"
```

- parameters
  - `$bitrate` = `320000`: bitrate in bits per second (bps)
  - `$input_`: input filename
  - `$output`: output filename without extension

#### AV1 and Opus in WebM

```shell
ffmpeg -i "$input_" -map 0 -c copy -filter:v:0 "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v:0 libaom-av1 -b:v:0 0 -crf:v:0 31 -g:v:0 "$($fps * 10)" -pix_fmt:v:0 "$pixel_format" -color_range:v:0 "$color_range" -colorspace:v:0 bt709 -color_primaries:v:0 bt709 -color_trc:v:0 bt709 -row-mt:v:0 1 -tiles 2x2 -cpu-used:v:0 4 -c:a libopus -b:a "$audio_bitrate" -pass 1 -f null -
ffmpeg -i "$input_" -map 0 -c copy -filter:v:0 "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v:0 libaom-av1 -b:v:0 0 -crf:v:0 31 -g:v:0 "$($fps * 10)" -pix_fmt:v:0 "$pixel_format" -color_range:v:0 "$color_range" -colorspace:v:0 bt709 -color_primaries:v:0 bt709 -color_trc:v:0 bt709 -row-mt:v:0 1 -tiles 2x2 -cpu-used:v:0 4 -c:a libopus -b:a "$audio_bitrate" -pass 2 -cues_to_front 1 "$output.webm"
```

- parameters
  - `$audio_bitrate` = `320000`: audio bitrate in bits per second (bps)
  - `$color_range` = `pc`: `pc` or `tv`; color range
  - `$fps` = `60`: frames per second
  - `$input_`: input filename
  - `$output`: output filename without extension
  - `$pixel_format` = `yuv420p`: pixel format

#### HEVC and AAC in QTFF

```shell
ffmpeg -i "$input_" -map 0 -c copy -filter:v:0 "fps=fps=$fps,scale=in_color_matrix=auto:out_color_matrix=bt709:in_range=auto:out_range=$color_range" -c:v:0 libx265 -tag:v:0 hvc1 -b:v:0 0 -crf:v:0 28 -g:v:0 "$($fps * 10)" -preset:v:0 medium -pix_fmt:v:0 "$pixel_format" -color_range:v:0 "$color_range" -colorspace:v:0 bt709 -color_primaries:v:0 bt709 -color_trc:v:0 bt709 -c:a aac -b:a "$audio_bitrate" -movflags +faststart "$output.mov"
exiftool -tagsFromFile "$input_" -all:all -extractEmbedded -FileModifyDate -overwrite_original "$output.mov"
```

- parameters
  - `$audio_bitrate` = `320000`: audio bitrate in bits per second (bps)
  - `$color_range` = `pc`: `pc` or `tv`; color range
  - `$fps` = `60`: frames per second
  - `$input_`: input filename
  - `$output`: output filename without extension
  - `$pixel_format` = `yuv420p`: pixel format

## GhostScript

### optimize PDF

```shell
gs -dBATCH -dNOPAUSE -dQUIET -sDEVICE=pdfwrite "-dPDFSETTINGS=$preset" '-dCompatibilityLevel=2.0' "-sOutputFile=$output" "$input_"
```

- parameters
  - `$preset` = `/default`: `/default` or (`/screen` < `/ebook` < `/printer` < `/prepress`); distiller parameters preset
  - `$input_`: input filename
  - `$output`: output filename
- source: <https://askubuntu.com/a/256449>

### remove metadata

The command below may not remove all metadata. See <https://stackoverflow.com/a/78633569>.

```shell
gs -dBATCH -dNOPAUSE -dQUIET -sDEVICE=pdfwrite -dOmitXMP=true "-sOutputFile=$output" "$input_" "$pdfmark.txt"
```

- parameters
  - `$input_`: input filename
  - `$output`: output filename
  - `$pdfmark`: a filename without extension, referring to a text file containing the content specified below
- source: <https://github.com/ArtifexSoftware/Ghostscript.NET/issues/117>

For `pdfmark.txt`, see [`GhostScript remove metadata pdfmark.txt`](attachments/GhostScript%20remove%20metadata%20pdfmark.txt):

```pdfmark
[ /Title ()
/Author ()
/Subject ()
/Creator ()
/ModDate ()
/Producer ()
/Keywords ()
/CreationDate ()
/DOCINFO pdfmark
[ /XML ()
/Ext_Metadata pdfmark
```

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
