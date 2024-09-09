---
aliases:
  - Buyer Utility Map
  - buyer utility map
tags:
  - flashcard/active/special/buyer_utility_map
  - language/in/English
---

# buyer utility map

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

It is similar to a {{[customer journey map](customer%20journey%20map.md)}}. <!--SR:!2024-12-09,160,310-->

## 6 stages of buyer experience cycle

The {{6 stages of buyer experience}} cycle are the {{map column headers}}. <!--SR:!2025-03-22,218,279!2024-11-17,138,290-->

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("29ba", "93ab"),
  """
purchase
delivery
use
supplements
maintenance
disposal
""".strip().splitlines(),
)
```

<!--pytextgen generate section="29ba"--><!-- The following content is generated at 2024-04-22T01:24:34.755556+08:00. Any edits will be overridden! -->

> 1. purchase
> 2. delivery
> 3. use
> 4. supplements
> 5. maintenance
> 6. disposal

<!--/pytextgen-->

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-04-22T01:24:34.779674+08:00. Any edits will be overridden! -->

- _(begin)_→:::←purchase <!--SR:!2024-10-11,115,290!2024-10-25,127,299-->
- purchase→:::←delivery <!--SR:!2025-04-28,281,330!2024-12-29,175,310-->
- delivery→:::←use <!--SR:!2025-02-20,213,310!2024-12-05,155,290-->
- use→:::←supplements <!--SR:!2025-02-03,183,279!2025-05-11,294,339-->
- supplements→:::←maintenance <!--SR:!2024-10-21,121,290!2024-09-16,94,279-->
- maintenance→:::←disposal <!--SR:!2025-01-21,191,310!2025-05-19,302,339-->
- disposal→:::←_(end)_ <!--SR:!2025-05-05,288,339!2025-05-16,299,339-->

<!--/pytextgen-->

## 6 utility levers

The {{6 utility levers}} are the {{map row headers}}. <!--SR:!2024-09-14,104,299!2024-09-16,96,279-->

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("9571", "aa92"),
  """
convenience: ease of spatial and temporal accessibility
environmental friendliness
fun and image: conveyed feel, look, or attitude
productivity: less effort, time, or money
risk reduction: financial, physical, reputational
simplicity: remove complexity or hassle
""".strip().splitlines(),
)
```

<!--pytextgen generate section="9571"--><!-- The following content is generated at 2024-04-22T01:24:34.815211+08:00. Any edits will be overridden! -->

> 1. convenience: ease of spatial and temporal accessibility
> 2. environmental friendliness
> 3. fun and image: conveyed feel, look, or attitude
> 4. productivity: less effort, time, or money
> 5. risk reduction: financial, physical, reputational
> 6. simplicity: remove complexity or hassle

<!--/pytextgen-->

<!--pytextgen generate section="aa92"--><!-- The following content is generated at 2024-04-22T01:24:34.799107+08:00. Any edits will be overridden! -->

- _(begin)_→:::←convenience: ease of spatial and temporal accessibility <!--SR:!2024-12-25,151,259!2024-12-17,166,310-->
- convenience: ease of spatial and temporal accessibility→:::←environmental friendliness <!--SR:!2025-05-05,242,279!2024-12-07,155,299-->
- environmental friendliness→:::←fun and image: conveyed feel, look, or attitude <!--SR:!2024-11-29,136,259!2024-11-05,68,239-->
- fun and image: conveyed feel, look, or attitude→:::←productivity: less effort, time, or money <!--SR:!2025-01-18,152,239!2025-01-03,134,239-->
- productivity: less effort, time, or money→:::←risk reduction: financial, physical, reputational <!--SR:!2024-11-05,114,250!2024-10-06,100,259-->
- risk reduction: financial, physical, reputational→:::←simplicity: remove complexity or hassle <!--SR:!2024-09-14,28,210!2024-12-15,147,259-->
- simplicity: remove complexity or hassle→:::←_(end)_ <!--SR:!2024-12-13,163,310!2024-10-07,113,299-->

<!--/pytextgen-->

## usage

Mark down {{customer pains with crosses}} on the map. Optionally, mark down {{current industry focuses with red points}}. Then, identify {{new unaddressed customer pains}}. <!--SR:!2025-11-01,418,319!2024-11-02,117,250!2025-10-04,390,310-->
