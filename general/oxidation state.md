---
aliases:
  - oxidation number
tags:
  - flashcard/active/general/oxidation_state
  - language/in/English
---

# oxidation state

## simple approach

```Python
# pytextgen generate data
from pytextgen import gen, read, util
data: gen.TextCode = gen.seq_to_code((
    R'element in a free form\: 0',
    R'ionic compound or ion\: _charge_',
    R'fluorine\: -1',
    R'(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine\: -1',
    R'group I metal\: +1',
    R'group II metal\: +2',
    R'metallic hydride\: -1',
    R'hydrogen\: +1',
    R'(if not bonded to oxygen or flourine) oxygen\: -2',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
return (
  util.Result(
    location=__env__.cwf_sect('2d99fe'),
    text=gen.quote_text(data),
  ),
  util.Result(
    location=__env__.cwf_sect('341d9e'),
    text=gen.memorize_linked_seq(data,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('341d9e')),
    ),
  ),
)
```

<!--pytextgen generate section="2d99fe"--><!-- The following content is generated at 2022-11-05T00:25:01.101869+08:00. Any edits will be overridden! -->

> 1. element in a free form: 0
> 2. ionic compound or ion: _charge_
> 3. fluorine: -1
> 4. (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1
> 5. group I metal: +1
> 6. group II metal: +2
> 7. metallic hydride: -1
> 8. hydrogen: +1
> 9. (if not bonded to oxygen or flourine) oxygen: -2

<!--/pytextgen-->

<!--pytextgen generate section="341d9e"--><!-- The following content is generated at 2024-01-04T20:17:52.416402+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←element in a free form: 0 <!--SR:!2024-11-24,560,310!2029-02-20,1796,350-->
- element in a free form: 0→::@::←ionic compound or ion: _charge_ <!--SR:!2025-11-27,764,270!2025-02-21,620,310-->
- ionic compound or ion: _charge_→::@::←fluorine: -1 <!--SR:!2025-11-05,662,250!2026-02-04,496,270-->
- fluorine: -1→::@::←(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1 <!--SR:!2027-05-05,930,230!2025-09-19,714,270-->
- (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1→::@::←group I metal: +1 <!--SR:!2027-08-07,1101,270!2026-03-11,487,210-->
- group I metal: +1→::@::←group II metal: +2 <!--SR:!2027-10-11,1380,330!2026-01-08,892,330-->
- group II metal: +2→::@::←metallic hydride: -1 <!--SR:!2025-01-04,62,190!2024-11-16,197,270-->
- metallic hydride: -1→::@::←hydrogen: +1 <!--SR:!2025-04-16,661,310!2024-12-10,576,310-->
- hydrogen: +1→::@::←(if not bonded to oxygen or flourine) oxygen: -2 <!--SR:!2025-03-30,541,250!2024-11-23,77,210-->
- (if not bonded to oxygen or flourine) oxygen: -2→::@::←_(end)_ <!--SR:!2026-06-10,610,310!2025-01-08,165,230-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/oxidation_state) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
