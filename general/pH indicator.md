---
aliases:
  - pH indicator
  - pH indicators
tags:
  - flashcards/general/pH_indicator
  - languages/in/English
---

# pH indicator

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
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
  '4.4~': '<span style="color: yellow;">yellow</span>',
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
%%

## methyl orange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9208f"--><!-- The following content is generated at 2023-08-01T10:43:41.600103+08:00. Any edits will be overridden! -->

> | pH | color |
> |-|-|
> | ~3.1 | <span style="color: red;">red</span> |
> | 3.1~4.4 | <span style="color: orange;">orange</span> |
> | 4.4~ | <span style="color: yellow;">yellow</span> |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d82740"--><!-- The following content is generated at 2023-08-01T10:43:41.495632+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←~3.1 <!--SR:!2024-03-19,316,261!2027-09-11,1369,341-->
2. ~3.1→:::←3.1~4.4 <!--SR:!2024-01-05,309,281!2027-07-28,1309,321-->
3. 3.1~4.4→:::←4.4~ <!--SR:!2025-03-27,641,301!2025-05-01,618,261-->
4. 4.4~→:::←_(basic)_ <!--SR:!2027-09-27,1382,341!2024-05-04,376,261-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1389d0"--><!-- The following content is generated at 2023-08-01T10:43:41.571798+08:00. Any edits will be overridden! -->

1. ~3.1:::<span style="color: red;">red</span> <!--SR:!2025-07-03,814,270!2025-10-28,844,250-->
2. 3.1~4.4:::<span style="color: orange;">orange</span> <!--SR:!2027-02-04,1210,270!2025-12-15,881,250-->
3. 4.4~:::<span style="color: yellow;">yellow</span> <!--SR:!2025-02-10,584,250!2024-07-06,250,190-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## litmus

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2acde1"--><!-- The following content is generated at 2023-08-01T10:43:41.619622+08:00. Any edits will be overridden! -->

> | pH | color |
> |-|-|
> | ~5 | <span style="color: red;">red</span> |
> | 5~8 | <span style="color: purple; background-color: white;">purple</span> |
> | 8~ | <span style="color: blue; background-color: white;">blue</span> |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f25a99"--><!-- The following content is generated at 2023-08-01T10:43:41.514215+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←~5 <!--SR:!2024-07-22,442,281!2024-02-02,351,321-->
2. ~5→:::←5~8 <!--SR:!2024-05-04,389,281!2025-06-12,724,321-->
3. 5~8→:::←8~ <!--SR:!2027-07-23,1305,321!2024-03-15,318,261-->
4. 8~→:::←_(basic)_ <!--SR:!2026-04-03,931,321!2024-11-04,516,281-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29f820"--><!-- The following content is generated at 2023-08-01T10:43:41.532759+08:00. Any edits will be overridden! -->

1. ~5:::<span style="color: red;">red</span> <!--SR:!2026-05-11,1063,290!2026-10-31,1141,270-->
2. 5~8:::<span style="color: purple; background-color: white;">purple</span> <!--SR:!2024-10-04,553,250!2025-10-29,845,250-->
3. 8~:::<span style="color: blue; background-color: white;">blue</span> <!--SR:!2026-02-06,999,290!2025-02-20,517,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## phenolphthalein

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5c8883"--><!-- The following content is generated at 2023-08-01T10:43:41.457564+08:00. Any edits will be overridden! -->

> | pH | color |
> |-|-|
> | ~8.3 | colorless |
> | 8.3~10 | <span style="color: lightPink;">very pale pink</span> |
> | 10~ | <span style="color: pink;">pink</span> |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="155d9a"--><!-- The following content is generated at 2023-08-01T10:43:41.553255+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←~8.3 <!--SR:!2025-04-10,524,241!2024-01-12,334,321-->
2. ~8.3→:::←8.3~10 <!--SR:!2024-12-23,553,281!2025-06-28,704,301-->
3. 8.3~10→:::←10~ <!--SR:!2026-02-19,833,301!2026-02-04,796,261-->
4. 10~→:::←_(basic)_ <!--SR:!2024-02-01,350,321!2024-12-18,548,281-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0245d8"--><!-- The following content is generated at 2023-08-01T10:43:41.476107+08:00. Any edits will be overridden! -->

1. ~8.3:::colorless <!--SR:!2024-04-13,349,230!2024-06-09,343,230-->
2. 8.3~10:::<span style="color: lightPink;">very pale pink</span> <!--SR:!2026-04-27,906,250!2024-09-28,357,210-->
3. 10~:::<span style="color: pink;">pink</span> <!--SR:!2024-05-03,391,250!2024-02-15,455,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/pH_indicator) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
