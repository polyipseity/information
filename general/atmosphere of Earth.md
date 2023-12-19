---
tags:
  - flashcards/general/atmosphere_of_Earth
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# atmosphere of Earth

## composition

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
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
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a34f1d"--><!-- The following content is generated at 2023-03-14T22:09:57.723829+08:00. Any edits will be overridden! -->

> 1. [N<sub>2</sub>](nitrogen.md): 78.084%
> 2. [O<sub>2</sub>](oxygen.md): 20.946%
> 3. [Ar](argon.md): 0.9340%
> 4. [CO<sub>2</sub>](carbon%20dioxide.md): 0.0417% (2022-04-xx)
> 5. _others_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123480"--><!-- The following content is generated at 2023-03-14T22:09:57.737978+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[N<sub>2</sub>](nitrogen.md) <!--SR:!2024-11-30,670,270!2024-08-30,680,327-->
2. [N<sub>2</sub>](nitrogen.md)→:::←[O<sub>2</sub>](oxygen.md) <!--SR:!2026-02-17,1059,290!2024-03-05,497,267-->
3. [O<sub>2</sub>](oxygen.md)→:::←[Ar](argon.md) <!--SR:!2024-04-29,533,270!2027-07-30,1422,287-->
4. [Ar](argon.md)→:::←[CO<sub>2</sub>](carbon%20dioxide.md) <!--SR:!2027-01-01,1326,310!2025-05-02,765,270-->
5. [CO<sub>2</sub>](carbon%20dioxide.md)→:::←_others_ <!--SR:!2027-05-11,1422,310!2027-05-29,1373,287-->
6. _others_→:::←_(end)_ <!--SR:!2024-10-15,785,345!2024-08-16,725,326-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1ad236"--><!-- The following content is generated at 2023-03-14T22:09:57.767517+08:00. Any edits will be overridden! -->

1. [N<sub>2</sub>](nitrogen.md)::78.084% <!--SR:!2027-02-08,1202,250-->
2. [O<sub>2</sub>](oxygen.md)::20.946% <!--SR:!2024-02-09,153,170-->
3. [Ar](argon.md)::0.9340% <!--SR:!2024-01-22,299,210-->
4. [CO<sub>2</sub>](carbon%20dioxide.md)::0.0417% (2022-04-xx) <!--SR:!2024-04-10,180,167-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
