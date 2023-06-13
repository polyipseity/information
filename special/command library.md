---
tags:
  - general/libraries
---

# command library

## FFmpeg

### measure loudness

```shell
ffmpeg -i $input -af ebur128=framelog=verbose -f null -
```

- source: https://superuser.com/a/1424365

### transcode to Advanced Audio Coding at transparency

```shell
ffmpeg -i $input -map 0:a -map_metadata 0:s:a -c:a aac -b:a 320000 -movflags +faststart $output.m4a
```

## rsync

### sync

```shell
rsync -avzuk --delete --progress $source $destination
```
