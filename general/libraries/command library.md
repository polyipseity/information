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
