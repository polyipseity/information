---
aliases:
  - Buyer Utility Map
  - buyer utility map
tags:
  - flashcard/special/buyer_utility_map
  - language/in/English
---

# buyer utility map

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

It is similar to a {{[customer journey map](customer%20journey%20map.md)}}. <!--SR:!2024-07-02,52,310-->

## 6 stages of buyer experience cycle

The {{6 stages of buyer experience}} cycle are the {{map column headers}}. <!--SR:!2024-05-28,22,259!2024-07-01,48,290-->

%%

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

%%

<!--pytextgen generate section="29ba"--><!-- The following content is generated at 2024-04-22T01:24:34.755556+08:00. Any edits will be overridden! -->

> 1. purchase
> 2. delivery
> 3. use
> 4. supplements
> 5. maintenance
> 6. disposal

<!--/pytextgen-->

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-04-22T01:24:34.779674+08:00. Any edits will be overridden! -->

- _(begin)_→:::←purchase <!--SR:!2024-06-18,40,290!2024-06-20,42,299-->
- purchase→:::←delivery <!--SR:!2024-07-18,65,310!2024-07-06,56,310-->
- delivery→:::←use <!--SR:!2024-07-22,69,310!2024-07-03,53,290-->
- use→:::←supplements <!--SR:!2024-05-30,24,279!2024-07-20,67,319-->
- supplements→:::←maintenance <!--SR:!2024-06-22,42,290!2024-06-14,34,279-->
- maintenance→:::←disposal <!--SR:!2024-07-14,62,310!2024-07-21,69,319-->
- disposal→:::←_(end)_ <!--SR:!2024-07-17,65,319!2024-07-20,68,319-->

<!--/pytextgen-->

## 6 utility levers

The {{6 utility levers}} are the {{map row headers}}. <!--SR:!2024-06-02,27,279!2024-06-12,34,279-->

%%

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

%%

<!--pytextgen generate section="9571"--><!-- The following content is generated at 2024-04-22T01:24:34.815211+08:00. Any edits will be overridden! -->

> 1. convenience: ease of spatial and temporal accessibility
> 2. environmental friendliness
> 3. fun and image: conveyed feel, look, or attitude
> 4. productivity: less effort, time, or money
> 5. risk reduction: financial, physical, reputational
> 6. simplicity: remove complexity or hassle

<!--/pytextgen-->

<!--pytextgen generate section="aa92"--><!-- The following content is generated at 2024-04-22T01:24:34.799107+08:00. Any edits will be overridden! -->

- _(begin)_→:::←convenience: ease of spatial and temporal accessibility <!--SR:!2024-05-28,22,259!2024-07-04,54,310-->
- convenience: ease of spatial and temporal accessibility→:::←environmental friendliness <!--SR:!2024-06-10,32,279!2024-05-15,18,299-->
- environmental friendliness→:::←fun and image: conveyed feel, look, or attitude <!--SR:!2024-05-26,20,259!2024-05-31,17,239-->
- fun and image: conveyed feel, look, or attitude→:::←productivity: less effort, time, or money <!--SR:!2024-05-21,10,239!2024-05-24,18,259-->
- productivity: less effort, time, or money→:::←risk reduction: financial, physical, reputational <!--SR:!2024-05-29,18,250!2024-05-17,13,259-->
- risk reduction: financial, physical, reputational→:::←simplicity: remove complexity or hassle <!--SR:!2024-05-21,8,210!2024-05-26,20,259-->
- simplicity: remove complexity or hassle→:::←_(end)_ <!--SR:!2024-07-03,53,310!2024-06-16,38,299-->

<!--/pytextgen-->

## usage

Mark down {{customer pains with crosses}} on the map. Optionally, mark down {{current industry focuses with red points}}. Then, identify {{new unaddressed customer pains}}. <!--SR:!2024-05-31,25,279!2024-05-21,17,250!2024-06-04,26,270-->