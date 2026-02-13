---
tags:
  - flashcard/active/general/eng/atmosphere_of_Earth
  - language/in/English
---

# atmosphere of Earth

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## composition

```Python
# pytextgen generate data
from pytextgen.compat import gen, read, util
data: gen.TextCode = gen.seq_to_code((
  fR'[N<sub>2</sub>](nitrogen.md){{{gen.Tag.TEXT}:\: 78.084%}}',
  fR'[O<sub>2</sub>](oxygen.md){{{gen.Tag.TEXT}:\: 20.946%}}',
  fR'[Ar](argon.md){{{gen.Tag.TEXT}:\: 0.9340%}}',
  fR'[CO<sub>2</sub>](carbon%20dioxide.md){{{gen.Tag.TEXT}:\: 0.0417% (2022-04-xx)}}',
  f'{{{gen.Tag.TEXT}:_others_}}{{{gen.Tag.MEMORIZE}:_others_}}{{{Tags.MEMORIZE_LINKED}:_others_}}',),
  index=1,
  prefix=f'{{{Tags.MEMORIZE_LINKED}:_(begin)_}}',
  suffix=f'{{{Tags.MEMORIZE_LINKED}:_(end)_}}',)
sem: gen.TextCode = gen.TextCode.compile(
  '''78.084%{}20.946%{}0.9340%{}0.0417% (2022-04-xx)'''
)
return (
  util.Result(
    location=__env__.cwf_sect('a34f1d'),
    text=gen.quote_text(data),
  ),
  util.Result(
    location=__env__.cwf_sect('123480'),
    text=gen.memorize_linked_seq(data,
      tag='mem lnk',
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('123480')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('1ad236'),
    text=gen.semantics_seq_map(data, sem,
      states=await read.read_flashcard_states(__env__.cwf_sect('1ad236')),
    ),
  ),
)
```

<!--pytextgen generate section="a34f1d"--><!-- The following content is generated at 2023-03-14T22:09:57.723829+08:00. Any edits will be overridden! -->

> 1. [N<sub>2</sub>](nitrogen.md): 78.084%
> 2. [O<sub>2</sub>](oxygen.md): 20.946%
> 3. [Ar](argon.md): 0.9340%
> 4. [CO<sub>2</sub>](carbon%20dioxide.md): 0.0417% (2022-04-xx)
> 5. _others_

<!--/pytextgen-->

<!--pytextgen generate section="123480"--><!-- The following content is generated at 2024-01-04T20:17:51.453474+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[N<sub>2</sub>](nitrogen.md)
- [N<sub>2</sub>](nitrogen.md)→::@::←[O<sub>2</sub>](oxygen.md)
- [O<sub>2</sub>](oxygen.md)→::@::←[Ar](argon.md)
- [Ar](argon.md)→::@::←[CO<sub>2</sub>](carbon%20dioxide.md)
- [CO<sub>2</sub>](carbon%20dioxide.md)→::@::←_others_
- _others_→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="1ad236"--><!-- The following content is generated at 2024-01-04T20:17:51.424468+08:00. Any edits will be overridden! -->

- [N<sub>2</sub>](nitrogen.md):@:78.084%
- [O<sub>2</sub>](oxygen.md):@:20.946%
- [Ar](argon.md):@:0.9340%
- [CO<sub>2</sub>](carbon%20dioxide.md):@:0.0417% (2022-04-xx)

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/atmosphere_of_Earth) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
