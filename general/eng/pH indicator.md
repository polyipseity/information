---
aliases:
  - pH indicator
  - pH indicators
tags:
  - flashcard/active/general/eng/pH_indicator
  - language/in/English
---

# pH indicator

```Python
# pytextgen generate data
from pytextgen.compat import gen, read, util
import typing
@typing.final
class pHRanges(typing.NamedTuple):
  data: typing.Mapping[str, str]

  @property
  def table(self: typing.Self) -> str:
    return gen.quotette(
      gen.rows_to_table(self.data.items(),
        names=('pH', 'color',),
        values=util.identity,),
      prefix='> ',
    )

  @property
  def mem_ranges(self: typing.Self) -> gen.TextCode:
    return gen.seq_to_code(self.data.keys(),
      index=1,
      prefix=f'{{{gen.Tag.MEMORIZE}:_(acidic)_}}',
      suffix=f'{{{gen.Tag.MEMORIZE}:_(basic)_}}',
      escape=True,)

  @property
  def mem_map(self: typing.Self) -> gen.TextCode:
    return gen.two_columns_to_code(self.data.items(),
      left=lambda item: gen.TextCode.escape(item[0]),
      right=lambda item: gen.TextCode.escape(item[1]),)
methyl_orange: pHRanges = pHRanges({
  '~3.1': '<span style="color: red;">red</span>',
  '3.1~4.4': '<span style="color: orange;">orange</span>',
  '4.4~': '<span style="color: yellow; background-color: black;">yellow</span>',
})
litmus: pHRanges = pHRanges({
  '~5': '<span style="color: red;">red</span>',
  '5~8': '<span style="color: purple; background-color: white;">purple</span>',
  '8~': '<span style="color: blue; background-color: white;">blue</span>',
})
phenolphthalein: pHRanges = pHRanges({
  '~8.3': 'colorless',
  '8.3~10': '<span style="color: lightPink;">very pale pink</span>',
  '10~': '<span style="color: pink;">pink</span>',
})

return (
  util.Result(
    location=__env__.cwf_sect('a9208f'),
    text=methyl_orange.table,
  ),
  util.Result(
    location=__env__.cwf_sect('d82740'),
    text=gen.memorize_linked_seq(methyl_orange.mem_ranges,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('d82740')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('1389d0'),
    text=gen.memorize_two_sided(methyl_orange.mem_map,
      states=await read.read_flashcard_states(__env__.cwf_sect('1389d0')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('2acde1'),
    text=litmus.table,
  ),
  util.Result(
    location=__env__.cwf_sect('f25a99'),
    text=gen.memorize_linked_seq(litmus.mem_ranges,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('f25a99')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('29f820'),
    text=gen.memorize_two_sided(litmus.mem_map,
      states=await read.read_flashcard_states(__env__.cwf_sect('29f820')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('5c8883'),
    text=phenolphthalein.table,
  ),
  util.Result(
    location=__env__.cwf_sect('155d9a'),
    text=gen.memorize_linked_seq(phenolphthalein.mem_ranges,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('155d9a')),
    ),
  ),
  util.Result(
    location=__env__.cwf_sect('0245d8'),
    text=gen.memorize_two_sided(phenolphthalein.mem_map,
      states=await read.read_flashcard_states(__env__.cwf_sect('0245d8')),
    ),
  ),
)
```

## methyl orange

<!--pytextgen generate section="a9208f"--><!-- The following content is generated at 2026-01-25T23:32:19.056387+08:00. Any edits will be overridden! -->

> | pH      | color                                                               |
> | ------- | ------------------------------------------------------------------- |
> | ~3.1    | <span style="color: red;">red</span>                                |
> | 3.1~4.4 | <span style="color: orange;">orange</span>                          |
> | 4.4~    | <span style="color: yellow; background-color: black;">yellow</span> |

<!--/pytextgen-->

<!--pytextgen generate section="d82740"--><!-- The following content is generated at 2024-01-04T20:17:52.374886+08:00. Any edits will be overridden! -->

- _(acidic)_→::@::←~3.1
- ~3.1→::@::←3.1~4.4
- 3.1~4.4→::@::←4.4~
- 4.4~→::@::←_(basic)_

<!--/pytextgen-->

<!--pytextgen generate section="1389d0"--><!-- The following content is generated at 2024-07-07T16:14:39.455963+08:00. Any edits will be overridden! -->

- ~3.1::@::<span style="color: red;">red</span>
- 3.1~4.4::@::<span style="color: orange;">orange</span>
- 4.4~::@::<span style="color: yellow; background-color: black;">yellow</span>

<!--/pytextgen-->

## litmus

<!--pytextgen generate section="2acde1"--><!-- The following content is generated at 2026-01-25T23:32:19.008228+08:00. Any edits will be overridden! -->

> | pH  | color                                                               |
> | --- | ------------------------------------------------------------------- |
> | ~5  | <span style="color: red;">red</span>                                |
> | 5~8 | <span style="color: purple; background-color: white;">purple</span> |
> | 8~  | <span style="color: blue; background-color: white;">blue</span>     |

<!--/pytextgen-->

<!--pytextgen generate section="f25a99"--><!-- The following content is generated at 2024-01-04T20:17:52.407406+08:00. Any edits will be overridden! -->

- _(acidic)_→::@::←~5
- ~5→::@::←5~8
- 5~8→::@::←8~
- 8~→::@::←_(basic)_

<!--/pytextgen-->

<!--pytextgen generate section="29f820"--><!-- The following content is generated at 2024-01-04T20:17:52.498475+08:00. Any edits will be overridden! -->

- ~5::@::<span style="color: red;">red</span>
- 5~8::@::<span style="color: purple; background-color: white;">purple</span>
- 8~::@::<span style="color: blue; background-color: white;">blue</span>

<!--/pytextgen-->

## phenolphthalein

<!--pytextgen generate section="5c8883"--><!-- The following content is generated at 2026-01-25T23:32:19.031797+08:00. Any edits will be overridden! -->

> | pH     | color                                                 |
> | ------ | ----------------------------------------------------- |
> | ~8.3   | colorless                                             |
> | 8.3~10 | <span style="color: lightPink;">very pale pink</span> |
> | 10~    | <span style="color: pink;">pink</span>                |

<!--/pytextgen-->

<!--pytextgen generate section="155d9a"--><!-- The following content is generated at 2024-01-04T20:17:52.334864+08:00. Any edits will be overridden! -->

- _(acidic)_→::@::←~8.3
- ~8.3→::@::←8.3~10
- 8.3~10→::@::←10~
- 10~→::@::←_(basic)_

<!--/pytextgen-->

<!--pytextgen generate section="0245d8"--><!-- The following content is generated at 2024-01-04T20:17:52.306888+08:00. Any edits will be overridden! -->

- ~8.3::@::colorless
- 8.3~10::@::<span style="color: lightPink;">very pale pink</span>
- 10~::@::<span style="color: pink;">pink</span>

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/pH_indicator) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
