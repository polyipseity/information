---
aliases:
  - spectral color
  - spectral colors
tags:
  - flashcards/general/spectral_color
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# spectral color

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
e = __env__
headers = ("[color](color.md)", "[wavelength](wavelength.md) ([nm](nanometer.md))", "[frequency](frequency.md) ([THz](hertz.md))", "[photon energy](photon%20energy.md) ([eV](electronvolt.md))",)
table = (
  (f"{colored_block("#7f00ff")} [violet](violet%20(color).md)", "380–450", "670–790", "2.75–3.26",),
  (f"{colored_block("blue")} [blue](blue.md)", "450–485", "620–670", "2.56–2.75",),
  (f"{colored_block("cyan")} [cyan](cyan.md)", "485–500", "600–620", "2.48–2.56",),
  (f"{colored_block("#00ff00")} [green](green.md)", "500–565", "530–600", "2.19–2.48",),
  (f"{colored_block("yellow")} [yellow](yellow.md)", "565–590", "510–530", "2.10–2.19",),
  (f"{colored_block("orange")} [orange](orange%20(color).md)", "590–625", "480–510", "1.98–2.10",),
  (f"{colored_block("red")} [red](red.md)", "625–750", "400–480", "1.65–1.98",),
)
return _chain.from_iterable(await _gather(
  memorize_table(e.cwf_sects("d951", "5861",), headers, table,),
  memorize_map(
    e.cwf_sects(None, "948f", "679d",),
    items_to_map(*(entry[:2] for entry in table)),
  ),
  memorize_map(
    e.cwf_sects(None, "da12", "3349",),
    items_to_map(*((entry[0], entry[2]) for entry in table)),
  ),
  memorize_map(
    e.cwf_sects(None, "5680", "e224",),
    items_to_map(*((entry[0], entry[3]) for entry in table)),
  ),
))
```
%%

The spectral colors have a range of {{[wavelength](wavelength.md) 380–750 [nm](nanometer.md), [frequency](frequency.md) 790–400 [THz](hertz.md), and [photon energy](photon%20energy.md) 3.26–1.65 [eV](electronvolt.md)}}. These values are {{approximations as the spectrum is continuous without clear boundaries}}. <!--SR:!2024-02-09,140,210!2025-06-12,587,330-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d951"--><!-- The following content is generated at 2023-11-26T19:27:40.284980+08:00. Any edits will be overridden! -->

> | [color](color.md) | [wavelength](wavelength.md) ([nm](nanometer.md)) | [frequency](frequency.md) ([THz](hertz.md)) | [photon energy](photon%20energy.md) ([eV](electronvolt.md)) |
> |-|-|-|-|
> | <span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md) | 380–450 | 670–790 | 2.75–3.26 |
> | <span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md) | 450–485 | 620–670 | 2.56–2.75 |
> | <span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md) | 485–500 | 600–620 | 2.48–2.56 |
> | <span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md) | 500–565 | 530–600 | 2.19–2.48 |
> | <span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md) | 565–590 | 510–530 | 2.10–2.19 |
> | <span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md) | 590–625 | 480–510 | 1.98–2.10 |
> | <span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md) | 625–750 | 400–480 | 1.65–1.98 |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5861"--><!-- The following content is generated at 2023-05-06T22:44:42.700045+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←<span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md) <!--SR:!2025-06-03,578,330!2025-06-07,582,330-->
2. <span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md)→:::←<span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md) <!--SR:!2025-05-25,569,330!2025-06-28,600,330-->
3. <span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md)→:::←<span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md) <!--SR:!2024-06-08,273,290!2024-09-28,385,310-->
4. <span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md)→:::←<span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md) <!--SR:!2024-02-07,187,290!2024-07-03,311,290-->
5. <span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md)→:::←<span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md) <!--SR:!2024-12-25,418,310!2025-05-26,570,330-->
6. <span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md)→:::←<span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md) <!--SR:!2025-06-07,582,330!2025-06-17,591,330-->
7. <span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md)→:::←<span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md) <!--SR:!2025-05-20,564,330!2025-05-23,567,330-->
8. <span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md)→:::←_(end)_ <!--SR:!2024-02-26,223,310!2025-06-23,595,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### color–wavelength (nm)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="948f"--><!-- The following content is generated at 2023-11-26T19:27:40.574202+08:00. Any edits will be overridden! -->

1. <span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md)::380–450 <!--SR:!2024-01-04,18,170-->
2. <span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md)::450–485 <!--SR:!2024-01-07,32,190-->
3. <span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md)::485–500 <!--SR:!2023-12-22,6,130-->
4. <span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md)::500–565 <!--SR:!2023-12-19,15,130-->
5. <span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md)::565–590 <!--SR:!2023-12-26,18,170-->
6. <span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md)::590–625 <!--SR:!2024-01-31,50,170-->
7. <span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md)::625–750 <!--SR:!2024-07-07,247,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="679d"--><!-- The following content is generated at 2023-11-26T19:27:40.397727+08:00. Any edits will be overridden! -->

1. 380–450::<span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md) <!--SR:!2024-01-15,34,303-->
2. 450–485::<span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md) <!--SR:!2023-12-20,13,243-->
3. 485–500::<span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md) <!--SR:!2023-12-19,7,203-->
4. 500–565::<span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md) <!--SR:!2024-01-14,28,243-->
5. 565–590::<span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md) <!--SR:!2023-12-23,11,223-->
6. 590–625::<span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md) <!--SR:!2023-12-25,9,243-->
7. 625–750::<span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md) <!--SR:!2024-01-24,42,303-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### color–frequency (THz)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="da12"--><!-- The following content is generated at 2023-11-27T11:23:41.750922+08:00. Any edits will be overridden! -->

1. <span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md)::670–790 <!--SR:!2023-12-23,17,150-->
2. <span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md)::620–670 <!--SR:!2023-12-20,3,150-->
3. <span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md)::600–620 <!--SR:!2023-12-18,1,130-->
4. <span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md)::530–600 <!--SR:!2024-01-08,24,210-->
5. <span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md)::510–530 <!--SR:!2023-12-18,2,130-->
6. <span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md)::480–510 <!--SR:!2024-01-10,39,190-->
7. <span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md)::400–480 <!--SR:!2023-12-26,53,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3349"--><!-- The following content is generated at 2023-11-27T11:23:41.710466+08:00. Any edits will be overridden! -->

1. 670–790::<span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md) <!--SR:!2024-01-19,36,283-->
2. 620–670::<span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md) <!--SR:!2024-01-12,31,283-->
3. 600–620::<span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md) <!--SR:!2024-01-08,24,243-->
4. 530–600::<span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md) <!--SR:!2023-12-18,11,243-->
5. 510–530::<span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md) <!--SR:!2023-12-20,8,203-->
6. 480–510::<span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md) <!--SR:!2023-12-19,7,183-->
7. 400–480::<span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md) <!--SR:!2024-01-06,25,263-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### color–photon energy (eV)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5680"--><!-- The following content is generated at 2023-11-27T11:23:41.775044+08:00. Any edits will be overridden! -->

1. <span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md)::2.75–3.26 <!--SR:!2024-02-08,131,230-->
2. <span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md)::2.56–2.75 <!--SR:!2023-12-22,10,130-->
3. <span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md)::2.48–2.56 <!--SR:!2024-05-01,180,210-->
4. <span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md)::2.19–2.48 <!--SR:!2023-12-25,23,150-->
5. <span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md)::2.10–2.19 <!--SR:!2024-01-02,80,230-->
6. <span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md)::1.98–2.10 <!--SR:!2024-01-15,42,210-->
7. <span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md)::1.65–1.98 <!--SR:!2024-02-02,51,130-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="e224"--><!-- The following content is generated at 2023-11-27T11:23:41.729899+08:00. Any edits will be overridden! -->

1. 2.75–3.26::<span style="background-color:#7f00ff;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [violet](violet%20(color).md) <!--SR:!2024-01-23,41,303-->
2. 2.56–2.75::<span style="background-color:blue;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [blue](blue.md) <!--SR:!2023-12-23,16,263-->
3. 2.48–2.56::<span style="background-color:cyan;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [cyan](cyan.md) <!--SR:!2024-01-04,23,263-->
4. 2.19–2.48::<span style="background-color:#00ff00;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [green](green.md) <!--SR:!2024-01-03,21,243-->
5. 2.10–2.19::<span style="background-color:yellow;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [yellow](yellow.md) <!--SR:!2024-01-04,19,223-->
6. 1.98–2.10::<span style="background-color:orange;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [orange](orange%20(color).md) <!--SR:!2023-12-19,12,243-->
7. 1.65–1.98::<span style="background-color:red;border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span> [red](red.md) <!--SR:!2024-01-28,46,303-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
