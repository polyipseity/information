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

It is similar to a {@{[customer journey map](customer%20journey%20map.md)}@}. <!--SR:!2026-10-28,687,330-->

## 6 stages of buyer experience cycle

The {@{6 stages of buyer experience}@} cycle are the {@{map column headers}@}. <!--SR:!2027-07-17,847,299!2025-12-22,400,290-->

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

- _(begin)_→::@::←purchase <!--SR:!2026-02-05,476,310!2025-09-20,263,299-->
- purchase→::@::←delivery <!--SR:!2028-11-06,1278,350!2026-06-29,547,310-->
- delivery→::@::←use <!--SR:!2026-12-12,660,310!2025-09-23,213,270-->
- use→::@::←supplements <!--SR:!2026-04-05,332,279!2029-03-05,1372,359-->
- supplements→::@::←maintenance <!--SR:!2025-10-12,356,290!2028-03-04,1006,299-->
- maintenance→::@::←disposal <!--SR:!2026-06-13,401,310!2028-03-21,1023,339-->
- disposal→::@::←_(end)_ <!--SR:!2029-01-11,1344,359!2029-03-28,1395,359-->

<!--/pytextgen-->

## 6 utility levers

The {@{6 utility levers}@} are the {@{map row headers}@}. <!--SR:!2027-09-01,821,319!2025-06-19,276,279-->

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

- _(begin)_→::@::←convenience: ease of spatial and temporal accessibility <!--SR:!2025-09-20,190,239!2026-12-02,715,330-->
- convenience: ease of spatial and temporal accessibility→::@::←environmental friendliness <!--SR:!2027-12-05,941,299!2026-03-19,467,299-->
- environmental friendliness→::@::←fun and image: conveyed feel, look, or attitude <!--SR:!2025-11-23,358,259!2026-05-19,397,239-->
- fun and image: conveyed feel, look, or attitude→::@::←productivity: less effort, time, or money <!--SR:!2026-01-21,365,239!2025-11-24,325,239-->
- productivity: less effort, time, or money→::@::←risk reduction: financial, physical, reputational <!--SR:!2025-08-16,284,250!2025-06-23,258,259-->
- risk reduction: financial, physical, reputational→::@::←simplicity: remove complexity or hassle <!--SR:!2025-12-17,273,210!2026-01-03,382,259-->
- simplicity: remove complexity or hassle→::@::←_(end)_ <!--SR:!2026-05-02,505,310!2025-09-10,337,299-->

<!--/pytextgen-->

## usage

Mark down {@{customer pains with crosses}@} on the map. Optionally, mark down {@{current industry focuses with red points}@}. Then, identify {@{new unaddressed customer pains}@}. <!--SR:!2025-11-01,418,319!2025-12-20,413,270!2025-10-04,390,310-->
